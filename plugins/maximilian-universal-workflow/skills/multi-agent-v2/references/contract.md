# MultiAgentV2 Contract

Use this active contract for `multi-agent-v2`. Expanded contract: `../../../docs/workflow-contracts/multi-agent-v2-contract.md`. Diagnostics: `../../../docs/workflow-contracts/multi-agent-v2-source-notes.md`.

## Boundary

Coordinate only agents you spawned. Spawned leaves do not collect sibling state unless assigned descendant orchestration. A child with descendants tracks returned task names and ignores unrelated live agents.

## Spawn

Spawn only when speed, breadth, critique, or isolation justify coordination cost. Default to none for narrow work and 1-3 for ordinary fanout; exceed 3 only for partitioned work with bounded synthesis.

Use lowercase snake_case `task_name`; avoid `/`, `root`, `.`, `..`, uppercase, and hyphens. Prefer `fork_turns: "none"`; use positive integer strings for recent context and `all` only for full history. Do not use `fork_context`. Leave overrides unset unless needed. Prompts include task, ownership, output, constraints, blockers, and evidence.

## Collect

`wait_agent` reports mailbox activity or timeout, never completed text. Collect results with `list_agents`, using `path_prefix` when useful. Completed text is in `agent_status`.

`send_message` queues only. `followup_task` triggers a non-root turn and must not target `/root`. Use relative targets locally and canonical paths across branches.

On timeout, avoid blind loops. Treat acknowledgement-only, empty, stale, or unrelated completion as unusable. Send at most one evidence-focused follow-up, then close and continue with partial evidence.

## Close

Close finished, unusable, or abandoned agents; use `previous_status` as a last chance to capture text. Do not close `/root`.
