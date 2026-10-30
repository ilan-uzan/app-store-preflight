# App Review Guidelines — 2. Performance
Source: https://developer.apple.com/app-store/review/guidelines/#performance  
Retrieved: 2026-10-30

Note: Apple page "Last Updated: October 16, 2026". Source text below is copied verbatim from that page. Links in Apple's text are shown as plain text.

## 2 Performance

**Source text (verbatim):**
> 2. Performance

**Applies to:** All apps

**Status:** Section heading only — no requirement text of its own; see 2.1–2.5.19 for checks.

## 2.1 App Completeness

**Source text (verbatim):**
> 2.1 App Completeness
> - (a) Submissions to App Review, including apps you make available for pre-order, should be final versions with all necessary metadata and fully functional URLs included; placeholder text, empty websites, and other temporary content should be scrubbed before submission. Make sure your app has been tested on-device for bugs and stability before you submit it, and include demo account info (and turn on your back-end service!) if your app includes a login. If you are unable to provide a demo account due to legal or security obligations, you may include a built-in demo mode in lieu of a demo account with prior approval by Apple. Ensure the demo mode exhibits your app’s full features and functionality. We will reject incomplete app bundles and binaries that crash or exhibit obvious technical problems.
> - (b) If you offer in-app purchases in your app, make sure they are complete, up-to-date, visible to the reviewer and functional. If any configured in-app purchase items cannot be found or reviewed in your app, explain the reason in your review notes.

**Applies to:** All apps; (b) applies to apps that offer in-app purchases

- **[2.1-01]** Is all required App Store Connect metadata for the version filled in (no empty required fields)?
  - quote: "should be final versions with all necessary metadata"
  - surface: asc
  - verify: App Store Connect > Apps > [app] > [platform] version page: confirm description, keywords, support URL, screenshots, app privacy, age rating, and App Review Information are complete; no "missing" warnings when clicking "Add for Review".
  - fix: Fill in every missing field on the version page and App Information page.
- **[2.1-02]** Do all URLs in the metadata and in the app (support URL, marketing URL, privacy policy URL, in-app links) load and work?
  - quote: "fully functional URLs included"
  - surface: asc
  - verify: Collect Support URL, Marketing URL (version page) and Privacy Policy URL (App Privacy page) from App Store Connect; grep the project for `http://` / `https://` literals and `URL(string:` / `Link(` destinations; request each URL and confirm HTTP 200 with real content.
  - fix: Fix or replace broken URLs in App Store Connect and in code; publish the target pages.
- **[2.1-03]** Is the app and its metadata free of placeholder text (e.g. "Lorem ipsum", "TODO", "TBD", "placeholder", "test") and other temporary content?
  - quote: "placeholder text, empty websites, and other temporary content should be scrubbed before submission"
  - surface: code
  - verify: grep -ri in source, `.strings`/`.xcstrings`, storyboards/XIBs and asset names for `lorem`, `ipsum`, `TODO`, `FIXME`, `placeholder`, `TBD`, `sample text`, `test@`; review App Store Connect description/promotional text/What’s New for the same.
  - fix: Replace temporary strings/assets with final content; remove debug-only screens from release builds.
- **[2.1-04]** Do the linked websites (support, marketing, privacy) contain real content rather than empty or "coming soon" pages?
  - quote: "empty websites"
  - surface: manual
  - verify: Open each URL from App Store Connect in a browser and confirm the page has substantive content relevant to the app.
  - fix: Publish real content on the linked sites.
- **[2.1-05]** Has the build being submitted been tested on a physical device for bugs and stability?
  - quote: "Make sure your app has been tested on-device for bugs and stability before you submit it"
  - surface: runtime
  - verify: Install the release/TestFlight build on a physical device; exercise all main flows; check Xcode Organizer / TestFlight crash reports for this build.
  - fix: Fix crashes and bugs found on device, then upload a new build.
- **[2.1-06]** If the app has a login, are demo account credentials provided in App Review Information?
  - quote: "include demo account info (and turn on your back-end service!) if your app includes a login"
  - surface: asc
  - verify: Detect login in code (grep for `ASAuthorizationController`, `SignInWithAppleButton`, Firebase/Supabase/Auth0 auth calls, password `SecureField`); then App Store Connect > version page > App Review Information > "Sign-in required" checked with User name and Password filled.
  - fix: Create a working demo account and enter its credentials in App Review Information.
- **[2.1-07]** Is the back-end service the app depends on running and reachable during review, and does the demo account successfully sign in?
  - quote: "turn on your back-end service!"
  - surface: runtime
  - verify: Using the demo credentials, sign in on a clean install against the production back end; confirm API hosts found in code respond.
  - fix: manual — requires developer decision/legal/business action (keep the production back end live through review).
- **[2.1-08]** If a built-in demo mode is used instead of a demo account, was prior approval from Apple obtained and does the demo mode show the app’s full features and functionality?
  - quote: "you may include a built-in demo mode in lieu of a demo account with prior approval by Apple. Ensure the demo mode exhibits your app’s full features and functionality."
  - surface: manual
  - verify: Ask the developer for evidence of Apple’s prior approval; run demo mode and confirm all features are reachable.
  - fix: manual — requires developer decision/legal/business action (obtain Apple approval or provide a demo account).
- **[2.1-09]** Does the binary launch and run without crashes or obvious technical problems, and is the bundle complete?
  - quote: "We will reject incomplete app bundles and binaries that crash or exhibit obvious technical problems."
  - surface: runtime
  - verify: Archive a Release build, install on simulator/device, launch cold, walk every tab/screen; check for crashes, hangs, missing assets, broken layouts; review crash logs.
  - fix: Fix the crash/technical issue and missing resources, then re-archive.
- **[2.1-10]** If the app offers in-app purchases, are they complete, up-to-date, visible to the reviewer and functional?
  - quote: "If you offer in-app purchases in your app, make sure they are complete, up-to-date, visible to the reviewer and functional."
  - surface: asc
  - verify: Code: grep for `StoreKit`, `Product.products(for:`, `SKProductsRequest`, `SubscriptionStoreView`, RevenueCat; list product IDs. ASC: Monetization > In-App Purchases / Subscriptions — each product has status "Ready to Submit"/"Approved", metadata and review screenshot complete, and is attached to the version. Runtime: products load and can be purchased in sandbox.
  - fix: Complete IAP metadata in App Store Connect, attach to the version, make product IDs in code match, and expose the purchase UI.
- **[2.1-11]** If any configured in-app purchase cannot be found or reviewed in the app, do the review notes explain why?
  - quote: "If any configured in-app purchase items cannot be found or reviewed in your app, explain the reason in your review notes."
  - surface: asc
  - verify: Compare product IDs configured in App Store Connect with product IDs referenced in code/StoreKit config; for any not reachable, check App Review Information > Notes for an explanation.
  - fix: Add an explanation to the review Notes, or surface the IAP in the app.

## 2.2 Beta Testing

**Source text (verbatim):**
> 2.2 Beta Testing
> Demos, betas, and trial versions of your app don’t belong on the App Store – use TestFlight instead. Any app submitted for beta distribution via TestFlight should be intended for public distribution and should comply with the App Review Guidelines. Note, however, that apps using TestFlight cannot be distributed to testers in exchange for compensation of any kind, including as a reward for crowd-sourced funding. Significant updates to your beta build should be submitted to TestFlight App Review before being distributed to your testers. To learn more, visit the TestFlight Beta Testing page.

**Applies to:** All apps; TestFlight items apply to apps distributed via TestFlight

**Related:** TestFlight Beta Testing page

- **[2.2-01]** Is the App Store submission a release version rather than a demo, beta, or trial version of the app (pre-release builds belong in TestFlight)?
  - quote: "Demos, betas, and trial versions of your app don’t belong on the App Store – use TestFlight instead."
  - surface: code
  - verify: grep source, strings files and Info.plist (`CFBundleDisplayName`, `CFBundleName`) for `beta`, `demo`, `trial version`, `preview build`; check App Store Connect app name, subtitle and description for the same.
  - fix: Remove beta/demo labeling; distribute pre-release builds through TestFlight only.
- **[2.2-02]** Is any app submitted to TestFlight intended for public distribution and compliant with the App Review Guidelines?
  - quote: "Any app submitted for beta distribution via TestFlight should be intended for public distribution and should comply with the App Review Guidelines."
  - surface: manual
  - verify: Ask the developer to confirm the TestFlight build is intended for public release; run the rest of this audit against the TestFlight build.
  - fix: manual — requires developer decision/legal/business action.
- **[2.2-03]** Are TestFlight testers not given access in exchange for any compensation (including crowd-funding rewards)?
  - quote: "apps using TestFlight cannot be distributed to testers in exchange for compensation of any kind, including as a reward for crowd-sourced funding"
  - surface: manual
  - verify: Ask the developer whether beta access is sold or offered as a backer/crowdfunding reward; check marketing sites/Kickstarter/Patreon pages if any.
  - fix: manual — requires developer decision/legal/business action (stop offering TestFlight access as paid reward).
- **[2.2-04]** Were significant updates to the beta build submitted to TestFlight App Review before being distributed to testers?
  - quote: "Significant updates to your beta build should be submitted to TestFlight App Review before being distributed to your testers."
  - surface: asc
  - verify: App Store Connect > TestFlight > builds: confirm builds distributed to external testers show beta review status "Approved".
  - fix: Submit the build for Beta App Review before distributing to external testers.

## 2.3 Accurate Metadata

**Source text (verbatim):**
> 2.3 Accurate Metadata
> Customers should know what they’re getting when they download or buy your app, so make sure all your app metadata, including privacy information, your app description, screenshots, and previews accurately reflect the app’s core experience and remember to keep them up-to-date with new versions.

**Applies to:** All apps

