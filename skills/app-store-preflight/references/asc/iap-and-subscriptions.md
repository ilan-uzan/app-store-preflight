# In-App Purchases and Auto-Renewable Subscriptions — App Store Connect and In-App Requirements
Source: https://developer.apple.com/app-store/subscriptions/ , https://developer.apple.com/in-app-purchase/ , https://developer.apple.com/design/human-interface-guidelines/in-app-purchase (redirects to /apple-in-app-purchase) , https://developer.apple.com/help/app-store-connect/ (In-App Purchase and subscription articles listed under Sources)  
Retrieved: 2026-10-30

Note: the start URL https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/overview-for-configuring-in-app-purchases returned "The page you’re looking for can’t be found." The current page is https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases (linked from the App Store Connect Help sidebar) and is used below.

---

## IAP.CONFIG Overview for configuring In-App Purchases

**Source text (verbatim):**
> In-App Purchases let you offer extra content and features in your apps distributed on the App Store — including digital goods, subscriptions, and premium content — directly within your app on all Apple platforms. To make an In-App Purchase available in multiple platform versions of your app, create a single In-App Purchase under the Distribution tab in App Store Connect, then use StoreKit to implement the In-App Purchase in the various platform versions of your app.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> There are four types of In-App Purchases:
>
> | Type | Description |
> |---|---|
> | Consumable | A product that is used once, after which it becomes depleted and must be purchased again. Example: fish food in a fishing app. |
> | Non-consumable | A product that is purchased once and does not expire or decrease with use. Example: race track for a game app. |
> | Auto-renewable subscriptions | A product that allows users to purchase dynamic content for a set period. This type of Subscription renews automatically unless canceled by the user. Example: Monthly subscriptions for an app offering streaming services. |
> | Non-renewing subscriptions | A product that allows users to access content for a limited duration of time. This type of Subscription does not renew automatically. Example: One year subscription to view live gaming content. |
>
> You can create up to 10,000 In-App Purchase products per app. Every In-App Purchase must be associated with an app and can be shared across multiple platform versions (iOS, macOS, tvOS). In-App Purchases are not shareable between different apps.
>
> Implementing In-App Purchases in your app requires configuration between your apps’ server and Apple’s servers, as well as set up and ongoing management in App Store Connect. The following workflow can be used:
>
> Accept the Paid Apps Agreement
>
> To offer In-App Purchases, the membership Account Holder must accept the Paid Apps Agreement in the Business section of App Store Connect and provide banking and tax information.
>
> Note: The agreement must be Active to test In-App Purchases in the sandbox environment.
>
> Design your In-App Purchase
>
> To ensure your In-App Purchase experience fits well with the rest of your app and effectively showcases your products, review the Human Interface Guidelines and App Review Guidelines.
>
> Configure In-App Purchases in App Store Connect
>
> Create In-App Purchases and add metadata, such as product name, description, price, and availability. You’ll also need to generate In-App Purchase keys and set a tax category, which will allow Apple to calculate the appropriate tax on customer transactions.
>
> Implement StoreKit
>
> Sign your app with a provisioning profile that includes your app's bundle identifier and the In-App Purchase capability. Make sure the bundle identifier and product identifiers in Xcode match those configured for your app and In-App Purchases in App Store Connect.
>
> Test your In-App Purchases
>
> Apple provides a testing environment, called sandbox, which allows you to test In-App Purchases without incurring charges using test accounts. Test each part of your code to verify that you’ve implemented it correctly by using your app to make In-App Purchases.
>
> You can further test your app and In-App Purchases using either TestFlight, or Xcode.
>
> Use App Store Server Notifications
>
> App Store Server Notifications provide near real-time updates about transaction status and key events related to In-App Purchases, such as a refund or a change in subscription status or Family Sharing access. To leverage these notifications, you’ll need to enter URLs for your production and sandbox server environments in App Store Connect.
>
> Submit your In-App Purchases for review
>
> Before you publish your In-App Purchase on the App Store it must be submitted for review. If you’re submitting your first In-App Purchase, you must submit it with a new version of your app. Ensure you aren't missing any required information before submitting. Monitor In-App Purchase statuses to understand if your In-App Purchase is available or if it needs your attention.

**Applies to:** Apps that offer In-App Purchases (any of the four types)
**Requires:** iap, subscriptions

- **[IAP-01]** Has the Account Holder accepted the Paid Apps Agreement and provided banking and tax information, with the agreement showing Active?
  - quote: "the membership Account Holder must accept the Paid Apps Agreement in the Business section of App Store Connect and provide banking and tax information"
  - surface: asc
  - verify: App Store Connect > Business: confirm the Paid Apps Agreement status is Active and banking + tax sections are complete.
  - fix: manual — requires developer decision/legal/business action (Account Holder must accept the agreement and enter banking/tax info).
- **[IAP-02]** Is every In-App Purchase the app sells created in App Store Connect with metadata (product name, description, price, availability)?
  - quote: "Create In-App Purchases and add metadata, such as product name, description, price, and availability."
  - surface: asc
  - verify: Collect all product IDs referenced in code (grep Swift/ObjC for `Product.products(for:`, `SKProductsRequest(productIdentifiers:`, `ProductView(id:`, `SubscriptionStoreView(groupID:`/`productIDs:`, string constants, and any `.storekit` configuration file). In App Store Connect > app > Monetization > In-App Purchases and Subscriptions, confirm each ID exists and has localized name/description, a price, and availability.
  - fix: Create the missing products in App Store Connect and complete their metadata.
- **[IAP-03]** Is a tax category set for the In-App Purchases?
  - quote: "set a tax category, which will allow Apple to calculate the appropriate tax on customer transactions"
  - surface: asc
  - verify: App Store Connect > app > In-App Purchase / subscription detail page > Tax Category (or app-level In-App Purchase tax category setting): confirm a category is selected that matches the content.
  - fix: Select the appropriate tax category in App Store Connect.
- **[IAP-04]** Is the app signed with a provisioning profile that includes the bundle identifier and the In-App Purchase capability?
  - quote: "Sign your app with a provisioning profile that includes your app's bundle identifier and the In-App Purchase capability."
  - surface: code
  - verify: In the Xcode project, open target > Signing & Capabilities and confirm the "In-App Purchase" capability is listed (in project.pbxproj, look for `com.apple.InAppPurchase` under `SystemCapabilities` with `enabled = 1`). Confirm the provisioning profile used for the release build is for the app's bundle identifier (Apple Pay's `com.apple.developer.in-app-payments` entitlement is a different technology and does not satisfy this).
  - fix: Add the In-App Purchase capability in Signing & Capabilities and regenerate/refresh the provisioning profile.
- **[IAP-05]** Do the bundle identifier and every product identifier used in code exactly match those configured in App Store Connect?
  - quote: "Make sure the bundle identifier and product identifiers in Xcode match those configured for your app and In-App Purchases in App Store Connect."
  - surface: code
  - verify: Compare `PRODUCT_BUNDLE_IDENTIFIER` (build settings / Info.plist) to App Store Connect > App Information > Bundle ID. Compare every product ID string in code and in any `.storekit` file to Product IDs in App Store Connect (case-sensitive, character-exact).
  - fix: Correct the mismatched identifiers in code (product IDs cannot be edited in App Store Connect after saving).
- **[IAP-06]** Have the In-App Purchases been tested in the sandbox environment (or StoreKit Testing / TestFlight) before submission?
  - quote: "Test each part of your code to verify that you’ve implemented it correctly by using your app to make In-App Purchases."
  - surface: runtime
  - verify: Run the app with a Sandbox Apple Account (or a StoreKit configuration file in Xcode / a TestFlight build) and complete a purchase of each product type offered, confirming content unlocks.
  - fix: Fix any purchase-flow defects found during sandbox testing.
- **[IAP-07]** If the app relies on App Store Server Notifications (refunds, subscription status, Family Sharing access), are production and sandbox server URLs entered in App Store Connect?
  - quote: "you’ll need to enter URLs for your production and sandbox server environments in App Store Connect"
  - surface: asc
  - verify: App Store Connect > app > App Information > App Store Server Notifications: confirm Production Server URL and Sandbox Server URL are set (if the project has a backend that handles notifications — grep server code for `signedPayload`, `notificationType`, `DID_RENEW`, `REFUND`, `REVOKE`).
  - fix: Enter the URLs for both the production and sandbox server environments in App Store Connect.
- **[IAP-08]** If this is the app's first In-App Purchase, is it being submitted together with a new app version?
  - quote: "If you’re submitting your first In-App Purchase, you must submit it with a new version of your app."
  - surface: asc
  - verify: App Store Connect > app > App Review (submissions) / draft submission: confirm the new IAP and an app version are in the same draft submission.
  - fix: Add the app version to the same submission as the first In-App Purchase (see IAP.SUBMIT).
- **[IAP-09]** Is no required information missing from any In-App Purchase before submission?
  - quote: "Ensure you aren't missing any required information before submitting."
  - surface: asc
  - verify: In App Store Connect, each IAP/subscription status must not indicate missing metadata (status "Prepare for Submission" with required fields empty); open each product and confirm all required fields (reference name, product ID, price, at least one localization, review screenshot) are filled.
  - fix: Fill in the missing fields in App Store Connect.

---

## IAP.TYPES In-App Purchase types

**Source text (verbatim):**
> In-App Purchase types refer to the different types of In-App Purchase options available.
>
> | Column | Description |
> |---|---|
> | Consumable | A product that is used once, after which it becomes depleted and must be purchased again. Example: fish food in a fishing app. |
> | Non-Consumable | A product that is purchased once and does not expire or decrease with use. Example: Race track for a game app. |
> | Auto-Renewable Subscription | A product that allows users to purchase dynamic content for a set period. This type of Subscription renews automatically unless cancelled by the user. Example: Monthly subscriptions for an app offering streaming services. Auto-renewable subscriptions can also support multiseat purchasing, which allows customers to buy multiple seats for a group. Learn how to set purchase options for an auto-renewable subscription. |
> | Non-Renewing Subscription | A product that allows users to purchase a service with a limited duration. The content of this In-App Purchase can be static. This type of Subscription does not renew automatically. Example: One year subscription to a catalog of archived articles. |

**Applies to:** Apps that offer In-App Purchases
**Requires:** iap, subscriptions

- **[IAP-10]** Is each product configured in App Store Connect with the type that matches how the app treats it (used once and depleted = Consumable; purchased once and does not expire = Non-Consumable; renews automatically = Auto-Renewable Subscription; limited duration, does not renew = Non-Renewing Subscription)?
  - quote: "A product that is used once, after which it becomes depleted and must be purchased again."
  - surface: code
  - verify: For each product ID, inspect how the code grants it (e.g. increments a balance = consumable; permanent unlock checked via `Transaction.currentEntitlements` = non-consumable; expiry/renewal logic = subscription). Compare with the product type shown in App Store Connect (Consumable / Non-Consumable listed under In-App Purchases; subscriptions under Subscriptions). Purchase type cannot be edited after creation.
  - fix: If the type is wrong, create a new product of the correct type with a new product ID and update the code.

---

## IAP.CREATE Create consumable or non-consumable In-App Purchases

**Source text (verbatim):**
> To offer In-App Purchases, add In-App Purchase information in App Store Connect. You can enter the metadata when you create your In-App Purchase or enter it later.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> Learn how to create In-App Purchases with the App Store Connect API.
>
> Required role: You must have the Account Holder, Admin, App Manager, Developer, or Marketing role to add and edit In-App Purchases. View role permissions.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases.
> - Click the add button (+).
> - Select Consumable or Non-Consumable. Learn about In-App Purchase types.
> - Add the reference name and product ID, then click Create.

**Applies to:** Apps that offer consumable or non-consumable In-App Purchases
**Requires:** iap

- **[IAP-11]** Does each consumable/non-consumable product have a reference name and product ID in App Store Connect?
  - quote: "Add the reference name and product ID, then click Create."
  - surface: asc
  - verify: App Store Connect > app > Monetization > In-App Purchases: confirm every consumable/non-consumable used by the app is listed with a reference name and product ID.
  - fix: Create the missing product via the add button (+) in App Store Connect.

---

## IAP.INFO In-App Purchase information (field reference)

**Source text (verbatim):**
> General Information
>
> The main In-App Purchase properties identify the product in App Store Connect and in the app.
>
> | Property | Description |
> |---|---|
> | Apple ID | A unique identifier automatically generated for your In-App Purchase when you add the In-App Purchase to your account. |
> | Reference Name | A unique name you give to your In-App Purchase for internal tracking that's not visible to customers, but used in App Store Connect and Sales and Trends reports. The reference name can include any characters and can be as long as 64 characters. The reference name can be edited at any time without review. |
> | Product ID | A unique ID specific to your app that you can assign to your In-App Purchases to uniquely identify them within your app. The product ID can contain letters, numbers, hyphens, periods, and underscores, and can be as long as 100 characters. You need separate identifiers for In-App Purchases in your iOS apps and your macOS apps. When your app uses StoreKit to communicate with the App Store, it uses product IDs to retrieve the configuration data you provided for each In-App Purchase. When a user wants to make a purchase, your app identifies the In-App Purchase using its product ID. The product ID isn't editable after you save the In-App Purchase. Once a product ID is assigned to an In-App Purchase, it can't be reused for another In-App Purchase within the same app, even if you delete the original In-App Purchase with that ID. |
> | Review Notes | Additional information about the In-App Purchase that might help Apple review the submission, such as test user accounts and passwords. Review notes should not exceed 4000 characters. |
> | Image | An image is required if you want to promote your In-App Purchase on your App Store product page or set up win-back offers. This image will represent your In-App Purchase in all countries or regions where your app is available. If you’re also using offer codes for auto-renewable subscriptions, your promotional image will appear on the App Store page when customers redeem their codes on iOS 14 or later. Your promotional image must meet the following requirements: - JPG or PNG. - Dimensions of 1024 x 1024 pixels. - 72 dpi, RGB, flattened and no rounded corners. |
> | Show to all App Store users, even those who don’t have the app installed | An indication that you'd like all customers to locate your promoted In-App Purchases, which is based on the user device information. By default, this is selected. If you deselect the checkbox, but haven’t implemented the SKProductStorePromotionController API, your In-App Purchase will not be visible on the App Store. Visit Promote In-App Purchases to relevant customers only. Note that a customer needs to have opened your app on their device at least once to locate your order and visibility settings inside your app. |
> | App Review Screenshot | A screenshot of the In-App Purchase that clearly shows the item or service being offered. This screenshot is used for review only and isn't displayed on the App Store. Upload a screenshot that meets any of the screenshot specifications your app supports. Once you’ve uploaded a screenshot, you can update it but not remove it. |
>
> Localizable information
>
> Add localizable In-App Purchases information used in the product display. You must include these properties for at least one language. For a list of languages, visit App Store localizations.
>
> Changes to the localized information require review. The existing text displays on the store until the new text is approved. The change has its own status separate from the overall status of the In-App Purchase. Before your changes are reviewed, you can revert the change.
>
> | Property | Description |
> |---|---|
> | Display Name | The name of the In-App Purchase that is displayed to customers. The display name must be at least two characters and no more than 30 characters. |
> | Description | A description of the In-App Purchase that potentially displays to users. If you make your In-App Purchase available for promotion, this displays under your In-App Purchase name on the App Store. The description must be no more than 45 characters. |

Field limits (verbatim values from the tables above):

| Field | Limit (verbatim) |
|---|---|
| Reference Name | "can include any characters and can be as long as 64 characters" |
| Product ID | "can contain letters, numbers, hyphens, periods, and underscores, and can be as long as 100 characters" |
| Review Notes | "should not exceed 4000 characters" |
| Image | "JPG or PNG." / "Dimensions of 1024 x 1024 pixels." / "72 dpi, RGB, flattened and no rounded corners." |
| Display Name | "must be at least two characters and no more than 30 characters" |
| Description | "must be no more than 45 characters" |

**Applies to:** All In-App Purchases (General Information); Image applies when promoting an In-App Purchase or setting up win-back offers
**Requires:** iap, subscriptions

