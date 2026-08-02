# Phase 1 Milestone 2C: Scientific Behaviour Contract

## Status and verdict

**Evidence audit date:** 2026-08-03

**Milestone status:** OPEN

**Implementation authority:** NOT GRANTED

The tracked source dossiers and project decisions support a stricter contract than the
earlier draft, but they do not close the manual scientific decisions needed for
production astronomy. This audit resolves source-defined input semantics, fixed UFUQ
coordinate conventions, typed state separation, and reference-test requirements.
Milestone 2C.2 now defines a reviewable SOFA-based candidate route and effect matrix,
but it does not approve an executable production implementation or close the epoch,
date-range, Earth-orientation, observer, refraction, visibility, error-budget, or
tolerance decisions on which that route depends.

No astronomy reviewer or owner approval is recorded for those open choices. Milestone
2C therefore remains open and `IMP-009` remains unresolved.

This document does not authorize catalogue parsing, source-derived tracked artifacts,
learner-facing cultural claims, or deployment.

## 1. Purpose

Define the normative behaviour for transforming approved catalogue astrometry into
observer-local directions while keeping scientific calculation, visibility, scene
mapping, and learner scoring separate. It also records which conclusions are already
supported, which are project choices, and which must stop before implementation.

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
- independent reference-test requirements.

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

Milestone 2C.1 and 2C.2 conclusions use only the first five classifications requested
for those audits: `SOURCE_SUPPORTED_FACT`, `PROJECT_DECISION`,
`EXPERIMENT_REQUIRED`, `HUMAN_REVIEW_REQUIRED`, and
`AUTHORITY_OR_EVIDENCE_MISSING`.

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
  `docs/references/studies/astropy-pyerfa-reference-docs.md`; and
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
included effects. Milestone 2C.2 supplies the following candidate for review; its
blocked stages and effect rows remain unavailable rather than being filled by a
default.

### 3.1 Milestone 2C.2 candidate typed route

The proposed production semantics are a componentized, CIO-based route aligned to IAU
SOFA issue `2023-10-11` and IERS TN36 Chapter 5. The proposal uses the SOFA routine
contracts as the algorithm candidate, not Astropy's dynamic transform graph and not an
unversioned claim of "SOFA compatibility." The future production implementation must
be independently authored in the approved TypeScript boundary or use a separately
approved production library. That implementation choice is not made here.

