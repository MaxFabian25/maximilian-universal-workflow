# Workflow Contracts

Human-facing authority for Maximilian Universal Workflow.

## Authority Order

1. System, developer, user, workspace instructions, and deeper `AGENTS.md`.
2. Active task packets and explicit decisions.
3. These workflow contracts.
4. Skill bodies and per-skill references.
5. Default assistant behavior.

## Files

- Repository `.codex/config.toml` defines the required Codex runtime features and agent role mapping.
- `harness-boundary.md` defines the repo-universal plugin boundary.
- `lifecycle-playbook.md` defines the phase order and ownership.
- `native-tool-map.md` defines phase-to-native-tool mapping.
- `phase-runtime.md` defines per-phase tools, evidence, exits, and next phases.
- `phase-transition.md` defines the packet passed between phases.
- `request-user-input.md` defines the root-thread decision prompt shape.
- `artifact-floor.md` defines supporting artifact requirements.

## Rules

- Git: confirm repo, branch, status, and instructions before mutation. If repo mechanics are missing, establish a repo/worktree or stop.
- Runtime config: keep `default_mode_request_user_input`, `goals`, `remote_plugin`, `mentions_v2`, `child_agents_md`, and `features.multi_agent_v2.enabled` enabled for this plugin.
- Phase loop: a general plugin invocation starts at `intake` and continues through later phases as far as evidence, approval, permissions, and safety allow.
- Goal-backed planning: `planning` outputs the plan first, then uses native goal tools. Use `get_goal` to compare current goal state against the planned objective. Use `create_goal` only when no current goal exists and proceed intent is clear. If a different current goal exists, call `request_user_input` for the goal conflict choice.
- Worktree isolation: use `git-worktrees` between planning and execution when substantial mutation should happen away from the current branch or current-branch execution is not approved.
- User choices: call root-thread `request_user_input` liberally for material ambiguity, branch choices, approval, ownership, and closeout. Use `request-user-input.md` for the exact choice shape.
- Subagents: encourage `explorer` read-only fanout and `worker` isolated ownership whenever useful; use `fork_turns: "none"`. Parents collect boundedly and close stuck leaves; leaves return results or `decision_needed`.
- MultiAgentV2: use `multi-agent-v2` when task-path coordination, result collection, stalled agents, recovery, or diagnostics are the primary task.
- Phase transition: every phase hands off with outcome, acceptance criteria, allowed side effects, evidence, current phase result, next phase, open decisions, and artifact status.
- Artifacts: `workflow-artifacts/` supports evidence and handoff. Interactive HTML is the default support artifact for substantial workflow runs. Source, tests, docs, branches, commits, and PRs are primary.