- **[IAP-12]** Is each reference name at most 64 characters?
  - quote: "can be as long as 64 characters"
  - surface: asc
  - verify: App Store Connect > each In-App Purchase/subscription > Reference Name: count characters.
  - fix: Shorten the reference name (editable at any time without review).
- **[IAP-13]** Does each product ID contain only letters, numbers, hyphens, periods, and underscores and is it at most 100 characters?
  - quote: "The product ID can contain letters, numbers, hyphens, periods, and underscores, and can be as long as 100 characters."
  - surface: code
  - verify: Grep all product ID strings in code / `.storekit` files and test each against regex `^[A-Za-z0-9._-]{1,100}$`; cross-check in App Store Connect.
  - fix: For a new product, choose a compliant ID. Existing product IDs aren't editable — create a new product with a compliant ID and update code.
- **[IAP-14]** Does every new product use a product ID that was never assigned to another In-App Purchase in this app, including deleted ones?
  - quote: "it can't be reused for another In-App Purchase within the same app, even if you delete the original In-App Purchase with that ID"
  - surface: code
  - verify: For each product ID in code that does not yet exist in App Store Connect, confirm it is not the ID of a previously deleted In-App Purchase of this app (ask the developer / check git history for removed product IDs); a developer plan to "recreate" a deleted product under the same ID fails.
  - fix: Use a new, never-used product ID for the replacement product and update code.
- **[IAP-15]** If the app ships for both iOS and macOS as separate apps, are separate product identifiers used for the iOS app and the macOS app?
  - quote: "You need separate identifiers for In-App Purchases in your iOS apps and your macOS apps."
  - surface: asc
  - verify: If there are separate iOS and macOS app records, confirm the products in each record have distinct product IDs; inspect each target's product ID constants in code.
  - fix: Create distinct product IDs per app record and reference them per target.
- **[IAP-16]** Do Review Notes contain information that helps App Review (for example test accounts and passwords where needed) and stay within 4000 characters?
  - quote: "Additional information about the In-App Purchase that might help Apple review the submission, such as test user accounts and passwords. Review notes should not exceed 4000 characters."
  - surface: asc
  - verify: App Store Connect > each In-App Purchase > Review Information > Review Notes: confirm content is present when the IAP needs login/setup to reach, and length ≤ 4000 characters.
  - fix: Add concise review notes (including demo credentials if a login is needed) under 4000 characters.
- **[IAP-17]** Does every In-App Purchase have an App Review Screenshot that clearly shows the item or service being offered?
  - quote: "A screenshot of the In-App Purchase that clearly shows the item or service being offered."
  - surface: asc
  - verify: App Store Connect > each In-App Purchase/subscription > Review Information > Screenshot: confirm an image is uploaded and it shows the purchase UI for that product.
  - fix: Capture a screenshot of the in-app purchase screen showing the product and upload it.
- **[IAP-18]** Does the App Review Screenshot meet one of the screenshot specifications the app supports?
  - quote: "Upload a screenshot that meets any of the screenshot specifications your app supports."
  - surface: asc
  - verify: Check the uploaded screenshot's pixel dimensions against the App Store screenshot specifications for a device family the app supports.
  - fix: Re-capture on a supported device/simulator size and upload.
- **[IAP-19]** If the In-App Purchase is promoted on the App Store or used for win-back offers, is an image uploaded that is JPG or PNG, 1024 x 1024 pixels, 72 dpi, RGB, flattened, with no rounded corners?
  - quote: "An image is required if you want to promote your In-App Purchase on your App Store product page or set up win-back offers."
  - surface: asc
  - verify: App Store Connect > In-App Purchase > Image section (and Promote on App Store setting). Download the image and check format (`file`/`sips -g pixelWidth -g pixelHeight -g dpiWidth -g space -g hasAlpha`).
  - fix: Export a flattened 1024x1024 72-dpi RGB JPG/PNG with square corners and upload it.
- **[IAP-20]** If "Show to all App Store users, even those who don’t have the app installed" is deselected, has the app implemented the SKProductStorePromotionController API?
  - quote: "If you deselect the checkbox, but haven’t implemented the SKProductStorePromotionController API, your In-App Purchase will not be visible on the App Store."
  - surface: code
  - verify: In App Store Connect, check the checkbox state for promoted IAPs. If deselected, grep the project for `SKProductStorePromotionController`.
  - fix: Either re-select the checkbox in App Store Connect or implement `SKProductStorePromotionController` visibility/order handling.
- **[IAP-21]** Does each In-App Purchase include localizable information (Display Name and Description) for at least one language?
  - quote: "You must include these properties for at least one language."
  - surface: asc
  - verify: App Store Connect > each In-App Purchase > App Store Localization: confirm at least one localization with Display Name and Description.
  - fix: Add a localization with Display Name and Description.
- **[IAP-22]** Is each localized Display Name at least two and no more than 30 characters?
  - quote: "The display name must be at least two characters and no more than 30 characters."
  - surface: asc
  - verify: Count characters of every localized Display Name in App Store Connect (or in the `.storekit` file's `displayName` values if mirrored).
  - fix: Edit the display name to 2–30 characters (requires review).
- **[IAP-23]** Is each localized Description no more than 45 characters?
  - quote: "The description must be no more than 45 characters."
  - surface: asc
  - verify: Count characters of every localized Description in App Store Connect.
  - fix: Shorten the description to ≤ 45 characters (requires review).

---

## IAP.EDIT View and edit In-App Purchase information — image and App Review information

**Source text (verbatim):**
> You can edit most metadata elements for your In-App Purchases, except for the product ID and purchase type. If your In-App Purchase was never submitted to Apple for review, you can make changes to its metadata. However, if your In-App Purchase was already submitted, some changes require approval by App Review.
>
> Add or remove an Image
>
> To promote your In-App Purchase on your App Store product page, set up win-back offers or Contingent Pricing, or display your offer codes and payment sheet, you must provide an image. This image represents your In-App Purchase in all countries or regions where your product is available. Your image must meet the following requirements:
> - JPG or PNG
> - Dimensions of 1024 x 1024 pixels.
> - 72 dpi, RGB, flattened and no rounded corners.
>
> To add or remove your image:
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, then scroll down to Non-Renewing Subscriptions and click Manage.)
> - Click the In-App Purchase you want to modify.
> - Scroll down to the Image section.
> - To add an image, click Choose File and upload the image. To delete an image, move your pointer over it and click the remove icon (—).
>
> When you're ready, submit your In-App Purchase for review. Your Image must be approved by App Review before it will appear on the App Store.
>
> Add App Review information
>
> When submitting your In-App Purchase for review, include review notes and a screenshot to help Apple's review process. This information is for Apple’s review only and isn’t displayed on the App Store. You can change it before you submit to App Review, or if your In-App Purchase is rejected.
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, then scroll down to Non-Renewing Subscriptions and click Manage.)
> - Click the In-App Purchase you want to view or edit.
> - Scroll down to the Review Information section.
> - Click Choose File to upload your image.
> - Add information under Review Notes, then click Save.

**Applies to:** All In-App Purchases being submitted for review; Image applies to promotion, win-back offers, Contingent Pricing, offer codes and payment sheet display
**Requires:** iap, subscriptions

- **[IAP-24]** If the In-App Purchase is promoted on the product page, used for win-back offers or Contingent Pricing, or used to display offer codes and the payment sheet, does it have an image uploaded (and approved before it appears on the App Store)?
  - quote: "To promote your In-App Purchase on your App Store product page, set up win-back offers or Contingent Pricing, or display your offer codes and payment sheet, you must provide an image."
  - surface: asc
  - verify: For each IAP/subscription used with promotion, win-back offers, Contingent Pricing, or offer codes, open App Store Connect > product > Image section; confirm an image is present and its status is approved.
  - fix: Upload a compliant image (see IAP-19) and submit it for review.
- **[IAP-25]** When submitting the In-App Purchase, are both review notes and a review screenshot included in Review Information?
  - quote: "When submitting your In-App Purchase for review, include review notes and a screenshot to help Apple's review process."
  - surface: asc
  - verify: App Store Connect > each In-App Purchase > Review Information: Screenshot uploaded and Review Notes filled.
  - fix: Upload a screenshot and add review notes, then Save.

---

## IAP.SUBMIT Submit an In-App Purchase

**Source text (verbatim):**
> You can submit In-App Purchases and subscriptions for review directly from the In-App Purchases and Subscriptions sections in App Store Connect. Items you add for review are collected in a submission, which you can submit with or without an app version.
>
> Note: The first consumable, non-consumable, auto-renewable subscription, and non-renewing subscription In-App Purchase of each type must be submitted with a new app version. After the first item of a given type is approved, you can submit additional items of that type without a new app version, as long as your app has at least one approved app version at the time of submission. If your app doesn't have an approved version, include one in your next submission.
>
> Learn how to submit In-App Purchases and subscriptions with the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> Submit an In-App Purchase for the first time
>
> After creating your In-App Purchase or subscription, click Add for Review to add it to a submission. If this is the first time you're submitting that type of In-App Purchase or subscription, include a new app version in the submission. If you're submitting a new subscription it must be submitted together with its subscription group. Each new subscription group must be submitted with at least one of its subscriptions. The app version, subscription group, and every subscription or In-App Purchase you want reviewed together must all be added to the same draft submission before you click Submit for Review.
> - In Apps, select the app you want to view.
> - In the sidebar under Monetization, click In-App Purchases or Subscriptions.
> - Click the In-App Purchase or subscription you want to submit.
> - Click Add for Review. If you have an existing submission, you can add the item to it or click Create New Submission.
> - If your In-App Purchase or subscription requires a new app version, select a platform and the app version to include in your submission. If you're submitting a subscription and the subscription group hasn't been approved yet, add the subscription group to the submission as well. You can add up to 200 items per submission at a time.
> - In the submission modal, review the items in your submission and click Submit for Review.
>
> Once your first consumable or non-consumable In-App Purchase has been approved, you can add additional In-App Purchases of that type without including an app version. The same applies for auto-renewable and non-renewing subscriptions.
>
> Note:
> - In-App Purchases with content hosting can no longer be submitted for review. You can still make changes to their pricing and availability.
> - In-App Purchases and subscriptions aren't supported on Apple Watch. To submit an Apple Watch app version, remove all in-app purchases and subscriptions from the submission.
>
> Add In-App Purchases or subscriptions to an existing submission
>
> You can add multiple In-App Purchases or subscriptions to a submission at the same time from the In-App Purchases or Subscriptions page.
> - In Apps, select the app you want to view.
> - In the sidebar under Monetization, click In-App Purchases or Subscriptions.
> - Click Edit. For subscriptions, first select a group, then click Edit.
> - Select the items you want to submit.
> - Click Add for Review. When you click Add for Review, a dropdown appears if there are any existing draft submissions. Select an existing submission to add an item to it, or click Create New Submission to start a new one.
>
> If any items can't be added to the submission, a banner identifies which items weren't added and includes a link to each item. You can add up to 200 items per submission at a time.
>
> Resolve and resubmit a rejected In-App Purchase or subscription
>
> If App Review rejects one or more items in a submission, you can edit each rejected item and update the submission before resubmitting for review.
> - In Apps, select the app you want to view.
> - In the sidebar, click App Review and open the submission.
> - Review the rejection reason in the Messages section and make the necessary changes by clicking Edit next to the rejected item.
> - Click Save.
> - Click Update Review to update the item in the submission.
> - Repeat steps 3–6 for any other rejected items in the submission, or remove them from the submission.
>
> Once all rejected items are resolved or removed, click Resubmit to App Review.

**Applies to:** All In-App Purchases and subscriptions being submitted for review
**Requires:** iap, subscriptions

- **[IAP-26]** For each IAP type being submitted for the first time (consumable, non-consumable, auto-renewable subscription, non-renewing subscription), is a new app version included in the same submission?
  - quote: "The first consumable, non-consumable, auto-renewable subscription, and non-renewing subscription In-App Purchase of each type must be submitted with a new app version."
  - surface: asc
  - verify: App Store Connect > app > App Review > Drafts: open the draft submission and confirm it contains the app version alongside any IAP whose type has never been approved before.
  - fix: Add the new app version to the draft submission (select platform and version in Add for Review).
- **[IAP-27]** When submitting additional IAPs without an app version, does the app have at least one approved app version?
  - quote: "as long as your app has at least one approved app version at the time of submission"
  - surface: asc
  - verify: App Store Connect > app > Distribution: confirm a version with status Ready for Distribution / previously approved exists.
  - fix: Include an app version in the submission.
- **[IAP-28]** Is each new subscription submitted together with its subscription group, and each new group with at least one of its subscriptions?
  - quote: "If you're submitting a new subscription it must be submitted together with its subscription group. Each new subscription group must be submitted with at least one of its subscriptions."
  - surface: asc
  - verify: In the draft submission, confirm the unapproved subscription group and at least one of its subscriptions are both listed.
  - fix: Add the subscription group (or a subscription of the group) to the same draft submission.
- **[IAP-29]** Are the app version, subscription group, and every subscription/IAP that must be reviewed together in the same draft submission before Submit for Review?
  - quote: "The app version, subscription group, and every subscription or In-App Purchase you want reviewed together must all be added to the same draft submission before you click Submit for Review."
  - surface: asc
  - verify: App Store Connect > App Review > Drafts: list items in the draft and compare with the set of new products the build depends on (product IDs from code that are not yet Approved).
  - fix: Add missing items to the draft submission before submitting.
- **[IAP-30]** Does the submission contain no more than 200 items?
  - quote: "You can add up to 200 items per submission at a time."
  - surface: asc
  - verify: Count items in the draft submission.
  - fix: Split items across multiple submissions.
- **[IAP-31]** Does the submission avoid including In-App Purchases with content hosting?
  - quote: "In-App Purchases with content hosting can no longer be submitted for review."
  - surface: asc
  - verify: For each IAP in the submission, check whether it uses Apple-hosted content (content hosting); also grep code for legacy hosted-content APIs (`SKDownload`, `downloadContentLengths`, `isDownloadable`).
  - fix: manual — requires developer decision/legal/business action (the source only states such items can no longer be submitted; their pricing and availability can still be changed).
- **[IAP-32]** If submitting an Apple Watch app version, are all In-App Purchases and subscriptions removed from that submission?
  - quote: "To submit an Apple Watch app version, remove all in-app purchases and subscriptions from the submission."
  - surface: asc
  - verify: If the draft submission's platform/version is an Apple Watch app version, confirm no IAP or subscription items are in it.
  - fix: Remove IAP/subscription items from the Apple Watch submission and submit them with another platform's version.
- **[IAP-33]** After a rejection, have all rejected items been edited and updated (Update Review) or removed before resubmitting?
  - quote: "Once all rejected items are resolved or removed, click Resubmit to App Review."
  - surface: asc
  - verify: App Store Connect > App Review > open the submission > Messages: confirm each rejected item has been edited and Update Review clicked, or removed.
  - fix: Address the rejection reason for each item, click Update Review, then Resubmit to App Review.

---

## IAP.STATUS In-App Purchase statuses

