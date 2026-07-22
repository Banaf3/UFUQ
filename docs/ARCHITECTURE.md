# System architecture

## Decision summary

Use a **TypeScript modular monolith in a monorepo**: one React browser application, one Express-compatible API process, one MySQL/InnoDB database, and framework-free domain packages. This is **CLARIFIED** and fits the report's technology baseline without introducing distributed-system overhead.

React Three Fiber is the proposed React integration layer over Three.js (**CLARIFIED**); direct Three.js APIs remain available for raycasting and performance-sensitive adapters. The application is not replaced by an external planetarium.

Unless a section explicitly says otherwise, implementation-detail conclusions in this document are **CLARIFIED**. Report changes are linked as **PROPOSED DEVIATION**, and values requiring authority are left as **MANUAL DOMAIN DECISION**.

## Architecture style and rationale

- A modular monolith keeps deployment and transactions feasible for a bachelor-level FYP while enforcing boundaries through packages and TypeScript project references.
- Pure deterministic domain packages make astronomy, angular assessment, BKT, and policy behavior independently testable.
- Server authority prevents client manipulation of correctness/mastery and gives retries one transactional truth.
- Versioned generated data separates scientific provenance from runtime efficiency.
- A thin 3D adapter isolates Three.js coordinate and interaction concerns from astronomy conventions.

Microservices, event brokers, and a distributed cache are intentionally absent. Add them only in a future ADR backed by measured need.

## Proposed repository layout

```text
apps/
  web/                    React UI, R3F scene, browser adapters
  api/                    composition root, HTTP/auth adapters, application use cases,
                          outbound ports and MySQL/session adapters
packages/
  astronomy-core/         coordinate/time/Qibla pure functions
  assessment-core/        task answer types and pure scoring
  tutoring-core/          pure bkt/, observations/, adaptive-policy/ modules
  contracts/              versioned serialized API DTOs and pure validators
  catalogue-schema/       catalogue/, content/, artifact/ schemas and validators
data/
  manifests/              tracked provenance/licence/query records
  raw/                    immutable acquired bytes, ignored by default
  curation/
    patterns/             reviewed SkyPattern sources
    relationships/        reviewed GuidanceRelationship sources
    routes/               reviewed LessonRoute sources
  generated/              deterministic deployable JSON, if licence permits
tools/
  catalogue/              npm workspace; internal acquisition/transform/verify modules
  astronomy-reference/    non-npm independent Python/Astropy fixture producer
tests/
  reference/              independent astronomy fixtures/generator metadata
  integration/            API and real-MySQL tests when persistence exists
  e2e/                    browser journeys and visual baselines
  performance/            frozen scene and benchmark definitions
docs/                     specifications, decisions, evidence indexes
```

The eight npm workspaces are `apps/web`, `apps/api`, the five packages shown above, and
`tools/catalogue`. `tools/astronomy-reference` is deliberately outside the npm and
production dependency graphs. This consolidated layout is approved for the empty Phase
0 scaffold; domain behavior remains subject to the phase-specific choices in
`IMPLEMENTATION_DECISIONS.md`.

## Logical layers and allowed dependencies

```mermaid
flowchart TB
  WEB[apps/web: presentation and 3D adapter]
  HTTP[API inbound adapters and composition]
  USE[API application use cases and outbound ports]
  CONTRACTS[contracts and catalogue schemas]
  ASSESS[assessment-core]
  ASTRO[astronomy-core]
  TUTOR[tutoring-core: bkt, observations, adaptive policy]
  INFRA[API outbound adapters: MySQL, session, logging]

  WEB --> CONTRACTS
  WEB --> ASTRO
  HTTP --> CONTRACTS
  HTTP --> USE
  USE --> CONTRACTS
  USE --> ASTRO
  USE --> ASSESS
  USE --> TUTOR
  INFRA --> USE
  ASSESS --> ASTRO
```

Rules:

1. Pure packages may depend only on other explicitly allowed pure packages and standard TypeScript/ECMAScript facilities.
2. No pure package imports React, Three.js, R3F, Express, a SQL client, Node-only I/O, DOM/browser globals, or application code.
3. `assessment-core` may consume astronomy value objects/functions.
   `tutoring-core` consumes typed correctness observations supplied by the API and has
   no dependency on `assessment-core`; its BKT and adaptive-policy modules remain
   logically separate. The reverse directions are forbidden.
