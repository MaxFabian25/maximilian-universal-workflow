# Information Structure

Use this contract when a repo task changes where information lives, how files are arranged, or how a file is organized internally. It generalizes the useful pressure of code architecture and refactoring without making software the center of the workflow.

## Core Idea

Information structure is the repository's durable arrangement of folders, files, file roles, and placement rules.

A well-structured repo makes each file easy to find, easy to classify, and safe to change. Each file should have one durable role, a clear relationship to nearby files, and an internal structure that fits its format and purpose.

## Vocabulary

- Folder: a durable grouping of related files.
- File: the smallest durable repo unit this contract names. It may be source, docs, config, data, test, fixture, generated output, report, asset, manifest, notebook, or any other tracked file.
- File role: the job a file performs, such as authority, explanation, executable source, configuration, input data, derived data, verification, generated output, or workflow support evidence.
- File placement: where a file lives and why that location helps discovery, change, and verification.
- File structure: how information inside a file is grouped, ordered, named, exposed, or validated according to that file's format.
- Locality: how tightly related understanding, change, and verification stay near the files they affect.
- Structural depth: how much useful repo behavior a file or folder arrangement supports per placement rule a maintainer must learn.
- Structure improvement opportunity: a repo-grounded change that improves locality or structural depth without blurring file roles.

Reserve "workflow artifact" for this plugin's support and evidence outputs. Do not use "artifact" as the universal noun for ordinary repo contents.

## Structural Depth

A structure is deep when a small, discoverable surface carries a coherent body of meaning behind it. The surface might be a path, filename, export, schema, key set, column set, entry point, command, rendered output, or documented convention.

A structure is shallow when it adds a name or location but does not concentrate responsibility. Shallow structure makes future agents bounce between many files to understand one concept, or makes one file carry unrelated roles.

## Deletion Test

Imagine deleting a file, folder, section, data column, exported name, config key, or placement rule.

- If deletion removes pass-through noise or duplicated authority, it was probably shallow.
- If the same responsibility reappears scattered across the repo, it was earning its place.
- If deletion removes the only discoverable home for a decision, input, rule, or proof surface, replace or relocate that authority before deleting.

## Improvement Shape

When proposing structure changes, record:

- files or folders involved;
- current friction;
- file roles involved;
- proposed placement or internal structure;
- locality gain;
- structural-depth gain;
- deletion-test result;
- proof surface;
- risk;
- recommendation strength: strong, worth exploring, or speculative.

Prefer hard cutovers: move, split, merge, rename, or delete the stale home once references and proof surfaces are updated. Do not keep compatibility paths unless a user or repo instruction explicitly requires them.

## Phase Hooks

- exploration: map current folders, files, roles, references, and friction before proposing structure changes.
- ideation: compare 2-3 structure options when placement, split, merge, or ownership is user-owned.
- planning: name moves, splits, deletions, reference updates, proof surfaces, and file-role changes.
- execution: make the selected hard cutover and update references in the same ownership boundary.
- verification: prove discovery paths, links, imports, schemas, generated outputs, data provenance, or rendered outputs still work.
- review: check locality, structural depth, duplicated authority, stale references, and overloaded files.
- repo-context-cleanup: classify stale context by file role before deleting, archiving, consolidating, or rewriting.
- handoff: report structure changes, residual risk, and any files whose role remains uncertain.

## Examples

- Source: move behavior, fixtures, and checks so one feature can be understood without searching unrelated folders.
- Docs: split decisions, guides, and reference material when one file mixes authority, narrative, and scratch notes.
- Config: keep schemas, defaults, examples, and validation evidence close enough that changes can be proven.
- Data: separate raw inputs, curated inputs, derived outputs, and validation manifests so provenance is visible.
- Reports: keep generated outputs distinct from source authority and record how to regenerate or verify them.
