# UFUQ phase/source matrix

## Reading rule

Use the smallest source set that can support the current claim. Project decisions define
UFUQ behavior; external sources support scientific, data, cultural, educational, or
engineering assertions. Missing sources block only the affected claim or behavior.

| Phase | Required project decisions | Required external sources | Supporting sources | Unresolved source gate |
|---|---|---|---|---|
| Phase 0: repository scaffold and reference preparation | UFUQ-AGENTS, UFUQ-ARCH, UFUQ-IMPL-DEC, UFUQ-PHASES, UFUQ-TEST, UFUQ-ADR-007 | None for empty domain packages | BASS-ET-AL-2022, WILSON-ET-AL-2014, WILSON-ET-AL-2017, KANEWALA-BIEMAN-2014 | None; source preparation does not activate Phase 1 |
| Phase 1: astronomy behaviour and data technical spike | UFUQ-ASTRO-SPEC, UFUQ-DATA, UFUQ-ADR-003, UFUQ-ADR-004, UFUQ-ADR-007, ScientificProfileV1 | SOFA-2023-10-11, IERS-TN36-2010, IERS-BULLETIN-B, IERS-BULLETIN-C, IERS-GAZETTE-13, IERS-C04-GUIDE, IANA-TZDB-LEAPS, JSON-SCHEMA-CORE-2020-12, JSON-SCHEMA-VALIDATION-2020-12, ASTROPY-DOCS-PIN, PYERFA-PIN, ASTROPY-IERS-DATA-PIN, RFC3339-TIMESTAMP, UMPSA-FK-PEKAN-SITE; HIP-I311-README, ESA-HIP-1997-V1, and VAN-LEEUWEN-2007-VALIDATION only for the I/311 local spike | Current official implementation-candidate audit: ASTRONOMY-ENGINE-2.1.19, ASTRONOMIA-4.2.0, OBSERVERLY-ASTROMETRY-0.66.0, TSOFA-18.1.0, ERFA-2.0.1; JUPEM-GEODETIC as an optional 2D observer-data route; EXSUP-3E, FUND-ASTRO-6E, FAIR-2016; KARNEY-2013 only if ellipsoidal Qibla is separately in scope | Zero 2C semantic blockers remain. The one-preset/time/boundary/outcome contracts, source-neutral SOFA `2023-10-11`-derived route/effect/runtime-astrometry mapping, and final-only leap/EOP quality/interpolation/offline/update policy are normative. Exact observer/source/leap/EOP/configuration bytes and derived bounds move to 2D/2E; production residuals, stronger-independent evidence and tolerances follow implementation. |
| Phase 2: minimal data-driven vertical slice | UFUQ-ARCH data-driven guidance, UFUQ-DATA, approved ScientificProfileV1 | The 2D/2E-approved catalogue, observer, leap and EOP artifacts gate real ProfileV1 execution; generic observer/astronomy contracts do not require their numerical values. Pinned production/reference fixtures follow code and gate scientific acceptance; approved cultural evidence gates only each learner-facing record that makes the claim | IBN-QUTAYBA-ANWA, KUNITZSCH-1961, HAFEZ-2010; KING sources only as context | Production/reference and any required stronger-independent evidence gate scientific acceptance after implementation; Najdi/regional evidence gates only claims labelled regional; exact membership/routes, Arabic review, and educational review remain missing. |
| Phase 3: assessments and BKT adaptation | UFUQ-BKT-SPEC, UFUQ-TEST, relevant assessment ADRs | Original knowledge-tracing source, Evidence-Centered Design, scaffolding research, BKT properties/sensitivity sources, educational-testing standards | KANEWALA-BIEMAN-2014 for oracle/test design | All listed education/BKT source families are unresolved; no active BKT skill is created yet |
| Phase 4: persistence and authentication | UFUQ-ARCH persistence/authority rules, persistence ADR, security/privacy decisions | OWASP ASVS, NIST SSDF, official MySQL transaction/isolation/deadlock documentation | BASS-ET-AL-2022 for quality-attribute review | Pin MySQL profile and security standards before production learner-account claims |
| Phase 5: complete lessons, dashboards, and hardening | Approved Phase 1–4 decisions and evidence | WCAG 2.2, WAI-ARIA APG, pinned Three.js/R3F documentation, selected 3D interaction/performance references | BASS-ET-AL-2022 and scientific-computing practices | Accessibility-equivalence and performance-reference sources remain unresolved |
| Phase 6: participant evaluation and deployment | Governance research, privacy, deployment, and thesis-traceability documents | Standards for Educational and Psychological Testing, selected usability instrument, study-design guidance, UMPSA ethics/data requirements, release-security sources | Earlier phase evidence manifests | Ethics, instrument, study design, participant-data, and deployment approvals remain unresolved |

## Cross-cutting distinctions

- SOFA/IERS/catalogue sources establish technical semantics; they do not approve a
  learner tolerance or educational task.
- Cultural sources establish historical or regional evidence only at their stated
  scope; they do not approve a modern instructional route.
- A reproducible reference result requires pinned software, datasets, policies, inputs,
  lineage, and comparison method. Calling it an independent oracle additionally
  requires demonstrated algorithm/code-lineage independence from production.
- FAIR and PROV sources may improve vocabulary and data hygiene without becoming
  compliance targets.
- Historical qibla sources do not replace a modern, approved geodesic convention.
