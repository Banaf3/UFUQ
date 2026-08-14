# Implementation decisions

This register contains only choices that affect code structure, runtime behavior, or
tests. **Approved** choices may be implemented. **Provisional** choices may be used
behind a replaceable boundary and must be pinned when introduced. **Unresolved**
choices block only the affected behavior; they do not block unrelated scaffolding.
Historical report/deviation/authority status remains in `governance/`.

## IMP-001 — Repository form

- **Decision:** Repository and application shape.
- **Current choice:** TypeScript modular monorepo with `apps/web`, `apps/api`, pure
  domain packages, shared contracts/schema packages, and a catalogue tool.
- **Status:** approved
- **What code it affects:** Root workspace, package folders, TypeScript references,
  import boundaries, build graph.
- **Validation required:** A clean checkout discovers every workspace; forbidden-import
  checks prove dependencies point inward and pure packages compile without app/runtime
  dependencies.

## IMP-002 — Runtime stack

- **Decision:** Primary application technologies.
- **Current choice:** React with React Three Fiber/Three.js in the browser,
  Node.js/Express in the API, and MySQL/InnoDB for durable persistence.
- **Status:** approved
- **What code it affects:** Web/API entry points, adapter packages, database adapter,
  dependency manifest.
- **Validation required:** Minimal build/type checks for both apps and an adapter smoke
  test; real MySQL validation begins when persistence is introduced.

## IMP-003 — Dependency direction

- **Decision:** Separation of domain, application, and adapter code.
- **Current choice:** `astronomy-core`, `assessment-core`, and `tutoring-core` are pure;
  BKT, observation semantics, and adaptive policy are logically separate modules inside
  `tutoring-core`; application use cases own ports; adapters depend inward.
- **Status:** approved
- **What code it affects:** Package public APIs, project references, lint/import rules,
  composition roots.
- **Validation required:** Automated forbidden-import and browser-bundle tests plus
  isolated compilation/unit tests for pure packages.

## IMP-004 — Server authority and contracts

- **Decision:** Location of authoritative assessment/adaptation behavior.
- **Current choice:** Versioned API contracts carry raw learner evidence; the API owns
  scenario validity, scoring, model decisions, revisions, and next scaffold state.
- **Status:** approved
- **What code it affects:** Contracts, web API client, API use cases, scenario and
  assessment interfaces.
- **Validation required:** Contract tests and a build check proving authoritative
  scorer/target/tolerance entry points are absent from the browser bundle.

## IMP-005 — Workspace and build tooling

- **Decision:** Concrete monorepo/build configuration.
- **Current choice:** npm workspaces, pinned supported Node.js and TypeScript versions,
  TypeScript project references, and Vite for the web application.
- **Status:** provisional
- **What code it affects:** Root/package manifests, lockfile, `tsconfig` hierarchy,
  web build configuration, scripts.
- **Validation required:** Pin exact versions in Phase 0; verify clean `npm ci`, build,
  type-check, and workspace script execution before adding behavior.

## IMP-006 — Automated test tooling

- **Decision:** Test runners used by the implementation workflow.
- **Current choice:** Separate fail-closed Vitest configurations for unit, reference,
  and integration tests, plus Playwright for browser tests. Inactive later-phase suites
  are omitted from Phase 0 CI rather than reported as passing; real MySQL tests activate
  the integration suite when persistence appears.
- **Status:** provisional
- **What code it affects:** Test configuration, package scripts, fixtures, CI jobs.
- **Validation required:** Phase 0 self-tests prove test discovery, deterministic seed
  reporting, failure exit codes, and separation of unit, reference, integration, and E2E
  suites.

## IMP-007 — Repository package layout

- **Decision:** Initial folders and package names.
- **Current choice:** Use exactly eight npm workspaces: `apps/web`, `apps/api`,
  `packages/astronomy-core`, `packages/assessment-core`, `packages/tutoring-core`,
  `packages/contracts`, `packages/catalogue-schema`, and `tools/catalogue`. Keep
  `tools/astronomy-reference` as a separate non-npm Python/Astropy fixture producer.
