# Astronomy model synthesis

## Scope and authority

This synthesis compares the current-phase astronomy sources:

1. exact routines and contracts in IAU SOFA issue `2023-10-11`;
2. the official registered IERS Conventions (2010) TN36 baseline, with later corrected
   chapters/non-registered working versions and separately linked non-official
   supporting documentation kept distinct;
3. the official ESA 1997 guide for original-catalogue semantics;
4. official Hipparcos I/311 metadata, Appendix G field tables, and van Leeuwen's
   validation study;
5. official IERS Bulletin A/B/C product metadata and `finals2000A` format/status
   documentation;
6. RFC 3339 and the IANA tzdb release archive for timestamp/leap transport semantics;
7. CDS *Standards for Astronomical Catalogues* Version 2.0 for the VizieR `yr` unit;
8. *Fundamental Astronomy* as explanatory support; and
9. the *Explanatory Supplement* only as an unresolved explanatory source because the
   local candidate is text-unavailable and completeness/provenance are unverified.

Project documents choose UFUQ behavior. None of these sources chooses the production
catalogue, observer, date range, refraction policy, approximation policy, learner
tolerance, or rendering contract.

## Shared model

The sources support a typed chain rather than one undifferentiated “star position”:

```text
catalogue astrometry at a declared frame and epoch
-> approved space-motion propagation
-> geocentric/celestial intermediate transformation
-> Earth rotation and terrestrial orientation
-> observer-dependent observed/horizontal direction
-> separately defined visibility and scene mapping
```

SOFA's `iauAtco13` exposes one composed ICRS-to-observed path. Its preamble and
`iauApco13` assign motion, parallax, light deflection, aberration, frame
bias/precession-nutation, Earth rotation, polar motion, diurnal effects, horizon
rotation, and refraction to distinct stages. IERS TN36 Chapter 5 independently
factorizes terrestrial/celestial orientation into polar motion, Earth rotation, and
celestial pole motion. *Fundamental Astronomy* Chapter 2 explains the catalogue,
mean/apparent, and observer-local distinctions but is not the implementation authority.

## Milestone 2C.2 proposed route

`PROJECT_DECISION`: the review candidate is a componentized SOFA `2023-10-11`
CIO-family semantic route, not an Astropy production call:

```text
I/311 CatalogueIcrsState at J1991.25 with unresolved scale
-> blocked iauPmsafe candidate to PropagatedIcrsAstrometry at a declared target epoch
-> iauApco13 model-only context + iauAtciq ObserverAwareCirsDirection
-> explicit EarthOrientationContext (TT, UT1, ERA, xp, yp, offset policy, data status)
-> iauAtioq GeometricHorizontalDirection with refraction coefficients zero
-> optional separate iauRefco/iauAtioq RefractedHorizontalDirection
-> separate VisibilityState
-> separate SceneDirection
```

For the selected celestial-interface candidate, the declared propagation target is
J2000.0. This is an epoch input boundary, not an ICRS frame transformation, and no
source-derived state exists while the epoch/space-motion inputs remain blocked.
Routine availability does not resolve the I/311 epoch or derivative time scale,
missing radial velocity, warnings, or tolerances.

The candidate semantic model includes frame bias, IAU 2006 precession with IAU 2000A
nutation, annual aberration, solar deflection, ERA-based Earth rotation, and diurnal
aberration; `included` does not mean approved or executable.
Proper-motion propagation, parallax, radial velocity, polar motion, celestial-pole
offsets, and refraction retain blocked or conditional gates. The full per-effect inputs,
omission consequences, validation cases, limitations, and reviewer approvals are in the
Scientific Behaviour Contract.

SOFA `iauApco13` is only the convenience candidate: it chooses the SOFA Earth
ephemeris and built-in model CIP/CIO from IAU 2006 precession with IAU 2000A nutation.
It accepts `UT1-UTC` and polar motion `xp`,`yp`, but has no observed celestial-pole-
offset `dX`,`dY` input. Polar motion and observed celestial-pole offsets are distinct
EOP responsibilities. If observed offsets or an external ephemeris are approved, the
production route must use lower-level `iauApco`-family inputs or an equivalent explicit
context rather than silently retaining `iauApco13`.

