# App Review Guidelines — 5. Legal
Source: https://developer.apple.com/app-store/review/guidelines/#legal (App Review Guidelines, "Last Updated: October 16, 2026")  
Retrieved: 2026-10-30

## 5 Legal

**Source text (verbatim):**
> Apps must comply with all legal requirements in any location where you make them available (if you’re not sure, check with a lawyer). We know this stuff is complicated, but it is your responsibility to understand and make sure your app conforms with all local laws, not just the guidelines below. And of course, apps that solicit, promote, or encourage criminal or clearly reckless behavior will be rejected. In extreme cases, such as apps that are found to facilitate human trafficking and/or the exploitation of children, appropriate authorities will be notified and the apps will be removed from the App Store and blocked from alternative distribution.

**Applies to:** All apps

- **[5-01]** Has the developer confirmed the app complies with all legal requirements in every location (storefront) where it is made available?
  - quote: "Apps must comply with all legal requirements in any location where you make them available"
  - surface: manual
  - verify: In App Store Connect > Pricing and Availability, list the selected countries/regions; ask the developer to attest local-law compliance for each (consult a lawyer if unsure, as the text advises).
  - fix: manual — requires developer decision/legal/business action (obtain legal review, or remove storefronts where compliance is not confirmed in Pricing and Availability).
- **[5-02]** Is the app free of content or features that solicit, promote, or encourage criminal or clearly reckless behavior?
  - quote: "apps that solicit, promote, or encourage criminal or clearly reckless behavior will be rejected"
  - surface: runtime
  - verify: Exercise all main flows and review in-app copy, bundled content, and the App Store description/screenshots for content that solicits, promotes, or encourages criminal or clearly reckless behavior; grep localized strings (`*.strings`, `*.xcstrings`) for such content.
  - fix: Remove or rewrite the offending content/feature and matching metadata.
- **[5-03]** Is the app free of any functionality that facilitates human trafficking and/or the exploitation of children?
  - quote: "apps that are found to facilitate human trafficking and/or the exploitation of children"
  - surface: manual
  - verify: Developer attests; review user-generated-content, messaging and marketplace features for such use and for moderation controls.
  - fix: manual — requires developer decision/legal/business action (remove the functionality).

## 5.1 Privacy

**Source text (verbatim):**
> Protecting user privacy is paramount in the Apple ecosystem, and you should use care when handling personal data to ensure you’ve complied with privacy best practices, applicable laws, and the terms of the Apple Developer Program License Agreement, not to mention customer expectations. More particularly:

**Applies to:** All apps

**Related:** Apple Developer Program License Agreement

- **[5.1-01]** Has the developer confirmed personal-data handling complies with privacy best practices, applicable laws, and the terms of the Apple Developer Program License Agreement?
  - quote: "you should use care when handling personal data to ensure you’ve complied with privacy best practices, applicable laws, and the terms of the Apple Developer Program License Agreement"
  - surface: manual
  - verify: Inventory personal data the app handles (grep for networking, analytics SDKs, `PrivacyInfo.xcprivacy` `NSPrivacyCollectedDataTypes`) and ask the developer to attest legal/DPLA compliance; the specific requirements are checked under 5.1.1–5.1.5.
  - fix: manual — requires developer decision/legal/business action.

## 5.1.1 Data Collection and Storage

**Source text (verbatim):**
> - (i) Privacy Policies: All apps must include a link to their privacy policy in the App Store Connect metadata field and within the app in an easily accessible manner. The privacy policy must clearly and explicitly:
>   - Identify what data, if any, the app/service collects, how it collects that data, and all uses of that data.
>   - Confirm that any third party with whom an app shares user data (in compliance with these Guidelines)—such as analytics tools, advertising networks and third-party SDKs, as well as any parent, subsidiary or other related entities that will have access to user data—will provide the same or equal protection of user data as stated in the app’s privacy policy and required by these Guidelines.
>   - Explain its data retention/deletion policies and describe how a user can revoke consent and/or request deletion of the user’s data.
> - (ii) Permission: Apps that collect user or usage data must secure user consent for the collection, even if such data is considered to be anonymous at the time of or immediately following collection. Paid functionality must not be dependent on or require a user to grant access to this data. Apps must also provide the customer with an easily accessible and understandable way to withdraw consent. Ensure your purpose strings clearly and completely describe your use of the data. Learn more about writing clear purpose strings. Apps that collect data for a legitimate interest without consent by relying on the terms of the European Union’s General Data Protection Regulation (“GDPR”) or similar statute must comply with all terms of that law. Learn more about Requesting Permission.
> - (iii) Data Minimization: Apps should only request access to data relevant to the core functionality of the app and should only collect and use data that is required to accomplish the relevant task. Where possible, use the out-of-process picker or a share sheet rather than requesting full access to protected resources like Photos or Contacts.
> - (iv) Access: Apps must respect the user’s permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access. For example, apps that include the ability to post photos to a social network must not also require microphone access before allowing the user to upload photos. Where possible, provide alternative solutions for users who don’t grant consent. For example, if a user declines to share Location, offer the ability to manually enter an address.
> - (v) Account Sign-In: If your app doesn’t include significant account-based features, let people use it without a login. If your app supports account creation, you must also offer account deletion within the app. Apps may not require users to enter personal information to function, except when directly relevant to the core functionality of the app or required by law. If your core app functionality is not related to a specific social network (such as Facebook, WeChat, Weibo, X, etc.), you must provide access without a login or via another mechanism. Pulling basic profile information, sharing to the social network, or inviting friends to use the app are not considered core app functionality. The app must also include a mechanism to revoke social network credentials and disable data access between the app and social network from within the app. An app may not store credentials or tokens to social networks off of the device and may only use such credentials or tokens to directly connect to the social network from the app itself while the app is in use.
> - (vi) Developers that use their apps to surreptitiously discover passwords or other private data will be removed from the Apple Developer Program.
> - (vii) SafariViewController must be used to visibly present information to users; the controller may not be hidden or obscured by other views or layers. Additionally, an app may not use SafariViewController to track users without their knowledge and consent.
> - (viii) Apps that compile personal information from any source that is not directly from the user or without the user’s explicit consent, even public databases, are not permitted on the App Store or alternative distribution.
> - (ix) Apps that provide services in highly regulated fields (such as banking and financial services, healthcare, gambling, legal cannabis use, air travel and crypto exchanges) or that require sensitive user information should be submitted by a legal entity that provides the services, and not by an individual developer. Apps that facilitate the legal sale of cannabis must be geo-restricted to the corresponding legal jurisdiction.
> - (x) Apps may request basic contact information (such as name and email address) so long as the request is optional for the user, features and services are not conditional on providing the information, and it complies with all other provisions of these guidelines, including limitations on collecting information from kids.

**Applies to:** All apps ((i) applies to "All apps"; other items apply as stated in each item)

**Related:** writing clear purpose strings; Requesting Permission

- **[5.1.1-01]** (i) Is a privacy policy URL entered in the App Store Connect metadata field?
  - quote: "All apps must include a link to their privacy policy in the App Store Connect metadata field"
  - surface: asc
  - verify: App Store Connect > App > App Privacy > Privacy Policy URL is filled in and the URL loads (HTTP 200, actual policy content).
  - fix: Enter a working privacy policy URL in App Store Connect > App Privacy > Privacy Policy URL.
- **[5.1.1-02]** (i) Does the app itself include an easily accessible link to the privacy policy?
  - quote: "and within the app in an easily accessible manner"
  - surface: code
  - verify: Grep the project for the privacy policy URL or "Privacy Policy"/"privacy" in strings, Settings/About/Account screens, onboarding and paywall views (`Link(`, `openURL`, `SFSafariViewController`); confirm at runtime it is reachable within a couple of taps and opens the same policy as in App Store Connect.
  - fix: Add a "Privacy Policy" link (e.g. in Settings/About and on sign-up/paywall screens) that opens the policy URL.
- **[5.1.1-03]** (i) Does the privacy policy identify what data the app/service collects, how it collects that data, and all uses of that data?
  - quote: "Identify what data, if any, the app/service collects, how it collects that data, and all uses of that data."
  - surface: manual
  - verify: Read the policy; compare against the data actually collected (grep networking/analytics/SDK calls, `PrivacyInfo.xcprivacy` `NSPrivacyCollectedDataTypes`, App Store Connect App Privacy answers) and confirm every collected data type, its collection method and every use is listed.
  - fix: Update the privacy policy text to list all collected data, collection methods and uses (developer/legal must approve wording).
- **[5.1.1-04]** (i) Does the privacy policy confirm that every third party receiving user data (analytics tools, ad networks, third-party SDKs, and parent/subsidiary/related entities) will provide the same or equal protection of user data?
  - quote: "will provide the same or equal protection of user data as stated in the app’s privacy policy and required by these Guidelines"
  - surface: manual
  - verify: List third-party SDKs from `Package.resolved`, `Podfile.lock`, `Cartfile.resolved`, embedded frameworks; read the policy for a statement covering those third parties' equal protection of user data.
  - fix: Add the equal-protection statement for third parties to the policy (developer/legal must approve wording).
- **[5.1.1-05]** (i) Does the privacy policy explain data retention/deletion policies and describe how a user can revoke consent and/or request deletion of their data?
  - quote: "Explain its data retention/deletion policies and describe how a user can revoke consent and/or request deletion of the user’s data."
  - surface: manual
  - verify: Read the policy for a retention/deletion section and concrete instructions for revoking consent and requesting deletion.
  - fix: Add retention/deletion and consent-revocation/deletion-request sections to the policy (developer/legal must approve wording).
- **[5.1.1-06]** (ii) If the app collects user or usage data (even anonymous), does it secure user consent for the collection?
  - quote: "Apps that collect user or usage data must secure user consent for the collection, even if such data is considered to be anonymous at the time of or immediately following collection."
  - surface: runtime
  - verify: Grep for analytics/telemetry SDKs and custom event logging; launch a fresh install and confirm a consent prompt appears before any collection (observe network traffic before consent, e.g. via proxy or SDK debug logs).
  - fix: Gate SDK initialization and data collection behind an explicit consent prompt; do not send data until consent is given.
