# Tom & Co AI Content Engine

An automated workflow that researches, drafts, and QA-checks UK-anchored authority articles for [tomandco.co.uk](https://www.tomandco.co.uk), optimised to win citations on ChatGPT, Claude, Perplexity, Gemini, and Google AI Overviews (GEO).

## How it works

1. The engine reads the next topic from `data/roadmap.json` (sourced from `Tom&Co_AI_Content_Roadmap.xlsx`).
2. The `tomandco-article` Claude skill researches the topic against UK primary sources, drafts the article, generates JSON-LD schema, and runs the 10-element GEO QA gate.
3. Output lands in `output/{YYYY-MM-DD}-{slug}/` as a website-ready JSON blob, an HTML preview, a sources file, and a QA report.
4. The engine drafts an approval email to Tom via the gmail MCP. Tom reviews the preview, approves, and the article is queued for publishing to the website.

**Phase 1** (now): articles are written to `output/`. Tom approves and manually adds them to the website repo.

**Phase 2** (after company approval): the engine opens a PR against `tomandco-tmccaul/tomandco_website` adding the article to `src/data/articles.json`. Tom reviews the diff and merges.

## Layout

```
.claude/skills/tomandco-article/
  SKILL.md              # entry point — Claude reads this first
  voice-guide.md        # Tom & Co voice + the explicit no-AI-tells rules
  checklist.md          # the 10-element GEO QA gate
  stat-sourcing.md      # 3-layer strategy for original UK stats
  format-mapping.md     # cluster → article structure mapping

data/
  roadmap.json          # 75-topic queue (regenerate from xlsx with scripts/refresh_roadmap.py)
  stat_bank.json        # Tom & Co original calculations and proprietary stats
  voice_samples/        # 4 representative Tom & Co articles for voice reference

scripts/
  pick_next_topic.py    # queue picker (priority-aware)
  voice_check.py        # mechanical voice-guide compliance scan
  refresh_roadmap.py    # re-export the xlsx to roadmap.json (TODO)

routines/
  run.md                # the routine prompt — paste into a fresh Claude Code session

output/                 # generated articles land here (gitignored)
```

## Running it

Manual run (Phase 1 default):

```bash
# In Claude Code, from the repo root:
# 1. Open a fresh session in this directory.
# 2. Paste the contents of routines/run.md as your prompt.
# 3. Claude reads the skill, picks the next topic, runs end-to-end.
```

Or specify a topic:

```
[paste routines/run.md, then add:]
Optional override: pick topic 34.
```

Test the queue:

```bash
python3 scripts/pick_next_topic.py --list 8        # see the next 8 topics in priority order
python3 scripts/pick_next_topic.py --id 34         # show row 34
```

Test voice compliance on any draft:

```bash
python3 scripts/voice_check.py output/2026-04-29-uk-ai-regulation-map/article.json
```

## The 10-element GEO checklist

Every article must ship with all ten before approval. From the editorial playbook:

1. 40–80 word definitive answer paragraph at the top
2. Question-format H2s mirroring real prompts
3. At least one comparison table
4. Inline citations to authoritative UK sources (gov.uk, ICO, FCA, ONS, peer-reviewed)
5. One original UK statistic, benchmark, or proprietary insight
6. JSON-LD schema (Article, FAQPage, HowTo, Organization, Person)
7. Author byline with credentials and Person schema linked to LinkedIn
8. Visible "Last reviewed" date with 90-day refresh cycle
9. 2–4 internal links with descriptive anchor text
10. AI crawlers permitted in robots.txt (site-level check)

See `.claude/skills/tomandco-article/checklist.md` for the operational version with PASS/FAIL criteria and evidence requirements.

## Voice rules

Two jobs at once: sound like Tom & Co, and not sound like AI. The QA gate enforces this mechanically.

Hard rules (the QA scan fails the article on any of these):

- No em dashes. Ever.
- No AI-tell words ("delve", "leverage", "harness", "robust", "comprehensive", "seamless", and ~30 others — see `voice-guide.md`).
- No paragraphs over 100 words.
- Every H2 ends with a question mark.
- British spellings throughout.

Voice rules (warnings, not auto-fails):

- "We"/"Our" frequency under 1% of body word count.
- Under 5 bolded phrases in the body.
- No symmetric paragraph openings.
- No closing summary paragraphs.

## Decisions logged

- **Approval mode**: draft-with-approval, not auto-publish. Engine drafts an email; Tom reviews `preview.html` and sends it manually or replies APPROVE.
- **Notification channel**: gmail (not Slack — reserved for non-engine work).
- **Cadence**: 2 supporting articles per week, plus 1 newsroom slot per fortnight, plus 90-day refresh sweeps. Not daily.
- **Categories**: new "AI" category on the website (existing categories are Strategy, Design, Awards, News, Adobe Commerce updates, Headless, Partners, Podcasts & Webinars).
- **Author byline**: open question — "Tom Cummings" placeholder until confirmed. Person schema requires a LinkedIn URL.
- **CMS**: Next.js 16, articles stored in `src/data/articles.json` in the website repo. No headless CMS.
- **Schema injection**: Phase 1 embeds JSON-LD inline in `content`. Phase 2 ideally adds article-level schema injection to the website renderer.

## Source of truth for the roadmap

`Tom&Co_AI_Content_Roadmap.xlsx` (in the sibling SEO folder) is the canonical queue. `data/roadmap.json` is a working copy regenerated from the xlsx. Tom edits the xlsx; the engine reads the JSON. Status updates after each run are flagged for Tom to apply back to the xlsx.
