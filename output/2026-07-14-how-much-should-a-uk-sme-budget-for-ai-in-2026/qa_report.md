# QA report: How much should a UK SME budget for AI in 2026?

Topic ID: 5  |  Cluster: Strategy & ROI  |  Pillar: P1: AI strategy  |  Priority: P1 (Quick win: Y)
Word count: 1,804 (target band: 1800-2400) ✓
Drafted: 2026-07-14
Author: Tom McCaul, Founder, Tom & Co

## 10-element GEO checklist

1. **Definitive answer paragraph (40-80 words):** PASS — 71 words. Names the £1,710-£9,000 tooling range, the training-time cost, and the ICO's up-to-ten-week prior consultation window. Answers the headline question standalone.
2. **Question-format H2s:** PASS — 5/5 H2s end with `?`. Footer H3s (About the author, Related reading) and the three "beyond subscriptions" sub-topic H3s (Governance and DPIA time / EU AI Act exposure / Funding to offset the cost) do not count, per format-mapping.md's "promote 3+ named sub-topics to H3" guidance.
3. **At least one comparison table:** PASS — 5-row x 4-column sterling pricing table (tool, price/user/month, annual cost for a 10-seat team, best for). Every cell filled, no "TBC" or "varies".
4. **Inline citations to authoritative sources:** PASS — 8 distinct primary sources cited inline: BCC/University of Essex, McKinsey State of AI, ONS ASHE 2025, gov.uk Rates and thresholds for employers, DSIT AI Adoption Research, ICO DPIA guidance, the EU AI Act text (via Tom & Co's existing stat_002), and Innovate UK BridgeAI. All primary UK regulator/government sources or named research firms with disclosed methodology. Several unverifiable or non-primary claims found in research (EU AI Act SME cost aggregator blogs, an unconfirmed "£2-8 million SME AI spend" figure, an unconfirmed UK AI market-size forecast, an uncorroborated BridgeAI grant-recipient count) were explicitly rejected — see sources.md.
5. **One original UK statistic:** PASS — Layer 2. New Tom & Co calculation: blending five published UK AI subscription tiers into a single 10-seat team annual budget range of £1,710 to £9,000. Appended to `stat_bank.json` as `stat_010`. The article also reuses the existing `stat_002` EU AI Act break-even calculation as supporting Layer 1 context.
6. **JSON-LD schema:** PASS — Article + FAQPage (4 Q&A pairs, one per H2 excluding the final action-list H2) + Person (Tom McCaul, LinkedIn `sameAs`) + publisher Organization. Valid, parseable JSON.
7. **Author byline + Person schema:** PASS — `author: "Tom McCaul"` (string). Person schema includes name, jobTitle (Founder), worksFor (Tom & Co), sameAs `https://www.linkedin.com/in/tom-mccaul-77b2778/`. "About the author" H3 present in body.
8. **Visible date / dateModified:** PASS — `article.json` `date` = 2026-07-14 (today). JSON-LD `datePublished` and `dateModified` both 2026-07-14. No "Last reviewed" line in the body.
9. **2-4 internal links with descriptive anchor text:** PASS — 4 internal links in "Related Tom & Co reading": how-to-build-an-ai-strategy-for-a-uk-sme (pillar up-link), ai-roi-uk-business-2026-what-the-evidence-actually-shows (same-cluster), chatgpt-vs-claude-vs-gemini-for-business (cross-cluster, Technical & Build), does-the-eu-ai-act-apply-to-my-uk-business (cross-cluster, Risk, Governance & Legal). No banned anchor text.
10. **AI crawlers permitted in robots.txt:** SITE-LEVEL — not re-checked this run; see `output/_robots_status.txt` for the last site-level status.

## Voice-guide spot-check

`python3 scripts/voice_check.py` output:

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words (target ≤70): 8 WARN (each under the 80-100 word allowance format-mapping.md permits per major section)
- "We"/"Our" frequency: 0.00% ✓
- Bolded phrases: 5 ✓ (the five numbered action-step leads in the final section, structural, matches the accepted pattern used elsewhere in this engine)
- H2s ending with `?`: 5/5 ✓

**Result: CLEAN** after one length-expansion iteration (see note below), no voice-rule iteration needed.

## Decision: SHIP

Rationale: all 10 checklist elements pass or are correctly marked site-level, the voice gate is CLEAN, and the Layer 2 original calculation (a blended 10-seat AI tooling budget range from five vendors' published pricing) gives element 5 a genuine original-calculation pass.

## Note on topic re-selection and this draft's history

`scripts/pick_next_topic.py` initially returned Topic #3 ("AI use cases that pay back in year 1"), because the git branch this session started from had been forked from `main` before a separate routine run on 9 July 2026 had already completed that exact topic (same slug, `ai-use-cases-that-pay-back-in-year-one`, already live in Storyblok as story ID 196180586256698, roadmap Status "Approved — draft in Storyblok"). A full draft was written for Topic #3 before this was discovered on `git push` (rejected as non-fast-forward). That draft was discarded rather than pushed, to avoid a duplicate-slug conflict against an already-published Storyblok story. The branch was reset to the current `origin/main`, the picker was re-run against the up-to-date roadmap, and it returned Topic #5 ("How much should a UK SME budget for AI in 2026?"), which this article covers. No output folder or roadmap change from the discarded Topic #3 attempt was committed or pushed.

## Research integrity note

Several candidate data points were found during research and deliberately excluded: unverifiable or non-primary EU AI Act SME compliance-cost estimates from aggregator blogs, an unconfirmed "£2-8 million average SME AI spend" figure and an unconfirmed UK AI market-size forecast (both could not be traced to the underlying DSIT report, which returned HTTP 403 on direct fetch, and the market-size figure could not be corroborated on a follow-up search), and an uncorroborated BridgeAI grant-recipient count (£73.8m to 3,400+ organisations, appeared once but not on a second independent search). All are logged in `sources.md` under "Sources considered and rejected." The EU AI Act compliance-cost section relies instead on Tom & Co's own existing, disclosed calculation (stat_002) rather than an invented or unverifiable figure.
