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
| AST-SRC-004 | Offline/network IERS-data policy | `PARTIAL_PROPOSAL`: Milestone 2C.3 proposes request-time offline execution from immutable hash-addressed bundles, separate reviewed atomic updates, retained old bundles, distinct source-quality/artifact-availability/field-availability/scientific-approval state for every required EOP field, and explicit non-results. No product class, production artifact, stale rule, update cadence, field-quality approval, field precedence, interpolation, or degraded mode is approved. | **PRE_IMPLEMENTATION:** approve product classes, accepted per-field quality, precedence/interpolation/coverage, stale/expiry/update/offline rules, and deterministic failure/warning semantics. **2D:** acquire and approve the exact bytes/hashes and activation/replay record. |
| AST-SRC-005 | Atmospheric-refraction assumptions | `DEFERRED_FROM_PROFILE_V1`: SOFA `iauRefco` input units/model form and `iauAtioq` numerical guard plus Astropy `8.0.1` pressure/default/low-altitude behavior are pinned. ScientificProfileV1 normatively disables refraction, requests no atmosphere, inserts no defaults, and emits no refracted coordinate. Library defaults/guards and the documented about-5-degree region are not UFUQ policy, range, or tolerance. | Required only before a later refraction extension: AST-004/006 approval of model/version, measured/derived input provenance and uncertainty, inputs/height/lapse, environment/altitude domain, near/below-horizon behavior, warnings, bounds, and experiments |
| AST-SRC-006 | Supported date range | `PARTIAL_PROPOSAL`: Milestone 2C.6 requires one bounded V1 interval derived from approved catalogue, model/ephemeris, leap, per-field EOP, observer, and scenario coverage, with explicit endpoint outcomes. A later tolerance gate evaluates results over the interval rather than forming a circular prerequisite to define it. No numerical endpoint, prediction horizon, or inclusion rule is selected. | Approved earliest/latest V1 instants, inclusive/exclusive semantics, interpolation-neighbour requirement, and endpoint/just-outside fixtures; prediction limits are later if V1 rejects prediction |
| AST-SRC-007 | Leap-second/time-scale policy | `PARTIAL_PROPOSAL`: source-defined UTC/TAI/TT/UT1 roles, RFC 3339's broader timestamp/leap syntax, IERS Bulletin C announcement authority, and Astropy leap-table behaviour are recorded. Milestone 2C.3 proposes a UFUQ-selected Z-only UTC subset and fail-closed offline artifact use; second `60` becomes syntactically valid only after exact-date validation. It selects no production machine artifact bytes/hash, precision, expiry rule, Bulletin C cross-check, or update cadence. | **PRE_IMPLEMENTATION:** approve UTC grammar/precision, exact-date leap validation, artifact class/validity/expiry/update semantics, and stable outcomes. **2D:** select and acquire the machine-readable artifact/version/hash and record its Bulletin C cross-check and replay provenance. Wall-time UX is a later adapter concern. |
| AST-SRC-008 | Approved Kaaba target coordinate and datum if Qibla geodesy is included | `OPEN`; outside Milestone 2C astronomy scope | Authority citation, coordinate/datum approval, and versioned decision record |
| AST-SRC-009 | Exact CDS I/311 epoch representation and time scale | `PARTIAL`: I/311 says only `Ep=1991.25`; official ESA Gaia DR1 directly identifies I/311 and calls its epoch `J1991.25`, resolving the representation as Julian. Neither source states an I/311 time scale. Original ESA `J1991.25(TT)` and generic Astropy `jyear` semantics are supporting candidates, not I/311 authority. | An I/311-applicable authoritative time-scale/exact-instant statement, or named astronomy-review approval of a bounded project interpretation; synthetic sensitivity results cannot close source meaning |
| AST-SRC-010 | Production transformation route and implement-or-omit effect decision | `PARTIAL_PROPOSAL`: Milestone 2C.2 defines a componentized SOFA `2023-10-11` CIO-family semantic candidate, classifies every effect, and separates the Astropy/PyERFA reference route. Milestone 2C.6 narrows preimplementation closure to approval of the `ScientificProfileV1` route/library mapping, motion/parallax/RV and effect dispositions, and route/data-specific warning ownership. The source-neutral boundary, geometric exclusions, core precedence, and warning preservation are already normative. No TypeScript implementation is required to make the remaining decision. | **PRE_IMPLEMENTATION:** AST-003 route/effect approval. **POST_IMPLEMENTATION:** production/reference comparison, implementation residuals, error-budget population, and tolerance approval. Remaining later-effect experiments do not block V1 when their effects are excluded. |
| AST-SRC-011 | I/311 space-motion time unit/scale and radial-velocity evidence | `PARTIAL`: CDS Catalogue Standard 2.0 defines the VizieR `yr` unit as exactly 365.25 days. It does not define I/311's epoch/derivative time scale, and I/311 supplies no radial velocity for the proposed route. This controls I/311 data eligibility, not the source-neutral engine boundary. | **2D:** I/311-applicable epoch/derivative authority and RV/parallax row policy if retained. **PRE_IMPLEMENTATION:** approve the typed unavailable/omission branch without substituting zero. Sensitivity results can inform later bounds but not source meaning. |
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
| `A BLOCKS_SCIENTIFIC_PROFILE_V1` | `AST-SRC-004`, `AST-SRC-006`, `AST-SRC-007`, `AST-SRC-010` |
| `B BLOCKS_2D_DATA_AUTHORITY` | `AST-SRC-009`, `AST-SRC-011`, `AST-SRC-012`, `DATA-SRC-001`, `DATA-SRC-002` |
| `C POST_IMPLEMENTATION_VALIDATION` | `AST-SRC-003`, `AST-SRC-014`, `AST-SRC-015` |
| `D BLOCKS_LATER_EXTENSION` | `AST-SRC-005`, `AST-SRC-013` |
| `E BLOCKS_LEARNER_FACING_CONTENT` | `CULT-SRC-001` through `CULT-SRC-004` |
| `F NOT_REQUIRED_FOR_PROFILE_V1` | `AST-SRC-001`, `AST-SRC-002`, `AST-SRC-008` |

For `AST-SRC-010`, production comparison is secondary C. For `AST-SRC-011`, the
source-neutral missing-value branch is secondary A. For `AST-SRC-014`, source-derived
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
