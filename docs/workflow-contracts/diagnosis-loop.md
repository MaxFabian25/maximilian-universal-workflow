# Diagnosis Loop

Use this contract for bugs, failed checks, bad outputs, incorrect documents, disputed claims, review feedback, performance regressions, or any unexpected result.

## Core Rule

No durable fix, rewrite, rejection, or risk disposition until the workflow has a red-capable feedback loop, a reproduced or bounded symptom, and a tested cause.

## Loop

1. Name expected state, actual state, affected files or outputs, current inputs, and proof target.
2. Build the lightest tight loop that can expose the specific problem: command, test, checklist, query, calculation, source set, dry-run, screenshot, replay, browser check, or human-in-the-loop script.
3. Reproduce and minimize until the remaining files, inputs, claims, or steps are load-bearing.
4. Write 3-5 ranked falsifiable hypotheses. Each hypothesis states what observation would support or disprove it.
5. Probe one variable at a time. Use targeted boundary evidence or temporary tagged instrumentation instead of broad logging or broad rewrites.
6. Resolve the cause with `proof-first-change.md`.
7. Rerun the original loop, rerun durable proof, remove or disposition temporary work, and record the winning hypothesis plus a prevention note.

For flaky, stateful, or subjective failures, raise the reproduction rate, pin inputs, capture examples, or narrow the review rubric until the loop is useful. If no loop can be built, record attempts and use `request_user_input` for access, source material, instrumentation, accepted-risk, or stop-with-evidence choices when 2-3 concrete options remain.

## Phase Hooks

- exploration: build or name the loop before recommending changes.
- execution: when an unexpected result appears, stop broad edits and diagnose before stacking fixes.
- verification: failed proof routes through diagnosis unless repair is obvious, narrow, and already in scope.
- review and receiving-review: disputed feedback is diagnosed before fix or rejection.
- handoff: report loop, cause, proof, gaps, temporary-work disposition, and residual owner.
