# Sources: AI agents vs RPA vs traditional automation: what's the difference?

Topic ID: 11 | Cluster: Operations & Efficiency | Priority: P1 | Accessed: 2026-08-18

1. **Office for National Statistics** — [Artificial intelligence in UK businesses: 2023 to 2026](https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/artificialintelligenceinukbusinesses/2023to2026)
   Accessed: 2026-08-18. Supports: UK business AI adoption rising from ~12% (late 2023) to ~35% (2026), and the average number of AI technologies used per adopting business rising only from 1.4 to 1.6 over the same period. Used twice — once for the breadth/depth context, once for the "combining tools is the norm" point in the hybrid section.

2. **techUK** — [Robotic process automation: Industry adoption trends and benefits](https://www.techuk.org/resource/robotic-process-automation-industry-adoption-trends-and-benefits.html)
   Accessed: 2026-08-18. Supports: 28% of UK businesses already running RPA, 34% planning to start, 64% using process mining first (figures drawn from Abbyy research, reported via techUK).

3. **UK Government (DSIT)** — [AI Insights: Agentic AI](https://www.gov.uk/government/publications/ai-insights/ai-insights-agentic-ai-html)
   Accessed: 2026-08-18. Supports: the definition of an AI agent as a small, specialised piece of software that can make decisions, and agentic AI as a system of such agents behaving and interacting autonomously.

4. **Bank of England (Bank Underground staff blog)** — [Is artificial intelligence making us more productive? What the UK industry data show](https://bankunderground.co.uk/2026/08/06/is-artificial-intelligence-making-us-more-productive-what-the-uk-industry-data-show/)
   Accessed: 2026-08-18. Published: 6 August 2026. Supports: AI's measured productivity gains sitting mostly in the sectors building the technology (software/IT consultancy's contribution to productivity growth rising roughly tenfold vs the pre-pandemic decade, adding ~0.1 percentage points 2023-2025), rather than in the sectors deploying automation.
   Note: Bank Underground is the Bank of England's official staff research blog, hosted on its own domain rather than bankofengland.co.uk directly. Flagged in qa_report.md as a judgement call against the checklist's literal domain list.

5. **UK Government** — [Interim government response to the AI Champions' AI Adoption Plans](https://www.gov.uk/government/publications/ai-champions-ai-adoption-plans-interim-government-response/interim-government-response-to-the-ai-champions-ai-adoption-plans)
   Accessed: 2026-08-18. Supports: the government writing to 19 regulators in January 2026 (covering financial services, life sciences, law and others) asking each to publish a plan for enabling safe AI-powered innovation.

6. **UK Government (HM Treasury / DSIT)** — [Financial Services AI Adoption Plan](https://www.gov.uk/government/publications/ai-adoption-plan-financial-services/financial-services-ai-adoption-plan)
   Accessed: 2026-08-18. Supports: "Know Your Agent" protocols and legal liability rules set out specifically for autonomous agentic payments, illustrating a governance layer that RPA has never required.

7. **UK Parliament — Public Accounts Committee / National Audit Office** — [Use of AI in Government](https://publications.parliament.uk/pa/cm5901/cmselect/cmpubacc/356/report.html)
   Accessed: 2026-08-18. Supports: NAO finding that 70% of government bodies were piloting or planning AI use by March 2024, and the PAC's follow-up report attributing stalled pilot-to-production progress to poor-quality data locked in legacy IT systems.

8. **British Chambers of Commerce, with Atos and the University of Essex** — [Half of SMEs using AI, with limited headcount impact so far](https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/)
   Accessed: 2026-08-18. Published: March 2026. Supports: 54% of UK SMEs using AI (up from 23% in 2023); only 11% of SMEs using AI extensively to automate operations. Basis for the Tom & Co original-calculation stat (see below).

9. **McKinsey** — [The state of AI](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
   Accessed: 2026-08-18. Supports: global figures on agentic AI maturity — only 23% of organisations scaling an agentic system, and 88% of agent pilots failing to reach production (evaluation gaps, governance friction and model reliability cited as the leading blockers). Included as a named research firm with disclosed methodology; figures are global, not UK-specific, and are presented as such in the article.

## Tom & Co original calculation (Layer 2)

**Claim:** Only around 1 in 5 AI-using UK SMEs (11 of the 54 percentage points reporting AI use) say they use AI to automate operations extensively.

**Method:** BCC/Atos found 54% of UK SMEs use AI in some form, and separately that 11% of SMEs use AI extensively to automate operations. 11 ÷ 54 = 0.2037 ≈ 20%, i.e. roughly 1 in 5 AI-using SMEs are using it for deep automation rather than lighter assistance. The source reports both figures but never publishes the ratio between them.

**Sources used:** British Chambers of Commerce / Atos / University of Essex, Future of Work: AI in the Workplace, March 2026 (URL above).

See `stat_bank_update.json` for the full entry appended to `data/stat_bank.json`.