**Source text (verbatim):**
> The In-App Purchase status indicates whether your In-App Purchase is available or if it needs your attention. A red status indicator means that you need to take action before the product can be made available. A yellow status indicator means that a process controlled by you or Apple is ongoing. A green status indicator means that the In-App Purchase is available.
> - A red status indicator () means that you need to perform some action before a product can be made available.
> - A yellow status indicator () means that some process is ongoing, controlled either by you or by Apple.
> - A green status indicator () means that the In-App Purchase is available.
>
> | Status | Description |
> |---|---|
> | Prepare for Submission | Your In-App Purchase has been created, but you haven't yet submitted it for review. Use Add for Review to add it to a submission. If your In-App Purchase is missing required metadata, complete it before adding for review. |
> | Ready for Review | Your In-App Purchase has been added to a submission, but you haven't sent the submission to App Review yet. While your product is in this state, you can edit only the reference name, pricing, and availability. |
> | Waiting for Review | You have submitted your In-App Purchase to be reviewed by Apple. While your product is in this state, you can edit only the reference name, pricing, and availability. |
> | In Review | Your In-App Purchase is currently being reviewed by Apple. While your product is in this state, you can edit only the reference name, pricing, and availability. |
> | Accepted | Your In-App Purchase has been accepted, but one or more other items in the same submission were rejected. Your In-App Purchase won't be approved until all items in the submission are accepted. You can edit the rejected items and resubmit them, or remove them from the submission. |
> | Approved | Apple has approved your In-App Purchase. For this status to appear, you must provide country or region availability for your In-App Purchase. If you select "Remove from Sale," the status appears as "Developer Removed from Sale." |
> | Rejected | Apple has rejected your In-App Purchase during the review process. You can edit the item and use Update Review to resubmit it. If you haven't been contacted by Apple with more information about the rejection, you can inquire through Contact Us. |
> | Developer Rejected | You removed your In-App Purchase from review. When you're ready, use Add for Review to resubmit it. |
> | Developer Removed from Sale | You removed the In-App Purchase from sale. Customers who already purchased it retain access. Those transactions are available with StoreKit and in the App Store Server API. To make the In-App Purchase available for sale again, update its availability settings. |
> | Removed from Sale | Apple removed this In-App Purchase from sale. |

**Applies to:** All In-App Purchases
**Requires:** iap, subscriptions

- **[IAP-34]** Is every product the app sells free of a red status (needing action) in App Store Connect?
  - quote: "A red status indicator means that you need to take action before the product can be made available."
  - surface: asc
  - verify: App Store Connect > In-App Purchases and Subscriptions lists: note the status and indicator color of each product the code references; flag any product shown with a red status indicator, and read that status's description in the statuses table above for the required action.
  - fix: Complete metadata and Add for Review, or address rejection and Update Review.
- **[IAP-35]** Is country or region availability set for each In-App Purchase?
  - quote: "For this status to appear, you must provide country or region availability for your In-App Purchase."
  - surface: asc
  - verify: App Store Connect > each In-App Purchase/subscription > Availability: confirm at least one country or region is selected.
  - fix: Select the countries or regions where the product is available.
- **[IAP-36]** Does the app still grant access to customers who purchased an In-App Purchase that has since been removed from sale?
  - quote: "Customers who already purchased it retain access. Those transactions are available with StoreKit and in the App Store Server API."
  - surface: code
  - verify: Confirm entitlement checks are based on transactions (`Transaction.currentEntitlements` / `Transaction.all` / server API), not on whether `Product.products(for:)` still returns the product.
  - fix: Base unlock logic on verified transactions rather than on product availability.

---

## IAP.SUBGROUP Offer auto-renewable subscriptions (groups, levels, durations, products)

**Source text (verbatim):**
> App Store Connect offers tools to help you run a subscription business on the App Store. How you configure your subscriptions in App Store Connect determine how users subscribe to your service, how often they are billed, and how they upgrade and downgrade between offerings. To begin offering a subscription in your app, you will need to create a Subscription Group, then add one or more Subscription products to that group, then assign levels to those products. Subscription setup is structured as the following:
> - Subscription group: A set of subscription products with varying levels and durations. You can have up to 100 subscriptions per group. Users can subscribe to one subscription product per group at a time.
> - Subscription: A product that lets users purchase dynamic content for a set period. Auto-renewable subscriptions renew automatically, unless cancelled by the user. Subscription duration and price is configured in App Store Connect.
> - Subscription levels: A ranking system of subscriptions within a subscription group that determines the upgrade, downgrade, and crossgrade path available to subscribers. Levels make it possible to offer varying access (basic, premium) of the same service.
> - Subscription duration: The length of time before the subscription renews and the subscriber is charged. Possible durations are 1 week, 1 month, 2 months, 3 months, 6 months, and 1 year.
>
> Single subscription product setup
>
> If you offer only one subscription product in your app, the subscription defaults to a single level within the subscription group.
>
> Multiple subscription and durations product setup
>
> Arrange your subscriptions in order from the one that offers the most (level 1) to the one that offers the least. You can stack subscriptions with equal content but different durations and other similar variables, at the same level. Each level can have multiple subscription products, offering multiple durations and prices for people to choose from. This lets them upgrade, downgrade, and crossgrade within the subscription group without impacting their days of paid service.
>
> Create an additional subscription group
>
> A subscription group contains all the variations of a single subscription product — for example, monthly and annual plans for the same service, or basic and premium tiers. Customers can only hold one active subscription per group at a time. Create additional subscription groups only when your app offers separate subscription products that customers can purchase at the same time.
>
> Note: Since users can only buy one subscription within a group at a time, creating a single group is the best practice for most apps, as it prevents people from accidentally purchasing multiple subscriptions. Users who buy subscriptions in multiple groups are billed separately for each subscription.
>
> Add subscription products
> - In the Sidebar, under Monetization, click Subscriptions.
> - Click a subscription group name.
> - Click Create.
> - Enter the subscription’s reference name and Product ID, then click Create. Once you've created your subscription product, you'll be taken to its information page to add more details.
> - Click Create.
>
> Note: In order to offer a monthly subscription with a 12 month commitment for subscriptions outside the United States and Singapore, select a duration of 1 year. Learn how to offer subscriptions with a 12 month commitment.
> - Under Subscription Duration, choose a duration and click Save.
> - Under Subscription Prices, set a price.
> - Under Availability, select which countries or regions you want to make your subscription available in.
> - Under Review Information, provide any additional information that may help the App Review team review your In-App Purchase.
> - Optionally, enable Family Sharing, edit the subscription’s tax category, and add localizations.
> - Click Save.
>
> Note:
> - If you'd like your subscription to be accessible from more than one app, create an equivalent subscription product for each app. Learn how to offer subscriptions across multiple apps.
> - Your first auto-renewable subscription must be submitted with a new app version. Your first subscription group must also be submitted with a new app version and must include an auto-renewable subscription in the same submission. After creating your subscription group and subscription product, select Add for Review on the subscription detail page to submit it for review. Once your first auto-renewable subscription has been approved, you can submit additional auto-renewable subscriptions without a new app version. Learn more about submitting subscriptions for review.
>
> Add localizations
>
> You can add languages and enter localized metadata for your auto-renewable subscriptions and subscription groups. For a list of supported languages, visit App Store localizations. Subscription group localizations and subscription localizations are reviewed independently from your In-App Purchase submission. For the properties you can localize, visit Required, localizable, and editable properties. For a detailed example visit Localize app information.
>
> Important: You can manage languages only when the app status is editable.
>
> Add subscription group localizations
>
> In each localization, you can customize subscription group names and app display options. Users will see these names when they manage subscriptions on their devices.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-37]** Is every auto-renewable subscription the app sells placed in a subscription group in App Store Connect?
  - quote: "To begin offering a subscription in your app, you will need to create a Subscription Group, then add one or more Subscription products to that group, then assign levels to those products."
  - surface: asc
  - verify: App Store Connect > Monetization > Subscriptions: confirm each subscription product ID from code belongs to a group; compare `subscriptionGroupID` values in code/`.storekit` with group IDs in App Store Connect.
  - fix: Create the group and the subscriptions within it.
- **[IAP-38]** Does each subscription group contain no more than 100 subscriptions?
  - quote: "You can have up to 100 subscriptions per group."
  - surface: asc
  - verify: Count subscriptions in each group in App Store Connect.
  - fix: Reduce the number of subscriptions in the group.
- **[IAP-39]** If there are multiple subscriptions with different levels of service, are they ranked from the one that offers the most (level 1) to the one that offers the least?
  - quote: "Arrange your subscriptions in order from the one that offers the most (level 1) to the one that offers the least."
  - surface: asc
  - verify: App Store Connect > Subscriptions > group > Edit Order: compare level order with what each tier unlocks in code (premium tier should be level 1).
  - fix: Reorder levels via Edit Order and Save.
- **[IAP-40]** Are additional subscription groups used only when the app offers separate subscription products customers can purchase at the same time?
  - quote: "Create additional subscription groups only when your app offers separate subscription products that customers can purchase at the same time."
  - surface: asc
  - verify: If more than one group exists, confirm the groups unlock independent content intended to be held simultaneously (not monthly/annual variants of the same service).
  - fix: Move variants of the same service into a single group (manual — requires developer decision on product structure).
- **[IAP-41]** Does each subscription have a duration, a price, availability, and Review Information set?
  - quote: "Under Subscription Duration, choose a duration and click Save."
  - surface: asc
  - verify: App Store Connect > each subscription: Subscription Duration (1 week, 1 month, 2 months, 3 months, 6 months, or 1 year), Subscription Prices, Availability, Review Information all filled.
  - fix: Fill in the missing sections and Save.
- **[IAP-42]** Is the first auto-renewable subscription (and first subscription group) submitted with a new app version, with the group including an auto-renewable subscription in the same submission?
  - quote: "Your first subscription group must also be submitted with a new app version and must include an auto-renewable subscription in the same submission."
  - surface: asc
  - verify: App Store Connect > App Review > Drafts: confirm the draft contains the app version, the group, and at least one subscription when no subscription has been approved before.
  - fix: Add the app version and group to the subscription's submission.
- **[IAP-43]** (Advisory — the source says "you can") Has the subscription group been given localized group names, which users see when they manage subscriptions on their devices?
  - quote: "In each localization, you can customize subscription group names and app display options. Users will see these names when they manage subscriptions on their devices."
  - surface: asc
  - verify: App Store Connect > Subscriptions > group > Localization: confirm a localization with Subscription Group Display Name exists.
  - fix: Add a group localization (Display Name, app name display option).
- **[IAP-44]** If the same subscription is meant to be accessible from more than one app, is an equivalent subscription product created for each app?
  - quote: "If you'd like your subscription to be accessible from more than one app, create an equivalent subscription product for each app."
  - surface: asc
  - verify: For multi-app subscription offerings, confirm each app record has its own equivalent subscription product.
  - fix: Create equivalent subscription products in each app record.
- **[IAP-108]** If the app offers a monthly subscription with a 12 month commitment outside the United States and Singapore, is that subscription's duration set to 1 year?
  - quote: "In order to offer a monthly subscription with a 12 month commitment for subscriptions outside the United States and Singapore, select a duration of 1 year."
  - surface: asc
  - verify: App Store Connect > the subscription > Subscription Duration: confirm 1 year for a monthly-with-12-month-commitment offering outside the United States and Singapore.
  - fix: Select a duration of 1 year before submitting (duration can't be changed after submitting for review; see IAP-47).

---

## IAP.SUBINFO Auto-renewable subscription information (field reference)

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Subscription Group | A set of subscription products with varying levels and durations. Users can subscribe to one subscription product per group at a time. |
> | Subscription Group Reference Name | An internal name you choose for a subscription group. This name will only appear on App Store Connect and in Sales and Trends reports, and won’t be visible to users. |
> | Subscription Group Display Name | A user-facing name you choose for a subscription group. This is the name that appears on the App Store, and it can be localized. Subscription group display names must not contain control characters (for example, null, new lines, carriage returns, escape, and other invisible characters), or markup language (for example, HTML tags, or Unicode characters, such as emoticons, diacritics, or special characters). |
> | App Name Display Options | A set of options that let you choose between using your app’s name or providing a custom name to display above the Subscription Group Display Name on the Manage Subscriptions page on user devices. |
> | Auto-Renewable Subscription | A product that allows users to purchase dynamic content for a set period. This type of subscription renews automatically unless cancelled by the user. Subscription duration and price is configured in App Store Connect. |
> | Auto-Renewable Subscription Levels | A ranking system of subscriptions within a subscription group that determines the upgrade, downgrade, and crossgrade path available to subscribers. Levels make it possible to offer varying access (basic, premium) of the same service. If you offer only one subscription product in your app, the subscription defaults to a single level within the subscription group. If you have multiple subscription products, arrange them in order from the one that offers the most (level 1) to the one that offers the least. You can stack subscriptions with equal content but different durations and other similar variables at the same level. Each level can have multiple subscription products, allowing for multiple durations and prices for people to choose from. This lets them upgrade, downgrade, and crossgrade within the subscription group without impacting their days of paid service. |
> | Upgrade | When someone switches to a subscription that you’ve ranked at a higher level. The customer’s prorated payment from lower level subscription is refunded to the original payment method. They’re charged for the higher level subscription, which goes into effect immediately. The date of upgrade is the renewal date for the higher level subscription. |
> | Downgrade | When someone switches to a subscription that you’ve ranked at a lower level. They’re charged for the lower level subscription on their next renewal date. |
> | Crossgrade | When someone switches between subscriptions that you’ve ranked at the same level. If the subscriptions are different durations, the crossgrade goes into effect on the customer’s next renewal date. If the subscriptions are the same duration, the customer’s prorated payment from the previous subscription is refunded to the original payment method. Then they’re charged for the new subscription, which goes into effect immediately. The date of cross grade is the renewal date for the new subscription. |
> | Auto-Renewable Subscription Duration | The length of time before the subscription renews and the subscriber is charged. Possible durations are 1 week, 1 month, 2 months, 3 months, 6 months, and 1 year. The duration can’t be changed after you submit for review. Auto-renewable subscriptions renew on the same day as the calendar date of the original purchase. If a one month free trial starts on January 7, the trial ends on February 7. If a one-month duration starts on a date that doesn’t occur in the next month, the trial ends on the last day of the next month, and reverts to the original date the next time that date occurs. For example, if someone subscribes on January 30, the next renewal date is February 28 (or February 29 in a leap year), and then March 30. |
> | Auto-Renewable Subscription Display Name | A user-facing name you choose for a subscription. This is the name that appears on the App Store, and it can be localized. Subscription display names must not contain control characters (for example, null, new lines, carriage returns, escape, and other invisible characters), or markup language (for example, HTML tags, or Unicode characters, such as emoticons, diacritics, or special characters). |
> | Multiseat Purchases | A purchase option that allows a customer to buy a subscription in quantities greater than 1. multiseat purchases are on by default for all auto-renewable subscriptions. Required for selling in Apple Business and Apple School Manager. Learn how to set purchase options for an auto-renewable subscription. |
> | Available for Purchase From | Where an auto-renewable subscription is available for purchase. Options are the App Store, Apple Business, and Apple School Manager. Learn how to set purchase options for an auto-renewable subscription. |

Subscription durations (verbatim): 1 week, 1 month, 2 months, 3 months, 6 months, and 1 year.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-45]** Are subscription group display names free of control characters and markup language (HTML tags, emoticons, diacritics, special characters)?
  - quote: "Subscription group display names must not contain control characters (for example, null, new lines, carriage returns, escape, and other invisible characters), or markup language (for example, HTML tags, or Unicode characters, such as emoticons, diacritics, or special characters)."
  - surface: asc
  - verify: Inspect every localized Subscription Group Display Name in App Store Connect for newlines, invisible characters, `<`/`>` tags, emoji, diacritics or special characters.
  - fix: Rewrite the display name using plain characters.
- **[IAP-46]** Are subscription display names free of control characters and markup language (HTML tags, emoticons, diacritics, special characters)?
  - quote: "Subscription display names must not contain control characters (for example, null, new lines, carriage returns, escape, and other invisible characters), or markup language (for example, HTML tags, or Unicode characters, such as emoticons, diacritics, or special characters)."
  - surface: asc
  - verify: Inspect every localized Auto-Renewable Subscription Display Name in App Store Connect.
  - fix: Rewrite the display name using plain characters.
- **[IAP-47]** Is the chosen subscription duration final before submission (it can’t be changed after submitting for review)?
  - quote: "The duration can’t be changed after you submit for review."
  - surface: manual
  - verify: Ask the developer to confirm each unsubmitted subscription's duration in App Store Connect matches the intended billing period and the period stated in the app's paywall copy.
  - fix: Correct the duration before submitting (after submission, create a new subscription).
- **[IAP-109]** If the subscription is offered for purchase from Apple Business or Apple School Manager, are multiseat purchases turned on for it?
  - quote: "Required for selling in Apple Business and Apple School Manager."
  - surface: asc
  - verify: App Store Connect > subscription > purchase options: if "Available for Purchase From" includes Apple Business or Apple School Manager, confirm Multiseat Purchases is on.
  - fix: Turn multiseat purchases back on for that subscription, or remove Apple Business / Apple School Manager availability.
