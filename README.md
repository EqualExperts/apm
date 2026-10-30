# APM

APM is Equal Experts' shared catalogue of agent capabilities. It helps consultants find and use reusable guidance and tooling across languages, clients, platforms and products, and contribute improvements back from their work.

## Get started with APM

### macOS · Homebrew

```bash
brew install apm
```

### Linux and macOS · without Homebrew

```sh
curl -sSL https://aka.ms/apm-unix | sh
```

### Windows · PowerShell

```powershell
irm https://aka.ms/apm-windows | iex
```

### Add a marketplace

After installing the CLI, use the following command to register the Equal Experts marketplace once its marketplace manifest is published:

```text
apm marketplace add EqualExperts/apm
```

Adding a marketplace makes its packages available for discovery; it does not install them.

For multiple GitHub accounts, you can use the active `gh` CLI account or set `GITHUB_APM_PAT_EQUALEXPERTS` to a token for the EqualExperts organisation. The account or token must have access to the repository and any required organisation authorisation.

When you install a package, APM can detect the project's assistant. To select one explicitly, use `--target codex`, `--target claude`, or `--target copilot` with `apm install`. If no assistant is detected, select a target explicitly.

## Start here

- [Repository guidance](AGENTS.md) defines how agents work in this repository.
- [Principles](docs/PRINCIPLES.md) describe the catalogue and its boundaries.
- [Skill standard](docs/SKILL_STANDARD.md) defines the structure and requirements for skills.
- [Primitive authoring](docs/PRIMITIVES.md) covers prompts, instructions and agents.
- [Catalogue design](docs/CATALOGUE.md) describes tiers, technology stacks and planned APM functionality.
- [Contributing](CONTRIBUTING.md) describes the fork and review workflow.
- [Releases and support](docs/RELEASES.md) describe release and adoption expectations.
- [Security](SECURITY.md) describes how to handle sensitive security findings.
- [Catalogue](skills/README.md) describes where skills belong.

The repository is at its foundation stage. Initial creator and validator skills are available; the installer and catalogue tooling are planned. Cross-harness support has not yet been verified.

## Repository structure

```text
.github/                 Issue and pull request templates
.apm/                    APM package primitives
  skills/                Package skills
  prompts/               Prompts and slash commands
  instructions/          Persistent instructions
  agents/                Agent definitions
  hooks/                 Runtime hook definitions
AGENTS.md                Guidance for agents working in this repository
docs/                    Principles, skill standard, catalogue and release guidance
skills/
  .system/               System classification guidance
  .curated/              Curated classification guidance
  .experimental/         Experimental classification guidance
catalogue/
  skills/                Planned skill discovery records
  stacks/                Planned named collections of skill references
```

Skill tiers describe how APM organises its catalogue; they do not automatically install or activate skills in a harness. Catalogue records and stacks will classify skills across technologies without duplicating them. Initial creator and validator skills are present; catalogue tooling remains planned. See the [catalogue design](docs/CATALOGUE.md) for details.

The `.apm/` directories follow Microsoft's [primitive authoring layout](https://microsoft.github.io/apm/producer/author-primitives/). Commands are authored as prompts; MCP servers are declared in a package's `apm.yml`, not a separate `.apm/` directory. The creator and validator skills live in `.apm/skills/`; the remaining primitive directories are empty. These directories alone do not make a package installable.

## Propose a contribution with AI

If you have an idea or a defect to report and would like maintainers to carry out the work, use the AI-prepared contribution issue form:

1. Ask your AI assistant to help research and draft the proposal. Describe the problem and intended users, scope and acceptance criteria, relevant evidence and existing capabilities, and any suggested approach or compatibility considerations. For a defect, include reproduction steps and expected and actual behaviour.
2. Review the draft for accuracy. Identify what you verified, any assumptions and open questions, and distinguish evidence from AI-generated suggestions. Do not include credentials, personal data, client-confidential information or material you cannot share.
3. In this repository on GitHub, open **Issues**, select **New issue**, and choose **AI-prepared contribution**. Complete the form using your reviewed draft, then submit it. You can also [open the issue form directly](../../issues/new?template=ai-prepared-contribution.yml).
4. Maintainers will assess the issue, ask for further information if needed, and decide how to address it.

You can also contribute changes through a pull request from a fork; see [Contributing](CONTRIBUTING.md) for both routes.
