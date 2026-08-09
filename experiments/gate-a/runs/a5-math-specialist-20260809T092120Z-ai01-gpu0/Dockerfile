FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HOME=/gate-cache/huggingface \
    TRANSFORMERS_CACHE=/gate-cache/huggingface

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3.10 python3-pip ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir \
      --index-url https://download.pytorch.org/whl/cu121 \
      torch==2.2.2 \
    && python3 -m pip install --no-cache-dir \
      --index-url https://pypi.org/simple \
      transformers==4.41.1 \
      safetensors==0.4.3 \
      accelerate==0.30.1 \
      tokenizers==0.19.1 \
      huggingface-hub==0.23.4 \
      numpy==1.26.4 \
      PyYAML==6.0.1

COPY run_inference.py /opt/gate-a/run_inference.py

ENTRYPOINT ["python3", "/opt/gate-a/run_inference.py"]
