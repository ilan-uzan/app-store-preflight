# App Review Guidelines — 1. Safety
Source: https://developer.apple.com/app-store/review/guidelines/#safety  
Retrieved: 2026-10-30

Guidelines version: "Last Updated: October 16, 2026"

## 1 Safety

**Source text (verbatim):**
> When people install an app from the App Store, they want to feel confident that it’s safe to do so—that the app doesn’t contain upsetting or offensive content, won’t damage their device, and isn’t likely to cause physical harm from its use. We’ve outlined the major pitfalls below, but if you’re looking to shock and offend people, the App Store isn’t the right place for your app. Some of these rules are also included in Notarization for iOS and iPadOS apps.

**Applies to:** All apps

**Related:** Notarization for iOS and iPadOS apps

- **[1-01]** Is the app free of upsetting or offensive content, and does it avoid behavior that could damage the device or cause physical harm from its use?
  - quote: "the app doesn’t contain upsetting or offensive content, won’t damage their device, and isn’t likely to cause physical harm from its use"
  - surface: manual
  - verify: Review all bundled content (Assets.xcassets, bundled media, strings/Localizable files, remote content endpoints) and the App Store screenshots/description in App Store Connect > App Information / version page; run the main flows on simulator. Confirm each sub-guideline 1.1–1.7 passes.
  - fix: Remove or rework offending content/behavior; see the sub-guideline checks below.
- **[1-02]** Is the app's purpose something other than to shock and offend people?
  - quote: "if you’re looking to shock and offend people, the App Store isn’t the right place for your app"
  - surface: manual
  - verify: Developer attests to the app's intent; review the App Store description, promotional text and keywords in App Store Connect for shock-value framing.
  - fix: manual — requires developer decision/legal/business action

## 1.1 Objectionable Content

**Source text (verbatim):**
> Apps should not include content that is offensive, insensitive, upsetting, intended to disgust, in exceptionally poor taste, or just plain creepy. Examples of such content include:

**Applies to:** All apps

- **[1.1-01]** Is the app free of content that is offensive, insensitive, upsetting, intended to disgust, in exceptionally poor taste, or just plain creepy? (Guideline wording: “should not”.)
  - quote: "Apps should not include content that is offensive, insensitive, upsetting, intended to disgust, in exceptionally poor taste, or just plain creepy."
  - surface: runtime
  - verify: Inspect bundled images/audio/video (Assets.xcassets, Resources), all user-facing strings (Localizable.strings / .xcstrings, hard-coded Text("...")), server-delivered content, and App Store Connect screenshots, previews and description; exercise every screen in the simulator.
  - fix: Remove or replace the objectionable assets/strings; if content is intentional (e.g. mature themes), ensure it does not cross into the 1.1.x categories and that the age rating questionnaire in App Store Connect reflects it.

## 1.1.1 Defamatory, discriminatory, or mean-spirited content

**Source text (verbatim):**
> Defamatory, discriminatory, or mean-spirited content, including references or commentary about religion, race, sexual orientation, gender, national/ethnic origin, or other targeted groups, particularly if the app is likely to humiliate, intimidate, or harm a targeted individual or group. Professional political satirists and humorists are generally exempt from this requirement.

**Applies to:** All apps (professional political satirists and humorists are generally exempt)

- **[1.1.1-01]** Is the app free of defamatory, discriminatory, or mean-spirited content, including references or commentary about religion, race, sexual orientation, gender, national/ethnic origin, or other targeted groups?
  - quote: "Defamatory, discriminatory, or mean-spirited content, including references or commentary about religion, race, sexual orientation, gender, national/ethnic origin, or other targeted groups"
  - surface: runtime
  - verify: Grep all localized strings, bundled text/JSON content and remote content samples for slurs or commentary targeting the listed groups; review images and character designs; review App Store Connect description and screenshots.
  - fix: Remove or rewrite the offending content.
- **[1.1.1-02]** Is the app unlikely to humiliate, intimidate, or harm a targeted individual or group?
  - quote: "particularly if the app is likely to humiliate, intimidate, or harm a targeted individual or group"
  - surface: manual
  - verify: Review features that name, rate, rank or depict real individuals or groups (e.g. roast/rating features, user-tagging) in the simulator; developer attests to intent.
  - fix: Remove or redesign features that target individuals or groups.
- **[1.1.1-03]** If the app relies on the satire exemption, is it from a professional political satirist or humorist?
  - quote: "Professional political satirists and humorists are generally exempt from this requirement."
  - surface: manual
  - verify: Developer attests to professional satirist/humorist status; if so, explain it in App Store Connect > version page > App Review Information > Notes.
  - fix: manual — requires developer decision/legal/business action

## 1.1.2 Realistic violence

**Source text (verbatim):**
> Realistic portrayals of people or animals being killed, maimed, tortured, or abused, or content that encourages violence. “Enemies” within the context of a game cannot solely target a specific race, culture, real government, corporation, or any other real entity.

**Applies to:** All apps; the “Enemies” rule applies to games

- **[1.1.2-01]** Is the app free of realistic portrayals of people or animals being killed, maimed, tortured, or abused?
  - quote: "Realistic portrayals of people or animals being killed, maimed, tortured, or abused"
  - surface: runtime
  - verify: Review bundled art, sprites, 3D models, cutscenes/video and gore/blood effects (e.g. particle systems, shaders, asset names like "blood", "gore", "dismember"); play through violent sequences in the simulator; check App Store Connect screenshots/app previews.
  - fix: Stylize or reduce realism of violent depictions (e.g. cartoon style, cap gore), or remove them.
