# Migration decisions

Create an extension inventory from the source build and resolved dependencies. For each extension record its responsibilities, target integration, configuration changes and acceptance checks. Use target-version documentation; neither Jakarta API overlap nor a similarly named module proves behavioural equivalence.

| Quarkus concern | Micronaut migration decision |
| --- | --- |
| Augmentation and bootstrap | Replace Quarkus plugins, generated bootstrap and dev-mode assumptions with Micronaut build processing and application startup. Configure processors for the chosen language; prove beans and routes from a clean build. |
| ArC/CDI | Review scopes, qualifiers, producers, alternatives, interceptors, observers and destruction. Map to Micronaut beans, factories, conditions, events and lifecycle hooks where semantics match. Test eager/lazy initialization and request scope; do not assume CDI extensions or self-interception transfer. |
| RESTEasy/Quarkus REST | Port Jakarta REST resources to Micronaut controllers and explicit bindings. Rewrite filters, exception mappers, validation and multipart/streaming handling. Compare status, media type, headers and error body. |
| SmallRye Config | Map ConfigMapping, profiles, environment overrides and build-time configuration to target configuration beans and environments. A quarkus.* property has no automatic Micronaut effect. |
| Panache and Hibernate | Replace active-record and repository convenience APIs with selected Micronaut Data repositories or explicit persistence operations. Choose blocking JPA/JDBC or reactive R2DBC according to requirements; these are not interchangeable. Preserve IDs, query ordering, pagination, locking, transaction boundaries and rollback. |
| Mutiny and Vert.x | Select documented reactive types/adapters. Preserve laziness, failure, cancellation, backpressure and context. Treat direct Vert.x usage as an explicitly managed integration, including startup and close. Verify execution placement instead of copying Quarkus blocking annotations. |
| OIDC and SecurityIdentity | Rebuild authentication, role mapping, tenant selection and method/route authorization with Micronaut Security. Preserve token issuer/audience checks, session, CSRF and CORS requirements. |
| REST clients | Replace MicroProfile clients with target HTTP clients or intentionally retained standalone clients; preserve timeout, retry, authentication propagation and error mapping. |
| Messaging and scheduling | Select target integrations; preserve acknowledgements, retry limits, dead-letter routing, duplicate handling and scheduler concurrency. Dev Services provisioned infrastructure needs explicit test replacements. |
| Operations and packaging | Map health/readiness, metrics, traces, shutdown and deployment settings. Quarkus native metadata does not prove Micronaut native compatibility. Rebuild and test the chosen package separately. |

## Official sources

Read only the guides needed for the features being migrated, recording the selected versions:

- [Quarkus CDI](https://quarkus.io/guides/cdi-reference/) and [Mutiny](https://quarkus.io/guides/mutiny-primer/) for source container and reactive semantics.
- [Quarkus guides](https://quarkus.io/guides/) for the source extensions' REST, Panache, security, messaging and Dev Services contracts.
- [Micronaut Core](https://docs.micronaut.io/5.2.x/core/) for DI, HTTP, configuration, lifecycle and execution.
- [Micronaut Data](https://micronaut-projects.github.io/micronaut-data/latest/guide/) for queries and transactions.
- [Micronaut Security](https://micronaut-projects.github.io/micronaut-security/latest/guide/) for target authentication and authorization.
- [Micronaut Serialization](https://micronaut-projects.github.io/micronaut-serialization/latest/guide/) for DTO processing and JSON contracts.
- [Micronaut Test](https://micronaut-projects.github.io/micronaut-test/latest/guide/) for target context and integration testing.
