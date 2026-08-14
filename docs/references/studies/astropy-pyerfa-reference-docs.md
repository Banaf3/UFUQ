# Astropy and PyERFA reference-documentation pin

## Scope and identity

- Source IDs: `ASTROPY-DOCS-PIN` and `PYERFA-PIN`.
- Retrieval date: 2026-08-03.
- Runtime under review: Astropy `8.0.1`, PyERFA `2.0.1.5`, ERFA `2.0.1`, and
  SOFA `20231011`, as locked by `tools/astronomy-reference/uv.lock` and reported by
  the workspace-local oracle environment.
- Scope: time representation and scale, space-motion propagation, GCRS/CIRS/ITRS/AltAz
  frame roles, Earth-orientation data status, and preservation of ERFA warnings/errors
  for a future code-independent reference implementation with shared ERFA/SOFA
  scientific lineage disclosed.
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
| [Astronomical coordinate systems](https://docs.astropy.org/en/stable/coordinates/index.html), [`GCRS`](https://docs.astropy.org/en/stable/api/astropy.coordinates.GCRS.html), [`CIRS`](https://docs.astropy.org/en/stable/api/astropy.coordinates.CIRS.html), and [`ITRS`](https://docs.astropy.org/en/stable/api/astropy.coordinates.ITRS.html) | Defines the reference library's frame graph and observer/time attributes. GCRS includes aberration relative to ICRS; CIRS and ITRS are explicit graph states. These pages support reference-state inspection but do not define UFUQ production stage ownership. |
| [`EarthLocation`](https://docs.astropy.org/en/stable/api/astropy.coordinates.EarthLocation.html) | Defines named geodetic longitude, latitude, and height input, east-positive longitude, and reference-ellipsoid handling required by an observer-bound reference case. |
| [`AltAz`](https://docs.astropy.org/en/stable/api/astropy.coordinates.AltAz.html) | Defines observation time/location, north-zero/east-positive azimuth, altitude, and the pressure/refraction switch for a proposed horizontal reference output. Its WGS 84 and refraction semantics remain candidate-library behaviour until UFUQ policy is approved. |
| [IERS data access](https://docs.astropy.org/en/stable/utils/iers.html), [`IERS`](https://docs.astropy.org/en/stable/api/astropy.utils.iers.IERS.html), and [`IERSWarning`](https://docs.astropy.org/en/stable/api/astropy.utils.iers.IERSWarning.html) | Defines packaged/automatic IERS data behaviour, predictive and range status, download controls, and warning/error surfaces that the reference protocol must capture. |
| [`LeapSeconds`](https://docs.astropy.org/en/stable/api/astropy.utils.iers.LeapSeconds.html) | Defines readers for IERS `Leap_Second.dat`, IETF/NTP `leap-seconds.list`, and ERFA tables; table expiration, expired-table warnings, network suppression, and ERFA-table update surfaces. |

`SOURCE_SUPPORTED_FACT`: these pages define Astropy's library semantics. They do not
define what the I/311 author meant by the catalogue's `Ep=1991.25` label.

## Milestone 2C.3 observer/time/data consequences

`SOURCE_SUPPORTED_FACT`:

- `EarthLocation.from_geodetic` uses east-positive longitude and height above a named
  reference ellipsoid and defaults to WGS 84. The default is library behaviour, not a
  UFUQ production decision.
- Astropy's IERS-A path contains historical and predictive data, may automatically
  download/refresh it, and may return nearest available values or allow degraded
  accuracy under permissive configuration. The independent runner must therefore set
  its own data table and fail-closed configuration explicitly.
- `LeapSeconds` can select among local, network, and ERFA sources; exposes expiration;
  and can warn while returning the newest expired table. That is a warning surface to
  test, not permission for stale UFUQ execution.
- `Time` keeps representation and scale distinct and uses two-part Julian Dates. Its
  output precision control does not set UFUQ's accepted input precision or scientific
  tolerance.

`PROJECT_DECISION`: a future scientific reference runner must install exact EOP and
leap tables from the fixture manifest, disable automatic download and cache discovery,
capture every field's separate source quality, availability, provenance, coverage,
scientific approval, and every warning/error, and prove offline reconstruction. It may
not inherit Astropy's nearest-value, permissive degraded-accuracy, stale-table,
prediction, WGS 84 default, or automatic leap-table selection as production policy.

`AUTHORITY_OR_EVIDENCE_MISSING`: no production EOP/leap artifact, supported range,
stale rule, prediction/preliminary policy, observer range, or precision is selected.
The existing `astropy-iers-data` files/hashes remain synthetic-smoke evidence only.

## Milestone 2C.4 refraction consequences

`SOURCE_SUPPORTED_FACT` from official Astropy `8.0.1` `AltAz` documentation:

- a nonzero `pressure` requests refraction, while pressure `0` disables it;
- the library fields are pressure in pressure units, ground-level temperature in
  degrees Celsius, relative humidity as a dimensionless fraction from 0 through 1,
  and observation wavelength in length units;
- the documented defaults are `0 hPa`, `0 deg C`, `0`, and `1 micron`; and
- the ERFA-based model is documented as inaccurate below about 5 degrees, with
  potentially meaningless or highly discrepant behavior near/below altitude zero.

`PROJECT_DECISION`: every future reference case explicitly supplies all atmosphere
fields, even when selecting pressure zero for a geometric result. It records geometric
and refracted states separately and captures every warning. Missing meteorology in a
requested UFUQ refraction case is an unavailable result, not permission to inherit the
Astropy defaults.

`AUTHORITY_OR_EVIDENCE_MISSING`: Astropy's defaults, about-5-degree statement, and
round-trip behavior do not select UFUQ's atmosphere, range, validity threshold,
below-horizon behavior, or tolerance. Astropy defines no terrain, photometric,
daylight/twilight, extinction/transparency, cloud/weather, light-pollution, renderer,
or learner-eligibility policy.

`HUMAN_REVIEW_REQUIRED`: AST-004/006 must approve the model/domain/input provenance,
warnings, and any comparison case before a nonzero-pressure output can become an
approved reference expectation. `APPROVED_REFRACTED_RESULT` and any warning-bearing
variant also require the approved combined operating domain, scientific tolerance, and
named astronomy-review approval; library output alone cannot make either reachable.

`EXPERIMENT_REQUIRED`: the seven 2C.4 experiment families compare model choice,
meteorology sensitivity, near-horizon numerics, geometric/apparent horizons,
below-horizon behavior, library-default consequences, and visibility-state separation.
They do not create source authority or a tolerance.

## Official PyERFA documentation and version boundary

| Record | Version/status | Required use |
|---|---|---|
| [PyPI release `2.0.1.5`](https://pypi.org/project/pyerfa/2.0.1.5/) | Exact runtime release; source distribution SHA-256 `17d6b24fe4846c65d5e7d8c362dcb08199dc63b30a236aedd73875cc83e1f6c0`, matching `uv.lock` | Pins the installed wrapper release and official distribution bytes. |
| [PyERFA stable API index](https://pyerfa.readthedocs.io/en/stable/api.html) | Official stable docs displayed `2.0.1.4` on 2026-08-03 | Defines `ErfaWarning` for positive ERFA status and `ErfaError` for negative status, but does not exactly match the locked patch release. |
| ERFA astrometry wrappers indexed by the stable API: `atco13`, `apco13`, `atciq`, `atioq`, `pnm06a`, `era00`, `sp00`, `pom00`, `c2t06a`, and `refco` | Official wrapper pages belong to the displayed `2.0.1.4` build; exact installed `2.0.1.5` docstrings were inspected locally | Exposes direct reference probes for the proposed stage/effect inventory. The governing algorithm authority remains pinned SOFA `2023-10-11`, and these probes do not select production code. |
| ERFA time/observer wrappers indexed by the stable API: `dtf2d`, `utctai`, `taitt`, `utcut1`, `eform`, and `gd2gc` | Official wrapper pages belong to the displayed `2.0.1.4` build; governing contracts remain pinned SOFA `2023-10-11` | Exposes direct leap/calendar warning, UTC/TAI/TT/UT1 conversion, ellipsoid, and geodetic-to-geocentric probes for 2C.3 boundary fixtures. It does not provide EOP or leap authority and cannot select UFUQ input/range policy. |
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

`HUMAN_REVIEW_REQUIRED`: before postimplementation scientific acceptance, the
astronomy reviewer must accept the exact Astropy/PyERFA reference route, installed-
patch evidence and warning mapping against the 2D-approved source-neutral rows. This
does not require I/311 if 2D selects another source.

## Milestone 2C.2 code-independent reference route

`PROJECT_DECISION`: the reference code/dependency route is deliberately not the
selected UFUQ-owned TypeScript production route:

1. construct ICRS `SkyCoord` with explicit source `obstime`, `pm_ra_cosdec`, `pm_dec`,
   distance/parallax, and radial velocity only after each input policy is approved;
2. use `apply_space_motion` only with explicit start/end times and capture warnings;
3. inspect an explicit topocentric `CIRS` state at the observation instant/location;
4. transform to `AltAz` with pressure explicitly zero for the geometric reference;
5. run a separately labelled nonzero-pressure `AltAz` case only when the refraction
   policy supplies pressure, temperature, humidity, wavelength, and a valid range; and
6. use direct PyERFA calls for structured warning/status capture and controlled effect
   ablations where the Astropy graph does not expose a policy switch.

Astropy `transform_to` chooses a library graph path and obtains Earth-orientation data
through Astropy's IERS machinery. The runner must pin/record that graph-visible frame
sequence, IERS table/hash, each EOP field's source quality and availability,
auto-download/cache state, observer WGS 84 semantics, ephemeris, refraction inputs, and
all warnings. A high-level result cannot be used to infer scientific approval or which
production stage owns topocentric parallax or diurnal aberration.

`AUTHORITY_OR_EVIDENCE_MISSING`: 2D source-row eligibility and exact production
leap/EOP operating artifacts still prevent approved source-derived reference truth.
The generic final-only policy is now normative. I/311's epoch/derivative scale and absent radial velocity matter only if 2D
retains it. Refraction is outside V1 rather than a route blocker. The official PyERFA
stable/runtime patch mismatch also remains for later reference acceptance.

The selected production implementation is derived from SOFA semantics while Astropy
uses PyERFA/ERFA. The implementations and dependencies are independent, but the
scientific lineage is shared. Their comparison is implementation verification, not
the later stronger-independent-validation stage.

## ScientificProfileV1 time-boundary consequence

Astropy's documented two-part JD storage and explicit scale conversions are
`SOURCE_SUPPORTED_FACT` for the reference path. They do not select UFUQ input syntax,
precision, operating dates, leap/EOP artifacts, or production behavior.

ScientificProfileV1 makes a separate normative `PROJECT_DECISION`: accept only whole-
second `YYYY-MM-DDTHH:mm:ssZ`; conditionally validate `23:59:60Z` against the selected
approved leap artifact; carry labelled UTC quasi-JD/TAI/TT/UT1 states and conversion
evidence; and reject implicit network/cache/table discovery. Exact supported-date
values are 2D/2E activation data. Astropy `Time.precision`, permissive input formats,
automatic IERS behavior, and ambient ERFA leap state are not production policy.

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