- **[IAP-48]** (Derived from Apple's described behavior, not a stated app rule) Does any in-app copy or entitlement logic about plan changes match how Apple applies them — upgrades take effect immediately, downgrades on the next renewal date?
  - quote: "They’re charged for the lower level subscription on their next renewal date."
  - surface: code
  - verify: Inspect plan-change copy and entitlement code: the active tier should come from the current verified transaction / `Product.SubscriptionInfo.Status` (renewal info `autoRenewPreference` indicates a pending downgrade) rather than switching the user to the lower tier immediately on downgrade.
  - fix: Use `Product.SubscriptionInfo.status(for:)` and current transaction to determine the active level; show pending downgrade separately.

---

## IAP.NONRENEW Create non-renewing subscriptions

**Source text (verbatim):**
> A non-renewing subscription gives customers access to a service or content for a specific period of time (for example, access to a magazine for one month). To offer non-renewing subscriptions, enter product details in App Store Connect.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> Learn how to create a non-renewing subscription using the App Store Connect API.
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Subscriptions.
> - Scroll down to Non-Renewing Subscriptions, and click Manage.
> - Click the add button (+).
> - Enter a Reference Name and Product ID, then click Create.
> - Set a price and add localizations.
> - Click Save.
>
> Note: Your first non-renewing subscription must be submitted with a new app version. After creating your subscription, select Add for Review and include an app version in your submission to have it reviewed together with your app. Once your first non-renewing subscription has been approved, you can submit additional non-renewing subscriptions without a new app version. Learn more about submitting subscriptions for review.

**Applies to:** Apps that offer non-renewing subscriptions
**Requires:** iap, subscriptions

- **[IAP-49]** Does each non-renewing subscription have a reference name, product ID, price, and localizations?
  - quote: "Enter a Reference Name and Product ID, then click Create."
  - surface: asc
  - verify: App Store Connect > Subscriptions > Non-Renewing Subscriptions > Manage: confirm each product has a price and at least one localization.
  - fix: Set a price and add localizations, then Save.
- **[IAP-50]** Is the first non-renewing subscription submitted with a new app version?
  - quote: "Your first non-renewing subscription must be submitted with a new app version."
  - surface: asc
  - verify: Draft submission includes an app version when no non-renewing subscription has been approved yet.
  - fix: Add the app version to the submission.

---

## IAP.INTRO Set up introductory offers for auto-renewable subscriptions

**Source text (verbatim):**
> You can set up introductory offers for your apps on the App Store that contain auto-renewable subscriptions in App Store Connect. An introductory offer is a limited-time discounted price or free trial for the initial period of a subscription.
>
> When you set up an introductory offer, it automatically appears on your app’s product page on the App Store for eligible users. You can also display introductory offers within your app. When displaying offers in your app, use receipt validation to ensure that you’re only showing offers to people who can redeem them. Learn about implementing introductory offers.
>
> There are three types of introductory offers: free trial, pay up front, and pay as you go. You can choose the length of the introductory offer based on the standard subscription duration.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> | Standard Subscription Duration | Pay As You Go | Pay Up Front | Free Trial |
> |---|---|---|---|
> | 1 Week | 1 to 12 Weeks | 1, 2, 3, or 6 Months. 1 Year. | 3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year. |
> | 1 Month | 1 to 12 Months | 1, 2, 3, or 6 Months. 1 Year. | 3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year. |
> | 2 Months | 2, 4, 6, 8, 10, or 12 Months | 1, 2, 3, or 6 Months. 1 Year. | 3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year. |
> | 3 Months | 3, 6, 9, or 12 Months | 1, 2, 3, or 6 Months. 1 Year. | 3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year. |
> | 6 Months | 6 or 12 Months | 1, 2, 3, or 6 Months. 1 Year. | 3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year. |
> | 1 Year | 1 Year | 1, 2, 3, or 6 Months. 1 Year. | 3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year. |
>
> Although you can create an introductory offer for each subscription product in App Store Connect, each person is only eligible to redeem one introductory offer per subscription group.
>
> Create an introductory offer
> - Select the countries or regions where you want to offer a discounted price, and click Next. You can have one current and one future introductory offer per storefront.
> - Make sure the details of your introductory offer are correct and click Confirm. Once you create an introductory offer, you won’t be able to edit it. To change the details of your introductory offer, delete it and create a new one.
>
> What is the difference between introductory offer limits and customer eligibility limits?
>
> App Store Connect allows you to set an introductory offer for each subscription product in App Store Connect. You can have multiple offers in each subscription group. New and returning customers are only eligible to use one introductory offer per subscription group. For example, if a customer uses a free trial and then upgrades to a subscription product in the same group that also has a free trial, they aren't eligible for the second offer.

**Applies to:** Apps that offer introductory offers (free trial, pay up front, pay as you go) on auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-51]** If the app displays an introductory offer in its own UI, does it only show the offer to people eligible to redeem it?
  - quote: "When displaying offers in your app, use receipt validation to ensure that you’re only showing offers to people who can redeem them."
  - surface: code
  - verify: Grep paywall code for introductory offer display (`subscription?.introductoryOffer`, `introductoryPrice`, "free trial", "trial" strings). Confirm it is gated by `Product.SubscriptionInfo.isEligibleForIntroOffer` / `isEligibleForIntroOffer(for:)` (StoreKit 2), receipt validation, or StoreKit views (`SubscriptionStoreView` handles eligibility).
  - fix: Gate intro-offer copy on `await product.subscription?.isEligibleForIntroOffer` (or use `SubscriptionStoreView`/`ProductView`), showing the standard price otherwise.
- **[IAP-53]** Does the app avoid promising a second introductory offer to someone who already used one in the same subscription group?
  - quote: "each person is only eligible to redeem one introductory offer per subscription group"
  - surface: runtime
  - verify: With a sandbox account that has redeemed a trial in the group, open the paywall for another product in the same group and confirm no free-trial/intro price is promised.
  - fix: Gate intro-offer messaging on eligibility per group (see IAP-51).
- **[IAP-111]** Does each subscription have no more than one current and one future introductory offer per storefront?
  - quote: "You can have one current and one future introductory offer per storefront."
  - surface: asc
  - verify: App Store Connect > subscription > View all Subscription Pricing > Introductory Offers: per storefront, count current and scheduled offers.
  - fix: Delete the extra offer (introductory offers can't be edited; delete and recreate to change them).

---

## IAP.PROMO Set up promotional offers for auto-renewable subscriptions

**Source text (verbatim):**
> Apps on the App Store with auto-renewable subscriptions can provide a discounted price for a specific duration for existing and previously subscribed customers on iOS, macOS, and tvOS. You can use these offers to help win back subscribers who canceled their subscriptions or promote an upgrade to a higher-ranked subscription at a special price. Customers can accept the offer even if they've already accepted an introductory offer.
>
> To get started, generate keys for In-App Purchases, create a promotional offer on your app's In-App Purchase page for each product, and choose a duration and offer type (pay as you go, pay up front, free). You can have up to 10 active offers per subscription. If you have enabled monthly subscriptions with a 12 month commitment you're limited to 10 active offers for that payment configuration.
>
> Once you've created offers in App Store Connect, use Xcode 10.2 or later to implement the StoreKit APIs to allow these offers to be accepted by customers running iOS 12.2, macOS 10.14.4, and tvOS 12.2, or later.
>
> Set up a promotional offer
> - Enter a Promotional Offer Reference Name and a Promotional Offer Identifier, then click Next.
> - Choose Pay as you go, Pay up front, or Free, then choose the appropriate duration and a base price. To search from a larger list of price points, click See Additional Prices. Click Next.
> - Promotional offers apply to all storefronts where your subscription is available — you can't limit an offer to specific countries or regions. App Store Connect provides comparable prices for each storefront, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.
>
> Edit a promotional offer
>
> Once you create a promotional offer, only the price can be edited. To edit the duration, type, or offer code, you must create a new offer.

**Applies to:** Apps that offer promotional offers on auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-54]** If the app uses promotional offers, have In-App Purchase keys been generated?
  - quote: "To get started, generate keys for In-App Purchases"
  - surface: asc
  - verify: Grep code for promotional offer use (`Product.PurchaseOption.promotionalOffer`, `SKPaymentDiscount`, `promotionalOffers`). If present, App Store Connect > Users and Access > Integrations > In-App Purchase: confirm an active key exists.
  - fix: Generate an In-App Purchase key in App Store Connect and use it server-side to sign offers.
- **[IAP-55]** Does each promotional offer identifier used in code exist on the corresponding subscription in App Store Connect?
  - quote: "Enter a Promotional Offer Reference Name and a Promotional Offer Identifier, then click Next."
  - surface: asc
  - verify: Collect offer identifier strings from code/server; compare with App Store Connect > subscription > View all Subscription Pricing > Promotional Offers tab.
  - fix: Create the missing promotional offer or correct the identifier in code.
- **[IAP-56]** Does each subscription have no more than 10 active promotional offers?
  - quote: "You can have up to 10 active offers per subscription."
  - surface: asc
  - verify: Count active offers in the Promotional Offers tab per subscription.
  - fix: Delete unneeded offers.

---

## IAP.WINBACK Set up win-back offers

**Source text (verbatim):**
> If your app offers auto-renewable subscriptions, you have the option to set up win-back offers to encourage lapsed subscribers to re-subscribe on the App Store.
>
> Win-back offers are configured per subscription product, not per subscription group. Customers are only eligible for win-back offers for their most recently lapsed subscription product within each group — so if you want to reach lapsed subscribers across multiple products, create a separate win-back offer for each one.
>
> App Store Connect allows you to create a maximum of 350 win-back offers per subscription. You can run a maximum of 5 win-back offers per storefront, per subscription at a time. If you have enabled monthly subscriptions with a 12 month commitment you're limited to 5 active offers per storefront for that payment configuration.
>
> Set up win-back offers
> - Choose the subscription group containing your subscription. Your subscription needs to be approved by App Review before you can create a win-back offer.
> - Enter an identifier for the offer. This will allow you to identify sales associated with the offer in Sales and Trends reports and in StoreKit transactions. It must not have already been used for another offer in the same subscription group. After you’ve created your offer, you can’t change the offer identifier.
> - Set the date range for when this offer will be available. The earliest you can schedule your offer to go live is one day after today, and the event must run for a minimum of 3 days. Please note that start dates and times vary by region.
> - Determine which customers are eligible for the offer, based on how long they were paid subscribers and when their subscriptions ended.
>
> | Eligibility Criteria | Definition |
> |---|---|
> | Minimum Paid Duration | The minimum time that a customer must have been subscribed to that subscription in order to be eligible for the offer. Choose any value between 1 and 24 months, or 3, 4, and 5 years. |
> | Time Since Last Subscribed | The range of months that must have passed since the customer last had an active subscription. You can choose a minimum value of 1 month and a maximum value of 24 months. For example, selecting a minimum of 5 months and a maximum of 11 months will configure your offer to be shown only to customers who have been lapsed for 5 to 11 months. Both a minimum and maximum value are required. |
> | Wait Between Offers | The required time a customer must wait after a win-back offer ends before redeeming the same offer again. Choose a value between 2 and 24 months. This field is optional. |
>
> - Make sure the details of your offer are correct, and then click Confirm. After the offer is created, a redemption URL to the offer is generated. The offer will automatically display on the customers' Manage Subscriptions page and within your app once the start date is reached. In order for your offer to appear on the App Store, make sure you have an approved image for your subscription, and have promoted the offer.
>
> Promote win-back offers on the App Store
>
> In order for your win-back offer to appear on your app’s product page and in editorially curated selections and personalized recommendations across the App Store, you must promote it. To promote an offer on the App Store, make sure you have an subscription image for your subscription approved by App Review.
>
> The App Store will display your image on a win-back offer sheet alongside your app icon, subscription display name, and description. You may not upload an image that is the same as your app icon, or any of your app screenshots.
>
> Display offers to eligible subscribers
>
> Win-back offers are automatically displayed to eligible customers in their Manage Subscription page on iOS 14.3, iPadOS 14.3, and macOS 14 or later, and within your app on the win-back offer sheet on iOS 18, iPadOS 18, and macOS 15 or later. You can manage how the win-back offer sheet is displayed in your app using StoreKit.
>
> You can also market win-back offers to eligible customers by sharing a redemption URL to your offer with them (such as through an email or website), or merchandise the offer within your app using StoreKit 2 APIs.
>
> To copy your offer's redemption URL to share it with customers:
> - Click the subscription, then go to the Redemption URL section and click Copy Link. Make sure you check customers eligibility before you send out the link. Learn more.

**Applies to:** Apps that offer win-back offers on auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-57]** Is each subscription that has (or will have) a win-back offer already approved by App Review?
  - quote: "Your subscription needs to be approved by App Review before you can create a win-back offer."
  - surface: asc
  - verify: App Store Connect > subscription status = Approved before planning a win-back offer.
  - fix: Get the subscription approved first, then create the win-back offer.
- **[IAP-58]** For a promoted win-back offer, does the subscription have an approved image that is not the same as the app icon or any app screenshot?
  - quote: "You may not upload an image that is the same as your app icon, or any of your app screenshots."
  - surface: asc
  - verify: App Store Connect > subscription > Image: compare the image with the app icon (AppIcon in Assets.xcassets) and uploaded screenshots; confirm status approved.
  - fix: Create a distinct promotional image (see IAP-19 specs) and submit it for review.
- **[IAP-59]** Are win-back offer limits respected (max 350 per subscription; max 5 running per storefront per subscription)?
  - quote: "You can run a maximum of 5 win-back offers per storefront, per subscription at a time."
  - surface: asc
  - verify: Subscription > View all Subscription Pricing > Win-Back Offers tab: count offers and concurrent offers per storefront.
  - fix: Delete or reschedule offers.
