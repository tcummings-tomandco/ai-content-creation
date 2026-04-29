# The 10-element GEO QA gate

Every article must pass all ten before the approval email is drafted. Failure on any item means iterate, not ship. The QA report (`output/{folder}/qa_report.md`) records PASS / FAIL / N/A with evidence for each.

The list below is the operational version of the playbook's Section 3. Always cross-check against the xlsx `Article Checklist` sheet — if it diverges, the xlsx wins.

## 1. Definitive answer paragraph (40–80 words, top of article)

**Pass criteria:**
- Word count between 40 and 80 inclusive.
- Answers the headline question on its own. A reader who reads only this paragraph and nothing else gets a correct, specific answer.
- Contains at least one specific number, date, regulator, or named UK scheme — not a hedge.
- Sits above the first H2.

**How to test:** copy the paragraph in isolation. Does it answer the headline H1 without context? If not, rewrite.

## 2. Question-format H2s

**Pass criteria:**
- Every H2 ends with a question mark.
- Each H2 mirrors a real user prompt (use the topic row's `Likely query phrasings` as the seed).
- 4–7 H2s in a 1500–2200 word article. Pillars can have 8–12.

**How to test:** `grep -c '## .*?$'` on the markdown source equals the H2 count.

## 3. At least one comparison table

**Pass criteria:**
- One table minimum. Rendered as proper HTML `<table>` with `<thead>` and `<tbody>`, not as text.
- Required for any "vs", "best", "alternative", "compared", "choose between" topic. Recommended otherwise.
- Columns name the things being compared; rows are the dimensions. Sterling pricing where relevant. Date stamps where relevant.
- Every cell has data, no "TBC" or "varies".

## 4. Inline citations to authoritative sources

**Pass criteria:**
- 5–10 inline citations in a 1500–2200 word article.
- Every citation links to a primary UK authority source, peer-reviewed research, or named industry survey with methodology.
- Approved domain pattern includes: gov.uk, ico.org.uk, fca.org.uk, mhra.gov.uk, ofcom.org.uk, sra.org.uk, bankofengland.co.uk, ons.gov.uk, parliament.uk, lordslibrary.parliament.uk, nice.org.uk, nhs.uk, britishchambers.org.uk, techuk.org, lawsociety.org.uk, ft.com, thetimes.co.uk, theguardian.com, bbc.co.uk, computerweekly.com, marketingweek.com, plus academic publishers (arxiv, springer, nature) and named research firms with disclosed methodology (Bain, McKinsey, Deloitte, IBM, MIT IDE, BCG, Profound, SemRush, Ahrefs, ConvertMate).
- Banned: other agency blogs, content farms, undated industry "reports", AI-generated summary sites, Wikipedia as a primary source.

**How to test:** every `<a href>` in the article body resolves to a domain on the approved list. Cite-counter script checks each.

## 5. One original UK statistic, benchmark, or proprietary insight

**Pass criteria:** at least one of the following is true:
- An entry from `data/stat_bank.json` is cited in the body with attribution to "Tom & Co analysis" or "Tom & Co survey".
- A new original calculation is performed, shown with workings in a methodology note, and appended to `stat_bank.json`. (Layer 2 in `stat-sourcing.md`.)
- A Tom & Co client outcome (anonymised) is cited with consent.

**How to test:** the `qa_report.md` records which layer (1, 2, or 3) the article relies on. Layer 1 alone is acceptable in the first 10 articles; from article 11 onwards, at least 60% of articles should carry a Layer 2 or Layer 3 datapoint.

If no honest stat is available, **flag in the email** and ship the article without element 5 marked PASS. Do not invent a number.

## 6. JSON-LD schema block

**Pass criteria:**
- A single `<script type="application/ld+json">` block at the end of the `content` HTML.
- Contains an array with: `Article` schema (always), `FAQPage` schema (if 3+ Q&A pairs), `HowTo` schema (if step-by-step format), `Person` schema for the author with `sameAs` LinkedIn URL.
- All required schema fields populated. No empty strings, no placeholder URLs.
- Validates against schema.org. (The QA script runs `python3 scripts/validate_jsonld.py`.)

## 7. Author byline with credentials and Person schema

**Pass criteria:**
- `author` field in `article.json` names a real human, not "Tom&Co Team", for AI authority articles.
- The article body contains an "About the author" line at the bottom with the author's role and one credential (years in industry, certification, prior role).
- Person schema in the JSON-LD block includes `name`, `jobTitle`, `worksFor: Tom & Co`, `sameAs: [LinkedIn URL]`.

**Open question for Tom:** which named human bylines this content? Until confirmed, the engine drafts with `author: "Tom Cummings"` placeholder and flags it in the email.

## 8. Visible "Last reviewed" date

**Pass criteria:**
- The article body contains a visible line near the top (immediately under the H1 or just below the answer paragraph) reading: `Last reviewed: {YYYY-MM-DD}`.
- The `dateModified` field in the Article JSON-LD matches.
- The roadmap row's `Notes` records the next review-due date (today + 90 days for supporting articles, today + 60 days for pillars).

## 9. 2–4 internal links with descriptive anchor text

**Pass criteria:**
- 2 to 4 inline `<a href>` links to existing Tom & Co articles. URLs follow `/blog/{category-slug}/{article-slug}` pattern.
- Anchor text restates the destination's H1 or a synonym. **Banned:** "click here", "read more", "this article", "learn more", "find out more".
- At least one link is up to the topic's pillar hub. At least one link is across to a sibling article in an adjacent cluster.
- The `internal_link_suggestions.md` output file lists the chosen links plus 2–3 alternates the website-side prebuild link injector can use.

**How to test:** every internal link's anchor text contains a noun phrase that appears in the destination's H1. Cite-counter flags any link with banned anchor text.

## 10. AI crawlers permitted in robots.txt

**Pass criteria:**
- This is a one-time site-level check, not a per-article check. The QA report flags it once per batch.
- Verify `https://www.tomandco.co.uk/robots.txt` allows GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended.
- If any are missing or disallowed, raise a separate flag for Tom — this is a site-wide config issue, not a per-article fix.

**How to test:** `python3 scripts/check_robots.py` runs once per day and writes status to `output/_robots_status.txt`. Articles do not block on this check; the engine just reports.

## Voice-guide spot-check (runs alongside the 10 elements)

These are mechanical and non-negotiable. Any failure forces a redraft.

- ` — ` (em dash) count in content: must be 0.
- ` – ` (en dash, used as sentence break) count: must be 0. Hyphens in numerical ranges (e.g. "40–80 words") are allowed.
- Banned-word scan against `voice-guide.md` Section "Banned words and phrases": must be 0 hits.
- Paragraphs over 100 words: must be 0.
- "We"/"Our" frequency in body text: under 1% of word count.
- Bolded phrases: under 5 in body.
- Every H2 ends with `?`.

The QA script in `scripts/voice_check.py` automates this scan and emits a section in `qa_report.md`. The skill must run it before drafting the email.

## QA report template

```markdown
# QA report: {title}

Topic ID: {n}  |  Cluster: {cluster}  |  Priority: {p}  |  Word count: {w}

## 10-element GEO checklist
1. Definitive answer paragraph: PASS/FAIL/N/A — [evidence]
2. Question-format H2s: PASS/FAIL/N/A — [count, examples]
3. Comparison table: PASS/FAIL/N/A — [present? rows × cols]
4. Authoritative inline citations: PASS/FAIL/N/A — [count, domains]
5. Original UK stat: PASS/FAIL/N/A — [Layer 1/2/3, source]
6. JSON-LD schema: PASS/FAIL/N/A — [schemas included]
7. Author byline + Person schema: PASS/FAIL/N/A — [author, LinkedIn]
8. Last reviewed date: PASS/FAIL/N/A — [stamp present, dateModified matches]
9. 2-4 internal links: PASS/FAIL/N/A — [links chosen, anchors]
10. Robots.txt check: PASS/FAIL/SITE-LEVEL — [last verified]

## Voice-guide spot-check
- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: [list or "none"]
- Paragraphs over 100 words: 0
- "We"/"our" frequency: x.x%
- Bolded phrases: n
- H2s ending with ?: n/n ✓

## Decision: SHIP / ITERATE
Rationale: [one line]
```
