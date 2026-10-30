# Skill standard

## Structure and naming

Each skill is a directory under `skills/<tier>/` named in lowercase kebab-case. Tiers are `.system`, `.curated` and `.experimental`; see [catalogue design](CATALOGUE.md). Skill names must be unique across all tiers, including case-insensitive comparisons. The directory name and `name` in frontmatter must match. Paths and filenames are case-sensitive in this repository, including on case-insensitive development systems. Use the exact names below:

```text
skills/<tier>/<skill-name>/
  SKILL.md
  agents/openai.yaml
  references/           # when needed
  scripts/              # when needed; Python scripts only
  assets/               # when needed
```

`SKILL.md` and `agents/openai.yaml` are required for every APM skill. Optional directories exist only when they contain useful resources. Do not use case-only renames or names that collide across case-insensitive filesystems. Use lowercase kebab-case for supporting filenames, except where a tool or format requires a specific name. Capitalisation makes a filename recognisable; it does not confer instruction priority.

## Instructions and references

`SKILL.md` starts with YAML frontmatter containing `name` and `description`. The description states what the skill does and when to use it. Its body contains purpose, necessary workflow, constraints and links that say when to consult supporting resources. Keep it concise and specific enough to avoid accidental activation.

Do not put examples in `SKILL.md`. Place useful examples in Markdown files in `references/`; split numerous or distinct examples into focused files. References contain conditional detail, sources and domain guidance; assets contain templates or other files used in output. Avoid redundant material and placeholders.

## OpenAI metadata

Provide `agents/openai.yaml` using the currently supported OpenAI schema. Define meaningful `interface.display_name`, `interface.short_description` and `interface.default_prompt`; the prompt identifies the skill using `$<skill-name>`. Declare actual tool dependencies where supported. Set invocation policy deliberately where needed. Add branding and other optional fields only when applicable and backed by real assets. Do not invent dependencies, values or permissions merely to populate fields. Validate against current OpenAI guidance when creating or updating metadata.

## Scripts and dependencies

All executable scripts in this repository must be Python, saved as `.py`; do not add shell, PowerShell, batch or other script files. State Python version and third-party dependencies where needed. Prefer the standard library when practical. Scripts should have clear inputs, outputs, error handling and documented side effects; avoid exposing secrets or silently modifying external systems. Test changed scripts and cover meaningful failure paths.

## Compatibility and quality

Specify actual tool, platform, network and permission requirements and supported harnesses where relevant. Keep shared guidance independent of one model or harness where possible; isolate product-specific behaviour. Verify claimed compatibility in the relevant environment and record limitations. Review skill discovery, instruction quality, examples and realistic task outcomes, including failure and misuse cases appropriate to the risk. A format check alone is not a behavioural or security evaluation.

## Creator and installer

APM's creator and installer will be based on OpenAI's corresponding models, adapted to this standard. Record upstream source and revision when adopting code or guidance, respect its licence, and review upstream changes. The creator should generate and validate the APM contract. The installer should support explicit source and version, provenance, safe handling of existing installations and documented updates; it must not silently overwrite customisations. These are requirements for future tooling, not claims that it exists today.