`AUTHORITY_OR_EVIDENCE_MISSING`: the source epoch/derivative scale, radial velocity,
production EOP/leap-second/correction product and policy, supported range, observer
semantics, and tolerances still block executable source-derived output. CDS Catalogue
Standard 2.0 resolves the numeric `yr` duration as 365.25 days.

`HUMAN_REVIEW_REQUIRED`: AST-003 must approve, revise, or reject the semantic route and
the actual pure-TypeScript implementation/library. AST-004 separately owns nonzero
refraction and visibility policy.

`EXPERIMENT_REQUIRED`: route decomposition, independent Astropy disagreement, effect
ablation/interactions, epoch/motion, EOP/range, observer/parallax/RV, deflection, and
refraction boundary experiments must precede approval.

## Milestone 2C.3 operating-domain proposal

`PROJECT_DECISION`: the proposed astronomy request boundary is fail-closed and
deterministic:

- the observer is a typed geodetic record with north-positive latitude, east-positive
  longitude, explicit normalization, datum/ellipsoid, ellipsoidal height, provenance,
  uncertainty, and validation status;
- the astronomy time uses a UFUQ-selected Z-only restricted subset of RFC 3339.
  Offset/IANA-zone wall time is resolved upstream with original input and zone-data
  provenance retained;
- UTC-to-TAI/TT/UT1 conversion and leap validation consume an immutable approved data
  bundle; request-time networking, cache discovery, in-place refresh, nearest-value
  substitution, and zero EOP defaults are prohibited;
- source quality, artifact/field availability, provenance, coverage, and scientific
  approval are separate dimensions for every required EOP field; one field cannot
  promote another, and any unavailable or unapproved required field blocks; and
- supported execution is the intersection of every approved catalogue, model,
  ephemeris, leap, EOP-field, observer, scenario, and tolerance domain.

`SOURCE_SUPPORTED_FACT`: IERS Bulletin A supplies rapid and predictive EOP and the
official `finals2000A` format distinguishes IERS/prediction status for polar motion,
`UT1-UTC`, and `dX`,`dY`. Bulletin B distinguishes final and preliminary values.
Bulletin C announces leap-second decisions but is not itself the selected production
machine-readable leap artifact. RFC 3339 defines the broader timestamp and conditional
leap-second syntax; UFUQ's Z-only subset is a project proposal. SOFA/Astropy define
geodetic/east-positive/ellipsoidal observer roles for the candidate routes.

`AUTHORITY_OR_EVIDENCE_MISSING`: no production EOP or leap artifact/hash, field
precedence/interpolation, stale rule, date endpoint, prediction horizon, height or
location range, precision, or tolerance exists.

`HUMAN_REVIEW_REQUIRED`: approve the production product bundle and update cadence;
per-field source-quality/availability/approval policy; WGS 84, longitude representative,
height/location/polar semantics; UTC precision/zone adapter; endpoints; and warning/
outcome serialization.

`EXPERIMENT_REQUIRED`: six 2C.3 experiment families cover offline reconstruction,
field-state partitions, degradation sensitivity, leap/time boundaries, observer
partitions, and future domain endpoints. No degraded result is currently approved.

## Milestone 2C.4 refraction, horizon, and visibility proposal

`SOURCE_SUPPORTED_FACT`: SOFA `iauRefco` defines a compact refraction-coefficient
model using pressure, temperature, relative humidity, and wavelength; `iauAtioq`
consumes coefficients and contains a low-altitude numerical guard. Astropy `8.0.1`
`AltAz` uses nonzero pressure to request refraction, documents library defaults, and
documents inaccurate or unstable behavior in its low-altitude region. None defines
UFUQ terrain, photometric, daylight, transmission, screen, or learner visibility.

`PROJECT_DECISION`: propose geometric altitude only for the first vertical slice.
Optional refraction produces a separate immutable result from an explicit
provenance-bearing `AtmosphereObservation`; no default atmosphere is approved, and the
scene adapter applies no refraction. Keep geometric, refracted-apparent, physical-dip,
terrain/obstruction, renderer, and learner horizons distinct. Geometric horizon means
the astronomical local horizontal plane at geometric altitude zero; refracted apparent
horizon means only apparent altitude zero under a named model/policy. Keep astronomical
horizon, photometric/variability, Sun-altitude/daylight/twilight, atmospheric-
extinction/transparency, cloud/weather, terrain/obstruction, light-pollution, screen,
and learner-eligibility visibility components independent. No component promotes
another. Below-geometric-horizon is a non-terminal classification attached to the
valid geometric direction, not a scientific failure or visibility/rendering decision;
it retains coordinates, provenance, warnings, and statuses. Optional-stage failures
retain earlier valid states.

