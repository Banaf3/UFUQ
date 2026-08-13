# Implementation status

**Assessment date:** 2026-08-10

The consolidated Phase 0 repository scaffold is validated. It contains health-only web
and API applications, eight npm workspaces, pure empty/type-placeholder production
domain boundaries, pinned tooling, fail-closed suite configurations, boundary checks,
and CI. The independent non-npm Python tool now contains a locked, synthetic-only
Astropy smoke oracle; production TypeScript still contains no astronomy calculation.
The repository contains no catalogue/cultural record, BKT formula,
persistence/authentication behavior, dashboard, or deployment configuration.

## Independent readiness gates

| Gate | Result | Basis |
|---|---|---|
| Repository scaffolding | YES | The consolidated eight-workspace TypeScript monorepo, non-npm oracle boundary, strict compiler/build setup, test discovery, dependency enforcement, lockfile, and CI are validated. |
| Validated celestial-guidance vertical slice | NO | The local I/311 parser contract is defined, but redistribution/deployment, selected-row scientific review, cultural membership/route approval, the production astronomy pipeline/error budget, scenario, and scoring tolerances remain unresolved. |
| Participant study | NO | Participant protocol, ethics applicability/approval, instruments, recruitment, privacy, consent, data handling, and study-ready software remain unresolved or unimplemented. |
| Deployment | NO | Hosting/operations target, production account policy, security/privacy release profile, performance/accessibility baselines, monitoring, and backup/restore evidence remain unresolved or unimplemented. |

READY_FOR_SCAFFOLDING: YES

READY_FOR_VERTICAL_SLICE: NO

READY_FOR_PARTICIPANT_STUDY: NO

READY_FOR_DEPLOYMENT: NO

## Phase 0 reference-study state

The local source library has been studied for current-phase needs without starting the
astronomy/data implementation spike. Tracked outputs now include a reading plan,
twenty-one source-specific dossiers, five cross-source syntheses, a coverage report, and
five project-scoped skills with mandatory-rule traceability.

The source study by itself did not select a catalogue and does not approve a production
astronomy pipeline, schema validator, Kaaba coordinate/datum, numerical tolerance,
cultural mapping, or learner-facing route. The separate project decision below now
selects I/311 only for the Phase 1 local technical spike. A locked synthetic Astropy
environment now closes the environment-compatibility smoke milestone, but it does not
settle production astronomy or source-derived validation. Najdi/regional evidence, a
stable edition for the studied Ibn Qutaybah
claims, exact membership/route evidence, and human Arabic/cultural review remain
required before learner-facing cultural claims.

The official I/311 archive Appendix G now confirms that I/311 `pmRA` is
`mu_alpha_star`; the normalized parser field maps directly to Astropy `pm_ra_cosdec`
after unit conversion. The high-declination omitted/double-cosine astronomy tests
remain required. I/311 states `Ep=1991.25`; official ESA Gaia DR1 documentation
directly identifies I/311 and calls the parameter epoch `J1991.25`, resolving the
representation as Julian. Neither record defines the I/311 time scale for production
propagation.

The detailed evidence boundaries are in `references/PDF_KNOWLEDGE_COVERAGE.md`.

## Phase 1 Milestone 1 decision audit

The documentation-only source, policy, licensing, and performance audit is complete.
It is recorded in `spikes/PHASE1_ASTRONOMY_DATA_SPIKE.md`. No implementation stage has
begun.

CDS I/311, *Hipparcos, the New Reduction*, is approved only as the sole source for the
bounded Phase 1 local technical spike. No alternate adapter is required inside that
spike. The production catalogue/release remains a 2D decision, and the source-neutral
`starId`/source-release crosswalk permits a reviewed source to coexist with or replace
astrometry without coupling cultural records to copied coordinates.

I/311 local structure is verified, acquisition provenance is partial, derived-data
redistribution remains unresolved, and the local-only parser boundary is defined in
Milestone 2B.
The documented 30 FPS and under-100-ms raycast targets were found, but their
measurement protocol, primary device, browser/WebGL renderer, and representative
product scale remain unapproved.

The synthetic-oracle smoke milestone is complete using only explicit synthetic inputs.
No catalogue parser, source-derived fixture, generated catalogue artifact, production
astronomy behavior, scene, renderer, or performance collector was created.

