# Karney, Algorithms for Geodesics — study dossier

Study status: `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE`. This dossier studies the
local arXiv v2 preprint. It does not treat that preprint as approval of UFUQ's runtime
model, destination coordinates, datum, or tolerances.

## Bibliographic identity

- Canonical source ID: `KARNEY-2012-ARXIV-V2` (the source register also uses
  `KARNEY-2013` for the published counterpart).
- Title: *Algorithms for Geodesics*.
- Author: Charles F. F. Karney.
- Edition/version: arXiv `1109.4448v2`, revised 28 March 2012.
- Year/publisher: 2012 preprint; the corresponding 2013 journal article has DOI
  `10.1007/s00190-012-0578-z`.
- Identifier: arXiv `1109.4448v2`.
- Local file: ignored
  `local-reference/astronomy/geodesy/karney-2012-algorithms-for-geodesics-preprint.pdf`.
- Extent/text: 12 PDF pages; reliable searchable text layer.
- Verification status: title, author, revision date, arXiv identifier, and extent
  verified locally. Acquisition provenance remains `PROVENANCE_UNVERIFIED`.

## UFUQ relevance

- Phases affected: Phase 1 sensitivity/reference work if ellipsoidal Qibla geodesy is
  included; Phase 2 only after the separate Kaaba coordinate/datum decision.
- Project decisions affected: `AST-005` (destination authority, not supplied here) and
  `AST-006` (measured error budget/tolerance, not supplied here).
- Studied: abstract and §1; §§2–5; WGS84 Table 1; inverse examples in Tables 3–6;
  implementation/accuracy evidence in §7.
- Supporting-only: §3 differential quantities.
- Intentionally not studied in depth: §6 polygonal area and §8 ellipsoidal gnomonic
  projection. Neither is required for one initial Qibla bearing.
- Scope reason: UFUQ needs the inverse problem, azimuth semantics, difficult-case
  behavior, numerical evidence, and independent cases—not polygon areas or a new map
  projection.

## Terminology

- A geodesic is the shortest surface path on the ellipsoid in the ordinary inverse
  problem (§1, PDF p. 1).
- The **direct problem** supplies the start point, initial azimuth, and length; the
  **inverse problem** supplies two points and seeks the shortest path and endpoint
  azimuths (§1, PDF p. 1; §8 summary, PDF p. 11).
- `a` and `b` are equatorial and polar semiaxes; `f` is flattening; `n` is third
  flattening; `φ` is geodetic latitude; `β` is reduced latitude (§2, Eqs. 1–6,
  PDF p. 2).
- `λ12` is longitude difference, `s12` geodesic length, and `α1`, `α2` the forward
  azimuths at the endpoints (Fig. 1 and caption, PDF p. 1; §2, PDF p. 2).
- **Reduced length** `m12` and **geodesic scales** `M12`, `M21` describe neighboring
  geodesics (§3, PDF pp. 4–5). They assist the inverse iteration; they are not needed
  in UFUQ's serialized result unless a selected library exposes them for diagnostics.

## Concepts and models

1. The ellipsoid of revolution is parameterized independently of any destination
   coordinate. The WGS84 example uses `a = 6,378,137 m` and
   `f = 1/298.257223563` (Table 1, PDF p. 3).
2. Mapping to an auxiliary sphere preserves azimuth while replacing geodetic latitude
   with reduced latitude. It is a computational technique, not a change of physical
   datum (§2, Eqs. 5–14, PDF p. 2).
3. The inverse problem is solved as root-finding in the initial azimuth: solve a hybrid
   problem for a trial `α1`, compare its longitude difference with the requested
   `λ12`, and update (§4, PDF pp. 5–6).
4. Meridional and equatorial configurations receive explicit branches; the general
   case uses Newton iteration (§4, PDF p. 6).
5. A dedicated near-antipodal starting construction avoids the convergence failure
   associated with the cited Vincenty iteration (§§4–5, PDF pp. 6–8).
