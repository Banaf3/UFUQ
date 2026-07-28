# Implementation status

**Assessment date:** 2026-07-26

The consolidated Phase 0 repository scaffold is validated. It contains health-only web
and API applications, eight npm workspaces, pure empty/type-placeholder production
domain boundaries, pinned tooling, fail-closed suite configurations, boundary checks,
and CI. The independent non-npm Python tool now contains a locked, synthetic-only
Astropy smoke oracle; production TypeScript still contains no astronomy calculation.
The repository contains no catalogue/cultural record, BKT formula,
persistence/authentication behavior, dashboard, or deployment configuration.

## Independent readiness gates

| Gate | Result | Basis |
|---|---|---|
| Repository scaffolding | YES | The consolidated eight-workspace TypeScript monorepo, non-npm oracle boundary, strict compiler/build setup, test discovery, dependency enforcement, lockfile, and CI are validated. |
| Validated celestial-guidance vertical slice | NO | The local I/311 parser contract is defined, but redistribution/deployment, selected-row scientific review, cultural membership/route approval, the production astronomy pipeline/error budget, scenario, and scoring tolerances remain unresolved. |
| Participant study | NO | Participant protocol, ethics applicability/approval, instruments, recruitment, privacy, consent, data handling, and study-ready software remain unresolved or unimplemented. |
| Deployment | NO | Hosting/operations target, production account policy, security/privacy release profile, performance/accessibility baselines, monitoring, and backup/restore evidence remain unresolved or unimplemented. |

READY_FOR_SCAFFOLDING: YES

READY_FOR_VERTICAL_SLICE: NO

READY_FOR_PARTICIPANT_STUDY: NO

READY_FOR_DEPLOYMENT: NO

## Phase 0 reference-study state

The local source library has been studied for current-phase needs without starting the
astronomy/data implementation spike. Tracked outputs now include a reading plan,
twenty-one source-specific dossiers, five cross-source syntheses, a coverage report, and
five project-scoped skills with mandatory-rule traceability.

The source study by itself did not select a catalogue and does not approve a production
astronomy pipeline, schema validator, Kaaba coordinate/datum, numerical tolerance,
cultural mapping, or learner-facing route. The separate project decision below now
selects I/311 only for the Phase 1 local technical spike. A locked synthetic Astropy
environment now closes the environment-compatibility smoke milestone, but it does not
settle production astronomy or source-derived validation. Najdi/regional evidence, a
stable edition for the studied Ibn Qutaybah
claims, exact membership/route evidence, and human Arabic/cultural review remain
required before learner-facing cultural claims.

The official I/311 archive Appendix G now confirms that I/311 `pmRA` is
`mu_alpha_star`; the normalized parser field maps directly to Astropy `pm_ra_cosdec`
after unit conversion. The high-declination omitted/double-cosine astronomy tests
remain required. I/311 states `Ep=1991.25`, but its metadata inspected here does not
separately define the epoch time scale for production propagation.

The detailed evidence boundaries are in `references/PDF_KNOWLEDGE_COVERAGE.md`.

## Phase 1 Milestone 1 decision audit

The documentation-only source, policy, licensing, and performance audit is complete.
It is recorded in `spikes/PHASE1_ASTRONOMY_DATA_SPIKE.md`. No implementation stage has
begun.

CDS I/311, *Hipparcos, the New Reduction*, is approved as the sole catalogue source for
the Phase 1 local technical spike. No alternate parser, fixture, benchmark, migration,
or dual-catalogue support is planned.

I/311 local structure is verified, acquisition provenance is partial, derived-data
redistribution remains unresolved, and the local-only parser boundary is defined in
Milestone 2B.
The documented 30 FPS and under-100-ms raycast targets were found, but their
measurement protocol, primary device, browser/WebGL renderer, and representative
product scale remain unapproved.

The synthetic-oracle smoke milestone is complete using only explicit synthetic inputs.
No catalogue parser, source-derived fixture, generated catalogue artifact, production
astronomy behavior, scene, renderer, or performance collector was created.

### Milestone 2B catalogue authority and provenance

