# Phase 1 Milestone 2C: Scientific Behaviour Contract

## Status and verdict

**Evidence audit date:** 2026-08-03

**Milestone status:** OPEN

**ScientificProfileV1 implementation authority:** NOT YET GRANTED; bounded only by
the preimplementation decisions in Section 18

The tracked source dossiers and project decisions support a stricter contract than the
earlier draft, but they do not close the manual scientific decisions needed for
production astronomy. This audit resolves documented source-field semantics while
retaining each named authority gap, fixed UFUQ coordinate conventions, typed state
separation, and reference-test requirements.
Milestone 2C.2 now defines a reviewable SOFA-based candidate route and effect matrix,
Milestones 2C.3-2C.4 add fail-closed operating-data and refraction/horizon/visibility
contracts, and Milestone 2C.5A freezes a separate experiment protocol,
machine-readable registry, fixture/result schemas, current execution classifications,
and a proposed synthetic-only first batch. Milestone 2C.5B executes that bounded
batch, and Milestone 2C.5C inventories its exact and measurement-only evidence in a
separate error-budget framework and machine-readable AST-006 ledger. Milestone 2C.6
now separates the narrow decisions needed to start `ScientificProfileV1` from 2D data
authority, postimplementation validation, later extensions, and learner-facing work.
It removes the circular requirement to produce TypeScript/reference residuals before
TypeScript implementation is permitted.

No astronomy reviewer or owner approval is recorded for the remaining profile-scoped
choices. Milestone 2C therefore remains open and `IMP-009` remains unresolved. Final
numerical tolerances, production/reference results, globally supported observers,
refraction, and aggregate visibility are not conditions for starting the bounded V1
implementation; they retain their later acceptance or extension gates.

This document does not authorize catalogue parsing, source-derived tracked artifacts,
learner-facing cultural claims, or deployment.

## 1. Purpose

Define the normative behaviour for transforming approved catalogue astrometry into
observer-local directions while keeping scientific calculation, visibility, scene
mapping, and learner scoring separate. It also records which conclusions are already
supported, which are project choices, which stop profile implementation, and which
instead stop only data eligibility, later extensions, learner-facing claims, or
scientific acceptance.

## 2. Scope and evidence classes

This milestone covers:

- coordinate states and transformation boundaries;
- reference frames, epochs, units, and time scales;
- proper-motion and space-motion inputs;
- observer location and geodetic conventions;
- Earth-orientation and leap-second data;
- azimuth and altitude conventions;
- refraction, horizon, and visibility boundaries;
- supported date range and failure behaviour;
- scientific error budgeting; and
- code-independent reference-test and stronger-oracle requirements.

This milestone does not implement:

- the I/311 catalogue parser or generated catalogue artifacts;
- production astronomy code or a production/reference comparison;
- cultural memberships or lesson routes;
- the Three.js scene;
- learner scoring or Bayesian Knowledge Tracing; or
- persistence, accounts, or deployment.

The classifications used below are:

- `SOURCE_SUPPORTED_FACT`: the cited external authority defines the input, algorithm
  role, or convention;
- `PROJECT_DECISION`: an existing tracked UFUQ decision fixes behaviour within project
  scope;
- `EXPERIMENT_REQUIRED`: a named sensitivity or comparison experiment is required but
  cannot supply source authority;
- `HUMAN_REVIEW_REQUIRED`: a named domain reviewer must approve or reject the bounded
  interpretation;
- `AUTHORITY_OR_EVIDENCE_MISSING`: the inspected authority does not define the value or
  semantics needed for the affected behaviour;
- `PROVISIONAL_CHOICE`: a bounded spike choice that cannot be promoted to production;
- `UNRESOLVED_QUESTION`: missing evidence, experiment, approval, or policy blocks only
  the affected behaviour.

Milestone 2C.1, 2C.2, 2C.3, and 2C.4 conclusions use only the first five classifications
requested for those audits: `SOURCE_SUPPORTED_FACT`, `PROJECT_DECISION`,
`EXPERIMENT_REQUIRED`, `HUMAN_REVIEW_REQUIRED`, and
`AUTHORITY_OR_EVIDENCE_MISSING`.

Milestone 2C.5A separately classifies experiment execution as
`RUNNABLE_SYNTHETIC_NOW`, `BLOCKED_BY_SOURCE_AUTHORITY`,
`BLOCKED_BY_PROJECT_DECISION`, `BLOCKED_BY_REVIEW`,
`BLOCKED_BY_REQUIRED_DATA`, or `DEFERRED_TO_PRODUCTION_IMPLEMENTATION`. Execution
classification never changes the evidence class of a scientific conclusion.

Milestone 2C.5C separately classifies each budget term or tolerance decision as
`EXACT_CONTRACT_INVARIANT`, `MEASURED_SYNTHETIC_SENSITIVITY`,
`SOURCE_UNCERTAINTY_UNRESOLVED`, `MODEL_UNCERTAINTY_UNRESOLVED`,
`OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED`, `IMPLEMENTATION_ERROR_UNMEASURED`,
`INDEPENDENT_VALIDATION_REQUIRED`, `HUMAN_REVIEW_REQUIRED`,
`CANDIDATE_TOLERANCE_PROPOSAL`, or `FINAL_TOLERANCE_NOT_JUSTIFIED`.
These classes do not promote a measured value into a source uncertainty, authority
limit, engineering allowance, or approved threshold.

Primary evidence for this audit is:

- IAU SOFA issue `2023-10-11`, exact studied routine contracts;
- the official registered IERS Conventions (2010) TN36 `v1.0.0` baseline, with later
  corrected chapters/non-registered working versions and separately linked
  non-official supporting documentation kept distinct and not promoted to the official
  distribution;
- CDS/VizieR I/311 `ReadMe` and official Appendix G Tables G.2-G.7;
- CDS *Standards for Astronomical Catalogues* Version 2.0 Section 3.2.2 for
  `yr = 365.25 d`;
- ESA Gaia DR1 processing documentation Section 4.2.1 for its direct I/311-specific
  `J1991.25` use;
- ESA SP-1200 Volume 1 for original-catalogue semantic support only;
- van Leeuwen's 2007 validation article for error-characteristic context only;
- `docs/ASTRONOMY_SPEC.md`, ADR-003, ADR-007, and the repository astronomy
  validation skill; and
- the official Astropy/PyERFA documentation pins in
  `docs/references/studies/astropy-pyerfa-reference-docs.md`;
- the 2C.4 topic extraction in
  `docs/references/studies/refraction-horizon-visibility.md`; and
- the locked synthetic-only Astropy smoke oracle, within its explicitly limited claim.

The local *Explanatory Supplement* candidate supplies no claim-level evidence because
its tracked dossier marks it text-unavailable, incomplete, and provenance-unverified.

## 3. Normative coordinate-state boundaries

The following separation is a `PROJECT_DECISION` and is normative:

```text
I/311 catalogue astrometry at its declared frame and source epoch label
-> approved space-motion propagation
-> approved celestial intermediate transformation
-> approved Earth rotation and terrestrial orientation
-> observer-dependent geometric horizontal direction
-> optional, separately labelled refracted direction
-> separately defined horizon/visibility result
-> separately defined scene mapping
```

Every implemented stage must declare its input and output state, frame, epoch or
observation time, units, convention, status, and policy/provenance identifier. An
immutable catalogue row must never be overwritten with observed, horizontal,
refracted, visibility, or scene values.

This separation does not select the exact production routines, transform route, or
included effects. Milestone 2C.2 supplied the candidate below; Milestone 2C.6 makes its
S1 boundary source-neutral while retaining the audited I/311 instantiation as a bounded
spike example. Blocked stages and effect rows remain unavailable rather than being
filled by a default.

### 3.1 Milestone 2C.2 candidate typed route

The proposed production semantics are a componentized, CIO-based route aligned to IAU
SOFA issue `2023-10-11` and IERS TN36 Chapter 5. The proposal uses the SOFA routine
contracts as the algorithm candidate, not Astropy's dynamic transform graph and not an
unversioned claim of "SOFA compatibility." The future production implementation must
be separately authored in the approved TypeScript boundary or use a separately
approved production library. That implementation choice is not made here.

| Stage | Typed state and proposed transition | Authority or algorithm candidate | Required inputs and current disposition | Classification |
|---|---|---|---|---|
| `2C.2-S1` | `CatalogueIcrsState`: immutable normalized source-neutral ICRS astrometry carrying right ascension, declination, explicit epoch label/representation/scale, proper-motion components and derivative convention/unit, parallax/distance and radial-velocity/perspective dispositions, uncertainty/covariance or reviewed omission, quality, source-release identity, and provenance. | `ScientificProfileV1` project boundary plus the exact selected-source authority. For the bounded I/311 spike only, its `ReadMe`, Appendix G Table G.3, and ESA Gaia DR1 Section 4.2.1 support ICRS, starred-alpha motion, and the Julian `J1991.25` representation. | An eligible production state may not carry an unspecified epoch/derivative scale or implicit zero. The I/311 instantiation retains literal `Ep=1991.25` and its unresolved scale and is ineligible unless 2D closes or rejects that gap. | `PROJECT_DECISION` plus source-specific `SOURCE_SUPPORTED_FACT`; I/311 scale remains `AUTHORITY_OR_EVIDENCE_MISSING` |
| `2C.2-S2` | `PropagatedIcrsAstrometry`: preliminary ICRS catalogue-astrometry propagation from an approved source instant to an explicitly declared target epoch. The type does not itself imply J2000.0 or a frame transformation. For the selected `iauAtciq`/`iauAtco13` candidate only, the target would be J2000.0. | SOFA `iauPmsafe`; `iauAtco13` and `iauAtciq` Note 1. The candidate target instant is J2000.0 at JD 2451545.0 TT converted, not relabelled, to the TDB date required by `iauPmsafe`. | Source epoch/derivative time scale, coordinate-rate conversion and polar guard, parallax/distance policy, radial-velocity policy, and warning ownership. The CDS-defined `yr` duration is resolved. Source-derived execution is blocked while those inputs are unresolved; a missing acceptance tolerance blocks later scientific acceptance, not implementation or measurement-only execution. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| `2C.2-S3` | `ObserverAwareCirsDirection`: transform successfully propagated J2000.0-target ICRS astrometry into a CIRS direction at the observation instant while keeping the observer-aware parallax/aberration context explicit. | Candidate SOFA `iauApco13` model-only context plus `iauAtciq`; ICRS/GCRS covers motion, parallax, solar deflection, and aberration, while GCRS/CIRS applies frame bias and the built-in model CIP/CIO from IAU 2006 precession with IAU 2000A nutation. This convenience branch does not apply observed celestial-pole offsets. | UTC, approved TT/UT1 conversion, Earth ephemeris/model, observer, `UT1-UTC`, polar motion `xp`,`yp`, complete approved space-motion state, SOFA issue/routine IDs, and an explicit `dX`,`dY`-unavailable status. Candidate only. | `PROJECT_DECISION` |
| `2C.2-S4` | `EarthOrientationContext`: an immutable context carrying UTC, TAI, TT, UT1, ERA, polar motion `xp`,`yp`, TIO locator, a separately typed celestial-pole-offset policy/status, leap/EOP bundle IDs and hashes, artifact availability, and independent field records for source quality, availability, provenance, coverage, and scientific approval. It is consumed with the CIRS direction rather than hidden in a sidereal-time scalar. | IERS TN36 Eq. (5.1) factorization and Sections 5.3-5.5; official IERS product/status documentation; SOFA `iauApco13`, `iauEra00`, `iauSp00`, `iauPom00`, and `iauC2t06a` as component checks. `iauApco13` can consume `UT1-UTC`,`xp`,`yp`; it cannot consume observed `dX`,`dY`. | Production leap-second/EOP products, separately pinned later corrections/working material if selected, field precedence/interpolation, stale/update and source-quality approval policy, celestial-pole-offset route, and supported dates. **Blocked**; missing values are not zero, and model CIP/CIO is not relabelled as observed-offset-corrected. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| `2C.2-S5` | `GeometricHorizontalDirection`: north-zero/east-positive azimuth, signed geometric altitude, ENU unit vector, observation instant, observer policy, EOP policy, singular-azimuth status, and warnings. | Candidate SOFA `iauAtioq` using the explicit model-only `iauApco13` context with refraction coefficients set to zero; `iauAtco13` is a composed cross-check, not the production API. A later reviewed decomposed context is required if observed celestial-pole offsets are included. | Approved geodetic datum/ellipsoid, ellipsoidal-height semantics/range, EOP context, celestial-pole-offset disposition, and stable status mapping. Route shape is proposed; execution remains blocked by those inputs. | `PROJECT_DECISION` |
| `2C.2-S6` | `RefractedHorizontalDirection`: optional result derived from the same pre-refraction CIRS/geometric evidence and labelled with model, meteorology, wavelength, and validity status. It never overwrites S5. | Candidate SOFA `iauRefco` coefficients consumed by a separate `iauAtioq` evaluation; Astropy `AltAz` is reference-only. | Pressure, temperature, humidity, wavelength, supported altitude/environment range, and unavailable/failure policy. **Conditional** and not approved. | `HUMAN_REVIEW_REQUIRED` |
| `2C.2-S7` | `VisibilityState`: a separate project-policy result that consumes geometric/refracted direction plus independently approved horizon, photometric/variability, Sun/daylight/twilight, extinction/transparency, cloud/weather, terrain/obstruction, light-pollution, screen, and learner inputs. | UFUQ Astronomy Specification and AST-004; SOFA does not define learner visibility. | Horizon equality, physical/terrain dip, all visibility components, aggregation, and below-horizon downstream policies remain blocked. | `PROJECT_DECISION` |
| `2C.2-S8` | `SceneDirection`: a presentation adapter from a valid direction state into the fixed ENU-to-Three axes. It carries the source state/policy ID and pending-or-approved validation state, and makes no visibility or scientific-correction claim. | UFUQ ADR-003/IMP-010. | Valid upstream direction only; rendering cannot fill an unavailable astronomy result or promote pending evidence to approval. | `PROJECT_DECISION` |

The Stage S3 name is deliberately observer-aware. In the proposed `iauApco13` plus
`iauAtciq` composition, the astrometry context carries the observer's barycentric
position and velocity, so parallax/aberration responsibilities must not be applied
again by a generic ITRS or scene transform. Stage S4 remains a separate typed evidence
context even though SOFA packages several values in one `iauASTROM` structure.

The convenience branch has four distinct responsibilities that must not be conflated:

- `iauApco13` internally selects the SOFA Earth ephemeris and the built-in model
  CIP/CIO from IAU 2006 precession with IAU 2000A nutation;
- supplied `UT1-UTC` governs Earth rotation;
- supplied `xp`,`yp` govern polar motion; and
- observed celestial-pole offsets `dX`,`dY` are not accepted or applied.

