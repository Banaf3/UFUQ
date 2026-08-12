# Data strategy

## Principle

Scientific measurements, cultural interpretation, visual relationships, pedagogy, and deployable artifacts are different data classes. They have different authorities and review gates and must not be merged into an untraceable hand-edited JSON file.

## Data classes

| Class | Contents | Authority | Repository policy |
|---|---|---|---|
| 1. Numerical astronomical catalogue | Stable UFUQ `starId`; source-release crosswalk; catalogue astrometry and reference epoch; the approved space-motion, photometric, uncertainty/covariance and quality fields or a reviewed omission rationale | Approved catalogue/table/version AST-001 | Acquisition output is immutable; commit only if licence permits; changing source releases does not change cultural identifiers |
| 2. `SkyPattern` curation | Stable pattern ID; names/cultural labels; member UFUQ `starId` values; ordered line-segment endpoint IDs; citations; cultural-review status/version | Ilm al-Falak/cultural expert AST-002 or the applicable reviewed-content record | Human-reviewed YAML/JSON; no coordinate duplication or catalogue-specific foreign keys; not limited to one named pattern |
| 3. `GuidanceRelationship` curation | Stable relationship ID; source pattern/star; target pattern/star/direction; type; instructional line/vector; explanation; applicable scenarios; citations; verification status/version | Applicable cultural, astronomy, and education reviewers | Human-reviewed and referentially validated; exact helper relationships remain provisional |
| 4. `LessonRoute` and educational metadata | Ordered relationship/learning steps; prerequisite skills; allowed alternative paths; scaffold-configuration reference; KC/task/cue/misconception metadata; route status/version | Supervisor/learning expert plus the underlying content authorities | Versioned reviewed content separate from scientific rows; no hardcoded Banat Na'sh-first flow |
| 5. Generated runtime JSON | Minimal joined projection needed by browser: normalized numeric fields, approved labels/edges/metadata, schema and versions | Deterministic build from 1–4 | Never hand-edit; generated header/manifest/checksum required |

Operational learner data is governed by `governance/SECURITY_AND_PRIVACY.md` and is not part of the catalogue pipeline.

## Physical ownership

- `packages/catalogue-schema/src/catalogue/` owns numerical serialized-row schemas and
  framework-free validators.
- `packages/catalogue-schema/src/content/` owns serialized `SkyPattern`,
  `GuidanceRelationship`, and `LessonRoute` shapes/validators; human-reviewed source
  records themselves live under `data/curation/`.
- `packages/catalogue-schema/src/artifact/` owns the generated artifact envelope,
  manifest, version, and checksum schema.
- `data/manifests/` tracks provenance, licence, query, selection, and expected hashes.
- `data/raw/` contains immutable acquired bytes locally and is ignored by default.
- `data/curation/patterns/`, `relationships/`, and `routes/` keep the three reviewed
  content classes visibly separate.
- `data/generated/` contains deterministic runtime output only when licence and release
  policy permit tracking it.
- `tools/catalogue/src/pipeline/` is an internal module of the single catalogue-tool
  workspace; there is no separate pipeline package.

## Data-driven guidance content

`SkyPattern`, `GuidanceRelationship`, and `LessonRoute` are distinct records so the
system can reuse reviewed patterns and edges in more than one lesson without embedding
cultural claims in code.

- A `SkyPattern` contains its stable ID, names and cultural labels, member UFUQ
  `starId` values, line segments, and cultural-review status. Coordinates and external
  catalogue identifiers remain solely in the numerical catalogue/crosswalk.
- A `GuidanceRelationship` connects a source pattern or star to a target pattern, star,
  or typed direction. It records its relationship type, instructional line/vector,
  explanation, applicable scenarios, and verification status.
- A `LessonRoute` orders learning steps, declares prerequisite skills, lists permitted
  alternative paths, and references scaffold configuration. It composes relationships;
  it does not duplicate their geometry or authority evidence.

The schemas permit helper pattern → Banat Na'sh or Dhat al-Kursi → Al-Jady → True North
→ Qibla routes, including either named pattern as the Al-Jady guide. This expresses a
generic capability only. No helper constellation, mapping, segment, explanation, or
relationship is approved by this structural clarification.

For each scenario, the server resolves a selected route alternative and derives the
union of required UFUQ `starId` values from all referenced patterns, star endpoints, and
instructional geometry. A route is eligible only when every required star is available
under that approved scenario and all content/reference/review constraints pass. Missing
stars make the whole route ineligible; the build/runtime must not silently remove a
relationship or substitute unreviewed content.

## Source and provenance manifest

Before retrieval, create a machine-readable source manifest under `data/manifests/`
containing:

- catalogue name, publisher/archive, catalogue/table ID and release/version;
- canonical metadata/download/query URL, exact selected columns, deterministic culturally-required/context-star subset rules, exclusions, duplicate/component resolution, filters, row-order rule, and units;
- coordinate frame, reference-epoch semantics, proper-motion/parallax/radial-velocity conventions as selected, magnitude band/variability meaning, uncertainties/covariance or exclusion rationale, null and quality-flag interpretation;
- retrieval timestamp in UTC, retrieval tool/version, source citation, licence URL/text identifier, and redistribution determination;
- raw byte SHA-256, normalized table SHA-256, expected row count, and approved reviewer/date.

CDS/VizieR I/311, *Hipparcos, the New Reduction*, is the selected source for the
Phase 1 local technical spike only; it is not thereby UFUQ's permanent production
catalogue. Milestone 2D must approve the first deployed source release, its rights, and
its mapping into stable UFUQ `starId` values. The source-release crosswalk must permit a
reviewed source such as Gaia to coexist with or replace individual astrometric records
without rewriting cultural records. For the existing I/311 spike, use the corrected
author-replacement files recorded on
2008-09-16, with `hip2.dat` as the main table and an exact matching supplement when a
selected `Sn` family requires it. The Phase 1 field, missing/duplicate, solution,
multiplicity, candidate-selection, schema, sorting, and checksum policies are fixed in
`spikes/PHASE1_CATALOGUE_AUTHORITY_PROVENANCE.md`. Acquisition provenance remains
partial and raw/derived redistribution is unresolved, so source-derived output stays
ignored and local. Do not add catalogue rows to Git or deployment storage; the existing
data-scaffold guard is intentionally unchanged.

I/311 `pmRA` is source-defined in Appendix G Table G.3 as `mu_alpha_star`; normalize it
as `properMotionRaCosDecMilliarcsecondsPerYear` and do not apply or remove another
`cos(delta)` factor when supplying Astropy `pm_ra_cosdec`.

## Acquisition and transformation

The future `tools/catalogue` command, introduced only by an ExecPlan, must implement:

```mermaid
flowchart LR
  M[Approved source manifest] --> FETCH[Deterministic fetch/query]
  FETCH --> RAW[Immutable raw snapshot + checksum]
  RAW --> NORMAL[Parse units/nulls/flags; stable sort]
  CURATE[Approved patterns, guidance, routes, education] --> JOIN[Keyed joins by stable IDs]
  NORMAL --> JOIN
  JOIN --> VALIDATE[Schema + scientific + review gates]
  VALIDATE --> JSON[Minimal runtime JSON]
  JSON --> CHECK[Canonical checksum + build manifest]
```

The command verifies transport/result bytes before transformation, fails on source drift unless an explicit update workflow is in progress, and emits a deterministic result for the same inputs/tool version. Coordinates come only from the numerical source—not websites, label files, screenshots, or report diagrams.

Phase 1 uses a minimal production-shaped instance of this same path: approved manifest,
permitted immutable input, normalization, required curation join, schema validation,
canonical serialization, and hash. Phase 2 expands rows and policies; it does not replace
a hand-made Phase 1 fixture with a different provenance mechanism.

## Raw snapshot policy

- Prefer retaining the exact permitted raw source or query result in an access-controlled reproducibility store with immutable checksum.
- Local acquired bytes are written under default-ignored `data/raw/`; a normal Git add
  cannot include them. Any future exception requires an explicit licence/provenance
  decision and ignore-policy change.
- Commit it only when the source licence explicitly permits repository redistribution and the repository audience is compatible.
- If redistribution is unclear or prohibited, commit only manifest, query/acquisition script, expected metadata/checksum where allowed, and citation; an authorized reproducibility store retains the immutable bytes when policy permits. A public fresh checkout can then verify manifests/scripts but cannot honestly claim byte-for-byte regeneration without authorized access.
- Never substitute an undocumented later response under the same version.
- A source update creates a new catalogue version and comparison report; it does not overwrite the old manifest used by historical scenarios.

## Schemas and validation

Schemas reject unknown required semantics and at least verify:

- unique, non-empty UFUQ `starId` values and unique source-release crosswalk keys;
- for the I/311 spike, exactly one main row for every selected HIP and no unrequested
  row in the selected artifact; a required 3/7/9-parameter or VIM supplement resolves
  exactly once;
