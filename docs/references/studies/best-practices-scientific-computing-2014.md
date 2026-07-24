# Bibliographic identity

- Canonical source ID: `WILSON-ET-AL-2014`.
- Title: *Best Practices for Scientific Computing*.
- Authors: Greg Wilson et al.
- Edition/version: Community Page, *PLOS Biology* 12(1), e1001745.
- Year/publisher: 2014; Public Library of Science.
- DOI: `10.1371/journal.pbio.1001745`.
- Local file:
  `local-reference/software-engineering/scientific-computing/best-practices-scientific-computing-2014.pdf`.
- Page count: 7 PDF/article pages.
- Text layer: reliable searchable text.
- Verification status: title, authors, date, DOI, publication statement, and
  extent agree with the
  [publisher article](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745).
  Acquisition provenance of the local copy remains unverified.

# UFUQ relevance

- Phases affected: Phase 0 engineering gates and Phase 1 scientific/data
  tooling; later phases inherit the reproducibility and testing discipline.
- Project decisions affected: `UFUQ-ARCH`, `UFUQ-TEST`,
  `UFUQ-ADR-007`, and the reproducible catalogue workflow in `UFUQ-DATA`.
- Sections studied: Introduction p. 1; Box 1 and "Write Programs..." /
  "Let the Computer Do the Work" p. 2; provenance, incremental change,
  version control, and "Plan for Mistakes" pp. 3-4; testing/oracles,
  documentation, collaboration, and Conclusion pp. 4-6.
- Sections intentionally not studied: bibliography details and author
  information pp. 6-7. They do not add project rules.
- Scope reason: extract proportional workflow controls for a scientific FYP,
  not a blanket mandate to adopt every practice or publish restricted data.
- Classification: `SUPPORTING_NOW`.

# Terminology

