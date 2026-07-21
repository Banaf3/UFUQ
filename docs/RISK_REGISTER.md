# Risk register

Likelihood and impact are qualitative until implementation measurements exist. Owners must update triggers, status, and residual risk in each phase ExecPlan.

| ID | Risk | L | I | Mitigation and early indicator | Owner / phase |
|---|---|---:|---:|---|---|
| R-01 | Mixed coordinate frames or time conventions produce plausible but wrong sky positions. | M | Critical | One explicit pipeline, versioned policy, singular fixtures, independent Astropy/USNO oracle. Any systematic angular bias stops release. | Astronomy / P0-P2 |
| R-02 | Cultural mapping or Arabic terminology is invented or disputed. | M | High | Expert-approved curated records with citations and review status; build rejects unapproved records. | Domain expert / P0-P2 |
| R-03 | Catalogue licensing or redistribution is incompatible with a public repository/deployment. | M | High | Approve source/licence first; preserve query/manifest/checksum; avoid committing raw or generated rows until cleared. | Supervisor / P0 |
| R-04 | BKT mastery is inflated by hinted attempts or sparse provisional parameters. | H | High | Separate assistance state, approve evidence policy, sensitivity analysis, require independent recall evidence. | Learning / P0-P3 |
| R-05 | Duplicate, stale, reordered, cold-start, or concurrent submissions corrupt mastery. | M | Critical | Canonical request fingerprint, immutable scenario expected revision, pre-provisioned mastery rows, fixed lock order, monotonic mastery revision, transaction, real-MySQL concurrency/fault tests. | API/data / P1-P3 |
| R-06 | Client tampering changes correctness or mastery. | M | High | Server generates/validates scenarios and computes score/BKT; reject unversioned/out-of-window evidence. | API/security / P1-P4 |
| R-07 | Three.js/React integration misses the performance target. | M | High | Small catalogue, buffer geometry/instancing, demand-based React updates, frozen-device benchmark early. | Web 3D / P1-P5 |
| R-08 | Near-horizon/refraction and near-zenith azimuth create unstable assessments. | M | High | Domain policy, exclude/flag singular fixtures, vector angular comparison. | Astronomy/assessment / P0-P2 |
| R-09 | Delayed local retry silently loses, double-counts, or applies stale learning evidence. | M | High | One pending item per KC, blocked progression, single-flight retry, expected mastery revision, server reconciliation/reissue, privacy and replay tests. | Web/API / P3 |
| R-10 | Authentication/authorization leaks learner progress, operational logs, exports, or privileged maintenance. | M | Critical | Durable same-origin session, ownership/capability checks, aggregate defaults, SEC-003 ASVS profile, no public admin role selection, fixture-bypass artifact test. | Security / P4-P5 |
| R-11 | Personal/research data is collected without settled authority, purpose or retention. | M | Critical | Separate operational/research consent, minimum data, approved codebook/export, pseudonymized extracts, no human study before EDU-001–005/SEC-001. | Institution / P0-P6 |
| R-12 | Scope expands into a general planetarium or content-management platform. | H | High | MVP boundary, risk-first phases, change control, reject optional work until MVP gates pass. | Owner / all |
| R-13 | Reference implementation shares the same code, data-policy mistake, or reviewer blind spot as production. | M | High | Separate generator/reviewer, prohibited code sharing, pinned oracle settings, policy differential cases, independent domain cross-check. | Testing / P1-P2 |
| R-14 | Visual-only assessment excludes users or invalidates an accessibility claim. | M | High | Resolve ACC-001, keyboard/focus/contrast/reduced-motion gates, qualify claims. | UX/research / P4-P6 |
| R-15 | Cloud/service loss or configuration drift destroys audit evidence. | L | High | Version manifests, migrations, environment schema, encrypted backups, restore drill, deployment evidence bundle. | Operations / P5 |
| R-16 | Restricted report or licensed catalogue data is accidentally committed. | L | Critical | Git ignore, pre-commit/CI path and secret scan, artifact allowlist, final privacy audit. | All / all |
| R-17 | Recruitment, ethics timing, attrition, or small sample prevents the planned educational inference. | H | High | EDU-001–005, power/rationale and latest dates, early synthetic instrument/analysis dry-run, recruitment trigger, prespecified bounded/no-claim outcome. | Supervisor/research / P0-P6 |
| R-18 | Mandatory scope and external approvals exceed one developer's remaining FYP capacity. | H | Critical | SCOPE-002 calendar/capacity, phase timeboxes, stop/go gates, protected cut line, explicit deferral order, no silent reduction of report claims. | Student/supervisor / all |
