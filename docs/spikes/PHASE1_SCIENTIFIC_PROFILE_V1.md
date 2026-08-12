# Phase 1 Milestone 2C.6: ScientificProfileV1 exit-gate audit

## Status and decision

- **Profile:** `ScientificProfileV1`
- **Profile state:** candidate; named astronomy-expert and supervisor approval required
- **Milestone decision:** `2C_REMAINS_OPEN_WITH_EXACT_PREIMPLEMENTATION_BLOCKERS`
- **Production astronomy implemented:** no
- **Numerical scientific tolerance approved:** no
- **Frozen Batch 01 evidence changed:** no

`ScientificProfileV1` is a deliberately narrow contract for starting the first real
UFUQ astronomy implementation. It accepts one approved observer preset and one bounded
UTC domain, consumes a small authority-approved star artifact through source-neutral
typed astrometry, and produces geometric horizontal directions only. It does not claim
global observer support, atmospheric refraction, scientific visibility, terrain,
weather, light pollution, rendering accuracy, learner tolerance, or scoring accuracy.

The profile is a permission-to-implement boundary, not a scientific-release approval.
An implementation result remains pending scientific acceptance until the later
production/reference, error-budget, and tolerance gates pass, together with any
stronger-independent-validation gate required for the claimed release boundary.

## Authority and evidence boundary

The candidate is grounded in the existing pinned IAU SOFA `2023-10-11` release, the
official IERS Conventions 2010 baseline and IERS product documentation, official CDS
and ESA catalogue documentation, and the locked Astropy/PyERFA reference environment.
Those sources define models, fields, and routine semantics. They do not choose UFUQ's
observer, catalogue, operating dates, operational artifacts, implementation, or
tolerances.

Project decisions below remain project decisions even when an authoritative source
supplies their available options. Library defaults never become profile policy.

## Candidate ScientificProfileV1

| Boundary | Candidate V1 contract | Gate state |
|---|---|---|
| Profile identity | Every request and result carries `ScientificProfileV1` plus the exact algorithm/model/ephemeris, source-artifact, observer-preset, leap, EOP, and policy identities, versions, and hashes. | `PROJECT_DECISION`; approval required. |
| Observer | Exactly one immutable preset is accepted. It declares geodetic latitude, east-positive longitude, normalization, datum/reference frame and epoch where applicable, reference ellipsoid, ellipsoidal height, units, uncertainty/accuracy, provenance, and approval. Any other preset or arbitrary coordinate is outside the profile. Internal astronomy types remain observer-generic. | Preset record and reviewer approval missing. |
| Time input | The astronomy boundary accepts only explicit canonical UTC text; there is no default current time. The candidate syntax is the 2C.3 Z-only subset `YYYY-MM-DDTHH:mm:ss[.fraction]Z`. Fractional precision, leap-backed second-`60` validation, earliest/latest instants, endpoint inclusion, and artifact coverage are profile fields rather than hidden parser behavior. | Exact precision, interval, endpoints, and approval missing. |
| Catalogue/data | The runtime artifact contains only the minimal approved numerical ProfileV1 star allowlist selected in 2D. Cultural records reference stable internal `starId` values; a versioned crosswalk maps each `starId` to one or more source-release identifiers. A catalogue may be replaced or coexist without copying coordinates into cultural records. I/311 is the Phase 1 spike source, not the permanent catalogue by default. | Source/release, rights, row eligibility, allowlist, and artifact authority belong to 2D. |
| Normalized astrometry | Every eligible row supplies ICRS frame, right ascension, declination, source epoch label, epoch representation and time scale, proper-motion derivative convention and duration unit, parallax/distance disposition, radial-velocity/perspective disposition, uncertainties/covariance or explicit reviewed omission, quality state, units, and provenance. `UNSPECIFIED` epoch scale, an implicit zero, or a library default is ineligible. | Interface is proposed; exact eligibility branches require profile approval and 2D data. |
| Propagation/model route | Candidate route: eligible normalized ICRS catalogue state -> explicitly declared target-epoch `PropagatedIcrsAstrometry` -> observer-aware CIRS -> explicit Earth-orientation context -> `GeometricHorizontalDirection`. J2000.0 is only a candidate epoch boundary where required by the selected celestial interface; it is not a frame conversion. The production mapping must be pure TypeScript and traceable to the reviewed SOFA semantics. | Normative route, implementation/library mapping, and effect dispositions require AST-003 approval. |
| Earth orientation | Runtime execution is offline against one immutable, hash-addressed leap/EOP bundle. `UT1-UTC`, `xp`, `yp`, and any selected `dX`,`dY` each retain independent provenance, coverage, source quality, availability, and scientific approval. No automatic download, ambient cache discovery, nearest-row substitution, zero substitution, stale acceptance, prediction acceptance, or degraded fallback is permitted. | Exact artifacts/hashes, interpolation, quality acceptance, coverage, expiry, and update policy missing. |
| Output | The only V1 astronomy success state is geometric: north-zero/eastward azimuth when defined, signed geometric altitude, ENU unit direction, singularity state, provenance, warnings, and upstream statuses. `BELOW_GEOMETRIC_HORIZON` remains a classification attached to that valid direction. | Semantic shape proposed; approval and production validation pending. |
| Refraction | Disabled. No atmosphere object is accepted by this profile, no pressure/temperature/humidity/wavelength/lapse default is inserted, and the scene adapter cannot add refraction. | Candidate exclusion requires AST-004/profile approval. |
| Horizon | Geometric altitude zero means only the astronomical local horizontal plane. Physical dip, apparent/refracted altitude zero, terrain, buildings, renderer clipping, and learner cues are not V1 horizon semantics. | Separation is proposed; later policies deferred. |
| Visibility | No aggregate scientific `visible`/`not-visible` result exists. Photometry/variability, daylight/twilight, extinction/transparency, cloud/weather, terrain/obstruction, light pollution, screen presentation, and learner eligibility remain separate unavailable components. | Excluded from V1. |
| Failure behavior | Evaluation fails closed after ordered validation of structure, leap-backed UTC, profile date, preset observer, normalized source state, leap/EOP artifacts, and each required EOP field. Optional/downstream concerns cannot hide an earlier failure or erase a valid geometric state. No degraded result is reachable. | Semantic outcome family, precedence, and warning preservation require final profile approval; wire/HTTP serialization remains a separate contract task. |
| Validation state | Preimplementation evidence permits code only after the remaining profile decisions below are approved. Production results are labelled pending validation until postimplementation comparison and tolerance review succeed. | Explicitly not `APPROVED_GEOMETRIC_RESULT` merely because code executes. |

