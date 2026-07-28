# Sources: How do you rank in ChatGPT in 2026?

1. **Profound — "How ChatGPT sources the web"** (analysis of 700,000+ ChatGPT conversations, Q4 2025)
   https://www.tryprofound.com/blog/chatgpt-citation-sources
   Accessed: 2026-07-28
   Supports: ~18% of ChatGPT conversations trigger at least one live web search; Wikipedia present in roughly 1 in 6 cited conversations; earlier conversation turns are markedly more likely to trigger citations than later ones.

2. **Profound — "AI Platform Citation Patterns: How ChatGPT, Google AI Overviews, and Perplexity Source Information"**
   https://www.tryprofound.com/blog/ai-platform-citation-patterns
   Accessed: 2026-07-28
   Supports: 87% of ChatGPT citations match Bing's top organic results; ChatGPT's citation ranking weighs domain authority at roughly 40%, content quality at 35%, and platform trust at 25%; 3 to 6 clickable citations returned per response.

3. **OpenAI Developer Platform — "Overview of OpenAI Crawlers"**
   https://developers.openai.com/api/docs/bots
   Accessed: 2026-07-28
   Supports: OpenAI operates three independently controllable crawlers, GPTBot (model training), OAI-SearchBot (ChatGPT search indexing), and ChatGPT-User (on-demand link fetches), each of which can be allowed or disallowed separately in robots.txt.

4. **Ofcom — "From apps to AI search: how the UK goes online in 2025"**
   https://www.ofcom.org.uk/media-use-and-attitudes/online-habits/from-apps-to-ai-search-how-the-uk-goes-online-in-2025
   Accessed: 2026-07-28
   Supports: ChatGPT recorded 1.8 billion UK web visits across the first eight months of 2025, up from 368 million in the same period of 2024; roughly 30% of UK Google searches now trigger an AI-generated summary. Base input for the Tom & Co Layer 2 growth-multiple calculation (see stat_bank_update.json).

5. **Ofcom — "Adults' Media Use and Attitudes 2026"**
   https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/media-literacy-research/adults/adults-media-use-and-attitudes-2026/adults-media-use-and-attitudes-2026-report.pdf
   Accessed: 2026-07-28
   Supports: 54% of UK adults now use an AI tool such as ChatGPT, Copilot or Gemini, up from 31% a year earlier.

6. **British Chambers of Commerce and University of Essex (with Atos) — "Half of SMEs using AI, with limited headcount impact so far"** (March 2026)
   https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
   Accessed: 2026-07-28
   Supports: 54% of UK SMEs use AI in some form, up from 35% in 2025.

7. **Aggarwal et al. — "GEO: Generative Engine Optimization"** (Princeton University, presented at ACM SIGKDD 2024)
   https://arxiv.org/abs/2311.09735
   Accessed: 2026-07-28
   Supports: adding a quotation from a credible source lifts citation likelihood by up to 40%; adding a specific, dated statistic lifts citation rates by roughly 37%.

## Original Tom & Co calculation (Layer 2)

**UK visits to ChatGPT grew by roughly 4.9 times between the first eight months of 2024 and the same period in 2025.**

Workings: Ofcom's "From apps to AI search" report (source 4) states ChatGPT recorded 1.8 billion UK web visits in the first eight months of 2025, up from 368 million in the same period of 2024. Growth multiple: 1,800,000,000 / 368,000,000 = 4.891..., rounded to "roughly 4.9 times" (equivalent to approximately 389% growth). Ofcom's page states the two absolute totals but does not itself publish the growth multiple or percentage; the multiple is Tom & Co's derivation from the reported figures. Full workings also recorded in `stat_bank_update.json`.

Caveat: Ofcom's own methodology note for the underlying web-visit measurement was not independently re-verified beyond what the published page states; the calculation assumes both eight-month totals were measured on a consistent basis.

## Sources considered and not used

Numerous SEO-agency and GEO-tool-vendor blogs (Seer Interactive, Anagram, Wellows, Mentionable, Trakkr and others) surfaced specific-sounding figures during research, including a widely repeated "87% Bing citation match" claim and third-party pricing estimates for AI-visibility tracking tools. Where the same finding traced back to Profound's own published research, Profound was cited directly instead. Where a figure (e.g. specific third-party pricing tiers for paid AI-visibility trackers) could not be traced to a primary, disclosed-methodology source, it was left out of the article and out of the tools comparison table rather than repeated on an agency blog's authority.
