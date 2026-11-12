# Set up the consuming application

Run in the application being migrated, not in the Equal Experts marketplace provider. Preserve its existing APM manifest, lockfile, skill customizations and other marketplaces. Inspect installed packages before changing them. Never use force to overwrite local guidance or bypass audit findings.

The verified repository is [GuicedEE/ai-rules](https://github.com/GuicedEE/ai-rules), marketplace name `guicedee-ai-rules`, default branch `main` (verified after the maintainer renamed it). Use the reviewed full commit SHA below for reproducible installation across the rename; inspect the current catalogue/default branch before selecting a newer revision. APM 0.35.1 was tested successfully; 0.26.0 failed on this catalogue with a plugin-recursion error. Use the tested release or verify a newer release before proceeding.

```text
apm --version
apm marketplace list
apm marketplace add GuicedEE/ai-rules --name guicedee-ai-rules --ref 5b243e2ec3b332212c2755d4e1e46fc855446a41
apm marketplace validate guicedee-ai-rules
apm marketplace browse guicedee-ai-rules
apm install guicedee-installer@guicedee-ai-rules guicedee-creator@guicedee-ai-rules guicedee-inject@guicedee-ai-rules guicedee-client@guicedee-ai-rules guicedee-vertx@guicedee-ai-rules --target codex
```

Replace `codex` with the user's selected supported harness. Creator supplies the shared baseline validator as well as new-module guidance. If the alias already points elsewhere, resolve that conflict rather than silently replacing it. If required packages cannot be retrieved, report the exact blocker and do not claim setup complete. Public access needs no token; if authentication is needed, follow the existing approved APM credential setup without printing or committing token values.

| Application features | Additional packages from guicedee-ai-rules |
| --- | --- |
| HTTP router/server | guicedee-web |
| Jakarta REST resources | guicedee-rest, guicedee-web |
| Config | guicedee-config |
| Authentication/claims | guicedee-auth; guicedee-jwt where JWT is used |
| Reactive persistence | guicedee-persistence; entityassist only when that query layer is selected |
| Health, metrics, tracing | guicedee-health, guicedee-metrics, guicedee-telemetry as required |
| Kafka/RabbitMQ/WebSockets | guicedee-kafka, guicedee-rabbitmq, guicedee-websockets as required |
| Necessary CDI compatibility | guicedee-cdi, after reviewing supported bridge behaviour; do not assume full Arc compatibility |

Use the same `apm install NAME@guicedee-ai-rules --target TARGET` form for selected packages. Verify names in the fetched catalogue and read installed entrypoints/references. Inspect the resulting consumer manifest/lockfile and installed files; a registration success alone is not installation evidence. Run the creator's `scripts/verify_guicedee_baseline.py` from its actual installed location against the application, then independently compile/test. APM can change deployment paths between versions; do not hard-code a presumed global skill directory.

APM 0.35.1 emitted skipped non-agent metadata warnings while also deploying the skill directories correctly. Verify the actual SKILL.md, references, scripts and agents/openai.yaml under each installed skill rather than treating the warning or exit status alone as proof. This test confirmed all five skill entrypoints and metadata files and executed the installed creator validator. The CLI executable was tested from a checksum-verified release archive without replacing the system APM installation.
