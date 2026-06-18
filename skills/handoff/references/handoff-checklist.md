# Handoff Checklist

Report: outcome delivered, acceptance criteria status, repo path, worktree path when used, branch/base, phase, changed paths/support artifacts, information-structure changes, vocabulary/decision capture, shaped work items, proof surfaces, scratch-work disposition, subagent evidence, git closeout state, verification, review resolution, decisions, residual risks, stop condition, next action, owner.

Use this final shape:

```text
Status: <done/blocked/needs decision>
Outcome delivered: <repo end state>
Acceptance criteria: <met/unmet/unverified with evidence>
Evidence: <proof surfaces, commands, review, changed paths, support artifacts>
Information structure: <none or file/folder placement, role, structure, locality changes>
Vocabulary/decisions: <none or new/changed/unresolved terms and decisions>
Work items: <none or briefs/slices/findings/destinations with owner>
Subagents: <none or task/result/proof/integration disposition>
Scratch work: <none/deleted/archived/folded-in/remaining with owner>
Git closeout: <clean/unstaged/staged/unpushed/pr-open/user-owned with branch, upstream, staged paths, untracked paths, unpushed commits, PR URL or gap>
Risks: <remaining risks or none>
Unverified gaps: <none or specific gaps>
Next owner: <user/agent/team>
Recommended closeout: <2-3 relevant options from stop with evidence/keep branch/stage and commit/push or create PR/user-owned remaining git work>
```

Do not report `Status: done` while the repo still has uncommitted changes, staged changes, unpushed commits, or missing PR closeout unless the user explicitly selected a user-owned stop and the handoff names the remaining git work.

First closeout prompt names 2-3 relevant next git actions selected from: stop with evidence, keep branch, stage and commit, push/create PR, or user-owned remaining git work. Stage, commit, merge, push, discard, delete, PR creation, or destructive cleanup requires explicit user approval and current verification.
