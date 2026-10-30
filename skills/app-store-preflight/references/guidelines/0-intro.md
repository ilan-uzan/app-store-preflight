# App Review Guidelines — Introduction, Before You Submit, After You Submit
Source: https://developer.apple.com/app-store/review/guidelines/  
Retrieved: 2026-10-30

Note: the source page states "Last Updated: October 16, 2026". These sections are not numbered guidelines; units are organized per heading and per bullet topic. The numbered guidelines (1–5) are in the other files of this directory.

## INTRO Introduction

**Source text (verbatim):**
> Apps are changing the world, enriching people’s lives, and enabling developers like you to innovate like never before. As a result, the App Store has grown into an exciting and vibrant ecosystem for millions of developers and more than a billion users. Whether you are a first-time developer or a large team of experienced programmers, we are excited that you are creating apps for our platforms, and want to help you understand our guidelines so you can be confident your app will get through the review process quickly.
>
> The guiding principle of the App Store is simple—we want to provide a safe experience for users to get apps and a great opportunity for all developers to be successful. We do this by offering a highly curated App Store where every app is reviewed by experts and an editorial team helps users discover new apps every day. We also scan each app for malware and other software that may impact user safety, security, and privacy. These efforts have made Apple’s platforms the safest for consumers around the world.
>
> In some markets and on certain platforms, developers can also distribute notarized apps from alternative app marketplaces and directly from their website. Learn more about alternative app marketplaces, Web Distribution, and Notarization for iOS and iPadOS apps. You can see which guidelines apply to Notarization for iOS and iPadOS apps by clicking on “Highlight Notarization Review Guidelines Only” in the menu to the left.
>
> For everything else there is always the open Internet. If the App Store model and guidelines or alternative distribution and Notarization for iOS and iPadOS apps are not best for your app or business idea that’s okay, we provide Safari for a great web experience too.
>
> On the following pages you will find our latest guidelines arranged into five clear sections: Safety, Performance, Business, Design, and Legal. The App Store is always changing and improving to keep up with the needs of our customers and our products. Your apps should change and improve as well in order to stay on the App Store.
>
> We hope these guidelines help you sail through the review process, and that approvals and rejections remain consistent across the board. This is a living document; new apps presenting new questions may result in new rules at any time. Perhaps your app will trigger this. We love this stuff too, and honor what you do. We’re really trying our best to create the best platform in the world for you to express your talents and make a living, too.

**Applies to:** All apps

**Related:** alternative app marketplaces; Web Distribution; Notarization for iOS and iPadOS apps; Safari

- **[INTRO-01]** (Apple states it scans every app) Is the app free of malware and other software that may impact user safety, security, or privacy?
  - quote: "We also scan each app for malware and other software that may impact user safety, security, and privacy."
  - surface: code
  - verify: Inventory all linked binaries/frameworks/SDKs (Podfile.lock, Package.resolved, Cartfile.resolved, embedded .framework/.xcframework, vendored static libs). Flag any SDK of unknown provenance, obfuscated binary blobs, or code that downloads and executes payloads. Confirm each third-party dependency comes from a known, reputable source.
  - fix: Remove unknown or untrusted binaries/SDKs; replace with vetted sources.
- **[INTRO-04]** (Advisory — Apple says apps "should" change and improve; not a stated rejection rule) Is the app being maintained so it changes and improves over time?
  - quote: "Your apps should change and improve as well in order to stay on the App Store."
  - surface: manual
  - verify: Check in App Store Connect (App > App Store tab > version history) the date of the last released version; ask the developer whether the app is actively maintained.
  - fix: manual — requires developer decision/legal/business action

## INTRO.1 Keeping kids and teens safe

**Source text (verbatim):**
> A few other points to keep in mind about distributing your app on our platforms:
> - We have lots of kids and teens downloading apps to stay in touch, explore creativity, learn, and grow their independence. Keeping them safe is something we take seriously. Parental controls give parents a powerful way to manage what their child can access and when — but you have to do your part too. Make sure kids are getting age-appropriate experiences inside your app.

**Applies to:** All apps

- **[INTRO-05]** Does the app ensure kids get age-appropriate experiences inside the app?
  - quote: "Make sure kids are getting age-appropriate experiences inside your app."
  - surface: asc
  - verify: In App Store Connect > App Information > Age Rating, review every questionnaire answer against actual app content (user-generated content, web access, mature themes, gambling, etc.). Exercise the app at runtime to confirm content matches the declared rating.
  - fix: Correct the age rating questionnaire answers, or gate/remove content that is not appropriate for the declared rating.

