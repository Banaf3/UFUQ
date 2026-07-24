# Bibliographic identity

- Canonical source ID: `FUND-ASTRO-6E`.
- Title: *Fundamental Astronomy*.
- Editors/authors: Hannu Karttunen, Pekka Kröger, Heikki Oja, Markku Poutanen, and Karl
  Johan Donner.
- Edition/version: sixth edition.
- Year: 2017 (Springer copyright); the eBook was first published in November 2016.
- Publisher: Springer-Verlag Berlin Heidelberg.
- DOI/ISBN: `10.1007/978-3-662-53045-0`; print ISBN `978-3-662-53044-3`;
  eBook ISBN `978-3-662-53045-0`.
- Local file: `local-reference/astronomy/foundations/fundamental-astronomy-6e.pdf`.
- Page count and accessibility: local PDF metadata reports 548 PDF pages and a
  searchable text layer. Springer describes the work as `XIV, 550` pages; the
  pagination/package difference is recorded below rather than silently reconciled.
- Verification status: title, editors, edition, identifiers, publisher, and chapter
  range were checked against the Springer record. Local acquisition provenance remains
  `PROVENANCE_UNVERIFIED`.

# UFUQ relevance

- Phases affected: explanatory support for the Phase 1 astronomy spike; vocabulary and
  learner-facing explanation review in Phase 2; not a production algorithm authority.
- Project decisions affected: AST-003 and AST-004 terminology; AST-006 only as a list
  of effects that require a measured error budget.
- Chapters studied:
  - Chapter 2, *Spherical Astronomy*, printed pp. 11-49;
  - specifically §§2.3-2.5 (celestial sphere, horizontal and equatorial systems),
    §2.9 (perturbations), §2.10 (positional astronomy), §2.12 (catalogues), §2.13
    (sidereal/solar time), §2.14 (astronomical time systems), and §2.15 (calendars).
- Chapters intentionally not studied: astrophysics, celestial mechanics, instruments,
  solar-system bodies, stellar/galactic topics, cosmology, and astrobiology. They do not
  govern the current catalogue-star-to-horizon validation claim.
- Scope reason: Chapter 2 is a compact explanatory account of coordinates, apparent
  place, catalogue position, time, and observation effects. SOFA, IERS, catalogue
  metadata, and independent fixtures remain higher authorities.

# Terminology

- **Horizontal system**: a local system using altitude (or elevation) and azimuth;
  zenith distance complements altitude (§2.4).
- **Equatorial system**: right ascension/declination and local hour angle are tied to the
  celestial equator/pole and local meridian (§2.5).
- **Mean place**: a catalogue-style position with specified apparent effects removed;
  the mean place of date also accounts for proper motion and precession (§2.9).
- **Apparent place**: the mean place of date after further apparent-position
  corrections such as nutation, parallax, and aberration (§2.9).
- **Proper motion**: the time-dependent motion of a star's catalogue direction
  (§§2.9-2.10).
- **Sidereal time** and **solar time**: rotation-related time measures that run at
  different rates (§2.13).
- **Astronomical time systems**: the chapter distinguishes Earth-rotation time,
  atomic/SI time, and dynamical/coordinate-like time concepts (§2.14).

# Concepts and models

## Local horizon versus catalogue coordinates

Section 2.4 explains that altitude/azimuth is observer-local and changes as the sky
rotates. Section 2.5 introduces equatorial coordinates and hour angle as the bridge to
the observer's meridian. These are explanatory relationships; the chapter does not
replace the SOFA/IERS apparent-place and Earth-orientation chain.

The book explicitly warns in §2.4 that azimuth origins and directions differ by
discipline. It adopts a conventional astronomical azimuth measured clockwise from the
south. UFUQ instead fixes north `0`, east `90` in ADR-003 and the selected SOFA horizon
routines. The book's equation signs must therefore not be copied without conversion.

## Catalogue, mean, and apparent place

