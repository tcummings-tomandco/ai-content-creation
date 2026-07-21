# Sources: What is MCP (Model Context Protocol) in plain English?

1. **Anthropic — "Introducing the Model Context Protocol"**
   https://www.anthropic.com/news/model-context-protocol
   Accessed: 2026-07-21
   Supports: MCP's release date (25 November 2024) and the framing of the fragmented, one-off integration problem ("M times N") that MCP replaces with a single open protocol.

2. **OpenAI — "OpenAI co-founds the Agentic AI Foundation under the Linux Foundation"**
   https://openai.com/index/agentic-ai-foundation/
   Accessed: 2026-07-21
   Supports: MCP's move to neutral governance in December 2025, and the founding members (Anthropic, OpenAI, Google, Microsoft, AWS, Block).

3. **Model Context Protocol project blog — "One Year of MCP: November 2025 Spec Release"**
   https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/
   Accessed: 2026-07-21
   Supports: registry size (close to 2,000 listed servers by November 2025) and community size (2,900+ contributors).

4. **British Chambers of Commerce and University of Essex — "Half of SMEs using AI, with limited headcount impact so far"** (Future of Work: AI in the Workplace report, March 2026)
   https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
   Accessed: 2026-07-21
   Supports: 54% of UK SMEs using AI in some form by 2026 (up from 35% in 2025, 25% in 2024, 23% in 2023), and ~11% of SMEs moving beyond generic tools into bespoke, deeper integration. Base input for the Tom & Co Layer 2 calculation (see stat_bank_update.json).

5. **gov.uk (Department for Business and Trade) — "Business population estimates for the UK and regions 2024: statistical release"**
   https://www.gov.uk/government/statistics/business-population-estimates-2024/business-population-estimates-for-the-uk-and-regions-2024-statistical-release
   Accessed: 2026-07-21
   Supports: 5,499,000 UK private-sector businesses at the start of 2024 (published October 2024). Second input for the Tom & Co Layer 2 calculation.

6. **US National Security Agency — "Model Context Protocol (MCP): Security Design Considerations"** (Cybersecurity Information Sheet, May 2026)
   https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF
   Accessed: 2026-07-21
   Supports: prompt injection and unauthorised "confused deputy" access as the primary risks to design MCP deployments around.

7. **Information Commissioner's Office — "Guidance on AI and data protection"**
   https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
   Accessed: 2026-07-21
   Supports: the UK data protection documentation duty that applies when an MCP server passes personal data between a model and business systems.

## Original Tom & Co calculation (Layer 2)

**~2.4 million UK businesses in the "shallow AI adoption" gap.**

Workings: BCC/Essex (source 4) reports 54% of UK SMEs used AI in some form by 2026, but only ~11% had moved beyond generic tools into deeper, bespoke integration. The gap is 54% − 11% = 43 percentage points of UK businesses using AI without deep systems integration. Applied to gov.uk's 5,499,000 UK private-sector businesses (source 5): 0.43 × 5,499,000 ≈ 2,364,570, rounded to "roughly 2.4 million."

Caveat noted in the workings and in `stat_bank_update.json`: the BCC/Essex survey samples SMEs specifically, while the gov.uk figure covers all UK private-sector businesses. Since SMEs make up the vast majority of that population by count, the two are treated as broadly comparable, but this is an order-of-magnitude estimate, not an exact calculation. Neither source publishes this combined figure.

## Sources considered and rejected

Several SEO/content-farm sites (toptenaiagents.co.uk, digitalapplied.com, synvestable.com) surfaced specific-sounding claims during research, e.g. a named UK government "Lex API" covering legal judgments back to 1267, a "28% Fortune 500 implementation rate," and "97 million monthly SDK downloads." None of these could be traced to a primary source, methodology, or original publication, and the "1267" claim in particular reads as an AI-generated fabrication. All were excluded per the stat-sourcing rule against undated, unsourced claims from content farms.