| Stage | Typed state and proposed transition | Authority or algorithm candidate | Required inputs and current disposition | Classification |
|---|---|---|---|---|
| `2C.2-S1` | `CatalogueIcrsState`: immutable I/311 ICRS right ascension, declination, `mu_alpha_star`, `mu_delta`, parallax, uncertainty/quality evidence, and literal `Ep=1991.25` plus Julian representation and unresolved scale. | I/311 `ReadMe`, Appendix G Table G.3, and ESA Gaia DR1 Section 4.2.1. | Preserve source units/provenance and scale status; never relabel as J2000 or TT. | `SOURCE_SUPPORTED_FACT` |
| `2C.2-S2` | `PropagatedIcrsAstrometry`: preliminary ICRS catalogue-astrometry propagation from an approved source instant to an explicitly declared target epoch. The type does not itself imply J2000.0 or a frame transformation. For the selected `iauAtciq`/`iauAtco13` candidate only, the target would be J2000.0. | SOFA `iauPmsafe`; `iauAtco13` and `iauAtciq` Note 1. The candidate target instant is J2000.0 at JD 2451545.0 TT converted, not relabelled, to the TDB date required by `iauPmsafe`. | Source epoch/derivative time scale, coordinate-rate conversion and polar guard, parallax/distance policy, radial-velocity policy, warnings, and acceptance tolerances. The CDS-defined `yr` duration is resolved. **Blocked** while the remaining items are unresolved; routine availability supplies none of them. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| `2C.2-S3` | `ObserverAwareCirsDirection`: transform successfully propagated J2000.0-target ICRS astrometry into a CIRS direction at the observation instant while keeping the observer-aware parallax/aberration context explicit. | Candidate SOFA `iauApco13` model-only context plus `iauAtciq`; ICRS/GCRS covers motion, parallax, solar deflection, and aberration, while GCRS/CIRS applies frame bias and the built-in model CIP/CIO from IAU 2006 precession with IAU 2000A nutation. This convenience branch does not apply observed celestial-pole offsets. | UTC, approved TT/UT1 conversion, Earth ephemeris/model, observer, `UT1-UTC`, polar motion `xp`,`yp`, complete approved space-motion state, SOFA issue/routine IDs, and an explicit `dX`,`dY`-unavailable status. Candidate only. | `PROJECT_DECISION` |
| `2C.2-S4` | `EarthOrientationContext`: an immutable context carrying UTC, TAI, TT, UT1, ERA, polar motion `xp`,`yp`, TIO locator, a separately typed celestial-pole-offset policy/status, IERS product/hash/coverage, predictive status, and approximation status. It is consumed with the CIRS direction rather than hidden in a sidereal-time scalar. | IERS TN36 Eq. (5.1) factorization and Sections 5.3-5.5; SOFA `iauApco13`, `iauEra00`, `iauSp00`, `iauPom00`, and `iauC2t06a` as component checks. `iauApco13` can consume `UT1-UTC`,`xp`,`yp`; it cannot consume observed `dX`,`dY`. | Production leap-second/EOP products, separately pinned later corrections/working material if selected, coverage, offline/update/extrapolation policy, celestial-pole-offset route, and supported dates. **Blocked**; missing values are not zero, and model CIP/CIO is not relabelled as observed-offset-corrected. | `AUTHORITY_OR_EVIDENCE_MISSING` |
| `2C.2-S5` | `GeometricHorizontalDirection`: north-zero/east-positive azimuth, signed geometric altitude, ENU unit vector, observation instant, observer policy, EOP policy, singular-azimuth status, and warnings. | Candidate SOFA `iauAtioq` using the explicit model-only `iauApco13` context with refraction coefficients set to zero; `iauAtco13` is a composed cross-check, not the production API. A later reviewed decomposed context is required if observed celestial-pole offsets are included. | Approved geodetic datum/ellipsoid, ellipsoidal-height semantics/range, EOP context, celestial-pole-offset disposition, and stable status mapping. Route shape is proposed; execution remains blocked by those inputs. | `PROJECT_DECISION` |
| `2C.2-S6` | `RefractedHorizontalDirection`: optional result derived from the same pre-refraction CIRS/geometric evidence and labelled with model, meteorology, wavelength, and validity status. It never overwrites S5. | Candidate SOFA `iauRefco` coefficients consumed by a separate `iauAtioq` evaluation; Astropy `AltAz` is reference-only. | Pressure, temperature, humidity, wavelength, supported altitude/environment range, and unavailable/failure policy. **Conditional** and not approved. | `HUMAN_REVIEW_REQUIRED` |
| `2C.2-S7` | `VisibilityState`: a separate project-policy result that consumes geometric/refracted direction plus only approved horizon, photometric, atmosphere, terrain, and teaching inputs. | UFUQ Astronomy Specification and AST-004; SOFA does not define learner visibility. | Horizon equality, terrain/dip, photometric band, extinction/weather/light-pollution, and below-horizon policies remain blocked. | `PROJECT_DECISION` |
| `2C.2-S8` | `SceneDirection`: a presentation adapter from an approved direction state into the fixed ENU-to-Three axes. It carries the source state/policy ID and makes no visibility or scientific-correction claim. | UFUQ ADR-003/IMP-010. | Approved upstream direction only; rendering cannot fill an unavailable astronomy result. | `PROJECT_DECISION` |

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

### 3.2 Production versus independent reference

`PROJECT_DECISION`: the production candidate and independent reference path remain
different implementations:

- production candidate: an explicitly staged SOFA `2023-10-11` CIO-family semantic
  route whose eventual TypeScript algorithm/library still requires AST-003 approval;