- **[IAP-112]** Is each win-back offer identifier unused by any other offer in the same subscription group?
  - quote: "It must not have already been used for another offer in the same subscription group."
  - surface: asc
  - verify: Compare win-back offer identifiers (App Store Connect and any identifiers referenced in code/StoreKit configuration) against other offer identifiers in the same group.
  - fix: Choose a new identifier (it can't be changed after the offer is created).
- **[IAP-113]** Does each scheduled win-back offer start no earlier than one day after today and run for at least 3 days?
  - quote: "The earliest you can schedule your offer to go live is one day after today, and the event must run for a minimum of 3 days."
  - surface: asc
  - verify: Win-Back Offers tab: check each offer's start and end dates.
  - fix: Adjust the date range.
- **[IAP-114]** If the win-back offer's redemption URL is shared with customers, is their eligibility checked before the link is sent?
  - quote: "Make sure you check customers eligibility before you send out the link."
  - surface: manual
  - verify: Ask the developer how redemption URLs are distributed (email, website) and whether recipients are filtered by the offer's eligibility criteria first.
  - fix: manual — requires developer decision/legal/business action (filter recipients by eligibility before sending).

---

## IAP.FAMILY-ASC Turn on Family Sharing for In-App Purchases

**Source text (verbatim):**
> Family Sharing is a feature supported only by apps that offer auto-renewable subscriptions and non-consumable In-App Purchases. This feature enables users to share their purchases with up to five additional family members. To configure which of your In-App Purchases are eligible for Family Sharing, navigate to App Store Connect.
>
> Whether or not a user’s purchases are automatically shared with their family members depends on the type of In-App Purchase, the user’s sharing preferences, and if the purchase was made before or after Family Sharing was turned on in App Store Connect. Users have the option of turning off Family Sharing in their subscription settings at any time.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> | | Auto-renewable subscriptions | Non-consumable In-App Purchases |
> |---|---|---|
> | New Users | Family Sharing is enabled by default depending on the preference set by the purchaser in Manage Subscriptions. | Family Sharing is enabled by default if the following conditions are met: - The family organizer has purchase sharing enabled. - The purchaser of a non-consumable In-App Purchase has Share Purchases/Share My Purchases enabled. - The family member you want to share with has Share Purchases/Share My Purchases enabled. - The app isn't hidden from the user's purchase history. |
> | Existing Users | Users must opt-in to Family Sharing from within their manage subscriptions page. | You can unlock access to the In-App Purchase using receipt validation or App Store server notifications if the following conditions are met: - The family organizer has purchase sharing enabled. - The purchaser of a non-consumable In-App Purchase has Share Purchases/Share My Purchases enabled. - The family member you want to share with has Share Purchases/Share My Purchases enabled. - The app is not hidden from the user's purchase history. |
>
> Required role: Account Holder or App Manager. View role permissions.
>
> Turn on Family Sharing
>
> This subscription will be able to be shared by up to six family members. Family Sharing is only available for subscriptions purchased from the App Store.
>
> If multiseat purchases are turned on for a subscription, only the group purchaser is eligible for Family Sharing — additional seats are for individual use only.
>
> Keep in mind that once you turn on Family Sharing for an In-App Purchases in App Store Connect, you can't turn it off.
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases, or Subscriptions then the subscription group.
> - Select your In-App Purchase, or subscription, from the list.
> - Scroll down to the Family Sharing section.
> - Click Turn On.
> - In the confirmation dialog, review the Family Sharing terms, then click Confirm.

**Applies to:** Apps that offer auto-renewable subscriptions or non-consumable In-App Purchases and turn on Family Sharing
**Requires:** iap, subscriptions

- **[IAP-60]** Is Family Sharing turned on only for auto-renewable subscriptions and non-consumables (not consumables or non-renewing subscriptions)?
  - quote: "Family Sharing is a feature supported only by apps that offer auto-renewable subscriptions and non-consumable In-App Purchases."
  - surface: asc
  - verify: App Store Connect > each product > Family Sharing section: confirm state, and that the app's marketing/paywall only claims family sharing for those product types.
  - fix: Remove Family Sharing claims for unsupported product types from app copy.
- **[IAP-61]** Has the developer confirmed the decision to turn on Family Sharing, given that it can't be turned off?
  - quote: "once you turn on Family Sharing for an In-App Purchases in App Store Connect, you can't turn it off"
  - surface: manual
  - verify: Ask the developer to confirm intent before enabling Family Sharing on any product.
  - fix: manual — requires developer decision/legal/business action.
- **[IAP-62]** If Family Sharing is on for non-consumables, can existing family members unlock access via receipt validation/App Store Server Notifications (i.e., does the app process restored/shared transactions)?
  - quote: "You can unlock access to the In-App Purchase using receipt validation or App Store server notifications if the following conditions are met"
  - surface: code
  - verify: Confirm entitlement logic iterates `Transaction.currentEntitlements` (which includes family-shared transactions, `ownershipType == .familyShared`) or validates receipts/server notifications, and that a restore action exists (`AppStore.sync()` / `SKPaymentQueue.restoreCompletedTransactions()`).
  - fix: Unlock based on `Transaction.currentEntitlements` and provide a Restore Purchases control.

---

## IAP.FAMILY-SK Supporting Family Sharing in your app (StoreKit)

**Source text (verbatim):**
> Family Sharing allows a customer to share access to auto-renewable subscriptions or non-consumables with up to five family members on all of their Apple devices. Enabling Family Sharing for a subscription can make your content or service more appealing to subscribers, and may encourage conversion to a paid subscription, increase customer engagement, and improve retention. Developers can choose to turn on Family Sharing for Apple In-App Purchases and non-consumables in App Store Connect. Users can also choose whether to share their purchases with family.
>
> When users share a purchase through Family Sharing, each family member gets their own unique receipts and transactions. Process the transactions in the same way you already handle purchases — you don’t need any special logic for shared products. However, you do need to implement a new method in your transaction observer, and listen for a new notification type in server notifications. Specifically, to support Family Sharing, you need to:
> - Enable Family Sharing for your Apple In-App Purchases in App Store Connect. For more information, see Turn on Family Sharing for Apple In-App Purchases.
> - During runtime, check whether Apple In-App Purchases support Family Sharing using either isFamilyShareable in Product or isFamilyShareable in SKProduct. Then inform users when merchandising your subscriptions.
> - Process purchased and restored transactions in your app. This is standard processing you already do for any purchases.
> - Implement paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:) in your transaction observer to handle conditions in which products are no longer shared.
> - Listen for the `REVOKE` notification_type from App Store Server Notifications on your server.
>
> Provide access to shared purchases
>
> Your app receives a unique receipt for each family member entitled to a shared purchase, on each of their devices. For subscriptions, your app unlocks access through the normal purchase flow. For non-consumable products, unlocking access may require users to initiate a restored purchase, depending on the Family Sharing settings at the time of purchase.
>
> To provide access for family members to a subscription or non-consumable, your app needs to handle purchased and restored transactions as usual. Specifically, follow these steps:
> - 1. Set up a transaction observer at app launch so your app receives transactions that occur outside of your app, such as receiving a Family Sharing purchase. For more information on this best practice, see Setting up the transaction observer for the payment queue.
> - 2. Verify the receipt. Look for a transaction in the latest receipt info array (responseBody.Latest_receipt_info) with the new Family Sharing purchase.
> - 3. Handle purchased (SKPaymentTransactionState.purchased) transactions. This is a standard state apps need to handle, and you don’t need anything special for Family Sharing. For shared subscriptions, the transaction always has a purchased state. For shared non-consumable products, the transaction has a purchased state if Family Sharing was enabled for the product at the time of the purchase. For more information about handling transactions, see Processing a transaction.
> - 4. Handle restored (SKPaymentTransactionState.restored) transactions, which is also a standard state apps need to handle. For shared non-consumable products, your app gets a restored transaction if developers enable Family Sharing after the user purchases the product. To gain access to the shared product, family members use your app’s restore functionality. For more information about restoring, see Restoring purchased products.
> - 5. Unlock access to the shared subscription or non-consumable product.
> - 6. Call finishTransaction(_:).
>
> Revoke access if Family Sharing is disabled
>
> With Family Sharing products, users have access to products only while Family Sharing is enabled. If the purchaser leaves the group, gets a refund, or stops sharing, the expectation is that the family’s access to the product stops immediately.
>
> When a condition occurs that disables sharing, StoreKit informs your app by updating the receipt, and then calling the paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:) method of the SKPaymentTransactionObserver protocol. Implement this method on your transaction observer, and do the following:
> - 1. Verify the receipt. Revoked products appear in the receipt with a `cancellation_date` field present.
> - 2. Provide the app with access to all the products to which the user is entitled.
>
> Listen for the revoke notification
>
> If you set up your server to receive App Store Server Notifications, your server gets a `REVOKE` notification_type as soon as a shared purchase is no longer shared. This notification serves the same purpose as the paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)call. Listen for and process this notification by:
> - 1. Checking the latest receipt (unified_receipt.Latest_receipt_info) in the response body. Revoked products appear in the receipt with a `cancellation_date` field present.
> - 2. Providing the app with access to all products to which the user is entitled.
> - 3. Updating your records, if you keep server-based records to manage your customers’ subscriptions.
>
> Indicate to users when products support Family Sharing
>
> When your app displays Apple In-App Purchases, indicate in your UI whether users can share the product with family. Call isFamilyShareable to determine at runtime whether the Apple In-App Purchase supports Family Sharing. Knowing whether a product is shareable helps users make a selection that best fits their needs.

**Applies to:** Apps with Family Sharing turned on for any In-App Purchase
**Requires:** iap, subscriptions

- **[IAP-63]** Does the app set up a transaction observer/listener at app launch so it receives transactions that occur outside the app (e.g., Family Sharing purchases)?
  - quote: "Set up a transaction observer at app launch so your app receives transactions that occur outside of your app, such as receiving a Family Sharing purchase."
  - surface: code
  - verify: StoreKit 2: grep for `Transaction.updates` iterated in a `Task` started at launch (App `init`, `@main` struct, `AppDelegate.application(_:didFinishLaunchingWithOptions:)`). StoreKit 1: `SKPaymentQueue.default().add(` an observer in launch code.
  - fix: Start a `Task { for await result in Transaction.updates { ... await transaction.finish() } }` at app launch (or add the `SKPaymentTransactionObserver` at launch).
- **[IAP-64]** Does the app handle revoked family-shared entitlements (StoreKit 1 `paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)`, or revocation info on StoreKit 2 transactions) and remove access?
  - quote: "Implement paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:) in your transaction observer to handle conditions in which products are no longer shared."
  - surface: code
  - verify: StoreKit 1: grep for `didRevokeEntitlementsForProductIdentifiers`. StoreKit 2: confirm entitlement checks honor `transaction.revocationDate` and re-derive access from `Transaction.currentEntitlements` when `Transaction.updates` delivers a revoked transaction.
  - fix: Implement the revoke delegate (SK1) or check `revocationDate`/recompute entitlements on updates (SK2).
- **[IAP-65]** If the app has a server that receives App Store Server Notifications, does it handle the `REVOKE` notification type?
  - quote: "Listen for the `REVOKE` notification_type from App Store Server Notifications on your server."
  - surface: code
  - verify: Grep server code for `REVOKE` handling in the notification endpoint.
  - fix: Add handling for `REVOKE` that removes the family member's access and updates records.
- **[IAP-66]** Does the app indicate in its UI whether each product can be shared with family, using `isFamilyShareable` at runtime?
  - quote: "When your app displays Apple In-App Purchases, indicate in your UI whether users can share the product with family. Call isFamilyShareable to determine at runtime whether the Apple In-App Purchase supports Family Sharing."
  - surface: code
  - verify: If any product has Family Sharing on, grep for `isFamilyShareable` in paywall/store views and confirm the UI shows a shareable indication when it is true.
  - fix: Show a "Family Sharing" label when `product.isFamilyShareable` is true.
- **[IAP-115]** After unlocking access for purchased/restored transactions, does the app finish each transaction?
  - quote: "Call finishTransaction(_:)."
  - surface: code
  - verify: StoreKit 1: grep for `finishTransaction(` in the transaction observer after content is unlocked. StoreKit 2 equivalent: `await transaction.finish()` after granting access in purchase and `Transaction.updates` handling.
  - fix: Finish each transaction after unlocking access.

---

## IAP.REFUND-SK Handling refund notifications

**Source text (verbatim):**
> The App Store server sends near real-time notifications when customers receive refunds for Apple In-App Purchases. If you offer content across multiple platforms, for example gems or coins for games, and you update player account balances on your server, receiving refund notifications is important. Respond to refund notifications by interpreting and handling the refund information, and informing customers in the app of any actions you take as a result of the refund.
>
> Receive notifications of customer refunds for one-time purchases
>
> Customers request refunds in several ways, such as:
> - Contacting Apple Customer Support and asking for a refund
> - Logging in and using Apple’s self-service tool, reportaproblem.apple.com, to request a refund
> - Asking their payment method issuer for a refund
>
> When the App Store processes a refund, the App Store server sends a `REFUND` notification to your server, at the URL you configure. Your server must respond to the post with a 200 response code. The `REFUND` notification applies to consumable, non-consumable, and non-renewing subscriptions only. To detect refunds for auto-renewable subscriptions, see Detect a Refund.
>
> Interpret and handle the refund notification
>
> You’re responsible to store, monitor, and take appropriate action for each refunded transaction when you receive a `REFUND` notification. For example, you might build your own in-game currency-rebalancing logic that handles refunded transactions by linking a notification to a player account or session.
>
> Inform customers by presenting contextual messaging in the app for any actions you take as a result of the refund.

**Applies to:** Apps with a server that receives App Store Server Notifications for consumable, non-consumable, or non-renewing subscription purchases
**Requires:** iap, subscriptions

- **[IAP-67]** Does the server's notification endpoint respond with a 200 response code to `REFUND` posts?
  - quote: "Your server must respond to the post with a 200 response code."
  - surface: code
  - verify: Inspect the server's App Store Server Notifications handler: it must return HTTP 200 after processing (including for `REFUND`).
  - fix: Return 200 from the handler after successfully receiving the notification.
- **[IAP-116]** Does the server store, monitor, and take appropriate action for each refunded transaction when it receives a `REFUND` notification?
  - quote: "You’re responsible to store, monitor, and take appropriate action for each refunded transaction when you receive a `REFUND` notification."
  - surface: code
  - verify: Inspect the server's notification handler: confirm `REFUND` notifications are persisted and trigger an action (e.g. balance/currency rebalancing or access removal linked to the player account).
  - fix: Persist refunded transactions and add handling logic for them.
- **[IAP-68]** If the app takes action on a refund (e.g., rebalancing currency, removing access), does it inform the customer in the app with contextual messaging?
  - quote: "Inform customers by presenting contextual messaging in the app for any actions you take as a result of the refund."
  - surface: code
  - verify: Find code paths that react to refunds (server `REFUND` handling, StoreKit 2 `transaction.revocationDate`/`revocationReason` in `Transaction.updates`). Confirm the app surfaces a user-facing message when it changes balances or access.
  - fix: Add in-app messaging explaining the change and any required action.

---

## IAP.SUB-GETREADY Auto-renewable subscriptions — Getting ready

**Source text (verbatim):**
> To offer subscriptions, youʼll need to configure them in App Store Connect and use StoreKit APIs in your app. You’ll also need to assign each subscription to a subscription group (a group of subscriptions with different access levels, prices, and durations that people can choose from), then add details such as a name, price, and description. This information displays in the Apple In-App Purchases section of your app’s product page on the App Store. Ensure that the subscriptions are available across all device types that your app supports. Consider allowing a way for subscribers to see the status of their subscription within your app, along with upgrade, crossgrade, and downgrade options, as well as a way to easily manage or turn off their auto-renewable subscription. Make sure to follow our design and review guidelines.
>
> To get ready:
> - Watch the Apple In-App Purchase and Subscriptions videos.
> - Refer to the Apple In-App Purchase StoreKit API documentation.
> - Learn how to configure your subscriptions in App Store Connect Help.
> - Use the App Store Server API and enable App Store Server Notifications to get real-time changes to the status of your subscriptions.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-69]** Are the subscriptions available across all device types the app supports?
  - quote: "Ensure that the subscriptions are available across all device types that your app supports."
  - surface: code
  - verify: Check `TARGETED_DEVICE_FAMILY` / supported platforms (iPhone, iPad, Mac Catalyst/Designed for iPad, Apple TV, Vision) and confirm the paywall/purchase flow and entitlement checks are not excluded on any supported platform (look for `#if os(...)` / `UIDevice.current.userInterfaceIdiom` gating around StoreKit code). Note: per IAP.SUBMIT, In-App Purchases and subscriptions aren't supported on Apple Watch.
  - fix: Enable the purchase/entitlement code path on every supported device type.

---

## IAP.SUB-DISCLOSE Auto-renewable subscriptions — Clearly describing subscriptions (required sign-up screen details)

**Source text (verbatim):**
> An effective subscription purchase flow makes it simple for people to get the product or service they’re interested in. Use consistent messaging and include clear terms so people can easily recognize the value of the offer. A lengthy sign-up process will lower your subscription conversion rate, so keep the purchase flow simple and only ask for necessary information. In addition, the following details must be included in your subscription’s sign-up screen:
> - Subscription name and duration, and the content or services provided during the subscription period
> - Full renewal price, shown clearly and prominently, and localized in available currencies
> - A way for current subscribers to sign in or restore purchases
>
> Please note that your app and App Store metadata must include links to your Terms of Use and Privacy Policy.
>
> Billing amount
> In the purchase flow, the amount that will be billed must be the most prominent pricing element in the layout. For example, an annual subscription should clearly display the total amount that will be billed upon purchase. While you may also present a breakdown price that the annual amount is equivalent to or a savings when compared to weekly or monthly subscriptions, these additional elements should be displayed in a subordinate position and size to the annual price. This ensures that people are not misled.
>
> Free trials
> In the purchase flow for a free trial, clearly indicate how long the free trial lasts and the price billed once the free trial is over.

**Applies to:** Apps that offer auto-renewable subscriptions

