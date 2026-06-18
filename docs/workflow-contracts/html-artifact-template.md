# HTML Artifact Template

Use this structure for substantial workflow support artifacts under `workflow-artifacts/YYYY-MM-DD-<slug>.html`.

Prefer copying `../../assets/workflow-artifact-template.html` and filling its placeholders instead of rewriting the HTML skeleton from scratch.

The artifact is a static, standalone evidence dashboard. It must not fetch remote assets, run destructive actions, or become the policy authority. It mirrors the current phase bundle for human scanning.

## Required Sections

- Header: objective, repo path, branch, current phase, next phase, artifact timestamp.
- Phase timeline: intake, exploration, ideation, planning, git-worktrees, execution, verification, review, handoff.
- Decision gates: `request_user_input` ids, selected options, unresolved decisions.
- Acceptance criteria: criterion, proof source, status, owner.
- Evidence: proof surfaces, subagents, scratch work, files, commands, exit statuses, and key output.
- Goal state: active objective, created/matching/conflict/complete/blocked, final usage when complete.
- Worktree state: mode, path, branch, baseline command and result.
- Verification and review: proof, failures, findings, dispositions.
- Handoff: closeout options, risks, next owner, exact next prompt.

## Template File

Use `../../assets/workflow-artifact-template.html` as the only maintained HTML skeleton. This contract defines required content and artifact rules; the asset carries the current HTML and CSS implementation.

When changing the support artifact shape, update this contract and the asset in the same patch. Do not keep compatibility skeletons or copied older templates.

## Rules

- Prefer tables for scan-heavy evidence and `pre` blocks for command output or the phase bundle.
- Keep copyable next prompts visible in the handoff section.
- Keep the template controls working: tabs use `data-tab` and `data-panel`, status filters use `data-filter` with optional row-level `data-status`, and next prompts use `data-copy-target`.
- Use simple CSS in the file; do not require build tools.
- Preserve useful earlier phase evidence when updating the artifact.
- If the artifact would duplicate a richer repo-native report, link or summarize that report instead of recreating it.
