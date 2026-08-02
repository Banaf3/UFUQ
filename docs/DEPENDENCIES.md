# Scaffold dependencies

All versions are exact in workspace manifests and `package-lock.json`. Phase 0 adds no
database client, authentication library, astronomy engine, catalogue client, BKT
library, analytics SDK, or deployment dependency.

## Production dependencies

| Dependency | Workspace | Why it is present |
|---|---|---|
| `react` 19.2.8 | `apps/web` | Approved component/UI runtime for the browser application and health screen. |
| `react-dom` 19.2.8 | `apps/web` | Mounts the React application in the browser DOM. |
| `three` 0.185.1 | `apps/web` | Approved future 3D rendering adapter dependency; no scene or astronomy behavior is implemented yet. |
| `@react-three/fiber` 9.6.1 | `apps/web` | Approved React integration layer for Three.js; installed now to pin the scaffold boundary, but not used for a lesson or scene yet. |
| `express` 5.2.1 | `apps/api` | Approved HTTP adapter used only for the minimal `/health` endpoint. |

Internal `@ufuq/*` entries are local workspace links, not third-party production
packages. They encode the approved eight-workspace dependency direction checked by
`npm run boundaries`. `tutoring-core` has no internal workspace dependency;
`assessment-core` depends only on `astronomy-core`; `tools/catalogue` depends only on
`catalogue-schema`; and applications consume only their approved pure packages.

No runtime schema library is present. `contracts` and `catalogue-schema` currently
contain types/empty boundaries and are permitted to add framework-free validators. A
schema dependency is postponed until Phase 1 implements a real validator and records
why the selected library is preferable to a small local parser or another candidate.

## Independent Python reference environment

`tools/astronomy-reference` is not an npm workspace and has no dependency on a
production package. Its `pyproject.toml` intentionally installs no library during this
migration. Phase 1 must select and pin Python, Astropy, and any reference-data
dependencies in a separate reproducible environment before the oracle produces a
fixture. This keeps the scientific oracle independent and avoids claiming an
unvalidated version choice now.

## Development dependencies

- TypeScript and Node/React/Express type packages provide strict compilation.
- Vite and its React plugin build/serve the web scaffold.
- ESLint, TypeScript ESLint, React Hooks/Refresh plugins, and Prettier enforce source
  quality and formatting.
- Vitest and Supertest test the API health surface without opening a network port.
  Separate unit, reference, and integration Vitest configurations prevent inactive
  scientific/database suites from being reported as passed.
- Playwright runs the real-browser web/API smoke test.
