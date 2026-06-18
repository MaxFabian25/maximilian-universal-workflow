# Replacement Coverage Map

This map records how `maximilian-universal-workflow` replaces the reusable workflow value of Superpowers and Codex Real Engineering Skills without cloning their skill lists.

Dispositions:

- covered: current workflow contracts already own the reusable behavior.
- generalize: absorb the discipline in repo-universal language.
- defer: route to a narrower skill, tool, or external process when needed.
- exclude: outside this plugin's boundary.

## Superpowers

| Source capability | Disposition | Destination | Rationale |
| --- | --- | --- | --- |
| brainstorming | generalize | `decision-interrogation.md`, ideation, planning | Keep evidence-first options, tradeoffs, acceptance criteria, and approval. Drop Superpowers-specific doc paths, mandatory commits, and visual companion mechanics. |
| dispatching parallel agents | covered | `evidence-discipline.md`, `phase-runtime.md` | Scoped subagents, evidence returns, and root integration are already native workflow duties. |
| executing plans | covered | execution, verification, handoff | Approved-plan execution, blockers, proof, and handoff already exist in the phase loop. |
| finishing a development branch | generalize | handoff, git-worktrees, `request-user-input.md` | Keep branch/PR/keep/stop choices as Codex-native closeout decisions, not a source-plugin menu. |
| receiving code review | covered | receiving-review, disposition ledger | Full feedback read, verification before fixes, pushback with evidence, and item-by-item disposition are covered. |
| requesting code review | generalize | review, subagent review hooks | Keep independent review and scoped reviewer context without copying prompt templates. |
| subagent-driven development | generalize | execution, review, `evidence-discipline.md` | Keep non-overlapping ownership, evidence, and review loops without forcing a fixed subagent ceremony for every task. |
| systematic debugging | generalize | `diagnosis-loop.md` | Keep tight loops, reproduction, hypotheses, probes, and cleanup in cross-domain language. |
| test-driven development | generalize | `proof-first-change.md`, plan proof surfaces | Translate test-first into proof-first. Tests remain one proof surface, not the universal rule. |
| using git worktrees | covered | git-worktrees, worktree playbook | Branch safety, isolation, ignore checks, setup, and baseline verification are covered. |
| using superpowers | exclude | none | Global skill-router behavior is outside this repo workflow boundary. |
| verification before completion | covered | verification, `evidence-discipline.md` | Fresh current-state proof before completion claims is already central. |
| writing plans | generalize | planning, `plan-structure.md`, `work-item-shaping.md` | Keep decision-complete task plans, ownership, proof surfaces, self-review, and no placeholders. Drop exact code-step format. |
| writing skills | exclude | none | Skill-authoring doctrine belongs to a skill-authoring workflow. |

## Codex Real Engineering Skills

| Source capability | Disposition | Destination | Rationale |
| --- | --- | --- | --- |
| ask-matt | exclude | lifecycle routing only | The replacement has its own phase routing and should not keep an old-pack router. |
| codebase-design | generalize | `information-structure.md` | Preserve locality, depth, deletion test, and improvement opportunities as file/folder information structure. Drop software-only module vocabulary as the governing frame. |
| diagnosing-bugs | generalize | `diagnosis-loop.md` | Keep red-capable loops, minimized repros, hypotheses, instrumentation, cleanup, and prevention notes. |
| domain-modeling | generalize | `vocabulary-decision-capture.md` | Preserve term sharpening and decision capture, but make repo conventions and laziness the default. |
| grilling, grill-me | generalize | `decision-interrogation.md` | Preserve one-question stress testing with recommended answers and repo evidence. |
| grill-with-docs | generalize | `decision-interrogation.md`, `vocabulary-decision-capture.md` | Preserve interrogation plus evidence and decision capture without forcing a domain-doc workflow. |
| handoff | exclude | replacement handoff | Source conversation compaction differs from this plugin's repo outcome, evidence, git closeout, and owner handoff. |
| improve-codebase-architecture | generalize/defer | `information-structure.md`; narrower architecture scanners | Absorb structural-friction review and improvement opportunity shape. Defer visual architecture scanner mechanics. |
| prototype | generalize | `question-first-scratch-work.md` | Keep "temporary work answers a named question, then delete/archive/fold in." Defer exact UI/logic recipes. |
| setup-engineering-skills | exclude | none | Old pack bootstrap is not part of this universal workflow. |
| tdd | generalize | `proof-first-change.md` | Preserve red/green discipline as proof-first change; strict software TDD stays narrower. |
| teach | exclude | none | Stateful teaching is outside repo workflow lifecycle. |
| to-issues | generalize/defer | `work-item-shaping.md`; external tracker workflows | Keep vertical slices and agent-ready briefs. Defer tracker publishing, labels, and closing behavior. |
| to-prd | generalize/defer | `work-item-shaping.md`; product/tracker workflows | Keep synthesis into durable work items. Defer PRD publishing mechanics. |
| triage | generalize/defer | receiving-review, `work-item-shaping.md`; external tracker workflows | Keep evidence-first classification and ready-for-agent shaping. Defer tracker state machine and labels. |
| writing-great-skills | exclude | none | Skill design vocabulary belongs to skill-authoring references. |
