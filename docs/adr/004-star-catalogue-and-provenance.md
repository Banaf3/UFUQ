# ADR-004: Star catalogue, cultural curation, and provenance

- **Status:** Parser contract accepted; Milestone 2D.1 prefers Gaia DR3 but production catalogue/row authority remains blocked; release and cultural gates remain blocked
- **Classification:** CONFIRMED/CLARIFIED; source and mappings are MANUAL DOMAIN DECISIONS
- **Date:** 2026-07-20
- **Blockers:** AST-001, AST-002

## Context

The report requires a small preprocessed static JSON star dataset and authentic Arabic nomenclature. Numerical astrometry, cultural names/relationships, visual line segments, and educational metadata come from different authorities. Hand-copying coordinates or combining them in an undocumented file would make errors, licensing, and thesis reproduction unmanageable.

## Decision

Use the five-class separation and deterministic pipeline in `../DATA_STRATEGY.md` from
Phase 1 onward. Acquire numerical data from one approved catalogue/table/version using
a pinned script/query and manifest, including exact subset/uncertainty/quality rules.
Join separately reviewed generic `SkyPattern` records, `GuidanceRelationship` edges,
and `LessonRoute`/educational metadata by stable internal IDs. A numerical star record
owns `starId` plus versioned external source/release identifiers in a crosswalk.
`SkyPattern` owns names/labels, member `starId` values, segments, and cultural status;
`GuidanceRelationship` owns a
typed source/target, instructional geometry/explanation, applicable scenarios, and
verification status; `LessonRoute` owns ordered steps, prerequisites, alternatives, and
the scaffold-configuration reference. Validate schemas/review status and emit
canonically serialized, versioned runtime JSON plus checksums consumed identically by
browser and API.

Keep those logical classes in one `catalogue-schema` npm workspace:
`src/catalogue/` for numerical serialized rows, `src/content/` for guidance content,
and `src/artifact/` for generated envelopes. Keep the pipeline as internal modules of
the single `tools/catalogue` workspace. Store tracked provenance in `data/manifests/`,
ignore `data/raw/` by default, separate reviewed patterns/relationships/routes under
`data/curation/`, and reserve `data/generated/` for deterministic outputs permitted by
licence. Canonical serialization explicitly writes UTF-8, LF, deterministic key/record
ordering, and defined numeric formatting; it does not rely on Git or host defaults.

The schema is not Banat Na'sh-specific. It permits reviewed helper patterns to lead to
Banat Na'sh or Dhat al-Kursi, either pattern to lead to Al-Jady, and subsequent
Al-Jady→True North→Qibla direction steps. The server may select a route only when all
stars required by its resolved patterns/relationships are available in the approved
scenario.

CDS I/311, *Hipparcos, the New Reduction*, is the sole catalogue source studied for
the Phase 1 local technical spike. This is not a permanent UFUQ source selection.
Milestone 2D must approve the actual catalogue/release, rights, crosswalk, row
eligibility, and minimal allowlist before 2E source-derived generation. If 2D retains
I/311, use the corrected author-replacement files dated
2008-09-16, `hip2.dat` as the main table, and an exact required supplement for selected
3/7/9-parameter or VIM solutions. Retain every main-table field and preserve raw
solution, multiplicity, uncertainty, weight, quality, variability, and photometric
evidence. I/311 Appendix G confirms `pmRA` is `mu_alpha_star`; normalize it explicitly
as the cosine-weighted right-ascension component.

The exact 19-HIP list in
`../spikes/PHASE1_CATALOGUE_AUTHORITY_PROVENANCE.md` is a local technical review
candidate only. It does not approve a source row's scientific suitability, helper
pattern, Arabic spelling, transliteration, historical membership, line geometry,
guidance relationship, explanation, or lesson route. Generated rows are never edited
manually.

Official VizieR rules support local scientific-context use with source citation, but no
catalogue-specific grant for raw or derived I/311 redistribution was found. Therefore
all raw and source-derived bytes stay ignored/local and are blocked from Git and
deployment until explicit clarification is recorded. ESA's licence for the original
1997 catalogue is not inherited by I/311.

