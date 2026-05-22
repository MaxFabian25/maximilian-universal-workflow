# Worktree Playbook

Use this playbook to set up a branch plus filesystem workspace for isolated execution.

## Preconditions

- Planning has identified outcome, acceptance criteria, allowed side effects, and execution ownership.
- Repo root, current branch, status, remotes, and applicable `AGENTS.md` are known.

## Isolation Decision

Before execution, record one of:

- `current-branch`: current-branch execution is explicitly approved and no mandatory worktree trigger applies.
- `worktree-needed`: isolation is required by the rules below.
- `decision-needed`: no mandatory trigger applies, but current-branch approval is missing or ambiguous.

Require `worktree-needed` when any of these are true:

- The user, repo instructions, or phase bundle requires isolated execution.
- The current branch is protected, default, release-like, or branch policy is unknown and current-branch mutation is not explicitly approved.
- `git status --short` shows unrelated changes outside the planned ownership scope.
- Execution uses write-owning worker fanout or mutable ownership across multiple independent areas.
- The plan includes destructive cleanup, generated artifacts plus source edits, or other side effects that should remain reviewable away from the source branch.

Use root-thread `request_user_input` for `decision-needed`; offer current branch, isolated worktree, or stop with evidence.

## Location Policy

Choose the worktree parent in this order:

1. Existing `.worktrees/`.
2. Existing `worktrees/`.
3. Worktree location named by `AGENTS.md` or repo docs.
4. Root-thread `request_user_input` with 2-3 concrete locations.

For a project-local parent, confirm the selected parent is ignored before creation:

```bash
git check-ignore -q -- <selected-parent>/
```

Check only the selected parent. When the selected project-local parent is not ignored, use `request_user_input` to choose adding the ignore rule, selecting another location, or stopping.

## Branch And Path

Use the repo's branch naming convention. Otherwise use:

```text
codex/<short-slug>
```

Use a path that combines the selected parent and the branch slug:

```text
<parent>/<short-slug>
```

Before creation, inspect:

```bash
git worktree list --porcelain
git branch --list <branch>
test -e <path>
```

Resolve collisions with `request_user_input`; do not overwrite existing branches, worktrees, or paths.

## Create

Run from the source repo:

```bash
git worktree add <path> -b <branch>
```

Then run all setup and baseline commands from `<path>`.

## Setup And Baseline

Infer setup and baseline commands from repo evidence such as package manifests, lockfiles, Makefiles, task runners, CI config, and AGENTS.md. Use the lightest command that proves the checkout is usable before mutation.

Report command, exit status, and key output lines. If baseline fails, use `request_user_input`:

```text
Header: Baseline
ID: baseline_failure
Question: How should execution proceed with the failing baseline?
Options:
Investigate (Recommended): Stop execution and route to exploration/debugging before mutation.
Proceed Known Red: Continue execution while preserving the failing baseline as explicit risk.
Stop With Evidence: Hand off the worktree, branch, command, and failure evidence.
```

## Output

Return:

- worktree path;
- branch name;
- source repo path;
- baseline command and result;
- setup command and result;
- dirty-state disposition;
- allowed side effects;
- artifact path for substantial runs;
- exact next `maximilian-universal-workflow:execution` prompt.

## Cleanup

Do not delete worktrees, remove branches, prune, or discard changes without root-thread `request_user_input` and explicit destructive-action confirmation.
