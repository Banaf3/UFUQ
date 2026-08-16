# Phase 1 Milestone 2D.1: production star-catalogue authority

- **Decision date:** 2026-08-16
- **Decision:** `CATALOGUE_AUTHORITY_BLOCKED`
- **Preferred next candidate:** Gaia DR3 version 1.1, table
  `gaiadr3.gaia_source`
- **Scope:** source/release, scientific field authority, row eligibility, identity
  crosswalk, and deployment rights for `ScientificProfileV1`
- **Not performed:** catalogue acquisition, parsing, row normalization, generated
  runtime JSON, production astronomy, or learner/cultural selection

## Decision summary

Gaia DR3 is the strongest single-source-first candidate for the first production
astrometric artifact. Its official data model supplies a TCB-typed Julian reference
epoch, ICRS position, starred-alpha and declination proper motion, parallax, formal
uncertainties/correlations, and a radial-velocity field for a subset of sources. ESA's
dataset record supplies a release DOI/version and CC BY-NC 3.0 IGO rights metadata,
while the release credit page separately says Gaia data are open and free to use with
ESA/Gaia/DPAC credit. Both official statements remain attached to the decision.

Gaia DR3 is **not yet approved as the active UFUQ catalogue**. No row may enter a real
ProfileV1 artifact until a bounded, reproducible official-archive query and row review
establish all required values, physical-component identity, applicable astrometric
covariance, separate RV uncertainty and reviewed joint-covariance disposition,
parallax-systematics disposition, quality, and licence provenance. The TCB-parametrized
source state must be normalized with the approved
`GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1` mapping into V1's TDB propagation interface.
The bounded official TAP screen preliminarily found eight matches among the 19 technical HIP
candidates; all eight have positive raw parallax and five have finite DR3 RV/error.
This establishes only a possible small raw-field-complete technical subset. It approves
no row. `HIP 11767` (the intended Polaris target) has no row in either official DR3
Hipparcos-2 crossmatch table, so a nearby Gaia source may not substitute it and an exact
component-scoped fallback is required.

The existing 19-HIP list remains only a bounded technical query/review candidate. It
does not establish cultural membership, learner-route eligibility, or scientific row
approval. CDS I/311 remains the Phase 1 parser spike source and is not promoted to
production.

## Evidence and classification

| Conclusion | Classification | Evidence or project consequence |
|---|---|---|
| Gaia DR3 was published on 2022-06-13; ESA's dataset record identifies version 1.1, updated 2023-02-07, and DOI `10.5270/esa-qa4lep3`. | `SOURCE_SUPPORTED_FACT` | ESA Gaia DR3 dataset record and documentation release 1.3. |
| Gaia DR4 is still described by ESA as forthcoming; its expected schema is not a released catalogue authority. | `SOURCE_SUPPORTED_FACT` | Official Gaia DR4 page says the data and final documentation will become available. |
| Gaia DR3 `gaiadr3.gaia_source` is the preferred single-source-first ProfileV1 candidate. | `PROJECT_DECISION` | It minimizes field mixing while exposing the required astrometric fields and subset RV in one release. It is not row approval. |
| A complete, unambiguous, quality-reviewed row is mandatory; missing or unapproved epoch/time mapping, position, motion, positive parallax/systematics disposition, RV, applicable uncertainty/covariance, identity, or rights makes that star ineligible. | `PROJECT_DECISION` | Normative `ScientificProfileV1` fail-closed contract. |
| The analytic Gaia DR3 TCB-compatible to UFUQ TDB-compatible parameter/covariance adapter is approved. | `PROJECT_DECISION` based on `SOURCE_SUPPORTED_FACT` | Milestone 2D.1A closes: convert the same epoch event with IAU B3; preserve direction; map proper-motion rates and parallax by `1 / (1 - L_B)`, coordinate distance by `1 - L_B`, and covariance by the recorded Jacobian; do not scale the Gaia spectroscopic-RV measure. This approves no row. |
| A bounded 2026-08-16 official Gaia TAP screen preliminarily found 8/19 Hipparcos-2 matches, 8/8 positive raw parallaxes and 5/8 finite RV/error fields; `HIP 11767` has no official crossmatch row in that screen. | `SOURCE_SUPPORTED_FACT` | Ephemeral field-presence evidence only. Exact ADQL/query text, response/canonical extraction, acquisition timestamp, hashes and query-result manifest were not retained, so the counts are not reproducible 2D authority and no physical component or row was approved. |
| General release documentation and field-presence screening cannot establish row eligibility or the intended physical component. | `AUTHORITY_OR_EVIDENCE_MISSING` | Requires immutable acquisition plus astronomy/data review; Polaris also requires one exact field-specific fallback strategy. |
| The DR3 credit page says Gaia data are open and free to use with ESA/Gaia/DPAC credit; the version 1.1 DOI record separately declares CC BY-NC 3.0 IGO. | `SOURCE_SUPPORTED_FACT` | Access/credit and dataset-specific distribution metadata remain explicit; neither statement is silently discarded or selected by assumption as the controlling derived-artifact term. Local analysis and attribution are established, while public tracking and derived-output deployment require an exact rights interpretation. |
| ESA Hipparcos 1997 is a possible bright-star astrometry fallback, but it is not a complete V1 source because the main catalogue supplies no general RV field. | `SOURCE_SUPPORTED_FACT` plus `PROJECT_DECISION` | Official ESA SP-1200 semantics and current ESA catalogue page. |
| I/311 is not production-eligible on current evidence. | `AUTHORITY_OR_EVIDENCE_MISSING` | Its exact epoch/derivative time scale, RV authority, row approvals, and raw/derived deployment rights remain unresolved. |
| PCRV `III/252` or XHIP `V/137D` may be evaluated only if a mandatory star fails the Gaia-only branch. | `PROVISIONAL_CHOICE` | Both add source mixing; exact row/component suitability and redistribution authority are not established. |

