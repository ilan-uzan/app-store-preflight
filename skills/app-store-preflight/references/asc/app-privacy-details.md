# App Privacy Details (Privacy Nutrition Labels) and App Tracking Transparency
Source: https://developer.apple.com/app-store/app-privacy-details/ , https://developer.apple.com/app-store/user-privacy-and-data-use/ , https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy , https://developer.apple.com/documentation/apptrackingtransparency , and the API pages listed under Sources  
Retrieved: 2026-10-30

How to use this file: each `## LABEL.<x>` unit reproduces Apple's text verbatim, then lists pass/fail checks derived only from that text. Check IDs `LABEL-<nn>` are stable. A label audit generally needs three inputs: (1) what the code and bundled SDKs send off the device (network calls, analytics/ads/crash SDKs, `PrivacyInfo.xcprivacy` files, web views); (2) the App Store Connect > App > App Privacy page; (3) the developer's attestation about server-side retention, linking and sharing.

---

## LABEL.A App privacy details on the App Store — overview

**Source text (verbatim):**
> The App Store helps people better understand an app’s privacy practices before they download the app on any Apple platform. On each app’s product page, users can learn about some of the data types the app may collect, and whether that data is linked to them or used to track them. You’ll need to provide information about your app’s privacy practices, including the practices of third-party partners whose code you integrate into your app, in App Store Connect. This information is required to submit new apps and app updates to the App Store.

**Applies to:** All apps submitted to the App Store (new apps and app updates)

- **[LABEL-01]** Has the App Privacy section in App Store Connect been completed (and published) before submitting this new app or app update?
  - quote: "This information is required to submit new apps and app updates to the App Store."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > sidebar "App Privacy". Pass if the page shows published data-type responses (or the "No, we do not collect data from this app" answer) rather than a "Get Started" button.
  - fix: Complete the App Privacy questionnaire (see LABEL.O) and click Publish.
- **[LABEL-02]** Do the App Privacy responses cover the practices of every third-party partner whose code is integrated into the app (not only first-party code)?
  - quote: "including the practices of third-party partners whose code you integrate into your app"
  - surface: code
  - verify: List all third-party code: `Package.resolved`, `Podfile.lock`, `Cartfile.resolved`, embedded `.framework`/`.xcframework` bundles, and every `PrivacyInfo.xcprivacy` inside them (`find . -name PrivacyInfo.xcprivacy`). In Xcode, Product > Archive > Organizer > right-click archive > Generate Privacy Report. Compare each SDK's declared `NSPrivacyCollectedDataTypes` against the ASC data-type selections.
  - fix: Add the missing data types / purposes / linked / tracking answers in ASC App Privacy and Publish.

---

## LABEL.B Answering app privacy questions

**Source text (verbatim):**
> As you get ready to select your answers from the options presented in App Store Connect, keep in mind:
> - You need to identify all of the data you or your third-party partners collect, unless the data meets all of the criteria for optional disclosure listed below.
> - Your app’s privacy practices should follow the App Review Guidelines and all applicable laws.
> - You’re responsible for keeping your responses accurate and up to date. If your practices change, update your responses in App Store Connect. You may update your answers at any time, and you do not need to submit an app update in order to change your answers.
>
> Account Holders, Admins, and App Managers can learn how to enter their responses in App Store Connect.

**Applies to:** All apps

- **[LABEL-03]** Is every data type that the app or its third-party partners collect identified in App Store Connect, except data that meets all optional-disclosure criteria?
  - quote: "You need to identify all of the data you or your third-party partners collect, unless the data meets all of the criteria for optional disclosure listed below."
  - surface: code
  - verify: Inventory outbound data: grep Swift/ObjC for `URLSession`, `URLRequest`, `Alamofire`, `WKWebView`, `Firestore`, `Analytics.logEvent`, `Mixpanel`, `Amplitude`, `Sentry`, `Crashlytics`, `CLLocationManager`, `HKHealthStore`, `CNContactStore`, `PHPhotoLibrary`, `AVAudioRecorder`, form fields (`TextField`, `UITextField` with `.emailAddress`, `.name`, `.telephoneNumber` content types) whose values are uploaded. Map each to the data-type table in LABEL.H and compare with ASC App Privacy.
  - fix: Add missing data types in ASC App Privacy > Data Types > Edit, answer their questions, Publish.
- **[LABEL-04]** Do the current App Privacy answers match the app's current practices (updated after any change)?
  - quote: "You’re responsible for keeping your responses accurate and up to date. If your practices change, update your responses in App Store Connect."
  - surface: manual
  - verify: Diff the SDK/network inventory from LABEL-03 against the last published ASC responses; ask the developer whether any new SDK, endpoint, or server-side use was added since the last publish.
  - fix: Update responses in ASC (no app update needed per "you do not need to submit an app update in order to change your answers").
- **[LABEL-05]** Does the person entering the App Privacy responses have the Account Holder, Admin, or App Manager role?
  - quote: "Account Holders, Admins, and App Managers can learn how to enter their responses in App Store Connect."
  - surface: asc
  - verify: ASC > Users and Access: confirm the operator's role. If the App Privacy page is read-only for them, the role is insufficient.
  - fix: manual — requires developer decision/legal/business action (Account Holder or Admin assigns a role).
- **[LABEL-104]** Do the privacy practices described in App Privacy follow the App Review Guidelines and all applicable laws (Apple states this as "should")?
  - quote: "Your app’s privacy practices should follow the App Review Guidelines and all applicable laws."
  - surface: manual
  - verify: Cross-reference the declared practices with the App Review Guidelines 5.1 privacy units in this skill; ask the developer which privacy laws apply (e.g., GDPR, CCPA) and whether the practices have been reviewed against them.
  - fix: manual — requires developer decision/legal/business action.

---

## LABEL.C Data collection — definitions of "Collect" and "Third-party partners"

**Source text (verbatim):**
> The purpose of the label is to help your customers understand what data is collected from your app and how it is used. To complete that, you’ll need to know the types of data that you and/or your third-party partners collect from your app before answering the questions in App Store Connect. Keep in mind that even if you collect the data for reasons other than analytics or advertising, it still needs to be declared. For example, if you collect data solely for the purpose of app functionality, declare the data on your label and indicate that it is only being used for that purpose.
>
> “Collect” refers to transmitting data off the device in a way that allows you and/or your third-party partners to access it for a period longer than what is necessary to service the transmitted request in real time.
>
> “Third-party partners” refers to analytics tools, advertising networks, third-party SDKs, or other external vendors whose code you’ve added to your app.

**Applies to:** All apps that transmit any data off the device

- **[LABEL-06]** Is data collected solely for app functionality (e.g., account email used to sign in, synced user content) declared on the label with the App Functionality purpose?
  - quote: "if you collect data solely for the purpose of app functionality, declare the data on your label and indicate that it is only being used for that purpose."
  - surface: asc
  - verify: For each backend/sync feature found in code (Firebase Auth, CloudKit private DB written by you, Supabase, custom API), confirm the corresponding data type exists in ASC App Privacy with purpose "App Functionality".
  - fix: Add the data type with purpose App Functionality in ASC.
- **[LABEL-07]** Has every analytics tool, advertising network, third-party SDK, or other external vendor code in the app been treated as a "third-party partner" whose collection must be declared?
  - quote: "“Third-party partners” refers to analytics tools, advertising networks, third-party SDKs, or other external vendors whose code you’ve added to your app."
  - surface: code
  - verify: Enumerate dependencies (SPM `Package.resolved`, CocoaPods `Podfile.lock`, Carthage, vendored frameworks). For each, read its `PrivacyInfo.xcprivacy` `NSPrivacyCollectedDataTypes` and vendor documentation; confirm each listed type appears in ASC.
  - fix: Declare each partner's collected data types in ASC App Privacy.
- **[LABEL-08]** For each data flow, has it been determined whether the data is retained (accessible longer than needed to service the request in real time) — the test for "collect"?
  - quote: "“Collect” refers to transmitting data off the device in a way that allows you and/or your third-party partners to access it for a period longer than what is necessary to service the transmitted request in real time."
  - surface: manual
  - verify: For each endpoint found in code, ask the developer whether the server or vendor stores the payload (logs, databases, analytics warehouses). Retained = collected.
  - fix: manual — requires developer decision/legal/business action (declare retained data in ASC).

---

## LABEL.D Optional disclosure — general criteria

**Source text (verbatim):**
> Data types that meet all of the following criteria are optional to disclose:
> - The data is not used for tracking purposes, meaning the data is not linked with Third-Party Data for advertising or advertising measurement purposes, or shared with a data broker. For details, see the Tracking section.
> - The data is not used for Third-Party Advertising, your Advertising or Marketing purposes, or for Other Purposes, as those terms are defined in the Tracking section.
> - Collection of the data occurs only in infrequent cases that are not part of your app’s primary functionality, and which are optional for the user.
> - The data is provided by the user in your app’s interface, it is clear to the user what data is collected, the user’s name or account name is prominently displayed in the submission form alongside the other data elements being submitted, and the user affirmatively chooses to provide the data for collection each time.
>
> Data types must meet all criteria in order to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in App Store Connect.
>
> Examples of data that may not need to be disclosed include data collected in optional feedback forms or customer service requests that are unrelated to the primary purpose of the app and meet the other criteria above.
>
> For the purpose of clarity, data collected on an ongoing basis after an initial request for permission must be disclosed.

**Applies to:** Apps that omit any collected data type from the label in reliance on optional disclosure

- **[LABEL-09]** For every collected data type omitted from the label, does it meet ALL four optional-disclosure criteria (not tracking; not used for Third-Party Advertising, Developer’s Advertising or Marketing, or Other Purposes; infrequent, not primary functionality, optional; user-provided in the UI with name/account name prominently displayed and affirmatively submitted each time)?
  - quote: "Data types must meet all criteria in order to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in App Store Connect."
  - surface: code
  - verify: For each omitted type, locate the collecting UI (e.g., a feedback/support form view). Confirm: it is reached only by explicit user action; the form shows the user's name or account name prominently; submission requires an explicit tap each time; no analytics/ads SDK receives the payload. Any failure → must be disclosed.
  - fix: Disclose the data type in ASC App Privacy, or change the form so all criteria hold (e.g., show the account name in the form, require explicit submit each time).
- **[LABEL-10]** Is any data collected on an ongoing basis after an initial permission request (e.g., continuous location after authorization, ongoing HealthKit sync) disclosed rather than treated as optional?
  - quote: "data collected on an ongoing basis after an initial request for permission must be disclosed."
  - surface: code
  - verify: grep for `startUpdatingLocation`, `startMonitoringSignificantLocationChanges`, `HKObserverQuery`, `enableBackgroundDelivery`, background upload tasks, periodic sync timers that upload permission-gated data; confirm those types are declared in ASC.
  - fix: Declare the data type in ASC App Privacy.

---

## LABEL.E Optional disclosure — Product Improvement Programs

**Source text (verbatim):**
> Data types that meet all of the following criteria are optional to disclose:
> - Data collected is only used for the purpose of improving your app and its services.
> - Collection of the data is optional and only occurs if the user explicitly opts in through a choice presented directly within the user interface — where the user is given two clear options: one to share the data and one to not share the data.
> - The user’s choice does not impact any features or functionality of the app, or their cost.
> - Users can update their choice at any time through an easily accessible setting.
> - The data is not linked to the user’s identity (via their account, device, or other details).
> - The data is not used for tracking purposes, meaning the data is not linked with Third-Party Data for advertising or advertising measurement purposes, or shared with a data broker. For details, see the Tracking section.
> - The data is not used for Third-Party Advertising, your Advertising or Marketing purposes, Product Personalization, or Other Purposes.
>
> Data types must meet all the criteria to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

**Applies to:** Apps that omit data from the label because it is collected through an opt-in product improvement program

