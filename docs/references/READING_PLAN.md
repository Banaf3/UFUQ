# UFUQ source reading plan

## Method

This plan is scoped to the documentation and skill-preparation work that precedes
Phase 1. “Studied” means the identified UFUQ-relevant units were inspected and
paraphrased with a verifiable section, routine, field, equation, table, figure, page,
verse, or folio pointer where the source permits one. It does not mean every page was
read.

Source locations use printed pages where the dossier says so and PDF pages otherwise.
For web standards, numbered sections and fragment identifiers replace page numbers.
An inaccessible, unverified, or ambiguous location remains unresolved; it is never
reconstructed from memory.

Priority labels are:

- `CRITICAL_NOW`: needed to design the Phase 1 experiment safely;
- `SUPPORTING_NOW`: useful current explanation or engineering guidance;
- `REQUIRED_LATER`: study must deepen before the affected later claim;
- `NOT_RELEVANT_TO_UFUQ`: identity was checked, but its substantive domain is outside
  UFUQ.

## Astronomy and catalogue sources

| Source | Verified identity and extent | Access | Relevant units and priority | Current-phase reading plan and result |
|---|---|---|---|---|
| `SOFA-2023-10-11` | IAU SOFA Board, ANSI C release 2023-10-11; local manual 379 PDF pages plus routine source | Searchable manual/source | `CRITICAL_NOW`: `00READ.ME`, licence, introduction, observed-place, time, Earth-attitude, motion, ephemeris, horizon, geodesy, and refraction routines | Studied exact preambles/source for `Pmsafe`, `Epv00`, `Pnm06a`, `Bpn2xy`, `S06`, `C2ixys`, `Era00`, `Sp00`, `Gd2gce`, `Pvtob`, `Apcs`, `Apco`, `Apco13`, `Atciq`, `Atciqn`, `Atioq`, `Atco13`, `C2t06a`, `Pom00`, `Hd2ae`, `Ae2hd`, `UtcTai`, `UtcUt1`, `TaiTt`, `Refco`, `Eform`, `Gd2gc`, and `Cal2jd`. Other routine families remain outside the current claim. |
| Current TypeScript/JavaScript astronomy candidates | Exact official npm/GitHub/release/licence records for Astronomy Engine `2.1.19`, astronomia `4.2.0`, Observerly Astrometry `0.66.0`, TSOFA `18.1.0`, and ERFA `2.0.1` | Official web/source records | `CRITICAL_NOW` for freshness-dependent production mapping | Audited version/date, activity, licence, dependencies, platforms, TypeScript/offline/data/status/effect control, lineage and maintenance risk in `studies/typescript-astronomy-production-candidates.md`. No candidate was installed; no audited package matches the selected V1 semantics. |
| `IERS-TN36-2010` | Petit and Luzum, eds., IERS Technical Note 36, 2010; 180 local PDF pages | Searchable | `CRITICAL_NOW`: Introduction; Ch. 2 §§2.1-2.2; Ch. 4 §§4.1-4.2; Ch. 5 §§5.1-5.6, 5.9; Ch. 8 §8.2; Ch. 10 §10.1; relevant glossary | Studied the listed units, including Ch. 5 Eqs. (5.1)-(5.3), (5.5), (5.11), (5.14)-(5.15), Ch. 5 post-interpolation ocean-tide/libration ordering, Ch. 8's ocean-tide EOP family, and Ch. 10 Eq. (10.1). Exact restoration bytes/dependencies and other station/geophysical models remain later pins. |
| IERS Bulletin A/B/C, `finals2000A`, `IERS-GAZETTE-13`, and the C04 guide | Official IERS/IERS Rapid Service product metadata, formats, Bulletin A/B explanatory material, Gazette 13 interpolation guidance, and C04 numerical-treatment guidance | Searchable official web | `CRITICAL_NOW`: source flags at documented quantity-group granularity and independently normalized field roles; final/preliminary/prediction distinctions; leap authority; interpolation support; continuous `UT1-TAI`; subdaily restoration | Studied the exact roles needed for V1. Gazette 13 recommends a Lagrangian procedure, shows four points, and permits equivalents; UFUQ selects four points and full support as project policy. C04 supports continuous `UT1-TAI` treatment across leaps. TN36, not Gazette's old `RAY`, governs the 2010 restoration family. Exact production artifacts/configuration are 2D pins. |
| `FUND-ASTRO-6E` | Karttunen et al., 6th ed., 2017, Springer; local 548 PDF pages; DOI `10.1007/978-3-662-53045-0` | Searchable | `SUPPORTING_NOW`: Ch. 2 §§2.3-2.5, 2.9-2.10, 2.12-2.15 | Studied as explanatory material, including Eq. (2.10) and the source's south-origin azimuth convention. Astrophysics and unrelated chapters are intentionally not studied. |
| `EXSUP-3E` | Urban and Seidelmann, eds., 3rd ed., 2013; local 716 PDF pages; ISBNs verified | `TEXT_UNAVAILABLE`; completeness/provenance unverified | Potentially `SUPPORTING_NOW`: positional astronomy, ICRS, precession/nutation, almanac methods | Cover/title/contents/index signals and official USNO scope only were inspected. No technical chapter, equation, or page claim was extracted; current status is partial/unusable for claim-level evidence. |
| `ESA-HIP-1997-V1` | European Space Agency, ESA SP-1200, Volume 1, 1997; 586 PDF pages; ISSN 0379-6566 and ISBN 92-9092-399-7 | Searchable; relevant symbol-bearing pages visually checked; acquisition provenance unverified | `CRITICAL_NOW`: front matter/contents; §1.2.1; §§1.2.3 and 1.2.5-1.2.8; §§1.5.4-1.5.5; §2.1 H8-H18; Table 2.1.1(a) | Studied PDF pp. 3-11 and printed pp. 19-34, 94-98, 109-111, and 136. The source defines the original catalogue's model, J1991.25(TT), units, and `mu_alpha_star`; it is not treated as I/311-specific field authority. |
| `HIP-I311-README` | CDS/VizieR I/311, *Hipparcos, the New Reduction*; text/HTML rather than paginated PDF | Searchable | `CRITICAL_NOW`: Notice, File Summary, all four byte descriptions, solution/VIM/global notes, history | Entire relevant metadata was studied at field/note level. Catalogue rows were intentionally not read or copied. |
| `VAN-LEEUWEN-2007-VALIDATION` | van Leeuwen, A&A 474 (2007) 653-664; 12 PDF pages; DOI `10.1051/0004-6361:20078357` | Searchable | `CRITICAL_NOW` if I/311 is evaluated: §§1-5, Eqs. (1)-(4), (7), Tables 1-3, relevant Figs. 1-18 | Studied reduction-level uncertainty, correlations, external checks, and aggregate weight claims. No coordinate was extracted and no aggregate result became a tolerance. |
| `ESA-GAIA-DR3-CANDIDATE` | ESA Gaia DR3 dataset version 1.1/DOI record, documentation release 1.3, astrometric TCB/reference-system, standard-motion-model, and transform/error-propagation sections, `gaia_source`, Hipparcos-2 crossmatch, credit/licence, archive, and DR4-status pages | Searchable official web | `CRITICAL_NOW`: fixed release identity; TCB/ICRS/epoch/PM/parallax/systematics/five-/six-parameter-covariance/RV/quality semantics; bright/RV coverage; release-scoped IDs/crossmatch; access, attribution and redistribution/deployment terms | Studied release evidence and retained the bounded official TAP screen as exact fixed-release ADQL plus hash-bound ignored responses. It verifies 8/19 matches, five rows with both RV/error fields, and no Polaris crossmatch while approving no row. The scale-aware TCB-to-TDB adapter and immutable query authority are closed; row/fallback review and exact derived-artifact rights interpretation remain required. |
| `IAU-TDB-2006-B3`, `IAU-AU-2012-B2`, `KLIONER-SCALING-2008`, and `KLIONER-NOMENCLATURE-2010` | Official IAU TDB/AU definitions and peer-reviewed compatible-quantity treatment/nomenclature | Searchable official/primary web | `CRITICAL_NOW`: distinguish event-time conversion from parameter/rate/distance/covariance mapping and preserve exact defining constants | Studied. Epoch-only relabelling is prohibited. The approved analytic map preserves direction, scales rates/parallax and coordinate distance consistently, maps covariance with an explicit Jacobian, and keeps native/normalized systems typed. |
| `IAU-RV-2000-C1` and `LINDEGREN-DRAVINS-RV-2003` | Official IAU spectroscopic barycentric radial-velocity definition and peer-reviewed distinction from astrometric/kinematic velocity | Searchable official/primary web | `CRITICAL_NOW`: decide whether the Gaia observational RV participates in compatible-coordinate scaling and how it may enter propagation | Studied. The Gaia spectroscopic number/error are preserved without `L_B` scaling or kinematic relabelling; a component-specific propagation-proxy approval remains row gate C. |
| `CDS-PCRV-III252` and `CDS-XHIP-V137D` | Official CDS ReadMes for the Pulkovo RV compilation and Extended Hipparcos Compilation | Searchable official web | `REQUIRED_LATER` only for the Gaia-ineligible Polaris path or another mandatory row | Studied metadata and bounded Polaris field-presence/reference evidence. Exact systemic/component suitability and redistribution/deployment rights remain open; no blanket mixed catalogue is approved. |
| `TORRES-POLARIS-2023` | Torres (2023), primary peer-reviewed Polaris spectroscopic-orbit paper | Searchable publisher record | `CRITICAL_NOW` candidate for the Gaia-ineligible Polaris systemic-RV field | Studied scope and data-availability statement only. The exact field value, convention, uncertainty, physical scope, crosswalk and rights are not approved. |

