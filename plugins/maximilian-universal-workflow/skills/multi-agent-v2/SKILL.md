---
name: multi-agent-v2
description: "Use when coordinating MultiAgentV2 task paths, row-manifest fanout, result collection, stalled agents, recovery, or spawn_agent/list_agents/assign_task/close_agent debugging."
---

# Multi-Agent V2

## Read

Read `references/contract.md`. Read `../../docs/workflow-contracts/multi-agent-v2-source-notes.md` only for source-backed diagnostics.

## Rule

Treat MultiAgentV2 as task-path coordination. `wait_agent` reports mailbox activity or timeout; `list_agents` collects results.

## Role Boundary

Before waiting, listing, following up, or closing, confirm you are coordinating agents you spawned. Spawned leaves do not collect sibling state unless assigned descendant orchestration.

## Delegate

Spawn only when speed, breadth, critique, or isolation justify coordination cost. Default to none for narrow work and 1-3 for ordinary fanout; exceed 3 only for partitioned tasks with bounded synthesis. For edits, assign ownership and forbid reverting others' work.

## Spawn

Use stable lowercase snake_case `task_name`, prefer `fork_turns: "none"`, never use `fork_context`, leave overrides unset unless needed, and make prompts self-contained.

## Collect

Track returned task names, use `path_prefix` where useful, and read completed text from `list_agents` `agent_status`. `send_message` queues; `assign_task` triggers a non-root turn. On timeout, avoid blind loops.

## Recover

Check required fields, `fork_turns`, full-history override limits, and target paths. For unusable completion, send one evidence-focused follow-up, then close and continue with partial evidence.

## Close

Close finished, unusable, or abandoned agents. Use `previous_status` as a last chance. Do not close `/root`.
