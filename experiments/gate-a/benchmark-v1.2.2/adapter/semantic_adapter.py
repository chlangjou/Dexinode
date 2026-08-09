"""Frozen deterministic semantic normalization for Gate A benchmark v1.2.

This module never executes generated source and never uses an expected answer
value to choose a generated candidate. Later source execution belongs only to
the approved judge-v2 sandbox.
"""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass
from fractions import Fraction
from typing import Any


_CANONICAL_LINE = re.compile(r"(?m)^[ \t]*ANSWER:[ \t]*(.*?)[ \t]*$")
_BOXED_INTEGER = re.compile(r"\\boxed\s*\{\s*([+-]?\d+)\s*\}")
_BOXED_RATIONAL = re.compile(r"\\boxed\s*\{\s*([+-]?\d+)\s*/\s*([+-]?\d+)\s*\}")
_BOXED_LATEX_RATIONAL = re.compile(
    r"\\boxed\s*\{\s*\\frac\s*\{\s*([+-]?\d+)\s*\}\s*\{\s*([+-]?\d+)\s*\}\s*\}"
)
_BOXED_TUPLE = re.compile(r"\\boxed\s*\{\s*\((.*?)\)\s*\}")
_FENCED_BLOCK = re.compile(r"```([^`\n]*)\n(.*?)```", re.DOTALL)


@dataclass(frozen=True)
class MathNormalization:
    status: str
    normalized: Any = None
    candidate_kind: str | None = None
    candidate_count: int = 0
    reason: str | None = None


@dataclass(frozen=True)
class ExtractionResult:
    status: str
    source: str | None = None
    block_index: int | None = None
    block_language: str | None = None
    reason: str | None = None


def _type_name(expected: dict[str, Any]) -> str:
    return str(expected.get("type", ""))


def _parse_integer(value: str) -> int | None:
    if re.fullmatch(r"[+-]?\d+", value.strip()) is None:
        return None
    return int(value.strip(), 10)


def _parse_rational(value: str) -> tuple[int, int] | None:
    match = re.fullmatch(r"([+-]?\d+)[ \t]*/[ \t]*([+-]?\d+)", value.strip())
    if match is None:
        return None
    numerator = int(match.group(1), 10)
    denominator = int(match.group(2), 10)
    if denominator <= 0:
        return None
    fraction = Fraction(numerator, denominator)
    return fraction.numerator, fraction.denominator


def _object_schema(expected: dict[str, Any]) -> tuple[list[str], list[str]] | None:
    schema = expected.get("schema")
    if not isinstance(schema, dict):
        return None
    keys = schema.get("keys")
    key_order = schema.get("key_order")
    if not isinstance(keys, list) or not isinstance(key_order, list):
        return None
    if not all(isinstance(key, str) for key in keys + key_order):
        return None
    if sorted(keys) != sorted(key_order) or len(set(keys)) != len(keys):
        return None
    if schema.get("value_type") != "integer":
        return None
    return list(keys), list(key_order)


def _normalize_object(value: str, expected: dict[str, Any]) -> dict[str, int] | None:
    schema = _object_schema(expected)
    if schema is None:
        return None
    keys, key_order = schema
    try:
        parsed = json.loads(value.strip())
    except json.JSONDecodeError:
        return None
    if not isinstance(parsed, dict) or set(parsed) != set(keys):
        return None
    if any(isinstance(item, bool) or not isinstance(item, int) for item in parsed.values()):
        return None
    return {key: int(parsed[key]) for key in key_order}


def _normalize_tuple(value: str, expected: dict[str, Any]) -> dict[str, int] | None:
    schema = _object_schema(expected)
    if schema is None:
        return None
    _, key_order = schema
    pieces = value.split(",")
    if len(pieces) != len(key_order):
        return None
    numbers: list[int] = []
    for piece in pieces:
        number = _parse_integer(piece.strip())
        if number is None:
            return None
        numbers.append(number)
    return {key: number for key, number in zip(key_order, numbers)}


def _parse_canonical(body: str, expected: dict[str, Any]) -> Any | None:
    expected_type = _type_name(expected)
    if expected_type == "integer":
        return _parse_integer(body)
    if expected_type == "rational":
        return _parse_rational(body)
    if expected_type == "structured_object":
        return _normalize_object(body, expected)
    return None


def _boxed_candidates(response: str, expected: dict[str, Any]) -> list[Any]:
    expected_type = _type_name(expected)
    if expected_type == "integer":
        return [int(match.group(1), 10) for match in _BOXED_INTEGER.finditer(response)]
    if expected_type == "rational":
        candidates: list[Any] = []
        for pattern in (_BOXED_RATIONAL, _BOXED_LATEX_RATIONAL):
            for match in pattern.finditer(response):
                denominator = int(match.group(2), 10)
                if denominator <= 0:
                    continue
                fraction = Fraction(int(match.group(1), 10), denominator)
                candidates.append((fraction.numerator, fraction.denominator))
        return candidates
    if expected_type == "structured_object":
        candidates = []
        for match in _BOXED_TUPLE.finditer(response):
            normalized = _normalize_tuple(match.group(1), expected)
            if normalized is not None:
                candidates.append(normalized)
        return candidates
    return []


