# Mandatory-rule traceability

Detailed evidence is in
`docs/references/syntheses/astronomy-model-synthesis.md` and the six astronomy dossiers.

| Skill rule | Evidence basis | Classification |
|---|---|---|
| Workflow 1: explicit frames, epoch, time, observer, units, motion, refraction, and IERS data | SOFA `iauAtco13`/`iauApco13`; IERS TN36 Chs. 2 and 5; ESA 1997 §§1.2.1 and 1.2.5-1.2.6; I/311 byte descriptions; ADR-003 | Source plus project decision |
| Workflow 2: supported range and invalid/singular cases | SOFA routine status/range notes; AST-003/004/006 | Project decision and experiment |
| Workflow 3: trace each step and bound omissions | SOFA `doc/intro.lis` Accuracy plus routine contracts; IERS Ch. 5; AST-003/006 | Source, project decision, experiment |
| Workflow 4: pin an independent oracle and audit imports/code sharing | Kanewala/Bieman §3.3, pp. 18-19; ADR-007; `docs/TEST_PLAN.md` | Source plus project decision |
| Workflow 5: fixtures retain policies, software/data versions, inputs, provenance, and outputs | Wilson et al. 2014 pp. 2-3; `docs/ASTRONOMY_SPEC.md` Validation §1-3 | Source plus project decision |
| Workflow 6: compare with angular/circular metrics | `docs/ASTRONOMY_SPEC.md`, Angular comparison | Project decision |
| Workflow 7: derive threshold from measured disagreement and an error budget | Kanewala/Bieman §3.3, p. 19; SOFA accuracy limitations; AST-006 | Experiment plus project decision |
| Workflow 8: partition boundary/scientific cases | SOFA routine contracts; IERS Eqs. (5.1), (5.14)-(5.15); ESA 1997 §1.5.4 Eq. (1.5.21) p. 94 for high-declination/cosine guards; `docs/ASTRONOMY_SPEC.md` Validation §5 | Source plus project decision |
| Workflow 9: reject visual plausibility as evidence | Kanewala/Bieman §1, pp. 1-2; ADR-007 | Source plus project decision |
| Stop: missing frame/epoch/time/observer/motion/refraction/IERS/range/tolerance | SOFA and IERS input contracts; `docs/ASTRONOMY_SPEC.md` safety rule | Source plus unresolved project decisions |
| Stop: I/311 `pmRA` star-component versus coordinate-angle mapping is unconfirmed | `studies/hipparcos-esa-1997-field-semantics.study.md`; I/311 `hip2.dat` bytes 52-59 | Source-supported strong inference plus unresolved experiment |
| Stop: unpinned or non-independent oracle | Kanewala/Bieman pseudo-oracle limitations; ADR-007 | Source plus project decision |
| Prohibition: do not invent scientific inputs, policies, or tolerances | `AGENTS.md`; `docs/ASTRONOMY_SPEC.md` safety rule | Project decision |
| Prohibition: Polaris is not True North | `docs/ASTRONOMY_SPEC.md`, astrometric pipeline/KC-04 distinction | Project decision |
| Prohibition: Three.js mapping is not an astronomy oracle | `docs/ASTRONOMY_SPEC.md`, Three.js mapping | Project decision |

The ESA source closes the original-1997 meaning, not the I/311 mapping. I/311
proper-motion-component and exact-epoch semantics remain explicit stop conditions and
are classified `STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED`.
