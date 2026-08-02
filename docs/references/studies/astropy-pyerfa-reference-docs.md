# Astropy and PyERFA reference-documentation pin

## Scope and identity

- Source IDs: `ASTROPY-DOCS-PIN` and `PYERFA-PIN`.
- Retrieval date: 2026-08-03.
- Runtime under review: Astropy `8.0.1`, PyERFA `2.0.1.5`, ERFA `2.0.1`, and
  SOFA `20231011`, as locked by `tools/astronomy-reference/uv.lock` and reported by
  the workspace-local oracle environment.
- Scope: time representation and scale, space-motion propagation, Earth-orientation
  data status, and preservation of ERFA warnings/errors for a future independent
  reference implementation.
- Out of scope: selecting the production astronomy algorithm, approving the I/311
  epoch time scale, choosing production EOP data, or setting a tolerance.

## Official Astropy 8.0.1 documentation

The following official pages displayed Astropy `8.0.1` when retrieved. The `stable`
URL is recorded with the displayed version and retrieval date because the alias can
move to a later release.

| Page | Required use |
|---|---|
| [`Time`](https://docs.astropy.org/en/stable/api/astropy.time.Time.html) and the [`astropy.time` guide](https://docs.astropy.org/en/stable/time/index.html) | Require an explicit time format and scale; distinguish `jyear`, `byear`, and `decimalyear`. |
| [`TimeJulianEpoch`](https://docs.astropy.org/en/stable/api/astropy.time.TimeJulianEpoch.html) | Defines Astropy `jyear`: a Julian year is exactly 365.25 days, with `J2000.0` anchored at 2000-01-01 12:00 TT. |
| [`TimeBesselianEpoch`](https://docs.astropy.org/en/stable/api/astropy.time.TimeBesselianEpoch.html) | Defines Astropy `byear` as a separate representation. |
| [`TimeDecimalYear`](https://docs.astropy.org/en/stable/api/astropy.time.TimeDecimalYear.html) | Defines calendar decimal year using the actual 365- or 366-day year; it is not `jyear`. |
| [`SkyCoord`](https://docs.astropy.org/en/stable/api/astropy.coordinates.SkyCoord.html) and [Accounting for Space Motion](https://docs.astropy.org/en/stable/coordinates/apply_space_motion.html) | Defines `obstime`, `pm_ra_cosdec`, and `apply_space_motion`; the propagation uses the coordinate's initial `obstime` and assumes linear space motion. The guide states that absent radial velocity is treated as zero. |
| [Transforming between systems](https://docs.astropy.org/en/stable/coordinates/transforming.html) | Defines the `transform_to` route used to move an explicitly constructed coordinate into the selected output frame; it does not itself select UFUQ's route. |
| [`EarthLocation`](https://docs.astropy.org/en/stable/api/astropy.coordinates.EarthLocation.html) | Defines named geodetic longitude, latitude, and height input, east-positive longitude, and reference-ellipsoid handling required by an observer-bound reference case. |
| [`AltAz`](https://docs.astropy.org/en/stable/api/astropy.coordinates.AltAz.html) | Defines observation time/location, north-zero/east-positive azimuth, altitude, and the pressure/refraction switch for a proposed horizontal reference output. Its WGS 84 and refraction semantics remain candidate-library behaviour until UFUQ policy is approved. |
| [IERS data access](https://docs.astropy.org/en/stable/utils/iers.html), [`IERS`](https://docs.astropy.org/en/stable/api/astropy.utils.iers.IERS.html), and [`IERSWarning`](https://docs.astropy.org/en/stable/api/astropy.utils.iers.IERSWarning.html) | Defines packaged/automatic IERS data behaviour, predictive and range status, download controls, and warning/error surfaces that the reference protocol must capture. |

`SOURCE_SUPPORTED_FACT`: these pages define Astropy's library semantics. They do not
define what the I/311 author meant by the catalogue's `Ep=1991.25` label.

## Official PyERFA documentation and version boundary

| Record | Version/status | Required use |
|---|---|---|
| [PyPI release `2.0.1.5`](https://pypi.org/project/pyerfa/2.0.1.5/) | Exact runtime release; source distribution SHA-256 `17d6b24fe4846c65d5e7d8c362dcb08199dc63b30a236aedd73875cc83e1f6c0`, matching `uv.lock` | Pins the installed wrapper release and official distribution bytes. |
| [PyERFA stable API index](https://pyerfa.readthedocs.io/en/stable/api.html) | Official stable docs displayed `2.0.1.4` on 2026-08-03 | Defines `ErfaWarning` for positive ERFA status and `ErfaError` for negative status, but does not exactly match the locked patch release. |
| [`pmsafe` stable API](https://pyerfa.readthedocs.io/en/stable/api/erfa.pmsafe.html) | Linked from the `2.0.1.4` stable API | Requires start/end epochs as two-part TDB Julian Dates, proper-motion rates per TDB Julian year, and documents warnings for overridden distance, excessive velocity, and non-convergence. |
| [`ErfaWarning`](https://pyerfa.readthedocs.io/en/stable/api/erfa.ErfaWarning.html) and [`ErfaError`](https://pyerfa.readthedocs.io/en/stable/api/erfa.ErfaError.html) | Linked from the `2.0.1.4` stable API | Names the wrapper warning/error categories that a reference runner must retain. |

`SOURCE_SUPPORTED_FACT`: the exact installed `2.0.1.5` package reports ERFA `2.0.1`
and SOFA `20231011`; its local generated `pmsafe` docstring contains the same TDB-date
contract and warning statuses. This is runtime verification, not a replacement for an
official version-matched documentation build.

`AUTHORITY_OR_EVIDENCE_MISSING`: the PyERFA ReadTheDocs stable build does not match
the locked `2.0.1.5` patch release. A version-matched official documentation build,
tagged source review, or a documented project acceptance of the stable-docs/runtime
combination is still required before calling the PyERFA documentation pin complete.

## Reference-protocol consequences

`PROJECT_DECISION`:

- construct every `Time` with an explicit `format` and `scale`; do not use a library
  default to decide catalogue meaning;
- convert an approved source epoch to the time scale required by the selected routine,
  rather than relabelling the same two-part Julian Date;
- capture Astropy, IERS, and PyERFA warnings and errors as structured reference
  evidence; and
- treat Astropy's missing-radial-velocity zero as a library behaviour, not an approved
  I/311 scientific policy.

`HUMAN_REVIEW_REQUIRED`: the astronomy reviewer must accept the exact Astropy/PyERFA
reference route and warning mapping after the I/311 epoch scale and space-motion input
policy are resolved.

## Required sensitivity experiment

`EXPERIMENT_REQUIRED`: use only synthetic astrometry to compare the following named
start-time interpretations; do not use output as source authority:

1. `Time(1991.25, format="jyear", scale="tt")` as the explicit Julian-TT candidate;
2. the same Julian epoch number labelled `tdb` and `utc`, converted to TDB before the
   ERFA call, to isolate scale-dependent start-instant changes;
3. `Time(1991.25, format="decimalyear", scale="tt")` to measure the distinct
   calendar-decimal-year interpretation; and
4. `Time(1991.25, format="byear", scale="tt")` as a rejection/guard case, not as a
   source-supported candidate.

For zero-motion and high synthetic proper-motion cases, with explicitly varied
parallax and radial velocity, record:

- each start instant as two-part TT and TDB Julian Dates;
- elapsed TDB time to identical target instants;
- output unit-vector angular separation and component residuals;
- all Astropy/PyERFA warnings and errors; and
- the locked software/data manifest and deterministic result hash.

The experiment may measure sensitivity and help a reviewer bound a project decision.
It cannot establish whether I/311 intended TT, TDB, UTC, or any other scale, and it
cannot supply an acceptance tolerance.
