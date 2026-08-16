# Astronomy and Qibla specification

## Safety rule

This specification separates fixed conventions from unresolved domain choices. No implementation may fill a **MANUAL DOMAIN DECISION** with a convenient constant. Approved values must name authority, version/date, units, uncertainty or tolerance, and reviewer.

## Convention register

| Topic | Required policy | Class/status |
|---|---|---|
| Catalogue/version | The author-replacement files dated 2008-09-16 for CDS/VizieR I/311, *Hipparcos, the New Reduction*, remain the Phase 1 local-spike source only. Milestone 2D.1 identifies ESA Gaia DR3 version 1.1 `gaiadr3.gaia_source` as the preferred single-source-first production candidate, not an active authority. Milestone 2D.1B's exact fixed-release ADQL and hash-bound ignored official TAP responses verify 8/19 technical HIP matches, five rows with both RV/error fields, and no `HIP 11767` crossmatch, but approve no row. The TCB-to-TDB analytic adapter and immutable query-evidence gates are closed; catalogue activation remains blocked on physical-component/quality/systematics/RV-proxy review, an exact Polaris fallback, and exact derived-artifact rights interpretation. Raw/query-derived material remains local and ignored until approved. | `CATALOGUE_AUTHORITY_BLOCKED`; adapter A and query gate B closed, Gaia DR3 source rows and deployment rights still 2D |
| Catalogue identifier | Numerical rows carry a stable opaque `starId` plus physical `SYSTEM`/`COMPONENT` scope, versioned source-release/table/row/component records, identity/crossmatch evidence, and independent per-field authority. HIP and Gaia IDs remain losslessly serialized release/source keys rather than cultural/domain primary keys; 64-bit Gaia IDs are opaque decimal strings, never JSON numbers. The exact 19-HIP list is a technical query/review candidate, not approved source eligibility or historical membership; a Gaia crossmatch never promotes a row automatically. | SCIENTIFICPROFILEV1/2D CONTRACT; crosswalk normative, records and rows blocked pending approval |
| Reference frame | Carry the selected source's declared ICRS frame explicitly. V1 normatively maps eligible ICRS astrometry through the pinned SOFA `2023-10-11`-derived CIO route; postimplementation reference/lineage-audited validation still gates approval. The I/311 spike declares ICRS but does not become the permanent source. | SOURCE-DEFINED INPUT; production route `PROJECT_DECISION`; concrete source/rows 2D |
| Catalogue reference epoch | Every source-neutral row carries the selected release's declared epoch representation and time scale. Gaia DR3 declares native `J2016.0 TCB`, exactly `JD(TCB) 2457389.0`. Rule `GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1` converts the same event with IAU B3 into two-part `JD(TDB)` and retains both states; it never relabels the Julian-year text or treats conversion as propagation. For the I/311 spike, carry literal `Ep=1991.25` separately: ESA Gaia DR1 establishes only its Julian `J1991.25` representation, not an I/311-applicable time scale. Never transfer the original catalogue's `J1991.25(TT)` or let a library default decide a missing scale. | Gaia/IAU relation `SOURCE_SUPPORTED_FACT`; exact compatible adapter `PROJECT_DECISION` closed; source-row approval still 2D; I/311 time scale `AUTHORITY_OR_EVIDENCE_MISSING` / `HUMAN_REVIEW_REQUIRED` |
| Space motion | Source `mu_alpha_star = (d alpha / dt) cos(delta)`, Dec motion, derivative time coordinate/unit, positive approved parallax/equivalent distance, and finite approved RV must all be explicit. For Gaia DR3, the approved compatible map preserves ICRS direction; multiplies `pmra`, `pmdec`, and catalogue parallax by `K_B = 1/(1-L_B)`; multiplies coordinate distance by `1-L_B`; maps five-parameter covariance with `D_5=diag(1,1,K_B,K_B,K_B)` and six-parameter-solution covariance with `D_6=diag(1,1,K_B,K_B,K_B,1)`, leaving pseudocolour unchanged; and preserves the spectroscopic RV/error numbers without compatible scaling or kinematic relabelling. A row/component review must still approve an explicit RV propagation proxy, systematics, covariance applicability and quality. Missing astrometry-RV cross-covariance is `UNKNOWN_NOT_PROVIDED`, never zero. I/311 Appendix G Table G.3 independently defines `pmRA` as starred alpha but does not close its time-scale or RV gaps. The selected SOFA-derived boundary converts starred-alpha to coordinate rate only away from the exact pole and fails closed on missing/unapproved state. | Compatible map `SOURCE_SUPPORTED_FACT` plus normative `PROJECT_DECISION`; Gaia row/RV-proxy and I/311 authority `BLOCKS_2D_DATA_AUTHORITY`; numerical acceptance postimplementation |
| Apparent-place effects | V1 normatively uses a decomposed UFUQ-owned pure-TypeScript subset derived from SOFA `2023-10-11`: source-to-`JD(TDB) 2451545.0` propagation, explicit `epv00` Earth/Sun model, IAU 2006 precession with IAU 2000A nutation and matching CIO transformation, observer-aware CIRS, ERA/`xp`/`yp` Earth-orientation context, and geometric `atioq`-derived output. Included: frame bias, precession, nutation, annual aberration, solar deflection, Earth rotation, polar motion, diurnal aberration, full motion/parallax/RV. Omitted/deferred: observed `dX`,`dY`, extra-body deflection, refraction. Omission terms remain unbounded. | NORMATIVE V1 `PROJECT_DECISION`; leap/EOP semantics are fixed below, exact artifacts/configuration are 2D/2E, and residuals/tolerances are postimplementation |
| Time input | ScientificProfileV1 normatively narrows RFC 3339 to whole-second `YYYY-MM-DDTHH:mm:ssZ`: fixed-width valid Gregorian fields, uppercase `T`/`Z`, no fraction, numeric offset, `-00:00`, wall time, Unix timestamp, bare JD, or implicit current time. Second `60` is structurally eligible only as `23:59:60Z` and becomes a validated UTC instant only when the approved leap artifact confirms that exact positive-leap date. Whole-second serialization is not scientific accuracy or permission to truncate. Local/IANA time and “now” resolve upstream into an immutable UTC `ScenarioSnapshot` with provenance. | RFC 3339/SOFA/IERS roles `SOURCE_SUPPORTED_FACT`; narrowed grammar/state and leap-validation boundary normative `PROJECT_DECISION`; concrete leap artifact remains 2D |
| Earth time/orientation | UTC is external; TAI/TT/UT1 remain typed internally and route-scoped TDB epochs are explicit. V1 requires approved leap state plus independent approved `FINAL` `UT1-UTC`,`xp`,`yp`. It selects Gazette 13's four-point example/full support, leap-aware `UT1-TAI`, and exactly-once IERS Conventions 2010 ocean-tide/applicable-libration restoration after interpolation, all from one explicitly supplied immutable offline bundle. Observed `dX`,`dY` and LOD are `NOT_REQUIRED_BY_PROFILE_V1`, not zero or hidden inputs. Acquisition age, publisher validity, field coverage, quality and approval remain separate; no nearest/extrapolated/degraded fallback exists. | Normative `PROJECT_DECISION` under AST-003/007; equivalent methods are source-permitted but not V1-approved; exact artifacts/hashes/restoration configuration and dates are `BLOCKS_2D_DATA_AUTHORITY`; uncertainty/tolerances remain postimplementation |
| Observer Earth model | `ObserverPreset` requires a stable ID/site identity; finite north-positive geodetic latitude; east-positive longitude canonically in `[-180 deg,+180 deg)`; explicit datum/frame/realization, ellipsoid, typed height/reference surface, conditional coordinate epoch, accuracy state, provenance, data/artifact version, availability, validation, and approval. V1 selects only `umpsa-pekan-faculty-of-computing`, identifying Faculty of Computing, UMPSA Pekan Campus, Pahang, Malaysia. No browser geolocation, `(0,0)`, WGS 84, zero height, map pin, height conversion, or zero uncertainty is inferred. | Contract/site identity `PROJECT_DECISION` for 2C; exact values/source/accuracy/artifact `BLOCKS_2D_DATA_AUTHORITY`; polar/multiple/global domains remain later |
| Longitude | Degrees east are positive; west is negative. Latitude north is positive. | CLARIFIED |
| Sidereal time | ScientificProfileV1 uses the CIO/ERA route and does not need GAST or local apparent sidereal time as a transformation input. The supporting relation `LAST = normalize24(GAST + longitudeEast/15)` hours remains valid for a separately approved equinox-based output/adapter, but must not be mixed into the V1 CIO route. | V1 CIO/ERA route `PROJECT_DECISION`; optional sidereal display later |
| Hour angle | `H = normalizeSigned(LST - RA)` with west-positive hour angle. | CONFIRMED |
| Azimuth | Degrees/radians clockwise from geographic True North: north 0°, east 90°, south 180°, west 270°. | CONFIRMED |
| Three.js axes | `+Y` zenith/up, `-Z` north, `+X` east. | CONFIRMED |
| Refraction | ScientificProfileV1 normatively requests no refraction, accepts/creates no atmosphere input, inserts no pressure/temperature/humidity/wavelength/height-transfer/lapse default, and emits no refracted coordinate. `REFRACTION_NOT_REQUESTED` is distinct from later `REFRACTION_UNAVAILABLE`. Future refraction is a separate immutable stage requiring explicit provenance-bearing inputs and approved model/domain/warnings. Astropy defaults are reference-library behavior only. | V1 exclusion/no-default `PROJECT_DECISION` normative; later model/ranges/warnings `HUMAN_REVIEW_REQUIRED` / `AUTHORITY_OR_EVIDENCE_MISSING` under AST-004/006 |
| Below horizon | `BELOW_GEOMETRIC_HORIZON` is an attached classification, not a terminal failure or replacement for `GeometricHorizontalDirection`. It preserves signed altitude, azimuth when defined, exact singularity state, normalized ENU direction, provenance, warnings, statuses, and validation state. Geometric horizon means the astronomical local horizontal plane at geometric altitude zero before refraction; it is not visible/apparent horizon, sea/Earth-curvature or observer-height dip, terrain/buildings, clipping, or a learner cue. | V1 separation/result retention `PROJECT_DECISION` normative; numerical near-boundary/physical-dip/terrain/downstream policy remains later |
| Magnitude/visibility | ScientificProfileV1 emits no aggregate scientific `visible` boolean. Keep astronomical horizon; approved-band photometry/variability; Sun altitude/daylight/twilight; atmospheric extinction/transparency; cloud/weather; terrain/obstruction; light pollution; screen presentation; and learner eligibility as independent future components. No component promotes another. A geometric or rendered star is not thereby scientifically visible, and learner eligibility is not inferred. | V1 exclusion/separation `PROJECT_DECISION` normative; later component rules `AUTHORITY_OR_EVIDENCE_MISSING` / `HUMAN_REVIEW_REQUIRED` under AST-001/004/006/007 |
| Qibla model | Initial great-circle bearing on a sphere, clockwise from True North and normalized to `[0,360)`. | CONFIRMED/CLARIFIED |
| Kaaba coordinate | No coordinate is approved here; record authority, datum, order/sign, precision, version/date, uncertainty, and the convention-compatible Malaysian/domain validation method. | MANUAL DOMAIN DECISION AST-005 |
| Angular comparison | Use robust unit-vector separation; use wrapped circular difference for headings. | CLARIFIED |
| Numerical tolerances | Milestone 2C.5C defines separate source, model, Earth-orientation/time, observer, atmosphere, numerical-implementation, scene, and learner/assessment budget layers; a boundary-specific metric hierarchy; and candidate worst-case/covariance/RSS combination rules. RSS is prohibited without justified independence, an unbounded required term leaves the combined budget unbounded, and scene/learner tolerances cannot weaken astronomy accuracy. All six tolerance classes remain blocked with no numerical value. | `CANDIDATE_TOLERANCE_PROPOSAL` for method only; `FINAL_TOLERANCE_NOT_JUSTIFIED` / MANUAL DOMAIN DECISION AST-006 for every numerical threshold |
| Reference and independent validation | The locked synthetic-only Astropy tool proves the environment, neutral-envelope, offline, and production-import boundaries. Production is now the separate UFUQ-owned SOFA `2023-10-11`-derived TypeScript subset; Astropy/PyERFA remains reference-only. This is code/dependency independence but shared scientific lineage. Batch 01 remains 9/9 bounded synthetic scopes, 24 exact passes/0 fails and 27 `MEASURED_NO_ACCEPTANCE` records. Postimplementation ProfileV1 acceptance needs multi-date, selected-source, one-preset-domain, EOP-boundary and production/reference partitions. A lineage-audited NOVAS or other oracle remains the stronger independent stage where required. | Production/reference boundary and production mapping established; source/data, PyERFA patch-doc acceptance, residuals, any required stronger-independent comparison, bounded terms, thresholds, and reviewer approval remain later |

