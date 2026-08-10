# Phase 1 Milestone 2C.5C: Scientific Error-Budget Framework

## Status and recommendation

- **Milestone:** 2C.5C
- **Evidence interpretation date:** 2026-08-11
- **AST-006 recommendation:** `FINAL_TOLERANCE_NOT_JUSTIFIED`
- **Numerical scientific tolerance approved:** no
- **Milestone 2C status:** `OPEN`
- **Review state:** named astronomy-expert and supervisor review required

This document interprets the committed synthetic Batch 01 evidence and defines the
method by which a future error budget can be assembled. It does not select a source
epoch scale, production algorithm, operating domain, EOP or leap product, observer,
refraction model, scene tolerance, or learner tolerance.

The companion machine-readable ledger is
`../governance/AST_006_ERROR_BUDGET_LEDGER.v1.json`. It is the complete inventory of terms,
measurements, exact invariants, tolerance classes, evidence hashes, and approval
states. Unknown terms are `UNBOUNDED_UNRESOLVED`, never zero.

The ledger contains exactly 49 terms: 45 terms have an
`UNBOUNDED_UNRESOLVED` numerical-bound state, and four exact non-numerical guards
(`F-002`, `F-003`, `F-004`, and `F-006`) contribute no numerical uncertainty value.
This count does not move downstream layers G-H into the astronomy budget.

## Frozen evidence boundary

The nine committed Batch 01 results were read directly. They contain 9/9 completed
experiments, 24 exact invariant passes, no exact invariant failures, six
measurement-only checks, and 27 individual `MEASURED_NO_ACCEPTANCE` records. A
measurement-only check is a check-level grouping; a measurement record is one
serialized quantity beneath such a check.

`PROJECT_DECISION`: the committed experiment protocol remains frozen at SHA-256
`c6e8f2e12b847cfb4b718b2b6b3c30ac0b2ae94f5e0451b1ecaef4ae70548b81`.
It is an input hash in all nine result manifests. Milestone 2C.5C therefore does not
edit that protocol, the registry, experiment schemas, Batch runner, fixtures,
environment manifest, or lockfile. Editing any of those hashed inputs would invalidate
the canonical evidence and require full Batch regeneration before this interpretation
could proceed.

No canonical Batch evidence is regenerated for 2C.5C. This document and its ledger
interpret the already committed results only. The required locked offline unit suite
may exercise the non-writing Batch runner as repository validation; such execution
does not replace, modify, or promote the canonical result records.

## Classification and numerical-value discipline

Every ledger term or tolerance decision uses exactly one of these statuses:

- `EXACT_CONTRACT_INVARIANT`;
- `MEASURED_SYNTHETIC_SENSITIVITY`;
- `SOURCE_UNCERTAINTY_UNRESOLVED`;
- `MODEL_UNCERTAINTY_UNRESOLVED`;
- `OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED`;
- `IMPLEMENTATION_ERROR_UNMEASURED`;
- `INDEPENDENT_VALIDATION_REQUIRED`;
- `HUMAN_REVIEW_REQUIRED`;
- `CANDIDATE_TOLERANCE_PROPOSAL`; and
- `FINAL_TOLERANCE_NOT_JUSTIFIED`.

Every number must also retain its value category:

| Category | Meaning |
|---|---|
| `MEASURED_VALUE` | Output observed in a named experiment. It is not a bound or threshold. |
| `MATHEMATICAL_EXACTNESS` | Exact identity or definition, not an empirical uncertainty. |
| `SOURCE_DECLARED_UNCERTAINTY` | Uncertainty supplied by a named source for a named field/case. |
| `EXTERNAL_AUTHORITY_LIMIT` | Domain or accuracy limit stated by an authority, not automatically UFUQ policy. |
| `CANDIDATE_ENGINEERING_ALLOWANCE` | Proposed allowance awaiting evidence and review. |
| `SCIENTIFICALLY_APPROVED_ACCEPTANCE_THRESHOLD` | Reviewed threshold for a named operation and domain. None exists yet. |

`MEASURED_VALUE` must never be promoted to one of the last four categories without
the corresponding source, model, domain, combination rule, and approval evidence.

## Error-budget layers