- **[5.1.1-07]** (ii) Is paid functionality available without requiring the user to grant access to user or usage data?
  - quote: "Paid functionality must not be dependent on or require a user to grant access to this data."
  - surface: runtime
  - verify: Decline data/permission prompts, then purchase or use paid features (StoreKit sandbox) and confirm they still work.
  - fix: Remove any dependency of paid features on data-access consent.
- **[5.1.1-08]** (ii) Does the app provide an easily accessible and understandable way to withdraw consent?
  - quote: "Apps must also provide the customer with an easily accessible and understandable way to withdraw consent."
  - surface: runtime
  - verify: Look for an in-app setting/toggle (grep for consent/analytics opt-out settings) that withdraws consent; confirm at runtime that toggling stops collection.
  - fix: Add a clearly labeled in-app setting to withdraw consent, wired to disable collection.
- **[5.1.1-09]** (ii) Do all purpose strings clearly and completely describe the app's use of the data?
  - quote: "Ensure your purpose strings clearly and completely describe your use of the data."
  - surface: code
  - verify: Inspect every `NS*UsageDescription` key in Info.plist / `INFOPLIST_KEY_NS*UsageDescription` build settings / `InfoPlist.xcstrings` (all localizations); each must state specifically what data is used and why (no placeholders, empty or generic text).
  - fix: Rewrite each purpose string to describe specifically what is accessed and how it is used, in every localization.
- **[5.1.1-10]** (ii) If the app collects data for a legitimate interest without consent under GDPR or a similar statute, has the developer confirmed compliance with all terms of that law?
  - quote: "Apps that collect data for a legitimate interest without consent by relying on the terms of the European Union’s General Data Protection Regulation (“GDPR”) or similar statute must comply with all terms of that law."
  - surface: manual
  - verify: Ask the developer whether any collection relies on legitimate interest rather than consent; if so, require attestation of full compliance with that law.
  - fix: manual — requires developer decision/legal/business action.
- **[5.1.1-11]** (iii) Does the app request access only to data relevant to its core functionality and collect/use only data required for the relevant task? (Apple says "should")
  - quote: "Apps should only request access to data relevant to the core functionality of the app and should only collect and use data that is required to accomplish the relevant task."
  - surface: code
  - verify: List all `NS*UsageDescription` keys, entitlements, and permission request calls (`requestAuthorization`, `requestAccess`, `requestWhenInUseAuthorization`, etc.); for each, find the feature that uses it and confirm it relates to core functionality. Flag keys/requests with no corresponding feature use.
  - fix: Remove unused permission requests, usage-description keys and entitlements; stop collecting unneeded data.
- **[5.1.1-12]** (iii) Where possible, does the app use the out-of-process picker or share sheet instead of requesting full access to Photos or Contacts?
  - quote: "Where possible, use the out-of-process picker or a share sheet rather than requesting full access to protected resources like Photos or Contacts."
  - surface: code
  - verify: Grep for `PHPhotoLibrary.requestAuthorization`, `PHAsset.fetch`, `CNContactStore().requestAccess`, `NSPhotoLibraryUsageDescription`, `NSContactsUsageDescription`; check whether the use case could use `PhotosPicker`/`PHPickerViewController`, `CNContactPickerViewController`, or `UIActivityViewController`/`ShareLink`.
  - fix: Replace full-library access with `PhotosPicker`/`PHPickerViewController`, `CNContactPickerViewController`, or a share sheet, and remove the now-unneeded usage-description key.
- **[5.1.1-13]** (iv) Does the app respect the user's permission settings and avoid manipulating, tricking, or forcing consent to unnecessary data access (e.g., not requiring microphone access to upload photos)?
  - quote: "Apps must respect the user’s permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access."
  - surface: runtime
  - verify: Deny each permission and confirm unrelated features still work; check that no flow blocks progress until an unrelated permission is granted, and that pre-permission screens do not mislead or pressure (review copy around permission requests in code).
  - fix: Decouple features from unrelated permissions; request permissions only when the related feature is used; remove manipulative pre-prompt copy.
- **[5.1.1-14]** (iv) Where possible, does the app offer an alternative when the user doesn't grant consent (e.g., manual address entry if Location is declined)?
  - quote: "Where possible, provide alternative solutions for users who don’t grant consent."
  - surface: runtime
  - verify: Deny each permission (Location, Photos, Contacts, Camera, etc.) and check for a fallback path (manual entry, picker, etc.); in code, inspect `.denied`/`.restricted` authorization handling.
  - fix: Implement fallbacks for denied permissions (e.g. manual address entry for Location).
- **[5.1.1-15]** (v) If the app doesn't include significant account-based features, can people use it without a login?
  - quote: "If your app doesn’t include significant account-based features, let people use it without a login."
  - surface: runtime
  - verify: Fresh install: check whether a login wall blocks use; if so, determine which features genuinely require an account.
  - fix: Allow use without login for non-account features (guest mode / defer sign-in until an account feature is used).
- **[5.1.1-16]** (v) If the app supports account creation, does it offer account deletion within the app?
  - quote: "If your app supports account creation, you must also offer account deletion within the app."
  - surface: code
  - verify: Grep for sign-up/registration flows (`createUser`, `signUp`, `ASAuthorizationAppleIDProvider`, Firebase/Supabase auth); then grep for an in-app delete-account action (e.g. "Delete Account") that calls a backend deletion endpoint; confirm at runtime it is reachable and completes.
  - fix: Add an in-app "Delete Account" flow (e.g. in Account settings) that deletes the account via the backend.
- **[5.1.1-17]** (v) Does the app avoid requiring personal information to function, except when directly relevant to core functionality or required by law?
  - quote: "Apps may not require users to enter personal information to function, except when directly relevant to the core functionality of the app or required by law."
  - surface: runtime
  - verify: Walk onboarding/sign-up; list every required personal-information field (name, birthday, phone, gender, etc.) and confirm each is core-relevant or legally required; inspect form validation code for required fields.
  - fix: Make non-essential personal-information fields optional or remove them.
- **[5.1.1-18]** (v) If core functionality isn't related to a specific social network, does the app provide access without a login or via another mechanism (not only social-network login)?
  - quote: "If your core app functionality is not related to a specific social network (such as Facebook, WeChat, Weibo, X, etc.), you must provide access without a login or via another mechanism."
  - surface: code
  - verify: Grep for social login SDKs (FacebookLogin, WeChat, Weibo, X/Twitter auth); if social login is the only sign-in option and the app's core functionality isn't about that network, flag it.
  - fix: Add access without login or another sign-in mechanism (e.g. email or Sign in with Apple).
- **[5.1.1-19]** (v) Does the app include an in-app mechanism to revoke social network credentials and disable data access between the app and the social network?
  - quote: "The app must also include a mechanism to revoke social network credentials and disable data access between the app and social network from within the app."
  - surface: code
  - verify: If social network integration exists, grep for a disconnect/logout/unlink action that clears stored tokens (Keychain) and calls the SDK's logout; confirm at runtime.
  - fix: Add an in-app "Disconnect <network>" action that revokes/clears credentials and stops data access.
- **[5.1.1-20]** (v) Does the app avoid storing social network credentials/tokens off the device, using them only to connect directly from the app while in use?
  - quote: "An app may not store credentials or tokens to social networks off of the device and may only use such credentials or tokens to directly connect to the social network from the app itself while the app is in use."
  - surface: code
  - verify: Trace where social tokens go: confirm they are stored locally (Keychain) and not uploaded to your backend/iCloud (check API payloads, `NSUbiquitousKeyValueStore`, CloudKit, keychain `kSecAttrSynchronizable`); check background tasks don't use them.
  - fix: Stop transmitting/storing social tokens off-device; use them only from the app in the foreground.
- **[5.1.1-21]** (vi) Is the app free of any code that surreptitiously discovers passwords or other private data?
  - quote: "Developers that use their apps to surreptitiously discover passwords or other private data will be removed from the Apple Developer Program."
  - surface: code
  - verify: Grep for keystroke capture, pasteboard harvesting (`UIPasteboard.general` reads without user action), web-view credential scraping (JS injection reading form fields), and uploads of data not disclosed to users.
  - fix: Remove the surreptitious collection code.
- **[5.1.1-22]** (vii) Is SafariViewController always visibly presented and never hidden or obscured by other views or layers?
  - quote: "SafariViewController must be used to visibly present information to users; the controller may not be hidden or obscured by other views or layers."
  - surface: code
  - verify: Grep for `SFSafariViewController`; check it is presented normally (`present(...)`) and not added off-screen, with zero alpha/size, or covered by overlay views.
  - fix: Present SFSafariViewController visibly and remove any hiding/overlaying.
- **[5.1.1-23]** (vii) Is SafariViewController never used to track users without their knowledge and consent?
  - quote: "an app may not use SafariViewController to track users without their knowledge and consent"
  - surface: code
  - verify: Inspect URLs loaded in `SFSafariViewController` for tracking/attribution endpoints opened without user action or consent.
  - fix: Remove covert SafariViewController tracking loads, or obtain informed consent first.
- **[5.1.1-24]** (viii) Does the app avoid compiling personal information from sources not directly from the user or without the user's explicit consent (even public databases)?
  - quote: "Apps that compile personal information from any source that is not directly from the user or without the user’s explicit consent, even public databases, are not permitted"
  - surface: manual
  - verify: Review backend/data sources the app uses (APIs, scraped/public databases, data brokers) for personal information about people not supplied by them; developer attests.
  - fix: manual — requires developer decision/legal/business action (remove such data sources/features).