`AUTHORITY_OR_EVIDENCE_MISSING`: there is no approved refraction model/input or
altitude range, height/lapse policy, physical-dip/terrain profile, photometric/
daylight/extinction/transparency/cloud/weather/light-pollution rule, visibility
aggregation, warning allowlist, or learner eligibility. Astropy defaults and its
about-5-degree limitation cannot fill those gaps.

`HUMAN_REVIEW_REQUIRED`: AST-001/004/006/007 must approve or reject the first-slice,
model/domain, atmosphere provenance/uncertainty, near/below-horizon, physical-dip/
terrain, visibility, outcome, warning, and learner-facing policies.
`APPROVED_REFRACTED_RESULT` and `WARNING_BEARING_REFRACTED_RESULT` remain unreachable
until the exact model/version, complete meteorology/provenance, reviewed validity and
combined supported operating domains, warning policy/allowlist, scientific tolerance,
and named astronomy-review approval exist.

`EXPERIMENT_REQUIRED`: seven experiment families cover model comparison, meteorology
sensitivity, near-horizon numerics, geometric/apparent horizon, below-horizon behavior,
default-atmosphere consequences, and visibility separation with deterministic
provenance.

## Milestone 2C.5A experiment-protocol proposal

`PROJECT_DECISION`: freeze 24 stable experiment records before execution. Each record
separates current executability from what its result may establish and explicitly
records input class, model/library/routines/version, frames/times/units/conventions,
EOP/leap/meteorology/observer/ephemeris needs, partitions, comparison lineage, metrics,
repetitions, hashes, output schema, acceptance basis, reviewer gate, and follow-up
decision. The machine registry classifies 17 records as runnable with synthetic inputs
only, five as project-decision blocked, one as required-data blocked, and one as
deferred until production exists.

`SOURCE_SUPPORTED_FACT`: the pinned documentation establishes the exact library and
routine behaviour available for experiments. It does not change source or production
authority. Astropy high-level coordinates use ERFA, and PyERFA directly exposes ERFA;
their applicable results therefore share the ERFA/SOFA model lineage even though both
remain code-independent from future UFUQ TypeScript production code.

`EXPERIMENT_REQUIRED`: the proposed five-group 2C.5B batch covers epoch-label guards,
same-family route/convention consistency, motion/cosine/status guards, deterministic
replay, and optional-state/no-default/visibility separation. No body or result is added
by 2C.5A.

`HUMAN_REVIEW_REQUIRED`: AST-003/004/006/007 review is required before a result changes
production policy. Until AST-006 supplies a separate error-budget ledger and threshold,
numerical results remain `MEASURED_NO_ACCEPTANCE`; only exact supported invariants may
pass or fail. Synthetic execution cannot establish I/311 meaning, production approval,
supported domains, degraded modes, omission bounds, refraction/visibility policy, or a
tolerance.

## Milestone 2C.5B Batch 01 execution

`PROJECT_DECISION`: execute only the nine registered Batch 01 synthetic scopes through
a fixed allowlist. PyERFA `2.0.1.5` becomes a direct dependency of this reference tool
because the runner imports `erfa`; no package release changes. Nine fixtures and nine
results retain complete canonical/hash/runtime/source-prohibition evidence, every
handler runs twice in an offline fresh-cache context, and the complete command is
replayed in two independent OS processes in the same pre-synchronized locked
environment. This does not establish clean-environment dependency reconstruction.

The three epoch-label fixtures and every affected Astropy `Time` constructor use an
explicit synthetic ITRS-geocentre `[0,0,0] m` TT/TDB conversion reference location.
Each case also initializes the exact pinned smoke-only leap artifact used by that
conversion, including isolated single-ID execution. The schema rejects absence or a
nonzero replacement. This is controlled synthetic
provenance, not I/311 authority, a physical observer, or a production observer policy.
All results and hashes created before this correction were excluded; the final evidence
set is the complete runner-regenerated and replayed nine-result inventory.