## ScientificProfileV1 lifecycle boundary

The normative contract in `spikes/PHASE1_SCIENTIFIC_PROFILE_V1.md` narrows real V1 execution to
one selected preset identity instantiated by a 2D-approved observer artifact, one
bounded explicit-UTC domain carried by a versioned `SupportedTimeDomain`, one
2D-approved minimal star artifact, an explicit source-neutral astrometric input, an
approved route/effect disposition, immutable offline leap/EOP inputs, and geometric
horizontal output. Refraction and aggregate visibility are disabled. Internal types
remain multi-location and multi-source capable; no global operating domain is implied.

The generic `ObserverPreset` types, validators, no-default branches, and observer-
generic transformation interfaces may be implemented before 2D supplies the numerical
UMPSA artifact. Missing or unapproved observer data blocks real V1 evaluation, not that
contract implementation.

Authoritative semantics, approved profile decisions, frozen synthetic guards, and the
pinned reference environment are `PRE_IMPLEMENTATION` evidence. TypeScript/reference
residuals, supported-domain partitions, implementation error, and numerical tolerance
approval are `POST_IMPLEMENTATION` evidence. USNO NOVAS or another genuinely
independent positional-astronomy path is a later
`STRONGER_INDEPENDENT_VALIDATION` candidate; shared Astropy/PyERFA/ERFA/SOFA lineage
does not satisfy that stage.

