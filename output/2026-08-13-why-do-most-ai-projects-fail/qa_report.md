# QA report: Why do most AI projects fail, and is 95% actually true?

Topic ID: 7  |  Cluster: Strategy & ROI  |  Priority: P1  |  Word count: 1806

## 10-element GEO checklist

1. Definitive answer paragraph: PASS — 76 words, sits directly above the first H2, names two specific figures (95%, and the ONS 12%-to-35% figure), a named research body (MIT) and a named UK statistics authority (ONS), a specific date (July 2025). Answers the headline question standalone: what the "95% fail" claim actually measures, and what the UK data shows.
2. Question-format H2s: PASS — 6 H2s, all end in `?`: "What does the data actually show about AI project failure?", "Why does the \"95% fail\" headline get the story wrong?", "What does the UK's own AI adoption data reveal?", "Which AI projects actually succeed, and what do they have in common?", "What should a UK leader do differently this quarter?", "How do you tell if your AI project is failing or just early?"
3. Comparison table: PASS — one table, 5 rows (the five most-repeated AI-failure claims) x 4 columns (the claim, how it's usually read, what the evidence shows, primary source). Every cell populated, no "TBC"/"varies".
4. Authoritative inline citations: PASS with one flagged judgement call — 8 inline citations: MIT Project NANDA (academic/primary research, disclosed methodology), RAND Corporation (named policy-research institute, disclosed methodology, not on checklist's explicit named-firm list but directly analogous in standing to Bain/BCG; flagged in sources.md), McKinsey (explicitly approved), ons.gov.uk, britishchambers.org.uk (explicitly approved), nao.org.uk x2 (UK's supreme audit institution, primary official source, same class as gov.uk/ico/fca), computerweekly.com (explicitly approved). No agency blogs, no undated reports. See sources.md for full list, the RAND judgement call, and a "considered and not used" section on Deloitte and Gartner figures deliberately left out.
5. Original UK stat: PASS (Layer 2) — Tom & Co analysis deriving a single ratio (2.5x) from two time series already published in the same ONS release (adoption breadth growth vs depth-of-use growth), quantifying the UK's own version of MIT's "GenAI Divide". Appended to `stat_bank_update.json` as stat_018, workings shown in full.
6. JSON-LD schema: PASS — Article + FAQPage (4 Q&A pairs) + Person. No HowTo (format is analysis/counter-narrative, not a numbered how-to).
7. Author byline + Person schema: PASS — `author` field is the string "Tom McCaul". "About the author" H3 present with role, 15+ years credential, LinkedIn link. Person schema includes name, jobTitle, worksFor, sameAs.
8. Visible date / dateModified: PASS — article.json `date` = 2026-08-13 (today). JSON-LD `datePublished` and `dateModified` both 2026-08-13. No "Last reviewed" line in the body. Next review due: 2026-11-11 (today + 90 days, supporting-article cadence).
9. 2-4 internal links: PASS with caveat — 3 links chosen (AI use cases that pay back in year one, AI vendor contract checklist, AI ROI in business 2026), plus 2 alternates listed for the injector. No genuine pillar-hub up-link is possible because no "P1: AI strategy" pillar article exists yet in the roadmap (topics #1-#10 and #75 are all supporting-length); used the closest existing hub-style piece (topic #1, AI ROI) instead and flagged this in `internal_link_suggestions.md`.
10. Robots.txt check: SITE-LEVEL, not re-verified this run — `scripts/check_robots.py` is not present in this repo checkout. Carrying forward the prior batches' assumption that this is tracked separately.

## Voice-guide spot-check (from `scripts/voice_check.py`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- Paragraphs 71-100 words: 3 (the answer paragraph, exempt by the voice guide's own rule, plus one each in the "UK adoption data" section covering the BCC and NAO 2024 findings; both are within the "one 80-100 word paragraph per major section" allowance for that single, data-dense section)
- "We"/"our" frequency: 0.00%
- Bolded phrases: 8, all numbered-list item leads across the two action lists (structural, excluded from the under-5 count per voice-guide.md)
- H2s ending with ?: 6/6 ✓

**voice_check.py result: CLEAN**

## Decision: SHIP

Rationale: all 10 elements PASS or PASS-with-caveat (caveats are structural: no P1 pillar page exists yet, and the site-level robots script isn't in this checkout), the voice gate reports CLEAN, and the original Layer 2 stat is an honest, fully-shown derivation from a single primary UK dataset (ONS). One inline source (RAND) required a judgement call rather than a literal match to the checklist's named-firm list; the reasoning is documented in sources.md for Tom's review, following the same precedent set by prior articles' handling of IPA and judiciary.uk. Two potentially punchier but under-verified figures (a specific Deloitte pilot-to-production percentage, and Gartner's commonly quoted failure rate) were deliberately excluded rather than guessed.
