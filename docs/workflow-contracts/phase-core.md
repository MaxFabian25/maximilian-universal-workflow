# Phase Core

Compact active contract for phase skills. Use detailed workflow-contract files only when this core, a phase reference, uncertainty, or a material decision requires deeper authority.

## Authority

User, developer, system, workspace, and applicable `AGENTS.md` instructions outrank this plugin. Active task packets and explicit user decisions outrank workflow contracts. Skill bodies and local references route into these contracts.

## Runtime

Default phase order:

```text
intake -> exploration -> ideation -> planning -> git-worktrees -> execution -> verification -> review -> handoff
```

Each phase consumes and updates the live phase bundle, then emits a compact footer:

```text
Phase footer:
phase: <current phase>
next_phase: <phase name or done>
continue_now: <yes/no>
decision_gate: <none or request_user_input id/question>
artifact_state: <path and updated/not-needed>
next_prompt: <exact prompt for later continuation or none>
```

Set `continue_now: yes` only when repo state, governing instructions, approval, ownership, side effects, and verification expectations are clear for the next phase. Otherwise ask or stop with evidence.

## Bundle Fields

Preserve and update the fields needed for handoff: repo state, objective, acceptance criteria, allowed side effects, evidence, proof surface, diagnosis loop, scratch work, information structure, vocabulary and decisions, work items, subagent state, goal state, decision gate, worktree state, git closeout state, verification state, review state, artifact state, next phase, and next prompt.

Do not edit contract files as live state. Use a thread footer for trivial runs and an HTML artifact for substantial runs under `artifact-floor.md`.

## Evidence

Apply `evidence-discipline.md` when the task involves uncertainty, a failed check, a broken output, disputed feedback, material repo mutation, or a completion claim. Use `proof-first-change.md` before material mutation and `diagnosis-loop.md` for unexpected results. Use the lightest proof surface that can prove or falsify the claim. Scratch work and prototypes follow `question-first-scratch-work.md`.

## Information Structure

Use `information-structure.md` when work changes folders, files, file roles, file placement, or file structure. Keep ordinary repo contents in file/folder vocabulary and reserve workflow artifact vocabulary for support evidence.

## Subagents

Use Codex-native subagents when they improve quality through independent context, parallel exploration, implementation isolation, or separate review. Keep ownership non-overlapping, require evidence in each return, and have the root thread verify and integrate results before phase transition.

## Decisions

Use `decision-interrogation.md` for material choices and `vocabulary-decision-capture.md` for terms or decisions that future agents must preserve. Any running agent with `request_user_input` available calls it for 2-3 concrete choices that affect scope, side effects, ownership, active-goal conflicts, worktree state, verification, review, cleanup, or handoff. Return `decision_needed` only when the tool is unavailable or the active workflow phase cannot own the choice.

Continue without asking when the user already made the decision or repo evidence safely decides it. Stop only for missing repo mechanics, unknown governing instructions, unsafe or unapproved side effects, ownership overlap, unavailable required tools, failed required verification, or explicit stop instructions.

## Git And Goals

Before mutation, confirm repo root, branch, status, and instructions. If repo mechanics are missing, establish a repo/worktree or stop. Use `git-worktrees` between planning and execution to record current-branch approval or prepare isolation.

Planning owns default native goal-backed setup for this workflow's explicit repo-lifecycle contract: compare active goal state with `get_goal`, resolve conflicts with `request_user_input`, and create a goal only after the plan is decision-complete. Later phases preserve goal identity; `verification` or later updates completion only after fresh proof and reports final token usage when completing a budgeted goal. Mark goals blocked only after the same blocking condition repeats for at least three consecutive goal turns.

## Work Items

Use `work-item-shaping.md` when a request, finding, plan, issue, PRD, or handoff must become worker-ready. Publishing outside the repo remains an explicit side effect.
