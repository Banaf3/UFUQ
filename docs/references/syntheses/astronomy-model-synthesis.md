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
5. CDS *Standards for Astronomical Catalogues* Version 2.0 for the VizieR `yr` unit;
6. *Fundamental Astronomy* as explanatory support; and
7. the *Explanatory Supplement* only as an unresolved explanatory source because the
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

## Authority by topic

| Topic | Highest authority | Supporting source | UFUQ consequence |
|---|---|---|---|
| Executable IAU routine contract | Exact SOFA routine preamble/source for the pinned issue | IERS TN36 model chapters | Record version, routine, units, statuses, and transform direction. |
| Reference systems and Earth orientation | IERS TN36 Chapters 2 and 5 | SOFA `iauC2t06a`, `iauPnm06a`, `iauEra00` | Keep ICRS/GCRS/CIRS/TIRS/ITRS and realizations distinct. |
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
| Choose geometric/refraction and horizon/visibility behavior explicitly. | SOFA `iauRefco`/`iauAtioq`; AST-004 | `PROJECT_DECISION_REQUIRED` |
| Derive acceptance thresholds from measured independent disagreement and an error budget; never copy model accuracy prose. | SOFA accuracy notes; van Leeuwen limitations; ADR-007/AST-006 | `EXPERIMENT_REQUIRED` |
| The Python/Astropy oracle remains pinned and imports no production UFUQ package. | ADR-007 and scientific-testing synthesis | `PROJECT_DECISION` |

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
Milestone 2C.2 now supplies a proposed production semantic route and effect matrix, but
the actual implementation/library and approvals remain open, together with production
offline/network EOP/correction policy, refraction policy, supported range, leap-second
policy, epoch/derivative scale, radial velocity, source-derived comparison cases,
omission bounds, error budget, and numerical tolerances. The I/311 `pmRA` component and
numeric 365.25-day rate-unit semantics are no longer open items.
