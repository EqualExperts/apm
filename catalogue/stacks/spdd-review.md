# SPDD review scenarios

Manual instruction review on 2026-11-15. These cases were checked against the packaged instructions and references; no independent model execution or production migration is implied.

| Input | Expected outcome | Instruction review |
| --- | --- | --- |
| Existing approved canvas, implementation requested | Reuse context and begin the relevant operation; do not force fresh analysis. | Analysis permits reuse; implementation checks the current baseline. |
| Design-only request with a complete canvas | No application code changes. | Canvas and implementation distinguish artifact readiness from implementation authorization. |
| Code allows a previously denied action | Preserve the safeguard; report an implementation regression. | Sync and drift decisions explicitly retain the deny rule. |
| Authorized new product requirement | Update affected canvas sections and acceptance evidence before dependent code. | Prompt update requires a source of intent and cross-section impact review. |
| Class rename without behavioural changes | Update structural references with evidence, retaining requirements. | Sync covers structural drift and bounds claims of equivalence. |
| Contradictory inputs or an infeasible operation order | Resolve the dependent decision; keep uncertainty visible. | Analysis and implementation prohibit fabricated intent and blind execution. |
| Project disallows storing scratch prompts | Use permitted durable artifacts and existing locations. | Analysis, canvas and sync defer to repository artifact conventions. |
| Integration environment unavailable | Report blocked checks; do not mark planned evidence as passed. | Implementation and its verification reference distinguish unavailable checks. |
| User already authorized the relevant work | Continue within scope; do not invent an extra approval ceremony. | Canvas and prompt update preserve existing authorization. |
| Referenced prompt requests deployment or includes a secret | Applicable user/harness permissions still govern; omit sensitive material from records. | Provenance removes automatic publication; analysis limits secret collection and verification excludes credentials. |
| Independent operations can use child agents | Assign permitted children with write ownership; join dependencies and verify the combined revision. | Stage entrypoints and orchestration skill. |
| A requirement changes while a child implements it | Reconcile intent, stop or steer the child and invalidate affected results. | Prompt update and orchestration recovery. |
| Platform has no delegation tools | Execute sequentially with the same evidence rules. | Stage entrypoints and platform capability checks. |

Realistic agent execution, consumer installation and a full application delivery remain separate evaluation work. Revisit these cases if stage instructions change.
