import { readFileSync, readdirSync, statSync } from 'node:fs';
import { builtinModules } from 'node:module';
import { dirname, join, relative, resolve, sep } from 'node:path';
import ts from 'typescript';

const repositoryRoot = resolve(import.meta.dirname, '..');
const expectedWorkspaceDirectories = [
  'apps/web',
  'apps/api',
  'packages/astronomy-core',
  'packages/assessment-core',
  'packages/tutoring-core',
  'packages/contracts',
  'packages/catalogue-schema',
  'tools/catalogue',
];
const errors = [];

const rootManifest = JSON.parse(readFileSync(join(repositoryRoot, 'package.json'), 'utf8'));
if (JSON.stringify(rootManifest.workspaces) !== JSON.stringify(expectedWorkspaceDirectories)) {
  errors.push('Root workspaces must be the approved eight explicit directories in approved order.');
}

const discoveredManifestDirectories = [];
for (const parent of ['apps', 'packages', 'tools']) {
  for (const entry of readdirSync(join(repositoryRoot, parent), { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const manifestPath = join(repositoryRoot, parent, entry.name, 'package.json');
    try {
      if (statSync(manifestPath).isFile()) {
        discoveredManifestDirectories.push(`${parent}/${entry.name}`);
      }
    } catch {
      // Directories without npm manifests are intentionally outside the workspace graph.
    }
  }
}

const expectedSet = new Set(expectedWorkspaceDirectories);
for (const directory of discoveredManifestDirectories) {
  if (!expectedSet.has(directory)) errors.push(`Unexpected npm workspace manifest: ${directory}.`);
}
for (const directory of expectedWorkspaceDirectories) {
  if (!discoveredManifestDirectories.includes(directory)) {
    errors.push(`Missing npm workspace manifest: ${directory}.`);
  }
}

const packages = new Map();
for (const directory of expectedWorkspaceDirectories) {
  const manifestPath = join(repositoryRoot, directory, 'package.json');
  const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
  if (packages.has(manifest.name)) errors.push(`Duplicate workspace name: ${manifest.name}.`);
  packages.set(manifest.name, { directory, manifest, manifestPath });
}

const allowedInternalDependencies = new Map([
  ['@ufuq/astronomy-core', new Set()],
  ['@ufuq/assessment-core', new Set(['@ufuq/astronomy-core'])],
  ['@ufuq/tutoring-core', new Set()],
  ['@ufuq/contracts', new Set()],
  ['@ufuq/catalogue-schema', new Set()],
  [
    '@ufuq/api',
    new Set([
      '@ufuq/contracts',
      '@ufuq/catalogue-schema',
      '@ufuq/astronomy-core',
      '@ufuq/assessment-core',
      '@ufuq/tutoring-core',
    ]),
  ],
  ['@ufuq/web', new Set(['@ufuq/contracts', '@ufuq/catalogue-schema', '@ufuq/astronomy-core'])],
  ['@ufuq/catalogue', new Set(['@ufuq/catalogue-schema'])],
]);

const graph = new Map();
const purePackageNames = new Set([
  '@ufuq/astronomy-core',
  '@ufuq/assessment-core',
  '@ufuq/tutoring-core',
  '@ufuq/contracts',
  '@ufuq/catalogue-schema',
]);
const forbiddenPureDependency =
  /^(?:react|react-dom|three|@react-three\/fiber|express|mysql|mysql2|pg|postgres|sequelize|typeorm|knex|better-sqlite3|sqlite3|@prisma\/client|drizzle-orm)$/;

for (const [name, { manifest, manifestPath }] of packages) {
  const dependencies = {
    ...(manifest.dependencies ?? {}),
    ...(manifest.devDependencies ?? {}),
    ...(manifest.peerDependencies ?? {}),
  };
  const internalDependencies = Object.keys(dependencies).filter((dependency) =>
    packages.has(dependency),
  );
  graph.set(name, internalDependencies);

  const allowed = allowedInternalDependencies.get(name);
  if (!allowed) {
    errors.push(`No boundary policy is defined for ${name}.`);
    continue;
  }
  for (const dependency of internalDependencies) {
    if (!allowed.has(dependency)) {
      errors.push(
        `${name} may not depend on ${dependency} (${relative(repositoryRoot, manifestPath)}).`,
      );
    }
  }
  if (purePackageNames.has(name)) {
    for (const dependency of Object.keys(dependencies)) {
      if (forbiddenPureDependency.test(dependency)) {
        errors.push(`${name} may not declare framework or persistence dependency ${dependency}.`);
      }
    }
  }
}

const visiting = new Set();
const visited = new Set();
const dependencyPath = [];

function visit(name) {
  if (visiting.has(name)) {
    const cycleStart = dependencyPath.indexOf(name);
    errors.push(
      `Workspace dependency cycle: ${[...dependencyPath.slice(cycleStart), name].join(' -> ')}`,
    );
    return;
  }
  if (visited.has(name)) return;
  visiting.add(name);
  dependencyPath.push(name);
  for (const dependency of graph.get(name) ?? []) visit(dependency);
  dependencyPath.pop();
  visiting.delete(name);
  visited.add(name);
}

for (const name of graph.keys()) visit(name);

function sourceFiles(directory) {
  const results = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) results.push(...sourceFiles(path));
    else if (/\.tsx?$/.test(entry.name)) results.push(path);
  }
  return results;
}

