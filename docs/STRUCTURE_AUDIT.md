# UFUQ repository structure audit

**Audit date:** 2026-07-22  
**Scope:** Folder, workspace, dependency, build, test, data, and tooling structure only.  
**Method:** Independent read-only inspection followed by the creation of this report. No
feature, astronomy/data spike, file migration, or architecture correction was performed.

## Executive finding

The modular-monolith direction is appropriate, but the current physical structure is
not yet suitable for the astronomy/data technical spike. The problem is not a missing
enterprise layer. It is a combination of three Phase 1 blockers, unnecessary workspace
facades, and reproducibility hygiene that the current passing boundary check does not
detect.

The 13 workspaces should be reduced to nine before meaningful code accumulates:

- retain the two applications;
- retain `astronomy-core`, `assessment-core`, `contracts`, and a corrected
  `catalogue-schema`;
- make `tutoring-core` the one pure BKT/observation/adaptive-policy package;
- retain one genuinely independent astronomy-reference tool; and
- retain one catalogue CLI/pipeline tool.

This keeps the necessary scientific, server-authority, tutoring, contract, and offline
tool boundaries without maintaining a workspace for every small concept.

## 1. Current repository tree

The tree below represents the 126 tracked files at audit time. `node_modules`, ignored
runtime build directories, and the restricted `local-reference/` contents are omitted.
Tracked generated files are shown because their presence is a finding.

```text
UFUQ/
├── .agent/
│   └── PLANS.md
├── .github/workflows/
│   └── ci.yml
├── apps/
│   ├── api/
│   │   ├── src/{app.ts, app.test.ts, server.ts}
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── tsconfig.tsbuildinfo                  [tracked generated state]
│   └── web/
│       ├── src/{App.tsx, main.tsx, styles.css, vite-env.d.ts}
│       ├── dist-types/                           [tracked generated declarations/state]
│       ├── index.html
│       ├── package.json
│       ├── tsconfig.json
│       └── vite.config.ts
├── data/
│   ├── sources/README.md
│   ├── curation/README.md
│   └── generated/README.md
├── docs/
│   ├── adr/
│   │   ├── 001-application-architecture.md
│   │   ├── 002-frontend-3d-integration.md
│   │   ├── 003-astronomical-coordinate-conventions.md
│   │   ├── 004-star-catalogue-and-provenance.md
│   │   ├── 005-bkt-runtime-boundary.md
│   │   ├── 006-persistence-and-transactions.md
│   │   ├── 007-testing-and-validation.md
│   │   └── README.md
│   ├── governance/                               [12 preserved governance documents]
│   ├── ARCHITECTURE.md
│   ├── ASTRONOMY_SPEC.md
│   ├── DATA_STRATEGY.md
│   ├── DEPENDENCIES.md
│   ├── IMPLEMENTATION_BRIEF.md
│   ├── IMPLEMENTATION_DECISIONS.md
│   ├── PHASES.md
│   ├── SCAFFOLD_AUDIT.md
│   ├── STATUS.md
│   ├── TEST_PLAN.md
│   └── TUTORING_BKT_SPEC.md
├── packages/
│   ├── adaptive-policy/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── assessment-core/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── astronomy-core/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── bkt-core/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── catalogue-schema/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── contracts/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── star-data/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── tutoring-core/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   └── README.md
├── scripts/
│   ├── check-boundaries.mjs
│   ├── run-e2e.mjs
│   └── verify-data-scaffold.mjs
├── tests/
│   ├── e2e/health.spec.ts
│   ├── integration/README.md
│   ├── performance/README.md
│   └── reference/README.md
├── tools/
│   ├── astronomy-reference/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── catalogue-pipeline/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   ├── catalogue/{src/index.ts, package.json, tsconfig.json, tsconfig.tsbuildinfo}
│   └── README.md
├── .env.example
├── .gitignore
├── .npmrc
├── .nvmrc
├── .prettierignore
├── .prettierrc.json
├── AGENTS.md
├── README.md
├── eslint.config.mjs
├── package.json
├── package-lock.json
├── playwright.config.ts
├── tsconfig.base.json
├── tsconfig.json
├── tsconfig.tests.json
└── vitest.config.ts
```

## 2. Current workspaces and dependency graph

