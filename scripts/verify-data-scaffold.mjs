import { createHash } from 'node:crypto';
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, resolve } from 'node:path';

const repositoryRoot = resolve(import.meta.dirname, '..');
const scaffoldDirectories = new Map([
  ['data/manifests', new Set(['README.md', 'gaia-dr3-hip-screen-v1'])],
  [
    'data/manifests/gaia-dr3-hip-screen-v1',
    new Set([
      'README.md',
      'acquisition-manifest.v1.json',
      'best-neighbour-source.v1.adql',
      'neighbourhood.v1.adql',
      'tap-schema.v1.adql',
    ]),
  ],
  ['data/curation/patterns', new Set(['README.md'])],
  ['data/curation/relationships', new Set(['README.md'])],
  ['data/curation/routes', new Set(['README.md'])],
  ['data/generated', new Set(['README.md'])],
]);
const errors = [];
const rawDirectory = 'data/raw';
let localGaiaResponseStatus = 'absent; original response bytes were not verified';

function sha256(path) {
  return createHash('sha256').update(readFileSync(path)).digest('hex');
}

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

const gaiaManifestPath = join(
  repositoryRoot,
  'data/manifests/gaia-dr3-hip-screen-v1/acquisition-manifest.v1.json',
);
let gaiaManifest;
try {
  gaiaManifest = JSON.parse(readFileSync(gaiaManifestPath, 'utf8'));
} catch (error) {
  errors.push(`Cannot parse Gaia query evidence manifest: ${error.message}`);
}

if (gaiaManifest) {
  const expectedHipIds = [
    746, 3179, 4427, 6686, 8886, 11767, 53910, 54061, 58001, 59774, 62956, 65378, 67301, 72607,
    75097, 77055, 79822, 82080, 85822,
  ];
  const expectedQueryPaths = [
    'data/manifests/gaia-dr3-hip-screen-v1/best-neighbour-source.v1.adql',
    'data/manifests/gaia-dr3-hip-screen-v1/neighbourhood.v1.adql',
    'data/manifests/gaia-dr3-hip-screen-v1/tap-schema.v1.adql',
  ];

  if (
    gaiaManifest.manifestType !== 'UFUQ_GAIA_TAP_QUERY_EVIDENCE_MANIFEST' ||
    gaiaManifest.schemaVersion !== 1
  ) {
    errors.push('Gaia query evidence manifest type/version is not the approved V1 contract');
  }
  if (gaiaManifest.authorityStatus !== 'QUERY_EVIDENCE_VERIFIED') {
    errors.push('Gaia query evidence manifest has an unexpected authority status');
  }
  if (gaiaManifest.rowScientificApproval !== 'NONE') {
    errors.push('Gaia query evidence must not approve scientific rows');
  }
  if (gaiaManifest.canonicalExtraction?.status !== 'NOT_PRODUCED') {
    errors.push('Milestone 2D.1B must not contain a canonical scientific row extraction');
  }
  if (
    gaiaManifest.release?.datasetVersion !== '1.1' ||
    gaiaManifest.release?.schema !== 'gaiadr3' ||
    gaiaManifest.service?.syncUrl !== 'https://gea.esac.esa.int/tap-server/tap/sync'
  ) {
    errors.push('Gaia query evidence is not pinned to the approved DR3 V1.1 TAP boundary');
  }
  if (
    JSON.stringify(gaiaManifest.queryConstruction?.candidateHipIds) !==
    JSON.stringify(expectedHipIds)
  ) {
    errors.push('Gaia query evidence candidate HIP set or ordering changed');
  }

  const manifestQueries = gaiaManifest.queryConstruction?.queries ?? [];
  if (
    JSON.stringify(manifestQueries.map((query) => query.path)) !==
    JSON.stringify(expectedQueryPaths)
  ) {
    errors.push('Gaia query evidence must contain exactly the three approved query files');
  }

  for (const query of manifestQueries) {
    if (!query.path.startsWith('data/manifests/gaia-dr3-hip-screen-v1/')) {
      errors.push(`Gaia query path escapes its tracked evidence directory: ${query.path}`);
      continue;
    }
    const absolutePath = join(repositoryRoot, query.path);
    if (!existsSync(absolutePath)) {
      errors.push(`Missing tracked Gaia query: ${query.path}`);
      continue;
    }
    const byteLength = statSync(absolutePath).size;
    const digest = sha256(absolutePath);
    if (byteLength !== query.byteLength || digest !== query.sha256) {
      errors.push(`Tracked Gaia query identity mismatch: ${query.path}`);
    }
  }

  const rawFiles = gaiaManifest.rawEvidence?.files ?? [];
  if (
    gaiaManifest.rawEvidence?.repositoryPolicy !== 'IGNORED_LOCAL_ONLY_RIGHTS_REVIEW_PENDING' ||
    rawFiles.length !== 10
  ) {
    errors.push('Gaia response evidence must remain the complete ten-file ignored local set');
  }
  if (
    gaiaManifest.structuralResults?.candidateCount !== 19 ||
    gaiaManifest.structuralResults?.bestNeighbourRowCount !== 8 ||
    gaiaManifest.structuralResults?.neighbourhoodRowCount !== 8
  ) {
    errors.push('Gaia query evidence structural inventory changed without a new version');
  }
  const rawPresence = rawFiles.map((file) => existsSync(join(repositoryRoot, file.path)));
  const presentRawCount = rawPresence.filter(Boolean).length;
  if (presentRawCount > 0 && presentRawCount !== rawFiles.length) {
    errors.push(
      `Local Gaia query evidence is incomplete: ${presentRawCount}/${rawFiles.length} files present`,
    );
  }
  if (presentRawCount === rawFiles.length) {
    localGaiaResponseStatus = 'complete and byte/hash verified';
    for (const file of rawFiles) {
      if (!file.path.startsWith('data/raw/')) {
        errors.push(`Gaia raw evidence path escapes data/raw: ${file.path}`);
        continue;
      }
      const absolutePath = join(repositoryRoot, file.path);
      const byteLength = statSync(absolutePath).size;
      const digest = sha256(absolutePath);
      if (byteLength !== file.byteLength || digest !== file.sha256) {
        errors.push(`Local Gaia response identity mismatch: ${file.path}`);
      }
    }

    const responseColumnChecks = new Map([
      ['best-neighbour-source.csv', gaiaManifest.responseColumns?.bestNeighbourSource],
      ['neighbourhood.csv', gaiaManifest.responseColumns?.neighbourhood],
      ['tap-schema.csv', gaiaManifest.responseColumns?.tapSchema],
    ]);
    for (const [filename, expectedColumns] of responseColumnChecks) {
      const file = rawFiles.find((candidate) => candidate.path.endsWith(`/${filename}`));
      if (!file || !Array.isArray(expectedColumns)) {
        errors.push(`Gaia response-column evidence is incomplete for ${filename}`);
        continue;
      }
      const header = readFileSync(join(repositoryRoot, file.path), 'utf8').split(/\r?\n/, 1)[0];
      if (JSON.stringify(header.split(',')) !== JSON.stringify(expectedColumns)) {
        errors.push(`Gaia response columns do not match the raw CSV header: ${filename}`);
      }
    }
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
    `Data boundary verified: the Gaia query manifest and tracked query hashes are intact; local Gaia response set ${localGaiaResponseStatus}; curation and generated data remain placeholders; local raw data is ignored and untracked.`,
  );
}
