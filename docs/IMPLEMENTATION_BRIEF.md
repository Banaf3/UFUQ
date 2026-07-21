# UFUQ implementation brief

## Objective

Build UFUQ as a browser-based 3D astronomy tutor that teaches multi-step celestial
guidance. A route may begin with a reviewed helper sky pattern, continue through Banat
Na'sh or Dhat al-Kursi to Al-Jady/Polaris, then connect Al-Jady to True North and True
North to Qibla. The implementation must not hardcode one named pattern as the universal
lesson flow. It should first prove the scientific/data path and then add assessment,
adaptation, persistence, accounts, full lessons, and formal evaluation.

## Start here

The default implementation reading path is:

1. `AGENTS.md`
2. `docs/IMPLEMENTATION_BRIEF.md`
3. `docs/ARCHITECTURE.md`
4. `docs/IMPLEMENTATION_DECISIONS.md`
5. `docs/PHASES.md`
6. `docs/TEST_PLAN.md`
7. `docs/STATUS.md`

Read a domain specification or ADR when the current phase touches that domain:

- astronomy/data: `ASTRONOMY_SPEC.md`, `DATA_STRATEGY.md`, ADR-003/004;
- 3D integration: ADR-002;
- assessment/BKT: `TUTORING_BKT_SPEC.md`, ADR-005;
- persistence: ADR-006;
- validation: ADR-007.

`docs/governance/` preserves the detailed review, report relationship, unresolved
authority questions, research protocol, privacy/release planning, and old plans. It is
not default coding context. Load it only for the governance-triggered work listed in
`AGENTS.md`.

## Implementation baseline

- TypeScript monorepo with a React/React Three Fiber/Three.js web app, a Node/Express
  API, MySQL/InnoDB persistence, pure domain packages, versioned contracts, and a
  reproducible catalogue tool.
- The API owns scenario validity, correctness, accepted BKT transitions, mastery
  revisions, and the next scaffold state. The browser sends raw evidence.
- Domain packages remain independent of React, Three.js, HTTP, persistence, browser
  globals, and environment-specific I/O.
- Cultural/educational content is versioned data: `SkyPattern` defines reviewed pattern
  membership/geometry, `GuidanceRelationship` defines one verified guidance edge, and
  `LessonRoute` composes ordered steps and permitted alternatives with prerequisites and
  scaffold configuration.
- The server selects only routes whose referenced patterns/relationships are applicable
  to the scenario and whose required catalogue stars are present in the approved
  scenario dataset.
- Scientific/data behavior is introduced behind typed interfaces. A technical spike may
  use clearly labelled synthetic or candidate fixtures, but they cannot become approved
  learner content or scientific evidence by accident.
- No catalogue row, coordinate, Arabic name, asterism relation, tolerance, BKT
  parameter, or cue meaning is invented to make a test pass.

## What can start now

Phase 0 repository scaffolding can start immediately. It creates folders, workspace and
TypeScript configuration, lint/type/test runners, package-boundary checks, empty public
entry points, and CI-ready scripts. It does not implement domain behavior or select
scientific/cultural values.

After the scaffold passes, Phase 1 may run a replaceable astronomy/data technical spike.
It may compare libraries, schemas, catalogue acquisition methods, coordinate types, and
reference-test mechanics without claiming that a candidate is approved production
truth.

## Hard boundaries

- Do not expose authoritative targets, tolerances, correctness, or mastery decisions to
  the browser.
- Do not encode a fixed Banat Na'sh-first sequence in components, routes, assessment
  code, or BKT policy; resolve the active `LessonRoute` and relationship versions from
  the server-issued scenario.
- Do not let adapters/frameworks leak into pure domain packages.
- Do not manually copy star coordinates or restricted-report content into code, tests,
  logs, or generated data.
- Do not collect participant or production learner data during Phases 0–3.
- Do not treat a technical spike, placeholder, mock, or synthetic fixture as thesis
  evidence for astronomical or educational correctness.
- Do not weaken a test gate because an input remains unresolved; mark the dependent
  behavior unavailable and continue with independent work.

## Active readiness

The four independently assessed readiness gates are maintained in `STATUS.md`.
Scaffolding readiness is intentionally narrower than vertical-slice, participant-study,
or deployment readiness.
