# UFUQ structure migration

**Migration date:** 2026-07-22
**Branch:** `chore/consolidate-ufuq-structure`
**Baseline:** `801e7da` (`main`)
**Preserved audit checkpoint:** `f30a774`

## Outcome

The accepted findings in `STRUCTURE_AUDIT.md` were applied without starting the
astronomy/data spike. The repository now has exactly eight npm workspaces, a separate
non-npm Python reference-tool scaffold, fail-closed test partitions, untracked compiler
outputs, explicit data/provenance boundaries, and dependency rules that describe the
intended application architecture.

No astronomical formula, catalogue row, cultural route, BKT behavior, application
feature, authentication behavior, database migration, or production deployment was
introduced.

## Old-to-new path mapping

| Old path | New path or disposition |
|---|---|
| `packages/bkt-core/src/` | `packages/tutoring-core/src/bkt/` |
| `packages/adaptive-policy/src/` | `packages/tutoring-core/src/adaptive-policy/` |
| No observation module | `packages/tutoring-core/src/observations/` |
| `packages/tutoring-core` facade dependencies | Removed; `tutoring-core` has no dependency on `assessment-core` or another workspace |
| `packages/star-data/src/index.ts` | `packages/catalogue-schema/src/content/index.ts` |
| `packages/catalogue-schema/src/index.ts` re-export facade | Root plus `src/catalogue/`, `src/content/`, and `src/artifact/` public modules |
| `tools/catalogue-pipeline/src/` | Internal `tools/catalogue/src/pipeline/` module |
| TypeScript/npm `tools/astronomy-reference` | Non-npm Python scaffold with a dependency contract and neutral fixture-envelope schema |
| `data/sources/` | Tracked `data/manifests/` plus default-ignored `data/raw/` |
| Single `data/curation/` placeholder | `patterns/`, `relationships/`, and `routes/` placeholders |
| Root `vitest.config.ts` | `vitest.unit.config.ts`, `vitest.reference.config.ts`, and `vitest.integration.config.ts` |
| Web `dist-types/` declaration build | No-emit TypeScript check plus Vite application build |

The obsolete `bkt-core`, `adaptive-policy`, `star-data`, and `catalogue-pipeline`
workspace manifests, TypeScript references, source placeholders, and stale local build
directories were removed after their logical boundaries were recreated at the target
paths.

## Structural decisions

1. The npm workspace list is explicit rather than globbed, so the non-npm oracle and
   future non-workspace tool directories cannot be enrolled accidentally.
2. BKT arithmetic, observation semantics, and adaptive policy retain separate module
   paths, subpath exports, future tests, and versioning responsibilities inside one pure
   `tutoring-core` package.
3. Numerical catalogue schemas, educational/cultural content schemas, and generated
   artifact schemas retain separate module paths inside one `catalogue-schema` package.
   Framework-free runtime validators are permitted; no validator or schema dependency
   was added before real Phase 1 behavior exists.
4. `contracts` may contain framework-free validators beside versioned serialized DTOs.
   Domain entities, database rows, React props, services, and cultural source records
   remain outside it.
5. The Python/Astropy oracle communicates through
   `astronomy-reference-fixture.v1.schema.json`. It has no npm manifest, TypeScript
   reference, production-package dependency, or calculation. Phase 1 must pin Python,
   Astropy, and reference data before producing any case.
6. Unit tests are the only active Vitest suite in Phase 0. Reference and integration
   configurations target their required root directories and fail if invoked empty.
   Reference becomes mandatory when Phase 1 introduces the first production/reference
   comparison; integration becomes mandatory when Phase 4 introduces the first
   API/persistence integration test.
7. The package checker enforces both declared and source-level edges, rejects cycles,
   private workspace paths, Node/framework/persistence imports from pure packages,
   runtime-to-tool imports, web imports of authoritative domains, and production
   coupling in the oracle.
8. `.gitattributes` normalizes textual source, schema, manifest, curation, and generated
   files to LF and marks actual binary formats as binary. Canonical data serialization
   separately requires UTF-8, LF, deterministic key/record ordering, Unicode policy,
   and defined numeric formatting.
9. No empty service, repository, utils, common, plugin, or performance-command
   abstraction was added.

## Approved npm workspaces