- **[2.3-01]** Do the app description, screenshots, and previews accurately reflect the app’s core experience as built?
  - quote: "your app description, screenshots, and previews accurately reflect the app’s core experience"
  - surface: asc
  - verify: Read App Store Connect description and view screenshots/previews; compare every claimed feature against the code (features present, reachable in UI) and against the running app.
  - fix: Rewrite description/replace screenshots to match the actual app, or implement the missing features.
- **[2.3-02]** Does the App Privacy information in App Store Connect accurately reflect the data the app actually collects?
  - quote: "all your app metadata, including privacy information"
  - surface: asc
  - verify: Inventory data collection in code (PrivacyInfo.xcprivacy `NSPrivacyCollectedDataTypes`, analytics/ads/crash SDKs, Info.plist usage-description keys, network calls sending user data) and compare with App Store Connect > App Privacy data types and linking/tracking answers.
  - fix: Update App Privacy answers (and PrivacyInfo.xcprivacy) so they match actual collection.
- **[2.3-03]** Has the metadata been updated for this new version (no stale features, screenshots, or descriptions from earlier versions)?
  - quote: "remember to keep them up-to-date with new versions"
  - surface: asc
  - verify: Compare the current version’s description and screenshots with UI and features changed since the last release (git log since last release tag).
  - fix: Update description and screenshots for the new version.

## 2.3.1 Misleading metadata and Notes for Review

**Source text (verbatim):**
> 2.3.1
> - (a) All new features, functionality, and product changes must be described with specificity in the Notes for Review section of App Store Connect (generic descriptions will be rejected) and accessible for review. Similarly, marketing your app in a misleading way, such as by promoting content or services that it does not actually offer (such as iOS-based virus and malware scanners) or promoting a false price, whether within or outside of the App Store, is grounds for removal of your app from the App Store or a block from installing via alternative distribution and termination of your developer account.
> - (b) Egregious or repeated behavior is grounds for removal from the Apple Developer Program. We work hard to make the App Store a trustworthy ecosystem and expect our app developers to follow suit; if you’re dishonest, we don’t want to do business with you.

**Applies to:** All apps

- **[2.3.1-01]** Are all new features, functionality, and product changes described with specificity (not generically) in the Notes for Review?
  - quote: "All new features, functionality, and product changes must be described with specificity in the Notes for Review section of App Store Connect (generic descriptions will be rejected)"
  - surface: asc
  - verify: Diff the code since the last released version (git log/tag) to list new features; App Store Connect > version page > App Review Information > Notes: confirm each is named specifically with where to find it.
  - fix: Write specific review notes listing each new feature and how to reach it.
- **[2.3.1-02]** Are the new features accessible to the reviewer (not gated behind server flags, regions, or accounts the reviewer cannot use)?
  - quote: "and accessible for review"
  - surface: runtime
  - verify: grep for feature flags/remote config (`RemoteConfig`, `featureFlag`, `isEnabled`, LaunchDarkly, Statsig); confirm new features are enabled for production/review; exercise them with the demo account.
  - fix: Enable the features for review, or explain access steps in review Notes.
- **[2.3.1-03]** Does the app avoid marketing content or services it does not actually offer?
  - quote: "promoting content or services that it does not actually offer (such as iOS-based virus and malware scanners)"
  - surface: asc
  - verify: Compare every claim in name, subtitle, description, promotional text, screenshots and external marketing with implemented functionality; flag claims such as virus/malware scanning.
  - fix: Remove claims of content/services the app does not provide.
- **[2.3.1-04]** Are prices shown in or outside the App Store accurate (no false price promoted)?
  - quote: "promoting a false price, whether within or outside of the App Store"
  - surface: manual
  - verify: Compare any price mentioned in metadata, in-app copy, or marketing site with App Store Connect pricing and IAP prices; flag hard-coded price strings in app copy that may not match the actual StoreKit price.
  - fix: Correct or remove false prices (displaying StoreKit-provided prices is one way to keep in-app prices accurate).
- **[2.3.1-05]** Is the developer’s marketing honest and not egregiously or repeatedly misleading?
  - quote: "Egregious or repeated behavior is grounds for removal from the Apple Developer Program."
  - surface: manual
  - verify: Ask the developer to attest that prior rejections for misleading behavior have been addressed and none recur.
  - fix: manual — requires developer decision/legal/business action.

## 2.3.2 In-app purchase disclosure and promotion

**Source text (verbatim):**
> 2.3.2 If your app includes in-app purchases, make sure your app description, screenshots, and previews clearly indicate whether any featured items, levels, subscriptions, etc. require additional purchases. If you decide to promote in-app purchases on the App Store, ensure that the in-app purchase Display Name, Screenshot and Description are appropriate for a public audience, that you follow the guidance found in Promoting Your In-App Purchases, and that your app properly handles the SKPaymentTransactionObserver method so that customers can seamlessly complete the purchase when your app launches.

**Applies to:** Apps that include in-app purchases; promotion items apply to apps that promote in-app purchases on the App Store

**Related:** Promoting Your In-App Purchases

- **[2.3.2-01]** Do the description, screenshots, and previews clearly indicate which featured items, levels, subscriptions, etc. require additional purchases?
  - quote: "make sure your app description, screenshots, and previews clearly indicate whether any featured items, levels, subscriptions, etc. require additional purchases"
  - surface: asc
  - verify: List paid features from code (entitlement checks, paywall gates). In App Store Connect, read description and view screenshots/previews; confirm features shown that are paid are marked as requiring purchase/subscription.
  - fix: Add clear disclosure (e.g. "requires subscription") in description and screenshot captions.
- **[2.3.2-02]** If in-app purchases are promoted on the App Store, are their Display Name, Screenshot and Description appropriate for a public audience?
  - quote: "ensure that the in-app purchase Display Name, Screenshot and Description are appropriate for a public audience"
  - surface: asc
  - verify: App Store Connect > Monetization > In-App Purchases/Subscriptions > each promoted product: review Display Name, Description (localizations) and promotional image.
  - fix: Edit the IAP display name/description/image to be appropriate for all audiences.
- **[2.3.2-03]** If in-app purchases are promoted, does the setup follow Apple’s "Promoting Your In-App Purchases" guidance?
  - quote: "that you follow the guidance found in Promoting Your In-App Purchases"
  - surface: manual
  - verify: Review promoted IAP configuration in App Store Connect against the Promoting Your In-App Purchases document.
  - fix: Adjust promotion configuration to match that guidance.
- **[2.3.2-04]** If in-app purchases are promoted, does the app handle App Store–initiated purchases at launch so customers can complete them?
  - quote: "your app properly handles the SKPaymentTransactionObserver method so that customers can seamlessly complete the purchase when your app launches"
  - surface: code
  - verify: grep for `SKPaymentTransactionObserver` and `paymentQueue(_:shouldAddStorePayment:for:)` (StoreKit 1) or `PurchaseIntent.intents` (StoreKit 2); confirm the observer is registered early (e.g. in `application(_:didFinishLaunchingWithOptions:)` / app `init`).
  - fix: Register a transaction observer at launch and implement the promoted-purchase handler to continue the purchase.

## 2.3.3 Screenshots

**Source text (verbatim):**
> 2.3.3 Screenshots should show the app in use, and not merely the title art, login page, or splash screen. They may also include text and image overlays (for example, to demonstrate input mechanisms, such as an animated touch point or Apple Pencil) and show extended functionality on device, such as Touch Bar. Learn more about showing your app in use in screenshots.

**Applies to:** All apps

- **[2.3.3-01]** Do the screenshots show the app in use, rather than only title art, the login page, or the splash screen?
  - quote: "Screenshots should show the app in use, and not merely the title art, login page, or splash screen."
  - surface: asc
  - verify: App Store Connect > version page > Previews and Screenshots: for each device size and localization, confirm screenshots depict actual app screens in use; flag any that are only splash/launch, login, or title art.
  - fix: Capture new screenshots of core app screens in use and upload them.

## 2.3.4 Previews

**Source text (verbatim):**
> 2.3.4 Previews are a great way for customers to see what your app looks like and what it does. To ensure people understand what they’ll be getting with your app, previews may only use video screen captures of the app itself. Stickers and iMessage extensions may show the user experience in the Messages app. You can add narration and video or textual overlays to help explain anything that isn’t clear from the video alone.

**Applies to:** Apps with App Previews

- **[2.3.4-01]** Do app previews use only video screen captures of the app itself (no live-action footage, other apps, or rendered footage not from the app)?
  - quote: "previews may only use video screen captures of the app itself"
  - surface: asc
  - verify: App Store Connect > version page > Previews and Screenshots: play each app preview and confirm all footage is screen capture of this app (narration and overlays are permitted). Stickers/iMessage extensions may show the Messages app.
  - fix: Re-record previews using screen capture of the app only.

## 2.3.5 Category

**Source text (verbatim):**
> 2.3.5 Select the most appropriate category for your app, and check out the App Store Category Definitions if you need help. If you’re way off base, we may change the category for you.

**Applies to:** All apps

**Related:** App Store Category Definitions

- **[2.3.5-01]** Is the selected primary (and secondary) category the most appropriate for the app’s functionality?
  - quote: "Select the most appropriate category for your app"
  - surface: asc
  - verify: App Store Connect > App Information > Category (Primary/Secondary); compare with the app’s core functionality and the App Store Category Definitions; also check `LSApplicationCategoryType` in Info.plist for macOS.
  - fix: Change the category in App Information to the best fit.

## 2.3.6 Age rating

**Source text (verbatim):**
> 2.3.6 Answer the age rating questions in App Store Connect honestly so that your app aligns properly with parental controls. If your app is mis-rated, customers might be surprised by what they get, or it could trigger an inquiry from government regulators. If your app includes media that requires the display of content ratings or warnings (such as films, music, games, etc.), you are responsible for complying with local requirements in each territory where your app is available.

