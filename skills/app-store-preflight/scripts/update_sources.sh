#!/usr/bin/env bash
# Re-scrape Apple's App Review Guidelines and App Review Help into source/ and show what changed.
# Maintainers then update references/ so every changed quote and check matches the new text.
set -euo pipefail
SKILL="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
UA="Mozilla/5.0"

curl -sfL -A "$UA" https://developer.apple.com/app-store/review/guidelines/ -o "$TMP/guidelines.html"
python3 -I "$SKILL/scripts/html2md.py" "$TMP/guidelines.html" > "$TMP/app-review-guidelines.md"

mkdir -p "$TMP/help"
curl -sfL -A "$UA" https://developer.apple.com/help/app-review/ -o "$TMP/help/index.html"
: > "$TMP/app-review-help.md"
for p in $(grep -o 'href="/help/app-review/[^"#]*"' "$TMP/help/index.html" | sed 's/href="//;s/"//' | sort -u); do
  f="$TMP/help/$(echo "$p" | tr '/' '_').html"
  curl -sfL -A "$UA" "https://developer.apple.com$p" -o "$f"
  echo "=== SOURCE: https://developer.apple.com$p" >> "$TMP/app-review-help.md"
  python3 -I "$SKILL/scripts/html2md.py" "$f" >> "$TMP/app-review-help.md"
  echo >> "$TMP/app-review-help.md"
done

for name in app-review-guidelines.md app-review-help.md; do
  if diff -q "$SKILL/source/$name" "$TMP/$name" > /dev/null; then
    echo "unchanged: $name"
  else
    echo "CHANGED: $name"
    diff -u "$SKILL/source/$name" "$TMP/$name" | head -200 || true
    cp "$TMP/$name" "$SKILL/source/$name"
  fi
done
echo "Next: update references/ for every changed passage, then run scripts/validate.sh"
