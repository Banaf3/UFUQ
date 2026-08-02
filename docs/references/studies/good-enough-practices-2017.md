# Bibliographic identity

- Canonical source ID: `WILSON-ET-AL-2017`.
- Title: *Good Enough Practices in Scientific Computing*.
- Authors: Greg Wilson, Jennifer Bryan, Karen Cranston, Justin Kitzes, Lex
  Nederbragt, and Tracy K. Teal.
- Edition/version: *PLOS Computational Biology* 13(6), e1005510.
- Year/publisher: 2017; Public Library of Science.
- DOI: `10.1371/journal.pcbi.1005510`.
- Local file:
  `local-reference/software-engineering/scientific-computing/good-enough-practices-2017.pdf`.
- Page count: 20 PDF/article pages.
- Text layer: reliable searchable text.
- Verification status: title, authors, date, DOI, copyright, and extent agree
  with the
  [publisher article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510).
  Acquisition provenance of the local copy remains unverified.

# UFUQ relevance

- Phases affected: Phase 0 project/repository hygiene and Phase 1 data and
  scientific-reference workflows.
- Project decisions affected: `UFUQ-DATA`, `UFUQ-ARCH`, `UFUQ-TEST`, and
  `UFUQ-ADR-004`.
- Sections studied: Overview p. 2; Box 1 pp. 3-4; Data management pp. 2-6;
  Software pp. 6-8; Collaboration pp. 8-9; Project organization pp. 9-11;
  Version control pp. 14-15; advanced practices including build tools, unit
  tests, coverage, and continuous integration p. 18; Conclusion p. 19.
- Sections intentionally not studied: manuscript workflow pp. 15-17 and
  bibliography/author details. They are not needed for current skill rules.
- Scope reason: identify low-overhead reproducibility practices appropriate to
  one developer while retaining stricter existing UFUQ gates where already
  activated.
- Classification: `SUPPORTING_NOW`.

# Terminology

- **Good enough practices**: an intentionally accessible minimum set selected
  for likely sustained adoption by individuals/small collaborations
  (Overview, p. 2).
- **Raw data**: the data in the form originally generated or acquired; when a
  local copy is impractical, the exact acquisition procedure/version/date
  should be recorded (Data management, p. 2).
- **Intermediate product**: a saved output between raw input and final
  analysis that makes a pipeline step easier to rerun and inspect
  (Data management, p. 6).
- **Modular code**: short, single-purpose functions with explicit inputs and
  outputs, supporting readability, reuse, and testability (Software, p. 6).
- **Build-and-smoke test**: a simple example/test dataset with known expected
  output used to check setup and basic operation (Software, p. 8).
- **Version control**: automated snapshot/change history for project files
  (Version control and Box 4, p. 14).
- **Continuous integration**: automatic execution of user-defined commands
  after repository changes, commonly to detect regressions (advanced
  practices, p. 18).

# Concepts and models

## Preserve raw input or preserve exact acquisition

The data-management section recommends retaining raw data unchanged and
making accidental edits difficult. When local retention is impractical, it
calls for the exact acquisition procedure, official version, and retrieval
date (p. 2). This directly supports UFUQ's ignored immutable raw bytes plus a
tracked acquisition manifest; it does not authorize redistribution.

## Record each transformation

The article recommends recording all processing steps and using persistent
keys consistently across tables (Box 1, pp. 3-4; Data management pp. 5-6).
It favors explicit intermediate products where they improve reruns,
inspection, sharing, or modification (p. 6). UFUQ may omit bulky intermediate
files when deterministic regeneration and hashes provide stronger evidence.

## Make dependencies and tests visible

Software guidance emphasizes explicit dependencies, modular functions, and a
small known test dataset (pp. 6-8). A README/CONTRIBUTING-style overview
should name setup and tests (Collaboration, p. 8). These support exact Phase 0
commands and the future pinned Python oracle environment.

## Organization is adaptable

The article offers a project layout, then explicitly values consistency and
predictability over fine-grained placement debates (pp. 9-11). Its example is
not authority to replace UFUQ's approved eight-workspace layout.

## What belongs in version control

The article favors version control for source/text and cautions that raw data
should not change, reproducible intermediates need not be tracked, large files
fit poorly, restricted data must not be shared publicly, and secrets must not
be committed (pp. 14-15). This aligns with UFUQ's ignored PDFs/raw bytes,
tracked manifests/scripts, and generated-output policy.

## CI is scale-sensitive, not forbidden

The advanced-practices section describes CI as valuable for regression
checking but less immediately beneficial to the paper's novice/small-project
audience (p. 18). UFUQ already has an active Phase 0 CI/test contract, so the
project decision controls; the paper supports keeping added process
proportionate rather than weakening an active gate.

# Equations and algorithms

No scientific equation is defined.

## Reproducible data pipeline

- Source location: Data management, pp. 2-6; Box 1, pp. 3-4.
- Inputs: immutable raw data or an exact acquisition procedure, metadata,
  software, and recorded processing steps.
