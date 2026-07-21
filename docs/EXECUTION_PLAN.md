# Risk-ordered execution plan

## Strategy

Implementation order follows scientific and integration risk rather than the report's sprint numbering. The first coding slice proves the central research contribution end to end. This ordering and temporary fixture learner are **PROPOSED DEVIATIONS DEV-001 and DEV-010**; approval is a prerequisite.

Every phase needs its own approved living ExecPlan under `.agent/execplans/` before code. No phase may encode an unresolved manual value. Later phases may begin only when shared dependency gates are satisfied; optional features wait until MVP acceptance.

## Capacity and cut-line gate

SCOPE-002 must record the submission date, available developer weeks, external approval
lead times, phase timeboxes, and latest-decision dates. Each phase ExecPlan states its
effort range and a stop/go review. The protected minimum is a reproducible,
scientifically validated, server-authoritative core with honest model-behavior evidence;
it is not permission to claim a completed product or learning effect. If time or external
approvals fail, scope is deferred in this order unless the supervisor records another
choice: multi-opportunity persistent offline behavior, broad visual snapshots, optional
browser/operations hardening beyond the approved deployment, delayed recall, and only
then report-level functionality through an explicit new deviation. Security essentials,
scientific/reference correctness, transaction integrity, and truthful claim boundaries
are never waived to meet a date.

## Phase 0 — Approvals, fixtures, and reproducibility contract

**Objective:** register and schedule every unresolved scientific, cultural, learning,
privacy, evaluation, deployment, database, and capacity assumption; resolve the inputs
needed by the next phase without pretending later decisions are already approved.

**Dependencies:** architecture review; no product code.

**Exact deliverables:** complete decision register with needed-by phases; approved
records for every P1 dependency; scheduled owners/latest dates for later items;
disposition of DEV-001–014 as needed by P1; reviewed ADRs; minimal
catalogue/licence/source manifest and canonicalization design; scenario/evidence/error-
budget fixture schemas; SYS-001 and SCOPE-002 records; Phase 1 ExecPlan.

**Tasks:** hold supervisor/domain reviews; verify Hipparcos candidate metadata/licence or select another approved catalogue; approve cultural mappings; freeze time/frame/Qibla policies and tolerance IDs; approve BKT evidence/parameters; define study and privacy gates; select baseline device/browsers; threat-model review.

**Tests/reviews:** every required astronomy field has a value or explicit non-applicability; worked BKT examples independently recalculated; traceability/ADR/deviation consistency review; restricted-file/licence review.

**Manual inputs:** all open-question owners; institution for research/privacy.

**Risks:** R-01–R-04, R-11, R-16. An unavailable expert blocks affected data/content, not the whole documentation review.

**Exit criteria:** all P1-blocking decisions and P1 deviations approved with
source/date/reviewer; every later decision has owner, needed-by phase, and latest date;
no silent default; Phase 1 ExecPlan accepted. Later privacy/hosting/study decisions are
started early but do not block a local, non-participant slice until their needed-by gate.

**Rollback/recovery:** decisions are append-only ADR revisions; retain rejected alternatives and revert manifests to last approved version. No catalogue bytes or participant data exist yet.

**Thesis evidence:** signed decision table, provenance/licence record, approved convention/model/protocol versions, architecture review notes.

## Phase 1 — Central research vertical slice

**Objective:** demonstrate one approved observer/time scenario through deterministic sky position and minimal 3D rendering, one spatial/direction answer, server-authoritative scoring, one atomic BKT transition, and the next scaffold state.

**Dependencies:** P0 science/tolerance/BKT policy decisions; DEV-001/010 approval; supported local MySQL; Phase 1 ExecPlan.

**Exact deliverables:** minimal monorepo/toolchain; public contracts; immutable
server-side scenario snapshot; pure astronomy/assessment/BKT/policy cores for the
chosen slice; minimal fingerprinted/revisioned API transaction; minimal R3F
scene/raycast; one approved generated data fixture built by a minimal production-shaped
provenance pipeline; independent reference/error-budget fixtures; local deterministic
demo using a fixture learner whose adapter cannot enter production.

**Tasks:** establish dependency enforcement; implement only required value objects/functions; create scenario issuance/submission contract; add InnoDB schema through the later approved implementation process; render selected stars; capture raw evidence; lock/idempotently commit attempt/mastery; show feedback/scaffold; instrument performance.

**Tests:** pure math/BKT oracles; schema/checksum/canonical rebuild; one independent
astronomy error-budget fixture set; raycast boundaries; browser-bundle scorer exclusion;
API validation; real SYS-001 MySQL rollback, concurrent cold start, matching duplicate,
different-payload key reuse, stale revision, and distinct-request serialization; fixture-
identity production exclusion; one browser journey; valid PERF-001 performance profile.

**Manual inputs:** approved single scenario, catalogue rows/cultural mapping needed for it, task tolerance, BKT/scaffold configuration, performance baseline.

**Risks:** R-01, R-05–R-08, R-13. Keep the slice small enough to diagnose errors.

