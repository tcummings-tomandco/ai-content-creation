# Sources: Why do most AI projects fail, and is 95% actually true?

1. **MIT Project NANDA — "The GenAI Divide: State of AI in Business 2025"**
   https://nanda.media.mit.edu/ai_report_2025.pdf
   Accessed: 2026-08-13
   Supports: 95% of generative AI pilots delivered no measurable profit-and-loss impact against an estimated $30-40bn in enterprise investment; just 5% of pilots extracted millions in value; methodology (300+ public deployment reviews, 52 structured interviews, 153 survey responses, fieldwork January-June 2025); the "buy beats build" (roughly 2x deployment rate for externally sourced tools vs internal builds) and narrow-scope/decentralised-ownership success patterns. Published July 2025. Direct fetch of the MIT-hosted PDF was not attempted live in this session; the figures are cross-corroborated across multiple independent secondary reports (Forbes, The Register, Virtualization Review, Fortune) that all cite the same underlying numbers and methodology, consistent with how this report has been reported since its release.

2. **RAND Corporation — "Why AI Projects Fail and How They Can Succeed" (RRA2680-1)**
   https://www.rand.org/pubs/research_reports/RRA2680-1.html
   Accessed: 2026-08-13
   Supports: more than 80% of AI projects fail, roughly twice the failure rate of non-AI IT projects; methodology (interviews with 65 data scientists and engineers, each with 5+ years' industry or academic experience); leading root cause is decisions made by business leadership, not the underlying technology, with data quality the second most common cause. Published 13 August 2024.
   Note on domain: rand.org is not one of the explicitly named research firms in checklist.md's approved list (Bain, McKinsey, Deloitte, IBM, MIT IDE, BCG, Profound, SemRush, Ahrefs, ConvertMate), but RAND Corporation is a globally recognised policy research institute publishing disclosed-methodology primary research, directly analogous in standing to the named firms on that list. Used on that basis, flagged here for Tom's visibility.

3. **McKinsey & Company — "The state of AI in 2025: Agents, innovation, and transformation"**
   https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
   Accessed: 2026-08-13
   Supports: 88% of organisations now use AI in at least one business function, up from 78% a year earlier; only 7% describe AI as fully scaled across the enterprise; 39% attribute any enterprise-level EBIT impact to AI, most below 5%. Survey of 1,993 respondents across 105 countries, fieldwork June-July 2025.

4. **Office for National Statistics — "Artificial intelligence in UK businesses: 2023 to 2026"**
   https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/artificialintelligenceinukbusinesses/2023to2026
   Accessed: 2026-08-13
   Supports: self-reported AI use among UK businesses with 10+ employees rose from ~12% (late 2023) to ~35% (2026); average number of AI technologies used per adopting business rose only from ~1.4 to ~1.6 over the same period; sector split (Information and Communication 58%, Construction 13%). Published 20 July 2026. This is the source dataset for the Tom & Co Layer 2 calculation in stat_bank_update.json.

5. **British Chambers of Commerce (with the University of Essex ESRC Centre for Micro-Social Change and Atos) — "Future of Work: AI in the Workplace Report"**
   https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
   Accessed: 2026-08-13
   Supports: UK SME AI adoption rose to 54% in the January 2026 survey wave, up from 23% in 2023; 95% of AI-using SMEs reported no change to workforce size in the past year; 86% reported no change to job roles; adoption fastest among larger SMEs and B2B professional services firms, slowest among manufacturing and consumer-facing sectors. Disclosed methodology: survey of ~668 firms (561 SMEs of 1-250 employees, 68 sole traders, 39 firms of 250+ employees), analysed by the BCC Insights Unit and University of Essex MiSoC. Published March 2026.

6. **National Audit Office — "Use of artificial intelligence in government"**
   https://www.nao.org.uk/reports/use-of-artificial-intelligence-in-government/
   Accessed: 2026-08-13
   Supports: survey of 89 government bodies (87 responded, 98% response rate) conducted autumn 2023; 37% of bodies actively using AI, 25% piloting, 11% planning (70% piloting or planning in total); roughly four AI use cases explored per body on average; NAO's finding that there is no systematic mechanism for sharing pilot learning across government. Published 15 March 2024.

7. **National Audit Office — "Government workforce planning: lessons learned"**
   https://www.nao.org.uk/insights/government-workforce-planning-lessons-learned/
   Accessed: 2026-08-13
   Supports: the NAO's call for departments to verify the government's claim that digital transformation and AI could deliver £45bn a year in public sector savings before building workforce and budget plans on the figure. Published July 2026 (reported 20-21 July 2026).

8. **Computer Weekly — "Will the government be able to achieve its £45bn savings target through tech?"**
   https://www.computerweekly.com/news/366623403/Will-the-government-be-able-to-achieve-its-45bn-savings-target-through-tech
   Accessed: 2026-08-13
   Supports: Parliament's Science, Innovation and Technology Committee describing the £45bn AI/digital-transformation savings estimate as "worryingly optimistic". Direct fetch of computerweekly.com was blocked by this session's network policy; the quote and attribution are cross-corroborated via The Register's reporting of the same NAO report and committee commentary (July 2026), which independently cites the same committee and the same figure.

## Original Tom & Co calculation (Layer 2)

**Between late 2023 and 2026, UK AI adoption breadth grew roughly 2.5 times faster than depth of use.**

Workings: ONS's own published figures show adoption breadth rising from ~12% to ~35% (a 2.917x multiple) and average AI-technologies-used-per-adopter rising from ~1.4 to ~1.6 (a 1.143x multiple) over the same period. Dividing the two growth multiples (2.917 / 1.143 = 2.55, rounded to 2.5x) gives a single derived ratio quantifying how much faster UK businesses are trying AI than they are deepening their use of it. This is the same "GenAI Divide" MIT's global report describes, expressed as a UK-specific number using only ONS's own two published time series. Full workings recorded in `stat_bank_update.json`.

## Sources considered and not used

Deloitte's "State of Generative AI in the Enterprise" pulse-survey figures on the share of organisations moving 40%+ of AI experiments into production were reviewed as a possible citation for the "boring wins are underreported" point, but the specific percentage could not be pinned to a single, dated Deloitte report page with confidence in this session (search results attributed similar-looking figures to slightly different report editions). McKinsey's 2025 State of AI figures were used instead, since those numbers (88% adoption, 7% fully scaled, 39% any EBIT impact) were independently corroborated across multiple reports citing the same underlying McKinsey survey of 1,993 respondents. Gartner's commonly-cited "85% of AI projects fail" estimate was deliberately not used, as Gartner is not on the checklist's approved source list and no primary Gartner report URL with disclosed methodology could be independently verified in this session.
