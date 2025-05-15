# OCR Notes

- [Using Amazon Bedrock for titling, commenting, and OCR (Optical Character Recognition) with Claude 3.7 Sonnet](https://hidekazu-konishi.com/entry/amazon_bedrock_for_titling_commenting_ocr_with_claude3-7_sonnet.html)

## Boards

- [Catalog Adventures With Contemporary OCR (2025)](https://miro.com/app/board/uXjVI4MKIKE=/?share_link_id=705877639469)

## VLMs

- [Test drive Qwen2.5-VL-32B-Instruct](https://huggingface.co/spaces/Qwen/Qwen2.5-VL-32B-Instruct)
- [OpenVLM Leaderboard](https://huggingface.co/spaces/opencompass/open_vlm_leaderboard)
- [Qwen-2.5-72b is now the best open source OCR model](https://www.reddit.com/r/LocalLLaMA/comments/1jm4agx/qwen2572b_is_now_the_best_open_source_ocr_model/)
- [olmOCR - The Open OCR System](https://www.youtube.com/watch?v=38loqDtlLok)

## Notes

- Qwen2.5-VL-32B quantized to 4-bit cannot fit into 24GB VRAM, so the 7B version was used.

## Costs

### Claude Sonnet 3.7

For text, Claude 3.7 Sonnet has the same price as its predecessors \$3 per million input tokens and $15 per million output tokens—which includes thinking tokens. [(Ref)](https://www.anthropic.com/news/claude-3-7-sonnet)

#### Vision Sizes

| Aspect ratio | Image size |
| ------------ | ---------- |
| 1:1 | 1092x1092 px |
| 3:4 | 951x1268 px |
| 2:3 | 896x1344 px |
| 9:16 | 819x1456 px |
| 1:2 | 784x1568 px |

#### Vision Cost [(Ref)](https://docs.anthropic.com/en/docs/build-with-claude/vision)

| Image size | # of Tokens | Cost / image | Cost / 1K images |
| --- | --- | --- | --- |
| 200x200 px(0.04 megapixels) | ~54 | ~$0.00016 | ~$0.16 |
| 1092x1092 px (1.19 megapixels) | ~1590 | ~$0.0048 | ~$4.80 |

See: [Vision Limitations](https://docs.anthropic.com/en/docs/build-with-claude/vision#limitations)
