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
candidate astronomy libraries, code-independent reference generation with explicit
lineage, and runtime data
shape.

**Read additionally:** `ASTRONOMY_SPEC.md`, `DATA_STRATEGY.md`, ADR-003/004/007. Load
formal science governance only when preparing approval evidence.

**Implement:** a bounded CDS I/311 acquisition/normalization experiment inside the
existing catalogue-tool boundary, while keeping its output behind stable internal
identifiers rather than treating that spike source as the permanent catalogue;
source/manifest/schema prototypes, including generic `SkyPattern`,
`GuidanceRelationship`, and `LessonRoute` schemas;
typed catalogue/propagated/horizontal/scene values; small synthetic or clearly labelled
candidate fixtures; a pinned Python/Astropy reference producer that is code-independent
of future TypeScript but discloses shared ERFA/SOFA lineage, and a comparison harness
under `tests/reference`; deterministic serialization/checksum
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
resolves documented I/311 field semantics while retaining the named time-scale gap,
fixed UFUQ coordinate conventions, typed scientific-state separation, and
reference-test requirements. It remains open:
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
tolerance questions. Milestone 2C.6 classifies which questions actually gate a bounded
implementation and which belong to data authority, postimplementation validation, or
later extensions.

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
visibility, warning, learner-eligibility policy, or tolerance. The later semantic-scope
audit makes geometric-only output, disabled refraction, no atmosphere defaults, no
aggregate visibility, result-bearing below-horizon classification, and non-erasing
optional-stage precedence normative for V1. AST-004/006/007 review remains required
only for the later capabilities and numerical boundaries.

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

Milestone 2C.5B completes 9/9 experiments in the five-group synthetic Batch 01 scope.
The non-production Python runner promotes the already locked PyERFA `2.0.1.5` package
to a direct dependency, rejects non-Batch/source/production inputs and partition drift,
consumes nine fixed canonical schema-validated fixtures, and emits nine canonical
results with complete hashes and two-repetition manifests. Twenty-four exact
contract/status/determinism checks pass and none fail; six measurement-only checks
cover 27 measurement records, all `MEASURED_NO_ACCEPTANCE`. Componentized versus
composed ERFA evidence is explicitly same-family consistency, not independent
scientific validation. No production code is compared, so `test:reference` remains
inactive. The evidence changes no source meaning, data eligibility, implementation
selection, operating-domain, or tolerance state.

Milestone 2C.5C interprets the committed Batch 01 evidence without changing or
rerunning its hashed inputs. A human framework and machine-checkable AST-006 ledger
inventory all 27 measurement records, all 24 passing exact checks, and 49 source,
model, Earth-orientation/time, observer, atmosphere, implementation, scene, and
learner terms. Of those ledger terms, 45 retain an unbounded numerical-bound state
and four are exact non-numerical aggregate guards, distinct from the 24 Batch checks.
Exact guards retire only bounded synthetic mutation/state-contract
classes; measured values, including zeros, remain without acceptance. The candidate
method uses boundary-specific metrics, conservative bounded sums when dependence is
unknown, covariance/joint treatment for correlated terms, and RSS only when
independence is justified. No required numerical term is bounded, all six tolerance
classes remain blocked, and `FINAL_TOLERANCE_NOT_JUSTIFIED` is prepared for AST-006
review. Milestone 2C remains open.

Milestone 2C.6 defines `ScientificProfileV1` and audits the exit gate.
The first profile is source-neutral and geometric-only: exactly one selected observer
preset identity under a generic fail-closed contract, one bounded explicit-UTC domain,
one minimal 2D-approved star artifact,
explicit normalized ICRS epoch/motion semantics, an approved route/effect disposition,
immutable offline leap/EOP inputs, fail-closed outcomes, disabled refraction, and no
aggregate visibility. Internal observer types remain multi-location capable. The audit
removes the circular requirement for TypeScript/reference residuals and numerical
tolerances before the TypeScript implementation exists. The selected V1 identity is
`umpsa-pekan-faculty-of-computing`; 2D, not 2C, owns its exact reference point,
coordinates, Earth model, typed height, accuracy and immutable data record. Milestone
The profile boundary, geometric/refraction/visibility exclusions, core outcomes,
precedence, exact singularity behavior, warning/status preservation, and pending-
validation lifecycle are normative. `APPROVED_GEOMETRIC_RESULT` remains unreachable
until postimplementation acceptance. Milestone 2C remains open only for the three
profile-scoped decisions in
`spikes/PHASE1_SCIENTIFIC_PROFILE_V1.md`; production/reference results, any stronger
independent validation required by the claimed release boundary, error-budget
population, and tolerance approval are later scientific-acceptance gates.