An implementation may emit `GEOMETRIC_RESULT_PENDING_VALIDATION` after the remaining
profile and data gates open. It may not emit `APPROVED_GEOMETRIC_RESULT` until the exact
implementation/profile/data combination passes postimplementation production/reference
partitions, error-budget/tolerance review, and named scientific approval.

The V1 scientific outcome taxonomy distinguishes invalid supplied input, missing
required input, unavailable required artifacts, unsupported profile/domain, required
state/data without scientific approval, scientific execution failure, and a successful
pending-validation geometric result. Azimuth singularity and
`BELOW_GEOMETRIC_HORIZON` attach to a valid result; optional-stage-not-requested states
cannot erase it. These are semantic domain classes, not finalized JSON/HTTP codes.

At exact zenith or nadir the horizontal ENU projection is zero: altitude and normalized
ENU remain valid while azimuth is `UNDEFINED_SINGULAR`. A near-singular
`ILL_CONDITIONED` state requires a separately reviewed numerical/domain boundary; no
epsilon, display precision, or test tolerance is selected here.

Underlying scientific warnings and raw statuses are preserved with their producing
stage/routine/model and provenance. They are neither silently downgraded to success nor
automatically treated as scientific rejection; the approved route/data policy decides
their result disposition. Scientific status is separate from HTTP transport, logging,
and log severity.

