# Catalogue and provenance synthesis

## Scope and authority

This synthesis joins:

- the ESA 1997 guide to original Hipparcos catalogue semantics;
- the Hipparcos I/311 `ReadMe`, Appendix G field tables, and validation paper;
- JSON Schema Draft 2020-12 Core and Validation;
- the FAIR principles;
- basic concepts from PROV Semantics; and
- UFUQ's approved data strategy and ADR-004.

The local ISO 20022 JSON-generation paper is intentionally excluded from the authority
chain. It applies Draft 2020-12 to financial-message definitions and supplies no UFUQ
schema or catalogue requirement.

## End-to-end evidence chain

```text
official source metadata
-> approved acquisition manifest
-> ignored immutable raw bytes
-> checksum and file-structure verification
-> field-aware parsing
-> unit/frame/epoch/quality normalization
-> runtime schema validation
-> deterministic canonical serialization
-> generated artifact plus explicit derivation evidence
```

Each arrow is evidence-bearing. Schema validity cannot replace source identity,
checksum verification, licence review, field semantics, scientific validation,
referential integrity, or deterministic byte comparison.

## Authority by topic

| Topic | Controlling source | Supporting source | Limit |
|---|---|---|---|
| Original 1997 H-field model, epoch, and units | ESA SP-1200 Volume 1 §§1.2, 1.5, and 2.1 | I/311 cross-reference to I/239 | The definitions apply to the original catalogue and do not establish I/311 identity. |
| I/311 files, fields, units, solution types, corrections | I/311 `ReadMe` and Appendix G Tables G.2–G.7 | van Leeuwen 2007 | I/311 is selected for the local spike; individual rows still need quality review. |
| I/311 scientific-use and attribution terms | Official VizieR rules plus I/311 ReadMe | ESA terms only for the original 1997 catalogue | Local scientific use is permitted with citation; I/311 raw/derived redistribution and deployment remain unresolved and fail closed. |
| Scientific quality/error context | van Leeuwen §§2-5 plus row metadata | I/311 weight/error fields | Aggregate findings do not become per-star tolerances. |
| Schema dialect/keyword semantics | JSON Schema Core/Validation 2020-12 | Selected validator documentation/conformance tests | A declared dialect does not prove library support. |
| Stable IDs, metadata, licences, reuse prompts | FAIR Box 2 | UFUQ manifests | FAIR is guidance; no compliance claim. |
| Entity/activity/agent and explicit derivation vocabulary | PROV Semantics §§3.2-3.5 | UFUQ manifest fields | No formal PROV semantics or conformance. |
| Canonical serialization and hashes | `docs/DATA_STRATEGY.md` and ADR-004 | Reproducible-computing studies | JSON Schema treats object order and numeric lexical form separately. |

## Agreements

- Raw input identity and the exact transformation history must be explicit.
- Stable identifiers should connect numerical rows, curation, manifests, and artifacts
  without duplicating coordinates.
- Metadata, data, tools, activities, schemas, and outputs can have different versions
  and access conditions.
- Licence and provenance must be recorded; neither FAIR nor a public URL grants
  redistribution.
- Validation occurs at trust boundaries and needs negative cases.
- Deterministic generation requires explicit encoding, line endings, ordering, Unicode,
  numeric formatting, and volatile-field rules beyond schema validity.

## Important distinctions

| Distinction | Consequence |
|---|---|
| Schema assertion versus annotation | Required type/null/cardinality/closure behavior must be expressed and tested; `format` is not silently assumed to assert. |
| Abstract JSON number versus JavaScript number | UFUQ needs separate finite/range/precision rules and runtime experiments. |
| Schema identity URI versus network retrieval | Schemas can be preloaded and resolved offline; URI presence does not authorize network access. |
| Source provenance versus scientific correctness | A perfectly traced row can still be scientifically unsuitable, and a plausible row can still lack provenance. |
| Numerical catalogue versus cultural curation | Catalogue rows contain no cultural labels, memberships, line segments, or lesson routes. Curation links by stable ID. |
| Original field terminology versus new-reduction mapping | I/311 Appendix G now defines its own `mu_alpha_star` field. ESA 1997 remains original-catalogue context, not the basis of the I/311 mapping. |
| Provenance vocabulary versus formal reasoning | UFUQ may record entity/activity/agent-like relationships without claiming PROV conformance. |
| FAIR guidance versus FAIR compliance | The principles improve review questions but provide no UFUQ certification method. |

