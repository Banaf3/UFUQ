# Astronomy reference dependency contract

This tool is an independent Python process and is not an npm workspace. It must not
import, invoke, translate, or share implementation code with `astronomy-core` or any
other production package.

Phase 1 will select and pin a supported Python version, Astropy, and any required
reference-data dependencies in an approved environment lock. They are deliberately not
selected or installed during this structural migration. Generated fixtures must record
the exact Python, Astropy, dependency, input-data, and generator versions used.

The tool may read approved independent inputs and emit only the versioned JSON fixture
envelope defined by `fixtures/astronomy-reference-fixture.v1.schema.json`. Comparison
code belongs in `tests/reference`; production code must never import this tool or its
fixtures as runtime data.
