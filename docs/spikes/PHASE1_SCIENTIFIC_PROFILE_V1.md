# Phase 1 Milestone 2C.6: ScientificProfileV1 exit-gate audit

## Status and decision

- **Profile:** `ScientificProfileV1`
- **Profile state:** normative for boundary/output/outcome, UTC/time-domain,
  transformation-route/effect/production-mapping, and leap/EOP scientific-policy
  semantics
- **Time-profile decision:** `TIME_PROFILE_BLOCKER_CLOSED`
- **Transformation-route decision:** `TRANSFORMATION_ROUTE_BLOCKER_CLOSED`
- **Leap/EOP-policy decision:** `LEAP_EOP_POLICY_BLOCKER_CLOSED`
- **Milestone decision:** `MILESTONE_2C_READY_TO_CLOSE_FOR_IMPLEMENTATION`
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
| Profile identity | Every request and result carries `ScientificProfileV1` plus the exact algorithm/model/ephemeris, source-artifact, observer-preset, leap, EOP, and policy identities, versions, and hashes. | `PROJECT_DECISION`; normative. This audit fixes the model/route family; implementation manifests and 2D/2E artifacts supply their exact source/build/data hashes before execution. |
| Observer | Exactly one preset ID is accepted: `umpsa-pekan-faculty-of-computing`, identifying **Faculty of Computing, UMPSA Pekan Campus, Pahang, Malaysia**. The generic `ObserverPreset` contract below fixes coordinate, Earth-model, height, accuracy, provenance, version, approval, and fail-closed semantics. Any other preset or arbitrary coordinate is outside V1; internal astronomy types remain observer-generic. | Contract semantics and site identity are the 2C project decision. Exact values and the approved immutable record are a 2D data handoff before real V1 execution. |
| Time input | The astronomy boundary accepts only explicit canonical UTC text `YYYY-MM-DDTHH:mm:ssZ`, at whole-second resolution, with uppercase `T`/`Z` and no fractional part, offset, local time, Unix timestamp, bare JD, or current-time default. Second `60` is a conditional token that becomes a validated instant only for `23:59:60Z` on an exact date confirmed by the approved leap artifact. | `PROJECT_DECISION`; normative grammar/state contract. RFC 3339 and SOFA supply broader syntax/conversion facts but do not choose UFUQ's subset, precision, or dates. |
| Catalogue/data | The runtime artifact contains only the minimal approved numerical ProfileV1 star allowlist selected in 2D. Cultural records reference stable internal `starId` values; a versioned crosswalk maps each `starId` to component-scoped source-release records and independent per-field authorities. I/311 is the Phase 1 spike source, not the permanent catalogue. The 2D.1 audit prefers Gaia DR3 version 1.1; its preliminary bounded screen found 8/19 technical matches and five finite-RV candidates but no Polaris match, yet retained no reproducible query/result manifest. The analytic TCB-to-TDB adapter is approved; no row is approved pending immutable acquisition, component/systematics/quality/RV-proxy review, an exact Polaris fallback and exact derived-artifact rights interpretation. | Source/release, rights, row eligibility, allowlist, and artifact authority belong to 2D; current result `CATALOGUE_AUTHORITY_BLOCKED`. |
| Normalized astrometry | Every eligible row supplies a source-neutral typed ICRS state with right ascension, declination, an approved normalized source-epoch instant/scale plus distinct native-epoch evidence, proper-motion derivative convention and duration unit, explicit `mu_alpha_star` and Dec components, a positive approved parallax or equivalent distance converted with provenance, an approved propagation radial velocity, uncertainties/covariance, quality state, units, compatible-system identity, normalization evidence, and provenance. `UNSPECIFIED` or relabelled epoch/derivative scale, mixed compatible systems, zero/negative/missing/unapproved parallax, missing/unapproved radial velocity, implicit zero, or a library default is V1-ineligible. | The source-neutral eligibility semantics are a normative `PROJECT_DECISION`; concrete source values/quality/crossmatches belong to 2D. |
| Propagation/model route | The normative typed dependency graph is `CatalogueIcrsState` -> target-epoch `PropagatedIcrsAstrometry`; typed time/observer/leap/EOP/model inputs -> `EarthOrientationContext`; both feed `ObserverAwareCirsDirection`, then `GeometricHorizontalDirection`. The propagation target is the SOFA J2000.0 epoch interface (`JD(TDB) 2451545.0`), not a frame conversion or a claim about a source epoch. | Normative `PROJECT_DECISION`: a UFUQ-owned pure-TypeScript subset derived from pinned SOFA `2023-10-11`, with explicit status/data injection and licence attribution. Implementation output remains pending validation. |
| Earth orientation | V1 requires approved leap state plus independently approved `FINAL` `UT1-UTC`, `xp`, and `yp` field states. It selects four-point Lagrange interpolation based on Gazette 13's published example, continuous `UT1-TAI` handling across leaps, and exactly-once IERS Conventions 2010 subdaily restoration; it also requires immutable offline bundles and fail-closed quality/support rules. The route consumes the resulting instantaneous fields. It uses model CIP/CIO from IAU 2006 precession with IAU 2000A nutation and the matching transformation; observed `dX`,`dY` offsets and LOD are not requested, not supplied as zero, and not hidden library inputs. | `PROJECT_DECISION`; normative for implementation entry. Exact artifact families/releases/bytes/hashes and exact official interpolation/restoration source configuration are 2D data authority before real execution. |
| Output | The only V1 astronomy success state is geometric: north-zero/eastward-positive azimuth when defined, signed geometric altitude, normalized ENU direction, azimuth state, provenance, warnings, and upstream statuses. `BELOW_GEOMETRIC_HORIZON` remains a classification attached to that valid direction. | `PROJECT_DECISION`; normative. Scientific acceptance remains postimplementation. |
| Refraction | Disabled and not requested. No atmosphere object is accepted, no pressure/temperature/humidity/wavelength/lapse input is created, no default atmosphere exists, and neither astronomy nor scene code emits a refracted direction. | `PROJECT_DECISION`; normative V1 exclusion. A later profile may add a separately approved stage. |
| Horizon | Geometric altitude zero means only the astronomical local horizontal plane. Physical dip, visible or apparent/refracted horizon, terrain/buildings, renderer clipping, and learner cues are outside V1. | `PROJECT_DECISION`; normative separation. Later capabilities remain deferred, not zero-error. |
| Visibility | No aggregate scientific `visible`/`not-visible` result exists. Photometry/variability, daylight/twilight, extinction/transparency, cloud/weather, terrain/obstruction, light pollution, screen presentation, and learner eligibility remain separately typed future components and are not requested by V1. | `PROJECT_DECISION`; normative exclusion. Geometry never promotes visibility or learner eligibility. |
| Failure behavior | Evaluation fails closed for an invalid or missing required input, unavailable required artifact, unsupported profile/domain, unapproved required state/data, or numerical/algorithm failure. Later classifications and excluded optional stages cannot hide an earlier failure or erase a valid geometric state. No degraded result is reachable. | `PROJECT_DECISION`; normative semantic precedence. Wire/HTTP serialization remains separate. |
| Validation state | Contract-conforming execution initially yields `GEOMETRIC_RESULT_PENDING_VALIDATION`. `APPROVED_GEOMETRIC_RESULT` remains unreachable until the exact implementation/profile/data combination passes the postimplementation validation, error-budget, tolerance, and named-review gate. | `PROJECT_DECISION`; normative lifecycle distinction. |

