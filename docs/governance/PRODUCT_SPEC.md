# Product specification

## Purpose and classification

UFUQ teaches a learner to reason from visible celestial patterns to True North and then to Qibla inside a browser-based 3D sky. It combines a mathematically testable simulation with per-skill adaptive support.

- **CONFIRMED:** browser delivery; React/Three.js; small static star data; five cognitive skills; raycast/equivalent spatial answers; BKT; visual scaffolding; learner/admin roles; mathematical, performance, and educational evaluation.
- **CLARIFIED:** the numbered requirements below close omissions in the report's mapping table without adding a new product category.
- **PROPOSED DEVIATION:** items are linked to `REPORT_DEVIATIONS.md` and are not approved by this document.
- **MANUAL DOMAIN DECISION:** scientific, cultural, research, and policy inputs are linked to `OPEN_QUESTIONS.md`.

## Target users

- **Learner — CONFIRMED:** a beginner, particularly a Muslim learner, studying traditional celestial orientation without assumed astronomy expertise.
- **Administrator — CONFIRMED:** an authorized person who views aggregate or authorized learner progress and system health; not an editor of attempts or mastery.
- **Researcher/supervisor — CLARIFIED:** an off-product governance role that approves fixtures, protocol, and anonymized evidence. It is not automatically an application role.

## Learning outcomes

A learner should be able to:

1. identify Banat Na'sh;
2. recognise Dhat al-Kursi;
3. locate Al-Jady/Polaris from the intended pattern relationships;
4. estimate True North from the celestial evidence;
5. derive the Qibla bearing from True North for an approved location;
6. demonstrate these skills without instructional cues after guided practice.

Outcomes 1–5 are **CONFIRMED** separate knowledge components. Outcome 6 is a **CLARIFIED** interpretation of the report's independent-recall evaluation; the evidence rule remains BKT-003.

## MVP scope

### In scope

- Desktop-class modern browser 3D sky for approved locations and selected time, defaulting to current local time (**CONFIRMED/CLARIFIED**).
- Approved small catalogue subset, magnitude policy, Arabic labels, cultural pattern relationships, and line segments (**CONFIRMED**, values **MANUAL DOMAIN DECISION**).
- Structured tasks for the five knowledge components, including raycast object selection and direction/bearing responses (**CONFIRMED**).
- Server-side scoring, angular error, feedback, BKT update, and visual scaffold decision (**CLARIFIED**).
- Learner account, own progress, assessment sessions, retry-safe attempt submission, and minimal aggregate read-only administrator analytics (**CONFIRMED/CLARIFIED**). Learner-level admin access, research export, operational-log detail, enrollment, and privacy maintenance are separate approved capabilities.
- Pre-test, guided learning, post-test, independent recall, rendering/performance, usability, and mathematical validation (**CONFIRMED**).
- Keyboard-accessible application shell, instructions, progress, and equivalent answer control where approved (**CLARIFIED**; ACC-001 remains open).

### Optional enhancements

These are not MVP acceptance dependencies: arbitrary/global location authoring, device geolocation or sensors, mobile/VR/AR modes, weather or physically realistic sky brightness, large catalogues, lesson-authoring CMS, advanced analytics, gamification, additional languages, social features, forgetting/individualized BKT variants, and ellipsoidal-geodesic runtime Qibla.

### Out of scope

- A replacement for Stellarium, a general-purpose planetarium, an iframe/external planetarium engine, a native application, or a mobile-only application.
- Religious rulings, legal/religious certification, or official mosque alignment.
- Navigation or emergency use.
- Administrator mutation of historical assessment evidence or mastery.
- Claims that a BKT probability alone proves learning.
- Manual copying of star coordinates from websites.

## Functional requirements