def _canonical_key(value: Any, expected: dict[str, Any]) -> Any:
    if _type_name(expected) == "structured_object":
        schema = _object_schema(expected)
        if schema is None or not isinstance(value, dict):
            return None
        return tuple(value[key] for key in schema[1])
    return value


def normalize_math_response(response: str, expected: dict[str, Any]) -> MathNormalization:
    """Normalize one math response using only the frozen expected type/schema."""

    canonical: list[Any] = []
    for match in _CANONICAL_LINE.finditer(response):
        parsed = _parse_canonical(match.group(1), expected)
        if parsed is not None:
            canonical.append(parsed)
    boxed = _boxed_candidates(response, expected)
    candidates = canonical + boxed
    if not candidates:
        return MathNormalization(status="rejected", candidate_count=0, reason="no_valid_final_candidate")

    keys = {_canonical_key(candidate, expected) for candidate in candidates}
    if len(keys) != 1:
        return MathNormalization(
            status="rejected",
            candidate_count=len(candidates),
            reason="ambiguous_conflicting_final_candidates",
        )
    chosen = canonical[0] if canonical else boxed[0]
    return MathNormalization(
        status="accepted",
        normalized=chosen,
        candidate_kind="canonical" if canonical else "boxed",
        candidate_count=len(candidates),
    )


def math_semantic_score(normalization: MathNormalization, expected: dict[str, Any]) -> int:
    """Compare only after extraction; this is the deterministic primary score."""

    if normalization.status != "accepted":
        return 0
    actual = _canonical_key(normalization.normalized, expected)
    expected_value = expected.get("value")
    if _type_name(expected) == "rational":
        parsed_expected = _parse_rational(str(expected_value))
        return int(actual == parsed_expected)
    if _type_name(expected) == "structured_object" and isinstance(expected_value, dict):
        schema = _object_schema(expected)
        if schema is None:
            return 0
        expected_key = tuple(int(expected_value[key]) for key in schema[1])
        return int(actual == expected_key)
    return int(actual == expected_value)


def strict_math_interface_compliance(response: str, expected: dict[str, Any]) -> bool:
    """Return whether the response is exactly one canonical ANSWER contract."""

    stripped = response.strip()
    if "\n" in stripped or "\r" in stripped:
        return False
    match = re.fullmatch(r"ANSWER:[ \t]*(.*?)[ \t]*", stripped)
    if match is None:
        return False
    body = match.group(1)
    parsed = _parse_canonical(body, expected)
    if parsed is None:
        return False
    if _type_name(expected) == "rational":
        fraction = _parse_rational(body)
        if fraction is None or body.strip() != f"{fraction[0]}/{fraction[1]}":
            return False
    if _type_name(expected) == "structured_object":
        schema = _object_schema(expected)
        if schema is None:
            return False
        try:
            object_value = json.loads(body)
        except json.JSONDecodeError:
            return False
        if list(object_value) != schema[1]:
            return False
    return True


def _top_level_defines(tree: ast.Module, entrypoint: str) -> bool:
    return any(
        isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == entrypoint
        for node in tree.body
    )


def _parse_source(source: str, entrypoint: str) -> ast.Module | None:
    try:
        tree = ast.parse(source, mode="exec")
    except (SyntaxError, ValueError, TypeError):
        return None
    return tree if _top_level_defines(tree, entrypoint) else None


def extract_python_source(response: str, entrypoint: str) -> ExtractionResult:
    """Select the first qualifying fenced implementation without execution."""

    blocks = list(_FENCED_BLOCK.finditer(response))
    for index, match in enumerate(blocks):
        language = match.group(1).strip().lower()
        if language not in {"", "python"}:
            continue
        source = match.group(2)
        if _parse_source(source, entrypoint) is not None:
            return ExtractionResult(
                status="accepted",
                source=source,
                block_index=index,
                block_language=language or "unlabeled",
                reason="first_qualifying_python_fenced_block",
            )
    if not blocks:
        if _parse_source(response, entrypoint) is not None:
            return ExtractionResult(
                status="accepted",
                source=response,
                reason="full_response_python_fallback",
            )
        return ExtractionResult(status="rejected", reason="full_response_missing_entrypoint_or_invalid_python")
    return ExtractionResult(status="rejected", reason="no_qualifying_python_fenced_block")


def strict_coding_interface_compliance(response: str, entrypoint: str) -> bool:
    """Return whether the complete response is one clean source interface."""

    blocks = list(_FENCED_BLOCK.finditer(response))
    if blocks:
        if len(blocks) != 1:
            return False
        block = blocks[0]
        language = block.group(1).strip().lower()
        if language not in {"", "python"}:
            return False
        if response[: block.start()].strip() or response[block.end() :].strip():
            return False
        return _parse_source(block.group(2), entrypoint) is not None
    return _parse_source(response, entrypoint) is not None
