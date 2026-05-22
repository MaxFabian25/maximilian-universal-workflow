# HTML Artifact Template

Use this structure for substantial workflow support artifacts under `workflow-artifacts/YYYY-MM-DD-<slug>.html`.

The artifact is a static, standalone evidence dashboard. It must not fetch remote assets, run destructive actions, or become the policy authority. It mirrors the current phase bundle for human scanning.

## Required Sections

- Header: objective, repo path, branch, current phase, next phase, artifact timestamp.
- Phase timeline: intake, exploration, ideation, planning, git-worktrees, execution, verification, review, handoff.
- Decision gates: `request_user_input` ids, selected options, unresolved decisions.
- Acceptance criteria: criterion, proof source, status, owner.
- Evidence: files, commands, exit statuses, key output, subagent summaries.
- Goal state: active objective, created/matching/conflict/complete/blocked, final usage when complete.
- Worktree state: mode, path, branch, baseline command and result.
- Verification and review: proof, failures, findings, dispositions.
- Handoff: closeout options, risks, next owner, exact next prompt.

## Minimal HTML Shape

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Workflow Evidence</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; color: #111827; background: #f9fafb; }
    main { max-width: 1120px; margin: 0 auto; padding: 24px; }
    header, section { background: #fff; border: 1px solid #e5e7eb; border-radius: 8px; padding: 16px; margin: 0 0 16px; }
    h1, h2 { margin: 0 0 12px; }
    table { width: 100%; border-collapse: collapse; }
    th, td { text-align: left; border-top: 1px solid #e5e7eb; padding: 8px; vertical-align: top; }
    code, pre { background: #f3f4f6; border-radius: 6px; }
    pre { padding: 12px; overflow: auto; }
    .status { font-weight: 600; }
    .pass { color: #047857; }
    .fail { color: #b91c1c; }
    .pending { color: #92400e; }
  </style>
</head>
<body>
<main>
  <header>
    <h1><!-- objective --></h1>
    <p><!-- repo, branch, phase, timestamp --></p>
  </header>
  <section id="bundle"><h2>Phase Bundle</h2><pre><!-- current phase bundle --></pre></section>
  <section id="criteria"><h2>Acceptance Criteria</h2><table><!-- rows --></table></section>
  <section id="decisions"><h2>Decisions</h2><table><!-- rows --></table></section>
  <section id="evidence"><h2>Evidence</h2><table><!-- rows --></table></section>
  <section id="verification"><h2>Verification And Review</h2><table><!-- rows --></table></section>
  <section id="handoff"><h2>Handoff</h2><pre><!-- risks, owner, next prompt --></pre></section>
</main>
</body>
</html>
```

## Rules

- Prefer tables for scan-heavy evidence and `pre` blocks for command output or the phase bundle.
- Keep copyable next prompts visible in the handoff section.
- Use simple CSS in the file; do not require build tools.
- Preserve useful earlier phase evidence when updating the artifact.
- If the artifact would duplicate a richer repo-native report, link or summarize that report instead of recreating it.
