# ADR-004: Star catalogue, cultural curation, and provenance

- **Status:** Blocked pending manual domain decisions
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

The schema is not Banat Na'sh-specific. It permits reviewed helper patterns to lead to
Banat Na'sh or Dhat al-Kursi, either pattern to lead to Al-Jady, and subsequent
Al-Jady→True North→Qibla direction steps. The server may select a route only when all
stars required by its resolved patterns/relationships are available in the approved
scenario.

Hipparcos Main Catalogue/CDS I/239 is only a candidate. No source, row, helper pattern,
Arabic spelling, transliteration, membership, guidance relationship, instructional
geometry/explanation, segment, lesson route, licence interpretation, or redistribution
is approved by this ADR. Generated rows are never edited manually.

## Consequences

- Scientific source updates do not overwrite cultural judgement, and cultural edits cannot alter coordinates.
- Lesson components and alternative paths can be composed from versioned data without
  hardcoding one named pattern as the route entry point.
- Missing scenario stars exclude an otherwise valid route instead of producing a
  partial or misleading lesson.
- A scenario/attempt can record one catalogue hash for replay.
- The pipeline may need local/private raw data if redistribution is not permitted.
- Manual expert and licence gates are real schedule dependencies.

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
