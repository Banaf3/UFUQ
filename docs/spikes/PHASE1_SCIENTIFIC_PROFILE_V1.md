# Phase 1 Milestone 2C.6: ScientificProfileV1 exit-gate audit

## Status and decision

- **Profile:** `ScientificProfileV1`
- **Profile state:** normative for boundary/output/outcome and UTC/time-domain contract
  semantics; route and leap/EOP scientific-policy decisions remain open
- **Time-profile decision:** `TIME_PROFILE_BLOCKER_CLOSED`
- **Milestone decision:** `2C_REMAINS_OPEN_WITH_EXACT_PREIMPLEMENTATION_BLOCKERS`
- **Production astronomy implemented:** no
- **Numerical scientific tolerance approved:** no
- **Frozen Batch 01 evidence changed:** no

`ScientificProfileV1` is a deliberately narrow contract for starting the first real
UFUQ astronomy implementation. It selects one observer-preset ID that becomes usable
for real execution only when instantiated by a 2D-approved record, and it accepts one
bounded UTC domain. It consumes a small authority-approved star artifact through
source-neutral typed astrometry and produces geometric horizontal directions only. It
does not claim global observer support, atmospheric refraction, physical-horizon dip,
terrain/building horizon, scientific visibility, cloud/weather, atmospheric extinction
or transparency, light pollution, rendering correctness, learner-interaction
correctness, or assessment/scoring correctness.

The profile is a permission-to-implement boundary, not a scientific-release approval.
An implementation result remains pending scientific acceptance until the later
production/reference, error-budget, and tolerance gates pass, together with any
stronger-independent-validation gate required for the claimed release boundary.

## Authority and evidence boundary

The profile is grounded in the existing pinned IAU SOFA `2023-10-11` release, the
official IERS Conventions 2010 baseline and IERS product documentation, official CDS
and ESA catalogue documentation, and the locked Astropy/PyERFA reference environment.
Those sources define models, fields, and routine semantics. They do not choose UFUQ's
observer, catalogue, operating dates, operational artifacts, implementation, or
tolerances.

Project decisions below remain project decisions even when an authoritative source
supplies their available options. Library defaults never become profile policy.

## Normative ScientificProfileV1 boundary

| Boundary | Normative V1 contract | Gate state |
|---|---|---|
| Profile identity | Every request and result carries `ScientificProfileV1` plus the exact algorithm/model/ephemeris, source-artifact, observer-preset, leap, EOP, and policy identities, versions, and hashes. | `PROJECT_DECISION`; normative. The named route/data identities remain supplied by their owning later decisions. |
| Observer | Exactly one preset ID is accepted: `umpsa-pekan-faculty-of-computing`, identifying **Faculty of Computing, UMPSA Pekan Campus, Pahang, Malaysia**. The generic `ObserverPreset` contract below fixes coordinate, Earth-model, height, accuracy, provenance, version, approval, and fail-closed semantics. Any other preset or arbitrary coordinate is outside V1; internal astronomy types remain observer-generic. | Contract semantics and site identity are the 2C project decision. Exact values and the approved immutable record are a 2D data handoff before real V1 execution. |
| Time input | The astronomy boundary accepts only explicit canonical UTC text `YYYY-MM-DDTHH:mm:ssZ`, at whole-second resolution, with uppercase `T`/`Z` and no fractional part, offset, local time, Unix timestamp, bare JD, or current-time default. Second `60` is a conditional token that becomes a validated instant only for `23:59:60Z` on an exact date confirmed by the approved leap artifact. | `PROJECT_DECISION`; normative grammar/state contract. RFC 3339 and SOFA supply broader syntax/conversion facts but do not choose UFUQ's subset, precision, or dates. |
| Catalogue/data | The runtime artifact contains only the minimal approved numerical ProfileV1 star allowlist selected in 2D. Cultural records reference stable internal `starId` values; a versioned crosswalk maps each `starId` to one or more source-release identifiers. A catalogue may be replaced or coexist without copying coordinates into cultural records. I/311 is the Phase 1 spike source, not the permanent catalogue by default. | Source/release, rights, row eligibility, allowlist, and artifact authority belong to 2D. |
| Normalized astrometry | Every eligible row supplies a source-neutral typed ICRS state with right ascension, declination, source epoch label, epoch representation and time scale, proper-motion derivative convention and duration unit, parallax/distance disposition, radial-velocity/perspective disposition, uncertainties/covariance or explicit reviewed omission, quality state, units, and provenance. `UNSPECIFIED` epoch scale, an implicit zero, or a library default is ineligible. | The source-neutral typed boundary is a normative `PROJECT_DECISION`; exact motion/parallax/RV eligibility and route dispositions remain with the route blocker, while concrete row evidence belongs to 2D. |
| Propagation/model route | Candidate route: eligible normalized ICRS catalogue state -> explicitly declared target-epoch `PropagatedIcrsAstrometry` -> observer-aware CIRS -> explicit Earth-orientation context -> `GeometricHorizontalDirection`. J2000.0 is only a candidate epoch boundary where required by the selected celestial interface; it is not a frame conversion. The production mapping must be pure TypeScript and traceable to the reviewed SOFA semantics. | The route, implementation/library mapping, and effect dispositions require AST-003 approval before becoming normative. |
| Earth orientation | The candidate policy uses one immutable, hash-addressed offline leap/EOP bundle. `UT1-UTC`, `xp`, `yp`, and any selected `dX`,`dY` each retain independent provenance, coverage, source quality, availability, and scientific approval. No automatic download, ambient cache discovery, nearest-row substitution, zero substitution, stale acceptance, prediction acceptance, or degraded fallback is permitted by the candidate. | Exact product classes, artifacts/hashes, interpolation, quality acceptance, coverage, expiry, and update policy remain open. |
| Output | The only V1 astronomy success state is geometric: north-zero/eastward-positive azimuth when defined, signed geometric altitude, normalized ENU direction, azimuth state, provenance, warnings, and upstream statuses. `BELOW_GEOMETRIC_HORIZON` remains a classification attached to that valid direction. | `PROJECT_DECISION`; normative. Scientific acceptance remains postimplementation. |
| Refraction | Disabled and not requested. No atmosphere object is accepted, no pressure/temperature/humidity/wavelength/lapse input is created, no default atmosphere exists, and neither astronomy nor scene code emits a refracted direction. | `PROJECT_DECISION`; normative V1 exclusion. A later profile may add a separately approved stage. |
| Horizon | Geometric altitude zero means only the astronomical local horizontal plane. Physical dip, visible or apparent/refracted horizon, terrain/buildings, renderer clipping, and learner cues are outside V1. | `PROJECT_DECISION`; normative separation. Later capabilities remain deferred, not zero-error. |
| Visibility | No aggregate scientific `visible`/`not-visible` result exists. Photometry/variability, daylight/twilight, extinction/transparency, cloud/weather, terrain/obstruction, light pollution, screen presentation, and learner eligibility remain separately typed future components and are not requested by V1. | `PROJECT_DECISION`; normative exclusion. Geometry never promotes visibility or learner eligibility. |
| Failure behavior | Evaluation fails closed for an invalid or missing required input, unavailable required artifact, unsupported profile/domain, unapproved required state/data, or numerical/algorithm failure. Later classifications and excluded optional stages cannot hide an earlier failure or erase a valid geometric state. No degraded result is reachable. | `PROJECT_DECISION`; normative semantic precedence. Wire/HTTP serialization remains separate. |
| Validation state | Contract-conforming execution initially yields `GEOMETRIC_RESULT_PENDING_VALIDATION`. `APPROVED_GEOMETRIC_RESULT` remains unreachable until the exact implementation/profile/data combination passes the postimplementation validation, error-budget, tolerance, and named-review gate. | `PROJECT_DECISION`; normative lifecycle distinction. |

