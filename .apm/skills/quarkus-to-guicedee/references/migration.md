# Replacement decisions

The installed GuicedEE skills and release documentation own exact APIs. The reviewed marketplace baseline requires Maven 4, JDK 25+, the `com.guicedee:guicedee-bom` import and separate main/test JPMS packages. Test packages end in `.test`, open to JUnit Platform, and declare the required test modules. Confirm inherited dependencies with the effective POM before duplicating versions.

| Quarkus facility | GuicedEE replacement and evidence |
| --- | --- |
| Arc/CDI beans | Guice constructors/bindings and explicit scope mapping. Review producers, qualifiers, interception and request state; bridge only supported CDI features. |
| Startup/shutdown | Lifecycle SPIs with both module-info provides and META-INF/services. Register the application module before injection. Use GuiceApplication for process mains; tests use embedded startup and await getLoadingFinished. Destroy is terminal: use a fresh JVM for another complete lifecycle. |
| Managed Vert.x | guicedee-vertx lifecycle and injected runtime. Resolve versions via the GuicedEE BOM, including Mutiny adapters. Preserve nonblocking work and explicitly configured worker execution. |
| ConsumeEvent | VertxEventDefinition consumers and named publishers where appropriate; verify request/reply, failure, timeout, codec and lifecycle semantics rather than mechanically renaming annotations. |
| REST/routes | guicedee-rest or web router SPI. Check request binding, errors, validation, body limits and security before removing Quarkus routing. |
| Properties/profiles | Use GuicedEE Config/Environment and explicit key mapping. Quarkus-prefixed settings do not automatically configure the replacement. |
| Panache/transactions | Explicit reactive persistence/session/query layer; preserve rollback, authorization and transaction scope. Do not replace reactive access with blocking ORM on event loops. |
| Security/JWT | GuicedEE auth/JWT integration with equivalent roles, claims, tenant rules and denied-access tests. Do not substitute permissive routes. |
| Packaging/observability | Replace Quarkus augmentation, runner and probes with GuicedEE lifecycle, health/metrics/telemetry modules and a verified executable entrypoint. Native images need separate proof. |

Open injection packages to `com.google.guice`, DTO packages to `tools.jackson.databind`, and relevant Vert.x packages to `com.guicedee.vertx`. Retain Jackson annotation namespaces where appropriate. Check module names against the chosen artifacts rather than inventing requires directives.

Sources: [GuicedEE marketplace](https://github.com/GuicedEE/ai-rules), [GuicedEE](https://guicedee.com/), [Quarkus CDI](https://quarkus.io/guides/cdi-reference), [Quarkus Vert.x](https://quarkus.io/guides/vertx-reference). The GuicedEE marketplace instructions are versioned dependencies of this workflow, not copied vendor documentation.
