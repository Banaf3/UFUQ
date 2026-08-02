# Arabian sky evidence synthesis

## Scope and non-approval rule

This synthesis compares Ibn Qutaybah, Kunitzsch, Hafez/al-Sufi, and King's historical
context for a small set of UFUQ-relevant names and patterns. It does not approve any
Arabic text, translation, modern identification, membership, line segment, guidance
relationship, or lesson route.

Every atomic claim must be classified as exactly one of:

- `OLD_ARABIAN`;
- `NAJDI_TRADITION`;
- `GRECO_ARABIC_SCHOLARLY`;
- `CROSS_REGIONAL_ARABIAN`; or
- `MODERN_PEDAGOGICAL`.

No studied source provides the explicit Najdi regional evidence required for
`NAJDI_TRADITION`.

## Authority and source roles

| Source | Permitted role | Critical limitation |
|---|---|---|
| Ibn Qutaybah, *Kitab al-Anwa* | Claim-specific `OLD_ARABIAN` evidence and historical stellar-guidance context | Local edition, pagination, completeness, and provenance are unverified; local pages are discovery pointers only. |
| Kunitzsch 1961 | Philological layering, source criticism, reading variants, conflict/negative mapping checks | OCR, German translation, Arabic reconstruction, and Greek-letter strings need page-image/human review; not a Najdi source. |
| Hafez 2010 / al-Sufi crosswalk | `GRECO_ARABIC_SCHOLARLY` manuscript/translation and HR crosswalk evidence | Secondary thesis; HR mappings are provisional and not coordinates, cultural approval, or Najdi evidence. |
| King 1993/1999 | Islamic astronomy/Qibla historical context and method distinctions | Not a star-membership, Arabic-name, modern geodesy, or Najdi authority. |
| Future Najdi/regional source and human reviewer | Required authority for `NAJDI_TRADITION` and learner-facing cultural approval | Currently missing under `CULT-SRC-001` through `CULT-SRC-004`. |

## Cross-source findings

### Banat Na'sh greater and lesser groups

Ibn Qutaybah sections 31-32 describe greater and lesser seven-star groups in
four-plus-three arrangements. Kunitzsch entries 55-56 compare the transmitted
philological and al-Sufi identifications. Hafez's Ursa chapters and Tables 18-19/24/26
provide Greco-Arabic scholarly HR crosswalks.

These sources agree that distinct greater and lesser groups and four/three
substructures were transmitted. They do not jointly approve current catalogue IDs,
line segments, an instructional route, a Najdi classification, or one English gloss
for `na'sh`.

### Al-Jady / al-gady / al-gudayy / al-Juday

Ibn Qutaybah section 31 associates the polar member of the lesser group with historical
direction finding. Kunitzsch entry 107a preserves a reading history between
`al-gady` and later diminutive `al-gudayy`. Hafez uses `al-Juday` and proposes the HR
424/Polaris crosswalk in Tables 18 and 24.

The reading, transliteration, translation, witness, and modern catalogue mapping must
remain separate evidence fields. Historical direction-finding language does not make
Polaris identical to terrestrial True North or supply a modern Qibla calculation.

### Cassiopeia and “chair” terminology

Hafez uses *Dhat al-Kursiy* as a Cassiopeia catalogue heading, but exact Arabic,
membership, geographical use, and modern instructional pattern remain unapproved.
Kunitzsch entries 148a-149 treat `kursi al-jawza'` as Orion/Lepus/Eridanus-related
material, not Cassiopeia. Lexical similarity is therefore a negative warning, not a
mapping argument. Kunitzsch's Cassiopeia-related `al-kaff` entries are a distinct
claim.

## Agreements

- Arabic transmission language does not prove old Arabian, Bedouin, or Najdi origin.
- Anwāʾ/philological material, Ptolemaic/Greco-Arabic scholarly catalogue material,
  modern crosswalks, and modern pedagogy are different layers.
- Exact Arabic, source witness/edition/location, transliteration, translation, period,
  and geography are required per atomic claim.
