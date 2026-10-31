# Catalogue and distribution design

APM separates lifecycle tier from technology classification. Skills live in `.apm/skills/` and have one lifecycle classification; catalogue entries and stacks can describe multiple technologies and workflows without duplicating the skill.

```text
.apm/skills/        Deployable skill directories
skills/              Tier descriptions
catalogue/
  skills/           Skill discovery records
  stacks/           Named selections of skills
```

These paths describe repository organisation, not harness discovery paths. The system classification does not automatically install skills, grant permissions or override other instructions. Names must be unique across skills, including on case-insensitive filesystems. Each skill follows the [skill standard](SKILL_STANDARD.md).

## Tiers

- `.system`: skills that create, validate, discover, install or maintain APM capabilities. APM-specific names should avoid collisions with harness-provided skills.
- `.curated`: skills reviewed for a clear use case, named maintainer, provenance, dependencies, structural compliance and representative verification. Curated status does not guarantee universal compatibility.
- `.experimental`: skills offered for evaluation with their maturity and limitations stated. Promotion to curated requires the same review as a new curated contribution.

## Technology and stacks

A skill can apply to multiple languages, frameworks, platforms, products, databases and workflows. Catalogue records should make these classifications searchable, together with the skill name, tier, path, description, maintainer, dependencies, provenance, maturity, supported environments and evidence for compatibility claims. Define a machine-readable schema and validation with the implementation rather than assuming one exists.

A stack is a named selection of skill references, not another copy of the skills. Its definition should describe its purpose, maintainer, included skills, version or revision constraints, dependencies and compatibility. Present the full selection for review before installation. A stack does not change skill activation or provide permissions.

## APM functionality

The APM skill creator and installer will be based on the OpenAI models, adapted to APM and the supported harnesses. Their implementation should provide:

- Discovery and filtering by capability, technology, tier and compatibility; clear indication of experimental status and installed versions.
- Creation and validation of skills, metadata, references, assets and Python helpers according to APM conventions.
- Installation by skill or stack from an explicit source and revision, including private repositories through existing authorised credentials. Preserve source and revision for later inspection.
- A preview of selected skills, destinations, dependencies and conflicts. Detect duplicate names and existing installations; never silently overwrite local modifications.
- Explicit update and removal operations that identify affected files and protect local changes, with actionable errors and recovery information.
- Harness-specific destination and discovery handling based on verified support. Keep shared skill instructions portable; document prerequisites and differences rather than assuming recursive discovery or automatic installation.
- Validation of catalogue references, stack membership, names, casing, provenance and declared compatibility, alongside meaningful behavioural checks.

The metadata schema, supported harnesses, versioning strategy, installation records and conflict-resolution mechanism remain implementation decisions to define and test. These capabilities are requirements, not claims of existing functionality.

The [catalogue website](PAGES.md) now implements browser search over published marketplace packages and optional named stack selections. Its minimal stack record format is documented there. This is discovery and install-command guidance; managed stack installation, version constraints and broader catalogue metadata remain planned.
