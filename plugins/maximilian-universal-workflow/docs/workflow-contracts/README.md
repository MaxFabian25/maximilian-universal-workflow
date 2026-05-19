# Workflow Contracts

Human-facing authority for Maximilian Universal Workflow.

## Authority Order

1. System, developer, user, workspace instructions, and deeper `AGENTS.md`.
2. Active task packets and explicit decisions.
3. These workflow contracts.
4. Skill bodies and per-skill references.
5. Default assistant behavior.

## Files

- `harness-boundary.md` defines the repo-universal plugin boundary.
- `lifecycle-playbook.md` defines the phase order and ownership.
- `native-tool-map.md` defines phase-to-native-tool mapping.
- `phase-runtime.md` defines per-phase tools, evidence, exits, and next phases.
- `artifact-floor.md` defines supporting artifact requirements.

## Rules

- Git: confirm repo, branch, status, and instructions before mutation. If repo mechanics are missing, establish a repo/worktree or stop.
- Goal planning: output `/goal ...` plus the later execution invocation; do not claim the command ran. `goals = true` is expected; when unavailable, output the same objective bundle without claiming `/goal` execution.
- Subagents: encourage `explorer` read-only fanout and `worker` isolated ownership whenever useful; use `fork_turns: "none"`. Parents collect boundedly and close stuck leaves; leaves return results or `decision_needed`.
- MultiAgentV2: use `multi-agent-v2` when task-path coordination, result collection, stalled agents, recovery, or diagnostics are the primary task.
- Artifacts: `workflow-artifacts/` supports evidence and handoff. Source, tests, docs, branches, commits, and PRs are primary.
