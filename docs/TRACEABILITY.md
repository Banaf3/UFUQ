# Requirements traceability

## Objectives and use cases

- **O-01:** identify and formalize celestial parameters, spherical calculations, and authentic Arabic nomenclature needed for True North and Qibla.
- **O-02:** build the browser 3D sky, spatial assessment, and BKT-driven tutoring system.
- **O-03:** evaluate mathematical accuracy, adaptive behavior, rendering performance, usability, and learning/independent recall.
- **UC-101:** authenticate and establish learner/administrator access.
- **UC-102:** enter a celestial environment for an approved location and selected time.
- **UC-103:** complete an assessment, receive adaptive feedback, and safely retry a failed submission.
- **UC-104:** view own learner progress.
- **UC-105:** view authorized read-only administrator analytics/logs.

The report's original mapping table omitted some stated objectives, BKT, evaluation, progress/admin, and retry relationships. The clarified FR/NFR/ER identifiers below preserve those report behaviors and make them testable.

## Report-authority crosswalk

This neutral crosswalk anchors only the already-paraphrased requirements. It does not
reproduce restricted report text. Relationship meanings are: **same** (direct report
behavior), **clarifies** (testable implementation detail), **new safeguard** (added
quality/security mechanism that does not remove report behavior), and **changes**
(requires the linked proposed deviation). Composite Product rows must be interpreted at
this clause level, not assigned one blanket authority.

| ID | Neutral report anchor | Relationship | Deviation/manual gate |
|---|---|---|---|
| O-01–O-03 | §1.3 | same | Domain values remain AST/EDU decisions |
| UC-101 | §3.4.2 table 3-2 | same | SEC-001–003 |
| UC-102 | §3.4.2 table 3-3 | same | AST-001–007 |
| UC-103 | §3.4.2 table 3-4 | same; retry/idempotency mechanics clarify | DEV-003–008; BKT/SYS gates |
| UC-104 | §3.4.2 table 3-5 | same | SEC-001/002 |
| UC-105 | §3.4.2 table 3-6 | same read-only aggregate baseline; capabilities clarify | DEV-012/014; SEC-001–003 |
| FR-01 | §3.3.3 FR-1 | same rendering/time/location; approved-scenario bound clarifies | AST-003/004/007 |
| FR-02 | §3.3.3 FR-2 | same; exact visibility semantics manual | AST-001/004; DEV-013 |
| FR-03 | §3.3.3 FR-3 | same task behavior; snapshot/revision new safeguard | EDU-002; SYS-001 |
| FR-04 | §3.3.3 FR-4 | same; typed evidence/server authority clarify | DEV-003/005; AST-006 |
| FR-05 | §3.3.3 FR-5 and §3.4.2 table 3-2 | same | DEV-010/011; SEC-001–003 |
| FR-06 | §3.3.3 FR-6 and §2.5.4 | same BKT intent; typed eligibility changes/clarifies | DEV-005/006/008; BKT-001/002/005 |
| FR-07 | §3.3.3 FR-7 and §2.5.4 | same adaptation intent; state machine changes/clarifies | DEV-004/007; BKT-003/004 |
| FR-08 | §1.3 O-01 and §3.7.1 | clarifies one versioned scientific policy | AST-003–007 |
| FR-09 | §2.5 and §3.6 tables 3-8/3-9 | clarifies durable per-KC/version state | DEV-002/004; BKT-002 |
| FR-10 | §3.4.2 table 3-4 and §3.4.5 | clarifies safe feedback/result contract | BKT-004 |
| FR-11 | §2.5.5 and §3.7.2 table 3-15 | changes Boolean/assisted semantics | DEV-004/006; BKT-001/003/004 |
| FR-12 | §3.4.2 table 3-5 | same | SEC-001/002 |
| FR-13 | §3.4.2 table 3-6 | same aggregate/read-only baseline; capability/log safeguards clarify | DEV-012/014; SEC-001–003 |
| FR-14 | §3.4.2 table 3-4 exception flow | same temporary local preservation; revision/idempotency clarify | SEC-001; SYS-001 |
| FR-15 | §1.4 and §3.3.2 | same static selected data; provenance pipeline clarifies/changes storage | DEV-009; AST-001/002 |
| NFR-01 | §3.3.4 NFR-1 | same targets; reproducible method clarifies | PERF-001 |
| NFR-02 | §3.3.4 NFR-2 and §3.8.1 | same; exact oracle/error budget clarifies | AST-003/005/006 |
| NFR-03 | §3.3.4 NFR-3 | same reliability intent; atomic/no-op invariant new safeguard | BKT-001; SYS-001 |
| NFR-04 | §3.4.2 authentication/authorization use cases | new safeguard | SEC-001–003; DEV-014 |
| NFR-05 | §3.4.2 table 3-4 reliability path | new safeguard | SYS-001 |
| NFR-06 | §3.6/§3.8 validation records | new safeguard/clarification | AST/BKT/DEP retention gates |
| NFR-07 | §3.3.1 target browser/device | multi-engine evidence is a new safeguard | PERF-001; SCOPE-002 staging |
| NFR-08 | §3.2 UI/UX design | new safeguard; spatial equivalence manual | ACC-001 |
| ER-01 | §3.8.1 | same; oracle-independence controls clarify | AST-005/006 |
| ER-02 | §3.8.2 | same arithmetic/policy validation; sensitivity clarifies | DEV-006–008; BKT-001–004 |
| ER-03 | §3.8.3–3.8.4 | same immediate pre/post/user evaluation; delayed recall and causal design manual | EDU-001–005; BKT-003/005 |

