# Phase Transition

Use `phase-bundle.md` whenever one phase hands work to the next phase, stops for a decision, or writes a durable support artifact.

## Bundle

The phase bundle is the handoff packet. A phase may report only fields that changed for trivial work, but substantial runs should preserve the complete bundle in the HTML artifact.

## Rules

- Treat acceptance criteria as the thread running through planning, execution, verification, review, and handoff.
- Continue directly into the next phase when the user asked Codex to do the work and the bundle proves approval, ownership, evidence, and safety are sufficient.
- Use `request_user_input` before crossing a material side-effect, scope, ownership, goal, verification, review, or closeout decision.
- For substantial runs, create or update `workflow-artifacts/YYYY-MM-DD-<slug>.html` with the current bundle, decisions, evidence, and next phase.
- Substantial runs include multi-phase work, multi-agent work, goal-backed execution, non-trivial verification, review ledgers, and handoff reports.
- Trivial single-step work may report the changed bundle fields in the final response without an HTML artifact.

## Pass/Fail Routing

- Exploration sufficient -> ideation or planning.
- Ideation selected -> planning.
- Planning complete, goal state settled, and `worktree_state.mode` is `current-branch` -> execution.
- Planning complete and `worktree_state.mode` is `worktree-needed` -> git-worktrees.
- Git worktree ready -> execution.
- Execution integrated -> verification.
- Verification pass -> review.
- Verification fail -> execution or `request_user_input`.
- Review pass -> handoff.
- Review findings -> execution or `request_user_input`.
- Handoff choice selected -> done, PR, branch continuation, or user-owned next action.