- **[5.1.1-25]** (ix) If the app provides services in a highly regulated field (banking/financial, healthcare, gambling, legal cannabis, air travel, crypto exchanges) or requires sensitive user information, is it submitted by a legal entity that provides the services rather than an individual developer? (Apple says "should")
  - quote: "should be submitted by a legal entity that provides the services, and not by an individual developer"
  - surface: asc
  - verify: Determine the app's field from its features/category; in App Store Connect / developer account, check the seller/developer name is an organization (not an individual) and is the entity providing the service.
  - fix: manual — requires developer decision/legal/business action (enroll/transfer to the organization account that provides the service).
- **[5.1.1-26]** (ix) If the app facilitates the legal sale of cannabis, is it geo-restricted to the corresponding legal jurisdiction?
  - quote: "Apps that facilitate the legal sale of cannabis must be geo-restricted to the corresponding legal jurisdiction."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability: only legal jurisdictions selected; in code, check for in-app geo-restriction (location/region checks) for sub-national jurisdictions.
  - fix: Restrict availability in App Store Connect and add in-app geo-restriction to the legal jurisdiction.
- **[5.1.1-27]** (x) If the app requests basic contact information (name, email), is the request optional with no features or services conditional on providing it?
  - quote: "so long as the request is optional for the user, features and services are not conditional on providing the information"
  - surface: runtime
  - verify: Find screens asking for name/email (grep for email/name text fields, newsletter prompts); confirm they can be skipped and that skipping does not lock features.
  - fix: Make the contact-info request optional (add Skip) and remove feature gating on it.

## 5.1.2 Data Use and Sharing

**Source text (verbatim):**
> - (i) Unless otherwise permitted by law, you may not use, transmit, or share someone’s personal data without first obtaining their permission. You must provide access to information about how and where the data will be used. You must clearly disclose where personal data will be shared with third parties, including with third-party AI, and obtain explicit permission before doing so. Data collected from apps may only be shared with third parties to improve the app or serve advertising (in compliance with the Apple Developer Program License Agreement). You must receive explicit permission from users via the App Tracking Transparency APIs to track their activity. Learn more about tracking. Your app may not require users to enable system functionalities (such as push notifications, location services, tracking) in order to access functionality, content, use the app, or receive monetary or other compensation, including but not limited to gift cards and codes. Apps that share user data without user consent or otherwise complying with data privacy laws may be removed from sale and may result in your removal from the Apple Developer Program.
> - (ii) Data collected for one purpose may not be repurposed without further consent unless otherwise explicitly permitted by law.
> - (iii) Apps should not attempt to surreptitiously build a user profile based on collected data and may not attempt, facilitate, or encourage others to identify anonymous users or reconstruct user profiles based on data collected from Apple-provided APIs or any data that you say has been collected in an “anonymized,” “aggregated,” or otherwise non-identifiable way.
> - (iv) Do not use information from Contacts, Photos, or other APIs that access user data to build a contact database for your own use or for sale/distribution to third parties, and don’t collect information about which other apps are installed on a user’s device for the purposes of analytics or advertising/marketing.
> - (v) Do not contact people using information collected via a user’s Contacts or Photos, except at the explicit initiative of that user on an individualized basis; do not include a Select All option or default the selection of all contacts. You must provide the user with a clear description of how the message will appear to the recipient before sending it (for example, What will the message say? Who will appear to be the sender?).
> - (vi) Data gathered from the HomeKit API, HealthKit, Clinical Health Records API, MovementDisorder APIs, ClassKit or from depth and/or facial mapping tools (such as ARKit, Camera APIs, or Photo APIs) may not be used for marketing, advertising or use-based data mining, including by third parties. Learn more about best practices for implementing CallKit, HealthKit, ClassKit, and ARKit.
> - (vii) Apps using Apple Pay may only share user data acquired via Apple Pay with third parties to facilitate or improve delivery of goods and services.

**Applies to:** All apps that use, transmit, or share personal data (items (vi) and (vii) apply to apps using the named APIs / Apple Pay)

**Related:** Apple Developer Program License Agreement; App Tracking Transparency APIs; tracking; best practices for implementing CallKit, HealthKit, ClassKit, and ARKit

- **[5.1.2-01]** (i) Does the app obtain permission before using, transmitting, or sharing someone's personal data (unless otherwise permitted by law)?
  - quote: "you may not use, transmit, or share someone’s personal data without first obtaining their permission"
  - surface: runtime
  - verify: Fresh install with network inspection: confirm no personal data is sent before a permission/consent step; grep for network calls in app launch paths and SDK init in `App`/`AppDelegate`.
  - fix: Defer transmission/sharing of personal data until permission is obtained.
- **[5.1.2-02]** (i) Does the app provide access to information about how and where data will be used?
  - quote: "You must provide access to information about how and where the data will be used."
  - surface: runtime
  - verify: Confirm the in-app privacy policy link and/or in-context disclosures explain how and where data is used.
  - fix: Add an in-app disclosure/privacy-policy link describing how and where data is used.
- **[5.1.2-03]** (i) Does the app clearly disclose where personal data is shared with third parties, including third-party AI, and obtain explicit permission before sharing?
  - quote: "You must clearly disclose where personal data will be shared with third parties, including with third-party AI, and obtain explicit permission before doing so."
  - surface: code
  - verify: Grep for calls to third-party services and AI APIs (e.g. `api.openai.com`, `api.anthropic.com`, `generativelanguage.googleapis.com`, other LLM/AI SDKs, analytics/ads SDKs); for each that receives personal data or user content, confirm an in-app disclosure naming the third party and an explicit opt-in shown before the first send.
  - fix: Add a disclosure naming the third party (incl. AI provider) and an explicit permission prompt before the first transfer; block sending until accepted.
- **[5.1.2-04]** (i) Is data shared with third parties only to improve the app or serve advertising?
  - quote: "Data collected from apps may only be shared with third parties to improve the app or serve advertising"
  - surface: manual
  - verify: List all third-party recipients (SDKs, backends) and their purposes; developer attests no other purpose (e.g. selling data to brokers).
  - fix: manual — requires developer decision/legal/business action (stop disallowed sharing).
- **[5.1.2-05]** (i) If the app tracks user activity, does it receive explicit permission via the App Tracking Transparency APIs?
  - quote: "You must receive explicit permission from users via the App Tracking Transparency APIs to track their activity."
  - surface: code
  - verify: Check for tracking (IDFA `ASIdentifierManager.advertisingIdentifier`, ad/attribution SDKs, cross-app data linking; `NSPrivacyTracking` = true in `PrivacyInfo.xcprivacy`); if present, confirm `ATTrackingManager.requestTrackingAuthorization` is called before tracking, `NSUserTrackingUsageDescription` exists in Info.plist, and tracking only happens when status is `.authorized`.
  - fix: Add `NSUserTrackingUsageDescription`, call `ATTrackingManager.requestTrackingAuthorization` before tracking, and gate tracking SDKs on `.authorized`.
- **[5.1.2-06]** (i) Does the app avoid requiring users to enable system functionalities (push notifications, location services, tracking) to access functionality, content, use the app, or receive compensation (incl. gift cards and codes)?
  - quote: "Your app may not require users to enable system functionalities (such as push notifications, location services, tracking) in order to access functionality, content, use the app, or receive monetary or other compensation"
  - surface: runtime
  - verify: Deny notifications, location and tracking prompts; confirm the app remains usable and no content/reward is withheld; grep for code that blocks flows when `authorizationStatus` is denied.
  - fix: Remove gating on these permissions; keep the app/rewards available when they are denied.
- **[5.1.2-07]** (ii) Is data collected for one purpose not repurposed without further consent (unless explicitly permitted by law)?
  - quote: "Data collected for one purpose may not be repurposed without further consent unless otherwise explicitly permitted by law."
  - surface: manual
  - verify: Compare stated purposes (purpose strings, consent screens, privacy policy) with actual uses in code/backend; developer attests.
  - fix: Obtain additional consent before using data for a new purpose, or stop the new use.
- **[5.1.2-08]** (iii) Does the app avoid surreptitiously building user profiles (Apple says "should not"), and does it never attempt, facilitate, or encourage others to identify anonymous users or reconstruct user profiles from Apple-API data or “anonymized”/“aggregated” data ("may not")?
  - quote: "Apps should not attempt to surreptitiously build a user profile based on collected data and may not attempt, facilitate, or encourage others to identify anonymous users or reconstruct user profiles"
  - surface: code
  - verify: Grep for fingerprinting signals (device model + locale + timezone + disk/uptime combinations, `identifierForVendor` linked across contexts, `systemUptime`) and for joining "anonymous" data with identifiers.
  - fix: Remove fingerprinting/re-identification logic.
- **[5.1.2-09]** (iv) Does the app avoid using Contacts, Photos, or other user-data APIs to build a contact database for its own use or for sale/distribution?
  - quote: "Do not use information from Contacts, Photos, or other APIs that access user data to build a contact database for your own use or for sale/distribution to third parties"
  - surface: code
  - verify: Grep for `CNContactStore` enumeration (`enumerateContacts`, `unifiedContacts`) and check whether contact data is uploaded/stored server-side beyond the user-initiated feature.
  - fix: Stop uploading/storing contact data into a database; use only for the user-initiated action.
- **[5.1.2-10]** (iv) Does the app avoid collecting which other apps are installed on the device for analytics or advertising/marketing?
  - quote: "don’t collect information about which other apps are installed on a user’s device for the purposes of analytics or advertising/marketing"
  - surface: code
  - verify: Grep for `canOpenURL` loops and `LSApplicationQueriesSchemes` lists in Info.plist used to probe installed apps, and whether results are logged/sent to analytics or ad SDKs.
  - fix: Remove installed-app probing and its reporting; trim `LSApplicationQueriesSchemes` to schemes actually needed for functionality.
