# Authoring APM primitives

Author package primitives under `.apm/`. Choose a prompt for an explicitly invoked workflow, an instruction for a persistent rule, an agent for a named specialist, and a skill for a reusable capability discovered by its description. Follow the [skill standard](SKILL_STANDARD.md) for skills and [Microsoft's target matrix](https://microsoft.github.io/apm/reference/targets-matrix/) for current target support. APM's transformations do not make all primitives or metadata available on every harness.

## Prompts and commands

Place one focused workflow per `.apm/prompts/<name>.prompt.md`. Its basename becomes the command name. Give it a one-line `description`; use `input`, `allowed-tools`, `model` and `argument-hint` only as needed. Reference named inputs in the body as `${input:name}`. Input names must begin with a letter and contain no more than 64 letters, digits, underscores or hyphens. Avoid additional frontmatter that may be dropped on transformed targets.

Write the body as direct instructions to the model. Commands are prompts; do not create a separate commands directory or duplicate a command name at the package root. Codex has no prompt primitive in the documented target mapping: where that workflow must reach Codex, provide a suitable skill as well and avoid duplicating guidance unnecessarily. Tool and model metadata is not enforced uniformly across targets.

## Instructions

Place one topic per `.apm/instructions/<name>.instructions.md`. Include a `description` and, for file-scoped rules, `applyTo` with a glob, comma-separated globs or a YAML list. Without `applyTo`, an instruction is unconditional rather than file-scoped. Write short, actionable rules and identify relevant repository paths. Check the target matrix: some harnesses receive native rules while Codex, Gemini and OpenCode use compiled context rather than per-file deployment.

## Agents

Place a named specialist in `.apm/agents/<name>.agent.md` using a real file, not a symlink. Supply a clear `description` and a descriptive name; avoid `default` and `start`. Explain its role, scope, required inputs, boundaries and expected output without repeating shared repository instructions. Keep the body under 300 lines.

Optional fields such as `model`, `model_reasoning_effort`, `tools`, `color`, `handoffs` and `user-invocable` have target-specific support. Do not claim that a tool restriction or picker visibility is enforced unless the selected harness supports it. Codex cannot preserve tool restrictions from these agents; do not rely on them for access control. OpenCode expects a boolean tool mapping and supported colour values; Kiro accepts only its supported tool capability tags. Windsurf and Gemini do not receive this agent primitive; consider a skill when the workflow needs to reach them.

## Hooks

Place JSON hook descriptors in `.apm/hooks/`. Hooks are runtime callbacks with target-specific behaviour, not portable instructions; unsupported targets may skip them. Use simple filenames and explicit package target restrictions where needed. A package's targets can narrow the consumer's active targets but cannot enable a target the consumer did not select. Do not use deprecated filename-based target routing.

APM accepts supported Claude and Copilot event shapes and translates them for supported targets, but event names, matchers and handler fields are not universally interchangeable. Cursor applies stricter validation and can reject unsupported translations. Choose one deployment route per dependency where Cursor imports Claude hooks, and check the resulting configuration for overlapping behaviour. Consult the current [hook and command guidance](https://microsoft.github.io/apm/producer/author-primitives/hooks-and-commands/) for event mappings and target support.

Use Python for executable helpers under this repository's script policy. Reference bundled helpers through supported package-root tokens such as `${PLUGIN_ROOT}`, quoting paths that may contain spaces; do not hard-code a contributor's machine path. Confirm the helper is present in the installed bundle and that the intended harness can execute it. APM's hook ownership sidecars are managed by APM and should not be edited manually.

## MCP servers

Declare MCP dependencies in the package's `apm.yml` under `dependencies.mcp` or, for development-only servers, `devDependencies.mcp`. There is no separate MCP primitive directory. Use registry references where appropriate; for self-defined servers, provide the supported transport and its required `command` and `args` or HTTP(S) `url`. Put arguments in `args`, not in the command string.

Do not commit credentials. Use environment-variable references and review how each target handles them: some preserve references while others may resolve values during installation. Document self-defined servers and their requirements for consumers. APM can skip self-defined servers received transitively unless the consumer explicitly trusts them; do not assume they were installed. Verify the generated target configuration and use `apm mcp list` where applicable. See [MCP authoring](https://microsoft.github.io/apm/producer/author-primitives/mcp-as-primitive/) for schema and current behaviour.

## Verification

Validate and preview against the actual package and intended targets. Where supported by the installed APM version, use `apm compile --validate`, `apm install --dry-run --target <target>` and `apm audit` as appropriate. Inspect generated output and warnings, especially dropped metadata and target-specific restrictions; run meaningful behavioural checks before claiming support. A dry run or structural check alone does not prove an agent works as intended. This repository has not yet configured an APM package, so these commands are not yet verified here.

Dry runs do not render hook previews. For hooks, inspect a real installation in an isolated test project and exercise each intended harness before publishing. Test MCP configuration and credential handling in the relevant target without committing secrets.

See Microsoft's [prompt guidance](https://microsoft.github.io/apm/producer/author-primitives/prompts/) and [instructions and agents guidance](https://microsoft.github.io/apm/producer/author-primitives/instructions-and-agents/) for the current schemas and transforms. Repository scripts remain Python-only, and diagrams use Mermaid.
