# App Review Help — submission, review process and guideline references
Source: https://developer.apple.com/help/app-review/  
Retrieved: 2026-10-30

## HELP.1 App Review Help

**Source page:** https://developer.apple.com/help/app-review/

**Source text (verbatim):**
> Apple reviews all submissions to confirm they're safe, secure, and reliable. This includes apps and app updates, as well as bundles, In-App Purchases, In-App Events, App Store metadata, and other content you submit for review. Learn more about how App Review works and how to prepare your app for submission.
>
> ## Get started
>
> Test your app on compatible devices
> How Apple device compatibility affects your app's distribution, how to test on physical devices with TestFlight, and when it makes sense to restrict availability.
> Provide information for a complete review
> How to use the Notes field in App Store Connect to give App Review the context and documentation it needs for a smooth review.
>
> ## Popular
>
> Track a submission's review status
> Where to check your submission's status in App Store Connect, what each status means, and why some reviews take longer.
> Contact App Review for help with a submission
> How to reply to App Review about an ongoing submission, and how to request a call with an Apple representative.
>
> ## Additional resources
>
> - App Review Guidelines
> - Apple Developer Program License Agreement
> - App Store Connect Help
> - Forums
> - Videos
> - Contact Us

**Applies to:** All apps

## HELP.2 Provide information for a complete review

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review

**Source text (verbatim):**
> Add everything App Review needs to complete its review in the App Review information section of App Store Connect, including:
>
> - General information about the app's concept, features, and intended audience
> - Demo account credentials for account-based features
> - Required documentation for regulated fields
>
> Submitting all required information and documentation up front can ensure a faster and more predictable review. Incomplete submissions will be rejected.

**Applies to:** All apps

- **[HELP-01]** Does the App Review Information section in App Store Connect include general information about the app's concept, features, and intended audience?
  - quote: "General information about the app's concept, features, and intended audience"
  - surface: asc
  - verify: App Store Connect > Apps > (app) > Distribution > (version being submitted) > App Review Information > Notes. Confirm the Notes describe the concept, the features and the intended audience.
  - fix: Add a short paragraph to App Review Information > Notes covering the app's concept, its main features, and who it is for.
- **[HELP-02]** If the app has account-based features, are demo account credentials entered in App Review Information?
  - quote: "Demo account credentials for account-based features"
  - surface: asc
  - verify: Look in the Xcode project for login/sign-up flows (e.g. `ASAuthorizationAppleIDProvider`, Firebase/Supabase/Auth0 auth calls, login views). If there are any, open App Store Connect > (version) > App Review Information and confirm "Sign-in required" is checked and the User name and Password fields are filled in.
  - fix: Create a dedicated review account and enter its credentials in App Review Information > Sign-In Information.
- **[HELP-03]** If the app operates in a regulated field, is the required documentation attached in App Review Information?
  - quote: "Required documentation for regulated fields"
  - surface: asc
  - verify: Find out whether the app is in a regulated field (see HELP.5). If it is, open App Store Connect > (version) > App Review Information > Attachment and confirm the documents are attached.
  - fix: manual — requires developer decision/legal/business action (get the documentation and attach it).

## HELP.3 Provide information about the app

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review

**Source text (verbatim):**
> Tell App Review about your app in general, covering who it's for and how it works:
>
> - New apps: Describe your app's concept and business model.
> - Updates: Describe what's changed, and where reviewers can find significant new content or features.
> - Purpose and audience: Describe the app's purpose and target audience.
> - Devices and OS versions tested: List the device models and operating systems you tested the app on before submitting.
> - External services and platforms: List the external services, tools, or platforms the app uses to deliver its core functionality (for example, data providers, authentication services, payment processors, or AI services).
> - Required hardware: Apps with required hardware must provide a video (not a screen recording) that shows your app running on a physical Apple device as it pairs and interacts with the hardware.
> - Regional differences: Describe any regional differences in the app's features or content, or confirm that the app functions consistently across all regions.

**Applies to:** All apps (the "New apps", "Updates" and "Required hardware" items apply only to those cases)

- **[HELP-04]** For a new app, do the review Notes describe the app's concept and business model?
  - quote: "New apps: Describe your app's concept and business model."
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information > Notes. Confirm there is a description of the concept and the business model (free, paid, subscription, ads, and so on).
  - fix: Add the app's concept and business model to the Notes.
- **[HELP-05]** For an update, do the Notes describe what changed and where reviewers can find significant new content or features?
  - quote: "Updates: Describe what's changed, and where reviewers can find significant new content or features."
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information > Notes. Compare against the changes since the last approved version (git log/diff between release tags) and confirm each significant new feature is listed with where to find it.
  - fix: List the changes in the Notes with the navigation path to each new feature.
- **[HELP-06]** Do the Notes describe the app's purpose and target audience?
  - quote: "Purpose and audience: Describe the app's purpose and target audience."
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information > Notes. Confirm both the purpose and the target audience are stated.
  - fix: Add a sentence on the purpose and one on the target audience.
- **[HELP-07]** Do the Notes list the device models and OS versions the app was tested on before submitting?
  - quote: "Devices and OS versions tested: List the device models and operating systems you tested the app on before submitting."
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information > Notes. Confirm there is a list of specific device models and OS versions.
  - fix: Add the tested devices and OS versions (for example "iPhone 15 Pro, iOS 18.x; iPad Air, iPadOS 18.x").
- **[HELP-08]** Do the Notes list the external services, tools, or platforms the app uses for its core functionality?
  - quote: "External services and platforms: List the external services, tools, or platforms the app uses to deliver its core functionality"
  - surface: asc
  - verify: Make an inventory from the Xcode project: `Package.resolved`, `Podfile.lock`, `Cartfile.resolved`, and network hosts in the source (`grep -rE "https?://" --include=*.swift`). Look for data providers, auth services, payment processors and AI services. Then confirm each one is named in App Review Information > Notes.
  - fix: Add a list of the external services (name and role) to the Notes.
- **[HELP-09]** If the app requires hardware, does the submission provide a video (not a screen recording) of the app on a physical Apple device pairing and interacting with that hardware?
  - quote: "Apps with required hardware must provide a video (not a screen recording) that shows your app running on a physical Apple device as it pairs and interacts with the hardware."
  - surface: asc
  - verify: Check the Xcode project for hardware accessories: `CoreBluetooth`, `ExternalAccessory`, `UISupportedExternalAccessoryProtocols` in Info.plist, `AccessorySetupKit`, Matter/HomeKit. If any are present, confirm App Store Connect > (version) > App Review Information > Attachment includes a camera-filmed video of the pairing and the interaction.
  - fix: Film the app on a physical device pairing with and using the hardware, then attach the video in App Review Information.
- **[HELP-10]** Do the Notes describe any regional differences in features or content, or confirm the app works the same in all regions?
  - quote: "Regional differences: Describe any regional differences in the app's features or content, or confirm that the app functions consistently across all regions."
  - surface: asc
  - verify: Search the code for region gating (`Locale.current.region`, `regionCode`, `Storefront.current`, `SKStorefront.countryCode`, server-side geo flags). Then confirm App Review Information > Notes either describes the differences or states that the app behaves the same in all regions.
  - fix: Add a regional-differences statement to the Notes.

## HELP.4 Provide demo accounts

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review

**Source text (verbatim):**
> Add up-to-date demo account login credentials:
>
> - Enter a username and password that work at the time of submission. Credentials that expire or change before your review starts may result in the submission being rejected.
> - If your app has multiple account types, such as administrative and general user accounts, use the Notes field to add additional credentials for each type.
> - If your app offers auto-renewable subscriptions, provide a demo account with an expired subscription to enable review of the entire purchase flow.
> - If your app requires an authentication code in addition to or instead of login credentials, include it in the Notes field in advance. Without it, a call may be required to continue the review. Calls are typically completed within three to five business days.

**Applies to:** Apps with account-based features (individual items apply to apps with multiple account types, auto-renewable subscriptions, or authentication codes)

- **[HELP-11]** Do the demo credentials work at the time of submission?
  - quote: "Enter a username and password that work at the time of submission."
  - surface: runtime
  - verify: On a clean install of the release build, sign in with the exact User name and Password from App Store Connect > (version) > App Review Information. Confirm sign-in succeeds and the account will not expire before review.
  - fix: Reset or recreate the demo account so it does not expire, and update the credentials in App Review Information.
- **[HELP-12]** If the app has multiple account types, does the Notes field contain credentials for each type?
  - quote: "use the Notes field to add additional credentials for each type."
  - surface: asc
  - verify: Look for roles in the code (admin/user/teacher/student enums, role checks). If there is more than one, confirm App Review Information > Notes has credentials for each role.
  - fix: Create a demo account for each account type and add them to the Notes.
- **[HELP-13]** If the app offers auto-renewable subscriptions, is a demo account with an expired subscription provided?
  - quote: "provide a demo account with an expired subscription to enable review of the entire purchase flow."
  - surface: asc
  - verify: Look for auto-renewable products in the code or config (`.storekit` files with `"type" : "RecurringSubscription"`, `Product.SubscriptionInfo`, `SubscriptionStoreView`) or in App Store Connect > Monetization > Subscriptions. If there are any, confirm the Notes give an account whose subscription has expired.
  - fix: Set up a demo account with an expired subscription and document it in the Notes.
- **[HELP-14]** If the app requires an authentication code (2FA/OTP/SMS), is that code (or how to get it) in the Notes field in advance?
  - quote: "If your app requires an authentication code in addition to or instead of login credentials, include it in the Notes field in advance."
  - surface: asc
  - verify: Search the code for OTP/2FA flows (`oneTimeCode` text content type, SMS verification, magic links). If present, confirm App Review Information > Notes includes a code that works for the demo account.
  - fix: Give the demo account a static code or a bypass, and put it in the Notes.

## HELP.5 Provide required documentation

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review

**Source text (verbatim):**
> Developers with apps operating in regulated fields must provide documentation demonstrating they are qualified and authorized to provide those services. If the app is available in multiple countries and regions, developers may need to provide additional documentation for each location where the app is distributed. Similarly, developers with apps containing protected content must show they have permission to include it in the app.
>
> Provide required documentation, which can vary by app type:
>
> - Medical apps that make diagnostic or treatment claims: Regulatory clearance for each country or region where the app is available, such as FDA, CE, or CFDA documentation, or a supporting test report or peer-reviewed study.
> - Cryptocurrency exchange apps: A cryptocurrency exchange license for each country or region where the app is available, plus partnership documentation if you're working with a third-party exchange.
> - Financial apps, including apps that offer loans: Documentation showing your partnership with the licensed financial institution or lender providing the underlying service.
> - Apps offering gambling, lotteries, or real-money gaming: The applicable gambling or lottery license for each storefront where your app is available.
> - Apps that use another party's intellectual property: Trademark or rights documentation, such as a signed contract, or email correspondence showing you have permission.
>
> If your app falls into one of these categories, attach everything App Review will need to complete its review in the App Review Information section before you submit.
>
> If you're unsure what information your app's review needs, consider requesting a one-on-one appointment to discuss your app's concept before you submit.
>
> ### Documentation examples by guideline
>
> App Review Guideline
>
> Documentation typically requested
>
> 1.4.1: Diagnosing or Treating Patients
>
> Regulatory clearance (FDA, CE, or CFDA documentation); a supporting test report or peer-reviewed study.
>
> 1.4.3: Cannabis, Alcohol, and Illegal Substances
>
> Cannabis dispensary license.
>
> 1.7: Reporting Criminal Activity
>
> Documentation confirming the developer's partnership with law enforcement or a government entity, printed on that entity's official letterhead.
>
> 2.1: Registration Verification
>
> International Standard Book Number (ISBN) or GRN documentation (China).
>
> 3.1.5: Cryptocurrencies
>
> Cryptocurrency exchange license; partnership documentation if you're leveraging a third-party exchange partner; legal opinion.
>
> 3.2.1: Financial Apps
>
> Documentation showing your partnership with the financial institution or bank providing the underlying service.
>
> 3.2.1 / 3.2.2: Apps Offering Loans
>
> Loan license; business license; partnership documentation demonstrating the formal agreement between you and a licensed lender.
>
> 4.1 / 5.2.1 / 5.2.3: Third-party trademarks, copycat concepts, fan apps, sports and sporting events, specific marks, audio/video/music, and apps that download or stream third-party content
>
> Trademark or rights documentation, such as a signed contract, electronic communication (emails, messaging-service screenshots), video recordings, or licensing documents.
>
> 5.0: Published Works for Sale in China
>
> Publication permit; Internet Publishing License; Internet Culture Operations Permit; Operating License of Publication; Radio and Television Program Production license, where applicable.
>
> 5.1.1: Verifying Seller and Company
>
> Partnership evidence, for example with an insurance company, brokerage, or applicable government body.
>
> 5.1.3: Health and Human Research
>
> Ethics Review Board or Institutional Review Board (IRB) approval; human research consent form.
>
> 5.3.3: Lotteries and Raffles
>
> Gambling license; SUSEP and SECAP documents (Brazil); lottery app license (China).
>
> 5.3.4: Gambling
>
> Gambling license.

**Applies to:** Apps operating in regulated fields, and apps containing protected content (each check names its category)

