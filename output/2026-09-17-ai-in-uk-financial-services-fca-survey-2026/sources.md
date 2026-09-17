# Sources: How are UK financial services firms actually using AI in 2026?

Accessed: 2026-09-17

---

## Primary citations (inline in article)

### 1. Bank of England & FCA — Artificial intelligence in UK financial services - 2024
- **URL**: https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024
- **Publisher**: Bank of England and Financial Conduct Authority (third joint survey, published 21 November 2024)
- **Claim supported**: 75% of UK financial services firms already using AI (10% more planning to within 3 years), up from 58%/14% in 2022; survey of 118 firms across six sectors; foundation models = 17% of use cases; third-party implementations = one third of use cases; 12% of foundation-model use cases and 16% of third-party use cases rated "high materiality"; cybersecurity is the top perceived systemic risk now and in three years, with third-party dependency causing the largest projected increase in risk; 34% "complete understanding" / 46% "partial understanding" of the AI firms use; 84% have an accountable person for their AI framework, 72% say executive leadership is accountable.
- **Accessed**: 2026-09-17

### 2. Bank of England — Artificial Intelligence Consortium minutes, 2 May 2025
- **URL**: https://www.bankofengland.co.uk/minutes/2025/may/ai-consortium-minutes-2-may-2025
- **Publisher**: Bank of England
- **Claim supported**: The Artificial Intelligence Consortium, co-chaired by the Bank of England and FCA, was established on 2 May 2025 as a standing forum for public-private dialogue on AI in UK financial services, meeting quarterly.
- **Accessed**: 2026-09-17

### 3. Bank of England (PRA) — SS1/23: Model risk management principles for banks
- **URL**: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- **Publisher**: Prudential Regulation Authority / Bank of England
- **Claim supported**: SS1/23's five model risk management principles (identification and classification, governance, development/implementation/use, independent validation, mitigants) came into force on 17 May 2024 and explicitly apply to AI and machine learning models across a firm's full operations, not just credit and market risk.
- **Accessed**: 2026-09-17

### 4. FCA — AI Sprint summary
- **URL**: https://www.fca.org.uk/publications/techsprints/ai-sprint-summary
- **Publisher**: Financial Conduct Authority
- **Claim supported**: The FCA's two-day AI Sprint (29-30 January 2025) brought together 115 participants from industry, academia, regulators and consumer groups; findings pointed to more consumer personalisation, more internal automation, agentic AI, and risks (algorithmic collusion, transparency) that existing principles-based regulation was judged to largely already cover.
- **Accessed**: 2026-09-17

### 5. FCA — AI Lab
- **URL**: https://www.fca.org.uk/firms/innovation/ai-lab
- **Publisher**: Financial Conduct Authority
- **Claim supported**: The FCA's advanced AI sandbox programme (a five-month, GPU-backed cohort programme) selected 23 firms from 132 applications for its first cohort (showcase 28-29 January 2026); the second cohort's showcase is scheduled for 26 November 2026, built with Anthropic's Claude tools.
- **Accessed**: 2026-09-17

### 6. FCA — FCA announces second cohort for AI Live Testing
- **URL**: https://www.fca.org.uk/news/press-releases/fca-announces-second-cohort-ai-live-testing
- **Publisher**: Financial Conduct Authority
- **Claim supported**: Applications for the second AI Live Testing cohort ran 19 January to 24 March 2026; eight firms were selected (Barclays, Experian, Lloyds Banking Group/Scottish Widows, UBS, Aereve, Coadjute, GoCardless, Palindrome); testing started from late April 2026 and runs to the end of 2026, with evaluation due Q1 2027.
- **Accessed**: 2026-09-17

### 7. FCA — Consumer Duty
- **URL**: https://www.fca.org.uk/firms/consumer-duty
- **Publisher**: Financial Conduct Authority
- **Claim supported**: The Consumer Duty's four outcomes (product governance, price and value, consumer understanding, consumer support) apply to any AI-driven decision that touches a retail customer, regardless of which tool produced it.
- **Accessed**: 2026-09-17

### 8. FCA — Senior Managers & Certification Regime
- **URL**: https://www.fca.org.uk/firms/senior-managers-certification-regime
- **Publisher**: Financial Conduct Authority
- **Claim supported**: SM&CR requires firms to identify the senior manager accountable for each area of the business, including AI use cases, mirroring the survey's finding that 84% of firms already name an accountable person for their AI framework.
- **Accessed**: 2026-09-17

---

## Layer 2 original calculation (Tom & Co analysis)

**Claim**: Only around 2% of all AI use cases in UK financial services are both built on a foundation model and rated high materiality by the firm running them.

**Method**: Multiplied two rates published separately in the Bank of England/FCA third survey (source 1 above): foundation models = 17% of all AI use cases; 12% of foundation-model use cases are rated "high materiality". 0.17 x 0.12 = 0.0204, approximately 2%. Full workings recorded in `stat_bank_update.json` in this folder.

**Caveat disclosed in the article**: this is a derived combination of two figures the source reports independently; the survey itself does not publish the combined share.

---

## Sources considered and excluded

- Several law-firm and consultancy commentary pieces on the third BoE/FCA survey (A&O Shearman, Lewis Silkin, Stephenson Harwood, Addleshaw Goddard, regulationtomorrow.com) were used only to triangulate and cross-check specific figures pulled from the primary survey report, since the primary Bank of England and FCA domains could not be fetched directly in this research session (network egress to bankofengland.co.uk and fca.org.uk was blocked for direct page fetches; all figures were corroborated via multiple independent secondary summaries quoting the same primary report before being cited). None of these secondary sources were cited directly in the article; every inline citation points to the primary gov/regulator URL.
- General AI-governance blogs (SureCloud, RRCompliance, airiskaware.com) were used only to confirm the general shape of FCA/PRA AI policy (existing frameworks, no bespoke AI rulebook) and were not cited as sources for any specific figure.
