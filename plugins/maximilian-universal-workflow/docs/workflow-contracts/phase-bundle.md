# Phase Bundle

Use this shared state object when a phase starts, hands off, stops for a decision, or updates a substantial HTML artifact.

The bundle is prose authority, not a hidden schema or a run-state file. Preserve useful fields from prior phases and update only what the current phase can prove. Do not edit this contract file as the live bundle for a workflow run.

## Bundle Ownership

The root thread or current orchestrator owns the live phase bundle. Spawned children return evidence, proposed field updates, and `decision_needed` payloads; they do not overwrite the bundle or artifact unless their packet explicitly assigns them an artifact section.

For trivial runs, the live bundle may exist only as the phase footer plus changed fields in the thread, final response, or next-phase packet. For substantial runs, the current HTML artifact stores the complete bundle, while the thread still carries the compact phase footer for routing.

When merging child results, preserve parent-owned decisions, acceptance criteria, allowed side effects, and verification status unless fresh parent-side evidence changes them. Record conflicting child evidence under `evidence.subagents` or `decision_gate` instead of silently choosing a side.

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

## Phase Footer

When a phase stops or continues, emit or update this compact footer in the thread, plan, or artifact:

```text
Phase footer:
phase: <current phase>
next_phase: <phase name or done>
continue_now: <yes/no>
decision_gate: <none or request_user_input id/question>
artifact_state: <path and updated/not-needed>
next_prompt: <exact prompt for later continuation or none>
```

Use the full bundle for substantial artifacts. Use the footer for turn-to-turn routing so the next phase does not depend on rereading a long report.

## Rules

- Keep `objective` tied to the executed repository end state, not to planning itself.
- Every phase stop or continuation includes the phase footer.
- Set `continue_now: yes` only when evidence, approval, ownership, and safety are sufficient for the next phase.
- Set `decision_gate.needed: yes` before crossing material scope, side-effect, ownership, goal, worktree, verification, review, or closeout choices.
- Treat `verification_state.proof` as valid only when the parent has fresh current-state evidence.
- Use `artifact_state.path` for substantial runs under `artifact-floor.md`; the artifact supports evidence and handoff, but repo files, tests, branches, commits, and PRs remain primary.
