# Bibliographic identity

- Canonical source ID: `HIP-I311-README`.
- Title: *I/311 Hipparcos, the New Reduction* catalogue `ReadMe`.
- Dataset author: Floor van Leeuwen; catalogue documentation maintained/distributed by
  CDS/VizieR.
- Edition/version: CDS catalogue `I/311`, corrected files dated 16 September 2008.
- Publication year: underlying reduction/book and validation article 2007; corrected
  catalogue-file history 2008.
- Publisher/archive: Centre de Données astronomiques de Strasbourg (CDS), VizieR.
- Identifier: catalogue `I/311`; associated bibcode `2007A&A...474..653V`; validation
  DOI `10.1051/0004-6361:20078357`.
- Local files: `data/raw/hipparcos-i311/ReadMe` and
  `local-reference/catalogues/hipparcos-i311/documentation/cds-readme.html`.
- Page count and accessibility: plain-text/HTML metadata, so PDF page count is not
  applicable. Both have directly searchable text; the local HTML reproduces the
  catalogue `ReadMe`.
- Verification status: catalogue ID, title, author, file list, row counts, fixed-width
  layouts, correction notice, and history were checked in both local forms. I/311 is
  selected by project decision for the Phase 1 local spike; acquisition manifest,
  authoritative raw-data checksum evidence, licensing/redistribution, fields, filters,
  and an approved UFUQ subset remain unresolved.

# UFUQ relevance

- Phases affected: Phase 1 I/311 catalogue/provenance spike; Phase 2 only if the
  remaining source-derived, scientific, and licensing gates are approved.
- Project decisions affected: AST-001 catalogue selection/fields, AST-003 frame/epoch
  and motion policy, AST-004 photometric/visibility policy, ADR-004, and the data
  strategy.
- Sections studied:
  - abstract, notice, file summary, and history;
  - complete byte-by-byte descriptions of `hip2.dat`, `hip7p.dat`, `hip9p.dat`, and
    `hipvim.dat`;
  - solution-type Notes (1)-(2), VIM Note (1), and Global Note (G1);
  - acknowledgement and references.
- Intentionally not studied: catalogue row values and any manually selected star
  coordinates. No parsing or astronomy implementation spike was begun.
- Scope reason: the `ReadMe` is the authority for fixed-width layout, field units,
  catalogue epoch/frame labels, solution types, and covariance representation.

# Terminology

- **HIP**: the six-character Hipparcos identifier field and stable row key in the
  catalogue layout.
- **Solution type (`Sn`)**: a number `10*d+s`; `s` is the adopted solution family and
  `d` encodes peculiarities.
- **Five-parameter solution**: right ascension, declination, parallax, and two proper
  motion components in `hip2.dat`, with formal errors and an upper-triangular weight
  matrix.
- **Seven-/nine-parameter solution**: acceleration and, for nine-parameter solutions,
  acceleration-change fields stored in supplemental files keyed by HIP.
- **VIM**: variability-induced mover; supplemental offsets describe photocentre motion
  linked to magnitude variation.
- **Formal error**: catalogue uncertainty field for a fitted astrometric parameter; it
  is not a UFUQ implementation tolerance.
- **Upper-triangular weight matrix (`UW`)**: stored factor `U` related to covariance
  `C` by the catalogue's Global Note (G1).
- **Hp magnitude**: the Hipparcos photometric band. It is not Johnson `V`.

# Concepts and models

## File-level model

The `File Summary` defines four data files:

- `hip2.dat`: record length 276, 117,955 astrometric-catalogue records;
- `hip7p.dat`: record length 129, 1,338 seven-parameter records;
- `hip9p.dat`: record length 274, 104 nine-parameter records;
- `hipvim.dat`: record length 129, 25 VIM records.

The supplemental files are joined by `HIP`; they are not independent star catalogues.
A parser must respect the solution type before interpreting supplemental parameters.

## Astrometric row

In `hip2.dat`, bytes 16-28 and 30-42 hold `RArad` and `DErad` in radians, labelled ICRS
at epoch 1991.25. Parallax is mas; proper motions and their errors are mas/year. Formal
errors for RA/Dec are mas even though the coordinates themselves are radians. This
mixed-unit source layout requires named normalization, not an unlabeled numeric tuple.

