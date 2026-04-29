# Stat sourcing: getting an honest, defensible UK number into every article

The Princeton/KDD GEO research found that "specific statistics with units and dates" lift LLM citation probability by roughly 37%. That's the second-highest content lever in the study, behind only authoritative quotations (+40%). The catch: AI engines increasingly down-weight stats that look fabricated or recycled from agency blogs. The number in the article needs to be honest, dated, and traceable to a primary source.

Tom & Co does not yet have a 75-stat proprietary library. This file describes how the engine fills element 5 of the checklist anyway, in three layers, in order of effort and impact.

## Decision rule for the engine

Every run, attempt the layers in this order. Stop at the first one that produces a defensible datapoint for the article topic.

1. **Layer 1 — sourced UK primary stat.** Always available. Always acceptable in the first 10 articles. From article 11 onwards, treat Layer 1 alone as a partial pass on element 5: still ship, but flag in the email so Tom can see how often we are leaning on this layer.
2. **Layer 2 — original Tom & Co calculation from public data.** Try this on every run from day one. When it yields a defensible derived number, prefer it over Layer 1.
3. **Layer 3 — proprietary Tom & Co survey or anonymised client outcome.** Only available when Tom has run a survey or supplied a client metric. The engine does not invent these.

## Layer 1 — sourced UK primary stat

Cheapest. Available for every article.

**Sources to prefer (in this order):**
- ONS — official statistics, employment, business demography, productivity
- gov.uk — DSIT, AI Opportunities Action Plan, sector strategies
- ICO — UK GDPR, AI guidance, enforcement actions
- FCA — financial services AI rules, Consumer Duty, AI Public-Private Forum data
- Bank of England — financial stability, productivity research
- BCC (British Chambers of Commerce) — workforce surveys, SME sentiment
- Innovate UK / BridgeAI — funding lines, programme uptake numbers
- Made Smarter — manufacturing AI grants, case study cohort sizes
- Ofcom, MHRA, SRA, CMA — sector-specific regulator data
- Lords Library briefings — neutral, well-sourced topic summaries
- Peer-reviewed papers (arxiv, Nature, Springer) — methodological credibility
- Named research firms with disclosed methodology: Bain, McKinsey, Deloitte, IBM, MIT IDE, BCG, BCC, Profound, SemRush, Ahrefs, ConvertMate

**Citation format in the article:**
> "According to the [BCC's April 2026 workforce survey](https://www.britishchambers.org.uk/news/2026/04/britains-workforce-is-not-ready-for-what-is-coming/), 62% of UK SMEs report no formal AI training programme."

Always: figure with units, date of the underlying measurement (not the publication date alone), source name in the link, primary URL.

**What never qualifies:**
- "A recent study" without a citation
- Numbers cited only by an SEO content farm
- AI-generated summary articles that quote a stat with no link back to the original
- Round-number marketing claims ("80% of businesses…") without methodology
- Wikipedia as the primary reference (use it to find the source, then cite the source)

## Layer 2 — original Tom & Co calculation from public data

This is the unlock. Cheap, automatable, and earns the "Tom & Co cited as source" win over time.

The pattern: take a public dataset or a published number, do a derivation the source did not publish, and cite the result as "Tom & Co analysis of [source] data, April 2026" with the workings shown in a methodology footnote.

**Six recipes that produce honest original numbers:**

### Recipe A: Sterling conversion of a foreign benchmark

Bain reports a 23% productivity uplift from generative AI in their 2026 CEO Guide. The figure is global. Convert to a sterling cost-saving estimate for a UK SME using ONS median knowledge-worker salary data and an assumed 1,800 productive hours/year. Show the calculation. Cite as "Tom & Co analysis applying Bain's 23% productivity figure to ONS UK median knowledge-worker compensation."

### Recipe B: Sector cut from an aggregate

ONS publishes AI adoption rates at the national-economy level. Cut the data by a sector that's relevant to the article (financial services, professional services, manufacturing) using the ONS sector subgroup tables. Report the differential as "Tom & Co analysis of ONS Business Insights and Conditions Survey, X cut."