- **[1.1.2-02]** Is the app free of content that encourages violence?
  - quote: "content that encourages violence"
  - surface: runtime
  - verify: Review strings, mission/quest text, prompts and marketing copy (App Store Connect description, promotional text) for encouragement of real-world violence.
  - fix: Remove or rewrite content that encourages violence.
- **[1.1.2-03]** If the app is a game with enemies, do the enemies avoid solely targeting a specific race, culture, real government, corporation, or any other real entity?
  - quote: "“Enemies” within the context of a game cannot solely target a specific race, culture, real government, corporation, or any other real entity."
  - surface: manual
  - verify: Review enemy definitions (enemy data files, faction names, character art, level scripts) and play the game in the simulator to confirm enemies are not solely a real race, culture, government, corporation or other real entity.
  - fix: Make enemies fictional or diverse so they do not solely target a real entity.

## 1.1.3 Weapons and dangerous objects

**Source text (verbatim):**
> Depictions that encourage illegal or reckless use of weapons and dangerous objects, or facilitate the purchase of firearms or ammunition.

**Applies to:** All apps

- **[1.1.3-01]** Is the app free of depictions that encourage illegal or reckless use of weapons and dangerous objects?
  - quote: "Depictions that encourage illegal or reckless use of weapons and dangerous objects"
  - surface: runtime
  - verify: Review content involving weapons or dangerous objects (strings, images, tutorials, video) in the simulator and in App Store Connect screenshots/description.
  - fix: Remove or reframe content that encourages illegal or reckless use.
- **[1.1.3-02]** Does the app avoid facilitating the purchase of firearms or ammunition?
  - quote: "facilitate the purchase of firearms or ammunition"
  - surface: code
  - verify: Grep for commerce flows, product catalogs, links (URLs, deep links, SFSafariViewController/openURL targets) and IAP/product IDs related to firearms or ammunition; exercise any shopping flows in the simulator.
  - fix: Remove firearm/ammunition purchase flows and links.

## 1.1.4 Overtly sexual or pornographic material

**Source text (verbatim):**
> Overtly sexual or pornographic material, defined as “explicit descriptions or displays of sexual organs or activities intended to stimulate erotic rather than aesthetic or emotional feelings.” This includes “hookup” apps and other apps that may include pornography or be used to facilitate prostitution, or human trafficking and exploitation.

**Applies to:** All apps

- **[1.1.4-01]** Is the app free of overtly sexual or pornographic material (explicit descriptions or displays of sexual organs or activities intended to stimulate erotic rather than aesthetic or emotional feelings)?
  - quote: "Overtly sexual or pornographic material, defined as “explicit descriptions or displays of sexual organs or activities intended to stimulate erotic rather than aesthetic or emotional feelings.”"
  - surface: runtime
  - verify: Review bundled images/video/text and any remote or AI-generated content paths in the simulator; check App Store Connect screenshots and description.
  - fix: Remove explicit material; for AI/UGC sources, add filtering (see 1.2).
- **[1.1.4-02]** Is the app something other than a “hookup” app?
  - quote: "This includes “hookup” apps"
  - surface: manual
  - verify: Review the app's core purpose, onboarding and App Store Connect description/keywords for hookup positioning.
  - fix: manual — requires developer decision/legal/business action
- **[1.1.4-03]** Is the app free of features through which it may include pornography or be used to facilitate prostitution, or human trafficking and exploitation?
  - quote: "other apps that may include pornography or be used to facilitate prostitution, or human trafficking and exploitation"
  - surface: manual
  - verify: Review features that allow posting, messaging, listings or paid meetups; confirm moderation exists (see 1.2) and developer attests to safeguards.
  - fix: Add moderation/filtering and remove features enabling these uses; otherwise manual — requires developer decision.

## 1.1.5 Religious commentary and quotations

**Source text (verbatim):**
> Inflammatory religious commentary or inaccurate or misleading quotations of religious texts.

**Applies to:** All apps

- **[1.1.5-01]** Is the app free of inflammatory religious commentary?
  - quote: "Inflammatory religious commentary"
  - surface: runtime
  - verify: Review strings and content referencing religion in the simulator and App Store Connect metadata.
  - fix: Remove or rewrite inflammatory commentary.
- **[1.1.5-02]** Are all quotations of religious texts accurate and not misleading?
  - quote: "inaccurate or misleading quotations of religious texts"
  - surface: manual
  - verify: Locate bundled religious texts/quotations (JSON, plist, database files, strings) and have the developer confirm their source edition and accuracy.
  - fix: Correct quotations against an authoritative source and cite it; manual verification by the developer.

## 1.1.6 False information and features

**Source text (verbatim):**
> False information and features, including inaccurate device data or trick/joke functionality, such as fake location trackers. Stating that the app is “for entertainment purposes” won’t overcome this guideline. Apps that enable anonymous or prank phone calls or SMS/MMS messaging will be rejected.

**Applies to:** All apps

- **[1.1.6-01]** Is the app free of false information and features, including inaccurate device data?
  - quote: "False information and features, including inaccurate device data"
  - surface: code
  - verify: Find features that display device data (battery, CPU, network speed, location, sensor readings) and confirm values come from real APIs (e.g. UIDevice, ProcessInfo, CoreLocation, CoreMotion, NWPathMonitor) rather than random/hard-coded values (grep for `random(`, `Int.random`, `arc4random`, fixed constants feeding displayed metrics).
  - fix: Replace fabricated values with real API data or remove the feature.
- **[1.1.6-02]** Is the app free of trick/joke functionality, such as fake location trackers?
  - quote: "trick/joke functionality, such as fake location trackers"
  - surface: runtime
  - verify: Exercise features in the simulator that claim to track, scan, detect or measure (e.g. phone/location trackers, X-ray, lie detector, fingerprint scanners) and confirm they do what they claim; review App Store Connect description for such claims.
  - fix: Remove the fake functionality or make it genuinely functional.
