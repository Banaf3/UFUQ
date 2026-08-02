# Bibliographic identity

- Canonical source IDs: `KANEWALA-BIEMAN-2014` for the peer-reviewed study
  and `KANEWALA-BIEMAN-2018-PREPRINT` for the local file.
- Title: *Testing Scientific Software: A Systematic Literature Review*.
- Authors: Upulee Kanewala and James M. Bieman.
- Edition/version: local arXiv v1 preprint `1804.01954`, dated 5 April 2018,
  corresponding to the 2014 peer-reviewed article.
- Year/publisher: peer-reviewed article published 2014 in *Information and
  Software Technology* 56(10), pp. 1219-1232, Elsevier; local preprint
  produced 2018.
- Identifiers: DOI `10.1016/j.infsof.2014.05.006`; arXiv `1804.01954`.
- Local file:
  `local-reference/software-engineering/scientific-testing/kanewala-bieman-2018-testing-scientific-software-preprint.pdf`.
- Page count: 30 local preprint pages; the published article's journal
  pagination is 1219-1232.
- Text layer: reliable searchable text.
- Verification status: title, authors, arXiv banner/date, and content extent
  agree with the [arXiv record](https://arxiv.org/abs/1804.01954). Cite
  local locations as preprint pages and the peer-reviewed study by DOI.
  Acquisition provenance of the local copy remains unverified.

# UFUQ relevance

- Phases affected: Phase 1 astronomy/data technical spike and every later
  scientific calculation or numerical regression suite.
- Project decisions affected: `UFUQ-TEST`, `UFUQ-ADR-007`, and the independent
  Astropy reference-fixture requirement in `UFUQ-ASTRO-SPEC`.
- Sections studied:
  - Abstract and §1, preprint pp. 1-3;
  - §§2-2.3 and Tables 1-4, pp. 3-7;
  - §3.2, pp. 13-16;
  - §3.3, Figures 1-2 and oracle/testing techniques, pp. 16-20;
  - §§3.4-4.4, pp. 20-23;
  - §5 opening/conclusion identified on pp. 23-24.
- Sections intentionally not studied in detail: the full inventory of primary
  studies and quality scores (Tables 5-10, pp. 7-14), complete references,
  and author biography. These do not add current UFUQ rules.
- Scope reason: derive oracle, boundary-case, layered-test, and evidence
  limitations without treating a literature review as a source of validated
  astronomical tolerances.
- Classification: `SUPPORTING_NOW`.

# Terminology

- **Scientific software**: software used for scientific purposes, commonly to
  understand or predict real processes (§1, p. 2).
- **Verification**: checking that the computational model works as intended;
  distinct from validating whether the scientific model represents the
  physical phenomenon (§1, p. 2).
- **Oracle**: a mechanism for deciding whether output for a test case is
  expected/correct (§3.2, p. 13).
- **Oracle problem**: difficulty obtaining reliable expected results,
  especially when outputs are novel, complex, approximate, or uncertain
  (§3.2, pp. 13-15).
- **Pseudo-oracle**: an independently developed program implementing the same
  specification (§3.3, p. 18).
- **Reference dataset**: a set of cases/expected results derived from a
  functional specification for black-box tests (§3.3, p. 19).
- **Metamorphic relation**: a specified relation between a controlled input
  change and the corresponding expected output change (§3.3, p. 19).
- **Regression test**: comparison of current and previous behavior after code
  modification (§3.3, p. 18).

# Concepts and models

## Scientific results can be plausibly wrong

The Introduction reports that small code faults can change output without a
crash and that scientific programs can produce plausible but materially
different results (§1, pp. 1-2). Passing type checks, rendering plausibly, or
avoiding exceptions is therefore not scientific evidence.

## Two categories of testing challenge

The review groups challenges into software/model characteristics and
development culture (§3.2; §4.1, pp. 13-16, 21). Technical challenges include
large input spaces, floating-point path dependence, unavailable physical
contexts, round-off/truncation, and missing oracles. Process challenges
include unwritten quality goals, ad hoc/late testing, and low use of
unit/automated regression tests.

## Oracle evidence is plural and limited

Section 3.3 identifies pseudo-oracles, analytic solutions, experiments,
measurements, professional judgment, simple cases, statistical oracles,
reference datasets, and metamorphic testing (pp. 18-19). Each has limits:
independent programs can share failures; analytic/experimental values may be
unavailable or wrong; simple cases miss numerical edge faults; expert judgment
can be subjective; reference datasets may not distinguish model error from
code error. UFUQ needs layered evidence rather than a single "golden" source.

## Multiple testing levels are underused

The review distinguishes unit, integration, system, acceptance, and
regression testing. Among its 62 primary studies, only 12 reported at least
one of these methods, most of those reported only one, and none reported four
or more (§3.3, pp. 16-18; §4.1, p. 21). The result is descriptive evidence of
weak practice, not a percentage target for UFUQ.

## Tolerance selection is empirical

Section 3.3 reports that tightening an oracle tolerance increased fault
detection in one experiment and that breaking algorithms into smaller tested
steps reduced compounding numerical effects (p. 19). It does not provide a
universal tolerance. UFUQ must measure errors against pinned independent
fixtures over the supported domain.

## Systematic-review boundary

The review followed a planned search and selection protocol, used quality and
data-extraction tables, and retained 62 primary studies (§2, pp. 3-7). Its
search was conducted in January 2013 and its authors acknowledge search,
selection, and evidence-uptake limitations (§4.3, pp. 22-23). Conclusions
describe the reviewed evidence up to that cutoff, not current exhaustive
tooling guidance.

# Equations and algorithms

## Pseudo-oracle comparison

- Source location: §3.3, preprint p. 18.
- Inputs: identical specification and test cases supplied to production and
  independently developed reference programs.
- Output: agreement/difference in results.
- Units: domain-specific.
- Assumptions: implementations are genuinely independent and the
  specification is correct.
- Valid domain: only the cases, policies, and numerical range exercised.
- Numerical concerns: both implementations can share a failure; disagreements
  do not identify which is wrong.
- UFUQ use: production TypeScript versus pinned Python/Astropy fixtures, with
  no import from a UFUQ production package.
- Required validation: add authoritative/simple cases, provenance, boundary
  cases, and investigation of every disagreement.

## Metamorphic testing

- Source location: §3.3, preprint p. 19.
- Inputs: a source test input and a controlled transformation.
- Output: result pair checked against a domain-justified relation.
- Assumptions: the relation is independently valid for the modeled domain.
- Valid domain: explicitly stated by each relation.
- Numerical concerns: the relation may require a measured comparison policy;
  manually selected relations can miss faults.
- UFUQ use: invariants such as normalization/range relations only after their
  scientific basis is cited.
- Required validation: source-located rationale, adverse cases, and an
  independent oracle where available.

## Tolerance experiment

- Source location: §3.3, preprint p. 19.
- Variables: candidate comparison threshold and faults detected over selected
  cases.
- Units: the comparison quantity's units; never implicit.
- Assumptions: fixtures span supported frames/times/observer/date policies and
  relevant numerical boundaries.
- Numerical concerns: a smaller threshold may detect more faults but can also
  reject legitimate model/data differences; the review supplies no UFUQ
  optimum.
- UFUQ use: measure error distributions during the technical spike.
- Required validation: report max/percentile/residual behavior by case class
  and approve the threshold as a project decision.

# Conventions

- Separate scientific-model validation, computational verification, and code
  testing (§1, p. 2).
- Record oracle source, version, policy, data, units, and limitations.
- Use "independent" only when the oracle does not import or call production
  UFUQ scientific code.
- Treat simple cases as one layer, not full numerical validation.
- State tolerances with units and evidence; never infer them from display
  precision or a source's generic claim.
- Distinguish unit, integration, system, acceptance, and regression evidence.

# Implementation implications

- `SOURCE_REQUIRED` — Scientific correctness claims require an oracle or
  property beyond no-crash/type/visual plausibility (§§1, 3.2, pp. 1-2,
  13-15).
- `PROJECT_DECISION_REQUIRED` — The independent Python/Astropy tool must not
  import a production UFUQ package (`UFUQ-ADR-007`); the review's
  pseudo-oracle model supports but does not itself name this boundary.
- `SOURCE_REQUIRED` — Combine unit, integration/system, and regression
  evidence rather than depending on one layer (§3.3, pp. 16-18; §4.1, p. 21).
- `EXPERIMENT_REQUIRED` — Determine numerical tolerance from pinned fixture
  results over explicit policy/date/boundary partitions; no tolerance is
  supplied by the review (§3.3, p. 19).
- `SOURCE_REQUIRED` — Include critical input boundaries, floating-point
  paths, degenerate cases, and production-shaped cases (§3.2, pp. 13-16).
- `SOURCE_REQUIRED` — Treat analytic/simple/reference/metamorphic evidence as
  complementary and record each limitation (§3.3, pp. 18-19).
- `PROJECT_DECISION_REQUIRED` — Active scientific suites fail closed once
  Phase 1 activates them; suite activation is governed by `UFUQ-TEST`, not the
  review.
- `INFORMATIONAL_ONLY` — Metamorphic testing is a candidate technique, not a
  requirement; each relation needs source support and must address the actual
  oracle gap.

# Testing implications

- Add separate unit, pipeline/integration, system/reference, and regression
  tests when the Phase 1 spike activates scientific behavior.
- Generate independent fixtures with a pinned environment, input policies,
  datasets, units, and expected output.
- Test analytical/simple cases, but also boundary, degenerate, random or
  stratified production-shaped, and floating-point-sensitive cases.
- Test each decomposed numerical stage where compounding round-off could hide
  a fault.
- Report actual residuals before proposing a tolerance; retain cases on both
  sides of the eventual boundary.
- Investigate oracle/production disagreement rather than automatically
  declaring either side correct.
- Convert every confirmed scientific defect to a permanent regression fixture
  with provenance.
- Stop a scientific claim when reference provenance, units, policies, data
  versions, or supported-domain coverage is missing.

# Limitations

- The local file is a 2018 preprint, not the 2014 publisher PDF.
- The systematic search was conducted in January 2013 (§2.1.2, p. 4).
- The review found limited empirical evaluation for many oracle techniques
  and little evidence of some techniques' practical use (§4.1, p. 21).
- Primary studies covered heterogeneous scientific domains; findings do not
  set UFUQ's astronomical tolerance or test count.
- The review cannot verify Astropy, SOFA, IERS data, catalogue metadata, or
  any UFUQ result.
- Professional judgment, pseudo-oracles, reference datasets, and simple cases
  all have documented failure modes.

# Conflicts and ambiguities

- Wilson et al. (2014) suggests a simpler/high-level predecessor as an oracle;
  this review warns independent programs can share faults (§3.3, p. 18).
  UFUQ therefore requires multiple evidence layers and source provenance.
- Regression tests compare against prior output, which can preserve an old
  error. Reference fixtures must be separately sourced and versioned.
- Metamorphic testing reduces reliance on exact outputs, but a wrong or
  incomplete relation becomes another oracle fault. No relation is adopted
  without domain evidence.
- The study reports tolerance sensitivity but no generally valid threshold;
  any numeric value remains `EXPERIMENT_REQUIRED`.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Plausible output can conceal code faults | §1, preprint pp. 1-2 | Type/no-crash/visual checks cannot establish science | `SOURCE_REQUIRED` |
| Oracle and input-space challenges | §3.2, pp. 13-16 | Cover boundaries, floating-point paths, and oracle provenance | `SOURCE_REQUIRED` |
| Multiple testing levels | §3.3, pp. 16-18; §4.1, p. 21 | Maintain layered scientific suites | `SOURCE_REQUIRED` |
| Pseudo-oracle and shared-failure risk | §3.3, p. 18 | Keep reference implementation independent and triangulate | `SOURCE_REQUIRED` |
| Simple/reference/metamorphic oracle limits | §3.3, pp. 18-19 | Record limitations and use complementary evidence | `SOURCE_REQUIRED` |
| Tolerance affects detection but is not universal | §3.3, p. 19 | Measure and approve UFUQ tolerance experimentally | `EXPERIMENT_REQUIRED` |
| Search and evidence limitations | §2.1.2, p. 4; §4.3, pp. 22-23 | Do not treat the review as exhaustive current tooling guidance | `INFORMATIONAL_ONLY` |