## Candidate effect disposition

`INCLUDED` below means included in the candidate semantic model. It does not mean that
an algorithm is implemented, a source row is eligible, a numerical omission is
bounded, or a result is scientifically accepted.

| Effect | Candidate V1 disposition | Required preimplementation decision |
|---|---|---|
| Proper motion | `INCLUDED` for an eligible explicit source state. | Approve source-neutral units/rate adapter, polar guard, warning ownership, and missing-state behavior. |
| Parallax/topocentric parallax | `CONDITIONAL`; a row must carry an approved usable-distance state or be rejected for this profile. No implicit infinite-distance substitute. | Approve the normalized eligibility branch; 2D supplies row evidence. |
| Radial velocity/perspective acceleration | `BLOCKED_DECISION`; no zero substitute. | Require an authoritative value or approve a visibly typed unavailable/omission branch for the bounded profile. |
| Frame bias | `INCLUDED`. | Approve production mapping to the SOFA model family. |
| IAU 2006 precession with IAU 2000A nutation | `INCLUDED`. | Approve the matching transformation and supported-date use. |
| Annual aberration | `INCLUDED`. | Approve ephemeris/model ownership and production mapping. |
| Solar gravitational light deflection | `INCLUDED`; extra gravitating bodies are excluded from the V1 candidate. | Approve solar-only scope and record the later validation obligation. |
| Multiple-body light deflection | `EXCLUDED_LATER_EXTENSION`. | No V1 algorithm; omission remains unbounded rather than zero. |
| Earth rotation | `INCLUDED` from UT1/ERA; UTC is never substituted for UT1. | Approve exact leap/EOP policy and mapping. |
| Polar motion | `INCLUDED`; explicit `xp`,`yp` are required. | Approve exact products, per-field status, interpolation, and failure behavior. |
| Observed celestial-pole offsets | Candidate `EXCLUDED_MODEL_CIP_ONLY`; model terms must never be labelled observed-offset corrected. | Approve this explicit V1 disposition or revise the route before code starts. Numerical effect remains unbounded until later evidence. |
| Diurnal aberration | `INCLUDED` exactly once. | Approve observer/context ownership and mapping. |
| Atmospheric refraction | `EXCLUDED_PROFILE_V1`. | Approve geometric-only/no-default boundary; all physical model questions move to a later extension. |

## Exact remaining preimplementation blockers

Only the following items keep Milestone 2C open. They require named astronomy-expert
and supervisor approval; none requires TypeScript output or a numerical tolerance.

1. Approve or revise the candidate profile boundary, typed states, exclusions, and the
   explicit distinction between an executable result and a scientifically accepted
   result.
2. Approve the normative V1 route and production algorithm/library/model/ephemeris
   mapping, including every include/exclude/unavailable effect disposition and the
   source-neutral parallax/radial-velocity/missing-state branches.