## Full matrix

| Objective | Requirement | Use case | Architecture module | Data entity/artifact | Test/evaluation | Phase | Final-report evidence |
|---|---|---|---|---|---|---|---|
| O-01,O-02 | FR-01 render approved sky by location/instant | UC-102 | web 3D adapter, astronomy-core, API scenario | scenario snapshot, generated catalogue | astronomy unit/reference, E2E, visual | P1,P2 | scene capture; fixture manifest/results |
| O-01,O-02 | FR-02 approved visibility/horizon/magnitude | UC-102,UC-103 | astronomy-core, adaptive scene view | catalogue magnitude/flags, visibility policy | boundary/reference, schema, raycast, visual | P2 | policy version; horizon/visibility cases |
| O-02 | FR-03 versioned structured tasks, one primary KC | UC-103 | API scenario use case, assessment-core | immutable scenario snapshot, task, cognitive skill, expected mastery revision | contract/API/E2E/stale-revision | P1,P2 | scenario schema and journey output |
| O-02 | FR-04 spatial/direction answer and server score | UC-103 | raycast adapter, assessment-core, API | typed assessment attempt | raycast, scoring unit, API, E2E | P1,P2 | answer/error trace; interaction recording |
| O-02 | FR-05 learner/admin authentication | UC-101,UC-104,UC-105 | web auth UI, API auth/authz, session adapter | user, server session, security audit event | auth API/E2E/security | P4,P5 | access-control matrix/results |
| O-02,O-03 | FR-06 typed BKT/model decision on accepted response | UC-103 | bkt-core, API submission use case | mastery state/revision, immutable attempt/model decision | BKT sequences/no-op, transaction, E2E | P1,P3 | before/posterior/after or explicit no-op trace |
| O-02,O-03 | FR-07 adaptive scaffolding | UC-103 | adaptive-policy, web scaffold renderer | attempt cue snapshot, policy version | state-machine, visual, E2E, study | P1,P3,P6 | scaffold transition trace/evaluation |
| O-01,O-02 | FR-08 star/True North/Qibla computation | UC-102,UC-103 | astronomy-core, assessment-core | astronomy/Qibla policy, fixture | pure/reference/angular tests | P1,P2 | independent error table |
| O-02 | FR-09 per-learner/per-KC mastery with versions | UC-103,UC-104,UC-105 | API mastery repository, bkt-core | cognitive skill, mastery state | DB constraint/integration | P1,P3 | schema/invariant test output |
| O-02 | FR-10 feedback and next scaffold | UC-103 | API submission response, web feedback | attempt reason/error, scaffold state | contract/E2E/accessibility | P1,P3 | annotated learner journey |
| O-02,O-03 | FR-11 distinguish issued assistance/independence | UC-103,UC-104 | adaptive-policy, API progress | authoritative issued cue snapshot, untrusted render telemetry, eligibility, independent status | BKT/policy/API/study audit | P3,P6 | assisted-vs-independent analysis |
| O-02 | FR-12 learner views own progress | UC-104 | web progress, API progress query | mastery state, summarized attempts | ownership API/E2E/accessibility | P4 | progress screenshot/test |
| O-02,O-03 | FR-13 aggregate read-only admin plus separate sensitive capabilities | UC-105 | web admin, API capability-scoped queries/adapters | aggregate view, structured system log, export/privacy audit where approved | capability/IDOR/export/E2E | P4,P5 | redacted dashboard and audit result |
| O-02 | FR-14 one pending idempotent local retry per KC | UC-103 | pending-submission adapter, API idempotency/revision | pending local item, fingerprinted idempotency result/attempt | disconnect/stale/concurrency/fault tests | P3 | disconnect/reconcile/reissue trace |
| O-01,O-02 | FR-15 validated versioned runtime catalogue | UC-102,UC-103 | catalogue tool/schema, web loader | source/curation/generated manifests and hashes | schema/checksum/rebuild | P0,P2 | provenance manifest and reproducible hash |
| O-03 | NFR-01 >=30 FPS and raycast <100 ms | UC-102,UC-103 | 3D adapter, performance harness | performance scene/device manifest | PERF-001 valid repeated FPS/raycast benchmark | P1,P5 | plots/raw benchmark metadata |
| O-01,O-03 | NFR-02 mathematical accuracy | UC-102,UC-103 | astronomy-core, independent reference harness | fixed reference fixture | per-case error/tolerance tests | P1,P2,P5 | signed fixture/error report |
| O-02,O-03 | NFR-03 reliable model-decision persistence | UC-103,UC-104 | API transaction/repositories | scenario, attempt, model/scaffold decision, mastery revision | fault/rollback/integration | P1,P3,P5 | atomicity test report |
| O-02 | NFR-04 security/capability/ownership | UC-101–UC-105 | auth/session/capability adapters, protected API routes | user, credential/session, capability/audit records | SEC-003 ASVS profile, negative API/E2E | P4,P5 | completed security profile |
| O-02,O-03 | NFR-05 atomic fingerprinted duplicate-safe submission | UC-103 | API transaction/idempotency | scenario, attempt, mastery revision, fingerprinted result | SYS-001 MySQL concurrency/fault | P1,P3 | replay/mismatch/stale/concurrency results |
| O-01,O-03 | NFR-06 versioned reproducibility | UC-102–UC-105 | contracts, data pipeline, all domains | scenario and policy/data/EOP/model/build/migration identifiers plus retained artifacts/results | replay/rebuild/schema/evidence manifest | P0-P6 | manifests and qualified replay result |
| O-02,O-03 | NFR-07 supported browser/WebGL | UC-101–UC-105 | web/R3F, E2E harness | browser/environment manifest | exact primary journey plus approved additional-engine coverage | P1,P5 | CI browser/support matrix |
| O-02,O-03 | NFR-08 accessible core journey | UC-101–UC-105 | web semantic UI, equivalent controls | accessibility checklist/baselines | axe plus manual WCAG checks | P4,P5,P6 | signed accessibility report |
| O-01,O-03 | ER-01 independent astronomy/Qibla validation | UC-102,UC-103 | reference harness (not runtime) | oracle fixture/source manifest | Astropy/USNO/domain comparison | P0,P2,P5 | independent fixture provenance/errors |
| O-02,O-03 | ER-02 BKT/scaffold validation | UC-103,UC-104 | bkt-core, adaptive-policy, analysis | parameter/policy fixture, attempts | oracle/sensitivity/policy tests | P0,P3,P6 | sequences and sensitivity report |
| O-03 | ER-03 pre/post/immediate-independent/performance/SUS evaluation | UC-102–UC-105 | study protocol/export/analysis boundary | consent-controlled pseudonymized dataset/codebook | EDU-001–005 human evaluation or explicit unsatisfied outcome | P6 | protocol, bounded results/effect/CI/SUS or documented no-claim outcome |