- **[1.1.6-03]** Does the app avoid relying on an “for entertainment purposes” disclaimer to justify false information or features?
  - quote: "Stating that the app is “for entertainment purposes” won’t overcome this guideline."
  - surface: code
  - verify: Grep strings and App Store Connect description for "entertainment purposes" / "for entertainment only" and check whether it is attached to a false/fake feature.
  - fix: Remove the false feature; a disclaimer is not a fix.
- **[1.1.6-04]** Does the app avoid enabling anonymous or prank phone calls or SMS/MMS messaging?
  - quote: "Apps that enable anonymous or prank phone calls or SMS/MMS messaging will be rejected."
  - surface: code
  - verify: Grep for telephony/messaging integrations (CallKit, `tel:` URLs, MFMessageComposeViewController, Twilio/Vonage or other SMS/voice SDKs, caller-ID spoofing or voice changer + call features) and check whether calls/messages can be sent anonymously or as pranks.
  - fix: Remove anonymous/prank calling or messaging capabilities.

## 1.1.7 Harmful concepts capitalizing on current events

**Source text (verbatim):**
> Harmful concepts which capitalize or seek to profit on recent or current events, such as violent conflicts, terrorist attacks, and epidemics.

**Applies to:** All apps

- **[1.1.7-01]** Does the app avoid harmful concepts which capitalize or seek to profit on recent or current events, such as violent conflicts, terrorist attacks, and epidemics?
  - quote: "Harmful concepts which capitalize or seek to profit on recent or current events, such as violent conflicts, terrorist attacks, and epidemics."
  - surface: manual
  - verify: Review app concept, content and App Store Connect name, subtitle, keywords and description for references to recent or current violent conflicts, terrorist attacks or epidemics used to attract downloads or revenue.
  - fix: manual — requires developer decision/legal/business action

## 1.2 User-Generated Content

**Source text (verbatim):**
> Apps that enable users to create, generate, upload, share, or otherwise contribute content present particular challenges, including intellectual property infringement, nonconsensual intimate imagery, and anonymous bullying. This includes social media, user-generated content platforms, and AI content creation apps. To prevent abuse, such apps must include:
> - A method for filtering objectionable material from being posted to the app
> - A mechanism to report offensive content and timely responses to concerns
> - The ability to block abusive users from the service
> - Published contact information so users can easily reach you
>
> Apps with user-generated content or services that end up being used primarily for pornographic content, Chatroulette-style experiences, random or anonymous chat, objectification of real people (such as “hot-or-not” voting), making physical threats, or bullying do not belong on the App Store and may be removed without notice. If your app includes user-generated content from a web-based service, it may display incidental mature “NSFW” content, provided that the content is hidden by default and only displayed when the user turns it on via your website.
>
> It is your responsibility to remove content that violates this guideline, your terms of service, or your community standards. Developers who fail to implement appropriate safeguards or fail to remediate identified violations after notice may be considered in violation of the Developer Code of Conduct. If we find such content, we will ask you to remove it, and provide a plan to improve your compliance with this guideline. Based on your response, your app may be removed from the App Store until you can demonstrate improvements that bring your app into compliance. Egregious or repeated behavior is grounds for immediate removal of your app from the App Store, and from the Apple Developer Program.

**Applies to:** Apps that enable users to create, generate, upload, share, or otherwise contribute content (including social media, user-generated content platforms, and AI content creation apps)

**Related:** Developer Code of Conduct

- **[1.2-01]** Does the app include a method for filtering objectionable material from being posted to the app?
  - quote: "A method for filtering objectionable material from being posted to the app"
  - surface: code
  - verify: Locate every content-submission path (post/comment/upload/message/AI prompt and AI output). Confirm a filter runs before content is published: client or server-side profanity/keyword lists, image moderation (e.g. SensitiveContentAnalysis, Vision, a moderation API such as a cloud moderation endpoint), or AI safety filters on prompts and outputs. Check backend functions/rules for moderation hooks.
  - fix: Add pre-publication filtering on all submission paths (text keyword/profanity filter plus image/AI-output moderation) and reject or hold flagged content.
- **[1.2-02]** Does the app include a mechanism to report offensive content?
  - quote: "A mechanism to report offensive content"
  - surface: runtime
  - verify: In the simulator, confirm every piece of UGC (posts, comments, profiles, messages, AI outputs shared to others) has a reachable Report action (context menu, "..." menu, long-press); grep for "report" actions and the backend endpoint/collection that stores reports.
  - fix: Add a Report action on every UGC item that sends the item ID, reporter and reason to a moderation queue.
- **[1.2-03]** Does the developer provide timely responses to reported concerns?
  - quote: "timely responses to concerns"
  - surface: manual
  - verify: Developer attests to a moderation process (who reviews reports and in what timeframe); describe it in App Store Connect > version page > App Review Information > Notes.
  - fix: manual — requires developer decision/legal/business action
- **[1.2-04]** Does the app provide the ability to block abusive users from the service?
  - quote: "The ability to block abusive users from the service"
  - surface: runtime
  - verify: In the simulator, confirm a Block user action exists on profiles/messages/posts and that blocked users are blocked from the service (their content hidden and interactions prevented); grep for block-list storage and filtering in queries.
  - fix: Add a Block user action that blocks the abusive user from the service (e.g. a block list enforced where content and interactions are served).
