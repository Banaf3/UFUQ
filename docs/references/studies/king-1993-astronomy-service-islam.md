# King 1993, Astronomy in the Service of Islam — study dossier

Study status: `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` for historical Qibla context.
This collected volume is `HISTORICAL_CONTEXT_ONLY` for UFUQ geodesy. It supplies no
approved modern algorithm, coordinate, datum, or tolerance.

## Bibliographic identity

- Canonical source ID: `KING-1993`.
- Title: *Astronomy in the Service of Islam*.
- Author: David A. King.
- Edition/year/publisher: first edition, 1993, Variorum.
- Series/identifier: Variorum Collected Studies Series CS416; ISBN
  `0-86078-357-X` / `978-0-86078-357-2`.
- Local file: ignored
  `local-reference/cultural-astronomy/qibla-history/king-1993-astronomy-in-service-of-islam.pdf`.
- Extent/text: 358 PDF pages; 352 scanned book pages plus scan leaves;
  `TEXT_SEARCHABLE_OCR`.
- Verification status: title, author, publisher, year, copyright, contents, ISBN, and
  content extent verified. Acquisition provenance remains unverified; page-dependent
  quotations require image checking.

## UFUQ relevance

- Phases affected: historical context for Phase 2 cultural content and Qibla teaching;
  review context for `AST-005`. It is not an implementation gate for Phase 1.
- Studied: preface XI–XIV (local PDF pp. 17–20); Paper I, “Science in the service of
  religion: the case of Islam,” internal pp. 245–262 (PDF pp. 21–36); Papers IX–XIV
  listed under “The Sacred Direction in Islam,” especially Paper IX *Kibla: sacred
  direction* (PDF pp. 189–206), Paper X *Makka: as the centre of the world*
  (PDF pp. 207–231), Paper XII *On the orientation of the Kaʿba* (internal
  pp. 102–109/PDF pp. 236–243), Paper XIII on astronomical alignments (internal
  pp. 303–312/PDF pp. 244–253), and Paper XIV on early mathematical methods/tables
  (internal pp. 82–149/PDF pp. 254–321).
- Intentionally not studied: crescent-visibility, prayer-time, and universal
  timekeeping papers not needed for the assigned cultural/geodesic question.
- Scope reason: identify distinct historical Qibla traditions and guard against
  converting them into an undocumented modern computation.

## Terminology

- **Folk astronomy**: naked-eye and horizon-phenomenon traditions used in religious
  practice (Paper I, internal pp. 246–257/PDF pp. 22–33).
- **Mathematical astronomy/geography**: scholarly calculation using terrestrial
  coordinates, spherical astronomy, and tables (Paper I, internal pp. 257–260/PDF
  pp. 33–34; Paper XIV).
- **Qibla/kibla**: sacred direction; the historical literature contains different
  operational definitions and conventions (Papers IX–X).
- **Sacred geography**: sector schemes around the Kaʿba associating regions with
  horizon phenomena or sides/corners of the sanctuary (Paper I, PDF pp. 29–32;
  Paper X, internal pp. 3–25/PDF pp. 209–231).
- **Mathematical qibla**: in the surveyed scientific tradition, direction from a
  locality to Mecca along the great circle on a terrestrial sphere (Paper I,
  internal p. 257/PDF p. 33; Paper XIV).

## Concepts and models

1. Historical Qibla determination was plural: early mosque orientation, horizon
   risings/settings, Kaʿba orientation, sector-based sacred geography, spherical
   calculation, tables, maps, and instruments were not one method (Paper I,
   PDF pp. 29–35; Papers IX–XIV).
2. Legal/folk and mathematical traditions could use different definitions and arrive
   at different directions without one being a numerical implementation of the other
   (Papers IX–X; preface, PDF pp. 19–20).
3. Medieval mosque orientation cannot be reverse-engineered safely into a modern
   destination coordinate. Paper I notes that many orientations reflect traditional
   procedures rather than computed qiblas (PDF pp. 29–35).
4. Mathematical treatment requires both locations' latitudes and a longitude
   difference on a sphere; historical geographical data and angular conventions vary
   (Paper I, PDF p. 33; Paper XIV, internal pp. 82–149).
5. Historical astronomical alignment to the Kaʿba/phenomena is cultural and
   architectural evidence, not WGS84 geodesy (Papers XII–XIII).

## Equations and algorithms

The volume documents historical algorithm families but none is promoted to UFUQ
production:

| Historical procedure | Source location | Variables/assumptions | UFUQ status |
|---|---|---|---|
| Great-circle direction on a terrestrial sphere | Paper I, internal p. 257/PDF p. 33; Paper XIV, internal pp. 82–89/PDF pp. 254–261 | Locality and Mecca latitudes, longitude difference; spherical Earth; historical angular convention | `HISTORICAL_CONTEXT_ONLY`; runtime formula is controlled by `ASTRONOMY_SPEC.md` |
| Approximate constructions/tables | Paper XIV, internal pp. 82–149/PDF pp. 254–321 | Historical coordinate tables, varied angular origins/units, approximate and exact procedures | Do not implement from this source; compare historically only |
| Qibla tables | Paper I, PDF pp. 33–35; Paper XIV | Tabulated direction by latitude/longitude arguments | No modern fixture without independent recomputation and approved inputs |
| Horizon/alignment methods | Paper X, PDF pp. 209–231; Papers XII–XIII | Risings/settings, Kaʿba sides/corners, regional traditions | Cultural history; not a geodesic algorithm |

