# QA report: What's the lightest AI governance framework for a UK SME?

Topic ID: 42 | Cluster: Risk, Governance & Legal | Priority: P1 | Word count: 2136

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 68 words, sits above the first H2, answers the headline question standalone, contains specific figures/entities (2026, December 2025, ICO, AI Management Essentials, ISO/IEC 42001).
2. **Question-format H2s**: PASS — 7/7 H2s end in `?`, within the 4-7 band (article sits at the top of the 2,000-2,800 word band for topic 42, which format-mapping's 2,000-3,000 band supports).
3. **Comparison table**: PASS — one `<table>` with `<thead>`/`<tbody>`, 3 rows (ICO accountability framework, DSIT AI assurance guidance, ISO/IEC 42001) x 5 columns (framework, what it is, cost, mandatory, best for), every cell populated, no "TBC" or "varies".
4. **Authoritative inline citations**: PASS — 10 inline citations across 5 distinct approved domains: gov.uk (x5: AIME guidance, AIME government response, trusted third-party AI assurance roadmap, MHRA software-as-a-medical-device, AI Opportunities Action Plan), ico.org.uk (x1), britishchambers.org.uk (x1), lawsociety.org.uk (x1), fca.org.uk (x2: AI approach, Mills Review).
5. **Original UK statistic**: PASS (Layer 2) — reused the existing Tom & Co calculation `stat_001` from `data/stat_bank.json` (£2.6bn direct UK government AI funding, Recipe E), which already lists topic ID 42 in its `applies_to` field. No new Layer 2 derivation was needed, so no `stat_bank_update.json` is included in this run's outputs.
6. **JSON-LD schema**: PASS — single `<script type="application/ld+json">` block containing Article, FAQPage (8 Q&A pairs: the answer paragraph plus all 7 H2s) and Person schemas. No HowTo schema (format is a regulator/framework explainer with a checklist close, not a numbered how-to).
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul"; About-the-author section present with role and credential; Person schema includes name, jobTitle, worksFor and sameAs LinkedIn URL.
8. **Visible date / dateModified**: PASS — `article.json` `date` = 2026-09-08 (today); JSON-LD `datePublished` and `dateModified` both 2026-09-08; no "Last reviewed" line in the body.
9. **2-4 internal links**: PASS — 4 distinct internal links (up-link to the Risk & Regulation pillar, two same-cluster siblings, one cross-cluster bridge to the UK Industry Verticals cluster), each used once inline and once in "Related Tom & Co reading" with descriptive, non-banned anchor text.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; does not block this article per `scripts/check_robots.py`'s once-per-batch cadence.

## Voice-guide spot-check (from scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 (MHRA/Software as a Medical Device paragraph, 76 words; allowed under voice-guide's "one 80-100 word paragraph per major section" exception)
- "We"/"our" frequency: 0.05% ✓
- Bolded phrases: 5 (all structural numbered-list leads in the closing checklist) ✓
- H2s ending with `?`: 7/7 ✓

Script result: **CLEAN**

## Research method note

Direct WebFetch/curl access to gov.uk, ico.org.uk, fca.org.uk, ons.gov.uk, legislation.gov.uk, britishchambers.org.uk, techuk.org, parliament.uk, sra.org.uk and ofcom.org.uk was blocked by this environment's network egress proxy (`EGRESS_BLOCKED` on WebFetch, `403` CONNECT-tunnel-failed on direct curl to every one of those domains tested). This matches the restriction logged in the 2026-08-27 GDPR article's QA report.

Every fact in this article was sourced via WebSearch restricted to the primary domain in question (`allowed_domains`), so each citation URL and the fact it supports both came directly from a snippet of the primary source page itself, not from a secondary summary or an unverified agency blog. The AIME shelving story (element central to this article) was independently corroborated across three separate domain-restricted searches against gov.uk before being used. Recommend a human spot-check of the cited URLs before publish given the fetch restriction.

## Decision: SHIP

Rationale: all 9 per-article checklist elements pass (element 10 is a site-level, once-per-batch check), the voice gate returns CLEAN, word count (2,136) sits inside the roadmap's 2,000-2,800 target band for this topic, and the article carries a genuine Layer 2 original UK statistic (reused from the stat bank, which had already anticipated this topic). Flagging the research-method note above for Tom's awareness given the network restriction encountered this run.