- **[5.1.2-11]** (v) Does the app contact people from the user's Contacts or Photos only at the user's explicit, individualized initiative, with no Select All option and no default selection of all contacts?
  - quote: "Do not contact people using information collected via a user’s Contacts or Photos, except at the explicit initiative of that user on an individualized basis; do not include a Select All option or default the selection of all contacts."
  - surface: runtime
  - verify: Exercise invite/share-with-contacts flows: confirm each recipient is chosen individually, no "Select All", nothing pre-selected, and no automatic messages; inspect the contact-selection UI code.
  - fix: Remove Select All / default-all selection and automatic sends; require per-contact user selection.
- **[5.1.2-12]** (v) Before sending a message to a contact, does the app clearly show how the message will appear to the recipient (content and sender)?
  - quote: "You must provide the user with a clear description of how the message will appear to the recipient before sending it"
  - surface: runtime
  - verify: Trigger an invite/message flow and confirm a preview of message text and apparent sender before send (e.g. `MFMessageComposeViewController` pre-filled or an explicit preview screen).
  - fix: Add a preview showing message text and sender before sending.
- **[5.1.2-13]** (vi) Is data from HomeKit, HealthKit, Clinical Health Records, MovementDisorder APIs, ClassKit, or depth/facial mapping tools (ARKit, Camera APIs, Photo APIs) never used for marketing, advertising, or use-based data mining, including by third parties?
  - quote: "may not be used for marketing, advertising or use-based data mining, including by third parties"
  - surface: code
  - verify: Grep for `HomeKit`, `HealthKit`/`HKHealthStore`, `HKClinicalRecord`, `CMMovementDisorderManager`, `ClassKit`, `ARKit`/`ARFaceAnchor`, depth data (`AVDepthData`); trace whether that data flows to analytics/ad SDKs or marketing backends.
  - fix: Stop sending such data to analytics/advertising/marketing destinations.
- **[5.1.2-14]** (vii) If the app uses Apple Pay, is user data acquired via Apple Pay shared with third parties only to facilitate or improve delivery of goods and services?
  - quote: "may only share user data acquired via Apple Pay with third parties to facilitate or improve delivery of goods and services"
  - surface: code
  - verify: Grep for `PKPaymentAuthorizationController`/`PKPaymentRequest`/`PayWithApplePayButton`; trace where `PKPayment` contact/shipping data goes and confirm only payment/fulfillment recipients receive it.
  - fix: Stop sharing Apple Pay data with recipients not involved in delivering the goods/services.

## 5.1.3 Health and Health Research

**Source text (verbatim):**
> Health, fitness, and medical data are especially sensitive and apps in this space have some additional rules to make sure customer privacy is protected:
> - (i) Apps may not use or disclose to third parties data gathered in the health, fitness, and medical research context—including from the Clinical Health Records API, HealthKit API, Motion and Fitness, MovementDisorder APIs, or health-related human subject research—for advertising, marketing, or other use-based data mining purposes other than improving health management, or for the purpose of health research, and then only with permission. Apps may, however, use a user’s health or fitness data to provide a benefit directly to that user (such as a reduced insurance premium), provided that the app is submitted by the entity providing the benefit, and the data is not shared with a third party. You must disclose the specific health data that you are collecting from the device.
> - (ii) Apps must not write false or inaccurate data into HealthKit or any other medical research or health management apps, and may not store personal health information in iCloud.
> - (iii) Apps conducting health-related human subject research must obtain consent from participants or, in the case of minors, their parent or guardian. Such consent must include the (a) nature, purpose, and duration of the research; (b) procedures, risks, and benefits to the participant; (c) information about confidentiality and handling of data (including any sharing with third parties); (d) a point of contact for participant questions; and (e) the withdrawal process.
> - (iv) Apps conducting health-related human subject research must secure approval from an independent ethics review board. Proof of such approval must be provided upon request.

**Applies to:** Apps handling health, fitness, and medical data (incl. Clinical Health Records API, HealthKit API, Motion and Fitness, MovementDisorder APIs); (iii)–(iv) apps conducting health-related human subject research

- **[5.1.3-01]** (i) Is health/fitness/medical research data never used or disclosed to third parties for advertising, marketing, or use-based data mining (other than improving health management or health research, and then only with permission)?
  - quote: "for advertising, marketing, or other use-based data mining purposes other than improving health management, or for the purpose of health research, and then only with permission"
  - surface: code
  - verify: Grep for `HKHealthStore`, `HKClinicalRecord`, `CMMotionActivityManager`/`CMPedometer`, `CMMovementDisorderManager`, ResearchKit; trace data flows to analytics/ad SDKs and third-party endpoints.
  - fix: Remove flows of health data to advertising/marketing/data-mining destinations; gate permitted research/health-management uses behind explicit permission.
- **[5.1.3-02]** (i) If the app uses health/fitness data to give the user a benefit (e.g., reduced insurance premium), is it submitted by the entity providing the benefit and is the data not shared with a third party?
  - quote: "provided that the app is submitted by the entity providing the benefit, and the data is not shared with a third party"
  - surface: manual
  - verify: Confirm the App Store Connect seller is the benefit provider; trace health data destinations to confirm no third-party sharing.
  - fix: manual — requires developer decision/legal/business action.
- **[5.1.3-03]** (i) Does the app disclose the specific health data it collects from the device?
  - quote: "You must disclose the specific health data that you are collecting from the device."
  - surface: code
  - verify: List `HKObjectType`s in `requestAuthorization(toShare:read:)`; confirm `NSHealthShareUsageDescription`/`NSHealthUpdateUsageDescription` and the privacy policy / App Store Connect App Privacy (Health & Fitness) disclose those specific types.
  - fix: Update purpose strings, privacy policy and App Privacy answers to list the specific health data types collected.
- **[5.1.3-04]** (ii) Does the app avoid writing false or inaccurate data into HealthKit or other medical research/health management apps?
  - quote: "Apps must not write false or inaccurate data into HealthKit or any other medical research or health management apps"
  - surface: code
  - verify: Grep for `HKHealthStore().save`, `HKQuantitySample`, `HKCategorySample` writes; confirm values come from real measurements/user entry (no demo/random/placeholder data written).
  - fix: Remove fabricated or test writes; only write accurate measured or user-entered data.
- **[5.1.3-05]** (ii) Does the app avoid storing personal health information in iCloud?
  - quote: "may not store personal health information in iCloud"
  - surface: code
  - verify: Check entitlements for `com.apple.developer.icloud-container-identifiers`/CloudKit/ubiquity-kvstore; grep for `CKRecord`, `NSPersistentCloudKitContainer`, `NSUbiquitousKeyValueStore`, iCloud Drive document storage, and SwiftData `cloudKitDatabase`; confirm no health data models sync to iCloud.
  - fix: Exclude health data from CloudKit/iCloud sync (separate local-only store or `cloudKitDatabase: .none` for those models).
- **[5.1.3-06]** (iii) If conducting health-related human subject research, does the app obtain consent from participants (or parent/guardian for minors) that includes nature, purpose, duration; procedures, risks, benefits; confidentiality and data handling incl. third-party sharing; a point of contact; and the withdrawal process?
  - quote: "Apps conducting health-related human subject research must obtain consent from participants or, in the case of minors, their parent or guardian. Such consent must include the (a) nature, purpose, and duration of the research; (b) procedures, risks, and benefits to the participant; (c) information about confidentiality and handling of data (including any sharing with third parties); (d) a point of contact for participant questions; and (e) the withdrawal process."
  - surface: runtime
  - verify: Walk the enrollment flow (e.g. ResearchKit `ORKConsentDocument`/`ORKConsentSection` in code); confirm each of the five elements (a)–(e) is present and that minors' consent goes to a parent/guardian.
  - fix: Add a consent flow covering items (a)–(e), with parent/guardian consent for minors.
- **[5.1.3-07]** (iv) If conducting health-related human subject research, has the app secured approval from an independent ethics review board, with proof available on request?
  - quote: "must secure approval from an independent ethics review board. Proof of such approval must be provided upon request."
  - surface: manual
  - verify: Developer provides the ethics board approval document; consider noting it in App Store Connect > App Review Information > Notes.
  - fix: manual — requires developer decision/legal/business action (obtain IRB/ethics approval).

## 5.1.4 Kids

**Source text (verbatim):**
> - (a) For many reasons, it is critical to use care when dealing with personal data from kids, and we encourage you to carefully review all the requirements for complying with laws like the Children’s Online Privacy Protection Act (“COPPA”), the European Union’s General Data Protection Regulation (“GDPR”), and any other applicable regulations or laws.
>
>   Apps may ask for birthdate and parental contact information only for the purpose of complying with these statutes, but must include some useful functionality or entertainment value regardless of a person’s age.
>
>   Apps intended primarily for kids should not include third-party analytics or third-party advertising. This provides a safer experience for kids.
> - (b) In limited cases, third-party analytics and third-party advertising may be permitted provided that the services adhere to the same terms set forth in Guideline 1.3.
>
>   Moreover, apps in the Kids Category or those that collect, transmit, or have the capability to share personal information (such as name, address, email, location, photos, videos, drawings, the ability to chat, other personal data, or persistent identifiers used in combination with any of the above) from a minor must include a privacy policy and must comply with all applicable children’s privacy statutes. For the sake of clarity, the parental gate requirement for the Kid’s Category is generally not the same as securing parental consent to collect personal data under these privacy statutes.
>
>   As a reminder, Guideline 2.3.8 requires that use of terms like “For Kids” and “For Children” in app metadata is reserved for the Kids Category. Apps not in the Kids Category cannot include any terms in app name, subtitle, icon, screenshots or description that imply the main audience for the app is children.

**Applies to:** Apps dealing with personal data from kids; apps intended primarily for kids; apps in the Kids Category or that collect, transmit, or can share personal information from a minor; all apps not in the Kids Category (metadata reminder)

**Related:** Children’s Online Privacy Protection Act (“COPPA”); General Data Protection Regulation (“GDPR”); Guideline 1.3; Guideline 2.3.8

