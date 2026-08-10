"""Complete deterministic B1R static validation.

This validator reads only benchmark definitions and synthetic fixtures. It does
not load a checkpoint, call a model, or execute generated source.
"""

from __future__ import annotations

import ast
import csv
import io
import re
import sys
from collections import Counter, defaultdict, deque
from fractions import Fraction
from pathlib import Path

import yaml
from transformers import PreTrainedTokenizerFast


ROOT = Path(__file__).resolve().parents[4]
BENCHMARK = ROOT / "experiments/gate-b/benchmark-v1.1.1"
TOKENIZER_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/tmp.lAuX9xsJpt/tokenizer.json")


def math_reference(case_id: str):
    direct = {
        "math-01": 45, "math-02": Fraction(3, 11), "math-03": 10, "math-04": 11,
        "math-05": Fraction(849, 10), "math-06": Fraction(9, 20), "math-07": 20,
        "math-08": 90, "math-09": 115, "math-10": 16, "math-11": {"real": 11, "imaginary": 10},
        "math-12": {"median": 12, "mad": 6}, "math-13": Fraction(25, 72), "math-14": 136,
        "math-15": Fraction(7, 2), "math-16": 21, "math-17": {"first": -3, "second": 6},
        "math-18": 13, "math-19": 8, "math-20": 1620, "math-21": 8, "math-22": 13,
        "math-23": Fraction(19, 48), "math-24": 8, "math-25": 55, "math-26": Fraction(80, 243),
        "math-27": 63, "math-28": 6, "math-29": 4, "math-30": 2, "math-31": 2,
        "math-32": Fraction(49, 9), "math-33": 294, "math-34": 2, "math-35": 8,
        "math-36": Fraction(1, 16), "math-37": Fraction(161, 36), "math-38": 84,
        "math-39": 125, "math-40": 11, "math-41": Fraction(3, 4), "math-42": 10,
        "math-43": 7, "math-44": 34650, "math-45": Fraction(175, 256), "math-46": 16,
        "math-47": 5, "math-48": -50,
    }
    return direct[case_id]


