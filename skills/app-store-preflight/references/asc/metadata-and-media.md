# App Store Connect — Product Page Metadata, Screenshots, App Previews, Localization, and App Review Information
Source: https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information ; https://developer.apple.com/help/app-store-connect/reference/app-information/app-information ; https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications ; https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications ; https://developer.apple.com/app-store/product-page/ (plus the child pages listed under "## Sources")  
Retrieved: 2026-10-30

Note: (1) The start URLs `.../reference/screenshot-specifications` and `.../reference/app-preview-specifications` redirect to `.../reference/app-information/screenshot-specifications` and `.../reference/app-information/app-preview-specifications`; the redirected pages were used. (2) Apple's pages disagree on the Keywords unit: the App Store Connect Help page says "100 bytes", the "Creating your product page" marketing page says "100 characters". Both are quoted below; checks use the stricter byte limit. (3) "Navigation path" lines quote Apple's own step text so a browser agent can find each field. (4) In the "Required, localizable, and editable properties" tables, "✓" stands for Apple's check-mark icon (not text on the page); digits are Apple's footnote markers. (5) The screenshot and app preview specification lists are reproduced in Apple's stacked order (display name in bold, then its devices, sizes, Requirement and Note entries); the Audio entries of the video specifications are listed per format. (6) Checks marked "report as advisory" quote Apple advice ("avoid", "should", "consider"); they are not stated as hard requirements.

## META.NAV Where the fields live in App Store Connect

**Source text (verbatim):**
> After you add an app to your account, you can view and edit the app information and platform version information in the Apps section.
>
> Some information is required before you upload a build or submit your app for review. You can edit some properties anytime, while others only when the app status is editable. Furthermore, you can localize your app information that appears on the App Store and when users install your app.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> - In Apps, select the app you want to view. The page opens with the Distribution tab selected.
> - Tip: If you have multiple apps, you can use the toolbar controls to find an app.
> - In the sidebar, select the app version under the platform you wish to edit.
> - You can localize the information that appears under Version Information. The information in the App Information section under General is shared across localizations. To learn more about a property, click the question mark next to the field, or go to Platform version information.
> - To update information shared across platforms, click App Information under General in the sidebar. To learn more about a property, click the question mark next to the field, or refer to App information.
> - Click Save.
>
> FAQs
>
> I updated my app information. Why isn’t it displaying in some App Store countries or regions?
>
> After updating your app information, it may take up to 24 hours for the changes to appear on the App Store or when users install your app.
>
> How is my app searchable on the App Store?
>
> Your app is searchable on the App Store by app name, app subtitle, keywords, and your company name. Learn more about discovery on the App Store.

Navigation map derived from the quoted Apple steps (for the browser agent):

| Page in ASC | How Apple says to reach it | Fields audited in this file |
|---|---|---|
| App Information (shared across platforms) | "click App Information under General in the sidebar" | Name, Subtitle, Privacy Policy URL (localized); Bundle ID, SKU, Apple ID, Content Rights, Age Rating, Made for Kids, License Agreement, Primary Language, Category/Subcategory, Korea/China mainland/Vietnam availability, URL for App Store Server Notifications, DSA, Regulated Medical Devices |
| Platform version page | "In the sidebar, select the app version under the platform you wish to edit." | Screenshots, App Previews, Promotional Text, Description, Keywords, Support URL, Marketing URL, Version Number, Copyright, Routing App Coverage File, Version Release, What’s New, Phased Release, Reset Overview Rating, App Review Information, Build |
| Screenshots / previews on version page | "Under the Product Page Information section, click the App Previews and Screenshots tab." / "select View All Sizes in Media Manager on the right." | Screenshots, App Previews, poster frames |
| Language switcher | "On the top right, click the primary language to display the language pop-up menu." | Per-localization metadata |
| Asset Library | "In the sidebar, click Asset Library." | Uploaded previews, screenshots, creative assets |
| App Review section | "Alternatively, you can go to the App Review section in the sidebar." | Draft submissions, App Review messages |

**Applies to:** All apps

- **[META-01]** Has every property that App Store Connect marks as required been completed before the build upload / review submission?
  - quote: "Some information is required before you upload a build or submit your app for review."
  - surface: asc
  - verify: Open Apps > (app) > App Information and each platform version page in the sidebar; for every localization in the language pop-up, confirm no field shows a missing-information warning. Cross-check against the required columns in META.RLE.
  - fix: Fill every missing required field (see the per-field checks below), then click Save.
- **[META-02]** Does the auditing account have a role that can view and edit app information (Account Holder, Admin, App Manager, or Marketing)?
  - quote: "Required role: Account Holder, Admin, App Manager, or Marketing."
  - surface: asc
  - verify: In App Store Connect, open Users and Access (or the profile) and confirm the signed-in user's role is one of the listed roles.
  - fix: manual — requires developer decision/legal/business action (Account Holder/Admin must grant the role).

## META.AI.NAME App Information — Name

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Name | The localized name of your app as it appears on App Store product pages and when users install your app. The name must be at least two characters and no more than 30 characters. You can edit it until you submit the app to App Review. Later, you can change the name when you create a new version or the status of the app version permits editing this property. |
>
> (Add a new app — FAQ) What can I do if the app name I want to use on the App Store is unavailable?
>
> You can use an app name for one app per localization.
>
> If an app in your account already uses the app name, you have two options: submit an update to the existing app to change its name, or remove the app from App Store Connect to allow the name to be used in a new app record.
>
> If another developer is using the app name and you have trademark rights to it, you can submit a claim.
>
> (Creating your product page — App name) Your app’s name plays a critical role in how users discover it on the App Store. Choose a simple, memorable name that is easy to spell and hints at what your app does. Be distinctive. Avoid names that use generic terms or are too similar to existing app names. An app name can be up to 30 characters long.

**Applies to:** All apps (each localization)

Navigation path: App Information (sidebar, under General) > Name, per language in the top-right language pop-up.

- **[META-03]** Is the Name, in every localization, between 2 and 30 characters long?
  - quote: "The name must be at least two characters and no more than 30 characters."
  - surface: asc
  - verify: For each language in the App Information language pop-up, read the Name field and count characters (Unicode characters, not bytes). Fail if < 2 or > 30.
  - fix: Shorten (or lengthen) the localized Name to 2–30 characters and Save; move extra descriptive words to the Subtitle.
- **[META-04]** Is the chosen name not already used by another app in the same localization?
  - quote: "You can use an app name for one app per localization."
  - surface: asc
  - verify: If App Store Connect reports the name as unavailable when saving, record it. Check the developer's other app records in Apps for the same name in the same localization.
  - fix: Choose a different name, or rename/remove the other app record in your account; if another developer holds the name and you hold trademark rights, submit a claim (manual).
- **[META-05]** Is the name distinctive rather than generic or too similar to existing app names? (Apple guidance worded as advice — report as advisory, not as a hard requirement.)
  - quote: "Avoid names that use generic terms or are too similar to existing app names."
  - surface: manual
  - verify: Search the App Store for the exact name and close variants; flag a name made only of generic terms or one closely matching another app's name.
  - fix: manual — requires developer decision/legal/business action (rename).

## META.AI.SUBTITLE App Information — Subtitle

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Subtitle | A summary of your app that appears under your app's name on your App Store product page. This can’t be longer than 30 characters. |
>
> (Creating your product page — Subtitle) Your app’s subtitle is intended to summarize your app in a concise phrase. Consider using this, rather than your app’s name, to explain the value of your app in greater detail. Avoid generic descriptions such as “world’s best app.” Instead, highlight features or typical uses of your app that resonate with your audience. You can update your subtitle when submitting a new version of your app to help you determine the subtitle that’s most effective for engaging users. A subtitle can be up to 30 characters long and appears below your app’s name throughout the App Store.

**Applies to:** All apps that set a subtitle (each localization)

Navigation path: App Information (sidebar, under General) > Subtitle.

- **[META-06]** Is the Subtitle, in every localization, at most 30 characters?
  - quote: "This can’t be longer than 30 characters."
  - surface: asc
  - verify: For each language, read App Information > Subtitle and count characters. Fail if > 30.
  - fix: Rewrite the subtitle to ≤ 30 characters and Save.
- **[META-07]** Does the Subtitle avoid generic descriptions such as “world’s best app”? (Apple guidance worded as advice — report as advisory, not as a hard requirement.)
  - quote: "Avoid generic descriptions such as “world’s best app.”"
  - surface: asc
  - verify: Read each localized Subtitle; flag superlative/generic phrases not describing a feature or use.
  - fix: Replace with a concise phrase naming a feature or typical use of the app.

## META.AI.PRIVACY App Information — Privacy Policy URL

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Privacy Policy URL | A URL that links to your company’s privacy policy. Required for iOS and macOS apps. If your app has a tvOS platform, the text of your privacy policy in the Apple TV Privacy Policy field is required. |
>
> (Required, localizable, and editable properties — App privacy)
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Privacy Policy URL | ✓ | ✓ | |
> | Privacy Choices URL | | ✓ | |
> | Data Types | ✓ | | ✓ |

**Applies to:** iOS and macOS apps (URL); apps with a tvOS platform (Apple TV Privacy Policy text)

Navigation path: App Information (sidebar). Localize app information: "Enter the app name and privacy policy URL for the language or locale, then on the top right, click Save."

- **[META-08]** For iOS/macOS apps, is a Privacy Policy URL set in every localization, and does it load the company's privacy policy?
  - quote: "A URL that links to your company’s privacy policy. Required for iOS and macOS apps."
  - surface: asc
  - verify: For each language in App Information, read Privacy Policy URL; open it (curl -sIL) and confirm HTTP 200 and that the page is a privacy policy. Also grep the project for an in-app privacy-policy link (e.g. `privacy` in Swift/Info.plist/Settings.bundle) to compare it with the ASC URL.
  - fix: Publish the privacy policy at a stable public URL and enter it for every localization; Save.
- **[META-09]** If the app has a tvOS platform, is the Apple TV Privacy Policy text filled in?
  - quote: "If your app has a tvOS platform, the text of your privacy policy in the Apple TV Privacy Policy field is required."
  - surface: asc
  - verify: If the Xcode project has a tvOS target (SDKROOT = appletvos) or ASC lists a tvOS platform, open App Information and confirm the Apple TV Privacy Policy field is non-empty.
  - fix: Paste the privacy policy text into the Apple TV Privacy Policy field and Save.

## META.AI.BUNDLE App Information — Bundle ID, SKU, Apple ID

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Bundle ID | A unique identifier for your app that is used throughout the system. (A build is uniquely identified by the combination of the bundle ID, version number, and build string.) You can’t change this property after you upload a build. Important: The Bundle ID property must match the bundle ID you set in the Xcode project. |
> | SKU | A unique ID you give to your app for internal tracking that's not visible to customers. The SKU can contain letters, numbers, hyphens, periods, and underscores but not start with a hyphen, period, or underscore. You can’t change the SKU after you add the app to your account. |
> | Apple ID | A unique identifier automatically generated for your app when you add the app to your account. You can view this property in the App information section in App Store Connect. This identifier is also used in the URL for the App Store on desktop computers. You can’t edit this property. |

**Applies to:** All apps

Navigation path: App Information (sidebar, under General).

- **[META-10]** Does the Bundle ID in App Store Connect exactly match the bundle ID set in the Xcode project?
  - quote: "Important: The Bundle ID property must match the bundle ID you set in the Xcode project."
  - surface: code
  - verify: In the project, read `PRODUCT_BUNDLE_IDENTIFIER` for the app target (project.pbxproj / .xcconfig, resolved `CFBundleIdentifier` in Info.plist). In ASC, read App Information > Bundle ID. Compare exactly (case-sensitive).
  - fix: Change `PRODUCT_BUNDLE_IDENTIFIER` in Xcode to the ASC Bundle ID (the ASC value can’t be changed after a build is uploaded).
- **[META-11]** Does the SKU contain only letters, numbers, hyphens, periods, and underscores, and not start with a hyphen, period, or underscore?
  - quote: "The SKU can contain letters, numbers, hyphens, periods, and underscores but not start with a hyphen, period, or underscore."
  - surface: asc
  - verify: Read App Information > SKU; test against regex `^[A-Za-z0-9][A-Za-z0-9._-]*$`.
  - fix: The SKU can’t be changed after the app is added; if invalid at creation, create the app record with a valid SKU (manual).

**Apple ID:** Informational (auto-generated, not editable) — no checks.

## META.AI.CONTENTRIGHTS App Information — Content Rights

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Content Rights | Apps that contain, show, or access third-party content must have all the necessary rights to that content or be otherwise permitted to use it under the laws of each App Store country or region in which they’re available. Learn more about the App Store guidelines. |
>
> (Required, localizable, and editable properties)
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Content Rights | ✓ | | |

**Applies to:** All apps (declaration required); rights obligation applies to apps that contain, show, or access third-party content

Navigation path: App Information (sidebar, under General) > Content Rights.

- **[META-12]** Has the Content Rights declaration been answered in App Information?
  - quote: "The tables below show the app and version properties required for App Store submission. ... Content Rights"
  - surface: asc
  - verify: Open App Information and confirm the Content Rights section shows an answer (not an empty/“Set Up” prompt).
  - fix: Answer the Content Rights question truthfully and Save.
- **[META-13]** If the app contains, shows, or accesses third-party content, does the developer hold the necessary rights (or legal permission) in every country or region where the app is available?
  - quote: "Apps that contain, show, or access third-party content must have all the necessary rights to that content or be otherwise permitted to use it under the laws of each App Store country or region in which they’re available."
  - surface: manual
  - verify: Inventory third-party content in the project (bundled media, fonts, images, data feeds, remote content endpoints in Swift `URL(string:)`/networking code, SDKs that stream content). Ask the developer for licences covering each storefront in Pricing and Availability.
  - fix: manual — requires developer decision/legal/business action (obtain licences or remove the content / limit availability).

## META.AI.AGE App Information — Age Rating and Made for Kids

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Age Rating | The age rating of your app for the purpose of parental controls. Note that the rating is set at the app level in the App information section and is applied across all platforms. Learn more about the age rating values. This property is required. |
> | Made for Kids | An indication that the app appears in the Kids category on the App Store. This property includes an age range set for the app. Once an app marked as Made for Kids is approved by App Review, this selection cannot be changed and all subsequent updates will need to follow the Kids category guidelines. |
>
> (Choosing a category — Apps for kids) If you have an app designed for kids ages 11 and under, select the Made for Kids checkbox in App Store Connect and choose an appropriate age band (5 and under, 6–8, or 9–11). Your app must comply with the App Review Guidelines for Kids apps and will go through review to be approved for the Kids category on the App Store. In addition to the Kids category, your app can be discovered in another primary and secondary category (for example: Games, Entertainment, or Education). For more details, see Building Apps for Kids.

**Applies to:** All apps (Age Rating); apps designed for kids ages 11 and under (Made for Kids)

Navigation path: App Information (sidebar, under General) > Age Rating / Made for Kids.

- **[META-14]** Is the Age Rating set in App Information?
  - quote: "This property is required."
  - surface: asc
  - verify: Open App Information and confirm the Age Rating shows a completed rating (questionnaire answered).
  - fix: Complete the age rating questionnaire truthfully and Save.
- **[META-15]** If the app is designed for kids ages 11 and under, is Made for Kids selected with an age band of 5 and under, 6–8, or 9–11?
  - quote: "If you have an app designed for kids ages 11 and under, select the Made for Kids checkbox in App Store Connect and choose an appropriate age band (5 and under, 6–8, or 9–11)."
  - surface: asc
  - verify: Ask/derive the target audience (app content, onboarding copy). In App Information, check Made for Kids and its age range.
  - fix: Select Made for Kids and the correct age band, and audit the app against the Kids category guidelines (see the guidelines reference, 1.3).
- **[META-16]** If Made for Kids is (or was) selected and approved, does this update still follow the Kids category guidelines?
  - quote: "Once an app marked as Made for Kids is approved by App Review, this selection cannot be changed and all subsequent updates will need to follow the Kids category guidelines."
  - surface: asc
  - verify: If App Information shows Made for Kids on an approved app, run the Kids-category checks (third-party analytics/ads SDKs, parental gates) from the guidelines reference against the current build.
  - fix: Remove non-compliant SDKs/flows from the build; the Made for Kids selection itself can’t be undone.

## META.AI.LICENSE App Information — License Agreement

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | License Agreement | Apple provides a standard EULA (End-User License Agreement) that applies in all regions. You may provide a custom license agreement that supersedes the Apple EULA for one or more regions. |
>
> (Required, localizable, and editable properties)
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | License Agreement | | 1 | ✓ |
>
> 1 Localized text may be included in the Custom License Agreement text box.

**Applies to:** Apps that use a custom license agreement

Navigation path: App Information (sidebar) > License Agreement.

- **[META-17]** If the developer intends a custom EULA (e.g. the app or its in-app text refers to its own terms of use as the licence), is a custom license agreement configured for the intended regions; otherwise is the standard Apple EULA in effect?
  - quote: "You may provide a custom license agreement that supersedes the Apple EULA for one or more regions."
  - surface: asc
  - verify: grep the project for "Terms of Use", "EULA", "License Agreement" links. In App Information > License Agreement, check whether it shows Apple’s standard EULA or a custom agreement and which regions it covers.
  - fix: manual — requires developer decision/legal/business action (choose Apple standard EULA or enter custom licence text for the regions).

## META.AI.LANG App Information — Primary Language

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Primary Language | The default language for the metadata that appears on App Store product pages, and is displayed when users install your app, when you don't provide localized metadata for a given country or region. You can change the primary language at any time. |

**Applies to:** All apps

Navigation path: "In the sidebar, click App Information." > "In the Primary Language pop-up menu, choose the new primary language."

- **[META-18]** Is a Primary Language set, and is its metadata complete (it is shown wherever no localized metadata exists)?
  - quote: "The default language for the metadata that appears on App Store product pages, and is displayed when users install your app, when you don't provide localized metadata for a given country or region."
  - surface: asc
  - verify: In App Information read Primary Language; switch the language pop-up to it and confirm all required fields (Name, Privacy Policy URL, Description, Keywords, Support URL, Screenshots) are filled.
  - fix: Complete the primary-language metadata, or change Primary Language (see META.LOC.PRIMARY for constraints).

## META.AI.CATEGORY App Information — Category (Primary and Secondary) and Subcategory

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Category (Primary and Secondary) | The categories that best describe your app. For macOS apps, you also set the app category in Xcode. The primary category you set in App Store Connect should match the category you set in Xcode. For more information, visit Choosing a Category. |
> | Subcategory | If you select Games or Stickers as the Primary or Secondary Category, you can also select one or two subcategories to help more accurately define your game or stickers app. |
>
> (Required, localizable, and editable properties)
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Primary Category | ✓ | | |
> | Secondary Category | | | |