## Geodesy and historical qibla sources

| Source | Verified identity and extent | Access | Relevant units and priority | Current-phase reading plan and result |
|---|---|---|---|---|
| `KARNEY-2012-ARXIV-V2` / `KARNEY-2013` | Charles F. F. Karney, *Algorithms for Geodesics*, 2012 arXiv v2, 12 PDF pages; published 2013 DOI `10.1007/s00190-012-0578-z` | Searchable | `CRITICAL_NOW` for Qibla-method preparation: §§1-7; Eqs./series used by the inverse method; Tables 1 and 4-6 | Study ellipsoid definitions, inverse/direct conventions, Newton/bracketing behavior, near-antipodal construction, error analysis, and test cases. The paper does not provide a Kaaba coordinate or approve UFUQ's runtime model. |
| `KING-1993` | David A. King, *Astronomy in the Service of Islam*, 1993; local 358 PDF pages | Searchable OCR | `REQUIRED_LATER` / historical context: relevant qibla, sacred-direction, folk astronomy, and Islamic mathematical-astronomy studies | Read only verified relevant studies/pages for historical distinctions. OCR-derived wording requires image verification. No modern coordinate, datum, or algorithm is derived. |
| `KING-1999` | David A. King, *World-Maps for Finding the Direction and Distance to Mecca*, 1999; local 679 PDF pages | Searchable OCR | `REQUIRED_LATER` / historical context: introduction, mathematical-geography context, map construction/use, and conclusions | Read only sections needed to distinguish historical mathematical/cartographic procedures. Maps are never a production-coordinate source. |

