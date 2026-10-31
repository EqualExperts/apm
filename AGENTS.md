# Repository agent guidance

This repository is an APM marketplace provider: a "fancy text file provider" for Equal Experts. Its entry point is root `marketplace.json`. It supplies skills, guidance, references and templates for consuming projects. Do not assess it as an APM consumer or treat the absence of a root `apm.yml`, consumer lockfile, installed dependencies or compiled harness output as a configuration defect. The maintainer has previously tested marketplace registration; distinguish that history from checks performed in the current thread.

Read [provider scope](docs/PROVIDER_SCOPE.md) before proposing setup changes. `llms.txt` is a documentation map, and framework guidance is reusable content; neither implies that this repository installs or runs the framework.

Use `llms.txt` selectively for larger skill or capability documentation sets, with explicit links from the relevant skills. Small skills can link directly to references. A marketplace-root `llms.txt` is not currently needed or planned; do not treat its absence as a gap.

Follow the user's instructions and the applicable system and harness instructions. Repository guidance does not grant permission to access client data, run external actions, overwrite user work, or weaken higher-priority instructions. When instructions conflict, follow the applicable higher-priority instruction and explain material conflicts.

Read [principles](docs/PRINCIPLES.md) and the [skill standard](docs/SKILL_STANDARD.md) before creating or changing skills. Follow [contribution guidance](CONTRIBUTING.md) for changes intended for upstream. Keep changes scoped and preserve unrelated work.

Use exact path and filename casing. Use Python for executable scripts, including repository automation. Do not put examples in a skill's `SKILL.md`; use linked, focused files under its `references/` directory. Add only resources that serve the skill. Do not claim support, security assurance or successful validation without evidence.

For changes, run checks appropriate to the affected files and report what was and was not verified. Do not invent client-specific facts, credentials, dependencies, approvals or tool capabilities.

Use Mermaid for diagrams across the repository. Keep diagram source in fenced `mermaid` blocks in Markdown where practical, and keep accompanying text understandable when diagrams cannot be rendered.