The source/release, complete main-table field contract, supplemental-solution policy,
missing/duplicate/invalid-row behavior, `pmRA` semantics, exact 19-HIP technical review
allowlist, numerical/cultural separation, canonical schemas, deterministic
serialization, manifest, and checksum requirements are recorded in
`spikes/PHASE1_CATALOGUE_AUTHORITY_PROVENANCE.md`.

This authorizes Phase 3 / Milestone 3A to implement a local, read-only, fail-closed
parser against ignored hash-identified bytes. It does not authorize source-derived Git
artifacts or deployment: VizieR supports scientific-context use with attribution, but
I/311 raw/derived redistribution remains unresolved. The HIP list is a retrieval and
review candidate only; all Arabic forms, memberships, pattern edges, relationships,
teaching roles, and row-level scientific suitability still require the recorded human
reviews.

### Milestone 2A modern synthetic-only retry

The earlier exact candidate set remains recorded as a failed experiment: Astropy 7.2.2
required `astropy-iers-data>=0.2026.6.22.1.23.34`, conflicting with the proposed older
IERS-data pin. The retry deliberately used a current stable compatible stack rather
than the minimum release satisfying that old constraint.

Exact CPython 3.14.6 and uv 0.11.32 now lock Astropy 8.0.1,
`astropy-iers-data` 0.2026.7.20.15.31.18, NumPy 2.5.1, packaging 26.2, PyERFA
2.0.1.5, and PyYAML 6.0.3. Astropy and IERS data are direct dependencies; the others
are transitive because UFUQ does not import them directly.

The two valid synthetic transforms and one structured invalid case passed seven
unittests. Automatic IERS download/general Astropy internet access are disabled,
connection attempts fail closed, a fresh temporary cache is used, and the actual
packaged Earth-orientation/leap-second files and hashes are recorded. Two separate
locked offline executions produced byte-identical canonical output with SHA-256
`d1183fd6ff3d74603ff6b4c70809ef4d954fdb55a6ac8a3b62f2ee78f341da69`.
A fresh environment was reconstructed offline from existing package caches, so the
honest reproduction classification is `CACHE_DEPENDENT_OFFLINE_EXECUTION`, not a full
air-gapped rebuild.

The oracle imports no UFUQ production package, executes no Node astronomy code, and
contains no catalogue value or identifier. It establishes no production algorithm,
scientific tolerance, final IERS date policy, refraction policy, or source-derived
authority. Catalogue work and Milestone 2B remain unauthorized and unstarted.

Milestone validation: exact uv lock check and locked offline sync passed; 7 Python
unittests passed; two isolated generations were byte-identical; a fresh temporary
environment reconstructed from populated caches; `npm.cmd run check`, `test`,
`cycles`, `exports:check`, `build`, and `test:e2e` all passed. `test:reference` still
fails closed because production/reference comparison has not begun. Restricted,
raw/generated-data, dependency/source-diff, environment/binary, secret, and staged-file
scans passed.

## Validated Phase 0 structure

The eight npm workspaces are:

1. `apps/web`
2. `apps/api`
3. `packages/astronomy-core`
4. `packages/assessment-core`
5. `packages/tutoring-core`
6. `packages/contracts`
7. `packages/catalogue-schema`
8. `tools/catalogue`

`tutoring-core` retains logical `bkt`, `observations`, and `adaptive-policy` modules
without separate package overhead or an assessment dependency. `catalogue-schema`
retains logical `catalogue`, `content`, and `artifact` modules and may later add
framework-free validators. `tools/catalogue` owns future pipeline modules internally.
`tools/astronomy-reference` is a separate locked Python/Astropy synthetic smoke oracle
with versioned JSON input/output envelopes and no npm or production-astronomy
dependency.

Tracked provenance and reviewed curation have separate directories. `data/raw/` is
ignored by default; locally acquired candidate bytes may exist there without becoming
part of the scaffold or a selected production catalogue. The data guard permits only
ignored/untracked raw content and rejects any tracked or unignored raw byte. No
catalogue or cultural record is part of a tracked runtime artifact. Compiler state,
declarations from the private web app, Vite output, and other build directories are
ignored and untracked. Source/data text is normalized to LF by `.gitattributes`, while
the future canonical data serializer must independently enforce UTF-8, LF,
deterministic key/record order, and defined numeric formatting.

