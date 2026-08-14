# UFUQ source gaps

## Rule

These gaps do not block repository scaffolding or reference-skill preparation. Each gap
blocks only the affected implementation, approval, or evidence claim. Do not substitute
memory, an unpinned web page, or an unrelated local PDF.

## Required before or during the astronomy/data spike

| Gap ID | Required source or decision evidence | Current status | Closure evidence |
|---|---|---|---|
| AST-SRC-001 | Pinned Astropy reference environment | `CLOSED_FOR_SYNTHETIC_SMOKE_ONLY`: CPython, uv, Astropy, PyERFA, transitive packages, platform, lock hash, and IERS resources are tracked. Source-derived scientific use remains outside the smoke claim, and shared lineage is disclosed. | `tools/astronomy-reference/uv.lock`, `environment-manifest.json`, dependency contract, and locked reproduction evidence |
| AST-SRC-002 | Official Astropy coordinate and IERS documentation | `CLOSED_FOR_2C.1_TO_2C.4_REFERENCE_DESIGN`: exact official pages for Astropy `8.0.1` time formats/scales, space motion, GCRS/CIRS/ITRS/AltAz transformation roles, EarthLocation, LeapSeconds, IERS status/warnings, refraction inputs/defaults, and low-altitude limitations are recorded with retrieval version/date. Astropy remains reference-only; no library default becomes UFUQ policy. | `studies/astropy-pyerfa-reference-docs.md`, `studies/refraction-horizon-visibility.md`, and `ASTROPY-DOCS-PIN` |
| AST-SRC-003 | PyERFA and `astropy-iers-data` versions | `PARTIAL`: PyERFA `2.0.1.5`, its official PyPI release/source hash, `astropy-iers-data` `0.2026.7.20.15.31.18`, and packaged file hashes are pinned. Official PyERFA `stable` API docs displayed `2.0.1.4`, leaving a version-matched documentation or reviewer-acceptance gap for later postimplementation reference-validation claims. This shared-lineage package cannot provide the stronger independent oracle. | Version-matched PyERFA documentation/tagged-source review or explicit reviewer acceptance before relying on its exact API behaviour in postimplementation reference validation |
| AST-SRC-004 | Offline/network IERS-data policy | `CLOSED_FOR_PROFILE_V1_IMPLEMENTATION`: V1 accepts only independently approved final Bulletin B/final-derived `UT1-UTC`,`xp`,`yp`; selects Gazette 13's four-point example/full support as project policy, uses continuous `UT1-TAI` across leaps, and requires exactly-once IERS Conventions 2010 ocean-tide/applicable-libration restoration after interpolation; separates quality, artifact integrity, field coverage/support, publisher validity, acquisition lifecycle and approval; executes from one explicit immutable offline bundle; activates only through reviewed atomic updates; retains prior bundles; and has no degraded fallback. | **2D:** select/acquire exact official artifacts, raw field evidence/hashes, Bulletin C consistency, exact 2010-baseline interpolation/restoration source configuration/product regularization and activation record. **2E:** implement parsers, normalized independent fields, interpolation/restoration, bundle generation and fail-closed lookup. Numerical uncertainty remains postimplementation. |
| AST-SRC-005 | Atmospheric-refraction assumptions | `DEFERRED_FROM_PROFILE_V1`: SOFA `iauRefco` input units/model form and `iauAtioq` numerical guard plus Astropy `8.0.1` pressure/default/low-altitude behavior are pinned. ScientificProfileV1 normatively disables refraction, requests no atmosphere, inserts no defaults, and emits no refracted coordinate. Library defaults/guards and the documented about-5-degree region are not UFUQ policy, range, or tolerance. | Required only before a later refraction extension: AST-004/006 approval of model/version, measured/derived input provenance and uncertainty, inputs/height/lapse, environment/altitude domain, near/below-horizon behavior, warnings, bounds, and experiments |
| AST-SRC-006 | Supported date range | `CONTRACT_RESOLVED_ACTIVATION_DATA_OPEN`: ScientificProfileV1 normatively requires a versioned `SupportedTimeDomain`, explicit earliest/latest canonical UTC values, independent inclusive/exclusive dispositions, whole-second resolution, complete required-field/interpolation support, exact-boundary and adjacent-instant behavior, and fail-closed outside-domain outcomes. No concrete endpoint is invented. Actual values are deterministically derived and approved in 2D/2E activation from the intersection of approved catalogue, model/ephemeris, leap, per-field EOP, observer, and scenario domains. | `BLOCKS_2D_DATA_AUTHORITY` / activation: approved source/artifact domains and derived bounds with fixtures. Prediction limits remain later unless the EOP policy includes prediction. This is no longer a 2C semantic blocker. |
| AST-SRC-007 | Leap-second/time-scale policy | `CLOSED_FOR_PROFILE_V1_IMPLEMENTATION`: source-defined UTC/TAI/TT/UT1 roles, RFC 3339's broader syntax, Bulletin C event authority, SOFA quasi-JD/conversion behavior and Astropy reference behavior are recorded. V1 selects whole-second `YYYY-MM-DDTHH:mm:ssZ`, exact-event validation of conditional `23:59:60Z`, typed UTC quasi-JD/TAI/TT/UT1 states, an official IERS/IANA machine-transport eligibility contract, publisher-validity handling, no implicit local/current time or unlabeled JD, explicit evidence and fail-closed outcomes. | **2D:** select/acquire exact transport bytes/hash, prove Bulletin C consistency, approve validity scope and activate the bundle; 2D/2E derives bounds. Wall-time UX and any future negative-leap grammar revision remain later. |
| AST-SRC-008 | Approved Kaaba target coordinate and datum if Qibla geodesy is included | `OPEN`; outside Milestone 2C astronomy scope | Authority citation, coordinate/datum approval, and versioned decision record |
| AST-SRC-009 | Exact CDS I/311 epoch representation and time scale | `PARTIAL`: I/311 says only `Ep=1991.25`; official ESA Gaia DR1 directly identifies I/311 and calls its epoch `J1991.25`, resolving the representation as Julian. Neither source states an I/311 time scale. Original ESA `J1991.25(TT)` and generic Astropy `jyear` semantics are supporting candidates, not I/311 authority. | An I/311-applicable authoritative time-scale/exact-instant statement, or named astronomy-review approval of a bounded project interpretation; synthetic sensitivity results cannot close source meaning |
| AST-SRC-010 | Production transformation route and implement-or-omit effect decision | `CLOSED_FOR_PROFILE_V1_IMPLEMENTATION`: Milestone 2C.6 selects the source-neutral typed route, a UFUQ-owned pure-TypeScript subset derived from exact SOFA `2023-10-11` C semantics, strict approved epoch/derivative/parallax/RV row states, model-CIP-only IAU 2006/2000A celestial orientation, explicit `UT1-UTC`,`xp`,`yp`, geometric-only output, and the complete V1 effect dispositions. Current official package/repository/licence evidence is recorded in `studies/typescript-astronomy-production-candidates.md`; no audited third-party package matches the required semantic/data/status boundary. | **POST_IMPLEMENTATION:** production/reference comparison, implementation and omission residuals, error-budget population, and tolerance approval remain mandatory acceptance work. A later stronger oracle must disclose that the production SOFA-derived subset and Astropy/PyERFA/ERFA reference share scientific lineage. No remaining registered experiment blocks implementation of the selected route. |
| AST-SRC-011 | I/311 space-motion time unit/scale and radial-velocity evidence | `SOURCE_DATA_OPEN_GENERIC_BRANCH_RESOLVED`: CDS Catalogue Standard 2.0 defines the VizieR `yr` unit as exactly 365.25 days. It does not define I/311's epoch/derivative time scale, and I/311 supplies no radial velocity for the V1 route. ScientificProfileV1 now requires approved epoch/derivative semantics, positive approved parallax/equivalent distance, and approved finite radial velocity for every eligible row; missing or unapproved values make the row ineligible and never become zero/defaults. | **2D:** establish I/311-applicable epoch/derivative authority and authoritative RV/parallax row evidence if retaining I/311, select another source/crossmatch, or mark affected rows ineligible. This no longer blocks the source-neutral engine boundary. Sensitivity results can inform later bounds but not source meaning. |
| AST-SRC-012 | Production observer and endpoint domain | `CONTRACT_DEFINED_DATA_OPEN`: Milestone 2C defines a generic fail-closed `ObserverPreset`, north-positive geodetic latitude, east-positive `[-180 deg,+180 deg)` canonical longitude, explicit datum/frame/ellipsoid/typed height/conditional epoch/accuracy/provenance/version/approval states, and V1-only ID `umpsa-pekan-faculty-of-computing`. Official UMPSA evidence supports the Faculty-at-Pekan identity only. This public-web audit did not establish an exact reference point, coordinate, height, accuracy, source artifact, or Faculty-specific JUPEM control record; that is not evidence none exists. | **2D:** acquire and approve the exact UMPSA record, use/licence conditions and immutable provenance before real V1 execution; unknown accuracy remains explicit and unbounded. A JUPEM survey-control record is optional, not mandatory. **LATER:** acquire `Riyadh, Saudi Arabia` or other presets and approve multiple/global ranges, poles, arbitrary locations, and their boundary fixtures. |
| AST-SRC-013 | Horizon and visibility policy authority | `V1_EXCLUSION_RESOLVED_LATER_POLICY_OPEN`: ScientificProfileV1 normatively emits geometric output only, retains below-geometric-horizon as a valid attached classification, requests no refraction, supplies no atmosphere default, emits no aggregate visibility, and does not infer learner eligibility. Geometric, refracted-apparent, physical-dip, terrain/obstruction, renderer, and learner horizon meanings remain distinct, as do the nine future visibility components. SOFA horizontal/refraction routines define none of UFUQ's physical dip, terrain, photometric, daylight, transparency, weather, light-pollution, rendering, or teaching rules. | **LATER:** primary evidence and AST-001/004/006/007 approval before enabling refraction, any numerical near-horizon/near-singular boundary, physical reference-surface/dip, terrain/building/obstruction, band/magnitude/null/variability, Sun-altitude/daylight/twilight, extinction/transparency, cloud/weather, light pollution, screen or learner policy, aggregation, warnings, or endpoint serialization. None blocks geometric V1 implementation, and no excluded term becomes zero. |
| AST-SRC-014 | Scientific experiment execution and acceptance evidence | `PARTIAL_BY_LIFECYCLE`: Milestone 2C.5A freezes 24 records; 2C.5B completes 9/9 synthetic Batch 01 experiments with 24 exact passes, 0 failures, six measurement-only checks, and 27 `MEASURED_NO_ACCEPTANCE` records; 2C.5C inventories them without changing hashed inputs. This is sufficient preimplementation guard/protocol evidence. No source-derived or production comparison exists because their inputs/code do not yet exist. | Review Batch 01 without promotion. Source-derived cases follow 2D eligibility. Production/reference cases and `test:reference` follow implementation. Other synthetic/refraction work runs only when its decision/data/later-scope gate opens. |
| AST-SRC-015 | Scientific error-budget terms, correlation model, supported-domain bounds, and operation-specific tolerances | `PARTIAL_FRAMEWORK_POSTIMPLEMENTATION_NUMBERS`: Milestone 2C.5C defines layers A-H and inventories 49 terms: 45 retain an unbounded numerical-bound state and four exact non-numerical aggregate guards are distinct from the 24 Batch checks. It blocks all six tolerance classes and recommends `FINAL_TOLERANCE_NOT_JUSTIFIED`. Milestone 2C.6 assigns each term a lifecycle without changing any bound. | Review the method now. Populate source/model/data/implementation evidence and approve per-operation bounds/tolerances only after production/reference and any stronger-independent evidence required by the claimed boundary exist. Numerical closure is a scientific-acceptance gate, not a 2C implementation prerequisite. |
| DATA-SRC-001 | Select the production catalogue/release and establish transport authenticity, local/deployment rights, minimal allowlist, row-level solution/quality/uncertainty/covariance evidence, and a stable UFUQ `starId`/source-release crosswalk. If 2D retains I/311, its original URL/timestamp or equivalent transport evidence and explicit raw/derived redistribution permission remain required. | `OPEN`; Milestone 2B closes only the I/311 local-spike parser contract and does not select a permanent source | 2D source decision plus licence, acquisition/provenance, crosswalk, and row-review records. Reuse the I/311 field/null/duplicate/sorting/checksum contract only if that source is retained; create tracked source manifests only when the scaffold guard is intentionally activated. |
| DATA-SRC-002 | Official JSON Schema Draft 2020-12 Core/Validation version pins and runtime validator decision | `PARTIAL`: official Core/Validation sources and schema dialect are pinned. Batch 01 uses a tested fail-closed local validator only for the exact keywords in its three experiment schemas; unsupported keywords/non-local references fail. This is not full meta-schema conformance or a production/browser validator choice. | Select and justify any general runtime validator; record exact version/vocabularies/reference/format policy; run official/meta-schema conformance and production-boundary tests before closing the broader decision |

