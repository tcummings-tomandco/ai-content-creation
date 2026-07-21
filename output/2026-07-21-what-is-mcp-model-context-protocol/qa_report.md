# QA report: What is MCP (Model Context Protocol) in plain English?

Topic ID: 15  |  Cluster: Operations & Efficiency  |  Priority: P1 (quick win)  |  Word count: 1621

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 64 words, sits directly under the H1, above the first H2. Names the source (Anthropic), the exact date (25 November 2024), and the three named adopters (OpenAI, Google, Microsoft), so it answers "what is MCP" on its own with no surrounding context required.
2. **Question-format H2s**: PASS — 7/7 H2s end with `?`. Each mirrors the roadmap row's likely query phrasings ("what is MCP", "Model Context Protocol business") or a natural follow-up a non-technical reader would ask (how it works, why it matters, what to do next).
3. **Comparison table**: PASS — one table under "What's the difference between MCP and the AI tools you already have?", 5 rows x 3 option columns (custom integration, vendor plugin, MCP server), every cell populated, no "TBC"/"varies".
4. **Authoritative inline citations**: PASS — 7 inline citations (excluding the author's LinkedIn link): anthropic.com, openai.com, blog.modelcontextprotocol.io, britishchambers.org.uk, gov.uk, media.defense.gov (NSA), ico.org.uk. All primary (protocol creator/adopters, a UK regulator, UK official statistics, a national cyber security agency) or a named survey with disclosed methodology (BCC + University of Essex). No agency blogs, content farms, or Wikipedia used as primary sources; several low-quality SEO sites with unverifiable/fabricated-looking stats were identified during research and explicitly excluded (see sources.md).
5. **Original UK statistic**: PASS (Layer 2) — new Tom & Co calculation: ~2.4 million UK businesses sit in the gap between broad AI use (54%, BCC/Essex 2026) and deep systems integration (11%, same source), applied to gov.uk's 5,499,000 UK private-sector business population (2024). Full workings in `stat_bank_update.json` and `sources.md`. Appended to `data/stat_bank.json` as `stat_011`.
6. **JSON-LD schema**: PASS — Article + FAQPage (5 Q&A pairs) + Person, single script block at the end of `content`. No HowTo (format is "Definition + diagram", not a numbered how-to). All fields populated, no placeholder URLs.
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul". Body has an `<h3>About the author</h3>` section naming Tom McCaul, Founder, Tom & Co, 15+ years in digital commerce, with LinkedIn link. Person schema includes name, jobTitle, worksFor, sameAs.
8. **Visible date / dateModified**: PASS — `article.json` `date` = 2026-07-21 (today). JSON-LD `datePublished`/`dateModified` both 2026-07-21. No "Last reviewed" line in the body. Roadmap `Notes` will record next review-due date (2026-10-19, +90 days).
9. **2-4 internal links**: PASS — 3 internal links in "Related Tom & Co reading": `what-is-agentic-ai` (up-link to the broader agentic-AI concept this protocol enables), `what-are-ai-agents` (adjacent, same cluster family), `agentic-ai-use-cases-mid-market` (cross-cluster bridge to Strategy & ROI). Anchor text restates each destination's H1. No banned anchor text.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; last checked per `output/_robots_status.txt` (site-wide config, not a per-article gate).

## Voice-guide spot-check (from `scripts/voice_check.py`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 (71-word illustrative accountancy-practice example; within the "one longer paragraph per major section" allowance)
- "We"/"our" frequency: 0.31% ✓
- Bolded phrases: 4 (all numbered-step leads in the closing action list) ✓
- H2s ending with ?: 7/7 ✓

**Automated result: CLEAN**

## Decision: SHIP

Rationale: all 10 elements pass (robots.txt is a site-level check, not blocking), the voice gate reports CLEAN, the original UK stat is an honest, sourced Layer 2 derivation with workings shown, and the article distinguishes itself clearly from the more technical/enterprise-integration sibling topic (#49, "What is MCP and how does it change enterprise AI integrations") by targeting the non-technical Ops/C-suite audience this roadmap row specifies.
