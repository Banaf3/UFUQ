# Security and privacy specification

## Scope and trust boundaries

The browser, network, local retry storage, and all client-supplied identifiers/results are untrusted. The API is the policy enforcement point; MySQL is private to it. Catalogue assets are public only if AST-001 permits redistribution. Administrator access increases confidentiality risk but does not grant permission to edit learning evidence.

Security uses OWASP ASVS 5.0.0 Level 1 as a minimum checklist and a risk-based set of
higher-assurance controls for privileged access, research export, recovery, privacy
maintenance, and sensitive learner data (**CLARIFIED**). SEC-003 approves the profile
and exception process. Legal/institutional conclusions are not made here; SEC-001 is a
**MANUAL DOMAIN DECISION**.

## Principal threats and controls

| Threat | Required controls |
|---|---|
| IDOR/wrong-role access to sessions or progress | Derive user from server session; query by ownership; central learner/admin authorization; negative route tests; aggregate admin defaults |
| Forged correctness, target, mastery, or policy | Server issues and validates scenario; recomputes target/score/BKT; accepts typed raw evidence only; immutable version checks |
| Duplicate/reordered attempts | Key bound to canonical endpoint/contract/request fingerprint; original result stored atomically; different-payload reuse conflicts; immutable scenario with expected mastery revision; row locks and bounded database-profile retry |
| SQL injection/mass assignment | Parameterized queries, allowlisted DTO schemas, reject unknown/oversized fields, least-privilege DB identity |
| Stored/reflected XSS through names/labels/logs | Contextual output escaping, no unsafe HTML, CSP, curated content validation, safe structured log viewer |
| CSRF/session theft/fixation | Same-origin HTTPS, server session in `__Host-` Secure HttpOnly SameSite cookie, CSRF protection for state change, session rotation, no URL tokens |
| Password attack/account enumeration | Argon2id candidate at OWASP baseline (19 MiB, 2 iterations, parallelism 1), long passphrases, generic responses, rate limits, audited recovery; confirm deployment capacity |
| Public admin creation/privilege escalation | No public admin role selection; controlled enrollment, explicit role checks, audit; MFA policy SEC-002 |
| Sensitive logging/export | DEV-014 allowlisted structured events, redaction, separate aggregate/log/export capabilities, purpose-bound pseudonymized export, access/audit controls |
| Malicious/offline local queue | Treat contents as untrusted on replay, bound size, validate age/version/ownership, no credentials or answer key, clear on sign-out per approved policy |
| Dependency/configuration compromise | Lockfile and review, automated vulnerability/secret checks, validated environment schema, patched runtime, minimal production image, no debug errors |
| Database loss/backup exposure | Encrypted transport/storage/backups, separate roles, tested restore, controlled retention/deletion, no production copy for development |

## Authentication and session policy

- Production uses a same-origin opaque server-side session persisted in MySQL in the
  initial topology and a cookie with `Secure`, `HttpOnly`, `SameSite`, `Path=/`, no
  `Domain`, and the `__Host-` prefix; never browser local storage for credentials/tokens.
- Rotate the session identifier on authentication and privilege change. Revoke on logout and credential/security events.
- Define idle/absolute lifetime, concurrent-session behavior, recovery, admin MFA, bootstrap, and breach response under SEC-002.
- Password hashes use a memory-hard library with versioned parameters and rehash-on-login policy. Passwords, hashes, recovery tokens, cookies, and CSRF secrets never enter logs or analytics.
- Rate-limit login, recovery, scenario issuance, submission, and export by appropriate user/IP signals without creating a privacy-heavy fingerprinting system.

## Authorization and API handling

Default deny. Every route declares whether it is intentionally public; otherwise it
declares authentication, required capability, ownership/scope, input schema, maximum
sizes, response schema, and audit behavior. Aggregate analytics, learner-level access,
operational logs, research export, enrollment, and privacy maintenance are distinct
capabilities. Administrators see only the minimum fields authorized by policy. Error
responses are stable and do not reveal account existence, SQL details, answer keys,
stack traces, or other learners.

The development fixture-identity adapter is excluded from production artifacts and
cannot be enabled by a runtime request or missing configuration. Production startup
fails if it is bundled/configured, and an artifact/E2E test proves the bypass is absent.

