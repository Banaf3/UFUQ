# Phase 1 Milestone 1: source, policy, licensing, and performance audit

**Audit date:** 2026-07-26  
**Scope:** Decision audit only; no catalogue, astronomy, oracle-environment,
fixture, scene-coordinate, rendering, or performance implementation.

## Outcome

Milestone 1 is complete as an evidence audit. Its I/311 proposal was subsequently
approved by project decision for the bounded Phase 1 local technical spike. It does
not approve a licence interpretation, source-derived tracking, parser policy,
numerical model, tolerance, performance protocol, or primary device.

The status block below is the Milestone 1 snapshot. Milestone 2B subsequently resolved
the local parser/schema policies and I/311 `pmRA` semantics; current catalogue status
is in `PHASE1_CATALOGUE_AUTHORITY_PROVENANCE.md`.

```text
CATALOGUE_SELECTION: CDS_I311
CATALOGUE_SELECTION_STATUS: APPROVED_FOR_PHASE1_LOCAL_TECHNICAL_SPIKE
I239_ACTIVE_SUPPORT: NONE
I239_PARSER_PLANNED: NO
I239_FIXTURES_PLANNED: NO
I239_BENCHMARKS_PLANNED: NO
DUAL_CATALOGUE_SUPPORT_PLANNED: NO
I311_LOCAL_STRUCTURE: VERIFIED
I311_ACQUISITION_PROVENANCE: PARTIAL
I311_DERIVED_DATA_REDISTRIBUTION: UNRESOLVED
PMRA_SEMANTICS: STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED
ORACLE_VERSION_CANDIDATES_RECORDED: YES
ORACLE_COMPATIBILITY: UNTESTED
FRAME_RATE_REQUIREMENT_FOUND: YES
SELECTION_LATENCY_REQUIREMENT_FOUND: YES
PERFORMANCE_MEASUREMENT_PROTOCOL: UNRESOLVED
PRIMARY_DEVICE_CANDIDATE_RECORDED: YES
PRIMARY_DEVICE_APPROVED: NO
WEBGL_RENDERER_VERIFIED: NO
PERFORMANCE_SCALE_CANDIDATES_RECORDED: YES
EXPECTED_PRODUCT_SCALE: UNRESOLVED
STAGE2_READY_FOR_SYNTHETIC_ORACLE_SMOKE_TEST: NO
STAGE2_READY_FOR_SOURCE_DERIVED_WORK: NO
```

## Evidence classifications

This audit uses these meanings:

- `SOURCE_DEFINED`: stated by an identified primary source.
- `EXISTING_PROJECT_DECISION`: already approved in tracked project documents.
- `CANDIDATE_PROPOSAL`: a review candidate, not an approval.
- `NEW_PROJECT_DECISION_REQUIRED`: the project must choose before affected work.
- `EXPERIMENT_REQUIRED`: evidence must come from a bounded technical experiment.
- `LICENSING_REVIEW_REQUIRED`: access or reuse authority is not sufficiently clear.
- `UNRESOLVED_STOP_CONDITION`: affected implementation must not proceed.

The task prompt is scope authority, not evidence for a scientific, legal, or
performance conclusion.

## 1. Repository readiness

The pre-edit worktree was clean on branch
`spike/phase-01-astronomy-data`. The repository has exactly eight npm
workspaces:

1. `apps/web`
2. `apps/api`
3. `packages/astronomy-core`
4. `packages/assessment-core`
5. `packages/tutoring-core`
6. `packages/contracts`
7. `packages/catalogue-schema`
8. `tools/catalogue`

Relevant boundaries already exist:

- `astronomy-core` is the empty pure production astronomy boundary.
- `catalogue-schema` owns future framework-free catalogue and artifact schemas.
- `tools/catalogue` is the empty non-runtime catalogue-pipeline boundary.
- `tools/astronomy-reference` is a non-npm, behavior-free Python scaffold that
  must not import production UFUQ packages.
- `apps/web` is a health-only React/Vite scaffold with Three.js and React Three
  Fiber installed; it contains no celestial scene or performance collector.
- `data/raw/` is ignored, while tracked generated artifacts require approved
  provenance and licensing. The data-scaffold guard currently permits only the
  scaffold README in `data/manifests/`.

The architecture and boundary rules remain unchanged. Existing Phase 0 gates
cover formatting, linting, type checking, unit tests, package boundaries,
cycles, data scaffolding, builds, public exports, and a Playwright health smoke
test.

No candidate manifest was created. Although I/311 is now selected for the bounded local
spike, local-processing authority, field/filter scope, redistribution, and artifact
tracking remain unresolved, and the current data-scaffold guard intentionally rejects
a non-scaffold manifest. Changing that implementation guard is outside this audit.

## 2. Catalogue decision

CDS I/311, *Hipparcos, the New Reduction*, is the sole catalogue source for the
Phase 1 local technical spike. The project will not plan an alternate parser,
fixtures, benchmarks, migration code, or dual-catalogue abstraction. This is a
bounded `EXISTING_PROJECT_DECISION` based on the intentionally acquired local files,
completed source dossiers and field-semantics investigation, existing I/311-centred
preparation, and avoidance of an unnecessary second Hipparcos pipeline.

