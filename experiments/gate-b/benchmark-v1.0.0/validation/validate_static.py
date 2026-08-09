"""Independent standard-library validation of Gate B coding evaluator fixtures."""

from __future__ import annotations

import csv
import heapq
import io
import re
from collections import Counter, defaultdict, deque
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[4]
CASES = yaml.safe_load((ROOT / "experiments/gate-b/benchmark-v1.0.0/cases/coding.yaml").read_text())['cases']


def ref(case_id, args):
    if case_id == "code-01":
        value, low, high = args
        return max(low, min(high, value))
    if case_id == "code-02":
        return sum(ch.casefold() in "aeiou" for ch in args[0])
    if case_id == "code-03":
        values, shift = args
        return values[shift % len(values):] + values[:shift % len(values)] if values else []
    if case_id == "code-04":
        clean = "".join(ch.casefold() for ch in args[0] if ch.isalnum())
        return clean == clean[::-1]
    if case_id == "code-05":
        return sum(row[i] for i, row in enumerate(args[0])) if args[0] else 0
    if case_id == "code-06":
        return sorted(set(args[0]) | set(args[1]))
    if case_id == "code-07":
        values, size = args
        return [values[i:i + size] for i in range(0, len(values), size)]
    if case_id == "code-08":
        value = args[0]
        return "freezing" if value <= 0 else "cold" if value <= 15 else "mild" if value <= 25 else "hot"
    if case_id == "code-09":
        digits = str(abs(args[0]))
        return dict(sorted(Counter(digits).items()))
    if case_id == "code-10":
        counts = Counter(args[0])
        return next((ch for ch in args[0] if counts[ch] == 1), "")
    if case_id in {"code-11", "code-23"}:
        intervals = sorted(args[0])
        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
    if case_id == "code-12":
        items, k = args
        counts = Counter(items)
        first = {value: items.index(value) for value in counts}
        return sorted(counts, key=lambda value: (-counts[value], first[value]))[:k]
    if case_id == "code-13":
        stack = []
        for token in args[0]:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue
            right, left = stack.pop(), stack.pop()
            if token == "+": stack.append(left + right)
            elif token == "-": stack.append(left - right)
            elif token == "*": stack.append(left * right)
            else: stack.append(int(left / right))
        return stack[0]
    if case_id == "code-14":
        groups, positions = {}, {}
        for index, word in enumerate(args[0]):
            key = "".join(sorted(word))
            groups.setdefault(key, []).append(word)
            positions.setdefault(key, index)
        return [sorted(groups[key]) for key in sorted(groups, key=positions.get)]
    if case_id == "code-15":
        return [list(column) for column in zip(*args[0])]
    if case_id == "code-16":
        result = {}
        for field in args[0].split(";"):
            if field.strip() and "=" in field:
                key, value = field.split("=", 1)
                result[key.strip()] = value.strip()
        return result
    if case_id == "code-17":
        values = args[0]
        if not values: return 0
        best = current = 1
        for left, right in zip(values, values[1:]):
            current = current + 1 if right > left else 1
            best = max(best, current)
        return best
    if case_id == "code-18":
        stack, pairs = [], {")": "(", "]": "[", "}": "{"
        }
        for char in args[0]:
            if char in "([{": stack.append(char)
            elif char in pairs and (not stack or stack.pop() != pairs[char]): return False
        return not stack
    if case_id == "code-19":
        matrix = args[0]
        return [list(column) for column in zip(*matrix[::-1])]
    if case_id == "code-20":
        coefficients, x = args
        value = 0
        for coefficient in reversed(coefficients): value = value * x + coefficient
        return value
    if case_id == "code-21":
        records, key = args
        seen, result = set(), []
        for record in records:
            if record[key] not in seen:
                seen.add(record[key]); result.append(record.copy())
        return result
    if case_id == "code-22":
        grid, start, goal = args
        queue, seen = deque([(start[0], start[1], 0)]), {(start[0], start[1])}
        while queue:
            row, col, distance = queue.popleft()
            if [row, col] == goal: return distance
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not grid[nr][nc] and (nr, nc) not in seen:
                    seen.add((nr, nc)); queue.append((nr, nc, distance + 1))
        return -1
    if case_id == "code-24":
        words, width = args
        lines, current = [], ""
        for word in words:
            if current and len(current) + 1 + len(word) > width:
                lines.append(current); current = word
            else:
                current = word if not current else current + " " + word
        if current: lines.append(current)
        return lines
    if case_id == "code-25":
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return sum((-values[ch] if i + 1 < len(args[0]) and values[ch] < values[args[0][i + 1]] else values[ch]) for i, ch in enumerate(args[0]))
    if case_id == "code-26":
        return [value for value in args[0] if value >= 0] + [value for value in args[0] if value < 0]
    if case_id == "code-27":
        return "".join(char * count for char, count in args[0])
    if case_id == "code-28":
        values, target = args
        total = answer = 0
        counts = {0: 1}
        for value in values:
            total += value; answer += counts.get(total - target, 0); counts[total] = counts.get(total, 0) + 1
        return answer
    if case_id == "code-29":
        nodes, edges = args
        graph = {node: [] for node in nodes}; indegree = {node: 0 for node in nodes}
        for left, right in edges: graph[left].append(right); indegree[right] += 1
        ready = [node for node in nodes if indegree[node] == 0]; heapq.heapify(ready); order = []
        while ready:
            node = heapq.heappop(ready); order.append(node)
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0: heapq.heappush(ready, child)
        return order
    if case_id == "code-30":
        parts = []
        for part in args[0].split("/"):
            if part in ("", "."): continue
            if part == "..":
                if parts: parts.pop()
            else: parts.append(part)
        return "/" + "/".join(parts)
    if case_id == "code-31":
        values = sorted(args[0] + args[1]); middle = len(values) // 2
        return float(values[middle]) if len(values) % 2 else (values[middle - 1] + values[middle]) / 2.0
    if case_id == "code-32":
        pieces = [piece for piece in args[0].split("_") if piece]
        return pieces[0] + "".join(piece[:1].upper() + piece[1:] for piece in pieces[1:])
    if case_id == "code-33":
        if not args[0]: return ""
        prefix = args[0][0]
        for word in args[0][1:]:
            while not word.startswith(prefix): prefix = prefix[:-1]
        return prefix
    if case_id == "code-34":
        values, queries = args
        return [sum(values[left:right + 1]) for left, right in queries]
    if case_id == "code-35":
        source, target = args
        row = list(range(len(target) + 1))
        for i, left in enumerate(source, 1):
            current = [i]
            for j, right in enumerate(target, 1):
                current.append(min(current[-1] + 1, row[j] + 1, row[j - 1] + (left != right)))
            row = current
        return row[-1]
    if case_id == "code-36":
        graph, start, goal = args
        heap, best = [(0, [start], start)], {}
        while heap:
            distance, path, node = heapq.heappop(heap)
            if node in best: continue
            best[node] = (distance, path)
            if node == goal: return [distance, path]
            for child, weight in graph.get(node, []):
                if child not in best: heapq.heappush(heap, (distance + weight, path + [child], child))
        return [-1, []]
    if case_id == "code-37":
        return sum(1 for _ in []) if not args[0] else _schedule(args[0])
    if case_id == "code-38":
        table = [0] * (args[1] + 1)
        for weight, value in args[0]:
            for capacity in range(args[1], weight - 1, -1): table[capacity] = max(table[capacity], table[capacity - weight] + value)
        return table[-1]
    if case_id == "code-39":
        left, right = args
        result = [0] * (len(left) + len(right) - 1)
        for i, first in enumerate(left):
            for j, second in enumerate(right): result[i + j] += first * second
        while len(result) > 1 and result[-1] == 0: result.pop()
        return result
    if case_id == "code-40":
        a, b, c, d, e, f = args
        determinant = a * d - b * c
        return {"x": (e * d - b * f) // determinant, "y": (a * f - e * c) // determinant}
    if case_id == "code-41":
        grid = [row[:] for row in args[0]]; count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 1: continue
                count += 1; queue = [(row, col)]; grid[row][col] = 0
                for current in queue:
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = current[0] + dr, current[1] + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                            grid[nr][nc] = 0; queue.append((nr, nc))
        return count
    if case_id == "code-42":
        text, target = args; need = Counter(target); have = Counter(); left = 0; missing = len(target); best = ""
        for right, char in enumerate(text):
            have[char] += 1
            if have[char] <= need[char]: missing -= 1
            while missing == 0:
                candidate = text[left:right + 1]
                if not best or len(candidate) < len(best): best = candidate
                have[text[left]] -= 1
                if have[text[left]] < need[text[left]]: missing += 1
                left += 1
        return best
    if case_id == "code-43":
        reader = csv.DictReader(io.StringIO(args[0])); return [dict(row) for row in reader]
    if case_id == "code-44":
        heights = args[0] + [0]; stack = []; best = 0
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                top = stack.pop(); left = stack[-1] + 1 if stack else 0; best = max(best, heights[top] * (index - left))
            stack.append(index)
        return best
    if case_id == "code-45":
        values = args[0]; best = (values[0], 0, 0)
        for left in range(len(values)):
            total = 0
            for right in range(left, len(values)):
                total += values[right]
                candidate = (total, left, right)
                if candidate[0] > best[0] or (candidate[0] == best[0] and candidate[1:] < best[1:]): best = candidate
        return list(best)
    if case_id == "code-46":
        board = args[0]
        groups = list(board) + [[board[row][col] for row in range(9)] for col in range(9)]
        groups += [[board[row][col] for row in range(box_row, box_row + 3) for col in range(box_col, box_col + 3)] for box_row in range(0, 9, 3) for box_col in range(0, 9, 3)]
        return all(len([value for value in group if value]) == len(set(value for value in group if value)) for group in groups)
    if case_id == "code-47":
        prime = [True] * (args[0] + 1)
        if args[0] >= 0: prime[0] = False
        if args[0] >= 1: prime[1] = False
        for value in range(2, int(args[0] ** 0.5) + 1):
            if prime[value]: prime[value * value::value] = [False] * len(prime[value * value::value])
        return [value for value, is_prime in enumerate(prime) if is_prime]
    if case_id == "code-48":
        coins, amount = args; best = [0] + [amount + 1] * amount
        for value in range(1, amount + 1):
            best[value] = min((best[value - coin] + 1 for coin in coins if coin <= value), default=amount + 1)
        return -1 if best[amount] > amount else best[amount]
    raise KeyError(case_id)


def _schedule(intervals):
    finish = -float("inf"); count = 0
    for start, end in sorted(intervals, key=lambda pair: (pair[1], pair[0])):
        if start >= finish:
            count += 1; finish = end
    return count


def exact_equal(actual, expected):
    if type(actual) is not type(expected): return False
    if isinstance(expected, dict): return actual.keys() == expected.keys() and all(exact_equal(actual[key], expected[key]) for key in expected)
    if isinstance(expected, list): return len(actual) == len(expected) and all(exact_equal(a, e) for a, e in zip(actual, expected))
    return actual == expected


def main():
    failures = []
    for case in CASES:
        for index, test in enumerate(case["evaluator"]["tests"]):
            actual = ref(case["id"], test["args"])
            if not exact_equal(actual, test["expected"]): failures.append((case["id"], index, actual, test["expected"]))
    if failures:
        for failure in failures: print(failure)
        return 1
    print(f"coding evaluator validation: {len(CASES)}/48 cases, {sum(len(c['evaluator']['tests']) for c in CASES)} tests PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