Use explicit CORS only if deployment later becomes cross-origin; the preferred same-origin topology does not allow wildcard credentials. Use TLS, CSP, frame protection, MIME sniffing protection, referrer policy, and Express production-hardening guidance. Avoid framework defaults that expose implementation details.

## Transaction and evidence integrity

The immutable scenario, request fingerprint, attempt, typed model decision (including
no-op), scaffold decision, mastery revision when applicable, consumed state, and stored
idempotency response form one atomic unit as specified in ADR-006. Historical attempts
are immutable application evidence; corrections are append-only annotations or
versioned recalculations, never silent updates. Store who/what/when/version/reason for
privileged exports or privacy actions.

Client time is telemetry only. The server records receipt/commit time; the approved scenario instant is part of the issued scenario. A database constraint and domain validation both enforce probability and sequence invariants.

## Local retry privacy

Local storage holds only the one unresolved submission per affected learner/KC: minimum
raw evidence, scenario/version identifiers, timestamp, contract version, request
fingerprint inputs, and idempotency key. It excludes password/session values, server
answer/target, mastery, unrelated profile data, and detailed analytics. The UI makes
pending/failed state visible and blocks further progression for that KC. Size/age are
bounded; successful items are removed after acknowledgement. Sign-out/shared-device
clearing is SEC-001. Persistent multi-opportunity offline tutoring is out of scope.

Offline retry is delivery resilience, not offline authentication or local-authoritative tutoring.

## Personal and research data

Potential personal data includes account identifiers/contact details, display name, role, mastery, answers, timing, assistance, session/location choices, IP/security events, and free-text feedback. Exact minimization, lawful basis, retention, data-subject rights, hosting, minors, and institutional research governance remain SEC-001/EDU-001–005.

Required design principles:

- collect only fields tied to an approved operational or research purpose; DEV-011 proposes no required legal name;
- separate operational privacy notice/terms from voluntary research consent;
- do not make tutoring access conditional on optional research use unless institutionally approved;
- export a random study ID, not email/name/database user ID; protect the linkage separately and delete it on schedule;
- use aggregate administrator views by default and suppress unsafe small groups if the protocol requires it;
- define retention per data class: account, learning evidence, security log, backup, research extract, consent record;
- support access/correction/withdrawal/deletion or approved anonymization through a controlled workflow; DEV-012 separates it from analytics administration;
- never reuse production learner data in development, screenshots, logs, or demos.

Malaysia's Personal Data Protection Act and 2024 amendment/resources are research inputs, not a legal determination. Institutional ethics approval and supervisor direction govern the human study.

## Logging and monitoring

Under DEV-014, allowlist event type, opaque actor/study ID as justified, request
correlation ID, server timestamp, outcome/reason code, policy versions, and performance
measures. Routine `SystemLog` entries have no unrestricted description field. Do not log
password/hash/token/cookie/CSRF secret/database URL, request bodies, raw free text,
exact answers/vectors unless an explicitly protected research dataset requires them, or
high-precision location beyond purpose.

Escape log display, restrict access, set retention, monitor repeated auth/authorization failures, idempotency conflicts, queue rejection, transaction rollback/deadlock exhaustion, catalogue/version mismatch, and export/privacy operations. Alerts must not embed sensitive payloads.

## Deployment and operations

- HTTPS-only reverse proxy; API and static web same origin; private MySQL with encrypted connection where supported.
- Separate migration and runtime accounts; least privilege; no root database credentials in application configuration.
- Secrets supplied by an approved secret manager/environment, validated at startup, excluded from repository and client bundle.
- Production error handling, dependency patch process, health/readiness checks, encrypted backups, restore drill, and documented incident response.
- Research and catalogue artifacts use separate access controls according to consent/licence.

Hosting region, backup/restore objectives, monitoring service, and retention are DEP-001/SEC-001.

## Release evidence

Complete the approved SEC-003 ASVS 5.0.0 profile, automated and manual
authz/CSRF/XSS/injection/session tests, dependency/vulnerability exception and
secret/restricted-file scans, log review, pending-submission inspection, backup restore,
privacy data-flow/retention review, and approved research protocol. No claim of legal
compliance or full WCAG conformance is made merely from automated tools.
