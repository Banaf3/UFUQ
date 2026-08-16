# Gaia DR3 TCB-to-TDB compatible-quantity authority

## Scope and decision

This study resolves only Milestone 2D.1A: the normalization of a native Gaia DR3
TCB-compatible astrometric state into the TDB-compatible catalogue state required by
ScientificProfileV1's approved SOFA-derived propagation boundary. It does not approve
a Gaia row, a radial-velocity measurement for a particular physical component, a
query response, a Polaris fallback, or deployment rights.

Decision: `TCB_TDB_ADAPTER_AUTHORITY_CLOSED`.

The analytic contract below is implementation-ready without a numerical acceptance
tolerance. Milestone 2E may implement it only from an approved native record; a later
production/reference comparison must verify the implementation. The overall 2D.1
catalogue decision remains `CATALOGUE_AUTHORITY_BLOCKED` on gates B-E.

## Authority and classification boundary

| Claim | Classification | Authority or decision |
|---|---|---|
| Gaia DR3 astrometry is parametrized in BCRS with TCB as independent time, and `ref_epoch` is a Julian year in TCB. | `SOURCE_SUPPORTED_FACT` | ESA Gaia DR3 reference-system, standard-motion-model, and `gaia_source` documentation. |
| TDB is the fixed linear transformation of TCB defined by IAU 2006 Resolution B3. | `SOURCE_SUPPORTED_FACT` | IAU 2006 Resolution B3. |
| A TDB-compatible barycentric spatial coordinate is scaled with the same defining factor as the TDB time coordinate; the corresponding coordinate velocity is unchanged. | `SOURCE_SUPPORTED_FACT` | Klioner (2008), applying the IAU-compatible-quantity framework. |
| The astronomical unit is exactly `149597870700 m` and is used with all time scales. | `SOURCE_SUPPORTED_FACT` | IAU 2012 Resolution B2. |
| UFUQ applies the compatible-system map below to Gaia's native five-parameter tangent-plane state and retains both native and normalized states. | `PROJECT_DECISION` | Rule `GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1`. |
| A Gaia spectroscopic barycentric radial-velocity measure is preserved as an observational quantity and is never scale-converted merely because the astrometry is normalized. | `SOURCE_SUPPORTED_FACT` for the observational meaning and coordinate-velocity scaling; `PROJECT_DECISION` for the typed preservation rule | Gaia DR3 data model; IAU 2000 Resolution C1; Lindegren and Dravins (2003); Klioner (2008). |
| A row may supply that value to the V1 propagation RV slot only after a separate row/component review approves the explicit proxy role. | `2D_DATA_SELECTION` | This is remaining 2D.1 gate C, not part of the compatible-system transform. |
| Exact serialization, Decimal/binary evaluation, schema, and transform implementation belong to 2E. | `2E_IMPLEMENTATION_CONFIGURATION` | Must reproduce this analytic contract without replacing exact constants by undocumented rounded values. |
| Numerical residuals and an acceptance tolerance belong after implementation. | `POST_IMPLEMENTATION_VALIDATION` | AST-006 remains `FINAL_TOLERANCE_NOT_JUSTIFIED`. |

No new human judgement is required to define the analytic compatible-quantity map.
Named astronomy/data review is still required to approve individual source records and
any spectroscopic-RV proxy.

## Defining constants and compatible systems

IAU 2006 Resolution B3 defines

```text
TDB = TCB - L_B * (JD_TCB - T_0) * 86400 s + TDB_0
```

with defining constants:

```text
L_B   = 1.550519768e-8
T_0   = 2443144.5003725
TDB_0 = -6.55e-5 s
```

UFUQ pins the exact derived expression

```text
F_B = 1 - L_B = 0.99999998449480232
K_B = 1 / F_B
```

`K_B` is stored/evaluated as the exact expression `1 / F_B`, not as a separately
rounded defining constant. `SOURCE_SUPPORTED_FACT`: `L_B`, `T_0`, and `TDB_0` are IAU
defining constants. `PROJECT_DECISION`: the rule manifest records `F_B` exactly and
the unevaluated inverse expression to prevent constant drift.

The terms **TCB-compatible** and **TDB-compatible** describe quantities associated
with their respective coordinate-time systems. They do not mean different SI units.
For the same barycentric solution,

