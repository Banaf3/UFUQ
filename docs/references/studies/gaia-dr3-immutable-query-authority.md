# Gaia DR3 immutable query/response authority

## Scope and outcome

This record closes only Milestone 2D.1B: immutable official-query evidence for the
bounded 19-HIP technical screen. It does not approve a Gaia row, physical component,
parallax, radial-velocity proxy, Polaris fallback, cultural membership, runtime
artifact, or deployment right.

Decision: `GAIA_QUERY_AUTHORITY_CLOSED`.

The response bytes are retained locally under ignored `data/raw/`; the tracked query
set and machine-readable manifest are under
[`data/manifests/gaia-dr3-hip-screen-v1/`](../../../data/manifests/gaia-dr3-hip-screen-v1/).
The rights-review gate still prohibits tracking the raw/query-derived rows.

## Official release, service, and tables

| Item | Pinned identity | Classification |
|---|---|---|
| Release | ESA/DPAC Gaia DR3 version 1.1, DOI `10.5270/esa-qa4lep3`; documentation release 1.3 | `SOURCE_SUPPORTED_FACT` |
| Service | Anonymous official ESA Gaia Archive TAP 1.1 base `https://gea.esac.esa.int/tap-server/tap`; synchronous endpoint `/sync` | `SOURCE_SUPPORTED_FACT` from the acquired VOSI capability response |
| Source table | `gaiadr3.gaia_source` | `SOURCE_SUPPORTED_FACT` |
| Identity bridge | `gaiadr3.hipparcos2_best_neighbour` | `SOURCE_SUPPORTED_FACT`; one official best-neighbour candidate is not physical-component approval |
| Complete match evidence | `gaiadr3.hipparcos2_neighbourhood` | `SOURCE_SUPPORTED_FACT`; retains every returned good neighbour and score/flag evidence |
| Query set | `GAIA_DR3_HIP_SCREEN_V1`, version 1, exact 19 numeric HIP IDs, no quality cut, deterministic ordering, `MAXREC=1000` | `PROJECT_DECISION` |

ESA's DR3 documentation defines the best-neighbour table as the highest-scoring good
neighbour selected by the release crossmatch and the neighbourhood table as all good
neighbours. It warns that the positional crossmatch balances completeness and
correctness. UFUQ therefore treats these tables as release-scoped candidate identity
evidence, never automatic component or row approval.

## Exact query and response boundary

The exact ADQL is the byte-identified tracked source, not a query copied from this
prose:

| Query | Tracked path | Bytes | SHA-256 |
|---|---|---:|---|
| Best neighbour plus bounded review fields from `gaia_source` | [`best-neighbour-source.v1.adql`](../../../data/manifests/gaia-dr3-hip-screen-v1/best-neighbour-source.v1.adql) | 2,282 | `a64512610f17fdb9145b11f49963b395ec72a0abb03f9a9377e38d90f5a19b30` |
| All returned neighbourhood candidates | [`neighbourhood.v1.adql`](../../../data/manifests/gaia-dr3-hip-screen-v1/neighbourhood.v1.adql) | 442 | `642757af0a185d5d228c413e46824a88137edc19952c2be6e9808348a9ba3bc3` |
| TAP schema snapshot for the three tables | [`tap-schema.v1.adql`](../../../data/manifests/gaia-dr3-hip-screen-v1/tap-schema.v1.adql) | 269 | `c4e10daade967ca3f7221c1861131327bef62bc70300489d42714b0600f1f403` |

All three queries used anonymous synchronous HTTP `POST` with `REQUEST=doQuery`,
`LANG=ADQL`, `FORMAT=csv`, and `MAXREC=1000`. The output column lists are fixed in the
manifest and come from the exact ADQL/TAP response headers. No arbitrary threshold,
astrometric-quality filter, source substitution, or normalization was applied.

The acquisition began at `2026-08-16T02:09:20.7638790Z` and completed at
`2026-08-16T02:09:31.0409551Z` using curl `8.21.0` on Windows x64. The service returned
HTTP 200 for availability, capabilities, schema, best-neighbour/source, and
neighbourhood requests; its acquired availability record says it was accepting
queries. No TAP request failure or service warning was returned. Crossmatch `xm_flag`
values remain source data and are not normalized into service warnings.

## Ignored raw evidence

Local evidence directory:

```text
data/raw/gaia-dr3/2d1b-gaia-dr3-hip-screen-v1-20260816T020920Z/
```

| Raw response | Bytes | SHA-256 |
|---|---:|---|
| `best-neighbour-source.csv` | 6,900 | `251bd3e82ad176dc887934d6d698c8b450c1bcbc6024a567bdfbe8ce85db3f4f` |
| `neighbourhood.csv` | 526 | `633b39c30d7f60b6f76b29995ed9b2ef82de34a43e22f9afb3df15cbd63975be` |
| `tap-schema.csv` | 17,420 | `003d4c5ba91bcf49992d6d99f76de70d83e91ffbc152e186be4d3ae95b2f8e7a` |
| `tap-availability.xml` | 362 | `b8122f451f17658e127b2220cc3d11c949cf7d72a560e9cb8890d5307d31323d` |
| `tap-capabilities.xml` | 32,360 | `5e9c08e69cbb84f474c12fa11dd78d7da5dd146dcc64637d05ba02103a5b4b42` |