### UTC and SupportedTimeDomain contract

The following is a normative `PROJECT_DECISION` for `ScientificProfileV1`. It closes
the generic time-input contract without selecting the still-open leap/EOP scientific
policy or inventing concrete supported dates.

The authority boundary is explicit:

| Conclusion | Classification |
|---|---|
| RFC 3339 defines a broader fixed-date/time syntax with mandatory seconds, optional fractional seconds, `Z` or numeric offset, and conditional second `60`; it does not validate the event date. | `SOURCE_SUPPORTED_FACT` |
| SOFA distinguishes UTC, TAI, TT, and UT1, represents calendar UTC as a two-part quasi Julian Date, and requires caller-supplied Earth-rotation inputs where applicable. | `SOURCE_SUPPORTED_FACT` |
| IERS Bulletin C is the authority for leap-second announcements; it is not by itself UFUQ's selected machine-readable artifact. | `SOURCE_SUPPORTED_FACT` |
| UFUQ accepts the whole-second Z-only subset, named internal states/split, fail-closed outcomes, and the `SupportedTimeDomain`/activation ownership below. | `PROJECT_DECISION` |

Astropy/PyERFA behavior remains reference-tool evidence only. Its accepted formats,
output precision, automatic IERS behavior, or ambient leap table cannot select
production policy.

The only public scientific timestamp grammar is:

```text
YYYY-MM-DDTHH:mm:ssZ
```

- `YYYY` is exactly four decimal digits; month, day, hour, minute, and second are
  exactly two digits; `T` and `Z` are uppercase literals;
- the date must be a valid Gregorian calendar date; hour is `00`-`23`, minute is
  `00`-`59`, and ordinary second is `00`-`59`;
- second `60` is only a conditional lexical representation. It is structurally
  eligible only as `23:59:60Z` and becomes a `ValidatedUtcInstant` only when the
  approved leap artifact confirms a positive leap second on that exact UTC date;
- no fractional-second form is accepted in V1. Whole-second resolution is the smallest
  deterministic scenario-input contract needed by this profile; it is not a
  scientific uncertainty, accuracy statement, rounding tolerance, or permission to
  truncate a higher-precision upstream observation silently; and
- numeric offsets, `-00:00`, local/IANA-zone text, unqualified date/time, calendar-only
  text, Unix/POSIX timestamps, JavaScript `Date`, bare Julian Dates, and implicit
  current/system time are not astronomy-core inputs.

A future profile may version a different precision. An upstream adapter may accept a
local civil time or a higher-precision value only under its own approved policy and
must deliberately resolve/quantize it into one exact V1 whole-second UTC instant while
retaining the original input, zone/offset, tzdb version, ambiguity decision, and any
rounding/quantization provenance. V1 defines no such rounding rule and therefore does
not silently accept a value that needs one.

The scientific time-state boundary is:

| State | Required semantics |
|---|---|
| `SuppliedCanonicalUtcText` | Exact accepted bytes plus parsed Gregorian fields; syntactic/calendar validity only. It is not yet leap-validated or domain-approved. |
| `ValidatedUtcInstant` | The supplied text and civil fields bound to the selected leap-data identity/version/hash and validation status. A second-`60` value cannot reach this state without exact event confirmation. |
| `UtcQuasiJulianDate` | Astronomy-core-only two-part representation of the validated UTC instant, explicitly labelled `UTC_QUASI_JD`, using the pinned `MJD_ZERO_PLUS_OFFSET` split (`part1 = 2400000.5`, `part2 = MJD including the UTC day fraction`) and retaining conversion routine/version/status. UTC civil days may contain 86399, 86400, or 86401 SI seconds; this is not a uniform time scale. |
| `TaiTwoPartJulianDate` | Two finite parts, `scale = TAI`, the same named split convention, leap-data identity, and conversion provenance/status. |
| `TtTwoPartJulianDate` | Two finite parts, `scale = TT`, the same named split convention, and conversion provenance/status. |
| `Ut1TwoPartJulianDate` | Two finite parts, `scale = UT1`, the same named split convention, exact `UT1-UTC` field provenance, EOP artifact/row/quality/availability/approval identity, interpolation-policy identity, and conversion provenance/status. |
| `TimeConversionEvidence` | Source and destination states, algorithm/routine/model/version, leap/EOP identities, raw and normalized warnings/statuses, and policy disposition. |

The branded two-part values are internal astronomy-core scientific states, not public
timestamp alternatives. Evidence/debug DTOs may serialize `part1`, `part2`, scale,
representation, split convention and provenance for replay. No unlabeled numeric JD,
single floating-point JD, or two-number tuple crosses a public scientific boundary.

Every activated profile version carries a `SupportedTimeDomain` record:

```text
SupportedTimeDomain {
  profileId,
  domainVersion,
  earliest { canonicalUtc, boundary: INCLUSIVE | EXCLUSIVE },
  latest { canonicalUtc, boundary: INCLUSIVE | EXCLUSIVE },
  inputResolution: WHOLE_SECOND,
  contributingDomainIdentities,
  requiredLeapAndEopPolicyIdentities,
  requiredArtifactManifestIdentities,
  requiredFieldCoverage,
  interpolationSupportRequirements,
  derivationMethodAndVersion,
  approval
}
```

Its concrete bounds are the intersection of every approved source/catalogue,
propagation/model/ephemeris, leap, required EOP-field, observer, and scenario domain.
Each boundary explicitly declares `INCLUSIVE` or `EXCLUSIVE`; file extent or another
field's coverage never implies either. An instant exactly on a boundary is supported
only when that boundary is inclusive and every required conversion, artifact, field,
quality/approval state, and interpolation neighbour/support requirement is satisfied.
The immediately preceding/following representable UTC whole second is tested, with
leap-second chronology respected; an excluded boundary or any instant outside returns
`TIME_OUTSIDE_SUPPORTED_DOMAIN`.

If one required EOP field lacks value or interpolation support at an otherwise in-range
instant, the result is `EOP_FIELD_UNAVAILABLE`, not a shortened implicit range, a
nearest row, extrapolation, zero, or promotion from another field. Missing or
unverified leap data returns `LEAP_VALIDATION_DATA_UNAVAILABLE`; available but
unapproved leap data returns `TIME_OR_EOP_STATE_NOT_APPROVED`. Either prevents UTC
validation/conversion before domain membership is claimed. The next EOP blocker owns
the permissible product/field/quality/interpolation/
offline/update policy; this contract only requires that its policy be explicit and
that activation prove complete coverage.

Lifecycle ownership is:

| Owner | Time responsibility |
|---|---|
| Milestone 2C | The exact V1 grammar and whole-second resolution; conditional leap syntax; typed UTC/TAI/TT/UT1 and two-part-JD states; no-current-time/no-local-time/no-unlabelled-JD rules; `SupportedTimeDomain` shape, explicit endpoint inclusion, complete-field/interpolation-support requirement, and fail-closed outcomes. |
| Remaining 2C leap/EOP decision | The scientifically permitted product/field roles, source-quality approval, interpolation, offline, expiry/update and warning/failure policy. This task does not close it. |
| Milestone 2D | Select/acquire the concrete leap/EOP families/releases and immutable bytes/manifests/hashes under the approved policy, plus the catalogue and observer artifacts whose coverage contributes to activation. |
| Milestone 2D/2E profile activation | Deterministically derive, record, review and approve the actual earliest/latest UTC values and boundary dispositions from the complete intersection; emit the versioned activation artifact. Generic astronomy-core code does not require those values to exist first. |

An application may later offer “now” only by sampling an approved clock outside
astronomy-core and freezing the resolved canonical UTC text and clock provenance in an
immutable `ScenarioSnapshot` before calling the core. Likewise, IANA time-zone and
daylight-saving resolution belongs to an upstream adapter; unresolved folds/gaps fail
there and one explicit canonical UTC instant crosses the scientific boundary.

### ObserverPreset contract and data handoff

Official UMPSA material establishes the selected site identity: the Faculty of
Computing is at the UMPSA Pekan campus. It supplies no approved latitude, longitude,
height, datum, coordinate epoch, or accuracy. `SOURCE_SUPPORTED_FACT` therefore covers
the identity only. Selecting that identity and the contract below is a
`PROJECT_DECISION`; the absent values remain `AUTHORITY_OR_EVIDENCE_MISSING` and are
owned by `B BLOCKS_2D_DATA_AUTHORITY`.

