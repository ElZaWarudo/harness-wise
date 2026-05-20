# Impact And Verification

Load when a review unit changes contracts, schemas, APIs, bindings, shared helpers, auth/tenant behavior, payloads, fixtures, or other surfaces that can drift.

## Impact Scan Gate

Run after implementation and before code review whenever the diff changes:

- API contract, endpoint, binding, generated client, shared helper, schema, payload.
- Auth, permissions, roles, scopes, tenant isolation, ownership behavior.
- Test fixture contracts or seeded setup.

Under `autonomy:guarded` or `autonomy:high`, delegate read-only discovery when the scan spans multiple modules, generated clients, fixtures, or broad tests. The lead records final gate result.

Required output:

- Changed contract.
- Consumer scan patterns.
- Consumers found.
- Required consumer tests.
- Contract-drift test scan.
- Run/skipped results.

Example:

```text
Changed contract:
- POST /api/v1/wallet now requires active tenant context.
Consumer scan patterns:
- CreateWallet
- ApiWallet
- /api/v1/wallet
Consumers found:
- web-application/backend/test/mocha/api-tests/tests-api-wallet.ts
Required consumer tests:
- Wallet, DID, VC, and Anchor Registry API tests.
Contract-drift test scan:
- rg "deepStrictEqual|toEqual|permissions|role.*bundle|tenant.*permission" web-application/backend/test
Run/skipped results:
- <commands/results or local blocker with CI coverage expectation>
```

Do not mark `review-passed` until this gate is complete for every contract change.

## Verification Ladder

- Run the narrowest useful targeted command for diagnosis.
- When tests depend on global hooks, shared fixtures, seeded state, or suite setup, run the natural affected sub-suite before trusting the result.
- Before release handoff or PR update for a CI fix, run the repo-specific command equivalent to the affected CI job, derived from workflow config, package scripts, Makefiles, task runners, or docs.
- If the CI-equivalent command cannot run locally, record the concrete blocker and pass it as an explicit verification gap to `krt-release-marshal`.

## Surface Verification Evidence

Record verification by changed surface instead of only by command:

```text
Changed surfaces:
- Permissions/roles: verified by <test/inspection> or skipped because <reason>
- Tenant isolation/ownership: verified by <test/inspection> or skipped because <reason>
- API/generated contract: verified by <test/inspection> or skipped because <reason>
- Persistence/schema: verified by <test/inspection> or skipped because <reason>
- Config/deployment: verified by <test/inspection> or skipped because <reason>
- Docs/orchestration: verified by <review/inspection> or skipped because <reason>
- Production compatibility: verified by <evidence> or intentionally relaxed because <rationale>
```

Omit unchanged surfaces. If a changed surface has no evidence, keep the review unit out of `review-passed` unless the gap is explicitly acceptable for the risk and CI is expected to cover it.
