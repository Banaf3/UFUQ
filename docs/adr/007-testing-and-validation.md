# ADR-007: Layered testing and independent validation

- **Status:** Independently reviewed; awaiting owner approval
- **Classification:** CONFIRMED/CLARIFIED; numerical tolerances remain MANUAL DOMAIN DECISION AST-006
- **Date:** 2026-07-20

## Context

UFUQ makes scientific, software, performance, usability, adaptive-model, and learning claims. Tests that reuse production formulas can reproduce the same bug; screenshots cannot prove coordinates; BKT arithmetic cannot prove learning; browser mocks cannot prove InnoDB atomicity.

## Decision

Adopt the layers and configured gates in `../governance/TEST_STRATEGY.md`: pure-domain
units/properties; catalogue schemas; separately authored/reviewed pinned reference
fixtures, plus lineage-independent oracle fixtures where required, and error budgets;
BKT oracles/sensitivity; real-SYS-001
MySQL API/transaction/concurrency tests; deterministic raycast and approved browser
E2E; focused scientific/scaffold visual regression; accessibility; performance;
security/privacy; backup/restore; evidence manifests; and a separately approved human
evaluation. Missing tolerances or baseline configuration fail rather than using invented
constants.

Keep reference fixture generation structurally independent from runtime TypeScript
astronomy. Every fixture and result records software/data/policy/tolerance status.
Missing tolerance prevents numerical acceptance; it does not prevent a clearly
labelled measurement-only experiment or an exact supported invariant. Coverage is
diagnostic; pure decision/formula modules target complete branches, while approved
production/reference evidence plus the error budget is the later acceptance basis.
Any stronger independent-oracle claim additionally requires a lineage audit.

Milestone 2C.5A adds a human and machine experiment registry before execution. Every
record states what it may and cannot establish, its input class, exact dependencies and
conventions, artifact needs, partitions, comparison lineage, metrics, repetitions and
hashes, result schema, acceptance mode, reviewer gate, and follow-up decision. Astropy
high-level transformations and direct PyERFA calls disclose their shared ERFA/SOFA
lineage and cannot validate each other as independent algorithms. Numerical results
remain `MEASURED_NO_ACCEPTANCE` until AST-006 approves bounded terms and an
operation-specific threshold; the separately versioned 2C.5C review-draft ledger
supplies neither. Exact deterministic, status-preservation, and deliberately injected
guard checks may pass or fail without a numerical tolerance.

Milestone 2C.5B completes 9/9 experiments in the registry's synthetic Batch 01. Its
non-production Python runner uses a fixed allowlist, direct pinned PyERFA, canonical
fixtures/results, complete source/data/environment hashes, two isolated fresh-cache
repetitions plus a two-process same-environment replay, and fail-closed
source/scope/schema guards. This does not prove clean-environment dependency
reconstruction. Twenty-four exact checks pass and none fail; six measurement-only
checks cover 27 measurement records, all `MEASURED_NO_ACCEPTANCE`.
Componentized/composed ERFA agreement retains the declared
same-family lineage; deterministic bytes and passing guards do not establish
scientific correctness. Because no production code is compared, this execution does
not activate the reference Vitest suite.

Milestone 2C.5C interprets the committed Batch results without changing a hashed input
or regenerating canonical evidence. Its machine-checkable AST-006 ledger accounts for
all 27 measured
records and all 24 exact passes, but an exact mutation/status/state guard is not a
numerical uncertainty bound. The candidate error-budget method keeps source, model,
Earth-orientation/time, observer, atmosphere, and implementation terms separate;
keeps scene and learner tolerances outside astronomy accuracy; uses boundary-specific
direction/component/time/observer metrics; uses a conservative bounded sum when
dependence is unknown; and permits RSS only with evidence of independent zero-mean
random terms. Correlated, systematic, asymmetric, or nonlinear terms require a joint
model, covariance, or conservative grouped bound. Every required numerical term is
currently unbounded, so all six tolerance classes remain blocked and the AST-006
recommendation is `FINAL_TOLERANCE_NOT_JUSTIFIED`.

Milestone 2C.6 makes the lifecycle non-circular. `PRE_IMPLEMENTATION` evidence consists
of authoritative semantics, the approved `ScientificProfileV1`, frozen synthetic
guards, the pinned candidate reference environment, and planned fixtures. It permits
implementation but not scientific acceptance. `POST_IMPLEMENTATION` evidence consists
of TypeScript/reference residuals, supported-domain partitions, implementation ledger
terms, `test:reference` activation, and tolerance review. A later
`STRONGER_INDEPENDENT_VALIDATION` stage evaluates USNO NOVAS or another genuinely
independent positional-astronomy path; shared Astropy/PyERFA/ERFA/SOFA lineage cannot
satisfy it. Neither later stage is required before the implementation that produces
its evidence exists.

Use separate fail-closed Vitest configurations for unit, reference, and integration
tests. Phase 0 CI runs only the active unit and browser suites. The reference suite
becomes mandatory when Phase 1 introduces the first production/reference comparison,
and the integration suite becomes mandatory when Phase 4 introduces the first
API/persistence integration test. Before activation, invoking either empty suite exits
non-zero, and no placeholder test stands in for scientific or MySQL evidence. The
reference producer is a non-npm Python/Astropy tool with a neutral versioned JSON
fixture envelope. It never imports production astronomy; comparison code under
`tests/reference` imports `astronomy-core`.

## Consequences

- Results are defensible and traceable to distinct claims.
- Runnable synthetic evidence remains visibly separate from source authority,
  production approval, and later scientific acceptance.
- CI/local environments need real MySQL and pinned browsers; astronomy fixture generation may use a separate approved Python/Astropy environment outside production.
- Visual/performance baselines require frozen environment metadata and reviewed updates.
- Human evaluation cannot start before ethics/privacy/protocol approval.

## Alternatives rejected

- Runtime-vs-copy-of-runtime formula comparison.
- SQLite for transaction/locking evidence.
- Single-browser manual testing.
- Automated accessibility scan as a full conformance claim.
- Mastery threshold or SUS as evidence of mathematical/learning correctness.

## Validation

An independent reviewer can reproduce the data hash, reference error table, BKT sequences, concurrency results, critical browser journey, performance run, accessibility/security checklists, and approved study analysis from recorded manifests.
