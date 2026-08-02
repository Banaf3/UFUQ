# Phase 1 Milestone 2C: Scientific Behaviour Contract

## Status and verdict

**Evidence audit date:** 2026-08-03

**Milestone status:** OPEN

**Implementation authority:** NOT GRANTED

The tracked source dossiers and project decisions support a stricter contract than the
earlier draft, but they do not close the manual scientific decisions needed for
production astronomy. This audit resolves source-defined input semantics, fixed UFUQ
coordinate conventions, typed state separation, and reference-test requirements. It
does not select a production transformation algorithm, effect matrix, date range,
Earth-orientation policy, observer datum/height policy, refraction or visibility
policy, error aggregation, or numerical tolerance.

No astronomy reviewer or owner approval is recorded for those open choices. Milestone
2C therefore remains open and `IMP-009` remains unresolved.

This document does not authorize catalogue parsing, source-derived tracked artifacts,
learner-facing cultural claims, or deployment.

## 1. Purpose

Define the normative behaviour for transforming approved catalogue astrometry into
observer-local directions while keeping scientific calculation, visibility, scene
mapping, and learner scoring separate. It also records which conclusions are already
supported, which are project choices, and which must stop before implementation.

## 2. Scope and evidence classes

This milestone covers:

- coordinate states and transformation boundaries;
- reference frames, epochs, units, and time scales;
- proper-motion and space-motion inputs;
- observer location and geodetic conventions;
- Earth-orientation and leap-second data;
- azimuth and altitude conventions;
- refraction, horizon, and visibility boundaries;
- supported date range and failure behaviour;
- scientific error budgeting; and
- independent reference-test requirements.

This milestone does not implement:

- the I/311 catalogue parser or generated catalogue artifacts;
- production astronomy code or a production/reference comparison;
- cultural memberships or lesson routes;
- the Three.js scene;
- learner scoring or Bayesian Knowledge Tracing; or
- persistence, accounts, or deployment.

The classifications used below are:

- `SOURCE_SUPPORTED_FACT`: the cited external authority defines the input, algorithm
  role, or convention;
- `PROJECT_DECISION`: an existing tracked UFUQ decision fixes behaviour within project
  scope;
- `PROVISIONAL_CHOICE`: a bounded spike choice that cannot be promoted to production;
- `UNRESOLVED_QUESTION`: missing evidence, experiment, approval, or policy blocks only
  the affected behaviour.

Primary evidence for this audit is:

- IAU SOFA issue `2023-10-11`, exact studied routine contracts;
- IERS Conventions (2010) TN36 `v1.0.0`, with later corrections kept separate;
- CDS/VizieR I/311 `ReadMe` and official Appendix G Tables G.2-G.7;
- ESA SP-1200 Volume 1 for original-catalogue semantic support only;
- van Leeuwen's 2007 validation article for error-characteristic context only;
- `docs/ASTRONOMY_SPEC.md`, ADR-003, ADR-007, and the repository astronomy
  validation skill; and
- the locked synthetic-only Astropy smoke oracle, within its explicitly limited claim.

The local *Explanatory Supplement* candidate supplies no claim-level evidence because
its tracked dossier marks it text-unavailable, incomplete, and provenance-unverified.

## 3. Normative coordinate-state boundaries

The following separation is a `PROJECT_DECISION` and is normative:

```text
I/311 catalogue astrometry at its declared frame and source epoch label
-> approved space-motion propagation
-> approved celestial intermediate transformation
-> approved Earth rotation and terrestrial orientation
-> observer-dependent geometric horizontal direction
-> optional, separately labelled refracted direction
-> separately defined horizon/visibility result
-> separately defined scene mapping
```

Every implemented stage must declare its input and output state, frame, epoch or
observation time, units, convention, status, and policy/provenance identifier. An
immutable catalogue row must never be overwritten with observed, horizontal,
refracted, visibility, or scene values.

This separation does not select the exact production routines, transform route, or
included effects. Those remain blocked under `2C-008`.

## 4. Catalogue frame and epoch

### 4.1 I/311 input frame

`SOURCE_SUPPORTED_FACT`:

