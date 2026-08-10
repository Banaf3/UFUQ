# UFUQ source gaps

## Rule

These gaps do not block repository scaffolding or reference-skill preparation. Each gap
blocks only the affected implementation, approval, or evidence claim. Do not substitute
memory, an unpinned web page, or an unrelated local PDF.

## Required before or during the astronomy/data spike

| Gap ID | Required source or decision evidence | Current status | Closure evidence |
|---|---|---|---|
| AST-SRC-001 | Pinned Astropy oracle environment | `CLOSED_FOR_SYNTHETIC_SMOKE_ONLY`: CPython, uv, Astropy, PyERFA, transitive packages, platform, lock hash, and IERS resources are tracked. Source-derived scientific use remains outside the smoke claim. | `tools/astronomy-reference/uv.lock`, `environment-manifest.json`, dependency contract, and locked reproduction evidence |
| AST-SRC-002 | Official Astropy coordinate and IERS documentation | `CLOSED_FOR_2C.1_TO_2C.4_REFERENCE_DESIGN`: exact official pages for Astropy `8.0.1` time formats/scales, space motion, GCRS/CIRS/ITRS/AltAz transformation roles, EarthLocation, LeapSeconds, IERS status/warnings, refraction inputs/defaults, and low-altitude limitations are recorded with retrieval version/date. Astropy remains reference-only; no library default becomes UFUQ policy. | `studies/astropy-pyerfa-reference-docs.md`, `studies/refraction-horizon-visibility.md`, and `ASTROPY-DOCS-PIN` |
| AST-SRC-003 | PyERFA and `astropy-iers-data` versions | `PARTIAL`: PyERFA `2.0.1.5`, its official PyPI release/source hash, `astropy-iers-data` `0.2026.7.20.15.31.18`, and packaged file hashes are pinned. Official PyERFA `stable` API docs displayed `2.0.1.4`, leaving a version-matched documentation or reviewer-acceptance gap; production data selection is also open. | Version-matched PyERFA documentation/tagged-source review or explicit reviewer acceptance, plus the separately approved production data selection |
| AST-SRC-004 | Offline/network IERS-data policy | `PARTIAL_PROPOSAL`: Milestone 2C.3 proposes request-time offline execution from immutable hash-addressed bundles, separate reviewed atomic updates, retained old bundles, distinct source-quality/artifact-availability/field-availability/scientific-approval state for every required EOP field, and explicit non-results. No production artifact, stale rule, update cadence, field-quality approval, field precedence, interpolation, or degraded mode is approved. | Astronomy/operations approval of exact EOP products/bytes/hashes, field precedence/interpolation and per-field quality/availability/approval policy, stale/expiry rule, update cadence/activation/replay procedure, and deterministic failure/warning mapping |
| AST-SRC-005 | Atmospheric-refraction assumptions | `PARTIAL_PROPOSAL`: SOFA `iauRefco` input units/model form and `iauAtioq` numerical guard plus Astropy `8.0.1` pressure/default/low-altitude behavior are pinned. Milestone 2C.4 proposes explicit provenance-bearing meteorology, no default atmosphere, geometric-only first-slice output, optional non-erasing refraction outcomes, and no approved below-horizon extrapolation. Library defaults/guards and the documented about-5-degree region are not UFUQ policy, range, or tolerance. | AST-004/006 approval of model/version, measured/derived input provenance and uncertainty, pressure/temperature/humidity/wavelength and height/lapse handling, valid environment/altitude domain, near/below-horizon/extrapolation behavior, warnings, bounds, and seven experiments |
| AST-SRC-006 | Supported date range | `PARTIAL_PROPOSAL`: Milestone 2C.3 defines the supported domain as the intersection of every approved catalogue, model/ephemeris, leap, per-field EOP, observer, scenario, and tolerance domain, with explicit unsupported/out-of-range endpoint outcomes. It selects no numerical endpoint, prediction horizon, or inclusion rule. | Approved earliest/latest instants, inclusive/exclusive semantics, interpolation-neighbour requirement, future-prediction limit, and endpoint/just-outside fixtures |
| AST-SRC-007 | Leap-second/time-scale policy | `PARTIAL_PROPOSAL`: source-defined UTC/TAI/TT/UT1 roles, RFC 3339's broader timestamp/leap syntax, IERS Bulletin C announcement authority, and Astropy leap-table behaviour are recorded. Milestone 2C.3 proposes a UFUQ-selected Z-only UTC subset and fail-closed offline artifact use; second `60` becomes syntactically valid only after exact-date validation. It selects no production machine artifact bytes/hash, precision, expiry rule, Bulletin C cross-check, or update cadence. | Approved UTC grammar/precision and IANA-wall-time adapter policy; selected machine-readable leap artifact/version/hash/validity; Bulletin C cross-check; update/replay procedure; stable outcome mapping |
| AST-SRC-008 | Approved Kaaba target coordinate and datum if Qibla geodesy is included | `OPEN`; outside Milestone 2C astronomy scope | Authority citation, coordinate/datum approval, and versioned decision record |
| AST-SRC-009 | Exact CDS I/311 epoch representation and time scale | `PARTIAL`: I/311 says only `Ep=1991.25`; official ESA Gaia DR1 directly identifies I/311 and calls its epoch `J1991.25`, resolving the representation as Julian. Neither source states an I/311 time scale. Original ESA `J1991.25(TT)` and generic Astropy `jyear` semantics are supporting candidates, not I/311 authority. | An I/311-applicable authoritative time-scale/exact-instant statement, or named astronomy-review approval of a bounded project interpretation; synthetic sensitivity results cannot close source meaning |
| AST-SRC-010 | Production transformation route and implement-or-omit effect decision | `PARTIAL_PROPOSAL`: Milestone 2C.2 defines a componentized SOFA `2023-10-11` CIO-family semantic candidate, classifies every effect, and separates the Astropy/PyERFA reference route. Milestone 2C.5B executes only the bounded same-family componentized/composed case and five synthetic motion-convention guards. Their measurement-only output cannot approve the production route or omission bounds. No production TypeScript implementation/library, reviewer approval, independent production comparison, omission bound, supported range, or tolerance is selected. | AST-003 approval of the final route/library/effect matrix and warning mapping; completed remaining applicable experiments; AST-006 error budget/tolerances; implementation/reference comparison evidence |
| AST-SRC-011 | I/311 space-motion time unit/scale and radial-velocity evidence | `PARTIAL`: CDS Catalogue Standard 2.0 defines the VizieR `yr` unit as exactly 365.25 days, supporting numeric conversion to SOFA radians per Julian year. It does not define I/311's epoch/derivative time scale. I/311 supplies no radial-velocity field for the proposed route. | I/311-applicable epoch/derivative-scale authority or named review, plus an authoritative RV source/crossmatch policy or named astronomy-review approval of bounded RV omission/unavailable behaviour backed by sensitivity results |
| AST-SRC-012 | Production observer and endpoint domain | `PARTIAL_PROPOSAL`: Milestone 2C.3 defines an explicit geodetic observer boundary with east-positive longitude, datum/ellipsoid, ellipsoidal height, provenance, uncertainty, invalid-versus-outside-domain outcomes, and no silent orthometric conversion. WGS 84, `[-180,+180)`, height/location ranges, polar semantics, uncertainty requirements, and unrestricted/global claims are not approved. | Named astronomy/scenario approval of datum/ellipsoid, height source/type/range and any geoid conversion, longitude representative, pole semantics, coordinate uncertainty/provenance, approved locations, and observer boundary fixtures |
| AST-SRC-013 | Horizon and visibility policy authority | `PARTIAL_PROPOSAL`: Milestone 2C.4 separates geometric, refracted-apparent, physical-dip, terrain/obstruction, renderer, and learner horizon states and nine independent astronomical, photometric/variability, Sun-altitude/daylight/twilight, atmospheric-extinction/transparency, cloud/weather, terrain/obstruction, light-pollution, screen, and learner-eligibility visibility components. Below-geometric-horizon attaches to and retains the valid geometric result. SOFA horizontal/refraction routines define none of UFUQ's physical dip, terrain, photometric, daylight, transparency, weather, light-pollution, rendering, or teaching rules. A rendered star is not scientifically visible. | Primary evidence and AST-001/004/006/007 approval for equality/tolerance, physical reference-surface/dip, terrain/building/obstruction, band/magnitude/null/variability, Sun-altitude/daylight/twilight, extinction/transparency, cloud/weather, light pollution, screen and learner policy, aggregation, warnings, endpoint serialization, and separation experiments |
| AST-SRC-014 | Scientific experiment execution and acceptance evidence | `PARTIAL`: Milestone 2C.5A freezes 24 human/machine records and schemas. Milestone 2C.5B completes 9/9 synthetic Batch 01 experiments with canonical fixtures/results/hashes: 24 exact checks pass, none fail, and six measurement-only checks cover 27 measurement records, all `MEASURED_NO_ACCEPTANCE`. The three epoch-label cases fix synthetic ITRS-geocentre `[0,0,0] m` as an explicit TT/TDB conversion input, not an observer-policy or source-authority decision; pre-correction evidence is invalidated and runner-regenerated. Same-family lineage, source prohibitions, and inactive production/reference status are retained. Milestone 2C.5C inventories every record and guard in the separate AST-006 ledger without editing hashed Batch inputs. No independent multi-model refraction path, source-derived case, or production comparison exists; five records remain project-decision blocked, one required-data blocked, and one production-deferred. | Review the bounded synthetic evidence without promoting it; pin missing independent models/data; resolve project decisions; execute remaining permitted families; add source-derived and production/reference cases only after their gates |
| AST-SRC-015 | Scientific error-budget terms, correlation model, supported-domain bounds, and operation-specific tolerances | `PARTIAL_FRAMEWORK`: Milestone 2C.5C defines layers A-H and inventories 49 terms: 45 retain an unbounded numerical-bound state and four exact non-numerical aggregate guards are distinct from the 24 Batch checks. It distinguishes all 27 measured values from source uncertainties/authority limits/allowances/thresholds, maps all 24 exact checks to bounded mistake classes, proposes boundary-specific metrics and conservative/covariance/RSS combination rules, and blocks all six tolerance classes. Required source, model, EOP/time, observer, atmosphere, production-implementation, scene, and learner numerical terms remain unbounded. The recommendation is `FINAL_TOLERANCE_NOT_JUSTIFIED`; no numerical threshold exists. | Resolve source epoch/derivative and selected-row uncertainty/covariance; approve route/effects, production EOP/leap/observer/refraction/domain policies; execute risk-ranked partitions; add source-derived and genuinely independent production/reference cases across dates and locations; justify correlations/distributions; then obtain named astronomy-expert and supervisor approval of per-operation bounds and thresholds |
| DATA-SRC-001 | For selected source I/311: original acquisition URL/timestamp or other transport-authenticity evidence, explicit raw/derived redistribution permission, and row-level review of the proposed allowlist's actual solution/multiplicity/quality evidence | `OPEN`; Milestone 2B closes only the local parser contract | Licence clarification plus reviewed acquisition/provenance and row-review records. The field, null/duplicate, candidate-scope, sorting, schema, checksum, local-use, and fail-closed tracking policies are defined in Milestone 2B; create a tracked manifest only when the scaffold guard is intentionally activated. |
| DATA-SRC-002 | Official JSON Schema Draft 2020-12 Core/Validation version pins and runtime validator decision | `PARTIAL`: official Core/Validation sources and schema dialect are pinned. Batch 01 uses a tested fail-closed local validator only for the exact keywords in its three experiment schemas; unsupported keywords/non-local references fail. This is not full meta-schema conformance or a production/browser validator choice. | Select and justify any general runtime validator; record exact version/vocabularies/reference/format policy; run official/meta-schema conformance and production-boundary tests before closing the broader decision |

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
