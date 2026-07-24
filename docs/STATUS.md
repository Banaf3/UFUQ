# Implementation status

**Assessment date:** 2026-07-25

The consolidated Phase 0 repository scaffold is validated. It contains health-only web
and API applications, eight npm workspaces, pure empty/type-placeholder domain
boundaries, a non-npm independent Python reference-tool scaffold, pinned tooling,
fail-closed suite configurations, boundary checks, and CI. It contains no astronomy
calculation, catalogue/cultural record, BKT formula, persistence/authentication
behavior, dashboard, or deployment configuration.

## Independent readiness gates

| Gate | Result | Basis |
|---|---|---|
| Repository scaffolding | YES | The consolidated eight-workspace TypeScript monorepo, non-npm oracle boundary, strict compiler/build setup, test discovery, dependency enforcement, lockfile, and CI are validated. |
| Validated celestial-guidance vertical slice | NO | The exact catalogue/subset, production astronomy pipeline/error budget, reviewed pattern/relationship content for one route, scenario, and scoring tolerances remain unresolved. |
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

This work does not approve I/311, a production astronomy pipeline, a schema validator,
a Kaaba coordinate/datum, a numerical tolerance, a cultural mapping, or a
learner-facing route. The pinned Astropy/PyERFA/IERS-data environment and official
Astropy documentation remain Phase 1 source gaps. Najdi/regional evidence, a stable
edition for the studied Ibn Qutaybah claims, exact membership/route evidence, and human
Arabic/cultural review remain required before learner-facing cultural claims.

The official ESA 1997 Volume 1 guide now establishes the original catalogue's
`mu_alpha_star` convention and J1991.25(TT) definition. The later I/311 `pmRA` mapping
is classified `STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED`; this clarification adds
future spike cases but does not activate Phase 1.

The detailed evidence boundaries are in `references/PDF_KNOWLEDGE_COVERAGE.md`.
Phase 1 has not begun.

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
`tools/astronomy-reference` is a separate Python/Astropy scaffold with a neutral
versioned JSON fixture envelope and no npm or production-astronomy dependency.

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

The repository scaffold is validated and ready for the Phase 1 astronomy/data
technical spike. Phase 1 has not begun. It may introduce only replaceable,
clearly-labelled candidate/synthetic technical inputs until the applicable decisions
are approved.

## Decisions that block the validated vertical slice

- **IMP-008 / AST-001:** exact catalogue source/version, permitted access/licence,
  required fields, subset, and quality rules.
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