## INTRO.2 Apps for family and friends only

**Source text (verbatim):**
> - The App Store is a great way to reach hundreds of millions of people around the world. If you build an app that you just want to show to family and friends, the App Store isn’t the best way to do that. Consider using Xcode to install your app on a device for free or use Ad Hoc distribution available to Apple Developer Program members. If you’re just getting started, learn more about the Apple Developer Program.

**Applies to:** Apps intended only to be shown to family and friends

**Related:** Xcode; Ad Hoc distribution; Apple Developer Program

- **[INTRO-06]** (Advisory — Apple says the App Store "isn’t the best way", not that such apps are rejected) Is the app intended for a wider audience than just family and friends?
  - quote: "If you build an app that you just want to show to family and friends, the App Store isn’t the best way to do that."
  - surface: manual
  - verify: Ask the developer who the intended audience is.
  - fix: If the app is only for family and friends, install via Xcode or use Ad Hoc distribution instead of submitting to the App Store — manual — requires developer decision.

## INTRO.3 Points of view and content over the line

**Source text (verbatim):**
> - We strongly support all points of view being represented on the App Store, as long as the apps are respectful to users with differing opinions and the quality of the app experience is great. We will reject apps for any content or behavior that we believe is over the line. What line, you ask? Well, as a Supreme Court Justice once said, “I’ll know it when I see it”. And we think that you will also know it when you cross it.

**Applies to:** All apps

- **[INTRO-07]** Is the app respectful to users with differing opinions?
  - quote: "as long as the apps are respectful to users with differing opinions"
  - surface: runtime
  - verify: Review in-app copy, onboarding, and content plus App Store Connect metadata (description, screenshots, promotional text) for content that demeans users holding differing opinions.
  - fix: Rewrite or remove disrespectful content/copy.
- **[INTRO-08]** Is the quality of the app experience great?
  - quote: "the quality of the app experience is great"
  - surface: runtime
  - verify: Exercise all primary flows on simulator/device; note broken screens, placeholder content, layout glitches, or dead ends.
  - fix: Fix identified bugs, placeholders, and broken flows before submission.
- **[INTRO-09]** Is the app free of content or behavior the developer would recognize as "over the line"?
  - quote: "We will reject apps for any content or behavior that we believe is over the line."
  - surface: manual
  - verify: Ask the developer to attest that no content or behavior in the app is one they would consider "over the line"; cross-reference with Safety guideline (section 1) checks.
  - fix: manual — requires developer decision/legal/business action

## INTRO.4 Cheating the system

**Source text (verbatim):**
> - If you attempt to cheat the system (for example, by trying to trick the review process, steal user data, copy another developer’s work, manipulate ratings or App Store discovery) your apps will be removed from the store and you will be expelled from the Apple Developer Program.

**Applies to:** All apps

- **[INTRO-10]** Is the app free of anything designed to trick the review process (e.g., features hidden or behaving differently during review)?
  - quote: "trying to trick the review process"
  - surface: code
  - verify: Grep for date/time-gated or remote-flag-gated feature switches (e.g., `Date()` comparisons enabling features, remote config keys like "review", "isReview", "hidden", "unlock"), checks for reviewer/sandbox environments that alter functionality (`appStoreReceiptURL` containing "sandboxReceipt" used to hide features), and server-driven UI that can swap app purpose.
  - fix: Remove review-evasion logic; disclose all features in App Review notes.
- **[INTRO-11]** Is the app free of code that steals user data?
  - quote: "steal user data"
  - surface: code
  - verify: Inspect network calls (URLSession, Alamofire, third-party SDKs) for transmission of contacts, photos, location, clipboard (`UIPasteboard`), device identifiers, or keystrokes without user-facing purpose and consent. Compare against PrivacyInfo.xcprivacy and App Store Connect App Privacy answers.
  - fix: Remove undisclosed data collection; obtain consent and disclose collection.
- **[INTRO-12]** Is the app free of copied work from another developer?
  - quote: "copy another developer’s work"
  - surface: manual
  - verify: Ask the developer to attest that code, assets, UI, name, and icon are original or properly licensed; check bundled assets and third-party code for license files.
  - fix: manual — requires developer decision/legal/business action