Milestone 2D records the data/source/deployment-authority outcome required before real
ProfileV1 execution. It selects the catalogue/release rather than inheriting I/311 from
the spike, approves acquisition/licensing and row eligibility, creates the stable
internal-star/source crosswalk and minimal allowlist, and selects the exact permitted
operational leap/EOP artifacts. It also acquires and approves the concrete UMPSA Pekan
Faculty `ObserverPreset` data and provenance before real ProfileV1 execution; a JUPEM
survey-control record is optional rather than mandatory. Unresolved redistribution
authority does not become permission to track or deploy I/311-derived rows.

Milestone 2E implements the local read-only catalogue parser, runtime validation, and
deterministic generation after Milestones 2C and 2D. Inputs and outputs remain ignored
and local unless separate redistribution/deployment authority explicitly permits
otherwise. Source-derived fixtures, cultural membership, and learner-facing content
remain outside this milestone until their scientific or human-review gates are met.

The corrected dependency order is 2C.6 profile approval -> 2D data/source authority ->
2E parser and deterministic data -> first bounded production astronomy implementation
-> production/reference comparison and `test:reference` activation -> any stronger
independent-oracle validation required by the claimed release boundary -> numerical
tolerance approval when justified -> later location/refraction/visibility extensions.
A comparison failure blocks scientific
acceptance and can force a revision; the comparison cannot be a prerequisite to the
implementation that produces it.

**Exit:** the spike defines an approved `ScientificProfileV1` implementation path,
explicit source/data handoffs, fail-closed behavior, and reproducible preimplementation
reference/protocol evidence. It does not require production/reference residuals or a
final numerical tolerance before production code exists; rejected spike code can be
removed without changing application contracts.

## Phase 2: minimal celestial-guidance vertical slice

**Goal:** deliver one validated local multi-step journey from an approved sky-pattern
route to Al-Jady/Polaris through server-issued scenario, 3D presentation, raw learner
response, server scoring, and feedback. The route may use a reviewed helper pattern and
Banat Na'sh or Dhat al-Kursi; it is selected from data rather than hardcoded. Persistence
and BKT adaptation are not required yet.

**Entry decisions:** the generic `ObserverPreset` types, validators, no-default branches,
and observer-generic astronomy interfaces do not require the UMPSA numerical values.
Real ProfileV1 execution and data-backed fixtures require the selected 2D/2E numerical
artifacts, approved profile semantics, and preset observer/time inputs under
IMP-008/009 and the astronomy-input part of IMP-012. IMP-011 and the learner/
scoring part of IMP-012 gate only integration into a learner-facing lesson; missing
cultural evidence does not block the astronomy engine. IMP-018 already fixes the
generic structure. A final scientific or learner tolerance is not an
implementation-entry requirement. It remains mandatory before the corresponding
postimplementation scientific or scoring acceptance claim. Other helper paths and
later lesson, participant, account, or deployment decisions remain deferred.

**Implement:** approved minimal generated dataset; reviewed `SkyPattern` and
`GuidanceRelationship` records; one `LessonRoute` with ordered steps and allowed
alternatives; deterministic scenario route selection constrained by required-star
availability; astronomy transformation; scene adapter; one interaction/answer form;
API scoring; accessible non-pointer control appropriate to this slice; reference and
browser evidence.

**Exit:** a clean local run reproduces the data and route hashes; the production route
has postimplementation pinned-reference results, any stronger-independent evidence
required by the approved release gate, and reviewed operation-specific acceptance;
removing a required
star makes the route ineligible; the browser never owns route eligibility, target,
tolerance, or correctness; boundary and raycast tests pass; the slice is explicitly
limited to its approved content and scenario.

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