Consequently, the `iauApco13` candidate is model-CIP-only, not an approved
observed-offset-corrected route. If AST-003 requires external ephemerides or observed
celestial-pole offsets, the route must be revised to lower-level `iauApco`-family
inputs or an equivalent explicitly supplied corrected context; the convenience routine
must not erase that policy choice.

### 3.2 Production versus code-independent reference

`PROJECT_DECISION`: the production candidate and reference path remain different
implementations, but shared ERFA/SOFA lineage prevents this pair from constituting the
later stronger independent oracle:

- production candidate: an explicitly staged SOFA `2023-10-11` CIO-family semantic
  route whose eventual TypeScript algorithm/library still requires AST-003 approval;
- code-independent reference: locked Astropy `8.0.1` `SkyCoord`/space-motion and explicit
  `CIRS`/`AltAz` transforms backed by PyERFA/IERS, with direct PyERFA probes where
  warnings or effect ablations must be exposed; and
- composed SOFA/ERFA `atco13` output: a same-family consistency check for the staged
  candidate, not an independent oracle by itself.

Astropy defaults, its automatic transform-graph route, missing-radial-velocity zero,
WGS 84 observer semantics, automatic IERS behavior, and pressure-zero default are not
production decisions. The reference runner must set and record each applicable input
and policy explicitly.

## 4. Catalogue frame and epoch

### 4.1 I/311 input frame

`SOURCE_SUPPORTED_FACT`:

- the selected I/311 `RArad` and `DErad` fields are ICRS catalogue astrometry;
- their source units are radians; and
- ICRS frame identity does not remove the need for a reference epoch for a moving
  star.

UFUQ must preserve `ICRS` as source metadata and in every normalized record and
fixture. Calling these values merely "J2000 coordinates" is prohibited because that
would conflate frame, epoch, equinox/origin, and time scale.

### 4.2 I/311 source epoch label

`SOURCE_SUPPORTED_FACT`:

- the exact I/311 field wording is `Right Ascension in ICRS, Ep=1991.25` and
  `Declination in ICRS, Ep=1991.25`;
- the I/311 `ReadMe` itself does not prefix the epoch with `J` or `B`, call it a
  decimal year, or name a time scale; and
- ESA Gaia DR1 Section 4.2.1 directly identifies its Hipparcos input as the new
  reduction retrieved from CDS/VizieR I/311 and calls the parameter epoch
  `J1991.25`. The source-supported representation is therefore Julian, not
  Besselian or calendar decimal year.

`AUTHORITY_OR_EVIDENCE_MISSING`:

- neither I/311 nor the ESA Gaia DR1 page states the time scale needed to turn that
  Julian representation into an exact propagation instant;
- ESA SP-1200 defines the original 1997 catalogue epoch as `J1991.25(TT)`, but that
  statement and Astropy's generic `jyear` definition are supporting candidates, not
  proof of I/311 intent; and
- no cited authoritative standard inspected here explicitly binds a generic TT-based
  Julian-epoch convention to I/311. The time scale is therefore genuinely unspecified
  at the I/311-applicable authority layer, not safely inferable merely from a library
  default.

`PROJECT_DECISION`: preserve the literal `Ep=1991.25` label and the evidence-backed
Julian representation separately. Source-derived propagation from that epoch returns
an explicit unavailable/unresolved outcome until an I/311-applicable authority or
reviewed project interpretation supplies the time scale. No production or reference
output may silently call the I/311 epoch `J1991.25(TT)`.

`HUMAN_REVIEW_REQUIRED`: if no more specific authority is obtained, an astronomy
reviewer must decide whether the original-catalogue `J1991.25(TT)` lineage plus the
generic Julian-epoch convention is sufficient for a bounded UFUQ interpretation. The
review must name the rejected alternatives, implementation consequence, validation
consequence, and limitation; it does not become a source-supported fact.

### 4.3 Consequences of the missing time scale

`SOURCE_SUPPORTED_FACT`:

- Astropy represents time format and time scale separately; its `jyear`, `byear`, and
  `decimalyear` formats are not interchangeable;
- Astropy `apply_space_motion` uses the coordinate's initial `obstime`; and
- PyERFA `pmsafe` requires start and end epochs as two-part TDB Julian Dates and
  interprets proper-motion rates per TDB Julian year.

`PROJECT_DECISION`: the reference implementation must convert a known source-scale
instant to the routine's required scale. It must not relabel an unlabeled Julian Date
as TDB. With the I/311 scale unresolved, the elapsed propagation time is conditional
on an unapproved assumption, so exact propagated coordinates, deterministic reference
fixtures, and warning/status evidence cannot be claimed as I/311-derived truth. A
possibly small numerical difference is still a semantic and reproducibility defect;
no `negligible` conclusion is permitted without the approved range and experiment.

### 4.4 Sensitivity experiment, not source authority

`EXPERIMENT_REQUIRED`: use only synthetic astrometry and the locked oracle. The
protocol freezes this family as three stable records:

1. `2C.1-EXP-01` compares explicit `jyear`/TT with the same Julian epoch number
   labelled TDB and UTC, each converted to TDB before propagation;
2. `2C.1-EXP-02` compares `decimalyear`/TT as the distinct calendar-year
   interpretation; and
3. `2C.1-EXP-03` uses `byear`/TT as a rejection/guard case, not a source-supported
   candidate.

Use zero-motion and high synthetic proper-motion cases with explicit parallax/radial-
velocity variants. Record the start instants in TT and TDB, elapsed TDB durations to
identical targets, unit-vector angular separation, component residuals, every warning
or error, the environment/data manifest, and a deterministic output hash. Experiment
output can bound sensitivity for review but cannot determine what I/311 meant, approve
TT, or set a tolerance.

## 5. Proper motion

The following is `SOURCE_SUPPORTED_FACT` plus an existing `PROJECT_DECISION`:

```text
I/311 pmRA = mu_alpha_star = (d alpha / dt) * cos(delta)
```

The normalized field is
`properMotionRaCosDecMilliarcsecondsPerYear`. It maps directly, after unit conversion,
to Astropy's `pm_ra_cosdec`; no additional multiplication or division by
`cos(delta)` is permitted for that interface.

A different library interface must be audited independently. In particular, SOFA
`iauPmsafe` expects the coordinate-angle rate `dRA/dt`, so the I/311 normalized field
must not be passed to it unchanged. Away from the celestial poles the component
conversion is `dRA/dt = mu_alpha_star / cos(dec)` with units converted from mas/year to
radians per Julian year. CDS Catalogue Standard 2.0 defines the I/311/VizieR `yr` unit
as exactly 365.25 days, resolving the numeric rate-unit duration. The I/311
epoch/derivative time scale, near-pole guard, and production numerical/status policy
remain open; the algebraic component relationship and unit duration do not resolve
them.

Required future comparison cases include:

- high-declination handling;
- omitted-cosine and double-cosine failures;
- source-epoch identity;
- positive and negative RA proper motion; and
- nonzero elapsed-time propagation.

The component and numeric rate-unit mappings are resolved. The source epoch/derivative
time scale, production space-motion model, singularity policy, and numerical
acceptance threshold are not.

## 6. Space-motion and source-quality contract

The Milestone 2B parser contract preserves the source fields and evidence. Milestone
2C must not convert that preservation requirement into an unapproved physical model.

| Input/effect | Resolved contract | Still blocked |
|---|---|---|
| Right ascension and declination | Preserve ICRS source values, units, epoch label, and provenance. | Exact production propagation and downstream frame path. |
| `pmRA` and `pmDE` | Preserve both; `pmRA` is explicitly the starred-alpha component. | Target-library mapping other than the reviewed Astropy field; production motion model. |
| Parallax | Preserve the estimate, including a finite negative value; do not reinterpret a negative estimate as missing. | Include/omit decision, distance handling, uncertainty propagation, and failure policy. |
| Radial velocity | Do not synthesize a value or silently substitute zero. | Approved source, missing-value behaviour, perspective-acceleration policy, and omission bound. |
| Formal errors and `UW` | Preserve the recorded uncertainties and weight/covariance evidence. | Covariance reconstruction/use, conditioning policy, propagation, and reviewed omission bound. |
| Solution/multiplicity/quality evidence | Preserve `Sn`, supplements, multiplicity/component, fit, rejection, variability, and related evidence under Milestone 2B. | Scientific suitability of each selected row and effect handling for non-five-parameter solutions. |

Any missing or unsupported input that the approved production model requires must
produce an explicit unavailable/error outcome. Library defaults are not scientific
decisions.

## 7. Time contract

### 7.1 Fixed roles

The following roles are `SOURCE_SUPPORTED_FACT` and normative for the contract:

- UTC represents the external civil-time instant;
- TAI supplies atomic-time continuity in the conversion chain;
- TT supplies the time argument for the selected precession-nutation model; and
- UT1 supplies Earth rotation.

UTC must not silently replace TT or UT1. Every two-part Julian Date or equivalent
value must retain its time-scale label.

RFC 3339 Sections 5.6-5.8 are `SOURCE_SUPPORTED_FACT` for an Internet timestamp
representation with a required `Z` or numeric-offset UTC relationship and for the
conditional syntax of second `60` at an announced positive leap second. They do not
require UFUQ's Z-only subset, select UFUQ's accepted precision, or validate a claimed
leap-second date.

### 7.2 Proposed time-input boundary

The following are `PROJECT_DECISION` proposals. They define the boundary to review;
they do not make source-derived execution available:

- the astronomy boundary receives a `UtcObservationInput`, not an unqualified local
  time, JavaScript `Date`, Unix timestamp, or scale-free Julian Date;
- its canonical text candidate is a restricted RFC 3339 UTC form
  `YYYY-MM-DDTHH:mm:ss[.fraction]Z`, with four-digit Gregorian year, uppercase `T` and
  `Z`, and mandatory seconds;
- numeric offsets and IANA-zone wall times may exist only in an upstream scenario or
  presentation adapter. That adapter must return the resolved UTC text plus original
  input, zone/offset, zone-data version, and ambiguity decision; unresolved folds or
  gaps are invalid and never guessed;
- `-00:00`, an absent offset, calendar-only input, and implicit system-local time are
  invalid at the astronomy boundary;
- `23:59:60Z` is only provisionally tokenizable before data validation and becomes
  syntactically valid only when the approved pinned leap-second artifact confirms that
  exact UTC date. It is invalid for a date known not to contain a positive leap second
  and returns leap-data-unavailable when that validation cannot be performed;
- the time adapter owns UTC-to-TAI-to-TT and UTC-to-UT1 conversion using the approved
  leap/EOP bundle. Downstream transforms consume typed scales and cannot relabel UTC;
  and
- syntactically valid historical or future input outside the approved operating
  domain returns `UNSUPPORTED_DATE`, not a best-effort coordinate.

The maximum accepted fractional precision, rounding rule, approved IANA zones and
zone-data version, fold/gap selection, SOFA dubious-year mapping, and exact wire
serialization remain `HUMAN_REVIEW_REQUIRED`. The earliest/latest accepted instant
remains `AUTHORITY_OR_EVIDENCE_MISSING`; no date is approved merely because a library
can parse it.

## 8. Earth-orientation and oracle-data policy

The production contract must name and hash:

- the IERS baseline, any separately selected corrections, and the exact EOP product;
- `UT1-UTC`, `xp`, `yp`, and any celestial-pole-offset policy;
- leap-second source and file;
- package and file versions/hashes;
- IERS-estimate, final, preliminary, and predictive coverage;
- network, cache, automatic-download, and update behaviour;
- missing, expired, predictive, and out-of-range behaviour; and
- any separately approved degraded approximation and its measured bound.

`PROJECT_DECISION` proposal: ordinary scientific execution is offline and
deterministic. It consumes an immutable prevalidated data bundle whose manifest names
every artifact, source URL, retrieval time, version/issue, byte length, SHA-256,
  coverage, field-level source quality, availability, and scientific approval, plus
  expiry metadata. It performs no download,
in-place refresh, cache fallback, nearest-value substitution, or data mutation during
a request.

Updates are a separate reviewed administrative workflow: acquire from the approved
authority, verify format and status fields, hash the bytes, cross-check leap history,
run offline fixture/warning diffs, approve, and atomically activate a new bundle.
Previous bundles remain addressable for deterministic replay. Publication frequency
does not silently become UFUQ's operational update cadence; that cadence is
`HUMAN_REVIEW_REQUIRED`.

### 8.1 Product and status authority

The following are `SOURCE_SUPPORTED_FACT` from official IERS product metadata and the
`finals2000A` format:

- Bulletin A provides rapid daily `xp`,`yp`,`UT1-UTC` estimates, predictions for up to
  365 days, and `dX`,`dY`; `finals2000A` gives separate IERS/prediction flags for polar
  motion, `UT1-UTC`, and nutation-offset fields;
- Bulletin B provides monthly Earth-orientation information with daily final and
  preliminary `xp`,`yp`,`UT1-UTC`,`dX`,`dY` values and uncertainties; and
- Bulletin C announces a leap second or confirms no step at the next opportunity.

Source flag/quality is field-specific and separate from artifact/field availability and
UFUQ scientific approval. A required value that is blank, absent, predictive,
preliminary, or sourced from a different product cannot inherit a better state from
another field. Missing `UT1-UTC`, `xp`, `yp`, `dX`, or `dY` is not zero.

### 8.2 Evidence already established by the synthetic smoke oracle

The tracked smoke oracle pins CPython `3.14.6`, uv `0.11.32`, Astropy `8.0.1`, PyERFA
`2.0.1.5`, and `astropy-iers-data` `0.2026.7.20.15.31.18`. Its environment manifest
records hashes and coverage for packaged `finals2000A.all` and `Leap_Second.dat`. Smoke
execution disables automatic downloads and general Astropy internet access, blocks
socket connections, uses a fresh temporary cache, and treats degraded IERS accuracy as
an error.

This bounded smoke configuration is a `PROJECT_DECISION` for environment
reproducibility only. It does not approve those files, coverage dates, predictive
rows, or failure rules for production.
Milestone 2C.1 pins the official Astropy `8.0.1` time, coordinate/space-motion, and
IERS pages required for reference design, plus the official PyERFA `2.0.1.5` release
and source hash. The official PyERFA `stable` API displayed `2.0.1.4`, so a
version-matched documentation/tagged-source review or explicit reviewer acceptance
remains `AUTHORITY_OR_EVIDENCE_MISSING` before a source-derived science protocol.

### 8.3 Proposed orthogonal state and failure policy

The following separated vocabularies are `PROJECT_DECISION` proposals. They must not
be collapsed into one status enum:

```text
SourceFieldQuality = FINAL | PRELIMINARY | PREDICTED | IERS_ESTIMATE
ArtifactAvailability = AVAILABLE | STALE | UNAVAILABLE
FieldAvailability = AVAILABLE | UNAVAILABLE | OUT_OF_RANGE
ScientificApproval = APPROVED | NOT_APPROVED | REVIEW_REQUIRED
```