```text
@ufuq/web --------------------------> @ufuq/contracts
@ufuq/api --------------------------> @ufuq/contracts
@ufuq/assessment-core --------------> @ufuq/astronomy-core
@ufuq/adaptive-policy --------------> @ufuq/bkt-core
@ufuq/catalogue-schema -------------> @ufuq/star-data
@ufuq/tutoring-core ----------------> @ufuq/assessment-core
                   ├----------------> @ufuq/bkt-core
                   └----------------> @ufuq/adaptive-policy
@ufuq/astronomy-reference ----------> @ufuq/astronomy-core       [defect]
@ufuq/catalogue-pipeline -----------> @ufuq/catalogue-schema
                         └----------> @ufuq/star-data
@ufuq/catalogue --------------------> @ufuq/catalogue-pipeline
```

The graph is acyclic. No runtime application/package currently imports a tool, and no
source imports another workspace's private `src` or `dist` path.

## 3. Responsibility and dependency assessment

| Workspace | Exact responsibility and intended public API | Current importers / intended consumers | Independent build and tests | Current value |
|---|---|---|---|---|
| `@ufuq/web` | Browser UI, R3F scene adapter, raw answer capture; application-only entry | No package importer; communicates with API and consumes contracts/presentation-safe data | Own Vite build, component tests near code, root E2E | Useful now |
| `@ufuq/api` | Express composition/HTTP application; later scenario, scoring, BKT orchestration, authz and persistence adapters | Reached over HTTP; should consume pure domains/contracts | Own Node build, API units and root integration tests | Useful now |
| `@ufuq/astronomy-core` | Pure coordinate/time/direction calculations and value types | Currently assessment and oracle manifests; later API, assessment and presentation-safe web use | Independent declarations/build and dense unit/reference tests | Immediately justified for Phase 1 |
| `@ufuq/assessment-core` | Pure typed spatial/directional scoring against authoritative targets/tolerances | Currently `tutoring-core`; should be consumed by API, not web/tutoring | Independent unit/property tests and build | Justified for Phase 2; currently empty |
| `@ufuq/bkt-core` | Pure BKT arithmetic and model value types | `adaptive-policy`, `tutoring-core`; later API indirectly | Independently testable, but does not require a separate package from policy at FYP scale | Speculative physical boundary |
| `@ufuq/adaptive-policy` | Pure scaffold transition policy over model evidence | `tutoring-core`; later API indirectly | Independently testable module, but not independently deployable | Speculative physical boundary |
| `@ufuq/tutoring-core` | Currently an empty facade over assessment, BKT and policy | No importer; intended API consumer is absent | Its build adds no independent behavior or tests | Redundant and conceptually mixed |
| `@ufuq/contracts` | Stable serialized request/response contracts by version | Web and API | Independent contract build/tests are justified | Useful, small, not yet a dumping ground |
| `@ufuq/star-data` | Generic cultural/learning content types, despite its numerical-sounding name | Catalogue schema and pipeline | No independent behavior/test need | Duplicate ownership with schema |
| `@ufuq/catalogue-schema` | Currently only a type re-export; should own runtime validation for catalogue, curation and generated artifacts | Catalogue pipeline; later web/API loaders | Independent schema build/tests are justified | Necessary name/boundary, unusable implementation |
| `@ufuq/astronomy-reference` | Independent oracle/fixture generation interface | Should be consumed only as artifacts by reference tests | Distinct toolchain/build/tests justified | Immediately useful, but current dependency invalidates independence |
| `@ufuq/catalogue-pipeline` | Intended acquisition/normalize/join/validate/serialize implementation | `@ufuq/catalogue` | No independent public API or deployment need | Redundant implementation workspace |
| `@ufuq/catalogue` | Approved catalogue command/tool entry | No package importer; should expose a CLI | Independent tool build and deterministic tests justified | Necessary, but currently wraps an empty wrapper |

## 4. Workspace recommendations

