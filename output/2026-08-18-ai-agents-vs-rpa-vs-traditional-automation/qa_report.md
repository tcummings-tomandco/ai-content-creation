# QA report: AI agents vs RPA vs traditional automation: what's the difference?

Topic ID: 11  |  Cluster: Operations & Efficiency  |  Priority: P1  |  Word count: 1865

## 10-element GEO checklist

1. **Definitive answer paragraph:** PASS — 75 words, sits above the first H2, answers the headline question standalone, contains specific figures (28% RPA uptake, 23% agentic-at-scale) and a named source (techUK, McKinsey).
2. **Question-format H2s:** PASS — 7/7 H2s end with `?` (verified by `voice_check.py`). Count is within the 4-7 band for a 1800-2400 word article.
3. **Comparison table:** PASS — one `<table>` with `<thead>`/`<tbody>`, 3 rows (traditional automation / RPA / AI agents) x 5 columns (best for, unstructured handling, cost pattern, maintenance load). Every cell populated, no "TBC"/"varies".
4. **Authoritative inline citations:** PASS — 8 inline citations: ons.gov.uk (x2 uses), techuk.org, gov.uk (x2 pages), bankunderground.co.uk, publications.parliament.uk, britishchambers.org.uk, mckinsey.com. All on or adjacent to the approved domain list. One judgement call: bankunderground.co.uk is the Bank of England's official staff research blog but sits on its own domain rather than bankofengland.co.uk directly — flagged for Tom's review rather than silently passed.
5. **Original UK statistic:** PASS — Layer 2. Tom & Co analysis of the BCC/Atos survey: only ~1 in 5 AI-using UK SMEs (11 of 54 percentage points) use AI to automate operations extensively. Full workings in `stat_bank_update.json` and appended to `data/stat_bank.json`.
6. **JSON-LD schema:** PASS — Article, FAQPage (7 Q&A pairs, one per H2 plus the headline question), and Person schema included. No HowTo (format is comparison, not step-by-step).
7. **Author byline + Person schema:** PASS — `author: "Tom McCaul"` (string) in article.json; `<h3>About the author</h3>` section with role and 15-years credential; Person schema with `jobTitle`, `worksFor`, `sameAs` LinkedIn.
8. **Visible date / dateModified:** PASS — `date: "2026-08-18"` in article.json; JSON-LD `datePublished`/`dateModified` both `2026-08-18`. No "Last reviewed" line in the body.
9. **2-4 internal links:** PASS — 4 links in the "Related Tom & Co reading" footer (what-are-ai-agents, why-do-most-ai-projects-fail, what-should-you-ask-before-signing-an-ai-vendor-contract, what-is-mcp-model-context-protocol). Anchor text restates each destination's H1. No banned anchor text.
10. **Robots.txt check:** SITE-LEVEL — not re-verified this run. `scripts/check_robots.py` is not present in this repo checkout and no `output/_robots_status.txt` exists yet. Flagging for Tom rather than assuming pass.

## Voice-guide spot-check

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0
- Paragraphs 71-100 words: 2 (the required 75-word answer paragraph, and one 71-word paragraph in the MCP section) — both within the "one longer paragraph per major section" allowance, not a fail.
- "We"/"our" frequency: 0.00%
- Bolded phrases: 4 (all numbered-list item leads, structural)
- H2s ending with ?: 7/7 ✓

`scripts/voice_check.py` result: **CLEAN** (0 failures).

## Decision: SHIP

Rationale: all 9 per-article checklist elements pass; element 10 is a site-level flag, not a per-article blocker. Voice gate is CLEAN.