- **[HELP-15]** If the app operates in a regulated field, has the developer provided documentation showing they are qualified and authorized to provide those services (plus any additional documentation needed for each location where the app is distributed)?
  - quote: "Developers with apps operating in regulated fields must provide documentation demonstrating they are qualified and authorized to provide those services."
  - surface: asc
  - verify: Classify the app from its description and features (medical, crypto, finance/loans, gambling, legal, insurance and so on). Compare against App Store Connect > Pricing and Availability > Countries or Regions. Confirm App Review Information > Attachment has the qualification/authorization documentation, plus any additional documentation a distribution location requires.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-16]** If the app contains protected content, has the developer shown permission to include it?
  - quote: "developers with apps containing protected content must show they have permission to include it in the app."
  - surface: asc
  - verify: Inventory third-party content in the bundle (Assets.xcassets, audio and video files, fonts, bundled data) and in remote content sources. For any protected content, confirm proof of permission is attached in App Review Information.
  - fix: manual — requires developer decision/legal/business action (get the license, or remove the content).
- **[HELP-17]** If the app is a medical app that makes diagnostic or treatment claims (1.4.1), is regulatory clearance (e.g. FDA, CE, CFDA) or a supporting test report or peer-reviewed study attached for each country or region where it is available?
  - quote: "Medical apps that make diagnostic or treatment claims: Regulatory clearance for each country or region where the app is available"
  - surface: asc
  - verify: Search the App Store description, the in-app copy (`Localizable.xcstrings`) and the features for diagnostic or treatment claims. If there are any, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-18]** If the app is a cryptocurrency exchange app, is an exchange license attached for each country or region (plus partnership documentation if a third-party exchange is used)?
  - quote: "Cryptocurrency exchange apps: A cryptocurrency exchange license for each country or region where the app is available, plus partnership documentation if you're working with a third-party exchange."
  - surface: asc
  - verify: Find out whether the app offers crypto exchange features (search for exchange SDKs and trading APIs). If it does, check App Review Information > Attachment against the availability list in Pricing and Availability.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-19]** If the app is a financial app (including loans), is documentation of the partnership with the licensed financial institution or lender attached?
  - quote: "Financial apps, including apps that offer loans: Documentation showing your partnership with the licensed financial institution or lender providing the underlying service."
  - surface: asc
  - verify: Look for banking, lending or payment-provider integrations in the code and metadata. If any are found, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-20]** If the app offers gambling, lotteries, or real-money gaming (5.3.3 / 5.3.4), is the applicable gambling or lottery license attached for each storefront?
  - quote: "Apps offering gambling, lotteries, or real-money gaming: The applicable gambling or lottery license for each storefront where your app is available."
  - surface: asc
  - verify: Find out whether the app has real-money wagering. If it does, compare App Review Information > Attachment against Pricing and Availability > Countries or Regions.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-21]** If the app uses another party's intellectual property (4.1 / 5.2.1 / 5.2.3), is trademark or rights documentation attached?
  - quote: "Apps that use another party's intellectual property: Trademark or rights documentation, such as a signed contract, or email correspondence showing you have permission."
  - surface: asc
  - verify: Check the app name, icon, screenshots, description and bundled assets for third-party marks, characters, sports leagues, music or streamed content. If any are present, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-22]** If the app falls into any of these categories, was everything App Review needs attached in the App Review Information section before submitting?
  - quote: "attach everything App Review will need to complete its review in the App Review Information section before you submit."
  - surface: asc
  - verify: Before pressing Add for Review / Submit, open App Store Connect > (version) > App Review Information > Attachment and confirm every document identified in HELP-15 to HELP-31 is uploaded.
  - fix: Upload the missing documents to App Review Information > Attachment before submitting.
- **[HELP-23]** If the app falls under 1.4.3 (Cannabis, Alcohol, and Illegal Substances) and involves cannabis, is a cannabis dispensary license provided?
  - quote: "Cannabis dispensary license."
  - surface: asc
  - verify: Find out whether the app involves cannabis. If it does, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-24]** If the app falls under 1.7 (Reporting Criminal Activity), is documentation of the partnership with law enforcement or a government entity, on that entity's official letterhead, provided?
  - quote: "Documentation confirming the developer's partnership with law enforcement or a government entity, printed on that entity's official letterhead."
  - surface: asc
  - verify: Find out whether the app lets users report criminal activity. If it does, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-25]** If the app falls under 2.1 (Registration Verification), is ISBN or GRN documentation (China) provided?
  - quote: "International Standard Book Number (ISBN) or GRN documentation (China)."
  - surface: asc
  - verify: Find out whether the app falls under registration verification (for example published works that carry an ISBN, or GRN documentation for China). If it does, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-26]** If the app falls under 3.1.5 (Cryptocurrencies), are the exchange license, partnership documentation for any third-party exchange partner, and a legal opinion provided?
  - quote: "Cryptocurrency exchange license; partnership documentation if you're leveraging a third-party exchange partner; legal opinion."
  - surface: asc
  - verify: Find out whether the app has cryptocurrency features. If it does, check App Review Information > Attachment for all three items.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-27]** If the app offers loans (3.2.1 / 3.2.2), are the loan license, business license, and lender partnership documentation provided?
  - quote: "Loan license; business license; partnership documentation demonstrating the formal agreement between you and a licensed lender."
  - surface: asc
  - verify: Find out whether the app offers loans. If it does, check App Review Information > Attachment for all three items.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-28]** If the app sells published works in China (5.0), are the applicable permits and licenses provided?
  - quote: "Publication permit; Internet Publishing License; Internet Culture Operations Permit; Operating License of Publication; Radio and Television Program Production license, where applicable."
  - surface: asc
  - verify: Check Pricing and Availability for China mainland, and whether the app sells published works. If both apply, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-29]** If the app falls under 5.1.1 (Verifying Seller and Company), is partnership evidence (e.g. with an insurance company, brokerage, or government body) provided?
  - quote: "Partnership evidence, for example with an insurance company, brokerage, or applicable government body."
  - surface: asc
  - verify: Find out whether the app acts on behalf of an insurer, a brokerage or a government body. If it does, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-30]** If the app falls under 5.1.3 (Health and Human Research), are Ethics/Institutional Review Board approval and a human research consent form provided?
  - quote: "Ethics Review Board or Institutional Review Board (IRB) approval; human research consent form."
  - surface: asc
  - verify: Look for ResearchKit (`ORKConsentDocument`) or other study/consent flows in the code. If present, check App Review Information > Attachment.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-31]** If the app falls under 5.3.3 (Lotteries and Raffles), are the gambling license and region-specific documents (SUSEP and SECAP for Brazil; lottery app license for China) provided?
  - quote: "Gambling license; SUSEP and SECAP documents (Brazil); lottery app license (China)."
  - surface: asc
  - verify: Find out whether the app runs lotteries or raffles. If it does, compare App Review Information > Attachment against the storefronts in Pricing and Availability.
  - fix: manual — requires developer decision/legal/business action.

## HELP.6 Use a demonstration mode when appropriate

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review

**Source text (verbatim):**
> If your app handles sensitive user information, or operates in a highly regulated industry, you can implement a demonstration mode instead of providing a demo account. A demonstration mode should show your app's full features and functionality using demonstration data.
>
> Related Request a one-on-one App Review appointment Manage App Review information with the App Store Connect API Test your app on compatible devices

**Applies to:** Apps that handle sensitive user information or operate in a highly regulated industry and use a demonstration mode instead of a demo account

- **[HELP-32]** If a demonstration mode is used instead of a demo account, does it show the app's full features and functionality using demonstration data?
  - quote: "A demonstration mode should show your app's full features and functionality using demonstration data."
  - surface: runtime
  - verify: Turn on the demo mode exactly as the review Notes describe. Walk every primary feature and confirm each one works with demonstration data (no feature is greyed out or missing). In code, check that the demo-mode flag does not skip feature screens.
  - fix: Extend the demo mode so it covers every feature, and describe how to enter it in App Review Information > Notes.

## HELP.7 Configure In-App Purchases for review in the sandbox

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases

**Source text (verbatim):**
> App Review evaluates your In-App Purchases in the same sandbox environment you use for testing. The sandbox lets App Review use real product data and server-to-server transactions without incurring any financial charges. Configure and test In-App Purchases in this environment before you submit them to ensure your products function as expected during review.
>
> Note: In-App Purchases do not need prior approval from App Review to function in review.
>
> - The Account Holder must accept the Paid Apps Agreement in the Business section of App Store Connect, then confirm the agreement is in effect. Paid In-App Purchases won't function in review until this agreement is active.
> - Create a Sandbox Apple Account and configure product information in App Store Connect.
> - Fetch product information using StoreKit APIs before presenting In-App Purchases in your app's UI to ensure the displayed details match your configuration in App Store Connect.
> - Test your In-App Purchases in the sandbox before you submit. If one fails to display, follow TN3186: Troubleshooting In-App Purchases availability in the sandbox.
> - If you restrict In-App Purchases by storefront or device configuration, specify this in the Notes field in the App Review Information section of App Store Connect.
> - Submit the In-App Purchases in App Store Connect once they're in the Ready for Review state.
>
> Related Overview of testing in sandbox Testing In-App Purchases with sandbox Provide information for a complete review Test your app on compatible devices

**Applies to:** Apps that offer In-App Purchases

- **[HELP-33]** Has the Account Holder accepted the Paid Apps Agreement, and is it in effect?
  - quote: "The Account Holder must accept the Paid Apps Agreement in the Business section of App Store Connect, then confirm the agreement is in effect."
  - surface: asc
  - verify: App Store Connect > Business > Agreements. Confirm the Paid Apps Agreement status is Active (not pending, and with no missing tax or banking information).
  - fix: manual — requires developer decision/legal/business action (the Account Holder accepts the agreement and completes tax and banking).
- **[HELP-34]** Has a Sandbox Apple Account been created, and is product information configured in App Store Connect?
  - quote: "Create a Sandbox Apple Account and configure product information in App Store Connect."
  - surface: asc
  - verify: App Store Connect > Users and Access > Sandbox > Test Accounts: at least one exists. Monetization > In-App Purchases / Subscriptions: every product ID used in code exists with its product information configured.
  - fix: Create a sandbox tester and fill in the missing product metadata.
- **[HELP-35]** Does the app fetch product information with StoreKit APIs before presenting In-App Purchases in its UI (rather than hard-coding names or prices)?
  - quote: "Fetch product information using StoreKit APIs before presenting In-App Purchases in your app's UI"
  - surface: code
  - verify: grep the code for `Product.products(for:)`, `SKProductsRequest`, `ProductView`, `StoreView`, `SubscriptionStoreView`. Confirm paywall price and name labels come from `Product.displayPrice` / `displayName` (or `SKProduct.price` with `priceLocale`), not from string literals such as "$4.99".
  - fix: Load products with `Product.products(for:)` and show `displayName` / `displayPrice`. Do not show a purchase button until the product has loaded.
- **[HELP-36]** Were the In-App Purchases tested in the sandbox before submitting?
  - quote: "Test your In-App Purchases in the sandbox before you submit."
  - surface: runtime
  - verify: Install a TestFlight or development build on a device signed in with a Sandbox Apple Account. Confirm every product appears and can be bought. If one fails to display, follow TN3186.
  - fix: Fix product configuration or loading until every product appears and completes a purchase in the sandbox.
- **[HELP-37]** If In-App Purchases are restricted by storefront or device configuration, is this stated in the App Review Information Notes?
  - quote: "If you restrict In-App Purchases by storefront or device configuration, specify this in the Notes field in the App Review Information section of App Store Connect."
  - surface: asc
  - verify: Search the code for storefront or device gating around purchases (`Storefront.current`, `SKPaymentQueue.default().storefront`, `UIDevice` idiom checks before the paywall). If present, confirm App Review Information > Notes describes the restriction.
  - fix: Describe the restriction in the Notes.
- **[HELP-38]** Have the In-App Purchases been submitted in App Store Connect once they reached the Ready for Review state?
  - quote: "Submit the In-App Purchases in App Store Connect once they're in the Ready for Review state."
  - surface: asc
  - verify: App Store Connect > Monetization > In-App Purchases / Subscriptions: every product is Ready for Review (not Missing Metadata). On the version page, confirm the products are added to the submission under "In-App Purchases and Subscriptions".
  - fix: Complete the metadata until each product is Ready for Review, then add it to the submission.

## HELP.8 Test your app on compatible devices

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices

**Source text (verbatim):**
> App Review evaluates apps the way your users will use them: installed on real devices and connected to networks with real-world conditions. Users expect the app to function on all the devices where it's available. Make sure your pre-submission testing includes running the app on each device platform where it could be used, not just in simulated environments. It will also be easier to identify and resolve these issues early than if they were to occur during review.

**Applies to:** All apps

- **[HELP-39]** Has the app been tested on a real device for each device platform where it could be used, not just in simulators?
  - quote: "Make sure your pre-submission testing includes running the app on each device platform where it could be used, not just in simulated environments."
  - surface: manual
  - verify: Work out the platforms where the app can run: `TARGETED_DEVICE_FAMILY`, `SUPPORTED_PLATFORMS`, `SUPPORTS_MAC_DESIGNED_FOR_IPHONE_IPAD`, `SUPPORTS_XR_DESIGNED_FOR_IPHONE_IPAD` in the project.pbxproj, and the availability settings in App Store Connect > Pricing and Availability. Ask for, or record, a physical-device test on each platform.
  - fix: Run the release build on a physical device for each platform (directly or through TestFlight) and fix the issues found.

## HELP.9 Use TestFlight for beta testing

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices

**Source text (verbatim):**
> TestFlight makes it easy for testers to provide feedback after running your app on real devices:
>
> - Add up to 100 internal testers from your Apple Developer Program account.
> - Invite up to 10,000 external testers by email invitation or a public link.
>
> The first build you add to a group with external testers is sent to App Review to make sure it follows the App Review Guidelines. Later builds in the same group may not need a full review.

**Applies to:** Apps distributed through TestFlight