```text
t_TDB-compatible = F_B * t_TCB-compatible + constant
x_TDB-compatible = F_B * x_TCB-compatible
v_TDB-compatible = dx_TDB-compatible / dt_TDB-compatible
                 = v_TCB-compatible
```

This is the compatible-quantity relation established by IAU B3 and Klioner's
treatment. UFUQ must not label values as being in “TDB units.”

## Reference-epoch instant

Gaia's native reference-epoch label `J2016.0 TCB` denotes a Julian epoch using a
Julian year of exactly `365.25` days of `86400 s`, with TCB as the coordinate time.
Using the standard Julian-epoch origin, its native two-part Julian Date is exactly:

```text
JD_TCB = 2451545.0 + (2016.0 - 2000.0) * 365.25
       = 2457389.0
```

`SOURCE_SUPPORTED_FACT`: the Gaia label, scale, and Julian-year convention come from
the official DR3 model; the Julian-epoch relation is the SOFA/IAU convention.

The target epoch is a TDB coordinate-time representation of the **same reference
event**, not a propagation target and not a renamed Julian-year label:

```text
JD_TDB = JD_TCB
       - L_B * (JD_TCB - T_0)
       + TDB_0 / 86400
```

`PROJECT_DECISION`: the normalized record retains the exact source label and
`JD_TCB`, and carries the target as a two-part `JD(TDB)` plus the B3 conversion
evidence. It does not store a rounded `J2016... TDB` string as authority. This event
conversion occurs before the later propagation from the normalized source epoch to
the approved J2000.0 TDB epoch interface.

## Field-by-field compatible-quantity map

Let native values have suffix `TCB` and normalized values have suffix `TDB`.

| Field | Approved mapping | Classification and consequence |
|---|---|---|
| ICRS direction vector | `u_TDB = u_TCB` | `SOURCE_SUPPORTED_FACT`: a positive uniform spatial scaling does not change direction. |
| Right ascension | `alpha_TDB = alpha_TCB` | `SOURCE_SUPPORTED_FACT`; preserve the ICRS angle and its wrap convention. |
| Declination | `delta_TDB = delta_TCB` | `SOURCE_SUPPORTED_FACT`; preserve the ICRS angle. |
| `mu_alpha_star` | `mu_alpha_star_TDB = K_B * mu_alpha_star_TCB` | `SOURCE_SUPPORTED_FACT` compatible-rate consequence; `PROJECT_DECISION` applies it to Gaia `pmra`. Starred-alpha semantics are preserved. |
| Declination proper motion | `mu_delta_TDB = K_B * mu_delta_TCB` | Same rule and time basis as `mu_alpha_star`. |
| Catalogue parallax | `parallax_TDB = K_B * parallax_TCB` | `SOURCE_SUPPORTED_FACT` consequence of the exact common AU and `distance_TDB = F_B * distance_TCB`; this is a compatible catalogue parameter, not a claim that an observed angular displacement changes. |
| Coordinate distance inferred as `AU/parallax` | `distance_TDB = F_B * distance_TCB` | `SOURCE_SUPPORTED_FACT`; retain the inference/model provenance separately from the observed parallax. |
| Optional barycentric Cartesian position | `x_TDB = F_B * x_TCB` | `SOURCE_SUPPORTED_FACT`; only if 2E constructs this explicit state. |
| Compatible Cartesian coordinate velocity | `v_TDB = v_TCB` | `SOURCE_SUPPORTED_FACT`; both position and time coordinate scale by `F_B`. |
| Gaia `radial_velocity` and `radial_velocity_error` | Preserve the published numbers unchanged in their native observational type; apply no `F_B` or `K_B` scale factor. | `SOURCE_SUPPORTED_FACT` that this is a spectroscopic Solar-system-barycentric measure, not an exact coordinate velocity; `PROJECT_DECISION` to preserve it without compatible scaling. |

`SOURCE_SUPPORTED_FACT`: total proper motion scales by `K_B`,
`parallax_over_error` remains numerically invariant because numerator and uncertainty
share the same positive factor, and any radial proper motion constructed from an
approved RV and compatible parallax scales by `K_B`. These helpers are not additional
SOFA catalogue inputs. `PROJECT_DECISION`: 2E recomputes and types derived helpers from
normalized primitive fields; it may not copy a native helper as new authority or use
one to bypass primitive-field normalization.

