# Bibliographic identity

- Canonical source ID: `BASS-ET-AL-2022`.
- Title: *Software Architecture in Practice*.
- Authors: Len Bass, Paul Clements, and Rick Kazman.
- Edition/version: fourth edition.
- Year/publisher: released 2021 with 2022 copyright; Addison-Wesley
  Professional / Pearson.
- ISBN: `978-0-13-688609-9`.
- Local file:
  `local-reference/software-engineering/architecture/software-architecture-in-practice-4e.pdf`.
- Page count: 460 PDF pages; Pearson lists 464 physical pages. The local
  contents-to-index sequence is continuous, so the format difference is not
  treated as truncation.
- Text layer: reliable searchable text.
- Verification status: title, authors, edition, publication page, contents,
  ISBN, and extent agree with the
  [publisher record](https://www.pearson.com/en-ca/subject-catalog/p/software-architecture-in-practice/P200000000111/9780136886099).
  Acquisition provenance remains unverified.

# UFUQ relevance

- Phases affected: Phase 0 architecture/boundary review and later reviews only
  when a concrete quality attribute, dependency risk, or architecture debt is
  demonstrated.
- Project decisions affected: `UFUQ-ARCH`, `UFUQ-IMPL-DEC`,
  `UFUQ-PHASES`, `UFUQ-TEST`, and `UFUQ-ADR-007`.
- Sections studied:
  - contents and preface, front matter;
  - §1.3 and summary, printed pp. 19-21;
  - §§3.2-3.5, printed pp. 41-49;
  - §§12.1-12.2 (through limiting structural complexity), printed
    pp. 186-190;
  - §§21.1-21.2, printed pp. 309-311;
  - §§21.6-21.7, printed pp. 324-327;
  - §22.7, printed pp. 346-347.
- Relevant chapters identified but intentionally not deeply studied:
  Chapters 4-11 and 13-14 (individual quality-attribute tactics), Chapter 20
  (full Attribute-Driven Design), the full ATAM procedure in §21.5, and most
  documentation views in Chapter 22. UFUQ has no demonstrated problem that
  warrants selecting a new tactic, process, or view set.
- Chapters not relevant to the current UFUQ review: virtualization, cloud,
  mobile, organizational competence, and quantum-computing chapters.
- Scope reason: use the book as a proportional review guardrail, not a source
  of architecture requirements or a redesign brief.
- Classification: studied sections are `SUPPORTING_NOW`; unselected tactics
  are `REQUIRED_LATER` only if a measured quality-attribute problem emerges.

# Terminology

- **Software architecture**: the structures needed to reason about a system,
  comprising software elements, their relations, and relevant properties
  (§1.4, p. 21).
- **Module structure**: the code/data-unit view of constructed or procured
  elements (§1.4, p. 21).
- **Component-and-connector structure**: runtime elements and their
  interactions (§1.4, p. 21).
- **Quality attribute scenario**: a testable requirement stated as stimulus
  source, stimulus, environment, artifact, response, and response measure
  (§3.3, pp. 42-44).
- **Tactic**: a design decision aimed at controlling a quality-attribute
  response (§3.5, pp. 46-48).
- **Testability**: the degree to which testing can control a system and
  observe whether faults are exposed, with effort/time/effectiveness measures
  (§§12.1-12.2, pp. 186-188).
- **Architecture evaluation**: determining how fit an architecture is for its
  intended purpose (§21 introduction, p. 309).
- **Risk**: an event with probability and impact; estimated exposure combines
  the two (§21.1, pp. 309-310).
- **Lightweight Architecture Evaluation (LAE)**: a regular, project-internal
  peer review focused on prioritized scenarios and recent/unexamined
  architectural areas (§21.6, pp. 324-326).
- **Design rationale**: recorded reasons, alternatives, evidence,
  assumptions, trade-offs, and risks behind important design decisions
  (§22.7, pp. 346-347).

# Concepts and models

## Fitness is purpose-dependent

Section 1.3 states that an architecture is not inherently good or bad; it is
more or less fit for stated goals. Evaluation without project-specific goals
is therefore not meaningful (p. 19). For UFUQ, a book pattern or additional
layer is never sufficient evidence for redesign.

## Quality attributes must be testable

General labels such as "modifiable" are not testable without naming the
change, affected artifact, environment, expected response, and measure
(§§3.2-3.3, pp. 41-44). Quality attributes also interact, so improving one
can impose a cost on another (§3.2, p. 42). UFUQ reviews should state an
observable scenario and trade-off before recommending a boundary change.

## Modular boundaries

The book's structural guidance calls for modules with well-defined
responsibilities, information hiding, separation of concerns, and explicit
interfaces around likely changes (§1.3, p. 20). It also distinguishes modules
that produce data from modules that consume it and recommends incremental
implementation (§1.3, pp. 19-20). These ideas support review of UFUQ's pure
domain, adapter, application, and catalogue-tool boundaries; the existing
eight-workspace design remains the project authority.

## Testability through control, observation, and limited complexity

The general scenario requires control of test inputs/state and observation of
results (§12.1, pp. 186-187). Tactics include abstracting data sources,
sandboxing/virtualizing external resources, executable assertions, and
reducing cyclic or environmental coupling (§12.2, pp. 188-190). They support
UFUQ's pure scientific functions and replaceable independent fixtures, but
they do not prescribe a framework.

## Evaluation is risk reduction

Evaluation should cost less than the value it provides and be proportionate
to risk (§21 introduction and §21.1, pp. 309-310). Reviewers establish
architectural drivers, trace prioritized scenarios through the design, look
for interference among scenarios, and record risks for explicit acceptance or
remediation (§21.2, pp. 310-311). LAE offers a lower-ceremony form suited to
regular internal peer review (§21.6, pp. 324-326).

## Rationale is evidence, not a diagram

Section 22.7 requires recording why an important design was selected,
discarded alternatives, evidence, assumptions, shortcuts, trade-offs, and
risks (pp. 346-347). A folder tree or dependency diagram alone does not
justify an architecture change.

# Equations and algorithms

## Quality attribute scenario

- Source location: §3.3, printed pp. 42-44.
- Form: stimulus source + stimulus + environment + affected artifact +
  response + measurable response.
- Units: determined by the quality attribute, such as elapsed time, effort,
  fault-detection probability, or count.
- Assumptions: the scenario is concrete enough to test.
- Valid domain: a specific system/project and stakeholder concern.
- UFUQ use: evidence template for any significant boundary, workspace, or
  test-gate proposal.
- Required validation: reproduce the stimulus in the stated environment and
  measure the response before accepting the claim.

## Risk exposure

- Source location: §21.1, pp. 309-310; testability measures also show
  `size(loss) × probability(loss)` in §12.1, p. 187.
- Variables: estimated consequence and estimated probability.
- Units: project-specific cost/risk units.
- Assumptions: estimates are explicit and comparable.
- Numerical concerns: estimates can be uncertain and must not be presented as
  measured facts.
- UFUQ use: choose review depth and compare cost of changing with cost of
  retaining the design.
- Required validation: record evidence and uncertainty; no numeric
  architecture threshold is adopted.

## Lightweight evaluation workflow

- Source location: §21.6, pp. 324-326.
- Operation: review goals and architecture, refresh/prioritize quality
  scenarios, trace high-priority/recent changes, and capture risks,
  sensitivities, and trade-offs.
- UFUQ use: focused review when a concrete architecture risk appears.
- Required validation: exact files, dependency paths, commands, outcomes, and
  unresolved risks.

# Conventions

- State architecture claims as quality-attribute scenarios, not broad
  adjectives.
- Distinguish module, runtime component/connector, and deployment/allocation
  views; do not infer one directly from another.
- Record both benefits and trade-offs of a tactic.
- Scale evaluation effort to demonstrated risk and project size.
- Treat current UFUQ ADRs and observed repository behavior as project
  authority; the book supplies review concepts, not replacement decisions.

# Implementation implications

- `SOURCE_REQUIRED` — A major architecture proposal must identify a concrete,
  prioritized quality-attribute scenario and measurable response
  (§§3.2-3.3, pp. 41-44).
- `SOURCE_REQUIRED` — Review responsibilities, likely changes, interfaces,
  information hiding, and data producer/consumer separation when a module
  boundary is questioned (§1.3, pp. 19-20).
- `PROJECT_DECISION_REQUIRED` — Preserve the approved eight-workspace
  architecture unless observed dependency behavior or a measured
  quality-attribute problem justifies an ADR change (`UFUQ-ARCH`;
  §1.3, p. 19).
- `SOURCE_REQUIRED` — Important architecture decisions must record rationale,
  alternatives, evidence, assumptions, trade-offs, and risks (§22.7,
  pp. 346-347).
- `SOURCE_REQUIRED` — Testability-sensitive design should expose controllable
  inputs and observable results and should isolate external state
  (§§12.1-12.2, pp. 186-190).
- `PROJECT_DECISION_REQUIRED` — Active UFUQ suites must fail closed and pure
  domains remain isolated; these are tracked UFUQ decisions, supported but not
  created by the book.
- `INFORMATIONAL_ONLY` — Named patterns/tactics are candidate mechanisms only.
  Do not implement one until the specific scenario and trade-off evidence
  require it.
- `SOURCE_REQUIRED` — Use the smallest evaluation whose cost is proportionate
  to the demonstrated risk (§§21.1, 21.6, pp. 309-310, 324-326).

# Testing implications

- Translate each claimed quality attribute into a reproducible stimulus,
  environment, artifact, response, and measure.
- Test module boundaries with dependency/cycle/import checks that target the
  actual stated risk.
- Keep scientific functions controllable through explicit inputs and
  observable outputs; isolate clock, file, network, database, and tool state.
- Include assertions/invariants where they expose invalid state, but do not
  mistake assertions copied from production logic for independent scientific
  evidence.
- Verify that an active test gate fails when its target behavior is broken;
  a passing or empty suite alone is insufficient architecture evidence.
- Record alternatives and risks for both changing and retaining the current
  design.
- Stop style-only refactors that have no scenario, observed violation,
  measurable maintenance cost, or phase-gate need.

# Limitations

- The book is general architecture guidance, not a UFUQ domain standard.
- It cannot establish astronomical correctness, numerical tolerances,
  catalogue semantics, cultural validity, or Qibla coordinates.
- It does not know UFUQ's team size, phase gates, eight-workspace history, or
  current dependency graph; those must be inspected.
- Its patterns/tactics are not mandatory and do not prove their own
  suitability.
- A quality-attribute scenario describes required evidence but does not
  guarantee the chosen measure or threshold is correct.

# Conflicts and ambiguities

- Some structural recommendations are broad rules of thumb (§1.3), while
  UFUQ already has approved, narrower dependency rules. The project rules
  control unless a demonstrated problem justifies change.
- The book presents comprehensive evaluation methods, but a one-developer FYP
  generally needs targeted checks or an LAE-sized review. Review depth is a
  risk/cost decision, not a maturity signal.
- Assertions can embed an oracle (§12.2, p. 190), but scientific assertions
  may share the same mistake as production code. Independent reference
  evidence remains required by `UFUQ-ADR-007`.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Architecture fitness depends on stated goals | §1.3, p. 19 | No redesign from pattern preference alone | `PROJECT_DECISION_REQUIRED` |
| Incremental implementation and modular responsibility | §1.3, pp. 19-20 | Preserve explicit, change-isolating boundaries | `SOURCE_REQUIRED` |
| Six-part measurable quality scenario | §§3.2-3.3, pp. 41-44 | Require a testable scenario for major architecture claims | `SOURCE_REQUIRED` |
| Quality attributes trade off | §3.2, p. 42 | State costs/risks of both change and retention | `SOURCE_REQUIRED` |
| Control/observe and isolate dependencies | §§12.1-12.2, pp. 186-190 | Design tests around explicit inputs, outputs, and replaceable externals | `SOURCE_REQUIRED` |
| Evaluation as proportional risk reduction | §§21.1-21.2, pp. 309-311 | Match review effort to demonstrated risk | `SOURCE_REQUIRED` |
| Lightweight internal evaluation | §§21.6-21.7, pp. 324-327 | Prefer a focused review for bounded UFUQ risks | `SOURCE_REQUIRED` |
| Record evidence, assumptions, alternatives, and risks | §22.7, pp. 346-347 | Architecture changes need traceable rationale | `SOURCE_REQUIRED` |
