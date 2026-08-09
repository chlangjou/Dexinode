"""Deterministic prompt-only Gate B route selector.

The public API accepts exactly one task-prompt string and returns one registered
route name. It performs no I/O and imports no model/runtime package.
"""

from __future__ import annotations

import re


ROUTES = ("mathematics_specialist", "general_baseline", "fallback")

_CODE_MARKERS = (
    "python 3.10",
    "python or unlabeled",
    "entrypoint",
    "implementation block",
    "return python",
)

_MATH_MARKERS = (
    "probability",
    "fraction",
    "integer",
    "equation",
    "matrix",
    "determinant",
    "coefficient",
    "divisible",
    "permutation",
    "functions from",
    "lattice paths",
    "triangle",
    "polygon",
    "sequence",
    "gcd",
    "greatest common divisor",
    "modulo",
    "modular",
    "prime",
    "quadratic",
    "binary string",
    "catalan",
    "diagonals",
    "vector",
    "transformation",
    "system",
)


def route_prompt(prompt: str) -> str:
    """Return one registered route using only the supplied task prompt."""

    if not isinstance(prompt, str):
        return "fallback"
    text = re.sub(r"\s+", " ", prompt.casefold()).strip()
    code_score = sum(marker in text for marker in _CODE_MARKERS)
    math_score = sum(marker in text for marker in _MATH_MARKERS)
    if code_score >= 2 and code_score > math_score:
        return "general_baseline"
    if math_score >= 1 and math_score > code_score:
        return "mathematics_specialist"
    return "fallback"
