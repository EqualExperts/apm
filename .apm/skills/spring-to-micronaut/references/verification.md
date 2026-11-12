# Acceptance scenarios

Run the existing wrapper's full build on both baselines. For Maven use `./mvnw verify` (Windows: `mvnw.cmd verify`); for Gradle use `./gradlew build`. Inspect test counts, skipped suites and dependency resolution for accidental mixed runtimes.

| Scenario | Required evidence where applicable |
| --- | --- |
| DI/configuration | Clean build starts the context, resolves constructor injection and uses the expected configuration; verify qualifiers and conditions. |
| HTTP | Start a server on a random port and exercise real HTTP: success, missing route, malformed input, status, headers and payload. Compare with Spring. |
| Serialization | Verify representative DTOs and custom serializers under the selected engine, including required processing/introspection. |
| Security | Allowed, forbidden and unauthenticated requests behave as specified; no disabled security to obtain green tests. |
| Persistence | Queries, transactions, rollback and migration ordering pass against isolated data. |
| Reactive/blocking | Verify execution placement, cancellation and context; a synchronous toy endpoint does not prove these. |
| Operations | Check health/readiness and shutdown, then packaged startup and deployment configuration in a test environment. |
| Compatibility | Test every retained Spring feature. Unsupported APIs are blockers, not a reason to add the entire Spring runtime until compilation succeeds. |

Record versions, commands, counts and failures. A small HTTP fixture establishes only its exercised behaviour, not native-image, security, persistence or production acceptance.
