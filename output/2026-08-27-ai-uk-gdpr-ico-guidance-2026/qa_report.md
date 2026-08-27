# QA report: What does the ICO's guidance mean for AI and UK GDPR in 2026?

Topic ID: 35 | Cluster: Risk, Governance & Legal | Priority: P1 | Word count: 2014

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 68 words, sits above the first H2, answers the headline question standalone, contains specific figures (5 February 2026, £17.5 million, 4%) and a named regulator (ICO) and scheme (Data (Use and Access) Act 2025).
2. **Question-format H2s**: PASS — 6/6 H2s end in `?`, within the 4-7 band for a 2,000-2,400 word article.
3. **Comparison table**: PASS — one `<table>` with `<thead>`/`<tbody>`, 5 rows (ICO guidance documents) x 4 columns (document, coverage, status, last updated), every cell populated, no "TBC" or "varies".
4. **Authoritative inline citations**: PASS — 9 inline citations across 2 distinct approved domains: legislation.gov.uk (x2, Data (Use and Access) Act 2025 and Section 80) and ico.org.uk (x7: core AI guidance, risk toolkit, generative AI consultation outcomes, draft ADM consultation, fining guidance, Upper Tribunal/Clearview press release, AI and biometrics strategy).
5. **Original UK statistic**: PASS (Layer 2) — new Tom & Co calculation (stat_022, 231 days between the Data (Use and Access) Act 2025 receiving royal assent and Section 80 taking effect) derived from two dates published separately on legislation.gov.uk, workings in `stat_bank_update.json`.
6. **JSON-LD schema**: PASS — single `<script type="application/ld+json">` block containing Article, FAQPage (7 Q&A pairs matching the answer paragraph plus all 6 H2s) and Person schemas. No HowTo schema (format is summary + checklist, not a numbered how-to).
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul"; About-the-author section present with role and credential; Person schema includes name, jobTitle, worksFor and sameAs LinkedIn URL.
8. **Visible date / dateModified**: PASS — `article.json` `date` = 2026-08-27 (today); JSON-LD `datePublished` and `dateModified` both 2026-08-27; no "Last reviewed" line in the body.
9. **2-4 internal links**: PASS — 4 distinct internal links (up-link to the Risk & Regulation pillar, two same-cluster siblings, one cross-cluster bridge to Strategy & ROI), each used once inline and once in "Related Tom & Co reading" with descriptive, non-banned anchor text.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; does not block this article per `scripts/check_robots.py`'s once-per-batch cadence.

## Voice-guide spot-check (from scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 0 ✓
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 5 (all structural numbered-list leads in the compliance checklist) ✓
- H2s ending with `?`: 6/6 ✓

Script result: **CLEAN**

## Research method note

Direct WebFetch access to ico.org.uk, gov.uk and legislation.gov.uk was blocked by this environment's network egress proxy (`EGRESS_BLOCKED` on all three domains). Every fact in this article was sourced via web search and cross-verified against at least two independent secondary legal-analysis sources (law firm client alerts, regulatory trackers) before use, and every inline citation points to the primary ico.org.uk / legislation.gov.uk page identified by that research, not to the secondary source. Recommend a human spot-check of the cited URLs before publish given the fetch restriction.

## Decision: SHIP

Rationale: all 9 per-article checklist elements pass (element 10 is a site-level, once-per-batch check), the voice gate returns CLEAN, word count (2014) sits inside the roadmap's 2,000-2,400 target band, and the article carries a genuine Layer 2 original UK statistic rather than leaning on Layer 1 alone. Flagging the research-method note above for Tom's awareness given the network restriction encountered this run.
