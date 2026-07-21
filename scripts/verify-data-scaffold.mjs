import { readdirSync } from 'node:fs';
import { join, resolve } from 'node:path';

const repositoryRoot = resolve(import.meta.dirname, '..');
const scaffoldDataDirectories = ['data/sources', 'data/curation', 'data/generated'];
const errors = [];

for (const directory of scaffoldDataDirectories) {
  const entries = readdirSync(join(repositoryRoot, directory));
  const unexpected = entries.filter((entry) => entry !== 'README.md');
  if (unexpected.length > 0) {
    errors.push(`${directory} contains non-scaffold files: ${unexpected.join(', ')}`);
  }
}

if (errors.length > 0) {
  console.error(errors.join('\n'));
  process.exitCode = 1;
} else {
  console.log(
    'Data scaffold verified: no catalogue rows, cultural records, or generated data exist.',
  );
}