## Cultural-astronomy sources

| Source | Verified identity and extent | Access | Relevant units and priority | Current-phase reading plan and result |
|---|---|---|---|---|
| `IBN-QUTAYBA-ANWA` | Ibn Qutaybah, *Kitab al-Anwa fi Mawasim al-Arab*; local 92-page derivative; edition/year/publisher unverified | Searchable derivative; edition-stable pagination unavailable | `REQUIRED_LATER`: exact passages for the specifically named star/pattern claim under review | Identify exact Arabic only; retain internal verse/chapter markers where present; do not treat derivative PDF pages as stable citations. Translation, edition identity, geography, modern identification, and any Najdi claim require human/edition review. |
| `KUNITZSCH-1961` | Paul Kunitzsch, *Untersuchungen zur Sternnomenklatur der Araber*, 1961; local 130 PDF pages | Searchable OCR | `REQUIRED_LATER`: classification method and entries relevant to Banat Na'sh/Ursa, al-Judayy/Polaris, and identified conflicts | Inspect exact entry/page images as needed. German/Arabic terminology and OCR remain human-review dependent; the source is not itself Najdi evidence. |
| `HAFEZ-2010` | Ihsan Hafez, al-Sufi fixed-stars PhD thesis, 2010; 406 PDF pages; DOI `10.25903/6xsf-aa64` | Searchable | `REQUIRED_LATER`: thesis pp. 31-39, 111-128, and 313-327; Tables 18-19, 24, and 26 | Study only the historical methodology and Greco-Arabic crosswalk relevant to current names/identifications. Proposed modern matches and translations stay provisional and are not Najdi evidence. |

## Data-governance and schema sources

