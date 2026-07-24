---
name: ufuq-catalogue-provenance
description: Prepare or review UFUQ astronomical-catalogue acquisition manifests, raw-byte checksums, parsing, normalization, runtime schemas, deterministic artifacts, and provenance evidence. Use for catalogue data-flow and generated-data work; do not use for coordinate transformations, cultural-content approval, or ordinary application DTOs.
---

# UFUQ Catalogue Provenance

Keep numerical catalogue data reproducible and separate from cultural curation.

## Trigger conditions

Use this skill when a task changes or reviews:

- a catalogue source, acquisition manifest, query, checksum, parser, field mapping,
  normalization rule, or quality/null policy;
- catalogue/content/artifact schemas or framework-free runtime validation;
- deterministic serialization, generated artifacts, licensing, or provenance records;
- links from curated patterns/routes to stable catalogue identifiers.

Do not trigger it for:

- coordinate, time, observer, or horizon calculations after rows are loaded; use
  `ufuq-astronomy-validation`;
- approval of Arabic names, pattern membership, or cultural routes; use
  `ufuq-najdi-arabian-sky`;
- Qibla inverse geodesics; use `ufuq-qibla-geodesy`;
- unrelated API DTO, database-row, or React-prop design.

## Required project files

Read `AGENTS.md`, `docs/DATA_STRATEGY.md`, `docs/ASTRONOMY_SPEC.md`,
`docs/IMPLEMENTATION_DECISIONS.md`, `docs/PHASES.md`, `docs/TEST_PLAN.md`,
`docs/adr/004-star-catalogue-and-provenance.md`, and
`docs/adr/007-testing-and-validation.md`. Read the selected source manifest, catalogue
`ReadMe`, `docs/references/UFUQ_SOURCE_REGISTER.md`,
`docs/references/SOURCE_GAPS.md`,
`docs/references/syntheses/catalogue-provenance-synthesis.md`, and this skill's four
reference files. Open only the study dossiers linked for the affected rule by
`references/traceability.md`.

## Source authority order

1. The selected archive's official catalogue metadata and byte-level `ReadMe`.
2. The approved acquisition/licence manifest and verified raw-byte checksum.
3. The catalogue's validation publication for scientific quality context.
4. JSON Schema Draft 2020-12 Core and Validation for serialized schema semantics.
5. UFUQ data decisions and deterministic-build requirements.
6. FAIR guidance and basic PROV-DM terminology as optional workflow aids.

Formal PROV semantics are not required. FAIR guidance does not establish compliance.

## Mandatory workflow

1. Identify the source/table/release and record the canonical URL, retrieval method,
   timestamp, licence status, selected columns, filters, and expected records.
2. Execute the chain without skipping a boundary:
   `source -> acquisition manifest -> ignored raw bytes -> checksum verification ->
   parsing -> normalization -> runtime schema validation -> deterministic serialization
   -> generated artifact and provenance`.
3. Verify the raw SHA-256 before parsing. Keep raw bytes immutable and ignored unless a
   separate redistribution decision permits tracking them.
4. Parse units, nulls, quality flags, reference epoch/frame, identifiers, and field
   semantics from official metadata. Never infer them from column names alone.
5. Normalize into catalogue records without cultural labels, copied coordinates, or
   lesson geometry. Join curation only by stable identifiers in a later validated step.
6. Validate catalogue, content, and artifact envelopes at their trust boundaries.
7. Serialize explicitly as UTF-8 with LF, deterministic key/record ordering, Unicode
   policy, numeric formatting, and excluded volatile metadata. Rebuild twice and
   compare bytes/hashes.
8. Record input/tool/schema/output versions, checksums, row counts, licence status, and
   every omission or drift. Confirm every mandatory conclusion has a basis in
   `references/traceability.md`, then report with `references/output-template.md`.

## Required evidence

- Official source metadata and acquisition/licence manifest.
- Raw and normalized checksums plus expected/actual record counts.
- Field-level unit/null/quality/epoch/frame mapping.
- Schema-validation results for valid and invalid cases.
- Two-build byte/hash equality under the recorded environment.
- Referential-integrity checks for every curated catalogue ID.
- A trace from each artifact field back to its numerical or curated source.

## Stop conditions

Stop the affected artifact or release claim when source identity, licence/redistribution,
raw checksum, field semantics, frame/epoch, required quality policy, or deterministic
serialization is unresolved. Stop when a source drifts, a curated ID does not resolve,
or generated output can only be reproduced from manually copied values.

## Prohibited assumptions

Do not manually copy catalogue coordinates. Do not embed cultural labels, memberships,
or routes into numerical catalogue rows. Do not treat a public URL as redistribution
permission. Do not claim FAIR compliance without an explicit evaluation. Do not make
the pipeline depend on formal PROV semantics.

## Required output

Use `references/output-template.md`. Classify claims as `SOURCE_SUPPORTED_FACT`,
`PROJECT_DECISION`, `PROVISIONAL_CHOICE`, or `UNRESOLVED_QUESTION`. Separate source
provenance, transformation evidence, artifact evidence, and release limitations.

## Relevant validation commands

Use only applicable repository commands:

```text
npm run data:verify
npm run test
npm run test:reference
npm run boundaries
```

`test:reference` is mandatory only after Phase 1 introduces a real comparison. Add
targeted deterministic rebuild and checksum commands from the approved catalogue tool;
do not add a fake passing data test.
