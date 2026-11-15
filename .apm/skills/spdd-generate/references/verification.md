# Implementation and verification decisions

Treat the canvas as the intended contract, with repository instructions and user scope governing execution. Before implementing, check that referenced files, dependency order and verification tools actually exist. A proposed component need not exist yet, but it must be labelled as proposed.

| Finding | Action |
| --- | --- |
| Valid acceptance criterion fails | Diagnose and correct implementation; retain the intended result. |
| Requirements are contradictory | Identify the conflicting criteria and resolve intent before dependent code. |
| An operation depends on a later operation | Explain and reconcile the dependency order before executing affected steps. |
| Input says design-only | Produce design observations; do not modify application code. |
| Tests require an unavailable service | Report those checks as blocked, with prerequisites; do not count them as passing. |
| Existing work already meets a criterion | Reuse it and record current evidence; avoid rewriting it to match a template. |

For each implemented criterion, prefer checks at the actual boundary: input validation and failure outputs, authorization where applicable, persisted effects, concurrent behaviour or external contracts. Compilation proves only that the compiler accepted the source. Generated tests can share the same misunderstanding as generated code; compare assertions with the agreed criterion and existing independent contracts.

After focused checks, run the relevant project suite and inspect skipped tests. Keep exact commands, environment limitations and outcomes in the canvas's evidence record or the project's linked verification artifact. Do not embed credentials or sensitive output.
