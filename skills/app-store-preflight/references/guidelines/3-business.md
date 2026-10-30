# App Review Guidelines — 3. Business
Source: https://developer.apple.com/app-store/review/guidelines/#business  
Retrieved: 2026-10-30

Guidelines document "Last Updated: October 16, 2026".

## 3 Business

**Source text (verbatim):**
> 3. Business
>
> There are many ways to monetize your app on the App Store. If your business model isn’t obvious, make sure to explain in its metadata and App Review notes. If we can’t understand how your app works or your in-app purchases aren’t immediately obvious, it will delay your review and may trigger a rejection. And while pricing is up to you, we won’t distribute apps and in-app purchase items that are clear rip-offs. We’ll reject expensive apps that try to cheat users with irrationally high prices.
>
> If we find that you have attempted to manipulate reviews, inflate your chart rankings with paid, incentivized, filtered, or fake feedback, or engage with third-party services to do so on your behalf, we will take steps to preserve the integrity of the App Store, which may include expelling you from the Apple Developer Program.

**Applies to:** All apps

- **[3-01]** If the app's business model isn’t obvious, is it explained in the app's metadata and in the App Review notes?
  - quote: "If your business model isn’t obvious, make sure to explain in its metadata and App Review notes."
  - surface: asc
  - verify: Identify the monetization model from code (StoreKit `Product`/`SKProduct` usage, `.storekit` config files, paywall views, ad SDKs, external payment code). In App Store Connect > App > iOS App > version page, read Description and App Review Information > Notes; confirm they state how the app makes money / what is paid.
  - fix: Add a plain-language explanation of the business model (what is free, what is paid, how purchases are made) to the App Review notes and, where relevant, the Description.
- **[3-02]** Are the app's in-app purchases immediately obvious (discoverable and understandable) to the reviewer?
  - quote: "If we can’t understand how your app works or your in-app purchases aren’t immediately obvious, it will delay your review and may trigger a rejection."
  - surface: runtime
  - verify: Launch the app and locate every paywall/store entry point; confirm each IAP configured in App Store Connect > Monetization > In-App Purchases / Subscriptions is reachable. Check App Review notes describe where to find IAPs if gated behind onboarding or accounts.
  - fix: Add clear entry points to purchase screens and document in App Review notes the exact steps to reach each IAP (including demo account credentials if needed).
