# Acceptance

1. Record marketplace revision, selected packages/target and actual installed files. Run APM validation/audit in the consumer as appropriate; do not add a consumer manifest to this provider.
2. Run the installed GuicedEE baseline validator. Reconcile inherited settings with the effective POM and dependency tree; do not weaken valid configuration to satisfy a local-file-only check.
3. Build on the selected JDK/Maven and verify module access, service discovery, Guice binding and asynchronous loading. Never call the exit-owning process bootstrap inside an in-process unit test.
4. Compare source/target real HTTP and event-bus contracts, including failed/unauthorized requests. Verify call-scope isolation and nonblocking execution where used.
5. Verify reactive persistence, rollback, configuration, health and shutdown with isolated services. Test failed startup and partial cleanup where resources are involved.
6. Inspect the runtime tree and packaged output for Quarkus extensions/Arc and obsolete build plugins. Start the packaged application separately from unit tests.

Run the project's Maven wrapper with `verify`, `help:effective-pom` and `dependency:tree`; inspect actual test counts and skipped suites. Report static baseline, runtime injection, HTTP/integration and production checks separately. A small fixture does not establish all extension compatibility.