3. Approve exactly one preset observer contract and record, including datum/reference
   frame, ellipsoid, ellipsoidal height, coordinate epoch where applicable,
   uncertainty, provenance, and reject-all-other-locations behavior.
4. Approve the exact UTC grammar/precision and one bounded date interval with endpoint
   inclusion and leap-second syntax.
5. Approve the V1 leap/EOP product classes, exact artifact-selection requirements,
   field-by-field quality/availability/interpolation/coverage rules, offline/expiry/
   update policy, and no-degraded-fallback behavior. Actual acquired bytes and hashes
   are a 2D handoff before real execution.
6. Make geometric-only output, disabled refraction, no default atmosphere, and no
   aggregate visibility normative.
7. Approve semantic fail-closed outcomes, validation precedence, singularity behavior,
   warning/status preservation, and the pending-validation result state. Exact wire and
   HTTP codes may follow without changing the science semantics.

No final numerical tolerance, production/reference residual, arbitrary-location
policy, atmosphere model, visibility model, scene behavior, learner policy, or fully
bounded 49-term ledger belongs in this preimplementation list.

## Blocker categories

| Category | Meaning |
|---|---|
| `A BLOCKS_SCIENTIFIC_PROFILE_V1` | The profile's semantic choice or input policy must be explicit before bounded production astronomy starts. A numerical uncertainty attached to that choice may remain unresolved until validation. |
| `B BLOCKS_2D_DATA_AUTHORITY` | Source selection, acquisition, rights, row eligibility, crosswalk, parsing, or artifact authority belongs to 2D/2E. |
| `C POST_IMPLEMENTATION_VALIDATION` | Evidence logically requires production or downstream code and gates scientific acceptance/release, not permission to write that code. |
| `D BLOCKS_LATER_EXTENSION` | The concern applies only to a capability explicitly excluded from V1. |
| `E BLOCKS_LEARNER_FACING_CONTENT` | The concern gates cultural, educational, scenario, or learner-facing claims rather than astronomy-core. |
| `F NOT_REQUIRED_FOR_PROFILE_V1` | The concern is closed for this purpose or belongs to an unrelated future capability. |

## Decision-topic blocker triage

Each row below is one distinct unresolved decision or evidence obligation with one
controlling lifecycle category. A related concern is split into separate rows where its
engine semantics and its source data have different owners.

| Decision or evidence obligation | Primary category | Controlling consequence |
|---|---|---|
| I/311 epoch time scale and exact source instant | `B BLOCKS_2D_DATA_AUTHORITY` | Blocks propagated I/311 rows if 2D retains them; never blocks the source-neutral type boundary. |
| I/311 proper-motion derivative time scale | `B BLOCKS_2D_DATA_AUTHORITY` | Blocks I/311 motion eligibility; the resolved 365.25-day unit does not supply the scale. |
| Source-neutral proper-motion adapter, polar guard, missing-state and warning ownership | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | Must be explicit before the route can be implemented. |
| Radial-velocity source/crossmatch and selected-row evidence | `B BLOCKS_2D_DATA_AUTHORITY` | 2D must supply an authoritative value or mark the row ineligible. |
| Radial-velocity/perspective missing-state branch | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | V1 must reject or use an explicitly reviewed unavailable/omission branch; zero is forbidden. |
| Parallax/distance row quality, uncertainty and covariance | `B BLOCKS_2D_DATA_AUTHORITY` | Controls selected-row eligibility in 2D. |
| Parallax/distance admissibility and unavailable branch | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | The engine must not silently substitute infinite distance. |
| Transformation route, TypeScript mapping and effect ownership | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | The included/excluded/conditional/unavailable matrix must be normative. |
| Leap/EOP product classes, per-field quality/interpolation and offline/fail policy | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | These are scientific runtime semantics required by the profile. |
| Exact operational leap/EOP bytes, hashes, acquisition and deployment authority | `B BLOCKS_2D_DATA_AUTHORITY` | 2D supplies the immutable artifacts after the semantic policy is approved. |
| One preset observer contract and authoritative record | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | Required to define the only accepted V1 location. |
| UTC grammar/precision and bounded supported instants/endpoints | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | Required to define the V1 time domain; no date is invented here. |
| Geometric-only, refraction-disabled and no-default-atmosphere decision | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | The exclusion itself must be approved before code starts. |
| Physical refraction model, meteorology and apparent-horizon domain | `D BLOCKS_LATER_EXTENSION` | Required only if a later profile enables refraction. |
| No aggregate visibility decision | `A BLOCKS_SCIENTIFIC_PROFILE_V1` | V1 must make the absence of a scientific visible/not-visible claim normative. |
| Photometric/daylight/extinction/cloud/terrain/light-pollution visibility model | `D BLOCKS_LATER_EXTENSION` | Required only for a later visibility capability. |
| Multiple presets, global ranges and arbitrary user locations | `D BLOCKS_LATER_EXTENSION` | The architecture remains capable, but V1 accepts only its one preset. |
| Production scene/camera/screen disagreement and scene tolerance | `D BLOCKS_LATER_EXTENSION` | Scene behaviour is excluded from the astronomy profile and cannot redefine astronomy accuracy. |
| Learner interaction and assessment tolerances | `E BLOCKS_LEARNER_FACING_CONTENT` | Needs an approved task/content policy and cannot redefine astronomy accuracy. |
| Arabic/Najdi classification, membership, segments, routes and human review | `E BLOCKS_LEARNER_FACING_CONTENT` | Gates only the affected learner-facing content, never astronomy-core. |
| TypeScript-versus-pinned-reference residuals and regression partitions | `C POST_IMPLEMENTATION_VALIDATION` | Requires production code and gates scientific acceptance, not implementation entry. |
| NOVAS or another lineage-independent positional-astronomy comparison | `C POST_IMPLEMENTATION_VALIDATION` | Stronger evidence follows production; same-family agreement is not promoted. |
| Combined numerical error budget and final scientific tolerance | `C POST_IMPLEMENTATION_VALIDATION` | Remains `FINAL_TOLERANCE_NOT_JUSTIFIED` until evidence and review exist. |
| Kaaba/Qibla target authority | `F NOT_REQUIRED_FOR_PROFILE_V1` | Outside this celestial-position profile. |
| General production runtime JSON-Schema validator | `B BLOCKS_2D_DATA_AUTHORITY` | Belongs to the 2D/2E artifact boundary, not the astronomy route. |