- **[INTRO-13]** Is the app free of mechanisms that manipulate ratings or App Store discovery?
  - quote: "manipulate ratings or App Store discovery"
  - surface: code
  - verify: Grep for review prompts (`SKStoreReviewController`, `requestReview`, `AppStore.requestReview`) and confirm they are not conditioned on positive sentiment or rewarded; look for incentivized-review copy ("rate 5 stars", "rate us to unlock"). In App Store Connect, check metadata (name, subtitle, keywords) for keyword stuffing.
  - fix: Remove incentives/gating around ratings; clean metadata of manipulation.

## INTRO.5 Responsibility for third-party SDKs

**Source text (verbatim):**
> - You are responsible for making sure everything in your app complies with these guidelines, including ad networks, analytics services, and third-party SDKs, so review and choose them carefully.

**Applies to:** All apps; especially apps including ad networks, analytics services, or third-party SDKs

- **[INTRO-14]** Has every ad network, analytics service, and third-party SDK in the app been reviewed for compliance with the guidelines?
  - quote: "You are responsible for making sure everything in your app complies with these guidelines, including ad networks, analytics services, and third-party SDKs"
  - surface: code
  - verify: Enumerate dependencies from Package.resolved, Podfile.lock, Cartfile.resolved, and embedded frameworks. For each, identify category (ads, analytics, crash reporting, etc.), check for a bundled PrivacyInfo.xcprivacy, and apply the rest of this audit's checks (privacy, tracking, data collection) to each SDK's behavior.
  - fix: Update, reconfigure, or remove non-compliant SDKs.

## INTRO.6 Entitlements for limited use cases

**Source text (verbatim):**
> - Some features and technologies that are not generally available to developers may be offered as an entitlement for limited use cases. For example, we offer entitlements for CarPlay Audio, HyperVisor, and Privileged File Operations.

**Applies to:** Apps using features or technologies that are not generally available to developers

**Related:** CarPlay Audio entitlement; HyperVisor entitlement; Privileged File Operations entitlement

- **[INTRO-15]** If the app uses a feature that is offered only as a limited-use entitlement (e.g., CarPlay Audio, HyperVisor, Privileged File Operations), has that entitlement been granted to the developer?
  - quote: "Some features and technologies that are not generally available to developers may be offered as an entitlement for limited use cases."
  - surface: code
  - verify: Read all `*.entitlements` files and the provisioning profile (`security cms -D -i embedded.mobileprovision`). For entitlements such as `com.apple.developer.carplay-audio`, `com.apple.security.hypervisor`, or privileged file operations, confirm they appear in the provisioning profile (i.e., were granted by Apple).
  - fix: Request the entitlement from Apple, or remove the feature and entitlement if not granted.

## BEFORE Before You Submit

**Source text (verbatim):**
> To help your app approval go as smoothly as possible, review the common missteps listed below that can slow down the review process or trigger a rejection. This doesn’t replace the guidelines or guarantee approval, but making sure you can check every item on the list is a good start. If your app no longer functions as intended or you’re no longer actively supporting it, it will be removed from the App Store. Learn more about App Store Improvements.
>
> Make sure you:

**Applies to:** All apps

**Related:** App Store Improvements

- **[INTRO-16]** Does the app still function as intended?
  - quote: "If your app no longer functions as intended or you’re no longer actively supporting it, it will be removed from the App Store."
  - surface: runtime
  - verify: Build and run the app on a current simulator/device; exercise its core advertised functionality end to end.
  - fix: Fix broken functionality before submission.
- **[INTRO-17]** Is the developer still actively supporting the app?
  - quote: "you’re no longer actively supporting it"
  - surface: manual
  - verify: Ask the developer to confirm active support; check that the support URL in App Store Connect (App Store tab > version > Support URL) resolves.
  - fix: manual — requires developer decision/legal/business action

## BEFORE.1 Test for crashes and bugs

**Source text (verbatim):**
> - Test your app for crashes and bugs. Learn more about testing your app on compatible devices and configuring In‑App Purchases for review.

**Applies to:** All apps

**Related:** testing your app on compatible devices; configuring In‑App Purchases for review

- **[INTRO-18]** Has the app been tested for crashes and bugs?
  - quote: "Test your app for crashes and bugs."
  - surface: runtime
  - verify: Run the test suite (`xcodebuild test`) and launch the app on simulator/device; exercise all main flows; check console/crash logs for crashes, exceptions, and assertion failures. Check Xcode Organizer / TestFlight crash reports for the build to be submitted.
  - fix: Fix reproduced crashes and bugs; re-test.