## Canonical value objects

Every public value carries units and convention in its type or field name. Distinct
conceptual types prevent accidental double propagation or frame mixing:

- `SuppliedCanonicalUtcText{canonicalUtcText,parsedGregorianFields}` followed only
  after artifact-backed validation by
  `ValidatedUtcInstant{canonicalUtcText,leapArtifactIdentity,validationStatus}`;
- internal `UtcQuasiJulianDate`, `TaiTwoPartJulianDate`, `TtTwoPartJulianDate`,
  route-scoped `TdbTwoPartJulianDate`, and `Ut1TwoPartJulianDate` values, each labelled by scale and the
  `MJD_ZERO_PLUS_OFFSET` split; UT1 additionally retains exact `UT1-UTC` field and EOP
  provenance, while TDB source/target epochs retain their conversion provenance;
- `TimeConversionEvidence{sourceState,destinationState,routineAndVersion,
  leapAndEopIdentities,warnings,statuses}`;
- `ObserverPreset{schemaVersion,presetId,siteIdentity,referencePointDescription,
  geodeticLatitude,geodeticLongitude,referenceSystem,referenceEllipsoidId,
  coordinateReferenceEpoch,height,heightConversion,coordinateAccuracy,provenance,
  dataVersionId,artifactIdentity,artifactAvailability,validationStatus,
  scientificApproval}`;
- `GaiaDr3NativeTcbAstrometry{sourceRelease,sourceTable,sourceRowAndComponent,
  sourceValues,sourceUnits,sourceParameterOrderAndBasis,sourceErrorsAndCorrelations,
  sourceCovariance,sourceEpochLabel,sourceEpochJd,sourceTimeScale,
  sourceCompatibleSystem,spectroscopicRadialVelocityMeasure,sourceQuality,
  warnings,statuses,approval}` remains immutable source evidence;
- `CompatibleQuantityNormalizationEvidence{normalizationRuleId,adapterVersion,
  sourceAndTargetEpochStates,sourceAndTargetCompatibleSystems,authorityIds,
  exactConstantsAndExpressions,fieldTransformations,parameterOrderAndBasis,
  nativeCovarianceIdentity,jacobian,targetCovarianceIdentity,rvDisposition,
  inputAndOutputHashes,warnings,statuses,reviewAndApproval,oneTimeNormalizationMarker}`;