### Milestone 2C scientific behaviour evidence audit

The Scientific Behaviour Contract in
`spikes/PHASE1_SCIENTIFIC_BEHAVIOUR_CONTRACT.md` was audited against the tracked SOFA,
IERS, I/311, ESA Hipparcos, and validation-study dossiers; the astronomy synthesis and
skill traceability; the Astronomy Specification and ADRs; and the actual locked oracle
artifacts.

The audit resolves the contract-level status of I/311 ICRS input semantics, the literal
`Ep=1991.25` source label, Julian representation, starred-alpha `pmRA`, UTC/TAI/TT/UT1 roles, UFUQ sign and
horizontal conventions, coordinate-state separation, structured-outcome requirement,
comparison metrics, and the code-independent reference protocol with shared-lineage
disclosure. It also corrects the
source-gap records: Astropy `8.0.1` reference-design pages and the official PyERFA
`2.0.1.5` release/hash are pinned. The PyERFA stable API is one patch behind, and the
production science protocol remains incomplete.

Milestone 2C.1 precisely bounds the remaining epoch gap. `SOURCE_SUPPORTED_FACT` covers
the I/311 wording and ESA's I/311-specific `J1991.25`; `AUTHORITY_OR_EVIDENCE_MISSING`
covers the unstated time scale. The bounded `PROJECT_DECISION` preserves the label and
Julian representation while source-derived propagation remains unavailable. Batch 01
runs the bounded synthetic TT/TDB/UTC, calendar-year, and Besselian-guard cases, but
named astronomy review and an authoritative source interpretation are still required;
experiment output cannot become source authority.

Milestone 2C.2 defines a proposed componentized SOFA `2023-10-11` CIO-family route:
source-to-declared-target-epoch space motion, observer-aware CIRS, an explicit
Earth-orientation context, geometric horizontal output, optional refraction, and
separate visibility and scene states. J2000.0 is only the candidate epoch input for the
selected `iauAtciq`/`iauAtco13` path, not a frame conversion. Its effect matrix records
candidate semantic inclusion of frame bias, IAU 2006 precession with IAU 2000A
nutation, annual aberration, solar deflection, ERA-based Earth rotation, and diurnal
aberration. The `iauApco13` convenience branch supplies model CIP/CIO and accepts
`UT1-UTC` and polar motion `xp`,`yp`, but it cannot apply observed celestial-pole
offsets `dX`,`dY`; those corrections require a reviewed lower-level route. Proper
motion, parallax/RV, polar motion, celestial-pole offsets, and refraction retain blocked
or conditional gates. Astropy and PyERFA remain a reference path independent of future
TypeScript code, while their shared ERFA/SOFA lineage and composed ERFA `atco13` make
the applicable comparisons same-family consistency checks rather than stronger
independent validation. Batch 01 runs the
bounded composed/componentized case and five convention guards; the remaining route/
effect families and broader partitions are unrun or blocked.

Milestone 2C.3 records `SOURCE_SUPPORTED_FACT` from the distinct official Bulletin A
rapid-estimate/prediction, Bulletin B final/preliminary, Bulletin C announcement, and
`finals2000A` field-flag roles for `xp`,`yp`,`UT1-UTC`,`dX`,`dY`; Bulletin C is not a
selected machine-readable production leap artifact. RFC 3339 supplies the broader
timestamp/leap syntax. Its `PROJECT_DECISION` proposal uses a Z-only restricted UTC
boundary, explicit
geodetic/ellipsoidal observer provenance and uncertainty, immutable hash-addressed
offline EOP/leap bundles, separate reviewed atomic updates and old-bundle replay,
separate per-field source quality, availability, provenance, coverage, and scientific
approval with any unavailable or unapproved required field blocking, supported-domain
intersection, and explicit endpoint outcomes with deterministic semantic precedence.
IERS-estimate, predicted, preliminary, stale,
zero-filled, nearest-value, extrapolated, and
degraded execution remain unapproved. Batch 01 runs only the bounded offline canonical
replay guard; the scientific EOP/status/degradation/time/observer/domain experiments
remain unrun or blocked.