6. The paper tests its implementation against higher-order, high-precision results.
   Those figures characterize that implementation and test setup, not every library
   implementing a nominally similar algorithm (§7, PDF pp. 9–10).

## Equations and algorithms

| Item and location | Variables, units, assumptions, domain | UFUQ use and validation |
|---|---|---|
| Ellipsoid definitions, §2 Eqs. (1)–(4), PDF p. 2 | `a,b` in one length unit; `f,n,e,e′` dimensionless; oblate/prolate ellipsoid of revolution | Store the named ellipsoid and its parameters; compare against an independently pinned library. |
| Reduced latitude, §2 Eq. (6), PDF p. 2 | `tan β = (1-f) tan φ`; angles internally consistent | Explanatory support for the algorithm. UFUQ should call a reviewed implementation, not mechanically translate the derivation. |
| Clairaut relation, §2 Eq. (5), PDF p. 2 | Relates azimuth and reduced latitude along a geodesic | Useful as a diagnostic invariant away from singular cases; not a substitute for reference cases. |
| Inverse canonical domain, §4 Eq. (44), PDF p. 5 | Uses symmetry to restrict endpoint ordering and longitude difference | A selected implementation may normalize internally. UFUQ must still specify input order, signs, and output normalization. |
| Newton derivative, §4 Eq. (46), PDF p. 6 | `dλ12/dα1` uses `m12`, endpoint reduced latitude, and endpoint azimuth; singular limit treated separately in Eq. (47) | Supports the robust inverse method. Validate difficult cases instead of assuming all Newton iterations are safe. |
| Near-antipodal start, §5 Eqs. (53)–(57), PDF pp. 7–8 | Scaled endpoint coordinates, astroid construction, positive root, starting `α1` | Required evidence for near-antipodal robustness if this algorithm family is selected. Do not reimplement from the dossier alone. |
| Near-antipodal reference case, Tables 4–6, PDF pp. 8–9 | WGS84; `φ1=-30°`, `φ2=29.9°`, `λ12=179.8°`; result includes `α1=161.89052473633°`, `α2=18.09073724574°`, `s12=19,989,832.827610 m` | Candidate independent regression case. Recompute with a separately pinned tool and preserve the paper-version provenance before use. |
| Accuracy study, §7, PDF pp. 9–10 | Higher-order `O(f^30)`/high-precision comparison on WGS84; reported direct/inverse roundoff below 15 nm; typically 2–4 Newton steps, rare cases up to 16, no observed failures | `INFORMATIONAL_ONLY`. It does not set UFUQ's tolerance and does not prove another implementation's behavior. |

## Conventions

- Latitude is geodetic latitude `φ`; longitude enters through the endpoint difference
  `λ12` (§2, PDF pp. 1–2).
- Figure 1 defines `α1` and `α2` as azimuths in the forward travel direction. The paper
  explicitly notes that some other authors use a back azimuth at point 2 (§2, PDF p. 2).
- The paper's examples use degrees in displayed inputs/outputs and metres for WGS84
  lengths (Tables 1–6, PDF pp. 3, 7–9). Production APIs must state whether they accept
  degrees or radians.
- The paper supplies an ellipsoid algorithm, not a geodetic datum realization or epoch.
  `WGS84` in Table 1 is a parameter set for examples; UFUQ must approve both endpoints'
  coordinate source and datum separately.
- Output azimuth normalization is an API/project convention. UFUQ currently requires
  clockwise from geographic True North in `[0,360)`; this project convention must be
  checked against the selected library's return convention.

## Implementation implications

- `SOURCE_REQUIRED`: If an ellipsoidal reference is used, name the inverse-geodesic
  algorithm/library/version and the exact ellipsoid parameters.
- `PROJECT_DECISION_REQUIRED`: Approve observer and Kaaba coordinates, coordinate
  sources, datum/frame, order, sign, precision, and uncertainty under `AST-005`.
