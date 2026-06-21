# Internal link suggestions

Topic 34 — UK AI regulation in 2026: principles-based field guide

## Currently in the article (2 links)

| # | Anchor text | Destination | Rationale |
|---|---|---|---|
| 1 | Coffee & Clarity: getting the most out of AI for your business | /blog/news/are-you-really-getting-the-most-out-of-ai | Existing on-site, on-brand AI content; converts a regulator-curious reader to the AI advisory funnel. |
| 2 | Tom & Co AI agency consultancy | /ai-agency-consultancy | Pillar up-link. Conversion path. |

## Forward references (add once these articles ship)

The website's prebuild link injector (`scripts/add-internal-links-to-blog-articles.js`) can pick these up automatically once the destination articles exist. Until then, the engine should leave the article at 2 links and add these in the next refresh cycle.

| # | Suggested anchor text | Destination (when published) | Roadmap topic |
|---|---|---|---|
| 3 | Does the EU AI Act apply to your UK business? A decision tree | /blog/ai/does-the-eu-ai-act-apply-to-my-uk-business | Topic #33 (P0, Quick Win) — sibling article in the same cluster |
| 4 | AI and UK GDPR: the ICO's 2026 guidance unpacked | /blog/ai/ai-and-uk-gdpr-ico-2026-guidance | Topic #35 (P1) — drills into the ICO row of the regulator map |
| 5 | The 2026 AI Playbook for UK Businesses | /blog/ai/2026-ai-playbook-for-uk-businesses | Pillar #1 — definitive hub once published |
| 6 | AI for UK law firms: the SRA framework after Garfield | /blog/ai/ai-for-uk-law-firms | Topic #60 (P0, Quick Win) — sibling article naming the same Garfield case |

## Anchor-text rules followed

- Every anchor is a noun phrase that restates the destination's H1 or a synonym.
- No banned anchors ("click here", "read more", "learn more", "this article", "find out more").
- One link is a pillar up-link (consultancy landing).
- One link is a cross-cluster bridge (sibling on-site AI content).

## Notes for the link injector

The website repo's `prebuild` step runs `scripts/add-internal-links-to-blog-articles.js`. That script auto-injects internal links into article bodies based on a registry mapping article keywords to destination URLs. When the engine publishes future Tom & Co AI articles, it should add an entry to that registry per article. Adding entries to the registry is part of the Phase 2 PR workflow.
