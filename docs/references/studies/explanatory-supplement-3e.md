# Bibliographic identity

- Canonical source ID: `EXSUP-3E`.
- Title: *Explanatory Supplement to the Astronomical Almanac*.
- Editors: Sean E. Urban and P. Kenneth Seidelmann.
- Edition/version: third edition.
- Year: 2013.
- Publisher: University Science Books.
- ISBN: print `978-1-891389-85-6`; eBook `978-1-938787-54-6`.
- Local file:
  `local-reference/astronomy/foundations/explanatory-supplement-3e.pdf`.
- Page count and accessibility: the local PDF has 716 PDF pages and
  `TEXT_UNAVAILABLE`. The visible index reaches printed page 676 and is followed by
  reference sheets; authoritative listings conflict between 676 printed pages and a
  current 734-page publisher listing.
- Verification status: the visible cover/title/contents identify the third edition and
  editors. Completeness and acquisition provenance are unverified; embedded
  third-party processing metadata is a provenance warning. Status remains
  `INCOMPLETE`, `PROVENANCE_UNVERIFIED`, and `TEXT_UNAVAILABLE`.

# UFUQ relevance

- Potential phases affected: explanatory support for Phase 1/2 positional astronomy and
  time/reference-system terminology.
- Potential project decisions affected: AST-003 and AST-004 only after reliable
  chapter/page verification.
- Material studied: visible cover, title, publication signals, contents structure, and
  index endpoint; official USNO description of the third edition's scope.
- Material intentionally not studied: all detailed chapters, equations, tables, and
  algorithms. The local text layer is unusable, whole-book OCR is prohibited, and no
  reliable chapter/page citations can be made from these bytes.
- Scope reason: preserve the source's explanatory role without inventing content or
  locations from a damaged/unverified derivative.

# Terminology

The official USNO description identifies the work as a reference to the theories and
algorithms used to produce *The Astronomical Almanac*, with emphasis on positional
data, computation methods, and use of almanac data. It also says the third edition
addresses ICRS, new precession/nutation theories, and a positional paradigm not tied to
the ecliptic/equinox.

No source-specific technical definition is recorded from the local file because a
reliable page/section pointer cannot be verified. Terms must be sourced to SOFA, IERS,
or another readable edition until this gap is resolved.

# Concepts and models

- The source is potentially valuable explanatory support for reference systems,
  positional astronomy, apparent place, and almanac production.
- The official USNO overview confirms broad topic coverage, not the wording, equations,
  or precise location of any local chapter.
- No detailed model is promoted from this local candidate.

# Equations and algorithms

No equation or algorithm was extracted. Reconstructing an equation from memory, a
filename, or another edition would violate the no-fabricated-location rule.

Any future extraction requires a verified complete copy with a usable text layer or
targeted visual verification of a specifically needed page. It must then be checked
against SOFA/IERS and independent results before affecting implementation.

# Conventions

No local convention is approved from this candidate. In particular, this dossier does
not infer coordinate-frame, azimuth, longitude, time-scale, refraction, epoch, or
observer conventions from the book's title or official summary.

# Implementation implications

- `INFORMATIONAL_ONLY`: retain the work as explanatory support subordinate to SOFA,
  IERS, catalogue metadata, and independent fixtures.
- `SOURCE_REQUIRED`: cite SOFA/IERS directly for any implementation-affecting
  coordinate, time, Earth-orientation, or refraction rule.
- `PROJECT_DECISION_REQUIRED`: no project policy may be selected from this candidate
  without reliable local verification.
- `EXPERIMENT_REQUIRED`: no numerical behavior or tolerance may be adopted from the
  unverified candidate.
- `INFORMATIONAL_ONLY`: the official USNO scope statement can guide a future targeted
  reading plan but cannot stand in for chapter study.

# Testing implications

- A test may not cite this local PDF as its numerical oracle.
- Fixture provenance must not claim that an expected value was reproduced from this
  book.
- A missing readable copy is a stop condition for a claim uniquely dependent on the
  book, but it does not block a claim independently grounded in SOFA/IERS/catalogue
  metadata.
- Add a documentation validation check that this dossier contains no invented chapter,
  page, equation, table, or quotation.

# Limitations

- No usable text layer.
- No whole-book OCR was performed.
- Edition identity is visually supported, but completeness and lawful acquisition
  provenance are not verified.
- Page-count records conflict.
- Detailed chapters, formulae, and conventions remain unstudied.
- The source cannot override SOFA, IERS, catalogue metadata, or independent reference
  outputs even after a usable copy is obtained.

# Conflicts and ambiguities

- Local PDF count: 716 pages. The visible index endpoint and publisher listings do not
  reconcile cleanly with that count.
- The file metadata identifies third-party image/PDF processing rather than an
  authoritative publisher production chain.
- The official USNO page describes the genuine third edition and its broad revisions;
  it does not prove that the local derivative is complete page-for-page.
- Existing tracked source notes previously warned against chapter/page citations from
  this candidate. This dossier follows that restriction.

# Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Bibliographic identity | Visible local cover/title; official USNO third-edition overview | Keep as restricted explanatory support | `INFORMATIONAL_ONLY` |
| Broad positional-astronomy purpose | Official USNO overview, paragraphs describing scope and third-edition changes | Plan future targeted reading; do not derive an algorithm | `INFORMATIONAL_ONLY` |
| Local text cannot support claim-level citations | Local file inspection; `REFERENCE_INVENTORY.local.md`, `EXPLANATORY-SUPPLEMENT-3E-CANDIDATE` | Stop source-specific claims lacking another authority | `SOURCE_REQUIRED` |
| Completeness is unresolved | Local page count/index signal versus publisher records | Do not cite local page/chapter completeness | `SOURCE_REQUIRED` |
| No production authority role | `UFUQ_SOURCE_REGISTER.md`, `EXSUP-3E` row | Use SOFA/IERS and independent fixtures first | `PROJECT_DECISION_REQUIRED` |
