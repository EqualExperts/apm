# Workflow review scenarios

These are manual instruction-review cases, not automated agent evaluations or successful application deliveries.

| Input | Required behaviour | Review result |
| --- | --- | --- |
| Existing project already has approved design and plan | Reuse valid artifacts and begin the next authorized stage. | Skill and stage reference allow reuse; no mandatory restart. |
| User authorizes delivery but a contract contradicts the current design | Identify the contradiction and resolve the product decision before dependent work. | Stage reference prevents silently rewriting acceptance criteria. |
| Local tests pass, CI is pending and deployment was not requested | Report local evidence only; leave CI and deployment unverified. | Skill and deliver prompt distinguish those outcomes. |
| Repository prohibits committing scratch prompts | Keep only allowed durable records in the repository. | Skill and resume prompt defer to repository record conventions. |
| An acceptance test fails | Investigate; preserve the criterion unless an authorized requirement change is established. | Deliver prompt and stage reference prohibit weakening criteria to fit results. |
| Existing API compatibility is required | Plan a compatible change or request a scope decision. | Skill preserves compatibility; no universal forward-only deletion rule. |
| No ticket or organization rules submodule exists | Follow actual repository requirements without inventing either. | Skill does not impose source-project infrastructure. |

All seven cases were inspected against the packaged text on 2026-11-12. Independent model execution and cross-harness behavioural evaluation remain unperformed.
