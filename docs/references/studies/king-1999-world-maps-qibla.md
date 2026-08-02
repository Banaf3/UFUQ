# King 1999, World-Maps for Finding the Direction and Distance to Mecca — study dossier

Study status: `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` for historical method
classification and map/table limitations. It is `HISTORICAL_CONTEXT_ONLY` for modern
UFUQ geodesy.

## Bibliographic identity

- Canonical source ID: `KING-1999`.
- Title: *World-Maps for Finding the Direction and Distance to Mecca: Innovation and
  Tradition in Islamic Science*.
- Author: David A. King.
- Edition/year/publisher: 1999, Brill, Leiden/Boston/Köln.
- Identifiers: ISBN `90-04-11367-3`; series ISSN `0169-8729`.
- Local file: ignored
  `local-reference/cultural-astronomy/qibla-history/king-1999-world-maps-qibla.pdf`.
- Extent/text: 679 PDF pages; bibliographic extent xxviii + 638;
  `TEXT_SEARCHABLE_OCR`.
- Verification status: title, author, publisher, year, copyright, contents, ISBN, and
  extent verified. Acquisition provenance remains unverified; quotations require
  visual confirmation.

## UFUQ relevance

- Phases affected: historical framing for Phase 2 Qibla teaching and review context for
  `AST-005`; not an authority for the Phase 1 runtime.
- Studied: foreword xiii–xv (PDF pp. 18–20); prefaces xvi–xxiii (PDF pp. 21–28);
  Chapter 1 sections on folk astronomy, mathematical methods/geography/cartography
  (printed pp. 7–39); Chapter 2, especially §§2.1–2.5 (printed pp. 47–70/PDF
  pp. 82–105), §2.8 (printed pp. 89–99/PDF pp. 124–134), and §2.9 opening
  (printed p. 100 onward/PDF p. 135 onward).
- Supporting/later: Chapter 3 on coordinate/table sources and errors; Part II and
  Chapter 9 on Safavid Mecca-centred maps.
- Intentionally not studied in depth: full gazetteers, appendices, maker biographies,
  and object catalogues. They are not needed for a modern direction implementation.
- Scope reason: identify historical method classes, conventions, data-error risks, and
  the explicit prohibition on measuring direction from non-mathematical sacred-
  geography diagrams.

## Terminology

- **Qibla**: the sacred direction; King distinguishes legal/folk approaches from
  mathematical-scientific approaches (§§2.1–2.2, printed pp. 47–50).
- **ʿayn al-Kaʿba / jihat al-Kaʿba**: facing the Kaʿba itself versus a broader
  directional notion illustrated in a legal treatise (Fig. 2.2.3 and surrounding
  discussion, printed p. 51/PDF p. 86). Translation and legal interpretation are
  `HUMAN_REVIEW_REQUIRED`.
- **Sacred geography**: region-based schemes around the Kaʿba using horizon phenomena;
  King warns they are not maps in the accepted mathematical sense (§2.3, printed
  pp. 51–55).
- **Mathematical qibla**: direction to Mecca along a great circle on the terrestrial
  sphere, measured from the local meridian (§2.4, printed p. 56/PDF p. 91).
- `inhirāf al-qibla`: literally the inclination of the qibla to the meridian in King's
  explanation (§2.4, printed p. 56). Transliteration/translation require review.
- **Mecca-centred world-map**: a cartographic instrument/grid designed to display
  direction and distance, distinct from a sacred-geography diagram (Part II; §9).

## Concepts and models

1. Historical legal scholars and scientists could define the target direction
   differently: toward an oriented building versus toward the city represented as a
   point in mathematical geography (§2.1, printed pp. 47–48/PDF pp. 82–83).
2. Folk methods used cardinal directions and astronomical risings/settings; sacred
   geography grouped regions into sectors (§§2.2–2.3, printed pp. 48–55).
3. Sacred-geography diagrams are non-mathematical and unsuitable for measuring a
   locality's qibla; King states this explicitly (§2.3, printed p. 54/PDF p. 89).
4. Mathematical geography models the locality `X` and Mecca `M` on a terrestrial
   sphere and solves a spherical triangle using their latitudes and longitude
   difference (§2.4 and Fig. 2.4.1, printed pp. 56–57/PDF pp. 91–92).
5. Historical mathematical sources contain both approximate and accurate methods,
   tables, maps, and instruments (§§2.4–2.9).
6. Accuracy of computed qiblas is constrained by the historical geographical
   coordinates. King notes that accurate computation can still disagree with modern
   results when input longitudes are wrong (§2.4 conclusion/§2.5 opening, printed
   pp. 63–64/PDF pp. 98–99).
7. Surviving tables can contain copyist errors (§2.5, printed p. 64/PDF p. 99);
   provenance and transcription checks are therefore essential even for historical
   reconstruction.

## Equations and algorithms

### Historical spherical formulation

Section 2.4 and Fig. 2.4.1 (printed pp. 56–57/PDF pp. 91–92) define:

- `X`: observer locality; `M`: Mecca.
- `φ` and `φ_M`: terrestrial latitudes.
- `Δλ = λ - λ_M`: longitude difference.
- `q`: direction at `X` to `M`, measured from the local meridian.
- `d`: spherical angular distance.

The valid domain is the historical terrestrial-sphere model with source-specific
geographical data. No ellipsoid, datum realization, height, coordinate uncertainty,
modern Kaaba point, or `[0,360)` normalization is defined.

### Algorithm families