## Candidate comparison

| Candidate | Scientific strengths | Scientific gaps for ProfileV1 | Access, rights, and disposition |
|---|---|---|---|
| Direct ESA Hipparcos 1997 release, legacy table `hipparcos1.hip_main` | Bright-star coverage; ICRS; explicit `J1991.25 (TT)` / JD `2448349.0625 TT`; Julian-year `mu_alpha_star`, declination motion, parallax, formal errors and correlations; stable HIP identifiers and multiplicity records | No general finite RV field; positive parallax, component identity, solution quality, and covariance still require row review | ESA states CC BY-NC 3.0 IGO plus `Credit: ESA` for its direct distribution. Conditional noncommercial fallback candidate, not standalone V1 authority; CDS I/239 rights remain separate. |
| CDS I/311 corrected 2008-09-16 `hip2.dat` | ICRS; Julian `J1991.25` representation; `pmRA = mu_alpha_star`; parallax, errors, inverse-covariance factor, solution/multiplicity fields; improved bright-star reduction | No I/311-applicable epoch or derivative time scale; no RV; row/component/positive-parallax review required; supplementary solution families must remain distinct | Local scientific spike use with citation is supported. Generated-row Git/deployment rights remain `REDISTRIBUTION_UNRESOLVED`; reject as current production authority. |
| Gaia DR3 version 1.1 `gaiadr3.gaia_source` | Fixed official release; ICRS; TCB-parametrized Julian `J2016.0`; explicit `mu_alpha_star`; declination motion; parallax; five-/six-parameter formal covariance inputs; subset barycentric spectroscopic RV with error/diagnostics; official release DOI and crossmatch tables | The bounded screen found eight matches and five finite-RV candidates but no Polaris match. The compatible-quantity adapter is approved; applicable covariance, parallax systematics, RV proxy/systemic suitability, physical components and quality remain row-review gates. | Official credit documentation says open/free with credit; the DOI record separately declares CC BY-NC 3.0 IGO. Local analysis with attribution is allowed. Derived deployment and public tracking are `RIGHTS_INTERPRETATION_REQUIRED`; noncommercial FYP use is only a candidate pending exact licence application. Active catalogue approval remains blocked. |
| Blanket Gaia + Hipparcos/PCRV/XHIP merge | Could fill a bright-star or RV gap on a per-star basis | Adds component/crossmatch ambiguity, distinct uncertainty models, compiled/variable RV questions, release conflict rules, and per-field authority | Rejected as the default. The smallest Polaris candidate is direct ESA Hipparcos 1997 astrometry plus one reviewed primary systemic-RV authority; PCRV/XHIP are evidence bridges, not an approved flattened source. |

## Gaia DR3 field-authority candidate