Paper XIV internal p. 88 (local PDF p. 260) describes the distance as the arc of a
great circle joining locality `X` and Mecca `M`. Paper XIV internal p. 104 (local PDF
p. 276) illustrates that historical authors could measure direction from a different
reference line than UFUQ's north-clockwise convention. Therefore formulas or table
values must not be lifted without convention analysis.

## Conventions

- The book is a collected-studies volume; use paper identifier plus internal page, not
  PDF page alone.
- Historical authors variously measure direction from meridian or east/west
  references. UFUQ's clockwise-from-True-North `[0,360)` is a project convention, not
  universal historical notation (Paper XIV, especially internal pp. 103–105/PDF
  pp. 275–277).
- Terrestrial sphere, medieval coordinates, sacred-geography sectors, and modern
  ellipsoidal datums are distinct models.
- “Facing the Kaʿba,” “direction of Mecca,” mosque-axis orientation, and magnetic
  compass indication must not be collapsed.
- No coordinate in the book is an approved UFUQ Kaaba target.

## Implementation implications

- `SOURCE_REQUIRED`: Label King-derived content as historical and identify the exact
  paper/tradition.
- `PROJECT_DECISION_REQUIRED`: UFUQ's runtime model, observer/destination records,
  datum, sign/order, and azimuth convention remain controlled by project decisions.
- `HUMAN_REVIEW_REQUIRED`: Any cultural explanation of historical legal, folk,
  architectural, or astronomical practice needs Islamic-history/cultural review.
- `SOURCE_REQUIRED`: Distinguish horizon/alignment, sacred-geography, approximate
  mathematical, and exact spherical traditions.
- `EXPERIMENT_REQUIRED`: If a historical numerical example is used pedagogically,
  recompute it independently and display its historical assumptions; do not score it
  as modern geodesy.
- `INFORMATIONAL_ONLY`: Mosque orientation or a historical map must never supply the
  production Kaaba coordinate.
- `HUMAN_REVIEW_REQUIRED`: Nothing in the studied papers establishes specifically
  Najdi star usage.

## Testing implications

- Negative-test that historical maps/tables cannot populate the destination-coordinate
  configuration.
- Require a `historicalMethod` label and source paper/page for historical examples.
- Test that True North, magnetic north, Polaris line-of-sight, mosque axis, and Qibla
  bearing remain distinct concepts.
- A modern numerical case must cite an approved coordinate/datum and an independent
  modern oracle, never King alone.
- Reject learner-facing historical claims without human review and explicit period/
  geography.

## Limitations

- King is a historian of Islamic science here, not a modern geodetic standards body.
- OCR requires visual confirmation for quotation and page-sensitive transcription.
- The collected articles reflect research states and terminology at their original
  publication dates.
- Historical coordinate tables may contain source/copying errors and different
  conventions.
- The volume does not approve a Kaaba coordinate, WGS84 realization, runtime
  algorithm, numerical tolerance, or Najdi cultural mapping.

## Conflicts and ambiguities

- “Qibla” may mean direction to the Kaʿba, direction to Mecca, a regionally accepted
  horizon phenomenon, or an architectural axis in different discussions.
- Sacred-geography diagrams and mathematical geography address different historical
  questions. Neither silently overrides the other.
- Historical angular origins differ; apparent numerical disagreement may be a
  convention mismatch.
- The project's confirmed spherical bearing is a modern project decision and must not
  be represented as the one historical method.

## Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Folk and mathematical astronomy are distinct traditions | Paper I, internal pp. 246–260/PDF pp. 22–34 | Label the historical method and authority | `SOURCE_REQUIRED` |
| Early/traditional mosque orientations may differ from computed qiblas | Paper I, PDF pp. 29–35 | Never infer target coordinates from an axis | `INFORMATIONAL_ONLY` |
| Sacred geography uses region/phenomenon schemes | Paper X, internal pp. 3–25/PDF pp. 209–231 | Historical/cultural context only | `HUMAN_REVIEW_REQUIRED` |
| Mathematical qibla uses a great circle on a sphere | Paper I, PDF p. 33; Paper XIV, internal pp. 82–89 | Compare conceptually; project spec controls runtime | `PROJECT_DECISION_REQUIRED` |
| Historical direction origins can vary | Paper XIV, internal pp. 103–105/PDF pp. 275–277 | State azimuth origin/direction for every case | `SOURCE_REQUIRED` |
| Kaʿba orientation/alignment is historical evidence | Papers XII–XIII | Do not convert alignment into production coordinate | `INFORMATIONAL_ONLY` |
| No modern coordinate/datum is approved | Entire studied Qibla section | Stop production cases under `AST-005` | `PROJECT_DECISION_REQUIRED` |
