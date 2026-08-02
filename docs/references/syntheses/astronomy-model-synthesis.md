# Astronomy model synthesis

## Scope and authority

This synthesis compares the current-phase astronomy sources:

1. exact routines and contracts in IAU SOFA issue `2023-10-11`;
2. the official IERS Conventions (2010) TN36 baseline, with later updates kept separate;
3. the official ESA 1997 guide for original-catalogue semantics;
4. official Hipparcos I/311 metadata, Appendix G field tables, and van Leeuwen's
   validation study;
5. *Fundamental Astronomy* as explanatory support; and
6. the *Explanatory Supplement* only as an unresolved explanatory source because the
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

## Authority by topic

| Topic | Highest authority | Supporting source | UFUQ consequence |
|---|---|---|---|
| Executable IAU routine contract | Exact SOFA routine preamble/source for the pinned issue | IERS TN36 model chapters | Record version, routine, units, statuses, and transform direction. |
| Reference systems and Earth orientation | IERS TN36 Chapters 2 and 5 | SOFA `iauC2t06a`, `iauPnm06a`, `iauEra00` | Keep ICRS/GCRS/CIRS/TIRS/ITRS and realizations distinct. |
| UTC/TAI/TT/UT1 handling | SOFA time-routine contracts plus IERS TN36 §§5.5.3 and 10.1 | Explanatory textbook material | UTC is not silently substituted for UT1 or TT. |
| Original 1997 catalogue field semantics | ESA SP-1200 Volume 1 §§1.2 and 2.1 | I/311 `ReadMe` only for explicit cross-reference to I/239 | Use ESA definitions for original H-fields only; do not transfer them silently to I/311. |
| I/311 catalogue field semantics | I/311 `ReadMe` plus Appendix G Tables G.2–G.7 | ESA 1997 for original-catalogue comparison and van Leeuwen 2007 for quality context | Carry units, frame, epoch, solution type, quality, uncertainty, and supplement semantics per field. |
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
| I/311 epoch instant | ESA 1997 §1.2.6 Eq. (1.2.3) gives original `J1991.25(TT)` exactly; I/311 gives only `Ep=1991.25` | `PROJECT_DECISION_REQUIRED`; the original statement is strong support but is not silently transferred to the new reduction. |
| Official baseline versus corrections | TN36 is the registered 2010 baseline; working corrections are separate | Pin and hash corrections separately; never edit the baseline in place. |
| Explanatory Supplement usability | Correct title/edition signals but no reliable text layer and conflicting extent | `SOURCE_UNUSABLE` for detailed current claims. |

## Candidate UFUQ rules

| Rule | Evidence | Classification |
|---|---|---|
| Every public/fixture value states frame, epoch/time scale, units, and convention. | SOFA routine contracts; IERS Chapters 2 and 5; ADR-003 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Catalogue rows remain immutable numerical source records; observed and refracted values are derived separately. | I/311 `ReadMe`; *Fundamental Astronomy* §§2.4, 2.9; `DATA_STRATEGY.md` | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Use TT for the selected precession-nutation model and UT1 for ERA, with pinned leap-second and EOP provenance. | IERS Eqs. (5.2), (5.14)-(5.15); SOFA time/ERA routines | `SOURCE_SUPPORTED_FACT` |
| Retain SOFA warning/error status, including dubious date and motion warnings. | `iauUtctai`, `iauAtco13`, `iauPmsafe` preambles | `SOURCE_SUPPORTED_FACT` |
| Select one named catalogue-to-observed pipeline and record every included/omitted effect. | SOFA `iauApco13`/`iauAtco13`; IERS Chapter 5; AST-003 | `PROJECT_DECISION_REQUIRED` |
| Preserve raw I/311 `pmRA` and expose it only as the explicitly named `mu_alpha_star` normalized component; do not apply or remove another cosine factor when supplying Astropy `pm_ra_cosdec`. | I/311 Appendix G Table G.3, printed p. 407; Tables G.5–G.6, printed p. 408 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Test RA proper-motion normalization with high-declination, epoch-1991.25, omitted-cosine, and double-cosine cases against the pinned independent oracle. | ESA 1997 §1.5.4 Eq. (1.5.21) p. 94; ADR-007 | `EXPERIMENT_REQUIRED` |
| Choose geometric/refraction and horizon/visibility behavior explicitly. | SOFA `iauRefco`/`iauAtioq`; AST-004 | `PROJECT_DECISION_REQUIRED` |
| Derive acceptance thresholds from measured independent disagreement and an error budget; never copy model accuracy prose. | SOFA accuracy notes; van Leeuwen limitations; ADR-007/AST-006 | `EXPERIMENT_REQUIRED` |
| The Python/Astropy oracle remains pinned and imports no production UFUQ package. | ADR-007 and scientific-testing synthesis | `PROJECT_DECISION` |

## Required validation evidence

- Exact catalogue release/file hashes and selected field/quality semantics. I/311
  `pmRA` is resolved; the epoch time-scale mapping for propagation remains open.
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
IERS-data, and packaged IERS file hashes. The exact official Astropy/PyERFA
documentation pins, production algorithm, production offline/network EOP policy,
refraction policy, supported range, leap-second policy, epoch time-scale mapping,
source-derived comparison cases, and numerical tolerances remain open. I/311 `pmRA`
semantics are no longer an open item.
