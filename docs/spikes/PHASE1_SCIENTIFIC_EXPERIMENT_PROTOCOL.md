# Phase 1 Milestone 2C.5A: Scientific Experiment Protocol

## Status and scope

This document freezes the review protocol for the scientific experiments proposed by
Milestones 2C.1–2C.4. It does not run an experiment, create a source-derived fixture,
select production astronomy, approve a scientific model or data product, or establish
a numerical tolerance.

The registry distinguishes whether an experiment can execute now from whether its
output can close a scientific decision. A synthetic measurement can be executable
while the source interpretation, production policy, supported domain, error budget,
and reviewer approval remain blocked.

The following constraints are normative for Milestone 2C.5A:

- only explicitly labelled synthetic inputs and the locked astronomy-reference
  environment may be used by a currently runnable experiment;
- no I/311 row, source-derived normalized value, production-generated direction, or
  unapproved production EOP/leap/refraction policy may enter a runnable-now fixture;
- Astropy and PyERFA are code-independent from future UFUQ TypeScript production code,
  but Astropy's coordinate path uses ERFA and direct PyERFA calls expose the same
  ERFA/SOFA algorithm family. Agreement between them is not algorithmically
  independent scientific validation;
- a library default, warning, numerical guard, packaged data file, or successful
  calculation remains library behaviour unless a separate UFUQ decision approves it;
- an experiment result cannot create catalogue authority, production approval, a
  supported operating domain, an omission bound, a degraded mode, or a tolerance; and
- `test:reference` remains inactive until a production/reference comparison exists.
  Synthetic experiment runners belong to the non-production Python reference tool and
  do not activate that suite by themselves.

Milestone 2C remains open.

## Execution classifications

Every experiment has exactly one current execution classification:

| Classification | Meaning |
|---|---|
| `RUNNABLE_SYNTHETIC_NOW` | The stated bounded question can execute using explicit synthetic inputs, the locked reference environment, and no unapproved production policy. Its result remains measurement, invariant, or library-behaviour evidence only. |
| `BLOCKED_BY_SOURCE_AUTHORITY` | The experiment inherently needs source-derived data or a source semantic that the applicable authority does not establish. |
| `BLOCKED_BY_PROJECT_DECISION` | The experiment cannot be instantiated without choosing an unapproved model, policy, range, endpoint, or degradation definition. |
| `BLOCKED_BY_REVIEW` | Inputs and protocol exist, but the run itself requires a named reviewer decision that has not occurred. This is distinct from review required to promote a runnable result. |
| `BLOCKED_BY_REQUIRED_DATA` | The protocol is defined, but a required pinned external artifact, independent model implementation, or ephemeris is unavailable. |
| `DEFERRED_TO_PRODUCTION_IMPLEMENTATION` | The scientific question requires the future production implementation or a production-generated result that 2C.5A is not authorized to create. |

When more than one blocker applies, the registry records every blocker and applies this
deterministic rule: a question that explicitly compares production is
`DEFERRED_TO_PRODUCTION_IMPLEMENTATION`; otherwise choose the first applicable class in
the order source authority, project decision, required data, and run approval. If none
applies, the record is `RUNNABLE_SYNTHETIC_NOW`.

No current family is classified `BLOCKED_BY_SOURCE_AUTHORITY` because every runnable
epoch/motion protocol is explicitly synthetic and excludes I/311 values. Adding an
I/311 row or claiming I/311 truth would create a separate source-derived execution and
immediately invoke that blocker. No current family is `BLOCKED_BY_REVIEW` merely to
record synthetic measurements; reviewer approval is instead required before those
measurements inform a production decision.

## Required record for every experiment

The human record below and the machine registry jointly retain all required fields.
Every future fixture and result must also conform to the versioned schemas named in the
registry.

1. Stable experiment ID and title.
2. Scientific question.
3. What the experiment may establish.
4. What it explicitly cannot establish.
5. Input class: `SYNTHETIC`, `SOURCE_DERIVED`, `PRODUCTION_GENERATED`, or
   `EXTERNAL_AUTHORITATIVE_ARTIFACT`.
6. Required model, library, routine, and pinned version.
7. Required time scales, frames, units, and coordinate conventions.
8. Required EOP, leap-second, meteorological, observer, and ephemeris inputs.
9. Parameter partitions and boundary cases.
10. Independent comparison path and shared-lineage declaration.
11. Metrics selected from great-circle angular separation, wrapped azimuth
    difference, altitude difference, component residuals, warnings, structured
    statuses, deterministic bytes, and deterministic hashes.
12. Repetition and determinism requirements.
13. Software, source, fixture, and artifact hashes.
14. Expected output schema.
15. Pass/fail basis without an invented numerical threshold.
16. Reviewer approval required to use the result in a later decision.
17. Follow-up decision the result may inform.

### Shared execution requirements

