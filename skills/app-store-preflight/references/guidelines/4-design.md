# App Review Guidelines — 4. Design
Source: https://developer.apple.com/app-store/review/guidelines/#design  
Retrieved: 2026-10-30

## 4 Design

**Source text (verbatim):**
> Apple customers place a high value on products that are simple, refined, innovative, and easy to use, and that’s what we want to see on the App Store. Coming up with a great design is up to you, but the following are minimum standards for approval to the App Store. And remember that even after your app has been approved, you should update your app to ensure it remains functional and engaging to new and existing customers. Apps that stop working or offer a degraded experience may be removed from the App Store at any time.

**Applies to:** All apps

- **[4-01]** Does every core flow of the app work (no broken features, dead screens or failing network calls) on the current OS version?
  - quote: "Apps that stop working or offer a degraded experience may be removed from the App Store at any time."
  - surface: runtime
  - verify: Build and run on the latest iOS/iPadOS simulator and device; exercise every tab, screen and primary action; watch the console for crashes, unhandled errors and failed requests; confirm deprecated-API warnings in the Xcode build log are not breaking features.
  - fix: Fix crashes/broken flows; remove or repair features that no longer work; update for current SDK.
- **[4-02]** (Advisory — Apple says "should") Is the app being kept updated so it remains functional and engaging for new and existing customers?
  - quote: "you should update your app to ensure it remains functional and engaging to new and existing customers"
  - surface: manual
  - verify: Check in App Store Connect (App Store > version history) the date of the last release; ask the developer whether there is an update cadence.
  - fix: manual — requires developer decision/legal/business action

## 4.1 Copycats

**Source text (verbatim):**
> - (a) Come up with your own ideas. We know you have them, so make yours come to life. Don’t simply copy the latest popular app on the App Store, or make some minor changes to another app’s name or UI and pass it off as your own. In addition to risking an intellectual property infringement claim, it makes the App Store harder to navigate and just isn’t fair to your fellow developers.
> - (b) Submitting apps which impersonate other apps or services is considered a violation of the Developer Code of Conduct and may result in removal from the Apple Developer Program.
> - (c) You cannot use another developer’s icon, brand, or product name in your app’s icon or name, without approval from the developer.
>
> Learn more about preventing copycat and impersonation rejections.

**Applies to:** All apps

**Related:** Developer Code of Conduct; "Learn more about preventing copycat and impersonation rejections"

- **[4.1-01]** Is the app an original concept rather than a copy of a popular App Store app?
  - quote: "Don’t simply copy the latest popular app on the App Store"
  - surface: manual
  - verify: Describe the app's core concept; search the App Store for the app's category/top apps and compare feature set and flows; developer attests originality.
  - fix: manual — requires developer decision/legal/business action (differentiate concept/features)
