# Mandatory-rule traceability

Detailed evidence is in
`docs/references/syntheses/engineering-quality-synthesis.md` and the linked dossiers.

| Skill rule | Evidence basis | Classification |
|---|---|---|
| Workflow 1: state claim, phase, and gate | Bass et al. §3.3, printed pp. 42-44; `docs/PHASES.md` | Source plus project decision |
| Workflow 2: separate fact, decision, provisional choice, and gap | `AGENTS.md`; `docs/references/UFUQ_SOURCE_REGISTER.md` | Project decision |
| Workflow 3: name a quality attribute/dependency risk and reject style-only work | Bass et al. §§1.3, 3.2-3.3, printed pp. 19, 41-44 | Source |
| Workflow 4: inspect actual manifests/imports/exports/references/scripts/tests/CI | Bass et al. §§1.3, 21.2, printed pp. 19-20, 310-311; `docs/ARCHITECTURE.md` | Source plus project decision |
| Workflow 5: run and record the smallest reproducible command set | Wilson et al. 2014, Box 1 and pp. 2-3; Bass et al. §§21.1, 21.6 | Source |
| Workflow 6: confirm pure boundaries, tool isolation, public APIs, and fail-closed suites | `AGENTS.md`; `docs/ARCHITECTURE.md`; `docs/TEST_PLAN.md` | Project decision |
| Workflow 7: require an independent scientific reference | Kanewala/Bieman §§3.2-3.3, preprint pp. 13-19; ADR-007 | Source plus project decision |
| Workflow 8: compare change/keep risks and choose the smallest correction | Bass et al. §§21.1, 21.6, printed pp. 309-310, 324-326; Wilson et al. 2017 Overview | Source |
| Workflow 9: report evidence without unauthorized decision changes | Bass et al. §22.7, printed pp. 346-347; `AGENTS.md` | Source plus project decision |
| Stop: no demonstrated risk/cost | Bass et al. §1.3 and §§21.1-21.2 | Source |
| Stop: skipped/empty/weak active gate | `docs/TEST_PLAN.md`, Failure and evidence rules | Project decision |
| Stop: missing input/environment/independent evidence | Kanewala/Bieman §§3.2-3.3; `AGENTS.md` | Source plus project decision |
| Prohibition: no enterprise layers or book-pattern redesign by assumption | Bass et al. §1.3, p. 19; Wilson et al. 2017 pp. 9-11; approved eight-workspace architecture | Source plus project decision |
| Prohibition: type/coverage/visual plausibility is not scientific correctness | Kanewala/Bieman §1 and §3.2, pp. 1-2, 13-15 | Source |

No mandatory engineering rule depends on an unsupported external claim.

