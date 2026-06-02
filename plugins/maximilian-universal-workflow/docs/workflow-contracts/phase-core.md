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

Preserve and update the fields needed for handoff: repo state, objective, acceptance criteria, allowed side effects, evidence, goal state, decision gate, worktree state, git closeout state, subagent state, verification state, review state, artifact state, next phase, and next prompt.

Do not edit contract files as live state. Use a thread footer for trivial runs and an HTML artifact for substantial runs under `artifact-floor.md`.

## Decisions

Any running agent with `request_user_input` available calls it for 2-3 concrete choices that affect scope, side effects, ownership, active-goal conflicts, worktree state, verification, review, cleanup, or handoff. Return `decision_needed` only when the tool is unavailable, the task packet explicitly assigns the decision to the parent, or sibling synthesis must happen first.

Continue without asking when the user already made the decision or repo evidence safely decides it. Stop only for missing repo mechanics, unknown governing instructions, unsafe or unapproved side effects, ownership overlap, unavailable required tools, failed required verification, or explicit stop instructions.

## Git And Goals

Before mutation, confirm repo root, branch, status, and instructions. If repo mechanics are missing, establish a repo/worktree or stop. Use `git-worktrees` between planning and execution to record current-branch approval or prepare isolation.

Planning owns default native goal-backed setup: compare active goal state with `get_goal`, resolve conflicts with `request_user_input`, and create a goal only after the plan is decision-complete. Later phases preserve goal identity; `verification` or later updates completion only after fresh proof.

## Subagents

Use `explorer` for independent read-only evidence, critique, and review. Use `worker` only for isolated non-overlapping mutable ownership. Prefer `fork_turns: "none"`, bounded packets, parent-side synthesis, and closing stuck or unusable children.