`SourceFieldQuality` records what the authority says about a value: a Bulletin A field
marked `I` is retained as `IERS_ESTIMATE`, not relabelled `FINAL`; Bulletin B final and
preliminary values remain distinct; predictive values remain `PREDICTED` even when
inside file coverage. `ArtifactAvailability` records whether the selected immutable
bytes are present, verified, and within the later approved validity/update rule.
`FieldAvailability` records whether a required field exists and the instant is inside
that field's own coverage/interpolation rule. `ScientificApproval` records UFUQ review
of that exact field/product/quality/domain combination. Source quality cannot imply
availability or approval, and availability cannot imply source quality or approval.

Each required field has an independent record:

```text
EopFieldState {
  field, value, sourceQuality, fieldAvailability,
  sourceProductId, artifactId, artifactHash, rowProvenance,
  coverage, interpolationEvidence, scientificApproval
}
```

`UT1-UTC`, `xp`, `yp`, and each selected `dX`, `dY` retain their own record. When an
official format supplies one flag for a pair, both field records cite that same flag;
neither inherits quality, provenance, coverage, availability, or approval from its
partner or any other field. A mixed instant remains mixed, and every required field
must independently be available and approved.

No `IERS_ESTIMATE`, `PRELIMINARY`, or `PREDICTED` EOP use is approved by this
milestone. Each produces a field-quality/approval non-result unless a named reviewer
later approves that exact field, product, quality, domain, maximum horizon where
applicable, uncertainty/error budget, warning, and endpoint rules. Expired/stale
leap-second data, stale EOP, nearest-value use, extrapolation, zero substitution,
automatic downloads, cached-table discovery, and implicit ERFA built-in fallback
likewise produce non-results.

No degraded astronomy mode is approved. A degraded outcome is reserved but
unreachable until a named degraded mode and warning contract, `EXPERIMENT_REQUIRED`
quantitative effect/interaction bounds, and `HUMAN_REVIEW_REQUIRED` domain, tolerances,
and approval are recorded.

### 8.4 Production stop condition

Production execution is blocked until the final data selection, coverage, update,
offline, interpolation, per-field source-quality/availability/approval, stale/expiry,
and failure policy is approved. No production EOP or leap-second artifact/version/hash is
selected here. The smoke-oracle pins remain smoke-only. Out-of-range operation must
fail explicitly unless a separately labelled degraded mode has a quantitative bound,
mandatory warning contract, and named reviewer approval.

## 9. Observer contract

Every observer input is resolved from a versioned `ObserverPreset`; observer fields may
not be an unlabelled tuple. Resolved `PROJECT_DECISION`:

- `ScientificProfileV1` accepts only preset ID
  `umpsa-pekan-faculty-of-computing`, whose human-readable identity is Faculty of
  Computing, UMPSA Pekan Campus, Pahang, Malaysia;
- latitude is geodetic and north-positive, finite, and within
  `[-90 degrees,+90 degrees]`;
- longitude is east-positive and canonicalized to `[-180 degrees,+180 degrees)`, with
  `+180 degrees` represented as `-180 degrees`; and
- arbitrary coordinates, browser geolocation, implicit `(0,0)`, another preset, or a
  hidden map-provider location are outside V1.

`SOURCE_SUPPORTED_FACT`: SOFA `iauAtco13`/`iauApco13` use east-positive geodetic
longitude, geodetic latitude, and height above the WGS 84 ellipsoid. Astropy
`EarthLocation.from_geodetic` has the same input roles and a WGS 84 default. Those
routine contracts do not select UFUQ's production datum or observer range.

The typed observer-data boundary is:

```text
ObserverPreset {
  schemaVersion,
  presetId,
  siteIdentity,
  referencePointDescription,
  geodeticLatitude { value, unit, northPositive },
  geodeticLongitude {
    value,
    unit,
    eastPositive,
    canonicalNormalization,
    sourceRepresentation
  },
  referenceSystem { kind, id, realization? },
  referenceEllipsoidId,
  coordinateReferenceEpoch:
    | { status: DECLARED, value, representation, scaleOrStandardSemantics, basis }
    | { status: NOT_REQUIRED, basis, source },
  height:
    | { heightType: ELLIPSOIDAL, value, unit, ellipsoidId }
    | { heightType: ORTHOMETRIC, value, unit, verticalDatumId }
    | { heightType: OTHER_APPROVED, value, unit, referenceSurfaceId,
        representationId },
  heightConversion? {
    modelAndVersion,
    inputs,
    provenance,
    outputRepresentation,
    uncertainty
  },
  coordinateAccuracy {
    status,
    componentsOrCovariance?,
    units?,
    confidenceOrCoverageMeaning?,
    method?,
    source,
    reasonWhenUnknown?
  },
  provenance {
    sourceId,
    sourceRecordOrServiceResponseId,
    sourceVersion,
    acquisitionIdentity,
    acquisitionDate,
    licenceOrUseConditions
  },
  dataVersionId,
  artifactIdentity,
  artifactAvailability,
  validationStatus,
  scientificApproval { status, scope, reviewer, decisionDate, decisionReference }
}
```

The following are resolved contract semantics for profile review:

- all coordinate and height values are finite and have explicit units;
- datum/reference frame, realization where applicable, ellipsoid, height type and
  height reference surface are named rather than inferred;
- `referenceSystem.kind` discriminates a geodetic datum from a terrestrial reference
  frame, and the selected reference system/ellipsoid must match the approved route or
  use an approved, provenance-bearing transformation with explicit uncertainty;
- `coordinateReferenceEpoch` is declared when the source/frame requires it, or carries
  a source-supported `NOT_REQUIRED` state; a missing required epoch is unsupported;
- an ellipsoidal-height route accepts an orthometric or other typed source height only
  through an approved, provenance-bearing conversion; no height is silently relabelled;
- accuracy state is `SOURCE_DECLARED`, `DERIVED`, or `UNKNOWN_UNBOUNDED`, with source
  and units retained where applicable; unknown accuracy is never zero;
- artifact availability, structural validation, and scientific approval are separate;
  none can promote another; and
- missing, invalid, unsupported, unavailable, or unapproved data produces a non-result
  rather than a default or coercion. These are distinct semantic states: missing means
  a required field/reference is absent; invalid means malformed representation/value/
  unit/range; unavailable means the identified artifact cannot be resolved; unsupported
  means a well-formed record is incompatible with the approved route/domain; and
  unapproved means activation is absent or rejected. Exact wire/HTTP codes remain
  separate.

Official UMPSA evidence supplies only the selected site identity. Milestone 2D owns the
exact reference point, latitude, longitude, height, datum/frame/ellipsoid, applicable
coordinate epoch, accuracy, source response, acquisition identity/date, licence/use
conditions, version, manifest/hash, and activation approval. An official reproducible
UMPSA institutional or Malaysian-government record with documented accuracy is an
eligible candidate for 2D review when it supplies every required semantic field. The
2D reviewer must approve the represented point, semantics, accuracy, transformations,
provenance, and bounded use; source class alone does not establish scientific adequacy.
A JUPEM survey-control record is optional, not mandatory, and this public-web audit did
not establish a Faculty-specific control record; that is not evidence none exists.

Pekan and Riyadh represent materially different observer geometry and are a useful
later multi-location validation partition. This qualitative distinction neither adds
Riyadh to ProfileV1 nor supplies a numerical position or angular tolerance.

`HUMAN_REVIEW_REQUIRED` after acquisition:

- approval of the selected UMPSA record and any height conversion for pending-validation
  V1 execution;
- whether its stated or unknown-unbounded accuracy is adequate for that approval scope;
  and
- later polar-site, multiple-preset, global-range, and arbitrary-location semantics.

WGS 84 and ellipsoidal height in the synthetic smoke fixtures are bounded fixture
choices, not production approval.

### 9.1 Supported operating domain

`PROJECT_DECISION` proposal: a request is supported only in the intersection of all
approved domains for catalogue propagation, selected astronomical models/ephemeris,
leap-second conversion, every required EOP field, observer datum/location/height,
scenario policy, and scientific tolerance. Product file coverage alone is not the
supported domain.

No earliest/latest instant, future-prediction interval, altitude range, unrestricted
global observer claim, or observer-height interval is approved. Those values remain
`AUTHORITY_OR_EVIDENCE_MISSING` or `HUMAN_REVIEW_REQUIRED` under AST-003/AST-006/
AST-007. When endpoints are eventually selected, their inclusive/exclusive semantics,
leap-second endpoint representation, interpolation-neighbour requirement, and first
outside instant must be versioned and tested. Until then, source-derived execution at
an asserted boundary remains unavailable.

## 10. Horizontal-coordinate convention

The following existing `PROJECT_DECISION` is normative.

### 10.1 Azimuth

```text
0 degrees   = geographic True North
90 degrees  = east
180 degrees = south
270 degrees = west
```

Azimuth increases eastward/clockwise and ordinary defined azimuths are normalized to
`[0 degrees, 360 degrees)`.

### 10.2 Altitude

```text
+90 degrees = zenith
0 degrees   = geometric horizon
-90 degrees = nadir
```

At the zenith or nadir, the direction and altitude may remain valid but azimuth is
undefined. A result must preserve that singular status and must not manufacture an
arbitrary azimuth. Direction comparisons near the singularity use unit-vector angular
separation, not azimuth difference.

The exact serialized representative at the `0/360` wrap, negative-zero handling, and
stable status code remain part of the unresolved API/numerical contract.

## 11. Geometric and refracted states

The following boundaries are `PROJECT_DECISION` proposals:

- `GeometricHorizontalDirection` and `RefractedHorizontalDirection` are distinct,
  immutable scientific states;
- catalogue or geometric altitude must not be relabelled as refracted altitude;
- the first vertical slice requests and exposes geometric altitude only; and
- scene code consumes an approved scientific state and must not apply refraction,
  atmosphere defaults, or apparent-horizon corrections.

The first-slice choice still requires `HUMAN_REVIEW_REQUIRED` approval under AST-004
and does not make the blocked upstream route executable.

### 11.1 Refraction input contract

A requested refracted state consumes an explicit typed `AtmosphereObservation`:

```text
AtmosphereObservation {
  pressureHpa,
  groundTemperatureC,
  relativeHumidityFraction,
  observationWavelengthMicrometres,
  measurementInstant,
  measurementLocation,
  sourceProvenance,
  uncertainty,
  measuredOrDerivedStatus,
  derivationModelAndVersion,
  heightOrLapseAssumptions,
  validationStatus
}
```

`SOURCE_SUPPORTED_FACT`: SOFA `iauRefco` accepts pressure in hPa, temperature in
degrees Celsius, relative humidity in `[0,1]`, and wavelength in micrometres for its
compact refraction model. Observer height and lapse rate are not direct `iauRefco`
inputs. If UFUQ derives ground meteorology from height or another observation, the
derivation model, inputs, units, location/time applicability, provenance, and
uncertainty become required project evidence.

`PROJECT_DECISION`: no default atmosphere is approved. Missing required meteorology
for a requested refracted result yields `REFRACTION_UNAVAILABLE`; it does not invoke a
library default. No pressure, temperature, humidity, wavelength, observer-atmosphere,
height-transfer, or lapse model is supplied silently. A malformed/non-finite value,
unit mismatch, or humidity outside the SOFA input interval yields
`REFRACTION_INPUT_INVALID`. Missing data and invalid data are not interchangeable.

`SOURCE_SUPPORTED_FACT`: Astropy `AltAz` documents library defaults of pressure
`0 hPa`, temperature `0 deg C`, relative humidity `0`, and wavelength `1 micron`, and
uses nonzero pressure to enable refraction. Those defaults describe the independent
reference library only. They are not an approved UFUQ atmosphere. The synthetic smoke
oracle's pressure-zero case proves only that the bounded geometric path runs.

### 11.2 Validity, extrapolation, and warnings

`SOURCE_SUPPORTED_FACT`: Astropy documents the ERFA-based refraction model as
inaccurate below about 5 degrees and warns that near/below zero altitude results or
round trips can become meaningless or highly discrepant. SOFA `iauAtioq` contains a
low-altitude numerical guard. The guard prevents a numerical failure; it does not
establish scientific validity.

`AUTHORITY_OR_EVIDENCE_MISSING`: no source selected here supplies UFUQ's accepted
pressure, temperature, wavelength, observer-height/lapse, or altitude domain. The
documented about-5-degree region is an experiment partition, not a UFUQ threshold or
tolerance. No below-horizon refracted output or extrapolation is approved.

`HUMAN_REVIEW_REQUIRED`: AST-004/006 must approve the exact refraction model/version,
input provenance and ranges, validity boundary, uncertainty treatment, extrapolation
rule, and warning allowlist. Until then, a model-specific outside-domain input yields
`REFRACTION_OUTSIDE_VALID_DOMAIN`; no warning-bearing refracted result is reachable.

## 12. Horizon, visibility, and rendering

### 12.1 Horizon state model

The following separation is a `PROJECT_DECISION`:

- `GeometricHorizonState` compares signed geometric altitude with the astronomical
  local horizontal plane at geometric altitude zero in the approved observer/frame
  convention, before atmospheric refraction. It retains `ABOVE`, `ON`, `BELOW`, or
  `INDETERMINATE_WITHIN_TOLERANCE` plus the tolerance/policy identifier;
- `RefractedApparentHorizonState` means only a model-dependent classification of an
  approved refracted direction relative to apparent altitude zero under the named
  refraction model/policy. It never changes the geometric classification and is not a
  visible skyline, terrain horizon, or library-guard boundary;
- `PhysicalHorizonDipState` consumes a separately reviewed Earth/reference-surface,
  observer-height, and dip model. It is not implied by geometric altitude zero;
- `TerrainObstructionHorizonState` consumes a direction-dependent terrain/obstruction
  profile and provenance, not a SOFA horizon rotation;
- `SceneClipState` records renderer clipping/presentation only; and
- `LearnerHorizonCueState` records an approved educational cue only.

`PROJECT_DECISION`: `BELOW_GEOMETRIC_HORIZON` is a non-terminal classification attached to
an otherwise approved `GeometricHorizontalDirection`, not a terminal failure or a
replacement result. The attached classification preserves the same signed geometric
altitude, azimuth when defined, azimuth-singularity status, ENU direction, scientific
provenance, upstream warnings, and statuses. It is not an apparent-horizon answer,
visible sea or Earth-curvature horizon, observer-height dip, terrain/building decision,
visibility claim, scene clipping command, or learner-eligibility rule.

`AUTHORITY_OR_EVIDENCE_MISSING`: the equality tolerance at zero, physical-horizon
reference surface/dip model, apparent-horizon boundary, terrain/building/obstruction
data, and corresponding uncertainty are absent. `HUMAN_REVIEW_REQUIRED`: AST-004/006
must approve those policies and the treatment of singular/uncertain cases.

