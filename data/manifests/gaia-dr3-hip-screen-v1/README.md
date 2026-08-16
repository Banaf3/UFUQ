# Gaia DR3 19-HIP query evidence

This directory contains the tracked query and provenance boundary for Milestone
2D.1B. It does not contain Gaia catalogue rows and it approves no source, component,
radial velocity, or ProfileV1 star.

The exact official ESA Gaia TAP responses are retained locally under the ignored
directory named by `acquisition-manifest.v1.json`. Public Git tracking and deployment
of raw or normalized Gaia rows remain rights-review gated. A checkout without those
local bytes can inspect and replay the query definition, but cannot claim to possess or
verify the original response bytes.

The acquisition used anonymous synchronous TAP `POST` requests with these form
parameters in order:

```text
REQUEST=doQuery
LANG=ADQL
FORMAT=csv
MAXREC=1000
QUERY@<tracked .adql file>
```

Each query targets the fixed `gaiadr3` schema rather than a moving `latest` alias.
Replaying a query does not recreate the recorded authority unless every received byte
has the recorded SHA-256. A differing response creates a new evidence version and raw
directory; it must not overwrite this acquisition.

The raw Gaia-native TCB values are not normalized by this evidence step. Any future
normalization must cite the separately approved
`GAIA_DR3_TCB_TO_TDB_COMPATIBLE_V1` adapter and preserve native and normalized states.

