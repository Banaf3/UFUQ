# Source notes

Start with `docs/references/syntheses/qibla-geodesy-synthesis.md`. Exact evidence and
limitations are in:

- `docs/references/studies/karney-geodesics.md`;
- `docs/references/studies/king-1993-astronomy-service-islam.md`; and
- `docs/references/studies/king-1999-world-maps-qibla.md`.

- `KARNEY-2013` — ellipsoidal direct/inverse geodesic algorithms and difficult-case
  analysis. It supplies no UFUQ destination coordinate and grants no cultural approval.
- `IERS-TN36-2010` — official reference-system terminology where applicable. Record
  later corrections separately; do not silently merge them.
- `KING-1993` and `KING-1999` — historical context only. Neither is a production
  geodesic specification, coordinate authority, or numerical oracle.
- `UFUQ-ASTRO-SPEC` — approved spherical runtime baseline, True-North azimuth
  convention, and unresolved Kaaba-coordinate/tolerance decisions.
- `UFUQ-ADR-003` — coordinate, sign, datum, and validation decisions.

`AST-SRC-008` in `docs/references/SOURCE_GAPS.md` is unresolved. If the approved Kaaba
coordinate/datum record is absent, stop before producing or approving a production
Qibla value. Do not recover a coordinate from memory, a map, or a search snippet.
