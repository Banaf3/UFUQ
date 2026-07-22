import { readFileSync } from 'node:fs';
import { access } from 'node:fs/promises';
import { join, resolve } from 'node:path';

const repositoryRoot = resolve(import.meta.dirname, '..');
const importableWorkspaceDirectories = [
  'apps/api',
  'packages/astronomy-core',
  'packages/assessment-core',
  'packages/tutoring-core',
  'packages/contracts',
  'packages/catalogue-schema',
  'tools/catalogue',
];
const errors = [];
let checkedExports = 0;

for (const directory of importableWorkspaceDirectories) {
  const manifest = JSON.parse(
    readFileSync(join(repositoryRoot, directory, 'package.json'), 'utf8'),
  );
  const exportMap =
    typeof manifest.exports === 'string' ? { '.': manifest.exports } : (manifest.exports ?? {});

  for (const [subpath, exportValue] of Object.entries(exportMap)) {
    const runtimeTarget =
      typeof exportValue === 'string' ? exportValue : (exportValue.default ?? exportValue.import);
    const typeTarget = typeof exportValue === 'object' ? exportValue.types : undefined;
    const publicSpecifier =
      subpath === '.' ? manifest.name : `${manifest.name}/${subpath.slice(2)}`;

    if (!runtimeTarget) {
      errors.push(`${publicSpecifier} has no runtime export target.`);
      continue;
    }
    try {
      await access(join(repositoryRoot, directory, runtimeTarget));
      await import(publicSpecifier);
      checkedExports += 1;
    } catch (error) {
      errors.push(`${publicSpecifier} does not resolve: ${String(error)}`);
    }
    if (typeTarget) {
      try {
        await access(join(repositoryRoot, directory, typeTarget));
      } catch (error) {
        errors.push(`${publicSpecifier} type export does not resolve: ${String(error)}`);
      }
    }
  }
}

if (errors.length > 0) {
  console.error(errors.join('\n'));
  process.exitCode = 1;
} else {
  console.log(`Resolved ${checkedExports} public exports across 7 importable workspaces.`);
}
