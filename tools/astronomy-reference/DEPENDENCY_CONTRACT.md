# Astronomy reference dependency contract

This tool is an independent Python process and is not an npm workspace. It must not
import, invoke, translate, or share implementation code with `astronomy-core` or any
other production package.

Phase 1 uses exact CPython 3.14.6 and uv 0.11.32. `pyproject.toml`
expresses supported compatibility ranges; `uv.lock` records exact releases and artifact
hashes. Astropy and `astropy-iers-data` are direct dependencies because the oracle
imports both. Milestone 2C.5B promotes the already locked PyERFA `2.0.1.5` release to a
direct dependency because the bounded Batch 01 runner imports `erfa`; its release and
artifact hashes do not change. NumPy remains transitive and is not directly imported.
All exact dependency kinds and versions remain recorded in `environment-manifest.json`.

This milestone accepts only the versioned synthetic input contract and emits only the
versioned synthetic output envelope. It blocks network connections, disables Astropy
automatic downloads, uses an isolated temporary cache, and explicitly loads packaged
IERS/leap-second files. It must not read catalogue paths or identifiers.

Milestone 2C.5B adds a second, fixed execution surface for exactly nine Batch 01
synthetic fixtures. It rejects arbitrary discovery, unknown/non-Batch IDs, scope
expansion, source-like input material, stale hashes, and noncanonical bytes. It uses a
fail-closed local validator for only the Draft 2020-12 keywords present in the committed
experiment schemas. That validator is runner source, not a selected third-party or
production runtime dependency, and it does not close the general `DATA-SRC-002`
validator decision.

The Batch runner may import `erfa` only from
`src/ufuq_astronomy_reference/batch01.py`. It may not import NumPy directly, any UFUQ
production package, catalogue tooling, or application code. Ordinary smoke and Batch
execution use the locked environment with no synchronization, automatic downloads,
network access, or cache discovery.

Comparison code belongs in `tests/reference`; production code must never import this
tool or its fixtures as runtime data. These smoke values establish no production
algorithm, date range, tolerance, or catalogue semantics.
