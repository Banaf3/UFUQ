# Catalogue provenance review checklist

- [ ] Source/table/release, canonical URL, retrieval method, timestamp, and licence are
  recorded.
- [ ] Raw bytes are ignored, immutable, and checked against the approved SHA-256 before
  parsing.
- [ ] Expected and actual record counts are compared.
- [ ] Every selected field has source pointer, units, null/quality semantics, and
  frame/epoch meaning.
- [ ] `pmRA` normalization distinguishes `mu_alpha` from `mu_alpha_star` and preserves
  the raw source value until the I/311-specific mapping is confirmed.
- [ ] No coordinate is manually copied and no cultural content is embedded in numerical
  rows.
- [ ] Parsing and normalization failures are explicit.
- [ ] Runtime schemas reject invalid, unknown, unresolved, or mixed-semantics data.
- [ ] Curation references stable catalogue IDs and passes referential integrity.
- [ ] Serialization explicitly fixes UTF-8, LF, ordering, Unicode, and numeric format.
- [ ] Repeated builds produce identical bytes and checksums.
- [ ] Proper-motion mapping tests include high declination and omitted/double-cosine
  failure cases when the suite becomes active.
- [ ] Input/tool/schema/output versions and hashes appear in the provenance record.
- [ ] Redistribution is allowed explicitly or generated/raw bytes remain untracked.
- [ ] FAIR is described as guidance, and formal PROV semantics are not made mandatory.