- finite required astrometric/photometric/uncertainty values and their documented ranges/units; every omitted uncertainty/covariance or space-motion field has an approved error-bound rationale;
- explicit frame/epoch/catalogue version; no mixed frames or epochs in one unlabelled artifact;
- approved handling of missing/flagged astrometry;
- Unicode NFC for Arabic and transliteration text;
- `SkyPattern` records with unique stable IDs, citations, reviewer/date/status, member
  UFUQ `starId` values that resolve to selected numerical rows, and segment endpoints that resolve to
  members; no self/duplicate edge unless explicitly justified;
- `GuidanceRelationship` source/target/geometry references resolve to typed
  pattern/star/direction records and carry applicable-scenario plus verification status;
- `LessonRoute` ordered steps, prerequisites, alternatives, scaffold configuration,
  task/KC/cue references, and relationship versions all resolve;
- scenario-route validation derives every required star and rejects a route when any is
  unavailable under that scenario;
- stable canonical ordering, schema version, generator version, input hashes, and output SHA-256;
- one specified canonical byte representation covering numeric formatting, object-key/row ordering, UTF-8/NFC, newline policy, and excluded volatile metadata.

The build fails if learner-facing pattern/relationship/route content lacks the required
review status, a route/reference is unresolved, a scientific row was edited after
acquisition, a checksum differs, or a coordinate appears only in curation.

## Generated-file policy

Generated JSON is a build artifact with a companion manifest containing input
versions/hashes, schema version, generator version/Git commit, selection evidence,
licence/citation notices, artifact byte length/count, and artifact SHA-256. The v1
canonical form is UTF-8 without BOM, NFC, lexicographic object-key order, stable
`starId` record order, schema-defined order for other arrays, finite shortest-round-trip JSON
numbers with negative zero normalized to zero, and one trailing LF. Volatile
retrieval/review timestamps and machine paths stay outside the canonical payload. Two
builds from identical approved inputs and tool versions must produce identical bytes.
It is committed only after explicit redistribution approval; otherwise it remains in
ignored local or authorized access-controlled storage. Code review changes
source/curation inputs or transformer logic, never generated rows alone.

AST-003 decides whether runtime rows carry catalogue-reference astrometry for runtime
propagation, precomputed scenario-time directions, or both. The browser and API consume
the same generated bytes/hash, validate schema/version/checksum before use, and refuse
scenario issuance/loading on mismatch. Scenario and attempt records store that hash and
the astronomy/EOP/build links needed for the qualified replay claim.

## Licensing and citation

Maintain a licence record per input and per distributed output: rights holder, licence
identifier/link, required attribution, transformation/redistribution conditions,
non-commercial constraints, approval, and display/report citation text. VizieR's
official rules permit scientific-context use and require the original
authors/publication/publisher to be cited; they request VizieR acknowledgement. The
I/311 ReadMe does not grant raw or derived redistribution. ESA's CC licence and credit
terms for the original 1997 catalogue must not be transferred to the later I/311
reduction by inference. Until CDS/data-origin clarification is recorded, classify
I/311 as `LOCAL_USE_ONLY` and every source-derived Git/deployment output as
`REDISTRIBUTION_UNRESOLVED` with `BLOCK_TRACKING_AND_DEPLOYMENT`. A public URL is not
permission to copy.

## Manual review gates

1. **Scientific gate:** catalogue fields, flags, frame, epoch, proper motion, and sample rows reviewed against source metadata.
2. **Cultural gate:** every learner-facing `SkyPattern` name/label, membership, segment,
   and culturally claimed `GuidanceRelationship` approved under AST-002 or its
   applicable reviewed-content record.
3. **Educational gate:** route order/alternatives, prerequisites, KC/task/cue semantics,
   explanations, and scaffold references approved under BKT-004 and the applicable
   learning review.
4. **Licence gate:** raw and generated redistribution approved under AST-001.
5. **Release gate:** deterministic rebuild, schemas, hashes, referential integrity, and visual spot-check pass.

The same reviewer should not silently approve every domain. Review records are versioned inputs, not comments lost in chat.

## Update and reproducibility procedure

1. Open a data-update ExecPlan and new immutable version; record purpose and old hashes.
2. Approve source/licence changes before retrieval.
3. Fetch with the pinned tool/query; retain bytes and hashes according to licence.
4. Produce a machine-readable diff: rows added/removed, changed fields, flags,
   `SkyPattern`, `GuidanceRelationship`, `LessonRoute`, and downstream fixture changes.
5. Re-run all schemas, astronomy reference tests, scene/raycast tests, screenshots, and performance benchmark.
6. Obtain scientific/cultural/educational reapproval for affected records.
7. Publish a new generated hash and scenario policy version. Retain old artifacts needed for audit subject to licence/retention rules.
8. Update research notes, ADR if semantics changed, traceability, risk/status, and final-report evidence index.