- `CatalogueIcrsState{raDeg,decDeg,nativeSourceEpochEvidenceId,
  normalizedSourceEpochTwoPartJd,normalizedEpochScale,
  properMotionRaCosDec,properMotionDec,derivativeScale,
  approvedPositiveParallax,approvedPropagationRadialVelocity,uncertainties,covariance,
  sourceAndApprovalProvenance,compatibleSystem,normalizationEvidenceId,...}`; Gaia
  input may enter this source-neutral TDB-compatible state only through
  `GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1`; mixed, missing, repeated, or unapproved
  normalization fails closed;
- `PropagatedIcrsAstrometry{raDeg,decDeg,targetEpochLabel,targetInstant,
  targetTimeScale,spaceMotionPolicy,warnings,...}`; the type records a successful
  declared target epoch/instant and does not itself promise J2000.0 or a frame
  transformation;
- `ObserverAwareCirsDirection{raDeg,decDeg,observationInstant,observerPolicy,
  celestialModel,...}`;
- `EopArtifactState{artifactId,version,hash,availability,integrity,publisherValidity,
  acquisitionIdentity,activationState}` plus independent
  `EopFieldState{field,value,unit,requestedUtcInstant,sourceQuality,sourceDeclaredUncertainty,fieldCoverage,
  sourceProductAndSeries,artifactAndSampleProvenance,interpolationEvidence,
  scientificApproval,rawAndNormalizedStatuses}` records for required `UT1-UTC`, `xp`, `yp`; later
  `dX`, `dY` records remain separate but are `NOT_REQUIRED_BY_PROFILE_V1`;
- `EarthOrientationContext{utc,tai,tt,ut1,era,eopArtifactState,eopFieldStates,
  celestialPoleOffsetPolicy,leapArtifactState,...}`;
- `GeometricHorizontalDirection{azimuthNorthEastDeg,geometricAltitudeDeg,
  enuDirection,observationInstant,observerPolicy,eopPolicy,singularityStatus,...}`;
- `RefractedHorizontalDirection{azimuthNorthEastDeg,refractedAltitudeDeg,
  sourceGeometricDirection,refractionPolicy,atmosphereObservation,modelInputs,
  validityStatus,warnings,...}`;
- `AtmosphereObservation{pressureHpa,groundTemperatureC,
  relativeHumidityFraction,observationWavelengthMicrometres,measurementInstant,
  measurementLocation,sourceProvenance,uncertainty,measuredOrDerivedStatus,
  derivationModelAndVersion,heightOrLapseAssumptions,validationStatus}`;
- separate `GeometricHorizonState`, `RefractedApparentHorizonState`,
  `PhysicalHorizonDipState`, `TerrainObstructionHorizonState`, `SceneClipState`, and
  `LearnerHorizonCueState` records;
- a componentized `VisibilityState` retaining independent astronomical-horizon,
  photometric/variability, Sun-altitude/daylight/twilight, atmospheric-extinction/
  transparency, cloud/weather, terrain/obstruction, light-pollution, screen, and
  learner-eligibility states and their policy/provenance/availability; and
- a separate `SceneDirection` that retains its upstream state/policy identifiers and
  applies no scientific correction;
- `EnuUnitVector{east,north,up}` and `BearingNorthEastDeg`.

`RefractedApparentHorizonState` means only comparison of an approved refracted
direction with apparent altitude zero under its named model/policy. Apparent altitude
zero is not geometric altitude zero, a visible skyline, terrain/building horizon,
physical horizon dip, or a SOFA/ERFA numerical guard. Each alternative requires its
own reviewed state and policy.

Reject non-finite values and out-of-range latitude. Observer longitude is east-positive
and canonically serialized in `[-180 deg,+180 deg)`, with `+180 deg` represented as
`-180 deg`; other angle-wrap decisions remain explicit so serialization and equality do
not disagree. The exact UMPSA reference point, numerical coordinates, Earth model,
height, accuracy and artifact provenance are 2D data and are not invented by this
specification.

