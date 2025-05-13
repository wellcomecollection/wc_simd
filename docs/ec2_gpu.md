
# EC2 GPU

## AMI

Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.6.0 (Ubuntu 22.04) 20250427

AMI ID: ami-0ce5dea9067b2595f

Instance type: g5.2xlarge

## Host LLM

```sh
pip install uv
uv pip install vllm==0.8.4
uv run vllm serve Qwen/Qwen3-30B-A3B-GPTQ-Int4 --max-model-len 24000
```

Note `max-model-len` is set to 24000 so that it fits on the Nvidia A10 24GB card.

## Test

From the remote terminal run:

```sh
curl <http://localhost:8000/v1/completions>     -H "Content-Type: application/json"     -d '{
        "model": "Qwen/Qwen3-30B-A3B-GPTQ-Int4",
        "prompt": "San Francisco is a",
        "max_tokens": 256,
        "temperature": 0
    }'
```
