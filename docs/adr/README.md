# Architecture decision records

ADRs record durable decisions and their report relationship. “Independently reviewed;
awaiting owner approval” means the review recommends the decision but the student and
supervisor have not approved implementation. Manual-domain blockers and proposed
deviations remain governed by `../governance/OPEN_QUESTIONS.md` and
`../governance/REPORT_DEVIATIONS.md`.

| ADR | Decision | Classification | Status |
|---|---|---|---|
| [001](001-application-architecture.md) | TypeScript modular monolith and pure domain boundaries | CLARIFIED | Independently reviewed; awaiting owner approval |
| [002](002-frontend-3d-integration.md) | React Three Fiber adapter over Three.js | CLARIFIED | Independently reviewed; awaiting owner approval |
| [003](003-astronomical-coordinate-conventions.md) | Explicit north/east/up and versioned astronomical policy | CONFIRMED/CLARIFIED; manual values | Blocked on AST-001/003–007 |
| [004](004-star-catalogue-and-provenance.md) | Reproducible catalogue/curation pipeline | CONFIRMED/CLARIFIED; manual source | Blocked on AST-001/002 |
| [005](005-bkt-runtime-boundary.md) | Pure BKT plus separate adaptive policy and independent evidence | CONFIRMED/CLARIFIED; deviations/manual policy | Blocked on DEV-004/006–008 and BKT-001–004 |
| [006](006-persistence-and-transactions.md) | InnoDB atomic, fingerprinted, revision-safe submission | CLARIFIED; storage/log deviations | Blocked on SYS-001 and DEV-002–005/014 |
| [007](007-testing-and-validation.md) | Layered independent validation and configured quality gates | CONFIRMED/CLARIFIED | Independently reviewed; tolerances/manual profiles pending |

When a decision is approved, add approver and date without erasing prior status. Replaced decisions get `Superseded by ADR-NNN`, not silent edits.
