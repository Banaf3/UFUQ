# Phase 1 Milestone 2C: Scientific Behaviour Contract

## Status

Draft for review.

This document defines the scientific behaviour that must be approved before UFUQ
implements production astronomy. It does not authorize catalogue parsing,
source-derived tracked artifacts, learner-facing cultural claims, or deployment.

## 1. Purpose

Define the normative behaviour for transforming approved catalogue astrometry into
observer-local directions while keeping scientific calculation, visibility, scene
mapping, and learner scoring separate.

## 2. Scope

This milestone covers:

- coordinate states and transformation boundaries;
- reference frames, epochs, units, and time scales;
- proper-motion handling;
- observer location and geodetic conventions;
- Earth-orientation and leap-second data;
- azimuth and altitude conventions;
- refraction and horizon behaviour;
- supported date range;
- structured warnings and errors;
- scientific error budgeting;
- independent reference-test requirements.

This milestone does not implement:

- the I/311 catalogue parser;
- generated catalogue artifacts;
- production astronomy code;
- cultural memberships or lesson routes;
- the Three.js scene;
- learner scoring or Bayesian Knowledge Tracing;
- persistence, accounts, or deployment.

## 3. Normative coordinate pipeline

The intended typed pipeline is:

```text
catalogue astrometry at a declared frame and epoch
-> approved space-motion propagation
-> celestial intermediate transformation
-> Earth rotation and terrestrial orientation
-> observer-dependent geometric horizontal direction
-> optional refracted direction
-> separately defined visibility result
-> separately defined scene mapping
```

Every stage must declare its frame, epoch or observation time, units, convention,
status, and provenance.

## 4. Catalogue frame and epoch

### 4.1 Catalogue frame

Candidate decision:

- treat the selected CDS I/311 astrometry as ICRS catalogue astrometry according to
  the approved source-field contract.

This must be confirmed against the recorded source evidence before becoming normative.

### 4.2 Catalogue epoch

Known source value:

- catalogue epoch value: `1991.25`.

Open decision:

- the exact time-scale interpretation of the I/311 epoch;
- whether UFUQ may treat it as Julian epoch `J1991.25`;
- the evidence required before production propagation.

No implementation may silently infer the epoch time scale.

## 5. Proper motion

The I/311 `pmRA` source field represents the starred right-ascension component:

```text
mu_alpha_star = mu_alpha * cos(delta)
```

The normalized field must preserve that meaning explicitly.

When using Astropy, the value maps directly to:

```text
pm_ra_cosdec
```

No additional cosine multiplication or division is permitted.

Required tests include:

- correct high-declination handling;
- omitted-cosine failure case;
- double-cosine failure case;
- catalogue-epoch identity case;
- nonzero elapsed-time propagation case.

## 6. Space-motion inputs

The contract must explicitly decide how UFUQ handles:

- right ascension and declination;
- proper motion in right ascension and declination;
- parallax;
- radial velocity;
- missing or invalid source values;
- uncertainty and correlation information;
- supplemental solution types.

No effect may be assumed merely because a selected library supports it.

## 7. Time scales

The public input time, internal time scales, and conversions must be explicit.

Required distinctions:

- UTC for external civil-time input;
- TAI for atomic-time continuity;
- TT for precession-nutation and related celestial models;
- UT1 for Earth rotation.

UTC must not silently replace TT or UT1.

Open decisions:

- accepted input format and precision;
- leap-second handling;
- dubious-date behaviour;
- missing-UT1 behaviour;
- whether warnings are returned or promoted to errors.

## 8. Earth-orientation and IERS policy

The contract must name:

- the Earth-orientation data source;
- exact package and file versions;
- file hashes;
- supported coverage range;
- predictive-data policy;
- network policy;
- offline behaviour;
- missing-data behaviour;
- out-of-range behaviour.

Automatic downloads must not occur during ordinary deterministic execution.

Open decision:

- whether out-of-range execution fails closed or permits a separately approved,
  explicitly bounded degraded mode.

## 9. Observer contract

Observer input must explicitly include:

- geodetic latitude;
- longitude;
- longitude sign convention;
- geodetic datum;
- observer height;
- height type;
- validation limits.

Candidate convention:

- datum: WGS 84;
- longitude: east-positive;
- latitude range: `[-90 degrees, +90 degrees]`;
- longitude normalized to a documented interval;
- height expressed in metres above the selected reference ellipsoid.

These candidates require approval before becoming normative.

