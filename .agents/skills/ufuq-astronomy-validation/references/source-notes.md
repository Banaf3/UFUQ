# Source notes

Start with `docs/references/syntheses/astronomy-model-synthesis.md`. Exact study
locations and limitations are in:

- `docs/references/studies/iau-sofa-2023-10-11.md`;
- `docs/references/studies/iers-conventions-2010.md`;
- `docs/references/studies/hipparcos-esa-1997-field-semantics.study.md`;
- `docs/references/studies/hipparcos-i311-readme.md`;
- `docs/references/studies/hipparcos-i311-validation.md`;
- `docs/references/studies/fundamental-astronomy-6e.md`; and
- `docs/references/studies/explanatory-supplement-3e.md`.

- `SOFA-2023-10-11` — first implementation authority for supported IAU algorithms.
  Cite the exact routine/manual section selected; a release pin alone does not define a
  UFUQ pipeline.
- `IERS-TN36-2010` — official 2010 reference-system and Earth-orientation baseline.
  Record corrections/working material separately under `IERS-UPDATES`.
- `ESA-HIP-1997-V1` — original-catalogue authority for J1991.25(TT), the standard
  astrometric parameters, and H12 `mu_alpha_star`. It strongly informs—but does not
  prove—the later I/311 `pmRA` mapping.
- `HIP-I311-README` — authority for I/311 epoch/frame/units/field and correction
  semantics. The data file is not self-describing.
- `VAN-LEEUWEN-2007-VALIDATION` — use the article's methods/results for new-reduction
  error characteristics, not for byte layout.
- `ASTROPY-DOCS-PIN`, `PYERFA-PIN`, and `ASTROPY-IERS-DATA-PIN` — currently unresolved
  required source pins. No oracle result is reference evidence until these are closed.
- `EXSUP-3E` — explanatory support only. The local candidate has no usable text layer
  and cannot support page/chapter citations.
- `FUND-ASTRO-6E` — explanatory support; it cannot override SOFA, IERS, catalogue
  metadata, or measured independent results.
- For I/311 propagation, preserve raw `pmRA` and stop until its star-component versus
  coordinate-angle semantics are confirmed. The current classification is
  `STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED`.
- `UFUQ-ASTRO-SPEC`, `UFUQ-ADR-003`, and `UFUQ-ADR-007` — project conventions and
  validation requirements, not external scientific authorities.

If local sources are absent, consult their official records in
`docs/references/UFUQ_SOURCE_REGISTER.md`, then stop any fact that needs unavailable
content. Never fill a missing value from memory.