## Milestone 2C.6 controlling categories

One primary category controls each astronomy/data gap even when its stable record also
mentions a secondary lifecycle:

| Primary category | Gap IDs |
|---|---|
| `A BLOCKS_SCIENTIFIC_PROFILE_V1` | None |
| `B BLOCKS_2D_DATA_AUTHORITY` | `AST-SRC-004`, `AST-SRC-006`, `AST-SRC-007`, `AST-SRC-009`, `AST-SRC-011`, `AST-SRC-012`, `DATA-SRC-001`, `DATA-SRC-002` |
| `C POST_IMPLEMENTATION_VALIDATION` | `AST-SRC-003`, `AST-SRC-014`, `AST-SRC-015` |
| `D BLOCKS_LATER_EXTENSION` | `AST-SRC-005`, `AST-SRC-013` |
| `E BLOCKS_LEARNER_FACING_CONTENT` | `CULT-SRC-001` through `CULT-SRC-004` |
| `F NOT_REQUIRED_FOR_PROFILE_V1` | `AST-SRC-001`, `AST-SRC-002`, `AST-SRC-008`, `AST-SRC-010` |

For `AST-SRC-010`, the closed route has secondary C production-comparison obligations.
For `AST-SRC-011`, the source-neutral missing-value branch is resolved while source-row
authority remains B. For `AST-SRC-014`, source-derived
cases are secondary B and nonrequired later synthetic/refraction work is D/F. These
secondary relationships do not change the primary roadmap owner.