## Validation evidence

| Command/check | Exact result on 2026-07-22 |
|---|---|
| `npm.cmd ci` | PASS; 306 packages installed from the lockfile. |
| `npm.cmd run format:check` | PASS; all matched files use Prettier style. |
| `npm.cmd run lint` | PASS; applications, packages, catalogue tool, tests, scripts, and root config modules reported no ESLint error. |
| `npm.cmd run typecheck` | PASS; seven composite Node/shared projects, the private no-emit web app, and test/config sources typechecked. |
| `npm.cmd run test` | PASS; 1 unit file and 1 API health test. |
| `npm.cmd run boundaries` | PASS; 8 workspaces, approved edges, no cycle/private import/runtime-to-tool edge, independent oracle. |
| `npm.cmd run cycles` | PASS; the same graph check explicitly confirmed acyclicity. |
| `npm.cmd run data:verify` | PASS at the scaffold checkpoint; the guard now distinguishes permitted ignored local raw candidates from prohibited tracked/unignored raw data. |
| `npm.cmd run build` | PASS; API, five shared packages, catalogue tool, and Vite web build completed; Vite transformed 16 modules. |
| `npm.cmd run exports:check` | PASS; 13 public export paths across 7 importable workspaces resolved. |
| `npm.cmd run test:e2e` | PASS; 1 Chromium web/API health smoke test. |
| `npm.cmd run test:reference` | Expected inactive-suite failure; exit 1 with include `tests/reference/**/*.test.ts`. |
| `npm.cmd run test:integration` | Expected inactive-suite failure; exit 1 with include `tests/integration/**/*.test.ts`. |
| Tracking/import/scope scans | PASS; no tracked generated output, restricted PDF, secret environment file, raw catalogue byte, runtime-to-tool/private import, astronomy/BKT behavior, persistence/authentication behavior, or concrete cultural/catalogue data. |

The pre-consolidation findings are preserved in `STRUCTURE_AUDIT.md`. The exact path
mapping, commands, corrections, and independent post-migration verdict are in
`STRUCTURE_MIGRATION.md`. `SCAFFOLD_AUDIT.md` is a historical audit of the original
13-workspace working tree and is not the current status.

## Authorized next work

Phase 1 Milestones 1, 2A, and 2B are complete. The next roadmap milestone is
Milestone 2C: Scientific Behaviour Contract.

The local I/311 parser is deferred to Phase 3 / Milestone 3A and remains subject to
catalogue deployment authority.

## Decisions that block the validated vertical slice

- **IMP-008 / AST-001:** raw/derived redistribution and deployment permission,
  acquisition provenance beyond `PARTIAL`, and scientific review of each selected
  row's solution, multiplicity, uncertainty, fit, variability, and supplement evidence.
  The local-only parser contract and candidate scope are resolved.
- **IMP-009 / AST-003 and AST-006:** production coordinate/time pipeline,
  implement-or-omit effects, supported range, failure policy, independent oracle,
  error budget, and tolerances.
- **IMP-011 / AST-002:** reviewed `SkyPattern` and `GuidanceRelationship` records for
  one complete route to Al-Jady, including stable IDs, labels, membership, segments,
  instructional geometry/explanation, and review/verification status.
- **IMP-012 / AST-007 and AST-006:** one sourced observer/time scenario, expected
  result, answer representation, and justified learner/scientific tolerance.

BKT parameters/cues do not block the Phase 2 minimal slice because adaptation begins in
Phase 3. Persistence, authentication, participant, privacy/security release, and
deployment decisions belong to Phases 4-6 and do not block Phases 0-2.

## Default implementation documents

1. `../AGENTS.md`
2. `IMPLEMENTATION_BRIEF.md`
3. `ARCHITECTURE.md`
4. `IMPLEMENTATION_DECISIONS.md`
5. `PHASES.md`
6. `TEST_PLAN.md`
7. `STATUS.md`

Technical domain specs and ADRs are loaded by phase. `governance/` remains conditional
context for formal approvals, participant/privacy/deployment work, report deviations,
and thesis traceability.
