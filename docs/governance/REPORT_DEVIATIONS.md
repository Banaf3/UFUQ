# Proposed deviations from the approved report

Every item is **PROPOSED DEVIATION** and must be explicitly approved, rejected, or
revised before the affected implementation. A rejection returns behavior to the report
baseline unless a new approved alternative is recorded. Report anchors below are
neutral locations for the already-paraphrased requirement; they do not reproduce
restricted text. Pure clarifications are not listed here. The required approver for every
row is the student and supervisor, plus the named domain/institutional owner where the
change affects that domain.

| ID | Proposed change | Why proposed / impact if rejected | Report anchor and affected IDs | Required co-approver | Status |
|---|---|---|---|---|---|
| DEV-001 | Implement the central science-to-learning vertical slice before full authentication and dashboards, using a non-production fixture learner. | Retires the main research and integration risks first. If rejected, follow the report sprint order and accept later integration-risk discovery. | §3.2; P1; FR-01/03/04/06/07 | Architecture reviewer | Pending |
| DEV-002 | Store astronomical values and BKT probabilities as MySQL `DOUBLE`, not `FLOAT`. | Reduces avoidable rounding error and improves replay/audit stability. If rejected, validation must accommodate lower precision. | §3.6 tables 3-9/3-11; FR-06/09; NFR-02/06; ADR-006 | Astronomy + learning reviewers | Pending |
| DEV-003 | Replace a generic `VARCHAR` learner answer with typed JSON/columns plus schema and version. | Preserves vectors, target IDs, bearings, and units. If rejected, every task needs ambiguous text encoding/parsing. | §3.6 table 3-11; FR-04; ADR-006 | Architecture reviewer | Pending |
| DEV-004 | Replace a hint Boolean with `GUIDED`, `FADING`, and `INDEPENDENT`, and store the server-issued cue snapshot. | Makes fading and evidence reconstructable. If rejected, retain the Boolean and weaker auditability. | §2.5.4 and §3.6 tables 3-9/3-11; FR-07/11; ADR-005/006 | Learning expert | Pending |
| DEV-005 | Define one BKT-updating attempt as one submitted task response; store raw clicks separately as optional telemetry. | Prevents exploratory clicks from repeatedly changing mastery. If rejected, each spatial click may become an observation. | §3.6 table 3-11; FR-04/06; ADR-006 | Learning expert | Pending |
| DEV-006 | Do not treat a hinted correct response as equivalent independent evidence; choose an approved assisted-evidence policy. | Prevents assistance from inflating independent mastery. If rejected, all responses update BKT identically. | §2.5.4–2.5.5; FR-06/11; BKT-001; ADR-005 | Learning/research-method expert | Pending; BKT-001 |
| DEV-007 | Replace “high slip rate triggers hints” with observed response/mastery history and policy state as the trigger. | Slip is a fixed parameter, not a per-attempt observation. If rejected, technically inaccurate terminology remains. | §3.4.5; FR-07; ADR-005 | Learning expert | Pending |
| DEV-008 | Replace “an incorrect response always lowers stored mastery” with the correct posterior/transition invariant. | Avoids a mathematically false test. If rejected, the documented standard BKT equations and test invariant conflict. | §2.5.4 and §3.8.2; ER-02; ADR-005 | Learning expert | Pending |
| DEV-009 | Keep Arabic naming and asterism relationships in versioned curated data, not ordinary operational database tables. | Preserves provenance and avoids CMS scope. If rejected, add operational content tables/migrations and their review workflow. | §3.2/3.3.2; FR-15; ADR-004 | Cultural expert | Pending |
| DEV-010 | Permit Phase 1 to use a fixture learner and server-generated scenario before production authentication. | Enables DEV-001. If rejected, the complete account workflow precedes the research slice. | §3.2 sprint order and §3.4.2; FR-05; P1/P4 | Security + architecture reviewers | Pending |
| DEV-011 | Make legal/full name optional and prefer a display name or pseudonym. | Minimizes personal data. If rejected, collect the report data-dictionary name field. | §3.6 table 3-7; FR-05; SEC-001 | Institution/privacy owner | Pending |
| DEV-012 | Add an audited privacy-maintenance deletion/anonymization path while keeping analytics administrators read-only. | Supports data-subject handling without general evidence editing. If rejected, use an approved manual institutional process. | §3.4.2 UC-105 and §3.6; FR-13; SEC-001 | Institution/privacy owner | Pending |
| DEV-013 | Keep correct time/location geometry and the resulting seasonal sky in MVP, but treat physical light-pollution, weather, sky-brightness, extinction, and season-specific environmental realism as optional unless separately approved. | Prevents an unvalidated atmosphere/weather subsystem. If rejected, add its data, model, performance, and validation burden. | §3.2 Sprint 2 and §3.3.3 FR-1/FR-2; FR-01/02; AST-004; SCOPE-001 | Astronomy/education expert | Pending; SCOPE-001 |
| DEV-014 | Replace the unrestricted free-text system-log payload with structured, allowlisted, size-bounded, redacted event fields; retain protected diagnostic detail only where an approved purpose requires it. | Prevents credentials, answers, personal data, or internals entering routine logs. If rejected, the report data-dictionary field requires compensating redaction/access controls. | §3.6 table 3-12; FR-13; NFR-04; ADR-006 | Security/privacy reviewer | Pending |

Selecting a non-Hipparcos catalogue is not automatically a deviation: the report names
catalogue candidates rather than fixing one. AST-001 still requires approval. Proper
motion, epoch handling, and other astrometric effects are scientifically motivated
clarifications, not silently attributed report requirements; AST-003 must implement each
or approve its omission with a quantified bound. Removing independent astronomical
validation would change the report evaluation baseline and requires a new deviation.

The report's administrator analytics use case is read-only. No deviation is needed to
forbid ordinary administrator mutation of attempts or mastery; DEV-012 concerns a
separate, audited privacy-maintenance authority.
