# Mandatory-rule traceability

Detailed evidence is in
`docs/references/syntheses/qibla-geodesy-synthesis.md` and the Karney/King dossiers.

| Skill rule | Evidence basis | Classification |
|---|---|---|
| Workflow 1: observer coordinate/source/datum/precision | Karney §2 treats endpoints/ellipsoid as explicit inputs; AST-005 | Project decision |
| Workflow 2: destination coordinate/source/datum/version/approval and hard stop | `SOURCE_GAPS.md` AST-SRC-008; neither Karney nor King supplies authority | Unresolved stop condition |
| Workflow 3: name spherical or ellipsoidal runtime model | `docs/ASTRONOMY_SPEC.md` Qibla model; Karney §§1, 4 | Project decision plus source |
| Workflow 4: define order, units, sign, branch, forward azimuth, and normalization | Karney Fig. 1, §2; ADR-003 | Source plus project decision |
| Workflow 5: distinguish True North, magnetic north, Polaris, and Qibla | King 1993 Paper I/Papers IX-XIV; King 1999 §§2.1-2.4; astronomy spec | Source plus project decision |
| Workflow 6: define coincident/polar/near-antipodal/antipodal/invalid behavior | Karney §§4-5; AST-006 | Source plus project decision |
| Workflow 7: independent cases across ordinary and difficult geometry | Karney Tables 3-6 and §7; ADR-007 | Source plus experiment |
| Workflow 8: wrapped comparison and measured error budget | `docs/ASTRONOMY_SPEC.md` Angular comparison; Karney §7 limits | Project decision plus experiment |
| Workflow 9: report all unresolved authorities | `AGENTS.md`; AST-005/006 | Project decision |
| Stop: unapproved Kaaba coordinate/datum | `SOURCE_GAPS.md` AST-SRC-008 | Unresolved stop condition |
| Stop: missing model/convention/reference/tolerance | Karney conventions/difficult cases; AST-005/006 | Source, project decision, experiment |
| Prohibition: no coordinate from map/table or historical source | King 1999 §2.3 p. 54 and §§2.5, 2.8-2.9; King 1993 Papers IX-XIV | Source |
| Prohibition: Karney does not approve the destination | Entire Karney source scope | Source absence / stop condition |

No production Qibla result can be approved until the destination-coordinate stop
condition is closed.

