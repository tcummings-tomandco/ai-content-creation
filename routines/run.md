# Routine: write the next article

This is the prompt the scheduler fires (twice a week per the playbook cadence). For ad-hoc runs, paste this prompt verbatim into a fresh Claude Code session.

---

Run the `tomandco-article` skill end-to-end on the next topic in the queue.

1. Load the skill from `.claude/skills/tomandco-article/SKILL.md` and read every supporting file (`voice-guide.md`, `checklist.md`, `stat-sourcing.md`, `format-mapping.md`).
2. Pick the next topic: `python3 scripts/pick_next_topic.py` (or accept the explicit topic ID I give you below).
3. Execute the run order in SKILL.md sections 1 through 7. Do not skip the QA gate.
4. After running `python3 scripts/voice_check.py output/{folder}/article.json`, read the output. Any FAIL means iterate the draft and re-check before moving on. CLEAN required to proceed.
5. Draft the approval email via the gmail MCP (`mcp__aef2722b-...__create_draft`). Subject line and body per SKILL.md Step 8. Recipient: tom@tomandco.co.uk. Leave as draft.
6. Print a one-screen summary in chat: topic, word count, QA scoresheet (10 elements + voice check), stat layer used, output folder path, draft email ID.
7. Stop. Do not push to the website repo. Do not auto-send the email.

If anything fails the QA gate after two iteration attempts, stop and surface the specific failure to me.

Optional override: pick topic [ID].

---

## Schedule

Once Tom approves the engine output and we move to a real schedule:

- Cadence: 2 supporting articles per week (per the playbook). Mondays 06:30 and Thursdays 06:30 UK time.
- Plus 1 newsroom slot per fortnight (separate routine, news-driven topic selection).
- Plus 90-day refresh sweeps (separate routine, picks oldest-reviewed article).

For now, run manually by pasting this prompt.