## HELP.10 Understand device compatibility

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices

**Source text (verbatim):**
> Apple platforms make it easy to distribute your app to a variety of compatible devices, so it's important to maximize your app experience on each platform you support. There are many ways an app built for one Apple device can run on other Apple devices:
>
> - Apps designed for iPhone can run on iPad in compatibility mode if there are no dependencies on iPhone device capabilities.
> - Compatible iPhone and iPad apps can run unmodified on Macs with Apple silicon.
> - Compatible iPhone and iPad apps can run unmodified on Apple Vision Pro.
>
> Xcode provides options to configure settings for apps on multiple platforms. You can specify which platforms your app's target supports in the Supported Destinations field.
>
> Note: People may still be able to run your app on a device even if you remove or don't include the device as a supported destination in Xcode. For example, as long as an app designed for iPhone doesn't depend on a capability that's only available on iPhone, it can be downloaded from the App Store onto iPad. Adding or removing iPad as a supported destination in Xcode won't change that app's availability on iPad.

**Applies to:** All apps

## HELP.11 Follow compatibility best practices

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices

**Source text (verbatim):**
> Plan and test for compatibility modes so your app works on every device on which it can be downloaded.
>
> #### Do
>
> - Use Xcode simulators to verify basic functionality across different device types.
> - Leverage TestFlight with external testers who have access to a wide range of Apple devices.
>
> #### Don't
>
> - Don't submit for review without testing your app's behavior in compatibility modes.
> - Don't assume removing a supported destination in Xcode prevents distribution to that device type.
>
> Build adaptive interfaces that work across device variations.
>
> #### Do
>
> - Build interfaces that respond to different screen sizes and orientations.
> - Adapt features based on available hardware, providing alternatives for a consistent experience.
>
> #### Don't
>
> - Don't design rigid interfaces that assume only one type of device or input method.
> - Don't let your app crash or become unusable when optional hardware is unavailable.

**Applies to:** All apps

- **[HELP-40]** Has the app's behavior been tested in compatibility modes (iPhone app on iPad, iPhone/iPad app on Apple silicon Mac, on Apple Vision Pro) wherever it can be downloaded?
  - quote: "Don't submit for review without testing your app's behavior in compatibility modes."
  - surface: runtime
  - verify: If `TARGETED_DEVICE_FAMILY = 1` (iPhone only), run the app on an iPad (or the iPad simulator) in compatibility mode. If the app is available on Mac or Vision Pro (App Store Connect > Pricing and Availability > "iPhone and iPad Apps on Apple Silicon Macs" / "Apple Vision Pro"), run it there too. Check launch, layout, primary flows and purchases.
  - fix: Fix the compatibility-mode issues found, or restrict availability where the source allows it (see HELP.12).
- **[HELP-41]** Does the developer avoid relying on removing a supported destination in Xcode to stop distribution to a device type?
  - quote: "Don't assume removing a supported destination in Xcode prevents distribution to that device type."
  - surface: code
  - verify: Compare the Xcode target's Supported Destinations (General tab, `SUPPORTED_PLATFORMS` / `TARGETED_DEVICE_FAMILY`) with the devices the app can actually be downloaded to: an iPhone-only app still installs on iPad unless `UIRequiredDeviceCapabilities` excludes it, and Mac / Vision Pro availability is set in App Store Connect > Pricing and Availability. Flag any device type that was removed from destinations but is still reachable.
  - fix: Test and support the reachable device types. To exclude one, use App Store Connect availability settings, or `UIRequiredDeviceCapabilities` for genuine hardware dependencies.
- **[HELP-42]** Do the app's interfaces respond to different screen sizes and orientations?
  - quote: "Build interfaces that respond to different screen sizes and orientations."
  - surface: runtime
  - verify: In code, check for fixed frames tied to one screen size (`UIScreen.main.bounds` hard-coding, literal widths) and check `UISupportedInterfaceOrientations` / `UISupportedInterfaceOrientations~ipad`. At runtime, rotate and resize (iPad Split View / Stage Manager, smallest and largest iPhone) and confirm nothing is clipped or overlapping.
  - fix: Use adaptive layout (Auto Layout constraints, SwiftUI flexible stacks, size classes), and support every orientation that is declared.
- **[HELP-43]** Does the app adapt its features to available hardware and provide alternatives for a consistent experience?
  - quote: "Adapt features based on available hardware, providing alternatives for a consistent experience."
  - surface: code
  - verify: For each hardware-dependent feature (camera, GPS, NFC, haptics, motion, telephony, Apple Pencil, LiDAR), confirm there is an availability check (`AVCaptureDevice.default(...) != nil`, `CMMotionManager.isDeviceMotionAvailable`, `NFCTagReaderSession.readingAvailable`, `CHHapticEngine.capabilitiesForHardware().supportsHaptics`, `ARWorldTrackingConfiguration.supportsSceneReconstruction`) and an alternative path.
  - fix: Gate each hardware feature behind an availability check and offer an alternative (for example a photo picker when there is no camera, or manual entry when NFC is missing).
- **[HELP-44]** Does the app avoid assuming only one type of device or input method?
  - quote: "Don't design rigid interfaces that assume only one type of device or input method."
  - surface: runtime
  - verify: Operate the app's primary flows with a hardware keyboard and trackpad (iPad / Mac) and with touch. In code, look for gestures that have no button or menu equivalent.
  - fix: Add pointer, keyboard and menu equivalents for touch-only interactions.
- **[HELP-45]** Does the app keep working (no crash, still usable) when optional hardware is unavailable?
  - quote: "Don't let your app crash or become unusable when optional hardware is unavailable."
  - surface: runtime
  - verify: Run on a device or simulator without the optional hardware (simulator: no camera; iPad Wi-Fi: no GPS or telephony; Mac: no motion sensors). Trigger each hardware feature and confirm there is no crash and no dead end. In code, look for force-unwraps of `AVCaptureDevice.default(...)!` and similar calls.
  - fix: Replace the force-unwraps with availability checks and show a graceful fallback.

## HELP.12 Restrict device distribution

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices

**Source text (verbatim):**
> Wherever possible, make your app available on multiple platforms to increase its reach and provide people with a consistent experience across devices. But there are cases where it makes sense to restrict an app's availability. For example:
>
> - iPhone apps that rely on iPhone-specific hardware won't function as expected on iPad. Use the UIRequiredDeviceCapabilities key in the information property list file to specify hardware dependencies.
>
> Note: Apps should only use the UIRequiredDeviceCapabilities key for genuine hardware dependencies, not to indicate distribution preferences.
>
> - Navigation- or camera-based apps are not well suited for visionOS. Learn more about managing availability of iPhone and iPad apps on Apple Vision Pro.
> - Apps that rely heavily on touch inputs that can't be replicated on a keyboard are not well suited for macOS. Learn more about restricting distribution to Apple Silicon devices.
>
> Related Testing a release build Acquiring crash reports and diagnostic logs How to configure multiplatform apps in Xcode Configure In-App Purchases for review in the sandbox

**Applies to:** Apps that restrict their device availability, and iPhone apps that rely on iPhone-specific hardware

- **[HELP-46]** If an iPhone app relies on iPhone-specific hardware, does Info.plist declare those dependencies with UIRequiredDeviceCapabilities?
  - quote: "Use the UIRequiredDeviceCapabilities key in the information property list file to specify hardware dependencies."
  - surface: code
  - verify: Find the hardware the app cannot work without (e.g. `telephony`, `nfc`, `gps`, `arkit`, `front-facing-camera`). Check Info.plist (or `INFOPLIST_KEY_UIRequiredDeviceCapabilities` in build settings) for matching `UIRequiredDeviceCapabilities` entries.
  - fix: Add the genuine hardware dependencies to `UIRequiredDeviceCapabilities` (and only genuine ones; see HELP-47).
- **[HELP-47]** Is UIRequiredDeviceCapabilities used only for genuine hardware dependencies, not to show distribution preferences?
  - quote: "Apps should only use the UIRequiredDeviceCapabilities key for genuine hardware dependencies, not to indicate distribution preferences."
  - surface: code
  - verify: For each `UIRequiredDeviceCapabilities` entry in Info.plist, confirm the code actually needs that hardware (for example `telephony` is listed only if the app calls `CTTelephonyNetworkInfo` or places calls as a core function).
  - fix: Remove entries that only express distribution preferences. Use App Store Connect availability settings instead.

## HELP.13 Request a one-on-one App Review appointment

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/app-review-appointment

**Source text (verbatim):**
> If you have questions about the review process, you can request to meet with App Review over Webex. In each 30-minute video appointment, you can ask for advice on what to expect during review, how your app can best align with guidelines, reasons for common rejections, and topics related to the process of reviewing your app for distribution.
>
> ## How to request an App Review appointment
>
> - Request an appointment on the Meet with Apple schedule page. Appointments are subject to availability during your local business hours on Tuesdays and Thursdays.
> - In your request, include your app's Apple ID from App Store Connect (if you have one) and the specific questions you'd like to discuss.
> - Discuss your app with an App Review expert during the appointment. Appointments are conducted on video over Webex; having your camera on is optional.
>
> Note: A Meet with Apple appointment is informational. It doesn't replace, expedite, or guarantee the outcome of your app's review.

**Applies to:** Developers requesting an App Review appointment

- **[HELP-48]** Does the appointment request include the app's Apple ID from App Store Connect (if there is one) and the specific questions to discuss?
  - quote: "In your request, include your app's Apple ID from App Store Connect (if you have one) and the specific questions you'd like to discuss."
  - surface: manual
  - verify: Before sending the Meet with Apple request, confirm it includes the Apple ID (App Store Connect > App Information > Apple ID) and a list of specific questions.
  - fix: manual — requires developer decision/legal/business action.

## HELP.14 Tips about appointment requests

**Source page:** https://developer.apple.com/help/app-review/before-submitting-for-review/app-review-appointment

**Source text (verbatim):**
> #### Do
>
> - Request an appointment if you're unsure how a specific guideline applies to your app, or want general guidance on how to prepare an app for review.
> - Come with specific questions so App Review can provide useful feedback in the time available.
> - Keep in mind every submission is evaluated against the App Review Guidelines at the time of review, so App Review cannot preapprove apps or specific features during your appointment.
>
> #### Don't
>
> - Don't consider an App Review appointment a replacement for reading the App Review Guidelines yourself.
>
> Related Provide information for a complete review Contact App Review for help with a submission

**Applies to:** Developers requesting an App Review appointment

## HELP.15 Track a submission’s review status: Check your submission status

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/review-status

**Source text (verbatim):**
> App Review works around the clock with the goal of reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours. While updates with minor changes and bug fixes typically move through review quickly, other submissions may take longer to verify.
>
> ## Check your submission status
>
> You can check the status of a submission at any time by visiting the App Review section of App Store Connect. Track the status of all your submitted items in one place, including your app versions, In-App Purchases, custom product pages, and more.
>
> Your submission will display one of several statuses during the review process, including:
>
> - Waiting for Review: Apple received your submission, but review hasn’t started. You can still edit certain information or remove items from the submission, though you can’t upload or edit screenshots and app previews.
> - In Review: App Review is reviewing your submission. You can cancel the submission to remove it from review.
> - Unresolved Issues: App Review identified issues with one or more items in the submission.
>
> For the full list of app, submission, and item statuses, see App and submission statuses.
>
> You can also set up webhooks to receive automatic server notifications whenever a submission’s status changes.

**Applies to:** All submissions

## HELP.16 When to resubmit for review

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/review-status

**Source text (verbatim):**
> In general, reserve resubmissions for changes that require a new review.
>
> It’s not necessary to resubmit when:
>
> - App Review requested more information and there are no other issues to resolve. Instead, you can reply directly to the message in App Store Connect. Resubmitting starts a new review, after which App Review can no longer reply to your previous message.
> - Issues can be resolved by revising metadata or making server-side adjustments, such as providing or activating demo credentials. Reply to App Review in App Store Connect once the required changes have been made.
> - You’ve been offered and want to accept approval for a Bug Fix Submission. Reply to the message to accept the offer without resubmitting. Learn more about accepting Bug Fix Submission offers.
> - You’re appealing a rejection or removal to the App Review Board. Resubmitting will initiate a new review and the appeal will be closed. Learn more about appealing to the App Review Board.
>
> It’s appropriate to resubmit when:
>
> - The submission is rejected for an issue in the build and you’ve fixed it. Upload the new build and submit that version. This starts a full review of the new build.
> - Some items in the submission were rejected, others were accepted, and you want to move ahead with approval on the accepted items. Remove the rejected items and resubmit.
>
> Note: Don’t resubmit until you’ve resolved every issue identified by App Review. Resubmitting with unresolved issues delays review and results in the same outcome. If you have questions about how to resolve an issue, contact App Review for help with a submission.

**Applies to:** Submissions that received a message, rejection, or Bug Fix Submission offer from App Review

