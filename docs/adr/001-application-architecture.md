# ADR-001: TypeScript modular-monolith application architecture

- **Status:** Independently reviewed; awaiting owner approval
- **Classification:** CLARIFIED
- **Date:** 2026-07-20

## Context

The report requires a browser 3D application, React/Three.js, a Node/Express or directly comparable backend, MySQL, adaptive BKT, and learner/admin workflows. The system needs independently testable astronomy/learning calculations and atomic attempt/mastery persistence, but its FYP scale does not justify distributed services.

## Decision

Use a TypeScript monorepo containing one React web application, one Express-compatible API modular monolith, and framework-free packages for astronomy, assessment, BKT, adaptive policy, contracts, and catalogue schema. Deploy one stateless API process behind same-origin HTTPS with private MySQL/InnoDB initially, subject to DEP-001/SYS-001.

Dependencies point inward: API application use cases define outbound ports; HTTP,
MySQL, session, and logging adapters implement them and are wired only by the
composition root. Pure domains never import application, framework, rendering,
database, HTTP, DOM, or Node I/O code. The browser imports contracts and
presentation-safe astronomy but not authoritative scorer/target/tolerance entry points.
The API is authoritative for immutable scenario snapshots, scoring, typed model
decisions, mastery revisions, and scaffold transitions.

## Consequences

- Formula and policy tests remain fast and deterministic.
- One database transaction can protect each assessment transition.
- Package/public-contract discipline is required; the monorepo is not permission for cross-imports.
- A single service is easier to deploy and explain; horizontal scaling remains possible because truth is not stored in API memory.

## Alternatives rejected

- Microservices/event broker: operational and consistency cost without measured benefit.
- Browser-only backend/mastery: tamperable and unreliable across retries.
- Framework classes inside domain packages: compromises independent validation.
- External planetarium/native client: contradicts approved scope.

## Validation

Enforce import rules/TypeScript references, unit-test pure packages without browser/database, run contract/API tests, and demonstrate the Phase 1 vertical slice. Any future service split needs a new ADR and measured bottleneck.