- **[1.2-05]** Does the app publish contact information so users can easily reach the developer?
  - quote: "Published contact information so users can easily reach you"
  - surface: runtime
  - verify: Confirm an in-app contact path (Settings/About/Help screen with email, form or support link) and check App Store Connect > version page > Support URL resolves to a page with contact details.
  - fix: Add a Contact/Support entry in-app and ensure the Support URL page lists contact information.
- **[1.2-06]** Is the app's UGC or service not used primarily for pornographic content, Chatroulette-style experiences, random or anonymous chat, objectification of real people (such as “hot-or-not” voting), making physical threats, or bullying?
  - quote: "Apps with user-generated content or services that end up being used primarily for pornographic content, Chatroulette-style experiences, random or anonymous chat, objectification of real people (such as “hot-or-not” voting), making physical threats, or bullying do not belong on the App Store"
  - surface: manual
  - verify: Review core features for random matching, anonymous chat, rating of people's appearance; sample live content; developer attests to actual primary usage.
  - fix: Remove or redesign random/anonymous chat and hot-or-not features; otherwise manual — requires developer decision.
- **[1.2-07]** If the app shows UGC from a web-based service, is any incidental mature “NSFW” content hidden by default and only displayed when the user turns it on via the developer's website?
  - quote: "it may display incidental mature “NSFW” content, provided that the content is hidden by default and only displayed when the user turns it on via your website"
  - surface: code
  - verify: Find NSFW/mature-content flags and settings; confirm default is off and that there is no in-app toggle to enable it (the setting must be changed on the website and read from the server).
  - fix: Default NSFW to hidden, remove any in-app toggle, and read the opt-in from the user's account setting managed on the website.
- **[1.2-08]** Does the developer remove content that violates this guideline, the terms of service, or community standards?
  - quote: "It is your responsibility to remove content that violates this guideline, your terms of service, or your community standards."
  - surface: code
  - verify: Confirm moderator tooling exists to remove content (admin panel, backend delete function, report-review workflow); developer attests that violating content is removed.
  - fix: Add a moderator removal path for violating content; the removal process is a developer responsibility.

## 1.2.1 Creator Content

**Source text (verbatim):**
> Apps which feature content from a specific community of users called “creators” are a great opportunity if properly moderated. These apps present a singular, unified experience for customers to interact with various kinds of creator content. They offer tools and programs to help this community of non-developer creators to author, share, and monetize user-generated experiences. These experiences must not change the core features and functionality of the native app—rather, they add content to those structured experiences. These experiences are not native “apps” coded by developers—they are content within the app itself and are treated as user-generated content by App Review. Such creator content may include video, articles, audio, and even casual games. The App Store supports apps offering such user-generated content so long as they follow all Guidelines, including Guideline 1.2 for moderating user-generated content and Guideline 3.1.1 for payments and in-app purchases. You should communicate to users which content requires additional purchases.
> - (a) Creator apps must provide a way for users to identify content that exceeds the app’s age rating, and use an age restriction mechanism based on verified or declared age to limit access by underage users.

**Applies to:** Apps which feature content from a specific community of users called “creators”

**Related:** Guideline 1.2; Guideline 3.1.1

- **[1.2.1-01]** Do creator experiences avoid changing the core features and functionality of the native app, only adding content to its structured experiences?
  - quote: "These experiences must not change the core features and functionality of the native app—rather, they add content to those structured experiences."
  - surface: code
  - verify: Inspect how creator content is loaded (web views, scripting/JS engines such as JavaScriptCore, downloaded bundles, mini-game runtimes) and confirm it cannot alter native app features or navigation beyond rendering content inside defined experiences.
  - fix: Constrain creator content to the app's structured content containers; remove any capability for it to change native functionality.
- **[1.2.1-02]** Is creator content moderated under Guideline 1.2 (filtering, reporting, blocking, contact info)?
  - quote: "including Guideline 1.2 for moderating user-generated content"
  - surface: code
  - verify: Apply checks 1.2-01 through 1.2-05 to all creator content types (video, articles, audio, casual games).
  - fix: Implement the 1.2 safeguards for creator content.
- **[1.2.1-03]** Does creator-content monetization follow Guideline 3.1.1 for payments and in-app purchases?
  - quote: "Guideline 3.1.1 for payments and in-app purchases"
  - surface: code
  - verify: Find purchase/tipping/unlock flows for creator content; confirm digital content is sold via StoreKit (Product, Transaction APIs) and that products exist in App Store Connect > Monetization > In-App Purchases; cross-check with 3.1.1 checks.
  - fix: Route digital creator-content purchases through In-App Purchase (see 3.1.1).
- **[1.2.1-04]** Does the app communicate to users which content requires additional purchases? (Guideline wording: “should”.)
  - quote: "You should communicate to users which content requires additional purchases."
  - surface: runtime
  - verify: In the simulator, browse creator content and confirm paid items are labeled (price, lock icon, "Premium" badge) before the user opens them.
  - fix: Add clear paid/locked indicators and pricing on creator content that requires purchase.
- **[1.2.1-05]** Does the creator app provide a way for users to identify content that exceeds the app’s age rating?
  - quote: "Creator apps must provide a way for users to identify content that exceeds the app’s age rating"
  - surface: runtime
  - verify: Compare the age rating in App Store Connect > App Information > Age Rating with available creator content; in the simulator confirm higher-rated content is labeled (maturity tags/badges); grep the content model for a rating/maturity field.
  - fix: Add a maturity/age rating field to creator content and display labels for content above the app's age rating.
- **[1.2.1-06]** Does the creator app use an age restriction mechanism based on verified or declared age to limit access by underage users?
  - quote: "use an age restriction mechanism based on verified or declared age to limit access by underage users"
  - surface: code
  - verify: Find age capture (birthdate entry at sign-up, or an age verification/declared-age API such as Declared Age Range) and confirm gating logic blocks underage users from content exceeding the age rating.
  - fix: Collect verified or declared age and gate content above the app's age rating for underage users.