- **[HELP-49]** Before resubmitting, has every issue identified by App Review been resolved?
  - quote: "Don’t resubmit until you’ve resolved every issue identified by App Review."
  - surface: manual
  - verify: List every guideline cited in the latest App Review message (App Store Connect > App Review > the submission's message). For each one, record the code, metadata or server change that resolves it.
  - fix: manual — requires developer decision/legal/business action (resolve the remaining issues first).
- **[HELP-50]** If App Review only asked for more information and there are no other issues, did the developer reply to the message instead of resubmitting?
  - quote: "Instead, you can reply directly to the message in App Store Connect."
  - surface: manual
  - verify: Read the App Review message. If it only asks for information, confirm the response goes through Reply to App Review and that no new build or submission was created.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-51]** If the issues can be fixed through metadata or server-side changes (such as demo credentials), did the developer make the changes and then reply to App Review?
  - quote: "Reply to App Review in App Store Connect once the required changes have been made."
  - surface: manual
  - verify: Confirm the metadata or server change is live (for example, the demo credentials work), then confirm a reply was sent in App Store Connect.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-52]** If the submission was rejected for an issue in the build and it has been fixed, was a new build uploaded and that version submitted?
  - quote: "Upload the new build and submit that version."
  - surface: manual
  - verify: Confirm a build with a higher `CFBundleVersion` containing the fix is uploaded and selected on the version page in App Store Connect, then submitted.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-53]** If some items were rejected and others accepted, and the developer wants to move ahead with the accepted ones, were the rejected items removed before resubmitting?
  - quote: "Remove the rejected items and resubmit."
  - surface: manual
  - verify: In App Store Connect > App Review > the submission, confirm the rejected items have been removed before resubmitting.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-132]** If an appeal to the App Review Board is pending, has the developer avoided resubmitting (which closes the appeal)?
  - quote: "Resubmitting will initiate a new review and the appeal will be closed."
  - surface: manual
  - verify: Check whether an appeal is open for the app. If one is, confirm no new submission was made while it is pending.
  - fix: manual — requires developer decision/legal/business action (wait for the App Review Board, or accept that resubmitting closes the appeal).

## HELP.17 Why some reviews take longer

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/review-status

**Source text (verbatim):**
> Most submissions are reviewed within 48 hours. Some need additional time for verification, particularly those involving the following:
>
> - Limited review history: Apps with little or no prior App Review history.
> - Required documentation: Authorizations, licenses, partnership agreements, or other materials App Review must confirm before approval.
> - Complex or novel issues: Regulated content, new platform capabilities, enabled entitlements, or other sensitive features that require greater scrutiny.
>
> To help reduce review time, provide information about your app and attach all required documentation in the App Review Information section before submitting. Learn more about providing information for a complete review.

**Applies to:** All submissions

- **[HELP-54]** Before submitting, has information about the app been provided and all required documentation attached in the App Review Information section?
  - quote: "provide information about your app and attach all required documentation in the App Review Information section before submitting."
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information: confirm the Notes are filled in (see HELP.3) and the Attachment holds any required documentation (see HELP.5). Also list the enabled entitlements from the `.entitlements` file(s), since those can add scrutiny.
  - fix: Fill in the Notes and upload the documentation before submitting.

## HELP.18 When fraud or malicious activity is detected

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/review-status

**Source text (verbatim):**
> To protect the App Store’s high standards for privacy, security, and quality, App Review has a zero-tolerance policy for fraudulent or malicious activity. App Review investigates all reported or identified conduct that falls outside the Developer Code of Conduct, which requires accurate representation and integrity across the app ecosystem. An investigation can extend a submission’s review. Examples include:
>
> - Misrepresented developer identity or impersonation, such as providing inauthentic documentation. (Guidelines 4.1 and 5.6.2)
> - Manipulation of the App Store experience, including gaming charts, search results, reviews, or referrals, or attempting to hide features in review. (Guidelines 2.3.1(a) and 5.6.3)
> - Submitting low-quality apps, as indicated by excessive customer reports such as negative customer reviews and high-volume refund requests. (Guidelines 4.3 and 5.6.4)
>
> When these signals appear, App Review investigates thoroughly. Repeated or serious violations can lead to additional rejections, app removals, and removal of your account from the Apple Developer Program.
>
> Related Provide information for a complete review Contact App Review for help with a submission Request an expedited review App and submission statuses

**Applies to:** All apps

- **[HELP-55]** Does the app avoid hiding features from App Review?
  - quote: "attempting to hide features in review"
  - surface: code
  - verify: Search the code for logic that changes behavior during review: remote-config or feature flags that turn features on after approval, date or time gates around the release date, checks for review-like conditions (sandbox receipt, reviewer IP or region, specific demo account IDs) that hide or show functionality. Confirm every feature is reachable by the reviewer, or disclosed in the Notes.
  - fix: Remove the review-detection or hidden-feature gating, and disclose all functionality in App Review Information > Notes.
- **[HELP-56]** Is the developer identity represented accurately, with only authentic documentation provided?
  - quote: "Misrepresented developer identity or impersonation, such as providing inauthentic documentation."
  - surface: manual
  - verify: Confirm the seller and developer name in App Store Connect (App Information) matches the real entity, and that every attached document is genuine.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-57]** Does the developer avoid gaming charts, search results, reviews, or referrals?
  - quote: "gaming charts, search results, reviews, or referrals"
  - surface: manual
  - verify: Review the marketing practices and in-app code for review or referral manipulation. Examples: rewards in exchange for ratings (search near `requestReview` / `SKStoreReviewController` for reward logic), fake or bought reviews, and keyword or chart manipulation services.
  - fix: manual — requires developer decision/legal/business action.

## HELP.19 Contact App Review for help with a submission

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review

**Source text (verbatim):**
> If a submission doesn't pass review, you'll receive a message from App Review in App Store Connect detailing the issues requiring your attention.
>
> If you have questions, contact App Review directly by clicking Reply to App Review in App Store Connect. Using App Store Connect to contact App Review is the best way to receive assistance with an ongoing submission. A specialist familiar with your app will reply to your message.
>
> ## What to include in your reply to App Review
>
> #### Do
>
> - Be specific about what you're asking, such as the exact feature, guideline, or step you need clarified.
> - Provide additional information that can help App Review understand the app's concept and intended functionality if you believe your app was misunderstood.
>
> #### Don't
>
> - Don't use the Reply to App Review field to appeal a rejection or removal or to request an expedited review. For these requests, use the appropriate Contact Us form instead.
> - Don't ask about the status of apps from other developers. Just as App Review wouldn't discuss your app with someone else, App Review can't discuss other developers' apps with you.

**Applies to:** Developers replying to App Review about an ongoing submission

- **[HELP-58]** Is the reply to App Review specific about what is being asked (the exact feature, guideline, or step)?
  - quote: "Be specific about what you're asking, such as the exact feature, guideline, or step you need clarified."
  - surface: manual
  - verify: Before sending a Reply to App Review, confirm it names the exact feature, guideline number, or step in question.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-59]** Does the developer use the appropriate Contact Us form, not the Reply to App Review field, for appeals and expedited review requests?
  - quote: "Don't use the Reply to App Review field to appeal a rejection or removal or to request an expedited review."
  - surface: manual
  - verify: Confirm that appeals and expedite requests go through their dedicated forms (see HELP.21 and HELP.23), not through Reply to App Review.
  - fix: manual — requires developer decision/legal/business action.

## HELP.20 Request a call with an Apple representative

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review

**Source text (verbatim):**
> If you need additional assistance after App Review replies to your message, you can use the Reply to App Review message window to request a call with an Apple representative.
>
> Before requesting a call, confirm your contact details in the App Review Information section of App Store Connect are up to date.
>
> When requesting a call, include your time zone so App Review can attempt to call during your local business hours. You can also specify a preferred language for the call. App Review will try to accommodate your request, though availability can vary. Calls are typically completed within three to five business days.
>
> Related Accept Bug Fix Submission offers Appeal to the App Review Board Request an expedited review

**Applies to:** Developers requesting a call with an Apple representative

- **[HELP-60]** Before requesting a call, are the contact details in the App Review Information section up to date?
  - quote: "confirm your contact details in the App Review Information section of App Store Connect are up to date."
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information > Contact Information: First name, Last name, Phone number (with country code) and Email are current and reachable.
  - fix: Update the contact information fields.
- **[HELP-61]** Does the call request include the developer's time zone?
  - quote: "When requesting a call, include your time zone"
  - surface: manual
  - verify: Confirm the Reply to App Review message requesting a call states the time zone (and, optionally, a preferred language).
  - fix: manual — requires developer decision/legal/business action.

## HELP.21 Request an expedited review

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review

**Source text (verbatim):**
> App Review works around the clock with the goal of reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours. However, if you're facing extenuating circumstances, such as fixing a critical bug or timing your release to coincide with an event, you can request an expedited review.
>
> - Submit the app for review in App Store Connect. Only submissions that have already been sent to App Review can be expedited. Make sure the app is ready for review by adding all required information in the Notes field and providing a demo account or demo mode for account-based features.
> - Go to Request an Expedited App Review, select the app and platform which you would like to receive an expedited review, and submit.
> - App Review will evaluate your request and expedite the app's review as allowed by availability and demand.
>
> Note: Expedite requests should be reserved for matters of genuine urgency.
>
> ### Critical bug fixes
>
> If you're requesting an expedited review to fix a critical bug, include this information in the Notes field in App Store Connect when you submit the app for review.
>
> ### Event-related apps
>
> If you're requesting an expedited review to align the app's release with an upcoming event, include the event, its date, and how your app is associated with it in the Notes field in App Store Connect when you submit the app for review. Schedule its release in App Store Connect ahead of time if you can.
>
> Related Track a submission's review status Contact App Review for help with a submission

**Applies to:** Developers requesting an expedited review

- **[HELP-62]** Before requesting an expedited review, was the app submitted with all required information in the Notes field and a demo account or demo mode for account-based features?
  - quote: "Make sure the app is ready for review by adding all required information in the Notes field and providing a demo account or demo mode for account-based features."
  - surface: asc
  - verify: Confirm the version status is Waiting for Review or later, App Review Information > Notes is complete, and sign-in information or demo-mode instructions are present.
  - fix: Complete the Notes and demo access, submit, and then file the expedite request.
- **[HELP-63]** If expediting to fix a critical bug, does the Notes field include that information?
  - quote: "If you're requesting an expedited review to fix a critical bug, include this information in the Notes field in App Store Connect when you submit the app for review."
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information > Notes: describes the critical bug being fixed.
  - fix: Add the critical-bug description to the Notes.
- **[HELP-64]** If expediting for an event, does the Notes field include the event, its date, and how the app is associated with it?
  - quote: "include the event, its date, and how your app is associated with it in the Notes field"
  - surface: asc
  - verify: App Store Connect > (version) > App Review Information > Notes: names the event, gives its date, and explains the app's link to it.
  - fix: Add the event details to the Notes.
- **[HELP-133]** Is the expedite request reserved for a matter of genuine urgency (such as a critical bug fix or a time-sensitive event)?
  - quote: "Expedite requests should be reserved for matters of genuine urgency."
  - surface: manual
  - verify: Confirm the reason for the expedite request is a critical bug or an upcoming event tied to the app, not general schedule preference.
  - fix: manual — requires developer decision/legal/business action.

## HELP.22 Accept Bug Fix Submission offers

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions

**Source text (verbatim):**
> If a bug-fix update is rejected but introduces no legal or safety concerns, you can choose to resolve the issues in your next submission. This process allows you to deliver bug fixes quickly, giving you time to resolve any outstanding issues in your next submission.
>
> Note: Bug Fix Submission offers are only available for updates to apps that have been previously approved for the App Store or alternative distribution.
>
> - In App Store Connect, open the rejection message. If your submission is eligible, this language will appear at the top of the message:
>
> "Bug Fix Submissions: The issues we've identified below are eligible to be resolved on your next update."
>
> - If you see the note, reply to the message and let App Review know you'd like the current submission approved and will address the issues in your next update. Do not resubmit the app at this time, as it will trigger a new review.
>
> If you don't see the note, the submission doesn't qualify, and you'll need to resolve the issues before the submission can be approved.
>
> - App Review will reply to confirm and approve the submission.
> - In your next update, resolve all deferred issues from the prior submission. App Review will verify that each issue has been addressed before approving the update.
>
> Note: Issues that were deferred on a previous submission aren't eligible to be deferred again on the next submission.
>
> Related Contact App Review for help with a submission

**Applies to:** Updates to previously approved apps whose rejection message carries the Bug Fix Submissions note

- **[HELP-65]** When accepting a Bug Fix Submission offer, did the developer reply to the message without resubmitting the app?
  - quote: "Do not resubmit the app at this time, as it will trigger a new review."
  - surface: manual
  - verify: Confirm the rejection message has the "Bug Fix Submissions" note, that a reply was sent accepting it, and that no new submission was created.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-66]** Does the next update resolve all issues deferred from the prior submission?
  - quote: "In your next update, resolve all deferred issues from the prior submission."
  - surface: manual
  - verify: List the issues from the earlier Bug Fix Submission rejection message and confirm each one is fixed in the new build or metadata (they cannot be deferred again).
  - fix: manual — requires developer decision/legal/business action (fix each deferred issue before submitting).

## HELP.23 Appeal to the App Review Board

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board

**Source text (verbatim):**
> If you disagree with the outcome of a review, you can file an appeal with the App Review Board. It's appropriate to file an appeal when:
>
> - Your app was rejected or removed, but you believe it follows the App Review Guidelines and the Apple Developer Program License Agreement.
> - Your account is facing termination, but you believe it complies with the App Review Guidelines and the Apple Developer Program License Agreement.
> - You believe you experienced unfair or biased treatment during review.
>
> Note: Don't file an appeal to reinstate an already-terminated account, get a status update on your app, or request an expedited review. For these requests, use the appropriate Contact Us form instead.
>
> - Before filing an appeal, reply to the rejection, removal, or termination message you received in App Store Connect and provide clarification about the issue. If this clarification is not sufficient to resolve the issue, proceed with filing an appeal.
> - Go to Submit an appeal to App Review and describe why you believe your app or account follows the App Review Guidelines and the Apple Developer Program License Agreement.
>
> For app rejections or removals, point to the specific requirements involved and explain how your app satisfies them.
>
> For account terminations, reference the specific terms your account was found to be violating, and explain how your account meets those requirements. If the termination references other guideline violations you believe were in error, provide an additional explanation of those instances as well.
>
> - The App Review Board will send you a message in App Store Connect once its investigation is complete. They may also message you in App Store Connect to request additional information or schedule a call to discuss the outcome of the investigation.
>
> Note: Only submit one appeal per rejected or removed app. If an app's rejection or removal message cites multiple guideline violations, address all of them in one appeal.