| Workspace | Recommendation | Reason |
|---|---|---|
| `@ufuq/web` | **KEEP** | A real application boundary with distinct browser/runtime dependencies. |
| `@ufuq/api` | **KEEP** | A real application and authority boundary; keep one modular-monolith process. |
| `@ufuq/astronomy-core` | **KEEP** | Central pure scientific domain and immediate Phase 1 work. |
| `@ufuq/assessment-core` | **KEEP** | Scoring semantics depend on astronomy but must remain unavailable to the web. |
| `@ufuq/bkt-core` | **MERGE into `tutoring-core`** | Preserve BKT as an internal module; a package plus facade is unnecessary for one developer. |
| `@ufuq/adaptive-policy` | **MERGE into `tutoring-core`** | Preserve a separate policy module/version inside the package; no independent deployment boundary exists. |
| `@ufuq/tutoring-core` | **KEEP, redefine** | Own pure BKT arithmetic, observation-decision semantics and adaptive policy. Remove its dependency on assessment. |
| `@ufuq/contracts` | **KEEP, narrow** | Own only versioned serialized API contracts and their framework-free runtime validation. Do not absorb domain models or database rows. |
| `@ufuq/star-data` | **MERGE into `catalogue-schema`** | Its only implementation is the content type source that the schema package re-exports. The name incorrectly suggests numerical rows. |
| `@ufuq/catalogue-schema` | **KEEP, enable runtime schemas** | One package can hold conceptually separate catalogue, content and generated-artifact schema modules. |
| `@ufuq/astronomy-reference` | **KEEP, decouple** | Independence and a different toolchain justify the boundary. It must not import production astronomy. If the oracle is Python-only, keep the tool directory but remove it from npm workspaces. |
| `@ufuq/catalogue-pipeline` | **MERGE into `@ufuq/catalogue`** | Pipeline stages are internal modules of one CLI, not a separately consumed product. |
| `@ufuq/catalogue` | **KEEP** | Reproducible offline acquisition/build/verification needs a tool boundary outside runtime. Expose a CLI rather than a library facade. |

The recommended npm-workspace count is nine. It becomes eight only if the independent
oracle is implemented solely as a non-Node/Python project rather than an npm workspace.

## 5. Findings by severity

### BLOCKING — STR-B01: root reference and integration tests are undiscoverable

`test:reference` and `test:integration` target root test directories, but
`vitest.config.ts` includes only `apps/**/*.test.ts`, `packages/**/*.test.ts`, and
`tools/**/*.test.ts`. Both commands currently return success with:

```text
No test files found, exiting with code 0
include: apps/**/*.test.ts, packages/**/*.test.ts, tools/**/*.test.ts
```

Adding a future test under `tests/reference` or `tests/integration` will not override the
include pattern. `--passWithNoTests` can therefore turn missing scientific or MySQL
evidence into a green command. Phase 1 requires an independently discovered reference
suite, so this must be corrected before that phase starts.

### BLOCKING — STR-B02: the schema package cannot implement schemas

`check-boundaries.mjs` classifies `catalogue-schema` as type-only and rejects every
runtime statement. The package currently just re-exports interfaces from `star-data`.
`PHASES.md`, `DATA_STRATEGY.md`, and ADR-004 require Phase 1 parsing, runtime schema
validation, referential integrity, canonical artifacts, and explicit rejection of bad
data. TypeScript interfaces disappear at runtime and cannot validate downloaded or
curated input. Keeping this rule would either make Phase 1 fail its boundary check or
encourage unvalidated data to cross the system.

### BLOCKING — STR-B03: the independent oracle depends on production astronomy

`@ufuq/astronomy-reference` declares and project-references `@ufuq/astronomy-core`, and
the boundary checker explicitly permits that edge. ADR-007 requires the reference
fixture generator to remain structurally independent from runtime TypeScript astronomy.
If the oracle imports production value/formula implementation, the same defect can
appear on both sides and create false agreement. The tool should emit a neutral,
versioned fixture artifact; `tests/reference` should compare that artifact with
`astronomy-core` without the oracle importing the system under test.

### MAJOR — STR-M01: four workspaces are facade/ownership duplication

`tutoring-core` adds a facade over three packages without an importer or unique API;
`catalogue-schema` re-exports all of `star-data`; and `catalogue` wraps
`catalogue-pipeline`. This creates extra manifests, references, build state, export
surfaces and boundary-map entries while leaving ownership ambiguous. Once code lands,
developers will need to decide repeatedly which of two packages owns each type or test.
The proposed merges remove four workspaces while retaining logical modules.

