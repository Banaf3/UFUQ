# ADR-007: Layered testing and independent validation

- **Status:** Independently reviewed; awaiting owner approval
- **Classification:** CONFIRMED/CLARIFIED; numerical tolerances remain MANUAL DOMAIN DECISION AST-006
- **Date:** 2026-07-20

## Context

UFUQ makes scientific, software, performance, usability, adaptive-model, and learning claims. Tests that reuse production formulas can reproduce the same bug; screenshots cannot prove coordinates; BKT arithmetic cannot prove learning; browser mocks cannot prove InnoDB atomicity.

## Decision

Adopt the layers and configured gates in `../TEST_STRATEGY.md`: pure-domain
units/properties; catalogue schemas; independently authored/reviewed pinned
Astropy/USNO/domain fixtures and error budgets; BKT oracles/sensitivity; real-SYS-001
MySQL API/transaction/concurrency tests; deterministic raycast and approved browser
E2E; focused scientific/scaffold visual regression; accessibility; performance;
security/privacy; backup/restore; evidence manifests; and a separately approved human
evaluation. Missing tolerances or baseline configuration fail rather than using invented
constants.

Keep reference fixture generation structurally independent from runtime TypeScript astronomy. Every fixture and result records software/data/policy/tolerance version. Missing tolerance fails validation. Coverage is diagnostic; pure decision/formula modules target complete branches but reference agreement is the correctness oracle.

## Consequences

- Results are defensible and traceable to distinct claims.
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