**Applies to:** Developers appealing a rejection, removal, or pending account termination

- **[HELP-134]** Does the developer avoid using an appeal to reinstate an already-terminated account, get a status update, or request an expedited review (using the appropriate Contact Us form instead)?
  - quote: "Don't file an appeal to reinstate an already-terminated account, get a status update on your app, or request an expedited review."
  - surface: manual
  - verify: Confirm the appeal concerns a rejection, removal, pending termination, or unfair treatment, and not one of the excluded requests.
  - fix: manual — requires developer decision/legal/business action (use the appropriate Contact Us form).
- **[HELP-67]** Before filing an appeal, did the developer reply to the rejection, removal, or termination message in App Store Connect with clarification?
  - quote: "Before filing an appeal, reply to the rejection, removal, or termination message you received in App Store Connect and provide clarification about the issue."
  - surface: manual
  - verify: Confirm a clarifying reply was sent in App Store Connect and did not resolve the issue before the appeal was filed.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-68]** For a rejection or removal, does the appeal point to the specific requirements involved and explain how the app satisfies them?
  - quote: "For app rejections or removals, point to the specific requirements involved and explain how your app satisfies them."
  - surface: manual
  - verify: Review the appeal draft: each cited requirement is named and addressed.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-69]** For an account termination, does the appeal reference the specific terms found to be violated and explain how the account meets them?
  - quote: "For account terminations, reference the specific terms your account was found to be violating, and explain how your account meets those requirements."
  - surface: manual
  - verify: Review the appeal draft against the termination message.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-70]** Is there only one appeal per rejected or removed app, addressing every cited guideline violation?
  - quote: "address all of them in one appeal."
  - surface: manual
  - verify: List every guideline cited in the rejection or removal message and confirm the single appeal addresses each one.
  - fix: manual — requires developer decision/legal/business action.

## HELP.24 What to include in your appeal

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board

**Source text (verbatim):**
> #### Do
>
> - Cite the specific guideline or terms your app was rejected or removed under, and explain point by point how your app meets it.
> - Include additional information about your app that is relevant to the rejection, removal, or pending termination decision you're disputing.
> - Use the form to submit appeals for up to five rejected or removed apps.
>
> #### Don't
>
> - Don't file an appeal for requests from App Review for additional information or documentation about your app. This information is necessary for App Review to complete the review.
> - Don't include information that is not relevant to the rejection, removal, or pending termination decision you are appealing.
> - Don't file an appeal if you've addressed the issues App Review identified and resubmitted the app for review.
>
> #### Example (Complete)
>
> "My app was rejected under Guideline 2.1 for incomplete information. The demo account and setup steps needed to test the flagged feature are included in the App Review Information section of this submission, along with screenshots showing the feature working as described."
>
> #### Example (Incomplete)
>
> "This app is important to my business and shouldn't have been rejected. Please take another look."
>
> Note: Appeals that include all required information help the App Review Board process your request quickly. Submitting a complete appeal does not guarantee that the App Review Board will overturn the rejection, removal, or termination.
>
> Related App Review Guidelines Apple Developer Program License Agreement Contact App Review for help with a submission Track a submission's review status Request an expedited review

**Applies to:** Developers appealing a rejection, removal, or pending account termination

- **[HELP-71]** Does the appeal cite the specific guideline or terms and explain point by point how the app meets it?
  - quote: "Cite the specific guideline or terms your app was rejected or removed under, and explain point by point how your app meets it."
  - surface: manual
  - verify: Review the appeal draft: guideline numbers are cited and there is a point-by-point explanation (compare the Complete and Incomplete examples).
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-72]** Is the appeal limited to information relevant to the decision being disputed?
  - quote: "Don't include information that is not relevant to the rejection, removal, or pending termination decision you are appealing."
  - surface: manual
  - verify: Review the appeal draft and remove unrelated content (for example business importance alone, as in the Incomplete example).
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-73]** Is the developer avoiding an appeal in response to App Review's requests for more information or documentation?
  - quote: "Don't file an appeal for requests from App Review for additional information or documentation about your app."
  - surface: manual
  - verify: If the App Review message only asks for information or documentation, answer it through Reply to App Review (see HELP-50) instead of appealing.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-74]** Is the developer avoiding an appeal after already fixing the issues and resubmitting?
  - quote: "Don't file an appeal if you've addressed the issues App Review identified and resubmitted the app for review."
  - surface: manual
  - verify: Check App Store Connect for a newer submission that addresses the issues. If there is one, do not file an appeal.
  - fix: manual — requires developer decision/legal/business action.

## HELP.25 Suggest changes to the guidelines

**Source page:** https://developer.apple.com/help/app-review/after-submitting-for-review/improve-guidelines

**Source text (verbatim):**
> The App Review Guidelines are regularly updated to meet the needs of both customers and developers. If you have an idea for how the App Review Guidelines could be clearer or more complete, you can suggest a guideline change.
>
> - Go to Suggest a guideline change.
> - Select the guidelines you have feedback on. You can submit feedback on up to five guidelines.
> - Describe your suggested changes or clarifications, as well as specific reasons to support these changes.
> - App Review will consider the suggestion for potential future updates and may contact you for more information.
>
> Note: You may also use this form to suggest changes to Notarization Review Guidelines.
>
> ## What to include in your suggestion
>
> #### Do
>
> - Cite the specific guideline text you're suggesting a change for.
> - Explain how the current guideline text is unclear or incomplete, and what change would address it.
> - Include the Apple IDs of apps you've submitted in App Store Connect that would be impacted by this change.
>
> #### Don't
>
> - Don't use this form to appeal a rejection or removal, ask about a previous submission, or report a specific app. Use the appropriate Contact Us form instead.
> - Don't assume that submitting a complete suggestion guarantees the guideline will change.
>
> #### Example (Complete)
>
> "I understand that App Review typically uses demo accounts to complete a full review of my app. However, due to legal and security obligations, I'm unable to provide demo accounts that can be used in review. Can you add options to the guidelines for other ways I can provide full access for review? For example, I could implement a demonstration mode that shows off all of my apps features."
>
> #### Example (Incomplete)
>
> "This guideline doesn't make sense. Change it."
>
> Related Appeal to the App Review Board App Review Guidelines Contact App Review for help with a submission Report an app

**Applies to:** Developers suggesting a guideline change

- **[HELP-75]** Does the guideline-change suggestion cite the specific guideline text, explain how it is unclear or incomplete and what change would address it, and include the Apple IDs of affected apps?
  - quote: "Cite the specific guideline text you're suggesting a change for."
  - surface: manual
  - verify: Review the suggestion draft for the cited text, the explanation, the proposed change, and the affected app Apple IDs.
  - fix: manual — requires developer decision/legal/business action.

## HELP.26 2.3.3 - Show your app in use with screenshots

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots

**Source text (verbatim):**
> Screenshots are often the first thing people see on your app’s product page, so they must show your actual app in use and make its value clear.
>
> App Review Guideline 2.3.3 provides guidance to ensure screenshots accurately communicate your app’s value and experience:
>
> 2.3.3
>
> Screenshots should show the app in use, and not merely the title art, login page, or splash screen. They may also include text and image overlays (for example, to demonstrate input mechanisms, such as an animated touch point or Apple Pencil) and show extended functionality on device, such as Touch Bar.

**Applies to:** All apps

- **[HELP-76]** Do the screenshots show the app in use, and not merely the title art, login page, or splash screen?
  - quote: "Screenshots should show the app in use, and not merely the title art, login page, or splash screen."
  - surface: asc
  - verify: App Store Connect > (version) > Previews and Screenshots, for each device size and localization. Look at each image (or the local fastlane `screenshots/` folder if one is used) and flag images that show only title art, login or splash screens.
  - fix: Replace those images with captures of the app's main screens in use.

## HELP.27 Show your app in use in the majority of your screenshots

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots

**Source text (verbatim):**
> You can decide how many screenshots to include for each device type supported by your app. App Review takes the set of screenshots submitted for each supported device into account, and will approve only those submissions where more than half of screenshots show the app in use. As long as the majority of the screenshots show the app in use, your other screenshots can exhibit the app’s main benefits and features using marketing materials and other information.
>
> For example, if an app has three screenshots for each supported device, two of the screenshots for each device must show the app in use on that device. If an app has four screenshots for each device, three must show the app in use, and so on.
>
> #### Do
>
> - Show your app’s main features and functionality in the majority of the screenshots for each device type.
> - Update your screenshots with each new version so they match the current user interface.
> - Include screenshots that show your app operating in different configurations, such as Dark Mode.
> - Include splash screens or marketing text, as long as the majority of screenshots still show the app in use.
>
> #### Don’t
>
> - Don’t submit screenshots that only show generic login pages or splash screens.
> - Don’t submit screenshots that misrepresent the app’s actual interface or include misleading marketing or promotional materials.

**Applies to:** All apps

- **[HELP-77]** For each supported device type, do more than half of the screenshots show the app in use on that device?
  - quote: "will approve only those submissions where more than half of screenshots show the app in use."
  - surface: asc
  - verify: App Store Connect > (version) > Previews and Screenshots. For each device size (iPhone, iPad, Mac, Apple TV, Apple Vision Pro, Apple Watch) count the in-use screenshots N and the total T, and pass only if N > T/2 (3 total needs 2; 4 total needs 3).
  - fix: Add in-use screenshots, or replace marketing-only ones, until in-use captures are a strict majority for each device.
- **[HELP-78]** Do the screenshots match the current version's user interface?
  - quote: "Update your screenshots with each new version so they match the current user interface."
  - surface: asc
  - verify: Compare each screenshot against the current build at runtime (same screens, current design, current feature names). Flag outdated UI.
  - fix: Capture fresh screenshots from the current build (for example with UI tests or fastlane snapshot) and upload them.
- **[HELP-79]** Do the screenshots avoid misrepresenting the app's actual interface or including misleading marketing or promotional materials?
  - quote: "Don’t submit screenshots that misrepresent the app’s actual interface or include misleading marketing or promotional materials."
  - surface: asc
  - verify: For every screenshot, confirm the UI shown exists in the build, and that any claims (features, prices, awards, rankings) are accurate.
  - fix: Replace mock-ups or edited UIs with real captures, and remove misleading claims.

## HELP.28 Include overlays and visuals to show how people interact with your app

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots

**Source text (verbatim):**
> Screenshots can contain more than a plain capture of your interface, provided the screenshot still reflects your app in use. Use text and image overlays to demonstrate input mechanisms. You can include messaging and other visuals, as long as the primary app functionality in the screenshot isn’t obscured.
>
> #### Do
>
> - Use overlays to demonstrate input mechanisms.
> - Show extended functionality on device alongside your app in use.
> - Show your app running on another Apple platform when that’s part of the experience.
>
> #### Don’t
>
> - Don’t let overlays or marketing visuals crowd out your app.
> - Don’t show only the hardware or an overlay with no app interface behind it.
>
> Note: Screenshots that reference third-party platforms, such as in a status bar, are assessed under App Review Guideline 2.3.10.

**Applies to:** Apps whose screenshots use overlays, marketing visuals, or device frames

- **[HELP-80]** In screenshots with overlays or messaging, is the primary app functionality left unobscured and not crowded out?
  - quote: "as long as the primary app functionality in the screenshot isn’t obscured."
  - surface: asc
  - verify: For each screenshot with text or image overlays, confirm the app's UI stays the main visible element and is not covered.
  - fix: Shrink or move the overlays so the app interface is clearly visible.
- **[HELP-81]** Does every screenshot show app interface, rather than only hardware or an overlay with no app interface behind it?
  - quote: "Don’t show only the hardware or an overlay with no app interface behind it."
  - surface: asc
  - verify: Flag screenshots that show only a device frame, hardware, or a graphic with no app UI.
  - fix: Replace them with screenshots that include the app interface.
