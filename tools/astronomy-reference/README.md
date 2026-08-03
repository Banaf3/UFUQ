# Independent synthetic astronomy reference tool

This non-npm Python tool is a bounded Phase 1 environment and independence smoke test.
It transforms at most two explicitly synthetic fixed ICRS directions to geometric
Astropy `AltAz` output and returns one structured invalid-input result. It contains no
catalogue row, production TypeScript astronomy, learner tolerance, cultural name,
rendering behavior, or runtime dependency.

## Locked environment

- Exact Python: `3.14.6` in `.python-version`.
- Exact environment manager: uv `0.11.32`, enforced by
  `tool.uv.required-version`.
- Direct compatibility ranges: Astropy `>=8.0.1,<9` and
  `astropy-iers-data>=0.2026.7.20.15.31.18,<0.2027`.
- Exact direct and transitive resolutions and hashes: `uv.lock`.
- Runtime/package/platform/IERS evidence: `environment-manifest.json`.

UFUQ imports Astropy and `astropy_iers_data` directly. NumPy and PyERFA remain
transitive because this tool does not import `numpy` or `erfa`; their exact locked
versions are still evidenced.

Install uv 0.11.32 through the approved developer/CI bootstrap, then run from this
directory:

```powershell
uv lock --check
uv sync --locked --managed-python
uv run --locked --no-sync python run.py environment
uv run --locked --no-sync python run.py fixture
uv run --locked --no-sync python -m unittest discover -s tests -v
```

Ordinary execution must use `--locked --no-sync`; it may not rewrite `uv.lock`.
Synchronization uses `sync --locked`. Initial dependency acquisition may use the
network. Smoke execution uses Astropy's packaged data with automatic IERS downloads and
general Astropy internet access disabled, a fresh temporary cache, and socket
connections blocked.

## Milestone 2C.5A experiment protocol

`experiments/experiment-registry.v1.json` is a declarative registry of the 24
Milestone 2C.1-2C.4 experiment records. Its registry, fixture, and result schemas freeze
input classification, comparison lineage, deterministic evidence, and acceptance
limits. They add no experiment runner, fixture instance, numerical result, source-
derived value, production code, or tolerance.

The current smoke tool still does not import PyERFA directly. Before a 2C.5B runner
uses direct `erfa` routines, that milestone must deliberately make PyERFA a direct
reference-tool dependency and update the dependency contract, lock evidence, import
audit, and tests. Its installed transitive version is already pinned, but transitive
availability alone is not the dependency policy.

Synthetic experiment execution in this tool does not activate `test:reference`.
That suite activates only when a comparison imports production astronomy and compares
it with the independent reference path.

## Canonical fixtures

`fixtures/synthetic-input.v1.json` is labelled `SYNTHETIC_TEST_INPUT` per case.
`fixtures/synthetic-output.v1.json` is canonical UTF-8 JSON with sorted keys, compact
separators, LF termination, no volatile execution metadata, and a separate SHA-256
file. Case hashes cover each valid case before its own hash field is added. Numeric
text uses the locked CPython 3.14 shortest round-trip representation; this is a
serialization rule, not a scientific tolerance.

The two valid cases use pressure zero, so the output is geometric/topocentric rather
than refracted. Astropy's documented convention is north-zero with azimuth increasing
eastward. This smoke use does not select the final UFUQ production pipeline, supported
date range, refraction policy, or numerical tolerance.

## Dependency maintenance

1. Do not update the lockfile during ordinary builds, tests, or fixture generation.
2. Review updates at a Phase 1 milestone boundary or for a relevant security/scientific
   fix.
3. Use a dedicated branch.
4. Deliberately refresh the lock with the approved uv release.
5. Record old/new Python, direct, transitive, and IERS-data versions.
6. Rerun the oracle unit tests.
7. Regenerate the synthetic fixtures.
8. Compare canonical bytes, hashes, and scientific values.
9. Investigate every unexpected numerical or warning change.
10. Rerun locked offline execution, cache isolation, and IERS/network checks.
11. Accept the update only after review.

No automatic update bot is introduced by this milestone.

## Independence

The tool imports no production UFUQ package, executes no Node astronomy code, and
accepts no production expected result. Automated tests inspect imports and paths.
`tests/reference` will later own comparisons with production astronomy; those
comparisons are outside this milestone.
