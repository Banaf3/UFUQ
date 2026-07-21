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
- **Current choice:** `astronomy-core`, `assessment-core`, `bkt-core`, and
  `adaptive-policy` are pure; application use cases own ports; adapters depend inward.
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
- **Current choice:** Vitest for unit/contract tests and Playwright for browser tests;
  real MySQL integration tests are a separate suite when persistence appears.
- **Status:** provisional
- **What code it affects:** Test configuration, package scripts, fixtures, CI jobs.
- **Validation required:** Phase 0 self-tests prove test discovery, deterministic seed
  reporting, failure exit codes, and separation of unit, reference, integration, and E2E
  suites.

## IMP-007 — Repository package layout

- **Decision:** Initial folders and package names.
- **Current choice:** Use the layout in `ARCHITECTURE.md`: `apps/web`, `apps/api`,
  `packages/astronomy-core`, `packages/assessment-core`, `packages/bkt-core`,
  `packages/adaptive-policy`, `packages/contracts`, `packages/catalogue-schema`, and
  `tools/catalogue`.
- **Status:** approved
- **What code it affects:** Folder creation, workspace globs, dependency graph, public
  entry points.
- **Validation required:** No unresolved scientific, cultural, BKT, participant,
  security, or deployment value changes these folder/package boundaries.

## IMP-008 — Catalogue source and runtime subset

- **Decision:** Exact catalogue/table/version, licence/access route, subset, fields,
  quality rules, and canonical runtime artifact.
- **Current choice:** No production source or subset is selected; Hipparcos I/239 is a
  candidate for the technical spike only.
- **Status:** unresolved
- **What code it affects:** Catalogue acquisition adapter, transform/schema fields,
  generated artifact, scientific fixtures.
- **Validation required:** Deterministic rebuild, provenance/licence manifest,
  schema/range/quality checks, checksum equality, and scientific review before the
  validated vertical slice.

## IMP-009 — Astronomy transformation pipeline

- **Decision:** Exact reference-frame/time/Earth-orientation/observer transformation
  algorithm, supported range, effects, failure modes, and error budget.
- **Current choice:** Typed transformation boundaries and fixed axis/sign conventions
  are approved; the production algorithm and implement-or-omit effect matrix are
  unresolved.
- **Status:** unresolved
- **What code it affects:** Astronomy-core transformations, scenario inputs,
  reference fixtures, errors, and scientific tolerances.
- **Validation required:** Independent pinned oracle cases, an effect/error budget, and
  operation-specific approved tolerances before scientific acceptance.

## IMP-010 — Scene coordinate adapter

- **Decision:** Mapping from horizontal astronomy coordinates to Three.js.
- **Current choice:** Domain ENU maps to Three.js `+X east`, `+Y up`, `-Z north`; scene
  code is an adapter and never the astronomy oracle.
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
- **Current choice:** Contract/type shape may be scaffolded; no production scenario or
  numeric tolerance is selected.
- **Status:** unresolved
- **What code it affects:** Scenario/route fixture, route-selection use case,
  assessment-core scoring, API validation, browser interaction, reference tests.
- **Validation required:** Approved sourced scenario and route, complete required-star
  availability, independent expected result, alternative/ineligible-route cases,
  boundary tests, and justified operation/task tolerances.

## IMP-013 — BKT arithmetic boundary

- **Decision:** Shape and update order of the learner model.
- **Current choice:** One standard binary BKT state per KC, observation posterior first
  and learning transition second, implemented in pure `bkt-core`.
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
- **What code it affects:** BKT configuration, adaptive-policy, lesson cues, mastery
  display, model-policy tests.
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
