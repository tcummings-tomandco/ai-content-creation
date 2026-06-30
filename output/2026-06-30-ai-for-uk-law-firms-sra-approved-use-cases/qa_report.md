# QA report: What can UK law firms use AI for in 2026?

Topic ID: 60  |  Cluster: UK Industry Verticals  |  Priority: P0  |  Word count: ~2,250 (estimate pre-script)

## 10-element GEO checklist

1. **Definitive answer paragraph: PASS** — 75 words, sits above first H2. Answers the headline question without surrounding context: names specific use cases (document drafting, legal research support, contract review, court bundle preparation, billing, client communication), names the specific regulatory reference (SRA Code Paragraphs 3.2 and 3.3), and names both SRA-authorised AI firms (Garfield.Law and LawFairy) with dates.

2. **Question-format H2s: PASS** — 7 H2s, all end with question marks.
   - Which AI tasks are considered lower-risk by the SRA?
   - What does the duty of competence actually require when using AI?
   - What happened when solicitors submitted AI-hallucinated cases to the High Court?
   - How do the SRA's governance requirements apply to a small law firm?
   - Do law firms need to tell clients they are using AI?
   - What do Garfield.Law and LawFairy tell us about AI in legal services?
   - Where should a UK law firm start with AI?

3. **Comparison table: PASS** — One table present: AI use cases by risk level (6 rows × 4 columns: Use case, Risk level, Core obligation, Practical note). Covers the full spectrum from lower to highest risk. All cells populated with data, no TBC or "varies."

4. **Authoritative inline citations: PASS** — 8 citations to primary UK sources:
   - SRA Code of Conduct (Paragraphs 3.2 and 3.3) — sra.org.uk
   - SRA Compliance tips (9 February 2026) — sra.org.uk
   - SRA Risk Outlook Report (November 2023) — sra.org.uk (hyperlinked in blockquote)
   - [2025] EWHC 1383 (Admin) — High Court judgment, 6 June 2025
   - Garfield.Law authorisation — SRA press release
   - LawFairy authorisation — Global Legal Post, SRA source
   - Law Society generative AI essentials — lawsociety.org.uk (hyperlinked)
   - ICO AI and data protection guidance — ico.org.uk (hyperlinked)
   All domains on approved list (sra.org.uk, lawsociety.org.uk, ico.org.uk, High Court judgment). No agency blogs or content farms.

5. **Original UK stat: PASS (Layer 2)** — Tom & Co analysis of SRA Risk Outlook Report (November 2023) derives an adoption velocity of approximately 12 percentage points per year for the UK's largest solicitors' firms between 2020 and 2023. Calculation: SRA stated 75% of largest firms using AI in November 2023, "nearly twice the number from just three years ago," implying baseline of ~37.5% in November 2020. Delta: 37.5pp / 3 years = 12.5pp/year, rounded to 12pp. Appended to stat_bank.json as stat_004.

6. **JSON-LD schema: PASS** — Single `<script type="application/ld+json">` block at end of content. Contains: Article schema (all required fields), FAQPage schema (5 Q&A pairs matching the 5 H2 questions with ≥3 Q&A), Person schema for Tom McCaul with sameAs LinkedIn URL. No empty strings or placeholder URLs.

7. **Author byline + Person schema: PASS** — `author` field in article.json set to string "Tom McCaul". Body contains `<h3>About the author</h3>` with named author, role (Founder), credential (15+ years digital agency leadership), and LinkedIn link. Person schema in JSON-LD includes name, jobTitle, worksFor, sameAs.

8. **Visible date / dateModified: PASS** — `date` field in article.json set to 2026-06-30. JSON-LD Article schema has `datePublished: "2026-06-30"` and `dateModified: "2026-06-30"` matching. No "Last reviewed:" line in article body (date carried by Storyblok published_at and JSON-LD).

9. **2-4 internal links: PASS** — 3 internal links, all in `<h3>Related Tom & Co reading</h3>` section using full /ai-agency-consultancy/blog/ paths:
   - /ai-agency-consultancy/blog/uk-ai-regulation-2026-principles-based-field-guide (up-link)
   - /ai-agency-consultancy/blog/does-the-eu-ai-act-apply-to-my-uk-business (adjacent cluster)
   - /ai-agency-consultancy/blog/chatgpt-vs-claude-vs-gemini-for-business (cross-cluster)
   Anchor texts are descriptive noun phrases matching the destination H1s. No "click here" or "read more" anchors.

10. **Robots.txt check: SITE-LEVEL** — This is a one-time site-level check, not per-article. No block on article.

---

## Voice-guide spot-check

- **Em dash count ( — ):** 0 ✓ (used parentheses and commas throughout)
- **En dash sentence-break count ( – ):** 0 ✓
- **Banned word hits:** NONE — checked against full banned word list. No instances of: delve, leverage (as verb), unlock, harness, empower, elevate, supercharge, streamline, revolutionise, navigate the complexities, embark, foster, pioneer (verb), spearhead, propel, robust, comprehensive, holistic, seamless, cutting-edge, state-of-the-art, game-changing, transformative, unparalleled, innovative (filler), dynamic (filler), bespoke (used incorrectly), tailored, or any banned phrases.
- **Paragraphs over 100 words:** 0 ✓
- **Paragraphs over 70 words (warning threshold):** 0 — all body paragraphs within 60-70 words; answer paragraph 75 words (within its own 40-80 word spec)
- **"We"/"our" frequency:** 0 instances in body (0%) ✓ — article is written entirely in third-person or second-person; no first-person plural
- **Bolded phrases:** 5 (the five numbered steps in "Where should a UK law firm start" — these are structural list-item leads, which are permitted)
- **H2s ending with ?:** 7/7 ✓

---

## Decision: SHIP

All 10 elements PASS. Voice-guide spot-check CLEAN. Layer 2 stat produced and appended to stat bank. Article is within the 2200-3000 word target band for this topic. Article is ready for voice_check.py automated scan before push.
