#!/usr/bin/env bash
# Sets up Claude Code the way I like it. Safe to re-run.
set -eu
cd "$(dirname "$0")"

mkdir -p ~/.claude
if [ -f ~/.claude/CLAUDE.md ] && ! cmp -s claude/CLAUDE.md ~/.claude/CLAUDE.md; then
  read -r -p "Replace ~/.claude/CLAUDE.md? A dated backup is kept. [y/N] " ok
  [ "$ok" = y ] || { echo "Kept your CLAUDE.md."; exit 0; }
  cp ~/.claude/CLAUDE.md ~/.claude/CLAUDE.md.bak."$(date +%Y%m%d%H%M%S)"
fi
cp claude/CLAUDE.md ~/.claude/CLAUDE.md

[ -d .git ] && ln -sf ../../scripts/pre-commit .git/hooks/pre-commit

echo "Now run these inside Claude Code:"
echo "  /plugin marketplace add Andrewi89/Stride-skills"
echo "  /plugin install design@stride-skills writing@stride-skills marketing@stride-skills steering@stride-skills"
echo "For the other skills I use, run ./install-others.sh (credits in README.md)."
