# QA report: RAG vs fine-tuning vs prompt engineering: which do you need?

Topic ID: 45  |  Cluster: Technical & Build  |  Priority: P1  |  Word count: 2066

## 10-element GEO checklist

1. **Definitive answer paragraph:** PASS — 78 words, sits above the first H2, answers the headline question standalone, cites the 7 May 2026 OpenAI fine-tuning wind-down date and the EMNLP 2024 finding.
2. **Question-format H2s:** PASS — 6 H2s, all end with `?`: "What's actually different between RAG, fine-tuning, and prompt engineering?", "How do you decide which one to use for a UK project?", "When does prompt engineering alone do the job?", "When should you reach for RAG instead?", "When is fine-tuning still worth it, and why is it getting harder to justify?", "What should a UK team do about each path?"
3. **Comparison table:** PASS — one `<table>` with `<thead>`/`<tbody>`, 5 rows x 4 columns (prompt engineering / RAG / fine-tuning), every cell populated, sterling figures and September 2026 date stamp included.
4. **Authoritative inline citations:** PASS — 5 external citations, all to approved domains: gov.uk (DSIT AI Adoption Research), developers.openai.com x2 (deprecations, pricing), aclanthology.org (EMNLP 2024 peer-reviewed paper), aws.amazon.com (Bedrock/Claude 3 Haiku fine-tuning). 4 internal Tom & Co links additionally.
5. **Original UK stat:** PASS — Layer 2. New calculation this run: OpenAI's published fine-tuning USD pricing ($25/1M tokens; $100/hour) converted to sterling (£18.50/1M tokens; £74/hour) at an approximate September 2026 GBP/USD market rate. Full workings in `stat_bank_update.json`. Also reuses existing bank entry stat_006 (13.6% vs 1.1% UK adoption gap) with "Tom & Co analysis" attribution.
6. **JSON-LD schema:** PASS — Article + FAQPage (5 Q&A pairs mirroring the H2s) + Person, at the end of `content`. Validated with `json.loads` on the extracted script block; no empty strings or placeholder URLs.
7. **Author byline + Person schema:** PASS — `author` field is the string "Tom McCaul". About-the-author section present with role and credential. Person schema includes name, jobTitle, worksFor, sameAs.
8. **Visible date / dateModified:** PASS — `article.json` `date` = 2026-09-10 (today). JSON-LD `datePublished`/`dateModified` both 2026-09-10. No "Last reviewed" line in the body.
9. **2-4 internal links:** PASS — 4 links in "Related Tom & Co reading" (what-is-rag-ai, what-is-mcp-model-context-protocol, how-much-should-a-uk-sme-budget-for-ai-in-2026, ai-uk-gdpr-ico-guidance-2026), plus 2 of those repeated inline at first natural mention. No banned anchor text. Up-link to Pillar 5 sibling (no hub published yet) and cross-cluster bridges to Strategy & ROI and Risk/Governance covered.
10. **Robots.txt check:** SITE-LEVEL — not re-verified this run. `scripts/check_robots.py` is not present in this repo checkout and no `output/_robots_status.txt` exists. Flagging for Tom rather than assuming pass.

## Voice-guide spot-check

Full mechanical output from `python3 scripts/voice_check.py`:

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 (the 78-word answer paragraph itself, which is expected and required to be 40-80 words per element 1)
- "We"/"our" frequency: 0.05% ✓
- Bolded phrases: 3 ✓ (numbered decision-tree list-item leads, structural)
- H2s ending with ?: 6/6 ✓

**Result: CLEAN**

## Research constraint flagged for Tom

This session's network egress policy blocked direct WebFetch/curl access to gov.uk, openai.com and arxiv.org. All citations were sourced via the WebSearch tool's synthesis of those primary pages rather than a direct full-page read. Cross-checked across multiple independent search hits for the load-bearing facts (OpenAI's fine-tuning wind-down dates, DSIT adoption percentages). Recommend a human spot-check of the OpenAI pricing figures and the DSIT survey date/wave before wide reliance, since vendor pricing pages change without notice. See `sources.md` for full detail.

## Decision: SHIP

Rationale: all 10 elements pass or are correctly flagged as site-level/out-of-scope; voice gate is CLEAN; word count (2066) sits within the 2000-2800 band for this topic; a new Layer 2 stat was produced and appended to the stat bank. The one open item is a research-integrity flag (network access constraint) for Tom to spot-check, not a QA failure.
