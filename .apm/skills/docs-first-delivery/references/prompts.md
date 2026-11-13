# Prompt usage

The separately installable `sdd-prompts` package contains six starting prompts: adopt, specify, design, plan, deliver and resume. The marketplace SDD Stack selects that prompt pack, this skill, and the existing test-driven-development, systematic-debugging and verification-before-completion skills.

Choose the prompt for the current stage and provide the requested outcome plus the relevant existing artifact paths. Review the files before use. Prompt installation and invocation vary by assistant; the catalogue's commands are installation guidance, not proof that every harness discovers a prompt automatically. A prompt can also be read and used manually.

The prompts are standalone instructions and do not silently activate, install or execute other packages. They preserve existing authorization and repository policy. Delivery does not implicitly include publishing, deployment or data operations.

Verified with APM 0.26.0: Copilot receives six `.github/prompts/*.prompt.md` files. Codex has no native prompt primitive; use this skill and read the prompt files manually. See the [APM target reference](https://microsoft.github.io/apm/producer/author-primitives/prompts/). Other harness installations and behavioural outcomes have not been tested.