**Applies to:** All apps (primary category); macOS apps (Xcode category match); Games/Stickers apps (subcategories)

Navigation path: App Information (sidebar, under General) > Category.

- **[META-19]** Is a Primary Category set?
  - quote: "The tables below show the app and version properties required for App Store submission. ... Primary Category"
  - surface: asc
  - verify: Open App Information > Category and confirm Primary is selected.
  - fix: Select the primary category that best describes the app (see META.CAT) and Save.
- **[META-20]** For macOS apps, does the Primary Category in App Store Connect match the app category set in Xcode? (Apple says “should match”.)
  - quote: "The primary category you set in App Store Connect should match the category you set in Xcode."
  - surface: code
  - verify: For a macOS target, read the Xcode app category (General > Identity > App Category, stored as `LSApplicationCategoryType` / `INFOPLIST_KEY_LSApplicationCategoryType`). Compare it with ASC App Information > Primary Category.
  - fix: Change one of them so both name the same category.
- **[META-21]** If Games or Stickers is a primary or secondary category, are at most two subcategories selected?
  - quote: "If you select Games or Stickers as the Primary or Secondary Category, you can also select one or two subcategories to help more accurately define your game or stickers app."
  - surface: asc
  - verify: In App Information > Category, if Games or Stickers is chosen, count subcategories (Apple allows one or two; they are optional).
  - fix: If subcategories are used, select at most two accurate ones and Save.

## META.AI.REGIONAL App Information — Korea, China mainland, Vietnam availability

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Availability in the Republic of Korea - Rating Classification Number | If your app meets one or more of the following characteristics, a Rating Classification Number from the Game Rating and Administration Committee (GRAC) is required in order to offer it on the App Store in the Republic of Korea. |
> - App has been given the KR-19 regional rating by GRAC.
> - Apps in the Casino subcategory with age rating 17+
> - Apps in the Games or Entertainment categories with a Frequent/Intense level of frequency in at least one of the following content descriptions:
>   - Simulated Gambling
>   - Sexual Content or Nudity
>   - Alcohol, Tobacco, or Drug Use or Reference
>   - Realistic Violence
>
> Please note that this field will display if your app is in the Games or Entertainment category with a rating of 17+, but is only required if your app meets the above criteria.
>
> | Availability in China mainland | Chinese law requires additional documentation for some apps to be available on the App Store in China mainland. |
>
> China’s Ministry of Industry and Information Technology (MIIT) requires that some apps possess a valid Internet Content Provider (ICP) Filing Number. The ICP number and metadata on the App Information page should match with the information you have filed with MIIT. This match is required for your Simplified Chinese localization; if not configured, then it should match your primary language. Once the provided ICP Filing Number is verified and saved, it will be displayed on your App Store product page.
>
> In addition, games must secure an approval number and apps with books and magazine content must secure an internet publishing permit from China’s National Press and Publication Administration (NPPA). Apps with religious content must secure an Internet Religious Information Permit from China’s National Religious Affairs Administration (NRAA). Apps with news content must obtain an Internet News Information Permit from the Cyberspace Administration of China (CAC). If you offer or plan to offer any of these on the App Store in China mainland, you must provide the required information along with one or more supporting documents.If applicable, provide the required ICP filing information in the designated section under the “App Information” tab. To help verify your approval number, upload your game’s ISBN Issuing Letter or Approval Reply, and a copy of your latest Business License. Additionally, you can include an authorization agreement from the matching operator. To help verify your publishing permit, upload your internet publishing permit or other relevant permit from the NPPA, a publishing permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation. To help verify your Internet Religious Information Permit, upload your Internet Religious Information Permit, a permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation. To help verify your Internet News Information Permit, upload your Internet News Information Permit, a permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation.
>
> | Availability in Vietnam | Vietnamese regulators require games distributed in Vietnam to be licensed to remain available on the App Store in Vietnam. To learn more about the game license, review the regulations on licensing game publishing in Vietnam. |
>
> (Required, localizable, and editable properties — footnotes) 2 Required for developers who enroll as an organization and distribute apps on the App Store in South Korea. 3 Required for apps that meet certain criteria to be available on the App Store in China mainland. Learn about availability requirements. 4 Can be entered at any time, but will be submitted for review with the next version submission.

**Applies to:** Apps distributed in the Republic of Korea, China mainland, or Vietnam that meet the stated criteria

Navigation path: App Information (sidebar) — “the designated section under the “App Information” tab”.

- **[META-22]** If the app is offered in the Republic of Korea and meets a GRAC criterion (KR-19 rating; Casino subcategory with 17+; Games/Entertainment with Frequent/Intense Simulated Gambling, Sexual Content or Nudity, Alcohol/Tobacco/Drug Use, or Realistic Violence), is a GRAC Rating Classification Number entered?
  - quote: "a Rating Classification Number from the Game Rating and Administration Committee (GRAC) is required in order to offer it on the App Store in the Republic of Korea"
  - surface: asc
  - verify: Check Pricing and Availability for Republic of Korea; check App Information category/subcategory and age rating answers; if a criterion matches, confirm the Rating Classification Number field is filled.
  - fix: manual — requires developer decision/legal/business action (obtain a GRAC number, or remove Korea from availability).
- **[META-23]** If the app is offered in China mainland and requires an ICP Filing Number, does the ICP number and App Information metadata match the MIIT filing (Simplified Chinese localization, else primary language)?
  - quote: "The ICP number and metadata on the App Information page should match with the information you have filed with MIIT."
  - surface: asc
  - verify: Check Pricing and Availability for China mainland; in App Information open the China mainland availability section and compare the ICP number and the Simplified Chinese (or primary-language) name with the developer’s MIIT filing.
  - fix: manual — requires developer decision/legal/business action (file/correct ICP, or align metadata).
- **[META-24]** If the app is a game, offers books/magazine, religious, or news content in China mainland, has the required NPPA/NRAA/CAC information and supporting documents been provided?
  - quote: "If you offer or plan to offer any of these on the App Store in China mainland, you must provide the required information along with one or more supporting documents."
  - surface: manual
  - verify: Determine content type (category, app content). In App Information > China mainland section, confirm the approval number/permit and the uploaded supporting documents.
  - fix: manual — requires developer decision/legal/business action.
- **[META-25]** If the app is a game distributed in Vietnam, is it licensed per Vietnamese regulations?
  - quote: "Vietnamese regulators require games distributed in Vietnam to be licensed to remain available on the App Store in Vietnam."
  - surface: manual
  - verify: Check Pricing and Availability for Vietnam and the Games category; ask the developer for the Vietnam game licence and check the Availability in Vietnam section of App Information.
  - fix: manual — requires developer decision/legal/business action (obtain licence or remove Vietnam).

## META.AI.ASSN App Information — URL for App Store Server Notifications

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | URL for App Store Server Notifications | If your app offers In-App Purchases, you can receive server notifications from the App Store about key events by setting up an optional URL that links to your server. Learn how to enable App Store Server Notifications. |
>
> (Footnote) 5 Only visible for apps that offer In-App Purchases.

**Applies to:** Apps that offer In-App Purchases (optional field)
**Requires:** iap, subscriptions

- **[META-26]** If the server code expects App Store Server Notifications (e.g. an endpoint handling signed notification payloads), is the URL configured in App Information?
  - quote: "you can receive server notifications from the App Store about key events by setting up an optional URL that links to your server"
  - surface: asc
  - verify: grep the app/backend repo for App Store Server Notifications handling (e.g. `signedPayload`, `notificationType`, `responseBodyV2`). If present, confirm the URL in App Information matches the deployed endpoint.
  - fix: Enter the production (and sandbox) notification URL in App Information and Save; optional otherwise.

## META.AI.DSA App Information — Digital Services Act (DSA)

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Digital Services Act (DSA) | You’ll be asked to disclose whether or not you’re a trader under the European Union’s Digital Services Act (DSA) in order to distribute apps in the EU. If you’re a trader, the DSA requires that you provide certain identification information, including your address and contact details, to be displayed on your App Store product pages to consumers in the EU. You also have the option to provide a labels and markings URL. Learn more. |
>
> (Required, localizable, and editable properties)
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Digital Services Act (DSA) Status | ✓ | | ✓ |

**Applies to:** Apps distributed in the EU (status declaration is marked required)

- **[META-27]** Has the DSA trader status been declared, and, if a trader, is the address and contact information provided?
  - quote: "You’ll be asked to disclose whether or not you’re a trader under the European Union’s Digital Services Act (DSA) in order to distribute apps in the EU."
  - surface: asc
  - verify: Open App Information (and Business/Agreements if prompted) and confirm the DSA status is set; if “trader”, confirm the identification information, including address and contact details, is provided.
  - fix: manual — requires developer decision/legal/business action (declare trader status; supply contact details).

## META.AI.MEDICAL App Information — Regulated Medical Devices

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Regulated Medical Devices | Apps that are available in the EU/EEA, UK, or U.S., and have a primary or secondary category of Health & Fitness or Medical, or that have "frequent" Medical or Treatment information listed in the age rating, are required to complete this declaration. |
>
> (Footnotes) 6 Required for apps that meet certain criteria to be available on the App Store in the EU/EEA, UK, or U.S.. Learn about availability requirements. 7 Localized text is only for the Use Statement and Safety Information.

**Applies to:** Apps available in the EU/EEA, UK, or U.S. with Health & Fitness or Medical category, or "frequent" Medical or Treatment information in the age rating

- **[META-28]** If the app is available in the EU/EEA, UK, or U.S. and has a Health & Fitness or Medical category (or "frequent" Medical/Treatment information in the age rating), is the Regulated Medical Devices declaration completed?
  - quote: "are required to complete this declaration"
  - surface: asc
  - verify: Read App Information > Category and Age Rating answers and Pricing and Availability; if criteria match, confirm the Regulated Medical Devices declaration is completed.
  - fix: manual — requires developer decision/legal/business action (complete the declaration truthfully).

## META.PVI.LANG Platform version — Language

**Source text (verbatim):**
> Platform version information refers to the set of properties of an app version specific to each platform the app supports.
>
> | Property | Description |
> |---|---|
> | Language | The language you choose to localize your metadata. This property is editable depending on the app status. |

**Applies to:** All apps

**Status:** Informational — no checks (see META.LOC for localization checks).

## META.PVI.SHOTS Platform version — Screenshots

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Screenshots | Screenshots that show what your app looks like on a device. Learn about the screenshot specifications. This property is required and can be localized. |

**Applies to:** All apps

Navigation path: version page > "Under the Product Page Information section, click the App Previews and Screenshots tab." > device tab.

- **[META-29]** Does the version have screenshots for its primary language (and are localized ones provided where intended)?
  - quote: "This property is required and can be localized."
  - surface: asc
  - verify: On the version page, open the App Previews and Screenshots tab for each language in the pop-up and confirm at least one screenshot exists for each required device size (see META.SS.REQ).
  - fix: Upload screenshots (see META.SS.*).
- **[META-30]** Do the screenshots show what the app looks like on a device (captured app UI, not unrelated artwork)?
  - quote: "Screenshots that show what your app looks like on a device."
  - surface: runtime
  - verify: Download each screenshot and compare with screens of the current build on a simulator/device; flag images that do not depict the app’s UI.
  - fix: Recapture screenshots from the current build.

## META.PVI.PREVIEW Platform version — App Preview

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | App Preview | An app preview is an optional short video demonstrating your app. You may add up to three app previews for each localization, per device size. Learn about the app preview specifications. |

**Applies to:** Apps that add app previews

- **[META-31]** Are there at most three app previews per localization per device size?
  - quote: "You may add up to three app previews for each localization, per device size."
  - surface: asc
  - verify: Version page > App Previews and Screenshots > View All Sizes in Media Manager; for each language and device size count previews.
  - fix: Remove extra previews so each set has ≤ 3.

## META.PVI.PROMO Platform version — Promotional Text

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Promotional Text | Promotional text lets you inform your App Store visitors of any current app features without requiring an updated submission. This text will appear above your description on the App Store for customers with devices running iOS 11 or later. This property can’t be longer than 170 characters. |
>
> (Creating your product page — Promotional text) Your app’s promotional text appears at the top of the description and is up to 170 characters long. You can update promotional text at any time without having to submit a new version of your app. Consider using this to share the latest news about your app, such as limited-time sales or upcoming features.
>
> In addition, keep in mind that promotional text doesn’t affect your app’s search ranking so it should not be used to display keywords.

**Applies to:** Apps that set promotional text (each localization)

Navigation path: version page > Promotional Text.

- **[META-32]** Is the Promotional Text, in every localization, at most 170 characters?
  - quote: "This property can’t be longer than 170 characters."
  - surface: asc
  - verify: Read Promotional Text per language and count characters; fail if > 170.
  - fix: Shorten to ≤ 170 characters and Save (no new submission needed).
- **[META-33]** Is the Promotional Text free of keyword lists? (Apple guidance worded as advice — report as advisory, not as a hard requirement.)
  - quote: "promotional text doesn’t affect your app’s search ranking so it should not be used to display keywords"
  - surface: asc
  - verify: Read Promotional Text; flag comma-separated term lists or repeated keyword strings.
  - fix: Rewrite as a sentence about current features/news.

## META.PVI.DESC Platform version — Description

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Description | A description of the app, detailing the features and functionality. Limited to 4000 characters. The description should be in plain text, with line breaks as needed. HTML format isn't supported. This appears on your app’s product page, when users install your app, and will be used for web engine search results once you release your app. This property is required and can be localized. |
>
> (Creating your product page — Description) Provide an engaging description that highlights the features and functionality of your app. The ideal description is a concise, informative paragraph followed by a short list of main features. Let potential users know what makes your app unique and why they’ll love it. Communicate in the tone of your brand, and use terminology your target audience will appreciate and understand. The first sentence of your description is the most important — this is what users can read without having to tap to read more. Every word counts, so focus on your app’s unique features.
>
> If you choose to mention an accolade, we recommend putting it at the end of your description or as part of your promotional text. Don’t add unnecessary keywords to your description in an attempt to improve search results. Also avoid including specific prices in your app description. Pricing is already shown on the product page, and references within the description may not be accurate in all regions.
>
> You can update your app’s description when you submit a new version of your app. If you want to share important updates more frequently, consider using your promotional text instead.

**Applies to:** All apps (each localization)

Navigation path: version page > Description.

- **[META-34]** Is a Description present in every localization?
  - quote: "This property is required and can be localized."
  - surface: asc
  - verify: For each language in the pop-up, confirm the version’s Description is non-empty (new languages do not copy the description — see META.LOC.ADD).
  - fix: Write a description for each localization and Save.
- **[META-35]** Is each Description at most 4000 characters?
  - quote: "Limited to 4000 characters."
  - surface: asc
  - verify: Count characters of each localized Description; fail if > 4000.
  - fix: Shorten to ≤ 4000 characters.
- **[META-36]** Is the Description plain text with no HTML markup?
  - quote: "The description should be in plain text, with line breaks as needed. HTML format isn't supported."
  - surface: asc
  - verify: Search each Description for HTML tags/entities (regex `<[a-zA-Z/][^>]*>` or `&[a-z]+;`).
  - fix: Remove HTML; use plain line breaks.
- **[META-37]** Does the Description detail the app’s features and functionality?
  - quote: "A description of the app, detailing the features and functionality."
  - surface: runtime
  - verify: List features claimed in the Description; confirm each exists in the current build (grep the code for the feature and exercise it in the simulator).
  - fix: Rewrite the Description so it details the features and functionality the app actually has.
- **[META-38]** Does the Description avoid specific prices? (Apple guidance worded as advice — report as advisory, not as a hard requirement.)
  - quote: "Also avoid including specific prices in your app description."
  - surface: asc
  - verify: Search each Description for currency symbols/codes and numeric prices (e.g. `[$€£¥₪]\s?\d`, `\d+[.,]\d{2}`, `USD|EUR`).
  - fix: Remove prices; pricing is shown on the product page.
- **[META-39]** Does the Description avoid unnecessary keywords added to improve search results?
  - quote: "Don’t add unnecessary keywords to your description in an attempt to improve search results."
  - surface: asc
  - verify: Flag keyword lists, repeated terms, or trailing tag blocks in the Description.
  - fix: Remove keyword blocks; put search terms in the Keywords field.

## META.PVI.KEYWORDS Platform version — Keywords

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Keywords | One or more keywords (each greater than two characters) describing your app. You can provide up to 100 bytes of content. Your app is searchable by app name and company name, so you shouldn't duplicate these values in the keyword list. Names of other apps or companies aren't allowed. This property is required and can be localized. |
>
> (Creating your product page) Keywords help determine where your app displays in search results, so choose them carefully to ensure your app is easily discoverable. Choose keywords based on words you think your audience will use to find an app like yours. Be specific when describing your app’s features and functionality to help the search algorithm surface your app in relevant searches. Consider the trade-off between ranking well for less common terms versus ranking lower for popular terms. Popular, functional terms, such as “jobs” or “social”, may drive a lot of traffic, but are highly competitive in the rankings. Less common terms drive lower traffic, but are less competitive.
>
> Keywords are limited to 100 characters total, with terms separated by commas and no spaces. (Note that you can use spaces to separate words within keyword phrases. For example: Property,House,Real Estate.) Maximize the number of words that fit in this character limit by avoiding the following:
> - Plurals of words that you’ve already included in singular form
> - Names of categories or the word “app”
> - Duplicate words
> - Special characters — such as # or @ — unless they’re part of your brand identity. Special characters don’t carry extra weight when users search for your app.
>
> Improper use of keywords is a common reason for App Store rejections. Do not use the following in your keywords:
> - Unauthorized use of trademarked terms, celebrity names, and other protected words and phrases
> - Terms that are not relevant to the app
> - Competing app names
> - Irrelevant, inappropriate, offensive, or objectionable terms

**Applies to:** All apps (each localization)

Navigation path: version page > Keywords.

- **[META-40]** Are Keywords present in every localization?
  - quote: "This property is required and can be localized."
  - surface: asc
  - verify: For each language, confirm Keywords is non-empty (new languages do not copy keywords — see META.LOC.ADD).
  - fix: Enter localized keywords and Save.
- **[META-41]** Is each localized Keywords field at most 100 bytes (UTF-8)?
  - quote: "You can provide up to 100 bytes of content."
  - surface: asc
  - verify: Copy the Keywords string per language and compute `len(s.encode('utf-8'))`; fail if > 100 (non-Latin scripts such as Hebrew, Arabic, CJK use 2–3 bytes per character).
  - fix: Remove low-value terms until ≤ 100 bytes.
