# Node.js migration decisions

Choose a supported Node.js release, JavaScript or TypeScript, module system and HTTP framework explicitly. Native HTTP is sufficient for the fixture, not mandatory for production. TypeScript does not validate untrusted JSON at runtime. Pin dependencies and use the selected package manager's reproducible lock/install workflow.

Replace Arc with explicit factories or the selected framework's composition model. Replace Jakarta REST with handlers, validation and ordered middleware. Centralize rejected-promise/error handling. CPU-heavy work and synchronous I/O block the event loop; use bounded workers/offloading where needed. Preserve streaming backpressure and disconnect/cancellation handling.

Java long/BigInteger/BigDecimal cannot generally map safely to JavaScript Number. Define wire representations for large integers and decimals; test dates/timezones, omitted versus null values, enum casing and BigInt serialization. Replace Panache/JTA with explicit transactions; do not assume Java libraries have equivalent Node packages. Test async request-identity isolation.

Preserve JWT/OIDC validation, authorization, CORS/CSRF/TLS and body limits. Native HTTP is not a security framework. Configure deadlines and graceful drain; server close does not dispose of all pools, consumers or upgraded connections. Do not replace event-bus delivery with EventEmitter without checking its different semantics.

## Official sources

- [HTTP and lifecycle](https://nodejs.org/api/http.html)
- [Built-in tests](https://nodejs.org/api/test.html)
- [Async context](https://nodejs.org/api/async_context.html)
- [Streams and backpressure](https://nodejs.org/api/stream.html)
- [Quarkus source behaviour](https://quarkus.io/guides/vertx-reference)

Read the selected version's documentation. The [HTTP fixture](http-contract.md) is a bounded example, not a production template.
