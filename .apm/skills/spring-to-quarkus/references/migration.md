# Migration decisions

## Destination and upstream guidance

The [official migration overview](https://quarkus.io/spring/migrate/) describes native Quarkus and Spring compatibility destinations and links the [Quarkus agent skills](https://github.com/quarkusio/skills). Consult that maintained guidance when useful; review its source and current revision before installing or running it. This package does not install it automatically or copy its instructions. Tool-generated edits still require contract review.

Prefer native APIs when the intended result removes Spring dependencies. Compatibility can reduce changes where every retained annotation and API is documented for the chosen Quarkus version. Record that choice per module, including any temporary compatibility dependency and its removal criteria.

| Spring concern | Quarkus migration decision and verification |
| --- | --- |
| Boot parent, starters, launcher | Import a compatible platform BOM and matching Quarkus build plugin; choose extensions and packaging deliberately. Verify effective dependencies and packaged startup. |
| Bean configuration, injection, scopes | Map to CDI beans, qualifiers and producers; check discovery, scope, proxying, conditional beans and initialization order. Review reflection and dynamically registered beans against build-time discovery. |
| Spring DI compatibility | The extension interprets supported metadata without starting a Spring application context. ApplicationContext calls, BeanPostProcessors and arbitrary Spring infrastructure need replacements. |
| MVC controllers | Use Jakarta REST resources and the selected JSON extension, or supported Spring Web annotations with the required REST implementation. Verify binding, validation, exception mapping, content negotiation, status codes and error bodies. Servlet-specific filters and APIs need a separately justified stack. |
| WebFlux and Reactor | Decide threading and streaming contracts before adapting types. Preserve cancellation, backpressure and security context; verify blocking isolation. A synchronous return type does not prove reactive equivalence. |
| Properties and profiles | Map keys explicitly to Quarkus configuration and config mappings. Distinguish build-time settings from runtime overrides, including profile precedence and missing required values. |
| JPA and repositories | Choose Hibernate ORM/Panache or the documented Spring Data JPA subset. Inventory derived queries, custom repositories, pagination, projections and locking rather than assuming API coverage. Preserve identifiers and schema migrations. |
| Transactions | Map propagation, rollback rules and resource enlistment explicitly. Reactive persistence is a separate execution model, not a mechanical repository replacement. Test rollback and lazy access boundaries. |
| Security | Replace authentication providers and filter-chain behaviour explicitly. The Spring Security extension supports a subset of authorization annotations/expressions; it is not the Spring Security runtime. Verify role prefix semantics, method interception, OIDC/JWT, CSRF, CORS, sessions and tenant isolation as applicable. |
| Events, scheduling and messaging | Distinguish in-process events from durable messaging. Preserve acknowledgement, retry, ordering, scheduling concurrency and shutdown behaviour; do not replace delivery guarantees with local callbacks. |
| Actuator and operations | Map required health, metrics, tracing and management endpoints with equivalent exposure controls. Validate shutdown and readiness in the packaged application. |

## Version-specific sources

Read only the guides relevant to the inventory, using documentation matching the selected release:

- [CDI reference](https://quarkus.io/guides/cdi-reference) and [Spring DI](https://quarkus.io/guides/spring-di/): bean discovery and supported compatibility metadata.
- [REST](https://quarkus.io/guides/rest) and [Spring Web](https://quarkus.io/guides/spring-web/): HTTP bindings and execution model.
- [Configuration reference](https://quarkus.io/guides/config-reference): build/runtime settings and profiles.
- [Spring Data JPA](https://quarkus.io/guides/spring-data-jpa/) and [transactions](https://quarkus.io/guides/transaction): repository support and transaction semantics.
- [Spring Security](https://quarkus.io/guides/spring-security/) and [security overview](https://quarkus.io/guides/security-overview): supported authorization and authentication choices.
- [Testing](https://quarkus.io/guides/getting-started-testing): application and packaged integration test boundaries.
