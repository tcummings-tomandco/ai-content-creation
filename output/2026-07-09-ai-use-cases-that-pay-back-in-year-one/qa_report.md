# QA report: Which AI use cases pay back within a year for a UK business?

Topic ID: 3  |  Cluster: Strategy & ROI  |  Pillar: P1: AI strategy  |  Priority: P1  |  Quick win: Y
Word count: 1,509 (target band: 1500-2000) ✓
Drafted: 2026-07-09
Author: Tom McCaul, Founder, Tom & Co

## 10-element GEO checklist

1. **Definitive answer paragraph (40-80 words):** PASS — 79 words. Names all four use cases, cites the 60-hours/month Made Smarter figure and McKinsey's 10-20% cost-reduction figure by name. Answers the headline question standalone.
2. **Question-format H2s:** PASS — 5/5 H2s end with `?`. Within the 4-7 range for this length band. The four use-case names are promoted to H3 (Invoice and back-office processing; Predictive maintenance and stock control; Software engineering and IT support; First-draft content and marketing copy), per voice-guide.md's "3+ named sub-topics" rule, and do not count toward the H2 total, matching the pattern used in the format-mapping.md "Listicle + ROI" template.
3. **At least one comparison table:** PASS — 4-row x 4-column table comparing all four use cases on UK evidence, typical time to a result, and complexity to start. Every cell has real data, including an honest "High" complexity / "6 to 12 months" rating for predictive maintenance rather than overselling it.
4. **Inline citations to authoritative sources:** PASS — 6 inline external citations: Made Smarter (Nordell case study), Made Smarter Innovation (DSPSC case study), ONS ASHE 2025, McKinsey State of AI, DSIT AI Adoption Research (gov.uk), British Chambers of Commerce/University of Essex. All primary UK government, regulator/statistics-body, or named-research-firm domains. Made Smarter is not in checklist.md's illustrative domain list but is explicitly named as a preferred Layer 1 source in stat-sourcing.md (a DBT/Innovate UK-backed manufacturing adoption programme, gov.uk-equivalent); treated as primary on that basis. No agency blogs or content-farm sources used, despite several early searches surfacing them.
5. **One original UK statistic:** PASS — Layer 2, new calculation. `stat_009`: Nordell's reported 60 hours/month AI invoice-processing saving, converted to a loaded sterling value (~£12,200/year) using ONS ASHE 2025 median admin/secretarial pay plus employer NI and pension on-costs. Full workings in `stat_bank_update.json` in this folder, one-line attribution in a blockquote in the body. `stat_008` (McKinsey-derived £4,500-£9,000/employee/year) is also reused from the existing bank for the software engineering use case.
6. **JSON-LD schema:** PASS — Article + FAQPage (5 Q&A pairs, one per H2) + Person (Tom McCaul, LinkedIn `sameAs`) + publisher Organization. No HowTo schema, correctly omitted as this is a listicle format, not a step-by-step how-to. Validated as parseable JSON via `json.loads`.
7. **Author byline + Person schema:** PASS — `author: "Tom McCaul"` (string). Person schema includes name, jobTitle (Founder), worksFor (Tom & Co), sameAs `https://www.linkedin.com/in/tom-mccaul-77b2778/`. "About the author" H3 present in body.
8. **Visible date / dateModified:** PASS — `article.json` `date` = 2026-07-09 (today). Article JSON-LD `datePublished` and `dateModified` both 2026-07-09. No "Last reviewed" line in the body.
9. **2-4 internal links with descriptive anchor text:** PASS — 3 internal links (each placed once inline and once in "Related Tom & Co reading"): ai-roi-uk-business-2026-what-the-evidence-actually-shows (same-pillar sibling), how-to-build-an-ai-strategy-for-a-uk-sme (same-pillar sibling), chatgpt-vs-claude-vs-gemini-for-business (cross-cluster, Technical & Build). No up-link to the AI-strategy pillar hub is possible yet, as it has not been written (this article is itself one of that pillar's three supporting pieces); flagged in `internal_link_suggestions.md`, matching the same flag raised for topics #1 and #2.
10. **AI crawlers permitted in robots.txt:** SITE-LEVEL — not re-checked this run; no `output/_robots_status.txt` currently exists in the repo, so this remains outstanding at the site level, not specific to this article.

## Voice-guide spot-check

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- Paragraphs 71-100 words: 1 (the 79-word answer paragraph, which the voice guide explicitly permits at the top of the article)
- "We"/"our" frequency: 0.13%
- Bolded phrases: 0
- H2s ending with ?: 5/5 ✓

`python3 scripts/voice_check.py` result: **CLEAN** on first pass, no iteration needed.

## Decision: SHIP

Rationale: all 10 checklist elements pass or are correctly marked site-level, the voice gate is CLEAN on the first run, the comparison table gives an honest complexity/timeline rating rather than overselling the manufacturing use case, and element 5 is satisfied by a fresh, transparent Layer 2 calculation with full workings rather than an invented number.

## Note on research

Initial web searches for UK AI ROI/payback stats returned mostly US-centric content-farm blogs (customer-service ROI multiples, generic "AI statistics 2026" roundups) with no verifiable primary source; these were discarded per stat-sourcing.md's "what never qualifies" list. All figures used in the final draft trace to a named UK government-backed programme (Made Smarter/Innovate UK), a UK statistics body (ONS), a named research firm with disclosed methodology (McKinsey), or a UK government department survey (DSIT).
