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
