# Architecture status

**Documentation state:** INDEPENDENT REVIEW COMPLETE; CORRECTIONS APPLIED

**Implementation state:** NOT READY FOR APPLICATION SCAFFOLDING

**Assessment date:** 2026-07-20

Five requested read-only role reviews were completed and synthesized in
`ARCHITECTURE_REVIEW.md`: software architecture/maintainability,
astronomy/provenance, BKT/adaptive scaffolding, verification/performance/educational
evaluation, and scope/report traceability. The restricted local report was inspected
without copying it into tracked artifacts. Findings were accepted, rejected with
evidence, deferred as optional, or retained as manual decisions.

## Review outcome

The TypeScript modular-monolith direction, pure-domain boundaries, server authority,
ENU/Three.js and spherical-Qibla mathematics, standard BKT update order, and
provenance-first data design remain recommended. The review corrected the following
material gaps:

- immutable authoritative scenario snapshots and shared API/browser catalogue hashes;
- request-fingerprinted idempotency, pre-provisioned mastery rows, monotonic per-KC
  revisions, stale-submission rejection, and one pending adaptive submission per KC;
- explicit BKT observation/no-op semantics and server-issued versus untrusted cue data;
- a complete astrometric-effect/error-budget decision envelope and no invented numeric
  or pixel tolerance;
- capability-scoped administration, durable sessions, fixture-identity exclusion,
  structured logs, and a risk-based security profile;
- evidence manifests, oracle-review independence, synthetic analysis dry-runs, and
  separate software/study/thesis completion verdicts;
- needed-by-phase decisions, capacity/cut-line governance, and report-authority anchors.

## Gates before Phase 1 scaffolding

1. Resolve every P1 item in `OPEN_QUESTIONS.md`, including AST-001/002/003/006/007,
   BKT-001/002/004, SYS-001, PERF-001, and SCOPE-002.
2. Approve or reject the P1-affecting entries in `REPORT_DEVIATIONS.md`, especially
   DEV-001–010 as applicable.
3. Approve ADRs 001–007 or record replacements; blocked ADRs stay blocked until their
   named inputs are approved.
4. Create and approve `.agent/execplans/phase-01-central-vertical-slice.md` under
   `.agent/PLANS.md`, including the exact database profile, scenario contract, minimal
   provenance pipeline, evidence manifest, schedule, and rollback.

Phase 0 decision work may proceed now. A local, non-participant Phase 1 may start only
after those four gates. Personal/research data, production authentication, deployment,
and participant work remain blocked until their later SEC/EDU/ACC/DEP gates.

## Quality-gate result after independent review

| Gate | Result |
|---|---|
| Objectives map to modules/tests and neutral report anchors | Pass after correction; see `TRACEABILITY.md` |
| Module responsibilities/dependencies clear | Pass after application-port/browser-scorer correction |
| Scenario authority and replay contract | Pass at architecture level; implementation blocked on inputs/SYS-001 |
| Astronomy convention scientifically complete | Blocked on AST-001–007; decision envelope is now complete |
| No invented catalogue/cultural mapping | Pass; source/content approval still blocks behavior |
| BKT equations/examples consistent | Pass; production evidence/policy decisions remain blocked |
| Atomic/retry model testable | Pass at architecture level; SYS-001 and deviations pending |
| Learner-account security sufficient | Not yet; SEC-001–003 and P4 implementation/evidence pending |
| Evaluation can support bounded claims | Planned; EDU-001–005 and recruitment remain blocking |
| Bachelor-level feasibility | Unproven until SCOPE-002 records calendar/capacity/cut line |
| MVP and optional work separated | Improved; persistent multi-opportunity offline work and delayed recall are not mandatory |
| Independent review evidence | Pass; `ARCHITECTURE_REVIEW.md` contains disposition index |

## Repository audit state

The repository remains documentation-only. Final static checks for Markdown links,
identifier/deviation/manual-decision references, restricted artifacts, and consistency
are recorded in `ARCHITECTURE_REVIEW.md`. Matching identifier sets are a syntactic
check only; semantic authority and evidence coverage are governed by the report
crosswalk and review dispositions.

## Core documents

- Product: `PRODUCT_SPEC.md`
- Architecture and ADRs: `ARCHITECTURE.md`, `adr/`
- Domains: `ASTRONOMY_SPEC.md`, `TUTORING_BKT_SPEC.md`, `DATA_STRATEGY.md`
- Assurance: `TEST_STRATEGY.md`, `SECURITY_AND_PRIVACY.md`, `TRACEABILITY.md`
- Delivery governance: `EXECUTION_PLAN.md`, `RISK_REGISTER.md`, `OPEN_QUESTIONS.md`, `REPORT_DEVIATIONS.md`
- Independent review: `ARCHITECTURE_REVIEW.md`