**Applies to:** All apps; the last sentence applies to apps that include media requiring content ratings or warnings

- **[2.3.6-01]** Do the age rating questionnaire answers honestly match the app’s actual content and features?
  - quote: "Answer the age rating questions in App Store Connect honestly"
  - surface: asc
  - verify: App Store Connect > App Information > Age Rating > Edit: review each answer; compare with content found in the app (violence, mature themes, gambling, user-generated content, unrestricted web access via `WKWebView`/`SFSafariViewController`, chat, etc.).
  - fix: Update the age rating answers to reflect actual content.
- **[2.3.6-02]** If the app includes media requiring content ratings or warnings (films, music, games, etc.), does it comply with local requirements in each territory where it is available?
  - quote: "If your app includes media that requires the display of content ratings or warnings (such as films, music, games, etc.), you are responsible for complying with local requirements in each territory where your app is available."
  - surface: manual
  - verify: Ask the developer which territories the app is available in (App Store Connect > Pricing and Availability) and whether each has rating/warning display requirements for the media included; confirm the app displays them.
  - fix: manual — requires developer decision/legal/business action.

## 2.3.7 App name, keywords, subtitle

**Source text (verbatim):**
> 2.3.7 Choose a unique app name, assign keywords that accurately describe your app, and don’t try to pack any of your metadata with trademarked terms, popular app names, pricing information, or other irrelevant phrases just to game the system. App names must be limited to 30 characters. Metadata such as app names, subtitles, screenshots, and previews should not include prices, terms, or descriptions that are not specific to the metadata type. App subtitles are a great way to provide additional context for your app; they must follow our standard metadata rules and should not include inappropriate content, reference other apps, or make unverifiable product claims. Apple may modify inappropriate keywords at any time or take other appropriate steps to prevent abuse.

**Applies to:** All apps

- **[2.3.7-01]** Is the app name unique (not copying another app’s name)?
  - quote: "Choose a unique app name"
  - surface: manual
  - verify: Search the App Store for the exact app name from App Store Connect > App Information > Name and confirm no confusingly identical app exists.
  - fix: Choose a distinct app name.
- **[2.3.7-02]** Do the keywords accurately describe the app?
  - quote: "assign keywords that accurately describe your app"
  - surface: asc
  - verify: App Store Connect > version page > Keywords: confirm each keyword relates to actual app functionality.
  - fix: Replace inaccurate keywords.
- **[2.3.7-03]** Is the metadata free of trademarked terms, popular app names, pricing information, or other irrelevant phrases used to game the system?
  - quote: "don’t try to pack any of your metadata with trademarked terms, popular app names, pricing information, or other irrelevant phrases just to game the system"
  - surface: asc
  - verify: Review name, subtitle, keywords, description and promotional text in App Store Connect for competitor/popular app names, third-party trademarks, words like "free", "$", "sale", and unrelated terms.
  - fix: Remove the offending terms from metadata.
- **[2.3.7-04]** Is the app name 30 characters or fewer?
  - quote: "App names must be limited to 30 characters."
  - surface: asc
  - verify: Count characters of App Store Connect > App Information > Name for every localization; also check `CFBundleDisplayName` length.
  - fix: Shorten the app name to 30 characters or fewer.
- **[2.3.7-05]** Are app names, subtitles, screenshots, and previews free of prices, terms, or descriptions not specific to that metadata type?
  - quote: "Metadata such as app names, subtitles, screenshots, and previews should not include prices, terms, or descriptions that are not specific to the metadata type."
  - surface: asc
  - verify: Inspect name, subtitle, screenshot text overlays and previews in App Store Connect for prices or text that belongs elsewhere.
  - fix: Remove prices and off-type text from those fields/assets.
- **[2.3.7-06]** Is the subtitle free of inappropriate content, references to other apps, and unverifiable product claims?
  - quote: "should not include inappropriate content, reference other apps, or make unverifiable product claims"
  - surface: asc
  - verify: App Store Connect > App Information > Subtitle (each localization): flag other app names and claims like "#1", "best", "most popular".
  - fix: Rewrite the subtitle.

## 2.3.8 Metadata appropriate for all audiences

**Source text (verbatim):**
> 2.3.8 Metadata should be appropriate for all audiences, so make sure your app and in-app purchase icons, screenshots, and previews adhere to a 4+ age rating even if your app is rated higher. For example, if your app is a game that includes violence, select images that don’t depict a gruesome death or a gun pointed at a specific character. Use of terms like “For Kids” and “For Children” in app metadata is reserved in the App Store for the Kids Category. Remember to ensure your metadata, including app name and icons (small, large, Apple Watch app, alternate icons, etc.), are similar to avoid creating confusion.

**Applies to:** All apps

- **[2.3.8-01]** Do the app icon, in-app purchase icons/images, screenshots, and previews adhere to a 4+ age rating, regardless of the app’s rating?
  - quote: "make sure your app and in-app purchase icons, screenshots, and previews adhere to a 4+ age rating even if your app is rated higher"
  - surface: asc
  - verify: Review the AppIcon in `Assets.xcassets`, alternate icons, IAP promotional images, and all screenshots/previews in App Store Connect for gore, gruesome death, a gun pointed at a character, sexual or other mature imagery.
  - fix: Replace assets with 4+-appropriate imagery.
- **[2.3.8-02]** If the app is not in the Kids Category, is metadata free of terms like “For Kids” and “For Children”?
  - quote: "Use of terms like “For Kids” and “For Children” in app metadata is reserved in the App Store for the Kids Category."
  - surface: asc
  - verify: Check App Information > Category; if not Kids, search name, subtitle, keywords, description, promotional text for "for kids", "for children".
  - fix: Remove those terms, or (if eligible) move the app to the Kids Category.
- **[2.3.8-03]** Are the app name and icons (small, large, Apple Watch app, alternate icons, etc.) consistent with each other to avoid confusion?
  - quote: "ensure your metadata, including app name and icons (small, large, Apple Watch app, alternate icons, etc.), are similar to avoid creating confusion"
  - surface: code
  - verify: Compare `CFBundleDisplayName`/`CFBundleName` with App Store Connect app name; compare AppIcon set, watchOS AppIcon, and `CFBundleAlternateIcons` / alternate app icon sets in `Assets.xcassets` for visual consistency.
  - fix: Align display name with the store name and make icon variants visually consistent.

## 2.3.9 Rights to materials; fictional account data

**Source text (verbatim):**
> 2.3.9 You are responsible for securing the rights to use all materials in your app icons, screenshots, and previews, and you should display fictional account information instead of data from a real person.

**Applies to:** All apps

- **[2.3.9-01]** Has the developer secured rights to all materials used in app icons, screenshots, and previews?
  - quote: "You are responsible for securing the rights to use all materials in your app icons, screenshots, and previews"
  - surface: manual
  - verify: Ask the developer to confirm ownership/licenses for fonts, images, characters, logos, and music in icons, screenshots and previews.
  - fix: manual — requires developer decision/legal/business action (license or replace the materials).
- **[2.3.9-02]** Do screenshots and previews display fictional account information instead of a real person’s data?
  - quote: "you should display fictional account information instead of data from a real person"
  - surface: asc
  - verify: Inspect screenshots/previews in App Store Connect for real names, emails, phone numbers, addresses, photos, or account details.
  - fix: Recapture screenshots using fictional demo data.

## 2.3.10 Focus on Apple platforms

**Source text (verbatim):**
> 2.3.10 Make sure your app is focused on the experience of the Apple platforms it supports, and don’t include names, icons, or imagery of other mobile platforms or alternative app marketplaces in your app or metadata, unless there is specific, approved interactive functionality. Make sure your app metadata is focused on the app itself and its experience. Don’t include irrelevant information.

**Applies to:** All apps

- **[2.3.10-01]** Are the app and its metadata free of names, icons, or imagery of other mobile platforms or alternative app marketplaces (unless there is specific, approved interactive functionality)?
  - quote: "don’t include names, icons, or imagery of other mobile platforms or alternative app marketplaces in your app or metadata, unless there is specific, approved interactive functionality"
  - surface: code
  - verify: grep -ri source, strings files and asset names for `Android`, `Google Play`, `Play Store`, `Galaxy Store`, `Windows Phone`, alternative marketplace names; review App Store Connect description, screenshots and previews for the same names or logos.
  - fix: Remove references to other platforms/marketplaces from the app and metadata.
- **[2.3.10-02]** Is the metadata focused on the app itself and its experience, without irrelevant information?
  - quote: "Make sure your app metadata is focused on the app itself and its experience. Don’t include irrelevant information."
  - surface: asc
  - verify: Read description, promotional text and What’s New in App Store Connect; flag content unrelated to the app.
  - fix: Remove irrelevant content from metadata.

## 2.3.11 Pre-orders

**Source text (verbatim):**
> 2.3.11 Apps you submit for pre-order on the App Store must be complete and deliverable as submitted. Ensure that the app you ultimately release is not materially different from what you advertise while the app is in a pre-order state. If you make material changes to the app (such as changing business models), you should restart your pre-order sales.

**Applies to:** Apps offered for pre-order

- **[2.3.11-01]** If the app is submitted for pre-order, is it complete and deliverable as submitted?
  - quote: "Apps you submit for pre-order on the App Store must be complete and deliverable as submitted."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > Pre-Orders: if enabled, run all 2.1 completeness checks against the submitted build.
  - fix: Complete the app before submitting for pre-order.
