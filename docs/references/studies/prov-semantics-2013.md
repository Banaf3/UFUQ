# Bibliographic identity

- Canonical source ID: `PROV-SEM-2013`.
- Title: *Semantics of the PROV Data Model*.
- Editor: James Cheney, University of Edinburgh.
- Edition/version: W3C Working Group Note, 30 April 2013.
- Publisher: World Wide Web Consortium (W3C), Provenance Working Group.
- DOI/ISBN/standard identifier: none; dated URI
  `http://www.w3.org/TR/2013/NOTE-prov-sem-20130430/`.
- Local file:
  `local-reference/standards/w3c-prov/2013/prov-semantics.pdf`.
- Page count: 33 PDF pages.
- Text layer: reliable searchable text.
- Verification status: title, editor, date, status, contents, and copyright
  match the [official W3C Note](https://www.w3.org/TR/prov-sem/).
  Acquisition provenance of the local copy remains unverified.

# UFUQ relevance

- Phases affected: optional terminology support for Phase 1 acquisition and
  generated-artifact provenance.
- Project decisions affected: `UFUQ-DATA` and `UFUQ-ADR-004`; both require
  practical manifests but not formal PROV reasoning.
- Sections studied:
  - Abstract and Status, PDF pp. 1-2;
  - §§1-1.3, PDF p. 3;
  - §§2.1-2.5, PDF pp. 3-4;
  - §§3.1-3.5, PDF pp. 5-9;
  - the semantics organization in §4 and validity relationship described in
    §§1.1-1.2.
- Sections intentionally not studied in detail: individual satisfaction
  clauses in §§4.2-4.5, formal inference/constraint proofs in §5, and
  soundness/completeness construction in §6. They are unnecessary because
  UFUQ is not implementing PROV validation or reasoning.
- Scope reason: extract careful entity/activity/agent/derivation terminology
  and understand its limits without importing a formal semantics requirement.
- Classification: `SUPPORTING_NOW` only for terminology; formal sections are
  `NOT_RELEVANT_TO_UFUQ` under the current project decision.

# Terminology

- **Provenance**: a record of people/institutions, entities, and activities
  involved in producing, influencing, or delivering data or a thing
  (Introduction, PDF p. 3).
- **Entity**: an object fixing some aspects of a thing during relevant events
  (§3.2.1, PDF pp. 5-6).
- **Activity**: a continuing process with start/end semantics, distinct from
  an entity (§3.2.2, PDF p. 6).
- **Agent**: an object bearing some responsibility for an activity, entity,
  or another agent's activity (§3.2.3, PDF pp. 6-7).
- **Influence**: a relation family covering events, associations,
  attributions, communications, delegations, and derivations (§3.2.4,
  PDF p. 7).
- **Generation / use**: instantaneous events connecting activities and
  entities (§3.2.4.1, PDF p. 7).
- **Derivation**: an explicitly represented influence chaining one or more
  generation/use steps; a possible chain alone does not imply that a
  derivation was asserted (§3.2.4.6, PDF p. 8).
- **Interpretation**: a mapping from identifiers to objects in a PROV
  structure (§3.5, PDF p. 9).

# Concepts and models

## Status of the semantics

The Note supplies one model-theoretic semantics for PROV-DM and relates it to
PROV-CONSTRAINTS validity. It expressly says the semantics is not canonical or
required and does not constrain PROV use (Abstract/Status, PDF pp. 1-2;
§1.1, PDF p. 3). This supports UFUQ's decision not to implement formal PROV
reasoning.

## Entity-activity-agent separation

The model distinguishes artifacts/views (`Entities`), processes
(`Activities`), and responsibility-bearing participants (`Agents`). Basic
manifest fields can borrow this separation: raw/normalized/generated
artifacts are entity-like records, acquisition/normalization/build steps are
activity-like records, and a person or pinned software tool can be described
as an agent-like participant. This is a terminology aid, not a claim that the
manifest is a conforming PROV instance.

## Derivation is explicit

Section 3.2.4.6 does not license inference from any apparent file sequence.
It distinguishes explicit derivations from possible generation/use paths.
For UFUQ, an output-to-input link should be recorded explicitly with hashes
and transformation identity rather than reconstructed from filenames.

## Formal validity model

The Note maps PROV statements to atomic first-order formulas and a PROV
instance to a theory; validity in PROV-CONSTRAINTS corresponds to model
satisfiability under the described conditions (§§1.1-1.2, 2.4-2.5, and 4-6).
UFUQ has no requirement for this normalization, constraint checking, or
satisfiability layer.

# Equations and algorithms

## Formal interpretation and satisfaction

- Source location: §§2.4-2.5, 3.5, and 4.1, PDF pp. 4, 9.
- Model: identifiers map to objects; atomic PROV statements are interpreted in
  a structure; satisfaction defines whether an instance's formulas hold.
- Inputs: a PROV instance, a mathematical structure, and an interpretation.
- Output: satisfaction/validity properties.
- Assumptions: PROV-DM/PROV-CONSTRAINTS concepts and the Note's axioms.
- Valid domain: formal PROV instances, not arbitrary UFUQ JSON.
- Numerical concerns/units: none relevant to UFUQ.
- UFUQ use: none as an executable algorithm.
- Required validation: not applicable unless a future ADR explicitly adopts
  formal PROV conformance.

## Derivation path model

- Source location: §3.2.4.6, PDF p. 8.
- Model: an explicit derivation is linked to a path alternating entities,
  generation events, activities, and use events.
- UFUQ use: informational vocabulary for an explicit
  input → transformation → output trace.
- Required independent validation: UFUQ verifies actual hashes, versions, and
  steps; it does not run PROV inference.

# Conventions

- Use `entity`, `activity`, `agent`, `generation`, `use`, and `derivation`
  only with meanings compatible with §§3.2.1-3.2.4.
- Do not label a UFUQ manifest "PROV conformant" merely because it has fields
  analogous to those concepts.
- Record derivation links explicitly; do not infer them from filename order.
- Keep formal PROV identifiers/relations separate from UFUQ's own stable
  catalogue identifiers unless a future mapping is approved.

# Implementation implications

- `INFORMATIONAL_ONLY` — A provenance record benefits from separating
  artifacts, processes, and responsible people/software using entity/activity/
  agent-like concepts (§§3.2.1-3.2.3, PDF pp. 5-7).
- `SOURCE_REQUIRED` — Record output derivation from specific inputs and
  activities explicitly; a plausible chain is not itself an asserted
  derivation (§3.2.4.6, PDF p. 8).
- `PROJECT_DECISION_REQUIRED` — UFUQ manifests use their approved simple
  schema and terminology; they do not claim PROV conformance or implement
  formal semantics (`UFUQ-DATA`, source-register interpretation control 1).
- `INFORMATIONAL_ONLY` — A software version may be represented as an agent-like
  responsible participant, but exact manifest fields remain a UFUQ decision.
- `PROJECT_DECISION_REQUIRED` — Formal normalization, inference, constraint
  checking, bundles, and satisfiability are outside current scope; adoption
  would require an ADR, source expansion to PROV-DM/PROV-CONSTRAINTS, and new
  tests.

# Testing implications

- Provenance tests should verify concrete UFUQ facts: input/output hashes,
  activity/tool versions, timestamps where non-canonical, and explicit links
  between each output and its inputs.
- Reject an output record whose derivation omits the acquisition,
  normalization, schema, or generator identity required by `UFUQ-DATA`.
- Do not add PROV inference or satisfiability tests.
- Do not claim that passing UFUQ's manifest schema establishes PROV validity.
- If PROV terminology is exposed, test that entity/activity/agent identifiers
  do not collide or silently change meaning across versions.

# Limitations

- This is a W3C Working Group Note, not a W3C Recommendation.
- It says its semantics is neither canonical nor required and places no
  constraints on PROV use (Abstract/Status).
- The proofs were reviewed by the Working Group but not formally peer-reviewed
  as an academic paper (§1.1, PDF p. 3).
- It does not define UFUQ acquisition fields, checksums, deterministic
  serialization, licensing, or catalogue semantics.
- It assumes familiarity with PROV-DM and PROV-CONSTRAINTS (§1.3); this study
  does not promote those full specifications into current UFUQ requirements.
- It does not cover general multi-instance PROV documents, dictionaries, or
  cross-bundle links (§1.1, PDF p. 3).

# Conflicts and ambiguities

- The formal model is much richer than UFUQ's required manifest. There is no
  evidence that formal reasoning would solve a current UFUQ requirement, so
  the smaller project schema controls.
- The Note's term `entity` is a formal provenance concept and must not be
  confused with UFUQ domain entities or database rows.
- A tool can be described as agent-like for responsibility/provenance
  vocabulary, but whether a software agent is encoded as an agent, entity, or
  both is not decided for UFUQ and is unnecessary for the current manifest.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Semantics is not canonical or required | Abstract/Status, PDF pp. 1-2; §1.1, p. 3 | Do not require formal PROV reasoning | `PROJECT_DECISION_REQUIRED` |
| Entity/activity/agent separation | §§3.2.1-3.2.3, PDF pp. 5-7 | Use only as optional provenance terminology | `INFORMATIONAL_ONLY` |
| Generation/use event vocabulary | §3.2.4.1, PDF p. 7 | Describe input consumption/output creation precisely if helpful | `INFORMATIONAL_ONLY` |
| Derivation must be explicit | §3.2.4.6, PDF p. 8 | Record actual input/activity/output links; do not infer from names | `SOURCE_REQUIRED` |
| Formal interpretation/satisfaction | §§3.5-4.1, PDF p. 9 | No executable UFUQ requirement | `INFORMATIONAL_ONLY` |
| Formal validity depends on PROV-CONSTRAINTS | §§1.1-1.3, PDF p. 3 | Do not claim PROV conformance from the UFUQ manifest | `PROJECT_DECISION_REQUIRED` |