| Workspace | Responsibility | Public surface | Direct internal dependencies | Build/test need |
|---|---|---|---|---|
| `apps/web` | React/Vite presentation and future R3F adapter | Private application; no package export | contracts, catalogue-schema, astronomy-core | Vite build, no-emit typecheck, component/E2E tests as behavior appears |
| `apps/api` | Express composition and authoritative application boundary | `createApp` for integration/composition | contracts, catalogue-schema, astronomy-core, assessment-core, tutoring-core | Node build and API tests |
| `packages/astronomy-core` | Pure astronomy value types/calculations | Root package export | none | Declarations and Phase 1 unit/reference comparison |
| `packages/assessment-core` | Pure spatial/directional scoring | Root package export | astronomy-core | Declarations and Phase 2 unit/property tests |
| `packages/tutoring-core` | Pure BKT, observations, and adaptive policy | Root plus three logical subpath exports | none | Declarations and Phase 3 module tests |
| `packages/contracts` | Versioned serialized DTOs and pure validators | Root package export | none | Shared declarations and contract tests |
| `packages/catalogue-schema` | Catalogue/content/artifact serialized schemas and validators | Root plus three logical subpath exports | none | Shared declarations and Phase 1 schema tests |
| `tools/catalogue` | Offline acquisition-to-artifact tooling | Root tool module until real CLI commands exist | catalogue-schema | Node build and Phase 1 deterministic pipeline tests |

Each workspace has an independently enforceable responsibility and at least two
consumers or a required isolated pure/tool test boundary. Further package splitting is
not justified at FYP scale.

## Generated files removed from tracking

Nineteen generated files were removed with `git rm --cached` and are now ignored:

- 13 `tsconfig.tsbuildinfo` files, one for each old npm workspace;
- `apps/web/dist-types/src/App.d.ts` and its map;
- `apps/web/dist-types/src/main.d.ts` and its map;
- `apps/web/dist-types/vite.config.d.ts` and its map.

Stale ignored `dist/` directories under the four removed workspaces and the former
TypeScript oracle were also removed locally. Current build output is reproducible and
remains ignored.

## Exact commands and results

| Command | Result |
|---|---|
| `git status --short` | Found only the prior untracked `docs/STRUCTURE_AUDIT.md`; no user source change was present. |
| `git switch -c chore/consolidate-ufuq-structure` | PASS; new branch created from `801e7da`. |
| `git add -- docs/STRUCTURE_AUDIT.md` and `git commit -m "docs: record UFUQ structure audit"` | PASS; preserved the accepted audit as checkpoint `f30a774`, leaving `main` unchanged. |
| `git rm --cached -- ':(glob)**/*.tsbuildinfo' ':(glob)apps/web/dist-types/**'` | PASS; 19 generated files removed from the index. |
| `npm.cmd install --package-lock-only --ignore-scripts` | Updated the active eight-workspace graph, but a targeted scan found five stale `extraneous` workspace objects retained by npm. |
| `npm.cmd prune --package-lock-only --ignore-scripts` | Completed but did not remove those stale objects; the five exact obsolete package objects were removed from the lockfile and JSON validity was rechecked by `npm ci`. |
| `npm.cmd ci` | PASS; 306 packages installed from the lockfile. |
| `npm.cmd run format:check` | PASS; all matched files use Prettier style. |
| `npm.cmd run lint` | PASS; source, tests, scripts, and relevant root configuration modules reported no error. |
| `npm.cmd run typecheck` | PASS; composite Node/shared build graph plus no-emit web and test/config checks. |
| `npm.cmd run test` | PASS; 1 unit file and 1 health test. |
| `npm.cmd run boundaries` | PASS; 8 workspaces, approved dependencies, no private/runtime-to-tool import, no cycle, independent oracle. |
| `npm.cmd run cycles` | PASS; workspace graph acyclic. |
| `npm.cmd run data:verify` | PASS; only tracked placeholders, no raw/generated/catalogue/cultural records. |
| `npm.cmd run build` | PASS; API, five shared packages, catalogue tool, and web built; Vite transformed 16 modules. |
| `npm.cmd run exports:check` | PASS; 13 public export paths across 7 importable workspaces resolved. |
| `npm.cmd run test:e2e` | PASS; 1 Chromium web/API health smoke test. |
| `npm.cmd run test:reference` | Expected exit 1: no test files; include was `tests/reference/**/*.test.ts`. |
| `npm.cmd run test:integration` | Expected exit 1: no test files; include was `tests/integration/**/*.test.ts`. |
| `npm.cmd ls --workspaces --depth=0` | PASS; exactly the approved 8 workspaces, no extraneous workspace. |
| Obsolete-name scan of `package-lock.json` | PASS after correction; zero removed workspace path/package name remains. |
| Tracked-output, runtime-to-tool, private-import, restricted/secret/raw, scope, and oracle scans | PASS; zero prohibited item found. |
| `git check-attr` on representative source/schema/manifest/curation/generated/binary paths | PASS; textual paths use LF and binary formats are marked binary. |

The targeted read-only scans used these core commands (PowerShell wrappers converted
an unexpected match into a non-zero assertion):

