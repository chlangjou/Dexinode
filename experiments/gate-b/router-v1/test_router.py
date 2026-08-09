from __future__ import annotations

import ast
import inspect
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "experiments/gate-b/benchmark-v1.0.0"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from router import ROUTES, route_prompt  # noqa: E402


class RouterContractTests(unittest.TestCase):
    def test_synthetic_domain_fixtures(self) -> None:
        self.assertEqual(route_prompt("Compute the determinant of a 3 by 3 matrix."), "mathematics_specialist")
        self.assertEqual(route_prompt("What is the probability of drawing two red cards?"), "mathematics_specialist")
        self.assertEqual(
            route_prompt("Define a Python 3.10 function named total and return its source in an implementation block."),
            "general_baseline",
        )
        self.assertEqual(route_prompt("Write Python 3.10 source for the requested entrypoint."), "general_baseline")
        self.assertEqual(route_prompt("Tell me a short story about a lighthouse."), "fallback")

    def test_registered_routes_and_determinism(self) -> None:
        fixtures = ["Compute 7/9 + 2/9.", "Define a Python 3.10 entrypoint.", "Unsupported request."]
        for prompt in fixtures:
            results = [route_prompt(prompt) for _ in range(20)]
            self.assertEqual(len(set(results)), 1)
            self.assertIn(results[0], ROUTES)

    def test_benchmark_domain_routing_accuracy(self) -> None:
        math_cases = yaml.safe_load((BENCHMARK / "cases/math.yaml").read_text())['cases']
        code_cases = yaml.safe_load((BENCHMARK / "cases/coding.yaml").read_text())['cases']
        cases = [(case, "mathematics_specialist") for case in math_cases]
        cases += [(case, "general_baseline") for case in code_cases]
        decisions = [route_prompt(case["prompt"]) for case, _ in cases]
        expected = [label for _, label in cases]
        correct = sum(actual == wanted for actual, wanted in zip(decisions, expected))
        self.assertEqual(len(cases), 96)
        self.assertGreaterEqual(correct / len(cases), 0.95)
        self.assertEqual(correct, 96)

    def test_prompt_only_signature(self) -> None:
        signature = inspect.signature(route_prompt)
        self.assertEqual(list(signature.parameters), ["prompt"])
        self.assertEqual(signature.return_annotation, "str")

    def test_router_source_has_no_hidden_information_channel(self) -> None:
        source = Path(inspect.getsourcefile(route_prompt)).read_text()
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
        forbidden = ("expected", "evaluator", "hidden_domain", "model_output", "case_metadata")
        for token in forbidden:
            self.assertNotIn(token, source)
        forbidden_calls = {"open", "exec", "eval", "compile", "system", "Popen"}
        calls = {
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        }
        self.assertTrue(calls.isdisjoint(forbidden_calls))

    def test_no_prompt_mutation_or_side_effect_input(self) -> None:
        prompt = "Compute a fraction 5/8."
        before = prompt[:]
        route_prompt(prompt)
        self.assertEqual(prompt, before)


if __name__ == "__main__":
    unittest.main()
