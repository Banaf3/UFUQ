# Bibliographic identity

- Canonical source ID: `IERS-TN36-2010`.
- Title: *IERS Conventions (2010)*.
- Editors: Gérard Petit and Brian Luzum.
- Edition/version: official IERS Technical Note No. 36, registered 2010 baseline
  (`v1.0.0` in the Conventions Centre archive).
- Year: 2010.
- Publisher: Verlag des Bundesamts für Kartographie und Geodäsie, Frankfurt am Main.
- Identifier: IERS Technical Note 36; ISSN 1019-4568.
- Local file: `local-reference/standards/iers/2010/iers-conventions-2010-tn36.pdf`.
- Page count and accessibility: local PDF metadata reports 180 PDF pages and a
  searchable text layer. The official Conventions Centre rendering currently reports
  179 PDF pages; printed page numbering runs through the glossary. Source locations
  below use printed chapter/page numbers, not local PDF page indices.
- Verification status: title, editors, publisher, year, ISSN, and official-baseline
  status were checked against the title/copyright matter and the IERS Conventions
  Centre. The Centre labels later corrected chapters as a non-registered working
  version; they are not silently merged here.

# UFUQ relevance

- Phases affected: Phase 1 astronomy/data spike; Phase 2 validated observer/time
  transformations; later fixture replay and release evidence.
- Project decisions affected: AST-003, AST-004 insofar as “observed” coordinates need
  an Earth/observer definition, AST-006, ADR-003, and ADR-007.
- Studied sections:
  - Introduction, printed pp. 6-14, especially model status and revision policy;
  - Chapter 1, numerical standards, printed pp. 15-20;
  - Chapter 2, §§2.1-2.2, printed pp. 21-25;
  - Chapter 4, concepts/terminology for terrestrial systems, §§4.1-4.2, printed
    pp. 31-40;
  - Chapter 5, §§5.1-5.6 and §5.9, printed pp. 43-71, with detailed extraction from
    §§5.3-5.5, including subdaily EOP restoration in §§5.5.1 and 5.5.3;
  - Chapter 8, §8.2, printed pp. 123-124, for the ocean-tide EOP correction family;
  - Chapter 10, time-coordinate relationships in §10.1, printed pp. 151-153;
  - Glossary entries for ERA, epoch, GCRS, TT, TIRS, UT1, and UT1-UTC, printed
    pp. 174-178.
- Intentionally not studied for the current phase: geopotential beyond the named EOP
  restoration dependencies, station displacement, antenna modelling, tidal series
  outside §§5.5.1/5.5.3 and §8.2, satellite equations of motion, and VLBI propagation
  details. They are not part of the current catalogue-star horizon claim.
- Scope reason: Chapters 2, 4, 5, and the relevant time definitions establish the
  reference-system and Earth-orientation vocabulary beneath any rigorous topocentric
  transformation.

# Terminology

- **Reference system** is the theoretical coordinate-system definition; a **reference
  frame** is its material/observational realization. Chapter 5 warns that numerical
  implementation uses the adopted ITRF and ICRF realizations.
- **ICRS** is the conventional celestial reference system; **ICRF** is its realization
  using compact extragalactic radio-source coordinates (Chapter 2, §2.2, printed
  p. 22).
- **GCRS** is the relativistic geocentric celestial reference system, oriented by
  default according to ICRS axes (Chapter 5, §5.3.1, printed p. 45).
- **ITRS** is the conventional terrestrial reference system; **ITRF** is a realization.
- **CIP** separates celestial pole motion into precession-nutation and terrestrial pole
  motion by convention (Chapter 5, §§5.3.2-5.3.3, printed pp. 45-46).
- **CIRS** and **TIRS** are the celestial and terrestrial intermediate systems using
  the CIP and the CIO/TIO (Chapter 5, §5.4, printed pp. 46-47).
- **ERA** is the angle on the CIP equator between CIO and TIO; UT1 is conventionally
  related linearly to it (Chapter 5, §§5.2.1 and 5.5.3).
- **Epoch** is a fixed date used to reckon time-varying quantities; the glossary warns
  that “date of observation” is clearer for an observation instant (printed p. 175).
- **TT** is a geocentric coordinate time related linearly to TCG and realized accurately
  by `TAI + 32.184 s` (Chapter 10, §10.1, printed p. 151; glossary p. 178).
- **UT1** is the Earth-rotation parameter obtained from observation; `UT1-UTC` is an
  IERS-provided quantity (glossary, printed p. 178).

# Concepts and models

## Systems, frames, and catalogue coordinates

Chapter 2 separates the ICRS from successive realizations of its axes. Section 2.2
states that ICRF source positions are independent of equator, equinox, ecliptic, and
epoch, while being aligned to earlier realizations within their uncertainty. A
catalogue epoch therefore remains necessary for a moving star even when the frame
orientation is ICRS.