- **[5.1.4-01]** If the app deals with personal data from kids, has the developer reviewed requirements under COPPA, GDPR, and other applicable laws? (Apple "encourage[s]" this — advisory, not a hard rule)
  - quote: "we encourage you to carefully review all the requirements for complying with laws like the Children’s Online Privacy Protection Act (“COPPA”), the European Union’s General Data Protection Regulation (“GDPR”), and any other applicable regulations or laws"
  - surface: manual
  - verify: Ask the developer whether the app may handle kids' personal data and whether COPPA/GDPR requirements were reviewed.
  - fix: manual — requires developer decision/legal/business action.
- **[5.1.4-02]** If the app asks for birthdate or parental contact information, is it only for complying with these statutes?
  - quote: "Apps may ask for birthdate and parental contact information only for the purpose of complying with these statutes"
  - surface: code
  - verify: Grep for birthdate/age pickers (`DatePicker` for birthday, "birth", "age") and parent email/phone fields; confirm the data is used only for age-gating/parental consent, not marketing/profiling.
  - fix: Restrict use of birthdate/parental contact info to statutory compliance, or remove the fields.
- **[5.1.4-03]** Does the app include some useful functionality or entertainment value regardless of a person's age?
  - quote: "must include some useful functionality or entertainment value regardless of a person’s age"
  - surface: runtime
  - verify: Enter an under-age birthdate at any age gate and confirm the app still offers some useful functionality or entertainment rather than a dead end.
  - fix: Provide a usable (e.g. limited, non-data-collecting) experience for users of any age.
- **[5.1.4-04]** If the app is intended primarily for kids, is it free of third-party analytics and third-party advertising (unless the limited exception under Guideline 1.3 applies)? (Apple says "should")
  - quote: "Apps intended primarily for kids should not include third-party analytics or third-party advertising."
  - surface: code
  - verify: If primarily for kids (Kids Category in ASC, or audience), list SDKs in `Package.resolved`/`Podfile.lock`/frameworks and flag analytics/ads SDKs (e.g. Firebase Analytics, Google Mobile Ads, Meta Audience Network, AppsFlyer, Adjust, Mixpanel, Amplitude); for any retained, confirm they adhere to Guideline 1.3's terms.
  - fix: Remove third-party analytics/ads SDKs, or keep only services that adhere to Guideline 1.3's terms.
- **[5.1.4-05]** If the app is in the Kids Category or collects, transmits, or can share personal information from a minor (incl. chat, photos, persistent identifiers combined with such data), does it include a privacy policy and comply with all applicable children's privacy statutes?
  - quote: "must include a privacy policy and must comply with all applicable children’s privacy statutes"
  - surface: asc
  - verify: Check App Store Connect > App Information for Kids Category / age rating; check Privacy Policy URL is set; ask developer to attest children's privacy statute compliance (e.g. verifiable parental consent where required).
  - fix: Add a privacy policy (ASC + in-app); manual — requires developer decision/legal/business action for statutory compliance.
- **[5.1.4-06]** If the app is in the Kids Category, has the developer accounted for the fact that the parental gate is generally not the same as securing parental consent to collect personal data?
  - quote: "the parental gate requirement for the Kid’s Category is generally not the same as securing parental consent to collect personal data under these privacy statutes"
  - surface: manual
  - verify: If the app collects minors' personal data, confirm a statutory parental-consent mechanism exists separately from any parental gate.
  - fix: manual — requires developer decision/legal/business action (implement a statute-compliant parental consent process).
- **[5.1.4-07]** If the app is not in the Kids Category, is its name, subtitle, icon, screenshots, and description free of terms (e.g., “For Kids”, “For Children”) implying the main audience is children?
  - quote: "Apps not in the Kids Category cannot include any terms in app name, subtitle, icon, screenshots or description that imply the main audience for the app is children."
  - surface: asc
  - verify: In App Store Connect, for every localization, review App Name, Subtitle, Description, screenshots and the app icon for terms like “For Kids”/“For Children” or other child-audience implications; also check `CFBundleDisplayName`.
  - fix: Remove child-audience terms from metadata/icon/screenshots, or move the app to the Kids Category.

## 5.1.5 Location Services

**Source text (verbatim):**
> Use Location Services in your app only when it is directly relevant to the features and services provided by the app. Location-based APIs shouldn’t be used to provide emergency services or autonomous control over vehicles, aircraft, and other devices, except for small devices such as lightweight drones and toys, or remote control car alarm systems, etc. Ensure that you notify and obtain consent before collecting, transmitting, or using location data. If your app uses Location Services, be sure to explain the purpose in your app; refer to the Human Interface Guidelines for best practices for doing so.

**Applies to:** Apps that use Location Services

**Related:** Human Interface Guidelines

- **[5.1.5-01]** Is Location Services used only when directly relevant to the app's features and services?
  - quote: "Use Location Services in your app only when it is directly relevant to the features and services provided by the app."
  - surface: code
  - verify: Grep for `CLLocationManager`, `CLLocationUpdate`, `CLMonitor`, `requestWhenInUseAuthorization`/`requestAlwaysAuthorization`, `NSLocation*UsageDescription` keys and `UIBackgroundModes` `location`; map each use to a user-facing feature. Flag "Always" access or background location with no feature needing it.
  - fix: Remove unneeded location use, background mode and usage-description keys; downgrade to When In Use where sufficient.
- **[5.1.5-02]** Are location-based APIs not used to provide emergency services or autonomous control over vehicles, aircraft, and other devices (except small devices like lightweight drones, toys, or remote control car alarm systems)? (Apple says "shouldn’t")
  - quote: "Location-based APIs shouldn’t be used to provide emergency services or autonomous control over vehicles, aircraft, and other devices"
  - surface: manual
  - verify: Review app purpose and location-driven features; developer attests.
  - fix: manual — requires developer decision/legal/business action.
- **[5.1.5-03]** Does the app notify and obtain consent before collecting, transmitting, or using location data?
  - quote: "Ensure that you notify and obtain consent before collecting, transmitting, or using location data."
  - surface: runtime
  - verify: Fresh install: confirm no location is read or sent before the system authorization prompt is accepted; check code reads location only when `authorizationStatus` is authorized, and that IP/other geolocation isn't sent before consent.
  - fix: Request authorization (with explanation) before any location collection/transmission.
- **[5.1.5-04]** Does the app explain the purpose of its location use in the app?
  - quote: "If your app uses Location Services, be sure to explain the purpose in your app"
  - surface: code
  - verify: Check `NSLocationWhenInUseUsageDescription` (and `NSLocationAlwaysAndWhenInUseUsageDescription` if used) exist and explain the purpose specifically, in all localizations; optionally check for in-context explanation (the text refers to the HIG for best practices).
  - fix: Write specific location purpose strings; follow HIG best practices for explaining location use.

## 5.2 Intellectual Property

**Source text (verbatim):**
> Make sure your app only includes content that you created or that you have a license to use. Your app may be removed if you’ve stepped over the line and used content without permission. Of course, this also means someone else’s app may be removed if they’ve “borrowed” from your work. If you believe your intellectual property has been infringed by another developer on the App Store, submit a claim via our web form. Laws differ in different countries and regions, but at the very least, make sure to avoid the following common errors:

**Applies to:** All apps

**Related:** web form (intellectual property claim)

- **[5.2-01]** Does the app only include content the developer created or has a license to use?
  - quote: "Make sure your app only includes content that you created or that you have a license to use."
  - surface: code
  - verify: Inventory bundled assets (`Assets.xcassets`, fonts, audio, video, images, 3D models, bundled data) and third-party code licenses (`Package.resolved` dependencies, vendored code LICENSE files); ask the developer to confirm source/license for each asset not created in-house.
  - fix: Replace unlicensed content with original or properly licensed content; add required license attributions (e.g. an Acknowledgements screen).

## 5.2.1 Generally

**Source text (verbatim):**
> Generally: Don’t use protected third-party material such as trademarks, copyrighted works, or patented ideas in your app without permission, and don’t include misleading, false, or copycat representations, names, or metadata in your app bundle or developer name. Apps should be submitted by the person or legal entity that owns or has licensed the intellectual property and other relevant rights.

**Applies to:** All apps

- **[5.2.1-01]** Is the app free of protected third-party material (trademarks, copyrighted works, patented ideas) used without permission?
  - quote: "Don’t use protected third-party material such as trademarks, copyrighted works, or patented ideas in your app without permission"
  - surface: manual
  - verify: Review app name, icon, screenshots, bundled assets and in-app text for third-party brand names/logos/characters/copyrighted media; developer provides permission for any found.
  - fix: Remove or replace the third-party material, or obtain written permission.
- **[5.2.1-02]** Are the app bundle, metadata, and developer name free of misleading, false, or copycat representations or names?
  - quote: "don’t include misleading, false, or copycat representations, names, or metadata in your app bundle or developer name"
  - surface: asc
  - verify: Check App Store Connect App Name, Subtitle, Description, Keywords, screenshots and seller/developer name, plus `CFBundleDisplayName`/`CFBundleName` and bundle ID, for names imitating other apps/brands or false claims.
  - fix: Rename/rewrite the misleading or copycat metadata.
- **[5.2.1-03]** Is the app submitted by the person or legal entity that owns or has licensed the intellectual property and other relevant rights? (Apple says "should")
  - quote: "Apps should be submitted by the person or legal entity that owns or has licensed the intellectual property and other relevant rights."
  - surface: manual
  - verify: Compare the App Store Connect seller name with the owner/licensee of the app's brand and content; developer attests.
  - fix: manual — requires developer decision/legal/business action.

## 5.2.2 Third-Party Sites/Services

**Source text (verbatim):**
> Third-Party Sites/Services: If your app uses, accesses, monetizes access to, or displays content from a third-party service, ensure that you are specifically permitted to do so under the service’s terms of use. Authorization must be provided upon request.

