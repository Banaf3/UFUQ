# Reference-test boundary

The reference suite intentionally has no astronomy or BKT case in Phase 0. Its
dedicated configuration discovers `tests/reference/**/*.test.ts`, fails if invoked
empty, and is omitted from Phase 0 CI. It becomes mandatory in Phase 1 with the first
scientific comparison.

Independent astronomy fixtures use the versioned envelope under
`tools/astronomy-reference/fixtures/`. The Python/Astropy tool produces fixtures
without importing production code; comparison tests here may import
`@ufuq/astronomy-core`. No fixture case exists yet.
