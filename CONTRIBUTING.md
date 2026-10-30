# Contributing

Thanks for helping developers ship without rejections. Every contribution counts, from a one-line rejection report to a new scanner signal.

## The one rule

**Every check must be backed by Apple's own words.** No requirements from memory, blog posts, or "I heard App Review rejects…". Each check quotes an Apple page, that page's text ships in `skills/app-store-preflight/source/`, and CI fails if a quote doesn't appear there word for word. That's what lets people trust the report.

A rejection you got is still valuable even if you can't find Apple's wording: open a [missed-rejection issue](https://github.com/ilan-uzan/app-store-preflight/issues/new?template=missed-rejection.yml) and we'll find the source together.

## Ways to contribute

- **Report real rejections**, redacted. This is the most valuable input. It shows which checks need sharper `verify` steps.
- **Fix a wrong verdict.** Improve a check's `verify` instructions so auditors judge it correctly.
- **Add a check** for an Apple requirement that's missing (steps below).
- **Improve the scanner** (`scripts/scan_project.py`): new feature signals, better React Native, Expo and Flutter detection, macOS and visionOS specifics.
- **Improve the workflow** (`skills/app-store-preflight/workflow/preflight.js`): better prompts, cheaper batching, more verification lenses.
- **Keep it current** when Apple updates a page.
- **Share a redacted report** in Discussions, so others can see what a run finds.

## Add or fix a check

1. Find the requirement on an Apple page (developer.apple.com, help.apple.com, apple.com).
2. Make sure that page's text is in `skills/app-store-preflight/source/`. If it isn't, add the scraped text under a `=== SOURCE: <url>` header line. Use `scripts/html2md.py` for HTML pages and `scripts/docc2md.py` for `https://developer.apple.com/tutorials/data/documentation/<path>.json` pages.
3. Add the check under the right unit in `references/guidelines/` or `references/asc/`:

   ```markdown
   - **[2.3.3-04]** One pass/fail question
     - quote: "exact phrase from Apple's text"
     - surface: code | asc | runtime | manual
     - verify: how to check it (files, App Store Connect page and field, or runtime flow)
     - fix: the concrete fix, or "manual — requires developer decision"
   ```

   `surface` decides who evaluates it: `code` by the code auditors, `asc` by the App Store Connect browser agent, `runtime` by the Simulator agent, `manual` by asking the developer.
4. Optional: if Apple's stated scope limits the whole unit to apps with a specific feature, add `**Requires:** <flag>[, <flag>…]` under its `**Applies to:**` line. The allowed flags are the profile flags in `workflow/preflight.js`. When the app's profile rules out every listed flag, the planner skips the unit's checks as NA, so tag only when no check in the unit could matter to an app without the feature. When unsure, leave it untagged: untagged checks are always evaluated.
5. Run `skills/app-store-preflight/scripts/validate.sh`. It fails if a quote isn't verbatim in `source/`, if a check ID is duplicated, if a check is malformed, or if the two workflow copies differ.

## Test your change

```bash
python3 -I skills/app-store-preflight/scripts/scan_project.py /path/to/YourApp /tmp/facts.json
python3 -I skills/app-store-preflight/scripts/build_checks.py skills/app-store-preflight/references /tmp/checks.json
python3 -I skills/app-store-preflight/scripts/show_checks.py /tmp/checks.json 2.3.3-04
```

Run the script tests with `python3 -I -m unittest discover -s tests -v`. CI runs them too, along with `validate.sh`.

Then run `/app-store-preflight` on a real app in Claude Code, in audit-only mode, and look at the verdict for your check.

## When Apple updates the guidelines

The weekly `guidelines-watch` action opens an issue. Run `skills/app-store-preflight/scripts/update_sources.sh`, read the diff, update every affected unit and check, then run `validate.sh`.

## Workflow changes

Edit `skills/app-store-preflight/workflow/preflight.js`, then copy it to `workflows/preflight.js`. The plugin install and the standalone install each use their own copy, and CI checks that they match.

## Etiquette

Be kind and assume good intent. Never post credentials, private app details, or App Review reviewer names. Small PRs are easier to review: one check or one fix per PR is perfect.
