# Sources: What is MCP and how does it change enterprise AI integration?

1. **Anthropic — "Donating the Model Context Protocol and establishing the Agentic AI Foundation"**
   https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
   Accessed: 2026-08-06
   Supports: Anthropic released MCP as an open standard in November 2024, and in 2026 donated its stewardship to the newly formed Agentic AI Foundation under the Linux Foundation.

2. **Model Context Protocol maintainers — "2026-07-28 specification update"** (blog.modelcontextprotocol.io, 28 July 2026)
   https://blog.modelcontextprotocol.io/posts/2026-07-28/
   Accessed: 2026-08-06
   Supports: the July 2026 spec update moved MCP's HTTP transport to a stateless request/response model, added OAuth 2.1 with RFC 9207 issuer validation, and reported close to half a billion downloads a month across MCP's main SDKs, with the TypeScript and Python SDKs each passing one billion downloads in total.

3. **Office for National Statistics — "Artificial intelligence in UK businesses: 2023 to 2026"**
   https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/articles/artificialintelligenceinukbusinesses/2023to2026
   Accessed: 2026-08-06
   Supports: 29% of UK businesses reported using at least one AI technology in June 2026, an increase of eight percentage points on the year; among businesses with 250 or more staff the figure was 49%, up 13 percentage points on the year.

4. **techUK — "UK Tech in 2025 and what comes next for 2026"**
   https://www.techuk.org/resource/uk-tech-in-2025-and-what-comes-next-for-2026.html
   Accessed: 2026-08-06
   Supports: 2025 was the year enterprise integration had to catch up with generative AI hype; agentic AI risks becoming a "side project" without real integration into existing systems; low-code and no-code integration tooling is pulling integration work toward business users, a trend expected to continue into 2026.

5. **Financial Conduct Authority — "Rethinking regulation for the age of AI"** (speech by Nikhil Rathi, Chief Executive, 24 June 2026)
   https://www.fca.org.uk/news/speeches/rethinking-regulation-age-ai
   Accessed: 2026-08-06
   Supports: more than 80% of financial services firms are already using or adopting AI; audit trails and human oversight remain live, unresolved regulatory questions.

6. **Computer Weekly — "Bank of England's large IT spend partly due to use of manual processes and legacy systems"**
   https://www.computerweekly.com/news/252459385/Bank-of-Englands-large-IT-spend-partly-due-to-use-of-manual-processes-and-legacy-systems
   Accessed: 2026-08-06
   Supports: the Bank of England's IT spend has been inflated by manual processes and legacy systems; integrating the Prudential Regulation Authority's applications duplicated work that added to integration cost.

7. **Government Digital Service — "Our roadmap for modern digital government"** (gds.blog.gov.uk, 20 January 2026)
   https://gds.blog.gov.uk/2026/01/20/our-roadmap-for-modern-digital-government/
   Accessed: 2026-08-06
   Supports: the six-point plan for modern digital government calls for public services to adopt a standard set of APIs and events for new services.

## Original Tom & Co calculation (Layer 2)

**86% fewer integrations to build: 15 MCP server connections vs 105 point-to-point connections, for a 15-system enterprise stack.**

Workings: applying the standard integration-complexity formula (N systems needing full pairwise connectivity require N(N-1)/2 point-to-point connections, vs N connections through a hub) to a stated worked example of N=15: 15 x 14 / 2 = 105 point-to-point connections, vs 15 MCP server connections. (105-15)/105 = 86% fewer. Full workings recorded in `stat_bank_update.json`.

Caveat: 15 is a stated illustrative assumption for a worked example, not a claimed average number of systems across UK enterprises. The formula itself (M x N collapsing to M + N) is standard integration-architecture reasoning also used in MCP's own documentation to explain the protocol's purpose; the worked arithmetic applying it to a concrete number is the original contribution here.

## Sources considered and not used

A secondary-source claim that 75% of API gateway vendors and 50% of iPaaS vendors will natively support MCP by the end of 2026, attributed to Gartner via several AI-industry blogs, was reviewed and left out of the article. Gartner is not on the approved primary-source list for this engine, and the underlying Gartner publication itself could not be located and verified within this research pass, only secondary paraphrases of it. Governance detail about the Agentic AI Foundation's Platinum members (Linux Foundation press release, PR Newswire) was also reviewed but not cited directly, since neither linuxfoundation.org nor prnewswire.com is on the approved domain list; the equivalent facts needed for the article (Anthropic donating MCP, the 2026 timing) are instead sourced to Anthropic's own announcement.