## Contract and AST blocker triage

Every current 2C audit record that is unresolved or could be mistaken for a gate has
one controlling category. Resolved records remain listed to show that they are not
silently reopened.

| Record | Primary category | Controlling roadmap meaning |
|---|---|---|
| `2C-001` | F | State separation is already resolved and carried into V1. |
| `2C-002` | B | I/311 row semantics matter only if 2D selects those rows. |
| `2C-003` | B | I/311 epoch-scale authority controls I/311 eligibility, not a source-neutral engine boundary. |
| `2C-004` | B | Starred-alpha normalization is resolved for I/311; source-row use remains 2D. |
| `2C-005` | F | UTC/TAI/TT/UT1 roles are resolved and carried forward. |
| `2C-006` | F | Sign, horizon, ENU, and singularity conventions are resolved. |
| `2C-007` | A | One preset observer contract/record is required; global ranges and pole support are later. |
| `2C-008` | A | V1 route, mapping, and effect dispositions must be normative. |
| `2C-009` | A | V1 leap/EOP semantics and fail-closed input policy are runtime science inputs; bytes/hashes are acquired in 2D. |
| `2C-010` | D | Refraction model questions move later once geometric-only V1 is approved. |
| `2C-011` | D | Physical/terrain/visibility aggregation is excluded; learner parts are secondarily E. |
| `2C-012` | A | Semantic outcomes, precedence, singularity, warnings, and pending-validation status are required. |
| `2C-013` | C | Numerical error budgets and thresholds govern postimplementation acceptance. |
| `2C-014` | C | Production/reference comparison requires production; the preimplementation protocol/environment already exists. |
| `2C-015` | A | V1 needs one bounded date/observer domain, not global coverage. |
| `AST-001` | B | Catalogue authority, rights, provenance, row quality, and allowlist belong to 2D. |
| `AST-002` | E | Arabic/Najdi names, membership, relationships, and lesson approval do not block astronomy-core. |
| `AST-003` | A | The controlling obligation is profile route/effect/input approval. I/311 is secondary B; residuals/tolerances are secondary C. |
| `AST-004` | A | Approving V1's geometric-only/no-refraction/no-visibility exclusion is the controlling obligation; after that, all remaining model and learner questions are D/E. |
| `AST-005` | F | Kaaba/Qibla target authority is outside this celestial-position profile. |
| `AST-006` | C | The 2C.5C method may be reviewed now; numerical bounds/tolerances are postimplementation acceptance work. |
| `AST-007` | A | Only the one-preset and bounded-UTC subset is A; multiple cities, arbitrary locations, wall-time UX, and learner fixtures are D/E. |

## Source-gap triage

Stable gap IDs are retained even where their existing record bundles more than one
lifecycle obligation. The primary category below controls the roadmap; secondary
relationships prevent loss of the bundled concern.

