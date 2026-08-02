import { existsSync, readdirSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, resolve } from 'node:path';

const repositoryRoot = resolve(import.meta.dirname, '..');
const scaffoldDirectories = new Map([
  ['data/manifests', new Set(['README.md'])],
  ['data/curation/patterns', new Set(['README.md'])],
  ['data/curation/relationships', new Set(['README.md'])],
  ['data/curation/routes', new Set(['README.md'])],
  ['data/generated', new Set(['README.md'])],
]);
const errors = [];
const rawDirectory = 'data/raw';

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

if (!existsSync(join(repositoryRoot, rawDirectory))) {
  errors.push(`Missing scaffold directory: ${rawDirectory}`);
} else {
  const trackedRawFiles = execFileSync('git', ['ls-files', '--', rawDirectory], {
    cwd: repositoryRoot,
    encoding: 'utf8',
  })
    .split(/\r?\n/)
    .filter(Boolean);
  const allowedTrackedRawFiles = new Set(['data/raw/.gitignore', 'data/raw/README.md']);
  const prohibitedTrackedRawFiles = trackedRawFiles.filter(
    (file) => !allowedTrackedRawFiles.has(file),
  );
  if (prohibitedTrackedRawFiles.length > 0) {
    errors.push(`Tracked raw data is prohibited: ${prohibitedTrackedRawFiles.join(', ')}`);
  }

  const unignoredRawFiles = execFileSync(
    'git',
    ['ls-files', '--others', '--exclude-standard', '--', rawDirectory],
    { cwd: repositoryRoot, encoding: 'utf8' },
  )
    .split(/\r?\n/)
    .filter(Boolean);
  if (unignoredRawFiles.length > 0) {
    errors.push(`Unignored raw data is prohibited: ${unignoredRawFiles.join(', ')}`);
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
    'Data scaffold verified: manifests, curation, and generated data are placeholders; local raw data is ignored and untracked.',
  );
}