- **[LABEL-11]** Is product-improvement data collected only after an explicit in-UI opt-in offering two clear options (share / don't share), with collection off by default?
  - quote: "only occurs if the user explicitly opts in through a choice presented directly within the user interface — where the user is given two clear options: one to share the data and one to not share the data."
  - surface: runtime
  - verify: Fresh install in Simulator; before any choice, monitor network (Proxyman/Charles or SDK debug logs) for diagnostics/analytics uploads. Confirm the opt-in screen shows two distinct buttons. In code, check that the SDK init (e.g., `Analytics.setAnalyticsCollectionEnabled`, Sentry `enabled`) is gated on a stored opt-in flag defaulting to false.
  - fix: Gate collection behind an explicit two-option opt-in, or disclose the data in ASC.
- **[LABEL-12]** Does declining the product-improvement program leave every feature and the price unchanged?
  - quote: "The user’s choice does not impact any features or functionality of the app, or their cost."
  - surface: runtime
  - verify: Decline the opt-in and exercise all main features and any paywall; grep for code branching on the opt-in flag outside of telemetry setup.
  - fix: Remove any feature/price dependency on the opt-in, or disclose the data in ASC.
- **[LABEL-13]** Can users change the product-improvement choice at any time through an easily accessible setting?
  - quote: "Users can update their choice at any time through an easily accessible setting."
  - surface: runtime
  - verify: Locate a toggle in the app's Settings screen (or Settings.bundle) bound to the same opt-in flag; toggle it and confirm collection stops.
  - fix: Add an in-app settings toggle, or disclose the data in ASC.
- **[LABEL-14]** Is product-improvement data free of links to the user's identity (account, device, or other details) and unused for tracking, Third-Party Advertising, Developer’s Advertising or Marketing, Product Personalization, or Other Purposes?
  - quote: "The data is not linked to the user’s identity (via their account, device, or other details)."
  - surface: code
  - verify: Inspect telemetry calls for `setUserID`, `identify(`, `setUser(`, user email/ID attributes, `identifierForVendor`, `advertisingIdentifier` attached to events. Any identifier attached → not eligible.
  - fix: Strip identifiers from telemetry, or disclose the data (as linked) in ASC.

---

## LABEL.F Optional disclosure — Regulated Financial Services Disclosure

**Source text (verbatim):**
> Data types that are collected by an app that facilitates regulated financial services and where the data collected meets all of the following criteria are optional to disclose:
> - Collection of the regulated data is in accordance with a legally required privacy notice under applicable financial services or data protection laws or regulations (e.g., GDPR or GLBA).
> - Collection by the app of that data occurs only in cases that are not part of your app’s primary functionality, and which are optional for the user.
> - Such notice provides that data is not shared with unaffiliated third parties to market other products and services.
> - Such data is not linked with third-party data for advertising purposes or shared with a data broker except for purposes of fraud detection or prevention or security purposes, or with a consumer reporting agency for credit reporting.
>
> Data types must meet all criteria in order to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

**Applies to:** Apps that facilitate regulated financial services and omit data from the label on this basis

- **[LABEL-15]** For each data type omitted under the regulated-financial-services exception, are all four criteria met (legally required privacy notice; not primary functionality and optional; notice says no sharing with unaffiliated third parties for marketing; no ad linking or data-broker sharing except fraud/security/credit reporting)?
  - quote: "Data types must meet all criteria in order to be considered optional for disclosure."
  - surface: manual
  - verify: Ask the developer for the legally required privacy notice (e.g., GLBA notice) and confirm its text; confirm the collection is outside primary functionality and optional for the user.
  - fix: manual — requires developer decision/legal/business action (otherwise disclose the data in ASC).

---

## LABEL.G Optional disclosure — Health Research Disclosure

**Source text (verbatim):**
> Data types that are collected as part of a health research study and where the data collected meets all of the following criteria are optional to disclose:
> - The data is collected by an entity whose collection of the data is subject to an informed consent form (ICF) as part of a health research study that has been reviewed and approved by an institutional review board or ethics review board.
> - All such data collection must follow the relevant App Review Guidelines and the data may not be used for tracking purposes.
>
> If the data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

**Applies to:** Apps that collect data as part of a health research study and omit it from the label on this basis

- **[LABEL-16]** Is health-research data omitted from the label only when collected under an informed consent form for a study approved by an institutional review board or ethics review board, and never used for tracking?
  - quote: "subject to an informed consent form (ICF) as part of a health research study that has been reviewed and approved by an institutional review board or ethics review board."
  - surface: manual
  - verify: Ask the developer for the IRB/ethics approval and the ICF presented in the app (ResearchKit `ORKConsentDocument` or equivalent); confirm no ads/attribution SDK receives the data.
  - fix: manual — requires developer decision/legal/business action (otherwise disclose the data in ASC).

---

## LABEL.H Types of data

**Source text (verbatim):**
> Refer to the list of data types below and compare them to the data collection practices in your app.

| Category | Data type | Definition (verbatim) |
|---|---|---|
| Contact Info | Name | Such as first or last name |
| Contact Info | Email Address | Including but not limited to a hashed email address |
| Contact Info | Phone Number | Including but not limited to a hashed phone number |
| Contact Info | Physical Address | Such as home address, physical address, or mailing address |
| Contact Info | Other User Contact Info | Any other information that can be used to contact the user outside the app |
| Health & Fitness | Health | Health and medical data, including but not limited to data from the Clinical Health Records API, HealthKit API, Movement Disorder API, or health-related human subject research or any other user provided health or medical data |
| Health & Fitness | Fitness | Fitness and exercise data, including but not limited to the Motion and Fitness API |
| Financial Info | Payment Info | Such as form of payment, payment card number, or bank account number. If your app uses a payment service, the payment information is entered outside your app, and you as the developer never have access to the payment information, it is not collected and does not need to be disclosed. |
| Financial Info | Credit Info | Such as credit score |
| Financial Info | Other Financial Info | Such as salary, income, assets, debts, or any other financial information |
| Location | Precise Location | Information that describes the location of a user or device with the same or greater resolution as a latitude and longitude with three or more decimal places |
| Location | Coarse Location | Information that describes the location of a user or device with lower resolution than a latitude and longitude with three or more decimal places, such as Approximate Location Services |
| Sensitive Info | Sensitive Info | Such as racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data |
| Contacts | Contacts | Such as a list of contacts in the user’s phone, address book, or social graph |
| User Content | Emails or Text Messages | Including subject line, sender, recipients, and contents of the email or message |
| User Content | Photos or Videos | The user’s photos or videos |
| User Content | Audio Data | The user’s voice or sound recordings |
| User Content | Gameplay Content | Such as saved games, multiplayer matching or gameplay logic, or user-generated content in-game |
| User Content | Customer Support | Data generated by the user during a customer support request |
| User Content | Other User Content | Any other user-generated content |
| Browsing History | Browsing History | Information about content the user has viewed that is not part of the app, such as websites |
| Search History | Search History | Information about searches performed in the app |
| Identifiers | User ID | Such as screen name, handle, account ID, assigned user ID, customer number, or other user- or account-level ID that can be used to identify a particular user or account |
| Identifiers | Device ID | Such as the device’s advertising identifier, or other device-level ID |
| Purchases | Purchase History | An account’s or individual’s purchases or purchase tendencies |
| Usage Data | Product Interaction | Such as app launches, taps, clicks, scrolling information, music listening data, video views, saved place in a game, video, or song, or other information about how the user interacts with the app |
| Usage Data | Advertising Data | Such as information about the advertisements the user has seen |
| Usage Data | Other Usage Data | Any other data about user activity in the app |
| Diagnostics | Crash Data | Such as crash logs |
| Diagnostics | Performance Data | Such as launch time, hang rate, or energy use |
| Diagnostics | Other Diagnostic Data | Any other data collected for the purposes of measuring technical diagnostics related to the app |
| Surroundings | Environment Scanning | Such as mesh, planes, scene classification, and/or image detection of the user’s surroundings |
| Body | Hands | The user’s hand structure and hand movements |
| Body | Head | The user’s head movement |
| Other Data | Other Data Types | Any other data types not mentioned |

**Applies to:** All apps that collect data

- **[LABEL-17]** Has each data practice found in the app been compared against every data type in Apple's list and mapped to the matching type(s)?
  - quote: "Refer to the list of data types below and compare them to the data collection practices in your app."
  - surface: code
  - verify: Build a table: for each outbound payload field (from LABEL-03 inventory and SDK `PrivacyInfo.xcprivacy` `NSPrivacyCollectedDataType` values) pick the row above. Compare with ASC App Privacy > Data Types.
  - fix: Add missing types in ASC App Privacy > Data Types > Edit.
- **[LABEL-18]** If hashed emails or hashed phone numbers are sent off device, are they declared as Email Address / Phone Number?
  - quote: "Including but not limited to a hashed email address"
  - surface: code
  - verify: grep for `SHA256`, `CC_SHA256`, `CryptoKit` hashing applied to email/phone strings, or SDK APIs such as `setHashedEmail`, `setUserEmail`, `sha256_email_address`, advanced-matching options in ads SDKs.
  - fix: Declare Email Address and/or Phone Number in ASC.
- **[LABEL-19]** If the app reads HealthKit, Clinical Health Records, or Movement Disorder data (or user-provided health data) and sends it off device, is Health declared; if it sends Motion and Fitness / exercise data, is Fitness declared?
  - quote: "Health and medical data, including but not limited to data from the Clinical Health Records API, HealthKit API, Movement Disorder API"
  - surface: code
  - verify: Check entitlements for `com.apple.developer.healthkit`, grep `HKHealthStore`, `HKClinicalType`, `MovementDisorderManager`, `CMMotionActivityManager`, `CMPedometer`; trace whether results are uploaded.
  - fix: Declare Health and/or Fitness in ASC.
- **[LABEL-20]** Is payment information declared unless it is entered outside the app via a payment service and the developer never has access to it?
  - quote: "If your app uses a payment service, the payment information is entered outside your app, and you as the developer never have access to the payment information, it is not collected and does not need to be disclosed."
  - surface: code
  - verify: grep for custom card fields (`cardNumber`, `cvv`, `iban`, Stripe `STPPaymentCardTextField`/`PaymentSheet` usage). StoreKit/Apple Pay sheet = entered outside the app. In-app card fields whose values reach your servers → declare Payment Info.
  - fix: Declare Payment Info in ASC, or move entry to a payment service UI the developer cannot access.
- **[LABEL-21]** Is location sent off device declared as Precise Location when its resolution is three or more decimal places of latitude/longitude, and Coarse Location otherwise?
  - quote: "the same or greater resolution as a latitude and longitude with three or more decimal places"
  - surface: code
  - verify: grep `CLLocationManager`, `desiredAccuracy`, `accuracyAuthorization`, `NSLocationDefaultAccuracyReduced`, and how `coordinate.latitude`/`longitude` are serialized (rounding before upload).
  - fix: Declare the correct location type in ASC (or round to fewer than three decimal places before upload and declare Coarse Location).
- **[LABEL-22]** If the app uploads AR/scene data (mesh, planes, scene classification, image detection) or hand/head tracking data, are Environment Scanning / Hands / Head declared?
  - quote: "Such as mesh, planes, scene classification, and/or image detection of the user’s surroundings"
  - surface: code
  - verify: grep `ARMeshAnchor`, `ARPlaneAnchor`, `sceneReconstruction`, `ARKitSession`, `HandTrackingProvider`, `WorldTrackingProvider`, `DeviceAnchor`; trace upload.
  - fix: Declare Environment Scanning / Hands / Head in ASC.
- **[LABEL-23]** Are crash logs, performance metrics, and other diagnostics collected by the app or SDKs (e.g., crash reporters) declared as Crash Data / Performance Data / Other Diagnostic Data?
  - quote: "Such as crash logs"
  - surface: code
  - verify: Look for Crashlytics, Sentry, Bugsnag, Datadog, `MXMetricManager` payloads uploaded to your own server.
  - fix: Declare the Diagnostics types in ASC.
- **[LABEL-24]** Are user or device identifiers sent off device (account ID, handle, customer number; advertising identifier or other device-level ID) declared as User ID / Device ID?
  - quote: "Such as the device’s advertising identifier, or other device-level ID"
  - surface: code
  - verify: grep `advertisingIdentifier`, `identifierForVendor`, `ASIdentifierManager`, custom install UUIDs stored in Keychain/UserDefaults and sent in headers, SDK `setUserId`/`identify`.
  - fix: Declare User ID and/or Device ID in ASC.

---

## LABEL.I Data use (purposes)

**Source text (verbatim):**
> You should have a clear understanding of how each data type is used by you and your third-party partners.
>
> For example, collecting an email address and using it to authenticate the user and personalize the user’s experience within your app would include App Functionality and Product Personalization.

| Purpose | Definition (verbatim) |
|---|---|
| Third-Party Advertising | Such as displaying third-party ads in your app, or sharing data with entities who display third-party ads |
| Developer’s Advertising or Marketing | Such as displaying first-party ads in your app, sending marketing communications directly to your users, or sharing data with entities who will display your ads |
| Analytics | Using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics |
| Product Personalization | Customizing what the user sees, such as a list of recommended products, posts, or suggestions |
| App Functionality | Such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support |
| Other Purposes | Any other purposes not listed |

**Applies to:** All apps that declare any data type

- **[LABEL-25]** For each declared data type, are all purposes selected that the developer and third-party partners use it for (a type may need multiple purposes)?
  - quote: "You should have a clear understanding of how each data type is used by you and your third-party partners."
  - surface: asc
  - verify: In ASC App Privacy, open each data type; compare selected purposes with code usage: ads SDKs (AdMob, AppLovin, Meta Audience Network, Unity Ads) → Third-Party Advertising; marketing email/push campaigns (Braze, OneSignal, Mailchimp) → Developer’s Advertising or Marketing; analytics SDKs → Analytics; recommendations/feeds → Product Personalization; login/sync/crash reporting → App Functionality.
  - fix: Add missing purposes per data type in ASC and Publish.
- **[LABEL-26]** If the app displays third-party ads, is Third-Party Advertising selected for the data types the ad SDK uses?
  - quote: "Such as displaying third-party ads in your app, or sharing data with entities who display third-party ads"
  - surface: code
  - verify: grep for `GADMobileAds`, `GoogleMobileAds`, `ALSdk`, `FBAudienceNetwork`, `UnityAds`, `IronSource`, `GADBannerView`; read the SDK's `PrivacyInfo.xcprivacy` `NSPrivacyCollectedDataTypePurposes` for `NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising`.
  - fix: Select Third-Party Advertising for those data types in ASC.
- **[LABEL-27]** If the app sends marketing communications directly to users or shows first-party ads, is Developer’s Advertising or Marketing selected for the data used?
  - quote: "sending marketing communications directly to your users"
  - surface: manual
  - verify: Ask whether collected emails/phone numbers/push tokens are used for newsletters or promotional campaigns; look for marketing-consent checkboxes or Braze/Iterable/Customer.io SDKs.
  - fix: Select Developer’s Advertising or Marketing for those data types in ASC.

---

## LABEL.J Data linked to the user

**Source text (verbatim):**
> You’ll need to identify whether each data type is linked to the user’s identity (via their account, device, or other details) by you and/or your third-party partners. Data collected from an app is often linked to the user’s identity, unless specific privacy protections are put in place before collection to de-identify or anonymize it, such as:
> - Stripping data of any direct identifiers, such as user ID or name, before collection.
> - Manipulating data to break the linkage and prevent re-linkage to real-world identities.
>
> Additionally, in order for data not to be linked to a particular user’s identity, you must avoid certain activities after collection:
> - You must not attempt to link the data back to the user’s identity.
> - You must not tie the data to other datasets that enable it to be linked to a particular user’s identity.
>
> Note: “Personal Information” and “Personal Data”, as defined under relevant privacy laws, are considered linked to the user.

**Applies to:** All apps that declare any data type

- **[LABEL-28]** For every data type marked "not linked", were specific privacy protections put in place before collection to de-identify or anonymize it (Apple's examples: stripping direct identifiers such as user ID or name; manipulating data to break the linkage and prevent re-linkage), by both the developer and third-party partners?
  - quote: "Data collected from an app is often linked to the user’s identity, unless specific privacy protections are put in place before collection to de-identify or anonymize it"
  - surface: code
  - verify: For each type answered "not linked" in ASC, inspect the upload code and SDK configuration: any `userId`, account email, `identifierForVendor`, `advertisingIdentifier`, or install ID attached to the payload/session means it is linked.
  - fix: Change the answer to linked in ASC, or remove identifiers before upload.
- **[LABEL-29]** For data marked "not linked", does the developer attest it is never linked back to the user's identity or tied to other datasets that enable linking?
  - quote: "You must not tie the data to other datasets that enable it to be linked to a particular user’s identity."
  - surface: manual
  - verify: Ask the developer whether backend analytics joins this data with account tables, CRM, or other datasets.
  - fix: manual — requires developer decision/legal/business action (mark as linked in ASC if it is).
- **[LABEL-30]** Is data that counts as "Personal Information"/"Personal Data" under relevant privacy laws marked as linked to the user?
  - quote: "“Personal Information” and “Personal Data”, as defined under relevant privacy laws, are considered linked to the user."
  - surface: asc
  - verify: In ASC App Privacy, for each type answered "not linked" (especially Contact Info, Identifiers, Location), ask whether the data is "Personal Information"/"Personal Data" under the privacy laws that apply to the developer; if so, it must be marked linked.
  - fix: Mark the data type as linked to the user in ASC.

---

## LABEL.K Tracking

**Source text (verbatim):**
> You’ll need to understand whether you and/or your third-party partners use data from your app to track users and, if so, which data is used for this purpose.
>
> “Tracking” refers to linking data collected from your app about a particular end-user or device, such as a user ID, device ID, or profile, with Third-Party Data for targeted advertising or advertising measurement purposes, or sharing data collected from your app about a particular end-user or device with a data broker.
>
> “Third-Party Data” refers to any data about a particular end-user or device collected from apps, websites, or offline properties not owned by you.
>
> Examples of tracking include:
> - Displaying targeted advertisements in your app based on user data collected from apps and websites owned by other companies.
> - Sharing device location data or email lists with a data broker.
> - Sharing a list of emails, advertising IDs, or other IDs with a third-party advertising network that uses that information to retarget those users in other developers’ apps or to find similar users.
> - Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes. For example, using a login SDK that repurposes the data it collects from your app to enable targeted advertising in other developers’ apps.
>
> The following situations are not considered tracking:
> - When the data is linked solely on the end-user’s device and is not sent off the device in a way that can identify the end-user or device.
> - When the data broker uses the data shared with them solely for fraud detection or prevention or security purposes.
> - When the data broker is a consumer reporting agency and the data is shared with them for purposes of (1) reporting on a consumer’s creditworthiness or (2) obtaining information on a consumer’s creditworthiness for the specific purpose of making a credit determination.
>
> Learn more about tracking.

**Applies to:** All apps that declare any data type

- **[LABEL-31]** Is each data type that the developer or third-party partners use for tracking marked "used to track you" in ASC?
  - quote: "You’ll need to understand whether you and/or your third-party partners use data from your app to track users and, if so, which data is used for this purpose."
  - surface: asc
  - verify: In ASC App Privacy, for each data type check the tracking answer. Cross-check against tracking SDKs found in code and the `NSPrivacyTracking` / `NSPrivacyCollectedDataTypeTracking` values in bundled `PrivacyInfo.xcprivacy` files.
  - fix: Set the tracking answer to Yes for those data types in ASC and Publish.
- **[LABEL-32]** Does the app contain any third-party SDK that combines app data with other developers' apps' data for ad targeting/measurement (even if the developer doesn't use it for that)? If so, is that treated as tracking?
  - quote: "Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes."
  - surface: code
  - verify: For each SDK, read its `PrivacyInfo.xcprivacy`: `NSPrivacyTracking` = true or non-empty `NSPrivacyTrackingDomains` indicates tracking. Include login SDKs (e.g., Facebook Login) and attribution SDKs (AppsFlyer, Adjust, Branch, Kochava).
  - fix: Mark affected data as used for tracking in ASC and request ATT permission (LABEL.S), or remove/reconfigure the SDK.
- **[LABEL-33]** Does the app share location data, email lists, advertising IDs, or other IDs with a data broker or a third-party ad network for retargeting / lookalike audiences? If so, is it declared as tracking?
  - quote: "Sharing a list of emails, advertising IDs, or other IDs with a third-party advertising network that uses that information to retarget those users in other developers’ apps or to find similar users."
  - surface: manual
  - verify: Ask the developer about server-side exports (custom audiences, conversions APIs, data broker contracts); grep app code for ad-network conversion APIs that send hashed emails/IDs.
  - fix: Declare tracking in ASC and obtain ATT permission before such sharing, or stop the sharing.
- **[LABEL-34]** If data is not declared as tracking on the basis of an exception, does it fall strictly within one (linked only on device; broker used solely for fraud/security; consumer reporting agency for creditworthiness)?
  - quote: "When the data is linked solely on the end-user’s device and is not sent off the device in a way that can identify the end-user or device."
  - surface: manual
  - verify: Ask for the specific exception relied on and confirm the data flow matches it (e.g., broker contract limited to fraud prevention).
  - fix: manual — requires developer decision/legal/business action.

---

## LABEL.L Privacy links

**Source text (verbatim):**
> By adding the following links on your product page, you can help users easily access your app’s privacy policy and manage their data in your app.
>
> Privacy Policy (Required): The URL to your publicly accessible privacy policy.
>
> Privacy Choices (Optional): A publicly accessible URL where users can learn more about their privacy choices for your app and how to manage them. For example, a webpage where users can access their data, request deletion, or make changes.

**Applies to:** All apps (Privacy Policy); Privacy Choices is optional

- **[LABEL-35]** Is a Privacy Policy URL entered in App Store Connect?
  - quote: "Privacy Policy (Required): The URL to your publicly accessible privacy policy."
  - surface: asc
  - verify: ASC > App > App Privacy > "Privacy Policy" section: confirm the Privacy Policy URL field is non-empty (check each localization).
  - fix: Click Edit next to Privacy Policy, enter the URL, Save.
- **[LABEL-36]** Is the privacy policy URL publicly accessible (loads without login, no 4xx/5xx)?
  - quote: "The URL to your publicly accessible privacy policy."
  - surface: runtime
  - verify: `curl -sL -o /dev/null -w "%{http_code}" "<privacy policy URL>"` returns 200; open in a private browser window to confirm no login wall.
  - fix: Host the policy at a public URL and update the field in ASC.
- **[LABEL-37]** If a Privacy Choices URL is provided, is it publicly accessible and does it explain the user's privacy choices and how to manage them?
  - quote: "Privacy Choices (Optional): A publicly accessible URL where users can learn more about their privacy choices for your app and how to manage them."
  - surface: runtime
  - verify: Fetch the Privacy Choices URL (if set in ASC); confirm 200 without login and content about accessing data, deletion, or changes.
  - fix: Fix or remove the Privacy Choices URL in ASC.

---

## LABEL.M1 Additional guidance — Your app has web views

**Source text (verbatim):**
> Your app has web views.
>
> Data collected via web traffic must be declared, unless you are enabling the user to navigate the open web.

**Applies to:** Apps with web views
**Requires:** webview

- **[LABEL-38]** Is data collected through the app's web views (other than open-web browsing) declared on the label?
  - quote: "Data collected via web traffic must be declared, unless you are enabling the user to navigate the open web."
  - surface: code
  - verify: grep `WKWebView`, `SFSafariViewController`, `WebView(` (SwiftUI), `UIWebView`; for web views loading the developer's own/partner pages, list analytics/ads scripts and forms on those pages and confirm their data types are in ASC.
  - fix: Declare the web-collected data types in ASC.

## LABEL.M2 Additional guidance — You collect and store IP address from your users

**Source text (verbatim):**
> You collect and store IP address from your users.
>
> Declare the relevant data types based on how you use IP address, such as precise location, coarse location, device ID, or diagnostics.

**Applies to:** Apps whose backend or partners collect and store users' IP addresses

- **[LABEL-39]** If IP addresses are stored, are the relevant data types (e.g., precise/coarse location, device ID, diagnostics) declared according to how the IP is used?
  - quote: "Declare the relevant data types based on how you use IP address, such as precise location, coarse location, device ID, or diagnostics."
  - surface: manual
  - verify: Ask whether server logs/analytics retain IPs and for what (geo-IP lookup → location; identification → Device ID; debugging → Diagnostics).
  - fix: Declare the matching data types in ASC.

## LABEL.M3 Additional guidance — In-app private messaging

**Source text (verbatim):**
> You offer in-app private messaging between users that are not SMS text messages.
>
> Declare emails or text messages on your label. Text messages refer to both SMS and non-SMS messages.

**Applies to:** Apps with in-app private messaging between users
**Requires:** chat-social

- **[LABEL-40]** If the app offers private messaging between users, is "Emails or Text Messages" declared?
  - quote: "Declare emails or text messages on your label. Text messages refer to both SMS and non-SMS messages."
  - surface: code
  - verify: Look for chat/messaging features (Stream Chat, Sendbird, Firebase messages collections, custom `Message` models sent to a server).
  - fix: Declare Emails or Text Messages in ASC.

## LABEL.M4 Additional guidance — Game saves, multiplayer matching, or gameplay logic

**Source text (verbatim):**
> Your app includes game saves, multiplayer matching, or gameplay logic.
>
> Declare Gameplay Content on your label.

**Applies to:** Apps with game saves, multiplayer matching, or gameplay logic
**Requires:** game

- **[LABEL-41]** If the app includes game saves, multiplayer matching, or gameplay logic, is Gameplay Content declared?
  - quote: "Declare Gameplay Content on your label."
  - surface: code
  - verify: grep `GKSavedGame`, `saveGameData`, `GKMatchmaker`, `GKMatch`, cloud save to own backend, multiplayer SDKs (Photon, Nakama, PlayFab).
  - fix: Declare Gameplay Content in ASC.

## LABEL.M5 Additional guidance — Data varies by user group

**Source text (verbatim):**
> You collect different types of data from users depending on whether the user is a child, whether they are a free or paid user, whether they opt in, where they live, or for some other reason.
>
> Please disclose all data collected from your app, unless it meets all of the criteria outlined in the Optional Disclosure section. You may use the Privacy Choices or Privacy Policy links to provide additional detail about how your data collection practices may vary.

**Applies to:** Apps that collect different data from different user groups

- **[LABEL-42]** Does the label disclose the union of data collected across all user groups (child/adult, free/paid, opted-in/not, region), not only the default group?
  - quote: "Please disclose all data collected from your app, unless it meets all of the criteria outlined in the Optional Disclosure section."
  - surface: code
  - verify: grep for branches on subscription status, age, consent flags, `Locale.current.region`/`regionCode`, remote config gating SDK initialization; include data collected in every branch.
  - fix: Add the data types collected in any branch to ASC.

## LABEL.M6 Additional guidance — Apple frameworks or services

**Source text (verbatim):**
> You use Apple frameworks or services, such as MapKit, CloudKit, or App Analytics.
>
> If you collect data about your app from Apple frameworks or services, you should indicate what data you collect and how you use it. You are not responsible for disclosing data collected by Apple.

**Applies to:** Apps using Apple frameworks or services

- **[LABEL-43]** Is data that the developer collects about the app from Apple frameworks or services indicated on the label, with how it is used (Apple says "should"), noting that data collected by Apple itself is not the developer's responsibility to disclose?
  - quote: "If you collect data about your app from Apple frameworks or services, you should indicate what data you collect and how you use it. You are not responsible for disclosing data collected by Apple."
  - surface: code
  - verify: grep `CKContainer`, `publicCloudDatabase`, `MKLocalSearch`, etc.; determine whether the developer can access the stored data (e.g., CloudKit public database records) and confirm those types are declared.
  - fix: Declare developer-accessible data types in ASC.

## LABEL.M7 Additional guidance — Data used only on device

**Source text (verbatim):**
> You use location, device identifiers, and other sensitive data, but only on device, and the data is never sent to a server.
>
> Data that is processed only on device is not “collected” and does not need to be disclosed in your answers. If you derive anything from that data and send it off device, the resulting data should be considered separately.

**Applies to:** Apps that process sensitive data on device

- **[LABEL-44]** Is anything derived from on-device-only data (e.g., inferred categories, scores, summaries) and then sent off device considered and declared separately?
  - quote: "If you derive anything from that data and send it off device, the resulting data should be considered separately."
  - surface: code
  - verify: Trace outputs of on-device processing (Core ML predictions, Vision/NaturalLanguage results, location-derived regions) to network calls or analytics events.
  - fix: Declare the derived data types in ASC.

## LABEL.M8 Additional guidance — Precise location immediately coarsened

**Source text (verbatim):**
> You collect precise location, but immediately de-identify and coarsen it before storing.
>
> Disclose that you collect Coarse Location, since the precise location data is immediately coarsened and precise location is not stored.

**Applies to:** Apps that coarsen precise location before storing
**Requires:** location

- **[LABEL-45]** If precise location is immediately coarsened and precise location is not stored, is Coarse Location (rather than nothing) declared?
  - quote: "Disclose that you collect Coarse Location, since the precise location data is immediately coarsened and precise location is not stored."
  - surface: asc
  - verify: Confirm in ASC App Privacy that Location > Coarse Location is selected when the backend coarsens location on receipt.
  - fix: Declare Coarse Location in ASC.

## LABEL.M9 Additional guidance — Free-form text fields or voice recordings

**Source text (verbatim):**
> Your app includes free-form text fields or voice recordings, and users can save any type of information they want through those mediums, including names and health data.
>
> Mark "Other User Content" to represent generic free form text fields and "Audio Data" for voice recordings. You’re not responsible for disclosing all possible data that users may manually enter in the app through free-form fields or voice recordings. However, if you ask a user to input a specific data type into a text field, such as their name or email, or if you have a feature that enables users to upload a particular media type, such as photos or videos, then you’ll need to disclose the specific type of data.

**Applies to:** Apps with free-form text fields or voice recordings that are collected

- **[LABEL-46]** Are uploaded free-form text fields declared as "Other User Content" and uploaded voice recordings as "Audio Data"?
  - quote: "to represent generic free form text fields"
  - surface: code
  - verify: Find user notes/posts/comments and `AVAudioRecorder`/`SFSpeechRecognizer` server uploads; confirm the types in ASC.
  - fix: Declare Other User Content / Audio Data in ASC.
- **[LABEL-47]** Where the app asks for a specific data type in a text field (e.g., name, email) or lets users upload a specific media type (e.g., photos, videos), is that specific type declared?
  - quote: "if you ask a user to input a specific data type into a text field, such as their name or email, or if you have a feature that enables users to upload a particular media type, such as photos or videos, then you’ll need to disclose the specific type of data."
  - surface: code
  - verify: grep `textContentType(.emailAddress)`, `.name`, `.telephoneNumber`, `.fullStreetAddress`, placeholder strings like "Email", `PhotosPicker`, `PHPickerViewController`, `UIImagePickerController` combined with upload code.
  - fix: Declare the specific data types (Name, Email Address, Photos or Videos, etc.) in ASC.

## LABEL.M10 Additional guidance — Data not retained after servicing the request

**Source text (verbatim):**
> You collect data to service a request but do not retain it after servicing the request.
>
> "Collect" refers to transmitting data off the device and storing it in a readable form for longer than the time it takes you and/or your third-party partners to service the request. For example, if an authentication token or IP address is sent on a server call and not retained, or if data is sent to your servers then immediately discarded after servicing the request, you do not need to disclose this in your answers in App Store Connect.

**Applies to:** Apps that omit data on the basis that it is not retained

- **[LABEL-48]** For data omitted because it is "not retained", does the developer confirm it is immediately discarded after servicing the request by them and all third-party partners (including logs)?
  - quote: "if data is sent to your servers then immediately discarded after servicing the request, you do not need to disclose this in your answers in App Store Connect."
  - surface: manual
  - verify: Ask the developer about server/API-gateway/CDN log retention and any vendor (e.g., AI API, translation API) retention policy for the payload.
  - fix: manual — requires developer decision/legal/business action (declare if retained).

## LABEL.M11 Additional guidance — Referencing legal consent in the ATT prompt

**Source text (verbatim):**
> You’d like your app to reference consent requests so you can comply with local privacy laws in its App Tracking Transparency prompt.
>
> If you’ve already shown the user a required government data-privacy consent prompt that is also covered by App Tracking Transparency (for example, through a third-party Consent Management Platform), you can reference that in your app’s App Tracking Transparency purpose string. Here’s an example of a purpose string that clearly explains the user’s choice:
>
> “[App] indicates you allowed it to use your data for advertising purposes in its legal prompt. Would you like your Apple device to provide [App] access to the advertising ID or otherwise allow it to use other means for the data processing described above?”

**Applies to:** Apps that show a government-required consent prompt (e.g., via a CMP) before the ATT prompt and reference it in the purpose string
**Requires:** tracking, ads, analytics

- **[LABEL-49]** If the ATT purpose string references a prior legal consent prompt, does it clearly explain the user's choice (as in Apple's example)?
  - quote: "Here’s an example of a purpose string that clearly explains the user’s choice"
  - surface: code
  - verify: Read `NSUserTrackingUsageDescription` in Info.plist / `InfoPlist.strings` / `InfoPlist.xcstrings`; if it references a prior consent, confirm it states what the user allowed and what the ATT choice controls.
  - fix: Rewrite the purpose string along the lines of Apple's example.

---

## LABEL.N App Store Connect — Manage app privacy (requirements)

**Source text (verbatim):**
> You’re required to provide a privacy policy URL for your iOS app platform and privacy policy text for your tvOS app platform. Offering a privacy choices URL is optional. Furthermore, if you're distributing your app on the App Store, you're required to explain your data handling practices in App Store Connect. This informs users about the data that may be collected through your app and how it may be used.
>
> Your responses to the app privacy questions are used to help inform customers about your app’s data practices. Based on the information you submit, your App Store product page will be updated to include details about the app's data collection and usage.
>
> Responses are provided at the app level and should accurately represent your app's data practices across all platforms. You should answer in the most comprehensive and inclusive way if your app collects more data on one platform than another. You must include information about your app's privacy practices and those of third-party partners whose code you integrate into your app.
>
> Note: You’re responsible for keeping your responses accurate and up to date. If your practices change, update your responses in App Store Connect.
>
> Learn about privacy and data.
>
> Learn about responding to app privacy questions.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** All apps distributed on the App Store; tvOS text applies to apps with a tvOS platform

- **[LABEL-50]** If the app has a tvOS platform, is privacy policy text entered for the tvOS app platform?
  - quote: "privacy policy text for your tvOS app platform"
  - surface: asc
  - verify: ASC > App > App Privacy > Privacy Policy: check the "Apple TV Privacy Policy" field is filled when a tvOS platform exists (check the project for a tvOS target / `SDKROOT = appletvos`).
  - fix: Edit Privacy Policy and paste the policy text into the Apple TV Privacy Policy field; Save.
- **[LABEL-51]** For multi-platform apps, do the app-level responses cover the most data collected on any platform (most comprehensive and inclusive answer)?
  - quote: "You should answer in the most comprehensive and inclusive way if your app collects more data on one platform than another."
  - surface: code
  - verify: List all targets (iOS, iPadOS, macOS, watchOS, tvOS, visionOS, extensions/widgets); run the LABEL-03 inventory per target and take the union; compare to ASC.
  - fix: Add data types collected on any platform to ASC.

---

## LABEL.O App Store Connect — Answering app privacy questions (procedure)

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click App Privacy.
> - On the right, click Get Started.
> - In the dialog that appears, indicate whether you or your third-party partners collect data from your app.
> - If the answer is no, select "No, we do not collect data from this app" and then click Save. You don’t need to answer any further questions.
> - If the answer is yes, select "Yes, we collect data from this app" and then click Next.
> - Select all of the data you or your third-party partners collect from this app and click Save.
>
> If your app is currently available on the App Store, make sure your responses reflect the data collected only from that app version.
> - In the Data Types section, click each data type and answer the questions that follow. If at any point you want to update your data types, click Edit next to Data Types.
> - Click Save when finished.
> - Your responses appear in each data type section. Scroll to the Product Page Preview section to view how this information will appear on the App Store. To view product page details, click See Details.
> - On the top right of the page, click Publish.
> - A dialog appears confirming that you agree that your responses are accurate, comply with the App Review Guidelines and applicable law, and that you will promptly update your responses if your data practices change. To agree and continue, click Publish. Your responses will be published on your product page on the App Store. If your product page isn’t live yet, your responses will be published once your product page goes live.

**Applies to:** All apps distributed on the App Store

- **[LABEL-52]** If ASC says "No, we do not collect data from this app", is it true that neither the app nor any third-party partner collects data?
  - quote: "indicate whether you or your third-party partners collect data from your app."
  - surface: code
  - verify: If ASC shows the "no data collected" answer, confirm the app has no analytics/ads/crash SDKs, no backend that retains user data, and no `PrivacyInfo.xcprivacy` (app or SDK) declaring `NSPrivacyCollectedDataTypes`.
  - fix: Switch to "Yes, we collect data from this app" and declare the types.
- **[LABEL-53]** Has every selected data type had its follow-up questions answered (no incomplete data type sections)?
  - quote: "In the Data Types section, click each data type and answer the questions that follow."
  - surface: asc
  - verify: In ASC App Privacy, open each data type card and confirm purposes, linked, and tracking answers are set.
  - fix: Answer the remaining questions for each data type and Save.
- **[LABEL-54]** Have the responses been Published (not only saved)?
  - quote: "On the top right of the page, click Publish."
  - surface: asc
  - verify: On the App Privacy page, check whether a Publish button is still active / unpublished-changes indicator is shown.
  - fix: Click Publish and confirm the dialog.
- **[LABEL-55]** Does the Product Page Preview in ASC match the data practices found in the audit?
  - quote: "Scroll to the Product Page Preview section to view how this information will appear on the App Store."
  - surface: asc
  - verify: Scroll to Product Page Preview, click See Details, and compare the "Data Used to Track You", "Data Linked to You", and "Data Not Linked to You" groupings to the audit's findings.
  - fix: Edit the data type answers and Publish.

---

## LABEL.P App Store Connect — Adding, removing, and updating data types

**Source text (verbatim):**
> Updates to data types will be published after you click Publish. If you select new data types, you must complete their setup by responding to the questions in each data type section before publishing.
> - In Apps, select the app you want to view.
> - In the sidebar, click App Privacy.
> - Next to Data Types, click Edit.
> - Update your selections for all of the data you or your third-party partners collect from this app.
>
> If your app is currently available on the App Store, ensure that your responses reflect the data collected only from that app version.
> - If you removed an existing data type, click Publish. Your responses to this data type will be removed from your app’s product page.
> - If you added a new data type, click Continue, then complete the setup for the newly added data type by clicking into it and responding to the questions that follow. Once completing your responses to the questions, click Publish. Your responses to the newly added data type will appear on your app’s product page after publishing.
> - If you have added a new data type and removed an existing one, click Publish, then click Continue. Your responses to the removed data type will be removed from your app's product page. You need to complete the setup for the newly added data type by clicking into it and responding to the questions that follow. Once you have finished responding to the questions, click Publish. Your responses to the newly added data type will appear on your app's product page after publishing.
>
> Updating app privacy responses
> - In Apps, select the app you want to view.
> - In the sidebar, select App privacy.
> - To edit existing responses, on the right, click on the data type you'd like to update your responses for.
> - Update your responses, then click Publish. Your updated responses will be published on your app’s product page after you click Publish.
>
> Below the Product Page Preview section on the App Store Connect, you can preview how this information about your app's data collection and usage will appear. To view the details of the product page preview, click See Details.

**Applies to:** Apps updating their App Privacy responses

- **[LABEL-56]** Are any newly added data types fully set up (questions answered) before publishing?
  - quote: "If you select new data types, you must complete their setup by responding to the questions in each data type section before publishing."
  - surface: asc
  - verify: In ASC App Privacy, any newly added type card must show purposes/linked/tracking answers.
  - fix: Click into the new type, answer the questions, then Publish.
- **[LABEL-57]** If the app is live, do the published responses reflect the data collected only by the live app version (so that changes for the upcoming version are timed correctly)?
  - quote: "If your app is currently available on the App Store, ensure that your responses reflect the data collected only from that app version."
  - surface: manual
  - verify: Compare the live version's SDK set (from the previous release tag) with the upcoming build's SDK set; decide with the developer when to publish updated responses.
  - fix: manual — requires developer decision/legal/business action.

---

## LABEL.Q App Store Connect — Entering privacy policy information

**Source text (verbatim):**
> In App Store Connect, you can enter privacy policy and user privacy choices URLs for your iOS and macOS app platforms, and privacy policy text for your tvOS app platform. A privacy policy URL is required for all apps, while a user privacy choices URL is optional. The URLs for your iOS app and macOS app platform and the text for your tvOS app platform can be updated if your app is in an editable app status. Learn more about required, localizable, and editable properties.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
> - In Apps, select the app you want to view.
> - In the sidebar, select App privacy.
> - Next to Privacy Policy, click Edit.
> - Enter the privacy policy URL and optionally, the user privacy choices URL. If your app includes a tvOS platform, enter the text of your privacy policy in the Apple TV Privacy Policy field.
>
> Note: You can localize the privacy policy URLs and text in all of the languages your app is available in.
> - Click Save.
>
> Any changes to the URLs releases with your next app version.

**Applies to:** All apps

- **[LABEL-58]** Is a privacy policy URL set for every app platform in ASC (iOS and macOS where present)?
  - quote: "A privacy policy URL is required for all apps, while a user privacy choices URL is optional."
  - surface: asc
  - verify: ASC > App > App Privacy > Privacy Policy: confirm the URL exists; if the app has localizations, check the URL is present for each localization shown.
  - fix: Edit next to Privacy Policy, enter the URL, Save.
- **[LABEL-59]** Has a changed privacy policy URL been entered before submitting, given that URL changes release only with the next app version?
  - quote: "Any changes to the URLs releases with your next app version."
  - surface: asc
  - verify: If the policy URL moved, confirm the new URL is saved in ASC before the version is submitted for review.
  - fix: Update the URL in ASC and include it with the next version submission.

---

## LABEL.R User privacy and data use — Privacy Nutrition Labels and privacy manifests

**Source text (verbatim):**
> At Apple, we believe privacy is a fundamental human right. That’s why we’ve built a number of features to help users understand developers’ privacy and data collection and sharing practices, and put users in the driver’s seat when it comes to their data. With Privacy Nutrition Labels on the App Store and in App Privacy Report, users can see what data an app collects and how it’s used. And App Tracking Transparency (ATT) empowers users to choose whether an app has permission to track their activity across other companies’ apps and websites for the purposes of advertising or sharing with data brokers.
>
> Privacy Nutrition Labels
>
> The App Store helps users better understand an app’s privacy practices before they download the app. On each app’s product page, users can learn about some of the data types an app may collect, and whether the information is used to track them or is linked to their identity or device. In order to submit new apps and app updates, you must provide information about your privacy practices in App Store Connect.
>
> Privacy manifests
>
> If your app uses third-party code, such as advertising or analytics SDKs, you must describe what data it collects, how it is used, and whether it tracks users. Privacy manifest files outline these practices in a single standard format. When you prepare to distribute your app, Xcode combines all these manifests into one comprehensive report, making it easier for you to create accurate Privacy Nutrition Labels.

**Applies to:** All apps; privacy manifest text applies to apps using third-party code

- **[LABEL-60]** Do the ASC labels agree with the privacy report Xcode builds from all bundled privacy manifests (Apple describes this report as an aid to accurate labels, not a separate requirement)?
  - quote: "When you prepare to distribute your app, Xcode combines all these manifests into one comprehensive report, making it easier for you to create accurate Privacy Nutrition Labels."
  - surface: code
  - verify: Archive the app; in Organizer, right-click the archive > Generate Privacy Report; compare every "Data Collected" row with ASC App Privacy. Alternatively parse each `PrivacyInfo.xcprivacy` with `plutil -p`.
  - fix: Update ASC responses to include every collected type in the report.
- **[LABEL-61]** For third-party code such as advertising or analytics SDKs, are what it collects, how it is used, and whether it tracks described (via privacy manifests)?
  - quote: "If your app uses third-party code, such as advertising or analytics SDKs, you must describe what data it collects, how it is used, and whether it tracks users."
  - surface: code
  - verify: For each third-party SDK, check its bundle contains `PrivacyInfo.xcprivacy` (`find <DerivedData or Pods or SourcePackages> -name PrivacyInfo.xcprivacy`); note SDKs without one.
  - fix: Update the SDK to a version that ships a privacy manifest; ensure its data is reflected in ASC.

---

## LABEL.S Ask permission to track

**Source text (verbatim):**
> In iOS 14.5, iPadOS 14.5, and tvOS 14.5 or later, you need to receive the user’s permission through the App Tracking Transparency (ATT) framework in order to track them or access their device’s advertising identifier. Tracking refers to the act of linking user or device data collected from your app with user or device data collected from other companies’ apps, websites, or offline properties for targeted advertising or advertising measurement purposes. Tracking also refers to sharing user or device data with data brokers.
>
> Examples of tracking include, but are not limited to:
> - Displaying targeted advertisements in your app based on user data collected from apps and websites owned by other companies.
> - Sharing device location data or email lists with a data broker.
> - Sharing a list of emails, advertising IDs, or other IDs with a third-party advertising network that uses that information to retarget those users in other developers’ apps or to find similar users.
> - Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes. For example, using an analytics SDK that repurposes the data it collects from your app to enable targeted advertising in other developers’ apps.
>
> The following use cases are not considered tracking, and do not require user permission through the App Tracking Transparency framework:
> - When user or device data from your app is linked to third-party data solely on the user's device and is not sent off the device in a way that can identify the user or device.
> - When the data broker with whom you share data uses the data solely for fraud detection, fraud prevention, or security purposes. For example, using a data broker solely to prevent credit card fraud.
> - When the data broker is a consumer reporting agency and the data is shared with them for purposes of (1) reporting on a consumer's creditworthiness, or (2) obtaining information on a consumer's creditworthiness for the specific purpose of making a credit determination.

**Applies to:** Apps on iOS 14.5, iPadOS 14.5, and tvOS 14.5 or later that track users or access the advertising identifier
**Requires:** tracking, ads, analytics

- **[LABEL-62]** If the app (or any SDK in it) tracks users or reads the advertising identifier, does it request permission through the ATT framework?
  - quote: "you need to receive the user’s permission through the App Tracking Transparency (ATT) framework in order to track them or access their device’s advertising identifier."
  - surface: code
  - verify: grep for `ASIdentifierManager`, `advertisingIdentifier`, `AdSupport`, and tracking SDKs (ads, attribution); grep for `import AppTrackingTransparency` and `ATTrackingManager.requestTrackingAuthorization`. Tracking present but no request call → fail.
  - fix: Add `NSUserTrackingUsageDescription` and call `ATTrackingManager.requestTrackingAuthorization` before any tracking/IDFA access.
- **[LABEL-63]** If ASC declares any data "used to track you", does the app implement the ATT permission request before that tracking?
  - quote: "Tracking refers to the act of linking user or device data collected from your app with user or device data collected from other companies’ apps, websites, or offline properties for targeted advertising or advertising measurement purposes."
  - surface: asc
  - verify: Compare ASC App Privacy tracking answers with presence of `requestTrackingAuthorization` in code. (A mismatch in the other direction, ATT requested but no tracking declared, is not covered by this text; flag it for review against LABEL-31 instead.)
  - fix: Add the ATT request, or correct the ASC answers if the data is not actually used for tracking.
- **[LABEL-64]** Are tracking SDKs (including analytics SDKs that repurpose data for ads in other developers' apps) prevented from tracking until ATT permission is granted?
  - quote: "For example, using an analytics SDK that repurposes the data it collects from your app to enable targeted advertising in other developers’ apps."
  - surface: runtime
  - verify: Fresh install; before answering ATT, monitor network for requests to domains listed in SDK `NSPrivacyTrackingDomains`; in code, check SDK init/consent flags (e.g., ad-personalization or tracking-enabled flags) are set from `trackingAuthorizationStatus`.
  - fix: Defer SDK tracking features until `.authorized`; configure SDK non-tracking mode when denied.

---

## LABEL.T Using the App Tracking Transparency framework

**Source text (verbatim):**
> To request permission to track the user and access the device’s advertising identifier, use the App Tracking Transparency framework. You must also include a purpose string in the system prompt that explains why you’d like to track the user. Unless you receive permission from the user to enable tracking, the device’s advertising identifier value will be all zeros and you may not track them as described above.
>
> While you can display the App Tracking Transparency prompt whenever you choose, the device’s advertising identifier value will only be returned once you present the prompt and the user grants permission. Use the purpose string to explain what this data will be used for to help the user understand what they’re opting in to share. If the user allows apps to request to track, but has turned tracking off for your app, you can ask the user to change their preference for your app by providing a shortcut to Settings where they can change the tracking permission.
>
> The identifier for vendor (IDFV) may be used for analytics across apps from the same content provider. In this case, the use of the App Tracking Transparency framework is not required. The IDFV may not be combined with other data to track a user across apps and websites owned by other companies. You remain fully responsible for ensuring that your collection and use of the IDFV comply with applicable law.

**Applies to:** Apps that track or access the advertising identifier; IDFV paragraph applies to apps using identifierForVendor

- **[LABEL-65]** Does the ATT purpose string explain why the app would like to track the user and what the data will be used for?
  - quote: "You must also include a purpose string in the system prompt that explains why you’d like to track the user."
  - surface: code
  - verify: Read `NSUserTrackingUsageDescription` (Info.plist, `INFOPLIST_KEY_NSUserTrackingUsageDescription` build setting, `InfoPlist.strings`/`.xcstrings` per language). Fail if empty, generic ("We need this"), or not explaining the use.
  - fix: Write a specific purpose string, e.g., describing personalized ads / ad measurement, and localize it.
- **[LABEL-66]** When ATT is not authorized, does the app refrain from tracking (no alternative tracking path)?
  - quote: "Unless you receive permission from the user to enable tracking, the device’s advertising identifier value will be all zeros and you may not track them as described above."
  - surface: runtime
  - verify: Deny ATT on a device; exercise the app; confirm via proxy that no hashed emails/IDs or fingerprints are sent to ad/attribution endpoints; in code check that tracking code paths check `trackingAuthorizationStatus == .authorized`.
  - fix: Gate all tracking on `.authorized`.
- **[LABEL-67]** If the app asks a user who allows tracking requests but has turned tracking off for this app to change their preference, does it do so by providing a shortcut to Settings where they can change the tracking permission (the mechanism Apple describes; offering it is optional)?
  - quote: "you can ask the user to change their preference for your app by providing a shortcut to Settings where they can change the tracking permission."
  - surface: code
  - verify: grep for `UIApplication.openSettingsURLString` near tracking-related UI.
  - fix: Use `UIApplication.shared.open(URL(string: UIApplication.openSettingsURLString)!)` for the shortcut.
- **[LABEL-68]** If the app uses `identifierForVendor` without ATT, is it used only for analytics across the same vendor's apps and never combined with other data to track across other companies' apps and websites?
  - quote: "The IDFV may not be combined with other data to track a user across apps and websites owned by other companies."
  - surface: code
  - verify: grep `identifierForVendor`; trace where the value is sent; fail if passed to ad/attribution SDKs or data brokers without ATT authorization.
  - fix: Stop sending IDFV to third-party ad/attribution services, or gate it behind ATT authorization.

---

## LABEL.U ATT in the European Union

**Source text (verbatim):**
> As part of agreements with select European competition authorities, Apple is introducing changes to its App Tracking Transparency framework in the European Union. Beginning with iOS 27.2 and iPadOS 27.2, developers will have the option to use an alternative version of the App Tracking Transparency system prompt in the EU. The requirements for when you must seek permission to track users will remain the same. Due to legal requirements, only the alternative version of the system prompt is available for apps distributed in Germany, France, Italy, Poland, and Romania.
>
> The alternative version of the App Tracking Transparency system prompt has modified formatting and language and provides you the option to use a text button labeled “Additional Information.” This allows you to surface additional information about your request to link user or device data collected from your app with user or device data collected from other companies’ apps, websites, or offline properties for targeted advertising or advertising measurement purposes, or to share user or device data with a data broker.
>
> In addition, for users in the European Union, you can reprompt a user via the App Tracking Transparency system prompt one year after the user’s previous choice in your app’s App Tracking Transparency system prompt, regardless of whether that choice was to accept or reject. A user cannot be re-prompted if they have disabled “Allow Apps to Request to Track” (renamed to “Allow Apps to Request to Link Your Activity Across Companies” in the EU) in their device’s Settings.
>
> For technical details on using the alternative App Tracking Transparency system prompt and optional text button in the European Union, see:
> - Requesting Authorization with Expanded Interface (new)
> - Requesting Authorization
> - Tracking Markdown Usage Description (new)
> - Tracking Usage Description

**Applies to:** Apps that request ATT and are distributed in the European Union
**Requires:** tracking, ads, analytics

- **[LABEL-69]** If the app is distributed in Germany, France, Italy, Poland, or Romania, has the ATT flow been tested with the alternative (full-page) prompt that is the only version available there?
  - quote: "Due to legal requirements, only the alternative version of the system prompt is available for apps distributed in Germany, France, Italy, Poland, and Romania."
  - surface: runtime
  - verify: Check ASC > Pricing and Availability for these countries; on an iOS 27.2+ device in one of those regions with a matching Apple Account, trigger the ATT request and confirm the prompt text (from `NSUserTrackingMarkdownUsageDescription` if set, else `NSUserTrackingUsageDescription`) reads correctly.
  - fix: Provide/adjust `NSUserTrackingMarkdownUsageDescription` and its localizations (de, fr, it, pl, ro).
- **[LABEL-70]** If the app re-prompts EU users for ATT, does it do so via the App Tracking Transparency system prompt, no sooner than one year after the user's previous choice, and not for users who disabled "Allow Apps to Request to Track"?
  - quote: "you can reprompt a user via the App Tracking Transparency system prompt one year after the user’s previous choice in your app’s App Tracking Transparency system prompt, regardless of whether that choice was to accept or reject."
  - surface: code
  - verify: Inspect logic around repeated `requestTrackingAuthorization` calls; confirm the re-prompt is the system API (the system "doesn’t allow the prompt to display again until a year passes", see LABEL.Y) rather than a custom screen that asks for the tracking decision again.
  - fix: Re-prompt only through the system API; remove custom screens that re-ask the ATT question.

---

## LABEL.V1 FAQ — Gating functionality or incentivizing tracking consent

**Source text (verbatim):**
> Can I gate functionality on agreeing to allow tracking, or incentivize users to agree to allow tracking in the App Tracking Transparency prompt?
>
> No, per the App Review Guidelines: 5.1.2(i).

**Applies to:** Apps that request ATT
**Requires:** tracking, ads, analytics

- **[LABEL-71]** Does the app keep all functionality available, and offer no incentive, regardless of the ATT answer?
  - quote: "No, per the App Review Guidelines: 5.1.2(i)."
  - surface: runtime
  - verify: Deny ATT; exercise all features. In code, grep for branches on `trackingAuthorizationStatus` / `.denied` that disable features, show "allow tracking to continue", or grant rewards (coins, unlocks) for `.authorized`.
  - fix: Remove gating and incentives tied to the ATT result.

## LABEL.V2 FAQ — Explaining before the tracking prompt

**Source text (verbatim):**
> Can I explain to users why I would like permission to track them before I show the tracking permission prompt?
>
> Yes, so long as you are transparent to users about your use of the data in your explanation. Per the App Review Guidelines: 5.1.1 (iv), apps must respect the user's permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access.

**Applies to:** Apps that show a pre-prompt screen before ATT
**Requires:** tracking, ads, analytics

- **[LABEL-72]** If the app shows an explanation screen before the ATT prompt, is it transparent about the data use and free of manipulation, tricks, or force?
  - quote: "apps must respect the user's permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access."
  - surface: runtime
  - verify: Fresh install; view the pre-prompt. Fail if it mimics the system alert, has only a "Continue/Allow" button leading straight into ATT with misleading copy, or implies features require tracking.
  - fix: Rewrite the pre-prompt copy to describe the data use accurately; avoid misleading design.

## LABEL.V3 FAQ — Other identifiers without permission

**Source text (verbatim):**
> If I have not received permission from a user via the tracking permission prompt, can I use an identifier other than the IDFA (for example, a hashed email address or hashed phone number) to track that user?
>
> No. You will need to receive the user's permission through the App Tracking Transparency framework to track that user.

**Applies to:** Apps that send hashed emails/phone numbers or other IDs to ad/attribution services
**Requires:** tracking, ads, analytics

- **[LABEL-73]** Without ATT authorization, does the app avoid sending hashed emails, hashed phone numbers, or other identifiers to ad/attribution services for tracking?
  - quote: "You will need to receive the user's permission through the App Tracking Transparency framework to track that user."
  - surface: code
  - verify: grep for hashed-identifier APIs in ads/attribution SDKs (e.g., `setUserEmails`, `setHashedEmail`, advanced matching, `setCustomerUserId` forwarded to ad partners) and confirm they are gated by `.authorized`.
  - fix: Gate those calls on ATT authorization.

## LABEL.V4 FAQ — Consent collected on a website

**Source text (verbatim):**
> If a user provides permission for tracking via a separate process on our website, but declines permission in the App Tracking Transparency prompt, can I track that user across apps and websites owned by other companies?
>
> Developers must get permission via the App Tracking Transparency prompt for data that's collected in the app and used for tracking. Data collected separately, outside of the app and not related to the app, is not in scope.

**Applies to:** Apps whose developer also collects tracking consent outside the app
**Requires:** tracking, ads, analytics

- **[LABEL-74]** Is in-app data used for tracking only when ATT permission was granted, regardless of consent the user gave elsewhere (e.g., on a website)?
  - quote: "Developers must get permission via the App Tracking Transparency prompt for data that's collected in the app and used for tracking."
  - surface: code
  - verify: Check that tracking gates read `ATTrackingManager.trackingAuthorizationStatus`, not a server-side or web consent flag alone.
  - fix: Use the ATT status as the gate for in-app tracking.

## LABEL.V5 FAQ — Fingerprinting

**Source text (verbatim):**
> Can I fingerprint or use signals from the device to try to identify the device or a user?
>
> No. Per the Apple Developer Program License Agreement, you may not derive data from a device for the purpose of uniquely identifying it. Examples of user or device data include, but are not limited to: properties of a user's web browser and its configuration, the user's device and its configuration, the user's location, or the user's network connection. Apps that are found to be engaging in this practice, or that reference SDKs (including but not limited to Ad Networks, Attribution services, and Analytics) that are, may be rejected from the App Store.

**Applies to:** All apps

- **[LABEL-75]** Is the app (and every referenced SDK) free of device fingerprinting — deriving data from the device, browser, location, or network connection to uniquely identify it?
  - quote: "you may not derive data from a device for the purpose of uniquely identifying it."
  - surface: code
  - verify: grep for combinations of device signals sent together to servers: `UIDevice.current.name`, `systemUptime`, `ProcessInfo.processInfo.systemUptime`, `sysctlbyname("hw.machine")`, `UIScreen.main.brightness`, `CTCarrier`, battery level, locale/timezone, disk space, keyboard list, used to build an ID. Check attribution/ads/analytics SDK versions and their documentation for "probabilistic"/"fingerprint" matching features.
  - fix: Remove fingerprinting code; disable probabilistic matching in SDKs or replace the SDK.

## LABEL.V6 FAQ — Consumer reporting agency (fraud and credit)

**Source text (verbatim):**
> If I share data with a consumer reporting agency to conduct fraud checks, and separately share data with them as part of a credit check or for credit reporting purposes, do I need permission to track?
>
> No. You do not need permission from the user when a data broker uses the data shared with them solely for fraud detection or prevention or security purposes. You also do not need permission from the user when sharing data with a consumer reporting agency and the data is shared with them for purposes of (1) reporting on a consumer's creditworthiness, or (2) obtaining information on a consumer's creditworthiness for the specific purpose of making a credit determination.

**Applies to:** Apps sharing data with data brokers or consumer reporting agencies

- **[LABEL-76]** If data sharing with a data broker or consumer reporting agency is treated as not requiring ATT, is it solely for fraud detection/prevention/security or for the stated creditworthiness purposes?
  - quote: "You do not need permission from the user when a data broker uses the data shared with them solely for fraud detection or prevention or security purposes."
  - surface: manual
  - verify: Ask the developer for the broker/agency relationship and the contractual purpose.
  - fix: manual — requires developer decision/legal/business action.

## LABEL.V7 FAQ — Deep-linking and deferred deep-linking tools

**Source text (verbatim):**
> Do I need to use the App Tracking Transparency framework to get user permission to use third-party deep-linking or deferred deep-linking tools?
>
> Yes. If your application uses any third-party services that pass unique identifiers or create a shared identity of the user between applications from different companies for ad targeting, ad measurement, or sharing with a data broker, your app will need to request permission from the user using the App Tracking Transparency framework.

**Applies to:** Apps using third-party deep-linking or deferred deep-linking services

- **[LABEL-77]** If the app uses third-party deep-linking/deferred deep-linking services that pass unique identifiers or create a shared identity across companies' apps for ad targeting/measurement or data brokers, does it request ATT permission?
  - quote: "your app will need to request permission from the user using the App Tracking Transparency framework."
  - surface: code
  - verify: grep for Branch (`Branch.getInstance`), AppsFlyer (`AppsFlyerLib`), Adjust (`Adjust.appDidLaunch`), Kochava, Firebase Dynamic Links, Singular; confirm `requestTrackingAuthorization` is called and the SDK waits for it (e.g., AppsFlyer `waitForATTUserAuthorization`).
  - fix: Add the ATT request and configure the SDK to wait for the result.

## LABEL.V8 FAQ — Responsibility for integrated SDKs

**Source text (verbatim):**
> I have integrated an SDK from another company. Am I responsible for the data collection and tracking of users of my app by that company?
>
> Yes. Developers are responsible for all code included in their apps. If you are unsure about the data collection and tracking practices of code used in your app that you didn't write, we suggest contacting the developer of the SDK.

**Applies to:** Apps integrating SDKs from other companies

- **[LABEL-78]** Are the data collection and tracking practices of every integrated SDK known (from its privacy manifest/documentation or the SDK developer)?
  - quote: "Developers are responsible for all code included in their apps."
  - surface: code
  - verify: For each dependency, record its `PrivacyInfo.xcprivacy` contents (`NSPrivacyTracking`, `NSPrivacyTrackingDomains`, `NSPrivacyCollectedDataTypes`); flag SDKs without a manifest or documentation as "unknown practices".
  - fix: Contact the SDK developer or replace the SDK; reflect its practices in ASC.

## LABEL.V9 FAQ — Single sign-on from another company

**Source text (verbatim):**
> I have integrated single sign-on functionality provided by another company. Am I responsible for the data collection and tracking practices of that company?
>
> Yes. Developers are responsible for all code included in their app, including single sign-on (SSO) functionality provided by third parties. If the user will be subject to tracking as a result of SSO functionality included in your app, you must use the App Tracking Transparency prompt to obtain permission from that user first.

**Applies to:** Apps with third-party single sign-on
**Requires:** third-party-login

- **[LABEL-79]** If a third-party SSO SDK subjects users to tracking, is ATT permission obtained before that SSO tracking occurs?
  - quote: "If the user will be subject to tracking as a result of SSO functionality included in your app, you must use the App Tracking Transparency prompt to obtain permission from that user first."
  - surface: code
  - verify: grep for `FBSDKLoginKit`/`LoginManager`, `GoogleSignIn`, `TwitterKit`, `LineSDK`, etc.; read each SSO SDK's `PrivacyInfo.xcprivacy` `NSPrivacyTracking`; confirm ATT request precedes SSO SDK initialization where tracking is declared.
  - fix: Request ATT before initializing the tracking-capable SSO SDK, or use a non-tracking login mode/provider.

## LABEL.V10 FAQ — What is a data broker

**Source text (verbatim):**
> What kind of company constitutes a data broker?
>
> Data brokers are defined by law in some jurisdictions. In general, a data broker is a company that regularly collects and sells, licenses, or otherwise discloses to third parties the personal information of particular end-users with whom the business does not have a direct relationship.

**Applies to:** Apps that share data with other companies

- **[LABEL-80]** Has the developer determined whether any company receiving app data is a data broker (regularly collects and sells, licenses, or discloses personal information of end-users it has no direct relationship with)?
  - quote: "a data broker is a company that regularly collects and sells, licenses, or otherwise discloses to third parties the personal information of particular end-users with whom the business does not have a direct relationship."
  - surface: manual
  - verify: Ask the developer to list every company receiving user data (from SDK inventory and backend integrations) and classify each.
  - fix: manual — requires developer decision/legal/business action (sharing with a data broker is tracking: declare it and obtain ATT).

## LABEL.V11 FAQ — Identifiers governed by the tracking policy

**Source text (verbatim):**
> What identifiers or data are governed by the "tracking" policy?
>
> Any user or device level identifier that is used to join data from your app with data from third parties (including SDKs used in your app) for purposes of advertising or ad measurement or sharing with a data broker. This includes, but is not limited to, the device's advertising identifier, session ID, fingerprint IDs, and device graph identifiers. If your app receives or shares any of these identifiers for the above listed purposes, you must use the App Tracking Transparency framework to obtain user consent.

**Applies to:** Apps that receive or share user/device identifiers with third parties

- **[LABEL-81]** If the app receives or shares any user/device-level identifier (advertising identifier, session ID, fingerprint IDs, device graph identifiers) to join data with third parties for advertising, ad measurement, or data brokers, is ATT consent obtained?
  - quote: "If your app receives or shares any of these identifiers for the above listed purposes, you must use the App Tracking Transparency framework to obtain user consent."
  - surface: code
  - verify: Trace identifiers passed to ad/attribution SDKs or partner APIs (`setUserId` on ad SDKs, custom install IDs in attribution postbacks); confirm gating on `.authorized`.
  - fix: Gate identifier sharing on ATT authorization.

## LABEL.V12 FAQ — Tracking inside web views

**Source text (verbatim):**
> If tracking occurs within a webview inside an app, do I need to use the App Tracking Transparency prompt?
>
> Yes. If you are using a webview for app functionality, it should be treated the same way as native functionality in your app, unless you are enabling the user to navigate the open web.

**Applies to:** Apps with web views used for app functionality
**Requires:** webview

- **[LABEL-82]** Is tracking inside app-functionality web views (ad pixels, third-party trackers on the developer's pages) subject to ATT permission like native code?
  - quote: "If you are using a webview for app functionality, it should be treated the same way as native functionality in your app, unless you are enabling the user to navigate the open web."
  - surface: runtime
  - verify: Load each in-app web view (`WKWebView` URLs found in code) with ATT denied; inspect network (Safari Web Inspector) for ad pixels/trackers (e.g., Meta Pixel, Google Ads tags). In code, check whether ATT status is passed to the web content.
  - fix: Suppress trackers in web views unless ATT is authorized, or obtain ATT first.

## LABEL.V13 FAQ — OS versions requiring ATT for IDFA

**Source text (verbatim):**
> What OS versions require App Tracking Transparency permission to access the value of the IDFA?
>
> To access the value of the IDFA for users on iOS/iPadOS version 14.5 or later, you will first need to receive permission from the user through the App Tracking Transparency prompt. For additional guidance on tracking, please refer to App Review Guidelines: 5.1.1 (iv).

**Applies to:** Apps that read the IDFA
**Requires:** tracking, ads, analytics

- **[LABEL-83]** Is the IDFA read only after ATT permission is granted on iOS/iPadOS 14.5 or later?
  - quote: "To access the value of the IDFA for users on iOS/iPadOS version 14.5 or later, you will first need to receive permission from the user through the App Tracking Transparency prompt."
  - surface: code
  - verify: Locate every `ASIdentifierManager.shared().advertisingIdentifier` read; confirm it occurs only after `trackingAuthorizationStatus == .authorized`.
  - fix: Move IDFA reads behind the ATT authorization check.

## LABEL.V14 FAQ — Separate privacy controls alongside ATT

**Source text (verbatim):**
> Can I offer a control in my app, separate from ATT, to comply with local privacy laws?
>
> Yes. You can offer separate privacy controls in your app. You can also provide a shortcut to Settings to enable the user to change their preference for your app with regard to the App Tracking Transparency permissions. When offering a separate control to comply with local privacy laws, please consider the following:
> - Don't confuse the user. Be clear that the control doesn't override their previous ATT choice.
> - Provide context. If possible, show the user's ATT status as part of a separate control so they can understand the choices they've already made.
> - Be clear about what the choice is. If the user has not granted ATT permission, and there is no additional data use beyond the scope of ATT, be clear that no further action is required. If the user has granted ATT permission, it should be clear what impact the separate control will have on their ATT choice.

**Applies to:** Apps offering privacy controls separate from ATT
**Requires:** tracking, ads, analytics

- **[LABEL-84]** If the app has a separate privacy control (e.g., CMP/consent screen), is it clear that the control doesn't override the user's previous ATT choice (one of the points Apple asks developers to "please consider")?
  - quote: "Be clear that the control doesn't override their previous ATT choice."
  - surface: runtime
  - verify: Open the in-app privacy/consent screen; read its copy; in code, confirm the control's toggles never enable tracking when `trackingAuthorizationStatus != .authorized`.
  - fix: Revise copy and logic so ATT remains authoritative; optionally show ATT status in the control.
- **[LABEL-105]** Does the separate privacy control make clear what the choice is: if ATT permission was not granted and there is no data use beyond ATT's scope, that no further action is required; if it was granted, what impact the control has on the ATT choice (Apple's "please consider" guidance)?
  - quote: "If the user has not granted ATT permission, and there is no additional data use beyond the scope of ATT, be clear that no further action is required. If the user has granted ATT permission, it should be clear what impact the separate control will have on their ATT choice."
  - surface: runtime
  - verify: Open the separate privacy control with ATT denied and again with ATT authorized; read the copy shown in each state.
  - fix: Add state-dependent copy explaining whether action is needed and how the control relates to the ATT choice.

## LABEL.V15 FAQ — Other permission requests for legal compliance

**Source text (verbatim):**
> Can I add other permission requests in order to comply with legal obligations or regulations?
>
> Yes, you can choose to include screens in order to comply with applicable law or government regulations. However, your app must always respect the user’s response to the App Tracking Transparency prompt, even if their response to other prompts conflicts. Guideline 5.1.1 (iv) states: "Apps must respect the user's permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access." This includes altering a user’s App Tracking Transparency response by only respecting their response to other permission requests. You can use third-party Consent Management Platforms to add these permission requests, as long as your collection and use of device or user data collected from your app does not contradict a user’s App Tracking Transparency response. You remain fully responsible to ensure that your collection and use of information linked to users’ identity or to their device, including information used to track users, complies with applicable law or government regulations.

**Applies to:** Apps using consent screens or Consent Management Platforms alongside ATT
**Requires:** tracking, ads, analytics

- **[LABEL-85]** When the ATT answer conflicts with a CMP/consent answer, does the app always respect the ATT answer (e.g., ATT denied + CMP accepted → no tracking)?
  - quote: "your app must always respect the user’s response to the App Tracking Transparency prompt, even if their response to other prompts conflicts."
  - surface: code
  - verify: grep CMP SDKs (Google UMP `UMPConsentInformation`, OneTrust, Didomi, Usercentrics, Sourcepoint) and check that ad/tracking SDK enablement requires BOTH CMP consent AND `.authorized`; test ATT denied + CMP accept at runtime with a proxy.
  - fix: Make ATT `.authorized` a mandatory condition for tracking regardless of CMP result.

## LABEL.V16 FAQ — Referencing legal consent in the ATT purpose string

**Source text (verbatim):**
> Can I reference consent requests to comply with local privacy laws in my app’s App Tracking Transparency system prompt?
>
> Yes. If you have already prompted the user with a prompt to comply with government regulations for data practices covered by App Tracking Transparency, e.g. using a third-party Consent Management Platform, and the user consented, you have the option to reference that previous legal consent in your app's App Tracking Transparency system prompt purpose string. When doing so, please consider the following:
> - Don’t confuse the user. Be clear about how the impact of the user’s respective choices.
> - Be consistent. You should not display the ATT prompt to users who have opted out of all relevant legal consent choices made in the previous, separate control.
> - You remain fully responsible to ensure that your implementation of consent requests in combination with the ATT prompt complies with applicable privacy laws.

**Applies to:** Apps whose ATT purpose string references a prior legal consent
**Requires:** tracking, ads, analytics

- **[LABEL-86]** If the ATT purpose string references a prior legal consent, does the app skip the ATT prompt for users who opted out of all relevant legal consent choices?
  - quote: "You should not display the ATT prompt to users who have opted out of all relevant legal consent choices made in the previous, separate control."
  - surface: code
  - verify: Inspect the flow between the CMP callback and `requestTrackingAuthorization`; confirm the call is skipped when the CMP result is "reject all".
  - fix: Skip the ATT request when the user rejected all relevant legal consents.

## LABEL.V17 FAQ — Additional Information button and layered consent (EU)

**Source text (verbatim):**
> Can I provide additional information and consent controls with my app’s ATT prompt implementation, to comply with local privacy laws in the European Union, such as ePrivacy or GDPR?
>
> Yes. In the European Union, you have the option to use the “Additional Information” text button in the ATT prompt to surface additional information and more granular consent controls to comply with local privacy laws or other applicable legal requirements for the collection and use of device or user data collected from your app that are described in your app’s App Tracking Transparency system prompt. Any additional information related to your request or more granular consent controls provided via the text button are entirely your responsibility. However, you cannot access the device’s advertising identifier, or otherwise collect and use device or user data from your app as described in the App Tracking Transparency system prompt, until the user has granted your app permission in that prompt. When implementing this “layered” approach to comply with local privacy laws, please consider the following:
> - Provide context. The purpose string in the App Tracking Transparency system prompt should contain the most important information about your intended collection and use of the advertising identifier or other relevant device or user data collected from your app, in line with local privacy laws and regulatory guidelines. You can also include information in the purpose string in the App Tracking Transparency system prompt to explain to your user what additional information and granular consent controls they can obtain by tapping on the “Additional Information” text button.
> - Be consistent. After a user taps on “Additional Information” and accesses the relevant screen in your app or page in your website, you can redirect the user back to the App Tracking Transparency system prompt for your app to ensure their choice is recorded in the App Tracking Transparency framework. However you should not redirect users to your ATT prompt if they have opted out of all relevant legal consent choices in the screen or page surfaced.
> - Assess the clearest and most suitable option for your app. The ability to link to additional information and more granular consent controls within the App Tracking Transparency prompt for your app is entirely optional. In addition, you remain free to add other permission requests and separate controls for your app independently from App Tracking Transparency (see Questions above).
> - You remain fully responsible to ensure that your implementation of the App Tracking Transparency system prompt and any corresponding information surfaced via the “Additional Information” text button complies with applicable privacy laws.

**Applies to:** Apps using the EU "Additional Information" button
**Requires:** tracking, ads, analytics

- **[LABEL-87]** When the Additional Information screen is shown, does the app avoid accessing the IDFA or collecting tracking data until the user grants permission in the ATT prompt?
  - quote: "you cannot access the device’s advertising identifier, or otherwise collect and use device or user data from your app as described in the App Tracking Transparency system prompt, until the user has granted your app permission in that prompt."
  - surface: code
  - verify: Inspect the `additionalInformationAction` closure and the screen it presents; confirm no IDFA read or tracking SDK enablement happens there based on in-screen consent alone.
  - fix: Defer IDFA/tracking until the ATT completion returns `.authorized`.
- **[LABEL-88]** After the Additional Information screen, does the app avoid redirecting users back to the ATT prompt if they opted out of all relevant legal consent choices there?
  - quote: "However you should not redirect users to your ATT prompt if they have opted out of all relevant legal consent choices in the screen or page surfaced."
  - surface: code
  - verify: Inspect the code path after the Additional Information screen closes; confirm `requestTrackingAuthorization` is re-called only if the user did not reject all.
  - fix: Skip the re-request when all consents were rejected.
- **[LABEL-106]** When using the Additional Information button, does the ATT purpose string contain the most important information about the intended collection and use of the advertising identifier or other relevant data (Apple's "should" guidance)?
  - quote: "The purpose string in the App Tracking Transparency system prompt should contain the most important information about your intended collection and use of the advertising identifier or other relevant device or user data collected from your app, in line with local privacy laws and regulatory guidelines."
  - surface: code
  - verify: Read `NSUserTrackingUsageDescription` and `NSUserTrackingMarkdownUsageDescription` (and EU localizations); confirm the key facts about the tracking use are in the string itself, not only behind the Additional Information screen.
  - fix: Move the key facts into the purpose string; keep detail in the Additional Information screen.

## LABEL.W App Privacy Report and attributing app installations

**Source text (verbatim):**
> With iOS and iPadOS, users can turn on App Privacy Report to see details about how often apps access their data — like location, camera, microphone, and more. They can see information about each app’s network activity and website network activity, as well as the web domains that all apps contact most frequently.
>
> Advertisers can use AdAttributionKit — Apple’s privacy-preserving, industry-leading technology — to attribute in-app ad campaigns and web ads on mobile, while maintaining user privacy.

**Applies to:** All apps (informational)

**Status:** Informational — no requirements stated; no checks.

---

## LABEL.X App Tracking Transparency framework (overview)

**Source text (verbatim):**
> Request authorization to access app-related data that your app can use to track the person or the device.
>
> Your app needs to use the App Tracking Transparency framework if it collects data about people and shares it with other companies to track them across apps and websites. The framework presents a tracking-authorization UI and reports the current authorization status.
>
> To use the App Tracking Transparency framework:
> - Add the NSUserTrackingUsageDescription key to your app’s target properties in Xcode.
> - Call requestTrackingAuthorization(completionHandler:) to present the tracking-authorization request.
> - Check trackingAuthorizationStatus to determine the current authorization status; see ATTrackingManager.AuthorizationStatus for the possible values.

**Applies to:** Apps that collect data about people and share it with other companies to track them across apps and websites
**Requires:** tracking, ads, analytics

- **[LABEL-89]** If the app links `AppTrackingTransparency`, is `NSUserTrackingUsageDescription` present in the app target's properties?
  - quote: "Add the NSUserTrackingUsageDescription key to your app’s target properties in Xcode."
  - surface: code
  - verify: grep sources for `AppTrackingTransparency` / `ATTrackingManager`; then check the built Info.plist (`plutil -p <App>.app/Info.plist | grep NSUserTrackingUsageDescription`) or the target's `INFOPLIST_KEY_NSUserTrackingUsageDescription` build setting.
  - fix: Add `NSUserTrackingUsageDescription` (Privacy - Tracking Usage Description) with a specific purpose string.
- **[LABEL-90]** Does the app check `trackingAuthorizationStatus` to determine the current status before tracking?
  - quote: "Check trackingAuthorizationStatus to determine the current authorization status"
  - surface: code
  - verify: grep `trackingAuthorizationStatus`; confirm tracking code paths branch on it.
  - fix: Read `ATTrackingManager.trackingAuthorizationStatus` and gate tracking on `.authorized`.

---

## LABEL.Y requestTrackingAuthorization(completionHandler:)

**Source text (verbatim):**
> Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.
>
> This method requests authorization to access app-related data that the app can use to track the person or the device. In France, Germany, Italy, Poland, and Romania, the system presents a full-page sheet; otherwise, the system prompts the person with an alert.
>
> Handle the person’s response
>
> When the person answers the prompt, the system calls the completion handler with a status object (ATTrackingManager.AuthorizationStatus) set to ATTrackingManager.AuthorizationStatus.authorized or ATTrackingManager.AuthorizationStatus.denied, depending on the person’s response.
>
> The status is ATTrackingManager.AuthorizationStatus.notDetermined if the system dismisses the prompt without a decision from the person; in this scenario, your app needs to call the method again to receive an authorization answer from the person.
>
> In some cases, the system doesn’t display the prompt and instead runs your completion handler immediately. The system doesn’t prompt the person when:
> - Tracking is restricted for the device; in this case, the trackingAuthorizationStatus is ATTrackingManager.AuthorizationStatus.restricted regardless of whether the system has shown the person the prompt.
> - The person disables “Allow Apps to Request to Track” (called “Allow Apps to Request to Link Your Activity Across Companies” in the European Union) in Settings > Privacy & Security > Tracking.
> - An existing permission request is pending.
> - Your code invokes this method through an app extension.
> - The app’s state is a value other than `UIApplicationStateActive`.
>
> Prompt again after a year
>
> In the European Union, if a person answers the prompt, the system notes the date and doesn’t allow the prompt to display again until a year passes. You can make an additional request after a year whether the person approves or denies your app’s previous tracking request, unless the person disables tracking in Settings > Privacy & Security > Tracking.
>
> Configure the app’s target properties
>
> To use this method, add the NSUserTrackingUsageDescription key to your app’s target properties in Xcode.
>
> In France, Germany, Italy, Poland, and Romania, the full-page sheet displays the NSUserTrackingMarkdownUsageDescription string with support for rich-text elements if you include it in your app’s target configuration in Xcode.

**Applies to:** Apps that call requestTrackingAuthorization
**Requires:** tracking, ads, analytics

- **[LABEL-91]** Is `requestTrackingAuthorization` called while the app is active (not from `didFinishLaunching` before the app becomes active, nor from an app extension), so the prompt actually appears?
  - quote: "The app’s state is a value other than `UIApplicationStateActive`."
  - surface: code
  - verify: Find the call site. Fail if called in `application(_:didFinishLaunchingWithOptions:)`, `init` of the `App` struct, or any extension target. Pass if triggered after `applicationDidBecomeActive` / `scenePhase == .active` / `.onAppear` of a visible view or a user action. Also grep extension targets for `ATTrackingManager`.
  - fix: Move the call to run when the app is active (e.g., on `scenePhase` change to `.active` or from a visible screen).
- **[LABEL-92]** Does the app handle a `.notDetermined` result (prompt dismissed without a decision) by calling the method again later?
  - quote: "your app needs to call the method again to receive an authorization answer from the person."
  - surface: code
  - verify: Inspect the completion handler/async result; confirm `.notDetermined` is not treated as final (e.g., re-request on next activation).
  - fix: Re-request when the status is still `.notDetermined`.
- **[LABEL-93]** Does the ATT request actually present the modal UI on a fresh install (verified at runtime)?
  - quote: "Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device."
  - surface: runtime
  - verify: Erase the simulator/device app, install, launch, reach the point where ATT is requested; confirm the system prompt appears with the purpose string. Check Settings > Privacy & Security > Tracking "Allow Apps to Request to Track" is on in the test device.
  - fix: Fix call timing (LABEL-91) and Info.plist key (LABEL-89).

---

## LABEL.Z requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)

**Source text (verbatim):**
> Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.
>
> This method requests authorization to access app-related data that the app can use to track the person or the device. The method augments the regular authorization request flow (see requestTrackingAuthorization(completionHandler:)) by adding functionality to the modal UI with the option of requesting a full-page sheet, Markdown-formatted text, and an optional Additional Information button.
>
> Display a full-page sheet
>
> The functionality this method adds to the authorization process is available regionally, and requires the device to be located in a specific European Union country and signed in with an Apple Account with a specific EU country or region:
> - France, Germany, Italy, Poland, and Romania: The system displays markdown text you supply via NSUserTrackingMarkdownUsageDescription in a full-page sheet regardless of what you set for `preferExpandedInterface`, and includes an Additional Information button if you supply an action.
> - The European Union: The system displays markdown text in the NSUserTrackingMarkdownUsageDescription, if you supply it. The system displays the full-page sheet if you set `preferExpandedInterface` to `true`, and includes an Additional Information button if you supply an action.
>
> Outside of the European Union, the system doesn’t use either parameter, and presents a system alert displaying the original NSUserTrackingUsageDescription, which is equivalent to calling requestTrackingAuthorization(completionHandler:).
>
> Handle the person’s response
>
> When the person answers the prompt, the system calls the argument completion handler with a status object (ATTrackingManager.AuthorizationStatus) set to ATTrackingManager.AuthorizationStatus.authorized or ATTrackingManager.AuthorizationStatus.denied, depending on the person’s response.
>
> The status is ATTrackingManager.AuthorizationStatus.notDetermined if the system dismisses the prompt without a decision from the person; in this case, your app needs to call this method again to receive an authorization answer from the person.
>
> In some cases, the system doesn’t display the prompt and instead runs your completion handler immediately. The system doesn’t prompt the person when:
> - Tracking is restricted for the device; in this case, the trackingAuthorizationStatus is ATTrackingManager.AuthorizationStatus.restricted regardless of whether the system has shown the person the prompt.
> - The person disables “Allow Apps to Request to Track” (called “Allow Apps to Request to Link Your Activity Across Companies” in the European Union) in Settings > Privacy & Security > Tracking.
> - An existing permission request is pending.
> - Your code invokes this method through an app extension.
> - The app’s state is a value other than `UIApplicationStateActive`.
>
> Provide additional information
>
> If someone taps Additional Information, the sheet dismisses without recording an answer, and your `additionalInformationAction` closure runs. In your closure, present your own custom UI that provides more information to assist people in their decision making. Then call this method again to ask for permission once more.
>
> The completion handler still runs after an Additional Information button tap, receiving ATTrackingManager.AuthorizationStatus.notDetermined, since the person hasn’t yet made a decision.
>
> Prompt again after a year
>
> In the European Union, if a person answers the prompt, the system notes the date and doesn’t allow the prompt to display again until a year passes. You can make an additional request after a year whether the person approves or denies your app’s previous tracking request, unless the person disables tracking in Settings > Privacy & Security > Tracking.
>
> Configure the app’s target properties
>
> To use this method, add the NSUserTrackingUsageDescription key to your app’s target properties in Xcode.
>
> Important: In the European Union, if your app’s target properties in Xcode also include NSUserTrackingMarkdownUsageDescription, the full-page sheet uses that string instead, with support for bold text, italic text, bullet lists, and paragraph breaks.

| Parameter | Description (verbatim) |
|---|---|
| preferExpandedInterface | A Boolean value that requests that the system present a full-page sheet instead of a system alert. |
| additionalInformationAction | An action to perform when someone taps Additional Information; pass `nil` to omit the button. |
| completion | A handler you implement to process the person’s response. |

Availability (from the page metadata): iOS 27.2, iPadOS 27.2, Mac Catalyst 27.2.

**Applies to:** Apps that call the expanded-interface ATT request (iOS/iPadOS 27.2+)
**Requires:** tracking, ads, analytics

- **[LABEL-94]** If the app uses the expanded-interface API, is the call guarded for iOS/iPadOS 27.2 availability with a fallback to `requestTrackingAuthorization(completionHandler:)`?
  - quote: "which is equivalent to calling requestTrackingAuthorization(completionHandler:)."
  - surface: code
  - verify: grep `preferExpandedInterface`; check it is inside `if #available(iOS 27.2, *)` (or the deployment target is ≥ 27.2) with an `else` calling the classic method.
  - fix: Wrap in `#available` and fall back to the classic request.
- **[LABEL-95]** If an `additionalInformationAction` is supplied, does the closure present custom informational UI and then call the method again?
  - quote: "In your closure, present your own custom UI that provides more information to assist people in their decision making. Then call this method again to ask for permission once more."
  - surface: code
  - verify: Inspect the closure body: it should present a view/sheet and, on dismissal, re-invoke the request (subject to LABEL-88).
  - fix: Implement the closure to show the information screen and re-request authorization.
- **[LABEL-96]** Does the completion handler avoid treating the `.notDetermined` result after an Additional Information tap as a final denial or approval?
  - quote: "The completion handler still runs after an Additional Information button tap, receiving ATTrackingManager.AuthorizationStatus.notDetermined, since the person hasn’t yet made a decision."
  - surface: code
  - verify: Inspect the completion handler: `.notDetermined` must not persist a "user declined" flag or enable tracking.
  - fix: Handle `.notDetermined` as undecided.

---

## LABEL.AA trackingAuthorizationStatus and ATTrackingManager.AuthorizationStatus

**Source text (verbatim):**
> A value that indicates the status of the app’s tracking authorization.
>
> Check this property to determine whether your app has permission to access app-related data it can use to track a person or device.
>
> If the status is ATTrackingManager.AuthorizationStatus.notDetermined, call one of the tracking-request methods to present the tracking-authorization prompt and ask the person for permission:
> - requestTrackingAuthorization(completionHandler:)
> - requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)
>
> This property returns ATTrackingManager.AuthorizationStatus.restricted when the system restricts tracking for the device, regardless of whether your app has presented the prompt.
>
> A type that represents the tracking-authorization status of an app.
>
> trackingAuthorizationStatus returns this type, and requestTrackingAuthorization(completionHandler:) passes an instance of this type to your completion handler when a person answers the system alert.

| Value | Description (verbatim) |
|---|---|
| ATTrackingManager.AuthorizationStatus.authorized | A value that indicates someone grants your app permission to access data your app can use to track a person or device. |
| ATTrackingManager.AuthorizationStatus.denied | A value that indicates someone denies your app permission to access data your app can use to track a person or device. |
| ATTrackingManager.AuthorizationStatus.notDetermined | A value that indicates the person hasn’t responded to a tracking authorization request. |
| ATTrackingManager.AuthorizationStatus.restricted | A value that indicates the system restricts tracking authorization. |

**Applies to:** Apps that use App Tracking Transparency
**Requires:** tracking, ads, analytics

- **[LABEL-97]** Does the app treat only `.authorized` as permission to track, and treat `.denied` and `.restricted` as no permission?
  - quote: "A value that indicates someone grants your app permission to access data your app can use to track a person or device."
  - surface: code
  - verify: grep `switch` statements / comparisons on `ATTrackingManager.AuthorizationStatus`; fail on patterns like `!= .denied` that would allow tracking under `.restricted` or `.notDetermined`.
  - fix: Use `== .authorized` as the only tracking-enabled condition.

---

## LABEL.AB NSUserTrackingUsageDescription

**Source text (verbatim):**
> A message that explains the purpose for accessing data that an app can use to track a person or device.
>
> If your application uses the App Tracking Transparency framework, you need to provide a usage-description string to explain the purpose for accessing app-related data that the app can use to track a person or device. The system displays the string in a modal UI from which the person can grant or deny permission to access the tracking data.
>
> This key is required. Your app crashes if it attempts to use the App Tracking Transparency framework without including the key in your target’s properties in Xcode.
>
> The system displays this key’s string in a modal UI when your app requests authorization to access app-related data that the app can use to track the person or the device by calling either method:
> - requestTrackingAuthorization(completionHandler:)
> - requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)
>
> Important: Alternatively, in the European Union, your app can provide a tracking-usage description that supports rich text elements by using markdown format (see NSUserTrackingMarkdownUsageDescription).
>
> Keep the text of your description short and specific. The system displays your app name in the prompt, so you don’t need to include it in the string. For example usage descriptions, see Apple’s Human Interface Guidelines.

| Property | Value (from the page) |
|---|---|
| Key | NSUserTrackingUsageDescription |
| Xcode name | Privacy - Tracking Usage Description |
| Type | String |
| Platforms | iOS 14.0+, iPadOS 14.0+, tvOS 14.0+, visionOS 1.0+ |

**Applies to:** Apps that use the App Tracking Transparency framework
**Requires:** tracking, ads, analytics

- **[LABEL-98]** Is `NSUserTrackingUsageDescription` present whenever the app uses the ATT framework (otherwise it crashes)?
  - quote: "This key is required. Your app crashes if it attempts to use the App Tracking Transparency framework without including the key in your target’s properties in Xcode."
  - surface: code
  - verify: If any target references `ATTrackingManager`, confirm the key in that target's Info.plist or `INFOPLIST_KEY_NSUserTrackingUsageDescription` build setting (check every build configuration, e.g., Debug and Release).
  - fix: Add the key with a specific purpose string to the target.
- **[LABEL-99]** Is the tracking usage description short and specific?
  - quote: "Keep the text of your description short and specific."
  - surface: code
  - verify: Read the string in Info.plist and every localization (`InfoPlist.strings` / `InfoPlist.xcstrings`); fail if empty, a placeholder, or vague.
  - fix: Rewrite to a short, specific explanation of the tracking purpose; localize it.

---

## LABEL.AC NSUserTrackingMarkdownUsageDescription

**Source text (verbatim):**
> A message that explains the purpose for accessing data that an application can use to track a person or device.
>
> If your application uses the App Tracking Transparency framework, use this key to provide a usage-description string to explain your app’s purpose for accessing data that the app can use to track the person or the device. The system displays the string value in a full-page authorization sheet from which the person can grant or deny permission to access the tracking data.
>
> The format of the string is Markdown text; you can apply bold or italic style, but it doesn’t support underline. You can include bullet lists and paragraph breaks.
>
> This key is optional. The system uses the NSUserTrackingUsageDescription if your app’s target properties omit this key.
>
> This key has regional availability. To use this key, the system requires that the device be located in a specific European Union (EU) country and signed in with an Apple Account that has its country or region set to a specific EU country or region:
> - France, Germany, Italy, Poland, and Romania: The system uses this key, if available.
> - The European Union: The system uses this key if available when your app calls requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:), passing `preferExpandedInterface` a value of `true`.
>
> Outside of the EU, the system uses the NSUserTrackingUsageDescription key instead of this key.
>
> Tip: Keep the text of your description short and specific. The system displays your app name in the prompt so you don’t need to include it in the string. For example usage descriptions, see Apple’s Human Interface Guidelines.

| Property | Value (from the page) |
|---|---|
| Key | NSUserTrackingMarkdownUsageDescription |
| Xcode name | Privacy - Tracking Markdown Usage Description |
| Type | String |
| Platforms | iOS 27.2+, iPadOS 27.2+ |

**Applies to:** Apps that provide NSUserTrackingMarkdownUsageDescription (optional)
**Requires:** tracking, ads, analytics

- **[LABEL-100]** If `NSUserTrackingMarkdownUsageDescription` is provided, does it use only supported Markdown (bold, italic, bullet lists, paragraph breaks — no underline)?
  - quote: "The format of the string is Markdown text; you can apply bold or italic style, but it doesn’t support underline. You can include bullet lists and paragraph breaks."
  - surface: code
  - verify: Read the key in Info.plist and localizations; flag HTML tags, `<u>`, links, headings, or images.
  - fix: Limit the string to bold, italic, bullet lists, and paragraph breaks.

---

## LABEL.AD advertisingIdentifier (AdSupport)

**Source text (verbatim):**
> The UUID that is specific to a device.
>
> The advertisingIdentifier is an alphanumeric string that’s unique to each device, and which you only use for advertising. Use this string for frequency capping, attribution, conversion events, estimating the number of unique users, advertising fraud detection, and debugging. On devices running iOS 14.5 and later and iPadOS 14.5 and later, your app must request tracking authorization before it can get the advertising identifier. For more information on getting the advertising identifier, see AdSupport.
>
> The advertising identifier returns either a unique UUID, or all zeros. It returns a unique UUID in the following cases:
> - If Settings > Privacy > Tracking > Allow Apps to Request to Track is On, you’ve requested tracking authorization from the user by calling the App Tracking Transparency APIs, and received authorization, indicated by ATTrackingManager.AuthorizationStatus.authorized.
> - If the user changes Settings > Privacy > Tracking > Allow Apps to Request to Track to Off after authorizing your app, and leaves the permissions On for your app.
>
> The advertising identifier returns all zeros (`00000000-0000-0000-0000-000000000000`) in the following cases:
> - In Simulator, regardless of any settings.
> - When you call this API on a device running macOS.
> - When you call this API in a compatible iPad or iPhone app running in visionOS.
> - On devices running iOS 14.5 and later and iPadOS 14.5 and later, if you haven’t requested authorization using the App Tracking Transparency framework.
> - If you’ve requested authorization using the App Tracking Transparency framework and the user declines, which results in an authorization status of ATTrackingManager.AuthorizationStatus.denied.
> - When a profile or configuration restricts access to the advertising identifier. For more information about restrictions, see ATTrackingManager.AuthorizationStatus.restricted.
>
> As a best practice, don’t store the advertising identifier value; access advertisingIdentifier instead. Users can change their authorization for tracking at any time in Settings > Privacy > Tracking. Check your app’s authorization using the App Tracking Transparency API doc://com.apple.documentation/documentation/apptrackingtransparency/attrackingmanager/3547038-trackingauthorizationstatus to determine the user’s intent.

**Applies to:** Apps that read the advertising identifier
**Requires:** tracking, ads, analytics

- **[LABEL-101]** Does the app use the advertising identifier only for advertising and request tracking authorization before reading it?
  - quote: "your app must request tracking authorization before it can get the advertising identifier."
  - surface: code
  - verify: grep `advertisingIdentifier`; confirm each read is preceded by an ATT request and gated on `.authorized`, and the value is not used for non-advertising purposes (e.g., as a user account key).
  - fix: Gate reads on ATT; use another identifier for non-advertising needs.
- **[LABEL-102]** Does the app follow Apple's stated best practice of not storing the advertising identifier value (reading `advertisingIdentifier` instead)?
  - quote: "As a best practice, don’t store the advertising identifier value; access advertisingIdentifier instead."
  - surface: code
  - verify: grep for the IDFA being written to `UserDefaults`, Keychain, Core Data/SwiftData, or files.
  - fix: Remove persistence; read `advertisingIdentifier` when needed after checking ATT status.
- **[LABEL-103]** Does the app handle an all-zeros IDFA (e.g., denied, restricted, Simulator) without treating it as a real identifier?
  - quote: "The advertising identifier returns all zeros (`00000000-0000-0000-0000-000000000000`) in the following cases"
  - surface: code
  - verify: grep for comparisons against the zero UUID or checks of ATT status before sending the IDFA; fail if the zero UUID is sent as a user key.
  - fix: Skip IDFA-dependent logic when not authorized or when the value is all zeros.

---

## LABEL.X2 ATTrackingManager (class overview)

**Source text (verbatim):**
> A class that requests tracking authorization and provides the current authorization status.
>
> This class presents an authorization request UI that asks a person for permission to access app-related data that your app can use to track a person or device across apps and websites (see requestTrackingAuthorization(completionHandler:)). You can check the result of prior requests with the trackingAuthorizationStatus property.
>
> Important: In the European Union, you can use requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:) to add an optional Additional Information button to the prompt, which provides more details to assist people in their decision-making. The authorization Ul is a full-page sheet that supports rich-text formatting.

