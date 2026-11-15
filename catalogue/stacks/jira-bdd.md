# Jira BDD Delivery Stack

An experimental [selection](jira-bdd.json) for delivering selected Jira tickets to verified implementation and a review-ready PR. Stewardship: Equal Experts APM maintainers; individual long-term ownership is unassigned. This workflow is separate from SPDD and does not require a REASONS canvas.

The five selected packages are [Jira BDD Delivery](../../.apm/skills/jira-bdd-delivery/SKILL.md), [Parallel Stage Orchestration](../../.apm/skills/parallel-stage-orchestration/SKILL.md), [test-driven development](../../.apm/skills/test-driven-development/SKILL.md), [systematic debugging](../../.apm/skills/systematic-debugging/SKILL.md) and [verification before completion](../../.apm/skills/verification-before-completion/SKILL.md). Each retains its own provenance and limitations; the three existing supporting skills retain their Superpowers attribution and licence.

On supported, permitted runtimes, one parent coordinates child tasks across independent ticket slices or stages. Children receive fixed inputs and file ownership; dependent stages wait for accepted prerequisites. The parent integrates and validates combined changes, manages checkpoints and owns Jira/PR publication. Unsupported runtimes execute the same workflow sequentially. Consult the [platform capability matrix](../../.apm/skills/parallel-stage-orchestration/references/platforms.md) rather than inferring support from an assistant label.

The agent continues through unmet criteria and actionable failures until the agreed delivery boundary or a concrete blocker. A review-ready PR is distinct from Jira Done, merge or deployment. Automatic ticket event dispatch needs an external runner; this selection installs neither a trigger nor platform agent configuration.

This is a catalogue selection, not a native managed-stack manifest. Pages expands it into five package installation commands and deduplicates packages shared with SPDD. Pin the provider revision for reproducibility. Current checks establish content and catalogue behaviour only; live ticket delivery and execution across platforms remain unverified.