- **Status:** approved
- **What code it affects:** Folder creation, explicit workspace list, dependency graph,
  public entry points, code-independent reference environment with lineage disclosure.
- **Validation required:** No unresolved scientific, cultural, BKT, participant,
  security, or deployment value changes these folder/package boundaries.

## IMP-008 — Catalogue source and runtime subset

- **Decision:** Exact catalogue/table/version, licence/access route, subset, fields,
  quality rules, and canonical runtime artifact.
- **Current choice:** The corrected 2008-09-16 CDS/VizieR I/311 `hip2.dat` table,
  supplements, and 19-HIP allowlist define only the bounded local Phase 1 parser spike.
  That spike preserves every source field and solution/multiplicity/quality record,
  fails on missing/duplicate/invalid rows or supplements, maps its source-supported
  `pmRA` directly to the starred-alpha normalized field, and keeps all raw/derived rows
  local while rights remain unresolved. Milestone 2D must separately select the
  production catalogue/release, minimal numerical ProfileV1 allowlist, rights, row
  eligibility, and stable UFUQ `starId`/source-release crosswalk. I/311 is neither
  automatically retained nor migrated away here. Cultural records reference `starId`,
  never copied coordinates or a permanently coupled external identifier.
- **Status:** provisional (local non-redistributing I/311 spike contract approved;
  production source/release, acquisition, deployment, allowlist, row authority, and
  crosswalk unresolved under Milestone 2D)
- **What code it affects:** Catalogue acquisition adapter, transform/schema fields,
  generated artifact, scientific fixtures.
- **Validation required:** For the source selected by 2D: transport/hash verification,
  source-specific parse/join rules, schema/range/quality reporting, sorted unique
  selection, byte-identical rebuild, provenance/licence manifest, crosswalk integrity,
  and scientific row review. The existing fixed-width/supplement/HIP checks apply only
  if 2D retains I/311. Falak/cultural review remains separate before learner-facing use.

## IMP-009 — Astronomy transformation pipeline

- **Decision:** Exact reference-frame/time/Earth-orientation/observer transformation
  algorithm, supported range, effects, failure modes, and error budget.