- **Build tool / automated workflow**: a machine-executable description of
  dependencies and commands that regenerates affected outputs ("Let the
  Computer Do the Work", p. 2).
- **Provenance**: automatically recorded identifiers/versions for data,
  software, parameters, and outputs sufficient to reconstruct how a result was
  produced (pp. 2-3).
- **Version control system**: a repository of file snapshots and change
  metadata supporting comparison, recovery, and conflict management
  ("Make Incremental Changes", p. 3).
- **Assertion**: an executable check on an invariant, input, output, or state
  ("Plan for Mistakes", pp. 3-4).
- **Unit / integration / regression tests**: checks of an isolated unit,
  combined components, and unchanged behavior after modification
  ("Plan for Mistakes", p. 4).
- **Test oracle**: a known/reference output against which program output is
  compared; the paper lists simple cases, experimental data, trusted earlier
  programs, and a simpler high-level implementation as examples (p. 4).
- **Pre-merge review**: review required before accepting a change
  ("Collaborate", p. 5).

# Concepts and models

## Software as scientific apparatus

The Introduction treats software as experimental apparatus that needs
careful construction, checking, and use (p. 1). This supports UFUQ's
separation between type/build correctness and independent scientific
validation.

## Automate repeated work

Box 1 practice 2 and the accompanying section recommend saving commands and
using a build tool so repeated processing is machine-executed rather than
manually retyped (p. 2). Reproducibility improves when a command records its
data/software versions, parameters, and outputs (pp. 2-3).

## Work incrementally under version control

Box 1 practice 3 recommends small steps with feedback, version control, and
tracking manually created sources (p. 2). The conclusion recommends
introducing practices incrementally rather than all at once (p. 5). Generated
outputs should be regenerated from tracked sources where practical; UFUQ's
licence and restricted-material policy remains controlling.

## One authoritative representation and modularity

Box 1 practice 4 asks for one authoritative representation of each datum and
modular reuse instead of copy/paste (p. 2). This supports catalogue
coordinates originating only from approved numerical source data and cultural
records linking by stable IDs rather than copying coordinates.

## Plan for mistakes with layered tests

Assertions, an established unit-test library, and converting discovered bugs
to regression tests form complementary defenses (Box 1 and "Plan for
Mistakes", pp. 2, 3-4). The paper recognizes unit, integration, and regression
roles and notes that testable isolated functions are also easier to understand
and reuse (p. 4).

## Reference implementations as oracles

The paper suggests a simple/high-level predecessor can check an optimized
implementation (p. 4). This is useful only if its construction and failure
modes are sufficiently independent. Kanewala and Bieman's review adds the
warning that even independently developed pseudo-oracles may agree on the
same fault; UFUQ therefore also needs authoritative source fixtures and
cross-checks.

# Equations and algorithms

No domain equation or numerical algorithm is defined.

## Reproducible workflow

- Source location: Box 1 practices 2-3, p. 2; provenance discussion pp. 2-3.
- Inputs: source data identifiers/versions, program/library versions,
  parameters, and commands.
- Output: regenerated result plus traceable provenance.
- Assumptions: inputs and dependencies are accessible and versions are
  recorded.
- Units: project/domain-specific.
- Numerical concerns: the paper does not define tolerance or floating-point
  policy.
- UFUQ use: exact Phase 0/1 commands and deterministic catalogue/reference
  generation.
- Required validation: rerun from the recorded inputs/environment and compare
  results or canonical hashes.

# Conventions

- Keep each scientific value in one authoritative representation and derive
  projections mechanically.
- Save exact commands rather than relying on interactive memory.
- Pin data, program, library, and parameter identity when it affects output.
- Make small reviewable changes and preserve history.
- Turn every fixed defect into a regression test.
- Document interfaces and reasons rather than narrating mechanics
  (Box 1 practice 7; pp. 4-5).

# Implementation implications

- `SOURCE_REQUIRED` — Scientific and data commands must be reproducible from
  recorded inputs, versions, parameters, and a machine-executable command
  (Box 1 practice 2; pp. 2-3).
- `SOURCE_REQUIRED` — Maintain one authoritative source for numerical
  catalogue values and derive all runtime projections; do not copy/paste
  coordinates (Box 1 practice 4, p. 2).
- `SOURCE_REQUIRED` — Use assertions plus unit, integration, and regression
  tests as complementary checks; convert defects to tests (Box 1 practice 5;
  pp. 3-4).
- `PROJECT_DECISION_REQUIRED` — Active UFUQ suites fail closed and phase-empty
  scientific suites must not pass via placeholders (`UFUQ-TEST`); the paper
  does not define suite activation.
- `SOURCE_REQUIRED` — Keep scientific computation in small, independently
  testable units and avoid duplicated implementations inside production code
  (pp. 2, 4).
- `EXPERIMENT_REQUIRED` — An independent/simpler oracle must be compared on
  representative, boundary, and failure cases; agreement alone is not
  proof of correctness (p. 4 plus `KANEWALA-BIEMAN-2014` §§3.3-4.1).
- `PROJECT_DECISION_REQUIRED` — Raw/private data tracking and publication
  follow UFUQ licence and ignore policies; general version-control advice does
  not authorize committing restricted bytes.
- `INFORMATIONAL_ONLY` — Introduce additional process controls incrementally
  and proportionately for one FYP developer (Conclusion, p. 5).

# Testing implications

- Run exact recorded commands from a clean/pinned dependency state.
- Assert invariants at parsing/normalization and scientific function
  boundaries.
- Cover units, component integration, and regressions; a defect fix requires
  a test that previously failed.
- Compare scientific results to simplified/analytic cases and an independently
  constructed reference where available.
- Do not treat two copies of one algorithm or shared production helpers as
  independent.
- Rebuild generated artifacts twice from identical inputs and compare
  canonical bytes/hashes.
- Include readable diagnostics and document the interface/reason for each
  reference fixture.

# Limitations

- The article is an experience/research-grounded recommendation set, not a
  formal standard.
- Its practices reduce risk but do not guarantee error-free or reproducible
  results (Introduction, p. 1).
- It does not define UFUQ's architecture, astronomy algorithms, catalogue
  policy, tolerance, validator, CI platform, or licence decision.
- Its general advice to version manually created material does not override
  restricted-data, privacy, or copyright rules.
- A trusted earlier program can still be wrong; the article does not quantify
  oracle independence.

# Conflicts and ambiguities

- The article recommends tracking manually created sources, while UFUQ keeps
  local PDFs and raw catalogue bytes ignored. The purpose—recoverable,
  attributable inputs—is retained through manifests, checksums, approved
  private storage, and citations without committing restricted material.
- The article permits a simple predecessor as an oracle; the scientific
  testing review shows pseudo-oracles can share faults. UFUQ requires both
  independence and multiple evidence layers.
- The paper's recommendations cover teams of varied size. UFUQ adopts only
  controls tied to current phase risks and existing gates.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Automate repeatable workflows | Box 1 practice 2 and discussion, p. 2 | Record one-command regeneration and dependencies | `SOURCE_REQUIRED` |
| Record data/software/parameter provenance | Provenance discussion, pp. 2-3 | Put versions, hashes, and parameters in evidence | `SOURCE_REQUIRED` |
| Small changes and version history | Box 1 practice 3, p. 2; discussion p. 3 | Keep changes reviewable and recoverable | `SOURCE_REQUIRED` |
| Single authoritative representation | Box 1 practice 4, p. 2 | No manually duplicated catalogue coordinates | `SOURCE_REQUIRED` |
| Assertions and layered tests | Box 1 practice 5; pp. 3-4 | Add invariants, unit/integration/regression checks | `SOURCE_REQUIRED` |
| High-level implementation as oracle | "Optimize..." and testing discussion, p. 4 | Build a separately sourced reference and test its limitations | `EXPERIMENT_REQUIRED` |
| Introduce practices incrementally | Conclusion, p. 5 | Keep controls proportionate to phase and developer capacity | `INFORMATIONAL_ONLY` |
