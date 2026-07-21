# UFUQ executable plans

Every major implementation phase in `docs/EXECUTION_PLAN.md` must have a self-contained, living ExecPlan before coding begins. Store it as `.agent/execplans/phase-XX-short-name.md`. Also require an ExecPlan for cross-package architectural change, schema migration, scientific-policy change, security-sensitive change, or work expected to span multiple sessions.

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

## Schedule, capacity, and scope guard
Available developer time, external-approval lead times, milestone effort ranges,
latest-decision dates, stop/go checks, protected minimum outcome, and explicit deferral
triggers linked to SCOPE-002. A schedule slip never silently changes a report requirement
or evidence claim.

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