- **[HELP-82]** Have screenshots that reference third-party platforms (for example in a status bar) been checked against Guideline 2.3.10?
  - quote: "Screenshots that reference third-party platforms, such as in a status bar, are assessed under App Review Guideline 2.3.10."
  - surface: asc
  - verify: Look in each screenshot for third-party platform references (non-Apple status bars, other platforms' devices, logos or names), and check any found against Guideline 2.3.10 (see the guidelines reference).
  - fix: Remove or recapture screenshots whose third-party platform references Guideline 2.3.10 does not allow.

## HELP.29 2.3.3 FAQs

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots

**Source text (verbatim):**
> ### Do I need the same number of screenshots for every device?
>
> No. The number can differ by device, and one screenshot for a device is sufficient as long as it shows your app in use.
>
> ### Can my screenshots differ between localizations?
>
> Yes. Screenshots can be tailored to a localization. Each localization’s screenshots are still assessed on whether the majority show your app in use. Learn more about app localization.
>
> ### Can an image of my app be spread across two or more screenshots?
>
> Yes. An image of an app in use can be displayed across multiple screenshots.
>
> Related App Review Guideline 2.3 Upload app previews and screenshots Creating your product page Contact App Review for help with a submission

**Applies to:** All apps (localization check: apps with localized screenshots)

- **[HELP-83]** If a device has a single screenshot, does it show the app in use?
  - quote: "one screenshot for a device is sufficient as long as it shows your app in use."
  - surface: asc
  - verify: App Store Connect > (version) > Previews and Screenshots: for any device size with exactly one screenshot, confirm it shows the app in use.
  - fix: Replace it with an in-use capture.
- **[HELP-84]** For each localization, do the majority of that localization's screenshots show the app in use?
  - quote: "Each localization’s screenshots are still assessed on whether the majority show your app in use."
  - surface: asc
  - verify: Switch the App Store Connect version page through every localization (language menu at the top right) and repeat the HELP-77 majority count for each device size.
  - fix: Fix the localized screenshot sets that fail the majority rule.

## HELP.30 4.1 - Preventing copycat and impersonation rejections

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/4-1-prevent-copycat-rejection

**Source text (verbatim):**
> App Review rejects apps that copy other apps, and closes accounts that repeatedly submit copycat apps or attempt to impersonate a service. Focus on original ideas and experiences that aren't already available. Rather than replicating an existing app's functionality, name, or branding, invest in developing a distinct concept, unique design, and features that offer real value to users and set your app apart in the App Store.
>
> The rules that prevent copycat and impersonator apps from being distributed on the App Store are described in App Review Guideline 4.1:
>
> 4.1 Copycats
>
> (a) Come up with your own ideas. We know you have them, so make yours come to life. Don't simply copy the latest popular app on the App Store, or make some minor changes to another app's name or UI and pass it off as your own. In addition to risking an intellectual property infringement claim, it makes the App Store harder to navigate and just isn't fair to your fellow developers.
>
> (b) Submitting apps which impersonate other apps or services is considered a violation of the Developer Code of Conduct and may result in removal from the Apple Developer Program.
>
> (c) You cannot use another developer's icon, brand, or product name in your app's icon or name, without approval from the developer.
>
> These requirements help make the App Store both a safe place for people to discover apps and a platform for all developers to be successful.

**Applies to:** All apps

- **[HELP-85]** Is the app something other than a copy of a popular app, or another app's name or UI with minor changes?
  - quote: "Don't simply copy the latest popular app on the App Store, or make some minor changes to another app's name or UI and pass it off as your own."
  - surface: manual
  - verify: Search the App Store for the app's name, its category leaders and close competitors. Compare the name, UI and feature set, and flag near-duplicates.
  - fix: manual — requires developer decision/legal/business action (make the concept, design and name distinct).
- **[HELP-86]** Does the app avoid impersonating other apps or services?
  - quote: "Submitting apps which impersonate other apps or services is considered a violation of the Developer Code of Conduct"
  - surface: manual
  - verify: Check the name, icon, subtitle, description, screenshots and in-app branding for anything suggesting the app is, or is affiliated with, another app or service.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-87]** Do the app's icon and name avoid another developer's icon, brand, or product name (unless approved by that developer)?
  - quote: "You cannot use another developer's icon, brand, or product name in your app's icon or name, without approval from the developer."
  - surface: asc
  - verify: Check the App Store Connect App Information > Name and the version's subtitle, plus `CFBundleDisplayName` / `CFBundleName` in Info.plist and the AppIcon set in Assets.xcassets, for third-party brands or product names (for example "for Instagram" or "WhatsApp"). If any are found, confirm the developer's approval is attached in App Review Information.
  - fix: Rename or redesign the icon, or get the brand owner's approval and attach it.

## HELP.31 Submit apps with unique content and features

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/4-1-prevent-copycat-rejection

**Source text (verbatim):**
> ## Best practices to prevent copycats
>
> People want unique app experiences. Find an underserved audience and build a compelling app just for them.
>
> #### Do
>
> - Create apps that provide a new experience or a unique spin on an existing concept.
> - Design original, delightful interfaces that elegantly meet people's needs.
>
> #### Don't
>
> - Don't imitate the features and functionality of other apps.
> - Don't copy the look and feel of other apps.

**Applies to:** All apps

- **[HELP-88]** Does the app avoid imitating the features, functionality, and look and feel of other apps?
  - quote: "Don't copy the look and feel of other apps."
  - surface: manual
  - verify: Compare the app's screens and feature set side by side with the closest competing apps. Flag cloned layouts, iconography or flows.
  - fix: manual — requires developer decision/legal/business action.

## HELP.32 Keep App Store metadata accurate and relevant

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/4-1-prevent-copycat-rejection

**Source text (verbatim):**
> The metadata you provide in App Store Connect appears on your app's product page on the App Store. People rely on this metadata to learn what your app offers, so leveraging another brand's or app's popularity, through irrelevant references or by including protected content, is misleading and won't help your app succeed.
>
> #### Do
>
> - Use engaging, descriptive language to describe your app.
> - Create original content that best represents your app. Include screenshots that show the actual app in use.
>
> #### Don't
>
> - Don't use protected material without the necessary permission.
> - Don't include references to popular app names or trademarked terms in any metadata field.

**Applies to:** All apps

- **[HELP-89]** Are all metadata fields free of references to popular app names or trademarked terms?
  - quote: "Don't include references to popular app names or trademarked terms in any metadata field."
  - surface: asc
  - verify: For every localization in App Store Connect, check App Information > Name and Subtitle, and the version's Promotional Text, Description, Keywords and What's New, for other apps' names and trademarked terms (or the same fields in the local fastlane `metadata/` folder if one is used).
  - fix: Remove the third-party app names and trademarks from those fields.
- **[HELP-90]** Is protected material (in metadata or the app) used only with the necessary permission?
  - quote: "Don't use protected material without the necessary permission."
  - surface: manual
  - verify: Inventory third-party images, characters, logos, music and text in the screenshots, previews, icon and app bundle, and confirm a license or permission exists for each.
  - fix: manual — requires developer decision/legal/business action.

## HELP.33 Provide authentic and verifiable information

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/4-1-prevent-copycat-rejection

**Source text (verbatim):**
> People want to know that the developers behind their favorite apps are who they say they are. Keep your account and app information, like your developer or company name and Support URL, accurate so users can reach you and impersonation is harder.
>
> #### Do
>
> - Keep all information, resources, and documentation related to your account and apps current and accurate.
>
> #### Don't
>
> - Don't provide inaccurate or outdated information or resources, such as directing people to old support pages.
> - Don't provide fraudulent documentation. Accounts that submit fraudulent documentation will be removed from the Apple Developer Program.
>
> Related Create engaging App Store product pages Appeal to the App Review Board Contact App Review for help with a submission Learn about foundational design principles from Apple designers and the developer community Submit an intellectual property claim

**Applies to:** All apps

- **[HELP-91]** Are the developer or company name and the Support URL accurate, and do they avoid pointing people to old support pages?
  - quote: "Keep your account and app information, like your developer or company name and Support URL, accurate"
  - surface: asc
  - verify: App Store Connect > (version) > Support URL, for every localization: open each URL (`curl -sIL <url>`) and confirm it resolves to a current page for this app with a way to contact the developer. Check the seller name shown in App Information.
  - fix: Update the Support URL to a live, current support page, and correct the account information.
- **[HELP-92]** Is all documentation provided to Apple genuine (not fraudulent)?
  - quote: "Don't provide fraudulent documentation."
  - surface: manual
  - verify: Confirm every attachment in App Review Information and every account verification document is authentic.
  - fix: manual — requires developer decision/legal/business action.

## HELP.34 5.1.1(v) - Offering account deletion in your app

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion

**Source text (verbatim):**
> Apps submitted to the App Store that support account creation must also let people initiate deletion of their account within the app.
>
> Deleting an account removes the account from the developer's records, along with any data associated with the account that the developer isn't legally required to maintain. Providing this capability gives people more control of the personal data they've shared. If you're updating an app or submitting a new app with account creation, read the guidance below for a smoother submission process.

**Applies to:** Apps that support account creation

- **[HELP-93]** If the app supports account creation, can people start deleting their account from within the app?
  - quote: "Apps submitted to the App Store that support account creation must also let people initiate deletion of their account within the app."
  - surface: code
  - verify: Look for account creation in the code: `createUser`, `signUp`, `register`, `Auth.auth().createUser`, `supabase.auth.signUp`, Sign in with Apple (`ASAuthorizationAppleIDProvider`, which creates accounts), and anonymous or guest auth. If any is found, search for an in-app deletion entry point (`deleteAccount`, `deleteUser`, `user.delete()`, a "Delete Account" string in `Localizable.xcstrings`) and confirm at runtime that the flow is reachable while signed in.
  - fix: Add a "Delete Account" action (usually in account settings) that starts deletion of the account and its data.

## HELP.35 Account deletion guidance

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion

**Source text (verbatim):**
> Deleting an account is a major decision, so the process to initiate and confirm it must be straightforward and transparent:
>
> - Make the account deletion option easy to find in your app. Typically, it's included in the app's account settings.
> - Offer to delete the entire account record, along with associated personal data. You may include additional options, but only offering to temporarily deactivate or disable an account is insufficient.
> - If people need to visit a website to finish deleting their account, include a link directly to the page on your website where they can complete the process. On tvOS, you can present a static URL or QR code that links directly to the account deletion page.
> - Keep people informed. If the deletion request will take additional time to complete, let them know. If your app supports in-app purchases, help people understand how billing and cancellations will be handled. If you're legally required to retain some user information, let people know what information will and won't be retained. For additional guidance, read the Human Interface Guidelines.
>
> Note: Follow applicable legal requirements for storing and retaining user account information and for handling account deletion. This includes complying with local laws where your app is available. If you have questions regarding your legal obligations, check with your legal counsel.

**Applies to:** Apps that support account creation

- **[HELP-94]** Is the account deletion option easy to find in the app (typically in account settings)?
  - quote: "Make the account deletion option easy to find in your app."
  - surface: runtime
  - verify: Signed in with the demo account, go from the home screen to the deletion option. Confirm it is easy to find (typically in the account settings) and not hidden behind support screens.
  - fix: Move the delete-account entry into the account settings screen.
- **[HELP-95]** Does the app offer to delete the entire account record and associated personal data (not only deactivate or disable it)?
  - quote: "only offering to temporarily deactivate or disable an account is insufficient."
  - surface: code
  - verify: Trace the deletion action to the backend call. Confirm it deletes the account record and its personal data (for example `user.delete()` plus removal of user documents and storage), not only a `disabled` / `isActive=false` flag.
  - fix: Implement real deletion of the account and its data. Deactivation can stay as an extra option.
- **[HELP-96]** If deletion is finished on a website, does the app link directly to the page where the process is completed?
  - quote: "include a link directly to the page on your website where they can complete the process."
  - surface: runtime
  - verify: Tap the in-app deletion option. If it opens a web page, confirm the URL lands directly on the deletion page (not a home page, help-center search or login wall without a redirect).
  - fix: Point the link at the exact deletion page URL.
- **[HELP-97]** If deletion takes additional time, does the app tell people?
  - quote: "If the deletion request will take additional time to complete, let them know."
  - surface: runtime
  - verify: Run the deletion flow and confirm the confirmation screen states the timeframe whenever deletion is not immediate.
  - fix: Add the expected completion time to the deletion confirmation UI.
- **[HELP-98]** If the app supports in-app purchases, does the deletion flow help people understand how billing and cancellations will be handled?
  - quote: "If your app supports in-app purchases, help people understand how billing and cancellations will be handled."
  - surface: runtime
  - verify: If StoreKit purchases exist in the code, run the deletion flow and confirm it explains billing and cancellation.
  - fix: Add billing and cancellation guidance to the deletion flow (see HELP-112).
- **[HELP-99]** If some user information must legally be retained, does the app say what will and won't be retained?
  - quote: "If you're legally required to retain some user information, let people know what information will and won't be retained."
  - surface: runtime
  - verify: Run the deletion flow and look for a retention statement whenever the backend keeps any data after deletion.
  - fix: Add a retention disclosure to the deletion flow.
- **[HELP-100]** Does the deletion and retention handling follow applicable legal requirements, including local laws where the app is available?
  - quote: "Follow applicable legal requirements for storing and retaining user account information and for handling account deletion."
  - surface: manual
  - verify: Review with legal counsel against the storefronts listed in App Store Connect > Pricing and Availability.
  - fix: manual — requires developer decision/legal/business action.

## HELP.36 Account deletion FAQs

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion

**Source text (verbatim):**
> ### Can I direct people to a customer service flow to complete account deletion?
>
> It depends. Apps in highly regulated industries, as described in App Review Guideline 5.1.1(ix), may use additional customer service flows to confirm and facilitate the account deletion process. Apps not operating in highly regulated industries should not require people to make a phone call, send an email, use a chat support flow, or go through other support flows.
>
> ### Can I require reauthentication or add confirmation steps to ensure the account isn't deleted by accident or by someone other than the account holder?
>
> Yes. It's appropriate to confirm the user genuinely intends to delete their account. You may add steps to verify the identity of the person making the request, and to confirm that they want to delete the account, such as by entering a code from an email or phone number already associated with the account. However, apps that make it unnecessarily difficult for someone to delete their account will not pass review.
>
> ### My app uses Sign in with Apple to provide account creation and authentication. What changes are necessary to support people who delete their accounts?
>
> Apps that support Sign in with Apple should use the Sign in with Apple REST API to revoke user tokens. Use server-to-server notification endpoints to process changes for Sign in with Apple accounts. Note that developers based in the Republic of Korea must provide a server‑to‑server notification endpoint when registering a new Services ID.
>
> ### If my app links out to the default web browser for account creation, does it still need to offer account deletion within the app?
>
> Yes. Additionally, linking out to the default web browser to sign in or register an account provides a poor user experience and isn't appropriate, per App Review Guideline 4.
>
> ### My app automatically creates an account for the user. Do I need to include an option to initiate account deletion?
>
> Yes. People should have the option to delete automatically generated accounts (sometimes called "guest" accounts) and the data associated with those accounts. Ensure any automatic account creation in your app complies with local laws where your app is available.
>
> ### I manually delete accounts and this takes time. Does account deletion need to be immediate and automatic?
>
> No. If your process for account deletion is manual or otherwise takes a reasonable amount of time to complete, this is acceptable. Inform the person how long it will take to delete the account and provide a confirmation when the deletion is complete. Ensure the time it takes to delete accounts complies with local laws where your app is available.
>
> ### Does the content provided by a person need to be deleted in apps that display and share user-generated content?
>
> Yes. People expect that all data associated with their account will be deleted when the account is deleted. This includes user-generated content that's shared with others, such as photos, videos, text posts, and reviews. If local laws or regulations require you to maintain some data, let people know.
>
> ### I allow account deletion in compliance with CCPA, GDPR, or other local laws in some of the locations where my app is available. Is this sufficient?
>
> No. Everyone should be able to delete their accounts, regardless of where they're located. Existing account deletion flows you've created to comply with local legal requirements can be made available to everyone, as long as they meet the requirements of App Review Guideline 5.1.1(v).
>
> ### How do I handle people with auto-renewable subscriptions? I don't want to accidentally charge someone after they've deleted their account.
>
> If a person has an auto-renewable subscription, notify them that billing will continue through Apple and ask them to cancel their subscription before continuing. If you use App Store Server Notifications for auto-renewable subscriptions, you can verify the status of the person's subscription in real time, or use the Subscription Status API to identify subscription status.
>
> Use showManageSubscriptions in iOS 15 and iPadOS 15, or later, or provide this link to let people manage their subscriptions: https://apps.apple.com/account/subscriptions/. For tvOS, provide onscreen instructions to change or cancel a subscription, as described in the Apple TV User Guide.
>
> You can also use beginRefundRequest in iOS 15 and iPadOS 15, or later, or provide this Apple Support link to let customers submit refund requests: https://support.apple.com/118223.
>
> Additionally, you can offer to schedule account deletion for a later date, aligned with the subscription's expiration, as long as there's also an option to delete the account immediately.
>
> Related App Review Guidelines Manage Accounts

**Applies to:** Apps that support account creation (individual checks note narrower conditions: Sign in with Apple, guest accounts, user-generated content, auto-renewable subscriptions)

- **[HELP-101]** If the app is not in a highly regulated industry, does deletion avoid requiring a phone call, email, chat support, or other support flow?
  - quote: "Apps not operating in highly regulated industries should not require people to make a phone call, send an email, use a chat support flow, or go through other support flows."
  - surface: runtime
  - verify: Run the deletion flow. Fail if it ends in `mailto:`, `tel:`, a chat widget (Intercom, Zendesk and similar) or a "contact support" instruction, unless the app is in a 5.1.1(ix) regulated industry. In code, grep the deletion handler for `mailto:` / `tel:`.
  - fix: Replace the support-based step with a self-service deletion flow.
- **[HELP-102]** Is the deletion flow free of unnecessary difficulty (confirmation and reauthentication steps are allowed)?
  - quote: "apps that make it unnecessarily difficult for someone to delete their account will not pass review."
  - surface: runtime
  - verify: Count the steps from the deletion entry point to completion. Confirmation and identity checks (such as a code sent to the existing email or phone) are fine. Flag retention mazes, repeated prompts and forced surveys.
  - fix: Remove the steps that are not needed.
- **[HELP-103]** If the app supports Sign in with Apple, does account deletion revoke user tokens through the Sign in with Apple REST API?
  - quote: "Apps that support Sign in with Apple should use the Sign in with Apple REST API to revoke user tokens."
  - surface: code
  - verify: If `ASAuthorizationAppleIDProvider` or a "Sign in with Apple" entitlement (`com.apple.developer.applesignin`) is present, confirm the deletion path (app or backend) calls `POST https://appleid.apple.com/auth/revoke` with the user's refresh or access token. Firebase `Auth.auth().revokeToken(withAuthorizationCode:)` and similar wrappers count.
  - fix: Store the authorization code or refresh token at sign-in, and call the revoke endpoint during deletion.
- **[HELP-104]** If the app supports Sign in with Apple, are server-to-server notification endpoints used to process changes for Sign in with Apple accounts?
  - quote: "Use server-to-server notification endpoints to process changes for Sign in with Apple accounts."
  - surface: code
  - verify: Check the Apple Developer portal (Certificates, Identifiers & Profiles > the App ID or Services ID > Sign in with Apple > Server-to-Server Notification Endpoint) for a configured URL, and check that the backend has a handler for `account-delete` / `consent-revoked` events.
  - fix: Configure the endpoint and handle the notification events on the server.
- **[HELP-105]** If the developer is based in the Republic of Korea, was a server-to-server notification endpoint provided when registering a new Services ID?
  - quote: "developers based in the Republic of Korea must provide a server‑to‑server notification endpoint when registering a new Services ID."
  - surface: manual
  - verify: Confirm the developer's location, then confirm the Services ID configuration in the Apple Developer portal includes the endpoint.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-106]** If account creation happens in the default web browser, does the app still offer account deletion within the app?
  - quote: "If my app links out to the default web browser for account creation, does it still need to offer account deletion within the app?"
  - surface: code
  - verify: grep for sign-up links opened in the browser (`UIApplication.shared.open` / SwiftUI `openURL` / `Link` to register or sign-up URLs). If found, confirm an in-app deletion flow still exists (see HELP-93).
  - fix: Add in-app account deletion.
- **[HELP-107]** Does the app avoid linking out to the default web browser to sign in or register an account?
  - quote: "linking out to the default web browser to sign in or register an account provides a poor user experience and isn't appropriate"
  - surface: code
  - verify: grep for `UIApplication.shared.open`, `openURL` and `Link(destination:)` with login, sign-in, register or sign-up URLs. Confirm sign-in and registration happen in the app instead (native UI, or `ASWebAuthenticationSession` / `SFSafariViewController` for OAuth).
  - fix: Move sign-in and registration into the app.
- **[HELP-108]** If the app automatically creates accounts (guest accounts), can people delete those accounts and their data?
  - quote: "People should have the option to delete automatically generated accounts"
  - surface: code
  - verify: Look for automatic or anonymous account creation (`signInAnonymously`, device-ID accounts, auto-provisioned backend users). If found, confirm the deletion option is available to guest users too, and that it removes their data.
  - fix: Expose account deletion to guest accounts.
- **[HELP-109]** If deletion is manual or takes time, does the app say how long it will take and confirm when it is complete?
  - quote: "Inform the person how long it will take to delete the account and provide a confirmation when the deletion is complete."
  - surface: runtime
  - verify: Run the deletion flow and confirm a timeframe is shown, then confirm a completion notice (email or in-app) is sent once deletion is processed.
  - fix: Add the timeframe message and a completion confirmation.
- **[HELP-110]** In apps that display and share user-generated content, does account deletion also delete the user's shared content (photos, videos, text posts, reviews)?
  - quote: "This includes user-generated content that's shared with others, such as photos, videos, text posts, and reviews."
  - surface: code
  - verify: Trace the backend deletion: confirm it removes the user's posts, media in storage buckets, comments and reviews, and doesn't only anonymize the profile, unless the law requires keeping some of it (and the user is told).
  - fix: Extend the deletion to the user-generated content, and disclose any data that must be kept.
- **[HELP-111]** Is account deletion available to everyone, regardless of where they are located?
  - quote: "Everyone should be able to delete their accounts, regardless of where they're located."
  - surface: code
  - verify: Check the deletion UI and backend for region gating (`Locale.current.region`, storefront or country checks, GDPR/CCPA-only flags) that hides deletion in some locations.
  - fix: Remove the region gating so the deletion flow is available everywhere.
