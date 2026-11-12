---
name: docs-first-delivery
description: Run specification-driven delivery for a new feature, adoption of an existing project, or resumption of a documented workstream. Establish requirements and architecture, validate contracts, plan traceable implementation, and verify delivered behaviour against the specification. Use when the user requests SDD or a docs-first workflow, not for every small edit.
---

# Docs-first delivery

Read [scope and provenance](references/provenance.md). Start from the user's requested outcome and the consuming repository's actual instructions, conventions and current implementation. Identify whether this is adoption, new work or continuation. Keep unknowns explicit; a proposed design is not evidence of existing behaviour.

Use [delivery stages](references/stages.md) in order, reusing current artifacts when they already satisfy a stage. Scale documentation to the change. Record the intended review gates and existing authorization; pause only where a decision or required approval is outstanding. An assistant or harness cannot grant approval. Do not invent a ticket requirement or force a new directory layout.

Establish scope and architecture, then specify contracts and validate the design, then produce an implementable plan with acceptance evidence. Resolve consequential contradictions before dependent implementation. Use Mermaid for useful diagrams and retain understandable text alongside them. Keep implementation within the agreed scope.

Deliver small slices with relevant tests, following the project's test-first practice where applicable. Link each acceptance criterion to implementation and observed verification. Treat security denials, failures, concurrency and data migration as first-class contracts when relevant. Preserve compatibility requirements; destructive cleanup and external deployment need their own authorization.

Maintain a concise continuation record using [the delivery record template](assets/delivery-record.md). Place it where the repository permits durable records, and keep scratch prompts out of version control when required. Record current behaviour, decisions, exact checks and remaining work without secrets or client-sensitive material.

For reusable starting messages, see [prompt usage](references/prompts.md). Before reporting completion, compare the implementation with the agreed specification and inspect current evidence. Report skipped, blocked and unperformed checks separately. A successful build, a green PR and a deployed application are different results.
