# Handoff Checklist

Report: outcome delivered, acceptance criteria status, repo path, worktree path when used, branch/base, phase, changed files/artifacts, git closeout state, verification, review resolution, decisions, residual risks, stop condition, next action, owner.

Use this final shape:

```text
Status: <done/blocked/needs decision>
Outcome delivered: <repo end state>
Acceptance criteria: <met/unmet/unverified with evidence>
Evidence: <commands, review, changed paths, artifacts>
Git closeout: <clean/unstaged/staged/unpushed/pr-open/user-owned with branch, upstream, staged paths, untracked paths, unpushed commits, PR URL or gap>
Risks: <remaining risks or none>
Unverified gaps: <none or specific gaps>
Next owner: <user/agent/team>
Recommended closeout: <stop with evidence/keep branch/create PR>
```

Do not report `Status: done` while the repo still has uncommitted changes, staged changes, unpushed commits, or missing PR closeout unless the user explicitly selected a user-owned stop and the handoff names the remaining git work.

First closeout prompt names the next git action clearly: stop with evidence, keep branch, stage and commit, push/create PR, or user-owned remaining git work. Stage, commit, merge, push, discard, delete, PR creation, or destructive cleanup requires explicit user approval and current verification.