## 1.3 Kids Category

**Source text (verbatim):**
> The Kids Category is a great way for people to easily find apps that are designed for children. If you want to participate in the Kids Category, you should focus on creating a great experience specifically for younger users. These apps must not include links out of the app, purchasing opportunities, or other distractions to kids unless reserved for a designated area behind a parental gate. Keep in mind that once customers expect your app to follow the Kids Category requirements, it will need to continue to meet these guidelines in subsequent updates, even if you decide to deselect the category. Learn more about parental gates.
>
> You must comply with applicable privacy laws around the world relating to the collection of data from children online. Be sure to review the Privacy section of these guidelines for more information. In addition, Kids Category apps may not send personally identifiable information or device information to third parties. Apps in the Kids Category should not include third-party analytics or third-party advertising. This provides a safer experience for kids. In limited cases, third-party analytics may be permitted provided that the services do not collect or transmit the IDFA or any identifiable information about children (such as name, date of birth, email address), their location, or their devices. This includes any device, network, or other information that could be used directly or combined with other information to identify users and their devices. Third-party contextual advertising may also be permitted in limited cases provided that the services have publicly documented practices and policies for Kids Category apps that include human review of ad creatives for age appropriateness.

**Applies to:** Apps that participate in the Kids Category (and apps that previously did, where customers expect them to follow Kids Category requirements)

**Related:** parental gates; Privacy section of these guidelines

- **[1.3-01]** Is the app's Kids Category participation determined (selected in App Store Connect, or previously selected so customers expect Kids Category compliance)?
  - quote: "once customers expect your app to follow the Kids Category requirements, it will need to continue to meet these guidelines in subsequent updates, even if you decide to deselect the category"
  - surface: asc
  - verify: App Store Connect > App Information > Category (Kids) and age band; ask the developer whether earlier versions were in the Kids Category. If yes now or previously, all 1.3 checks apply.
  - fix: manual — requires developer decision/legal/business action
- **[1.3-02]** Is the app free of links out of the app, except in a designated area behind a parental gate?
  - quote: "These apps must not include links out of the app"
  - surface: code
  - verify: Grep for `openURL`, `UIApplication.shared.open`, `Link(`, `SFSafariViewController`, `WKWebView` navigation to external domains, `mailto:`/`tel:`/`itms-apps:` URLs, share sheets and SKStoreProductViewController; confirm each is reachable only after a parental gate.
  - fix: Remove external links or place them in a designated area behind a parental gate.
- **[1.3-03]** Is the app free of purchasing opportunities, except in a designated area behind a parental gate?
  - quote: "purchasing opportunities, or other distractions to kids unless reserved for a designated area behind a parental gate"
  - surface: code
  - verify: Grep for StoreKit purchase calls (`Product.purchase`, `SKPaymentQueue`, `SubscriptionStoreView`, `ProductView`, paywall views) and confirm each is presented only after a parental gate.
  - fix: Place all purchase UI behind a parental gate in a designated area.
- **[1.3-04]** Is the app free of other distractions to kids outside a designated area behind a parental gate?
  - quote: "or other distractions to kids unless reserved for a designated area behind a parental gate"
  - surface: runtime
  - verify: Run the app in the simulator and look for possible distractions in kid-facing areas (e.g. promotional pop-ups, cross-promotion, prompts that interrupt play); the guideline does not enumerate “other distractions”, so judge each case.
  - fix: Move distractions behind a parental gate or remove them.
- **[1.3-05]** If the app has a designated area containing links out, purchasing opportunities or other distractions, is that area behind a parental gate?
  - quote: "reserved for a designated area behind a parental gate"
  - surface: runtime
  - verify: In the simulator, attempt to reach external links/purchases/settings and confirm a parental gate (an adult-level challenge) appears first; locate the gate implementation in code.
  - fix: Implement a parental gate before the designated adult area.
- **[1.3-06]** Does the app comply with applicable privacy laws around the world relating to the collection of data from children online?
  - quote: "You must comply with applicable privacy laws around the world relating to the collection of data from children online."
  - surface: manual
  - verify: Developer attests to legal compliance for children's data in the regions the app is distributed; review the privacy policy URL in App Store Connect > App Privacy.
  - fix: manual — requires developer decision/legal/business action
- **[1.3-07]** Does the app avoid sending personally identifiable information or device information to third parties?
  - quote: "Kids Category apps may not send personally identifiable information or device information to third parties"
  - surface: code
  - verify: List third-party SDKs (Package.resolved, Podfile.lock, Cartfile, embedded frameworks) and network calls to non-developer domains; check PrivacyInfo.xcprivacy NSPrivacyCollectedDataTypes and App Store Connect > App Privacy responses for data shared with third parties.
  - fix: Remove third-party data sharing of PII/device information.
- **[1.3-08]** Is the app free of third-party analytics (unless the limited exception is met)? (Guideline wording: “should not”.)
  - quote: "Apps in the Kids Category should not include third-party analytics"
  - surface: code
  - verify: Search dependencies and imports for analytics SDKs (e.g. Firebase Analytics, Google Analytics, Mixpanel, Amplitude, Segment, Flurry, AppsFlyer, Adjust, Branch, Sentry with user data, TelemetryDeck).
  - fix: Remove third-party analytics SDKs, or confirm the limited exception in 1.3-10.