The 2010 text discusses the Hipparcos catalogue as the optical realization available at
the time (Chapter 2, §2.2.1). That historical role does not make every Hipparcos
astrometric row epoch-free or apparent-of-date.

## Celestial/terrestrial transformation

Chapter 5 decomposes ITRS-to-GCRS into polar motion, Earth rotation, and celestial pole
motion. It describes equivalent CIO-based and equinox-based procedures but emphasizes
the CIO route required by the IAU non-rotating-origin resolution. Mixing ERA/CIO
quantities with an incompatible equinox/sidereal-time path is therefore a convention
error, even if the output looks plausible.

## Precession and nutation

Section 5.3.3 requires the IAU 2006 precession plus IAU 2000A or 2000B nutation
according to needed precision, together with observed celestial pole offsets where the
realized CIP is required. The model alone and the observed EOP corrections are distinct
inputs.

## Earth rotation and EOP

Section 5.5.3 defines ERA from UT1 and says that the IERS `UT1-UTC` value is used when
it is not estimated from observations. Chapter 2 §2.2.2 describes EOP as the ongoing
tie between ICRF and ITRF through polar coordinates/celestial pole offsets and
`UT1-UTC`. A pinned model without pinned EOP inputs is not a reproducible realized
transformation.

Sections 5.5.1 and 5.5.3 state that the subdaily terms omitted from reported daily EOP
are added after interpolation. For `xp`,`yp`, Eq. (5.11) and §5.5.1.1 require the
Chapter 8 ocean-tide corrections plus the diurnal polar-motion libration terms of
Table 5.1a; long-period and secular libration are already in observed polar motion and
must not be added again. For UT1, §5.5.3.1 requires Chapter 8 ocean-tide corrections
plus the semidiurnal UT1 libration terms of Table 5.1b. Chapter 8 identifies the
`ORTHO_EOP`/`CNMTX` family; Chapter 5 identifies `PMSDNUT2` and `UTLIBR`. These are the
registered 2010 baseline families, distinct from Gazette 13's older 1996 `RAY` example
and from later non-registered working corrections.

## Time

Chapter 5 §5.3.1 fixes J2000.0 at JD 2451545.0 TT and uses TT Julian centuries for
precession/nutation quantities. ERA uses UT1. Chapter 10 §10.1 separates TT, TCG, TDB,
TCB, and proper time; the glossary separates uniform UTC from observed UT1.

# Equations and algorithms

| Item | Source location | Variables, units, assumptions, and domain | UFUQ use and validation |
|---|---|---|---|
| ITRS-to-GCRS decomposition | Chapter 5, §5.1, Eq. (5.1), printed p. 43 | `[GCRS] = Q(t) R(t) W(t) [ITRS]`; `W` is polar motion, `R` Earth rotation, `Q` celestial pole motion. It is a system-level formulation whose realization uses ITRF/ICRF. | Authority for conceptual factorization. Test transform direction/order against the chosen executable routine and nonzero EOP fixtures. |
| TT Julian-century argument | Chapter 5, §5.3.1, Eq. (5.2), printed p. 45 | `t` is TT days from 2000-01-01 12h TT divided by 36525; J2000.0 is JD 2451545.0 TT. | Retain scale and epoch in every PN computation; never derive this argument from unlabeled UTC. |
| Polar-motion matrix | Chapter 5, §5.4.1, Eq. (5.3), printed p. 48 | `W(t)=R3(-s') R2(xp) R1(yp)`; `xp`,`yp` are CIP coordinates in ITRS and `s'` is the TIO locator. Rotation sign/order follows the chapter's ITRS-to-GCRS convention. | Cross-check inverse/direction against SOFA's celestial-to-terrestrial matrix. |
| CIO Earth-rotation matrix | Chapter 5, §5.4.2, Eq. (5.5), printed p. 48 | `R(t)=R3(-ERA)` for TIRS-to-CIRS in the chapter's direction. | Prevent mixing ERA with an equinox-origin path. |
| ERA from UT1 | Chapter 5, §5.5.3, Eqs. (5.14)-(5.15), printed p. 52 | `ERA = 2pi(0.7790572732640 + 1.00273781191135448 Tu)` modulo `2pi`, where `Tu = JD(UT1)-2451545.0`; Eq. (5.15) rearranges day fractions to reduce rounding error. | Exact model reference; compare multiple two-part-JD layouts and retain the matching IERS `UT1-UTC`. |
| Subdaily EOP restoration | Chapter 5, §§5.5.1.1-5.5.1.3 and §§5.5.3.1-5.5.3.3, printed pp. 49-53; Chapter 8, §8.2, printed pp. 123-124 | Interpolate reported daily values first; then add ocean-tide terms to `xp`,`yp`,UT1, diurnal libration to `xp`,`yp`, and semidiurnal libration to UT1. Do not re-add long-period/secular polar-motion libration already present in observations. | Pin exact baseline routine/coefficient/dependency bytes and product regularization in 2D; implement once in 2E; pass only restored instantaneous fields to astronomy-core. |
| TT/TCG relationship | Chapter 10, §10.1, Eq. (10.1), printed p. 151 | TT differs from TCG by a fixed rate using defining constant `LG`; the chapter also states `TT = TAI + 32.184 s` as a realization relationship. | Keep scale conversions explicit; do not use TT and UTC interchangeably. |