- independent reference: locked Astropy `8.0.1` `SkyCoord`/space-motion and explicit
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

`EXPERIMENT_REQUIRED`: use only synthetic astrometry and the locked oracle to compare:

1. explicit `jyear`/TT as the lineage-based candidate;
2. the same Julian epoch number labelled TDB and UTC, each converted to TDB before
   propagation;
3. `decimalyear`/TT as the distinct calendar-year interpretation; and
4. `byear`/TT as a rejection/guard case, not a source-supported candidate.

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

The existing UFUQ `PROJECT_DECISION` requires an ISO 8601 input with an explicit offset
or an approved IANA zone, resolved to UTC while retaining the original zone/offset for
display and audit.

### 7.2 Open operational choices

The following remain `UNRESOLVED_QUESTION` under AST-003/AST-007:

- accepted input precision and exact serialization;
- approved IANA zones and ambiguous/nonexistent local-time handling;
- leap-second input and data-update behaviour;
- SOFA/Astropy dubious-date warning policy;
- missing `UT1-UTC` behaviour; and
- stable API warning/error mapping.

## 8. Earth-orientation and oracle-data policy

The production contract must name and hash:

- the IERS baseline, any separately selected corrections, and the exact EOP product;
- `UT1-UTC`, `xp`, `yp`, and any celestial-pole-offset policy;
- leap-second source and file;
- package and file versions/hashes;
- observed and predictive coverage;
- network, cache, automatic-download, and update behaviour;
- missing, expired, predictive, and out-of-range behaviour; and
- any separately approved degraded approximation and its measured bound.

Ordinary deterministic execution must record and obey an explicit network/update
policy. Whether production permits any automatic download is part of the unresolved
AST-003 decision.

### 8.1 Evidence already established by the synthetic smoke oracle

The tracked smoke oracle pins CPython `3.14.6`, uv `0.11.32`, Astropy `8.0.1`, PyERFA
`2.0.1.5`, and `astropy-iers-data` `0.2026.7.20.15.31.18`. Its environment manifest
records hashes and coverage for packaged `finals2000A.all` and `Leap_Second.dat`. Smoke
execution disables automatic downloads and general Astropy internet access, blocks
socket connections, uses a fresh temporary cache, and treats degraded IERS accuracy as
an error.

This is `PROVISIONAL_CHOICE` evidence for environment reproducibility only. It does not
approve those files, coverage dates, predictive rows, or failure rules for production.
Milestone 2C.1 pins the official Astropy `8.0.1` time, coordinate/space-motion, and
IERS pages required for reference design, plus the official PyERFA `2.0.1.5` release
and source hash. The official PyERFA `stable` API displayed `2.0.1.4`, so a
version-matched documentation/tagged-source review or explicit reviewer acceptance
remains `AUTHORITY_OR_EVIDENCE_MISSING` before a source-derived science protocol.

### 8.2 Production stop condition

Production execution is blocked until the final data selection, coverage, update,
offline, extrapolation, and failure policy is approved. Out-of-range operation must
fail explicitly unless a separately labelled degraded mode has a quantified bound and
approval.

## 9. Observer contract

Every observer input must explicitly include:

- geodetic latitude;
- east-positive longitude;
- datum/ellipsoid identifier;
- height in metres;
- height type/datum; and
- input provenance and validation status.

Resolved `PROJECT_DECISION`:

- latitude is north-positive and longitude is east-positive;
- latitude must be finite and within `[-90 degrees, +90 degrees]`; and
- observer fields may not be an unlabelled tuple.

`UNRESOLVED_QUESTION`:

- whether production uses WGS 84;
- ellipsoidal versus orthometric/source height and any conversion;
- allowed height range and below-ellipsoid handling;
- the canonical longitude interval and wrap representative;
- polar-site longitude/azimuth semantics;
- whether height contributes to topocentric parallax, horizon dip, or both; and
- approved scenario coordinates and their authority.