The only V1 identity is:

| Field | V1 value |
|---|---|
| `presetId` | `umpsa-pekan-faculty-of-computing` |
| Display label | `UMPSA Pekan — Faculty of Computing` |
| `siteIdentity` | `Faculty of Computing, UMPSA Pekan Campus, Pahang, Malaysia` |

The values below are required fields of every versioned `ObserverPreset`; their
concrete UMPSA values are deliberately absent from 2C:

| Contract field | Required semantics |
|---|---|
| `schemaVersion` | Identifies the observer-preset schema. |
| `presetId` | Stable project identifier; arbitrary coordinates and unknown IDs are outside V1. |
| `siteIdentity` | Human-readable physical-site identity, separate from numerical coordinates. |
| `referencePointDescription` | Identifies the point represented within a spatially extended site; a nearby control monument or campus centroid cannot be silently relabelled as the Faculty observation point. |
| `geodeticLatitude` | Finite value and unit; geodetic rather than geocentric; north-positive. The representational range is `[-90 deg,+90 deg]`, but V1 accepts only its approved preset rather than every point in that range. |
| `geodeticLongitude` | Finite value and unit; east-positive. Canonical V1 serialization is `[-180 deg,+180 deg)`, so `+180 deg` canonicalizes to `-180 deg`; the source representation and any normalization applied remain recorded. |
| `referenceSystem` | Discriminated kind (`GEODETIC_DATUM` or `TERRESTRIAL_REFERENCE_FRAME`), named identifier, and realization where applicable. WGS 84 is not inferred from absence. |
| `referenceEllipsoidId` | Named ellipsoid associated with the usable geodetic coordinates. |
| `coordinateReferenceEpoch` | Discriminated `DECLARED` value/representation and scale or standard semantics when required, or `NOT_REQUIRED` only with a source-supported basis. Missing a required epoch makes the artifact unsupported. |
| `height` | A discriminated `ELLIPSOIDAL`, `ORTHOMETRIC`, or `OTHER_APPROVED` representation: finite value and unit plus ellipsoid, vertical datum, or other approved reference-surface ID as applicable. |
| `heightConversion` | Absent when no conversion occurred; otherwise carries the model/version, inputs, provenance, output representation, and uncertainty. If the approved route requires ellipsoidal height, another height type is unsupported without an approved conversion. |
| `coordinateAccuracy` | State is `SOURCE_DECLARED`, `DERIVED`, or `UNKNOWN_UNBOUNDED`; retain horizontal/vertical components or covariance, units, confidence/coverage meaning, method, and source when supplied. Unknown accuracy is never encoded as zero. |
| `provenance` | Authority/source ID, source record or service-response ID, source version, acquisition identity/date, and licence/use conditions. A hidden map-provider coordinate is prohibited. |
| `dataVersionId` | Immutable version of the concrete observer data. |
| `artifactIdentity` | Manifest ID, byte length and SHA-256 when an immutable artifact or retained service response exists; a justified non-byte source reference must still be reproducible. |
| `artifactAvailability` | Availability is independent of scientific approval. Missing/unavailable data cannot activate the preset. |
| `validationStatus` | Structural/unit/range/reference-system validation is independent of source authority and approval. |
| `scientificApproval` | `APPROVED`, `NOT_APPROVED`, or `REVIEW_REQUIRED`, with scope, named reviewer, decision date, and decision reference. Approval for pending-validation implementation input is not a numerical accuracy bound or scientific result acceptance. |

| Lifecycle owner | Exact ownership |
|---|---|
| Milestone 2C | The generic fields and meanings above; north/east sign conventions and canonical longitude normalization; typed frame/ellipsoid/epoch/height/accuracy/provenance/version/approval states; the selected stable ID and site identity; one-preset-only V1 behavior; missing/unsupported outcomes; default prohibitions; and observer-generic, multi-preset-capable architecture. |
| Milestone 2D | The exact reference point within the Faculty site; latitude, longitude and height values; datum/frame realization, ellipsoid and applicable coordinate epoch; height source/conversion; accuracy evidence; source artifact/service response; acquisition identity/date; licence/use conditions; data version; manifest/hash; scientific/data review; and activation approval. |

The contract fails closed. It never obtains browser geolocation, inserts `(0,0)`, uses
zero height, discovers a map-provider pin, assumes WGS 84, substitutes another preset,
converts orthometric and ellipsoidal height silently, drops provenance, or turns an
unknown accuracy into zero. Missing, invalid, unsupported, unavailable, or unapproved
observer data prevents real V1 astronomy evaluation; it does not prevent implementing
the generic types, validation branches, and transformation interfaces.

Those observer states are distinct semantic outcomes: `MISSING` means a required field
or preset reference is absent; `INVALID` means its representation, value, unit, or
range is malformed; `UNAVAILABLE` means the identified artifact cannot be resolved;
`UNSUPPORTED` means a well-formed record is incompatible with the approved route or
domain; and `UNAPPROVED` means scientific activation is absent or rejected. The exact
wire and HTTP codes remain a separate contract decision. The selected reference system,
ellipsoid, epoch state, and height representation must match the approved route or pass
through an approved, provenance-bearing transformation whose uncertainty remains
explicit.