The source choice does not establish redistribution or deployment rights,
acquisition authenticity beyond the recorded partial provenance, final parser fields,
solution/quality filters, a subset, `pmRA` semantics, scientific correctness, or a
numerical tolerance. The original 1997 catalogue documentation remains supporting
scientific context only and cannot define later-reduction fields by inference.

## 3. Local I/311 structural verification

The ignored files were read without emitting catalogue rows.

| File | Bytes | Records/lines | Fixed-width result | SHA-256 |
|---|---:|---:|---|---|
| `ReadMe` | 10,375 | 200 lines | Not applicable | `6c017925d658447d40983da3b459ba16bf9789c8f7573e263952c75692622499` |
| `hip2.dat` | 32,673,535 | 117,955 | All 276 characters | `c45d6325bd59dd691764af173a9702e543804a2b6c1d9fea59210e8332e50a4a` |
| `hip7p.dat` | 173,940 | 1,338 | All 129 characters | `6928e0480d0f29620c0aef842ae71821d17d3a6a7a1ebe6b7f4ab86cc9838f20` |
| `hip9p.dat` | 28,600 | 104 | All 274 characters | `93d563896f37ae7cb422ebfe36bef4c91aa8f7c49f098ea12a811306bcc65dba` |
| `hipvim.dat` | 3,250 | 25 | All 129 characters | `9a564a255429c319af85cf23089eb31809ab291a0fcc1198c88796ff7a511baa` |

The data directory contains only those five expected entries. Counts and record
widths agree with the local and official I/311 ReadMe.

```text
I311_LOCAL_STRUCTURE: VERIFIED
I311_ACQUISITION_PROVENANCE: PARTIAL
```

`PARTIAL` means that the official catalogue identity and local structural
plausibility agree and the local bytes now have hashes. It does not mean that
the acquisition path is authenticated: the original per-file URLs, download
method, acquisition log, and authoritative expected hashes are not recorded.

## 4. Licensing audit

The official VizieR rules permit data retrieved through VizieR to be used
freely for scientific purposes, require citation of the original work, and
request VizieR acknowledgement. They also direct users to catalogue-specific
or publisher terms. The I/311 ReadMe supplies acknowledgements and publication
references but no explicit redistribution, republication, deployment, or
derived-subset grant.

| Use | Result | Basis |
|---|---|---|
| Public catalogue access | `LICENSING_CONFIRMED` | Official VizieR access and rules. |
| Local academic/scientific analysis | `LICENSING_CONFIRMED` | VizieR scientific-use rule, subject to source citation and any underlying rights. |
| Commit or republish raw I/311 bytes | `REDISTRIBUTION_UNRESOLVED` | No explicit I/311 redistribution permission found. |
| Commit a source-derived subset | `REDISTRIBUTION_UNRESOLVED` | Derivation and small size do not themselves grant republication rights. |
| Deploy source-derived records | `REDISTRIBUTION_UNRESOLVED` | Public download and non-commercial intent are not deployment permission. |
| Apply ESA's original-catalogue CC licence to I/311 | `USE_NOT_PERMITTED` as an inference | ESA explicitly labels the original 1997 catalogues; this audit found no basis to extend that licence to the later reduction. |

Overall result: `REDISTRIBUTION_UNRESOLVED`.

Clarification should be requested from CDS/VizieR
(`cds-question@unistra.fr`) and, as CDS directs, the I/311 data-origin rights
holder or publication rights holder. No contact was made. This is a project
licensing assessment, not legal advice.

## 5. Scientific decision register

Evidence anchors are the official catalogue ReadMes and the focused Hipparcos
studies for P1-D01 through P1-D07; `IMP-008`, `AST-001`, and
`docs/DATA_STRATEGY.md` for catalogue policy; `IMP-009`, `AST-003`,
`docs/ASTRONOMY_SPEC.md`, and ADR-003 for P1-D08 through P1-D16; and
`docs/TEST_PLAN.md`, ADR-007, and `AST-006` for P1-D17 through P1-D18.
`docs/references/SOURCE_GAPS.md` records the missing official
Astropy/IERS/environment and policy evidence. Lower-authority explanatory
material does not close those decisions.

