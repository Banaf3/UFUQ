# Phase 0 ESA Hipparcos source integration

## Purpose and user-visible outcome

Integrate the official 1997 ESA Volume 1 guide as focused supporting evidence for
Hipparcos field semantics. The outcome is a verified local record, a traceable dossier,
updated astronomy/catalogue syntheses and skill notes, and a precise Phase 1 test
requirement without starting that spike.

## Classification and authority

- `ESA-HIP-1997-V1` controls statements about the original 1997 catalogue.
- `HIP-I311-README` controls the local CDS I/311 byte layout.
- `VAN-LEEUWEN-2007-VALIDATION` controls its stated new-reduction quality evidence.
- UFUQ project choices remain controlled by `docs/ASTRONOMY_SPEC.md`,
  `docs/DATA_STRATEGY.md`, ADR-004, and ADR-007.
- No catalogue, normalized schema, production algorithm, or tolerance is approved by
  this documentation task.

## Progress

- [x] 2026-07-25 01:40+08:00 — Verified the PDF title/publication/contents, extent,
  text layer, SHA-256, and packaging discrepancy.
- [x] 2026-07-25 01:55+08:00 — Studied the exact astrometric, epoch, proper-motion,
  propagation, and field-guide sections.
- [x] 2026-07-25 — Reconciled the dossier, source register, syntheses, and two skills.
- [x] 2026-07-25 — Ran traceability, citation, formatting, and repository-safety
  validation.

## Surprises and discoveries

- The visible publication is the expected June 1997 ESA SP-1200 Volume 1, while the
  PDF container was assembled in 2007 using pdfsam/iText. The bibliographic identity is
  verified, but acquisition provenance is not.
- ESA explicitly defines original field H12 as `mu_alpha_star`; the available I/311
  ReadMe and validation article do not repeat the cosine definition.

## Decision log

- 2026-07-25 — `SOURCE_SUPPORTED_FACT`: the original 1997 H12 component is
  `mu_alpha_star = mu_alpha cos(delta)` in mas per Julian year.
- 2026-07-25 — `EXPERIMENT_REQUIRED`: classify the I/311 mapping as
  `STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED`, because no studied I/311-specific
  source explicitly supplies the cosine definition.

## Outcomes and retrospective

The focused source is integrated without starting Phase 1. Both skills passed
`quick_validate.py`; their 9 and 8 mandatory workflow rules respectively have matching
traceability rows. Citation validation checked 38 printed-page references, 3 PDF-page
references, and 7 source-text anchors. Prettier, ignore/tracking, checksum, staged-file,
and application/tool-diff checks passed. The PDF and local records remain ignored, and
no file is staged.

## Context and orientation

The repository remains a Phase 0 eight-workspace scaffold. The ESA PDF and local
inventory are ignored. Tracked source knowledge is concise and paraphrased under
`docs/references/`; operational rules live under the two existing skills.

## Dependencies and manual inputs

- Local ESA PDF and its ignored SHA/inventory record.
- Existing I/311 ReadMe and van Leeuwen validation dossier.
- A future pinned Astropy/PyERFA environment and authoritative I/311 semantic
  clarification.

## Scope guard

Do not alter application, domain, catalogue-tool, or astronomy-tool code. Do not parse
catalogue rows, implement propagation, add tests, select a catalogue, or invent a
tolerance. Do not stage a PDF, local inventory, or raw catalogue byte.

## Milestones and implementation narrative

1. Verify and record local identity, access, extent, provenance, and checksum.
2. Create one focused dossier with exact printed-page/section pointers.
3. Compare ESA original semantics with I/311 metadata and validation evidence.
4. Update only the relevant register, plan, matrix, coverage, syntheses, and two skills.
5. Validate traceability, citations, formatting, ignore rules, and code non-modification.

## Commands

Run from the repository root:

```text
git status --short
git diff --check
npm run format:check
python C:/Users/abboud/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/ufuq-astronomy-validation
python C:/Users/abboud/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/ufuq-catalogue-provenance
git check-ignore -v local-reference/catalogues/hipparcos-esa-1997/documentation/volume-1-catalogue-introduction.pdf
git check-ignore -v local-reference/catalogues/hipparcos-esa-1997/README.local.md
```

Use targeted repository scripts/scans for traceability, restricted files, raw data,
generated outputs, and source-code changes.

## Validation and acceptance

- Every new implementation-affecting rule has a source, project-decision, experiment,
  or stop-condition basis.
- All ESA printed-page citations are within the verified 542-page printed body and
  match the studied section.
- The pmRA classification does not claim I/311 confirmation.
- The PDF and local README remain ignored; no raw/PDF/generated/secret file is staged.
- No application or tool code changes are introduced by this task.

## Idempotence, rollback, and recovery

Reruns update stable Markdown paths and local inventory entries. The PDF is read-only.
Rollback is limited to this task's documentation/skill files; unrelated dirty work is
preserved.

## Risks and safeguards

- Mathematical glyph extraction error: use section/equation identifiers and visually
  verify the cited symbol-bearing pages.
- Source conflation: label original ESA catalogue and I/311 new reduction separately.
- Scope creep: retain future tests as documented requirements only.
- Copyright: paraphrase; do not copy long passages or redistribute bytes.

## Evidence for the thesis

Retain the focused tracked dossier, syntheses, skill traceability, exact validation
commands/results, and ignored local checksum record. Do not retain or publish the PDF,
temporary extracted text, raw catalogue rows, secrets, or restricted report text.