## Required before Najdi cultural claims

| Gap ID | Required source or decision evidence | Closure evidence |
|---|---|---|
| CULT-SRC-001 | Najdi primary or regional evidence | Citable source with period/geographical scope and exact claim pointer |
| CULT-SRC-002 | Rashid al-Khalawi material or a credible scholarly treatment | Verified edition/treatment and claim-level citation |
| CULT-SRC-003 | Human Arabic/cultural review | Named review role, date, status, conflicts, and approved text |
| CULT-SRC-004 | Explicit evidence for exact pattern membership and instructional routes | Claim table joining Arabic evidence, modern catalogue IDs, geometry, route role, and review status |

Kunitzsch, Ibn Qutaybah, Hafez, and King cannot close these gaps by themselves.

## Required before assessment/BKT implementation

| Gap ID | Required source area | Closure evidence |
|---|---|---|
| EDU-SRC-001 | Corbett and Anderson's original knowledge-tracing source | Verified bibliographic record and relevant model sections |
| EDU-SRC-002 | Evidence-Centered Design | Selected authoritative source and assessment-argument mapping |
| EDU-SRC-003 | Scaffolding research | Selected evidence tied to each proposed scaffold meaning |
| EDU-SRC-004 | BKT properties, parameter, and sensitivity sources | Source set, parameter rationale, simulations, and sensitivity plan |
| EDU-SRC-005 | Educational-testing standards | Approved standards source and task-validity checklist |

