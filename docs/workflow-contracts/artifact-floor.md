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

Every durable support artifact includes purpose, repo path, branch when known, inputs reviewed, proof surfaces, scratch-work disposition, subagent evidence, evidence status, decision state, open questions, next actions, and owner when known.

## Interactive HTML Default

Create or update `workflow-artifacts/YYYY-MM-DD-<slug>.html` for substantial workflow runs. Keep the artifact supporting evidence, not authority.

Prefer HTML over Markdown for durable workflow support artifacts. Use Markdown only when repo instructions name it, the user explicitly asks for it, or the artifact must stay plain text for a specific downstream tool.

Prefer copying `../../assets/workflow-artifact-template.html` and filling its placeholders. Use `html-artifact-template.md` for required sections and rules unless repo instructions name a different artifact format.

Allowed interaction: static tabs, filters, collapsible evidence, severity toggles, task tables, acceptance-criteria status, and copyable next prompts. Avoid hidden state, remote dependencies, destructive controls, or requiring the artifact to understand the repo.

## Substantial Run Test

A run is substantial when any of these are true:

- two or more phase transitions happen after `intake`;
- native goal state is created, updated, completed, or blocked;
- write-owning execution changes multiple files or combines source changes with generated support artifacts;
- verification fails, is blocked, or leaves material unverified gaps;
- review produces findings or a disposition ledger;
- handoff needs branch, PR, closeout, owner, or residual-risk decisions.

A run is trivial only when all of these are true:

- the work fits in one phase or one direct command;
- no native goal state changes;
- no repo mutation occurs, or mutation is limited to one narrowly scoped file;
- verification and review have no failures, findings, or unresolved gaps.

## Exceptions

Do not create an HTML artifact when the repo convention names another durable surface, the task is trivial, or the user opts out.