The parallax rule does not assert a physically different observation. The same
parallactic displacement is represented consistently only when the observer/ephemeris
coordinates, source distance, and catalogue parameter belong to the same compatible
system. Copying Gaia parallax unchanged into a TDB-compatible distance model would mix
systems.

## Proper-motion and pole boundary

Gaia `pmra` is `mu_alpha_star = (d alpha / dt) cos(delta)` in milliarcseconds per TCB
Julian year; `pmdec` is toward increasing declination per TCB Julian year.
`PROJECT_DECISION`: normalization first multiplies both tangent-plane rates by `K_B`
and labels their duration basis `TDB_JULIAN_YEAR_365_25_DAYS`.

The source-neutral normalized record continues to carry `mu_alpha_star`. Only the
SOFA `pmsafe` adapter computes the coordinate-angle rate

```text
pmr = mu_alpha_star_TDB / cos(delta)
```

in radians per TDB Julian year. It applies no second compatible-system scale factor.
At the exact pole this coordinate-angle representation is singular; the adapter fails
closed or uses a separately approved vector-state route. No numerical pole epsilon is
defined by this decision.

`SOURCE_SUPPORTED_FACT`: SOFA `pmsafe`/`starpm` accept TDB epochs, coordinate-rate
proper motion in right ascension, declination proper motion, parallax, and radial
velocity. `PROJECT_DECISION`: the starred-to-coordinate conversion is isolated at
that boundary and exact-pole input is ineligible for this scalar route.

## Uncertainty and covariance transformation

For the Gaia five-parameter tangent-plane differential vector

```text
q = [delta_alpha_star, delta_delta, parallax,
     mu_alpha_star, mu_delta]
```

UFUQ selects the analytic Jacobian

```text
D = diag(1, 1, K_B, K_B, K_B)
C_TDB = D * C_TCB * transpose(D)
```

`SOURCE_SUPPORTED_FACT`: covariance under a deterministic differentiable parameter
map transforms as `J C J^T`; the scale factors follow the compatible-quantity rules
above. The official Gaia transformation documentation states the same linearized
covariance rule. `PROJECT_DECISION`: this vector order and tangent-plane basis are the
canonical Gaia five-parameter normalization basis.

For a Gaia six-parameter astrometric solution, the sixth catalogue parameter is
pseudocolour rather than a barycentric space/time coordinate. Its compatible-system
map is therefore the explicit six-dimensional extension

```text
q_6 = [delta_alpha_star, delta_delta, parallax,
       mu_alpha_star, mu_delta, pseudocolour]
D_6 = diag(1, 1, K_B, K_B, K_B, 1)
C_6_TDB = D_6 * C_6_TCB * transpose(D_6)
```

`SOURCE_SUPPORTED_FACT`: the Gaia data model defines pseudocolour, its uncertainty,
and its correlations as the additional six-parameter-solution dimension.
`PROJECT_DECISION`: pseudocolour and its standard uncertainty are unchanged by the
compatible-coordinate map, while all covariance elements use their corresponding
`D_6` factor.

Consequently:

- `sigma_alpha_star` and `sigma_delta` are unchanged;
- parallax, `mu_alpha_star`, and `mu_delta` standard uncertainties multiply by `K_B`;
- every covariance element multiplies by the product of its two diagonal factors; and
- Pearson correlation coefficients remain numerically invariant under this positive
  diagonal rescaling, but only when their parameter order/basis is unchanged and the
  target uncertainties/covariance are transformed consistently.

Correlations are not copied as free-standing proof of a target covariance. The
manifest preserves the native errors/correlations and records reconstruction of the
native covariance, `D` or `D_6`, and the target covariance. If the source-neutral V1
state does not consume pseudocolour, its normalization evidence still retains the
full native and normalized six-dimensional covariance and explicitly identifies the
five-dimensional astrometric principal submatrix; it does not condition on, discard,
or pretend never to have solved pseudocolour. Row suitability for that solution class
remains gate C. A later conversion from
`alpha_star` to unstarred right ascension, epoch propagation, or Cartesian coordinates
has a separate Jacobian and must not be folded invisibly into `D`.

For an explicitly constructed Cartesian state `[x, v]`, the compatible-system
Jacobian is `diag(F_B I_3, I_3)`. Gaia's unavailable astrometry-to-RV covariance remains
`UNKNOWN_NOT_PROVIDED`, never zero and never manufactured by this transform.

