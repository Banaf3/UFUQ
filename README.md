# UFUQ

UFUQ is a planned browser-based 3D celestial simulator and intelligent tutoring system
for learning how to identify Banat Na'sh and Dhat al-Kursi, locate Al-Jady/Polaris,
estimate True North, and derive the Qibla direction.

## Current status

The architecture review is complete and preserved under
[`docs/governance/`](docs/governance/README.md). The active workflow now uses four
independent readiness gates:

- repository scaffolding: **ready**;
- validated celestial-guidance vertical slice: **not ready**;
- participant study: **not ready**;
- deployment: **not ready**.

See [Status](docs/STATUS.md) for the exact gate declarations and blockers. No application
code, package manifest, or database migration exists yet.

## Default implementation path

Codex and contributors should start with:

1. `AGENTS.md`
2. [Implementation Brief](docs/IMPLEMENTATION_BRIEF.md)
3. [Architecture](docs/ARCHITECTURE.md)
4. [Implementation Decisions](docs/IMPLEMENTATION_DECISIONS.md)
5. [Phases](docs/PHASES.md)
6. [Test Plan](docs/TEST_PLAN.md)
7. [Status](docs/STATUS.md)

Domain specifications and ADRs are read only when the active phase needs them. Detailed
review, report, decision, participant, privacy/release, deployment, risk, and thesis
traceability material is conditional context in `docs/governance/`.

## Architecture at a glance

The implementation baseline is a TypeScript modular monorepo: a React/React Three Fiber
browser application, a Node/Express API, MySQL/InnoDB persistence, pure framework-free
astronomy/assessment/BKT/adaptive-policy packages, versioned contracts, and a
reproducible small-catalogue pipeline. The server owns scenario validity, scoring,
mastery transitions, and scaffold decisions. The browser submits raw evidence.

Phase 0 creates only the repository layout and tooling. Phase 1 is a replaceable
astronomy/data technical spike. Scientific or cultural values are not guessed merely to
start implementation.

Lesson content is data-driven rather than fixed to Banat Na'sh. Versioned sky patterns,
guidance relationships, and lesson routes can represent reviewed helper-pattern paths,
Banat Na'sh or Dhat al-Kursi paths to Al-Jady, and the subsequent True North and Qibla
steps. Exact helper patterns and cultural mappings remain provisional.

## Restricted report

`local-reference/CB23011_FYP_REPORTv2.pdf` is a restricted local reference. The entire
`local-reference/` directory is ignored by Git. Do not copy, commit, upload, quote, or
reproduce the report in tracked content. Existing reviewed documentation contains only
approved paraphrased requirements.