- **[2.3.11-02]** Is the released app not materially different from what was advertised during pre-order, and were pre-order sales restarted after any material change (such as a business model change)?
  - quote: "Ensure that the app you ultimately release is not materially different from what you advertise while the app is in a pre-order state. If you make material changes to the app (such as changing business models), you should restart your pre-order sales."
  - surface: manual
  - verify: Ask the developer whether features or business model changed since pre-order began; compare pre-order metadata with the release build.
  - fix: manual — requires developer decision/legal/business action (restart pre-order sales or restore advertised functionality).

## 2.3.12 What’s New text

**Source text (verbatim):**
> 2.3.12 Apps must clearly describe new features and product changes in their “What’s New” text. Simple bug fixes, security updates, and performance improvements may rely on a generic description, but more significant changes must be listed in the notes.

**Applies to:** App updates

- **[2.3.12-01]** Does the “What’s New” text clearly describe new features and product changes, listing significant changes specifically (generic text only for simple bug fixes, security updates, and performance improvements)?
  - quote: "Apps must clearly describe new features and product changes in their “What’s New” text. Simple bug fixes, security updates, and performance improvements may rely on a generic description, but more significant changes must be listed in the notes."
  - surface: asc
  - verify: Diff code since the last released version (git log/tags) to list significant changes; App Store Connect > version page > What’s New in This Version (each localization): confirm each significant change is listed.
  - fix: Rewrite What’s New to list each significant feature/change.

## 2.3.13 In-app events

**Source text (verbatim):**
> 2.3.13 In-app events are timely events that happen within your app. To feature your event on the App Store, it must fall within an event type provided in App Store Connect. All event metadata must be accurate and pertain to the event itself, rather than the app more generally. Events must happen at the times and dates you select in App Store Connect, including across multiple storefronts. You may monetize your event so long as you follow the rules set forth in Section 3 on Business. And your event deep link must direct users to the proper destination within your app. Read In-App Events for detailed guidance on acceptable event metadata and event deep links.

**Applies to:** Apps featuring in-app events on the App Store

**Related:** In-App Events; Section 3 on Business

- **[2.3.13-01]** Does each in-app event fall within an event type provided in App Store Connect?
  - quote: "it must fall within an event type provided in App Store Connect"
  - surface: asc
  - verify: App Store Connect > [app] > In-App Events: for each event, confirm the selected Event Type matches what the event actually is.
  - fix: Change the event type or redesign the event to fit a provided type.
- **[2.3.13-02]** Is all event metadata accurate and about the event itself rather than the app generally?
  - quote: "All event metadata must be accurate and pertain to the event itself, rather than the app more generally."
  - surface: asc
  - verify: Read each event’s name, short description, long description and media in App Store Connect.
  - fix: Rewrite event metadata to describe the event specifically.
- **[2.3.13-03]** Does the event actually happen at the times and dates selected in App Store Connect, across all storefronts?
  - quote: "Events must happen at the times and dates you select in App Store Connect, including across multiple storefronts."
  - surface: runtime
  - verify: Compare event start/end dates and storefront availability in App Store Connect with the in-app/server event schedule (remote config, server dates, time-zone handling in code).
  - fix: Align the in-app schedule with App Store Connect dates, or update the dates.
- **[2.3.13-04]** If the event is monetized, does it follow Section 3 Business rules?
  - quote: "You may monetize your event so long as you follow the rules set forth in Section 3 on Business."
  - surface: manual
  - verify: If the event involves purchases, run the Section 3 checks (e.g. in-app purchase usage) for the event flow.
  - fix: Apply the relevant Section 3 fixes.
- **[2.3.13-05]** Does each event deep link open the proper destination within the app?
  - quote: "your event deep link must direct users to the proper destination within your app"
  - surface: runtime
  - verify: Get each event’s deep link from App Store Connect; check handling in code (`onOpenURL`, `application(_:open:options:)`, `scene(_:openURLContexts:)`, universal links / `NSUserActivity`); open the link on simulator (`xcrun simctl openurl booted <url>`) and confirm the event screen opens.
  - fix: Implement or fix deep link routing to the event destination.

## 2.3.14 Creative assets

**Source text (verbatim):**
> 2.3.14 Creative assets allow you to highlight the value of your app in new ways compared to app-in-use screenshots and preview videos, and can be used across the App Store, including the product page header and in search results. Creative assets must pertain to your app’s content and functionality or overarching brand, follow standard metadata guidelines, and be appropriate for all audiences. They should not include inappropriate content, references to other apps with an intent to mislead, unverifiable product claims, or specific or discounted pricing information. Read App Store asset best practices for detailed guidance on acceptable recommendations.

**Applies to:** Apps that provide creative assets

**Related:** App Store asset best practices

- **[2.3.14-01]** Do creative assets pertain to the app’s content and functionality or overarching brand, and are they appropriate for all audiences?
  - quote: "Creative assets must pertain to your app’s content and functionality or overarching brand, follow standard metadata guidelines, and be appropriate for all audiences."
  - surface: asc
  - verify: Review creative assets uploaded in App Store Connect against app features/brand and 4+ appropriateness.
  - fix: Replace unrelated or inappropriate creative assets.
- **[2.3.14-02]** Are creative assets free of inappropriate content, misleading references to other apps, unverifiable product claims, and specific or discounted pricing?
  - quote: "They should not include inappropriate content, references to other apps with an intent to mislead, unverifiable product claims, or specific or discounted pricing information."
  - surface: asc
  - verify: Inspect text and imagery of each creative asset for other app names, "#1"/"best" claims, prices, "% off", "sale".
  - fix: Remove the offending elements from creative assets.

## 2.4 Hardware Compatibility

**Source text (verbatim):**
> 2.4 Hardware Compatibility

**Applies to:** All apps

**Status:** Section heading only — no requirement text of its own; see 2.4.1–2.4.5 for checks.

## 2.4.1 iPhone apps on iPad

**Source text (verbatim):**
> 2.4.1 To ensure people get the most out of your app, iPhone apps should run on iPad whenever possible. We encourage you to consider building apps so customers can use them on all of their devices.

**Applies to:** iPhone apps

- **[2.4.1-01]** Does the iPhone app run properly on iPad (natively or in iPhone compatibility mode) where possible?
  - quote: "iPhone apps should run on iPad whenever possible"
  - surface: runtime
  - verify: Check `TARGETED_DEVICE_FAMILY` in project.pbxproj (1 = iPhone, 1,2 = iPhone+iPad) and `UIRequiredDeviceCapabilities` in Info.plist; run the app on an iPad simulator and exercise main flows for crashes or broken layout.
  - fix: Fix iPad layout/crash issues; consider adding iPad to supported destinations.

## 2.4.2 Power efficiency and device safety

**Source text (verbatim):**
> 2.4.2 Design your app to use power efficiently and be used in a way that does not risk damage to the device. Apps should not rapidly drain battery, generate excessive heat, or put unnecessary strain on device resources. For example, apps should not encourage placing the device under a mattress or pillow while charging or perform excessive write cycles to the solid state drive. Apps, including any third-party advertisements displayed within them, may not run unrelated background processes, such as cryptocurrency mining.

**Applies to:** All apps

- **[2.4.2-01]** Does the app avoid rapidly draining battery, generating excessive heat, or straining device resources?
  - quote: "Apps should not rapidly drain battery, generate excessive heat, or put unnecessary strain on device resources."
  - surface: runtime
  - verify: Profile with Instruments (Energy Log, Time Profiler) and Xcode debug gauges (CPU, energy) during typical use and while idle; grep for tight timers (`Timer.scheduledTimer` with very small intervals), continuous `CLLocationManager` high-accuracy updates, `isIdleTimerDisabled = true`.
  - fix: Reduce polling/timer frequency, lower location accuracy, stop work when idle/backgrounded.
- **[2.4.2-02]** Does the app avoid encouraging use that risks device damage (e.g. placing the device under a mattress or pillow while charging)?
  - quote: "apps should not encourage placing the device under a mattress or pillow while charging"
  - surface: code
  - verify: grep UI strings and onboarding copy for `mattress`, `pillow`, `under your`, instructions about device placement while charging.
  - fix: Remove such instructions.
- **[2.4.2-03]** Does the app avoid excessive write cycles to the storage drive?
  - quote: "perform excessive write cycles to the solid state drive"
  - surface: runtime
  - verify: Use Instruments (File Activity / Disk I/O) during typical use; grep for writes in loops/timers (`write(to:`, `FileHandle`, `UserDefaults.set` in high-frequency paths, Core Data saves per frame).
  - fix: Batch and debounce writes.
- **[2.4.2-04]** Do the app and any third-party ads it shows avoid running unrelated background processes such as cryptocurrency mining?
  - quote: "Apps, including any third-party advertisements displayed within them, may not run unrelated background processes, such as cryptocurrency mining."
  - surface: code
  - verify: grep for mining libraries/terms (`miner`, `hashrate`, `stratum`, `coinhive`, `monero`); review `UIBackgroundModes` and `BGTaskScheduler` tasks for unrelated work; list ad SDKs in Package.resolved/Podfile.lock.
  - fix: Remove unrelated background processing and offending SDKs.

## 2.4.3 Apple TV input

**Source text (verbatim):**
> 2.4.3 People should be able to use your Apple TV app without the need for hardware inputs beyond the Siri remote or third-party game controllers, but feel free to provide enhanced functionality when other peripherals are connected. If you require a game controller, make sure you clearly explain that in your metadata so customers know they need additional equipment to play.

**Applies to:** Apple TV (tvOS) apps

- **[2.4.3-01]** Can the Apple TV app be used with only the Siri Remote or third-party game controllers?
  - quote: "People should be able to use your Apple TV app without the need for hardware inputs beyond the Siri remote or third-party game controllers"
  - surface: runtime
  - verify: Run the tvOS app in the Apple TV simulator using only the Siri Remote; confirm every flow is usable; check code for dependence on other peripherals.
  - fix: Add Siri Remote / game controller support for all required interactions.