Milestone 2D must choose the exact Faculty reference point and acquire/review its
latitude, longitude, height, datum/frame/ellipsoid, applicable coordinate epoch,
accuracy, source record or official service response, acquisition identity/date,
licence/use conditions, data version, and immutable manifest/hash where appropriate.
An official reproducible UMPSA institutional or Malaysian-government geographic record
with documented accuracy is an eligible candidate for 2D review for this educational
celestial-direction application. The reviewer must approve its represented point,
semantics, accuracy, transformations, provenance, and bounded use; source class alone
does not establish scientific adequacy. A JUPEM survey-control record is **optional**,
not mandatory: it is useful only when it represents the intended point or supports a
documented transformation to it. This public-web audit did not establish a Faculty-
specific control record; that is not evidence none exists.

Exact coordinates remain necessary for replay and provenance. Away from a singular or
classification boundary, nearby points within the campus produce correspondingly local
changes in the direction vector; near the horizon a classification can change, and
near zenith/nadir azimuth can be ill-conditioned even when vector separation is small.
This qualitative sensitivity supplies no observer-position or angular tolerance and
does not turn UFUQ into a surveying system. Pekan and `Riyadh, Saudi Arabia` represent
materially different observer geometry and therefore form a useful later multi-location
validation partition, without implying any numerical positional tolerance. Riyadh is
only a planned later preset using this same contract: no Riyadh values are acquired, it
is not in V1, and it does not block the first implementation.

## Normative geometric and optional-stage contract

The following `PROJECT_DECISION` is normative for `ScientificProfileV1`. It fixes the
scientific state boundary without selecting the still-open transformation route,
supported UTC interval, leap/EOP product policy, concrete data, or any numerical
tolerance.

A successful V1 calculation returns an immutable `GeometricHorizontalDirection` with:

- signed geometric altitude in an explicit angular unit;
- north-zero, eastward-positive azimuth in its canonical angular representation when
  `azimuthState` permits a value;
- a finite normalized east/north/up direction vector;
- `azimuthState` and geometric-horizon classification;
- profile, algorithm/model/ephemeris, source-artifact, observer-preset, leap, EOP, and
  policy identities and versions applicable to the result;
- preserved scientific warnings and raw/normalized routine statuses; and
- `scientificValidationState`, initially
  `GEOMETRIC_RESULT_PENDING_VALIDATION`.

Geometric altitude zero is the astronomical local horizontal plane. A negative signed
altitude attaches `BELOW_GEOMETRIC_HORIZON` to the valid direction; it does not replace
or invalidate the result. The classification says nothing about apparent/refracted or
visible horizon, Earth-curvature or observer-height dip, terrain/buildings, renderer
clipping, physical visibility, or learner eligibility. No tolerance is invented for
equality with the plane.

`azimuthState` has these semantic states:

- `DEFINED`: a canonical azimuth value accompanies the direction;
- `UNDEFINED_SINGULAR`: at mathematical zenith or nadir the horizontal projection is
  zero, so altitude and ENU remain valid while azimuth has no scientific value; and
- `ILL_CONDITIONED`: reserved for a future reviewed numerical/domain boundary near the
  singular geometry. No implementation may assign this state from an arbitrary
  epsilon, machine precision, display precision, or test tolerance.

Until the `ILL_CONDITIONED` boundary is approved, implementations retain the ENU vector
and altitude, never use azimuth as the sole comparison/scoring quantity near the
singular geometry, and report the exact singular state when established. The missing
numerical boundary does not prevent implementing the value/state separation.

Refraction is excluded, not missing, for V1:

- the profile fixes the stage to `REFRACTION_NOT_REQUESTED`;
- it accepts and creates no atmosphere or refraction inputs;
- it inserts no default pressure, temperature, humidity, wavelength, height-transfer,
  or lapse assumption;
- it emits no model-apparent or refracted coordinate; and
- `REFRACTION_UNAVAILABLE` remains a distinct later-profile state for a requested stage
  whose required policy/input is unavailable. It is unreachable in V1 because V1 never
  requests the stage.

Visibility is likewise excluded, not inferred:

- V1 emits no aggregate `visible: true` or `visible: false` claim;
- geometric position and `BELOW_GEOMETRIC_HORIZON` are only coordinate/classification
  evidence;
- photometry/variability, Sun altitude/daylight/twilight, atmospheric extinction/
  transparency, cloud/weather, terrain/obstruction, light pollution, screen
  presentation, and learner eligibility remain separately typed future components;
  and
- no component promotes another, and learner eligibility is never inferred from a
  geometric direction.

These excluded capabilities remain unbounded/deferred in the error-budget ledger. An
excluded stage is outside the profile; it is not assigned zero uncertainty.

## Normative scientific outcomes and precedence

The following names identify semantic outcome classes, not finalized JSON or HTTP
codes:

| Semantic outcome | Result retention and meaning |
|---|---|
| `GEOMETRIC_RESULT_PENDING_VALIDATION` | A contract-conforming geometric result executed using the approved profile inputs and policies. It is executable evidence, not a scientifically accepted learner/release result. |
| `APPROVED_GEOMETRIC_RESULT` | The same provenance-bearing result only after the exact implementation/profile/data combination passes the applicable postimplementation production/reference partitions, error-budget/tolerance review, and named scientific approval. Initially unreachable. |
| `INVALID_INPUT` | A supplied field/value/representation is malformed, non-finite, contradictory, or otherwise structurally invalid. No fabricated result. |
| `REQUIRED_INPUT_MISSING` | A required profile input was not supplied. Distinct from malformed input and unavailable artifacts. No fabricated default. |
| `REQUIRED_ARTIFACT_UNAVAILABLE` | An identified required artifact or required artifact field cannot be resolved or verified. Exact leap/EOP subtypes remain owned by the later data-policy decision. |
| `UNSUPPORTED_PROFILE_DOMAIN` | Inputs are structurally valid but lie outside the profile or its later-approved date/observer/source/model domain. |
| `REQUIRED_STATE_NOT_SCIENTIFICALLY_APPROVED` | A required input, field quality, policy, or data state exists but lacks approval for this exact profile/domain. This is distinct from the pending validation of an executed implementation result. |
| `SCIENTIFIC_EXECUTION_FAILURE` | The approved numerical/algorithm path cannot complete or produces an invalid scientific state. Preserve the failing stage and routine statuses; do not return partial coordinates as success. |
| `TIMESTAMP_SYNTAX_INVALID` | The supplied scientific timestamp does not match the exact V1 grammar or valid Gregorian civil fields. Distinct from a conditional second-`60` that fails event validation. |
| `LEAP_SECOND_INSTANT_INVALID` | `23:59:60Z` has the conditional form but the approved leap artifact confirms no positive leap second on that exact date. |
| `LEAP_VALIDATION_DATA_UNAVAILABLE` | The identified required leap artifact is absent, unreadable, unverified, or hash-mismatched, so UTC validation/conversion fails closed. No ambient ERFA table or system clock substitutes. An available but unapproved artifact uses `TIME_OR_EOP_STATE_NOT_APPROVED`. |
| `REQUIRED_TIME_SCALE_UNAVAILABLE` | A required labelled UTC/TAI/TT/UT1 conversion state cannot be constructed from approved inputs. Retain the failed conversion stage. |
| `EOP_FIELD_UNAVAILABLE` | A required EOP field or its approved interpolation support is absent/out of range at the instant. Other fields cannot promote it. Exact field/policy refinements remain with the EOP decision. |
| `TIME_OUTSIDE_SUPPORTED_DOMAIN` | The validated instant is at an excluded boundary or outside the activated domain's explicit earliest/latest bounds. Distinct from artifact/field unavailability inside the declared interval. |
| `TIME_OR_EOP_STATE_NOT_APPROVED` | Required leap/EOP data or field quality exists but lacks scientific approval for this profile/domain. |
| `TIME_CONVERSION_WARNING` | Attached evidence, not automatic success or rejection: preserve the producing stage/routine/version and raw/normalized status for disposition by the approved policy. |
| `AZIMUTH_UNDEFINED_OR_ILL_CONDITIONED` | Attached state, not a terminal result: retain valid altitude/ENU/provenance. Exact singularity is normative; a near-singular numerical boundary remains review-gated. |
| `BELOW_GEOMETRIC_HORIZON` | Attached classification, not a terminal result: retain the complete valid geometric direction and validation state. |
| `OPTIONAL_STAGE_NOT_REQUESTED` | Attached stage state. In V1 this includes `REFRACTION_NOT_REQUESTED` and profile-excluded visibility processing; it cannot invalidate geometry. |

Deterministic semantic precedence is:

1. validate request structure and supplied values, including timestamp grammar and
   Gregorian fields;
2. identify missing required V1 inputs;
3. resolve/verify/approve the leap artifact, validate conditional second `60`, and
   construct `ValidatedUtcInstant`;
4. validate the activated `SupportedTimeDomain`;
5. validate the observer preset and required artifact;
6. validate source-astrometry availability and eligibility;
7. validate the EOP artifact and each required field's independent availability,
   coverage, interpolation support, source quality/provenance, and approval;
8. validate every other required state/data/policy approval;
9. execute the approved scientific route and preserve failures, warnings, and statuses;
10. create the pending-validation geometric result;
11. attach azimuth/singularity and geometric-horizon classifications without erasing
   the result; and
12. attach V1 optional-stage-not-requested states without invoking refraction,
   visibility, scene, learner, or assessment policy.

The remaining leap/EOP decision may refine ordering inside stages 3 and 7 among its
field quality, availability, interpolation, and warning checks. It cannot move EOP
failure before timestamp/domain validation or reverse this invariant: a later
classification or
optional-stage state never hides an earlier required-input/artifact/domain/approval/
execution failure, and never erases an earlier valid geometric state.

Every underlying scientific warning and status is retained with source stage,
routine/model identity and version, raw code/value where available, normalized meaning
where approved, and policy disposition. A warning is neither silently downgraded to
success nor automatically promoted to scientific rejection; the approved profile
policy decides whether it permits a result. Warning/status evidence remains distinct
from transport status, HTTP mapping, application logging, and log severity.

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
| Atmospheric refraction | `EXCLUDED_PROFILE_V1`. | Normative V1 exclusion; no V1 atmosphere/refraction algorithm or input. All physical model questions move to a later extension. |

## Exact remaining preimplementation blockers

Only the following two items keep Milestone 2C open. They require named astronomy-
expert and supervisor approval; none requires TypeScript output or a numerical
tolerance. The boundary/output/outcome and UTC/time-domain clusters closed by the
successive audits are not included.

