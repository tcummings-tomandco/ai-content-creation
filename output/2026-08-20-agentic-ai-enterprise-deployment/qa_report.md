# QA report: What is agentic AI and how do enterprises deploy it?

Topic ID: 12 | Cluster: Operations & Efficiency | Priority: P1 | Word count: 1847

## 10-element GEO checklist

1. **Definitive answer paragraph:** PASS — 72 words, sits above the first H2, answers the headline question standalone. Contains specific figures (7% agentic adoption among AI-using firms, ~3% of 250+ staff firms) and a named source (DSIT).
2. **Question-format H2s:** PASS — 6/6 H2s end with `?` (verified by `voice_check.py`). Within the 4-7 band for a 1800-2400 word article.
3. **Comparison table:** PASS — one `<table>` with `<thead>`/`<tbody>`, 5 rows (the five named examples) x 4 columns (sector, enterprise/programme, what the agent does, deployment stage). Every cell populated, no "TBC"/"varies".
4. **Authoritative inline citations:** PASS, with judgement calls flagged — 10 inline external citations: ons.gov.uk, gov.uk (x2), bankofengland.co.uk, ico.org.uk are on the checklist's literal domain list. Four are judgement calls, same convention as prior articles' `bankunderground.co.uk` flag: `newsroom.bt.com` and `lloydsbankinggroup.com` (each company's own primary statement about its own deployment), `england.nhs.uk` (NHS England's official subdomain, not the literal `nhs.uk` string), and `thegrocer.co.uk` (established UK grocery trade press, comparable in kind to `computerweekly.com`/`marketingweek.com` on the approved list but not itself named). No agency blogs, content farms or undated reports used. Full detail in `sources.md`.
5. **Original UK statistic:** PASS — Layer 2, two calculations. New this run: Tom & Co scaling of NHS England's 43-minutes-a-day Copilot saving to the 500,000-staff rollout target, roughly 79 million hours a year (full workings in `stat_bank_update.json`, appended to `data/stat_bank.json` as `stat_020`). Also reuses the existing `stat_005` (ONS x DSIT, ~3% of UK enterprises running agentic AI) already in the bank from an earlier article.
6. **JSON-LD schema:** PASS — Article, FAQPage (7 Q&A pairs: the headline question plus all 6 H2s), and Person schema included. No HowTo (format is "Definition + 5 examples", not step-by-step). Verified to parse as valid JSON.
7. **Author byline + Person schema:** PASS — `author: "Tom McCaul"` (string) in article.json; `<h3>About the author</h3>` section with role and 15-years credential; Person schema with `jobTitle`, `worksFor`, `sameAs` LinkedIn.
8. **Visible date / dateModified:** PASS — `date: "2026-08-20"` in article.json; JSON-LD `datePublished`/`dateModified` both `2026-08-20`. No "Last reviewed" line in the body.
9. **2-4 internal links:** PASS — 4 links in the "Related Tom & Co reading" footer (what-is-agentic-ai, agentic-ai-use-cases-mid-market, ai-agents-vs-rpa-vs-traditional-automation, risks-of-agentic-ai), plus 2 of the same links also placed inline earlier in the body where each is first referenced. Anchor text restates each destination's H1. No banned anchor text.
10. **Robots.txt check:** SITE-LEVEL — not re-verified this run; no `scripts/check_robots.py` present in this checkout and no `output/_robots_status.txt` exists yet. Flagging for Tom rather than assuming pass, consistent with the last article's flag.

## Note on overlap with the existing "what-is-agentic-ai" article

`output/2026-07-01-what-is-agentic-ai/` already covers "What is agentic AI and how does it work?", a near-identical headline question to this roadmap topic. This is a genuine gap in how topic 12 was scoped against content already produced outside the tracked roadmap rows (that earlier batch of ten vocabulary articles from 2026-07-01 has no corresponding roadmap IDs). To avoid duplicate content, this article keeps its own definition to two short paragraphs, links out to the existing piece for the full mechanics, and spends the bulk of the word count on five sourced 2026 enterprise deployments (Lloyds, GOV.UK, NHS England, Ocado, BT) that appear nowhere else in the published corpus. Flagged in `internal_link_suggestions.md` as well. Recommend Tom spot-check for cannibalisation once both are live, and consider back-filling roadmap IDs for the 2026-07-01 batch so future picker runs can see them.

## Voice-guide spot-check

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words: 6 (the 72-word answer paragraph, exempt per voice-guide, plus 5 body paragraphs of 76-83 words, roughly one per major H2 section) — within the "one longer paragraph per major section" allowance, not a fail.
- "We"/"our" frequency: 0.00%
- Bolded phrases: 5 (all numbered-list item leads, structural)
- H2s ending with ?: 6/6 ✓

`scripts/voice_check.py` result: **CLEAN** (0 failures).

## Decision: SHIP

Rationale: all 9 per-article checklist elements pass (element 5 with two Layer 2 stats, one new); element 10 is a site-level flag, not a per-article blocker. Voice gate is CLEAN. The overlap with the existing what-is-agentic-ai article is a real scoping gap, addressed by differentiation rather than duplication, and flagged above for Tom's awareness.