- **[1.3-09]** Is the app free of third-party advertising (unless the contextual-advertising exception is met)? (Guideline wording: “should not”.)
  - quote: "or third-party advertising"
  - surface: code
  - verify: Search dependencies and imports for ad SDKs (e.g. Google Mobile Ads/AdMob, AppLovin, Unity Ads, ironSource, Meta Audience Network, Vungle, Chartboost); check Info.plist for `GADApplicationIdentifier` and `SKAdNetworkItems`.
  - fix: Remove third-party advertising SDKs, or confirm the exception in 1.3-11.
- **[1.3-10]** If third-party analytics are used, do the services avoid collecting or transmitting the IDFA or any identifiable information about children (such as name, date of birth, email address), their location, or their devices, including any device, network, or other information that could be used to identify users and their devices?
  - quote: "third-party analytics may be permitted provided that the services do not collect or transmit the IDFA or any identifiable information about children (such as name, date of birth, email address), their location, or their devices"
  - surface: code
  - verify: Grep for `ASIdentifierManager`, `advertisingIdentifier`, `ATTrackingManager`, `identifierForVendor`, CoreLocation usage and analytics calls passing user properties (name, birthdate, email, device/network info); confirm analytics configuration disables IDFA/device/IP collection; check PrivacyInfo.xcprivacy and SDK privacy manifests.
  - fix: Remove the analytics SDK, or configure it to collect no IDFA, identifiers, location or device/network data.
- **[1.3-11]** If third-party contextual advertising is used, does the ad service have publicly documented practices and policies for Kids Category apps that include human review of ad creatives for age appropriateness?
  - quote: "Third-party contextual advertising may also be permitted in limited cases provided that the services have publicly documented practices and policies for Kids Category apps that include human review of ad creatives for age appropriateness."
  - surface: manual
  - verify: Identify the ad network; developer provides the URL to the network's public Kids Category policy showing human review of ad creatives; confirm ads are contextual (not behavioral).
  - fix: Switch to a qualifying ad network or remove advertising; manual — requires developer decision.

## 1.4 Physical Harm

**Source text (verbatim):**
> If your app behaves in a way that risks physical harm, we may reject it. For example:

**Applies to:** All apps

- **[1.4-01]** Does the app avoid behaving in a way that risks physical harm?
  - quote: "If your app behaves in a way that risks physical harm, we may reject it."
  - surface: manual
  - verify: Review app features (health, fitness, driving, challenges, device usage) against 1.4.1–1.4.5.
  - fix: See sub-guideline fixes.

## 1.4.1 Medical apps

**Source text (verbatim):**
> Medical apps that could provide inaccurate data or information, or that could be used for diagnosing or treating patients may be reviewed with greater scrutiny.
> - Apps must clearly disclose data and methodology to support accuracy claims relating to health measurements, and if the level of accuracy or methodology cannot be validated, we will reject your app. For example, apps that claim to take x-rays, measure blood pressure, body temperature, blood glucose levels, or blood oxygen levels using only the sensors on the device are not permitted.
> - Apps should remind users to check with a doctor in addition to using the app and before making medical decisions.
> If your medical app has received regulatory clearance, please submit a link to that documentation with your app.

**Applies to:** Medical apps that could provide inaccurate data or information, or that could be used for diagnosing or treating patients

- **[1.4.1-01]** Does the app clearly disclose data and methodology to support accuracy claims relating to health measurements?
  - quote: "Apps must clearly disclose data and methodology to support accuracy claims relating to health measurements"
  - surface: runtime
  - verify: Find health measurement features (HealthKit, CoreMotion, camera/flash-based measurement, sensor reads) and any accuracy claims in strings and App Store Connect description; confirm the data and methodology behind each claim are clearly disclosed (e.g. in-app screen or link, or the App Store description).
  - fix: Clearly disclose the data sources and methodology supporting each accuracy claim (e.g. an in-app disclosure), or remove the claims.
- **[1.4.1-02]** Can the level of accuracy or methodology of health measurements be validated?
  - quote: "if the level of accuracy or methodology cannot be validated, we will reject your app"
  - surface: manual
  - verify: Developer provides validation evidence (studies, testing data); reference it in App Store Connect > App Review Information > Notes.
  - fix: manual — requires developer decision/legal/business action
- **[1.4.1-03]** Does the app avoid claiming to take x-rays, measure blood pressure, body temperature, blood glucose levels, or blood oxygen levels using only the sensors on the device?
  - quote: "apps that claim to take x-rays, measure blood pressure, body temperature, blood glucose levels, or blood oxygen levels using only the sensors on the device are not permitted"
  - surface: code
  - verify: Grep strings, feature names and App Store Connect metadata for "x-ray", "blood pressure", "temperature", "glucose", "SpO2"/"oxygen" measurement claims; confirm whether readings come from external hardware/accessories or HealthKit data written by such devices rather than iPhone sensors only.
  - fix: Remove on-device-only measurement claims, or source readings from validated external devices.
- **[1.4.1-04]** Does the app remind users to check with a doctor in addition to using the app and before making medical decisions? (Guideline wording: “should”.)
  - quote: "Apps should remind users to check with a doctor in addition to using the app and before making medical decisions."
  - surface: runtime
  - verify: In the simulator, confirm a visible reminder (onboarding, results screen, or disclaimer) advising users to consult a doctor; grep strings for "doctor"/"physician"/"medical advice".
  - fix: Add a "consult a doctor" reminder near health results/recommendations and in onboarding.
- **[1.4.1-05]** If the medical app has received regulatory clearance, is a link to that documentation submitted with the app?
  - quote: "If your medical app has received regulatory clearance, please submit a link to that documentation with your app."
  - surface: asc
  - verify: App Store Connect > version page > App Review Information > Notes contains a link to the clearance documentation (if cleared).
  - fix: Add the regulatory clearance link to App Review Notes.

