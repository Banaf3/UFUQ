# Astronomy validation checklist

- [ ] Input/output frames and catalogue epoch are explicit.
- [ ] Observation instant and every time scale are explicit.
- [ ] Observer latitude/longitude sign, datum, and height are explicit.
- [ ] Every value has a unit and angle/azimuth convention.
- [ ] Proper motion and all included/omitted space-motion effects are documented.
- [ ] RA proper motion states whether it is `mu_alpha` or `mu_alpha_star`; no cosine
  conversion is implicit or applied twice.
- [ ] Refraction, horizon, and visibility policies are explicit.
- [ ] IERS source/version/hash and offline/network/extrapolation policy are recorded.
- [ ] Supported date/location ranges and singular cases are declared.
- [ ] Oracle Python, Astropy, PyERFA, and IERS-data versions are pinned.
- [ ] Oracle fixtures use a neutral versioned JSON contract.
- [ ] Oracle has no production-package dependency or mechanically shared algorithm.
- [ ] Cases cover wrap, time boundaries, horizon, zenith, epoch, motion, and endpoints.
- [ ] A high-declination case exposes omitted/double `cos(delta)` behavior when a
  Hipparcos RA proper-motion component is used.
- [ ] Comparison uses robust angular/circular metrics.
- [ ] Error components and total disagreement are reported per case.
- [ ] The tolerance is measured/approved, not invented.
- [ ] Missing local sources cause a stop, not a reconstructed fact.
