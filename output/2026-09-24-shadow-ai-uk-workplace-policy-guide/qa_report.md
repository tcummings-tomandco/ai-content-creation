# QA report: What is shadow AI and how should a UK employer manage it?

Topic ID: 70  |  Cluster: Workforce  |  Priority: P1  |  Word count: 1950 (target band 1800-2400)

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 70 words, sits above the first H2, answers the headline question standalone, contains a specific figure (£958m), a date (September 2026) and a named source (Deloitte UK).
2. **Question-format H2s**: PASS — 7/7 H2s end with `?`, each mirrors the roadmap's "shadow AI; employees using ChatGPT" query phrasings (e.g. "What is shadow AI and how common is it in the UK?", "What should a shadow AI policy actually include?").
3. **Comparison table**: PASS — one table (5 rows x 3 columns) contrasting a shadow AI usage policy against a full AI governance framework across scope, owner, review cycle, core output and typical first step. Every cell populated, no "TBC"/"varies".
4. **Authoritative inline citations**: PASS — 7 inline citations to primary/named-survey sources: Deloitte UK (x1, cited twice), Microsoft UK/Censuswide, British Chambers of Commerce/Atos (x2 pages), CIPD, ICO (x2 pages), ONS. All on the approved domain list or a named research firm with disclosed methodology (Deloitte, Microsoft/Censuswide). No agency blogs, no undated reports.
5. **Original UK statistic**: PASS — Layer 2. Tom & Co analysis combining Deloitte's shadow-AI usage rate (19.5% of UK workers) with ONS's UK employment total (34.48m, May-July 2026) to estimate 6.7 million UK workers use shadow AI. Full workings in `stat_bank_update.json`, appended to `data/stat_bank.json` as `stat_029`.
6. **JSON-LD schema**: PASS — Article, FAQPage (7 Q&A pairs matching the 7 H2s), and Person schema included. No HowTo (format is a policy template, not a numbered how-to walkthrough). All fields populated, no placeholder URLs.
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul". Body has an `<h3>About the author</h3>` section naming Tom McCaul, Founder, Tom & Co, 15+ years in digital commerce, with LinkedIn link. Person schema includes name, jobTitle, worksFor, sameAs.
8. **Visible date / dateModified**: PASS — `article.json` `date` set to 2026-09-24 (today). JSON-LD `datePublished` and `dateModified` both match. No "Last reviewed" line in the body.
9. **2-4 internal links**: PASS — 4 distinct inline body links to existing Tom & Co articles (DPIA template, ICO/UK GDPR guide, SME governance framework, workforce jobs-evidence article), each with descriptive anchor text restating the destination's H1/topic. At least one cross-cluster bridge (Risk, Governance & Legal: DPIA, ICO/GDPR, governance framework) and one same-cluster link (Workforce: jobs-evidence article), which also serves as the closest available up-link since the Workforce pillar hub isn't published yet (flagged in `internal_link_suggestions.md`).
10. **Robots.txt check**: SITE-LEVEL — not re-verified this run; last checked status carried forward from `output/_robots_status.txt` if present. Not a per-article blocker per `checklist.md`.

## Voice-guide spot-check

(from `scripts/voice_check.py`, run against `article.json`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 0 ✓
- "We"/"our" frequency: 0.10% ✓ (well under the 1% threshold)
- Bolded phrases: 10 WARN — all are numbered-list item leads (two `<ol>` blocks: the five-element policy list and the "this quarter" action list, one bold phrase per item), which `voice-guide.md` classes as structural and excludes from the marketing-emphasis count. No inline marketing-style bolding was used. Same pattern as the precedent set in `will-ai-take-my-job-uk-workforce-evidence-2026` (6 bolded phrases, same WARN, same justification).
- H2s ending with `?`: 7/7 ✓

**voice_check.py result: CLEAN (0 failures)**

## Research method note

Direct page fetch (WebFetch) was blocked by this session's network egress policy for every domain tested, including gov.uk, ons.gov.uk, ico.org.uk, britishchambers.org.uk, and even non-UK-government domains such as arxiv.org. All research was conducted via WebSearch, which returns synthesised summaries with source URLs; every citation in the article links to the primary source itself, not a secondary write-up. See `sources.md` for the full note and per-source detail. A human reviewer should ideally spot-check the live pages before publish.

## Roadmap title vs. researched figures

The roadmap topic title referenced "78-86% of staff using unauthorised AI." That range traces to global (non-UK) vendor surveys (Microsoft/LinkedIn Work Trend Index, PagerDuty/Wakefield Research, Freshworks), not to a UK-primary source, so it was not used. The honest UK-specific figures found in research are lower and more defensible: 31% of UK GenAI users (Deloitte, UK n=25,000) and 71% of UK employees having used an unapproved tool at least once (Microsoft/Censuswide, UK n=2,003). The article and its title were built around these UK-sourced figures instead of the unsourced roadmap placeholder.

## Decision: SHIP

Rationale: all 9 applicable checklist elements PASS (robots.txt is site-level and not per-article), voice gate is CLEAN, word count and citation count are within target bands, and the original UK statistic is an honest, fully-worked Layer 2 calculation rather than an invented number.
