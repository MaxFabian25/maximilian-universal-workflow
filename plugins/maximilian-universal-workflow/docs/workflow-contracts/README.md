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
- `artifact-floor.md` defines supporting artifact requirements.

## Rules

- Git: confirm repo, branch, status, and instructions before mutation. If repo mechanics are missing, establish a repo/worktree or stop.
- Runtime config: keep `default_mode_request_user_input`, `goals`, `remote_plugin`, `mentions_v2`, `child_agents_md`, and `features.multi_agent_v2.enabled` enabled for this plugin.
- Phase loop: a general plugin invocation starts at `intake` and continues through later phases as far as evidence, approval, permissions, and safety allow.
- Goal-backed planning: `planning` outputs the plan first, then a single next prompt that starts with `/goal <execution objective>` and invokes `maximilian-universal-workflow:execution`. `goals = true` is expected; when native goal tools are available and user intent is clear, `planning` may create the goal after the plan is complete.
- User choices: call root-thread `request_user_input` liberally for material ambiguity, branch choices, approval, ownership, and closeout. Do not replace choice collection with a plain-text prompt.
- Subagents: encourage `explorer` read-only fanout and `worker` isolated ownership whenever useful; use `fork_turns: "none"`. Parents collect boundedly and close stuck leaves; leaves return results or `decision_needed`.
- MultiAgentV2: use `multi-agent-v2` when task-path coordination, result collection, stalled agents, recovery, or diagnostics are the primary task.
- Artifacts: `workflow-artifacts/` supports evidence and handoff. Source, tests, docs, branches, commits, and PRs are primary.