`SOURCE_SUPPORTED_FACT`: raw `pmsafe` status `1` and the wrapper `ErfaWarning` are
preserved together. The componentized `apco13`/`atciq`/`atioq` branch and composed
`atco13` branch share ERFA/SOFA lineage, so agreement is same-family consistency only.

`EXPERIMENT_REQUIRED`: all 9/9 bounded Batch 01 experiments complete, yielding 24 passing exact checks with no
failures; six measurement-only checks cover 27 measurement records, all
`MEASURED_NO_ACCEPTANCE`. It exercises TT/TDB/UTC labels, calendar decimal year,
Besselian rejection, composed/decomposed routing, omitted/double-cosine mutations,
declared target epoch, JD splits, warning/status preservation, replay, below-horizon
non-erasure, no-default atmosphere, and visibility-component independence. Broader
effect/data/model/domain experiment partitions remain unrun or blocked.

`HUMAN_REVIEW_REQUIRED`: no measurement may become acceptance, source meaning,
production selection, omission bound, domain, refraction/visibility policy, degraded
mode, error budget, or tolerance without the existing AST-003/004/006/007 gates.

## Authority by topic

| Topic | Highest authority | Supporting source | UFUQ consequence |
|---|---|---|---|
| Executable IAU routine contract | Exact SOFA routine preamble/source for the pinned issue | IERS TN36 model chapters | Record version, routine, units, statuses, and transform direction. |
| Reference systems and Earth orientation | IERS TN36 Chapters 2 and 5 | SOFA `iauC2t06a`, `iauPnm06a`, `iauEra00` | Keep ICRS/GCRS/CIRS/TIRS/ITRS and realizations distinct. |
| Operational EOP fields/state | IERS Bulletin A/B metadata and official `finals2000A` format | Astropy `8.0.1` IERS reference-library docs | For every field, preserve source quality, provenance, coverage, availability, scientific approval, errors, and hashes as separate dimensions; do not substitute zero/nearest rows or promote fields. |
| Leap announcement and wire syntax | IERS Bulletin C; RFC 3339 | IANA release artifacts and Astropy `LeapSeconds` reference behaviour | Separate event authority, machine artifact, input syntax, and project validity/update policy. |
| UTC/TAI/TT/UT1 handling | SOFA time-routine contracts plus IERS TN36 §§5.5.3 and 10.1 | Explanatory textbook material | UTC is not silently substituted for UT1 or TT. |
| Original 1997 catalogue field semantics | ESA SP-1200 Volume 1 §§1.2 and 2.1 | I/311 `ReadMe` only for explicit cross-reference to I/239 | Use ESA definitions for original H-fields only; do not transfer them silently to I/311. |
| I/311 catalogue field semantics | I/311 `ReadMe` plus Appendix G Tables G.2–G.7 | ESA 1997 for original-catalogue comparison and van Leeuwen 2007 for quality context | Carry units, frame, epoch, solution type, quality, uncertainty, and supplement semantics per field. |
| Catalogue `yr` unit duration | CDS Catalogue Standard 2.0 Section 3.2.2 | SOFA `iauPmsafe` Julian-year rate contract | Convert I/311 numeric rates using 365.25 days per `yr`; keep the derivative/epoch scale separate. |
| Catalogue error behavior | I/311 row metadata plus van Leeuwen §§2-5 | None | Do not use one global Hipparcos accuracy constant. |
| General explanation | *Fundamental Astronomy*, Chapter 2 | Verified official overview of the Explanatory Supplement | Explanatory formulae cannot set a current model or tolerance. |
| Numerical expected results | Pinned independent oracle fixtures plus cross-checks | SOFA/IERS algorithms and catalogue metadata | No dossier result is itself a production acceptance tolerance. |

## Agreements

- Frame, equinox/origin, catalogue epoch, and observation time are different concepts.
- Precession-nutation arguments use TT, while Earth Rotation Angle uses UT1.
- A realized terrestrial/celestial transformation needs versioned Earth-orientation
  inputs; setting missing values to zero is an approximation requiring a bound.
- Catalogue astrometry is not apparent or observer-local position.
- Observer longitude sign, geodetic datum, height type, polar motion, refraction inputs,
  units, and azimuth convention must be explicit.
- Catalogue uncertainties and correlations are scientific inputs, not test or learner
  tolerances.
- Plausible visual orientation does not validate a transformation.

## Conflicts and ambiguities

