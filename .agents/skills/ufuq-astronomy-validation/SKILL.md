---
name: ufuq-astronomy-validation
description: Validate UFUQ celestial-coordinate, time, observer, visibility, and reference-fixture work. Use for astronomical transformations, policies, tolerances, or science evidence; do not use for catalogue acquisition alone, Qibla geodesy, or cultural-name approval.
---

# Ufuq Astronomy Validation

Establish whether an astronomical result is defined, independently reproducible, and
within a measured error budget before UFUQ calls it correct.

## Trigger conditions

Use this skill for:

- catalogue-epoch astrometry propagated to an observation time;
- coordinate-frame, precession/nutation, Earth-rotation, time-scale, observer, horizon,
  refraction, visibility, or Three.js direction validation;
- independent Astropy fixtures, angular comparisons, error budgets, tolerances, or
  scientific release evidence.

Do not trigger it for:

- raw catalogue acquisition, parsing, checksums, schemas, or deterministic artifacts
  without coordinate transformation; use `ufuq-catalogue-provenance`;
- Qibla inverse geodesics or destination-coordinate approval; use
  `ufuq-qibla-geodesy`;
- cultural pattern names, membership, or routes; use `ufuq-najdi-arabian-sky`;
- visual scene layout that makes no astronomical correctness claim.

## Required project files

Read `AGENTS.md`, `docs/ASTRONOMY_SPEC.md`, `docs/DATA_STRATEGY.md`,
`docs/IMPLEMENTATION_DECISIONS.md`, `docs/TEST_PLAN.md`,
`docs/adr/003-astronomical-coordinate-conventions.md`, and
`docs/adr/007-testing-and-validation.md`. Read
`docs/references/UFUQ_SOURCE_REGISTER.md`,
`docs/references/SOURCE_GAPS.md`,
`docs/references/syntheses/astronomy-model-synthesis.md`, and this skill's four
reference files. Open the astronomy study dossiers linked by
`references/traceability.md` for the affected rule. When present, inspect the selected
catalogue manifest/`ReadMe`, oracle environment manifest, fixture schema, fixture
metadata, and comparison tests.

## Source authority order

1. Applicable IAU SOFA algorithms and release documentation.
2. Official IERS TN36 baseline plus separately pinned corrections/data.
3. Approved catalogue metadata for frame, epoch, units, and field semantics.
4. Pinned official Astropy, PyERFA, and `astropy-iers-data` documentation/runtime for
   the independent oracle.
5. Independently produced fixtures and measured production disagreement.
6. *Explanatory Supplement* and *Fundamental Astronomy* as explanatory support.
7. UFUQ project decisions for selected scope and behavior.

No lower authority may erase a contradiction with a higher authority. Project decisions
must record any deliberate approximation.

## Mandatory workflow

1. Define the claim and record, without defaults:
   - input and output coordinate frames;
   - catalogue reference epoch;
   - observation instant and time scale;
   - observer latitude, east-positive longitude, datum, and height;
   - units and angle conventions;
   - proper-motion and other space-motion policy;
   - atmospheric-refraction/horizon/visibility policy;
   - IERS data source, version/hash, network/cache/extrapolation state.
2. State supported date/location/altitude ranges and singular/invalid cases.
3. Trace each transformation step to its authority and version. Record omitted effects
   with a quantified bound; never label an omission “negligible” without evidence.
4. Pin the Python/Astropy oracle environment and neutral fixture schema. Audit that the
   oracle imports no production UFUQ package and does not mechanically translate the
   TypeScript implementation.
5. Generate or review fixtures independently. Each fixture records inputs, policies,
   software/data versions, provenance, expected outputs, and intended comparison.
6. Compare production and reference outputs using robust angular separation or the
   applicable circular metric. Report component and great-circle differences.
7. Build the error budget. Derive the test threshold from measured disagreement,
   independent uncertainty, and approved scope; never invent a convenient tolerance.
8. Partition cases across meridian/east/west, wrap, time boundaries, horizon,
   zenith/singularity, reference epoch, motion, supported-range endpoints, and approved
   Malaysian scenarios.
9. Confirm every mandatory conclusion has a basis in
   `references/traceability.md`, then report with `references/output-template.md`. A
   plausible sky image is not evidence.

## Required evidence

- Versioned algorithm/data/policy manifest and fixture-schema version.
- Independent fixture provenance and code-sharing/import audit.
- Exact inputs/outputs with units and convention labels.
- Per-case angular differences and error-budget components.
- Measured tolerance rationale and failures, not only averages.
- Explicit offline/out-of-range/missing-IERS behavior.

## Stop conditions

Stop the affected claim when any required frame, epoch, time scale, datum/height, units,
motion policy, refraction policy, IERS provenance, supported range, or tolerance is
missing. Also stop when the oracle is unpinned, imports production code, shares the same
implementation, or cannot reproduce a fixture offline under the approved policy.

## Prohibited assumptions

Do not invent coordinates, epochs, time scales, EOP values, leap-second handling,
refraction constants, visibility rules, or tolerances. Do not treat Polaris as True
North. Do not use the internal Three.js axis-mapping fixture as an independent astronomy
oracle.

## Required output

Use `references/output-template.md`. Distinguish `SOURCE_SUPPORTED_FACT`,
`PROJECT_DECISION`, `PROVISIONAL_CHOICE`, and `UNRESOLVED_QUESTION`. State the exact
claim that passes or remains blocked; do not generalize beyond the tested range.

## Relevant validation commands

Use only commands that exist in the repository:

```text
npm run check
npm run boundaries
npm run test:reference
```

`test:reference` becomes mandatory when Phase 1 introduces the first
production/reference comparison; before activation, its empty invocation must fail.
Run the pinned oracle command from its committed environment instructions once those
instructions exist. Use targeted import scans to prove
`tools/astronomy-reference` does not import production packages.
