# UFUQ PDF knowledge coverage

**Assessment date:** 2026-07-25

## Measurement rule

Coverage is the number of identified current-phase relevant units studied divided by
the identified current-phase relevant units. A unit is a chapter group, standard
section group, routine family, catalogue metadata group, paper section group, or
claim-specific cultural entry named in `READING_PLAN.md`. It is not the percentage of
all book pages read.

This makes the percentage reproducible without suggesting that unrelated chapters were
studied. Coverage and reliability are separate: a source can have all targeted units
inspected but remain `SOURCE_STUDY_PARTIAL` because its edition, OCR, translation, or
provenance is inadequate.

## Source coverage

| Source/dossier | Extent | Relevant units studied | Locations studied | Skipped relevant material | Access and confidence | Claims/rules derived | Status |
|---|---:|---:|---|---|---|---|---|
| SOFA 2023-10-11 | 379-page manual plus source | 16/16, 100% | Release/introduction and 16 named astrometry, time, Earth-attitude, horizon, motion, geodesy, and refraction routine groups | None for the declared catalogue-to-horizon preparation scope; unrelated routine families excluded | Searchable source/manual; high confidence in routine contracts | 11 trace items; astronomy input, status, convention, and experiment rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| IERS TN36 | 180 PDF pages | 7/7, 100% | Intro; Chs. 1, 2, 4, 5; Ch. 10 §10.1; glossary | High-frequency/station/geophysical terms require later study only if a measured scope needs them | Searchable; high confidence in cited printed pages/equations | 11 trace items; frame, time, EOP, transform-direction, and update-version rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Fundamental Astronomy 6e | 548 PDF pages | 7/7, 100% | Ch. 2 §§2.3-2.5, 2.9-2.10, 2.12-2.15 | Deeper pedagogical examples and all unrelated astronomy chapters | Searchable; medium-high confidence, explanatory authority only | 8 trace items; conceptual-stage and azimuth-conflict rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Explanatory Supplement 3e candidate | 716 PDF pages | 0/4, 0% detailed units | Cover/title/contents/index signals and official USNO scope only | All detailed frame, time, apparent-place, and refraction material | `TEXT_UNAVAILABLE`, incomplete/provenance unverified; no claim-level confidence | 5 limitation/stop trace items; no technical rule | `SOURCE_UNUSABLE` |
| ESA Hipparcos 1997 Volume 1 | 586 PDF pages | 7/7, 100% | PDF pp. 3-11; printed pp. 19-34, 94-98, 109-111, and 136 | Photometry, individual rows, catalogue statistics, mission construction, annex detail, and other volumes are outside the focused field-semantics question | Searchable with visual checks for cited symbols; high confidence in original-1997 semantics, acquisition provenance unverified | 9 trace items; model, epoch, unit, `mu_alpha_star`, parallax, and I/311 stop/test rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Hipparcos I/311 ReadMe | Text/HTML | 6/6, 100% | Notice, File Summary, four byte descriptions, all relevant notes/history | Catalogue row values deliberately excluded | Searchable; high confidence in field/note metadata | 10 trace items; acquisition, field, quality, covariance, and stop rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| van Leeuwen I/311 validation | 12 PDF pages | 5/5, 100% | §§1-5, relevant equations, tables, and figures | No row coordinates or downstream science use | Searchable; high confidence, limited by study's own samples | 8 trace items; per-row uncertainty and layered-validation rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Karney geodesics | 12 PDF pages | 7/7, 100% | §§1-5, §7, Tables 1 and 3-6 | Polygon area and gnomonic projection are outside current need | Searchable; high confidence in preprint locations | 8 trace items; inverse, azimuth, difficult-case, and tolerance-stop rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Ibn Qutaybah, Kitab al-Anwa | 92-page derivative | 4/4 targeted units, 100% | Contents/introduction; sections 31-32 and 52-53 using local discovery pointers | Full lunar-station/weather/verse corpus; stable-edition verification | Searchable but edition/completeness/provenance unverified; low-medium confidence | 7 trace items; `OLD_ARABIAN` candidates and hard human/edition gates | `SOURCE_STUDY_PARTIAL` |
| Kunitzsch 1961 | 130 PDF pages | 12/12 targeted units, 100% | Part I A-E and entries 55-57, 96, 107a-b, 136a-c, 148a-149 | Remaining catalogue entries | OCR; page-image/German/Arabic/Greek review required; medium confidence | 7 trace items; layer classification, variants, and negative-mapping rules | `SOURCE_STUDY_PARTIAL` |
| Hafez 2010 | 406 PDF pages | 8/8, 100% | Intro, §2.3, Ursa chapters, §§5.1 and 5.10-5.12, Tables 18/19/24/26 | Remaining 48-constellation catalogue and quantitative analysis | Searchable; high confidence in thesis pointers, mappings still provisional | 7 trace items; Greco-Arabic crosswalk and human-review rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| King 1993 | 358 PDF pages | 7/7, 100% | Preface, Paper I, Papers IX-XIV relevant portions | Prayer-time/crescent/timekeeping studies | OCR; page-image verification needed for quotations; medium-high conceptual confidence | 7 trace items; historical-method distinction and no-modern-coordinate rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| King 1999 | 679 PDF pages | 8/8, 100% | Foreword/prefaces, Ch. 1 relevant units, Ch. 2 §§2.1-2.5, 2.8-2.9 | Full gazetteers, appendices, object catalogue, later map detail | OCR; medium-high conceptual confidence | 8 trace items; method/data/convention limits and historical-map prohibition | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| JSON Schema Core/Validation 2020-12 | Official HTML, no fixed pages | 8/8, 100% | Core §§4.2-13; Validation §§1-10 and App. A, scoped by `READING_PLAN.md` | Hypermedia detail, every format, Relative JSON Pointer | Official searchable HTML; high confidence in section pointers | 10 trace items; dialect, vocabulary, reference, composition, output, and validator-experiment rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| ISO 20022 JSON generation 2025 | 49 PDF pages | 1/1 identity/scope unit, 100% | Title/status/contents/Foreword/Introduction/§§1-5 opening, pp. 1-7 | Financial transformation rules pp. 8-49 intentionally irrelevant | Searchable; high confidence that it is not UFUQ authority | 5 trace items; non-authority guard only | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| PROV Semantics 2013 | 33 PDF pages | 4/4, 100% | Abstract/Status, §§1-3.5, §4 organization | Formal clauses, constraints, proofs, reasoning | Searchable; high confidence, optional authority only | 6 trace items; terminology/explicit-derivation and no-formal-PROV rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| FAIR 2016 | 9 PDF pages | 5/5, 100% | pp. 1-5, Box 2, conclusion p. 7 | Domain examples/references | Searchable; high confidence, guidance only | 7 trace items; ID/metadata/licence/provenance prompts and no-compliance rule | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Software Architecture in Practice 4e | 460 PDF pages | 7/7, 100% | §§1.3, 3.2-3.5, 12.1-12.2 partial, 21.1-21.2, 21.6-21.7, 22.7 | Tactic catalogues/full ATAM until a demonstrated risk requires them | Searchable; high confidence, general guidance only | 8 trace items; quality-scenario, proportional review, and rationale rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Best Practices for Scientific Computing | 7 PDF pages | 6/6, 100% | pp. 1-6 | Bibliography/author detail | Searchable; high confidence, recommendations not standard | 7 trace items; reproducibility, authority, layered-test rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Good Enough Practices | 20 PDF pages | 7/7, 100% | pp. 2-11, 14-15, 18-19 | Manuscript workflow | Searchable; high confidence, proportional guidance | 7 trace items; raw/acquisition, transform, stable-key, VCS/CI rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |
| Testing Scientific Software | 30-page local preprint | 6/6, 100% | Abstract; §§1-3.4, 4.1-4.4; conclusion opening | Full primary-study/quality tables and references | Searchable; high confidence in preprint pointers, literature cutoff noted | 7 trace items; oracle limits, layered evidence, boundary, and tolerance-experiment rules | `SOURCE_STUDY_COMPLETE_FOR_CURRENT_PHASE` |

