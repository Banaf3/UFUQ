---
name: ufuq-najdi-arabian-sky
description: Prepare evidence records for UFUQ Arabic star names, Arabian sky-pattern membership, historical classifications, and culturally claimed guidance routes, with explicit Najdi-evidence and human-review gates. Use for cultural-content research or validation; do not use for numerical catalogue parsing or approve any mapping automatically.
---

# UFUQ Najdi Arabian Sky

Trace each cultural claim to its actual period and region. This skill prepares evidence;
it never grants cultural approval.

## Trigger conditions

Use this skill when a task concerns:

- Arabic star/pattern names, transliteration, translation, membership, line segments,
  oral or textual provenance, or culturally framed lesson routes;
- whether evidence is old Arabian, specifically Najdi, Greco-Arabic scholarly,
  cross-regional, or a modern pedagogical construction;
- human Arabic/cultural review records and conflicts between cultural sources.

Do not trigger it for:

- numerical catalogue acquisition or coordinate rows; use
  `ufuq-catalogue-provenance`;
- coordinate/time calculations or star visibility; use
  `ufuq-astronomy-validation`;
- modern Qibla geodesy; use `ufuq-qibla-geodesy`;
- generic synthetic route-schema tests that make no cultural claim.

## Required project files

Read `AGENTS.md`, `docs/DATA_STRATEGY.md`, `docs/IMPLEMENTATION_DECISIONS.md`,
`docs/PHASES.md`, the cultural-content sections of `docs/ARCHITECTURE.md`,
`docs/governance/OPEN_QUESTIONS.md` when formal approval is in scope,
`docs/references/UFUQ_SOURCE_REGISTER.md`,
`docs/references/SOURCE_GAPS.md`,
`docs/references/syntheses/arabian-sky-evidence-synthesis.md`, and this skill's four
reference files. Open only the study dossiers linked for the affected rule by
`references/traceability.md`. Read only the exact local source pages needed for the
claim and never copy long passages into tracked files.

## Source authority order

Authority depends on the classification claimed:

1. Explicit Najdi primary/regional evidence and documented human Arabic/cultural
   review for `NAJDI_TRADITION`.
2. Ibn Qutaybah for claim-specific `OLD_ARABIAN` evidence.
3. Kunitzsch for philological classification and source-conflict analysis.
4. Hafez/al-Ṣūfī for `GRECO_ARABIC_SCHOLARLY` crosswalks.
5. King for Islamic-astronomy historical context.
6. A clearly labelled project decision for `MODERN_PEDAGOGICAL` constructions.

No source moves upward in this order because it uses Arabic or discusses Arabia.

## Mandatory workflow

1. State one atomic claim: exact name, membership edge, line segment, cultural
   association, or instructional relationship.
2. Assign exactly one evidence classification:
   `OLD_ARABIAN`, `NAJDI_TRADITION`, `GRECO_ARABIC_SCHOLARLY`,
   `CROSS_REGIONAL_ARABIAN`, or `MODERN_PEDAGOGICAL`.
3. Record the exact Arabic text, transliteration system/output, original translation or
   cited translation, source page/verse/folio, edition, period, and geographical scope.
   If the local edition or text layer is unverified, record that limitation and stop
   page-dependent approval.
4. Map referenced objects to modern catalogue IDs only through a separate evidence
   argument. Keep coordinates in catalogue data and cultural claims in curation.
5. Record conflicts, alternate readings/names, uncertain identifications, and whether
   a line or route is historical evidence or modern pedagogy.
6. Record evidence status and human-review status separately. No automated result or
   Codex output is cultural approval.
7. For `NAJDI_TRADITION`, require explicit Najdi evidence and human review. Ibn
   Qutaybah, Kunitzsch, Hafez, or King alone is insufficient.
8. Confirm every mandatory conclusion has a basis in
   `references/traceability.md`, then report using
   `references/output-template.md`; unresolved claims remain excluded from
   learner-facing content.

## Required evidence

- Exact Arabic and claim-level page/verse/folio in a verified edition.
- Transliteration, translation, period, and geographical scope.
- Modern catalogue-ID identification argument and uncertainty.
- Conflicting sources/readings and classification rationale.
- Evidence status plus named human review role/date/status.
- Separate citations for historical claim, modern identification, and instructional
  route when they are different claims.

## Stop conditions

Stop learner-facing use when the edition, relevant text, location pointer, translation,
geographical scope, modern identification, conflict resolution, or human review is
missing. Stop any `NAJDI_TRADITION` claim without explicit Najdi evidence. Local PDF
absence or unusable text must produce an evidence gap, never a reconstructed claim.

## Prohibited assumptions

An Arabic name is not automatically ancient Arabian, Bedouin, or Najdi. Do not infer
Najdi use from pan-Arabian, Islamic, Greco-Arabic, or modern material. Do not invent
Arabic spelling, transliteration, translation, membership, line segments, catalogue
IDs, or route meanings. Do not approve any cultural mapping.

## Required output

Use `references/output-template.md`. Include the classification, evidence and review
statuses, exact source pointer, conflicts, and allowed use. Distinguish
`SOURCE_SUPPORTED_FACT`, `PROJECT_DECISION`, `PROVISIONAL_CHOICE`, and
`UNRESOLVED_QUESTION`.

## Relevant validation commands

Use the relevant checks after real curation records exist:

```text
npm run data:verify
npm run test
npm run check
```

Run schema and referential-integrity checks for curation without treating them as
cultural approval.