- **Current choice:** The Milestone 2C evidence audit confirms the typed state
  boundaries, I/311 ICRS input/frame label, starred-alpha `pmRA`, UTC/TAI/TT/UT1 roles,
  fixed sign/horizontal conventions, structured-outcome requirement, and the
  code-independent comparison protocol with explicit lineage. Milestone 2C.1 records
  ESA Gaia DR1's direct I/311-specific
  `J1991.25` usage as source support for the Julian representation. It does not find an
  I/311 time scale. Preserve the label/representation and make source-derived
  propagation unavailable until exact authority or named astronomy-review approval
  supplies the scale. Milestone 2C.2 first proposed a componentized SOFA
  `2023-10-11` CIO-family route; the focused 2C.6 route audit now makes its bounded
  production mapping normative. Production implements a UFUQ-owned pure-TypeScript
  subset derived from exact lower-level SOFA C semantics: strict `pmsafe`-derived full
  space motion to the J2000.0 TDB epoch interface, pinned `epv00` Earth/Sun state,
  `pnm06a`/CIO model orientation, declared-ellipsoid observer construction, an
  `apco`/`apcs`-derived context, `atciq`-derived ICRS-to-CIRS, and only the geometric
  part of the `atioq`-derived local transformation. It requires approved epoch and
  derivative scales, `mu_alpha_star`, Dec motion, positive parallax/equivalent
  distance, finite radial velocity, leap data, `UT1-UTC`, `xp`, `yp`, and an approved
  observer. It includes frame bias, IAU 2006 precession with IAU 2000A nutation,
  annual aberration, solar deflection, Earth rotation, polar motion and diurnal
  aberration. Observer velocity carries the diurnal term through the `apcs`/`atciq`-
  derived context and the later local `diurab` term is disabled as redundant, matching
  SOFA `apco`. Observed `dX`,`dY`, extra-body deflection and refraction are explicitly
  outside V1 and remain unbounded rather than zero. Missing or unapproved required
  row/operational inputs fail closed.
  Astropy `8.0.1` remains a reference path independent of production code/dependencies,
  not a scientifically lineage-independent oracle; the SOFA-derived production subset
  and Astropy/PyERFA/ERFA share scientific lineage, and composed ERFA `atco13` remains
  only a same-family consistency check. Current official package/repository/licence
  evidence finds no third-party TypeScript package that matches the V1 model, EOP,
  warning/status and offline boundary. ERFA or official SOFA C compiled to WebAssembly
  is a reviewed fallback if the owned subset proves unmaintainable, not the selected
  implementation or a stronger oracle. The ScientificProfileV1 time audit makes normative
  a whole-second Z-only restricted subset of RFC 3339 at the UTC astronomy input;
  conditional exact-date leap validation; typed UTC quasi-JD, TAI, TT, and UT1 states;
  a versioned `SupportedTimeDomain` with explicit endpoints and complete required-field
  coverage; no local/current-time or unlabeled-JD fallback; explicit geodetic observer
  provenance and uncertainty;
  immutable hash-addressed offline EOP/leap bundles; separately reviewed atomic
  updates with prior-bundle replay; separate source-quality, artifact integrity,
  field-coverage/interpolation support, publisher-validity, acquisition-lifecycle and
  scientific-approval states for every required EOP field; a
  supported-domain intersection rule; and explicit non-result/result outcome families.
  The final leap/EOP audit accepts only independently approved final Bulletin B/final-
  derived `UT1-UTC`,`xp`,`yp`, selects Gazette 13's four-point example with complete
  support, interpolates UT1 through continuous `UT1-TAI`, restores the IERS Conventions
  2010 ocean-tide and applicable libration terms exactly once after interpolation, and keeps Bulletin C as
  leap-event authority with a separately selected official IERS/IANA machine transport.
  It forbids request-time download/cache fallback, zero/nearest/extrapolated EOP,
  estimate/preliminary/prediction fallback, expired-for-request leap data, and every
  unapproved field quality or degraded execution. No production artifact/hash, exact
  restoration source/configuration, update cadence, observer datum/range, concrete date
  endpoint, prediction horizon, degraded bound, or wire serialization is approved.
  Concrete date values are activation data derived in 2D/2E from the approved domain
  intersection; their absence does not block generic implementation. The semantic-
  scope and leap/EOP audits make core deterministic failure precedence and field-
  specific fail-closed dispositions normative, while stable wire codes remain under
  review. ScientificProfileV1 normatively emits
  geometric-only output, requests no refraction or atmosphere, supplies no default
  atmosphere, keeps geometric, refracted-apparent, physical-dip, terrain, renderer,
  and learner horizon meanings distinct, emits no aggregate visibility, and retains
  earlier valid scientific states through later classifications, including all
  geometric coordinates, provenance, warnings, and statuses. SOFA/Astropy input/
  default/low-altitude behavior is evidence, not UFUQ policy. The model, input ranges/provenance,
  near/below-horizon domain, warnings, physical dip, terrain, photometric/daylight,
  extinction/transparency, cloud/weather, light-pollution, renderer, and learner-
  eligibility policies remain unresolved. No approved or warning-bearing refracted
  result is reachable before the model/input/domain/warning/tolerance/operating-domain
  gates and named astronomy review are complete. Milestone 2C.5A freezes a separate
  24-record scientific experiment protocol and machine registry. It classifies 17
  synthetic-only records as runnable for bounded measurement/invariant evidence, five
  as project-decision blocked, one as required-data blocked, and one as deferred until
  production exists. It adds no numerical body/result, source-derived input,
  production selection, or tolerance. Same-family Astropy/PyERFA/ERFA agreement is
  explicitly non-independent, and all numerical measurements remain without
  acceptance until AST-006 approves bounded terms and an operation-specific
  threshold; the 2C.5C review-draft ledger supplies neither. Milestone 2C.5B then
  completes 9/9 reviewed Batch 01 synthetic scopes inside the non-production
  Python tool. It promotes the unchanged locked PyERFA release to a direct tool
  dependency, passes 24 exact guard/status/replay checks with no failures, and has six
  measurement-only checks covering 27 measurement records, all
  `MEASURED_NO_ACCEPTANCE`. It adds no production implementation, source-derived
  propagation, independent scientific validation, or policy/tolerance approval.
  Milestone 2C.5C interprets those frozen results in a separate 49-term AST-006
  ledger: 45 terms retain an unbounded numerical-bound state and four aggregate
  ledger terms are exact non-numerical guards, distinct from the 24 Batch checks. It
  separates source, model, Earth-orientation/time, observer, atmosphere,
  implementation, scene, and learner layers; keeps scene and learner budgets outside
  astronomy accuracy; defines boundary-specific metrics and candidate conservative/
  covariance/RSS rules; and ranks the remaining runnable synthetic experiments.
  Every required numerical term remains unbounded, RSS remains prohibited without
  justified independence, all six tolerance classes are blocked, and the review
  recommendation is `FINAL_TOLERANCE_NOT_JUSTIFIED`. No hashed Batch input changed.
  Milestone 2C.6 defines `ScientificProfileV1` and separates lifecycle
  gates. V1 is one-preset, one-bounded-UTC-domain, source-neutral, offline,
  fail-closed, geometric-only, refraction-disabled, and without aggregate visibility.
  Its generic `ObserverPreset` contract and the UMPSA Pekan Faculty site identity are
  preimplementation semantics; exact coordinates, Earth model, typed height, accuracy,
  provenance and immutable observer artifact move to 2D. I/311 source authority also
  moves to 2D if retained. Production/reference residuals,
  any stronger independent validation required by the claimed release boundary,
  numerical error-budget population, and tolerance approval follow implementation and
  do not precede it. The semantic-scope audit makes the profile boundary, geometric-
  only/refraction-disabled/no-visibility scope, and outcome/precedence/singularity/
  warning/pending-validation contracts normative. `GEOMETRIC_RESULT_PENDING_VALIDATION`
  is executable after the remaining gates; `APPROVED_GEOMETRIC_RESULT` remains
  unreachable until postimplementation scientific acceptance. The route/effect/
  production mapping and final-only leap/EOP semantic policy are resolved for
  implementation entry. Exact production EOP/leap artifacts, field evidence,
  interpolation/restoration configuration, concrete observer record and actual
  supported-time bounds are 2D/2E activation data, not additional 2C blockers.
