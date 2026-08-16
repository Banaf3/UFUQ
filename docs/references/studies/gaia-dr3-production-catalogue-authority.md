# Gaia DR3 production-catalogue authority study

## Scope and evidence boundary

This study records release-level source facts and a bounded row-screening result used
by Milestone 2D.1. It does not copy catalogue values into Git, approve a
source/component match, select a quality threshold, or authorize a runtime artifact.
Official web material and the official Gaia TAP service were inspected on 2026-08-16;
the registered local ESA Hipparcos documentation was used read-only.

## Gaia DR3 release identity and availability

- `SOURCE_SUPPORTED_FACT`: ESA identifies Gaia DR3 as released on 2022-06-13 and its
  dataset record as version 1.1, last updated 2023-02-07, DOI
  `10.5270/esa-qa4lep3`. Documentation release 1.3 is the matching official guide.
- `SOURCE_SUPPORTED_FACT`: Gaia DR4 remains forthcoming on ESA's current release page;
  expected DR4 contents are not a released dataset that UFUQ can pin.
- `SOURCE_SUPPORTED_FACT`: the Gaia Archive supports release-scoped queries and the
  DR3 archive publishes Hipparcos-2 best-neighbour and neighbourhood crossmatch tables.
- `SOURCE_SUPPORTED_FACT`: a bounded read-only TAP screen of the 19 existing technical
  HIP candidates found eight Hipparcos-2 crossmatch rows. All eight have positive raw
  parallax, five have finite DR3 RV and RV uncertainty, and the neighbourhood table has
  one neighbour for each of the same eight HIP identifiers. The screen retained no
  exact ADQL/query text, release/table-bound response bytes or canonical extracted
  response, acquisition timestamp, hashes, or query-result manifest. Its counts are
  preliminary field-presence evidence, not reproducible 2D acquisition or activation
  authority.
- `AUTHORITY_OR_EVIDENCE_MISSING`: release documentation and an ephemeral TAP screen
  cannot approve physical-component identity, covariance handling, parallax
  systematics, RV suitability, quality, or a runtime row. A future acquisition must
  retain the exact ADQL/query text, Gaia release/table identities, response bytes or
  canonical extracted response, service identity, acquisition timestamp, hashes and
  query-result manifest.

## Astrometric semantics

The official DR3 data model and astrometric reference-system documentation establish:

- `ra` and `dec` are barycentric ICRS directions at `ref_epoch`;
- `ref_epoch` is expressed as a Julian year in TCB and DR3 uses `J2016.0`;
- Gaia catalogue astrometry is parametrized with TCB as the independent time
  coordinate;
- `pmra` is `mu_alpha_star = mu_alpha cos(dec)`, the tangent-plane component toward
  increasing right ascension, and `pmdec` is the component toward increasing
  declination;
- `ra_error` is `sigma_alpha_star`, not an unstarred coordinate-angle error, and
  `pmra_error` has the corresponding starred tangent-plane basis;
- parallax, formal errors, astrometric solution metadata, fit/observation diagnostics,
  and pairwise astrometric correlations are published in `gaiadr3.gaia_source`;
- a five-parameter solution's five formal errors and ten correlations define its
  five-dimensional astrometric covariance block; and
- a six-parameter solution also has pseudocolour, its uncertainty, and five additional
  pseudocolour correlations. It must not be represented as the five-parameter block or
  silently stripped without a reviewed disposition.

These facts do not themselves define UFUQ's TCB-to-TDB-compatible propagation adapter.
IAU 2006 Resolution B3 defines TDB as a fixed linear transformation of TCB, with the
defining factor `L_B`. The relativistic-scaling literature distinguishes TCB-compatible
from TDB-compatible quantities: converting only the epoch label is not a valid
conversion of a rate-parametrized catalogue state.

The required normalization contract is therefore fail-closed:

1. retain the native Gaia state and covariance as TCB-parametrized evidence;
2. convert the reference instant using the IAU B3 TCB-to-TDB transformation, not by
   renaming `J2016.0 TCB` to `J2016.0 TDB`;
3. apply a source-pinned analytic compatible-quantity mapping to every affected rate,
   uncertainty and covariance term before the TDB SOFA boundary; and
