# QA report: Agentic AI vs generative AI: what's the difference?

Topic: Agentic AI vs generative AI (ad-hoc batch)  |  Cluster: Technical & Build / Tools & emerging vocabulary  |  Priority: batch  |  Word count: ~1,580 (body), 7 min read

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 77 words, sits above the first H2, answers the headline on its own. Contains specific figures (85% text generation vs 7% agentic among UK AI adopters, DSIT February 2026). Reads correctly in isolation.
2. **Question-format H2s**: PASS — 7 H2s, all end with "?". Examples: "What is generative AI in plain terms?", "What is the difference between agentic AI and generative AI?", "Which one does a UK business actually need?". Two named sub-topics promoted to H3 under the global-data section, plus H3s in the footer.
3. **Comparison table**: PASS — one HTML `<table>` with `<thead>`/`<tbody>`, 8 rows × 3 columns (Dimension / Generative AI / Agentic AI). Every cell populated, no "TBC" / "varies". Required for this "vs" topic and present.
4. **Authoritative inline citations**: PASS — 7 inline external citations. Domains: gov.uk (DSIT), mitsloan.mit.edu, anthropic.com, mckinsey.com, gartner.com. All primary UK authority, named research firm, peer institution, or vendor primary docs. No agency blogs, no content farms.
5. **Original UK stat**: PASS (Layer 2) — Tom & Co analysis of DSIT February 2026 figures deriving generative-AI reach (~13.6% of all UK firms) vs agentic-AI reach (~1.1%), a ~12x gap, a share-of-all-firms cut the source did not publish. Recipe C. Workings recorded in sources.md and stat_bank_update.json.
6. **JSON-LD schema block**: PASS — single `<script type="application/ld+json">` at end of content with Article + FAQPage (4 Q&A) + Person. No HowTo (not a step-by-step format), correctly omitted. No placeholder URLs.
7. **Author byline + Person schema**: PASS — `author` field = plain string "Tom McCaul". "About the author" `<h3>` + `<p>` with role and 15+ years credential and LinkedIn. Person schema includes name, jobTitle, worksFor Tom & Co, sameAs LinkedIn.
8. **Visible date / dateModified**: PASS — `date` = "2026-07-01"; JSON-LD datePublished and dateModified both "2026-07-01". No "Last reviewed:" line in body. Next review due 2026-09-29 (today + 90 days).
9. **2-4 internal links**: PASS — 4 links to sibling batch articles under /ai-agency-consultancy/blog/{slug}: what-is-agentic-ai, what-are-ai-agents, agentic-ai-use-cases-mid-market, risks-of-agentic-ai. Descriptive anchors restating each destination H1. No banned anchor text. Listed with alternates in internal_link_suggestions.md.
10. **Robots.txt check**: SITE-LEVEL — one-time per batch, not blocking this article. Flag to central process to confirm GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended are allowed on tomandco.co.uk/robots.txt.

## Voice-guide spot-check (scripts/voice_check.py)
- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 WARN — the 77-word answer paragraph, explicitly exempt per voice guide ("the answer paragraph at the top is its own thing, 40-80 words, dense by design"). No FAIL.
- "We"/"our" frequency: 0.06% ✓ (under 1%)
- Bolded phrases: 2 ✓ (the two decision-rule leads; under 5)
- H2s ending with ?: 7/7 ✓

**voice_check result: CLEAN**

## Decision: SHIP
Rationale: All 10 elements PASS (element 10 is site-level). voice_check CLEAN. "vs" comparison table present as required, front-loaded answer paragraph within band, Layer 2 UK original stat included, 4 sibling internal links, JSON-LD valid with Article + FAQPage + Person.
