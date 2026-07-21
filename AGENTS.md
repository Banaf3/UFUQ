# UFUQ agent instructions

## Read first

Read `docs/STATUS.md`, `docs/OPEN_QUESTIONS.md`, `docs/REPORT_DEVIATIONS.md`, `docs/EXECUTION_PLAN.md`, and `docs/ARCHITECTURE.md`; then read the domain specification and ADRs relevant to the task. Each major coding phase requires its own approved ExecPlan following `.agent/PLANS.md`.

## Restricted material

`local-reference/` is private and Git-ignored. Never commit, upload, move, copy, quote, or summarize its report into tracked files beyond the already approved paraphrased requirements. Never add the PDF or extracted text to a prompt, issue, artifact, fixture, log, or generated documentation.

## Dependency rules

- `astronomy-core`, `bkt-core`, `assessment-core`, and `adaptive-policy` are pure TypeScript. They may not import React, Three.js, React Three Fiber, Express, MySQL clients, browser globals, or persistence code.
- Adapters depend inward on pure domains; pure domains never depend on adapters or applications. `apps/web` and `apps/api` communicate through versioned contracts.
- The API is authoritative for scenario validity, correctness, BKT transitions, and the next scaffold state. The client submits raw answer evidence, never authoritative correctness or mastery.
- One accepted assessment submission, its attempt record, mastery update, and scaffold transition are one idempotent database transaction.

## Never invent

Do not invent catalogue identifiers or coordinates, Arabic names/transliterations, asterism membership or line segments, Kaaba coordinates, astronomical reference-frame/time policies, tolerances, BKT parameters or threshold, scaffold meaning, research protocol, privacy retention, or accessibility equivalence. Use `docs/OPEN_QUESTIONS.md`; record approved answers in the owning specification and an ADR.

## Commands

Before a toolchain exists, use `git status --short`, `git diff --check`, and targeted `rg` checks. Once the package scripts are introduced by an approved ExecPlan, the required gates are `npm ci`, `npm run check`, `npm run data:verify`, `npm run test`, `npm run test:reference`, `npm run test:integration`, and `npm run test:e2e`. Do not weaken a gate to make a change pass.

## Documentation and scope

Keep requirement IDs, traceability, ADRs, risk status, open questions, deviations, and `docs/STATUS.md` synchronized with behavior. Mark decisions with the four repository classifications. Keep MVP and optional work separate. Do not substitute an iframe, Stellarium/external planetarium engine, native app, mobile-only app, or manually copied star coordinates.

## Definition of done

A change is done only when its ExecPlan acceptance criteria pass; pure-domain, integration, reference, and browser tests appropriate to the change pass; scientific and cultural inputs are cited and approved; atomic/retry behavior is demonstrated where relevant; documentation and traceability are updated; no restricted material or secret is tracked; and thesis evidence is reproducible. Unresolved decisions stop the affected implementation—they are not guessed.