**Spike migration record (2026-07-26):** previous candidate: CDS I/239; current local
spike source: CDS I/311. UFUQ obtained, studied, and prepared I/311 and does not require
two Hipparcos spike pipelines. This history does not prevent a reviewed Gaia or other
release from coexisting with or replacing astrometric records through the internal
`starId` crosswalk.

**Milestone 2D.1 authority audit (2026-08-16):** fixed-release Gaia DR3 version 1.1,
table `gaiadr3.gaia_source`, is the preferred single-source-first production candidate.
Its official schema supplies ICRS astrometry at a TCB-typed Julian `J2016.0`,
`mu_alpha_star`, declination motion, parallax, formal errors/correlations, quality
evidence, and subset radial velocity. ESA's credit page says open/free with credit and
the DOI record separately declares CC BY-NC 3.0 IGO distribution metadata. Their exact
application to a UFUQ derived artifact is not inferred: local analysis and attribution
are established, but derived-output deployment and public Git tracking remain
`RIGHTS_INTERPRETATION_REQUIRED`, noncommercial FYP use is only a candidate pending
exact licence application, and commercial reuse is not approved. This is not an active
catalogue approval. A bounded official TAP screen preliminarily found 8/19 technical
matches and five finite-RV candidates but no `HIP 11767` match; the counts are not
reproducible 2D authority until the exact query, response/canonical extraction,
timestamp, hashes and manifest are retained. Immutable acquisition
and row review must still prove physical-component identity, applicable five-/six-
parameter covariance, explicit unknown astrometry-RV cross-covariance disposition,
positive-parallax systematics, finite scientifically suitable RV/proxy approval, and
quality. Milestone 2D.1A approves the scale-aware
`GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1` parameter/covariance mapping while preserving the
native TCB evidence; it does not approve a row or make Gaia's spectroscopic RV an
automatic kinematic/systemic value. Gaia's crossmatch is identity evidence rather than
automatic eligibility. ESA Hipparcos 1997 is the smallest Polaris
astrometry fallback candidate but has no general RV; one primary systemic-RV authority
and field-specific crosswalk remain open. I/311 remains production-ineligible on its
unresolved epoch/derivative scale, RV, row, and redistribution evidence. See
`../spikes/PHASE1_PRODUCTION_CATALOGUE_AUTHORITY.md`.

## Consequences

- Scientific source updates do not overwrite cultural judgement, and cultural edits cannot alter coordinates.
- Lesson components and alternative paths can be composed from versioned data without
  hardcoding one named pattern as the route entry point.
- Missing scenario stars exclude an otherwise valid route instead of producing a
  partial or misleading lesson.
- A scenario/attempt can record one catalogue hash for replay.
- The pipeline may need local/private raw data if redistribution is not permitted.
- Stable internal IDs prevent cultural records from depending on copied coordinates or
  one catalogue's identifier namespace.
- Identifier crosswalks do not establish historical membership, pattern edges,
  directional use, or lesson approval.
- Multiple source records and crossmatches retain independent per-field authority;
  proximity, release recency, or a populated field never promotes another source,
  component, or field.
- Manual expert and licence gates are real schedule dependencies.
- Numerical and cultural schemas remain logically separate without the manifest,
  reference, and build overhead of separate npm packages.

## Alternatives rejected

- Copy coordinates from web pages or the report.
- Key stars by display name/transliteration.
- Store static cultural content only in mutable operational DB tables; DEV-009 records this report interpretation.
- Query a large live catalogue from the learner browser.

## Validation

Deterministic rebuild and SHA-256, schema/range/unit checks, unique internal `starId`
and source-release crosswalk checks, pattern/relationship/route referential integrity,
required-star availability filtering, alternative-path
composition, zero unapproved learner-facing curation, scientific/cultural sample
review, reference astronomy rerun, visual review, and licence/artifact scan.