### 12.2 Visibility state model

`PROJECT_DECISION`: do not collapse visibility into one boolean. A composite
`VisibilityState` retains independent component states, policy versions, provenance,
and availability for:

- `AstronomicalHorizonClassification`;
- `PhotometricVisibilityState`, including approved band/source, magnitude/null, and
  variability semantics;
- `SolarAltitudeDaylightTwilightState`, retaining Sun altitude separately from any
  unapproved daylight/twilight threshold;
- `AtmosphericExtinctionTransparencyState`;
- `CloudWeatherState`;
- `TerrainObstructionState`;
- `LightPollutionState`;
- `ScreenPresentationState`; and
- `LearnerEligibilityState`.

A rendered star is not evidence of scientific or unaided-eye visibility. `Hp` is not
Johnson `V`, and neither is by itself a visibility claim. No component can promote,
fill, or approve another; in particular, screen presentation and learner eligibility
cannot promote an unavailable scientific component.

`AUTHORITY_OR_EVIDENCE_MISSING`: no approved photometric threshold/band, variability,
daylight/twilight, extinction/transparency, weather/light-pollution, terrain, or
learner-eligibility rule exists. `HUMAN_REVIEW_REQUIRED`: AST-001/004/006/007 must
approve any such component and aggregation policy. Until then a requested aggregate
visibility decision yields `VISIBILITY_POLICY_UNAVAILABLE` without discarding a valid
direction, its pending-or-approved validation state, or its horizon classification.

## 13. Production effect matrix

The statuses below describe the **proposed semantic matrix**, not implemented or
scientifically accepted behaviour. Once the profile and its required input policies
are approved, `INCLUDED` assigns an effect exactly once to the implementable semantic
route. It does not mean the algorithm already exists or that output is scientifically
accepted. Postimplementation experiments, residuals, error-budget population, and
tolerance review gate later acceptance, not permission to execute pending-validation
code. `CONDITIONAL` means the route exposes a deliberate policy branch. `BLOCKED` means
the named effect branch cannot produce a result until its preimplementation input/policy
gate opens. `OMITTED` would require a quantified, reviewed bound; no required effect
currently has such an approved omission.

### 13.1 Candidate inclusion and authority

| Effect | Proposed status | Stage | Authority and library/algorithm candidate | Classification |
|---|---|---|---|---|
| Proper motion | `BLOCKED`; candidate is inclusion from the approved source instant to a declared target epoch and onward to observation. J2000.0 is the selected celestial-interface candidate target only. | S2/S3 | I/311 Appendix G `mu_alpha_star`; SOFA `iauPmsafe` then `iauAtciq`. `iauPmsafe` requires `dRA/dt`, so the adapter converts `mu_alpha_star/cos(dec)` only away from the polar singularity. Routine availability does not supply the missing epoch/derivative scale, RV, warnings policy, or tolerance. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| Parallax, including observer-dependent parallax | `CONDITIONAL`; include only when an approved distance/parallax interpretation is usable, otherwise return unavailable or use a separately approved infinite-distance omission. | S2/S3 | I/311 parallax field; SOFA `iauPmsafe`, `iauApco13`, and `iauAtciq`/`iauPmpx`. | `HUMAN_REVIEW_REQUIRED` |
| Radial velocity and perspective acceleration | `BLOCKED`; do not substitute Astropy's or SOFA's numeric zero for an absent source value. | S2/S3 | SOFA `iauPmsafe` and `iauAtciq`; I/311 supplies no radial-velocity field for this route. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| Frame bias | `INCLUDED` in the proposed semantic ICRS/GCRS-to-CIRS matrix. | S3 | SOFA `iauAtciq` using the bias-precession-nutation matrix prepared by `iauApco13`; IERS TN36 system separation. | `PROJECT_DECISION` |
| Precession-nutation | `INCLUDED` in the proposed semantic model using IAU 2006 precession and IAU 2000A nutation. | S3 | SOFA `iauPnm06a` through `iauApco13`; IERS TN36 Sections 5.3-5.5. TT is the time argument. | `PROJECT_DECISION` |
| Annual aberration | `INCLUDED` in the proposed semantic ICRS-to-CIRS step. | S3 | SOFA `iauAtciq`/`iauAb` with the issue-pinned Earth ephemeris and barycentric observer velocity. | `PROJECT_DECISION` |
| Gravitational light deflection | `CONDITIONAL`: include the SOFA candidate's solar deflection; additional gravitating bodies are outside the baseline until their scope and omission bound are reviewed. | S3 | SOFA `iauAtciq`/`iauLdsun` for the Sun; `iauAtciqn` is only an experiment candidate for multiple bodies. | `EXPERIMENT_REQUIRED` |
| Earth rotation | `INCLUDED` in the proposed semantic CIO/ERA route; UTC is never used as UT1. | S4/S5 | IERS TN36 Eqs. (5.1), (5.14)-(5.15); SOFA `iauEra00`, `iauApco13`, and `iauAtioq`. | `PROJECT_DECISION` |
| Polar motion | `BLOCKED`; candidate requires non-silently sourced `xp`,`yp` and TIO-locator handling rather than zero defaults. | S4/S5 | IERS TN36 polar-motion matrix; SOFA `iauSp00`, `iauPom00`, `iauApco13`, and `iauC2t06a` component checks. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| Celestial pole offsets | `BLOCKED`; the candidate records an explicit observed-offset inclusion/omission policy separate from the built-in IAU 2006-precession/IAU 2000A-nutation model CIP. | S3/S4 | IERS TN36 Section 5.3.3 and the selected IERS EOP product. `iauApco13` cannot accept observed offsets; `iauApco` or an equivalent lower-level context is the revision candidate. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| Diurnal aberration | `INCLUDED` in the proposed semantic CIRS-to-observed step exactly once. | S5 | SOFA `iauApco13` context and `iauAtioq`; Astropy's topocentric-CIRS split is reference-library behaviour and must not be copied mechanically. | `PROJECT_DECISION` |
| Atmospheric refraction | `CONDITIONAL`; S5 is always explicitly geometric, while S6 exists only for an approved nonzero-refraction request. | S6 | SOFA `iauRefco` plus a separate `iauAtioq` evaluation. Astropy `AltAz` is reference-only and documents the pressure switch and low-altitude limitations. | `HUMAN_REVIEW_REQUIRED` |

### 13.2 Inputs, omission consequences, validation, and approval

| Effect | Required inputs | Consequence if omitted | Required validation case | Unresolved limitations | Required reviewer approval |
|---|---|---|---|---|---|
| Proper motion | Approved source epoch/derivative scale and instant; CDS-defined 365.25-day `yr`; RA/Dec; `mu_alpha_star`,`mu_delta`; parallax/RV policy; TDB start/end dates. | Position error grows with elapsed time and source motion; magnitude is unknown without the approved date/source range. | Source-epoch identity; source-to-declared-target-epoch split, including candidate J2000.0; high/negative motion; high-declination omitted/double-cosine guards; near-pole rejection; 2C.1 scale variants. | I/311 epoch/derivative time scale; near-pole coordinate-rate singularity; solution-family suitability; tolerance. | AST-003 astronomy reviewer approves epoch/time-scale interpretation, motion model, polar guard, warnings, and supported range. |
| Parallax | Parallax and uncertainty/covariance; approved positive-distance rule or explicit omission state; observer barycentric/geocentric position and height. | Removes annual/topocentric displacement in a source- and geometry-dependent way; cannot be bounded globally from a catalogue-wide slogan. | Positive/zero/negative parallax; annual extrema; geocentre versus nonzero site/height; missing-distance failure. | Negative/low-significance estimate policy, distance inference, covariance use, selected-row evidence, range/tolerance. | AST-003 reviewer approves usable-distance rule and per-row/solution handling or an omission bound. |
| Radial velocity | Authoritative RV with units/sign/provenance, or an approved explicit missing-value policy; parallax/distance; motion; source/target epochs. | Omits perspective acceleration and distance evolution; effect depends on RV, distance, motion, and elapsed time. | Zero/nonzero/missing/high synthetic RV crossed with parallax and long/short intervals; warning preservation. | I/311 has no RV field; no supplemental source, crossmatch policy, or omission bound is approved. | AST-003 reviewer approves a source and model, or a bounded unavailable/omission policy. |
| Frame bias | ICRS input; pinned SOFA issue and BPN routine/model identity. | Produces an inconsistent ICRS-to-date orientation and a systematic frame offset. | Compare candidate BPN route with an intentionally bypassed-bias guard and composed `atco13`/independent outputs over distributed directions. | Exact production implementation/library and measured tolerance. | AST-003 reviewer approves the SOFA 2023-10-11 model family and implementation mapping. |
| Precession-nutation | Observation TT; IAU 2006 precession, IAU 2000A nutation, and the matching bias-precession-nutation transformation; separately typed celestial-pole-offset policy; two-part JD. | Creates date-dependent systematic celestial-orientation error. | J2000 identity/near-identity; separated dates including future supported endpoints; alternative JD splits; nonzero nutation cases. | Supported dates, observed offsets/corrections, implementation disagreement, and tolerance. | AST-003 reviewer approves model, matching transformation, range, correction policy, and failure behaviour. |
| Annual aberration | Observation instant; pinned Earth position/velocity model/ephemeris; observer barycentric velocity. | Creates season- and direction-dependent apparent-place error. | Synthetic directions parallel/perpendicular/opposite the Earth-velocity vector across seasonal dates; ablation residual. | Ephemeris/version choice, supported dates, omission/error budget, tolerance. | AST-003 reviewer approves ephemeris/model and inclusion mapping. |
| Gravitational light deflection | Observation instant; Sun-observer geometry; source direction; for extra bodies, mass and barycentric ephemeris/limiter inputs. | Error grows near a deflecting body and depends on angular separation; non-solar omission is unbounded for UFUQ until scoped. | Synthetic far/intermediate/near-solar elongations; solar-on/off ablation; separately tagged multiple-body trial if proposed. | Minimum solar elongation, night/day scenario constraints, additional-body scope, supported ephemeris/range, tolerance. | AST-003 reviewer approves solar-only scope or adds named bodies after experiment. |
| Earth rotation | UTC input; leap-second data; `UT1-UTC`; two-part UT1 JD; ERA/CIO convention and SOFA issue. | Gives incorrect local Earth angle/hour angle and horizontal direction; substituting UTC hides EOP dependence. | Nonzero `UT1-UTC`; UTC day and approved leap-second boundaries; alternative JD splits; ERA equation cross-check. | Production leap-second/EOP data, coverage, dubious-date handling, supported range, tolerance. | AST-003 reviewer approves CIO/ERA route, data policy, range, and status mapping. |
| Polar motion | Pinned `xp`,`yp`, TT for `s'`, observer coordinates, and independent source quality, availability, provenance, coverage, and approval for each field. | Misorients the terrestrial frame and local meridian by an EOP- and location-dependent amount. | Nonzero `xp`,`yp`; zero-ablation guard; swapped-sign/order fault; TN36/SOFA opposite-direction matrix check. | Product/corrections, field-quality/availability/approval policy, omission bound, range/tolerance. | AST-003 reviewer approves product, corrections, nonzero handling, and any degraded mode. |
| Celestial pole offsets | Selected IERS `dX`,`dY` or equivalent observed-offset fields, model baseline, and independent source quality, availability, provenance, coverage, and approval for each field. | Leaves the realized CIP at the conventional model rather than the observed orientation; impact is date/data dependent. | Model-only versus nonzero-offset cases; `iauApco13` versus lower-level corrected-context route; sign/application-order fault; preliminary/predicted/stale/out-of-range cases. | Whether required for UFUQ scope, route revision, product mapping, update policy, omission bound, tolerance. | AST-003 reviewer approves inclusion through a lower-level context or a quantified omission over the supported range. |
| Diurnal aberration | Observer geodetic position/height, Earth rotation, observer rotational velocity, context ownership showing it is applied once. | Creates observer-latitude/time-dependent apparent-direction error. | Equatorial and high-latitude observers; east/west hour angles; zero-velocity/polar guard; double-application fault. | Observer datum/height, exact stage ownership in production, range/tolerance. | AST-003 reviewer approves the component mapping and observer model. |
| Atmospheric refraction | Pressure, temperature, relative humidity, wavelength, model/version, geometric input, supported environment/altitude range. | For a geometric-only claim there is no hidden omission because S5 is labelled geometric; a refracted/visibility claim becomes unavailable without this stage. | Pressure-zero identity; nonzero controlled atmosphere above the accepted lower-altitude bound; 5-degree boundary study; horizon/below-horizon rejection; wavelength variants. | Model validity near/below horizon, input authority/defaults, terrain/dip relationship, uncertainty and tolerance. | AST-004 astronomy/education reviewer approves whether S6 is exposed, its inputs/range, and unavailable/failure semantics. |

The presence of an effect in SOFA, ERFA, or Astropy does not select it for UFUQ. No
blocked or conditional row may be coerced to zero, and no omission may be called
negligible without a measured bound over the approved source/date/location range and
AST-006 error budget.

## 14. Structured outcomes

The API must return a discriminated scientific outcome rather than a bare coordinate
or silently coerced fallback. The following semantic outcome families are a
`PROJECT_DECISION` proposal. Their exact serialized schema and HTTP mapping remain
`HUMAN_REVIEW_REQUIRED`:

