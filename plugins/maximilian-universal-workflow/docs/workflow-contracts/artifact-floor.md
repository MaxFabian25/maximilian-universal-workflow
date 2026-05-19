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

## Exceptions

Do not create an HTML artifact when the repo convention names another durable surface, the task is trivial, or the user opts out.
