# Independent adversarial architecture review

**Review date:** 2026-07-20

**Scope:** documentation and restricted local report only; no application code or
dependency installation

**Review state:** completed and corrections applied
**Verdict:** not ready for application scaffolding

## Documents reviewed

- Governing/project files: `AGENTS.md`, `README.md`, `.agent/PLANS.md`.
- Core architecture/delivery: `STATUS.md`, `ARCHITECTURE.md`,
  `EXECUTION_PLAN.md`, `OPEN_QUESTIONS.md`, `REPORT_DEVIATIONS.md`.
- Product/domains/data: `PRODUCT_SPEC.md`, `ASTRONOMY_SPEC.md`,
  `TUTORING_BKT_SPEC.md`, `DATA_STRATEGY.md`.
- Assurance/governance: `TEST_STRATEGY.md`, `SECURITY_AND_PRIVACY.md`,
  `TRACEABILITY.md`, `RISK_REGISTER.md`, `RESEARCH_NOTES.md`.
- ADR set: `adr/README.md` and ADR-001 through ADR-007.
- Restricted local FYP report, all 98 PDF pages. It was inspected locally only; no
  report text or extraction artifact is reproduced here.

## Reviewer categories

Five read-only adversarial role passes were completed:

1. software architecture and maintainability (`SA-*`);
2. astronomical correctness and dataset provenance (`AST-*`, `DATA-*`, `QIB-*`,
   `CULT-*`, `VAL-*`, `TRACE-*`);
3. BKT and adaptive-scaffolding correctness (`BKT-*`);
4. verification, performance, security assurance, and educational evaluation
   (`VER-*`);
5. scope control and report traceability (`ST-*`).

The main agent independently read the same corpus, checked current primary guidance
used by the documents, merged true duplicates, rejected unsupported reviewer claims,
and made all tracked-file changes.

## Resolution meanings

- **ACCEPT AND FIX:** the finding is valid and the cited documentation was corrected.
- **REJECT WITH JUSTIFICATION:** the finding conflicts with the report/repository or
  demands an unnecessary change; the reason is retained below.
- **NEEDS MANUAL DECISION:** the architecture now exposes and gates the issue but no
  value, policy, authority, or study choice was invented.
- **DEFER AS OPTIONAL:** useful work that is not needed for the protected MVP/research
  path was removed from mandatory acceptance or made conditional.

## Findings by severity

### Blocking findings

| ID | Finding | Resolution | Result/reference |
|---|---|---|---|
| F-B01 | Scientific inputs and the production astronomy algorithm/error budget remain unapproved. | NEEDS MANUAL DECISION | AST-001–007 now cover catalogue fields/uncertainty/subset/licence, cultural authority, every relevant astrometric effect, EOP/datum/elevation, Qibla coordinates, scenarios and tolerances. ADR-003/004 remain blocked. |
| F-B02 | BKT observation eligibility, parameter/version migration, threshold, cues and evaluation-session semantics remain unapproved. | NEEDS MANUAL DECISION | BKT-001–005 now define the complete decision surface. ADR-005 remains blocked; report examples remain arithmetic fixtures only. |
| F-B03 | The authoritative scenario, idempotency, cold start, stale ordering and replay contracts were incomplete. | ACCEPT AND FIX; SYS-001 still manual | Added immutable `ScenarioSnapshot`, request fingerprint, stored canonical result, pre-provisioned mastery rows, expected/next mastery revisions, fixed lock order, stale rejection/reissue and real-MySQL fault cases in Architecture, ADR-006, Product, Tests and Traceability. |
| F-B04 | The report-derived `1e-10 rad`, BKT `1e-12`, and global visual pixel thresholds were unapproved/invented gates. | ACCEPT AND FIX | Removed fixed values. AST-006/BKT-002/PERF-001 must justify operation-specific numeric/visual thresholds; missing configuration fails. |
| F-B05 | Human-study design and completion semantics could not support the intended evidence/claims. | NEEDS MANUAL DECISION and ACCEPT AND FIX | Split EDU-001–005; added task/KC and alternate-form validity, estimand/comparator or non-causal boundary, power/recruitment contingency, codebook/export/analysis freeze, and separate “ER-03 satisfied/not satisfied” outcomes. |
| F-B06 | Learner-account/research-data security cannot be called ready while institutional, session, recovery and privileged-access policies are open. | NEEDS MANUAL DECISION | SEC-001–003 now own privacy, identity/session/capabilities and a risk-based ASVS 5.0.0 profile. P4/participant work remains blocked. |
| F-B07 | All P1 deviations/manual decisions and ADR approvals remain unresolved. | NEEDS MANUAL DECISION | `STATUS.md` and Phase 0 now list the exact P1 gates and needed-by phases. Phase 0 decision work may proceed; application scaffolding may not. |
| F-B08 | A reviewer alleged that the report grants ordinary administrators mutation rights. | REJECT WITH JUSTIFICATION | The report's UC-105 baseline is read-only. Product/Traceability retain read-only aggregate analytics; DEV-012 is a separate privacy-maintenance authority. No manufactured deviation was added. |