### UTC and SupportedTimeDomain contract

The following is a normative `PROJECT_DECISION` for `ScientificProfileV1`. It closes
the generic time-input contract without selecting concrete leap/EOP artifacts or
inventing supported dates.

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
| `TdbTwoPartJulianDate` | Route-scoped two-part epoch state, `scale = TDB`, constructed from an approved source/target epoch conversion and retaining the conversion model/status. It is required at the `pmsafe`-derived propagation boundary; no source epoch may be relabelled TDB. The fixed target interface is `JD(TDB) 2451545.0`. |
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
validation/conversion before domain membership is claimed. The leap/EOP policy below
defines the permissible source quality, interpolation/restoration, offline, update,
validity, and warning disposition; activation must prove complete support.

Lifecycle ownership is:

| Owner | Time responsibility |
|---|---|
| Milestone 2C | The exact V1 grammar and whole-second resolution; conditional leap syntax; typed UTC/TAI/TT/UT1 and route-scoped TDB epoch states; no-current-time/no-local-time/no-unlabelled-JD rules; `SupportedTimeDomain` shape, explicit endpoint inclusion, complete-field/interpolation-support requirement, final-only leap/EOP semantic policy, and fail-closed outcomes. |
| Milestone 2D | Select/acquire the concrete leap/EOP families/releases and immutable bytes/manifests/hashes under the approved policy, plus the catalogue and observer artifacts whose coverage contributes to activation. |
| Milestone 2D/2E profile activation | Deterministically derive, record, review and approve the actual earliest/latest UTC values and boundary dispositions from the complete intersection; emit the versioned activation artifact. Generic astronomy-core code does not require those values to exist first. |

An application may later offer “now” only by sampling an approved clock outside
astronomy-core and freezing the resolved canonical UTC text and clock provenance in an
immutable `ScenarioSnapshot` before calling the core. Likewise, IANA time-zone and
daylight-saving resolution belongs to an upstream adapter; unresolved folds/gaps fail
there and one explicit canonical UTC instant crosses the scientific boundary.

### Leap/EOP scientific and operational policy

This subsection is the normative `PROJECT_DECISION` that closes
`LEAP_EOP_POLICY_BLOCKER_CLOSED`. Official IERS product documentation supplies the
field/product facts; IERS Gazette 13 supplies a recommended interpolation/restoration
procedure, a four-point Lagrange example, and permission for equivalent methods; IERS
Conventions 2010 supplies the governing subdaily correction families; the official C04
guide supports continuous `UT1-TAI` treatment across leap discontinuities; IERS
Bulletin C supplies leap-event authority; and IANA supplies one eligible official
machine-transport family. None of those sources independently chooses UFUQ's exact
four-point support, final-only acceptance, replay, or fail-closed policy.

#### Required state and accepted source quality

The complete V1 operational input set is:

| Input | Meaning and unit | V1 disposition |
|---|---|---|
| `ApprovedLeapState` | Ordered `TAI-UTC` transition/event state bound to exact authority, transport, version, byte/hash, publisher-validity, coverage and approval identities. | Required for every UTC validation/conversion. Bulletin C is event authority; a 2D-selected official IERS or IANA machine artifact is transport. |
| `UT1-UTC` | UT1 minus UTC, seconds, evaluated for the requested validated UTC instant. | Required; `FINAL` and independently approved only. Passed explicitly to the SOFA-derived route. |
| `xp` | ITRS polar-motion coordinate of the CIP along the IERS reference meridian, radians. | Required; `FINAL` and independently approved only. |
| `yp` | ITRS polar-motion coordinate of the CIP along the 90-degrees-west meridian, radians. | Required; `FINAL` and independently approved only. |

Observed CPO `dX`,`dY` and LOD are `NOT_REQUIRED_BY_PROFILE_V1`. They are neither
looked up nor represented as zero; no dependency may request them implicitly.

Bulletin B final Section 1 values are eligible source material. A `finals2000A` artifact
is eligible only through Bulletin B columns whose final lineage is independently
verified in the activation manifest. The format defines its Bulletin A `I` flag as
`IERS`, not `FINAL`; Bulletin A documentation separately calls the non-predicted rapid
values quick-look estimates, which UFUQ maps to `IERS_ESTIMATE`. V1 rejects
`IERS_ESTIMATE`, `PRELIMINARY`, `PREDICTED`, `UNKNOWN`, blank,
unmapped, or unapproved quality. Official publication and file presence never equal
UFUQ scientific approval.

Every EOP field carries an independent state:

```text
ApprovedEopFieldState {
  field: UT1_MINUS_UTC | XP | YP,
  value,
  unit: SECOND | RADIAN,
  requestedUtcInstant,
  sourceProductId,
  sourceSeriesId,
  sourceArtifactIdsAndHashes,
  sourceSampleIdsAndEpochs,
  rawSourceFlags,
  sourceQuality,
  sourceDeclaredUncertainty,
  artifactAvailability,
  fieldCoverage,
  publisherValidity,
  interpolationEvidence,
  scientificApproval,
  policyAndBundleIdentity,
  rawAndNormalizedStatuses
}
```

The orthogonal vocabularies are:

```text
SourceFieldQuality = FINAL | PRELIMINARY | PREDICTED | IERS_ESTIMATE | UNKNOWN
ArtifactAvailability = AVAILABLE | UNAVAILABLE | INTEGRITY_FAILURE
FieldCoverage = COVERED | OUT_OF_RANGE | GAP | INSUFFICIENT_INTERPOLATION_SUPPORT
PublisherValidity = VALID_FOR_REQUEST | EXPIRED_FOR_REQUEST | NOT_DECLARED | UNVERIFIED
ScientificApproval = APPROVED | NOT_APPROVED | REVIEW_REQUIRED
```

A shared source flag may be cited by `xp` and `yp`, but each field independently proves
value presence, finite/unit validity, quality, sample provenance, support, coverage and
approval. A source-declared uncertainty is retained with its native meaning and unit;
missing or unknown uncertainty is explicit and never becomes zero. One field, row,
pair, or product never promotes another.

#### Interpolation and endpoint support

