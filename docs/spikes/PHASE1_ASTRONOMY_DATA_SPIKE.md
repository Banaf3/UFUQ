# Phase 1 Milestone 1: source, policy, licensing, and performance audit

**Audit date:** 2026-07-26  
**Scope:** Decision audit only; no catalogue, astronomy, oracle-environment,
fixture, scene-coordinate, rendering, or performance implementation.

## Outcome

Milestone 1 is complete as an evidence audit. It does not approve a catalogue,
licence interpretation, numerical model, tolerance, performance protocol, or
primary device.

```text
CATALOGUE_SELECTION_PROPOSAL: I311
CATALOGUE_SELECTION_APPROVAL_REQUIRED: YES
I311_LOCAL_STRUCTURE: VERIFIED
I311_ACQUISITION_PROVENANCE: PARTIAL
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

No candidate manifest was created. The source is not approved, and the current
data-scaffold guard intentionally rejects a non-scaffold manifest. Changing
that implementation guard is outside this audit.

## 2. I/239 versus I/311

| Criterion | I/239 | I/311 | Evidence | Consequence |
|---|---|---|---|---|
| Catalogue identity and reduction | Original 1997 Hipparcos and Tycho catalogues, ESA SP-1200. | van Leeuwen's later new reduction of Hipparcos astrometry. | Official [I/239 ReadMe](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/I/239?format=html&tex=true), official [I/311 ReadMe](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/I/311?format=html&tex=true), and the tracked I/311/ESA studies. | They are distinct products; changing the identifier is not a clerical edit. |
| Local file availability | No raw I/239 catalogue is present in the approved local candidate location. | The four documented I/311 data files and its ReadMe are present locally. | Read-only local inventory. | I/311 has lower immediate acquisition effort, but presence is not approval. |
| Documentation studied | ESA Volume 1 field and astrometric-model sections have been studied. | The I/311 ReadMe, van Leeuwen validation material, and ESA comparison material have been studied. | Source dossiers and astronomy/catalogue syntheses. | Both have useful documentation; I/311-specific semantic gaps remain. |
| Astrometric fields | The main catalogue includes the five standard astrometric parameters plus errors, correlations, quality, and photometry. | Four solution-family files expose astrometry, solution metadata, errors/weights, quality fields, and photometry with different layouts. | Official catalogue ReadMes. | The parser and validation policy would differ materially. |
| Reference epoch | J1991.25 is explicitly tied to JD 2448349.0625 TT in the ESA guide. | The ReadMe labels coordinates with epoch `Ep=1991.25`; the exact time-scale interpretation is not explicit there. | ESA field-semantics dossier and I/311 ReadMe. | I/311 propagation must not silently inherit the full I/239 epoch statement. |
| Proper-motion documentation | `mu_alpha*cos(delta)` is explicit for the right-ascension component. | `pmRA` is labelled in mas/yr, but the I/311 ReadMe does not explicitly state the cosine factor. | ESA guide versus I/311-specific ReadMe and pmRA study. | I/311 remains `STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED`; normalized naming and a high-declination test are required. |
| Acquisition provenance | No local raw-byte acquisition chain exists. | File structure and local hashes are known, but the download chain and authoritative expected hashes are incomplete. | Local inventory and this audit. | Neither candidate currently has complete acquisition evidence. |
| Licensing or redistribution | ESA identifies the original 1997 catalogue under CC BY-NC 3.0 IGO with required ESA credit. | VizieR permits scientific use, but the I/311 ReadMe gives no clear catalogue-specific redistribution or deployment grant. | [ESA catalogue page](https://www.cosmos.esa.int/web/hipparcos/catalogues), [CC BY-NC 3.0 IGO](https://creativecommons.org/licenses/by-nc/3.0/igo/legalcode.en), [VizieR rules of use](https://cds.unistra.fr/vizier-org/licences_vizier.html), and I/311 ReadMe. | The ESA licence must not be transferred to I/311 by inference; I/311 redistribution remains unresolved. |
| Parser impact | A large fixed-width main file plus numerous annexes and companion files. | Four fixed-width solution-family files require an explicit inclusion and merge policy. | Official ReadMes. | Catalogue selection determines parser scope and malformed-input cases. |
| Reference-oracle impact | Explicit epoch and `mu_alpha_star` semantics reduce configuration ambiguity. | The oracle needs an approved mapping for I/311 epoch, solution family, and `pmRA`. | Astronomy synthesis and study dossiers. | Synthetic oracle work can remain independent; source-derived comparisons cannot. |
| Migration or rework | Selecting it reverses current I/311 preparation and requires acquisition/study work. | Selecting it contradicts older candidate-I/239 project documents but reuses current local preparation. | Project decision documents and tracked studies. | I/311 is the lower-rework candidate, but approval and synchronization are mandatory. |

### Catalogue proposal

```text
CATALOGUE_SELECTION_PROPOSAL: I311
CATALOGUE_SELECTION_APPROVAL_REQUIRED: YES
```

`I311` is a `CANDIDATE_PROPOSAL`, based on the available new-reduction files,
current source study, and reduced rework. It is not approved. Approval is
blocked by incomplete acquisition provenance, unresolved redistribution terms,
and unapproved field, solution, quality, and subset policies.

After approval, the selected identifier and policy must be synchronized in:

- `docs/ASTRONOMY_SPEC.md`
- `docs/DATA_STRATEGY.md`
- `docs/IMPLEMENTATION_DECISIONS.md` (`IMP-008`)
- `docs/governance/OPEN_QUESTIONS.md` (`AST-001`)
- `docs/adr/004-star-catalogue-and-provenance.md`
- `docs/references/PHASE_SOURCE_MATRIX.md`
- `docs/references/SOURCE_GAPS.md`
- `docs/STATUS.md`
- this spike record

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
| P1-D01 | Catalogue selection | I/239 is the older documented project candidate; I/311 is the prepared new-reduction candidate. | `CANDIDATE_PROPOSAL`: I/311; approval required | Catalogue and licensing approval | All source-derived work |
| P1-D02 | Parser fields | Each ReadMe defines many fields, but UFUQ's retained set is unapproved. | `NEW_PROJECT_DECISION_REQUIRED` | Use-case-to-field review and schema proposal | Parser/schema |
| P1-D03 | Solution-type policy | I/311 separates five-, seven-, nine-parameter, and variability-induced-mover solutions. | `NEW_PROJECT_DECISION_REQUIRED` | Scientific inclusion/exclusion rationale | Parser/subset |
| P1-D04 | Quality filtering | Source quality and uncertainty fields exist; no UFUQ rule is approved. | `NEW_PROJECT_DECISION_REQUIRED` | Distribution audit and science rationale | Runtime subset |
| P1-D05 | Subset selection | “Small catalogue subset” is approved only as spike scope; no predicate is approved. | `NEW_PROJECT_DECISION_REQUIRED` | Reproducible candidate comparison | Artifact/performance |
| P1-D06 | I/311 `pmRA` interpretation | Original ESA semantics explicitly use `mu_alpha_star`; I/311 says only `pmRA`. | `EXPERIMENT_REQUIRED` | I/311-specific confirmation plus omitted/double-cosine and high-declination cases | Proper-motion propagation |
| P1-D07 | Source epoch | I/311 says `Ep=1991.25`; original ESA gives J1991.25(TT) for I/239. | `EXPERIMENT_REQUIRED` | Confirm I/311 time-scale semantics and Astropy configuration | Propagation |
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

The independence boundary exists, but the environment and package set remain
unapproved and compatibility is untested.

`STAGE2_READY_FOR_SYNTHETIC_ORACLE_SMOKE_TEST: NO`

### Source-derived work readiness

Source-derived work requires:

- approved catalogue selection;
- confirmed authority for local processing;
- a source acquisition record with identity and approved hashes;
- approved parser fields, solution families, quality rules, and subset;
- approved raw-versus-derived tracking and redistribution policy; and
- enforcement that no generated subset bypasses unresolved rights.

Those conditions are not met.

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
| Official-source licensing/release check | PASS as an audit: I/239/I/311 identities, ESA's original-catalogue licence, VizieR scientific-use rule, and candidate release existence were checked. I/311 redistribution remains unresolved rather than being inferred. |
| Tracked restricted/raw/generated/secret scan | PASS: no tracked PDF, `local-reference` file, raw catalogue byte, generated catalogue artifact, secret environment file, build/compiler output, or high-confidence secret candidate. |
| Ignore checks | PASS: representative local PDF, I/311 raw file, `*.tsbuildinfo`, and web `dist` output resolve to ignore rules. |
| Python-environment check | PASS: no root/oracle `.venv` or `uv.lock` exists; the existing empty oracle scaffold was unchanged. |
| `git diff --check` | PASS. |

No application, package, API, tool, astronomy, catalogue, rendering, UI,
dependency, or lockfile changed. No raw/derived catalogue row or generated
artifact was created or tracked. Nothing is staged.

## 12. Audit risk summary

- **Blocking:** catalogue approval, I/311 redistribution and source-derived
  tracking authority, parser scope, time/EOP/refraction policies, and measured
  numerical tolerance.
- **Major:** acquisition provenance is only partial; I/311 `pmRA` and epoch
  semantics require explicit confirmation; performance thresholds lack an
  approved protocol.
- **Minor:** a candidate manifest is deliberately deferred until the source is
  approved and the scaffold guard is intentionally changed in its own stage.
- **Optional:** none added; this audit does not redesign the repository.

Milestone 2 and all implementation work remain unstarted.