4. Applications compose packages through public entry points. Applications do not import each other's internals. API use cases define outbound ports; MySQL, session, logging, and framework adapters implement those ports and depend inward. The composition root is the only place that constructs concrete adapters.
5. Contracts carry units, coordinate frame, time, and version fields explicitly. No unlabelled numeric tuple crosses a boundary.
6. The browser may calculate positions for presentation, but server recalculation is authoritative for scoring.
7. The browser does not import authoritative scorer, target-resolution, or tolerance-resolution entry points from `assessment-core`. Raw answer DTOs live in `contracts`; bundle/import tests enforce this boundary.
8. `contracts` and `catalogue-schema` may execute framework-free validation at trust
   boundaries. They do not own domain entities, database rows, React props, cultural
   source records, or application services.
9. Runtime applications/packages never import tools. `tools/catalogue` may import only
   `catalogue-schema`; the independent Python oracle never imports production astronomy
   and communicates only through versioned JSON fixtures consumed by reference tests.

## Responsibilities

| Boundary | Owns | Must not own |
|---|---|---|
| Web/UI | Routing, forms, accessible controls, status/error display, own-progress views | Correctness, mastery truth, SQL, secrets |
| 3D scene adapter | Camera, star meshes/buffers, labels/segments, raycaster, resize, conversion from domain vector to Three vector | Sidereal/Qibla formulae, BKT, persistence |
| API inbound/composition | HTTP/session adaptation, schema validation, composition, response shaping | Domain decisions or SQL embedded in controllers |
| API use cases/ports | Authz, scenario issuance, submission orchestration, server scoring, transaction and session ports | UI, rendering, or concrete database/framework code |
| Astronomy core | Explicit time/frame transformations, horizontal/vector conversion, Qibla/angle functions | Catalogue I/O, Three objects, API/database |
| Assessment core | Typed answer validation and scoring against versioned target/tolerance | UI effects, SQL, BKT persistence |
| Tutoring core: BKT | Observation posterior, learning transition, parameter constraints | Hint UI, database, educational claims |
| Tutoring core: observations/policy | Observation semantics and scaffold transition from approved evidence/policy version | Assessment scoring, rendering implementation, mutable persistence |
| Persistence adapter | Transactions, locking, constraints, idempotency, queries | Domain formulas |
| Catalogue tool | Source retrieval, provenance, normalization, `SkyPattern`/`GuidanceRelationship`/`LessonRoute` curation merge, schema/checksum output | Runtime user data or hardcoded lesson branching |

## Container view

```mermaid
flowchart LR
  L[Learner browser] -->|HTTPS same origin| RP[Reverse proxy / TLS]
  A[Administrator browser] -->|HTTPS same origin| RP
  RP --> WEB[Static web + generated JSON]
  RP -->|/api| API[Node/TypeScript API]
  API --> DB[(MySQL / InnoDB)]
  PIPE[Offline catalogue pipeline] -->|same reviewed artifact/hash| WEB
  PIPE -->|same reviewed artifact/hash| API
  ORACLE[Independent Astropy/USNO fixture process] -->|fixed test fixtures only| TESTS[Test suites]
  TESTS --> WEB
  TESTS --> API
```

The database is private to the API. The API and browser must refuse scenario issuance or
loading when their catalogue hashes differ. Production is HTTPS-only. Static assets and
API should be same-origin to simplify session and CSRF controls. A single API instance
is the initial deployment candidate, subject to DEP-001; correctness must not depend on
in-memory session, scenario, idempotency, or mastery state.

## 3D scene architecture

`ScenePage` loads an immutable scenario snapshot and validated catalogue version. A scene controller derives render records from pure astronomy results. The R3F layer renders stars with buffer geometry/instancing, cultural line segments, approved labels, horizon/reference cues, and the camera. Per-frame animation/camera data stays outside ordinary React state; React state changes only for semantic UI events.