### Major findings

| ID | Finding | Resolution | Result/reference |
|---|---|---|---|
| F-M01 | The browser could import authoritative assessment/scoring code and the API/adaptor direction was ambiguous. | ACCEPT AND FIX | Browser now imports raw DTOs/contracts and presentation-safe astronomy only; API use cases own ports and server-only scoring; adapters depend inward; bundle/import tests enforce it. |
| F-M02 | Browser and API were not explicitly bound to the same generated catalogue. | ACCEPT AND FIX | Pipeline now feeds identical bytes/hash to both; mismatch blocks loading/scenario issuance. Phase 1 includes a minimal production-shaped provenance path. |
| F-M03 | Version fields alone did not preserve executable/data semantics. | ACCEPT AND FIX | Added compatibility/retention contract across scenario, catalogue, astronomy/EOP, BKT/scaffold, API/build/database and qualified replay when licence/privacy prevents artifact retention. |
| F-M04 | Catalogue subset, uncertainties, canonical bytes, cultural conflict handling and runtime astrometry content were incomplete. | ACCEPT AND FIX plus AST-001/002 manual | Data Strategy and open decisions now require deterministic subset rules, uncertainty/covariance or exclusion rationale, canonical serialization, source-quality/conflict review and runtime-content choice. |
| F-M05 | Astronomy validation lacked a full scientific error budget and exact oracle-governance protocol. | ACCEPT AND FIX plus AST-003/005/006 manual | Added independent generator/reviewer, prohibited code sharing, pinned Astropy/ERFA/IERS settings, policy differential cases and per-source error-budget fields. |
| F-M06 | Task-to-KC labels, issued-versus-rendered cues, no-op attempts and model migration were under-specified. | ACCEPT AND FIX plus BKT/EDU manual | Added typed `OBSERVATION`/`TRANSITION_ONLY`/`NO_MODEL_UPDATE`, authoritative issued cues, untrusted render telemetry, task/KC review, session-purpose gates and audited version-chain migration. |
| F-M07 | Durable multi-item offline tutoring conflicted with server-authoritative adaptation and was disproportionate. | DEFER AS OPTIONAL | MVP retains at most one pending submission per learner/KC, blocks that KC, reconciles/reissues on stale revision, and excludes multi-opportunity offline teaching. |
| F-M08 | Session, fixture identity and administrator privilege architecture was too coarse. | ACCEPT AND FIX plus SEC manual | Initial topology uses durable MySQL session adapters, fail-closed production exclusion of fixture identity, and distinct aggregate/learner/log/export/enrollment/privacy capabilities. |
| F-M09 | ASVS Level 1 alone was an insufficient risk statement for privileged/research functions. | ACCEPT AND FIX plus SEC-003 manual | L1 is a minimum; SEC-003 selects higher controls, vulnerability exception/expiry and independent-review needs. Current Argon2id values remain only a deployment-benchmarked candidate. |
| F-M10 | Performance, visual, accessibility and flaky-test evidence was not reproducibly specified. | ACCEPT AND FIX plus PERF-001/ACC-001 manual | Expanded valid-run/instrumentation/raw-trace rules, narrowed visual baselines to science/scaffolds, required WCAG/AT matrices, exact environment manifests and disclosed reruns/quarantines. |
| F-M11 | Evidence retention had no manifest schema/location/clean-run contract. | ACCEPT AND FIX | `.agent/PLANS.md` and Test Strategy now require requirement/risk IDs, exact commands, dirty state, environment, hashes, raw/derived status, approvals, retention/access and clean-environment steps. |
| F-M12 | Phase 0 both appeared to require every later decision and allowed only P1 decisions at exit. | ACCEPT AND FIX | Every item is registered/scheduled in P0; only next-phase decisions block that phase. Later institutional work starts early without blocking a local non-participant slice prematurely. |
| F-M13 | One-developer feasibility and external approval timing were asserted without a calendar or cut line. | NEEDS MANUAL DECISION | Added SCOPE-002, R-18, phase timeboxes/stop-go requirements and deferral order. Feasibility is now “unproven,” not “Pass.” |
| F-M14 | Software MVP, study readiness and completed thesis evaluation were conflated. | ACCEPT AND FIX | Product now has three separate acceptance layers; Phase 6 cannot satisfy ER-03 merely by documenting failed recruitment. |
| F-M15 | EDU evidence could support within-participant change but not automatically attribute benefit to BKT adaptation. | NEEDS MANUAL DECISION | EDU-003 must choose a comparator or explicitly non-causal claim; model/policy behavior is reported separately. |
| F-M16 | Analysis code, event definitions and form-equivalence checks appeared too late. | ACCEPT AND FIX plus EDU manual | Phase 3 freezes codebook/export and runs synthetic analysis; EDU-002/003/005 approve forms, estimand and measures before recruitment. |
| F-M17 | Recruitment/underpowering was not a governed risk. | ACCEPT AND FIX | Added R-17, EDU-004 and an explicit no-learning/no-adaptation-effect contingency. |
| F-M18 | Status claimed completed independent review and passed gates without a review artifact. | ACCEPT AND FIX | Rewrote Status/README and created this finding/disposition record. Identifier equality is now described as syntactic only. |
| F-M19 | Report traceability lacked neutral source anchors and clause-level relationship types. | ACCEPT AND FIX | Added a report-authority crosswalk with `same`, `clarifies`, `new safeguard`, and `changes`; composite Product rows now use clause-level wording. |
| F-M20 | Deviation entries lacked affected/source/approver traceability and log redaction was an unrecorded report-level change. | ACCEPT AND FIX | Expanded every deviation with neutral report anchor/affected IDs/co-approver and added DEV-014 for structured redacted logs. |
| F-M21 | Hipparcos was alleged to be a fixed report constraint. | REJECT WITH JUSTIFICATION | The report names catalogue candidates; AST-001 may approve another defensible source without an automatic deviation. Proper-motion/epoch requirements are classified as scientific clarifications. |