Milestone 2C.4 records `SOURCE_SUPPORTED_FACT` for SOFA `iauRefco` inputs and
`iauAtioq`'s numerical guard, plus Astropy `8.0.1` `AltAz` pressure/default and
low-altitude limitations. Its `PROJECT_DECISION` proposal uses geometric altitude only
for the first vertical slice, requires an explicit provenance-bearing atmosphere with
no defaults for optional refraction, keeps six horizon meanings and nine visibility
components distinct, preserves below-geometric-horizon as a non-terminal classification
attached to the valid direction, and extends optional-stage outcome precedence without
erasing its coordinates, provenance, warnings, or statuses. Physical dip,
cloud/weather, and light pollution remain separate. The refraction model/ranges,
near/below-horizon validity, warnings, physical dip, terrain, photometric/daylight,
extinction/transparency, cloud/weather, light pollution, screen, learner eligibility,
and tolerances remain blocked. Approved and warning-bearing refracted results remain
unreachable. Seven experiment families are specified; Batch 01 later runs only the
bounded state/no-default/visibility guard subsets, not the blocked numerical studies.

Milestone 2C.5A freezes the experiment protocol without executing numerical work. The
human and machine registries contain 24 stable records, each separating executability,
permitted and prohibited claims, inputs/conventions/artifacts, comparison lineage,
metrics, deterministic repetition/hashes, result schema, pass/fail basis, reviewer
gate, and follow-up decision. Seventeen records are runnable with explicit synthetic
inputs only, five are blocked by project decisions, one by a required independent
data/model path, and the production/reference comparison is deferred. Astropy
high-level and direct PyERFA routes retain their shared ERFA/SOFA lineage; their
agreement is consistency evidence, not independent validation. A five-group
synthetic-only first batch is proposed for 2C.5B, but no experiment body, fixture
instance, result, error-budget ledger, or threshold is added in 2C.5A.

Milestone 2C.5B implements and completes exactly 9/9 Batch 01 experiments. The
locked PyERFA `2.0.1.5` release is now a direct dependency of the non-production Python
runner; no dependency version or unrelated package changes. Nine canonical synthetic
fixtures produce nine schema-validated canonical results plus companion hashes. The
runner rejects unknown/non-Batch IDs, source/production material, partition drift,
noncanonical bytes, and stale manifests; every experiment executes twice in a fresh
offline cache context, and the complete command is replayed in two independent OS
processes in the same pre-synchronized locked environment. This does not reconstruct a
clean virtual environment. Twenty-four exact contract/status/determinism checks pass,
none fail, and six measurement-only checks cover 27 measurement records, all
`MEASURED_NO_ACCEPTANCE`. The componentized/composed result is same-family ERFA/SOFA
consistency only. No production
comparison exists, so `test:reference` remains inactive.

The final epoch-label evidence explicitly supplies a synthetic ITRS-geocentre
`[0,0,0] m` location to every affected Astropy `Time` constructor. It is only a TT/TDB
conversion reference location and does not approve a physical observer or production
observer policy. All three cases also initialize and evidence the pinned smoke-only
leap artifact in isolated execution; this does not approve production leap data. The
schema/tests reject missing or nonzero variants. This correction
invalidated all earlier Batch results, manifests, output hashes, and replay claims; the
final nine-result inventory was regenerated only through the runner before the
isolated-process/cache replay.

Milestone 2C.5C reads those committed results without regenerating canonical Batch 01
evidence or changing any hashed input. The new human framework and machine-checkable
AST-006 ledger retain
all 27 measurements, including serialized zeros, and all 24 exact passes with the
specific fault class each can and cannot retire. Forty-nine terms are separated across
source, model, Earth-orientation/time, observer, atmosphere, numerical implementation,
scene, and learner layers: 45 terms retain an unbounded numerical-bound state, while
four aggregate ledger terms are exact non-numerical guards distinct from the 24 Batch
checks. Scene/learner quantities cannot weaken astronomy accuracy;
RSS requires evidenced independence; and any required unbounded term leaves the case
unbounded. All six tolerance classes are blocked with no numerical value. The AST-006
recommendation is `FINAL_TOLERANCE_NOT_JUSTIFIED` pending named review and future
evidence.