The `ReadMe` does not state the time scale associated with the Julian epoch label
`Ep=1991.25`, and it does not state the RA proper-motion cosine convention with enough
precision to satisfy the `iauPmsafe` interface. Those are blocking metadata questions,
not values to infer.

## Solution quality and covariance

`Sn`, old solution type `So`, component count `Nc`, transit count `Ntr`, goodness of fit
`F2`, rejected-data percentage `F1`, and stochastic dispersion `var` are scientifically
meaningful selection/quality fields. Omitting them from an approved UFUQ subset needs a
reviewed rationale.

Global Note (G1) gives the factorization of the inverse covariance. The 15 stored
elements correspond to the five astrometric parameters; the supplemental solutions add
elements for acceleration terms. A consumer cannot treat the formal errors as
independent merely because scalar error columns exist.

## Dataset correction history

The `Notice` says the CDS files differ slightly from the book files because a
goodness-of-fit error was corrected. It also says files distributed between 9 June and
15 September 2008 contained errors corrected after that date. A manifest must identify
and hash the actual bytes; “I/311” alone is not a complete version pin.

# Equations and algorithms

| Item | Source location | Variables, units, assumptions, and domain | UFUQ use and validation |
|---|---|---|---|
| Solution-type decomposition | `hip2.dat`, Note (1) | `Sn = 10*d+s`; `s` selects stochastic/VIM/5-/7-/9-parameter solution; `d` combines single/double, variability, photocentre, and secondary flags. | Parse and validate the decimal encoding before joining supplemental rows; preserve raw value and decoded flags. |
| Weight/covariance relationship | Global Note (G1) | `C^-1 = U^T U`; `U` is stored upper-triangular in a specified element order on RA, Dec, parallax, pmRA, pmDE and supplemental derivatives. Units follow their parameter axes. | Do not assume diagonal independent errors. Reconstruct/check only after a reviewed normalization design and numerical conditioning tests. |
| VIM displacement | `hipvim.dat`, Note (1) | Component `ups * (1 - 10^(-0.4*(m_r-m)))`; `upsRA`,`upsDE` are mas and depend on reference/observed magnitude. | `REQUIRED_LATER` only if VIM rows enter the approved subset. Do not silently treat VIM offsets as ordinary position/proper motion. |
| Fixed-width parsing | Each `Byte-by-byte Description` | Byte ranges are one-based inclusive; Fortran-like formats and units are given per field. | Candidate parser must use the manifest-pinned file/record length and fail on short/long or malformed records. No parser was implemented in this study. |

# Conventions

- `RArad`/`DErad`: radians, ICRS, epoch 1991.25.
- `Plx`: milliarcseconds.
- `pmRA`/`pmDE`: milliarcseconds per year; exact RA cosine convention unresolved in
  this local metadata.
- Formal RA/Dec errors: milliarcseconds, despite coordinate columns being radians.
- `Hpmag`: Hipparcos magnitude; `B-V` and `V-I` are separate colour indices.
- `UW` is a factor of inverse covariance, not a row of independent standard deviations.
- HIP is the join key across the four files.
- File byte positions are fixed-width and one-based in the documentation.
- Epoch, frame, and observation time are separate concepts. `Ep=1991.25` does not
  define a runtime observation instant.

# Implementation implications

- `SOURCE_REQUIRED`: an I/311 manifest must pin catalogue ID, corrected-file
  acquisition URL/date, raw hashes, exact files/columns, expected record lengths/counts,
  filters, row order, and source citation.
- `EXISTING_PROJECT_DECISION`: I/311 is the sole source for the Phase 1 local spike;
  alternate and dual-catalogue support are outside scope.
- `SOURCE_REQUIRED`: normalize every numeric field with explicit source unit, frame,
  epoch, null/quality semantics, and raw-field provenance.
- `EXPERIMENT_REQUIRED`: resolve and validate the exact `pmRA` convention before
  mapping it to SOFA/Astropy. Never apply or omit `cos(dec)` from memory.
- `PROJECT_DECISION_REQUIRED`: select handling for 5-, 7-, 9-parameter, stochastic,
  VIM, double/multiple, photocentre, and secondary-component solutions.
- `PROJECT_DECISION_REQUIRED`: decide which uncertainty/covariance and quality fields
  are retained and how unsupported solution types fail.
- `SOURCE_REQUIRED`: keep `Hp` distinct from Johnson `V`; visibility/filter behavior
  needs an approved photometric policy.