| ID | Decision | Current evidence | Status | Next evidence | Blocks |
|---|---|---|---|---|---|
| P1-D01 | Catalogue selection | I/311 preparation and source study support one bounded local-spike source; a second Hipparcos pipeline has no demonstrated need. | `EXISTING_PROJECT_DECISION`: CDS I/311 only for Phase 1 local technical spike | New approval only if scope changes | None; separate source-derived gates below still block row processing |
| P1-D02 | Parser fields | Each ReadMe defines many fields, but UFUQ's retained set was unapproved at Milestone 1. | Historical `NEW_PROJECT_DECISION_REQUIRED`; resolved by Milestone 2B | See the Milestone 2B field contract | None for the local parser |
| P1-D03 | Solution-type policy | I/311 separates five-, seven-, nine-parameter, and variability-induced-mover solutions. | Historical `NEW_PROJECT_DECISION_REQUIRED`; fail-closed supplement/review policy defined by Milestone 2B | Inspect selected rows and obtain astronomy review | Scientific row approval |
| P1-D04 | Quality filtering | Source quality and uncertainty fields exist; no UFUQ rule was approved at Milestone 1. | Historical `NEW_PROJECT_DECISION_REQUIRED`; Milestone 2B preserves all evidence and prohibits silent filtering | Row-level science review | Learner-facing subset |
| P1-D05 | Subset selection | “Small catalogue subset” was approved only as spike scope at Milestone 1. | Historical `NEW_PROJECT_DECISION_REQUIRED`; exact 19-HIP technical candidate defined by Milestone 2B | Falak/cultural and scientific review | Final lesson allowlist |
| P1-D06 | I/311 `pmRA` interpretation | Milestone 1 had only original-catalogue support. I/311 Appendix G was subsequently located. | Historical `EXPERIMENT_REQUIRED`; `CONFIRMED_FOR_I311` by Milestone 2B | Keep omitted/double-cosine and high-declination astronomy tests | No longer blocks parser naming; propagation validation remains |
| P1-D07 | Source epoch | I/311 says `Ep=1991.25`; the original ESA catalogue gives J1991.25(TT), which cannot be transferred silently. | `EXPERIMENT_REQUIRED` | Confirm I/311 time-scale semantics and Astropy configuration | Propagation |
| P1-D08 | Production astronomy approach | Pure production boundary and independent oracle are approved; algorithm/library is not. | `NEW_PROJECT_DECISION_REQUIRED` and `EXPERIMENT_REQUIRED` | Candidate implementation comparison against independent fixtures | Astronomy implementation |
| P1-D09 | UTC/TT/UT1 handling | UTC is the external input; transformation/time-scale policy remains open. | `EXISTING_PROJECT_DECISION` for input; `NEW_PROJECT_DECISION_REQUIRED` internally | Explicit scale-conversion and Earth-rotation policy | Apparent/horizontal output |
| P1-D10 | Leap-second policy | No production policy is approved. | `NEW_PROJECT_DECISION_REQUIRED` | Official time-data source, stale-data behavior, and boundary tests | Supported time conversion |
| P1-D11 | Offline IERS policy | Reproducible offline behavior is required but unselected. | `NEW_PROJECT_DECISION_REQUIRED` | Pinned data/version/cache experiment and failure policy | Oracle fixtures and production parity |
| P1-D12 | Supported date range | No validated range exists. | `EXPERIMENT_REQUIRED` | Source-data coverage, error, and degradation measurements | Public date inputs |
| P1-D13 | Observer datum | Latitude/longitude/height are required; datum is unapproved. | `NEW_PROJECT_DECISION_REQUIRED` | Datum choice and conversion/input contract | Observer-dependent output |
| P1-D14 | Longitude convention | East-positive longitude is already specified. | `EXISTING_PROJECT_DECISION` | Contract and transformation tests later | Does not block Stage 2 |
| P1-D15 | Observer-height policy | Height is required but reference surface, units, range, and default are open. | `NEW_PROJECT_DECISION_REQUIRED` | Datum/height contract and sensitivity check | Observer-dependent output |
| P1-D16 | Geometric versus refracted output | Refraction must be explicit; implement/omit and atmospheric inputs are open. | `NEW_PROJECT_DECISION_REQUIRED` and `EXPERIMENT_REQUIRED` | Compare geometric and candidate refracted behavior | Visibility/lesson claims |
| P1-D17 | Fixture tracking | Oracle independence and a versioned envelope are approved; source-derived tracking depends on rights. | `EXISTING_PROJECT_DECISION` plus `LICENSING_REVIEW_REQUIRED` | Synthetic fixture policy, then source-derived permission | Scientific evidence |
| P1-D18 | Numerical tolerance | No tolerance has been measured or approved. | `EXPERIMENT_REQUIRED` | Error-budget decomposition and measured comparison distribution | Pass/fail science claims |

## 6. Independent-oracle environment candidates

Existence, Python requirement, and declared licence metadata were checked on
official project/PyPI records. No package was installed and no compatibility
claim was made.

