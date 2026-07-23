# QA report: What is GEO and how is it different from SEO?

Topic ID: 21  |  Cluster: Marketing & Sales  |  Priority: P1 (quick win)  |  Word count: 2036

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 69 words, sits directly under the H1, above the first H2. Names the mechanism (structuring content so generative engines cite it), the specific engines (ChatGPT, Claude, Perplexity, Google's AI Overviews), and a dated, sourced figure (Princeton's 2024 GEO study, up to 40% citation lift), so it answers "what is GEO and how does it differ from SEO" on its own with no surrounding context required.
2. **Question-format H2s**: PASS — 8/8 H2s end with `?`. Each mirrors the roadmap row's likely query phrasings ("what is GEO", "GEO vs SEO") or a natural follow-up (why it matters, who's doing it, what improves it, how to measure it, what to do next).
3. **Comparison table**: PASS — one table under "How is GEO different from traditional SEO?", 6 rows x 2 option columns (SEO, GEO), every cell populated with specific content, no "TBC"/"varies". Required for this "vs" format and placed early, right where the format-mapping template calls for it.
4. **Authoritative inline citations**: PASS — 5 inline citations (excluding internal links and the author's LinkedIn link): arxiv.org (Princeton/KDD peer-reviewed paper), ofcom.org.uk, britishchambers.org.uk, gov.uk, ons.gov.uk. All primary UK regulator/official-statistics sources or a peer-reviewed academic paper. No agency blogs, content farms, or Wikipedia used as primary sources; several SEO-tool-vendor blogs with unverifiable UK AI-search-traffic numbers were identified during research and explicitly excluded (see sources.md).
5. **Original UK statistic**: PASS (Layer 2) — new Tom & Co calculation: roughly 2.1 million UK businesses now use AI for marketing or content work, combining the BCC/Essex/Atos 2026 survey (54% of UK SMEs use AI, 72% of AI-using SMEs apply it to marketing) with gov.uk's 5,499,000 UK private-sector business population estimate. Full workings in `stat_bank_update.json` and `sources.md`. Appended to `data/stat_bank.json` as `stat_012`.
6. **JSON-LD schema**: PASS — Article + FAQPage (5 Q&A pairs) + Person, single script block at the end of `content`. No HowTo (format is "Definition + comparison", not a numbered how-to). Verified the block parses as valid JSON and contains 3 schema objects with no placeholder URLs or empty required fields (no `validate_jsonld.py` script exists in this repo to run automatically; validated manually by parsing the JSON-LD and checking required fields).
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul". Body has an `<h3>About the author</h3>` section naming Tom McCaul, Founder, Tom & Co, 15+ years in digital commerce, with LinkedIn link. Person schema includes name, jobTitle, worksFor, sameAs.
8. **Visible date / dateModified**: PASS — `article.json` `date` = 2026-07-23 (today). JSON-LD `datePublished`/`dateModified` both 2026-07-23. No "Last reviewed" line in the body. Next review-due date to record in roadmap `Notes`: 2026-10-21 (+90 days).
9. **2-4 internal links**: PASS — 3 internal links, each used inline in the body and again in "Related Tom & Co reading": `chatgpt-vs-claude-vs-gemini-for-business` (cross-cluster bridge to Technical & Build — the exact engines GEO targets), `what-is-rag-ai` (cross-cluster bridge — the retrieval mechanism behind AI answers), `ai-roi-uk-business-2026-what-the-evidence-actually-shows` (up-link to the Strategy & ROI pillar). Anchor text restates each destination's H1 or a clear synonym. No banned anchor text. This is the first article in the GEO pillar (topics 21-32, 73), so no sibling-cluster links exist yet; noted in `internal_link_suggestions.md` for future reciprocal linking.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; last checked per `output/_robots_status.txt` (site-wide config, not a per-article gate).

## Voice-guide spot-check (from `scripts/voice_check.py`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 0 ✓
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 7 (all are numbered/bulleted list-item leads in the two closing action lists, which the voice guide explicitly excludes from the "under 5" count as structural; script reports a WARN, not a FAIL) ✓
- H2s ending with ?: 8/8 ✓

**Automated result: CLEAN**

## Decision: SHIP

Rationale: all 10 elements pass (robots.txt is a site-level check, not blocking), the voice gate reports CLEAN on the first draft, the original UK stat is an honest, sourced Layer 2 derivation with workings shown and consistent with the stat bank's existing methodology, and sourcing was kept strictly to UK regulators/official statistics (Ofcom, BCC, ONS, gov.uk) plus the peer-reviewed Princeton/KDD paper that originated the term GEO, deliberately excluding SEO-tool-vendor blog statistics that could not be traced to a disclosed methodology.