Unless a row is stricter, every runnable experiment uses:

- CPython `3.14.6`, Astropy `8.0.1`, PyERFA `2.0.1.5`/ERFA `2.0.1`/SOFA
  `20231011`, `astropy-iers-data 0.2026.7.20.15.31.18`, and the exact hashes in
  `tools/astronomy-reference/environment-manifest.json`;
- explicit frames, epoch representation and scale, two-part Julian Dates where the
  routine requires them, units, longitude/azimuth sign, observer semantics, and
  refraction state in every fixture rather than inherited defaults;
- network disabled, automatic downloads disabled, fresh isolated cache state, and no
  production-package import;
- at least two executions from the same canonical fixture with byte-identical
  canonical results and matching SHA-256 hashes; any experiment claiming isolated
  replay additionally repeats in a fresh synchronized environment;
- explicit hashes for the protocol document, registry, registry schema, fixture
  schema, result schema, environment manifest, lockfile, canonical fixture bytes,
  every consumed external artifact, and every runner source file;
- `ufuq.astronomy-experiment-result.v1` as the result envelope, including an embedded
  execution manifest, runtime/operating-system context, argv/runner identity,
  measurements, warnings/statuses, execution outcome, checks, and decision limits;
  and
- `MEASURED_NO_ACCEPTANCE` for numerical observations until AST-006 supplies an error
  budget and approved threshold. `PASS`/`FAIL` is permitted only for an exact
  source- or project-supported invariant such as status preservation, prohibited
  default insertion, stable serialization, or a deliberately injected cosine fault
  being detected. Floating-point equality is not assumed to be exact unless the
  invariant is explicitly byte identity.

Every v1 fixture is machine-labelled `SYNTHETIC_EXPERIMENT_INPUT` and affirmatively
records that I/311 rows, HIP-derived fixture values, catalogue source bytes,
production-generated values, and an I/311 epoch-resolution claim are absent. Its
experiment-specific `inputs` extension point accepts only closed records with explicit
synthetic provenance, unit, frame, time scale, and coordinate convention. A new input
shape or source/production class requires a reviewed successor schema; changing a
label in a v1 file cannot authorize it.

Every input also declares `VALID_VALUE`, `DELIBERATELY_INVALID_TOKEN`, or
`DELIBERATELY_MISSING`. Missing inputs use the explicit `MISSING` sentinel; they are
never represented by an absent required field or `null`. Non-finite strings may appear
only as deliberately invalid tokens for rejection cases, never as valid numerical
values.

The result distinguishes `COMPLETED`, `BLOCKED`, `SKIPPED`, and `EXECUTION_ERROR`
execution outcomes. A non-completed execution carries at least one structured reason,
no measurements, and only `NOT_RUN` checks. A completed exact invariant may be
`PASS`/`FAIL`; a completed numerical check is always `MEASURED_NO_ACCEPTANCE`.
Execution `BLOCKED` is a run-level outcome and does not replace or weaken the
registry's pre-execution classification.

`fixtureId` is the exact concatenation `experimentId:caseId`. The same three values in
the result and embedded execution manifest must match the fixture; a runner rejects a
mismatch before execution. Schema v1 accepts no JSON `null` except the required
`numericalThreshold: null`, whose explicit meaning is “numerical acceptance prohibited
in this schema,” not unknown or omitted.

PyERFA is installed and version-pinned transitively in the locked environment, but the
current smoke executable does not import it. Before a 2C.5B body uses direct `erfa`
routines, that milestone must promote PyERFA to a direct reference-tool dependency and
update the lock/dependency evidence and import tests. This is a required mechanical
runner change, not permission to select production astronomy and not a missing
scientific input for the runnable classifications.

All runnable results require the owning AST-003, AST-004, AST-006, or AST-007 reviewer
before they may change production policy. Merely recording a measurement requires no
such promotion approval.

## Complete experiment classification