No BKT/adaptive-scaffolding skill is active until this set can support a focused
procedure.

## Required before the 3D interaction phase

| Gap ID | Required source area | Closure evidence |
|---|---|---|
| UI-SRC-001 | *3D User Interfaces*, 2nd edition, or equivalent | Verified source and applicable interaction sections |
| UI-SRC-002 | WCAG 2.2 | Pinned W3C Recommendation and conformance scope |
| UI-SRC-003 | WAI-ARIA Authoring Practices Guide | Pinned W3C APG version and component patterns used |
| UI-SRC-004 | Pinned Three.js and React Three Fiber documentation | Exact library/doc versions and relevant API pages |
| UI-SRC-005 | Relevant rendering/performance reference | Selected benchmark/design source tied to UFUQ scene risks |

## Required before persistence and authentication

| Gap ID | Required source area | Closure evidence |
|---|---|---|
| SEC-SRC-001 | OWASP ASVS | Pinned ASVS version and selected verification level/requirements |
| SEC-SRC-002 | NIST Secure Software Development Framework | Pinned SSDF version and applicability mapping |
| DB-SRC-001 | Official MySQL transaction, isolation, and deadlock documentation | Pinned MySQL version/pages plus real-MySQL transaction tests |

## Required before participant evaluation

| Gap ID | Required source area | Closure evidence |
|---|---|---|
| EVAL-SRC-001 | *Standards for Educational and Psychological Testing* | Verified edition and applicable validation/interpretation sections |
| EVAL-SRC-002 | Selected usability instrument source | Licensed instrument, scoring source, and use conditions |
| EVAL-SRC-003 | Study-design guidance | Selected source tied to design, sampling, analysis, and limitations |
| EVAL-SRC-004 | UMPSA ethics and participant-data requirements | Current institutional policy, approval route, and approved protocol/data plan |

## Sources deliberately not promoted

- The local ISO 20022 JSON paper is `NOT_REQUIRED`; it is not the JSON Schema
  specification.
- PROV Semantics is `OPTIONAL`; formal PROV reasoning is outside UFUQ scope.
- David King's books are `HISTORICAL_CONTEXT_ONLY` for production geodesy.
- No source currently supports a `NAJDI_TRADITION` production classification without
  additional regional evidence and human review.