- **[META-42]** Is every keyword longer than two characters?
  - quote: "One or more keywords (each greater than two characters) describing your app."
  - surface: asc
  - verify: Split on commas, trim, and flag any term with ≤ 2 characters.
  - fix: Remove or replace short terms.
- **[META-43]** Are keywords comma-separated with no spaces around the commas?
  - quote: "Keywords are limited to 100 characters total, with terms separated by commas and no spaces."
  - surface: asc
  - verify: Regex-check for `\s,|,\s` in the Keywords string.
  - fix: Remove spaces around commas (spaces inside multi-word phrases are fine).
- **[META-44]** Do the keywords avoid duplicating the app name and company (developer) name?
  - quote: "Your app is searchable by app name and company name, so you shouldn't duplicate these values in the keyword list."
  - surface: asc
  - verify: Tokenize the localized Name and the developer/seller name; flag keyword terms equal to those words.
  - fix: Remove the duplicated terms.
- **[META-45]** Do the keywords contain no names of other apps or companies (competing app names)?
  - quote: "Names of other apps or companies aren't allowed."
  - surface: asc
  - verify: Review each term against known app/company/brand names (search the App Store for each proper-noun term).
  - fix: Remove other apps’/companies’ names.
- **[META-46]** Do the keywords avoid unauthorized trademarked terms, celebrity names, and other protected words?
  - quote: "Unauthorized use of trademarked terms, celebrity names, and other protected words and phrases"
  - surface: manual
  - verify: Flag proper nouns and brand-like terms; ask the developer for authorization where used.
  - fix: Remove unauthorized terms.
- **[META-47]** Are all keywords relevant to the app and free of inappropriate, offensive, or objectionable terms?
  - quote: "Irrelevant, inappropriate, offensive, or objectionable terms"
  - surface: asc
  - verify: Compare each term against the app’s actual features (code/UI); flag unrelated or objectionable terms.
  - fix: Replace with relevant feature terms.
- **[META-48]** Do the keywords avoid wasted space: plurals of included singulars, category names or the word “app”, duplicate words, and special characters such as # or @ (unless part of the brand)? (Apple guidance worded as advice — report as advisory, not as a hard requirement.)
  - quote: "Maximize the number of words that fit in this character limit by avoiding the following:"
  - surface: asc
  - verify: Normalize terms; flag duplicates, singular/plural pairs, the word "app", category names (see META.CAT table), and `#`/`@`.
  - fix: Remove the redundant terms and reuse the space.

