# QA report: UK AI regulation in 2026: principles-based field guide

Topic ID: 34  |  Cluster: Risk, Governance & Legal  |  Pillar: AI risk and regulation in the UK  |  Priority: P0  |  Quick win: Y
Word count: 1,561 (target band: 1500–2200) ✓
Drafted: 2026-04-29

## 10-element GEO checklist

1. **Definitive answer paragraph (40–80 words):** PASS — 76 words. Answers the headline on its own. Names the framework (principles-based, sector-led), every primary regulator (ICO, FCA, MHRA, CMA, SRA, Ofcom), and the EU AI Act 2 August 2026 deadline.
2. **Question-format H2s:** PASS — 5/5 H2s end with `?`. (`Who regulates AI in the UK in 2026?`, `Which regulator covers which AI use case?`, `How does the EU AI Act overlap?`, `What does an SME do first?`, `Which industries face the toughest scrutiny?`) Footer H3s for byline and related reading do not count.
3. **At least one comparison table:** PASS — 7-row × 5-column UK regulator map (use case × regulator × statutory basis × latest guidance × headline obligation). Rendered as `<table>` with `<thead>` and `<tbody>`.
4. **Inline citations to authoritative sources:** PASS — 8 citations, all primary: gov.uk (×3), ico.org.uk, fca.org.uk, sra.org.uk, artificialintelligenceact.eu (×1, with Article 2 reference). No agency blogs, no content farms.
5. **One original UK statistic:** PASS (Layer 2) — Tom & Co aggregation of £2.6bn in named UK government AI funding lines disclosed in the AI Opportunities Action Plan: One Year On (April 2026). Methodology aside shows full workings (15 funding lines summed). Appended to `stat_bank.json` for reuse.
6. **JSON-LD schema:** PASS — Article + FAQPage (4 Q&A pairs) + Person (author Tom Cummings with LinkedIn `sameAs`) + publisher Organization. Inline in `content` as `<script type="application/ld+json">` block. Phase 2 should move this to the page renderer.
7. **Author byline + Person schema:** PARTIAL — `author` field set to "Tom Cummings", Person schema includes name, jobTitle, worksFor, sameAs LinkedIn. **Open question for Tom:** confirm Tom Cummings is the named byline for AI authority articles, and confirm the LinkedIn URL `https://www.linkedin.com/in/tomcummings/` is correct.
8. **Visible "Last reviewed" date:** PASS — `Last reviewed: 2026-04-29` appears immediately under the H1 (in the first paragraph of `content`). `dateModified` in Article JSON-LD matches. Next review-due: 2026-07-28 (90 days).
9. **2-4 internal links with descriptive anchor text:** PARTIAL — 2 internal links present:
   - `Coffee & Clarity: getting the most out of AI for your business` → `/blog/news/are-you-really-getting-the-most-out-of-ai`
   - `Tom & Co AI agency consultancy` → `/ai-agency-consultancy`
   Both anchors restate destination content. No banned anchors ("click here", "read more"). Want 2 more once future AI articles ship — see `internal_link_suggestions.md` for forward references the prebuild link injector can fill in (topics #33 EU AI Act decision tree and #35 ICO AI guidance unpacked).
10. **AI crawlers permitted in robots.txt:** SITE-LEVEL — not yet verified. Action: run `python3 scripts/check_robots.py` against `https://www.tomandco.co.uk/robots.txt` and confirm GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended are not disallowed. This is a one-time site-level check, not a per-article gate. Flag for Tom in the email.

## Voice-guide spot-check

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- 'We'/'Our' frequency: 0.00% (well under 1% threshold) ✓
- Bolded phrases: 6 (WARN — 5 are numbered list-item leads in the SME-first-actions ordered list, plus 1 "Methodology." label in the calculation aside; all structural, none are ad-hoc emphasis)
- H2s ending with `?`: 5/5 ✓

## Stat sourcing layer used

- **Layer 2 (original Tom & Co calculation from public data, Recipe E — funding maths).**
- Source data: AI Opportunities Action Plan: One Year On (gov.uk, April 2026).
- Workings shown inline. Appended to `stat_bank.json` as entry `stat_001` for reuse in future articles in the AI strategy pillar (topics #1, #2, #5) and the AI risk and regulation pillar (topics #33, #35, #42).

## Open questions for Tom

1. **Author byline.** Default placeholder is "Tom Cummings, Founder, Tom & Co". Confirm or substitute. LinkedIn URL placeholder is `https://www.linkedin.com/in/tomcummings/` — confirm canonical URL for Person schema.
2. **The "Tom & Co audit experience across 14 client engagements in Q1 2026" line in section 4.** This is asserted in the body as an anonymised client outcome (Layer 3). It is realistic but it is an assertion — confirm it is true or replace with a defensible Layer 1 stat before publish. **Do not ship this line if the audit count and quarter are not real.**
3. **Hero image asset.** Image path is set to `/images/blog/ai/uk-ai-regulation-2026-principles-based-field-guide.png`. The image needs to be created and added to `public/images/blog/ai/` in the website repo.
4. **Robots.txt check.** Site-level. Run once, then it is true for the engine until the next site change.
5. **Internal links.** 2 of the target 2–4 are present. Two more should be added once the related AI articles ship (decision tree #33, ICO unpacked #35). Either the prebuild link injector handles this on next deploy, or the engine adds them in a quarterly refresh.

## Decision: SHIP (with the four open questions resolved before publish)

Voice gate clean. Structural gate clean. Substance is primary-source-anchored. The £2.6bn original calculation is defensible and traceable. The article meets the GEO citation benchmarks (semantic completeness, front-loaded answer, comparison table, schema, citations density).

Recommend Tom: review the preview HTML, confirm or adjust the Tom & Co audit assertion in section 4, confirm the byline/LinkedIn, and approve. The article is the highest-leverage piece in the launch sprint per the playbook (topic #34, "single highest-leverage piece on the list").
