# Implementation status

**Assessment date:** 2026-07-22

The Phase 0 repository scaffold is complete. It contains health-only web and API
applications, empty or type-only domain boundaries, pinned tooling, boundary checks,
tests, and CI. It contains no astronomy calculation, catalogue/cultural record, BKT
formula, persistence/authentication behavior, dashboard, or deployment configuration.
Scientific, cultural, learning-policy, participant, privacy/security release, and
deployment decisions remain assessed at the gate they actually affect.

## Independent readiness gates

| Gate | Result | Basis |
|---|---|---|
| Repository scaffolding | YES | The TypeScript npm-workspace monorepo, apps/packages/tools layout, React/R3F/Three.js web stack, Node/Express API, pure-package boundaries, strict compiler configuration, test tooling, lockfile, and CI are implemented and validated. No unresolved value affects the scaffold. |
| Validated celestial-guidance vertical slice | NO | The generic route/content model is settled, but the exact catalogue/subset, production astronomy pipeline/error budget, reviewed pattern/relationship content for one route, scenario, and scoring tolerances are unresolved. A replaceable astronomy/data spike may proceed first. |
| Participant study | NO | Participant protocol, ethics applicability/approval, instruments, recruitment, privacy, consent, data handling, and study-ready software remain unresolved or unimplemented. |
| Deployment | NO | Hosting/operations target, production account policy, security/privacy release profile, performance/accessibility baselines, monitoring, and backup/restore evidence remain unresolved or unimplemented. |

READY_FOR_SCAFFOLDING: YES

READY_FOR_VERTICAL_SLICE: NO

READY_FOR_PARTICIPANT_STUDY: NO

READY_FOR_DEPLOYMENT: NO

## Phase 0 scaffold delivered

- npm workspaces cover `apps/*`, `packages/*`, and `tools/*`; all external versions are
  exact in the manifests and root lockfile.
- `apps/web` is a React/Vite health screen. `apps/api` is an Express service with only
  `GET /health` and a separately startable server.
- Pure boundaries exist for astronomy, assessment, BKT, adaptive policy, tutoring,
  contracts, catalogue schema, and star/route data. Tool boundaries exist for the
  astronomy reference harness and catalogue pipeline.
- `SkyPattern`, `GuidanceRelationship`, and `LessonRoute` are generic type placeholders;
  there are no concrete stars, patterns, cultural mappings, or lesson routes.
- Strict TypeScript, ESLint, Prettier, Vitest, Playwright, package-boundary validation,
  the empty-data guard, and GitHub Actions CI are configured.
- Every production dependency is explained in `DEPENDENCIES.md`. No database,
  authentication, astronomy, catalogue-client, BKT, analytics, or deployment library
  was added.

## Phase 0 validation evidence

| Command/check | Exact result on 2026-07-22 |
|---|---|
| `npm.cmd install` | PASS; 311 packages added, 325 packages audited, 0 vulnerabilities. |
| `npm.cmd run format:check` | PASS; all matched files use Prettier style. |
| `npm.cmd run lint` | PASS; ESLint reported no error. |
| `npm.cmd run typecheck` | PASS; project references and test configuration compile in no-emit mode. |
| `npm.cmd run boundaries` | PASS; 13 workspaces checked, allowed edges enforced, type-only packages checked, and dependency graph acyclic. |
| `npm.cmd run data:verify` | PASS; data directories contain README placeholders only. |
| `npm.cmd run test` | PASS; 1 test file and 1 API health test passed. |
| `npm.cmd run test:reference` | PASS with no tests, as explicitly allowed for the empty Phase 0 reference harness. |
| `npm.cmd run test:integration` | PASS with no tests, as explicitly allowed for the empty Phase 0 integration harness. |
| `npm.cmd run build` | PASS; TypeScript build passed and Vite built 16 modules. |
| `npm.cmd run test:e2e` | PASS; the Chromium web/API health smoke test passed (1/1). |

The first two browser-smoke attempts passed their assertion but exposed a Windows
Playwright web-server teardown hang. The runner was changed to own and terminate both
health servers explicitly; the final command exited successfully. Git ignore/tracking
checks found no tracked restricted PDF or environment file, `.env.example` contains no
secret, the secret-pattern scan returned no match, and targeted scans found no concrete
cultural route or real astronomy/BKT implementation.

## Authorized next work

Phase 0 must stop here. Phase 1 may run a technical astronomy/data spike using synthetic
or clearly labelled candidate fixtures behind replaceable interfaces. It cannot promote
candidate values into learner-facing content or scientific evidence.

## Decisions that genuinely block the validated vertical slice

- **IMP-008 / AST-001:** exact catalogue source/version, permitted access/licence,
  required fields, subset, and quality rules.
- **IMP-009 / AST-003 and AST-006:** production coordinate/time pipeline,
  implement-or-omit effects, supported range, failure policy, independent oracle, error
  budget, and tolerances.
- **IMP-011 / AST-002:** approved `SkyPattern` and `GuidanceRelationship` records for
  one complete route to Al-Jady, including stable catalogue IDs, names/labels,
  membership, segments, instructional geometry/explanation, and review/verification
  status. The exact helper pattern and whether the first route uses Banat Na'sh or Dhat
  al-Kursi remain provisional.
- **IMP-012 / AST-007 and AST-006:** one sourced observer/time scenario, expected
  result, answer representation, and justified learner/scientific tolerance.

BKT parameters/cues do not block the Phase 2 minimal slice because adaptation begins in
Phase 3. Persistence, authentication, participant, privacy/security release, and
deployment decisions belong to Phases 4–6 and do not block Phases 0–2.

**IMP-018 is approved:** generic `SkyPattern`, `GuidanceRelationship`, and
`LessonRoute` schemas plus scenario-availability filtering can be scaffolded without
selecting any cultural record. This clarification does not change scaffolding readiness.

## Default implementation documents

1. `../AGENTS.md`
2. `IMPLEMENTATION_BRIEF.md`
3. `ARCHITECTURE.md`
4. `IMPLEMENTATION_DECISIONS.md`
5. `PHASES.md`
6. `TEST_PLAN.md`
7. `STATUS.md`

Technical domain specs and ADRs are loaded by phase. `governance/` is conditional
context and retains the complete independent review, original single-gate verdict,
report deviations, open decisions, research/release governance, risks, and
traceability.