- **[2.4.3-02]** If a game controller is required, is that clearly explained in the metadata?
  - quote: "If you require a game controller, make sure you clearly explain that in your metadata"
  - surface: asc
  - verify: Check Info.plist `GCSupportsControllerUserInteraction` / `GCSupportedGameControllers` and any controller-required logic; if required, confirm App Store Connect description states a game controller is required.
  - fix: Add a clear "game controller required" statement to the description.

## 2.4.4 No device restart or unrelated settings changes

**Source text (verbatim):**
> 2.4.4 Apps should never suggest or require a restart of the device or modifications to system settings unrelated to the core functionality of the app. For example, don’t encourage users to turn off Wi-Fi, disable security features, etc.

**Applies to:** All apps

- **[2.4.4-01]** Does the app avoid suggesting or requiring a device restart?
  - quote: "Apps should never suggest or require a restart of the device"
  - surface: code
  - verify: grep UI strings for `restart your`, `reboot`, `restart the device`, `turn your device off`.
  - fix: Remove the restart prompt and fix the underlying issue in-app.
- **[2.4.4-02]** Does the app avoid asking users to change system settings unrelated to its core functionality (e.g. turning off Wi-Fi, disabling security features)?
  - quote: "modifications to system settings unrelated to the core functionality of the app. For example, don’t encourage users to turn off Wi-Fi, disable security features, etc."
  - surface: code
  - verify: grep UI strings for `turn off Wi-Fi`, `disable`, `Settings >`, `passcode`, `Face ID off`; review uses of `UIApplication.openSettingsURLString` and confirm each relates to the app’s own permissions/core features.
  - fix: Remove unrelated settings-change prompts.

## 2.4.5 Mac App Store requirements

**Source text (verbatim):**
> 2.4.5 Apps distributed via the Mac App Store have some additional requirements to keep in mind:
> - (i) They must be appropriately sandboxed, and follow macOS File System Documentation. They should also only use the appropriate macOS APIs for modifying user data stored by other apps (such as bookmarks, Address Book, or Calendar entries).
> - (ii) They must be packaged and submitted using technologies provided in Xcode; no third-party installers allowed. They must also be self-contained, single app installation bundles and cannot install code or resources in shared locations.
> - (iii) They may not auto-launch or have other code run automatically at startup or login without consent nor spawn processes that continue to run without consent after a user has quit the app. They should not automatically add their icons to the Dock or leave shortcuts on the user desktop.
> - (iv) They may not download or install standalone apps, kexts, additional code, or resources to add functionality or significantly change the app from what we see during the review process.
> - (v) They may not request escalation to root privileges or use setuid attributes.
> - (vi) They may not present a license screen at launch, require license keys, or implement their own copy protection.
> - (vii) They must use the Mac App Store to distribute updates; other update mechanisms are not allowed.
> - (viii) Apps should run on the currently shipping OS and may not use deprecated or optionally installed technologies (such as Java).
> - (ix) Apps must contain all language and localization support in a single app bundle.

**Applies to:** Apps distributed via the Mac App Store

**Related:** macOS File System Documentation

- **[2.4.5-01]** Is the Mac app appropriately sandboxed?
  - quote: "They must be appropriately sandboxed"
  - surface: code
  - verify: Check the macOS target’s `.entitlements` for `com.apple.security.app-sandbox` = true (and `ENABLE_APP_SANDBOX = YES`); review that only needed `com.apple.security.*` entitlements are present; `codesign -d --entitlements - <App>.app`.
  - fix: Enable App Sandbox and add only the required entitlements.
- **[2.4.5-02]** Does the Mac app follow macOS File System Documentation (writing only to appropriate locations)?
  - quote: "follow macOS File System Documentation"
  - surface: code
  - verify: grep for hard-coded paths (`/Library/`, `/usr/`, `/Applications/`, `~/`, `NSHomeDirectory()` concatenations) versus `FileManager.default.urls(for:in:)` container directories; check security-scoped bookmark use for user-selected files.
  - fix: Use container directories via FileManager APIs and user-selected file access.
- **[2.4.5-03]** Does the Mac app only use appropriate macOS APIs to modify user data stored by other apps (bookmarks, Address Book, Calendar)?
  - quote: "only use the appropriate macOS APIs for modifying user data stored by other apps (such as bookmarks, Address Book, or Calendar entries)"
  - surface: code
  - verify: grep for direct file access to other apps’ data (`~/Library/Safari`, `AddressBook`, `Calendars` paths, sqlite of other apps) versus use of `Contacts` (`CNContactStore`) and `EventKit` (`EKEventStore`).
  - fix: Replace direct file access with the framework APIs.
- **[2.4.5-04]** Is the Mac app packaged and submitted with Xcode technologies, with no third-party installer?
  - quote: "They must be packaged and submitted using technologies provided in Xcode; no third-party installers allowed."
  - surface: code
  - verify: Confirm the distribution path is Xcode Archive > Distribute App (or `xcodebuild -exportArchive`); search the repo for `.pkg` builders, `Packages`, `installer`, `InstallShield`, DMG scripts used for Mac App Store distribution.
  - fix: Distribute via Xcode archive/export to App Store Connect.
- **[2.4.5-05]** Is the Mac app a self-contained, single app bundle that does not install code or resources in shared locations?
  - quote: "They must also be self-contained, single app installation bundles and cannot install code or resources in shared locations."
  - surface: code
  - verify: grep for writes/copies to `/Library`, `/usr/local`, `~/Library/Application Support` of other bundles, `/Library/LaunchDaemons`, `/Library/Frameworks`, shared plug-in folders.
  - fix: Keep all code and resources inside the app bundle/container.
- **[2.4.5-06]** Does the Mac app avoid auto-launching or running code at startup/login without consent?
  - quote: "They may not auto-launch or have other code run automatically at startup or login without consent"
  - surface: code
  - verify: grep for `SMAppService`, `SMLoginItemSetEnabled`, LaunchAgents plists, `LSSharedFileList`; confirm login-item registration only follows an explicit user opt-in (e.g. a settings toggle defaulting off).
  - fix: Register login items only after explicit user consent.
- **[2.4.5-07]** Does the Mac app avoid spawning processes that keep running without consent after the user quits?
  - quote: "nor spawn processes that continue to run without consent after a user has quit the app"
  - surface: runtime
  - verify: grep for `Process()`, `NSTask`, `posix_spawn`, helper tools, `SMAppService.agent`; quit the app and check Activity Monitor / `ps aux` for remaining helper processes.
  - fix: Terminate helpers on quit or obtain explicit consent for persistent helpers.
- **[2.4.5-08]** Does the Mac app avoid automatically adding its icon to the Dock or leaving desktop shortcuts?
  - quote: "They should not automatically add their icons to the Dock or leave shortcuts on the user desktop."
  - surface: code
  - verify: grep for `com.apple.dock` defaults writes, `persistent-apps`, writes to `~/Desktop` or `.desktopDirectory`, alias/symlink creation.
  - fix: Remove automatic Dock/desktop modifications.
- **[2.4.5-09]** Does the Mac app avoid downloading or installing standalone apps, kexts, additional code, or resources that add functionality or significantly change the app after review?
  - quote: "They may not download or install standalone apps, kexts, additional code, or resources to add functionality or significantly change the app from what we see during the review process."
  - surface: code
  - verify: grep for downloads of `.app`, `.kext`, `.dylib`, `.bundle`, `.framework`, scripts, `dlopen`, `NSBundle(path:).load()`, `Bundle.load`, `JSContext` evaluating downloaded code.
  - fix: Ship all functionality in the reviewed bundle.
- **[2.4.5-10]** Does the Mac app avoid requesting root privileges or using setuid attributes?
  - quote: "They may not request escalation to root privileges or use setuid attributes."
  - surface: code
  - verify: grep for `AuthorizationExecuteWithPrivileges`, `SMJobBless`, `AuthorizationCreate` with admin rights, `sudo`, `setuid`, `chmod u+s`, `osascript ... with administrator privileges`.
  - fix: Remove privilege escalation and setuid usage.
- **[2.4.5-11]** Does the Mac app avoid a launch license screen, license keys, and custom copy protection?
  - quote: "They may not present a license screen at launch, require license keys, or implement their own copy protection."
  - surface: code
  - verify: grep for `license key`, `serial number`, `activation`, `EULA` shown at launch, licensing SDKs (Paddle, Gumroad license, DevMate), custom receipt-based copy protection beyond Apple receipt validation; run the app to confirm no launch license screen.
  - fix: Remove license-key/activation flows and custom copy protection.
- **[2.4.5-12]** Does the Mac app use only the Mac App Store for updates (no other update mechanism)?
  - quote: "They must use the Mac App Store to distribute updates; other update mechanisms are not allowed."
  - surface: code
  - verify: grep Package.resolved/Podfile/Cartfile and source for `Sparkle`, `SUUpdater`, `SPUStandardUpdaterController`, `SUFeedURL` in Info.plist, custom "check for updates" code.
  - fix: Remove Sparkle/custom updaters from the Mac App Store build.
- **[2.4.5-13]** Does the Mac app run on the currently shipping macOS and avoid deprecated or optionally installed technologies (such as Java)?
  - quote: "Apps should run on the currently shipping OS and may not use deprecated or optionally installed technologies (such as Java)."
  - surface: code
  - verify: Build with the current Xcode/SDK and review deprecation warnings; grep for Java/JRE dependencies, `JavaVM.framework`, and other deprecated frameworks; run on the current macOS.
  - fix: Replace deprecated/optional technologies and fix issues on the current macOS.
- **[2.4.5-14]** Does the Mac app contain all language and localization support in a single app bundle?
  - quote: "Apps must contain all language and localization support in a single app bundle."
  - surface: code
  - verify: Confirm all `.lproj` / String Catalog localizations are inside the main app bundle; grep for downloaded language packs or separate localization bundles.
  - fix: Include all localizations in the app bundle.

