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
packages. They encode the allowed dependency direction checked by `npm run boundaries`.

## Development dependencies

- TypeScript and Node/React/Express type packages provide strict compilation.
- Vite and its React plugin build/serve the web scaffold.
- ESLint, TypeScript ESLint, React Hooks/Refresh plugins, and Prettier enforce source
  quality and formatting.
- Vitest and Supertest test the API health surface without opening a network port.
- Playwright runs the real-browser web/API smoke test.
