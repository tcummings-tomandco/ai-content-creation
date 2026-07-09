# Sources: Which AI use cases pay back within a year for a UK business?

Topic ID: 3 | Cluster: Strategy & ROI | Priority: P1 (quick win) | Accessed: 2026-07-09

1. **Made Smarter — "First wave of South East manufacturers geared for growth with Made Smarter"**
   URL: https://www.madesmarter.uk/resources/news-first-wave-of-south-east-manufacturers-geared-for-growth-with-made-smarter/
   Publisher: Made Smarter (Innovate UK / DBT-backed UK manufacturing adoption programme)
   Claim supported: Nordell (Worthing plastics injection moulding manufacturer) secured Made Smarter South East grant funding towards AI-powered invoice processing software expected to save more than 60 hours of administration every month.

2. **Office for National Statistics — "Employee earnings in the UK: 2025" (Annual Survey of Hours and Earnings, ASHE 2025)**
   URL: https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2025
   Publisher: Office for National Statistics
   Claim supported: Median hourly pay for full-time employees in administrative and secretarial occupations, used as the wage basis for the Tom & Co Layer 2 calculation of the sterling value of Nordell's reported time saving.

3. **Made Smarter Innovation — "The Digital Spare Parts Supply Chain (DSPSC)"**
   URL: https://www.madesmarter.uk/resources/innovation-case-study-the-digital-spare-parts-supply-chain-dspsc/
   Publisher: Made Smarter Innovation (Innovate UK-funded challenge, project partners NBT Group, Senseye Ltd, Northumbria University)
   Claim supported: AI-driven predictive maintenance and stock management, connecting Senseye's predictive maintenance software to NBT Group's stock management system, was modelled to save in the region of £40m on a single large manufacturing site.

4. **McKinsey & Company (QuantumBlack) — "The state of AI: How organizations are rewiring to capture value"**
   URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
   Publisher: McKinsey & Company
   Claim supported: A reported 10-20% cost reduction specifically in software engineering, IT and manufacturing functions among organisations that have scaled AI use. Basis for the existing Tom & Co stat_bank calculation (stat_008) converting this to £4,500-£9,000 saved per UK employee per year.

5. **Department for Science, Innovation and Technology (DSIT), with IFF Research and Technopolis Group — "AI Adoption Research"**
   URL: https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research
   Publisher: DSIT (fieldwork 12 February to 2 May 2025; published 28 January 2026, updated 13 February 2026; 3,500 business interviews)
   Claim supported: 16% of UK businesses currently use at least one AI technology; among adopters, text generation/NLP is used by 85%, the most common application.

6. **British Chambers of Commerce and University of Essex — SME AI adoption survey, March 2026**
   URL: https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
   Publisher: British Chambers of Commerce
   Claim supported: AI adoption reached 54% of UK firms by March 2026, up from 23% in 2023.

## Tom & Co original calculation (Layer 2, this article)

**Sterling value of Nordell's reported AI invoice-processing time saving**, using ONS ASHE 2025 median admin/secretarial pay, loaded for employer National Insurance and minimum auto-enrolment pension. Full workings in `stat_bank_update.json` in this folder. Result: approximately £12,200 a year in reclaimed staff time from 60 hours/month, before any software subscription cost.

## Reused from stat_bank.json (no new entry required)

- `stat_008` — McKinsey State of AI 10-20% cost reduction converted to £4,500-£9,000 per UK employee per year (software engineering, IT, manufacturing). First used in `ai-roi-uk-business-2026-what-the-evidence-actually-shows`; reused here with the same attribution.
