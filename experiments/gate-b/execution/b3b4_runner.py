#!/usr/bin/env python3
"""Frozen Gate B B3B4 inference runner for one approved checkpoint row."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import random
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import torch
import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer


MAX_NEW_TOKENS = 1024
TOTAL_CONTEXT_TOKENS = 4096
EXPECTED_TEMPLATE_ID = "qwen-neutral-role-delimiter-v1"
EXPECTED_BENCHMARK_ID = "gate-b-orchestration-v1.1.1"


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def package_versions() -> dict[str, str]:
    names = ["torch", "transformers", "safetensors", "accelerate", "tokenizers", "huggingface-hub", "PyYAML"]
    result = {"python": platform.python_version(), "platform": platform.platform()}
    for name in names:
        try:
            result[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            result[name] = "missing"
    result["torch_cuda_build"] = str(torch.version.cuda)
    result["cuda_available"] = str(torch.cuda.is_available())
    result["cuda_device_count"] = str(torch.cuda.device_count())
    return result


def gpu_receipt() -> dict[str, object]:
    query = [
        "nvidia-smi",
        "--query-gpu=index,uuid,name,driver_version,memory.total,memory.used,memory.free,pci.bus_id,utilization.gpu",
        "--format=csv,noheader",
    ]
    result = subprocess.run(query, capture_output=True, check=False, text=True)
    visible = torch.cuda.device_count()
    return {
        "torch_cuda_available": bool(torch.cuda.is_available()),
        "torch_cuda_device_count": visible,
        "torch_device_name": torch.cuda.get_device_name(0) if visible == 1 else None,
        "torch_bfloat16_supported": bool(torch.cuda.is_bf16_supported()) if visible == 1 else False,
        "nvidia_smi": {
            "command": " ".join(query),
            "exit_code": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        },
    }


def load_benchmark(root: Path) -> tuple[list[dict], dict[str, int], str, dict[str, str]]:
    template = yaml.safe_load((root / "template.yaml").read_text(encoding="utf-8"))
    if template["template_id"] != EXPECTED_TEMPLATE_ID:
        raise RuntimeError("unexpected template id")
    if template["benchmark_version"] != EXPECTED_BENCHMARK_ID:
        raise RuntimeError("unexpected template benchmark version")
    math_cases = yaml.safe_load((root / "cases/math.yaml").read_text(encoding="utf-8"))["cases"]
    code_cases = yaml.safe_load((root / "cases/coding.yaml").read_text(encoding="utf-8"))["cases"]
    cases = list(math_cases) + list(code_cases)
    expected_ids = [f"math-{index:02d}" for index in range(1, 49)] + [f"code-{index:02d}" for index in range(1, 49)]
    if [str(case["id"]) for case in cases] != expected_ids:
        raise RuntimeError("frozen case order mismatch")
    token_doc = yaml.safe_load((root / "token_counts.yaml").read_text(encoding="utf-8"))
    token_counts = {str(case["case_id"]): int(case["rendered_input_tokens"]) for case in token_doc["cases"]}
    if set(token_counts) != set(expected_ids):
        raise RuntimeError("token count IDs do not match frozen cases")
    manifest = yaml.safe_load((root / "manifest.yaml").read_text(encoding="utf-8"))
    if manifest["benchmark_id"] != EXPECTED_BENCHMARK_ID:
        raise RuntimeError("unexpected benchmark version")
    handoffs = template["handoff_contracts"]
    return cases, token_counts, str(template["system_content"]), handoffs


def render_prompt(system_content: str, case: dict, handoffs: dict[str, str]) -> str:
    return (
        "<|im_start|>system\n"
        + system_content
        + "<|im_end|>\n"
        + "<|im_start|>user\n"
        + str(case["semantic_task"])
        + "\n\n"
        + str(handoffs[case["domain"]])
        + "<|im_end|>\n"
        + "<|im_start|>assistant\n"
    )


def selected_cases(cases: list[dict], selected_path: Path | None) -> list[dict]:
    if selected_path is None:
        return cases
    selected_ids = [line.strip() for line in selected_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    case_by_id = {str(case["id"]): case for case in cases}
    if len(selected_ids) != len(set(selected_ids)) or any(case_id not in case_by_id for case_id in selected_ids):
        raise RuntimeError("invalid selected case ID file")
    selected = [case_by_id[case_id] for case_id in selected_ids]
    if [str(case["id"]) for case in selected] != selected_ids:
        raise RuntimeError("selected case order mismatch")
    return selected


def validate_tokenizer(model_dir: Path, benchmark_root: Path, cases: list[dict], selected_path: Path | None) -> dict[str, object]:
    all_cases, expected_counts, system_content, handoffs = load_benchmark(benchmark_root)
    selected = selected_cases(all_cases, selected_path)
    tokenizer = AutoTokenizer.from_pretrained(
        str(model_dir), use_fast=True, trust_remote_code=False, local_files_only=True
    )
    observed: dict[str, int] = {}
    for case in selected:
        case_id = str(case["id"])
        rendered = render_prompt(system_content, case, handoffs)
        count = len(tokenizer(rendered, add_special_tokens=False)["input_ids"])
        observed[case_id] = count
        if count != expected_counts[case_id]:
            raise RuntimeError(f"token count mismatch {case_id}: {count} != {expected_counts[case_id]}")
        if count + MAX_NEW_TOKENS > TOTAL_CONTEXT_TOKENS:
            raise RuntimeError(f"context envelope exceeded for {case_id}")
    return {
        "tokenizer_class": tokenizer.__class__.__name__,
        "tokenizer_json_sha256": sha256_file(Path(model_dir) / "tokenizer.json"),
        "template_id": EXPECTED_TEMPLATE_ID,
        "case_count": len(selected),
        "observed_token_counts": observed,
        "max_rendered_input_tokens": max(observed.values()),
        "max_rendered_input_plus_generation_tokens": max(observed.values()) + MAX_NEW_TOKENS,
        "total_context_tokens": TOTAL_CONTEXT_TOKENS,
        "max_new_tokens": MAX_NEW_TOKENS,
    }


def check_gpu() -> dict[str, object]:
    gpu = gpu_receipt()
    if gpu["torch_cuda_device_count"] != 1 or gpu["torch_device_name"] != "NVIDIA L40":
        raise RuntimeError(f"expected one visible NVIDIA L40: {gpu}")
    if not gpu["torch_bfloat16_supported"]:
        raise RuntimeError("BF16 is not supported")
    return gpu


def preflight(args: argparse.Namespace) -> int:
    model_dir = Path(args.model_dir)
    benchmark_root = Path(args.benchmark_root)
    if not model_dir.is_dir():
        raise RuntimeError(f"model directory missing: {model_dir}")
    all_cases, _, _, _ = load_benchmark(benchmark_root)
    selected_path = Path(args.selected_case_ids_file) if args.selected_case_ids_file else None
    selected = selected_cases(all_cases, selected_path)
    gpu = check_gpu()
    token_policy = validate_tokenizer(model_dir, benchmark_root, all_cases, selected_path)
    write_json(
        Path(args.receipt),
        {
            "schema_version": 1,
            "status": "pass",
            "operation": "b3b4_inference_preflight",
            "timestamp_utc": now(),
            "model_id": args.model_id,
            "model_role": args.model_role,
            "model_revision": args.model_revision,
            "model_dir": str(model_dir),
            "selected_case_count": len(selected),
            "dtype": "bfloat16",
            "quantization": "none",
            "external_tools": False,
            "generation_policy": {"max_new_tokens": MAX_NEW_TOKENS, "do_sample": False, "num_beams": 1, "repetition_penalty": 1.0, "seed": 0},
            "package_versions": package_versions(),
            "gpu": gpu,
            "token_policy": token_policy,
        },
    )
    print(f"B3B4_PREFLIGHT_PASS selected={len(selected)}", flush=True)
    return 0


def seed_everything() -> None:
    random.seed(0)
    torch.manual_seed(0)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(0)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def run_model(args: argparse.Namespace) -> int:
    model_dir = Path(args.model_dir)
    benchmark_root = Path(args.benchmark_root)
    output_path = Path(args.raw_output)
    receipt_path = Path(args.receipt)
    all_cases, expected_counts, system_content, handoffs = load_benchmark(benchmark_root)
    selected_path = Path(args.selected_case_ids_file) if args.selected_case_ids_file else None
    cases = selected_cases(all_cases, selected_path)
    seed_everything()
    token_policy = validate_tokenizer(model_dir, benchmark_root, all_cases, selected_path)
    gpu_before = check_gpu()
    load_started = time.monotonic()
    tokenizer = AutoTokenizer.from_pretrained(str(model_dir), use_fast=True, trust_remote_code=False, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        str(model_dir), revision=args.model_revision, torch_dtype=torch.bfloat16, device_map={"": "cuda:0"},
        low_cpu_mem_usage=True, trust_remote_code=False, use_safetensors=True, local_files_only=True,
    )
    model.eval()
    model_dtype = str(next(model.parameters()).dtype)
    model_device = str(next(model.parameters()).device)
    quantized = bool(getattr(model, "is_loaded_in_4bit", False) or getattr(model, "is_loaded_in_8bit", False))
    if model_dtype != "torch.bfloat16" or quantized:
        raise RuntimeError(f"invalid effective model state dtype={model_dtype} quantized={quantized}")
    if gpu_before["torch_cuda_device_count"] != 1 or gpu_before["torch_device_name"] != "NVIDIA L40":
        raise RuntimeError("GPU visibility changed before generation")
    device = next(model.parameters()).device
    output_path.parent.mkdir(parents=True, exist_ok=True)
    generated_records = 0
    failed_records = 0
    with output_path.open("w", encoding="utf-8") as output:
        for ordinal, case in enumerate(cases, start=1):
            case_id = str(case["id"])
            rendered = render_prompt(system_content, case, handoffs)
            encoded = tokenizer(rendered, add_special_tokens=False, return_tensors="pt")
            input_tokens = int(encoded["input_ids"].shape[1])
            if input_tokens != expected_counts[case_id] or input_tokens + MAX_NEW_TOKENS > TOTAL_CONTEXT_TOKENS:
                raise RuntimeError(f"context policy failure for {case_id}")
            encoded = {key: value.to(device) for key, value in encoded.items()}
            started = time.perf_counter()
            record: dict[str, object] = {
                "ordinal": ordinal, "case_id": case_id, "domain": case["domain"], "difficulty": case["difficulty"],
                "input_tokens": input_tokens, "max_new_tokens": MAX_NEW_TOKENS, "started_utc": now(),
                "generation_policy": {"do_sample": False, "num_beams": 1, "repetition_penalty": 1.0, "max_new_tokens": MAX_NEW_TOKENS, "seed": 0},
            }
            try:
                if torch.cuda.is_available():
                    torch.cuda.synchronize()
                with torch.inference_mode():
                    generated = model.generate(**encoded, max_new_tokens=MAX_NEW_TOKENS, do_sample=False, num_beams=1,
                                               repetition_penalty=1.0, pad_token_id=tokenizer.eos_token_id,
                                               eos_token_id=tokenizer.eos_token_id, use_cache=True)
                if torch.cuda.is_available():
                    torch.cuda.synchronize()
                generated_tokens = generated[0, encoded["input_ids"].shape[1]:].detach().cpu().tolist()
                record.update({
                    "status": "generated", "output_tokens": len(generated_tokens),
                    "raw_response": tokenizer.decode(generated_tokens, skip_special_tokens=False, clean_up_tokenization_spaces=False),
                    "response_for_scoring": tokenizer.decode(generated_tokens, skip_special_tokens=True, clean_up_tokenization_spaces=False),
                })
                generated_records += 1
            except Exception as exc:
                record.update({"status": "generation_failed", "error_type": type(exc).__name__, "error_message": str(exc)})
                failed_records += 1
            record["elapsed_seconds"] = time.perf_counter() - started
            output.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            output.flush()
    write_json(
        receipt_path,
        {
            "schema_version": 1, "status": "complete" if failed_records == 0 else "complete_with_case_failures", "timestamp_utc": now(),
            "model_id": args.model_id, "model_role": args.model_role, "model_revision": args.model_revision,
            "benchmark_id": EXPECTED_BENCHMARK_ID, "case_count": len(cases), "generated_records": generated_records,
            "failed_records": failed_records, "load_elapsed_seconds": time.monotonic() - load_started,
            "effective_model_dtype": model_dtype, "effective_model_device": model_device, "quantized": quantized,
            "gpu_before_generation": gpu_before, "package_versions": package_versions(),
            "generation_policy": {"max_new_tokens": MAX_NEW_TOKENS, "do_sample": False, "num_beams": 1, "repetition_penalty": 1.0, "seed": 0, "external_tools": False},
            "token_policy": token_policy, "raw_output": str(output_path),
        },
    )
    print(f"B3B4_INFERENCE_COMPLETE generated={generated_records}/{len(cases)} failed={failed_records}", flush=True)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["preflight", "run"])
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-role", required=True)
    parser.add_argument("--model-revision", required=True)
    parser.add_argument("--model-dir", required=True)
    parser.add_argument("--benchmark-root", default="/benchmark")
    parser.add_argument("--raw-output", default="/run/raw-responses.jsonl")
    parser.add_argument("--receipt", default="/run/inference-receipt.json")
    parser.add_argument("--selected-case-ids-file")
    args = parser.parse_args()
    return preflight(args) if args.mode == "preflight" else run_model(args)


if __name__ == "__main__":
    raise SystemExit(main())