The normative core outcome taxonomy separates invalid input, missing required input,
unavailable required artifacts, unsupported profile/domain, required state/data
without scientific approval, and scientific execution failure. Time refinements are
`TIMESTAMP_SYNTAX_INVALID`, `LEAP_SECOND_INSTANT_INVALID`,
`LEAP_VALIDATION_DATA_UNAVAILABLE`, `REQUIRED_TIME_SCALE_UNAVAILABLE`,
`EOP_FIELD_UNAVAILABLE`, `EOP_ARTIFACT_INTEGRITY_FAILURE`, `EOP_OUT_OF_RANGE`,
`EOP_INTERPOLATION_SUPPORT_UNAVAILABLE`, `LEAP_SECOND_DATA_EXPIRED_FOR_REQUEST`,
`TIME_OUTSIDE_SUPPORTED_DOMAIN`, `TIME_OR_EOP_STATE_NOT_APPROVED`, and
`TIME_CONVERSION_WARNING`. Source quality, byte integrity, field support, publisher
validity and scientific approval remain distinct.
Semantic evaluation proceeds through supplied-value validation, missing inputs,
artifact availability/integrity, domain, approval, scientific execution, result
creation, attached classifications, and excluded optional-stage states. Exact wire
codes remain under review. A valid geometric result carries an explicit pending-or-
approved validation state. The name
`APPROVED_GEOMETRIC_RESULT` is reserved until postimplementation production/reference,
error-budget/tolerance, and named-review gates pass. A
degraded result is reserved and unreachable until a named degraded mode, quantitative
bound, warning contract, and reviewer approval exist.

After a valid geometric direction exists, attach azimuth/singularity and geometric-
horizon classifications without erasing the result, then attach V1's
`REFRACTION_NOT_REQUESTED` and profile-excluded visibility-stage states. Core invalid,
missing, unavailable, unsupported, unapproved, or execution-failure outcomes always
precede these classifications. Later-profile semantic outcomes include
`APPROVED_REFRACTED_RESULT`, `REFRACTION_UNAVAILABLE`,
`REFRACTION_INPUT_INVALID`, `REFRACTION_OUTSIDE_VALID_DOMAIN`, and
`VISIBILITY_POLICY_UNAVAILABLE`; they are unreachable in V1 and their exact wire/HTTP
forms remain unapproved. `APPROVED_REFRACTED_RESULT` remains unreachable until its exact
model/version, complete meteorology/provenance, validity and combined supported
operating domains, warning policy, scientific tolerance, and named astronomy-review
approval exist. `BELOW_GEOMETRIC_HORIZON` attaches to and retains the valid geometric
result rather than replacing it.

The supported input domain is the intersection of the approved catalogue-propagation,
model/ephemeris, leap, per-field EOP, observer, and scenario domains. A later
validation/tolerance gate evaluates results over that domain; a nonexistent tolerance
domain must not prevent the input domain from being specified. No numerical date,
location, or height endpoints are approved by this specification.

The Milestone 2C.5C error-budget framework is recorded in
`spikes/PHASE1_SCIENTIFIC_ERROR_BUDGET.md` and its machine-checkable AST-006 ledger.
Layers A-F form the future astronomy scientific budget. Scene/render layer G and
downstream scenario/learner/assessment layer H remain separate. Scenario generation is
an independent downstream policy term in that layer, not learner uncertainty.
Catalogue/source, model, operational data,
observer, atmosphere, and production implementation terms are currently
`UNBOUNDED_UNRESOLVED`; exact Batch 01 guards have no numerical contribution.

Internal computation uses radians and double-precision JavaScript numbers. Serialization uses named degree fields; never serialize an unlabelled `[a,b]` coordinate pair.

The evidence classification and production-data handoffs are audited in
`spikes/PHASE1_SCIENTIFIC_BEHAVIOUR_CONTRACT.md`. Milestone 2C fixes no new numerical
tolerance and is ready to close for bounded implementation now that the profile-scoped
leap/EOP product-class/quality/interpolation/offline/update semantics are normative.
Exact bytes/configuration remain 2D/2E. AST-006 numerical tolerances and production/
reference experiments remain mandatory postimplementation acceptance work rather than
2C entry conditions.

## Horizontal transformation

For observer latitude `phi`, declination `delta`, and west-positive hour angle `H`, a numerically clear east/north/up formulation is:

```text
east  = -cos(delta) sin(H)
north =  sin(delta) cos(phi) - cos(delta) cos(H) sin(phi)
up    =  sin(delta) sin(phi) + cos(delta) cos(H) cos(phi)

altitude = atan2(up, hypot(east, north))
azimuth  = normalize2pi(atan2(east, north))
```

This is equivalent to the report's spherical-trigonometry intent and directly matches the declared azimuth convention. At the zenith/nadir, azimuth is undefined; code must return a documented singular status and assessment must compare direction vectors rather than arbitrary azimuth.

## Three.js mapping

For radius `r`, geometric altitude `h`, and north-clockwise-east azimuth `A`:

```text
x =  r cos(h) sin(A)   // east
y =  r sin(h)          // up
z = -r cos(h) cos(A)   // north is -Z
```