WGS 84 and ellipsoidal height in the synthetic smoke fixtures are bounded fixture
choices, not production approval.

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

`PROJECT_DECISION`:

- geometric and refracted direction are distinct states;
- catalogue or geometric altitude must not be relabelled as refracted altitude; and
- scene code must not silently apply refraction.

`UNRESOLVED_QUESTION` under AST-004:

- whether the Phase 2 slice uses geometric altitude only;
- atmospheric pressure, temperature, humidity, and wavelength inputs;
- default-atmosphere policy;
- model and low-altitude validity range;
- behaviour below the geometric horizon; and
- whether unavailable/invalid refraction is an error, warning, or unavailable
  optional result.

The synthetic smoke oracle uses pressure zero. That proves the bounded geometric path
runs; it does not select the production refraction policy.

## 12. Horizon, visibility, and rendering

The following separation is a `PROJECT_DECISION`:

- geometric altitude;
- optional refracted altitude;
- geometric horizon classification;
- project-defined visibility;
- terrain/obstruction handling; and
- renderer clipping/presentation.

A rendered star is not evidence of astronomical visibility. `Hp` is not Johnson `V`,
and neither is by itself a claim about unaided visibility.

The exact horizon boundary, equality rule at zero altitude, terrain/horizon dip,
photometric filter, variability, extinction, weather, light-pollution, below-horizon
teaching, and visibility statuses remain blocked under AST-004.

## 13. Production effect matrix

The statuses below describe the **proposed semantic matrix**, not implemented or
approved behaviour. `INCLUDED` means only that the proposed semantic model contains the
effect once all required inputs, route revisions, experiments, tolerances, and approvals
exist; it does not mean the effect is approved or executable now. `CONDITIONAL` means
the route exposes a deliberate policy branch. `BLOCKED` means no production output may
cross that effect boundary yet. `OMITTED` would require a quantified, reviewed bound;
no required effect currently has such an approved omission.

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
| Polar motion | Pinned `xp`,`yp`, TT for `s'`, IERS product/hash/coverage/status, observer coordinates. | Misorients the terrestrial frame and local meridian by an EOP- and location-dependent amount. | Nonzero `xp`,`yp`; zero-ablation guard; swapped-sign/order fault; TN36/SOFA opposite-direction matrix check. | Product/corrections, predictive/expired/out-of-range policy, omission bound, range/tolerance. | AST-003 reviewer approves product, corrections, nonzero handling, and any degraded mode. |
| Celestial pole offsets | Selected IERS `dX`,`dY` or equivalent observed-offset fields, model baseline, product/hash/status. | Leaves the realized CIP at the conventional model rather than the observed orientation; impact is date/data dependent. | Model-only versus nonzero-offset cases; `iauApco13` versus lower-level corrected-context route; sign/application-order fault; predictive/out-of-range cases. | Whether required for UFUQ scope, route revision, product mapping, update policy, omission bound, tolerance. | AST-003 reviewer approves inclusion through a lower-level context or a quantified omission over the supported range. |
| Diurnal aberration | Observer geodetic position/height, Earth rotation, observer rotational velocity, context ownership showing it is applied once. | Creates observer-latitude/time-dependent apparent-direction error. | Equatorial and high-latitude observers; east/west hour angles; zero-velocity/polar guard; double-application fault. | Observer datum/height, exact stage ownership in production, range/tolerance. | AST-003 reviewer approves the component mapping and observer model. |
| Atmospheric refraction | Pressure, temperature, relative humidity, wavelength, model/version, geometric input, supported environment/altitude range. | For a geometric-only claim there is no hidden omission because S5 is labelled geometric; a refracted/visibility claim becomes unavailable without this stage. | Pressure-zero identity; nonzero controlled atmosphere above the accepted lower-altitude bound; 5-degree boundary study; horizon/below-horizon rejection; wavelength variants. | Model validity near/below horizon, input authority/defaults, terrain/dip relationship, uncertainty and tolerance. | AST-004 astronomy/education reviewer approves whether S6 is exposed, its inputs/range, and unavailable/failure semantics. |