| Gap | Primary category | Secondary relationship or clarification |
|---|---|---|
| `AST-SRC-001` | F | Closed for the preimplementation synthetic reference boundary; source-derived fixtures are B/C later. |
| `AST-SRC-002` | F | Closed for 2C.1-2C.4 reference design. |
| `AST-SRC-003` | C | The PyERFA patch-document mismatch does not block a TypeScript implementation; it gates later postimplementation reference-validation claims. |
| `AST-SRC-004` | A | Exact acquired EOP/leap bytes and deployment authority are secondary B. |
| `AST-SRC-005` | D | Refraction is excluded from V1. |
| `AST-SRC-006` | A | One bounded interval and endpoints must be approved. |
| `AST-SRC-007` | A | V1 needs explicit UTC/leap semantics; exact acquired bytes are secondary B. |
| `AST-SRC-008` | F | Qibla geodesy is outside this profile. |
| `AST-SRC-009` | B | Controls I/311 eligibility only. |
| `AST-SRC-010` | A | Route/effect selection is A; production comparison and tolerance are C. |
| `AST-SRC-011` | B | Source scale/RV authority is B; the normalized unavailable/omission branch is secondary A. |
| `AST-SRC-012` | A | One preset is required; multiple/global observer support is D. |
| `AST-SRC-013` | D | Learner-facing visibility is secondary E. |
| `AST-SRC-014` | C | Production comparison controls acceptance; source-derived cases are B and nonrequired synthetic work is F/D. |
| `AST-SRC-015` | C | Numerical closure and tolerances are postimplementation; the framework already exists. |
| `DATA-SRC-001` | B | Catalogue acquisition, rights, and row review. |
| `DATA-SRC-002` | B | General production runtime-validator choice belongs to the data boundary. |
| `CULT-SRC-001` | E | Najdi/regional evidence gates only affected cultural claims. |
| `CULT-SRC-002` | E | Rashid al-Khalawi evidence gates only claims that use it. |
| `CULT-SRC-003` | E | Named Arabic/cultural review is learner-content authority. |
| `CULT-SRC-004` | E | Pattern/route evidence is learner-content authority. |

## Error-budget relationship

The 2C.5C evidence remains unchanged: 49 terms, 45
`UNBOUNDED_UNRESOLVED` numerical-bound states, four exact non-numerical guards, all
six tolerance classes `BLOCKED`, and `FINAL_TOLERANCE_NOT_JUSTIFIED`. An A assignment
below means the term's semantic ownership or input disposition must be decided before
implementation. It does not turn the term into a numerical bound or require its
uncertainty to be closed before code starts.

| Primary category | Ledger IDs | Count | Profile interpretation |
|---|---|---:|---|
| A | `A-003`, `A-004`, `B-002`-`B-006`, `B-008`, `B-009`, `C-001`-`C-004`, `C-007`-`C-009`, `D-001`-`D-006` | 22 | Decide included-input/effect/observer/time semantics; their numerical bounds may remain unresolved for later acceptance. |
| B | `A-001`, `A-002`, `A-005`, `A-006`, `B-001` | 5 | Catalogue/source uncertainty and epoch authority move to 2D eligibility. |
| C | `F-001`, `F-005`, `F-006` | 3 | Production floating-point/reference disagreement and production determinism require code. `F-005` includes the code-independent production/reference measurement plus any stronger lineage-independent evidence required by the claim; it does not label Astropy/ERFA agreement independent. `F-006` is already satisfied for Batch evidence transport only. |
| D | `B-007`, `C-005`, `C-006`, `E-001`-`E-007`, `G-001`-`G-003` | 13 | Multiple-body deflection, observed CPO, refraction, and scene/render terms remain explicitly unresolved because the candidate excludes those capabilities. Their dispositions revert to A or C only if a later profile includes them. |
| E | `H-001`-`H-003` | 3 | Scenario, learner-interaction, and scoring tolerances remain outside astronomy accuracy. |
| F | `F-002`-`F-004` | 3 | These exact contract guards are already established for the preimplementation boundary. Future production code must retain them, but no unresolved scientific magnitude or policy is assigned to them. |
| **Total** | `A-001` through `H-003` | **49** | Each stable ID appears exactly once. |

Unresolved terms are never encoded as zero, machine epsilon, test epsilon, display
precision, a library default, or an omitted ledger row. G/H cannot loosen A-F.

## Exit-gate work classes

| Work class | Milestone meaning |
|---|---|
| `PRE_IMPLEMENTATION_SPECIFICATION` | Milestone 2C: approve the bounded profile's inputs, typed states, route/effect ownership, exclusions, fail-closed outcomes, and explicit 2D/postimplementation handoffs. This answers what may be implemented. |
| `POST_IMPLEMENTATION_VERIFICATION` | After TypeScript exists: measure production/reference residuals across the approved profile domain, populate implementation/error evidence, activate `test:reference`, and review numerical acceptance. |
| `LATER_CAPABILITY_APPROVAL` | Before enabling a capability excluded from V1: approve broader locations/dates/effects, refraction, apparent/physical/terrain horizons, visibility/weather/light pollution, scene behavior, or learner policy as applicable. |