- **[4.1-02]** Are the app's name and UI distinct from another app's (not a minor variation of another app's name or UI)?
  - quote: "make some minor changes to another app’s name or UI and pass it off as your own"
  - surface: asc
  - verify: App Store Connect > App Information > Name and Subtitle; App Store > version > screenshots. Search the App Store for similarly named apps; compare the app's main screens (runtime screenshots) with leading competitor UIs.
  - fix: Rename the app and/or redesign UI elements that mirror another app's; update name/subtitle/screenshots in App Store Connect.
- **[4.1-03]** Does the app avoid impersonating other apps or services?
  - quote: "Submitting apps which impersonate other apps or services is considered a violation of the Developer Code of Conduct"
  - surface: asc
  - verify: Review App Store Connect name, subtitle, description, icon, screenshots, and in-app branding (Assets.xcassets, launch screen, strings) for claims or visuals suggesting it is, or is affiliated with, another app/service.
  - fix: Remove impersonating branding/claims from the binary and metadata.
- **[4.1-04]** Are the app icon and app name free of another developer’s icon, brand, or product name (or has approval been obtained from that developer)?
  - quote: "You cannot use another developer’s icon, brand, or product name in your app’s icon or name, without approval from the developer."
  - surface: code
  - verify: Inspect AppIcon in Assets.xcassets (and alternate icons via CFBundleAlternateIcons in Info.plist) and CFBundleDisplayName/CFBundleName; check App Store Connect > App Information > Name. Look for third-party logos/trademarks; if present, ask for evidence of approval from that developer.
  - fix: Replace the icon/name with original assets, or obtain approval from the developer who owns it (manual).

## 4.2 Minimum Functionality

**Source text (verbatim):**
> Your app should include features, content, and UI that elevate it beyond a repackaged website. If your app is not particularly useful, unique, or “app-like,” it doesn’t belong on the App Store. If your App doesn’t provide some sort of lasting entertainment value or adequate utility, it may not be accepted. Apps that are simply a song or movie should be submitted to the iTunes Store. Apps that are simply a book or game guide should be submitted to the Apple Books Store.

**Applies to:** All apps

- **[4.2-01]** Does the app include features, content and UI beyond a repackaged website (not just a WKWebView wrapping a site)?
  - quote: "Your app should include features, content, and UI that elevate it beyond a repackaged website."
  - surface: code
  - verify: grep for `WKWebView`, `SFSafariViewController`, `UIWebView`, `WebView(` and count screens built natively vs. web views; check whether the root view controller/SwiftUI root loads a remote URL; run the app and see whether native features exist (offline behavior, native navigation, device integration).
  - fix: Add native features/UI that provide functionality beyond the website; replace web-wrapper screens with native screens.
- **[4.2-02]** Is the app useful, unique, or “app-like”?
  - quote: "If your app is not particularly useful, unique, or “app-like,” it doesn’t belong on the App Store."
  - surface: runtime
  - verify: Run the app end-to-end and list the distinct user-facing features; note whether they use native interaction patterns.
  - fix: manual — requires developer decision/legal/business action (expand functionality)
- **[4.2-03]** Does the app provide lasting entertainment value or adequate utility?
  - quote: "If your App doesn’t provide some sort of lasting entertainment value or adequate utility, it may not be accepted."
  - surface: manual
  - verify: Assess the amount of content/features available after first use (e.g., does the app have only one screen or single-use content?); developer attests.
  - fix: manual — requires developer decision/legal/business action
- **[4.2-04]** Is the app more than simply a song or movie?
  - quote: "Apps that are simply a song or movie should be submitted to the iTunes Store."
  - surface: code
  - verify: Inspect bundled resources (`.mp3`, `.m4a`, `.mp4`, `.mov`) and app structure; if the app's sole purpose is playing one song/movie (AVPlayer on a single asset), it fails.
  - fix: manual — submit the content to the iTunes Store instead, or build substantial app functionality.
- **[4.2-05]** Is the app more than simply a book or game guide?
  - quote: "Apps that are simply a book or game guide should be submitted to the Apple Books Store."
  - surface: code
  - verify: Inspect bundled resources (`.epub`, `.pdf`, large text/HTML bundles) and screens; if the app is only paginated reading content for a book or game guide, it fails.
  - fix: manual — submit to Apple Books, or build substantial app functionality.

## 4.2.1 ARKit apps

**Source text (verbatim):**
> 4.2.1 Apps using ARKit should provide rich and integrated augmented reality experiences; merely dropping a model into an AR view or replaying animation is not enough.

**Applies to:** Apps using ARKit
**Requires:** arkit

- **[4.2.1-01]** Does the ARKit experience go beyond merely dropping a model into an AR view or replaying an animation?
  - quote: "merely dropping a model into an AR view or replaying animation is not enough"
  - surface: code
  - verify: grep for `import ARKit`, `ARSession`, `ARView`, `ARSCNView`, `RealityKit`, `.usdz`/`.reality` assets; inspect what interaction exists beyond placing an entity (e.g., interaction, scene understanding, gameplay); run the AR flow on device.
  - fix: Build a richer, integrated AR experience, or remove the AR feature.
- **[4.2.1-02]** Is the AR experience rich and integrated into the app?
  - quote: "Apps using ARKit should provide rich and integrated augmented reality experiences"
  - surface: runtime
  - verify: Run AR flows on a physical device; confirm AR is integrated into the app's purpose rather than a standalone novelty.
  - fix: Integrate AR more deeply into the app's functionality (developer decision).

## 4.2.2 Not primarily marketing, ads, web clippings, aggregators, or links

**Source text (verbatim):**
> 4.2.2 Other than catalogs, apps shouldn’t primarily be marketing materials, advertisements, web clippings, content aggregators, or a collection of links.

**Applies to:** All apps (catalogs excepted)

- **[4.2.2-01]** Is the app (unless it is a catalog) something other than primarily marketing materials, advertisements, web clippings, content aggregators, or a collection of links?
  - quote: "apps shouldn’t primarily be marketing materials, advertisements, web clippings, content aggregators, or a collection of links"
  - surface: code
  - verify: Inspect main screens: are they mostly lists of external links (`UIApplication.shared.open`, `Link(`, `openURL`, `SFSafariViewController`), RSS/feed aggregation without original functionality, or promotional content? Run the app to confirm.
  - fix: Add genuine functionality; remove link-list/aggregator-only design.

## 4.2.3 Standalone functionality and initial downloads

**Source text (verbatim):**
> - (i) Your app should work on its own without requiring installation of another app to function.
> - (ii) If your app needs to download additional resources in order to function on initial launch, disclose the size of the download and prompt users before doing so.

**Applies to:** (i) All apps; (ii) apps that download additional resources to function on initial launch

- **[4.2.3-01]** Does the app work on its own without requiring installation of another app?
  - quote: "Your app should work on its own without requiring installation of another app to function."
  - surface: runtime
  - verify: Fresh-install on a clean simulator with no companion apps; grep for `canOpenURL`, `LSApplicationQueriesSchemes` in Info.plist and for gating logic that blocks use when another app is absent; run all core flows.
  - fix: Remove the dependency or provide full functionality without the other app.
- **[4.2.3-02]** If the app downloads additional resources needed on initial launch, does it disclose the download size?
  - quote: "disclose the size of the download"
  - surface: code
  - verify: grep for `NSBundleResourceRequest` (On-Demand Resources), `BackgroundAssets`/`BADownloadManager`, `URLSession` downloads in first-launch/onboarding code; inspect the UI shown before the download for a size figure.
  - fix: Show the download size (e.g., "Download 450 MB?") before starting.
- **[4.2.3-03]** Does the app prompt users before downloading those resources?
  - quote: "prompt users before doing so"
  - surface: runtime
  - verify: Fresh-install and launch; confirm a prompt appears and no large download begins before user confirmation (monitor network).
  - fix: Add a confirmation prompt gating the initial download.

## 4.2.4 Intentionally omitted

**Source text (verbatim):**
> 4.2.4 Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 4.2.5 Intentionally omitted

**Source text (verbatim):**
> 4.2.5 Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 4.2.6 Template and app generation services

**Source text (verbatim):**
> 4.2.6 Apps created from a commercialized template or app generation service will be rejected unless they are submitted directly by the provider of the app’s content. These services should not submit apps on behalf of their clients and should offer tools that let their clients create customized, innovative apps that provide unique customer experiences. Another acceptable option for template providers is to create a single binary to host all client content in an aggregated or “picker” model, for example as a restaurant finder app with separate customized entries or pages for each client restaurant, or as an event app with separate entries for each client event.

**Applies to:** Apps created from a commercialized template or app generation service

- **[4.2.6-01]** If the app was created from a commercialized template or app generation service, is it submitted directly by the provider of the app’s content?
  - quote: "will be rejected unless they are submitted directly by the provider of the app’s content"
  - surface: asc
  - verify: Inspect the project for template/app-builder fingerprints (generator-named frameworks, config files, bundle ID prefixes, boilerplate); compare App Store Connect > Users and Access / account holder and App Information > seller name with the content owner.
  - fix: manual — the content provider must submit under their own developer account.
- **[4.2.6-02]** If you are a template/app generation service, are you refraining from submitting apps on behalf of clients (or using a single aggregated “picker” binary)?
  - quote: "These services should not submit apps on behalf of their clients"
  - surface: manual
  - verify: Developer attests whether the account submits apps for third-party clients; check App Store Connect > Apps for many near-identical apps.
  - fix: manual — consolidate client content into one binary with a “picker” model, or have clients submit their own apps.

## 4.2.7 Remote Desktop Clients

**Source text (verbatim):**
> 4.2.7 Remote Desktop Clients: If your remote desktop app acts as a mirror of specific software or services rather than a generic mirror of the host device, it must comply with the following:
> - (a) The app must only connect to a user-owned host device that is a personal computer or dedicated game console owned by the user, and both the host device and client must be connected on a local and LAN-based network.
> - (b) Any software or services appearing in the client are fully executed on the host device, rendered on the screen of the host device, and may not use APIs or platform features beyond what is required to stream the Remote Desktop.
> - (c) All account creation and management must be initiated from the host device.
> - (d) The UI appearing on the client does not resemble an iOS or App Store view, does not provide a store-like interface, or include the ability to browse, select, or purchase software not already owned or licensed by the user. For the sake of clarity, transactions taking place within mirrored software do not need to use in-app purchase, provided the transactions are processed on the host device.
> - (e) Thin clients for cloud-based apps are not appropriate for the App Store.

**Applies to:** Remote desktop apps that mirror specific software or services rather than a generic mirror of the host device ((e) applies to thin clients for cloud-based apps)
**Requires:** remote-desktop-streaming, webview

- **[4.2.7-01]** Does the app only connect to a user-owned personal computer or dedicated game console?
  - quote: "The app must only connect to a user-owned host device that is a personal computer or dedicated game console owned by the user"
  - surface: code
  - verify: Inspect connection/pairing code (`Network.framework` `NWConnection`, `NWBrowser`, Bonjour `NSBonjourServices`) for connections to remote/cloud hosts vs. user-paired devices.
  - fix: Restrict connections to user-paired PCs/consoles.
- **[4.2.7-02]** Are both host and client required to be on a local, LAN-based network?
  - quote: "both the host device and client must be connected on a local and LAN-based network"
  - surface: code
  - verify: Check for `NSLocalNetworkUsageDescription`, `NSBonjourServices`, local discovery; grep for relay/WAN/cloud endpoints or remote-access tunneling; test that connection fails off-LAN.
  - fix: Remove WAN/cloud relay connectivity; require local network.
- **[4.2.7-03]** Is all software/services shown in the client fully executed and rendered on the host device?
  - quote: "Any software or services appearing in the client are fully executed on the host device, rendered on the screen of the host device"
  - surface: code
  - verify: Confirm the client only decodes a video stream and forwards input; grep for locally executed content (WebKit/JavaScriptCore execution of mirrored apps, local game engines).
  - fix: Move execution to the host; client only streams.
- **[4.2.7-04]** Does the client avoid using APIs or platform features beyond what is required to stream?
  - quote: "may not use APIs or platform features beyond what is required to stream the Remote Desktop"
  - surface: code
  - verify: Review entitlements and Info.plist usage descriptions, linked frameworks (Build Phases > Link Binary) for capabilities unrelated to streaming (e.g., HealthKit, Contacts, location).
  - fix: Remove unneeded capabilities/frameworks.
- **[4.2.7-05]** Is all account creation and management initiated from the host device (not the client)?
  - quote: "All account creation and management must be initiated from the host device."
  - surface: runtime
  - verify: Run the client; check for sign-up, account-management or settings-of-account screens in the client; grep for registration endpoints.
  - fix: Remove account creation/management from the client; direct users to the host.
- **[4.2.7-06]** Does the client UI avoid resembling an iOS or App Store view and avoid a store-like interface?
  - quote: "The UI appearing on the client does not resemble an iOS or App Store view, does not provide a store-like interface"
  - surface: runtime
  - verify: Run the client and screenshot all screens; compare to iOS home screen/App Store layouts; look for catalog/storefront UI.
  - fix: Redesign the client UI to avoid iOS/App Store resemblance and storefront layouts.
- **[4.2.7-07]** Does the client avoid the ability to browse, select, or purchase software not already owned or licensed by the user?
  - quote: "include the ability to browse, select, or purchase software not already owned or licensed by the user"
  - surface: runtime
  - verify: Run the client; check whether unowned titles can be browsed/selected/bought; grep for store/catalog APIs.
  - fix: Limit the client to software the user already owns/licenses.
- **[4.2.7-08]** Are any transactions within mirrored software processed on the host device (if not using in-app purchase)?
  - quote: "transactions taking place within mirrored software do not need to use in-app purchase, provided the transactions are processed on the host device"
  - surface: code
  - verify: grep the client for payment SDKs/endpoints (Stripe, PayPal, web checkout URLs) processed on the client rather than the host.
  - fix: Ensure non-IAP transactions occur only on the host.
- **[4.2.7-09]** Is the app something other than a thin client for a cloud-based app?
  - quote: "Thin clients for cloud-based apps are not appropriate for the App Store."
  - surface: code
  - verify: Check whether the app's main content is streamed from cloud servers (remote streaming endpoints) rather than a user-owned host.
  - fix: manual — requires developer decision/legal/business action

## 4.3 Spam

**Source text (verbatim):**
> - (a) Don’t create multiple Bundle IDs of the same app (for example, submitting a separate map app for every city in the world instead of a single worldwide map that allows users to search any city). This practice results in unnecessary apps, which makes it hard for users to find the apps they want. If your app has different versions for specific locations, sports teams, universities, etc., consider submitting a single app and providing the variations using in-app purchase.
> - (b) Don’t submit apps that are indistinguishable from what's already widely available. Opportunistically creating variants of existing app categories or popular apps degrades App Store discovery, reduces overall app quality, and harms both users and developers. Certain kinds of apps, such as dating, flashlight, sound effects, wallpaper, simple timers, and fortune telling, are well established on the App Store and we will not accept new submissions unless they offer a meaningfully different or improved experience. We may remove these apps from the App Store going forward if they are not updated, improved, or do not attract customers. Other kinds of apps, such as drinking games, Kama Sutra, fart, and burp apps, are mediocre, low-quality, or low-effort and do not add value to the App Store. Repeated submissions of this kind may lead to removal from the Apple Developer Program.

**Applies to:** All apps

- **[4.3-01]** Is this app not one of multiple Bundle IDs of the same app?
  - quote: "Don’t create multiple Bundle IDs of the same app"
  - surface: asc
  - verify: App Store Connect > Apps: list the account's apps and look for near-identical apps differing by location/team/university/etc.; in the project, check for multiple targets/schemes with different `PRODUCT_BUNDLE_IDENTIFIER` but the same code (white-label targets).
  - fix: Consolidate into a single app; provide variations in-app (optionally via in-app purchase).
- **[4.3-02]** Is the app distinguishable from what's already widely available?
  - quote: "Don’t submit apps that are indistinguishable from what's already widely available."
  - surface: manual
  - verify: Search the App Store for the app's category and keywords; list the app's differentiating features.
  - fix: manual — requires developer decision/legal/business action
- **[4.3-03]** If the app is a dating, flashlight, sound effects, wallpaper, simple timer, or fortune telling app, does it offer a meaningfully different or improved experience?
  - quote: "we will not accept new submissions unless they offer a meaningfully different or improved experience"
  - surface: asc
  - verify: Check App Store Connect > App Information > Primary/Secondary Category, name, description and keywords for these app types; if matched, document the meaningful differentiation.
  - fix: manual — add meaningful differentiation or reconsider submission.
- **[4.3-04]** Is the app not a drinking game, Kama Sutra, fart, or burp app?
  - quote: "Other kinds of apps, such as drinking games, Kama Sutra, fart, and burp apps, are mediocre, low-quality, or low-effort and do not add value to the App Store."
  - surface: asc
  - verify: Check App Store Connect name, subtitle, description, keywords and in-app content for these app types.
  - fix: manual — do not submit this kind of app.

## 4.4 Extensions

**Source text (verbatim):**
> Apps hosting or containing extensions must comply with the App Extension Programming Guide, the Safari app extensions documentation, or the Safari web extensions documentation and should include some functionality, such as help screens and settings interfaces where possible. You should clearly and accurately disclose what extensions are made available in the app’s marketing text, and the extensions may not include marketing, advertising, or in-app purchases.

**Applies to:** Apps hosting or containing extensions
**Requires:** extensions-widgets, keyboard

**Related:** App Extension Programming Guide; Safari app extensions documentation; Safari web extensions documentation

- **[4.4-01]** Do the extensions comply with the App Extension Programming Guide / Safari app or web extensions documentation?
  - quote: "must comply with the App Extension Programming Guide, the Safari app extensions documentation, or the Safari web extensions documentation"
  - surface: code
  - verify: List extension targets (`.appex`, `NSExtension` / `NSExtensionPointIdentifier` in each extension's Info.plist, `EXAppExtensionAttributes`); confirm each uses a supported extension point and builds without warnings; validate Safari web extensions' `manifest.json`.
  - fix: Correct extension configuration per Apple's extension documentation.
- **[4.4-02]** Does the containing app include some functionality, such as help screens and settings interfaces, where possible?
  - quote: "should include some functionality, such as help screens and settings interfaces where possible"
  - surface: runtime
  - verify: Run the containing app; confirm it is not an empty shell (has help/setup instructions and settings for the extension).
  - fix: Add help/setup screens and settings to the containing app.
- **[4.4-03]** Does the app’s marketing text clearly and accurately disclose which extensions are available?
  - quote: "You should clearly and accurately disclose what extensions are made available in the app’s marketing text"
  - surface: asc
  - verify: Compare extension targets in the project with App Store Connect > App Store > version > Description (and Promotional Text); each extension should be mentioned accurately.
  - fix: Update the App Store description to list each extension accurately.
- **[4.4-04]** Are the extensions free of marketing, advertising, and in-app purchases?
  - quote: "the extensions may not include marketing, advertising, or in-app purchases"
  - surface: code
  - verify: In extension targets' sources and linked frameworks, grep for ad SDKs (`GADMobileAds`, `GoogleMobileAds`, `AppLovin`, `FBAudienceNetwork`, etc.), `StoreKit` (`Product.purchase`, `SKPaymentQueue`), and promotional UI/strings.
  - fix: Remove ads, marketing and IAP from extension targets.

## 4.4.1 Keyboard extensions

**Source text (verbatim):**
> 4.4.1 Keyboard extensions have some additional rules.
>
> They must:
> - Provide keyboard input functionality (such as typed characters);
> - Follow Sticker guidelines if the keyboard includes images or emoji;
> - Provide a method for progressing to the next keyboard;
> - Remain functional without full network access and without requiring full access;
> - Collect user activity only to enhance the functionality of the user’s keyboard extension on the iOS device.
>
> They must not:
> - Launch other apps besides Settings; or
> - Repurpose keyboard buttons for other behaviors (such as holding down the “return” key to launch the camera).

**Applies to:** Apps with keyboard extensions (`com.apple.keyboard-service`)
**Requires:** keyboard, extensions-widgets

- **[4.4.1-01]** Does the keyboard provide keyboard input functionality (such as typed characters)?
  - quote: "Provide keyboard input functionality (such as typed characters);"
  - surface: code
  - verify: Find the `UIInputViewController` subclass in the extension with `NSExtensionPointIdentifier` = `com.apple.keyboard-service`; confirm it calls `textDocumentProxy.insertText(...)`.
  - fix: Implement text input via `textDocumentProxy`.
- **[4.4.1-02]** If the keyboard includes images or emoji, does it follow Sticker guidelines?
  - quote: "Follow Sticker guidelines if the keyboard includes images or emoji;"
  - surface: manual
  - verify: Check keyboard assets for images/emoji; review them against Apple's sticker guidelines.
  - fix: Bring image/emoji content in line with Sticker guidelines.
- **[4.4.1-03]** Does the keyboard provide a method for progressing to the next keyboard?
  - quote: "Provide a method for progressing to the next keyboard;"
  - surface: code
  - verify: grep the keyboard extension for `advanceToNextInputMode()` or `handleInputModeList(from:with:)`, and check `needsInputModeSwitchKey` handling; confirm a globe/next-keyboard key exists at runtime.
  - fix: Add a next-keyboard key wired to `handleInputModeList(from:with:)` / `advanceToNextInputMode()`.
- **[4.4.1-04]** Does the keyboard remain functional without full network access and without requiring full access?
  - quote: "Remain functional without full network access and without requiring full access;"
  - surface: runtime
  - verify: Check `RequestsOpenAccess` in the extension's Info.plist `NSExtensionAttributes`; run with Full Access off and network disabled and confirm typing works; grep for `hasFullAccess` gating that blocks input.
  - fix: Make core typing work without Full Access and offline; degrade gracefully.
- **[4.4.1-05]** Is user activity collected only to enhance the keyboard extension’s functionality on the device?
  - quote: "Collect user activity only to enhance the functionality of the user’s keyboard extension on the iOS device."
  - surface: code
  - verify: grep the keyboard extension for analytics/network calls (`URLSession`, analytics SDKs) and logging of typed text; check App Privacy answers in App Store Connect.
  - fix: Remove collection of keystrokes/activity for purposes other than enhancing the keyboard.
- **[4.4.1-06]** Does the keyboard avoid launching other apps besides Settings?
  - quote: "Launch other apps besides Settings; or"
  - surface: code
  - verify: grep the extension for `openURL`, `extensionContext?.open`, responder-chain `openURL:` hacks, and custom URL schemes other than `UIApplication.openSettingsURLString`.
  - fix: Remove app-launching code except opening Settings.
- **[4.4.1-07]** Are keyboard buttons free of repurposed behaviors (e.g., holding “return” to launch the camera)?
  - quote: "Repurpose keyboard buttons for other behaviors (such as holding down the “return” key to launch the camera)."
  - surface: code
  - verify: Inspect gesture recognizers (`UILongPressGestureRecognizer`) and key handlers in the keyboard for actions unrelated to input.
  - fix: Remove non-input behaviors from keyboard keys.

## 4.4.2 Safari extensions

**Source text (verbatim):**
> 4.4.2 Safari extensions must run on the current version of Safari on the relevant Apple operating system. They may not interfere with System or Safari UI elements and must never include malicious or misleading content or code. Violating this rule will lead to removal from the Apple Developer Program. Safari extensions should not claim access to more websites than strictly necessary to function.

**Applies to:** Apps containing Safari extensions
**Requires:** extensions-widgets, macos

- **[4.4.2-01]** Does the Safari extension run on the current version of Safari on the relevant OS?
  - quote: "Safari extensions must run on the current version of Safari on the relevant Apple operating system."
  - surface: runtime
  - verify: Install on the latest iOS/macOS simulator/device; enable the extension in Safari settings; exercise its features; check for deprecated `manifest.json` keys/APIs.
  - fix: Update the extension for the current Safari version.
- **[4.4.2-02]** Does the extension avoid interfering with System or Safari UI elements?
  - quote: "They may not interfere with System or Safari UI elements"
  - surface: runtime
  - verify: Run the extension and check it does not hide/override Safari toolbar, tabs, address bar or system UI; review content scripts for overlays mimicking Safari UI.
  - fix: Remove UI interference.
- **[4.4.2-03]** Is the extension free of malicious or misleading content or code?
  - quote: "must never include malicious or misleading content or code"
  - surface: code
  - verify: Review all extension JS (content scripts, background scripts) for obfuscated code, remote code loading (`eval`, remote script injection), data exfiltration, and misleading UI text.
  - fix: Remove malicious/misleading code or content.
- **[4.4.2-04]** Does the extension claim access only to the websites strictly necessary to function?
  - quote: "Safari extensions should not claim access to more websites than strictly necessary to function"
  - surface: code
  - verify: Inspect `manifest.json` `permissions`, `host_permissions`, `content_scripts.matches` for `<all_urls>`, `*://*/*`; for Safari app extensions check `SFSafariWebsiteAccess` / `Allowed Domains` in Info.plist.
  - fix: Narrow host permissions/allowed domains to only those required.

## 4.4.3 Intentionally omitted

**Source text (verbatim):**
> 4.4.3 Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 4.5 Apple Sites and Services

**Source text (verbatim):**
> 4.5 Apple Sites and Services

**Applies to:** Apps using Apple sites and services (see 4.5.1–4.5.6)

Heading only; requirements are in 4.5.1–4.5.6 — no checks at this level.

## 4.5.1 Apple sites and RSS feeds

**Source text (verbatim):**
> 4.5.1 Apps may use approved Apple RSS feeds such as the iTunes Store RSS feed, but may not scrape any information from Apple sites (such as apple.com, the iTunes Store, App Store, App Store Connect, developer portal, etc.) or create rankings using this information.

**Applies to:** Apps that use information from Apple sites

**Related:** iTunes Store RSS feed

- **[4.5.1-01]** Does the app avoid scraping information from Apple sites (apple.com, iTunes Store, App Store, App Store Connect, developer portal, etc.)?
  - quote: "may not scrape any information from Apple sites (such as apple.com, the iTunes Store, App Store, App Store Connect, developer portal, etc.)"
  - surface: code
  - verify: grep sources and server config for `apple.com`, `apps.apple.com`, `itunes.apple.com`, `appstoreconnect.apple.com`, `developer.apple.com` URLs with HTML parsing (SwiftSoup, regex on HTML); confirm only approved RSS feeds are used.
  - fix: Replace scraping with approved Apple RSS feeds or remove the feature.
- **[4.5.1-02]** Does the app avoid creating rankings using information scraped from Apple sites?
  - quote: "or create rankings using this information"
  - surface: code
  - verify: Look for ranking/chart features built from Apple-site data.
  - fix: Remove rankings derived from scraped Apple data.

## 4.5.2 Apple Music

**Source text (verbatim):**
> - (i) MusicKit on iOS lets users play Apple Music and their local music library natively from your apps and games. When a user provides permission to their Apple Music account, your app can create playlists, add songs to their library, and play any of the millions of songs in the Apple Music catalog. Users must initiate the playback of an Apple Music stream and be able to navigate using standard media controls such as “play,” “pause,” and “skip.” Moreover, your app may not require payment or indirectly monetize access to the Apple Music service (such as in-app purchase, advertising, requesting user info, etc.). Do not download, upload, or enable sharing of music files sourced from the MusicKit APIs, except as explicitly permitted in MusicKit documentation.
> - (ii) Using the MusicKit APIs is not a replacement for securing the licenses you might need for a deeper or more complex music integration. For example, if you want your app to play a specific song at a particular moment, or to create audio or video files that can be shared to social media, you’ll need to contact rights-holders directly to get their permission (such as synchronization or adaptation rights) and assets. Cover art and other metadata may only be used in connection with music playback or playlists (including screenshots displaying your app’s functionality), and should not be used in any marketing or advertising without getting specific authorization from rights-holders. Make sure to follow the Apple Music Identity Guidelines when integrating Apple Music services in your app.
> - (iii) Apps that access Apple Music user data, such as playlists and favorites, must clearly disclose this access in the purpose string. Any data collected may not be shared with third parties for any purpose other than supporting or improving the app experience. This data may not be used to identify users or devices, or to target advertising.

**Applies to:** Apps using MusicKit / Apple Music

**Related:** MusicKit documentation; Apple Music Identity Guidelines

- **[4.5.2-01]** Is Apple Music playback initiated by the user (no autoplay)?
  - quote: "Users must initiate the playback of an Apple Music stream"
  - surface: code
  - verify: grep for `import MusicKit`, `ApplicationMusicPlayer`, `SystemMusicPlayer`, `MPMusicPlayerController`, `.play()`; confirm play calls originate from user actions, not `onAppear`/launch.
  - fix: Start playback only from explicit user actions.
- **[4.5.2-02]** Can users navigate playback with standard media controls such as “play,” “pause,” and “skip”?
  - quote: "be able to navigate using standard media controls such as “play,” “pause,” and “skip.”"
  - surface: runtime
  - verify: Run playback; confirm in-app play/pause/skip controls and that Control Center/lock screen controls work (`MPRemoteCommandCenter` if applicable).
  - fix: Add standard play/pause/skip controls.
- **[4.5.2-03]** Does the app avoid requiring payment for, or indirectly monetizing, access to Apple Music (IAP, ads, requesting user info, etc.)?
  - quote: "your app may not require payment or indirectly monetize access to the Apple Music service (such as in-app purchase, advertising, requesting user info, etc.)"
  - surface: code
  - verify: Check whether Apple Music features are behind a paywall/`StoreKit` entitlement check, ad gates (rewarded ads), or a sign-up/info form.
  - fix: Remove paywalls, ad gates or info requests from Apple Music access.
- **[4.5.2-04]** Does the app avoid downloading, uploading, or enabling sharing of music files sourced from MusicKit (except as permitted by MusicKit documentation)?
  - quote: "Do not download, upload, or enable sharing of music files sourced from the MusicKit APIs, except as explicitly permitted in MusicKit documentation."
  - surface: code
  - verify: grep for code that writes/uploads/shares audio derived from MusicKit items (`AVAssetExportSession`, `UIActivityViewController` with audio files, upload calls).
  - fix: Remove download/upload/sharing of MusicKit-sourced music files.
- **[4.5.2-05]** For deeper music integration (specific song at a particular moment, shareable audio/video files), have licenses been secured from rights-holders?
  - quote: "you’ll need to contact rights-holders directly to get their permission (such as synchronization or adaptation rights) and assets"
  - surface: manual
  - verify: Identify features that sync specific songs to moments or export shareable audio/video; ask developer for license documentation.
  - fix: manual — requires developer decision/legal/business action
- **[4.5.2-06]** Is cover art and other metadata used only in connection with music playback or playlists?
  - quote: "Cover art and other metadata may only be used in connection with music playback or playlists (including screenshots displaying your app’s functionality)"
  - surface: code
  - verify: grep for `Artwork`, `artwork.url(`, `MPMediaItemArtwork` usage outside playback/playlist screens.
  - fix: Restrict cover art/metadata to playback and playlist contexts.
- **[4.5.2-07]** Is cover art/metadata kept out of marketing or advertising unless rights-holders specifically authorized it?
  - quote: "should not be used in any marketing or advertising without getting specific authorization from rights-holders"
  - surface: asc
  - verify: Review App Store Connect screenshots, app previews, promotional text and any marketing for album art not tied to showing app functionality.
  - fix: Remove cover art from marketing or obtain authorization (manual).
- **[4.5.2-08]** Does the Apple Music integration follow the Apple Music Identity Guidelines?
  - quote: "Make sure to follow the Apple Music Identity Guidelines when integrating Apple Music services in your app."
  - surface: manual
  - verify: Review Apple Music badges/logos/naming in the UI and metadata against the Apple Music Identity Guidelines.
  - fix: Correct Apple Music branding per the Identity Guidelines.
- **[4.5.2-09]** If the app accesses Apple Music user data (playlists, favorites), is this access clearly disclosed in the purpose string?
  - quote: "must clearly disclose this access in the purpose string"
  - surface: code
  - verify: Check Info.plist `NSAppleMusicUsageDescription` exists and clearly describes access to the user's Apple Music data; grep for `MusicAuthorization.request()` / `MPMediaLibrary.requestAuthorization`.
  - fix: Add/clarify `NSAppleMusicUsageDescription`.
- **[4.5.2-10]** Is collected Apple Music data not shared with third parties except to support or improve the app experience?
  - quote: "Any data collected may not be shared with third parties for any purpose other than supporting or improving the app experience."
  - surface: code
  - verify: Trace Apple Music data (library, playlists, favorites) to network calls and third-party SDKs (analytics/ads); compare with App Store Connect App Privacy answers.
  - fix: Stop sending Apple Music data to third parties for other purposes.
- **[4.5.2-11]** Is Apple Music data not used to identify users or devices, or to target advertising?
  - quote: "This data may not be used to identify users or devices, or to target advertising."
  - surface: code
  - verify: Check whether Apple Music data is combined with identifiers (IDFA, device IDs, user IDs) or passed to ad SDKs.
  - fix: Remove identification/ad-targeting uses of Apple Music data.

## 4.5.3 No spam or exploitation via Apple Services

**Source text (verbatim):**
> 4.5.3 Do not use Apple Services to spam, phish, or send unsolicited messages to customers, including Game Center, Push Notifications, Live Activities, etc. Do not attempt to reverse lookup, trace, relate, associate, mine, harvest, or otherwise exploit Player IDs, aliases, or other information obtained through Game Center, or you will be removed from the Apple Developer Program.

**Applies to:** Apps using Apple Services (Game Center, Push Notifications, Live Activities, etc.)

- **[4.5.3-01]** Does the app avoid using Apple Services (Game Center, Push Notifications, Live Activities, etc.) to spam, phish, or send unsolicited messages?
  - quote: "Do not use Apple Services to spam, phish, or send unsolicited messages to customers, including Game Center, Push Notifications, Live Activities, etc."
  - surface: code
  - verify: Review push-sending server logic and notification content, `ActivityKit` (`Activity.request`) usage, Game Center invites/challenges; confirm messages relate to user-initiated or expected activity.
  - fix: Remove unsolicited/spam messaging.
- **[4.5.3-02]** Does the app avoid reverse lookup, tracing, associating, mining, harvesting or otherwise exploiting Game Center Player IDs, aliases, or other information?
  - quote: "Do not attempt to reverse lookup, trace, relate, associate, mine, harvest, or otherwise exploit Player IDs, aliases, or other information obtained through Game Center"
  - surface: code
  - verify: grep for `GKLocalPlayer`, `gamePlayerID`, `teamPlayerID`, `playerID`, `alias`, `displayName` and trace whether they are sent to servers/analytics or joined with other identifiers.
  - fix: Stop collecting/associating Game Center identifiers beyond approved use.

## 4.5.4 Push Notifications

**Source text (verbatim):**
> 4.5.4 Push Notifications must not be required for the app to function, and should not be used to send sensitive personal or confidential information. Push Notifications should not be used for promotions or direct marketing purposes unless customers have explicitly opted in to receive them via consent language displayed in your app’s UI, and you provide a method in your app for a user to opt out from receiving such messages. Abuse of these services may result in revocation of your privileges.

**Applies to:** Apps using Push Notifications
**Requires:** push

- **[4.5.4-01]** Does the app function when push notification permission is denied?
  - quote: "Push Notifications must not be required for the app to function"
  - surface: runtime
  - verify: Fresh install; deny the notification prompt (`UNUserNotificationCenter.requestAuthorization`); confirm all core features work and there is no blocking gate; grep for code that blocks progress when `authorizationStatus != .authorized`.
  - fix: Remove gating on notification permission.
- **[4.5.4-02]** Do push notifications avoid sending sensitive personal or confidential information?
  - quote: "should not be used to send sensitive personal or confidential information"
  - surface: code
  - verify: Review server push payload templates and Notification Service Extension for health, financial, passwords/OTP-with-context, or other sensitive content in `alert` body.
  - fix: Remove sensitive data from payloads; show generic text and load details in-app.
- **[4.5.4-03]** If push is used for promotions/direct marketing, have users explicitly opted in via consent language displayed in the app’s UI?
  - quote: "unless customers have explicitly opted in to receive them via consent language displayed in your app’s UI"
  - surface: runtime
  - verify: Find consent language for promotional/marketing notifications displayed in the app's UI (e.g., an opt-in screen or toggle with consent text) that users explicitly accept; grep for marketing opt-in flags sent to the push server.
  - fix: Add an explicit in-app marketing opt-in with consent language; send promotional pushes only to opted-in users.
- **[4.5.4-04]** Does the app provide an in-app method to opt out of promotional push messages?
  - quote: "you provide a method in your app for a user to opt out from receiving such messages"
  - surface: runtime
  - verify: Check the app's settings screen for a marketing-notifications toggle that updates the server opt-in state.
  - fix: Add an in-app opt-out toggle wired to the backend.

## 4.5.5 Game Center Player IDs

**Source text (verbatim):**
> 4.5.5 Only use Game Center Player IDs in a manner approved by the Game Center terms and do not display them in the app or to any third party.

**Applies to:** Apps using Game Center

**Related:** Game Center terms

- **[4.5.5-01]** Are Game Center Player IDs used only as approved by the Game Center terms?
  - quote: "Only use Game Center Player IDs in a manner approved by the Game Center terms"
  - surface: manual
  - verify: grep for `gamePlayerID`, `teamPlayerID`, `playerID`; document how they are used; developer confirms compliance with Game Center terms.
  - fix: manual — requires developer decision/legal/business action
- **[4.5.5-02]** Are Player IDs never displayed in the app or provided to any third party?
  - quote: "do not display them in the app or to any third party"
  - surface: code
  - verify: Trace `gamePlayerID`/`teamPlayerID`/`playerID` into UI (`Text(`, labels) and into third-party SDK calls (analytics, ads, backend shared with partners).
  - fix: Remove Player ID display and third-party sharing; display `displayName`/`alias` only where appropriate.

## 4.5.6 Apple emoji

**Source text (verbatim):**
> 4.5.6 Apps may use Unicode characters that render as Apple emoji in their app and app metadata. Apple emoji may not be used on other platforms or embedded directly in your app binary.

**Applies to:** Apps using Apple emoji

- **[4.5.6-01]** Is Apple emoji not embedded directly in the app binary (e.g., as image assets)?
  - quote: "Apple emoji may not be used on other platforms or embedded directly in your app binary."
  - surface: code
  - verify: Search Assets.xcassets and bundled images/fonts for Apple emoji artwork (e.g., PNGs of emoji, copies of `Apple Color Emoji` font); emoji should come only from Unicode characters in text.
  - fix: Replace embedded emoji images with Unicode characters or original artwork.
- **[4.5.6-02]** Is Apple emoji not used on other platforms (e.g., Android/web versions of the product)?
  - quote: "Apple emoji may not be used on other platforms"
  - surface: manual
  - verify: Developer confirms other-platform versions/websites do not use Apple emoji images.
  - fix: manual — replace Apple emoji images on other platforms.

## 4.6 Intentionally omitted

**Source text (verbatim):**
> 4.6 Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 4.7 Mini apps, mini games, streaming games, chatbots, plug-ins, and game emulators

**Source text (verbatim):**
> Apps may offer certain software that is not embedded in the binary, specifically HTML5 and JavaScript mini apps and mini games, streaming games, chatbots, and plug-ins. Additionally, retro game console and PC emulator apps can offer to download games. You are responsible for all such software offered in your app, including ensuring that such software complies with these Guidelines and all applicable laws. Software that does not comply with one or more guidelines will lead to the rejection of your app. You must also ensure that the software adheres to the additional rules that follow in 4.7.1 through 4.7.5. These additional rules are important to preserve the experience that App Store customers expect, and to help ensure user safety.

**Applies to:** Apps offering software not embedded in the binary (HTML5/JavaScript mini apps and mini games, streaming games, chatbots, plug-ins) and retro game console/PC emulator apps
**Requires:** mini-apps, dynamic-code, webview, generative-ai, chat-social, game, remote-desktop-streaming

- **[4.7-01]** Does all software offered in the app (mini apps/games, streaming games, chatbots, plug-ins, emulator games) comply with the Guidelines and applicable laws?
  - quote: "You are responsible for all such software offered in your app, including ensuring that such software complies with these Guidelines and all applicable laws."
  - surface: manual
  - verify: Identify downloaded/hosted software (grep for `WKWebView` loading remote mini-app bundles, `JavaScriptCore`/`JSContext`, plug-in loaders, emulator ROM download flows, chatbot backends); developer documents the review process for that software.
  - fix: manual — requires developer decision/legal/business action (establish content review/moderation of offered software)
- **[4.7-02]** Does the offered software adhere to the additional rules in 4.7.1 through 4.7.5?
  - quote: "You must also ensure that the software adheres to the additional rules that follow in 4.7.1 through 4.7.5."
  - surface: manual
  - verify: Run checks 4.7.1-* through 4.7.5-*.
  - fix: See 4.7.1–4.7.5 fixes.

## 4.7.1 Privacy, moderation, and payments for offered software

**Source text (verbatim):**
> 4.7.1 Software offered in apps under this rule must:
> - follow all privacy guidelines, including but not limited to the rules set forth in Guideline 5.1 concerning collection, use, and sharing of data, and sensitive data (such as health and personal data from kids);
> - include a method for filtering objectionable material, a mechanism to report content and timely responses to concerns, and the ability to block abusive users; and
> - follow Guideline 3.1 in order to offer digital goods or services to end users.

**Applies to:** Software offered under 4.7
**Requires:** mini-apps, dynamic-code, webview, generative-ai, chat-social, game, remote-desktop-streaming

- **[4.7.1-01]** Does the offered software follow all privacy guidelines, including Guideline 5.1 on collection, use, and sharing of data and sensitive data?
  - quote: "follow all privacy guidelines, including but not limited to the rules set forth in Guideline 5.1 concerning collection, use, and sharing of data, and sensitive data (such as health and personal data from kids)"
  - surface: code
  - verify: Identify what data the hosted software can collect (JS bridges, `WKScriptMessageHandler`, chatbot input logging); apply the 5.1 checks to it; compare with App Store Connect App Privacy answers.
  - fix: Apply Guideline 5.1 fixes to the hosted software.
- **[4.7.1-02]** Does the app include a method for filtering objectionable material in the offered software?
  - quote: "include a method for filtering objectionable material"
  - surface: runtime
  - verify: Look for content filtering (moderation APIs, blocklists, content settings) applied to mini apps/chatbot output; exercise it at runtime.
  - fix: Add content filtering.
- **[4.7.1-03]** Is there a mechanism to report content, with timely responses to concerns?
  - quote: "a mechanism to report content and timely responses to concerns"
  - surface: runtime
  - verify: Find a "Report" action on mini apps/chatbot responses/plug-in content and the backend that receives reports; developer attests to response process.
  - fix: Add an in-app report mechanism and a response process.
- **[4.7.1-04]** Can users block abusive users?
  - quote: "the ability to block abusive users"
  - surface: runtime
  - verify: Where offered software has user interaction, find a "Block user" action and confirm it hides that user's content.
  - fix: Add user blocking.
- **[4.7.1-05]** Does offered software follow Guideline 3.1 when offering digital goods or services?
  - quote: "follow Guideline 3.1 in order to offer digital goods or services to end users"
  - surface: code
  - verify: Check mini apps/plug-ins for digital purchases routed outside StoreKit (web checkout, third-party payment SDKs in JS bridges); apply 3.1 checks.
  - fix: Route digital goods/services through in-app purchase as required by 3.1.

## 4.7.2 Native API exposure

**Source text (verbatim):**
> 4.7.2 Your app may not extend or expose native platform APIs or technologies to the software without prior permission from Apple.

**Applies to:** Apps offering software under 4.7
**Requires:** mini-apps, dynamic-code, webview, generative-ai, chat-social, game, remote-desktop-streaming

- **[4.7.2-01]** Does the app avoid extending or exposing native platform APIs or technologies to the offered software (unless Apple granted prior permission)?
  - quote: "Your app may not extend or expose native platform APIs or technologies to the software without prior permission from Apple."
  - surface: code
  - verify: grep for `WKScriptMessageHandler`, `addScriptMessageHandler`, `userContentController`, `JSContext`/`JSExport` bridges exposing camera, location, contacts, file system, Bluetooth, HealthKit, etc. to hosted JS/plug-ins.
  - fix: Remove native API bridges or obtain prior permission from Apple (manual).

## 4.7.3 Data and permission sharing consent

**Source text (verbatim):**
> 4.7.3 Your app may not share data or privacy permissions to any individual software offered in your app without explicit user consent in each instance.

**Applies to:** Apps offering software under 4.7
**Requires:** mini-apps, dynamic-code, webview, generative-ai, chat-social, game, remote-desktop-streaming

- **[4.7.3-01]** Does the app obtain explicit user consent each time before sharing data or privacy permissions with an individual piece of offered software?
  - quote: "Your app may not share data or privacy permissions to any individual software offered in your app without explicit user consent in each instance."
  - surface: runtime
  - verify: Trace data (user profile, location, contacts, photos) passed into mini apps/plug-ins/chatbots; confirm a per-software, per-instance consent prompt precedes each share; run the flow.
  - fix: Add an explicit consent prompt per software and per instance before sharing.

## 4.7.4 Index of software with universal links

**Source text (verbatim):**
> 4.7.4 You must provide an index of software and metadata available in your app. It must include universal links that lead to all of the software offered in your app.

**Applies to:** Apps offering software under 4.7
**Requires:** mini-apps, dynamic-code, webview, generative-ai, chat-social, game, remote-desktop-streaming

- **[4.7.4-01]** Does the app provide an index of software and metadata available in the app?
  - quote: "You must provide an index of software and metadata available in your app."
  - surface: manual
  - verify: Developer provides the location of the index (e.g., web page) listing every mini app/game/plug-in with metadata.
  - fix: Publish an index of all offered software with metadata.
- **[4.7.4-02]** Does the index include universal links leading to all offered software?
  - quote: "It must include universal links that lead to all of the software offered in your app."
  - surface: code
  - verify: Check `com.apple.developer.associated-domains` entitlement for `applinks:` domains, the hosted `apple-app-site-association` file paths, and that the app handles those links (`onOpenURL`, `application(_:continue:restorationHandler:)`) to open each software item.
  - fix: Add associated domains/AASA routes and in-app handling for universal links to each software item.

## 4.7.5 Age rating identification and restriction

**Source text (verbatim):**
> 4.7.5 Your app must provide a way for users to identify software that exceeds the app’s age rating, and use an age restriction mechanism based on verified or declared age to limit access by underage users.

**Applies to:** Apps offering software under 4.7
**Requires:** mini-apps, dynamic-code, webview, generative-ai, chat-social, game, remote-desktop-streaming

- **[4.7.5-01]** Does the app provide a way for users to identify software that exceeds the app’s age rating?
  - quote: "Your app must provide a way for users to identify software that exceeds the app’s age rating"
  - surface: runtime
  - verify: Compare App Store Connect > App Information > Age Rating with the offered software; confirm items exceeding it are labeled in the UI.
  - fix: Add age-rating labels to offered software exceeding the app's rating.
- **[4.7.5-02]** Does the app use an age restriction mechanism based on verified or declared age to limit underage access?
  - quote: "use an age restriction mechanism based on verified or declared age to limit access by underage users"
  - surface: code
  - verify: grep for age gates / birthdate entry / age-verification or declared-age APIs (e.g., `DeclaredAgeRange`), and confirm gating logic blocks over-rated software for underage users.
  - fix: Implement an age gate using verified or declared age.

## 4.8 Login Services

**Source text (verbatim):**
> Apps that use a third-party or social login service (such as Facebook Login, Google Sign-In, Log in with X, Sign In with LinkedIn, Login with Amazon, or WeChat Login) to set up or authenticate the user’s primary account with the app must also offer as an equivalent option another login service with the following features:
> - the login service limits data collection to the user’s name and email address;
> - the login service allows users to keep their email address private as part of setting up their account; and
> - the login service does not collect interactions with your app for advertising purposes without consent.
>
> A user’s primary account is the account they establish with your app for the purposes of identifying themselves, signing in, and accessing your features and associated services.
>
> Another login service is not required if:
> - Your app exclusively uses your company’s own account setup and sign-in systems.
> - Your app is an alternative app marketplace, or an app distributed from an alternative app marketplace, that uses a marketplace-specific login for account, download, and commerce features.
> - Your app is an education, enterprise, or business app that requires the user to sign in with an existing education or enterprise account.
> - Your app uses a government or industry-backed citizen identification system or electronic ID to authenticate users.
> - Your app is a client for a specific third-party service and users are required to sign in to their mail, social media, or other third-party account directly to access their content.

**Applies to:** Apps that use a third-party or social login service to set up or authenticate the user’s primary account (unless an exemption listed in the source applies)
**Requires:** third-party-login, login

- **[4.8-01]** Does the app use a third-party or social login (Facebook, Google, X, LinkedIn, Amazon, WeChat, etc.) for the user’s primary account?
  - quote: "Apps that use a third-party or social login service (such as Facebook Login, Google Sign-In, Log in with X, Sign In with LinkedIn, Login with Amazon, or WeChat Login) to set up or authenticate the user’s primary account"
  - surface: code
  - verify: grep for `FBSDKLoginKit`/`LoginManager`, `GoogleSignIn`/`GIDSignIn`, `ASWebAuthenticationSession` with OAuth providers, `LoginWithAmazon`, `WechatOpenSDK`, Firebase Auth providers (`GoogleAuthProvider`, `FacebookAuthProvider`, `OAuthProvider`), Auth0/Supabase social providers; check Podfile/Package.resolved. If none, 4.8 does not apply (mark N/A).
  - fix: N/A (classification check).
- **[4.8-02]** If an exemption is claimed, does at least one listed exemption apply (own account system only; alternative marketplace login; existing education/enterprise account; government/industry citizen ID/eID; client for a specific third-party service)?
  - quote: "Another login service is not required if:"
  - surface: manual
  - verify: Developer states which exemption applies; verify against code (e.g., only company-owned auth, enterprise SSO only, client app for a third-party service).
  - fix: manual — requires developer decision/legal/business action
- **[4.8-03]** If 4.8 applies, does the app also offer another login service as an equivalent option?
  - quote: "must also offer as an equivalent option another login service"
  - surface: runtime
  - verify: Run the sign-in/sign-up screen; confirm an equivalent alternative is presented alongside the social logins (e.g., Sign in with Apple via `AuthenticationServices` `ASAuthorizationAppleIDProvider` / `SignInWithAppleButton`, with `com.apple.developer.applesignin` entitlement), available at both account setup and sign-in.
  - fix: Add another login service, offered as an equivalent option, that meets the three listed features (e.g., Sign in with Apple).
- **[4.8-04]** Does that other login service limit data collection to the user’s name and email address?
  - quote: "the login service limits data collection to the user’s name and email address"
  - surface: code
  - verify: For the alternative login, inspect requested scopes (e.g., `request.requestedScopes = [.fullName, .email]`) and confirm no extra data is required in the flow.
  - fix: Limit requested data to name and email.
- **[4.8-05]** Does that other login service allow users to keep their email address private when setting up their account?
  - quote: "the login service allows users to keep their email address private as part of setting up their account"
  - surface: runtime
  - verify: Run account setup with the alternative login choosing a private/relay email (e.g., Hide My Email); confirm the account is created without demanding a real email afterwards.
  - fix: Support private relay emails; don't force a real email after sign-up.
- **[4.8-06]** Does that other login service avoid collecting interactions with the app for advertising purposes without consent?
  - quote: "the login service does not collect interactions with your app for advertising purposes without consent"
  - surface: manual
  - verify: Identify the alternative login provider and its data practices; for a custom provider, check that login-linked events are not sent to ad SDKs without consent.
  - fix: Use a login service that meets this requirement, or obtain consent before ad-related collection.

## 4.9 Apple Pay

**Source text (verbatim):**
> Apps using Apple Pay must provide all material purchase information to the user prior to sale of any good or service and must use Apple Pay branding and user interface elements correctly, as described in the Apple Pay Marketing Guidelines and Human Interface Guidelines. Apps using Apple Pay to offer recurring payments must, at a minimum, disclose the following information:
> - The length of the renewal term and the fact that it will continue until canceled
> - What will be provided during each period
> - The actual charges that will be billed to the customer
> - How to cancel

**Applies to:** Apps using Apple Pay (recurring-payment checks apply to apps using Apple Pay for recurring payments)
**Requires:** apple-pay

**Related:** Apple Pay Marketing Guidelines; Human Interface Guidelines

- **[4.9-01]** Does the app provide all material purchase information before the sale?
  - quote: "must provide all material purchase information to the user prior to sale of any good or service"
  - surface: runtime
  - verify: grep for `PassKit`, `PKPaymentRequest`, `PKPaymentAuthorizationController`, `PayWithApplePayButton`, `PKPaymentButton`; run the checkout and confirm all material purchase information (e.g., item, price, taxes, shipping, totals via `paymentSummaryItems`) is shown before the sale is completed.
  - fix: Show complete purchase details before payment.
- **[4.9-02]** Does the app use Apple Pay branding and UI elements correctly per the Apple Pay Marketing Guidelines and HIG?
  - quote: "must use Apple Pay branding and user interface elements correctly, as described in the Apple Pay Marketing Guidelines and Human Interface Guidelines"
  - surface: code
  - verify: Review Apple Pay buttons, marks and text mentioning Apple Pay against the Apple Pay Marketing Guidelines and HIG (e.g., check use of `PKPaymentButton`/`PayWithApplePayButton` and button type/style).
  - fix: Correct Apple Pay branding/UI elements per the Apple Pay Marketing Guidelines and HIG.
- **[4.9-03]** For recurring payments, does the app disclose the renewal term length and that it continues until canceled?
  - quote: "The length of the renewal term and the fact that it will continue until canceled"
  - surface: runtime
  - verify: grep for `PKRecurringPaymentRequest`; run the recurring checkout and confirm the disclosure text.
  - fix: Add renewal term and "continues until canceled" disclosure.
- **[4.9-04]** For recurring payments, does the app disclose what will be provided during each period?
  - quote: "What will be provided during each period"
  - surface: runtime
  - verify: Inspect recurring checkout copy for a description of what each period includes.
  - fix: Add per-period deliverable disclosure.
- **[4.9-05]** For recurring payments, does the app disclose the actual charges billed?
  - quote: "The actual charges that will be billed to the customer"
  - surface: runtime
  - verify: Confirm the actual billed amount per period is shown (e.g., `PKRecurringPaymentSummaryItem` amount and checkout copy).
  - fix: Display actual charges.
- **[4.9-06]** For recurring payments, does the app disclose how to cancel?
  - quote: "How to cancel"
  - surface: runtime
  - verify: Confirm cancellation instructions are shown in checkout (and `managementURL` on `PKRecurringPaymentRequest` if used).
  - fix: Add cancellation instructions.

## 4.10 Monetizing Built-In Capabilities

**Source text (verbatim):**
> You may not monetize built-in capabilities provided by the hardware or operating system, such as Push Notifications, the camera, or the gyroscope; or Apple services and technologies, such as Apple Music access, iCloud storage, or Screen Time APIs.

**Applies to:** All apps

- **[4.10-01]** Does the app avoid monetizing built-in hardware/OS capabilities (e.g., Push Notifications, camera, gyroscope)?
  - quote: "You may not monetize built-in capabilities provided by the hardware or operating system, such as Push Notifications, the camera, or the gyroscope"
  - surface: code
  - verify: Inspect paywall/IAP gating (`Product.purchase`, entitlement checks, RevenueCat `entitlements`) and what features they unlock; flag paywalls whose only value is access to a built-in capability (e.g., paying to enable notifications or basic camera/sensor access).
  - fix: Remove charges for built-in capabilities; monetize only the app's own added value.
- **[4.10-02]** Does the app avoid monetizing Apple services and technologies (e.g., Apple Music access, iCloud storage, Screen Time APIs)?
  - quote: "or Apple services and technologies, such as Apple Music access, iCloud storage, or Screen Time APIs"
  - surface: code
  - verify: Check whether IAP gates iCloud sync/storage (`CloudKit`, `NSUbiquitousKeyValueStore`, iCloud entitlements), Apple Music access (MusicKit), or Screen Time (`FamilyControls`, `ManagedSettings`, `DeviceActivity`) as the purchased value itself; review App Store Connect IAP display names/descriptions.
  - fix: Remove paywalls on Apple services/technologies themselves.
