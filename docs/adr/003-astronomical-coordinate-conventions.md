# ADR-003: Astronomical coordinate and scene conventions

- **Status:** Accepted for bounded implementation entry; activation and scientific acceptance remain gated
- **Classification:** SCIENTIFIC_PROFILE_V1 PREIMPLEMENTATION CONTRACT COMPLETE
- **Date:** 2026-07-20
- **Blocker:** none for generic `ScientificProfileV1` implementation; 2D/2E data activation and postimplementation validation remain mandatory

## Context

Sky positions can look plausible while being wrong if catalogue epoch/frame, proper motion, precession/nutation, sidereal time, longitude sign, or refraction conventions are mixed. The report fixes the visible azimuth and Three.js axes but does not fully settle the astrometric/time pipeline, Kaaba authority, or tolerances.

## Decision

The Phase 1 Milestone 2C evidence audit in
`../spikes/PHASE1_SCIENTIFIC_BEHAVIOUR_CONTRACT.md` confirms which items below are
source-supported or already fixed project conventions. Successive focused audits now
approve the ProfileV1 route, exclusions, observer/time contracts, leap/EOP policy and
implementation-entry boundary. Exact source and operational-data artifacts remain
2D/2E activation inputs rather than Milestone 2C semantics.

Milestone 2C.1 adds one source-supported clarification: ESA Gaia DR1 directly
identifies the I/311 new reduction and calls its parameter epoch `J1991.25`, resolving
the representation as Julian. I/311-applicable time-scale authority is still missing.
The project therefore preserves the source label/representation but treats
source-derived propagation as unavailable pending exact authority or named astronomy
review. The specified synthetic interpretation experiment can measure sensitivity but
cannot decide source meaning.

Milestone 2C.2 proposes, without approving, a componentized SOFA `2023-10-11`
CIO-family production semantic route: `iauPmsafe` to a declared target epoch, with
J2000.0 as the candidate epoch input required by `iauAtciq`/`iauAtco13` rather than a
frame conversion; `iauApco13` plus `iauAtciq` to an observer-aware CIRS state; a
separately typed Earth-orientation context; and `iauAtioq` geometric output with
optional `iauRefco`-based refraction kept as another state. `iauApco13` supplies the
built-in model CIP/CIO from IAU 2006 precession with IAU 2000A nutation and accepts
`UT1-UTC` plus polar motion `xp`,`yp`; it does not apply observed celestial-pole
offsets `dX`,`dY`. A reviewed lower-level context is required if those corrections are
selected. The proposed semantic-inclusion matrix and eight required experiment
families are recorded in the contract. Astropy/PyERFA is a reference route independent
of future TypeScript code, not the production selection or a lineage-independent
oracle, and composed `atco13` is only same-family consistency evidence. Routine
availability does not close the epoch/derivative-scale,
radial-velocity, or tolerance blockers.

Milestone 2C.3 proposes as a `PROJECT_DECISION`, without selecting production data or
ranges, a Z-only restricted subset of RFC 3339 at the UTC astronomy boundary; an
explicit geodetic observer with datum/ellipsoid,
ellipsoidal height, provenance, uncertainty, and normalization; request-time offline
execution from immutable hash-addressed EOP/leap bundles; separate reviewed atomic
updates with prior bundles retained; and independent source quality, artifact/field
availability, provenance, coverage, and scientific approval for every required EOP
field.
The supported input domain is the intersection of every approved catalogue, model,
ephemeris, leap, EOP, observer, and scenario domain. Missing, integrity-failed,
expired-for-request, out-of-coverage, or unapproved-quality data return structured non-results. Postimplementation acceptance
evaluates results over that already defined domain; a missing tolerance does not block
pending-validation execution. One EOP field cannot promote another. No degraded result
is approved.

Milestone 2C.4 proposes as a `PROJECT_DECISION`, without approving a model or range,
geometric altitude only for the first vertical slice and a separate optional refracted
state that requires explicit provenance-bearing meteorology. No default atmosphere is
approved, and a scene adapter may not apply refraction. Geometric, refracted-apparent,
physical-dip, terrain/obstruction, renderer, and learner horizon states are distinct;
astronomical, photometric/variability, Sun-altitude/daylight/twilight, atmospheric-
extinction/transparency, cloud/weather, terrain/obstruction, light-pollution, screen,
and learner-eligibility visibility components are also independent and cannot promote
one another. Below-geometric-horizon is attached to the valid direction with its
pending-or-approved validation state and retains
signed altitude, defined azimuth/singularity, provenance, warnings, and statuses; it
cannot decide visibility or presentation. Optional-stage failures never hide an
earlier core scientific failure or erase a valid geometric state. A refracted apparent
horizon means only apparent altitude zero under a named approved refraction policy; it
is not geometric altitude zero, physical dip, skyline/terrain, or a numerical guard.

