# Native Tool Map

`AGENTS.md` and repo instructions outrank this map.

The public repository includes `.codex/config.toml` with the required feature flags and `default`, `explorer`, and `worker` role mappings.

- intake: `git status --short`, branch, `AGENTS.md`, `rg --files`.
- phase loop: when the plugin is invoked generally, start at `intake` and continue through the next phase instead of returning only a route label.
- exploration/review: local reads first; spawn read-only `explorer` leaves with `fork_turns: "none"` whenever fanout improves evidence, critique, or confidence.
- ideation/planning/handoff/cleanup: call root-thread `request_user_input` liberally for material choices, branch selection, approval, ownership, and closeout.
- planning: cite fresh exploration or run it first; name ownership and verification; output a plan plus one next prompt that starts with `/goal <execution objective>` and invokes `maximilian-universal-workflow:execution`; keep the objective under 4,000 characters; put long instructions in the execution prompt body or a repo file.
- goal tools: `get_goal` may inspect state; `create_goal` may create the goal when the plan is complete and the user's intent to proceed is clear; `update_goal` only for proven completion when exposed.
- execution: spawn `worker` freely for isolated ownership; `fork_turns: "none"`; no `fork_context`. Goal bundles are binding context, not implicit create-goal permission.
- multi-agent-v2: use the bundled skill for task-path mechanics, stalled-agent recovery, collection diagnostics, or source-backed MultiAgentV2 contracts.
- verification: parent current-state commands/checklists; child summaries and old output are not proof.
- review: use native whole-worktree review surfaces when available.
- receiving-review: read the full feedback, verify each item against repo evidence, then fix, push back, or escalate with a disposition ledger.

Parent lifecycle: `spawn_agent`, `wait_agent`, `list_agents`, optional one `followup_task`, then `close_agent`. Close stuck children and report partial evidence.

Leaf rule: spawned explorers/workers do not coordinate fanout or wait on siblings unless explicitly assigned descendants. Parent owns choices, synthesis, verification, review arbitration, and handoff.
