# Sources: What is an AI agent orchestrator?

Accessed: 2026-07-01

---

## 1. How we built our multi-agent research system — Anthropic

**URL:** https://www.anthropic.com/engineering/multi-agent-research-system
**Publisher:** Anthropic (engineering blog)
**Claim supported:** The orchestrator-worker pattern in which a lead agent analyses a query, develops a strategy, and spawns subagents to explore different aspects in parallel. The lead agent is the orchestrator. A system using Claude Opus 4 as lead agent with Claude Sonnet 4 subagents scored 90.2% higher than a single Claude Opus 4 agent on Anthropic's internal research eval (task: identifying all board members of S&P 500 IT companies). Agents use ~4x the tokens of a chat; multi-agent systems use ~15x. Token usage alone explains 80% of performance variance on the BrowseComp evaluation. Multi-agent systems excel at heavy parallelisation, information exceeding a single context window, and interfacing with many complex tools; they are poorly suited to tasks where all agents need the same shared context or have heavy inter-agent dependencies.

---

## 2. AI Agent Orchestration Patterns — Microsoft Azure Architecture Center

**URL:** https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns
**Publisher:** Microsoft (Azure Architecture Center)
**Page dates:** ms.date 12 February 2026; updated 12 May 2026
**Claim supported:** Definition of multi-agent orchestration as an orchestrator (or peer-based protocol) that manages work distribution, context sharing, and result aggregation. The five orchestration patterns: sequential (pipeline / prompt chaining / linear delegation), concurrent (parallel / fan-out-fan-in / scatter-gather), group chat (roundtable / multi-agent debate, chat manager coordinates, recommend three or fewer agents, maker-checker loops), handoff (routing / triage / dispatch, one agent at a time), and magentic (dynamic / task-ledger-based / adaptive planning, manager agent builds and refines a plan). Guidance to use the lowest level of complexity that reliably meets requirements. Examples: sequential contract pipeline, concurrent stock analysis, group-chat park proposal review, handoff telecom support, magentic SRE incident response.

---

## 3. Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026

**URL:** https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
**Publisher:** Gartner (press release, 26 August 2025)
**Claim supported:** 40% of enterprise applications will feature task-specific AI agents by the end of 2026, up from less than 5% in 2025. By 2027, one-third of agentic AI implementations will combine agents with different skills to manage complex tasks. (Note: primary URL returned HTTP 403 to the automated fetcher; figures corroborated across multiple reporting outlets citing this Gartner release and the identical press-release title. Verify the live page before publish.)

---

## 4. AI Adoption Research — GOV.UK (DSIT)

**URL:** https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research
**Publisher:** Department for Science, Innovation & Technology (DSIT). Research page updated 13 February 2026.
**Fieldwork:** Computer-assisted telephone interviews, 12 February to 2 May 2025, 3,500 completed business interviews.
**Claim supported:** 16% of UK businesses currently use at least one AI technology (a further 5% plan to adopt). Agentic AI was the least adopted technology at 7%, "likely due to its relative newness." Sector variation: agentic AI adoption reached 12% in agriculture, mining, manufacturing and energy, and 10% in information and communication, versus 5% among businesses overall.

---

## 5. The State of AI in 2025: Agents, innovation, and transformation — McKinsey

**URL:** https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
**Publisher:** McKinsey & Company (QuantumBlack), published November 2025
**Claim supported:** 23% of organisations are actively scaling an agentic AI system in at least one business function; in any given business function no more than 10% of respondents report scaling AI agents. Used to illustrate the gap between experimenting with agents and scaling them in production, which is where orchestration decisions become material.

---

## Tom & Co Layer 2 Calculation (Recipe D — cost-per-outcome ratio)

**Stat:** Orchestration cost premium of a multi-agent orchestrated system over a single agent
**Value:** approximately 3.75x
**Method:** Anthropic reports that a multi-agent system uses about 15x the tokens of a chat, and a single agent uses about 4x the tokens of a chat. Dividing the multi-agent multiplier by the single-agent multiplier isolates the premium attributable to orchestration itself: 15 / 4 = 3.75. Worked example in the article: a request costing a single agent £100 in model spend runs to roughly £375 for an orchestrated multi-agent version.
**Assumptions / caveats:** Token count is used as a proxy for model spend; the ratio holds only where per-token pricing is comparable across the models used (Anthropic's own example mixes Opus lead + Sonnet subagents, which would change the sterling figure but is presented in the article as an illustrative like-for-like model-spend comparison). The premium is a coordination-cost indicator, not a full total-cost-of-ownership figure (it excludes engineering, latency, and observability costs).
**Cited in article as:** "Tom & Co analysis of Anthropic's published token figures"