| Candidate | Release observed | Declared Python support | Declared licence | Status |
|---|---|---|---|---|
| [Python](https://www.python.org/downloads/release/python-31314/) | 3.13.14 | Python 3.13 maintenance release | [PSF License v2](https://docs.python.org/3.13/license.html) | `CANDIDATE_PROPOSAL` |
| [uv](https://pypi.org/project/uv/0.11.32/) | 0.11.32 | Python >=3.8 | MIT OR Apache-2.0 | `CANDIDATE_PROPOSAL` |
| [Astropy](https://pypi.org/project/astropy/7.2.2/) | 7.2.2 | Python >=3.11 | BSD-3-Clause | `CANDIDATE_PROPOSAL` |
| [PyERFA](https://pypi.org/project/pyerfa/2.0.1.5/) | 2.0.1.5 | Python >=3.9 | BSD-3-Clause | `CANDIDATE_PROPOSAL` |
| [NumPy](https://pypi.org/project/numpy/2.4.6/) | 2.4.6 | Python >=3.11 | Multiple declared open-source licences | `CANDIDATE_PROPOSAL` |
| [astropy-iers-data](https://pypi.org/project/astropy-iers-data/0.2026.5.11.1.8.52/) | 0.2026.5.11.1.8.52 | Python >=3.10 | BSD-3-Clause | `CANDIDATE_PROPOSAL` |

These releases were recorded to make a bounded lock experiment possible, not
because newest releases are automatically suitable. Stage 2 must select and
test one complete set, produce a lockfile, verify licences, and exercise
offline/cache isolation.

```text
ORACLE_VERSION_CANDIDATES_RECORDED: YES
ORACLE_COMPATIBILITY: UNTESTED
```

## 7. Performance-requirement audit

| Requirement | Location | Concise requirement | Status | Measurement definition |
|---|---|---|---|---|
| Frame rate | `docs/governance/PRODUCT_SPEC.md`, NFR-01; traced to FYP report §3.3.4 NFR-1 by `docs/governance/TRACEABILITY.md` | Maintain at least 30 FPS. | Mandatory existing requirement | Unresolved: sampling window, percentile/minimum interpretation, warm-up, repetitions, and failure rule are not defined. |
| Selection/raycast latency | `docs/governance/PRODUCT_SPEC.md`, NFR-01; traceability as above | Raycast under 100 ms. | Mandatory existing requirement | Unresolved: computation versus input-to-visible-feedback interval and median/p95/maximum are not defined. |
| Smoothness | Product NFR-01 and `docs/governance/TEST_STRATEGY.md`, performance row | Interactive behavior and long-frame evidence are expected. | Preferred qualitative outcome; no separate threshold found | Unresolved. |
| Target device/OS/GPU/browser | `docs/governance/OPEN_QUESTIONS.md`, PERF-001 | A representative environment must be approved. | Proposed measurement input | Unresolved. |
| Viewport/resolution/DPR | `docs/governance/OPEN_QUESTIONS.md`, PERF-001 | Reproducible display conditions must be recorded. | Proposed measurement input | Unresolved. |
| Representative star-field size | `docs/governance/PRODUCT_SPEC.md` says a small subset; PERF-001 requires representative load | A reproducible representative catalogue/scene is needed. | Proposed; no approved count | Unresolved. |

```text
FRAME_RATE_REQUIREMENT_FOUND: YES
SELECTION_LATENCY_REQUIREMENT_FOUND: YES
PERFORMANCE_MEASUREMENT_PROTOCOL: UNRESOLVED
```

The 30 FPS requirement is not interpreted here as an average, percentile, or
permanent lower bound. The 100 ms requirement is not interpreted here as
computation-only or visible-feedback latency.

## 8. Primary-device candidate

Read-only operating-system inventory produced this candidate:

| Item | Observed value | Evidence boundary |
|---|---|---|
| Manufacturer/model | Lenovo 83GS | Windows hardware inventory |
| CPU | 12th Gen Intel Core i5-12450HX; 12 logical processors | Windows hardware inventory |
| Installed RAM | 29,758,447,616 bytes (about 27.7 GiB) | Windows hardware inventory |
| Integrated GPU | Intel UHD Graphics, driver 32.0.101.7026 | Installed adapter only |
| Discrete GPU | NVIDIA GeForce RTX 3050 6GB Laptop GPU, driver 32.0.15.9579 | Installed adapter only |
| Operating system | Windows 11 Home Single Language, build 26200.8875, reported 25H2 | CIM and registry; a legacy registry product-name string says Windows 10 |
| Active display reported by integrated adapter | 1920×1080 at 144 Hz | OS inventory, not browser canvas evidence |
| Installed Chrome | 150.0.7871.182 | Installed binary version |
| Installed Edge | 150.0.4078.83 | Installed binary version |

No evidence establishes which GPU Chrome uses.

A later headed-browser capture must record the actual WebGL renderer,
hardware-acceleration status, viewport, canvas dimensions, device-pixel ratio,
browser zoom, power state, Git commit, and production/development build mode.

```text
PRIMARY_DEVICE_CANDIDATE_RECORDED: YES
PRIMARY_DEVICE_APPROVED: NO
WEBGL_RENDERER_VERIFIED: NO
```

## 9. Candidate performance scale tiers

Aggregate-only inspection of the local `hip2.dat` candidate produced the
following reproducible counts. No row or coordinate was emitted.

Common candidate predicate: solution number `Sn` is exactly 5, component count
`Nc` is exactly 1, and `Hpmag` is finite. Requiring finite `RArad`, `DErad`,
`Plx`, `pmRA`, and `pmDE` did not change these counts.

| Candidate tier | Additional predicate | Aggregate count |
|---|---|---:|
| Bright | `Hpmag <= 6` | 3,329 |
| Medium | `Hpmag <= 7` | 10,891 |
| Large | `Hpmag <= 8` | 31,132 |

The source is the ignored local `hip2.dat` with SHA-256
`c45d6325bd59dd691764af173a9702e543804a2b6c1d9fea59210e8332e50a4a`.
The counts are reproducible for that byte sequence.

All three tiers are `CANDIDATE_PROPOSAL`. Hipparcos magnitude is not an
approved product-selection rule, a Johnson V substitute, or a complete
visibility model. The solution, quality, uncertainty, cultural-content, and
scenario policies remain unresolved.

```text
PERFORMANCE_SCALE_CANDIDATES_RECORDED: YES
EXPECTED_PRODUCT_SCALE: UNRESOLVED
```

## 10. Stage 2 entry criteria

### Synthetic oracle readiness

The synthetic smoke test may proceed without catalogue redistribution
permission only after:

- an environment manager and complete candidate package set are approved for
  lock testing;
- the offline/cache-isolation objective and acceptance check are explicit;
- the oracle remains independent from all production UFUQ packages; and
- inputs and expected output contain no catalogue-derived value.

The independence boundary exists. Section 14 records the subsequently approved modern
candidate evaluation and completed synthetic-only smoke milestone.

`STAGE2_READY_FOR_SYNTHETIC_ORACLE_SMOKE_TEST: YES`

### Source-derived work readiness

Source-derived work requires:

- approved catalogue selection (`CDS_I311`) — met;
- confirmed authority for local processing;
- a source acquisition record with identity and approved hashes;
- approved parser fields, solution families, quality rules, and subset;
- approved raw-versus-derived tracking and redistribution policy; and
- enforcement that no generated subset bypasses unresolved rights.

The source-selection condition is met; the remaining conditions are not.

`STAGE2_READY_FOR_SOURCE_DERIVED_WORK: NO`

## 11. Validation evidence

Validation is recorded after the documentation edit. No dependency
installation is required because dependency files are unchanged and the
existing installation is valid.

| Command/check | Result |
|---|---|
| `npm.cmd run check` | PASS: Prettier, ESLint, TypeScript, the eight-workspace boundary/acyclic/private-import/oracle check, and the data-scaffold guard passed. |
| `npm.cmd run test` | PASS: one unit file and one test passed. |
| `npm.cmd run cycles` | PASS: eight workspaces; graph acyclic; private imports absent; oracle independent. |
| `npm.cmd run exports:check` | PASS: 13 public exports resolved across seven importable workspaces. |
| `npm.cmd run build` | PASS: TypeScript build and web production build completed; Vite transformed 16 modules. |
| `npm.cmd run test:e2e` | PASS: the build repeated and one Chromium web/API health smoke test passed. |
| `PYTHONUTF8=1; python <skill-creator>/scripts/quick_validate.py <each .agents/skills directory>` | PASS: all five existing skills passed the repository's validator. This mechanical validation did not invoke the historical or Qibla workflows. |
| Targeted citation/source-location assertion | PASS: all 72 ESA printed-page tokens in the focused dossier have a maximum of 136 within its 586-page file; seven required project/source targets exist. Two initial assertion attempts used incorrect literal match tokens and were corrected; they did not identify a source or repository defect. |
| Mandatory-rule traceability assertion | PASS: engineering 9/9, astronomy 9/9, catalogue 8/8; all 18 audit decision rows contain an allowed evidence classification. An initial assertion matched an unrelated numbered authority list and was narrowed to the mandatory-workflow section. |
| Aggregate-only I/311 structure/checksum script | PASS: all four data-file counts and fixed widths agree with the ReadMe; no row was printed. |
| Aggregate-only candidate-tier script | PASS: 3,329, 10,891, and 31,132 records for the documented predicates and pinned local hash; no row was printed. |
| Read-only Windows CIM/registry/browser inventory | PASS: candidate device metadata recorded; no browser WebGL renderer was inferred. |
| Official-source licensing/release check | PASS as an audit: original- and new-reduction identities, ESA's original-catalogue licence, VizieR scientific-use rule, and I/311 release existence were checked. I/311 redistribution remains unresolved rather than being inferred. |
| Tracked restricted/raw/generated/secret scan | PASS: no tracked PDF, `local-reference` file, raw catalogue byte, generated catalogue artifact, secret environment file, build/compiler output, or high-confidence secret candidate. |
| Ignore checks | PASS: representative local PDF, I/311 raw file, `*.tsbuildinfo`, and web `dist` output resolve to ignore rules. |
| Python-environment check | PASS: no root/oracle `.venv` or `uv.lock` exists; the existing empty oracle scaffold was unchanged. |
| `git diff --check` | PASS. |

No application, package, API, tool, astronomy, catalogue, rendering, UI,
dependency, or lockfile changed. No raw/derived catalogue row or generated
artifact was created or tracked. Nothing is staged.

## 12. Audit risk summary

- **Blocking at Milestone 1:** I/311 local-processing authority, redistribution and source-derived
  tracking policy, parser scope, time/EOP/refraction policies, and measured numerical
  tolerance. Catalogue selection itself is resolved for the bounded local spike.
- **Major at Milestone 1:** acquisition provenance is only partial; I/311 `pmRA` and epoch
  semantics require explicit confirmation; performance thresholds lack an
  approved protocol.
- **Minor:** a candidate manifest is deliberately deferred until I/311 local-processing
  authority and manifest scope are approved and the scaffold guard is intentionally
  changed in its own stage.
- **Optional:** none added; this audit does not redesign the repository.

Milestone 2 and all implementation work remain unstarted.

## 13. Historical Milestone 2A lock attempt

**Attempt date:** 2026-07-26

**Claim:** Determine whether the approved exact candidate set can form a locked,
independent synthetic-only Astropy smoke environment.

**Gate:** Environment compatibility only; no scientific-model, tolerance, catalogue, or
production-implementation claim.

### Evidence classification

| Item | Classification | Evidence |
|---|---|---|
| Python 3.13.14 and uv 0.11.32 may be tested | `PROJECT_DECISION` limited to candidate lock testing | Milestone 2A authorization |
| Exact Astropy, PyERFA, NumPy, and IERS-data pins | `PROJECT_DECISION` limited to candidate lock testing | Milestone 2A authorization |
| uv 0.11.32 executed and selected CPython 3.13.14 | `SOURCE_SUPPORTED_FACT` | Exact command output below |
| Astropy 7.2.2 requires a newer IERS-data release than the approved pin | `SOURCE_SUPPORTED_FACT` | uv resolver metadata for Astropy 7.2.2 |
| A replacement version set | `UNRESOLVED_QUESTION` | Separate approval is required before another installation attempt |

### Exact candidate set requested

| Component | Requested exact candidate | Result |
|---|---|---|
| Python | 3.13.14 | Acquired in an isolated OS-temporary location and selected by the resolver |
| uv | 0.11.32 | Executed successfully |
| Astropy | 7.2.2 | Resolver inspected its dependency metadata; environment not resolved |
| PyERFA | 2.0.1.5 | Requested; no environment resolution completed |
| NumPy | 2.4.6 | Requested; no environment resolution completed |
| astropy-iers-data | 0.2026.5.11.1.8.52 | Conflicts with Astropy 7.2.2's declared minimum |

### Lock attempt and incompatibility

The existing global Python 3.13.7 and uv 0.11.15 were not treated as the oracle
environment. The installed uv was used only to acquire and execute exact uv 0.11.32 in
an isolated temporary cache. Exact uv 0.11.32 then acquired CPython 3.13.14 outside the
repository and attempted the project lock with `UV_PYTHON_PREFERENCE=only-managed`.

```powershell
$taskRoot = "C:\tmp\ufuq-oracle-m2a"
$env:UV_CACHE_DIR = Join-Path $taskRoot "uv-bootstrap-cache"
$env:UV_PYTHON_INSTALL_DIR = Join-Path $taskRoot "python"
$env:UV_PYTHON_PREFERENCE = "only-managed"
$bootstrapUv = (Get-Command uv).Source

& $bootstrapUv tool run --from "uv==0.11.32" uv --version
# uv 0.11.32 (3010295ae 2026-07-23 x86_64-pc-windows-msvc)

& $bootstrapUv tool run --from "uv==0.11.32" uv python install 3.13.14
# Installed Python 3.13.14

& $bootstrapUv tool run --from "uv==0.11.32" uv lock --python 3.13.14
# Using CPython 3.13.14
# No solution found:
# astropy==7.2.2 depends on astropy-iers-data>=0.2026.6.22.1.23.34
# but the project requires astropy-iers-data==0.2026.5.11.1.8.52
```

The last command exited 1. Therefore:

- no `uv.lock` was produced;
- no project `.venv` was created;
- no package set was installed or imported;
- there are no exact resolved runtime package versions beyond the verified uv and
  Python executables;
- compatibility, IERS isolation, synthetic execution, deterministic output, and
  independence could not be tested.

The attempted `.python-version`, dependency pins, and Python-ignore changes were
reverted so the repository does not retain an unsatisfiable environment declaration.
The existing behavior-free oracle scaffold is unchanged.

### Stop result

The approved exact set cannot produce a valid environment. Per the milestone stop
condition, no alternative version was installed and no oracle code, schema, synthetic
input, output fixture, test, environment manifest, IERS file record, or lockfile was
created.

The smallest candidate correction for a future approval is one of:

1. retain Astropy 7.2.2 and approve an exact `astropy-iers-data` release satisfying
   `>=0.2026.6.22.1.23.34`; or
2. retain `astropy-iers-data==0.2026.5.11.1.8.52` and separately identify an exact
   Astropy release whose official dependency metadata accepts it.

Neither alternative is selected here. The complete exact set must be approved before a
new lock attempt.

### Validation after the stop

| Exact command/check | Result |
|---|---|
| `uv tool run --from "uv==0.11.32" uv lock --python 3.13.14` | FAIL as the milestone result: exit 1 with the exact IERS-data constraint conflict above. |
| uv lock verification and locked synchronization | NOT RUN: no valid lock exists. |
| Python `unittest`, synthetic generation, two-run byte comparison, prohibited-import test, and IERS/network-isolation test | NOT RUN: creating code or claiming these checks after an unsatisfied environment would violate the stop condition. |
| `npm.cmd run check` | PASS: formatting, lint, TypeScript, boundaries, cycles, oracle boundary, and data scaffold. |
| `npm.cmd run test` | PASS: one test in one unit file. |
| `npm.cmd run cycles` | PASS: eight-workspace graph is acyclic and the behavior-free oracle boundary remains independent. |
| `npm.cmd run exports:check` | PASS: 13 exports across seven importable workspaces. |
| `npm.cmd run build` | PASS: TypeScript and Vite production builds completed. |
| `npm.cmd run test:e2e` | PASS: one Chromium web/API health smoke test. |
| `npm.cmd run test:reference` | Expected inactive-suite failure: exit 1 because no reference tests exist; no placeholder was added. |
| Tracked restricted/raw/generated/environment/binary/secret scan | PASS: none is tracked or staged. |
| Dependency and implementation diff scans | PASS: no npm manifest/lock, application, package, tool, test, script, renderer, scene, or catalogue source changed. |
| `git diff --check` | PASS after removing Markdown-only trailing-space line breaks. |

```text
OFFLINE_REPRODUCTION: OFFLINE_REPRODUCTION_FAILED
ORACLE_ENVIRONMENT_LOCKED: NO
ORACLE_COMPATIBILITY_VERIFIED: NO
ORACLE_INDEPENDENCE_VERIFIED: NO
IERS_NETWORK_ISOLATED: NO
SYNTHETIC_FIXTURES_DETERMINISTIC: NO
SOURCE_DERIVED_DATA_USED: NO
READY_FOR_CATALOGUE_MILESTONE: NO
```

Milestone 2A stopped at dependency resolution. Milestone 2B and all
catalogue/source-derived work remain unstarted.

## 14. Milestone 2A retry: modern locked synthetic-only oracle

**Retry date:** 2026-07-26

**Claim:** Verify one current, stable, mutually compatible Python/Astropy environment
and a reproducible synthetic-only oracle path. This is environment and independence
evidence. It does not validate a UFUQ production astronomy implementation, a source
catalogue, a numerical tolerance, or a final date-range/refraction policy.

### Why the candidate policy changed

The historical set in section 13 was unsatisfiable because Astropy 7.2.2 required
`astropy-iers-data>=0.2026.6.22.1.23.34`, while that experiment explicitly pinned
`0.2026.5.11.1.8.52`. Selecting only the oldest acceptable IERS-data release was
rejected for this retry: Earth-orientation and leap-second resources are
scientifically significant inputs, so UFUQ selected the current compatible stable
release and records its exact files and hashes. No package was downgraded to preserve
the failed set.

Official release metadata checked on 2026-07-26 gave:

| Component | Current stable evidence | Python/Windows evidence | Dependency role and selected constraint |
|---|---|---|---|
| Python | 3.14.6 from [python.org](https://www.python.org/downloads/release/python-3146/) | Current stable 3.14 line; Windows x86-64 installer published | Exact interpreter `3.14.6`; `requires-python = ">=3.14,<3.15"` |
| uv | 0.11.32 from [PyPI](https://pypi.org/project/uv/0.11.32/) and [Astral locked-mode documentation](https://docs.astral.sh/uv/concepts/projects/sync/#checking-the-lockfile) | `win_amd64` wheel published | External environment manager; exact 0.11.32 used |
| Astropy | 8.0.1 from [PyPI](https://pypi.org/project/astropy/8.0.1/) | Requires Python `>=3.11`; CPython stable-ABI Windows x86-64 wheel published | Direct import; `>=8.0.1,<9` |
| `astropy-iers-data` | 0.2026.7.20.15.31.18 from [PyPI](https://pypi.org/project/astropy-iers-data/0.2026.7.20.15.31.18/) | Requires Python `>=3.10`; universal wheel published | Direct science-data dependency; `>=0.2026.7.20.15.31.18,<0.2027` |
| NumPy | 2.5.1 from [PyPI](https://pypi.org/project/numpy/2.5.1/) | Requires Python `>=3.12`; CPython 3.14 Windows x86-64 wheel published | Transitive because UFUQ does not import `numpy` |
| PyERFA | 2.0.1.5 from [PyPI](https://pypi.org/project/pyerfa/2.0.1.5/) | Requires Python `>=3.9`; stable-ABI Windows x86-64 wheel published | Transitive because UFUQ does not import `erfa` |

Only Astropy and `astropy-iers-data` are direct project dependencies. Packaging,
PyYAML, NumPy, and PyERFA remain transitive and are still exact in the lock and
environment evidence. The selected direct ranges express supported compatibility;
`uv.lock` supplies exact releases and artifact hashes.

### Resolution, platform, and lock evidence

Exact uv 0.11.32 resolved one modern candidate set under exact CPython 3.14.6:

| Runtime package | Exact locked version | Kind |
|---|---|---|
| Astropy | 8.0.1 | Direct |
| `astropy-iers-data` | 0.2026.7.20.15.31.18 | Direct |
| NumPy | 2.5.1 | Transitive |
| packaging | 26.2 | Transitive |
| PyERFA | 2.0.1.5 | Transitive |
| PyYAML | 6.0.3 | Transitive |

The tested interpreter was CPython 3.14.6, MSC v.1944, 64-bit AMD64, on Windows 11
build 10.0.26200. `uv lock --check` succeeded and exact `uv sync --locked` installed
the six runtime packages. One sync invocation exceeded the command-observation timeout
while still running; it subsequently completed with the exact lock. This was a runner
timeout, not a resolver or compatibility failure.

### IERS and network evidence

The generator directly identifies the packaged inputs actually opened:

| Role | Package resource | SHA-256 | Observed packaged coverage |
|---|---|---|---|
| Earth orientation | `astropy_iers_data/data/finals2000A.all` | `d4bb5af084caf3e82621bc75aad902dc7ad9e38e785a97d3fcac0a23d89644fb` | MJD 41684-61610 (1973-01-02 to 2027-07-24); predictive data begins MJD 61238 (2026-07-17) |
| Leap seconds | `astropy_iers_data/data/Leap_Second.dat` | `6cb6f5d4b819f2e568e25db4b0b26d89dedf031fdffb18bc94d40f4e94e268d7` | Effective entries 1972-01-01 through 2017-01-01; last TAI-UTC 37 s; packaged expiry text says 28 June 2027 |

During each transform, Astropy automatic IERS download and general Astropy internet
access are disabled, degraded IERS accuracy is an error, a fresh temporary Astropy
cache is used, and standard-library socket/URL connection entry points fail closed.
The locked executions also used uv offline mode. No warning or degraded-accuracy result
was emitted for the two selected instants. These observations do not approve UFUQ's
final supported date range or long-term IERS refresh policy.

### Synthetic fixture and independence evidence

The input contains only three records labelled `SYNTHETIC_TEST_INPUT`:

1. an ordinary finite synthetic ICRS direction and observer;
2. a different synthetic declination, hemisphere, observer, and time; and
3. an invalid latitude that returns `INVALID_OBSERVER_LATITUDE`.

The two valid records use explicit ICRS degrees, a `J2000.0` metadata label with no
space-motion application, UTC instants, WGS84 geodetic observers, east-positive
longitude, ellipsoidal height, and zero pressure. Output is geometric topocentric
Astropy `AltAz`, in degrees, with north-zero azimuth increasing eastward. These are
Astropy smoke conventions, not a new production API or tolerance decision.

Canonical output is UTF-8, lexicographically key-sorted compact JSON with one LF,
CPython 3.14 shortest round-trip float text, and no current timestamp, duration,
username, absolute path, or locale-dependent field. Two separate locked offline
processes produced byte-identical output with SHA-256
`d1183fd6ff3d74603ff6b4c70809ef4d954fdb55a6ac8a3b62f2ee78f341da69`.

The Python source imports no UFUQ production package, reads no production expected
result, executes no Node code, and contains no permitted path to `data/raw`,
`node_modules`, or production `dist`. A focused AST/path test enforces these
prohibitions. The input/output checks reject catalogue identifiers and volatile
metadata. No source-derived data was read or emitted.

### Reproduction and maintenance

Initial acquisition required network access. Subsequent fixture generation and tests
ran with package-network access disabled. A fresh temporary virtual environment was
also reconstructed successfully using the exact lock, managed CPython 3.14.6, and
already populated local package caches. An empty-cache, no-network rebuild and a
committed wheelhouse were not tested.

`OFFLINE_REPRODUCTION: CACHE_DEPENDENT_OFFLINE_EXECUTION`

Ordinary builds and tests use `--locked --no-sync` and must not rewrite the lock.
Updates occur only at a Phase 1 milestone boundary or for a relevant security or
scientific fix, on a dedicated branch. The update must deliberately refresh the lock,
record old/new versions, rerun unit tests, regenerate and compare synthetic fixtures,
investigate every unexpected numerical/warning change, repeat offline and IERS
isolation checks, and receive review before acceptance. No update bot is introduced.

### Retry result and unresolved scope

Seven Python unittests passed: lock/environment metadata, valid transformation,
structured invalid input, deterministic bytes/hash, network/IERS fail-closed policy,
prohibited imports/paths, catalogue/volatile-data exclusion, and output-path
independence.

| Exact command/check | Result |
|---|---|
| exact uv 0.11.32 `lock --check --offline` | PASS; 7 project/runtime records resolved from the unchanged lock |
| exact uv 0.11.32 `sync --offline --locked --managed-python --python 3.14.6` | PASS; 6 locked runtime packages checked |
| locked offline `python -m unittest discover -s tests -v` | PASS; 7 tests |
| two separate locked offline `python run.py fixture` executions | PASS; byte equality true and both SHA-256 values equal `d1183fd6ff3d74603ff6b4c70809ef4d954fdb55a6ac8a3b62f2ee78f341da69` |
| fresh temporary `uv sync --offline --locked` using populated caches | PASS; exact CPython 3.14.6 and 6 runtime packages reconstructed |
| `npm.cmd run check` | PASS; format, lint, typecheck, boundaries, cycles, oracle independence, and data scaffold |
| `npm.cmd run test` | PASS; 1 TypeScript unit test |
| `npm.cmd run cycles` | PASS; 8 workspaces, acyclic, no private import, oracle independent |
| `npm.cmd run exports:check` | PASS; 13 public exports across 7 importable workspaces |
| `npm.cmd run build` | PASS; TypeScript and Vite production builds |
| `npm.cmd run test:e2e` | PASS; 1 Chromium web/API health smoke test |
| `npm.cmd run test:reference` | Expected fail-closed inactive-suite result; no production/reference comparison test exists and no placeholder was added |
| tracked PDF/raw/generated/secret/environment/binary and implementation-diff scans | PASS; only allowed raw/generated READMEs are tracked; no prohibited or staged item and no npm/production-source diff |
| `git diff --check` | PASS |

At completion of Milestone 2A, still unresolved were source-derived processing
authority and redistribution, catalogue fields/subset/quality, I/311 `pmRA`
confirmation, production astronomy
design, UTC/TT/UT1 and leap-second behavior, final offline-IERS/date-range policy,
refraction, observer-height handling, fixture tracking for source-derived cases, and a
measured numerical tolerance. This retry does not alter the approved I/311 selection
or authorize the catalogue milestone.

```text
CURRENT_STABLE_STACK_EVALUATED: YES
PYTHON_STABLE_LINE: 3.14.6
ASTROPY_STABLE_LINE: 8.0.1
ORACLE_ENVIRONMENT_LOCKED: YES
ORACLE_COMPATIBILITY_VERIFIED: YES
ORACLE_INDEPENDENCE_VERIFIED: YES
IERS_NETWORK_ISOLATED: YES
SYNTHETIC_FIXTURES_DETERMINISTIC: YES
DEPENDENCY_UPDATE_POLICY_DEFINED: YES
SOURCE_DERIVED_DATA_USED: NO
READY_FOR_CATALOGUE_MILESTONE: NO
```

At completion of Milestone 2A, Milestone 2B and every catalogue/source-derived,
production-astronomy, scene, rendering, and performance milestone remained unstarted.
Milestone 2B is now recorded separately; this historical result is not its current
gate.