Milestone 2C.6 audits the circular exit gate and defines a candidate
`ScientificProfileV1`. The first profile is one-preset, one-bounded-UTC-domain,
source-neutral, offline, fail-closed, and geometric-only. Refraction is disabled, no
atmosphere default exists, and no aggregate scientific visibility claim is produced.
Internal observer and astrometry types remain extensible to later locations and source
releases. I/311 is not promoted from spike source to permanent catalogue; its authority,
rights, row eligibility, and unresolved time scale move to 2D if 2D retains it.

The observer-preset audit selects only the identity
`umpsa-pekan-faculty-of-computing` (Faculty of Computing, UMPSA Pekan Campus, Pahang,
Malaysia) and fixes the generic `ObserverPreset` semantics and no-default behavior.
Actual latitude, longitude, reference point, datum/frame/ellipsoid, typed height,
applicable coordinate epoch, accuracy, provenance, version and immutable record belong
to 2D. Their absence blocks real V1 execution, not 2C closure or generic astronomy-core
work. A JUPEM survey-control record is optional, not mandatory.

The semantic-scope audit makes three clusters normative: the profile boundary/typed
exclusions/pending-validation state; geometric-only/refraction-disabled/no-atmosphere-
default/no-aggregate-visibility scope; and fail-closed outcomes, non-erasing
precedence, exact zenith/nadir singularity, and warning/status preservation.
`GEOMETRIC_RESULT_PENDING_VALIDATION` is the initial executable success state;
`APPROVED_GEOMETRIC_RESULT` remains unreachable until postimplementation acceptance.
No numerical ill-conditioned-azimuth boundary is invented.

Milestone 2C remains **OPEN**, but only for three exact preimplementation decision
clusters: the pure-TypeScript route and effect dispositions; one exact UTC grammar/
precision and date interval; and leap/EOP product-class and field/offline policy.
Production code,
production/reference residuals, any stronger independent validation required by the
claimed release boundary, numerical tolerance, global locations, refraction,
visibility, and numerical closure of all 49 ledger terms
do not keep 2C open. They retain their data, postimplementation acceptance, later-
extension, or learner-content gates. The decision is
`2C_REMAINS_OPEN_WITH_EXACT_PREIMPLEMENTATION_BLOCKERS`.

### Milestone 2B catalogue authority and provenance

The source/release, complete main-table field contract, supplemental-solution policy,
missing/duplicate/invalid-row behavior, `pmRA` semantics, exact 19-HIP technical review
allowlist, numerical/cultural separation, canonical schemas, deterministic
serialization, manifest, and checksum requirements are recorded in
`spikes/PHASE1_CATALOGUE_AUTHORITY_PROVENANCE.md`.

This completes the parser contract but does not authorize source-derived processing.
Phase 1 Milestone 2E may implement the local, read-only, fail-closed parser against
ignored hash-identified bytes only after Milestone 2D records the required
source/deployment-authority outcome. It does not authorize source-derived Git artifacts
or deployment: VizieR supports scientific-context use with attribution, but I/311
raw/derived redistribution remains unresolved. The HIP list is a retrieval and review
candidate only; all Arabic forms, memberships, pattern edges, relationships, teaching
roles, and row-level scientific suitability still require the recorded human reviews.

### Milestone 2A modern synthetic-only retry

The earlier exact candidate set remains recorded as a failed experiment: Astropy 7.2.2
required `astropy-iers-data>=0.2026.6.22.1.23.34`, conflicting with the proposed older
IERS-data pin. The retry deliberately used a current stable compatible stack rather
than the minimum release satisfying that old constraint.

Exact CPython 3.14.6 and uv 0.11.32 now lock Astropy 8.0.1,
`astropy-iers-data` 0.2026.7.20.15.31.18, NumPy 2.5.1, packaging 26.2, PyERFA
2.0.1.5, and PyYAML 6.0.3. At the 2A checkpoint, Astropy and IERS data were direct and
PyERFA was transitive. Milestone 2C.5B subsequently promotes the same locked PyERFA
release to direct because its bounded runner imports `erfa`; NumPy, packaging, and
PyYAML remain transitive.

