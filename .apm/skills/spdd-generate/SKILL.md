---
name: "spdd-generate"
description: "Implement an existing SPDD REASONS canvas in small verifiable slices, preserving its requirements, safeguards and acceptance traceability. Use when implementation from a canvas is requested, not for writing a specification or treating a design-only request as permission to code."
---

# SPDD implementation

Read [provenance and adaptation boundaries](references/provenance.md) and [verification decisions](references/verification.md). Locate the current canvas, applicable repository instructions and implementation baseline. Confirm that the user has requested implementation and that required decisions are resolved; a file named approved is not authorization by itself.

Compare canvas assumptions with relevant code and tests before edits. Follow the operations' dependency order, using small reviewable slices. If the order is infeasible or the design contradicts the repository, explain the affected dependency and revise the plan within the authorized scope rather than blindly following it.

Implement the agreed contracts and safeguards using established project patterns. Apply test-first development where appropriate and run focused checks after each meaningful slice. Preserve unrelated work. Do not regenerate entire modules or add capabilities absent from the requested outcome.

Distinguish implementation defects from specification defects. If the implementation violates a valid criterion, fix the code and retain the criterion. If the intended requirement changes, reconcile the canvas first, then update affected implementation and tests. Never weaken a safeguard or rewrite an expected result solely to obtain green tests.

Maintain a trace from acceptance criteria to changed files and observed test evidence. Record commands, outcomes, skipped checks and pre-existing failures. Keep canvas and code changes together for review; commit, publish and deploy only within the user's actual authorization.

Report completion only to the level demonstrated: compilation, tests, integration, packaging and deployed behaviour are separate evidence. Leave unresolved criteria visible. The existing testing, debugging and verification skills can support this work when available; this stage is usable independently.

Where the runtime supports and permits delegation, the parent may assign ready independent operations to child agents in parallel. Give each child criterion IDs, accepted input revisions and disjoint files or verified isolated worktrees. Hold dependent operations for accepted prerequisites, reserve shared files for one writer, inspect returned evidence and retest the integrated revision. Keep publication with the parent and invalidate results affected by changed inputs. Use parallel-stage-orchestration if installed; otherwise use these rules with sequential execution when needed.
