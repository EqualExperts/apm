# Acceptance scenarios

Capture source behaviour before edits, then run the same external contracts against the target. Use the existing wrapper's full verification lifecycle, recording actual commands and counts. Do not assume that replacing @QuarkusTest with @MicronautTest reproduces test resources, mocks or transaction handling.

| Scenario | Evidence required when applicable |
| --- | --- |
| Clean build and startup | Generated beans/routes work without stale classes; constructor injection, qualifiers, conditions and configuration precedence match expectations. |
| HTTP and JSON | Real requests on a random port cover success, missing route, invalid input, status, headers, error shape and representative DTOs. Exercise streams/multipart if present. |
| Security | Unauthenticated, forbidden and allowed paths; token validation, roles, tenant isolation and context propagation. No bypasses introduced for tests. |
| Data | Isolated database checks for queries, pagination, optimistic locking, commit and rollback. Verify reactive transaction context where used. |
| Reactive execution | Failure, cancellation, backpressure and blocking-work placement; a synchronous greeting endpoint is insufficient. |
| Lifecycle and integrations | Startup failure, resource cleanup, messaging acknowledgement/retry and graceful shutdown. Missing test infrastructure is blocked evidence, not a pass. |
| Runtime removal | Inspect source and resolved dependencies for Quarkus runtime/deployment artifacts and build plugins. Document intentionally retained standalone libraries. |
| Packaging | Start the actual JVM package and verify readiness and shutdown. If native deployment is required, build and exercise that binary separately. |

Record failures, skipped checks and unsupported extension mappings. Compare observable outputs rather than framework implementation details. Performance claims require comparable measurements under the same workload. Local checks do not establish production acceptance.
