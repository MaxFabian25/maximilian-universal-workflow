# Workflow Contracts

Human-facing authority for Maximilian Universal Workflow.

## Authority Order

1. System, developer, user, workspace instructions, and deeper `AGENTS.md`.
2. Active task packets and explicit decisions.
3. These workflow contracts.
4. Skill bodies and per-skill references.
5. Default assistant behavior.

## Files

- Marketplace/source repository root `.codex/config.toml` defines the required Codex runtime features and agent role mapping; `.codex/agents/*.toml` defines the bundled `default`, `explorer`, and `worker` role instructions.
- `harness-boundary.md` defines the repo-universal plugin boundary.
- `lifecycle-playbook.md` defines the phase order and ownership.
- `multi-agent-v2-source-notes.md` preserves source-backed MultiAgentV2 diagnostics without making them part of the `multi-agent-v2` skill's normal deferred payload.
- `native-tool-map.md` defines phase-to-native-tool mapping.
- `phase-bundle.md` defines the shared handoff state each phase consumes and updates.
- `phase-runtime.md` defines per-phase tools, evidence, exits, and next phases.
- `phase-transition.md` defines the packet passed between phases.
- `request-user-input.md` defines the root-thread decision prompt shape.
- `artifact-floor.md` defines supporting artifact requirements.
- `html-artifact-template.md` defines the default standalone HTML support artifact shape.

## Rules

- Git: confirm repo, branch, status, and instructions before mutation. If repo mechanics are missing, establish a repo/worktree or stop.
- Runtime config: install or merge the source repository `.codex/config.toml` and `.codex/agents/*.toml` into the active Codex home; keep `default_mode_request_user_input`, `goals`, `remote_plugin`, `mentions_v2`, `child_agents_md`, and `features.multi_agent_v2.enabled` enabled for this plugin.
- Phase loop: a general plugin invocation starts at `intake` and continues through later phases as far as evidence, approval, permissions, and safety allow.
- Goal-backed planning: `planning` outputs the plan first, then uses native goal tools by default. Use `get_goal` to compare current goal state against the planned objective. If a different current goal exists, call `request_user_input` for the goal conflict choice. When no current goal exists, `create_goal` creates the default goal after the plan is decision-complete. Normal workflow invocations use goal-backed setup unless the user explicitly asks for planning-only, no-goal, or stop-with-evidence behavior.
- Branch safety: use `git-worktrees` between planning and execution to record current-branch approval or prepare an isolated worktree before write-owning mutation.
- Narrower skills: use domain-specific skills, tools, or repo-local processes for their specialized procedure while this workflow owns repo lifecycle, evidence, decision, worktree, goal, review, and handoff mechanics.
- User choices: call root-thread `request_user_input` when there are 2-3 concrete paths and the choice affects scope, side effects, ownership, active-goal conflict disposition, verification, review, or closeout. Use `request-user-input.md` for the exact choice shape.
- Subagents: use `explorer` read-only fanout and `worker` isolated ownership when the work is independent, bounded, and improves confidence, speed, critique, or isolation. Use `fork_turns: "none"`. Parents collect boundedly and close stuck leaves; leaves return results or `decision_needed`.
- MultiAgentV2: use `multi-agent-v2` when task-path coordination, result collection, stalled agents, recovery, or diagnostics are the primary task.
- Phase transition: every phase consumes and updates the shared `phase-bundle.md` state, then routes through `phase-transition.md`.
- Artifacts: follow `artifact-floor.md` for requirements and exceptions, and `html-artifact-template.md` for HTML shape. Source, tests, docs, branches, commits, and PRs are primary.
