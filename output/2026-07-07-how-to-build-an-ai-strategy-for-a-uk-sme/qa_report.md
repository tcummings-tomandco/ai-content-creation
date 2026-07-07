# QA report: How do you build an AI strategy for a UK SME?

Topic ID: 2  |  Cluster: Strategy & ROI  |  Pillar: P1: AI strategy  |  Priority: P1  |  Quick win: Y
Word count: 1,849 (target band: 1800-2400) ✓
Drafted: 2026-07-07
Author: Tom McCaul, Founder, Tom & Co

## 10-element GEO checklist

1. **Definitive answer paragraph (40-80 words):** PASS — 76 words. Names the five steps, cites the 33% no-plans figure and the BridgeAI scheme by name. Answers the headline question standalone.
2. **Question-format H2s:** PASS — 7/7 H2s end with `?`. 4-7 H2s expected for this length band; at the top of the range, matching the format-mapping.md "5-step framework" template (overview + 5 steps + "how long does it take"). Footer H3s (About the author, Related reading) and the three Step 3 pilot-category H3s do not count, per format-mapping.md.
3. **At least one comparison table:** PASS — 3-row x 5-column table comparing BridgeAI Innovation Exchange, Made Smarter Adoption and Innovate UK Smart Grants (scheme, audience, grant size, match funding, current status). Every cell has real data, including the honest "paused since January 2025" status for Smart Grants rather than omitting an inconvenient scheme.
4. **Inline citations to authoritative sources:** PASS — 7 inline external citations: BCC/Essex (news page + PDF), ICO AI and Data Protection Risk Toolkit, Innovate UK Business Connect (BridgeAI programme page), Made Smarter Adoption, GOV.UK AI Opportunities Action Plan: One Year On, Innovate UK Innovation Funding Service (BridgeAI competition detail). All primary UK regulator, government or UKRI/Innovate UK domains. No agency blogs. (Innovate UK Smart Grants guidance on ukri.org is cited in sources.md supporting the table row rather than inline in prose.)
5. **One original UK statistic:** PASS — Layer 2, reused. Cites the existing `stat_001` Tom & Co calculation (£2.6bn in named UK government AI funding lines, from `data/stat_bank.json`) with correct attribution in a blockquote. No new calculation was performed for this article, so no `stat_bank_update.json` is included; per stat-sourcing.md, reusing an established Tom & Co calculation as primary is an accepted pattern once the bank holds prior entries.
6. **JSON-LD schema:** PASS — Article + HowTo (5 steps, matching the format's mandatory requirement for "5-step framework") + FAQPage (5 Q&A pairs) + Person (Tom McCaul, LinkedIn `sameAs`) + publisher Organization. Validated as parseable JSON via `json.loads` in the build script; no `validate_jsonld.py` script present in the repo.
7. **Author byline + Person schema:** PASS — `author: "Tom McCaul"` (string). Person schema includes name, jobTitle (Founder), worksFor (Tom & Co), sameAs `https://www.linkedin.com/in/tom-mccaul-77b2778/`. "About the author" H3 present in body.
8. **Visible date / dateModified:** PASS — `article.json` `date` = 2026-07-07 (today). Article JSON-LD `datePublished` and `dateModified` both 2026-07-07. No "Last reviewed" line in the body.
9. **2-4 internal links with descriptive anchor text:** PASS — 3 internal links (each placed once inline and once in "Related Tom & Co reading"): ai-roi-uk-business-2026-what-the-evidence-actually-shows (same-pillar sibling), does-the-eu-ai-act-apply-to-my-uk-business (cross-cluster, Risk/Governance/Legal), chatgpt-vs-claude-vs-gemini-for-business (cross-cluster, Technical & Build). No up-link to the AI-strategy pillar hub is possible yet because the pillar page has not been written (this article is itself one of that pillar's supporting pieces); flagged in `internal_link_suggestions.md`.
10. **AI crawlers permitted in robots.txt:** SITE-LEVEL — not re-checked this run; read the last status from `output/_robots_status.txt` if present.

## Voice-guide spot-check

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- Paragraphs 71-100 words: 1 (the 76-word answer paragraph, which the voice guide explicitly permits at the top of the article)
- "We"/"our" frequency: 0.00%
- Bolded phrases: 0
- H2s ending with ?: 7/7 ✓

`python3 scripts/voice_check.py` result: **CLEAN** on first pass, no iteration needed.

## Decision: SHIP

Rationale: all 10 checklist elements pass or are correctly marked site-level, the voice gate is CLEAN on the first run, the comparison table gives honest (including unflattering) data on all three funding schemes, and element 5 is satisfied by a transparent reuse of an existing, audited Tom & Co calculation rather than an invented number.

## Note on stat reuse

`scripts/pick_next_topic.py` returned Topic #2 as the next open row (Status was empty; #1 is already "Approved — draft in Storyblok"). This article's Layer 2 stat (`stat_001`, £2.6bn UK government AI funding) was first calculated for the `uk-ai-regulation-2026-principles-based-field-guide` article and is reused here with the same sources and workings, per the stat bank's intended "entity-authority moat" design. `data/stat_bank.json` and `data/roadmap.json` are otherwise unmodified by this run except for the Status flip on Topic #2.
