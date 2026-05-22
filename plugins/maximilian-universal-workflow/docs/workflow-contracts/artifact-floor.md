# Artifact Floor

`workflow-artifacts/` stores supporting workflow evidence. It is not the primary output surface for repo work.

## Default Path

```text
./workflow-artifacts/YYYY-MM-DD-<slug>.html
```

## Use For

- evidence ledgers;
- planning reports;
- exploration summaries;
- verification or review ledgers;
- operator handoff reports.

## Required Content

Every durable support artifact includes purpose, repo path, branch when known, inputs reviewed, evidence status, decision state, open questions, next actions, and owner when known.

## Interactive HTML Default

Create or update `workflow-artifacts/YYYY-MM-DD-<slug>.html` for substantial workflow runs. Substantial runs include multi-phase work, multi-agent work, goal-backed execution, non-trivial verification, review ledgers, and handoff reports. Keep the artifact supporting evidence, not authority.

Prefer copying `assets/workflow-artifact-template.html` and filling its placeholders. Use `html-artifact-template.md` for required sections and rules unless repo instructions name a different artifact format.

Allowed interaction: static tabs, filters, collapsible evidence, severity toggles, task tables, acceptance-criteria status, and copyable next prompts. Avoid hidden state, remote dependencies, destructive controls, or requiring the artifact to understand the repo.

## Exceptions

Do not create an HTML artifact when the repo convention names another durable surface, the task is trivial, or the user opts out.