- **[IAP-70]** Does the subscription sign-up screen show the subscription name and duration, and the content or services provided during the subscription period?
  - quote: "Subscription name and duration, and the content or services provided during the subscription period"
  - surface: runtime
  - verify: Launch the app, open every paywall/sign-up screen (onboarding, settings, feature gates) and confirm each option shows its name, its duration (e.g. "monthly"/"1 year"), and a description of what is included. In code, inspect paywall views for `product.displayName`, `product.subscription?.subscriptionPeriod`, and a features list (or `SubscriptionStoreView` marketing content).
  - fix: Add name, period, and included-features text to each option on the paywall.
- **[IAP-71]** Is the full renewal price shown clearly and prominently and localized in available currencies?
  - quote: "Full renewal price, shown clearly and prominently, and localized in available currencies"
  - surface: code
  - verify: Grep paywall code for hard-coded prices (regex like `\$[0-9]`, `€`, `USD`, `"9.99"`). Prices should come from `product.displayPrice` / `product.priceFormatStyle` (SK2) or `SKProduct.price` formatted with `priceLocale` (SK1). At runtime, switch the sandbox storefront/locale and confirm currency changes.
  - fix: Replace hard-coded prices with `product.displayPrice` (or StoreKit views) and display the renewal price prominently.
- **[IAP-72]** Does the sign-up screen include a way for current subscribers to sign in or restore purchases?
  - quote: "A way for current subscribers to sign in or restore purchases"
  - surface: code
  - verify: Grep for `AppStore.sync()`, `restoreCompletedTransactions`, `.storeButton(.visible, for: .restorePurchases)`, `SubscriptionStoreView` (restore button configurable), or a "Restore"/"Sign in" button on the paywall. Confirm at runtime that the control is visible on the sign-up screen.
  - fix: Add a "Restore Purchases" button calling `try await AppStore.sync()` (or `.storeButton(.visible, for: .restorePurchases)`) and/or a sign-in option on the paywall.
- **[IAP-73]** Does the app include links to the Terms of Use and Privacy Policy?
  - quote: "your app and App Store metadata must include links to your Terms of Use and Privacy Policy"
  - surface: code
  - verify: Grep the app for Terms/EULA and Privacy Policy links (URLs, `Link(`, `openURL`, `.subscriptionStorePolicyDestination`, strings "Terms", "Privacy") on or reachable from the paywall; open each URL and confirm it loads.
  - fix: Add tappable Terms of Use and Privacy Policy links to the paywall.
- **[IAP-74]** Does the App Store metadata include links to the Terms of Use and Privacy Policy?
  - quote: "your app and App Store metadata must include links to your Terms of Use and Privacy Policy"
  - surface: asc
  - verify: App Store Connect > App Information / App Privacy: Privacy Policy URL is set; Terms of Use: either the App Description contains a Terms of Use (EULA) link, or a custom EULA is set under App Information > License Agreement.
  - fix: Add the Privacy Policy URL and a Terms of Use link (in the description or as a custom EULA).
- **[IAP-75]** In the purchase flow, is the amount that will be billed the most prominent pricing element (required: "must"), and is any per-period breakdown or savings shown in a subordinate position and size (Apple: "should")?
  - quote: "the amount that will be billed must be the most prominent pricing element in the layout"
  - surface: runtime
  - verify: Screenshot each paywall option; for annual/multi-month plans confirm the total billed amount (e.g. "$39.99/year") uses a larger/more prominent style than any "$3.33/month" or "save 50%" text. In code, compare font sizes/weights of `displayPrice` vs computed breakdown labels.
  - fix: Make the billed total the largest price text; reduce breakdown/savings text size and place it below.
- **[IAP-76]** For a free trial, does the purchase flow clearly indicate how long the free trial lasts and the price billed once it is over?
  - quote: "clearly indicate how long the free trial lasts and the price billed once the free trial is over"
  - surface: runtime
  - verify: With an eligible sandbox account, open the paywall and confirm text like "<trial length> free, then <price>/<period>". In code, check that the trial period (`introductoryOffer.period`) and `displayPrice` are both rendered near the CTA.
  - fix: Add "X days free, then {displayPrice}/{period}" copy using StoreKit values.
- **[IAP-52]** Is the paywall's messaging consistent with the offers configured in App Store Connect (introductory offer type, duration, price) and are its terms clear?
  - quote: "Use consistent messaging and include clear terms so people can easily recognize the value of the offer."
  - surface: asc
  - verify: App Store Connect > subscription > View all Subscription Pricing > Introductory Offers tab: note type, duration, storefronts. Compare with paywall strings in code/Localizable files (e.g. "7-day free trial"); prefer that the app reads `introductoryOffer.period`/`paymentMode` from StoreKit rather than hard-coding.
  - fix: Replace hard-coded offer text with values from `Product.SubscriptionOffer`, or align the App Store Connect offer.
- **[IAP-127]** Does the subscription purchase flow ask only for necessary information?
  - quote: "keep the purchase flow simple and only ask for necessary information"
  - surface: runtime
  - verify: Walk the sign-up flow and list every field/step before purchase; flag fields not needed to complete the subscription (defer them until after sign-up).
  - fix: Move non-essential questions after sign-up.

---

## IAP.SUB-GROUP-GUIDE Auto-renewable subscriptions — Creating a subscription group

**Source text (verbatim):**
> Each subscription you offer must be assigned to a subscription group. A subscription group is made up of subscriptions with different access levels, prices, and durations so people can select the option that best fits their needs. Since people can only buy one subscription within a group at a time, creating a single group is the best practice for most apps as it prevents people from accidentally purchasing multiple subscriptions.
>
> If your app needs to offer the ability to buy multiple subscriptions — for example, to subscribe to more than one channel in a streaming app — you can add these subscriptions to different groups. People who buy subscriptions in multiple groups are billed separately for each subscription. Keep in mind that if someone cancels a subscription in one group and then purchases a new subscription in a different group, the renewal date will change and the days of paid service will reset.
>
> Multiple subscription groups aren’t recommended for apps in which people would expect to have a single active subscription. Keep your offerings simple and easy to understand. For each subscription, create a user-friendly, self-explanatory name that differentiates it from others in the group. Use distinct names for the app, the subscription group, and each subscription to avoid confusion.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-77]** Does each subscription have a user-friendly, self-explanatory display name that differs from the others in the group, and are app, group, and subscription names distinct?
  - quote: "Use distinct names for the app, the subscription group, and each subscription to avoid confusion."
  - surface: asc
  - verify: Compare the app name, each Subscription Group Display Name, and each Subscription Display Name in App Store Connect; flag duplicates.
  - fix: Rename the group/subscriptions so each is distinct and descriptive.

---

## IAP.SUB-MULTIAPP Auto-renewable subscriptions — Offering subscriptions to multiple apps

**Source text (verbatim):**
> You can offer auto-renewable subscriptions to access multiple apps. Each app must be approved to use auto-renewable Apple In-App Purchases and published under the same developer account.
>
> Use App Store Connect to set up separate and equivalent auto-renewable subscriptions for each app included in the multiapp subscription so that people can subscribe from any app. To help people avoid paying multiple times for the same offering, make sure to verify that they’re active subscribers before showing any subscription options. View details on determining if a subscription is active.

**Applies to:** Apps whose subscription grants access to multiple apps
**Requires:** subscriptions

- **[IAP-78]** Are all apps in the multiapp subscription published under the same developer account?
  - quote: "Each app must be approved to use auto-renewable Apple In-App Purchases and published under the same developer account."
  - surface: asc
  - verify: Confirm each app in the multiapp offering appears under the same App Store Connect team.
  - fix: manual — requires developer decision/legal/business action.
- **[IAP-79]** For a multiapp subscription, does the app verify that someone is an active subscriber before showing any subscription options?
  - quote: "make sure to verify that they’re active subscribers before showing any subscription options"
  - surface: code
  - verify: Confirm the paywall presentation is gated on an entitlement check (`Transaction.currentEntitlements`, `Product.SubscriptionInfo.status(for:)`, server-side status) that runs before the paywall is shown.
  - fix: Check entitlement status (including from the server for cross-app access) before presenting the paywall.

---

## IAP.SUB-FAMILY Auto-renewable subscriptions — Family Sharing (business guidance)

**Source text (verbatim):**
> Family Sharing allows a subscriber to share access to an auto-renewable subscription with up to five family members across their Apple devices. With a streamlined, convenient user experience, Family Sharing can help you attract subscribers, encourage paid subscriptions, increase engagement, and improve retention. You can enable Family Sharing for your subscription in App Store Connect. Please note that this can’t be undone.
>
> Verify subscription access using purchase validation, then provide the proper access to subscribers and their family members. Whether a subscription is shared with a subscriber’s family by default depends on their subscription sharing settings and if the purchase was made before or after you enabled Family Sharing in App Store Connect. Subscribers whose settings don’t share the subscription by default are informed by Apple via push notification that the subscription can be shared with their family.
>
> You can highlight Family Sharing in several ways:
>
> Highlight Family Sharing to potential subscribers. Include Family Sharing in your subscription’s display name so it’s easy to spot when reviewing subscription options. If you offer a Family Sharing-enabled subscription alongside subscriptions that don’t include Family Sharing, you can note the price difference for the Family Sharing option on the sign up screen.
>
> Remind subscribers to enable Family Sharing. Mention Family Sharing within your app — for example, as part of onboarding for new subscribers or via in-app messaging for existing subscribers. Consider explaining how to confirm they’ve turned on Family Sharing for the subscription. If you offer a Family Sharing-enabled subscription they’re not currently subscribed to, you might provide a way for them to upgrade without leaving your app. Make sure you’ve ranked your subscriptions within the same subscription level in App Store Connect to provide a seamless upgrade experience.
>
> Help subscribers share subscriptions. You can use in-app messaging to ask subscribers to confirm their Family Sharing settings, or implement share extensions so they can easily share your app. Within the transaction information, you can look at ownershipType to see if someone is the subscriber or a family member, so you can make sure to display your message to the person who completed the purchase.

**Applies to:** Apps with Family Sharing enabled for an auto-renewable subscription
**Requires:** subscriptions

- **[IAP-80]** Does the app verify subscription access via purchase validation and grant access to both subscribers and their family members?
  - quote: "Verify subscription access using purchase validation, then provide the proper access to subscribers and their family members."
  - surface: code
  - verify: Confirm entitlement checks accept verified transactions with `ownershipType` `.purchased` and `.familyShared` (do not filter out `.familyShared`).
  - fix: Grant access for both ownership types when the product is family-shareable.

---

## IAP.SUB-OFFERCODES Auto-renewable subscriptions — Offer codes

**Source text (verbatim):**
> Use offer codes to acquire, retain, and re-acquire subscribers by providing a subscription at a discount or for free for a limited time. You can create two types of offer codes: one-time-use codes (18-digit unique codes), or custom codes (such as SPRINGPROMO). Learn how to create offer codes and how to support offer codes using StoreKit. To get notified of redemptions, ensure you've set up App Store Server Notifications.
>
> Customers can redeem offer codes using a redemption URL or on the App Store (in iOS 14.2, iPadOS 14.2, and macOS 15 or later). They can also redeem offer codes within your app if your app supports the offerCodeRedemption method. For a smooth customer experience, be sure to mention any eligibility or availability limits in your communications.
>
> Apple handles the redemption experience, which includes an offer details screen that includes your app icon, subscription display name, duration, and pricing. If you’ve previously added a promotional image for the subscription, this is shown instead of your app icon. To help people make an informed decision, make sure that these details clearly describe the subscription experience. In order for offer codes to be redeemed, your app must be available on the App Store. If someone doesn’t have your app, they’ll be able to download it during the redemption experience.
>
> Depending on your subscription setup, existing subscribers may be able to redeem more than one offer if the offers are in different subscription groups. If you intend for someone to subscribe to only one subscription group at a time, make sure the offer is within their current subscription group. Existing subscribers can only redeem codes that are an upgrade from or at the same level as their current subscription.

**Applies to:** Apps that offer subscription offer codes
**Requires:** subscriptions

- **[IAP-117]** If offer codes are distributed, is the app available on the App Store?
  - quote: "In order for offer codes to be redeemed, your app must be available on the App Store."
  - surface: asc
  - verify: App Store Connect > app: confirm a version is live (Ready for Distribution) in the storefronts where codes are distributed before codes go out.
  - fix: manual — requires developer decision/legal/business action (schedule code distribution after the app is available).
- **[IAP-118]** Do offer code communications mention any eligibility or availability limits?
  - quote: "be sure to mention any eligibility or availability limits in your communications"
  - surface: manual
  - verify: Review the emails, flyers, in-app merchandising or web pages that carry offer codes for eligibility/availability limits.
  - fix: Add the limits to the communication copy.
- **[IAP-119]** If the app needs to know about offer code redemptions, are App Store Server Notifications set up?
  - quote: "To get notified of redemptions, ensure you've set up App Store Server Notifications."
  - surface: asc
  - verify: App Store Connect > App Information > App Store Server Notifications: production and sandbox URLs set (see IAP-07).
  - fix: Enter the server notification URLs.
- **[IAP-120]** Do the subscription display name, duration, and pricing shown on Apple's offer details screen clearly describe the subscription experience?
  - quote: "To help people make an informed decision, make sure that these details clearly describe the subscription experience."
  - surface: asc
  - verify: Review each subscription's localized display name and description, duration, and price in App Store Connect for accuracy against what the subscription unlocks in the app.
  - fix: Edit the localized display name/description (changes require review).
- **[IAP-128]** If people should hold only one subscription group at a time, is each offer code's offer within the subscriber's current subscription group?
  - quote: "If you intend for someone to subscribe to only one subscription group at a time, make sure the offer is within their current subscription group."
  - surface: asc
  - verify: App Store Connect > Offer Codes: confirm the subscription each code targets is in the group the intended recipients already subscribe to.
  - fix: Create the offer on a subscription in the recipients' current group.

---

## IAP.SUB-WINBACK-GUIDE Auto-renewable subscriptions — Win-back offer configuration and merchandising

**Source text (verbatim):**
> When configuring win-back offers in App Store Connect, you provide offer details and select the offer priority. Your priority selection affects how your offer is ranked within your app, in someone’s Subscription settings, and on the App Store (if you’ve chosen to promote it). Apple uses your subscription display name and description when displaying your win-back offer, so be sure this information is accurate.
>
> If you’d like to display your offer on the App Store, you’ll need an approved subscription image. Aim for a simple graphic that’s different than your app icon or screenshots that conveys the essence of the Apple In-App Purchase included as part of the offer.

**Applies to:** Apps that offer win-back offers
**Requires:** subscriptions

- **[IAP-121]** For subscriptions with win-back offers, are the subscription display name and description accurate?
  - quote: "Apple uses your subscription display name and description when displaying your win-back offer, so be sure this information is accurate."
  - surface: asc
  - verify: Compare each such subscription's localized display name/description in App Store Connect with what the subscription actually provides in the app.
  - fix: Correct the localized display name/description.

---

## IAP.SUB-NOTIFY Auto-renewable subscriptions — Sending notifications

**Source text (verbatim):**
> When written thoughtfully, notifications can help people stay engaged with your service and keep their subscriptions active. To ensure a positive experience, make sure your notifications are timely, serve a clear purpose, and deliver meaningful information. You can also use push notifications to market your content — for example, promoting a subscription offer to people who haven’t yet subscribed. However, people must first explicitly opt in to receiving marketing push notifications via a method within your app that includes consent language and a clear way of opting out. Carefully consider the frequency, timing, and content of your notifications to ensure they always provide value to subscribers. Push notifications must not include sensitive personal or confidential information.

**Applies to:** Apps that send push notifications about subscriptions or offers
**Requires:** push

- **[IAP-122]** If the app sends marketing push notifications (e.g. promoting a subscription offer), do people first explicitly opt in within the app via a method with consent language and a clear way of opting out?
  - quote: "people must first explicitly opt in to receiving marketing push notifications via a method within your app that includes consent language and a clear way of opting out"
  - surface: code
  - verify: Find marketing/promotional push sends (server campaigns, notification categories). Confirm an in-app opt-in UI with consent text exists before such pushes are sent, and an opt-out control (e.g. a Settings toggle) is available.
  - fix: Add an in-app marketing-notifications opt-in with consent language and an opt-out toggle; send marketing pushes only to opted-in users.