The authority/policy split is explicit: Gazette 13 recommends its Lagrangian procedure,
its example uses four points, and it permits equivalent interpolation schemes. The
following exact four-point method and strict support rules are UFUQ `PROJECT_DECISION`
semantics rather than an assertion that IERS mandates four points:

- interpolate the daily low-frequency component of each required EOP field with a
  four-point Lagrange window;
- for a request between ordered samples `i` and `i+1`, require
  `i-1`,`i`,`i+1`,`i+2` for that field; use the same full-support rule at an exact
  tabulated instant so profile endpoints have one deterministic rule. Requiring the
  full window at an exact sample is conservative, not mathematically necessary to
  reproduce that value, and deliberately narrows the activated interval at both ends;
- require every contributor to be finite, `FINAL`, individually approved, and part of
  an explicitly reviewed coherent series; record artifact/row IDs, epochs, qualities,
  interpolation weights, method/model identities and statuses;
- derive each support value as
  `UT1-TAI = (UT1-UTC) - (TAI-UTC)`, interpolate that continuous quantity, then
  reconstruct `UT1-UTC = (UT1-TAI) + (TAI-UTC)` with the approved target-instant leap
  state; never polynomial-interpolate directly across a UTC leap step. UT1 and TAI
  continuity, UTC leap discontinuity, and the C04 conversion practice are
  `SOURCE_SUPPORTED_FACT`; this exact
  UFUQ reconstruction contract is a `PROJECT_DECISION`, not a Gazette 13 algorithm;
- after interpolation, restore exactly once the IERS Conventions 2010 terms absent
  from the daily series: Chapter 8 ocean-tide corrections for `xp`,`yp`, and UT1;
  Chapter 5 Table 5.1a diurnal libration corrections for `xp`,`yp`; and Table 5.1b
  semidiurnal libration corrections for UT1. Long-period and secular polar-motion
  libration already present in reported observations is not added again; and
- reject a gap, duplicate or nonmonotonic epoch, missing/unapproved neighbor,
  unrecorded source boundary, insufficient support, nearest-row request, or
  extrapolation.

IERS Gazette 13 says an equivalent interpolation can be substituted, but V1 has no
approved equivalence evidence. Therefore a generic linear, spline, Astropy-default, or
otherwise “equivalent” implementation is not permitted by this profile. Gazette 13's
historical eight-term `RAY` routine is not the selected IERS 2010 restoration. 2D pins
the exact official 2010-baseline routine/coefficient/dependency bytes (including the
`ORTHO_EOP`/`CNMTX`, `PMSDNUT2`, and `UTLIBR` families), the selected product's
regularization semantics, and any separately reviewed working correction; 2E
implements and verifies that configuration. The astronomy route consumes the resulting
instantaneous `UT1-UTC`,`xp`,`yp` and does not restore them again. This configuration
handoff does not reopen the generic astronomy-core boundary.

#### Leap authority, validity, age, and coverage

Bulletin C is the leap-event announcement authority, not the runtime transport. 2D may
select a versioned official IERS machine artifact or an official IANA-distributed leap
artifact only when its transitions are checked against the applicable Bulletin C
history, its publisher integrity/validity metadata is preserved, and UFUQ records the
exact bytes and SHA-256. SOFA's compiled `dat` table and ambient ERFA state are not
production sources.

`23:59:60Z` becomes a `ValidatedUtcInstant` only when that exact positive event is in
the active approved artifact and within its approved validity scope. A missing,
inconsistent, unverified, expired-for-the-request, or unapproved leap artifact fails
closed. If an authority announces a negative leap, V1 requires a new versioned grammar/
validation decision before activating dates affected by it; it does not guess.

Acquisition age, publisher expiry/valid-through metadata, scientific row coverage,
source quality, bundle activation, and scientific approval remain separate. A final
historical EOP row does not become scientifically stale merely because its bytes are
old; a newly downloaded file can still be out of range or unapproved. Leap-artifact
expiry describes source validity metadata. As a UFUQ `PROJECT_DECISION`, it limits what
the artifact may assert about later leap knowledge but does not erase an approved
historical transition for an identified replay whose requested instant lies within its
recorded approval scope. A superseded artifact cannot claim later knowledge or become a
hidden latest-file fallback. Final EOP data
uses independent field coverage and four-sample support, not a universal age expiry.
V1 defines no age-based `STALE` scientific status and copies no `auto_max_age` value.

#### Offline execution, activation, and no degradation

One explicitly supplied immutable approved bundle contains the leap/EOP records,
interpolation/restoration configuration, policy identity, source metadata, and all
SHA-256 hashes. Request execution performs no network access, automatic refresh,
cached-table discovery, ambient library-table lookup, current-time lookup, or product
substitution.

Candidate updates follow this sequence outside a request:

```text
acquire candidate
-> verify publisher integrity and UFUQ hashes
-> parse/schema validate
-> inspect each field's quality/coverage/support
-> diff values, statuses, warnings and derived domain against the active bundle
-> astronomy/data review
-> atomic activation
-> retain every prior bundle for identified replay
```

An official publication never silently replaces the active bundle. Publication
frequency does not select a polling cadence; deployment/operations may set one later.
A superseded bundle remains addressable only for an explicitly identified historical
replay under its recorded scope; it is never silently used for a new request or chosen
by wall-clock “latest file” discovery.

No degraded V1 result is reachable: no zero `UT1-UTC`, zero `xp`/`yp`, nearest row,
extrapolation, preliminary/predicted/estimate fallback, expired/unapproved fallback,
automatic field substitution, or “best effort” coordinate. Missing or unapproved
requirements return a typed non-result.

Raw product flags and scientific-routine statuses/warnings are preserved with their
source/stage/routine identity. Informational metadata may accompany a pending result.
A source-quality warning, unavailable field, out-of-coverage request, integrity/hash
failure, unapproved state, dubious/unacceptable conversion date, or any unclassified
scientific warning blocks V1 execution unless a future version explicitly allowlists
it. Normalized project meaning remains separate from transport/log severity.

#### Data/tool handoff and practicality

| Owner | Exact responsibility |
|---|---|
| Milestone 2D | Select and acquire exact official final-derived EOP and leap families/releases; retain raw bytes, publisher/product/licence metadata, source flags, per-field coverage and uncertainty, Bulletin C consistency evidence, acquisition identity, SHA-256, exact interpolation/restoration source configuration, and activation approval. |
| Milestone 2E | Implement fail-closed parsers/validators, normalized independent field records, UFUQ-selected four-point interpolation through continuous `UT1-TAI`, the pinned IERS Conventions 2010 restoration exactly once after interpolation, deterministic bundle/manifest generation, runtime lookup, canonical evidence, boundary/negative/replay tests, and no-request-network enforcement. |
| Profile activation | Derive the explicit earliest/latest whole-second UTC values from the intersection of approved leap validity, independent four-sample support for `UT1-UTC`,`xp`,`yp`, and every other approved source/model/observer/scenario constraint; record endpoint inclusion and adjacent-outside fixtures. |

