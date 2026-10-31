# Marketplace provider scope

Equal Experts APM is a marketplace provider: a "fancy text file provider". It publishes reusable agent-facing content for consultants to discover and use in their own projects. Root `marketplace.json` is the marketplace entry point. The maintainer has previously tested marketplace registration; this records that context rather than claiming a fresh installation check.

This repository is not an APM consumer. A root `apm.yml`, consumer lockfile, installed dependency tree and compiled harness configuration are not prerequisites for its marketplace role. Do not introduce these merely to make the marketplace look like a consumer. Individual packages or isolated verification projects may need configuration appropriate to their own purpose.

## Documentation and templates

Skills supply workflows, references supply supporting knowledge, and assets supply output templates. React, Next.js and other framework guidance fits this model without installing or running those frameworks here.

`llms.txt` is a documentation map containing concise context and annotated links. It can include terminology, but is broader than a glossary. It complements skills by helping agents locate knowledge for their workflows.

- Use `llms.txt` where a larger skill or capability set benefits from a concise index into substantial documentation, following the documentation-discovery approach that the maintainer found useful with WebAwesome. A marketplace-root index is not currently needed or planned.
- For a skill-owned index, use `references/llms.txt` and link to it from `SKILL.md`, explaining when to consult it. Keep the workflow in `SKILL.md`; use the index for concise context and annotated links so agents can select relevant detail on demand. This is a repository authoring convention, not an automatic APM discovery mechanism.
- Small skills should link directly to their supporting references. Do not add an index solely for consistency or duplicate a shared documentation set across multiple skills; link to its maintained index instead.
- A skill's `references/` directory identifies authoritative framework documentation and upstream `llms.txt` indexes where available, and explains when to consult them. Keep framework facts separate from agreed EE conventions.
- A skill's `assets/` directory holds templates used to produce output. Worked examples belong in `references/`, following the skill standard.
- Prefer links to maintained upstream documentation over copying entire documentation libraries. Record relevant versions or revisions where reproducibility matters.

The marketplace distributes content; consuming agents read and apply it. An index does not automatically install dependencies or guarantee that every linked page is loaded. This describes the content model, not missing functionality in the provider.

## Review boundaries

Review marketplace entries, referenced paths, content quality, provenance, documentation links and relevant package behaviour. Verify consumer installation in an isolated consumer project when needed for a change. Report structural checks, registration, installation and behavioural checks separately. Additional tooling and CI can improve maintenance; their absence alone does not make this provider an incomplete consumer setup.
