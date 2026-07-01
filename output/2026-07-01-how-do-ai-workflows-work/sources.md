# Sources: How do AI workflows work?

Slug: `how-do-ai-workflows-work` | Date: 2026-07-01 | Target keyword: ai workflows

All figures carry a figure + unit + date + primary source URL. No agency blogs, no undated reports.

## Inline citations (primary sources)

1. **Anthropic, "Building Effective Agents"** — published 19 December 2024.
   URL: https://www.anthropic.com/engineering/building-effective-agents
   Supports:
   - Definition of a workflow: "systems where LLMs and tools are orchestrated through predefined code paths."
   - Definition of an agent: "systems where LLMs dynamically direct their own processes and tool usage."
   - The five workflow patterns (prompt chaining, routing, parallelisation [sectioning + voting], orchestrator-workers, evaluator-optimizer) and each pattern's example use case.
   - Guidance quote: "Start with simple prompts ... and add multi-step agentic systems only when simpler solutions fall short." (Verbatim in article, trimmed with ellipsis to omit the word "comprehensive", a banned voice-guide term; meaning preserved.)

2. **ONS Business Insights and Conditions Survey (BICS)** — bulletin published 8 January 2026, Wave 147, fieldwork 15-28 December 2025.
   URL: https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/bulletins/businessinsightsandimpactontheukeconomy/8january2026
   Supports:
   - "Approximately a quarter (25%) of businesses reported that they are currently using some form of artificial intelligence (AI) technology in late December 2025."
   - 44% of businesses with 250+ employees currently using AI.
   - +15 percentage points since the question was first introduced in late September 2023.

3. **British Chambers of Commerce with the University of Essex (ESRC Centre for Micro-Social Change, MiSoC)** — "Half of SMEs using AI, with limited headcount impact so far", published 18 March 2026 (research partner: Atos).
   URL: https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
   Supports:
   - "More than half of UK firms (54%) are now actively using AI."
   - Year-on-year series: 23% (2023), 25% (2024), 35% (2025), 54% (2026).
   - "A smaller group of SMEs (one in ten) are adopting deeper bespoke AI" beyond generic tools like ChatGPT and Copilot.

4. **McKinsey, "The State of AI in 2025: Agents, innovation, and transformation"** — published November 2025.
   URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
   Supports:
   - 23% of organisations scaling agentic AI systems somewhere in the enterprise; 62% at least experimenting with agents.
   - ~6% of respondents qualify as high performers reporting significant value and attributing more than 5% of EBIT to AI.
   - High performers are 2.8x more likely to report fundamental workflow redesign (55% vs 20% of others).
   Note: the McKinsey source page repeatedly timed out on direct fetch; the 2.8x / 55% vs 20% figure and the 6% / 23% / 62% figures were captured from search-surfaced quotes of the report and cross-checked against a secondary that quotes the report verbatim (cxtoday.com, 23 Feb 2026). Recommend a human confirm the 2.8x line against the report PDF before publish.

## Layer 2 original calculation (Tom & Co analysis)

**Stat used in body (blockquote) and key_stats tile:** The single-year jump in UK AI adoption to 2026 was +19 percentage points, the largest annual gain in the BCC series and more than the previous two years combined.

- Method: Recipe C (year-on-year delta from published snapshots the source did not itself difference).
- Source data: BCC/University of Essex adoption series — 23% (2023), 25% (2024), 35% (2025), 54% (2026), from the 18 March 2026 BCC release above.
- Workings: YoY deltas = +2pp (2023→2024), +10pp (2024→2025), +19pp (2025→2026). The +19pp gain exceeds +2pp + +10pp = +12pp (the prior two years combined). Adoption near-doubled its 2023 base in three years (CAGR of the adoption share ≈ 33%/yr: (54/23)^(1/3) − 1 = 0.329).
- Attribution string in article: "Tom & Co analysis of the BCC adoption series (23% in 2023, 25% in 2024, 35% in 2025, 54% in 2026)".

**Second Layer 2 figure referenced (cost of productive hour):** ~£24/hour of UK knowledge-worker productive time.
- This reuses the existing stat_bank entry stat_003 workings (ONS ASHE 2024 median full-time weekly earnings £728 → ~£42,800/yr fully loaded employer cost ÷ 1,800 productive hours ≈ £23.78/hr, rounded to ~£24). Attributed as "Tom & Co analysis of ONS Annual Survey of Hours and Earnings 2024 data".
- Source: ONS ASHE 2024, https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2024

## Stat bank note

Per the ad-hoc batch rules, this subagent did NOT edit `data/stat_bank.json`. A new Layer 2 entry should be appended by the central process for the BCC adoption-velocity calculation (Recipe C). Proposed entry:

- stat: "Single-year jump in UK AI adoption (share of firms) to 2026"
- value: "19" | unit: "percentage points" | date_calculated: 2026-07-01
- method: Recipe C (YoY delta from BCC/University of Essex 2023-2026 series)
- first_used_in: how-do-ai-workflows-work
