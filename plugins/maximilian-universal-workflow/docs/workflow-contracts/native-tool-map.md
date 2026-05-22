# Native Tool Map

`AGENTS.md` and repo instructions outrank this map.

The marketplace/source repository root includes `.codex/config.toml` and `.codex/agents/*.toml` with the required feature flags and `default`, `explorer`, and `worker` role mappings. Install or merge them into the active Codex home before relying on this map.

- intake: `git status --short`, branch, `AGENTS.md`, `rg --files`.
- phase loop: when the plugin is invoked generally, start at `intake` and continue through the next phase instead of returning only a route label.
- phase bundle: every phase updates the current phase bundle state described by `phase-bundle.md`; do not edit that contract file as run state. `continue_now: yes` in the phase footer is the native handoff signal for immediate continuation. Use `update_plan` for transient in-turn task status during substantial work; the phase bundle remains the durable handoff state.
- exploration/review: local reads first; spawn read-only `explorer` leaves with `fork_turns: "none"` when independent fanout improves evidence, critique, or confidence enough to justify coordination cost.
- every phase: call root-thread `request_user_input` for material choices, implementation paths, approval, ownership, blockers, and closeout; use `request-user-input.md` for the prompt shape; children return decision payloads to the parent.
- planning: cite fresh exploration or run it first; name ownership and verification; use native goal tools for goal setup.
- goal tools: `get_goal` compares current goal state to the planned or verified objective; `create_goal` creates the goal only when no current goal exists after a complete plan and clear proceed intent; `update_goal` marks completion only after goal identity matches and verification proves no required work remains. Use `update_goal(status="blocked")` only for a repeated impasse, not for pause, budget limits, or ordinary handoff.
- git-worktrees: use `git worktree list --porcelain`, `git branch --list`, `git check-ignore`, `git worktree add`, setup commands, and baseline verification; use `request_user_input` for location, dirty state, collision, baseline failure, and destructive cleanup choices.
- execution: spawn `worker` only for explicitly owned, non-overlapping mutable scope; `fork_turns: "none"`; no `fork_context`. Goal bundles are binding context, not implicit create-goal permission.
- multi-agent-v2: use the bundled skill for task-path mechanics, stalled-agent recovery, collection diagnostics, or source-backed MultiAgentV2 contracts.
- verification: parent current-state commands/checklists; child summaries and old output are not proof; complete active goals only after `get_goal` identity check and proof.
- review: use `git status`, `git diff --stat`, `git diff`, changed tests, relevant `rg`, and read-only explorer review packets.
- receiving-review: read the full feedback, verify each item against repo evidence, then fix, push back, or escalate with a disposition ledger.

Parent lifecycle: `spawn_agent`, `wait_agent`, `list_agents`, optional `send_message` for queue-only context, at most one focused `followup_task`, then `close_agent`. Close stuck children and report partial evidence.

Leaf rule: spawned explorers/workers do not coordinate fanout or wait on siblings unless explicitly assigned descendants. Parent owns choices, synthesis, verification, review arbitration, and handoff.
