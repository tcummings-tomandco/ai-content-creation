# Sources: What is GEO and how is it different from SEO?

1. **Aggarwal et al. — "GEO: Generative Engine Optimization"** (Princeton University, presented at ACM SIGKDD 2024)
   https://arxiv.org/abs/2311.09735
   Accessed: 2026-07-23
   Supports: the origin and definition of the term GEO; the finding that adding a quotation from a credible source lifts citation likelihood by up to 40%; the finding that specific statistics with units and dates lift citation rates by roughly 37%; the GEO-bench framework's scale (roughly 10,000 queries across nine domains).

2. **Ofcom — "Adults' Media Use and Attitudes 2026"**
   https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/media-literacy-research/adults/adults-media-use-and-attitudes-2026/adults-media-use-and-attitudes-2026-report.pdf
   Accessed: 2026-07-23
   Supports: 75% of UK online adults read AI-generated search summaries at least sometimes; 54% of UK adults use AI tools, up from 31% the year before. Report published 2 April 2026.

3. **British Chambers of Commerce and University of Essex (with Atos) — "Half of SMEs using AI, with limited headcount impact so far"** (March 2026)
   https://www.britishchambers.org.uk/news/2026/03/half-of-smes-using-ai-with-limited-headcount-impact-so-far/
   Accessed: 2026-07-23
   Supports: 54% of UK SMEs using AI in some form (up from 35% in 2025, 25% in 2024, 23% in 2023); marketing tied with admin as the top use case at 72% among AI-using SMEs. Base input for the Tom & Co Layer 2 calculation (see stat_bank_update.json).

4. **gov.uk (Department for Business and Trade) — "Business population estimates for the UK and regions 2024: statistical release"**
   https://www.gov.uk/government/statistics/business-population-estimates-2024/business-population-estimates-for-the-uk-and-regions-2024-statistical-release
   Accessed: 2026-07-23
   Supports: 5,499,000 UK private-sector businesses (2024 estimate). Second input for the Tom & Co Layer 2 calculation.

5. **Office for National Statistics — "Retail sales, Great Britain: March 2026"**
   https://www.ons.gov.uk/businessindustryandtrade/retailindustry/bulletins/retailsales/march2026
   Accessed: 2026-07-23
   Supports: internet sales holding at roughly 27-28% of total UK retail sales through 2026.

## Original Tom & Co calculation (Layer 2)

**Roughly 2.1 million UK businesses now use AI for marketing or content work.**

Workings: BCC/Essex/Atos (source 3) reports 54% of UK SMEs use AI in some form, and of those, 72% use it for marketing (a joint-top use case with admin). 0.54 x 0.72 = 0.3888. Applied to gov.uk's 5,499,000 UK private-sector businesses (source 4): 0.3888 x 5,499,000 = 2,138,011, rounded to "roughly 2.1 million." Full workings also recorded in `stat_bank_update.json`.

Caveat: the BCC/Essex survey samples SMEs specifically, while the gov.uk figure covers all UK private-sector businesses. SMEs make up the vast majority of that population by count, so the two are treated as broadly comparable, but this is an order-of-magnitude estimate, not an exact calculation. Neither source publishes this combined figure.

## Sources considered and not used

Several SEO-tool-vendor blog posts (searchscore.io, rank4ai.co.uk, seoworks.co.uk, limelightdigital.co.uk) surfaced specific-sounding UK "AI search traffic" statistics during research (e.g. precise monthly shopping-intent visit counts from chat platforms). None disclosed a checkable methodology or linked back to a primary dataset, so none were cited in the article body, consistent with the rule against undated or unsourced agency-blog claims. Ofcom and ONS data were used instead wherever the same underlying phenomenon (AI search behaviour, online retail share) needed a citation.