| ID | Requirement | Class | MVP |
|---|---|---|---|
| FR-01 | Render the approved star subset for an approved observer location and selected instant; selected time defaults to current local time. | CONFIRMED/CLARIFIED | Yes |
| FR-02 | Apply the approved visibility, horizon, and apparent-magnitude policies and prevent non-assessable objects from being accepted. | CONFIRMED; values manual | Yes |
| FR-03 | Deliver versioned structured scenarios for each learning outcome, with a single primary knowledge component per scored task; persist an immutable authoritative snapshot and expected mastery revision. | CONFIRMED task behavior; CLARIFIED safeguard | Yes |
| FR-04 | Capture object selection by raycasting or an equivalent 3D spatial method and direction/bearing responses; calculate correctness from raw evidence. | CONFIRMED | Yes |
| FR-05 | Authenticate learners and administrators and enforce role and record ownership. | CONFIRMED | Yes |
| FR-06 | After an accepted response, persist a typed observation/transition-only/no-update decision and update the separate learner/KC BKT state only when the approved policy makes it eligible. | CONFIRMED BKT behavior; CLARIFIED decision contract | Yes |
| FR-07 | Select, maintain, fade, remove, or restore visual scaffolding from the approved adaptive policy. | CONFIRMED/CLARIFIED | Yes |
| FR-08 | Compute star directions, True North, and Qibla bearing using one versioned astronomy policy. | CLARIFIED | Yes |
| FR-09 | Create and retain one mastery state per learner and cognitive skill, including the parameter/policy version needed for replay. | CLARIFIED | Yes |
| FR-10 | Return explanation-safe feedback, angular/selection result, mastery transition, and next scaffold without exposing answer keys prematurely. | CLARIFIED | Yes |
| FR-11 | Record authoritative server-issued assistance separately from untrusted render telemetry and distinguish independent recall from guided/fading attempts. | CLARIFIED; DEV-004/006 | Yes |
| FR-12 | Let a learner view only their own progress by skill and independent-evidence status. | CLARIFIED from UC-104 | Yes |
| FR-13 | Let an administrator read aggregate analytics; any learner-level data, operational logs, exports, enrollment, or privacy maintenance requires a separate authorized capability and audit. No ordinary analytics capability edits evidence. | CONFIRMED read-only aggregate baseline; CLARIFIED capability split | Yes |
| FR-14 | Preserve at most one unresolved submission per learner/KC locally, retry it with idempotency and visible reconciliation, and block advancement of that KC until the server result arrives or the stale task is safely reissued. | CONFIRMED local-cache intent; CLARIFIED safeguard | Yes |
| FR-15 | Load only schema-valid, checksum-matching, reviewed, versioned generated catalogue data. | CLARIFIED | Yes |

## Non-functional and evaluation requirements