The conservative final-only policy is usable: official Bulletin B archives contain
daily final `UT1-UTC`,`xp`,`yp`, so 2D can construct a nonempty bounded historical
interval whose interior has four-point support. V1 does not promise current/“now”
execution; final publication latency limits the activation endpoint rather than
silently enabling predictions. Exact artifacts, values, dates and hashes remain 2D/2E
activation data.

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
scientific state boundary under the selected transformation and leap/EOP semantic
contracts without selecting concrete catalogue/observer/operational-data values, the
activated UTC interval derived from those values, or any numerical tolerance.

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
| `REQUIRED_ARTIFACT_UNAVAILABLE` | An identified required artifact or required artifact field cannot be resolved or verified. Exact leap/EOP subtype serialization remains owned by the 2D/2E artifact contract; the scientific failure semantics are fixed here. |
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

The final leap/EOP policy refines ordering inside stages 3 and 7 among field integrity,
publisher validity, coverage/support, quality, approval, interpolation and warning
checks. No later refinement can move EOP
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

## Normative transformation route

The following `PROJECT_DECISION` is the only route production may implement for V1:

```text
CatalogueIcrsState
  -> PropagatedIcrsAstrometry

ValidatedTimeStates + ObserverPreset + ApprovedLeapState
  + RequiredEopFieldStates + PinnedModelIdentity
  -> EarthOrientationContext

PropagatedIcrsAstrometry + EarthOrientationContext
  -> ObserverAwareCirsDirection
  -> GeometricHorizontalDirection
```

This is a dependency graph, not a claim that CIRS can be constructed before its
Earth-orientation context. Each arrow creates a new immutable typed scientific state;
no frame, epoch, scale, observer, artifact, effect, warning, or approval identity is
overwritten.

The production mapping is a decomposed subset derived from the exact IAU SOFA
`2023-10-11` C semantics:

1. validate and normalize the source-neutral ICRS astrometry;
2. convert `mu_alpha_star` to the coordinate rate required by the SOFA space-motion
   boundary and execute `pmsafe`-derived propagation from approved source-epoch TDB to
   the declared J2000.0 interface `JD(TDB) 2451545.0`, preserving every status bit;
3. obtain the Earth heliocentric/barycentric position and velocity from an
   `epv00`-derived pinned simplified-VSOP2000 module, using TT exactly as the official
   `apco13` composition does and retaining the otherwise-discarded `epv00` status;
4. form model CIP/CIO and the bias-precession-nutation matrix with `pnm06a`, `bpn2xy`,
   `s06`, and `c2ixys`-derived semantics; compute ERA from UT1 and the TIO locator
   `s'` from TT;
5. convert the explicit declared observer ellipsoid/ellipsoidal height to geocentric
   position with `gd2gce`-derived semantics, then form the observer position/velocity
   with the polar-motion/ERA part of `pvtob`; a non-ellipsoidal height must already
   have an approved provenance-bearing conversion;
6. build an `apco`/`apcs`-derived observer astrometry context from the caller-supplied
   ephemeris, model CIP/CIO, ERA, `xp`,`yp`, observer state, and explicit no-refraction
   policy; observer velocity is included in the astrometric aberration context and the
   later local `diurab` term is explicitly disabled as redundant, matching `apco`;
7. execute the `atciq`-derived ICRS-to-CIRS stage with proper motion, parallax,
   radial velocity, solar deflection, annual plus observer-velocity/diurnal aberration,
   and the model BPN matrix; and
8. execute only the geometric part of the `atioq`-derived CIRS-to-local stage: Earth
   rotation, polar motion, ENU direction, signed altitude, and north-zero/eastward-
   positive azimuth state. It must not reapply diurnal aberration. The refraction
   calculation and its numerical guards are not in V1.

The high-level `apco13`/`atco13` routines remain reference/composed-consistency
surfaces, not the production policy boundary. They assume WGS 84 site coordinates,
consult their compiled leap-second state, accept atmosphere inputs, provide no
`dX`,`dY` input, and discard the `epv00` status. The lower-level mapping prevents
those conveniences from becoming hidden UFUQ assumptions.

### Proper-motion and source-epoch adapter

The normalized runtime field is `mu_alpha_star`, not `dRA/dt`. Away from the exact
celestial pole the route computes:

```text
dRA/dt = mu_alpha_star / cos(dec)
```

after explicit unit and derivative-time-scale conversion. Dec proper motion maps as
the coordinate rate after the same approved scale/unit conversion. At exact
declination `+/-90 deg`, RA and its coordinate rate are singular, so the row is
`UNSUPPORTED_PROFILE_DOMAIN`; the implementation must not divide by zero. No
near-pole epsilon is selected. Finite near-pole cases retain a conditioning/status
record and remain subject to postimplementation domain/tolerance review.

The `pmsafe`-derived boundary consumes two-part TDB epochs and rates per TDB Julian
year. A source with an unspecified epoch or derivative time scale is ineligible. A
nonzero `pmsafe` warning status is preserved and fails V1 closed unless a future
profile-specific allowlist explicitly approves that status. In particular, status 1
would mean the routine overrode the supplied distance, which V1 forbids as a hidden
substitute.

### Parallax and radial velocity

Every V1 row requires an `APPROVED_USABLE_DISTANCE` state. It may contain a finite
positive measured parallax or a finite positive distance converted to parallax under
an approved, versioned conversion with propagated provenance. A raw zero or negative
catalogue parallax remains valid source evidence but is not a usable physical distance
for V1. Missing, non-finite, unapproved, or quality-ineligible parallax/distance makes
that row ineligible; it is never changed to zero, an arbitrary finite distance, or an
implicit infinite-distance branch.

Every V1 row also requires an approved finite radial velocity with the explicit SOFA
sign convention (positive when receding), unit, reference semantics, uncertainty, and
provenance. An authoritative value may numerically be zero; absence must never be
represented by zero. Missing or unapproved radial velocity makes the row ineligible.
This makes perspective motion part of the required straight-line space-motion model
rather than an unbounded silent omission. A distant-source/no-RV branch is deferred to
a later profile and would require its own omission evidence and review.

These requirements do not make I/311 permanent or block generic astronomy-core. If
2D retains I/311, its unresolved epoch/derivative scale and absent RV make affected
rows ineligible until an authoritative crossmatch/interpretation is approved. 2D may
select another release or crossmatch under the source-neutral contract.

### Ephemeris/model ownership