**Applies to:** Apps that use, access, monetize access to, or display content from a third-party service

- **[5.2.2-01]** For each third-party service the app uses, accesses, monetizes access to, or displays content from, is the developer specifically permitted to do so under that service's terms of use, with authorization available on request?
  - quote: "ensure that you are specifically permitted to do so under the service’s terms of use. Authorization must be provided upon request."
  - surface: code
  - verify: Grep for external hosts/APIs (`URL(string:`, base URLs, SDK configs, `WKWebView` loads) to list third-party services; for each, developer confirms the terms of use permit the usage (esp. scraping, displaying, or charging for access) and has authorization documentation. Consider noting it in App Review Information > Notes.
  - fix: manual — requires developer decision/legal/business action (obtain permission/API license, or remove the integration).

## 5.2.3 Audio/Video Downloading

**Source text (verbatim):**
> Audio/Video Downloading: Apps should not facilitate illegal file sharing or include the ability to save, convert, or download media from third-party sources (such as Apple Music, YouTube, SoundCloud, Vimeo, etc.) without explicit authorization from those sources. Streaming of audio/video content may also violate Terms of Use, so be sure to check before your app accesses those services. Authorization must be provided upon request.

**Applies to:** Apps that handle audio/video from third-party sources

- **[5.2.3-01]** Does the app avoid facilitating illegal file sharing? (Apple says "should not")
  - quote: "Apps should not facilitate illegal file sharing"
  - surface: code
  - verify: Grep for torrent/P2P libraries or file-sharing features that distribute media; developer attests.
  - fix: Remove the file-sharing functionality.
- **[5.2.3-02]** Does the app avoid saving, converting, or downloading media from third-party sources (Apple Music, YouTube, SoundCloud, Vimeo, etc.) without explicit authorization from those sources? (Apple says "should not")
  - quote: "include the ability to save, convert, or download media from third-party sources (such as Apple Music, YouTube, SoundCloud, Vimeo, etc.) without explicit authorization from those sources"
  - surface: code
  - verify: Grep for downloaders/converters (e.g. youtube-dl/yt-dlp ports, `URLSession` downloads of media from youtube.com/googlevideo.com/soundcloud.com/vimeo.com, `AVAssetExportSession` on third-party streams); confirm written authorization exists for any.
  - fix: Remove download/convert features for third-party media, or obtain explicit authorization.
- **[5.2.3-03]** If the app streams audio/video from third-party services, has the developer checked that it doesn't violate their Terms of Use, with authorization available on request?
  - quote: "Streaming of audio/video content may also violate Terms of Use, so be sure to check before your app accesses those services. Authorization must be provided upon request."
  - surface: manual
  - verify: List third-party streaming sources (`AVPlayer` URLs, embedded players); developer confirms ToS compliance and has authorization documentation.
  - fix: manual — requires developer decision/legal/business action.

## 5.2.4 Apple Endorsements

**Source text (verbatim):**
> Apple Endorsements:
> - (a) Don’t suggest or imply that Apple is a source or supplier of the App, or that Apple endorses any particular representation regarding quality or functionality.
> - (b) If your app is selected as an “Editor’s Choice,” Apple will apply the badge automatically.

**Applies to:** All apps

- **[5.2.4-01]** (a) Is the app and its metadata free of any suggestion that Apple is a source or supplier of the app or endorses any representation about its quality or functionality?
  - quote: "Don’t suggest or imply that Apple is a source or supplier of the App, or that Apple endorses any particular representation regarding quality or functionality."
  - surface: asc
  - verify: Review App Store Connect description, subtitle, promotional text, screenshots and in-app strings (grep `.strings`/`.xcstrings` for "Apple", "endorsed", "approved by", "official") for implied Apple sourcing or endorsement.
  - fix: Remove wording/imagery implying Apple supplies or endorses the app.
- **[5.2.4-02]** (b) Is the app free of a self-applied “Editor’s Choice” badge (Apple applies it automatically if selected)?
  - quote: "If your app is selected as an “Editor’s Choice,” Apple will apply the badge automatically."
  - surface: asc
  - verify: Check screenshots, app previews, icon and description for an “Editor’s Choice” badge or claim added by the developer.
  - fix: Remove self-applied Editor’s Choice badges/claims from metadata.

## 5.2.5 Apple Products

**Source text (verbatim):**
> Apple Products: Don’t create an app that appears confusingly similar to an existing Apple product, interface (such as Finder), app (such as the App Store, iTunes Store, or Messages) or advertising theme. Apps and extensions, including third-party keyboards and Sticker packs, may not include Apple emoji. Music from iTunes and Apple Music previews may not be used for their entertainment value (such as as the background music to a photo collage or the soundtrack to a game) or in any other unauthorized manner. If you provide music previews from iTunes or Apple Music, you must display a link to the corresponding music in iTunes or Apple Music. If your app displays Activity rings, they should not visualize Move, Exercise, or Stand data in a way that resembles the Activity control. The Human Interface Guidelines have more information on how to use Activity rings. If your app displays Apple Weather data, it should follow the attribution requirements provided in the WeatherKit documentation.

**Applies to:** All apps (music, Activity rings, and Apple Weather items apply when the app uses them)

**Related:** Human Interface Guidelines; WeatherKit documentation

- **[5.2.5-01]** Does the app avoid appearing confusingly similar to an existing Apple product, interface (e.g., Finder), app (e.g., App Store, iTunes Store, Messages), or advertising theme?
  - quote: "Don’t create an app that appears confusingly similar to an existing Apple product, interface (such as Finder), app (such as the App Store, iTunes Store, or Messages) or advertising theme."
  - surface: runtime
  - verify: Compare the icon, name, main screens and App Store screenshots with Apple apps/products/ad themes for confusing similarity.
  - fix: Redesign the icon/UI/metadata to be distinct.
- **[5.2.5-02]** Are the app and its extensions (incl. keyboards and Sticker packs) free of Apple emoji?
  - quote: "Apps and extensions, including third-party keyboards and Sticker packs, may not include Apple emoji."
  - surface: code
  - verify: Inspect sticker pack assets (`*.stickerpack`), keyboard extension assets, and bundled images for rendered Apple Color Emoji artwork (images of Apple emoji, not Unicode text characters rendered by the system).
  - fix: Replace Apple emoji images with original artwork.
- **[5.2.5-03]** Is music from iTunes and Apple Music previews not used for entertainment value (e.g., background music for a photo collage or game soundtrack) or any other unauthorized manner?
  - quote: "Music from iTunes and Apple Music previews may not be used for their entertainment value (such as as the background music to a photo collage or the soundtrack to a game) or in any other unauthorized manner."
  - surface: code
  - verify: Grep for `previewURL`/`previewAssets` (MusicKit, iTunes Search API `previewUrl`) and check how preview audio is played (e.g. as background track, in exports/collages, game audio).
  - fix: Remove entertainment/background use of previews; use licensed music instead.
- **[5.2.5-04]** If the app provides music previews from iTunes or Apple Music, does it display a link to the corresponding music in iTunes or Apple Music?
  - quote: "If you provide music previews from iTunes or Apple Music, you must display a link to the corresponding music in iTunes or Apple Music."
  - surface: runtime
  - verify: Where previews play, confirm a visible link (e.g. `trackViewUrl` / Apple Music URL) to the corresponding item.
  - fix: Add a link to the corresponding song/album in Apple Music/iTunes next to each preview.
- **[5.2.5-05]** If the app displays Activity rings, does it avoid visualizing Move, Exercise, or Stand data in a way that resembles the Activity control? (Apple says "should")
  - quote: "If your app displays Activity rings, they should not visualize Move, Exercise, or Stand data in a way that resembles the Activity control."
  - surface: code
  - verify: Grep for `HKActivityRingView`, `HKActivitySummary`, and custom concentric-ring views fed with move/exercise/stand data; compare against HIG Activity rings guidance.
  - fix: Use `HKActivityRingView` per HIG, or redesign custom visuals so they don't resemble the Activity control.
- **[5.2.5-06]** If the app displays Apple Weather data, does it follow the WeatherKit attribution requirements? (Apple says "should")
  - quote: "If your app displays Apple Weather data, it should follow the attribution requirements provided in the WeatherKit documentation."
  - surface: code
  - verify: Grep for `WeatherService`/`import WeatherKit` (or WeatherKit REST calls); confirm the UI displays the Apple Weather attribution mark and legal link (`WeatherService.shared.attribution` `combinedMarkLightURL`/`combinedMarkDarkURL`, `legalPageURL`) wherever weather data appears.
  - fix: Add the Apple Weather attribution mark and legal attribution link per WeatherKit documentation.

## 5.3 Gaming, Gambling, and Lotteries

**Source text (verbatim):**
> Gaming, gambling, and lotteries can be tricky to manage and tend to be one of the most regulated offerings on the App Store. Only include this functionality if you’ve fully vetted your legal obligations everywhere you make your app available and are prepared for extra time during the review process. Some things to keep in mind:

**Applies to:** Apps with gaming, gambling, or lottery functionality

- **[5.3-01]** If the app includes gaming, gambling, or lottery functionality, has the developer fully vetted legal obligations everywhere the app is available?
  - quote: "Only include this functionality if you’ve fully vetted your legal obligations everywhere you make your app available and are prepared for extra time during the review process."
  - surface: manual
  - verify: Check App Store Connect > Pricing and Availability storefront list; developer attests legal vetting for each; plan for extra review time.
  - fix: manual — requires developer decision/legal/business action.

## 5.3.1 Sweepstakes and contests sponsored by developer

**Source text (verbatim):**
> Sweepstakes and contests must be sponsored by the developer of the app.

**Applies to:** Apps offering sweepstakes or contests