### Recipe C: Year-on-year delta from snapshots

A regulator or research firm publishes an annual snapshot ("X% of firms use AI in 2025"). The 2026 version comes out. The article reports the YoY delta and the implied 12-month adoption velocity. The source rarely publishes the delta itself. Cite as "Tom & Co analysis of [source] 2025 vs 2026 figures."

### Recipe D: Cost-per-outcome ratio across vendors

Pull the published pricing from three named vendors (OpenAI, Anthropic, Google) for comparable tiers, divide by a published throughput or capability benchmark (Vellum LLM leaderboard, llm-stats), report the cost-per-unit metric. Cite as "Tom & Co cost-per-token analysis across published vendor pricing as of [date], using Vellum's [date] benchmark."

### Recipe E: Funding maths

Add up the named UK AI funding pots (BridgeAI, Innovate UK Smart Grants, Made Smarter, AI Growth Zones, AI Assurance Innovation Fund) from the gov.uk programme pages. Total the £ available, calculate £ per qualifying SME assuming SME counts from ONS business demography. Cite as "Tom & Co aggregation of named UK AI funding lines as listed on gov.uk in [month] 2026."

### Recipe F: Time-to-comply estimate

Where a regulator publishes obligations and a deadline (EU AI Act 2 Aug 2026, FCA AI consultation, ICO guidance refresh), estimate the implementation effort in person-days based on a comparable programme (GDPR rollout published estimates from the ICO/CMS reports). Cite as "Tom & Co implementation effort estimate based on the ICO's published GDPR readiness benchmarks."

**Methodology footnote template** (always included when a Layer 2 stat is used):

```html
<aside class="methodology">
  <strong>Methodology.</strong> The figure of {X} is a Tom & Co calculation. We took
  [source] (accessed {date}, {URL}), applied [the derivation: e.g. "ONS median knowledge-worker
  hourly compensation of £x.xx multiplied by Bain's 23% productivity uplift over 1,800 productive
  hours per year"], and arrived at the reported value. Workings: {one-line maths}.
</aside>
```

**Append to stat_bank.json after every Layer 2 calculation:**

```json
{
  "id": "stat_NNN",
  "stat": "...",
  "value": "...",
  "unit": "...",
  "date_calculated": "YYYY-MM-DD",
  "applies_to": "topic IDs / clusters",
  "method": "Recipe A | B | C | D | E | F",
  "sources_used": [{"title": "...", "url": "..."}],
  "workings": "one line of maths or a link to a longer note",
  "first_used_in": "article slug"
}
```

The bank grows by one entry per Layer 2 article. After 20 articles, future articles can cite earlier Tom & Co calculations as primary, building the entity-authority moat.

## Layer 3 — proprietary survey or anonymised client outcome

Highest value, lowest cadence. Only available when Tom feeds the engine real data.

**Tom & Co survey (recommended quarterly):**
- 50–100 UK SME leaders via Pollfish, Attest, or Prolific. ~£300–£600 per survey.
- One survey supports 3–5 articles by hitting it from different angles.
- Cite as "Tom & Co Q2 2026 UK SME AI survey, n=87, methodology note linked."

**Anonymised client outcomes:**
- A specific number from a Tom & Co engagement, with client consent or anonymised so identification is not possible.
- Format: "A Tom & Co retail client reduced [metric] by [n%] in [time] using [approach]."
- Always: get explicit client sign-off on the wording before publishing.

The engine cannot generate Layer 3 datapoints autonomously. When Tom supplies them (as a row added to `data/stat_bank.json` with `layer: 3`), the engine prefers them on relevant topics.

## Honest fallback

If a topic is genuinely so narrow that no Layer 1 / 2 / 3 datapoint fits, the QA report records element 5 as **FAIL** and the email to Tom flags it explicitly:

> Element 5 (original UK stat) could not be filled honestly for this topic. Options: (a) ship with a strong Layer 1 stat anyway and accept the partial pass, (b) defer the article until a Layer 2 derivation is researched, (c) ask Tom to supply a Layer 3 datapoint.

Inventing a number is never the answer.