This also reconciles the physical repository with FYP scale. ADR-005's separation of
BKT arithmetic and adaptive policy should remain as modules, tests and versioned
interfaces inside `tutoring-core`; it does not require separate npm packages. Because
ADR-005 and IMP-007 currently describe the old physical layout, those decisions must be
updated explicitly before migration rather than silently reinterpreted.

### MAJOR — STR-M02: 19 generated compiler files are tracked

Thirteen `tsconfig.tsbuildinfo` files and six emitted web declaration/map files under
`apps/web/dist-types` are committed. `.gitignore` does not currently exclude
`dist-types/` or `*.tsbuildinfo`. These machine-generated files can change with OS,
absolute path, compiler version or build ordering, creating merge churn and stale public
declarations. They are outputs, not source or evidence, and should be regenerated by a
clean build.

### MAJOR — STR-M03: boundary policy encodes scaffold edges, not the approved runtime

The current allowlist permits web and API to depend only on `contracts`. The approved
architecture requires the API to consume astronomy, assessment and tutoring domains,
and permits the web to consume a presentation-safe astronomy API while forbidding
authoritative scoring/tutoring. When correct Phase 2 code is introduced, the existing
checker will reject it. That makes duplication in the apps or an ad-hoc weakening of the
checker likely. Define the intended final allowed graph during the consolidation:

```text
web -> contracts, catalogue-schema, presentation-safe astronomy API
api -> contracts, catalogue-schema, astronomy-core, assessment-core, tutoring-core
assessment-core -> astronomy-core
tutoring-core -> no app/framework/persistence package
runtime packages/apps -X-> tools
```

If the web will instead receive all render vectors from the API, document that choice
and omit its astronomy edge. Do not leave the decision implicit.

### MAJOR — STR-M04: contracts are incorrectly constrained to compile-time types only

The package is not yet a dumping ground: it contains only `HealthResponse`. However,
the boundary checker prohibits runtime statements and ESLint prohibits all imports,
while the architecture requires versioned validation schemas for untrusted HTTP data.
Pure framework-free parsers/validators belong with their serialized DTOs so API and web
do not maintain divergent shapes. Domain entities, astronomy calculations, ORM rows,
React props and cultural source records do not belong there.

### MAJOR — STR-M05: tracked provenance and restricted/raw catalogue bytes lack a
physical boundary

`data/sources` is intended to hold both tracked manifests and possibly permitted raw
snapshots. Nothing structurally prevents a large, restricted or redistribution-unclear
download from being staged. Before acquisition, use a tracked `data/manifests` area and
a default-ignored `data/raw` area. An approved licence decision can explicitly opt a
specific immutable snapshot into Git; accidental tracking should not be the default.

### MAJOR — STR-M06: cross-platform line-ending policy is missing

There is no `.gitattributes`. UFUQ intends byte-for-byte catalogue and fixture hashes on
Windows and Linux, while Git line-ending conversion can change checked-out text bytes.
The canonical serializer must define its own encoding/newline behavior, and repository
attributes should pin LF for source, manifests, curation and generated textual
artifacts while marking true binary inputs as binary. Without this, local/CI checksum
differences can be environmental rather than scientific.

### MINOR — STR-N01: tool packages expose library entries instead of command entries

Both tools currently publish `main`/`types` entries but no `bin`. They are private and
empty, so resolution works, but their intended public surface is a command plus artifact
format, not a runtime library API. The merged catalogue tool and reference wrapper
should expose named commands when implementation begins.

### MINOR — STR-N02: root tooling scripts are formatted but not linted

The ESLint command covers apps, packages, tools and tests, but not the non-trivial
root `scripts/*.mjs` or configuration modules. `node --check` was used during the prior
audit, but it is not a stable CI lint gate. Include root tooling in lint scope or add a
small dedicated check.

### MINOR — STR-N03: no performance-suite command exists

`tests/performance` is a sensible cross-system location, but no root script/config owns
it. This does not block Phase 1; define the command and recorded-environment behavior
before Phase 5 performance evidence begins.

### MINOR — STR-N04: the prior scaffold audit is now historical but not marked superseded

