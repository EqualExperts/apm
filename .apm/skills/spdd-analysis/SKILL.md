---
name: "spdd-analysis"
description: "Analyse requirements against an existing codebase for Structured Prompt-Driven Development (SPDD), producing grounded domain context, options and risks before a REASONS canvas. Use for SPDD discovery and analysis, not implementation or routine debugging."
---

# SPDD analysis

Read [provenance and adaptation boundaries](references/provenance.md). Establish the requested outcome, available requirement sources, repository instructions and existing decisions. Reuse applicable analysis; do not restart an agreed workstream merely to fill a template.

Inspect build metadata and the repository layout, then search for the domain concepts, behaviours and interfaces named in the requirement. Follow relevant dependencies far enough to explain the change and record uninspected boundaries. Avoid collecting unrelated source or secret-bearing configuration.

Separate observed behaviour with source paths from proposed requirements, inferred intent and unanswered questions. Describe domain vocabulary, affected contracts, feasible approaches, trade-offs and material risks. If inputs contradict one another, record the conflict and resolve decisions needed for the next stage; do not fabricate missing business rules.

Produce analysis using [the analysis record](assets/analysis-record.md), adapted to the project's document layout. Split oversized work into independently verifiable outcomes where useful. Keep implementation detail proportional to the decision; analysis does not authorize code changes.

Report the analysis artifact, evidence inspected, recommended direction and unresolved decisions. Hand the resulting context to canvas creation when requested; no other skill or upstream CLI installation is required to use this stage.

For supported runtimes, use parent/child agents to explore independent domain areas or contracts in parallel when delegation is permitted. Give children read-only scopes and an input revision; the parent reconciles findings and contradictions into one analysis before dependent canvas work. Use parallel-stage-orchestration if installed for the scheduling contract, or apply these rules sequentially when delegation is unavailable.