## 10. Horizontal-coordinate convention

Candidate UFUQ convention:

### 10.1 Azimuth

```text
0 degrees   = north
90 degrees  = east
180 degrees = south
270 degrees = west
```

Azimuth increases eastward and is normalized to `[0 degrees, 360 degrees)`.

### 10.2 Altitude

```text
+90 degrees = zenith
0 degrees   = geometric horizon
-90 degrees = nadir
```

Open decisions:

- behaviour at the zenith, where azimuth may be undefined;
- numerical normalization near `0 degrees` and `360 degrees`;
- returned status for degenerate directions.

## 11. Geometric and refracted direction

The system must represent geometric and refracted directions as different states.

Open decisions:

- whether the Phase 2 slice uses geometric altitude only;
- atmospheric pressure, temperature, humidity, and wavelength inputs;
- default-atmosphere policy;
- low-altitude validity limit;
- behaviour below the geometric horizon;
- whether refraction failure produces an error, warning, or unavailable result.

Scene code must not silently apply refraction.

## 12. Horizon and visibility

Astronomical direction, horizon classification, visibility, and rendering are separate.

The contract must distinguish:

- geometric altitude;
- refracted altitude;
- geometric above-horizon or below-horizon state;
- project-defined visibility state;
- terrain or obstruction handling;
- renderer clipping and presentation choices.

A rendered star must not be treated as evidence of scientific visibility.

## 13. Included and omitted effects

The final production pipeline must identify every included and omitted effect.

Candidate effects to evaluate:

- proper motion;
- parallax;
- radial velocity;
- frame bias;
- precession-nutation;
- annual aberration;
- light deflection;
- Earth rotation;
- polar motion;
- diurnal aberration;
- atmospheric refraction.

Each selected effect must have a named authority, implementation path, input contract,
and validation case.

## 14. Structured errors, warnings, and statuses

The production API must preserve structured scientific outcomes.

Candidate categories:

- invalid input;
- unsupported date;
- unavailable Earth-orientation data;
- dubious time;
- incomplete source astrometry;
- propagation warning;
- numerical failure;
- valid geometric result;
- valid refracted result;
- refraction unavailable.

Warnings from the independent reference implementation must not be silently discarded.

## 15. Scientific error budget

The error budget must keep these sources separate:

- catalogue uncertainty;
- source-field uncertainty and correlation;
- propagation-model uncertainty;
- Earth-orientation uncertainty;
- reference-algorithm disagreement;
- floating-point and serialization effects;
- scene-coordinate error;
- learner-response tolerance.

Scientific acceptance tolerance must not be reused as learner scoring tolerance.

No final threshold is approved by this draft.

## 16. Required independent reference cases

The comparison suite should eventually cover:

- catalogue-epoch identity;
- nonzero proper motion;
- high-declination `mu_alpha_star`;
- omitted-cosine and double-cosine failures;
- zero and nonzero parallax;
- zero and nonzero radial velocity;
- UTC boundaries and leap-second-adjacent cases;
- nonzero UT1-UTC and polar motion;
- eastern and western longitudes;
- meridian crossing;
- azimuth wrapping;
- horizon crossing;
- zenith and nadir;
- invalid latitude, longitude, height, and time;
- unavailable or out-of-range IERS data;
- geometric versus refracted output.

Fixtures must declare all units, frames, time scales, conventions, source versions,
and expected statuses.

## 17. Decision record requirements

Every approved behaviour must record:

- decision identifier;
- authoritative evidence;
- selected behaviour;
- rejected alternatives;
- implementation consequence;
- validation consequence;
- unresolved limitation;
- reviewer and approval status.

## 18. Open decisions blocking production implementation

- I/311 epoch time-scale interpretation.
- Exact production transformation pipeline.
- Included and omitted astrometric effects.
- Leap-second and Earth-orientation policy.
- Supported date range.
- Observer datum and height definition.
- Refraction policy.
- Horizon and visibility policy.
- Warning and error mapping.
- Scientific error-budget methodology.
- Production/reference acceptance tolerances.

## 19. Exit criteria

Milestone 2C is complete only when:

- each blocking decision is approved or explicitly deferred with consequences;
- frames, epochs, units, time scales, and conventions are normative;
- included and omitted effects are recorded;
- observer and IERS policies are recorded;
- structured error behaviour is defined;
- the independent test matrix is approved;
- scientific, rendering, and learner tolerances remain separate;
- no catalogue parser or production implementation is presented as approved.