- Modern catalogue identification needs its own source/argument and confidence.
- Cultural records link stable catalogue IDs but never contain copied coordinates.
- Historical membership does not define modern line segments or a teaching route.
- Automated schema/referential checks cannot confer cultural approval.

## Conflicts and ambiguities

| Issue | Evidence | Required treatment |
|---|---|---|
| Meaning of `na'sh` | Hafez uses bier/coffin gloss; Kunitzsch entry 55 questions the etymological history | Preserve variants; human philological review. |
| Polar-name reading | Ibn derivative, Kunitzsch entry 107a, and Hafez Tables 18/24 use different normalizations | Store source form and approved transliteration separately; do not collapse silently. |
| Modern star IDs | Hafez HR crosswalk versus source-text descriptions/OCR | Resolve through a versioned approved catalogue crosswalk; no manual coordinate copy. |
| Cassiopeia versus other “chair” terms | Hafez Cassiopeia heading; Kunitzsch entries 148a-149 | Require claim-specific evidence; lexical match is insufficient. |
| Geographical scope | Sources discuss old Arabic or Greco-Arabic/Islamic scholarly traditions | None establishes specifically Najdi usage. |
| Edition stability | Ibn local derivative lacks verified edition/pagination | No learner-facing source claim until a stable edition and review exist. |

## Candidate UFUQ rules

| Rule | Evidence | Classification |
|---|---|---|
| Create one evidence record per atomic name, identification, membership, segment, or route claim. | Cross-source conflicts above; `DATA_STRATEGY.md` | `PROJECT_DECISION` |
| Record exact Arabic, source form, approved transliteration system/output, translation/source, verified edition and page/verse/folio, period, and geography. | Ibn/Kunitzsch/Hafez dossier limitations | `HUMAN_REVIEW_REQUIRED` |
| Assign exactly one evidence classification and keep evidence status separate from human-review status. | `AGENTS.md`; source roles above | `PROJECT_DECISION` |
| A name is not automatically ancient Arabian, Bedouin, or Najdi because it is Arabic. | Kunitzsch Part I.A-C; absence of Najdi evidence | `SOURCE_SUPPORTED_FACT` / stop condition |
| Never assign `NAJDI_TRADITION` without explicit Najdi primary/regional evidence and qualified human review. | `SOURCE_GAPS.md` CULT-SRC-001/003; current source limitations | Unresolved stop condition |
| Treat Hafez/al-Sufi as `GRECO_ARABIC_SCHOLARLY` crosswalk evidence and Ibn only claim-by-claim as `OLD_ARABIAN`. | Dossier source roles | `SOURCE_SUPPORTED_FACT` |
| Map cultural claims to approved modern IDs through a separate argument; keep coordinates in the numerical catalogue. | Hafez/Kunitzsch crosswalk limits; `DATA_STRATEGY.md` | `PROJECT_DECISION` |
| Label a modern line segment or route `MODERN_PEDAGOGICAL` unless exact historical evidence supports that same geometry/relationship. | Source limitations; data-driven route architecture | `PROJECT_DECISION_REQUIRED` |
| Exclude unresolved claims from learner-facing content. | AST-002 and cultural review gaps | Stop condition |

## Required evidence and tests

- A verified edition/witness and claim-level page/verse/folio.
- Page-image verification for OCR-derived Kunitzsch/King details and qualified review
  of Arabic, German, transliteration, and translation.
- Independent modern catalogue-ID crosswalk with conflicts and confidence.
- Separate membership, line-segment, guidance-relationship, and route evidence.
- Negative tests rejecting absent source pointers, copied coordinates, silent variant
  collapse, `kursi al-jawza'` as Cassiopeia evidence, and unsupported
  `NAJDI_TRADITION`.
- Referential integrity and schema validity as technical checks only, never cultural
  approval.

## Unresolved gaps

- A stable approved edition of Ibn Qutaybah for claim-level citation.
- Najdi primary/regional evidence, including Rashid al-Khalawi or a credible scholarly
  treatment.
- Human Arabic, philological, cultural, and educational review.
- Approved exact pattern membership, modern catalogue IDs, line segments, guidance
  relationships, and lesson routes.
- A resolved transliteration policy and the source-form variants it must preserve.

