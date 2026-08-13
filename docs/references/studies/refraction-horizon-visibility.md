# Refraction, horizon, and visibility evidence dossier

## Scope and authority

- Milestone: 2C.4.
- Governing question: AST-004.
- Primary algorithm authority: IAU SOFA issue `2023-10-11`, especially
  `iauRefco`, `iauAtioq`, and `iauHd2ae`.
- Independent-reference documentation: official Astropy `8.0.1` `AltAz`
  documentation retrieved on 2026-08-03.
- This dossier records source behaviour and authority limits. The separately tracked
  UFUQ project decision now normatively excludes refraction and aggregate visibility
  from V1 and fixes geometric-state separation; this dossier does not approve an
  atmosphere, refraction model/range, physical/terrain horizon, visibility component
  rule, model-specific warning disposition, or tolerance for a later profile.

## Pinned official documentation

| Source | Exact documentation | Authority use |
|---|---|---|
| `SOFA-2023-10-11` | IAU SOFA ANSI C issue `2023-10-11`, release/manual routine documentation for `iauRefco`, `iauAtioq`, and `iauHd2ae`; official release index: <https://www.iausofa.org/current-software> | Production-route algorithm semantics and routine inputs; not UFUQ policy. |
| `ASTROPY-DOCS-PIN` | Astropy `8.0.1`, [`AltAz`](https://docs.astropy.org/en/stable/api/astropy.coordinates.AltAz.html), official stable page as displayed on 2026-08-03 | Independent-reference frame/input/default/limitation behaviour; not production policy. |

## Source-supported facts

| Conclusion | Classification | Consequence |
|---|---|---|
| `iauRefco` computes coefficients for the compact model `dZ = A tan(Z) + B tan^3(Z)`, using pressure in hPa, temperature in degrees Celsius, relative humidity in `[0,1]`, and wavelength in micrometres. | `SOURCE_SUPPORTED_FACT` | A SOFA-family refracted fixture must record all four inputs, units, routine issue, and coefficients. |
| `iauAtioq` consumes refraction coefficients and contains a low-altitude numerical guard. | `SOURCE_SUPPORTED_FACT` | The guard is implementation behaviour, not evidence that the result is scientifically valid near or below the horizon. |
| `iauHd2ae` is a rotational horizon-coordinate conversion and contains no terrain, obstruction, extinction, photometric, or learner-eligibility model. | `SOURCE_SUPPORTED_FACT` | A SOFA horizontal direction cannot be labelled terrain-visible or learner-visible. |
| Astropy `AltAz` applies refraction when pressure is nonzero and documents pressure `0` as disabling refraction. Its documented library defaults are pressure `0 hPa`, temperature `0 deg C`, relative humidity `0`, and wavelength `1 micron`. | `SOURCE_SUPPORTED_FACT` | These are reference-library defaults only. They do not select UFUQ defaults or make a default-atmosphere claim. |
| Astropy documents its ERFA-based model as inaccurate below about 5 degrees and warns that near/below altitude 0 degrees results or round trips can become meaningless or highly discrepant. | `SOURCE_SUPPORTED_FACT` | About 5 degrees is an experiment partition and warning boundary from the reference documentation, not an approved UFUQ validity threshold or tolerance. |
| Neither SOFA nor Astropy defines UFUQ's physical-dip/terrain horizon, photometric visibility, daylight/twilight, atmospheric extinction/transparency, cloud/weather, light pollution, screen visibility, or learner-facing eligibility. | `SOURCE_SUPPORTED_FACT` | These states require separate project policy and evidence. |

## UFUQ semantic boundary

| Conclusion | Classification | Status |
|---|---|---|
| Keep `GeometricHorizontalDirection` and `RefractedHorizontalDirection` distinct; refraction never mutates or relabels the geometric state. | `PROJECT_DECISION` | Normative typed separation for V1; later refraction remains a separate reviewed stage. |
| Use geometric altitude only for the first vertical slice and prohibit scene adapters from applying refraction. | `PROJECT_DECISION` | Normative V1 exclusion; upstream route/time/EOP blockers remain separate. |
| Do not approve a default atmosphere. V1 requests no refraction and reaches `REFRACTION_NOT_REQUESTED`; a later requested refracted result with missing required meteorology returns `REFRACTION_UNAVAILABLE` rather than using Astropy or SOFA convenience defaults. | `PROJECT_DECISION` | Normative no-default and state-separation rule; later model/input/domain approval remains open. |
| Treat below-geometric-horizon as a non-terminal classification attached to an approved geometric direction, not an astronomy failure, apparent-horizon result, or visibility decision. | `PROJECT_DECISION` | Preserve signed altitude, defined azimuth/singularity, direction, scientific provenance, warnings, and statuses; exact equality/tolerance and learner/render consequences remain open. |
| Geometric horizon means the astronomical local horizontal plane at geometric altitude zero before refraction. Keep it distinct from a model-dependent refracted-apparent-altitude-zero state, physical sea/Earth-curvature/observer-height dip, terrain/buildings, renderer clipping, and learner cues. | `PROJECT_DECISION` | `RefractedApparentHorizonState` means only apparent altitude zero under a named approved model/policy; no physical-dip, terrain, or learner policy is selected. |
| Keep astronomical horizon, photometric/variability, Sun-altitude/daylight/twilight, atmospheric-extinction/transparency, cloud/weather, terrain/obstruction, light-pollution, screen, and learner-eligibility states as nine independent visibility components. | `PROJECT_DECISION` | No component promotes another and no aggregate visible/not-visible boolean is approved. |
| Keep refraction-not-requested, requested-but-unavailable, supplied-input-invalid, outside-reviewed-domain, valid-input-with-model-warning, and approved-result states distinct. | `PROJECT_DECISION` | No default atmosphere is supplied. Warning-bearing and approved refracted results remain unreachable until their full approval gates close. |

## Authority and approval gaps

| Gap | Classification | Required closure |
|---|---|---|
| Exact accepted pressure, temperature, wavelength, observer-height, lapse-model, and altitude ranges. | `AUTHORITY_OR_EVIDENCE_MISSING` | Select a model/domain authority, quantify behavior, and obtain AST-004/AST-006 approval. Relative humidity's SOFA routine interval does not settle the other project ranges. |
| Whether measured or derived meteorology is acceptable, including measurement location/time, uncertainty, height transfer, and lapse assumptions. | `HUMAN_REVIEW_REQUIRED` | Approve provenance and uncertainty requirements. |
| Near-horizon and below-horizon validity, extrapolation, warnings, and any apparent-horizon definition. | `HUMAN_REVIEW_REQUIRED` | Review experiment evidence and approve a model-specific domain and warning contract. |
| Terrain/dip, extinction, transparency, light pollution, daylight/twilight, magnitude/variability, and learner eligibility. | `AUTHORITY_OR_EVIDENCE_MISSING` | Supply primary authority or explicitly bounded project policy, then obtain domain/education review. |
| Exact later-refraction warning allowlist and wire/HTTP serialization. | `HUMAN_REVIEW_REQUIRED` | Core scientific precedence and warning preservation are normative; approve model-specific warning disposition before enabling refraction and map transport separately. |
| Reachability of an approved or warning-bearing refracted result. | `HUMAN_REVIEW_REQUIRED` | Requires exact model/version, complete meteorology/provenance, reviewed model and combined operating domains, warning policy/allowlist, quantitative bound, scientific tolerance, and named astronomy-review approval. |

## Required experiments

Each family is `EXPERIMENT_REQUIRED`; experiment output may measure consequences but
cannot create source authority or approve a threshold.

1. Compare named refraction models under identical explicit inputs and retain each
   model/version, status, and domain claim.
2. Sweep pressure, temperature, humidity, and wavelength independently and jointly,
   retaining uncertainty assumptions.
3. Probe numerical sensitivity above, around, and below the documented Astropy
   about-5-degree region and around zero altitude.
4. Compare geometric and apparent horizon crossings without treating either as a
   terrain horizon.
5. Exercise below-horizon inputs and verify that numerical guards do not become
   validity approval.
6. Compare explicit atmosphere inputs, library defaults, pressure-zero geometric
   operation, and missing-input rejection to quantify default-atmosphere consequences.
7. Prove visibility-policy separation by varying astronomical horizon, photometry/
   variability, Sun altitude/daylight/twilight, extinction/transparency, cloud/weather,
   terrain/obstruction, light pollution, screen, and learner states independently.

## Independent-reference fixture requirements

Every geometric/refraction fixture must retain the synthetic source, observation and
observer/EOP/leap provenance, geometric direction, model/routine/version, pressure,
temperature, humidity, wavelength, measurement time/location, input uncertainty,
measured-versus-derived status, any height/lapse model, validity-domain result,
warnings, refracted result or explicit non-result, every horizon/visibility component,
offline configuration, artifact hashes, and deterministic replay hash. Library
defaults must be disabled or recorded explicitly. Fixtures must include geometric
identity, controlled nonzero refraction, meteorology partitions, near-horizon,
zero-altitude, below-horizon, invalid-input, missing-input, and multi-fault precedence
cases.
