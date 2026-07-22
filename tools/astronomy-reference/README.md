# Independent astronomy reference tool

This is a documentation-only Python/Astropy tool scaffold. It contains no astronomical
calculation, catalogue record, fixture case, or production-package dependency.

The Phase 1 technical spike may add a pinned Python environment and an independent
fixture producer under its own approved ExecPlan. The producer writes the neutral JSON
envelope defined in `fixtures/`; `tests/reference` owns comparison with
`@ufuq/astronomy-core`. The oracle must never import production astronomy code.
