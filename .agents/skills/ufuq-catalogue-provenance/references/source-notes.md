# Source notes

Start with `docs/references/syntheses/catalogue-provenance-synthesis.md`. Exact evidence
locations are in the Hipparcos, JSON Schema, FAIR, PROV, and scientific-computing
dossiers under `docs/references/studies/`.

Use source IDs and limits from `docs/references/UFUQ_SOURCE_REGISTER.md`.

- `HIP-I311-README` — byte-level authority for I/311 fields, units, epoch/frame
  statements, record counts, solution types, and the 2008 correction history. It does
  not approve a UFUQ subset, access route, or redistribution.
- `ESA-HIP-1997-V1` — original-1997 catalogue authority for the H-field model,
  J1991.25(TT), and H12 `mu_alpha_star`; use it as a semantic cross-check, not as proof
  that I/311 `pmRA` is identical.
- `VAN-LEEUWEN-2007-VALIDATION` — quality/error context for the new reduction; it does
  not replace the catalogue `ReadMe`.
- `JSON-SCHEMA-CORE-2020-12` and `JSON-SCHEMA-VALIDATION-2020-12` — schema dialect and
  validation vocabulary. The local ISO 20022 paper is not either specification.
- `FAIR-2016` — workflow guidance only. Do not claim formal FAIR compliance.
- `PROV-SEM-2013` — optional formal-semantics background. Simple provenance fields do
  not require PROV reasoning.
- `UFUQ-DATA` and `UFUQ-ADR-004` — project ownership, manifest, deterministic-build,
  licence, curation, and release rules.

The current I/311 RA-motion conclusion is
`STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED`. Preserve the raw field, require an
explicit normalized semantic name, and do not apply or remove `cos(delta)` before the
spike resolves the mapping.

If official source metadata or local raw bytes are absent, stop the affected mapping or
checksum claim. Never reconstruct a catalogue row from memory or a cultural source.
