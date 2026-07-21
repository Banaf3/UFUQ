# Package boundaries

- `astronomy-core`: pure astronomy boundary; empty until Phase 1.
- `assessment-core`: pure scoring boundary; empty until validated science/task inputs exist.
- `bkt-core`: pure learner-model boundary; no formulas or parameters yet.
- `adaptive-policy`: pure scaffold-policy boundary; no cues or transitions yet.
- `tutoring-core`: pure façade over assessment/BKT/policy boundaries; no behavior yet.
- `contracts`: shared application types only.
- `star-data`: type-only placeholders for generic patterns, guidance relationships, and routes.
- `catalogue-schema`: type-only schema boundary over `star-data`; runtime validation begins later.

Applications may depend on these packages. They never depend on either application.