V1 pins the Earth/Sun model to the SOFA `2023-10-11` `epv00` simplified VSOP2000
semantics and coefficient set. It supplies Earth barycentric position/velocity and
Earth heliocentric position, from which the observer barycentric velocity, annual
aberration, and solar-deflection direction are constructed. It requires no external
ephemeris file, network request, cache, or hidden refresh. The model issue, originating
file/hash, coefficient identity, time argument, and status are part of every algorithm
manifest/result provenance.

SOFA documents a warning outside 1900-2100 for `epv00`; that external model-status
limit is not itself UFUQ's activated date range or a tolerance. Profile activation
must intersect the eventual supported domain with model status/coverage and V1 fails
closed on a nonzero `epv00` status unless a later reviewed policy says otherwise. No
other gravitating-body ephemeris is needed because multiple-body deflection is deferred.

### Effect disposition matrix

`INCLUDED_V1` means the named deterministic model term is part of every successful V1
route. `UNAVAILABLE_INPUT_FAILS_CLOSED` means the effect is also required, but its
approved source/operational input can be unavailable and then no geometric result is
fabricated. `EXPLICITLY_OMITTED_V1` and `DEFERRED_LATER_PROFILE` never mean zero
uncertainty.

| Effect | V1 disposition | Authority and exact route/input | Consequence and error-budget disposition |
|---|---|---|---|
| Catalogue epoch propagation | `UNAVAILABLE_INPUT_FAILS_CLOSED` | SOFA `pmsafe`-derived straight-line space motion from approved source TDB epoch to declared J2000.0 TDB interface. | Missing/unknown epoch scale blocks only the row. `A-006`,`B-001`,`B-002`; source uncertainty remains 2D and propagation disagreement postimplementation. |
| Proper motion in RA | `UNAVAILABLE_INPUT_FAILS_CLOSED` | Source `mu_alpha_star`; explicit division by `cos(dec)` only for the SOFA coordinate-rate boundary; TDB Julian-year scale. | Missing/unknown derivative semantics or exact-pole singularity blocks the row. `A-002`,`A-006`,`B-002`,`F-003`,`F-004`. |
| Proper motion in Dec | `UNAVAILABLE_INPUT_FAILS_CLOSED` | Explicit Dec coordinate rate with approved units/scale. | Missing/unknown derivative semantics blocks the row. `A-002`,`A-006`,`B-002`. |
| Parallax/topocentric parallax | `UNAVAILABLE_INPUT_FAILS_CLOSED` | Positive approved parallax/equivalent distance enters `pmsafe`/`atciq`-derived observer-aware propagation. | Zero/negative/missing/unapproved distance makes row ineligible; no infinite-distance substitute. `A-003`,`B-008`. |
| Radial velocity/perspective effects | `UNAVAILABLE_INPUT_FAILS_CLOSED` | Approved finite RV, positive receding, enters full space motion. | Missing/unapproved RV makes row ineligible; no `0 km/s` substitute. `A-004`,`B-002`. |
| Frame bias | `INCLUDED_V1` | SOFA `pnm06a`/CIO-family BPN semantics. | Model/implementation uncertainty remains unbounded for later validation. `B-003`,`B-009`. |
| IAU 2006 precession | `INCLUDED_V1` | IAU 2006 precession through SOFA `pnm06a` semantics. | No omission; model/implementation term remains unbounded. `B-004`,`B-009`. |
| IAU 2000A nutation | `INCLUDED_V1` | IAU 2000A nutation plus the matching transformation used with IAU 2006 precession; never called “IAU 2006A nutation.” | No omission; model/implementation term remains unbounded. `B-004`,`B-009`. |
| Annual aberration | `INCLUDED_V1` | Earth barycentric velocity from `epv00` supplies the annual component of the combined `apcs`/`atciq`-derived aberration context. | No omission; ephemeris/model and implementation terms remain unbounded. `B-005`,`B-009`. |
| Solar gravitational deflection | `INCLUDED_V1` | `ldsun`-derived solar-only deflection using the pinned Earth/Sun model. | No omission; elongation/model term remains unbounded. `B-006`,`B-009`. |
| Extra-body gravitational deflection | `DEFERRED_LATER_PROFILE` | SOFA `atciqn` demonstrates a controlled later route but V1 supplies no body list/ephemerides. | Planet-dependent direction bias is unbounded and scenario dependent; later ablation/approval required. It does not block explicitly solar-only pending-validation V1. `B-007`. |
| Earth rotation | `UNAVAILABLE_INPUT_FAILS_CLOSED` | ERA from typed UT1; approved `UT1-UTC` is required and UTC is never substituted. | Missing/unapproved field blocks calculation. `C-002`,`C-007`,`C-008`,`C-009`. |
| Polar motion `xp` | `UNAVAILABLE_INPUT_FAILS_CLOSED` | Explicit independently approved `xp` field in observer/context construction. | Missing/unapproved field blocks calculation; zero is not a fallback. `C-003`,`C-007`,`C-008`,`C-009`. |
| Polar motion `yp` | `UNAVAILABLE_INPUT_FAILS_CLOSED` | Explicit independently approved `yp` field in observer/context construction. | Missing/unapproved field blocks calculation; zero is not a fallback. `C-004`,`C-007`,`C-008`,`C-009`. |
| Observed celestial-pole offset `dX` | `EXPLICITLY_OMITTED_V1` | V1 uses uncorrected model CIP X/Y from the IAU 2006/2000A matrix; no `dX` input is read. | Difference between observed and model CIP can perturb the direction; no bound is claimed. It is a later-profile uncertainty, not zero. `C-005`. |
| Observed celestial-pole offset `dY` | `EXPLICITLY_OMITTED_V1` | Same model-CIP-only route; no `dY` input is read. | Same unbounded later-profile consequence, correlated with `dX`. `C-006`. |
| Diurnal aberration | `INCLUDED_V1` | The station-rotation velocity component is included exactly once through the explicit observer velocity in the combined `apcs`/`atciq`-derived aberration context; the later `atioq`-derived `diurab` term is zero/disabled as redundant, matching SOFA `apco`. | No omission; double application is prohibited and the observer/implementation interaction remains unbounded. `B-008`,`B-009`. |
| Observer geodetic position/height | `UNAVAILABLE_INPUT_FAILS_CLOSED` | Approved `ObserverPreset`; explicit ellipsoid and ellipsoidal height enter `gd2gce`/`pvtob`-derived context. | Missing/unapproved/incompatible observer state blocks real execution; no WGS 84, `(0,0)`, or zero-height default. `D-001`-`D-006`. |
| Atmospheric refraction | `EXPLICITLY_OMITTED_V1` | Profile fixes `REFRACTION_NOT_REQUESTED`; production skips `refco` and the refraction section/guards of `atioq`. | Geometric and apparent altitude can differ, especially near the horizon; all model/meteorology/domain terms remain deferred and unbounded. `E-001`-`E-007`. |