## Entity coverage

| Report entity | Owning requirement rows | Integrity evidence |
|---|---|---|
| `USER` | FR-05, FR-12, FR-13, NFR-04 | unique normalized login, role/ownership tests, data-minimization review |
| `COGNITIVE_SKILL` | FR-03, FR-06, FR-09 | exactly KC-01–KC-05 for MVP; stable IDs/version |
| `BKT_MASTERY_STATE` | FR-06, FR-09, NFR-03, NFR-05 | provisioned before assessment; unique active learner/KC; probability/model/policy/version/revision constraints; locked chain |
| `ASSESSMENT_SESSION` | FR-03, FR-04, FR-14 | owner, purpose, lifecycle/expiry, scenario links |
| `ASSESSMENT_ATTEMPT` | FR-04, FR-06, FR-10, FR-11, FR-14 | typed answer, committed order, request fingerprint/idempotency, immutable typed model decision and before/posterior/after or no-op values |
| `SYSTEM_LOG` | FR-13, NFR-04 | DEV-014 allowlisted/redacted structured events, capability/retention/access tests |

Implementation-support records required by the clarified architecture are:

| Support record | Coverage | Integrity evidence |
|---|---|---|
| `SCENARIO_SNAPSHOT` | FR-03/04/08/11, NFR-02/05/06 | immutable authoritative inputs/target/version links, ownership, expected mastery revision, expiry/consumption |
| `IDEMPOTENCY_RESULT` | FR-14, NFR-03/05 | unique user/key, canonical request fingerprint, committed response, mismatch conflict |
| Credential/session/recovery | FR-05, NFR-04 | durable opaque sessions, rotation/revocation/expiry, fixture-bypass exclusion |
| Capability/privacy/export audit | FR-13, NFR-04 | purpose, actor capability, scope, approval and immutable event |

The report dictionary's missing attempt-order field is resolved as a **CLARIFIED**
required `(session_id, attempt_order)` constraint. A committed sequence is serialized
and replayable; no separate research claim depends on cosmetic database ID gaps.
Catalogue/curation/generated artifacts are intentionally version-controlled data rather
than operational user entities, subject to AST-001 licensing.

## Change-control rule

A requirement is not removed by deleting a row. Any scope change must update `PRODUCT_SPEC.md`, this matrix, affected ADR/spec/test/phase, and `REPORT_DEVIATIONS.md` when it changes the report. Final thesis evidence must cite its requirement and immutable data/policy/software version.