- **[IAP-123]** Are push notifications free of sensitive personal or confidential information?
  - quote: "Push notifications must not include sensitive personal or confidential information."
  - surface: code
  - verify: Review push payload templates (server code, notification content strings) for personal data, account details, or confidential information.
  - fix: Remove the sensitive content from notification payloads.

---

## IAP.SUB-MANAGE Auto-renewable subscriptions — Letting people manage their subscriptions; Retaining subscribers

**Source text (verbatim):**
> A subscriber’s preferences may change during a subscription period. You can use the showManageSubscriptions(in:) method to let them manage their subscription within your app. By providing a dedicated place in your app to manage subscriptions, you can also display other options to complement the system-provided management UI. For example, you might show a promotional offer that provides a higher service level for a discounted price. If they cancel, you might provide an offer to help win them back and encourage them to resubscribe. Or you might present a survey where they can share feedback about their subscription experience and reasons for cancelling, which can inform your marketing strategy. To ensure a positive experience, always make it easy for people to access the system-provided management UI where they can cancel if they wish.
>
> Voluntary churn. Determine if a subscriber has turned off auto-renew for a particular subscription using the Get All Subscription Statuses endpoint. You can also use App Store Server Notifications to get real-time updates about changes in a user’s status and key events related to their Apple In-App Purchases, such as a change in renewal status. Use this information to take action in response. For example, you might present a promotional offer or suggest an alternate tier that better fits their needs. When a subscription expires, you can lock access to the subscription’s content or service. Be sure to inform the user of any changes and let them know if there’s anything they need to do in response and how to resubscribe if needed.
>
> When a subscription renewal fails, Apple attempts to recover it for 60 days. If you’ve chosen to pause access to your service or content during this time, you’ll need to reinstate access once the issue is resolved. If the subscription renews within 60 days, the days of paid service resume from the renewal date.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-81]** Is it easy for people to access the system-provided subscription management UI where they can cancel?
  - quote: "always make it easy for people to access the system-provided management UI where they can cancel if they wish"
  - surface: code
  - verify: Grep for `showManageSubscriptions(in:)`, `.manageSubscriptionsSheet(isPresented:)`, or a link to `https://apps.apple.com/account/subscriptions`; at runtime confirm it is easy to reach (e.g. from Settings/Account) and clearly labeled.
  - fix: Add a "Manage Subscription" row in Settings that presents `.manageSubscriptionsSheet` / calls `AppStore.showManageSubscriptions(in:)`.
- **[IAP-82]** When a subscription expires and access is locked, does the app inform the user and tell them how to resubscribe?
  - quote: "Be sure to inform the user of any changes and let them know if there’s anything they need to do in response and how to resubscribe if needed."
  - surface: runtime
  - verify: With a sandbox subscription allowed to expire (or StoreKit Testing "Expire subscription"), relaunch and confirm the app shows a message explaining access ended and offers a way to resubscribe.
  - fix: Add an expired-state message with a resubscribe CTA.
- **[IAP-83]** If the app pauses access during a billing failure, does it reinstate access once the issue is resolved?
  - quote: "If you’ve chosen to pause access to your service or content during this time, you’ll need to reinstate access once the issue is resolved."
  - surface: code
  - verify: Confirm entitlement state is recomputed on `Transaction.updates` / `Product.SubscriptionInfo.Status` changes (billing retry → subscribed) rather than cached permanently as expired.
  - fix: Re-evaluate entitlements on transaction updates and app foreground.

---

## IAP.SK-REFUND Apple In-App Purchase — Refund requests

**Source text (verbatim):**
> Let people request refunds directly within your app by using the beginRefundRequest API and providing a dedicated place in your app for these requests. You can also provide other options — such as technical support or in-app credits — before the option to request a refund.
>
> If youʼve enabled App Store Server Notifications, youʼll receive a notification when someone receives a refund. You can use this information to take action — for example, updating the account balance based on the refund or restricting access to content unlocked by the Apple In‑App Purchase. If you choose to take action, inform the user of any changes and let them know if there’s anything they need to do. You can also identify if someone previously received refunds for any Apple In‑App Purchases made in your app using the Get Refund History endpoint.
>
> Apple uses a variety of factors to determine whether a refund request is approved or denied. To help inform and improve the refund process, you can send information about a user’s Apple In‑App Purchase (including auto-renewable subscriptions) to Apple via the Send Consumption Information endpoint in the App Store Server API (for example, if they used the Apple In-App Purchase or you were unable to deliver the purchase). Data is incorporated into our refund logic, to help ensure flexible, accurate, and informed decision making.

**Applies to:** Apps that offer In-App Purchases
**Requires:** iap, subscriptions

- **[IAP-84]** If the app restricts access or updates balances after a refund, does it inform the user of the change?
  - quote: "If you choose to take action, inform the user of any changes and let them know if there’s anything they need to do."
  - surface: code
  - verify: Find refund-handling code (`revocationDate`, `revocationReason`, server `REFUND`); confirm a user-facing message accompanies the change.
  - fix: Present a message describing the change and any needed action.

---

## IAP.SK-RESTORE Apple In-App Purchase — Purchase management

**Source text (verbatim):**
> If someone redownloads your app or switches to a new device, be sure to immediately provide access to the content or functionality from their past Apple In‑App Purchases. Use the currentEntitlements property in StoreKit to understand a user’s entitlements and provide access accordingly. Your app must also include a restore mechanism for any restorable Apple In‑App Purchases, per App Review Guideline 3.1.1.
>
> If someone requests support for an Apple In‑App Purchase, you can use the Look Up Order ID endpoint to make sure you’re taking action on the right purchase. Simply ask the user for the Order ID included on their email receipt from Apple, then use the endpoint to confirm the invoice and any associated information — for example, whether the user has already received a refund for their purchase — or to match the date and time of the purchase with your records.

**Applies to:** Apps that offer restorable In-App Purchases (non-consumables, auto-renewable subscriptions, non-renewing subscriptions)
**Requires:** iap, subscriptions

- **[IAP-85]** Does the app include a restore mechanism for restorable In-App Purchases?
  - quote: "Your app must also include a restore mechanism for any restorable Apple In‑App Purchases, per App Review Guideline 3.1.1."
  - surface: code
  - verify: Grep for `AppStore.sync()`, `restoreCompletedTransactions`, `.storeButton(.visible, for: .restorePurchases)`, or StoreKit views that include restore; confirm a visible "Restore Purchases" control exists (paywall and/or Settings) when the app sells non-consumables or subscriptions.
  - fix: Add a Restore Purchases button that calls `try await AppStore.sync()` and refreshes entitlements.
- **[IAP-86]** On redownload or a new device, does the app immediately provide access to past purchases using current entitlements?
  - quote: "be sure to immediately provide access to the content or functionality from their past Apple In‑App Purchases"
  - surface: code
  - verify: Confirm launch-time code iterates `Transaction.currentEntitlements` (SK2) to unlock content, rather than relying only on local flags (`UserDefaults`, Keychain) set at purchase time. At runtime: delete and reinstall the app signed into a sandbox account with a purchase; content should unlock without buying again.
  - fix: On launch, compute entitlements from `Transaction.currentEntitlements` and unlock accordingly.

---

## IAP.HIG-TECH HIG Apple In-App Purchase — Apple In-App Purchase vs. Apple Pay

**Source text (verbatim):**
> Apple In-App Purchase and Apple Pay are different technologies that support different use cases. Use Apple In-App Purchase to sell virtual goods in your app, such as premium content for your app and subscriptions for digital content. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations.

**Applies to:** Apps that sell anything in-app

- **[IAP-124]** Does the app use Apple In-App Purchase for virtual goods (premium content, subscriptions for digital content) and Apple Pay — not In-App Purchase — for physical goods, the listed services, and donations?
  - quote: "Use Apple In-App Purchase to sell virtual goods in your app, such as premium content for your app and subscriptions for digital content. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations."
  - surface: code
  - verify: List everything the app sells. Grep for StoreKit purchase calls (`product.purchase(`, `SKPaymentQueue.default().add(`) and PassKit (`PKPaymentRequest`, `PayWithApplePayButton`); confirm digital content/subscriptions go through StoreKit and physical goods/services/donations do not.
  - fix: Move each item to the matching technology.

---

## IAP.HIG-BEST HIG Apple In-App Purchase — Best practices

**Source text (verbatim):**
> Let people experience your app before making a purchase. People may be more inclined to invest in paid items or features after they’ve enjoyed your app and discovered its value. If you offer Auto-renewable subscriptions, consider supporting limited free access to your content.
>
> Design an integrated shopping experience. You don’t want people to think they’ve entered a different app when they browse and purchase your digital products. Present products and handle transactions in ways that mirror the style of your app.
>
> Use simple, succinct product names and descriptions. Titles that don’t truncate or wrap and plain, direct language can help people find products quickly.
>
> Display the total billing price for each in-app purchase you offer, regardless of type. People need to know the total billing amount for every purchase they consider.
>
> Display your store only when people can make payments. If someone canʼt make payments — for example, because of parental restrictions — consider hiding your store or displaying UI that explains why the store isnʼt available. For developer guidance, see canMakePayments.
>
> Use the default confirmation sheet. When someone makes a purchase using Apple In-App Purchase, the system displays a confirmation sheet to help prevent accidental purchases. Don’t modify or replicate this sheet.

**Applies to:** Apps that offer In-App Purchases
**Requires:** iap, subscriptions

- **[IAP-87]** Does the app display the total billing price for every in-app purchase it offers (consumables and non-consumables included)?
  - quote: "Display the total billing price for each in-app purchase you offer, regardless of type."
  - surface: runtime
  - verify: Open every store/purchase button and confirm the price (from `product.displayPrice`) is visible before purchase.
  - fix: Show `product.displayPrice` on each purchase button/row.
- **[IAP-88]** Does the app display its store only when people can make payments (HIG suggests hiding the store or explaining why it isn't available)?
  - quote: "Display your store only when people can make payments."
  - surface: code
  - verify: Grep for `AppStore.canMakePayments` / `SKPaymentQueue.canMakePayments()`; confirm the store UI branches on it.
  - fix: Check `AppStore.canMakePayments` and hide the store or show an explanation.
- **[IAP-89]** Does the app use the system confirmation sheet unmodified and avoid replicating it?
  - quote: "Don’t modify or replicate this sheet."
  - surface: code
  - verify: Confirm purchases go through StoreKit (`product.purchase()`, `SKPaymentQueue.add(_:)`, StoreKit views) and that no custom view imitates the App Store payment sheet (e.g. a custom "Confirm purchase / Double-click to pay" modal before calling purchase).
  - fix: Remove any custom imitation sheet and rely on the system confirmation sheet.
- **[IAP-90]** (HIG best practice) Are product names and descriptions simple and succinct, with titles that don't truncate or wrap?
  - quote: "Use simple, succinct product names and descriptions. Titles that don’t truncate or wrap and plain, direct language can help people find products quickly."
  - surface: runtime
  - verify: View the store on the smallest supported device and largest Dynamic Type size; check product titles for truncation (…) or wrapping.
  - fix: Shorten display names (≤ 30 characters per IAP-22) or adjust layout.

---

## IAP.HIG-FAMILY HIG Apple In-App Purchase — Supporting Family Sharing

**Source text (verbatim):**
> People can use Family Sharing to share access to their purchased content, such as auto-renewable subscriptions and non-consumable in-app purchases, with up to five additional family members, across all their Apple devices. To encourage people to take advantage of the Family Sharing support you offer, consider the following guidelines.
>
> Prominently mention Family Sharing in places where people learn about the content you offer. For example, including “Family” or “Shareable” in a subscription or item name and referring to Family Sharing in your sign-up screen can highlight the feature and help people make an informed choice.
>
> Help people understand the benefits of Family Sharing and how to participate. When you turn on Family Sharing, people can receive notifications about the change, depending on their current settings. For example, an existing subscriber whose sharing setting is turned off (the default) receives a notice from Apple that invites them to share their subscription with family members. Similarly, a family member can get a notification about content that’s being shared with them. To learn more about the types of notifications people can receive, see Auto-renewable subscriptions.
>
> Aim to customize your in-app messaging so that it makes sense to both purchasers and family members. For example, when a family member views shared content for the first time, you might welcome them with wording like “Your family subscription includes…”.

**Applies to:** Apps with Family Sharing enabled (advisory guidance)
**Requires:** iap, subscriptions

- **[IAP-91]** If Family Sharing is enabled, is it mentioned where people learn about the content (e.g., product name or sign-up screen)?
  - quote: "Prominently mention Family Sharing in places where people learn about the content you offer."
  - surface: runtime
  - verify: For family-shareable products, check the paywall/sign-up screen and display names for a Family Sharing mention.
  - fix: Add "Family" / "Shareable" wording or a Family Sharing note on the sign-up screen.

---

## IAP.HIG-HELP HIG Apple In-App Purchase — Providing help (refunds)

**Source text (verbatim):**
> Sometimes, people need help with a purchase or want to request a refund. To help make this experience convenient, you can present custom UI within your app that provides assistance, offers alternative solutions, and helps people initiate the system-provided refund flow. For developer guidance, see beginRefundRequest(for:in:); for related guidance specific to auto-renewable subscriptions, see Helping people manage their subscriptions.
>
> Provide help that customers can view before they request a refund. In addition to including a link to the system-provided refund flow, your custom purchase-help screen can provide assistance you tailor to your app. For example, your custom screen might help people resolve problems with missing purchases, answer frequently asked questions about the in-app purchases you offer, and give people ways to submit feedback or contact you directly for support.
>
> Use a simple title for the refund action, like “Refund” or “Request a Refund”. The system-provided refund flow makes it clear that people request a refund from Apple, so there’s no need to reiterate this information.
>
> Help people find the problematic purchase. For each recent purchase you display, include contextual information that helps people identify the one they want. For example, you might display an image of the product — along with its name and description — and list the original purchase date.
>
> Consider offering alternative solutions. For example, if the customer didn’t receive the item they purchased, you might offer immediate fulfillment or a conciliatory item. Regardless of the alternatives you offer, make it clear that people can still request a refund.
>
> Make it easy for people to request a refund. Although your purchase-help screen can offer useful information and alternative solutions, make sure this content doesn’t create a barrier to requesting a refund. For example, avoid making people scroll or open another screen to reveal your refund-request button. When people choose your refund-request item, they automatically enter the system-provided refund flow shown below.
>
> Avoid characterizing or providing guidance on Apple’s refund policies. For example, don’t speculate about whether customers will receive the refund they request. To help people understand the refund-request process, you can provide a link to Request a refund for apps or content that you bought from Apple.

**Applies to:** Apps that present custom purchase-help / refund UI
**Requires:** iap, subscriptions

- **[IAP-92]** If the app has a purchase-help screen, does its refund action use a simple title (like “Refund” or “Request a Refund”) and enter the system-provided refund flow?
  - quote: "Use a simple title for the refund action, like “Refund” or “Request a Refund”."
  - surface: code
  - verify: Grep for `beginRefundRequest` / `.refundRequestSheet(for:isPresented:)`; check the button label string.
  - fix: Use `.refundRequestSheet` / `Transaction.beginRefundRequest(in:)` with a "Request a Refund" label.
- **[IAP-93]** If alternatives are offered, does the help screen keep the refund-request button visible without scrolling or opening another screen?
  - quote: "make sure this content doesn’t create a barrier to requesting a refund. For example, avoid making people scroll or open another screen to reveal your refund-request button."
  - surface: runtime
  - verify: Open the purchase-help screen on the smallest supported device; the refund button must be visible without scrolling or navigating further.
  - fix: Move the refund button above the fold.
- **[IAP-94]** Does the app avoid characterizing Apple’s refund policies or speculating whether a refund will be granted?
  - quote: "Avoid characterizing or providing guidance on Apple’s refund policies."
  - surface: code
  - verify: Grep localized strings near refund UI for statements about refund eligibility/outcomes (e.g. "you will be refunded", "Apple will approve").
  - fix: Remove such statements; optionally link to Apple's "Request a refund for apps or content that you bought from Apple" support article.

---

## IAP.HIG-SUBS HIG Apple In-App Purchase — Auto-renewable subscriptions

**Source text (verbatim):**
> Call attention to subscription benefits during onboarding. By showing the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they’ll gain by subscribing. Include a strong call to action and a clear summary of subscription terms (see Making signup effortless). For related guidance, see Onboarding.
>
> Offer a range of content choices, service levels, and durations. People appreciate the flexibility to choose the subscription that best meets their needs.
>
> Consider letting people try your content for free before signing up. Limited free access gives people the opportunity to sample your content and encourages people who already engaged with your content to sign up. For example, you might offer a freemium app, a metered paywall, or a free trial.
>
> Prompt people to subscribe at relevant times, like when they near their monthly limit of free content. Additionally, consider making it easy for people to subscribe at any time by including prompts at relevant points throughout your app.
>
> Encourage a new subscription only when someone isn’t already a subscriber. Otherwise, people may believe their existing subscription has lapsed when that’s not actually the case. If you offer the same subscription options in multiple apps or through your website, provide a sign-in option so people don’t think they have to pay multiple times for the same service.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-95]** Does the app avoid prompting existing subscribers to subscribe?
  - quote: "Encourage a new subscription only when someone isn’t already a subscriber."
  - surface: runtime
  - verify: With an active sandbox subscription, navigate the app (launch, onboarding, gated features) and confirm no subscribe paywall/upsell for the already-held subscription appears. In code, confirm paywall triggers check entitlement first.
  - fix: Gate paywall presentation on entitlement status.