The first class closes 2C. The latter two remain mandatory at their own gates but are
not retroactive prerequisites to writing the implementation that supplies their
evidence.

## Evidence lifecycle

### PRE_IMPLEMENTATION

- authoritative model, frame, time, observer, and data-field semantics;
- the approved `ScientificProfileV1` route, inputs, exclusions, and fail-closed states;
- the frozen synthetic exact guards and measurement-only evidence;
- the pinned candidate Astropy/PyERFA reference environment; and
- planned fixtures and comparison metrics.

This stage permits implementation. It does not scientifically accept its output.

### POST_IMPLEMENTATION

- production TypeScript versus pinned reference fixtures;
- implementation residuals for supported dates, observers, source states, effects, and
  boundary outcomes;
- population of implementation terms such as `F-001` and `F-005`;
- activation of `test:reference`; and
- operation-specific error-budget and tolerance review.

### STRONGER_INDEPENDENT_VALIDATION

- evaluate USNO NOVAS 3.1 or another genuinely independent positional-astronomy path;
- pin its software, algorithms, ephemerides, inputs, fixtures, and provenance; and
- compare lineage before calling any agreement independent.

Astropy, PyERFA, ERFA, and SOFA share relevant lineage. Their agreement is useful
consistency evidence but is not this stronger independent stage. NOVAS is a future
candidate, not a prerequisite to writing V1.

## Circular dependencies removed by this audit

| Previous circular statement | Correct lifecycle |
|---|---|
| Production astronomy could not start until 2C closed. | Production may start once the profile-scoped A decisions are approved and 2D/2E supply eligible data. |
| 2C closure required production/reference residuals. | Residuals are POST_IMPLEMENTATION and activate `test:reference`. |
| 2C closure required final scientific/reference tolerances. | Tolerances gate scientific acceptance/release after implementation evidence exists. |
| Every required error-budget term had to be bounded before 2C closed. | Terms stay explicit and unresolved; excluded terms are D, data terms B, implementation terms C, and downstream terms E. |
| Full refraction/visibility/global-location policy blocked the first implementation. | V1 disables/defer these capabilities and preserves typed extension points. |

## Exact Milestone 2C exit criteria

Milestone 2C closes for `ScientificProfileV1` implementation when:

1. the versioned profile names every supported input/state and every excluded
   capability;
2. its normalized astrometric input contract, frames, epochs/scales, units, motion
   conventions, and missing-value branches are explicit;
3. the profile-scoped route/effect ownership and pure-TypeScript mapping are normative;
4. one preset-observer contract and named approved preset record, one UTC/date domain,
   leap/EOP input policy, and offline/fail-closed rules are normative;
5. geometric horizontal output, below-horizon classification, singularity behavior,
   warning/status precedence, and pending-validation status are normative;
6. catalogue acquisition, licensing, row eligibility, source crosswalk, and artifact
   decisions are explicitly handed to 2D and cannot be bypassed;
7. production/reference, error-budget, tolerance, and any applicable
   stronger-independent-oracle obligations are recorded at their postimplementation
   gates; and
8. broader dates/locations, refraction, apparent/physical/terrain horizons, visibility,
   weather/light pollution, scene, and learner policy are explicitly deferred.

Milestone 2C does **not** require TypeScript output, production/reference residuals,
final numerical tolerances, arbitrary-location support, refraction or visibility
implementation, or numerical closure of all 49 ledger terms.

## Multi-location architecture

The initial profile's one-preset restriction is an operating-domain rule, not a
hard-coded astronomy formula. Observer coordinates enter through the same typed
`ObserverInput` used by future profiles. Later validation must partition multiple
approved presets, latitude, longitude, ellipsoidal height, near-equatorial
Polaris/horizon cases, and any eventual arbitrary-location domain. No worldwide range
is claimed here.

## Catalogue and cultural boundaries

Milestone 2D selects the actual catalogue/release, acquisition and deployment rights,
row quality/uncertainty, minimal star allowlist, crosswalk, and artifact provenance.
I/311 remains a studied spike candidate only. A future reviewed Gaia release can
coexist with or replace individual astrometric records through the internal `starId`
crosswalk without changing cultural claims or copying coordinates into them.

Missing Najdi/regional evidence does not block astronomy-core. No content may be
labelled `NAJDI_TRADITION` without claim-level regional evidence and named human
review. Arabic labels, membership, guidance relationships, line segments, and lesson
eligibility remain separate E-category gates.

## Resource status