The presence of an effect in SOFA, ERFA, or Astropy does not select it for UFUQ. No
blocked or conditional row may be coerced to zero, and no omission may be called
negligible without a measured bound over the approved source/date/location range and
AST-006 error budget.

## 14. Structured outcomes

The API must return a discriminated scientific outcome rather than a bare coordinate
or silently coerced fallback. At minimum, the design must distinguish:

- invalid input;
- unsupported date or observer;
- unavailable/expired/out-of-range Earth-orientation data;
- dubious time or predictive-data warning;
- incomplete/unsupported source astrometry;
- propagation warning or numerical failure;
- valid geometric direction, including singular azimuth state;
- valid refracted direction; and
- refraction unavailable.

Upstream SOFA, Astropy, PyERFA, and IERS warnings/errors used by the approved path must
be retained in evidence and deliberately mapped. They must not be discarded because a
numeric output was also returned.

The requirement for structured outcomes is a `PROJECT_DECISION`. Exact stable status
codes, severity, API serialization, warning promotion, and retry/fallback behaviour are
`UNRESOLVED_QUESTION`.

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

## 16. Independent reference protocol

The repository requires a neutral versioned JSON fixture protocol. Each scientific
fixture must contain exact inputs, policies, software/data versions, hashes,
provenance, expected outputs, warnings/statuses, and intended comparisons.

The independently authored Python/Astropy producer must:

- import no production UFUQ package;
- invoke no Node astronomy implementation;
- avoid mechanically translating the selected TypeScript algorithm;
- run with locked dependencies and explicit IERS/leap-second files;
- fail on prohibited network/data fallback under the approved offline policy; and
- keep source-derived fixtures out of Git unless the applicable source authority
  permits them.

The tracked synthetic-only oracle satisfies the environment/independence smoke claim:
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

## 17. Evidence and decision audit

