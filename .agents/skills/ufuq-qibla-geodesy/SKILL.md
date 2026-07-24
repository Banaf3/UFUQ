---
name: ufuq-qibla-geodesy
description: Validate or review UFUQ Qibla direction calculations, observer and destination geodetic coordinates, inverse-geodesic conventions, azimuth semantics, and independent geodesic reference cases. Use for modern Qibla geodesy; do not use for general celestial transformations or historical/cultural interpretation.
---

# UFUQ Qibla Geodesy

Define a reproducible modern direction claim without extracting a production coordinate
or algorithm from historical material.

## Trigger conditions

Use this skill for:

- selecting or reviewing spherical or ellipsoidal Qibla direction semantics;
- observer/destination coordinates, datums, inverse-geodesic calls, bearings, wrap,
  degeneracy, or numerical reference cases;
- distinguishing True North, magnetic north, celestial cues, and Qibla headings.

Do not trigger it for:

- general equatorial-to-horizontal astronomy; use `ufuq-astronomy-validation`;
- catalogue parsing or data artifacts; use `ufuq-catalogue-provenance`;
- historical qibla practice, Arabic terminology, or Najdi cultural approval; use
  `ufuq-najdi-arabian-sky`;
- UI compass styling with no direction-correctness claim.

## Required project files

Read `AGENTS.md`, `docs/ASTRONOMY_SPEC.md`, `docs/IMPLEMENTATION_DECISIONS.md`,
`docs/PHASES.md`, `docs/TEST_PLAN.md`,
`docs/adr/003-astronomical-coordinate-conventions.md`,
`docs/references/UFUQ_SOURCE_REGISTER.md`,
`docs/references/SOURCE_GAPS.md`,
`docs/references/syntheses/qibla-geodesy-synthesis.md`, and this skill's four
reference files. Open only the Karney/King dossiers linked for the affected rule by
`references/traceability.md`. Read the approved target-coordinate decision and datum
record before any production case.

## Source authority order

1. The approved UFUQ observer and Kaaba destination coordinate/datum records.
2. The approved runtime Qibla model and azimuth convention in project decisions.
3. Karney's geodesic algorithms for ellipsoidal inverse-geodesic methods and difficult
   cases.
4. Official IERS/WGS 84 terminology applicable to frames, datums, and ellipsoids.
5. Independent numerical implementations/reference cases.
6. King's works for historical context only.

Historical sources never override a modern geodetic specification.

## Mandatory workflow

1. Record observer latitude, east-positive longitude, height if applicable, coordinate
   source, datum/reference frame, epoch if applicable, and precision.
2. Record destination latitude, east-positive longitude, coordinate source, datum,
   version/date, precision, uncertainty, and approval. Stop if either destination
   coordinate or datum is unapproved.
3. Name the runtime model: spherical initial great-circle bearing or a specified
   ellipsoidal inverse-geodesic method. Do not mix them under one label.
4. Define input order, radians/degrees, longitude sign, inverse-geodesic return branch,
   forward-azimuth convention, normalization range, and clockwise-from-True-North
   semantics.
5. Distinguish geographic True North from magnetic north and from the elevated
   line-of-sight to Al-Jady/Polaris.
6. Define coincident, polar, near-antipodal, antipodal, non-finite, and out-of-range
   behavior before testing.
7. Create independent numerical cases covering Malaysian observers, wrap, both
   hemispheres, poles as reference-only where supported, and degenerate/difficult
   geometry. Record the independent tool/version and inputs.
8. Compare with wrapped circular differences and a measured error budget. Do not invent
   a tolerance to make a test pass.
9. Confirm every mandatory conclusion has a basis in
   `references/traceability.md`, then report with `references/output-template.md`,
   including every unresolved authority decision.

## Required evidence

- Approved observer and destination source/datum records.
- Versioned runtime model and azimuth convention.
- Independent implementation/tool and case provenance.
- Per-case expected/actual bearings and wrapped differences.
- Explicit difficult/degenerate-case behavior.
- Error-budget and tolerance rationale scoped to the tested model.

## Stop conditions

Stop production calculation, fixture approval, and learner scoring if the Kaaba
destination coordinate or datum is not approved. Also stop when observer datum,
algorithm, azimuth convention, degeneracy policy, independent reference, or justified
tolerance is missing.

## Prohibited assumptions

Do not invent or silently round the Kaaba coordinate. Do not extract a production
coordinate from a historical map. Do not treat Karney as approving UFUQ's destination
coordinate. Do not use King's historical work as a geodesic algorithm specification.
Do not conflate True North, magnetic north, Polaris, and Qibla.

## Required output

Use `references/output-template.md`. Mark each assertion as
`SOURCE_SUPPORTED_FACT`, `PROJECT_DECISION`, `PROVISIONAL_CHOICE`, or
`UNRESOLVED_QUESTION`, and state whether the production calculation must stop.

## Relevant validation commands

Use repository commands only after real behavior exists:

```text
npm run check
npm run test
npm run test:reference
npm run boundaries
```

Use a separately pinned geodesic reference command for numerical cases. The independent
reference must not import production UFUQ code.