1. Approve the normative V1 route and production algorithm/library/model/ephemeris
   mapping, including every include/exclude/unavailable effect disposition and the
   source-neutral parallax/radial-velocity/missing-state branches.
2. Approve the V1 leap/EOP product classes, exact artifact-selection requirements,
   field-by-field quality/availability/interpolation/coverage rules, offline/expiry/
   update policy, and no-degraded-fallback behavior. Actual acquired bytes and hashes
   are a 2D handoff before real execution.

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
engine semantics and its source data have different owners. The resolved generic
observer contract is documented above and is no longer an open row.

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
| Exact UMPSA reference point, coordinates, Earth model, height, accuracy and immutable record | `B BLOCKS_2D_DATA_AUTHORITY` | 2D acquires and approves the concrete preset before real V1 execution; missing values do not prevent generic astronomy-core implementation. |
| UTC grammar/precision and `SupportedTimeDomain` semantics | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved as the normative whole-second Z-only grammar, conditional leap validation, typed scales, explicit endpoint disposition and fail-closed domain contract. |
| Concrete ProfileV1 earliest/latest UTC values | `B BLOCKS_2D_DATA_AUTHORITY` | 2D/2E activation derives and approves values from complete approved source/model/leap/EOP/observer/scenario coverage; values are data, not generic implementation semantics. |
| Geometric-only, refraction-disabled and no-default-atmosphere decision | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved as normative V1 semantics. Physical refraction remains D and no excluded uncertainty becomes zero. |
| Physical refraction model, meteorology and apparent-horizon domain | `D BLOCKS_LATER_EXTENSION` | Required only if a later profile enables refraction. |
| No aggregate visibility decision | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved as normative V1 semantics; no aggregate visibility result exists. |
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
| `2C-007` | F | The generic contract and UMPSA Pekan Faculty site identity are defined; the concrete record is B, while global ranges and pole support are D. |
| `2C-008` | A | V1 route, mapping, and effect dispositions must be normative. |
| `2C-009` | A | V1 leap/EOP semantics and fail-closed input policy are runtime science inputs; bytes/hashes are acquired in 2D. |
| `2C-010` | D | Refraction model questions move later once geometric-only V1 is approved. |
| `2C-011` | D | Physical/terrain/visibility aggregation is excluded; learner parts are secondarily E. |
| `2C-012` | F | Semantic outcomes, precedence, exact singularity behavior, warning/status preservation, and pending-versus-approved validation states are normative. A numerical ill-conditioned boundary and wire/HTTP mapping remain later without reopening the semantic contract. |
| `2C-013` | C | Numerical error budgets and thresholds govern postimplementation acceptance. |
| `2C-014` | C | Production/reference comparison requires production; the preimplementation protocol/environment already exists. |
| `2C-015` | F | The bounded-domain shape, explicit endpoint semantics and no-extrapolation behavior are normative; actual UTC bounds are a B activation artifact and broader dates remain D. |
| `AST-001` | B | Catalogue authority, rights, provenance, row quality, and allowlist belong to 2D. |
| `AST-002` | E | Arabic/Najdi names, membership, relationships, and lesson approval do not block astronomy-core. |
| `AST-003` | A | The controlling obligation is profile route/effect/input approval. I/311 is secondary B; residuals/tolerances are secondary C. |
| `AST-004` | D | The V1 geometric-only/no-refraction/no-visibility exclusion is normative. Remaining refraction/horizon/visibility model questions are later D, with learner questions secondarily E. |
| `AST-005` | F | Kaaba/Qibla target authority is outside this celestial-position profile. |
| `AST-006` | C | The 2C.5C method may be reviewed now; numerical bounds/tolerances are postimplementation acceptance work. |
| `AST-007` | F | The V1 UTC grammar/time-state/domain contract and observer contract/site identity are resolved for 2C. Concrete time bounds and observer record are B; multiple cities, arbitrary locations, local-time UX, and learner fixtures are D/E. |

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
| `AST-SRC-006` | B | Domain/endpoint semantics are resolved; actual bounds are derived and approved at 2D/2E activation from concrete coverage. |
| `AST-SRC-007` | A | UTC grammar and conditional leap validation are resolved; only leap-product/validity/update scientific policy remains A, with exact acquired bytes secondary B. |
| `AST-SRC-008` | F | Qibla geodesy is outside this profile. |
| `AST-SRC-009` | B | Controls I/311 eligibility only. |
| `AST-SRC-010` | A | Route/effect selection is A; production comparison and tolerance are C. |
| `AST-SRC-011` | B | Source scale/RV authority is B; the normalized unavailable/omission branch is secondary A. |
| `AST-SRC-012` | B | The V1 contract/site identity is defined; exact UMPSA values, accuracy and artifact approval are 2D data, while multiple/global observer support is D. |
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
| A | `A-003`, `A-004`, `B-002`-`B-006`, `B-008`, `B-009`, `C-001`-`C-004`, `C-007`-`C-009` | 16 | Decide included-input/effect/time semantics; their numerical bounds may remain unresolved for later acceptance. |
| B | `A-001`, `A-002`, `A-005`, `A-006`, `B-001`, `D-001`-`D-006` | 11 | Catalogue/source and concrete observer-artifact values, provenance, uncertainty and domain instantiation move to 2D eligibility. The generic observer contract remains fixed by 2C. |
| C | `F-001`, `F-005`, `F-006` | 3 | Production floating-point/reference disagreement and production determinism require code. `F-005` includes the code-independent production/reference measurement plus any stronger lineage-independent evidence required by the claim; it does not label Astropy/ERFA agreement independent. `F-006` is already satisfied for Batch evidence transport only. |
| D | `B-007`, `C-005`, `C-006`, `E-001`-`E-007`, `G-001`-`G-003` | 13 | Multiple-body deflection, observed CPO, refraction, and scene/render terms remain explicitly unresolved because the profile excludes those capabilities. Their dispositions revert to A or C only if a later profile includes them. |
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
4. the generic preset-observer contract and selected site identity, exact UTC grammar,
   typed time states and `SupportedTimeDomain` semantics, plus leap/EOP scientific
   input policy and offline/fail-closed rules are normative, while exact observer/time/
   operational-data activation records are explicitly handed to 2D/2E;
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
hard-coded astronomy formula. Observer coordinates enter through the same generic
`ObserverPreset` resolution contract used by future profiles. Later validation must
partition multiple approved presets, latitude, longitude, ellipsoidal height, near-equatorial
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
| RFC 3339 official record | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Defines the broader Internet timestamp grammar and conditional leap-second representation. It does not require UFUQ's whole-second Z-only subset or select supported dates. |
| Astropy `8.0.1` and locked reference environment | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Candidate reference path only. |
| PyERFA `2.0.1.5` release/source pin | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient for frozen synthetic evidence. Version-matched documentation/tagged-source review and reviewer acceptance remain a later prerequisite for postimplementation reference-validation claims; PyERFA cannot supply the stronger independent oracle. |
| IERS Bulletin A/B/C and `finals2000A` documentation | `OFFICIAL_WEB_SUFFICIENT` | Defines products/fields/quality roles; does not select bytes, accepted qualities, dates, or policy. |
| IANA versioned leap artifacts | `OFFICIAL_WEB_SUFFICIENT` | Candidate machine artifact; IERS Bulletin C remains event authority. |
| CDS I/311 ReadMe/Appendix G/unit standard and ESA I/311 epoch page | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient for known fields and Julian representation, not time scale, rights, row suitability, or permanent source selection. |
| ESA Gaia release documentation/archive | `OFFICIAL_WEB_SUFFICIENT` | Sufficient for 2D candidate evaluation; no Gaia release or subset is selected here. |
| Official UMPSA Faculty/Pekan site-identity pages | `OFFICIAL_WEB_SUFFICIENT` | Establish the selected Faculty-at-Pekan identity only; they supply no approved geodetic value or accuracy. |
| JUPEM geodetic product/service documentation | `OFFICIAL_WEB_SUFFICIENT` | Establishes available GPS-control, coordinate-transformation, geoid and GNSS/RINEX services. It does not prove a Faculty-specific control record exists or make survey control mandatory. |
| Exact UMPSA observer-preset data record | `USER_ACTION_REQUIRED_BEFORE_2D` | Required before 2D can approve the concrete preset and before real V1 execution, not before 2C closes or generic astronomy-core is written. |
| JUPEM survey-control record for the Faculty site | `NOT_NEEDED` | Optional evidence if site-matched and proportionate; no control monument is a profile requirement. |
| Future `Riyadh, Saudi Arabia` preset record | `REQUIRED_LATER` | Uses the same generic contract in a later multi-location profile; no coordinates are needed now. |
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

