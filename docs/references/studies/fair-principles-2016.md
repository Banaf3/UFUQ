# Bibliographic identity

- Canonical source ID: `FAIR-2016`.
- Title: *The FAIR Guiding Principles for Scientific Data Management and
  Stewardship*.
- Authors: Mark D. Wilkinson et al.
- Edition/version: journal Comment, *Scientific Data* 3, article 160018.
- Year/publisher: 2016; Nature Portfolio / *Scientific Data*.
- DOI: `10.1038/sdata.2016.18`.
- Local file:
  `local-reference/data-governance/fair/fair-guiding-principles-2016.pdf`.
- Page count: 9 PDF/article pages.
- Text layer: reliable searchable text.
- Verification status: title, authors, dates, DOI, copyright, and article
  extent agree with the
  [publisher record](https://www.nature.com/articles/sdata201618).
  Acquisition provenance of the local copy remains unverified.

# UFUQ relevance

- Phases affected: supporting guidance for Phase 1 acquisition manifests,
  stable identifiers, metadata, licensing, provenance, and artifact
  stewardship.
- Project decisions affected: `UFUQ-DATA` and `UFUQ-ADR-004`.
- Sections studied: opening summary and "Supporting discovery through good
  data management" pp. 1-2; "The significance of machines..." pp. 3-4;
  Box 2 and "The FAIR Guiding Principles in detail" pp. 4-5; "The Principles
  precede implementation" p. 5; conclusion p. 7.
- Sections intentionally not studied in detail: domain examples on pp. 5-6,
  community-initiative survey, author affiliations, and references pp. 7-9.
  They do not establish additional UFUQ rules.
- Scope reason: derive data-hygiene prompts while preserving the project's
  explicit rule not to claim formal FAIR compliance.
- Classification: `SUPPORTING_NOW`; the paper's principles are high-level
  guidance, not an implementation specification.

# Terminology

- **FAIR**: Findable, Accessible, Interoperable, and Reusable (Box 1, p. 2).
- **Machine-actionable**: a continuum in which a computational agent can
  identify, assess, access under applicable constraints, and act on a digital
  object based on its metadata and content ("The significance of machines...",
  pp. 3-4).
- **(Meta)data**: the paper's shorthand when a principle applies to both
  metadata and data (Box 2 and following discussion, p. 4).
- **Persistent identifier**: a globally unique, durable identifier for data
  or metadata (F1, Box 2, p. 4).
- **Qualified reference**: a semantically described relation to other data or
  metadata (I3, Box 2, p. 4).
- **Detailed provenance**: contextual history associated with reusable data
  (R1.2, Box 2, p. 4).

# Concepts and models

## FAIR applies to more than final data

The opening discussion extends the principles to algorithms, tools, and
workflows leading to data (p. 1). For UFUQ, this supports describing source
manifests, transformation tools, schemas, and generated artifacts—not merely
the final JSON.

## Findability

F1-F4 call for globally unique persistent identifiers, rich metadata,
metadata that names the described data, and registration/indexing in a
searchable resource (Box 2, p. 4). Current UFUQ can apply the first three as
design prompts. Public indexing is constrained by licences and project scope
and is not required.

## Accessibility

A1-A2 distinguish retrievability by standardized protocol (with
authentication where needed) from permanent openness; metadata can remain
accessible when data are unavailable (Box 2, p. 4). This is compatible with
keeping raw licensed catalogue bytes private while tracking a permissible
manifest and citation. It does not itself settle redistribution rights.

## Interoperability

I1-I3 emphasize shared formal representation, FAIR vocabularies, and
qualified references (Box 2, p. 4). For UFUQ, a versioned JSON Schema and
stable links between catalogue IDs, manifests, and artifacts improve
machine interpretation, but schema validity alone does not establish full
interoperability.

## Reusability

R1-R1.3 require rich accurate attributes, clear usage licence, detailed
provenance, and domain-relevant community standards (Box 2, p. 4). These
principles directly motivate licence fields, source/version/hash records, and
official catalogue metadata. They do not create a licence or substitute for
the catalogue authority.

## Principles precede implementation

The paper states that FAIR principles do not prescribe a technology,
standard, or implementation and are not themselves a specification
("The Principles precede implementation", p. 5). Therefore they cannot choose
JSON Schema, PROV, a repository, a checksum, or a serialization format for
UFUQ.

# Equations and algorithms

The paper contains no normative equation or executable algorithm.

- Source location: Box 2, p. 4, supplies a checklist of principles rather than
  a scoring method.
- Inputs/outputs/units: not defined.
- Assumptions: application is domain- and implementation-specific.
- UFUQ use: requirements-review prompts for IDs, metadata, licences,
  provenance, and standards.
- Required independent validation: any FAIR compliance or maturity claim
  would require a separately selected assessment method and evidence; none is
  currently approved.

# Conventions

- Use the labels F1-F4, A1-A2, I1-I3, and R1-R1.3 only as the paper defines
  them (Box 2, p. 4).
- Accessibility is not identical to unrestricted public access; authenticated
  access can satisfy the protocol principle (A1.2).
- Metadata and data may have different accessibility/retention status (A2).
- A persistent identifier must identify the described object/version
  unambiguously; a mutable filename alone is not enough.
- FAIR guidance does not override licence, privacy, cultural review, or source
  authority.

# Implementation implications

- `SOURCE_REQUIRED` — Assign stable identifiers and versions to source,
  schema, tool, and generated artifacts, and make metadata explicitly identify
  the described artifact (F1-F3, Box 2, p. 4).
- `SOURCE_REQUIRED` — Record a clear licence/usage status and detailed
  provenance with each releasable artifact (R1.1-R1.2, Box 2, p. 4).
- `SOURCE_REQUIRED` — Use official domain metadata and standards where
  available rather than inventing catalogue semantics (R1.3, Box 2, p. 4).
- `PROJECT_DECISION_REQUIRED` — Determine what metadata may be tracked when
  raw bytes cannot be redistributed; A2 supports the distinction but does not
  decide UFUQ's licence status.
- `INFORMATIONAL_ONLY` — Machine-actionable metadata is a design direction,
  not a claim that a JSON Schema alone makes the pipeline interoperable
  (pp. 3-4).
- `PROJECT_DECISION_REQUIRED` — UFUQ must not claim FAIR compliance. The
  source supplies principles but no conformance test, scoring threshold, or
  certification method (p. 5).
- `INFORMATIONAL_ONLY` — Public registration/indexing (F4) is not required for
  the current private raw catalogue workflow and must not cause restricted
  material to be published.

# Testing implications

- Verify stable identifiers are non-empty, unique, versioned where needed, and
  referenced consistently between manifest, schema, output, and scenario
  records.
- Verify every generated artifact identifies its input versions/hashes,
  generator version, schema version, and licence status.
- Verify metadata points to the exact artifact/hash it describes.
- Verify restricted/unavailable data can still be traced through permissible
  metadata without exposing raw bytes.
- Verify links between records are qualified by an explicit relation/field
  meaning and pass referential integrity.
- Treat any claimed FAIR status as a stop condition until an assessment method,
  scope, evaluator, and evidence are approved.

# Limitations

- The principles are deliberately technology-neutral and do not define a
  manifest schema, checksum algorithm, canonical JSON encoding, validator, or
  repository.
- The paper does not grant data licences or decide redistribution.
- It does not establish scientific accuracy, source authenticity, or
  catalogue-field semantics.
- It gives no formal compliance algorithm or threshold.
- A subset of principles can guide work without justifying a global
  "FAIR-compliant" label.

# Conflicts and ambiguities

- FAIR encourages access and reuse, while UFUQ may be unable to redistribute
  raw catalogue bytes. A1.2 and A2 allow access controls and persistent
  metadata, but actual rights remain a licence decision.
- The paper uses "FAIRness" as a continuum and allows incremental application
  (p. 4), but UFUQ deliberately avoids a compliance claim because no
  evaluation framework is approved.
- F4's searchable registration is broader than the current local pipeline.
  It is guidance, not permission to publish a source or generated artifact.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Principles apply to data, tools, and workflows | Opening discussion, p. 1 | Describe inputs, transforms, schemas, and outputs | `SOURCE_REQUIRED` |
| Stable IDs and rich linked metadata | F1-F3, Box 2, p. 4 | Version and link manifests/artifacts unambiguously | `SOURCE_REQUIRED` |
| Controlled access and persistent metadata | A1.2 and A2, Box 2, p. 4 | Keep permissible metadata when raw data are restricted | `PROJECT_DECISION_REQUIRED` |
| Shared representations and qualified references | I1-I3, Box 2, p. 4 | Use versioned schemas and explicit typed links | `SOURCE_REQUIRED` |
| Licence, provenance, community standards | R1.1-R1.3, Box 2, p. 4 | Record rights/provenance; follow official catalogue metadata | `SOURCE_REQUIRED` |
| Principles do not prescribe implementation | "The Principles precede implementation", p. 5 | FAIR cannot select JSON Schema, PROV, or repository tooling | `INFORMATIONAL_ONLY` |
| No approved compliance method | Box 2 p. 4 and implementation discussion p. 5 | Do not claim formal FAIR compliance | `PROJECT_DECISION_REQUIRED` |