The report's check `h=30°`, `A=45°`, `r=100` gives approximately `(61.24, 50.00, -61.24)` and is retained as an internal mapping fixture, not an independent astronomy oracle.

## Astrometric pipeline

ScientificProfileV1 normatively selects the following typed dependency graph, aligned
to the pinned SOFA issue. It authorizes implementation but not scientific acceptance:

```mermaid
flowchart LR
  CAT[Eligible CatalogueIcrsState<br/>epoch, motion, positive distance, RV] -->|pmsafe-derived to J2000 TDB interface| PROP[PropagatedIcrsAstrometry]
  PROP --> CIRS[ObserverAwareCirsDirection<br/>atciq-derived, model CIP]
  TIME[Typed UTC/TAI/TT/UT1 + approved leap data] --> EOP[EarthOrientationContext<br/>ERA + required xp/yp; dX/dY omitted]
  OBS[Approved geodetic observer] --> EOP
  EOP --> CIRS
  CIRS --> GEO[GeometricHorizontalDirection<br/>geometric atioq-derived subset]
  EOP --> GEO
  GEO -. later profile .-> REF[RefractedHorizontalDirection]
  GEO -. downstream .-> VIS[Separate VisibilityState]
  GEO -. downstream .-> SCENE[Separate SceneDirection]
```

The production route uses `pmsafe`-derived semantics from an approved source TDB
instant to the declared J2000.0 interface `JD(TDB) 2451545.0`. That is an epoch input
requirement, not an ICRS frame transformation. `mu_alpha_star` is converted to
coordinate rate only away from the exact pole; nonzero propagation status fails V1
closed. Positive approved distance and approved finite radial velocity are mandatory.
I/311-derived rows remain ineligible until 2D resolves their source scale and missing
inputs; that does not block the source-neutral implementation.

Production is a UFUQ-owned pure-TypeScript subset derived from the lower-level SOFA
`2023-10-11` semantics. It exposes the pinned `epv00` Earth/Sun model and status,
declared-ellipsoid `gd2gce` observer conversion, model CIP/CIO, ERA, required
`UT1-UTC`,`xp`,`yp`, topocentric parallax and diurnal aberration exactly once. Observer
velocity carries the diurnal term through the `apcs`/`atciq`-derived aberration context;
the later local `diurab` term is disabled as redundant, matching SOFA `apco`. Observed
`dX`,`dY`, extra-body deflection and refraction are omitted/deferred and remain
unbounded, not zero. The production path skips refraction math rather than creating
weather defaults. Astropy remains reference-only; SOFA/ERFA shared lineage means its
comparison is implementation verification, not stronger independent validation.

If required Earth-orientation data is missing, nonfinal, unapproved, outside its
independent field range, lacks the full four-sample support/restoration configuration,
or fails integrity/validity checks, `ScientificProfileV1` fails explicitly. A later
profile may expose a separately labelled, bounded approximation only after AST-003/006
approval. Runtime scenarios persist the bundle, field/sample, interpolation/model,
policy and status identities. Do not quietly change algorithms between browser,
server, fixture generation, and evaluation.

Polaris/Al-Jady is an instructional cue near the north celestial pole; it is not identical to True North. The system must maintain distinct targets and knowledge components for locating the star and estimating the terrestrial direction.

KC-04 scores a terrestrial True-North bearing/direction defined by the approved task,
not the elevated line of sight to Polaris. KC-05 scores the approved Qibla bearing
relative to that True-North convention. EDU-002 and AST-007 must define how each task
captures these responses without allowing a visual cue or context-star selection rule to
make the answer trivial.

## Qibla bearing

For observer latitude/longitude `(phi, lambda)` and approved Kaaba `(phiK, lambdaK)`, all in radians with east-positive longitude, the initial spherical great-circle bearing is:

```text
deltaLambda = lambdaK - lambda
bearing = normalize2pi(
  atan2(
    sin(deltaLambda),
    cos(phi) * tan(phiK) - sin(phi) * cos(deltaLambda)
  )
)
```

Handle coincident/antipodal degeneracy explicitly. Qibla is compared to the learner's True-North-referenced direction using wrapped circular distance. An ellipsoidal calculation may be used for sensitivity/reference analysis, but changing runtime semantics requires a new proposed deviation.

## Angular comparison

For normalized 3D directions `u` and `v`:

```text
separation = atan2(length(cross(u,v)), dot(u,v))
```

Clamp or normalize only with documented floating-point guards. For two bearings, use:

```text
distance = abs(atan2(sin(a-b), cos(a-b)))
```

