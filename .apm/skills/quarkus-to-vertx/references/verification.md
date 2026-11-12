# Acceptance scenarios

Run the source build before edits and the target build without Quarkus test dependencies. Use the project's checked-in Maven/Gradle wrapper and inspect test reports for skipped tests.

| Scenario | Evidence |
| --- | --- |
| HTTP | Real server on a random local port: compare status, headers, payloads, missing routes and invalid inputs. Verify limits, errors and authorization where used. |
| Event bus | Successful request/reply, explicit failure and timeout; consumer registration completes before readiness and unregisters on stop. |
| Execution | Assert appropriate context for asynchronous handlers and isolate blocking work. Thread-safe service wiring must preserve per-request isolation. |
| Startup/shutdown | Await binding/deployment. Test startup failure and cleanup. Close owned resources and ensure redeployment does not duplicate consumers/timers. |
| Data/security | Exercise rollback, sessions, token/role rules and denied access using isolated services; do not infer these from a hello endpoint. |
| Removal | Inspect source imports, effective POM/Gradle configuration, dependency tree and packaged runtime for Quarkus/Arc extensions and plugins. The target must start without Quarkus. |
| Packaging | Verify the production entrypoint and signal handling separately from in-process tests. Revalidate native images only if part of the application scope. |

Useful review commands, adapted to the project's wrapper:

```text
./mvnw verify
./mvnw dependency:tree
./mvnw help:effective-pom
./gradlew build
./gradlew dependencies --configuration runtimeClasspath
```

Report exact source and target versions and each unperformed check. Synthetic HTTP/event-bus fixtures do not prove persistence, security, telemetry, clustering or production readiness.