## Radial-velocity disposition

Gaia publishes a multi-transit spectroscopic radial velocity in the Solar-system
barycentric reference frame. IAU Resolution C1 calls the rigorously corrected
spectroscopic quantity a barycentric radial-velocity measure and warns that it cannot
generally be interpreted unambiguously as physical radial motion. Lindegren and
Dravins distinguish that observational measure from astrometric/kinematic radial
velocity. Gaia's standard astrometric model nevertheless documents that its sixth
space-motion parameter, the radial component, is normally taken from spectroscopy.
That radial space-motion parameter is distinct from a Gaia catalogue “six-parameter
astrometric solution,” whose additional solved dimension is pseudocolour.

The compatible-quantity decision is therefore:

1. preserve the Gaia value and uncertainty unchanged as
   `SpectroscopicBarycentricRadialVelocityMeasure`;
2. never multiply either by `F_B` or `K_B` merely because the astrometry is mapped;
3. never relabel the source field as exact coordinate or systemic velocity;
4. allow a distinct `PropagationRadialVelocity` to copy the numeric value only after
   gate C approves the explicit rule
   `GAIA_SPECTROSCOPIC_RV_PROXY_FOR_STANDARD_SPACE_MOTION_V1` for the named physical
   component; and
5. carry the observational type, source error, proxy rule, component evidence, and
   unbounded spectroscopic-to-kinematic model discrepancy into provenance and the
   error budget.

Items 1-3 are the `PROJECT_DECISION` that closes the compatible-system ambiguity.
Item 4 is `2D_DATA_SELECTION`, so it can reject an individual row without reopening
the generic adapter. Missing or unapproved RV still fails that row closed. Item 5 is
`POST_IMPLEMENTATION_VALIDATION` for its numerical consequence; this task selects no
tolerance.

## SOFA-derived propagation boundary

The normalized `CatalogueIcrsState` supplied to the selected production route has:

- ICRS `alpha` and `delta` unchanged from the approved Gaia native state;
- a source epoch carried as two-part `JD(TDB)` for the same Gaia reference event;
- `mu_alpha_star` and `mu_delta` per TDB Julian year after the one-time `K_B` map;
- TDB-compatible parallax after the one-time `K_B` map;
- a separately approved `PropagationRadialVelocity` in kilometres per second,
  positive-receding as required by the SOFA catalogue interface; and
- the transformed uncertainty/covariance plus complete normalization evidence.

At the `pmsafe`-derived adapter, UFUQ converts units, converts starred-alpha motion to
coordinate-angle motion once, and supplies the TDB source and target epochs. It does
not reapply the compatible-system transform. SOFA's notes sometimes permit neglecting
the TCB/TDB distinction in catalogue observables; UFUQ deliberately does not rely on
that approximation because its type contract requires explicit compatible systems.
This decision does not alter the approved 2C route.

## Typed normalization and provenance contract

2E must keep three states distinct:

```text
GaiaDr3NativeTcbAstrometry
  -> CompatibleQuantityNormalizationEvidence
  -> CatalogueIcrsState (TDB-compatible)
```

The native state preserves:

- release/table/source/component and immutable acquisition identities;
- source parameter values, errors/correlations or covariance, order, basis, and units;
- `sourceEpochLabel = J2016.0`, exact `sourceEpochJd`,
  `sourceTimeScale = TCB`, and `sourceCompatibleSystem = TCB_COMPATIBLE`;
- the spectroscopic RV observational type and its separate uncertainty; and
- source quality, warnings, statuses, and approval.

The normalization evidence requires:

- `normalizationRuleId = GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1` and adapter version;
- exact authority IDs and constants/expressions (`L_B`, `T_0`, `TDB_0`, `F_B`, `K_B`);
- source and target epoch states and the B3 event-conversion identity;
- field-by-field transformation dispositions;
- parameter-vector order/basis, native covariance identity, Jacobian, and target
  covariance identity;
- RV preservation/proxy disposition;
- input/output artifact hashes, warnings, raw statuses, reviewer identity, and
  scientific approval; and
- an explicit one-time-normalization marker that rejects already-normalized input.

