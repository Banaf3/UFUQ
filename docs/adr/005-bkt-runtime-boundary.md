# ADR-005: BKT runtime and adaptive-policy boundary

- **Status:** Blocked pending deviations and manual learning decisions
- **Classification:** CONFIRMED/CLARIFIED plus PROPOSED DEVIATIONS
- **Date:** 2026-07-20
- **Blockers:** DEV-004, DEV-006, DEV-007, DEV-008; BKT-001–BKT-005

## Context

The report uses standard binary BKT per cognitive skill and adaptive visual support. Model arithmetic, scaffold behavior, hinted evidence, and independent-recall claims are different concerns. The provisional parameters cross the `.85` threshold after only two correct answers from `.20`, so assistance semantics materially affect validity.

## Decision

Create a pure `tutoring-core` package with separate `bkt`, `observations`, and
`adaptive-policy` modules. The BKT module implements observation posterior followed by
learning transition; the policy module returns a versioned state/reason. Logical and
test separation is retained without separate npm packages. `tutoring-core` consumes a
typed observation and does not depend on `assessment-core`.
Store separate mastery and a monotonic revision for KC-01–KC-05. Persist a typed
`OBSERVATION`, `TRANSITION_ONLY`, or `NO_MODEL_UPDATE` decision;
prior/posterior/next values where applicable; immutable parameter/policy versions; the
authoritative server-issued cue snapshot; and independent-evidence status in the atomic
submission.

Use proposed `GUIDED`, `FADING`, and `INDEPENDENT` semantics (DEV-004). A manual decision selects how assisted attempts affect BKT (BKT-001/DEV-006). Independent recall is not inferred from threshold alone. Correct the report's “slip trigger” terminology and incorrect-response invariant through DEV-007/008.

## Consequences

- Pure equations are replayable and independently testable.
- UI cue changes cannot silently change model arithmetic.
- Parameter/scaffold versions cannot be edited in place.
- Production behavior is blocked until observation/session-purpose, evidence,
  threshold, version-migration, cue and independent-recall policies are approved.
- Scenarios bind an expected mastery revision; stale delayed evidence is rejected and a
  current task is reissued.
- Fewer physical packages reduce FYP maintenance overhead without merging BKT
  arithmetic, observation eligibility, and scaffold-policy responsibilities.

## Alternatives rejected

- BKT embedded in React components or SQL triggers.
- One mastery score for the whole lesson.
- Treat every click as a BKT observation.
- Claim threshold crossing proves independent learning.
- Dynamically infer “slip rate” from a single wrong answer without a different approved model.

## Validation

Examples/sequences against an independently justified numeric tolerance,
parameter/property/edge tests with retained seeds, typed no-op/transition-only and
assisted-policy fixtures, idempotent/stale-revision replay, sensitivity/policy metrics,
and separate approved no-hint pre/post/immediate-independent evaluation.