## Candidate UFUQ rules

| Rule | Evidence | Classification |
|---|---|---|
| Pin source/table/release, corrected file variant, retrieval method/time, licence status, selected fields/filters/order, expected counts, and raw SHA-256 before parsing. | I/311 `Notice`, `File Summary`; `DATA_STRATEGY.md` | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Verify raw bytes before transformation and keep them immutable/ignored unless redistribution is separately approved. | Wilson 2017 p. 2; ADR-004 | `PROJECT_DECISION` |
| Parse from byte-level metadata, including mixed units, solution types, quality fields, and covariance semantics. | I/311 byte descriptions, Notes, Global Note G1 | `SOURCE_SUPPORTED_FACT` |
| Preserve I/311 `pmRA` as `properMotionRaCosDecMilliarcsecondsPerYear`; map directly to Astropy `pm_ra_cosdec` after unit conversion and prohibit a second cosine operation. | I/311 Appendix G Table G.3, printed p. 407 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Preserve cultural curation outside numerical catalogue rows and join only through validated stable identifiers. | `DATA_STRATEGY.md`; Wilson 2014 single-authority principle | `PROJECT_DECISION` |
| Declare Draft 2020-12 explicitly, assign stable `$id`, and pin required vocabularies and offline reference behavior. | Core §§8-9 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION_REQUIRED` |
| Use schema meta-validation, negative fixtures, and validator conformance checks; unknown/misspelled keywords must not silently weaken an approved schema. | Core §§4.3.1, 6.5; Validation §§5-6 | `SOURCE_SUPPORTED_FACT` |
| Decide and test `format`, composed-object closure, number handling, and structured error output in the chosen validator. | Core §§10-12; Validation §7 | `EXPERIMENT_REQUIRED` |
| Serialize canonically as explicitly approved and rebuild twice to compare bytes/hashes. | `DATA_STRATEGY.md`; JSON Core §§4.2.1-4.2.2 | `PROJECT_DECISION` |
| Record explicit input/activity/output derivation links, tool/schema versions, and hashes without claiming formal PROV conformance. | PROV Semantics §3.2.4.6; ADR-004 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Do not claim FAIR compliance without a selected assessment method, scope, and evidence. | FAIR, “The Principles precede implementation,” p. 5 | Stop condition |

## Required tests

- Manifest schema and invalid acquisition/licence/version cases.
- Hash mismatch and source-drift failure before parsing.
- Exact fixed-width record length/count and selected-field byte boundaries.
- Unit, null, quality, solution-family, supplemental-row, and covariance mapping.
- Explicit `pmRA` normalization cases for high declination, J1991.25, and omitted or
  double application of `cos(delta)`, compared with a pinned independent oracle.
- Schema meta-validation, wrong types, explicit nulls, missing/unknown fields, invalid
  identifiers/enums, local `$ref` failures, duplicate `$id`, composition closure, and
  numeric edge cases.
- Referential integrity from curation to numerical catalogue IDs.
- Two clean builds with identical canonical bytes and hashes.
- Provenance graph checks from each output field/artifact to source or reviewed
  curation, including tool/schema versions and licence status.

## Unresolved gaps

- I/311 is the approved sole source for the Phase 1 local technical spike. Local
  scientific processing is constrained to ignored storage; acquisition provenance is
  partial and raw/derived redistribution remains unresolved.
- The parser field, missing/duplicate/multiplicity, candidate-selection, schema, and
  fail-closed quality-review policies are recorded in the Milestone 2B audit.
- I/311 `pmRA` is confirmed as `mu_alpha_star`; the exact epoch time-scale mapping still
  needs astronomy approval before propagation.
- No runtime JSON Schema validator has been selected or proven conformant.
- Generated-artifact tracking remains subject to source licence and provenance
  decisions.
- No current evidence supports formal FAIR compliance or a need for formal PROV
  reasoning.
