# Acceptance scenarios

| Area | Evidence where applicable |
| --- | --- |
| HTTP | Compare real HTTP status, headers and semantic JSON for success, missing routes, invalid input and service failure. Preserve method/path matching and content negotiation. |
| Data | Exercise large integers/decimals, timestamps, omitted/null fields and enum/validation errors. |
| Security | Unauthenticated, forbidden and allowed requests retain policy. |
| Persistence | Test commit/rollback, concurrency and queries on isolated data. |
| Execution | Verify bounded concurrency, cancellation/deadlines and request-context isolation. |
| Messaging | Preserve acknowledgements, ordering, retries and idempotency; callbacks do not replace distributed delivery. |
| Operations | Await binding before readiness; drain and close resources. Verify packaged startup and telemetry separately. |
| Removal | Inspect source/build/runtime dependencies for obsolete Quarkus facilities. |

Run the target's build/tests and source baseline, inspecting counts and skipped suites. Record synthetic fixture coverage separately from complete application acceptance. Do not run production or destructive data operations merely to validate this skill.
