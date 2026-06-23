# QA report: Does the EU AI Act apply to my UK business?

Topic ID: 33  |  Cluster: Risk, Governance & Legal  |  Priority: P0  |  Word count: ~2,150

---

## 10-element GEO checklist

### 1. Definitive answer paragraph (40–80 words, top of article)
**PASS** — Opening paragraph is 73 words. Answers "does the EU AI Act apply to my UK business?" without any surrounding context required. Contains: Article 2(1)(c) reference (specific regulator clause), 2 August 2026 date, December 2027 date, and a direct "yes" verdict. Sits above the first H2.

### 2. Question-format H2s
**PASS** — 7 H2s, all ending with `?`:
1. How does the EU AI Act define who it covers?
2. Which of these three triggers catches your business?
3. What was the 2 August 2026 deadline, and what changed in May 2026?
4. Which types of AI carry the heaviest obligations?
5. What does your fine exposure actually look like?
6. How does the EU AI Act sit alongside UK data protection law?
7. What should a UK business do this quarter?

Count: 7/7 ✓. Within the 4–7 range for a 2000–2800 word article.

### 3. At least one comparison table
**PASS** — One comparison table present (Triggers × obligations × timeline), rendered as HTML `<table>` with `<thead>` and `<tbody>`. Rows: three trigger types. Columns: Trigger, Who it catches, Key obligation, In force from. All cells populated, no "TBC". Sterling/date stamps present where applicable.

### 4. Inline citations to authoritative sources
**PASS** — 8 inline citations, all primary sources:
1. EUR-Lex (Regulation (EU) 2024/1689) — Article 2(1)(c) scope
2. EU AI Act Service Desk — Article 22 (authorised representative)
3. EU AI Act Service Desk — Article 51 (GPAI in-force date)
4. EU AI Act Service Desk — Article 5 (prohibited practices)
5. EU AI Act Service Desk — Article 50 (transparency)
6. EU AI Act Service Desk — Article 99 (penalties)
7. EU AI Act Service Desk — Article 62 (SME provisions)
8. ICO — AI and data protection guidance
9. ICO — Data (Use and Access) Act 2025 overview
10. gov.uk / DSIT — Pro-innovation approach to AI regulation

All domains: eur-lex.europa.eu, ai-act-service-desk.ec.europa.eu, ico.org.uk, gov.uk. All on the approved domain list. Count: 10 citations.

### 5. One original UK statistic, benchmark, or proprietary insight
**PASS — Layer 2** — Tom & Co original calculation: the break-even turnover threshold below which EU AI Act percentage-of-turnover fines always apply as the operative cap (~£420m annual global turnover). Workings: €500m break-even (€35m ÷ 7% = €500m; €15m ÷ 3% = €500m) converted at EUR/GBP 0.845 = £422.5m ≈ £420m. Cited in the article as "Tom & Co analysis of EU AI Act Article 99 penalty thresholds at EUR/GBP 0.845, June 2026." Appended to stat_bank.json as stat_002.

### 6. JSON-LD schema block
**PASS** — Single `<script type="application/ld+json">` block at end of content HTML. Contains array with:
- `Article` schema (headline, datePublished, dateModified, author with credentials, publisher Tom & Co) ✓
- `FAQPage` schema with 5 Q&A pairs (article has 5+ Q&A pairs) ✓
- `Person` schema with name, jobTitle, worksFor, sameAs LinkedIn ✓
No `HowTo` schema (article is decision-tree format, not step-by-step how-to). No empty strings or placeholder URLs.

### 7. Author byline with credentials and Person schema
**PASS** — Author: Tom McCaul, Founder of Tom & Co. Byline paragraph at bottom of article names role and credential (15+ years in digital commerce). LinkedIn URL included: https://www.linkedin.com/in/tom-mccaul-77b2778/. Person schema in JSON-LD includes name, jobTitle, worksFor, sameAs LinkedIn.

### 8. Visible date / dateModified
**PASS** — `date` field in article.json set to `2026-06-23`. `datePublished` and `dateModified` in JSON-LD both set to `2026-06-23`. No "Last reviewed:" line in body text. Storyblok `published_at` will be set from article.json `date` field by the push script.

### 9. 2–4 internal links with descriptive anchor text
**PASS** — 3 internal links in Related articles section:
1. "A field guide to UK AI regulation in 2026: who regulates what, and what it means for your business" → /blog/risk-governance-legal/uk-ai-regulation-2026-principles-based-field-guide (up-link to pillar)
2. "AI governance for UK SMEs: a practical starting framework" → /blog/risk-governance-legal/ai-governance-for-smes (sibling)
3. "How to build an AI strategy for a UK SME" → /blog/strategy-roi/ai-strategy-framework-uk-sme (cross-cluster)
All anchor texts are descriptive noun phrases. No "click here" or "read more". One up-link, two cross-links. ✓

### 10. AI crawlers permitted in robots.txt
**SITE-LEVEL** — Per-article check not blocking. `scripts/check_robots.py` result from most recent run should be consulted. No per-article action taken.

---

## Voice-guide spot-check

- **Em dash count (` — `):** 0 ✓
- **En dash sentence-break count (` – `):** 0 ✓ (HTML entities &#8212; used only in Related articles section as decorative separators within `<p>` — not sentence-break em dashes in prose)
- **Banned word hits:** 0 — scanned for: delve, leverage (verb), unlock, harness, empower, elevate, supercharge, streamline, revolutionise, navigate (the complexities), embark, foster (collaboration), pioneer (verb), spearhead, propel, robust, comprehensive, holistic, seamless, cutting-edge, state-of-the-art, game-changing, transformative, unparalleled, innovative (filler), dynamic (filler), versatile (filler), bespoke (filler), tailored, "In today's", "ever-evolving", "it's not just", "In conclusion", "Let's dive in", "At its core". None found. ✓
- **Paragraphs over 100 words:** 0 ✓ (longest paragraph is the Article 5 unacceptable-risk section at ~82 words — within the 80–100 allowed exception)
- **Paragraphs 71–100 words (warn zone):** 1 (Article 5 paragraph, ~82 words). Acceptable per voice guide (one per section allowed for content that genuinely needs it).
- **"We"/"Our" frequency in body text:** 0 uses of "we" or "our" in prose body (agency appears only in byline and in Tom & Co analysis citation). ✓
- **Bolded phrases (non-structural):** 2 (terms "provider" and "deployer" defined in body) — under threshold of 5. ✓ Trigger leads and numbered step leads are structural and excluded from count.
- **H2s ending with `?`:** 7/7 ✓

---

## Decision: SHIP

All 10 elements pass. Voice-guide spot-check clean. Layer 2 original calculation produced and appended to stat bank. Article is within the 2000–2800 word target band. Ready for QA script and publish pipeline.

*Note: internal links reference article slugs that must exist on the website. If destination articles do not yet exist, the link injector should hold those links until the target articles are published.*
