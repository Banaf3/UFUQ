# Governance and reviewed history

This directory preserves the detailed independent review, report relationship,
decision registers, prior phase/test plans, research governance, release governance,
risks, and traceability. Moving these files changed navigation, not their historical
finding or decision status.

They are deliberately outside the default implementation reading path. Read only the
relevant subset when working on formal scientific approval, cultural-content
validation, participant research, privacy/security release, deployment, or thesis
traceability. The active implementation workflow and current readiness gates live in
`../IMPLEMENTATION_BRIEF.md`, `../IMPLEMENTATION_DECISIONS.md`, `../PHASES.md`,
`../TEST_PLAN.md`, and `../STATUS.md`.

| File | Role |
|---|---|
| `ARCHITECTURE_REVIEW.md` | Historical adversarial review and original single-gate verdict |
| `OPEN_QUESTIONS.md` | Manual scientific, cultural, learning, research, security, deployment, and scope decisions |
| `REPORT_DEVIATIONS.md` | Proposed changes from the report baseline and their approval status |
| `PHASE0_DECISION_BOARD.md` | Detailed routing board created before the implementation-first refactor |
| `PRODUCT_SPEC.md` | Reviewed report-aligned product/research requirements |
| `EXECUTION_PLAN.md` | Prior risk-ordered, approval-heavy execution plan retained for history |
| `TEST_STRATEGY.md` | Detailed assurance and thesis-evidence strategy |
| `SECURITY_AND_PRIVACY.md` | Privacy, account, release-security, and research-data governance |
| `TRACEABILITY.md` | Report/requirement/code/test/evidence traceability baseline |
| `RISK_REGISTER.md` | Reviewed project, science, security, and research risks |
| `RESEARCH_NOTES.md` | Primary-source notes supporting the review |

The `READY_FOR_SCAFFOLDING: NO` line in `ARCHITECTURE_REVIEW.md` is retained as the
historical verdict of that review under its former all-in-one gate. It is not the active
readiness model. `../STATUS.md` independently assesses scaffolding, vertical slice,
participant study, and deployment.

## Legacy path map

Inline-code references inside preserved historical documents may name their location at
the time of review. Resolve these former repository paths as follows:

| Former path | Current path |
|---|---|
| `docs/ARCHITECTURE_REVIEW.md` | `docs/governance/ARCHITECTURE_REVIEW.md` |
| `docs/EXECUTION_PLAN.md` | `docs/governance/EXECUTION_PLAN.md` |
| `docs/OPEN_QUESTIONS.md` | `docs/governance/OPEN_QUESTIONS.md` |
| `docs/PHASE0_DECISION_BOARD.md` | `docs/governance/PHASE0_DECISION_BOARD.md` |
| `docs/PRODUCT_SPEC.md` | `docs/governance/PRODUCT_SPEC.md` |
| `docs/REPORT_DEVIATIONS.md` | `docs/governance/REPORT_DEVIATIONS.md` |
| `docs/RESEARCH_NOTES.md` | `docs/governance/RESEARCH_NOTES.md` |
| `docs/RISK_REGISTER.md` | `docs/governance/RISK_REGISTER.md` |
| `docs/SECURITY_AND_PRIVACY.md` | `docs/governance/SECURITY_AND_PRIVACY.md` |
| `docs/TEST_STRATEGY.md` | `docs/governance/TEST_STRATEGY.md` |
| `docs/TRACEABILITY.md` | `docs/governance/TRACEABILITY.md` |