| Source | Verified identity and extent | Access | Relevant units and priority | Current-phase reading plan and result |
|---|---|---|---|---|
| `JSON-SCHEMA-CORE-2020-12` and `JSON-SCHEMA-VALIDATION-2020-12` | Official Draft 2020-12 Core and Validation, published HTML, 16 June 2022 | Searchable official HTML | `CRITICAL_NOW`: Core §§4.2-13; Validation §§1-10 and Appendix A, restricted to dialect, vocabularies, assertions, references, composition, output, security | Studied by stable section number. Hypermedia details, every `format`, full output examples, and Relative JSON Pointer are deferred. |
| `ISO20022-JSON-2025` | ISO 20022 TSG/RMG, *Generation of JSON Schema Draft 2020-12 for ISO 20022:2013*, 2025; 49 PDF pages | Searchable | `NOT_RELEVANT_TO_UFUQ`: title/status/contents/Foreword/Introduction/§§1-5 opening only | Identity and financial-message scope studied through pp. 1-7. Transformation rules pp. 8-49 are intentionally not studied or adopted. |
| `PROV-SEM-2013` | James Cheney, ed., W3C Working Group Note, 2013; 33 PDF pages | Searchable | `SUPPORTING_NOW`: Abstract/Status, §§1-3.5, and §4 organization | Studied entity/activity/agent/influence/explicit derivation terminology. Formal satisfaction, constraints, proofs, and reasoning are out of scope. |
| `FAIR-2016` | Wilkinson et al., *Scientific Data* 3, 160018; 9 PDF pages; DOI `10.1038/sdata.2016.18` | Searchable | `SUPPORTING_NOW`: pp. 1-5, Box 2, and conclusion p. 7 | Studied as technology-neutral guidance. Domain examples and references are not current rule sources; no FAIR compliance claim is made. |

## Engineering-quality sources

| Source | Verified identity and extent | Access | Relevant units and priority | Current-phase reading plan and result |
|---|---|---|---|---|
| `BASS-ET-AL-2022` | Bass, Clements, and Kazman, *Software Architecture in Practice*, 4th ed.; local 460 PDF pages; ISBN `978-0-13-688609-9` | Searchable | `SUPPORTING_NOW`: §§1.3, 3.2-3.5, 12.1-12.2 partial, 21.1-21.2, 21.6-21.7, 22.7 | Studied quality scenarios, testability, risk-based/lightweight evaluation, and rationale. Tactic catalogues and comprehensive methods are deferred unless a demonstrated UFUQ risk needs them. |
| `WILSON-ET-AL-2014` | Wilson et al., *PLOS Biology* 12(1), e1001745; 7 PDF pages | Searchable | `SUPPORTING_NOW`: pp. 1-6 | Studied reproducible commands, provenance, incremental/versioned work, tests, oracles, and conclusion. |
| `WILSON-ET-AL-2017` | Wilson et al., *PLOS Computational Biology* 13(6), e1005510; 20 PDF pages | Searchable | `SUPPORTING_NOW`: pp. 2-11, 14-15, 18-19 | Studied raw data/acquisition, transforms, modular software, project organization, version control, CI, and proportional adoption. Manuscript workflow is deferred. |
| `KANEWALA-BIEMAN-2014` / local 2018 preprint | Kanewala and Bieman, systematic review; local arXiv preprint 30 PDF pages; published DOI `10.1016/j.infsof.2014.05.006` | Searchable | `SUPPORTING_NOW`: Abstract, §§1-3.4, 4.1-4.4, and conclusion opening | Studied oracle problems, testing levels, pseudo-oracles, reference data, metamorphic tests, numerical tolerance evidence, and review limitations. Full primary-study tables are deferred. |

## Project documents

The project documents named in the request were read as current decisions and
constraints, not as external evidence:

- `docs/ASTRONOMY_SPEC.md`;
- `docs/DATA_STRATEGY.md`;
- `docs/IMPLEMENTATION_DECISIONS.md`;
- `docs/ARCHITECTURE.md`;
- `docs/PHASES.md`;
- `docs/TEST_PLAN.md`;
- `docs/TUTORING_BKT_SPEC.md`;
- `docs/references/UFUQ_SOURCE_REGISTER.md`;
- `docs/references/SOURCE_GAPS.md`; and
- `docs/references/PHASE_SOURCE_MATRIX.md`.

They control project status and stop conditions. They cannot authenticate a local PDF
or turn a provisional scientific/cultural value into an external fact.
