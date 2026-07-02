# QA report: What is the ROI of AI in business in 2026?

Topic ID: 1  |  Cluster: Strategy & ROI  |  Pillar: P1: AI strategy  |  Priority: P1  |  Quick win: Y
Word count: 1,542 (target band: 1500-2200) ✓
Drafted: 2026-07-02
Author: Tom McCaul, Founder, Tom & Co

## 10-element GEO checklist

1. **Definitive answer paragraph (40-80 words):** PASS — 67 words. Answers the headline question standalone: names the 54% adoption figure, the 6% McKinsey EBIT-impact figure, and the one-line mechanism (workflow redesign vs bolt-on chatbot).
2. **Question-format H2s:** PASS — 6/6 H2s end with `?`. Footer H3s (About the author, Related reading) do not count, per format-mapping.md.
3. **At least one comparison table:** PASS — 4-row x 5-column sterling pricing table (Microsoft 365 Copilot, ChatGPT Business, Claude Team Standard, Claude Team Premium) with price, billing basis, requirements and best-fit for each. Every cell has data, no "varies" or "TBC".
4. **Inline citations to authoritative sources:** PASS — 8 inline external citations: BCC/Essex (x2), ONS BICS ad hoc tables, McKinsey State of AI, Bain Automation and AI Pathfinder Survey 2026. All primary UK sources or named research firms with disclosed methodology. No agency blogs. (ONS ASHE 2025 and the GOV.UK NI rates page support the Layer 2 calculation and are cited in sources.md and stat_bank_update.json rather than inline, consistent with stat-sourcing.md's "no inline methodology block" rule.)
5. **One original UK statistic:** PASS — Layer 2. New Tom & Co calculation: applying McKinsey's reported 10-20% AI cost reduction to the fully loaded cost of a median UK employee (ONS ASHE 2025 + employer NI + pension) implies a £4,500-£9,000 per employee annual saving. Appended to `stat_bank.json` as `stat_008`. Also carries a Layer 1 stat (BCC/Essex, ONS BICS) as supporting evidence.
6. **JSON-LD schema:** PASS — Article + FAQPage (5 Q&A pairs, one per major H2) + Person (Tom McCaul, LinkedIn `sameAs`) + publisher Organization. Validated as parseable JSON with a standalone check (no `validate_jsonld.py` script present in the repo).
7. **Author byline + Person schema:** PASS — `author: "Tom McCaul"` (string). Person schema includes name, jobTitle (Founder), worksFor (Tom & Co), sameAs `https://www.linkedin.com/in/tom-mccaul-77b2778/`. "About the author" H3 present in body.
8. **Visible date / dateModified:** PASS — `article.json` `date` = 2026-07-02 (today). Article JSON-LD `datePublished` and `dateModified` both 2026-07-02. No "Last reviewed" line in the body (this replaces an earlier 29 April 2026 draft at the same slug that incorrectly included one).
9. **2-4 internal links with descriptive anchor text:** PASS — 3 internal links in "Related Tom & Co reading": chatgpt-vs-claude-vs-gemini-for-business, does-the-eu-ai-act-apply-to-my-uk-business, agentic-ai-use-cases-mid-market. All cross-cluster bridges (Technical & Build; Risk, Governance & Legal). No up-link to the AI-strategy pillar is possible yet because Topic #2 has not been written; flagged in `internal_link_suggestions.md` for a future refresh.
10. **AI crawlers permitted in robots.txt:** SITE-LEVEL — not re-checked this run; last site-level status should be read from `output/_robots_status.txt`.

## Voice-guide spot-check

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- "We"/"our" frequency: 0.00%
- Bolded phrases: 5 (the five numbered action-step leads in the final section; structural, matches the accepted pattern from topic #60)
- H2s ending with ?: 6/6 ✓

`python3 scripts/voice_check.py` result: **CLEAN** on first pass, no iteration needed.

## Decision: SHIP

Rationale: all 10 checklist elements pass or are correctly marked site-level/N-A, the voice gate is CLEAN on the first run, and the Layer 2 original calculation strengthens element 5 beyond the April draft it replaces.

## Note on topic re-selection

`scripts/pick_next_topic.py` returned Topic #1 because its roadmap `Status` field was empty. An output folder for this exact topic already existed at `output/2026-04-29-ai-roi-uk-business-2026/` (slug `ai-roi-uk-business-2026-what-the-evidence-actually-shows`), and that slug is already live in the GitHub Pages preview library and is referenced as an internal link from the published `chatgpt-vs-claude-vs-gemini-for-business` article. The April draft's roadmap Status was never set, which is why the picker offered it again. Rather than create a second, competing article on the same topic, this run treats the request as a refresh (SKILL.md input option 3): same slug, same topic ID, fully re-researched with July 2026 data, brought into line with the current output standards (the April draft predates the "no Last reviewed line" rule and the mandatory `key_stats.json` requirement). See `sources.md` for detail.
