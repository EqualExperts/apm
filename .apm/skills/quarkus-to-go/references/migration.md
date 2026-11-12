# Go migration decisions

Choose a supported Go toolchain and pin modules. Use net/http or the approved router; adopting a larger framework is a separate decision. Compose services with constructors/interfaces and ordered middleware rather than simulating CDI. Map exceptions to explicit error handling.

HTTP requests execute concurrently: shared maps, caches and services need deliberate synchronization/ownership. Propagate context.Context through client and database calls. Bound concurrency and avoid orphan goroutines; use the race detector on representative paths. Shutdown does not close every application resource or hijacked connection automatically.

Java nullable fields, primitives, generics and exceptions are not mechanical Go translations. Decide pointers/optional fields, JSON tags, omitted/null behaviour, unknown-field policy and exact integer/decimal representation. Avoid float64 decoding for numbers that need exactness. Test time formats and enum validation.

Replace Panache/JTA with explicit repositories and transactions. Preserve rollback/isolation. net/http alone does not validate tokens or roles: select reviewed auth middleware and test denied access. Configure timeouts, request-size limits and TLS. Goroutines/channels are not durable queues or a replacement for distributed Vert.x messaging.

## Official sources

- [HTTP and shutdown](https://pkg.go.dev/net/http)
- [Cancellation and context](https://pkg.go.dev/context)
- [JSON](https://pkg.go.dev/encoding/json)
- [Race detector](https://go.dev/doc/articles/race_detector)
- [Module reference](https://go.dev/ref/mod)
- [Quarkus source behaviour](https://quarkus.io/guides/vertx-reference)

Use documentation matching the selected toolchain. Standard-library fixture success does not prove third-party integration compatibility.
