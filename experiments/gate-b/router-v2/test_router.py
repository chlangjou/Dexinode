from __future__ import annotations

import ast
import inspect
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
BENCHMARK = ROOT / "gate-b/benchmark-v1.1.0"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from router import ROUTES, route_semantic_task  # noqa: E402


class RouterContractTests(unittest.TestCase):
    def test_semantic_fixtures(self) -> None:
        self.assertEqual(route_semantic_task("Find the volume of a tetrahedron."), "mathematics_specialist")
        self.assertEqual(route_semantic_task("Implement a stable transformation of records."), "general_baseline")
        self.assertEqual(route_semantic_task(""), "fallback")

    def test_benchmark_routes_use_only_semantic_task(self) -> None:
        math_cases = yaml.safe_load((BENCHMARK / "cases/math.yaml").read_text())["cases"]
        code_cases = yaml.safe_load((BENCHMARK / "cases/coding.yaml").read_text())["cases"]
        decisions = [route_semantic_task(case["semantic_task"]) for case in math_cases]
        decisions += [route_semantic_task(case["semantic_task"]) for case in code_cases]
        self.assertEqual(decisions, ["mathematics_specialist"] * 48 + ["general_baseline"] * 48)

    def test_signature_and_registered_routes(self) -> None:
        self.assertEqual(list(inspect.signature(route_semantic_task).parameters), ["semantic_task"])
        for text in ("x", "Implement x", ""):
            self.assertIn(route_semantic_task(text), ROUTES)

    def test_source_has_no_hidden_information_channel_or_contract_cues(self) -> None:
        source = Path(inspect.getsourcefile(route_semantic_task)).read_text()
        tree = ast.parse(source)
        imported = {
            node.module or node.names[0].name
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
        }
        imported.update(
            alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        )
        self.assertEqual(imported, {"__future__", "re"})
        forbidden = ("expected", "evaluator", "task_family", "model_output", "metadata", "handoff", "python", "entrypoint", "answer", "fraction", "integer", "implementation", "fenced")
        for token in forbidden:
            self.assertNotIn(token, source.casefold())

    def test_no_mutation_or_io_calls(self) -> None:
        source = Path(inspect.getsourcefile(route_semantic_task)).read_text()
        tree = ast.parse(source)
        forbidden_calls = {"open", "exec", "eval", "compile", "system", "Popen"}
        calls = {
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        }
        self.assertTrue(calls.isdisjoint(forbidden_calls))
        prompt = "Find a rational value."
        self.assertEqual(route_semantic_task(prompt), "mathematics_specialist")
        self.assertEqual(prompt, "Find a rational value.")


if __name__ == "__main__":
    unittest.main()
