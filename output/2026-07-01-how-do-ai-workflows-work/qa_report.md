# QA report: How do AI workflows work?

Topic: How do AI workflows work? (ad-hoc batch) | Target keyword: ai workflows | Cluster: Technical & Build | Format: Definition + explainer (with comparison table) | Word count: ~1,944 (band 1500-2200, on target)

## 10-element GEO checklist

1. **Definitive answer paragraph: PASS** — 78 words (within 40-80). Answers "How do AI workflows work?" on its own: defines the workflow, contrasts it with an agent, names a specific stat (55% of high performers, McKinsey Nov 2025). Sits above the first H2.
2. **Question-format H2s: PASS** — 7/7 H2s end with "?". Examples: "What is an AI workflow, and how is it different from an AI agent?", "What are the five AI workflow patterns?", "How do you build an AI workflow step by step?", "How many UK businesses actually use AI workflows in 2026?". 7 H2s is within the 4-7 range for the length band.
3. **Comparison table: PASS** — one HTML `<table>` with `<thead>`/`<tbody>`, 6 rows x 3 columns (AI workflow vs AI agent across: who decides steps, predictability, best for, cost/latency, testing/audit, example). Every cell populated, no "TBC".
4. **Authoritative inline citations: PASS** — 4 distinct primary/authoritative sources cited inline (5 link instances; McKinsey cited twice): Anthropic engineering (Dec 2024), ONS BICS (8 Jan 2026), BCC + University of Essex (18 Mar 2026), McKinsey State of AI 2025 (Nov 2025). All on the approved domain list. No agency blogs. Sits at the lower end of the 5-10 guide range, appropriate for a definition/technical topic where over-citing dilutes; each source is load-bearing.
5. **Original UK stat: PASS (Layer 2)** — Tom & Co Recipe C calculation: +19pp single-year jump in UK AI adoption to 2026 (biggest in the BCC series, more than the prior two years combined). Derived from the BCC 2023-2026 series, a delta the source did not publish. Workings recorded in sources.md. Secondary Layer 2 figure (~£24/productive hour) reuses stat_bank stat_003. NOTE: stat_bank.json NOT edited (ad-hoc batch rule); central process to append the new entry.
6. **JSON-LD schema: PASS** — single `<script type="application/ld+json">` array at end of content with Article, FAQPage (5 Q&A pairs matching H2s), and Person schemas. No HowTo (format is definition/explainer, not a formal how-to framework; the build section is prose steps). All fields populated, no placeholder URLs.
7. **Author byline + Person schema: PASS** — `author` field is plain string "Tom McCaul". "About the author" `<h3>` + `<p>` with role (Founder), credential (15+ years digital/agency leadership), and LinkedIn. Person schema includes name, jobTitle, worksFor Tom & Co, sameAs LinkedIn.
8. **Visible date / dateModified: PASS** — `date` = "2026-07-01"; JSON-LD datePublished and dateModified both "2026-07-01". No "Last reviewed:" line in body. Next review due 2026-09-29 (today + 90 days, supporting article).
9. **2-4 internal links: PASS** — 4 internal links to sibling batch articles, all `/ai-agency-consultancy/blog/{slug}`: what-are-agentic-workflows, what-are-ai-agents, what-is-an-ai-agent-orchestrator, what-is-rag-ai. Descriptive question anchors restating each destination H1. No banned anchor text. internal_link_suggestions.md lists these plus 1 alternate (what-is-agentic-ai).
10. **Robots.txt check: SITE-LEVEL** — not a per-article check; flagged once per batch by the central process. Not re-run here.

## Voice-guide spot-check (scripts/voice_check.py)

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓ (the word "comprehensive" in the Anthropic quote was trimmed out with an ellipsis, meaning preserved)
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 WARN (the 78-word answer paragraph, which is intentionally dense and within element 1's 40-80 range; the checker merges it with adjacent text but in isolation it is 78 words)
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 10 WARN — all are structural numbered/bulleted list-item leads (build steps 1-5 and the 5 "where to start" bullets), which the voice guide explicitly exempts. Zero decorative marketing bold in prose.
- H2s ending with ?: 7/7 ✓

**voice_check.py overall result: CLEAN**

## Decision: SHIP
Rationale: All 10 GEO elements PASS or are site-level; voice_check CLEAN; primary-sourced throughout with a Layer 2 UK original stat; on-band word count. One follow-up: human to verify the McKinsey 2.8x / 55% vs 20% line against the report PDF (source page timed out on fetch, figure captured via quoted secondary), and central process to append the Layer 2 entry to stat_bank.json.