### Production implementation strategy

The selected strategy is a UFUQ-owned pure-TypeScript implementation of only the
approved SOFA-derived subset. It imports no production data or Python/reference code,
performs no I/O, and accepts every source/time/observer/EOP value as an explicit typed
argument. Each derived module must use UFUQ names, cite the exact SOFA source
issue/file/hash, describe all differences, preserve applicable SOFA licence terms,
and carry an explicit statement that it is derived from SOFA but is neither
SOFA/IAU-provided nor SOFA/IAU-endorsed software.

The freshness audit is recorded in
`docs/references/studies/typescript-astronomy-production-candidates.md`. No current
third-party package matches the route and status/data boundary. `astronomy-engine` and
`astronomia` use different/approximate model families; `@observerly/astrometry`
declares itself pre-production; `@tsastro/tsofa` tracks SOFA `2021-05-12`, embeds leap
state, and drops the `pmsafe` warning bitmask. Native ERFA or official SOFA C compiled
to WebAssembly remains a viable fallback if the owned route proves unmaintainable, but
it adds a binary toolchain/loader boundary and does not strengthen scientific lineage
independence.

Production and `tools/astronomy-reference` are code/dependency independent. They are
not scientifically lineage independent: a SOFA-derived TypeScript implementation
compared with Astropy/PyERFA/ERFA is
`SHARED_SCIENTIFIC_LINEAGE_IMPLEMENTATION_VERIFICATION`. A later lineage-audited
NOVAS or other oracle is `STRONGER_INDEPENDENT_VALIDATION`.

### Runtime scientific artifact

V1 selects **catalogue-reference astrometry propagated at runtime**. The deterministic
2E runtime artifact must carry:

- schema/profile/data-manifest IDs and hashes;
- stable UFUQ `starId` plus source-release/crosswalk identity;
- ICRS RA/Dec with units and approved source epoch representation/scale;
- explicit `mu_alpha_star`, Dec proper motion, units, duration, and derivative scale;
- positive approved parallax/equivalent-distance state and conversion provenance;
- approved radial velocity, sign convention, units, and provenance;
- uncertainties/covariance, source quality, eligibility/approval, and omission states;
- source row/release/licence/provenance and deterministic artifact identity.

The astronomy implementation never parses raw catalogue files. Precomputed
scenario-time directions may exist later as derived fixtures/caches with complete
input/profile/model/EOP hashes, but they are not catalogue authority and cannot replace
runtime propagation in V1.

### Experiment and tolerance boundary

No unrun experiment is required to choose this semantic route. Batch 01 supports only
the exact convention/status/determinism guards and same-family route consistency it
actually executed. Effect ablation/interactions, observer/parallax/RV sensitivity,
source-derived cases, production/reference residuals, supported-domain partitions,
and stronger-independent comparisons remain postimplementation or later-profile work.
No measurement-only record becomes a tolerance or approval.

## Exact remaining preimplementation blockers

There are **zero** genuine Milestone 2C preimplementation blockers. The leap/EOP
policy above closes the final semantic cluster without selecting production bytes or a
date range. Milestone 2C is ready to close as permission to implement
`ScientificProfileV1`; it is not permission to execute real data or claim scientific
acceptance.

Exact catalogue/observer/leap/EOP artifacts and activated bounds remain 2D/2E data
gates. Production/reference residuals, implementation error, error-budget population,
numerical tolerance and named scientific acceptance remain postimplementation gates.
No arbitrary-location policy, atmosphere model, visibility model, scene behavior,
learner policy, or fully bounded 49-term ledger belongs in the preimplementation list.

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
| Source-neutral proper-motion adapter, polar guard, missing-state and warning ownership | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved: explicit `mu_alpha_star` adapter, exact-pole rejection, no arbitrary near-pole epsilon, raw-status preservation, and fail-closed nonzero-status policy are normative. |
| Radial-velocity source/crossmatch and selected-row evidence | `B BLOCKS_2D_DATA_AUTHORITY` | 2D must supply an authoritative value or mark the row ineligible. |
| Radial-velocity/perspective missing-state branch | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved: an approved finite RV is mandatory for each V1 row; absence makes the row ineligible and is never `0 km/s`. |
| Parallax/distance row quality, uncertainty and covariance | `B BLOCKS_2D_DATA_AUTHORITY` | Controls selected-row eligibility in 2D. |
| Parallax/distance admissibility and unavailable branch | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved: every V1 row needs a positive approved parallax/equivalent-distance state; zero/negative/missing/unapproved values make the row ineligible. |
| Transformation route, TypeScript mapping and effect ownership | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved as the decomposed SOFA `2023-10-11`-derived pure-TypeScript route, model-CIP-only EOP input set, explicit effect matrix, and pending-validation lifecycle. |
| Leap/EOP product classes, per-field quality/interpolation and offline/fail policy | `F NOT_REQUIRED_FOR_PROFILE_V1` | Resolved: V1 is final-only and field-independent; it selects Gazette's four-point example/full support and TN36-2010 exactly-once restoration; it is immutable-offline and fail-closed. |
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
| `2C-008` | F | V1 route, pure-TypeScript mapping, effect dispositions, required row states, ephemeris, and EOP field interface are normative. |
| `2C-009` | F | V1 final-only leap/EOP semantics, interpolation/restoration family and fail-closed input policy are normative; bytes/hashes and exact source configuration are B. |
| `2C-010` | D | Refraction model questions move later once geometric-only V1 is approved. |
| `2C-011` | D | Physical/terrain/visibility aggregation is excluded; learner parts are secondarily E. |
| `2C-012` | F | Semantic outcomes, precedence, exact singularity behavior, warning/status preservation, and pending-versus-approved validation states are normative. A numerical ill-conditioned boundary and wire/HTTP mapping remain later without reopening the semantic contract. |
| `2C-013` | C | Numerical error budgets and thresholds govern postimplementation acceptance. |
| `2C-014` | C | Production/reference comparison requires production; the preimplementation protocol/environment already exists. |
| `2C-015` | F | The bounded-domain shape, explicit endpoint semantics and no-extrapolation behavior are normative; actual UTC bounds are a B activation artifact and broader dates remain D. |
| `AST-001` | B | Catalogue authority, rights, provenance, row quality, and allowlist belong to 2D. |
| `AST-002` | E | Arabic/Najdi names, membership, relationships, and lesson approval do not block astronomy-core. |
| `AST-003` | F | The preimplementation route/effect/input and leap/EOP policy mapping is resolved. Exact source/artifact activation remains B and residuals/tolerances remain C; neither reopens the generic route. |
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
| `AST-SRC-004` | B | The offline/final-only/interpolation/update policy is resolved; exact acquired EOP/leap bytes, configuration and activation authority remain data work. |
| `AST-SRC-005` | D | Refraction is excluded from V1. |
| `AST-SRC-006` | B | Domain/endpoint semantics are resolved; actual bounds are derived and approved at 2D/2E activation from concrete coverage. |
| `AST-SRC-007` | B | UTC grammar, conditional leap validation, transport requirements and validity/update policy are resolved; exact acquired transport bytes and activation evidence remain data work. |
| `AST-SRC-008` | F | Qibla geodesy is outside this profile. |
| `AST-SRC-009` | B | Controls I/311 eligibility only. |
| `AST-SRC-010` | F | Route/effect/production mapping is resolved and no longer a ProfileV1 gap; production comparison, omission measurement, and tolerance evidence are secondary C obligations. |
| `AST-SRC-011` | B | Source scale/RV authority controls row eligibility; the generic branch is resolved by requiring approved epoch/derivative/distance/RV states. |
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
six tolerance classes `BLOCKED`, and `FINAL_TOLERANCE_NOT_JUSTIFIED`. Closing the
leap/EOP semantic policy changes lifecycle ownership, not a term's numerical bound or
approval state.