The following are source-supported Gaia DR3 meanings. They define what the future
adapter must preserve; they do not approve any row or quality threshold.

| Profile field | Candidate source authority | Required UFUQ disposition |
|---|---|---|
| Release | ESA Gaia DR3 version 1.1, DOI `10.5270/esa-qa4lep3`; documentation release 1.3 | Pin exact table/query, archive endpoint, response bytes, query text, retrieval identity, and hashes during acquisition. |
| Frame and position | `ra`,`dec`: barycentric ICRS coordinates at `ref_epoch` | Require finite values and retain native units/metadata before normalization. |
| Epoch/time coordinate | `ref_epoch`: Julian year in TCB; DR3 reference epoch `J2016.0`; Gaia catalogue astrometry is TCB-parametrized; IAU 2006 B3 defines the TCB-to-TDB time transformation | Preserve exact native `J2016.0 TCB`/`JD(TCB) 2457389.0`. Convert the same event to two-part `JD(TDB)` with B3; never relabel the epoch or treat the conversion as propagation. |
| RA proper motion | `pmra = mu_alpha_star = mu_alpha cos(delta)` in mas per TCB Julian year; `ra_error` and `pmra_error` use the starred tangent-plane basis | Preserve the native starred-alpha field, then map it once by `1 / (1 - L_B)` to per-TDB-Julian-year `mu_alpha_star`. Convert to coordinate `dRA/dt` only at the SOFA boundary; never apply or remove `cos(delta)` twice. |
| Dec proper motion | `pmdec` toward increasing declination in mas per TCB Julian year | Map once by `1 / (1 - L_B)` to the TDB-compatible rate; require finite value and complete normalization evidence. |
| Parallax | `parallax` and `parallax_error`, with release-specific systematic/known-issue evidence | Map the compatible catalogue parameter once by `1 / (1 - L_B)`; a derived coordinate distance maps by `1 - L_B`. Separately require finite positive source parallax and an approved release-pinned systematics correction or omission disposition. |
| Astrometric uncertainty/covariance | Five-parameter solutions publish five errors and ten correlations; six-parameter solutions additionally publish pseudocolour/error and five pseudocolour correlations | Reconstruct and retain the complete applicable native covariance. Apply `D C D^T`: `D_5=diag(1,1,K_B,K_B,K_B)` for `[delta_alpha_star,delta_delta,parallax,mu_alpha_star,mu_delta]`; extend to `D_6=diag(1,1,K_B,K_B,K_B,1)` for pseudocolour solutions. Preserve the full 6D evidence even when V1 consumes its 5D astrometric principal submatrix. Missing astrometry-RV covariance remains `UNKNOWN_NOT_PROVIDED`, never zero. |
| Radial velocity | `radial_velocity`: multi-transit Solar-system-barycentric spectroscopic RV in km/s; `radial_velocity_error` and RV diagnostics; no published astrometry-RV cross-covariance in the main astrometric block | Preserve value/error unchanged as an observational measure; do not scale or relabel it as coordinate velocity. A component review must approve its positive-receding mapping and explicit propagation-proxy role. A catalogue mean is not automatically an approved systemic velocity. |
| Quality | Astrometric solution, goodness-of-fit/RUWE, excess-noise, IPD, observation/visibility-period, duplicate, RV transit/method/deblend, variability, non-single-star, and release-known-issue evidence as applicable | Preserve source fields and the exact release-known-issue review, then produce an explicit reviewer disposition. This audit selects no numeric quality cut. |
| Identity | DR3 `source_id`, `solution_id`, designation, and official Hipparcos-2 crossmatch evidence | Treat 64-bit identifiers as release-scoped opaque decimal strings in JSON. Crossmatch proximity is evidence, not physical-identity or row-eligibility approval. |

Candidate row eligibility is therefore a conjunction, not a score. Every required
field and identity assertion must independently be `AVAILABLE`, source-typed,
quality-reviewed, and `APPROVED`. One valid field, row, match, or source release never
promotes another.

## Radial-velocity and bright-star stop rule

ScientificProfileV1's full-space-motion input remains unchanged. The catalogue audit
does not loosen it for catalogue convenience:

1. use Gaia DR3 RV only when the same reviewed physical source/component has a finite
   value, uncertainty, applicable diagnostics, source-pinned sign mapping, and explicit
   approval;
