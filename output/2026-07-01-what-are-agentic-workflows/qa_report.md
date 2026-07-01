# QA report: What are agentic workflows?

Topic: What are agentic workflows? | Slug: what-are-agentic-workflows | Cluster: Technical & Build / Tools | Priority: ad-hoc batch | Word count: 1,563 (band 1500–2200, target ~1800) | Date: 2026-07-01

## 10-element GEO checklist

1. **Definitive answer paragraph: PASS** — 77 words (within 40–80), sits above the first H2. Answers the headline on its own: defines an agentic workflow, gives the Anthropic workflow-vs-agent distinction, and carries a dated stat (Gartner: 40% of enterprise apps by end of 2026, up from under 5% in 2025).

2. **Question-format H2s: PASS** — 6 H2s, all end with "?": "What does 'agentic workflow' actually mean in 2026?", "How is an agentic workflow different from a normal AI workflow or a single agent?", "What are the main agentic workflow patterns?", "What does the adoption data actually show?", "Where do agentic workflows fit in a UK business's stack?", "What should a UK leader do this quarter?". Five workflow patterns promoted to H3 (prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimiser) per the "3+ named sub-topics → H3" rule.

3. **Comparison table: PASS** — one HTML `<table>` with `<thead>`/`<tbody>`, 6 rows x 4 columns, comparing single LLM call vs agentic workflow vs autonomous agent across who-decides-steps, tool use, predictability, cost/latency, good-for, and auditability. Every cell populated, no "TBC".

4. **Authoritative inline citations: PASS** — 6 authoritative external citations (excludes the author LinkedIn link): Anthropic "Building Effective Agents" (anthropic.com), McKinsey State of AI Nov 2025 (mckinsey.com), Gartner via Reuters (reuters.com), ONS ASHE 2024 (ons.gov.uk), ICO automated decision-making guidance (ico.org.uk), ICO work on AI (ico.org.uk). All on the approved-domain list. Within the 5–10 range.

5. **Original UK stat: PASS (Layer 2)** — the article uses the Tom & Co Layer 2 calculation from stat_bank.json (stat_003): a UK knowledge worker costs an employer ~£23.80/hour on ONS ASHE 2024 data, used here as the break-even baseline an agentic workflow must beat (two hours/week saved = over £2,400/year). Reuses the existing bank entry; per the ad-hoc batch rules this subagent does NOT write to data/stat_bank.json.

6. **JSON-LD schema: PASS** — single `<script type="application/ld+json">` block at the end of content. Array contains Article, FAQPage (4 Q&A pairs), and Person. Parses as valid JSON; all required fields populated, no placeholder URLs. (No scripts/validate_jsonld.py present in repo; validated by JSON parse and schema.org field check.)

7. **Author byline + Person schema: PASS** — `author` field is the plain string "Tom McCaul". `<h3>About the author</h3>` section names Tom McCaul, Founder, Tom & Co, with the "15+ years in digital commerce" credential and the LinkedIn link. Person schema includes name, jobTitle (Founder), worksFor (Tom & Co), sameAs (https://www.linkedin.com/in/tom-mccaul-77b2778/).

8. **Visible date / dateModified: PASS** — article.json `date` = "2026-07-01". Article JSON-LD `datePublished` and `dateModified` both "2026-07-01". No "Last reviewed:" line in body. (Storyblok published_at set by the central push step.) Next review due: 2026-09-29 (today + 90 days, supporting article).

9. **2–4 internal links: PASS** — 4 internal links, all `/ai-agency-consultancy/blog/{slug}` to sibling articles in this batch: how-do-ai-workflows-work, what-is-agentic-ai, what-are-ai-agents, what-is-an-ai-agent-orchestrator. Anchors restate each destination H1; no banned anchor text. Up-link (What is agentic AI? = parent category) plus cross-cluster siblings present. Alternates listed in internal_link_suggestions.md.

10. **Robots.txt check: SITE-LEVEL** — not a per-article check; flagged once per batch. Verify www.tomandco.co.uk/robots.txt permits GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended (site-wide config, not blocking this article).

## Voice-guide spot-check (from scripts/voice_check.py — CLEAN, exit 0)

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71–100 words: 1 WARN (the 77-word answer paragraph, which is intentionally dense and within element-1's 40–80 range; all body paragraphs are ≤70)
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 0 ✓
- H2s ending with ?: 6/6 ✓

## Fact-check notes

- Anthropic workflow/agent definitions quoted verbatim from the primary source (fetched directly), published 19 December 2024.
- McKinsey figures corrected during drafting: an early secondary summary gave "62% experimenting"; the verified primary figure is 39% experimenting / 23% scaling / 88% using AI in at least one function (survey fielded 25 June–29 July 2025, 1,993 respondents). Body, FAQ and key_stats all use the verified 39% / 23%.
- Gartner "40% by 2026, up from <5%" is stated in the 26 Aug 2025 press-release title itself; "40%+ cancelled by 2027" is the 25 June 2025 release (poll of 3,412 attendees, Jan 2025), cited via Reuters because gartner.com blocks automated fetch.
- ICO Article 22 / Data (Use and Access) Act 2025 material and the March 2026 draft ADM guidance are confirmed to ico.org.uk pages (URLs in sources.md).
- Note on spelling: Anthropic's source uses US "parallelization"; the article uses UK "parallelisation" (anglicised, not a verbatim quote of that word).

## Decision: SHIP
Rationale: All 10 elements PASS or SITE-LEVEL; voice_check CLEAN (exit 0); word count in band; all figures reconciled to primary/reputable sources with corrected McKinsey numbers.
