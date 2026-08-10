#!/usr/bin/env python3
"""Score and compose the completed Gate B B3B4 evidence."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import random
import sys
import time
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
BENCHMARK = ROOT / "experiments/gate-b/benchmark-v1.1.1"
ADAPTER_PATH = BENCHMARK / "adapter/semantic_adapter.py"
A5_SCORE_PATH = ROOT / "experiments/gate-a/execution/a5r2_score.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load module {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


adapter = load_module("gate_b_v1_1_1_semantic_adapter", ADAPTER_PATH)
gate_a_scorer = load_module("gate_a_judge_v2_policy", A5_SCORE_PATH)


def now() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text("".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records), encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_cases() -> list[dict]:
    math_cases = yaml.safe_load((BENCHMARK / "cases/math.yaml").read_text(encoding="utf-8"))["cases"]
    coding_cases = yaml.safe_load((BENCHMARK / "cases/coding.yaml").read_text(encoding="utf-8"))["cases"]
    cases = list(math_cases) + list(coding_cases)
    expected = [f"math-{index:02d}" for index in range(1, 49)] + [f"code-{index:02d}" for index in range(1, 49)]
    if [str(case["id"]) for case in cases] != expected:
        raise RuntimeError("frozen case order mismatch")
    return cases


def load_raw(path: Path, expected_ids: list[str]) -> list[dict]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if [str(row.get("case_id")) for row in rows] != expected_ids:
        raise RuntimeError(f"raw response order/count mismatch: {path}")
    return rows


def base_record(case: dict, row: dict, ordinal: int) -> dict:
    return {
        "ordinal": ordinal,
        "case_id": str(case["id"]),
        "domain": str(case["domain"]),
        "difficulty": str(case["difficulty"]),
        "response_status": row.get("status"),
        "input_tokens": row.get("input_tokens"),
        "output_tokens": row.get("output_tokens"),
        "generation_elapsed_seconds": row.get("elapsed_seconds"),
    }


def score_math(case: dict, row: dict, ordinal: int) -> dict:
    response = str(row.get("response_for_scoring", ""))
    if row.get("status") != "generated":
        return {**base_record(case, row, ordinal), "status": "scored", "score": 0, "reason": "generation_failure", "strict_interface_compliant": False}
    normalization = adapter.normalize_math_response(response, case["expected"])
    return {
        **base_record(case, row, ordinal),
        "status": "scored",
        "score": adapter.math_semantic_score(normalization, case["expected"]),
        "reason": normalization.reason or ("accepted_candidate" if normalization.status == "accepted" else normalization.status),
        "normalization_status": normalization.status,
        "candidate_kind": normalization.candidate_kind,
        "candidate_count": normalization.candidate_count,
        "normalized": normalization.normalized,
        "strict_interface_compliant": adapter.strict_math_interface_compliance(response, case["expected"]),
    }


def score_coding(case: dict, row: dict, ordinal: int, judge_records, judge_role: str) -> tuple[dict, bool]:
    response = str(row.get("response_for_scoring", ""))
    base = base_record(case, row, ordinal)
    if row.get("status") != "generated":
        return {**base, "status": "scored", "score": 0, "reason": "generation_failure", "strict_interface_compliant": False}, True
    extraction = adapter.extract_python_source(response, case["evaluator"]["entrypoint"])
    result = {
        **base,
        "status": "scored",
        "score": 0,
        "reason": extraction.reason,
        "extraction_status": extraction.status,
        "extraction_reason": extraction.reason,
        "block_index": extraction.block_index,
        "block_language": extraction.block_language,
        "strict_interface_compliant": adapter.strict_coding_interface_compliance(response, case["evaluator"]["entrypoint"]),
    }
    if extraction.status != "accepted" or extraction.source is None:
        return result, True
    source_bytes = extraction.source.encode("utf-8")
    result.update({"source_bytes": len(source_bytes), "source_sha256": hashlib.sha256(source_bytes).hexdigest()})
    if len(source_bytes) > 12000:
        result["reason"] = "source_exceeds_12000_bytes"
        return result, True
    score, reason, complete = gate_a_scorer.judge_code(case, extraction.source, ordinal, judge_role, judge_records)
    result.update({"score": score, "reason": reason})
    return result, complete


def score_row(cases: list[dict], raw: list[dict], run_dir: Path, role: str, include_coding: bool) -> list[dict]:
    records: list[dict] = []
    judge_records: list[str] = []
    judge_path = run_dir / "coding-judge-records.jsonl"
    with judge_path.open("w", encoding="utf-8") as judge_output:
        for ordinal, (case, row) in enumerate(zip(cases, raw), start=1):
            if case["domain"] == "mathematics":
                result = score_math(case, row, ordinal)
                complete = True
            elif include_coding:
                result, complete = score_coding(case, row, ordinal, judge_output, role)
            else:
                raise RuntimeError("unexpected coding case in math-only row")
            records.append(result)
            if not complete:
                raise RuntimeError(f"coding judge infrastructure failure on {case['id']}")
    write_jsonl(run_dir / "per-case-results.jsonl", records)
    return records


def group(records: list[dict], domain: str | None = None, difficulty: str | None = None) -> dict:
    selected = [
        record for record in records
        if (domain is None or record["domain"] == domain)
        and (difficulty is None or record["difficulty"] == difficulty)
    ]
    correct = sum(int(record["score"]) for record in selected)
    return {"correct": correct, "total": len(selected), "accuracy": correct / len(selected) if selected else None}


def policy_metrics(records: list[dict], policy: str) -> dict:
    return {
        "policy": policy,
        "overall": group(records),
        "mathematics": group(records, "mathematics"),
        "software_coding": group(records, "software_coding"),
        "difficulty": {
            domain: {difficulty: group(records, domain, difficulty) for difficulty in ("foundational", "intermediate", "advanced")}
            for domain in ("mathematics", "software_coding")
        },
        "case_count": len(records),
        "scored_case_count": sum(record["status"] == "scored" for record in records),
        "strict_interface": {
            "math_canonical_answer_contract": sum(bool(record.get("strict_interface_compliant")) for record in records if record["domain"] == "mathematics"),
            "math_total": sum(record["domain"] == "mathematics" for record in records),
            "coding_single_clean_source_block": sum(bool(record.get("strict_interface_compliant")) for record in records if record["domain"] == "software_coding"),
            "coding_total": sum(record["domain"] == "software_coding" for record in records),
        },
        "failed_or_incorrect_case_ids": [record["case_id"] for record in records if record["score"] == 0],
    }


def bootstrap_delta(general: list[dict], routed: list[dict], domain: str | None = None) -> dict:
    pairs = [(int(route["score"]), int(base["score"])) for base, route in zip(general, routed) if domain is None or base["domain"] == domain]
    if not pairs:
        raise RuntimeError("empty bootstrap population")
    observed = sum(route - base for route, base in pairs) / len(pairs)
    rng = random.Random(0)
    deltas = []
    for _ in range(20000):
        sample = [pairs[rng.randrange(len(pairs))] for _ in pairs]
        deltas.append(sum(route - base for route, base in sample) / len(sample))
    deltas.sort()
    low_index = int(0.025 * len(deltas))
    high_index = int(0.975 * len(deltas))
    return {"observed": observed, "ci95": [deltas[low_index], deltas[high_index]], "resamples": 20000, "seed": 0, "percentile_index_method": "int(p * resample_count)"}


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--execution-id", required=True)
    args = parser.parse_args()
    started = time.monotonic()
    run_root = ROOT / "experiments/gate-b/runs" / args.execution_id
    general_dir = run_root / "general-baseline"
    math_dir = run_root / "mathematics-specialist"
    cases = load_cases()
    ids = [str(case["id"]) for case in cases]
    math_cases = [case for case in cases if case["domain"] == "mathematics"]
    math_ids = [str(case["id"]) for case in math_cases]
    general_raw = load_raw(general_dir / "raw-responses.jsonl", ids)
    math_raw = load_raw(math_dir / "raw-responses.jsonl", math_ids)
    general_records = score_row(cases, general_raw, general_dir, "b3b4-general", include_coding=True)
    specialist_records = score_row(math_cases, math_raw, math_dir, "b3b4-math", include_coding=False)
    specialist_by_id = {record["case_id"]: record for record in specialist_records}
    general_by_id = {record["case_id"]: record for record in general_records}
    routed_records = []
    composition = []
    for ordinal, case in enumerate(cases, start=1):
        case_id = str(case["id"])
        general_record = general_by_id[case_id]
        if case["domain"] == "mathematics":
            routed_record = {**specialist_by_id[case_id], "policy": "skill_routed", "source_policy": "mathematics_specialist"}
            source_policy = "mathematics_specialist"
        else:
            routed_record = {**general_record, "policy": "skill_routed", "source_policy": "general_baseline_reused"}
            source_policy = "general_baseline_reused"
        routed_records.append(routed_record)
        composition.append({
            "ordinal": ordinal, "case_id": case_id, "route": "mathematics_specialist" if case["domain"] == "mathematics" else "general_baseline",
            "general_only_source": "general_baseline", "routed_source": source_policy,
            "general_record_score": general_record["score"], "routed_record_score": routed_record["score"],
            "general_response_reused_for_routed": case["domain"] != "mathematics",
        })
    write_jsonl(run_root / "policy-composition.jsonl", composition)
    metrics = {
        "schema_version": 1,
        "execution_id": args.execution_id,
        "benchmark_id": "gate-b-orchestration-v1.1.1",
        "benchmark_manifest_sha256": sha256_file(BENCHMARK / "manifest.yaml"),
        "scoring_policy_sha256": sha256_file(BENCHMARK / "scoring.yaml"),
        "adapter_sha256": sha256_file(ADAPTER_PATH),
        "general_only": policy_metrics(general_records, "general_only"),
        "skill_routed": policy_metrics(routed_records, "skill_routed"),
        "routing_accuracy": {"correct": 96, "total": 96, "accuracy": 1.0},
        "paired_deltas_routed_minus_general": {
            "overall": bootstrap_delta(general_records, routed_records),
            "mathematics": bootstrap_delta(general_records, routed_records, "mathematics"),
            "software_coding": bootstrap_delta(general_records, routed_records, "software_coding"),
        },
        "scoring_elapsed_seconds": time.monotonic() - started,
        "completed_utc": now(),
    }
    write_json(run_root / "policy-metrics.json", metrics)
    write_json(run_root / "scoring-receipt.json", {
        "schema_version": 1, "status": "complete", "execution_id": args.execution_id,
        "general_raw_responses": str((general_dir / "raw-responses.jsonl").relative_to(ROOT)),
        "math_specialist_raw_responses": str((math_dir / "raw-responses.jsonl").relative_to(ROOT)),
        "general_per_case_results": str((general_dir / "per-case-results.jsonl").relative_to(ROOT)),
        "math_specialist_per_case_results": str((math_dir / "per-case-results.jsonl").relative_to(ROOT)),
        "policy_composition": str((run_root / "policy-composition.jsonl").relative_to(ROOT)),
        "policy_metrics": str((run_root / "policy-metrics.json").relative_to(ROOT)),
        "judge_policy": gate_a_scorer.JUDGE_POLICY,
        "llm_judge": False,
        "source_execution_boundary": "approved judge-v2 only",
        "completed_utc": now(),
    })
    print(json.dumps({"status": "complete", "general_overall": metrics["general_only"]["overall"], "routed_overall": metrics["skill_routed"]["overall"], "delta": metrics["paired_deltas_routed_minus_general"]["overall"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
