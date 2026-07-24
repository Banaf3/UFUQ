# UFUQ repository-skill validation

**Validation date:** 2026-07-24

## Method

The five repository-scoped skills were checked with the skill-creator validator, a
directory/front-matter assertion, a required-file assertion, metadata-only prompt
classification by an independent subagent, mandatory-rule traceability assertions, and
repository scope/tracking scans.

The independent prompt test read only each YAML `name` and `description`; it did not
read the skill bodies or receive expected answers. This tests whether the descriptions
are narrow enough for implicit selection. It is not evidence that every Codex client
supports dynamic project-skill discovery.

## Structural validation

| Skill | Front matter | Directory/name | Required references | Description scope |
|---|---|---|---|---|
| `ufuq-engineering-quality` | PASS | PASS | PASS | Engineering architecture, boundaries, reproducibility, and test evidence only |
| `ufuq-astronomy-validation` | PASS | PASS | PASS | Celestial coordinate/time/observer and independent astronomy validation only |
| `ufuq-catalogue-provenance` | PASS | PASS | PASS | Catalogue acquisition-to-artifact provenance only |
| `ufuq-qibla-geodesy` | PASS | PASS | PASS | Modern Qibla geodesy and numerical reference cases only |
| `ufuq-najdi-arabian-sky` | PASS | PASS | PASS | Arabic/Arabian/Najdi cultural claim evidence only |

“Required references” now means `source-notes.md`, `review-checklist.md`,
`output-template.md`, and `traceability.md`.

The skill-creator check passed for all five with UTF-8 mode enabled:

```powershell
$env:PYTHONUTF8='1'
python <skill-creator>/scripts/quick_validate.py <skill-directory>
```

Windows UTF-8 mode is required because the cultural/geodesy skills intentionally use
Arabic transliteration characters. Without it, the validator's host-default CP1252
reader fails before parsing YAML; that is a validator-environment issue, not invalid
front matter.

## Activation tests

| Skill | Prompt that should activate | Result | Nearby prompt that should not activate | Result |
|---|---|---|---|---|
| `ufuq-engineering-quality` | “Review whether splitting another UFUQ npm workspace improves maintainability and CI evidence.” | PASS: engineering skill only | “Fix a typo in a React health-screen heading.” | PASS: no skill |
| `ufuq-astronomy-validation` | “Validate ICRS catalogue-epoch propagation to a UTC observer scenario against Astropy fixtures.” | PASS: astronomy skill only | “Decide how the catalogue download manifest should record SHA-256 and null-field normalization.” | PASS: catalogue skill, not astronomy |
| `ufuq-catalogue-provenance` | “Check that two catalogue builds serialize identical UTF-8/LF bytes and provenance hashes.” | PASS: catalogue skill only | “Add a generic synthetic LessonRoute schema test with no cultural labels or claims.” | PASS: no domain skill |
| `ufuq-qibla-geodesy` | “Verify an ellipsoidal Qibla bearing for an approved observer and destination datum, including near-antipodal cases.” | PASS: Qibla skill only | “Summarize medieval qibla-map history without calculating a modern direction.” | PASS: no active skill |
| `ufuq-najdi-arabian-sky` | “Classify whether an Arabic star name is specifically Najdi and prepare its human-review evidence.” | PASS: cultural skill only | “Change the CSS color of the API health badge.” | PASS: no skill |

An additional prompt about an acquisition manifest, SHA-256, and normalization selected
only `ufuq-catalogue-provenance`. A deterministic-catalogue-build prompt could also
justify `ufuq-engineering-quality` if broadened into a system-wide quality-gate review;
the narrow prompt correctly selected only the catalogue skill.

## Overlap rules

| Overlap | Resolution |
|---|---|
| Catalogue provenance and astronomy validation | Catalogue skill proves input/field/artifact provenance; astronomy skill proves transformations and scientific disagreement. |
| Astronomy validation and Qibla geodesy | Use both only when a task connects a terrestrial Qibla bearing to celestial guidance; keep coordinate pipelines and evidence records separate. |
| Catalogue provenance and Arabian-sky evidence | Catalogue skill proves numerical IDs/rows; cultural skill proves names, identification, membership, region, and review. Neither implies the other. |
| Engineering quality with any domain skill | Engineering skill may audit reproducibility/boundaries but cannot supply scientific or cultural authority. |
| Historical qibla and modern geodesy | The active Qibla skill is modern numerical geodesy. Historical interpretation alone does not activate it. |

No BKT/adaptive-scaffolding, 3D-interaction, security, persistence, or participant-study
skill was created because `SOURCE_GAPS.md` records inadequate source support.

## Source-derivation validation

Each `SKILL.md` reads one matching synthesis and its local
`references/traceability.md`. The traceability files map every numbered mandatory
workflow rule plus the important stop/prohibition rules to an exact dossier location,
an approved project decision, an experiment requirement, a human-review requirement,
or an unresolved stop condition.

| Skill | Numbered workflow rules | Traceability rows for those rules | Unsupported rules |
|---|---:|---:|---:|
| `ufuq-engineering-quality` | 9 | 9 | 0 |
| `ufuq-astronomy-validation` | 9 | 9 | 0 |
| `ufuq-catalogue-provenance` | 8 | 8 | 0 |
| `ufuq-qibla-geodesy` | 9 | 9 | 0 |
| `ufuq-najdi-arabian-sky` | 8 | 8 | 0 |

The activation descriptions did not broaden during source derivation. The positive and
nearby-negative prompts above therefore remain valid; the astronomy, catalogue,
geodesy, and cultural descriptions still hand adjacent work to the narrower matching
skill or to no domain skill.

## Source-absence and copyright checks

- Every skill consults `UFUQ_SOURCE_REGISTER.md` and the relevant gaps before making a
  source-dependent claim.
- Every skill consults its synthesis and traceability file before treating a mandatory
  rule as binding.
- Each skill has a stop condition for absent, unusable, unverified, or unpinned
  evidence; none instructs the agent to reconstruct facts from memory.
- Local PDF paths are not required inputs to ordinary skill activation. Missing PDFs
  narrow or stop the affected claim rather than causing invention.
- Skill/reference files contain concise original procedural notes, not copied textbook
  passages or long quotations.
- Tracked documents contain bibliographic citations and page/section pointer rules, not
  restricted source text.

## Repository-scope result

- All referenced tracked project files existed at validation time.
- No application or domain source file was changed by this reference-library task.
- No PDF, `local-reference` file, raw catalogue byte, secret, build output, or
  `*.tsbuildinfo` file was added to the proposed tracked set.

SKILL_VALIDATION: PASS
