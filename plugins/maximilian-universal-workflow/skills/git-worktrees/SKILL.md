---
name: git-worktrees
description: Use when planning must choose current-branch approval or isolated git worktree setup before execution.
---

# Git Worktrees

Resolve branch safety before write-owning execution.

## Read

Read `../../docs/workflow-contracts/phase-runtime.md`, `../../docs/workflow-contracts/phase-transition.md`, `../../docs/workflow-contracts/phase-bundle.md`, `../../docs/workflow-contracts/native-tool-map.md`, and `references/worktree-playbook.md`. Read `../../docs/workflow-contracts/README.md` only for authority/setup.

## Do

- Confirm repo root, current branch, status, remotes, applicable `AGENTS.md`, and the planned execution objective.
- Use this after planning and before every write-owning execution handoff.
- Record `worktree_state.mode: current-branch` when current-branch execution is explicitly approved and no mandatory isolation trigger applies.
- Create an isolated worktree when `references/worktree-playbook.md` records `worktree-needed`.
- Use root-thread `request_user_input` when `references/worktree-playbook.md` records `decision-needed`.
- Choose location by priority: existing `.worktrees/`, existing `worktrees/`, AGENTS.md rule, then root-thread `request_user_input`.
- Verify the selected project-local worktree directory is ignored before creating a worktree.
- Name the branch from the plan outcome using repo conventions; avoid overwriting existing branches or worktrees.
- Create the worktree with `git worktree add` and switch execution context to the new path.
- Run repo-appropriate setup and baseline verification in the worktree.
- Use `request_user_input` for branch/location choices, dirty-state decisions, baseline failure disposition, and destructive cleanup only when 2-3 concrete options remain.
- Update the shared phase bundle with worktree path, branch, baseline evidence, allowed side effects, artifact state, and next execution prompt.

## Stop

Stop when repo state is dirty outside the intended scope, branch naming conflicts, location policy is unclear, ignore protection is missing, baseline fails without a user decision, or creating the worktree requires destructive cleanup.
