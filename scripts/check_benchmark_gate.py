#!/usr/bin/env python3
"""Validate a Plugin Eval benchmark result against committed thresholds."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def mapping(value: Any):
    return value if isinstance(value, dict) else {}


def fallback(primary: Any, secondary: Any):
    return (primary, secondary)[primary is None]


def maybe(condition: bool, message: str):
    return (None, message)[bool(condition)]


def compact(items: list[str | None]):
    return list(filter(None, items))


def both_int(*values: Any):
    return all(map(lambda value: isinstance(value, int), values))


def exceeds(value: Any, limit: Any):
    return value > limit if both_int(value, limit) else False


def differs(value: Any, expected: Any):
    return value != expected if isinstance(expected, int) else False


def changed_file_count(scenario: dict[str, Any]):
    summary = mapping(scenario.get("workspaceSummary"))
    value = summary.get("changedFileCount")
    if isinstance(value, int):
        return value
    changes = scenario.get("workspaceChanges")
    return len(changes) if isinstance(changes, list) else None


def summed_tokens(input_tokens: Any, output_tokens: Any):
    return input_tokens + output_tokens if both_int(input_tokens, output_tokens) else None


def total_tokens(scenario: dict[str, Any]):
    usage = mapping(scenario.get("usage"))
    direct = usage.get("total_tokens")
    return direct if isinstance(direct, int) else summed_tokens(usage.get("input_tokens"), usage.get("output_tokens"))


def summary_failures(result: dict[str, Any], thresholds: dict[str, Any], scenario_count: int):
    summary = mapping(result.get("summary"))
    expected_count = thresholds.get("expectedScenarioCount")
    return compact(
        [
            maybe(
                differs(scenario_count, expected_count),
                f"expected {expected_count} scenarios, found {scenario_count}",
            ),
            maybe(
                exceeds(summary.get("failedScenarios"), thresholds.get("maxFailedScenarios")),
                f"failedScenarios {summary.get('failedScenarios')} exceeds {thresholds.get('maxFailedScenarios')}",
            ),
            maybe(
                thresholds.get("requireUsage") is True and summary.get("usageAvailability") != "present",
                "benchmark usage is not present",
            ),
            maybe(
                exceeds(summary.get("averageTotalTokens"), thresholds.get("maxAverageTotalTokens")),
                f"averageTotalTokens {summary.get('averageTotalTokens')} exceeds "
                f"{thresholds.get('maxAverageTotalTokens')}",
            ),
            maybe(
                exceeds(summary.get("failedShellCommands"), thresholds.get("maxFailedShellCommands")),
                f"failedShellCommands {summary.get('failedShellCommands')} exceeds "
                f"{thresholds.get('maxFailedShellCommands')}",
            ),
        ]
    )


def scenario_failures(scenario: dict[str, Any], thresholds: dict[str, Any], scenario_thresholds: dict[str, Any]):
    scenario_id = str(scenario.get("id", "<missing-id>"))
    per_scenario = mapping(scenario_thresholds.get(scenario_id))
    changed_files = changed_file_count(scenario)
    scenario_total = total_tokens(scenario)
    max_changed = fallback(per_scenario.get("maxChangedFiles"), thresholds.get("maxChangedFiles"))
    max_total = fallback(per_scenario.get("maxTotalTokens"), thresholds.get("maxScenarioTotalTokens"))
    return compact(
        [
            maybe(
                thresholds.get("requireCompletedStatus") is True and scenario.get("status") != "completed",
                f"{scenario_id}: status {scenario.get('status')!r} is not completed",
            ),
            maybe(
                scenario.get("exitCode") not in (0, None),
                f"{scenario_id}: exitCode {scenario.get('exitCode')} is not 0",
            ),
            maybe(
                exceeds(changed_files, max_changed),
                f"{scenario_id}: changed files {changed_files} exceeds {max_changed}",
            ),
            maybe(changed_files is None, f"{scenario_id}: workspace change evidence is missing"),
            maybe(scenario_total is None, f"{scenario_id}: total token usage is missing"),
            maybe(
                exceeds(scenario_total, max_total),
                f"{scenario_id}: total tokens {scenario_total} exceeds {max_total}",
            ),
        ]
    )


def scenario_entry_failures(scenario: Any, thresholds: dict[str, Any], scenario_thresholds: dict[str, Any]):
    return (
        scenario_failures(scenario, thresholds, scenario_thresholds)
        if isinstance(scenario, dict)
        else ["scenario entry must be an object"]
    )


def validate_result(result: dict[str, Any], thresholds_doc: dict[str, Any]):
    scenarios = result.get("scenarios")
    if not isinstance(scenarios, list):
        return ["result.scenarios must be a list"]
    thresholds = mapping(thresholds_doc.get("thresholds"))
    scenario_thresholds = mapping(thresholds_doc.get("scenarioThresholds"))
    nested = map(lambda item: scenario_entry_failures(item, thresholds, scenario_thresholds), scenarios)
    return summary_failures(result, thresholds, len(scenarios)) + sum(nested, [])


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result", type=Path, help="Plugin Eval benchmark result JSON")
    parser.add_argument(
        "--thresholds",
        type=Path,
        default=Path("benchmarks/plugin-eval/scenario-suite-thresholds.json"),
        help="Threshold JSON file",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    result = load_json(args.result)
    thresholds_doc = load_json(args.thresholds)
    summary = mapping(result.get("summary"))
    scenarios = result.get("scenarios")
    failures = validate_result(result, thresholds_doc)

    if failures:
        print("Benchmark gate failed:", file=sys.stderr)
        print("\n".join(map(lambda failure: f"- {failure}", failures)), file=sys.stderr)
        return 1

    scenario_count = len(scenarios) if isinstance(scenarios, list) else 0
    print(
        "Benchmark gate passed: "
        f"{scenario_count} scenarios, averageTotalTokens={summary.get('averageTotalTokens')}, "
        f"failedScenarios={summary.get('failedScenarios')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