function moduleSpecifiers(sourceFile) {
  const source = readFileSync(sourceFile, 'utf8');
  const syntaxTree = ts.createSourceFile(sourceFile, source, ts.ScriptTarget.Latest, true);
  const specifiers = [];

  function inspect(node) {
    if (
      (ts.isImportDeclaration(node) || ts.isExportDeclaration(node)) &&
      node.moduleSpecifier &&
      ts.isStringLiteral(node.moduleSpecifier)
    ) {
      specifiers.push(node.moduleSpecifier.text);
    }
    if (
      ts.isCallExpression(node) &&
      node.expression.kind === ts.SyntaxKind.ImportKeyword &&
      node.arguments[0] &&
      ts.isStringLiteral(node.arguments[0])
    ) {
      specifiers.push(node.arguments[0].text);
    }
    ts.forEachChild(node, inspect);
  }

  inspect(syntaxTree);
  return specifiers;
}

const runtimeWorkspaceEntries = [...packages.values()];
const packageNames = [...packages.keys()].sort((left, right) => right.length - left.length);
const nodeBuiltinSpecifiers = new Set(
  builtinModules.flatMap((moduleName) => [moduleName, `node:${moduleName}`]),
);
const forbiddenPureImport =
  /^(?:node:|react(?:\/|$)|react-dom(?:\/|$)|three(?:\/|$)|@react-three\/fiber(?:\/|$)|express(?:\/|$)|mysql2?(?:\/|$)|pg(?:\/|$)|postgres(?:\/|$)|sequelize(?:\/|$)|typeorm(?:\/|$)|knex(?:\/|$)|better-sqlite3(?:\/|$)|sqlite3(?:\/|$)|@prisma\/client(?:\/|$)|drizzle-orm(?:\/|$)|@ufuq\/(?:web|api|catalogue)(?:\/|$))/;
const forbiddenWebImport = /^@ufuq\/(?:assessment-core|tutoring-core|api|catalogue)(?:\/|$)/;
const privatePackageImport = /^@ufuq\/[^/]+\/(?:src|dist)(?:\/|$)/;

for (const { directory, manifest } of runtimeWorkspaceEntries) {
  const src = join(repositoryRoot, directory, 'src');
  let files;
  try {
    files = sourceFiles(src);
  } catch {
    continue;
  }

  for (const sourceFile of files) {
    for (const specifier of moduleSpecifiers(sourceFile)) {
      const displayPath = relative(repositoryRoot, sourceFile);
      if (
        purePackageNames.has(manifest.name) &&
        (forbiddenPureImport.test(specifier) || nodeBuiltinSpecifiers.has(specifier))
      ) {
        errors.push(`Forbidden import ${specifier} in pure package file ${displayPath}.`);
      }
      if (manifest.name === '@ufuq/web' && forbiddenWebImport.test(specifier)) {
        errors.push(`Forbidden authoritative/tool import ${specifier} in web file ${displayPath}.`);
      }
      if (privatePackageImport.test(specifier)) {
        errors.push(`Private workspace path import ${specifier} in ${displayPath}.`);
      }
      const importedPackage = packageNames.find(
        (packageName) => specifier === packageName || specifier.startsWith(`${packageName}/`),
      );
      if (importedPackage) {
        const allowed = allowedInternalDependencies.get(manifest.name);
        if (!allowed?.has(importedPackage)) {
          errors.push(`Source import ${specifier} is not allowed from ${manifest.name}.`);
        }
        const declaredDependencies = {
          ...(manifest.dependencies ?? {}),
          ...(manifest.devDependencies ?? {}),
          ...(manifest.peerDependencies ?? {}),
        };
        if (!(importedPackage in declaredDependencies)) {
          errors.push(`Source import ${specifier} is undeclared in ${manifest.name}.`);
        }
      }
      if (specifier.startsWith('.')) {
        const resolvedImport = resolve(dirname(sourceFile), specifier);
        const sourceWorkspace = resolve(repositoryRoot, directory);
        const toolsRoot = resolve(repositoryRoot, 'tools');
        if (
          (directory.startsWith('apps/') || directory.startsWith('packages/')) &&
          resolvedImport.startsWith(`${toolsRoot}${sep}`)
        ) {
          errors.push(`Runtime-to-tool relative import ${specifier} in ${displayPath}.`);
        }
        if (
          /(?:^|[\\/])(?:src|dist)(?:[\\/]|$)/.test(specifier) &&
          !resolvedImport.startsWith(`${sourceWorkspace}${sep}`)
        ) {
          errors.push(`Cross-workspace private relative import ${specifier} in ${displayPath}.`);
        }
      }
    }
  }
}

const oracleDirectory = join(repositoryRoot, 'tools', 'astronomy-reference');
for (const file of sourceFiles(join(oracleDirectory, 'src')).filter((path) =>
  path.endsWith('.ts'),
)) {
  errors.push(
    `The Python oracle contains unexpected TypeScript source: ${relative(repositoryRoot, file)}.`,
  );
}
for (const file of readdirSync(oracleDirectory)) {
  if (file === 'package.json' || file === 'tsconfig.json') {
    errors.push(`The independent oracle must not contain ${file}.`);
  }
}
for (const pythonFile of readdirSync(join(oracleDirectory, 'src', 'ufuq_astronomy_reference'))) {
  if (!pythonFile.endsWith('.py')) continue;
  const source = readFileSync(
    join(oracleDirectory, 'src', 'ufuq_astronomy_reference', pythonFile),
    'utf8',
  );
  if (/(?:@ufuq\/|astronomy-core|packages[\\/]astronomy-core)/i.test(source)) {
    errors.push(`Oracle source depends on production astronomy: ${pythonFile}.`);
  }
}

if (errors.length > 0) {
  console.error(errors.join('\n'));
  process.exitCode = 1;
} else {
  console.log(
    'Boundary check passed for 8 workspaces; dependency graph is acyclic; private imports are absent; the oracle is independent.',
  );
}
