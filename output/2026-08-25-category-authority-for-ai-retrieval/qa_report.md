# QA report: How do you build category authority so AI tools retrieve your brand?

Topic ID: 30 | Cluster: Marketing & Sales | Priority: P1 | Word count: 2,315

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 79 words, sits above the first H2, answers the headline question standalone, contains a specific figure (71%), a named source (Ofcom) and a date (2026).
2. **Question-format H2s**: PASS — 7/7 H2s end in `?`. Count is at the upper end of the 4-7 band, justified by the 2,315-word length (roadmap target band 2,000-2,800).
3. **Comparison table**: PASS — one `<table>` with `<thead>`/`<tbody>`, 5 rows (platform type) x 4 columns (UK examples, what it signals, action to take), every cell populated, no "TBC".
4. **Authoritative inline citations**: PASS — 6 inline citations (excluding the author LinkedIn link) across 5 distinct sources: Ofcom (x2), British Chambers of Commerce, arxiv.org (Princeton/IIT Delhi GEO paper, KDD 2024), gov.uk (CMA case page), techuk.org. All resolve to approved domains.
5. **Original UK statistic**: PASS (Layer 2) — new Tom & Co calculation (stat_021, 71% of UK adults within reach of an AI-generated answer at least sometimes) derived from two Ofcom-published rates, workings in `stat_bank_update.json`. Also reuses the existing stat_012 (2.1m UK businesses using AI for marketing) from the bank as supporting context.
6. **JSON-LD schema**: PASS — single `<script type="application/ld+json">` block containing Article, FAQPage (7 Q&A pairs matching the 7 H2s) and Person schemas. No HowTo schema (format is strategy + checklist, not a numbered how-to).
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul"; About-the-author section present with role and credential; Person schema includes name, jobTitle, worksFor and sameAs LinkedIn URL.
8. **Visible date / dateModified**: PASS — `article.json` `date` = 2026-08-25 (today); JSON-LD `datePublished` and `dateModified` both 2026-08-25; no "Last reviewed" line in the body.
9. **2-4 internal links**: PASS — 4 distinct internal links (up-link to the GEO pillar, two same-cluster siblings, one cross-cluster bridge to Strategy & ROI), each used once inline and once in "Related Tom & Co reading" with descriptive (non-banned) anchor text.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; last checked per `output/_robots_status.txt` if present. Does not block this article.

## Voice-guide spot-check (from scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 1 (the 79-word answer paragraph, which is exempt — the voice guide sets its own 40-80 word band)
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 5 (all structural numbered-list leads in the "how to earn a place" checklist) ✓
- H2s ending with `?`: 7/7 ✓

Script result: **CLEAN**

## Decision: SHIP

Rationale: all 9 per-article checklist elements pass (element 10 is a site-level, once-per-batch check), the voice gate returns CLEAN, word count (2,315) sits inside the roadmap's 2,000-2,800 target band, and the article carries a genuine Layer 2 original UK statistic rather than leaning on Layer 1 alone.