- the selected I/311 `RArad` and `DErad` fields are ICRS catalogue astrometry;
- their source units are radians; and
- ICRS frame identity does not remove the need for a reference epoch for a moving
  star.

UFUQ must preserve `ICRS` as source metadata and in every normalized record and
fixture. Calling these values merely "J2000 coordinates" is prohibited because that
would conflate frame, epoch, equinox/origin, and time scale.

### 4.2 I/311 source epoch label

`SOURCE_SUPPORTED_FACT`:

- I/311 labels the catalogue astrometry with `Ep=1991.25`.

`UNRESOLVED_QUESTION`:

- the inspected I/311-specific evidence does not state the time scale needed to turn
  that label into an exact propagation instant;
- ESA SP-1200 defines the original 1997 catalogue epoch as `J1991.25(TT)`, but that
  statement must not be transferred silently to the later I/311 reduction; and
- no production propagation may call the I/311 epoch `J1991.25(TT)` until an
  I/311-applicable authority or reviewed decision supports it.

Until resolved, the parser contract may preserve the literal source epoch label, but
source-derived propagation from that epoch is blocked.

## 5. Proper motion

The following is `SOURCE_SUPPORTED_FACT` plus an existing `PROJECT_DECISION`:

```text
I/311 pmRA = mu_alpha_star = (d alpha / dt) * cos(delta)
```

The normalized field is
`properMotionRaCosDecMilliarcsecondsPerYear`. It maps directly, after unit conversion,
to Astropy's `pm_ra_cosdec`; no additional multiplication or division by
`cos(delta)` is permitted for that interface.

A different library interface must be audited independently. In particular, SOFA
`iauPmsafe` expects the coordinate-angle rate `dRA/dt`, so the I/311 normalized field
must not be passed to it unchanged.

Required future comparison cases include:

- high-declination handling;
- omitted-cosine and double-cosine failures;
- source-epoch identity;
- positive and negative RA proper motion; and
- nonzero elapsed-time propagation.

The component mapping is resolved. The production space-motion model and the numerical
acceptance threshold are not.

## 6. Space-motion and source-quality contract

The Milestone 2B parser contract preserves the source fields and evidence. Milestone
2C must not convert that preservation requirement into an unapproved physical model.

| Input/effect | Resolved contract | Still blocked |
|---|---|---|
| Right ascension and declination | Preserve ICRS source values, units, epoch label, and provenance. | Exact production propagation and downstream frame path. |
| `pmRA` and `pmDE` | Preserve both; `pmRA` is explicitly the starred-alpha component. | Target-library mapping other than the reviewed Astropy field; production motion model. |
| Parallax | Preserve the estimate, including a finite negative value; do not reinterpret a negative estimate as missing. | Include/omit decision, distance handling, uncertainty propagation, and failure policy. |
| Radial velocity | Do not synthesize a value or silently substitute zero. | Approved source, missing-value behaviour, perspective-acceleration policy, and omission bound. |
| Formal errors and `UW` | Preserve the recorded uncertainties and weight/covariance evidence. | Covariance reconstruction/use, conditioning policy, propagation, and reviewed omission bound. |
| Solution/multiplicity/quality evidence | Preserve `Sn`, supplements, multiplicity/component, fit, rejection, variability, and related evidence under Milestone 2B. | Scientific suitability of each selected row and effect handling for non-five-parameter solutions. |

Any missing or unsupported input that the approved production model requires must
produce an explicit unavailable/error outcome. Library defaults are not scientific
decisions.

## 7. Time contract

### 7.1 Fixed roles

The following roles are `SOURCE_SUPPORTED_FACT` and normative for the contract:

- UTC represents the external civil-time instant;
- TAI supplies atomic-time continuity in the conversion chain;
- TT supplies the time argument for the selected precession-nutation model; and
- UT1 supplies Earth rotation.

UTC must not silently replace TT or UT1. Every two-part Julian Date or equivalent
value must retain its time-scale label.

The existing UFUQ `PROJECT_DECISION` requires an ISO 8601 input with an explicit offset
or an approved IANA zone, resolved to UTC while retaining the original zone/offset for
display and audit.

### 7.2 Open operational choices

The following remain `UNRESOLVED_QUESTION` under AST-003/AST-007:

- accepted input precision and exact serialization;
- approved IANA zones and ambiguous/nonexistent local-time handling;
- leap-second input and data-update behaviour;
- SOFA/Astropy dubious-date warning policy;
- missing `UT1-UTC` behaviour; and
- stable API warning/error mapping.

## 8. Earth-orientation and oracle-data policy

The production contract must name and hash:

- the IERS baseline, any separately selected corrections, and the exact EOP product;
- `UT1-UTC`, `xp`, `yp`, and any celestial-pole-offset policy;
- leap-second source and file;
- package and file versions/hashes;
- observed and predictive coverage;
- network, cache, automatic-download, and update behaviour;
- missing, expired, predictive, and out-of-range behaviour; and
- any separately approved degraded approximation and its measured bound.

Ordinary deterministic execution must record and obey an explicit network/update
policy. Whether production permits any automatic download is part of the unresolved
AST-003 decision.

### 8.1 Evidence already established by the synthetic smoke oracle

The tracked smoke oracle pins CPython `3.14.6`, uv `0.11.32`, Astropy `8.0.1`, PyERFA
`2.0.1.5`, and `astropy-iers-data` `0.2026.7.20.15.31.18`. Its environment manifest
records hashes and coverage for packaged `finals2000A.all` and `Leap_Second.dat`. Smoke
execution disables automatic downloads and general Astropy internet access, blocks
socket connections, uses a fresh temporary cache, and treats degraded IERS accuracy as
an error.

This is `PROVISIONAL_CHOICE` evidence for environment reproducibility only. It does not
approve those files, coverage dates, predictive rows, or failure rules for production.
The source register also still lacks the exact official Astropy/PyERFA documentation
pins used to justify a source-derived science protocol.

### 8.2 Production stop condition

Production execution is blocked until the final data selection, coverage, update,
offline, extrapolation, and failure policy is approved. Out-of-range operation must
fail explicitly unless a separately labelled degraded mode has a quantified bound and
approval.

## 9. Observer contract

Every observer input must explicitly include:

- geodetic latitude;
- east-positive longitude;
- datum/ellipsoid identifier;
- height in metres;
- height type/datum; and
- input provenance and validation status.

Resolved `PROJECT_DECISION`:

- latitude is north-positive and longitude is east-positive;
- latitude must be finite and within `[-90 degrees, +90 degrees]`; and
- observer fields may not be an unlabelled tuple.

`UNRESOLVED_QUESTION`:

- whether production uses WGS 84;
- ellipsoidal versus orthometric/source height and any conversion;
- allowed height range and below-ellipsoid handling;
- the canonical longitude interval and wrap representative;
- polar-site longitude/azimuth semantics;
- whether height contributes to topocentric parallax, horizon dip, or both; and
- approved scenario coordinates and their authority.

WGS 84 and ellipsoidal height in the synthetic smoke fixtures are bounded fixture
choices, not production approval.

## 10. Horizontal-coordinate convention

The following existing `PROJECT_DECISION` is normative.

### 10.1 Azimuth

```text
0 degrees   = geographic True North
90 degrees  = east
180 degrees = south
270 degrees = west
```

Azimuth increases eastward/clockwise and ordinary defined azimuths are normalized to
`[0 degrees, 360 degrees)`.

### 10.2 Altitude

```text
+90 degrees = zenith
0 degrees   = geometric horizon
-90 degrees = nadir
```

At the zenith or nadir, the direction and altitude may remain valid but azimuth is
undefined. A result must preserve that singular status and must not manufacture an
arbitrary azimuth. Direction comparisons near the singularity use unit-vector angular
separation, not azimuth difference.

The exact serialized representative at the `0/360` wrap, negative-zero handling, and
stable status code remain part of the unresolved API/numerical contract.

## 11. Geometric and refracted states

`PROJECT_DECISION`:

- geometric and refracted direction are distinct states;
- catalogue or geometric altitude must not be relabelled as refracted altitude; and
- scene code must not silently apply refraction.

`UNRESOLVED_QUESTION` under AST-004:

- whether the Phase 2 slice uses geometric altitude only;
- atmospheric pressure, temperature, humidity, and wavelength inputs;
- default-atmosphere policy;
- model and low-altitude validity range;
- behaviour below the geometric horizon; and
- whether unavailable/invalid refraction is an error, warning, or unavailable
  optional result.