The manifest separately identifies and hashes every acquired HTTP-header file. The
schema snapshot has 162 rows: 152 `gaia_source` columns and five columns for each
crossmatch table. Gaia `source_id` values are preserved in the raw CSV as exact decimal
lexemes; the structural check found zero non-decimal spellings. Future JSON consumers
must treat them as strings.

No canonical scientific-row extraction was produced. The exact raw CSV bytes remain
the authority response, so 2D.1B did not change a scientific value. Later 2E
normalization must retain these native Gaia TCB values and cite
`GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1`; native and normalized records remain distinct.

## Structural results only

The immutable evidence reproduces the earlier screen with no discrepancy:

| Structural result | Count or identity |
|---|---|
| Technical candidates | 19 |
| Best-neighbour/source rows | 8 |
| Neighbourhood rows / distinct HIP IDs | 8 / 8 |
| Matched HIP IDs | `3179`, `6686`, `59774`, `65378`, `77055`, `79822`, `82080`, `85822` |
| Unmatched HIP IDs | `746`, `4427`, `8886`, `11767`, `53910`, `54061`, `58001`, `62956`, `67301`, `72607`, `75097` |
| Both RV and RV-error fields present | 5 |
| RV or RV-error field missing | 3 |
| Positive raw-parallax field values | 8 |
| Five-parameter / six-parameter solutions | 2 / 6 |
| Returned HIP IDs with multiple neighbourhood candidates | 0 |
| `HIP 11767` best/neighbourhood rows | 0 / 0 |

These statements mean only `MATCH_PRESENT`, `MATCH_ABSENT`, `FIELD_PRESENT`,
`FIELD_MISSING`, and `QUERY_EVIDENCE_VERIFIED`. They must not be promoted to
`ROW_SCIENTIFICALLY_APPROVED`, `RV_SYSTEMIC_APPROVED`, `PARALLAX_APPROVED`,
`COMPONENT_APPROVED`, or `PROFILE_STAR_APPROVED`. Gates C and D own those decisions.

## Reproducibility and versioning policy

- The hash-bound local raw response, not the live service, is the acquired authority.
- The queries use the fixed `gaiadr3` schema and exact table names, never a `latest`
  alias.
- A later re-query is the same evidence only when all relevant response hashes match.
- A changed response creates a new query-evidence ID, timestamped raw directory,
  manifest, and comparison; it never overwrites this evidence version.
- A public checkout can inspect query text, metadata, counts, and hashes but cannot
  claim byte verification without an authorized copy of the ignored raw files.
- `npm run data:verify` checks tracked query hashes and, when the local response set is
  present, verifies every raw byte length/hash while continuing to prohibit tracked or
  unignored raw data.

## Rights and lifecycle boundary

Current policy remains unchanged:

- `LOCAL_ANALYSIS_ALLOWED = YES`;
- `ATTRIBUTION_REQUIRED = YES`;
- raw/query-derived Gaia rows remain `IGNORED_LOCAL_ONLY`;
- public row tracking and generated-derived deployment remain
  `RIGHTS_INTERPRETATION_REQUIRED`.

This acquisition closes evidence gate B without solving gate E. The tracked files
contain query text, non-row metadata, structural counts, and hashes only. No production
parser or runtime JSON was created.

Remaining Milestone 2D.1 gates are:

1. C — row-by-row scientific eligibility and a minimal technical subset;
2. D — Polaris source/component/systemic-RV authority; and
3. E — derived-artifact rights interpretation.

## Resource audit

| Resource | Status | Consequence |
|---|---|---|
| Official Gaia DR3 release 1.3 data model and Hipparcos-2 crossmatch documentation | `OFFICIAL_WEB_SUFFICIENT` | Establishes table/column/crossmatch semantics. |
| Official ESA Gaia TAP service | `OFFICIAL_WEB_SUFFICIENT` | Supplied the bounded immutable response bytes and service metadata. |
| Existing 2D.1/2D.1A repository dossiers | `ALREADY_AVAILABLE_AND_SUFFICIENT` | Establish the candidate list, release boundary, native TCB state, adapter, and no-row-approval rule. |
| New PDF, manual, bulk catalogue download, or local-reference file | `NOT_NEEDED` | The bounded official response and existing evidence are sufficient for gate B. |

`USER_ACTION_REQUIRED`: none.

## Official sources

- ESA/DPAC, [Gaia DR3 documentation release 1.3](https://gea.esac.esa.int/archive/documentation/GDR3/) and [`gaiadr3.gaia_source` data model](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_main_source_catalogue/ssec_dm_gaia_source.html).
- ESA/DPAC, [`hipparcos2_best_neighbour`](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_cross-matches/ssec_dm_hipparcos2_best_neighbour.html), [`hipparcos2_neighbourhood`](https://gea.esac.esa.int/archive/documentation/GDR3/Gaia_archive/chap_datamodel/sec_dm_cross-matches/ssec_dm_hipparcos2_neighbourhood.html), and [Hipparcos-2 crossmatch method](https://gea.esac.esa.int/archive/documentation/GDR3/Catalogue_consolidation/chap_crossmatch/sec_crossmatch_externalCat/ssec_crossmatch_hipparcos.html).
- ESA, [Gaia Archive](https://gea.esac.esa.int/archive/) and the acquired TAP/VOSI responses identified above.
- ESA/DPAC, [Gaia DR3 version 1.1 dataset record](https://esdcdoi.esac.esa.int/doi/html/data/astronomy/gaia/DR3.html), DOI `10.5270/esa-qa4lep3`.