The raycast adapter converts pointer/keyboard answer controls into normalized answer evidence: target object ID or unit direction/bearing with camera/viewport metadata. It filters hidden/non-assessable objects and resolves overlaps with a documented deterministic policy. It never decides BKT or authoritative correctness.

Axes are fixed by `ASTRONOMY_SPEC.md`: `+Y` up, `-Z` north, `+X` east. Only one adapter converts domain east/north/up vectors to Three.js coordinates.

## Data-driven celestial guidance

Lesson structure is a versioned content graph, not a component-level sequence and not a
Banat Na'sh-specific state machine. Three generic content concepts are validated by
`catalogue-schema` and emitted by the data pipeline:

| Concept | Required content |
|---|---|
| `SkyPattern` | Stable ID; names and cultural labels; member star catalogue IDs; line segments keyed by catalogue ID; cultural-review status and content version |
| `GuidanceRelationship` | Stable ID; source pattern or star; target pattern, star, or direction; relationship type; instructional line/vector; explanation; applicable scenarios; verification status and version |
| `LessonRoute` | Stable ID; ordered learning steps referencing guidance relationships; prerequisite skills; allowed alternative guidance paths; scaffold-configuration reference; route version/status |

Pattern members and relationship geometry reference stable catalogue IDs; they never
duplicate astronomical coordinates. Direction targets such as True North and Qibla are
typed direction references, not fake stars or patterns. Exact names, helper patterns,
memberships, segments, relationships, explanations, and geometry remain provisional
until their applicable cultural/scientific/educational reviews are recorded.

The model supports composition such as:

- a reviewed helper `SkyPattern` guiding toward Banat Na'sh;
- a reviewed helper `SkyPattern` guiding toward Dhat al-Kursi;
- Banat Na'sh or Dhat al-Kursi guiding toward Al-Jady;
- Al-Jady guiding toward the True North direction; and
- True North supporting derivation of the scenario-specific Qibla direction.

These are permitted graph shapes, not approved concrete cultural records. A lesson may
start at any route step allowed by its prerequisites and scenario; no application
component assumes that Banat Na'sh is always first.

For each candidate `LessonRoute`, the server resolves the selected alternative into an
ordered relationship chain and computes the complete required-star set from every
referenced pattern, star endpoint, and instructional geometry. The scenario engine may
issue the route only when every required star is available under the approved
scenario's catalogue and availability/visibility policy, every reference resolves, and
the applicable review/verification statuses permit learner use. Otherwise that route is
ineligible; the engine may select another eligible approved route but may not silently
drop a step or substitute a pattern. Synthetic technical-spike routes are isolated from
learner-facing scenarios.

## Scenario authority and replay

Each issued scored task has an immutable server-side `ScenarioSnapshot`. A browser
response contains only its opaque scenario ID, raw answer evidence, contract version,
and idempotency key; it cannot replace authoritative fields. The snapshot records at
least:

- learner/session ownership, task ID and one primary KC;
- selected lesson-route ID/version, ordered step and relationship IDs/versions,
  selected alternative path, required-star IDs, and content/review-status hash;
- observer coordinates/datum/elevation, UTC instant, original display zone, and any
  deterministic seed;
- catalogue/schema/hash, astronomy algorithm and Earth-orientation dataset/hash or
  labelled approximation status, visibility and tolerance policy versions;
- BKT model, adaptive-policy, server-issued cue snapshot, session purpose, and the
  expected learner/KC mastery revision;
- scenario-generator and server build identifiers, issue/expiry state, and a server-only
  target/answer-key representation.

The database record, not a client token, is authoritative. A scored attempt retains the
scenario ID and all transition/result version links. Expiry and one-time-use rules are
validated against server time. A duplicate request with the same idempotency key and
request fingerprint returns the original committed result even after expiry; a new
submission against an expired, consumed, or stale-revision scenario is rejected without
state change. Old executable/data artifacts needed for replay follow the compatibility
and retention table below.

## Scenario and assessment workflow