- **Status:** approved for bounded ScientificProfileV1 implementation entry; real-data
  execution and scientific acceptance remain gated
- **What code it affects:** Astronomy-core transformations, scenario inputs,
  reference fixtures, errors, and scientific tolerances.
- **Validation required:**
  - **PRE_IMPLEMENTATION:** implement the now normative pure-TypeScript route/effect/
    final-only leap/EOP mapping and typed
    UTC/time-domain boundary, exclusions, fail-closed precedence, warnings/statuses,
    and pending-validation outcome without promoting it to scientific acceptance.
    Review Batch 01 only for its bounded synthetic claims.
  - **2D/2E ACTIVATION:** select and approve exact official EOP/leap bytes, Bulletin C
    consistency, per-field final support, exact IERS interpolation/restoration source
    configuration, bundle hashes, observer/source artifacts and supported-time bounds
    before any real ProfileV1 execution.
  - **POST_IMPLEMENTATION:** compare the TypeScript implementation with pinned
    reference fixtures across the approved domain, record residuals and statuses,
    populate `F-001`/`F-005` and other applicable ledger evidence, activate
    `test:reference`, and seek operation-specific tolerance approval before scientific
    acceptance.
  - **STRONGER_INDEPENDENT_VALIDATION:** evaluate USNO NOVAS or another genuinely
    independent positional-astronomy path. Astropy/PyERFA/ERFA/SOFA shared lineage
    cannot satisfy this stage.

