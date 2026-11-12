# http4k migration decisions

Align JVM/Kotlin and http4k versions, using the BOM as appropriate. Select a server backend for protocol and deployment requirements. HttpHandler maps Request to Response; wire dependencies explicitly and compose Filters around routes. Jakarta REST/CDI annotations do not provide routing or injection in http4k.

Use lenses/codecs for extraction and response construction, with explicit invalid-input/error handling. Preserve filter order, authentication, authorization, CSRF/CORS, tracing and transaction boundaries. Test both pure handlers and the real server adapter.

The core handler model is synchronous, not a drop-in Mutiny/Vert.x nonblocking runtime. Evaluate backend execution, blocking clients, JDBC, streaming, WebSockets and cancellation. Do not execute blocking handlers on a shared Vert.x event loop without deliberate isolation.

Java/Kotlin interoperability does not guarantee unchanged JSON. Test nullable/default fields, JSON engine configuration, exact decimals/longs, timestamps and error payloads. Reuse domain libraries only after checking their Quarkus dependencies. Panache and Arc need explicit replacements; retaining JPA requires independent lifecycle and transaction wiring.

Own server start/stop, pool/client cleanup, configuration and management endpoint exposure. Consult official http4k agent guidance when available, otherwise use primary documentation. That skill is optional and does not certify a migration.

## Official sources

- [Core model](https://www.http4k.org/ecosystem/http4k/reference/core/)
- [Server adapters](https://www.http4k.org/ecosystem/http4k/reference/servers/)
- [Lenses](https://www.http4k.org/ecosystem/http4k/concepts/lenses/)
- [Official agent guidance](https://github.com/http4k/agent-skills)
- [Quarkus CDI behaviour](https://quarkus.io/guides/cdi-reference)

Verify selected-version APIs and backend support rather than assuming latest documentation matches an older dependency.