`SCAFFOLD_AUDIT.md` ends in failure because the lockfile/workflow were untracked at that
time. They are tracked now and the worktree was clean during this audit. Preserve the
history, but a future status update should clearly link the resolving checkpoint or a
rerun so readers do not treat the old blocker as current.

### OPTIONAL — STR-O01: app-internal layers should appear only with behavior

Do not create empty `services`, `repositories`, `utils`, `common` or plugin folders.
When Phase 2 introduces scenario issuance/submission, add small use-case modules and
HTTP adapters inside `apps/api/src`; add persistence ports/adapters there in Phase 4.
Likewise, add web scene/lesson/API-client feature folders only when their first files
exist. No additional app workspace is needed.

### OPTIONAL — STR-O02: app declaration output is unnecessary

`apps/web` is private and has no package consumers. Emitting declarations for it adds no
public API value. It may use a no-emit typecheck plus Vite build instead, provided the
root project-reference strategy is adjusted deliberately. Ignoring rather than tracking
`dist-types` is the minimum required correction.

## 6. Architecture-layer assessment

### Pure domains

`astronomy-core` and `assessment-core` are correctly directed and framework-free.
`tutoring-core` should become the pure learning domain containing internal BKT,
observation-decision and adaptive-policy modules. Its current dependency on
`assessment-core` should disappear: correctness evidence is an input to tutoring, not a
reason for tutoring to own spatial scoring.

### Contracts

Keep one narrow contract package. Organize future exports by API version or endpoint,
not as a generic `shared` barrel. It may contain serialized DTOs, discriminants,
version identifiers and framework-free runtime validators. It must not become the
source of truth for domain objects, persistence rows, UI props or curation records.

### Web

The current web app has no authoritative scorer, BKT mutation, persistence or secret.
Keep rendering/raycast/input conversion in the app. Direct Three.js types stop at the
scene adapter. The future dependency rule must explicitly allow only the selected
presentation-safe astronomy/content surface and continue forbidding assessment,
tutoring, API internals and persistence.

### API

One workspace is correct. Do not create separate application, repository or adapter
packages. As behavior arrives, use folders inside `apps/api/src`, for example
`application/`, `adapters/http/`, `adapters/persistence/` and `composition/`, but create
each only with its first concrete module. Use cases own ports; Express/MySQL adapters
depend inward. This is sufficient for scenario issuance, scoring, BKT orchestration,
authorization, idempotency and transactions.

### Offline tools

Tools are outside the production dependency graph today. Keep that invariant. The
catalogue tool may consume schema modules; runtime packages/apps may never consume the
tool. The reference oracle should consume only its independent inputs and output
fixtures; comparison code, not the oracle, imports production astronomy.

## 7. Data and lesson-content placement

Numerical astronomy and reviewed educational/cultural content must remain conceptually
separate, but separate npm workspaces are unnecessary. The simplest maintainable
arrangement is:

- `packages/catalogue-schema/src/catalogue/`: serialized numerical source/runtime row
  schemas, units, versions and validators;
- `packages/catalogue-schema/src/content/`: `SkyPattern`,
  `GuidanceRelationship`, `LessonRoute`, review metadata and validators;
- `packages/catalogue-schema/src/artifact/`: generated manifest/hash/version envelope;
- `data/manifests/`: tracked source/licence/query manifests;
- `data/raw/`: immutable acquired bytes, ignored by default;
- `data/curation/patterns`, `relationships`, and `routes`: separately reviewed source
  records, with no duplicated coordinates;
- `data/generated/`: deterministic joined runtime artifacts, committed only when the
  approved licence/release policy permits;
- `tools/catalogue`: acquisition, normalization, joins, validation, canonical
  serialization and checksum commands;
- `apps/api`: authoritative scenario/route eligibility and runtime artifact loading;
- `apps/web`: read-only loading/rendering of the same version/hash; and
- schema and referential tests beside `catalogue-schema`, deterministic-build tests
  beside the catalogue tool, and cross-system/scientific fixtures under root tests.

This supports helper pattern to Banat Na'sh or Dhat al-Kursi, either path to Al-Jady,
then True North and Qibla without a named-pattern package or hardcoded app folder. The
graph is content data; infrastructure deals only in generic IDs, typed nodes, ordered
edges, alternatives, review status and scenario availability.

## 8. Testing-layout assessment

