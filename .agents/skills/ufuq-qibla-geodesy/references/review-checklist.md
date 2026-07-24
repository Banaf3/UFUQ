# Qibla geodesy review checklist

- [ ] Observer latitude/longitude, coordinate source, datum/frame, precision, and
  applicable height are explicit.
- [ ] Destination latitude/longitude, source, datum/frame, precision, version/date,
  uncertainty, and approval are explicit.
- [ ] The selected spherical or ellipsoidal model is named and versioned.
- [ ] Coordinate order, east-positive longitude, units, and normalization are explicit.
- [ ] The inverse-geodesic forward azimuth is clockwise from geographic True North.
- [ ] True North, magnetic north, Polaris line-of-sight, and Qibla remain distinct.
- [ ] Coincident, polar, near-antipodal, antipodal, wrap, and invalid inputs have
  specified behavior.
- [ ] Independent cases record tool/version, exact inputs, and provenance.
- [ ] Comparison uses wrapped circular difference.
- [ ] Tolerance follows a measured error budget rather than convenience.
- [ ] Historical sources provide context only.
- [ ] An unapproved destination coordinate or datum stops production work.