| Resource | Status | Use and limit |
|---|---|---|
| IAU SOFA `2023-10-11` source/manual | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Current official algorithm/routine authority for preimplementation semantics; does not select UFUQ code or policy. |
| IERS Conventions 2010 / TN36 | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Official registered baseline; corrected working material remains separately classified. |
| Astropy `8.0.1` and locked reference environment | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Candidate reference path only. |
| PyERFA `2.0.1.5` release/source pin | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient for frozen synthetic evidence. Version-matched documentation/tagged-source review and reviewer acceptance remain a later prerequisite for postimplementation reference-validation claims; PyERFA cannot supply the stronger independent oracle. |
| IERS Bulletin A/B/C and `finals2000A` documentation | `OFFICIAL_WEB_SUFFICIENT` | Defines products/fields/quality roles; does not select bytes, accepted qualities, dates, or policy. |
| IANA versioned leap artifacts | `OFFICIAL_WEB_SUFFICIENT` | Candidate machine artifact; IERS Bulletin C remains event authority. |
| CDS I/311 ReadMe/Appendix G/unit standard and ESA I/311 epoch page | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient for known fields and Julian representation, not time scale, rights, row suitability, or permanent source selection. |
| ESA Gaia release documentation/archive | `OFFICIAL_WEB_SUFFICIENT` | Sufficient for 2D candidate evaluation; no Gaia release or subset is selected here. |
| Selected preset-observer geodetic record | `USER_ACTION_REQUIRED_NOW` | Required to close the one-preset V1 contract. |
| I/311 epoch/derivative-scale authority | `USER_ACTION_REQUIRED_BEFORE_2D` | Conditional before 2D can approve propagated I/311 data; it does not prevent 2D from starting or evaluating another source. |
| I/311 raw/derived deployment permission | `USER_ACTION_REQUIRED_BEFORE_2D` | Conditional before 2D can approve deployment of I/311-derived records; it does not prevent 2D from starting. |
| Per-row catalogue acquisition, quality, uncertainty, and covariance evidence | `HUMAN_REVIEW_REQUIRED` | 2D scientific/data review; no new general astronomy book required. |
| Exact production leap/EOP artifacts and activation policy | `HUMAN_REVIEW_REQUIRED` | Official web artifacts exist; project selection and approval remain A/B work. |
| USNO NOVAS 3.1 software and official guides | `REQUIRED_LATER` | Candidate stronger independent oracle after production exists. |
| Replacement Explanatory Supplement PDF | `NOT_NEEDED` | SOFA/IERS already supply the authority needed for this profile. |
| *Fundamental Astronomy*, 6th ed. | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Explanatory support only; cannot override standards or data authority. |
| Najdi/regional claim source | `USER_ACTION_REQUIRED_BEFORE_PHASE2` | Conditional on making a Najdi learner-facing claim; does not block astronomy-core. |
| Rashid al-Khalawi critical edition/treatment | `USER_ACTION_REQUIRED_BEFORE_PHASE2` | Conditional on using that material. |
| Named Arabic/cultural/education review | `HUMAN_REVIEW_REQUIRED` | Learner-facing content only. |
| WCAG 2.2 / WAI-ARIA APG | `OFFICIAL_WEB_SUFFICIENT` | Later UI/accessibility work, not a 2C science resource. |
| Restricted local FYP report | `NOT_NEEDED` | It is not external scientific authority and remains private. |

**Immediate user-action answer:** yes, one item is needed now to close 2C: select the
first physical observer preset and provide or authorize retrieval of its authoritative
geodetic site record. No new astronomy standards PDF, positional-astronomy manual,
replacement SOFA/IERS document, or NOVAS package is needed now.

### USER_ACTION_REQUIRED: selected observer preset

- **Project choice required:** nominate and approve the physical site that V1 will use;
  the geodetic record must refer to that exact site rather than a nearby city centroid.
- **Exact resource:** an official JUPEM GPS-control/MyRTKnet station record or a
  licensed survey record for the physical site selected as the first preset.
- **Why:** V1 needs latitude, east-positive longitude, ellipsoidal height,
  datum/reference frame, reference ellipsoid, coordinate epoch where applicable,
  uncertainty/accuracy, source identity, and acquisition date/version. Orthometric
  height alone is insufficient without a separately evidenced geoid conversion.
- **Acceptable source:** official JUPEM product/service output or an equivalently
  authoritative licensed survey tied to the named site. An official Malaysian Falak
  facility record is sufficient only if it supplies every required geodetic field, or
  is paired with authoritative survey evidence that does.
- **PDF/download actually needed:** no particular file format is required; an official
  web/download record is sufficient if it exposes every required site-specific field.
- **Suggested path:**
  `local-reference/astronomy/observers/<preset-id>/jupem-geodetic-site-record.<original-extension>`.
