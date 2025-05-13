# LLM Notes

By: @danniesim

## Hosting LLMs

- [Looks like SGLang takes the lead in easy of use and performance](https://medium.com/@occlubssk/llm-inference-engines-performance-testing-sglang-vs-vllm-cfd2a597852a)
  - I was a fan of TGI, llama.cpp and VLLM before.
  - [TGI now supports vLLM as a backend](https://huggingface.co/blog/tgi-multi-backend)

- [EC2 Nvidia GPU Instances](https://www.vantage.sh/blog/aws-ec2-gpu-instances-g-family-vs-p-family-g4dn?utm_campaign=Instances%20Blog%20Clicks&utm_source=instances&utm_content=gpu)
  - [g5 instances](https://instances.vantage.sh/aws/ec2/g5.12xlarge) start from US$1/hr for 24GB VRAM

- [Inf2 instances](https://instances.vantage.sh/aws/ec2/inf2.8xlarge) are purpose built for deep learning (DL) inference. They deliver high performance at the lowest cost in Amazon EC2 for generative artificial intelligence (AI) models
  - [Hugging Face Text Generation Inference available for AWS Inferentia2](https://huggingface.co/blog/text-generation-inference-on-inferentia2)
  - [How to run Qwen 2.5 on AWS AI chips using Hugging Face libraries](https://aws.amazon.com/blogs/machine-learning/how-to-run-qwen-2-5-on-aws-ai-chips-using-hugging-face-libraries/)
  - [Hugging Face Optimum Neuron Docs](https://huggingface.co/docs/optimum-neuron/en/index)
  - **NOTE: Requires compilation of models into Inferentia**

## Benchmarks

- [Compared performance of vLLM vs SGLang on 2 Nvidia GPUs - SGLang crushes it with Data Parallelism](https://www.reddit.com/r/LocalLLaMA/comments/1jjl45h/compared_performance_of_vllm_vs_sglang_on_2/)
- [Qwen 3 vs DeepSeek R1: Complete comparison](https://dev.to/composiodev/qwen-3-vs-deep-seek-r1-evaluation-notes-1bi1)

## Model Cards

- [Qwen3-30B-A3B-GPTQ-Int4](https://huggingface.co/Qwen/Qwen3-30B-A3B-GPTQ-Int4)

## Why is VLLM faster than running Hugging Face Transformers in Python?

vLLM achieves much higher inference speeds than a vanilla Hugging Face Transformers setup in Python by introducing several key systems-level and kernel-level optimizations:

1. **Near-Optimal KV-Cache Memory Management**  
   Traditional Transformers implementations waste **60–80%** of the GPU memory reserved for the key-value (KV) cache; vLLM’s **PagedAttention** algorithm partitions KV cache into small “pages,” reducing waste to under **4%**.  This drastic reduction in fragmentation lets you batch far more requests in the same GPU memory footprint, boosting throughput dramatically  [oai_citation:0‡Medium](https://medium.com/%40asimsultan2/vllm-a-deep-dive-into-efficient-llm-inference-and-serving-17804bf047df) [oai_citation:1‡RunPod Blog](https://blog.runpod.io/introduction-to-vllm-and-how-to-run-vllm-on-runpod-serverless/).

2. **Dynamic Scheduling & Chunked Prefill**  
   vLLM distinguishes between **compute-bound prefill** (building the KV cache for the prompt) and **memory-bound decode** (generating new tokens), and batches them together in an order that maximizes GPU utilization.  Its **chunked prefill** feature automatically splits large prefill jobs into smaller chunks interleaved with decode work, slashing both latency and end-to-end token-generation time  [oai_citation:2‡vLLM](https://docs.vllm.ai/en/latest/performance/optimization.html?utm_source=chatgpt.com).

3. **Specialized, Fused GPU Kernels**  
   Rather than relying on generic PyTorch operators, vLLM leverages highly-optimized, fused attention kernels (e.g. FlashAttention2 via Triton) and other C++/Triton routines.  By consolidating multiple tensor operations into single GPU kernels, it reduces global memory traffic and kernel-launch overhead by orders of magnitude  [oai_citation:3‡Medium](https://medium.com/%40asimsultan2/vllm-a-deep-dive-into-efficient-llm-inference-and-serving-17804bf047df) [oai_citation:4‡Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1fwde4t/why_is_transformers_library_w_huggingface_so_slow/?utm_source=chatgpt.com).

4. **Minimal Python-Level Overhead**  
   Hugging Face’s `pipeline` or `model.generate()` loops incur a Python interpreter call for each token (and often re-prefill the entire sequence), which adds significant latency as the sequence grows.  vLLM pushes almost all per-token work into compiled code, using an **incremental KV cache** to avoid redundant computation and minimizing CPU–GPU synchronization  [oai_citation:5‡Hugging Face](https://huggingface.co/docs/transformers/main/en/llm_optims?utm_source=chatgpt.com) [oai_citation:6‡Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1fwde4t/why_is_transformers_library_w_huggingface_so_slow/?utm_source=chatgpt.com).

5. **Real-World Benchmarks**  
   In head-to-head tests on models like LLaMA-7B and LLaMA-13B, vLLM sustains **14×–24× higher throughput** than Hugging Face Transformers, and even outpaces Hugging Face’s own Text Generation Inference (TGI) by up to **3.5×**  [oai_citation:7‡Medium](https://medium.com/%40asimsultan2/vllm-a-deep-dive-into-efficient-llm-inference-and-serving-17804bf047df) [oai_citation:8‡RunPod Blog](https://blog.runpod.io/introduction-to-vllm-and-how-to-run-vllm-on-runpod-serverless/).

---

**Bottom line:** by combining smart memory paging, adaptive batching, fused GPU kernels, and a lean Python footprint, vLLM transforms the standard Hugging Face inference workflow into a hyper‐efficient engine—delivering real-time throughput that vanilla Python pipelines simply can’t match.
