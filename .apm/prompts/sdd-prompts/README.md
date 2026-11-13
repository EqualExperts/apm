# SDD prompts

Six independent starting prompts: adopt, specify, design, plan, deliver and resume. Provide the requested outcome and relevant specification or delivery-record paths with the selected prompt.

Newly authored for this marketplace on 2026-11-12 from the staged workflow reviewed with the maintainer. No client repository content, operational examples or scripts are copied. Experimental; stewarded by Equal Experts APM maintainers, with individual long-term ownership unassigned. The prompts require only the consuming project's authorized context and existing tools; they do not execute commands automatically.

APM 0.26.0 local installation with target `copilot` deployed all six prompt files under `.github/prompts/`. That verifies packaging, not agent behaviour. [APM prompt documentation](https://microsoft.github.io/apm/producer/author-primitives/prompts/) describes supported targets: Codex has no native prompt/command primitive. Codex users can read these files manually and use the separately installed `docs-first-delivery` skill. Other prompt targets and cross-harness behaviour remain untested.

The marketplace SDD Stack also selects docs-first delivery, test-driven development, systematic debugging and verification before completion. This package remains usable by itself and does not install those dependencies implicitly. Local and hosted checks are recorded in the PR; no production outcome is claimed.