The synthetic smoke oracle uses pressure zero. That proves the bounded geometric path
runs; it does not select the production refraction policy.

## 12. Horizon, visibility, and rendering

The following separation is a `PROJECT_DECISION`:

- geometric altitude;
- optional refracted altitude;
- geometric horizon classification;
- project-defined visibility;
- terrain/obstruction handling; and
- renderer clipping/presentation.

A rendered star is not evidence of astronomical visibility. `Hp` is not Johnson `V`,
and neither is by itself a claim about unaided visibility.

The exact horizon boundary, equality rule at zero altitude, terrain/horizon dip,
photometric filter, variability, extinction, weather, light-pollution, below-horizon
teaching, and visibility statuses remain blocked under AST-004.

## 13. Production effect matrix

The production implementation must record an implement-or-omit decision, input
contract, authority/routine, validation case, and quantified omission bound for every
applicable effect:

| Effect | Evidence-backed role | Milestone 2C decision status |
|---|---|---|
| Proper motion | Catalogue-to-observation propagation input. | `UNRESOLVED_QUESTION` for production inclusion/model. |
| Parallax/topocentric parallax | Distance and observer-dependent direction effect. | `UNRESOLVED_QUESTION`. |
| Radial velocity/perspective acceleration | Space-motion input where supported and material. | `UNRESOLVED_QUESTION`. |
| Frame bias | Part of a named ICRS/GCRS path such as the studied SOFA chain. | `UNRESOLVED_QUESTION`. |
| Precession-nutation | TT-dependent celestial orientation. | `UNRESOLVED_QUESTION` for exact model/routine. |
| Annual aberration | Barycentric/geocentric apparent-place effect. | `UNRESOLVED_QUESTION`. |
| Light deflection | Apparent-place effect in the studied SOFA chain. | `UNRESOLVED_QUESTION`. |
| Earth rotation | UT1-dependent celestial/terrestrial orientation. | Required role is source-supported; exact route/data policy is unresolved. |
| Polar motion and celestial-pole offsets | Realized Earth orientation from pinned EOP data. | `UNRESOLVED_QUESTION`. |
| Diurnal aberration | Observer-dependent observed-place effect. | `UNRESOLVED_QUESTION`. |
| Atmospheric refraction | Optional meteorology/wavelength-dependent observed effect. | `UNRESOLVED_QUESTION` under AST-004. |

The presence of an effect in SOFA or Astropy does not select it for UFUQ. No omission
may be called negligible without a bound over the approved date/location/source range.

## 14. Structured outcomes

The API must return a discriminated scientific outcome rather than a bare coordinate
or silently coerced fallback. At minimum, the design must distinguish:

- invalid input;
- unsupported date or observer;
- unavailable/expired/out-of-range Earth-orientation data;
- dubious time or predictive-data warning;
- incomplete/unsupported source astrometry;
- propagation warning or numerical failure;
- valid geometric direction, including singular azimuth state;
- valid refracted direction; and
- refraction unavailable.

Upstream SOFA, Astropy, PyERFA, and IERS warnings/errors used by the approved path must
be retained in evidence and deliberately mapped. They must not be discarded because a
numeric output was also returned.

The requirement for structured outcomes is a `PROJECT_DECISION`. Exact stable status
codes, severity, API serialization, warning promotion, and retry/fallback behaviour are
`UNRESOLVED_QUESTION`.

## 15. Scientific error budget and comparison metrics

Resolved `PROJECT_DECISION` requirements:

- compare directions with robust unit-vector great-circle separation;
- compare headings with wrapped circular distance;
- report component residuals as well as total angular separation;
- keep implementation numerics, scientific/reference acceptance, rendering error,
  and learner-answer tolerance separate; and
- fail as unconfigured when a required threshold is absent.

Each approved case must report, where applicable:

- catalogue position and space-motion uncertainty, including correlation policy;
- source-field and supplemental-solution uncertainty;
- omitted-effect bound;
- Earth-orientation/leap-second uncertainty and data status;
- observer-coordinate/datum/height uncertainty;
- reference-algorithm and implementation disagreement;
- floating-point and serialization effects;
- scene-coordinate error; and
- learner-response tolerance as a separate educational/assessment quantity.