| ID | Requirement | Measurable interpretation | Class |
|---|---|---|---|
| NFR-01 | Interactive performance | On PERF-001's frozen device/scene and valid-run conditions, retain raw traces from the approved warm-up/repeated measurement and demonstrate the report's at-least-30-FPS and under-100-ms raycast interpretations; percentile/window algorithms and any input-to-feedback measure are frozen before use. | CONFIRMED targets; CLARIFIED method manual |
| NFR-02 | Mathematical accuracy | Every approved independent fixture is within its operation-specific AST-006 tolerance; no tolerance may default silently. | CONFIRMED/CLARIFIED |
| NFR-03 | Reliable mastery persistence | No accepted submission lacks its immutable attempt and matching model/scaffold decision (including explicit no-op); no rejected/rolled-back submission changes evidence or state. | CONFIRMED reliability intent; CLARIFIED invariant |
| NFR-04 | Security and authorization | Every protected API route denies unauthenticated, wrong-capability, and wrong-owner access; intentionally public authentication routes are allowlisted/rate-limited; the approved ASVS 5.0.0 risk profile has no unresolved release blocker. | CLARIFIED safeguard |
| NFR-05 | Atomic and duplicate-safe submission | Concurrent identical key+fingerprint retries cause exactly one attempt/decision; same key with different content conflicts; distinct current-revision attempts form one serialized locked mastery chain. | CLARIFIED safeguard |
| NFR-06 | Reproducibility | Scenario, catalogue, astronomy/EOP, tolerance, BKT/scaffold, contract, database migration, and software-build identifiers link to the permitted artifact/configuration or immutable result needed for the stated replay period. | CLARIFIED safeguard |
| NFR-07 | Browser/WebGL compatibility | Critical journey passes the pinned primary study browser; approved compatibility smoke/full journeys cover only the additional engines claimed as supported. Exact revisions, OS/GPU/WebGL renderer and claim scope are retained. | CLARIFIED; PERF-001/SCOPE-002 stage breadth |
| NFR-08 | Accessibility | DOM/core journey has zero automated serious/critical violations and passes documented keyboard, focus, zoom, contrast, and reduced-motion checks; spatial equivalence is governed by ACC-001. | CLARIFIED |
| ER-01 | Independent scientific validation | Fixed astronomy and Qibla fixtures are produced by an implementation independent from runtime and reviewed with sources/versions. | CONFIRMED/CLARIFIED |
| ER-02 | Tutoring validation | BKT sequence/oracle tests pass and scaffold behavior is evaluated separately from learning effectiveness. | CONFIRMED/CLARIFIED |
| ER-03 | Educational/user evaluation | Approved no-hint pre/post/immediate-independent protocol, task accuracy/time/assistance, and SUS are reported; mean SUS target is at least 68. Delayed recall is required only if EDU-001–004 approve it. Causal claims follow EDU-003. | CONFIRMED core evaluation; delayed design manual |

## Learner workflow

1. Sign in and receive an authorized session.
2. Enter a pre-test or learning session with approved observer location and instant.
3. Inspect the 3D sky and task instructions; the UI displays only the current scaffold state's approved cues.
4. Select an object or submit a direction/bearing. The client sends raw typed evidence plus scenario version and an idempotency key.
5. The server validates the scenario, scores the response, atomically records the attempt and eligible BKT update, and selects the next scaffold state.
6. The learner receives feedback and continues. Network failures produce a visible bounded pending state and ordered retry.
7. The learner views own per-skill progress and completes no-hint post-test/independent recall tasks under the approved protocol.

## Administrator workflow

1. Sign in through the restricted administrator process.
2. View authorized aggregates and, only where policy permits, learner-level progress and operational failures.
3. Export approved pseudonymized research data only through a separately authorized,
   purpose-recorded capability and schema version; it is not implied by aggregate
   analytics access.
4. Never alter historical attempts or mastery through analytics. DEV-012, if approved, provides a separate audited privacy-maintenance workflow.

## Layered acceptance

Acceptance is not one all-or-nothing claim:

1. **Core research software demonstrated:** the approved Phase 1–3 science-to-learning
   path passes applicable FR/NFR/ER-01/ER-02 gates with fixture identities and no
   personal/participant data. This is not production-ready or evidence of learning.
2. **Study-ready software MVP:** all FR-01–FR-15 and applicable NFR-01–NFR-08 gates
   for the approved study deployment pass; SEC/ACC/DEP/EDU approvals are in force;
   authentication has replaced fixture identity; restricted/licensed-data scans are clean;
   and required restore/security evidence exists.
3. **Thesis evaluation completed:** ER-03 is satisfied under the frozen protocol and
   the evidence/analysis reproduces. If recruitment, ethics, or power prevents this, the
   phase may close only as a documented bounded outcome: ER-03 remains unsatisfied and
   claims are reduced to the scientific, software, usability-pilot, and model-behavior
   evidence actually obtained.

Production/public release may require additional P5 browser, operations, and security
hardening beyond a controlled study deployment. Passing BKT unit tests or reaching a
mastery threshold is not, by itself, evidence that learners improved.
