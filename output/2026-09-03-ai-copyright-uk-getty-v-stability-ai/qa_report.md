# QA report: What did the Getty v Stability AI ruling decide for UK copyright?

Topic ID: 39  |  Cluster: Risk, Governance & Legal  |  Priority: P1  |  Word count: ~1,900 (body, excluding JSON-LD)

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 70 words, sits above the first H2, answers the headline question standalone, cites the case citation, judgment date and the March 2026 report.
2. **Question-format H2s**: PASS — 5/5 H2s end with `?`, all mirror real query phrasings ("Getty Stability AI", "AI copyright UK").
3. **Comparison table**: PASS — one 4-row table contrasting the popular narrative against what the ruling and the law actually say, matching the Analysis format template.
4. **Authoritative inline citations**: PASS — 9 distinct primary-source URLs (judiciary.uk x1 reused, legislation.gov.uk x6, gov.uk x1), 10 inline citation instances total. All UK primary legal/government sources; no agency blogs cited.
5. **Original UK statistic**: PASS (Layer 2) — new Tom & Co calculation: the government's March 2026 statutory report was published 1 calendar day inside its own 9-month deadline under the Data (Use and Access) Act 2025 ss.135-136. Full workings in `stat_bank_update.json` (stat_024) and `sources.md`.
6. **JSON-LD schema**: PASS — Article, FAQPage (5 Q&A pairs plus the headline answer), and Person schemas included. No HowTo (format is Analysis, not step-by-step).
7. **Author byline + Person schema**: PASS — `author: "Tom McCaul"`, About-the-author section with credential and LinkedIn link, Person schema with `sameAs`.
8. **Visible date / dateModified**: PASS — `article.json` `date` set to 2026-09-03 (today), JSON-LD `datePublished`/`dateModified` match. No "Last reviewed" line in the body.
9. **2-4 internal links**: PASS — 4 links in "Related Tom & Co reading": pillar up-link (UK AI regulation field guide), sibling (EU AI Act), cross-cluster bridge (AI vendor contract), sibling vertical (UK law firms). No banned anchor text.
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; see `output/_robots_status.txt` for the last daily check.

## Voice-guide spot-check (from `scripts/voice_check.py`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 0 ✓
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 5 (all numbered-list item leads, structural) ✓
- H2s ending with ?: 5/5 ✓

**voice_check.py result: CLEAN**

## Research method note

Direct WebFetch/curl access to gov.uk, legislation.gov.uk, judiciary.uk, ico.org.uk and ons.gov.uk was blocked by this session's network egress policy. All facts were sourced via web search and corroborated across 2+ independent professional legal summaries before inclusion; every inline citation links to the primary source URL rather than a summary site. See `sources.md` for full detail. No statistic was invented; the honest-fallback rule in `stat-sourcing.md` was not needed as a strong Layer 2 datapoint was available.

## Decision: SHIP
Rationale: all 9 per-article checklist elements PASS, voice gate CLEAN, one iteration needed to fix two over-length paragraphs (now resolved).
