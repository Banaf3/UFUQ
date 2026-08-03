# Implementation phases

The phases are ordered for a single developer. Each phase loads only the technical
context it needs. Later participant, deployment, meeting, or institutional decisions do
not block earlier local implementation.

## Phase 0: repository scaffold

**Goal:** create the empty monorepo, tooling, package boundaries, and test harness.

The documentation-only source study and grounded-skill work is tracked in
`.agent/execplans/phase-00-reference-pdf-study.md`; it prepares later evidence without
activating Phase 1. The focused official ESA Hipparcos 1997 field-semantics integration
is tracked in `.agent/execplans/phase-00-esa-hipparcos-source-integration.md`; it also
does not activate Phase 1.

**Implement:** exactly eight npm workspace/package manifests; a non-npm independent
Python reference-tool scaffold; pinned Node/TypeScript/tool versions; the layout from
`ARCHITECTURE.md`; shared TypeScript configuration; formatter/linter/type-checker;
separate unit/reference/integration/E2E test discovery; dependency rules; minimal CI
scripts; empty typed public entry points. BKT, observations, and adaptive policy remain
logical modules inside `tutoring-core`; catalogue/content/artifact schemas remain
logical modules inside `catalogue-schema`.

**Do not implement:** catalogue data, astronomy formulas, cultural mappings, scoring,
BKT policy, persistence, accounts, participant instrumentation, or deployment.

**Exit:** clean install and scripts work; every applicable workspace compiles; the unit
and browser smoke tests prove active discovery; inactive reference/integration suites
are omitted from Phase 0 CI and fail closed when invoked empty; forbidden imports fail;
no placeholder is presented as domain truth.

## Phase 1: astronomy and data technical spike

**Goal:** retire uncertainty about catalogue acquisition, typed coordinate flow,
candidate astronomy libraries, independent reference generation, and runtime data
shape.

**Read additionally:** `ASTRONOMY_SPEC.md`, `DATA_STRATEGY.md`, ADR-003/004/007. Load
formal science governance only when preparing approval evidence.

**Implement:** a bounded CDS I/311 acquisition/normalization experiment inside the
existing catalogue-tool boundary, with no alternate-catalogue abstraction;
source/manifest/schema prototypes, including generic `SkyPattern`,
`GuidanceRelationship`, and `LessonRoute` schemas;
typed catalogue/propagated/horizontal/scene values; small synthetic or clearly labelled
candidate fixtures; an independently pinned Python/Astropy fixture producer and
comparison harness under `tests/reference`; deterministic serialization/checksum
experiment. The reference suite becomes mandatory when the first production/reference
comparison is introduced.

**Do not claim:** approval beyond the bounded I/311 Phase 1 local-spike selection,
redistribution or deployment rights, approved cultural content, production astrometry,
final tolerance, or learner-facing correctness.

Milestone 2B fixes the local parser contract in
`spikes/PHASE1_CATALOGUE_AUTHORITY_PROVENANCE.md`: corrected 2008-09-16 I/311 files,
complete source-field preservation, confirmed starred-alpha `pmRA`, an exact 19-HIP
technical review allowlist, fail-closed row/supplement policies, and versioned
artifact/provenance schemas.

Milestone 2C is the Scientific Behaviour Contract. Its 2026-08-03 evidence audit
resolves source-defined I/311 input semantics, fixed UFUQ coordinate conventions,
typed scientific-state separation, and reference-test requirements. It remains open:
Milestone 2C.1 resolves the I/311 epoch representation as Julian from official ESA
Gaia DR1's direct `J1991.25` use, but finds no I/311-applicable time scale. It therefore
keeps source-derived propagation unavailable and specifies a synthetic sensitivity
experiment plus human-review gate. Astropy `8.0.1` reference-design documentation is
pinned; the PyERFA stable-doc/runtime patch mismatch remains recorded. Milestone 2C.2
proposes a componentized SOFA `2023-10-11` CIO-family semantic route, a fully classified
candidate-included/conditional/blocked effect matrix, a separate Astropy/PyERFA
reference path, and eight experiment families. `Included` describes the proposed
semantic model only, not approved executable behaviour. CDS Catalogue Standard 2.0
resolves the 365.25-day
proper-motion `yr`, but the proposal does not approve the future TypeScript
implementation or close the epoch/derivative-scale, observer,
EOP/celestial-pole-offset, refraction/visibility, supported-range, error-budget, or
tolerance blockers. The contract grants no implementation authority while those
blockers remain.

Milestone 2C.3 pins the distinct official IERS Bulletin A/B/C roles and `finals2000A`
field-flag semantics and proposes the supported-domain boundary: a UFUQ-selected Z-only
RFC 3339 UTC subset, explicit
geodetic/ellipsoidal observer provenance, immutable hash-addressed offline EOP/leap
bundles, separately reviewed atomic updates with deterministic replay, independent
per-field source-quality/availability/approval state, fail-closed structured outcomes
with deterministic semantic precedence, and six additional
reference experiments. It selects no production product/hash, date/location/height
range, stale/update threshold, field-quality approval, degraded mode, or
tolerance. Milestone 2C remains open and source-derived execution remains blocked.

Milestone 2C.4 proposes geometric altitude only for the first vertical slice, explicit
atmosphere provenance with no default atmosphere, separate geometric/refracted
direction states, six distinct horizon states, nine independent visibility components,
optional-stage outcome precedence that retains the valid geometric result, and seven
experiment families. Official
SOFA/Astropy documentation supports the candidate input and limitation inventory but
does not approve a model, input/altitude range, near/below-horizon rule, terrain,
visibility, warning, learner-eligibility policy, or tolerance. AST-004/006/007 review
remains required, so Milestone 2C remains open.

Milestone 2C.5A freezes the scientific experiment protocol before numerical execution.
It records 24 stable experiment IDs with permitted/prohibited claims, exact input and
dependency requirements, shared-lineage disclosure, metrics, deterministic replay and
hash rules, result/acceptance semantics, reviewer gates, and follow-up decisions. A
machine registry plus separate fixture/result schemas support later deterministic
execution without widening the existing smoke fixture. Seventeen records can run now
only with explicit synthetic inputs; five await project decisions, one awaits a
required independent data/model path, and one awaits production. The proposed
five-group 2C.5B batch runs no source-derived input and cannot create authority,
production approval, a domain, an error budget, or a tolerance. No experiment body or
result is added by 2C.5A, `test:reference` remains inactive, and Milestone 2C remains
open.

Milestone 2D records the catalogue source/deployment-authority outcome required before
source-derived processing. It must explicitly resolve local processing authority and
the permitted handling of generated data; unresolved redistribution authority does not
become permission to track or deploy I/311-derived rows.

Milestone 2E implements the local read-only catalogue parser, runtime validation, and
deterministic generation after Milestones 2C and 2D. Inputs and outputs remain ignored
and local unless separate redistribution/deployment authority explicitly permits
otherwise. Source-derived fixtures, cultural membership, and learner-facing content
remain outside this milestone until their scientific or human-review gates are met.

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

**Implement:** five-KC model interfaces; pure BKT in `tutoring-core/src/bkt`; observation
semantics in `tutoring-core/src/observations`; adaptive policy in
`tutoring-core/src/adaptive-policy`; typed no-update and transition-only decisions;
issued cue snapshots; assessment types; deterministic model and policy traces.

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

The integration suite becomes mandatory with the first API/persistence integration
test and must use the frozen real-MySQL profile for transaction claims.

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