4. preserve the native and normalized states, transformation/version identity and
   reviewer disposition.

`SOURCE_SUPPORTED_FACT`: TDB is linearly related to TCB and Gaia's catalogue state is
TCB-parametrized. `PROJECT_DECISION`: UFUQ requires an explicit scale-aware adapter and
covariance Jacobian. `AUTHORITY_OR_EVIDENCE_MISSING`: the current evidence set has not
yet approved the complete stellar-parameter mapping, including the exact proper-motion,
parallax/distance and spectroscopic-RV dispositions expected by the selected SOFA
interface. Relabelling or applying an epoch-only conversion is prohibited. Milestone
2D must approve that mapping; Milestone 2E later implements and tests it.

Gaia's release documentation also records release-dependent parallax systematics and
known issues. A positive raw parallax plus its formal error is therefore not, by
itself, a complete uncertainty disposition. A future row review must preserve the raw
value and decide, with release-pinned authority, whether a zero-point/systematic
correction or explicit reviewed omission applies. This study selects no correction or
numeric quality cut.

## Radial velocity and joint uncertainty limit

`gaiadr3.gaia_source.radial_velocity` is a multi-transit Solar-system-barycentric
spectroscopic radial velocity, with a separate error and diagnostics, for a subset of
DR3 sources. ESA's release record reports radial velocities for about 33 million
sources, not the full astrometric catalogue. The main field may be a median or another
release-described combination depending on the recorded method.

The source-level facts do not establish that a populated mean is the systemic radial
velocity of a multiple or variable object, nor that it belongs to the intended physical
component. The data model does not publish astrometry-to-RV cross-covariance as part of
the five-/six-parameter astrometric covariance. ScientificProfileV1 does not require a
fictional complete astrometry-plus-RV covariance. UFUQ must preserve the applicable
Gaia astrometric covariance and the separate RV uncertainty, and record the absent
joint covariance as `UNKNOWN_NOT_PROVIDED` with an explicit reviewed
omission/correlation disposition. It must never encode that absence as zero or assume
independence silently. The missing cross-covariance does not by itself make a row
ineligible after that omission is approved; its numerical consequence remains an
unbounded error-budget and postimplementation-validation term.

The exact source-to-ScientificProfileV1 RV sign mapping remains a source-adapter review
item. A finite database value is not approval, and missing RV cannot become
`0 km/s`.

## Bright sources, components, and crossmatches

ESA describes Gaia DR3's approximate bright limit near `G = 3`; RV coverage is a
smaller subset. Those release facts justify a row-level stop rule for bright teaching
stars but do not prove that Polaris or any other candidate is present or absent.

The official Hipparcos-2 crossmatch supplies release-scoped candidate identity
evidence. A best neighbour, a close position, or a populated Gaia row does not prove
the intended physical component. The bounded audit must retain all mates/neighbours,
match metrics, source/component evidence, and ambiguity flags. Where the main row
indicates non-single-star or variability evidence, the audit must also retrieve and
review every applicable official DR3 NSS/variability record and the relevant RV
evidence. No NSS model or threshold is selected here.

Gaia `source_id` and `solution_id` are 64-bit identifiers. Serialized artifacts must
preserve their exact decimal spelling as opaque strings rather than JSON numbers.
They are release/source record keys, not stable UFUQ or cultural identifiers.

### Bounded 19-HIP screening result

The following table reports only field-presence and solution-class evidence from the
official DR3 TAP screen. It deliberately omits coordinates and measured values. A
match means only that the release crossmatch returned one candidate; it is not physical
identity or scientific approval.

