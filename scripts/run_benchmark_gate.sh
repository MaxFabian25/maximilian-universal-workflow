#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
plugin_root="$repo_root/plugins/maximilian-universal-workflow"
benchmark_root="$repo_root/benchmarks/plugin-eval"
out_dir="${1:-$repo_root/tmp/plugin-eval-benchmark}"
source_dir="$out_dir/source"
config_path="$out_dir/scenario-suite.generated.json"
usage_path="$out_dir/scenario-suite-usage.jsonl"
result_path="$out_dir/scenario-suite-result.json"
report_path="$out_dir/scenario-suite-report.md"
analysis_path="$out_dir/scenario-suite-observed-analysis.md"

repo_real="$(python3 -c 'import pathlib, sys; print(pathlib.Path(sys.argv[1]).resolve())' "$repo_root")"
out_real="$(python3 -c 'import pathlib, sys; print(pathlib.Path(sys.argv[1]).resolve())' "$out_dir")"
case "$out_real" in
  "$repo_real"/tmp|"$repo_real"/tmp/*|"$repo_real"/.tmp|"$repo_real"/.tmp/*) ;;
  "$repo_real"/*)
    printf 'error: output directory inside the repository must be under tmp/ or .tmp/: %s\n' "$out_dir" >&2
    exit 2
    ;;
esac

mkdir -p "$out_dir"

python3 - "$repo_root" "$source_dir" <<'PY'
import shutil
import sys
from pathlib import Path

repo_root = Path(sys.argv[1]).resolve()
source_dir = Path(sys.argv[2]).resolve()
ignored_names = {".git", "tmp", "workflow-artifacts", ".plugin-eval", ".pytest_cache", "__pycache__"}

if source_dir.exists():
    shutil.rmtree(source_dir)


def ignore_names(_directory, names):
    return [name for name in names if name in ignored_names]


shutil.copytree(repo_root, source_dir, ignore=ignore_names)
PY

git -C "$source_dir" init -q
git -C "$source_dir" checkout -B benchmark-snapshot >/dev/null 2>&1
git -C "$source_dir" config user.name "Plugin Eval Benchmark"
git -C "$source_dir" config user.email "plugin-eval-benchmark@example.invalid"
git -C "$source_dir" add -A
git -C "$source_dir" commit -q -m "Benchmark snapshot"

python3 - "$benchmark_root/scenario-suite.json" "$config_path" "$source_dir" <<'PY'
import json
import sys
from pathlib import Path

source_config = Path(sys.argv[1])
target_config = Path(sys.argv[2])
source_dir = Path(sys.argv[3]).resolve()

config = json.loads(source_config.read_text(encoding="utf-8"))
config["workspace"] = {
    **config.get("workspace", {}),
    "sourcePath": str(source_dir),
    "setupMode": "copy",
}
target_config.write_text(f"{json.dumps(config, indent=2)}\n", encoding="utf-8")
PY

plugin-eval benchmark "$source_dir/plugins/maximilian-universal-workflow" \
  --config "$config_path" \
  --usage-out "$usage_path" \
  --result-out "$result_path" \
  --format markdown \
  --output "$report_path"

python3 "$repo_root/scripts/check_benchmark_gate.py" \
  "$result_path" \
  --thresholds "$benchmark_root/scenario-suite-thresholds.json"

if [[ -f "$usage_path" ]]; then
  plugin-eval analyze "$plugin_root" \
    --observed-usage "$usage_path" \
    --format markdown \
    --output "$analysis_path"
fi

printf 'Benchmark artifacts written to %s\n' "$out_dir"