```mermaid
sequenceDiagram
  participant W as Web client
  participant A as API
  participant D as Pure domains
  participant M as MySQL

  W->>A: Request authorized scenario
  A->>D: Build/validate versioned target
  A-->>W: Public scenario view + catalogue/policy versions
  W->>W: Render and capture raw answer
  W->>A: Submit raw evidence + idempotency key
  A->>M: Begin; claim key+fingerprint; lock session/scenario/mastery
  A->>D: Recompute target and score answer
  A->>D: Typed model decision + scaffold decision
  A->>M: Insert attempt/result; update revision if eligible; consume scenario
  A->>M: Commit
  A-->>W: Stored result + next scaffold + replay flag
```

The server rejects expired, consumed, unauthorized, incompatible, unversioned, or
stale-mastery-revision scenarios. Only one unresolved assessed scenario per learner/KC
is allowed. One scored task has one primary knowledge component. Compound learner
activity may produce multiple tasks but not an ambiguous multi-KC update; EDU-002 must
still validate that each task actually measures its claimed KC.

## BKT workflow

For every accepted response, the use case produces a typed model decision:
`OBSERVATION`, `TRANSITION_ONLY`, or `NO_MODEL_UPDATE`, with an approved reason and
session purpose. On an eligible observation it loads the skill-specific prior and
parameter/policy version, calls `tutoring-core/bkt` for posterior and transition, then
calls `tutoring-core/adaptive-policy`. A no-update decision persists an explicit no-op
rather than inventing an observation. The transaction stores the server-issued cue snapshot used for
eligibility; optional client render telemetry is untrusted and can never promote an
attempt to independent. Independent-recall status is separate from numeric mastery.
Details and manual policy gates are in `TUTORING_BKT_SPEC.md`.

## Persistence and atomicity

The six report entities are `User`, `CognitiveSkill`, `BktMasteryState`,
`AssessmentSession`, `AssessmentAttempt`, and `SystemLog`. Implementation-support
records additionally include `ScenarioSnapshot`, `IdempotencyResult`, durable
credential/session/recovery records, and capability/privacy/export audit records. Exact
personal-data fields and retention remain SEC-001/002. Research exports and catalogue
artifacts are not live user entities.

Before a learner can receive an assessed scenario, all five current-version mastery rows
are provisioned atomically in stable KC order from an approved `L0`, model version,
policy version, and initial scaffold. Fixture learners are seeded the same way. An
accepted response therefore never tries to lock a missing mastery row. Model-version
migration is BKT-002; it creates an auditable new chain or approved mapping and never
silently overwrites history.

One submission transaction, under the database profile approved in SYS-001:

1. authenticate and authorize session ownership;
2. canonicalize the endpoint, contract version, scenario ID, and validated raw evidence;
   calculate a request fingerprint and claim `(user_id, idempotency_key)`;
3. on an existing key, return its committed response only when the fingerprint matches;
   otherwise return a safe conflict and make no state change;
4. lock in the fixed order: idempotency result, assessment session, scenario, then
   `(user_id, skill_id)` mastery row;
5. validate ownership, expiry/consumption, catalogue/policy/build compatibility, and the
   scenario's expected mastery revision;
6. allocate the next committed attempt order, calculate authoritative score and typed
   model/scaffold decision in bounded pure code, and persist the attempt;
7. update the mastery row and monotonic `masteryRevision` only when the model decision
   requires it; persist the scaffold result and canonical response in the same unit;
8. mark the scenario consumed and idempotency result committed, then commit; retry the
   entire transaction only for the recognized, bounded SYS-001 cases.

Unique constraints include the approved normalized login identifier, active
`(user_id, skill_id)` state, `(session_id, attempt_order)`, scenario consumption, and
`(user_id, idempotency_key)`. Probabilities have database and domain range checks.
The different-payload/same-key case, concurrent cold start, stale expected revision,
post-commit response loss, deadlock, and lock-timeout paths are mandatory real-MySQL
tests. DEV-002–005 govern improved types and attempt semantics.

## Errors and offline retry

- Validation/auth/conflict errors are final and safely explained; they are not blindly retried.
- A transient network/5xx failure may keep only the unresolved raw submission for an
  affected learner/KC in bounded same-origin storage, display pending state, and retry
  it with one request in flight. The learner cannot advance that KC until the server
  result reconciles. Multi-opportunity offline tutoring is out of MVP scope.
