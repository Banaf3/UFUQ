# ADR-006: Relational persistence and assessment transactions

- **Status:** Blocked pending SYS-001 and storage/log deviations
- **Classification:** CONFIRMED/CLARIFIED plus PROPOSED DEVIATIONS DEV-002–005/014
- **Date:** 2026-07-20

## Context

The report chooses MySQL and requires continuous mastery storage. An accepted response affects an immutable attempt, the learner/KC mastery, assistance decision, ordering, and retry result. Separate writes or client authority can lose/double transitions during failure or concurrency.

## Decision

Use MySQL/InnoDB under SYS-001. Provision all five active mastery rows atomically before
assessed scenario issuance. In one API transaction: authorize ownership; canonicalize
endpoint/contract/scenario/raw evidence and claim a per-user idempotency key with its
request fingerprint; on matching duplicate return the stored committed response and on
mismatch conflict; lock idempotency result, session, immutable scenario, then
learner/KC mastery in fixed order; validate expiry/consumption/versions and expected
mastery revision; score; persist attempt plus typed model/scaffold decision; update the
revision when eligible; consume scenario; store canonical response; commit. Retry the
entire transaction only for recognized bounded SYS-001 cases.

Enforce the approved normalized login, active learner/KC, session/order,
scenario-consumption, and user/idempotency constraints, foreign keys, finite/range
domain checks, bounded typed payloads, and immutable historical evidence. DEV-002
proposes `DOUBLE`; DEV-003 typed JSON/columns; DEV-004 explicit scaffold/server-issued
cue snapshot; DEV-005 one submitted task per attempt; DEV-014 structured logs.

## Consequences

- Accepted evidence and mastery never diverge, and offline retry is safe.
- The API must run transaction/concurrency tests against real MySQL, not SQLite.
- Long computations should be deterministic and bounded while locks are held; scenario target inputs are prepared/validated appropriately without weakening the authoritative transaction.
- Privacy deletion/anonymization requires a deliberate audited path, not cascading accidental evidence loss.

## Alternatives rejected

- Multiple autocommit writes or eventual consistency.
- Client-supplied attempt order, correctness, or mastery.
- An in-memory retry registry.
- MySQL `FLOAT` for probabilities/astronomical evidence (pending DEV-002).

## Validation

Fault injection before/after each write; concurrent cold start; rollback; matching
duplicates; same-key/different-content conflict; consumed/expired/stale revision;
deadlock/timeout handling; concurrent replay yielding one decision; and distinct
current-revision submissions yielding one serialized chain against the frozen MySQL
profile.