**Applies to:** Apps that use App Tracking Transparency
**Requires:** tracking, ads, analytics

**Status:** Informational — the requirements on this page are restated on the method and property pages; see LABEL.Y, LABEL.Z, and LABEL.AA (checks LABEL-90 to LABEL-97). No additional checks.

---

## LABEL.AE identifierForVendor (UIKit)

**Source text (verbatim):**
> An alphanumeric string that uniquely identifies a device to the app’s vendor.
>
> The value of this property is the same for apps that come from the same vendor running on the same device. A different value is returned for apps on the same device that come from different vendors, and for apps on different devices regardless of vendor.
>
> Normally, the vendor is determined by data provided by the App Store. If the app wasn’t installed from the app store (such as enterprise apps and apps still in development), then a vendor identifier is calculated based on the app’s bundle ID. The bundle ID is assumed to be in reverse-DNS format.
>
> If the value is `nil`, wait and get the value again later. This happens, for example, after the device has been restarted but before the user has unlocked the device.
>
> The value in this property remains the same while the app (or another app from the same vendor) is installed on the iOS device. The value changes when the user deletes all of that vendor’s apps from the device and subsequently reinstalls one or more of them. The value can also change when installing test builds using Xcode or when installing an app on a device using ad-hoc distribution. Therefore, if your app stores the value of this property anywhere, you should gracefully handle situations where the identifier changes.

