# Phase 1 Milestone 2B: catalogue authority and provenance

**Review date:** 2026-07-26  
**Scope:** Decisions and schemas only; no catalogue row was parsed, copied, generated,
tracked, or deployed.

## Gate

Milestone 2B completes the local, non-redistributing parser contract. Implementation is
deferred to **Phase 1 / Milestone 2E** after Milestone 2C defines the Scientific
Behaviour Contract and Milestone 2D records the required source/deployment-authority
outcome. It is not ready for a tracked/generated catalogue artifact, deployment,
source-derived astronomy fixture, or learner-facing cultural content.

| Gate | Result | Reason |
|---|---|---|
| Local parsing against the ignored, hash-identified source | **BLOCKED UNTIL MILESTONE 2D** | Source/table/release, fields, units, row policies, candidate selection, schemas, and provenance requirements are explicit, but the required source/deployment-authority outcome is not recorded. |
| Track or redistribute raw I/311 bytes | **BLOCKED** | No catalogue-specific redistribution grant was found. |
| Track or deploy an I/311-derived subset | **BLOCKED** | Derived-subset and deployment permission remain `REDISTRIBUTION_UNRESOLVED`. |
| Treat the proposed HIP list as historical or lesson approval | **BLOCKED** | Every cultural membership, display form, relationship, edge, and teaching role still needs human review. |
| Source-derived astronomy/reference comparison | **BLOCKED** | Production propagation, the epoch time-scale interpretation, and numerical tolerances belong to later astronomy milestones. |

```text
MILESTONE_2B_GATE: PASS_FOR_LOCAL_NONREDISTRIBUTING_PIPELINE_CONTRACT
READY_FOR_MILESTONE_2D_SOURCE_AUTHORITY_RESOLUTION: YES
READY_FOR_PHASE1_MILESTONE_2E_LOCAL_PARSER: NO
READY_TO_TRACK_OR_DEPLOY_SOURCE_DERIVED_ROWS: NO
CULTURAL_MEMBERSHIP_APPROVED: NO
```

## 1. Catalogue authority and exact release