Recommended placement:

| Test class | Location |
|---|---|
| Astronomy calculation/value units and properties | Beside `packages/astronomy-core/src` |
| Spatial scoring units/properties | Beside `packages/assessment-core/src` |
| BKT, observation semantics and policy units | Beside modules in `packages/tutoring-core/src` |
| Catalogue/content schema and referential integrity | Beside `packages/catalogue-schema/src` |
| Pipeline deterministic-build/checksum tests | Beside `tools/catalogue/src` |
| React component/raycast adapter tests | Beside web feature modules when needed |
| API use-case/controller units | Beside API modules |
| Independent astronomy/BKT fixtures and comparisons | `tests/reference/{astronomy,bkt}` with a dedicated config |
| Real MySQL transaction/auth/API tests | `tests/integration/{api,mysql}` with a dedicated config/environment |
| Browser journeys/accessibility | `tests/e2e` under Playwright |
| Frozen scene/performance evidence | `tests/performance` with a recorded environment and separate command |

Do not make one Vitest include pattern run units, slow MySQL and independent reference
suites together. Give reference and integration suites their own config/include and
remove `--passWithNoTests` as soon as their phase begins.

## 9. Build and TypeScript assessment

The current technical mechanics are otherwise sound:

- all manifest internal edges match TypeScript project references;
- shared strict settings and composite/declaration settings are valid;
- the root solution covers all 13 workspaces and build order follows references;
- every declared public entry currently resolves after a build;
- there are no cycles, private-source imports, editor-only path aliases or runtime-to-tool
  edges; and
- NodeNext is used for Node packages while the web correctly uses Vite's bundler
  resolution.

The required corrections are structural rather than compiler failures: remove tracked
outputs, update references after consolidation, allow runtime validation where
required, break the oracle edge, and make the allowed graph represent intended runtime
layers rather than the empty scaffold.

## 10. Over-engineering and missing-boundary summary

### Over-engineered

- separate BKT, adaptive-policy and empty tutoring-facade workspaces;
- separate star-data and catalogue-schema workspaces where one only re-exports the
  other; and
- separate catalogue entry and catalogue-pipeline workspaces with no independent
  consumer.

### Missing or incorrect

- discoverable, fail-closed reference/integration test configurations;
- a runtime schema/validation capability;
- genuine oracle independence;
- an explicit approved future app-to-domain dependency graph;
- a safe tracked-manifest versus raw-download data boundary;
- repository line-ending rules for deterministic artifacts; and
- ignore/removal policy for compiler state and declarations.

No microservice, event system, plugin architecture, generic service layer, separate
persistence workspace or shared-utils package is missing.

## 11. Recommended final tree

```text
apps/
├── web/                         # React/R3F UI; internal feature folders when needed
└── api/                         # one modular monolith; internal use-case/adapters later
packages/
├── astronomy-core/              # pure science/value types
├── assessment-core/             # pure scoring
├── tutoring-core/               # bkt/, observations/, adaptive-policy/ modules
├── contracts/                   # versioned DTOs + pure runtime validation
└── catalogue-schema/            # catalogue/, content/, artifact/ schemas/validators
data/
├── manifests/                   # tracked provenance/licence/query inputs
├── raw/                         # ignored by default; immutable authorized inputs
├── curation/
│   ├── patterns/
│   ├── relationships/
│   └── routes/
└── generated/                   # deterministic output under explicit licence policy
tools/
├── astronomy-reference/         # independent CLI/environment; no production import
└── catalogue/                   # one acquisition-to-verification CLI
tests/
├── reference/{astronomy,bkt}/
├── integration/{api,mysql}/
├── e2e/
└── performance/
scripts/                         # cross-platform repository orchestration only
docs/
.github/workflows/
```

This tree has nine npm workspaces if both tools use Node wrappers.

## 12. Minimal migration plan

No migration was performed by this audit. Before Phase 1:

1. Approve and document the physical-package consolidation, including an explicit
   update to ADR-005 and IMP-003/007. Preserve logical BKT/policy separation inside
   `tutoring-core`.
2. Add deterministic line-ending/encoding attributes. Ignore `dist-types/`,
   `*.tsbuildinfo`, `.vite/` and other generated state; remove the 19 tracked generated
   files from Git while retaining source.
