# Native Tool Map

`AGENTS.md` and repo instructions outrank this map.

The marketplace/source repository root includes `.codex/config.toml` and `.codex/agents/*.toml` with the required feature flags and `default`, `explorer`, and `worker` role mappings. Install or merge them into the active Codex home before relying on this map.

- intake: `git status --short`, branch, `AGENTS.md`, `rg --files`.
- phase loop: when the plugin is invoked generally, start at `intake` and continue through the next phase instead of returning only a route label.
- phase bundle: every phase updates the current phase bundle state described by `phase-bundle.md`; do not edit that contract file as run state. `continue_now: yes` in the phase footer is the native handoff signal for immediate continuation. Use `update_plan` for transient in-turn task status during substantial work; the phase bundle remains the durable handoff state.
- exploration/review: local reads first; spawn read-only `explorer` leaves with `fork_turns: "none"` when independent fanout improves evidence, critique, or confidence enough to justify coordination cost.
- every phase: call `request_user_input` for material decision gates, implementation paths, approval, ownership, blockers, and closeout whenever the tool is available; use `request-user-input.md` for prompt shape; return `decision_needed` only when the tool is unavailable, the parent owns the choice, or sibling synthesis must happen first.
- planning: cite fresh exploration or run it first; name ownership and verification; use native goal tools for default goal-backed setup; hand off through `git-worktrees` before execution.
- goal tools: `get_goal` compares current goal state to the planned or verified objective. This plugin explicitly instructs goal-backed workflow invocations to call `create_goal` when no current goal exists after a decision-complete plan under `../../skills/planning/references/plan-structure.md`; do not infer goals for ordinary non-workflow tasks, and do not require a separate continuation or goal decision unless the user asks for planning-only, no-goal, or stop-with-evidence. Set `token_budget` only when the user explicitly requested a token budget. `update_goal` marks completion only after goal identity matches and verification proves no required work remains; when completing a budgeted goal, report final token usage from the tool result. Use `update_goal(status="blocked")` only after the same blocking condition has repeated for at least three consecutive goal turns, not for pause, budget limits, usage limits, ordinary handoff, hard work, uncertainty, or a blocker that would merely benefit from clarification.
- git-worktrees: record approved current-branch execution or use `git worktree list --porcelain`, `git branch --list`, `git check-ignore`, `git worktree add`, setup commands, and baseline verification; use `request_user_input` only when 2-3 concrete options remain for location, dirty state, collision, baseline failure, or destructive cleanup choices.
- execution: require the `git-worktrees` branch-safety handoff before write-owning mutation; spawn `worker` only for explicitly owned, non-overlapping mutable scope; `fork_turns: "none"`; no `fork_context`. Goal bundles are binding execution context. Missing goal state is a planning/setup gap because default goal-backed planning should have created or preserved native goal state before execution.
- multi-agent-v2: use the bundled skill for task-path mechanics, row-manifest fanout with bounded `spawn_agent` packets, stalled-agent recovery, collection diagnostics, or source-backed MultiAgentV2 contracts.
- verification: parent current-state commands/checklists; child summaries and old output are not proof; complete active goals only after `get_goal` identity check and proof.
- review: use `git status`, `git diff --stat`, `git diff`, changed tests, relevant `rg`, and read-only explorer review packets.
- receiving-review: read the full feedback, verify each item against repo evidence, then fix, push back, or escalate with a disposition ledger.
- handoff: run `git status --short`, inspect branch/upstream and unpushed commits, record `git_closeout_state`, and do not finish as `done` while staging, commit, push, or PR work is pending unless the user explicitly owns that remaining closeout.

Parent lifecycle: `spawn_agent`, `wait_agent`, `list_agents`, optional `send_message` for queue-only context, at most one focused `followup_task`, then `close_agent`. Close stuck children and report partial evidence.

Leaf rule: spawned explorers/workers do not coordinate fanout or wait on siblings unless explicitly assigned descendants. Parent owns choices, synthesis, verification, review arbitration, and handoff.
