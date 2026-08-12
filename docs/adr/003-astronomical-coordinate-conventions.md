# ADR-003: Astronomical coordinate and scene conventions

- **Status:** Blocked pending manual domain decisions
- **Classification:** CONFIRMED and CLARIFIED, with MANUAL DOMAIN DECISION inputs
- **Date:** 2026-07-20
- **Blockers:** AST-001, AST-003, AST-004, AST-005, AST-006, AST-007

## Context

Sky positions can look plausible while being wrong if catalogue epoch/frame, proper motion, precession/nutation, sidereal time, longitude sign, or refraction conventions are mixed. The report fixes the visible azimuth and Three.js axes but does not fully settle the astrometric/time pipeline, Kaaba authority, or tolerances.

## Decision

The Phase 1 Milestone 2C evidence audit in
`../spikes/PHASE1_SCIENTIFIC_BEHAVIOUR_CONTRACT.md` confirms which items below are
source-supported or already fixed project conventions. It does not change this ADR's
blocked status or approve the remaining AST-003/004/006/007 choices.

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
ephemeris, leap, EOP, observer, and scenario domain. Missing, stale, out-of-range, or
unapproved-quality data return structured non-results. Postimplementation acceptance
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

Milestone 2C.6 proposes `ScientificProfileV1`: one approved preset observer, one
bounded explicit-UTC domain, a 2D-approved minimal source-neutral star artifact, one
normative pure-TypeScript route/effect disposition, immutable offline leap/EOP inputs,
fail-closed geometric output, disabled refraction, no atmosphere defaults, and no
aggregate visibility. It separates permission to implement from later scientific
acceptance. I/311 authority is a 2D eligibility question if retained;
production/reference residuals, any stronger independent validation required by the
claimed boundary, numerical bounds, and tolerances follow implementation.

Fixed now:

- latitude north and longitude east are positive;
- hour angle is west-positive `LST-RA`;
- azimuth is clockwise from True North (`N=0°, E=90°`);
- domain horizontal direction is east/north/up;
- Three coordinates are `+X east`, `+Y up`, `-Z north`;
- Qibla baseline is the initial spherical great-circle bearing clockwise from True North;
- angular answers use robust vector separation or wrapped circular distance;
- every policy and tolerance is versioned and server scoring is authoritative.

Before `ScientificProfileV1` implementation, AST-003 must approve, revise, or reject
the profile's semantic route and actual pure-TypeScript algorithm/library mapping. It
must give every effect an explicit included, excluded, conditional, or unavailable
disposition; approve source-neutral motion/parallax/radial-velocity branches, one
preset-observer contract, one UTC/date domain, leap/EOP field and offline policy,
geometric-only/no-refraction/no-visibility scope, and fail-closed warning/status
semantics. Actual I/311 scale, row, rights, and artifact eligibility belong to 2D if
that source is retained; the generic engine accepts no unspecified scale.

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
- Near zenith, azimuth cannot be used as the scoring oracle; direction vectors are required.
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
