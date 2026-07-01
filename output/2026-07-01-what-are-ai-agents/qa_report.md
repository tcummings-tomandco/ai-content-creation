# QA report: What are AI agents? A plain-English guide for UK businesses

Slug: what-are-ai-agents  |  Cluster: Operations & Efficiency  |  Format: A (Definition + benchmark table)  |  Priority: n/a (ad-hoc batch)  |  Word count: ~1,640 (band 1500–2200, PASS)

## 10-element GEO checklist

1. **Definitive answer paragraph: PASS** — 77 words, sits above the first H2, answers "what are AI agents?" on its own. Contains specifics (LLM, plan/pick tools/act/loop, named vendor Anthropic). Within the 40–80 word target.
2. **Question-format H2s: PASS** — 7/7 end with "?". Examples: "What is an AI agent, exactly?", "How does an AI agent actually work?", "How is an AI agent different from a chatbot or RPA?", "How many UK businesses actually use AI agents?", "Do AI agents work, or is it hype?", "How should a UK business start with AI agents?". Each mirrors a real user prompt.
3. **Comparison table: PASS** — one HTML `<table>` with `<thead>`/`<tbody>`, 6 rows × 4 columns (Chatbot vs RPA vs AI agent across 6 dimensions). Every cell populated, no "TBC"/"varies".
4. **Authoritative inline citations: PASS** — 8 inline citations across 7 distinct authoritative domains: anthropic.com, openai.com, ibm.com (named vendor engineering docs), gov.uk/DSIT and ons.gov.uk (UK primaries), gartner.com and mckinsey (named research firms), computerweekly.com (named trade press reporting Salesforce/Vanson Bourne). No agency blogs or content farms. Within the 5–10 range.
5. **Original UK stat: PASS (Layer 2, reused)** — Tom & Co analysis of ONS ASHE 2024 data: ~9 minutes/person/week break-even for a 10-person team on a ~£1,900/year AI subscription. Reuses stat_bank stat_003 (Recipe D), cited in body as "Tom & Co analysis". No new stat_bank.json entry written, per ad-hoc batch rule (do not edit files outside the output folder).
6. **JSON-LD schema: PASS** — single `<script type="application/ld+json">` block at end of content, array of Article + FAQPage (5 Q&A pairs) + Person. All fields populated, no placeholder URLs, no empty strings. Parses as valid JSON.
7. **Author byline + Person schema: PASS** — `author` field is the plain string "Tom McCaul". Body has `<h3>About the author</h3>` with role (Founder) and credential (15+ years digital commerce/agency leadership) + LinkedIn. Person schema includes name, jobTitle, worksFor Tom & Co, sameAs LinkedIn.
8. **Visible date / dateModified: PASS** — article.json `date` = 2026-07-01; JSON-LD datePublished and dateModified both = 2026-07-01. No "Last reviewed:" line in body. Review due: 2026-09-29 (today + 90 days, supporting article).
9. **2–4 internal links: PASS** — 4 links in the "Related Tom & Co reading" footer, all using `/ai-agency-consultancy/blog/{slug}`. Anchors restate destination H1s ("What is agentic AI?", "What are multi-agent systems?", "What are agentic workflows?", "Agentic AI use cases for mid-market businesses"). No banned anchor text. Sibling articles in this batch; an orchestrator alternate listed in internal_link_suggestions.md.
10. **Robots.txt check: SITE-LEVEL** — not a per-article check; handled once per batch by the central process. Not blocking.

## Voice-guide spot-check (from scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71–100 words: 1 WARN (the 77-word answer paragraph, intentional and within element-1's 40–80 target; all other body paragraphs ≤70)
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 0 ✓
- H2s ending with ?: 7/7 ✓

**voice_check result: CLEAN**

## Decision: SHIP
Rationale: all 10 elements PASS or SITE-LEVEL; voice_check CLEAN; word count in band; sourcing is primary/named-vendor throughout with a genuine UK-government primary (DSIT) and a Layer 2 Tom & Co calculation. The single length WARN is the intentional answer paragraph.
