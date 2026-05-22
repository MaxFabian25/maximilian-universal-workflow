# Phase Transition

Use the phase bundle state described by `phase-bundle.md` whenever one phase hands work to the next phase, stops for a decision, or writes a durable support artifact.

## Bundle

The phase bundle is the handoff packet. A phase may report only fields that changed for trivial work, but substantial runs should preserve the complete bundle in the HTML artifact. Do not edit `phase-bundle.md` as live workflow state.

Every phase stop or continuation includes the compact phase footer from `phase-bundle.md`. Treat `continue_now: yes` in that footer as the handoff signal for immediate continuation.

## Transition Checklist

Before a phase hands off, asks, or stops:

- update acceptance criteria status or state why it is still unknown;
- record new evidence, commands, changed paths, and unresolved uncertainty;
- record decisions already made and the next decision gate, if any;
- update artifact state for substantial runs or state why no artifact is needed;
- set `next_phase` to one phase name or `done`;
- set `continue_now` to `yes` only when no material decision gate remains;
- include the phase footer in the response, artifact, or next-phase packet.

If `decision_gate` is not `none`, call `request_user_input` before continuing. If `decision_gate` is `none` and `continue_now` is `yes`, continue immediately into `next_phase`. If `continue_now` is `no`, stop with the current evidence and exact next prompt.

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
