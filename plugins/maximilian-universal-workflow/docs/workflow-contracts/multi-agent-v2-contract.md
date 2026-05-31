# MultiAgentV2 Contract

Detailed operating contract for `../../skills/multi-agent-v2/SKILL.md`.

## Rule

Treat MultiAgentV2 as task-path coordination, not a result queue. `wait_agent` reports mailbox activity or timeout; `list_agents` collects results.

## Role Boundary

Before using `wait_agent`, `list_agents`, `followup_task`, or `close_agent`, decide whether you are the orchestrator for agents you spawned. If you are any spawned agent and the task did not explicitly assign descendant orchestration, you are a leaf: do not wait for sibling agents, do not collect sibling results, and do not close agents. Finish your assigned task and return your result to the parent.

If a child intentionally spawns its own descendants, it may coordinate only those descendants. Track the returned task names and ignore unrelated live agents. Do not treat root-spawned siblings as blockers.

## Delegation

Spawn subagents when they improve speed, breadth, critique, or isolation enough to justify coordination cost. Default to no subagents for narrow single-thread work and 1-3 subagents for ordinary fanout. Exceed 3 only when the task naturally partitions and the parent can synthesize bounded summaries. Use multiple agents for independent questions, disjoint edit scopes, or independent row-manifest work. For row manifests, the parent turns rows into bounded self-contained `spawn_agent` packets and keeps structured result collection itself. For edits, assign ownership and tell workers not to revert others' changes.

## Spawn

- Always provide stable lowercase snake_case `task_name`; root spawns become `/root/task_name`, while child spawns join under the child path, such as `/root/parent/task_name`. Use lowercase letters, digits, underscores only. Avoid `/`, `root`, `.`, `..`, uppercase, hyphens.
- Prefer `fork_turns: "none"` for self-contained exploration, source reading, verification, and narrow edits. Use a positive integer string for recent context. Use `all` only for full history; it rejects `agent_type`, `model`, and `reasoning_effort` overrides.
- Leave model/reasoning/service-tier overrides unset unless explicitly needed. Use `agent_type` only for natural roles.
- Make prompts self-contained: task, ownership, expected output, constraints, blockers, evidence.

## Message

Use `send_message` for queue-only updates; it accepts relative or canonical targets and does not trigger a turn. Send child handoffs to the current parent/orchestrator; target `/root` only when `/root` is the immediate orchestrator for that child. Use `followup_task` for a non-root agent's new turn; never target `/root`. Use relative targets only within the current branch and canonical paths across branches.

## Collect

When collecting child state/results after `wait_agent`, call `list_agents`; completed text is in target `agent_status`, never in `wait_agent`. Use `path_prefix` when useful; it accepts relative or canonical prefixes. `wait_agent` can wake for any mailbox update. On timeout, avoid blind loops. If one child sticks, close it and continue with partial evidence rather than waiting for every child. Treat acknowledgement-only, empty, stale, or unrelated completed text as unusable.

## Recover

Recover v2 failures by checking required fields, `fork_turns` values, full-history override limits, and target paths. Resolve missing paths with `list_agents` and canonical targets. For unusable completion, send one evidence-focused `followup_task`; if it shuts down, sticks, or fails again, close and retry fresh only if worthwhile.

## Close

Close finished, unusable, or abandoned agents to preserve concurrency. Use `previous_status` as a last chance to capture text. Do not close `/root`. Minimal flow: spawn with `fork_turns: "none"`, work locally, wait only when blocked, list, inspect, maybe follow up once, close.
