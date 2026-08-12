# UFUQ source register

## Purpose and status

This register identifies what a source may support in UFUQ. It does not copy source
text, approve unresolved project values, or make local reference files redistributable.
Local PDFs are ignored and restricted to the project machine. Their acquisition
provenance is recorded privately in `local-reference/REFERENCE_INVENTORY.local.md`.

Source authority and project approval are separate. An authoritative publication can
define a method or standard without selecting UFUQ's observer data, target coordinates,
tolerances, cultural mapping, educational policy, or deployment policy.

Priority values are `REQUIRED_NOW`, `SUPPORTING_NOW`, `REQUIRED_LATER`, `OPTIONAL`,
`HISTORICAL_CONTEXT_ONLY`, and `NOT_REQUIRED`.

## Scientific, data, and technical sources

| Source ID | Citation and pointer | Class | Priority | Availability | Permitted UFUQ use and limit |
|---|---|---|---|---|---|
| SOFA-2023-10-11 | IAU SOFA Board, *Standards of Fundamental Astronomy*, Issue 2023-10-11; local `00READ.ME`, release/manual sections; [official release](https://www.iausofa.org/current-software) | AUTHORITATIVE_STANDARD | REQUIRED_NOW | Local restricted distribution and official web record | Highest-order implementation reference for supported IAU algorithms. Milestone 2C.2 uses the exact `iauPmsafe`, `iauAtco13`, `iauApco13`, `iauAtciq`, `iauAtioq`, `iauPnm06a`, `iauEra00`, `iauSp00`, `iauPom00`, `iauC2t06a`, and `iauRefco` contracts to define a candidate route/effect inventory. Milestone 2C.4 records `iauRefco` input units/model form, the `iauAtioq` numerical guard, and the purely rotational role of `iauHd2ae`. The release does not select UFUQ's production implementation, atmosphere/defaults, validity range, terrain/visibility policy, omission bounds, or tolerance. |
| USNO-NOVAS-3.1 | U.S. Naval Observatory, *Naval Observatory Vector Astrometry Software (NOVAS)* 3.1; [official software overview](https://aa.usno.navy.mil/software/novas_info) and [official guide/FAQ](https://aa.usno.navy.mil/software/novas_faq) | CURRENT_TOOL_DOCUMENTATION | REQUIRED_LATER | Official USNO web; no local package, guide, ephemeris, or fixture is pinned | Candidate for a genuinely independent positional-astronomy path in the stronger postimplementation validation stage. Its algorithm, edition, ephemeris, inputs, and lineage must be audited and pinned before use. It is not a prerequisite to implementing ScientificProfileV1 and its published accuracy prose is not a UFUQ tolerance. |
| IERS-TN36-2010 | Petit, G., and Luzum, B., eds. (2010), *IERS Conventions (2010)*, IERS Technical Note 36; title page and contents; [official baseline and update status](https://iers-conventions.obspm.fr/conventions_material.php) | AUTHORITATIVE_STANDARD | REQUIRED_NOW | Local restricted PDF; official web record | Official registered 2010 baseline for reference systems, time/Earth-orientation terminology, models, and procedures. The Centre labels later corrected chapters/working versions as non-definitive and not officially approved as a registered edition; it separately states that linked supporting documentation is not part of the official distribution or the same review process. |
| IERS-UPDATES | IERS Conventions Centre, later corrections and non-registered working versions; [official Centre status/material page](https://iers-conventions.obspm.fr/conventions_material.php) | CURRENT_TOOL_DOCUMENTATION | REQUIRED_NOW | Official Centre status page; working/correction content is not yet pinned and is not the official registered TN36 distribution | Candidate correction/working evidence only. Every selected item requires its own version/hash/status and must be recorded independently from TN36 before it changes a result; separately linked supporting documentation is also non-official. |
| IERS-BULLETIN-A | IERS Rapid Service/Prediction Centre, [Bulletin A product metadata](https://datacenter.iers.org/productMetadata.php?id=6) and [Rapid Service product description](https://www.iers.org/iers/en/organization/productcentres/rapidservicepredictioncentre/rapid) | PRIMARY_DATASET_DOCUMENTATION | REQUIRED_NOW | Official IERS product documentation, retrieved 2026-08-03; no live product bytes selected for production | Authority for rapid/predictive `xp`,`yp`,`UT1-UTC`,`dX`,`dY` roles, publication frequency, and moving product extent. It does not approve predictions, live coverage, a stale threshold, or UFUQ's production product. |
| IERS-FINALS2000A-FORMAT | IERS Rapid Service/Prediction Centre/USNO, [`finals2000A` format](https://maia.usno.navy.mil/ser7/readme.finals2000A) | PRIMARY_DATASET_DOCUMENTATION | REQUIRED_NOW | Official product-format documentation, retrieved 2026-08-03; no live file selected | Authority for UTC MJD, field units/columns, separate Bulletin A/B columns, and independent IERS/prediction flags for polar motion, `UT1-UTC`, and `dX`,`dY`. Blank values are not zero; the format does not select product precedence or UFUQ scientific approval. |
| IERS-BULLETIN-B | IERS Earth Orientation Centre, [Bulletin B product metadata](https://datacenter.iers.org/productMetadata.php?id=207) | PRIMARY_DATASET_DOCUMENTATION | REQUIRED_NOW | Official IERS product documentation, retrieved 2026-08-03; no Bulletin B artifact selected | Authority for monthly daily final/preliminary `xp`,`yp`,`UT1-UTC`,`dX`,`dY` roles and uncertainties. It does not select field precedence, interpolation, coverage, or freshness for UFUQ. |
| IERS-BULLETIN-C | IERS Earth Orientation Centre, [Bulletin C product metadata](https://datacenter.iers.org/productMetadata.php?id=16) | PRIMARY_DATASET_DOCUMENTATION | REQUIRED_NOW | Official IERS product documentation, retrieved 2026-08-03; no production machine artifact selected | Authority for leap-second announcements/confirmations and UTC-TAI information. A machine-readable transport, version/hash, expiration rule, and update workflow still require approval. |
| RFC3339-TIMESTAMP | Klyne, G., and Newman, C. (2002), RFC 3339, *Date and Time on the Internet: Timestamps*, Sections 5.6-5.8; [RFC Editor record](https://www.rfc-editor.org/rfc/rfc3339.html) | AUTHORITATIVE_STANDARD | REQUIRED_NOW | Official immutable RFC | Authority for the broader timestamp profile, UTC offsets, and conditional leap-second syntax. UFUQ's Z-only astronomy-boundary subset is a project proposal; the RFC does not validate a claimed leap date or select precision. |
| IANA-TZDB-LEAPS | IANA Time Zone Database release archives, including [`tzdb-2026b`](https://data.iana.org/time-zones/tzdb-2026b/) `leap-seconds.list`/`leapseconds` artifacts | PRIMARY_DATASET_DOCUMENTATION | SUPPORTING_NOW | Official versioned release directory inspected 2026-08-03; no production IANA artifact/hash selected | Candidate machine-readable leap transport and zone-data provenance only. IERS Bulletin C remains the leap-event authority; production selection and cross-check remain open. |
| UMPSA-FK-PEKAN-SITE | Universiti Malaysia Pahang Al-Sultan Abdullah, [Faculty of Computing history](https://fk.umpsa.edu.my/index.php/about/background-vision-mission), [UMPSA Pekan-campus overview](https://umpsa.edu.my/en/about), and [Faculty contact page](https://fk.umpsa.edu.my/index.php/contact) | PRIMARY_INSTITUTIONAL_DOCUMENTATION | REQUIRED_NOW | Official UMPSA web, inspected 2026-08-13 | Establishes that the Faculty of Computing is at UMPSA Pekan Campus and supports the V1 site identity. It supplies no approved reference point, latitude, longitude, datum/frame/ellipsoid, height, coordinate epoch, accuracy, or licence for copied map-provider coordinates. |
| JUPEM-GEODETIC | Department of Survey and Mapping Malaysia (JUPEM), [official public geodetic products](https://www.jupem.gov.my/en/orang-awam), [eBiz geodetic services](https://ebiz.jupem.gov.my/Perkhidmatan/PerkhidmatanGeodetik), and [GDM circular](https://www.jupem.gov.my/jupem18a/assets/uploads/files/pekeliling/d95f4-pkpup-2-2021.pdf) | PRIMARY_DATASET_DOCUMENTATION | SUPPORTING_NOW | Official web inspected 2026-08-13; this public-web audit did not establish a Faculty-specific observer or control record | Documents GPS-control, coordinate/datum transformation, geoid, MyRTKnet, and RINEX service routes. It does not select UFUQ's record, require a control monument, convert height silently, or prove a Faculty-specific record exists. A site-matched JUPEM record is optional evidence; 2D may instead review a reproducible official UMPSA or Malaysian-government record that supplies the complete `ObserverPreset` semantics and documented accuracy. Source class alone does not establish adequacy. |
| EXSUP-3E | Urban, S. E., and Seidelmann, P. K., eds. (2013), *Explanatory Supplement to the Astronomical Almanac*, 3rd ed.; [USNO overview](https://aa.usno.navy.mil/publications/exp_supp) | AUTHORITATIVE_BOOK | SUPPORTING_NOW | Local third-edition identity is visually verified, but the file is `TEXT_UNAVAILABLE`, `INCOMPLETE`, and `PROVENANCE_UNVERIFIED`; embedded third-party processing metadata is an additional provenance warning | Explanatory support for positional-astronomy methods. Do not redistribute or use the local file for chapter/page citations until completeness, searchable text, and provenance are resolved. |
| FUND-ASTRO-6E | Karttunen, H., et al. (2017), *Fundamental Astronomy*, 6th ed., DOI `10.1007/978-3-662-53045-0`; [publisher record](https://link.springer.com/book/10.1007/978-3-662-53045-0) | AUTHORITATIVE_BOOK | SUPPORTING_NOW | Local restricted PDF; bibliographic identity verified, acquisition provenance unverified | Conceptual and explanatory support. It does not override SOFA, IERS, catalogue metadata, code-independent reference results, or later lineage-independent evidence. |
| ASTROPY-DOCS-PIN | Astropy Project, official `8.0.1` time, coordinate/space-motion, frame-transformation, EarthLocation, LeapSeconds, and IERS documentation; exact pages in `studies/astropy-pyerfa-reference-docs.md` | CURRENT_TOOL_DOCUMENTATION | REQUIRED_NOW | `PINNED_FOR_REFERENCE_DESIGN`: official `stable` pages displayed `8.0.1` on 2026-08-03; retrieval version/date are recorded because the alias can move | Defines the candidate reference library's explicit time format/scale, epoch formats, observer/refraction inputs, frame graph, IERS auto/offline/prediction/degraded behaviour, leap-table expiration/update surfaces, `AltAz` defaults, and low-altitude warnings. Milestones 2C.3-2C.4 require explicit offline overrides, explicit atmosphere inputs/no hidden defaults, and status capture. Astropy remains reference-only and selects no UFUQ production behavior, atmosphere, range, or tolerance. |
| PYERFA-PIN | PyERFA [`2.0.1.5` release](https://pypi.org/project/pyerfa/2.0.1.5/) plus official API/space-motion/astrometry/time/observer/warning documentation listed in `studies/astropy-pyerfa-reference-docs.md` | CURRENT_TOOL_DOCUMENTATION | REQUIRED_NOW | `PARTIAL`: exact release and source-distribution SHA-256 are pinned; official ReadTheDocs `stable` displayed `2.0.1.4`, not locked runtime `2.0.1.5`, on 2026-08-03 | Records wrapper/status contracts and direct reference probes for 2C.2 stages/effects and 2C.3 time/observer boundaries below Astropy. SOFA remains the algorithm authority. A version-matched official documentation build, tagged-source review, or explicit reviewer acceptance is required before relying on its exact API behaviour in postimplementation reference-validation claims; it is not a preimplementation production-algorithm or data-policy decision. |
| ASTROPY-IERS-DATA-PIN | Astropy IERS data package/release plus selected table files and hashes | PRIMARY_DATASET | REQUIRED_NOW | `PINNED_FOR_SYNTHETIC_SMOKE_ONLY`: package `0.2026.7.20.15.31.18`; packaged EOP/leap-second files, coverage, sizes, and SHA-256 values are tracked in `tools/astronomy-reference/environment-manifest.json` | Reproduces the bounded synthetic smoke oracle. Production selection, predictive/expiry/update handling, supported range, and approval remain open. |
| CDS-CATALOGUE-STANDARD-2.0 | CDS, *Standards for Astronomical Catalogues*, Version 2.0, Section 3.2.2 basic unit symbols; [official HTML](https://vizier.cds.unistra.fr/vizier/doc/catstd-3.2.htx) and [official PDF](https://vizier.cds.unistra.fr/vizier/doc/catstd.pdf) | AUTHORITATIVE_STANDARD | REQUIRED_NOW | Official CDS/VizieR documentation, retrieved 2026-08-03 | Defines the catalogue unit token `yr` (also `a`) as exactly 365.25 days. Applied to I/311 `mas/yr`, this supports the numeric rate-unit conversion to SOFA radians per Julian year. It does not define I/311's epoch or proper-motion derivative time scale. |
| HIP-I311-README | CDS/VizieR catalogue I/311, *Hipparcos, the New Reduction* `ReadMe`; byte descriptions and notes; [official catalogue record](https://cdsarc.cds.unistra.fr/viz-bin/cat/I/311) | PRIMARY_DATASET | REQUIRED_NOW | Local raw metadata file and official web record | Authority for the selected Phase 1 local-spike source's file layout, units, solution types, literal `Ep=1991.25` label, frame metadata, row counts, and 2008 correction notice. It does not type the epoch representation or name its time scale, grant redistribution, select the UFUQ subset, or establish row suitability. |
| HIP-I311-APPENDIX-G | van Leeuwen, F. (2007), *Hipparcos, the new reduction*, Appendix G, Tables G.2–G.7; [official I/311 archive copy](https://cdsarc.cds.unistra.fr/ftp/I/311/intro.pdf) | PRIMARY_DATASET | REQUIRED_NOW | Official web PDF in the I/311 archive | I/311-specific authority for main/supplementary field symbols. Table G.3, printed p. 407, defines the right-ascension proper-motion field as `mu_alpha_star`; Tables G.5–G.6 extend the starred-alpha convention to acceleration terms. It does not decide UFUQ's production propagation or tolerance. |
| VIZIER-RULES | CDS, “Rules of usage of VizieR data”; [official rules](https://cds.unistra.fr/vizier-org/licences_vizier.html) | CURRENT_TOOL_DOCUMENTATION | REQUIRED_NOW | Official web | Supports scientific-use access, original-author/publication/publisher citation, and VizieR acknowledgement requirements. It directs catalogue-specific rights questions to source/ReadMe policies and does not by itself grant UFUQ permission to redistribute I/311 raw or derived rows. |
| SIMBAD-IDENTIFIERS | CDS SIMBAD identifier database and TAP service; [official service](https://simbad.cds.unistra.fr/simbad/sim-tap) | CURRENT_TOOL_DOCUMENTATION | SUPPORTING_NOW | Official web; identifier-only query recorded in the Milestone 2B audit | Supplies modern HR/Bayer/HIP cross-identifiers for review candidates. Cross-identification does not establish an Arabic historical name, membership, line drawing, directional use, or lesson approval. |
| ESA-HIP-1997-V1 | European Space Agency (1997), *The Hipparcos and Tycho Catalogues*, Volume 1: *Introduction and Guide to the Data*, ESA SP-1200; §§1.2, 1.5, and 2.1 | PRIMARY_DATASET | REQUIRED_NOW | Local restricted searchable PDF; bibliographic identity verified from content, acquisition provenance unverified | Official guide for the original 1997 catalogue's astrometric model, epoch, units, and H-field semantics. It strongly supports interpreting Hipparcos terminology but does not by itself define the later CDS I/311 reduction or prove that I/311 `pmRA` has identical semantics. |
| ESA-GAIA-DR1-I311-EPOCH | ESA Gaia DR1 processing documentation release 1.2, Section 4.2.1, [Properties of the input data](https://gea.esac.esa.int/archive/documentation/GDR1/Data_processing/chap_cu3tyc/sec_cu3tyc_property.html) | CURRENT_TOOL_DOCUMENTATION | REQUIRED_NOW | Official ESA web record, retrieved 2026-08-03 | Directly identifies the new Hipparcos reduction retrieved as CDS I/311 and calls its parameter epoch `J1991.25`. Supports the Julian representation, but does not state a time scale or exact Julian Date for I/311. |
| ESA-GAIA-DR3-CANDIDATE | ESA Gaia Archive/DPAC, [Gaia Data Release 3 documentation](https://gea.esac.esa.int/archive/documentation/GDR3/) and [official archive](https://gea.esac.esa.int/archive/) | PRIMARY_DATASET_DOCUMENTATION | SUPPORTING_NOW | Official ESA web; no release table/query/subset/rights manifest selected | Sufficient official documentation for Milestone 2D to evaluate a release-specific Gaia candidate and crosswalk. It does not approve Gaia for UFUQ, choose a subset, inherit future-release semantics, or couple cultural records to Gaia coordinates. |
| VAN-LEEUWEN-2007-VALIDATION | van Leeuwen, F. (2007), Hipparcos new-reduction validation article, *Astronomy & Astrophysics* 474, 653; DOI `10.1051/0004-6361:20078357`; article methods/results | FOUNDATIONAL_RESEARCH | REQUIRED_NOW | Local restricted PDF and official catalogue link | Supports evaluation of the new reduction's error characteristics. It does not replace the I/311 byte-level `ReadMe`. |
| KARNEY-2013 | Karney, C. F. F. (2013), “Algorithms for Geodesics,” *Journal of Geodesy* 87, 43–55, DOI `10.1007/s00190-012-0578-z`; algorithm and error-analysis sections; [publisher record](https://link.springer.com/article/10.1007/s00190-012-0578-z) | FOUNDATIONAL_RESEARCH | REQUIRED_LATER | Published record verified independently; no local publisher PDF | Ellipsoidal direct/inverse geodesic algorithms and difficult-case analysis. It does not provide or approve UFUQ's Kaaba target coordinate. |
| KARNEY-2012-ARXIV-V2 | Karney, C. F. F., *Algorithms for Geodesics*, arXiv `1109.4448v2` (revised 2012); [author's addenda](https://geographiclib.sourceforge.io/geod-addenda.html) | FOUNDATIONAL_RESEARCH | SUPPORTING_NOW | Local restricted searchable preprint; identity verified, acquisition provenance unverified | Local counterpart to the later 2013 article. Cite the local bytes as the preprint, not as the publisher PDF; use the peer-reviewed 2013 record for the final algorithm authority. |
| JSON-SCHEMA-CORE-2020-12 | Wright, A., et al., *JSON Schema: A Media Type for Describing JSON Documents*, Draft 2020-12; core and security sections; [official specification](https://json-schema.org/draft/2020-12/json-schema-core) | AUTHORITATIVE_STANDARD | REQUIRED_NOW | Official web | Schema dialect/core authority for versioned manifests, catalogue/content records, and fixtures. |
| JSON-SCHEMA-VALIDATION-2020-12 | Bhutton, B., et al., *JSON Schema Validation*, Draft 2020-12; validation vocabulary and security sections; [official specification](https://json-schema.org/draft/2020-12/json-schema-validation) | AUTHORITATIVE_STANDARD | REQUIRED_NOW | Official web | Validation-vocabulary authority. A chosen runtime library still requires a pinned dependency decision and conformance tests. |
| ISO20022-JSON-2025 | ISO 20022 TSG/RMG (2025), *Generation of JSON Schema Draft 2020-12 for ISO 20022:2013*; title and contents; [official listing](https://www.iso20022.org/about-iso-20022/apis-and-iso-20022) | CURRENT_TOOL_DOCUMENTATION | NOT_REQUIRED | Local restricted PDF; corrected identity | An ISO 20022 transformation paper, not the JSON Schema Draft 2020-12 specification. It supplies no UFUQ requirement. |
| FAIR-2016 | Wilkinson, M. D., et al. (2016), “The FAIR Guiding Principles for Scientific Data Management and Stewardship,” *Scientific Data* 3, 160018, DOI `10.1038/sdata.2016.18`; abstract and principles box; [publisher record](https://www.nature.com/articles/sdata201618) | FOUNDATIONAL_RESEARCH | SUPPORTING_NOW | Local restricted PDF and official web record | Guidance for findability, accessibility, interoperability, and reuse. UFUQ does not claim formal FAIR compliance. |
| PROV-SEM-2013 | Cheney, J., ed. (2013), *Semantics of the PROV Data Model*, W3C Working Group Note; status and introduction; [W3C note](https://www.w3.org/TR/prov-sem/) | CURRENT_TOOL_DOCUMENTATION | OPTIONAL | Local restricted PDF and official web record | Optional background on formal PROV semantics. Basic PROV-DM concepts may inform terminology; UFUQ is not implementing PROV reasoning. |

## Cultural and historical sources

| Source ID | Citation and pointer | Class | Priority | Availability | Permitted UFUQ use and limit |
|---|---|---|---|---|---|
| IBN-QUTAYBA-ANWA | Ibn Qutaybah, *Kitāb al-Anwāʾ fī Mawāsim al-ʿArab*; local title/author signals; [ISMI work/edition record](https://ismi.mpiwg-berlin.mpg.de/text/116262) | PRIMARY_HISTORICAL_SOURCE | REQUIRED_LATER | Local text-bearing derivative; `EDITION_UNVERIFIED`, `INCOMPLETE`, and `PROVENANCE_UNVERIFIED` | Evidence for claims classified `OLD_ARABIAN` only when tied to exact Arabic and an approved edition. It does not make every item `NAJDI_TRADITION`; local page numbers are not edition-stable. |
| KUNITZSCH-1961 | Kunitzsch, P. (1961), *Untersuchungen zur Sternnomenklatur der Araber*, Harrassowitz; bibliographic extent and contents; [German National Library partner record](https://www.deutsche-digitale-bibliothek.de/item/BGRHZDF6I4UHVHI6XBMND2OJZBY2FDVT) | SECONDARY_SCHOLARLY_SOURCE | REQUIRED_LATER | Local restricted OCR PDF; bibliographic identity verified, acquisition provenance unverified | Philological classification and conflict checking. It is not by itself evidence of specifically Najdi usage. Verify OCR-derived quotations against the page image. |
| HAFEZ-2010 | Hafez, I. (2010), *ʿAbd al-Raḥmān al-Ṣūfī and His Book of the Fixed Stars: A Journey of Re-discovery*, PhD thesis, DOI `10.25903/6xsf-aa64`; repository record and thesis sections; [JCU record](https://researchonline.jcu.edu.au/28854/) | SECONDARY_SCHOLARLY_SOURCE | REQUIRED_LATER | Local restricted PDF; identity verified, acquisition provenance unverified | `GRECO_ARABIC_SCHOLARLY` historical crosswalk and al-Ṣūfī context. It is not a Najdi authority. |
| KING-1993 | King, D. A. (1993), *Astronomy in the Service of Islam*, Variorum, ISBN 0-86078-357-X; contents and historical studies; [publisher record](https://www.routledge.com/Astronomy-in-the-Service-of-Islam/King/p/book/9780860783572) | SECONDARY_SCHOLARLY_SOURCE | HISTORICAL_CONTEXT_ONLY | Local restricted OCR PDF; identity verified, acquisition provenance unverified | Islamic-astronomy history and context. It is neither a production geodesic specification nor a specifically Najdi authority. |
| KING-1999 | King, D. A. (1999), *World-Maps for Finding the Direction and Distance to Mecca*, Brill, ISBN 90-04-11367-3; front matter and historical analysis; [publisher front matter](https://brill.com/display/book/9789004450738/front-1.pdf) | SECONDARY_SCHOLARLY_SOURCE | HISTORICAL_CONTEXT_ONLY | Local restricted OCR PDF; identity verified, acquisition provenance unverified | Historical qibla/cartography context only. Do not extract a production algorithm or destination coordinate from a historical map. |

## Engineering-quality sources

| Source ID | Citation and pointer | Class | Priority | Availability | Permitted UFUQ use and limit |
|---|---|---|---|---|---|
| BASS-ET-AL-2022 | Bass, L., Clements, P., and Kazman, R. (2022), *Software Architecture in Practice*, 4th ed., ISBN 978-0-13-688609-9; quality-attribute and evaluation sections; [publisher record](https://www.pearson.com/en-ca/subject-catalog/p/software-architecture-in-practice/P200000000111/9780136886099) | AUTHORITATIVE_BOOK | SUPPORTING_NOW | Local restricted PDF; identity verified, acquisition provenance unverified | Review guardrail for demonstrated quality attributes and trade-offs. It does not justify redesign merely because another pattern exists. |
| WILSON-ET-AL-2014 | Wilson, G., et al. (2014), “Best Practices for Scientific Computing,” *PLOS Biology* 12(1), e1001745, DOI `10.1371/journal.pbio.1001745`; recommendations and conclusion; [publisher article](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745) | FOUNDATIONAL_RESEARCH | SUPPORTING_NOW | Local restricted PDF and official web record | Supports version control, automated checks, readable code, and reproducible commands. Apply proportionately to an FYP. |
| WILSON-ET-AL-2017 | Wilson, G., et al. (2017), “Good Enough Practices in Scientific Computing,” *PLOS Computational Biology* 13(6), e1005510, DOI `10.1371/journal.pcbi.1005510`; workflow recommendations; [publisher article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) | FOUNDATIONAL_RESEARCH | SUPPORTING_NOW | Local restricted PDF and official web record | Supports low-overhead reproducibility and data/workflow hygiene suitable for one developer. |
| KANEWALA-BIEMAN-2014 | Kanewala, U., and Bieman, J. M. (2014), “Testing Scientific Software: A Systematic Literature Review,” *Information and Software Technology* 56(10), 1219–1232, DOI `10.1016/j.infsof.2014.05.006`; abstract, results, and conclusion | FOUNDATIONAL_RESEARCH | SUPPORTING_NOW | Local file is the 2018 arXiv preprint, not the publisher PDF | Supports oracle-problem awareness and layered scientific testing. Cite the peer-reviewed 2014 article by DOI and the local version as arXiv:1804.01954. |

## Project decisions

These tracked documents state UFUQ decisions; they are not external authorities.

| Source ID | Document and pointer | Class | Priority | Role |
|---|---|---|---|---|
| UFUQ-AGENTS | `AGENTS.md`, default reading path, dependency rules, never-invent rules | PROJECT_DECISION | REQUIRED_NOW | Repository operating constraints |
| UFUQ-ARCH | `docs/ARCHITECTURE.md`, layout, dependency rules, data-driven guidance, scenario authority | PROJECT_DECISION | REQUIRED_NOW | Approved architecture |
| UFUQ-ASTRO-SPEC | `docs/ASTRONOMY_SPEC.md`, conventions, unresolved decisions, validation specification | PROJECT_DECISION | REQUIRED_NOW | Astronomy contract and stop conditions |
| UFUQ-ASTRO-EXPERIMENT-PROTOCOL | `docs/spikes/PHASE1_SCIENTIFIC_EXPERIMENT_PROTOCOL.md` and `tools/astronomy-reference/experiments/`, Milestone 2C.5A classifications and schemas | PROJECT_DECISION | REQUIRED_NOW | Freezes experiment IDs, permitted/prohibited claims, current executability, lineage, deterministic evidence, acceptance limits, and reviewer gates. It is not a source authority, experiment result, production approval, error budget, or tolerance. |
| UFUQ-ASTRO-ERROR-BUDGET | `docs/spikes/PHASE1_SCIENTIFIC_ERROR_BUDGET.md` and `docs/governance/AST_006_ERROR_BUDGET_LEDGER.v1.json`, Milestone 2C.5C framework and evidence inventory | PROJECT_DECISION | REQUIRED_NOW | Separates measured values, exact guards, unresolved uncertainty terms, candidate combination/metric methodology, and six blocked tolerance classes. It is a review draft, not source authority, a bounded total, or an approved threshold. |
| UFUQ-SCIENTIFIC-PROFILE-V1 | `docs/spikes/PHASE1_SCIENTIFIC_PROFILE_V1.md`, Milestone 2C.6 candidate and exit-gate audit | PROJECT_DECISION | REQUIRED_NOW | Defines the minimal one-preset, bounded-time, source-neutral, geometric-only candidate; complete A-F blocker triage; three-stage validation lifecycle; 49-term roadmap disposition; resource actions; and exact 2C exit criteria. It is a review candidate, not reviewer approval, a data source, production output, or a numerical tolerance. |
| UFUQ-DATA | `docs/DATA_STRATEGY.md`, data classes, provenance manifest, pipeline, schemas | PROJECT_DECISION | REQUIRED_NOW | Catalogue/content provenance contract |
| UFUQ-IMPL-DEC | `docs/IMPLEMENTATION_DECISIONS.md`, active decisions | PROJECT_DECISION | REQUIRED_NOW | Code/test-affecting decision status |
| UFUQ-PHASES | `docs/PHASES.md`, phase outcomes and gates | PROJECT_DECISION | REQUIRED_NOW | Work sequencing |
| UFUQ-TEST | `docs/TEST_PLAN.md`, suite activation and evidence | PROJECT_DECISION | REQUIRED_NOW | Validation contract |
| UFUQ-STATUS | `docs/STATUS.md`, current readiness gates | PROJECT_DECISION | REQUIRED_NOW | Current state, not scientific evidence |
| UFUQ-STRUCTURE-MIGRATION | `docs/STRUCTURE_MIGRATION.md`, post-migration assertions | PROJECT_DECISION | SUPPORTING_NOW | Historical structure evidence |
| UFUQ-BKT-SPEC | `docs/TUTORING_BKT_SPEC.md`, BKT/observation/policy decisions and blockers | PROJECT_DECISION | REQUIRED_LATER | Phase 3 contract; external sources remain missing |
| UFUQ-ADR-003 | `docs/adr/003-astronomical-coordinate-conventions.md`, decision and validation | PROJECT_DECISION | REQUIRED_NOW | Coordinate-convention decision record |
| UFUQ-ADR-004 | `docs/adr/004-star-catalogue-and-provenance.md`, decision and validation | PROJECT_DECISION | REQUIRED_NOW | Catalogue/provenance decision record |
| UFUQ-ADR-007 | `docs/adr/007-testing-and-validation.md`, reference-lineage and validation-lifecycle decision | PROJECT_DECISION | REQUIRED_NOW | Layered-test decision record |

## Mandatory interpretation controls

1. PROV Semantics is optional and is not required for UFUQ's manifest design. Basic
   PROV-DM concepts may inform terminology, but UFUQ is not implementing formal PROV
   reasoning.
2. David King's historical books must not be treated as production geodesic algorithm
   specifications.
3. Karney supplies geodesic algorithms but does not supply or approve UFUQ's Kaaba
   target coordinates.
4. *Fundamental Astronomy* is explanatory support, not the final authority over SOFA,
   IERS, catalogue metadata, code-independent reference results, or later
   lineage-independent evidence.
5. IERS Technical Note 36 is the official registered 2010 baseline. Later corrected
   chapters and non-registered working versions must be tracked separately and must not
   be silently merged with or promoted to official TN36. Centre-linked supporting
   documentation is not part of the official distribution or the same review process.
6. FAIR provides guidance. Do not claim formal FAIR compliance.
7. Kunitzsch, Ibn Qutaybah, Hafez, and King do not by themselves establish specifically
   Najdi usage.
8. Hafez/al-Ṣūfī is a Greco-Arabic and historical crosswalk, not a Najdi authority.
9. Ibn Qutaybah supports `OLD_ARABIAN` evidence but does not make every item
   `NAJDI_TRADITION`.
10. *Software Architecture in Practice* is a review guardrail. It must not cause
    architecture redesign without a demonstrated quality-attribute or dependency
    problem.

## Study and synthesis index

`READING_PLAN.md` defines the scoped study method, and
`PDF_KNOWLEDGE_COVERAGE.md` records coverage and reliability. Claim-level notes are
under `studies/`; cross-source authority and conflict resolution rules are under
`syntheses/`.

| Source IDs | Dossier |
|---|---|
| `SOFA-2023-10-11` | `studies/iau-sofa-2023-10-11.md`; 2C.4 extraction in `studies/refraction-horizon-visibility.md` |
| `IERS-TN36-2010` | `studies/iers-conventions-2010.md` |
| `IERS-BULLETIN-A` / `IERS-FINALS2000A-FORMAT` / `IERS-BULLETIN-B` / `IERS-BULLETIN-C` / `RFC3339-TIMESTAMP` / `IANA-TZDB-LEAPS` | `studies/iers-eop-leap-second-products.md` |
| `FUND-ASTRO-6E` | `studies/fundamental-astronomy-6e.md` |
| `EXSUP-3E` | `studies/explanatory-supplement-3e.md` |
| `HIP-I311-README` | `studies/hipparcos-i311-readme.md` |
| `HIP-I311-APPENDIX-G` | `studies/hipparcos-i311-readme.md` |
| `ESA-HIP-1997-V1` | `studies/hipparcos-esa-1997-field-semantics.study.md` |
| `ESA-GAIA-DR1-I311-EPOCH` | `studies/hipparcos-i311-readme.md` |
| `ASTROPY-DOCS-PIN` / `PYERFA-PIN` | `studies/astropy-pyerfa-reference-docs.md`; 2C.4 extraction in `studies/refraction-horizon-visibility.md` |
| `CDS-CATALOGUE-STANDARD-2.0` | `studies/hipparcos-i311-readme.md` |
| `VAN-LEEUWEN-2007-VALIDATION` | `studies/hipparcos-i311-validation.md` |
| `KARNEY-2012-ARXIV-V2` / `KARNEY-2013` | `studies/karney-geodesics.md` |
| `IBN-QUTAYBA-ANWA` | `studies/ibn-qutayba-kitab-al-anwa.md` |
| `KUNITZSCH-1961` | `studies/kunitzsch-1961-sternnomenklatur.md` |
| `HAFEZ-2010` | `studies/hafez-2010-al-sufi.md` |
| `KING-1993` | `studies/king-1993-astronomy-service-islam.md` |
| `KING-1999` | `studies/king-1999-world-maps-qibla.md` |
| `JSON-SCHEMA-CORE-2020-12` / `JSON-SCHEMA-VALIDATION-2020-12` | `studies/json-schema-2020-12.md` |
| `ISO20022-JSON-2025` | `studies/iso20022-json-schema-generation-2025.md` |
| `PROV-SEM-2013` | `studies/prov-semantics-2013.md` |
| `FAIR-2016` | `studies/fair-principles-2016.md` |
| `BASS-ET-AL-2022` | `studies/software-architecture-in-practice-4e.md` |
| `WILSON-ET-AL-2014` | `studies/best-practices-scientific-computing-2014.md` |
| `WILSON-ET-AL-2017` | `studies/good-enough-practices-2017.md` |
| `KANEWALA-BIEMAN-2014` / `KANEWALA-BIEMAN-2018-PREPRINT` | `studies/testing-scientific-software.md` |

The five synthesis files are:

- `syntheses/engineering-quality-synthesis.md`;
- `syntheses/astronomy-model-synthesis.md`;
- `syntheses/catalogue-provenance-synthesis.md`;
- `syntheses/qibla-geodesy-synthesis.md`; and
- `syntheses/arabian-sky-evidence-synthesis.md`.
