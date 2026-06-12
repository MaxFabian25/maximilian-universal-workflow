# Benchmark Gate

The Scenario Suite benchmark gate makes Plugin Eval performance regression checks repeatable for `maximilian-universal-workflow`.

The gate is intentionally separate from deterministic validation. Run deterministic checks first; run the benchmark gate when validating token or behavior changes to workflow guidance.

## Files

- `benchmarks/plugin-eval/scenario-suite.json`: Plugin Eval benchmark config.
- `benchmarks/plugin-eval/scenario-suite-thresholds.json`: token and behavior thresholds.
- `scripts/check_benchmark_gate.py`: deterministic result checker for Plugin Eval benchmark output.
- `scripts/run_benchmark_gate.sh`: current-working-tree runner that snapshots the repo into `tmp/`, replaces the original `.git` metadata with a clean snapshot commit, and invokes Plugin Eval from that snapshot.

These files are repository-development support files that live beside the plugin manifest in this flat plugin repository. They are not workflow authority; the installed runtime guidance remains in `skills/`, `docs/workflow-contracts/`, and `.codex-plugin/plugin.json`.

## Scenarios

- `read-only-regression-review`: checks token-load regression review across planning, git-worktrees, execution, and MultiAgentV2 guidance.
- `goal-backed-planning-gate`: checks goal-backed planning and branch-safety disposition without creating a goal or editing files.
- `weak-match-boundary`: checks that the plugin narrows scope for weak-match requests.

All committed gate scenarios are read-only. This keeps token and latency signals focused on workflow guidance rather than implementation work inside benchmark copies.

## Thresholds

The committed thresholds use repeated Scenario Suite live benchmarks from 2026-05-31 as the baseline:

- observed range: `155910-276019`, `167308-256620`, and `111765-193068` total tokens, with suite averages from `144994.33` to `241902.33`.
- `read-only-regression-review`: must stay at or below `330000` total tokens.
- `goal-backed-planning-gate`: must stay at or below `310000` total tokens.
- `weak-match-boundary`: must stay at or below `235000` total tokens.
- every scenario must complete, report usage, and leave `0` changed files.
- suite average total tokens must stay at or below `300000`.

When a behavior improvement intentionally costs more tokens, update the threshold file in the same change and explain the tradeoff in review.

## Run

From the repository root:

```bash
scripts/run_benchmark_gate.sh
```

The runner writes these generated files under `tmp/plugin-eval-benchmark/`:

- `source/`: current working tree snapshot with generated artifacts and caches excluded, plus a clean local git commit of the snapshot contents.
- `scenario-suite.generated.json`: generated benchmark config with `workspace.sourcePath` rewritten to the snapshot.
- `scenario-suite-result.json`: Plugin Eval benchmark result consumed by the threshold checker.
- `scenario-suite-usage.jsonl`: observed usage samples for Plugin Eval analysis.
- `scenario-suite-report.md` and `scenario-suite-observed-analysis.md`: human-readable reports.

`tmp/` is ignored by git. Do not commit generated benchmark runs unless a user explicitly asks for a durable evidence artifact. Use the runner instead of calling `plugin-eval benchmark` directly from this repo; direct copy mode can encounter `.git` filesystem-monitor sockets and does not give a clean current-working-tree snapshot with repo mechanics intact.

## Deterministic Validation

Run these before handoff:

```bash
jq empty .agents/plugins/marketplace.json
jq empty .codex-plugin/plugin.json
python3 ~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
for skill in skills/*; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
plugin-eval analyze . --format markdown
```
