#!/usr/bin/env bash
# Guard for the public repo: fails on anything that should not be committed.
set -u
cd "$(git rev-parse --show-toplevel)" || exit 1
fail=0
bad() { echo "FAIL: $1"; fail=1; }

EM=$(printf '\xe2\x80\x94')
while IFS= read -r f; do bad "em dash in $f"; done < <(git grep --cached -lIF "$EM")

while IFS= read -r f; do
  dir=$(basename "$(dirname "$f")")
  fm=$(awk 'NR==1&&$0!="---"{exit} NR>1&&$0=="---"{exit} NR>1{print}' "$f")
  name=$(sed -n 's/^name: *//p' <<<"$fm" | head -1 | tr -d "\"'")
  [ "$name" = "$dir" ] || bad "$f: name does not match folder"
  grep -q '^description:' <<<"$fm" || bad "$f: missing description"
  [ "$(wc -l < "$f")" -le 500 ] || bad "$f: over 500 lines"
  if command -v ruby >/dev/null; then
    printf '%s\n' "$fm" | ruby -ryaml -e 'YAML.safe_load(STDIN.read)' 2>/dev/null || bad "$f: frontmatter is not valid YAML"
  fi
done < <(git ls-files '*SKILL.md')

# Personal data a denylist can't know in advance. Binaries included on purpose.
while IFS= read -r f; do bad "personal file path in $f"; done < <(git grep --cached -l -a -F -e '/Users/' -e '/home/' -- . ':!scripts/check.sh')
EMAIL='[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z.]{2,}'
while IFS= read -r hit; do bad "email address: $hit"; done < <(git grep --cached -n -I -E "$EMAIL" | grep -viE 'noreply')
[ -z "$(git ls-files '*.pyc' '*__pycache__*' '*.DS_Store')" ] || bad "build or OS junk is tracked (pyc, __pycache__, .DS_Store)"

[ -z "$(git ls-files docs/superpowers sources)" ] || bad "private folder is tracked (docs/superpowers or sources)"

m=.claude-plugin/marketplace.json
if [ -f "$m" ]; then
  command -v jq >/dev/null || { bad "jq is not installed"; exit 1; }
  if jq empty "$m" 2>/dev/null; then
    while IFS= read -r p; do [ -d "$p" ] || bad "missing plugin folder $p"; done \
      < <(jq -r '.plugins[] | select(.source|type=="string") | .source' "$m")
  else
    bad "$m is invalid JSON"
  fi
fi
exit $fail