The two valid synthetic transforms and one structured invalid case passed seven
unittests. Automatic IERS download/general Astropy internet access are disabled,
connection attempts fail closed, a fresh temporary cache is used, and the actual
packaged Earth-orientation/leap-second files and hashes are recorded. Two separate
locked offline executions produced byte-identical canonical output with SHA-256
`2e179cad1d694e8da42a12d19ec854d7955ce89c617e791bc0ade43ceed3d2a4`
after regenerating environment evidence for the PyERFA dependency-kind change; the
smoke astronomy inputs and coordinate outputs are unchanged.
A fresh environment was reconstructed offline from existing package caches, so the
honest reproduction classification is `CACHE_DEPENDENT_OFFLINE_EXECUTION`, not a full
air-gapped rebuild.

The oracle imports no UFUQ production package, executes no Node astronomy code, and
contains no catalogue value or identifier. It establishes no production algorithm,
scientific tolerance, final IERS date policy, refraction policy, or source-derived
authority. Milestone 2B is complete; source-derived parsing, propagation, and
production/reference comparison remain unauthorized and unstarted.

Milestone validation: exact uv lock check and locked offline sync passed; 7 Python
unittests passed; two isolated generations were byte-identical; a fresh temporary
environment reconstructed from populated caches; `npm.cmd run check`, `test`,
`cycles`, `exports:check`, `build`, and `test:e2e` all passed. `test:reference` still
fails closed because production/reference comparison has not begun. Restricted,
raw/generated-data, dependency/source-diff, environment/binary, secret, and staged-file
scans passed.

## Validated Phase 0 structure

The eight npm workspaces are:

1. `apps/web`
2. `apps/api`
3. `packages/astronomy-core`
4. `packages/assessment-core`
5. `packages/tutoring-core`
6. `packages/contracts`
7. `packages/catalogue-schema`
8. `tools/catalogue`

`tutoring-core` retains logical `bkt`, `observations`, and `adaptive-policy` modules
without separate package overhead or an assessment dependency. `catalogue-schema`
retains logical `catalogue`, `content`, and `artifact` modules and may later add
framework-free validators. `tools/catalogue` owns future pipeline modules internally.
`tools/astronomy-reference` is a separate locked Python/Astropy synthetic smoke oracle
with versioned JSON input/output envelopes and no npm or production-astronomy
dependency.

Tracked provenance and reviewed curation have separate directories. `data/raw/` is
ignored by default; locally acquired candidate bytes may exist there without becoming
part of the scaffold or a selected production catalogue. The data guard permits only
ignored/untracked raw content and rejects any tracked or unignored raw byte. No
catalogue or cultural record is part of a tracked runtime artifact. Compiler state,
declarations from the private web app, Vite output, and other build directories are
ignored and untracked. Source/data text is normalized to LF by `.gitattributes`, while
the future canonical data serializer must independently enforce UTF-8, LF,
deterministic key/record order, and defined numeric formatting.

## Validation evidence

| Command/check | Exact result on 2026-07-22 |
|---|---|
| `npm.cmd ci` | PASS; 306 packages installed from the lockfile. |
| `npm.cmd run format:check` | PASS; all matched files use Prettier style. |
| `npm.cmd run lint` | PASS; applications, packages, catalogue tool, tests, scripts, and root config modules reported no ESLint error. |
| `npm.cmd run typecheck` | PASS; seven composite Node/shared projects, the private no-emit web app, and test/config sources typechecked. |
| `npm.cmd run test` | PASS; 1 unit file and 1 API health test. |
| `npm.cmd run boundaries` | PASS; 8 workspaces, approved edges, no cycle/private import/runtime-to-tool edge, code-independent reference-tool boundary. |
| `npm.cmd run cycles` | PASS; the same graph check explicitly confirmed acyclicity. |
| `npm.cmd run data:verify` | PASS at the scaffold checkpoint; the guard now distinguishes permitted ignored local raw candidates from prohibited tracked/unignored raw data. |
| `npm.cmd run build` | PASS; API, five shared packages, catalogue tool, and Vite web build completed; Vite transformed 16 modules. |
| `npm.cmd run exports:check` | PASS; 13 public export paths across 7 importable workspaces resolved. |
| `npm.cmd run test:e2e` | PASS; 1 Chromium web/API health smoke test. |
| `npm.cmd run test:reference` | Expected inactive-suite failure; exit 1 with include `tests/reference/**/*.test.ts`. |
| `npm.cmd run test:integration` | Expected inactive-suite failure; exit 1 with include `tests/integration/**/*.test.ts`. |
| Tracking/import/scope scans | PASS; no tracked generated output, restricted PDF, secret environment file, raw catalogue byte, runtime-to-tool/private import, astronomy/BKT behavior, persistence/authentication behavior, or concrete cultural/catalogue data. |

