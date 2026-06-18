---
name: git-worktrees
description: Use when planning must choose current-branch approval or isolated git worktree setup before execution.
---

# Git Worktrees

Resolve branch safety before write-owning execution.

## Read

Read `../../docs/workflow-contracts/phase-core.md` and `references/worktree-playbook.md`. Use other workflow-contract files only when the core or local reference requires deeper authority.

## Do

- Confirm repo root, current branch, status, remotes, applicable `AGENTS.md`, and the planned execution objective.
- Use this after planning and before every write-owning execution handoff.
- Follow `references/worktree-playbook.md` for `current-branch`, `worktree-needed`, and `decision-needed` routing.
- Choose location by priority: repo instruction, existing `.worktrees/`, existing `worktrees/`, then `request_user_input` when available; verify any project-local parent is ignored before creation.
- Name the branch from the plan outcome using repo conventions; avoid overwriting existing branches or worktrees.
- Create the worktree with `git worktree add` and switch execution context to the new path.
- Run repo-appropriate setup and baseline verification in the worktree.
- Use `request_user_input` for branch/location, dirty-state, baseline failure, and destructive cleanup choices when the tool is available and 2-3 concrete options remain; return `decision_needed` only when the tool is unavailable or the active workflow phase cannot own the choice.
- Update the shared phase bundle with worktree path, branch, baseline evidence, allowed side effects, artifact state, and next execution prompt.

## Stop

Stop when dirty state, branch/path conflicts, location policy, ignore protection, baseline failure, or destructive cleanup needs a user decision.
