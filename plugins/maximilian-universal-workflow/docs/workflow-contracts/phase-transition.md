# Phase Transition

Use the phase bundle state described by `phase-bundle.md` whenever one phase hands work to the next phase, stops for a decision, or writes a durable support artifact.

## Bundle

The phase bundle is the handoff packet. A phase may report only fields that changed for trivial work, but substantial runs should preserve the complete bundle in the HTML artifact. Do not edit `phase-bundle.md` as live workflow state.

Every phase stop or continuation includes the compact phase footer from `phase-bundle.md`. Treat `continue_now: yes` in that footer as the handoff signal for immediate continuation.

## Decision Precedence

When stopping, asking, and continuing are all plausible, apply this order:

1. Stop only for a hard blocker: missing repo/worktree, unknown governing instructions, unsafe or unapproved side effect, unresolved ownership overlap, unavailable required tool, failed required verification, or a user instruction to stop.
2. Ask with root-thread `request_user_input` for any material user-owned choice with 2-3 concrete options, including choices that affect scope, side effects, ownership, active-goal conflict disposition, verification confidence, review disposition, or closeout.
3. Continue when repo state is known, governing instructions are known, allowed side effects cover the next phase, ownership is non-overlapping, and no material user-owned choice remains.
4. Treat explicit user wording such as planning-only, no-goal, stop-with-evidence, current-branch approved, or worktree required as an already-made decision; record it in the phase bundle instead of asking again.

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
- Continue directly into the next phase when Decision Precedence proves approval, ownership, evidence, and safety are sufficient; workflow invocation is enough continuation and goal setup intent unless the user explicitly asked for planning-only, no-goal, or stop-with-evidence behavior.
- Use `request_user_input` before crossing a material side-effect, scope, ownership, active-goal conflict disposition, verification, review, or closeout decision.
- Apply `artifact-floor.md` for substantial-run artifact requirements and exceptions.
- Trivial single-step work may report the changed bundle fields in the final response without an HTML artifact.

## Pass/Fail Routing

- Intake complete -> exploration.
- Exploration sufficient -> ideation.
- Ideation selected -> planning.
- Planning complete and goal state settled -> git-worktrees.
- Git-worktrees complete with `worktree_state.mode` as `current-branch` or `worktree-ready` -> execution.
- Execution integrated -> verification.
- Verification pass -> review.
- Verification fail -> execution or `request_user_input`.
- Review pass -> handoff.
- Review findings -> execution or `request_user_input`.
- Handoff choice selected -> done, PR, branch continuation, or user-owned next action.

## Auxiliary Routing

- `receiving-review` may interrupt execution, verification, review, or handoff when feedback arrives. After triage, route to execution, verification, review, handoff, or `request_user_input`.
- `repo-context-cleanup` may interrupt any phase when stale repo context blocks reliable work. After cleanup, return to the blocked phase with refreshed evidence.
- `multi-agent-v2` is an auxiliary coordination skill for fanout mechanics, task-path debugging, stalled-agent handling, and collection. Return to the owning phase after coordination evidence is collected.