| Outcome | Result? | Required meaning |
|---|---:|---|
| `INVALID_INPUT` | No | Malformed/non-finite field, invalid calendar or offset, unqualified time, invalid leap-second syntax/date, latitude outside `[-90,+90]`, or structurally invalid observer. Include field and reason; do not coerce. |
| `UNSUPPORTED_DATE` | No | A valid UTC instant lies outside the approved combined operating domain. This is distinct from a missing artifact. |
| `EOP_UNAVAILABLE` | No | `ArtifactAvailability` or a required field's `FieldAvailability` is `UNAVAILABLE`: the selected artifact/field is absent, unreadable, blank, unverified, or hash-mismatched. |
| `EOP_STALE` | No | `ArtifactAvailability` is `STALE` under the later approved validity/update rule. No stale threshold is invented here, and staleness says nothing about source quality or approval. |
| `EOP_FIELD_QUALITY_NOT_APPROVED` | No | One or more required fields have `ScientificApproval = NOT_APPROVED` or `REVIEW_REQUIRED` for their exact `IERS_ESTIMATE`, `PRELIMINARY`, `PREDICTED`, or `FINAL` source-quality/product/domain combination. Return every blocking field and its independent quality/provenance/approval; do not promote fields from another field's quality. |
| `EOP_OUT_OF_RANGE` | No | The instant lies outside required-field coverage/interpolation rules; nearest-value substitution is forbidden. |
| `LEAP_SECOND_DATA_UNAVAILABLE` | No | The approved leap artifact is absent, unreadable, unverified, or hash-mismatched, so required UTC conversion/validation cannot be performed. |
| `LEAP_SECOND_DATA_STALE` | No | The approved leap artifact violates its approved expiration/validity rule. It is not used with a warning-only fallback. |
| `OBSERVER_OUTSIDE_SUPPORTED_DOMAIN` | No | Structurally valid observer data uses an unapproved datum/height/location/range or unresolved polar-site semantics. |
| `SOURCE_ASTROMETRY_UNAVAILABLE` | No | Existing epoch, motion, parallax, RV, solution-quality, or propagation blockers prevent the source state required by the route. |
| `GEOMETRIC_RESULT_PENDING_VALIDATION` | Yes; not scientifically accepted | Geometric horizontal direction produced wholly within the profile's approved input domain and exact approved bundle/policies before postimplementation production/reference, error-budget, and tolerance acceptance is complete. Include provenance identifiers, validation state, warnings/statuses, and singular-azimuth status. This is the only executable V1 success state initially; its name is semantic, not a finalized wire code. |
| `APPROVED_GEOMETRIC_RESULT` | Yes; reserved until scientific acceptance | The same provenance-bearing geometric result only after the applicable postimplementation production/reference partitions, error-budget evidence, operation-specific tolerance, and named review have passed. Preimplementation profile approval or successful execution alone cannot reach this state. |
| `WARNING_BEARING_GEOMETRIC_RESULT` | Conditional | A result plus only explicitly approved warning codes. Any availability or field-quality/approval failure remains a non-result; no current stale, IERS-estimate, preliminary, predicted, missing, zero, or nearest-value case enters this family. |
| `DEGRADED_GEOMETRIC_RESULT` | Reserved | Unreachable in Milestone 2C.3. It requires a named degraded mode, quantitative bound, approved domain/tolerance, provenance, mandatory warning contract, and named reviewer approval. |
| `REFRACTION_NOT_REQUESTED` | No refracted result; geometric result retained | The caller/policy did not request refraction. This is neither unavailable nor invalid and supplies no atmosphere defaults. |
| `REFRACTION_UNAVAILABLE` | No refracted result; geometric result retained | Refraction was requested but required meteorology, provenance, model, or approved policy is absent. This does not invalidate the geometric direction; library defaults are forbidden. |
| `REFRACTION_INPUT_INVALID` | No refracted result; geometric result retained | A supplied refraction-input field is malformed, non-finite, has invalid units, or violates a source-defined input interval such as relative humidity outside `[0,1]`. It does not reclassify core astronomy/observer input. |
| `REFRACTION_OUTSIDE_VALID_DOMAIN` | No refracted result; geometric result retained | Structurally valid atmosphere/direction inputs lie outside an explicitly reviewed model-specific environment or altitude domain. No domain can be inferred from a library guard, and no extrapolated value is substituted. |
| `WARNING_BEARING_REFRACTED_RESULT` | Reserved | Valid, fully provenance-bearing refraction inputs produced a model warning. This result remains unreachable until the exact model/version, model-specific validity and combined supported operating domains, warning allowlist and severity mapping, quantitative bound, scientific tolerance, and named astronomy-review approval exist. |
| `APPROVED_REFRACTED_RESULT` | Conditional result | A separate refracted direction produced from a valid geometric result only after approval of the exact model/version, complete meteorological inputs and provenance, model-specific validity domain, warning policy, scientific tolerance, combined supported operating domain, postimplementation validation, and named astronomy reviewer. It never overwrites the geometric result. It is not currently reachable. |
| `BELOW_GEOMETRIC_HORIZON` | Classification attached to geometric result | A valid geometric direction, at its retained pending or approved validation state, is below the astronomical local horizontal plane at geometric altitude zero. Preserve the same direction, signed altitude, azimuth when defined, singularity state, scientific provenance, upstream warnings, and statuses; do not infer apparent, physical-dip, terrain/building, photometric, screen, or learner visibility. Exact equality/tolerance remains under review. |
| `VISIBILITY_POLICY_UNAVAILABLE` | No aggregate visibility result; scientific direction retained | One or more requested visibility components or their aggregation policy is absent or unapproved. Report components independently; do not convert rendering into scientific visibility. |

The semantic families above are a `PROJECT_DECISION` proposal. The refracted,
below-horizon, and visibility families retain their AST-004/006 blockers; adding a
name does not approve or make a branch executable.

Upstream SOFA, Astropy, PyERFA, and IERS warnings/errors used by the approved path must
be retained in evidence and deliberately mapped. They must not be discarded because a
numeric output was also returned.

The requirement and semantic distinctions are `PROJECT_DECISION`. Exact stable wire
codes, severity, HTTP/API serialization, warning allowlist, and retry behaviour remain
`HUMAN_REVIEW_REQUIRED`. There is no fallback from a non-result to a numeric result.

### 14.1 Deterministic semantic precedence

The validation order is a `PROJECT_DECISION` proposal; exact wire codes remain
`HUMAN_REVIEW_REQUIRED`. Evaluation stops at the first numbered failure level, while
all blocking fields at that level are reported in canonical field order
`UT1-UTC`, `xp`, `yp`, `dX`, `dY`:

1. validate core request structure, finite astronomy/observer numeric values,
   calendar/offset form, and structurally valid observer fields; return `INVALID_INPUT`
   before consulting EOP, refraction, or visibility policy;
2. validate the selected leap artifact and UTC text. For second `60`, unavailable
   takes precedence over stale leap data and returns the corresponding leap-data
   non-result; available data that
   disproves that exact UTC leap date returns `INVALID_INPUT`;
3. after a canonical UTC instant exists, apply the approved combined date domain and
   return `UNSUPPORTED_DATE` before request-specific observer/source/EOP evaluation;
4. apply the approved observer domain, then source-astrometry readiness;
5. evaluate the selected EOP artifact's availability: unavailable before stale;
6. evaluate each required EOP field's availability: unavailable before out of range,
   retaining every blocking field independently; and
7. evaluate each available field's `SourceFieldQuality` and `ScientificApproval`, then
   map only explicitly approved warnings before producing a geometric direction whose
   validation state is explicitly pending or, only after the later acceptance gate,
   approved;
8. classify the geometric horizon without discarding or replacing the direction.
   Attach `BELOW_GEOMETRIC_HORIZON` when applicable while retaining altitude, defined
   azimuth/singularity, direction, provenance, upstream warnings, and statuses; the
   classification does not stop optional-stage evaluation or silently choose
   refraction, visibility, clipping, or learner eligibility;
9. record `REFRACTION_NOT_REQUESTED` when the optional stage was not requested.
   Otherwise validate supplied meteorology before testing policy/model availability
   and then the approved model-specific domain. Map invalid supplied fields to
   `REFRACTION_INPUT_INVALID`, absent required input/policy to
   `REFRACTION_UNAVAILABLE`, and valid inputs outside the approved domain to
   `REFRACTION_OUTSIDE_VALID_DOMAIN`. A model warning maps only to the reserved
   `WARNING_BEARING_REFRACTED_RESULT`; an `APPROVED_REFRACTED_RESULT` is reachable only
   after every approval listed in its outcome definition; and
10. evaluate requested visibility components independently after the scientific
    direction and horizon states. Missing or unapproved policy returns
    `VISIBILITY_POLICY_UNAVAILABLE` without hiding the earlier geometric/refracted
    result. Screen presentation and learner eligibility are evaluated last.

At levels 8-10, the earlier valid geometric result and its validation state are
retained rather than replaced by a later optional-stage non-result. A core invalid timestamp therefore cannot be
reported first as missing meteorology; missing EOP cannot be hidden by below-horizon or
visibility state; and a refraction failure cannot erase the geometric classification.
Where more than one atmosphere field is invalid, report all fields at that level in a
canonical order to be approved with the wire contract.

This order does not approve the provisional outcome names or any currently blocked
date, observer, source, EOP, warning, or degraded branch. If review rejects this order,
the unresolved precedence itself blocks endpoint serialization and combined-fault
fixtures; no implementation may choose an incidental library exception order.

## 15. Scientific error budget and comparison metrics

Resolved `PROJECT_DECISION` requirements:

- compare directions with robust unit-vector great-circle separation;
- compare headings with wrapped circular distance;
- report component residuals as well as total angular separation;
- keep implementation numerics, scientific/reference acceptance, rendering error,
  and learner-answer tolerance separate; and
- fail as unconfigured when a required threshold is absent.

Each approved case must report, where applicable:

- catalogue position and space-motion uncertainty, including correlation policy;
- source-field and supplemental-solution uncertainty;
- omitted-effect bound;
- Earth-orientation/leap-second uncertainty and data status;
- observer-coordinate/datum/height uncertainty;
- reference-algorithm and implementation disagreement;
- floating-point and serialization effects;
- scene-coordinate error; and
- learner-response tolerance as a separate educational/assessment quantity.

No aggregation rule or final threshold is approved. Catalogue formal errors, SOFA
accuracy prose, the van Leeuwen aggregate results, smoke-fixture byte identity, and a
visually plausible sky are not UFUQ acceptance tolerances.

Milestone 2C.5C records the review candidate in
`PHASE1_SCIENTIFIC_ERROR_BUDGET.md` and
`../governance/AST_006_ERROR_BUDGET_LEDGER.v1.json`:

- layers A-F separately retain source/catalogue, propagation/model,
  Earth-orientation/time, observer, atmosphere/refraction, and numerical
  implementation uncertainty;
- scene/render layer G and downstream scenario/learner/assessment layer H are tracked
  separately and may not weaken or redefine astronomy accuracy; scenario generation
  remains its own policy term rather than learner uncertainty;
- the 49 ledger terms comprise 45 terms with an explicitly
  `UNBOUNDED_UNRESOLVED` numerical-bound state and four exact non-numerical aggregate
  guards (`F-002`, `F-003`, `F-004`, and `F-006`), distinct from the 24 Batch checks;
  none contributes a numerical value to a combined budget yet, and this count does
  not move downstream layers G-H into the astronomy budget;
- worst-case bounded sum is the conservative candidate when dependence is unknown;
  RSS is allowed only for evidenced independent zero-mean random terms, while
  correlated/systematic/asymmetric terms require covariance, a joint model, or a
  conservative grouped bound;
- metrics are boundary-specific: great-circle/vector separation for directions,
  component/covariance evidence in the owning frame, signed altitude and wrapped
  azimuth where defined, field-specific time/EOP residuals, and observer-position
  perturbations; and
- azimuth is not a valid universal metric at or near zenith/nadir, while refraction
  and altitude behavior near the horizon require a model- and domain-dependent rule.

The six named classes `ScientificReferenceTolerance`,
`ProductionImplementationTolerance`, `ScenarioGenerationTolerance`,
`SceneAngularTolerance`, `LearnerInteractionTolerance`, and
`AssessmentScoringTolerance` are all `BLOCKED` with no numerical value. The candidate
method is reviewable, but the AST-006 recommendation is
`FINAL_TOLERANCE_NOT_JUSTIFIED`.

## 16. Independent reference protocol

The repository requires a neutral versioned JSON fixture protocol. Each scientific
fixture must contain exact inputs, policies, software/data versions, hashes,
provenance, expected outputs, warnings/statuses, and intended comparisons.

The separately authored, code-independent Python/Astropy producer must:

- import no production UFUQ package;
- invoke no Node astronomy implementation;
- avoid mechanically translating the selected TypeScript algorithm;
- run with locked dependencies and explicit IERS/leap-second files;
- fail on prohibited network/data fallback under the approved offline policy; and
- keep source-derived fixtures out of Git unless the applicable source authority
  permits them.

The tracked synthetic-only reference tool satisfies the environment/code-separation
smoke claim:
it uses a neutral versioned envelope, contains no catalogue identity, imports no
production package, and has byte-identical deterministic output. It is not a
source-derived scientific fixture and cannot activate `test:reference`.

The future scientific comparison matrix must cover:

- I/311 source-epoch identity after the epoch time scale is resolved;
- nonzero/high proper motion and high-declination cosine guards;
- zero, negative, and nonzero parallax under the selected policy;
- zero/nonzero/missing radial velocity under the selected policy;
- UTC boundaries, approved leap-second behaviour, and alternative Julian-date splits;
- nonzero `UT1-UTC`, `xp`, and `yp`;
- meridian, east/west, and azimuth-wrap cases;
- geometric horizon crossing and below-horizon cases;
- zenith/nadir singularities;
- supported-range endpoints and just-outside endpoints;
- invalid latitude, longitude, height, time, and source astrometry;
- unavailable, predictive, expired, and out-of-range IERS data; and
- geometric versus refracted output if refraction is included.

No case may be accepted on an average that hides an individual failure.

Each future scientific comparison fixture must additionally record:

- canonical observer fields, datum/ellipsoid, ellipsoidal-height semantics,
  uncertainty/provenance, normalization policy, and supported-domain status;
- original time text, canonical UTC text, input grammar/precision, UTC/TAI/TT/UT1
  two-part values, and every conversion warning;
- leap and EOP source IDs, immutable artifact versions, byte sizes, SHA-256 hashes,
  artifact availability/expiry and, independently for each EOP field, source quality,
  field availability, scientific approval, coverage, and interpolation
  neighbours, and update-bundle identifier;
- offline/network/cache configuration and evidence that the selected files, rather
  than library built-ins, nearest rows, or network state, supplied the values;
- expected structured outcome, warning set, coordinate state, and the policy IDs that
  made the case supported or unsupported; and
- canonical serialization rules and deterministic fixture/content hashes sufficient
  to reconstruct the result with the named locked environment.

For any 2C.4 case, the fixture additionally records both the geometric state and the
refracted result/non-result; model, routine and version; pressure, temperature,
humidity, wavelength, units, measurement time/location, uncertainty, provenance and
measured/derived status; any height/lapse derivation; validity and warning state; all
six horizon-state types; every requested visibility component; and proof that no
unrecorded library default supplied an input.

### 16.1 Milestone 2C.2 required experiments

Every row below is classified `EXPERIMENT_REQUIRED`. Synthetic cases may be run before
source-derived authority exists; they measure sensitivity and implementation
differences but do not approve a source interpretation, supported range, or tolerance.

