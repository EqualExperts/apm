---
name: "spdd-prompt-update"
description: "Update an existing SPDD REASONS canvas when requirements, design decisions or constraints change, tracing impacts before implementation. Use for intent-to-spec changes, not reverse-engineering code drift or silently changing acceptance criteria to match a failing build."
---

# SPDD prompt update

Read [provenance and adaptation boundaries](references/provenance.md). Identify the current canvas and the requested change from the conversation and repository. Ask for missing inputs only when they cannot be established; a failing test alone is not a requirement change.

Compare the requested intent with the current requirement, design and safeguards. Record the source of the decision, its scope and any unresolved conflicts. Preserve already authorized decisions and actual review requirements; do not manufacture approval or force redundant confirmation.

Trace effects through all seven REASONS sections: Requirements, Entities, Approach, Structure, Operations, Norms and Safeguards. Change only affected material. Preserve stable identifiers and useful rationale; record superseded decisions rather than silently erasing history.

Update acceptance criteria and planned evidence together when the requirement genuinely changes. Check compatibility, migration and security implications against the request. Surface consequential choices beyond the authorized scope before dependent implementation.

Check cross-references and operation dependencies after the edit. Report changed intent, affected implementation/tests and remaining decisions. A documentation-only request ends with the canvas update. Continue implementation only if already authorized; do not regenerate the whole application.

Code-driven structural drift belongs in a comparison against the intended canvas. It must not be reclassified as approved intent merely because the implementation already exists.

On runtimes supporting permitted parent/child execution, independent impact analyses can run in parallel against the same input revision. Children return findings; one parent edits the canonical canvas, reconciles requirements and invalidates affected downstream work. Do not race requirement edits with implementation that depends on them. Use parallel-stage-orchestration if installed; the same stage remains executable sequentially without it.
