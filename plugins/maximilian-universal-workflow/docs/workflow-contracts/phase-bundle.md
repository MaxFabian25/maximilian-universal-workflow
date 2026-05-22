# Phase Bundle

Use this shared state object when a phase starts, hands off, stops for a decision, or updates a substantial HTML artifact.

The bundle is prose authority, not a hidden schema. Preserve useful fields from prior phases and update only what the current phase can prove.

## Fields

```text
phase: <current phase>
repo_state:
  root: <absolute repo/worktree path>
  branch: <current branch>
  status: <git status summary>
  instructions: <AGENTS.md or repo instruction evidence>
objective: <durable repo end state>
acceptance_criteria:
  - <criterion and proof expectation>
allowed_side_effects:
  - <read/write/external action boundary>
evidence:
  files: <paths and line refs when useful>
  commands: <commands, exit status, key output>
  subagents: <agent task_names and useful summaries>
goal_state:
  active_goal: <none/matching/conflict/created/complete/blocked>
  objective: <active or planned goal objective>
  decision: <request_user_input id or none>
decision_gate:
  needed: <yes/no>
  id: <request_user_input id or none>
  question: <decision question or none>
worktree_state:
  mode: <current-branch/worktree-needed/worktree-ready/not-applicable>
  path: <worktree path or none>
  branch: <worktree branch or none>
subagent_state:
  mode: <none/explorer/worker/mixed>
  ownership: <read-only or non-overlapping mutable ownership>
verification_state:
  status: <not-run/pass/fail/blocked>
  proof: <fresh parent-side commands/checks or gaps>
review_state:
  status: <not-run/pass/findings/blocked>
  findings: <blocking findings or none>
artifact_state:
  path: <workflow-artifacts html path or none>
  updated: <yes/no/not-needed>
next_phase: <phase name or done>
continue_now: <yes/no>
next_prompt: <exact prompt for later continuation or none>
```

## Rules

- Keep `objective` tied to the executed repository end state, not to planning itself.
- Set `continue_now: yes` only when evidence, approval, ownership, and safety are sufficient for the next phase.
- Set `decision_gate.needed: yes` before crossing material scope, side-effect, ownership, goal, worktree, verification, review, or closeout choices.
- Treat `verification_state.proof` as valid only when the parent has fresh current-state evidence.
- Use `artifact_state.path` for substantial runs; the artifact supports evidence and handoff, but repo files, tests, branches, commits, and PRs remain primary.