| ID | Experiment | Required comparison and evidence |
|---|---|---|
| `2C.2-EXP-01` | Componentized-route equivalence | Compare the proposed `pmsafe` + `apco13`/`atciq` + `atioq` decomposition with composed ERFA `atco13` under identical fully explicit synthetic inputs. Preserve every status and intermediate state. This is same-family consistency evidence, not independence. |
| `2C.2-EXP-02` | Independent-reference disagreement | Compare future production-stage outputs with locked Astropy `SkyCoord`/`CIRS`/`AltAz` results using explicit time, observer, EOP, motion, distance/RV, and pressure policies. Record great-circle/component differences and warning mismatches without a pass threshold until AST-006. |
| `2C.2-EXP-03` | Effect ablation and interaction | Toggle or replace one effect at a time in controlled PyERFA/SOFA-family probes: motion, parallax, RV, bias/precession-nutation, aberration, solar deflection, `UT1-UTC`, polar motion, celestial-pole offsets, diurnal aberration, and refraction. Include interactions and report per-case deltas; one-at-a-time results alone cannot prove a total bound. |
| `2C.2-EXP-04` | Epoch and motion boundary | Run the 2C.1 scale/representation experiment plus source-to-declared-target-epoch and target-to-observation partitions, including the candidate J2000.0 target without treating it as a frame conversion; add high-declination cosine faults, near-pole rejection, alternative two-part-JD splits, and propagation warning cases. |
| `2C.2-EXP-05` | Earth-orientation and range sensitivity | Exercise nonzero/zero `UT1-UTC`, `xp`,`yp`, and candidate celestial-pole offsets; observed/predictive/expired/out-of-range data; UTC/leap boundaries; and candidate supported-range endpoints. Record product/version/hash and fail/approximation status. |
| `2C.2-EXP-06` | Observer, parallax, and velocity policy | Cross geocentric/nonzero observer positions, candidate height semantics, positive/zero/negative parallax, and zero/nonzero/missing/high synthetic RV. Detect double topocentric parallax or diurnal aberration. |
| `2C.2-EXP-07` | Solar and optional multi-body deflection | Sweep synthetic source elongation from the Sun across the proposed scenario domain; if additional bodies are considered, evaluate them separately with pinned ephemerides and identify the maximum omission candidate. |
| `2C.2-EXP-08` | Refraction validity boundary | Compare pressure-zero geometric identity with controlled meteorology/wavelength above the candidate valid-altitude floor and explicit 5-degree, horizon, and below-horizon rejection/availability cases. Do not promote SOFA/Astropy accuracy prose into a UFUQ tolerance. |

### 16.2 Milestone 2C.3 required experiments

Every row is `EXPERIMENT_REQUIRED`. Results quantify consequences and validate status
handling; they cannot select an authority, date range, stale threshold, prediction
policy, or tolerance.

| ID | Experiment | Required comparison and evidence |
|---|---|---|
| `2C.3-EXP-01` | Offline deterministic reconstruction (bounded Batch 01 replay partition) | Use the explicitly named synthetic EOP/leap bundle in fresh cache contexts and independent OS processes within the pre-synchronized locked reference environment; disable network/cache fallback; reproduce canonical bytes, hashes, warnings, and statuses. Clean-environment dependency reconstruction remains outside this bounded run. |
| `2C.3-EXP-02` | EOP state partitions | Exercise source quality, artifact availability, field availability, and scientific approval independently for `UT1-UTC`, `xp`, `yp`, `dX`, and `dY`; cover mixed quality, stale, missing, blank, hash-mismatch, and out-of-range cases, prove one field cannot promote another, and assert no nearest/zero substitution. |
| `2C.3-EXP-03` | EOP degradation sensitivity | Measure nonzero-versus-zero, fresh-versus-candidate-stale, and observed-versus-predicted differences for each field and interactions over candidate domains. Do not enable a degraded outcome without AST-006 tolerances and review. |
| `2C.3-EXP-04` | Leap and timestamp boundaries | Test valid and invalid `23:59:60Z`, adjacent instants, fractional seconds, malformed dates/offsets, `-00:00`, unavailable/expired tables, and UTC-to-TAI/TT/UT1 status preservation against a pinned synthetic bundle. |
| `2C.3-EXP-05` | Observer partitions | Test latitude endpoints and outside values, longitude equivalents/wrap candidate, pole and zenith/nadir singularities, ellipsoidal-height candidates, orthometric-label rejection, non-finite values, and uncertainty/provenance retention. |
| `2C.3-EXP-06` | Operating-domain endpoints and outcome precedence | After endpoints are proposed, test each exact endpoint, required interpolation neighbours, the smallest representable just-outside instants, future prediction boundary, observer-height/location boundaries, every structured outcome, and multi-fault cases at each precedence boundary. |

### 16.3 Milestone 2C.4 required experiments

Every row is `EXPERIMENT_REQUIRED`. Results measure model, input, and policy
consequences; they cannot establish authority, approve a default, choose a validity
threshold, or set a tolerance.

| ID | Experiment | Required comparison and evidence |
|---|---|---|
| `2C.4-EXP-01` | Refraction-model comparison | Compare named primary-authority model candidates under identical explicit synthetic inputs. Record routine/model/version, coefficients, directions, warnings, documented domain, and disagreement. Do not turn agreement into production selection. |
| `2C.4-EXP-02` | Meteorology sensitivity | Sweep pressure, temperature, relative humidity, and wavelength separately and jointly, including uncertainty partitions and any measured/derived variants. Report angular/component changes without inventing accepted ranges. |
| `2C.4-EXP-03` | Near-horizon numerical sensitivity | Probe directions above, around, and below Astropy's documented about-5-degree limitation region and around zero geometric altitude with alternative numerical paths and round trips. A SOFA guard is not a validity oracle. |
| `2C.4-EXP-04` | Geometric versus apparent horizon | Locate model-specific geometric/apparent horizon crossings using explicit atmosphere input while retaining both classifications. Do not introduce terrain or learner rules. |
| `2C.4-EXP-05` | Below-horizon behaviour | Exercise small and large negative geometric altitudes, numerical-guard regions, missing policy, and proposed rejection/non-result states. Verify that no refracted value overwrites the geometric state. |
| `2C.4-EXP-06` | Default-atmosphere consequences | Compare explicit inputs, Astropy library defaults, pressure-zero geometric operation, and UFUQ missing-input rejection. Record deltas to show consequences; do not approve a default from convenience behaviour. |
| `2C.4-EXP-07` | Visibility-policy separation | Vary astronomical horizon, photometric band/value/variability, Sun altitude/daylight/twilight, extinction/transparency, cloud/weather, terrain/obstruction, light pollution, screen presentation, and learner eligibility independently. Prove no component or renderer state promotes another. |

### 16.4 Milestone 2C.5A experiment-execution protocol

`PROJECT_DECISION`: the complete human registry and execution rules are frozen in
`PHASE1_SCIENTIFIC_EXPERIMENT_PROTOCOL.md`; the corresponding machine registry and
Draft 2020-12 fixture/result schemas are under
`tools/astronomy-reference/experiments/`. At the 2C.5A checkpoint they add no numerical
experiment body or result; 2C.5B execution is recorded separately below.

The audit classifies 24 experiment records: 17 are runnable now only with explicit
synthetic inputs and measurement/invariant claims, five are blocked by missing project
decisions, one is blocked by a required independent data/model path, and one is
deferred until production exists. No current family is source-derived. Any I/311 input
would require a separate source-derived execution and restore the source-authority
stop. Synthetic run permission does not approve the later scientific decision.

Astropy and PyERFA remain independent of future production code, but their shared
ERFA/SOFA lineage is recorded for every applicable comparison. Same-family agreement
is consistency evidence only. Numerical results use `MEASURED_NO_ACCEPTANCE` until
AST-006 approves the 2C.5C error-budget method and an operation-specific threshold;
the review-draft ledger itself supplies no acceptance. Only exact, source- or
project-supported invariants may return `PASS` or `FAIL` now.

The executed 2C.5B first batch covers epoch-label guards, route/convention consistency,
motion/cosine/status guards, deterministic replay, and optional-state/no-default/
visibility-separation guards. Its 24 exact checks pass and none fail; six
measurement-only checks cover 27 measurement records, all `MEASURED_NO_ACCEPTANCE`.
It remains synthetic-only and does not activate
`test:reference` because no production/reference comparison exists.

The three epoch-label cases supply an explicit synthetic ITRS-geocentre Cartesian
`[0,0,0] m` location to every affected Astropy `Time` constructor. This controls the
TT/TDB conversion input without selecting a physical observer or production observer
policy. Each case also initializes the exact pinned smoke-only leap artifact consumed
by the conversion path, so isolated execution does not inherit leap state. The schema
rejects a missing/nonzero replacement, result manifests bind the
fixture bytes, and structured statuses preserve the explicit-location fact. All
pre-correction result and replay hashes were invalidated and replaced only by the
complete runner regeneration.

The 2C.5A protocol document is itself a hashed Batch 01 input. Milestone 2C.5C does
not edit it, the registry, schemas, runner, fixtures, environment manifest, or
lockfile. Interpretive additions live in the separate 2C.5C document and AST-006
ledger so the committed result evidence remains valid; changing any hashed input
requires complete Batch regeneration before further interpretation.

## 17. Evidence and decision audit

| ID | Claim/decision | Classification and evidence | Audit result |
|---|---|---|---|
| `2C-001` | Keep catalogue, propagated, celestial-intermediate, geometric horizontal, refracted, visibility, and scene states distinct. | `PROJECT_DECISION`: Astronomy Specification, ADR-003, architecture/data strategy. | `RESOLVED_CONTRACT`. |
| `2C-002` | Treat selected I/311 `RArad`/`DErad` as ICRS catalogue inputs in radians. | `SOURCE_SUPPORTED_FACT`: I/311 `ReadMe`, `hip2.dat` byte description. | `RESOLVED_INPUT_SEMANTICS`. |
| `2C-003` | Interpret `Ep=1991.25` as a representation and exact propagation instant/time scale. | `SOURCE_SUPPORTED_FACT`: I/311 gives the literal label and ESA Gaia DR1 directly calls the I/311 epoch `J1991.25`. `AUTHORITY_OR_EVIDENCE_MISSING`: neither gives the I/311 time scale. | Julian representation resolved; exact instant remains blocked. Preserve the label/representation and return propagation unavailable pending authority or `HUMAN_REVIEW_REQUIRED`. |
| `2C-004` | Interpret I/311 `pmRA` as `mu_alpha_star` and normalize explicitly. | `SOURCE_SUPPORTED_FACT`: I/311 Appendix G Table G.3; project field-name decision. | `RESOLVED_INPUT_SEMANTICS`; production motion model remains open. |
| `2C-005` | Keep UTC, TAI, TT, and UT1 distinct with TT for precession-nutation and UT1 for Earth rotation. | `SOURCE_SUPPORTED_FACT`: SOFA routine contracts; IERS TN36 Chapters 5 and 10. | `RESOLVED_TIME_ROLES`; operational data/failure policy remains open. |
| `2C-006` | Use north-positive latitude, east-positive longitude, north-zero/eastward azimuth, signed altitude, and vector comparison at zenith/nadir. | `PROJECT_DECISION`: Astronomy Specification and ADR-003; SOFA supports the horizon convention. | `RESOLVED_CONVENTIONS`; exact serialization/status code remains open. |
| `2C-007` | Define observer-preset semantics and separate them from concrete site data. | `PROJECT_DECISION`: V1 fixes the generic versioned `ObserverPreset`, north-positive geodetic latitude, east-positive `[-180 deg,+180 deg)` canonical longitude, explicit datum/frame/ellipsoid/typed height/conditional epoch/accuracy/provenance/version/approval states, the UMPSA Pekan Faculty identity, and fail-closed no-default behavior. `SOURCE_SUPPORTED_FACT`: official UMPSA material places the Faculty at Pekan campus. | `RESOLVED_CONTRACT_FOR_PROFILE_REVIEW`; exact reference point, coordinates, height, Earth model, accuracy and artifact are `BLOCKS_2D_DATA_AUTHORITY`. Unknown accuracy remains unbounded, global/polar/multiple-location support remains later, and no Faculty-specific JUPEM control record is claimed. |
| `2C-008` | Select the production algorithm/library, coherent CIO/equinox route, and implement-or-omit effect matrix. | Milestone 2C.2 proposes a componentized SOFA `2023-10-11` CIO-family semantic route and classifies every effect. It does not approve the future TypeScript algorithm/library, blocked inputs, omission bounds, or tolerances. | `PARTIAL_PROPOSAL`; AST-003 profile review remains preimplementation, while experiments run only at their registered lifecycle stages. |
| `2C-009` | Select production leap-second/EOP files, coverage, source-quality approval/offline/update policy, and approximation/failure modes. | Milestone 2C.3 pins the distinct official Bulletin A/B/C roles and `finals2000A` field flags, then proposes immutable offline bundles and orthogonal source-quality/availability/approval semantics. Smoke files/hashes remain smoke-only. | `PARTIAL_PROPOSAL`; product bytes/hashes, precedence, stale/update cadence, field-quality approval, coverage, and degraded mode remain open. |
| `2C-010` | Keep geometric and refracted direction separate; select the Phase 2 refraction model/policy. | Milestone 2C.4 proposes geometric-only first-slice semantics, an explicit atmosphere record, no defaults, and optional refraction non-results. SOFA/Astropy supply input and limitation evidence but do not choose UFUQ policy. | Separation/default prohibition proposed; model, ranges, uncertainty, validity, warnings, and exposure remain `HUMAN_REVIEW_REQUIRED`/`AUTHORITY_OR_EVIDENCE_MISSING` under AST-004/006. |
| `2C-011` | Keep direction, every horizon type, visibility components, and rendering/learner states separate; select actual behaviour. | Milestone 2C.4 defines distinct typed states and makes below-geometric-horizon result-bearing. No source/owner has selected terrain, photometric, daylight, transmission, or learner policy. | Separation proposed; policy remains blocked under AST-001/004/006/007. |
| `2C-012` | Preserve structured scientific outcomes and upstream warnings; fix stable API mapping. | SOFA status contracts plus ADR-003/007. Milestones 2C.3-2C.4 propose core, geometric, refraction, horizon, visibility, warning, and reserved-degraded families with staged precedence. | Semantic families `PARTIAL_PROPOSAL`; stable wire/HTTP mapping and warning allowlists require review. |
| `2C-013` | Use per-case vector/circular metrics and a separated error budget; approve aggregation and tolerances. | Astronomy Specification/ADR-007 plus independent-measurement requirement. | Metrics resolved; budget aggregation and thresholds `BLOCKED_EXPERIMENT_AND_APPROVAL` under AST-006. |
| `2C-014` | Establish a pinned reference path, comparison matrix, and stronger independent oracle. | The locked synthetic-only tool proves environment and production-code independence. Milestone 2C.2 distinguishes the Astropy/PyERFA reference route from the SOFA-based production candidate and names the comparison experiments; 2C.5B executes the first same-family/structural synthetic batch. | `PARTIAL`; source-derived fixtures, a lineage-independent model path for applicable claims, production implementation, and production/reference comparison remain unstarted postimplementation work. |
| `2C-015` | Select supported date/location/altitude range and endpoint failures. | Milestone 2C.3 defines the domain as the intersection of every approved scientific/data/observer/scenario range and fixes explicit endpoint outcomes. Sources expose individual limits but do not select UFUQ endpoints. | Exact one-preset V1 input endpoints remain `AUTHORITY_OR_EVIDENCE_MISSING`/`HUMAN_REVIEW_REQUIRED` under AST-003/AST-007. Broader/global ranges are later extensions; AST-006 owns postimplementation error bounds and numerical acceptance, not endpoint selection. |

