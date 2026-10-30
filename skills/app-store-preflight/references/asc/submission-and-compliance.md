# Submission Process and Compliance Gates
Source: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review , https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app , https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions , https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating , https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations , https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements , https://developer.apple.com/news/upcoming-requirements/ , https://developer.apple.com/distribute/app-review/ , https://developer.apple.com/app-store/submitting/ , https://developer.apple.com/help/app-review/ (child pages listed under Sources)  
Retrieved: 2026-10-30

Scope note: every unit below is copied from the Apple page named in its heading. Tables reproduce Apple's published lists. Multi-line table cells in Apple's page are joined with "; " / ". " / ": " in one cell. Non-compliance App information and Platform version properties (name, subtitle, description, keywords, URLs, What's New, release options) are covered in metadata-and-media.md. Where a table cell in Apple's page is an image (pictogram or checkmark), it is marked "(image on source page)" — the image content is not transcribed.

---

## SUBMIT.OVERVIEW Overview of submitting for review

**Source text (verbatim):**
> The review process covers every version of your app and its content, like In-App Purchases, subscription offers, and Apple-hosted asset packs, to ensure a safe and trustworthy experience for users and to support developers' success.
> Our goal is to make the submission process as convenient and efficient as possible. While you typically submit one submission for review at a time per platform, you also have the flexibility to submit items with one additional submission, even if you already have an app version submitted for review.
> For example, if you have an app version currently under review, you can also submit an In-App Event in a separate submission, or if you have a custom product page under review, you can also submit an app version in a separate submission.
> Note: Submissions may not be reviewed in the order you submit them.
> You can choose to submit items for review together with, or separately from, an app version. If your submission includes an app version, items will be reviewed together with that app version. If your submission doesn’t include an app version, or your submission includes items associated with multiple platforms, items will be reviewed together with the latest version of the platform you specify during the submission process. Use the App Review information section on the latest approved app version for that platform to provide additional information or context that will help App Review during the review process. Learn about App Review guidelines.
> App versions for each platform are submitted separately. The status of any app versions on one platform doesn’t influence the status of app versions on other platforms.
> Manage your submissions and messages with the App Review team in the App Review section of the sidebar. This section may display four types of content:
> - App (iOS, macOS, tvOS, visionOS) Submission: App versions and/or items that you submitted to App Review, and any related messages from App Review.
> - Beta Build: Beta versions of your app that you submitted and App Review didn’t accept, and any related messages from App Review.
> - Beta Asset Pack: Beta versions of asset packs that you submitted and App Review didn’t accept, and any related messages from App Review.
> - App Review Message: Other messages from App Review that don’t relate to a submission.
>
> FAQs
> How many submissions can I submit for review at a time?
> - Each platform can have one app version submission under review at a time.
> - A platform can have a maximum of two submissions under review at a time: one that includes an app version and one that includes items, like In-App Events or custom product pages, without an app version.
>
> What items can I add to a submission?
> Items associated with different platforms can't be added to the same submission. For example, if you’ve selected the macOS platform for a submission with an Apple-hosted asset pack, you’ll need to create a separate submission to submit a custom product page for iOS.
> In addition to an app version, you can add the following items to a submission to App Review:
> - Auto-renewable subscription, non-renewing subscriptions, and subscription groups
> - In-App Purchases
> - In-App Events
> - Custom product pages
> - Product page optimization tests
> - Apple-hosted asset packs
> - Game Center components, including new or modified leaderboards, leaderboard sets, achievements, challenges, and activities

**Applies to:** All apps

- **[SUBMIT-01]** Is there no other app version submission for this platform already under review (so the new app version submission can be accepted)?
  - quote: "Each platform can have one app version submission under review at a time."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > App Review (sidebar) > Submissions: count submissions in Waiting for Review / In Review that include an app version for the target platform. Pass if 0 before submitting a new version.
  - fix: manual — wait for the current version submission to complete, or remove it from review (see SUBMIT.REMOVE) if the developer decides to replace it.
- **[SUBMIT-02]** Does the platform have at most two submissions under review (one with an app version, one items-only)?
  - quote: "A platform can have a maximum of two submissions under review at a time: one that includes an app version and one that includes items, like In-App Events or custom product pages, without an app version."
  - surface: asc
  - verify: App Review page > Submissions list, filter by platform; count active (Waiting for Review / In Review) submissions.
  - fix: manual — add items to the existing draft/version submission instead of opening a third submission.
- **[SUBMIT-03]** Are all items in each submission associated with a single platform?
  - quote: "Items associated with different platforms can't be added to the same submission."
  - surface: asc
  - verify: Open the draft submission on the App Review page; confirm every listed item (IAP, event, custom product page, asset pack, Game Center component) belongs to the platform selected for that submission.
  - fix: Move items for the other platform into a separate submission.
- **[SUBMIT-04]** For an items-only submission (no app version), is the App Review information on the latest approved version of that platform current?
  - quote: "Use the App Review information section on the latest approved app version for that platform to provide additional information or context that will help App Review during the review process."
  - surface: asc
  - verify: Apps > (app) > latest approved version for the platform > App Review Information: check contact, sign-in, and Notes are current for the items being submitted.
  - fix: Click Edit in the App Review Information section of the approved version and update contact, demo account and Notes.

## SUBMIT.APP Submit an app

**Source text (verbatim):**
> Before submitting an app version for review, provide required metadata and choose the build for the version.
> Learn how to submit using the App Store Connect API.
> Required role: Account Holder, Admin, or App Manager. View role permissions.
> In Apps, select the app you want to view.
> In the sidebar, click the app version you want to submit.
> On the right, scroll down to the Build section and verify that you added the right build for the version.
> On the top right, click “Add for Review,” and select whether to add the app version to an existing draft submission or create a new submission. The app status changes to Ready for Review. Your submission won’t be sent to App Review until you submit it for review in the next step.
> You can add items, such as In-App Events or Apple-hosted asset packs, to your submission. All items submitted together must be Accepted to complete the submission.
> To review the items you've added, click Draft Submissions on the bottom right of the screen and select the submission. Alternatively, you can go to the App Review section in the sidebar.
> Click Submit for Review. When the review process starts, the app status changes to In Review. Learn about the tasks you can do in these statuses.

**Applies to:** All apps submitting an app version

- **[SUBMIT-05]** Has all required metadata been provided and a build chosen for the version before submitting?
  - quote: "Before submitting an app version for review, provide required metadata and choose the build for the version."
  - surface: asc
  - verify: Apps > (app) > (version): confirm no red required-field warnings on the version page, App Information and App Privacy pages; the Build section shows a build (icon, build string, upload date).
  - fix: Fill all required fields flagged by App Store Connect; add a build (see SUBMIT.BUILD).
- **[SUBMIT-06]** Does the person submitting hold the Account Holder, Admin, or App Manager role?
  - quote: "Required role: Account Holder, Admin, or App Manager."
  - surface: asc
  - verify: Users and Access > the submitting user > Roles.
  - fix: manual — Account Holder/Admin assigns the role, or a user with the role submits.
- **[SUBMIT-07]** Is the build attached to the version the right build (matching the project's version and build number intended for release)?
  - quote: "verify that you added the right build for the version"
  - surface: code
  - verify: Read MARKETING_VERSION / CFBundleShortVersionString and CURRENT_PROJECT_VERSION / CFBundleVersion from the Xcode project (`xcodebuild -showBuildSettings` or project.pbxproj / Info.plist); compare to the version number and build string shown in ASC > version > Build section.
  - fix: Remove the wrong build and add the intended one (SUBMIT.BUILD), or upload a new build with the correct numbers.
- **[SUBMIT-08]** After "Add for Review", was Submit for Review actually clicked (status In Review / Waiting for Review, not just Ready for Review in a draft)?
  - quote: "Your submission won’t be sent to App Review until you submit it for review in the next step."
  - surface: asc
  - verify: App Review page: the submission is not under Draft Submissions; version status is Waiting for Review or In Review.
  - fix: Open Draft Submissions > select the submission > click Submit for Review.
- **[SUBMIT-09]** Has every item added to the submission been reviewed by the developer as ready, given all items must be Accepted for the submission to complete?
  - quote: "All items submitted together must be Accepted to complete the submission."
  - surface: asc
  - verify: Draft Submissions > the submission: list every item (IAPs, subscriptions, In-App Events, asset packs); confirm each item is complete and ready to be Accepted.
  - fix: Complete or remove unfinished items from the draft before submitting.

## SUBMIT.BUILD Choose a build to submit

**Source text (verbatim):**
> Before submitting an app to App Review, choose a build from those you’ve uploaded for the version. You can only associate one build with each app version. However, you can change the build as often as you want until you submit the version to App Review.
> Required role: Account Holder, Admin, or App Manager. View role permissions.
> Add a build to a version
> In Apps, select the app you want to view.
> In the sidebar, click the app version under the platform you wish to select.
> On the right, scroll down to the Build section, then click the add button (+) next to Build.
> The add button (+) appears once you have uploaded builds but have not yet selected one. If a different build is selected than the one you want to submit for review, remove the build.
> In the Add Build dialog, select the build you want to submit.
> If an earlier version of your app is Ready for Distribution, the list only includes builds you have uploaded since that version was released on the App Store. Learn how to view available builds.
> Click Done.
> In the Build section, the app icon, build string, and upload date and time appear.
> On the top right, click Save.
> Note: If you select a build with the Missing Compliance status, you must answer the export compliance questions before submitting for review. Click Manage or Choose File next to the build and answer the questions, or follow the steps to upload app encryption documentation.
> Remove a build from a version
> When you remove a build from an app version, it’s not removed from your account.
> In Apps, select the app you want to view.
> In the sidebar, click the app version under the platform you wish to remove.
> On the right, scroll to the Build section.
> Hold the pointer over the build, then click the delete button (–) that appears to the right of the upload date.
> On the top right, click Save.

**Applies to:** All apps submitting an app version

- **[SUBMIT-10]** Is exactly one build associated with the app version?
  - quote: "You can only associate one build with each app version."
  - surface: asc
  - verify: Version page > Build section shows one build with icon, build string, upload date and time.
  - fix: Click + next to Build, select the build, click Done, then Save.
- **[SUBMIT-11]** Was the selected build uploaded after the currently released version (when an earlier version is Ready for Distribution)?
  - quote: "If an earlier version of your app is Ready for Distribution, the list only includes builds you have uploaded since that version was released on the App Store."
  - surface: code
  - verify: ASC > version > Build > + (Add Build dialog): the intended build is listed (it was uploaded after the version that is Ready for Distribution was released).
  - fix: Archive and upload a new build for this version (SUBMIT.UPLOAD), then select it.
- **[SUBMIT-12]** Is the selected build free of the Missing Compliance status (export compliance questions answered)?
  - quote: "If you select a build with the Missing Compliance status, you must answer the export compliance questions before submitting for review."
  - surface: asc
  - verify: Version page > Build section, or TestFlight > Builds: status of the build is not "Missing Compliance".
  - fix: Click Manage next to the build and answer the questions, or Choose File to attach approved documentation; and add ITSAppUsesNonExemptEncryption to Info.plist for future builds (SUBMIT.EXPORT.KEY).

## SUBMIT.UPLOAD Upload builds

**Source text (verbatim):**
> Required role: Account Holder, Admin, App Manager, or Developer. View role permissions.
> After adding an app to your account, you can upload a build using Xcode, Swift Playground, altool, or Transporter. If you use the App Store Connect API, you might want to upload your binary using the Transporter command-line tool and JSON Web Tokens (JWTs) for authentication. You can use the same JWTs that you use for the API to upload your binary. As your app changes, you can upload more builds, distribute a build for testing, or submit your app for review.
> The first time you upload a build, a beta version of the app is created in your account. However, the build needs to be processed in Apple’s system before it appears in App Store Connect. You’ll receive an email when this process is complete.
> Each time you upload a build, the bundle ID and version number, which are located in the app bundle, are used to associate the build with the app and version record in App Store Connect. The build string is used to uniquely identify the build throughout the system.
> You can also create and upload your build using Xcode Cloud. Xcode Cloud lets you adopt continuous integration and continuous delivery (CI/CD), a standard practice that helps monitor and improve software quality over time, ensuring your app or framework is always in a releasable state. Learn more about Xcode Cloud.
> You also have the option to upload assets that are managed separately from a build by using Apple-Hosted Background Assets. Learn more.
> Supported Xcode Versions
> App Store Connect supports the following versions of Xcode to upload your app for customer distribution or to testers using TestFlight. You can view delivery progress, including warnings, errors, and delivery logs, as well as a history of past deliveries.
>
> | Target type | Built using Xcode | Uploaded using Xcode |
> |---|---|---|
> | iOS app | Xcode 26 or later | Xcode 14 or later |
> | iOS app extension | Xcode 26 or later | Xcode 14 or later |
> | watchOS app extension | Xcode 26 or later | Xcode 14 or later |
> | macOS app | Xcode 6 or later | Xcode 14 or later |
> | tvOS app | Xcode 26 or later | Xcode 14 or later |
> | visionOS app | Xcode 26 or later | Xcode 15 or later |
>
> Upload for all target types is supported for Transporter and altool.
> $ xcrun altool --validate-app -f file -t platform -u username [-p password] [--output-format xml]
> $ xcrun altool --upload-app -f file -t platform -u username [-p password] [--output-format xml]

**Applies to:** All apps uploading builds

- **[SUBMIT-13]** Do the bundle ID and version number in the app bundle match the App Store Connect app and version record?
  - quote: "the bundle ID and version number, which are located in the app bundle, are used to associate the build with the app and version record in App Store Connect"
  - surface: code
  - verify: `xcodebuild -showBuildSettings -scheme <scheme> | grep -E 'PRODUCT_BUNDLE_IDENTIFIER|MARKETING_VERSION'`; compare to ASC > App Information > Bundle ID and the version being prepared in the sidebar.
  - fix: Set PRODUCT_BUNDLE_IDENTIFIER / MARKETING_VERSION in the target build settings to match the ASC record (or create the matching version in ASC).
- **[SUBMIT-14]** Is the build string unique (never previously uploaded for this version)?
  - quote: "The build string is used to uniquely identify the build throughout the system."
  - surface: code
  - verify: Read CURRENT_PROJECT_VERSION / CFBundleVersion; compare against builds listed in ASC > TestFlight > Builds for the version.
  - fix: Increment CURRENT_PROJECT_VERSION (e.g., `agvtool next-version -all`) and re-archive.
- **[SUBMIT-15]** Are iOS, tvOS, visionOS apps and iOS/watchOS app extensions built using Xcode 26 or later?
  - quote: "Xcode 26 or later"
  - surface: code
  - verify: `xcodebuild -version`; in the archived app's Info.plist read DTXcode and DTXcodeBuild (`plutil -p <App>.app/Info.plist | grep DTXcode`); in CI config (Xcode Cloud workflow, GitHub Actions `xcode-version`, fastlane) check the selected Xcode.
  - fix: Install Xcode 26 or later, select it (`xcode-select -s`), update CI image, rebuild and upload.
- **[SUBMIT-16]** Has the uploaded build finished processing and appeared in App Store Connect?
  - quote: "the build needs to be processed in Apple’s system before it appears in App Store Connect"
  - surface: asc
  - verify: TestFlight > Builds: build appears with a non-Processing status.
  - fix: Wait for the processing email; if an error email arrives, fix the reported issue and upload a new build.

## SUBMIT.SIZE Maximum build file sizes

**Source text (verbatim):**
> Verify that your app, along with each Mach-O executable file (for example, app_name.app/app_name), doesn’t exceed the maximum file size limits on the supported operating systems.
> For iOS, iPadOS, macOS, tvOS, and visionOS apps, you can use Background Assets to host larger assets that are managed separately from your build.
> The size shown on your App Store product page varies depending on the device that’s viewing the page. On macOS, the product page shows the the universal installation size. On all other platforms, it shows the installation size for the specific device model. If your app uses Apple-Hosted Background Assets, the product page shows an “Up to” size that also includes any non-localized essential asset packs and the localized essential asset packs for the single language with the largest total size.
>
> | Platform | Minimum deployment target | Maximum uncompressed app size | Maximum executable file size |
> |---|---|---|---|
> | iOS and iPadOS | iOS 9.0 and later | 4 GB | 500 MB 1 |
> | iOS and iPadOS | iOS 7.X through iOS 8.X | 4 GB | 60 MB 2 |
> | iOS and iPadOS | Earlier than iOS 7.0 | 4 GB | 80 MB 1 |
> | macOS | All macOS versions | 200 GB | |
> | tvOS | tvOS 9.0 and later | 4 GB | 500 MB 1 |
> | visionOS | visionOS 1.0 and later | 4 GB | 500 MB 1 |
> | watchOS | All watchOS versions | 75 MB | |
>
> 1 For the total of all __TEXT sections in the binary.
> 2 For the __TEXT sections in each architecture slice. An architecture slice is a part of the fat binary layout that targets a specific architecture. For example, a fat binary might include slices for 32-bit and 64-bit architectures.
>
> App Clips
> To ensure a successful launch experience, verify that the uncompressed main bundle of any App Clip variant, after app thinning, doesn’t exceed the maximum size limit for the minimum deployment target used in the App Clip.
>
> | Minimum deployment target | Maximum variant size | Notes |
> |---|---|---|
> | iOS 17 and later | 100 MB | Following requirements must be met: |
> |  |  | The App Clip only supports digital invocations — for example, from your website or Spotlight search — and not from physical invocations like App Clip Codes, QR codes, or NFC tags. |
> |  |  | People use your App Clip in situations where a reliable internet connection is likely, for example, at home. |
> |  |  | Your App Clip doesn’t support iOS versions prior to iOS 17. |
> | iOS 16 and later | 15 MB | |
> | Earlier than iOS 16 | 10 MB | |

**Applies to:** All apps (App Clip rows: apps with an App Clip)

- **[SUBMIT-17]** Is the uncompressed app size within the platform limit (4 GB iOS/iPadOS/tvOS/visionOS, 200 GB macOS, 75 MB watchOS)?
  - quote: "Verify that your app, along with each Mach-O executable file (for example, app_name.app/app_name), doesn’t exceed the maximum file size limits on the supported operating systems."
  - surface: code
  - verify: Archive, export, then `du -sk <App>.app` on the unzipped .app (and the watch app bundle separately); compare against the table row for the platform.
  - fix: Move large content to Background Assets / Apple-Hosted Background Assets, remove unused resources, compress assets.
- **[SUBMIT-18]** Is the total of all __TEXT sections of the main executable within 500 MB (iOS 9.0+, tvOS, visionOS deployment targets)?
  - quote: "For the total of all __TEXT sections in the binary."
  - surface: code
  - verify: `size -m <App>.app/<App>` or `otool -l <App>.app/<App> | grep -A3 __TEXT`; sum __TEXT sizes and compare against 500 MB (60 MB per slice for iOS 7.X–8.X targets; 80 MB for earlier than iOS 7.0).
  - fix: Reduce executable size (dead-strip, remove unused dependencies, move code into dynamic frameworks/extensions as appropriate).
- **[SUBMIT-19]** Is each App Clip variant's uncompressed main bundle (after thinning) within the limit for its deployment target (100 MB iOS 17+ with conditions, 15 MB iOS 16+, 10 MB earlier)?
  - quote: "verify that the uncompressed main bundle of any App Clip variant, after app thinning, doesn’t exceed the maximum size limit for the minimum deployment target used in the App Clip"
  - surface: code
  - verify: Export with "App Thinning: All compatible device variants" and read "App Thinning Size Report.txt" for the App Clip target; compare each variant's uncompressed size to the row matching the App Clip target's IPHONEOS_DEPLOYMENT_TARGET.
  - fix: Shrink App Clip assets/code; for the 100 MB limit, ensure deployment target iOS 17 and only digital invocations.
- **[SUBMIT-20]** If an App Clip relies on the 100 MB limit, does it meet all listed conditions (digital invocations only, no support for iOS before 17)?
  - quote: "Your App Clip doesn’t support iOS versions prior to iOS 17."
  - surface: code
  - verify: App Clip target IPHONEOS_DEPLOYMENT_TARGET ≥ 17.0; inspect ASC App Clip experiences for App Clip Codes / QR / NFC (physical) invocations.
  - fix: Raise the App Clip deployment target to iOS 17 and remove physical invocations, or reduce the variant size to 15 MB.

## SUBMIT.REQ.IOS-MIN iOS and iPadOS minimum system requirements (Upcoming Requirements)

**Source text (verbatim):**
> iOS and iPadOS minimum system requirements
> Since September 9, 2026
> iOS and iPadOS apps uploaded to App Store Connect must target iOS 13 or later.

**Applies to:** iOS and iPadOS apps uploaded to App Store Connect

- **[SUBMIT-21]** Is the iOS/iPadOS deployment target iOS 13 or later for every target in the app?
  - quote: "iOS and iPadOS apps uploaded to App Store Connect must target iOS 13 or later."
  - surface: code
  - verify: `grep -n IPHONEOS_DEPLOYMENT_TARGET *.xcodeproj/project.pbxproj`, plus Package.swift `platforms: [.iOS(...)]`, Podfile `platform :ios`, and any .xcconfig; every value must be ≥ 13.0.
  - fix: Raise IPHONEOS_DEPLOYMENT_TARGET to at least 13.0 in all targets/configurations (see also SUBMIT-32 for April 2027).

## SUBMIT.REQ.SDK SDK minimum requirements (Upcoming Requirements)

**Source text (verbatim):**
> SDK minimum requirements
> Since April 28, 2026
> Apps uploaded to App Store Connect must be built with Xcode 26 or later using an SDK for iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26.

**Applies to:** Apps uploaded to App Store Connect

- **[SUBMIT-22]** Is the app built with Xcode 26 or later using a 26 SDK?
  - quote: "Apps uploaded to App Store Connect must be built with Xcode 26 or later using an SDK for iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26."
  - surface: code
  - verify: In the archived app Info.plist read DTSDKName / DTPlatformVersion and DTXcode (`plutil -p`); or `xcodebuild -showsdks` with the CI Xcode; SDKROOT should resolve to the 26 (or later) SDK.
  - fix: Build with Xcode 26 or later (update local and CI Xcode), resolve new SDK warnings, re-archive and upload.

## SUBMIT.REQ.AGE Age Rating Updates (Upcoming Requirements)

**Source text (verbatim):**
> Age Rating Updates
> Since January 31, 2026
> Ratings for all apps and games on the App Store have been automatically updated to align with our new age rating system and will be reflected on Apple devices running a minimum of iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, visionOS 26, and watchOS 26.
> Provide responses to the updated age rating questions for each of your apps by January 31, 2026, to avoid an interruption when submitting your app updates in App Store Connect. You can view the age rating for each of your apps under the updated system and respond to the new questions in the App Information section of your app in App Store Connect.

**Applies to:** All apps

- **[SUBMIT-23]** Have the updated age rating questions been answered for the app?
  - quote: "Provide responses to the updated age rating questions for each of your apps by January 31, 2026, to avoid an interruption when submitting your app updates in App Store Connect."
  - surface: asc
  - verify: App Information > Age Ratings: questionnaire shows completed responses under the new system (In-App Controls, Capabilities, content sections) and a rating value (not a prompt to set up).
  - fix: Click Set Up Age Ratings / Edit and answer every section (SUBMIT.AGE.SET).

## SUBMIT.REQ.APNS APNs Certificate Update (Upcoming Requirements)

**Source text (verbatim):**
> APNs Certificate Update
> Since February 24, 2025
> The Apple Push Notification service (APNs) will be updated with a new server certificate in production on February 24, 2025. Update your application’s Trust Store to include the new server certificate: SHA-2 Root : USERTrust RSA Certification Authority certificate.
> APNs Certificate Update
> Since January 20, 2025
> The Apple Push Notification service (APNs) will be updated with a new server certificate in sandbox on January 20, 2025. Update your application’s Trust Store to include the new server certificate: SHA-2 Root : USERTrust RSA Certification Authority certificate.

**Applies to:** Apps that send push notifications via APNs
**Requires:** push

- **[SUBMIT-24]** Does the push provider's Trust Store include the SHA-2 Root : USERTrust RSA Certification Authority certificate?
  - quote: "Update your application’s Trust Store to include the new server certificate: SHA-2 Root : USERTrust RSA Certification Authority certificate."
  - surface: manual
  - verify: Detect APNs use in the app (aps-environment in .entitlements, `registerForRemoteNotifications`); then ask the developer/inspect the server repo for certificate pinning or a custom CA bundle used to connect to api.push.apple.com / api.sandbox.push.apple.com.
  - fix: manual — add the USERTrust RSA Certification Authority root to the provider server's trust store.

## SUBMIT.REQ.QUARANTINE Quarantine attribute in macOS apps uploaded to App Store Connect (Upcoming Requirements)

**Source text (verbatim):**
> Quarantine attribute in macOS apps uploaded to App Store Connect
> Since February 18, 2025
> macOS apps distributed on TestFlight and the App Store shouldn’t include the quarantine extended file attribute com.apple.quarantine. Starting February 18, you must remove this attribute from all files within macOS apps in order to upload to App Store Connect.

**Applies to:** macOS apps distributed on TestFlight and the App Store
**Requires:** macos, ipad

- **[SUBMIT-25]** Is the com.apple.quarantine extended attribute absent from every file in the macOS app bundle?
  - quote: "you must remove this attribute from all files within macOS apps in order to upload to App Store Connect"
  - surface: code
  - verify: `xattr -rl <App>.app | grep com.apple.quarantine` on the exported app, and on resource files checked into the repo (`xattr -rl <project dir> | grep com.apple.quarantine`). Pass if no output.
  - fix: `xattr -rd com.apple.quarantine <path>` on affected source files/bundles, then rebuild.

## SUBMIT.REQ.DSA DSA trader status required (Upcoming Requirements)

**Source text (verbatim):**
> DSA trader status required for apps in the EU
> Since February 17, 2025
> Apps without trader status will be removed from the App Store in the European Union (EU) until trader status is provided and verified in order to comply with the Digital Services Act.
> DSA trader status required for app updates in the EU
> Since October 16, 2024
> Your trader status is required to submit app updates for apps distributed on the App Store in the European Union (EU), in order to comply with the Digital Services Act.

**Applies to:** Apps distributed on the App Store in the EU

- **[SUBMIT-26]** Is trader status provided and verified for an app distributed in the EU?
  - quote: "Your trader status is required to submit app updates for apps distributed on the App Store in the European Union (EU), in order to comply with the Digital Services Act."
  - surface: asc
  - verify: Business > Agreements > Compliance > Digital Services Act shows completed status; App Information > App Store Regulations and Permits > Digital Services Act shows a trader status for this app; Pricing and Availability lists EU storefronts.
  - fix: Complete SUBMIT.DSA steps (Complete Compliance Requirements).

## SUBMIT.REQ.RECEIPT App Store Receipt Signing / Intermediate certificate (Upcoming Requirements)

**Source text (verbatim):**
> App Store Receipt Signing Intermediate Certificate
> Since January 24, 2025
> The SHA-1 intermediate certificate used for signing App Store receipts expires on January 24, 2025. If your app performs on-device receipt validation, make sure it supports the SHA-256 algorithm; alternatively, use the AppTransaction and Transaction APIs to verify App Store transactions.
> For more details, view TN3138: Handling App Store receipt signing certificate change.
> Intermediate certificate update
> Since August 16, 2023
> Receipts in new apps and app updates submitted to the App Store, as well as all apps in sandbox, will be signed with the SHA‑256 intermediate certificate. If your app verifies App Store transactions using the AppTransaction and Transaction APIs, or the verifyReceipt web service endpoint, no action is required.
> If your app validates App Store receipts on device, make sure your app will support the SHA-256 version of this certificate. New apps and app updates that don’t support the SHA-256 version of this certificate will no longer be accepted by the App Store starting August 16, 2023.

**Applies to:** Apps that perform on-device receipt validation

- **[SUBMIT-27]** If the app validates App Store receipts on device, does the validation support SHA-256 (or does the app use AppTransaction/Transaction instead)?
  - quote: "If your app performs on-device receipt validation, make sure it supports the SHA-256 algorithm; alternatively, use the AppTransaction and Transaction APIs to verify App Store transactions."
  - surface: code
  - verify: `grep -rn "appStoreReceiptURL\|PKCS7\|SecTrust\|SHA1\|sha1\|AppleIncRootCertificate\|TPInAppReceipt\|ReceiptValidator" --include=*.swift --include=*.m --include=*.h`; check any on-device verification code/library for SHA-1-only digest handling. Pass if not found, or if StoreKit 2 `AppTransaction`/`Transaction` is used, or the library supports SHA-256.
  - fix: Migrate to StoreKit 2 `AppTransaction.shared` / `Transaction.currentEntitlements` verification, or update the receipt validation library to a SHA-256-capable version.

## SUBMIT.REQ.PRIVACY-API Approved reasons for APIs (Upcoming Requirements)

**Source text (verbatim):**
> Approved reasons for APIs
> Since May 1, 2024
> You’ll need to include approved reasons for the listed APIs used by your app’s code (including from third-party SDKs) to upload a new or updated app to App Store Connect.

**Applies to:** Apps (and their third-party SDKs) that use the listed APIs

- **[SUBMIT-28]** Does the app (and each third-party SDK) include approved reasons for every listed API it uses?
  - quote: "You’ll need to include approved reasons for the listed APIs used by your app’s code (including from third-party SDKs) to upload a new or updated app to App Store Connect."
  - surface: code
  - verify: Find PrivacyInfo.xcprivacy files (`find . -name PrivacyInfo.xcprivacy`, including inside Pods/SPM checkouts/xcframeworks); confirm NSPrivacyAccessedAPITypes entries exist for each required-reason API category the code uses (see the privacy reference file for the API category list).
  - fix: Add/complete NSPrivacyAccessedAPITypes in the app's PrivacyInfo.xcprivacy; update SDKs to versions that ship their own privacy manifest.

## SUBMIT.REQ.GAMECENTER Game Center entitlement and configuration requirement (Upcoming Requirements)

**Source text (verbatim):**
> Game Center entitlement and configuration requirement
> Since August 16, 2023
> New apps and app updates for iOS, iPadOS, or tvOS offering Game Center features need to include the Game Center entitlement in the entitlements plist and have Game Center features configured in App Store Connect before you can submit them to the App Store.

**Applies to:** iOS, iPadOS, or tvOS apps offering Game Center features

- **[SUBMIT-29]** If the app uses Game Center, does its entitlements plist include the Game Center entitlement and are Game Center features configured in App Store Connect?
  - quote: "need to include the Game Center entitlement in the entitlements plist and have Game Center features configured in App Store Connect before you can submit them to the App Store"
  - surface: code
  - verify: `grep -rn "import GameKit\|GKLocalPlayer" --include=*.swift --include=*.m`; if found, check the target's .entitlements for `com.apple.developer.game-center`; in ASC > (app) > Game Center (Services/Features), confirm Game Center is enabled with leaderboards/achievements configured as used in code.
  - fix: Add the Game Center capability in Xcode (Signing & Capabilities), and configure Game Center for the app version in App Store Connect.

## SUBMIT.REQ.NOTARY Apple notary service update (Upcoming Requirements)

**Source text (verbatim):**
> Apple notary service update
> Since November 1, 2023
> If you notarize Mac software with the Apple notary service using the altool command-line utility or Xcode 13 or earlier, you’ll need to transition to the notarytool command-utility or upgrade to Xcode 14 or later. Starting November 1, 2023, the Apple notary service will no longer accept uploads from altool or Xcode 13 or earlier. Existing notarized software will continue to function properly.

**Applies to:** Mac software notarized with the Apple notary service
**Requires:** macos, ipad

- **[SUBMIT-30]** Does any notarization script use notarytool (or Xcode 14+) rather than altool?
  - quote: "the Apple notary service will no longer accept uploads from altool or Xcode 13 or earlier"
  - surface: code
  - verify: `grep -rn "altool.*--notarize\|notarize-app" .` across scripts, Makefiles, fastlane, CI workflows. Pass if none.
  - fix: Replace with `xcrun notarytool submit ... --wait`.

## SUBMIT.REQ.HISTORY Earlier and informational entries (Upcoming Requirements)

**Source text (verbatim):**
> Transition from XML to the App Store Connect API
> Since July 15, 2024
> Game Center management will no longer be supported by the XML feed as of July 15, 2024.
> Support for in-app purchases, subscriptions, metadata, and app pricing ended on November 9, 2022.
> You can manage this content via the App Store Connect REST API, which makes it easy to customize and automate your workflows.
> Xcode 15
> Since April 29, 2024
> Apps uploaded to App Store Connect must be built with Xcode 15 for iOS 17, iPadOS 17, tvOS 17, or watchOS 10 starting April 29, 2024.
> tvOS 16.1 SDK
> Since July 31, 2023
> All tvOS apps submitted to the App Store must be built with Xcode 14.1 and tvOS 16.1 SDK or later.
> App Store global pricing update in May
> Since May 9, 2023
> Pricing for existing apps and one-time in-app purchases will be updated with enhanced global prices across App Store storefronts using your current price in the United States as the basis—unless you’ve made relevant updates after March 8, 2023. This update has been deferred to later this year for the App Store in Türkye.
> Xcode 14.1
> Since April 25, 2023
> iOS and iPadOS apps submitted to the App Store must be built with Xcode 14.1 and the iOS 16.1 SDK or later. And watchOS apps submitted to the App Store must be built with Xcode 14.1 and the watchOS 9.1 SDK or later.
> Transition from subscription reports version 1.2 to 1.3
> Since March 1, 2023
> Subscription reports version 1.2 will no longer be available as of March 1, 2023. If you automatically download subscription reports using the App Store Connect API or Reporter, please update your query parameter to version 1.3 if you haven’t already.
> Transition from XML to App Store Connect API
> Since November 9, 2022
> The XML feed will no longer support in-app purchases, subscriptions, metadata, or app pricing as of November 9, 2022. You can manage this content via the App Store Connect REST API, which makes it easy to customize and automate your workflows.
> The XML feed will continue to support existing Game Center management functionality.

**Applies to:** Informational — the Xcode/SDK minimums in this unit are lower than the current minimum in SUBMIT.REQ.SDK (Xcode 26), so SUBMIT-22 covers them.

- **[SUBMIT-31]** If the developer automates subscription report downloads, do they request version 1.3?
  - quote: "please update your query parameter to version 1.3 if you haven’t already"
  - surface: code
  - verify: `grep -rn "salesReports\|Subscription.*1\.2\|version=1\.2\|reportVersion" .` in scripts/CI that call the App Store Connect API or Reporter.
  - fix: Change the report version parameter to 1_3 / 1.3.

## SUBMIT.SUBMITTING Submit your apps and games today

**Source text (verbatim):**
> Update for the latest OS releases
> Build and test with Xcode 27, which supports the latest SDKs for iOS, iPadOS, macOS, tvOS, visionOS, and watchOS to take advantage of the latest advancements in Apple platforms. Make sure your apps and games work as expected on Apple devices running the latest OS releases. Starting April 2027, apps and games uploaded to App Store Connect need to meet the following minimum requirements.
> - iOS and iPadOS apps must be built with the iOS & iPadOS 27 SDK or later, and target iOS 15 or later
> - tvOS apps must be built with the tvOS 27 SDK or later
> - visionOS apps must be built with the visionOS 27 SDK or later
> - watchOS apps must be built with the watchOS 27 SDK or later
>
> App Review
> The guiding principle of the App Store is simple — we want to provide a trusted experience for people to get apps and games, and a great opportunity for developers to succeed. To do this, Apple reviews submissions to confirm they're safe, secure, and reliable. This includes apps and app updates, as well as bundles, Apple In-App Purchases, In-App Events, App Store metadata, and other content you submit for review. As you plan and build, get acquainted with the App Review Guidelines early on in your app or game’s development in order to make appropriate design decisions and help your review process goes as smooth as possible.
> Product page
> Make sure your app’s name, icon, description, screenshots, app previews, and keywords are ready for your App Store product page. You can also take this opportunity to update your subtitle and promotional text, and choose to promote any new Apple In-App Purchases. Before submitting, make sure to:
> Complete the age rating questionnaire. Respond to the age rating questionnaire in App Store Connect. This questionnaire includes a list of content descriptors, in-app controls, and capabilities that allow you to specify the frequency of each content type in your app. An Apple global age rating is provided based on your responses, as well as additional region-specific ratings if required. Learn how to set an app rating.
> Provide your app’s privacy details. Enter all necessary information about your app’s privacy practices, including the practices of third‑party partners whose code you integrate into your app, in App Store Connect. These details inform the Privacy Nutrition Label that appears on your product page and are required in order to submit new apps and app updates to the App Store.
> Indicate your accessibility support. You can share information in App Store Connect about your app or game’s support — such as whether it includes VoiceOver, Voice Control, Larger Text, Captions, and more. Based on this information, an Accessibility Nutrition Label will appear on your App Store product page, specific to each platform you support. If you’d like, you can also add a URL on your App Store product page that links people to a website with even more details.
> Availability options
> Verify required device capabilities. The App Store is designed to provide users with apps that work seamlessly with their devices’ capabilities. Verify that your information property list (info.plist) is compatible with any device requirements when submitting a new app that takes advantage of the latest technologies.
> Explore universal purchase. With universal purchase, people can discover and enjoy your app or game across their Apple devices with a single purchase. Apple In-App Purchases and subscriptions can also easily be set up and shared across platforms. Your product page shows the other platforms your app supports along with screenshots, and you’ll be able to promote your app using a single URL across your marketing channels.
> Offer iPadOS and iOS apps on Mac computers and Apple Vision Pro. Most iPadOS and iOS apps can run unmodified on Apple Vision Pro and on Mac computers with Apple silicon, so your app can easily extend to these platforms — with no additional work required. By default, your compatible apps are published automatically on the App Store for Apple Vision Pro or Mac using the metadata you’ve already provided in App Store Connect.

**Applies to:** All apps (April 2027 minimums: apps and games uploaded to App Store Connect starting April 2027)

- **[SUBMIT-32]** (Forward-looking, April 2027) Is the iOS/iPadOS app built with the iOS & iPadOS 27 SDK or later and targeting iOS 15 or later?
  - quote: "iOS and iPadOS apps must be built with the iOS & iPadOS 27 SDK or later, and target iOS 15 or later"
  - surface: code
  - verify: IPHONEOS_DEPLOYMENT_TARGET in project.pbxproj / xcconfig / Package.swift ≥ 15.0; DTSDKName in archive Info.plist is iphoneos27.x or later. Report as WARN before April 2027, FAIL from April 2027.
  - fix: Raise IPHONEOS_DEPLOYMENT_TARGET to 15.0+, build with Xcode 27.
- **[SUBMIT-33]** (Forward-looking, April 2027) Are tvOS, visionOS, and watchOS targets built with their 27 SDK or later?
  - quote: "tvOS apps must be built with the tvOS 27 SDK or later"
  - surface: code
  - verify: For each tvOS/visionOS/watchOS target, read DTSDKName from the archived bundle's Info.plist (appletvos27 / xros27 / watchos27 or later). WARN before April 2027.
  - fix: Build with Xcode 27 or later.
- **[SUBMIT-34]** Are the app's name, icon, description, screenshots, app previews (if used), and keywords ready on the product page?
  - quote: "Make sure your app’s name, icon, description, screenshots, app previews, and keywords are ready for your App Store product page."
  - surface: asc
  - verify: Version page for each localization: Name, Description, Keywords, Screenshots populated; the build supplies an app icon (AppIcon in Assets.xcassets in code).
  - fix: Complete missing product page fields per localization.
- **[SUBMIT-35]** Has the age rating questionnaire been completed?
  - quote: "Complete the age rating questionnaire."
  - surface: asc
  - verify: App Information > Age Ratings shows a computed rating.
  - fix: See SUBMIT.AGE.SET.
- **[SUBMIT-36]** Have the app's privacy details (including third-party partners' practices) been entered in App Store Connect?
  - quote: "These details inform the Privacy Nutrition Label that appears on your product page and are required in order to submit new apps and app updates to the App Store."
  - surface: asc
  - verify: App Privacy page: data collection answers are published (not "Get Started"); cross-check against SDKs found in code (Podfile.lock, Package.resolved) and their PrivacyInfo.xcprivacy NSPrivacyCollectedDataTypes.
  - fix: Complete App Privacy responses covering the app and all third-party SDKs, then Publish.
- **[SUBMIT-37]** (Recommended — Apple lists it under "Before submitting, make sure to" but says you "can share" this information) Has accessibility support been indicated in App Store Connect?
  - quote: "Indicate your accessibility support. You can share information in App Store Connect about your app or game’s support"
  - surface: asc
  - verify: App Store Connect > (app) > Accessibility (Accessibility Nutrition Labels) for each platform: entries are set. Report as WARN, not FAIL, if missing.
  - fix: manual — developer evaluates the app against Apple's evaluation criteria and declares supported features.
- **[SUBMIT-38]** Is the Info.plist compatible with the device requirements (required device capabilities) of the app?
  - quote: "Verify that your information property list (info.plist) is compatible with any device requirements when submitting a new app that takes advantage of the latest technologies."
  - surface: code
  - verify: Read UIRequiredDeviceCapabilities in Info.plist (and INFOPLIST_KEY_UIRequiredDeviceCapabilities build setting); compare to frameworks actually required (e.g., ARKit → arkit, Metal → metal, NFC). Flag capabilities listed but not needed, or hard requirements missing.
  - fix: Edit UIRequiredDeviceCapabilities to list only the capabilities the app cannot run without.

## SUBMIT.AGE.SET Set an app age rating

**Source text (verbatim):**
> An age rating is a required app information property that helps users assess the content and any potentially objectionable material within your app or game. This rating supports the functionality of parental controls, allowing parents and guardians to establish a safe online environment for children. As a developer, you can deliver age-appropriate experiences tailored for users across all age groups.
> To determine the age rating of your app, respond to the age rating questionnaire in App Store Connect. This questionnaire includes a list of content descriptors, in-app controls, and capabilities that allow you to specify the frequency of each content type in your app. Your selections are then translated into an Apple global age rating, as well as additional region-specific ratings if required. Learn about age rating values and definitions.
> This process helps you understand how different types of content can impact your app’s rating across various regions, enabling you to make informed declarations of frequency of the content and features in your app.
> Depending on your responses, an age rating is assigned to each country or region based on their specific age suitability standards. This rating will be displayed on the App Store for that country or region and will remain consistent across all platforms. Learn about age rating values with region-specific requirements for Australia, Brazil, and Korea.
> Notes:
> Age ratings for an app may vary based on the OS version. View age range value details for Apple devices running a minimum of iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, visionOS 26, and watchOS 26. View details for Apple devices running an earlier OS version.
> An Unrated app can’t be published on the App Store. It may be published on alternative app marketplaces or websites.
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
> Set an app age rating
> In Apps, select the app you want to view.
> In the sidebar, under General, click App Information.
> Tip: To learn more about and view examples of the features and content used to determine age ratings, select a category from the panel of examples on the App Information Page. You can also browse Age rating categories.
> Below Age Ratings, click the Set Up Age Ratings button.
> When the dialog box appears, review the list of in-app controls and capabilities options, and select any that your app includes that can restrict content, then click Next.
> Navigate through each section of the progress bar, answering the questions and selecting the appropriate level of frequency for each content description, then click Next.
> Made for Kids category on the App Store
> If your calculated rating is 4+ or 9+ and you want your app to also display in the Kids category on the App Store, under Age Categories and Override, choose Made for Kids and from the menu, select the appropriate age range for your app. You can’t change this selection once your app is approved by App Review. The app and all subsequent updates will need to follow the Kids category guidelines.
> Note: You can’t select the Made for Kids option for visionOS apps, and apps in the Kids category can’t be made available on visionOS apps.
> Override to higher age rating
> To increase the rating of your app to a rating that exceeds the rating assigned by Apple, choose Override to Higher Age Rating and select the appropriate rating from the menu. App Store will display this specified age rating, and the content descriptions will still reflect your questionnaire answers.
> If your app will be distributed through alternative app marketplaces or your website in the European Union and you believe your app is Unrated, select Unrated from the menu options under Override to Higher Age Rating.
> Note:
> If your app has a EULA with minimum age requirements that exceed the rating that Apple calculated, you must override to a rating that adheres to the requirements.
> The override will apply in all regions where your app is available and may override to a different rating value per region based on region-specific requirements. Learn about age rating values with region-specific requirements for Australia, Brazil, and Korea.
> If your app has a dedicated website with details on age suitability, you can provide the URL in the field provided under Age Suitability URL (Optional).
> Click Save. The dialog box will close, returning you to the App Information page. Here, you can view your global and region-specific ratings . Click on each panel for details on the age ratings and the specific countries and regions they apply to.
> To edit your age rating, click App Information in the sidebar, then click Edit at the top of the page.
> Note: You can view the age ratings for Apple devices running an earlier OS version than 26 under the Operating Systems Earlier than Version 26 section. Learn more.
> Override age rating for the Republic of Korea
> App Review may contact you if the Korean Games Rating and Administration Committee (GRAC) issues a region-specific rating that differs from your app's existing age rating. If you receive this notice, you need to update your app's age rating for the App Store in Korea by providing your Rating Classification Number (RCN) and submitting a new version of your app to App Review.
> In Apps, select your app.
> In the sidebar, under General, click App Information.
> In the Age Ratings section, next to Republic of Korea, click Add RCN.
> In the dialog that appears, enter your RCN and select the rating you received from GRAC.
> Select the checkbox confirming that this is the official rating issued by GRAC for your app, then click Save.
> Note: If an error appears after clicking Save, address the error message and click Save again.
> You can edit your RCN or override at any time before submitting your app for review by clicking Edit RCN next to Republic of Korea. From there, you can select a new rating, or clear your RCN and rating together by clicking Remove. While your app is in review, you can only view your RCN and rating by clicking View RCN. Once your app is approved, your RCN and rating are locked and can no longer be edited.

**Applies to:** All apps

- **[SUBMIT-39]** Does the app have an age rating other than Unrated (required to publish on the App Store)?
  - quote: "An Unrated app can’t be published on the App Store."
  - surface: asc
  - verify: App Information > Age Ratings: global rating is 4+, 9+, 13+, 16+ or 18+, and Override to Higher Age Rating is not set to Unrated.
  - fix: Complete the questionnaire; if the content drives an Unrated result, the content must be removed for App Store distribution (manual — developer decision).
- **[SUBMIT-40]** Do the selected in-app controls and capabilities match what the app actually includes?
  - quote: "review the list of in-app controls and capabilities options, and select any that your app includes"
  - surface: code
  - verify: Scan code for each item in SUBMIT.AGE.VALUES "Age rating categories" (In-App Controls and Capabilities): see SUBMIT-47 to SUBMIT-54 for concrete greps; compare with the selections in App Information > Age Ratings.
  - fix: Edit the age rating questionnaire to match the detected features.
- **[SUBMIT-41]** Has an appropriate frequency been selected for every content description?
  - quote: "answering the questions and selecting the appropriate level of frequency for each content description"
  - surface: manual
  - verify: Review each section answer in the questionnaire against the app's content (exercise the app at runtime for mature themes, violence, sexuality, gambling-like features).
  - fix: manual — developer re-answers sections whose frequency does not reflect the content.
- **[SUBMIT-42]** If Made for Kids is selected, is the calculated rating 4+ or 9+?
  - quote: "If your calculated rating is 4+ or 9+ and you want your app to also display in the Kids category on the App Store"
  - surface: asc
  - verify: App Information > Age Ratings > Age Categories and Override: Made for Kids selected only when the calculated rating is 4+ or 9+, with an age range chosen.
  - fix: Remove Made for Kids, or remove content that raises the rating above 9+ (manual decision).
- **[SUBMIT-43]** If the app is Made for Kids (or intends to be), does the developer accept that the selection is permanent and that all updates must follow the Kids category guidelines?
  - quote: "You can’t change this selection once your app is approved by App Review. The app and all subsequent updates will need to follow the Kids category guidelines."
  - surface: manual
  - verify: Ask the developer to confirm; cross-check code for third-party analytics/ads SDKs that conflict with Kids category guidelines (see guideline reference files).
  - fix: manual — requires developer decision.
- **[SUBMIT-44]** Is Made for Kids not selected for an app offered on visionOS?
  - quote: "You can’t select the Made for Kids option for visionOS apps, and apps in the Kids category can’t be made available on visionOS apps."
  - surface: code
  - verify: Check for visionOS targets (SDKROOT = xros / SUPPORTED_PLATFORMS contains xros) and ASC visionOS availability ("Manage availability of iPhone and iPad apps on Apple Vision Pro"); if present, Made for Kids must be off.
  - fix: Remove visionOS availability, or don't use Made for Kids (manual decision).
- **[SUBMIT-45]** If the app has a EULA with a minimum age above the calculated rating, is the rating overridden to adhere to it?
  - quote: "If your app has a EULA with minimum age requirements that exceed the rating that Apple calculated, you must override to a rating that adheres to the requirements."
  - surface: asc
  - verify: Read App Information > License Agreement (custom EULA) and the app's terms of service for a minimum age; compare with the Apple-calculated rating; check Override to Higher Age Rating.
  - fix: Choose Override to Higher Age Rating with a value ≥ the EULA minimum age.
- **[SUBMIT-46]** If App Review sent a GRAC notice for Korea, has the RCN and GRAC rating been entered before submitting the new version?
  - quote: "you need to update your app's age rating for the App Store in Korea by providing your Rating Classification Number (RCN) and submitting a new version of your app to App Review"
  - surface: asc
  - verify: App Review messages for a GRAC notice; App Information > Age Ratings > Republic of Korea shows an RCN.
  - fix: Click Add RCN, enter the RCN and GRAC rating, confirm the checkbox, Save, then submit a new version.

## SUBMIT.AGE.VALUES Age ratings values and definitions

**Source text (verbatim):**
> The age rating is a required app information field used for property used by the parental controls. These controls enable parents and guardians to establish a safe online environment for children. As a developer, you can deliver age-appropriate experiences tailored for users across all age groups.
> In App Store Connect, you'll find a list of content descriptors, in-app controls, and capabilities that allow you to specify the frequency or presence of each in your app. Apple generates appropriate ratings based on your answer to the age rating questionnaire. Learn how to set an app age rating.
> The tables below provide detailed information about the different age rating categories and age rating values by region.
> Notes:
> An Unrated app can't be published on the App Store. It may be published on alternative app marketplaces or websites.
> Age ratings for an app may vary based on the OS version. View age range value details for Apple devices running a minimum of iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, visionOS 26, and watchOS 26. View details for Apple devices running an earlier OS version.
>
> Age rating categories
>
> | Category | Examples of included features and content |
> |---|---|
> | In-App Controls | Parental Controls: Settings or tools that allow parents/guardians to monitor, manage, or restrict a child's access to in-app content or features that may not be suitable. May include: tools to enable content blocking or filtering; setting usage limits; or restrictions on using certain features, such as making purchases or using communication features. |
> | In-App Controls | Age Assurance: Mechanism to confirm an individual's age meets the age requirement for accessing specific content or services. May include: declared age range API; age estimation capabilities; age verification via government-issued passport, drivers license, national ID, or other means of age assurance. |
> | Capabilities | Unrestricted Web Access: Users can navigate to any webpage within the app or freely browse the web. May include: embedded browser functionality or browser app. |
> | Capabilities | User-Generated Content: Includes the broad distribution of content created by users as a component of the app's intended user experience. May include: broadly distributed videos, photos, text, and/or audio created by users of the app. |
> | Capabilities | Social Media: Redistribution, amplification, or interaction with user-generated content through a social feed or similar discovery method that visibly spreads content to many users. May include: feeds that allow users to engage with and amplify user-generated content through features such as views, likes, comments, and shares. |
> | Capabilities | Social Media Disabled for Users Under 13: Users under 13 don't have access to social media capabilities. At a minimum, the Declared Age Range API is called to check users' age ranges before enabling social media features. Only age-appropriate UGC is delivered. |
> | Capabilities | Messaging and Chat: Users can directly communicate with one another through features within the app. May include: text, voice and/or video chat, direct and/or group messaging, or public posting. |
> | Capabilities | Advertising: Paid promotion of products or services within the app. May include: banner ads, video and playable ads, rich media ads, or native ad formats. |
> | Mature Themes | Profanity or Crude Humor: Offensive or vulgar language that may be considered rude, obscene, or inappropriate. May include: swearing, derogatory slurs, insult-based humor, or jokes about bodily functions. |
> | Mature Themes | Horror/Fear Themes: Content or storylines that evoke feelings of anxiety, dread, or terror. May include: supernatural or psychological elements; body horror; or fear of the unknown, isolation, or death. |
> | Mature Themes | Alcohol, Tobacco, or Drug Use or References: References to or depictions of the consumption of alcohol, tobacco products, or other licit or illicit substances. May include: drunken behavior, cigarette smoking, or the taking of illegal drugs. |
> | Medical or Wellness | Medical or Treatment Information: Content that provides diagnoses or guidance around the management of medical conditions or health and wellness. May include: medication guidance, emergency medical care, or treatment information. |
> | Medical or Wellness | Health or Wellness Topics: Content that provides self-care or lifestyle recommendations. May include: calorie tracking, dieting advice, or exercise recommendations. |
> | Sexuality or Nudity | Mature or Suggestive Themes: Content that implies or indirectly references sexual or mature topics without being explicit or topics for older audiences due to the complex, intense, or sensitive nature, which may deal with real-world issues or content unsuitable for children. May include: sexual innuendo, sensual or suggestive imagery, censored or implied nudity, real-world crimes, psychological trauma or abuse, moral or ethical dilemmas, or war or political strife. |
> | Sexuality or Nudity | Sexual Content or Nudity: Non-explicit depictions of sexual behavior, including brief or partial nudity. May include: mild romantic intimacy, implied sexual activity, or erotic or sensual dialog. |
> | Sexuality or Nudity | Graphic Sexual Content and Nudity: Explicit, detailed depictions of sexual activity or nudity. May include: uncensored or full-frontal nudity; realistic, illustrative, or pornographic portrayals of sex. |
> | Violence | Cartoon or Fantasy Violence: Physical conflict or harm of an exaggerated or fantastical nature that can easily be distinguished from real life. May include: animated magic used to harm animals or animated human wrestling. |
> | Violence | Realistic Violence: Aggressive physical conflict or harm involving humans in lifelike situations. May include: a bloody nose from being punched, a shoot-out, or combat between characters. |
> | Violence | Prolonged Graphic or Sadistic Realistic Violence: Prolonged detailed or realistic-looking depictions of physical conflict. May include: realistic and/or extreme depictions of gore, human injury, or death. |
> | Violence | Guns or Other Weapons: References to or depictions of guns, weapons, or objects that may cause bodily harm. May include: guns, swords, or knives. |
> | Chance-Based Activities | Gambling: Betting or wagering using real money or in-game currency that may be exchanged for real money. May include: casino or card games, sports and non-sports betting, or lotteries and raffles. |
> | Chance-Based Activities | Simulated Gambling: Betting or wagering without using real money or in-game currency that can be exchanged for real money. |
> | Chance-Based Activities | Contests: Events that allow users to compete with one another for rankings, rewards, or the achievement of personal goals. May include: skill-based competitions, trivia quizzes, or sport or fitness contests |
> | Chance-Based Activities | Loot Boxes: Virtual containers that provide players with randomized virtual items for purchase. May include: randomized functional cards or cosmetic items for purchase. |
>
> Age rating values
> These ratings apply to all regions that don’t have any additional regional requirements.
>
> Rating
> Definition
> 4+
> Apps with this rating contain no objectionable material but may contain instances of the following content that may not be suitable for children under the age of 4:
> In-App Controls:
> Parental controls
> Age assurance
> Capabilities:
> User-generated content
> Messaging and chat
> Advertising
> Chance-Based Activities:
> Infrequent contests
> 9+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 9:
> Mature Themes
> Infrequent profanity and crude humor
> Infrequent horror or fear themes
> Medical or Wellness
> Health and wellness topics
> Sexuality or Nudity
> Infrequent mature or suggestive themes
> Violence
> Infrequent cartoon or fantasy violence
> Infrequent guns or other weapons
> Chance-Based Activities
> Loot boxes
> 13+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 13:
> Capabilities:
> Social media
> Social media disabled for users under 13
> Mature Themes:
> Frequent profanity and crude humor
> Frequent horror or fear themes
> Infrequent alcohol, tobacco, or drug use or references
> Medical or Wellness:
> Infrequent medical or treatment information
> Sexuality or Nudity:
> Infrequent sexual content or nudity
> Violence:
> Frequent cartoon or fantasy violence
> Infrequent realistic violence
> Frequent guns or other weapons
> Chance-Based Activities:
> Infrequent simulated gambling
> Frequent contests
> 16+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 16:
> Capabilities:
> Unrestricted web access
> Medical or Wellness:
> Frequent medical or treatment information
> Sexuality or Nudity:
> Frequent mature or suggestive themes
> 18+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 18:
> Mature Themes:
> Frequent alcohol, tobacco, or drug use or references
> Sexuality or Nudity:
> Frequent sexual content or nudity
> Violence:
> Frequent realistic violence
> Chance-Based Activities:
> Gambling
> Frequent simulated gambling
> Unrated
> Apps with this rating may contain instances of the following content that can’t be published on the App Store. It may be published on alternative app marketplaces or websites:
> Sexuality or Nudity:
> Infrequent or Frequent graphic sexual content and nudity
> Violence:
> Infrequent or Frequent prolonged graphic or sadistic realistic violence
>
> Australia age rating values
> As required by Australia’s guidelines for the classification of computer games, apps that have at least one of the following content descriptors will display the regional region-specific age rating. Note: Only the age rating values listed below differ from the age rating values.
>
> Rating
> Definition
> 16+
> Apps that contain:
> Capabilities:
> Social media
> Social media disabled for users under 13
> Chance-Based Activities:
> Loot boxes
> R 18+
> Apps that contain:
> Chance-Based Activities:
> Infrequent simulated gambling
>
> If we’re notified by the regulator that your app doesn’t meet their guidelines or requires a region-specific rating, you’ll receive a message from App Review. If you receive this message, follow the instructions and re-submit your app for review.
>
> Brazil age rating values
> As required by the Brazilian Ministry of Justice and Public Security (MJSP), the App Store uses a different set of region-specific rating pictograms and descriptors for self-rated apps, than for ratings officially issued by the MJSP.
> Official Brazil region-specific ratings and descriptors apply to apps that were issued an official rating by the MJSP. If a rating or descriptor has been issued to your app by the MJSP, Apple will update your regional rating and/or descriptors on your behalf and it'll display on the App Store in Brazil.
> Apps that include fixed-odds betting (gambling) features require a valid Brazilian fixed-odds betting license from the Secretariat of Prizes and Bets (SPA) to be distributed on the App Store in Brazil. When submitting a new app update, provide your license details and any supporting documentation in the App Review Information section in App Store Connect. Enter your license details in the Notes field and attach any supporting documents using the file attachment field.
> Review App Review Guideline 5.3.4. to ensure gambling app compliance.
> Possible values for official Brazil age pictograms are:
> Possible values for self-rated Brazil age pictograms are:
>
> Rating
> Definition
> AL
> Apps that contain no objectionable material but may contain instances of the following content:
> In-App Controls:
> Parental controls
> Age assurance
> A6
> Apps that contain:
> Capabilities:
> User-generated content
> Violence:
> Infrequent cartoon or fantasy violence
> Chance-Based Activities:
> Infrequent contests
> A10
> Apps that contain:
> Mature Themes:
> Infrequent profanity and crude humor
> Infrequent horror or fear themes
> Medical or Wellness:
> Health and wellness topics
> Violence:
> Infrequent guns or other weapons
> A12
> Apps that contain:
> Capabilities:
> Advertising
> Messaging and chat
> Mature Themes:
> Frequent profanity and crude humor
> Medical or Wellness:
> Infrequent medical or treatment information
> Sexuality or Nudity:
> Infrequent mature or suggestive themes
> Infrequent sexual content or nudity
> Violence:
> Frequent cartoon or fantasy violence
> Infrequent realistic violence
> Frequent guns or other weapons
> Chance-Based Activities:
> Infrequent simulated gambling
> A14
> Apps that contain:
> Mature Themes:
> Frequent horror or fear themes
> Infrequent alcohol, tobacco, or drug use or references
> A16
> Apps that contain:
> Capabilities:
> Unrestricted web access
> Infrequent guns or other weapons
> Social media
> Social media disabled for users under 13
> Mature Themes:
> Frequent alcohol, tobacco, or drug use or references
> Medical or Wellness:
> Frequent medical or treatment information
> A18
> Apps that contain:
> Sexuality or Nudity:
> Frequent mature or suggestive themes
> Frequent sexual content or nudity
> Violence:
> Frequent realistic violence
> Chance-Based Activities:
> Frequent gambling
> Frequent simulated gambling
> Loot boxes
>
> Republic of Korea age rating values
> For all apps made available in Korea, the following region-specific rating values will display:
> Note: Apps and games with Frequent or Intense simulated gambling content are only available on the App Store in Korea if you provide a Rating Classification Number (RCN).
>
> Rating
> Definition
> All
> Apps that contain:
> In-App Controls:
> Parental controls
> Age assurance
> Capabilities:
> User-generated content
> Messaging and chat
> Advertising
> Mature Themes:
> Infrequent horror or fear themes
> Medical or Wellness:
> Health or wellness topics
> Violence:
> Infrequent cartoon or fantasy violence
> Infrequent guns or other weapons
> Chance-Based Activities:
> Infrequent contests
> Loot boxes
> 12+
> Apps that contain:
> Mature Themes:
> Infrequent profanity and crude humor
> Frequent profanity and crude humor
> Frequent horror or fear themes
> Infrequent alcohol, tobacco, or drug use or reference
> Medical or Wellness:
> Infrequent medical or treatment information
> Sexuality or Nudity:
> Infrequent mature or suggestive themes
> Frequent mature or suggestive themes
> Infrequent sexual content or nudity
> Violence:
> Frequent cartoon or fantasy violence
> Infrequent realistic violence
> Frequent guns or other weapons
> Chance-Based Activities:
> Infrequent simulated gambling
> 15+
> Apps that contain:
> Capabilities:
> Unrestricted web access
> Social media
> Social media disabled for users under 13
> Medical or Wellness:
> Frequent medical or treatment information
> 19+
> Apps that contain:
> Mature Themes:
> Frequent alcohol, tobacco, or drug use or references
> Sexuality or Nudity:
> Frequent sexual content or nudity
> Violence:
> Frequent realistic violence
> Chance-Based Activities:
> Frequent simulated gambling
>
> Note: You’ll receive a message from App Review if the Korean Games Rating and Administration Committee(GRAC) issues an official rating for your app that is different from your app’s age rating. If you receive this notice, follow the instructions in the override age rating for Korea section and re-submit your app for review.
>
> Vietnam age rating values
> As required by Article 38 of Vietnam Decree 147, apps that have at least one of the following content descriptors will display the region-specific age rating.
>
> Rating
> Definition
> 00+
> Apps with this rating contain no objectionable material but may contain instances of the following content:
> In-App Controls:
> Parental controls
> Age assurance
> Capabilities:
> User-generated content
> Messaging and chat
> Advertising
> Chance-Based Activities:
> Infrequent contests
> 12+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 12:
> Mature Themes:
> Infrequent profanity and crude humor
> Frequent profanity and crude humor
> Infrequent horror or fear themes
> Frequent horror or fear themes
> Infrequent alcohol, tobacco, or drug use or reference
> Medical or Wellness:
> Infrequent medical or treatment information
> Health and wellness topics
> Sexuality or Nudity:
> Infrequent mature or suggestive themes
> Infrequent sexual content or nudity
> Violence:
> Infrequent cartoon or fantasy violence
> Frequent cartoon or fantasy violence
> Infrequent guns or other weapons
> Chance-Based Activities:
> Frequent contests
> Loot boxes
> 16+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 16:
> Capabilities:
> Unrestricted web access
> Social media
> Social media disabled for users under 13
> Medical or Wellness:
> Frequent medical or treatment information
> Sexuality or Nudity:
> Frequent mature or suggestive themes
> Violence:
> Infrequent realistic violence
> Frequent guns or other weapons
> Chance-Based Activities:
> Infrequent simulated gambling
> 18+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 18:
> Mature Themes:
> Frequent alcohol, tobacco, or drug use or references
> Sexuality or Nudity:
> Frequent sexual content or nudity
> Violence:
> Frequent realistic violence
> Chance-Based Activities:
> Frequent simulated gambling
> Gambling
>
> Age ratings on OS versions earlier than 26
> The age rating is a required app information field used for parental controls. These controls enable parents and guardians to establish a safe online environment for children. As a developer, you can deliver age-appropriate experiences tailored for users across all age groups. Learn more about how parents approve what kids buy with ask to buy.
> View the age ratings that'll be displayed for Apple devices running an earlier OS version than 26 in the Operating Systems Earlier than Version 26 section under Age Ratings in App Store Connect.
>
> Global age ratings
>
> Rating
> Definition
> 4+
> Apps with this rating contain no objectionable material.
> 9+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 9:
> Infrequent or mild cartoon or fantasy violence
> Infrequent or mild profanity or crude humor
> Infrequent or mild mature, suggestive, or horror or fear themed
> 12+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 12:
> Infrequent or mild medical or treatment-focused content
> Infrequent or mild references to alcohol, tobacco, or drug use
> Infrequent or mild sexual content or nudity
> Frequent or intense contests
> Frequent or intense profanity or crude humor
> Frequent or intense horror or fear themed content
> Frequent or intense cartoon or fantasy violence
> Infrequent or mild occurrences of realistic violence
> Infrequent or mild simulated gambling
> 17+
> Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 17:
> Unrestricted web access, such as with an embedded browser
> Gambling
> Frequent or intense simulated gambling
> Frequent or intense mature or suggestive content
> Frequent or intense medical or treatment-focused content
> Frequent or intense references to alcohol, tobacco, or drug use
> Frequent or intense sexual content or nudity
> Frequent or intense realistic violence
> Unrated
> Apps with this rating may contain instances of the following content that can’t be published on the App Store. It may be published on alternative app marketplaces or websites:
> Infrequent or mild graphic sexual content and nudity
> Frequent or intense graphic sexual content and nudity
> Infrequent or mild prolonged graphic or sadistic realistic violence
> Frequent or intense prolonged graphic or sadistic realistic violence
>
> Australia regional ratings
> As required by Australia’s guidelines for the classification of computer games, apps with Games as the primary or secondary category that have at least one of the following content descriptions will display an additional regional rating along with their Apple global age rating. The relevant regional rating will display on the App Store in Australia for iOS 18, macOS 15, tvOS 18, watchOS 11, and visionOS 2 or later.
>
> | Content description | Region-specific rating |
> |---|---|
> | App that contains purchasable loot boxes |  |
> | App with any instances of simulated gambling |  |
>
> Brazil regional ratings
> As required by the Brazilian Ministry of Justice and Public Security (MJSP), the App Store uses a different set of regional rating pictograms and descriptors for self-rated apps, than for ratings officially issued by the MJSP.
> Official Brazil regional ratings apply to apps that were issued an official rating and/or descriptors by the MJSP. If a rating or descriptor has been issued to your app by the MJSP, Apple will update your regional rating and/or descriptors on your behalf. The updated regional rating will display on the App Store in Brazil for iOS 16.2, iPadOS 16.2, macOS 13.1, and tvOS 16.2, or later.
> Possible values for official Brazil age pictograms are:
> Possible values for self-rated Brazil age pictograms are:
> France regional rating
> As required by the Agence Nationale des Fréquences ("ANFR"), apps with a 17+ Apple global age rating will display an additional regional rating of 18+ on the App Store in France for iOS 18, macOS 15, tvOS 18, watchOS 11, and visionOS 2 or later.
> Republic of Korea regional ratings
> As required by the Korean Games Rating and Administration Committee(GRAC), apps in the Games or Entertainment categories (primary or secondary) and/or apps with Frequent/Intense instances of Simulated Gambling will display an additional regional rating along with their Apple global age rating. The relevant regional rating will display on the App Store in Republic of Korea for iOS 18, macOS 15, tvOS 18, watchOS 11, and visionOS 2 or later.
> Possible values for Korea regional ratings are:
>
> | Apple global age ratings | Region-specific rating |
> |---|---|
> | 4+ |  |
> | 9+ |  |
> | 12+* |  |
>
> * The GRAC may issue a KR-15 regional rating with an updated pictogram, or text that indicates KR-19 regional age rating for some apps.

Note: On Apple's page the Region-specific rating column of the Australia and Republic of Korea regional ratings tables shows pictogram images, not text.

**Applies to:** All apps (regional rows: apps available in the named region)

- **[SUBMIT-47]** If users can navigate to any webpage within the app, is Unrestricted Web Access declared?
  - quote: "Unrestricted Web Access: Users can navigate to any webpage within the app or freely browse the web."
  - surface: code
  - verify: `grep -rn "WKWebView\|SFSafariViewController\|WebView(\|UIWebView" --include=*.swift --include=*.m`; inspect whether the URL is user-controlled (address/search field, arbitrary link following without a domain allowlist in `decidePolicyFor navigationAction`). Compare with Capabilities answer in ASC.
  - fix: Declare Unrestricted Web Access in the questionnaire, or restrict navigation to an allowlist of domains in code.
- **[SUBMIT-48]** If the app broadly distributes content created by users, is User-Generated Content declared?
  - quote: "User-Generated Content: Includes the broad distribution of content created by users as a component of the app's intended user experience."
  - surface: code
  - verify: Look for upload/post/share flows to a backend that other users can view (e.g., PhotosPicker/UIImagePickerController + upload calls, "post", "publish", "feed" models, Firestore/Supabase collections read by other users). Compare with ASC answer.
  - fix: Declare User-Generated Content in the questionnaire.
- **[SUBMIT-49]** If the app has a social feed that redistributes/amplifies UGC (views, likes, comments, shares), is Social Media declared?
  - quote: "Social Media: Redistribution, amplification, or interaction with user-generated content through a social feed or similar discovery method that visibly spreads content to many users."
  - surface: code
  - verify: Grep for feed/like/comment/share/follow models and views (`like`, `comment`, `follow`, `Feed`, `Timeline`). Compare with ASC answer.
  - fix: Declare Social Media in the questionnaire.
- **[SUBMIT-50]** If "Social Media Disabled for Users Under 13" is declared, does the app call the Declared Age Range API before enabling social media features?
  - quote: "At a minimum, the Declared Age Range API is called to check users' age ranges before enabling social media features."
  - surface: code
  - verify: `grep -rn "DeclaredAgeRange\|AgeRangeService\|requestAgeRange" --include=*.swift`; confirm the call gates feed/social views; check the entitlement `com.apple.developer.declared-age-range` in .entitlements.
  - fix: Integrate the Declared Age Range API and gate social features on the returned range, or declare Social Media instead.
- **[SUBMIT-51]** If users can directly communicate with one another (text, voice, video chat, messaging, public posting), is Messaging and Chat declared?
  - quote: "Messaging and Chat: Users can directly communicate with one another through features within the app."
  - surface: code
  - verify: Grep for chat SDKs and features (`StreamChat`, `Sendbird`, `TwilioConversations`, `Agora`, `WebRTC`, `MessageKit`, `CallKit`, chat/message models).
  - fix: Declare Messaging and Chat in the questionnaire.
- **[SUBMIT-52]** If the app shows paid promotion (banner, video, playable, rich media, native ads), is Advertising declared?
  - quote: "Advertising: Paid promotion of products or services within the app."
  - surface: code
  - verify: Check Podfile.lock / Package.resolved / frameworks for ad SDKs (GoogleMobileAds, AppLovinSDK, IronSource, UnityAds, FBAudienceNetwork, Vungle, ChartboostSDK, InMobi, Mintegral, AdServices-only is attribution) and code calls like `GADBannerView`, `MAAdView`.
  - fix: Declare Advertising in the questionnaire, or remove the ad SDK.
- **[SUBMIT-53]** If the app includes parental controls or age assurance (incl. the declared age range API, age estimation or ID verification), are those In-App Controls selected?
  - quote: "Age Assurance: Mechanism to confirm an individual's age meets the age requirement for accessing specific content or services."
  - surface: code
  - verify: Grep for DeclaredAgeRange, age-gate screens (date of birth pickers), ID verification SDKs (Persona, Onfido, Jumio, Yoti), and parental-control settings (content filters, purchase restrictions, usage limits).
  - fix: Select Parental Controls / Age Assurance in the In-App Controls step.
- **[SUBMIT-54]** If the app offers betting or wagering with real money (or exchangeable currency), is Gambling declared (yielding 18+)?
  - quote: "Gambling: Betting or wagering using real money or in-game currency that may be exchanged for real money."
  - surface: code
  - verify: Grep for betting/wager/casino/odds/lottery/raffle features and payment flows tied to them; check category Casino/Games.
  - fix: Declare Gambling; also see SUBMIT-61 (Brazil) and guideline 5.3 reference.
- **[SUBMIT-55]** If the app offers betting/wagering without real money (e.g., virtual casino), is Simulated Gambling declared at the right frequency?
  - quote: "Simulated Gambling: Betting or wagering without using real money or in-game currency that can be exchanged for real money."
  - surface: code
  - verify: Grep for slot, poker, roulette, blackjack, "spin", "bet" in game code/assets.
  - fix: Declare Simulated Gambling (Infrequent or Frequent) in the questionnaire.
- **[SUBMIT-56]** If the app sells virtual containers with randomized items, is Loot Boxes declared?
  - quote: "Loot Boxes: Virtual containers that provide players with randomized virtual items for purchase."
  - surface: code
  - verify: Grep for gacha/loot box/chest/pack-opening logic using random selection tied to StoreKit products or in-game currency purchases.
  - fix: Declare Loot Boxes in the questionnaire.
- **[SUBMIT-57]** If the app has events where users compete for rankings, rewards, or personal goals, is Contests declared at the right frequency?
  - quote: "Contests: Events that allow users to compete with one another for rankings, rewards, or the achievement of personal goals."
  - surface: code
  - verify: Grep for leaderboards (GKLeaderboard), tournaments, trivia quizzes, challenges.
  - fix: Declare Contests (Infrequent/Frequent).
- **[SUBMIT-58]** If the app provides diagnoses or guidance on managing medical conditions, is Medical or Treatment Information declared at the right frequency?
  - quote: "Medical or Treatment Information: Content that provides diagnoses or guidance around the management of medical conditions or health and wellness."
  - surface: code
  - verify: Grep/inspect for HealthKit clinical records, medication, symptom checker, diagnosis content; App category Medical/Health & Fitness.
  - fix: Declare Medical or Treatment Information; if Frequent, also see SUBMIT-70 (Regulated Medical Devices).
- **[SUBMIT-59]** If the app provides self-care or lifestyle recommendations (calorie tracking, dieting, exercise), is Health or Wellness Topics declared?
  - quote: "Health or Wellness Topics: Content that provides self-care or lifestyle recommendations."
  - surface: code
  - verify: Grep for HealthKit (HKWorkout, HKQuantityTypeIdentifier.dietaryEnergyConsumed), calorie/diet/exercise features.
  - fix: Declare Health or Wellness Topics.
- **[SUBMIT-60]** Does the app avoid graphic sexual content/nudity and prolonged graphic or sadistic realistic violence (which yield Unrated and can't be published on the App Store)?
  - quote: "Apps with this rating may contain instances of the following content that can’t be published on the App Store."
  - surface: runtime
  - verify: Exercise the app and inspect bundled media/assets and remote content sources for explicit sexual content or prolonged gore; compare with Sexuality or Nudity and Violence answers.
  - fix: manual — remove or tone down the content for App Store distribution (developer decision).
- **[SUBMIT-61]** If the app includes fixed-odds betting and is distributed in Brazil, is a valid SPA license provided in the App Review Information Notes with supporting documents attached?
  - quote: "Apps that include fixed-odds betting (gambling) features require a valid Brazilian fixed-odds betting license from the Secretariat of Prizes and Bets (SPA) to be distributed on the App Store in Brazil."
  - surface: asc
  - verify: Pricing and Availability includes Brazil; version > App Review Information > Notes contains license details and an attachment is present.
  - fix: Enter the license details in Notes and attach documents, or remove Brazil from availability (manual — legal/business).
- **[SUBMIT-62]** If the app has Frequent or Intense simulated gambling and is available in Korea, has an RCN been provided?
  - quote: "Apps and games with Frequent or Intense simulated gambling content are only available on the App Store in Korea if you provide a Rating Classification Number (RCN)."
  - surface: asc
  - verify: Age rating answer for Simulated Gambling = Frequent; availability includes Republic of Korea; App Information > Age Ratings > Republic of Korea shows an RCN.
  - fix: Obtain an RCN from GRAC and add it (manual), or remove Korea availability.
- **[SUBMIT-63]** If App Review sent a regulator message (Australia or Korea GRAC), were the instructions followed and the app re-submitted?
  - quote: "If you receive this message, follow the instructions and re-submit your app for review."
  - surface: asc
  - verify: App Review page > messages for regulator notices.
  - fix: manual — follow the instructions in the message and resubmit.

## SUBMIT.APPINFO App information (compliance properties)

**Source text (verbatim):**
> App information refers to the properties that are shared across the platforms added to an app. Some of these properties are set when you add the app to your account, and later, you can edit app information as needed based on the app's status.
>
> | Property | Description |
> |---|---|
> | Bundle ID | A unique identifier for your app that is used throughout the system. (A build is uniquely identified by the combination of the bundle ID, version number, and build string.) You can’t change this property after you upload a build. Important: The Bundle ID property must match the bundle ID you set in the Xcode project. |
> | Content Rights | Apps that contain, show, or access third-party content must have all the necessary rights to that content or be otherwise permitted to use it under the laws of each App Store country or region in which they’re available. Learn more about the App Store guidelines. |
> | Age Rating | The age rating of your app for the purpose of parental controls. Note that the rating is set at the app level in the App information section and is applied across all platforms. Learn more about the age rating values. This property is required. |
> | Made for Kids | An indication that the app appears in the Kids category on the App Store. This property includes an age range set for the app. Once an app marked as Made for Kids is approved by App Review, this selection cannot be changed and all subsequent updates will need to follow the Kids category guidelines. |
> | License Agreement | Apple provides a standard EULA (End-User License Agreement) that applies in all regions. You may provide a custom license agreement that supersedes the Apple EULA for one or more regions. |
> | Category (Primary and Secondary) | The categories that best describe your app. For macOS apps, you also set the app category in Xcode. The primary category you set in App Store Connect should match the category you set in Xcode. For more information, visit Choosing a Category. |
> | Availability in the Republic of Korea - Rating Classification Number | If your app meets one or more of the following characteristics, a Rating Classification Number from the Game Rating and Administration Committee (GRAC) is required in order to offer it on the App Store in the Republic of Korea. |
> |  | App has been given the KR-19 regional rating by GRAC. |
> |  | Apps in the Casino subcategory with age rating 17+ |
> |  | Apps in the Games or Entertainment categories with a Frequent/Intense level of frequency in at least one of the following content descriptions: |
> |  | Simulated Gambling |
> |  | Sexual Content or Nudity |
> |  | Alcohol, Tobacco, or Drug Use or Reference |
> |  | Realistic Violence |
> |  | Please note that this field will display if your app is in the Games or Entertainment category with a rating of 17+, but is only required if your app meets the above criteria. |
> | Availability in China mainland | Chinese law requires additional documentation for some apps to be available on the App Store in China mainland. China’s Ministry of Industry and Information Technology (MIIT) requires that some apps possess a valid Internet Content Provider (ICP) Filing Number. The ICP number and metadata on the App Information page should match with the information you have filed with MIIT. This match is required for your Simplified Chinese localization; if not configured, then it should match your primary language. Once the provided ICP Filing Number is verified and saved, it will be displayed on your App Store product page. In addition, games must secure an approval number and apps with books and magazine content must secure an internet publishing permit from China’s National Press and Publication Administration (NPPA). Apps with religious content must secure an Internet Religious Information Permit from China’s National Religious Affairs Administration (NRAA). Apps with news content must obtain an Internet News Information Permit from the Cyberspace Administration of China (CAC). If you offer or plan to offer any of these on the App Store in China mainland, you must provide the required information along with one or more supporting documents.If applicable, provide the required ICP filing information in the designated section under the “App Information” tab. To help verify your approval number, upload your game’s ISBN Issuing Letter or Approval Reply, and a copy of your latest Business License. Additionally, you can include an authorization agreement from the matching operator. To help verify your publishing permit, upload your internet publishing permit or other relevant permit from the NPPA, a publishing permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation. To help verify your Internet Religious Information Permit, upload your Internet Religious Information Permit, a permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation. To help verify your Internet News Information Permit, upload your Internet News Information Permit, a permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation. |
> | Availability in Vietnam | Vietnamese regulators require games distributed in Vietnam to be licensed to remain available on the App Store in Vietnam. To learn more about the game license, review the regulations on licensing game publishing in Vietnam. |
> | Digital Services Act (DSA) | You’ll be asked to disclose whether or not you’re a trader under the European Union’s Digital Services Act (DSA) in order to distribute apps in the EU. If you’re a trader, the DSA requires that you provide certain identification information, including your address and contact details, to be displayed on your App Store product pages to consumers in the EU. You also have the option to provide a labels and markings URL. Learn more. |
> | Regulated Medical Devices | Apps that are available in the EU/EEA, UK, or U.S., and have a primary or secondary category of Health & Fitness or Medical, or that have "frequent" Medical or Treatment information listed in the age rating, are required to complete this declaration. |


**Applies to:** All apps (regional rows: apps available in the named region/category)

- **[SUBMIT-65]** Does the ASC Bundle ID match the bundle ID set in the Xcode project?
  - quote: "The Bundle ID property must match the bundle ID you set in the Xcode project."
  - surface: code
  - verify: PRODUCT_BUNDLE_IDENTIFIER of the app target vs App Information > Bundle ID.
  - fix: Change PRODUCT_BUNDLE_IDENTIFIER in Xcode to match (the ASC value can't change after a build is uploaded).
- **[SUBMIT-66]** If the app contains, shows, or accesses third-party content, does the developer have the necessary rights (and has the Content Rights declaration been answered accordingly)?
  - quote: "Apps that contain, show, or access third-party content must have all the necessary rights to that content or be otherwise permitted to use it under the laws of each App Store country or region in which they’re available."
  - surface: manual
  - verify: ASC > App Information > Content Rights: declaration answered. In code, look for third-party content sources (streaming/media URLs, scraped feeds, bundled music/images/fonts, external APIs such as YouTube/Spotify/news APIs) and ask the developer for licenses.
  - fix: manual — obtain rights/licences; attach evidence in App Review Information (see SUBMIT-109); set the Content Rights answer.
- **[SUBMIT-67]** For macOS apps, does the primary category set in App Store Connect match the category set in Xcode?
  - quote: "The primary category you set in App Store Connect should match the category you set in Xcode."
  - surface: code
  - verify: Read LSApplicationCategoryType from the macOS target's Info.plist (or INFOPLIST_KEY_LSApplicationCategoryType); compare with App Information > Primary Category.
  - fix: Update LSApplicationCategoryType or the ASC category so they match.
- **[SUBMIT-68]** If the app meets the Korea criteria (KR-19, Casino 17+, or Games/Entertainment with Frequent/Intense listed content), is a GRAC Rating Classification Number provided?
  - quote: "a Rating Classification Number from the Game Rating and Administration Committee (GRAC) is required in order to offer it on the App Store in the Republic of Korea"
  - surface: asc
  - verify: Category (Games/Entertainment, Casino subcategory), age rating answers, Korea availability; App Information > Republic of Korea RCN field.
  - fix: manual — obtain RCN from GRAC, or remove Korea availability.
- **[SUBMIT-69]** If distributed in China mainland, are the required ICP Filing Number and (for games/books/magazines/religious/news content) the required approval number or permits provided?
  - quote: "If you offer or plan to offer any of these on the App Store in China mainland, you must provide the required information along with one or more supporting documents."
  - surface: asc
  - verify: Pricing and Availability includes China mainland; App Information > Availability in China mainland section shows ICP Filing Number and, as applicable, approval number/permit documents; ICP metadata matches the Simplified Chinese localization (or primary language).
  - fix: manual — obtain ICP filing/permits, or remove China mainland availability.
- **[SUBMIT-70]** If the app is available in the EU/EEA, UK, or U.S. and is in Health & Fitness or Medical (or has "frequent" Medical or Treatment information), is the Regulated Medical Devices declaration completed?
  - quote: "are required to complete this declaration"
  - surface: asc
  - verify: App Information > category and age rating Medical answer; App Information > Regulated Medical Device status completed.
  - fix: Complete the Regulated Medical Device declaration in App Information (manual answer by developer).
- **[SUBMIT-71]** If the app is a game distributed in Vietnam, is it licensed?
  - quote: "Vietnamese regulators require games distributed in Vietnam to be licensed to remain available on the App Store in Vietnam."
  - surface: manual
  - verify: Category Games + Vietnam availability; ask the developer for the license; check App Information > Availability in Vietnam.
  - fix: manual — obtain the game license, or remove Vietnam availability.

## SUBMIT.DSA Manage European Union Digital Services Act trader requirements

**Source text (verbatim):**
> Articles 30 and 31 of the Digital Services Act (DSA) require Apple to verify and display trader contact information for all traders distributing apps on the App Store in the European Union (EU). This includes an address, phone number, and email address that you provide to Apple for the purpose of posting on your App Store product page in accordance with the DSA. Once verified, Apple will publish this information on your App Store product page when your app is distributed in any of the 27 territories of the EU. Even if you don’t distribute apps in the EU, you’ll still need to declare a trader status.
> If you haven't already confirmed your trader status, next time you submit a new app in App Store Connect you’ll be asked to disclose whether or not you’re a trader in connection with the DSA in order to stay compliant across territories when distributing on the App Store. You'll need to confirm your trader status if you have at least one app on the App Store in the EU that qualifies you as a trader. You’ll then have the option to turn off or specify your trader status for each specific app that you distribute. If you’re not a trader, consumers in the EU will be informed that consumer rights stemming from applicable consumer protection laws won’t apply to contracts between you and them.
> Trader self-assessment
> You must assess whether you're a trader for EU law purposes. If you don't distribute apps on the App Store in the EU (for example you only distribute apps through alternative distribution, or TestFlight, or on the App Store only outside the EU), you're not acting as a trader on the App Store. Apple can't determine whether you're a trader.
> How to know if you’re a trader
> The DSA defines a trader as “any natural person, or any legal person irrespective of whether privately or publicly owned, who is acting, including through any person acting in his or her name or on his or her behalf, for purposes relating to his or her trade, business, craft or profession.”
> The European Commission (EC) has issued a Notice on what constitutes a trader (See Section 2.2. “Concept of Trader"), though it is not specific to digital commerce. The EC has also published Guidance in the digital commerce context, from the perspective of when an ”influencer“ may be considered a trader.
> To determine if you're a trader, you should consider a range of non-exhaustive and non-exclusive factors (see those listed on page 2 in the EC’s Guidance), which may include:
> - Whether you make revenue as a result of your app, for example if your app includes In-App Purchases, or if it's a paid or ad-sponsored app — especially if you're transacting in large volumes;
> - Whether you engage in commercial practices towards consumers, including advertising, or promoting products or services;
> - Whether you're registered for VAT purposes; and
> - Whether you develop your app in connection with your trade, business, craft, or profession—meaning that you’re acting in a professional/business capacity. You're unlikely to be a trader for EU law purposes if you're acting “for purposes which are outside your trade, business, craft, or profession.” For example, if you're a hobbyist and you developed your app with no intention of commercializing it, you may not be considered a trader.
>
> Regardless of whether you’re an individual developer or organization, if you have a legal status associated with a business activity, that would suggest you may be a trader.
> The material contained herein is informational, general in nature, and does not constitute legal advice. If you're uncertain about your status as a trader, consult with your legal advisor.
> Information you need to provide if you're a trader
> The information you need to provide depends on whether you’re enrolled in the Apple Developer Program as an individual or organization.
> Organizations: The address associated with your D-U-N-S Number will automatically display. You’ll need to enter the following for display on your App Store product pages:
> - Phone number
> - Email address
>
> This information is for display purposes only and won’t impact the information associated with your Apple Developer Program membership. If you need to update your physical address, contact us.
> Individuals: You’ll need to enter the following for display on your App Store product pages:
> - Address or P.O. Box
> - Phone number
> - Email address
>
> This information is for display purposes only and won’t impact the information associated with your Apple Developer Program membership.
> All traders: You’ll need to provide payment account details, if you haven’t already entered them in App Store Connect. You'll also be asked to certify that you only offer products or services that comply with the applicable rules of EU law.
> Enter EU Digital Services Act compliance information
> Required role: Account Holder or Admin. View role permissions.
> Select Business at the top of the page.
> On the Agreements tab, scroll down to the Compliance section.
> Next to Digital Services Act, click Complete Compliance Requirements.
> Select from the following options:
> “This is a trader account.” You’ll need to enter contact information for display on your App Store product pages. Continue to step 5.
> Note: You’ll still have the option to turn off your trader status for specific apps later.
> “This is not a trader account.” You won’t need to provide any contact information. Click Done.
> Enter or confirm the required contact information and click Next.
> Validate the email address you provided using two-factor authentication. Once you’re done, you’ll automatically be directed to the next step.
> Validate the phone number you provided on the previous screen using two-factor authentication. Once you’re done, you’ll automatically be directed to the next step. If you're using a phone number that can't receive two-factor authentication codes, you can request manual verification.
> Follow the instructions to upload your documentation. You’ll need to provide a current document that verifies your business name and address. Acceptable documents include business or legal records. If you’re displaying an alternate address, such as a P.O. Box, you’ll also need to provide documentation that reflects your association with this alternate address (for example, a receipt or bill). When you’re done, click Next.
> Review your information to make sure it’s correct, then click Confirm.
> Enter app-specific EU Digital Services Act compliance information
> Required role: Account Holder and Admin. View role permissions.
> If you need to change your trader status for one or more of your individual apps, you can do so.
> In Apps, select your app from the list.
> In the left sidebar, click App Information.
> Scroll to the App Store Regulations and Permits section.
> Under Digital Services Act, click Edit.
> In the pop-up window, change your trader status for that app. If you’re declaring yourself a trader for the first time, you’ll need to enter and verify your contact information that displays on your app’s App Store product page.
> Enter labels and markings URLs
> Required role: Account Holder and Admin. View role permissions.
> Under the Digital Services Act, you have the option to provide a Labels and Markings URL to display labels or markings required by European Union law. This URL will be visible on your App Store product pages for apps where you have identified as a trader.
> In Apps, select your app from the list.
> In the left sidebar, click App Information.
> Scroll to the App Store Regulations and Permits section.
> Click Add Labels and Markings.
> In the pop-up window, enter the URL and click Done. You can edit this URL at any time.

**Applies to:** All developers (trader status declaration); contact/verification items apply to traders

- **[SUBMIT-72]** Has a trader status been declared for the account (required even when not distributing in the EU)?
  - quote: "Even if you don’t distribute apps in the EU, you’ll still need to declare a trader status."
  - surface: asc
  - verify: Business > Agreements tab > Compliance section > Digital Services Act: status shows completed (trader or not a trader).
  - fix: Account Holder/Admin clicks Complete Compliance Requirements and selects an option.
- **[SUBMIT-73]** Has the developer performed the trader self-assessment (revenue, commercial practices, VAT registration, professional capacity)?
  - quote: "You must assess whether you're a trader for EU law purposes."
  - surface: manual
  - verify: Ask the developer; gather facts from code/ASC that inform it (IAPs/subscriptions in ASC, paid price, ad SDKs in code — see SUBMIT-52).
  - fix: manual — requires developer decision/legal advice.
- **[SUBMIT-74]** If a trader, have the required contact details been entered (organizations: phone + email; individuals: address or P.O. Box, phone, email) and validated by two-factor authentication?
  - quote: "Validate the email address you provided using two-factor authentication."
  - surface: asc
  - verify: Business > Agreements > Compliance > Digital Services Act: contact info present and verified.
  - fix: Enter/confirm contact information and complete email and phone verification (or request manual verification for phone).
- **[SUBMIT-75]** If a trader, has a current document verifying business name and address (and alternate address, if shown) been uploaded?
  - quote: "You’ll need to provide a current document that verifies your business name and address."
  - surface: manual
  - verify: Business > Compliance > Digital Services Act shows the documentation step completed / verified.
  - fix: manual — upload business or legal records (plus receipt/bill for a P.O. Box).
- **[SUBMIT-76]** If a trader, are payment account details entered in App Store Connect?
  - quote: "You’ll need to provide payment account details, if you haven’t already entered them in App Store Connect."
  - surface: asc
  - verify: Business > banking/payment information is present.
  - fix: Enter banking/payment information in Business.
- **[SUBMIT-77]** If a trader, has the developer certified they only offer products or services that comply with EU law?
  - quote: "You'll also be asked to certify that you only offer products or services that comply with the applicable rules of EU law."
  - surface: manual
  - verify: Ask the developer; DSA flow completed through Confirm.
  - fix: manual — legal/business attestation.
- **[SUBMIT-78]** Is the app-specific trader status correct for this app?
  - quote: "You’ll then have the option to turn off or specify your trader status for each specific app that you distribute."
  - surface: asc
  - verify: App Information > App Store Regulations and Permits > Digital Services Act: the status for this app matches the developer's self-assessment for it.
  - fix: Edit the app's trader status; verify contact info if declaring trader for the first time.
- **[SUBMIT-79]** (Optional per Apple) If EU law requires labels or markings for the app's products, is a Labels and Markings URL provided?
  - quote: "you have the option to provide a Labels and Markings URL to display labels or markings required by European Union law"
  - surface: manual
  - verify: App Information > App Store Regulations and Permits: Labels and Markings URL present when the developer indicates labels/markings are required.
  - fix: Click Add Labels and Markings, enter the URL, Done.

## SUBMIT.EXPORT.OVERVIEW Overview of export compliance

**Source text (verbatim):**
> If your app uses, accesses, contains, implements, or incorporates encryption, and you intend to upload, test, and distribute it, you need to determine your export compliance requirements in App Store Connect.
> Examples of apps requiring an export compliance determination include, but aren’t limited to, apps that use:
> - Standard encryption algorithms.
> - Crypto functionality within Apple’s operating system.
> - Proprietary or non-standard encryption algorithms. The US Government defines "non-standard cryptography" as any implementation of “cryptography” involving the incorporation or use of proprietary or unpublished cryptographic functionality, including encryption algorithms or protocols that have not been adopted or approved by a duly recognized international standards body (e.g., IEEE, IETF, ISO, ITU, ETSI, 3GPP, TIA, and GSMA) and haven’t otherwise been published.
>
> Please note that it’s your responsibility to review the Export Administration Regulation to determine whether your app's use of encryption requires a formal classification (Commodity Classification Automated Tracking System or CCATS) from BIS. you're responsible for all liabilities associated with misinterpretation of export regulations or claiming exemption inaccurately. To learn about encryption export controls, search for "encryption policy" on the US Department of Commerce Bureau of Industry and Security (BIS) website. The import and export of encryption apps distributed in France are also controlled by the French Government. The main items of control for France are Secure Storage, Secure Communications, and Security Anti-Virus applications. Exemptions include Banking and Medical applications. For more information about these French controls, visit the Agence nationale de la sécurité des systèmes d’information (ANSSI) website.
> When you submit a new version of your app, you’ll need to answer questions in App Store Connect about your app's use of encryption. Follow the steps below before submitting your app to App Review to ensure that you’re submitting the right documentation and to bypass these questions if your app doesn’t use encryption.
> Determine your export compliance requirements
> App Store Connect provides a simple way for you to determine your export compliance requirements by presenting you with a set of questions about your app and where you plan to make it available. Based on your answers, complete the following steps:
>
> | Scenario | Next Steps |
> |---|---|
> | No export compliance documentation required | Update your app’s information property list (Info.plist) file in Xcode so that you don’t need to answer encryption questions with each app submission. |
> | Export compliance documentation required | Use App Store Connect to submit your app encryption documentation. |
> |  | Once the documentation is approved, attach it to your beta build or app version build. |
> |  | Update your app’s information property list (Info.plist) file in Xcode so that you don’t need to answer encryption questions with each app submission. |

**Applies to:** Apps that use, access, contain, implement, or incorporate encryption

- **[SUBMIT-80]** Has the app's use of encryption (OS crypto, standard algorithms, proprietary/non-standard algorithms, including in third-party libraries) been inventoried to determine export compliance requirements?
  - quote: "you need to determine your export compliance requirements in App Store Connect"
  - surface: code
  - verify: Grep the app and dependencies: `grep -rn "import CryptoKit\|CommonCrypto\|CCCrypt\|SecKeyCreate\|SecKeyEncrypt\|kSecAttrKeyType\|import Security\|OpenSSL\|BoringSSL\|libsodium\|Sodium\|CryptoSwift\|RNCryptor\|SQLCipher\|Signal\|WireGuard\|NetworkExtension\|URLSession\|https://"`; check Podfile.lock / Package.resolved for crypto libraries. Classify each hit as OS-provided, industry-standard non-OS, or proprietary.
  - fix: Record the classification and answer the ASC encryption questions accordingly (App Information > App Encryption Documentation > +).
- **[SUBMIT-81]** Has the developer determined whether a CCATS formal classification from BIS is required?
  - quote: "it’s your responsibility to review the Export Administration Regulation to determine whether your app's use of encryption requires a formal classification (Commodity Classification Automated Tracking System or CCATS) from BIS"
  - surface: manual
  - verify: Ask the developer; required when SUBMIT-80 finds proprietary/non-standard cryptography (see SUBMIT.EXPORT.DOCS table).
  - fix: manual — legal/business action (BIS classification).
- **[SUBMIT-82]** If the app is distributed in France and involves Secure Storage, Secure Communications, or Security Anti-Virus functionality, has the French control been considered?
  - quote: "The main items of control for France are Secure Storage, Secure Communications, and Security Anti-Virus applications."
  - surface: manual
  - verify: Pricing and Availability includes France; app category/features match a control item (Banking and Medical are listed exemptions).
  - fix: manual — consult ANSSI requirements; upload French encryption declaration if required (SUBMIT.EXPORT.DOCS).

## SUBMIT.EXPORT.DOCS Export compliance documentation for encryption

**Source text (verbatim):**
> Depending on the kind of encryption algorithm your app uses, you may need to provide documentation in App Store Connect.
>
> | Encryption algorithm in use | Required documentation |
> |---|---|
> | Your app uses encryption limited to that within the Apple operating system | No documentation required in App Store Connect. |
> | Your app uses an industry standard algorithm, not provided within the Apple operating system | Upload your French encryption declaration in App Store Connect.1 |
> | Your app uses proprietary encryption algorithms not accepted by international standard bodies (such as IEEE, IETF, or ITU) | Upload your: |
> |  | US Commodity Classification Automated Tracking System (CCATS) |
> |  | French encryption declaration in App Store Connect1 |
>
> 1 French encryption declaration form is only required if you’re distributing your app on the App Store in France.

**Applies to:** Apps using encryption beyond that within the Apple operating system

- **[SUBMIT-83]** If the app uses an industry-standard algorithm not provided by the Apple OS and is distributed in France, has a French encryption declaration been uploaded?
  - quote: "Your app uses an industry standard algorithm, not provided within the Apple operating system"
  - surface: asc
  - verify: From SUBMIT-80 findings (e.g., OpenSSL, libsodium, CryptoSwift, SQLCipher bundled); Pricing and Availability includes France; App Information > App Encryption Documentation lists an approved French declaration.
  - fix: manual — prepare the French declaration and upload via App Encryption Documentation (+ > Choose File).
- **[SUBMIT-84]** If the app uses proprietary encryption algorithms not accepted by international standard bodies, has a CCATS (and French declaration if distributed in France) been uploaded?
  - quote: "Your app uses proprietary encryption algorithms not accepted by international standard bodies (such as IEEE, IETF, or ITU)"
  - surface: asc
  - verify: From SUBMIT-80 findings (custom cipher implementations); App Encryption Documentation lists approved CCATS.
  - fix: manual — obtain CCATS from BIS and upload.

## SUBMIT.EXPORT.UPLOAD Determine and upload app encryption documentation

**Source text (verbatim):**
> Required role: Account Holder, Admin, or App Manager. View role permissions.
> Determine your export compliance requirements
> App Store Connect provides a set of questions to help you determine whether app encryption documentation is required from you, and which forms are specifically needed.
> In Apps, select the app you want to view.
> In the sidebar, click App Information.
> Next to App Encryption Documentation, click the add button (+) and answer the questions that appear in the dialogs.
> Alternatively, you can click Manage next to the build that’s missing app encryption information on either the Distribution tab or TestFlight tab to answer the required questions.
> Upload your documentation
> If you’re required to upload app encryption documentation, you can do so in the App Encryption Documentation section in the App Store Connect. This should be completed before submitting a build for review on either App Review or TestFlight App Review. To ensure a smooth review process, populate the App Description field and manage availability for your app on the App Store before providing this documentation. Without this information, Apple can’t determine whether the app encryption documents are sufficient.
> In Apps, select the app you want to view.
> In the sidebar, click App Information.
> Next to App Encryption Documentation, click the add button (+) and answer the questions that appear in the dialogs.
> When prompted, click Choose File to upload your document.
> Click Save.
> Apple evaluates export compliance reviews on a case-by-case basis. If you provide complete information, Apple expects to review and clear apps in approximately two business days. Once your documentation is approved, Apple will provide you a key value. You must enter this value in Xcode to avoid answering encryption questions with each app submission. You can find this key value next to your approved documentation in the App Encryption Documentation section of App Store Connect.
> If your app doesn’t require documentation, update your app’s information property list (Info.plist) file in Xcode to let us know that your app doesn't use encryption or is exempt from providing documentation.
> If you have specific questions about Apple's export process, contact us.

**Applies to:** Apps required to upload app encryption documentation (last paragraph: apps not requiring documentation)

- **[SUBMIT-85]** If documentation is required, was it uploaded before submitting the build for App Review or TestFlight App Review (Apple: "should be completed before")?
  - quote: "This should be completed before submitting a build for review on either App Review or TestFlight App Review."
  - surface: asc
  - verify: App Information > App Encryption Documentation lists the document with an approved status before the version is submitted.
  - fix: Upload via + > answer questions > Choose File > Save; allow approximately two business days.
- **[SUBMIT-86]** (Recommended "to ensure a smooth review process") Before providing encryption documentation, are the App Description populated and App Store availability set, so Apple can determine whether the documents are sufficient?
  - quote: "populate the App Description field and manage availability for your app on the App Store before providing this documentation"
  - surface: asc
  - verify: Version page Description is non-empty; Pricing and Availability has storefronts selected.
  - fix: Fill Description and set availability first, then upload documentation.
- **[SUBMIT-87]** If documentation was approved, has the key value Apple provided been entered in Xcode (ITSEncryptionExportComplianceCode)?
  - quote: "You must enter this value in Xcode to avoid answering encryption questions with each app submission."
  - surface: code
  - verify: Info.plist / INFOPLIST_KEY_ITSEncryptionExportComplianceCode contains the value shown next to the approved document in ASC.
  - fix: Add `ITSEncryptionExportComplianceCode` (String) with the approved key value to Info.plist.

## SUBMIT.EXPORT.KEY Complying with Encryption Export Regulations (ITSAppUsesNonExemptEncryption / ITSEncryptionExportComplianceCode)

**Source text (verbatim):**
> Declare the use of encryption in your app to streamline the app submission process.
> When you submit your app to TestFlight or the App Store, you upload your app to a server in the United States. If you distribute your app outside the U.S. or Canada, your app is subject to U.S. export laws, regardless of where your legal entity is based. If your app uses, accesses, contains, implements, or incorporates encryption, this is considered an export of encryption software, which means your app is subject to U.S. export compliance requirements, as well as the import compliance requirements of the countries where you distribute your app.
> Every time you submit a new version of your app, App Store Connect asks you questions to guide you through a compliance review. You can bypass these questions and streamline the submission process by providing the required information in your app’s Information Property List file.
> Declare Your App’s Use of Encryption
> Add the ITSAppUsesNonExemptEncryption key to your app’s information property list with a Boolean value that indicates whether your app uses encryption. Set the value to NO if your app—including any third-party libraries it links against—doesn’t use encryption, or if it only uses forms of encryption that are exempt from export compliance documentation requirements. Otherwise, set it to YES.
> Typically, the use of encryption that’s built into the operating system—for example, when your app makes HTTPS connections using URLSession—is exempt from export documentation upload requirements, whereas the use of proprietary encryption is not. To determine whether your use of encryption is considered exempt, see Determine and upload app encryption documentation.
> If your app uses exempt forms of encryption, you might alternatively be required to submit a year-end self-classification report to the U.S. government. (If you use non-exempt encryption and provide documentation to Apple, the self-classification report isn’t necessary.) To learn more, see How to file an Annual Self Classification Report.
> Provide Compliance Documentation
> If your app requires export compliance documentation, upload the required items to App Store Connect, as described in Determine and upload app encryption documentation. After successfully reviewing the documents, Apple provides you with a code. Add this string as the value for the ITSEncryptionExportComplianceCode key in your app’s information property list.
>
> ITSAppUsesNonExemptEncryption
> A Boolean value indicating whether the app uses encryption.
> Set the value for this key to NO in your app’s Information Property List file to indicate that your app—including any third-party libraries you link against—either uses no encryption, or only uses encryption that’s exempt from export compliance requirements, as described in Overview of export compliance. Set the value to YES to indicate that your app uses non-exempt encryption.
> If you set the value to YES, you typically also provide a value for the ITSEncryptionExportComplianceCode key. You set that key’s value using a code Apple provides after successfully reviewing your export compliance documentation.
> If you don’t have the ITSAppUsesNonExemptEncryption key in your app’s Info.plist file, App Store Connect walks you through an export compliance questionnaire every time you upload a new version of your app. Including the key streamlines the app submission process.
>
> ITSEncryptionExportComplianceCode
> The export compliance code provided by App Store Connect for apps that require it.
> Include this key in your app’s Information Property List file if you set the ITSAppUsesNonExemptEncryption key’s value to YES. Set the value for this key to the code that Apple sends you after successfully reviewing export compliance documentation that you provide through App Store Connect.

**Applies to:** All apps (the key is optional but avoids the per-upload questionnaire); compliance code: apps that set ITSAppUsesNonExemptEncryption to YES

- **[SUBMIT-88]** (Recommended — without the key, App Store Connect walks you through the export compliance questionnaire for every new version) Does the app's Info.plist contain ITSAppUsesNonExemptEncryption with a Boolean value?
  - quote: "Add the ITSAppUsesNonExemptEncryption key to your app’s information property list with a Boolean value that indicates whether your app uses encryption."
  - surface: code
  - verify: `plutil -p <Info.plist> | grep ITSAppUsesNonExemptEncryption` for each app target's Info.plist, or `grep -rn "INFOPLIST_KEY_ITSAppUsesNonExemptEncryption" *.xcodeproj/project.pbxproj`; the value must be a Boolean (`<true/>`/`<false/>` or YES/NO), not a string. Missing key = WARN (questionnaire must then be answered in ASC per build, see SUBMIT-12/SUBMIT-92).
  - fix: Add `<key>ITSAppUsesNonExemptEncryption</key><false/>` (or `<true/>`) to Info.plist, or set the build setting INFOPLIST_KEY_ITSAppUsesNonExemptEncryption — the value must reflect SUBMIT-89.
- **[SUBMIT-89]** Is ITSAppUsesNonExemptEncryption set to NO only if the app, including linked third-party libraries, uses no encryption or only exempt encryption?
  - quote: "Set the value to NO if your app—including any third-party libraries it links against—doesn’t use encryption, or if it only uses forms of encryption that are exempt from export compliance documentation requirements. Otherwise, set it to YES."
  - surface: code
  - verify: Compare the key's value with the SUBMIT-80 inventory. Only OS-provided crypto used (e.g., HTTPS via URLSession) is typically exempt; proprietary encryption is not. Flag NO + proprietary crypto as FAIL; flag ambiguous non-OS standard crypto as manual.
  - fix: Set the value to YES and provide documentation (SUBMIT.EXPORT.UPLOAD), or remove the non-exempt crypto; final determination is the developer's legal responsibility.
- **[SUBMIT-90]** If ITSAppUsesNonExemptEncryption is YES, is ITSEncryptionExportComplianceCode present with the code Apple provided?
  - quote: "Include this key in your app’s Information Property List file if you set the ITSAppUsesNonExemptEncryption key’s value to YES."
  - surface: code
  - verify: `plutil -p <Info.plist> | grep ITSEncryptionExportComplianceCode` (String value); compare with the key value next to approved documentation in ASC > App Information > App Encryption Documentation.
  - fix: Add `<key>ITSEncryptionExportComplianceCode</key><string>APPLE-PROVIDED-CODE</string>`.
- **[SUBMIT-91]** If the app uses exempt forms of encryption, has the developer checked whether a year-end self-classification report to the U.S. government is required?
  - quote: "If your app uses exempt forms of encryption, you might alternatively be required to submit a year-end self-classification report to the U.S. government."
  - surface: manual
  - verify: Ask the developer.
  - fix: manual — legal/business action (BIS Annual Self Classification Report).

## SUBMIT.EXPORT.BETA Provide export compliance information for beta builds

**Source text (verbatim):**
> Specify encryption use for your build to avoid the beta being marked as Missing Compliance. Answer the export compliance questions or attach previously approved documentation in the TestFlight section.
> Required role: Account Holder, Admin, and App Manager. View role permissions.
> In Apps, select the app you want to view.
> Click the TestFlight tab.
> In the sidebar, under Builds, click the platform.
> In the Build column in the table on the right, click the app icon or build string for the build that’s missing compliance information.
> To address compliance issues for a build, you can either click Manage beside the relevant build to answer the required questions, or click Choose File to upload previously approved documentation.
> Click Provide Export Compliance Information, and answer the required questions.
> If app encryption documentation is required, click Go to App Encryption Page to upload your file. Apple will provide you with a key value to enter in Xcode This will remove the need to answer encryption questions with each app submission. Learn more about uploading app encryption documentation.
> If documentation isn’t required, click Save. You can indicate that your app doesn’t use encryption or is exempt from documentation by specifying encryption settings in the app's Info.plist file in Xcode. This eliminates the need to answer encryption questions with each app submission.

**Applies to:** Builds distributed via TestFlight

- **[SUBMIT-92]** Is every TestFlight build intended for testing/submission free of the Missing Compliance status?
  - quote: "Specify encryption use for your build to avoid the beta being marked as Missing Compliance."
  - surface: asc
  - verify: TestFlight tab > Builds > (platform): status column for recent builds.
  - fix: Click Manage beside the build and answer the questions (or Choose File), and add ITSAppUsesNonExemptEncryption to Info.plist for future builds.

## SUBMIT.REVIEWINFO App Review information (Platform version information)

**Source text (verbatim):**
> You must provide the following information to App Review. It isn’t visible to customers and can be edited at any time.
> Submissions that include an app version will be reviewed together with the App Review information for that version.
> Submissions that don’t include an app version, or those that include items associated with multiple platforms, will be reviewed together with the App Review information for the latest approved version of the platform you specify during the submission process. To edit the App Review information on an approved app version, click Edit in the top right corner of the App Review Information section.
>
> | Property | Description | Required |
> |---|---|---|
> | Contact: Name, email, phone number | Information for the contact person in your organization if the App Review team needs additional information. Enter the phone number in international format, including a plus sign (+) followed by the country code (for example, +852 for Hong Kong) — the field doesn't accept numbers-only entry. |  |
> | Notes | Additional information about your app that can help during the review process. Include information that may be needed to test your app, such as app-specific settings and test registration or account details. If your app delivers streaming video over the cellular network, enter a test stream URL. The Notes field can contain up to 4000 bytes. You can write notes in any language. |  |
> | Sign-in required: Username and password | Sign-in information for a demo account. If your app uses a single sign-on service, such as Facebook or Twitter, include the demo account login information for it. The demo account is used during the App Review process and must not expire. Details for additional accounts should be included in the Notes field. | If your app requires a login to use it. |

Note: On Apple's page the Required column shows an image (not text) for the Contact and Notes rows.

**Applies to:** All app version submissions (Sign-in row: apps that require a login)

- **[SUBMIT-93]** Are the App Review contact name, email, and phone number filled, with the phone in international format (+ and country code)?
  - quote: "Enter the phone number in international format, including a plus sign (+) followed by the country code"
  - surface: asc
  - verify: Version page > App Review Information > Contact Information: all three fields filled; phone starts with "+".
  - fix: Enter the contact person's details; prefix the phone with + and country code.
- **[SUBMIT-94]** If the app requires a login, is a demo account (username and password) provided that will not expire?
  - quote: "The demo account is used during the App Review process and must not expire."
  - surface: code
  - verify: Detect login gating in code (auth screens before main content; `ASAuthorizationAppleIDProvider`, FirebaseAuth, Auth0, Supabase auth, custom login views). If present, ASC > App Review Information > Sign-in required is checked with username/password filled.
  - fix: Create a non-expiring demo account and enter it; or provide a demonstration mode (SUBMIT-110).
- **[SUBMIT-95]** If the app uses a single sign-on service, is the demo login information for that service included?
  - quote: "If your app uses a single sign-on service, such as Facebook or Twitter, include the demo account login information for it."
  - surface: code
  - verify: Grep for FBSDKLoginKit, GoogleSignIn, TwitterKit/X SDK, Okta/MSAL; if SSO is the only login path, ASC Sign-in or Notes contains credentials for it.
  - fix: Provide SSO demo credentials in the Sign-in fields or Notes.
- **[SUBMIT-96]** If there are additional account types, are their details in the Notes field?
  - quote: "Details for additional accounts should be included in the Notes field."
  - surface: asc
  - verify: Detect roles in code (admin/teacher/business/provider user types); ASC Notes lists credentials for each.
  - fix: Add each account type's credentials to Notes.
- **[SUBMIT-97]** If the app delivers streaming video over the cellular network, is a test stream URL in Notes?
  - quote: "If your app delivers streaming video over the cellular network, enter a test stream URL."
  - surface: code
  - verify: Grep for AVPlayer/AVPlayerItem with remote .m3u8/.mpd URLs, `allowsCellularAccess`; ASC Notes contains a stream URL.
  - fix: Add a working test stream URL to Notes.
- **[SUBMIT-98]** Are the App Review Notes within 4000 bytes?
  - quote: "The Notes field can contain up to 4000 bytes."
  - surface: asc
  - verify: Copy Notes text and measure UTF-8 byte length (`printf %s "$NOTES" | wc -c`).
  - fix: Shorten Notes; move long material into an attachment.

## SUBMIT.COMPLETE Provide information for a complete review (App Review Help)

**Source text (verbatim):**
> Add everything App Review needs to complete its review in the App Review information section of App Store Connect, including:
> - General information about the app's concept, features, and intended audience
> - Demo account credentials for account-based features
> - Required documentation for regulated fields
>
> Submitting all required information and documentation up front can ensure a faster and more predictable review. Incomplete submissions will be rejected.
> Provide information about the app
> Tell App Review about your app in general, covering who it's for and how it works:
> - New apps: Describe your app's concept and business model.
> - Updates: Describe what's changed, and where reviewers can find significant new content or features.
> - Purpose and audience: Describe the app's purpose and target audience.
> - Devices and OS versions tested: List the device models and operating systems you tested the app on before submitting.
> - External services and platforms: List the external services, tools, or platforms the app uses to deliver its core functionality (for example, data providers, authentication services, payment processors, or AI services).
> - Required hardware: Apps with required hardware must provide a video (not a screen recording) that shows your app running on a physical Apple device as it pairs and interacts with the hardware.
> - Regional differences: Describe any regional differences in the app's features or content, or confirm that the app functions consistently across all regions.
>
> Provide demo accounts
> Add up-to-date demo account login credentials:
> - Enter a username and password that work at the time of submission. Credentials that expire or change before your review starts may result in the submission being rejected.
> - If your app has multiple account types, such as administrative and general user accounts, use the Notes field to add additional credentials for each type.
> - If your app offers auto-renewable subscriptions, provide a demo account with an expired subscription to enable review of the entire purchase flow.
> - If your app requires an authentication code in addition to or instead of login credentials, include it in the Notes field in advance. Without it, a call may be required to continue the review. Calls are typically completed within three to five business days.
>
> Provide required documentation
> Developers with apps operating in regulated fields must provide documentation demonstrating they are qualified and authorized to provide those services. If the app is available in multiple countries and regions, developers may need to provide additional documentation for each location where the app is distributed. Similarly, developers with apps containing protected content must show they have permission to include it in the app.
> Provide required documentation, which can vary by app type:
> - Medical apps that make diagnostic or treatment claims: Regulatory clearance for each country or region where the app is available, such as FDA, CE, or CFDA documentation, or a supporting test report or peer-reviewed study.
> - Cryptocurrency exchange apps: A cryptocurrency exchange license for each country or region where the app is available, plus partnership documentation if you're working with a third-party exchange.
> - Financial apps, including apps that offer loans: Documentation showing your partnership with the licensed financial institution or lender providing the underlying service.
> - Apps offering gambling, lotteries, or real-money gaming: The applicable gambling or lottery license for each storefront where your app is available.
> - Apps that use another party's intellectual property: Trademark or rights documentation, such as a signed contract, or email correspondence showing you have permission.
>
> If your app falls into one of these categories, attach everything App Review will need to complete its review in the App Review Information section before you submit.
> If you're unsure what information your app's review needs, consider requesting a one-on-one appointment to discuss your app's concept before you submit.
> Documentation examples by guideline
>
> | App Review Guideline | Documentation typically requested |
> |---|---|
> | 1.4.1: Diagnosing or Treating Patients | Regulatory clearance (FDA, CE, or CFDA documentation); a supporting test report or peer-reviewed study. |
> | 1.4.3: Cannabis, Alcohol, and Illegal Substances | Cannabis dispensary license. |
> | 1.7: Reporting Criminal Activity | Documentation confirming the developer's partnership with law enforcement or a government entity, printed on that entity's official letterhead. |
> | 2.1: Registration Verification | International Standard Book Number (ISBN) or GRN documentation (China). |
> | 3.1.5: Cryptocurrencies | Cryptocurrency exchange license; partnership documentation if you're leveraging a third-party exchange partner; legal opinion. |
> | 3.2.1: Financial Apps | Documentation showing your partnership with the financial institution or bank providing the underlying service. |
> | 3.2.1 / 3.2.2: Apps Offering Loans | Loan license; business license; partnership documentation demonstrating the formal agreement between you and a licensed lender. |
> | 4.1 / 5.2.1 / 5.2.3: Third-party trademarks, copycat concepts, fan apps, sports and sporting events, specific marks, audio/video/music, and apps that download or stream third-party content | Trademark or rights documentation, such as a signed contract, electronic communication (emails, messaging-service screenshots), video recordings, or licensing documents. |
> | 5.0: Published Works for Sale in China | Publication permit; Internet Publishing License; Internet Culture Operations Permit; Operating License of Publication; Radio and Television Program Production license, where applicable. |
> | 5.1.1: Verifying Seller and Company | Partnership evidence, for example with an insurance company, brokerage, or applicable government body. |
> | 5.1.3: Health and Human Research | Ethics Review Board or Institutional Review Board (IRB) approval; human research consent form. |
> | 5.3.3: Lotteries and Raffles | Gambling license; SUSEP and SECAP documents (Brazil); lottery app license (China). |
> | 5.3.4: Gambling | Gambling license. |
>
> Use a demonstration mode when appropriate
> If your app handles sensitive user information, or operates in a highly regulated industry, you can implement a demonstration mode instead of providing a demo account. A demonstration mode should show your app's full features and functionality using demonstration data.

**Applies to:** All app submissions (documentation rows: apps in the listed regulated categories)

- **[SUBMIT-99]** For a new app, do the Notes describe the app's concept and business model?
  - quote: "New apps: Describe your app's concept and business model."
  - surface: asc
  - verify: App Review Information > Notes (first version only) contains concept and business model (free/paid/IAP/subscription/ads).
  - fix: Draft Notes text from the code inventory (features, StoreKit products, ad SDKs) for the developer to confirm.
- **[SUBMIT-100]** For an update, do the Notes describe what changed and where reviewers can find significant new content or features?
  - quote: "Updates: Describe what's changed, and where reviewers can find significant new content or features."
  - surface: asc
  - verify: Notes mention the changes and navigation paths; compare with `git log <last-release-tag>..HEAD` in code.
  - fix: Draft a change summary with navigation steps from the git diff for the developer to confirm.
- **[SUBMIT-101]** Do the Notes describe the app's purpose and target audience?
  - quote: "Purpose and audience: Describe the app's purpose and target audience."
  - surface: asc
  - verify: Notes include purpose and audience.
  - fix: Add a purpose/audience sentence (developer confirms).
- **[SUBMIT-102]** Do the Notes list the device models and OS versions the app was tested on?
  - quote: "Devices and OS versions tested: List the device models and operating systems you tested the app on before submitting."
  - surface: asc
  - verify: Notes include device models + OS versions.
  - fix: manual — developer lists the devices/OS versions actually tested.
- **[SUBMIT-103]** Do the Notes list the external services, tools, or platforms used for core functionality (data providers, authentication, payments, AI services)?
  - quote: "External services and platforms: List the external services, tools, or platforms the app uses to deliver its core functionality"
  - surface: code
  - verify: Inventory dependencies (Podfile.lock, Package.resolved, Cartfile.resolved) and network hosts in code (`grep -rnoE "https://[a-zA-Z0-9.-]+" --include=*.swift`): auth (Firebase, Auth0, Supabase), payments (Stripe, RevenueCat), AI (OpenAI, Anthropic, Gemini), data APIs. Compare against Notes.
  - fix: Add the detected list to Notes.
- **[SUBMIT-104]** If the app requires hardware, is a video (not a screen recording) of the app running on a physical Apple device pairing and interacting with the hardware provided?
  - quote: "Apps with required hardware must provide a video (not a screen recording) that shows your app running on a physical Apple device as it pairs and interacts with the hardware."
  - surface: code
  - verify: Grep for CoreBluetooth (CBCentralManager), ExternalAccessory (EAAccessoryManager, UISupportedExternalAccessoryProtocols), Matter/HomeKit, AccessorySetupKit, CoreNFC tags of specific devices; if found, App Review Information attachment contains a video.
  - fix: manual — developer records the video and attaches it (or links it in Notes).
- **[SUBMIT-105]** Do the Notes describe regional differences in features/content, or confirm consistent function across regions?
  - quote: "Regional differences: Describe any regional differences in the app's features or content, or confirm that the app functions consistently across all regions."
  - surface: code
  - verify: Grep for region gating (`Locale.current.region`, `regionCode`, `SKStorefront`, `Storefront.current`, country checks, remote-config by country); compare against Notes.
  - fix: Add a regional-differences statement to Notes.
- **[SUBMIT-106]** Do the demo credentials work at the time of submission?
  - quote: "Enter a username and password that work at the time of submission."
  - surface: runtime
  - verify: Launch the build in Simulator/device and sign in with the credentials from App Review Information.
  - fix: Reset/create the demo account on the backend; update ASC.
- **[SUBMIT-107]** If the app offers auto-renewable subscriptions, is a demo account with an expired subscription provided?
  - quote: "If your app offers auto-renewable subscriptions, provide a demo account with an expired subscription to enable review of the entire purchase flow."
  - surface: code
  - verify: Detect auto-renewable products (StoreKit `Product.SubscriptionInfo`, `.autoRenewable`, .storekit configuration files, RevenueCat entitlements; ASC Subscriptions); if present, Notes/Sign-in describe an account whose subscription is expired.
  - fix: Create/describe such an account in Notes.
- **[SUBMIT-108]** If the app requires an authentication code (2FA/OTP), is it included in Notes in advance?
  - quote: "If your app requires an authentication code in addition to or instead of login credentials, include it in the Notes field in advance."
  - surface: code
  - verify: Grep for OTP/SMS verification flows (`oneTimeCode` textContentType, PhoneAuthProvider, verification code screens, magic links); Notes include a static code or bypass.
  - fix: Provide a fixed test code for the demo account and add it to Notes.
- **[SUBMIT-109]** If the app is in a regulated field or uses another party's IP, is the required documentation (per the table) attached in App Review Information before submitting?
  - quote: "If your app falls into one of these categories, attach everything App Review will need to complete its review in the App Review Information section before you submit."
  - surface: manual
  - verify: Classify the app (medical claims, crypto exchange, financial/loans, gambling/lotteries, third-party IP, China published works, research, law enforcement reporting) from code and metadata; check App Review Information > Attachment.
  - fix: manual — developer obtains and attaches the documents listed in the table.
- **[SUBMIT-110]** If a demonstration mode is used instead of a demo account, does it show the app's full features and functionality using demonstration data?
  - quote: "A demonstration mode should show your app's full features and functionality using demonstration data."
  - surface: runtime
  - verify: Launch the app, enter demo mode, and exercise every main feature.
  - fix: Extend demo mode to cover all features; describe how to enter it in Notes.

## SUBMIT.REVIEW.PREP App Review — Preparing for review and Submitting for review

**Source text (verbatim):**
> We review all apps, app updates, app bundles, in-app purchases, and in-app events submitted to App Store Connect to help provide a safe and trusted experience for users and the opportunity for developers to succeed. As you plan and build, use these guidelines and resources to help the review process go as smoothly as possible.
> Guidelines
> Get in-depth details on the technical, content, and design criteria that we use for review, and learn about other key guidelines.
> - App Review Guidelines
> - Human Interface Design Guidelines
> - Guidelines for Using Apple Trademarks and Copyrights
>
> Apple Developer Program License Agreement
> The Apple Developer Program License Agreement details your obligations and responsibilities for the use of Apple software and services. The latest agreement can be found on the Agreements and Guidelines page.
> App review information
> If your app requires specific settings, user account information, or special instructions, include these details in the App Review Information section of App Store Connect. If you don’t include this information, the app review process may be delayed and your app may not pass review.
> Submitting for review
> When you submit for review in App Store Connect, you can:
> - Manage your submissions and communicate with App Review on the App Review page within Apps. You can visit the App Review page at any time, even if you don’t have active submissions or conversations.
> - Submit items such as in-app events, custom product pages, and product page optimization tests without needing a new app version.
> - Include multiple items in one submission.
> - Remove items with issues from your submission and continue with items that were accepted by App Review.
> - View a history of submissions created using the updated experience, including messages from App Review.
> - Decide whether your app is reviewed for the App Store or Notarization only.
>
> Review status
> App Review works around the clock, typically reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours.
> You’ll be notified by email of status changes. You can also check the review status of your submission in the Apps section of App Store Connect or on the App Store Connect app for iPhone and iPad. If your submission is incomplete, review times may be delayed or your submission may not pass.

**Applies to:** All apps

- **[SUBMIT-112]** If the app requires specific settings, user account information, or special instructions, are they in App Review Information?
  - quote: "If your app requires specific settings, user account information, or special instructions, include these details in the App Review Information section of App Store Connect."
  - surface: code
  - verify: Detect setup prerequisites in code (feature flags, server environment toggles, required permissions, onboarding codes, invite-only flows, location-specific features) and check Notes covers them.
  - fix: Add the settings/instructions to Notes.

## SUBMIT.COMMON App Review — Avoiding common issues

**Source text (verbatim):**
> We’ve highlighted some of the most common issues to help you better prepare before submitting for review. On average, over 40% of unresolved issues are related to guideline 2.1: App Completeness, which covers crashes, placeholder content, incomplete information, and more.
> Crashes and bugs
> Submit items for review only when they’re complete and ready to be published. Make sure to thoroughly test on devices running the latest software and fix all bugs before submitting. View guideline 2.1.
> Broken links
> All links in your app must be functional. A link to user support with up-to-date contact information and a link to your privacy policy is required for all apps. View guideline 2.1 and guideline 5.1.
> Placeholder content
> Finalize all images and text before submitting for review. Items that are still in progress and contain placeholder content are not ready to be distributed and cannot be approved. View guideline 2.1.
> Incomplete information
> Enter all of the details needed for review in the App Review Information section of App Store Connect. If some features require signing in, provide a valid demo account username and password. If there are special configurations to set, include the specifics. If features require an environment that is hard to replicate or require specific hardware, be prepared to provide a demo video or the hardware. Also, please make sure your contact information is complete and up to date. View guideline 2.1.
> Specific documentation is required for certain scenarios and types of apps. Here are a few examples:
> - If the app is for kids and contains third-party ads, provide a link to the ad services’ publicly documented practices and policies for Kids category apps, including human review of ad creatives for age appropriateness. View guideline 1.3.
> - If the app works with medical hardware, provide a copy of regulatory clearance for the locations where the app is available. View guideline 1.4.
> - If the app features third-party trademarks or copyrighted content or lets users stream or download third-party content, provide the authorization to do so. Examples include video streaming and marketing that uses imagery of celebrities, sports, movies, or music. View guideline 4.1 and guideline 5.2.
> - If the app facilitates services requiring licensing, such as real money gaming and gambling, lotteries, raffles, and VPN licensing, provide the authorization to do so. Note that licensing requirements may vary depending on region. View guideline 5.
>
> Privacy policy issues
> Make sure your privacy policy adheres to guideline 5.1 and:
> - Identifies the data the app collects, how it collects that data, and all uses of that data.
> - Confirms that any third party with whom the app shares user data provides the same or equal protection of user data as stated in the app’s privacy policy.
> - Explains your data retention and deletion policies and describes how a user can revoke consent and/or request deletion of their data.
>
> Unclear data access requests
> When requesting permission to access user or usage data, you should clearly and completely describe how your app will use the data. Including an example can help users understand why your app is requesting access to their personal information.
> If your app’s code references one or more APIs that access sensitive user data, the app’s Info.plist file should contain a $!{infoPlistKey} key with a user-facing purpose string explaining clearly and completely why your app needs the data. All apps submitted to App Store Connect that access user data are required to include a purpose string.
> Inaccurate screenshots
> Screenshots should accurately communicate value and functionality. Use text and overlay images to highlight the user experience, not obscure it. To learn more, visit 2.3.3 - Show your app in use with screenshots on App Review Help and view guideline 2.3.
> Substandard user interface
> Apple places a high value on clean, refined, and user-friendly interfaces. Make sure your UI meets these requirements by planning your design carefully and following our design guides.
> Web clippings, content aggregators, or a collection of links
> Your app should be engaging and useful, and make the most of the features unique to iOS. Websites served in an iOS app, web content that is not formatted for iOS, and limited web interactions do not make a quality app. View guideline 4.2.
> Repeated submission of similar apps
> Submitting several apps that are essentially the same ties up the App Review process and risks your apps not passing review. Improve your review experience — and the experience of your future users — by thoughtfully combining your apps into one. View guideline 4.3.
> Copycats
> When working on your app, focus on creating interesting, unique experiences that aren’t already available. Apps that actively try to copy other apps won’t pass review. To learn more, visit 4.1 - Preventing copycat and impersonation rejections on App Review Help and view guideline 4.1.
> Misleading users
> Your app must perform as advertised and should not give users the impression the app is something it is not. If your app appears to promise certain features and functionalities, it needs to deliver. View guideline 2.3.
> Not enough lasting value
> If your app doesn’t offer much functionality or content, or only applies to a small niche market, it may not be approved. Before creating your app, take a look at the apps in your category on the App Store and consider how you can provide an even better user experience. View guideline 4.2.
> Submitted by incorrect entity
> Certain types of apps must be submitted by the legal entity that provides the services rather than an individual developer. These apps include, but are not limited to, those that require sensitive user information or provide services in highly regulated fields, such as banking and financial services, cryptocurrency, healthcare, gambling, and air travel. If you need to provide partnership documentation or authorization, attach the files in the Attachment section in App Store Connect and provide any descriptions or links in the Review Notes field. View guideline 3 and guideline 5.1.1.
> Technical Support
> If your app didn’t pass review for technical reasons, such as crashes or bugs, view the following documentation:
> - Acquiring Crash Reports and Diagnostic Logs
> - Analyzing a Crash Report
> - Identifying the Cause of Common Crashes
>
> You can also visit the Apple Developer Forums or request code-level support.

**Applies to:** All apps (documentation bullets: the condition stated in each bullet)

- **[SUBMIT-113]** Has the app been thoroughly tested on devices running the latest software with all known bugs fixed?
  - quote: "Make sure to thoroughly test on devices running the latest software and fix all bugs before submitting."
  - surface: runtime
  - verify: Build and run on a simulator/device with the latest iOS; exercise every main flow (launch, onboarding, sign-in, purchase, settings); run the test suite (`xcodebuild test`); check Xcode Organizer/TestFlight crash reports for the build.
  - fix: Fix crashes/bugs found; re-upload.
- **[SUBMIT-114]** Are all links in the app functional?
  - quote: "All links in your app must be functional."
  - surface: code
  - verify: Extract URL literals (`grep -rhoE "https?://[^\"' )]+" --include=*.swift --include=*.m --include=*.plist --include=*.strings --include=*.xcstrings`) and request each (`curl -sIL -o /dev/null -w "%{http_code}"`); flag non-2xx/3xx. At runtime, tap in-app links.
  - fix: Update or remove broken URLs.
- **[SUBMIT-115]** Does the app provide a link to user support with up-to-date contact information and a link to the privacy policy?
  - quote: "A link to user support with up-to-date contact information and a link to your privacy policy is required for all apps."
  - surface: code
  - verify: Grep for support/privacy URLs or views in the app (Settings/About screens); check ASC Support URL (version page) and Privacy Policy URL (App Information) resolve and show contact info / a privacy policy.
  - fix: Add Support and Privacy Policy links in the app's settings/about screen and fill ASC URLs.
- **[SUBMIT-116]** Are all images and text finalized (no placeholder content)?
  - quote: "Finalize all images and text before submitting for review."
  - surface: code
  - verify: `grep -rniE "lorem ipsum|placeholder|TODO|FIXME|coming soon|test test|sample text|xxx" --include=*.swift --include=*.strings --include=*.xcstrings --include=*.storyboard --include=*.xib`; inspect Assets.xcassets for empty image sets or default/template images; runtime walkthrough.
  - fix: Replace placeholder text/images with final content; hide unfinished features.
- **[SUBMIT-117]** If there are special configurations to set, are the specifics included in App Review Information?
  - quote: "If there are special configurations to set, include the specifics."
  - surface: asc
  - verify: Compare configuration prerequisites found in code (SUBMIT-112) against Notes.
  - fix: Add configuration steps to Notes.
- **[SUBMIT-118]** If features require a hard-to-replicate environment or specific hardware, is a demo video (or hardware) ready?
  - quote: "If features require an environment that is hard to replicate or require specific hardware, be prepared to provide a demo video or the hardware."
  - surface: manual
  - verify: See SUBMIT-104 detection; ask developer whether a video is attached/linked.
  - fix: manual — record a demo video and attach/link it.
- **[SUBMIT-119]** Is the App Review contact information complete and up to date?
  - quote: "Also, please make sure your contact information is complete and up to date."
  - surface: asc
  - verify: App Review Information > Contact fields (see SUBMIT-93); developer confirms they are current.
  - fix: Update the contact fields.
- **[SUBMIT-120]** If the app is for kids and contains third-party ads, is a link to the ad services’ Kids category practices and policies (including human review of ad creatives) provided?
  - quote: "If the app is for kids and contains third-party ads, provide a link to the ad services’ publicly documented practices and policies for Kids category apps, including human review of ad creatives for age appropriateness."
  - surface: code
  - verify: Made for Kids selected (ASC) and ad SDK present (SUBMIT-52); Notes contain the ad network's Kids policy link.
  - fix: Add the link to Notes, or remove third-party ads.
- **[SUBMIT-121]** If the app works with medical hardware, is a copy of regulatory clearance for the available locations provided?
  - quote: "If the app works with medical hardware, provide a copy of regulatory clearance for the locations where the app is available."
  - surface: manual
  - verify: Detect BLE/accessory integrations with medical devices (glucose, blood pressure, ECG — CBUUID service UUIDs like 0x1808, 0x1810) in code; check App Review Information attachment.
  - fix: manual — attach clearance documents.
- **[SUBMIT-122]** If the app features third-party trademarks/copyrighted content or lets users stream/download third-party content, is authorization provided?
  - quote: "If the app features third-party trademarks or copyrighted content or lets users stream or download third-party content, provide the authorization to do so."
  - surface: manual
  - verify: Inspect app name, icon, screenshots, bundled media and streaming sources; check App Review Information attachment/Notes.
  - fix: manual — attach licences/authorization.
- **[SUBMIT-123]** If the app facilitates licensed services (real money gaming, gambling, lotteries, raffles, VPN), is authorization provided?
  - quote: "If the app facilitates services requiring licensing, such as real money gaming and gambling, lotteries, raffles, and VPN licensing, provide the authorization to do so."
  - surface: code
  - verify: Grep for NetworkExtension (`NEVPNManager`, `NETunnelProviderManager`, `com.apple.developer.networking.networkextension` entitlement) and gambling/lottery features; check App Review Information attachment.
  - fix: manual — attach the licence(s) for each region.
- **[SUBMIT-124]** Does the privacy policy identify the data collected, how it is collected, and all uses of that data?
  - quote: "Identifies the data the app collects, how it collects that data, and all uses of that data."
  - surface: manual
  - verify: Fetch the Privacy Policy URL from ASC and read it; compare with data collected in code (analytics SDKs, PrivacyInfo.xcprivacy NSPrivacyCollectedDataTypes, network payloads).
  - fix: manual — developer/legal updates the privacy policy (a draft can be generated from the code inventory).
- **[SUBMIT-125]** Does the privacy policy confirm that third parties receiving user data provide the same or equal protection?
  - quote: "Confirms that any third party with whom the app shares user data provides the same or equal protection of user data as stated in the app’s privacy policy."
  - surface: manual
  - verify: Read the privacy policy for this statement; list third-party SDKs/services from code.
  - fix: manual — add the statement (legal review).
- **[SUBMIT-126]** Does the privacy policy explain data retention and deletion policies and how a user can revoke consent and/or request deletion?
  - quote: "Explains your data retention and deletion policies and describes how a user can revoke consent and/or request deletion of their data."
  - surface: manual
  - verify: Read the privacy policy for retention, deletion, consent revocation sections.
  - fix: manual — add these sections (legal review).
- **[SUBMIT-127]** For every API in the code that accesses sensitive user data, does Info.plist contain the corresponding purpose string key?
  - quote: "All apps submitted to App Store Connect that access user data are required to include a purpose string."
  - surface: code
  - verify: Map APIs to keys, e.g., AVCaptureDevice → NSCameraUsageDescription; AVAudioSession record / AVAudioRecorder → NSMicrophoneUsageDescription; PHPhotoLibrary → NSPhotoLibraryUsageDescription / NSPhotoLibraryAddUsageDescription; CLLocationManager → NSLocationWhenInUseUsageDescription; CNContactStore → NSContactsUsageDescription; EKEventStore → NSCalendarsFullAccessUsageDescription / NSRemindersFullAccessUsageDescription; HKHealthStore → NSHealthShareUsageDescription / NSHealthUpdateUsageDescription; CBCentralManager → NSBluetoothAlwaysUsageDescription; SFSpeechRecognizer → NSSpeechRecognitionUsageDescription; ATTrackingManager → NSUserTrackingUsageDescription; LAContext Face ID → NSFaceIDUsageDescription; CMMotionManager → NSMotionUsageDescription; MPMediaLibrary → NSAppleMusicUsageDescription; NWBrowser/Bonjour → NSLocalNetworkUsageDescription. Check Info.plist and INFOPLIST_KEY_* build settings (and SDK-triggered APIs).
  - fix: Add the missing NS*UsageDescription keys with specific user-facing text.
- **[SUBMIT-128]** Do purpose strings clearly and completely describe how the app will use the data (ideally with an example)?
  - quote: "When requesting permission to access user or usage data, you should clearly and completely describe how your app will use the data."
  - surface: code
  - verify: Read each NS*UsageDescription value (Info.plist and InfoPlist.strings / .xcstrings localizations); flag empty, generic ("This app needs camera access"), or developer-facing text.
  - fix: Rewrite each string to state the specific feature and use, e.g., "Scan your class notes with the camera to save them as PDFs."
- **[SUBMIT-129]** Do screenshots accurately communicate the app's value and functionality, with text/overlays that don't obscure the UI?
  - quote: "Screenshots should accurately communicate value and functionality."
  - surface: asc
  - verify: Compare ASC screenshots (each device size/localization) with screens observed at runtime.
  - fix: Recapture screenshots from the current build.
- **[SUBMIT-130]** Is the app more than a website served in an app, unformatted web content, or limited web interactions?
  - quote: "Websites served in an iOS app, web content that is not formatted for iOS, and limited web interactions do not make a quality app."
  - surface: code
  - verify: Check whether the main UI is a single WKWebView loading a remote site (e.g., root view is a WebView with `load(URLRequest(url: "https://..."))`) with little native functionality.
  - fix: manual — add native functionality (developer decision); see guideline 4.2 reference.
- **[SUBMIT-131]** Is the developer not submitting several apps that are essentially the same?
  - quote: "Submitting several apps that are essentially the same ties up the App Review process and risks your apps not passing review."
  - surface: manual
  - verify: Review the developer's app list in ASC for near-duplicates (same codebase/bundle ID prefix with minor changes).
  - fix: manual — combine apps into one.
- **[SUBMIT-132]** Does the app perform as advertised (features promised in metadata are delivered)?
  - quote: "Your app must perform as advertised and should not give users the impression the app is something it is not."
  - surface: runtime
  - verify: List features claimed in the ASC description/subtitle/screenshots and confirm each exists in code and at runtime.
  - fix: Remove claims for missing features or implement them.
- **[SUBMIT-133]** If the app requires sensitive user information or is in a highly regulated field (banking/financial, cryptocurrency, healthcare, gambling, air travel), is it submitted by the legal entity that provides the services?
  - quote: "Certain types of apps must be submitted by the legal entity that provides the services rather than an individual developer."
  - surface: manual
  - verify: Check the developer account type (individual vs organization) and seller name in ASC against the service provider; ask the developer.
  - fix: manual — submit from the service provider's organization account, or attach partnership documentation in Attachment and describe in Notes.
- **[SUBMIT-151]** Is the app not an attempt to copy another app (it offers its own experience rather than copying an existing app)?
  - quote: "Apps that actively try to copy other apps won’t pass review."
  - surface: manual
  - verify: Compare the app name, icon, screenshots and core feature set with the top apps in its App Store category; ask the developer whether the app is modeled on a specific existing app.
  - fix: manual — differentiate the concept, name, and design (see guideline 4.1 reference).
- **[SUBMIT-152]** (Risk — Apple says such apps "may not be approved") Does the app offer enough functionality or content (not only a small niche market with little functionality)?
  - quote: "If your app doesn’t offer much functionality or content, or only applies to a small niche market, it may not be approved."
  - surface: runtime
  - verify: Exercise the app and count distinct features/screens; compare with apps in the same category on the App Store. Report as WARN, not FAIL.
  - fix: manual — add functionality or content (developer decision); see guideline 4.2 reference.
- **[SUBMIT-153]** Does the UI follow Apple's design guides (clean, refined, user-friendly)?
  - quote: "Make sure your UI meets these requirements by planning your design carefully and following our design guides."
  - surface: runtime
  - verify: Walk every screen at runtime on current device sizes (incl. iPad if supported); flag clipped/overlapping layouts, unreadable text, non-standard controls that break platform conventions (Human Interface Guidelines).
  - fix: Fix the layout/UI issues found; follow the Human Interface Guidelines.

## SUBMIT.EXPEDITE Request an expedited review

**Source text (verbatim):**
> App Review works around the clock with the goal of reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours. However, if you're facing extenuating circumstances, such as fixing a critical bug or timing your release to coincide with an event, you can request an expedited review.
> Submit the app for review in App Store Connect. Only submissions that have already been sent to App Review can be expedited. Make sure the app is ready for review by adding all required information in the Notes field and providing a demo account or demo mode for account-based features.
> Go to Request an Expedited App Review, select the app and platform which you would like to receive an expedited review, and submit.
> App Review will evaluate your request and expedite the app's review as allowed by availability and demand.
> Note: Expedite requests should be reserved for matters of genuine urgency.
> Critical bug fixes
> If you're requesting an expedited review to fix a critical bug, include this information in the Notes field in App Store Connect when you submit the app for review.
> Event-related apps
> If you're requesting an expedited review to align the app's release with an upcoming event, include the event, its date, and how your app is associated with it in the Notes field in App Store Connect when you submit the app for review. Schedule its release in App Store Connect ahead of time if you can.
>
> Expedited reviews
> You can request the review of your app to be expedited if you face extenuating circumstances, such as fixing a critical bug in your app or releasing your app to coincide with an event you’re directly associated with.
> Critical bug fix. When submitting an expedited review to fix a critical bug, include the steps to reproduce the bug on the current version of your app.
> Event-related app. For apps associated with an event, we recommend you plan and schedule the release of your app in App Store Connect. However, if your app is still in review and the launch of your event is quickly approaching, you can request to have your app review expedited. Make sure your request includes the event, date of the event, and your app’s association with the event.

**Applies to:** Developers requesting an expedited review

- **[SUBMIT-134]** Has the submission already been sent to App Review before requesting expedite?
  - quote: "Only submissions that have already been sent to App Review can be expedited."
  - surface: asc
  - verify: Submission status is Waiting for Review or In Review.
  - fix: Submit for Review first (SUBMIT-08).
- **[SUBMIT-135]** For a critical bug fix expedite, do the Notes include the bug information and steps to reproduce it on the current version?
  - quote: "When submitting an expedited review to fix a critical bug, include the steps to reproduce the bug on the current version of your app."
  - surface: asc
  - verify: App Review Information > Notes contains reproduction steps.
  - fix: Add reproduction steps to Notes.
- **[SUBMIT-136]** For an event-related expedite, do the Notes include the event, its date, and the app's association with it?
  - quote: "include the event, its date, and how your app is associated with it in the Notes field in App Store Connect when you submit the app for review"
  - surface: asc
  - verify: Notes contain event name, date, and association.
  - fix: Add the event details; schedule release (Version Release: Automatic, no earlier than) where possible.

## SUBMIT.APPEAL Appeal to the App Review Board

**Source text (verbatim):**
> If you disagree with the outcome of a review, you can file an appeal with the App Review Board. It's appropriate to file an appeal when:
> - Your app was rejected or removed, but you believe it follows the App Review Guidelines and the Apple Developer Program License Agreement.
> - Your account is facing termination, but you believe it complies with the App Review Guidelines and the Apple Developer Program License Agreement.
> - You believe you experienced unfair or biased treatment during review.
>
> Note: Don't file an appeal to reinstate an already-terminated account, get a status update on your app, or request an expedited review. For these requests, use the appropriate Contact Us form instead.
> Before filing an appeal, reply to the rejection, removal, or termination message you received in App Store Connect and provide clarification about the issue. If this clarification is not sufficient to resolve the issue, proceed with filing an appeal.
> Go to Submit an appeal to App Review and describe why you believe your app or account follows the App Review Guidelines and the Apple Developer Program License Agreement.
> For app rejections or removals, point to the specific requirements involved and explain how your app satisfies them.
> For account terminations, reference the specific terms your account was found to be violating, and explain how your account meets those requirements. If the termination references other guideline violations you believe were in error, provide an additional explanation of those instances as well.
> The App Review Board will send you a message in App Store Connect once its investigation is complete. They may also message you in App Store Connect to request additional information or schedule a call to discuss the outcome of the investigation.
> Note: Only submit one appeal per rejected or removed app. If an app's rejection or removal message cites multiple guideline violations, address all of them in one appeal.
> What to include in your appeal
> Do
> - Cite the specific guideline or terms your app was rejected or removed under, and explain point by point how your app meets it.
> - Include additional information about your app that is relevant to the rejection, removal, or pending termination decision you're disputing.
> - Use the form to submit appeals for up to five rejected or removed apps.
>
> Don't
> - Don't file an appeal for requests from App Review for additional information or documentation about your app. This information is necessary for App Review to complete the review.
> - Don't include information that is not relevant to the rejection, removal, or pending termination decision you are appealing.
> - Don't file an appeal if you've addressed the issues App Review identified and resubmitted the app for review.
>
> Example (Complete)
> "My app was rejected under Guideline 2.1 for incomplete information. The demo account and setup steps needed to test the flagged feature are included in the App Review Information section of this submission, along with screenshots showing the feature working as described."
> Example (Incomplete)
> "This app is important to my business and shouldn't have been rejected. Please take another look."
> Note: Appeals that include all required information help the App Review Board process your request quickly. Submitting a complete appeal does not guarantee that the App Review Board will overturn the rejection, removal, or termination.
>
> Appeals
> If you file an appeal, make sure to:
> - Provide specific reasons why you believe your app complies with the App Review Guidelines.
> - Submit only one appeal per submission that didn’t pass review.
> - Respond to any requests for additional information before submitting an appeal.

**Applies to:** Developers whose app was rejected/removed or account faces termination and who disagree with the outcome

- **[SUBMIT-137]** Before appealing, did the developer reply to the rejection message in App Store Connect with clarification?
  - quote: "Before filing an appeal, reply to the rejection, removal, or termination message you received in App Store Connect and provide clarification about the issue."
  - surface: asc
  - verify: App Review page > the rejected submission > message thread contains a developer reply.
  - fix: Reply to App Review with clarification first (SUBMIT.REPLY).
- **[SUBMIT-138]** Does the appeal cite the specific guideline(s) and explain point by point how the app meets each, addressing all cited violations in one appeal?
  - quote: "Cite the specific guideline or terms your app was rejected or removed under, and explain point by point how your app meets it."
  - surface: manual
  - verify: Review the appeal draft against the guideline numbers in the rejection message.
  - fix: Draft the appeal with one section per cited guideline, using evidence from the code and the App Review Information.
- **[SUBMIT-139]** Is only one appeal being filed for this rejected/removed app?
  - quote: "Only submit one appeal per rejected or removed app."
  - surface: manual
  - verify: Ask the developer whether an appeal is already open.
  - fix: manual — don't file a second appeal.
- **[SUBMIT-140]** Is the developer not appealing a request for additional information (which should be answered instead)?
  - quote: "Don't file an appeal for requests from App Review for additional information or documentation about your app."
  - surface: asc
  - verify: Read the App Review message: if it requests information/documentation, the correct action is a reply.
  - fix: Reply with the requested information instead of appealing.

## SUBMIT.REPLY Reply to App Review messages / Contact App Review for help with a submission

**Source text (verbatim):**
> If App Review or TestFlight App Review rejects your app, you can communicate with Apple and resolve issues in the App Review section.
> When your app is rejected, you'll get a message containing information about the rejection, including how it violates the App Review Guidelines or Notarization Review Guidelines. You can correspond with Apple, and include attachments, such as screenshots and supporting documents, until you resubmit to App Review. If your app was rejected for a metadata issue, you can resubmit the same build after resolving the issue.
> Required role: Account Holder, Admin, or App Manager. View role permissions.
> Reply to messages on the App Review page
> In Apps, select the app you want to view.
> At the top of the page, click the link that indicates that there are unresolved issues.
> In the In Progress section, click Resolve next to the submission you want to view.
> To reply, click Reply to App Review.
> Enter text in the Reply field.
> To include a file, click Attach File and, in the dialog that appears, choose a file.
> Click Reply.
>
> Contact App Review for help with a submission
> If a submission doesn't pass review, you'll receive a message from App Review in App Store Connect detailing the issues requiring your attention.
> If you have questions, contact App Review directly by clicking Reply to App Review in App Store Connect. Using App Store Connect to contact App Review is the best way to receive assistance with an ongoing submission. A specialist familiar with your app will reply to your message.
> What to include in your reply to App Review
> Do
> - Be specific about what you're asking, such as the exact feature, guideline, or step you need clarified.
> - Provide additional information that can help App Review understand the app's concept and intended functionality if you believe your app was misunderstood.
>
> Don't
> - Don't use the Reply to App Review field to appeal a rejection or removal or to request an expedited review. For these requests, use the appropriate Contact Us form instead.
> - Don't ask about the status of apps from other developers. Just as App Review wouldn't discuss your app with someone else, App Review can't discuss other developers' apps with you.
>
> Request a call with an Apple representative
> If you need additional assistance after App Review replies to your message, you can use the Reply to App Review message window to request a call with an Apple representative.
> Before requesting a call, confirm your contact details in the App Review Information section of App Store Connect are up to date.
> When requesting a call, include your time zone so App Review can attempt to call during your local business hours. You can also specify a preferred language for the call. App Review will try to accommodate your request, though availability can vary. Calls are typically completed within three to five business days.

**Applies to:** Submissions that did not pass review

- **[SUBMIT-141]** If the rejection was for a metadata issue only, is the developer resubmitting the same build after fixing the metadata (rather than uploading an unnecessary new build)?
  - quote: "If your app was rejected for a metadata issue, you can resubmit the same build after resolving the issue."
  - surface: asc
  - verify: Read the rejection message: guideline concerns metadata (description, screenshots, keywords, name); confirm metadata is updated.
  - fix: Update the metadata, then reply/resubmit with the same build.
- **[SUBMIT-142]** Is the reply to App Review specific (exact feature, guideline, or step) and not used to appeal or request expedite?
  - quote: "Be specific about what you're asking, such as the exact feature, guideline, or step you need clarified."
  - surface: manual
  - verify: Review the reply draft.
  - fix: Rewrite the reply to reference the exact guideline/feature; use the appeal or expedite forms for those requests.
- **[SUBMIT-143]** Before requesting a call, are the App Review Information contact details up to date, and does the request include a time zone?
  - quote: "Before requesting a call, confirm your contact details in the App Review Information section of App Store Connect are up to date."
  - surface: asc
  - verify: App Review Information > Contact fields; reply text includes time zone.
  - fix: Update contact details; add time zone (and optional preferred language) to the request.

## SUBMIT.BUGFIX Accept Bug Fix Submission offers

**Source text (verbatim):**
> If a bug-fix update is rejected but introduces no legal or safety concerns, you can choose to resolve the issues in your next submission. This process allows you to deliver bug fixes quickly, giving you time to resolve any outstanding issues in your next submission.
> Note: Bug Fix Submission offers are only available for updates to apps that have been previously approved for the App Store or alternative distribution.
> In App Store Connect, open the rejection message. If your submission is eligible, this language will appear at the top of the message:
> "Bug Fix Submissions: The issues we've identified below are eligible to be resolved on your next update."
> If you see the note, reply to the message and let App Review know you'd like the current submission approved and will address the issues in your next update. Do not resubmit the app at this time, as it will trigger a new review.
> If you don't see the note, the submission doesn't qualify, and you'll need to resolve the issues before the submission can be approved.
> App Review will reply to confirm and approve the submission.
> In your next update, resolve all deferred issues from the prior submission. App Review will verify that each issue has been addressed before approving the update.
> Note: Issues that were deferred on a previous submission aren't eligible to be deferred again on the next submission.
>
> Bug fix submissions
> If you’re submitting a bug fix update for your app and we find additional issues during review, you have the option to resolve the additional issues with your next submission, as long as there are no legal or safety concerns. To accept, simply reply to the offer message in App Store Connect and indicate you would like the current submission to be approved.

**Applies to:** Updates to previously approved apps whose rejection message contains the Bug Fix Submissions note

- **[SUBMIT-144]** If the rejection carries the Bug Fix Submissions note and the developer accepts, did they reply instead of resubmitting?
  - quote: "Do not resubmit the app at this time, as it will trigger a new review."
  - surface: asc
  - verify: Rejection message begins with "Bug Fix Submissions:"; the thread contains a developer reply accepting; no new submission was created.
  - fix: Reply to the message asking for the current submission to be approved.
- **[SUBMIT-145]** Does this update resolve all issues deferred from the prior Bug Fix Submission?
  - quote: "In your next update, resolve all deferred issues from the prior submission."
  - surface: code
  - verify: Collect deferred issues from the previous rejection message (ASC App Review history); verify each is fixed in code/metadata (map each guideline to the relevant checks in the guideline reference files).
  - fix: Fix every deferred issue before submitting — they can't be deferred again.

## SUBMIT.STATUS Track a submission’s review status / When to resubmit

**Source text (verbatim):**
> App Review works around the clock with the goal of reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours. While updates with minor changes and bug fixes typically move through review quickly, other submissions may take longer to verify.
> Check your submission status
> You can check the status of a submission at any time by visiting the App Review section of App Store Connect. Track the status of all your submitted items in one place, including your app versions, In-App Purchases, custom product pages, and more.
> Your submission will display one of several statuses during the review process, including:
> - Waiting for Review: Apple received your submission, but review hasn’t started. You can still edit certain information or remove items from the submission, though you can’t upload or edit screenshots and app previews.
> - In Review: App Review is reviewing your submission. You can cancel the submission to remove it from review.
> - Unresolved Issues: App Review identified issues with one or more items in the submission.
>
> For the full list of app, submission, and item statuses, see App and submission statuses.
> You can also set up webhooks to receive automatic server notifications whenever a submission’s status changes.
> When to resubmit for review
> In general, reserve resubmissions for changes that require a new review.
> It’s not necessary to resubmit when:
> - App Review requested more information and there are no other issues to resolve. Instead, you can reply directly to the message in App Store Connect. Resubmitting starts a new review, after which App Review can no longer reply to your previous message.
> - Issues can be resolved by revising metadata or making server-side adjustments, such as providing or activating demo credentials. Reply to App Review in App Store Connect once the required changes have been made.
> - You’ve been offered and want to accept approval for a Bug Fix Submission. Reply to the message to accept the offer without resubmitting. Learn more about accepting Bug Fix Submission offers.
> - You’re appealing a rejection or removal to the App Review Board. Resubmitting will initiate a new review and the appeal will be closed. Learn more about appealing to the App Review Board.
>
> It’s appropriate to resubmit when:
> - The submission is rejected for an issue in the build and you’ve fixed it. Upload the new build and submit that version. This starts a full review of the new build.
> - Some items in the submission were rejected, others were accepted, and you want to move ahead with approval on the accepted items. Remove the rejected items and resubmit.
>
> Note: Don’t resubmit until you’ve resolved every issue identified by App Review. Resubmitting with unresolved issues delays review and results in the same outcome. If you have questions about how to resolve an issue, contact App Review for help with a submission.
> Why some reviews take longer
> Most submissions are reviewed within 48 hours. Some need additional time for verification, particularly those involving the following:
> - Limited review history: Apps with little or no prior App Review history.
> - Required documentation: Authorizations, licenses, partnership agreements, or other materials App Review must confirm before approval.
> - Complex or novel issues: Regulated content, new platform capabilities, enabled entitlements, or other sensitive features that require greater scrutiny.
>
> To help reduce review time, provide information about your app and attach all required documentation in the App Review Information section before submitting. Learn more about providing information for a complete review.
> When fraud or malicious activity is detected
> To protect the App Store’s high standards for privacy, security, and quality, App Review has a zero-tolerance policy for fraudulent or malicious activity. App Review investigates all reported or identified conduct that falls outside the Developer Code of Conduct, which requires accurate representation and integrity across the app ecosystem. An investigation can extend a submission’s review. Examples include:
> - Misrepresented developer identity or impersonation, such as providing inauthentic documentation. (Guidelines 4.1 and 5.6.2)
> - Manipulation of the App Store experience, including gaming charts, search results, reviews, or referrals, or attempting to hide features in review. (Guidelines 2.3.1(a) and 5.6.3)
> - Submitting low-quality apps, as indicated by excessive customer reports such as negative customer reviews and high-volume refund requests. (Guidelines 4.3 and 5.6.4)
>
> When these signals appear, App Review investigates thoroughly. Repeated or serious violations can lead to additional rejections, app removals, and removal of your account from the Apple Developer Program.

**Applies to:** All submissions

- **[SUBMIT-146]** Before resubmitting, has every issue identified by App Review been resolved?
  - quote: "Don’t resubmit until you’ve resolved every issue identified by App Review."
  - surface: code
  - verify: List each guideline cited in the latest rejection message; for each, re-run the matching checks (guideline reference files) on the current code and metadata; all must pass.
  - fix: Fix remaining issues before resubmitting.
- **[SUBMIT-147]** If the issues are resolvable via metadata or server-side changes (e.g., activating demo credentials), is the developer replying instead of resubmitting?
  - quote: "Issues can be resolved by revising metadata or making server-side adjustments, such as providing or activating demo credentials. Reply to App Review in App Store Connect once the required changes have been made."
  - surface: asc
  - verify: Rejection reason type; whether a new submission was created vs. a reply sent.
  - fix: Make the metadata/server change and reply in the existing thread.
- **[SUBMIT-148]** If an appeal is open, is the developer not resubmitting (which would close the appeal)?
  - quote: "Resubmitting will initiate a new review and the appeal will be closed."
  - surface: manual
  - verify: Ask the developer whether an appeal is pending.
  - fix: manual — wait for the App Review Board outcome.
- **[SUBMIT-149]** Does the app avoid hiding features from App Review (e.g., code paths that disable features during review)?
  - quote: "attempting to hide features in review"
  - surface: code
  - verify: Grep for review-evasion patterns: date/version gates around features (`if Date() > ...`, `if version == reviewVersion`), remote-config flags like `isInReview`, `reviewMode`, `hideForReview`, checks for Apple IP ranges or sandbox receipts (`appStoreReceiptURL.lastPathComponent == "sandboxReceipt"`) toggling features, and features activated only by server flags after approval.
  - fix: Remove the hidden-feature mechanism; disclose all features (including server-toggled ones) in Notes.

## SUBMIT.UNRESOLVED Manage a submission with unresolved issues

**Source text (verbatim):**
> If any of the items in your submission are rejected, the submission status changes to Unresolved Issues. To consider a submission approved, App Review needs to approve all items. To continue with the accepted items, you need to either edit and resubmit, or remove the rejected items from the submission. When a submission has a status of Unresolved Issues, you can’t add more items to it.
> Remove rejected items
> In Apps, click View App Review Issues & Messages.
> In the In Progress section, click Resolve next to the submission.
> Hold the pointer over the item you want to remove, then click the delete button (–).
> Once you remove all rejected items, the submission moves to the Completed section of the App Review page and is ready for release.
> Edit and resubmit rejected items
> In Apps, click View App Review Issues & Messages.
> In the In Progress section, click Resolve next to the submission.
> Click Edit next to the item you want to edit.
> Make the necessary changes, then click Add for Review.
> You can edit items in a submission once before resubmission. If you no longer want to submit the item, you can remove it. Please note that you can’t add back removed items to the same submission.
> Once you edit or remove all rejected items, click Resubmit to App Review from the submission details page.

**Applies to:** Submissions with status Unresolved Issues

- **[SUBMIT-150]** For a submission with Unresolved Issues, has every rejected item been either edited or removed before clicking Resubmit to App Review?
  - quote: "Once you edit or remove all rejected items, click Resubmit to App Review from the submission details page."
  - surface: asc
  - verify: App Review page > In Progress > Resolve: no rejected items remain un-edited.
  - fix: Edit (once) or remove each rejected item, then Resubmit to App Review.

## SUBMIT.REMOVE Remove a submission from review

**Source text (verbatim):**
> You can remove an app from the review and release process if the app is in one of the following states:
> - Waiting for Export Compliance
> - Waiting for Review
> - In Review
> - Pending Developer Release
> - Pending Apple Release
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
> Remove an app from the review and release process
> In Apps, select the app you want to view.
> In the sidebar, click the app version that you want to remove a build for.
> In the message that appears at the top, click “remove this version from review.”
> In the dialog that appears, click Remove.
> The app, and any other items in the submission, are removed from the queue and the app status changes to Developer Rejected. If you resubmit the review process will start over.
> Cancel a submission
> In Apps, select the app you want to view.
> In the sidebar, click App Review.
> Under Submissions, click the submission you want to remove.
> At the bottom of the page, click Cancel Submission.
> Click Confirm.
> Your submission will be cancelled, and any items marked as Accepted must be resubmitted. If the submission includes an app version, its status will change to Developer Rejected. If you resubmit, the review process will start over.

**Applies to:** Informational — procedure for withdrawing a submission

**Status:** Informational procedure — no pass/fail checks (used as the fix path for SUBMIT-01).

## SUBMIT.APPOINTMENT Request a one-on-one App Review appointment

**Source text (verbatim):**
> If you have questions about the review process, you can request to meet with App Review over Webex. In each 30-minute video appointment, you can ask for advice on what to expect during review, how your app can best align with guidelines, reasons for common rejections, and topics related to the process of reviewing your app for distribution.
> How to request an App Review appointment
> Request an appointment on the Meet with Apple schedule page. Appointments are subject to availability during your local business hours on Tuesdays and Thursdays.
> In your request, include your app's Apple ID from App Store Connect (if you have one) and the specific questions you'd like to discuss.
> Discuss your app with an App Review expert during the appointment. Appointments are conducted on video over Webex; having your camera on is optional.
> Note: A Meet with Apple appointment is informational. It doesn't replace, expedite, or guarantee the outcome of your app's review.
> Tips about appointment requests
> Do
> - Request an appointment if you're unsure how a specific guideline applies to your app, or want general guidance on how to prepare an app for review.
> - Come with specific questions so App Review can provide useful feedback in the time available.
> - Keep in mind every submission is evaluated against the App Review Guidelines at the time of review, so App Review cannot preapprove apps or specific features during your appointment.
>
> Don't
> - Don't consider an App Review appointment a replacement for reading the App Review Guidelines yourself.

**Applies to:** Informational — optional service

**Status:** Informational — no pass/fail checks. The skill may suggest an appointment when a check result is "manual" and the developer is unsure how a guideline applies.

## SUBMIT.CONTACT App Review page — Contacting us (Suggestions, Report a concern, Other questions)

**Source text (verbatim):**
> App Review submissions
> You can view your past and current submissions to App Review in App Store Connect. If your submission didn’t pass review, details are provided, including any specific App Review Guidelines that your submission didn’t follow. You can correspond with App Review to resolve the issues before resubmitting the build. Access the App Review section on the app’s page in App Store Connect.
> Suggestions
> Help improve the App Review Guidelines or identify a need for clarity in our policies by suggesting guideline changes. Your suggestions will be taken into consideration by App Review.
> Report a concern
> If you believe that an app presents a trust or safety concern, or is in violation of the App Review Guidelines, you can share details with us to investigate.
> Other questions
> You can contact us to ask for support with an unresolved app rejection or removal.

**Applies to:** Informational

**Status:** Informational — no pass/fail checks.

---

## Sources
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-for-review — redirects to "Overview of submitting for review - Manage submissions to App Review - App Store Connect - Help - Apple Developer" (https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review)
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app — "Submit an app"
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/reply-to-app-review-messages — "Reply to App Review messages"
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/remove-a-submission-from-review — "Remove a submission from review"
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/manage-a-submission-with-unresolved-issues — "Manage a submission with unresolved issues"
- https://developer.apple.com/help/app-store-connect/manage-builds/choose-a-build-to-submit — "Choose a build to submit"
- https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds — "Upload builds"
- https://developer.apple.com/help/app-store-connect/reference/app-uploads/maximum-build-file-sizes — "Maximum build file sizes"
- https://developer.apple.com/help/app-store-connect/reference/age-ratings-values-and-definitions — redirects to "Age ratings values and definitions" (https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions)
- https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating — "Set an app age rating"
- https://developer.apple.com/help/app-store-connect/reference/app-information/app-information — "App information"
- https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information — "Platform version information" (App Review information section)
- https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements — "Manage European Union Digital Services Act trader requirements"
- https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance — "Overview of export compliance"
- https://developer.apple.com/help/app-store-connect/manage-app-information/determine-and-upload-app-encryption-documentation — "Determine and upload app encryption documentation"
- https://developer.apple.com/help/app-store-connect/reference/app-information/export-compliance-documentation-for-encryption — "Export compliance documentation for encryption"
- https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-export-compliance-information-for-beta-builds — "Provide export compliance information for beta builds"
- https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations — "Complying with Encryption Export Regulations" (read via its DocC JSON at https://developer.apple.com/tutorials/data/documentation/security/complying-with-encryption-export-regulations.json)
- https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption — "ITSAppUsesNonExemptEncryption" (DocC JSON)
- https://developer.apple.com/documentation/bundleresources/information-property-list/itsencryptionexportcompliancecode — "ITSEncryptionExportComplianceCode" (DocC JSON)
- https://developer.apple.com/news/upcoming-requirements/ — "Upcoming Requirements - Apple Developer"
- https://developer.apple.com/app-store/review/ — redirects to https://developer.apple.com/distribute/app-review/
- https://developer.apple.com/distribute/app-review/ — "App Review"
- https://developer.apple.com/app-store/submitting/ — "Submit your apps and games today"
- https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review — "Provide information for a complete review"
- https://developer.apple.com/help/app-review/before-submitting-for-review/app-review-appointment — "Request a one-on-one App Review appointment"
- https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review — "Request an expedited review"
- https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board — "Appeal to the App Review Board"
- https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review — "Contact App Review for help with a submission"
- https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions — "Accept Bug Fix Submission offers"
- https://developer.apple.com/help/app-review/after-submitting-for-review/review-status — "Track a submission’s review status"
