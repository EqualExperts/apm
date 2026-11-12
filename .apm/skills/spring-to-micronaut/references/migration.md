# Migration decisions

A native migration replaces Spring bootstrap and APIs with Micronaut equivalents. A compatibility migration uses Micronaut for Spring's compile-time support for a documented subset. Adding the Micronaut Spring Boot starter to a Spring runtime is a third integration scenario, not proof of framework replacement. Treat unlisted Spring features as unsupported until demonstrated.

| Concern | Decision and verification |
| --- | --- |
| Build | Use compatible platform dependency management and explicit annotation processing for the language/JDK. A clean build must generate working beans and routes. |
| DI | Review constructor injection, Jakarta scopes, factories, qualifiers, conditional beans and lifecycle. Do not assume Spring scanning or proxy/self-invocation semantics transfer unchanged. |
| HTTP | Port controllers and explicit request/response bindings. Compare paths, verbs, headers, status and error payloads. Servlet filters are not automatically Netty filters. |
| Configuration | Map keys, typed configuration, environments and precedence deliberately; a Spring YAML key need not be consumed by Micronaut. Test overrides without exposing secrets. |
| Serialization | Choose Micronaut Serialization or Jackson Databind integration deliberately. Configure processing and DTO introspection/Serdeable where required. Test dates, enums, nulls and custom serializers. |
| Security | Replace Spring filter chains, method security and OAuth configuration explicitly. Test unauthenticated, forbidden and allowed access. Retain relevant CSRF/CORS/TLS and session requirements. |
| Data | Select Data/JPA/JDBC/R2DBC integration; verify repository queries, lazy loading, transaction propagation and rollback. Keep schema migration separate and use isolated data. |
| Execution | Preserve cancellation, context and backpressure. Keep blocking database/client work off Netty event loops using the documented execution model. Test scheduling and messaging semantics separately. |
| Operations | Re-map health/readiness, metrics, tracing and shutdown without widening endpoint exposure. Measure performance instead of assuming improvements. |

## Official sources

Read the sources relevant to the affected features. Latest URLs can change major version: record selected versions and check their release documentation before editing.

- [Core guide](https://docs.micronaut.io/latest/guide/) — DI, HTTP, configuration, threading and processing.
- [Micronaut for Spring](https://micronaut-projects.github.io/micronaut-spring/latest/guide/) — supported annotations/interfaces and unsupported features.
- [Serialization](https://micronaut-projects.github.io/micronaut-serialization/latest/guide/) — engine selection and processing.
- [Security](https://micronaut-projects.github.io/micronaut-security/latest/guide/) — authentication and authorization.
- [Data](https://micronaut-projects.github.io/micronaut-data/latest/guide/) — repositories and transactions.
- [Test](https://micronaut-projects.github.io/micronaut-test/latest/guide/) — context and integration testing.
