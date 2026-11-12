# Acceptance evidence

Compare the same external contracts before and after migration. Use isolated, approved test services and explicit timeouts; inspect test counts and skipped tests.

| Area | Required evidence when applicable |
| --- | --- |
| Build and startup | Clean augmentation, resolved BOM/plugin versions, discovered beans, required configuration errors and packaged process startup. |
| HTTP | Real requests for successful JSON, absent routes, invalid inputs, exception bodies, methods, content types, dates, decimals and nulls. |
| Injection/configuration | Constructor dependencies, qualifiers, scopes, conditional components, profile precedence and runtime overrides. |
| Security | Anonymous, expired credentials, insufficient roles, allowed users and cross-tenant denials; management endpoint exposure and browser protections. |
| Data | Representative repository queries, pagination, transaction commit/rollback, schema compatibility and concurrency. |
| Reactive/integrations | Event-loop isolation, cancellation, streaming/backpressure, messaging retries/acknowledgement and context propagation. |
| Operations | Readiness/liveness, shutdown, metrics/tracing, deployment configuration and rollback procedure. |
| Removal | Dependency tree and source search identify remaining Spring APIs and their intentional compatibility providers; no obsolete Boot launcher. |

Repository smoke fixtures compare the existing Spring baseline at `tests/fixtures/spring-to-micronaut-baseline` with `tests/fixtures/spring-to-quarkus`. Both exercise constructor injection and real HTTP: JSON success, content type and missing-route status. The new target uses native CDI and Jakarta REST, not Spring compatibility. These checks do not establish security, persistence, reactive, compatibility-extension, native-image or production acceptance. An application migration needs the broader scenarios above.
