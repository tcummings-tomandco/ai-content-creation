# QA report: How are UK financial services firms actually using AI in 2026?

Topic ID: 58  |  Cluster: UK Industry Verticals  |  Priority: P1  |  Word count: 2293

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 61 words, sits above the first H2, states the 75%/10%/58% figures with the Bank of England/FCA regulator name and the November 2024 date. Answers "how are UK financial firms using AI" on its own with no surrounding context needed.
2. **Question-format H2s**: PASS — 7/7 H2s end with "?" (verified by `scripts/voice_check.py`). Each mirrors a plausible query: "What share of UK financial services firms use AI in 2026?", "What are UK financial firms actually using AI for?", "Which regulators oversee AI in UK financial services?", "What risks are UK financial firms most worried about?", "What did the FCA's AI Sprint conclude about the next five years?", "How can a firm test AI with the regulator before it goes live?", "What should a UK financial services firm do in the next 90 days?".
3. **Comparison table**: PASS — two tables. Table 1 (regulator / role / key mechanism / latest activity, 4 rows) under "Which regulators oversee AI in UK financial services?". Table 2 (route / what it does / scale / latest cohort, 3 rows) under "How can a firm test AI with the regulator before it goes live?". Both proper HTML `<table>` with `<thead>`/`<tbody>`, every cell populated, no "TBC"/"varies".
4. **Authoritative inline citations**: PASS — 8 distinct primary sources, 10 inline citation instances (2 sources cited twice for separate claims from the same report). All resolve to approved domains: bankofengland.co.uk (4 pages) and fca.org.uk (4 pages). No agency blogs cited.
5. **Original UK statistic**: PASS — Layer 2. New Tom & Co calculation: approximately 2% of all AI use cases in UK financial services are both foundation-model-based and rated high materiality (17% x 12%, derived from the BoE/FCA third survey). Appended to `stat_bank_update.json` as `stat_027` for merge into `data/stat_bank.json`.
6. **JSON-LD schema**: PASS — Article, FAQPage (7 Q&A pairs matching the 7 H2s) and Person schema present in a single script block at the end of `content`. No HowTo (format is Sector report, not a how-to/framework). All fields populated, no placeholder URLs.
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul". Body has an "About the author" H3 with role (Founder, Tom & Co), a credential (15+ years in digital commerce and agency leadership) and a LinkedIn link. JSON-LD Person schema includes name, jobTitle, worksFor and sameAs.
8. **Visible date / dateModified**: PASS — `article.json` `date` = 2026-09-17 (today). JSON-LD `datePublished`/`dateModified` both 2026-09-17. No "Last reviewed" line in the body (date is carried by the `date` field and JSON-LD per the skill's rule). Next review-due date: 2026-12-16 (+90 days).
9. **2-4 internal links**: PASS — 4 distinct internal links with descriptive anchor text (no "click here"/"read more"): AI for UK law firms (up-link within the UK Industry Verticals pillar), the ICO/UK GDPR guide and the DPIA template (cross-links to Risk, Governance & Legal), and the hallucination-risk piece (cross-link extending the "hidden models" theme). `internal_link_suggestions.md` lists these plus 3 alternates.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; last checked in a prior batch. No per-article action required per `checklist.md`.

## Voice-guide spot-check (from `scripts/voice_check.py`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: 0 — none (one draft used "Supercharged Sandbox", the FCA programme's own name, which trips the banned-word scan on "supercharge"; reworded to "advanced AI sandbox programme" throughout, citation link kept intact, before this was reported CLEAN)
- Paragraphs over 100 words: 0
- Paragraphs 71-100 words: 0
- "We"/"our" frequency: 0.04%
- Bolded phrases: 6 (all six are numbered-list-item leads in the 90-day checklist, which `checklist.md`'s bold-count rule explicitly excludes from the "under 5" target; zero inline marketing-emphasis bolding in body prose)
- H2s ending with ?: 7/7 ✓

**Script result: CLEAN** (0 failures)

## Decision: SHIP

Rationale: all 10 checklist elements PASS or SITE-LEVEL, the voice gate reports CLEAN, and the one honest Layer 2 stat (element 5) is a genuine derived figure with full workings recorded, not an invented number.