## 2.5 Software Requirements

**Source text (verbatim):**
> 2.5 Software Requirements

**Applies to:** All apps

**Status:** Section heading only — no requirement text of its own; see 2.5.1–2.5.19 for checks.

## 2.5.1 Public APIs, current OS, intended use

**Source text (verbatim):**
> 2.5.1 Apps may only use public APIs and must run on the currently shipping OS. Learn more about public APIs. Keep your apps up-to-date and make sure you phase out any deprecated features, frameworks or technologies that will no longer be supported in future versions of an OS. Apps should use APIs and frameworks for their intended purposes and indicate that integration in their app description. For example, the HomeKit framework should provide home automation services; and HealthKit should be used for health and fitness purposes and integrate with the Health app.

**Applies to:** All apps

**Related:** public APIs

- **[2.5.1-01]** Does the app use only public APIs?
  - quote: "Apps may only use public APIs"
  - surface: code
  - verify: grep for private API usage: `NSClassFromString(`/`NSSelectorFromString(` with underscore-prefixed or undocumented names, `performSelector:` on private selectors, `valueForKey:@"_`, `dlopen`/`dlsym` of system frameworks, `/System/Library/PrivateFrameworks`, `UIStatusBar`/`_UI` classes; run `nm -u` on the binary for private symbols.
  - fix: Replace private API calls with public alternatives.
- **[2.5.1-02]** Does the app run on the currently shipping OS?
  - quote: "must run on the currently shipping OS"
  - surface: runtime
  - verify: Build with the current Xcode/SDK and run on a simulator/device with the current OS release; exercise main flows.
  - fix: Fix issues on the current OS.
- **[2.5.1-03]** Have deprecated features, frameworks, or technologies that will no longer be supported been phased out?
  - quote: "make sure you phase out any deprecated features, frameworks or technologies that will no longer be supported in future versions of an OS"
  - surface: code
  - verify: Build and review deprecation warnings; grep for `UIWebView`, `AddressBook` framework, `ALAssetsLibrary`, `UIAlertView`, `UIActionSheet`, `openURL:` (deprecated), `NSURLConnection`, `UILaunchImages`, and similar deprecated APIs.
  - fix: Migrate to the replacement APIs.
- **[2.5.1-04]** Are APIs and frameworks used for their intended purposes, and is that integration indicated in the app description?
  - quote: "Apps should use APIs and frameworks for their intended purposes and indicate that integration in their app description."
  - surface: code
  - verify: List capabilities/frameworks from entitlements and imports (`HealthKit`, `HomeKit`, `CarPlay`, `ClassKit`, `NFC`, `ShazamKit`, etc.); confirm each is used for its intended purpose (e.g. HealthKit for health and fitness, integrating with Health; HomeKit for home automation) and that the App Store Connect description mentions the integration.
  - fix: Remove frameworks used for unintended purposes; mention genuine integrations in the description.

## 2.5.2 Self-contained bundles; no downloaded executable code

**Source text (verbatim):**
> 2.5.2 Apps should be self-contained in their bundles, and may not read or write data outside the designated container area, nor may they download, install, or execute code which introduces or changes features or functionality of the app, including other apps. Educational apps designed to teach, develop, or allow students to test executable code may, in limited circumstances, download code provided that such code is not used for other purposes. Such apps must make the source code provided by the app completely viewable and editable by the user.

**Applies to:** All apps; the last two sentences apply to educational apps that teach or test executable code

- **[2.5.2-01]** Does the app avoid reading or writing data outside its designated container?
  - quote: "may not read or write data outside the designated container area"
  - surface: code
  - verify: grep for absolute file paths (`/var/mobile`, `/private/var`, `/Library`, `/User`), `..` path traversal, file access not derived from `FileManager.default.urls(for:in:)`, `containerURL(forSecurityApplicationGroupIdentifier:)` or user-picked documents.
  - fix: Restrict file I/O to the app container, app groups, or user-selected files.
- **[2.5.2-02]** Does the app avoid downloading, installing, or executing code that introduces or changes its features or functionality (or other apps’)?
  - quote: "nor may they download, install, or execute code which introduces or changes features or functionality of the app, including other apps"
  - surface: code
  - verify: grep for `dlopen`, `NSBundle`/`Bundle(path:)` `.load()`, `JSContext.evaluateScript` with remote scripts, `WKWebView.evaluateJavaScript` with downloaded logic, Lua/Python interpreters fed downloaded code, hot-patching SDKs (JSPatch, Rollout, DynamicCocoa); check whether any downloaded payload alters features.
  - fix: Remove hot-patching/remote code execution; ship features in a reviewed build.
- **[2.5.2-03]** If the app is an educational app that downloads executable code, is that code used only for teaching/testing and is the source code completely viewable and editable by the user?
  - quote: "Such apps must make the source code provided by the app completely viewable and editable by the user."
  - surface: runtime
  - verify: If the app downloads code for students, run it and confirm every downloaded code item can be viewed and edited in the app before execution, and is not used for other purposes.
  - fix: Expose full view/edit of the downloaded source; stop using it for any other purpose.

## 2.5.3 No harmful code

**Source text (verbatim):**
> 2.5.3 Apps that transmit viruses, files, computer code, or programs that may harm or disrupt the normal operation of the operating system and/or hardware features, including Push Notifications and Game Center, will be rejected. Egregious violations and repeat behavior will result in removal from the Apple Developer Program.

**Applies to:** All apps

- **[2.5.3-01]** Does the app avoid transmitting viruses, files, code, or programs that may harm or disrupt the OS or hardware features, including Push Notifications and Game Center?
  - quote: "Apps that transmit viruses, files, computer code, or programs that may harm or disrupt the normal operation of the operating system and/or hardware features, including Push Notifications and Game Center, will be rejected."
  - surface: code
  - verify: Review code that sends files/code to other devices or users (sharing, AirDrop, Multipeer, server push payloads) and push/Game Center usage for abuse (notification spam loops, malformed payloads); scan bundled third-party binaries/SDKs.
  - fix: Remove the harmful transmission behavior or SDK.

## 2.5.4 Background services

**Source text (verbatim):**
> 2.5.4 Multitasking apps may only use background services for their intended purposes: VoIP, audio playback, location, task completion, local notifications, etc.

**Applies to:** Apps using background services

- **[2.5.4-01]** Is each declared background mode used only for its intended purpose?
  - quote: "Multitasking apps may only use background services for their intended purposes: VoIP, audio playback, location, task completion, local notifications, etc."
  - surface: code
  - verify: Read `UIBackgroundModes` in Info.plist (`audio`, `location`, `voip`, `fetch`, `remote-notification`, `processing`, `bluetooth-central`, etc.) and Signing & Capabilities > Background Modes. For each, confirm matching use: `audio` → real audible playback via `AVAudioSession`/`AVPlayer` (not silent audio to stay alive); `location` → user-facing location feature with `CLLocationManager` and `allowsBackgroundLocationUpdates`; `voip` → CallKit/PushKit VoIP; `processing`/`fetch` → `BGTaskScheduler` tasks.
  - fix: Remove unused or misused background modes from Info.plist and capabilities.

## 2.5.5 IPv6

**Source text (verbatim):**
> 2.5.5 Apps must be fully functional on IPv6-only networks.

**Applies to:** All apps

- **[2.5.5-01]** Is the app fully functional on an IPv6-only network?
  - quote: "Apps must be fully functional on IPv6-only networks."
  - surface: runtime
  - verify: grep for hard-coded IPv4 literals (regex `\b\d{1,3}(\.\d{1,3}){3}\b`), `inet_addr`, `AF_INET` without `AF_INET6`, `gethostbyname`, `sockaddr_in` usage; test on a NAT64 network (macOS Internet Sharing "Create NAT64 Network") and exercise all network features.
  - fix: Use hostnames and high-level APIs (`URLSession`, `Network.framework`); remove IPv4 literals and IPv4-only socket code.

## 2.5.6 WebKit for web browsing

**Source text (verbatim):**
> 2.5.6 Apps that browse the web must use the appropriate WebKit framework and WebKit JavaScript. You may apply for an entitlement to use an alternative web browser engine in your app. Learn more about these entitlements for the EU and Japan.

**Applies to:** Apps that browse the web

**Related:** entitlements for the EU and Japan

- **[2.5.6-01]** Does the app use the appropriate WebKit framework and WebKit JavaScript for web browsing (unless it holds an alternative browser engine entitlement)?
  - quote: "Apps that browse the web must use the appropriate WebKit framework and WebKit JavaScript."
  - surface: code
  - verify: grep for web views: `WKWebView`, `SFSafariViewController`, `ASWebAuthenticationSession` (OK) versus bundled engines (Chromium, GeckoView, V8 used to render web content); if an alternative engine is used, check entitlements for `com.apple.developer.web-browser-engine.*`.
  - fix: Switch to WKWebView/SFSafariViewController, or obtain the alternative browser engine entitlement.

## 2.5.7 Intentionally omitted

**Source text (verbatim):**
> 2.5.7 Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 2.5.8 Alternate home screen environments

**Source text (verbatim):**
> 2.5.8 Apps that create alternate desktop/home screen environments will be rejected.

**Applies to:** All apps

- **[2.5.8-01]** Does the app avoid creating an alternate desktop/home screen environment?
  - quote: "Apps that create alternate desktop/home screen environments will be rejected."
  - surface: runtime
  - verify: Review the app’s purpose and UI: flag launcher-style grids of other apps, home-screen replacements, or "desktop" environments; grep for `canOpenURL` loops over many app URL schemes and `LSApplicationQueriesSchemes` lists of many third-party apps.
  - fix: manual — requires developer decision/legal/business action (redesign the product concept).

