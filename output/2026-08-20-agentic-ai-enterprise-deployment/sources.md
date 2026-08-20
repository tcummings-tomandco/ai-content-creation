# Sources: What is agentic AI and how do enterprises deploy it?

Topic ID: 12 | Cluster: Operations & Efficiency | Priority: P1 | Accessed: 2026-08-20

1. **Office for National Statistics** — [Business insights and impact on the UK economy, 8 January 2026 bulletin](https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/bulletins/businessinsightsandimpactontheukeconomy/8january2026)
   Accessed: 2026-08-20. Supports: 44% of UK businesses with 250 or more staff use AI in some form. Basis (with source 2) for the reused Tom & Co calculation already in `data/stat_bank.json` (stat_005).

2. **Department for Science, Innovation and Technology (DSIT)** — [AI Adoption Research](https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research)
   Accessed: 2026-08-20. Published: 13 February 2026 (survey fieldwork 12 Feb-2 May 2025). Supports: agentic AI is used by 7% of AI-adopting UK businesses, the least-adopted AI category tracked.

3. **UK Government (DSIT)** — [Top British AI expertise to help spark renewal of public services and bolster national security](https://www.gov.uk/government/news/top-british-ai-expertise-to-help-spark-renewal-of-public-services-and-bolster-national-security)
   Accessed: 2026-08-20. Supports: the GOV.UK Agentic AI Companion project, Anthropic selected to build it, the "Scan, Pilot, Scale" framework, the 2025/26 pilot scope (employment, education, career guidance for 16-34 year olds) and the 2026/27 scale target.

4. **BT (company newsroom)** — [BT Business collaborates with Accenture to supercharge AI deployment](https://newsroom.bt.com/bt-business-collaborates-with-accenture-to-supercharge-ai-deployment/)
   Accessed: 2026-08-20. Supports: BT's AI-Ops programme with Accenture and ServiceNow, agentic self-healing network and security operations under human-set controls, and the roughly two-year timeline to full agentic embedding.
   Note: BT's own official newsroom, the primary source for a claim about BT's own programme. Not on the checklist's literal domain list; flagged here per the same judgement-call convention used for company-published primary announcements in earlier articles.

5. **Lloyds Banking Group (company site)** — [2026: The year of Agentic AI, and a new era for finance](https://www.lloydsbankinggroup.com/insights/2026-the-year-of-agentic-ai-and-a-new-era-for-finance.html)
   Accessed: 2026-08-20. Supports: Lloyds' agentic financial assistant live across 21 million-plus customer accounts from early 2026, and plans to extend it into mortgages, vehicle finance and insurance.
   Note: same judgement call as source 4 — the bank's own primary statement about its own deployment.

6. **NHS England** — [500,000 NHS staff to get new artificial intelligence tools to help free up more time for patients](https://www.england.nhs.uk/2026/06/500000-nhs-staff-to-get-new-artificial-intelligence-tools-to-help-free-up-more-time-for-patients/)
   Accessed: 2026-08-20. Supports: the Microsoft 365 Copilot trial across 90 organisations and 30,000+ staff, averaging at least 43 minutes saved per person per day. Basis for the new Tom & Co calculation (see `stat_bank_update.json`).

7. **NHS England** — [NHS accelerates artificial intelligence rollout to cut waiting times and improve care for millions](https://www.england.nhs.uk/2026/07/nhs-accelerates-artificial-intelligence-rollout-to-cut-waiting-times-and-improve-care-for-millions/)
   Accessed: 2026-08-20. Supports: Copilot Studio letting NHS teams build their own agents for bed management, discharge planning and rota scheduling, governed via Agent 365, and the 500,000-staff rollout target for October 2026.
   Note: england.nhs.uk is NHS England's own official site. The checklist's domain list names "nhs.uk"; this is the equivalent official NHS England subdomain, flagged as a judgement call rather than assumed.

8. **The Grocer (trade press)** — [Ocado to ramp up use of 'game-changing' AI to improve shopper experience](https://www.thegrocer.co.uk/news/ocado-to-ramp-up-use-of-game-changing-ai-to-improve-shopper-experience/715759.article)
   Accessed: 2026-08-20. Published: 26 February 2026. Supports: Ocado's agentic AI chatbot trial, initially to around 10% of website users.
   Note: established UK grocery trade press, comparable in kind to computerweekly.com/marketingweek.com on the approved list, but not itself named on it. Flagged as a judgement call; no Ocado-published primary release was found covering this specific feature.

9. **Bank of England** — [Artificial intelligence in UK financial services 2024](https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024)
   Accessed: 2026-08-20. Third joint Bank of England/FCA AI survey, data collected 2024, published 21 November 2024. Supports: 55% of AI use cases in UK financial services involve some form of autonomous decision-making, only 2% are fully autonomous, and both regulators expect agentic AI to move into core decisions such as credit underwriting and portfolio management, with the Financial Policy Committee tasking further work on agentic AI in payments and markets.

10. **Information Commissioner's Office (ICO)** — [Guidance on AI and data protection](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/)
    Accessed: 2026-08-20. Supports: a decision with a legal or similarly significant effect on a person still needs a lawful basis and, in most cases, meaningful human review under UK GDPR, regardless of whether an AI agent is involved.

## Gartner (context stat, not a UK primary source)

Gartner's forecast that over 40% of agentic AI projects will be cancelled by the end of 2027 (cited for the governance section) is reused from the same figure already cited, with full attribution, in `output/2026-07-01-agentic-ai-use-cases-mid-market`. Included as global context alongside UK-primary data, consistent with that article's precedent; not counted toward the UK-primary citation total above.

## Tom & Co original calculation (Layer 2, new this run)

**Claim:** Scaling NHS England's own 43-minutes-a-day Copilot time-saving across the 500,000 staff targeted for the full rollout, over a standard 220-day NHS working year, comes to roughly 79 million hours of staff time a year.

**Method and sources:** see `stat_bank_update.json` for the full entry appended to `data/stat_bank.json` (id `stat_020`).

## Reused Tom & Co calculation (Layer 2, already in the bank)

`stat_005` (44% of UK firms with 250+ staff use AI, per ONS BICS, multiplied by DSIT's 7% agentic-AI share among adopters, giving roughly 3% of UK enterprises actually running agentic AI) was already in `data/stat_bank.json` from an earlier article and is cited here again as supporting context. No new entry needed for this figure.