Layers A-F form the future astronomy scientific budget. Layers G-H are tracked beside
it but are prohibited from changing or weakening the astronomy budget.

| Layer | Scope | Current result |
|---|---|---|
| A | Source/catalogue uncertainty: position, proper motion, parallax, radial velocity, correlations, and epoch/derivative semantics. | `SOURCE_UNCERTAINTY_UNRESOLVED`; selected-row values/covariances and source-scale authority are absent. |
| B | Propagation/model uncertainty: epoch interpretation, space motion, bias/precession/nutation, aberration, deflection, frame transformations, and omitted/optional terms. | `MODEL_UNCERTAINTY_UNRESOLVED`; Batch 01 supplies sensitivities and guards, not approved bounds. |
| C | Earth-orientation/time uncertainty: leap seconds, `UT1-UTC`, `xp`, `yp`, `dX`, `dY`, quality state, interpolation, prediction, and staleness. | `OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED`; no production artifacts or policies are approved. |
| D | Observer uncertainty: latitude, longitude, ellipsoidal height, datum, coordinate uncertainty, and supported observer domain. | `OPERATIONAL_DATA_UNCERTAINTY_UNRESOLVED`; no datum, values, ranges, or uncertainties are approved. |
| E | Atmosphere/refraction uncertainty: model, meteorology, wavelength, height/lapse handling, near-horizon behavior, and validity domain. | `MODEL_UNCERTAINTY_UNRESOLVED`; optional refraction remains unavailable. |
| F | Numerical implementation uncertainty: floating point, two-part JD, units/sign/cosine adapters, production/reference disagreement, and status preservation. | Exact guards retire bounded mutation classes; the numerical production error remains `IMPLEMENTATION_ERROR_UNMEASURED`. Serialization determinism is not a scientific term. |
| G | Scene/render mapping: ENU-to-scene mapping, camera projection, visual placement, and screen discretization. | Separate non-astronomy budget; currently `IMPLEMENTATION_ERROR_UNMEASURED`. |
| H | Downstream scenario/learner/assessment: scenario-generation, interaction radius, answer selection, and scoring policy. | Separate downstream policy budget; currently `HUMAN_REVIEW_REQUIRED`. |

The ledger records every term with its layer, quantity, authority, status, units,
bound state, correlation assumption, affected stage, supported domain, evidence IDs,
combined-budget disposition, reviewer, and approval state.

Scenario generation is tracked in layer H only as a separate downstream policy term;
it is not learner uncertainty and cannot redefine the upstream astronomy budget. Empty
or missing scene evidence is represented by the `AST-SRC-015` gap, never by zero.

## What the 24 exact invariants retire

`EXACT_CONTRACT_INVARIANT`: each pass retires only the named fault in the synthetic
Batch runner/fixture path. It assigns no angular uncertainty and does not prove that a
future production implementation contains the guard.