### 17.1 Milestone 2C.1 authority audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.1-001` | The exact I/311 field wording supplies ICRS plus `Ep=1991.25` but no representation name or scale. | `SOURCE_SUPPORTED_FACT` | Catalogue-owned wording pinned. |
| `2C.1-002` | ESA Gaia DR1 directly identifies I/311 and calls its parameter epoch `J1991.25`. | `SOURCE_SUPPORTED_FACT` | Julian representation resolved; Besselian and calendar decimal year are not supported interpretations. |
| `2C.1-003` | No inspected I/311-applicable authority states TT/TDB/UTC or an exact two-part Julian Date. | `AUTHORITY_OR_EVIDENCE_MISSING` | Exact propagation instant remains blocked. |
| `2C.1-004` | Preserve the literal label and Julian representation, but make source-derived propagation unavailable while the scale is unresolved. | `PROJECT_DECISION` | Prevents a library default or silent TT transfer from becoming science authority. |
| `2C.1-005` | Approve or reject a bounded TT interpretation if no stronger source is found. | `HUMAN_REVIEW_REQUIRED` | Astronomy reviewer decision remains open under AST-003. |
| `2C.1-006` | Compare explicit candidate interpretations with synthetic motion cases and structured warnings. | `EXPERIMENT_REQUIRED` | Batch 01 executes TT/TDB/UTC, calendar-decimal-year, and Besselian-guard synthetic cases. Measurements cannot decide source meaning or tolerance. |
| `2C.1-007` | Astropy `8.0.1` reference-design pages and the official PyERFA `2.0.1.5` release/source hash are pinned. | `SOURCE_SUPPORTED_FACT` | Astropy documentation gap closed for 2C.1; exact PyERFA distribution is reproducible. |
| `2C.1-008` | Official PyERFA stable API documentation displays `2.0.1.4`, one patch behind the locked `2.0.1.5`. | `AUTHORITY_OR_EVIDENCE_MISSING` | Version-matched documentation/tagged-source review or explicit reviewer acceptance remains open. |

### 17.2 Milestone 2C.2 route and effect audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.2-001` | SOFA `iauAtco13` defines a composed ICRS-catalogue-astrometry-at-J2000.0-epoch to observed chain through `iauApco13`, `iauAtciq`, and `iauAtioq`; this J2000.0 requirement is an epoch input boundary, not a frame conversion. IERS TN36 separately factorizes celestial pole motion, Earth rotation, and polar motion. | `SOURCE_SUPPORTED_FACT` | Authoritative algorithm roles and time/EOP inputs are pinned; they do not select UFUQ production code or resolve blocked source inputs. |
| `2C.2-002` | Propose a componentized SOFA `2023-10-11` CIO-family semantic route with typed catalogue, declared-target-epoch propagated ICRS, observer-aware CIRS, Earth-orientation context, geometric, refracted, visibility, and scene states. J2000.0 is the candidate celestial-interface target epoch, not a frame conversion or a guarantee of the generic propagated-state type. | `PROJECT_DECISION` | Candidate route defined for review; it becomes implementation authority only through the approved profile-scoped 2C.6 decision. |
| `2C.2-003` | Approve the intended pure-TypeScript production implementation/library mapping to the proposed SOFA routine contracts; after code exists, prove that it conforms to the approved mapping. | `HUMAN_REVIEW_REQUIRED` | AST-003 preimplementation mapping review remains open; Astropy is not selected for production. Conformance evidence is postimplementation. |
| `2C.2-004` | Cross the source-to-declared-target-epoch space-motion boundary, with J2000.0 as the selected celestial-interface candidate target. | `AUTHORITY_OR_EVIDENCE_MISSING` | I/311-backed execution is blocked by its epoch/derivative time scale and distance/RV policies; the generic implementation also needs an approved polar guard and warning policy. `iauPmsafe` availability and the separately resolved numeric `yr` duration do not close those blockers. Numerical tolerance remains a postimplementation acceptance gate. |
| `2C.2-005` | Construct the production Earth-orientation context. | `AUTHORITY_OR_EVIDENCE_MISSING` | Blocked by EOP/leap-second product, correction, coverage, update/offline/extrapolation, celestial-pole-offset, and date-range decisions. |
| `2C.2-006` | Include frame bias, IAU 2006 precession with IAU 2000A nutation, annual aberration, ERA-based Earth rotation, and diurnal aberration in the proposed semantic model. | `PROJECT_DECISION` | Proposed semantic inclusions recorded; `included` is not approval or present executability, and implementation mapping, experiments, corrections, and tolerances remain open. |
| `2C.2-007` | Apply parallax only through an approved usable-distance policy and return unavailable or an explicitly reviewed infinite-distance branch otherwise. | `HUMAN_REVIEW_REQUIRED` | Negative/low-significance parallax, covariance, selected-row, and omission-bound decisions remain open. |
| `2C.2-008` | Supply radial velocity or treat perspective acceleration as an approved omission/unavailable branch. | `AUTHORITY_OR_EVIDENCE_MISSING` | I/311 supplies no RV field and no supplemental source/crossmatch policy or omission bound is approved. |
| `2C.2-009` | Bound solar-only versus multiple-body light deflection and every other candidate omission across the approved domain. | `EXPERIMENT_REQUIRED` | Ablation/interaction and elongation studies specified; no result or threshold exists. |
| `2C.2-010` | Keep pressure-zero geometric output normative as a separate state and expose nonzero refraction only under an approved input/range policy. | `HUMAN_REVIEW_REQUIRED` | AST-004 approval and low-altitude experiment remain open. |
| `2C.2-011` | Use Astropy/PyERFA only for the code-independent reference route, with explicit policies and structured warnings; use composed ERFA `atco13` only as a same-family consistency check. | `PROJECT_DECISION` | Reference/production code boundary fixed; Batch 01 executes same-family componentized/composed and bounded motion guards, not lineage-independent scientific validation. |
| `2C.2-012` | Run route-equivalence, production/reference, stronger-independent, effect-ablation, epoch/motion, EOP/range, observer/motion, deflection, and refraction experiments at their registered lifecycle gates. | `EXPERIMENT_REQUIRED` | Batch 01 executes the bounded route-equivalence case and five synthetic convention guards. Production/reference work follows implementation; stronger-independent work is separately lineage-audited where required; refraction work follows a later-scope decision. None can determine a missing source meaning or tolerance. |
| `2C.2-013` | Interpret the I/311/VizieR proper-motion unit `yr` as exactly 365.25 days for numeric conversion to SOFA radians per Julian year. | `SOURCE_SUPPORTED_FACT` | Resolved by CDS Catalogue Standard 2.0 Section 3.2.2; this does not resolve the I/311 epoch/derivative time scale. |

### 17.3 Milestone 2C.3 operating-domain and data-policy audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.3-001` | IERS Bulletin A provides rapid `xp`,`yp`,`UT1-UTC`, predictions, and `dX`,`dY`; `finals2000A` records separate IERS/prediction flags per field. Bulletin B supplies monthly final/preliminary EOP, and Bulletin C announces leap-second decisions. | `SOURCE_SUPPORTED_FACT` | Official roles, fields, publication frequencies, flags, and source-quality distinctions are pinned; no UFUQ product or scientific approval is selected. |
| `2C.3-002` | Use a restricted RFC 3339 UTC text at the astronomy boundary and keep offset/IANA-wall-time resolution in a provenance-preserving upstream adapter. | `PROJECT_DECISION` | Candidate input boundary defined; fractional precision, IANA-zone set/version, fold/gap rules, and wire mapping require review. |
| `2C.3-003` | Accept second `60` only for an instant validated by the approved leap artifact and reject unqualified time/`-00:00` at the astronomy boundary. | `PROJECT_DECISION` | Fail-closed candidate semantics defined; production leap bytes/hash remain missing. |
| `2C.3-004` | Use a versioned `ObserverPreset` with explicit geodetic latitude, east-positive longitude, reference system/realization, ellipsoid, discriminated height and conditional epoch, accuracy, provenance, version, validation, availability, and approval. | `PROJECT_DECISION` | Generic typed observer boundary and `[-180,+180)` canonical longitude are defined; no reference system, height conversion, position, or uncertainty is inferred. |
| `2C.3-005` | Approve the selected preset's concrete reference system/ellipsoid, height representation or conversion, accuracy adequacy, and supported observer domain. | `HUMAN_REVIEW_REQUIRED` | Exact UMPSA data and activation move to 2D; broader height/location ranges and polar semantics remain a later profile concern. SOFA/Astropy behavior does not choose either policy. |
| `2C.3-006` | Execute astronomy offline from an immutable, hash-addressed, prevalidated EOP/leap bundle and update only through a separate reviewed atomic workflow with old bundles retained. | `PROJECT_DECISION` | Proposed deterministic execution/update boundary; production artifact and operational cadence remain open. |
| `2C.3-007` | Keep `SourceFieldQuality`, artifact/field availability, and `ScientificApproval` separate for every required EOP field; Bulletin A `I` is an IERS estimate rather than final, missing/blank is not zero, prediction/preliminary is not final, and file coverage is not the supported domain. | `PROJECT_DECISION` | Orthogonal fail-closed state model defined from official field flags/product roles plus explicit UFUQ approval; no field can promote another. |
| `2C.3-008` | Approve a production EOP product/file, field precedence, per-field source-quality/availability/approval policy, version/hashes, interpolation, and corrections/CPO mapping. | `HUMAN_REVIEW_REQUIRED` | No selection or approval; Earth-orientation execution remains blocked. |
| `2C.3-009` | Approve a production leap artifact/version/hash, Bulletin C cross-check, expiry/validity, and refresh cadence. | `HUMAN_REVIEW_REQUIRED` | No selection or approval; UTC conversion/validation requiring the artifact remains blocked. |
| `2C.3-010` | Treat a source publication frequency, file age, or Astropy default as the UFUQ stale rule. | `AUTHORITY_OR_EVIDENCE_MISSING` | None supplies a project validity threshold, and stale remains distinct from IERS-estimate/final/preliminary/predicted source status. |
| `2C.3-011` | Approve the EOP/leap stale/expiry rule and operational update cadence. | `HUMAN_REVIEW_REQUIRED` | No rule or cadence is selected. |
| `2C.3-012` | Support only the intersection of approved catalogue, model/ephemeris, leap, per-field EOP, observer, and scenario domains. Apply later validation/tolerance approval over that domain rather than using a nonexistent tolerance domain to prevent its definition. | `PROJECT_DECISION` | Domain-composition rule resolved; numerical endpoints and inclusivity remain unapproved. |
| `2C.3-013` | Derive earliest/latest instants, future-prediction limit, observer locations, height/altitude limits, or endpoint inclusion directly from one source/product. | `AUTHORITY_OR_EVIDENCE_MISSING` | No authority selects the combined UFUQ operating domain. |
| `2C.3-014` | Approve numerical operating-domain endpoints and inclusion rules after the component source/model/data/observer domains are available. | `HUMAN_REVIEW_REQUIRED` | No range is invented; source-derived execution remains unavailable at asserted boundaries. Tolerance approval later evaluates results over this domain. |
| `2C.3-015` | Return distinct invalid, unsupported-date, EOP/leap status, observer-domain, approved-result, warning-result, and reserved-degraded outcomes with no non-result fallback. | `PROJECT_DECISION` | Semantic outcome families proposed; exact stable serialization/warning allowlist requires review. |
| `2C.3-016` | Quantify IERS-estimate, predicted, preliminary, stale, zero-filled, nearest-value, extrapolated, or other degraded astronomy over a proposed domain. | `EXPERIMENT_REQUIRED` | No bound exists; `DEGRADED_GEOMETRIC_RESULT` remains reserved and unreachable. |
| `2C.3-017` | Approve any IERS-estimate, predicted, preliminary, stale, zero-filled, nearest-value, extrapolated, or other degraded astronomy after a named mode, quantitative bound, warning contract, and domain/tolerance evidence exist. | `HUMAN_REVIEW_REQUIRED` | None is approved. |
| `2C.3-018` | Reconstruct independent fixtures offline with observer/time/EOP/leap provenance, separate source-quality/availability/approval states, boundary cases, warnings/outcomes, and deterministic hashes. | `PROJECT_DECISION` | Batch 01 proves the bounded synthetic offline/canonical replay transport using smoke-only artifact hashes. Scientific EOP/leap partitions and the other families remain unrun or blocked. |
| `2C.3-019` | Apply deterministic semantic failure precedence before stable wire-code selection. | `PROJECT_DECISION` | Structural input precedes leap-backed UTC validation, combined date, observer, source, EOP artifact, EOP field availability, and field-quality/approval checks; exact serialization remains `HUMAN_REVIEW_REQUIRED`. |