## IMP-010 — Scene coordinate adapter

- **Decision:** Mapping from horizontal astronomy coordinates to Three.js.
- **Current choice:** Domain ENU maps to Three.js `+X east`, `+Y up`, `-Z north`; scene
  code is an adapter and never the astronomy oracle. It consumes a labelled valid
  direction with its pending-or-approved validation state, never promotes that state,
  and does not apply refraction, horizon corrections, or scientific visibility policy.
- **Status:** approved
- **What code it affects:** Astronomy-to-scene adapter, camera orientation, raycasting,
  deterministic scene tests.
- **Validation required:** Cardinal-direction, horizon/zenith, camera, and raycast tests
  independent of screenshots.

## IMP-011 — Reviewed sky-pattern and guidance content

- **Decision:** Exact helper patterns, Arabic names/labels, memberships, line segments,
  guidance relationships, instructional geometry/explanations, and route content for
  learner-facing lessons.
- **Current choice:** No concrete helper pattern or learner-facing mapping is selected.
  The first reviewed route may use Banat Na'sh or Dhat al-Kursi to reach Al-Jady;
  synthetic IDs may exercise generic interfaces in a technical spike but cannot ship as
  content.
- **Status:** unresolved
- **What code it affects:** Curated `SkyPattern`, `GuidanceRelationship`, and
  `LessonRoute` data; scene overlays; assessment targets; lesson/scaffold configuration;
  content fixtures.
- **Validation required:** Applicable cultural/scientific/educational source review,
  stable-ID and relationship integrity, conflict record, verification status, and
  explicit historical-versus-pedagogical classification.

## IMP-018 — Data-driven celestial guidance model

- **Decision:** How patterns, guidance edges, multi-step lessons, and alternative paths
  are represented and selected.
- **Current choice:** Versioned generic `SkyPattern`, `GuidanceRelationship`, and
  `LessonRoute` records form a content graph. Routes can compose helper pattern to Banat
  Na'sh or Dhat al-Kursi, either pattern to Al-Jady, Al-Jady to True North, and True
  North to Qibla. The server selects only routes whose resolved required stars are
  available in the approved scenario; no named pattern is hardcoded as the universal
  entry point.
- **Status:** approved
- **What code it affects:** Catalogue/curation schemas, generated runtime content,
  scenario route selection, lesson renderer, assessment-step orchestration, scaffold
  configuration references, contracts, and fixtures.
- **Validation required:** Schema/referential-integrity tests; ordered-step and
  alternative-path tests; missing-star route exclusion; applicable-scenario filtering;
  review-status enforcement; server-authority and no-special-case dependency tests.

## IMP-012 — Minimal scenario and scoring policy

- **Decision:** Observer/time scenario, eligible lesson route, required-star
  availability, target evidence, supported answer form, and learner/scientific
  tolerances for the first vertical slice.
- **Current choice:** The generic `ObserverPreset` contract selects only
  `umpsa-pekan-faculty-of-computing` for V1 and may be implemented without numerical
  coordinates. Milestone 2D owns its exact reference point, coordinates, Earth model,
  typed height, accuracy, provenance, version and approval artifact before real V1
  execution. No production scenario or numeric tolerance is selected. The observer/time
  input remains separate from learner-answer and scoring policy; a missing final
  scientific tolerance blocks later acceptance, not implementation start.
