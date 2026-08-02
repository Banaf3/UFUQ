# Source notes

Start with `docs/references/syntheses/catalogue-provenance-synthesis.md`. Exact evidence
locations are in the Hipparcos, JSON Schema, FAIR, PROV, and scientific-computing
dossiers under `docs/references/studies/`.

Use source IDs and limits from `docs/references/UFUQ_SOURCE_REGISTER.md`.

- `HIP-I311-README` — byte-level authority for I/311 fields, units, epoch/frame
  statements, record counts, solution types, and the 2008 correction history. It does
  not approve a UFUQ subset, access route, or redistribution.
- `HIP-I311-APPENDIX-G` — field-symbol authority for the new reduction. Table G.3,
  printed p. 407, identifies source `pmRA` as `mu_alpha_star`; Tables G.5–G.6 retain
  the starred-alpha convention for acceleration terms.
- `VIZIER-RULES` — permits scientific-context use with source citation and requests
  VizieR acknowledgement, but does not grant UFUQ raw/derived I/311 redistribution.
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

The I/311 RA-motion conclusion is `CONFIRMED_FOR_I311`. Preserve the raw field,
normalize it only as `properMotionRaCosDecMilliarcsecondsPerYear`, and do not apply or
remove another `cos(delta)` when mapping to Astropy `pm_ra_cosdec`.

If official source metadata or local raw bytes are absent, stop the affected mapping or
checksum claim. Never reconstruct a catalogue row from memory or a cultural source.