**Applies to:** Apps that read `UIDevice.identifierForVendor` (privacy use of IDFV is covered by LABEL-68 and LABEL-24)

- **[LABEL-107]** Does the app handle a `nil` `identifierForVendor` by getting the value again later rather than force-unwrapping it or treating `nil` as an identifier?
  - quote: "If the value is `nil`, wait and get the value again later."
  - surface: code
  - verify: grep `identifierForVendor`; fail on force unwraps (`identifierForVendor!`) or code that sends/stores a placeholder when it is `nil`.
  - fix: Unwrap optionally and retry later (e.g., on next activation) when the value is `nil`.
- **[LABEL-108]** If the app stores the IDFV anywhere, does it gracefully handle the identifier changing (Apple says "should")?
  - quote: "Therefore, if your app stores the value of this property anywhere, you should gracefully handle situations where the identifier changes."
  - surface: code
  - verify: grep for IDFV values written to `UserDefaults`, Keychain, files, or a server; check that a changed value does not break login, entitlements, or data lookup keyed on it.
  - fix: Do not key critical state solely on the stored IDFV; handle a mismatch between the stored and current value.

---

## LABEL.AF openSettingsURLString (UIKit)

**Source text (verbatim):**
> The URL string you use to deep link to your app’s custom settings in the Settings app.
>
> Create a URL from this value and pass it to the open(_:options:completionHandler:) method to launch the Settings app and display your app’s custom settings, if it has any.

