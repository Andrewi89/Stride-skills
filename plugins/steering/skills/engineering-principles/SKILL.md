---
name: engineering-principles
description: "Use when building, planning or reviewing software for Andy, or whenever a change risks over-engineering. A short version of how he wants Claude to work: simple, fast-moving startup habits, not enterprise ones. The full text is in claude/CLAUDE.md in the Stride-skills repo."
---

# Engineering principles (short version)

Andy is a solo founder still learning to code. The aim is software that stays simple and maintainable as it grows. We are a fast-moving company, not an enterprise.

## The things he always says

- **Keep it simple.** Handle the cases that matter, not every imaginable edge case. Extra complexity has to earn its place.
- **Only add code that is small or genuinely necessary.** If a change is neither, don't make it.
- **Fast-moving company, not an enterprise.** No process, layers or ceremony without a real reason.
- **Reuse or delete before you add.** Duplication is cheaper than the wrong abstraction.
- **YAGNI.** Add an abstraction when the second real case demands it.
- **One file, one job.** Soft limit about 300 lines, split before 500. Keep entry points thin.
- **Async for every external call.** Validate untrusted data where it enters. Secrets come from the environment, never the source.
- **Name things so the code reads itself.** Comment the why, not the what.
- **Test the parts that hold logic.** Fast, offline, mock the outside world.
- **Small, reversible commits.** One thing each.

## How to work with him

- Take the lead on infrastructure, security and deployment. Make the call and explain why, instead of asking him to validate details he doesn't know yet.
- Teach as you go. When you apply a principle, add a one-line note on the reason.
- Never use em dashes in code, copy, docs or chat. UK English.
- Writing style: see `anti-slop-writing` and `conversational-tone-of-voice`.

Full wording, with the reason behind each rule: `claude/CLAUDE.md` in the Stride-skills repo.