### Minor findings

| ID | Finding | Resolution | Result/reference |
|---|---|---|---|
| F-N01 | Equatorial types conflated reference epoch, frame/equinox and observation time. | ACCEPT AND FIX | Astronomy Spec now uses distinct catalogue, propagated, mean/apparent and horizontal typed states. |
| F-N02 | Angle canonical representatives, elevation semantics and runtime JSON content were ambiguous. | ACCEPT AND FIX / NEEDS MANUAL DECISION | Added explicit AST-003/004/007 choices and runtime-content gate. |
| F-N03 | Randomized tests omitted seeds/case counts and strict BKT properties omitted preconditions. | ACCEPT AND FIX | Tests now retain generator metadata and condition monotonic properties on possible informative interior cases. |
| F-N04 | “Independent learner states” overstated KC independence and learner-facing probability language was unspecified. | ACCEPT AND FIX plus BKT-003/004 manual | Renamed to separate skill states and gated probability/rounding/reason wording. |
| F-N05 | “Pinned current browser,” current time, SUS and flaky reruns were not reproducible. | ACCEPT AND FIX plus PERF/EDU manual | Evidence manifest records exact builds/GPU; fake-clock/zone tests added; EDU-002 governs SUS; reruns are disclosed. |
| F-N06 | ADR-003 blocker list omitted AST-001/007 in its index. | ACCEPT AND FIX | ADR-003 and ADR index now agree on AST-001/003–007. |
| F-N07 | README omitted ADR and per-phase ExecPlan gates. | ACCEPT AND FIX | README now names all gates and the completed review. |
| F-N08 | Gap-free numbering was stronger than the evidence need. | DEFER AS OPTIONAL | Retained a serialized, monotonic, replayable committed chain; no thesis claim depends on cosmetic ID gaps. |
| F-N09 | Same-origin/single-instance deployment was described before hosting approval. | REJECT WITH JUSTIFICATION | It remains an explicitly initial candidate subject to DEP-001, not an approved institutional fact. |
| F-N10 | Per-KC participant parameter fitting may be excessive. | REJECT WITH JUSTIFICATION | It was already conditional on ethics and sufficient data; expert-set frozen parameters plus sensitivity remain the documented fallback. |
| F-N11 | High-latitude/high-proper-motion fixtures were called unnecessary scope. | REJECT WITH JUSTIFICATION | They remain cheap reference robustness tests and now explicitly do not expand learner scenarios/UI. |

