---
name: multi-agent-v2
description: "Use when coordinating MultiAgentV2 task paths, row-manifest fanout, result collection, stalled agents, recovery, or spawn_agent/list_agents/followup_task/close_agent debugging."
---

# Multi-Agent V2

## Rule

Treat MultiAgentV2 as task-path coordination, not a result queue. `wait_agent` reports mailbox activity or timeout; `list_agents` collects results. Read `references/contract.md` for the full operational contract and `references/source-notes.md` only for source-backed diagnostics.

## Role Boundary

Before using `wait_agent`, `list_agents`, `followup_task`, or `close_agent`, decide whether you are the orchestrator for agents you spawned. If you are any spawned agent and the task did not explicitly assign descendant orchestration, you are a leaf: do not wait for siblings, collect sibling results, or close agents. A child that intentionally spawns descendants may coordinate only those descendants.

## Delegate

Spawn subagents when they improve speed, breadth, critique, or isolation enough to justify coordination cost. Default to no subagents for narrow single-thread work and 1-3 subagents for ordinary fanout. Exceed 3 only when the task naturally partitions and the parent can synthesize bounded summaries. Use multiple agents for independent questions, disjoint edit scopes, or independent row-manifest work; spawn bounded `spawn_agent` packets directly and keep structured result collection in the parent. For edits, assign ownership and tell workers not to revert others' changes.

## Spawn

Use stable lowercase snake_case `task_name`, prefer `fork_turns: "none"` for self-contained packets, leave model/reasoning overrides unset unless explicitly needed, and make prompts self-contained.

## Collect

Track returned task names, use `path_prefix` where useful, and inspect completed text in `list_agents` target `agent_status`. `send_message` queues only; `followup_task` triggers a non-root turn. On timeout, avoid blind loops.

## Recover

Recover by checking required fields, `fork_turns`, full-history override limits, and target paths. For unusable completion, send one evidence-focused `followup_task`; if it fails again, close and continue with partial evidence.

## Close

Close finished, unusable, or abandoned agents. Use `previous_status` as a last chance to capture text. Do not close `/root`.
