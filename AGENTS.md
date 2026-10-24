# Repository rules for coding agents

This is an evidence-first GEO training and delivery skill, not a ranking manipulation package.

- Follow `skills/geo-first-client/SKILL.md` when editing or executing workflows.
- Do not introduce automatic posting, spam, platform bypass, scraping against terms, false reviews, false benchmarks, or fabricated client outcomes.
- Avoid external dependencies where the stdlib is sufficient.
- Never commit real client material, secrets, session cookies, or proprietary source articles.
- Preserve all 78 original task IDs in `references/curriculum-78.md` when editing; changing IDs requires a migration note and explicit user instruction.
- Test with `python skills/geo-first-client/scripts/validate_skill.py` before committing.
- For changes in metric formulas, add methodology notes and tests; do not claim causality from before/after samples.
