# Phase 0 reference-PDF study and grounded skills

## Purpose and user-visible outcome

Study the verified local UFUQ references deeply enough to produce source-specific
dossiers, cross-source syntheses, and five operational project skills whose mandatory
rules have explicit evidence bases. This is documentation and agent guidance only; it
does not start the astronomy/data technical spike or select production scientific or
cultural values.

## Classification and authority

- Project constraints: `AGENTS.md`.
- Architecture and phase decisions: `docs/ARCHITECTURE.md`,
  `docs/IMPLEMENTATION_DECISIONS.md`, `docs/PHASES.md`, and `docs/TEST_PLAN.md`.
- Domain constraints: `docs/ASTRONOMY_SPEC.md`, `docs/DATA_STRATEGY.md`, and
  `docs/TUTORING_BKT_SPEC.md`.
- Source authority/limits: `docs/references/UFUQ_SOURCE_REGISTER.md` and
  `docs/references/SOURCE_GAPS.md`.
- All new rules remain source facts, proposed project rules, experiment requirements,
  human-review requirements, or unresolved stop conditions; this plan approves none.

## Progress

- [x] 2026-07-24 — Verified scope, current worktree, local inventory, and skill-creator
  instructions.
- [x] 2026-07-25 — Created and reviewed the source reading plan and twenty source
  dossiers.
- [x] 2026-07-25 — Created and reviewed five cross-source syntheses.
- [x] 2026-07-25 — Added source-derived traceability to the five active skills.
- [x] 2026-07-25 — Validated coverage, citation plausibility, copyright limits, scope,
  repository safety, and all Phase 0 commands.

## Surprises and discoveries

- The local JSON-named PDF is an ISO 20022 transformation paper, not the JSON Schema
  Draft 2020-12 specification; the official Core and Validation specifications require
  their own dossier.
- The local Karney PDF is the 2012 arXiv v2 preprint corresponding to the 2013 journal
  article, not the publisher PDF.
- The Explanatory Supplement has no reliable text layer, so only targeted visual study
  is permitted and deep claims remain unresolved.

## Decision log

- 2026-07-24 — `PROJECT_DECISION`: keep all source study notes concise, paraphrased,
  and tracked while local source bytes remain ignored. Reason: reproducible procedural
  knowledge without redistributing copyrighted material.
- 2026-07-24 — `UNRESOLVED_QUESTION`: do not promote any catalogue, tolerance, Kaaba
  coordinate, cultural mapping, or BKT value through this study.

## Outcomes and retrospective

Twenty source dossiers and five cross-source syntheses now ground the five operational
skills. Detailed coverage is current-phase scoped rather than page-count based.
Explanatory Supplement detail remains unusable; Ibn Qutaybah and Kunitzsch remain
partial because of edition/OCR/translation limits. No catalogue, tolerance, Kaaba
coordinate, cultural mapping, or Phase 1 implementation value was approved.

Validation on 2026-07-25 passed:

- five `quick_validate.py` skill checks and mandatory-workflow traceability counts;
- `npm ci` (306 packages);
- `npm run check` including formatting, lint, typecheck, eight-workspace boundaries,
  and ignored/untracked raw-data verification;
- `npm run test` (one file/one test);
- `npm run build`;
- `npm run exports:check` (13 paths across seven importable workspaces); and
- `npm run test:e2e` (one Chromium web/API health smoke).

Tracking scans found no staged file, PDF, local-reference file, raw catalogue byte,
secret, build output, or compiler state. No application/domain/tool source changed.

## Context and orientation

The current repository is a validated eight-workspace Phase 0 scaffold. The source
library is ignored under `local-reference/`; raw catalogue candidates are ignored under
`data/raw/`. Tracked study outputs belong only in `docs/references/`, and operational
skills belong in `.agents/skills/`.

## Dependencies and manual inputs

- Verified local inventory and checksums in ignored `local-reference/` files.
- Reliable text layers or targeted visual inspection.
- Exact source locations for every derived factual/technical rule.
- Human Arabic/cultural review remains missing.
- Pinned Astropy/PyERFA/IERS-data policy, production catalogue selection, numerical
  tolerances, and Kaaba coordinates remain missing.

## Scope guard

Do not implement code, parsing, calculations, cultural mappings, UI behavior, or Phase
1 tests. Do not read or summarize the restricted FYP report. Do not copy long source
passages. Stop a claim when its location, edition, translation, or authority is
unverifiable.

## Milestones and implementation narrative

1. Build `docs/references/READING_PLAN.md` with source identity, relevant units,
   priority, text accessibility, and deliberate exclusions.
2. Build one dossier per external source under `docs/references/studies/`.
3. Compare authority, agreements, conflicts, project choices, experiments, and human
   review in five files under `docs/references/syntheses/`.
4. Keep each `SKILL.md` operational; link detailed studies/syntheses from
   `source-notes.md` and map mandatory rules in `traceability.md`.
5. Record per-source and per-skill status in
   `docs/references/PDF_KNOWLEDGE_COVERAGE.md`.

## Commands

Run from the repository root:

```text
git status --short
git diff --check
npm ci
npm run check
npm run test
npm run build
npm run exports:check
npm run test:e2e
```

Use the skill-creator `quick_validate.py` with UTF-8 mode for each skill.

## Validation and acceptance

- Every mandatory skill rule maps to a dossier/source location, project decision,
  experiment requirement, or unresolved stop condition.
- Citation locations are syntactically plausible and do not exceed verified source
  extents.
- Historical sources are not implementation standards and Arabian evidence is not
  relabelled Najdi.
- No tolerance, Kaaba coordinate, or catalogue coordinate is introduced.
- No PDF/raw/secret/generated output is tracked or staged.
- Application/domain source files are unchanged and Phase 0 commands pass.

## Idempotence, rollback, and recovery

All deliverables are Markdown. Reruns update the same stable paths. Local PDFs and raw
data are never rewritten. Partial dossiers are marked partial rather than discarded.
Rollback consists of reverting only the documentation/skill files listed by Git; do not
reset or delete unrelated user work.

## Risks and safeguards

- False precision from PDF page numbering: label PDF versus printed pages and use
  section/routine identifiers where possible.
- OCR or translation error: mark uncertainty and require visual/human review.
- Copyright over-copying: paraphrase and keep exact excerpts to atomic names or terms.
- Authority inversion: preserve the source hierarchy in each synthesis and skill.
- Scope creep into Phase 1: retain experiment and decision tags without implementation.

## Evidence for the thesis

Retain the tracked reading plan, dossiers, syntheses, skill traceability, coverage
report, exact validation commands/results, dirty-state file list, and local inventory
hash result. Do not retain source bytes, raw catalogue bytes, restricted-report text,
secrets, or personal data in tracked evidence.
