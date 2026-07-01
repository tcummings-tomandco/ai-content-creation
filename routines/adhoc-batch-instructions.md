# Ad-hoc batch instructions (one article per subagent)

These instructions are for producing a single article from an explicitly-supplied topic (NOT from the roadmap). Each subagent handles exactly one topic and writes it to disk. A central process pushes to Storyblok afterwards — subagents must NOT touch git or Storyblok.

## Working directory

`cd "/Users/tomcummings/Desktop/T&Co/ai-content-creation"`

## Read first

- `.claude/skills/tomandco-article/SKILL.md`
- `.claude/skills/tomandco-article/voice-guide.md`
- `.claude/skills/tomandco-article/checklist.md`
- `.claude/skills/tomandco-article/stat-sourcing.md`
- `.claude/skills/tomandco-article/format-mapping.md`

Follow them exactly. The rules below are the ad-hoc-specific overrides.

## The article

Your topic, target keyword, and slug are given in your task prompt. Date for all articles in this batch: **2026-07-01**.

## Rules (in addition to the skill)

1. **Research** against reputable primary and named sources. For these agentic-AI / RAG topics, UK-regulatory angles are thin, so it is acceptable to lean on Layer 1 sourced stats (adoption benchmarks, vendor docs, peer-reviewed papers, named research firms with disclosed methodology: Gartner, McKinsey, Deloitte, MIT, Anthropic/OpenAI/Google docs, arXiv). Still: every stat needs a figure + unit + date + source URL. No agency blogs, no undated "reports". Where a UK angle genuinely exists (UK adoption, ICO/FCA relevance for agentic-AI risk), use it.
2. **Voice:** friend-who-knows-AI register. British spellings. No em dashes. No banned AI-tell words. Body paragraphs 30–60 words (70 max). Front-load a 40–80 word definitive answer paragraph. Question-format H2s. Promote 3+ named sub-topics in a section to H3.
3. **Comparison table:** required for the "vs" topic; strongly recommended for the others (e.g. agent vs orchestrator, RAG vs fine-tuning, single-agent vs multi-agent). Render as a proper HTML `<table>`.
4. **key_stats.json:** MANDATORY. Exactly **3 or 4** stat tiles (never 5). Each with value (≤12 chars), label, source.
5. **Footer structure — use `<h3>` headings exactly:**
   - `<h3>About the author</h3>` then one `<p>` (Tom McCaul, Founder, Tom & Co, one credential, LinkedIn https://www.linkedin.com/in/tom-mccaul-77b2778/).
   - `<h3>Related Tom & Co reading</h3>` then a `<ul>` of 2–4 `<li><a href="/ai-agency-consultancy/blog/{sibling-slug}">Descriptive anchor</a>. One-sentence description.</li>`. Cross-link to sibling articles in THIS batch (slugs supplied in your task prompt). Use the `/ai-agency-consultancy/blog/{slug}` path exactly.
6. **article.json fields:** `author` must be the plain string `"Tom McCaul"` (not an object). `categories`: `["AI"]`. `date`: `"2026-07-01"`. `featured`: false. `slug` and `id`: your supplied slug. Include the `metadata` block (title, description, keywords, openGraph, twitter) and the JSON-LD `<script>` block (Article + FAQPage + Person) at the end of `content`.
7. **JSON-LD Person** uses Tom McCaul + LinkedIn https://www.linkedin.com/in/tom-mccaul-77b2778/.

## Outputs

Write to `output/2026-07-01-{slug}/`:
- `article.json` (website schema)
- `key_stats.json`
- `sources.md`
- `qa_report.md`
- `internal_link_suggestions.md`
- `preview.html` (standalone, wrap `content` with basic CSS)

## QA gate

Run `python3 scripts/voice_check.py output/2026-07-01-{slug}/article.json`. If any check FAILs, iterate the draft and re-run until it reports CLEAN. CLEAN is required.

## Do NOT

- Do NOT run git add / commit / push.
- Do NOT run push_to_storyblok.py or call Storyblok.
- Do NOT edit any file outside your own `output/2026-07-01-{slug}/` folder (in particular, do not touch data/roadmap.json, data/stat_bank.json, or docs/ — the central process handles those).

## Return

A short summary: slug, word count, citation count, stat layer used, voice_check result (CLEAN), and the output folder path.
