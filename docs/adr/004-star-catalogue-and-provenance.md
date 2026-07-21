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
Join separately reviewed cultural mappings, segment edges, and educational metadata by
stable catalogue ID. Validate schemas/review status and emit canonically serialized,
versioned runtime JSON plus checksums consumed identically by browser and API.

Hipparcos Main Catalogue/CDS I/239 is only a candidate. No source, row, Arabic spelling, transliteration, membership, pointer relation, segment, licence interpretation, or redistribution is approved by this ADR. Generated rows are never edited manually.

## Consequences

- Scientific source updates do not overwrite cultural judgement, and cultural edits cannot alter coordinates.
- A scenario/attempt can record one catalogue hash for replay.
- The pipeline may need local/private raw data if redistribution is not permitted.
- Manual expert and licence gates are real schedule dependencies.

## Alternatives rejected

- Copy coordinates from web pages or the report.
- Key stars by display name/transliteration.
- Store static cultural content only in mutable operational DB tables; DEV-009 records this report interpretation.
- Query a large live catalogue from the learner browser.

## Validation

Deterministic rebuild and SHA-256, schema/range/unit checks, referential integrity, zero unapproved curation, scientific/cultural sample review, reference astronomy rerun, visual review, and licence/artifact scan.
