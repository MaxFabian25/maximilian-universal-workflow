# Request User Input

Use root-thread `request_user_input` for material choices. Children return `decision_needed` to the parent with the same fields. Do not emulate the tool with markdown checkboxes or a prose menu.

## Decision Rule

Ask when the answer changes side effects, branch/worktree state, goal state, ownership, verification disposition, review disposition, cleanup, handoff, or the next phase.

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

## Use For

- phase routing when more than one phase is plausible;
- ideation implementation-path selection and branch/worktree approval;
- goal conflict or proceed decisions;
- git worktree location, branch collision, dirty-state, baseline failure, and cleanup decisions;
- worker ownership overlap;
- verification failure disposition;
- review finding disposition;
- cleanup delete/archive/report choices;
- handoff closeout.

## Option Pattern

Use labels that name the action, not the sentiment:

```text
Continue (Recommended): Continue through the next phase with the current evidence and allowed side effects.
Revise Scope: Adjust the outcome, acceptance criteria, or ownership before continuing.
Stop With Evidence: Stop now and hand off the current phase bundle and artifact.
```