## 1.4.2 Drug dosage calculators

**Source text (verbatim):**
> Drug dosage calculators must come from the drug manufacturer, a hospital, university, health insurance company, pharmacy or other approved entity, or receive approval by the FDA or one of its international counterparts. Given the potential harm to patients, we need to be sure that the app will be supported and updated over the long term.

**Applies to:** Apps that include drug dosage calculators

- **[1.4.2-01]** Does the app contain a drug dosage calculator?
  - quote: "Drug dosage calculators"
  - surface: code
  - verify: Grep for dosage/dose/mg-per-kg calculations, medication databases and related strings.
  - fix: If present and the publisher is not an approved entity (1.4.2-02), remove the calculator.
- **[1.4.2-02]** Does the drug dosage calculator come from the drug manufacturer, a hospital, university, health insurance company, pharmacy or other approved entity, or has it received approval by the FDA or one of its international counterparts?
  - quote: "must come from the drug manufacturer, a hospital, university, health insurance company, pharmacy or other approved entity, or receive approval by the FDA or one of its international counterparts"
  - surface: asc
  - verify: App Store Connect > Users and Access / Agreements: check the developer/seller name is the qualifying entity; or developer provides FDA (or international counterpart) approval documentation for App Review Notes.
  - fix: manual — requires developer decision/legal/business action
- **[1.4.2-03]** Will the app be supported and updated over the long term?
  - quote: "we need to be sure that the app will be supported and updated over the long term"
  - surface: manual
  - verify: Developer attests to a long-term maintenance commitment.
  - fix: manual — requires developer decision/legal/business action

## 1.4.3 Tobacco, vape, drugs, and alcohol

**Source text (verbatim):**
> Apps that encourage consumption of tobacco and vape products, illegal drugs, or excessive amounts of alcohol are not permitted. Apps that encourage minors to consume any of these substances will be rejected. Facilitating the sale of controlled substances (except for licensed pharmacies and licensed or otherwise legal cannabis dispensaries), or tobacco is not allowed.

**Applies to:** All apps

- **[1.4.3-01]** Does the app avoid encouraging consumption of tobacco and vape products, illegal drugs, or excessive amounts of alcohol?
  - quote: "Apps that encourage consumption of tobacco and vape products, illegal drugs, or excessive amounts of alcohol are not permitted."
  - surface: runtime
  - verify: Review content, game mechanics (e.g. drinking games), strings and App Store Connect metadata for encouragement of these substances.
  - fix: Remove or reframe content that encourages consumption.
- **[1.4.3-02]** Does the app avoid encouraging minors to consume any of these substances?
  - quote: "Apps that encourage minors to consume any of these substances will be rejected."
  - surface: manual
  - verify: Review target audience, age rating (App Store Connect > App Information > Age Rating) and any substance-related content reachable by minors.
  - fix: Remove such content; manual — requires developer decision on audience.
- **[1.4.3-03]** Does the app avoid facilitating the sale of controlled substances (except for licensed pharmacies and licensed or otherwise legal cannabis dispensaries), or tobacco?
  - quote: "Facilitating the sale of controlled substances (except for licensed pharmacies and licensed or otherwise legal cannabis dispensaries), or tobacco is not allowed."
  - surface: code
  - verify: Find commerce/ordering flows and product catalogs; check for tobacco/vape/controlled-substance listings or links; if the developer is a licensed pharmacy or legal dispensary, confirm licensing and note it in App Review Notes.
  - fix: Remove sale/ordering of tobacco or controlled substances unless the exception applies (manual — licensing is a business fact).

## 1.4.4 DUI checkpoints and reckless driving

**Source text (verbatim):**
> Apps may only display DUI checkpoints that are published by law enforcement agencies, and should never encourage drunk driving or other reckless behavior such as excessive speed.

**Applies to:** All apps (DUI checkpoint rule applies to apps that display DUI checkpoints)

- **[1.4.4-01]** If the app displays DUI checkpoints, are they only those published by law enforcement agencies?
  - quote: "Apps may only display DUI checkpoints that are published by law enforcement agencies"
  - surface: code
  - verify: Grep for checkpoint/DUI/police map features and trace the data source; confirm it is an official law-enforcement publication and not user-reported.
  - fix: Restrict checkpoint data to law-enforcement-published sources or remove the feature.
- **[1.4.4-02]** Does the app never encourage drunk driving or other reckless behavior such as excessive speed? (Guideline wording: “should never”.)
  - quote: "should never encourage drunk driving or other reckless behavior such as excessive speed"
  - surface: runtime
  - verify: Review driving-related features (speedometers, leaderboards for speed, challenges) and copy in the simulator and App Store Connect metadata.
  - fix: Remove speed rewards/encouragement and drunk-driving content; add safety messaging where relevant.

## 1.4.5 Activities that risk physical harm

**Source text (verbatim):**
> Apps should not urge customers to participate in activities (like bets, challenges, etc.) or use their devices in a way that risks physical harm to themselves or others.

**Applies to:** All apps

- **[1.4.5-01]** Does the app avoid urging customers to participate in activities (like bets, challenges, etc.) that risk physical harm to themselves or others? (Guideline wording: “should not”.)
  - quote: "Apps should not urge customers to participate in activities (like bets, challenges, etc.)"
  - surface: runtime
  - verify: Review challenge/dare/bet features, notifications and copy in the simulator for activities that risk physical harm.
  - fix: Remove or redesign harmful challenges.
