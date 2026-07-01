# Sources: What are AI agents? A plain-English guide for UK businesses

Slug: `what-are-ai-agents` | Date: 2026-07-01 | Cluster: Operations & Efficiency (Format A: Definition + benchmark table)

Every cited source below is a named vendor engineering doc, a UK government primary, a named research firm with disclosed methodology, or a reputable named trade-press report. No agency blogs or undated content-farm listicles were used.

## Inline citations (in article body order)

1. **Anthropic, "Building Effective Agents" (engineering)**
   - URL: https://www.anthropic.com/engineering/building-effective-agents
   - Accessed: 2026-07-01
   - Claims supported: Agents are "LLMs that dynamically direct their own processes and tool usage"; agents "are typically just LLMs using tools based on environmental feedback in a loop"; the agent/workflow distinction ("workflows... orchestrated through predefined code paths" vs agents that dynamically direct themselves); the need to get "ground truth" from the environment at each step.

2. **OpenAI, "A Practical Guide to Building Agents" (April 2025)**
   - URL: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
   - Accessed: 2026-07-01
   - Claims supported: Agents are "systems that independently accomplish tasks on your behalf"; agents execute workflows end-to-end with autonomy; three core components (model, tools, instructions/guardrails).

3. **IBM, "What Are AI Agents?" (Think Topics)**
   - URL: https://www.ibm.com/think/topics/ai-agents
   - Accessed: 2026-07-01
   - Claims supported: An AI agent is a system "capable of autonomously performing tasks on behalf of a user by designing its workflow and utilising available tools"; core components of reasoning, planning, tool use and memory; chatbots typically lack tools, memory and advanced reasoning.

4. **DSIT, "AI Adoption Research" (gov.uk)** — UK PRIMARY
   - URL: https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research
   - Publisher: Department for Science, Innovation and Technology
   - Measurement window: survey conducted 12 February – 2 May 2025; 3,500 UK private-sector businesses with 5+ employees
   - Accessed: 2026-07-01
   - Claims supported: 16% of UK businesses use at least one AI technology; agentic AI is the least-adopted technology among AI adopters at 7%; only 13% of planned adopters intend to use agentic AI, and about a quarter of those expect implementation within 12 months.

5. **Computer Weekly, "Governance lags agentic AI adoption in the UK, says Salesforce"** (reporting the Salesforce 2026 Connectivity Benchmark, produced with Vanson Bourne / Deloitte Digital)
   - URL: https://www.computerweekly.com/news/366638841/Governance-lags-agentic-AI-adoption-in-the-UK-says-Salesforce
   - Underlying survey: 1,050 IT professionals, October–November 2025; UK/Ireland figures reported
   - Accessed: 2026-07-01
   - Claims supported: 89% of UK and Ireland organisations already deploy AI agents; ~12 agents on average; roughly half of agents sit in silos; only 54% of organisations have a centralised governance framework.

6. **Gartner press release, "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027" (25 June 2025)**
   - URL: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
   - Accessed: 2026-07-01
   - Claims supported: over 40% of agentic AI projects cancelled by end of 2027 (costs, unclear value, weak risk controls); "agent washing"; only ~130 of thousands of claimed agentic vendors are genuine; at least 15% of day-to-day work decisions made autonomously via agentic AI by 2028 (up from 0% in 2024).
   - Note: Gartner press-release page returns HTTP 403 to automated fetchers; figures cross-checked against the release title/URL and multiple independent reports (MarTech, BigDATAwire).

7. **McKinsey, "The State of AI in 2025: Agents, innovation, and transformation" (November 2025)**
   - URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
   - Accessed: 2026-07-01
   - Claims supported (blockquote): 62% of organisations are at least experimenting with AI agents; 23% are scaling them somewhere; ~6% qualify as AI high performers seeing significant value; most respondents attribute less than 5% of EBIT to AI.

8. **ONS, "Annual Survey of Hours and Earnings (ASHE) 2024"** — UK PRIMARY (Layer 2 workings)
   - URL: https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2024
   - Accessed: 2026-07-01
   - Claims supported: median full-time weekly earnings £728, underpinning the Tom & Co break-even calculation.

## Original stat used (Layer 2)

- **Tom & Co analysis (stat_bank stat_003):** a 10-person UK knowledge-worker team on a ~£1,900/year business AI subscription needs each person to save roughly 9 minutes per working week to break even.
- Method: Recipe D (cost-per-outcome ratio using ONS median earnings and published vendor pricing). First calculated 2026-06-25 for `chatgpt-vs-claude-vs-gemini-for-business`; reused here as prior Tom & Co analysis.
- Workings (from `data/stat_bank.json`): ONS ASHE 2024 median £728/week × 52 = £37,856 gross; + employer NI (13.8% above £9,100) £3,968; + 3% pension (above £6,240) £948 = ≈£42,800/year; at 1,800 productive hours = £23.78/hour; £1,920/year ÷ 10 = £192/person ÷ £23.78 = 8.07 hours/year = ~9 minutes/person/week.
- No new stat_bank.json entry written (per ad-hoc batch rules: do not edit files outside this output folder). This article reuses stat_003 rather than deriving a new number.

## Sources considered and rejected

- smartaihuman.com, nexos.ai, cogitx.ai, aristral.com, whito.co.uk, molevalleychamber.co.uk, paul-okhrem.com, prefactor.tech, firstpagesage.com, digitalapplied.com — SEO content-farm or agency-blog listicles, not primary; used only as discovery leads, none cited.
- Wikipedia — not cited as a primary reference.