- Each item has a stable UUID idempotency key and the complete versioned evidence required by the API, but no credential, session cookie, answer key, or server secret.
- Re-authentication pauses and resumes reconciliation. Server response replaces local prediction. A duplicate response returns the originally committed result.
- Queue age/size, sign-out/shared-device clearing, backoff, compatibility window, and
  terminal-error UX require the applicable Phase 3/4 decisions. A stale revision is never
  silently applied; it is rejected and the learner receives a newly issued task.

## Compatibility and retention contract

| Artifact | Required identifier/link | Compatibility behavior | Retention authority |
|---|---|---|---|
| API request/response | Contract version + canonical request fingerprint | Exact replay for supported duplicate; explicit rejection outside support | Technical window in Phase 3 plan |
| Scenario | Immutable scenario ID + generator/build version | No migration after issue; expire/reissue on incompatibility | Operational retention under SEC-001 |
| Catalogue/curation | Schema/version + content hashes | Exact hash must be available to score/replay | AST-001 licence and DEP-001 storage |
| Astronomy/EOP/tolerance | Algorithm/policy/EOP hashes | Exact historical implementation or retained immutable result/fixture | AST-003/006 and DEP-001 |
| BKT/scaffold | Model/policy versions + mastery revisions | No in-place edits; migration creates an audited chain | BKT-002/003 and SEC-001 |
| Software/database | Commit/build manifest + migration version | Rollback only when data/contract compatible | Applicable phase plan and deployment decision |

Recording a version is not sufficient by itself: the corresponding permitted artifact,
configuration, build recipe, or immutable result must remain retrievable for the claimed
replay period. If licence or privacy prevents retention, the evidence claim is reduced to
verification against retained hashes/results and stated explicitly.

## Deployment topology

```mermaid
flowchart TB
  Internet --> HTTPS[Managed TLS / reverse proxy]
  HTTPS --> STATIC[Versioned static web and catalogue assets]
  HTTPS --> API[Single stateless Node API process]
  API --> MYSQL[(Private MySQL InnoDB)]
  API --> LOG[Structured redacted logs]
  MYSQL --> BACKUP[Encrypted backups + restore drill]
```

Use separate least-privilege application and migration identities, environment-validated configuration, secret management, health/readiness endpoints, and versioned deployment artifacts. Hosting, retention, monitoring, and recovery targets are selected only for deployment readiness.

Opaque credentials and sessions use durable MySQL-backed adapters in the initial
topology; application use cases depend only on identity/session ports. The early-phase
fixture identity is a separate development adapter that is available only in a local,
non-personal-data build. Production configuration fails closed if that adapter or its
route is present, and an artifact inspection/E2E gate proves that no fixture principal can
be selected outside the approved development profile. Learner/admin capability policy,
recovery, MFA, and session lifetimes remain SEC-002.

Administrative authority is capability-scoped even if the UI presents one report-level
administrator role. Aggregate analytics, learner-level access, operational-log access,
research export, enrollment, and privacy maintenance are separate server permissions.
Only aggregate read-only analytics are baseline; the others require SEC-001/002 and
purpose/audit approval. Ordinary administrators never edit assessment evidence or
mastery.

Pin an Active or Maintenance LTS Node.js release in each implementation/release manifest and re-evaluate it at phase start; do not encode the documentation-date “latest” version as a permanent architecture constant.

## Rejected alternatives

| Alternative | Reason |
|---|---|
| Stellarium, iframe, or external planetarium engine | Violates the approved product boundary and hides the research implementation. |
| Native or mobile-only application | Contradicts browser-based scope. |
| Microservices/event broker | Adds deployment and consistency cost without FYP-scale benefit. |
| Browser-authoritative scoring/BKT | Enables tampering and inconsistent retries. |
| ORM/domain model shared indiscriminately with UI | Couples persistence to pure science and learning rules. |
| Full catalogue queried at runtime | Conflicts with small deterministic JSON and harms reproducibility/performance. |
| Manual coordinate transcription | Untraceable and error-prone. |
| Astropy inside production runtime | Breaks the proposed TypeScript boundary; use it independently for reference fixtures. |
| Start with extensive auth/admin work | Does not first prove the core research contribution; the active phase order keeps this work in Phase 4. |