| ID | Claim/decision | Classification and evidence | Audit result |
|---|---|---|---|
| `2C-001` | Keep catalogue, propagated, celestial-intermediate, geometric horizontal, refracted, visibility, and scene states distinct. | `PROJECT_DECISION`: Astronomy Specification, ADR-003, architecture/data strategy. | `RESOLVED_CONTRACT`. |
| `2C-002` | Treat selected I/311 `RArad`/`DErad` as ICRS catalogue inputs in radians. | `SOURCE_SUPPORTED_FACT`: I/311 `ReadMe`, `hip2.dat` byte description. | `RESOLVED_INPUT_SEMANTICS`. |
| `2C-003` | Interpret `Ep=1991.25` as a representation and exact propagation instant/time scale. | `SOURCE_SUPPORTED_FACT`: I/311 gives the literal label and ESA Gaia DR1 directly calls the I/311 epoch `J1991.25`. `AUTHORITY_OR_EVIDENCE_MISSING`: neither gives the I/311 time scale. | Julian representation resolved; exact instant remains blocked. Preserve the label/representation and return propagation unavailable pending authority or `HUMAN_REVIEW_REQUIRED`. |
| `2C-004` | Interpret I/311 `pmRA` as `mu_alpha_star` and normalize explicitly. | `SOURCE_SUPPORTED_FACT`: I/311 Appendix G Table G.3; project field-name decision. | `RESOLVED_INPUT_SEMANTICS`; production motion model remains open. |
| `2C-005` | Keep UTC, TAI, TT, and UT1 distinct with TT for precession-nutation and UT1 for Earth rotation. | `SOURCE_SUPPORTED_FACT`: SOFA routine contracts; IERS TN36 Chapters 5 and 10. | `RESOLVED_TIME_ROLES`; operational data/failure policy remains open. |
| `2C-006` | Use north-positive latitude, east-positive longitude, north-zero/eastward azimuth, signed altitude, and vector comparison at zenith/nadir. | `PROJECT_DECISION`: Astronomy Specification and ADR-003; SOFA supports the horizon convention. | `RESOLVED_CONVENTIONS`; exact serialization/status code remains open. |
| `2C-007` | Select datum/ellipsoid, height semantics/range, longitude representative, and approved observer locations. | Sources require explicit inputs but do not select UFUQ values. | `BLOCKED_PROJECT_DECISION` under AST-003/AST-007. |
| `2C-008` | Select the production algorithm/library, coherent CIO/equinox route, and implement-or-omit effect matrix. | Milestone 2C.2 proposes a componentized SOFA `2023-10-11` CIO-family semantic route and classifies every effect. It does not approve the future TypeScript algorithm/library, blocked inputs, omission bounds, or tolerances. | `PARTIAL_PROPOSAL`; AST-003 review and 2C.2 experiments remain required. |
| `2C-009` | Select production leap-second/EOP files, coverage, predictive/offline/update policy, and approximation/failure modes. | Smoke files/hashes are pinned only for a bounded synthetic oracle. Astropy `8.0.1` reference-design docs are pinned; PyERFA's official stable-doc/runtime patch mismatch is recorded. | `BLOCKED_PROJECT_DECISION`; the PyERFA documentation acceptance and all production data/policy choices remain open. |
| `2C-010` | Keep geometric and refracted direction separate; select the Phase 2 refraction model/policy. | Separation is a `PROJECT_DECISION`; SOFA shows required meteorological inputs and limitations. | Separation resolved; policy `BLOCKED_PROJECT_DECISION` under AST-004. |
| `2C-011` | Keep direction, horizon, visibility, and rendering separate; select actual visibility/horizon behaviour. | Separation is a `PROJECT_DECISION`; no source/owner has selected the policy. | Separation resolved; policy `BLOCKED_PROJECT_DECISION` under AST-004. |
| `2C-012` | Preserve structured scientific outcomes and upstream warnings; fix stable API mapping. | SOFA status contracts plus ADR-003/007. | Requirement resolved; exact mapping `BLOCKED_PROJECT_DECISION`. |
| `2C-013` | Use per-case vector/circular metrics and a separated error budget; approve aggregation and tolerances. | Astronomy Specification/ADR-007 plus independent-measurement requirement. | Metrics resolved; budget aggregation and thresholds `BLOCKED_EXPERIMENT_AND_APPROVAL` under AST-006. |
| `2C-014` | Establish an independent, pinned scientific oracle and comparison matrix. | Locked synthetic-only oracle proves environment/independence smoke. Milestone 2C.2 distinguishes the Astropy/PyERFA reference route from the SOFA-based production candidate and names the comparison experiments. | `PARTIAL`; reference implementation expansion, source-derived fixtures, and production comparison remain unstarted. |
| `2C-015` | Select supported date/location/altitude range and endpoint failures. | Sources expose model/data limits but do not select UFUQ scope. | `BLOCKED_PROJECT_DECISION` under AST-003/AST-007. |

### 17.1 Milestone 2C.1 authority audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.1-001` | The exact I/311 field wording supplies ICRS plus `Ep=1991.25` but no representation name or scale. | `SOURCE_SUPPORTED_FACT` | Catalogue-owned wording pinned. |
| `2C.1-002` | ESA Gaia DR1 directly identifies I/311 and calls its parameter epoch `J1991.25`. | `SOURCE_SUPPORTED_FACT` | Julian representation resolved; Besselian and calendar decimal year are not supported interpretations. |
| `2C.1-003` | No inspected I/311-applicable authority states TT/TDB/UTC or an exact two-part Julian Date. | `AUTHORITY_OR_EVIDENCE_MISSING` | Exact propagation instant remains blocked. |
| `2C.1-004` | Preserve the literal label and Julian representation, but make source-derived propagation unavailable while the scale is unresolved. | `PROJECT_DECISION` | Prevents a library default or silent TT transfer from becoming science authority. |
| `2C.1-005` | Approve or reject a bounded TT interpretation if no stronger source is found. | `HUMAN_REVIEW_REQUIRED` | Astronomy reviewer decision remains open under AST-003. |
| `2C.1-006` | Compare explicit candidate interpretations with synthetic motion cases and structured warnings. | `EXPERIMENT_REQUIRED` | Experiment specified; output cannot decide source meaning or tolerance. |
| `2C.1-007` | Astropy `8.0.1` reference-design pages and the official PyERFA `2.0.1.5` release/source hash are pinned. | `SOURCE_SUPPORTED_FACT` | Astropy documentation gap closed for 2C.1; exact PyERFA distribution is reproducible. |
| `2C.1-008` | Official PyERFA stable API documentation displays `2.0.1.4`, one patch behind the locked `2.0.1.5`. | `AUTHORITY_OR_EVIDENCE_MISSING` | Version-matched documentation/tagged-source review or explicit reviewer acceptance remains open. |

