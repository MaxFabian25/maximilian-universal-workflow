# Workflow Contracts

Human-facing authority for Maximilian Universal Workflow.

## Authority Order

1. System, developer, user, workspace instructions, and deeper `AGENTS.md`.
2. Active task packets and explicit decisions.
3. These workflow contracts.
4. Skill bodies and per-skill references.
5. Default assistant behavior.

## Files

- `harness-boundary.md` defines the repo-universal plugin boundary.
- `evidence-discipline.md` defines cross-domain evidence, feedback-loop, scratch-work, subagent, review, and completion gates.
- `proof-first-change.md` defines the proof surface required before material repo mutation.
- `diagnosis-loop.md` defines the loop for bugs, failed checks, bad outputs, disputed claims, and other unexpected results.
- `information-structure.md` defines folder, file, file role, placement, structure, locality, structural depth, and structure improvement guidance.
- `decision-interrogation.md` defines how material choices are grounded, asked, and preserved.
- `vocabulary-decision-capture.md` defines durable terminology and decision capture.
- `question-first-scratch-work.md` defines temporary scripts, prototypes, notes, and generated outputs that answer named questions.
- `work-item-shaping.md` defines behavior-first work items, vertical slices, and destination choices.
- `replacement-coverage-map.md` records how this plugin replaces reusable value from Superpowers and Codex Real Engineering Skills.
- `lifecycle-playbook.md` defines the phase order and ownership.
- `native-tool-map.md` defines phase-to-native-tool mapping.
- `phase-core.md` defines the compact active contract phase skills read before escalating to detailed contracts.
- `phase-bundle.md` defines the shared handoff state each phase consumes and updates.
- `plan-structure.md` defines the expanded goal-backed planning payload and native goal gates.
- `phase-runtime.md` defines per-phase tools, evidence, exits, and next phases.
- `phase-transition.md` defines the packet passed between phases.
- `request-user-input.md` defines the root-thread decision prompt shape.
- `worktree-playbook.md` defines the expanded branch and filesystem isolation contract.
- `artifact-floor.md` defines supporting artifact requirements.
- `html-artifact-template.md` defines the default standalone HTML support artifact shape.

## Rules

- Git: confirm repo, branch, status, and instructions before mutation. If repo mechanics are missing, establish a repo/worktree or stop.
- Environment: the user's Codex environment owns native tool and feature availability. This plugin assumes the relevant native surfaces are available when a phase asks for them.
- Phase loop: a general plugin invocation starts at `intake` and continues through later phases as far as evidence, approval, permissions, and safety allow.
- Evidence discipline: apply `evidence-discipline.md` before material changes and before completion claims. Use `proof-first-change.md` before material mutation and `diagnosis-loop.md` for bugs, failed checks, bad outputs, disputed claims, and review feedback. Treat old summaries as leads, not proof.
- Information structure: use `information-structure.md` when work changes folders, files, file roles, file placement, or file structure. Reserve workflow artifact vocabulary for support evidence, not ordinary repo contents.
- Decisions and shaping: use `decision-interrogation.md`, `vocabulary-decision-capture.md`, `question-first-scratch-work.md`, and `work-item-shaping.md` when choices, terminology, scratch work, or worker-ready briefs affect a phase.
- Goal-backed planning: `planning` outputs the plan first, then uses native goal tools by default under this workflow's explicit repo-lifecycle contract. Use `get_goal` to compare current goal state against the planned objective. If a different current goal exists, call `request_user_input` for the goal conflict choice. When no current goal exists, `create_goal` creates the default goal after the plan is decision-complete. Normal workflow invocations use goal-backed setup unless the user explicitly asks for planning-only, no-goal, or stop-with-evidence behavior; do not infer goals for ordinary non-workflow tasks. Set `token_budget` only when explicitly requested. Complete only after proof, reporting final token usage for budgeted goals; mark blocked only after the same blocker repeats for at least three consecutive goal turns.
- Branch safety: use `git-worktrees` between planning and execution to record current-branch approval or prepare an isolated worktree before write-owning mutation.
- Narrower skills: use domain-specific skills, tools, or repo-local processes for their specialized procedure while this workflow owns repo lifecycle, evidence, decision, worktree, goal, review, and handoff mechanics.
- User choices: call `request_user_input` when the tool is available, there are 2-3 concrete paths, and the choice affects scope, side effects, ownership, active-goal conflict disposition, verification, review, or closeout. Use `request-user-input.md` for the exact choice shape.
- Phase transition: every phase consumes and updates the shared `phase-bundle.md` state, then routes through `phase-transition.md`.
- Artifacts: follow `artifact-floor.md` for requirements and exceptions, and `html-artifact-template.md` for HTML shape. Source, tests, docs, branches, commits, and PRs are primary.
