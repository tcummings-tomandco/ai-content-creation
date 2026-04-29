---
name: tomandco-article
description: Research, draft, and QA a UK-anchored authority article for tomandco.co.uk that wins LLM citations (GEO). Use when the user asks for the next article, names a topic from the roadmap, or invokes the daily/twice-weekly routine. Produces an article.json matching the website schema, an HTML preview, a sources file, and a QA report — all under output/YYYY-MM-DD-slug/.
---

# Tom & Co article skill

This skill turns a row from `data/roadmap.json` into a publish-ready article that meets the 10-element GEO checklist. Output goes to `output/{YYYY-MM-DD}-{slug}/` and is sent to Tom for approval. Nothing pushes to the live website without his sign-off.

## Inputs

The skill picks up a topic in one of three ways:

1. **Named topic**: user says "write topic 34" or "write the EU AI Act decision tree" — match by ID or fuzzy title.
2. **Next-in-queue** (default for the routine): run `python3 scripts/pick_next_topic.py` which prints the next P0/P1 row from `data/roadmap.json` with empty Status. The script's tiebreaker order: P0 → P1 quick-wins (Quick win=Y) → P1 by ID → P2 → P3.
3. **Refresh mode**: user says "refresh topic N" — pulls the existing article, runs research again, regenerates with current stats. Used at 90-day cycle.

## Read these supporting files before drafting

- `voice-guide.md` — Tom & Co voice rules and the explicit list of AI tells to avoid. Read every run.
- `checklist.md` — the 10-element GEO checklist. The QA gate. Block "approve email" until every box is ticked.
- `stat-sourcing.md` — the 3-layer strategy for getting an original UK stat into every piece.
- `format-mapping.md` — which article structure to use for which cluster (decision tree, comparison table, definition + benchmark, etc).

## Run order (do not reorder)

### 1. Load context

- Read the picked roadmap row and surface: ID, Topic, Cluster, Pillar, Priority, Audience, Format, Likely query phrasings, UK angle, Suggested length, Quick win flag.
- Load `data/stat_bank.json` (create as empty `{"stats": []}` if missing). Note any existing Tom & Co calculations that fit the topic.
- Load the 6 voice samples in `data/voice_samples/` and skim them. The voice guide compresses them into rules but you should re-read the source occasionally so the rules don't drift.

### 2. Research

Goal: 5–10 specific, citable, UK-primary-source datapoints. Plus 1 original calculation candidate.

- Start with the topic row's `Likely query phrasings` and `UK angle`.
- Search authoritative UK sources first — `data/roadmap.json` → `authoritative_sources` is the seed list (gov.uk, ICO, FCA, Bank of England, Ofcom, ONS, Innovate UK, BCC, Made Smarter, professional bodies, peer-reviewed). Use WebSearch + WebFetch.
- Avoid agency blogs, listicles from SEO content farms, and undated industry "reports" with no methodology.
- For each datapoint capture: claim, exact figure with units, date of measurement, source title, source URL. If you can't pin all five, drop the datapoint.
- Identify one **original-calculation opportunity**: a public dataset where a derivation, sterling conversion, sector cut, or year-on-year delta gives a number the source didn't publish. See `stat-sourcing.md` Layer 2.
- Note 2–4 candidate internal links to existing Tom & Co articles in adjacent clusters (cross-cluster bridges) and one up-link to the topic's pillar.

### 3. Plan the structure

Use `format-mapping.md` to pick the structural template for the topic's Cluster + Format combination. Sketch:

- The headline question (≤70 chars, mirrors the strongest query phrasing)
- The 40–80 word answer paragraph (this is the part LLMs will lift verbatim — write it like a definition, not a teaser)
- 4–7 question-format H2s mirroring real prompts
- Where the comparison table goes (required for vs/best/alternative; recommended otherwise)
- Where the original UK stat lives, prominently in the body
- The internal link placements (2–4)
- The "Last reviewed" stamp position

### 4. Draft