- **[INTRO-19]** Has the app been tested on compatible devices?
  - quote: "testing your app on compatible devices"
  - surface: runtime
  - verify: Read supported device families (`TARGETED_DEVICE_FAMILY`, `UIRequiredDeviceCapabilities`, `UISupportedInterfaceOrientations~ipad`) and deployment target; run on at least one simulator/device for each supported family (e.g., iPhone and iPad) and the minimum supported OS if possible.
  - fix: Fix layout/crash issues on each supported device family, or remove unsupported families.
- **[INTRO-20]** If the app offers In‑App Purchases, are they configured for review?
  - quote: "configuring In‑App Purchases for review"
  - surface: asc
  - verify: In App Store Connect > Monetization > In-App Purchases / Subscriptions, confirm each product used in code (grep `Product.products(for:`, `SKProductsRequest`, product ID strings, `.storekit` files) exists, has status "Ready to Submit" or approved, has review screenshot and review notes, and is attached to the app version being submitted (first-time IAPs).
  - fix: Complete IAP metadata in App Store Connect and add the IAPs to the version submission.

## BEFORE.2 Complete and accurate metadata

**Source text (verbatim):**
> - Ensure that all app information and metadata is complete and accurate.

**Applies to:** All apps

- **[INTRO-21]** Is all app information and metadata in App Store Connect complete?
  - quote: "Ensure that all app information and metadata is complete"
  - surface: asc
  - verify: In App Store Connect, check App Information (name, subtitle, category, age rating, privacy policy URL), the version page (description, keywords, screenshots for each required device size, support URL, copyright, build selected), App Privacy, and Pricing and Availability for empty or missing required fields, for every localization.
  - fix: Fill in all missing fields.
- **[INTRO-22]** Is all app information and metadata accurate to the app?
  - quote: "metadata is complete and accurate"
  - surface: asc
  - verify: Compare App Store Connect description, screenshots, and app name against the actual app (CFBundleDisplayName, features in code, runtime screens); flag features described but not implemented, or screenshots not matching the app.
  - fix: Update metadata to accurately reflect the app.

## BEFORE.3 Contact information

**Source text (verbatim):**
> - Update your contact information in case App Review needs to reach you.

**Applies to:** All apps

- **[INTRO-23]** Is the App Review contact information up to date?
  - quote: "Update your contact information in case App Review needs to reach you."
  - surface: asc
  - verify: In App Store Connect > app version page > App Review Information > Contact Information, confirm first name, last name, phone number, and email are filled in; ask the developer to confirm they are current and monitored.
  - fix: Update the contact information fields in App Store Connect.

## BEFORE.4 Full access for App Review

**Source text (verbatim):**
> - Provide App Review with full access to your app. If your app includes account-based features, provide either an active demo account or fully-featured demo mode, plus any other hardware or resources that might be needed to review your app (such as login credentials or a sample QR code). Learn more about providing information for a complete review.

**Applies to:** All apps; demo account/mode requirement applies to apps that include account-based features

**Related:** providing information for a complete review

- **[INTRO-24]** Does App Review have full access to the app?
  - quote: "Provide App Review with full access to your app."
  - surface: runtime
  - verify: Identify gated areas in code (login screens, paywalls, invite codes, region/geo checks, device pairing). Confirm each can be reached by the reviewer using information provided in App Review Information.
  - fix: Provide credentials/instructions in App Review notes, or add a demo path for gated areas.
- **[INTRO-25]** If the app includes account-based features, is an active demo account or a fully-featured demo mode provided?
  - quote: "If your app includes account-based features, provide either an active demo account or fully-featured demo mode"
  - surface: asc
  - verify: Grep code for authentication (Sign in with Apple `ASAuthorizationAppleIDProvider`, Firebase/Supabase/Auth0 sign-in, custom login). If present, in App Store Connect > version > App Review Information > Sign-In Information, confirm "Sign-in required" is checked with username/password filled in (or notes explain the demo mode). At runtime, log in with those credentials and confirm they work and reach full features.
  - fix: Create an active demo account (with sample data) and enter it in Sign-In Information, or implement a fully-featured demo mode and document it.
