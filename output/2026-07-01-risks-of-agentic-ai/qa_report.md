# QA report: What are the risks of agentic AI?

Topic: Risks of agentic AI (ad-hoc batch) | Cluster: Risk, Governance & Legal | Priority: batch | Word count: ~1,554 (body, band 1500-2200) | Format: Analysis / counter-narrative (Template H)

## 10-element GEO checklist

1. **Definitive answer paragraph: PASS** — 75-word opener answers "what are the risks of agentic AI?" on its own. Contains specific number (>40% cancelled by end 2027), named sources (Gartner), and named UK regulators (ICO, FCA). Sits above the first H2. Within the 40-80 word answer band (voice_check WARN on 71+ is expected and permitted for the answer paragraph).
2. **Question-format H2s: PASS** — 6/6 H2s end with "?". Examples: "What does the data actually show about agentic AI risk?", "What are the security risks specific to agentic AI?", "Who is accountable when a UK agentic AI system gets it wrong?". Count is within the 4-7 range for this length band.
3. **Comparison table: PASS** — 5 rows x 4 columns (Risk area / Popular narrative / What the evidence shows / Primary source). Proper HTML `<table>` with `<thead>`/`<tbody>`. Every cell populated; no "TBC"/"varies". Fits Template H's popular-view vs evidence-based-view contrast.
4. **Authoritative inline citations: PASS** — 6 inline authoritative citations: Gartner (named research firm, disclosed poll methodology), OWASP GenAI (peer-reviewed security framework), Anthropic (primary research), ICO (regulator, x2 pages), FCA (regulator via ADM page + speech). All on the approved-domain list. No agency blogs cited as primary.
5. **Original UK stat: PASS (Layer 2)** — Tom & Co analysis of Gartner's June 2025 agent-washing estimate: ~93% of self-described agentic vendors are agent washing (conservative ratio derivation, 130 genuine / 2,000 floor). Cited inline as a blockquote with one-line attribution. Appended to stat_bank as a suggested entry (see note; central process merges into data/stat_bank.json — this subagent does not write that file).
6. **JSON-LD schema: PASS** — single `<script type="application/ld+json">` block at end of content with Article + FAQPage (5 Q&A) + Person. Author Person has name, jobTitle, worksFor Tom & Co, sameAs LinkedIn. No placeholder URLs.
7. **Author byline + Person schema: PASS** — article.json `author` is the plain string "Tom McCaul". `<h3>About the author</h3>` block names Tom McCaul, Founder, Tom & Co, with 15+ years credential and LinkedIn. Person schema resolves to Tom McCaul with LinkedIn sameAs.
8. **Visible date / dateModified: PASS** — article.json `date` = 2026-07-01; Article JSON-LD datePublished and dateModified both 2026-07-01. No "Last reviewed:" line in body. Review-due: 2026-09-29 (today + 90 days).
9. **2-4 internal links: PASS** — 4 internal links, all `/ai-agency-consultancy/blog/{slug}` to sibling batch articles (what-is-agentic-ai, what-are-multi-agent-systems, agentic-ai-use-cases-mid-market, what-are-agentic-workflows). Anchor text restates each destination H1. No banned anchors. internal_link_suggestions.md lists 3 alternates.
10. **Robots.txt check: SITE-LEVEL** — not a per-article check. Not re-verified by this subagent (no site push in ad-hoc batch).

## Voice-guide spot-check (scripts/voice_check.py output)

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 WARN (the 75-word definitive answer paragraph, permitted by design)
- "We"/"Our" frequency: 0.00% ✓
- Bolded phrases: 5 (at the cap; all are numbered-step leads in the final section, i.e. structural)
- H2s ending with ?: 6/6 ✓

**voice_check result: CLEAN**

## Decision: SHIP
Rationale: All 10 elements PASS or SITE-LEVEL; voice_check CLEAN; UK regulatory angle (ICO 8 Jan 2026, FCA Jan 2026, DUAA Articles 22A-22D in force 5 Feb 2026) used as instructed; Layer 2 original stat present; counter-narrative format fits the topic. One reviewer flag: the 16%/41% UK-vs-US deployment figure is RingCentral trade-press research used only as supporting colour, not a key-stat tile (see sources.md).
