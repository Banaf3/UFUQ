# Reference-test boundary

The reference suite intentionally has no astronomy or BKT case in Phase 0. Its
dedicated configuration discovers `tests/reference/**/*.test.ts`, fails if invoked
empty, and is omitted from Phase 0 CI. It becomes mandatory in Phase 1 with the first
scientific comparison.

Independent astronomy fixtures use the versioned envelope under
`tools/astronomy-reference/fixtures/`. The Python/Astropy tool produces fixtures
without importing production code; comparison tests here may import
`@ufuq/astronomy-core`. No fixture case exists yet.

Milestone 2C.5A adds only declarative experiment records and schemas under the Python
tool. A later synthetic-only experiment runner still does not activate this suite. The
first test added here must be a genuine production/reference comparison with the
approved input policies, provenance, error-budget status, and no placeholder
acceptance threshold.