| Decision | Result | Classification and evidence |
|---|---|---|
| Catalogue | CDS/VizieR **I/311, Hipparcos, the New Reduction**, van Leeuwen (2007) | `EXISTING_PROJECT_DECISION`; official [I/311 catalogue record](https://cdsarc.cds.unistra.fr/viz-bin/cat/I/311). |
| Phase 1 source table | `hip2.dat`, the main astrometric catalogue | `SOURCE_DEFINED`; official [I/311 ReadMe](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/I/311?format=html&tex=true), file summary and byte description. |
| Archive variant | Author-replacement files dated **2008-09-16** | `SOURCE_DEFINED`; ReadMe Notice and History say the earlier June–15 September files contained errors and record replacement files on 16 September 2008. |
| Original-catalogue support | None | `EXISTING_PROJECT_DECISION`; I/239 is historical/scientific context only and no dual-catalogue parser, fixture, benchmark, or migration is planned. |
| Reference frame | `ICRS` | `SOURCE_DEFINED`; I/311 ReadMe fields `RArad` and `DErad`. |
| Reference epoch | source notation `Ep=1991.25`, numeric value `1991.25` | `SOURCE_DEFINED`; I/311 ReadMe. The I/311 metadata inspected does not separately define the epoch time scale. The parser must preserve `UNSPECIFIED_BY_I311_METADATA`; astronomy code must not silently copy the original catalogue's `J1991.25(TT)` statement. |

The local raw source remains ignored and has `I311_ACQUISITION_PROVENANCE: PARTIAL`.
The source structure already recorded in Milestone 1 is:

| File | Bytes | Records | Fixed width | SHA-256 |
|---|---:|---:|---:|---|
| `hip2.dat` | 32,673,535 | 117,955 | 276 | `c45d6325bd59dd691764af173a9702e543804a2b6c1d9fea59210e8332e50a4a` |
| `hip7p.dat` | 173,940 | 1,338 | 129 | `6928e0480d0f29620c0aef842ae71821d17d3a6a7a1ebe6b7f4ab86cc9838f20` |
| `hip9p.dat` | 28,600 | 104 | 274 | `93d563896f37ae7cb422ebfe36bef4c91aa8f7c49f098ea12a811306bcc65dba` |
| `hipvim.dat` | 3,250 | 25 | 129 | `9a564a255429c319af85cf23089eb31809ab291a0fcc1198c88796ff7a511baa` |

These hashes identify the local bytes; they do not prove the original acquisition URL,
timestamp, transport authenticity, or redistribution rights.

## 2. Licence, use, redistribution, and attribution

The official [VizieR rules of use](https://cds.unistra.fr/vizier-org/licences_vizier.html)
permit VizieR data use in a scientific context and require explicit citation of the
original authors and publication references, including the publisher. They request
VizieR acknowledgement and identify service DOI `10.26093/cds/vizier`. The rules also
say catalogue copyright depends on data origin and direct users to the catalogue
ReadMe or origin/publisher policy.

The I/311 ReadMe identifies Floor van Leeuwen, the 2007 new-reduction book, and the
associated A&A publication, but it does not state a licence granting republication of
raw or derived data. ESA's official page applies `CC BY-NC 3.0 IGO` and “Credit: ESA”
to the **original 1997 Hipparcos and Tycho Catalogues**. That licence is not silently
transferred to van Leeuwen's later I/311 reduction.

| Use | Status | Enforced project decision |
|---|---|---|
| Access official metadata | `LICENSING_CONFIRMED` | Record source URLs and access evidence. |
| Local FYP scientific processing of ignored bytes | `LOCAL_USE_ONLY` | Allowed for the technical spike, with citation and no redistribution claim. |
| Commit or republish raw I/311 bytes | `REDISTRIBUTION_UNRESOLVED` | Prohibited. |
| Commit a generated I/311 subset | `REDISTRIBUTION_UNRESOLVED` | Prohibited, even if transformed or small. |
| Deploy generated rows to learners | `REDISTRIBUTION_UNRESOLVED` | Prohibited. |
| Publish aggregate validation results, schema, code, and non-row provenance | `LICENSING_CONFIRMED` for project-created material | Must not enable reconstruction of prohibited rows; cite source and method. |

Every future source manifest must record the I/311 catalogue citation, van Leeuwen
book/article citation, VizieR catalogue/service acknowledgement, terms URLs, use
classification, and the `BLOCK_TRACKING_AND_DEPLOYMENT` decision. Clarification for
derived-subset redistribution must come from CDS (`cds-question@unistra.fr`) and any
data-origin rights holder or publisher CDS identifies. No message was sent in this
milestone.

## 3. Parser field and unit contract

The parser contract defined by Milestone 2B requires the Phase 1 / Milestone 2E parser
to read all fields in the main I/311 row so that it does not hide solution, quality,
multiplicity, uncertainty, covariance, or photometric evidence.
`packages/catalogue-schema/src/catalogue/` records the exact byte ranges and normalized
names.

| Group | Source fields | Source units | Normalized policy |
|---|---|---|---|
| Identity/control | `HIP`, `Sn`, `So`, `Nc`, `ic` | none | Preserve raw codes; decode `Sn` without discarding it. |
| Astrometry | `RArad`, `DErad`, `Plx`, `pmRA`, `pmDE` | rad, rad, mas, mas/yr, mas/yr | ICRS at source epoch `Ep=1991.25`; preserve negative parallax as a measurement, not as a parse error. |
| Formal errors | `e_RArad`, `e_DErad`, `e_Plx`, `e_pmRA`, `e_pmDE` | mas, mas, mas, mas/yr, mas/yr | Non-negative; `e_RArad` is normalized as the `alpha-star` component error. |
| Quality/fit | `Ntr`, `F2`, `F1`, `var` | none, source-unspecified, percent, source-unspecified | Preserve; do not invent units for fields marked `---`. |
| Photometry | `Hpmag`, `e_Hpmag`, `sHp`, `VA`, `B-V`, `e_B-V`, `V-I` | mag except `VA` | `B-V`, its error, and `V-I` may be `null` only for a blank source field; never coerce missing values to zero. |
| Weight data | `UW` | no single unit declared | Preserve exactly 15 finite numeric values and the source's `C^-1 = U^T U` semantics; do not call the mixed-unit matrix dimensionless. |

For `Sn` families 7, 9, or 3, the parser must also require exactly one matching
`hip7p.dat`, `hip9p.dat`, or `hipvim.dat` record and preserve every source-defined
supplemental field and weight-matrix value. A missing, duplicate, mismatched, or
unexpected supplement is fatal. No supplement is permitted for a five-parameter or
stochastic main solution.

## 4. I/311 `pmRA` decision

The official I/311 archive's *Hipparcos, the new reduction*, Appendix G, Table G.3
(printed p. 407) labels the byte-52 field `mu_alpha,*`, in mas/yr. Tables G.5–G.6
(printed p. 408) use the same starred-alpha convention for right-ascension acceleration
terms. This is I/311-specific evidence, not a transfer from ESA SP-1200.

Therefore:

```text
I/311 pmRA = mu_alpha_star = (d alpha / dt) cos(delta)
normalized field = properMotionRaCosDecMilliarcsecondsPerYear
Astropy mapping = pm_ra_cosdec, directly after unit conversion
```

The parser and schema must not expose an ambiguous `pmRa` normalized field. Production
propagation must neither multiply nor divide this source value by `cos(delta)` when
supplying Astropy `pm_ra_cosdec`. High-declination and accidental double-cosine tests
remain required in the astronomy milestone; this catalogue decision does not set an
astronomical tolerance.

`PMRA_SEMANTICS: CONFIRMED_FOR_I311`

## 5. Row, solution, quality, and multiplicity policies

| Case | Required behavior |
|---|---|
| Allowlisted HIP absent from `hip2.dat` | Fail the complete build; report the missing HIP without substituting another object. |
| Duplicate HIP in `hip2.dat` | Fail before normalization; one numeric HIP key must resolve to exactly one main row. |
| Non-allowlisted row | Ignore without parsing into the selected artifact; never use magnitude or Western-constellation membership as an implicit selector. |
| Wrong fixed width, non-ASCII source byte, invalid integer/number, non-finite normalized value, or out-of-range RA/Dec/error/percent/annex value | Fail with file, record number, source field, and reason; never skip silently. |
| Blank required scientific/control field | Fail. |
| Blank `B-V`, `e_B-V`, or `V-I` | Preserve as `null`, record the missing optional photometric field, and do not infer colour. |
| Negative parallax | Preserve; it is not a parser failure or a distance estimate. |
| `Sn` family 0 | Preserve evidence but block selected-artifact acceptance because no new solution is available. |
| `Sn` family 1, 3, 7, or 9 | Preserve and require explicit row-level astronomy review; 3/7/9 also require the exact supplement. Do not silently reduce them to five parameters. |
| `Sn` family 5 | Structurally eligible, but still requires row-level quality review. |
| Peculiarity flags, `Nc > 1`, photocentre, secondary, or component-qualified cross-ID | Preserve all source flags. Do not split, merge, or invent a component. Block learner-facing identity until the scientific crosswalk is reviewed. |
| `F2`, `F1`, uncertainty, weight, transit, variability, or photometry concern | Preserve and report. No unrecorded quality threshold or row drop is permitted. |

The Phase 1 selection is an explicit HIP allowlist, not a magnitude threshold. Quality
review happens after parsing and may reject a candidate, but it may not silently replace
one or widen the list.

## 6. Proposed HIP-ID review allowlist

This is an exact **technical retrieval candidate** of 19 unique numeric HIP IDs. It is
not approved historical membership or lesson content. The existing sources leave
unqualified “Banāt Naʿsh” ambiguous between greater and lesser groups, so both
seven-object scholarly crosswalks are included for review instead of silently choosing
one. Scientific HR/Bayer/HIP equivalences were checked through an identifier-only
SIMBAD TAP query on 2026-07-26; no coordinates or catalogue rows were retrieved.

All Arabic spelling, transliteration, translation, source tradition, membership,
subgroup role, pattern geometry, directional relationship, and instructional
suitability below are `FALAK_OR_CULTURAL_REVIEW_REQUIRED`.

### Al-Jady review candidate

| HIP ID | Scientific identity | Intended educational role | Evidence and status |
|---:|---|---|---|
| 11767 | HR 424; alpha UMi | Candidate target star for the historically named polar-star claim; also appears in the lesser-group candidate | Hafez Tables 18/24 (thesis pp. 314/322) proposes HR 424/Polaris; Kunitzsch entry 107a (printed pp. 62–63) discusses the polar-name readings; SIMBAD supplies HR–HIP cross-ID. Mapping and display form remain unapproved. |

### Banāt Naʿsh greater-group review candidates

| HIP ID | Scientific identity | Intended educational role | Evidence and status |
|---:|---|---|---|
| 53910 | HR 4295; beta UMa | Candidate member of the four-object portion | Hafez Table 19 and Table 26 crosswalk; SIMBAD identifier cross-ID. Exact membership/role requires review. |
| 54061 | HR 4301; alpha UMa | Candidate member of the four-object portion | Same evidence/status. |
| 58001 | HR 4554; gamma UMa | Candidate member of the four-object portion | Same evidence/status. |
| 59774 | HR 4660; delta UMa | Candidate member of the four-object portion | Same evidence/status. |
| 62956 | HR 4905; epsilon UMa | Candidate member of the three-object portion | Hafez Table 19/26 crosswalk; SIMBAD identifier cross-ID. Exact membership/role requires review. |
| 65378 | HR 5054; zeta-1 UMa; SIMBAD component identifier `HIP 65378A` | Candidate member of the three-object portion | Hafez Table 19/26 crosswalk; SIMBAD component-qualified cross-ID. I/311 uses a numeric HIP key, so the system/component relation is a mandatory astronomy-review item. |
| 67301 | HR 5191; eta UMa | Candidate member of the three-object portion | Hafez Table 19/26 crosswalk; SIMBAD identifier cross-ID. Exact membership/role requires review. |

### Banāt Naʿsh lesser-group review candidates

| HIP ID | Scientific identity | Intended educational role | Evidence and status |
|---:|---|---|---|
| 11767 | HR 424; alpha UMi | Candidate member of the three-object portion and separate polar-target claim | Hafez Table 18 crosswalk and Tables 18/24 polar claim; SIMBAD identifier cross-ID. |
| 85822 | HR 6789; delta UMi | Candidate member of the three-object portion | Hafez Table 18 crosswalk; SIMBAD identifier cross-ID. Exact membership/role requires review. |
| 82080 | HR 6322; epsilon UMi | Candidate member of the three-object portion | Same evidence/status. |
| 77055 | HR 5903; zeta UMi | Candidate member of the four-object portion | Same evidence/status. |
| 79822 | HR 6116; eta UMi | Candidate member of the four-object portion | Same evidence/status. |
| 72607 | HR 5563; beta UMi | Candidate member of the four-object portion | Same evidence/status. |
| 75097 | HR 5735; gamma UMi | Candidate member of the four-object portion | Same evidence/status. |

### Dhāt al-Kursī review candidates

Hafez uses *Dhāt al-Kursīy* as a Cassiopeia catalogue heading (PDF p. 151), but the
reviewed evidence does **not** establish a five-star historical membership or a W-shaped
line drawing. The following five objects are therefore only a bounded modern technical
review set. Their Western constellation membership is not treated as sufficient
evidence for the Arabic historical identification.

| HIP ID | Scientific identity | Intended educational role | Evidence and status |
|---:|---|---|---|
| 746 | HR 21; beta Cas | Candidate object for domain review of a possible modern five-object teaching pattern | Hafez heading supports only the constellation-level scholarly label; SIMBAD supplies HR/Bayer/HIP identity. Membership, role, ordering, and edges are unapproved project proposals. |
| 3179 | HR 168; alpha Cas | Same candidate role | Same evidence/status. |
| 4427 | HR 264; gamma Cas | Same candidate role | Same evidence/status. |
| 6686 | HR 403; delta Cas | Same candidate role | Same evidence/status. |
| 8886 | HR 542; epsilon Cas | Same candidate role | Same evidence/status. |

Sorted unique candidate retrieval list:

```text
746, 3179, 4427, 6686, 8886, 11767, 53910, 54061, 58001, 59774,
62956, 65378, 67301, 72607, 75097, 77055, 79822, 82080, 85822
```

No line segment, sequence, route, directional method, Arabic display label, or
learner-facing explanation is approved by this list.

## 7. Scientific and cultural separation

- A normalized catalogue row contains only numeric HIP identity, source astrometry,
  solution/multiplicity/quality fields, photometry, uncertainties, weight data, and
  explicit source metadata.
- Arabic strings, transliterations, historical claims, aliases, proposed HIP links,
  pattern membership, edges, guidance relationships, and teaching roles belong only in
  reviewed curation records.
- A curation record references a numerical row by `HIP` ID; it never duplicates a
  coordinate or overwrites a catalogue field.
- A valid identifier crosswalk proves object identity only. It does not prove a
  historical name, membership, line geometry, directional use, or pedagogical
  suitability.
- A learner-facing build fails unless every curation record is human-approved and every
  referenced HIP is present in the scientifically reviewed numerical artifact.

## 8. Canonical schemas, provenance, and checksums

`@ufuq/catalogue-schema` now exposes Draft 2020-12 schema constants for:

- a normalized I/311 main record;
- 7-parameter, 9-parameter, and VIM supplements;
- a numerical catalogue artifact; and
- its provenance manifest.

No runtime validator dependency is selected in this milestone. Phase 1 / Milestone 2E
must either implement a small documented validator at the trust boundary or propose a
dependency with conformance evidence; schema declarations alone are not validation.

The canonical payload rules are: UTF-8 without BOM, NFC text, LF with one trailing
line feed, lexicographically ordered object keys, records sorted by numeric HIP ID,
schema-defined order for other arrays, finite shortest-round-trip JSON numbers,
negative zero normalized to zero, and no volatile timestamp/path/username field.

The companion provenance manifest must contain:

- source catalogue/table/archive variant and URLs;
- acquisition UTC/method plus every ignored raw relative path, exact byte
  length/count/width, and SHA-256;
- acquisition-provenance status;
- terms URLs, required attribution, use status, and redistribution decision;
- exact sorted HIP selection, selection evidence, and approval status;
- generator name/version/Git commit;
- schema IDs;
- canonicalization policy; and
- artifact relative path, byte length, record count, and SHA-256.

The artifact does not contain its own hash. The companion manifest or `.sha256` record
hashes the final canonical artifact bytes. Same approved inputs, tool version, schema,
and policy must reproduce byte-identical output. Volatile acquisition/review events
belong in non-canonical audit metadata.

## 9. Required human approvals

| Approval | Authority | Blocks |
|---|---|---|
| Confirm local FYP use falls within the intended scientific-use scope and accept the no-redistribution operating rule | Supervisor/data owner; legal/licence clarification if required | Local pipeline authorization beyond this technical record |
| Obtain explicit terms for committing or deploying any I/311-derived subset | CDS/data-origin rights holder or publisher, then supervisor records the decision | Git tracking, distribution, deployment |
| Confirm the proposed greater/lesser-group interpretation, Al-Jady identity, and every membership/source claim | Qualified falak, Arabic, and historical-domain reviewer | Curation approval and learner-facing content |
| Decide whether either Banāt group, both, or neither is in product scope | Supervisor after domain evidence | Final allowlist and lesson scope |
| Review the five Dhāt al-Kursī candidates without treating the modern W pattern as historical proof | Qualified falak/historical-domain reviewer | Any Dhāt pattern or route |
| Review HIP 65378 system/component semantics and every selected row's `Sn`, `Nc`, uncertainty, fit, variability, and supplement evidence | Astronomy/domain reviewer | Scientific row approval |
| Approve any line drawing, guidance relationship, and instructional role independently from name/membership evidence | Falak/cultural reviewer plus supervisor/education reviewer | Pattern geometry and lesson route |
| Approve the I/311 epoch time-scale mapping and production propagation/effect policy | Astronomy reviewer | Source-derived astronomy and reference comparison |

## 10. Phase 1 / Milestone 2E entry contract

After Milestones 2C and 2D, Phase 1 / Milestone 2E should implement only a **local,
read-only, allowlist-first I/311 parser and validator**:

1. verify the ignored source file identities before reading;
2. parse exact fixed-width fields and required supplements;
3. normalize to the versioned schemas without astronomy propagation;
4. use the 19-ID list only as `TECHNICAL_CANDIDATE_ONLY`;
5. produce output only in ignored local storage while redistribution is unresolved;
6. emit a provenance manifest and checksum beside that ignored output;
7. fail on missing/duplicate/invalid/ambiguous supplement conditions;
8. report all solution, multiplicity, uncertainty, fit, variability, and optional-field
   observations for later human review;
9. prove deterministic bytes with a second build; and
10. add only synthetic parser contract tests to Git unless source-derived test data is
    separately authorized.

Phase 1 / Milestone 2E must not propagate coordinates, create Astropy reference
expectations, render stars, approve cultural content, invent pattern edges, or make a
source-derived artifact trackable.