| ID | Title | Current classification | Runnable or blocked scope |
|---|---|---|---|
| `2C.1-EXP-01` | Julian TT/TDB/UTC epoch-label sensitivity | `RUNNABLE_SYNTHETIC_NOW` | Measure explicitly labelled synthetic start-instant and propagated-direction differences only. I/311 meaning remains excluded. |
| `2C.1-EXP-02` | Calendar decimal-year comparison | `RUNNABLE_SYNTHETIC_NOW` | Measure `decimalyear` versus Julian-epoch consequences under synthetic motion; it cannot make calendar decimal year an I/311 candidate. |
| `2C.1-EXP-03` | Besselian rejection guard | `RUNNABLE_SYNTHETIC_NOW` | Verify `byear` stays an explicit rejected interpretation and measure its diagnostic difference without promoting it. |
| `2C.2-EXP-01` | Componentized-route equivalence | `RUNNABLE_SYNTHETIC_NOW` | Same-family PyERFA/ERFA consistency only; no independent scientific validation or production-route approval. |
| `2C.2-EXP-02` | Independent-reference disagreement | `DEFERRED_TO_PRODUCTION_IMPLEMENTATION` | Requires future production TypeScript stage outputs and a production-import audit. |
| `2C.2-EXP-03` | Effect ablation and interaction | `RUNNABLE_SYNTHETIC_NOW` | Controlled same-family measurements with explicit synthetic inputs; no effect inclusion, omission bound, or aggregate error budget follows. |
| `2C.2-EXP-04` | Epoch and motion boundary | `RUNNABLE_SYNTHETIC_NOW` | Synthetic scale, target-epoch, cosine-fault, pole-guard, JD-split, and warning probes only; source-derived propagation remains blocked. |
| `2C.2-EXP-05` | Earth-orientation and range sensitivity | `BLOCKED_BY_PROJECT_DECISION` | Requires a candidate EOP/leap product policy, field-quality disposition, degradation definition, and proposed date endpoints. |
| `2C.2-EXP-06` | Observer, parallax, and velocity sensitivity | `RUNNABLE_SYNTHETIC_NOW` | Measure explicit synthetic branches without selecting observer, parallax, RV, or omission policy. |
| `2C.2-EXP-07` | Solar and optional multi-body deflection | `BLOCKED_BY_PROJECT_DECISION` | The complete family needs a selected additional-body scope followed by a separately pinned multi-body model/ephemeris and body inputs. Solar-only ablation remains a bounded partition of `2C.2-EXP-03`. |
| `2C.2-EXP-08` | Refraction validity boundary | `BLOCKED_BY_PROJECT_DECISION` | A validity floor/domain and candidate refraction policy do not exist; library limitation prose cannot supply them. |
| `2C.3-EXP-01` | Offline deterministic reconstruction | `RUNNABLE_SYNTHETIC_NOW` | Reconstruct the explicitly synthetic smoke bundle and protocol artifacts only; this does not approve production EOP/leap data. |
| `2C.3-EXP-02` | EOP state partitions | `RUNNABLE_SYNTHETIC_NOW` | Exercise synthetic orthogonal status records and exact no-promotion/no-substitution invariants without calculating approved astronomy. |
| `2C.3-EXP-03` | EOP degradation sensitivity | `BLOCKED_BY_PROJECT_DECISION` | “Stale,” prediction acceptance, degradation modes, candidate domain, and field perturbation policy are not defined. |
| `2C.3-EXP-04` | Leap and timestamp boundaries | `RUNNABLE_SYNTHETIC_NOW` | Probe locked reference-library syntax/conversion/status behaviour against the smoke-only leap artifact; no production UTC or leap policy follows. |
| `2C.3-EXP-05` | Observer partitions | `RUNNABLE_SYNTHETIC_NOW` | Exercise structural/source-defined input guards, convention invariants, and provenance retention with explicit synthetic observers; no supported observer domain follows. |
| `2C.3-EXP-06` | Operating-domain endpoints and outcome precedence | `BLOCKED_BY_PROJECT_DECISION` | Numerical endpoints, inclusion rules, future horizon, and observer range are absent. Precedence-only synthetic checks belong to runnable state-preservation experiments. |
| `2C.4-EXP-01` | Refraction-model comparison | `BLOCKED_BY_REQUIRED_DATA` | A second named, primary-authority model and independently pinned implementation/data path have not been selected and recorded. |
| `2C.4-EXP-02` | Meteorology sensitivity | `RUNNABLE_SYNTHETIC_NOW` | Measure the pinned SOFA-family model under explicit synthetic inputs; no accepted meteorological range or default follows. |
| `2C.4-EXP-03` | Near-horizon numerical sensitivity | `RUNNABLE_SYNTHETIC_NOW` | Measure reference-library behaviour and warnings around documented partitions; no UFUQ validity boundary follows. |
| `2C.4-EXP-04` | Geometric versus model-apparent horizon | `RUNNABLE_SYNTHETIC_NOW` | Locate a named reference-model apparent-altitude-zero crossing while retaining geometric state; it is not an approved `RefractedApparentHorizonState`. |
| `2C.4-EXP-05` | Below-horizon behaviour | `RUNNABLE_SYNTHETIC_NOW` | Probe library guards and exact non-erasure/status-preservation invariants; no below-horizon refraction approval follows. |
| `2C.4-EXP-06` | Default-atmosphere consequences | `RUNNABLE_SYNTHETIC_NOW` | Compare explicit library inputs/defaults and verify UFUQ protocol never inserts them; no atmosphere default is approved. |
| `2C.4-EXP-07` | Visibility-policy separation | `RUNNABLE_SYNTHETIC_NOW` | Exercise structural independence of nine synthetic component states; no scientific visibility or learner rule follows. |

## Experiment records

The records below add the experiment-specific information to the shared requirements.
`None` for an artifact means the fixture must explicitly declare it not required; it
does not permit a library default.