| Primary category | Ledger IDs | Count | Profile interpretation |
|---|---|---:|---|
| A | None | 0 | No remaining preimplementation semantic term. |
| B | `A-001`-`A-006`, `B-001`, `C-001`-`C-004`, `C-007`-`C-009`, `D-001`-`D-006` | 20 | Catalogue/source eligibility, concrete observer records, exact leap/EOP artifacts/field evidence/interpolation configuration and supported-domain activation move to 2D/2E. Their uncertainty remains unbounded; data selection does not approve a numerical bound. |
| C | `B-002`-`B-006`, `B-008`, `B-009`, `F-001`, `F-005`, `F-006` | 10 | Space-motion/model/route implementation effects, production floating-point/reference disagreement, and production determinism require code. `F-005` includes code-independent production/reference measurement plus any stronger lineage-independent evidence required by the claim; it does not label Astropy/ERFA agreement independent. `F-006` is already satisfied for Batch evidence transport only. |
| D | `B-007`, `C-005`, `C-006`, `E-001`-`E-007`, `G-001`-`G-003` | 13 | Multiple-body deflection, observed CPO, refraction, and scene/render terms remain explicitly unresolved because the profile excludes those capabilities. Their dispositions revert to A or C only if a later profile includes them. |
| E | `H-001`-`H-003` | 3 | Scenario, learner-interaction, and scoring tolerances remain outside astronomy accuracy. |
| F | `F-002`-`F-004` | 3 | These exact contract guards are already established for the preimplementation boundary. Future production code must retain them, but no unresolved scientific magnitude or policy is assigned to them. |
| **Total** | `A-001` through `H-003` | **49** | Each stable ID appears exactly once. |

Unresolved terms are never encoded as zero, machine epsilon, test epsilon, display
precision, a library default, or an omitted ledger row. G/H cannot loosen A-F.

The Earth-orientation/time terms retain these secondary evidence obligations without
changing their ledger values or primary lifecycle category:

| Ledger terms | Current semantic disposition | Evidence still required |
|---|---|---|
| `C-001` | Leap authority/transport/validity and fail-closed behavior are fixed; exact transport is 2D data. | Selected artifact evidence and postimplementation UTC-conversion verification; the numerical uncertainty remains unbounded. |
| `C-002`-`C-004` | `UT1-UTC`,`xp`,`yp` are final-only, field-independent required inputs. | 2D source values/declared uncertainties and support; 2E interpolation evidence; postimplementation directional sensitivity and numerical acceptance. |
| `C-007` | Quality disposition is fixed: only independently approved `FINAL` is eligible. | 2D source group flags where the product groups quantities, independently normalized field provenance/approval, and later quantitative assessment; the rejected classes are not assigned zero effect. |
| `C-008` | UFUQ-selected four-point support, leap-aware `UT1-TAI`, exactly-once TN36-2010 restoration, offline update/activation and no-fallback semantics are fixed. | 2D exact source/configuration, 2E implementation verification, and later interpolation/implementation-error bounds. |
| `C-009` | Domain-intersection and endpoint semantics are fixed. | 2D/2E concrete coverage intersection and boundary fixtures; later supported-domain acceptance. |
| `C-005`,`C-006` | Observed `dX`,`dY` are excluded from V1. | Their unbounded terms remain later-profile uncertainty, not zero and not V1 input. |

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
| Production astronomy could not start until 2C closed. | Generic bounded astronomy-core types and algorithms may start after this 2C specification gate. Real-data execution, data-backed fixtures, and profile activation additionally require eligible 2D/2E artifacts. |
| 2C closure required production/reference residuals. | Residuals are POST_IMPLEMENTATION and activate `test:reference`. |
| 2C closure required final scientific/reference tolerances. | Tolerances gate scientific acceptance/release after implementation evidence exists. |
| Every required error-budget term had to be bounded before 2C closed. | Terms stay explicit and unresolved; excluded terms are D, data terms B, implementation terms C, and downstream terms E. |
| Full refraction/visibility/global-location policy blocked the first implementation. | V1 disables or defers these capabilities and preserves typed extension points. |

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

Milestone 2D selects and activates the actual catalogue/release, acquisition and
deployment rights, row quality/uncertainty, minimal star allowlist, crosswalk, and
artifact provenance. Its 2D.1 release-level audit prefers fixed Gaia DR3 version 1.1,
but its bounded official TAP screen approves no source row. Immutable acquisition,
component identity, parallax systematics, applicable covariance, component-specific RV
proxy/systemic suitability, quality, and the Polaris fallback remain open. The
scale-aware TCB-to-TDB parameter/covariance map is closed by Milestone 2D.1A without
approving any row.
I/311 remains a studied spike only.
Reviewed source records may coexist or be replaced through the internal `starId` and
per-field authority model without changing cultural claims or copying coordinates into
them.

Missing Najdi/regional evidence does not block astronomy-core. No content may be
labelled `NAJDI_TRADITION` without claim-level regional evidence and named human
review. Arabic labels, membership, guidance relationships, line segments, and lesson
eligibility remain separate E-category gates.

## Resource status