No aggregation rule or final threshold is approved. Catalogue formal errors, SOFA
accuracy prose, the van Leeuwen aggregate results, smoke-fixture byte identity, and a
visually plausible sky are not UFUQ acceptance tolerances.

## 16. Independent reference protocol

The repository requires a neutral versioned JSON fixture protocol. Each scientific
fixture must contain exact inputs, policies, software/data versions, hashes,
provenance, expected outputs, warnings/statuses, and intended comparisons.

The independently authored Python/Astropy producer must:

- import no production UFUQ package;
- invoke no Node astronomy implementation;
- avoid mechanically translating the selected TypeScript algorithm;
- run with locked dependencies and explicit IERS/leap-second files;
- fail on prohibited network/data fallback under the approved offline policy; and
- keep source-derived fixtures out of Git unless the applicable source authority
  permits them.

The tracked synthetic-only oracle satisfies the environment/independence smoke claim:
it uses a neutral versioned envelope, contains no catalogue identity, imports no
production package, and has byte-identical deterministic output. It is not a
source-derived scientific fixture and cannot activate `test:reference`.

The future scientific comparison matrix must cover:

- I/311 source-epoch identity after the epoch time scale is resolved;
- nonzero/high proper motion and high-declination cosine guards;
- zero, negative, and nonzero parallax under the selected policy;
- zero/nonzero/missing radial velocity under the selected policy;
- UTC boundaries, approved leap-second behaviour, and alternative Julian-date splits;
- nonzero `UT1-UTC`, `xp`, and `yp`;
- meridian, east/west, and azimuth-wrap cases;
- geometric horizon crossing and below-horizon cases;
- zenith/nadir singularities;
- supported-range endpoints and just-outside endpoints;
- invalid latitude, longitude, height, time, and source astrometry;
- unavailable, predictive, expired, and out-of-range IERS data; and
- geometric versus refracted output if refraction is included.

No case may be accepted on an average that hides an individual failure.

## 17. Evidence and decision audit

