#!/usr/bin/env bash
# Fails if a tracked file contains a denylisted string. The denylist is never committed.
set -u
cd "$(git rev-parse --show-toplevel)" || exit 1
list="${ANDY_DENYLIST:-$HOME/.config/stride-skills/denylist.txt}"
if [ ! -f "$list" ]; then
  echo "No denylist at $list"
  [ "${CI:-}" = true ] && { echo "Skipping in CI."; exit 0; }
  exit 1
fi
clean=$(mktemp)
grep -v '^[[:space:]]*$' "$list" > "$clean"
[ -s "$clean" ] || exit 0
if [ "${CI:-}" = true ]; then flags=-IiFl; else flags=-IiFn; fi
if git grep --cached $flags -f "$clean" -- .; then echo "FAIL: denylisted string found above"; rm -f "$clean"; exit 1; fi
rm -f "$clean"
