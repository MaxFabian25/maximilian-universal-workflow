#!/usr/bin/env python3
"""Tests for the deterministic benchmark gate checker."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check_benchmark_gate.py"
SPEC = importlib.util.spec_from_file_location("check_benchmark_gate", SCRIPT_PATH)
assert SPEC and SPEC.loader
check_benchmark_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_benchmark_gate)


class BenchmarkGateTests(unittest.TestCase):
    def test_validate_result_accepts_passing_result(self) -> None:
        result = {
            "summary": {
                "failedScenarios": 0,
                "usageAvailability": "present",
                "averageTotalTokens": 200,
                "failedShellCommands": 0,
            },
            "scenarios": [
                {
                    "id": "example",
                    "status": "completed",
                    "exitCode": 0,
                    "workspaceSummary": {"changedFileCount": 0},
                    "usage": {"total_tokens": 100},
                }
            ],
        }
        thresholds = {
            "thresholds": {
                "expectedScenarioCount": 1,
                "maxFailedScenarios": 0,
                "requireUsage": True,
                "maxAverageTotalTokens": 300,
                "maxScenarioTotalTokens": 150,
                "maxChangedFiles": 0,
                "maxFailedShellCommands": 0,
                "requireCompletedStatus": True,
            },
            "scenarioThresholds": {},
        }

        self.assertEqual(check_benchmark_gate.validate_result(result, thresholds), [])

    def test_validate_result_reports_token_and_mutation_failures(self) -> None:
        result = {
            "summary": {
                "failedScenarios": 1,
                "usageAvailability": "missing",
                "averageTotalTokens": 500,
                "failedShellCommands": 1,
            },
            "scenarios": [
                {
                    "id": "example",
                    "status": "failed",
                    "exitCode": 1,
                    "workspaceSummary": {"changedFileCount": 2},
                    "usage": {"total_tokens": 900},
                }
            ],
        }
        thresholds = {
            "thresholds": {
                "expectedScenarioCount": 1,
                "maxFailedScenarios": 0,
                "requireUsage": True,
                "maxAverageTotalTokens": 300,
                "maxScenarioTotalTokens": 150,
                "maxChangedFiles": 0,
                "maxFailedShellCommands": 0,
                "requireCompletedStatus": True,
            },
            "scenarioThresholds": {},
        }

        failures = check_benchmark_gate.validate_result(result, thresholds)

        self.assertIn("failedScenarios 1 exceeds 0", failures)
        self.assertIn("benchmark usage is not present", failures)
        self.assertIn("averageTotalTokens 500 exceeds 300", failures)
        self.assertIn("failedShellCommands 1 exceeds 0", failures)
        self.assertIn("example: status 'failed' is not completed", failures)
        self.assertIn("example: exitCode 1 is not 0", failures)
        self.assertIn("example: changed files 2 exceeds 0", failures)
        self.assertIn("example: total tokens 900 exceeds 150", failures)

    def test_validate_result_requires_workspace_change_evidence(self) -> None:
        result = {
            "summary": {
                "failedScenarios": 0,
                "usageAvailability": "present",
                "averageTotalTokens": 100,
                "failedShellCommands": 0,
            },
            "scenarios": [
                {
                    "id": "example",
                    "status": "completed",
                    "exitCode": 0,
                    "usage": {"total_tokens": 100},
                }
            ],
        }
        thresholds = {
            "thresholds": {
                "expectedScenarioCount": 1,
                "maxFailedScenarios": 0,
                "requireUsage": True,
                "maxAverageTotalTokens": 300,
                "maxScenarioTotalTokens": 150,
                "maxChangedFiles": 0,
                "maxFailedShellCommands": 0,
                "requireCompletedStatus": True,
            },
            "scenarioThresholds": {},
        }

        failures = check_benchmark_gate.validate_result(result, thresholds)

        self.assertIn("example: workspace change evidence is missing", failures)


if __name__ == "__main__":
    unittest.main()