| Issue | Sources | Status |
|---|---|---|
| Azimuth origin | *Fundamental Astronomy* §2.4 uses clockwise from south; SOFA `iauHd2ae` and UFUQ use north zero/east positive | Project/SOFA convention controls; textbook equations require explicit conversion. |
| Transform direction | IERS Eq. (5.1) presents ITRS to GCRS; SOFA `iauC2t06a` returns celestial to terrestrial | Test direction and inversion; do not copy matrix order by appearance. |
| CIO and equinox procedures | IERS TN36 documents both | Choose one coherent route; never mix ERA/CIO and incompatible sidereal/equinox quantities. |
| Hipparcos RA proper-motion component | I/311 Appendix G Table G.3, printed p. 407, labels the byte-52 value `mu_alpha_star`; Tables G.5–G.6, printed p. 408, use starred-alpha acceleration components | `CONFIRMED_FOR_I311`; normalize source `pmRA` to `properMotionRaCosDecMilliarcsecondsPerYear` and map it directly to Astropy `pm_ra_cosdec` after unit conversion. Keep omitted/double-cosine high-declination tests. |
| I/311 epoch representation and instant | I/311 gives only `Ep=1991.25`; ESA Gaia DR1 Section 4.2.1 directly identifies the I/311 new reduction and calls its parameter epoch `J1991.25`; ESA 1997 Section 1.2.6 gives the original catalogue `J1991.25(TT)` exactly | Julian representation is `SOURCE_SUPPORTED_FACT`. I/311-applicable time scale/exact instant is `AUTHORITY_OR_EVIDENCE_MISSING`; preserve the label and block source-derived propagation pending authority or `HUMAN_REVIEW_REQUIRED`. |
| Official baseline versus later material | TN36 is the official registered 2010 baseline; later corrected chapters/working versions are non-definitive and not officially approved as a registered edition, while separately linked supporting documentation is outside the official distribution and its review process | Pin and hash every selected later item separately; never edit the baseline in place or promote working/supporting material to official TN36. |
| Explanatory Supplement usability | Correct title/edition signals but no reliable text layer and conflicting extent | `SOURCE_UNUSABLE` for detailed current claims. |

## Candidate UFUQ rules

| Rule | Evidence | Classification |
|---|---|---|
| Every public/fixture value states frame, epoch/time scale, units, and convention. | SOFA routine contracts; IERS Chapters 2 and 5; ADR-003 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Catalogue rows remain immutable numerical source records; observed and refracted values are derived separately. | I/311 `ReadMe`; *Fundamental Astronomy* §§2.4, 2.9; `DATA_STRATEGY.md` | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Use TT for the selected precession-nutation model and UT1 for ERA, with pinned leap-second and EOP provenance. | IERS Eqs. (5.2), (5.14)-(5.15); SOFA time/ERA routines | `SOURCE_SUPPORTED_FACT` |
| Retain SOFA warning/error status, including dubious date and motion warnings. | `iauUtctai`, `iauAtco13`, `iauPmsafe` preambles | `SOURCE_SUPPORTED_FACT` |
| Propose a componentized SOFA `2023-10-11` CIO-family route and record every included/omitted/conditional/blocked effect while keeping Astropy as the independent reference path. | SOFA `iauPmsafe`/`iauAtco13`/`iauApco13`/`iauAtciq`/`iauAtioq`; IERS Chapter 5; AST-003 | `PROJECT_DECISION`; approval and implementation mapping remain `HUMAN_REVIEW_REQUIRED` |
| Preserve raw I/311 `pmRA` and expose it only as the explicitly named `mu_alpha_star` normalized component; do not apply or remove another cosine factor when supplying Astropy `pm_ra_cosdec`; convert `yr` using 365.25 days. | I/311 Appendix G Table G.3, printed p. 407; Tables G.5–G.6, printed p. 408; CDS Catalogue Standard 2.0 Section 3.2.2 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Test RA proper-motion normalization with high-declination, epoch-1991.25, omitted-cosine, and double-cosine cases against the pinned independent oracle. | ESA 1997 §1.5.4 Eq. (1.5.21) p. 94; ADR-007 | `EXPERIMENT_REQUIRED` |
| Compare explicit Julian-TT/TDB/UTC, calendar-decimal-year, and Besselian guard interpretations with synthetic space-motion inputs; record time and direction deltas without inferring source meaning. | I/311/ESA epoch evidence conflict; Astropy `8.0.1` time docs; PyERFA `pmsafe` TDB contract | `EXPERIMENT_REQUIRED` |
| Use geometric-only first-slice output, no default atmosphere, separate optional refraction states, six typed horizon meanings, and nine independent visibility components. | SOFA `iauRefco`/`iauAtioq`/`iauHd2ae`; Astropy `8.0.1` `AltAz`; AST-004 | `PROJECT_DECISION`; model/range/physical-dip/terrain/visibility/warning/tolerance approval remains required |
| Derive acceptance thresholds from measured independent disagreement and an error budget; never copy model accuracy prose. | SOFA accuracy notes; van Leeuwen limitations; ADR-007/AST-006 | `EXPERIMENT_REQUIRED` |
| The Python/Astropy oracle remains pinned and imports no production UFUQ package. | ADR-007 and scientific-testing synthesis | `PROJECT_DECISION` |
| Register every scientific experiment before execution, disclose shared algorithm lineage, and keep synthetic executability separate from authority/approval. | ADR-007; testing-scientific-software dossier; 2C.5A protocol | `PROJECT_DECISION`; numerical acceptance remains `HUMAN_REVIEW_REQUIRED` under AST-006 |
| Run scientific requests offline from an immutable hash-addressed EOP/leap bundle; update separately and retain old bundles for replay. | IERS product/status evidence; Astropy fallback surfaces; reproducibility contract | `PROJECT_DECISION`; product selection, cadence, and activation approval remain `HUMAN_REVIEW_REQUIRED` |
| Reject missing/stale/out-of-range data and any field quality without explicit scientific approval; reserve degraded output until a named mode, quantitative bound, warning contract, and reviewer approval exist. | IERS field flags/product roles; Astropy warning/degraded surfaces; AST-003/006 | `PROJECT_DECISION`; degradation sensitivity is `EXPERIMENT_REQUIRED` |