The target state carries target values/units, `targetTimeScale = TDB`,
`targetCompatibleSystem = TDB_COMPATIBLE`, target epoch, normalization-evidence ID,
source authority, adapter version, warnings/statuses, and approval. Missing evidence,
mixed source/target fields, repeated normalization, an omitted covariance mapping, or
an unapproved RV proxy fails closed.

## Error-budget and lifecycle consequences

This decision affects AST-006 terms A-001 (position), A-002 (proper motion), A-003
(parallax/distance), A-004 (radial velocity), A-005 (uncertainty/covariance), B-001
(epoch interpretation), B-002 (space-motion model), F-001 (floating-point numerical
implementation), and F-005 (production/reference disagreement). The terms remain
`UNBOUNDED_UNRESOLVED`; the exact analytic map is not a zero uncertainty, a residual,
or a tolerance. Exact Batch 01 guards F-002/F-003/F-004/F-006 support convention and
replay discipline but do not validate this Gaia adapter.

No additional preimplementation numerical experiment is required. 2E must add exact
constant, mapping, covariance, one-time-normalization, and fail-closed tests. After
production exists, the pinned reference path must compare native-to-normalized and
propagated states across representative rows and domains without promoting shared-
SOFA-lineage agreement to independent scientific validation.

## Remaining 2D.1 gates

Closing 2D.1A does not activate Gaia DR3. The remaining gates are:

1. B — immutable Gaia query/response authority;
2. C — row-by-row scientific eligibility and a minimal technical subset, including
   component-specific approval of any spectroscopic-RV proxy;
3. D — Polaris source/component/RV authority; and
4. E — derived-artifact rights interpretation.

## Resource audit

| Resource | Status | Use |
|---|---|---|
| IAU B3/B2/C1, official Gaia DR3 model/data documentation, and the Klioner/Lindegren-Dravins primary papers | `OFFICIAL_WEB_SUFFICIENT` | Sufficient to define the epoch, compatible quantities, covariance, and RV-type boundary. |
| Pinned local IAU SOFA `2023-10-11` source and routine preambles | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient to type the selected propagation interface and statuses; read-only. |
| *Fundamental Astronomy*, another book/manual, or bulk Gaia rows | `NOT_NEEDED` | The analytic adapter does not require another secondary source or catalogue acquisition. |

`USER_ACTION_REQUIRED`: none. Row, query, Polaris, and rights work remains under gates
B-E, but no new document or data download is needed to close adapter A.

## Sources

- IAU, [2006 Resolution B3: Re-definition of TDB](https://www.iau.org/static/resolutions/IAU2006_Resol3.pdf).
- IAU, [2012 Resolution B2: re-definition of the astronomical unit](https://www.iau.org/static/resolutions/IAU2012_English.pdf).
- IAU, [2000 Resolution C1: definition of a spectroscopic barycentric radial-velocity measure](https://www.iau.org/static/resolutions/IAU2000_French.pdf).
- ESA/DPAC, Gaia DR3 documentation release 1.3: [reference systems and time scales](https://gea.esac.esa.int/archive/documentation/GDR3/Data_processing/chap_cu3ast/sec_cu3ast_intro/ssec_cu3ast_intro_refsystems.html), [standard model of stellar motion](https://gea.esac.esa.int/archive/documentation/GDR3/Data_processing/chap_cu3ast/sec_cu3ast_intro/ssec_cu3ast_intro_motion.html), [transformations and covariance propagation](https://gea.esac.esa.int/archive/documentation/GDR3/Data_processing/chap_cu3ast/sec_cu3ast_intro/ssec_cu3ast_intro_tansforms.html), and [`gaiadr3.gaia_source`](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html).
- Klioner (2008), [*Relativistic scaling of astronomical quantities and the system of astronomical units*](https://doi.org/10.1051/0004-6361:20077786).
- Klioner et al. (2010), [*Units of relativistic time scales and associated quantities*](https://doi.org/10.1051/0004-6361/200913090).
- Lindegren and Dravins (2003), [*The fundamental definition of radial velocity*](https://doi.org/10.1051/0004-6361:20030181).
- IAU SOFA issue `2023-10-11`, local official `tcbtdb.c`, `tdbtcb.c`, `epj.c`,
  `epj2jd.c`, `pmsafe.c`, `starpm.c`, `starpv.c`, and `pvstar.c` routine preambles and
  sources, inspected read-only.