### 17.2 Milestone 2C.2 route and effect audit

| ID | Conclusion | Classification | Result |
|---|---|---|---|
| `2C.2-001` | SOFA `iauAtco13` defines a composed ICRS-catalogue-astrometry-at-J2000.0-epoch to observed chain through `iauApco13`, `iauAtciq`, and `iauAtioq`; this J2000.0 requirement is an epoch input boundary, not a frame conversion. IERS TN36 separately factorizes celestial pole motion, Earth rotation, and polar motion. | `SOURCE_SUPPORTED_FACT` | Authoritative algorithm roles and time/EOP inputs are pinned; they do not select UFUQ production code or resolve blocked source inputs. |
| `2C.2-002` | Propose a componentized SOFA `2023-10-11` CIO-family semantic route with typed catalogue, declared-target-epoch propagated ICRS, observer-aware CIRS, Earth-orientation context, geometric, refracted, visibility, and scene states. J2000.0 is the candidate celestial-interface target epoch, not a frame conversion or a guarantee of the generic propagated-state type. | `PROJECT_DECISION` | Candidate route defined for review; no implementation authority. |
| `2C.2-003` | Select the actual pure-TypeScript production implementation/library and prove its mapping to the proposed SOFA routine contracts. | `HUMAN_REVIEW_REQUIRED` | AST-003 astronomy review remains open; Astropy is not selected for production. |
| `2C.2-004` | Cross the source-to-declared-target-epoch space-motion boundary, with J2000.0 as the selected celestial-interface candidate target. | `AUTHORITY_OR_EVIDENCE_MISSING` | Blocked by the I/311 epoch/derivative time scale, distance/RV policies, polar guard, warning policy, and tolerances. `iauPmsafe` availability and the separately resolved numeric `yr` duration do not close those blockers. |
| `2C.2-005` | Construct the production Earth-orientation context. | `AUTHORITY_OR_EVIDENCE_MISSING` | Blocked by EOP/leap-second product, correction, coverage, update/offline/extrapolation, celestial-pole-offset, and date-range decisions. |
| `2C.2-006` | Include frame bias, IAU 2006 precession with IAU 2000A nutation, annual aberration, ERA-based Earth rotation, and diurnal aberration in the proposed semantic model. | `PROJECT_DECISION` | Proposed semantic inclusions recorded; `included` is not approval or present executability, and implementation mapping, experiments, corrections, and tolerances remain open. |
| `2C.2-007` | Apply parallax only through an approved usable-distance policy and return unavailable or an explicitly reviewed infinite-distance branch otherwise. | `HUMAN_REVIEW_REQUIRED` | Negative/low-significance parallax, covariance, selected-row, and omission-bound decisions remain open. |
| `2C.2-008` | Supply radial velocity or treat perspective acceleration as an approved omission/unavailable branch. | `AUTHORITY_OR_EVIDENCE_MISSING` | I/311 supplies no RV field and no supplemental source/crossmatch policy or omission bound is approved. |
| `2C.2-009` | Bound solar-only versus multiple-body light deflection and every other candidate omission across the approved domain. | `EXPERIMENT_REQUIRED` | Ablation/interaction and elongation studies specified; no result or threshold exists. |
| `2C.2-010` | Keep pressure-zero geometric output normative as a separate state and expose nonzero refraction only under an approved input/range policy. | `HUMAN_REVIEW_REQUIRED` | AST-004 approval and low-altitude experiment remain open. |
| `2C.2-011` | Use Astropy/PyERFA only for the independent reference route, with explicit policies and structured warnings; use composed ERFA `atco13` only as a same-family consistency check. | `PROJECT_DECISION` | Reference/production independence boundary fixed; scientific fixtures and comparisons remain unstarted. |
| `2C.2-012` | Run route-equivalence, independent-reference, effect-ablation, epoch/motion, EOP/range, observer/motion, deflection, and refraction experiments before approval. | `EXPERIMENT_REQUIRED` | Eight experiment families specified; none can determine a missing source meaning or tolerance. |
| `2C.2-013` | Interpret the I/311/VizieR proper-motion unit `yr` as exactly 365.25 days for numeric conversion to SOFA radians per Julian year. | `SOURCE_SUPPORTED_FACT` | Resolved by CDS Catalogue Standard 2.0 Section 3.2.2; this does not resolve the I/311 epoch/derivative time scale. |