2. do not assume Gaia DR3 contains RV for every astrometric source;
3. do not use `0 km/s`, a SIMBAD aggregate, a neighbouring component, or a catalogue
   mean for a variable/multiple system without field-specific authority;
4. if an instructional star is Gaia-ineligible, either approve an exact supplemental
   source/crossmatch with its own rights and provenance or mark the star/profile route
   ineligible;
5. never replace Polaris A with Polaris B or another nearby source merely because the
   latter has a complete Gaia row.

### Current bounded row screen

No coordinate or measured catalogue value is copied here. `Matched` means only that
the official DR3 Hipparcos-2 tables returned one neighbour in this bounded screen.

| HIP | DR3 state needed for the authority decision |
|---|---|
| `746` | No match; Gaia-only branch fails. |
| `3179` | Six-parameter match with positive raw parallax; RV missing. |
| `4427` | No match; Gaia-only branch fails. |
| `6686` | Six-parameter match with positive raw parallax; RV missing. |
| `8886` | No match; Gaia-only branch fails. |
| `11767` | No match; intended Polaris component requires a field-specific fallback. |
| `53910` | No match; Gaia-only branch fails. |
| `54061` | No match; Gaia-only branch fails. |
| `58001` | No match; Gaia-only branch fails. |
| `59774` | Six-parameter match with positive raw parallax and finite RV/error; NSS evidence requires review. |
| `62956` | No match; Gaia-only branch fails. |
| `65378` | Six-parameter match with positive raw parallax; RV missing and component identity requires review. |
| `67301` | No match; Gaia-only branch fails. |
| `72607` | No match; Gaia-only branch fails. |
| `75097` | No match; Gaia-only branch fails. |
| `77055` | Six-parameter match with positive raw parallax and finite RV/error; review required. |
| `79822` | Five-parameter match with positive raw parallax and finite RV/error; review required. |
| `82080` | Six-parameter match with positive raw parallax and finite RV/error; RV uncertainty/quality review required. |
| `85822` | Five-parameter match with positive raw parallax and finite RV/error; review required. |

The five raw-field-complete matches demonstrate that a small technical Gaia subset may
exist. They are not approved rows, a final teaching set, or cultural membership. Every
no-match or missing-RV state remains recorded rather than silently dropping the star.

The bounded row audit must cover all 19 technical HIP candidates and report at least:
no match; every candidate match; neighbour/mate or split/merge evidence; physical
component scope; five-/six-/two-parameter solution state; required astrometric values;
positive raw parallax and zero-point/systematics disposition; complete applicable
astrometric covariance; separate RV error and absent joint-covariance disposition;
relevant astrometric/RV, variability and non-single-star diagnostics; and the reviewer
disposition. When main-row flags indicate them, retrieve and review every applicable
official DR3 NSS/variability/RV record rather than treating a boolean flag as evidence.
It must
separately identify `HIP 11767` and component-qualified `HIP 65378A`. This does not
approve either object's cultural role.

For `HIP 11767`, the original Hipparcos 1997 main row supplies an explicit TT epoch,
astrometry, positive parallax and formal errors/correlations, but no RV and no main-row
field that resolves the known `Polaris Aa+Ab` spectroscopic system for this use. PCRV
and XHIP expose compiled RV evidence; XHIP's component-A record points to an older
spectroscopic-binary source but also carries I/311 astrometry if adopted wholesale.
Neither compilation is approved as the V1 systemic-RV authority. Torres (2023) is a
more direct primary candidate for the Polaris-system orbit/systemic velocity, but its
physical scope, convention, uncertainty, crosswalk and derived-value rights still need
2D review. The proposed fallback shape is therefore direct ESA Hipparcos 1997
astrometry plus one exact primary systemic-RV authority, with independent per-field
provenance; the authority pairing remains blocked.

## Stable UFUQ identity and crosswalk contract

`starId` is an opaque, stable UFUQ identity and never a HIP number, Gaia `source_id`,
display name, transliteration, or copied coordinate. The crosswalk must model, rather
than flatten, source authority:

```text
StarIdentity
  starId
  physicalScope: SYSTEM | COMPONENT

SourceRecordRef
  sourceFamily + release + table + opaqueStringRowId + optional componentId
  acquisition/query manifest and artifact hash

StarSourceLink
  starId + SourceRecordRef
  asserted relationship + identity authority/evidence + approval

CrossmatchEvidence
  crossmatch authority/release/table
  both source records + match metrics/flags/multiplicity
  component-resolution evidence + approval

FieldAuthorityAssertion
  owned field set
  native and normalized value semantics
  uncertainty/covariance + quality + provenance + approval
```

