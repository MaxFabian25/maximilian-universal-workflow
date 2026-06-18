# Evidence Discipline

Use this contract for any repo-backed claim, change, review item, or handoff. It absorbs cross-domain workflow discipline without turning the plugin into a software-only harness.

## Core Rule

Evidence before claims, and a proof surface before material changes.

Do not report completion, correctness, support, rejection, or risk disposition from memory, summaries, or old output. Treat earlier notes as leads. Prove the current state again or name the unverified gap.

Use `proof-first-change.md` before material repo mutation. Use `diagnosis-loop.md` for bugs, failed checks, bad outputs, disputed claims, review feedback, and other unexpected results.

## Proof Surfaces

Choose the proof surface that matches the work:

- source-backed writing: cited sources, quotations within limits, checked claims, and open attribution gaps;
- research or analysis: raw inputs, queries, calculations, assumptions, and reproducible outputs;
- planning: repo evidence, acceptance criteria, ownership, decision gates, and verification method;
- implementation: tests, builds, linters, command output, screenshots, generated outputs, or manual checklist evidence;
- cleanup: inventory, classification, approval, and deletion/archive evidence;
- review: changed paths, diffs, support artifacts, requirements, and current branch state.

If no proof surface exists, create the lightest useful one before changing durable repo state. For software this can be a failing test; for writing it can be a claim checklist; for research it can be a reproducible query or calculation; for operations it can be a dry-run or inventory.

## Tight Feedback Loop

When the task is a bug, failed check, bad output, broken analysis, incorrect document, or any other unexpected result, follow `diagnosis-loop.md` before fixing:

- red-capable: it can expose the specific failure or disputed claim;
- current: it runs against the active repo/worktree and current inputs;
- narrow: it isolates the smallest useful scenario;
- repeatable: another agent can run or inspect it without hidden context.

Then form and test one hypothesis at a time. Do not stack speculative fixes, broad rewrites, or unexplained edits on top of an unproven cause. If a loop cannot be built, record what was tried and use `request_user_input` for access, evidence, instrumentation, stop-with-evidence, or accepted-risk choices when 2-3 concrete options remain.

## Scratch Work And Prototypes

Use `question-first-scratch-work.md` for scratch work, scripts, drafts, generated outputs, or prototypes. Temporary work answers a named question, records the result, and is deleted, archived, folded into durable repo work, or assigned an owner before handoff.

Do not let exploratory outputs become authority. Durable authority belongs in repo instructions, docs, source, tests, issue/PR records, accepted support evidence, or explicit user decisions.

## Subagent Evidence

Use Codex-native subagents when independent context, parallel exploration, implementation isolation, or separate review would materially improve quality. Give each subagent a bounded task, explicit ownership, expected evidence, and stop conditions.

The root thread owns integration. Treat subagent reports as evidence to verify, not final truth. Record the task, owner, result, changed paths or support artifacts, proof surface, and integration disposition in the phase bundle or support artifact.

## Review And Feedback

Treat feedback as a claim to evaluate, not an order to obey blindly. Read the whole feedback, verify each item against current repo evidence, then disposition it as fix, reject with evidence, defer, or decision needed.

Apply accepted fixes one item at a time when possible, then run the proof surface that demonstrates the item is resolved. Keep replies technical and evidence-backed.

## Completion Gate

Before `verification`, `review`, or `handoff` reports success:

- map each acceptance criterion to fresh evidence or an explicit gap;
- include command/check names, exit status, pass/fail counts, files, support artifacts, or source evidence;
- remove or disposition scratch work;
- verify or disposition subagent results;
- record residual risk and owner for anything unverified;
- do not mark a native goal complete unless identity and proof gates in `plan-structure.md` are satisfied.
