from __future__ import annotations

import unittest

try:
    from .semantic_adapter import (
        extract_python_source,
        math_semantic_score,
        normalize_math_response,
        strict_coding_interface_compliance,
        strict_math_interface_compliance,
    )
except ImportError:  # Direct invocation: python adapter/test_adapter.py
    from semantic_adapter import (
        extract_python_source,
        math_semantic_score,
        normalize_math_response,
        strict_coding_interface_compliance,
        strict_math_interface_compliance,
    )


def integer_expected(value: int) -> dict[str, object]:
    return {"type": "integer", "value": value}


def rational_expected(value: str) -> dict[str, object]:
    return {"type": "rational", "value": value}


def object_expected(value: dict[str, int]) -> dict[str, object]:
    return {
        "type": "structured_object",
        "schema": {"keys": ["x", "y"], "key_order": ["x", "y"], "value_type": "integer"},
        "value": value,
    }


class MathAdapterTests(unittest.TestCase):
    def test_canonical_integer(self) -> None:
        expected = integer_expected(6)
        result = normalize_math_response("ANSWER: 6", expected)
        self.assertEqual(result.status, "accepted")
        self.assertEqual(math_semantic_score(result, expected), 1)
        self.assertTrue(strict_math_interface_compliance("ANSWER: 6", expected))

    def test_boxed_integer(self) -> None:
        expected = integer_expected(-14)
        result = normalize_math_response("The calculation gives \\boxed{-14}.", expected)
        self.assertEqual(result.normalized, -14)
        self.assertEqual(math_semantic_score(result, expected), 1)
        self.assertFalse(strict_math_interface_compliance("The calculation gives \\boxed{-14}.", expected))

    def test_canonical_rational_reduces(self) -> None:
        expected = rational_expected("2/7")
        result = normalize_math_response("reasoning\nANSWER: 6/21", expected)
        self.assertEqual(result.normalized, (2, 7))
        self.assertEqual(math_semantic_score(result, expected), 1)

    def test_boxed_rational_and_latex_fraction(self) -> None:
        expected = rational_expected("3/28")
        slash = normalize_math_response("\\boxed{6/56}", expected)
        latex = normalize_math_response("Therefore \\boxed{\\frac{3}{28}}", expected)
        self.assertEqual(slash.normalized, (3, 28))
        self.assertEqual(latex.normalized, (3, 28))

    def test_structured_json_and_boxed_tuple(self) -> None:
        expected = object_expected({"x": 4, "y": -9})
        json_result = normalize_math_response('ANSWER: {"y": -9, "x": 4}', expected)
        tuple_result = normalize_math_response("\\boxed{(4, -9)}", expected)
        self.assertEqual(math_semantic_score(json_result, expected), 1)
        self.assertEqual(tuple_result.normalized, {"x": 4, "y": -9})

    def test_conflicting_candidates_rejected(self) -> None:
        result = normalize_math_response("ANSWER: 5\nfinal: \\boxed{6}", integer_expected(6))
        self.assertEqual(result.status, "rejected")
        self.assertEqual(result.reason, "ambiguous_conflicting_final_candidates")

    def test_malformed_answer_rejected(self) -> None:
        expected = rational_expected("5/9")
        result = normalize_math_response("ANSWER: five ninths", expected)
        self.assertEqual(result.status, "rejected")
        self.assertFalse(strict_math_interface_compliance("ANSWER: 5/0", expected))


class CodingAdapterTests(unittest.TestCase):
    def test_implementation_with_surrounding_prose(self) -> None:
        response = "Here is the implementation:\n```python\ndef target(x):\n    return x + 1\n```\n"
        result = extract_python_source(response, "target")
        self.assertEqual(result.status, "accepted")
        self.assertEqual(result.reason, "first_qualifying_python_fenced_block")
        self.assertFalse(strict_coding_interface_compliance(response, "target"))

    def test_implementation_then_example_block(self) -> None:
        response = (
            "```python\ndef target(x):\n    return x * 2\n```\n"
            "Example:\n```python\nprint(target(4))\n```"
        )
        result = extract_python_source(response, "target")
        self.assertEqual(result.block_index, 0)
        self.assertIn("return x * 2", result.source or "")

    def test_missing_entrypoint_rejected(self) -> None:
        result = extract_python_source("```python\ndef helper(x):\n    return x\n```", "target")
        self.assertEqual(result.status, "rejected")
        self.assertEqual(result.reason, "no_qualifying_python_fenced_block")

    def test_first_of_multiple_implementation_candidates_wins(self) -> None:
        response = (
            "```python\ndef target(x):\n    return 'first'\n```\n"
            "```python\ndef target(x):\n    return 'second'\n```"
        )
        result = extract_python_source(response, "target")
        self.assertEqual(result.block_index, 0)
        self.assertIn("'first'", result.source or "")

    def test_full_response_python_fallback(self) -> None:
        result = extract_python_source("def target(x):\n    return x - 2\n", "target")
        self.assertEqual(result.reason, "full_response_python_fallback")
        self.assertTrue(strict_coding_interface_compliance("def target(x):\n    return x - 2\n", "target"))

    def test_non_python_fence_is_not_a_candidate(self) -> None:
        result = extract_python_source("```javascript\nfunction target(x) { return x; }\n```", "target")
        self.assertEqual(result.status, "rejected")
        self.assertEqual(result.reason, "no_qualifying_python_fenced_block")


if __name__ == "__main__":
    unittest.main()