```powershell
git ls-files
git check-ignore --quiet -- local-reference/CB23011_FYP_REPORTv2.pdf
rg -n 'astronomy-reference|@ufuq/catalogue|(?:^|[./])tools/' apps packages --glob '*.ts' --glob '*.tsx'
rg -n '@ufuq/[^/]+/(src|dist)(/|$)' apps packages tools/catalogue tests --glob '*.ts' --glob '*.tsx'
rg -n 'packages/(adaptive-policy|bkt-core|star-data)|tools/(astronomy-reference|catalogue-pipeline)|@ufuq/(adaptive-policy|bkt-core|star-data|astronomy-reference|catalogue-pipeline)' package-lock.json
rg -n 'Math\.|sin\(|cos\(|tan\(|atan|sidereal|precession|nutation|parallax|proper.?motion|qibla|kaaba' packages/astronomy-core packages/assessment-core --glob '*.ts'
rg -n 'posterior|mastery|P\(L|guess|slip|transition|threshold' packages/tutoring-core --glob '*.ts'
rg -n 'CREATE TABLE|ALTER TABLE|SELECT .* FROM|INSERT INTO|passport|bcrypt|argon|login|authenticate' apps packages tools/catalogue --glob '*.ts' --glob '*.tsx'
Get-ChildItem data -Recurse -File
git check-attr text eol -- apps/api/src/app.ts packages/catalogue-schema/src/content/index.ts tools/astronomy-reference/fixtures/astronomy-reference-fixture.v1.schema.json data/manifests/README.md data/curation/patterns/README.md data/generated/README.md
git diff --check
git diff --cached --check
```

Expected-match filters allowed only `data/raw/.gitignore`, `data/raw/README.md`, and
`.env.example`; high-confidence secret patterns were also scanned across the full
working tree outside ignored dependency/build/restricted directories. All assertions
passed.

## CI behavior

GitHub Actions continues to use `npm ci` on the Node version pinned by `.nvmrc`. It runs
formatting, linting, type checking, the dependency/cycle/oracle boundary check, the data
guard, active unit tests, all production builds, export resolution, Playwright Chromium
installation, and the smoke test. Reference and integration suites are deliberately
absent from Phase 0 CI; adding each command is part of its documented activation rule.
Playwright failure reports and traces remain retained by the existing artifact step.

## Independent post-migration audit

### Layering

- `astronomy-core` is framework-, I/O-, app-, database-, and oracle-independent.
- `assessment-core` points only to `astronomy-core`.
- `tutoring-core` is pure, has no workspace dependency, and cannot import
  `assessment-core`; authoritative correctness reaches it as an application-supplied
  observation in a later phase.
- `contracts` and `catalogue-schema` have narrow serialized-data responsibilities and
  can validate at runtime without becoming domain or UI dumping grounds.
- The web cannot import assessment/tutoring/tool code. The API can compose the five
  approved package boundaries. No app layer exists before its first behavior.
- Production code cannot import either offline tool. The catalogue tool depends inward
  on schemas; the Python oracle has no production dependency.

Result: no incorrect dependency, duplicated source of truth, or missing runtime/tool
boundary remains.

### Data-driven content

The structure supports arbitrary reviewed pattern-to-pattern/star/direction graphs.
Schemas and curated sources are separated from catalogue rows and generated artifacts;
the generic content types are preserved with no concrete constellation, cultural
mapping, star row, or application special case. Route eligibility will belong to the
API when implemented, using the same versioned generated artifact as the web.

Result: suitable for the multi-step/alternative-route requirement without premature
content selection.

### Testing and build

Unit tests remain beside code; cross-system reference, real-MySQL integration, browser,
and later performance evidence have distinct roots. Empty later suites cannot pass.
Every emit-producing TypeScript project is composite with valid declarations; the
private web app is deliberately no-emit and is checked explicitly before Vite builds.
Package exports resolve without editor-only aliases or private `src`/`dist` imports.

Result: discovery, build order, declarations, and package resolution are suitable.

### FYP scale and portability

The migration removes four speculative npm boundaries and does not add enterprise
layers. Eight workspaces are the minimum approved set that preserves pure science,
scoring, learning, serialized contracts/content, two applications, and one offline
catalogue tool. Scripts are Node/TypeScript based and ran from the Windows OneDrive path
containing spaces; CI uses Linux-compatible commands. OneDrive remains an environmental
risk for locks, synchronization churn, and large future raw data, not an architecture
defect.

Result: the structure is proportionate for one bachelor-level developer.

## Remaining risks

- Phase 1 must pin the independent Python/Astropy environment and define the concrete
  case payload fields before producing scientific fixtures.
- Phase 1 must justify any runtime schema dependency when the first validator is
  implemented.
- Reference CI must be activated with the first astronomy comparison; integration CI
  must be activated with the first real API/MySQL integration.
- `data/raw/` may become large and OneDrive may lock or partially hydrate it. Prefer a
  non-synchronized working clone or an approved external reproducibility store before
  catalogue acquisition.
- The domains are intentionally empty. Structural suitability is not evidence of
  astronomy, cultural, educational, persistence, security, participant, or deployment
  readiness.

No structure change is required before the astronomy/data technical spike.

STRUCTURE_SUITABLE: YES
