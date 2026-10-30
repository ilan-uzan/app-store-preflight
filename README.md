<div align="center">

# 🛫 App Store Preflight

**Catch App Store rejections before Apple does.**

A Claude Code skill + multi-agent workflow that reviews your app against **every App Store Review Guideline** and **every App Store Connect submission requirement**, marks each one ✅ or ❌ with evidence from your code, checks your App Store Connect listing in the browser, and then **fixes what fails**.

[![validate](https://github.com/ilan-uzan/app-store-preflight/actions/workflows/validate.yml/badge.svg)](https://github.com/ilan-uzan/app-store-preflight/actions/workflows/validate.yml)
![Guidelines](https://img.shields.io/badge/App%20Review%20Guidelines-Oct%2016%2C%202026-blue)
![Checks](https://img.shields.io/badge/checks-1773-success)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

</div>

---

## Why

A rejection costs days: wait in the queue, get a one-line guideline number, guess what it means, fix, resubmit, wait again. Most rejections come from things you could have checked: a missing purpose string, no in-app account deletion, a paywall without Restore Purchases, privacy labels that don't match the SDKs you ship, no demo account for the reviewer, placeholder text, a required-reason API missing from the privacy manifest.

App Store Preflight checks all of it in one command.

## What makes it different

- **Nothing is invented.** Every check quotes Apple word for word: the [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [App Review Help](https://developer.apple.com/help/app-review/), [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) and Apple's developer documentation. The scraped source texts ship in [`source/`](skills/app-store-preflight/source), and CI fails if any of the **10,915 quoted passages** doesn't appear verbatim in them.
- **Every guideline, not a top 10.** All 132 numbered guideline sections (1 to 5.6.4), plus privacy manifests and required-reason APIs, App Privacy labels and ATT, metadata limits and screenshot specs, age rating, export compliance, EU DSA trader status, in-app purchase and subscription setup, account deletion, Sign in with Apple, purpose strings, TestFlight and build statuses, agreements, tax and banking, pricing and availability, App Clips, Game Center, in-app events and custom product pages: **1,773 checks** in total.
- **It reads your app first.** A profiler works out what your app actually does (login? subscriptions? UGC? kids? health? location? AI?). Guidelines that don't apply are marked N/A with a reason, not padded into the report.
- **Failures are cross-examined.** For every ❌, a separate skeptic agent tries to prove it wrong (the deletion flow is on another screen; the SDK ships its own manifest; the purpose string is set in build settings). Only failures that survive are reported.
- **It checks App Store Connect too.** With Claude in Chrome or Playwright MCP, a read-only browser agent goes through your listing and compares it with the code: privacy labels vs the data your code collects, IAP product IDs in code vs products in App Store Connect, demo account present when login is required, age rating vs content, screenshots for every required size.
- **Backtested on real rejections.** Run against an app build that App Review rejected under guideline 5.6 (a paywall "Close" button that opened a discount offer instead of closing), preflight fails that build with `file:line` evidence and passes the fixed resubmission.
- **Then it fixes.** Confirmed code failures are fixed on a new git branch, one fixer at a time, followed by a rebuild and independent re-verification of every fix. App Store Connect changes are proposed and applied only with your approval. It never submits for you.

## Install

**As a Claude Code plugin (recommended):**

```
/plugin marketplace add ilan-uzan/app-store-preflight
/plugin install app-store-preflight@app-store-preflight
```

**As a standalone skill:**

```bash
git clone https://github.com/ilan-uzan/app-store-preflight.git
ln -s "$PWD/app-store-preflight/skills/app-store-preflight" ~/.claude/skills/app-store-preflight
```

Requirements: Claude Code, Python 3.9+ (standard library only), macOS with Xcode for the build/Simulator steps. Optional: [Claude in Chrome](https://claude.com/chrome) or the [Playwright MCP](https://github.com/microsoft/playwright-mcp) for the App Store Connect pass, and [AXe](https://github.com/cameroncooke/AXe) (`brew install cameroncooke/axe/axe`) so the Simulator pass can tap through your app.

## Use

From your app's folder:

```
/app-store-preflight
```

or just ask: *"Will my app get rejected?"*, *"Run an App Store preflight"*, *"Check my app against the App Store guidelines before I submit"*.

It asks four questions (audit or audit + fix, App Store Connect via browser or not, Simulator run or not, standard or thorough), then runs in the background. Watch it with `/workflows`.

## How it works

```
                ┌──────────────┐
   your app ──▶ │   scanner    │  Info.plist, purpose strings, entitlements, privacy manifests,
                │  (python)    │  required-reason APIs, SDKs, StoreKit, login, feature signals
                └──────┬───────┘
                       ▼
                ┌──────────────┐
                │   profiler   │  what the app really does → which guidelines apply
                └──────┬───────┘
        ┌──────────────┼──────────────────────────┐
        ▼              ▼                          ▼
 ┌─────────────┐ ┌───────────────┐        ┌───────────────┐
 │ auditors ×N │ │ App Store     │        │ Simulator run │ (optional)
 │ (per check  │ │ Connect agent │        │ build, launch,│
 │  batch)     │ │ (read-only)   │        │ walk flows    │
 └──────┬──────┘ └───────┬───────┘        └───────┬───────┘
        ▼                │                        │
 ┌─────────────┐         │                        │
 │ skeptic per │         │                        │
 │ ❌ and ⚠️    │         │                        │
 └──────┬──────┘         │                        │
        └────────────────┴──────────┬─────────────┘
                                    ▼
                    ┌──────────────────────────────┐
                    │ fixers (sequential) → build  │  audit + fix mode
                    │ → independent re-verify      │
                    └──────────────┬───────────────┘
                                   ▼
                        PREFLIGHT_REPORT.md
```

## The report

`.preflight/<timestamp>/PREFLIGHT_REPORT.md` in your project:

- **Status**: ❌ NOT READY / ⚠️ READY AFTER YOU CONFIRM / ✅ READY TO SUBMIT
- ❌ **Blocking issues**: guideline, problem, `file:line` evidence, how to fix
- 🔧 **Fixed by preflight**: what changed, which files, how to verify
- 🌐 **Check in App Store Connect** and ✋ **only you can confirm**: questions about legal, business or content facts
- **Draft notes for App Review**, ready to paste
- **Full checklist**: every check, grouped by guideline

## What's covered

| Area | Source |
|---|---|
| App Review Guidelines 1 Safety · 2 Performance · 3 Business · 4 Design · 5 Legal, plus Before / After You Submit | [guidelines](https://developer.apple.com/app-store/review/guidelines/) |
| App Review Help: complete review, IAP review, compatible devices, account deletion, purpose strings, screenshots, copycats, appeals | [help/app-review](https://developer.apple.com/help/app-review/) |
| Privacy manifests, required-reason APIs and approved reasons, third-party SDK requirements | [privacy manifest docs](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files) |
| App Privacy details (nutrition labels), App Tracking Transparency | [app privacy details](https://developer.apple.com/app-store/app-privacy-details/) |
| Product page metadata limits, screenshot and preview specifications, App Review Information | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) |
| Submission, age ratings, export compliance, EU DSA trader status, upcoming SDK requirements | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) |
| In-App Purchase and subscription configuration, disclosures, pricing, offers, server notifications | [subscriptions](https://developer.apple.com/app-store/subscriptions/) |
| TestFlight, Beta App Review, build upload and build statuses, app and submission statuses, phased release | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) |
| Agreements, tax, banking, pricing, availability, distribution methods, roles, China and Korea compliance | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) |
| watchOS, iMessage, visionOS, Mac App Sandbox, App Clips, asset packs, Game Center | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) |
| In-app events, custom product pages, accessibility nutrition labels, EULA, medical device declaration | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/) |
| Account deletion, Sign in with Apple, purpose strings, app icons, ATS | [developer docs](https://developer.apple.com/documentation/) |

## Staying current

Apple revises the guidelines several times a year. The skill compares its bundled copy with Apple's live page on every run and warns you if Apple's is newer. A weekly GitHub Action opens an issue when that happens, and `scripts/update_sources.sh` re-scrapes and diffs the sources.

## 🤝 Help make it better

This project gets better every time someone shares what App Review actually did. You don't need to write code to help:

| You have… | Do this |
|---|---|
| 🚫 A rejection preflight didn't catch | [Report a missed rejection](https://github.com/ilan-uzan/app-store-preflight/issues/new?template=missed-rejection.yml). The guideline number and the redacted message are enough |
| 🤔 A verdict that's wrong | [Report a wrong verdict](https://github.com/ilan-uzan/app-store-preflight/issues/new?template=false-positive.yml) with the check ID |
| 📜 Spotted an Apple change | [Report an Apple update](https://github.com/ilan-uzan/app-store-preflight/issues/new?template=apple-change.yml) |
| 🛠️ A bit of time and Python/JS | Pick a [`good first issue`](https://github.com/ilan-uzan/app-store-preflight/labels/good%20first%20issue) or [`help wanted`](https://github.com/ilan-uzan/app-store-preflight/labels/help%20wanted) |
| 💬 A report, an idea, a question | Start a [discussion](https://github.com/ilan-uzan/app-store-preflight/discussions) |

The one rule: **every check must quote Apple's own text**, and CI enforces it. See [CONTRIBUTING.md](CONTRIBUTING.md). Your first PR can be a single check.

## Disclaimer

Not affiliated with or endorsed by Apple. App Store, App Store Connect, TestFlight and Xcode are trademarks of Apple Inc. This tool lowers your rejection risk; it doesn't guarantee approval. App Review makes the final call.

If it saved you a rejection, a ⭐ helps other developers find it.
