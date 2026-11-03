---
name: update-stride-skills
description: "Use whenever adding, importing, editing or removing a skill or plugin in the Stride-skills repo, or committing and pushing it. Runs the provenance check, the personal-data sweep (remove or make generic anything that identifies Andy, his employer, colleagues, customers or private projects), the guard scripts, and the push from the right GitHub account."
---

# Updating Stride-skills

This repo is public. Every change goes through the steps below, in order. If a step fails, stop and fix it before moving on.

## 1. Provenance: whose skill is it?

Before copying anything in, find out who wrote it.

- Check `~/.agents/.skill-lock.json`, `~/skills-lock.json` and `~/.claude/plugins/known_marketplaces.json` for a recorded source.
- If a source exists, diff the local copy against upstream. Identical or lightly edited means it is theirs.
- Check the `synced/` folder in `~/.claude/skills`. Those are claude.ai built-ins.

| Result | Action |
|---|---|
| Andy wrote it | Copy it in (step 2). |
| Someone else's, unchanged | Never copy it. Add a credit row to the README tables and an install line to `install-others.sh`. |
| A fork Andy changed substantially | Copy it, keep the upstream licence file beside it, credit the repo and author by real name (check their GitHub profile), and list the changes in a Source line. Follow the stricter licence if repo and file disagree. |
| Unsure | Ask Andy. |

## 2. Copy, never move

Copy from `~/.claude/skills/<name>` into `plugins/<plugin>/skills/<name>`. Leave the original in place. Exclude `transcripts/`, raw dumps, caches, `__pycache__`, `.DS_Store` and anything generated.

Never commit verbatim third-party documentation (Apple's HIG, vendor docs, book text). Link to it instead.

## 3. Personal-data sweep (the safeguard)

Read every new or changed file in full. The scripts catch known strings; this step catches what they can't know. Look for:

- **Employer and work:** the company name, internal product or project names, internal tools, team structure, roadmap, unreleased plans, metrics, customers, suppliers.
- **People:** colleagues', customers' or family members' names, handles or emails.
- **Infrastructure:** cloud project IDs, bucket names, internal domains and hostnames, IP addresses, service account names, deploy targets.
- **Identity:** email addresses, phone numbers, home address, work GitHub handles, Apple team IDs, bundle IDs, API keys, tokens.
- **Machine details:** home-folder paths, usernames in paths, local folder names that reveal private projects.
- **Private projects:** names of personal apps or side projects that are not already public.

For each hit, do one of these, and prefer the first that keeps the skill useful:

1. **Make it generic.** Keep the lesson, drop the identity.
2. **Remove it** if the detail adds nothing.
3. **Ask Andy** if it might be public already. Never assume something is public.

| Personal | Generic |
|---|---|
| "Our installer app at <company>" | "An app for installers" |
| "<personal app name> only reads your activity" | "This app only reads your activity" |
| A real project ID, domain or bucket | `my-project`, `example.com`, `my-bucket` |
| A colleague's name | "a teammate" |
| A real metric from work | Remove it, or a clearly made-up example marked as one |

If a hit reveals a new kind of sensitive string, add it to the denylist at `~/.config/stride-skills/denylist.txt` and update the CI secret (step 6). Never write the denylist's contents into the repo.

## 4. House rules

- No em dashes anywhere. UK English.
- `SKILL.md` frontmatter: `name` matches the folder. Quote the `description` if it contains `: `.
- One job per skill, under 300 lines where possible, never over 500.
- Writing inside skills follows `anti-slop-writing`.
- Bump the `version` in the plugin's `plugin.json` (patch for edits, minor for a new skill) so installs pick up the change.
- Update the README tables when a skill is added, renamed or removed.

## 5. Run the guards

```sh
bash scripts/check.sh && bash scripts/leak-scan.sh && claude plugin validate .
```

All three must pass. Never bypass the pre-commit hook. If a guard is wrong, fix the guard in its own commit.

## 6. Commit and push from the personal account

The repo belongs to `Andrewi89`. The active `gh` account on this machine may be a different one, so never rely on it.

- Commits use the repo-local no-reply email. Check with `git config user.email`. It must end in `users.noreply.github.com`.
- Show Andy a short summary of what changed and ask before pushing. Pushing publishes.
- Push with the personal account's token for that command only:

```sh
GH_TOKEN=$(gh auth token --user Andrewi89) git -c credential.helper= \
  -c "credential.helper=!f() { echo username=Andrewi89; echo password=\$GH_TOKEN; }; f" push
```

- If the denylist changed: `GH_TOKEN=$(gh auth token --user Andrewi89) gh secret set ANDY_DENYLIST -R Andrewi89/Stride-skills < ~/.config/stride-skills/denylist.txt`
- Confirm the Actions run is green: `GH_TOKEN=$(gh auth token --user Andrewi89) gh run list -R Andrewi89/Stride-skills --limit 1`

## 7. If something personal was already pushed

Tell Andy straight away. Remove it in a new commit, add the string to the denylist, and ask whether to rewrite history with a force push. Rewriting is his call, and anything public may already be cached.