### 17.4 Milestone 2C.4 refraction, horizon, and visibility audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.4-001` | SOFA `iauRefco` accepts pressure, temperature, relative humidity, and wavelength for its compact model; `iauAtioq` consumes coefficients and contains a low-altitude numerical guard. | `SOURCE_SUPPORTED_FACT` | Inputs/routine behavior are pinned; the guard is not validity evidence. |
| `2C.4-002` | Astropy `AltAz` uses nonzero pressure for refraction, documents its library defaults, and reports limited/unreliable behavior below about 5 degrees and near/below zero altitude. | `SOURCE_SUPPORTED_FACT` | Reference behavior is pinned; library defaults and limitation prose do not become UFUQ policy or tolerance. |
| `2C.4-003` | Use geometric altitude only for the first vertical slice, keep refracted direction optional and immutable, and prohibit scene-adapter refraction. | `PROJECT_DECISION` | Proposed semantic boundary; AST-004 approval and all upstream blockers remain. `APPROVED_REFRACTED_RESULT` is unreachable pending every recorded model/input/domain/warning/tolerance/operating-domain/reviewer gate. |
| `2C.4-004` | Require explicit atmosphere observations with units, time/location applicability, provenance, uncertainty, measured/derived status, and any height/lapse derivation. | `PROJECT_DECISION` | Typed input boundary proposed; allowed ranges and provenance sufficiency require review. |
| `2C.4-005` | Approve no default atmosphere; missing required meteorology yields `REFRACTION_UNAVAILABLE`, while invalid supplied data yields `REFRACTION_INPUT_INVALID`. | `PROJECT_DECISION` | Fail-closed proposal; exact serialization remains open. |
| `2C.4-006` | Select exact refraction model/version, input and altitude domain, height/lapse handling, uncertainty, extrapolation, warnings, and below-horizon disposition. | `HUMAN_REVIEW_REQUIRED` | No selection; nonzero refracted output remains unreachable. |
| `2C.4-007` | Infer accepted pressure, temperature, wavelength, height, or altitude limits from SOFA routine signatures, a numerical guard, or Astropy's about-5-degree statement. | `AUTHORITY_OR_EVIDENCE_MISSING` | No UFUQ range or tolerance is invented. |
| `2C.4-008` | Keep geometric, refracted-apparent, physical-dip, terrain/obstruction, renderer, and learner horizon states distinct; treat below-geometric-horizon as a classification attached to the valid geometric direction. | `PROJECT_DECISION` | Typed separation and non-erasing result semantics proposed; altitude, defined azimuth/singularity, provenance, warnings, and statuses are retained. Equality/tolerance and downstream policy remain open. |
| `2C.4-009` | Keep astronomical horizon, photometric/variability, Sun-altitude/daylight/twilight, atmospheric extinction/transparency, cloud/weather, terrain/obstruction, light-pollution, screen, and learner-eligibility visibility components independent. | `PROJECT_DECISION` | No component promotes another; a rendered star is not scientifically visible and no aggregate boolean is approved. |
| `2C.4-010` | Supply authority and approve terrain/dip, photometric band/threshold/variability, daylight/twilight, extinction/transparency/weather/light pollution, and learner eligibility. | `AUTHORITY_OR_EVIDENCE_MISSING` | Requested aggregate visibility returns unavailable until review under AST-001/004/006/007. |
| `2C.4-011` | Extend outcome precedence so core scientific failures precede geometric calculation, attached horizon classification, optional refraction, visibility, rendering, and learner policy; retain earlier valid states. | `PROJECT_DECISION` | The detailed 2C.3 order is preserved; exact wire/HTTP mapping and canonical field order require review. |
| `2C.4-012` | Approve warning-bearing or approved refracted output without exact model/version, complete input provenance, reviewed validity and supported operating domains, quantitative bound, tolerance, warning contract, and named astronomy reviewer. | `HUMAN_REVIEW_REQUIRED` | Neither branch is reachable now. |
| `2C.4-013` | Run seven refraction/input/horizon/visibility experiment families with complete deterministic provenance. | `EXPERIMENT_REQUIRED` | Batch 01 executes only the bounded below-horizon state, no-default-atmosphere, and visibility-separation guards. Numerical model/domain families remain unrun or data/decision blocked; no authority or tolerance follows. |

### 17.5 Milestone 2C.5A experiment-protocol audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.5A-001` | Separate experiment executability from the scientific authority or approval a result may later inform. | `PROJECT_DECISION` | A runnable synthetic measurement cannot promote source, production, policy, domain, omission, degraded-mode, or tolerance status. |
| `2C.5A-002` | Freeze 24 stable experiment records with permitted/prohibited claims, explicit inputs/conventions/artifacts, partitions, lineage, metrics, deterministic hashes, output schema, acceptance mode, reviewer gate, and follow-up decision. | `PROJECT_DECISION` | Human and machine registries plus fixture/result schemas are added; no result instance or experiment body exists. |
| `2C.5A-003` | Astropy high-level transforms and direct PyERFA calls share ERFA/SOFA lineage for the affected calculations. | `SOURCE_SUPPORTED_FACT` | Different Python interfaces do not make them independent algorithms; agreement is same-family consistency only. |
| `2C.5A-004` | Permit numerical pass/fail before an error budget and threshold exist. | `HUMAN_REVIEW_REQUIRED` | Prohibited until AST-006; numerical outputs are `MEASURED_NO_ACCEPTANCE`. Exact deterministic/status/guard invariants remain eligible for pass/fail. |
| `2C.5A-005` | Execute the proposed five-group Batch 01 using only explicit synthetic inputs and the locked reference environment. | `EXPERIMENT_REQUIRED` | No experiment ran in 2C.5A; the exact batch is subsequently executed in 2C.5B. |
| `2C.5A-006` | Create a separate error-budget ledger now. | `PROJECT_DECISION` | Deferred at the 2C.5A checkpoint; result schemas report `NOT_ESTABLISHED_AST_006_OPEN`. Milestone 2C.5C subsequently creates a review-draft ledger without changing those result semantics or approving a threshold. |

### 17.6 Milestone 2C.5B Batch 01 execution audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.5B-001` | Execute exactly nine registered Batch 01 fixtures and no other runnable or blocked experiment. | `PROJECT_DECISION` | Fixed allowlist, scope/partition cross-checks, and rejection tests pass; the five-part `2C.2-EXP-04` scope cannot silently expand. |
| `2C.5B-002` | Promote PyERFA `2.0.1.5` to a direct reference-tool dependency because the runner imports `erfa`. | `PROJECT_DECISION` | Direct dependency and environment kind recorded; version and package artifact hashes unchanged; no unrelated package changes. |
| `2C.5B-003` | Treat componentized-versus-composed ERFA output as independent validation. | `SOURCE_SUPPORTED_FACT` | Prohibited: both branches share ERFA/SOFA lineage. Residuals are `MEASURED_NO_ACCEPTANCE`. |
| `2C.5B-004` | Pass or fail numerical scientific agreement without AST-006. | `HUMAN_REVIEW_REQUIRED` | Prohibited. Six measurement-only checks cover 27 measurement records, all `MEASURED_NO_ACCEPTANCE`, including zero residuals. |
| `2C.5B-005` | Apply exact source/project-supported contract, warning/status, and deterministic guards. | `PROJECT_DECISION` plus `SOURCE_SUPPORTED_FACT` where a SOFA status contract is checked | Twenty-four exact checks pass; none fail. Raw `pmsafe` status `1` and its `ErfaWarning` are both retained. |
| `2C.5B-006` | Preserve a below-horizon geometric result and separate optional refraction/visibility states. | `PROJECT_DECISION` | Exact guards retain signed altitude, azimuth, provenance, warnings/statuses, distinguish not-requested from unavailable, insert no atmosphere defaults, and emit no aggregate visibility claim. |
| `2C.5B-007` | Reproduce canonical fixtures/results offline. | `PROJECT_DECISION` | Nine fixtures and nine results validate; two internal fresh-cache repetitions and two independent OS-process, identical-argv runs in the same locked environment produce identical bytes and SHA-256 values. Clean-environment dependency reconstruction is not established; byte identity is determinism evidence only. |
| `2C.5B-008` | Activate the production/reference suite. | `PROJECT_DECISION` | Not activated: Batch 01 imports no production code and contains no production/reference comparison. |
| `2C.5B-009` | Make the Astropy epoch-label conversion location and leap input explicit without approving observer/leap policy. | `PROJECT_DECISION` | The three affected fixtures/schema/constructors fix synthetic ITRS-geocentre `[0,0,0] m` and initialize the pinned smoke-only leap artifact even in isolated runs; manifests and statuses retain the boundary. This is no physical observer, source interpretation, datum/site or production-leap approval, or production default. Pre-correction evidence was invalidated and runner-regenerated. |

### 17.7 Milestone 2C.5C error-budget audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.5C-001` | Inventory every committed Batch 01 measurement without summarizing away serialized zero residuals. | `MEASURED_SYNTHETIC_SENSITIVITY` | All 27 records, values, units, fixture/result IDs, hashes, lineages, guard context, and budget dispositions are machine checked. Ten epoch/calendar records are descriptive future inputs only; none is currently combinable. |
| `2C.5C-002` | Treat the 24 exact passes as bounded mutation/state-contract guards rather than numerical uncertainty bounds. | `EXACT_CONTRACT_INVARIANT` | Each guard names the mistake class it retires and the source/model/production uncertainty it cannot retire. No guard contributes a numerical budget term. |
| `2C.5C-003` | Separate astronomy layers A-F from scene/render layer G and downstream scenario/learner/assessment layer H. | `CANDIDATE_TOLERANCE_PROPOSAL` | The layer boundary and traceability method are proposed for review; scenario generation remains an independent policy term, and G/H cannot weaken astronomy acceptance. |
| `2C.5C-004` | Combine bounded terms with worst-case, covariance/joint, RSS, or asymmetric rules according to evidenced dependence and distribution. | `CANDIDATE_TOLERANCE_PROPOSAL` | RSS is prohibited without justified independence; any required unbounded term keeps the case and total unbounded. |
| `2C.5C-005` | Approve any numerical tolerance from same-family zeros, deterministic hashes, library behavior, convenient epsilons, or UI needs. | `FINAL_TOLERANCE_NOT_JUSTIFIED` | All six tolerance classes are blocked; no final numerical scientific tolerance is defensible. |
| `2C.5C-006` | Require future multi-date, claimed-observer-domain, motion/parallax/RV, EOP, horizon, supported-endpoint, source-derived, and production/reference evidence. | `INDEPENDENT_VALIDATION_REQUIRED` | ProfileV1 will cover its selected identity instantiated by the eventual 2D-approved preset record and applicable boundary/uncertainty partitions. Multiple-location evidence is required before generalizing to a broader observer domain; same-family ERFA/SOFA consistency remains separate. No geographic range or one-site global tolerance is invented. |
| `2C.5C-007` | Rank the remaining runnable synthetic work without executing it. | `MEASURED_SYNTHETIC_SENSITIVITY` plus `EXACT_CONTRACT_INVARIANT` as applicable | `2C.3-EXP-02`, `2C.3-EXP-05`, and `2C.3-EXP-04` are the proposed next structural/boundary batch, followed by effect, observer/parallax/RV, and refraction/horizon sensitivity work. The ranking is risk/knowledge-value planning, not execution or scientific approval. Separate batch review is still required, and unavailable policy, data, or review prerequisites remain fail-closed. |

## 18. Milestone 2C.6 profile and lifecycle audit

The complete candidate, category definitions, blocker tables, 49-term disposition,
resource report, and corrected roadmap are in
`PHASE1_SCIENTIFIC_PROFILE_V1.md`.

### 18.1 Decisions that still block ScientificProfileV1 implementation

Only these profile-scoped decisions remain preimplementation blockers:

1. approve the `ScientificProfileV1` boundary, typed states, exclusions, and explicit
   pending-validation result status;
2. approve the pure-TypeScript route/library mapping and each effect's included,
   excluded, conditional, or unavailable disposition, including parallax, radial
   velocity, multiple-body deflection, and celestial-pole offsets;
3. approve one exact UTC grammar/precision and bounded date interval with endpoint and
   leap-second semantics;
4. approve exact leap/EOP product classes, artifact-selection requirements, per-field
   quality/availability/interpolation/coverage, offline/expiry/update, and no-degraded
   behavior;
5. make geometric-only output, disabled refraction, no atmosphere defaults, and no
   aggregate visibility normative; and
6. approve fail-closed semantic outcomes, precedence, singularity, warning/status
   preservation, and the distinction between executable and scientifically accepted
   output.

These decisions require the authority, reviewer, approval status/date, rejected
alternatives, implementation consequence, validation consequence, and limitations
specified by repository governance. This audit proposes them; it does not substitute
for named approval.

### 18.2 Work that does not block starting ScientificProfileV1

- I/311 acquisition, licensing, row eligibility, time-scale authority, and permanent
  source selection are `BLOCKS_2D_DATA_AUTHORITY`. The engine rejects an astrometric
  state with unspecified epoch/derivative semantics; it does not assume I/311.
- The exact `umpsa-pekan-faculty-of-computing` reference point, latitude, longitude,
  height, datum/frame/ellipsoid, applicable coordinate epoch, accuracy, provenance,
  licence, version and immutable artifact are `BLOCKS_2D_DATA_AUTHORITY`. Their absence
  blocks real V1 execution, not the generic `ObserverPreset` implementation.
- TypeScript/reference residuals, production floating-point error, supported-domain
  partitions, any stronger independent validation required by the claimed boundary,
  combined error bounds, and numerical tolerances are
  `POST_IMPLEMENTATION_VALIDATION`.
- Multiple/global observer support, refraction, apparent/physical/terrain horizons,
  visibility aggregation, weather, extinction, and light pollution are
  `BLOCKS_LATER_EXTENSION` because the candidate V1 excludes them.
- Arabic/Najdi claims, cultural membership/relationships, routes, learner eligibility,
  interaction, and scoring are `BLOCKS_LEARNER_FACING_CONTENT`.
- Qibla target authority and unrelated later sources are
  `NOT_REQUIRED_FOR_PROFILE_V1`.

The 2C.5C ledger remains exactly 49 terms: 45 numerical-bound states are still
`UNBOUNDED_UNRESOLVED`, four terms remain exact non-numerical guards, all six tolerance
classes remain `BLOCKED`, and the recommendation remains
`FINAL_TOLERANCE_NOT_JUSTIFIED`. No unresolved term becomes zero. The profile triage
changes lifecycle ownership, not scientific magnitude.

### 18.3 Validation lifecycle

`PRE_IMPLEMENTATION` contains authoritative semantics, approved profile decisions,
synthetic guards, the pinned candidate reference environment, and planned fixtures.
It permits implementation but not scientific acceptance.

`POST_IMPLEMENTATION` contains production TypeScript versus pinned-reference cases,
implementation residuals, supported-domain partitions, error-budget population, and
`test:reference` activation.

`STRONGER_INDEPENDENT_VALIDATION` evaluates USNO NOVAS or another genuinely independent
positional-astronomy path. Astropy, PyERFA, ERFA, and SOFA shared-lineage agreement is
not promoted to this stage. NOVAS is a future candidate, not a prerequisite to writing
the first implementation.

## 19. Exit criteria and current outcome

Milestone 2C closes for `ScientificProfileV1` implementation when:

1. the versioned profile names every supported input/state and excluded capability;
2. normalized astrometric frames, epochs/scales, units, motion conventions, and
   missing-value branches are explicit;
3. the profile-scoped transformation route, effect ownership, and production mapping
   are normative;
4. the generic preset-observer contract and selected UMPSA site identity, one UTC/date
   domain, leap/EOP input policy, and offline/fail-closed rules are normative, while the
   exact observer record is explicitly handed to 2D;
5. geometric output, below-horizon classification, singularity behavior,
   warning/status precedence, and pending-validation status are normative;
6. source acquisition, rights, row eligibility, crosswalk, and artifact decisions are
   handed to 2D and cannot be bypassed;
7. production/reference, error-budget, tolerance, and any applicable
   stronger-independent-oracle obligations are registered at their postimplementation
   gates; and
8. broader dates/locations, refraction, visibility, terrain/weather/light pollution,
   scene, and learner rules are explicitly deferred.

Milestone 2C does **not** require TypeScript output, production/reference residuals,
final numerical tolerances, arbitrary-location support, refraction/visibility
implementation, or numerical closure of all 49 error-budget terms.

**Current outcome:** `2C_REMAINS_OPEN_WITH_EXACT_PREIMPLEMENTATION_BLOCKERS`.
Milestones 2C.1-2C.5C retain all source, synthetic, and error-budget evidence without
promotion. Milestone 2C.6 removes the circular gate and narrows the open set to the
six profile decisions in Section 18.1. The absence of production code,
production/reference residuals, and numerical tolerances no longer keeps 2C open.
