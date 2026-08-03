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
families are recorded in the contract. Astropy/PyERFA is the independent reference
route, not the production selection, and composed `atco13` is only same-family
consistency evidence. Routine availability does not close the epoch/derivative-scale,
radial-velocity, or tolerance blockers.

Milestone 2C.3 proposes as a `PROJECT_DECISION`, without selecting production data or
ranges, a Z-only restricted subset of RFC 3339 at the UTC astronomy boundary; an
explicit geodetic observer with datum/ellipsoid,
ellipsoidal height, provenance, uncertainty, and normalization; request-time offline
execution from immutable hash-addressed EOP/leap bundles; separate reviewed atomic
updates with prior bundles retained; and independent source quality, artifact/field
availability, provenance, coverage, and scientific approval for every required EOP
field.
The supported domain is the intersection of every approved catalogue, model,
ephemeris, leap, EOP, observer, scenario, and tolerance domain. Missing, stale,
out-of-range, or unapproved-quality data return structured non-results. One EOP field
cannot promote another. No degraded result is approved.

Fixed now:

- latitude north and longitude east are positive;
- hour angle is west-positive `LST-RA`;
- azimuth is clockwise from True North (`N=0°, E=90°`);
- domain horizontal direction is east/north/up;
- Three coordinates are `+X east`, `+Y up`, `-Z north`;
- Qibla baseline is the initial spherical great-circle bearing clockwise from True North;
- angular answers use robust vector separation or wrapped circular distance;
- every policy and tolerance is versioned and server scoring is authoritative.

Before implementation, AST-003 must approve, revise, or reject the proposed route and
select the actual pure-TypeScript algorithm/library, including the exact I/311 epoch
and proper-motion derivative time scale. The CDS-defined 365.25-day `yr` duration is
resolved. AST-003 must explicitly implement or omit with a
quantified bound proper motion, parallax, radial velocity/perspective acceleration,
aberration, light deflection, precession/nutation, topocentric effects, polar motion,
celestial-pole offsets, EOP/time handling, datum/elevation and supported range. It must
also select the exact production data artifacts/hashes, field precedence/interpolation,
stale and expiry rules, update cadence, preliminary/prediction disposition, UTC
precision/zone adapter, observer normalization/ranges, endpoint semantics, and warning
mapping. Also
approve refraction/horizon/visibility, Kaaba/observer coordinate semantics, error
budget and tolerances as detailed in `../ASTRONOMY_SPEC.md`.

## Consequences

- Browser, server, fixtures, and thesis results can use identical named semantics.
- Missing IERS/policy/tolerance data causes an explicit non-result. A labelled degraded
  approximation is unavailable until separately quantified and approved.
- Near zenith, azimuth cannot be used as the scoring oracle; direction vectors are required.
- Polaris remains a star cue distinct from terrestrial True North.

## Alternatives rejected

- Unlabelled degrees/coordinates or implicit west-positive longitude.
- Mixing catalogue-epoch RA with apparent sidereal time without an approved transformation.
- Treating Polaris direction as exactly True North.
- Selecting Kaaba coordinates or refraction constants from memory.

## Validation

Independent pinned Astropy/PyERFA/domain fixtures across frame/time/EOP/leap/observer/
wrap/horizon/singularity and exact-endpoint partitions, reconstructed offline with
artifact hashes, independent per-field source-quality/availability/approval records,
warnings, deterministic multi-fault precedence, and structured outcomes. Every numeric
comparison must be inside AST-006. Internal Three mapping fixtures cannot serve as
independent astronomy proof.
