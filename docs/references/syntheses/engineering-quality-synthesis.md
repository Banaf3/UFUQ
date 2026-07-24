# Engineering quality synthesis

## Scope

This synthesis compares the engineering sources that can guide UFUQ now:

- `BASS-ET-AL-2022`;
- `WILSON-ET-AL-2014`;
- `WILSON-ET-AL-2017`;
- `KANEWALA-BIEMAN-2014` / the local 2018 preprint; and
- the approved UFUQ architecture, phase, test, and ADR decisions.

Detailed locations and limitations are in the corresponding files under
`../studies/`.

## Authority by topic

| Topic | Controlling authority | Supporting sources | Boundary |
|---|---|---|---|
| Current package and dependency design | Tracked UFUQ architecture and ADRs | Bass et al., §§1.3, 3.2-3.5, 21.1-21.7, 22.7 | A general architecture pattern cannot override an approved project decision. |
| Quality-attribute review | Bass et al., §§3.2-3.5 and 21 | Observed repository behavior and measurements | A major finding needs a concrete stimulus, response, and measure. |
| Reproducible computational workflow | Wilson et al. 2014, pp. 2-5 | Wilson et al. 2017, pp. 2-15 | Licence, privacy, and restricted-material rules still control what may be tracked. |
| Small-project proportionality | Wilson et al. 2017, Overview and pp. 18-19 | Bass et al., §21.6 | “Good enough” does not authorize weakening an already active gate. |
| Scientific testing and oracle limits | Kanewala and Bieman, §§3.2-4.3 | Wilson et al. 2014, p. 4 | The review supplies no astronomy result or universal tolerance. |
| Phase suite activation | `docs/TEST_PLAN.md` | Scientific-testing literature | Project decisions define when suites become mandatory and fail closed. |

## Agreements

1. Important work should be divided into explicit, testable responsibilities with
   controllable inputs and observable results. Bass et al. ground the architecture and
   testability language; both Wilson papers ground small modular functions and explicit
   workflows.
2. Exact commands, inputs, software versions, parameters, and outputs are part of
   reproducibility evidence. This supports UFUQ's lockfile, manifests, independent
   oracle environment, and deterministic data pipeline.
3. Automated unit, integration, regression, and system/reference checks are
   complementary. A passing type check, plausible display, or no-crash run does not
   establish scientific correctness.
4. Reference implementations and datasets are useful but fallible. An independent
   implementation can share a specification error, and regression output can preserve
   an old error. Multiple evidence layers and explicit limitations are required.
5. Process and architecture effort should be proportional to demonstrated risk. For one
   FYP developer, focused checks and a lightweight review are preferable to adopting
   enterprise layers without a concrete failure mode.

## Tensions and resolutions

| Tension | Evidence | UFUQ treatment |
|---|---|---|
| Track raw inputs versus keep restricted bytes out of Git | Wilson 2014 recommends versioning sources; Wilson 2017 warns against sharing restricted/large data | Preserve ignored immutable bytes locally and track only permissible manifests, hashes, scripts, and citations. |
| A simpler implementation as oracle versus shared-fault risk | Wilson 2014, p. 4; Kanewala/Bieman, §3.3 | Require genuine implementation independence plus authoritative/simple cases and disagreement investigation. |
| Comprehensive architecture evaluation versus FYP cost | Bass et al., Ch. 21; Wilson 2017 | Use a focused, risk-based review unless a high-impact decision justifies more ceremony. |
| Minimal novice workflow versus existing active CI | Wilson 2017, p. 18; `docs/TEST_PLAN.md` | Keep Phase 0 gates. Proportionality governs new controls, not removal of proven gates. |

## Candidate UFUQ rules

| Rule | Basis | Classification |
|---|---|---|
| State a reproducible quality-attribute scenario before proposing a major architecture change. | Bass et al., §§3.2-3.3, pp. 41-44 | `SOURCE_SUPPORTED_FACT` |
| Preserve the approved eight-workspace structure unless a dependency violation, observed failure, or measurable maintenance cost justifies an ADR change. | `docs/ARCHITECTURE.md`; Bass et al., §1.3, p. 19 | `PROJECT_DECISION` |
| Record exact commands, input/data versions, parameters, environment, outputs, and failures for evidence-bearing runs. | Wilson et al. 2014, pp. 2-3; Wilson et al. 2017, pp. 6-8 | `SOURCE_SUPPORTED_FACT` |
| Keep pure scientific and tutoring domains free of framework, I/O, and persistence dependencies. | `AGENTS.md`; `docs/ARCHITECTURE.md` | `PROJECT_DECISION` |
| Once a suite is active, it must fail when no expected test is discovered; placeholders and `passWithNoTests` are not evidence. | `docs/TEST_PLAN.md` | `PROJECT_DECISION` |
| Scientific claims need a source-grounded independent reference and layered tests; agreement between production copies is insufficient. | Kanewala/Bieman, §§3.2-3.3; ADR-007 | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` |
| Numerical tolerance is measured over the declared domain and approved after an error analysis. | Kanewala/Bieman, §3.3, p. 19; AST-006 | `EXPERIMENT_REQUIRED` |
| Architecture review effort and corrections should be the smallest sufficient response to the demonstrated risk. | Bass et al., §§21.1, 21.6; Wilson 2017 | `SOURCE_SUPPORTED_FACT` |

## Testing consequences

- Reproduce every gate from a clean/pinned environment and retain exit status.
- Test dependency rules against actual manifests, public exports, imports, and project
  references rather than folder names alone.
- Demonstrate fail-closed behavior for active suites as well as successful behavior.
- Isolate external clocks, files, networks, databases, catalogue inputs, and oracle
  tools behind explicit inputs or adapters when their state affects a test.
- Convert confirmed faults into regression tests, while retaining separate independent
  scientific fixtures.
- Record risks of both changing and retaining an architecture.

## Unresolved gaps

- The current sources do not close astronomy, catalogue, Qibla, cultural, BKT,
  security, accessibility, participant-research, or deployment decisions.
- No source provides a universal coverage target, test count, performance threshold, or
  numerical tolerance.
- A future architecture change still needs current repository measurements; these books
  cannot supply them in advance.

