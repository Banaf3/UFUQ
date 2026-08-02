# Mandatory-rule traceability

Detailed evidence is in
`docs/references/syntheses/catalogue-provenance-synthesis.md` and its linked dossiers.

| Skill rule | Evidence basis | Classification |
|---|---|---|
| Workflow 1: source/release, URL/method/time, licence, fields, filters, records | I/311 `Notice` and `File Summary`; FAIR R1.1-R1.2, Box 2 p. 4; `DATA_STRATEGY.md` | Source plus project decision |
| Workflow 2: preserve the complete acquisition-to-artifact chain | Wilson et al. 2017 pp. 2-6; PROV §3.2.4.6 p. 8; ADR-004 | Source plus project decision |
| Workflow 3: hash before parsing; immutable ignored raw bytes | Wilson et al. 2017 p. 2 and pp. 14-15; `DATA_STRATEGY.md` | Source plus project decision |
| Workflow 4: derive units/nulls/quality/frame/epoch/IDs from official metadata | I/311 byte descriptions, Notes, Global Note G1; ESA 1997 §§1.2 and 2.1 only as original-catalogue semantic support | Source |
| Workflow 5: separate numerical catalogue and cultural curation | Wilson et al. 2014 Box 1 practice 4 p. 2; `DATA_STRATEGY.md` | Source plus project decision |
| Workflow 6: validate catalogue/content/artifact trust boundaries | JSON Core §§4.3, 8-12; Validation §§3-7; ADR-004 | Source plus project decision |
| Workflow 7: explicit UTF-8/LF/order/Unicode/numeric canonicalization and repeat build | JSON Core §§4.2.1-4.2.2 shows schema does not define bytes; `DATA_STRATEGY.md`; Wilson et al. 2014 pp. 2-3 | Project decision supported by source |
| Workflow 8: record versions, hashes, counts, licence, omissions, and drift | FAIR F1-F3/R1.1-R1.2, Box 2 p. 4; I/311 correction notice; ADR-004 | Source plus project decision |
| Stop: missing source/licence/hash/field semantics/frame/epoch/quality/canonicalization | I/311 metadata limits; FAIR R1.1-R1.2; `SOURCE_GAPS.md` DATA-SRC-001/002 | Source plus unresolved decision |
| Rule: normalize I/311 `pmRA` only as the starred-alpha component and map directly to Astropy `pm_ra_cosdec` after unit conversion | I/311 Appendix G Table G.3, printed p. 407; `studies/hipparcos-i311-readme.md` | I/311-specific source plus project field-name decision |
| Stop: source drift, unresolved curation ID, manually copied value | I/311 correction history; `DATA_STRATEGY.md` | Source plus project decision |
| Prohibition: no manually copied coordinates or cultural data in numerical rows | Wilson et al. 2014 single-authority rule; `AGENTS.md`; `DATA_STRATEGY.md` | Source plus project decision |
| Prohibition: no automatic redistribution, FAIR compliance, or formal PROV requirement | FAIR “Principles precede implementation” p. 5; PROV Abstract/Status pp. 1-2; licence gap | Source plus unresolved decision |

Validator selection, `format`, composed-object closure, and JavaScript number behavior
remain experiment/project-decision requirements; the skill must not imply they are
already resolved.