## 2.5.9 Standard switches and UI behaviors

**Source text (verbatim):**
> 2.5.9 Apps that alter or disable the functions of standard switches, such as the Volume Up/Down and Ring/Silent switches, or other native user interface elements or behaviors will be rejected. For example, apps should not block links out to other apps or other features that users would expect to work a certain way.

**Applies to:** All apps

- **[2.5.9-01]** Does the app avoid altering or disabling standard switches such as Volume Up/Down and Ring/Silent?
  - quote: "Apps that alter or disable the functions of standard switches, such as the Volume Up/Down and Ring/Silent switches"
  - surface: code
  - verify: grep for volume-button hijacking: KVO on `AVAudioSession.outputVolume` used to trigger non-volume actions, hidden `MPVolumeView` used to suppress the HUD/reset volume; run the app and press hardware buttons.
  - fix: Remove the code that alters or disables the standard switch behavior.
- **[2.5.9-02]** Does the app avoid altering or disabling native UI elements or behaviors, including blocking links out to other apps?
  - quote: "or other native user interface elements or behaviors will be rejected. For example, apps should not block links out to other apps or other features that users would expect to work a certain way."
  - surface: runtime
  - verify: grep `WKNavigationDelegate` `decidePolicyFor` implementations that cancel external URLs without opening them, and other code that overrides native UI behaviors users would expect to work a certain way; tap external links in the app and confirm they open.
  - fix: Allow external links and native behaviors to work as expected.

## 2.5.10 Intentionally omitted

**Source text (verbatim):**
> 2.5.10 Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 2.5.11 SiriKit and Shortcuts

**Source text (verbatim):**
> 2.5.11 SiriKit and Shortcuts
> - (i) Apps integrating SiriKit and Shortcuts should only sign up for intents they can handle without the support of an additional app and that users would expect from the stated functionality. For example, if your app is a meal planning app, you should not incorporate an intent to start a workout, even if the app shares integration with a fitness app.
> - (ii) Ensure that the vocabulary and phrases in your plist pertains to your app and the Siri functionality of the intents the app has registered for. Aliases must relate directly to your app or company name and should not be generic terms or include third-party app names or services.
> - (iii) Resolve the Siri request or Shortcut in the most direct way possible and do not insert ads or other marketing between the request and its fulfillment. Only request a disambiguation when required to complete the task (such as asking the user to specify a particular type of workout).

**Applies to:** Apps integrating SiriKit and Shortcuts

- **[2.5.11-01]** Does the app only register intents it can handle without another app and that users would expect from its stated functionality?
  - quote: "should only sign up for intents they can handle without the support of an additional app and that users would expect from the stated functionality"
  - surface: code
  - verify: List intents: `IntentsSupported` in Intents extension Info.plist, `.intentdefinition` files, `AppIntent` / `AppShortcutsProvider` types, `INExtension` handlers; compare each with the app’s stated functionality and confirm each handler completes without another app.
  - fix: Remove intents unrelated to the app or that depend on another app.
- **[2.5.11-02]** Does the vocabulary and phrases in the plist pertain to the app and its registered Siri intents?
  - quote: "Ensure that the vocabulary and phrases in your plist pertains to your app and the Siri functionality of the intents the app has registered for."
  - surface: code
  - verify: Inspect `AppIntentVocabulary.plist` (`ParameterVocabularies`, `IntentPhrases`) and `AppShortcutsProvider` phrases; confirm each relates to the app and its registered intents.
  - fix: Remove unrelated vocabulary/phrases.
- **[2.5.11-03]** Do aliases relate directly to the app or company name, without generic terms or third-party app/service names?
  - quote: "Aliases must relate directly to your app or company name and should not be generic terms or include third-party app names or services."
  - surface: code
  - verify: Check `INAlternativeAppNames` in Info.plist and App Shortcut phrase app-name usages for generic words or third-party names.
  - fix: Replace aliases with names directly tied to the app/company.
- **[2.5.11-04]** Are Siri requests/Shortcuts resolved directly, without ads or marketing between request and fulfillment, and with disambiguation only when required?
  - quote: "Resolve the Siri request or Shortcut in the most direct way possible and do not insert ads or other marketing between the request and its fulfillment. Only request a disambiguation when required to complete the task"
  - surface: runtime
  - verify: Review `perform()` / `handle(intent:)` implementations for ad/paywall/marketing presentation or unnecessary `requestDisambiguation`/`resolve...` prompts; run each Shortcut in the Shortcuts app.
  - fix: Remove ads/marketing from intent flows; drop unnecessary disambiguation.

## 2.5.12 CallKit and SMS Fraud Extensions

**Source text (verbatim):**
> 2.5.12 Apps using CallKit or including an SMS Fraud Extension should only block phone numbers that are confirmed spam. Apps that include call-, SMS-, and MMS- blocking functionality or spam identification must clearly identify these features in their marketing text and explain the criteria for their blocked and spam lists. You may not use the data accessed via these tools for any purpose not directly related to operating or improving your app or extension (for example, you may not use, share, or sell it for tracking purposes, create user profiles, etc.).

**Applies to:** Apps using CallKit or including an SMS Fraud Extension; apps with call/SMS/MMS blocking or spam identification

- **[2.5.12-01]** Does the app only block phone numbers that are confirmed spam?
  - quote: "should only block phone numbers that are confirmed spam"
  - surface: manual
  - verify: Code: find `CXCallDirectoryProvider` (`addBlockingEntry`) and `ILMessageFilterExtension` targets; review the source of blocked numbers. Ask the developer how numbers are confirmed as spam.
  - fix: manual — requires developer decision/legal/business action (restrict block lists to confirmed spam).
- **[2.5.12-02]** Does the marketing text clearly identify call/SMS/MMS blocking or spam identification features and explain the criteria for the blocked and spam lists?
  - quote: "must clearly identify these features in their marketing text and explain the criteria for their blocked and spam lists"
  - surface: asc
  - verify: If a Call Directory or Message Filter extension exists, read App Store Connect description/promotional text for a clear feature statement and an explanation of list criteria.
  - fix: Add feature identification and list criteria to the description.
- **[2.5.12-03]** Is data accessed via these tools used only for operating or improving the app/extension (not for tracking, profiles, sharing, or sale)?
  - quote: "You may not use the data accessed via these tools for any purpose not directly related to operating or improving your app or extension"
  - surface: code
  - verify: Inspect Call Directory / Message Filter extension code and `ILNetworkResponse` server handling for forwarding numbers/message content to analytics, ads, or third-party SDKs; check privacy policy.
  - fix: Remove non-essential use/sharing of that data.

## 2.5.13 Facial recognition for authentication

**Source text (verbatim):**
> 2.5.13 Apps using facial recognition for account authentication must use LocalAuthentication (and not ARKit or other facial recognition technology) where possible, and must use an alternate authentication method for users under 13 years old.

**Applies to:** Apps using facial recognition for account authentication

- **[2.5.13-01]** Does facial-recognition account authentication use LocalAuthentication (not ARKit or other face recognition) where possible?
  - quote: "must use LocalAuthentication (and not ARKit or other facial recognition technology) where possible"
  - surface: code
  - verify: grep for `LAContext`, `evaluatePolicy` (good) versus `ARFaceTrackingConfiguration`, `VNDetectFaceRectanglesRequest`, third-party face-auth SDKs used in login flows; check `NSFaceIDUsageDescription` in Info.plist when LocalAuthentication is used.
  - fix: Use `LAContext` biometrics for face-based authentication.
- **[2.5.13-02]** Is an alternate authentication method available for users under 13?
  - quote: "must use an alternate authentication method for users under 13 years old"
  - surface: runtime
  - verify: Confirm the login flow offers a non-facial method (passcode/password/Sign in with Apple) and that users under 13 are routed to it.
  - fix: Add a non-facial authentication path for users under 13.

## 2.5.14 Consent and indication when recording

**Source text (verbatim):**
> 2.5.14 Apps must request explicit user consent and provide a clear visual and/or audible indication when recording, logging, or otherwise making a record of user activity. This includes any use of the device camera, microphone, screen recordings, or other user inputs.

**Applies to:** Apps that record, log, or otherwise make a record of user activity

- **[2.5.14-01]** Does the app request explicit user consent before recording or logging user activity (camera, microphone, screen recordings, other inputs)?
  - quote: "Apps must request explicit user consent"
  - surface: code
  - verify: grep for `AVCaptureSession`, `AVAudioRecorder`, `AVAudioEngine` input taps, `SFSpeechRecognizer`, `RPScreenRecorder`, `ReplayKit`, keystroke/touch logging, session replay SDKs (e.g. FullStory, Smartlook, UXCam, LogRocket); confirm `NSCameraUsageDescription`/`NSMicrophoneUsageDescription`/`NSSpeechRecognitionUsageDescription` exist and that recording starts only after an explicit user action/consent.
  - fix: Add an explicit consent step before recording/logging and required usage descriptions.
- **[2.5.14-02]** Does the app show a clear visual and/or audible indication while recording?
  - quote: "provide a clear visual and/or audible indication when recording, logging, or otherwise making a record of user activity"
  - surface: runtime
  - verify: Start each recording feature and confirm an in-app indicator (recording badge, timer, red dot, waveform) is visible for the whole duration, including session-replay logging.
  - fix: Add a persistent recording indicator in the UI.

## 2.5.15 Files app and iCloud documents

**Source text (verbatim):**
> 2.5.15 Apps that enable users to view and select files should include items from the Files app and the user’s iCloud documents.

**Applies to:** Apps that enable users to view and select files

