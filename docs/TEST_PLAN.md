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
| `test` | deterministic pure unit/contract/property tests |
| `test:reference` | independent astronomy and BKT reference comparisons |
| `test:integration` | API plus real-MySQL transaction/authentication tests when those components exist |
| `test:e2e` | focused browser journeys, interaction boundaries, and accessibility checks |

Exact commands and tool versions are pinned by the scaffold. A suite may initially be
an honest no-applicable-tests check, but it must not report domain behavior as covered
before that behavior exists.

## Phase 0 tests

- Clean dependency installation from the lockfile.
- Workspace discovery and TypeScript project-reference build.
- One trivial test in each configured runner proves discovery and non-zero failure exit.
- Forbidden imports: pure packages cannot import framework, browser, database, HTTP, or
  environment I/O modules.
- Browser bundle cannot import server scorer/target/tolerance entry points.
- No application/domain feature acceptance is asserted.

## Phase 1 tests

- Source-adapter and schema prototypes use synthetic or clearly labelled candidate data.
- Generic schema tests cover `SkyPattern`, `GuidanceRelationship`, and `LessonRoute`
  without asserting that any synthetic helper pattern or mapping is culturally valid.
- Acquisition inputs, transformation options, serialization, and hashes are recorded.
- Coordinate types prevent frame/unit/epoch mixing at compile time where practical.
- Candidate transformations are compared with an independently implemented/pinned
  reference harness; differences are recorded, not hidden behind an invented tolerance.
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
