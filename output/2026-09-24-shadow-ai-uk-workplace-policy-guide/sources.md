# Sources: What is shadow AI and how should a UK employer manage it?

All sources accessed 2026-09-24 via web search (direct fetch of gov.uk/ico.org.uk/britishchambers.org.uk/ons.gov.uk domains was blocked by this session's network egress policy, so figures are taken from search-result summaries of the primary pages rather than a direct read of the source page; URLs point to the primary source in every case, not to a secondary write-up).

1. **Deloitte UK GenAI Workforce Survey** (British workers spend nearly £1bn of their own money on GenAI for work)
   https://www.deloitte.com/uk/en/about/press-room/british-workers-spend-one-billion-pounds-of-their-own-money-on-gen-ai-for-work.html
   Publisher: Deloitte UK. Fieldwork 7 May - 10 June 2026, n=25,000 UK workers aged 18-70 (Deloitte's own description: the largest single-country study of workplace GenAI use to date). Published September 2026.
   Supports: 63% of UK workers knowingly use GenAI for work; 31% of those users do so without their employer's knowledge (shadow AI); almost 1 in 10 UK workers has used a tool their employer bans; UK workers spend close to £958m/year of their own money on GenAI tools for work; 17% of GenAI users pay personally for at least one external tool.

2. **Rise in 'Shadow AI' tools raising security concerns for UK** (Microsoft UK, commissioning a Censuswide survey)
   https://ukstories.microsoft.com/features/rise-in-shadow-ai-tools-raising-security-concerns-for-uk/
   Publisher: Microsoft UK. Survey by Censuswide, fielded October 2025, n=2,003 UK employees aged 18+, including minimum quotas across financial services, retail, education, health & social care, large businesses (250+ staff) and public sector.
   Supports: 71% of UK employees have used an unapproved AI tool at least once; 51% continue weekly; top shadow-AI uses are drafting/replying to workplace communications (49%), reports/presentations (40%), finance-related tasks (22%).

3. **Powering Productivity: AI and the Future of UK Work** (British Chambers of Commerce and Atos, March 2026)
   https://www.britishchambers.org.uk/wp-content/uploads/2026/03/Powering-Productivity-AI-and-the-Future-of-UK-Work_FINAL.pdf
   Publisher: British Chambers of Commerce, in partnership with Atos.
   Supports: 54% of UK SMEs actively using AI; 70% of UK businesses give staff access to an AI tool but only 48% set aside time for staff to learn it; 97% of UK organisations report at least one significant AI skills gap.

4. **Britain's Workforce Is Not Ready for What Is Coming** (British Chambers of Commerce, April 2026)
   https://www.britishchambers.org.uk/news/2026/04/britains-workforce-is-not-ready-for-what-is-coming/
   Publisher: British Chambers of Commerce.
   Supports: only 21% of UK adults can explain AI in any meaningful detail; only 1 in 5 people in work feel confident using AI.

5. **CIPD: AI use in the workplace - practical advice for HR professionals**
   https://www.cipd.org/en/knowledge/guides/preparing-organisation-ai-use/
   Publisher: Chartered Institute of Personnel and Development (CIPD).
   Supports: 61% of UK organisations allow employees to use generative AI for work tasks; a quarter (25%) don't allow it and have no plans to; generative AI enabled in 73% of public sector organisations vs 57% private sector and 62% third sector; 31% of employers have worked on a generative AI policy in the past 12 months, up from 16% previously.

6. **ICO: Personal data breaches - a guide**
   https://ico.org.uk/for-organisations/report-a-breach/personal-data-breach/personal-data-breaches-a-guide/
   Publisher: Information Commissioner's Office.
   Supports: definition of a personal data breach as unauthorised access to, or disclosure of, personal data; the requirement to report a breach likely to risk individuals' rights to the ICO within 72 hours where feasible.

7. **ICO: Putting an AI policy in place - what this means for employers and employees**
   https://ico.org.uk/media2/uism0uia/ai-data-protection-and-the-public-sector-session-4-ai-policies.pdf
   Publisher: Information Commissioner's Office (AI, data protection and the public sector guidance series).
   Supports: the role of a written AI use policy in achieving UK GDPR compliance, and the requirement for a Data Protection Impact Assessment (DPIA) for high-risk AI processing.

8. **Labour market overview, UK: September 2026**
   https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/bulletins/uklabourmarket/september2026
   Publisher: Office for National Statistics.
   Supports: 34.48 million people aged 16+ in UK employment, May to July 2026. Used as the denominator for the Tom & Co original calculation (see stat_bank_update.json).

## Original calculation (Layer 2)

**Tom & Co analysis of Deloitte and ONS data, September 2026**: combines Deloitte's shadow-AI usage rate (63% x 31% = 19.5% of UK workers) with ONS's UK employment total (34.48 million, May-July 2026) to estimate approximately 6.7 million UK workers routinely use unsanctioned AI tools at work. Full workings in `stat_bank_update.json`.

## Note on research method for this run

WebFetch (direct page retrieval) was blocked by this session's network egress policy for every domain tested, including gov.uk, ons.gov.uk, ico.org.uk, britishchambers.org.uk and even non-UK domains such as arxiv.org and example.com. All research for this article was therefore conducted via WebSearch, which returns synthesised summaries of primary-source pages together with their URLs. Every URL cited above points to the primary source itself. Figures were cross-checked against multiple independent search queries where possible, but a human reviewer should ideally confirm exact wording against the live pages before publish, given the inability to fetch them directly in this session.
