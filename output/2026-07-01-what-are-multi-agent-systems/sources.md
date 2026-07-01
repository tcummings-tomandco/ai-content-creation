# Sources: What are multi-agent systems? A plain-English UK guide

Topic: What are multi-agent systems? | Target keyword: multi agent systems | Slug: what-are-multi-agent-systems | Date: 2026-07-01

## Cited sources (in article body)

1. **Anthropic, "How we built our multi-agent research system"** (engineering blog)
   - URL: https://www.anthropic.com/engineering/multi-agent-research-system
   - Published: 13 June 2025. Accessed: 1 July 2026.
   - Supports: orchestrator-worker architecture; lead agent spins up 3-5 subagents in parallel; each subagent has a self-contained brief, its own fresh context window, no knowledge of the others; simple fact-finding needs ~1 agent; multi-agent system beat single-agent Claude Opus 4 by 90.2% on internal eval; agents use ~4x tokens of a chat, multi-agent systems ~15x; token usage alone explains ~80% of performance variance; separate citation pass.

2. **Anthropic pricing page** (Claude Opus 4.8 list pricing)
   - URL: https://www.anthropic.com/pricing
   - Accessed: 1 July 2026.
   - Supports: Claude Opus 4.8 list price of $5 per million input tokens and $25 per million output tokens, used as the basis for the Layer 2 cost calculation. (Pricing cross-checked against the Anthropic model catalogue: Opus 4.8 = $5.00 input / $25.00 output per 1M tokens.)

3. **British Chambers of Commerce, "Powering Productivity: AI and the Future of UK Work"** (report, with Atos and University of Essex ESRC Centre for Micro-Social Change / MiSoC)
   - URL: https://www.britishchambers.org.uk/wp-content/uploads/2026/03/Powering-Productivity-AI-and-the-Future-of-UK-Work_FINAL.pdf
   - Published: March 2026. Accessed: 1 July 2026.
   - Supports: agentic AI was the least-adopted AI category at 7% of firms; text generation at 85%; half of AI-using firms using more than one AI technology.

4. **British Chambers of Commerce, "Half of SMEs Using AI - With Limited Headcount Impact So Far"** (news release on the same research)
   - URL: https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
   - Published: 18 March 2026. Accessed: 1 July 2026.
   - Supports: 54% of UK firms actively using AI, up from 35% in 2025, 25% in 2024 and 23% in 2023; 95% of AI-using SMEs report no impact on workforce size; research by BCC Insights Unit with the University of Essex MiSoC, in partnership with Atos; ~94% of firms surveyed were SMEs.

5. **Gartner press release, "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026..."**
   - URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
   - Published: 26 August 2025. Accessed: 1 July 2026 (page returned HTTP 403 to automated fetch; figures confirmed via Gartner-attributed search results and the press-release headline itself).
   - Supports: over 40% of agentic AI projects predicted to be cancelled by the end of 2027 (cost, unclear value, inadequate risk controls); headline forecast that 40% of enterprise apps will feature task-specific AI agents by end-2026, up from less than 5% in 2025.

6. **ICO, "Guidance on AI and data protection"**
   - URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
   - Accessed: 1 July 2026.
   - Supports: requirement for a Data Protection Impact Assessment when an AI system processes personal data at scale (UK GDPR / DPIA obligation).

## Supporting / background research (not cited inline)

- **Tran, Dao, Nguyen, Pham, O'Sullivan, Nguyen, "Multi-Agent Collaboration Mechanisms: A Survey of LLMs"**, arXiv:2501.06322, submitted 10 January 2025. https://arxiv.org/abs/2501.06322
  - Confirms the academic framing of LLM multi-agent collaboration across five dimensions: actors, types (cooperation/competition/coopetition), structures (peer-to-peer/centralized/distributed), strategies (role-based/model-based) and coordination protocols. Used to sense-check the definition and the orchestrator-worker framing.
- **Framework landscape (background, not cited):** OpenAI Agents SDK (handoffs, March 2025), Google A2A protocol / ADK (April 2025), Microsoft Agent Framework / AutoGen successor, LangGraph, CrewAI. Used only to confirm that the orchestrator-worker + parallel-worker pattern is consistent across the major 2025-2026 frameworks.

## Layer 2 original calculation (methodology note)

**Claim:** A single complex query costs roughly £0.39 as a single-agent run (~4x a chat) and roughly £1.48 as a multi-agent run (~15x a chat), against about 10p as a plain chat turn, on Claude Opus 4.8 list pricing.

**Method:** Recipe A / D (sterling conversion of a benchmark multiplier + vendor cost application).

**Workings:**
- Baseline representative complex chat turn assumed at 15,000 input tokens + 2,000 output tokens.
- Claude Opus 4.8 list pricing: $5.00 / 1M input tokens, $25.00 / 1M output tokens (Anthropic).
- Baseline chat cost = (15,000 x $5 + 2,000 x $25) / 1,000,000 = $0.075 + $0.050 = $0.125.
- Apply Anthropic's published token multipliers to the whole token bill: single agent ~4x = $0.50; multi-agent ~15x = $1.875.
- FX at $1.27 to the pound (illustrative, July 2026): baseline chat = £0.098 (~10p); single agent = £0.394 (~£0.39); multi-agent = £1.476 (~£1.48).
- Presented as directional estimates, rounded, with the multiplier ratio (15x) as the headline. Not a vendor quote.

**Attribution used in article:** "Tom & Co estimate applying Anthropic's published token multipliers to Claude Opus 4.8 list pricing (July 2026, converted at $1.27 to the pound)."

**Note for stat bank:** This is a fresh Layer 2 calculation. The central process should append it to data/stat_bank.json (subagents do not edit the shared bank). Suggested entry: value 15 (ratio, multi-agent tokens vs chat) and the £1.48-per-query derived figure; method Recipe A/D; sources = Anthropic multi-agent write-up + Anthropic pricing; first_used_in = what-are-multi-agent-systems; layer 2.