### Milestone 2C.1

| ID | Question; may establish; cannot establish | Inputs, dependencies, and conventions | Partitions, comparison, metrics, approval, and follow-up |
|---|---|---|---|
| `2C.1-EXP-01` | Does assigning TT, TDB, or UTC to the same synthetic Julian epoch label change the represented instant and propagated direction? May measure scale sensitivity and warning/status differences. Cannot identify the I/311 time scale, approve TT, or set a tolerance. | `SYNTHETIC` astrometry plus the smoke-only leap artifact; Astropy `Time`/`apply_space_motion` and PyERFA `pmsafe`; ICRS, explicit `jyear` scale, conversion to two-part TDB JD, mas/Julian-year, explicit parallax/RV. No EOP, observer, meteorology, or ephemeris. | Zero/high motion, high declination, parallax/RV branches, short/long synthetic intervals, alternative JD splits. Astropy high-level versus direct PyERFA has shared ERFA lineage. Use time/component/angular/status metrics. AST-003/006 review may use measurements to bound alternatives, never to establish source meaning. |
| `2C.1-EXP-02` | How does calendar `decimalyear` differ from the source-supported Julian representation under otherwise identical synthetic motion? May measure instant and direction deltas. Cannot make `decimalyear` source-supported. | `SYNTHETIC`; Astropy `TimeDecimalYear`, `TimeJulianEpoch`, and space motion with the same explicit conventions and smoke-only leap data when a UTC conversion is exercised. | Leap/non-leap calendar partitions, zero/high motion, identical target instants. Comparison shares Astropy/ERFA lineage; report time, angular, component, warning, byte, and hash metrics. AST-003 review may reject or bound this alternative. |
| `2C.1-EXP-03` | Does the protocol prevent Besselian `byear` from being treated as an I/311 candidate? May establish an exact registry/fixture rejection invariant and measure diagnostic differences. Cannot infer catalogue intent from numerical distance. | `SYNTHETIC`; Astropy `TimeBesselianEpoch` and `TimeJulianEpoch`; explicit TT label for the diagnostic only. No EOP, observer, meteorology, or ephemeris. | Ordinary/high-motion partitions and a deliberately mislabelled fixture. Exact check: the candidate set rejects `byear`; numerical outputs are measurement-only. AST-003 review may use the guard when approving an epoch adapter. |

### Milestone 2C.2