Milestone 2C.5B executes only the nine bounded synthetic Batch 01 scopes. It passes
exact epoch-label/rejection, motion-convention, raw-status, deterministic-replay, and
optional-state guards while retaining all numerical outputs as
`MEASURED_NO_ACCEPTANCE`. Componentized/composed ERFA agreement is same-family
consistency, not independent validation. These results change none of this ADR's
source, production, EOP, observer, refraction, domain, tolerance, or approval blockers.

Milestone 2C.6 defines `ScientificProfileV1`: one selected observer-preset identity
under a generic fail-closed contract, one bounded explicit-UTC domain, a 2D-approved
minimal source-neutral star artifact, one normative pure-TypeScript route/effect
disposition, immutable offline leap/EOP inputs, fail-closed geometric output, disabled
refraction, no atmosphere defaults, and no aggregate visibility. The selected identity
is `umpsa-pekan-faculty-of-computing`; exact coordinates, reference point, datum/frame/
ellipsoid, typed height, accuracy, provenance, version, and activation record belong to
2D and block real V1 execution rather than generic astronomy-core implementation. It
separates permission to implement from later scientific acceptance. I/311 authority is
a 2D eligibility question if retained;
production/reference residuals, any stronger independent validation required by the
claimed boundary, numerical bounds, and tolerances follow implementation.

The semantic-scope audit adopts the V1 boundary/output/outcome subset as normative:
geometric output only; no refraction request or atmosphere input/default; no aggregate
visibility; result-bearing below-geometric-horizon classification; exact zenith/nadir
azimuth singularity with altitude/ENU retained; non-erasing failure/partial-result
precedence; preserved scientific warnings/statuses; and
`GEOMETRIC_RESULT_PENDING_VALIDATION` distinct from the initially unreachable
`APPROVED_GEOMETRIC_RESULT`. Physical refraction, apparent/physical/terrain horizons,
visibility components, scene/learner/scoring correctness, and any numerical
ill-conditioned-azimuth boundary remain later capabilities rather than zero-error V1
terms.

The time audit also adopts a normative whole-second Z-only UTC input grammar,
conditional artifact-backed leap-second validation, explicit UTC quasi-JD/TAI/TT/UT1
states, and a versioned `SupportedTimeDomain` with explicit endpoint dispositions and
complete required-field coverage. Exact earliest/latest timestamp values are derived
from approved artifacts during 2D/2E activation; neither RFC 3339 nor SOFA selects
them, and generic astronomy-core implementation does not require them first.

The focused route audit now approves the ProfileV1 transformation and production
mapping. The source-neutral typed route is `CatalogueIcrsState` to
`PropagatedIcrsAstrometry`, then `ObserverAwareCirsDirection` under an explicit
`EarthOrientationContext`, then `GeometricHorizontalDirection`. Production is a
UFUQ-owned pure-TypeScript subset derived from exact SOFA `2023-10-11` lower-level C
semantics: strict full-input `pmsafe` propagation to the J2000.0 TDB epoch interface,
pinned `epv00` Earth/Sun state, IAU 2006 precession with IAU 2000A nutation/CIO model
orientation, declared-ellipsoid observer construction, `apco`/`apcs`-derived context,
`atciq`-derived ICRS-to-CIRS and only the geometric part of the `atioq`-derived local
stage. Observer velocity carries diurnal aberration through the `apcs`/`atciq`-
derived context, so the later local `diurab` term is disabled as redundant, matching
SOFA `apco`. Every eligible row requires approved epoch/derivative scale, `mu_alpha_star`,
Dec motion, positive parallax/equivalent distance and finite radial velocity. V1
requires leap data plus `UT1-UTC`,`xp`,`yp`; it deliberately does not consume observed
`dX`,`dY`. Extra-body deflection and refraction are also outside V1. None of these
omissions is zero uncertainty. The current-package audit finds no third-party
TypeScript package with this exact model/data/status boundary, so ERFA or official
SOFA C-to-WebAssembly is only a fallback if the owned subset proves unmaintainable.