Multiple records and candidate links may coexist. Each ProfileV1 data release selects
exactly one approved active authority for each required scientific field. “Newest
wins”, row-order joins, closest-position-only joins, or silent merging are prohibited.
An ambiguous match, multiple mate, source split/merge, component mismatch, or authority
conflict fails closed.

## Reproducibility and maintenance

Gaia DR3 is a fixed, DOI-identified official release with an official archive and
versioned documentation; forthcoming DR4 does not mutate or silently supersede it.
Reproducibility still requires retaining the exact ADQL, response bytes, retrieval
identity, and hashes because a live service is not itself an immutable UFUQ artifact.
Gaia source identifiers remain release-scoped.

The direct ESA Hipparcos 1997 release is a stable historical scientific dataset, not an
unmaintained software dependency, but its lack of general RV prevents a standalone V1
selection. I/311, PCRV, and XHIP are also fixed scientific releases; their risks are
source-semantic, component-matching, field-mixing, and redistribution authority rather
than software age. No runtime catalogue client, CDN, hidden update, or live archive
query is approved. A future release change creates a new reviewed data version and
crosswalk; it never overwrites a hash-bound historical scenario.

## Rights and deployment

The following classifications apply to the fixed official ESA releases, not to every
CDS-hosted catalogue and not to future Gaia releases.

| Use | Gaia DR3 v1.1 | ESA Hipparcos 1997 | I/311 / PCRV / XHIP |
|---|---|---|---|
| `LOCAL_ANALYSIS_ALLOWED` | `YES`: official documentation says open/free to use with credit | Yes | Scientific-context access with citation; yes for the bounded audit |
| Raw/query-derived source redistribution | `RIGHTS_INTERPRETATION_REQUIRED`; material remains local and ignored | Licence permits noncommercial sharing with conditions; use the direct ESA route and avoid unnecessary bulk tracking | `REDISTRIBUTION_UNRESOLVED` |
| `GENERATED_DERIVED_OUTPUT_DEPLOYMENT` | `RIGHTS_INTERPRETATION_REQUIRED` | Conditional yes, noncommercial | `REDISTRIBUTION_UNRESOLVED` |
| `PUBLIC_GIT_TRACKING` | `RIGHTS_INTERPRETATION_REQUIRED` | Conditional yes for a separately marked small derived artifact | `REDISTRIBUTION_UNRESOLVED` |
| `NONCOMMERCIAL_FYP_USE` | `CANDIDATE_ALLOWED_PENDING_EXACT_LICENSE_APPLICATION` | Conditional candidate | `REDISTRIBUTION_UNRESOLVED` |
| `ATTRIBUTION_REQUIRED` | `YES`: ESA/Gaia/DPAC acknowledgement and mission/release citations; exact licence/notice application remains part of the rights interpretation | `Credit: ESA`, licence link, and change indication | Original authors/publication/publisher plus VizieR acknowledgement; exact grant still required |
| `COMMERCIAL_REUSE` | `NOT_APPROVED` | `BLOCKED` without separate permission | `BLOCKED` |

The broad official statement that Gaia data are open and free to use with credit and
the DOI record's dataset-specific CC BY-NC 3.0 IGO metadata are both recorded. UFUQ
does not collapse the release to the phrase "noncommercial only" and does not choose
which statement controls the planned normalized/derived artifact by assumption.
Local scientific analysis is allowed and attribution is mandatory. Public Git tracking
and generated-derived-output deployment remain blocked on an exact rights
interpretation for that artifact. Noncommercial FYP use is a candidate only pending
that licence application; commercial reuse is not approved. Raw and query-derived
catalogue material remains local and ignored until the interpretation is approved.

## Runtime-artifact requirements for Milestone 2E

No runtime JSON is produced by this decision. A later deterministic scientific artifact
must carry or hash-link:

- `starId`, physical scope, profile/data/schema/generator identities, and approval;
- active source/release/table/row/component references and every retained crosswalk or
  crossmatch assertion;