- **[HELP-112]** If a person has an auto-renewable subscription, does the deletion flow tell them billing will continue through Apple and ask them to cancel before continuing?
  - quote: "notify them that billing will continue through Apple and ask them to cancel their subscription before continuing."
  - surface: runtime
  - verify: With a sandbox account that has an active subscription, start deletion and confirm the notice appears with a way to manage the subscription (`showManageSubscriptions(in:)` / `.manageSubscriptionsSheet` or the https://apps.apple.com/account/subscriptions/ link; onscreen instructions on tvOS).
  - fix: Check the subscription status (`Product.SubscriptionInfo.status` / `Transaction.currentEntitlements`) at the start of deletion, then show the notice and a manage-subscriptions action.
- **[HELP-113]** If account deletion can be scheduled for a later date (aligned with the subscription's expiration), is there also an option to delete the account immediately?
  - quote: "as long as there's also an option to delete the account immediately."
  - surface: runtime
  - verify: If the flow offers scheduled deletion, confirm an immediate-deletion choice is also shown.
  - fix: Add an immediate-deletion option next to the scheduled one.

## HELP.37 5.1.1(ii) - Write clear purpose strings

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings

**Source text (verbatim):**
> Apple operating systems restrict access to protected data and resources by default, so before your app can access resources like the camera, location, microphone, or health data, it has to request permission. These requests often include a purpose string, also called a usage description, that explains how your app will use the requested data or resource.
>
> App Review Guideline 5.1.1(ii) specifies requirements for purpose strings:
>
> 5.1.1(ii) Permission
>
> [...] Ensure your purpose strings clearly and completely describe your use of the data. [...]
>
> This requirement allows users to make an informed decision about whether or not to grant your app access.

**Applies to:** Apps that request access to protected data or resources

- **[HELP-114]** Does every purpose string clearly and completely describe the app's use of the data?
  - quote: "Ensure your purpose strings clearly and completely describe your use of the data."
  - surface: code
  - verify: Collect all `NS*UsageDescription` keys from every target's Info.plist and `INFOPLIST_KEY_NS*UsageDescription` build settings in project.pbxproj (including extensions and the Watch app). Read each value and confirm it says what data is used and for what.
  - fix: Rewrite each string to state the specific use.

## HELP.38 Best practices for purpose strings

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings

**Source text (verbatim):**
> A purpose string that only restates the name of the resource, or promises a general benefit without saying what your app actually does, doesn't meet the requirement.
>
> ### Explain specifically how your app will use the data.
>
> #### Do
>
> - Name the specific feature or outcome the data makes possible.
> - Write a separate purpose string for every protected resource your app requests.
>
> #### Don't
>
> - Don't obscure who has access to data behind a vague benefit or a passive construction, such as, "Your data will be used to provide a better experience."
> - Don't restate the name of the resource without explaining its use.
>
> ### Provide an example of how the data will be used.
>
> #### Do
>
> - Give a concrete example of what your app does with the data.
> - Write one brief, complete sentence in active voice and sentence case, ending with a period.
>
> #### Don't
>
> - Don't fill the request with marketing copy or a full feature list.
>
> Insufficient examples
>
> Clear and specific examples
>
> "To use location."
>
> "The app uses location data to determine the recommended route to your destination and provide turn-by-turn directions."
>
> "Your data will be used to provide a better experience."
>
> "The app uses tracking data to deliver personalized advertising for products that are most relevant to you."

**Applies to:** Apps that request access to protected data or resources

- **[HELP-115]** Does each purpose string do more than restate the resource name or promise a general benefit?
  - quote: "A purpose string that only restates the name of the resource, or promises a general benefit without saying what your app actually does, doesn't meet the requirement."
  - surface: code
  - verify: For each `NS*UsageDescription` value, fail strings like "To use location.", "Camera access", "Needed for the app" or "To improve your experience".
  - fix: Rewrite the string to describe what the app actually does with the data.
- **[HELP-116]** Does each purpose string name the specific feature or outcome the data makes possible?
  - quote: "Name the specific feature or outcome the data makes possible."
  - surface: code
  - verify: Confirm each `NS*UsageDescription` value names a concrete feature (for example "scan documents", "turn-by-turn directions").
  - fix: Name the feature in the string.
- **[HELP-117]** Is there a separate purpose string for every protected resource the app requests?
  - quote: "Write a separate purpose string for every protected resource your app requests."
  - surface: code
  - verify: Map the APIs used to the required keys and confirm each key is present with its own text. Examples: `CLLocationManager` → `NSLocationWhenInUseUsageDescription` / `NSLocationAlwaysAndWhenInUseUsageDescription`; `AVCaptureDevice` video → `NSCameraUsageDescription`; audio → `NSMicrophoneUsageDescription`; `PHPhotoLibrary` → `NSPhotoLibraryUsageDescription` / `NSPhotoLibraryAddUsageDescription`; `CNContactStore` → `NSContactsUsageDescription`; `EKEventStore` → `NSCalendarsFullAccessUsageDescription` / `NSRemindersFullAccessUsageDescription`; `HKHealthStore` → `NSHealthShareUsageDescription` / `NSHealthUpdateUsageDescription`; `SFSpeechRecognizer` → `NSSpeechRecognitionUsageDescription`; `ATTrackingManager` → `NSUserTrackingUsageDescription`; `CBCentralManager` → `NSBluetoothAlwaysUsageDescription`; `CMMotionManager` → `NSMotionUsageDescription`; `NFCReaderSession` → `NFCReaderUsageDescription`; `LAContext` Face ID → `NSFaceIDUsageDescription`; local network → `NSLocalNetworkUsageDescription`.
  - fix: Add the missing keys, each with its own specific text.
- **[HELP-118]** Do purpose strings avoid hiding who has access to data behind a vague benefit or a passive construction?
  - quote: "Don't obscure who has access to data behind a vague benefit or a passive construction"
  - surface: code
  - verify: Flag values using passive phrases such as "will be used", "is used to improve" or "to provide a better experience".
  - fix: Rewrite in active voice, naming the app as the actor ("The app uses …").
- **[HELP-119]** Does each purpose string give a concrete example of what the app does with the data?
  - quote: "Give a concrete example of what your app does with the data."
  - surface: code
  - verify: Confirm each `NS*UsageDescription` value contains a concrete example of use (compare the "Clear and specific examples" in the source).
  - fix: Add a concrete example to the string.
- **[HELP-120]** Is each purpose string one brief, complete sentence in active voice and sentence case, ending with a period?
  - quote: "Write one brief, complete sentence in active voice and sentence case, ending with a period."
  - surface: code
  - verify: For each value (base language and every localization), check that it is a single sentence, starts with a capital letter, is not Title Case or all caps, ends with ".", and is in active voice.
  - fix: Rewrite the string to match.
- **[HELP-121]** Are purpose strings free of marketing copy and full feature lists?
  - quote: "Don't fill the request with marketing copy or a full feature list."
  - surface: code
  - verify: Flag long values, lists of features, or promotional wording in `NS*UsageDescription` values.
  - fix: Cut the string down to one specific use.

## HELP.39 Purpose strings FAQs

**Source page:** https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings

**Source text (verbatim):**
> ### Do purpose strings need to be localized?
>
> Yes. If your app supports localizations for a global audience, you must provide localized purpose strings. Set your app to each localization and test to confirm the correct localized text appears in the permission request. Learn more about app localization.
>
> ### A third-party SDK in my app requests permissions. Am I responsible for its purpose strings?
>
> Yes. As stated in the App Review Guidelines and the Apple Developer Program License Agreement, you're responsible for everything in your app, including SDKs, libraries, and other code from third parties. SDKs can reference APIs that access protected resources such as location, sometimes without your realizing it. If your app has a valid reason to access a resource, define a purpose string on the Info.plist that describes your app's specific use case. If it doesn't, remove references to those APIs from your app's binary. Familiarize yourself with the resources an SDK may try to access before you submit.
>
> Related App Review Guideline 5.1.1 Requesting access to protected resources Human Interface Guidelines: Privacy Provide information for a complete review

**Applies to:** Apps that request access to protected resources (localization checks: apps that support localizations; SDK checks: apps that include third-party SDKs)

- **[HELP-122]** If the app supports localizations, are localized purpose strings provided?
  - quote: "If your app supports localizations for a global audience, you must provide localized purpose strings."
  - surface: code
  - verify: List the app's localizations (`knownRegions` in project.pbxproj, the `*.lproj` folders). For each one, confirm every `NS*UsageDescription` key has a translation in `InfoPlist.strings` or `InfoPlist.xcstrings` (no missing or untranslated entries).
  - fix: Add an `InfoPlist.xcstrings` catalog (or `InfoPlist.strings` per language) with translations for each key.
- **[HELP-123]** In each localization, does the correct localized text appear in the permission request?
  - quote: "Set your app to each localization and test to confirm the correct localized text appears in the permission request."
  - surface: runtime
  - verify: For each language, run the app with that language (Scheme > Run > Options > App Language, or `-AppleLanguages (xx)`), reset permissions (`xcrun simctl privacy booted reset all <bundle-id>`), trigger each permission prompt, and check the text.
  - fix: Fix the missing or incorrect translations.
- **[HELP-124]** For protected-resource APIs referenced by third-party SDKs, is there either a purpose string describing the app's specific use (if the app has a valid reason) or have the API references been removed from the binary?
  - quote: "If your app has a valid reason to access a resource, define a purpose string on the Info.plist that describes your app's specific use case."
  - surface: code
  - verify: Build the release archive and inspect the main binary and embedded frameworks for protected API symbols (`nm -u` / `strings` for `CLLocationManager`, `AVCaptureDevice`, `PHPhotoLibrary`, `CNContactStore`, `EKEventStore`, `ATTrackingManager`, `CBCentralManager`, and so on). For each symbol, confirm a matching `NS*UsageDescription` exists (HELP-117) or flag it.
  - fix: Add a specific purpose string for each valid use (see HELP-125 for unneeded ones).
- **[HELP-125]** If the app has no valid reason to access a resource that an SDK references, have those API references been removed from the binary?
  - quote: "If it doesn't, remove references to those APIs from your app's binary."
  - surface: code
  - verify: For each protected API symbol found in HELP-124 that has no app use case, confirm it is gone from the rebuilt binary.
  - fix: Remove or replace the SDK (or the SDK module or subspec) that references the unused API, or configure the SDK to exclude it, then rebuild and re-check.

## HELP.40 Respond to an app removal

**Source page:** https://developer.apple.com/help/app-review/safe-and-trusted-store/app-removals

**Source text (verbatim):**
> Apps may be removed from distribution if they fail to follow the App Review Guidelines, the Apple Developer Program License Agreement, or applicable law.
>
> This can happen when:
>
> - The app includes hidden features or has been modified after approval, such as through a server-side change, in a way that introduces a violation.
> - Users report issues that did not occur during review.
> - Apple receives a legal, intellectual property, or government takedown request.
>
> If App Review confirms an issue with a live version of your app, you'll receive a message in App Store Connect describing the issue and the rules that were violated.
>
> ## Removal deadlines
>
> Depending on the severity of the issues, you may be given additional time to resolve them before the app is removed from distribution:
>
> - Apps with less severe issues may be given 14 days to resolve the issue. If App Review doesn't receive a compliant update submission within the resolution window, the app will be removed.
> - Apps with serious issues, such as safety or legal concerns, may be immediately removed. You must submit a compliant update to restore a removed app.
> - Apps with a fundamentally incompatible concept, such as one designed to deliver objectionable content, are removed immediately and can't be restored. Developers must submit a new app with a compatible concept.
>
> If you have questions or additional information to provide, reply to the removal message in App Store Connect. Learn more about contacting App Review for help.
>
> Note: Developers with apps that haven't been updated within the last three years and fail to meet a minimal download threshold will receive an App Store Improvements notice, notifying them to submit an update within 90 days or the app will be removed. Learn more about App Store Improvements.
>
> Related Appeal to the App Review Board Track a submission's review status

**Applies to:** All apps (removal-response checks: apps that received a removal message)

- **[HELP-126]** Is the app free of hidden features, and of changes after approval (such as server-side changes) that introduce a violation?
  - quote: "The app includes hidden features or has been modified after approval, such as through a server-side change, in a way that introduces a violation."
  - surface: code
  - verify: Inventory the remote-controlled behavior: remote config keys (Firebase Remote Config, LaunchDarkly, custom JSON flags), server-driven UI, and WebViews loading remote content that can change features. For each, confirm the reviewed build and server state show the same functionality users will get, and that no flag turns on unreviewed features.
  - fix: Remove the hidden or flag-gated features, or disclose them and make them available during review. Resubmit before changing functionality.
- **[HELP-127]** If the app received a removal notice with a resolution window, was a compliant update submitted within it (14 days for less severe issues)?
  - quote: "If App Review doesn't receive a compliant update submission within the resolution window, the app will be removed."
  - surface: manual
  - verify: Check App Store Connect messages for a removal notice and its deadline, and confirm a compliant update was submitted before it.
  - fix: manual — requires developer decision/legal/business action.
- **[HELP-128]** If the app was removed for serious issues, has a compliant update been submitted to restore it?
  - quote: "You must submit a compliant update to restore a removed app."
  - surface: manual
  - verify: Confirm a compliant update addressing the cited issues is submitted in App Store Connect.
  - fix: manual — requires developer decision/legal/business action.

## HELP.41 App Store Improvements

**Source page:** https://developer.apple.com/help/app-review/safe-and-trusted-store/app-store-improvements

**Source text (verbatim):**
> To help the App Store remain a safe and trusted place to discover and download apps, Apple has an ongoing evaluation process that removes apps that no longer function as intended, don't follow current review guidelines, or are outdated.
>
> ## Benefits of this process
>
> Since 2016, App Store Improvements has delivered real benefits for users and developers, including:
>
> - Discoverability. Removing outdated apps helps people find the right apps more easily and improves discoverability for active developers.
> - Security and privacy. We continually update Apple hardware and software to help developers enhance performance, security, and privacy. Keeping your apps up to date helps safeguard user security.
> - User experience. Keeping apps up to date to align with modern screen sizes, SDKs, APIs, and additional features ensures users can have a great experience with any app they get from the App Store.
>
> ## What to expect
>
> Apps in all categories on the App Store are evaluated to make sure they function as expected, follow current App Review Guidelines, and are up to date:
>
> - If your app has an issue, App Review will contact you to request the changes needed to keep your app available on the App Store.
> - Developers who have apps that haven't been updated within the last three years and fail to meet a minimal download threshold — meaning the app has not been downloaded at all or extremely few times during a rolling 12-month period — will receive a message from App Review in App Store Connect notifying them that their app has been identified for possible removal from the App Store.
>
> ## FAQs
>
> ### How long do I have to make changes?
>
> If your app has been identified for removal because it hasn't been updated in three years and doesn't meet the download threshold, you'll be asked to submit an update within 90 days. If you're unable to make the changes within this time frame, your app will be removed from the App Store until you submit an update and it's approved. There's no time limit in which a developer can submit an app after it has been removed from the App Store for this process, as long as the developer still has an active membership in the Apple Developer Program. Please note that apps that crash on launch will be removed immediately.
>
> Apple always wants to help developers get and keep quality software on the App Store. That's why developers can appeal app removals.
>
> ### If my app is removed, will my app's name become available for other developers to use?
>
> No. When apps are removed from the App Store, they aren't deleted from your account. Your app name will continue to be associated with your app.
>
> ### If my app is removed, will current users be able to access it?
>
> Yes. Your app will remain fully functional for current users. They will not experience any service interruptions and can continue to make in-app purchases. However, we recommend that you update your app as soon as possible to reinstate it on the App Store and ensure that it remains functional and engaging for both new and existing customers.
>
> Related Respond to an app removal Create a new version

**Applies to:** All apps on the App Store (update check: apps identified for removal under App Store Improvements)

- **[HELP-129]** Does the app launch without crashing?
  - quote: "Please note that apps that crash on launch will be removed immediately."
  - surface: runtime
  - verify: Install the release (archive or TestFlight) build on a clean device or simulator for each supported platform and OS, launch it cold (first launch, signed out, no network, and with network), and check Xcode Organizer > Crashes for launch crashes.
  - fix: Fix the launch crash before submitting.
- **[HELP-130]** If the app was identified for removal under App Store Improvements, was an update submitted within 90 days?
  - quote: "you'll be asked to submit an update within 90 days."
  - surface: manual
  - verify: Check App Store Connect messages for an App Store Improvements notice. If there is one, confirm an update was submitted before the deadline.
  - fix: manual — requires developer decision/legal/business action.

## HELP.42 Report an app

**Source page:** https://developer.apple.com/help/app-review/safe-and-trusted-store/report-an-app

**Source text (verbatim):**
> If you believe an app presents a trust or safety concern, or otherwise doesn't meet the App Review Guidelines and Apple Developer Program License Agreement, you can report it to App Review for investigation. App Review takes every report seriously and works directly with the app's developer if a violation is confirmed.
>
> There are two ways to report an app to App Review:
>
> - Use the Report an app form.
> - If you're already corresponding with App Review about your own app and want to raise a concern about another app, you can include it in your reply to App Review.
>
> Note: Just as App Review wouldn't discuss your app with someone else, App Review can't share the outcome of an investigation into another developer's app with you.
>
> ## What to include in your report
>
> #### Do
>
> - Provide identifying information for the app you're reporting, such as a product page App Store URL, a recruitment link for a TestFlight app, or an app ID for apps available through alternative distribution.
> - Describe specifically what you observed and why you believe it's a concern. Cite the App Review Guidelines you believe the app doesn't meet.
> - Provide detailed steps to reproduce the issue. If it occurs outside the app, describe how to observe it.
> - Include links to any related websites or content.
>
> #### Don't
>
> - Don't file a report to check the status of a previous report.
> - Don't expect reporting another app to change the outcome of your app's review. All apps are reviewed against the App Review Guidelines and Apple Developer Program License Agreement.
>
> Related Contact App Review for help with a submission 4.1 - Preventing copycat and impersonation rejections

**Applies to:** Developers reporting another app

- **[HELP-131]** Does the report give identifying information for the app, a specific description citing the guidelines, detailed reproduction steps, and related links?
  - quote: "Provide identifying information for the app you're reporting, such as a product page App Store URL, a recruitment link for a TestFlight app, or an app ID for apps available through alternative distribution."
  - surface: manual
  - verify: Review the report draft for the app identifier, the observation with cited guidelines, the repro steps, and the links.
  - fix: manual — requires developer decision/legal/business action.

## Sources

- https://developer.apple.com/help/app-review/
- https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review
- https://developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases
- https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices
- https://developer.apple.com/help/app-review/before-submitting-for-review/app-review-appointment
- https://developer.apple.com/help/app-review/after-submitting-for-review/review-status
- https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review
- https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review
- https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions
- https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board
- https://developer.apple.com/help/app-review/after-submitting-for-review/improve-guidelines
- https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots
- https://developer.apple.com/help/app-review/guideline-reference/4-1-prevent-copycat-rejection
- https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion
- https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings
- https://developer.apple.com/help/app-review/safe-and-trusted-store/app-removals
- https://developer.apple.com/help/app-review/safe-and-trusted-store/app-store-improvements
- https://developer.apple.com/help/app-review/safe-and-trusted-store/report-an-app
