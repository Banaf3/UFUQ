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
| `test:reference` | production/reference astronomy and separately justified independent-oracle or BKT comparisons discovered only by `vitest.reference.config.ts` |
| `test:integration` | API plus real-MySQL tests discovered only by `vitest.integration.config.ts` |
| `test:e2e` | focused browser journeys, interaction boundaries, and accessibility checks |

Exact commands and tool versions are pinned by the scaffold. Unit tests and browser E2E
are active in Phase 0 CI. Reference and integration configurations exist but are not run
by default while their behavior is absent. Their scripts intentionally exit non-zero
when no matching test exists; neither uses `passWithNoTests`.

| Suite | Mandatory from | Activation rule |
|---|---|---|
| Unit | Phase 0 | Always; the health test proves discovery. |
| Reference | First production/reference comparison | Add to CI when a production implementation first has pinned comparison fixtures; it remains mandatory thereafter. |
| Integration | Phase 4 | Add to CI with the first API/persistence integration test; real MySQL is mandatory for transaction claims. |
| E2E | Phase 0 | Always; the health smoke proves browser/server lifecycle. |

Milestone 2C.6 makes the astronomy evidence order explicit:

- `PRE_IMPLEMENTATION` approves `ScientificProfileV1` semantics, exclusions,
  fail-closed outcomes, the source-neutral SOFA `2023-10-11`-derived pure-TypeScript
  route/effect mapping, synthetic exact guards, the pinned candidate reference
  environment, the final-only per-field leap/EOP policy, and the comparison plan. This
  stage defines the operational semantics for leap data, `UT1-UTC`,`xp`,`yp`; it does
  not require concrete 2D/2E artifact bytes, TypeScript residuals, or a numerical
  tolerance.
- `POST_IMPLEMENTATION` introduces TypeScript/reference fixtures, residuals,
  supported-domain partitions, implementation-error evidence, and activates
  `test:reference`. Numerical acceptance remains blocked until AST-006 supplies an
  operation-specific threshold.
- `STRONGER_INDEPENDENT_VALIDATION` later evaluates USNO NOVAS or another genuinely
  independent positional-astronomy path. Shared Astropy/PyERFA/ERFA/SOFA lineage is
  not an independent oracle.

The absence of a postimplementation comparison cannot block writing the production
implementation that the comparison must exercise. It does block scientific acceptance
once that implementation exists.

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
- If 2D retains I/311, Milestone 2E adapter tests must cover fixed widths,
  source-hash mismatch, missing/duplicate/invalid rows, blank optional photometry,
  negative parallax, solution/supplement joins, component/multiplicity reporting,
  sorted unique HIP selection, and two-run byte/hash determinism. If 2D selects another
  release, its approved adapter contract replaces the I/311-specific obligations.
  Source-derived outputs remain ignored and may not enter Git or the reference suite
  while their applicable redistribution authority is unresolved.
- For Gaia DR3, 2E adapter tests must verify exact IAU constants/expressions, same-event
  TCB-to-TDB epoch conversion, direction invariance, one-time proper-motion/parallax/
  distance mapping, the declared five-/six-parameter covariance Jacobians and
  pseudocolour preservation, unchanged typed spectroscopic
  RV, native/normalized provenance, and rejection of mixed, missing, repeated, or
  unapproved normalization. These tests establish contract conformance, not a
  numerical scientific tolerance or row approval.
- Source-adapter and schema prototypes use synthetic data clearly labelled as
  non-catalogue input until the applicable source-derived gates are met.
- Generic schema tests cover `SkyPattern`, `GuidanceRelationship`, and `LessonRoute`
  without asserting that any synthetic helper pattern or mapping is culturally valid.
- Acquisition inputs, transformation options, serialization, and hashes are recorded.
- Coordinate types prevent frame/unit/epoch mixing at compile time where practical.
- After the production route exists, candidate transformations are compared with
  fixtures produced by the separately pinned Python/Astropy reference tool. The tool
  does not import production astronomy, but shared ERFA/SOFA lineage is disclosed and
  is not called stronger independent validation. Comparison code in `tests/reference`
  imports `astronomy-core`; differences are recorded, not hidden behind an invented
  tolerance.
- The normative ScientificProfileV1 semantic suite must prove geometric output retains
  signed altitude, normalized ENU, defined azimuth or exact singular state, provenance,
  warnings/statuses, and pending-validation state; below-horizon remains result-bearing;
  refraction is `NOT_REQUESTED`; no atmosphere/default/refracted coordinate exists; no
  aggregate visibility or learner eligibility is inferred; and later classifications
  cannot erase a valid result or hide an earlier required-input/artifact/domain/
  approval/execution failure. `APPROVED_GEOMETRIC_RESULT`, near-singular epsilon-based
  classification, degraded output, and every refracted result remain unreachable.
- The normative time-boundary suite must accept only fixed-width whole-second
  `YYYY-MM-DDTHH:mm:ssZ`; reject fractions, offsets, `-00:00`, local/unqualified time,
  Unix timestamps, bare JDs, and implicit current time; distinguish structural
  `23:59:60Z` eligibility from approved-artifact validation; preserve labelled UTC
  quasi-JD/TAI/TT/UT1 states and conversion evidence; and fail closed for unavailable
  leap data, missing required EOP fields, unapproved time data, and instants outside the
  activated `SupportedTimeDomain`.
- Activation tests must derive the concrete earliest/latest instants from every
  approved contributing domain, exercise each boundary according to its explicit
  inclusion rule plus the chronologically adjacent whole second (including leap-second
  ordering), and prove that one EOP field cannot borrow another field's coverage or
  interpolation support. These tests begin after 2D/2E supplies the immutable artifacts;
  no placeholder date range is permitted.