Section 2.9 separates catalogue mean places from mean place of date and apparent place.
It notes that diurnal aberration and refraction depend on the observer and are not part
of a generic catalogue apparent-place tabulation. For UFUQ, this supports typed
separation between catalogue astrometry, propagated coordinates, apparent/topocentric
coordinates, and the final horizontal result.

## Perturbing effects

Section 2.9 discusses parallax, aberration, precession, nutation, and refraction as
different effects with different physical causes and dependencies. It is useful for
ensuring the pipeline inventory is complete, but it does not select the current IAU
model, implementation routine, data source, or omission bound.

## Time

Sections 2.13-2.15 distinguish local/Greenwich sidereal and solar concepts, UT-like
Earth-rotation time, atomic time, dynamical/coordinate time, Julian dates, and calendar
conversion. The worked formulae are pedagogical and cannot override current SOFA/IERS
algorithms or leap-second/EOP data.

# Equations and algorithms

| Item | Source location | Variables, units, assumptions, and domain | UFUQ use and validation |
|---|---|---|---|
| Altitude/zenith-distance complement | Chapter 2, §2.4, Eq. (2.10) | `z = 90 deg - a`; `a` is altitude and `z` zenith distance. Chapter 2 generally uses degrees. | Unit/convention sanity check only; production uses explicit radians internally and named degree fields at boundaries. |
| Horizontal/equatorial spherical triangle | Chapter 2, §§2.4-2.6 | Relates latitude, declination, hour angle, altitude, and azimuth under the book's south-origin azimuth convention and simplified spherical observer model. | Do not copy signs directly. Compare the selected north-origin ENU implementation against SOFA/Astropy reference vectors. |
| Mean-to-apparent conceptual sequence | Chapter 2, §2.9 | Catalogue mean place -> proper-motion/precession mean place of date -> nutation/parallax/aberration apparent place; observer-dependent diurnal/refraction effects remain separate. | Use as a pipeline completeness checklist; exact models and order are controlled by SOFA/IERS and the approved spike decision. |
| Sidereal/solar worked computations | Chapter 2, §2.13 and Examples in §2.16 | Pedagogical degree/hour/day formulae and examples, with explicitly approximate examples in places. | Explanatory tests only. They are not numerical oracles for current ERA/GAST behavior. |
| Julian-date/calendar examples | Chapter 2, §§2.14-2.16 | Demonstrates named time concepts and calendar/JD use. | Use SOFA time routines and pinned leap-second data for reference fixtures; do not implement from the textbook example alone. |

# Conventions

- Chapter 2 states that it normally expresses angles in degrees unless otherwise noted.
- The book adopts azimuth clockwise from south in §2.4; this conflicts with UFUQ's
  north-zero/east-positive convention and must be converted explicitly when comparing
  formulae.
- Altitude is positive above the geometric horizon and zenith distance is its
  complement.
- Right ascension, declination, hour angle, mean place, and apparent place are distinct
  concepts; catalogue frame/epoch and date of observation must remain explicit.
- Diurnal effects and refraction depend on observer/location/conditions; they are not
  properties of immutable catalogue rows.
- Time-system names are semantically meaningful and cannot be replaced by an unlabeled
  JavaScript timestamp or single Julian number.

# Implementation implications

- `SOURCE_REQUIRED`: preserve the conceptual separation catalogue mean place -> motion
  propagation -> date-dependent celestial place -> observer-dependent horizontal
  place.
- `PROJECT_DECISION_REQUIRED`: define exactly which apparent-place and topocentric
  effects UFUQ includes or omits; the textbook's explanatory list does not make that
  decision.
- `SOURCE_REQUIRED`: label the azimuth origin/direction on every formula and serialized
  field. Do not import the book's south-origin signs into UFUQ.
- `SOURCE_REQUIRED`: keep catalogue coordinates separate from observer-dependent
  refraction and horizon/visibility data.
- `EXPERIMENT_REQUIRED`: quantify omitted motion/apparent/EOP/refraction effects over
  the approved date/location range using independent fixtures.
