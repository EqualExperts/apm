# Verification scenarios

Run in the consuming project, using its wrapper and existing profiles. Examples are commands to adapt, not evidence of a completed migration.

```text
./mvnw verify
./mvnw dependency:tree
./gradlew build
./gradlew dependencies --configuration runtimeClasspath
```

On Windows use the checked-in Windows wrapper. Record the actual executed test counts and skipped suites. Do not substitute a skipped-test build for acceptance.

| Scenario | Acceptance evidence |
| --- | --- |
| MVC application | Controller and JSON tests pass with new MVC test imports and technology test starter; compare status, headers and payload contracts. |
| Reactive application | Preserve WebFlux/nonblocking architecture; verify reactive controller and client tests. Do not replace WebFlux with MVC to resolve imports. |
| Security | Verify unauthenticated, forbidden and allowed requests; retain applicable CSRF/CORS/TLS requirements. |
| Persistence | Use isolated test data to verify startup schema validation, transactions and migration scripts. Never run a destructive schema reset against retained data. |
| Serialization | Compare representative dates, enums, nulls and custom Jackson modules. Retain Jackson annotation imports. |
| Runtime | Start the packaged application in a test environment; check representative endpoints and configured health/readiness. Remove the properties migrator and repeat. |
| Native/Kotlin/integrations | Run native build, Kotlin compilation and relevant external integration tests only where used; record each unperformed check. |
| Blocked dependency | Stop the affected change and report incompatible coordinates/version and evidence. Do not force resolution or disable security/tests. |

A clean skill validator checks packaging only. A sample application validates only its exercised surface. Keep those results separate from consumer runtime acceptance.
