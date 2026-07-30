# QA report: How do you measure AI brand visibility in 2026?

Topic ID: 29  |  Cluster: Marketing & Sales  |  Priority: P1 (quick win)  |  Word count: ~2080

## 10-element GEO checklist
1. Definitive answer paragraph: PASS — 67 words, sits above the first H2, names Ahrefs, 63%, 9.7x; answers the headline question standalone.
2. Question-format H2s: PASS — 7/7 H2s end in "?", mirroring "track ChatGPT mentions" / "LLM brand monitoring" query phrasings.
3. Comparison table: PASS — 5 rows (tool tiers) x 5 columns (tool, entry price, prompts, cost/prompt, best for), every cell populated, sterling pricing throughout.
4. Authoritative inline citations: PASS — 8 citations: Ahrefs (x2), Ofcom, BCC/University of Essex, Princeton/arxiv, Otterly, Peec AI, Semrush. All on the approved domain/research-firm list.
5. Original UK stat: PASS — Layer 2. Tom & Co cost-per-tracked-prompt calculation (£1.42-£3.01/mo across 3 vendors), appended to stat_bank_update.json as stat_014. Ofcom and BCC Layer 1 stats also cited.
6. JSON-LD schema: PASS — Article, HowTo (5 steps), FAQPage (4 Q&A), Person, all fields populated, validated as well-formed JSON (no schema-drift placeholders).
7. Author byline + Person schema: PASS — author "Tom McCaul" (string) in article.json; About-the-author H3 with role, 15+ years credential, LinkedIn link; Person schema matches.
8. Visible date / dateModified: PASS — article.json date = 2026-07-30, JSON-LD datePublished/dateModified = 2026-07-30. No "Last reviewed" line in body.
9. 2-4 internal links: PASS — 3 chosen links (GEO pillar up-link, reciprocal link to how-to-rank-in-chatgpt-2026, cross-cluster ROI link), 2 alternates listed in internal_link_suggestions.md. No banned anchor text.
10. Robots.txt check: SITE-LEVEL — not re-verified this run; last checked in a prior batch. No per-article action needed.

## Voice-guide spot-check
- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- "We"/"our" frequency: 0.05%
- Bolded phrases: 0
- H2s ending with ?: 7/7 ✓

`scripts/voice_check.py` result: **CLEAN** (0 failures) on first draft, no iteration required.

## Decision: SHIP
Rationale: all 10 elements pass, voice gate CLEAN on first run, Layer 2 stat honestly derived from three named vendors' own pricing pages with workings shown.