| Experiment / check | Bounded mistake class retired | Explicit limitation |
|---|---|---|
| `2C.1-EXP-01 / explicit-scale-labels-preserved` | Collapsing TT/TDB/UTC candidate labels or omitting the explicit synthetic geocentre input. | Does not resolve I/311 scale, conversion correctness, observer policy, or leap policy. |
| `2C.1-EXP-01 / source-meaning-claim-absent` | Claiming synthetic output establishes I/311 meaning. | Retires no physical, source, model, or numerical uncertainty. |
| `2C.1-EXP-03 / besselian-source-candidate-rejected` | Admitting `BYEAR` to the supported source-representation set. | Does not select an exact Julian scale/instant. |
| `2C.2-EXP-01 / geometric-pressure-zero-preserved` | Inserting nonzero pressure/refraction into the two tested route inputs. | Does not prove geometric-transform accuracy or exclude every hidden effect. |
| `2C.2-EXP-01 / same-family-lineage-preserved` | Calling shared ERFA/SOFA agreement independent validation. | Provides no correctness or numerical bound. |
| `2C.2-EXP-01 / sofa-statuses-preserved` | Dropping raw statuses from the tested ERFA stages. | Does not approve nonzero-status handling or the route. |
| `2C.2-EXP-04 / declared-target-epoch-label-preserved` | Treating target-epoch propagation as a frame conversion or losing the declared target/frame labels. | Does not approve J2000.0 or source-derived propagation. |
| `2C.2-EXP-04 / double-cosine-mutation-rejected` | Admitting an injected double-`cos(dec)` proper-motion adapter. | Does not bound production propagation or source-motion uncertainty. |
| `2C.2-EXP-04 / omitted-cosine-mutation-rejected` | Admitting an injected omitted-`cos(dec)` adapter. | Does not bound production propagation or all declinations. |
| `2C.2-EXP-04 / pmsafe-warning-status-preserved` | Swallowing raw `pmsafe` status `1` or its wrapper warning. | Does not approve distance override, parallax/RV policy, or the warning. |
| `2C.2-EXP-04 / two-part-jd-declarations-equivalent` | Declared split pairs encoding different exact source/target JDs in the tested case. | Does not bound general floating-point or production JD handling. |
| `2C.3-EXP-01 / artifact-hashes-verified` | Substitution of the two named smoke-only data files. | Does not approve their accuracy, currency, coverage, or production use. |
| `2C.3-EXP-01 / canonical-replay-bytes-identical` | Nondeterministic serialization of the fixed replay payload. | Byte identity is not scientific correctness or an error term. |
| `2C.3-EXP-01 / network-and-cache-policy-preserved` | Known auto-download/cache-discovery and standard network paths in the bounded runner context. | Does not prove air-gapped reconstruction or production offline policy. |
| `2C.4-EXP-05 / below-horizon-attaches-to-geometric-state` | Replacing a valid signed geometric direction with a terminal horizon failure. | Does not establish physical, terrain, refraction, or visibility correctness. |
| `2C.4-EXP-05 / optional-failure-does-not-erase-geometric-state` | A later visibility non-result erasing earlier coordinates. | Does not establish visibility policy. |
| `2C.4-EXP-05 / signed-altitude-azimuth-provenance-preserved` | Clamping/dropping signed altitude, defined azimuth, frame, or provenance. | Does not validate the direction or singularity policy. |
| `2C.4-EXP-05 / warnings-and-statuses-preserved` | Reordering/dropping the injected upstream warning/status. | Does not establish real warning coverage or approval. |
| `2C.4-EXP-06 / missing-meteorology-produces-unavailable` | Producing refracted output from missing requested meteorology. | Does not select a model, input domain, or tolerance. |
| `2C.4-EXP-06 / no-atmosphere-default-inserted` | Inserting pressure, temperature, humidity, wavelength, or lapse defaults. | Does not approve any atmosphere input or behavior. |
| `2C.4-EXP-06 / not-requested-distinct-from-unavailable` | Conflating two optional-stage states. | Does not validate refracted coordinates or wire serialization. |
| `2C.4-EXP-07 / aggregate-visibility-claim-absent` | Producing an unapproved aggregate visible/not-visible claim. | Does not establish any visibility component. |
| `2C.4-EXP-07 / geometric-state-retained-through-visibility-failure` | Visibility-policy failure erasing valid coordinates. | Does not establish visibility correctness. |
| `2C.4-EXP-07 / nine-visibility-components-independent` | Merging, omitting, or promoting the nine component keys. | Does not validate component values, interactions, aggregation, or learner eligibility. |

## Interpretation of all 27 numerical/hash records

All values below are `MEASURED_VALUE` and remain
`MEASURED_SYNTHETIC_SENSITIVITY` or non-budget diagnostics. Serialized zero is retained
and is not interpreted as exact scientific agreement.

