# ADR-004: Star catalogue, cultural curation, and provenance

- **Status:** Parser contract accepted for Phase 1 / Milestone 2E after Milestone 2D source/deployment-authority resolution; release and cultural gates remain blocked
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
and `LessonRoute`/educational metadata by stable IDs. `SkyPattern` owns names/labels,
member catalogue IDs, segments, and cultural status; `GuidanceRelationship` owns a
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

CDS I/311, *Hipparcos, the New Reduction*, is the sole catalogue source approved for
the Phase 1 local technical spike. Use the corrected author-replacement files dated
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

**Migration record (2026-07-26):** previous candidate: CDS I/239; current Phase 1
source: CDS I/311. UFUQ obtained, studied, and prepared I/311 and does not require two
Hipparcos pipelines.

## Consequences

- Scientific source updates do not overwrite cultural judgement, and cultural edits cannot alter coordinates.
- Lesson components and alternative paths can be composed from versioned data without
  hardcoding one named pattern as the route entry point.
- Missing scenario stars exclude an otherwise valid route instead of producing a
  partial or misleading lesson.
- A scenario/attempt can record one catalogue hash for replay.
- The pipeline may need local/private raw data if redistribution is not permitted.
- Identifier crosswalks do not establish historical membership, pattern edges,
  directional use, or lesson approval.
- Manual expert and licence gates are real schedule dependencies.
- Numerical and cultural schemas remain logically separate without the manifest,
  reference, and build overhead of separate npm packages.

## Alternatives rejected

- Copy coordinates from web pages or the report.
- Key stars by display name/transliteration.
- Store static cultural content only in mutable operational DB tables; DEV-009 records this report interpretation.
- Query a large live catalogue from the learner browser.

## Validation

Deterministic rebuild and SHA-256, schema/range/unit checks, pattern/relationship/route
referential integrity, required-star availability filtering, alternative-path
composition, zero unapproved learner-facing curation, scientific/cultural sample
review, reference astronomy rerun, visual review, and licence/artifact scan.
