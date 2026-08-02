# Tool boundaries

- `catalogue` is the only npm tool workspace. Acquisition, transformation,
  validation, canonical serialization, and checksum behavior will be internal modules
  introduced during Phase 1; none exists yet.
- `astronomy-reference` is a separate non-npm Python/Astropy fixture-producer scaffold.
  It has no production-package dependency or scientific behavior.

Runtime applications and packages never import tools.