**Exit criteria:** a fresh authorized environment reproduces the same data hash (a
public checkout is explicitly limited when licensed bytes are private) and completes the
journey; every scientific case meets AST-006; exactly one retry-safe decision/revision;
same key/different content is safe; no forbidden dependency/fixture bypass;
performance meets or has a documented measured remediation accepted before expansion.

**Rollback/recovery:** feature branch and reversible migrations; idempotent seed/fixture; keep UI behind a development-only route; revert to last passing catalogue/policy hash without rewriting history.

**Thesis evidence:** architecture/dependency report, deterministic demo recording, astronomy error table, transaction trace, BKT before/posterior/after, initial FPS/raycast results.

## Phase 2 — Complete astronomy, curated data, and five skill assessments

**Objective:** expand the validated core to all approved scenarios and all five KCs without adding broad account/dashboard scope.

**Dependencies:** P1 passes; AST-001–007 and AST-002 cultural content approved; data redistribution decision.

**Exact deliverables:** full approved small-catalogue pipeline and runtime artifact; complete astrometric/Qibla policy; all cultural segments/labels; scenario/task types for KC-01–KC-05; deterministic visibility/horizon behavior; expanded reference suite.

**Tasks:** implement pinned acquisition/transform/validation; proper motion/time policy; horizontal/Three mapping; visibility; Qibla; typed selection/vector/bearing scoring; complete scene layers and equivalent controls where defined.

**Tests:** 100% data-schema gates, deterministic rebuild/checksum, full astronomy fixture partitions, property/singularity tests, task/raycast matrix, browser and visual scenes, catalogue-size performance.

**Manual inputs:** remaining cultural records, cities/dates, visibility/refraction/horizon policies, task tolerances and accessibility equivalence.

**Risks:** R-01–R-03, R-07–R-08, R-13, R-16.

**Exit criteria:** all five tasks are scientifically/reference validated; no unapproved data record; artifact/licence policy passes; critical scene stays above performance floor; every mapping is traceable to an authority.

**Rollback/recovery:** retain prior catalogue/policy versions; generated outputs are replaceable from inputs; reject a failed source update without altering the last approved runtime artifact.

**Thesis evidence:** provenance graph/checksums, full error table, cultural review record, screenshots, performance comparison by scene size.

## Phase 3 — Adaptive tutoring, durable progress, and retry reconciliation

**Objective:** make the five-KC learning loop durable, adaptive, auditable, and resilient to transient network failure.

**Dependencies:** P1 transaction foundation, P2 tasks, BKT-001–005 approved.

**Exact deliverables:** versioned per-KC parameters/mastery/revisions; approved typed
observation policy and GUIDED/FADING/INDEPENDENT policy; authoritative issued cue
snapshots plus separate render telemetry; independent-recall status; at most one pending
submission per affected KC with blocked progression; progress query model;
replay/sensitivity tooling; frozen event codebook/export schema and synthetic analysis
dry-run for EDU-002/003/005.

**Tasks:** implement observation eligibility; scaffold UI per KC; restoration/fading rules; session/attempt lifecycle; queue/re-auth/reconciliation UX; learning event export schema without PII; model sensitivity report.

**Tests:** BKT sequences and reproducible seeded properties; typed no-op/transition-only
decisions; all policy transitions; hinted/independent semantics; database fault matrix;
disconnect/reload/single-pending/stale-revision E2E; local-storage privacy/limit;
mastery reconstruction; synthetic export/analysis reproduction.

**Manual inputs:** parameter versions, threshold, independent-success rule, cue content, queue age/clear policy.

**Risks:** R-04–R-06, R-09. Detect inflated mastery and divergence between stored attempts and state.

**Exit criteria:** every accepted response reconstructs its attempt and typed model/policy
decision; matching retries never double-count and mismatched reuse conflicts; pending
submission visibly reconciles before that KC advances; independent evidence cannot be
promoted by client metadata; prespecified policy-behavior metrics and synthetic analysis
reproduce.

**Rollback/recovery:** version policies; disable adaptation to a safe approved guided state without deleting evidence; replay only into a new audited model version; preserve/reconcile pending queue through contract-compatible updates.

**Thesis evidence:** state-transition diagrams/traces, sensitivity plots, offline recovery recording, concurrency/fault results.

## Phase 4 — Production roles, learner progress, and minimal admin analytics

**Objective:** replace the fixture identity with secure learner/admin access and expose only authorized, useful progress views.

**Dependencies:** P3 durable model; SEC-001–003, ACC-001, DEV-011/012/014 decisions.

**Exact deliverables:** durable credential/session/recovery adapters; central
capability/ownership authorization; learner own-progress UI; read-only aggregate admin
UI; separately controlled learner-level/log/export/enrollment/privacy capabilities where
approved; privacy-maintenance path if DEV-012 is approved; accessible semantic shell;
production artifact with no fixture-identity path.

**Tasks:** password/session implementation; rate limits/CSRF/headers; ownership-scoped queries; aggregate views; safe audit/log view; data minimization; consent/privacy notice integration as approved; keyboard/focus/zoom/reduced-motion work.