| ID | Question; may establish; cannot establish | Inputs, dependencies, and conventions | Partitions, comparison, metrics, approval, and follow-up |
|---|---|---|---|
| `2C.2-EXP-01` | Are decomposed `pmsafe` + `apco13`/`atciq` + `atioq` results internally consistent with composed `atco13` for identical explicit synthetic inputs? May detect wiring, unit, convention, status, and intermediate-state faults. Cannot provide independent science validation or approve the route. | `SYNTHETIC` ICRS astrometry, explicit UTC/TT/UT1, synthetic `dut1`,`xp`,`yp`, WGS84 candidate observer, pressure-zero atmosphere, smoke-only leap artifact; direct PyERFA routines from the pinned environment. | Cardinal/wrap/meridian/east/west/horizon/zenith, nonzero EOP, alternative JD splits, motion branches. `SAME_FAMILY`; report great-circle, wrapped azimuth, altitude, component, warning/status, bytes/hashes. AST-003/006 review may identify stage ownership and defects. |
| `2C.2-EXP-02` | How does future production disagree with the independent Astropy reference path? May measure implementation disagreement and warning/status mismatches. Cannot exist before production, make Astropy production code, or set acceptance. | `PRODUCTION_GENERATED` plus matched synthetic or later approved source/reference fixtures; future TypeScript route and Astropy `SkyCoord`/`CIRS`/`AltAz`; every time/frame/EOP/observer/motion/refraction input explicit. | All approved scientific and boundary partitions. Code-independent pseudo-oracle comparison, with shared SOFA-model lineage recorded where applicable. Angular/component/status/hash metrics. AST-003/006 approval and the first production comparison activate `test:reference`. |
| `2C.2-EXP-03` | What changes when each candidate effect and selected interactions are toggled in controlled SOFA-family probes? May measure local sensitivities and detect double application. Cannot approve inclusion/omission or sum one-at-a-time deltas into a total bound. | `SYNTHETIC`; direct PyERFA routines for motion, parallax/RV, BPN, aberration, solar deflection, EOP terms, diurnal aberration, and refraction; explicit model/time/frame/unit inputs and synthetic EOP/metrology where exercised. | Zero/nonzero, sign/order faults, pairwise and risk-selected interactions, direction/time/observer partitions. No independent comparison; same-family measurements only. AST-003/004/006 may use results to prioritize deeper evidence and define later candidate bounds. |
| `2C.2-EXP-04` | Do epoch/target boundaries, starred-alpha conversion, pole guards, JD splits, and warning propagation behave as declared for synthetic astrometry? May establish exact omitted/double-cosine fault-detection and status-preservation invariants plus measurements. Cannot authorize I/311 propagation. | `SYNTHETIC`; the three 2C.1 epoch protocols, PyERFA `pmsafe`, explicit ICRS/JD/TDB/mas-per-Julian-year conventions, synthetic parallax/RV. | Source-label candidates, candidate J2000.0 target, target-to-observation split, high declination, near pole, alternative JD splits, warning-producing cases. Shared-lineage only; component/angular/status/hash metrics. AST-003 review may approve adapter guards after source policy exists. |
| `2C.2-EXP-05` | What is the sensitivity to EOP field quality/availability, corrections, and candidate range endpoints? It could later bound EOP policy choices. It cannot run honestly before those candidate choices exist or turn a product horizon into UFUQ support. | Would require `EXTERNAL_AUTHORITATIVE_ARTIFACT` EOP/leap bundles, per-field quality/provenance/approval, a candidate CPO route, and proposed endpoints. | Blocked by product/field precedence/interpolation, quality approval, stale/degraded definitions, and supported endpoints. Later comparison must include per-field/interactions and exact statuses. AST-003/006/007 review owns follow-up. |
| `2C.2-EXP-06` | How sensitive are results to observer position, parallax, and radial velocity, and can double topocentric/diurnal effects be detected? May measure controlled synthetic branches. Cannot select a distance/RV/observer policy or omission bound. | `SYNTHETIC`; direct PyERFA/Astropy candidate routines with explicit ICRS, distance/parallax, RV, geodetic observer, time, and EOP values. No source rows. | Geocentre/site/height, positive/zero/negative parallax, missing/zero/nonzero/high RV, equatorial/high-latitude candidate observers, single/double-application faults. Shared lineage; angular/component/status metrics. AST-003/006 review may bound policy alternatives. |
| `2C.2-EXP-07` | Is solar-only deflection adequate over a proposed domain, or are named additional bodies required? May eventually measure solar and multi-body differences. Cannot run the complete question before the additional-body scope is selected and its model/ephemeris is pinned. | `SYNTHETIC` directions plus `EXTERNAL_AUTHORITATIVE_ARTIFACT` ephemerides/body constants; SOFA `ldsun` and candidate `ldn`/`atciqn` family. The scope and required external path are not selected. | Elongation sweep, dates, bodies, interaction with aberration. Solar-only diagnostics may run under `2C.2-EXP-03`, but this ID remains blocked. AST-003 must first select solar-only or additional-body scope; AST-006 review follows later measurements. |
| `2C.2-EXP-08` | Where is a proposed refraction route scientifically valid and what warning/non-result boundary should apply? May later test an approved candidate domain. Cannot derive a validity floor from SOFA/Astropy prose or a guard. | Would require a selected model/version, approved atmosphere provenance/ranges, candidate altitude domain, observer policy, and explicit meteorology. | Pressure-zero identity, controlled nonzero atmosphere, documented 5-degree partition, zero/below horizon, invalid/unavailable inputs. Blocked by AST-004/006 project decisions; later results inform model/domain/warnings only. |

### Milestone 2C.3