| Evidence ID | Value | Interpretation | Error-budget use now |
|---|---:|---|---|
| `2C.1-EXP-01/tdb-astropy-vs-pyerfa-separation` | `0 rad` | Same-family Astropy/PyERFA consistency. | None; shared lineage. |
| `2C.1-EXP-01/tdb-utc-propagated-separation` | `9.758026479142074e-11 rad` | Synthetic epoch-scale-label sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-01/tdb-utc-start-instant-seconds` | `-58.18564352977016 s` | Synthetic represented-instant sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-01/tt-astropy-vs-pyerfa-separation` | `2.0630814761166832e-16 rad` | Same-family Astropy/PyERFA consistency. | None; shared lineage. |
| `2C.1-EXP-01/tt-tdb-propagated-separation` | `2.694516999735788e-15 rad` | Synthetic epoch-scale-label sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-01/tt-tdb-start-instant-seconds` | `0.0016435295460581756 s` | Synthetic represented-instant sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-01/tt-utc-propagated-separation` | `9.757755367285327e-11 rad` | Synthetic epoch-scale-label sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-01/tt-utc-start-instant-seconds` | `-58.1840000002241 s` | Synthetic represented-instant sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-01/utc-astropy-vs-pyerfa-separation` | `0 rad` | Same-family Astropy/PyERFA consistency. | None; shared lineage. |
| `2C.1-EXP-02/label-1991-25-propagated-separation` | `4.52803878167281e-8 rad` | Calendar-decimal-year versus Julian-epoch sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-02/label-1991-25-start-instant-seconds` | `27000.00000012702 s` | Calendar versus Julian represented-instant sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-02/label-1992-25-propagated-separation` | `4.529871110088503e-8 rad` | Leap-year partition sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-02/label-1992-25-start-instant-seconds` | `27000.000000265965 s` | Leap-year represented-instant sensitivity. | Descriptive candidate input only. |
| `2C.1-EXP-03/besselian-vs-julian-propagated-separation` | `5.91146145377762e-9 rad` | Diagnostic consequence of a rejected representation. | None; rejection is authority/contract based, not magnitude based. |
| `2C.1-EXP-03/besselian-vs-julian-start-instant-seconds` | `-34416.68259658114 s` | Diagnostic consequence of a rejected representation. | None. |
| `2C.2-EXP-01/altitude-residual` | `0 rad` | Componentized/composed ERFA same-family consistency. | None; no independent comparison. |
| `2C.2-EXP-01/azimuth-residual` | `0 rad` | Componentized/composed ERFA same-family consistency. | None. |
| `2C.2-EXP-01/horizontal-direction-separation` | `0 rad` | Componentized/composed ERFA same-family consistency. | None. |
| `2C.2-EXP-01/observed-component-residuals` | `[0,0,0,0] rad` | Componentized/composed ERFA component consistency. | None. |
| `2C.2-EXP-04/double-cosine-propagated-separation` | `0.002018722526328022 rad` | Deliberate adapter-mutation consequence. | Convention diagnostic only; not residual uncertainty. |
| `2C.2-EXP-04/jd-split-1-coordinate-residuals` | `[0,0,0,0,0,0] mixed pmsafe units` | Tested split diagnostic. | None; no general floating-point bound. |
| `2C.2-EXP-04/jd-split-2-coordinate-residuals` | `[0,0,0,0,0,0] mixed pmsafe units` | Tested split diagnostic. | None. |
| `2C.2-EXP-04/omitted-cosine-propagated-separation` | `0.0003505483020686592 rad` | Deliberate adapter-mutation consequence. | Convention diagnostic only. |
| `2C.2-EXP-04/warning-wrapper-vs-raw-residuals` | `[0,0,0,0,0,0] mixed pmsafe units` | Wrapper/raw same-family warning-case diagnostic. | None. |
| `2C.3-EXP-01/canonical-payload-byte-length` | `158 byte` | Reproducibility metadata. | None; serialization size is not astronomy error. |
| `2C.3-EXP-01/canonical-payload-sha256` | `2fd69f3ed98002971de5ae37efb0ef1427f4a523d742ef714150c4377a486d4a` | Reproducibility metadata. | None; a hash is not scientific correctness. |
| `2C.4-EXP-05/retained-coordinate-residuals` | `[0,0] deg` | Exact state-retention diagnostic. | None; does not validate physical coordinates. |

The ten epoch/calendar sensitivity records that are not direct wrapper/route agreement
records may help design a future candidate bound. Their execution still uses shared
ERFA/SOFA lineage and is not independent. They cannot be combined now because the
source interpretation, source rows, supported date domain, motion/RV/parallax policy,
and correlation model are absent. The two rejected-Besselian records cannot enter a
budget because that interpretation is prohibited rather than probabilistic.

## Candidate combination rules

These rules are `CANDIDATE_TOLERANCE_PROPOSAL`; no numerical total can be calculated
until every required term has an approved bound and compatible domain.

1. Use a worst-case bounded sum for terms that are only known to lie in deterministic
   intervals or whose dependence is unknown. Do not assume cancellation.
2. Use root-sum-square only for terms supported as independent, zero-mean random
   quantities under the same case/domain. Record the evidence for independence and
   distribution. Shared source fields, common EOP products, common model lineage, and
   common observer surveys are not presumed independent.
3. Carry correlated/systematic terms through a covariance matrix, joint sensitivity
   model, or conservative grouped bound. Do not combine a deterministic model bias
   with random observation error without an explicit model.
4. Preserve asymmetric positive/negative bounds when effects are directional or the
   domain is nonlinear. A symmetric scalar must not hide a one-sided horizon or time
   effect.
5. Transform compatible covariance/bounds into the quantity at the tested boundary
   before combination. RA/Dec, ENU direction, altitude, azimuth, time, and observer
   position are not interchangeable units.
6. Report both the combined result and its term-level contributions per case. No RMS
   or maximum may aggregate unrelated fixtures merely because they use angular units,
   and no average may hide a failed case.
7. If a required term is `UNBOUNDED_UNRESOLVED`, the combined scientific budget is
   `UNBOUNDED_UNRESOLVED`; it is not computed from the remaining terms.

## Metric hierarchy

| Boundary | Primary metric | Required supporting metrics and limitations |
|---|---|---|
| Catalogue/propagated ICRS | Unit-vector great-circle separation | RA and declination residuals plus covariance. RA residual alone is ill-conditioned near celestial poles. |
| Celestial/intermediate direction | Unit-vector great-circle separation | Frame-labelled component residuals and status/warning differences. |
| Earth orientation/time | `UT1-UTC` or other time residual in seconds, plus direction consequence | Record `xp`,`yp`,`dX`,`dY` component perturbations separately; do not collapse field quality. |
| Geometric horizontal | ENU/unit-vector angular separation | Signed altitude residual and wrapped azimuth residual. Azimuth is undefined at zenith/nadir and increasingly ill-conditioned nearby. |
| Horizon/refraction | Signed geometric and apparent altitude residuals separately | Great-circle separation and warnings; a near-horizon rule must be model/domain dependent. Geometric and refracted altitude are never merged. |
| Observer | Geodetic/Cartesian position perturbation in declared units and resulting direction separation | Preserve datum, height type, latitude/longitude partition, and correlation. |
| Scene | Direction-vector/angular placement before projection, then pixel/screen residual | Scene metrics are separate from scientific acceptance. |
| Learner/scoring | Task-specific circular/vector/selection distance | Educational validity and scoring rules are separate from astronomy error. |

No global altitude/azimuth tolerance is proposed. Near the zenith, use vector
separation instead of azimuth. Near the horizon, retain geometric and refracted
altitude separately and condition any future rule on the approved model, atmosphere,
observer, and domain. Azimuth at the geometric horizon remains defined when the
horizontal projection and north reference are defined; the horizon sensitivity is not
permission to assign it the zenith singularity. Observer locations at geographic poles
still require their unresolved north/longitude policy. Below-geometric-horizon remains
an attached classification on a valid signed direction, not a tolerance failure.

Astropy 8.0.1's documented statement that its ERFA-based refraction becomes inaccurate
below about 5 degrees is recorded as `EXTERNAL_AUTHORITY_LIMIT`. It is a
reference-library limitation and experiment partition only—not a UFUQ validity domain,
uncertainty bound, or acceptance threshold.

## Tolerance classes

| Tolerance class | Status | Numerical value | Reason |
|---|---|---|---|
| `ScientificReferenceTolerance` | `BLOCKED` | none | Source/model/EOP/observer/domain terms are unbounded and no independent end-to-end scientific validation exists. |
| `ProductionImplementationTolerance` | `BLOCKED` | none | No production TypeScript implementation or production/reference disagreement exists. |
| `ScenarioGenerationTolerance` | `BLOCKED` | none | Source-derived processing, scenario domain, and upstream scientific threshold are unavailable. |
| `SceneAngularTolerance` | `BLOCKED` | none | Scene, camera, projection, and screen errors are unmeasured; this class cannot redefine astronomy accuracy. |
| `LearnerInteractionTolerance` | `BLOCKED` | none | No approved interaction task/domain or educational review exists. |
| `AssessmentScoringTolerance` | `BLOCKED` | none | No approved scoring policy, learner evidence, or boundary rule exists. |

The class boundaries and candidate combination/metric method are reviewable now, but
no numerical tolerance is `APPROVABLE_NOW` or `CANDIDATE_ONLY`. Exact guards remain
boolean contract tests, not tolerances.

## Evidence required before production scientific acceptance

`INDEPENDENT_VALIDATION_REQUIRED`: a production scientific tolerance needs all of the
following before AST-006 approval:

- the approved TypeScript production route and a code-sharing audit;
- a genuinely independent reference path for the claimed boundary, with same-family
  SOFA/ERFA consistency recorded separately;
- source-derived fixtures only after I/311 epoch/derivative authority and catalogue
  processing authority are resolved;
- row-level position/motion/parallax uncertainty and covariance plus the approved RV
  or omission policy;
- approved production leap/EOP artifacts and per-field quality, coverage,
  interpolation, stale/prediction, and celestial-pole-offset policy;
- multiple dates across the eventual supported domain, including endpoints and
  leap/EOP boundaries;
- multiple approved observers: the initial first-slice location, preset locations,
  latitude and longitude partitions, height partitions, near-equatorial guide-star
  cases, and any future arbitrary-location mode;
- high- and low-declination, high-motion, parallax, RV, horizon, zenith/nadir, and
  warning/status cases; and
- per-case disagreement and term budgets reviewed by a named astronomy expert.

No geographic range is invented here. Polaris or another guide star changes altitude
with observer latitude, including near-equatorial cases close to the geometric
horizon. Future validation must therefore partition locations rather than certify one
hard-coded site as a global tolerance.

## Ranked next synthetic experiments

No experiment is executed by 2C.5C. The remaining eight
`RUNNABLE_SYNTHETIC_NOW` records are ranked by scientific risk retired per expected
implementation effort:

| Rank | Experiment | Rationale and limit |
|---:|---|---|
| 1 | `2C.3-EXP-02` EOP state partitions | High-risk field promotion/zero/nearest substitution guards with low effort; structural evidence only. |
| 2 | `2C.3-EXP-05` observer partitions | Retires sign, pole, height-label, provenance, and singularity faults before a domain is selected. |
| 3 | `2C.3-EXP-04` leap/timestamp boundaries | Retires high-impact grammar, table, conversion, and status-loss faults using the smoke-only artifact; no production leap policy follows. |
| 4 | `2C.2-EXP-03` effect ablation/interactions | Detects ownership, sign, omission, and double-application risks; higher effort and same-family only. |
| 5 | `2C.2-EXP-06` observer/parallax/RV sensitivity | Describes major unbounded terms and double-application risks; cannot select policies. |
| 6 | `2C.4-EXP-03` near-horizon numerical sensitivity | Demonstrates domain dependence and warnings; cannot set a validity threshold. |
| 7 | `2C.4-EXP-02` meteorology sensitivity | Supplies reference-model sensitivity for a later atmosphere proposal; refraction remains optional and blocked. |
| 8 | `2C.4-EXP-04` geometric/apparent horizon sensitivity | Model-specific crossing evidence has lower near-term value while the model/policy is unavailable. |

A candidate next batch is ranks 1-3 because they primarily exercise exact state and
boundary guards without inventing policy. This ranking is risk/knowledge-value
planning only, not execution authority, scientific approval, or policy approval. It
still requires a separate reviewed batch scope before execution, and any experiment
whose required policy, data, or review prerequisite is unavailable must fail closed
rather than silently execute.

## AST-006 review recommendation and stop condition

`FINAL_TOLERANCE_NOT_JUSTIFIED`: Batch 01 establishes bounded exact contract guards,
descriptive synthetic sensitivity, same-family consistency, warning/status retention,
and deterministic evidence transport. It does not establish source uncertainty,
physical/model uncertainty, production implementation error, independent scientific
agreement, supported-domain coverage, or a final numerical threshold.

AST-006 should review and either approve or revise the layer, metric, combination, and
traceability method while leaving every numerical tolerance unapproved. Milestone
2C.5C and Milestone 2C remain open/review-gated until the unbounded required terms are
bounded or the affected behavior is explicitly removed from scope, followed by named
astronomy-expert and supervisor approval.