## 18. Decisions still blocking implementation

### 18.1 Evidence gaps

- I/311-applicable evidence or named reviewer approval for the exact `J1991.25`
  propagation and proper-motion derivative time scale; the Julian representation and
  CDS-defined 365.25-day `yr` duration are resolved, but the scale is not;
- an authoritative radial-velocity source/crossmatch policy or a measured, reviewed
  perspective-acceleration omission/unavailable policy;
- version-matched PyERFA documentation/tagged-source review or explicit acceptance of
  the official stable-doc/runtime patch mismatch; Astropy `8.0.1` reference-design
  documentation is pinned;
- a selected and hashed production EOP/leap-second dataset and supported coverage;
- an approved celestial-pole-offset and IERS-correction policy;
- source-derived independent cases after catalogue-processing authority permits them;
- the eight 2C.2 route/effect experiments, including measured effect/omission
  sensitivity and production/reference disagreement; and
- a per-case scientific error budget.

### 18.2 Manual scientific/project decisions

- AST-003: approve, revise, or reject the proposed SOFA-based CIO route and each effect
  status; select the production TypeScript implementation/library, date range, observer
  datum and height semantics, time/EOP/leap-second/celestial-pole-offset policy, and
  failure/degraded modes;
- AST-004: refraction, horizon, below-horizon, photometric, and visibility policy;
- AST-006: error aggregation and operation-specific scientific/reference tolerances;
- AST-007: supported observer/time scenario inputs and boundary semantics; and
- exact structured status/error/warning serialization for the production contracts.

These decisions require the authority, reviewer, approval status/date, rejected
alternatives, implementation consequence, validation consequence, and limitations
specified by the repository governance records. This audit is not a substitute for
that approval.

## 19. Exit criteria and current outcome

Milestone 2C is complete only when:

- every blocking decision above is approved or explicitly deferred with a consequence
  that removes the affected behaviour from the implemented scope;
- the I/311 epoch has an approved propagation interpretation or source-derived
  propagation is explicitly unavailable;
- the production algorithm/effect matrix, supported range, observer policy, and
  leap-second/EOP policy are normative;
- structured warning/error and singular-result behaviour is defined;
- the independent scientific fixture protocol and case matrix are approved;
- the error-budget method and scientific/reference thresholds are approved;
- scientific, rendering, and learner tolerances remain separate; and
- no catalogue parser or production implementation is presented as approved by this
  document.

**Current outcome:** the contract is evidence-audited but not approved for production.
Milestone 2C.1 precisely bounds the epoch authority and documentation gaps but does not
close the time-scale blocker. Milestone 2C.2 defines a classified candidate route,
effect matrix, independent-reference boundary, and experiment programme without
approving the implementation or any blocked input/policy. Milestone 2C remains
**OPEN**.
