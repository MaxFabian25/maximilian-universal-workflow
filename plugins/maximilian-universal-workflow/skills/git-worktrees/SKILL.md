---
name: git-worktrees
description: Use when repo work needs an isolated git worktree, a new branch plus filesystem workspace, or branch safety before execution.
---

# Git Worktrees

Create an isolated branch workspace before write-owning execution.

## Read

Follow `../../docs/workflow-contracts/README.md` and `references/worktree-playbook.md`.

## Do

- Confirm repo root, current branch, status, remotes, applicable `AGENTS.md`, and the planned execution objective.
- Use this before execution when substantial mutation should not happen on the current branch or the user has not approved current-branch execution.
- Choose location by priority: existing `.worktrees/`, existing `worktrees/`, AGENTS.md rule, then root-thread `request_user_input`.
- Verify project-local worktree directories are ignored before creating a worktree.
- Name the branch from the plan outcome using repo conventions; avoid overwriting existing branches or worktrees.
- Create the worktree with `git worktree add` and switch execution context to the new path.
- Run repo-appropriate setup and baseline verification in the worktree.
- Use `request_user_input` for branch/location choices, dirty-state decisions, baseline failure disposition, and destructive cleanup.
- Update the shared phase bundle with worktree path, branch, baseline evidence, allowed side effects, artifact state, and next execution prompt.

## Stop

Stop when repo state is dirty outside the intended scope, branch naming conflicts, location policy is unclear, ignore protection is missing, baseline fails without a user decision, or creating the worktree requires destructive cleanup.