- **[2.5.15-01]** Does the app’s file selection include items from the Files app and the user’s iCloud documents?
  - quote: "Apps that enable users to view and select files should include items from the Files app and the user’s iCloud documents."
  - surface: code
  - verify: grep for file pickers: `UIDocumentPickerViewController`, `.fileImporter`, `UIDocumentBrowserViewController`, `NSOpenPanel` (good) versus custom pickers listing only the app sandbox; run the picker and confirm Files/iCloud Drive locations appear.
  - fix: Use the system document picker / `.fileImporter`.

## 2.5.16 Widgets, extensions, notifications, App Clips

**Source text (verbatim):**
> 2.5.16 Widgets, extensions, and notifications should be related to the content and functionality of your app.
> - (a) Additionally, all App Clip features and functionality must be included in the main app binary. App Clips cannot contain advertising.

**Applies to:** Apps with widgets, extensions, or notifications; (a) applies to apps with App Clips

- **[2.5.16-01]** Are widgets, extensions, and notifications related to the app’s content and functionality?
  - quote: "Widgets, extensions, and notifications should be related to the content and functionality of your app."
  - surface: code
  - verify: List extension targets (WidgetKit, Share, Action, Keyboard, Notification Content/Service, Live Activities) and notification content (`UNMutableNotificationContent` bodies, server push templates); confirm each relates to the app’s functionality.
  - fix: Remove or rework unrelated widgets/extensions/notifications.
- **[2.5.16-02]** Are all App Clip features and functionality included in the main app binary?
  - quote: "all App Clip features and functionality must be included in the main app binary"
  - surface: code
  - verify: If an App Clip target exists, compare its source files/features with the main app target (target membership in project.pbxproj); confirm every App Clip flow exists in the full app.
  - fix: Add missing App Clip features to the main app.
- **[2.5.16-03]** Is the App Clip free of advertising?
  - quote: "App Clips cannot contain advertising."
  - surface: code
  - verify: Check App Clip target dependencies and imports for ad SDKs (`GoogleMobileAds`, `AppLovinSDK`, `FBAudienceNetwork`, `UnityAds`, `IronSource`, etc.) and ad views.
  - fix: Remove ad SDKs and ad UI from the App Clip target.

## 2.5.17 Matter

**Source text (verbatim):**
> 2.5.17 Apps that support Matter must use Apple’s support framework for Matter to initiate pairing. In addition, if you choose to use any Matter software component in your app other than the Matter SDK provided by Apple, the software component must be certified by the Connectivity Standards Alliance for the platform it runs on.

**Applies to:** Apps that support Matter

- **[2.5.17-01]** Does the app use Apple’s support framework for Matter to initiate pairing?
  - quote: "Apps that support Matter must use Apple’s support framework for Matter to initiate pairing."
  - surface: code
  - verify: grep for `MatterSupport`, `MatterAddDeviceRequest` (good) versus custom commissioning flows initiating pairing; check `com.apple.developer.matter.allow-setup-payload` entitlement where applicable.
  - fix: Initiate pairing through `MatterAddDeviceRequest`.
- **[2.5.17-02]** Is any non-Apple Matter software component certified by the Connectivity Standards Alliance for its platform?
  - quote: "if you choose to use any Matter software component in your app other than the Matter SDK provided by Apple, the software component must be certified by the Connectivity Standards Alliance for the platform it runs on"
  - surface: manual
  - verify: List third-party Matter libraries in Package.resolved/Podfile.lock/vendored code (e.g. connectedhomeip/CHIP); ask the developer for CSA certification evidence.
  - fix: manual — requires developer decision/legal/business action (use Apple’s Matter SDK or obtain CSA certification).

## 2.5.18 Advertising

**Source text (verbatim):**
> 2.5.18 Display advertising should be limited to your main app binary, and should not be included in extensions, App Clips, widgets, notifications, keyboards, watchOS apps, etc. Ads displayed in an app must be appropriate for the app’s age rating, allow the user to see all information used to target them for that ad (without requiring the user to leave the app), and may not engage in targeted or behavioral advertising based on sensitive user data such as health/medical data (such as from the HealthKit APIs), school and classroom data (such as from ClassKit), or from kids (such as from apps in the App Store’s Kids Category), etc. Interstitial ads or ads that interrupt or block the user experience must clearly indicate that they are an ad, must not manipulate or trick users into tapping into them, and must provide easily accessible and visible close/skip buttons large enough for people to easily dismiss the ad. Apps that contain ads must also include the ability for users to report any inappropriate or age-inappropriate ads.

**Applies to:** Apps that display advertising

- **[2.5.18-01]** Is display advertising limited to the main app binary (none in extensions, App Clips, widgets, notifications, keyboards, watchOS apps, etc.)?
  - quote: "Display advertising should be limited to your main app binary, and should not be included in extensions, App Clips, widgets, notifications, keyboards, watchOS apps, etc."
  - surface: code
  - verify: For every non-main target in project.pbxproj (extensions, widgets, App Clip, keyboard, watchOS), check linked frameworks/packages and imports for ad SDKs and ad views; check notification content for ads.
  - fix: Remove ad SDKs/ads from non-main targets.
- **[2.5.18-02]** Are ads appropriate for the app’s age rating?
  - quote: "Ads displayed in an app must be appropriate for the app’s age rating"
  - surface: code
  - verify: Check ad SDK configuration for content rating limits (e.g. AdMob `maxAdContentRating`, `tagForChildDirectedTreatment`, `tagForUnderAgeOfConsent`) against the App Store Connect age rating; observe ads at runtime.
  - fix: Set ad content-rating filters matching the app’s age rating.
- **[2.5.18-03]** Can users see all information used to target them for an ad without leaving the app?
  - quote: "allow the user to see all information used to target them for that ad (without requiring the user to leave the app)"
  - surface: runtime
  - verify: Tap the ad’s info/AdChoices control; confirm targeting information is shown in-app (not only via external browser).
  - fix: Use ad SDK in-app ad-info disclosure or implement an in-app "Why am I seeing this ad" view.
- **[2.5.18-04]** Does the app avoid targeted or behavioral advertising based on sensitive data (health/medical, HealthKit, ClassKit school data, kids’ data)?
  - quote: "may not engage in targeted or behavioral advertising based on sensitive user data such as health/medical data (such as from the HealthKit APIs), school and classroom data (such as from ClassKit), or from kids (such as from apps in the App Store’s Kids Category)"
  - surface: code
  - verify: If the app uses `HealthKit`, `ClassKit`, or is in the Kids Category and shows ads: check that health/school/kid data is not passed to ad SDKs (custom targeting keywords, user properties) and that ads are not targeted or behavioral based on that data (e.g. request non-personalized ads).
  - fix: Disable personalized/behavioral ads and stop passing sensitive data to ad networks.
- **[2.5.18-05]** Do interstitial or interrupting ads clearly indicate they are ads and avoid tricking users into tapping them?
  - quote: "Interstitial ads or ads that interrupt or block the user experience must clearly indicate that they are an ad, must not manipulate or trick users into tapping into them"
  - surface: runtime
  - verify: Trigger interstitials; confirm an "Ad" label is visible and that ad placement does not coincide with expected tap targets (e.g. ads appearing under a button being tapped).
  - fix: Label ads clearly and move/time interstitials to avoid accidental taps.
- **[2.5.18-06]** Do interrupting ads provide easily accessible, visible close/skip buttons large enough to dismiss easily?
  - quote: "must provide easily accessible and visible close/skip buttons large enough for people to easily dismiss the ad"
  - surface: runtime
  - verify: Trigger interstitials/rewarded/custom full-screen ads; confirm a clearly visible, easily accessible close/skip control large enough to dismiss the ad easily is available.
  - fix: Use ad formats/SDK settings with accessible close buttons; enlarge custom close buttons.
- **[2.5.18-07]** Can users report inappropriate or age-inappropriate ads?
  - quote: "Apps that contain ads must also include the ability for users to report any inappropriate or age-inappropriate ads."
  - surface: runtime
  - verify: Look for an in-app "Report ad" mechanism (ad SDK feedback/report menu, or an in-app report option linked to support); grep for `report ad` strings.
  - fix: Add a "Report this ad" option (SDK-provided or custom contact flow).

## 2.5.19 No hidden or undocumented features

**Source text (verbatim):**
> 2.5.19 Don’t include any hidden, dormant, or undocumented features in your app; your app’s functionality should be clear to end users and App Review. Attempting to hide undocumented features in your app binary, such as through code obfuscation or other methods, is grounds for removal of your app from the App Store and termination of your developer account.

**Applies to:** All apps

- **[2.5.19-01]** Is the app free of hidden, dormant, or undocumented features (e.g. features enabled remotely after review)?
  - quote: "Don’t include any hidden, dormant, or undocumented features in your app"
  - surface: code
  - verify: grep for remote-config/feature-flag gates (`RemoteConfig`, `featureFlag`, `isFeatureEnabled`, server `enabled` keys), date-based switches, secret gestures/codes, region/IP-based switches; list every gated feature and confirm it is documented in the description or review notes.
  - fix: Remove hidden features, or document and enable them for review in Notes for Review.
- **[2.5.19-02]** Is the app’s functionality clear to end users and App Review?
  - quote: "your app’s functionality should be clear to end users and App Review"
  - surface: asc
  - verify: Confirm App Store Connect description and review notes cover all functionality found in the code.
  - fix: Document all functionality in the description and review notes.
- **[2.5.19-03]** Does the app avoid hiding undocumented features through code obfuscation or other methods?
  - quote: "Attempting to hide undocumented features in your app binary, such as through code obfuscation or other methods"
  - surface: code
  - verify: Check build phases and dependencies for obfuscation tools (SwiftShield, iXGuard, obfuscator-llvm) and for encoded/encrypted strings or code paths that unlock features; review what obfuscated code does.
  - fix: Remove obfuscation that conceals features; document all features.