3. Merge `star-data` into structured modules under `catalogue-schema`; remove the
   type-only restriction from the schema package and add runtime-validation tests.
4. Merge `catalogue-pipeline` into `tools/catalogue` and define one CLI surface.
5. Break the `astronomy-reference -> astronomy-core` dependency. Define a neutral
   versioned fixture exchange and put comparison logic in `tests/reference`.
6. Merge BKT and adaptive policy into `tutoring-core`; remove its assessment dependency.
   Preserve separate files, types, tests and version identifiers.
7. Replace scaffold-only dependency allowlists with the approved final layer graph and
   explicit runtime-to-tools/private-source prohibitions.
8. Separate tracked manifests from ignored raw catalogue bytes before any acquisition.
9. Give unit, reference, integration, E2E and performance suites distinct discovery
   rules; make an active suite fail when its expected tests are absent.
10. Update root workspaces, project references, manifests, lockfile, CI, architecture,
    implementation decisions and status together. Run clean install, typecheck,
    boundaries, export resolution, all active tests and deterministic-data checks before
    checkpointing the migration.

Because the affected workspaces contain almost no behavior, this is the cheapest and
safest time to make the change.

## 13. Risks of changing versus keeping

| Choice | Risks |
|---|---|
| Change now | One controlled documentation/package/lockfile migration; boundary and CI scripts must be updated together; ADR-005's physical-package wording needs explicit revision. Empty packages make code-loss and merge risk low. |
| Keep current | Ambiguous ownership becomes real duplication; every small change touches more manifests/references/build outputs; correct app dependencies fail the checker; reference suites can stay falsely green; the oracle can reproduce production bugs; raw data can be committed accidentally; generated compiler state causes cross-platform churn. Later migration will require moving implemented code and fixtures. |

The risk of keeping the structure is materially higher than changing it before Phase 1.

## 14. Portability and OneDrive risks

Current scripts use Node process spawning and path APIs rather than shell-specific
commands. Workspace discovery, boundary checks and typechecking passed from the Windows
path containing spaces. GitHub Actions uses Linux-compatible commands. Case-sensitive
consistency checking is enabled.

OneDrive is an environmental risk, not an architecture defect:

- synchronization can lock or repeatedly upload `node_modules`, compiler state,
  Playwright artifacts and raw catalogue files;
- Files On-Demand can make a present-looking raw/reference artifact unavailable during
  a build;
- timestamp/sync behavior can trigger unnecessary incremental rebuilds; and
- Windows' case-insensitive filesystem can hide case errors that Linux CI exposes.

Prefer a non-synchronized working clone before large catalogue/oracle work, or exclude
dependency/build/raw-output directories from OneDrive synchronization. Keep the Git
remote and approved reproducibility store as the durable sources; do not treat OneDrive
sync as provenance or backup evidence.

## 15. Read-only validation results

| Check | Result |
|---|---|
| `git ls-tree -r --name-only HEAD` | 126 tracked files inventoried. |
| `npm.cmd ls --workspaces --depth=0` | 13 workspaces found. |
| `npm.cmd run boundaries` | PASS; 13 workspaces and no dependency cycle. |
| `npm.cmd run typecheck` | PASS; root solution and no-emit test config. |
| Manifest dependencies versus project references | PASS; every internal edge matches. |
| Public `main`/`types`/`exports` path check | PASS after existing build; no missing entry. |
| Runtime-to-tools manifest/source scan | PASS; no runtime package imports a tool. |
| Private `src`/`dist` import scan | PASS; zero matches. |
| `npm.cmd run test:reference` | Structural FAIL: exits 0 with no tests and an include pattern that excludes `tests/reference`. |
| `npm.cmd run test:integration` | Structural FAIL: exits 0 with no tests and an include pattern that excludes `tests/integration`. |
| Tracked-output check | FAIL: 19 compiler-state/declaration output files tracked. |
| `git status --short` after validation | Clean; read-only checks did not alter tracked files. |

## Final verdict

The high-level architecture is defensible, but the current folder/workspace structure
requires a small, explicit consolidation and three Phase 1 blocker corrections before
the astronomy/data spike. Passing compilation and cycle checks do not override those
findings.

STRUCTURE_SUITABLE: NO