## Skill-rule coverage

Counts below cover numbered mandatory workflow rules. Categories overlap because one
rule can be grounded in both a source and a project decision and can also require an
experiment or human approval.

| Skill | Mandatory rules | Exact-source grounded | Project-decision grounded | Experiment dependent | Human-review dependent | Unresolved stop-dependent | Unsupported |
|---|---:|---:|---:|---:|---:|---:|---:|
| `ufuq-engineering-quality` | 9 | 7 | 6 | 0 | 0 | 1 | 0 |
| `ufuq-astronomy-validation` | 9 | 8 | 9 | 4 | 0 | 4 | 0 |
| `ufuq-catalogue-provenance` | 8 | 8 | 8 | 2 | 0 | 3 | 0 |
| `ufuq-qibla-geodesy` | 9 | 7 | 9 | 3 | 0 | 4 | 0 |
| `ufuq-najdi-arabian-sky` | 8 | 4 | 7 | 0 | 6 | 4 | 0 |

Each `references/traceability.md` also maps the skill's stop conditions and prohibited
assumptions. A rule without one of the permitted bases is not retained.

## Cross-source validation result

- Historical sources are not used as modern geodesic or catalogue specifications.
- General Arabic/Arabian/Islamic evidence is not relabelled `NAJDI_TRADITION`.
- No proposed numerical tolerance is marked validated.
- No Kaaba coordinate or catalogue coordinate was introduced.
- Original-1997 `mu_alpha_star` evidence is not relabelled as a confirmed I/311 field
  definition.
- No local PDF is a required fallback for an unavailable fact; source absence narrows
  or stops the claim.
- Detailed Explanatory Supplement knowledge remains unresolved rather than inferred.

## Remaining limitations

- Coverage percentages do not measure source authenticity, translation quality, or
  legal acquisition provenance.
- The Astropy/PyERFA/IERS-data environment and official Astropy documentation remain
  unpinned and therefore were not studied as a versioned oracle source.
- The current cultural source set cannot close Najdi, Arabic-human-review, exact
  membership, line-segment, or instructional-route approval.
- Source study alone does not approve a project catalogue choice, runtime astronomy
  model, Qibla destination, schema validator, numerical tolerance, or learner-facing
  content. The separate project decision selecting I/311 for the Phase 1 local spike
  does not change those source-evidence limits.