Word counts by topic length band (from the roadmap row's `Suggested length`):
- 1500–2200: ~1800 target
- 2000–3000: ~2400 target
- Pillars: 3000–5000

Hard rules from `voice-guide.md`:
- No em dashes. None. Use commas, parentheses, full stops, or rewrite.
- No banned AI-tell words (see voice guide).
- British spellings.
- Short paragraphs (1–4 sentences). No walls of text.
- Inline citations as `[source name](url)` markdown that converts to `<a>` in HTML output.
- Specific numbers with units and dates everywhere claims are made.
- One concrete UK example or scenario per major section.

### 5. Build the JSON-LD block

Generate a single `<script type="application/ld+json">` block containing an array with:
- `Article` schema (headline, datePublished, dateModified, author with credentials, publisher Tom & Co)
- `FAQPage` schema if the article has 3+ Q&A pairs
- `HowTo` schema if the format is "5-step framework" or "how-to"
- Author `Person` schema with sameAs LinkedIn URL

Embed at the end of the article `content` HTML. (Phase 2: when the website renderer is updated, this moves to the page header. Until then it's inline.)

### 6. Self-review against the 10-element checklist

Run every item in `checklist.md`. For each, mark PASS / FAIL / N/A. Any FAIL means iterate, don't ship.

Specifically watch for:
- Element 1: answer paragraph is 40–80 words and answers the headline question on its own with no surrounding context required
- Element 2: every H2 is in question form
- Element 4: every cited source is primary (gov.uk, regulator, peer-reviewed, named survey) — not another agency blog
- Element 5: at least one stat is from `stat_bank.json` or marked as a fresh original-calculation that gets appended to the bank
- Voice guide rules: scan for em dashes and banned words

### 7. Write outputs

To `output/{YYYY-MM-DD}-{slug}/`:

- `article.json` — exact match to the website schema (id, slug, title, excerpt, content, image, date, readTime, categories ["AI"], author, featured: false, metadata{title, description, keywords, openGraph, twitter})
- `preview.html` — standalone HTML doc wrapping the article content with basic CSS, so Tom can open it in a browser and read it like a published page
- `sources.md` — every cited source with title, URL, accessed date, and the specific claim it supports
- `qa_report.md` — the 10-element scoresheet plus voice-guide spot-check (em-dash count, banned-word count, paragraph length distribution)
- `internal_link_suggestions.md` — 2–4 anchor texts and target Tom & Co URLs for the website-side `prebuild` link injector to consume (or for manual placement)
- `stat_bank_update.json` — any new original calculation to merge back into `data/stat_bank.json`

### 8. Email Tom for approval

Use the gmail MCP `create_draft` tool. Subject: `[Tom&Co AI engine] Article ready: {title}`. Body includes:
- Topic, cluster, priority, target word count vs actual
- The 40–80 word answer paragraph (so he can judge in 30 seconds)
- The 10-element QA scoresheet
- Stat layer used (1 sourced, 2 original, 3 survey)
- Link to `output/{folder}/preview.html` (file:// URL)
- One-line "Reply APPROVE to mark for publish, or REVISE: [your notes]"

Create as a **draft**, not send. Tom reviews and sends himself, or copies to a publish step.

### 9. Update the queue

After Tom approves (in a later turn), update `data/roadmap.json` for that topic ID:
- `Status`: "Approved — awaiting publish"
- `Target publish date`: today
- `Notes`: link to the output folder

The xlsx is the source of truth — flag at the end of each batch that the xlsx needs syncing (the engine doesn't write xlsx directly to keep the file unlocked for Tom's editing).

## What this skill does not do

- Does not push to the website repo. Phase 1 only writes to local `output/`. Phase 2 will add a PR step against `tomandco-tmccaul/tomandco_website`.
- Does not invent statistics. If element 5 cannot be filled honestly, raise it to Tom with a flag in the email — do not fabricate a number.
- Does not skip the QA gate to "save time." Every element 1–10 must pass.
- Does not generate hero images. Image path in `article.json` is a placeholder (`/images/blog/ai/{slug}.png`) plus a note in the email asking Tom to add the asset.
