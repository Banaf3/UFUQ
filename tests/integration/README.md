# Integration-test boundary

The integration suite intentionally has no database or authentication case in Phase 0.
Its dedicated configuration discovers `tests/integration/**/*.test.ts`, fails if
invoked empty, and is omitted from Phase 0 CI. It becomes mandatory in Phase 4 with the
first API/persistence integration and must use real MySQL for transaction claims.