Fixed now:

- latitude north and longitude east are positive;
- hour angle is west-positive `LST-RA`;
- azimuth is clockwise from True North (`N=0°, E=90°`);
- domain horizontal direction is east/north/up;
- V1 output is geometric only and below-horizon remains a valid result classification;
- V1 requests no refraction, creates no atmosphere, and emits no aggregate visibility;
- scientific warnings and raw statuses remain provenance-bearing evidence;
- successful execution is pending validation rather than scientific approval;
- the core accepts no local/current time, numeric offset, fractional input, Unix
  timestamp, or unlabeled Julian Date;
- Three coordinates are `+X east`, `+Y up`, `-Z north`;
- Qibla baseline is the initial spherical great-circle bearing clockwise from True North;
- angular answers use robust vector separation or wrapped circular distance;
- every policy and tolerance is versioned and server scoring is authoritative.

AST-003 now approves the final Milestone 2C leap/EOP contract. V1 requires an explicitly
supplied immutable approved leap state plus independently approved final `UT1-UTC` in
seconds and `xp`,`yp` in radians. Every field retains independent source/row/support
identity, quality, coverage, interpolation evidence, availability and approval. V1
selects Gazette 13's four-point Lagrange example with complete support; across leap
boundaries `UT1-UTC` is interpolated via continuous `UT1-TAI`, and the IERS Conventions
2010 ocean-tide and applicable libration terms are restored exactly once after
interpolation. Equivalent schemes are source-permitted but not V1-approved. Missing,
blank, preliminary, predicted, estimated, unsupported,
expired-for-request, integrity-failed or otherwise unapproved input fails closed. No
zero, nearest-row, extrapolated, automatic-download, hidden-cache or library-table
fallback exists. Bulletin C is the event authority; 2D must select the exact official
machine-readable transport and EOP release, and 2E must build and verify the immutable
bundle before real execution. The route/effect mapping,
source-neutral motion/parallax/radial-velocity eligibility, observer and UTC contracts,
geometric/no-refraction/no-visibility scope and core outcome/precedence contracts are
normative. Actual I/311 scale, row, rights and artifact eligibility belong to 2D if
that source is retained; the generic engine accepts no unspecified scale or missing
parallax/RV substitute.

Quantified production disagreement, omission bounds, final numerical error budgets,
and scientific/reference tolerances are postimplementation acceptance gates. Full
refraction, atmosphere, physical/terrain horizon, visibility, global observer, Kaaba,
scene, and learner policies are later or separate gates. None is silently treated as
zero or as a library default.

## Consequences

- Browser, server, fixtures, and thesis results can use identical named semantics.
- Missing required IERS data or profile policy causes an explicit non-result. A missing
  tolerance prevents later scientific acceptance, not pending-validation execution. A
  labelled degraded approximation is unavailable until separately quantified and
  approved.
- Publication age is not scientific field quality: an older immutable bundle can
  remain valid for approved historical replay, while a newly acquired bundle can be
  unusable when field coverage, interpolation support, integrity, publisher validity
  or UFUQ approval is absent.
- At exact zenith/nadir azimuth is undefined while altitude/ENU remain valid. Near that
  geometry, azimuth cannot be the sole comparison/scoring quantity; no numerical
  ill-conditioned boundary is invented.
- Polaris remains a star cue distinct from terrestrial True North.

## Alternatives rejected

- Unlabelled degrees/coordinates or implicit west-positive longitude.
- Mixing catalogue-epoch RA with apparent sidereal time without an approved transformation.
- Treating Polaris direction as exactly True North.
- Selecting Kaaba coordinates or refraction constants from memory.

## Validation

Preimplementation review covers authoritative semantics, profile decisions, Batch 01
guards, the pinned candidate reference environment, and planned fixtures.
Postimplementation pinned reference fixtures cover frame/time/EOP/leap/observer/wrap/
horizon/singularity and exact endpoints with artifact hashes, independent per-field
states, warnings, precedence, and outcomes; `test:reference` activates then. Every
numeric acceptance remains inside AST-006. A later NOVAS or other genuinely independent
path strengthens validation; shared ERFA/SOFA lineage does not. Refraction fixtures are
required only when that later capability is proposed. Internal Three mapping fixtures
cannot serve as independent astronomy proof.
