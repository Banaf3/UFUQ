# Current production-astronomy implementation candidates

## Scope and method

This dossier records a freshness-dependent implementation audit performed on
2026-08-13 for the `ScientificProfileV1` transformation route. It uses only official
project repositories, official package-registry metadata, official release records,
and official licences. Package popularity and marketing language are not scientific
authority. IAU SOFA `2023-10-11` remains the algorithm/routine authority.

The audit asks whether a candidate can implement the approved source-neutral route,
accept all operational data explicitly, run deterministically offline in browser and
server builds, preserve scientific statuses, and expose exact effect ownership. A
package can be current and well maintained while still being scientifically
incompatible with this profile.

## Current candidate inventory

| Candidate | Current official state on 2026-08-13 | Runtime/platform evidence | Scientific and policy fit | Decision |
|---|---|---|---|---|
| [`astronomy-engine`](https://www.npmjs.com/package/astronomy-engine) | npm `2.1.19`, published 2023-12-14; repository latest commit 2025-01-27; MIT; zero runtime dependencies; bundled TypeScript declarations | Official documentation supports browser and Node use and contains no runtime package dependency. Its `AstroTime` documentation approximates UT1 as UTC and derives TT from a fitted polynomial; the horizon API owns its own optional-refraction behavior. | The project states a compact approximately one-arcminute design, uses truncated models, and documents a five-term nutation optimization rather than the full IAU 2000A route. It does not expose UFUQ's required caller-supplied `UT1-UTC`, `xp`, `yp`, per-field EOP status, or SOFA-compatible warning surface. | `NOT_SELECTED`: healthy convenience library, different scientific contract. |
| [`astronomia`](https://www.npmjs.com/package/astronomia) | npm `4.2.0`, published 2025-08-30; repository latest commit 2025-08-30; MIT; zero runtime dependencies; Node `>=12`; no package TypeScript declarations | Official package documentation supports modern browsers and Node and implements JavaScript translations of selected Meeus algorithms plus other modules. | It does not implement the pinned SOFA CIO-family astrometric route or expose external per-field EOP injection/status ownership. Its different model family cannot silently replace the selected IAU/SOFA semantics. | `NOT_SELECTED`: maintained, but not a semantic match. |
| [`@observerly/astrometry`](https://www.npmjs.com/package/@observerly/astrometry) | npm `0.66.0`, published 2026-08-11; repository latest commit 2026-08-12; MIT; TypeScript; one declared runtime type dependency | The official README targets Node/Deno/Bun/browser use and relies heavily on JavaScript `Date`. It also explicitly says the project is early-stage, API-unstable, and not ready for production use. | Its high-level J2000/correction helpers do not expose the required SOFA model identity, caller-owned leap/EOP field states, or complete status/warning boundary. | `NOT_SELECTED`: active but explicitly pre-production and not a route match. |
| [`@tsastro/tsofa`](https://www.npmjs.com/package/@tsastro/tsofa) | npm `18.1.0`, published 2024-10-24; repository latest commit 2025-01-23; TypeScript ESM; zero declared runtime dependencies; npm metadata says MIT, while the distributed licence also carries the SOFA-derived-work terms | Pure TypeScript and therefore browser/server portable after normal bundling. The package source identifies its tracked SOFA release as `2021-05-12`, embeds leap-second state, and exposes the SOFA-like routines as one large transcription. | It does not track the pinned SOFA `2023-10-11` issue. Its `jauPmsafe` returns coordinates without the original integer warning bitmask, so the required raw status cannot be preserved. The embedded leap state also conflicts with UFUQ's explicit artifact boundary. | `NOT_SELECTED`: closest API shape, but stale baseline/status loss/embedded-data ownership are blocking mismatches. |
| [ERFA](https://github.com/liberfa/erfa) C library | release `2.0.1`, published 2023-10-13; repository latest commit 2026-07-24; three-clause BSD; no runtime astronomy-data download | Maintained C library, not an official Node/browser/TypeScript distribution. It can be compiled to native or WebAssembly with a separate pinned build toolchain and adapter. ERFA says `2.0.1` differs from SOFA `2023-10-11` only by its version and runtime leap-second extensions. | Excellent semantic coverage and explicit C statuses/EOP inputs, but it shares the ERFA/SOFA lineage with the Python reference and adds binary build, loading, licence, and deployment surfaces. No current official ERFA WebAssembly package was found. | `VIABLE_FALLBACK`, not selected for V1: use only if the owned TypeScript route proves unmaintainable. |
| Official IAU SOFA C `2023-10-11` compiled to WebAssembly | Current official nineteenth release, issued 2023-10-11; SOFA licence | Exact authority implementation can be built offline, but SOFA supplies C/Fortran rather than an official browser/Wasm artifact. UFUQ would own the compiler, binary reproducibility, loader, and status/data adapter. | Exact semantics and effect control, but it introduces a native/Wasm toolchain and browser binary boundary where the bounded pure-TypeScript route is feasible. It also remains the same scientific lineage as the reference route. | `VIABLE_FALLBACK`, not selected for V1. |
| UFUQ-owned pure-TypeScript SOFA-derived subset | No third-party runtime dependency or hidden data source; future code is pinned to exact SOFA `2023-10-11` source files/hashes | Pure deterministic functions in `astronomy-core`; explicit typed leap/EOP/observer inputs; browser/server portability; no network, cache, clock, atmosphere, or catalogue access. | Implements only the normative route and can preserve every raw status. UFUQ assumes maintenance, port verification, licence/attribution, and release-diff responsibility. | `SELECTED_PRODUCTION_STRATEGY` for V1. |

Dates above come from official npm/GitHub metadata. A repository commit is only a
maintenance signal; it does not prove scientific fitness. The npm `astronomia` release
date is later than many search-index summaries, so the official registry timestamp
controls this audit.

## Operational-control comparison

| Candidate | Offline/hidden-input boundary | Effect and EOP control | Status/warning surface | Scientific lineage and maintenance risk |
|---|---|---|---|---|
| Astronomy Engine `2.1.19` | Self-contained model data and no documented runtime astronomy-data download, but time-scale approximations and refraction choices are library-owned rather than injected UFUQ artifacts. | Does not accept the required independent `UT1-UTC`,`xp`,`yp` states or expose the selected full IAU 2000A/CIO composition. | Does not expose SOFA-equivalent raw routine status provenance for the selected route. | Separate implementation/model lineage, but scientifically incompatible with V1; adopting it would transfer an approximation contract to UFUQ. |
| astronomia `4.2.0` | Modular offline calculations with no documented runtime data refresh; callers would still have to build missing operational-data policy externally. | Individual Meeus-derived modules are selectable, but no exact selected SOFA route, caller-owned per-field EOP context or matching effect inventory is provided. | No route-wide SOFA raw-status contract. | Different model lineage; maintained, but substantial adapter/reimplementation work would still be required and would not prove V1 semantics. |
| Observerly Astrometry `0.66.0` | No automatic EOP/leap acquisition contract suitable for V1 was found; JavaScript `Date` is a primary time surface. | High-level correction functions do not expose exact model/effect/EOP ownership needed by V1. | No complete raw SOFA-status boundary was found. | Active TypeScript project, but its explicit pre-production warning makes long-term API/stability risk unacceptable for the core. |
| TSOFA `18.1.0` | Offline code with zero declared runtime dependencies, but a compiled leap table is ambient package state. | Broad SOFA-shaped effect/EOP control, tied to the older declared issue and not the exact pinned subset. | `jauPmsafe` loses the integer warning status even though other routines can return status-bearing objects. | Shared SOFA lineage; modest dependency surface but release/status/data-ownership drift would become UFUQ maintenance risk. |
| ERFA `2.0.1` C | Offline and caller-supplied scientific inputs; no hidden astronomy-data download. A Wasm/native build and loader would be UFUQ-owned artifacts. | Close match with explicit EOP/effect routines and runtime leap extensions. | Native status returns are available. | Same ERFA/SOFA lineage as the reference; healthy upstream, but browser binary/toolchain reproducibility is added risk. |
| Official SOFA C-to-Wasm | Offline after a pinned reproducible build; no official Wasm artifact, so no third party can silently update it. | Exact selected routines/effects and explicit EOP adapter are possible. | Exact C statuses can be retained. | Same SOFA lineage; stable authority, but UFUQ owns compiler, ABI, binary and browser-loader maintenance. |
| UFUQ-owned TypeScript subset | No clock, network, file, cache, catalogue, leap, EOP, observer or atmosphere discovery is permitted. | Only selected effects exist; every time/observer/leap/EOP input is typed and caller supplied. | Raw derived-routine statuses plus normalized policy disposition are explicit outputs. | Same SOFA scientific lineage as the reference but code/dependency independent; smallest runtime surface, with permanent port/release-diff responsibility. |

No candidate is called independent scientific validation merely because its source
code, language, or package graph differs. Scientific-lineage independence is assessed
separately from implementation independence.

## Selected implementation boundary

`PROJECT_DECISION`: implement a bounded UFUQ-owned pure-TypeScript route derived from
the exact IAU SOFA `2023-10-11` C semantics. Do not copy a high-level convenience API
as policy. The implementation must:

- use UFUQ names rather than `iau`/`sofa` prefixes;
- identify every originating SOFA file, issue, source hash, derivation, and intentional
  difference in source and the algorithm manifest;
- reproduce the applicable SOFA licence conditions and attribution without implying
  IAU endorsement;
- preserve every integer/warning status that the selected source routine exposes;
- inject typed time, observer, leap, and EOP inputs rather than consulting global
  tables, current time, files, caches, or network services;
- keep the `tools/astronomy-reference` environment out of the production dependency
  graph; and
- run source-vector, SOFA test-vector, mutation, property, deterministic-replay, and
  postimplementation production/reference tests before scientific acceptance.

The selected subset includes the semantics and coefficient data needed for the
approved space-motion, Earth ephemeris, IAU 2006/2000A CIO-family, observer-context,
CIRS, and geometric-horizontal stages. It does not include refraction or extra-body
deflection. The implementation must not call the monolithic `iauApco13` behavior as an
opaque policy boundary: that convenience routine owns a WGS 84 conversion, an ambient
SOFA leap table, refraction inputs, and model-CIP-only path, and it discards the
`iauEpv00` status. The production composition instead exposes the corresponding
lower-level inputs/statuses and uses the declared observer ellipsoid through the
`iauGd2gce`-equivalent semantics.

## Maintenance and independence disposition

The pinned science release is an authoritative stable standard, not an abandoned
software dependency. UFUQ must audit each later SOFA issue as a deliberate model
upgrade; it does not fetch or float to a release at runtime.

Production code and dependencies remain independent from the Python/Astropy reference
tool. Scientific lineage is not fully independent: an owned implementation derived
from SOFA compared with Astropy/PyERFA/ERFA is a shared-scientific-lineage
implementation-verification path. A later NOVAS or other lineage-audited oracle is the
stronger independent-validation stage. Neither same-family agreement nor deterministic
bytes establishes a numerical acceptance tolerance.

## Resource conclusion

The local official SOFA `2023-10-11` release/manual/source and IERS TN36 material are
sufficient for the preimplementation mapping. No new PDF, package download, or user
action is required. Exact npm tarball integrity values and repository commits were
inspected for candidate evaluation only; no candidate was installed and no dependency
or lockfile changed.