- Leap/EOP activation tests must verify exact raw and normalized bundle hashes; Bulletin
  C consistency of the selected official machine-readable leap transport; explicit
  expiry/validity metadata; exact-event `23:59:60Z` validation; independent final
  source-quality, row/support, coverage and approval state for `UT1-UTC`,`xp`,`yp`;
  UFUQ-selected four-point support and the selected versioned IERS Conventions 2010
  ocean-tide/applicable-libration restoration, ordered after interpolation and applied
  exactly once;
  continuous `UT1-TAI` handling across leap boundaries; rejection of blanks, gaps,
  duplicates, non-monotonic samples and mixed/unapproved support; and deterministic
  offline replay. Tests must prove there is no zero, nearest-row, extrapolated,
  preliminary, predicted, estimate, expired-for-request, hidden-cache, ambient library
  table, automatic-download or cross-field fallback. Artifact acquisition age alone
  must neither approve nor invalidate a historical final row.
- Milestone 2C.4's later reference design retains separate geometric/refracted states,
  explicit atmosphere units/provenance and no implicit defaults, model/domain/warning
  capture, near/zero/below-horizon partitions, distinct geometric/refracted-apparent/
  physical-dip/terrain/renderer/learner horizon states, and nine independent visibility
  components. Its seven experiment families run only when a later refraction/visibility
  profile opens their scientific policy and input-data gates. Only cases that compare
  production code with the reference tool depend on `test:reference` activation.
- Milestone 2C.5A freezes 24 experiment records in a human protocol and machine
  registry with separate fixture/result schemas. A runnable synthetic record must use
  explicit synthetic inputs, locked offline dependencies, declared ERFA/SOFA lineage,
  at least two deterministic repetitions, complete hashes, and either exact supported
  invariants or `MEASURED_NO_ACCEPTANCE`. The first 2C.5B batch may add experiment
  bodies only to the non-production Python reference tool. It must not create I/311-
  derived fixtures, production astronomy, numerical acceptance, or a placeholder
  reference test. Synthetic tool experiments alone do not activate `test:reference`;
  the first production/reference comparison does. The 2C.5A protocol-shape suite
  checks the exact human/machine ID and classification inventory, zero-count intent,
  Batch 01 membership and bounded partitions, synthetic-only fixture/result scope,
  schema/version/closed-object contracts, execution outcomes and manifest fields,
  canonicalization rules, local schema references, and the absence of direct `erfa`
  imports or experiment instances at that milestone boundary.
- Milestone 2C.5B promotes the already locked PyERFA release to a direct reference-tool
  dependency and permits an `erfa` import only in the bounded Batch 01 runner. The
  offline Python unit suite validates the exact nine fixture/result inventory, registry
  allowlist and five-part `2C.2-EXP-04` scope, schema keyword subset and negative
  branches, canonical bytes/hash boundaries, source prohibitions, unknown/non-Batch
  rejection, two internal fresh-cache repetitions, in-process full-batch replay,
  warning/raw-status
  preservation, exact guard outcomes, measurement-only outcomes, optional-state
  non-erasure, dependency/lock/environment consistency, and production-import absence.
  The epoch-label tests additionally require the exact synthetic ITRS-geocentre
  `[0,0,0] m` fixture record, reject missing/nonzero variants, statically confirm every
  affected Astropy `Time` constructor supplies `location=`, and require the matching
  structured status/fixture-manifest binding. Each epoch case must run alone after
  explicitly initializing and evidencing the pinned smoke-only leap artifact; inherited
  ERFA leap state is prohibited. Stale result or companion hashes fail.
  A separate execution check invokes the complete Batch command in two independent OS
  processes with separate temporary cache/comparison directories in the same
  pre-synchronized locked environment and compares every result byte/hash; it does not
  claim clean-environment dependency reconstruction. All
  numerical measurements remain `MEASURED_NO_ACCEPTANCE`; the synthetic execution does
  not activate `test:reference` because no production/reference comparison exists.
- Milestone 2C.5C validates the error-budget ledger directly against the committed
  result bytes and companion hashes without importing or rerunning the Batch runner.
  The ledger test proves exact 9/24/0/6/27 totals; full measurement/check coverage;
  frozen protocol/registry/schema/environment/lock/runner hashes; 49 terms split into
  45 unbounded numerical-bound states and four exact non-numerical aggregate
  guards; exact layer counts/IDs; evidence-ID and human-document cross-references;
  external-authority-limit ownership; separation of scene/learner layers; six blocked
  tolerance classes with no numerical values; and a ranking containing exactly the
  eight remaining runnable non-Batch experiments. Exact guards remain boolean contract
  evidence, measured zeros remain without acceptance, and an unbounded required term
  prevents a combined scientific budget. This documentation/ledger validation still
  does not activate `test:reference`.
- The spike can be removed or replaced without changing public contracts.

## Phase 2 tests

- Approved minimal catalogue/curation artifact rebuilds deterministically.
- Production/reference astronomy cases cover the selected scenario and ProfileV1
  boundary partitions; any stronger independent-oracle cases are separately labelled
  and lineage-audited.
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
- Never substitute machine epsilon, a library/test-framework epsilon, display
  precision, deterministic hash identity, same-family agreement, scene pixels, or a
  learner radius for an unresolved AST-006 scientific term.
- Generic route tests use visibly synthetic IDs/labels; a passing schema or selection
  test is not cultural verification.
- Record random seeds, exact environment/tool/browser/database versions, input hashes,
  and raw versus derived artifacts for evidence-bearing runs.
- A technical-spike comparison may fail or remain outside final tolerance; report the
  result and keep production readiness false until resolved.
- Do not weaken a gate. Narrow the implemented claim or keep the affected readiness
  gate at `NO`.
