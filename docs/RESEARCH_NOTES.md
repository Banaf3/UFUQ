# Research notes

**Access date for all links:** 2026-07-20. Primary/official material was preferred. These notes record the decision supported and important limitations; they do not copy the restricted report.

## Agent workflow and application architecture

| Source | Decision supported | Limitation |
|---|---|---|
| [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Keep durable repository guidance on layout, commands, constraints, conventions, and definition of done. | Workflow guidance, not a UFUQ domain authority. |
| [OpenAI: Codex ExecPlans](https://developers.openai.com/cookbook/articles/codex_exec_plans) | Require living, self-contained executable plans for multi-session/complex phases. | Adapted to this repository in `.agent/PLANS.md`. |
| [React: Managing State](https://react.dev/learn/managing-state) | Treat UI state structure and single ownership deliberately; keep semantic React state separate from high-frequency scene internals. | Does not prescribe a 3D architecture. |
| [Three.js: Raycaster](https://threejs.org/docs/pages/Raycaster.html) | Raycasting is the direct Three.js mechanism for spatial picking; account for camera and layers. | Correct answer and overlap policy remain UFUQ responsibilities. |
| [Three.js: Vector3](https://threejs.org/docs/pages/Vector3.html) | Use vector dot/cross/normalization in the scene adapter and angular tests. | Not an astronomy reference. |
| [React Three Fiber: first scene](https://r3f.docs.pmnd.rs/getting-started/your-first-scene) | R3F can declaratively integrate Three.js with React while preserving direct Three objects/hooks where necessary. | Integration choice is clarified, not required by the report. |
| [TypeScript: Project References](https://www.typescriptlang.org/docs/handbook/project-references) | Enforce package boundaries and scalable cross-package checking in the planned monorepo. | Exact build tooling awaits an ExecPlan. |
| [Node.js: release policy](https://nodejs.org/en/about/previous-releases) | Pin a supported Active or Maintenance LTS runtime for production and recheck it at phase/release time. | Release status changes; this audit does not hard-code a transient “latest” version. |
| [Express production security](https://expressjs.com/en/advanced/best-practice-security/) | TLS, secure headers/cookies, input handling, dependency hygiene, and reduced fingerprinting inform API hardening. | A checklist is not a full threat model. |
| [MySQL 8.4: InnoDB transaction model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html) | Use InnoDB transactions for the attempt/mastery unit and understand isolation/locking behavior. | Exact supported MySQL version and isolation level must be tested. |
| [MySQL 8.4: locking reads](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html) | Lock mastery/session rows during serialized assessment updates. | Lock ordering and deadlock retry are application responsibilities. |
| [MySQL: locks set by statements](https://dev.mysql.com/doc/refman/8.0/en/innodb-locks-set.html) | Duplicate-key inserts have non-trivial locking/deadlock behavior; idempotency needs a tested state machine rather than assuming a unique key is the whole protocol. | Exact behavior must be tested against the frozen SYS-001 version/profile. |
| [MySQL: InnoDB error handling](https://dev.mysql.com/doc/refman/8.0/en/innodb-error-handling.html) | Deadlocks can roll back a transaction while lock timeouts may have different scope; retry classification and bounds must be explicit. | Version/configuration behavior belongs to SYS-001 and integration evidence. |
| [MySQL 8.4: floating-point types](https://dev.mysql.com/doc/refman/8.4/en/floating-point-types.html) | `DOUBLE` provides more precision than `FLOAT`, supporting DEV-002. | Floating point is still approximate; tests need tolerances. |

## Astronomy, data, and Qibla

| Source | Decision supported | Limitation |
|---|---|---|
| [ESA Hipparcos catalogues](https://www.cosmos.esa.int/web/hipparcos/catalogues) | Hipparcos is a credible candidate catalogue with ESA provenance and stated credit/licensing information. | Catalogue/table choice and redistribution remain AST-001; link alone is not approval. |
| [CDS/VizieR I/239 ReadMe](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/I/239?format=html&tex=true) | Candidate field metadata for Hipparcos Main Catalogue, including identifiers, astrometry, proper motion, magnitude, and flags. | Metadata must be pinned/reviewed; redistribution terms are not sufficiently settled by this page. |
| [VizieR HIP catalogue search](https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=+HIP) | Shows archive catalogue alternatives/versions that make explicit AST-001 selection necessary. | Search results are not a source-selection decision. |
| [ESA Hipparcos catalogue description](https://hipparcos-tools.cosmos.esa.int/pstex/sect2_01.pdf) | Candidate catalogue epoch/frame/component semantics require exact source interpretation. | PDF metadata must be independently reviewed before constants are encoded. |
| [Astropy: AltAz](https://docs.astropy.org/en/stable/api/astropy.coordinates.AltAz.html) | Independent horizontal-coordinate fixtures; pressure zero represents topocentric/no-refraction behavior; near-horizon refraction needs care. | Astropy is the oracle tool, not production runtime; version/data must be pinned. |
| [Astropy: IERS data access](https://docs.astropy.org/en/stable/utils/iers.html) | UT1 and Earth-orientation data/version, auto-download and degraded/offline behavior affect accurate transformations and reproducibility. | Exact file/hash/settings and extrapolation policy remain AST-003. |
| [Astropy: apply_space_motion](https://docs.astropy.org/en/latest/coordinates/apply_space_motion.html) | Proper-motion propagation should be explicit and validated over the supported date range. | Result quality depends on complete source astrometry and assumptions. |
| [USNO: altitude and azimuth](https://aa.usno.navy.mil/faq/alt_az) | Independent conceptual/reference check for local horizontal position and observational inputs. | Online results/advice are not a packaged deterministic oracle by themselves. |
| [USNO: Greenwich Apparent Sidereal Time](https://aa.usno.navy.mil/faq/GAST) | Confirms the need to distinguish apparent sidereal time and Earth-orientation inputs. | Exact production algorithm remains AST-003. |
| [Mufti of Federal Territory: Falak FAQ](https://www.muftiwp.gov.my/ms/perkhidmatan/data-falak/faq-falak) | Malaysian domain source for Qibla practice/context and approximate national bearing range; supports expert validation. | Does not settle a single authoritative Kaaba coordinate or numerical tolerance. |
| [Mufti of Federal Territory: Qibla and satellite dish](https://muftiwp.gov.my/en/artikel/bayan-al-falak/5374-bayan-al-falak-siri-ke-13-arah-kiblat-dan-piring-astro) | Reinforces True-North-referenced Qibla context and local authority involvement. | Educational/domain discussion, not a complete computational specification. |
| [JUPEM Almanac 2025](https://www.jupem.gov.my/storage/upload/almanak/almanak2025-1732247258.pdf) | Candidate Malaysian official cross-check named during audit. | Retrieval timed out during this audit; no value from it is approved or used. Manual verification required. |
| [GeographicLib JavaScript tutorial](https://geographiclib.sourceforge.io/html/js/tutorial-2-interface.html) | Optional ellipsoidal inverse-geodesic sensitivity check. | Runtime baseline is spherical; adopting ellipsoidal semantics would need a deviation. |

## Learning model

| Source | Decision supported | Limitation |
|---|---|---|
| [Corbett & Anderson, 1994](https://link.springer.com/article/10.1007/BF01099821) | Original knowledge-tracing foundation and separate latent skill-state rationale. | Historical model assumptions do not validate UFUQ parameters or learning effect. |
| [pyBKT, 2023](https://www.mdpi.com/2624-8611/5/3/770) | Peer-reviewed implementation context and model variants reinforce reproducibility and comparison. | UFUQ uses its own small pure runtime; it must not import parameter claims uncritically. |
| [Systematic review of BKT](https://link.springer.com/article/10.1007/s11257-023-09389-4) | Supports documenting BKT assumptions, variants, evaluation diversity, and limitations. | Review findings do not choose UFUQ's KCs, hints, threshold, or protocol. |
| [BKT parameter constraints record](https://zenodo.org/records/12729768) | Supports explicit plausibility/identifiability constraints and sensitivity analysis. | Repository record should be followed to its underlying research before thesis claims; constraints remain model-dependent. |

## Testing, accessibility, performance, and security

| Source | Decision supported | Limitation |
|---|---|---|
| [Playwright: visual comparisons](https://playwright.dev/docs/test-snapshots) | Deterministic browser screenshot baselines and reviewed updates. | Pixel equality is environment-sensitive and does not prove scientific correctness. |
| [Playwright: accessibility testing](https://playwright.dev/docs/accessibility-testing) | Automated axe checks can be integrated into browser tests. | Official documentation states automated testing finds only some issues; manual review remains mandatory. |
| [Playwright: assertions](https://playwright.dev/docs/test-assertions) | Web-first assertions reduce timing flakiness in critical journeys. | Cannot replace database/domain assertions. |
| [Vitest: coverage](https://vitest.dev/guide/coverage.html) | Coverage thresholds can enforce exercised pure-domain branches. | Coverage is not correctness and does not select a test oracle. |
| [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Target WCAG 2.2 AA criteria for the accessible application shell and document limitations. | Spatial-assessment equivalence requires ACC-001 and human evaluation. |
| [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse) | Repeatable diagnostic accessibility/performance audits can supplement tests. | Scores vary and are not the 30 FPS/raycast acceptance measurement. |
| [web.dev RAIL](https://web.dev/articles/rail) | Frame responsiveness and user-centric performance framing inform measurement design. | UFUQ retains the report's explicit 30 FPS and 100 ms targets. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Version 5.0.0 is the stable verification standard; Level 1 is a minimum baseline for the proposed security profile. | SEC-003 must add risk-based privileged/research controls and evidence; it is not automatic certification. |
| [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | Supports the Argon2id candidate parameters and rehash strategy. | Benchmark on deployment hardware and update with security guidance. |
| [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | Opaque high-entropy sessions, secure cookie attributes, rotation, and expiry principles. | Exact lifetime/MFA/recovery remain SEC-002. |
| [Malaysia PDPA Amendment Act 2024 resources](https://www.pdp.gov.my/ppdpv1/en/akta/personal-data-protection-amendment-act-2024/) | Flags current amendment, DPO/breach and related regulator guidance for institutional review. | This architecture is not legal advice; applicability and operational duties remain SEC-001. |

## Restricted report inspection

The local report was parsed only into a temporary path outside the repository. Its objective, scope, formal requirements, use cases, data entities, equations, provisional BKT values, and evaluation targets were compared across sections. The extraction was reliable enough to avoid guessing missing sections. No report text, image, or extracted artifact is included here; its SHA-256 was used only for local identity checking and is intentionally not recorded in tracked documentation.
