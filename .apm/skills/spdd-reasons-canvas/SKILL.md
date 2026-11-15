---
name: "spdd-reasons-canvas"
description: "Create or review a REASONS canvas for Structured Prompt-Driven Development (SPDD), turning requirements and analysis into a maintained implementation specification with acceptance evidence. Use for SPDD canvas design, not code generation or automatic approval."
---

# SPDD REASONS canvas

Read [provenance and adaptation boundaries](references/provenance.md). Read the requested outcome, relevant analysis, existing contracts and repository instructions. Record missing evidence and decisions instead of turning assumptions into agreed requirements.

Use [the canvas template](assets/reasons-canvas.md) to cover Requirements, Entities, Approach, Structure, Operations, Norms and Safeguards. Reuse existing document paths and identifiers. Keep the artifact in a repository-approved location; do not introduce a compulsory ticket format or new documentation tree.

Give acceptance criteria stable identifiers. Describe domain concepts and affected components with source references; label proposed components explicitly. Record the selected approach and meaningful alternatives. Order operations by their dependencies and map them to acceptance checks. Specify public contracts and invariants precisely where they matter, without copying whole implementations into the canvas.

Use the project's actual engineering norms and safeguards. Include failure, authorization, concurrency, compatibility and data-handling constraints where relevant. Use Mermaid when a diagram improves understanding and keep supporting prose usable without rendering.

Check cross-section consistency: operations use the stated entities and components, dependencies are feasible, and each acceptance criterion has planned evidence. Document unknowns, decision owners where known, and actual approval status. A complete-looking canvas is not an approved design or a passing implementation.

Report readiness for the requested next stage. Do not implement merely because a canvas was created; preserve any existing authorization for implementation rather than inventing a new approval gate.

Where parent/child agents are supported and permitted, parallelise independent section proposals or feature canvases with settled inputs. Give children separate output artifacts; one parent owns integration into the canonical canvas and cross-section checks. Implementation for a slice waits for its accepted canvas. Use parallel-stage-orchestration if installed; otherwise retain these ownership rules and a sequential fallback.
