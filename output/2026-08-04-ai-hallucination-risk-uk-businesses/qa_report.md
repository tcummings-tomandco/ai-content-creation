# QA report: What is the AI hallucination risk for UK businesses?

Topic ID: 37  |  Cluster: Risk, Governance & Legal  |  Priority: P1 (quick win)  |  Word count: ~2016

## 10-element GEO checklist
1. Definitive answer paragraph: PASS — 80 words, sits above the first H2, names the High Court, £2,000 wasted costs, £89.4m claim, 18 fictitious authorities, SRA/judiciary/ICO; answers the headline question standalone.
2. Question-format H2s: PASS — 6/6 H2s end in "?", mirroring "AI hallucination risk" / "stop AI hallucinations" query phrasings from the roadmap row.
3. Comparison table: PASS — 4 rows (UK court/tribunal cases, 2023-2026) x 5 columns (case, year, court, fabricated citations, outcome), every cell populated with a specific fact, no "TBC"/"varies".
4. Authoritative inline citations: PASS — 10 citations: BAILII (Harber), judiciary.uk (Ayinde judgment, AI judicial guidance), caselaw.nationalarchives.gov.uk (Al-Haroun, Divisional Court), Law Gazette/Law Society (2026 county court referral), SRA (x2: Garfield.law authorisation, supervision guidance), ICO, FCA. All primary UK courts, regulators, or the Law Society's own publication.
5. Original UK stat: PASS — Layer 2. Tom & Co calculation: £800 in direct wasted costs per fabricated citation, derived from the Ayinde v Haringey judgment (£4,000 combined wasted costs / 5 fake citations). Appended to stat_bank_update.json as stat_015. Multiple Layer 1 stats (SRA, ICO, FCA, judiciary) also cited.
6. JSON-LD schema: PASS — Article, FAQPage (4 Q&A pairs), Person, all fields populated, no placeholder URLs. HowTo omitted: the format is "definition + mitigation", not a step-by-step framework.
7. Author byline + Person schema: PASS — author "Tom McCaul" (string) in article.json; About-the-author H3 with role, 15+ years credential, LinkedIn link; Person schema matches.
8. Visible date / dateModified: PASS — article.json date = 2026-08-04, JSON-LD datePublished/dateModified = 2026-08-04. No "Last reviewed" line in body.
9. 2-4 internal links: PASS — 3 chosen links (pillar up-link to the Risk & Regulation field guide, sibling link to the EU AI Act article, cross-cluster bridge to the AI for UK law firms piece). No banned anchor text; each anchor restates the destination's H1.
10. Robots.txt check: SITE-LEVEL — not re-verified this run; last checked in a prior batch. No per-article action needed.

## Voice-guide spot-check
- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- "We"/"our" frequency: 0.15%
- Bolded phrases: 5 (all numbered-list-item leads in the mitigation section, structural per voice-guide exception)
- H2s ending with ?: 6/6 ✓

`scripts/voice_check.py` result: **CLEAN** (0 failures) on first draft. Two paragraphs flagged as 71-100 word WARNs (the 80-word answer paragraph, which is within the mandated 40-80 word range by design, and one 75-word regulator paragraph, within the "one longer paragraph per major section" allowance). No iteration required.

## Decision: SHIP
Rationale: all 10 elements pass, voice gate CLEAN on first run, Layer 2 stat honestly derived from a single named, dated court judgment with workings shown, and every cited case cross-checked against a primary judiciary/National Archives/SRA source.
