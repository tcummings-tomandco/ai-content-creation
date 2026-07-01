# Sources: What are agentic workflows?

Slug: what-are-agentic-workflows | Date: 2026-07-01 | Cluster: Technical & Build / Tools

Every cited source below is a primary vendor document, a named research firm with disclosed methodology, a UK regulator, or an official statistics body. Accessed 2026-07-01.

## 1. Anthropic, "Building Effective Agents" (published 19 December 2024)

- URL: https://www.anthropic.com/research/building-effective-agents
- Publisher: Anthropic
- Claims it supports:
  - Definition of agentic systems, and the split into workflows vs agents.
  - Exact quoted definitions: workflows are "systems where LLMs and tools are orchestrated through predefined code paths"; agents are "systems where LLMs dynamically direct their own processes and tool usage."
  - The "augmented LLM" building block = retrieval + tools + memory.
  - The five named workflow patterns: prompt chaining, routing, parallelisation, orchestrator-workers, evaluator-optimiser.
  - The guidance to "find the simplest solution possible, and only increase complexity when needed."
- Verified: fetched directly, definitions quoted verbatim.

## 2. Gartner — task-specific AI agents in 40% of enterprise apps by 2026

- Claim: "40% of enterprise applications will feature task-specific AI agents by the end of 2026, up from less than 5% in 2025."
- Press release: "Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up from Less Than 5% in 2025" (dated 26 August 2025).
- URL: https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025
- Publisher: Gartner, Inc.
- Note: gartner.com returns HTTP 403 to automated fetch; figures corroborated across multiple search summaries quoting the release headline verbatim. Headline figure and baseline are stated in the press-release title itself.

## 3. Gartner — 40%+ of agentic AI projects cancelled by 2027

- Claim: "Over 40% of agentic AI projects will be scrapped by the end of 2027, due to escalating costs, unclear business value and inadequate risk controls."
- Source: Gartner press release, June 2025, reported by Reuters.
- URL (used in article): https://www.reuters.com/business/over-40-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says-2025-06-25/
- Original Gartner release: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- Publisher: Gartner, Inc. (Reuters used as accessible citation because gartner.com blocks automated fetch).
- Underlying data: Gartner poll of 3,412 webinar attendees, January 2025. Attributed to Anushree Verma, Senior Director Analyst, Gartner. The same release notes only ~130 of "thousands" of agentic AI vendors are genuine ("agent washing").

## 4. McKinsey, "The State of AI" (November 2025 — "Agents, innovation, and transformation")

- URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- PDF: https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf
- Publisher: McKinsey & Company (QuantumBlack)
- Claims it supports:
  - 88% of organisations use AI in at least one business function (up from 78% a year earlier).
  - 39% of organisations are experimenting with AI agents; 23% are scaling an agentic AI system somewhere in the enterprise.
- Survey window: 25 June to 29 July 2025; 1,993 participants across 105 nations.
- Note: figures verified verbatim across multiple published summaries tracing to the November 2025 report ("Twenty-three percent... are scaling an agentic AI system... with an additional 39 percent experimenting with AI agents"). The "experimenting vs scaling" gap is the article's central adoption point. mckinsey.com timed out on direct automated fetch; PDF at the URL above.

## 5. ONS, Annual Survey of Hours and Earnings (ASHE) 2024 — used for the Tom & Co calculation

- URL: https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2024
- Publisher: Office for National Statistics
- Claim it supports: a UK knowledge worker costs an employer roughly £23.80/hour once employer NI and pension are added.
- Layer 2 workings (Tom & Co analysis, reused from stat_003 in the stat bank, calculated 2026-06-25):
  - ONS ASHE 2024 median full-time weekly earnings £728 x 52 = £37,856/year gross.
  - Employer NI (13.8% above £9,100 secondary threshold): (£37,856 - £9,100) x 0.138 = £3,968.
  - Employer pension (3% minimum on qualifying earnings above £6,240): (£37,856 - £6,240) x 0.03 = £948.
  - Total employer cost: £37,856 + £3,968 + £948 = £42,772/year ≈ £42,800.
  - Hourly rate at 1,800 productive hours/year: £42,800 / 1,800 = £23.78/hour ≈ £23.80.
  - Two hours saved per person per week x 52 x £23.80 = £2,475/year ≈ over £2,400.
- Note: this reuses the existing stat_bank.json entry stat_003 rather than creating a new one. Per the ad-hoc batch rules, this subagent does not write to data/stat_bank.json.

## 6. ICO — automated decision-making and profiling guidance

- URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/automated-decision-making-and-profiling/
- Publisher: Information Commissioner's Office
- Claims it supports:
  - A "solely automated" decision with a legal or similarly significant effect (e.g. declining a mortgage, rejecting a job application) gives the individual specific rights under UK GDPR.
  - A human in the loop only counts if they have the authority and competence to change the outcome, not rubber-stamp it.
- Note: ico.org.uk returns HTTP 403 to automated fetch; content taken from the ICO's published guidance pages (individual rights + AI and data protection sub-pages) via search.

## 7. ICO — work on artificial intelligence (Data (Use and Access) Act 2025 context)

- URL: https://ico.org.uk/about-the-ico/what-we-do/our-work-on-artificial-intelligence/
- Publisher: Information Commissioner's Office
- Claims it supports:
  - The Data (Use and Access) Act 2025 replaced the old Article 22 UK GDPR with new provisions on automated decisions.
  - The ICO issued updated draft guidance on automated decision-making in March 2026.
- Note: the March 2026 draft ADM guidance is well documented in ICO consultation materials and legal commentary; cited via the ICO's own AI work hub page.
