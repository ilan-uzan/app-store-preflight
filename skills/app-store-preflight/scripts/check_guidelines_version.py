#!/usr/bin/env python3
"""Compare the bundled App Review Guidelines date with Apple's live page.

Usage: python3 -I check_guidelines_version.py <bundled app-review-guidelines.md>
Exit code 0 = current (or offline), 1 = Apple's page is newer.
"""
import re
import sys
import urllib.request
from datetime import datetime

URL = "https://developer.apple.com/app-store/review/guidelines/"


def parse(text):
    m = re.search(r"Last Updated:\s*(?:<[^>]+>\s*)*([A-Z][a-z]+ \d{1,2}, \d{4})", text)
    return datetime.strptime(m.group(1), "%B %d, %Y") if m else None


def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        bundled = parse(f.read())
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
        live = parse(urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "replace"))
    except Exception as e:  # offline or blocked: never fail the audit for this
        print(f"Could not reach {URL} ({e.__class__.__name__}); using bundled guidelines dated {bundled:%B %d, %Y}.")
        return 0
    if live and bundled and live > bundled:
        print(f"NEWER GUIDELINES: Apple's page says Last Updated {live:%B %d, %Y}; bundled copy is {bundled:%B %d, %Y}. "
              "Run scripts/update_sources.sh and review the diff, or update the skill.")
        return 1
    print(f"Guidelines current: Last Updated {bundled:%B %d, %Y}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