## META.PVI.URLS Platform version — Support URL and Marketing URL

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Support URL | The URL of the support website you plan to provide for users, which displays on the App Store for users who have downloaded your app. This URL must lead to actual contact information (legal address, email address, telephone number), as may be required by local law, so that users can reach you regarding app issues, general feedback, and feature enhancement requests. Specify the entire URL, including the protocol (for example, http://support.example.com). If you need to provide a Software Bill of Materials (SBOM), you can include it on your support site. This property is required and can be localized. |
> | Marketing URL | The website where users get more information about the app. Specify the entire URL, including the protocol. This property can be localized. |

**Applies to:** All apps (Support URL); apps that set a Marketing URL

Navigation path: version page > Support URL / Marketing URL.

- **[META-49]** Is a Support URL present in every localization, specified as a full URL including the protocol?
  - quote: "Specify the entire URL, including the protocol (for example, http://support.example.com)."
  - surface: asc
  - verify: For each language read Support URL; confirm it starts with `http://` or `https://`; `curl -sIL` returns HTTP 200.
  - fix: Enter the full URL with protocol and Save.
- **[META-50]** Does the Support URL page lead to actual contact information (legal address, email address, telephone number, as may be required by local law)?
  - quote: "This URL must lead to actual contact information (legal address, email address, telephone number), as may be required by local law"
  - surface: asc
  - verify: Fetch the Support URL page; confirm visible contact information (email and, where required by local law, legal address and phone). Flag pages that are only a marketing landing page, a 404, or a placeholder.
  - fix: Add a support/contact page with email, phone, and legal address as required; update the URL.
- **[META-51]** If a Marketing URL is set, is it a full URL including the protocol that gives more information about the app?
  - quote: "The website where users get more information about the app. Specify the entire URL, including the protocol."
  - surface: asc
  - verify: Read Marketing URL per language; check protocol prefix and HTTP 200; confirm the page is about this app.
  - fix: Correct the URL or clear the optional field.

## META.PVI.VERSION Platform version — Version Number and Copyright

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Version Number | The version number that's provided for your app that appears on App Store product pages and is displayed when users install your app. |
> | Copyright | The name of the person or entity that owns the exclusive rights to the app, preceded by the year the rights were obtained (for example, 2014 Example, Inc.). The copyright symbol is added automatically. This property is required. |
>
> (Bundle ID row) (A build is uniquely identified by the combination of the bundle ID, version number, and build string.)

**Applies to:** All apps

Navigation path: version page > Copyright; version number is the version shown in the sidebar under the platform.

- **[META-52]** Is the Copyright field filled in as the year followed by the person or entity owning the exclusive rights (e.g. “2014 Example, Inc.”), without typing the copyright symbol (it is added automatically)?
  - quote: "The name of the person or entity that owns the exclusive rights to the app, preceded by the year the rights were obtained (for example, 2014 Example, Inc.). The copyright symbol is added automatically."
  - surface: asc
  - verify: Read Copyright; check regex `^\d{4} .+`; flag a leading `©`/`(c)` (would display twice) or an empty field.
  - fix: Enter "<year> <owner name>" and Save.
- **[META-53]** Is the owner named in Copyright the person or entity that actually owns the exclusive rights to the app?
  - quote: "The name of the person or entity that owns the exclusive rights to the app"
  - surface: manual
  - verify: Compare with the developer/seller name in the account and the copyright line in the app (grep for `©`/`Copyright` in strings, `NSHumanReadableCopyright` in Info.plist for macOS).
  - fix: manual — requires developer decision/legal/business action.
- **[META-54]** Is the build attached to this version identified by the expected bundle ID, version number, and build string (the three values Apple says uniquely identify a build)?
  - quote: "A build is uniquely identified by the combination of the bundle ID, version number, and build string."
  - surface: code
  - verify: Read `MARKETING_VERSION` / `CFBundleShortVersionString` and `CURRENT_PROJECT_VERSION` / `CFBundleVersion` in the project; compare with the version shown in the ASC sidebar and the build selected in the Build section.
  - fix: If the attached build is not the intended one (wrong bundle ID, version number, or build string), select or upload the intended build.

## META.PVI.ROUTING Platform version — Routing App Coverage File

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Routing App Coverage File | A routing app’s geographic coverage file (a file with a .geojson file extension) that specify the geographic regions supported by your app. The file can have only one MultiPolygon element. MultiPolygon elements consist of at least one Polygon. Polygons contain at least four coordinate points. The start and end coordinate points for a polygon must be the same. For file specifications, read “Specifying the Geographic Coverage File Contents” in Location and Maps Programming Guide. |
>
> (Upload a geographic coverage file — iOS, watchOS) If you submit a routing app to App Review, Apple doesn’t start the review process until you upload a geographic coverage file. You can upload the geographic coverage file when you first create the app record or later after you upload a build.
>
> For the complete steps to configure a routing app, an app that provides point-to-point directions for other apps, visit Configure a routing app (iOS, watchOS) in Xcode Help.
> - In Apps, select the app you want to view.
> - In the sidebar, click the version of your app that you want to edit.
> - Click the Choose File button under Routing App Coverage File.

**Applies to:** Routing apps (apps that provide point-to-point directions for other apps), iOS and watchOS

- **[META-55]** If the app is a routing app, has a geographic coverage (.geojson) file been uploaded?
  - quote: "If you submit a routing app to App Review, Apple doesn’t start the review process until you upload a geographic coverage file."
  - surface: code
  - verify: Detect a routing app in the project (e.g. `MKDirectionsApplicationSupportedModes` in Info.plist, a Maps routing capability, or a `.geojson` in the repo). If present, on the ASC version page confirm a file is shown under Routing App Coverage File.
  - fix: Upload the .geojson via "Choose File" under Routing App Coverage File.
- **[META-56]** Does the coverage file contain exactly one MultiPolygon, each Polygon with at least four coordinate points and identical start and end points?
  - quote: "The file can have only one MultiPolygon element. MultiPolygon elements consist of at least one Polygon. Polygons contain at least four coordinate points. The start and end coordinate points for a polygon must be the same."
  - surface: code
  - verify: Parse the .geojson with a JSON parser (do not execute it): count MultiPolygon geometries (must be 1), each polygon ring length ≥ 4, ring[0] == ring[-1]; extension must be `.geojson`.
  - fix: Regenerate the file to meet these rules.

## META.PVI.RELEASE Platform version — Version Release Settings, What’s New, Phased Release, Reset Overview Rating

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Version Release Settings | Determines how the app version will be released. The following settings are allowed: |
> - Manual. When the app status changes to Pending Developer Release after approval and you must manually release the version.
> - Automatic. The app goes live automatically after it is approved by App Review.
> - Automatic, no earlier than. If the date hasn't passed when the app is approved, the app status changes to Pending Developer Release, but is automatically released at the date specified.
>
> | What’s New in this Version | A description of the changes in this version of the app, such as new features, UI improvements, or bug fixes. Limited to 4000 characters. We recommend that you provide detailed information to let users know the specifics of the changes, improvements, or fixes in the version. This property isn't available for the first version of the app but required for all subsequent versions. This property can be localized. |
> | Phased Release for Automatic Updates | When you release a version update of your app, you can choose to release your iOS app in stages. If you choose this option, your version update will be released over a 7-day period to a percentage of your users on iOS with automatic updates turned on. Learn how to release a version update in phases. |
> | Reset Overview Rating | You can reset your app’s overview rating when you release a new version. Learn how to reset overview rating. |
>
> (Required, localizable, and editable properties)
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Version Release Settings | ✓ | | |
> | What’s New in this Version | 1 | ✓ | |
> | Phased Release for Automatic Updates | 1 | | 2 |
> | Reset overview rating | 1 | | |
>
> 1 Required for version updates only.
> 2 Version release can be paused at any time within the seven-day window, but can't be changed once a version is released to all users.
>
> (Creating your product page — What’s New) When you update your app, you can use What’s New to communicate changes to users. This text appears on your product page and on the Updates tab.
>
> If you added a feature or fixed a bug based on feedback, use What’s New to let users know that you’ve listened to them. List new features, content, or functionality in order of importance, and add call-to-action messaging that gets users excited about the update.

**Applies to:** All apps (release setting); version updates (What’s New, phased release, reset rating choice)

Navigation path: version page (sidebar > app version under the platform) > the Version Release Settings, What’s New in this Version, Phased Release for Automatic Updates, and Reset Overview Rating properties.

- **[META-57]** Is a Version Release setting chosen (Manual, Automatic, or Automatic, no earlier than <date>) and does it match the developer’s intended launch timing?
  - quote: "Determines how the app version will be released."
  - surface: asc
  - verify: Read the version-release option on the version page; if "no earlier than", confirm the date/time is in the future and intended.
  - fix: Select the intended option and Save.
- **[META-58]** For any version after the first, is What’s New in this Version filled in for every localization?
  - quote: "This property isn't available for the first version of the app but required for all subsequent versions."
  - surface: asc
  - verify: If the app already has a released version, read What’s New for each language; fail if empty.
  - fix: Write release notes for each localization (derive from git log/CHANGELOG between the last released tag and HEAD).
- **[META-59]** Is What’s New at most 4000 characters?
  - quote: "Limited to 4000 characters."
  - surface: asc
  - verify: Count characters of each localized What’s New; fail if > 4000.
  - fix: Shorten.
- **[META-60]** Does What’s New describe the actual changes in this version (features, UI improvements, bug fixes)?
  - quote: "A description of the changes in this version of the app, such as new features, UI improvements, or bug fixes."
  - surface: code
  - verify: Compare What’s New items with the code diff/commit history since the previously released version; flag claims with no corresponding change.
  - fix: Rewrite What’s New to match the shipped changes.
- **[META-61]** For a version update, has the developer chosen whether to use phased release and whether to reset the overview rating?
  - quote: "1 Required for version updates only."
  - surface: asc
  - verify: On an update’s version page, confirm the Phased Release for Automatic Updates and Reset Overview Rating properties have deliberate selections.
  - fix: manual — requires developer decision/legal/business action.

## META.REVIEW App Review Information

**Source text (verbatim):**
> You must provide the following information to App Review. It isn’t visible to customers and can be edited at any time.
>
> Submissions that include an app version will be reviewed together with the App Review information for that version.
>
> Submissions that don’t include an app version, or those that include items associated with multiple platforms, will be reviewed together with the App Review information for the latest approved version of the platform you specify during the submission process. To edit the App Review information on an approved app version, click Edit in the top right corner of the App Review Information section.
>
> | Property | Description | Required |
> |---|---|---|
> | Contact: Name, email, phone number | Information for the contact person in your organization if the App Review team needs additional information. Enter the phone number in international format, including a plus sign (+) followed by the country code (for example, +852 for Hong Kong) — the field doesn't accept numbers-only entry. | ✓ |
> | Notes | Additional information about your app that can help during the review process. Include information that may be needed to test your app, such as app-specific settings and test registration or account details. If your app delivers streaming video over the cellular network, enter a test stream URL. The Notes field can contain up to 4000 bytes. You can write notes in any language. | |
> | Sign-in required: Username and password | Sign-in information for a demo account. If your app uses a single sign-on service, such as Facebook or Twitter, include the demo account login information for it. The demo account is used during the App Review process and must not expire. Details for additional accounts should be included in the Notes field. | If your app requires a login to use it. |
>
> (Required, localizable, and editable properties)
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | App review information | ✓ | | ✓ |
>
> (Overview of submitting for review) Use the App Review information section on the latest approved app version for that platform to provide additional information or context that will help App Review during the review process.

**Applies to:** All apps (contact info); apps that require a login (sign-in); apps delivering streaming video over cellular (test stream URL)

Navigation path: version page > App Review Information section (scroll down); on an approved version, "click Edit in the top right corner of the App Review Information section."

- **[META-62]** Are the App Review contact name, email, and phone number all filled in?
  - quote: "Information for the contact person in your organization if the App Review team needs additional information."
  - surface: asc
  - verify: On the version page, read App Review Information > Contact (name, email, phone number): all non-empty.
  - fix: Enter a reachable contact and Save.
- **[META-63]** Is the contact phone number in international format, beginning with + and the country code?
  - quote: "Enter the phone number in international format, including a plus sign (+) followed by the country code (for example, +852 for Hong Kong) — the field doesn't accept numbers-only entry."
  - surface: asc
  - verify: Check the phone value against regex `^\+\d`.
  - fix: Re-enter as +<country code><number>.
- **[META-64]** If the app requires a login to use it, are a demo account username and password provided under Sign-in required?
  - quote: "If your app requires a login to use it."
  - surface: code
  - verify: Detect login gates in code (e.g. `ASAuthorizationAppleIDProvider`, `GIDSignIn`, `FirebaseAuth`, `Auth.auth()`, Supabase/Auth0/MSAL SDKs, custom login views shown before main content) and confirm at runtime whether core features require sign-in. Then check ASC: "Sign-in required" is checked and username/password are filled.
  - fix: Create a dedicated demo account, check Sign-in required, and enter its credentials.
- **[META-65]** Does the demo account work and is it set to never expire?
  - quote: "The demo account is used during the App Review process and must not expire."
  - surface: runtime
  - verify: Sign in to the current build on a simulator/device with the exact credentials from ASC; confirm full access (including paid/gated areas reviewers must see). Ask the developer whether the account has an expiry, trial limit, 2FA, or region lock.
  - fix: Provide a demo account that does not expire; put any extra access details reviewers need in Notes.
- **[META-66]** If the app uses a single sign-on service, is demo login information for that service included?
  - quote: "If your app uses a single sign-on service, such as Facebook or Twitter, include the demo account login information for it."
  - surface: code
  - verify: grep for third-party SSO SDKs (FBSDKLoginKit, GoogleSignIn, Twitter/X, MSAL, OAuth `ASWebAuthenticationSession` flows). If the SSO path is the only login, confirm SSO demo credentials are present in ASC.
  - fix: Add SSO demo credentials (Sign-in fields or Notes).
- **[META-67]** Are details for any additional accounts (e.g. different roles or tiers) placed in the Notes field?
  - quote: "Details for additional accounts should be included in the Notes field."
  - surface: asc
  - verify: If the app has multiple roles (admin/user, free/paid, teacher/student found in code), confirm Notes lists credentials for each role reviewers need.
  - fix: Add the extra accounts to Notes.
- **[META-68]** Do the Notes include information needed to test the app (app-specific settings, test registration or account details)?
  - quote: "Include information that may be needed to test your app, such as app-specific settings and test registration or account details."
  - surface: asc
  - verify: Identify non-obvious requirements in the code/runtime (hardware accessories, location/region, feature flags, QR codes, invite codes, hidden gestures, server-side configuration) and confirm Notes explains each.
  - fix: Write Notes with step-by-step test instructions.
- **[META-69]** If the app delivers streaming video over the cellular network, is a test stream URL in the Notes?
  - quote: "If your app delivers streaming video over the cellular network, enter a test stream URL."
  - surface: code
  - verify: grep for streaming video playback (`AVPlayer` with `.m3u8`/HLS URLs, `AVPlayerViewController`, third-party players) not restricted to Wi-Fi (`allowsCellularAccess`, `NWPathMonitor` checks). If present, confirm Notes contains a test stream URL.
  - fix: Add a working test stream URL to Notes.
- **[META-70]** Are the Notes at most 4000 bytes?
  - quote: "The Notes field can contain up to 4000 bytes."
  - surface: asc
  - verify: Copy Notes and compute UTF-8 byte length; fail if > 4000.
  - fix: Shorten the Notes to 4000 bytes or less.
- **[META-71]** For submissions without an app version (e.g. In-App Events, custom product pages), is the App Review Information on the latest approved version of that platform up to date?
  - quote: "will be reviewed together with the App Review information for the latest approved version of the platform you specify during the submission process"
  - surface: asc
  - verify: Open the latest approved version page; read App Review Information (credentials still valid, Notes current).
  - fix: Click Edit in the top right of the App Review Information section on that version and update.

## META.RLE Required, localizable, and editable properties

**Source text (verbatim):**
> The tables below show the app and version properties required for App Store submission. The tables also indicate the properties that can be localized and edited at any time without submitting a new version of your app.
>
> App information
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Name | ✓ | ✓ | |
> | Subtitle | | ✓ | |
> | Age Rating | ✓ | | |
> | Bundle ID | ✓ | | |
> | SKU | ✓ | | |
> | Content Rights | ✓ | | |
> | License Agreement | | 1 | ✓ |
> | Primary Language | ✓ | | ✓ |
> | Primary Category | ✓ | | |
> | Secondary Category | | | |
> | Availability in the Republic of Korea2 | | | 4 |
> | Availability in China mainland3 | | | 4 |
> | Availability in Vietnam | | | |
> | URL for App Store Server Notifications5 | | | ✓ |
> | Digital Services Act (DSA) Status | ✓ | | ✓ |
> | Regulated Medical Devices | 6 | 7 | ✓ |
>
> 1 Localized text may be included in the Custom License Agreement text box.
> 2 Required for developers who enroll as an organization and distribute apps on the App Store in South Korea.
> 3 Required for apps that meet certain criteria to be available on the App Store in China mainland. Learn about availability requirements.
> 4 Can be entered at any time, but will be submitted for review with the next version submission.
> 5 Only visible for apps that offer In-App Purchases.
> 6 Required for apps that meet certain criteria to be available on the App Store in the EU/EEA, UK, or U.S.. Learn about availability requirements.
> 7 Localized text is only for the Use Statement and Safety Information.
>
> Platform version information
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Support URL | ✓ | ✓ | |
> | Marketing URL | | ✓ | |
> | App Motion information | 3 | | ✓ |
> | Version Number | ✓ | | |
> | Copyright | ✓ | | ✓ |
> | Routing App Coverage File | | | ✓ |
> | App review information | ✓ | | ✓ |
> | Version Release Settings | ✓ | | |
> | What’s New in this Version | 1 | ✓ | |
> | Phased Release for Automatic Updates | 1 | | 2 |
> | Reset overview rating | 1 | | |
>
> 1 Required for version updates only.
> 2 Version release can be paused at any time within the seven-day window, but can't be changed once a version is released to all users.
> 3 Required for visionOS apps only.
>
> App privacy
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Privacy Policy URL | ✓ | ✓ | |
> | Privacy Choices URL | | ✓ | |
> | Data Types | ✓ | | ✓ |
>
> App accessibility
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Accessibility URL | | | ✓ |
> | Accessibility Support | | | ✓ |

(The same page also contains tables for App Clips, pricing and availability, In-App Purchases, subscriptions, Game Center, and In-App Events; those are outside this file’s scope.)

**Applies to:** All apps (visionOS apps for App Motion information)

- **[META-72]** For a visionOS app, is the App Motion information provided?
  - quote: "3 Required for visionOS apps only."
  - surface: asc
  - verify: If the project has a visionOS target (SDKROOT = xros) or ASC lists visionOS, open the visionOS version page and confirm App Motion information is completed.
  - fix: Complete the App Motion information for the visionOS version.
- **[META-73]** Have App Privacy Data Types been declared (required)?
  - quote: "| Data Types | ✓ | | ✓ |"
  - surface: asc
  - verify: Open the App Privacy page in the sidebar and confirm data collection answers are published (cross-check with PrivacyInfo.xcprivacy and SDKs — see the privacy reference).
  - fix: Complete and publish the App Privacy questionnaire.
- **[META-74]** Are final values in place for properties the tables do not mark as Editable (e.g. Name, Subtitle, Support URL, Marketing URL, Version Number), since only properties marked Editable can be edited at any time without submitting a new version?
  - quote: "The tables also indicate the properties that can be localized and edited at any time without submitting a new version of your app."
  - surface: manual
  - verify: Confirm with the developer that final copy for non-editable fields is in place before submitting.
  - fix: manual — requires developer decision/legal/business action.

## META.SS.GENERAL Screenshot specifications — counts, formats, and display scaling

**Source text (verbatim):**
> You must include at least one screenshot and can upload up to 10 screenshots per device size in .jpeg, .jpg, or .png formats, with the following specifications. All screenshots must adhere to the App Store Review Guidelines before you submit them for review.
>
> Display scaling
>
> If your app’s user interface is consistent across multiple device sizes and localizations, you only need to provide screenshots for the highest required resolution. App Store Connect automatically scales them down for smaller device sizes.
>
> If you prefer not to use scaled screenshots, you can upload specific screenshots and app previews tailored to each device size and localization. If an app preview is not provided for a specific language, the preview in the next best available language appears on your App Store product page.
>
> Note: Images can’t include alpha channels or transparencies.
>
> (Creating your product page — Screenshots) Use images captured from your app’s UI to visually communicate your app’s user experience. You can feature up to 10 screenshots on your App Store and Mac App Store product pages. Depending on the orientation of your screenshots, the first one to three images will appear in search results when no app preview is available, so make sure these highlight the essence of your app. Focus each subsequent screenshot on a main benefit or feature so that you fully convey your app’s value. If your app supports Dark Mode, consider including at least one screenshot that showcases what the experience looks like for users.

**Applies to:** All apps

Navigation path: version page > Product Page Information > App Previews and Screenshots tab > device tab; or "View All Sizes in Media Manager".

- **[META-75]** Does each provided device size have between 1 and 10 screenshots?
  - quote: "You must include at least one screenshot and can upload up to 10 screenshots per device size"
  - surface: asc
  - verify: In Media Manager (View All Sizes), for each language and device size count screenshots; fail if a required size has 0 or any size has > 10.
  - fix: Add or remove screenshots.
- **[META-76]** Is every screenshot a .jpeg, .jpg, or .png file?
  - quote: "in .jpeg, .jpg, or .png formats"
  - surface: code
  - verify: For local screenshot sources (e.g. fastlane/screenshots, marketing folders) run `file`/`sips -g format` on each; in ASC, check uploads were accepted.
  - fix: Re-export as PNG or JPEG.
- **[META-77]** Are screenshots free of alpha channels and transparency?
  - quote: "Note: Images can’t include alpha channels or transparencies."
  - surface: code
  - verify: For each local screenshot, run `sips -g hasAlpha <file>` (macOS) or inspect PNG color type; fail if `hasAlpha: yes`.
  - fix: Flatten onto an opaque background and re-export without alpha (e.g. export JPEG, or `sips -s format jpeg`).
- **[META-78]** Do all screenshots adhere to the App Store Review Guidelines (accurate metadata, 2.3.3)?
  - quote: "All screenshots must adhere to the App Store Review Guidelines before you submit them for review."
  - surface: asc
  - verify: Review every screenshot against guideline 2.3.3/2.3.4 checks in the guidelines reference (app in use, not just title art/splash/login; accurate UI; no misleading content).
  - fix: Replace non-compliant screenshots.
- **[META-84]** Is every uploaded screenshot exactly one of the accepted pixel sizes for its display slot?
  - quote: "You must include at least one screenshot and can upload up to 10 screenshots per device size in .jpeg, .jpg, or .png formats, with the following specifications."
  - surface: code
  - verify: For local screenshot files run `sips -g pixelWidth -g pixelHeight` and match each against the table in META.SS.SIZES for the intended slot.
  - fix: Recapture on the matching simulator or resize/crop to an accepted size (keep UI undistorted).
- **[META-87]** If relying only on highest-resolution (scaled) screenshots, is the app’s UI actually consistent across device sizes and localizations (the condition Apple states for providing only the highest required resolution)?
  - quote: "If your app’s user interface is consistent across multiple device sizes and localizations, you only need to provide screenshots for the highest required resolution."
  - surface: runtime
  - verify: Run the app on the smallest and largest supported devices and in each localized language (including RTL); if layouts/text differ materially, check Media Manager for per-size/per-language uploads rather than scaled ones.
  - fix: Upload tailored screenshots for those sizes/localizations.

## META.SS.REQ Screenshot specifications — Required device sizes

**Source text (verbatim):**
> To submit your app, you must provide screenshots for the following required display sizes:
> - iPhone: At least one screenshot for iPhone with Dynamic Island (medium display).
> - iPad (if your app supports iPadOS): At least one screenshot for iPad 13-inch display.

Note: The entries below are the Requirement and Notes entries Apple shows for the named displays in the Specifications section (full lists under META.SS.SIZES).
>
> **iPhone with Face ID (large display)**
> Requirement
> - Required if app runs on iPhone and screenshots for iPhone with Dynamic Island (large display) aren't provided
>
> **13" display**
> Requirement
> - Required if app runs on iPad
>
> **Mac**
> Requirement
> - Required for Mac apps
>
> **Apple TV**
> Requirement
> - Required for Apple TV apps
>
> **Apple Vision Pro**
> Requirement
> - Required for Apple Vision Pro
>
> **Apple Watch**
> Requirement
> - Required for Apple Watch apps
>
> **iPhone Duo**
> Notes
> - Starting in April 2027, screenshots will be required for any app using the iOS 27.1 SDK or later. Learn how to prepare your apps for launch on iPhone Duo
> - When you submit iPhone Duo screenshots in App Store Connect, your App Store product page will display a badge to let people know your app is optimized for iPhone Duo.

**Applies to:** Per platform/device family the app supports

- **[META-79]** If the app runs on iPhone, is there at least one screenshot for iPhone with Dynamic Island (medium display)?
  - quote: "iPhone: At least one screenshot for iPhone with Dynamic Island (medium display)."
  - surface: asc
  - verify: Code: `TARGETED_DEVICE_FAMILY` contains 1 (iPhone). ASC: Media Manager shows ≥ 1 screenshot in the iPhone Dynamic Island (medium display) slot (sizes 1179 x 2556 / 1206 x 2622 or landscape).
  - fix: Capture on an iPhone 18 Pro/17 Pro/16 Pro-class simulator and upload.
- **[META-80]** If the app runs on iPhone and no Dynamic Island (large display) screenshots are provided, are iPhone with Face ID (large display) screenshots provided?
  - quote: "Required if app runs on iPhone and screenshots for iPhone with Dynamic Island (large display) aren't provided"
  - surface: asc
  - verify: In Media Manager, check the iPhone large-display slots: either Dynamic Island (large) or Face ID (large) must have screenshots.
  - fix: Upload screenshots at 1320 x 2868 / 1290 x 2796 / 1260 x 2736 (Dynamic Island large) or 1284 x 2778 / 1242 x 2688 (Face ID large).
- **[META-81]** If the app supports iPadOS / runs on iPad, is there at least one 13-inch iPad screenshot?
  - quote: "iPad (if your app supports iPadOS): At least one screenshot for iPad 13-inch display."
  - surface: code
  - verify: `TARGETED_DEVICE_FAMILY` contains 2 (or the iPhone app is not restricted from iPad); ASC Media Manager shows ≥ 1 screenshot in the iPad 13" slot (2064 x 2752 / 2048 x 2732 or landscape).
  - fix: Capture on an iPad Pro 13-inch simulator and upload.
- **[META-82]** For Mac apps, are Mac screenshots provided?
  - quote: "Required for Mac apps"
  - surface: asc
  - verify: If the project has a macOS target, confirm the macOS version in ASC has screenshots at a Mac size in META.SS.SIZES.
  - fix: Capture and upload Mac screenshots.
- **[META-133]** For Apple TV apps, are Apple TV screenshots provided?
  - quote: "Required for Apple TV apps"
  - surface: asc
  - verify: If the project has a tvOS target, confirm the tvOS version in ASC has screenshots at 1920 x 1080 or 3840 x 2160 pixels.
  - fix: Capture and upload Apple TV screenshots.
- **[META-134]** For Apple Vision Pro apps, are Apple Vision Pro screenshots provided?
  - quote: "Required for Apple Vision Pro"
  - surface: asc
  - verify: If the project has a visionOS target, confirm the visionOS version in ASC has screenshots at 3840 x 2160 pixels.
  - fix: Capture and upload Apple Vision Pro screenshots.
- **[META-135]** For Apple Watch apps, are Apple Watch screenshots provided?
  - quote: "Required for Apple Watch apps"
  - surface: asc
  - verify: If the project has a watchOS target, confirm Media Manager has Apple Watch screenshots at one of the listed Watch sizes.
  - fix: Capture and upload Apple Watch screenshots via View All Sizes in Media Manager.
- **[META-83]** If the app is built with the iOS 27.1 SDK or later and will be submitted from April 2027, are iPhone Duo screenshots provided?
  - quote: "Starting in April 2027, screenshots will be required for any app using the iOS 27.1 SDK or later."
  - surface: code
  - verify: Read the SDK used (`SDKROOT`, Xcode version / `DTSDKName` in the built Info.plist). If iOS 27.1+ and the submission date is April 2027 or later, check Media Manager for iPhone Duo screenshots (outer 1398 × 2034 / inner 2007 × 2853 or landscape).
  - fix: Capture iPhone Duo screenshots for outer and/or inner display and upload.

## META.SS.SIZES Screenshot specifications — Accepted sizes per display

**Source text (verbatim):**
> **iPhone**
>
> **iPhone Duo**
> Screenshot size
> - 1398 × 2034 pixels
> - 2034 × 1398 pixels (outer display)
> - 2007 × 2853 pixels
> - 2853 × 2007 pixels (inner display)
> Notes
> - Starting in April 2027, screenshots will be required for any app using the iOS 27.1 SDK or later. Learn how to prepare your apps for launch on iPhone Duo
> - When you submit iPhone Duo screenshots in App Store Connect, your App Store product page will display a badge to let people know your app is optimized for iPhone Duo.
>
> **iPhone with Dynamic Island (large display)**
> - iPhone Air
> - iPhone 18 Pro Max
> - iPhone 17 Pro Max
> - iPhone 16 Pro Max
> - iPhone 16 Plus
> - iPhone 15 Pro Max
> - iPhone 15 Plus
> - iPhone 14 Pro Max
> Screenshot size
> - 1260 x 2736 pixels (portrait)
> - 2736 x 1260 pixels (landscape)
> - 1290 x 2796 pixels (portrait)
> - 2796 x 1290 pixels (landscape)
> - 1320 x 2868 pixels (portrait)
> - 2868 x 1320 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Face ID (large display) are used.
>
> **iPhone with Face ID (large display)**
> - iPhone 14 Plus
> - iPhone 13 Pro Max
> - iPhone 12 Pro Max
> - iPhone 11 Pro Max
> - iPhone 11
> - iPhone XS Max
> - iPhone XR
> Screenshot size
> - 1284 x 2778 pixels (portrait)
> - 2778 x 1284 pixels (landscape)
> - 1242 x 2688 pixels (portrait)
> - 2688 x 1242 pixels (landscape)
> Requirement
> - Required if app runs on iPhone and screenshots for iPhone with Dynamic Island (large display) aren't provided
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Dynamic Island (large display) are used.
>
> **iPhone with Dynamic Island (medium display)**
> - iPhone 18 Pro
> - iPhone 17 Pro
> - iPhone 17
> - iPhone 16 Pro
> - iPhone 16
> - iPhone 15 Pro
> - iPhone 15
> - iPhone 14 Pro
> Screenshot size
> - 1179 x 2556 pixels (portrait)
> - 2556 x 1179 pixels (landscape)
> - 1206 x 2622 pixels (portrait)
> - 2622 x 1206 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Face ID (large display) are used.
>
> **iPhone with Face ID (medium display)**
> - iPhone 17e
> - iPhone 16e
> - iPhone 14
> - iPhone 13 Pro
> - iPhone 13
> - iPhone 13 mini
> - iPhone 12 Pro
> - iPhone 12
> - iPhone 12 mini
> - iPhone 11 Pro
> - iPhone XS
> - iPhone X
> Screenshot size
> - 1170 x 2532 pixels (portrait)
> - 2532 x 1170 pixels (landscape)
> - 1125 x 2436 pixels (portrait)
> - 2436 x 1125 pixels (landscape)
> - 1080 x 2340 pixels (portrait)
> - 2340 x 1080 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Dynamic Island (medium display) are used.
>
> **iPhone with Home Button (large display)**
> - iPhone 8 Plus
> - iPhone 7 Plus
> - iPhone 6S Plus
> - iPhone 6 Plus
> Screenshot size
> - 1242 x 2208 pixels (portrait)
> - 2208 x 1242 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Face ID (medium display) are used.
>
> **iPhone with Home Button (medium display)**
> - iPhone SE (3rd generation, 2nd generation)
> - iPhone 8
> - iPhone 7
> - iPhone 6S
> - iPhone 6
> Screenshot size
> - 750 x 1334 pixels (portrait)
> - 1334 x 750 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Home Button (large display) are used.
>
> **iPhone with Home Button (4" display)**
> - iPhone SE (1st generation)
> - iPhone 5S
> - iPhone 5C
> - iPhone 5
> Screenshot size
> - 640 x 1096 pixels (portrait without status bar)
> - 640 x 1136 pixels (portrait with status bar)
> - 1136 x 600 pixels (landscape without status bar)
> - 1136 x 640 pixels (landscape with status bar)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Home Button (medium display) are used.
>
> **iPhone with Home Button (3.5" display)**
> - iPhone 4S
> - iPhone 4
> Screenshot size
> - 640 x 920 pixels (portrait without status bar)
> - 640 x 960 pixels (portrait with status bar)
> - 960 x 600 pixels (landscape without status bar)
> - 960 x 640 pixels (landscape with status bar)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for iPhone with Home Button (4" display) are used.
>
> **iPad**
>
> **13" display**
> - iPad Pro (M5, M4)
> - iPad Pro (6th generation, 5th generation, 4th generation, 3rd generation, 1st generation)
> - iPad Air (M4, M3, M2)
> Screenshot size
> - 2064 x 2752 pixels (portrait)
> - 2752 x 2064 pixels (landscape)
> - 2048 x 2732 pixels (portrait)
> - 2732 x 2048 pixels (landscape)
> Requirement
> - Required if app runs on iPad
>
> **12.9" display**
> - iPad Pro (2nd generation)
> Screenshot size
> - 2048 x 2732 pixels (portrait)
> - 2732 x 2048 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for 13" displays are used.
>
> **11" display**
> - iPad Pro (M5, M4)
> - iPad Pro (4th generation, 3rd generation, 2nd generation, 1st generation)
> - iPad Air (M4, M3, M2)
> - iPad Air (5th generation, 4th generation)
> - iPad (A16)
> - iPad (10th generation)
> - iPad mini (A17 Pro)
> - iPad mini (6th generation)
> Screenshot size
> - 1488 x 2266 pixels (portrait)
> - 2266 x 1488 pixels (landscape)
> - 1668 x 2420 pixels (portrait)
> - 2420 x 1668 pixels (landscape)
> - 1668 x 2388 pixels (portrait)
> - 2388 x 1668 pixels (landscape)
> - 1640 x 2360 pixels (portrait)
> - 2360 x 1640 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for 13" displays are used.
>
> **10.5" display**
> - iPad Pro
> - iPad Air (3rd generation)
> - iPad (9th generation, 8th generation, 7th generation)
> Screenshot size
> - 1668 x 2224 pixels (portrait)
> - 2224 x 1668 pixels (landscape)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for 12.9" displays are used.
>
> **9.7" display**
> - iPad Pro
> - iPad Air
> - iPad Air 2
> - iPad
> - iPad 2
> - iPad (6th generation, 5th generation, 4th generation, 3rd generation)
> - iPad mini (5th generation)
> - iPad mini 4
> - iPad mini 3
> - iPad mini 2
> Screenshot size
> - 1536 x 2008 pixels (portrait without status bar)
> - 1536 x 2048 pixels (portrait with status bar)
> - 2048 x 1496 pixels (landscape without status bar)
> - 2048 x 1536 pixels (landscape with status bar)
> - 768 x 1004 pixels (portrait without status bar)
> - 768 x 1024 pixels (portrait with status bar)
> - 1024 x 748 pixels (landscape without status bar)
> - 1024 x 768 pixels (landscape with status bar)
> Note
> - If screenshots with the accepted sizes aren't provided, scaled screenshots for 10.5" displays are used.
>
> **Mac**
> Screenshot size
> - One of the following, with a 16:10 aspect ratio
> - 1280 x 800 pixels
> - 1440 x 900 pixels
> - 2560 x 1600 pixels
> - 2880 x 1800 pixels
> Requirement
> - Required for Mac apps
>
> **Apple TV**
> Screenshot size
> - 1920 x 1080 pixels
> - 3840 x 2160 pixels
> Requirement
> - Required for Apple TV apps
>
> **Apple Vision Pro**
> Screenshot size
> - 3840 x 2160 pixels
> Requirement
> - Required for Apple Vision Pro
>
> **Apple Watch**
> - Ultra 4, Ultra 3, Ultra 2, Ultra, Series 12, Series 11, Series 10, Series 9, Series 8, Series 7, Series 6, Series 5, Series 4, Series 3, Series 2, Series 1, SE 3, SE 2, SE
> Screenshot size
> - One of the following:
> - 422 x 514 pixels (Ultra 4, Ultra 3)
> - 410 x 502 pixels (Ultra 2, Ultra)
> - 416 x 496 pixels (Series 12, Series 11, Series 10)
> - 396 x 484 pixels (Series 9, Series 8, Series 7)
> - 368 x 448 pixels (Series 6, Series 5, Series 4, SE 3, SE 2, SE)
> - 312 x 390 pixels (Series 3, Series 2, Series 1)
> Requirement
> - Required for Apple Watch apps
> Note
> - You must use the same screenshot size for Apple Watch consistently across all localizations for the app

**Applies to:** All apps (per supported display/platform)

- **[META-85]** Do Mac screenshots use a 16:10 size from the list (1280 x 800, 1440 x 900, 2560 x 1600, 2880 x 1800)?
  - quote: "One of the following, with a 16:10 aspect ratio"
  - surface: code
  - verify: Check pixel dimensions of Mac screenshots.
  - fix: Re-export at one of the listed sizes.
- **[META-86]** For Apple Watch apps, is the same screenshot size used across all localizations?
  - quote: "You must use the same screenshot size for Apple Watch consistently across all localizations for the app"
  - surface: asc
  - verify: In Media Manager, for each localization, read Apple Watch screenshot dimensions; all must be the same size.
  - fix: Re-upload Watch screenshots at one consistent size for every localization.

## META.AP.GENERAL App preview specifications — Overview and upload rules

**Source text (verbatim):**
> App previews give customers a look at your app or game's main features, functionality, and content, right on the App Store product page.
>
> App previews are optional. You can upload up to three app previews per supported device size and language for iOS, macOS, tvOS, and visionOS apps. If you upload an app preview in an aspect ratio that differs from your screenshots, it appears in the “A Closer Look” section on your product page.
>
> To create an app preview, make sure you have the following:
> - A Mac running macOS 10.10 or later, with Safari 8 or later
> - A video editor, such as iMovie or Final Cut Pro X
> - One of the following devices:
>   - iPhone (iPhone with Face ID (large display), iOS 8 or later)
>   - iPad (13" display, iOS 8 or later)
>   - Apple TV
>   - Apple Vision Pro
>
> When you upload
> - Display order: App previews always appear before screenshots on iPhone, iPad, Mac, and Apple TV — even if you reorder them in your app record. If a preview video uses an aspect ratio different from your screenshots, it appears in the “A Closer Look” section of your product page instead.
> - File formats: .mov, .m4v, .mp4 (H.264); .mov for ProRes 422 (HQ only).
> - Poster frame: You choose the image shown on the product page and during app install. Learn how to set the poster frame.
> - Processing time: Up to 24 hours after upload.
> - iMessage: App previews are not available for apps on the App Store for iMessage.
> - Orientation:
>   - iOS apps: Landscape or Portrait (rotates to original orientation on play)
>   - macOS, tvOS, visionOS apps: Landscape only
> - Scaling: If your app's user interface is the same across multiple device sizes and localizations, provide only the highest resolution required. They automatically scale down to smaller device sizes.
> - Unscaled versions: If you prefer not to use scaled versions, you can add specific screenshots and app previews for other device sizes and localizations. If a localized app preview is missing for your localized metadata, the app preview in the next best available language is used on App Store product pages and displayed to users when they install your app.

**Applies to:** Apps that upload app previews (iOS, macOS, tvOS, visionOS)

- **[META-88]** Are there at most three app previews per supported device size and language?
  - quote: "You can upload up to three app previews per supported device size and language for iOS, macOS, tvOS, and visionOS apps."
  - surface: asc
  - verify: Media Manager: count previews per language per device size.
  - fix: Remove extras.
- **[META-89]** Is each preview file .mov, .m4v, or .mp4 (H.264), or .mov (ProRes 422 HQ)?
  - quote: "File formats: .mov, .m4v, .mp4 (H.264); .mov for ProRes 422 (HQ only)."
  - surface: code
  - verify: For local preview files run `ffprobe -v error -show_entries stream=codec_name,profile -of csv` (or `mdls`/`avmediainfo`) and check container extension and codec.
  - fix: Re-export from the video editor as H.264 (.mov/.m4v/.mp4) or ProRes 422 HQ (.mov).
- **[META-90]** For macOS, tvOS, and visionOS apps, are app previews landscape only?
  - quote: "macOS, tvOS, visionOS apps: Landscape only"
  - surface: code
  - verify: Check preview width > height for those platforms (ffprobe `width,height`).
  - fix: Re-record/export in landscape.
- **[META-91]** For apps on the App Store for iMessage, is the plan free of app previews (they are not available there)?
  - quote: "iMessage: App previews are not available for apps on the App Store for iMessage."
  - surface: asc
  - verify: If the app is an iMessage-only/sticker app (Messages extension target only), confirm no preview is expected for the iMessage product page.
  - fix: Use screenshots only for iMessage.
- **[META-92]** Have uploaded app previews finished processing (which can take up to 24 hours after upload)?
  - quote: "Processing time: Up to 24 hours after upload."
  - surface: asc
  - verify: In Media Manager confirm each preview shows as processed (not "Processing").
  - fix: Wait for processing to finish before submitting.

## META.AP.REQ App preview specifications — Requirements and video specifications

**Source text (verbatim):**
> The following are required to create your app preview and upload it to App Store Connect.
>
> | Context | Description |
> |---|---|
> | Maximum file size | 500MB |
> | Minimum length | 15 Seconds |
> | Maximum length | 30 Seconds |
> | Default poster frame setting | 5 Seconds (Visit Set an app preview poster frame.) |
> | Orientation | Portrait or Landscape (Note: macOS and tvOS app previews accepted in landscape only.) |
> | OS device capture and play | iOS 8 or later |
> | Upload and playback on App Store Connect | Safari 8 and macOS 10.10 or later |
>
> Video specifications
>
> | | H.264 format | ProRes 422 (HQ only) format |
> |---|---|---|
> | Target bit rate | 10-12 Mbps | VBR ~220 Mbps |
> | Video characteristics | Progressive, up to High Profile Level 4.0 | Progressive, no external references |
> | Max frame rate | 30 frames per second | 30 frames per second |
> | Supported extensions | .mov, .m4v, .mp4 | .mov |

Note: Apple lists the Audio entries once per column; the first list is the H.264 format column, the second the ProRes 422 (HQ only) format column.
> Audio
> - Stereo
> - Codec: 256kbps AAC
> - Sample Rate: 44.1kHz or 48kHz
> - All tracks should be enabled
> - Stereo configuration:
> - 1 track with 2-channel stereo (1st channel L and 2nd channel R)
> - 2 tracks with 1-channel stereo (1st track L and 2nd track R)
>
> - Stereo
> - Codec: PCM or 256kbps AAC
> - Bit Depth (for PCM): 16-, 24-, or 32-bit
> - Sample Rate: 44.1 or 48kHz
> - All tracks should be enabled
> - Stereo configuration:
> - 1 track with 2-channel stereo (1st channel L and 2nd channel R)
> - 2 tracks with 1-channel stereo (1st track L and 2nd track R)

**Applies to:** Apps that upload app previews

- **[META-93]** Is each app preview file 500MB or smaller?
  - quote: "| Maximum file size | 500MB |"
  - surface: code
  - verify: `stat -f%z <file>` (macOS) on each local preview; fail if > 500 MB.
  - fix: Re-encode at the target bit rate.
- **[META-94]** Is each app preview between 15 and 30 seconds long?
  - quote: "| Minimum length | 15 Seconds |"
  - surface: code
  - verify: `ffprobe -v error -show_entries format=duration -of csv=p=0 <file>`; fail if < 15 or > 30.
  - fix: Trim or extend to 15–30 s.
- **[META-95]** Is the frame rate at most 30 frames per second?
  - quote: "| Max frame rate | 30 frames per second | 30 frames per second |"
  - surface: code
  - verify: ffprobe `r_frame_rate`/`avg_frame_rate` ≤ 30.
  - fix: Re-export at 30 fps.
- **[META-96]** For H.264 previews, is the video progressive, up to High Profile Level 4.0, at about 10–12 Mbps; for ProRes, ProRes 422 HQ progressive with no external references?
  - quote: "Progressive, up to High Profile Level 4.0"
  - surface: code
  - verify: ffprobe `profile`, `level` (≤ 40), `field_order` (progressive), `bit_rate`; for ProRes check `codec_name=prores` and profile HQ.
  - fix: Re-export with the specified profile/level/bit rate.
- **[META-97]** Does the audio meet the spec: stereo, 256kbps AAC (or PCM 16/24/32-bit for ProRes), 44.1 or 48 kHz, all tracks enabled, in one of the two stereo configurations?
  - quote: "All tracks should be enabled"
  - surface: code
  - verify: ffprobe audio streams: `codec_name` (aac/pcm_*), `bit_rate` ≈ 256000 for AAC, `sample_rate` 44100/48000, `channels`; either one 2-channel track or two 1-channel tracks (L then R); no disabled tracks.
  - fix: Re-export audio with these settings (add a silent stereo track if needed).

## META.AP.RES App preview specifications — Resolutions

**Source text (verbatim):**
> Device resolution is the screen resolution of the physical device itself. Accepted resolution is the resolution App Store Connect actually accepts for your app preview file — because most app previews are recorded via screen recording rather than rendered at native resolution, App Store Connect accepts a defined set of standard portrait or landscape resolutions per display size instead of requiring an exact per-device match. Use the accepted resolution — not the device resolution — when preparing your video file.
>
> **iPhone**
>
> **iPhone Duo**
> Device resolutions
> - 2034 × 1398 pixels
> - 2853 × 2007 pixels (19.5:9 aspect ratio)
> Accepted resolutions
> - 886 x 1920 pixels (portrait)
> - 1920 x 886 pixels (landscape)
>
> **iPhone with Dynamic Island (large display)**
> - iPhone Air
> - iPhone 18 Pro Max
> - iPhone 17 Pro Max
> - iPhone 16 Pro Max
> - iPhone 16 Plus
> - iPhone 15 Pro Max
> - iPhone 15 Plus
> - iPhone 14 Pro Max
> Device resolutions
> - 2736 x 1260 pixels
> - 2796 x 1290 pixels
> - 2868 x 1320 pixels (19.5:9 aspect ratio)
> Accepted resolutions
> - 886 x 1920 pixels (portrait)
> - 1920 x 886 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for iPhone with Face ID (large display) are used.
>
> **iPhone with Face ID (large display)**
> - iPhone 14 Plus
> - iPhone 13 Pro Max
> - iPhone 12 Pro Max
> - iPhone 11 Pro Max
> - iPhone 11
> - iPhone XS Max
> - iPhone XR
> Device resolutions
> - 2778 x 1284 pixels
> - 2688 x 1242 pixels (19.5:9 aspect ratio)
> Accepted resolutions
> - 886 x 1920 pixels (portrait)
> - 1920 x 886 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for iPhone with Dynamic Island (large display) are used.
>
> **iPhone with Dynamic Island (medium display)**
> - iPhone 18 Pro
> - iPhone 17 Pro
> - iPhone 17
> - iPhone 16 Pro
> - iPhone 16
> - iPhone 15 Pro
> - iPhone 15
> - iPhone 14 Pro
> Device resolutions
> - 2556 x 1179 pixels
> - 2622 x 1206 pixels (19.5:9 aspect ratio)
> Accepted resolutions
> - 886 x 1920 pixels (portrait)
> - 1920 x 886 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for iPhone with Face ID (large display) are used.
>
> **iPhone with Face ID (medium display)**
> - iPhone 17e
> - iPhone 16e
> - iPhone 14
> - iPhone 13 Pro
> - iPhone 13
> - iPhone 13 mini
> - iPhone 12 Pro
> - iPhone 12
> - iPhone 12 mini
> - iPhone 11 Pro
> - iPhone XS
> - iPhone X
> Device resolutions
> - 2532 x 1170 pixels
> - 2436 x 1125 pixels
> - 2340 x 1080 pixels (19.5:9 aspect ratio)
> Accepted resolutions
> - 886 x 1920 pixels (portrait)
> - 1920 x 886 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for iPhone with Dynamic Island (medium display) are used.
>
> **iPhone with Home Button (large display)**
> - iPhone 8 Plus
> - iPhone 7 Plus
> - iPhone 6S Plus
> - iPhone 6 Plus
> Device resolutions
> - (Rendered pixels) 2208 x 1242 pixels
> - (Physical pixels) 1920 x 1080 pixels (16:9 aspect ratio)
> Accepted resolutions
> - 1080 x 1920 pixels (portrait)
> - 1920 x 1080 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for iPhone with Face ID (medium display) are used.
>
> **iPhone with Home Button (medium display)**
> - iPhone SE (3rd generation, 2nd generation)
> - iPhone 8
> - iPhone 7
> - iPhone 6S
> - iPhone 6
> Device resolutions
> - 1334 x 750 pixels (16:9 aspect ratio)
> Accepted resolutions
> - 750 x 1334 pixels (portrait)
> - 1334 x 750 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for iPhone with Home Button (large display) are used.
>
> **iPhone with Home Button (4" display)**
> - iPhone SE (1st generation)
> - iPhone 5S
> - iPhone 5C
> - iPhone 5
> Device resolutions
> - 1136 x 640 pixels (16:9 aspect ratio)
> Accepted resolutions
> - 1080 x 1920 pixels (portrait)
> - 1920 x 1080 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for iPhone with Home Button (medium display) are used.
>
> **iPhone with Home Button (3.5" display)**
> - App previews aren't supported
>
> **iPad**
>
> **13" display**
> - iPad Pro (M5, M4)
> - iPad Pro (6th generation, 5th generation, 4th generation, 3rd generation, 1st generation)
> - iPad Air (M4, M3, M2)
> Device resolutions
> - 2752 x 2064 pixels
> - 2732 x 2048 pixels (4:3 aspect ratio)
> Accepted resolutions
> - 1200 x 1600 pixels (portrait)
> - 1600 x 1200 pixels (landscape)
>
> **12.9" display**
> - iPad Pro (2nd generation)
> Device resolutions
> - 2732 x 2048 pixels (4:3 aspect ratio)
> Accepted resolutions
> - 1200 x 1600 pixels (portrait)
> - 1600 x 1200 pixels (landscape)
> - 900 x 1200 pixels (portrait)
> - 1200 x 900 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for 13" displays are used.
>
> **11" display**
> - iPad Pro (M5, M4)
> - iPad Pro (4th generation, 3rd generation, 2nd generation, 1st generation)
> - iPad Air (M4, M3, M2)
> - iPad Air (5th generation, 4th generation)
> - iPad (A16)
> - iPad (10th generation)
> - iPad mini (A17 Pro)
> - iPad mini (6th generation)
> Device resolutions
> - 2266 x 1488 pixels
> - 2420 x 1668 pixels
> - 2388 x 1668 pixels
> - 2360 x 1640 pixels (4.3:3 aspect ratio)
> Accepted resolutions
> - 1200 x 1600 pixels (portrait)
> - 1600 x 1200 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for 13" displays are used.
>
> **10.5" display**
> - iPad Pro
> - iPad Air (3rd generation)
> - iPad (9th generation, 8th generation, 7th generation)
> Device resolutions
> - 2224 x 1668 pixels (4:3 aspect ratio)
> Accepted resolutions
> - 1200 x 1600 pixels (portrait)
> - 1600 x 1200 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for 12.9" displays are used.
>
> **9.7" display**
> - iPad Pro
> - iPad Air
> - iPad Air 2
> - iPad
> - iPad 2
> - iPad (6th generation, 5th generation, 4th generation, 3rd generation)
> - iPad mini (5th generation)
> - iPad mini 4
> - iPad mini 3
> - iPad mini 2
> Device resolutions
> - 2048 x 1536 pixels
> - 1024 x 768 pixels (4:3 aspect ratio)
> Accepted resolutions
> - 900 x 1200 pixels (portrait)
> - 1200 x 900 pixels (landscape)
> Note
> - If app previews with the accepted resolutions aren't provided, scaled app previews for 10.5" displays are used.
>
> **Mac**
> Device resolutions
> - 1920 x 1080 pixels (16:9 aspect ratio)
> Accepted resolutions
> - 1920 x 1080 pixels (landscape)
>
> **Apple TV**
> Device resolutions
> - 1920 x 1080 pixels (16:9 aspect ratio)
> Accepted resolutions
> - 1920 x 1080 pixels (landscape)
>
> **Apple Vision Pro**
> Device resolutions
> - 3840 x 2160 pixels (16:9 aspect ratio)
> Accepted resolutions
> - 3840 x 2160 pixels (landscape)

**Applies to:** Apps that upload app previews

- **[META-98]** Is each app preview file at an accepted resolution for its display slot (not the device resolution)?
  - quote: "Use the accepted resolution — not the device resolution — when preparing your video file."
  - surface: code
  - verify: ffprobe `width,height` for each local preview and match against the "Accepted resolutions" column for the intended slot (e.g. 886 x 1920 / 1920 x 886 for modern iPhones; 1200 x 1600 / 1600 x 1200 for 13" iPad).
  - fix: Re-export the video at the accepted resolution.
- **[META-99]** Is no app preview planned for the iPhone with Home Button (3.5" display) slot?
  - quote: "App previews aren't supported"
  - surface: asc
  - verify: Confirm no preview is expected for 3.5" display.
  - fix: Use screenshots only for that size.

## META.ASSETS Manage your App Store assets — upload, poster frames, guidelines

**Source text (verbatim):**
> You can manage your app previews and screenshots across three places in App Store Connect, each with different capabilities.
>
> Product Page Information (on the version page, Custom Product Pages, and Product Page Optimization): Upload assets, sort their order, set or remove their placement, browse existing assets from Asset Library, and set a poster frame, all scoped to the version, Custom Product Page, or Product Page Optimization treatment you're currently editing.
>
> Media Manager: Manage app preview and screenshot placements for each supported device size and localization. You can add assets from the Asset Library, reorder their display sequence, remove placements, and choose poster frames.
>
> Asset Library: Upload new assets, set a poster frame, and delete unapproved assets, independent of any app version.
>
> Your app previews and screenshots must meet Apple's guidelines and the App Review Guidelines(sections 2.3.3 and 2.3.4).
>
> Upload your previews and screenshots
>
> You upload your app previews and screenshots through the Product Page Information section on the version page or directly in Asset Library then submit them for review when your app has one of these statuses:
> - Prepare for Submission
> - Invalid Binary
> - Rejected
> - Metadata Rejected
> - Developer Rejected
>
> Follow the steps below to manage your screenshots and app previews. You can also manage them by selecting View All Sizes in Media Manager:
> - In Apps, select the app you want to view.
> - In the sidebar, select the app version under the platform you want to edit.
> - Note: To upload assets for other localizations, choose the language from the pop-up menu on the top right.
> - Under the Product Page Information section, click the App Previews and Screenshots tab.
> - Under Previews and Screenshots, select the device tab for the asset you want to upload.
> - Note: To upload the required screenshots for iMessage and watchOS apps, or to manage scaled app previews and screenshots for other device sizes, select View All Sizes in Media Manager on the right.
> - Click Upload or drag your screenshots and app preview into the appropriate well.
> - Note: You can also click Browse Assets to use approved, compatible images and videos from the Asset Library.
>
> Set an app preview poster frame
> - Click View All Sizes in Media Manager on the right.
> - Scroll to the device size where you want to edit the app preview.
> - Hold the pointer over the app preview and click Edit Poster Frame.
> - Select the new poster frame or restore the default frame.
> - Use the playback controls to navigate to the frame of the video you want to use for your poster frame.
> - To select the currently displayed frame of the video as your poster frame, click Set Poster Frame.
> - To save the poster frame, click Done.
>
> Note:
> - Poster frames can't be edited after assets have been approved.
> - You can also set your poster frame directly from the Product Page Information section by holding the pointer over the app preview and clicking Edit Poster Frame. The poster frame set applies to everywhere the asset is used.
>
> (Remove your previews and screenshots) After you remove a screenshot or app preview, it’s also removed for all other display sizes using scaled versions.
>
> Creative assets are optional and separate from your app's screenshots, app previews, In-App Purchase and Subscription images, and any promotional artwork requested by editorial teams.

**Applies to:** All apps with screenshots/app previews

- **[META-100]** Do the app previews and screenshots meet App Review Guidelines sections 2.3.3 and 2.3.4?
  - quote: "Your app previews and screenshots must meet Apple's guidelines and the App Review Guidelines(sections 2.3.3 and 2.3.4)."
  - surface: asc
  - verify: Review every screenshot and preview against the 2.3.3/2.3.4 checks in the guidelines reference.
  - fix: Replace non-compliant media.
- **[META-101]** For iMessage and watchOS apps, have the required screenshots been uploaded via View All Sizes in Media Manager?
  - quote: "To upload the required screenshots for iMessage and watchOS apps, or to manage scaled app previews and screenshots for other device sizes, select View All Sizes in Media Manager on the right."
  - surface: asc
  - verify: If the project has a Messages extension or watchOS target, open Media Manager and confirm iMessage/Apple Watch screenshot sets are populated.
  - fix: Upload the iMessage/watchOS screenshots in Media Manager.
- **[META-102]** Has each app preview’s poster frame been deliberately set before approval?
  - quote: "Poster frames can't be edited after assets have been approved."
  - surface: asc
  - verify: In Media Manager hover each preview > Edit Poster Frame; confirm the chosen frame is representative (default is 5 seconds).
  - fix: Set a representative poster frame before submitting.

## META.LOC.ADD Localize app information — adding and editing languages

**Source text (verbatim):**
> After adding an app to your account, you can add languages and localized metadata on the App Information page. Learn more about supported languages and localizable properties.
>
> For example, if you select English as the primary language for your app in App Store Connect, and it’s the only language you provide, your app metadata will appear in English in all App Store countries or regions. If you localize your app metadata in French, the French localization displays to users whose language setting is in French. The French localization also displays to users in countries or regions where the App Store supports French but not English. Users can search for your app using localized keywords in all countries or regions where the App Store supports French. If no localization matches a user's language setting, the next most relevant localization is used. In other countries or regions, your metadata displays in the primary language (English in this example).
>
> Languages on the App Information page in App Store Connect are part of your app's metadata. This differs from adding languages to your app in Xcode when you localize your binary. Learn about localizing your app binary.
>
> Important: You can manage languages only when the app status is editable.
>
> Add a language
>
> When you add a language to your app, screenshots and the properties for the new language default to those of the primary language, except for the description and keywords. When you add a localization from the platform version section, it’s automatically added to the shared metadata under App Information and to other platforms.
> - In Apps, select the app you want to view.
> - On the top right, click the primary language to display the language pop-up menu.
> - Scroll down the menu to Not Localized, hold the pointer over the language (and locale) you want to add, then click the add button (+) that appears to the right of the language.
> - Enter localized metadata—such as descriptions and keywords—for the platform, then click Save.
> - To enter information that is shared across platforms, click App information.
> - On the top right, click the primary language to display the language pop-up menu.
> - Hold the pointer over the language (and locale) you want to add, then click the add button (+) that appears.
> - Enter the app name and privacy policy URL for the language or locale, then on the top right, click Save.
>
> Delete a language
>
> When you delete a language, countries or regions that display app information in that language revert to showing the information entered for the primary language.
>
> (Creating your product page — Localization) If your app is available in multiple languages, make sure to localize your app description, keywords, app previews, and screenshots, for each of the markets in which you offer your app. You can also translate your app’s name and tailor your keywords to reflect the values of each market so your app might better resonate with the local audience.

**Applies to:** Apps with more than one App Store localization

- **[META-103]** Does every added App Store localization have its own Description and Keywords entered (they are not copied from the primary language)?
  - quote: "When you add a language to your app, screenshots and the properties for the new language default to those of the primary language, except for the description and keywords."
  - surface: asc
  - verify: For each language in the version page pop-up, confirm Description and Keywords are non-empty and in that language.
  - fix: Enter localized description and keywords and Save.
- **[META-104]** Does each App Information localization have the app name and privacy policy URL entered?
  - quote: "Enter the app name and privacy policy URL for the language or locale, then on the top right, click Save."
  - surface: asc
  - verify: In App Information, switch each language and confirm Name and Privacy Policy URL are filled.
  - fix: Enter them per language and Save.
- **[META-105]** If the app binary is localized into languages that the App Store supports, is there a matching App Store localization with translated description, keywords, screenshots, and app previews?
  - quote: "If your app is available in multiple languages, make sure to localize your app description, keywords, app previews, and screenshots, for each of the markets in which you offer your app."
  - surface: code
  - verify: List the binary’s localizations (`knownRegions` in project.pbxproj, `*.lproj` folders, `Localizable.xcstrings` languages). Compare with the languages in the ASC pop-up (and the list in META.LOC.LIST).
  - fix: Add the missing App Store localizations and their metadata/screenshots (or drop the binary localization).
- **[META-106]** Do localized screenshots actually show the app in that language (rather than defaulting to primary-language screenshots) where the developer intends localized media?
  - quote: "screenshots and the properties for the new language default to those of the primary language"
  - surface: asc
  - verify: Per language in Media Manager, check whether screenshots are inherited from the primary language; compare text in images with the localization.
  - fix: Capture screenshots with the app running in that language and upload them for that localization.

## META.LOC.PRIMARY Localize app information — Change the primary language

**Source text (verbatim):**
> You can change the primary language for an app. For a language to be selectable as the primary language:
> - You must have already added the language to a previous version.
> - App Review must approve the new language. If the language hasn’t been approved, submit a version with this localized metadata for approval. Then, select it as your primary language in a subsequent update.
> - You must have already uploaded and received App Review approval for screenshots in the language for all supported platforms. The screenshot sizes for this language must match those of your current primary language. If this localization's screenshots were previously derived from another localization, you must first manually upload new screenshots that match your current primary language's sizes and submit a version for approval. Then, change the primary language on a subsequent update. Learn more about adding screenshots and previews.
>
> Note: If your app has a custom product page configured, you must also have uploaded screenshots in the language for each custom product page.
> - In Apps, select the app you want to view.
> - In the sidebar, click App Information.
> - In the Primary Language pop-up menu, choose the new primary language.
> - On the top right, click Save.

**Applies to:** Apps changing their primary language

- **[META-107]** If the primary language is being changed, was the new language already added and approved in a previous version, with approved screenshots for all supported platforms at the same sizes as the current primary language (and for each custom product page)?
  - quote: "You must have already uploaded and received App Review approval for screenshots in the language for all supported platforms."
  - surface: asc
  - verify: Check version history for an approved version containing the language; in Media Manager confirm that language’s screenshots are uploaded (not derived) and sizes match the current primary language; check each custom product page.
  - fix: Submit a version with the localized metadata and screenshots first; change the primary language in a subsequent update.

## META.LOC.LIST App Store localizations — Supported languages and storefront defaults

**Source text (verbatim):**
> Your app’s metadata appears to the customers, and you can localize it in the following languages and locales:
>
> Arabic, Bangla, Catalan, Chinese (Simplified), Chinese (Traditional), Croatian, Czech, Danish, Dutch, English (Australia), English (Canada), English (U.K.), English (U.S.), Finnish, French, French (Canada), German, Greek, Gujarati, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Kannada, Korean, Malay, Malayalam, Marathi, Norwegian, Odia, Polish, Portuguese (Brazil), Portuguese (Portugal), Punjabi, Romanian, Russian, Slovak, Slovenia, Spanish (Mexico), Spanish (Spain), Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese.
>
> When adding more than one language or locales for your app’s metadata in App Store Connect, keep in mind the language shown to each customer could be impacted by factors like the App Store language for their location, their device’s language settings, languages you’ve added, and your primary language in App Store Connect.
>
> Note: The language displayed to users may vary based on their device and system settings.
>
> | ISO code | Country or region | Default language | Additional supported language(s) |
> | --- | --- | --- | --- |
> | AFG | Afghanistan | English (U.K.) |  |
> | ALB | Albania | English (U.K.) |  |
> | DZA | Algeria | English (U.K.) | Arabic, French |
> | AGO | Angola | English (U.K.) |  |
> | AIA | Anguilla | English (U.K.) |  |
> | ATG | Antigua and Barbuda | English (U.K.) |  |
> | ARG | Argentina | Spanish (Mexico) | English (U.K.) |
> | ARM | Armenia | English (U.K.) |  |
> | AUS | Australia | English (Australia) | English (U.K.) |  |
> | AUT | Austria | German | English (U.K.) |
> | AZE | Azerbaijan | English (U.K.) |  |
> | BHS | Bahamas | English (U.K.) |  |
> | BHR | Bahrain | English (U.K.) | Arabic |  |
> | BRB | Barbados | English (U.K.) |  |
> | BLR | Belarus | English (U.K.) |  |
> | BEL | Belgium | English (U.K.) | Dutch, French |
> | BLZ | Belize | English (U.K.) | Spanish (Mexico) |
> | BEN | Benin | English (U.K.) | French |
> | BMU | Bermuda | English (U.K.) |  |
> | BTN | Bhutan | English (U.K.) |  |
> | BOL | Bolivia | Spanish (Mexico) | English (U.K.) |
> | BIH | Bosnia and Herzegovina | English (U.K.) | Croatian |
> | BWA | Botswana | English (U.K.) |  |
> | BRA | Brazil | Portuguese (Brazil) | English (U.K.) |
> | VGB | British Virgin Islands | English (U.K.) |  |
> | BRN | Brunei | English (U.K.) |  |
> | BGR | Bulgaria | English (U.K.) |  |
> | BFA | Burkina Faso | English (U.K.) | French |
> | KHM | Cambodia | English (U.K.) | French |
> | CMR | Cameroon | French | English (U.K.) |
> | CAN | Canada | English (Canada) | French (Canada) |
> | CPV | Cape Verde | English (U.K.) |  |
> | CYM | Cayman Islands | English (U.K.) |  |
> | TCD | Chad | English (U.K.) | French |
> | CHL | Chile | Spanish (Mexico) | English (U.K.) |
> | CHN | China mainland | Simplified Chinese | English (U.K.) |
> | COL | Colombia | Spanish (Mexico) | English (U.K.) |
> | COD | Congo, Democratic Republic of the | English (U.K.) | French |
> | COG | Congo, Republic of the | English (U.K.) | French |
> | CRI | Costa Rica | Spanish (Mexico) | English (U.K.) |
> | CIV | Cote d’Ivoire | French | English (U.K.) |
> | HRV | Croatia | English (U.K.) | Croatian |
> | CYP | Cyprus | English (U.K.) | Greek, Turkish |
> | CZE | Czechia | English (U.K.) | Czech |
> | DNK | Denmark | English (U.K.) | Danish |
> | DMA | Dominica | English (U.K.) |  |
> | DOM | Dominican Republic | Spanish (Mexico) | English (U.K.) |
> | ECU | Ecuador | Spanish (Mexico) | English (U.K.) |
> | EGY | Egypt | English (U.K.) | Arabic, French |
> | SLV | El Salvador | Spanish (Mexico) | English (U.K.) |
> | EST | Estonia | English (U.K.) |  |
> | SWZ | Eswatini | English (U.K.) |  |
> | FJI | Fiji | English (U.K.) |  |
> | FIN | Finland | English (U.K.) | Finnish |
> | FRA | France | French | English (U.K.) |
> | GAB | Gabon | French | English (U.K.) |
> | GMB | Gambia | English (U.K.) |  |
> | GEO | Georgia | English (U.K.) |  |
> | DEU | Germany | German | English (U.K.) |
> | GHA | Ghana | English (U.K.) |  |
> | GRC | Greece | English (U.K.) | Greek |
> | GRD | Grenada | English (U.K.) |  |
> | GTM | Guatemala | Spanish (Mexico) | English (U.K.) |
> | GNB | Guinea-Bissau | English (U.K.) | French |
> | GUY | Guyana | English (U.K.) | French |
> | HND | Honduras | Spanish (Mexico) | English (U.K.) |
> | HKG | Hong Kong | Chinese (Traditional) | English (U.K.) |
> | HUN | Hungary | English (U.K.) | Hungarian |
> | ISL | Iceland | English (U.K.) |  |
> | IND | India | English (U.K.) | Bangla, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Urdu |
> | IDN | Indonesia | English (U.K.) | Indonesian |
> | IRQ | Iraq | English (U.K.) | Arabic |
> | IRL | Ireland | English (U.K.) |  |
> | ISR | Israel | English (U.K.) | Hebrew |
> | ITA | Italy | Italian | English (U.K.) |
> | JAM | Jamaica | English (U.K.) |  |
> | JPN | Japan | Japanese | English (US) |
> | JOR | Jordan | English (U.K.) | Arabic |
> | KAZ | Kazakhstan | English (U.K.) |  |
> | KEN | Kenya | English (U.K.) |  |
> | XKS | Kosovo | English (U.K.) |  |
> | KWT | Kuwait | English (U.K.) | Arabic |
> | KGZ | Kyrgyzstan | English (U.K.) |  |
> | LAO | Laos | English (U.K.) | French |
> | LVA | Latvia | English (U.K.) |  |
> | LBN | Lebanon | English (U.K.) | Arabic, French |
> | LBR | Liberia | English (U.K.) |  |
> | LBY | Libya | English (U.K.) | Arabic |
> | LTU | Lithuania | English (U.K.) |  |
> | LUX | Luxembourg | English (U.K.) | French, German |
> | MAC | Macau | Chinese (Traditional) | English (U.K.) |
> | MDG | Madagascar | English (U.K.) | French |
> | MWI | Malawi | English (U.K.) |  |
> | MYS | Malaysia | English (U.K.) | Malay |
> | MDV | Maldives | English (U.K.) |  |
> | MLI | Mali | English (U.K.) | French |
> | MLT | Malta | English (U.K.) |  |
> | MRT | Mauritania | English (U.K.) | Arabic, French |
> | MUS | Mauritius | English (U.K.) | French |
> | MEX | Mexico | Spanish (Mexico) | English (U.K.) |
> | FSM | Micronesia | English (U.K.) |  |
> | MDA | Moldova | English (U.K.) |  |
> | MNG | Mongolia | English (U.K.) |  |
> | MNE | Montenegro | English (U.K.) | Croatian |
> | MSR | Montserrat | English (U.K.) |  |
> | MAR | Morocco | English (U.K.) | Arabic, French |
> | MOZ | Mozambique | English (U.K.) |  |
> | MMR | Myanmar | English (U.K.) |  |
> | NAM | Namibia | English (U.K.) |  |
> | NRU | Nauru | English (U.K.) |  |
> | NPL | Nepal | English (U.K.) |  |
> | NLD | Netherlands | Dutch | English (U.K.) |
> | NZL | New Zealand | English (Australia) | English (U.K.) |
> | NIC | Nicaragua | Spanish (Mexico) | English (U.K.) |
> | NER | Niger | English (U.K.) | French |
> | NGA | Nigeria | English (U.K.) |  |
> | MKD | North Macedonia | English (U.K.) |  |
> | NOR | Norway | English (U.K.) | Norwegian |
> | OMN | Oman | English (U.K.) | Arabic |
> | PAK | Pakistan | English (U.K.) | Urdu |
> | PLW | Palau | English (U.K.) |  |
> | PAN | Panama | Spanish (Mexico) | English (U.K.) |
> | PNG | Papua New Guinea | English (U.K.) |  |
> | PRY | Paraguay | Spanish (Mexico) | English (U.K.) |
> | PER | Peru | Spanish (Mexico) | English (U.K.) |
> | PHL | Philippines | English (U.K.) |  |
> | POL | Poland | English (U.K.) | Polish |
> | PRT | Portugal | Portuguese (Portugal) | English (U.K.) |
> | QAT | Qatar | English (U.K.) | Arabic |
> | KOR | Republic of Korea | Korean | English (U.K.) |
> | ROU | Romania | English (U.K.) | Romanian |
> | RUS | Russia | Russian | English (U.K.), Ukrainian |
> | RWA | Rwanda | English (U.K.) | French |
> | STP | Sao Tome and Principe | English (U.K.) |  |
> | SAU | Saudi Arabia | English (U.K.) | Arabic |
> | SEN | Senegal | English (U.K.) | French |
> | SRB | Serbia | English (U.K.) | Croatian |
> | SYC | Seychelles | English (U.K.) | French |
> | SLE | Sierra Leone | English (U.K.) |  |
> | SGP | Singapore | English (U.K.) | Chinese (Simplified) |
> | SVK | Slovakia | English (U.K.) | Slovak |
> | SVN | Slovenia | English (U.K.) | Slovenian |
> | SLB | Solomon Islands | English (U.K.) |  |
> | ZAF | South Africa | English (U.K.) |  |
> | ESP | Spain | Spanish (Spain) | Catalan, English (U.K.) |
> | LKA | Sri Lanka | English (U.K.) |  |
> | KNA | St. Kitts and Nevis | English (U.K.) |  |
> | LCA | St. Lucia | English (U.K.) |  |
> | VCT | St. Vincent and the Grenadines | English (U.K.) |  |
> | SUR | Suriname | English (U.K.) | Dutch |
> | SWE | Sweden | Swedish | English (U.K.) |
> | CHE | Switzerland | German | English (U.K.), French, Italian |
> | TWN | Taiwan | Chinese (Traditional) | English (U.K.) |
> | TJK | Tajikistan | English (U.K.) |  |
> | TZA | Tanzania | English (U.K.) |  |
> | THA | Thailand | English (U.K.) | Thai |
> | TON | Tonga | English (U.K.) |  |
> | TTO | Trinidad and Tobago | English (U.K.) | French |
> | TUN | Tunisia | English (U.K.) | Arabic, French |
> | TUR | Türkiye | English (U.K.) | Turkish |
> | TKM | Turkmenistan | English (U.K.) |  |
> | TCA | Turks and Caicos Islands | English (U.K.) |  |
> | UGA | Uganda | English (U.K.) |  |
> | UKR | Ukraine | English (U.K.) | Russian, Ukrainian |
> | ARE | United Arab Emirates | English (U.K.) | Arabic |
> | GBR | United Kingdom | English (U.K.) |  |
> | USA | United States | English (US) | Arabic, Chinese (Simplified), Chinese (Traditional), French, Korean, Portuguese (Brazil), Russian, Spanish (Mexico), Vietnamese |
> | URY | Uruguay | English (U.K.) | Spanish (Mexico) |
> | UZB | Uzbekistan | English (U.K.) |  |
> | VUT | Vanuatu | English (U.K.) | French |
> | VEN | Venezuela | Spanish (Mexico) | English (U.K.) |
> | VNM | Vietnam | English (U.K.) | Vietnamese |
> | YEM | Yemen | English (U.K.) | Arabic |
> | ZMB | Zambia | English (U.K.) |  |
> | ZWE | Zimbabwe | English (U.K.) |  |

**Applies to:** All apps (choose localizations for the storefronts in Pricing and Availability)

- **[META-108]** For each storefront where the app is available, is its metadata provided in that storefront’s default language or a supported additional language (otherwise the primary language shows)?
  - quote: "the language shown to each customer could be impacted by factors like the App Store language for their location, their device’s language settings, languages you’ve added, and your primary language in App Store Connect"
  - surface: asc
  - verify: Read Pricing and Availability storefronts; map each to its Default language / Additional supported language(s) in the table; list storefronts for which none of the app’s ASC localizations match. Report as informational unless the developer targets that market.
  - fix: manual — requires developer decision/legal/business action (add localizations for target markets).
- **[META-109]** Are all App Store localizations chosen from Apple’s supported list (e.g. Hebrew localized metadata for Israel, where the default storefront language is English (U.K.))?
  - quote: "you can localize it in the following languages and locales"
  - surface: asc
  - verify: Compare languages in the ASC pop-up with the supported list; for a target market, check whether its language is a "Default language" or only an "Additional supported language(s)" there.
  - fix: Add the needed supported localizations.

## META.PP Creating your product page — marketing guidance with rejection-relevant rules

**Source text (verbatim):**
> Every element of your App Store product page has the power to drive downloads of your app. Learn how to help customers discover your app and engage them through thoughtfully crafted metadata on your product page and in search results. You can build and maintain your product page in App Store Connect or automate your workflow with the App Store Connect API.
>
> (Icon) Your app icon is one of the first elements of your app that users see, so it’s essential to make a strong first impression that communicates your app’s quality and purpose. Work with a graphic designer to create an icon that is simple and recognizable. Try testing different options to determine which icon is the most recognizable and meaningful to your target audience.
>
> To ensure the icon is legible in all sizes, avoid adding unnecessary visual details. For information about creating a beautiful and memorable icon, see the Human Interface Guidelines.
>
> (App previews) An app preview demonstrates the features, functionality, and UI of your app in a short video that users watch directly on the App Store. Previews can be up to 30 seconds long and use footage captured on the device to show the experience of using your app. You can feature up to three app previews on your App Store and Mac App Store product pages, and localize them for all available App Store languages.
>
> App previews autoplay with muted audio when users view your product page, so make sure the first few seconds of your video are visually compelling. App preview poster frames appear whenever videos do not autoplay.
>
> (In-app purchases) Users can view and start an in-app purchase from your product page. In-app purchases and subscriptions are shown in two separate sections on your product page, and you can showcase up to 20 total items across both of these sections. You can even choose the order in which to list them to help drive awareness for specific content. Each item has its own display name, promotional image, and description. In-app purchase names are limited to 35 characters and descriptions are limited to 55 characters, so be descriptive, accurate, and concise when highlighting their benefits.
>
> (Ratings and reviews) The SKStoreReviewController API lets you give users an easy way to provide feedback about your app. You can prompt for ratings up to three times in a 365-day period. Users will submit a rating through the standardized prompt, and can write and submit a review without leaving the app.
>
> (Categories) Categories on the App Store help users discover new apps to meet their needs. You can assign a primary and a secondary category to your app. The primary category is particularly important for discoverability, as it helps users find your app when browsing or filtering search results, and it determines in which tab your app appears on the App Store. Be sure to select the primary category that’s most relevant. Choosing categories that are not relevant to your app may cause your app to be rejected when submitted for review.

(Name, Subtitle, Screenshots, Description, Promotional text, Keywords, What’s New, and Localization sections of this page are quoted in the corresponding units above.)

**Applies to:** All apps

- **[META-110]** Are In-App Purchase display names at most 35 characters and descriptions at most 55 characters?
  - quote: "In-app purchase names are limited to 35 characters and descriptions are limited to 55 characters"
  - surface: asc
  - verify: Open Monetization > In-App Purchases / Subscriptions; for each product and localization, count characters of Display Name and Description.
  - fix: Shorten to ≤ 35 / ≤ 55 characters.
- **[META-111]** If the app prompts for ratings, does it use the SKStoreReviewController API, which allows prompting up to three times in a 365-day period?
  - quote: "You can prompt for ratings up to three times in a 365-day period."
  - surface: code
  - verify: grep for `SKStoreReviewController`, `requestReview`, `RequestReviewAction`, `AppStore.requestReview`; also grep for custom "Rate us"/star dialogs or links to `itms-apps://…?action=write-review` triggered automatically.
  - fix: Request ratings through the SKStoreReviewController API (see guideline 5.6.1 in the guidelines reference for custom-prompt rules).
- **[META-112]** Is the primary category the most relevant one for the app (irrelevant categories may cause rejection)?
  - quote: "Choosing categories that are not relevant to your app may cause your app to be rejected when submitted for review."
  - surface: asc
  - verify: Compare App Information > Category with the app’s main function (see META.CAT definitions).
  - fix: Select the most relevant primary category.
- **[META-113]** Do app previews last no more than 30 seconds and use footage captured on the device?
  - quote: "Previews can be up to 30 seconds long and use footage captured on the device to show the experience of using your app."
  - surface: code
  - verify: ffprobe duration ≤ 30 s; review footage for device-captured app UI.
  - fix: Trim and re-capture from the device/simulator.

## META.CAT Choosing a category

**Source text (verbatim):**
> You can assign two categories to your app — a primary and a secondary category. The primary category you select is important for your app’s discoverability on the App Store. This will be the category in which the app appears when people browse the App Store or filter search results, and it determines placement on the Apps tab or Games tab on the App Store for iPhone and iPad.
>
> For macOS apps, the primary category you select determines where your app appears when people browse or filter search results in the Mac App Store. It also determines your app's placement in the Categories tab on the Mac App Store in macOS 10.14 or later.
>
> Apps and games with Entertainment or Games selected as a primary or secondary category in App Store Connect will appear in the corresponding Time Allowance category. The Time Allowance category for Social Media works differently — it's based on whether your app or game offers social media capabilities, regardless of the app category selected in App Store Connect. To help determine this, the age rating questionnaire in App Store Connect includes questions about your app’s social media capabilities. Apps with these capabilities will display a new Social Media content descriptor on their App Store product page.
>
> Let’s say you have a photo-sharing social networking app. For the App Store, you could choose either Photo & Video or Social Networking as your primary category. To decide which category will best serve your app, consider the following:
> - Your app’s purpose. Your primary category should be the one that best describes the main function or subject matter of your app.
> - Where users naturally look for an app like yours. Understanding your audience will help you identify the category in which they will likely look for your app. Will they consider your app to be more of a social network app or a photography app?
> - Which categories contain the same type of apps as yours. Research how similar apps are categorized — users may already know to visit these categories to find this type of app.
>
> Make sure that the category you choose accurately reflects your app’s core experience. Choosing categories that are not appropriate for your app is against the App Review Guidelines.
>
> (Games) If your app is a game, you can choose up to two Games subcategories. Users can find your app by browsing the subcategories on the App Store and in the Games subcategory charts. If you don’t know which subcategory best suits your game, research the types of games in each one before making your selection.
>
> (Stickers) On the App Store for iMessage, you can assign your sticker pack app to a category called Stickers, or to another primary category that best describes your app. If you use the Stickers category, you can also select a Stickers subcategory. Standalone sticker pack apps are not displayed in categories on the App Store for iPhone and iPad — they are discoverable only in search results. Categories for iOS app with iMessage extensions are taken from the iOS app and are used on the App Store for iPhone, iPad, and iMessage. For more details, see iMessage Apps and Stickers.
>
> | Category | Definition | For example |
> |---|---|---|
> | Books | Apps that provide extensive interactivity for content that is traditionally offered in printed form. If you’re planning a more traditional reading experience, you may want to look at publishing an iBook instead. | stories, comics, eReaders, coffee table books, graphic novels. |
> | Business | Apps that assist with running a business or provide a means to collaborate, edit, or share content. | document management (PDFs, scanning, file viewing/editing), VoIP telephony, dictation, remote desktop, job search resources, customer resource management, collaboration, enterprise resource planning, point of sale. |
> | Developer Tools | Apps that provide tools for app development, management, and distribution. | coding, testing, debugging, workflow management, text and code editing. |
> | Education | Apps that provide an interactive learning experience on a specific skill or subject. | arithmetic, alphabet, writing, early learning and special education, solar system, vocabulary, colors, language learning, standardized test prep, geography, school portals, pet training, astronomy, crafts. |
> | Entertainment | Apps that are interactive and designed to entertain and inform the user, and which contain audio, visual, or other content. | television, movies, second screens, fan clubs, theatre, ringtones, voice manipulation, ticketing services, art creation. |
> | Finance | Apps that perform financial transactions or assist the user with business or personal financial matters. | personal financial management, mobile banking, investment, bill reminders, budgets, debt management, tax, small business finance, insurance. |
> | Food & Drink | Apps that provide recommendations, instruction, or critique related to the preparation, consumption, or review of food or beverages. | recipe collections, cooking guides, restaurant reviews, celebrity chefs/recipes, dietary & food allergy, alcohol reviews, brewery guides, international cuisine. |
> | Games | Apps that provide single or multiplayer interactive activities for entertainment purposes. | action, adventure, board, card, family, music, puzzle, racing, role playing, simulation, sports, strategy. |
> | Graphics & Design | Apps that provide tools for art, design, and graphics creation. | vector graphic design, image editing, drawing and illustration. |
> | Health & Fitness | Apps related to healthy living, including stress management, fitness, and recreational activities. | yoga, muscle diagrams, workout tracking, running, cycling, stress management, pregnancy, meditation, weight loss, pilates, acupuncture/acupressure, Eastern/Chinese medicine. |
> | Lifestyle | Apps relating to a general-interest subject matter or service. | real estate, crafts, hobbies, parenting, fashion, home improvement. |
> | Kids (iOS and iPadOS only) | Apps designed specifically for children ages 11 and under. Age-appropriate apps must be placed in one of three age bands based on their primary audience: 5 and under, 6–8, or 9–11. | age-appropriate games, interactive stories, educational materials, magazines. |
> | Magazines & Newspapers | Apps that offer auto-renewing subscriptions to magazine or newspaper content. Choose Magazines & Newspapers if you deliver content using an issue-based strategy or are producing interactive versions of a printed periodical. | newspapers, magazines, other recurring periodicals. |
> | Medical | Apps that are focused on medical education, information management, or health reference for patients or healthcare professionals. | skeletal, muscular, anatomy, medical record-keeping, diseases, symptom reference, companion devices (blood pressure, pulse, and so on), health tracking. |
> | Music | Apps that are for discovering, listening to, recording, performing, or composing music, and that are interactive in nature. | music creation, radio, education, sound editing, music discovery, composition, lyric writing, band and recording artists, music videos and concerts, concert ticketing. |
> | Navigation | Apps that provide information to help a user travel to a physical location. | driving assistance, walking assistance, topographical maps, maritime, pilot logs/assistance, oceanic tides, road atlas, fuel finders, public transit maps. |
> | News | Apps that provide information about current events or developments in areas of interest such as politics, entertainment, business, science, technology, and so on. Choose News if your app serves content via newsreader or digest format, or if your app is for a digital-first or broadcast-first media outlet with frequent content updates. | television, video, radio, or online news outlets or programs, RSS readers. |
> | Photo & Video | Apps that assist in capturing, editing, managing, storing, or sharing photos and videos. | capture, editing, special effects, sharing, imaging, printing, greeting card creation, manuals. |
> | Productivity | Apps that make a specific process or task more organized or efficient. | task management, calendar management, translation, note taking, printing, password management, cloud storage, email clients, flow chart generators, audio dictation, simulation, data viewing. |
> | Reference | Apps that assist the user in accessing or retrieving information. | atlas, dictionary, thesaurus, quotations, encyclopedia, general research, animals, law, religion, how-tos, politics. |
> | Safari Extensions | Apps that offer extensions to help enhance and customize the web browsing experience on Safari. | content bookmarkers, password managers, adblockers, savings finders. |
> | Shopping | Apps that support the purchase of consumer goods or materially enhance the shopping experience. | commerce, marketplace, coupon, product review, apps with Apple Pay. |
> | Social Networking | Apps that connect people by means of text, voice, photo, or video. Apps that contribute to community development. | interpersonal connections, text messaging, voice messaging, video communication, photo & video sharing, dating, blogs, special interest communities, companion apps for traditional social networking services. |
> | Sports | Apps related to professional, amateur, collegiate, or recreational sporting activities. | fantasy sports companions, college teams/conference, professional teams/leagues, athletes, score trackers, instruction, sports news. |
> | Travel | Apps that assist the user with any aspect of travel, such as planning, purchasing, or tracking. | flight tracking, multi-time clocks, city guides, hotel/rental car/air fare shopping, vacation planning, public transportation, travel rewards. |
> | Utilities | Apps that enable the user to solve a problem or complete a specific task. | calculators (standard, tip, financial), clocks, measurement, time, web browsing, flashlights, screen locks, barcode scanners, unit conversion tools, password management, remote controls. |
> | Weather | Apps that provide forecasts, alerts, and information related to weather conditions. | radar, forecast, storms, tides, severe weather, local weather. |

**Applies to:** All apps

- **[META-114]** Does the selected primary category accurately reflect the app’s core experience, per Apple’s category definitions?
  - quote: "Make sure that the category you choose accurately reflects your app’s core experience. Choosing categories that are not appropriate for your app is against the App Review Guidelines."
  - surface: code
  - verify: Summarize the app’s main function from code (root views, main features, frameworks such as HealthKit, MapKit, StoreKit) and match it to the definitions table; compare with ASC App Information > Category.
  - fix: Change the primary (and secondary) category to the best match.
- **[META-115]** If the app offers social media capabilities, are the age rating questionnaire’s social media questions answered accordingly?
  - quote: "the age rating questionnaire in App Store Connect includes questions about your app’s social media capabilities"
  - surface: code
  - verify: grep for user-generated content/feeds/messaging/follow features; compare with the age rating answers in App Information.
  - fix: Update the age rating questionnaire answers.
- **[META-116]** If the Magazines & Newspapers category is chosen, does the app offer auto-renewing subscriptions to magazine or newspaper content?
  - quote: "Apps that offer auto-renewing subscriptions to magazine or newspaper content."
  - surface: code
  - verify: Check StoreKit products/configuration (`.storekit` file, `Product.SubscriptionInfo`) for auto-renewable subscriptions and periodical content.
  - fix: Choose another category (e.g. News or Books) if not.

## META.PREVIEWS.CONTENT Show more with app previews — content rules

**Source text (verbatim):**
> App previews demonstrate the features, functionality, and user interface of your app using footage captured on device. You can have up to three app previews for each language your app supports, and each preview can be up to 30 seconds long. App previews display and autoplay on your product page and within search results, and they can be used in Apple Ads.
>
> Like your App Store product page screenshots, app previews are device-specific. For technical specifications and details on how to submit app previews, see App Store Connect Help. Be sure to follow the App Review Guidelines when submitting your app previews. And get best practices for capturing app previews and screenshots of your visionOS app.
>
> Depict appropriate content. App previews must be appropriate for all ages, so they shouldn’t include objectionable content that includes violence, adult themes, or profanity. Show more gameplay than cutscenes so you don’t mislead your audience by giving a false impression of gameplay.
>
> Stay within the app. App previews must show only content within the app itself. Don’t film people interacting with a device, such as an over-the-shoulder angle or fingers tapping the screen.
>
> Include only authorized content. Show only material you have the legal right to display. If your app displays any protected content such as music, film, trademarked characters, brands, or other intellectual property assets, ensure you have the appropriate licensing rights for your marketing use in all territories.
>
> Use graphics and transitions. If you need to demonstrate how interaction or navigation works within your app, you may add graphic elements, such as touch hotspots. We recommend capturing the native UI resolution rather than zooming in on the view. Ensure that any transitions between scenes don’t imply functionality that your app doesn’t include. Aim to use straightforward transitions, like dissolves and fades.
>
> Add additional context with copy. By default, app previews play with the sound muted, so consider using copy to add additional context to your footage. Ensure text is legible, is easy to understand, and remains on the screen long enough for people to read. Avoid any seasonal or timely references that will age your video, such as “new for spring” or dates. Don’t include specific prices, as pricing and currencies vary across regions.
>
> Note if a purchase is required. If you display features that are only available through in-app purchase, or if your app uses a subscription model or requires login, you must disclose this. Disclaimer copy can be included within the footage or in the end frame.
>
> If you’d like, you can nod to augmented reality in short form in your app description: AR app or AR game. Only use AR to refer to apps that offer actual augmented reality functionality. You can also choose to mention AR in one of three other metadata fields: your app name, subtitle, or keywords.
>
> If someone has turned off video autoplay in their App Store settings, a poster frame will display. Select a visually compelling poster frame from your footage that conveys the essence of your app. If you change the poster frame on an app preview that’s already approved, you’ll need to submit a new version of your app preview.

**Applies to:** Apps with app previews (AR rule: apps mentioning AR in metadata)

- **[META-117]** Are app previews appropriate for all ages (no violence, adult themes, or profanity)?
  - quote: "App previews must be appropriate for all ages, so they shouldn’t include objectionable content that includes violence, adult themes, or profanity."
  - surface: asc
  - verify: Watch each preview in Media Manager; flag violence, adult themes, profanity.
  - fix: Re-edit the preview.
- **[META-118]** Do app previews show only content within the app (no people, hands, or over-the-shoulder device footage)?
  - quote: "App previews must show only content within the app itself. Don’t film people interacting with a device, such as an over-the-shoulder angle or fingers tapping the screen."
  - surface: asc
  - verify: Watch each preview; flag any real-world footage of people/devices.
  - fix: Replace with screen-captured footage.
- **[META-119]** Do previews show only material the developer has the legal right to display (music, film, trademarked characters, brands)?
  - quote: "Show only material you have the legal right to display."
  - surface: manual
  - verify: Ask for licences for any soundtrack, footage, or brand shown.
  - fix: manual — requires developer decision/legal/business action.
- **[META-120]** Do preview transitions avoid implying functionality the app doesn’t include, and does gameplay footage outweigh cutscenes?
  - quote: "Ensure that any transitions between scenes don’t imply functionality that your app doesn’t include."
  - surface: runtime
  - verify: Compare each feature shown in the preview with the current build in the simulator.
  - fix: Remove footage/effects that misrepresent the app.
- **[META-121]** Do previews avoid specific prices?
  - quote: "Don’t include specific prices, as pricing and currencies vary across regions."
  - surface: asc
  - verify: Watch previews for on-screen prices/currencies.
  - fix: Remove prices from the footage/copy.
- **[META-122]** If previewed features require an in-app purchase, a subscription, or a login, is that disclosed in the footage or end frame?
  - quote: "If you display features that are only available through in-app purchase, or if your app uses a subscription model or requires login, you must disclose this."
  - surface: asc
  - verify: Cross-reference features in the preview with StoreKit-gated code paths/login gates; check for disclaimer copy in the video.
  - fix: Add disclaimer copy within the footage or the end frame.
- **[META-123]** If “AR” appears in the name, subtitle, keywords, or description, does the app offer actual augmented reality functionality?
  - quote: "Only use AR to refer to apps that offer actual augmented reality functionality."
  - surface: code
  - verify: Search ASC Name/Subtitle/Keywords/Description for "AR"; grep the project for `ARKit`, `ARSession`, `RealityKit` AR anchors.
  - fix: Remove "AR" from metadata, or ship real AR features.

## META.ABP App Store asset best practices — content rules for images and videos

**Source text (verbatim):**
> To make sure your assets meet our policies, get familiar with the App Review Guidelines (particularly section 2.3 about Accurate Metadata) and the Apple Advertising Policies before you start creating.
>
> While you may depict content outside of your app or game in use, it must still relate to its general functionality. Keep your assets focused on things directly related to your app or game, to ensure people know what to expect before they download. This includes:
> - Don’t include specific pricing, discounts, website URLs, copyright symbols. This ensures your content remains relevant to a global audience and more evergreen.
> - Avoid claims that can’t be verified, such as awards or recognition that your app or game hasn’t actually received.
> - Don’t include logos or references to other platforms or marketplaces.
> - Please don’t include any Apple-designated recognitions — such as Editor’s Choice, App of the Day, Game of the Day, or Apple Design Award winner, as many of these already appear alongside your app or game in search results, as well as on your product page.
>
> Create for all ages. Choose imagery that’s appropriate and inclusive for people of all ages. Assets displayed on the App Store must meet a 4+ age rating, even if your app’s rating is higher and it’s intended for an older audience. Refrain from showing objectionable content, including explicit or harmful imagery, profanity, illegal drugs, self-harm, hate speech, stereotypes, sexually suggestive content, inflammatory religious commentary, or inaccurate and misleading quotations of religious texts.
>
> Focus on your core experience
>
> While you may depict content outside of your app or game in use, it must still relate to its general functionality.
>
> Keep violent content in check. Games that include violence may use action imagery, but must avoid depictions of gore, graphic imagery, or weapons that are pointed directly at a person or the audience.
>
> Be intentional with your text. Text can help people understand what they’re looking at, and you can use image overlays to demonstrate input mechanisms or highlight specific functionality. If using text, use a short phrase that enhances your visual rather than describes it. Be sure to localize for all languages your app supports.
>
> Screenshots are one of the most effective ways to communicate your app or game’s value on the App Store and show the user experience. You can have up to 10 screenshots on your product page. Depending on orientation, up to three screenshots can appear in search results.
> - Show what people can expect. Use screenshots to depict your app or game in use and give people a clear, detailed view into the experience. Stay focused on the core user experience — avoid using the entire asset to highlight general accolades or call-to-action statements.
>
> (Videos) Use audio mindfully. In most cases, audio is muted by default, so your creative must work silently first.
>
> - (In-App Events) Design for both aspect ratios. You need media for the event card (16:9 landscape) and the event details page (9:16 portrait). Ensure both communicate your event’s essence. Use similar colors or illustration styles for visual continuity.

**Applies to:** All apps (screenshots, app previews, creative assets)

- **[META-124]** Are screenshots/previews/creative assets free of specific pricing, discounts, website URLs, and copyright symbols?
  - quote: "Don’t include specific pricing, discounts, website URLs, copyright symbols."
  - surface: asc
  - verify: OCR or visually inspect each image/preview frame for prices, "% off", URLs, ©.
  - fix: Remove those elements and re-export.
- **[META-125]** Are assets free of unverifiable claims (awards or recognition the app hasn’t received) and of Apple-designated recognitions (Editor’s Choice, App of the Day, Game of the Day, Apple Design Award)?
  - quote: "Please don’t include any Apple-designated recognitions — such as Editor’s Choice, App of the Day, Game of the Day, or Apple Design Award winner"
  - surface: asc
  - verify: Inspect images/text overlays for award badges and claims; ask the developer to substantiate any non-Apple awards.
  - fix: Remove the badges/claims.
- **[META-126]** Are assets free of logos or references to other platforms or marketplaces?
  - quote: "Don’t include logos or references to other platforms or marketplaces."
  - surface: asc
  - verify: Inspect for logos of or references to other platforms or marketplaces (e.g. Google Play, Android, Windows).
  - fix: Remove them.
- **[META-127]** Do all assets meet a 4+ age rating even if the app is rated higher (no explicit/harmful imagery, profanity, illegal drugs, self-harm, hate speech, stereotypes, sexually suggestive content, inflammatory religious commentary)?
  - quote: "Assets displayed on the App Store must meet a 4+ age rating, even if your app’s rating is higher and it’s intended for an older audience."
  - surface: asc
  - verify: Inspect every screenshot, preview, and creative asset with a 4+ standard.
  - fix: Replace or censor offending imagery.
- **[META-128]** For games with violence, do assets avoid gore, graphic imagery, and weapons pointed directly at a person or the audience?
  - quote: "Games that include violence may use action imagery, but must avoid depictions of gore, graphic imagery, or weapons that are pointed directly at a person or the audience."
  - surface: asc
  - verify: Inspect game screenshots/previews for gore and weapons aimed at people or the camera.
  - fix: Choose different scenes/angles.
- **[META-129]** Is text in screenshots localized for all languages the app supports?
  - quote: "Be sure to localize for all languages your app supports."
  - surface: asc
  - verify: For each ASC localization, compare screenshot text with the localization language.
  - fix: Produce localized screenshot text for each language.
- **[META-136]** Does any content shown in assets that is outside the app or game in use still relate to the app’s general functionality?
  - quote: "While you may depict content outside of your app or game in use, it must still relate to its general functionality."
  - surface: asc
  - verify: Inspect each screenshot, preview, and creative asset; flag imagery unrelated to what the app does (compare with the app’s features in code and in the simulator).
  - fix: Replace unrelated imagery with content that reflects the app’s functionality.
- **[META-137]** Do screenshots depict the app or game in use rather than using the entire image for general accolades or call-to-action statements?
  - quote: "Stay focused on the core user experience — avoid using the entire asset to highlight general accolades or call-to-action statements."
  - surface: asc
  - verify: Flag screenshots that contain no app UI (only text, badges, or calls to action).
  - fix: Replace them with screenshots showing the app in use.
- **[META-138]** Do video creative assets and app previews work without sound (audio is muted by default in most cases)?
  - quote: "In most cases, audio is muted by default, so your creative must work silently first."
  - surface: asc
  - verify: Watch each video asset with sound off; flag videos whose meaning depends on narration or audio.
  - fix: Add on-screen copy or visuals so the video makes sense muted.
- **[META-139]** If the app uses In-App Events creative, is media provided for both the event card (16:9 landscape) and the event details page (9:16 portrait)?
  - quote: "You need media for the event card (16:9 landscape) and the event details page (9:16 portrait)."
  - surface: asc
  - verify: For each In-App Event in ASC, confirm event card media is 16:9 landscape and event details page media is 9:16 portrait.
  - fix: Produce and upload media in both aspect ratios.

## META.ADDAPP Add a new app — app record prerequisites

**Source text (verbatim):**
> Before uploading a build of your app to App Store Connect, first create an app record in your App Store Connect account.
>
> If you want to offer an app with multiple platforms as a single purchase, create it as a single record in App Store Connect. All platforms will share the same bundle ID, but you'll add platform-specific information separately.
>
> Note: You can't add an app to your account until the Account Holder signs the latest agreement in the Business section.
>
> Required role: Account Holder, App Manager, or Admin. View role permissions.
>
> Note: Watch-only apps are considered part of the iOS platform in App Store Connect.
>
> - Click Create, and check for messages indicating any missing information.
>
> After creating an App Store Connect record for an app, it appears in Apps, and its status is Prepare for Submission. You can select the app on this page to view and edit app information.

**Applies to:** All apps (app record); multi-platform single-purchase apps; Watch-only apps

Navigation path: "In Apps, click the add button (+) on the top left." > "In the pop-up menu, select New App."

- **[META-140]** Does an App Store Connect app record exist for the app before a build is uploaded?
  - quote: "Before uploading a build of your app to App Store Connect, first create an app record in your App Store Connect account."
  - surface: asc
  - verify: In Apps, find a record whose Bundle ID equals the project’s `PRODUCT_BUNDLE_IDENTIFIER`.
  - fix: Create the app record (Apps > + > New App) with the project’s bundle ID; requires Account Holder, App Manager, or Admin.
- **[META-141]** Has the Account Holder signed the latest agreement in the Business section?
  - quote: "Note: You can't add an app to your account until the Account Holder signs the latest agreement in the Business section."
  - surface: asc
  - verify: Open the Business section and confirm no unsigned latest agreement is pending.
  - fix: manual — requires developer decision/legal/business action (the Account Holder signs the agreement).
- **[META-142]** If the app is offered on multiple platforms as a single purchase, is it one app record whose platforms share the same bundle ID?
  - quote: "If you want to offer an app with multiple platforms as a single purchase, create it as a single record in App Store Connect. All platforms will share the same bundle ID, but you'll add platform-specific information separately."
  - surface: code
  - verify: Compare `PRODUCT_BUNDLE_IDENTIFIER` across the project’s platform targets meant for one purchase; in ASC confirm they appear as platforms of one app record.
  - fix: Add the platform to the existing record and use the shared bundle ID (manual if records already diverge).
- **[META-143]** For a Watch-only app, is it being managed under the iOS platform in App Store Connect?
  - quote: "Note: Watch-only apps are considered part of the iOS platform in App Store Connect."
  - surface: asc
  - verify: If the project has only a watchOS app (no iOS app target), confirm the ASC record has the iOS platform and the version/screenshots are set there.
  - fix: Manage the Watch-only app’s metadata under the iOS platform.

## META.SUBMIT Submit an app and Overview of submitting for review

**Source text (verbatim):**
> Before submitting an app version for review, provide required metadata and choose the build for the version.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
> - In Apps, select the app you want to view.
> - In the sidebar, click the app version you want to submit.
> - On the right, scroll down to the Build section and verify that you added the right build for the version.
> - On the top right, click “Add for Review,” and select whether to add the app version to an existing draft submission or create a new submission. The app status changes to Ready for Review. Your submission won’t be sent to App Review until you submit it for review in the next step.
>
> You can add items, such as In-App Events or Apple-hosted asset packs, to your submission. All items submitted together must be Accepted to complete the submission.
>
> To review the items you've added, click Draft Submissions on the bottom right of the screen and select the submission. Alternatively, you can go to the App Review section in the sidebar.
> - Click Submit for Review. When the review process starts, the app status changes to In Review. Learn about the tasks you can do in these statuses.
>
> (Overview of submitting for review) App versions for each platform are submitted separately. The status of any app versions on one platform doesn’t influence the status of app versions on other platforms.
>
> - Each platform can have one app version submission under review at a time.
> - A platform can have a maximum of two submissions under review at a time: one that includes an app version and one that includes items, like In-App Events or custom product pages, without an app version.
>
> Items associated with different platforms can't be added to the same submission.
>
> In addition to an app version, you can add the following items to a submission to App Review:
> - Auto-renewable subscription, non-renewing subscriptions, and subscription groups
> - In-App Purchases
> - In-App Events
> - Custom product pages
> - Product page optimization tests
> - Apple-hosted asset packs
> - Game Center components, including new or modified leaderboards, leaderboard sets, achievements, challenges, and activities

**Applies to:** All app submissions

- **[META-130]** Is the right build selected in the version’s Build section?
  - quote: "On the right, scroll down to the Build section and verify that you added the right build for the version."
  - surface: asc
  - verify: On the version page, read the Build section: build version/number must equal the project’s `MARKETING_VERSION` / `CURRENT_PROJECT_VERSION` of the audited commit, and processing must be complete.
  - fix: Select (or upload) the correct build.
- **[META-131]** Are the items the developer intends to submit alongside this version (e.g. new In-App Purchases, subscriptions, In-App Events) added to the submission?
  - quote: "In addition to an app version, you can add the following items to a submission to App Review:"
  - surface: asc
  - verify: Open Draft Submissions (bottom right) or the App Review section; compare included items with products referenced in code (StoreKit product IDs in Swift / `.storekit`) that are not yet approved in ASC.
  - fix: Add the missing items to the draft submission before clicking Submit for Review.
- **[META-132]** Has the draft submission actually been submitted (status In Review), not just added (Ready for Review)?
  - quote: "Your submission won’t be sent to App Review until you submit it for review in the next step."
  - surface: asc
  - verify: Check the version status in the sidebar / App Review section after the developer finishes.
  - fix: Click Submit for Review (developer action — the audit agent does not press it).
- **[META-144]** Does the user who will submit have the Account Holder, Admin, or App Manager role?
  - quote: "Required role: Account Holder, Admin, or App Manager."
  - surface: asc
  - verify: In Users and Access, read the submitting user’s role (the Marketing role, which can edit app information per META-02, is not listed for submitting).
  - fix: manual — requires developer decision/legal/business action (an Account Holder or Admin grants the role, or a user with the role submits).
- **[META-145]** Is no other app version submission for the same platform already under review?
  - quote: "Each platform can have one app version submission under review at a time."
  - surface: asc
  - verify: Open the App Review section in the sidebar and list submissions under review for this platform; fail if one already includes an app version.
  - fix: Wait for the existing review to finish, or remove that submission, before submitting the new version.
- **[META-146]** Does the submission contain only items associated with one platform?
  - quote: "Items associated with different platforms can't be added to the same submission."
  - surface: asc
  - verify: Open the draft submission and confirm every item belongs to the platform selected for it.
  - fix: Move other-platform items into a separate submission.

## Sources

- https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information — "Platform version information"
- https://developer.apple.com/help/app-store-connect/reference/app-information/app-information — "App information"
- https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications — "Screenshot specifications" (reached from https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications via redirect)
- https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications — "App preview specifications" (reached from https://developer.apple.com/help/app-store-connect/reference/app-preview-specifications via redirect)
- https://developer.apple.com/app-store/product-page/ — "Creating your product page"
- https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information — "View and edit app information"
- https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app — "Add a new app"
- https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information — "Localize app information"
- https://developer.apple.com/help/app-store-connect/manage-app-information/manage-your-app-store-assets — "Manage your App Store assets"
- https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-localizations — "App Store localizations"
- https://developer.apple.com/help/app-store-connect/reference/app-information/required-localizable-and-editable-properties — "Required, localizable, and editable properties"
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app — "Submit an app"
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review — "Overview of submitting for review"
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/upload-a-geographic-coverage-file — "Upload a geographic coverage file"
- https://developer.apple.com/app-store/categories/ — "Choosing a category"
- https://developer.apple.com/app-store/app-previews/ — "Show more with app previews"
- https://developer.apple.com/app-store/asset-best-practices/ — "App Store asset best practices and resources"