## Unjustified assumptions resolved

- Arrival order is no longer assumed to be learning order; expected mastery revisions
  and one unresolved scenario per KC define acceptance.
- Server-issued cues are no longer claimed as proof of successful rendering; render
  telemetry is separate and cannot promote evidence.
- Version labels are no longer assumed to reconstruct behavior without retained
  artifacts/results.
- A 30 FPS run, SUS result, BKT threshold, or pre/post change is no longer allowed to
  substitute for another evidence category.
- Expert/licence/ethics/hosting/recruitment availability is not assumed; SCOPE-002 and
  R-17/R-18 require dates, owners and claim-reduction triggers.
- A full apparent-place/IERS runtime is not assumed necessary: AST-003 must select the
  simplest named pipeline whose total error is safely within AST-006, with every omitted
  effect bounded.

## Reviewer finding disposition index

Every reviewer-local problem, assumption, missing-decision and unnecessary-scope ID is
mapped below. True duplicates share a disposition/master finding. Reviewer
recommendations are indexed separately afterward.

### Software architecture and maintainability

| Reviewer IDs | Resolution | Master finding/reason |
|---|---|---|
| SA-B01, SA-M01, SA-D02 | ACCEPT AND FIX | F-B03/F-M02: durable scenario and shared catalogue |
| SA-B02, SA-D01 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-B03; SYS-001 |
| SA-M02, SA-M10 | ACCEPT AND FIX | F-M01 |
| SA-M03, SA-M06, SA-M09, SA-D03, SA-N04 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M08; SEC-001/002 |
| SA-M04, SA-A03, SA-D04 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M03; retention authorities |
| SA-M05, SA-D06, SA-U03 | ACCEPT AND FIX | F-M12 |
| SA-M07, SA-A01, SA-D05 | NEEDS MANUAL DECISION | F-M13; SCOPE-002 |
| SA-M08, SA-A04 | ACCEPT AND FIX | F-M18 |
| SA-N01 | REJECT WITH JUSTIFICATION | Report data model explicitly uses email; SEC-002 may change identifier policy only through approval/deviation. |
| SA-N02, SA-U01 | DEFER AS OPTIONAL | F-N08 |
| SA-N03, SA-U02 | DEFER AS OPTIONAL / ACCEPT SAFEGUARDS | F-M07 |
| SA-A02 | REJECT WITH JUSTIFICATION | F-N09 |

### Astronomy and provenance

| Reviewer IDs | Resolution | Master finding/reason |
|---|---|---|
| AST-B01 | NEEDS MANUAL DECISION | F-B01 |
| AST-B02, AST-D01, AST-D02, AST-M04, SCOPE-A01, SCOPE-A02 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-B01/F-M05; implement-or-omit/error-bound rule |
| AST-B03 | ACCEPT AND FIX | F-B04 |
| DATA-B04 | ACCEPT AND FIX | F-M02/F-M04; Phase 1 minimal pipeline and qualified checkout claim |
| AST-M01 | ACCEPT AND FIX | F-N01 |
| AST-M02 | ACCEPT AND FIX | F-M03/F-M05 |
| AST-M03 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M05; AST-006 |
| DATA-M05, DATA-M06, DATA-D03, AST-U03 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M04; AST-001 |
| QIB-M07, QIB-D05, VAL-U04 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-B01; AST-005–007 |
| CULT-M08, CULT-D04 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M04; AST-002 |
| VAL-M09 | ACCEPT AND FIX | F-M05 |
| TRACE-M10 | REJECT WITH JUSTIFICATION | F-M21 |
| AST-m01, DATA-m02, AST-m03, DATA-m05, TIME-D06 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-N02; AST-003/004/007 |
| DOC-m04 | ACCEPT AND FIX | F-N06 |
| AST-U01, AST-U02 | ACCEPT AND FIX | F-N01/F-M21: corrected epoch/time-scale and report-authority wording |
| SCOPE-A03 | REJECT WITH JUSTIFICATION | F-N11 |

