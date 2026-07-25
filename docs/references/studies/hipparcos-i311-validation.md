# Bibliographic identity

- Canonical source ID: `VAN-LEEUWEN-2007-VALIDATION`.
- Title: “Validation of the new Hipparcos reduction.”
- Author: Floor van Leeuwen.
- Edition/version: journal article and corresponding arXiv preprint `0708.1752`.
- Year: 2007.
- Publisher/journal: *Astronomy & Astrophysics* 474, 653-664.
- DOI/identifier: `10.1051/0004-6361:20078357`;
  bibcode `2007A&A...474..653V`.
- Local file:
  `local-reference/catalogues/hipparcos-i311/documentation/van-leeuwen-2007-validation.pdf`.
- Page count and accessibility: 12 PDF pages corresponding to journal pp. 653-664; a
  searchable text layer is present.
- Verification status: title, author, journal, volume/pages, year, DOI, section
  structure, equations, figures, and tables were checked against the local PDF metadata,
  the A&A record, and arXiv `0708.1752`.

# UFUQ relevance

- Phases affected: Phase 1 evaluation of the selected I/311 local-spike source; Phase 2
  uncertainty/error-budget design only if the remaining source-derived gates are met.
- Project decisions affected: AST-001 field/quality selection, AST-003
  space-motion/uncertainty treatment, AST-006 error budget, ADR-004, and ADR-007.
- Sections studied:
  - §1 Introduction;
  - §2 Internal accuracy verification, including §§2.1-2.7;
  - §3 External accuracy verification, including §§3.1-3.3;
  - §4 Potential impact;
  - §5 Conclusions;
  - Figs. 1-19 and Tables 1-3 as referenced by those sections;
  - Eq. (7), accumulated parallax weight.
- Intentionally not studied: downstream scientific uses of Hipparcos and individual
  catalogue coordinates. The article is evidence about reduction-level error behavior,
  not a row-selection list or positional oracle.
- Scope reason: the paper tests whether formal errors and correlations in the new
  reduction behave plausibly and explains improvements over the 1997 catalogue.

# Terminology

- **Transit**: a short modulated observation of a star crossing the Hipparcos grid
  (§2.1).
- **Abscissa residual**: along-scan positional residual used in attitude and astrometric
  solutions (§§2.1-2.5).
- **Field-transit abscissa residual (FTAR)**: combined field-transit residual entering
  the astrometric solution (§2.4).
- **Formal error**: uncertainty propagated by the reduction model and checked against
  internal/external behavior.
- **Attitude noise**: residual position error associated with reconstruction of the
  satellite attitude (§2.4).
- **Error correlation**: correlation of abscissa/parallax errors between observations
  or nearby stars, relevant to clustered samples (§2.5).
- **External accuracy verification**: comparisons with radio-star observations,
  reference-frame orientation/spin, and parallax-distribution behavior (§3).
- **Accumulated weight**: the sum of inverse squared formal parallax errors used in §4
  to compare aggregate precision.

# Concepts and models

## Layered validation

The paper follows uncertainties through several reduction levels rather than checking
only final rows: modulation phase (§2.1), basic angle and instrument parameters (§2.2),
attitude reconstruction, field-transit residuals and astrometric parameters (§2.4),
correlations (§2.5), and final formal-error dependencies (§2.6). This supports a UFUQ
rule that catalogue uncertainty cannot be represented by one global “Hipparcos
accuracy.”

## Remaining dependencies

Section 2.6 identifies photon statistics, number/distribution of observations, scan
coverage, and residual calibration/attitude effects as dependencies of formal errors.
Figure 11 shows separate distributions near the ecliptic plane and poles. A magnitude
or a catalogue name alone cannot determine per-star positional uncertainty.

## Correlations

Section 2.5 reports a large reduction in abscissa-error correlations relative to the
1997 reduction, while still examining local parallax correlations for selected stars.
It reports no observed correlation beyond about 3 degrees in that selected analysis,
not a universal theorem that all I/311 rows are independent.

The I/311 `UW` field remains the row-level covariance authority. This article explains
why correlations matter; it does not replace the `ReadMe` layout.

## External checks

Section 3.1 compares a small radio-star sample and explicitly acknowledges the limited
power of external verification at sub-mas accuracy. For eight single stars the paper
reports a weighted mean parallax difference of `-0.013 ± 0.48 mas`, with unit-weight
standard deviation `1.55 ± 0.39`. The sample is too small and contains complications;
it is evidence about aggregate consistency, not a fixture set for arbitrary stars.

Section 3.3 uses negative-parallax and other statistical checks. Its conclusion is
carefully limited: the analysed data do not prove an additional parallax-noise term,
but a small contribution of a few tenths of a mas cannot be excluded.

## Improvement claim

Section 4 and Table 3 report an aggregate weight ratio of 2.16 for selected
five-parameter single-star parallaxes in the new versus old reduction. This does not
mean every coordinate or propagated position is 2.16 times more accurate.

# Equations and algorithms

| Item | Source location | Variables, units, assumptions, and domain | UFUQ use and validation |
|---|---|---|---|
| Modulation-phase formal-error scaling | §2.1, equation immediately following the introduction of modulation phase; Fig. 1 | Relates the phase uncertainty to first-harmonic modulation amplitude `M1` and integrated photon count `I_tot`; the paper notes the scale's mission stability. | Explains photon-statistics dependence only. It is not needed in the UFUQ runtime catalogue path. |
| Catalogue/frame comparison | §3.1, Eqs. (1)-(4); §3.2 | Small rotations/spins are estimated from position/proper-motion differences between radio and optical or old/new catalogues. Units are mas or mas/year as labelled in the article. | Context for external frame checks; do not use the small sample as the sole modern ICRS oracle. |
| Additional-noise tests | §3.3; Figs. 16-18; Table 2 | Statistical behavior of negative parallaxes and selected comparison samples tests consistency of formal errors. | Preserve negative parallaxes and uncertainty fields; do not censor them merely because they are physically unintuitive. |
| Accumulated parallax weight | §4, Eq. (7) and Table 3 | `w = sum_i (1/sigma_pi)^2`; `sigma_pi` is formal parallax error in mas. Aggregate ratios assume the defined selections. | May compare candidate subsets descriptively. Never convert aggregate weight into an individual-star tolerance. |

