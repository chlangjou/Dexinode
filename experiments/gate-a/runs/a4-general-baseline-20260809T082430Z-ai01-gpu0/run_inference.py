#!/usr/bin/env python3
"""Pinned, non-interactive Gate A General baseline acquisition and runner."""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.metadata
import json
import os
import platform
import random
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import torch
import yaml
from huggingface_hub import HfApi, snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer, __version__ as transformers_version


MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"
MODEL_REVISION = "a09a35458c702b33eeacc393d103063234e8bc28"
BENCHMARK_VERSION = "gate-a-cross-skill-v1.1.0"
MAX_NEW_TOKENS = 1024
TOTAL_CONTEXT_TOKENS = 4096
SYSTEM_CONTENT = "You are a helpful assistant. Follow the task instructions exactly. Return only the requested answer format."
EXPECTED_TOKEN_COUNTS = {
    # Loaded from token_counts.yaml at runtime; this constant only prevents
    # accidental use of repository chat templates in the rendering function.
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


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


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_inventory(root: Path) -> tuple[list[dict[str, object]], int]:
    entries: list[dict[str, object]] = []
    total = 0
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        size = path.stat().st_size
        total += size
        entries.append({"path": str(path.relative_to(root)), "size_bytes": size, "sha256": sha256_file(path)})
    return entries, total


def nvidia_query() -> dict[str, object]:
    command = [
        "nvidia-smi",
        "--query-gpu=index,uuid,name,driver_version,memory.total,memory.used,memory.free,pci.bus_id,utilization.gpu",
        "--format=csv,noheader",
    ]
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    return {
        "command": " ".join(command),
        "exit_code": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def load_cases(benchmark_root: Path) -> tuple[list[dict[str, object]], dict[str, int]]:
    math_doc = yaml.safe_load((benchmark_root / "cases/math.yaml").read_text(encoding="utf-8"))
    coding_doc = yaml.safe_load((benchmark_root / "cases/coding.yaml").read_text(encoding="utf-8"))
    cases = list(math_doc["cases"]) + list(coding_doc["cases"])
    expected_ids = [f"math-{i:02d}" for i in range(1, 49)] + [f"code-{i:02d}" for i in range(1, 49)]
    actual_ids = [str(case["id"]) for case in cases]
    if actual_ids != expected_ids:
        raise RuntimeError(f"frozen case order mismatch: {actual_ids[:3]} ... {actual_ids[-3:]}")
    token_doc = yaml.safe_load((benchmark_root / "token_counts.yaml").read_text(encoding="utf-8"))
    token_counts = {str(case["id"]): int(case["rendered_input_tokens"]) for case in token_doc["cases"]}
    if set(token_counts) != set(actual_ids):
        raise RuntimeError("token count case IDs do not match frozen cases")
    return cases, token_counts


def render_neutral_prompt(case_prompt: str) -> str:
    return (
        "<|im_start|>system\n"
        + SYSTEM_CONTENT
        + "<|im_end|>\n"
        + "<|im_start|>user\n"
        + case_prompt
        + "<|im_end|>\n"
        + "<|im_start|>assistant\n"
    )


def selected_gpu_preflight() -> dict[str, object]:
    visible_count = torch.cuda.device_count()
    name = torch.cuda.get_device_name(0) if visible_count == 1 else None
    bf16_supported = bool(torch.cuda.is_bf16_supported()) if visible_count == 1 else False
    return {
        "torch_cuda_available": bool(torch.cuda.is_available()),
        "torch_cuda_device_count": visible_count,
        "torch_device_name": name,
        "torch_bfloat16_supported": bf16_supported,
        "nvidia_smi": nvidia_query(),
    }


def tokenizer_preflight(model_dir: Path, benchmark_root: Path) -> dict[str, object]:
    tokenizer = AutoTokenizer.from_pretrained(
        str(model_dir),
        use_fast=True,
        trust_remote_code=False,
        local_files_only=True,
    )
    cases, expected_counts = load_cases(benchmark_root)
    observed: dict[str, int] = {}
    for case in cases:
        rendered = render_neutral_prompt(str(case["prompt"]))
        count = len(tokenizer(rendered, add_special_tokens=False)["input_ids"])
        observed[str(case["id"])] = count
        if count != expected_counts[str(case["id"])]:
            raise RuntimeError(
                f"frozen token count mismatch for {case['id']}: observed={count} expected={expected_counts[str(case['id'])]}"
            )
        if count + MAX_NEW_TOKENS > TOTAL_CONTEXT_TOKENS:
            raise RuntimeError(f"context envelope exceeded for {case['id']}")
    return {
        "tokenizer_class": tokenizer.__class__.__name__,
        "use_fast_tokenizer": True,
        "trust_remote_code": False,
        "add_special_tokens": False,
        "template_id": "qwen-neutral-role-delimiter-v1",
        "system_content": SYSTEM_CONTENT,
        "case_count": len(cases),
        "observed_token_counts": observed,
        "max_rendered_input_tokens": max(observed.values()),
        "max_rendered_input_plus_generation_tokens": max(observed.values()) + MAX_NEW_TOKENS,
        "total_context_tokens": TOTAL_CONTEXT_TOKENS,
        "max_new_tokens": MAX_NEW_TOKENS,
    }


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def acquire(args: argparse.Namespace) -> None:
    model_dir = Path(args.model_dir)
    cache_dir = Path(args.hf_cache)
    model_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    api = HfApi()
    info_before = api.model_info(MODEL_ID, revision=MODEL_REVISION)
    if info_before.sha != MODEL_REVISION:
        raise RuntimeError(f"Hugging Face revision resolution mismatch: {info_before.sha}")
    started = time.time()
    snapshot_path = snapshot_download(
        repo_id=MODEL_ID,
        revision=MODEL_REVISION,
        cache_dir=str(cache_dir),
        local_dir=str(model_dir),
        local_dir_use_symlinks=False,
        allow_patterns=["*.json", "*.txt", "*.safetensors", "LICENSE", "README.md"],
    )
    info_after = api.model_info(MODEL_ID, revision=MODEL_REVISION)
    if info_after.sha != MODEL_REVISION:
        raise RuntimeError(f"Hugging Face revision changed or did not resolve exactly: {info_after.sha}")
    files, total = file_inventory(model_dir)
    write_json(
        Path(args.receipt),
        {
            "schema_version": 1,
            "status": "pass",
            "operation": "general_model_acquisition",
            "timestamp_utc": utc_now(),
            "model_id": MODEL_ID,
            "requested_revision": MODEL_REVISION,
            "resolved_revision_before_download": info_before.sha,
            "resolved_revision_after_download": info_after.sha,
            "snapshot_path": snapshot_path,
            "model_dir": str(model_dir),
            "hf_cache": str(cache_dir),
            "download_elapsed_seconds": time.time() - started,
            "artifact_file_count": len(files),
            "artifact_total_bytes": total,
            "files": files,
            "package_versions": package_versions(),
        },
    )
    print(f"ACQUISITION_PASS revision={info_after.sha} files={len(files)} bytes={total}", flush=True)


def preflight(args: argparse.Namespace) -> None:
    model_dir = Path(args.model_dir)
    benchmark_root = Path(args.benchmark_root)
    gpu = selected_gpu_preflight()
    if gpu["torch_cuda_device_count"] != 1:
        raise RuntimeError(f"expected one CUDA device, observed {gpu['torch_cuda_device_count']}")
    if gpu["torch_device_name"] != "NVIDIA L40":
        raise RuntimeError(f"unexpected visible GPU {gpu['torch_device_name']}")
    if not gpu["torch_bfloat16_supported"]:
        raise RuntimeError("BF16 is not supported by the selected device")
    token_policy = tokenizer_preflight(model_dir, benchmark_root)
    write_json(
        Path(args.receipt),
        {
            "schema_version": 1,
            "status": "pass",
            "operation": "inference_preflight_before_formal_generation",
            "timestamp_utc": utc_now(),
            "host_identity_from_container": {"hostname": platform.node(), "platform": platform.platform()},
            "model_id": MODEL_ID,
            "model_revision": MODEL_REVISION,
            "dtype": "bfloat16",
            "quantization": "none",
            "trust_remote_code": False,
            "external_tools": False,
            "generation_policy": {
                "max_new_tokens": MAX_NEW_TOKENS,
                "do_sample": False,
                "num_beams": 1,
                "repetition_penalty": 1.0,
                "seed": 0,
            },
            "package_versions": package_versions(),
            "gpu": gpu,
            "token_policy": token_policy,
        },
    )
    print("INFERENCE_PREFLIGHT_PASS devices=1 template=qwen-neutral-role-delimiter-v1", flush=True)


def seed_everything() -> None:
    random.seed(0)
    torch.manual_seed(0)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(0)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


def run_model(args: argparse.Namespace) -> None:
    model_dir = Path(args.model_dir)
    benchmark_root = Path(args.benchmark_root)
    output_path = Path(args.raw_output)
    cases, expected_counts = load_cases(benchmark_root)
    seed_everything()
    load_started = time.time()
    tokenizer = AutoTokenizer.from_pretrained(
        str(model_dir), use_fast=True, trust_remote_code=False, local_files_only=True
    )
    model = AutoModelForCausalLM.from_pretrained(
        str(model_dir),
        revision=MODEL_REVISION,
        torch_dtype=torch.bfloat16,
        device_map={"": "cuda:0"},
        low_cpu_mem_usage=True,
        trust_remote_code=False,
        use_safetensors=True,
        local_files_only=True,
    )
    model.eval()
    model_dtype = str(next(model.parameters()).dtype)
    model_device = str(next(model.parameters()).device)
    quantized = bool(getattr(model, "is_loaded_in_4bit", False) or getattr(model, "is_loaded_in_8bit", False))
    if model_dtype != "torch.bfloat16":
        raise RuntimeError(f"effective model dtype was {model_dtype}")
    if quantized:
        raise RuntimeError("quantized model state detected")
    load_elapsed = time.time() - load_started
    gpu_before = selected_gpu_preflight()
    if gpu_before["torch_cuda_device_count"] != 1 or gpu_before["torch_device_name"] != "NVIDIA L40":
        raise RuntimeError("GPU visibility changed before formal generation")
    device = next(model.parameters()).device
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as output:
        for number, case in enumerate(cases, start=1):
            case_id = str(case["id"])
            rendered = render_neutral_prompt(str(case["prompt"]))
            encoded = tokenizer(rendered, add_special_tokens=False, return_tensors="pt")
            input_tokens = int(encoded["input_ids"].shape[1])
            if input_tokens != expected_counts[case_id] or input_tokens + MAX_NEW_TOKENS > TOTAL_CONTEXT_TOKENS:
                raise RuntimeError(f"context policy failure for {case_id}")
            encoded = {key: value.to(device) for key, value in encoded.items()}
            started_utc = utc_now()
            started = time.perf_counter()
            record: dict[str, object] = {
                "ordinal": number,
                "case_id": case_id,
                "domain": case["domain"],
                "difficulty": case["difficulty"],
                "input_tokens": input_tokens,
                "max_new_tokens": MAX_NEW_TOKENS,
                "started_utc": started_utc,
                "generation_policy": {
                    "do_sample": False,
                    "num_beams": 1,
                    "repetition_penalty": 1.0,
                    "max_new_tokens": MAX_NEW_TOKENS,
                    "seed": 0,
                },
            }
            try:
                if torch.cuda.is_available():
                    torch.cuda.synchronize()
                with torch.inference_mode():
                    generated = model.generate(
                        **encoded,
                        max_new_tokens=MAX_NEW_TOKENS,
                        do_sample=False,
                        num_beams=1,
                        repetition_penalty=1.0,
                        pad_token_id=tokenizer.eos_token_id,
                        eos_token_id=tokenizer.eos_token_id,
                        use_cache=True,
                    )
                if torch.cuda.is_available():
                    torch.cuda.synchronize()
                generated_tokens = generated[0, encoded["input_ids"].shape[1] :].detach().cpu().tolist()
                raw_response = tokenizer.decode(
                    generated_tokens, skip_special_tokens=False, clean_up_tokenization_spaces=False
                )
                scoring_response = tokenizer.decode(
                    generated_tokens, skip_special_tokens=True, clean_up_tokenization_spaces=False
                )
                record.update(
                    {
                        "status": "generated",
                        "output_tokens": len(generated_tokens),
                        "raw_response": raw_response,
                        "response_for_scoring": scoring_response,
                    }
                )
            except Exception as exc:  # preserve a per-case failure and continue the complete matrix
                record.update(
                    {
                        "status": "generation_failed",
                        "error_type": type(exc).__name__,
                        "error_message": str(exc),
                    }
                )
            record["elapsed_seconds"] = time.perf_counter() - started
            output.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            output.flush()
            print(f"CASE {number}/96 {case_id} status={record['status']} elapsed={record['elapsed_seconds']:.3f}s", flush=True)
    generated_records = sum(1 for line in output_path.read_text(encoding="utf-8").splitlines() if '"status": "generated"' in line)
    write_json(
        Path(args.execution_receipt),
        {
            "schema_version": 1,
            "status": "complete" if generated_records == 96 else "complete_with_case_failures",
            "timestamp_utc": utc_now(),
            "model_id": MODEL_ID,
            "model_revision": MODEL_REVISION,
            "benchmark_version": BENCHMARK_VERSION,
            "case_count": len(cases),
            "generated_records": generated_records,
            "load_elapsed_seconds": load_elapsed,
            "effective_model_dtype": model_dtype,
            "effective_model_device": model_device,
            "quantized": quantized,
            "gpu_before_generation": gpu_before,
            "package_versions": package_versions(),
            "generation_policy": {
                "max_new_tokens": MAX_NEW_TOKENS,
                "do_sample": False,
                "num_beams": 1,
                "repetition_penalty": 1.0,
                "seed": 0,
                "external_tools": False,
            },
            "raw_output": str(output_path),
        },
    )
    print(f"INFERENCE_COMPLETE generated={generated_records}/96", flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["acquire", "preflight", "run"])
    parser.add_argument("--model-dir", default="/gate-cache/models/qwen2.5-7b-instruct")
    parser.add_argument("--hf-cache", default="/gate-cache/huggingface")
    parser.add_argument("--benchmark-root", default="/benchmark")
    parser.add_argument("--receipt", default="/run/acquisition.json")
    parser.add_argument("--raw-output", default="/run/raw-responses.jsonl")
    parser.add_argument("--execution-receipt", default="/run/inference-execution.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.mode == "acquire":
        acquire(args)
    elif args.mode == "preflight":
        preflight(args)
    else:
        run_model(args)


if __name__ == "__main__":
    main()