- `PROJECT_DECISION_REQUIRED`: approve the supported time range and leap-second/EOP
  policy; textbook examples are not current operational data.
- `INFORMATIONAL_ONLY`: Chapter 2 can support concise learner explanations once those
  explanations are checked against the final pipeline.

# Testing implications

- Unit tests must make azimuth convention conversion explicit: the book's south-origin
  examples cannot be expected unchanged under UFUQ's north-origin convention.
- Test named intermediate types so catalogue, mean-of-date, apparent/CIRS, observed,
  and horizontal values cannot be interchanged.
- Reference fixtures should isolate proper motion, precession-nutation, aberration,
  parallax, Earth rotation, polar motion, diurnal effects, and refraction where the
  approved pipeline includes them.
- Include horizon, zenith/nadir, meridian, east/west, date-boundary, catalogue-epoch,
  and high-proper-motion cases.
- Malformed inputs include unlabeled degrees/radians, unlabeled time scales, and
  catalogue rows contaminated with observer-dependent values.
- Stop when the authoritative algorithm/data source or measured error budget is absent;
  a matching textbook example is not sufficient.

# Limitations

- *Fundamental Astronomy* is explanatory support, not the authority for current IAU
  models, IERS data, Hipparcos field semantics, leap seconds, or independent expected
  results.
- Chapter 2 intentionally simplifies some presentation and assumes a northern-hemisphere
  observer for exposition; UFUQ must support only its explicitly approved domain
  without inheriting that pedagogical simplification silently.
- The book's azimuth convention is not UFUQ's convention.
- The study did not adopt the chapter's sidereal-time or calendar formulae as production
  algorithms.
- The local file's acquisition provenance is unverified, and the local/publisher
  pagination counts differ.

# Conflicts and ambiguities

- Local metadata reports 548 PDF pages while Springer lists `XIV, 550`. The edition
  identity is verified, but the packaging/page-count difference has not been resolved.
  Source pointers therefore use printed chapter/section identifiers.
- Section 2.4 uses clockwise-from-south azimuth; SOFA `iauHd2ae` and UFUQ use
  clockwise-from-north.
- The textbook's “apparent place” explanation is conceptual. SOFA's “observed place”
  includes additional Earth-orientation, diurnal, and refraction behavior; the labels
  are not interchangeable.
- Worked sidereal-time examples are pedagogical and may use approximations or legacy
  expressions. IERS TN36/SOFA control the modern reference calculation.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Horizontal coordinates are local | Chapter 2, §2.4 | Observer and time belong to the horizontal result, not the catalogue row | `SOURCE_REQUIRED` |
| Zenith distance complements altitude | Chapter 2, §2.4, Eq. (2.10) | Label altitude versus zenith distance in APIs and fixtures | `SOURCE_REQUIRED` |
| Azimuth conventions vary | Chapter 2, §2.4 | Retain UFUQ north-zero/east-positive convention explicitly | `PROJECT_DECISION_REQUIRED` |
| Catalogue mean and apparent places differ | Chapter 2, §2.9 | Use typed, named pipeline stages | `SOURCE_REQUIRED` |
| Proper motion/precession/nutation/parallax/aberration are distinct | Chapter 2, §2.9 | Record implement/omit decisions and bounds separately | `EXPERIMENT_REQUIRED` |
| Diurnal/refraction effects depend on observer | Chapter 2, §2.9 | Do not embed them in catalogue records | `SOURCE_REQUIRED` |
| Sidereal/solar/atomic/dynamical time are distinct | Chapter 2, §§2.13-2.14 | Carry exact time scales and use SOFA/IERS algorithms | `SOURCE_REQUIRED` |
| Textbook formulae do not set production tolerance | Chapter 2 scope; `UFUQ_SOURCE_REGISTER.md` interpretation control 4 | Validate independently | `EXPERIMENT_REQUIRED` |

