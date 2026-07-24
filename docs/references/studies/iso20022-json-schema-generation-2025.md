# Bibliographic identity

- Canonical source ID: `ISO20022-JSON-2025`.
- Title: *Generation of JSON Schema Draft 2020-12 for ISO 20022:2013:
  Financial Services — Universal Financial Industry Message Scheme*.
- Author/editor: members of the ISO 20022 Registration Management Group and
  Technical Support Group; named editors in the local publication record are
  Myles Houghton, Christian Frei, and Jason Polis.
- Edition/version: ISO 20022 TSG recommendation approved for publication
  10 June 2025; the title-page warning says it is not an ISO International
  Standard and may change without notice.
- Year/publisher: 2025; ISO 20022 Technical Support Group.
- DOI/ISBN/standard identifier: none. It supplements the ISO 20022:2013
  metamodel and is not itself an International Standard.
- Local file:
  `local-reference/standards/json-schema/2020-12/iso20022-json-schema-generation-2025.pdf`.
- Page count: 49 PDF pages; the main numbered material reaches p. 35 and is
  followed by four annexes through p. 49.
- Text layer: reliable searchable text.
- Verification status: title, date, issuing groups, warning, copyright,
  contents, and scope were inspected; identity agrees with the
  [official ISO 20022 listing](https://www.iso20022.org/about-iso-20022/apis-and-iso-20022).
  Acquisition provenance remains unverified.

# UFUQ relevance

- Classification: `NOT_RELEVANT_TO_UFUQ` and `NOT_REQUIRED`.
- Phases affected: none. The source does not control Phase 1 schema semantics.
- Project decision affected: it reinforces `SOURCE_GAPS.md`'s warning that
  this local PDF cannot close `DATA-SRC-002`.
- Sections studied: title/warning p. 1; contents pp. 2-3; Foreword p. 4;
  Introduction p. 5; §§1-4 and the opening of §5, pp. 6-7; revision-history
  extent identified from the contents.
- Sections intentionally not studied: ISO 20022 transformation rules and
  informative annexes, pp. 8-49. Those rules transform a financial messaging
  metamodel into schemas and have no UFUQ catalogue or provenance use.
- Scope reason: establish identity and prevent accidental promotion to JSON
  Schema authority, not extract reusable financial-message patterns.

# Terminology

- **MessageSet / MessageDefinition**: ISO 20022 metamodel constructs used as
  inputs to the paper's transformation (Introduction and §5, pp. 5-7).
- **Syntax generation**: deterministic transformation from ISO 20022 logical
  metamodel constructs to a physical JSON Schema representation (§§1, 5,
  pp. 6-7).
- **Recommendation**: the document's own title-page status; it explicitly is
  not an ISO International Standard (p. 1).

# Concepts and models

The paper specifies how repositories conforming to ISO 20022-1:2013 can
generate Draft 2020-12 schemas for financial message definitions
(Introduction and §1, pp. 5-6). Its normative context is the ISO 20022
metamodel, not an astronomical catalogue, a generic provenance manifest, or
UFUQ's serialized data classes.

The paper itself depends on the JSON Schema Core specification (§2, p. 6).
That dependency establishes the authority direction: official JSON Schema
Core/Validation define keyword semantics; this paper applies some of those
semantics to ISO 20022.

# Equations and algorithms

- Source location: §5 "Method", p. 7, with detailed transformation rules in
  pp. 9-35.
- Inputs: a valid ISO 20022 `MessageSet`/`MessageDefinition`.
- Output: a JSON Schema representation of that financial message definition.
- Assumptions: conformance to the ISO 20022 metamodel and its naming/tag
  algorithms.
- Units and numerical concerns: ISO 20022 domain-specific and not studied for
  UFUQ.
- UFUQ use: none.
- Required independent validation: none for UFUQ; do not implement or test
  this transformation.

# Conventions

- No convention in this paper is adopted by UFUQ.
- Its use of UTF-8 for derived ISO 20022 messages (§5.2.1, p. 7) does not
  define UFUQ's canonical serialization policy.
- Its completeness restriction (§5.2.2, p. 7) applies only to the stated ISO
  20022 transformation.

# Implementation implications

- `SOURCE_REQUIRED` — Use official JSON Schema Draft 2020-12 Core and
  Validation for UFUQ schema semantics; this paper expressly cites Core as a
  dependency (§2, p. 6).
- `INFORMATIONAL_ONLY` — Retain the corrected bibliographic identity so a
  filename or old download label cannot cause this paper to be treated as the
  JSON Schema specification (title/warning p. 1; scope p. 6).
- `PROJECT_DECISION_REQUIRED` — `DATA-SRC-002` remains open until UFUQ pins a
  conforming validator and conformance tests.
- No implementation-affecting rule is derived from the transformation
  chapters.

# Testing implications

- Add no test based on ISO 20022 financial-message transformation rules.
- Repository reference validation should ensure this source is never cited as
  the authority for a JSON Schema keyword or UFUQ field.
- Any schema test must cite the official Core/Validation sections and the
  selected runtime validator, not this PDF.

# Limitations

- The paper is not a JSON Schema specification.
- It is not an ISO International Standard.
- It does not address astronomical catalogues, provenance manifests,
  deterministic catalogue generation, scientific units, or UFUQ data
  classes.
- It cannot select or validate a UFUQ runtime validator.
- Acquisition provenance for the local PDF is unverified.

# Conflicts and ambiguities

- The original local filename suggested a generic Draft 2020-12
  specification, while the title page identifies an ISO 20022 generation
  recommendation. The title page controls.
- The document uses normative language internally, but the title-page warning
  limits its status and its requirements remain scoped to the ISO 20022
  transformation.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Not an ISO International Standard | Title-page warning, p. 1 | Do not promote the paper to standards authority | `INFORMATIONAL_ONLY` |
| Financial-message transformation scope | Introduction p. 5; §§1 and 5, pp. 6-7 | No UFUQ catalogue/provenance rule is derived | `INFORMATIONAL_ONLY` |
| JSON Schema Core is an external dependency | §2, p. 6 | Cite official Core/Validation for keyword semantics | `SOURCE_REQUIRED` |
| Local filename/title discrepancy | Title p. 1; contents pp. 2-3 | Preserve corrected identity in registers and notes | `INFORMATIONAL_ONLY` |
| Runtime validator remains unselected | No supporting section in this paper; `SOURCE_GAPS.md` `DATA-SRC-002` | Stop validator claims pending a project decision and tests | `PROJECT_DECISION_REQUIRED` |
