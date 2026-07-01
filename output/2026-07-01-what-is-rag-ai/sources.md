# Sources: What is RAG (retrieval-augmented generation) in plain English?

Slug: what-is-rag-ai | Date: 2026-07-01 | Cluster: Technical & Build | Format: Definition + comparison table

All inline citations resolve to primary research, vendor technical documentation, peer-reviewed publication, or UK official statistics. No agency blogs, listicles, or undated reports are cited.

## Inline citations

1. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** (Lewis, Perez, Piktus, Petroni, Karpukhin, Goyal, Küttler, M. Lewis, Yih, Rocktäschel, Riedel, Kiela)
   - URL: https://arxiv.org/abs/2005.11401
   - Publisher: arXiv (preprint), accepted at NeurIPS 2020
   - Submitted: 22 May 2020
   - Accessed: 2026-07-01
   - Supports: the origin and definition of RAG; the claim that RAG "set the state-of-the-art on three open domain QA tasks" and generated "more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline". Direct quotes taken from the paper abstract.

2. **What is RAG (Retrieval-Augmented Generation)?** — AWS
   - URL: https://aws.amazon.com/what-is/retrieval-augmented-generation/
   - Publisher: Amazon Web Services (vendor technical documentation)
   - Accessed: 2026-07-01
   - Supports: the four-stage how-it-works description (create/prepare external data as embeddings in a vector database; retrieve relevant information via query embedding match; augment the prompt; generate the answer). Also supports the benefits framing (cost vs retraining, current information, source citations, reduced hallucination).

3. **Hallucination Mitigation for Retrieval-Augmented Large Language Models: A Review** (2025)
   - URL: https://www.mdpi.com/2227-7390/13/5/856
   - Publisher: Mathematics (MDPI), peer-reviewed journal, Vol 13, Issue 5, article 856
   - Accessed: 2026-07-01
   - Supports: the claim that grounding responses in retrieved evidence is the leading practical method for reducing the rate at which language models fabricate facts, and the "reduces but does not eliminate" framing.

4. **Business insights and impact on the UK economy: 8 January 2026** — ONS Business Insights and Conditions Survey (BICS)
   - URL: https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/bulletins/businessinsightsandimpactontheukeconomy/8january2026
   - Publisher: Office for National Statistics
   - Measurement period: late December 2025 (with September 2023 baseline)
   - Accessed: 2026-07-01
   - Supports: 25% of UK businesses reported using some form of AI in late December 2025; up 15 percentage points from the ~10% recorded when the question was first introduced in late September 2023; 44% for businesses with 250+ employees. Underpins the Layer 2 adoption-velocity calculation.

5. **Guidance on AI and data protection** — Information Commissioner's Office (ICO)
   - URL: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/
   - Publisher: ICO (UK regulator)
   - Accessed: 2026-07-01
   - Supports: the UK-regulatory angle that automated outputs must be explainable and documentable, and that a data protection impact assessment is expected where AI processes personal data at scale. Used to anchor the "answers you can audit" and "sensitive/proprietary data" points.

## Layer 2 original calculation (Tom & Co analysis)

**Stat:** UK AI adoption velocity, September 2023 to December 2025 = approximately 6.7 percentage points per year.

**Method:** Recipe C (year-on-year delta from official snapshots).

**Workings:**
- ONS BICS baseline: ~10% of UK businesses using some form of AI when the question was introduced in late September 2023 (the 8 January 2026 bulletin states the December 2025 figure is "up 15 percentage points since the question was first introduced in late September 2023", implying a ~10% baseline).
- ONS BICS latest: 25% of UK businesses using some form of AI in late December 2025.
- Change: 25% − 10% = 15 percentage points.
- Elapsed time: late September 2023 to late December 2025 = approximately 27 months = 2.25 years.
- Velocity: 15pp / 2.25 years = 6.67pp per year, reported as roughly 6.7 percentage points per year.
- Attribution used inline: "Tom & Co analysis of the ONS 2023 and 2025 figures."

**Note:** This entry is NOT written back to data/stat_bank.json by this subagent, per the ad-hoc batch instructions (do not edit files outside the output folder). The central process should append it to the stat bank if it wishes to reuse the calculation. Suggested stat bank entry:

```json
{
  "id": "stat_005",
  "stat": "UK AI adoption velocity across all businesses, Sept 2023 to Dec 2025",
  "value": "6.7",
  "unit": "percentage points per year",
  "date_calculated": "2026-07-01",
  "applies_to": ["topic: what-is-rag-ai", "clusters: Technical & Build; Strategy & ROI"],
  "method": "Recipe C — year-on-year delta from ONS BICS snapshots",
  "sources_used": [
    {"title": "Business insights and impact on the UK economy: 8 January 2026", "url": "https://www.ons.gov.uk/businessindustryandtrade/business/businessservices/bulletins/businessinsightsandimpactontheukeconomy/8january2026", "publisher": "Office for National Statistics", "accessed": "2026-07-01"}
  ],
  "workings": "25% (Dec 2025) minus ~10% (Sept 2023 baseline, implied by the bulletin's '+15pp since introduced') = 15pp over ~27 months (2.25 years) = 6.67pp/year, reported as ~6.7pp/year.",
  "first_used_in": "what-is-rag-ai",
  "first_used_date": "2026-07-01",
  "layer": 2
}
```

## Sources reviewed but not cited

- IBM, "RAG vs fine-tuning vs. prompt engineering" (https://www.ibm.com/think/topics/rag-vs-fine-tuning-vs-prompt-engineering) — used to sense-check the comparison-table framing (prompting = how you ask, RAG = what the model sees, fine-tuning = how it behaves; and the layered start-with-prompts-then-RAG-then-fine-tune order). Not cited inline because the table content is standard and the primary/vendor sources above already carry the load; returned HTTP 403 on direct fetch.
- Google Cloud RAG use-case page — page content truncated on fetch; not cited.
