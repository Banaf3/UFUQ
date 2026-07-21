# Implementation status

**Assessment date:** 2026-07-22

The repository remains documentation-only. The reviewed stack, package layout,
dependency boundaries, server-authority model, and test approach are sufficient to
create empty packages and tooling. Scientific, cultural, learning-policy, participant,
privacy/security release, and deployment decisions are assessed at the gate they
actually affect.

## Independent readiness gates

| Gate | Result | Basis |
|---|---|---|
| Repository scaffolding | YES | The TypeScript monorepo, apps/packages/tools layout, React/R3F/Three.js web stack, Node/Express API, MySQL boundary, dependency rules, and provisional build/test tooling are sufficient to create empty packages and configuration. No unresolved value changes folder or package creation. |
| Validated celestial-guidance vertical slice | NO | The generic route/content model is settled, but the exact catalogue/subset, production astronomy pipeline/error budget, reviewed pattern/relationship content for one route, scenario, and scoring tolerances are unresolved. A replaceable astronomy/data spike may proceed first. |
| Participant study | NO | Participant protocol, ethics applicability/approval, instruments, recruitment, privacy, consent, data handling, and study-ready software remain unresolved or unimplemented. |
| Deployment | NO | Hosting/operations target, production account policy, security/privacy release profile, performance/accessibility baselines, monitoring, and backup/restore evidence remain unresolved or unimplemented. |

READY_FOR_SCAFFOLDING: YES

READY_FOR_VERTICAL_SLICE: NO

READY_FOR_PARTICIPANT_STUDY: NO

READY_FOR_DEPLOYMENT: NO

## Authorized next work

Phase 0 in `PHASES.md` may begin without astronomy values, Arabic cultural validation,
BKT calibration, participant ethics, production security, deployment decisions,
meeting schedules, reviewer-response dates, or personal weekly availability.

Phase 1 may then run a technical astronomy/data spike using synthetic or clearly
labelled candidate fixtures behind replaceable interfaces. It cannot promote candidate
values into learner-facing content or scientific evidence.

## Decisions that genuinely block the validated vertical slice

- **IMP-008 / AST-001:** exact catalogue source/version, permitted access/licence,
  required fields, subset, and quality rules.
- **IMP-009 / AST-003 and AST-006:** production coordinate/time pipeline,
  implement-or-omit effects, supported range, failure policy, independent oracle, error
  budget, and tolerances.
- **IMP-011 / AST-002:** approved `SkyPattern` and `GuidanceRelationship` records for
  one complete route to Al-Jady, including stable catalogue IDs, names/labels,
  membership, segments, instructional geometry/explanation, and review/verification
  status. The exact helper pattern and whether the first route uses Banat Na'sh or Dhat
  al-Kursi remain provisional.
- **IMP-012 / AST-007 and AST-006:** one sourced observer/time scenario, expected
  result, answer representation, and justified learner/scientific tolerance.

BKT parameters/cues do not block the Phase 2 minimal slice because adaptation begins in
Phase 3. Persistence, authentication, participant, privacy/security release, and
deployment decisions belong to Phases 4–6 and do not block Phases 0–2.

**IMP-018 is approved:** generic `SkyPattern`, `GuidanceRelationship`, and
`LessonRoute` schemas plus scenario-availability filtering can be scaffolded without
selecting any cultural record. This clarification does not change scaffolding readiness.

## Default implementation documents

1. `../AGENTS.md`
2. `IMPLEMENTATION_BRIEF.md`
3. `ARCHITECTURE.md`
4. `IMPLEMENTATION_DECISIONS.md`
5. `PHASES.md`
6. `TEST_PLAN.md`
7. `STATUS.md`

Technical domain specs and ADRs are loaded by phase. `governance/` is conditional
context and retains the complete independent review, original single-gate verdict,
report deviations, open decisions, research/release governance, risks, and
traceability.
