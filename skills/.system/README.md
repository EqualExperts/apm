# APM system skills

This tier contains skills used to create, validate, discover, install and maintain APM capabilities. These support the catalogue and its contributors.

## Available skills

- [apm-skill-creator](../../.apm/skills/apm-skill-creator/SKILL.md) helps create and update APM skills and includes an initializer for new skills.
- [apm-skill-validator](../../.apm/skills/apm-skill-validator/SKILL.md) checks aspects of skill structure and metadata. Its results require manual review and do not establish behavioural correctness or harness compatibility.

Both are initial implementations. An APM installer and further catalogue tooling are planned; see the [catalogue design](../../docs/CATALOGUE.md).

System is a catalogue classification; deployable skills live in `.apm/skills/`. It does not automatically install or activate these skills, give them higher instruction priority, or grant additional permissions. Each skill must follow the [skill standard](../../docs/SKILL_STANDARD.md) and have a name unique across tiers.