- Output: analysis-friendly data and explicit intermediate/final products.
- Assumptions: stable identifiers and transformations are documented.
- Units/numerical concerns: domain-specific and not supplied by the paper.
- UFUQ use: source manifest → ignored raw bytes → normalization → generated
  artifact.
- Required validation: checksums, record counts, step-level failures, and
  deterministic rebuild evidence under the approved UFUQ policy.

# Conventions

- Treat raw bytes as immutable; never hand-edit them.
- If raw bytes cannot be kept/distributed, record exact acquisition details.
- Use stable identifiers consistently across joined records.
- Make dependencies, setup, and commands explicit.
- Keep source, data, generated results, and documentation distinguishable,
  adapting layout to the existing project.
- Never commit restricted data or credentials (pp. 14-15).

# Implementation implications

- `SOURCE_REQUIRED` — Preserve approved raw bytes immutably or record an exact
  reproducible acquisition procedure with version/date metadata (Data
  management, p. 2).
- `SOURCE_REQUIRED` — Record every transformation and use persistent,
  consistently encoded identifiers for joins (Box 1 pp. 3-4; pp. 5-6).
- `SOURCE_REQUIRED` — Pin dependencies and provide an executable
  production-shaped example/reference dataset with known expected behavior
  (Software, pp. 7-8).
- `PROJECT_DECISION_REQUIRED` — Keep the current UFUQ repository/workspace
  layout; the paper's directory example is adaptable guidance, not a redesign
  mandate (Project organization, pp. 9-11).
- `SOURCE_REQUIRED` — Keep large/restricted raw files, reproducible
  intermediates, and credentials out of public version control; retain
  manifests, code, and permissible checksums instead (pp. 14-15).
- `PROJECT_DECISION_REQUIRED` — Existing active Phase 0 CI/test commands
  remain mandatory and fail closed. The paper's scale caution does not
  authorize weakening a gate (advanced practices, p. 18; `UFUQ-TEST`).
- `INFORMATIONAL_ONLY` — Add new tools/processes only when their benefit
  exceeds adoption/maintenance cost for the current phase (Overview p. 2;
  advanced practices pp. 18-19).

# Testing implications

- Verify raw inputs are read-only/unchanged by comparing approved hashes before
  transformation.
- Test the documented one-command setup/smoke path on a clean environment.
- Validate every join key for uniqueness, stable representation, and
  referential integrity.
- Test each transformation separately and verify intermediate/final row counts
  or hashes.
- Ensure CI runs the active commands on change and reports/rejects regressions
  according to the existing repository policy.
- Scan tracked/staged files for raw data, local references, generated outputs
  not approved for tracking, and credentials.
- Do not copy the article's sample folder layout or thresholds into tests.

# Limitations

- The recommendations target individuals and small collaborations and are
  deliberately minimal; they are not a complete software-engineering
  standard.
- The paper does not define scientific correctness, independent oracles,
  tolerance selection, canonical serialization, licensing conclusions, or
  catalogue semantics.
- It does not justify removing an active test/CI gate.
- Its example directory layout is illustrative, not universal.
- Saving intermediate data is a trade-off; UFUQ's deterministic/hash policy
  may provide equivalent or stronger evidence without tracking outputs.

# Conflicts and ambiguities

- The paper recommends saving raw data, while UFUQ forbids tracking restricted
  raw catalogue bytes. The compatible interpretation is immutable ignored
  local/private storage plus a tracked manifest/checksum where permitted.
- It describes unit tests, coverage, and CI as later practices for its novice
  audience (p. 18), whereas UFUQ Phase 0 already activates tests and CI
  commands. Project maturity and risk, not the article's minimum, control.
- It suggests saved intermediate products, while UFUQ favors deterministic
  regeneration. The decision depends on data size, cost, licence, and replay
  evidence and must be recorded.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Preserve raw data or exact acquisition details | Data management, p. 2 | Immutable ignored raw bytes plus approved manifest | `SOURCE_REQUIRED` |
| Record processing steps and stable keys | Box 1 pp. 3-4; Data management pp. 5-6 | Trace transforms and joins deterministically | `SOURCE_REQUIRED` |
| Explicit dependencies and known sample | Software, pp. 7-8 | Pin environment and provide a smoke/reference fixture | `SOURCE_REQUIRED` |
| Layout should be consistent and project-appropriate | Project organization, pp. 9-11 | Do not redesign the eight workspaces from an example | `PROJECT_DECISION_REQUIRED` |
| Avoid tracking large/restricted data and secrets | Version control, pp. 14-15 | Preserve ignore/staging gates | `SOURCE_REQUIRED` |
| CI automatically checks regressions but has cost | Advanced practices, p. 18 | Keep active gates; add only proportional new process | `PROJECT_DECISION_REQUIRED` |
| Pragmatic incremental adoption | Overview p. 2; Conclusion p. 19 | Scale controls to phase risk and one developer | `INFORMATIONAL_ONLY` |
