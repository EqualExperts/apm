# Replace managed behaviour explicitly

| Quarkus facility | Pure Vert.x responsibility |
| --- | --- |
| Managed Vert.x and lifecycle observers | Own Vert.x creation, asynchronous deployment and close. Readiness follows successful binding and consumer registration; startup failure must terminate or surface rather than leave a half-running service. |
| Arc/CDI injection, producers, scopes and interceptors | Explicit constructors/factories and ownership. Reproduce relevant scope, lazy initialization and interceptor behaviour; do not replace request-scoped state with a shared singleton. |
| REST resources and reactive routes | Explicit Vert.x Web routes, binding, body limits, validation, content negotiation, error mapping and ordering. Jakarta REST annotations alone do nothing in a bare Router. |
| ConsumeEvent | Register event-bus consumers, reply/fail paths, codecs, timeouts and unregister lifecycle. Distinguish local consumers from clustered delivery. Test registration before requests. |
| Mutiny and context propagation | Select core Future/Promise or independently managed adapters deliberately. Preserve context, cancellation and request state. Quarkus duplicated contexts and CDI request scope do not appear automatically. |
| Config and profiles | Explicit typed configuration, defaults, validation and precedence. Translate quarkus-prefixed keys; loading their text does not apply them to Vert.x options. Redact secrets. |
| Security/OIDC | Explicit compatible Vert.x Auth/Web handlers or approved libraries. Preserve token validation, roles, tenant rules, CSRF/CORS and TLS. Test denied and allowed requests. |
| Panache, ORM/reactive sessions and transactions | Explicit client/session factories, transaction boundaries, rollback and shutdown. Panache behaviour is not recreated by swapping a database client. Keep blocking access off event loops. |
| Reactive Messaging, scheduling and retries | Explicit clients/consumers/timers with acknowledgement, retry, ordering, idempotency and cancellation semantics. Avoid duplicate background work during redeployment. |
| Health, telemetry and packaging | Explicit probes, metrics/tracing, executable entrypoint, signal handling and resource closure. Preserve management endpoint exposure policies. Native-image metadata and Quarkus fast-jar assumptions need separate replacement. |

## Sources

Use guides for the selected versions; latest documentation may describe a different major release.

- [Quarkus Vert.x reference](https://quarkus.io/guides/vertx-reference) — managed runtime and event consumers to inventory.
- [Quarkus CDI reference](https://quarkus.io/guides/cdi-reference) — scopes and interception that removal must account for.
- [Quarkus reactive routes](https://quarkus.io/guides/reactive-routes) — route semantics on the source side.
- [Vert.x Core](https://vertx.io/docs/vertx-core/java/) — deployment, futures, contexts, event bus and lifecycle.
- [Vert.x Web](https://vertx.io/docs/vertx-web/java/) — explicit router behaviour and handlers.
- [Vert.x Auth](https://vertx.io/docs/vertx-auth-common/java/) — authentication primitives, not an automatic security replacement.
- [Vert.x SQL client](https://vertx.io/docs/vertx-sql-client/java/) — reactive connection and transaction ownership.

Do not combine a major Vert.x upgrade with framework removal without identifying the additional API/behaviour changes. An independently selected target fixture is evidence of its contract only, not universal binary compatibility with Quarkus-managed Vert.x.