- **Blocks:** remaining 2C profile approval and first real ProfileV1 execution.
- **Web substitution:** yes, only if an official JUPEM page/download exposes every
  required field for the exact site.

### USER_ACTION_REQUIRED_BEFORE_2D: I/311 time-scale clarification

This action is conditional before 2D can approve propagated I/311 data; it does not
prevent 2D from beginning or choosing another source.

- **Exact resource:** Floor van Leeuwen, *Hipparcos, the New Reduction of the Raw
  Data*, 1st ed., ASSL 350, Springer (2007), DOI
  `10.1007/978-1-4020-6342-8`, specifically an explicit new-reduction catalogue epoch
  and proper-motion independent-time-variable statement; if absent, an official
  written clarification from CDS, ESA, or the catalogue author.
- **Why:** existing I/311/ESA evidence establishes `J1991.25` but not TT/TDB/UTC or an
  exact instant/derivative scale.
- **Acceptable source:** the cited first-edition book if it contains an explicit
  I/311-applicable statement, or an official CDS/ESA/author clarification.
- **PDF/download actually needed:** conditional. Obtain the book/official chapter only
  if I/311 remains a 2D candidate and official web evidence still lacks the statement;
  an authoritative written web/email clarification substitutes.
- **Suggested path:**
  `local-reference/catalogues/hipparcos-i311/authority/van-leeuwen-2007-new-reduction.pdf`
  or
  `local-reference/catalogues/hipparcos-i311/authority/i311-epoch-timescale-clarification.eml`.
- **Blocks:** I/311 eligibility in 2D, not the source-neutral engine interface.
- **Web substitution:** only an official I/311-applicable statement; original-1997 TT
  wording is not sufficient.

### USER_ACTION_REQUIRED_BEFORE_2D: I/311 deployment rights

This action is conditional before 2D can approve deployment of I/311-derived data; it
does not prevent 2D from beginning or choosing another source.

- **Exact resource:** a catalogue-specific official licence/rights statement or written
  CDS/data-origin permission covering the intended raw, normalized, and derived subset.
- **Why:** general VizieR scientific-use rules do not prove redistribution permission.
- **Acceptable source:** versioned official catalogue licence or written rights-holder
  clarification.
- **PDF/download actually needed:** no; a versioned official web licence or retained
  written permission is sufficient.
- **Suggested path:**
  `local-reference/catalogues/hipparcos-i311/licensing/redistribution-clarification.eml`.
- **Blocks:** 2D authorization for tracked/deployed I/311-derived artifacts.
- **Web substitution:** yes, if a versioned official catalogue-specific licence covers
  the intended use.

### USER_ACTION_REQUIRED_BEFORE_PHASE2: Najdi evidence

This action is conditional on the first lesson making a Najdi/regional claim.

- **Exact resource:** a citable Najdi/regional primary source or peer-reviewed
  scholarly treatment with the exact claim, passage pointer, period, and geography;
  for Rashid al-Khalawi, a verified critical edition or scholarly treatment tied to a
  manuscript/edition.
- **Why:** current general Arabic, Old Arabian, and Greco-Arabic sources do not prove a
  specifically Najdi classification.
- **Acceptable source:** a specified scholarly edition, regional primary source, or
  peer-reviewed study with claim-level passage, period, and geography; general web
  summaries are not acceptable.
- **PDF/download actually needed:** only if the first lesson makes the affected claim
  and no stable official academic/publisher/repository full text is available. The
  resource need not be PDF if the authoritative edition is available in another
  citable form.
- **Suggested path:**
  `local-reference/cultural-astronomy/najdi/<author-year-short-title>.pdf` or
  `local-reference/cultural-astronomy/najdi/rashid-al-khalawi/<edition-or-study>.pdf`.
- **Blocks:** only the affected `NAJDI_TRADITION` label and learner-facing claim.
- **Web substitution:** only stable official academic/publisher/repository full text
  with claim-level pointers; general web pages cannot substitute.

No new standards PDF or general positional-astronomy manual is required now.

## Corrected roadmap

```text
2C.6 profile contract and exit-gate approval
  -> 2D catalogue/source, acquisition, rights, row, crosswalk, and operational-data authority
  -> 2E parser, runtime validation, and deterministic generated data
  -> first bounded pure-TypeScript astronomy implementation
  -> production/reference comparison and test:reference activation
  -> stronger independent-oracle evaluation where required by the claimed release boundary
  -> error-budget population and numerical tolerance approval when justified
  -> later date/location, refraction, horizon, visibility, scene, and learner expansions
```

A failed postimplementation comparison can block scientific acceptance/release and
force implementation or profile revision. It is not retroactively a prerequisite to
starting the implementation that produces the evidence.