# Conventions

- SI metre, kilogram, and second are the base units; a day is 86400 SI seconds and a
  Julian century is 36525 days (Introduction, printed p. 6).
- J2000.0 is JD 2451545.0 TT (Chapter 5, §5.3.1, Eq. 5.2).
- Precession/nutation arguments use TT; Earth rotation uses UT1.
- `UT1 = UTC + (UT1-UTC)` for the ERA computation (Chapter 5, §5.5.3).
- `xp`,`yp` are pole coordinates, not geographic longitude/latitude.
- CIO-based and equinox-based paths have different origins and parameterizations; a
  valid pipeline must remain internally consistent.
- ITRS/GCRS matrix signs depend on transform direction. SOFA's `iauC2t06a` documents
  the inverse celestial-to-terrestrial direction; formulae must not be copied without
  checking the vector sense.
- ITRS/ITRF does not by itself define a user's latitude/longitude datum, coordinate
  source, or height type. Those observer semantics remain explicit project inputs.

# Implementation implications

- `SOURCE_REQUIRED`: label ICRS, GCRS, CIRS, TIRS, ITRS, and their realizations
  distinctly; do not use “J2000” as a combined frame, equinox, epoch, and time scale.
- `SOURCE_REQUIRED`: use TT for precession-nutation arguments and UT1 for ERA; preserve
  the IERS data/version used to obtain `UT1-UTC` and pole coordinates.
- `PROJECT_DECISION_RESOLVED_FOR_PROFILE_V1`: use the selected coherent CIO-based,
  model-CIP-only route. Any later equinox route or observed-CPO extension requires a
  separate decision; the selected routine family and omissions remain recorded.
- `SOURCE_REQUIRED`: treat model CIP coordinates and observed celestial-pole offsets as
  distinct where the approved accuracy scope requires realized Earth orientation.
- `PROJECT_DECISION_RESOLVED_FOR_PROFILE_V1`: the generic `ObserverPreset`, final-only
  polar-motion, and supported-domain semantics are fixed. Exact observer data and the
  activated date interval remain 2D/2E data rather than open 2C semantics.
- `EXPERIMENT_REQUIRED`: quantify the result of omitting or approximating `xp`,`yp`,
  celestial-pole offsets, or EOP terms over UFUQ's approved scenarios.
- `SOURCE_REQUIRED`: keep official TN36 `v1.0.0` and later IERS corrections/working
  material as separate versioned inputs.
- `SOURCE_REQUIRED`: apply the Chapter 5/8 subdaily restoration exactly once after
  interpolation. Do not substitute Gazette 13's historical `RAY` routine for the
  complete 2010 baseline or silently merge later working corrections.
- `EXPERIMENT_REQUIRED`: derive UFUQ tolerances from independent outputs and an error
  budget. TN36 model figures are not learner or implementation thresholds.
- `INFORMATIONAL_ONLY`: Chapters on station displacement, tides, and relativistic
  ranging show the wider IERS scope but do not automatically enter the UFUQ MVP.

# Testing implications

- Fixture metadata must include input/output frame and realization, TT and UT1 values,
  UTC source instant, leap-second source, `UT1-UTC`, `xp`,`yp`, celestial-pole-offset
  policy, IERS table version/hash, and transform direction.
- Reference cases must include nonzero EOP inputs so a pipeline that silently sets them
  to zero cannot pass through shared defaults.
- Compare CIO-based reference results against the same CIO-based convention; if an
  equinox path is also tested, compare only after the equation-of-origins relationship
  is handled.
- Test Eq. (5.14)/(5.15) equivalence with numerically stable two-part JDs at day
  boundaries and across the supported range.
- Test inverse matrices/vectors explicitly because TN36 Eq. (5.1) and SOFA
  `iauC2t06a` document opposite transform directions.
- Malformed-input tests must reject unlabeled time scales, frame/epoch conflation,
  unavailable/out-of-coverage/unapproved EOP, invalid latitude, and unlabelled height.
