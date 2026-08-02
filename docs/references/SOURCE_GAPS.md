# UFUQ source gaps

## Rule

These gaps do not block repository scaffolding or reference-skill preparation. Each gap
blocks only the affected implementation, approval, or evidence claim. Do not substitute
memory, an unpinned web page, or an unrelated local PDF.

## Required before or during the astronomy/data spike

| Gap ID | Required source or decision evidence | Current status | Closure evidence |
|---|---|---|---|
| AST-SRC-001 | Pinned Astropy oracle environment | `CLOSED_FOR_SYNTHETIC_SMOKE_ONLY`: CPython, uv, Astropy, PyERFA, transitive packages, platform, lock hash, and IERS resources are tracked. Source-derived scientific use remains outside the smoke claim. | `tools/astronomy-reference/uv.lock`, `environment-manifest.json`, dependency contract, and locked reproduction evidence |
| AST-SRC-002 | Official Astropy coordinate and IERS documentation | `OPEN`: runtime Astropy is locked, but the exact official documentation URLs/sections for the selected science protocol are not. | Versioned documentation URLs and the exact sections used |
| AST-SRC-003 | PyERFA and `astropy-iers-data` versions | `PARTIAL`: PyERFA `2.0.1.5`, `astropy-iers-data` `0.2026.7.20.15.31.18`, and packaged file hashes are pinned for the smoke oracle; the official PyERFA documentation record and production data selection are not. | Pinned versions, hashes where applicable, compatibility record, and selected documentation record |
| AST-SRC-004 | Offline/network IERS-data policy | `OPEN_FOR_PRODUCTION`: the smoke oracle is fail-closed/offline, but that bounded choice does not approve production data, expiry, prediction, update, or out-of-range behaviour. | Approved auto-download, cache, expiry, fallback, and failure behavior |
| AST-SRC-005 | Atmospheric-refraction assumptions | `OPEN` | Approved model/inputs, exclusion policy, and error analysis |
| AST-SRC-006 | Supported date range | `OPEN` | Approved endpoints and out-of-range behavior with fixture partitions |
| AST-SRC-007 | Leap-second/time-scale policy | `OPEN`: source-defined UTC/TAI/TT/UT1 roles are recorded, but production leap-second data and operational policy are not. | Approved UTC/UT1/TT handling and data provenance |
| AST-SRC-008 | Approved Kaaba target coordinate and datum if Qibla geodesy is included | `OPEN`; outside Milestone 2C astronomy scope | Authority citation, coordinate/datum approval, and versioned decision record |
| DATA-SRC-001 | For selected source I/311: original acquisition URL/timestamp or other transport-authenticity evidence, explicit raw/derived redistribution permission, and row-level review of the proposed allowlist's actual solution/multiplicity/quality evidence | `OPEN`; Milestone 2B closes only the local parser contract | Licence clarification plus reviewed acquisition/provenance and row-review records. The field, null/duplicate, candidate-scope, sorting, schema, checksum, local-use, and fail-closed tracking policies are defined in Milestone 2B; create a tracked manifest only when the scaffold guard is intentionally activated. |
| DATA-SRC-002 | Official JSON Schema Draft 2020-12 Core/Validation version pins and runtime validator decision | `OPEN` | Versioned schema references, dependency rationale if a validator is selected, and conformance tests |

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
