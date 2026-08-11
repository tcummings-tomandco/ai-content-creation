# QA report: How are UK creative and media agencies using AI in 2026?

Topic ID: 64  |  Cluster: UK Industry Verticals  |  Priority: P1 (quick win)  |  Word count: 2118

## 10-element GEO checklist

1. Definitive answer paragraph: PASS — 75 words, sits directly above the first H2, names two specific figures (51% vs 33%), a named scheme (the government's 2026 AI Adoption Plan), a named regulator (Advertising Standards Authority) and a named case (Getty Images v Stability AI, November 2025). Answers the headline question standalone.
2. Question-format H2s: PASS — 7 H2s, all end in `?`: "What is the current state of AI adoption in UK creative and media agencies?", "What AI use cases are actually paying back for agencies right now?", "Is AI actually costing jobs at UK agencies?", "Which UK regulators and rules actually apply to agency AI use?", "What does the Getty Images v Stability AI ruling mean for agencies using AI tools?", "What funding is available for AI adoption in the UK creative industries?", "What should a UK creative or media agency do about AI in the next 90 days?"
3. Comparison table: PASS — one table, 4 rows (ICO, Intellectual Property Office, ASA/CAP, CMA) x 4 columns (regulator, what it covers, latest position, date). Every cell populated, no "TBC"/"varies".
4. Authoritative inline citations: PASS — 9 inline citations: gov.uk (AI Adoption Plan, DCMS Economic Estimates, copyright and AI statement of progress, Creative Industries Sector Plan news release), ons.gov.uk, marketingweek.com, ipa.co.uk (disclosed-methodology industry census, matches the checklist's "named industry survey with methodology" carve-out), asa.org.uk (the UK's advertising regulator, a primary UK authority), judiciary.uk (the UK courts service, the most primary possible source for a judgment). All primary UK sources, no agency blogs. See sources.md for the full list plus a "considered and not used" section flagging two figures (Innovate UK competition deadlines, an unverified advertising-and-marketing GVA sub-figure) that were deliberately left out rather than guessed.
5. Original UK stat: PASS (Layer 2) — Tom & Co analysis cross-referencing DCMS's 2023 creative-industries GVA sub-sector data with DSIT's 2026 AI-adoption sub-sector data: the sub-sector with the highest AI adoption (IT/software/computer services, 60%) is also the largest GVA contributor (£49.1bn of £124bn, nearly 40%). Appended to `stat_bank_update.json` as stat_017, with the cross-year caveat stated explicitly in both the article blockquote and sources.md.
6. JSON-LD schema: PASS — Article + FAQPage (6 Q&A pairs) + Person. No HowTo (format is a sector report, not a numbered how-to).
7. Author byline + Person schema: PASS — `author` field is the string "Tom McCaul". "About the author" H3 present with role, 15+ years credential, LinkedIn link. Person schema includes name, jobTitle, worksFor, sameAs.
8. Visible date / dateModified: PASS — article.json `date` = 2026-08-11 (today). JSON-LD `datePublished` and `dateModified` both 2026-08-11. No "Last reviewed" line in the body. Next review due: 2026-11-09 (today + 90 days, supporting-article cadence).
9. 2-4 internal links: PASS with caveat — 3 links chosen (GEO vs SEO, AI hallucination risk, AI vendor contract checklist), all cross-cluster bridges, plus 2 alternates listed for the injector. No pillar-hub up-link is possible because topic #64 is the first "UK Industry Verticals" cluster article published and no "P4: AI for UK industries" pillar piece exists yet; flagged in `internal_link_suggestions.md` for Tom.
10. Robots.txt check: SITE-LEVEL, not re-verified this run — `scripts/check_robots.py` is not present in this repo checkout. Carrying forward the prior batches' assumption that this is tracked separately; flagging so Tom can confirm cadence.

## Voice-guide spot-check (from `scripts/voice_check.py`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- Paragraphs 71-100 words: 5 (the answer paragraph, exempt by the voice guide's own rule, plus one per major section: the Layer 2 blockquote in the adoption section, the IPO-consultation paragraph in the regulators section, the trade-mark paragraph in the Getty section, and the British Business Bank paragraph in the funding section — each section carries at most one, consistent with the "one 80-100 word paragraph per major section" allowance)
- "We"/"our" frequency: 0.05%
- Bolded phrases: 6, all numbered-list item leads in the 90-day checklist (structural, excluded from the under-5 count per voice-guide.md)
- H2s ending with ?: 7/7 ✓

**voice_check.py result: CLEAN**

## Decision: SHIP

Rationale: all 10 elements PASS or PASS-with-caveat (caveats are structural, not content quality issues — no P4 pillar page exists yet since this is the first article in its cluster, and the site-level robots check script isn't in this checkout), the voice gate reports CLEAN, and the original Layer 2 stat is honestly derived, cross-year caveat disclosed in both the article and sources.md, and traceable to two independently corroborated primary UK sources. Getty Images v Stability AI (the highest-stakes single claim in the article) was independently corroborated against seven UK law-firm case notes after direct network access to judiciary.uk was blocked in this session, rather than relying on a single unverified search snippet.