def coding_reference(case_id: str, args):
    if case_id == "code-01":
        value, step = args; return ((2 * value + step) // (2 * step)) * step
    if case_id == "code-02": return bool(re.fullmatch(r"#[0-9a-fA-F]{6}", args[0]))
    if case_id == "code-03":
        n, out = args[0], ""
        while n: n, rem = divmod(n - 1, 26); out = chr(65 + rem) + out
        return out
    if case_id == "code-04": return sum(value if i % 2 == 0 else -value for i, value in enumerate(args[0]))
    if case_id == "code-05": return [i for i in range(1, len(args[0])) if args[0][i] != args[0][i - 1]]
    if case_id == "code-06": return [item for group in args[0] for item in group]
    if case_id == "code-07":
        left, right, fill = args; return [[left[i] if i < len(left) else fill, right[i] if i < len(right) else fill] for i in range(max(len(left), len(right)))]
    if case_id == "code-08": return "negative" if args[0] < 0 else "zero" if args[0] == 0 else "positive"
    if case_id == "code-09":
        total = args[0]; h, rem = divmod(total, 3600); m, s = divmod(rem, 60); return {"hours": h, "minutes": m, "seconds": s}
    if case_id == "code-10": return sorted(args)[1]
    if case_id == "code-11":
        out = {}
        for line in args[0].splitlines():
            if line.strip() and "=" in line:
                key, value = line.split("=", 1); out[key.strip()] = value.strip()
        return out
    if case_id == "code-12":
        seen = set(); out = []
        for value in args[0]: seen.add(value); out.append(len(seen))
        return out
    if case_id == "code-13": return [len(row) for row in args[0]]
    if case_id == "code-14": return [args[0][i] for i in args[1]]
    if case_id == "code-15":
        values = args[0]
        if not values: return 0
        best = current = 1; previous = 0
        for left, right in zip(values, values[1:]):
            sign = (right > left) - (right < left)
            current = current + 1 if sign and previous and sign != previous else 2 if sign else 1
            best = max(best, current); previous = sign
        return best
    if case_id == "code-16":
        import datetime
        return datetime.date(*args).isoweekday()
    if case_id == "code-17":
        kept = {label: [time, label] for time, label in args[0]}; return sorted(kept.values())
    if case_id == "code-18":
        out = {}
        for piece in args[0].split(','):
            if piece.strip():
                key, value = piece.split(':', 1); out[key.strip()] = int(value.strip())
        return out
    if case_id == "code-19":
        values = args[0]
        return next((i for i in range(1, len(values) - 1) if values[i] > values[i - 1] and values[i] > values[i + 1]), -1)
    if case_id == "code-20":
        out = defaultdict(list)
        for month, value in args[0]: out[month].append(value)
        return dict(out)
    if case_id == "code-21":
        rows = args[0]
        if not rows: return []
        out = []
        for start in range(len(rows) + len(rows[0]) - 1):
            word = "".join(rows[r][start - r] for r in range(len(rows)) if 0 <= start - r < len(rows[0]))
            if word: out.append(word)
        return out
    if case_id == "code-22":
        values = args[0]; total = sum(values); left = 0
        for index, value in enumerate(values):
            if left == total: return index
            left += value; total -= value
        return -1
    if case_id == "code-23":
        values = args[0]; return [abs(values[i] - values[(i + 1) % len(values)]) for i in range(len(values))] if values else []
    if case_id == "code-24": return [value for i, value in enumerate(args[0]) if i == 0 or value != args[0][i - 1]]
    if case_id == "code-25":
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}; return sum(-values[c] if i + 1 < len(args[0]) and values[c] < values[args[0][i + 1]] else values[c] for i, c in enumerate(args[0]))
    if case_id == "code-26": return [x for x in args[0] if x < 0] + [x for x in args[0] if x >= 0]
    if case_id == "code-27": return [value for value, count in args[0] for _ in range(count)]
    if case_id == "code-28":
        values = args[0]; first = {0: -1}; balance = best = 0
        for i, value in enumerate(values):
            balance += 1 if value % 2 else -1
            if balance in first: best = max(best, i - first[balance])
            else: first[balance] = i
        return best
    if case_id == "code-29":
        edges, target = args; parents = defaultdict(list)
        for left, right in edges: parents[right].append(left)
        seen = set(); stack = list(parents[target])
        while stack:
            node = stack.pop()
            if node not in seen: seen.add(node); stack.extend(parents[node])
        return sorted(seen)
    if case_id == "code-30":
        parts = []
        for part in args[0].split('/'):
            if part in ('', '.'): continue
            if part == '..':
                if parts: parts.pop()
            else: parts.append(part)
        return '/' + '/'.join(parts)
    if case_id == "code-31":
        latest = {}
        for key, time, value in args[0]:
            if key not in latest or time > latest[key][0]: latest[key] = (time, value)
        return [[key, latest[key][1]] for key in sorted(latest)]
    if case_id == "code-32":
        if args[0] is None: return []
        out = []; queue = deque([args[0]])
        while queue:
            out.append(len(queue))
            for _ in range(len(queue)):
                node = queue.popleft()
                if node[1] is not None: queue.append(node[1])
                if node[2] is not None: queue.append(node[2])
        return out
    if case_id == "code-33":
        nodes, edges = args; graph = {node: [] for node in nodes}
        for left, right in edges: graph[left].append(right); graph[right].append(left)
        color = {}
        for start in nodes:
            if start in color: continue
            color[start] = 0; queue = deque([start])
            while queue:
                node = queue.popleft()
                for child in graph[node]:
                    if child in color and color[child] == color[node]: return False
                    if child not in color: color[child] = 1 - color[node]; queue.append(child)
        return True
    if case_id == "code-34":
        out = []
        for i, value in enumerate(args[0]):
            count = 1
            while i - count >= 0 and args[0][i - count] < value: count += 1
            out.append(count)
        return out
    if case_id == "code-35":
        nodes, edges = args; graph = {node: [] for node in nodes}
        for left, right in edges: graph[left].append(right); graph[right].append(left)
        base = 1 if nodes else 0; out = []
        def components(skip):
            seen = set(); count = 0
            for node in nodes:
                if node == skip or node in seen: continue
                count += 1; stack = [node]; seen.add(node)
                while stack:
                    current = stack.pop()
                    for child in graph[current]:
                        if child != skip and child not in seen: seen.add(child); stack.append(child)
            return count
        for node in sorted(nodes):
            if components(node) > base: out.append(node)
        return out
    if case_id == "code-36":
        nodes, edges = args; parent = {node: node for node in nodes}; total = 0
        def find(node):
            while parent[node] != node: parent[node] = parent[parent[node]]; node = parent[node]
            return node
        for left, right, weight in sorted(edges, key=lambda item: item[2]):
            a, b = find(left), find(right)
            if a != b: parent[a] = b; total += weight
        return total if len({find(node) for node in nodes}) == 1 else None
    if case_id == "code-37":
        words = args[0]; return sum(any(candidate == candidate[::-1] for candidate in (left + right, right + left)) for i, left in enumerate(words) for right in words[i + 1:])
    if case_id == "code-38":
        values, groups = args; n = len(values); dp = [[-10**9] * (groups + 1) for _ in range(n + 1)]; dp[0][0] = 0
        for end in range(1, n + 1):
            product = 1
            for start in range(end, 0, -1):
                product *= values[start - 1]
                for count in range(1, groups + 1): dp[end][count] = max(dp[end][count], dp[start - 1][count - 1] + product)
        return dp[n][groups]
    if case_id == "code-39":
        left, right = args; out = [0] * (len(left) + len(right) - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right): out[i + j] += x * y
        while len(out) > 1 and out[-1] == 0: out.pop()
        return out
    if case_id == "code-40":
        a, b, c, d, e, f = args; determinant = a * d - b * c
        if determinant == 0: return None
        x_num, y_num = e * d - b * f, a * f - e * c
        return [x_num // determinant, y_num // determinant] if x_num % determinant == 0 and y_num % determinant == 0 else None
    if case_id == "code-41":
        rows, cols, start, goal, blocked = args; blocked = {tuple(cell) for cell in blocked}; queue = deque([tuple(start)]); seen = {tuple(start)}; moves = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
        while queue:
            row, col = queue.popleft()
            if [row, col] == goal: return True
            for dr, dc in moves:
                nxt = (row + dr, col + dc)
                if 0 <= nxt[0] < rows and 0 <= nxt[1] < cols and nxt not in blocked and nxt not in seen: seen.add(nxt); queue.append(nxt)
        return False
    if case_id == "code-42":
        text, remove = args; remaining = Counter(remove)
        if any(Counter(remove)[char] > Counter(text)[char] for char in Counter(remove)): return None
        out = []
        for char in text:
            if remaining[char]: remaining[char] -= 1
            else: out.append(char)
        return ''.join(out)
    if case_id == "code-43":
        rows = list(csv.DictReader(io.StringIO(args[0]))); return [{column: row[column] for column in args[1]} for row in rows]
    if case_id == "code-44":
        heights, threshold = args; indexes = [i for i, height in enumerate(heights) if height >= threshold]; return indexes[-1] - indexes[0] if len(indexes) >= 2 else 0
    if case_id == "code-45":
        rotations = [(args[0][i:] + args[0][:i], i) for i in range(len(args[0]))]; return min(rotations)[1] if rotations else 0
    if case_id == "code-46":
        text, word = args; target = Counter(word); return sum(Counter(text[i:i + len(word)]) == target for i in range(len(text) - len(word) + 1))
    if case_id == "code-47":
        words = args[0]
        if not words: return ""
        prefix = words[0]
        for word in words[1:]:
            while not word.startswith(prefix): prefix = prefix[:-1]
        return prefix
    if case_id == "code-48":
        nodes, edges = args; graph = {node: [] for node in nodes}
        for left, right in edges: graph[left].append(right); graph[right].append(left)
        def solve(node, parent):
            without = 0; with_node = 1
            for child in graph[node]:
                if child != parent:
                    child_without, child_with = solve(child, node); without += child_with; with_node += min(child_without, child_with)
            return without, with_node
        return min(solve(nodes[0], None)) if nodes else 0
    raise KeyError(case_id)


def main() -> None:
    math_doc = yaml.safe_load((BENCHMARK / "cases/math.yaml").read_text())
    code_doc = yaml.safe_load((BENCHMARK / "cases/coding.yaml").read_text())
    math_cases, code_cases = math_doc["cases"], code_doc["cases"]
    assert len(math_cases) == len(code_cases) == 48
    assert {c["difficulty"] for c in math_cases} == {"foundational", "intermediate", "advanced"}
    assert {c["difficulty"] for c in code_cases} == {"foundational", "intermediate", "advanced"}
    assert all(sum(c["difficulty"] == d for c in math_cases) == n for d, n in {"foundational": 10, "intermediate": 24, "advanced": 14}.items())
    assert all(sum(c["difficulty"] == d for c in code_cases) == n for d, n in {"foundational": 10, "intermediate": 24, "advanced": 14}.items())

    oracle = yaml.safe_load((BENCHMARK / "oracle-validation.yaml").read_text())["cases"]
    assert len(oracle) == 48 and all(row["status"] == "PASS" for row in oracle)
    for case, row in zip(math_cases, oracle):
        independent = math_reference(case["id"])
        expected = case["expected"]["value"]
        if isinstance(independent, Fraction): independent = f"{independent.numerator}/{independent.denominator}"
        assert independent == expected == row["independently_recomputed"], case["id"]
    print("math oracle validation: 48/48 PASS")

    evaluator = yaml.safe_load((BENCHMARK / "evaluator-validation.yaml").read_text())["cases"]
    assert len(evaluator) == 48 and all(row["status"] == "PASS" for row in evaluator)
    for case, row in zip(code_cases, evaluator):
        assert row["case_id"] == case["id"] and row["test_count"] == len(case["evaluator"]["tests"])
        for test in case["evaluator"]["tests"]:
            if "raises" in test:
                try: coding_reference(case["id"], test["args"])
                except ValueError: continue
                raise AssertionError((case["id"], "expected ValueError"))
            assert coding_reference(case["id"], test["args"]) == test["expected"], (case["id"], test)
    print("coding evaluator validation: 48/48 PASS")

    contract_audit = yaml.safe_load((BENCHMARK / "semantic-contract-audit.yaml").read_text())
    assert contract_audit["result"] == "48/48 PASS"
    assert len(contract_audit["cases"]) == 48
    assert all(row["audit_status"] == "PASS" for row in contract_audit["cases"])
    assert [row["case_id"] for row in contract_audit["cases"]] == [case["id"] for case in code_cases]
    assert [row["entrypoint"] for row in contract_audit["cases"]] == [case["evaluator"]["entrypoint"] for case in code_cases]
    print("coding semantic-contract audit: 48/48 PASS")

    router_dir = ROOT / "experiments/gate-b/router-v2"
    sys.path.insert(0, str(router_dir))
    from router import route_semantic_task  # noqa: E402
    routes = [route_semantic_task(case["semantic_task"]) for case in math_cases + code_cases]
    assert routes == ["mathematics_specialist"] * 48 + ["general_baseline"] * 48
    print("router target benchmark validation: 96/96 PASS")

    token_doc = yaml.safe_load((BENCHMARK / "token_counts.yaml").read_text())
    tokenizer = PreTrainedTokenizerFast(tokenizer_file=str(TOKENIZER_PATH))
    system = "You are a helpful assistant. Follow the task instructions exactly. Use the common handoff contract supplied after the semantic task."
    math_handoff = "Reasoning may be included. Finish with exactly one recoverable final answer: use `ANSWER: value` or one permitted boxed final form. Do not give conflicting final candidates."
    code_handoff = "Explanatory prose may be included. Provide one source block defining the requested entrypoint. A Python or unlabeled fenced block is preferred; do not provide multiple implementation candidates."
    expected_tokens = {row["case_id"]: row["rendered_input_tokens"] for row in token_doc["cases"]}
    for case in math_cases + code_cases:
        handoff = math_handoff if case["domain"] == "mathematics" else code_handoff
        rendered = f"<|im_start|>system\n{system}<|im_end|>\n<|im_start|>user\n{case['semantic_task']}\n\n{handoff}<|im_end|>\n<|im_start|>assistant\n"
        actual = len(tokenizer.encode(rendered, add_special_tokens=False))
        assert actual == expected_tokens[case["id"]], (case["id"], actual, expected_tokens[case["id"]])
        assert actual + 1024 <= 4096
    assert max(expected_tokens.values()) == token_doc["constraints"]["maximum_rendered_input_tokens"]
    print("token/context validation: 96/96 PASS; max=124; margin=2948")


if __name__ == "__main__":
    main()