| ID | Claim/decision | Classification and evidence | Audit result |
|---|---|---|---|
| `2C-001` | Keep catalogue, propagated, celestial-intermediate, geometric horizontal, refracted, visibility, and scene states distinct. | `PROJECT_DECISION`: Astronomy Specification, ADR-003, architecture/data strategy. | `RESOLVED_CONTRACT`. |
| `2C-002` | Treat selected I/311 `RArad`/`DErad` as ICRS catalogue inputs in radians. | `SOURCE_SUPPORTED_FACT`: I/311 `ReadMe`, `hip2.dat` byte description. | `RESOLVED_INPUT_SEMANTICS`. |
| `2C-003` | Interpret `Ep=1991.25` as an exact propagation instant/time scale. | I/311 supplies only the label; ESA's `J1991.25(TT)` applies directly to the original catalogue. | `BLOCKED_EVIDENCE_AND_APPROVAL`; preserve the label only. |
| `2C-004` | Interpret I/311 `pmRA` as `mu_alpha_star` and normalize explicitly. | `SOURCE_SUPPORTED_FACT`: I/311 Appendix G Table G.3; project field-name decision. | `RESOLVED_INPUT_SEMANTICS`; production motion model remains open. |
| `2C-005` | Keep UTC, TAI, TT, and UT1 distinct with TT for precession-nutation and UT1 for Earth rotation. | `SOURCE_SUPPORTED_FACT`: SOFA routine contracts; IERS TN36 Chapters 5 and 10. | `RESOLVED_TIME_ROLES`; operational data/failure policy remains open. |
| `2C-006` | Use north-positive latitude, east-positive longitude, north-zero/eastward azimuth, signed altitude, and vector comparison at zenith/nadir. | `PROJECT_DECISION`: Astronomy Specification and ADR-003; SOFA supports the horizon convention. | `RESOLVED_CONVENTIONS`; exact serialization/status code remains open. |
| `2C-007` | Select datum/ellipsoid, height semantics/range, longitude representative, and approved observer locations. | Sources require explicit inputs but do not select UFUQ values. | `BLOCKED_PROJECT_DECISION` under AST-003/AST-007. |
| `2C-008` | Select the production algorithm/library, coherent CIO/equinox route, and implement-or-omit effect matrix. | SOFA/IERS define candidate algorithms and roles, not the UFUQ selection. | `BLOCKED_PROJECT_DECISION_AND_EXPERIMENT` under AST-003. |
| `2C-009` | Select production leap-second/EOP files, coverage, predictive/offline/update policy, and approximation/failure modes. | Smoke files/hashes are pinned only for a bounded synthetic oracle. | `BLOCKED_PROJECT_DECISION`; official tool-documentation pins also remain incomplete. |
| `2C-010` | Keep geometric and refracted direction separate; select the Phase 2 refraction model/policy. | Separation is a `PROJECT_DECISION`; SOFA shows required meteorological inputs and limitations. | Separation resolved; policy `BLOCKED_PROJECT_DECISION` under AST-004. |
| `2C-011` | Keep direction, horizon, visibility, and rendering separate; select actual visibility/horizon behaviour. | Separation is a `PROJECT_DECISION`; no source/owner has selected the policy. | Separation resolved; policy `BLOCKED_PROJECT_DECISION` under AST-004. |
| `2C-012` | Preserve structured scientific outcomes and upstream warnings; fix stable API mapping. | SOFA status contracts plus ADR-003/007. | Requirement resolved; exact mapping `BLOCKED_PROJECT_DECISION`. |
| `2C-013` | Use per-case vector/circular metrics and a separated error budget; approve aggregation and tolerances. | Astronomy Specification/ADR-007 plus independent-measurement requirement. | Metrics resolved; budget aggregation and thresholds `BLOCKED_EXPERIMENT_AND_APPROVAL` under AST-006. |
| `2C-014` | Establish an independent, pinned scientific oracle and comparison matrix. | Locked synthetic-only oracle proves environment/independence smoke; it supplies no production comparison. | `PARTIAL`; source-derived fixtures and comparison remain unstarted. |
| `2C-015` | Select supported date/location/altitude range and endpoint failures. | Sources expose model/data limits but do not select UFUQ scope. | `BLOCKED_PROJECT_DECISION` under AST-003/AST-007. |

## 18. Decisions still blocking implementation

### 18.1 Evidence gaps

- I/311-applicable evidence or approved interpretation for the exact `Ep=1991.25`
  propagation time scale;
- pinned official Astropy coordinate/time/IERS documentation for the selected science
  protocol, plus the matching PyERFA documentation record;
- a selected and hashed production EOP/leap-second dataset and supported coverage;
- source-derived independent cases after catalogue-processing authority permits them;
- measured effect/omission sensitivity and production/reference disagreement; and
- a per-case scientific error budget.

### 18.2 Manual scientific/project decisions

- AST-003: production routine/library/path, effect matrix, date range, observer datum
  and height semantics, time/EOP/leap-second policy, and failure/degraded modes;
- AST-004: refraction, horizon, below-horizon, photometric, and visibility policy;
- AST-006: error aggregation and operation-specific scientific/reference tolerances;
- AST-007: supported observer/time scenario inputs and boundary semantics; and
- exact structured status/error/warning serialization for the production contracts.

These decisions require the authority, reviewer, approval status/date, rejected
alternatives, implementation consequence, validation consequence, and limitations
specified by the repository governance records. This audit is not a substitute for
that approval.

## 19. Exit criteria and current outcome

Milestone 2C is complete only when:

- every blocking decision above is approved or explicitly deferred with a consequence
  that removes the affected behaviour from the implemented scope;
- the I/311 epoch has an approved propagation interpretation or source-derived
  propagation is explicitly unavailable;
- the production algorithm/effect matrix, supported range, observer policy, and
  leap-second/EOP policy are normative;
- structured warning/error and singular-result behaviour is defined;
- the independent scientific fixture protocol and case matrix are approved;
- the error-budget method and scientific/reference thresholds are approved;
- scientific, rendering, and learner tolerances remain separate; and
- no catalogue parser or production implementation is presented as approved by this
  document.

**Current outcome:** the contract is evidence-audited but not approved for production.
Milestone 2C remains **OPEN**.
