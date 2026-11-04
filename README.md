# Stride Skills

These are my go-to skills for Claude Code. The ones I reach for on every project: design, writing, marketing, and how I like AI to work. They're public so I can install them on any machine, and so you can borrow them.

## Install

Inside Claude Code:

```
/plugin marketplace add Andrewi89/Stride-skills
/plugin install stride-design@stride-skills
/plugin install stride-writing@stride-skills
/plugin install stride-marketing@stride-skills
/plugin install stride-steering@stride-skills
```

To also copy my global `CLAUDE.md` (the engineering principles) onto a new machine, clone the repo and run `./install.sh`. It asks before replacing your file and keeps a dated backup.

## What's inside

| Plugin | Skills |
|---|---|
| `stride-design` | `apple-design-duo` (iPhone Duo), `expo-duo`, `apple-preflight` (App Store checks), `design-copy` (words in interfaces) |
| `stride-writing` | `conversational-tone-of-voice` (my voice), `anti-slop-writing` (banned words and patterns), `ogilvy-copy` (selling copy) |
| `stride-marketing` | `marketing` (positioning and channels), `product-led-growth`, `product-naming` (finding a name that isn't safe) |
| `stride-steering` | `engineering-principles` (simple, fast-moving, no enterprise habits), `antigravity-driven-development` (Gemini does the grunt work, Claude reviews) |

## Skills I use alongside these

Other people built these, and they're excellent. I don't copy them here. Credit and installs go to their own repos.

To install the lot in one go (needs Node and the Claude Code CLI):

```
./install-others.sh
```

### Skill packs (installed with `npx skills add`)

| Repo | By | Licence | What I use it for |
|---|---|---|---|
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Emil Kowalski | MIT | `apple-design`, `emil-design-eng`, the animation skills, `break-ui`, `mobile-native`, `prototype`, `write-swift` |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Leon Lin | MIT | `design-taste-frontend`, `minimalist-ui`, `industrial-brutalist-ui`, `redesign-existing-projects`, `brandkit`, image-led frontends |
| [mvanhorn/cli-printing-press](https://github.com/mvanhorn/cli-printing-press) | Matt Van Horn | MIT | Generating and polishing command-line tools for APIs |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | Vercel | MIT | `find-skills`, and the `skills` installer itself |

### Plugins (installed with `/plugin install`)

| Plugin | By | Licence | What I use it for |
|---|---|---|---|
| [superpowers](https://github.com/obra/superpowers) | Jesse Vincent | MIT | Brainstorming, planning, TDD, debugging and review |
| [impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus | Apache 2.0 | Design critique, polish and anti-pattern detection |
| [ponytail](https://github.com/DietrichGebert/ponytail) | DietrichGebert | MIT | Pushing towards the simplest thing that works |
| [frontend-design](https://github.com/anthropics/claude-plugins-official) | Anthropic | Apache 2.0 | Distinctive frontend direction |
| [playwright](https://github.com/anthropics/claude-plugins-official) | Microsoft, via Anthropic's marketplace | Apache 2.0 | Driving a browser to check real pages |
| [expo](https://github.com/expo/skills) | Expo | see repo | Expo and EAS workflows |
| [paper-desktop](https://github.com/paper-design/agent-plugins) | Paper | see repo | Paper design tool integration |
| [claude-seo](https://github.com/AgriciDaniel/claude-seo) | Agrici Daniel | MIT | SEO audits |
| [claude-pulse](https://github.com/NoobyGains/claude-pulse) | David Innes | see repo | Usage and status display |

### Built into claude.ai

`docx`, `pdf`, `pptx`, `xlsx` and `skill-creator` are Anthropic's own skills. Turn them on in claude.ai's skill settings.

`ogilvy-copy` here is modified from the `ogilvy` skill in [boraoztunc/skills](https://github.com/boraoztunc/skills) by Bora (Apache 2.0, licence copy alongside it).

`anti-slop-writing` borrows patterns and its editing method from [humanizer](https://github.com/blader/humanizer) by Siqi Chen (MIT). `antigravity-driven-development` builds on superpowers' `subagent-driven-development` (MIT, licence copy alongside it).

## Keeping it clean

Before every commit, `scripts/check.sh` checks for em dashes, malformed skills and private folders, and `scripts/leak-scan.sh` checks every file against a private denylist that never leaves my machine. GitHub Actions repeats the checks on every push.

## Licence

My own files are MIT. Third-party skills keep their own licences and live in their own repos.
