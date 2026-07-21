# Implementation phases

The phases are ordered for a single developer. Each phase loads only the technical
context it needs. Later participant, deployment, meeting, or institutional decisions do
not block earlier local implementation.

## Phase 0: repository scaffold

**Goal:** create the empty monorepo, tooling, package boundaries, and test harness.

**Implement:** workspace/package manifests; pinned Node/TypeScript/tool versions;
`apps/`, `packages/`, and `tools/` layout from `ARCHITECTURE.md`; shared TypeScript
configuration; formatter/linter/type-checker; unit/reference/integration/E2E test
partitions; dependency rules; minimal CI scripts; empty typed public entry points.

**Do not implement:** catalogue data, astronomy formulas, cultural mappings, scoring,
BKT policy, persistence, accounts, participant instrumentation, or deployment.

**Exit:** clean install and scripts work; every workspace compiles; a sample unit test
and browser smoke test prove discovery; forbidden imports fail; no placeholder is
presented as domain truth.

## Phase 1: astronomy and data technical spike

**Goal:** retire uncertainty about catalogue acquisition, typed coordinate flow,
candidate astronomy libraries, independent reference generation, and runtime data
shape.

**Read additionally:** `ASTRONOMY_SPEC.md`, `DATA_STRATEGY.md`, ADR-003/004/007. Load
formal science governance only when preparing approval evidence.

**Implement:** replaceable catalogue-source adapter; source/manifest/schema prototypes,
including generic `SkyPattern`, `GuidanceRelationship`, and `LessonRoute` schemas;
typed catalogue/propagated/horizontal/scene values; small synthetic or clearly labelled
candidate fixtures; comparison harness against an independent reference; deterministic
serialization/checksum experiment.

**Do not claim:** an approved catalogue, approved cultural content, production
astrometry, final tolerance, or learner-facing correctness.

**Exit:** the spike identifies a viable implementation path and produces reproducible
comparison evidence; rejected spike code can be removed without changing application
contracts.

## Phase 2: minimal celestial-guidance vertical slice

**Goal:** deliver one validated local multi-step journey from an approved sky-pattern
route to Al-Jady/Polaris through server-issued scenario, 3D presentation, raw learner
response, server scoring, and feedback. The route may use a reviewed helper pattern and
Banat Na'sh or Dhat al-Kursi; it is selected from data rather than hardcoded. Persistence
and BKT adaptation are not required yet.

**Entry decisions:** IMP-008, IMP-009, IMP-011, and IMP-012 must be resolved for the
selected slice; IMP-018 already fixes the generic structure. Only the patterns,
relationships, route steps, scenario, scientific pipeline, and tolerances actually used
by this slice need approval. Other helper paths and later lesson, participant, account,
or deployment decisions remain deferred.

**Implement:** approved minimal generated dataset; reviewed `SkyPattern` and
`GuidanceRelationship` records; one `LessonRoute` with ordered steps and allowed
alternatives; deterministic scenario route selection constrained by required-star
availability; astronomy transformation; scene adapter; one interaction/answer form;
API scoring; accessible non-pointer control appropriate to this slice; reference and
browser evidence.

**Exit:** a clean local run reproduces the data and route hashes and independent
expected result; removing a required star makes the route ineligible; the browser never
owns route eligibility, target, tolerance, or correctness; boundary and raycast tests
pass; the slice is explicitly limited to its approved content and scenario.

## Phase 3: assessments and BKT adaptation

**Goal:** expand task types and add pure, versioned BKT plus adaptive scaffolding.

**Read additionally:** `TUTORING_BKT_SPEC.md`, ADR-005, and the relevant assessment
sections of `ASTRONOMY_SPEC.md`.

**Entry decisions:** approve the observation taxonomy, parameters, thresholds,
scaffold cues, task-to-KC mapping, and evaluation-session isolation needed by the
implemented tasks. Participant recruitment or ethics is not required for synthetic and
local functional testing.

**Implement:** five-KC model interfaces; pure BKT; adaptive policy; typed no-update and
transition-only decisions; issued cue snapshots; assessment types; deterministic model
and policy traces.

**Exit:** independent BKT sequences, scoring boundaries, policy transitions, assistance
semantics, sensitivity evidence, and local E2E journeys pass without participant data.

## Phase 4: persistence and authentication

**Goal:** make attempts/mastery durable and introduce secure learner/admin identity
boundaries.

**Read additionally:** ADR-006. Load privacy/security governance when choosing account,
personal-data, privileged-access, or release policy.

**Implement:** migrations; transaction/idempotency/revision flow; retry reconciliation;
sessions; ownership/capability authorization; learner progress; minimal read-only
aggregate administration. A development fixture identity is removed from production
composition.

**Exit:** real-MySQL fault/concurrency tests pass; matching retries return one result;
mismatches/stale submissions fail safely; authorization and session tests pass; no
production claim is made until release security/privacy policy is approved.

## Phase 5: complete lessons, dashboards and hardening

**Goal:** complete approved lesson content, learner/admin views, accessibility,
performance, security hardening, and reproducible evidence.

**Implement:** remaining approved content/scenarios; lesson flow; dashboards; supported
accessible equivalents; performance tuning; security controls; logging; evidence
manifests; backup/restore mechanics required by the selected release target.

**Exit:** all implemented requirements have code/test/evidence links; scientific,
browser, accessibility, performance, security, and restore suites pass under recorded
environments. Participant and deployment gates are still assessed independently.

## Phase 6: participant evaluation and deployment

**Goal:** run only the approved participant protocol and deploy only to an approved
target. Either activity may be omitted without invalidating the completed local
software evidence; the thesis claim must reflect what actually occurred.

**Read additionally:** the relevant files in `docs/governance/` for participant
research, privacy/security release, deployment, and thesis traceability.

**Entry:** participant work requires its own ethics/protocol/privacy readiness;
deployment requires its own hosting/security/operations readiness. One gate does not
silently satisfy the other.

**Exit:** record separate participant-study and deployment outcomes, immutable version
manifests, evidence limitations, and any withdrawn claims.