| ID | Question; may establish; cannot establish | Inputs, dependencies, and conventions | Partitions, comparison, metrics, approval, and follow-up |
|---|---|---|---|
| `2C.3-EXP-01` | Can a named synthetic EOP/leap bundle, fixtures, warnings, and results be reconstructed offline byte-for-byte? May establish deterministic protocol and artifact replay. Cannot approve the packaged smoke files for production or prove an air-gapped rebuild without package artifacts. | `SYNTHETIC` plus the pinned `EXTERNAL_AUTHORITATIVE_ARTIFACT` files in the environment manifest; locked Python/Astropy tool; explicit network/cache policy. | Two local repetitions and a fresh isolated synchronized environment; artifact-present/hash-mismatch/missing negative cases. Compare canonical bytes/hashes and statuses exactly. ADR-007 review may approve the replay mechanism, not science data. |
| `2C.3-EXP-02` | Does every EOP field retain independent source quality, availability, provenance, coverage, and approval without substitution or promotion? May establish exact structural/status invariants. Cannot approve any quality or calculate accepted astronomy. | `SYNTHETIC` status fixtures only; no numeric EOP value is needed for the invariant. Fields are independently labelled `UT1-UTC`,`xp`,`yp`,`dX`,`dY`. | Mixed qualities, missing/blank/stale/out-of-range/hash mismatch, one-field changes, zero/nearest fault injection. Structural comparison independent of ERFA; exact status and canonical hash checks. AST-003/007 review may approve a future state schema. |
| `2C.3-EXP-03` | What are the consequences of named degraded EOP modes over a proposed domain? May later quantify candidate degradation. Cannot define “stale,” prediction acceptance, zero fill, or a domain by inventing inputs. | Would require a project-selected product, per-field modes, freshness rule, candidate range, observer cases, and approved perturbation partitions. | Field-by-field and interaction measurements across candidate endpoints; blocked until AST-003/007 define the modes. AST-006 later evaluates quantitative bounds. |
| `2C.3-EXP-04` | Does the locked reference path preserve syntax, leap validation, UTC/TAI/TT/UT1 values, warnings, and errors at timestamp boundaries? May establish reference-library and protocol status behaviour. Cannot select production grammar, precision, artifact, expiry, or date range. | `SYNTHETIC` timestamp strings plus the smoke-only pinned leap artifact; Astropy `Time`/`LeapSeconds` and PyERFA `dtf2d`/time conversions. | Valid/invalid second 60, adjacent instants, fractions, malformed dates/offsets, `-00:00`, artifact missing/expired simulations. Shared ERFA lineage; time component/status/byte/hash metrics. AST-003/007 review may approve later grammar/status mapping. |
| `2C.3-EXP-05` | Do structural observer guards, sign conventions, equivalent longitudes, singularity states, and provenance fields behave explicitly? May establish exact input/convention invariants and reference-library behaviour. Cannot approve WGS84, normalization, poles, locations, or height ranges. | `SYNTHETIC` observers; Astropy `EarthLocation` and PyERFA `eform`/`gd2gc`; explicit candidate datum, geodetic latitude, east-positive longitude, ellipsoidal-height label. | Latitude endpoints/outside, equivalent longitudes, poles, zenith/nadir, varied synthetic heights, orthometric-label/non-finite rejection, provenance retention. Shared library lineage; status/component/hash metrics. AST-003/007 review may select a domain later. |
| `2C.3-EXP-06` | Do exact supported-domain endpoints and multi-fault precedence produce the approved outcomes? May later establish endpoint/precedence conformance. Cannot run without numerical endpoints, inclusion rules, interpolation neighbours, and future/observer limits. | Would use synthetic astrometry against approved EOP/leap/model/observer/tolerance domain artifacts and outcome mapping; no catalogue row is required. | Each endpoint, smallest representable outside neighbour, future horizon, location/height boundaries, and multi-fault combinations. Blocked by AST-003/006/007 project decisions. |

### Milestone 2C.4

| ID | Question; may establish; cannot establish | Inputs, dependencies, and conventions | Partitions, comparison, metrics, approval, and follow-up |
|---|---|---|---|
| `2C.4-EXP-01` | How do independently specified primary-authority refraction models disagree under identical inputs? May later measure model disagreement. Cannot compare models when only the pinned ERFA/SOFA family is available. | Would require `SYNTHETIC` inputs plus a second pinned independent model/library, exact source/version, domain, and coefficient conventions. | Atmosphere and altitude grid, warnings, model domains. Blocked by required independent model/data; AST-004/006 review follows pinning. |
| `2C.4-EXP-02` | How does the pinned SOFA-family refraction output respond to explicit meteorological inputs? May measure local and interaction sensitivity. Cannot approve a range, default, uncertainty model, or tolerance. | `SYNTHETIC`; PyERFA `refco`/`atioq`, explicit pressure hPa, temperature °C, humidity fraction, wavelength µm, geometric direction, and pressure-zero control. | One-at-a-time/joint changes, explicit uncertainty candidates, measured/derived labels. Same-family only; altitude/component/angular/warning/hash metrics. AST-004/006 review may design an approved domain later. |
| `2C.4-EXP-03` | What numerical behaviour and warnings occur around the documented low-altitude partitions? May measure library sensitivity and path disagreement. Cannot establish a UFUQ validity threshold or below-horizon applicability. | `SYNTHETIC`; Astropy `AltAz` and direct PyERFA/SOFA-family routines with explicit atmosphere and geometric directions. | Above/around/below the documented about-5-degree region, around zero, negative altitudes, forward/reverse paths. Shared lineage declared; altitude/angular/warning/status/hash metrics. AST-004/006 review may select later experiments or a domain. |
| `2C.4-EXP-04` | Where does a named reference model place apparent altitude zero relative to geometric altitude zero? May measure a model-specific crossing while retaining both values. Cannot instantiate an approved UFUQ apparent-horizon state or introduce terrain/dip/learner semantics. | `SYNTHETIC`; one explicitly named SOFA-family model, explicit atmosphere, geometric direction sweep, north-east azimuth convention. | Pressure-zero identity, selected explicit atmospheres, crossing brackets, azimuth partitions. No independent model; altitude/angular/status/hash metrics. AST-004/006 review may define a later approved horizon policy. |
| `2C.4-EXP-05` | Does below-horizon probing preserve the valid geometric direction and earlier warnings/statuses? May establish exact non-erasure and precedence invariants plus library-behaviour measurements. Cannot approve refracted values below the horizon. | `SYNTHETIC`; explicit geometric directions, candidate refraction routine when requested, no-default state records. | Small/large negative altitude, numerical-guard region, refraction not requested/unavailable/invalid, deliberately later visibility failure. Exact state/status preservation plus measurement metrics. AST-004/007 review may approve outcome semantics later. |
| `2C.4-EXP-06` | What changes when Astropy library defaults are used, and does the UFUQ protocol prohibit their silent use? May quantify default consequences and establish exact no-default/status guards. Cannot approve any default. | `SYNTHETIC`; Astropy `AltAz` default and fully explicit fields, PyERFA pressure-zero/nonzero controls, explicit missing-meteorology state. | Each omitted library field, all explicit defaults, pressure-zero geometric, missing requested input, malformed input. Shared lineage; angular/altitude/status/byte/hash metrics. AST-004 review may retain the no-default rule. |
| `2C.4-EXP-07` | Can each visibility component change independently without promoting another or erasing coordinates? May establish structural independence and state-preservation invariants. Cannot establish photometric visibility, an aggregate boolean, screen policy, or learner eligibility. | `SYNTHETIC` component/status records only; no astronomy library, terrain, weather, or photometric data required. | Change each of nine components alone and in multi-fault precedence cases; inject forbidden promotion/erasure faults. Structural comparison is independent of ERFA; exact status/byte/hash checks. AST-004/007 review may approve a later serialized state model. |