- **[IAP-96]** If the same subscription is offered in multiple apps or through a website, does the app provide a sign-in option?
  - quote: "If you offer the same subscription options in multiple apps or through your website, provide a sign-in option so people don’t think they have to pay multiple times for the same service."
  - surface: code
  - verify: If the service sells the subscription elsewhere (web, other apps), confirm a "Sign in" entry point exists on/near the paywall.
  - fix: Add a sign-in option on the paywall.

---

## IAP.HIG-SIGNUP HIG Apple In-App Purchase — Making signup effortless

**Source text (verbatim):**
> A simple and informative sign-up experience makes it easy for people to act on their interest in your content, whether they’re in your app or viewing your App Store product page.
>
> Provide clear, distinguishable subscription options. Use short, self-explanatory names that differentiate subscription options from one another, and specify the price and duration for each option. If you offer an introductory price, be sure to list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends.
>
> Simplify initial signup by asking only for necessary information. A lengthy sign-up process may lower your subscription conversion rate. Defer asking for additional information until after people have signed up.
>
> In your tvOS app, help people sign up or authenticate using another device. Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need.
>
> Give people more information in your app’s sign-up screen. In addition to including links to your Terms of Service and Privacy Policy in your app and App Store metadata, the in-app sign-up screen needs to include:
> - The subscription name, duration, and the content or services provided during each subscription period
> - The billing amount, correctly localized for the territories and currencies where the subscription is available for purchase
> - A way for existing subscribers to sign in or restore purchases
>
> For example, the Forest Explorer sign-up screen displays billing totals for monthly, biannual, and annual subscriptions in the most prominent positions. In subordinate positions, it shows breakdowns of the biannual and annual prices, so that people can compare the values and make an informed choice. The sign-up screen also contains a button that existing subscribers can use to restore their purchases.
>
> Clearly describe how a free trial works. It’s particularly important to make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period. For example, the Ocean Journal sign-up screen explicitly states both the duration of the free trial and the amount that’s billed when it ends.
>
> Include a sign-up opportunity in your app’s settings. App and account settings are common places for people to look for a way to subscribe.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions, tvos

- **[IAP-97]** If an introductory price is offered, does the sign-up screen list the introductory price, the offer duration, and the standard price after the offer ends?
  - quote: "be sure to list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends"
  - surface: runtime
  - verify: With an eligible sandbox account, open the paywall and confirm all three values are shown for each option with an intro offer (from `introductoryOffer.displayPrice`, `introductoryOffer.period`, `product.displayPrice`).
  - fix: Render all three values from StoreKit on the paywall.
- **[IAP-98]** Does the free-trial copy make clear that a payment will be automatically initiated when the trial ends?
  - quote: "make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period"
  - surface: runtime
  - verify: Read the trial paywall copy; it must state that billing starts automatically after the trial (e.g. "then $X/year, auto-renews until canceled").
  - fix: Add explicit auto-renew/billing-after-trial wording.
- **[IAP-99]** Is there a sign-up opportunity in the app's settings?
  - quote: "Include a sign-up opportunity in your app’s settings."
  - surface: code
  - verify: Inspect the Settings/Account screen for a subscribe/upgrade entry that opens the paywall.
  - fix: Add a "Subscribe"/"Upgrade" row in Settings.
- **[IAP-100]** In a tvOS app, does sign-up/authentication avoid requiring text input on the TV by using another device?
  - quote: "Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need."
  - surface: code
  - verify: For tvOS targets, inspect sign-up/login screens for `TextField`/`UITextField` credential entry vs. a device-code / companion-device flow.
  - fix: Implement a code-based sign-in on another device.

---

## IAP.HIG-OFFERCODES HIG Apple In-App Purchase — Supporting offer codes

**Source text (verbatim):**
> In iOS and iPadOS, subscription offer codes let you use both online and offline channels to give new, existing, and lapsed subscribers free or discounted access to your subscription content. For example, you might provide offer codes through email, give them out at a store or event, or print one on a physical product.
>
> There are two types of offer codes you can support:
> - A one-time use code is a unique code you generate in App Store Connect. People can redeem a one-time use code through a redemption URL (a shareable link), within your app (when you support redemption), or by entering it in the App Store, where they’re prompted to install your app if they haven’t already. Consider using one-time use codes when your distribution is small or when you need to restrict access to a code.
> - A custom code is a code you create, such as NEWYEAR or SPRINGSALE. People can redeem a custom code through a redemption URL or within your app (when you support redemption). Consider using a custom code when you want to support a large campaign that requires a mass distribution of codes.
>
> Clearly explain offer details. To help people make an informed decision, provide a straightforward and succinct description of your offer in your marketing materials.
>
> Follow guidelines for creating a custom code. A custom code can contain only alphanumeric ASCII characters. Don’t use special characters, including Chinese and Arabic characters.
>
> Tell people how to redeem a custom code. Because people can’t redeem a custom code by entering it in their App Store account settings, it’s important to let them know that they can redeem it through a redemption URL or within your app.
>
> Consider supporting offer redemption within your app. The system automatically provides screens that present the offer-redemption flow, whether people redeem the offer in your app or in the App Store. When you use StoreKit API to let people redeem offer codes within your app, the only custom UI you need to create is one that initiates the system-provided flow. For developer guidance, see presentOfferCodeRedeemSheet(from:options:) and offerCodeRedemption(options:isPresented:onCompletion:). There are several natural places to provide this custom UI. For example, you could add a “Redeem Code” button to your paywall, onboarding screens, or your app’s settings screen.
>
> Help people benefit from unlocked content as soon as they complete the redemption flow. Think about ways to align the post-redemption experience in your app with the subscriber’s new status. For example, you might provide a welcome experience for new subscribers or a brief tour of new features for an existing subscriber who’s unlocked additional functionality. In particular, be prepared to welcome people who subscribe before they open your app for the first time. For example, if you require people to create an account or sign in before they can use your app, make this process as smooth as possible for new subscribers who haven’t experienced it before.

**Applies to:** Apps that use subscription offer codes
**Requires:** subscriptions

- **[IAP-101]** Do custom offer codes contain only alphanumeric ASCII characters?
  - quote: "A custom code can contain only alphanumeric ASCII characters."
  - surface: asc
  - verify: App Store Connect > subscription > Offer Codes: check each custom code against `^[A-Za-z0-9]+$`.
  - fix: Create a new custom code with only alphanumeric ASCII characters.
- **[IAP-125]** For custom offer codes, are people told they can redeem them through a redemption URL or within the app (not in App Store account settings)?
  - quote: "Because people can’t redeem a custom code by entering it in their App Store account settings, it’s important to let them know that they can redeem it through a redemption URL or within your app."
  - surface: manual
  - verify: Review custom-code marketing copy and any in-app messaging for redemption instructions (redemption URL or in-app "Redeem Code").
  - fix: Add redemption instructions to the custom code communications.
- **[IAP-102]** If the app supports offer code redemption in-app, does its custom UI initiate the system-provided redemption flow?
  - quote: "When you use StoreKit API to let people redeem offer codes within your app, the only custom UI you need to create is one that initiates the system-provided flow."
  - surface: code
  - verify: Grep for `presentOfferCodeRedeemSheet`, `.offerCodeRedemption(`; confirm the "Redeem Code" control invokes it.
  - fix: Wire the "Redeem Code" control to `.offerCodeRedemption(isPresented:)` / `presentOfferCodeRedeemSheet`.
- **[IAP-103]** After redemption, are unlocked features available immediately (including for people who subscribe before first opening the app)?
  - quote: "Help people benefit from unlocked content as soon as they complete the redemption flow."
  - surface: code
  - verify: Confirm the redemption completion handler / `Transaction.updates` listener refreshes entitlements immediately; for first-launch, confirm entitlements are read from `Transaction.currentEntitlements` before showing a paywall.
  - fix: Refresh entitlements on redemption completion and on launch.

---

## IAP.HIG-MANAGE HIG Apple In-App Purchase — Helping people manage their subscriptions

**Source text (verbatim):**
> Supporting subscription management means people can upgrade, downgrade, or cancel a subscription without leaving your app. Offering subscription management within your app also gives you a natural place to provide help for common subscriber issues and present alternative offers for people to consider.
>
> Provide summaries of the customer’s subscriptions. In particular, people appreciate viewing the upcoming renewal date without having to search for it. Consider displaying this information in a settings or account screen, near the subscription-management option. For developer guidance, see Product.SubscriptionInfo.
>
> Consider using the system-provided subscription-management UI. Using StoreKit APIs lets you present a consistent experience that helps people manage or cancel their subscriptions without leaving your app. For developer guidance, see showManageSubscriptions(in:).
>
> Encourage a subscriber to keep their subscription or resubscribe later. When someone attempts to cancel, consider reminding them what they’d lose access to, suggesting a different plan, or offering a discount to encourage them to stay subscribed. If someone still cancels, consider reaching out later with a personalized, discounted offer to resubscribe. For developer guidance, see Retention Messaging API and Win-back offers.
>
> Always make it easy for customers to cancel an auto-renewable subscription. If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they’re being discouraged or prevented from canceling.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAP-104]** Is the manage-subscription action easy to find (not deep within the app or hard to recognize)?
  - quote: "If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they’re being discouraged or prevented from canceling."
  - surface: runtime
  - verify: From the main screen, count taps to reach a clearly labeled "Manage Subscription" action; confirm the label is recognizable.
  - fix: Place a clearly labeled "Manage Subscription" entry in Settings/Account.
- **[IAP-105]** Does any retention/cancel flow still let the user proceed to cancel easily?
  - quote: "Always make it easy for customers to cancel an auto-renewable subscription."
  - surface: runtime
  - verify: Trigger the manage/cancel path; if the app shows a retention offer or survey first, confirm a clear way to continue to the system management UI is visible on the same screen.
  - fix: Add a prominent "Continue to cancel" / "Manage in App Store" button on retention screens.

---

## IAP.HIG-WATCHOS HIG Apple In-App Purchase — watchOS sign-up screen

**Source text (verbatim):**
> The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app. For the complete list of required items, see Making signup effortless. The following guidelines can help you design a sign-up screen that feels at home on Apple Watch.
>
> Clearly describe the differences between versions of your app that run on different devices. If your watchOS app supports different functionality or provides a subset of the content that’s available on other devices, be sure to clarify these differences in your description. Be straightforward about the advantages of accessing subscription content through your watchOS app without implying that the experience is identical to the ones in other versions of your app.
>
> Consider using a modal sheet to display the required information. After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single view. Even though people must scroll the view to access all the information, displaying it in a modal sheet helps your app UI remain streamlined and concise. Also, a modal sheet’s default Close button makes it easy for people to return to your free content with one tap. If you create a custom sign-up view instead of using a modal sheet, design a complete, efficient flow and include a Close or Cancel button that lets people return to your free content.
>
> Make subscription options easy to compare on a small screen. People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that’s easy to scan and compare. Here are two ways you might present subscription options in your watchOS app:
> - Display each option in a separate button. Using one button per payment option lets people start the signup process with one tap. In this design, it’s important to lock up each button with its description so that people can see how these elements are related, especially while scrolling.
> - Display a list of options, followed by a button people tap to start the signup process. Using a list to display one option per row gives you a compact design that minimizes scrolling while making subscription choices easy to scan and understand. In this design, the button’s title can update to reflect the chosen option.

**Applies to:** watchOS apps with a subscription sign-up screen
**Requires:** watchos, subscriptions

- **[IAP-106]** Does the watchOS sign-up screen display the same subscription information shown in other versions of the app (name, duration, content, localized billing amount, sign-in/restore)?
  - quote: "The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app."
  - surface: code
  - verify: For watchOS targets with a paywall, compare displayed fields with the iOS paywall (see IAP-70–IAP-73).
  - fix: Add the missing fields to the watchOS sign-up view.
- **[IAP-126]** If the watchOS app offers different functionality or a subset of content, does its subscription description clarify the differences without implying the experience is identical to other versions?
  - quote: "If your watchOS app supports different functionality or provides a subset of the content that’s available on other devices, be sure to clarify these differences in your description."
  - surface: code
  - verify: Read the watchOS sign-up screen's subscription description strings and compare with the watchOS feature set.
  - fix: Add copy describing what the subscription provides on Apple Watch versus other devices.
- **[IAP-107]** If the watchOS sign-up view is custom (not a modal sheet), does it include a Close or Cancel button back to free content?
  - quote: "include a Close or Cancel button that lets people return to your free content"
  - surface: code
  - verify: Inspect the watchOS paywall view for a dismiss control.
  - fix: Present the paywall as a sheet or add a Close/Cancel button.

---

## Sources

| URL | Page title |
|---|---|
| https://developer.apple.com/app-store/subscriptions/ | Auto-renewable subscriptions |
| https://developer.apple.com/in-app-purchase/ | Simple and safe Apple In-App Purchases |
| https://developer.apple.com/design/human-interface-guidelines/in-app-purchase (redirects to https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase; content read from https://developer.apple.com/tutorials/data/design/human-interface-guidelines/apple-in-app-purchase.json) | Apple In-App Purchase (Human Interface Guidelines) |
| https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/overview-for-configuring-in-app-purchases | (404 — "The page you’re looking for can’t be found.") |
| https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases | Overview for configuring In-App Purchases |
| https://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions | Offer auto-renewable subscriptions |
| https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information | In-App Purchase information |
| https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-information | Auto-renewable subscription information |
| https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-types | In-App Purchase types |
| https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-statuses | In-App Purchase statuses |
| https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-consumable-or-non-consumable-in-app-purchases | Create consumable or non-consumable In-App Purchases |
| https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information | View and edit In-App Purchase information |
| https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-purchase | Submit an In-App Purchase |
| https://developer.apple.com/help/app-store-connect/manage-subscriptions/create-non-renewing-subscriptions | Create non-renewing subscriptions |
| https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions | Set up introductory offers for auto-renewable subscriptions |
| https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions | Set up promotional offers for auto-renewable subscriptions |
| https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers | Set up win-back offers |
| https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/turn-on-family-sharing-for-in-app-purchases | Turn on Family Sharing for In-App Purchases |
| https://developer.apple.com/documentation/storekit/supporting-family-sharing-in-your-app (via https://developer.apple.com/tutorials/data/documentation/storekit/supporting-family-sharing-in-your-app.json) | Supporting Family Sharing in your app |
| https://developer.apple.com/documentation/storekit/handling-refund-notifications (via https://developer.apple.com/tutorials/data/documentation/storekit/handling-refund-notifications.json) | Handling refund notifications |
