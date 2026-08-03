# Astronomy reference dependency contract

This tool is an independent Python process and is not an npm workspace. It must not
import, invoke, translate, or share implementation code with `astronomy-core` or any
other production package.

Phase 1 Milestone 2A uses exact CPython 3.14.6 and uv 0.11.32. `pyproject.toml`
expresses supported compatibility ranges; `uv.lock` records exact releases and artifact
hashes. Astropy and `astropy-iers-data` are direct dependencies because the oracle
imports both. NumPy and PyERFA remain transitive because UFUQ does not import them
directly; their exact locked versions are still recorded in
`environment-manifest.json`.

This milestone accepts only the versioned synthetic input contract and emits only the
versioned synthetic output envelope. It blocks network connections, disables Astropy
automatic downloads, uses an isolated temporary cache, and explicitly loads packaged
IERS/leap-second files. It must not read catalogue paths or identifiers.

Milestone 2C.5A adds declarative experiment registry/fixture/result schemas only; the
current executable still accepts and emits only the smoke contracts above. A future
2C.5B direct PyERFA experiment runner must first make PyERFA a direct dependency and
update this contract, lock/environment evidence, prohibited-import audit, and tests.
The currently pinned transitive installation is not implicit permission to import it.

Comparison code belongs in `tests/reference`; production code must never import this
tool or its fixtures as runtime data. These smoke values establish no production
algorithm, date range, tolerance, or catalogue semantics.