| HIP | Official DR3 crossmatch screen | Required disposition |
|---|---|---|
| `746` | No match | Gaia-only row unavailable; record failure. |
| `3179` | Six-parameter astrometry; positive raw parallax; RV unavailable | Ineligible under the current V1 required-RV contract unless an exact supplement is approved. |
| `4427` | No match | Gaia-only row unavailable; record failure. |
| `6686` | Six-parameter astrometry; positive raw parallax; RV unavailable | Ineligible under the current V1 required-RV contract unless an exact supplement is approved. |
| `8886` | No match | Gaia-only row unavailable; record failure. |
| `11767` | No match in best-neighbour or neighbourhood table | Intended Polaris target requires a separately approved component-scoped fallback; no nearby Gaia source may substitute. |
| `53910` | No match | Gaia-only row unavailable; record failure. |
| `54061` | No match | Gaia-only row unavailable; record failure. |
| `58001` | No match | Gaia-only row unavailable; record failure. |
| `59774` | Six-parameter astrometry; positive raw parallax; finite RV/error; non-single-star evidence | Candidate only; retrieve applicable NSS/variability records and review physical/systemic meaning. |
| `62956` | No match | Gaia-only row unavailable; record failure. |
| `65378` | Six-parameter astrometry; positive raw parallax; RV unavailable | Ineligible without a supplement; component-qualified identity requires separate review. |
| `67301` | No match | Gaia-only row unavailable; record failure. |
| `72607` | No match | Gaia-only row unavailable; record failure. |
| `75097` | No match | Gaia-only row unavailable; record failure. |
| `77055` | Six-parameter astrometry; positive raw parallax; finite RV/error | Candidate only; six-parameter, component, quality and RV review required. |
| `79822` | Five-parameter astrometry; positive raw parallax; finite RV/error | Candidate only; component, systematics, quality and RV review required. |
| `82080` | Six-parameter astrometry; positive raw parallax; finite RV/error | Candidate only; six-parameter and RV-uncertainty/quality review required. |
| `85822` | Five-parameter astrometry; positive raw parallax; finite RV/error | Candidate only; component, systematics, quality and RV review required. |

The screen establishes a possible small raw-field-complete Gaia subset of five rows,
not five eligible or culturally approved stars. Eleven technical HIP identifiers have
no official DR3 Hipparcos-2 crossmatch row, and three of the eight matches lack RV. No
failure may be hidden by silently dropping a candidate from the review manifest.

### Polaris fallback boundary

The intended `HIP 11767` object is not represented by an official DR3 Hipparcos-2
crossmatch row. A bounded check of the original Hipparcos main row found position,
proper motion, positive parallax and formal errors, but no RV; its main-row component
fields do not by themselves resolve the known `Polaris Aa+Ab` spectroscopic system.
PCRV has a HIP-keyed compiled RV and XHIP identifies a component-A RV with a source
reference, but neither compilation by itself proves the systemic, component-scoped RV
needed for full space motion. XHIP also uses the I/311 astrometric reduction and cannot
be adopted wholesale without inheriting its epoch-scale blocker.

Torres (2023) is a peer-reviewed primary candidate for a Polaris-system spectroscopic
orbit and systemic velocity. It is not yet an approved field authority: 2D must review
the physical scope, velocity convention/epoch, uncertainty, identity crosswalk and
derived-value deployment terms. The smallest possible fallback is therefore
field-specific direct ESA Hipparcos 1997 astrometry plus one approved primary
systemic-RV authority; the exact pairing is still blocked and must not be flattened into
a synthetic single-catalogue identity.

## Hipparcos and CDS comparison boundary

- The direct ESA 1997 Hipparcos release and ESA legacy table
  `hipparcos1.hip_main` provide bright-star astrometry, explicit
  `J1991.25 (TT)`, proper motion, parallax, formal uncertainty/correlation fields, and
  multiplicity records, but no general RV field.
- ESA's current catalogue page applies CC BY-NC 3.0 IGO and `Credit: ESA` to the direct
  ESA catalogue distribution. This licence is not transferred to the CDS I/239 mirror
  without separate evidence.
- CDS I/311 remains the new-reduction spike source. Its I/311-applicable epoch/rate time
  scale, RV, row/component approval, and raw/derived redistribution rights are not
  established.
- PCRV III/252 and XHIP V/137D have relevant compiled RV/cross-reference metadata, but
  exact row/component suitability and redistribution/deployment authority were not
  established. They are not an approved blanket supplement.

## Rights boundary

Two official ESA statements must be retained without flattening either one:

- the DR3 credit page says Gaia data are open and free to use when ESA/Gaia/DPAC is
  credited and gives the required acknowledgement and release citations; and
- the version 1.1 DOI dataset record separately classifies data hosted in ESA Space
  Science Archives under CC BY-NC 3.0 IGO.