| Resource | Status | Use and limit |
|---|---|---|
| IAU SOFA `2023-10-11` source/manual | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Current official algorithm/routine authority for preimplementation semantics; does not select UFUQ code or policy. |
| Current TypeScript/JavaScript production-candidate audit | `OFFICIAL_WEB_SUFFICIENT` | Official npm/GitHub/release/licence evidence is recorded in `typescript-astronomy-production-candidates.md`. No package matches V1's exact route/status/data boundary; no package installation is required. |
| UFUQ-owned SOFA-derived TypeScript subset | `ALREADY_AVAILABLE_AND_SUFFICIENT` | The existing local SOFA issue/manual/source plus official licence are sufficient to specify and start the bounded implementation. Future source files must record derivation/differences/attribution and preserve statuses. |
| ERFA or official SOFA C-to-WebAssembly fallback | `REQUIRED_LATER` | Reconsider only if the selected owned TypeScript subset proves unmaintainable; a fallback requires its own pinned build, binary reproducibility, adapter and architecture review. |
| IERS Conventions 2010 / TN36 | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Official registered baseline; corrected working material remains separately classified. |
| IERS Gazette 13, C04 guide, TN36 Chapters 5/8, and Bulletin A/B explanatory material | `OFFICIAL_WEB_SUFFICIENT` | Official guidance is sufficient to separate Gazette's four-point example/equivalent allowance, continuous `UT1-TAI`, and the governing 2010 restoration families. 2D still pins the exact source/configuration bytes used by 2E. |
| RFC 3339 official record | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Defines the broader Internet timestamp grammar and conditional leap-second representation. It does not require UFUQ's whole-second Z-only subset or select supported dates. |
| Astropy `8.0.1` and locked reference environment | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Candidate reference path only. |
| PyERFA `2.0.1.5` release/source pin | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient for frozen synthetic evidence. Version-matched documentation/tagged-source review and reviewer acceptance remain a later prerequisite for postimplementation reference-validation claims; PyERFA cannot supply the stronger independent oracle. |
| IERS Bulletin A/B/C and `finals2000A` documentation | `OFFICIAL_WEB_SUFFICIENT` | Defines products/fields/quality roles. UFUQ's final-only decision is a project policy; exact bytes and dates remain 2D. |
| IANA versioned leap artifacts | `OFFICIAL_WEB_SUFFICIENT` | Eligible machine-transport family with publisher validity metadata; IERS Bulletin C remains event authority and 2D selects exact bytes. |
| CDS I/311 ReadMe/Appendix G/unit standard and ESA I/311 epoch page | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient for known fields and Julian representation, not time scale, rights, row suitability, or permanent source selection. |
| ESA Gaia DR3 release documentation/archive and bounded TAP screen | `OFFICIAL_WEB_SUFFICIENT` for release semantics and preliminary screening only | Sufficient to prefer version 1.1 and preliminarily report 8/19 matches, five finite-RV candidates and no Polaris match. It does not approve a row or derived-artifact rights: exact query/result authority, immutable acquisition, scientific review and rights interpretation remain 2D work. |
| Exact Gaia TCB-to-TDB stellar-parameter/covariance adapter | `ALREADY_AVAILABLE_AND_SUFFICIENT` | IAU/Gaia/Klioner/Lindegren-Dravins and pinned SOFA evidence support `GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1`; implementation/residual validation remains later. |
| Polaris fallback and row-specific RV proxy | `HUMAN_REVIEW_REQUIRED` | Named astronomy/data review must approve the physical component and exact field authorities. No new PDF is needed for the generic adapter. |
| Official UMPSA Faculty/Pekan site-identity pages | `OFFICIAL_WEB_SUFFICIENT` | Establish the selected Faculty-at-Pekan identity only; they supply no approved geodetic value or accuracy. |
| JUPEM geodetic product/service documentation | `OFFICIAL_WEB_SUFFICIENT` | Establishes available GPS-control, coordinate-transformation, geoid and GNSS/RINEX services. It does not prove a Faculty-specific control record exists or make survey control mandatory. |
| Exact UMPSA observer-preset data record | `USER_ACTION_REQUIRED_BEFORE_2D` | Required before 2D can approve the concrete preset and before real V1 execution, not before 2C closes or generic astronomy-core is written. |
| JUPEM survey-control record for the Faculty site | `NOT_NEEDED` | Optional evidence if site-matched and proportionate; no control monument is a profile requirement. |
| Future `Riyadh, Saudi Arabia` preset record | `REQUIRED_LATER` | Uses the same generic contract in a later multi-location profile; no coordinates are needed now. |
| I/311 epoch/derivative-scale authority | `REQUIRED_LATER` only if I/311 is reconsidered | The 2D.1 preferred path does not select I/311, so no clarification is needed for Gaia evaluation. |
| I/311 raw/derived deployment permission | `REQUIRED_LATER` only if I/311 is reconsidered | The 2D.1 preferred path does not deploy I/311-derived records. |
| Per-row catalogue acquisition, quality, uncertainty, and covariance evidence | `HUMAN_REVIEW_REQUIRED` | 2D scientific/data review; no new general astronomy book required. |
| Exact production leap/EOP artifacts and activation record | `REQUIRED_LATER` | 2D selects/acquires official bytes, hashes, exact interpolation/restoration configuration and review evidence before real execution. No user download is needed to close 2C or start generic implementation. |
| USNO NOVAS 3.1 software and official guides | `REQUIRED_LATER` | Candidate stronger independent oracle after production exists. |
| Replacement Explanatory Supplement PDF | `NOT_NEEDED` | SOFA/IERS already supply the authority needed for this profile. |
| *Fundamental Astronomy*, 6th ed. | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Explanatory support only; cannot override standards or data authority. |
| Najdi/regional claim source | `USER_ACTION_REQUIRED_BEFORE_PHASE2` | Conditional on making a Najdi learner-facing claim; does not block astronomy-core. |
| Rashid al-Khalawi critical edition/treatment | `USER_ACTION_REQUIRED_BEFORE_PHASE2` | Conditional on using that material. |
| Named Arabic/cultural/education review | `HUMAN_REVIEW_REQUIRED` | Learner-facing content only. |
| WCAG 2.2 / WAI-ARIA APG | `OFFICIAL_WEB_SUFFICIENT` | Later UI/accessibility work, not a 2C science resource. |
| Restricted local FYP report | `NOT_NEEDED` | It is not external scientific authority and remains private. |

**Current lifecycle update:** no user action was needed to close 2C. Milestone 2D.1 has
completed a small ephemeral official Gaia DR3 screen and now requires immutable
acquisition plus scientific review; it does not require a bulk catalogue, new astronomy
PDF/manual, installed third-party astronomy package, Riyadh record, or NOVAS package.

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

### REQUIRED_LATER only if I/311 is reconsidered: time-scale clarification

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

### REQUIRED_LATER only if I/311 is reconsidered: deployment rights

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

**Final status:** `LEAP_EOP_POLICY_BLOCKER_CLOSED` and
`MILESTONE_2C_READY_TO_CLOSE_FOR_IMPLEMENTATION`. This is implementation-entry
permission only; all B/C/D/E lifecycle gates remain enforceable at their recorded
stages. The frozen 2C.5A experiment protocol retains its historical checkpoint phrase
that Milestone 2C was open; immutability makes that evidence provenance, not the
current milestone verdict.