## Required validation evidence

- Exact catalogue release/file hashes and selected field/quality semantics. I/311
  `pmRA` and the Julian epoch representation are resolved; the epoch time-scale
  mapping, derivative time scale, and radial-velocity policy for propagation remain
  open. The CDS-defined 365.25-day rate unit is resolved.
- A versioned manifest naming SOFA/IERS models, Astropy/PyERFA/IERS-data, leap-second
  and EOP data, network/offline state, observer datum/height, refraction, and supported
  range.
- Neutral fixtures containing all inputs and expected outputs with units/conventions.
- Cases for epoch identity/motion, nonzero EOP, alternative Julian-date splits, UTC
  boundaries, meridian/east/west, wrap, horizon, zenith/nadir, invalid inputs, and
  high-declination omitted/double-cosine proper-motion cases.
- Great-circle and wrapped-angle residuals, component/status differences, and a
  per-case error budget.
- An import/code-sharing audit proving oracle independence.

## Unresolved gaps

The pinned synthetic-only oracle environment exists, including exact Astropy, PyERFA,
IERS-data, and packaged IERS file hashes. Astropy reference-design documentation and the
PyERFA release/hash are pinned; PyERFA's official stable docs remain one patch behind.
Milestone 2C.2 supplies a proposed production semantic route and effect matrix.
Milestone 2C.3 supplies proposed observer/time boundaries, immutable offline data and
update semantics, orthogonal field-state handling, domain composition, deterministic
outcome precedence, structured outcomes, and reference evidence. Milestone 2C.4
supplies a geometric-only/no-default proposal, explicit atmosphere/refraction state,
separate horizon and visibility components, optional-stage precedence, and reference
experiment requirements. Milestone 2C.5A supplies a human/machine experiment registry,
fixture/result schemas, execution/claim separation, and shared-lineage disclosure.
Milestone 2C.5B executes only its bounded synthetic first batch; this adds guard and
determinism evidence, not independent scientific or production validation. The actual
implementation/library and approvals remain open, together with production EOP/leap artifacts and hashes,
stale/update and prediction/
preliminary policy, refraction, date/location/height endpoints, epoch/derivative scale,
radial velocity, source-derived comparison cases, omission bounds, error budget, and
numerical tolerances. No degraded mode is approved. The I/311 `pmRA` component and
numeric 365.25-day rate-unit semantics are no longer open items.