The first statement supports access and use with credit; it does not erase the
dataset-specific rights metadata. The second records CC BY-NC 3.0 IGO for the DOI
dataset distribution. This audit does not choose which statement controls UFUQ's exact
normalized/derived artifact by assumption. The resulting project classifications are:

- `LOCAL_ANALYSIS_ALLOWED = YES`;
- `ATTRIBUTION_REQUIRED = YES`;
- `GENERATED_DERIVED_OUTPUT_DEPLOYMENT = RIGHTS_INTERPRETATION_REQUIRED`;
- `PUBLIC_GIT_TRACKING = RIGHTS_INTERPRETATION_REQUIRED`;
- `NONCOMMERCIAL_FYP_USE = CANDIDATE_ALLOWED_PENDING_EXACT_LICENSE_APPLICATION`; and
- `COMMERCIAL_REUSE = NOT_APPROVED`.

UFUQ must not describe Gaia generally as "noncommercial only" or claim public
redistribution/deployment permission before the exact derived-artifact terms are
reconciled. Raw and query-derived catalogue material remains local and ignored until
that approval. This rights scope is separate from scientific row approval and does not
prevent continued local scientific evaluation.

Public availability through CDS is not a redistribution grant. VizieR's official usage
rules require source citation and catalogue-specific rights review; they do not close
I/311, PCRV, or XHIP derived-row deployment permission.

## Authoritative sources

- ESA/DPAC, [Gaia DR3 version 1.1 dataset and rights record](https://esdcdoi.esac.esa.int/doi/html/data/astronomy/gaia/DR3.html), DOI `10.5270/esa-qa4lep3`.
- ESA/DPAC, [Gaia DR3 documentation release 1.3](https://gea.esac.esa.int/archive/documentation/GDR3/), [`gaiadr3.gaia_source`](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html), and [reference systems/time scales](https://gea.esac.esa.int/archive/documentation/GDR3/Data_processing/chap_cu3ast/sec_cu3ast_intro/ssec_cu3ast_intro_refsystems.html).
- ESA/DPAC, [Gaia Archive](https://gea.esac.esa.int/archive/), [Hipparcos-2 crossmatch](https://gea.esac.esa.int/archive/documentation/GDR3/Catalogue_consolidation/chap_crossmatch/sec_crossmatch_externalCat/ssec_crossmatch_hipparcos.html), and [credit/citation instructions](https://gea.esac.esa.int/archive/documentation/GDR3/Miscellaneous/sec_credit_and_citation_instructions/).
- ESA, [Gaia DR4 status](https://www.cosmos.esa.int/web/gaia/data-release-4).
- ESA, [1997 Hipparcos catalogue/access/licence page](https://www.cosmos.esa.int/web/hipparcos/catalogues) and ESA SP-1200 Volume 1 in the registered local evidence library.
- CDS, [I/311 catalogue record](https://cdsarc.cds.unistra.fr/viz-bin/cat/I/311), [VizieR rules](https://cds.unistra.fr/vizier-org/licences_vizier.html), [PCRV III/252](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/III/252?format=html&tex=true), and [XHIP V/137D](https://cdsarc.cds.unistra.fr/viz-bin/ReadMe/V/137D?format=html&tex=true).
- IAU, [2006 Resolution B3: Re-definition of TDB](https://www.iau.org/static/resolutions/IAU2006_Resol3.pdf), and Klioner (2008), [relativistic scaling of astronomical quantities](https://doi.org/10.1051/0004-6361:20077786).
- Torres (2023), [*The spectroscopic orbit of Polaris and its pulsation properties*](https://doi.org/10.1093/mnras/stad2735), as a not-yet-approved primary fallback candidate.

## Study conclusion

`PROJECT_DECISION`: the release evidence is sufficient to make Gaia DR3 version 1.1
the preferred single-source-first candidate. It is insufficient to approve an active
catalogue or row. The bounded screen demonstrates a possible small Gaia-only technical
subset but excludes Polaris and leaves every match review-gated. The saved acquisition,
scale-aware TCB-to-TDB parameter/covariance mapping, per-row component/systematics/
quality approval, Polaris astrometry-plus-systemic-RV fallback, and its rights remain
Milestone 2D.1 gates.
