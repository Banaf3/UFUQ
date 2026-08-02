# Open questions and manual decisions

Items marked **MANUAL DOMAIN DECISION** block only the affected behavior from the
listed phase onward. Phase 0 must register and schedule every item, but only decisions
whose **Needed by** phase is next are prerequisites to that phase. Owners are
suggestions; record the answer, authority/source, approver, date, affected version, and
any tolerance in the owning specification and ADR. Every item below is currently
**Open**.

| ID | Decision required | Suggested owner | Needed by | Blocks |
|---|---|---|---:|---|
| AST-001 | I/311 release, parser fields, `pmRA`, missing/duplicate/supplement policy, candidate HIP scope, schemas, canonicalization, and local-only operating rule are recorded in Milestone 2B. Confirm the FYP's local scientific-use authority; obtain explicit raw/derived redistribution and deployment terms; complete acquisition provenance; and approve each selected row's actual solution, multiplicity, uncertainty, fit, variability, and supplement evidence. | Supervisor + astronomy/data reviewer; CDS/data-origin authority for rights clarification | P1 | Milestone 2D authority outcome, tracked/deployed source-derived artifact, scientific row approval, and the Phase 1 Milestone 2E local fail-closed parser |
| AST-002 | Review rather than assume the proposed greater/lesser Banāt Naʿsh crosswalks, polar-target identification, and five-object Dhāt al-Kursī review set. Approve or reject each Arabic form/transliteration, source tradition, membership, role, line segment, relationship, and historical-versus-pedagogical claim independently. Western constellation membership and a modern identifier crosswalk are insufficient. | Ilm al-Falak/Arabic/historical reviewer + supervisor | P1/P2 | Final allowlist, named patterns, edges, relationships, and lessons |
| AST-003 | The Milestone 2C audit confirms I/311 ICRS input, the literal `Ep=1991.25` label, starred-alpha `pmRA`, distinct UTC/TAI/TT/UT1 roles, and the fixed UFUQ horizontal conventions. Approve the exact I/311 epoch time-scale interpretation, production algorithm/library and supported date range; proper motion model; parallax; radial velocity/perspective acceleration; annual/diurnal aberration; light deflection; precession/nutation; UT1/TT/leap-second/IERS handling; polar motion; geodetic datum/ellipsoid/height; and a quantified implement-or-omit decision for every effect. Define EOP pinning, extrapolation, failure, and labelled approximation modes. | Astronomy expert | P1 | Astronomy core/reference fixtures and Milestone 2C closure |
| AST-004 | Choose refraction, elevation and horizon-dip use, below-horizon behavior, magnitude/variability, light-pollution, extinction, weather, and near-horizon teaching policies. | Supervisor + astronomy/education expert | P2 | Visibility/rendering |
| AST-005 | Approve authoritative Kaaba coordinates with datum, coordinate order/sign, precision, version/date, uncertainty, and the exact Malaysian/domain comparison authority and procedure. | Ilm al-Falak/supervisor | P2 | Qibla calculation/fixtures |
| AST-006 | Approve a scientific error budget and tolerances by operation: catalogue/propagation uncertainty, omitted effects, Earth orientation, observer coordinates, floating point, independent-reference disagreement, and learner-answer tolerances. No implementation-numerics threshold is active before it is justified and recorded. | Astronomy expert + supervisor | P1 | Test release gate |
| AST-007 | Approve supported cities and observer coordinates/datum/elevation, dates/date range, IANA zones and ambiguous/nonexistent wall-time handling, default-current-time limits, scenario distribution, and fixed evaluation fixtures. | Supervisor + astronomy expert | P1/P2 | Scenarios/evaluation |
| BKT-001 | Approve the total observation taxonomy and assisted-evidence policy: binary observation, transition-only opportunity, no-model-update, invalid/no-response/timeout/abandonment, feedback-revealed retry, and duplicate behavior, including persisted no-op/null semantics. | Supervisor/learning expert | P1 | BKT and scaffold policy |
| BKT-002 | Approve parameters globally or per skill, admissible numerical region/precision, minimum-data and calibration rules, initial-state assignment, freeze rules, and model/policy version migration or parallel-chain behavior. Report values remain provisional. | Supervisor/learning expert | P1/P3 | Production BKT configuration |
| BKT-003 | Approve mastery threshold, immediate independent-success count, spacing/reset/expiry, learner-facing wording/rounding, and whether delayed recall is required or optional. | Supervisor/learning expert | P3/P6 | Mastery display/evaluation |
| BKT-004 | Define the exact server-issued cues in GUIDED, FADING, and INDEPENDENT states; initial scaffold, restoration rules, reason codes, accessibility classification, feedback/reveal behavior, and learner-facing explanations. | Supervisor/domain expert | P1/P3 | Adaptive UI |
| BKT-005 | Decide model and policy eligibility separately for PRE_TEST, LEARNING, POST_TEST, and RECALL sessions. Evaluation-only responses must not train, transition, or alter later outcome items unless explicitly approved. | Supervisor/research-method expert | P3/P6 | Study protocol/model state |
| EDU-001 | Approve cohort, inclusion/exclusion, ethics, operational privacy versus research consent, withdrawal, facilitator procedure, and whether any formative participant work may occur before release. | Supervisor/institution | P4, before participants | Human evaluation governance |
| EDU-002 | Approve task-to-KC mapping, prerequisite controls, equivalent pre/post forms, scenario exposure/counterbalancing, instruments, SUS version/language/scoring, and accessibility accommodations. | Supervisor/learning-method expert | P3/P6 | Measurement validity |
| EDU-003 | Approve the primary estimand and outcome, comparator or explicit non-causal claim boundary, unit of analysis, statistical tests, effect/uncertainty reporting, multiplicity across KCs, and missing-data/exclusion handling. | Supervisor/research-method expert | P3/P6 | Analysis and thesis claims |
| EDU-004 | Approve recruitment target and power/sample-size rationale, latest feasible recruitment date, stopping rules, and the under-recruitment/underpowered contingency. | Supervisor/institution | P4/P6 | Study completion claim |
| EDU-005 | Approve the event/codebook definitions for time, pauses, assistance exposure, retries/offline delay and abandonment; the pseudonymized export schema; analysis environment; and retention/access for raw and derived evidence. | Supervisor/research/data owner | P3/P6 | Instrumentation and reproducible analysis |
| SEC-001 | Confirm Malaysian PDPA/institutional applicability, privacy notice, consent/withdrawal, retention, deletion/anonymization, minors, hosting region, research-data controller, shared-device/offline-queue clearing, and lawful handling of each data class. | Institution/supervisor | P4, before personal data | Production/research data |
| SEC-002 | Decide login identifier policy, public learner registration, admin enrollment, recovery, MFA, idle/absolute session lifetime, concurrent sessions, revocation, emergency access, and capability assignment for aggregates, learner-level access, logs, exports, enrollment, and privacy maintenance. | Owner/institution | P4 | Production authentication/authorization |
| SEC-003 | Approve the risk-based ASVS 5.0.0 profile, mandatory higher-assurance controls for privileged/research functions, vulnerability-severity and exception expiry rules, and whether an independent security reviewer is required. | Security reviewer + owner | P4/P5 | Security release evidence |
| PERF-001 | Approve representative minimum hardware/OS/GPU/browser, catalogue/scene/settings, 30 FPS and raycast interpretations, instrumentation, foreground/power/thermal/network conditions, repetitions, run-validity and flake rules, percentile/window algorithms, raw format, visual-baseline environment/masks, and regression policy. | Supervisor | P1/P5 | Performance/visual acceptance |
| ACC-001 | Define an accessible equivalent for inherently visual spatial assessments, relevant WCAG 2.2 AA criteria, browser/assistive-technology/zoom matrix, and the supported accommodation/conformance claim. | Supervisor/accessibility reviewer | P2/P4 | Accessibility acceptance |
| DEP-001 | Select hosting, same-origin feasibility, TLS/reverse proxy, database service, backup retention, restore target, monitoring, secret manager, and artifact retention locations. | Owner/supervisor | P4/P5 | Deployment |
| SYS-001 | Freeze the supported MySQL/InnoDB version, isolation level, SQL mode, UTC/database time-zone behavior, character set/collation, CI topology, lock order, idempotency-result representation, and deadlock/lock-timeout classification and retry bounds. | Developer + architecture reviewer | P1 | Transaction and concurrency oracle |
| SCOPE-001 | Approve DEV-013. Correct time/location geometry and the resulting seasonal sky remain MVP; decide separately whether any light-pollution, weather, atmospheric visibility, or season-specific environmental model is required. | Supervisor | P2 | Product scope |
| SCOPE-002 | Record thesis submission date, available developer weeks, expert/licence/ethics lead times, phase timeboxes, latest-decision dates, minimum defensible thesis cut line, and explicit deferral/claim-reduction triggers. | Student + supervisor | P1 and every gate | Feasibility and critical path |

## Approval record template

```text
Decision ID:
Selected option/value:
Classification: MANUAL DOMAIN DECISION or approved PROPOSED DEVIATION
Status: Approved, Rejected, Superseded, or Deferred
Needed-by phase and latest decision date:
Authority and source:
Approver:
Date:
Affected specification/ADR/version:
Rationale and limitations:
```
