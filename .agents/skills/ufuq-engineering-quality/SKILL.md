---
name: ufuq-engineering-quality
description: Review UFUQ architecture, package-boundary, reproducibility, test-gate, or engineering-evidence changes. Use when an engineering proposal or implementation needs a quality-attribute-backed review; do not use for validating astronomical, geodesic, or cultural facts.
---

# Ufuq Engineering Quality

Review engineering claims against UFUQ's approved boundaries and evidence, without
turning general architecture literature into a redesign mandate.

## Trigger conditions

Use this skill when a task asks to:

- review or change repository structure, package dependencies, build/test gates, CI,
  reproducibility, deterministic tooling, or maintainability;
- justify an architecture change with a concrete quality attribute, dependency
  violation, observed failure, or measured cost;
- assess whether engineering evidence is sufficient for a phase gate or thesis claim.

Do not trigger it for:

- choosing an astronomical frame, time scale, catalogue field, tolerance, or reference
  fixture; use `ufuq-astronomy-validation` or `ufuq-catalogue-provenance`;
- deriving Qibla or selecting target coordinates; use `ufuq-qibla-geodesy`;
- classifying Arabic, Arabian, or Najdi claims; use `ufuq-najdi-arabian-sky`;
- ordinary edits whose correctness is already covered by a narrow existing test.

## Required project files

Read `AGENTS.md`, `docs/ARCHITECTURE.md`, `docs/IMPLEMENTATION_DECISIONS.md`,
`docs/PHASES.md`, `docs/TEST_PLAN.md`, and `docs/STATUS.md`. Read the affected ADR and
`docs/references/UFUQ_SOURCE_REGISTER.md`. Read
`docs/references/SOURCE_GAPS.md` when the claim crosses into a missing evidence area.
Then read `docs/references/syntheses/engineering-quality-synthesis.md` and this skill's
`references/source-notes.md`, `references/traceability.md`,
`references/review-checklist.md`, and `references/output-template.md`. Open only the
study dossiers linked for the rule or claim under review.

## Source authority order

1. Current tracked UFUQ decisions and observed repository behavior.
2. Reproducible command output, dependency graphs, tests, and measurements.
3. Independent scientific-reference evidence for scientific behavior.
4. *Software Architecture in Practice* for named quality attributes and trade-offs.
5. Scientific-computing and scientific-testing research for proportional workflow
   controls.

Books and papers cannot silently override an approved project decision. Record an
actual contradiction before proposing a decision change.

## Mandatory workflow

1. State the claim, affected phase, and applicable phase gate.
2. Separate observed facts, project decisions, provisional choices, and unresolved
   questions.
3. Identify the exact quality attribute or dependency rule at risk. Reject
   style-only refactors.
4. Inspect current imports, manifests, exports, TypeScript references, scripts, tests,
   and CI paths relevant to that risk.
5. Run the smallest reproducible command set that can confirm or refute the claim.
   Record commands, environment assumptions, exit status, and failures.
6. Confirm pure-domain boundaries, runtime-to-tool isolation, public-entry-point use,
   and fail-closed active suites.
7. For scientific behavior, require an independent reference rather than accepting
   agreement between two copies of production logic.
8. Compare the cost and risk of changing with the cost and risk of keeping the current
   design. Prefer the smallest demonstrated correction suitable for one FYP developer.
9. Confirm every mandatory conclusion has a basis in
   `references/traceability.md`, then report with `references/output-template.md`; do
   not edit architecture decisions unless the task authorizes it.

## Required evidence

- Exact files and dependency paths supporting each finding.
- Exact commands and results for every validation assertion.
- A reproducible failing example or measurable maintenance/quality cost for a major
  architecture change.
- Active-suite failure behavior, not only a passing happy path.
- Independent source/result provenance for scientific correctness claims.

## Stop conditions

Stop and mark the claim unresolved when:

- the proposed change has no demonstrated quality attribute, dependency failure, or
  significant maintenance cost;
- an active gate passes only by skipping tests, using `passWithNoTests`, or weakening a
  boundary;
- required input, environment, or independent evidence is missing;
- the task would silently change an approved architecture or report-level requirement.

## Prohibited assumptions

Do not assume more workspaces, services, repositories, plugins, or layers improve
quality. Do not infer scientific correctness from type safety, coverage, snapshots, or
visual plausibility. Do not treat a book's preferred pattern as a UFUQ requirement.

## Required output

Use `references/output-template.md`. Classify every conclusion as
`SOURCE_SUPPORTED_FACT`, `PROJECT_DECISION`, `PROVISIONAL_CHOICE`, or
`UNRESOLVED_QUESTION`, and every finding as `BLOCKING`, `MAJOR`, `MINOR`, or
`OPTIONAL`.

## Relevant validation commands

Use the applicable existing scripts; do not invent passing placeholder commands:

```text
npm ci
npm run check
npm run test
npm run build
npm run exports:check
npm run test:e2e
```

Add targeted boundary, cycle, import, or deterministic-output checks already defined by
the repository. Phase-inactive reference and integration suites must remain omitted
from Phase 0 CI and fail when invoked empty.