- source-neutral ICRS RA/Dec, explicit epoch representation/scale, `mu_alpha_star`,
  declination motion, positive parallax/equivalent distance, finite RV, units,
  uncertainties/covariance, quality state, and per-field source authority;
- acquisition/query manifest, exact raw/query-response and normalized-artifact hashes,
  selection rationale, row-review identity, and source/version provenance;
- licence identifier/link, rights holder, permitted-use boundary, attribution/citation,
  modification statement, and deployment approval; and
- explicit failure/ineligibility evidence for omitted candidate rows outside the runtime
  payload or in the review manifest.

All external 64-bit identifiers, including Gaia `source_id` and `solution_id`, are
serialized as exact decimal strings, never JavaScript/JSON numbers.

Cultural names, `SkyPattern` membership, `GuidanceRelationship`, and `LessonRoute`
remain separate upstream authority classes. A generated projection may join only
approved records by `starId`; it may not turn catalogue coordinates or identifiers into
cultural authority.

## Lifecycle ownership

### Milestone 2D.1A closed

The dedicated
[`gaia-tcb-tdb-compatible-quantities.md`](../references/studies/gaia-tcb-tdb-compatible-quantities.md)
record approves the source-pinned analytic epoch, parameter, uncertainty/covariance,
parallax/distance, and RV-type-preservation contract. It returns
`TCB_TDB_ADAPTER_AUTHORITY_CLOSED`. It neither approves a row nor converts a
spectroscopic measure into an automatically approved physical velocity.

### Milestone 2D.1 remains blocked on

B. **immutable Gaia query/response authority:** retain the exact ADQL/query text,
   Gaia release and table identities, response bytes or a canonical extracted
   response, acquisition timestamp, hashes and query-result manifest for both
   Hipparcos-2 crossmatch tables and the required `gaia_source` fields;
C. **row-by-row scientific eligibility and minimal subset:** approve physical-component
   identity, astrometric solution, positive-parallax/systematics, applicable covariance,
   explicit `UNKNOWN_NOT_PROVIDED` astrometry-RV cross-covariance disposition,
   component-specific spectroscopic-RV propagation-proxy/systemic suitability,
   variability/multiplicity, quality and the minimal intended ProfileV1 technical route;
D. **Polaris source/component/RV authority:** approve an exact component-scoped
   fallback, provisionally direct ESA Hipparcos 1997 astrometry plus one separately
   approved primary systemic-RV authority, without flattening the authorities; and
E. **derived-artifact rights interpretation:** reconcile the open/free-with-credit and
   CC BY-NC 3.0 IGO statements for the exact normalized/derived artifact before public
   Git tracking or deployment.

### Milestone 2E owns later

- exact acquisition/query tooling and ignored raw-response storage;
- manifest and checksum generation;
- source-specific parser, crossmatch loader, normalization, covariance reconstruction,
  and fail-closed validation;
- deterministic subset selection and canonical runtime-artifact generation; and
- byte-identical rebuild, schema, provenance, licence-notice, and deployment guards.

2E may implement only after 2D.1 records an approved source strategy and row policy.
It does not resolve missing scientific authority by parser behavior.

Postimplementation production/reference residuals, numerical error-budget population,
and tolerance approval remain separate. Cultural review still owns named membership,
Arabic/Najdi claims, segments, and learner routes.

## Resource status

| Resource | Status | Consequence |
|---|---|---|
| Existing ESA Hipparcos 1997 and I/311 dossiers/local documentation | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Sufficient for their release semantics and stop rules; the direct ESA archive/licence route remains distinct from CDS I/239, and no new PDF is needed. |
| Gaia DR3 release, data model, crossmatch, DOI/rights, and credit pages | `OFFICIAL_WEB_SUFFICIENT` | Sufficient to select Gaia DR3 as the preferred next candidate and define the query/review contract. They do not resolve the exact derived-artifact rights interpretation. |
| Bounded 19-HIP Gaia DR3 screen | `OFFICIAL_WEB_SUFFICIENT` for preliminary field-presence screening only | The official TAP screen found 8/19 matches and five finite-RV candidates, but no exact ADQL/query text, response/canonical extraction, acquisition timestamp, hashes or query-result manifest was retained. It is not reproducible 2D authority evidence and approves no row. |
| TCB-to-TDB compatible-quantity mapping | `ALREADY_AVAILABLE_AND_SUFFICIENT` | IAU B3, IAU B2, Gaia, Klioner, IAU C1, Lindegren/Dravins, and pinned SOFA evidence support the approved analytic contract. Row-specific RV proxy suitability remains gate C. |
| Astronomy/data row approval | `HUMAN_REVIEW_REQUIRED` | Required for component, covariance, parallax, RV, multiplicity/variability, and quality dispositions. |
| Polaris field-specific fallback | `HUMAN_REVIEW_REQUIRED` | Direct ESA Hipparcos astrometry plus a primary systemic-RV authority is the smallest candidate shape; exact physical scope, value authority, crosswalk and rights remain open. |
| PCRV/XHIP | `REQUIRED_LATER` as supporting evidence only | Do not adopt either compilation wholesale or flatten it into Gaia/Hipparcos authority. |
| Another book/manual/PDF | `NOT_NEEDED` | Existing local material and official web documentation are sufficient for this decision. |

