# Sources: How much should a UK SME budget for AI in 2026?

Accessed: 2026-07-14

---

## 1. British Chambers of Commerce and University of Essex: Half of SMEs Using AI, With Limited Headcount Impact So Far (March 2026)

**URL:** https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
**Publisher:** British Chambers of Commerce, in partnership with the University of Essex (ISER) and Atos. Survey of 668 UK businesses (94% SMEs).
**Claim supported:** 54% of UK firms are now using AI in some form. Used for context in the "three layers" definition section.

---

## 2. McKinsey & Company: The state of AI: How organizations are rewiring to capture value

**URL:** https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
**Publisher:** McKinsey & Company (QuantumBlack), named research firm with disclosed survey methodology
**Claim supported:** The enablement cost of AI (time spent adapting workflows) frequently exceeds the licence fee for organisations that do not redesign the process around the tool. Used for the "enablement" layer of the budget definition.

---

## 3. ONS: Employee earnings in the UK: 2025 (ASHE 2025 provisional results)

**URL:** https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/earningsandworkinghours/bulletins/annualsurveyofhoursandearnings/2025
**Publisher:** Office for National Statistics
**Claim supported:** Median gross annual earnings for a full-time employee in post at least a year, April 2025, were £39,039. Used as the base salary for the fully loaded £25.06/hour and £45,100/year (per person) figures used throughout the article, including the £451,000 payroll comparison for a 10-person team.

---

## 4. GOV.UK: Rates and thresholds for employers 2026 to 2027

**URL:** https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027
**Publisher:** HM Revenue & Customs
**Claim supported:** Employer National Insurance at 15% above the £5,000 secondary threshold, used with the ONS salary figure to build the fully loaded employee cost.

---

## 5. GOV.UK: AI Adoption Research

**URL:** https://www.gov.uk/government/publications/ai-adoption-research/ai-adoption-research
**Publisher:** Department for Science, Innovation and Technology (DSIT), fieldwork by IFF Research and Technopolis Group, 12 February to 2 May 2025 (Computer Assisted Telephone Interviewing)
**Claim supported:** 65% of organisations anticipate increasing their AI-related budgets, rising to 82% among large businesses. Planned investment focuses on off-the-shelf AI applications (65%) and embedding AI into existing systems (59%) rather than bespoke development.

---

## 6. ICO: Data Protection Impact Assessments (DPIAs)

**URL:** https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/
**Publisher:** Information Commissioner's Office
**Claim supported:** The ICO does not charge a fee for a DPIA; a DPIA "does not have to be complex or time-consuming in every case", scaled to the actual privacy risk; where high residual risk remains, the ICO must be consulted before processing starts, with a service standard of up to six weeks to respond (extendable by a further month for complex cases).

---

## 7. EU AI Act penalty tiers (via Tom & Co's existing stat_002 calculation)

**URL:** https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99 ; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689
**Publisher:** European Commission EU AI Act Service Desk; Official Journal of the European Union
**Claim supported:** The roughly £420 million break-even turnover figure (above which the fixed euro cap rather than the percentage cap applies) is Tom & Co's existing Layer 2 calculation, first published in `does-the-eu-ai-act-apply-to-my-uk-business` and stored as `stat_002` in `data/stat_bank.json`. Reused here (Layer 1 reuse of an existing Tom & Co stat) rather than recalculated. The Act's obligations apply in full from 2 August 2026 per the Act's own text.

---

## 8. Innovate UK: BridgeAI programme

**URL:** https://www.gov.uk/government/organisations/innovate-uk ; https://iuk-business-connect.org.uk/programme/bridgeai/
**Publisher:** Innovate UK (UKRI)
**Claim supported:** BridgeAI is a £100 million programme running January 2023 to June 2026, targeting UK SMEs in transport, construction, agriculture and food processing, and the creative industries, with grants of up to £200,000 available for approved five-month projects through its Innovation Exchange strand.

---

## Vendor pricing (factual reference, not a claim of evidence)

- Microsoft 365 Copilot pricing (UK): https://www.microsoft.com/en-us/microsoft-365-copilot/pricing
- ChatGPT Business pricing: https://openai.com/business/chatgpt-pricing/
- Claude Team pricing: https://claude.com/pricing
- GitHub Copilot pricing ($19/user/month, Business tier): https://github.com/features/copilot/plans
- GBP/USD exchange rate reference ($1 = £0.75, used throughout for $ to £ conversions, July 2026): https://www.poundsterlinglive.com/history/GBP-USD-2026

---

## Tom & Co Layer 2 calculation (Recipe A/D hybrid) — see stat_bank_update.json for the full entry

**Stat:** Blended annual AI tooling budget range for a 10-seat UK team across five commonly cited subscription tiers.
**Value:** £1,710 to £9,000 per year.
**Workings:** Per-seat monthly prices for GitHub Copilot Business ($19), ChatGPT Business ($20), Claude Team Standard ($20), Microsoft 365 Copilot (£30) and Claude Team Premium ($100), converted at $1 = £0.75 where needed, multiplied by 10 seats and 12 months. Range: £1,710 (GitHub Copilot Business, lowest) to £9,000 (Claude Team Premium, highest).
**Cited in article as:** "Tom & Co analysis: blending the cheapest and priciest of these five tiers across a 10-seat team gives a core AI tooling budget of £1,710 to £9,000 a year..."

---

## Sources considered and rejected

- Several SEO aggregator articles claiming specific EU AI Act SME compliance cost figures (e.g. "€20,000-€50,000 initial investment" for deployers) were found but not used inline, since none traced to a disclosed-methodology primary source (European Commission impact assessment or a named research firm survey). The article instead relies on Tom & Co's own existing, disclosed EU AI Act penalty-tier calculation (stat_002) for the compliance-cost framing.
- A search-engine-synthesised claim that UK SME AI spend averages "£2-8 million annually" (attributed to DSIT's AI Adoption Research) could not be verified against the source document (which returned HTTP 403 on direct fetch) and is implausible on its face for typical SME-scale spend. Not used.
- A claimed UK AI market forecast of "£18.2 billion (2025) to £31.4 billion (2028)" could not be traced to any primary source on a follow-up search. Not used.
- An unverified "£73.8 million in BridgeAI grant funding to 3,400+ organisations" figure appeared once in an early search but could not be corroborated on a second, independent search. The article uses only the doubly-corroborated £100 million total programme figure and the £200,000 per-project Innovation Exchange grant cap instead.
