# Request User Input

Use `request_user_input` for material choices whenever the tool is available to the running agent. Return a `decision_needed` payload only when `request_user_input` is unavailable or the active workflow phase cannot own the choice. Do not emulate the tool with markdown checkboxes or a prose menu.

## Decision Rule

Ask when the answer changes side effects, branch/worktree state, active-goal conflict disposition, ownership, verification disposition, review disposition, cleanup, handoff, or the next phase.

Continue without asking only when approval, acceptance criteria, ownership, tool permissions, and next phase are already clear from the user request or local evidence.

Do not ask for low-risk implementation details when repository convention, tests, or the approved plan already decide the answer.

## Shape

```text
Header: <= 12 characters
ID: stable snake_case
Question: one sentence
Options: 2-3 mutually exclusive choices
Recommended: first option label ends with "(Recommended)"
Descriptions: one short sentence each explaining impact or tradeoff
```

## Decision Payload

When `request_user_input` cannot be called in the current phase, return this payload to the owning workflow:

```text
decision_needed:
  header: <12 chars or fewer>
  id: <stable snake_case>
  question: <one sentence>
  options:
    - <label ending with "(Recommended)">: <impact/tradeoff>
    - <label>: <impact/tradeoff>
    - <optional label>: <impact/tradeoff>
  recommended_option: <label>
  evidence: <files, commands, or uncertainty proving why the decision is needed>
  blocking_phase: <phase or task name>
```

The owning workflow converts this payload into `request_user_input` when the decision is still needed after synthesis.

## Use For

- phase routing when more than one phase is plausible;
- ideation implementation-path selection and branch/worktree approval;
- active-goal conflicts or explicit planning-only/no-goal/stop-with-evidence decisions;
- git worktree location, branch collision, dirty-state, baseline failure, and cleanup decisions;
- ownership overlap;
- verification failure disposition;
- review finding disposition;
- cleanup delete/archive/report choices;
- handoff closeout.

## Prompt Registry

| ID | Header | When | Recommended Option |
| --- | --- | --- | --- |
| `phase_route` | Phase | intake has multiple plausible phases after read-only state | Continue With <phase> (Recommended) |
| `ideation_direction` | Direction | ideation has 2-3 viable repo-grounded implementation paths | Select <direction> (Recommended) |
| `decision_interrogation` | Decision | a material choice cannot be settled from repo evidence | Select <decision> (Recommended) |
| `active_goal_conflict` | Goal | an active goal conflicts with the planned or verified objective | Keep Current Goal (Recommended) |
| `planning_disposition` | Plan | explicit planning-only/no-goal/stop-with-evidence or worktree side-effect choice remains after planning | Continue To Worktree (Recommended) |
| `work_item_granularity` | Work Items | work can be shaped as one task, vertical slices, or a separate brief | Use Vertical Slices (Recommended) |
| `work_item_destination` | Destination | shaped work needs a repo, tracker, PR, handoff, or user-owned destination | Keep In Repo (Recommended) |
| `worktree_location` | Worktree | branch or worktree isolation has 2-3 safe locations | Create Worktree (Recommended) |
| `dirty_state` | Dirty State | uncommitted changes affect planned mutation | Preserve And Isolate (Recommended) |
| `baseline_failure` | Baseline | baseline setup/check fails before mutation | Stop With Evidence (Recommended) |
| `ownership_overlap` | Ownership | mutable scopes overlap | Integrate Locally (Recommended) |
| `verification_failure` | Verify | proof fails and fix/risk/stop choices remain | Fix Failures (Recommended) |
| `review_finding` | Review | findings require fix/accept/defer decision | Fix Findings (Recommended) |
| `cleanup_choice` | Cleanup | generated branches, worktrees, or workflow support evidence can be removed or archived | Keep Evidence (Recommended) |
| `handoff_closeout` | Handoff | stop, continue, branch, PR, or cleanup closeout remains | Stop With Evidence (Recommended) |

## Option Pattern

Use labels that name the action, not the sentiment:

```text
Continue (Recommended): Continue through the next phase with the current evidence and allowed side effects.
Revise Scope: Adjust the outcome, acceptance criteria, or ownership before continuing.
Stop With Evidence: Stop now and hand off the current phase bundle and support evidence.
```

Fallback `decision_needed` payloads must use the Decision Payload shape above.
