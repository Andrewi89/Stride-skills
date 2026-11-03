#!/usr/bin/env bash
# Installs the third-party skills and plugins I use alongside Stride Skills.
# Safe to re-run: anything already installed just reports and moves on.
set -u
failed=()

for repo in emilkowalski/skills Leonxlnx/taste-skill mvanhorn/cli-printing-press vercel-labs/skills; do
  echo "== skills: $repo"
  npx -y skills add "$repo" -g -a claude-code -s '*' -y || failed+=("$repo")
done

for m in pbakaus/impeccable DietrichGebert/ponytail paper-design/agent-plugins AgriciDaniel/claude-seo NoobyGains/claude-pulse; do
  echo "== marketplace: $m"
  claude plugin marketplace add "$m" || failed+=("$m")
done

for p in superpowers@claude-plugins-official frontend-design@claude-plugins-official \
         playwright@claude-plugins-official expo@claude-plugins-official \
         impeccable@impeccable ponytail@ponytail paper-desktop@paper \
         claude-seo@agricidaniel-claude-seo claude-pulse@claude-pulse; do
  echo "== plugin: $p"
  claude plugin install "$p" || failed+=("$p")
done

echo
if [ ${#failed[@]} -gt 0 ]; then
  echo "Didn't install (may already be there): ${failed[*]}"
else
  echo "All done. Restart Claude Code to load them."
fi
echo "Anthropic's built-ins (product-naming, docx, pdf, pptx, xlsx) are switched on in claude.ai settings."
