# Sources: Copilot or ChatGPT Enterprise: which is right for your UK business?

Accessed: 2026-09-15

---

## Primary citations (inline in article)

### 1. ONS — Artificial intelligence in UK businesses: 2023 to 2026
- **URL**: https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/artificialintelligenceinukbusinesses/2023to2026
- **Publisher**: Office for National Statistics
- **Claim supported**: Large language models were the most widely used AI technology among UK businesses with 10 or more employees in June 2026, at 18% adoption.
- **Accessed**: 2026-09-15

### 2. Department for Business and Trade — Business population estimates for the UK and regions 2024
- **URL**: https://www.gov.uk/government/statistics/business-population-estimates-2024/business-population-estimates-for-the-uk-and-regions-2024-statistical-release
- **Publisher**: Department for Business and Trade (via GOV.UK)
- **Claim supported**: UK business counts by employment size band (approx. 211,000 businesses with 10-49 employees, 37,800 with 50-249, 8,250 with 250+), used as the population base for the Tom & Co original calculation.
- **Accessed**: 2026-09-15

### 3. ICO — Microsoft 365 Copilot privacy notice
- **URL**: https://ico.org.uk/global/privacy-notice/microsoft-365-copilot/
- **Publisher**: Information Commissioner's Office
- **Claim supported**: The ICO's own Microsoft 365 Copilot data stays within its secure UK Microsoft 365 and Azure tenancy and is not used to train foundation models.
- **Accessed**: 2026-09-15

### 4. National Cyber Security Centre — AI and cyber security: what you need to know
- **URL**: https://www.ncsc.gov.uk/guidance/ai-and-cyber-security-what-you-need-to-know
- **Publisher**: National Cyber Security Centre
- **Claim supported**: Organisations should classify their data before deciding what can go into any AI tool, rather than relying on vendor contract terms alone.
- **Accessed**: 2026-09-15

### 5. Microsoft — Microsoft 365 Copilot pricing
- **URL**: https://www.microsoft.com/en-us/microsoft-365/copilot/pricing
- **Publisher**: Microsoft
- **Claim supported**: Microsoft 365 Copilot's UK enterprise add-on price (£30/user/month) and the Business SKU price ($21/user/month, up to 300 seats), plus the licensing prerequisite of a qualifying Microsoft 365 plan.
- **Accessed**: 2026-09-15

### 6. OpenAI — Business data privacy, security, and compliance
- **URL**: https://openai.com/business-data/
- **Publisher**: OpenAI
- **Claim supported**: ChatGPT Enterprise offers in-region data residency, including a UK option, for approved advanced data controls customers.
- **Accessed**: 2026-09-15

### 7. OpenAI — ChatGPT Business pricing (via ChatGPT Business overview)
- **URL**: https://chatgpt.com/pricing/
- **Publisher**: OpenAI
- **Claim supported**: ChatGPT Business costs $20/user/month billed annually ($25 billed monthly), with a 2-seat minimum, cut from $25/$30 on 2 April 2026. ChatGPT Enterprise pricing is not published and is negotiated per contract.
- **Accessed**: 2026-09-15

---

## Layer 2 original calculation (Tom & Co analysis)

**Claim**: Approximately 46,000 UK businesses with 10 or more employees are already running a large language model day to day.

**Method**: Applied the ONS's 18% large-language-model adoption figure (source 1 above, businesses with 10+ employees, June 2026) to the Department for Business and Trade's 2024 business population estimate for the same employment size bands (source 2 above): 211,000 (10-49) + 37,800 (50-249) + 8,250 (250+) = 257,050 businesses. 257,050 x 0.18 = 46,269, rounded to approximately 46,000.

**Caveat disclosed in the article's workings**: this joins a June 2026 adoption survey to a 2024 business population count. Neither source publishes this combined total itself. Full workings recorded in `stat_bank_update.json` in this folder.

---

## Sources considered and excluded

- Multiple third-party pricing aggregator blogs (Coworker.ai, GoSearch, Velosio, justinmckelvey.com, etc.) were used only to triangulate and cross-check the vendor-published pricing figures above. None were cited directly in the article, per the skill's ban on agency blogs and content-farm sources as citations. Where their figures disagreed with what could be attributed to Microsoft's or OpenAI's own pricing pages, the vendor's own stated figure was preferred and the aggregator figure discarded (this is why the article does not state a specific ChatGPT Enterprise per-seat price: OpenAI does not publish one).