- `SOURCE_REQUIRED`: raw catalogue bytes remain immutable and ignored; coordinates may
  only enter generated artifacts through the approved parser/normalizer.
- `PROJECT_DECISION_REQUIRED`: determine licensing and redistribution before tracking
  any raw or generated source-derived rows.

# Testing implications

- File tests: exact record lengths and counts from `File Summary`; final newline policy;
  invalid/short/overlong records; malformed numeric fields; and unexpected additional
  records.
- Field tests: byte-boundary fixtures for every selected field; radians/mas/mas-year
  conversions; range/finite checks; and preservation of raw precision.
- Solution tests: all documented `s` values and combinations of `d`; required
  supplemental-row presence; duplicate/missing HIP; and forbidden supplemental joins.
- Covariance tests: stored `U` element order, dimensions by solution family,
  positive/ill-conditioned cases, and rejection of non-finite factors.
- Provenance tests: corrected version/hash, source-drift failure, deterministic row
  order, deterministic serialization, and generated-artifact checksum.
- Astronomy-reference tests: epoch identity at 1991.25 and motion propagation only
  after `pmRA` semantics and time-scale policy are approved.
- Stop conditions: absent approved acquisition/licence record, hash mismatch,
  unresolved motion convention, unsupported solution type, or ambiguous null/quality
  field blocks the affected artifact.

# Limitations

- The `ReadMe` defines byte-level metadata; it does not select I/311 for UFUQ.
- It does not approve a culturally required subset, magnitude threshold, context-star
  policy, or redistribution.
- The local raw catalogue data files were not studied or parsed.
- The epoch's time-scale semantics and `pmRA` cosine convention are not explicit enough
  here for transformation code.
- Formal errors characterize the catalogue solution; they do not validate a future
  propagated horizontal position or set a test tolerance.
- The correction notice makes a catalogue ID/year insufficient as a byte-version pin.

# Conflicts and ambiguities

- Project documents now select I/311 for the Phase 1 local spike. This resolves only
  source choice; it does not resolve the source-specific semantic, field, quality,
  subset, licence, or artifact-policy questions recorded in this dossier.
- `iauAtco13`/`iauPmsafe` expect RA proper motion as coordinate-angle rate. The I/311
  `ReadMe` label alone does not prove whether conversion from a cosine-scaled component
  is required.
- `Ep=1991.25` is a Julian-epoch label but the local `ReadMe` does not provide the
  exact time-scale instant required by a propagation routine.
- Scalar formal errors coexist with a full weight-matrix factor. Treating them as
  independent would discard documented correlations.
- The 2008 correction notice creates at least two historical byte variants. Only a
  reviewed acquisition hash can establish which one UFUQ holds.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Corrected file/version history | `Notice`; `History` | Pin raw bytes and acquisition date/hash | `SOURCE_REQUIRED` |
| File names, lengths, counts | `File Summary` | Verify complete fixed-width inputs before parsing | `SOURCE_REQUIRED` |
| Stable row key | `hip2.dat`, bytes 1-6, `HIP` | Join by HIP; never by cultural name | `SOURCE_REQUIRED` |
| Frame/epoch and coordinate units | `hip2.dat`, bytes 16-42 | Carry ICRS, 1991.25, and radians explicitly | `SOURCE_REQUIRED` |
| Proper-motion units but ambiguous component semantics | `hip2.dat`, bytes 52-68 | Resolve SOFA/Astropy mapping before propagation | `EXPERIMENT_REQUIRED` |
| Formal errors and quality fields | `hip2.dat`, bytes 70-128 | Approve retention/selection policy | `PROJECT_DECISION_REQUIRED` |
| Hp is its own band | `hip2.dat`, bytes 130-149 | Do not relabel as Johnson V or unaided visibility | `SOURCE_REQUIRED` |
| Solution-family encoding | `hip2.dat`, Note (1) | Parse and gate supplemental solution types | `SOURCE_REQUIRED` |
| Covariance factorization | Global Note (G1) | Preserve correlations or document reviewed omission | `PROJECT_DECISION_REQUIRED` |
| I/311 source selected; licence/field/subset policy unresolved | `ASTRONOMY_SPEC.md` AST-001; `SOURCE_GAPS.md` DATA-SRC-001 | No production rows or redistribution yet | `EXISTING_PROJECT_DECISION` plus `PROJECT_DECISION_REQUIRED` |