**Tests:** public/protected route and capability/IDOR matrix; session
fixation/logout/expiry/revocation, CSRF, enumeration and rate limit; XSS/input bounds;
fixture-bypass artifact test; E2E learner/aggregate-admin and separately approved
capabilities; axe plus ACC-001 criterion/AT matrix; privacy/export/structured-log
inspection.

**Manual inputs:** institution policy, admin MFA/enrollment/recovery, copy, retention/rights, accommodation claim.

**Risks:** R-10–R-11, R-14.

**Exit criteria:** fixture identity is impossible in production; all unauthorized cases deny; no sensitive log/client storage; critical workflows meet approved accessibility claim; admin cannot edit evidence.

**Rollback/recovery:** deploy behind access control; invalidate sessions on rollback; reversible schema migration with tested backup; privacy actions are audited and separately authorized.

**Thesis evidence:** authz matrix, security test output, redacted UI captures, accessibility report, data-flow/retention record.

## Phase 5 — Release hardening and deployment validation

**Objective:** make the complete MVP reproducible, secure, observable, recoverable, and stable on the approved baseline.

**Dependencies:** P2–P4 complete; DEP-001 and PERF-001 approved.

**Exact deliverables:** HTTPS deployment; private SYS-001 MySQL/least privilege; CI
quality gates; environment/config schema; redacted monitoring; encrypted
backup/restore; supported-browser, performance, focused scientific/scaffold visual,
accessibility, SEC-003 security and reference evidence bundle; evidence manifest/index.

**Tasks:** production configuration; dependency/secret/SBOM review as approved; tune measured 3D bottlenecks; freeze browser/device/data scene; complete ASVS checklist; failure/restore rehearsal; final restricted/licence scan.

**Tests:** all applicable suites from `TEST_STRATEGY.md` through exact commands in the
Phase 5 ExecPlan; PERF-001 performance; approved browser matrix; focused visual
baselines; manual accessibility/security checks; restore/replay known chain; catalogue
deterministic rebuild; clean-environment evidence-manifest replay. Generic `npm` gates
must invoke or point to these named evidence commands; they are not a substitute.

**Manual inputs:** hosting/operations targets, release reviewer, accepted residual risks.

**Risks:** R-07, R-10, R-14–R-16.

**Exit criteria:** all MVP software gates pass from a clean environment; restore meets targets; no critical/high unaccepted security/privacy issue; deployment versions match evidence manifests.

**Rollback/recovery:** immutable deploy artifact/database backup, backward-compatible rollout where possible, documented rollback command and data compatibility, health-gated release.

**Thesis evidence:** CI/release manifest, performance graphs, browser/accessibility/security reports, restore record, deployed architecture capture.

## Phase 6 — Pilot, freeze, and formal evaluation

**Objective:** verify instruments and then execute the approved evaluation without tuning on outcomes.

**Dependencies:** P5 study-ready candidate; EDU-001–005, SEC-001 and supervisor/institution approval.

**Exact deliverables:** pilot report; frozen software/catalogue/science/BKT/scaffold/protocol versions; participant materials; pseudonymized dataset and analysis script/manifest under approved access; final mathematical, performance, usability, model, and learning results.

**Tasks:** pilot only within approval; fix protocol/software defects through documented change control; refreeze; recruit/consent; run pre-test, learning, no-hint post-test and approved recall; analyze prespecified outcomes/effect/uncertainty; document limitations.

**Tests/reviews:** participant-flow audit, approved equivalent-form and
counterbalancing/comparator checks, timing/codebook audit, missing/exclusion and
multiplicity checks, reproducible analysis, privacy/access audit, consistency against
traceability. No post-hoc parameter tuning presented as confirmatory.

**Manual inputs:** ethics approval, recruitment/sample, facilitator script, final statistical plan, data retention/destruction approval.

**Risks:** R-04, R-11, R-14, R-17.

**Exit criteria:** one of two explicit outcomes is recorded. **ER-03 satisfied:** the
approved protocol completed with adequate or transparently qualified sample, all
exclusions/deviations reported, analysis reproduced, and claims bounded. **ER-03 not
satisfied:** ethics/recruitment/power prevented the planned evaluation; available
software/scientific/pilot evidence is reported, learning/adaptation-effect claims are
withdrawn, and Product “thesis evaluation completed” remains false. Retention and
withdrawal obligations are scheduled in either case.

**Rollback/recovery:** pause the study on safety/privacy/protocol breach; preserve consented immutable audit data only as permitted; issue protocol amendment before resuming; never silently repair participant records.

**Thesis evidence:** approved protocol/ethics reference, version freeze, anonymized analysis outputs, effect sizes/confidence intervals, SUS, limitations, traceability completion.

## Recommended first coding phase

After Phase 0 approvals, implement **Phase 1**. It is intentionally narrow but crosses every core boundary: astronomy, 3D interaction, assessment, transaction, BKT, and adaptation. Authentication scaffolding or dashboard breadth must not displace this proof unless DEV-001/010 are rejected.
