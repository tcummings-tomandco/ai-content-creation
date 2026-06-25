# QA report: ChatGPT, Claude, or Gemini: which LLM is right for your UK business?

Topic ID: 47  |  Cluster: Technical & Build  |  Priority: P0  |  Word count: 2,373

---

## 10-element GEO checklist

**1. Definitive answer paragraph: PASS**
- Word count: 75 words (within 40-80)
- Answers the headline question independently: Yes. Names all three platforms, specifies the use-case fit for each, includes specific price range (£16-25/user/month), specific date (October 2025 for UK data residency), and specific technical figure (1M-token context window).
- Sits above the first H2: Yes.

**2. Question-format H2s: PASS**
- Count: 6 H2s (within 4-7 range for 2000-3000 word article)
- All 6 end with ?: Yes (6/6)
- Questions:
  1. What are the main options for a UK business team in 2026?
  2. How do the pricing plans compare in pounds?
  3. Which model scores highest on independent benchmarks?
  4. What does a business AI subscription actually cost a UK team?
  5. How do they handle UK data and compliance requirements?
  6. Which platform should a UK SME choose?
- Mirror likely query phrasings from roadmap row: Yes ("ChatGPT vs Claude vs Gemini for business")

**3. Comparison table: PASS**
- Tables present: 2
  - Table 1: Platform × pricing/context/residency comparison (6 cols, 3 data rows)
  - Table 2: Use case × best fit × reason decision table (3 cols, 8 data rows)
- Rendered as proper HTML `<table>` with `<thead>` and `<tbody>`: Yes
- Sterling pricing included: Yes (£ figures in all pricing cells)
- No empty "TBC" cells: Confirmed — all cells have data

**4. Inline citations to authoritative sources: PASS**
- Count: 8 inline citations (within 5-10)
- Domains cited:
  - vellum.ai — Vellum LLM Leaderboard (approved for Technical & Build cluster per format-mapping.md)
  - llm-stats.com — LLM benchmark tracking (approved: Technical & Build cluster)
  - lmcouncil.ai — LM Council benchmark suite (benchmark tracking, Technical & Build)
  - ons.gov.uk — ONS ASHE 2024 median earnings (approved primary UK statistical authority)
  - ico.org.uk — ICO AI and data protection guidance (approved regulator)
  - gov.uk — DSIT UK AI Safety commitments (approved UK government source)
  - fca.org.uk — FCA DP5/5 AI Foundation Models discussion paper (approved regulator)
  - britishchambers.org.uk — BCC/University of Essex March 2026 survey (approved: named survey with methodology)
- No agency blogs, content farms, or undated sources: Confirmed
- All citations link to primary sources: Confirmed

**5. One original UK statistic, benchmark, or proprietary insight: PASS (Layer 2)**
- Layer 2 calculation performed: Yes
- Stat: A 10-person UK knowledge-worker team spending ~£1,900/year on a business AI subscription needs each person to save roughly 9 minutes per week for the cost to break even.
- Method: Recipe D (cost-per-outcome ratio). ONS ASHE 2024 median earnings (£728/week = £37,856/year) + employer NI (13.8% above £9,100) + employer pension (3% above £6,240) = ~£42,800/year total employer cost per employee. At 1,800 productive hours/year: £23.78/hour. ChatGPT Business annual at ~£16/user/month × 10 users = £1,920/year. Per-person break-even: £192 / £23.78 = 8.07 hours/year = 9.3 minutes/week.
- Attribution in article: "Tom & Co analysis applying ONS ASHE 2024 median earnings data to published vendor pricing (June 2026)"
- Appended to stat bank: Yes (stat_bank_update.json — stat_003)

**6. JSON-LD schema block: PASS**
- Single `<script type="application/ld+json">` block at end of content: Yes
- Schemas included: Article (always required), FAQPage (5 Q&A pairs — threshold met), Person (Tom McCaul with LinkedIn sameAs)
- HowTo schema: N/A (format is Comparison, not How-To)
- All required fields populated: Yes (headline, datePublished, dateModified, author with worksFor, publisher with logo, mainEntityOfPage)
- No empty strings or placeholder URLs: Confirmed

**7. Author byline with credentials and Person schema: PASS**
- `author` field in article.json: "Tom McCaul" (string, per format-mapping.md)
- About the author section present (H3 heading): Yes
- Content includes: name, role (Founder, Tom & Co), credential (15+ years digital commerce and agency leadership), LinkedIn link
- Person schema in JSON-LD: Yes (name, jobTitle, worksFor, sameAs LinkedIn URL)

**8. Visible date / dateModified: PASS**
- `date` field in article.json: "2026-06-25" (today, date of drafting)
- No "Last reviewed:" line in article body: Confirmed absent
- `datePublished` in JSON-LD Article schema: "2026-06-25" — matches `date` field ✓
- `dateModified` in JSON-LD Article schema: "2026-06-25" — matches ✓
- Roadmap `Notes` 90-day review date: 2026-09-23 (to be recorded by mark_topic_done.py)

**9. 2-4 internal links with descriptive anchor text: PASS**
- Count: 3 internal links (within 2-4)
- Links placed:
  1. `/ai-agency-consultancy/blog/ai-roi-uk-business-2026-what-the-evidence-actually-shows` — "What is the ROI of AI in business in 2026? An honest UK evidence review" (cross-cluster: Strategy & ROI)
  2. `/ai-agency-consultancy/blog/does-the-eu-ai-act-apply-to-my-uk-business` — "Does the EU AI Act apply to my UK business?" (cross-cluster: Risk, Governance & Legal)
  3. `/ai-agency-consultancy/blog/uk-ai-regulation-2026-principles-based-field-guide` — "A field guide to UK AI regulation in 2026" (cross-cluster: Risk, Governance & Legal)
- Anchor text: All contain noun phrases from the destination article's H1 ✓
- Banned anchors ("click here", "read more", "learn more" etc.): None ✓
- Pillar up-link: Pillar 5 (Building with AI) hub article does not yet exist. Closest substitute: the AI ROI and regulation articles serve as adjacent cluster bridges. Flag: add pillar up-link when P5 hub is drafted.

**10. AI crawlers permitted in robots.txt: SITE-LEVEL (cannot verify this run)**
- `scripts/check_robots.py` not found in this environment. No `output/_robots_status.txt` available.
- **Action required**: Verify that https://www.tomandco.co.uk/robots.txt allows GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended. This is a site-wide config check, not a per-article blocker.

---

## Voice-guide spot-check (from voice_check.py output)

- Em dash count (` — `): **0** ✓
- En dash sentence-break count (` – `): **0** ✓
- Banned word hits: **0** ✓
- Paragraphs over 100 words: **0** ✓
- Paragraphs 71-100 words (warnings): **9** — within acceptable range (none exceed 100 words, which is the failure threshold)
- 'We'/'Our' frequency: **0.00%** ✓ (well under 1%)
- Bolded phrases in body: **3** ✓ (under limit of 5; all are structural "Choose X if" paragraph leads)
- H2s ending with ?: **6/6** ✓

---

## Decision: SHIP

**Rationale**: All 10 GEO elements PASS or are SITE-LEVEL (element 10, robots.txt — not a per-article blocker). Voice check returns CLEAN. Word count 2,373 within the 2000-3000 target band. Layer 2 original UK stat derived, methodology documented, stat_bank_update.json ready to merge. 8 inline citations to approved primary UK sources.