Correctness is `distance <= approvedTaskTolerance`; the exact tolerance and inclusive boundary are versioned with the scenario. Near-zenith direction tasks use vector separation, not azimuth difference.

## Validation specification

1. Pin the exact oracle program/commit, Astropy, ERFA, IERS source/file/hash and
   auto-download/extrapolation settings, catalogue snapshot/query, observer Earth model,
   refraction inputs, and all selected policies in a manifest.
2. A reviewer other than the runtime implementer approves the oracle protocol and a
   code-sharing audit. The generator must not import, call, or mechanically translate
   runtime TypeScript. Add policy-level differential cases so two implementations
   cannot agree merely because they share the same wrong convention. Astropy
   high-level transforms and direct PyERFA calls disclose their shared ERFA/SOFA
   lineage and are not independent algorithms for same-family agreement.
3. Before execution, register the experiment's stable ID, scientific question,
   permitted/prohibited claims, input class, exact dependencies and conventions,
   artifacts, partitions, comparison lineage, metrics, repetition/hashes, result
   schema, acceptance mode, reviewer gate, and follow-up decision under the 2C.5A
   protocol. Source-derived and production-generated inputs remain unavailable unless
   their separate gates are open.
4. Generate fixed expected equatorial/horizontal values through the pinned
   code-independent reference process. Preserve the permitted fixed outputs,
   provenance, and shared-lineage disclosure; the production runtime never calls the
   reference tool. This step is not by itself stronger algorithmic independence.
5. Where the claimed release boundary requires stronger independent validation,
   cross-check selected time/sidereal cases against a pinned, precisely identified
   USNO or other lineage-independent artifact. Separately, cross-check Qibla cases
   against the approved convention-compatible Malaysian/domain procedure when Qibla is
   in scope. A contextual web page alone is not a numerical oracle.
6. For V1, include meridian/east/west, angle wrap, UTC day boundary, leap-date and
   approved leap-second input behavior, the approved preset and its uncertainty/domain
   boundaries, horizon/below-horizon, zenith singularity, catalogue reference epoch,
   reference-only high-proper-motion data, and supported-range endpoints. Additional
   Malaysian, equatorial, high-latitude, height, and arbitrary-location partitions gate
   only profiles that claim those domains. These tests do not expand the learner UI
   beyond approved scenarios. Later refraction cases additionally
   retain explicit atmosphere inputs/provenance, geometric and refracted states or
   non-results, model/domain/warnings, geometric versus apparent horizon,
   below-horizon partitions, and independent visibility components; no fixture may
   rely on an unrecorded library default.
7. Produce an error-budget table per case/policy using the 2C.5C ledger terms:
   catalogue position/space-motion uncertainty and covariance, model/omitted-effect
   bounds, per-field EOP/time and observer uncertainty, atmosphere when requested,
   floating-point/production error, and independent-oracle disagreement. Record both
   component and boundary-appropriate vector errors. Use RSS only for justified
   independent random terms; keep systematic/correlated/asymmetric terms explicit.
   Scene and learner quantities remain separate. Release requires every case within
   AST-006; an unresolved required term leaves the case unbounded and no average may
   hide a failed fixture.
8. Separate implementation-numerics tolerances, scientific/reference tolerances, and
   learner-answer tolerances. Until AST-006 approves them, numerical acceptance
   assertions remain inactive/fail closed as unconfigured rather than use a convenient
   constant. Postimplementation comparison must still run and emit
   `MEASURED_NO_ACCEPTANCE` so the evidence needed to propose a threshold can exist;
   only exact supported invariants can pass or fail before then.

Milestone 2C.5B Batch 01 satisfies only the registration/execution-shape prerequisite
in item 3 and the exact/measurement separation in item 8. It supplies code-separation
and shared-lineage evidence toward item 2, but the required independent reviewer
approval and policy-level differential cases remain open. It imports no production
astronomy, uses no source-derived values, and therefore cannot satisfy items 4-7 as a
production/reference correctness claim or activate `test:reference`.

Milestone 2C.5C interprets those committed results without regenerating canonical
evidence or changing a hashed Batch input: all 27 records remain measured values
without acceptance, and the 24 exact passes retire only
bounded synthetic mutation/state-contract classes. No serialized zero, same-family
agreement, hash identity, or deterministic replay supplies an implementation or
scientific tolerance.

Astropy documents its ERFA-based refraction as inaccurate below about 5 degrees and
warns of meaningless or highly discrepant behavior near/below zero altitude in
affected cases. These are source-supported reference-library limitations and
experiment partitions, not UFUQ validity thresholds or tolerances. USNO's online
material is a validation reference, not a runtime service dependency.