## Proposed first executable batch for Milestone 2C.5B

`PROJECT_DECISION`: propose `2C.5B-BATCH-01` as five execution groups. “Executable”
means protocol-authorized synthetic measurement or invariant work, not scientific or
production approval.

| Group | Registry IDs | Risk retired | Permitted result |
|---|---|---|---|
| Epoch-label guards | `2C.1-EXP-01`, `2C.1-EXP-02`, `2C.1-EXP-03` | Quantifies representation/scale sensitivity while proving rejected interpretations remain rejected. | Measurements plus exact candidate-set guard; no source interpretation or tolerance. |
| Route/convention consistency | `2C.2-EXP-01` | Detects route wiring, sign, unit, intermediate-state, cardinal/wrap, and warning/status faults early. | Same-family consistency only; never independent validation. |
| Motion-convention guards | Runnable subset of `2C.2-EXP-04` | Detects omitted/double cosine, target-epoch labelling, JD-split, pole-guard, and warning-loss defects. | Exact injected-fault/status checks plus measurements; no I/311 propagation. |
| Deterministic replay | `2C.3-EXP-01` | Proves registry/fixture/result serialization, hashes, offline configuration, and replay before numerical evidence expands. | Exact byte/hash/status checks; no production EOP/leap approval. |
| Optional-state guards | `2C.4-EXP-05`, `2C.4-EXP-06`, `2C.4-EXP-07` | Proves geometric-state preservation, no default atmosphere, outcome precedence, and visibility-component independence. | Exact structural/status checks plus library-default consequence measurements; no refraction/visibility policy. |

Meteorology sweeps, near-horizon numerical studies, broad effect ablations, timestamp
boundaries, and observer partitions are runnable but excluded from Batch 01. They add
many measurements before the protocol runner, canonical result envelope, and warning/
status preservation have proved stable. The blocked experiments remain blocked.

The machine registry is authoritative for Batch 01 membership and scope identifiers.
For `2C.2-EXP-04`, only
`2C.2-EXP-04-BATCH01-SYNTHETIC-CONVENTION-GUARDS` is admitted: omitted-cosine,
double-cosine, declared-target-epoch-label, two-part-JD-split, and warning/status-
preservation partitions. Batch-level guards reject `SOURCE_DERIVED` and
`PRODUCTION_GENERATED` inputs, I/311 rows, HIP-derived values, catalogue source bytes,
and claims of I/311 epoch resolution, independent validation from shared lineage,
production approval, or accepted scientific tolerance. Adding a partition or member
changes the reviewed registry and its protocol-shape test; it is not an implicit
extension of Batch 01.

## Machine-readable structure

Milestone 2C.5A requires the smallest structure that can prevent silent claim drift:

| Artifact | Decision |
|---|---|
| Human experiment registry | Required; this document owns scientific questions, permitted/prohibited claims, classifications, blockers, and follow-up approvals. |
| Versioned machine-readable registry | Required at `tools/astronomy-reference/experiments/experiment-registry.v1.json`; it freezes IDs, classifications, schemas, lineages, first-batch membership, and execution/acceptance modes. |
| Registry schema | Required at `experiment-registry.v1.schema.json`. Draft 2020-12 is declared, but full schema meta-validation remains limited by the unresolved runtime-validator decision `DATA-SRC-002`. |
| Fixture schema | Required at `experiment-fixture.v1.schema.json`; it accepts only the 17 currently runnable IDs and closed, provenance-labelled synthetic input records. The existing three-case smoke schema is intentionally not widened or reinterpreted. |
| Result schema | Required at `experiment-result.v1.schema.json`; it contains completed/blocked/skipped/error outcomes, measurements, exact checks, warnings/statuses, decision limits, and canonical hashes. |
| Separate execution manifest | Not required. The result embeds an immutable execution manifest with experiment/fixture/case IDs, protocol/registry/schema versions and hashes, environment/lock/fixture hashes, exact software versions, runtime/OS context, runner argv/source hashes, lineage, offline/cache state, used external-artifact provenance, repetition count, canonicalization, and record ordering. Purely synthetic cases use an empty external-artifact list rather than inventing an artifact. |
| Separate error-budget ledger | Not created in 2C.5A. Measurement-only and exact-invariant runs have no numerical acceptance threshold. A separately versioned ledger becomes mandatory before AST-006 proposes any scientific/reference tolerance or total-error acceptance. The result envelope must report `NOT_ESTABLISHED_AST_006_OPEN` until then. |

No fixture or result instance and no numerical experiment body is added by 2C.5A.
The v1 fixture/result schemas accept only synthetic experiment evidence. A future
source-derived or production/reference comparison requires a separately reviewed
successor schema rather than relabelling a v1 synthetic document.
The result's embedded `canonicalContentSha256` covers the canonical object before that
field is inserted; the hash of the complete result file is a separate companion
execution artifact. No self-referential hash is permitted.

### Canonical serialization and hash boundaries

`PROJECT_DECISION`: `UFUQ_CANONICAL_JSON_V1` means UTF-8 without a byte-order mark,
Unicode NFC strings, lexicographically ordered object keys, two-space indentation, LF
line endings, and exactly one terminal LF. JSON numbers must be finite IEEE-754 binary64
values, except non-negative byte counts may be exact JSON integers. `NaN`, positive or
negative infinity, negative zero, numeric strings, locale formatting, and redundant
leading/trailing zeroes are prohibited. Binary64 numbers use the shortest decimal that
round-trips to the same value, lowercase `e`, and no `+` exponent sign.

Array order is semantic and must not depend on hash-map or filesystem iteration. The
registry is ordered by experiment ID; Batch 01 groups use their declared order and
members are ordered by experiment ID; measurements by `measurementId`; warnings,
statuses, and execution reasons by `sequenceIndex`; checks by `checkId`; and source,
schema, artifact, and runner-file hashes by role then stable identifier/path. Fixture
parameter partitions retain their declared registry order. A runner must reject a
duplicate ordering key.

The fixture SHA-256 covers the complete canonical fixture bytes. Registry, schema,
environment, lockfile, runner-source, and external-artifact hashes cover the exact
named file bytes. `canonicalContentSha256` covers canonical result bytes with only that
field omitted; after insertion, the complete result file receives a separate companion
SHA-256. Byte identity establishes deterministic serialization and replay only. It is
not evidence of scientific correctness, source authority, or numerical acceptance.

## Decisions experiment output may inform

- the magnitude and warning/status consequences of candidate epoch labels without
  deciding source meaning;
- whether a decomposed candidate route has internal wiring, convention, or ownership
  faults before production selection;
- where cosine, pole, double-application, status-loss, default-insertion, and state-
  erasure guards are required;
- which effects, EOP/refraction partitions, and numerical boundaries deserve deeper
  experiments;
- whether the deterministic fixture/result protocol is sufficient for offline replay;
  and
- evidence supplied to AST-003/004/006/007 reviewers when they later assess candidate
  policies.

## Decisions experiment output cannot resolve

- the I/311 epoch or proper-motion derivative time scale, catalogue row meaning, or
  any other missing source authority;
- the production TypeScript algorithm/library or approval of the proposed SOFA route;
- radial-velocity provenance, usable parallax policy, or source-derived propagation;
- production EOP/leap artifacts, field precedence/quality approval, stale/update rule,
  prediction acceptance, supported dates, observer domain, or degraded mode;
- refraction model selection, atmosphere defaults/ranges, validity domain, physical or
  terrain horizon, visibility, rendering, or learner eligibility;
- an omission bound, error budget, scientific/reference tolerance, rendering
  tolerance, learner tolerance, or wire/HTTP contract; or
- scientific approval merely because deterministic, Astropy, PyERFA, or same-family
  SOFA/ERFA results agree.

## Exit decision

Milestone 2C.5A freezes a proposed protocol and machine-readable scaffolding. Milestone
2C.5B may implement Batch 01 only after explicit project review accepts its frozen
synthetic scope; it may not introduce source-derived or production astronomy.
Milestone 2C remains **OPEN** because the 2C.1–2C.4 source, project-decision, data,
review, production, error-budget, and tolerance blockers are unchanged.
