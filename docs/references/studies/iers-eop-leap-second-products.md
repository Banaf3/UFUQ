# IERS EOP and leap-second product documentation

## Scope and identity

- Source IDs: `IERS-BULLETIN-A`, `IERS-BULLETIN-B`, `IERS-BULLETIN-C`,
  `IERS-FINALS2000A-FORMAT`, `IERS-GAZETTE-13`, `IERS-C04-GUIDE`,
  `IERS-TN36-2010`, `RFC3339-TIMESTAMP`, and `IANA-TZDB-LEAPS`.
- Retrieval dates: original product audit 2026-08-03; official interpolation and
  leap-transport validity recheck 2026-08-13.
- Scope: official product roles and fields needed to specify UFUQ's Earth-orientation,
  leap-second, time-input, update, offline, and degraded-data policies.
- Out of scope: choosing a production artifact, inventing a supported date interval,
  accepting predicted data, or assigning a numerical tolerance.

## Primary-authority findings

| Authority | Source-supported fact | UFUQ limit |
|---|---|---|
| [IERS Bulletin A metadata](https://datacenter.iers.org/productMetadata.php?id=6) | Bulletin A contains daily `x`, `y`, and `UT1-UTC` estimates and errors, predictions for up to 365 days, and `dX`,`dY` celestial-pole offsets from 2003. It is published weekly by the IERS Rapid Service/Prediction Centre. | The product's existence and coverage description do not approve predictive rows, a particular downloaded file, or UFUQ's update cadence. |
| [IERS `finals2000A` format](https://maia.usno.navy.mil/ser7/readme.finals2000A) | MJD is labelled UTC. Separate `I`/`P` flags identify IERS/prediction values for polar motion, `UT1-UTC`, and nutation offsets. Bulletin A and Bulletin B fields occupy distinct columns. | A row is not wholly IERS-estimate or final merely because one field has that quality; source quality must be retained per required field and kept separate from availability and UFUQ approval. Blank or absent fields are unavailable, not zero. |
| [IERS Rapid Service/Prediction Centre](https://www.iers.org/iers/en/organization/productcentres/rapidservicepredictioncentre/rapid) | The IAU 2000 `finals.all` product carries polar motion, `UT1-UTC`, length of day, and `dX`,`dY` since 1973 and includes one year of predictions; the weekly and daily products have different extents. | The live extent moves with each release. It cannot be copied into a timeless project-supported range. |
| [IERS Bulletin B metadata](https://datacenter.iers.org/productMetadata.php?id=207) | Bulletin B provides monthly Earth-orientation information. Section 1 includes daily final `x`,`y`,`UT1-UTC`,`dX`,`dY` values for one month and preliminary values for one month, with uncertainties. | "Preliminary" and "final" remain distinct source-quality/provenance classes. The metadata does not define a UFUQ stale threshold or scientific approval. |
| [IERS Bulletin C metadata](https://datacenter.iers.org/productMetadata.php?id=16) | Bulletin C announces leap seconds in UTC or confirms no step at the next opportunity and is issued every six months. IERS is responsible for deciding when a leap second is introduced. | Bulletin C is announcement authority; the production machine-readable transport and refresh procedure still require selection and hashing. |
| [IERS Gazette 13](https://maia.usno.navy.mil/information/iers-gaz13.txt) and the [IERS Bulletin A/B explanatory material](https://hpiers.obspm.fr/iers/bul/bulb/explanatory.html) | Daily IERS polar-motion and UT1 products omit diurnal and semidiurnal variations. Gazette 13 recommends its Lagrangian interpolation-and-restoration procedure; its published `LAGINT` example uses four data points and its driver requires support on both sides. The Gazette explicitly permits an equivalent interpolation scheme. The explanatory material likewise says to add modeled subdaily terms after interpolation. | Four points are the Gazette's example, not an IERS mandate excluding equivalent methods. UFUQ's exact four-point choice and stricter support rule are project decisions. The Gazette's historical eight-term `RAY` routine is official historical IERS guidance, not the complete IERS Conventions 2010 restoration or part of the registered TN36 distribution. |
| [IERS Conventions (2010), TN36](https://iers-conventions.obspm.fr/conventions/content/tn36.pdf), Chapter 5 Sections 5.5.1 and 5.5.3 and Chapter 8 Section 8.2 | Interpolate the reported daily EOP first, then add the omitted subdaily terms. For `xp`,`yp`, the 2010 baseline adds the Chapter 8 ocean-tide terms and the diurnal polar-motion libration terms of Chapter 5 Table 5.1a; for UT1 it adds the Chapter 8 ocean-tide terms and the semidiurnal UT1 libration terms of Table 5.1b. Long-period and secular polar-motion libration are already in the reported observations and are not added again. | V1 must identify and apply these 2010 model families exactly once. `ORTHO_EOP`/`CNMTX`, `PMSDNUT2`, and `UTLIBR` identify the baseline routine families; exact source/coefficient bytes, dependencies, product-regularization compatibility, and any later working correction remain separate 2D/2E pins. The old Gazette `RAY` routine is not silently substituted. |
| [IERS C04 guide](https://hpiers.obspm.fr/eoppc/eop/eopc04_14/C04.guide.pdf) | The Earth Orientation Centre converts discontinuous `UT1-UTC` series to continuous `UT1-TAI` before numerical treatment and translates the result back afterward because leap-second jumps are unsuitable for numerical treatment. | This is official product-centre guidance, not part of registered TN36. UFUQ's exact sample-by-sample conversion and target-instant reconstruction are a project decision recorded below. |
| [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html), Sections 5.6-5.8 | The Internet timestamp profile uses a four-digit Gregorian date, `T`, time through seconds, optional fractional seconds, and a required `Z` or numeric UTC offset. A positive leap second can use second `60` only at its valid instant; `-00:00` has different semantics from known UTC. | RFC 3339 permits choices that UFUQ can narrow. It does not validate a claimed leap second against a current IERS table or define scientific precision. |
| [IANA tzdb 2026b archive](https://data.iana.org/time-zones/tzdb-2026b/) | The versioned release directory contains `leap-seconds.list` and `leapseconds` artifacts. | This records an official candidate transport only. No IANA artifact/version/hash is selected for production by Milestone 2C.3. IERS Bulletin C remains the event authority. |
| [IANA-distributed `leap-seconds.list`](https://data.iana.org/time-zones/tzdb/leap-seconds.list) | The machine-readable file identifies its last update, an explicit expiration instant, cumulative `TAI-UTC` transitions, its Bulletin C lineage, and an integrity code. IANA documents that this NTP-format file is maintained by IERS and distributed with tzdb. | The source states file validity metadata but does not define UFUQ replay semantics. UFUQ's future-knowledge and historical-replay treatment is a project decision; UFUQ also supplies its own SHA-256, scoped approval, and exact release identity. |

Every middle-column statement in this table is `SOURCE_SUPPORTED_FACT`. The last
column states a limit or a separately labelled UFUQ decision and prevents source
description from being promoted into project policy.

## Official Astropy reference behaviour

The official Astropy `8.0.1` documentation remains reference-library documentation,
not production authority:

- [IERS data access](https://docs.astropy.org/en/stable/utils/iers.html) describes
  IERS-A as weekly data with historical and predictive portions, IERS-B as monthly
  data, automatic download/cache behaviour, and the warning/error controls for
  degraded accuracy. It also warns that out-of-range access can use nearest values in
  some configurations and that disabling age checks can produce inaccurate answers.
- [`LeapSeconds`](https://docs.astropy.org/en/stable/api/astropy.utils.iers.LeapSeconds.html)
  can read IERS `Leap_Second.dat`, IETF/NTP `leap-seconds.list`, or ERFA's table. It
  exposes the table expiration, can warn and return the newest expired table, and can
  extend ERFA's leap-second table.
- [`EarthLocation`](https://docs.astropy.org/en/stable/api/astropy.coordinates.EarthLocation.html)
  accepts east-positive geodetic longitude, latitude, height above a named reference
  ellipsoid, and defaults to WGS 84. That default is a reference-path behaviour, not a
  UFUQ observer-policy decision.
- [`Time`](https://docs.astropy.org/en/stable/time/index.html) distinguishes
  representation from scale, represents instants as two-part Julian Dates, and makes
  UTC/TAI/TT/UT1 conversions explicit. Its string-output precision setting is not an
  input-acceptance or UFUQ accuracy policy.

These are `SOURCE_SUPPORTED_FACT` about Astropy. UFUQ's independent runner must disable
implicit network access, install explicitly selected tables, and capture every source
quality, availability state, and warning instead of inheriting permissive library
defaults. Scientific approval remains a separate UFUQ decision.

## ScientificProfileV1 time contract

The source findings above support available representation and conversion semantics;
they do not choose UFUQ behavior. ScientificProfileV1 therefore makes the following
normative `PROJECT_DECISION`:

- accept only whole-second `YYYY-MM-DDTHH:mm:ssZ` at the astronomy boundary;
- treat `23:59:60Z` as structurally eligible but require the selected approved leap
  artifact to confirm that exact positive-leap date before producing a validated UTC
  instant;
- reject fractions, numeric offsets, `-00:00`, local/unqualified time, Unix timestamps,
  bare Julian Dates, and implicit current time at that boundary;
- carry labelled UTC quasi-JD, TAI, TT, and UT1 states and all conversion provenance,
  warnings, and statuses; and
- require each activated profile to state explicit earliest/latest values and endpoint
  dispositions, while deriving those concrete values only after approved artifacts and
  all contributing domains exist.

Whole-second serialization is an input-resolution choice, not a scientific accuracy,
uncertainty, or tolerance. RFC 3339 does not require this subset; SOFA does not choose
UFUQ's dates; Astropy output precision and defaults do not become production policy.

## Normative ScientificProfileV1 leap/EOP policy

The following are bounded `PROJECT_DECISION` semantics. They close the generic
preimplementation policy without selecting production bytes or a supported date:

1. The only operational time/orientation inputs are an approved leap state,
   `UT1-UTC` in seconds, and polar motion `xp`,`yp` in radians. `UT1-UTC` is UT1 minus
   UTC. `xp`,`yp` are the CIP coordinates in the ITRS along the IERS reference meridian
   and 90 degrees west respectively. `dX`,`dY` and LOD are not requested by V1, are not
   hidden library inputs, and are not represented as zero.
2. V1 accepts only source fields classified `FINAL` and separately approved for the
   exact product, field, series, domain, and bundle. Bulletin B final Section 1 values
   are eligible source material. A `finals2000A` container is eligible only through its
   independently verified Bulletin B columns/lineage. The format defines its Bulletin
   A `I` flag as `IERS`, not `FINAL`; Bulletin A documentation separately identifies
   the corresponding non-predicted rapid values as quick-look estimates, which UFUQ
   maps to `IERS_ESTIMATE`. `IERS_ESTIMATE`, `PRELIMINARY`, `PREDICTED`, unknown,
   blank, or unmapped quality is not approved for V1.
3. Each required EOP field retains its own source product, artifact and row/sample IDs,
   raw source flags, source quality, source-declared uncertainty (explicitly unknown,
   never zero, when absent), unit, coverage,
   interpolation support and evidence,
   availability, and scientific approval. A shared source flag is cited separately by
   each field. No row, pair, product, or approved field promotes another.
4. Gazette 13 recommends a Lagrangian interpolation-and-restoration procedure, shows a
   four-data-point implementation, and permits equivalent interpolation schemes.
   ScientificProfileV1 selects that four-point Lagrange example as its V1 method and
   combines it with the IERS Conventions 2010 restoration described below. V1 does not
   permit generic linear interpolation or an unspecified “equivalent” method. 2D must
   pin the exact official method/model source identity, issue/version and hash; 2E
   implements and verifies that configuration.
5. For an instant between daily samples `i` and `i+1`, each field requires the four
   ordered support samples `i-1`,`i`,`i+1`,`i+2`. Every contributing value must be
   present, finite, `FINAL`, approved, and part of one explicitly reviewed coherent
   field series. Contributor artifact/row IDs, epochs, qualities, interpolation weights,
   restoration-model identity, and raw/normalized statuses are evidence. A gap,
   duplicate/nonmonotonic epoch, unapproved neighbor, unrecorded source boundary, or
   insufficient support fails closed. V1 never extrapolates or substitutes a nearest
   row. The same full support rule applies at a tabulated instant so endpoint behavior
   has one deterministic contract. This last rule is a conservative UFUQ project
   decision, not a mathematical necessity for reproducing a tabulated value; it
   intentionally narrows both ends of the activatable interval.
6. UT1 and TAI are continuous while UTC has integer leap discontinuities; official
   IERS C04 processing converts `UT1-UTC` to continuous `UT1-TAI` before numerical
   treatment and translates it back afterward. UFUQ therefore derives each support
   value as `UT1-TAI = (UT1-UTC) - (TAI-UTC)`, interpolates that continuous quantity,
   and reconstructs the target value as `UT1-UTC = (UT1-TAI) + (TAI-UTC)` using the
   target instant's approved leap state. The equations and target-state requirement
   are the UFUQ project decision; they are not attributed to Gazette 13. `xp` and `yp`
   are interpolated independently. No value crosses a source-quality boundary; a
   coherent series assembled from multiple retained Bulletin B artifacts must name
   and approve every contributor in its bundle manifest.
7. After interpolation, V1 restores exactly once the IERS Conventions 2010 subdaily
   terms absent from the reported daily series: Chapter 8 ocean-tide terms for
   `xp`,`yp`, and UT1; Chapter 5 Table 5.1a diurnal libration terms for `xp`,`yp`; and
   Table 5.1b semidiurnal libration terms for UT1. It does not re-add the long-period
   or secular polar-motion libration already present in observations. The exact
   baseline routine/coefficient/dependency bytes and compatibility with the selected
   product's regularization are 2D/2E configuration. Later corrected working material
   is separately identified and never silently merged into registered TN36.
8. Scientific calculation is offline and deterministic. One immutable, prevalidated,
   explicitly supplied bundle contains all leap, EOP, interpolation/model, policy, and
   manifest identities and SHA-256 hashes. Request execution performs no download,
   cache discovery, auto-refresh, ambient ERFA leap-table lookup, or data fallback.
9. Bulletin C remains leap-event authority. The production transport may be a
   versioned official IERS machine artifact or official IANA-distributed leap artifact
   only after 2D selects exact bytes, verifies integrity, records publisher validity,
   supplies a UFUQ SHA-256, and proves the relevant transition history agrees with the
   applicable Bulletin C record. `23:59:60Z` validates only for an exact approved
   positive-leap event. Missing, expired-for-that-request, inconsistent, or unapproved
   leap evidence blocks UTC validation/conversion. SOFA's compiled table is not the
   production authority.
10. Acquisition age, publisher expiry/valid-through metadata, scientific field coverage,
   source quality, bundle activation, and UFUQ approval are separate. Old final
   historical values do not become scientifically stale merely because bytes were
   acquired long ago. A recently acquired file can still be out of range or unapproved.
   As a UFUQ project decision, publisher expiry limits the artifact's approved claim
   about future leap knowledge; it does not erase a transition inside an explicitly
   approved historical replay scope. A superseded hash-bound artifact remains eligible
   only for an identified replay whose requested instant is inside that recorded
   scope; it cannot assert later leap knowledge or become a hidden “latest file.” EOP final rows have per-field
   coverage/interpolation support rather than a universal age expiry. V1 therefore has
   no free-standing age-based `STALE` scientific status or invented day threshold.
11. No degraded mode is reachable. Zero `UT1-UTC`, zero `xp`/`yp`, nearest-row use,
    extrapolation, predicted/preliminary/estimate fallback, expired-for-request/unapproved bundle
    fallback, automatic product substitution, and warning-only “best effort” results
    are prohibited. A missing or unapproved requirement returns a typed non-result.

The state axes remain orthogonal:

```text
SourceFieldQuality = FINAL | PRELIMINARY | PREDICTED | IERS_ESTIMATE | UNKNOWN
ArtifactAvailability = AVAILABLE | UNAVAILABLE | INTEGRITY_FAILURE
FieldCoverage = COVERED | OUT_OF_RANGE | GAP | INSUFFICIENT_INTERPOLATION_SUPPORT
PublisherValidity = VALID_FOR_REQUEST | EXPIRED_FOR_REQUEST | NOT_DECLARED | UNVERIFIED
ScientificApproval = APPROVED | NOT_APPROVED | REVIEW_REQUIRED
```

Acquisition timestamp/age and active/superseded/replay-only lifecycle are evidence
fields, not values in `SourceFieldQuality` or `ScientificApproval`.

## Update, activation, and replay

Updates occur outside a scientific request through this normative sequence:

```text
candidate acquisition
-> publisher and UFUQ hash/integrity verification
-> parse/schema validation
-> per-field source-quality and coverage inspection
-> comparison with the active bundle, including value/status/warning/domain diffs
-> astronomy/data review of the proposed activation scope
-> atomic activation of a new immutable bundle
-> indefinite retention of the previous bundle for identified replay
```

An official publication never silently replaces the active bundle. A superseded bundle
may reproduce an old recorded result under its historical identity, but it cannot be
silently selected for a new request. Publication frequencies do not select UFUQ's
polling cadence; deployment/operations may set a cadence later without changing the
scientific policy.

## Lifecycle handoff and remaining data decisions

| Owner | Responsibility |
|---|---|
| Milestone 2C | Required field set, final-only quality policy, per-field state/evidence, UFUQ-selected four-point/continuous-UT1 semantics, IERS-2010 restoration family, leap-authority/transport requirements, offline/replay/update semantics, and fail-closed/no-degraded behavior. |
| Milestone 2D | Select exact official Bulletin B/final-derived EOP and leap artifact families/releases; acquire raw bytes; record licences/use terms, publisher metadata, acquisition identity, source flags and coverage; verify integrity and Bulletin C consistency; pin SHA-256 and exact interpolation/restoration source/configuration; approve the candidate bundle. |
| Milestone 2E | Implement fail-closed parsers/validators, normalized independent field records, UFUQ-selected four-point interpolation through continuous `UT1-TAI`, the pinned IERS-2010 restoration once afterward, canonical bundle/manifest generation and hashing, runtime lookup, and negative/boundary/replay tests without request-time network access. |
| 2D/2E profile activation | Derive explicit earliest/latest whole-second UTC bounds from the intersection of leap validity, independent `UT1-UTC`,`xp`,`yp` four-sample support, model/catalogue/observer/scenario constraints, and approval; record endpoint disposition and fixtures. |

Archived official Bulletin B final daily values provide all three required EOP fields,
and the four-point rule leaves nonempty interior historical intervals. A bounded
historical first profile is therefore practical without preliminary or predicted data.
The policy does not promise current/“now” operation: final publication latency simply
limits the later activated endpoint. Exact files, dates, values, and hashes remain 2D/
2E activation data.

## Decisions that remain open after the semantic policy

| Decision | Classification | Closure evidence |
|---|---|---|
| Select and activate exact production EOP/leap artifacts and exact interpolation/restoration source/configuration. | `BLOCKS_2D_DATA_AUTHORITY` | Official bytes, identities, SHA-256, field-quality/coverage evidence, Bulletin C cross-check, review, and activation manifest. |
| Instantiate the earliest/latest supported instants under the normative endpoint contract. | `BLOCKS_2D_DATA_AUTHORITY` / activation data | Deterministic approved-domain intersection and boundary fixtures. |
| Accept any IERS-estimate, preliminary, predicted, unknown-quality, extrapolated, nearest, or degraded value. | `BLOCKS_LATER_EXTENSION` plus `HUMAN_REVIEW_REQUIRED` | A new profile/mode, field-specific domain, source uncertainty, interaction evidence, warning contract, numerical acceptance, and named review. V1 rejects them. |
| Select an operational polling cadence. | `REQUIRED_LATER` | Deployment/operations owner decision. It does not change request-time immutability or activation review. |
| Quantify EOP source/interpolation/implementation uncertainty and approve a numerical tolerance. | `POST_IMPLEMENTATION_VALIDATION` plus `HUMAN_REVIEW_REQUIRED` | Source uncertainty, production/reference residuals, domain partitions, error-budget combination, and named review. |

## Required experiments

Every item below is `EXPERIMENT_REQUIRED`; none can choose source authority or close a
missing policy:

- replay identical fixtures with an explicitly installed EOP/leap bundle in isolated
  offline environments and compare canonical bytes, warnings, each field's quality/
  availability/approval state, and hashes;
- exercise source quality, artifact availability/integrity, field coverage, publisher
  validity, and scientific approval independently for IERS-estimate, final,
  preliminary, mixed, predicted, expired-for-request, missing, blank, gap, and
  out-of-range records without allowing nearest-value or zero substitution;
- quantify nonzero-versus-zero and active-versus-superseded changes separately for V1
  `UT1-UTC`, `xp`,`yp`, including interactions; evaluate `dX`,`dY` only before a later
  profile proposes to include observed celestial-pole offsets;
- test valid and invalid `23:59:60Z` inputs against a pinned leap table, adjacent UTC
  instants, and normative rejection of fractional seconds, malformed offsets, and
  `-00:00`; and
- run every eventual supported endpoint and its immediate outside neighbour, plus
  observer latitude/longitude/height and polar/zenith singular partitions.

## Evidence boundary

`PROJECT_DECISION`: the final-only, offline, field-independent and fail-closed
ScientificProfileV1 policy is specified sufficiently for implementation entry.
`BLOCKS_2D_DATA_AUTHORITY`: exact production families/releases/bytes/hashes,
Bulletin C cross-checks, exact interpolation/restoration source configuration, and
activated supported-date values still must exist before real V1 execution.
`FINAL_TOLERANCE_NOT_JUSTIFIED`: final data and the selected interpolation family do not
eliminate source, interpolation, implementation, or model uncertainty; no numerical
bound or tolerance follows from this decision.