**Immediate user-action answer:** no. The first site identity is selected and the 2C
contract can close without numerical observer data. No coordinate download, new
astronomy standards PDF, positional-astronomy manual, replacement SOFA/IERS document,
Riyadh record, or NOVAS package is needed now.

### USER_ACTION_REQUIRED_BEFORE_2D: exact UMPSA observer record

- **Selected site:** `Faculty of Computing, UMPSA Pekan Campus, Pahang, Malaysia`;
  official UMPSA evidence already supports this identity.
- **Exact resource:** an official reproducible UMPSA institutional geographic/asset
  record, Malaysian-government geographic record, JUPEM product/service response, or
  equivalent licensed record for a described point at the Faculty site.
- **Why:** 2D must instantiate latitude, east-positive longitude, typed height,
  datum/reference frame, reference ellipsoid, coordinate epoch where applicable,
  accuracy/uncertainty, source identity, acquisition metadata, use conditions, and
  version/hash. Orthometric height cannot reach an ellipsoidal-height route without a
  separately evidenced conversion.
- **Acceptable source:** an official/reproducible institutional or Malaysian-government
  record is eligible for 2D review when it supplies the contract fields and documented
  accuracy. The reviewer, not the source class, decides whether it is adequate for the
  bounded use. A JUPEM survey-control record is optional and must not be substituted
  for the intended Faculty point merely because it is more precise.
- **PDF/download actually needed:** no particular file format is required; an official
  retained service response or reproducible web/download record is an acceptable
  acquisition format for 2D review if it exposes the required site-specific fields.
- **Suggested path:**
  `local-reference/astronomy/observers/umpsa-pekan-faculty-of-computing/<source-record>.<original-extension>`.
- **Blocks:** 2D approval/activation of the concrete observer artifact and real
  ProfileV1 execution. It does not block 2C closure or generic astronomy-core work.
- **Web substitution:** yes. An authoritative reproducible web/service record can be
  retained with its source identity, acquisition date, version, and hash where
  appropriate.

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
  -> 2D catalogue/source, observer-preset, acquisition, rights, row, crosswalk, and operational-data authority
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