- **[INTRO-26]** Are any other hardware or resources needed for review (such as login credentials or a sample QR code) provided?
  - quote: "plus any other hardware or resources that might be needed to review your app (such as login credentials or a sample QR code)"
  - surface: asc
  - verify: Grep code for QR/barcode scanning (`AVCaptureMetadataOutput`, `VNDetectBarcodesRequest`, `DataScannerViewController`), external accessory/Bluetooth (`CoreBluetooth`, `ExternalAccessory`), or hardware pairing. If present, confirm App Review notes or attachments in App Store Connect provide a sample QR code, demo video, or other needed resources.
  - fix: Attach sample QR codes/resources or a demo video and explain in App Review notes.

## BEFORE.5 Live backend services

**Source text (verbatim):**
> - Enable backend services so that they’re live and accessible during review.

**Applies to:** Apps that use backend services

- **[INTRO-27]** Are backend services enabled, live, and accessible during review?
  - quote: "Enable backend services so that they’re live and accessible during review."
  - surface: runtime
  - verify: Grep code/config for backend base URLs (e.g., `https://` constants, xcconfig, Info.plist keys, Firebase/Supabase config). Confirm the release build points at production (not localhost/staging/ngrok) and that the endpoints respond; exercise network-dependent flows on the release configuration.
  - fix: Point release config to the production backend and ensure it is deployed, live, and accessible during review.

## BEFORE.6 App Review notes for non-obvious features

**Source text (verbatim):**
> - Include detailed explanations of non-obvious features and in-app purchases in the App Review notes, including supporting documentation where appropriate.

**Applies to:** Apps with non-obvious features or in-app purchases

- **[INTRO-28]** Do the App Review notes include detailed explanations of non-obvious features?
  - quote: "Include detailed explanations of non-obvious features"
  - surface: asc
  - verify: Identify non-obvious features from code (background modes in `UIBackgroundModes`, widgets, App Clips, Siri/App Intents, extensions, Watch app, gestures, hidden settings, location/health usage). In App Store Connect > version > App Review Information > Notes, confirm each is explained.
  - fix: Write App Review notes explaining how to find and use each non-obvious feature.
- **[INTRO-29]** Do the App Review notes explain the in-app purchases?
  - quote: "Include detailed explanations of non-obvious features and in-app purchases in the App Review notes"
  - surface: asc
  - verify: If StoreKit is used in code, confirm the App Review notes explain where each in-app purchase is offered and what it unlocks.
  - fix: Add IAP explanations (location in app, what is unlocked) to App Review notes.
- **[INTRO-30]** Is supporting documentation included where appropriate?
  - quote: "including supporting documentation where appropriate"
  - surface: asc
  - verify: In App Store Connect > App Review Information > Attachment, check for supporting files (demo video, documents) when features are complex or need hardware.
  - fix: Attach supporting documentation or a demo video.

## BEFORE.7 Regulatory documentation

**Source text (verbatim):**
> - Provide required documentation for apps and features that require regulatory approval.

**Applies to:** Apps and features that require regulatory approval

- **[INTRO-31]** If the app or any feature requires regulatory approval, is the required documentation provided?
  - quote: "Provide required documentation for apps and features that require regulatory approval."
  - surface: manual
  - verify: Ask the developer whether any feature is subject to regulatory approval (e.g., in their market or category). If so, confirm the documentation is attached in App Store Connect > App Review Information > Attachment or referenced in Notes.
  - fix: manual — requires developer decision/legal/business action

## BEFORE.8 Other Apple documentation

**Source text (verbatim):**
> - Check whether your app follows guidance in other documentation, such as:
>
> Developer Documentation
> - SwiftUI
> - UIKit
> - AppKit
> - App extensions
> - Optimizing Your App’s Data for iCloud Backup
> - Apple File System
> - App Store Connect Help
> - App Review Help
> - Developer Account Help
>
> Design Guidelines
> - Human Interface Guidelines
>
> Brand and Marketing Guidelines
> - Marketing Resources and Identity Guidelines
> - Apple Pay Marketing Guidelines
> - Add to Apple Wallet Guidelines
> - Guidelines for Using Apple Trademarks and Copyrights
>
> Guidelines that include  apply to Notarization for iOS and iPadOS apps.

**Applies to:** All apps (each document as relevant to the technologies the app uses)

**Related:** SwiftUI; UIKit; AppKit; App extensions; Optimizing Your App’s Data for iCloud Backup; Apple File System; App Store Connect Help; App Review Help; Developer Account Help; Human Interface Guidelines; Marketing Resources and Identity Guidelines; Apple Pay Marketing Guidelines; Add to Apple Wallet Guidelines; Guidelines for Using Apple Trademarks and Copyrights

