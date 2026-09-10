# Sources: RAG vs fine-tuning vs prompt engineering: which do you need?

Researched via web search (direct fetch of gov.uk/openai.com/arxiv.org was blocked by this session's network egress policy; figures below are taken from search-tool synthesis of the primary pages, cross-checked across multiple independent hits where possible). Flagging this constraint for Tom: none of these figures were fabricated, but none were independently re-fetched and re-read in full either. Worth a spot check before wide reliance.

1. **Ovadia, O. et al., "Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs"**
   URL: https://arxiv.org/abs/2312.05934 (also published as ACL Anthology 2024.emnlp-main.15, EMNLP 2024)
   Accessed: 2026-09-10
   Supports: "RAG consistently outperforms unsupervised fine-tuning, both for existing knowledge encountered during training and entirely new knowledge" (blockquote), and the explanation of why (fine-tuning bakes facts into weights, sensitive to phrasing; RAG grounds at answer time).

2. **OpenAI, "Deprecations"**
   URL: https://developers.openai.com/api/docs/deprecations
   Accessed: 2026-09-10
   Supports: the fine-tuning platform wind-down timeline — notified 7 May 2026, new-starter block from that date, 2 July 2026 widening to accounts inactive 60+ days, 6 January 2027 full stop on new fine-tuning jobs for all customers.

3. **OpenAI, "Pricing"**
   URL: https://developers.openai.com/api/docs/pricing
   Accessed: 2026-09-10
   Supports: standard supervised fine-tuning training cost for GPT-4.1/GPT-4o at $25 per 1M training tokens; o4-mini reinforcement fine-tuning training compute at $100/hour.

4. **AWS, fine-tuning for Claude 3 Haiku in Amazon Bedrock (AWS News Blog / ML Blog)**
   URL: https://aws.amazon.com/blogs/aws/fine-tuning-for-anthropics-claude-3-haiku-model-in-amazon-bedrock-is-now-generally-available/
   Accessed: 2026-09-10
   Supports: Anthropic has no general-purpose native fine-tuning API; the only route to a fine-tuned Claude model is via Amazon Bedrock, currently limited to Claude 3 Haiku.

5. **DSIT, "AI Adoption Research"**
   URL: https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research
   Publisher: Department for Science, Innovation and Technology (IFF Research and Technopolis Group)
   Accessed: 2026-09-10
   Supports: among UK AI-adopting businesses, 85% use text generation/NLP tools, 7% use agentic AI (the least-adopted technology).

6. **Tom & Co stat bank entry stat_006** (data/stat_bank.json)
   Derived from: DSIT AI Adoption Research, published 13 Feb 2026
   Supports: 13.6% of all UK businesses use generative/text-generation AI vs 1.1% use agentic AI, a roughly 12x gap. Reused from the existing bank rather than recalculated, since it draws on the same underlying DSIT survey wave cited in this article.

7. **Bank of England / market rate context** — approximate GBP/USD conversion
   Used for: converting OpenAI's $25/1M training tokens and $100/hour figures to sterling at an approximate September 2026 market rate of 1.35 (multiple financial data sources placed GBP/USD between 1.33 and 1.36 in the week of 8 September 2026).
   Accessed: 2026-09-10
   Note: this is an approximate market rate, not a same-day Bank of England reference rate pulled directly, consistent with the conversion methodology already used in stat_bank.json stat_002.

## New Tom & Co original calculation (Layer 2)

**Sterling cost of OpenAI fine-tuning, September 2026 exchange rate.**
- $25 per 1M training tokens (GPT-4.1/GPT-4o standard supervised fine-tuning) ÷ 1.35 (GBP/USD) = £18.52/1M tokens, rounded to £18.50.
- $100/hour (o4-mini reinforcement fine-tuning training compute) ÷ 1.35 = £74.07/hour, rounded to £74/hour.
- Full workings appended to `stat_bank_update.json` in this folder for merge into `data/stat_bank.json`.

## Flag for Tom

This session's network policy blocked direct WebFetch to gov.uk, openai.com and arxiv.org (egress denied by organisation policy, confirmed via curl). All research above came through the WebSearch tool's own synthesis of those pages rather than a direct read of the full source document. The DSIT adoption percentages (85%/7%) and the OpenAI deprecation dates were corroborated across multiple independent search results, which gives reasonable confidence, but a human should ideally re-verify the OpenAI pricing figures and DSIT survey wave/date directly before this goes out, since pricing pages change without notice.
