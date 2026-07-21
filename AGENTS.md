# UFUQ agent instructions

## Default implementation reading path

For ordinary scaffolding and implementation work, read only this baseline first:

1. `AGENTS.md`
2. `docs/IMPLEMENTATION_BRIEF.md`
3. `docs/ARCHITECTURE.md`
4. `docs/IMPLEMENTATION_DECISIONS.md`
5. `docs/PHASES.md`
6. `docs/TEST_PLAN.md`
7. `docs/STATUS.md`

Then read only the domain specification and ADR relevant to the current phase. Do not
load `docs/governance/` by default.

Read the relevant governance files only when the task concerns:

- formal scientific approval or a thesis-grade science claim;
- Arabic/Islamic cultural-content validation;
- participant research, instruments, ethics, consent, or analysis;
- privacy/security release assessment or production learner accounts;
- deployment, operations, backup/restore, or public release;
- report deviations, thesis traceability, or final evidence reconciliation.

The repository scaffold and replaceable technical spikes do not require meeting
frequency, reviewer availability, expected response dates, or a personal weekly
schedule. Use `.agent/PLANS.md` only when the current work meets its planning trigger.

## Restricted material

`local-reference/` is private and Git-ignored. Never commit, upload, move, copy, quote, or summarize its report into tracked files beyond the already approved paraphrased requirements. Never add the PDF or extracted text to a prompt, issue, artifact, fixture, log, or generated documentation.

## Dependency rules

- `astronomy-core`, `bkt-core`, `assessment-core`, and `adaptive-policy` are pure TypeScript. They may not import React, Three.js, React Three Fiber, Express, MySQL clients, browser globals, or persistence code.
- Adapters depend inward on pure domains; pure domains never depend on adapters or applications. `apps/web` and `apps/api` communicate through versioned contracts.
- The API is authoritative for scenario validity, correctness, BKT transitions, and the next scaffold state. The client submits raw answer evidence, never authoritative correctness or mastery.
- One accepted assessment submission, its attempt record, mastery update, and scaffold transition are one idempotent database transaction.
- Celestial lesson flow is data-driven through versioned `SkyPattern`,
  `GuidanceRelationship`, and `LessonRoute` records. Do not hardcode Banat Na'sh—or any
  other named pattern—as the universal route entry point.

## Never invent

Do not invent catalogue identifiers or coordinates, Arabic names/transliterations,
asterism membership or line segments, Kaaba coordinates, astronomical
reference-frame/time policies, tolerances, BKT parameters or threshold, scaffold
meaning, research protocol, privacy retention, or accessibility equivalence. An
unresolved value blocks only its affected behavior: scaffold the interface or use a
clearly synthetic technical fixture where `IMPLEMENTATION_DECISIONS.md` permits it.
Formal answers remain recorded in `docs/governance/OPEN_QUESTIONS.md`, the owning
specification, and an ADR.

Exact helper patterns and cultural mappings remain provisional. Synthetic route records
may test generic schemas and selection logic, but must be visibly non-production and
must not reuse invented cultural claims.

## Commands

Before the Phase 0 toolchain exists, use `git status --short`, `git diff --check`, and
targeted `rg` checks. Once package scripts exist, use the applicable gates defined in
`docs/TEST_PLAN.md`: `npm ci`, `npm run check`, `npm run data:verify`, `npm run test`,
`npm run test:reference`, `npm run test:integration`, and `npm run test:e2e`. A suite
may honestly report that no applicable behavior exists yet; it may not claim unbuilt
behavior is covered. Do not weaken a gate to make a change pass.

## Documentation and scope

Keep `IMPLEMENTATION_DECISIONS.md`, `PHASES.md`, `TEST_PLAN.md`, ADRs, and
`docs/STATUS.md` synchronized with implemented behavior. Update governance
traceability/registers only when a task triggers that context. Preserve MVP/optional
separation. Do not substitute an iframe, Stellarium/external planetarium engine, native
app, mobile-only app, or manually copied star coordinates.

## Definition of done

A change is done when the applicable phase outcome and tests pass, implementation
decisions/documentation match behavior, no restricted material or secret is tracked,
and no unresolved value was guessed. Scientific/cultural approval, atomic/retry proof,
participant evidence, privacy/security release, deployment, and thesis traceability are
required only when the change makes the corresponding claim or crosses that gate.
