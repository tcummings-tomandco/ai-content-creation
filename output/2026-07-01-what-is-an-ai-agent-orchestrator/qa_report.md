# QA report: What is an AI agent orchestrator?

Topic: What is an AI agent orchestrator? (ad-hoc batch, not from roadmap)  |  Cluster: Technical & Build / Tools & emerging vocabulary  |  Format: A (Definition + benchmark table)  |  Word count: 1,805 (body, excl. JSON-LD; band 1500-2200, target ~1800)

## 10-element GEO checklist

1. **Definitive answer paragraph: PASS** — 79 words, sits above the first H2. Answers the headline question in isolation: defines the orchestrator as the control layer coordinating agents (order, context, output combination), gives the conductor analogy, and carries a specific number (Anthropic's 90.2% eval result). Within the 40-80 word rule.
2. **Question-format H2s: PASS** — 6 H2s, all end with "?". Mirror real prompts: "What does an AI agent orchestrator actually do?", "How is an orchestrator different from a single AI agent?", "What are the main AI agent orchestration patterns?", "What does the data show on orchestration cost versus payoff?", "How does orchestration fit a UK business's AI stack in 2026?", "What should a UK leader do about agent orchestration this quarter?". (4-7 for this band.)
3. **Comparison table: PASS** — 1 HTML `<table>` with `<thead>`/`<tbody>`, single agent vs orchestrator across 6 dimensions (structure, best for, token cost, reliability risk, latency, when to avoid). Every cell populated, no "TBC"/"varies". Sterling not applicable (token multipliers used, sourced to Anthropic).
4. **Authoritative inline citations: PASS** — 5 external citations, all on the approved list: Anthropic engineering docs, Microsoft/Azure architecture docs (vendor docs, Technical & Build cluster), Gartner (named research firm), gov.uk/DSIT (primary UK), McKinsey (named research firm). No agency blogs, no undated reports. In the 5-10 range.
5. **Original UK stat: PASS (Layer 2)** — Tom & Co analysis of Anthropic's published token figures derives a ~3.75x orchestration cost premium (15x chat / 4x chat). Recipe D (cost-per-outcome ratio). Workings in sources.md and stat_bank_update below; attributed inline as "Tom & Co analysis of Anthropic's published token figures". UK anchoring also carried by the DSIT 7% / 16% adoption figures and the sector cut (12% / 10% / 5%).
6. **JSON-LD schema: PASS** — Single `<script type="application/ld+json">` block at end of content. Array contains Article, FAQPage (4 Q&A pairs, all drawn from H2 content), and Person. All fields populated, no placeholder URLs. datePublished/dateModified = 2026-07-01.
7. **Author byline + Person schema: PASS** — `author` field is the string "Tom McCaul". `<h3>About the author</h3>` present with role (Founder, Tom & Co), credential (15+ years digital/agency leadership), and LinkedIn. Person schema includes name, jobTitle, worksFor (Tom & Co), sameAs LinkedIn.
8. **Visible date / dateModified: PASS** — `date` = "2026-07-01". JSON-LD datePublished and dateModified both "2026-07-01". No "Last reviewed:" line in body. Next review due 2026-09-29 (today + 90 days, supporting article).
9. **2-4 internal links: PASS** — 4 internal links, all `/ai-agency-consultancy/blog/{slug}`, all batch siblings. Descriptive anchors restate destination H1s ("What are AI agents?", "What are multi-agent systems?", "What are agentic workflows?", "What is agentic AI?"). No banned anchors. Mix of down-link (building block), up-links (multi-agent systems, agentic AI category), and applied cross-link (agentic workflows). Alternate (how-do-ai-workflows-work) logged in internal_link_suggestions.md.
10. **Robots.txt check: SITE-LEVEL** — Not a per-article check. Flag once per batch; not re-verified here.

## Voice-guide spot-check (scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 WARN — the 79-word answer paragraph, which is intentional and required to sit in the 40-80 word element-1 band. No body paragraph exceeds 70 words. Acceptable.
- "We"/"Our" frequency: 0.00% ✓
- Bolded phrases: 4 (all numbered-list-item leads in the two action sections; structural, under the 5 limit) ✓
- H2s ending with ?: 6/6 ✓
- British spellings: prioritised throughout (specialisms, parallelisation, aggregates, coherent). $ not used; token multipliers and £ example used for the Layer 2 stat.

**voice_check.py result: CLEAN**

## Decision: SHIP
Rationale: All 10 elements PASS (element 10 is site-level). voice_check CLEAN. 1,805 words on target, strong primary/authoritative sourcing, a defensible Layer 2 UK-anchored calculation, and the required comparison table and footer structure. One flag for review: the Gartner primary URL returned HTTP 403 to the automated fetcher; figures are corroborated across multiple outlets citing the identical press-release title, but a human should confirm the live Gartner page before publish.