# Conventions

- Journal statistical results use milliarcseconds and milliarcseconds per year where
  labelled.
- Comparisons distinguish single and double/multiple or otherwise special solutions.
- Negative parallax is a legitimate noisy astrometric estimate and participates in
  distribution-level validation.
- Formal errors and correlations are catalogue-solution evidence, not horizontal
  position, renderer, or learner-answer thresholds.
- Magnitude-dependent and sky-coverage-dependent uncertainty must remain visible.
- Article-level aggregate comparisons do not override row-level solution type,
  covariance factor, and quality metadata in the I/311 `ReadMe`.

# Implementation implications

- `SOURCE_REQUIRED`: retain formal errors, solution type, and sufficient quality/
  covariance information to avoid representing I/311 as uniformly precise.
- `PROJECT_DECISION_REQUIRED`: define approved selection and treatment of
  five-/seven-/nine-parameter, stochastic, VIM, double, photocentre, and secondary
  solutions.
- `SOURCE_REQUIRED`: preserve negative parallaxes and flags through acquisition/
  normalization unless a reviewed downstream rule explicitly filters them.
- `PROJECT_DECISION_REQUIRED`: define whether and how covariance enters propagation and
  error budgets; a scalar error-only design needs an explicit omission rationale.
- `EXPERIMENT_REQUIRED`: compare the approved UFUQ subset and propagated reference
  outputs against independent Astropy/SOFA fixtures; this paper is not a coordinate
  oracle.
- `EXPERIMENT_REQUIRED`: derive date-dependent propagated uncertainty and numeric
  tolerance per scenario. Do not reuse the paper's aggregate improvement factor or
  sub-mas discussion as an acceptance threshold.
- `INFORMATIONAL_ONLY`: the paper supports preferring the new reduction for many
  scientific uses, but the project's bounded source selection and its licensing policy
  are separate decisions.

# Testing implications

- Data validation must retain negative parallax, formal errors, solution/quality fields,
  and any approved covariance representation.
- Create synthetic/statistical tests showing that a global catalogue accuracy constant
  cannot replace per-row error metadata.
- Partition candidate rows by magnitude, sky region/ecliptic latitude, solution type,
  multiplicity/photocentre flags, and formal error when evaluating the subset.
- If correlations/covariance are omitted, measure sensitivity on the approved subset
  and record the bound and reviewer decision.
- Independent position fixtures must come from a pinned oracle and exact catalogue
  fields, not from plots/tables manually transcribed from the validation article.
- Stop if the manifest cannot identify the corrected I/311 byte version, selected
  quality policy, uncertainty mapping, or independent propagation reference.

# Limitations

- The external radio-star sample is small and the paper itself describes limited
  verification power below roughly the sub-mas scale.
- The paper does not prove that every row's formal errors are perfect or that no
  additional noise exists.
- Aggregate weight improvement does not imply uniform per-star improvement.
- The article does not define fixed-width fields, nulls, solution encoding, or
  redistribution; the I/311 `ReadMe` and acquisition/licence record control those.
- It does not supply current observation-time coordinates, apparent positions, horizon
  positions, or UFUQ tolerances.
- It does not select a catalogue for UFUQ; the separate project decision supplies that
  choice for the bounded Phase 1 local spike.

# Conflicts and ambiguities

- The abstract/result supports improved aggregate precision and confirms the formal
  parallax errors within the available checks, while §3.3 says a small extra-noise
  contribution cannot be excluded. UFUQ must retain both statements.
- Local I/311 files include a later correction to goodness-of-fit values and a corrected
  September 2008 byte release. The 2007 paper cannot identify UFUQ's local bytes by
  itself.
- Reported local correlations are selection- and separation-dependent. They do not
  justify assuming either full independence or a universal correlation length.
- The article's frame comparison is relative to then-available optical/radio
  realizations; a current independent oracle still needs pinned modern software/data.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Validation follows errors through multiple reduction levels | §§2.1-2.6; Figs. 1-12 | Retain row-level uncertainty and quality evidence | `SOURCE_REQUIRED` |
| Residual attitude noise is reduced but not absent | §2.4, discussion around Figs. 5-7 | Do not model the catalogue as exact | `SOURCE_REQUIRED` |
| Error correlations matter | §2.5, Figs. 8-10 | Preserve covariance or document/measure omission | `PROJECT_DECISION_REQUIRED` |
| Formal errors depend on magnitude and coverage | §2.6, Figs. 11-12 | Avoid one global Hipparcos accuracy | `SOURCE_REQUIRED` |
| External radio comparison is small/limited | §3.1, Figs. 13-15 | Do not use it as the only numerical oracle | `SOURCE_REQUIRED` |
| Additional small noise cannot be excluded | §3.3 conclusion | Include catalogue uncertainty in the error budget | `EXPERIMENT_REQUIRED` |
| Aggregate weight ratio is selection-level evidence | §4, Eq. (7), Table 3 | Do not turn 2.16 into a per-star/tolerance claim | `INFORMATIONAL_ONLY` |
| Byte layout and corrected release come from elsewhere | I/311 `ReadMe` Notice/File Summary | Join article evidence to a pinned catalogue manifest | `PROJECT_DECISION_REQUIRED` |