### BKT and adaptive scaffolding

| Reviewer IDs | Resolution | Master finding/reason |
|---|---|---|
| BKT-B01 | NEEDS MANUAL DECISION | F-B02 |
| BKT-B02, BKT-D01, BKT-A02 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M06; BKT-001/005 |
| BKT-B03, BKT-D02 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-B03; approved initial values still needed |
| BKT-B04, BKT-D03, BKT-A04 | ACCEPT AND FIX | F-B03 |
| BKT-M01, BKT-D05, BKT-A01 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M06/F-M16; EDU-002 |
| BKT-M02, BKT-D06 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M06; BKT-005 |
| BKT-M03, BKT-D04 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M06; BKT-002 |
| BKT-M04, BKT-A03 | ACCEPT AND FIX | F-M06 |
| BKT-M05, BKT-S01 | DEFER AS OPTIONAL / ACCEPT REVISION SAFEGUARD | F-M07 |
| BKT-M06 | ACCEPT AND FIX | F-B03 |
| BKT-M07, BKT-D07 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M15/F-M16; EDU-003 |
| BKT-M08 | NEEDS MANUAL DECISION | F-M15 |
| BKT-M09 | ACCEPT AND FIX + NEEDS MANUAL DECISION | Immediate independent evidence mandatory; delayed recall BKT-003/EDU choice |
| BKT-N01, BKT-N02, BKT-N03 | ACCEPT AND FIX | F-N03/F-N04 |
| BKT-N04 | NEEDS MANUAL DECISION | BKT-002 admissible region; fixed tolerance removed |
| BKT-N05, BKT-D08 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-N04; BKT-003/004 |
| BKT-A05 | ACCEPT AND FIX | Predictive-validity/claim boundary added |
| BKT-S02 | REJECT WITH JUSTIFICATION | F-N10 |

### Verification, performance, security and evaluation

| Reviewer IDs | Resolution | Master finding/reason |
|---|---|---|
| VER-B01 | ACCEPT AND FIX | F-M14 |
| VER-B02, VER-D03, VER-D04 | NEEDS MANUAL DECISION / ACCEPT STRUCTURE | F-B05/F-M15; EDU-001–005 |
| VER-B03, VER-D01 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-B03; SYS-001 |
| VER-B04 | NEEDS MANUAL DECISION | F-B06 |
| VER-M01 | ACCEPT AND FIX | Exact applicable commands are required in phase ExecPlans; no pre-toolchain command names were invented. |
| VER-M02, VER-A02, VER-D02 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M10; PERF-001 |
| VER-M03, VER-A04 | ACCEPT AND FIX | F-M05 |
| VER-M04, VER-D06 | ACCEPT AND FIX | F-M11 |
| VER-M05, VER-A05 | ACCEPT AND FIX | F-M16; synthetic/expert dry-run precedes recruitment; participant work still needs approval/security. |
| VER-M06, VER-A01 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M16; EDU-002 |
| VER-M07 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M10; ACC-001 |
| VER-M08, VER-D08 | NEEDS MANUAL DECISION | F-M13; SCOPE-002 |
| VER-M09, VER-A03, VER-D07 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M09; SEC-003 |
| VER-M10 | ACCEPT AND FIX | F-M17 |
| VER-M11 | ACCEPT AND FIX | F-M10 |
| VER-M12, VER-D05 | ACCEPT AND FIX + NEEDS MANUAL DECISION | F-M16; EDU-005 |
| VER-m01 | ACCEPT AND FIX | F-M18 |
| VER-m02, VER-m03, VER-m05 | ACCEPT AND FIX | F-N05 |
| VER-m04 | ACCEPT AND FIX + NEEDS MANUAL DECISION | EDU-002 owns instrument/language/scoring/uncertainty |
| VER-A06, VER-S03 | DEFER AS OPTIONAL | Delayed recall is conditional; immediate no-hint independent evidence remains |
| VER-S01 | DEFER AS OPTIONAL | F-M07 |
| VER-S02 | DEFER AS OPTIONAL | Broad UI pixel baselines replaced by semantic assertions |