- Real-data activation stops if the exact IERS-data pin, approved offline bundle,
  leap-second artifact, or derived supported interval is absent. Approximation bounds
  remain a postimplementation scientific-acceptance gate, not an implementation-entry
  prerequisite.

# Limitations

- TN36 defines IERS systems, models, and procedures; it does not choose UFUQ's
  catalogue, observer, atmospheric refraction, horizon, or tolerance.
- TN36's 2010 discussion of ICRF realizations is a historical baseline. A modern
  external frame realization or EOP product must be separately pinned if selected.
- The subdaily EOP components required by the selected V1 input contract were studied
  only to identify the governing 2010 families and ordering. Exact coefficient/source
  bytes, dependencies, product regularization, later corrections, and numerical
  uncertainty remain 2D/2E/postimplementation work. Other station-displacement and
  tidal models remain outside the claim.
- The document does not make WGS84 and ITRS interchangeable labels for arbitrary
  coordinates or heights.
- The official baseline does not silently include later errata or working-version
  changes.

# Conflicts and ambiguities

- Local PDF metadata reports 180 pages while the current official web PDF reports 179.
  This dossier cites printed chapter/page numbers and does not infer a missing or added
  scientific page from that one-page packaging difference.
- TN36 writes the terrestrial-to-celestial direction in Eq. (5.1); SOFA
  `iauC2t06a` returns celestial-to-terrestrial. Their matrix sequences are compatible
  only after direction/inversion is handled.
- TN36 provides both CIO- and equinox-based procedures. This is not permission to mix
  ERA/CIO and GAST/equinox quantities within one path.
- The IERS Conventions Centre working version contains identified corrections but says
  it is not the official registered edition. UFUQ must pin any correction explicitly
  rather than editing the TN36 baseline in place.
- The numerical contribution and implementation residual of the required subdaily EOP
  restoration remain `POST_IMPLEMENTATION_VALIDATION`; the exactly-once restoration
  semantics are no longer an open implementation-contract question.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Official baseline and model purpose | Introduction, printed pp. 6-14; Conventions Centre `v1.0.0` notice | Pin TN36 separately from updates | `SOURCE_REQUIRED` |
| ICRS versus ICRF | Chapter 2, §§2.1-2.2, printed pp. 21-25 | Frame identity does not erase star epoch/motion | `SOURCE_REQUIRED` |
| ITRS/GCRS factorization | Chapter 5, §5.1, Eq. (5.1), printed p. 43 | Trace PN, Earth rotation, and polar motion separately | `SOURCE_REQUIRED` |
| GCRS is ICRS-oriented by default | Chapter 5, §5.3.1, printed p. 45 | Label intermediate frames and axis orientation | `SOURCE_REQUIRED` |
| J2000.0 and PN time argument | Chapter 5, §5.3.1, Eq. (5.2), printed p. 45 | Carry TT and catalogue epoch separately | `SOURCE_REQUIRED` |
| CIP realization includes model plus observations | Chapter 5, §5.3.3, printed pp. 46-47 | V1 selects model CIP and explicitly omits observed `dX`,`dY`; a later observed-CPO profile needs its own data policy | `PROJECT_DECISION_RESOLVED_FOR_PROFILE_V1` |
| CIO/equinox paths are distinct | Chapter 5, §§5.3.4-5.4, printed pp. 47-48 | V1 selects one coherent CIO route; later alternatives require separate review | `PROJECT_DECISION_RESOLVED_FOR_PROFILE_V1` |
| ERA is defined from UT1 | Chapter 5, §5.5.3, Eqs. (5.14)-(5.15), printed p. 52 | Pin `UT1-UTC`; do not substitute UTC | `SOURCE_REQUIRED` |
| Restore omitted subdaily EOP after interpolation | Chapter 5, §§5.5.1/5.5.3, printed pp. 49-53; Chapter 8, §8.2, printed pp. 123-124 | Add the 2010 ocean-tide and applicable libration families once; 2D pins exact configuration and 2E implements it | `SOURCE_REQUIRED` plus `2D_DATA_SELECTION`/`2E_IMPLEMENTATION_CONFIGURATION` |
| EOP ties celestial and terrestrial frames | Chapter 2, §2.2.2, printed p. 25 | Version/hash EOP data in every fixture | `SOURCE_REQUIRED` |
| TT is distinct from TAI/TCG/UTC | Chapter 10, §10.1, printed pp. 151-153; glossary p. 178 | Use named time-scale conversions | `SOURCE_REQUIRED` |
| Numerical restoration and other omission bounds remain unknown | Named subdaily terms plus unstudied station/other tidal terms; `SOURCE_GAPS.md` AST-SRC-004/006/007 | Do not infer zero uncertainty from selecting a model family | `POST_IMPLEMENTATION_VALIDATION` / `EXPERIMENT_REQUIRED` |
