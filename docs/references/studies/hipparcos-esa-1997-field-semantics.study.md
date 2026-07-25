# ESA Hipparcos 1997 field semantics

## Bibliographic identity

- Canonical source ID: `ESA-HIP-1997-V1`.
- Title: *The Hipparcos and Tycho Catalogues*.
- Volume: Volume 1, *Introduction and Guide to the Data*.
- Corporate author/publisher: European Space Agency; ESA Publications Division.
- Scientific coordination: M. A. C. Perryman and the Hipparcos Science Team; Volume 1
  composition is credited to M. A. C. Perryman.
- Edition/version and year: ESA Special Publication SP-1200, June 1997.
- Identifiers: ISSN 0379-6566; ISBN 92-9092-399-7 for Volumes 1-17.
- Local file:
  `local-reference/catalogues/hipparcos-esa-1997/documentation/volume-1-catalogue-introduction.pdf`.
- Extent and access: 586 PDF pages with a searchable text layer. A malformed Type 3
  font warning affects extraction reliability for some glyphs; the cited mathematical
  symbols were checked against rendered pages.
- Verification status: `VERIFIED_FROM_CONTENT` for bibliographic identity and
  continuity of Volume 1; `PROVENANCE_UNVERIFIED` for the acquisition chain. The PDF
  container reports 2007 pdfsam/iText packaging, while the visible publication is the
  1997 ESA volume.

## UFUQ relevance and study scope

- Phases affected: Phase 1 astronomy/data technical spike; Phase 2 only if a Hipparcos
  source is approved.
- Project decisions affected: AST-001 catalogue fields, AST-003 epoch/proper-motion
  policy, ADR-004 provenance and normalization, and the independent-oracle cases in
  ADR-007.
- Exact material studied:
  - title, publication, volume-title, and contents pages, PDF pp. 3-11;
  - §1.2.1, printed pp. 19-21;
  - §1.2.3, printed pp. 23-24;
  - §§1.2.5-1.2.8, printed pp. 25-34, including Eqs. (1.2.2)-(1.2.4) and
    (1.2.11)-(1.2.21);
  - §§1.5.4-1.5.5, printed pp. 94-98, including Eqs. (1.5.21) and (1.5.25)-(1.5.32);
  - §2.1, printed pp. 109-111; and
  - Table 2.1.1(a), printed p. 136.
- Intentionally not studied: photometric calibration, individual star rows, catalogue
  statistics, mission construction, double-star annex detail, and the remaining
  volumes. They are not needed to settle this focused field-semantics question.

## Standard astrometric parameters

Section 1.2.1, printed pp. 19-20, describes a uniform rectilinear barycentric
space-motion model at reference epoch `T0`. Its six quantities are right ascension
`alpha`, declination `delta`, annual parallax `pi`, two proper-motion components, and
radial velocity. The five catalogue astrometric parameters omit radial velocity.
Section 1.2.8, printed pp. 29-34, represents the direction and tangential motion with a
normal triad and distinguishes barycentric coordinate direction from topocentric
coordinate direction. These catalogue quantities are not apparent or observed
horizontal coordinates.

The source warns that non-standard binary/multiple-star behavior may not fit the
five-parameter model (§1.2.1, printed pp. 20-21). Section 2.1, printed p. 109, also
limits extrapolation of acceleration-solution terms and recommends the documented
five parameters, with radial velocity where perspective acceleration matters, as the
more robust general extrapolation basis for the original catalogue.

## Reference epoch and time unit

- Common catalogue epoch: `T0 = J1991.25(TT)` (§1.2.1, printed p. 20).
- Exact epoch relation: `J1991.25(TT) = JD 2448349.0625(TT)` (§1.2.6,
  Eq. (1.2.3), printed p. 27).
- Proper-motion time unit: the Julian year of exactly 365.25 days, or 31,557,600
  seconds (§§1.2.4 and 1.2.6, printed pp. 25-26).
- Frame: catalogue positions and proper motions are specified in ICRS (§§1.2.1-1.2.2,
  printed pp. 19-23).

This exact 1997 epoch statement is strong semantic support, but it does not silently
assign `TT` to the later I/311 ReadMe's shorter `Ep=1991.25` label.