- **[INTRO-32]** Has the app been checked against the guidance in the relevant developer documentation (SwiftUI, UIKit, AppKit, App extensions)?
  - quote: "Check whether your app follows guidance in other documentation, such as:"
  - surface: code
  - verify: Determine which UI frameworks and extension types the project uses (imports of SwiftUI/UIKit/AppKit; extension targets and `NSExtensionPointIdentifier` in extension Info.plists). Flag deprecated API usage reported by the compiler (`xcodebuild` warnings).
  - fix: Address deprecated/discouraged API usage per framework documentation.
- **[INTRO-33]** Does the app follow the guidance in "Optimizing Your App’s Data for iCloud Backup"?
  - quote: "Optimizing Your App’s Data for iCloud Backup"
  - surface: code
  - verify: Grep for file writes to the Documents and Application Support directories (`.documentDirectory`, `.applicationSupportDirectory`) of large or re-downloadable data (caches, downloaded media, models); check whether `isExcludedFromBackup` / `URLResourceValues.isExcludedFromBackup` or the Caches/tmp directories are used for such data.
  - fix: Move re-creatable data to Caches/tmp or mark it excluded from backup.
- **[INTRO-34]** Does the app follow the Human Interface Guidelines?
  - quote: "Human Interface Guidelines"
  - surface: runtime
  - verify: Run the app and review screens for HIG conformance relevant to the platform (standard navigation, controls, Dynamic Type, Dark Mode, safe areas, app icon). Cross-reference with Design guideline (section 4) checks.
  - fix: Adjust UI to conform to the HIG.
- **[INTRO-35]** If the app or its marketing uses Apple brand assets, Apple Pay, Apple Wallet, or Apple trademarks, does it follow the corresponding brand and marketing guidelines?
  - quote: "Guidelines for Using Apple Trademarks and Copyrights"
  - surface: asc
  - verify: Grep the project and assets for Apple marks/badges ("Apple Pay", "Add to Apple Wallet" buttons via `PKPaymentButton`/`PKAddPassButton` vs custom images, "Download on the App Store" badges, Apple product images). Review App Store Connect screenshots and description for Apple trademarks/device imagery usage.
  - fix: Use the system-provided buttons/official badges and follow Apple's marketing/trademark guidelines; remove improper use.

## AFTER After You Submit

**Source text (verbatim):**
> Once you’ve submitted your app and metadata in App Store Connect and you’re in the review process, here are some things to keep in mind:
>
> We’re excited to see what you come up with next!

**Applies to:** Apps that have been submitted and are in the review process

**Status:** Informational — no checks.

## AFTER.1 Timing

**Source text (verbatim):**
> - Timing: App Review will examine your app as soon as we can. However, if your app is complex or presents new issues, it may require greater scrutiny and consideration. And remember that if your app is repeatedly rejected for the same guideline violation or you’ve attempted to manipulate the review process, review of your app will take longer to complete. Learn more about App Review.

**Applies to:** Apps in the review process

**Related:** App Review

- **[INTRO-36]** Have all issues cited in any previous rejection been resolved, so the app is not rejected again for the same guideline violation?
  - quote: "if your app is repeatedly rejected for the same guideline violation"
  - surface: asc
  - verify: In App Store Connect > App Review (Resolution Center / submission messages), read previous rejection messages; for each cited guideline, confirm the corresponding fix exists in the current build/metadata and re-run that guideline's checks.
  - fix: Fix every previously cited violation before resubmitting; explain the fix in App Review notes.

## AFTER.2 Status Updates

**Source text (verbatim):**
> - Status Updates: The current status of your app will be reflected in App Store Connect, so you can keep an eye on things from there. Learn more about tracking a submission’s review status.

**Applies to:** Apps in the review process

**Related:** tracking a submission’s review status


## AFTER.3 Expedite Requests

**Source text (verbatim):**
> - Expedite Requests: If you have a critical timing issue, you can request an expedited review. Please respect your fellow developers by seeking expedited review only when you truly need it. If we find you’re abusing this system, we may reject your requests going forward. Learn more about expediting requests.

**Applies to:** Developers considering an expedited review request

**Related:** expediting requests