**Applies to:** Apps that provide a shortcut to Settings (e.g., for the tracking permission, LABEL-67)

**Status:** Informational — API usage for the Settings shortcut described in LABEL.T; it is applied in the LABEL-67 fix. No additional checks.

---

## Sources
- https://developer.apple.com/app-store/app-privacy-details/ — "App Privacy Details - App Store - Apple Developer" (page heading: "App privacy details on the App Store")
- https://developer.apple.com/app-store/user-privacy-and-data-use/ — "User Privacy and Data Use - App Store - Apple Developer" (page heading: "User privacy and data use")
- https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy — "Manage app privacy - Manage app information - App Store Connect - Help - Apple Developer"
- https://developer.apple.com/documentation/apptrackingtransparency — "App Tracking Transparency | Apple Developer Documentation" (content read via https://developer.apple.com/tutorials/data/documentation/apptrackingtransparency.json)
- https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager — "ATTrackingManager" (LABEL.X2)
- https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:) — "requestTrackingAuthorization(completionHandler:)"
- https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(preferexpandedinterface:additionalinformationaction:completionhandler:) — "requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)"
- https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/trackingauthorizationstatus — "trackingAuthorizationStatus"
- https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus — "ATTrackingManager.AuthorizationStatus"
- https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingusagedescription — "NSUserTrackingUsageDescription"
- https://developer.apple.com/documentation/bundleresources/information-property-list/nsusertrackingmarkdownusagedescription — "NSUserTrackingMarkdownUsageDescription"
- https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier — "advertisingIdentifier"
- https://developer.apple.com/documentation/uikit/uidevice/identifierforvendor — "identifierForVendor" (LABEL.AE; LABEL-68)
- https://developer.apple.com/documentation/uikit/uiapplication/opensettingsurlstring — "openSettingsURLString" (LABEL.AF; supports LABEL-67 fix)
