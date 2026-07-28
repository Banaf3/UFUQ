# Implementation test plan

## Purpose

Tests follow the implementation phases. A missing later governance decision blocks only
the affected acceptance claim; it does not prevent scaffolding an interface, running a
technical spike, or testing unrelated pure code.

## Standard suites

The Phase 0 scaffold should expose these stable intentions through package scripts:

| Suite | Purpose |
|---|---|
| `check` | formatting/lint, TypeScript, package boundaries, and browser-bundle exclusions |
| `data:verify` | schema, provenance manifest, canonical serialization, referential integrity, and hashes |
| `test` | unit/contract/property tests discovered only by `vitest.unit.config.ts` |
| `test:reference` | independent astronomy and BKT comparisons discovered only by `vitest.reference.config.ts` |
| `test:integration` | API plus real-MySQL tests discovered only by `vitest.integration.config.ts` |
| `test:e2e` | focused browser journeys, interaction boundaries, and accessibility checks |

Exact commands and tool versions are pinned by the scaffold. Unit tests and browser E2E
are active in Phase 0 CI. Reference and integration configurations exist but are not run
by default while their behavior is absent. Their scripts intentionally exit non-zero
when no matching test exists; neither uses `passWithNoTests`.

| Suite | Mandatory from | Activation rule |
|---|---|---|
| Unit | Phase 0 | Always; the health test proves discovery. |
| Reference | Phase 1 | Add to CI with the first independent astronomy comparison; it remains mandatory thereafter. |
| Integration | Phase 4 | Add to CI with the first API/persistence integration test; real MySQL is mandatory for transaction claims. |
| E2E | Phase 0 | Always; the health smoke proves browser/server lifecycle. |

## Phase 0 tests

- Clean dependency installation from the lockfile.
- Workspace discovery and TypeScript project-reference build.
- The API health unit and browser health smoke prove active test discovery.
- Static configuration inspection proves `tests/reference/**/*.test.ts` and
  `tests/integration/**/*.test.ts` are the separate later-suite roots. Invoking either
  empty suite must exit non-zero; do not add fake scientific or integration tests.
- Forbidden imports: pure packages cannot import framework, browser, database, HTTP, or
  environment I/O modules.
- Browser bundle cannot import server scorer/target/tolerance entry points.
- No application/domain feature acceptance is asserted.

## Phase 1 tests

- Catalogue contract tests target CDS I/311 metadata and wholly synthetic records. They
  verify the exact field/unit mapping, explicit `pmRA` to `mu_alpha_star` name,
  supplemental solution shapes, numerical/cultural separation, canonical artifact
  rules, and provenance/licence/checksum requirements. No alternate-catalogue contract
  or fixture is required.
- Phase 3 / Milestone 3A tests must cover fixed widths, source-hash mismatch,
  missing/duplicate/invalid rows, blank optional photometry, negative parallax,
  solution/supplement joins, component/multiplicity reporting, sorted unique HIP
  selection, and two-run byte/hash determinism. Source-derived outputs remain ignored
  and may not enter Git or the reference suite while redistribution is unresolved.
- Source-adapter and schema prototypes use synthetic data clearly labelled as
  non-catalogue input until the applicable source-derived gates are met.
- Generic schema tests cover `SkyPattern`, `GuidanceRelationship`, and `LessonRoute`
  without asserting that any synthetic helper pattern or mapping is culturally valid.
- Acquisition inputs, transformation options, serialization, and hashes are recorded.
- Coordinate types prevent frame/unit/epoch mixing at compile time where practical.
- Candidate transformations are compared with fixtures produced by the separately
  pinned Python/Astropy oracle. The oracle does not import production astronomy;
  comparison code in `tests/reference` imports `astronomy-core`. Differences are
  recorded, not hidden behind an invented tolerance.
- The spike can be removed or replaced without changing public contracts.

## Phase 2 tests

- Approved minimal catalogue/curation artifact rebuilds deterministically.
- Independent astronomy cases cover the selected scenario and boundary partitions.
- Every numeric tolerance is named, sourced, versioned, and justified before it becomes
  an acceptance gate.
- ENU-to-Three cardinal/horizon/zenith and camera tests are deterministic.
- Raycast and accessible answer controls produce raw evidence only.
- Contract/API tests prove the server owns scenario, target, scoring, and feedback.
- Route validation resolves every pattern/star/direction reference, step order,
  prerequisite, alternative path, and scaffold-configuration reference.
- Scenario selection accepts a route only when every star required by its selected
  pattern and relationship steps exists in the approved scenario; missing any required
  star excludes that route deterministically.
- Composition tests support helper-pattern to Banat Na'sh or Dhat al-Kursi, either
  reviewed pattern to Al-Jady, Al-Jady to True North, and True North to Qibla without
  special-case branches for a named pattern.
- One browser journey reproduces the selected approved route outcome and records the
  route/content versions.

## Phase 3 tests

- Standard BKT examples are independently recalculated.
- Parameter boundaries, observation/no-update/transition-only cases, and seeded
  properties are deterministic.
- Assisted and independent evidence cannot be conflated by client metadata.
- Every adaptive state/reason/cue transition has a fixture.
- Assessment boundary/wrap/singularity cases cover each implemented answer type.
- Evaluation-only sessions do not update model/policy unless an approved rule says so.

## Phase 4 tests

- Run transaction and concurrency tests against the frozen MySQL/InnoDB profile, never
  SQLite as the atomicity oracle.
- Cover rollback at each write, concurrent cold start, matching duplicate, same-key
  mismatch, stale revision, deadlock/timeout classification, and ordered concurrent
  submissions.
- Cover ownership and capability authorization, IDOR, session lifecycle, CSRF,
  enumeration/rate limiting, recovery, and fixture-identity production exclusion for
  the implemented policy.
- Verify sensitive values are absent from logs and client storage.

## Phase 5 tests

- Full reference/data suites across the approved scenario partitions.
- Focused browser/visual baselines for scientific orientation and scaffold state.
- Performance under the recorded representative hardware/browser/scene protocol.
- Automated plus manual accessibility checks for the approved claim and equivalent
  controls.
- Security/privacy checklist, dependency/secret scan, backup/restore, and clean-build
  evidence replay appropriate to the intended release.

## Phase 6 evidence checks

- Participant tests are protocol, consent, version-freeze, codebook, exclusion,
  analysis-reproduction, and privacy checks—not ordinary software unit tests.
- Deployment tests are TLS/configuration, least privilege, secret handling, monitoring,
  recovery, supported-browser, and artifact/version checks.
- Participant-study readiness and deployment readiness remain independent.

## Failure and evidence rules

- Never choose a catalogue value, cultural mapping, tolerance, BKT parameter, or policy
  merely to make a test pass.
- Generic route tests use visibly synthetic IDs/labels; a passing schema or selection
  test is not cultural verification.
- Record random seeds, exact environment/tool/browser/database versions, input hashes,
  and raw versus derived artifacts for evidence-bearing runs.
- A technical-spike comparison may fail or remain outside final tolerance; report the
  result and keep production readiness false until resolved.
- Do not weaken a gate. Narrow the implemented claim or keep the affected readiness
  gate at `NO`.
