# QA report: What does a DPIA for AI need to include under UK GDPR?

Topic ID: 36 | Cluster: Risk, Governance & Legal | Priority: P1 | Word count: 2012

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 65 words, sits above the first H2, answers the headline question standalone, contains specific figures (seven-step ICO process, £8.7 million, 2%) and a named regulator (ICO).
2. **Question-format H2s**: PASS — 6/6 H2s end in `?`, within the 4-7 band for a 2,000-2,400 word article.
3. **Comparison table**: PASS — one `<table>` with `<thead>`/`<tbody>`, 6 rows (DPIA template sections) x 3 columns (section, standard question, AI-specific addition), every cell populated, no "TBC" or "varies".
4. **Authoritative inline citations**: PASS — 10 inline citations across 2 approved domains: ico.org.uk (x9: examples of high-risk processing, when do we need a DPIA, how do we do a DPIA, four individual step pages, the DPIA template, do we need to consult the ICO, MediaLab enforcement, fining guidance) and ons.gov.uk (x1: AI in UK businesses).
5. **Original UK statistic**: PASS (Layer 2) — new Tom & Co calculation (stat_023: the ICO's maximum prior-consultation wait is 75% longer than its standard window, 98 days versus 56) derived from two figures the ICO publishes separately, workings in `stat_bank_update.json`.
6. **JSON-LD schema**: PASS — single `<script type="application/ld+json">` block containing Article, FAQPage (7 Q&A pairs matching the answer paragraph plus all 6 H2s), HowTo (the 7-step ICO DPIA process), and Person schemas. JSON-LD block validated as parseable JSON with all four expected `@type` entries present.
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul"; About-the-author section present with role and credential; Person schema includes name, jobTitle, worksFor and sameAs LinkedIn URL.
8. **Visible date / dateModified**: PASS — `article.json` `date` = 2026-09-01 (today); JSON-LD `datePublished` and `dateModified` both 2026-09-01; no "Last reviewed" line in the body.
9. **2-4 internal links**: PASS — 4 distinct internal links (up-link to the Risk & Regulation pillar, two same-cluster siblings, one cross-cluster bridge to Strategy & ROI), each used once inline and once in "Related Tom & Co reading" with descriptive, non-banned anchor text.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; does not block this article per `scripts/check_robots.py`'s once-per-batch cadence.

## Voice-guide spot-check (from scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 0 ✓
- "We"/"our" frequency: 0.05% ✓
- Bolded phrases: 5 (all structural numbered-list leads in the quarterly action list) ✓
- H2s ending with `?`: 6/6 ✓

Script result: **CLEAN**

## Research method note

Direct WebFetch access to ico.org.uk and ons.gov.uk was blocked by this environment's network egress proxy (`EGRESS_BLOCKED`), consistent with prior runs. Every fact in this article was sourced via web search and cross-verified against at least one independent secondary source before use; every inline citation points to the primary ico.org.uk / ons.gov.uk page identified by that research, not to the secondary source. The ICO's seven-step DPIA process and the naming of Steps 1, 3, 4 and 7 were confirmed against live ico.org.uk URLs surfaced in search results (the children's code DPIA worked-example tool); Steps 2, 5 and 6 follow the same well-documented ICO structure but were not confirmed against a distinct live ICO URL for each. The MediaLab.AI enforcement figures (£247,590, 4 February 2026) and the ONS 29%/June 2026 adoption figure were both corroborated by multiple independent search results. Recommend a human spot-check of the ICO step-naming and the two figures above before publish given the fetch restriction.

## Decision: SHIP

Rationale: all 9 per-article checklist elements pass (element 10 is a site-level, once-per-batch check), the voice gate returns CLEAN, word count (2012) sits inside the roadmap's 2,000-2,400 target band, and the article carries a genuine Layer 2 original UK statistic rather than leaning on Layer 1 alone. Flagging the research-method note above for Tom's awareness given the network restriction encountered this run, particularly around independent verification of ICO Steps 2, 5 and 6 naming.