## Proper-motion conventions

### Right ascension

Section 1.2.5, printed p. 25, distinguishes:

- `mu_alpha = d(alpha)/dt`, a coordinate-angle rate; and
- `mu_alpha_star = (d(alpha)/dt) cos(delta)`, the great-circle component tabulated by
  the original catalogue.

The asterisk denotes that the cosine factor is already included. The unit is
milliarcseconds per Julian year (§1.2.1, printed p. 20). Section 1.5.4,
Eq. (1.5.21), printed p. 94, explicitly applies `sec(delta)` when a simplified
coordinate-angle update is formed from `mu_alpha_star`; applying another cosine would
therefore be the wrong direction of conversion.

The original field guide confirms that H12 is `mu_alpha_star = mu_alpha cos(delta)` in
mas per Julian year (§2.1, printed p. 110; Table 2.1.1(a), printed p. 136).

### Declination

`mu_delta = d(delta)/dt` is the declination component, also in milliarcseconds per
Julian year (§§1.2.1 and 1.2.5, printed pp. 19-25). The original field guide assigns it
to H13 (§2.1, printed p. 110; Table 2.1.1(a), printed p. 136).

### Propagation limitation

The source's simplified coordinate update (§1.5.4, Eq. (1.5.21), printed p. 94) is
explicitly unsuitable for general-purpose software, especially near the poles or over
long intervals. The rigorous treatment in §1.5.5, printed pp. 94-98, propagates
direction, parallax, proper-motion vector, and radial component under the standard
uniform-space-motion model. This dossier does not select either formula as UFUQ's
production implementation.

## Parallax terminology and units

Section 1.2.1, printed pp. 19-20, calls `pi` annual parallax and uses it to relate
coordinate distance to the astronomical unit. Section 2.1, printed p. 110, labels H11
trigonometric parallax in milliarcseconds and states that estimates are supplied even
when statistically insignificant or negative. A negative estimate is therefore not a
parser error or missing value.

## Relationship to Hipparcos catalogue sources

### Original ESA catalogue

This volume is the official guide for the 1997 Hipparcos and Tycho catalogues. It
defines the original Hipparcos H8-H18 fields, model, frame, epoch, units, and
`mu_alpha_star` convention.

### CDS I/311 new reduction

CDS I/311 is van Leeuwen's later reduction, not the 1997 catalogue. Its local ReadMe:

- identifies I/311 as the new reduction;
- points to I/239 for the 1997 catalogue;
- labels bytes 52-59 `pmRA`, “Proper motion in Right Ascension,” in mas/year; and
- does not explicitly write `mu_alpha_star` or the cosine factor.

The van Leeuwen validation article studies new-versus-original error behavior but does
not define the I/311 `pmRA` component. Therefore ESA's 1997 definition supplies strong
terminological and model support, but it is not by itself I/311-specific field
documentation. In particular, no claim is made that every I/311 field, null, solution,
or covariance semantic is identical to I/239.

## pmRA conclusion

**Classification: `STRONG_SUPPORT_BUT_SPIKE_CONFIRMATION_REQUIRED`.**

Confidence is high that the original 1997 H12 field stores
`mu_alpha_star = mu_alpha cos(delta)` in mas per Julian year at J1991.25(TT). Confidence
is not high enough to mark the later I/311 field `pmRA` confirmed because the currently
available I/311-specific ReadMe and validation paper do not spell out the cosine
convention. `CONFIRMED_FOR_I311` would require an I/311-specific authoritative field
definition or a pinned independent experiment that is then reviewed and recorded.

## UFUQ implementation implications

- `SOURCE_REQUIRED`: preserve the raw I/311 `pmRA` value and its source-field identity;
  never silently apply or remove `cos(delta)`.
- `PROJECT_DECISION_REQUIRED`: the normalized schema must distinguish coordinate-angle
  `mu_alpha` from great-circle `mu_alpha_star`. If the spike confirms the latter for
  I/311, use an explicit name such as `properMotionRaStarMasPerYear`; do not use an
  ambiguous `properMotionRa`.
- `EXPERIMENT_REQUIRED`: map the candidate field to the independently pinned Astropy
  interface explicitly and record whether that interface accepts the star component or
  coordinate-angle derivative.
