# IERS EOP and leap-second product documentation

## Scope and identity

- Source IDs: `IERS-BULLETIN-A`, `IERS-BULLETIN-B`, `IERS-BULLETIN-C`,
  `IERS-FINALS2000A-FORMAT`, `RFC3339-TIMESTAMP`, and `IANA-TZDB-LEAPS`.
- Retrieval date: 2026-08-03.
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
| [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html), Sections 5.6-5.8 | The Internet timestamp profile uses a four-digit Gregorian date, `T`, time through seconds, optional fractional seconds, and a required `Z` or numeric UTC offset. A positive leap second can use second `60` only at its valid instant; `-00:00` has different semantics from known UTC. | RFC 3339 permits choices that UFUQ can narrow. It does not validate a claimed leap second against a current IERS table or define scientific precision. |
| [IANA tzdb 2026b archive](https://data.iana.org/time-zones/tzdb-2026b/) | The versioned release directory contains `leap-seconds.list` and `leapseconds` artifacts. | This records an official candidate transport only. No IANA artifact/version/hash is selected for production by Milestone 2C.3. IERS Bulletin C remains the event authority. |

Every statement in this table is `SOURCE_SUPPORTED_FACT`. The last column prevents a
source description from being promoted into a UFUQ project decision.

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

## Remaining leap/EOP bounded project proposal

The following are `PROJECT_DECISION` proposals for later approval:

1. Scientific calculation is offline and deterministic. It reads an immutable,
   prevalidated data bundle identified by manifest version and SHA-256 hashes; it does
   not download or refresh data during a request.
2. Data acquisition/update is a separate reviewed administrative operation. A new
   bundle is added atomically; old bundles remain available for replay; fixture and
   warning diffs are reviewed before activation.
3. EOP state uses three orthogonal dimensions rather than one flat status: source-field
   quality (`FINAL`, `PRELIMINARY`, `PREDICTED`, `IERS_ESTIMATE`); artifact/field
   availability (`AVAILABLE`, `STALE`, `UNAVAILABLE`, `OUT_OF_RANGE`, with artifact
   staleness distinct from field coverage); and scientific approval (`APPROVED`,
   `NOT_APPROVED`, `REVIEW_REQUIRED`).
4. ScientificProfileV1 requires `UT1-UTC`, `xp`, and `yp`; each retains independent
   product/row provenance, source quality, availability, coverage, interpolation
   evidence, and approval. Observed `dX`,`dY` are explicitly outside the model-CIP-only
   V1 route and are neither requested nor represented as zero. If a later profile
   selects them, each gets the same independent field state. If a source flag applies
   to a pair, both fields cite it independently; no field promotes another.
5. Missing, blank, stale, expired, out-of-range, or unapproved-quality inputs are
   explicit non-result outcomes. Automatic downloads, cached-table discovery, stale-
   table use, prediction acceptance, zero substitution, and nearest-row extrapolation
   are prohibited.
6. No degraded astronomical result is approved. The outcome vocabulary reserves a
   degraded variant, but it is unreachable until a named mode, quantitative bound,
   warning contract, and named reviewer approval of the inputs, domain, and tolerance
   exist.

## Decisions that remain open

| Decision | Classification | Closure evidence |
|---|---|---|
| Select the production EOP family/file classes, field precedence/interpolation, and per-field source-quality/availability/approval policy for V1 `UT1-UTC`,`xp`,`yp`. | `HUMAN_REVIEW_REQUIRED` | Astronomy review of the semantic policy. Exact version/bytes/hashes and concrete immutable-bundle activation then belong to 2D. |
| Select the production leap-second machine artifact and prove it agrees with the applicable Bulletin C history. | `HUMAN_REVIEW_REQUIRED` | Version, bytes, SHA-256, expiration/validity metadata, cross-check, and approval. |
| Instantiate the earliest/latest supported instants under the normative endpoint contract. | `BLOCKS_2D_DATA_AUTHORITY` / activation data | Deterministic intersection of approved source epoch/propagation, leap, per-field EOP/interpolation support, ephemeris/model, observer, and scenario ranges; explicit approval and boundary fixtures. |
| Accept any IERS-estimate, preliminary, or predicted EOP value. | `HUMAN_REVIEW_REQUIRED` | Named field-by-field scope, prediction horizon where applicable, uncertainty/error budget, warning contract, and approval. |
| Define when an EOP artifact is stale rather than merely old or predictive. | `AUTHORITY_OR_EVIDENCE_MISSING` | Approved update service level or artifact validity rule. Astropy's defaults are not UFUQ authority. |
| Select an operational polling/update cadence. | `HUMAN_REVIEW_REQUIRED` | Operations owner and astronomy reviewer approval; source publication frequencies are evidence, not the project cadence. |
| Quantify zero-EOP, stale-leap, predictive, nearest-value, extrapolated, or other degraded calculations. | `EXPERIMENT_REQUIRED` | Per-effect and interaction bounds over a proposed domain. |
| Approve any such degraded calculation after evidence exists. | `HUMAN_REVIEW_REQUIRED` | Accepted tolerances, exact domain, provenance, warnings, and labelled endpoint semantics. |

## Required experiments

Every item below is `EXPERIMENT_REQUIRED`; none can choose source authority or close a
missing policy:

- replay identical fixtures with an explicitly installed EOP/leap bundle in isolated
  offline environments and compare canonical bytes, warnings, each field's quality/
  availability/approval state, and hashes;
- exercise source quality, artifact availability, field availability, and scientific
  approval independently for IERS-estimate, final, preliminary, mixed, predicted,
  stale, expired, missing, blank, and out-of-range rows without allowing nearest-value
  or zero substitution;
- quantify nonzero-versus-zero and current-versus-stale changes separately for V1
  `UT1-UTC`, `xp`,`yp`, including interactions; evaluate `dX`,`dY` only before a later
  profile proposes to include observed celestial-pole offsets;
- test valid and invalid `23:59:60Z` inputs against a pinned leap table, adjacent UTC
  instants, and normative rejection of fractional seconds, malformed offsets, and
  `-00:00`; and
- run every eventual supported endpoint and its immediate outside neighbour, plus
  observer latitude/longitude/height and polar/zenith singular partitions.

## Stop condition

`AUTHORITY_OR_EVIDENCE_MISSING`: this dossier does not establish production EOP or
leap-second families/bytes/hashes, activated supported-date values, observer-height
range, prediction horizon, stale threshold, or degraded-error bound. The generic UTC/
time-domain contract is implementable, but real astronomy execution remains blocked
where required artifacts, activated bounds, or the still-open leap/EOP policy are absent.
