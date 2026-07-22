import { existsSync, readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';

const repositoryRoot = resolve(import.meta.dirname, '..');
const scaffoldDirectories = new Map([
  ['data/manifests', new Set(['README.md'])],
  ['data/raw', new Set(['.gitignore', 'README.md'])],
  ['data/curation/patterns', new Set(['README.md'])],
  ['data/curation/relationships', new Set(['README.md'])],
  ['data/curation/routes', new Set(['README.md'])],
  ['data/generated', new Set(['README.md'])],
]);
const errors = [];

for (const [directory, allowedEntries] of scaffoldDirectories) {
  const absoluteDirectory = join(repositoryRoot, directory);
  if (!existsSync(absoluteDirectory)) {
    errors.push(`Missing scaffold directory: ${directory}`);
    continue;
  }
  const unexpected = readdirSync(absoluteDirectory).filter((entry) => !allowedEntries.has(entry));
  if (unexpected.length > 0) {
    errors.push(`${directory} contains non-scaffold files: ${unexpected.join(', ')}`);
  }
}

for (const obsoleteDirectory of ['data/sources']) {
  if (existsSync(join(repositoryRoot, obsoleteDirectory))) {
    errors.push(`Obsolete data directory remains: ${obsoleteDirectory}`);
  }
}

if (errors.length > 0) {
  console.error(errors.join('\n'));
  process.exitCode = 1;
} else {
  console.log(
    'Data scaffold verified: manifests and curation are placeholders; raw and generated data are empty.',
  );
}
