import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative, resolve } from 'node:path';
import ts from 'typescript';

const repositoryRoot = resolve(import.meta.dirname, '..');
const workspaceRoots = ['apps', 'packages', 'tools'];
const packageManifests = [];

for (const root of workspaceRoots) {
  const absoluteRoot = join(repositoryRoot, root);
  for (const entry of readdirSync(absoluteRoot)) {
    const manifestPath = join(absoluteRoot, entry, 'package.json');
    try {
      if (statSync(manifestPath).isFile()) {
        packageManifests.push(manifestPath);
      }
    } catch {
      // A non-workspace directory is ignored deliberately.
    }
  }
}

const packages = new Map();
for (const manifestPath of packageManifests) {
  const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
  if (packages.has(manifest.name)) {
    throw new Error(`Duplicate workspace package name: ${manifest.name}`);
  }
  packages.set(manifest.name, { manifest, manifestPath });
}

const allowedInternalDependencies = new Map([
  ['@ufuq/astronomy-core', new Set()],
  ['@ufuq/assessment-core', new Set(['@ufuq/astronomy-core'])],
  ['@ufuq/bkt-core', new Set()],
  ['@ufuq/adaptive-policy', new Set(['@ufuq/bkt-core'])],
  ['@ufuq/contracts', new Set()],
  ['@ufuq/star-data', new Set()],
  ['@ufuq/catalogue-schema', new Set(['@ufuq/star-data'])],
  [
    '@ufuq/tutoring-core',
    new Set(['@ufuq/assessment-core', '@ufuq/bkt-core', '@ufuq/adaptive-policy']),
  ],
  ['@ufuq/astronomy-reference', new Set(['@ufuq/astronomy-core'])],
  ['@ufuq/catalogue-pipeline', new Set(['@ufuq/catalogue-schema', '@ufuq/star-data'])],
  ['@ufuq/catalogue', new Set(['@ufuq/catalogue-pipeline'])],
  ['@ufuq/api', new Set(['@ufuq/contracts'])],
  ['@ufuq/web', new Set(['@ufuq/contracts'])],
]);

const graph = new Map();
const errors = [];
const purePackageNames = new Set([
  '@ufuq/astronomy-core',
  '@ufuq/assessment-core',
  '@ufuq/bkt-core',
  '@ufuq/adaptive-policy',
  '@ufuq/tutoring-core',
  '@ufuq/contracts',
  '@ufuq/star-data',
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
        errors.push(
          `${name} may not declare framework or persistence dependency ${dependency} (${relative(repositoryRoot, manifestPath)}).`,
        );
      }
    }
  }
}

const visiting = new Set();
const visited = new Set();
const path = [];

function visit(name) {
  if (visiting.has(name)) {
    const cycleStart = path.indexOf(name);
    errors.push(`Workspace dependency cycle: ${[...path.slice(cycleStart), name].join(' -> ')}`);
    return;
  }
  if (visited.has(name)) return;
  visiting.add(name);
  path.push(name);
  for (const dependency of graph.get(name) ?? []) visit(dependency);
  path.pop();
  visiting.delete(name);
  visited.add(name);
}

for (const name of graph.keys()) visit(name);

const purePackages = [
  'astronomy-core',
  'assessment-core',
  'bkt-core',
  'adaptive-policy',
  'tutoring-core',
  'contracts',
  'star-data',
  'catalogue-schema',
];
const forbiddenImport =
  /(?:from\s+|import\s*\()['"](?:react(?:\/|['"])|react-dom(?:\/|['"])|three(?:\/|['"])|@react-three\/fiber|express(?:\/|['"])|mysql2?(?:\/|['"])|pg(?:\/|['"])|postgres(?:\/|['"])|sequelize(?:\/|['"])|typeorm(?:\/|['"])|knex(?:\/|['"])|better-sqlite3(?:\/|['"])|sqlite3(?:\/|['"])|@prisma\/client|drizzle-orm(?:\/|['"])|@ufuq\/(?:web|api))/;

function sourceFiles(directory) {
  const results = [];
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) results.push(...sourceFiles(path));
    else if (/\.tsx?$/.test(entry.name)) results.push(path);
  }
  return results;
}

for (const packageDirectory of purePackages) {
  const src = join(repositoryRoot, 'packages', packageDirectory, 'src');
  for (const sourceFile of sourceFiles(src)) {
    const source = readFileSync(sourceFile, 'utf8');
    if (forbiddenImport.test(source)) {
      errors.push(
        `Forbidden framework/application import in ${relative(repositoryRoot, sourceFile)}.`,
      );
    }
  }
}

for (const typeOnlyPackage of ['contracts', 'star-data', 'catalogue-schema']) {
  const src = join(repositoryRoot, 'packages', typeOnlyPackage, 'src');
  for (const sourceFile of sourceFiles(src)) {
    const source = readFileSync(sourceFile, 'utf8');
    const syntaxTree = ts.createSourceFile(sourceFile, source, ts.ScriptTarget.Latest, true);
    for (const statement of syntaxTree.statements) {
      const isTypeOnlyDeclaration =
        ts.isInterfaceDeclaration(statement) ||
        ts.isTypeAliasDeclaration(statement) ||
        (ts.isImportDeclaration(statement) && statement.importClause?.isTypeOnly === true) ||
        (ts.isExportDeclaration(statement) && statement.isTypeOnly);
      if (!isTypeOnlyDeclaration) {
        errors.push(
          `Runtime statement is forbidden in type-only package: ${relative(repositoryRoot, sourceFile)}.`,
        );
      }
    }
  }
}

if (errors.length > 0) {
  console.error(errors.join('\n'));
  process.exitCode = 1;
} else {
  console.log(
    `Boundary check passed for ${packages.size} workspaces; dependency graph is acyclic.`,
  );
}
