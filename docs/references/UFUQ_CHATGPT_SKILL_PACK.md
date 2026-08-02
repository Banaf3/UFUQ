# UFUQ ChatGPT project skill pack

## Use

Apply only the skill matching the affected claim. Before using any skill, consult
`UFUQ_SOURCE_REGISTER.md` for source authority and limits and `SOURCE_GAPS.md` for
missing evidence. Classify conclusions as:

- `SOURCE_SUPPORTED_FACT`
- `PROJECT_DECISION`
- `PROVISIONAL_CHOICE`
- `UNRESOLVED_QUESTION`

Never infer a missing coordinate, catalogue value, cultural mapping, tolerance, BKT
parameter, or approval. A missing source blocks only its affected claim.

The detailed knowledge base is in `READING_PLAN.md`, `studies/`, and `syntheses/`.
Each repository skill's `references/traceability.md` maps its mandatory rules to that
knowledge base, project decisions, experiments, human-review requirements, or stop
conditions. Use the concise rules below when uploading this pack; consult the register
and gaps rather than embedding source text.

## Engineering quality

**Trigger:** architecture, package boundaries, CI/test gates, reproducibility,
maintainability, or engineering evidence.

**Do not trigger:** scientific, geodesic, or cultural fact validation.

**Procedure:** name the quality attribute or dependency failure; inspect the actual
graph/configuration; run reproducible commands; prove pure-domain and runtime/tool
boundaries; require fail-closed active suites and independent scientific references;
compare change-versus-keep risk. Do not redesign because an architecture book presents
another pattern.

**Output:** claim/scope, classified evidence, severity findings, exact commands/results,
stop conditions, smallest justified correction, gate impact.

## Astronomy validation

**Trigger:** celestial frames, catalogue epoch, time scales, observer model, proper
motion, Earth orientation, horizon/refraction/visibility, angular comparisons, or
independent astronomy fixtures.

**Do not trigger:** catalogue acquisition alone, Qibla geodesy, or cultural approval.

**Procedure:** explicitly record frames, epoch, time/scale, observer datum/height,
units, motion, refraction, IERS provenance/offline policy, supported range, and
singularities. Use a pinned independent Python/Astropy oracle that imports no UFUQ
production package. Compare angularly, build an error budget, and derive—not invent—the
tolerance.

**Output:** conventions, oracle independence, per-case expected/actual/angular
difference, error budget, classified evidence, gaps, and exact claim verdict.

## Catalogue provenance

**Trigger:** catalogue acquisition, checksums, parsing, normalization, schemas,
deterministic artifacts, licensing, and generated-data provenance.

**Do not trigger:** coordinate transformations, cultural approval, or unrelated DTOs.

**Procedure:** enforce:

`source -> acquisition manifest -> ignored raw bytes -> checksum verification ->
parsing -> normalization -> runtime schema validation -> deterministic serialization ->
generated artifact and provenance`

Use official catalogue metadata for fields/units/nulls/frame/epoch. Never copy
coordinates manually or mix cultural content into numerical rows. Serialize explicitly
as UTF-8/LF with deterministic ordering and numeric rules. FAIR is guidance only;
formal PROV semantics are optional.

**Output:** acquisition record, field mapping, input/tool/schema/output hashes,
repeat-build result, referential integrity, licence limit, classified evidence, and
stop condition.

## Qibla geodesy

**Trigger:** observer/destination geodetic coordinates, spherical or ellipsoidal
inverse geodesics, bearing conventions, degenerate cases, and numerical Qibla
references.

**Do not trigger:** general celestial transformations or historical interpretation.

**Procedure:** record both points' sources/datums/precision; stop unless the Kaaba
destination coordinate and datum are approved. Name the model and inverse-geodesic
conventions. Distinguish True North, magnetic north, Polaris, and Qibla. Use independent
reference cases, wrapped circular differences, difficult cases, and a measured
tolerance. Karney supplies algorithms, not UFUQ's destination coordinate; King is
historical context only.

**Output:** geodetic inputs, conventions, per-case comparisons, classified evidence,
stop condition, and scoped verdict.

## Najdi and Arabian sky evidence

**Trigger:** Arabic names, translations, pattern membership, historical/regional
classification, cultural guidance routes, and human cultural review.

**Do not trigger:** numerical catalogue rows, astronomy calculations, modern Qibla
geodesy, or non-cultural synthetic route tests.

**Procedure:** classify every atomic claim as `OLD_ARABIAN`, `NAJDI_TRADITION`,
`GRECO_ARABIC_SCHOLARLY`, `CROSS_REGIONAL_ARABIAN`, or `MODERN_PEDAGOGICAL`. Record
exact Arabic, transliteration, translation, edition/page/verse/folio, period,
geographical scope, modern catalogue-ID evidence, conflicts, evidence status, and human
review. Never classify `NAJDI_TRADITION` without explicit Najdi evidence. No automated
output approves cultural content.

**Output:** atomic claim record, classification, textual/regional evidence, modern
identification, conflicts, separate evidence/human-review statuses, allowed use, and
stop condition.

## Cross-skill boundaries

- Astronomy plus catalogue work may activate both skills: provenance establishes the
  inputs; astronomy validates transformations.
- Qibla geodesy plus astronomy may activate both only when a lesson connects a
  terrestrial bearing to celestial guidance. Keep the calculations and evidence
  separate.
- Cultural content may reference catalogue IDs, but catalogue integrity is not cultural
  approval and cultural review is not numerical provenance.
- Engineering quality may review any workflow's reproducibility without becoming the
  scientific or cultural authority.
- Do not create BKT, 3D interaction, security, or participant-research skills until the
  corresponding source gaps are closed.
