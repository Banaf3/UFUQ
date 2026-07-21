# UFUQ executable plans

Use a self-contained living ExecPlan when a task changes cross-package architecture,
introduces a schema migration, selects scientific policy, changes security-sensitive
behavior, spans multiple sessions, or is explicitly requested. Store it as
`.agent/execplans/phase-XX-short-name.md` and link it to the phase in `docs/PHASES.md`.
The empty Phase 0 repository scaffold does not require a separate ExecPlan when its
work remains within the approved layout and decisions in the default implementation
documents.

An ExecPlan must let a new contributor complete and verify the work using only the repository and the plan. Prefer observable outcomes over internal activity. Update the plan while work proceeds; do not treat it as a one-time proposal.

## Required structure

```markdown
# <Phase and outcome>

## Purpose and user-visible outcome
Why this phase exists, the research claim it supports, and what becomes demonstrable.

## Classification and authority
Related CONFIRMED/CLARIFIED decisions, approved deviations, manual inputs, ADRs, and named owner/approval date.

## Progress
- [ ] YYYY-MM-DD HH:MMZ — concrete step

## Surprises and discoveries
Unexpected behavior with concise evidence.

## Decision log
Date, classification, decision, reason, approver when required, and affected documents.

## Outcomes and retrospective
What passed, what remains, and evidence locations.

## Context and orientation
Relevant files, packages, domain terms, invariants, and current behavior. Define non-obvious terms.

## Dependencies and manual inputs
Prerequisites, exact approved scientific/educational values, fixtures, tools, and blocking decisions.

## Scope guard
The protected outcome, excluded work, dependencies, stop/go checks, and explicit
deferral triggers. Do not require personal weekly schedules, meeting frequency, reviewer
availability, or expected response dates as repository context. A scope change never
silently changes a report requirement or evidence claim.

## Milestones and implementation narrative
Ordered, independently verifiable increments. For each: files, behavior, tests, and evidence.

## Commands
Exact commands and working directory, including expected success signals.

## Validation and acceptance
Measurable functional, numerical, transactional, browser, accessibility, performance, and documentation gates that apply.

## Idempotence, rollback, and recovery
How reruns behave, how partial work is detected, and how to return to the prior safe state without deleting user work.

## Risks and safeguards
Linked risk IDs, failure indicators, mitigations, and escalation conditions.

## Evidence for the thesis
Artifacts to retain without personal data, secrets, restricted report text, or licensed data that cannot be redistributed. Name the evidence-manifest path and include requirement/risk IDs, exact command and working directory, commit/dirty state, environment/hardware/browser, input and artifact hashes, raw/derived classification, approvals, access/retention class, and clean-environment reproduction steps.
```

Plans must name exact repository paths and public interfaces when known, explain dependency direction, and include fixed reference fixtures. If a manual decision is still open, the plan may prepare reversible infrastructure but may not encode a guessed value. When implementation finishes, reconcile progress, decisions, outcomes, traceability, ADRs, and `docs/STATUS.md`.