- **[INTRO-38]** If an expedited review is requested, is there a critical timing issue that truly requires it?
  - quote: "Please respect your fellow developers by seeking expedited review only when you truly need it."
  - surface: manual
  - verify: Ask the developer whether an expedited review is planned and what the critical timing issue is.
  - fix: manual — requires developer decision/legal/business action

## AFTER.4 Release Date

**Source text (verbatim):**
> - Release Date: If your release date is set for the future, the app will not appear on the App Store until that date, even if it is approved by App Review. And remember that it can take up to 24-hours for your app to appear on all selected storefronts.

**Applies to:** All apps

- **[INTRO-39]** (Informational — not a rejection criterion) Is the version release setting (manual, automatic, or scheduled date) the one the developer intends?
  - quote: "If your release date is set for the future, the app will not appear on the App Store until that date, even if it is approved by App Review."
  - surface: asc
  - verify: In App Store Connect > version page > App Store Version Release, read the selected release option and any scheduled date; confirm with the developer it is intended.
  - fix: Change the release option in App Store Connect.
- **[INTRO-40]** (Informational — not a rejection criterion) Does the developer's launch plan allow up to 24 hours for the app to appear on all selected storefronts?
  - quote: "it can take up to 24-hours for your app to appear on all selected storefronts"
  - surface: manual
  - verify: Ask the developer whether any launch announcement depends on the app being live immediately after release; check selected storefronts in App Store Connect > Pricing and Availability.
  - fix: manual — requires developer decision/legal/business action

## AFTER.5 Rejections

**Source text (verbatim):**
> - Rejections: Our goal is to apply these guidelines fairly and consistently, but nobody’s perfect. If your app has been rejected and you have questions or would like to provide additional information, please use App Store Connect to communicate directly with the App Review team. This may help get your app on the store, and it can help us improve the App Review process or identify a need for clarity in our policies. Learn more about contacting App Review for help with a submission.

**Applies to:** Apps that have been rejected

**Related:** contacting App Review for help with a submission

- **[INTRO-41]** If the app was rejected and the developer has questions or additional information, has it been communicated to App Review through App Store Connect?
  - quote: "please use App Store Connect to communicate directly with the App Review team"
  - surface: asc
  - verify: In App Store Connect > App Review messages for the rejected submission, check whether open questions/additional info have been replied to.
  - fix: Reply to App Review in App Store Connect with the clarifying information (drafted for the developer to send).

## AFTER.6 Appeals

**Source text (verbatim):**
> - Appeals: If you disagree with the outcome of your review, please submit an appeal. This may help get your app on the store. You may also suggest changes to the guidelines themselves to help us improve the App Review process or identify a need for clarity in our policies. Learn more about submitting complete appeals and suggesting guideline changes.

**Applies to:** Developers who disagree with the outcome of their review

**Related:** submitting complete appeals; suggesting guideline changes

- **[INTRO-42]** If the developer disagrees with the review outcome, has an appeal been submitted?
  - quote: "If you disagree with the outcome of your review, please submit an appeal."
  - surface: manual
  - verify: Ask the developer whether they disagree with the rejection; if so, confirm whether an appeal has been submitted.
  - fix: manual — requires developer decision/legal/business action

## AFTER.7 Bug Fix Submissions

**Source text (verbatim):**
> - Bug Fix Submissions: For apps that are already on the App Store or alternative distribution, bug fixes will not be delayed over guideline violations except for those related to legal or safety issues. If your app has been rejected, and qualifies for this process, please use App Store Connect to communicate directly with the App Review team indicating that you would like to take advantage of this process and plan to address the issue in your next submission. Learn more about accepting Bug Fix Submission offers.

**Applies to:** Apps already on the App Store or alternative distribution that were rejected and qualify for the Bug Fix Submission process

**Related:** accepting Bug Fix Submission offers

- **[INTRO-43]** If a qualifying bug-fix update was rejected for a guideline violation not related to legal or safety issues, has the developer told App Review via App Store Connect that they want to use this process and will address the issue in the next submission?
  - quote: "please use App Store Connect to communicate directly with the App Review team indicating that you would like to take advantage of this process and plan to address the issue in your next submission"
  - surface: asc
  - verify: Confirm the app is already live (App Store Connect version history shows a released version) and the rejection cites a non-legal, non-safety guideline; check App Review messages for a reply accepting the Bug Fix Submission process.
  - fix: Reply to App Review in App Store Connect (drafted for the developer to send) and schedule the fix for the next submission.
