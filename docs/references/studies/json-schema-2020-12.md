# Bibliographic identity

- Canonical source IDs: `JSON-SCHEMA-CORE-2020-12` and
  `JSON-SCHEMA-VALIDATION-2020-12`.
- Titles: *JSON Schema: A Media Type for Describing JSON Documents* (Core) and
  *JSON Schema Validation: A Vocabulary for Structural Validation of JSON*
  (Validation).
- Authors/editors: Austin Wright, Henry Andrews, Ben Hutton, and Greg Dennis
  (Core); Ben Hutton, Austin Wright, Henry Andrews, and Greg Dennis
  (Validation).
- Edition/version: JSON Schema Draft 2020-12, Internet-Drafts
  `draft-bhutton-json-schema-01` and
  `draft-bhutton-json-schema-validation-01`.
- Publication date: 16 June 2022.
- Publisher: JSON Schema project / IETF Internet-Draft publication process.
- Identifier: no DOI or ISBN; canonical dialect meta-schema
  `https://json-schema.org/draft/2020-12/schema`.
- Local file: none. The similarly named local ISO 20022 PDF is not either
  specification.
- Official sources:
  [Core](https://json-schema.org/draft/2020-12/json-schema-core) and
  [Validation](https://json-schema.org/draft/2020-12/json-schema-validation).
- Page count: not applicable to the authoritative HTML; section numbers and
  fragment identifiers are the stable pointers.
- Text access: reliable searchable HTML.
- Verification status: identity and publication date verified against the
  official Draft 2020-12 index. The specifications are the schema-semantics
  authority; a runtime validator and its conformance remain unselected.

# UFUQ relevance

- Phases affected: Phase 1 catalogue/data spike and every later phase that
  consumes versioned catalogue, curation, artifact, or fixture JSON.
- Project decisions affected: `UFUQ-DATA`, `UFUQ-ADR-004`, and the unresolved
  runtime-validator decision `DATA-SRC-002`.
- Sections studied:
  - Core §§4.2.1-4.3.2 (instance data model, schema documents, keyword kinds,
    boolean schemas);
  - Core §§6.2-6.5 (language independence, numbers, regular expressions, and
    extensions);
  - Core §§7.6-7.8 (assertions, annotations, and reserved locations);
  - Core §§8-8.2.4 (Core vocabulary, meta-schemas, `$schema`, `$vocabulary`,
    identifiers, references, and `$defs`);
  - Core §§9.1-9.4 (URI identification, loading, dereferencing, bundling, and
    recursion/reference caveats);
  - Core §§10-12 (applicators, unevaluated locations, and validation output);
  - Core §13 (security considerations);
  - Validation §§1-6 (scope, data-model cautions, meta-schema, and structural
    assertions);
  - Validation §§7-9 (format, content, and metadata vocabularies);
  - Validation §10 (security considerations) and Appendix A (keywords moved to
    Core).
- Sections intentionally not studied in detail: the full hypermedia usage,
  every defined `format`, complete output examples, acknowledgements, change
  logs, and Relative JSON Pointer. They are not needed to establish UFUQ's
  current trust-boundary and validator-selection rules.
- Scope reason: the current-phase need is correct dialect selection, runtime
  validation semantics, diagnostic evidence, and validator conformance—not a
  custom vocabulary or schema implementation.
- Classification: Core and Validation are `CRITICAL_NOW`;
  implementation-specific validator behavior is unresolved and requires a
  separate experiment/decision.

# Terminology

- **Instance**: a JSON value to which a schema is applied; its location is
  addressed with a JSON Pointer (Core §§4.2, 12.3.3).
- **Schema resource**: a JSON Schema with its own base URI, potentially
  embedded in a larger schema document (Core §§4.3, 8.2.1).
- **Dialect**: the set of vocabularies and syntax identified by the
  `$schema` meta-schema URI (Core §8.1.1).
- **Vocabulary**: a named set of keyword semantics; a meta-schema declares
  which vocabularies are required or optional (Core §8.1).
- **Assertion**: a keyword behavior that contributes a boolean validation
  result (Core §4.3.1; Validation §6).
- **Annotation**: information attached to a successfully evaluated instance
  location for application use, without independently asserting validity
  (Core §§4.3.1, 7.7).
- **Applicator**: a keyword that applies subschemas and combines or modifies
  their results (Core §§4.3.1, 10).
- **Meta-schema**: a schema that declares a dialect's vocabularies and
  constrains valid schema syntax (Core §8.1).
- **Validation output unit**: a result carrying validity and, for detailed
  output, schema/keyword and instance locations plus an error or annotation
  (Core §§12.3-12.4).

# Concepts and models

## Data model and equality

Core §4.2.1 defines six primitive instance types: null, boolean, object,
array, number, and string. Objects are unordered mappings; arrays are ordered.
Numbers are mathematical arbitrary-precision base-10 values at the schema
model level. Lexical numeric representation and JSON formatting are outside
schema semantics (Core §§4.2.1-4.2.2). Therefore schema validity cannot prove
UFUQ's byte-level deterministic serialization or a JavaScript implementation's
numeric representability.

## Dialect and vocabulary control

`$schema` identifies both the dialect and its meta-schema. If it is omitted at
the document root, behavior is implementation-defined (Core §8.1.1).
`$vocabulary` is a meta-schema mechanism, not a normal per-instance switch; a
required vocabulary must be understood by a conforming processor (Core
§8.1.2). UFUQ schemas need an explicit Draft 2020-12 dialect declaration, and
the selected validator must demonstrate support for every vocabulary on which
the schemas depend.

## Independent keyword behavior

Keywords normally evaluate independently. A constraint such as `maxLength`
does not itself assert that the instance is a string; a separate `type`
assertion is needed when type exclusion matters (Core §§7.3, 10.1;
Validation §§3, 6). The same principle applies to numerical, array, and object
keywords. Schema tests must include wrong-type cases rather than assuming a
constraint implies its type.

## Unknown keywords and schema misspellings

Unknown or unsupported keywords are generally treated as annotations rather
than assertion failures (Core §§4.3.1, 6.5). A misspelled validation keyword
can therefore make a schema less restrictive without causing the validator to
reject it. Validating schemas against the intended meta-schema and running
negative conformance cases are necessary evidence.

## References and identifiers

`$id` establishes a schema resource's canonical base URI; a root `$id` should
be an absolute URI without a fragment (Core §§8.2.1, 8.2.1.1).
`$anchor` provides a location-independent fragment, while `$dynamicAnchor`
and `$dynamicRef` are advanced dynamic-scope features (Core §§8.2.2-8.2.3).
Dereferencing resolves a reference as a URI-reference against the current base
URI (Core §9.2). Reference URIs do not imply that a validator must download
anything; schemas can be pre-associated with their URIs (Core §9.1.2).

## Object closure and composed schemas

`additionalProperties` is an applicator whose scope is determined by adjacent
`properties` and `patternProperties`; it does not see successful evaluations
performed in a separate branch as a global closure mechanism (Core
§10.3.2.3). `unevaluatedProperties` instead depends on successful annotation
results across applicable adjacent/dynamic-scope subschemas (Core
§§11, 11.3). Selecting either mechanism is a schema-design decision that
requires composition tests.

## `format` is not automatically a hard assertion

Draft 2020-12 separates Format-Annotation and Format-Assertion vocabularies.
Support for annotation is required, but assertion behavior is optional unless
the assertion vocabulary is explicitly required. With annotation semantics,
format checking is disabled by default and may be partial (Validation
§§7.1-7.2). UFUQ cannot rely on `format` alone for a required semantic
constraint without pinning the vocabulary, validator mode, and tests.

## Validation output

Core §12 defines flag, basic, detailed, and verbose result shapes. Beyond a
boolean, diagnostic output can identify keyword-relative location,
absolute keyword location, and instance location. The wording of error
messages is not standardized (Core §12.3.4), so tests should assert structured
locations and validity rather than exact prose unless the chosen library makes
that prose part of UFUQ's own contract.

# Equations and algorithms

## Schema evaluation

- Source location: Validation §3; Core §§7, 10-11.
- Operation: each applicable schema object is evaluated at an instance
  location; assertions contribute validity, applicators control subschema
  application, and annotations are retained only through successful
  evaluations.
- Inputs: schema resource/dialect, instance, reference registry, and enabled
  vocabularies.
- Output: a boolean result and optionally structured annotations/errors.
- Assumptions: the validator correctly supports the declared dialect and all
  required vocabularies.
- Valid domain: values representable in the JSON Schema instance data model.
- Numerical concern: JSON Schema permits arbitrary-precision numbers, while
  the host runtime may not (Core §§4.2.1, 6.2; Validation §4.2).
- UFUQ use: validation of acquisition manifests, normalized records,
  curation records, artifact envelopes, and generated runtime data at trust
  boundaries.
- Independent validation: conformance fixtures must cover accepted and
  rejected cases, schema meta-validation, references, numeric edge cases, and
  the configured `format` behavior.

## Reference resolution

- Source location: Core §§8.2.1-8.2.4 and 9.1-9.4.
- Operation: establish a base URI, resolve `$ref`/`$dynamicRef` as URI
  references, identify a schema resource or anchor, then evaluate it under the
  specified lexical or dynamic scope.
- Inputs/units: URI references and schemas; no physical units.
- Assumptions: URI-to-schema associations are unambiguous and available.
- Numerical concerns: none; recursion and unrecognized nested extension
  locations can produce undefined or unsafe behavior.
- UFUQ use: reuse versioned definitions without copying constraints.
- Required validation: offline resolution tests and failure tests for missing,
  duplicate, or cyclic/unsupported references.

# Conventions

- Declare Draft 2020-12 with the canonical `$schema` URI at each document root
  unless an approved bundling design proves inheritance semantics (Core
  §8.1.1).
- Give reusable root schema resources stable absolute `$id` values without
  fragments (Core §8.2.1.1).
- Treat objects as unordered for schema semantics; deterministic key order is
  a separate serialization convention (Core §4.2.2).
- Treat JSON numbers according to the schema mathematical model while also
  imposing UFUQ's separately approved finite/runtime numeric policy.
- Treat regular expressions as Unicode-aware and unanchored unless `^` and
  `$` are written explicitly (Core §6.4; Validation §6.3.3).
- Do not interpret annotations such as `title`, `description`, `default`, or
  `format` as validation assertions unless their vocabulary explicitly says so
  (Validation §§7, 9).
- Keep schema retrieval offline/pinned for reproducible builds; a URI is an
  identifier and need not trigger a network fetch (Core §9.1.2).

# Implementation implications

- `SOURCE_REQUIRED` — Every tracked UFUQ schema must name the Draft 2020-12
  dialect explicitly; omitted `$schema` has implementation-defined behavior
  (Core §8.1.1).
- `SOURCE_REQUIRED` — Schema compilation/meta-validation and negative
  instances must detect misspelled or unsupported constraints; unknown
  keywords are not reliably fail-closed assertions (Core §§4.3.1, 6.5).
- `PROJECT_DECISION_REQUIRED` — Select and pin a runtime validator only after
  recording its Draft 2020-12 vocabularies, reference-loading policy, output
  capabilities, number handling, and `format` configuration
  (`DATA-SRC-002`).
- `SOURCE_REQUIRED` — Required type, nullability, identifier, cardinality, and
  closed-object behavior must be expressed as assertions/applicators rather
  than assumed from annotations or neighboring keywords (Validation §§3, 6;
  Core §10.1).
- `EXPERIMENT_REQUIRED` — Prove the chosen validator's behavior for
  `additionalProperties` versus `unevaluatedProperties` under `$ref`,
  `allOf`/`anyOf`, and conditionals before using either as a release gate
  (Core §§10.3.2.3, 11).
- `EXPERIMENT_REQUIRED` — Prove that runtime numeric parsing and validation
  reject non-finite or unsafe values required by UFUQ even though the JSON
  Schema abstract number model is unbounded (Core §§4.2.1, 6.2).
- `PROJECT_DECISION_REQUIRED` — Canonical UTF-8/LF/key ordering, Unicode
  normalization, number formatting, and output hashing remain UFUQ
  serialization choices; JSON Schema validity does not define bytes.
- `SOURCE_REQUIRED` — Validation evidence should retain structured instance
  and keyword locations; exact validator error prose is not portable
  (Core §§12.3-12.4).
- `PROJECT_DECISION_REQUIRED` — Use preloaded/pinned schemas in deterministic
  builds and define failure behavior for any unavailable reference; Core does
  not require network retrieval (Core §9.1.2).

# Testing implications

- Meta-validate every schema under the pinned Draft 2020-12 meta-schema and
  fail on unsupported required vocabularies.
- For each schema, pair at least one production-shaped valid fixture with
  malformed cases for missing required members, unexpected members, wrong
  primitive types, explicit nulls, invalid stable IDs, invalid enum values,
  numeric boundaries, and nested/reference failures.
- Test wrong-type values for keywords that otherwise ignore unrelated types.
- Test that a deliberately misspelled keyword does not silently enter an
  approved schema; this may require linting/meta-schema policy beyond ordinary
  instance validation.
- Test `format` with the validator's actual configured vocabulary and mode;
  never infer assertion behavior from the keyword's presence.
- Exercise local/offline `$ref` resolution, missing targets, duplicate `$id`
  collisions, anchor relocation, and recursion failure behavior.
- Exercise composed schemas specifically for unknown-property closure and
  annotation-dependent `unevaluated*` behavior.
- Compare structured output fields (`valid`, keyword location, instance
  location) rather than implementation-specific English messages.
- Keep deterministic byte/hash rebuild tests separate from schema-validity
  tests.

# Limitations

- The specifications define schema processing, not UFUQ domain semantics,
  catalogue field meanings, coordinate validity, cultural review, or licence
  approval.
- Schema validity does not establish scientific correctness, provenance
  truth, referential integrity against an external catalogue, or deterministic
  bytes.
- The abstract numeric model can exceed JavaScript/runtime capabilities.
- A conforming schema does not prove that a particular validator conforms.
- `format` and extension support vary by implementation.
- Draft 2020-12 does not choose UFUQ's schema organization, validator package,
  error API, or schema-version migration policy.

# Conflicts and ambiguities

- `UFUQ-DATA` requires fail-closed runtime validation, while Core directs
  unsupported keywords to annotation behavior. Resolution: pin supported
  vocabularies and add schema meta-validation/linting plus negative fixtures;
  do not rely on unknown-keyword rejection.
- JSON objects are unordered in the schema model, while UFUQ requires stable
  serialized key order. These are complementary layers, not conflicting
  standards.
- `format` often appears to users as validation but is annotation-first in the
  default Draft 2020-12 dialect. UFUQ must record an explicit validator
  decision rather than silently assuming assertion.
- `$id`/`$ref` URIs can look like download URLs, but Core permits preloaded
  URI associations. UFUQ's offline deterministic policy remains a project
  decision.
- The source register's shorter `json-schema-core` URL redirects to the
  published `draft-bhutton-json-schema-01` content. Both identify the same
  Draft 2020-12 publication; the canonical dialect URI is the meta-schema URI,
  not the document URL.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Explicit dialect declaration | Core §§8.1-8.1.1 | Put canonical Draft 2020-12 `$schema` in root schemas | `SOURCE_REQUIRED` |
| Required vocabulary support | Core §§8-8.1.2; Validation §§5-6 | Pin a validator and prove required vocabulary support | `PROJECT_DECISION_REQUIRED` |
| Unknown keywords are annotations | Core §§4.3.1, 6.5 | Meta-validate/lint schemas and use negative fixtures | `SOURCE_REQUIRED` |
| Keywords generally act independently | Core §§7.3, 10.1; Validation §3 | State type/null assertions explicitly | `SOURCE_REQUIRED` |
| Stable resource identity and references | Core §§8.2-9.4 | Use stable `$id`; pre-register schemas; test reference failures | `SOURCE_REQUIRED` |
| `format` annotation/assertion split | Validation §§7.1-7.2 | Do not rely on `format` without a pinned mode/vocabulary | `EXPERIMENT_REQUIRED` |
| Abstract arbitrary-precision numbers | Core §§4.2.1, 6.2; Validation §4.2 | Add separate finite/runtime numeric rules and edge tests | `PROJECT_DECISION_REQUIRED` |
| Composed-object closure semantics | Core §§10.3.2.3, 11 | Test chosen `additionalProperties`/`unevaluatedProperties` design | `EXPERIMENT_REQUIRED` |
| Structured validation output | Core §§12.2-12.4 | Preserve machine-locatable errors, not portable prose assumptions | `SOURCE_REQUIRED` |
| Schema validity is not canonical serialization | Core §§4.2.1-4.2.2 | Keep deterministic byte/hash verification as a separate gate | `PROJECT_DECISION_REQUIRED` |
