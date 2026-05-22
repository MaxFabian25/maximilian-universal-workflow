# Handoff Checklist

Report: outcome delivered, acceptance criteria status, repo path, worktree path when used, branch/base, phase, changed files/artifacts, verification, review resolution, decisions, residual risks, stop condition, next action, owner.

Use this final shape:

```text
Status: <done/blocked/needs decision>
Outcome delivered: <repo end state>
Acceptance criteria: <met/unmet/unverified with evidence>
Evidence: <commands, review, changed paths, artifacts>
Risks: <remaining risks or none>
Unverified gaps: <none or specific gaps>
Next owner: <user/agent/team>
Recommended closeout: <stop with evidence/keep branch/create PR>
```

First closeout prompt is non-destructive: stop with evidence, keep branch, or create PR. Merge, push, discard, delete, or destructive cleanup requires a second explicit user request and confirmation.
