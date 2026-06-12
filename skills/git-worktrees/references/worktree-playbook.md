# Worktree Playbook

Use this compact gate before write-owning execution. Extended contract: `../../../docs/workflow-contracts/worktree-playbook.md`.

## Decide

Record one mode: `current-branch`, `worktree-needed`, or `decision-needed`.

Require `worktree-needed` for isolation requirements, protected/default/release-like or unknown branch policy without explicit approval, unrelated dirty state, write-owning worker fanout, multiple mutable ownership areas, destructive cleanup, or generated artifacts plus source edits.

Resolve `decision-needed` with `request_user_input` when available, offering current branch, isolated worktree, or stop with evidence. Return `decision_needed` only when the tool is unavailable, the parent owns the choice, or sibling synthesis must happen first.

## Create

Choose parent by priority: repo instruction, existing `.worktrees/`, existing `worktrees/`, then root-thread `request_user_input`. For project-local parents, verify ignore protection with `git check-ignore -q -- <parent>/`.

Name branches from repo convention, otherwise `codex/<short-slug>`. Inspect worktrees, branch, and path before creation; never overwrite branches, worktrees, or paths.

Run `git worktree add <path> -b <branch>` from the source repo; run setup and baseline from `<path>`.

## Output

Update the phase bundle with mode, path, branch, source repo, dirty-state disposition, setup/baseline results, allowed side effects, artifact path, and exact execution prompt.

Do not delete worktrees, branches, or changes without root-thread `request_user_input` and explicit destructive confirmation.