## USER ACTION REQUIRED

None now. No large catalogue download, new PDF or manual is needed. Local scientific
evaluation may continue with raw/query-derived material kept ignored and local. The
next 2D evidence task must retain the already-bounded Gaia query deterministically;
named astronomy/data review must approve rows, RV proxies and the Polaris fallback;
and a rights reviewer must reconcile the exact licence application before any derived
artifact is tracked or deployed. Commercial reuse remains unapproved.

## Authoritative sources used

- ESA/DPAC, [Gaia DR3 version 1.1 dataset and rights record](https://esdcdoi.esac.esa.int/doi/html/data/astronomy/gaia/DR3.html), DOI `10.5270/esa-qa4lep3`.
- ESA/DPAC, [Gaia DR3 documentation release 1.3](https://gea.esac.esa.int/archive/documentation/GDR3/) and [`gaiadr3.gaia_source` data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html).
- ESA/DPAC, [Gaia DR3 astrometric reference systems and TCB time coordinate](https://gea.esac.esa.int/archive/documentation/GDR3/Data_processing/chap_cu3ast/sec_cu3ast_intro/ssec_cu3ast_intro_refsystems.html).
- ESA/DPAC, [Gaia Archive](https://gea.esac.esa.int/archive/), [Hipparcos-2 crossmatch documentation](https://gea.esac.esa.int/archive/documentation/GDR3/Catalogue_consolidation/chap_crossmatch/sec_crossmatch_externalCat/ssec_crossmatch_hipparcos.html), and [credit/citation instructions](https://gea.esac.esa.int/archive/documentation/GDR3/Miscellaneous/sec_credit_and_citation_instructions/).
- ESA, [Gaia DR4 release status](https://www.cosmos.esa.int/web/gaia/data-release-4); expected content is not a released authority.
- ESA, [1997 Hipparcos catalogue and current access/licence page](https://www.cosmos.esa.int/web/hipparcos/catalogues) and ESA SP-1200 Volume 1 in the registered local evidence library.
- CDS, [original Hipparcos I/239 record](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/I/239?format=html&tex=true), [I/311 official catalogue record](https://cdsarc.cds.unistra.fr/viz-bin/cat/I/311), and [VizieR rules of use](https://cds.unistra.fr/vizier-org/licences_vizier.html).
- CDS, official ReadMes for [PCRV III/252](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/III/252?format=html&tex=true) and [XHIP V/137D](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/V/137D?format=html&tex=true).
- IAU, [2006 Resolution B3: Re-definition of TDB](https://www.iau.org/static/resolutions/IAU2006_Resol3.pdf), [2012 Resolution B2: re-definition of the astronomical unit](https://www.iau.org/static/resolutions/IAU2012_English.pdf), and [2000 Resolution C1: spectroscopic barycentric radial-velocity measure](https://www.iau.org/static/resolutions/IAU2000_French.pdf).
- Klioner (2008), [relativistic scaling of astronomical quantities](https://doi.org/10.1051/0004-6361:20077786), Klioner et al. (2010), [compatible-quantity nomenclature](https://doi.org/10.1051/0004-6361/200913090), and Lindegren and Dravins (2003), [the fundamental definition of radial velocity](https://doi.org/10.1051/0004-6361:20030181).
- Torres (2023), [*The spectroscopic orbit of Polaris and its pulsation properties*](https://doi.org/10.1093/mnras/stad2735), as a not-yet-approved primary systemic-RV candidate.