The pre-consolidation findings are preserved in `STRUCTURE_AUDIT.md`. The exact path
mapping, commands, corrections, and independent post-migration verdict are in
`STRUCTURE_MIGRATION.md`. `SCAFFOLD_AUDIT.md` is a historical audit of the original
13-workspace working tree and is not the current status.

## Authorized next work

Phase 1 Milestones 1, 2A, and 2B are complete. Milestone 2C has an evidence-audited
contract but remains open only for the three `ScientificProfileV1` decision clusters
listed above. The next 2C work is named astronomy-expert and supervisor review of those
route/time/EOP choices; another synthetic batch and AST-006 numerical approval are not
prerequisites to starting the bounded implementation.

After profile approval, Milestone 2D selects the actual catalogue/release and minimal
star allowlist, records acquisition/licensing/row/crosswalk authority, approves the
permitted operational leap/EOP artifacts, and acquires/approves the concrete UMPSA Pekan
Faculty observer record. It must not inherit I/311 as a permanent source merely because
the spike studied it or require a survey-control monument merely because one could be
more precise. Milestone 2E then implements the parser, runtime validation, and
deterministic generated data.

The first bounded pure-TypeScript astronomy implementation follows 2E. Its
production/reference comparison then activates `test:reference`; stronger independent
validation (for example, a pinned USNO NOVAS candidate) and numerical tolerance review
follow. Production/reference evidence remains mandatory for scientific acceptance;
stronger independent validation applies where required by the claimed release
boundary. Neither is a circular prerequisite to implementation.

## Decisions that block the validated vertical slice

- **IMP-008 / AST-001 (`BLOCKS_2D_DATA_AUTHORITY`):** select the real catalogue/release
  and minimal allowlist; resolve acquisition, raw/derived handling, deployment rights,
  stable internal-star/source crosswalks, and row-level scientific eligibility. The
  local I/311 spike contract does not select a permanent source.
- **IMP-009 / AST-003 (`BLOCKS_SCIENTIFIC_PROFILE_V1`):** approve the candidate
  pure-TypeScript route/library mapping and effect dispositions, one bounded UTC
  domain, and leap/EOP field/offline policy. Generic one-preset semantics, geometric-
  only exclusions, fail-closed precedence, and pending-validation outcomes are now
  normative. AST-006 numerical tolerance and production/reference residuals are
  `POST_IMPLEMENTATION_VALIDATION`.
- **IMP-011 / AST-002:** reviewed `SkyPattern` and `GuidanceRelationship` records for
  one complete route to Al-Jady, including stable IDs, labels, membership, segments,
  instructional geometry/explanation, and review/verification status.
- **IMP-012 / AST-007:** the observer contract/site identity is fixed by 2C; its sourced
  numerical record is `BLOCKS_2D_DATA_AUTHORITY`, while the time-domain semantics remain
  preimplementation. Expected learner answers and learner/scoring tolerances remain
  downstream; scientific tolerance remains postimplementation.

BKT parameters/cues do not block the Phase 2 minimal slice because adaptation begins in
Phase 3. Persistence, authentication, participant, privacy/security release, and
deployment decisions belong to Phases 4-6 and do not block Phases 0-2.

## Default implementation documents

1. `../AGENTS.md`
2. `IMPLEMENTATION_BRIEF.md`
3. `ARCHITECTURE.md`
4. `IMPLEMENTATION_DECISIONS.md`
5. `PHASES.md`
6. `TEST_PLAN.md`
7. `STATUS.md`

Technical domain specs and ADRs are loaded by phase. `governance/` remains conditional
context for formal approvals, participant/privacy/deployment work, report deviations,
and thesis traceability.
