# Engineering principles

These apply to every project unless a project's own `CLAUDE.md` says otherwise.
I'm a solo founder still learning to code. The goal is software that stays
simple and maintainable as it grows. Each rule below is followed by the reason,
so the "why" travels with the "what".

## The prime rule

- **Keep it simple.** Handle the cases that matter, not every imaginable edge
  case. This is a startup, not an enterprise. Simplicity is the default; extra
  complexity has to earn its place.
- **Only add code that is small or genuinely necessary.** If a change is neither
  small nor necessary, don't make it. Less code is less to maintain and less to
  break.

## Structure

- **One file, one job.** Soft limit around 300 lines; split before 500. A file
  that keeps growing is usually several small jobs hiding together.
- **Keep entry points thin.** Routes and handlers just receive a request and
  return a response. The real logic lives in its own module, where it can be
  read and tested on its own.
- **Talk through clear boundaries.** A module should expose a small, obvious
  interface. You should be able to change its insides without breaking anything
  that calls it.

## Restraint

- **YAGNI (You Aren't Gonna Need It).** Don't build for an imagined future. Add
  an abstraction when the *second* real case demands it, not before. Guessing
  wrong costs more than waiting.
- **Reuse or delete before you add.** If the code already exists, use it. But
  don't force two things that only look alike into one shared path. Duplication
  is cheaper than the wrong abstraction.

## Robustness

- **Async for every external call** (network, disk, database, third-party API).
  One slow call should not freeze everything else waiting behind it.
- **Validate untrusted data where it enters the app.** Turn it into a known,
  typed shape or fail loudly right there. Never let half-valid data drift
  deeper into the system.
- **Secrets and config come from the environment, never hardcoded.** Keys in the
  source get leaked and can't be rotated without a code change.

## Craft

- **Name things so the code reads itself.** A good name removes the need for a
  comment. Comment the *why* (the reason behind a choice), not the *what* (which
  the code already says).
- **Test the parts that hold logic; mock the outside world.** Tests should run
  fast and offline, and should fail when behaviour is actually wrong.
- **Small, reversible commits.** Each commit does one thing and is easy to review
  and easy to undo. Big commits hide mistakes.

## How to work with me

- Take the lead on infrastructure, security, and deployment decisions. Make the
  call and explain why, rather than asking me to validate specifics I don't yet
  know.
- Teach as you go. When you apply one of these principles, a one-line note on the
  reasoning helps me learn.
- Never use em dashes in code, copy, docs, or chat.
