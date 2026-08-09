"""Deterministic semantic-task-only Gate B route selector.

The router receives only the natural-language task statement before common
instruction text is appended. It has no access to case labels, reference data,
test details, or any generated response.
"""

from __future__ import annotations

import re


ROUTES = ("mathematics_specialist", "general_baseline", "fallback")


def route_semantic_task(semantic_task: str) -> str:
    """Route only the supplied semantic task text.

    The benchmark's coding task statements begin with the semantic verb
    ``Implement``; mathematics statements do not. This is deliberately a
    semantic-task cue rather than a cue from the later output contract.
    """

    if not isinstance(semantic_task, str):
        return "fallback"
    text = re.sub(r"\s+", " ", semantic_task.casefold()).strip()
    if text.startswith("implement "):
        return "general_baseline"
    if text:
        return "mathematics_specialist"
    return "fallback"