| Family | Exact location | Assumptions/numerical concerns | UFUQ use |
|---|---|---|---|
| Folk/horizon method | §2.2, printed pp. 48–50/PDF pp. 83–85 | Cardinal directions, risings/settings, regional/legal practice | Historical teaching context only |
| Sacred-geography sectors | §2.3, pp. 51–55/PDF pp. 86–90 | No calculation; approximate regional direction | Never measure a modern bearing from these diagrams |
| Approximate mathematical constructions | §2.4, pp. 57–60/PDF pp. 92–95; Figs. 2.4.2–2.4.4 | Spherical/planar approximations; convention and input-data dependence | Historical comparison only |
| Accurate spherical methods | §2.4, pp. 60–63/PDF pp. 95–98 | Spherical trigonometry and historical coordinates | Project spec, not King, controls UFUQ's modern formula |
| Tables | §2.5, pp. 64–70/PDF pp. 99–105 | Arguments are latitude/longitude differences; surviving copies may have errors | Reconstruct only with provenance and independent recomputation |
| Maps and instruments | §§2.8–2.9, pp. 89 onward/PDF pp. 124 onward | Projection/grid/instrument-specific; some display precomputed qiblas | Historical object study; no target coordinate extraction |

No historical table value, map reading, or formula is adopted as a production fixture.

## Conventions

- Printed Chapter 2 pages are 35 less than local PDF pages in the studied section
  (`printed p. 56 = PDF p. 91`).
- The mathematical direction is described relative to the local meridian, but
  historical sign/quadrant notation varies. UFUQ's north-clockwise `[0,360)` is a
  separate project convention.
- The model in §2.4 is a sphere. Karney's ellipsoid, WGS84 datum realization, and
  historical geographical tables are different authorities.
- Mecca as a mathematical point, the Kaʿba as an oriented building, a mosque axis,
  and a sacred-geography sector are distinct.
- Magnetic compasses appear as historical instruments; magnetic north is not
  geographic True North.

## Implementation implications

- `SOURCE_REQUIRED`: Identify the historical method class—folk, sacred-geographic,
  approximate mathematical, accurate spherical, tabular, map, or instrument.
- `PROJECT_DECISION_REQUIRED`: Use only the approved UFUQ observer/destination
  coordinate records, datum, model, and azimuth convention for production.
- `INFORMATIONAL_ONLY`: Do not read a production coordinate or bearing from a
  historical map, table, mosque orientation, or sacred-geography diagram.
- `SOURCE_REQUIRED`: A historical numerical reconstruction must preserve the original
  geographical data, method, convention, source version, and known errors.
- `EXPERIMENT_REQUIRED`: Recompute any displayed historical numerical case with an
  independent implementation and compare under both historical and approved modern
  inputs.
- `HUMAN_REVIEW_REQUIRED`: Historical/legal/cultural explanations require qualified
  review.
- `HUMAN_REVIEW_REQUIRED`: The book provides no specifically Najdi star-pattern
  evidence.

## Testing implications

- Add a negative test that sacred-geography diagram data cannot populate modern
  destination coordinates or bearings.
- Historical fixtures must include method class, printed source location, source
  coordinates, convention, and a “not production geodesy” label.
- Mutate longitude sign, coordinate order, azimuth origin, and spherical/ellipsoidal
  model to ensure convention differences are detected.
- Require independent recomputation of table/map readings and record transcription
  uncertainty.
- Production Qibla tests remain blocked until `AST-005` and `AST-006` are approved.

## Limitations

- This is historical scholarship, not a modern geodetic specification.
- OCR is unsuitable for unchecked quotation or exact numerical transcription.
- Historical coordinate tables, copied manuscripts, and instruments can contain
  errors.
- The book provides no approved Kaaba coordinate, datum, ellipsoid, observer location,
  magnetic-declination model, or numerical tolerance.
- It does not establish Najdi cultural claims.

## Conflicts and ambiguities

- Legal/folk “direction toward the Kaʿba” and scientific “great-circle direction to
  Mecca” are historically distinct definitions (§2.1, printed pp. 47–48).
- Sacred-geography diagrams may look map-like but King explicitly separates them from
  mathematical maps (§2.3, printed pp. 51–55).
- Approximate procedures may be adequate within their historical setting but are not
  interchangeable with exact spherical or modern ellipsoidal methods.
- A mathematically accurate result from inaccurate historical coordinates is not an
  accurate modern bearing (§§2.4–2.5, printed pp. 63–64).

## Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Legal/folk and scientific definitions can differ | §2.1, printed pp. 47–48/PDF pp. 82–83 | Name the target semantics; do not conflate building and point | `SOURCE_REQUIRED` |
| Folk methods use cardinal/horizon phenomena | §2.2, printed pp. 48–50 | Historical context only | `HUMAN_REVIEW_REQUIRED` |
| Sacred-geography diagrams are not measurable modern maps | §2.3, especially printed p. 54/PDF p. 89 | Prohibit coordinate/bearing extraction | `SOURCE_REQUIRED` |
| Mathematical qibla is a spherical great-circle direction from local meridian | §2.4, printed p. 56; Fig. 2.4.1, p. 57 | Compare terminology; project spec controls production | `PROJECT_DECISION_REQUIRED` |
| Approximate and accurate methods coexist | §2.4, printed pp. 57–63 | Label every historical result by method | `SOURCE_REQUIRED` |
| Historical input coordinates limit accuracy | §2.4 conclusion, printed p. 63/PDF p. 98 | Preserve data provenance and error | `EXPERIMENT_REQUIRED` |
| Surviving tables may contain copying errors | §2.5, printed p. 64/PDF p. 99 | Verify transcription/recompute independently | `SOURCE_REQUIRED` |
| Historical maps/instruments are not coordinate authorities | §§2.8–2.9 | Never derive UFUQ's Kaaba point from them | `PROJECT_DECISION_REQUIRED` |