- **Status:** unresolved
- **What code it affects:** Scenario/route fixture, route-selection use case,
  assessment-core scoring, API validation, browser interaction, reference tests.
- **Validation required:** Approved sourced scenario and route, complete required-star
  availability, independent expected result, alternative/ineligible-route cases,
  boundary tests, and justified operation/task tolerances.

## IMP-013 — BKT arithmetic boundary

- **Decision:** Shape and update order of the learner model.
- **Current choice:** One standard binary BKT state per KC, observation posterior first
  and learning transition second, implemented in the pure `tutoring-core/src/bkt`
  module.
- **Status:** approved
- **What code it affects:** BKT value types, pure update function, replay records,
  parameter interface.
- **Validation required:** Independently calculated sequences, edge/property tests, and
  deterministic numeric behavior; production parameters are handled separately.

## IMP-014 — BKT parameters and adaptive cues

- **Decision:** Production parameters, observation eligibility, threshold, cue content,
  and GUIDED/FADING/INDEPENDENT transition policy.
- **Current choice:** Interfaces and typed decision states may be scaffolded; production
  values and cue semantics are unresolved.
- **Status:** unresolved
- **What code it affects:** BKT configuration, the `tutoring-core/src/adaptive-policy`
  module, lesson cues, mastery display, and model-policy tests.
- **Validation required:** Approved worked sequences, sensitivity results, complete
  observation decision table, and cue/state transition fixtures before Phase 3
  acceptance.

## IMP-015 — Persistence transaction model

- **Decision:** Atomic submission and retry architecture.
- **Current choice:** MySQL/InnoDB transaction with immutable scenario, request
  fingerprint, stored canonical result, attempt/model/scaffold record, monotonic per-KC
  revision, fixed lock order, and bounded recognized retries.
- **Status:** approved
- **What code it affects:** API use case, persistence ports/adapters, schema/migrations,
  integration tests.
- **Validation required:** Freeze the exact MySQL profile before Phase 4 acceptance and
  demonstrate rollback, duplicate, mismatch, cold-start, stale, deadlock, and concurrent
  ordering cases against that profile.

## IMP-016 — Development identity boundary

- **Decision:** How pre-authentication phases exercise API workflows.
- **Current choice:** A local fixture identity adapter may be used for non-production
  technical work and must be excluded fail-closed from production artifacts.
- **Status:** provisional
- **What code it affects:** API composition root, development configuration, build
  guards, early E2E fixtures.
- **Validation required:** Production-mode build and route tests prove the adapter and
  bypass capability are absent before Phase 4/5 acceptance.

## IMP-017 — Production account policy

- **Decision:** Registration/enrollment, identifier, recovery, MFA, session lifetimes,
  revocation, and privileged capabilities.
- **Current choice:** Ports and capability types may be scaffolded; production policy is
  unresolved.
- **Status:** unresolved
- **What code it affects:** Authentication/session adapters, account schema, routes,
  authorization and security tests.
- **Validation required:** Approved policy plus threat-model, session, authorization,
  IDOR, recovery, rate-limit, and production fixture-exclusion tests before account or
  deployment readiness.

## IMP-019 — Runtime validation ownership

- **Decision:** Where untrusted serialized data and HTTP payloads are validated.
- **Current choice:** `catalogue-schema` may provide framework-free runtime schemas and
  validators from its `catalogue`, `content`, and `artifact` modules. `contracts` may
  provide framework-free validators beside versioned DTOs. Domain entities, database
  rows, React props, application services, and human curation source records remain in
  their owning layers. No validation library is selected until Phase 1 introduces a
  real validator and can justify its size, API, maintenance, and cross-runtime support.
- **Status:** approved
- **What code it affects:** Trust-boundary parsing, catalogue/content artifact loading,
  API request/response validation, package dependencies, and schema tests.
- **Validation required:** Invalid/unknown input tests, web/API agreement on serialized
  DTOs, framework-free package checks, and one documented dependency decision before a
  validator library is added.