- **[3-03]** Are app and in-app purchase prices free of clear rip-offs / irrationally high prices intended to cheat users?
  - quote: "we won’t distribute apps and in-app purchase items that are clear rip-offs. We’ll reject expensive apps that try to cheat users with irrationally high prices."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability (app price) and Monetization > In-App Purchases / Subscriptions (each product's price). Compare price against the content/value delivered.
  - fix: manual — requires developer decision/legal/business action (re-price products to reflect delivered value).
- **[3-04]** Is the developer free of any attempts to manipulate reviews or inflate chart rankings with paid, incentivized, filtered, or fake feedback (directly or via third-party services)?
  - quote: "If we find that you have attempted to manipulate reviews, inflate your chart rankings with paid, incentivized, filtered, or fake feedback, or engage with third-party services to do so on your behalf"
  - surface: code
  - verify: Grep for review-gating logic: code that asks "Do you like the app?" before calling `SKStoreReviewController.requestReview` / `AppStore.requestReview` / `requestReview` environment action only for positive responses; code that rewards users for ratings/reviews; third-party "review booster" SDKs. Developer must also attest to no paid/fake review services.
  - fix: Remove filtering/incentive logic around review prompts (call the system review API unconditionally at appropriate moments); stop any paid/incentivized review campaigns (manual).

## 3.1 Payments

**Source text (verbatim):**
> 3.1 Payments

**Applies to:** All apps (parent heading of 3.1.1–3.1.5)

**Status:** Heading only — no requirement text of its own; see sub-guidelines 3.1.1–3.1.5. No checks.

## 3.1.1 In-App Purchase

**Source text (verbatim):**
> 3.1.1 In-App Purchase:
>
> - If you want to unlock features or functionality within your app, (by way of example: subscriptions, in-game currencies, game levels, access to premium content, or unlocking a full version), you must use in-app purchase. Apps may not use their own mechanisms to unlock content or functionality, such as license keys, augmented reality markers, QR codes, cryptocurrencies and cryptocurrency wallets, etc.
> - Apps may use in-app purchase currencies to enable customers to “tip” the developer or digital content providers in the app.
> - Any credits or in-game currencies purchased via in-app purchase may not expire, and you should make sure you have a restore mechanism for any restorable in-app purchases.
> - Apps may enable gifting of items that are eligible for in-app purchase to others. Such gifts may only be refunded to the original purchaser and may not be exchanged.
> - Apps distributed via the Mac App Store may host plug-ins or extensions that are enabled with mechanisms other than the App Store.
> - Apps offering “loot boxes” or other mechanisms that provide randomized virtual items for purchase must disclose the odds of receiving each type of item to customers prior to purchase.
> - Digital gift cards, certificates, vouchers, and coupons which can be redeemed for digital goods or services can only be sold in your app using in-app purchase. Physical gift cards that are sold within an app and then mailed to customers may use payment methods other than in-app purchase.
> - Non-subscription apps may offer a free time-based trial period before presenting a full unlock option by setting up a Non-Consumable IAP item at Price Tier 0 that follows the naming convention: “XX-day Trial.” Prior to the start of the trial, your app must clearly identify its duration, the content or services that will no longer be accessible when the trial ends, and any downstream charges the user would need to pay for full functionality. Learn more about managing content access and the duration of the trial period using Receipts and DeviceCheck.
> - Apps may use in-app purchase to sell and sell services related to non-fungible tokens (NFTs), such as minting, listing, and transferring. Apps may allow users to view their own NFTs, provided that NFT ownership does not unlock features or functionality within the app. Apps may allow users to browse NFT collections owned by others, provided that, except for apps on the United States storefront, the apps may not include buttons, external links, or other calls to action that direct customers to purchasing mechanisms other than in-app purchase.

**Applies to:** Apps that unlock features or functionality within the app (sub-bullets apply to apps with tipping, IAP credits/currencies, gifting, Mac App Store plug-ins, loot boxes, gift cards, free trials in non-subscription apps, or NFTs)

**Related:** Receipts; DeviceCheck

- **[3.1.1-01]** Is every paid unlock of features or functionality (subscriptions, in-game currencies, game levels, premium content, full version) done via in-app purchase?
  - quote: "If you want to unlock features or functionality within your app, (by way of example: subscriptions, in-game currencies, game levels, access to premium content, or unlocking a full version), you must use in-app purchase."
  - surface: code
  - verify: Find all premium/paywall gates (grep `isPro`, `isPremium`, `unlocked`, `entitlement`, `subscription`). Confirm each gate's unlock path is StoreKit (`Product.purchase`, `Transaction.currentEntitlements`, `SKPaymentQueue`, or RevenueCat/StoreKit wrappers) and not a web checkout (Stripe, PayPal, Braintree SDKs, `SFSafariViewController`/`openURL` to a payment page) — subject to the exceptions in 3.1.1(a) and 3.1.3.
  - fix: Replace non-IAP unlock flows for digital features/content with StoreKit in-app purchases configured in App Store Connect > Monetization.
- **[3.1.1-02]** Is the app free of its own unlock mechanisms such as license keys, augmented reality markers, QR codes, cryptocurrencies, or cryptocurrency wallets?
  - quote: "Apps may not use their own mechanisms to unlock content or functionality, such as license keys, augmented reality markers, QR codes, cryptocurrencies and cryptocurrency wallets, etc."
  - surface: code
  - verify: Grep for license/serial/activation code entry (`licenseKey`, `activationCode`, `serial`, `redeem` text fields not using `AppStore.presentOfferCodeRedeemSheet`), QR/barcode scanning (`AVCaptureMetadataOutput`, `VNDetectBarcodesRequest`, `DataScannerViewController`) or ARKit image anchors whose result sets an unlock flag, and crypto wallet SDKs (WalletConnect, web3) gating features.
  - fix: Remove custom unlock mechanisms; sell the content as an IAP (offer codes via `presentOfferCodeRedeemSheet` are the StoreKit path for redeemable codes).
- **[3.1.1-04]** Do credits or in-game currencies purchased via IAP never expire?
  - quote: "Any credits or in-game currencies purchased via in-app purchase may not expire"
  - surface: code
  - verify: Inspect credit/currency balance models (grep `credits`, `coins`, `gems`, `balance`, `expir`) on client and server for expiry dates, TTLs, or reset jobs applied to purchased balances.
  - fix: Remove expiry logic from purchased credits/currencies.
- **[3.1.1-05]** Does the app provide a restore mechanism for any restorable in-app purchases? (Apple states this as "should".)
  - quote: "you should make sure you have a restore mechanism for any restorable in-app purchases"
  - surface: code
  - verify: If the app has non-consumable or auto-renewable/non-renewing subscription products, grep for `AppStore.sync()`, `Transaction.currentEntitlements`, `SKPaymentQueue.default().restoreCompletedTransactions()`, `restorePurchases` (RevenueCat), or SwiftUI `SubscriptionStoreView`/`StoreView` restore button; confirm a visible "Restore Purchases" control exists. Exercise it at runtime with a sandbox account.
  - fix: Add a "Restore Purchases" button on the paywall/settings that calls `AppStore.sync()` (StoreKit 2) or `restoreCompletedTransactions()` and refreshes entitlements.
- **[3.1.1-06]** If the app allows gifting IAP-eligible items, can such gifts only be refunded to the original purchaser and not be exchanged?
  - quote: "Such gifts may only be refunded to the original purchaser and may not be exchanged."
  - surface: code
  - verify: Grep for gifting features (`gift`, `send to friend`); inspect server/client logic for refunds or exchange/convert-to-other-item flows on gifted items.
  - fix: Restrict gift refunds to the original purchaser and remove gift exchange functionality.
- **[3.1.1-07]** If plug-ins or extensions are enabled with mechanisms other than the App Store, is the app distributed via the Mac App Store?
  - quote: "Apps distributed via the Mac App Store may host plug-ins or extensions that are enabled with mechanisms other than the App Store."
  - surface: code
  - verify: Check for non-App Store plug-in/extension enablement (license-gated plug-ins); confirm the target platform is macOS (Mac App Store). On iOS/iPadOS/tvOS/watchOS/visionOS, such enablement falls under 3.1.1-01/02.
  - fix: For non-Mac platforms, move plug-in/extension unlocks to IAP.
- **[3.1.1-08]** If the app offers loot boxes or other randomized virtual items for purchase, does it disclose the odds of receiving each type of item before purchase?
  - quote: "Apps offering “loot boxes” or other mechanisms that provide randomized virtual items for purchase must disclose the odds of receiving each type of item to customers prior to purchase."
  - surface: runtime
  - verify: Grep for `lootbox`, `gacha`, `chest`, `crate`, `random`, `drop rate`, `odds` near purchase code; run the app and confirm odds per item type are displayed on or before the purchase screen.
  - fix: Add an odds disclosure (probability per item type) visible before the purchase is confirmed.
- **[3.1.1-09]** Are digital gift cards, certificates, vouchers, and coupons redeemable for digital goods or services sold only via in-app purchase?
  - quote: "Digital gift cards, certificates, vouchers, and coupons which can be redeemed for digital goods or services can only be sold in your app using in-app purchase."
  - surface: code
  - verify: Grep for `gift card`, `voucher`, `coupon`, `certificate` sale flows; confirm any that redeem for digital goods/services use StoreKit, not external payments. (Physical mailed gift cards may use other payment methods.)
  - fix: Sell digital gift cards/vouchers via IAP, or remove their in-app sale.
- **[3.1.1-10]** If a non-subscription app offers a free time-based trial, is it set up as a Non-Consumable IAP at Price Tier 0 named “XX-day Trial.”?
  - quote: "Non-subscription apps may offer a free time-based trial period before presenting a full unlock option by setting up a Non-Consumable IAP item at Price Tier 0 that follows the naming convention: “XX-day Trial.”"
  - surface: asc
  - verify: App Store Connect > Monetization > In-App Purchases: find the trial product; confirm Type = Non-Consumable, price = free (Tier 0), Reference Name/Display Name follows “XX-day Trial.” (e.g., “14-day Trial”). Cross-check product ID in code.
  - fix: Create/rename the trial IAP as a free Non-Consumable named “XX-day Trial.” and use it to start the trial.
- **[3.1.1-11]** Before the trial starts, does the app clearly identify the trial duration, the content/services that will no longer be accessible when it ends, and any downstream charges for full functionality?
  - quote: "Prior to the start of the trial, your app must clearly identify its duration, the content or services that will no longer be accessible when the trial ends, and any downstream charges the user would need to pay for full functionality."
  - surface: runtime
  - verify: Run the app to the trial-start screen; confirm all three items (duration, what is lost after trial, price of full unlock) are shown before the trial-start action.
  - fix: Add trial duration, post-trial limitations, and full-unlock price text to the trial-start screen.
- **[3.1.1-13]** If users can view their own NFTs, does NFT ownership avoid unlocking features or functionality in the app?
  - quote: "Apps may allow users to view their own NFTs, provided that NFT ownership does not unlock features or functionality within the app."
  - surface: code
  - verify: Search for logic that checks NFT/token ownership (wallet address lookups, contract calls) and sets feature flags/entitlements.
  - fix: Remove feature unlocks based on NFT ownership.
- **[3.1.1-14]** Outside the United States storefront, are NFT-browsing apps free of buttons, external links, or other calls to action directing customers to non-IAP purchasing mechanisms?
  - quote: "except for apps on the United States storefront, the apps may not include buttons, external links, or other calls to action that direct customers to purchasing mechanisms other than in-app purchase"
  - surface: code
  - verify: In NFT collection browsing screens, grep for buy/marketplace links (OpenSea etc.), `openURL`, `Link`, `SFSafariViewController`; check whether they are gated by storefront (`Storefront.current?.countryCode == "USA"` / `SKPaymentQueue.default().storefront`).
  - fix: Remove external purchase CTAs, or show them only on the United States storefront by checking the StoreKit storefront.

## 3.1.1(a) Link to Other Purchase Methods

**Source text (verbatim):**
> - 3.1.1(a) Link to Other Purchase Methods: Developers may apply for entitlements to provide a link in their app to a permitted destination in order to purchase digital content or services. These entitlements are not required for developers to include buttons, external links, or other calls to action in their United States storefront apps. Please see additional details below.
> - StoreKit External Purchase Link Entitlements: apps on the App Store in specific regions may offer in-app purchases and also use a StoreKit External Purchase Link Entitlement or, where permitted, a Music Streaming Services Entitlement to include a link to a permitted destination that informs users of other ways to purchase digital goods or services. Approved destinations may vary by region. Learn more about these entitlements. In accordance with the entitlement agreements, the link may inform users about where and how to purchase those in-app purchase items, and the fact that such items may be available for a comparatively lower price. The entitlements are limited to use only in specific storefronts of the App Store, and only on certain platforms in each of those storefronts. In all other storefronts, except for the United States storefront, where this prohibition does not apply, apps and their metadata may not include buttons, external links, or other calls to action that direct customers to purchasing mechanisms other than in-app purchase.
> - If your app engages in misleading marketing practices, scams, or fraud in relation to the entitlement, your app will be removed from the App Store and you may be removed from the Apple Developer Program.

**Applies to:** Apps that link to purchase methods other than in-app purchase for digital content or services

**Related:** StoreKit External Purchase Link Entitlement; Music Streaming Services Entitlement

- **[3.1.1(a)-01]** If the app links to an external purchase destination for digital content/services outside the United States storefront, does it hold an approved entitlement (StoreKit External Purchase Link Entitlement or Music Streaming Services Entitlement)?
  - quote: "Developers may apply for entitlements to provide a link in their app to a permitted destination in order to purchase digital content or services."
  - surface: code
  - verify: Grep for external purchase links (`openURL`, `Link(`, `SFSafariViewController`, `ExternalPurchaseLink`, `ExternalPurchase.presentNoticeSheet`). Inspect `.entitlements` for `com.apple.developer.storekit.external-purchase-link` or `com.apple.developer.storekit.external-purchase-link-streaming` and Info.plist for `SKExternalPurchaseLink` / `SKExternalPurchase`; confirm the entitlement is enabled on the App ID in the developer portal (Certificates, Identifiers & Profiles).
  - fix: Apply for the appropriate entitlement (manual) or restrict the link to the United States storefront, or remove it.
- **[3.1.1(a)-02]** Is the external link used only in the specific storefronts and on the platforms the entitlement covers, pointing to a permitted/approved destination?
  - quote: "The entitlements are limited to use only in specific storefronts of the App Store, and only on certain platforms in each of those storefronts."
  - surface: code
  - verify: Check Info.plist `SKExternalPurchaseLink` dictionary (storefront country codes → URLs) and code that gates the link by storefront (`Storefront.current`, `ExternalPurchaseLink.canOpen`/`ExternalPurchase.canPresent`); confirm the platform target matches the entitlement's allowed platforms and URLs match approved destinations.
  - fix: Gate the link by StoreKit storefront and platform; limit destinations to approved URLs listed in Info.plist.
- **[3.1.1(a)-03]** In all other storefronts (except the United States), are the app and its metadata free of buttons, external links, or other calls to action directing customers to non-IAP purchasing mechanisms?
  - quote: "In all other storefronts, except for the United States storefront, where this prohibition does not apply, apps and their metadata may not include buttons, external links, or other calls to action that direct customers to purchasing mechanisms other than in-app purchase."
  - surface: asc
  - verify: App Store Connect > version page: Description, Promotional Text, What's New, screenshots, and Keywords for "buy on our website", pricing on web, etc. In code, grep paywall/settings for web-purchase CTAs and confirm they are storefront-gated.
  - fix: Remove external purchase CTAs from metadata for non-entitled storefronts and gate in-app CTAs by storefront.
- **[3.1.1(a)-04]** Does the app avoid misleading marketing practices, scams, or fraud in relation to the entitlement?
  - quote: "If your app engages in misleading marketing practices, scams, or fraud in relation to the entitlement, your app will be removed from the App Store"
  - surface: manual
  - verify: Review the text shown alongside the external link and on the destination for false or misleading claims; developer attests to compliance with the entitlement agreement.
  - fix: manual — requires developer decision/legal/business action.

## 3.1.2 Subscriptions

**Source text (verbatim):**
> 3.1.2 Subscriptions: Apps may offer auto-renewable in-app purchase subscriptions, regardless of category on the App Store. When incorporating auto-renewable subscriptions into your app, be sure to follow the guidelines below.

**Applies to:** Apps offering auto-renewable in-app purchase subscriptions
**Requires:** iap, subscriptions

- **[3.1.2-01]** If the app incorporates auto-renewable subscriptions, does it follow the guidelines in 3.1.2(a)–(c)?
  - quote: "When incorporating auto-renewable subscriptions into your app, be sure to follow the guidelines below."
  - surface: asc
  - verify: App Store Connect > Monetization > Subscriptions: list subscription groups and products; cross-check product IDs used in code (`Product.products(for:)`, `.storekit` file). Then run checks 3.1.2(a)-*, 3.1.2(b)-*, 3.1.2(c)-*.
  - fix: Configure subscriptions in App Store Connect and resolve any failing 3.1.2(a)–(c) checks.

## 3.1.2(a) Permissible uses

**Source text (verbatim):**
> - 3.1.2(a) Permissible uses: If you offer an auto-renewable subscription, you must provide ongoing value to the customer, and the subscription period must last at least seven days and be available across all of the user’s devices. While the following list is not exhaustive, examples of appropriate subscriptions include: new game levels; episodic content; multiplayer support; apps that offer consistent, substantive updates; access to large collections of, or continually updated, media content; software as a service (“SAAS”); and cloud support. In addition:
> - Subscriptions may be offered alongside à la carte offerings (for example, you may offer a subscription to an entire library of films as well the purchase or rental of a single movie).
> - Games offered in a streaming game service subscription may offer a single subscription that is shared across third-party apps and services; however, they must be downloaded directly from the App Store, must be designed to avoid duplicate payment by a subscriber, and should not disadvantage non-subscriber customers.
> - Subscriptions must work on all of the user’s devices where the app is available. Learn more about sharing a subscription across your apps.
> - As with all apps, those offering subscriptions should allow a user to get what they’ve paid for without performing additional tasks, such as posting on social media, uploading contacts, checking in to the app a certain number of times, etc.
> - Subscriptions may include consumable credits, gems, in-game currencies, etc., and you may offer subscriptions that include access to discounted consumable goods (such as a platinum membership that exposes gem-packs for a reduced price).
> - If you are changing your existing app to a subscription-based business model, you should not take away the primary functionality existing users have already paid for. For example, let customers who have already purchased a “full game unlock” continue to access the full game after you introduce a subscription model for new customers.
> - Auto-renewable subscription apps may offer a free trial period to customers by providing the relevant information set forth in App Store Connect. Learn more about providing subscription offers.
> - Apps that attempt to scam users will be removed from the App Store. This includes apps that attempt to trick users into purchasing a subscription under false pretenses or engage in bait-and-switch and scam practices; these will be removed from the App Store and you may be removed from the Apple Developer Program.
> - Cellular carrier apps may include auto-renewable music and video subscriptions when purchased in bundles with new cellular data plans, with prior approval by Apple. Other auto-renewable subscriptions may also be included in bundles when purchased with new cellular data plans, with prior approval by Apple, if the cellular carrier apps support in-app purchase for users. Such subscriptions cannot include access to or discounts on consumable items, and the subscriptions must terminate coincident with the cellular data plan.

**Applies to:** Apps offering auto-renewable subscriptions

**Related:** sharing a subscription across your apps; providing subscription offers

- **[3.1.2(a)-01]** Does the auto-renewable subscription provide ongoing value to the customer?
  - quote: "If you offer an auto-renewable subscription, you must provide ongoing value to the customer"
  - surface: manual
  - verify: Review what subscribers receive over time (new content, cloud services, updates, SaaS features) versus a one-time unlock; check App Review notes/description explain the ongoing value.
  - fix: manual — requires developer decision/legal/business action (add ongoing value or switch to a non-consumable).
- **[3.1.2(a)-02]** Does every auto-renewable subscription period last at least seven days?
  - quote: "the subscription period must last at least seven days"
  - surface: asc
  - verify: App Store Connect > Monetization > Subscriptions > each subscription > Subscription Duration; confirm none is shorter than 1 week. Also check the `.storekit` config `recurringSubscriptionPeriod`.
  - fix: Set Subscription Duration to 1 week or longer.
- **[3.1.2(a)-03]** Is the subscription available and working across all of the user’s devices where the app is available?
  - quote: "Subscriptions must work on all of the user’s devices where the app is available."
  - surface: code
  - verify: Confirm entitlement checks derive from StoreKit (`Transaction.currentEntitlements` / receipt) or an account-based server, not device-local only flags (e.g., `UserDefaults` set once on purchase without sync). Check every platform target (iPhone, iPad, Mac, Watch, Vision, TV) shares the same entitlement logic; test restore on a second device.
  - fix: Read entitlements from StoreKit transactions (synced via Apple ID) or a server account on every device/platform the app runs on.
- **[3.1.2(a)-04]** If games are offered in a streaming game service subscription, are they downloaded directly from the App Store, and designed to avoid duplicate payment by a subscriber ("must"), and do they avoid disadvantaging non-subscriber customers ("should")?
  - quote: "they must be downloaded directly from the App Store, must be designed to avoid duplicate payment by a subscriber, and should not disadvantage non-subscriber customers"
  - surface: manual
  - verify: Applies only to streaming game services. Developer confirms each game is an App Store download, subscribers are not charged twice, and non-subscribers are not disadvantaged.
  - fix: manual — requires developer decision/legal/business action.
- **[3.1.2(a)-05]** Can users get what they’ve paid for without performing additional tasks (posting on social media, uploading contacts, checking in a certain number of times, etc.)? (Apple states this as "should".)
  - quote: "those offering subscriptions should allow a user to get what they’ve paid for without performing additional tasks, such as posting on social media, uploading contacts, checking in to the app a certain number of times, etc."
  - surface: code
  - verify: Inspect entitlement-granting code paths for extra conditions after purchase (share-sheet completion, `CNContactStore` access, streak/check-in counters) gating paid content.
  - fix: Grant purchased access immediately upon a verified transaction without additional tasks.
- **[3.1.2(a)-06]** If an existing app moved to a subscription model, do existing users who already paid keep the primary functionality they paid for? (Apple states this as "should not take away".)
  - quote: "If you are changing your existing app to a subscription-based business model, you should not take away the primary functionality existing users have already paid for."
  - surface: code
  - verify: If the app was previously paid-upfront or had a full-unlock IAP, check for grandfathering logic (`AppTransaction.shared` `originalAppVersion`/`originalPurchaseDate`, legacy non-consumable product IDs in entitlement checks).
  - fix: Grant legacy purchasers continued access by checking `AppTransaction.originalAppVersion` or legacy non-consumable transactions.
- **[3.1.2(a)-07]** If a free trial is offered on an auto-renewable subscription, is it configured via the relevant information in App Store Connect?
  - quote: "Auto-renewable subscription apps may offer a free trial period to customers by providing the relevant information set forth in App Store Connect."
  - surface: asc
  - verify: App Store Connect > Monetization > Subscriptions > subscription > Subscription Prices > Introductory Offers; confirm the free trial is set up there (not a custom server-side trial that later charges outside StoreKit).
  - fix: Configure the free trial as an Introductory Offer in App Store Connect.
- **[3.1.2(a)-08]** Is the app free of attempts to trick users into purchasing a subscription under false pretenses or bait-and-switch/scam practices?
  - quote: "This includes apps that attempt to trick users into purchasing a subscription under false pretenses or engage in bait-and-switch and scam practices"
  - surface: runtime
  - verify: Walk through the paywall: check that the advertised features/prices match what is delivered, no misleading "free" claims hiding auto-renewal, and button labels match the action.
  - fix: Make paywall copy and pricing accurate and matching the actual product delivered.
- **[3.1.2(a)-09]** If a cellular carrier app bundles auto-renewable subscriptions with new cellular data plans, does it have prior approval by Apple, exclude access to/discounts on consumables, and terminate coincident with the data plan?
  - quote: "Such subscriptions cannot include access to or discounts on consumable items, and the subscriptions must terminate coincident with the cellular data plan."
  - surface: manual
  - verify: Applies only to cellular carrier apps. Developer attests to Apple's prior approval and bundle terms.
  - fix: manual — requires developer decision/legal/business action.

## 3.1.2(b) Upgrades and Downgrades

**Source text (verbatim):**
> - 3.1.2(b) Upgrades and Downgrades: Users should have a seamless upgrade/downgrade experience and should not be able to inadvertently subscribe to multiple variations of the same thing. Review best practices on managing your subscription upgrade and downgrade options.

**Applies to:** Apps offering multiple auto-renewable subscription levels or variations
**Requires:** iap, subscriptions

**Related:** best practices on managing your subscription upgrade and downgrade options

- **[3.1.2(b)-01]** Is the app set up so users cannot inadvertently subscribe to multiple variations of the same thing? (Apple states this as "should not".)
  - quote: "should not be able to inadvertently subscribe to multiple variations of the same thing"
  - surface: asc
  - verify: App Store Connect > Monetization > Subscriptions: check whether tiers/durations of the same service (e.g., monthly/yearly, Basic/Pro) are split across separate subscription groups (which would let a user hold several at once); also check `.storekit` file `subscriptionGroups`.
  - fix: Move variations of the same service into one subscription group and rank levels.
- **[3.1.2(b)-02]** Do users have a seamless upgrade/downgrade experience? (Apple states this as "should".)
  - quote: "Users should have a seamless upgrade/downgrade experience"
  - surface: runtime
  - verify: With a sandbox subscriber, open the paywall/manage screen and switch tiers; confirm the app recognizes the current plan, offers switching, and links to subscription management (`showManageSubscriptions(in:)` / `manageSubscriptionsSheet`).
  - fix: Show current plan, allow switching within the group, and add a Manage Subscription entry using `manageSubscriptionsSheet`.

## 3.1.2(c) Subscription Information

**Source text (verbatim):**
> - 3.1.2(c) Subscription Information: Before asking a customer to subscribe, you should clearly describe what the user will get for the price. How many issues per month? How much cloud storage? What kind of access to your service? Ensure you clearly communicate the requirements described in Schedule 2 of the Apple Developer Program License Agreement.

**Applies to:** Apps offering auto-renewable subscriptions
**Requires:** iap, subscriptions

**Related:** Schedule 2 of the Apple Developer Program License Agreement

- **[3.1.2(c)-01]** Before asking the customer to subscribe, does the app clearly describe what the user will get for the price (e.g., issues per month, cloud storage, kind of access)? (Apple states this as "should".)
  - quote: "Before asking a customer to subscribe, you should clearly describe what the user will get for the price."
  - surface: runtime
  - verify: Open every paywall; confirm it lists concrete deliverables and shows the price (from `Product.displayPrice`) and period for each plan before the subscribe button.
  - fix: Add a clear feature list and price/period per plan on the paywall.
- **[3.1.2(c)-02]** Does the app clearly communicate the requirements described in Schedule 2 of the Apple Developer Program License Agreement?
  - quote: "Ensure you clearly communicate the requirements described in Schedule 2 of the Apple Developer Program License Agreement."
  - surface: manual
  - verify: Developer compares paywall and metadata disclosures against Schedule 2 of the Apple Developer Program License Agreement (document not reproduced in this guideline).
  - fix: manual — requires developer decision/legal/business action (review Schedule 2 and add required disclosures).

## 3.1.3 Other Purchase Methods

**Source text (verbatim):**
> 3.1.3 Other Purchase Methods: The following apps may use purchase methods other than in-app purchase. Apps in this section cannot, within the app, encourage users to use a purchasing method other than in-app purchase, except for apps on the United States storefront and as set forth in 3.1.1(a) and 3.1.3(a). Developers can send communications outside of the app to their user base about purchasing methods other than in-app purchase.

**Applies to:** Apps using purchase methods other than in-app purchase under 3.1.3(a)–(g)

- **[3.1.3-01]** If the app uses a 3.1.3 exception, is it free of in-app encouragement to use non-IAP purchasing methods (except on the United States storefront and as set forth in 3.1.1(a) and 3.1.3(a))?
  - quote: "Apps in this section cannot, within the app, encourage users to use a purchasing method other than in-app purchase, except for apps on the United States storefront and as set forth in 3.1.1(a) and 3.1.3(a)."
  - surface: code
  - verify: Grep UI strings (`Localizable.strings`/`.xcstrings`, SwiftUI `Text`) for "subscribe on our website", "cheaper on web", "buy at", and links to web checkout; confirm they are gated to the US storefront or covered by an entitlement.
  - fix: Remove in-app encouragement of non-IAP purchasing, or gate it to the United States storefront / an approved entitlement.

## 3.1.3(a) “Reader” Apps

**Source text (verbatim):**
> - 3.1.3(a) “Reader” Apps: Apps may allow a user to access previously purchased content or content subscriptions (specifically: magazines, newspapers, books, audio, music, and video). Reader apps may offer account creation for free tiers, and account management functionality for existing customers. Reader app developers may apply for the External Link Account Entitlement to provide an informational link in their app to a web site the developer owns or maintains responsibility for in order to create or manage an account. This entitlement is not required for developers to include buttons, external links, or other calls to action in their United States storefront apps. Learn more about the External Link Account Entitlement.

**Applies to:** Reader apps (magazines, newspapers, books, audio, music, and video) that let users access previously purchased content or subscriptions

**Related:** External Link Account Entitlement

- **[3.1.3(a)-01]** If the app relies on the reader exception, is its content specifically magazines, newspapers, books, audio, music, or video?
  - quote: "Apps may allow a user to access previously purchased content or content subscriptions (specifically: magazines, newspapers, books, audio, music, and video)."
  - surface: manual
  - verify: Determine whether the app's primary content falls in the listed categories; if not, the reader exception does not apply.
  - fix: manual — requires developer decision/legal/business action (use IAP if not a reader app).
- **[3.1.3(a)-02]** Is in-app account creation limited to free tiers (with account management for existing customers)?
  - quote: "Reader apps may offer account creation for free tiers, and account management functionality for existing customers."
  - surface: runtime
  - verify: Run sign-up; confirm the in-app sign-up creates only free-tier accounts and does not sell paid plans outside IAP.
  - fix: Restrict in-app sign-up to free tiers.
- **[3.1.3(a)-03]** Outside the United States storefront, is any informational link to create or manage an account covered by the External Link Account Entitlement and pointing to a web site the developer owns or maintains responsibility for?
  - quote: "Reader app developers may apply for the External Link Account Entitlement to provide an informational link in their app to a web site the developer owns or maintains responsibility for in order to create or manage an account."
  - surface: code
  - verify: Inspect `.entitlements` for `com.apple.developer.storekit.external-link.account` and Info.plist `SKExternalLinkAccount`; check link URLs domains belong to the developer; confirm use of `ExternalLinkAccount` APIs or storefront gating.
  - fix: Apply for the External Link Account Entitlement (manual) or gate the link to the US storefront, or remove it.

## 3.1.3(b) Multiplatform Services

**Source text (verbatim):**
> - 3.1.3(b) Multiplatform Services: Apps that operate across multiple platforms may allow users to access content, subscriptions, or features they have acquired in your app on other platforms or your web site, including consumable items in multi-platform games, provided those items are also available as in-app purchases within the app.

**Applies to:** Apps that operate across multiple platforms and honor purchases made on other platforms or the web

- **[3.1.3(b)-01]** Are content, subscriptions, or features acquired on other platforms or the web (including consumables) also available as in-app purchases within the app?
  - quote: "provided those items are also available as in-app purchases within the app"
  - surface: asc
  - verify: List web/other-platform products (from server entitlement code, Stripe/Google Play product IDs in backend); compare against App Store Connect > Monetization > In-App Purchases / Subscriptions for equivalents.
  - fix: Create equivalent IAP products in App Store Connect and offer them in the app.

## 3.1.3(c) Enterprise Services

**Source text (verbatim):**
> - 3.1.3(c) Enterprise Services: If your app is only sold directly by you to organizations or groups for their employees or students (for example professional databases and classroom management tools), you may allow enterprise users to access previously-purchased content or subscriptions. Consumer, single user, or family sales must use in-app purchase.

**Applies to:** Apps sold directly to organizations or groups for their employees or students

- **[3.1.3(c)-01]** If relying on the enterprise exception, is the app only sold directly to organizations or groups for their employees or students?
  - quote: "If your app is only sold directly by you to organizations or groups for their employees or students"
  - surface: manual
  - verify: Developer confirms the sales channel is organizational only.
  - fix: manual — requires developer decision/legal/business action.
- **[3.1.3(c)-02]** Do consumer, single user, or family sales use in-app purchase?
  - quote: "Consumer, single user, or family sales must use in-app purchase."
  - surface: code
  - verify: Check for individual/family plan purchase flows outside StoreKit (web checkout links, external payment SDKs).
  - fix: Offer individual/family plans via IAP.

## 3.1.3(d) Person-to-Person Services

**Source text (verbatim):**
> - 3.1.3(d) Person-to-Person Services: If your app enables the purchase of real-time person-to-person services between two individuals (for example tutoring students, medical consultations, real estate tours, or fitness training), you may use purchase methods other than in-app purchase to collect those payments. One-to-few and one-to-many real-time services must use in-app purchase.

**Applies to:** Apps that sell real-time services between individuals

- **[3.1.3(d)-01]** If non-IAP payments are used under this exception, are they only for real-time person-to-person services between two individuals?
  - quote: "If your app enables the purchase of real-time person-to-person services between two individuals"
  - surface: manual
  - verify: Review what external payments buy (e.g., 1:1 live session) versus recorded content or group sessions.
  - fix: manual — requires developer decision/legal/business action.
- **[3.1.3(d)-02]** Do one-to-few and one-to-many real-time services use in-app purchase?
  - quote: "One-to-few and one-to-many real-time services must use in-app purchase."
  - surface: code
  - verify: Grep for group class/webinar/livestream purchase flows and confirm they use StoreKit.
  - fix: Sell group/one-to-many real-time services via IAP.

## 3.1.3(e) Goods and Services Outside of the App

**Source text (verbatim):**
> - 3.1.3(e) Goods and Services Outside of the App: If your app enables people to purchase physical goods or services that will be consumed outside of the app, you must use purchase methods other than in-app purchase to collect those payments, such as Apple Pay or traditional credit card entry.

**Applies to:** Apps that sell physical goods or services consumed outside of the app

- **[3.1.3(e)-01]** Are physical goods or services consumed outside the app paid with methods other than in-app purchase (e.g., Apple Pay or credit card entry)?
  - quote: "you must use purchase methods other than in-app purchase to collect those payments, such as Apple Pay or traditional credit card entry"
  - surface: code
  - verify: Identify physical goods/real-world service products; confirm they are not sold as StoreKit products (check `.storekit` and App Store Connect IAP list) and use `PKPaymentRequest`/Apple Pay or a card processor instead.
  - fix: Remove IAP products for physical goods/services and use Apple Pay or a payment processor.

## 3.1.3(f) Free Stand-alone Apps

**Source text (verbatim):**
> - 3.1.3(f) Free Stand-alone Apps: Free apps acting as a stand-alone companion to a paid web-based tool for VoIP, Cloud Storage, Email Services, or Web Hosting do not need to use in-app purchase, provided there is no purchasing inside the app, or calls to action for purchase outside of the app.

**Applies to:** Free companion apps to a paid web-based tool for VoIP, Cloud Storage, Email Services, or Web Hosting

- **[3.1.3(f)-01]** If relying on this exception, is the app free and are there no purchasing inside the app and no calls to action for purchase outside the app?
  - quote: "provided there is no purchasing inside the app, or calls to action for purchase outside of the app"
  - surface: code
  - verify: Confirm App Store Connect > Pricing and Availability price is Free; grep for purchase screens, "upgrade", "buy", pricing links in UI strings.
  - fix: Remove in-app purchasing and purchase calls to action, or implement IAP.

## 3.1.3(g) Advertising Management Apps

**Source text (verbatim):**
> - 3.1.3(g) Advertising Management Apps: Apps for the sole purpose of allowing advertisers (persons or companies that advertise a product, service, or event) to purchase and manage advertising campaigns across media types (television, outdoor, websites, apps, etc.) do not need to use in-app purchase. These apps are intended for campaign management purposes and do not display the advertisements themselves. Digital purchases for content that is experienced or consumed in an app, including buying advertisements to display in the same app (such as sales of “boosts” for posts in a social media app) must use in-app purchase.

**Applies to:** Apps for the sole purpose of advertising campaign management; apps selling in-app digital promotion (e.g., boosts)

- **[3.1.3(g)-01]** If relying on this exception, is the app solely for advertisers to purchase and manage campaigns, without displaying the advertisements itself?
  - quote: "These apps are intended for campaign management purposes and do not display the advertisements themselves."
  - surface: manual
  - verify: Review the app's purpose and whether it renders the purchased ads.
  - fix: manual — requires developer decision/legal/business action.
- **[3.1.3(g)-02]** Are digital purchases consumed in the app, including ads displayed in the same app (e.g., post “boosts”), sold via in-app purchase?
  - quote: "including buying advertisements to display in the same app (such as sales of “boosts” for posts in a social media app) must use in-app purchase"
  - surface: code
  - verify: Grep for `boost`, `promote post`, `sponsor`; confirm purchase uses StoreKit.
  - fix: Sell boosts/in-app promotions via IAP.

## 3.1.4 Hardware-Specific Content

**Source text (verbatim):**
> 3.1.4 Hardware-Specific Content: In limited circumstances, such as when features are dependent upon specific hardware to function, the app may unlock that functionality without using in-app purchase (such as an astronomy app that adds features when synced with a telescope). App features that work in combination with an approved physical product (such as a toy) on an optional basis may unlock functionality without using in-app purchase, provided that an in-app purchase option is available as well. You may not, however, require users to purchase unrelated products or engage in advertising or marketing activities to unlock app functionality.

**Applies to:** Apps that unlock functionality via specific hardware or approved physical products

- **[3.1.4-01]** If functionality is unlocked by hardware without IAP, is that functionality dependent on the specific hardware to function?
  - quote: "such as when features are dependent upon specific hardware to function, the app may unlock that functionality without using in-app purchase"
  - surface: code
  - verify: Inspect hardware-pairing unlocks (`CoreBluetooth`, `ExternalAccessory`, `AccessorySetupKit`, NFC `CoreNFC`) and confirm unlocked features actually require the hardware to operate.
  - fix: Use IAP for features that do not depend on the hardware.
- **[3.1.4-02]** For features working optionally with an approved physical product (such as a toy), is an in-app purchase option available as well?
  - quote: "provided that an in-app purchase option is available as well"
  - surface: asc
  - verify: Identify product-based unlocks in code; confirm an equivalent IAP exists in App Store Connect > Monetization and is offered in-app.
  - fix: Add an IAP alternative to the physical-product unlock.
- **[3.1.4-03]** Is the app free of requirements to purchase unrelated products or engage in advertising/marketing activities to unlock functionality?
  - quote: "You may not, however, require users to purchase unrelated products or engage in advertising or marketing activities to unlock app functionality."
  - surface: code
  - verify: Grep for unlock conditions tied to sharing, referrals, social posts, or purchase codes from unrelated products.
  - fix: Remove such unlock conditions.

## 3.1.5 Cryptocurrencies

**Source text (verbatim):**
> 3.1.5 Cryptocurrencies:

**Applies to:** Apps involving cryptocurrencies (see 3.1.5(i)–(v))
**Requires:** crypto

**Status:** Heading only — requirements are in 3.1.5(i)–(v). No checks.

## 3.1.5(i) Wallets

**Source text (verbatim):**
> - (i) Wallets: Apps may facilitate virtual currency storage, provided they are offered by developers enrolled as an organization.

**Applies to:** Apps that facilitate virtual currency storage
**Requires:** crypto

- **[3.1.5(i)-01]** If the app facilitates virtual currency storage, is it offered by a developer enrolled as an organization?
  - quote: "provided they are offered by developers enrolled as an organization"
  - surface: asc
  - verify: Detect wallet functionality (grep for wallet SDKs, `mnemonic`, `seed phrase`, `privateKey`, web3 libs). Check the Apple Developer account > Membership details: entity type is Organization (not Individual).
  - fix: manual — requires developer decision/legal/business action (enroll as an organization).

## 3.1.5(ii) Mining

**Source text (verbatim):**
> - (ii) Mining: Apps may not mine for cryptocurrencies unless the processing is performed off device (such as cloud-based mining).

**Applies to:** Apps involving cryptocurrency mining

- **[3.1.5(ii)-01]** Is the app free of on-device cryptocurrency mining?
  - quote: "Apps may not mine for cryptocurrencies unless the processing is performed off device"
  - surface: code
  - verify: Grep for mining libraries/terms (`miner`, `hashrate`, `stratum`, `xmrig`, `coinhive`, `cryptonight`), and Metal/compute kernels or WKWebView JS performing hashing.
  - fix: Remove on-device mining; any mining must be performed off device.

## 3.1.5(iii) Exchanges

**Source text (verbatim):**
> - (iii) Exchanges: Apps may facilitate transactions or transmissions of cryptocurrency on an approved exchange, provided they are offered only in countries or regions where the app has appropriate licensing and permissions to provide a cryptocurrency exchange.

**Applies to:** Apps facilitating cryptocurrency transactions or transmissions
**Requires:** crypto

- **[3.1.5(iii)-01]** Are cryptocurrency transactions/transmissions facilitated on an approved exchange?
  - quote: "Apps may facilitate transactions or transmissions of cryptocurrency on an approved exchange"
  - surface: manual
  - verify: Developer identifies the exchange used and its approval status.
  - fix: manual — requires developer decision/legal/business action.
- **[3.1.5(iii)-02]** Is the app offered only in countries or regions where it has appropriate licensing and permissions to provide a cryptocurrency exchange?
  - quote: "provided they are offered only in countries or regions where the app has appropriate licensing and permissions to provide a cryptocurrency exchange"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > Country or Region Availability; compare the list against the developer's licenses.
  - fix: Remove availability in unlicensed countries/regions; obtain licenses (manual).

## 3.1.5(iv) Initial Coin Offerings

**Source text (verbatim):**
> - (iv) Initial Coin Offerings: Apps facilitating Initial Coin Offerings (“ICOs”), cryptocurrency futures trading, and other crypto-securities or quasi-securities trading must come from established banks, securities firms, futures commission merchants (“FCM”), or other approved financial institutions and must comply with all applicable law.

**Applies to:** Apps facilitating ICOs, cryptocurrency futures trading, or other crypto-securities/quasi-securities trading

- **[3.1.5(iv)-01]** Does the app come from an established bank, securities firm, futures commission merchant (“FCM”), or other approved financial institution?
  - quote: "must come from established banks, securities firms, futures commission merchants (“FCM”), or other approved financial institutions"
  - surface: asc
  - verify: Check App Store Connect seller name / developer account legal entity matches a qualifying financial institution.
  - fix: manual — requires developer decision/legal/business action.
- **[3.1.5(iv)-02]** Does the app comply with all applicable law?
  - quote: "must comply with all applicable law"
  - surface: manual
  - verify: Developer/legal attests to compliance.
  - fix: manual — requires developer decision/legal/business action.

## 3.1.5(v) Cryptocurrency rewards for tasks

**Source text (verbatim):**
> - (v) Cryptocurrency apps may not offer currency for completing tasks, such as downloading other apps, encouraging other users to download, posting to social networks, etc.

**Applies to:** Cryptocurrency apps
**Requires:** crypto

- **[3.1.5(v)-01]** Is the app free of offering currency for completing tasks such as downloading other apps, encouraging others to download, or posting to social networks?
  - quote: "Cryptocurrency apps may not offer currency for completing tasks, such as downloading other apps, encouraging other users to download, posting to social networks, etc."
  - surface: code
  - verify: Grep for reward/airdrop/referral/bounty flows (`reward`, `airdrop`, `referral`, `earn`, `share to earn`) that credit crypto.
  - fix: Remove task-based crypto rewards.

## 3.2 Other Business Model Issues

**Source text (verbatim):**
> 3.2 Other Business Model Issues
> The lists below are not exhaustive, and your submission may trigger a change or update to our policies, but here are some additional dos and don’ts to keep in mind:

**Applies to:** All apps

**Status:** Informational heading — the dos and don’ts are in 3.2.1 and 3.2.2. No checks.

## 3.2.1 Acceptable

**Source text (verbatim):**
> 3.2.1 Acceptable

**Applies to:** All apps (see 3.2.1(i)–(viii))

**Status:** Heading only — requirements are in 3.2.1(i)–(viii). No checks.

## 3.2.1(i) Promoting your own apps

**Source text (verbatim):**
> - (i) Displaying your own apps for purchase or promotion within your app, provided the app is not merely a catalog of your apps.

**Applies to:** Apps that display the developer's own apps for purchase or promotion

- **[3.2.1(i)-01]** If the app promotes the developer's own apps, is it more than merely a catalog of those apps?
  - quote: "provided the app is not merely a catalog of your apps"
  - surface: runtime
  - verify: Grep for `SKStoreProductViewController`, `SKOverlay`, "More apps" screens; run the app and confirm it has primary functionality beyond the catalog.
  - fix: manual — requires developer decision/legal/business action (add core functionality or remove the catalog app).

## 3.2.1(ii) Third-party app collections for an approved need

**Source text (verbatim):**
> - (ii) Displaying or recommending a collection of third-party apps that are designed for a specific approved need (such as health management, aviation, accessibility). Your app should provide robust editorial content so that it doesn’t seem like a mere storefront.

**Applies to:** Apps displaying or recommending collections of third-party apps

- **[3.2.1(ii)-01]** Is any third-party app collection designed for a specific approved need (such as health management, aviation, accessibility)?
  - quote: "Displaying or recommending a collection of third-party apps that are designed for a specific approved need (such as health management, aviation, accessibility)."
  - surface: manual
  - verify: Review the collection's theme/purpose.
  - fix: manual — requires developer decision/legal/business action.
- **[3.2.1(ii)-02]** Does the app provide robust editorial content so it doesn’t seem like a mere storefront? (Apple states this as "should".)
  - quote: "Your app should provide robust editorial content so that it doesn’t seem like a mere storefront."
  - surface: runtime
  - verify: Run the app; check each recommended app is accompanied by substantive editorial text (reviews, explanations), not just icons and links.
  - fix: Add editorial content for each recommendation.

## 3.2.1(iii) Rental content expiry

**Source text (verbatim):**
> - (iii) Disabling access to specific approved rental content (such as films, television programs, music, books) after the rental period has expired; all other items and services may not expire.

**Applies to:** Apps that disable access to purchased items or services

- **[3.2.1(iii)-01]** Is access expiry limited to approved rental content (such as films, television programs, music, books), with all other items and services not expiring?
  - quote: "all other items and services may not expire"
  - surface: code
  - verify: Grep for `expir`, `rentalPeriod`, `validUntil` on purchased items; confirm only approved rental content expires.
  - fix: Remove expiry on non-rental purchased items/services.

## 3.2.1(iv) Wallet passes

**Source text (verbatim):**
> - (iv) Wallet passes can be used to make or receive payments, transmit offers, or offer identification (such as movie tickets, coupons, and VIP credentials). Other uses may result in the rejection of the app and the revocation of Wallet credentials.

**Applies to:** Apps that create or distribute Wallet passes

- **[3.2.1(iv)-01]** Are Wallet passes used only to make or receive payments, transmit offers, or offer identification (such as movie tickets, coupons, and VIP credentials)?
  - quote: "Wallet passes can be used to make or receive payments, transmit offers, or offer identification (such as movie tickets, coupons, and VIP credentials)."
  - surface: code
  - verify: Grep for `PassKit`, `PKAddPassesViewController`, `PKPass`, `.pkpass`, `pass.json`, and `com.apple.developer.pass-type-identifiers` entitlement; inspect pass contents/purpose.
  - fix: Restrict passes to payments, offers, or identification uses, or remove them.

## 3.2.1(v) Insurance apps

**Source text (verbatim):**
> - (v) Insurance apps must be free, in legal compliance in the regions distributed, and cannot use in-app purchase.

**Applies to:** Insurance apps

- **[3.2.1(v)-01]** Is the insurance app free?
  - quote: "Insurance apps must be free"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability: price is Free.
  - fix: Set the app price to Free.
- **[3.2.1(v)-02]** Is the insurance app free of in-app purchases?
  - quote: "cannot use in-app purchase"
  - surface: code
  - verify: Grep for `StoreKit` imports/usage, `.storekit` files; check App Store Connect > Monetization has no IAPs/subscriptions.
  - fix: Remove IAPs and StoreKit purchasing.
- **[3.2.1(v)-03]** Is the insurance app in legal compliance in the regions distributed?
  - quote: "in legal compliance in the regions distributed"
  - surface: manual
  - verify: Compare App Store Connect > Pricing and Availability regions with the developer's licensing.
  - fix: manual — requires developer decision/legal/business action.

## 3.2.1(vi) Approved nonprofit fundraising

**Source text (verbatim):**
> - (vi) Approved nonprofits may fundraise directly within their own apps or third-party apps, provided those fundraising campaigns adhere to all App Review Guidelines and offer Apple Pay support. These apps must disclose how the funds will be used, abide by all required local and federal laws, and ensure appropriate tax receipts are available to donors. Additional information shall be provided to App Review upon request. Nonprofit platforms that connect donors to other nonprofits must ensure that every nonprofit listed in the app has also gone through the nonprofit approval process. Learn more about becoming an approved nonprofit.

**Applies to:** Apps fundraising for approved nonprofits within the app

**Related:** becoming an approved nonprofit

- **[3.2.1(vi)-01]** Does in-app fundraising for approved nonprofits offer Apple Pay support?
  - quote: "provided those fundraising campaigns adhere to all App Review Guidelines and offer Apple Pay support"
  - surface: code
  - verify: Grep for `PKPaymentRequest`, `PKPaymentButton`/`PayWithApplePayButton`, and `com.apple.developer.in-app-payments` merchant ID entitlement in donation flows.
  - fix: Add Apple Pay as a donation payment method.
- **[3.2.1(vi)-02]** Does the app disclose how the funds will be used?
  - quote: "These apps must disclose how the funds will be used"
  - surface: runtime
  - verify: Run the donation flow; confirm a use-of-funds disclosure is shown.
  - fix: Add a use-of-funds disclosure to the donation screen.
- **[3.2.1(vi)-03]** Are appropriate tax receipts available to donors?
  - quote: "ensure appropriate tax receipts are available to donors"
  - surface: runtime
  - verify: Complete a test donation; confirm a tax receipt is provided or retrievable.
  - fix: Provide tax receipts (email or in-app download).
- **[3.2.1(vi)-04]** Does the fundraising abide by all required local and federal laws?
  - quote: "abide by all required local and federal laws"
  - surface: manual
  - verify: Developer/legal attests.
  - fix: manual — requires developer decision/legal/business action.
- **[3.2.1(vi)-05]** If the app is a platform connecting donors to other nonprofits, has every listed nonprofit gone through the nonprofit approval process?
  - quote: "Nonprofit platforms that connect donors to other nonprofits must ensure that every nonprofit listed in the app has also gone through the nonprofit approval process."
  - surface: manual
  - verify: Developer confirms approval status of each listed nonprofit.
  - fix: manual — requires developer decision/legal/business action (delist unapproved nonprofits).

## 3.2.1(vii) Monetary gifts between individuals

**Source text (verbatim):**
> - (vii) Apps may enable individual users to give a monetary gift to another individual without using in-app purchase, provided that (a) the gift is a completely optional choice by the giver, and (b) 100% of the funds go to the receiver of the gift. However, a gift that is connected to or associated at any point in time with receiving digital content or services must use in-app purchase.

**Applies to:** Apps enabling individual-to-individual monetary gifts

- **[3.2.1(vii)-01]** Is a non-IAP monetary gift a completely optional choice by the giver?
  - quote: "the gift is a completely optional choice by the giver"
  - surface: runtime
  - verify: Exercise the gift/tip flow; confirm no content or feature requires gifting.
  - fix: Make gifting optional.
- **[3.2.1(vii)-02]** Do 100% of the funds go to the receiver of the gift?
  - quote: "100% of the funds go to the receiver of the gift"
  - surface: manual
  - verify: Inspect fee logic in payment code/backend (platform fee, commission) and developer attests.
  - fix: Remove the developer's cut from non-IAP gifts, or use IAP.
- **[3.2.1(vii)-03]** Do gifts connected at any point with receiving digital content or services use in-app purchase?
  - quote: "a gift that is connected to or associated at any point in time with receiving digital content or services must use in-app purchase"
  - surface: code
  - verify: Check whether gifts trigger rewards to the giver or receiver (badges, shout-outs, unlocks, exclusive content); if so, confirm StoreKit is used.
  - fix: Use IAP for gifts associated with digital content/services.

## 3.2.1(viii) Financial trading, investing, money management

**Source text (verbatim):**
> - (viii) Apps used for financial trading, investing, or money management should be submitted by the financial institution performing such services and must have necessary licensing and permissions in the locations where you make them available.

**Applies to:** Apps used for financial trading, investing, or money management

- **[3.2.1(viii)-01]** Is the app submitted by the financial institution performing the services? (Apple states this as "should".)
  - quote: "should be submitted by the financial institution performing such services"
  - surface: asc
  - verify: Compare App Store Connect seller/developer legal entity with the institution performing the services.
  - fix: manual — requires developer decision/legal/business action.
- **[3.2.1(viii)-02]** Does the app have necessary licensing and permissions in every location where it is available?
  - quote: "must have necessary licensing and permissions in the locations where you make them available"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > Country or Region Availability vs. license list.
  - fix: Restrict availability to licensed locations (and/or obtain licenses — manual).

## 3.2.2 Unacceptable

**Source text (verbatim):**
> 3.2.2 Unacceptable

**Applies to:** All apps (see 3.2.2(i)–(x))

**Status:** Heading only — requirements are in 3.2.2(i)–(x). No checks.

## 3.2.2(i) App Store–like interfaces

**Source text (verbatim):**
> - (i) Creating an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection.

**Applies to:** All apps

- **[3.2.2(i)-01]** Is the app free of an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection?
  - quote: "Creating an interface for displaying third-party apps, extensions, or plug-ins similar to the App Store or as a general-interest collection."
  - surface: code
  - verify: Grep for lists of third-party app IDs, `SKStoreProductViewController`/`itms-apps://`/`apps.apple.com` links in bulk, plug-in marketplaces.
  - fix: Remove the store-like interface or narrow it to an approved need with editorial content (3.2.1(ii)).

## 3.2.2(ii) Intentionally omitted

**Source text (verbatim):**
> - (ii) Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 3.2.2(iii) Ad fraud and ad-predominant apps

**Source text (verbatim):**
> - (iii) Artificially increasing the number of impressions or click-throughs of ads, as well as apps that are designed predominantly for the display of ads.

**Applies to:** Apps displaying ads
**Requires:** ads

- **[3.2.2(iii)-01]** Is the app free of artificially increasing ad impressions or click-throughs?
  - quote: "Artificially increasing the number of impressions or click-throughs of ads"
  - surface: code
  - verify: Inspect ad SDK integrations (Google Mobile Ads, AppLovin, Unity Ads, etc.) for hidden/stacked/offscreen ad views, programmatic clicks, auto-refresh loops, ads placed under touch targets.
  - fix: Remove artificial impression/click logic; show ads only in visible, user-intended placements.
- **[3.2.2(iii)-02]** Is the app not designed predominantly for the display of ads?
  - quote: "apps that are designed predominantly for the display of ads"
  - surface: runtime
  - verify: Run core flows; assess ad frequency and screen share relative to content.
  - fix: Reduce ad density so app content is primary.

## 3.2.2(iv) Charity fundraising by non-approved apps

**Source text (verbatim):**
> - (iv) Unless you are an approved nonprofit or otherwise permitted under Section 3.2.1 (vi) above, collecting funds within the app for charities and fundraisers. Apps that seek to raise money for such causes must be free on the App Store and may only collect funds outside of the app, such as via Safari or SMS.

**Applies to:** Apps raising money for charities or fundraisers (not approved nonprofits)

- **[3.2.2(iv)-01]** Unless an approved nonprofit or otherwise permitted under 3.2.1(vi), is the app free of in-app fund collection for charities and fundraisers?
  - quote: "Unless you are an approved nonprofit or otherwise permitted under Section 3.2.1 (vi) above, collecting funds within the app for charities and fundraisers."
  - surface: code
  - verify: Grep for `donate`, `donation`, `charity`, `fundraiser` with in-app payment (Apple Pay, StoreKit, card SDKs).
  - fix: Move fund collection outside the app (Safari or SMS) or obtain approved nonprofit status (manual).
- **[3.2.2(iv)-02]** Is a charity-fundraising app free on the App Store and collecting funds only outside the app (e.g., via Safari or SMS)?
  - quote: "Apps that seek to raise money for such causes must be free on the App Store and may only collect funds outside of the app, such as via Safari or SMS."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability price = Free; in code, donation buttons open Safari (`openURL` to external browser) or SMS (`MFMessageComposeViewController`/`sms:`) rather than in-app payment.
  - fix: Set price to Free and route donations to Safari or SMS.

## 3.2.2(v) Arbitrary user restrictions

**Source text (verbatim):**
> - (v) Arbitrarily restricting who may use the app, such as by location or carrier.

**Applies to:** All apps

- **[3.2.2(v)-01]** Is the app free of arbitrary restrictions on who may use it, such as by location or carrier?
  - quote: "Arbitrarily restricting who may use the app, such as by location or carrier."
  - surface: code
  - verify: Grep for gating by `CTCarrier`/`CTTelephonyNetworkInfo`, `Locale.current.region`, IP geolocation, `CLLocationManager` region checks that block app use; ask the developer for the reason of any found.
  - fix: Remove arbitrary gates (use App Store Connect availability settings for legitimate regional distribution).

## 3.2.2(vi) Intentionally omitted

**Source text (verbatim):**
> - (vi) Intentionally omitted.

**Status:** Intentionally omitted by Apple — no checks.

## 3.2.2(vii) Manipulating visibility on other services

**Source text (verbatim):**
> - (vii) Artificially manipulating a user’s visibility, status, or rank on other services unless permitted by that service’s Terms and Conditions.

**Applies to:** Apps interacting with other services (social networks, platforms)

- **[3.2.2(vii)-01]** Is the app free of artificially manipulating a user’s visibility, status, or rank on other services (unless permitted by that service’s Terms and Conditions)?
  - quote: "Artificially manipulating a user’s visibility, status, or rank on other services unless permitted by that service’s Terms and Conditions."
  - surface: code
  - verify: Grep for follower/like/view boosting, auto-follow, bot automation against third-party APIs (Instagram, TikTok, X), purchasable "followers"/"likes".
  - fix: Remove manipulation features, or document the other service's Terms permitting them (manual).

## 3.2.2(viii) Binary options and CFD/derivatives trading

**Source text (verbatim):**
> - (viii) Apps that facilitate binary options trading are not permitted on the App Store. Consider a web app instead. Apps that facilitate trading in contracts for difference (“CFDs”) or other derivatives (such as FOREX) must be properly licensed in all jurisdictions where the service is available.

**Applies to:** Trading apps

- **[3.2.2(viii)-01]** Is the app free of facilitating binary options trading?
  - quote: "Apps that facilitate binary options trading are not permitted on the App Store."
  - surface: code
  - verify: Grep for `binary option`, `high/low`, `call/put` fixed-payout trading features.
  - fix: Remove binary options trading (consider a web app instead).
- **[3.2.2(viii)-02]** If the app facilitates CFDs or other derivatives (such as FOREX), is it properly licensed in all jurisdictions where the service is available?
  - quote: "must be properly licensed in all jurisdictions where the service is available"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability regions vs. the developer's licenses.
  - fix: Restrict availability to licensed jurisdictions (and/or obtain licenses — manual).

## 3.2.2(ix) Personal loans

**Source text (verbatim):**
> - (ix) Apps offering personal loans must clearly and conspicuously disclose all loan terms, including but not limited to equivalent maximum Annual Percentage Rate (APR) and payment due date. Loan apps may not charge a maximum APR higher than 36%, including costs and fees, and may not require repayment in full in 60 days or less.

**Applies to:** Apps offering personal loans

- **[3.2.2(ix)-01]** Does the app clearly and conspicuously disclose all loan terms, including the equivalent maximum APR and payment due date?
  - quote: "must clearly and conspicuously disclose all loan terms, including but not limited to equivalent maximum Annual Percentage Rate (APR) and payment due date"
  - surface: runtime
  - verify: Run the loan application flow; confirm max APR and due date (and all terms) are displayed prominently before acceptance. Also check the App Store Connect Description.
  - fix: Add a prominent loan-terms disclosure with max APR and due date.
- **[3.2.2(ix)-02]** Is the maximum APR, including costs and fees, 36% or lower?
  - quote: "Loan apps may not charge a maximum APR higher than 36%, including costs and fees"
  - surface: manual
  - verify: Developer confirms loan product terms; check any APR constants in code/config.
  - fix: manual — requires developer decision/legal/business action.
- **[3.2.2(ix)-03]** Does the loan avoid requiring repayment in full in 60 days or less?
  - quote: "may not require repayment in full in 60 days or less"
  - surface: manual
  - verify: Developer confirms minimum repayment term > 60 days; check term options in code/config.
  - fix: manual — requires developer decision/legal/business action.

## 3.2.2(x) Forcing store-related actions

**Source text (verbatim):**
> - (x) Apps must not force users to rate the app, review the app, download other apps, or other store-related actions in order to access functionality, content, or use of the app. Apps may otherwise incentivize users to take specific actions within apps (such as by completing a level or watching an ad).

**Applies to:** All apps

- **[3.2.2(x)-01]** Is the app free of forcing users to rate, review, download other apps, or perform other store-related actions to access functionality, content, or use of the app?
  - quote: "Apps must not force users to rate the app, review the app, download other apps, or other store-related actions in order to access functionality, content, or use of the app."
  - surface: code
  - verify: Grep around `requestReview`, `SKStoreReviewController`, `write-review` URLs (`action=write-review`), `SKStoreProductViewController`, and `itms-apps://` for code that blocks or gates content until the action is taken (unlock flags set after rating/download).
  - fix: Remove gates tied to rating/reviewing/downloading; make review prompts non-blocking.