- **[5.3.1-01]** Are all sweepstakes and contests in the app sponsored by the app's developer?
  - quote: "Sweepstakes and contests must be sponsored by the developer of the app."
  - surface: manual
  - verify: Find sweepstakes/contest features (grep "sweepstakes", "contest", "giveaway", "raffle", "prize"); confirm the sponsor named in the rules is the developer/seller.
  - fix: manual — requires developer decision/legal/business action.

## 5.3.2 Official rules presented in app; Apple not a sponsor

**Source text (verbatim):**
> Official rules for sweepstakes, contests, and raffles must be presented in the app and make clear that Apple is not a sponsor or involved in the activity in any manner.

**Applies to:** Apps offering sweepstakes, contests, or raffles

- **[5.3.2-01]** Are official rules for sweepstakes, contests, and raffles presented in the app?
  - quote: "Official rules for sweepstakes, contests, and raffles must be presented in the app"
  - surface: runtime
  - verify: Open each sweepstakes/contest/raffle and confirm official rules are viewable in-app.
  - fix: Add an in-app "Official Rules" screen/link for each.
- **[5.3.2-02]** Do the official rules make clear that Apple is not a sponsor or involved in any manner?
  - quote: "make clear that Apple is not a sponsor or involved in the activity in any manner"
  - surface: runtime
  - verify: Read the rules text for an explicit statement that Apple is not a sponsor or involved.
  - fix: Add a statement such as "Apple is not a sponsor of, and is not involved in, this promotion in any manner."

## 5.3.3 No in-app purchase for real money gaming credit

**Source text (verbatim):**
> Apps may not use in-app purchase to purchase credit or currency for use in conjunction with real money gaming of any kind.

**Applies to:** Apps with real money gaming

- **[5.3.3-01]** Is in-app purchase never used to buy credit or currency used with real money gaming?
  - quote: "Apps may not use in-app purchase to purchase credit or currency for use in conjunction with real money gaming of any kind."
  - surface: code
  - verify: If real money gaming exists, list StoreKit products (`Product.products(for:)`, `.storekit` config, App Store Connect > In-App Purchases) and confirm none fund real-money wagering balances.
  - fix: Remove those IAP products; fund real money gaming through a non-IAP mechanism as permitted.

## 5.3.4 Real money gaming and lotteries

**Source text (verbatim):**
> Apps that offer real money gaming (such as sports betting, poker, casino games, horse racing) or lotteries must have necessary licensing and permissions in the locations where the app is used, must be geo-restricted to those locations, and must be free on the App Store. Illegal gambling aids, including card counters, are not permitted on the App Store. Lottery apps must have consideration, chance, and a prize.

**Applies to:** Apps offering real money gaming or lotteries; gambling aids

- **[5.3.4-01]** If the app offers real money gaming or lotteries, does it have the necessary licensing and permissions in the locations where it is used?
  - quote: "must have necessary licensing and permissions in the locations where the app is used"
  - surface: manual
  - verify: Developer provides licenses per jurisdiction; consider listing them in App Store Connect > App Review Information > Notes.
  - fix: manual — requires developer decision/legal/business action.
- **[5.3.4-02]** Is the real money gaming/lottery app geo-restricted to the licensed locations?
  - quote: "must be geo-restricted to those locations"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability lists only licensed countries/regions; in code, check for location-based geofencing (e.g. `CLLocationManager` checks before wagering) for sub-national licensing.
  - fix: Restrict availability in App Store Connect and add in-app geolocation enforcement.
- **[5.3.4-03]** Is the real money gaming/lottery app free on the App Store?
  - quote: "must be free on the App Store"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > Price is Free (0).
  - fix: Set the app price to Free.
- **[5.3.4-04]** Is the app free of illegal gambling aids, including card counters?
  - quote: "Illegal gambling aids, including card counters, are not permitted on the App Store."
  - surface: manual
  - verify: Review features for card counting or other illegal gambling aids.
  - fix: Remove the gambling-aid functionality.
- **[5.3.4-05]** If it is a lottery app, does it have consideration, chance, and a prize?
  - quote: "Lottery apps must have consideration, chance, and a prize."
  - surface: manual
  - verify: Confirm the lottery mechanics include consideration (entry cost), chance, and a prize.
  - fix: manual — requires developer decision/legal/business action.

## 5.4 VPN Apps

**Source text (verbatim):**
> Apps offering VPN services must utilize the NEVPNManager API and may only be offered by developers enrolled as an organization. You must make a clear declaration of what user data will be collected and how it will be used on an app screen prior to any user action to purchase or otherwise use the service. Apps offering VPN services may not sell, use, or disclose to third parties any data for any purpose, and must commit to this in their privacy policy. VPN apps must not violate local laws, and if you choose to make your VPN app available in a territory that requires a VPN license, you must provide your license information in the App Review Notes field. Parental control, content blocking, and security apps, among others, from approved providers may also use the NEVPNManager API. Apps that do not comply with this guideline will be removed from the App Store and blocked from installing via alternative distribution and you may be removed from the Apple Developer Program.

**Applies to:** Apps offering VPN services (and parental control, content blocking, and security apps using the NEVPNManager API)

**Related:** NEVPNManager API

- **[5.4-01]** Does the VPN app use the NEVPNManager API?
  - quote: "Apps offering VPN services must utilize the NEVPNManager API"
  - surface: code
  - verify: Grep for `NEVPNManager`/`NETunnelProviderManager` and a Packet Tunnel extension; check entitlements for `com.apple.developer.networking.networkextension` / Personal VPN.
  - fix: Implement the VPN with NetworkExtension (`NEVPNManager`/`NETunnelProviderManager`).
- **[5.4-02]** Is the VPN app offered by a developer enrolled as an organization?
  - quote: "may only be offered by developers enrolled as an organization"
  - surface: asc
  - verify: Check the Apple Developer account/App Store Connect seller type is Organization, not Individual.
  - fix: manual — requires developer decision/legal/business action (enroll as an organization).
- **[5.4-03]** Does an app screen clearly declare what user data is collected and how it is used, before any user action to purchase or use the service?
  - quote: "You must make a clear declaration of what user data will be collected and how it will be used on an app screen prior to any user action to purchase or otherwise use the service."
  - surface: runtime
  - verify: Fresh install: confirm a data-collection/use disclosure screen appears before the paywall and before the connect button.
  - fix: Add a disclosure screen shown before purchase or first connection.
- **[5.4-04]** Does the VPN app avoid selling, using, or disclosing any data to third parties, and commit to this in its privacy policy?
  - quote: "may not sell, use, or disclose to third parties any data for any purpose, and must commit to this in their privacy policy"
  - surface: manual
  - verify: Check for third-party analytics/ads SDKs in app and tunnel extension; read privacy policy for the explicit commitment.
  - fix: Remove third-party data sharing and add the commitment to the privacy policy.
- **[5.4-05]** Does the VPN app comply with local laws, and if available in a territory requiring a VPN license, is the license information provided in the App Review Notes field?
  - quote: "if you choose to make your VPN app available in a territory that requires a VPN license, you must provide your license information in the App Review Notes field"
  - surface: asc
  - verify: Check App Store Connect > Pricing and Availability for territories requiring a VPN license; check App Review Information > Notes contains the license info.
  - fix: Add license information to App Review Notes, or remove those territories.

## 5.5 Mobile Device Management

**Source text (verbatim):**
> Mobile Device Management Apps that offer Mobile Device Management (MDM) services must request this capability from Apple. Such apps may only be offered by commercial enterprises, educational institutions, or government agencies, and in limited cases, companies using MDM for parental control services or device security. You must make a clear declaration of what user data will be collected and how it will be used on an app screen prior to any user action to purchase or otherwise use the service. MDM apps must not violate any applicable laws. Apps offering MDM services may not sell, use, or disclose to third parties any data for any purpose, and must commit to this in their privacy policy. In limited cases, third-party analytics may be permitted provided that the services only collect or transmit data about the performance of the developer’s MDM app, and not any data about the user, the user’s device, or other apps used on that device. Apps offering configuration profiles must also adhere to these requirements. Apps that do not comply with this guideline will be removed from the App Store and blocked from installing via alternative distribution and you may be removed from the Apple Developer Program.

**Applies to:** Apps offering Mobile Device Management (MDM) services or configuration profiles

- **[5.5-01]** Has the MDM capability been requested from Apple?
  - quote: "Apps that offer Mobile Device Management (MDM) services must request this capability from Apple."
  - surface: manual
  - verify: Developer confirms the MDM capability was requested/granted by Apple.
  - fix: manual — requires developer decision/legal/business action (request the capability from Apple).
- **[5.5-02]** Is the MDM app offered by a commercial enterprise, educational institution, or government agency (or, in limited cases, a company using MDM for parental control or device security)?
  - quote: "Such apps may only be offered by commercial enterprises, educational institutions, or government agencies"
  - surface: asc
  - verify: Check the App Store Connect seller is an organization of an allowed type.
  - fix: manual — requires developer decision/legal/business action.
- **[5.5-03]** Does an app screen clearly declare what user data is collected and how it is used, before any user action to purchase or use the service?
  - quote: "You must make a clear declaration of what user data will be collected and how it will be used on an app screen prior to any user action to purchase or otherwise use the service."
  - surface: runtime
  - verify: Fresh install: confirm the disclosure screen precedes any purchase or enrollment action.
  - fix: Add a disclosure screen shown before purchase or enrollment.
- **[5.5-04]** Does the MDM app comply with applicable laws?
  - quote: "MDM apps must not violate any applicable laws."
  - surface: manual
  - verify: Developer attests.
  - fix: manual — requires developer decision/legal/business action.
- **[5.5-05]** Does the MDM app avoid selling, using, or disclosing any data to third parties, and commit to this in its privacy policy?
  - quote: "Apps offering MDM services may not sell, use, or disclose to third parties any data for any purpose, and must commit to this in their privacy policy."
  - surface: manual
  - verify: Review SDKs/data flows for third-party disclosure; read privacy policy for the explicit commitment.
  - fix: Remove third-party data sharing and add the commitment to the privacy policy.
