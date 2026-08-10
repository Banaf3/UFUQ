# Independent synthetic astronomy reference tool

This non-npm Python tool contains the bounded Phase 1 environment/independence smoke
test and the Milestone 2C.5B synthetic-only Batch 01 runner. It contains no catalogue
row, production TypeScript astronomy, learner tolerance, cultural name, rendering
behavior, or application runtime dependency.

## Locked environment

- Exact Python: `3.14.6` in `.python-version`.
- Exact environment manager: uv `0.11.32`, enforced by
  `tool.uv.required-version`.
- Direct constraints: Astropy `>=8.0.1,<9`,
  `astropy-iers-data>=0.2026.7.20.15.31.18,<0.2027`, and PyERFA `2.0.1.5`.
- Exact direct and transitive resolutions and hashes: `uv.lock`.
- Runtime/package/platform/IERS evidence: `environment-manifest.json`.

The smoke oracle imports Astropy and `astropy_iers_data`. The Batch runner additionally
imports `erfa`, so PyERFA is a direct reference-tool dependency. NumPy remains
transitive and is not imported directly.

Install uv 0.11.32 through the approved developer/CI bootstrap, then run from this
directory:

```powershell
uv lock --check
uv sync --locked --managed-python
uv run --locked --no-sync python run.py environment
uv run --locked --no-sync python run.py fixture
uv run --locked --no-sync python run.py batch-01
uv run --locked --no-sync python run.py validate-batch-01
uv run --locked --no-sync python -m unittest discover -s tests -v
```

Ordinary execution must use `--locked --no-sync`; it may not rewrite `uv.lock`.
Synchronization uses `sync --locked`. Initial dependency acquisition may use the
network. Smoke execution uses Astropy's packaged data with automatic IERS downloads and
general Astropy internet access disabled, a fresh temporary cache, and socket
connections blocked.

## Milestone 2C.5A protocol and 2C.5B Batch 01

`experiments/experiment-registry.v1.json` is a declarative registry of the 24
Milestone 2C.1-2C.4 experiment records. Its registry, fixture, and result schemas freeze
input classification, comparison lineage, deterministic evidence, and acceptance
limits. Milestone 2C.5A added no execution.

Milestone 2C.5B implements and completes only the registry's 9/9 Batch 01 IDs/scopes. The runner
uses nine canonical synthetic fixtures and emits nine schema-validated canonical
results plus full-file SHA-256 companions. Every handler executes twice with fresh
cache isolation; the whole command is replayed in independent OS processes with
identical argv in the same pre-synchronized locked environment. This does not prove a
clean-environment dependency rebuild. Unknown or non-Batch IDs, altered fixture bytes
or partitions, source-like inputs, stale manifests, and unsupported schema keywords
fail closed. Numerical values are always
`MEASURED_NO_ACCEPTANCE`; only exact contract/status/determinism guards may pass or
fail.

The three epoch-label fixtures declare ITRS-geocentric Cartesian `[0,0,0]` metres and
pass that exact synthetic location to every affected Astropy `Time` constructor. It is
only the TT/TDB conversion reference location: no physical observer, datum/site,
topocentric geometry, production observer policy, or implicit location default follows.
All three cases explicitly initialize the pinned smoke-only leap artifact consumed by
that conversion, including isolated single-ID runs; this is not production leap-data
approval. The fixture schema and tests reject a missing or nonzero replacement, while each
result binds the canonical fixture hash and retains an explicit-location status.

Batch result JSON and `.sha256` companions are runner-owned evidence and must not be
hand-edited. Any fixture, schema, protocol, or runner-source hash change requires the
full nine-result runner regeneration and replay. The external replay uses independent
processes plus separate temporary cache/comparison directories in the same existing
locked environment; it is not a dependency rebuild. Componentized/composed output
remains same-family consistency, never independent scientific validation.

The local schema validator implements only the Draft 2020-12 keyword subset actually
used by the three experiment schemas, refuses non-local references and unsupported
keywords, and has negative/conditional tests. It is not a production runtime-validator
selection or a full meta-schema conformance claim.

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
