# Qibla geodesy synthesis

## Scope and authority

This synthesis separates three questions that the sources do not collapse:

1. modern UFUQ direction semantics and approved endpoint records;
2. a numerical inverse-geodesic method; and
3. historical Qibla definitions, practices, tables, and maps.

The controlling order is:

1. approved UFUQ observer and destination coordinate/datum records;
2. the approved UFUQ runtime model and azimuth convention;
3. Karney's geodesic work for an ellipsoidal algorithm and difficult-case analysis;
4. independently pinned numerical implementations/cases; and
5. King only for historical context.

Karney supplies no Kaaba coordinate. King supplies no production coordinate, modern
datum, runtime algorithm, or tolerance.

## Agreements and distinctions

- A modern direction claim needs both endpoint coordinates, their source/datum, a
  named model, units/sign/order, and an azimuth convention.
- The inverse problem returns the shortest-path initial direction at the observer;
  forward and back azimuth conventions differ between APIs and literature.
- Spherical, ellipsoidal, horizon/folk, sacred-geography, architectural, tabular, and
  map methods are different models.
- Geographic True North, magnetic north, the line of sight to Polaris, a mosque axis,
  and Qibla are not interchangeable.
- Historical mathematical accuracy can be limited by historical input coordinates;
  copying a table/map value into a modern system is not validation.
- Near-antipodal, antipodal, coincident, polar, meridional, equatorial, and wrap cases
  need explicit behavior.

## Source comparison

| Topic | Karney | King 1993/1999 | UFUQ treatment |
|---|---|---|---|
| Geometry | Ellipsoid of revolution; direct/inverse geodesics | Historical sphere, approximate methods, horizon sectors, tables, maps, instruments | Runtime currently uses the approved spherical initial bearing; ellipsoidal work is reference/sensitivity unless an approved deviation changes it. |
| Inputs | Two geodetic latitudes/longitudes and ellipsoid parameters | Source-specific historical coordinates and conventions | Production uses separately approved observer/Kaaba records; neither source supplies them. |
| Azimuth | Forward azimuth at both endpoints in the paper's convention | Historical origins/quadrants vary | Adapter must expose initial forward azimuth clockwise from True North in the approved range. |
| Difficult cases | Explicit branches and near-antipodal start, §§4-5 | Historical sources are not numerical robustness specifications | Use Karney-derived independent difficult cases for a selected ellipsoidal library. |
| Accuracy | Implementation-specific high-precision comparison, §7 | Historical tables/maps can contain input/transcription error | Measure UFUQ residuals; neither source provides a UFUQ threshold. |
| Destination | Not supplied | Historical Mecca/Kaaba concepts and coordinates vary | `AST-005` remains a stop condition. |

## Candidate UFUQ rules

| Rule | Evidence | Classification |
|---|---|---|
| Record observer and destination coordinate source, datum/frame, order/sign, precision, uncertainty, version/date, and approval. | Project AST-005; Karney §2 shows endpoints/ellipsoid are independent inputs | `PROJECT_DECISION_REQUIRED` |
| Stop production calculation or fixture approval if the Kaaba destination coordinate or datum is unapproved. | `SOURCE_GAPS.md` AST-SRC-008; neither Karney nor King supplies authority | Unresolved stop condition |
| Name the runtime as either the approved spherical initial bearing or a specified ellipsoidal inverse method; do not mix labels. | `ASTRONOMY_SPEC.md`; Karney §§1, 4 | `PROJECT_DECISION` |
| Verify the selected API's initial/final, forward/back, unit, order, sign, and normalization conventions. | Karney Fig. 1 and §2 | `SOURCE_SUPPORTED_FACT` |
| Distinguish True North, magnetic north, Polaris line of sight, mosque axis, historical sector, and Qibla. | King 1993 Paper I/Papers IX-XIV; King 1999 §§2.1-2.4; project spec | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Define coincident, polar, near-antipodal, antipodal, non-finite, and out-of-range behavior before release. | Karney §§4-5; project validation policy | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION_REQUIRED` |
| Independently recompute difficult cases, including Karney Tables 4-6, under a pinned implementation. | Karney §§4-7, Tables 4-6 | `EXPERIMENT_REQUIRED` |
| Compare bearings with wrapped circular difference and approve a threshold only after a measured error budget. | `ASTRONOMY_SPEC.md`; Karney §7 limitations | `EXPERIMENT_REQUIRED` |
| Historical examples retain method, source coordinates, original convention, and “not production geodesy” status. | King 1999 §§2.1-2.9; King 1993 Papers IX-XIV | `HUMAN_REVIEW_REQUIRED` / informational |
| Never extract a production coordinate or bearing from a historical map, table, mosque orientation, or sacred-geography diagram. | King 1999 §2.3 p. 54 and §§2.5, 2.8-2.9 | Stop condition |

## Required tests

- Both-hemisphere and approved Malaysian observer cases after endpoint approval.
- Longitude sign/order mutants and degree/radian mistakes.
- Initial versus endpoint/back azimuth and `[0,360)` wrap.
- Meridional, equatorial, coincident, polar, near-antipodal, antipodal, and invalid
  cases.
- Independent spherical/ellipsoidal cases with exact tool/version/ellipsoid/inputs.
- Wrapped residuals and a measured error budget; no copied tolerance.
- Negative tests preventing historical sources from populating production coordinate
  configuration.

## Unresolved gaps

- `AST-005`: an approved Kaaba coordinate, datum, source, precision, uncertainty, and
  version/date.
- The runtime remains spherical unless an approved deviation selects an ellipsoidal
  model.
- The independent numerical library/environment and measured tolerance are unpinned.
- Historical/legal explanations require qualified human review and do not establish a
  specifically Najdi claim.