- **[5.5-06]** If the MDM app uses third-party analytics, do they collect/transmit only data about the performance of the MDM app and nothing about the user, device, or other apps?
  - quote: "third-party analytics may be permitted provided that the services only collect or transmit data about the performance of the developer’s MDM app, and not any data about the user, the user’s device, or other apps used on that device"
  - surface: code
  - verify: List analytics SDKs; inspect logged events/parameters and SDK auto-collection settings (device info, identifiers) to confirm only app-performance data is sent.
  - fix: Disable auto-collection of user/device data, restrict events to app-performance metrics, or remove the SDK.
- **[5.5-07]** If the app offers configuration profiles, does it adhere to these same MDM requirements?
  - quote: "Apps offering configuration profiles must also adhere to these requirements."
  - surface: code
  - verify: Grep for `.mobileconfig` files or code that serves/installs configuration profiles; if present, apply checks 5.5-01 through 5.5-06.
  - fix: Bring the configuration-profile app into compliance with 5.5-01–5.5-06.

## 5.6 Developer Code of Conduct

**Source text (verbatim):**
> Please treat everyone with respect, whether in your responses to App Store reviews, customer support requests, or when communicating with Apple, including your responses in App Store Connect. Do not engage in harassment of any kind, discriminatory practices, intimidation, bullying, and don’t encourage others to engage in any of the above. Repeated manipulative or misleading behavior or other fraudulent conduct will lead to your removal from the Apple Developer Program.
>
> Customer trust is a cornerstone of the App ecosystem. Apps should never prey on users or attempt to rip off customers, trick them into making unwanted purchases, force them to share unnecessary data, raise prices in a tricky manner, charge for features or content that are not delivered, or engage in any other manipulative practices within or outside of the app.
>
> Your Developer Program account will be terminated if you engage in activities or actions that are not in accordance with the Developer Code of Conduct. To restore your account, you may provide a written statement detailing the improvements you plan to make. If your plan is approved by Apple and we confirm the changes have been made, your account may be restored.

**Applies to:** All apps / developers

- **[5.6-01]** Are communications (App Store review responses, customer support, communication with Apple incl. App Store Connect responses) respectful and free of harassment, discrimination, intimidation, or bullying?
  - quote: "Please treat everyone with respect, whether in your responses to App Store reviews, customer support requests, or when communicating with Apple, including your responses in App Store Connect."
  - surface: asc
  - verify: Review App Store Connect > Ratings and Reviews developer responses and App Review (Resolution Center) messages for disrespectful tone; also review any planned App Review Notes text.
  - fix: Edit or remove disrespectful responses; manual — developer conduct.
- **[5.6-02]** Is the app free of attempts to trick users into making unwanted purchases?
  - quote: "trick them into making unwanted purchases"
  - surface: runtime
  - verify: Exercise paywalls/purchase flows and inspect paywall views in code for anything that could trick a user into a purchase they did not intend (e.g. disguised or misleading purchase actions, obscured price or what is being bought).
  - fix: Remove or redesign deceptive purchase UI so users knowingly choose each purchase.
- **[5.6-07]** Do the paywall's and purchase flow's controls do what their labels say, with no manipulative pattern around leaving the offer?
  - quote: "engage in any other manipulative practices within or outside of the app"
  - surface: runtime
  - verify: In every paywall/offer view, find each control labelled or styled as dismissing (X, "Close", "Not now", "Maybe later", "Skip", swipe-down). Trace its action in code: it must dismiss. FAIL if a dismiss-labelled control presents another offer, a discount card or a second paywall instead of closing, or if declining loops back to the paywall so the sheet can only be left by buying. A hard paywall with no close control is not by itself this pattern (judge it under 3.1.1/3.1.2); a control that claims to close but doesn't is. Implementation guidance, not Apple text: App Review has rejected this exact pattern under 5.6 in real submissions.
  - fix: Make every dismiss-labelled control dismiss. Any retention offer must be presented as its own clearly labelled choice, never behind the close control.
- **[5.6-03]** Does the app avoid forcing users to share unnecessary data?
  - quote: "force them to share unnecessary data"
  - surface: runtime
  - verify: See 5.1.1-13 and 5.1.1-17: confirm no flow forces sharing of data unrelated to the feature.
  - fix: Make unnecessary data optional or remove the request.
- **[5.6-04]** Does the app avoid raising prices in a tricky manner?
  - quote: "raise prices in a tricky manner"
  - surface: asc
  - verify: Review App Store Connect subscription/IAP price change history and paywall copy for price increases made in a tricky manner (e.g. an introductory price followed by a higher price the user was not made aware of).
  - fix: Disclose price changes clearly; manual — requires developer decision/business action.
- **[5.6-05]** Are all charged features or content actually delivered?
  - quote: "charge for features or content that are not delivered"
  - surface: runtime
  - verify: In StoreKit sandbox/TestFlight, purchase each IAP/subscription and confirm the promised features/content unlock; compare paywall feature lists and IAP descriptions in App Store Connect with what the app provides.
  - fix: Implement missing paid features or remove them from paywall/IAP descriptions.
- **[5.6-06]** Is the app free of other manipulative practices that prey on users within or outside the app?
  - quote: "Apps should never prey on users or attempt to rip off customers"
  - surface: manual
  - verify: Review flows, notifications and marketing (in-app and external) for manipulative practices; developer attests.
  - fix: manual — requires developer decision/legal/business action.

## 5.6.1 App Store Reviews

**Source text (verbatim):**
> App Store customer reviews can be an integral part of the app experience, so you should treat customers with respect when responding to their comments. Keep your responses targeted to the user’s comments and do not include personal information, spam, or marketing in your response.
>
> Use the provided API to prompt users to review your app; this functionality allows customers to provide an App Store rating and review without the inconvenience of leaving your app, and we will disallow custom review prompts.

**Applies to:** All apps

- **[5.6.1-01]** Are developer responses to App Store reviews respectful, targeted to the user's comments, and free of personal information, spam, or marketing?
  - quote: "Keep your responses targeted to the user’s comments and do not include personal information, spam, or marketing in your response."
  - surface: asc
  - verify: App Store Connect > Ratings and Reviews: read each developer response.
  - fix: Edit responses to address the comment respectfully without personal info, spam or marketing.
- **[5.6.1-02]** Does the app use the provided API to prompt for reviews, with no custom review prompts?
  - quote: "Use the provided API to prompt users to review your app"
  - surface: code
  - verify: Grep for `SKStoreReviewController.requestReview`, `AppStore.requestReview(in:)`, SwiftUI `@Environment(\.requestReview)`; grep strings for custom rating prompts ("Rate us", "Enjoying", star-rating dialogs, "Leave a review") that are not the system API.
  - fix: Replace custom review prompts with `AppStore.requestReview(in:)` / `requestReview` environment action.

## 5.6.2 Developer Identity

**Source text (verbatim):**
> Providing verifiable information to Apple and customers is critical to customer trust. Your representation of yourself, your business, and your offerings on the App Store or alternative distribution must be accurate. The information you provide must be truthful, relevant, and up-to-date so that Apple and customers understand who they are engaging with and can contact you regarding any issues.

**Applies to:** All developers

- **[5.6.2-01]** Is the developer's representation of themselves, their business, and their offerings accurate?
  - quote: "Your representation of yourself, your business, and your offerings on the App Store or alternative distribution must be accurate."
  - surface: asc
  - verify: Review App Store Connect seller name, copyright, description and App Information for accuracy against the real business and the app's actual features.
  - fix: Correct inaccurate representations in App Store Connect.
- **[5.6.2-02]** Is the information provided truthful, relevant, and up-to-date so Apple and customers can contact the developer?
  - quote: "The information you provide must be truthful, relevant, and up-to-date so that Apple and customers understand who they are engaging with and can contact you regarding any issues."
  - surface: asc
  - verify: Check App Store Connect Support URL (loads and has contact info), Marketing URL if set, App Review Information contact (name, phone, email), and developer account contact details are current.
  - fix: Update Support URL, contact info and account details to current, working values.

## 5.6.3 Discovery Fraud

**Source text (verbatim):**
> Participating in the App Store requires integrity and a commitment to building and maintaining customer trust. Manipulating any element of the App Store customer experience such as charts, search, reviews, or referrals to your app erodes customer trust and is not permitted.

**Applies to:** All developers

- **[5.6.3-01]** Is the developer free of manipulation of any element of the App Store customer experience (charts, search, reviews, or referrals)?
  - quote: "Manipulating any element of the App Store customer experience such as charts, search, reviews, or referrals to your app erodes customer trust and is not permitted."
  - surface: manual
  - verify: Developer attests no purchased reviews/installs, incentivized ratings, or keyword/search manipulation; check code for rewards tied to rating/reviewing (grep "review"/"rate" near reward/coins logic) and App Store Connect keywords for manipulation.
  - fix: Remove incentivized-review code and manipulative keywords; manual — stop manipulation practices.

## 5.6.4 App Quality

**Source text (verbatim):**
> Customers expect the highest quality from the App Store, and maintaining high quality content, services, and experiences promotes customer trust. Indications that this expectation is not being met include excessive customer reports about concerns with your app, such as negative customer reviews, and excessive refund requests. Inability to maintain high quality may be a factor in deciding whether a developer is abiding by the Developer Code of Conduct.

**Applies to:** All apps

- **[5.6.4-01]** Is the app free of indications of low quality such as excessive customer reports, negative customer reviews, or excessive refund requests?
  - quote: "Indications that this expectation is not being met include excessive customer reports about concerns with your app, such as negative customer reviews, and excessive refund requests."
  - surface: asc
  - verify: For updates: App Store Connect > Ratings and Reviews (recurring complaints), and refund/report trends (App Analytics, Sales and Trends); for new apps, note as N/A.
  - fix: manual — requires developer decision/legal/business action (address recurring complaints and causes of refunds in the next build).