- **[1.4.5-02]** Does the app avoid urging customers to use their devices in a way that risks physical harm to themselves or others? (Guideline wording: “should not”.)
  - quote: "or use their devices in a way that risks physical harm to themselves or others"
  - surface: runtime
  - verify: Review features requiring device use while moving, driving, or in hazardous conditions (e.g. AR games prompting movement, throwing/shaking the device); check for safety warnings.
  - fix: Remove harmful device-use prompts or add safeguards and warnings.

## 1.5 Developer Information

**Source text (verbatim):**
> People need to know how to reach you with questions and support issues. Make sure your app and its Support URL include an easy way to contact you; this is particularly important for apps that may be used in the classroom. Failure to include accurate and up-to-date contact information not only frustrates customers, but may violate the law in some countries or regions. Also ensure that Wallet passes include valid contact information from the issuer and are signed with a dedicated certificate assigned to the brand or trademark owner of the pass.

**Applies to:** All apps; the Wallet pass requirement applies to apps that provide Wallet passes

- **[1.5-01]** Does the app include an easy way to contact the developer?
  - quote: "Make sure your app and its Support URL include an easy way to contact you"
  - surface: runtime
  - verify: In the simulator, find an in-app Contact/Support/Help entry (email link, form, or support page) reachable from Settings/About; grep for `mailto:` or support URLs.
  - fix: Add an in-app Contact/Support entry with a working contact method.
- **[1.5-02]** Does the Support URL include an easy way to contact the developer?
  - quote: "its Support URL include an easy way to contact you"
  - surface: asc
  - verify: App Store Connect > version page > Support URL: open it and confirm it loads and shows contact information (email, form, or other contact method).
  - fix: Update the support page to include contact information, or change the Support URL to a page that does.
- **[1.5-03]** Is the contact information accurate and up-to-date?
  - quote: "Failure to include accurate and up-to-date contact information"
  - surface: manual
  - verify: Developer confirms the email/form/phone actually reach them (send a test message); compare in-app, Support URL and App Store Connect contact details for consistency.
  - fix: Update all contact details to current, monitored channels.
- **[1.5-04]** If the app provides Wallet passes, do they include valid contact information from the issuer?
  - quote: "ensure that Wallet passes include valid contact information from the issuer"
  - surface: code
  - verify: Grep for PassKit usage (`PKPass`, `PKAddPassesViewController`, `.pkpass` files, pass.json); inspect pass.json fields (e.g. back fields) for issuer contact information.
  - fix: Add valid issuer contact information to the pass (e.g. in back fields).
- **[1.5-05]** If the app provides Wallet passes, are they signed with a dedicated certificate assigned to the brand or trademark owner of the pass?
  - quote: "are signed with a dedicated certificate assigned to the brand or trademark owner of the pass"
  - surface: manual
  - verify: Check the pass's passTypeIdentifier/teamIdentifier in pass.json and the Pass Type ID certificate in the Apple Developer account (Certificates, Identifiers & Profiles); developer confirms it belongs to the brand/trademark owner.
  - fix: Sign passes with a Pass Type ID certificate owned by the brand/trademark owner; manual — requires developer/business action.

## 1.6 Data Security

**Source text (verbatim):**
> Apps should implement appropriate security measures to ensure proper handling of user information collected pursuant to the Apple Developer Program License Agreement and these Guidelines (see Guideline 5.1 for more information) and prevent its unauthorized use, disclosure, or access by third parties.

**Applies to:** Apps that collect user information

**Related:** Apple Developer Program License Agreement; Guideline 5.1

- **[1.6-01]** Does the app implement appropriate security measures to ensure proper handling of user information it collects? (Guideline wording: “should”.)
  - quote: "Apps should implement appropriate security measures to ensure proper handling of user information collected"
  - surface: code
  - verify: Check that credentials/tokens are stored in Keychain (not UserDefaults/plist/plain files); grep Info.plist for `NSAppTransportSecurity` with `NSAllowsArbitraryLoads` = YES; check file protection (`NSFileProtection*`, Data Protection entitlement); search for hard-coded API keys/secrets in source and bundled plists; check backend access rules (e.g. database security rules) for open read/write.
  - fix: Move secrets to Keychain, enforce HTTPS/ATS, enable data protection, remove hard-coded secrets, and lock down backend access rules.
- **[1.6-02]** Does the app prevent unauthorized use, disclosure, or access to user information by third parties? (Guideline wording: “should”.)
  - quote: "prevent its unauthorized use, disclosure, or access by third parties"
  - surface: code
  - verify: List third-party SDKs and the data passed to them; check logging (`print`, `NSLog`, `os_log` with `.public`) for personal data; confirm backend endpoints require authentication; cross-check App Store Connect > App Privacy and PrivacyInfo.xcprivacy against actual data flows (see 5.1).
  - fix: Stop passing user data to unnecessary third parties, redact logs, require authentication on endpoints, and align privacy disclosures.

## 1.7 Reporting Criminal Activity

**Source text (verbatim):**
> Apps for reporting alleged criminal activity must involve local law enforcement, and can only be offered in countries or regions where such involvement is active.

**Applies to:** Apps for reporting alleged criminal activity

- **[1.7-01]** Does the app for reporting alleged criminal activity involve local law enforcement?
  - quote: "Apps for reporting alleged criminal activity must involve local law enforcement"
  - surface: manual
  - verify: Developer documents the law enforcement partnership and where reports are routed; reference it in App Store Connect > App Review Information > Notes.
  - fix: manual — requires developer decision/legal/business action
- **[1.7-02]** Is the app offered only in countries or regions where law enforcement involvement is active?
  - quote: "can only be offered in countries or regions where such involvement is active"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > Country or Region Availability: compare selected territories with regions where law enforcement involvement is active.
  - fix: Restrict availability to regions with active law enforcement involvement.
