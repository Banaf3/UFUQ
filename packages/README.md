# Package boundaries

- `astronomy-core`: pure astronomy boundary; empty until Phase 1.
- `assessment-core`: pure scoring boundary; empty until validated science/task inputs exist.
- `tutoring-core`: pure logical `bkt`, `observations`, and `adaptive-policy` modules;
  no learner-model behavior exists yet and it does not depend on assessment scoring.
- `contracts`: versioned serialized DTOs and future framework-free validators only.
- `catalogue-schema`: logical `catalogue`, `content`, and `artifact` modules. The
  content module retains generic pattern/guidance/route type placeholders; no runtime
  validator or concrete content exists yet.

Applications depend only on the approved public package exports. Pure packages never
depend on applications, adapters, frameworks, persistence, browser APIs, Node I/O, or
tools.