### Scope control and report traceability

| Reviewer IDs | Resolution | Master finding/reason |
|---|---|---|
| ST-B01, ST-A03, ST-D01 | REJECT WITH JUSTIFICATION | F-B08 |
| ST-B02, ST-D02 | ACCEPT AND FIX | F-M19 |
| ST-B03 | NEEDS MANUAL DECISION | F-B07 |
| ST-M01 | ACCEPT AND FIX | F-M19 |
| ST-M02, ST-A01, ST-D03, ST-U01 | ACCEPT AND FIX / DEFER OPTIONAL EXTRAS | F-M07/F-M09/F-M10/F-M14 |
| ST-M03, ST-D04 | ACCEPT AND FIX | F-M14 |
| ST-M04 | ACCEPT AND FIX | F-M20 |
| ST-M05, ST-U03 | ACCEPT AND FIX | F-M12 |
| ST-M06, ST-A02, ST-D05 | NEEDS MANUAL DECISION | F-M13; SCOPE-002 |
| ST-M07, ST-D06 | ACCEPT AND FIX + NEEDS MANUAL DECISION | DEV-013 now preserves seasonal geometry and isolates atmosphere/weather; SCOPE-001 |
| ST-M08, ST-N02 | ACCEPT AND FIX | F-M18 |
| ST-N01 | ACCEPT AND FIX | F-N07 |
| ST-N03 | ACCEPT AND FIX | Needed-by/status semantics added |
| ST-U02 | DEFER AS OPTIONAL | F-N08 |

## Reviewer recommendation disposition

Recommendations inherit the evidence and resolution of their underlying findings:

| Recommendation IDs | Resolution |
|---|---|
| SA-RC01–SA-RC07, SA-RC09 | ACCEPT AND FIX |
| SA-RC08 | ACCEPT AND FIX for capacity/cut line and retry narrowing; gap-free numbering deferred as optional |
| REC-A01–REC-A06, REC-A08–REC-A10 | ACCEPT AND FIX, with named AST decisions still manual |
| REC-A07 | ACCEPT AND FIX IN PART: proper-motion/report authority was corrected; an automatic non-Hipparcos deviation was rejected |
| BKT-R01–BKT-R12 | ACCEPT AND FIX, with BKT/EDU approvals still manual |
| VER-RC01–VER-RC09 | ACCEPT AND FIX, with exact values/approvals still manual |
| VER-RC10 | ACCEPT: readiness verdict adopted |
| ST-RC01, ST-RC03–ST-RC07 | ACCEPT AND FIX |
| ST-RC02 | REJECT WITH JUSTIFICATION: it depends on the unsupported administrator-mutation claim |

## Unresolved blockers

1. P1 science/data inputs: AST-001/002/003/006/007.
2. P1 learning inputs: BKT-001/002/004 and applicable deviations.
3. P1 transaction/performance/capacity profile: SYS-001, PERF-001, SCOPE-002.
4. P1 deviations and ADR approvals, especially DEV-001–010 as applicable.
5. Approved Phase 1 ExecPlan does not yet exist.
6. Later production/participant gates remain open: AST-004/005, BKT-003/005,
   EDU-001–005, SEC-001–003, ACC-001, DEP-001, SCOPE-001 and DEV-011–014.

## Manual approvals required

- Student and supervisor: every deviation disposition, SCOPE-001/002, ADR acceptance,
  phase ExecPlans and the bounded thesis claim.
- Astronomy/data reviewer: AST-001/003/004/006/007, oracle/error budget and runtime
  algorithm.
- Ilm al-Falak/cultural authority: AST-002/005 and cultural/Qibla source decisions.
- Learning/research-method reviewers: BKT-001–005 and EDU-002–005.
- Institution/privacy/security owners: EDU-001/004, SEC-001–003, participant and
  privileged-data handling.
- Accessibility, deployment and performance owners: ACC-001, DEP-001, PERF-001.

## Final readiness verdict

The revised architecture is internally coherent and substantially more testable, but it
is intentionally not executable yet: scientific truth, learning semantics, database
profile, deviation authority, delivery capacity and the Phase 1 ExecPlan are unresolved.
Phase 0 decision work is ready. Application scaffolding is not.

READY_FOR_SCAFFOLDING: NO