- `EXPERIMENT_REQUIRED`: include a high-declination case because cosine omission or
  double application becomes materially more visible there.
- `SOURCE_REQUIRED`: retain J1991.25 as source metadata; use the exact time-scale
  instant only after the I/311 mapping is supported.
- `INFORMATIONAL_ONLY`: ESA's rigorous model explains why a scalar RA update is not a
  sufficient general propagation implementation.

## Required Phase 1 spike tests

These are test requirements, not implemented tests:

1. Preserve and expose the raw `pmRA` input before normalization.
2. Test an explicitly named `mu_alpha_star` normalization and reject ambiguous or
   double-converted values.
3. Use a high-declination case selected through the approved manifest, without
   manually copying a catalogue coordinate into source code.
4. Propagate from catalogue epoch J1991.25 with the epoch and time-scale assumptions
   recorded in the fixture.
5. Include positive and negative RA-component cases.
6. Compare against independently configured, version-pinned Astropy/PyERFA fixtures;
   the oracle must not import a production UFUQ package.
7. Add a paired failure case that would expose accidental second application of
   `cos(delta)` and a paired case that would expose its omission.
8. Measure disagreement before selecting any tolerance.

## Unresolved questions

- Which I/311-specific authoritative source explicitly defines `pmRA` as
  `mu_alpha_star`, if any?
- Does the approved Astropy representation for the pinned version accept
  `mu_alpha_star` directly, and under what field/unit name?
- May J1991.25(TT) from the 1997 guide be applied to the I/311 reduction, or must the
  new-reduction documentation state that separately?
- Which I/311 solution families and covariance/quality fields are approved?
- Which I/311 licence, local-processing, subset, field, and generated-artifact policy
  will UFUQ approve for source-derived work?
- What date range, radial-velocity policy, uncertainty treatment, and measured
  comparison tolerance will the spike support?

## Limitations

- This source does not define the CDS I/311 fixed-width file or corrections.
- It does not select a UFUQ catalogue, Astropy, SOFA, a propagation implementation, or
  a numerical tolerance.
- It supplies no approved UFUQ star subset or catalogue coordinate.
- It does not establish that all original and new-reduction field semantics are
  identical.
- Its local acquisition provenance remains unverified, and its bytes must not be
  redistributed.

## Traceability

| Knowledge item | Source location | UFUQ implication | Status |
|---|---|---|---|
| Five astrometric parameters omit radial velocity | §1.2.1, printed pp. 19-20 | Keep source parameters and model assumptions explicit | `SOURCE_REQUIRED` |
| Catalogue frame is ICRS | §§1.2.1-1.2.2, printed pp. 19-23 | Record frame with every normalized record/fixture | `SOURCE_REQUIRED` |
| Original catalogue epoch is J1991.25(TT) | §1.2.6, Eq. (1.2.3), printed p. 27 | Test propagation from an explicit source epoch | `SOURCE_REQUIRED` |
| Julian year is exactly 365.25 days | §§1.2.4 and 1.2.6, printed pp. 25-26 | Do not leave “per year” undefined | `SOURCE_REQUIRED` |
| Original RA motion is `mu_alpha_star` | §1.2.5, printed p. 25; §2.1, printed p. 110; Table 2.1.1(a), printed p. 136 | Name normalized semantics and prevent cosine duplication | `SOURCE_REQUIRED` |
| Simplified RA update reverses the included cosine with secant | §1.5.4, Eq. (1.5.21), printed p. 94 | Add double/omitted-cosine spike cases | `EXPERIMENT_REQUIRED` |
| General propagation needs the rigorous model or another approved equivalent | §§1.5.4-1.5.5, printed pp. 94-98 | Do not adopt the scalar formula as production merely for convenience | `PROJECT_DECISION_REQUIRED` |
| Original H11 parallax may be negative | §2.1, printed p. 110 | Do not reject negative estimates as malformed | `SOURCE_REQUIRED` |
| I/311 `pmRA` remains indirectly supported | I/311 `ReadMe`, `hip2.dat` bytes 52-59; van Leeuwen validation §§1-5 | Require I/311-specific evidence or a reviewed spike | `EXPERIMENT_REQUIRED` |