- `PROJECT_DECISION_REQUIRED`: Define whether the runtime remains the approved
  spherical initial bearing or changes by an approved deviation to an ellipsoidal
  inverse solution.
- `SOURCE_REQUIRED`: Preserve the distinction between forward and back azimuth; expose
  the initial forward azimuth at the observer.
- `EXPERIMENT_REQUIRED`: Exercise meridional, equatorial, coincident, polar,
  near-antipodal, antipodal, and longitude-wrap partitions using independent tools.
- `EXPERIMENT_REQUIRED`: Derive a measured comparison/error budget. Do not adopt the
  paper's sub-micrometre implementation result as UFUQ's tolerance.
- `INFORMATIONAL_ONLY`: Reduced length, scales, area, and gnomonic projection remain
  internal/supporting unless a future requirement justifies exposing them.

## Testing implications

- Pin the independent library, version, ellipsoid, coordinate order, units, and
  azimuth-normalization wrapper.
- Recompute Tables 4–6 as a difficult-case candidate; do not hand-copy its output into
  a production data record without a generation manifest.
- Add inverse/direct round-trip tests where the reference tool supports both, while
  accounting for non-unique antipodal solutions.
- Test longitude-sign and coordinate-order mutants, forward-versus-back azimuth, wrap
  at `0/360`, both hemispheres, and Malaysian observer cases after coordinates are
  approved.
- Compare bearings with wrapped circular difference. `AST-006` must justify the
  threshold; until then the production fixture is blocked.
- Reject non-finite/out-of-range inputs and define coincident/antipodal behavior
  explicitly.

## Limitations

- Karney does not supply, endorse, or validate a Kaaba coordinate.
- The paper does not decide UFUQ's observer datum, height handling, magnetic
  declination, True-North realization, output range, or learner tolerance.
- Its accuracy claims concern the described implementation and test environment.
- A geodesic azimuth is not a magnetic-compass heading and is not the line of sight to
  Polaris.
- The local file is the 2012 arXiv v2 preprint, not the publisher PDF.

## Conflicts and ambiguities

- UFUQ's approved baseline is a spherical initial great-circle bearing; Karney is an
  ellipsoidal sensitivity/reference source unless an approved deviation changes that.
- Endpoint `α2` conventions differ across literature. Adapters must verify whether a
  library returns a forward or back azimuth.
- An exact antipodal pair has non-unique shortest geodesics. A library result cannot be
  treated as a unique semantic answer without a project policy.
- Near-antipodal success in this paper does not prove that a third-party wrapper uses
  the same algorithm or settings.

## Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Direct versus inverse problem | §1 and Fig. 1, PDF p. 1 | Qibla geodesy needs the inverse problem from observer to approved destination | `SOURCE_REQUIRED` |
| Ellipsoid parameters are explicit inputs | §2 Eqs. (1)–(4), PDF p. 2; Table 1, PDF p. 3 | Version the ellipsoid/datum decision | `PROJECT_DECISION_REQUIRED` |
| Both endpoint azimuths are forward in this paper | Fig. 1, PDF p. 1; §2, PDF p. 2 | Verify library return convention | `SOURCE_REQUIRED` |
| General inverse solution is a root-finding problem | §4, PDF pp. 5–6 | Use a robust implementation and difficult-case tests | `SOURCE_REQUIRED` |
| Near-antipodal start is explicit | §5 Eqs. (53)–(57), PDF pp. 7–8 | Near-antipodal tests are mandatory | `EXPERIMENT_REQUIRED` |
| Traceable difficult reference case exists | Tables 4–6, PDF pp. 8–9 | Recompute as an independent fixture candidate | `EXPERIMENT_REQUIRED` |
| Reported nanometre accuracy is implementation-specific | §7, PDF pp. 9–10 | It cannot become the UFUQ tolerance | `INFORMATIONAL_ONLY` |
| Destination coordinate is absent | Entire source, scoped against `AST-005` | Stop production Qibla calculation until approved | `PROJECT_DECISION_REQUIRED` |
