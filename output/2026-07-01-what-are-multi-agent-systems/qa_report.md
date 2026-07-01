# QA report: What are multi-agent systems? A plain-English UK guide

Topic: What are multi-agent systems? | Cluster: Technical & Build | Priority: (ad-hoc batch) | Word count: 1,378 (body, excl. JSON-LD)

Target keyword: multi agent systems | Slug: what-are-multi-agent-systems | Date: 2026-07-01

## 10-element GEO checklist

1. **Definitive answer paragraph:** PASS — 79-word opening paragraph directly answers "what are multi-agent systems?", names the orchestrator/worker structure, and carries specific figures (90.2% improvement, ~15x tokens). Sits above the first H2. Within the 40-80 word answer-paragraph rule (voice_check flags it as a 71-100 WARN, which is expected and permitted for the answer paragraph).
2. **Question-format H2s:** PASS — 7/7 H2s end with "?" (What is a multi-agent system in simple terms? / How does a multi-agent system actually work? / What is the difference between a single-agent and a multi-agent system? / How much do multi-agent systems cost to run? / Where do UK businesses actually use multi-agent systems in 2026? / What are the main risks of multi-agent systems? / Should a UK business build a multi-agent system?). Mirror real query phrasings.
3. **Comparison table:** PASS — one proper HTML `<table>` with `<thead>`/`<tbody>`, 6 rows x 3 columns, single-agent vs multi-agent across structure, best-for, token cost, sterling cost, debugging, failure mode. Every cell has data; no "TBC"/"varies".
4. **Authoritative inline citations:** PASS — 6 authoritative citations: Anthropic engineering blog (primary vendor doc), Anthropic pricing (primary), BCC Powering Productivity report (named survey, primary), BCC news release (primary), Gartner press release (named research firm), ICO guidance (UK regulator). All on the approved domain pattern. No agency blogs or undated reports.
5. **Original UK stat / Layer 2:** PASS (Layer 2) — Tom & Co cost-per-query estimate applying Anthropic's published token multipliers (~4x single agent, ~15x multi-agent) to Claude Opus 4.8 list pricing, converted to sterling: ~£0.39 single-agent, ~£1.48 multi-agent, vs ~10p as a plain chat. Workings and attribution recorded in sources.md. Flag: the central process should append this to data/stat_bank.json (subagent did not edit the shared bank).
6. **JSON-LD schema:** PASS — single `<script type="application/ld+json">` block at end of content: Article + FAQPage (5 Q&As) + Person. All required fields populated, no placeholder URLs. dateModified matches date.
7. **Author byline + Person schema:** PASS — author field is the plain string "Tom McCaul"; `<h3>About the author</h3>` names role and credential (15+ years, founder) with LinkedIn; Person schema resolves to Tom McCaul with jobTitle, worksFor Tom & Co, sameAs LinkedIn.
8. **Visible date / dateModified:** PASS — article.json `date` = "2026-07-01"; Article JSON-LD datePublished and dateModified both "2026-07-01". No "Last reviewed" line in body. Next review due (supporting article): 2026-09-29 (today + 90 days) — for the central process to record on the roadmap.
9. **2-4 internal links:** PASS — 4 inline internal links using `/ai-agency-consultancy/blog/{slug}` to siblings in this batch (what-are-ai-agents, what-is-an-ai-agent-orchestrator, what-are-agentic-workflows, risks-of-agentic-ai). Descriptive anchors restate each destination H1; no banned anchor text. Alternates listed in internal_link_suggestions.md.
10. **Robots.txt check:** SITE-LEVEL — not a per-article check; deferred to the batch-level robots check for GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended.

## Voice-guide spot-check (scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 (the 79-word answer paragraph — expected/permitted)
- "We"/"our" frequency: 0.00% ✓ (first-person plural used only in the "Tom & Co" brand name)
- Bolded phrases: 0 ✓
- H2s ending with ?: 7/7 ✓

**voice_check.py result: CLEAN**

## Notes / accuracy checks

- Anthropic figures (90.2% vs single-agent Claude Opus 4; ~15x multi-agent tokens, ~4x single-agent; 80% of variance from token usage; 3-5 subagents; orchestrator-worker) verified directly against the Anthropic engineering blog (13 June 2025).
- Claude / Anthropic references checked against current model facts: Claude Opus 4.8 is the current model with $5/$25 per MTok pricing. No stale model IDs or deprecated API claims made in the article (the piece does not include code).
- Gartner press-release page returned HTTP 403 to automated fetch; the "40% of agentic AI projects cancelled by end-2027" and "40% of enterprise apps by 2026" figures are Gartner-attributed and corroborated across the press-release headline and multiple Gartner-sourced summaries.
- BCC 7% agentic-AI and 85% text-generation figures are attributed to the Powering Productivity report (the PDF is binary and not machine-readable via fetch; figures corroborated across BCC-hosted material and reporting on the report). Headline 54%/35%/23% figures verified against the BCC news release directly.

## Decision: SHIP
Rationale: All 10 elements PASS or SITE-LEVEL; voice_check CLEAN; Layer 2 original stat present; comparison table present; all citations primary. Word count 1,378 reads complete for a definitional explainer; could be padded toward 1,500 but padding would dilute extraction clarity.
