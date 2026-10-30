=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-information/
### App Store Connect Help

App Store Connect / Reference / In-App Purchases and subscriptions / Auto-renewable subscription information 
Filter ⌘K  
Filter ⌘K  

Reference  

# Auto-renewable subscription information

Property

Description

Subscription Group

A set of subscription products with varying levels and durations. Users can subscribe to one subscription product per group at a time.

Subscription Group Reference Name

An internal name you choose for a subscription group. This name will only appear on App Store Connect and in Sales and Trends reports, and won’t be visible to users.

Subscription Group Display Name

A user-facing name you choose for a subscription group. This is the name that appears on the App Store, and it can be localized. Subscription group display names must not contain control characters (for example, null, new lines, carriage returns, escape, and other invisible characters), or markup language (for example, HTML tags, or Unicode characters, such as emoticons, diacritics, or special characters).

App Name Display Options

A set of options that let you choose between using your app’s name or providing a custom name to display above the Subscription Group Display Name on the Manage Subscriptions page on user devices.

Auto-Renewable Subscription

A product that allows users to purchase dynamic content for a set period. This type of subscription renews automatically unless cancelled by the user. Subscription duration and price is configured in App Store Connect.

Auto-Renewable Subscription Levels

A ranking system of subscriptions within a subscription group that determines the upgrade, downgrade, and crossgrade path available to subscribers. Levels make it possible to offer varying access (basic, premium) of the same service. If you offer only one subscription product in your app, the subscription defaults to a single level within the subscription group.

If you have multiple subscription products, arrange them in order from the one that offers the most (level 1) to the one that offers the least. You can stack subscriptions with equal content but different durations and other similar variables at the same level. Each level can have multiple subscription products, allowing for multiple durations and prices for people to choose from. This lets them upgrade, downgrade, and crossgrade within the subscription group without impacting their days of paid service.

Upgrade

When someone switches to a subscription that you’ve ranked at a higher level. The customer’s prorated payment from lower level subscription is refunded to the original payment method. They’re charged for the higher level subscription, which goes into effect immediately. The date of upgrade is the renewal date for the higher level subscription.

Downgrade

When someone switches to a subscription that you’ve ranked at a lower level. They’re charged for the lower level subscription on their next renewal date.

Crossgrade

When someone switches between subscriptions that you’ve ranked at the same level. If the subscriptions are different durations, the crossgrade goes into effect on the customer’s next renewal date. If the subscriptions are the same duration, the customer’s prorated payment from the previous subscription is refunded to the original payment method. Then they’re charged for the new subscription, which goes into effect immediately. The date of cross grade is the renewal date for the new subscription.

Auto-Renewable Subscription Duration

The length of time before the subscription renews and the subscriber is charged. Possible durations are 1 week, 1 month, 2 months, 3 months, 6 months, and 1 year. The duration can’t be changed after you submit for review.

Auto-renewable subscriptions renew on the same day as the calendar date of the original purchase. If a one month free trial starts on January 7, the trial ends on February 7. If a one-month duration starts on a date that doesn’t occur in the next month, the trial ends on the last day of the next month, and reverts to the original date the next time that date occurs. For example, if someone subscribes on January 30, the next renewal date is February 28 (or February 29 in a leap year), and then March 30.

Auto-Renewable Subscription Display Name

A user-facing name you choose for a subscription. This is the name that appears on the App Store, and it can be localized. Subscription display names must not contain control characters (for example, null, new lines, carriage returns, escape, and other invisible characters), or markup language (for example, HTML tags, or Unicode characters, such as emoticons, diacritics, or special characters).

Multiseat Purchases

A purchase option that allows a customer to buy a subscription in quantities greater than 1. multiseat purchases are on by default for all auto-renewable subscriptions. Required for selling in Apple Business and Apple School Manager. Learn how to set purchase options for an auto-renewable subscription.

Available for Purchase From

Where an auto-renewable subscription is available for purchase. Options are the App Store, Apple Business, and Apple School Manager. Learn how to set purchase options for an auto-renewable subscription.

Related In-App Purchase types In-App Purchase information

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-consumable-or-non-consumable-in-app-purchases/
### App Store Connect Help

App Store Connect / Manage In-App Purchases / Create consumable or non-consumable In-App Purchases 
Filter ⌘K  
Filter ⌘K  

Manage In-App Purchases  

# Create consumable or non-consumable In-App Purchases

To offer In-App Purchases, add In-App Purchase information in App Store Connect. You can enter the metadata when you create your In-App Purchase or enter it later.

Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

Learn how to create In-App Purchases with the App Store Connect API.

Required role: You must have the Account Holder, Admin, App Manager, Developer, or Marketing role to add and edit In-App Purchases. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click In-App Purchases.

-  
Click the add button (+).

-  
Select Consumable or Non-Consumable. Learn about In-App Purchase types.

-  
Add the reference name and product ID, then click Create.

Related Overview for configuring In-App Purchases Offer auto-renewable subscriptions

=== SOURCE: https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/turn-on-family-sharing-for-in-app-purchases/
### App Store Connect Help

App Store Connect / Configure In-App Purchase settings / Turn on Family Sharing for In-App Purchases 
Filter ⌘K  
Filter ⌘K  

Configure In-App Purchase settings  

# Turn on Family Sharing for In-App Purchases

Family Sharing is a feature supported only by apps that offer auto-renewable subscriptions and non-consumable In-App Purchases. This feature enables users to share their purchases with up to five additional family members. To configure which of your In-App Purchases are eligible for Family Sharing, navigate to App Store Connect.

Whether or not a user’s purchases are automatically shared with their family members depends on the type of In-App Purchase, the user’s sharing preferences, and if the purchase was made before or after Family Sharing was turned on in App Store Connect. Users have the option of turning off Family Sharing in their subscription settings at any time.

Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

Learn how to enable Family Sharing for an in-app purchase using the App Store Connect API.

Auto-renewable subscriptions

Non-consumable In-App Purchases

New Users

Family Sharing is enabled by default depending on the preference set by the purchaser in Manage Subscriptions.

Family Sharing is enabled by default if the following conditions are met:

- The family organizer has purchase sharing enabled.

- The purchaser of a non-consumable In-App Purchase has Share Purchases/Share My Purchases enabled.

- The family member you want to share with has Share Purchases/Share My Purchases enabled.

- The app isn't hidden from the user's purchase history.

Existing Users

Users must opt-in to Family Sharing from within their manage subscriptions page.

You can unlock access to the In-App Purchase using receipt validation or App Store server notifications if the following conditions are met:

- The family organizer has purchase sharing enabled.

- The purchaser of a non-consumable In-App Purchase has Share Purchases/Share My Purchases enabled.

- The family member you want to share with has Share Purchases/Share My Purchases enabled.

- The app is not hidden from the user's purchase history.

Required role: Account Holder or App Manager. View role permissions.

## Turn on Family Sharing

This subscription will be able to be shared by up to six family members. Family Sharing is only available for subscriptions purchased from the App Store.

If multiseat purchases are turned on for a subscription, only the group purchaser is eligible for Family Sharing — additional seats are for individual use only.

Keep in mind that once you turn on Family Sharing for an In-App Purchases in App Store Connect, you can't turn it off.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click In-App Purchases, or Subscriptions then the subscription group.

-  
Select your In-App Purchase, or subscription, from the list.

-  
Scroll down to the Family Sharing section.

-  
Click Turn On.

-  
In the confirmation dialog, review the Family Sharing terms, then click Confirm.

## Family Sharing and multiseat purchases

Family Sharing and multiseat purchases interact in the following ways:

-  
If a subscription offers both Family Sharing and multiseat purchases, only group organizers can share the subscription with their family members. Other members of multiseat groups cannot share the subscription with their family members.

-  
You can turn multiseat purchases on at any time. If you turn on multiseat purchases for a subscription that already has Family Sharing turned on, a dialog asks you to confirm that you understand that the group purchaser will be able to share with family members.

Related Supporting Family Sharing in Your App Enabling App Store Server Notifications Setting Up the Transaction Observer for the Payment Queue Auto-Renewable Subscriptions Manage Sandbox Apple Account settings

=== SOURCE: https://developer.apple.comdoc://com.apple.storekit/documentation/StoreKit/supporting-family-sharing-in-your-app
# Supporting Family Sharing in your app

Provide service to share subscriptions and non-consumable products to family members.

### Overview

Family Sharing allows a customer to share access to auto-renewable subscriptions or non-consumables with up to five family members on all of their Apple devices. Enabling Family Sharing for a subscription can make your content or service more appealing to subscribers, and may encourage conversion to a paid subscription, increase customer engagement, and improve retention. Developers can choose to turn on Family Sharing for Apple In-App Purchases and non-consumables in App Store Connect. Users can also choose whether to share their purchases with family.

When users share a purchase through Family Sharing, each family member gets their own unique receipts and transactions. Process the transactions in the same way you already handle purchases — you don’t need any special logic for shared products. However, you do need to implement a new method in your transaction observer, and listen for a new notification type in server notifications. Specifically, to support Family Sharing, you need to:

- Enable Family Sharing for your Apple In-App Purchases in App Store Connect. For more information, see Turn on Family Sharing for Apple In-App Purchases.

- During runtime, check whether Apple In-App Purchases support Family Sharing using either  isFamilyShareable in Product or isFamilyShareable in SKProduct. Then inform users when merchandising your subscriptions.

- Process purchased and restored transactions in your app. This is standard processing you already do for any purchases.

- Implement paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:) in your transaction observer to handle conditions in which products are no longer shared.

- Listen for the REVOKE notification_type from App Store Server Notifications on your server.

[Related Sessions from WWDC20]

Related Sessions from WWDC20:  Session 10661: What’s new with Apple In-App Purchase

#### Enable Family Sharing for Apple In-App Purchases

To make Family Sharing available for an Apple In-App Purchase, developers need to turn on Family Sharing in App Store Connect. After you enable Family Sharing for an Apple In-App Purchase, you can’t turn it off. For more information, see Turn on Family Sharing for Apple In-App Purchases.

Users can choose whether to share their purchases with family. As users join or leave family groups and enable or disable sharing, your app needs to update the family’s access to your products. For information about how users manage their Family Sharing choices, see Set Up Family Sharing on iPhone.

#### Provide access to shared purchases

Your app receives a unique receipt for each family member entitled to a shared purchase, on each of their devices. For subscriptions, your app unlocks access through the normal purchase flow. For non-consumable products, unlocking access may require users to initiate a restored purchase, depending on the Family Sharing settings at the time of purchase.

To provide access for family members to a subscription or non-consumable, your app needs to handle purchased and restored transactions as usual. Specifically, follow these steps:

1. Set up a transaction observer at app launch so your app receives transactions that occur outside of your app, such as receiving a Family Sharing purchase. For more information on this best practice, see Setting up the transaction observer for the payment queue.

2. Verify the receipt. Look for a transaction in the latest receipt info array (responseBody.Latest_receipt_info) with the new Family Sharing purchase.

3. Handle purchased (SKPaymentTransactionState.purchased) transactions. This is a standard state apps need to handle, and you don’t need anything special for Family Sharing. For shared subscriptions, the transaction always has a purchased state. For shared non-consumable products, the transaction has a purchased state if Family Sharing was enabled for the product at the time of the purchase. For more information about handling transactions, see Processing a transaction.

4. Handle restored (SKPaymentTransactionState.restored) transactions, which is also a standard state apps need to handle. For shared non-consumable products, your app gets a restored transaction if developers enable Family Sharing after the user purchases the product. To gain access to the shared product, family members use your app’s restore functionality. For more information about restoring, see Restoring purchased products.

5. Unlock access to the shared subscription or non-consumable product.

6. Call finishTransaction(_:).

#### Revoke access if Family Sharing is disabled

With Family Sharing products, users have access to products only while Family Sharing is enabled. If the purchaser leaves the group, gets a refund, or stops sharing, the expectation is that the family’s access to the product stops immediately.

When a condition occurs that disables sharing, StoreKit informs your app by updating the receipt, and then calling the paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:) method of the SKPaymentTransactionObserver protocol. Implement this method on your transaction observer, and do the following:

1. Verify the receipt. Revoked products appear in the receipt with a cancellation_date field present.

2. Provide the app with access to all the products to which the user is entitled.

For more information, including a list of conditions that trigger this call, see paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:).

#### Listen for the revoke notification

If you set up your server to receive App Store Server Notifications, your server gets a REVOKE notification_type as soon as a shared purchase is no longer shared. This notification serves the same purpose as the paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:)call. Listen for and process this notification by:

1. Checking the latest receipt (unified_receipt.Latest_receipt_info) in the response body. Revoked products appear in the receipt with a cancellation_date field present.

2. Providing the app with access to all products to which the user is entitled.

3. Updating your records, if you keep server-based records to manage your customers’ subscriptions.

#### Indicate to users when products support Family Sharing

When your app displays Apple In-App Purchases, indicate in your UI whether users can share the product with family. Call isFamilyShareable to determine at runtime whether the Apple In-App Purchase supports Family Sharing. Knowing whether a product is shareable helps users make a selection that best fits their needs.

## Family Sharing

- isFamilyShareable: A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect.

- paymentQueue(_:didRevokeEntitlementsForProductIdentifiers:): Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases.

=== SOURCE: https://developer.apple.com/design/human-interface-guidelines/apple-in-app-purchase
Apple In-App Purchase | Apple Developer Documentation                         

# This page requires JavaScript.

Please turn on JavaScript in your browser and refresh the page to view its content.

## Automated tools and assistive tools:

A Markdown version of the page content is available: View Markdown

=== SOURCE: https://developer.apple.comdoc://com.apple.HIG/design/Human-Interface-Guidelines/apple-in-app-purchase
# Apple In-App Purchase

People can use Apple In-App Purchase to pay for digital goods and services, like premium content and subscriptions, securely within your app.



You can also promote and offer your Apple In-App Purchase items directly through the App Store.

[Tip]

Tip: Apple In-App Purchase and Apple Pay are different technologies that support different use cases. Use Apple In-App Purchase to sell virtual goods in your app, such as premium content for your app and subscriptions for digital content. Use Apple Pay in your app to sell physical goods like groceries, clothing, and appliances; for services such as club memberships, hotel reservations, and event tickets; and for donations.

Apple In-App Purchase supports four types of content:

- Consumable content like lives or gems in a game. After purchase, consumable content depletes as people use it, and people can purchase it again.

- Non-consumable content like premium features in an app. Purchased non-consumable content doesn’t expire.

- Auto-renewable subscriptions to virtual content, services, and premium features in your app on an ongoing basis. An auto-renewable subscription continues to automatically renew at the end of each subscription period until people choose to cancel it.

- Non-renewing subscriptions to a service or content that lasts for a limited time, like access to an in-game battle pass. People purchase a non-renewing subscription each time they want to extend their access to the service or content.



For marketing and business guidance, see Apple In-App Purchase and Auto-renewable subscriptions. For information about what you can and can’t sell in your app, including usage requirements and restrictions for Apple In-App Purchase, see App Review Guidelines. For developer guidance, see Apple In-App Purchase.

[Note]

Note: For apps with exceptionally large, frequently updated catalogs of one-time purchases or subscription content from multiple creators, or apps that provide subscriptions with optional add-on content as a single purchase within the app, the Advanced Commerce API allows you to manage your catalog of Apple In-App Purchase items directly. See the Advanced Commerce API App Store support page for an overview, and see Advanced Commerce API for developer guidance.

### Best practices

Let people experience your app before making a purchase. People may be more inclined to invest in paid items or features after they’ve enjoyed your app and discovered its value. If you offer Auto-renewable subscriptions, consider supporting limited free access to your content.

Design an integrated shopping experience. You don’t want people to think they’ve entered a different app when they browse and purchase your digital products. Present products and handle transactions in ways that mirror the style of your app.

Use simple, succinct product names and descriptions. Titles that don’t truncate or wrap and plain, direct language can help people find products quickly.

Display the total billing price for each in-app purchase you offer, regardless of type. People need to know the total billing amount for every purchase they consider.

Display your store only when people can make payments. If someone canʼt make payments — for example, because of parental restrictions — consider hiding your store or displaying UI that explains why the store isnʼt available. For developer guidance, see canMakePayments.

Use the default confirmation sheet. When someone makes a purchase using Apple In-App Purchase, the system displays a confirmation sheet to help prevent accidental purchases. Don’t modify or replicate this sheet.

#### Supporting Family Sharing

People can use Family Sharing to share access to their purchased content, such as auto-renewable subscriptions and non-consumable in-app purchases, with up to five additional family members, across all their Apple devices. To encourage people to take advantage of the Family Sharing support you offer, consider the following guidelines.

Prominently mention Family Sharing in places where people learn about the content you offer. For example, including “Family” or “Shareable” in a subscription or item name and referring to Family Sharing in your sign-up screen can highlight the feature and help people make an informed choice.

Help people understand the benefits of Family Sharing and how to participate. When you turn on Family Sharing, people can receive notifications about the change, depending on their current settings. For example, an existing subscriber whose sharing setting is turned off (the default) receives a notice from Apple that invites them to share their subscription with family members. Similarly, a family member can get a notification about content that’s being shared with them. To learn more about the types of notifications people can receive, see Auto-renewable subscriptions.

Aim to customize your in-app messaging so that it makes sense to both purchasers and family members. For example, when a family member views shared content for the first time, you might welcome them with wording like “Your family subscription includes…”.

#### Providing help

Sometimes, people need help with a purchase or want to request a refund. To help make this experience convenient, you can present custom UI within your app that provides assistance, offers alternative solutions, and helps people initiate the system-provided refund flow. For developer guidance, see beginRefundRequest(for:in:); for related guidance specific to auto-renewable subscriptions, see Helping people manage their subscriptions.

Provide help that customers can view before they request a refund. In addition to including a link to the system-provided refund flow, your custom purchase-help screen can provide assistance you tailor to your app. For example, your custom screen might help people resolve problems with missing purchases, answer frequently asked questions about the in-app purchases you offer, and give people ways to submit feedback or contact you directly for support.



Use a simple title for the refund action, like “Refund” or “Request a Refund”. The system-provided refund flow makes it clear that people request a refund from Apple, so there’s no need to reiterate this information.

Help people find the problematic purchase. For each recent purchase you display, include contextual information that helps people identify the one they want. For example, you might display an image of the product — along with its name and description — and list the original purchase date.



Consider offering alternative solutions. For example, if the customer didn’t receive the item they purchased, you might offer immediate fulfillment or a conciliatory item. Regardless of the alternatives you offer, make it clear that people can still request a refund.

Make it easy for people to request a refund. Although your purchase-help screen can offer useful information and alternative solutions, make sure this content doesn’t create a barrier to requesting a refund. For example, avoid making people scroll or open another screen to reveal your refund-request button. When people choose your refund-request item, they automatically enter the system-provided refund flow shown below.

Avoid characterizing or providing guidance on Apple’s refund policies. For example, don’t speculate about whether customers will receive the refund they request. To help people understand the refund-request process, you can provide a link to Request a refund for apps or content that you bought from Apple.

### Auto-renewable subscriptions

Call attention to subscription benefits during onboarding. By showing the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they’ll gain by subscribing. Include a strong call to action and a clear summary of subscription terms (see Making signup effortless). For related guidance, see Onboarding.



Offer a range of content choices, service levels, and durations. People appreciate the flexibility to choose the subscription that best meets their needs.

Consider letting people try your content for free before signing up. Limited free access gives people the opportunity to sample your content and encourages people who already engaged with your content to sign up. For example, you might offer a freemium app, a metered paywall, or a free trial.

Prompt people to subscribe at relevant times, like when they near their monthly limit of free content. Additionally, consider making it easy for people to subscribe at any time by including prompts at relevant points throughout your app.

Encourage a new subscription only when someone isn’t already a subscriber. Otherwise, people may believe their existing subscription has lapsed when that’s not actually the case. If you offer the same subscription options in multiple apps or through your website, provide a sign-in option so people don’t think they have to pay multiple times for the same service.

#### Making signup effortless

A simple and informative sign-up experience makes it easy for people to act on their interest in your content, whether they’re in your app or viewing your App Store product page.

Provide clear, distinguishable subscription options. Use short, self-explanatory names that differentiate subscription options from one another, and specify the price and duration for each option. If you offer an introductory price, be sure to list the introductory price, the duration of the offer, and the standard price the customer pays after the offer ends.

Simplify initial signup by asking only for necessary information. A lengthy sign-up process may lower your subscription conversion rate. Defer asking for additional information until after people have signed up.

In your tvOS app, help people sign up or authenticate using another device. Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need.

Give people more information in your app’s sign-up screen. In addition to including links to your Terms of Service and Privacy Policy in your app and App Store metadata, the in-app sign-up screen needs to include:

- The subscription name, duration, and the content or services provided during each subscription period

- The billing amount, correctly localized for the territories and currencies where the subscription is available for purchase

- A way for existing subscribers to sign in or restore purchases

For example, the Forest Explorer sign-up screen displays billing totals for monthly, biannual, and annual subscriptions in the most prominent positions. In subordinate positions, it shows breakdowns of the biannual and annual prices, so that people can compare the values and make an informed choice. The sign-up screen also contains a button that existing subscribers can use to restore their purchases.



Clearly describe how a free trial works. It’s particularly important to make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period. For example, the Ocean Journal sign-up screen explicitly states both the duration of the free trial and the amount that’s billed when it ends.



Include a sign-up opportunity in your app’s settings. App and account settings are common places for people to look for a way to subscribe.

#### Supporting offer codes

In iOS and iPadOS, subscription offer codes let you use both online and offline channels to give new, existing, and lapsed subscribers free or discounted access to your subscription content. For example, you might provide offer codes through email, give them out at a store or event, or print one on a physical product.

There are two types of offer codes you can support:

- A one-time use code is a unique code you generate in App Store Connect. People can redeem a one-time use code through a redemption URL (a shareable link), within your app (when you support redemption), or by entering it in the App Store, where they’re prompted to install your app if they haven’t already. Consider using one-time use codes when your distribution is small or when you need to restrict access to a code.

- A custom code is a code you create, such as NEWYEAR or SPRINGSALE. People can redeem a custom code through a redemption URL or within your app (when you support redemption). Consider using a custom code when you want to support a large campaign that requires a mass distribution of codes.

For developer guidance on implementing offer codes, see Offer codes and Set up offer codes. For guidance on other types of offers, see Providing subscription offers.

Clearly explain offer details. To help people make an informed decision, provide a straightforward and succinct description of your offer in your marketing materials.

Follow guidelines for creating a custom code. A custom code can contain only alphanumeric ASCII characters. Don’t use special characters, including Chinese and Arabic characters.

Tell people how to redeem a custom code. Because people can’t redeem a custom code by entering it in their App Store account settings, it’s important to let them know that they can redeem it through a redemption URL or within your app.

Consider supporting offer redemption within your app. The system automatically provides screens that present the offer-redemption flow, whether people redeem the offer in your app or in the App Store. When you use StoreKit API to let people redeem offer codes within your app, the only custom UI you need to create is one that initiates the system-provided flow. For developer guidance, see presentOfferCodeRedeemSheet(from:options:) and offerCodeRedemption(options:isPresented:onCompletion:). There are several natural places to provide this custom UI. For example, you could add a “Redeem Code” button to your paywall, onboarding screens, or your app’s settings screen.

After people tap your custom redeem button, the system automatically provides a series of code-redemption screens like the ones shown below.

Supply an engaging and informative promotional image. Creating this optional image can help people understand the value of your content. If you don’t supply a promotional image, the code redemption screens use your app icon by default. To learn more, see Promoting your in-app purchases.

Help people benefit from unlocked content as soon as they complete the redemption flow. Think about ways to align the post-redemption experience in your app with the subscriber’s new status. For example, you might provide a welcome experience for new subscribers or a brief tour of new features for an existing subscriber who’s unlocked additional functionality. In particular, be prepared to welcome people who subscribe before they open your app for the first time. For example, if you require people to create an account or sign in before they can use your app, make this process as smooth as possible for new subscribers who haven’t experienced it before.

#### Helping people manage their subscriptions

Supporting subscription management means people can upgrade, downgrade, or cancel a subscription without leaving your app. Offering subscription management within your app also gives you a natural place to provide help for common subscriber issues and present alternative offers for people to consider.



Provide summaries of the customer’s subscriptions. In particular, people appreciate viewing the upcoming renewal date without having to search for it. Consider displaying this information in a settings or account screen, near the subscription-management option. For developer guidance, see Product.SubscriptionInfo.

Consider using the system-provided subscription-management UI. Using StoreKit APIs lets you present a consistent experience that helps people manage or cancel their subscriptions without leaving your app. For developer guidance, see showManageSubscriptions(in:).

Encourage a subscriber to keep their subscription or resubscribe later. When someone attempts to cancel, consider reminding them what they’d lose access to, suggesting a different plan, or offering a discount to encourage them to stay subscribed. If someone still cancels, consider reaching out later with a personalized, discounted offer to resubscribe. For developer guidance, see Retention Messaging API and Win-back offers.

Always make it easy for customers to cancel an auto-renewable subscription. If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they’re being discouraged or prevented from canceling.

### Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, or visionOS.

#### watchOS

The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app. For the complete list of required items, see Making signup effortless. The following guidelines can help you design a sign-up screen that feels at home on Apple Watch.

Clearly describe the differences between versions of your app that run on different devices. If your watchOS app supports different functionality or provides a subset of the content that’s available on other devices, be sure to clarify these differences in your description. Be straightforward about the advantages of accessing subscription content through your watchOS app without implying that the experience is identical to the ones in other versions of your app.

Consider using a modal sheet to display the required information. After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single view. Even though people must scroll the view to access all the information, displaying it in a modal sheet helps your app UI remain streamlined and concise. Also, a modal sheet’s default Close button makes it easy for people to return to your free content with one tap. If you create a custom sign-up view instead of using a modal sheet, design a complete, efficient flow and include a Close or Cancel button that lets people return to your free content.

Make subscription options easy to compare on a small screen. People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that’s easy to scan and compare. Here are two ways you might present subscription options in your watchOS app:

- Display each option in a separate button. Using one button per payment option lets people start the signup process with one tap. In this design, it’s important to lock up each button with its description so that people can see how these elements are related, especially while scrolling.

- Display a list of options, followed by a button people tap to start the signup process. Using a list to display one option per row gives you a compact design that minimizes scrolling while making subscription choices easy to scan and understand. In this design, the button’s title can update to reflect the chosen option.

### Resources

##### Related

Apple In-App Purchase

Offering Subscriptions

App Review Guidelines

##### Developer documentation

Apple In-App Purchase — StoreKit

##### Videos

- What’s new in Apple In-App Purchase: Discover how monthly subscriptions with a 12-month commitment give people a more affordable option to pay for your subscription and secure a longer-term commitment. Explore how to configure and test this new payment option using App Store Connect, StoreKit APIs, Xcode testing, and more. Plus, learn about improvements to offer code redemption APIs, and enhancements to the App Review submission experience.

### Change log

| Date | Changes |

| September 17, 2026 | Rebranded as Apple In-App Purchase and refined guidance to reflect current best practices. |

| September 12, 2023 | Updated artwork and guidance for redeeming offer codes. |

| November 3, 2022 | Added a guideline for displaying the total billing price for every in-app purchase item and consolidated guidance into one page. |

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information/
### App Store Connect Help

App Store Connect / Reference / In-App Purchases and subscriptions / In-App Purchase information 
Filter ⌘K  
Filter ⌘K  

Reference  

# In-App Purchase information

## General Information

The main In-App Purchase properties identify the product in App Store Connect and in the app.

Property

Description

Apple ID

A unique identifier automatically generated for your In-App Purchase when you add the In-App Purchase to your account.

Reference Name

A unique name you give to your In-App Purchase for internal tracking that's not visible to customers, but used in App Store Connect and Sales and Trends reports. The reference name can include any characters and can be as long as 64 characters.

The reference name can be edited at any time without review.

Product ID

A unique ID specific to your app that you can assign to your In-App Purchases to uniquely identify them within your app.

The product ID can contain letters, numbers, hyphens, periods, and underscores, and can be as long as 100 characters. You need separate identifiers for In-App Purchases in your iOS apps and your macOS apps.

When your app uses StoreKit to communicate with the App Store, it uses product IDs to retrieve the configuration data you provided for each In-App Purchase. When a user wants to make a purchase, your app identifies the In-App Purchase using its product ID.

The product ID isn't editable after you save the In-App Purchase.

Once a product ID is assigned to an In-App Purchase, it can't be reused for another In-App Purchase within the same app, even if you delete the original In-App Purchase with that ID.

Review Notes

Additional information about the In-App Purchase that might help Apple review the submission, such as test user accounts and passwords. Review notes should not exceed 4000 characters.

Image

An image is required if you want to promote your In-App Purchase on your App Store product page or set up win-back offers. This image will represent your In-App Purchase in all countries or regions where your app is available. If you’re also using offer codes for auto-renewable subscriptions, your promotional image will appear on the App Store page when customers redeem their codes on iOS 14 or later. Your promotional image must meet the following requirements:

-  
JPG or PNG.

-  
Dimensions of 1024 x 1024 pixels.

-  
72 dpi, RGB, flattened and no rounded corners.

Show to all App Store users, even those who don’t have the app installed 

An indication that you'd like all customers to locate your promoted In-App Purchases, which is based on the user device information. By default, this is selected. If you deselect the checkbox, but haven’t implemented the SKProductStorePromotionController API, your In-App Purchase will not be visible on the App Store. Visit Promote In-App Purchases to relevant customers only. Note that a customer needs to have opened your app on their device at least once to locate your order and visibility settings inside your app.

App Review Screenshot

A screenshot of the In-App Purchase that clearly shows the item or service being offered. This screenshot is used for review only and isn't displayed on the App Store.

Upload a screenshot that meets any of the screenshot specifications your app supports. Once you’ve uploaded a screenshot, you can update it but not remove it.

## Localizable information

Add localizable In-App Purchases information used in the product display. You must include these properties for at least one language. For a list of languages, visit App Store localizations.

Changes to the localized information require review. The existing text displays on the store until the new text is approved. The change has its own status separate from the overall status of the In-App Purchase. Before your changes are reviewed, you can revert the change.

Property

Description

Display Name

The name of the In-App Purchase that is displayed to customers. The display name must be at least two characters and no more than 30 characters.

Description

A description of the In-App Purchase that potentially displays to users. If you make your In-App Purchase available for promotion, this displays under your In-App Purchase name on the App Store. The description must be no more than 45 characters.

=== SOURCE: https://developer.apple.com/in-app-purchase/
# Simple and safe Apple In-App Purchases

The App Store provides a powerful commerce system that makes it simple to offer your content and services across Apple platforms to people around the world. Facilitating billions of transactions annually, it handles end-to-end payment processing — so you can focus on creating great apps and games that people will love. Learn how to leverage world-class App Store commerce and payment features to grow your business as you offer Apple In-App Purchases (including subscriptions).

## Checkout and payment support

Developers have earned more than $300 billion through the App Store commerce system since its launch in 2008. And the App Store receives more than half a billion visitors every week, making it a great place to promote your Apple In-App Purchases.

### Effortless checkout

Apple In-App Purchase makes it simple for customers to purchase your digital goods and services on the App Store and in your apps. When creating an Apple Account, customers add a payment method that can be used to make purchases. And with secure authentication using Face ID, Optic ID, or Touch ID, customers can make purchases within your app in just a few taps — minimizing abandoned purchases.

When a purchase is initiated, an App Store payment sheet displays relevant details that help customers easily understand the transaction (like the type of good or service, price, and subscription duration) before confirming their purchase.

### Global payment reach

Apple handles worldwide end-to-end payment processing — from decrypting payments, to validating tokens, to receiving payments — so you don’t have to coordinate with multiple payment providers. Customers can pay with their preferred regional method with support for more than 200 payment methods, including credit and debit cards, carrier billing, digital wallets, and more.

To help you reach as many customers as possible in 175 regions, we continuously add support for new payment methods.

##### Customer

Transacts in the App Store or in your app using secure biometric authentication.

##### App Store

Using payment methods already collected from customers, aggregates purchases securely.

##### Payment Service Provider

Authenticates transactions and when relevant routes transactions over various card networks.

##### Bank Issuer

Receives payment request and will approve or decline based on customers balance or credit line.

### Powerful pricing tools

App Store tools make it convenient to manage Apple In-App Purchase pricing across international markets, so you can easily offer content and expand your business worldwide.

Regional availability options. Choose the storefronts where you want to make your Apple In-App Purchases (including subscriptions) available, so you can deliver content and services customized for each market.

Flexible pricing. Choose from 900 price points, ranging from United States $0.29 to $10,000, with similar prices in each currency. Options follow the most common pricing conventions in each country or region to make sure your pricing is relevant to customers. You can also offer a custom price point option in each storefront for an Apple In-App Purchase, and set up custom prices for a limited time period or indefinitely.

United States Dollar (USD) 
China (CNY) 
Japan (JPY) 
Korea (KRW)  

Price steps Lowest
supported price Highest
supported price    
$0.10 $0.29 $9.99  
$0.50 $0.49 $49.99  
$1.00 $0.99 $199.99  
$5.00 $4.99 $499.99  
$10.00 $9.99 $9,999.99    
Supported Conventions     
X.99 $0.99 $9,999.99  
X.00 $1.00 $10,000  
X.90 $0.90 $99.90  
X.95 $0.95 $49.95     

Price steps Lowest
supported price Highest
supported price    
CN¥0.50 1 10  
CN¥1 1 200  
CN¥5 3 498  
CN¥10 8 998  
CN¥50 48 3,998  
CN¥100 98 7,998  
CN¥500 498 29,999  
CN¥1000 998 74,999    
Supported Conventions     
X9 9 74,999  
X8 8 9,998  
X0 10 500  
X.80 1.80 99.80  
X9.90 9.90 99.90     

Price steps Lowest
supported price Highest
supported price    
¥10 50 2,000  
¥100 100 15,000  
¥500 400 49,800  
¥1,000 800 99,800  
¥5000 4,800 158,800  
¥10,000 9,800 800,000  
¥50,000 48,800 1,600,000    
Supported Conventions     
X0 50 160,000  
X,800 800 1,598,800  
X80 80 99,980  
X90 90 9,990     

Price steps Lowest
supported price Highest
supported price    
₩100 400 20,000  
₩500 500 100,000  
₩1,000 1,000 200,000  
₩5,000 5,000 500,000  
₩10,000 10,000 1,600,000  
₩100,000 90,000 7,590,000  
₩500,000 490,000 15,900,000    
Supported Conventions     
Double first digit 440 9,900,000  
X00 400 16,000,000  
X,900 / X9,000 / X90,000 / X900,000 900 15,900,000      
Easy-to-set-pricing worldwide. Specify a country or region you’re familiar with as the basis for automatically generated prices across the other 174 regions in 43 currencies. Automatically generated prices are globally equalized, accounting for taxes and foreign currency rates. Prices of apps and Apple In‑App Purchases (excluding auto-renewable subscriptions) are automatically updated as taxes or foreign currency change. Prices in your base region and any region with a custom price will never be adjusted by Apple.

### Taxes handled for you

Apple provides an automated system that handles the calculation, collection, and remittance of transactional taxes (such as value added tax) and compliance requirements in more than 80 regions, including most major markets, for your app and Apple In-App Purchases on the App Store. This makes it easy to sell your digital goods and services globally. The system applies the correct tax rates and regulations for each region based on the tax category assigned to your apps, such as videos, books, or news publications. We seamlessly adapt tax changes into our commerce system.

### Payment collection

Customers are encouraged to provide multiple payment methods and if a billing issue occurs with a given payment method, Apple attempts to collect using the other methods. Further, Apple automatically updates payment instruments whenever possible and when not possible, uses messaging and follow-ups to encourage customers to resolve.

If there’s a billing issue with an auto-renewable subscription, the App Store will recover the vast majority of the subscription for you. In addition, StoreKit displays a Billing Problem message sheet (either when your app launches or when you’ve configured your app to display it) that lets subscribers fix their billing issue without leaving your app. Apple also notifies them of the issue via push notifications and in-app messaging.

When you enable Billing Grace Period in App Store Connect, subscribers can continue to access your app’s paid content for a period of time, all while Apple attempts to resolve the billing issue. And if Apple recovers the subscription within the grace period, there’s no lost revenue and no interruption to the subscriber's days of paid service. Learn more about offering subscriptions.

## Simple set-up

You can offer one or more types of Apple In-App Purchases: consumable, non-consumable, auto-renewable subscription, and non-renewing subscription. Set up your Apple In-App Purchases using App Store Connect, the StoreKit framework, and Apple In-App Purchase APIs to retrieve product information, process payments, and deliver the product.

### Quick paywall creation

It’s easy to build intuitive payment experiences for Apple In-App Purchases and subscriptions using StoreKit views. With as little as one line of code, StoreKit views clearly present the description, price, and duration for each level of service. And with built-in localization support, Apple In-App Purchase details are displayed in the relevant language and currency, without any extra development work. You can also customize StoreKit views to match the look and feel of your app.

- Configure Apple In-App Purchases

- StoreKit essentials

- StoreKit documentation

- StoreKit views documentation

- Human Interface Guidelines: Apple In-App Purchase

- App Review Guidelines: Apple In-App Purchase

### Up-to-date transaction statuses

Near-real time status updates for refunds, subscription state, Family Sharing access, and more, are available through App Store Server Notifications. Use this information to update your transaction records and create customized user experiences. For example, if someone has turned off auto-renew, you might display a promotional offer to encourage them to resubscribe. To enable App Store Server Notifications, configure your server’s HTTPS URL in App Store Connect.

And you can get the latest product entitlements and transaction updates using the App Store Server API. Find out the latest status and history for Apple In-App Purchase transactions, including status changes that take place outside your app.

- App Store Server Notifications documentation

- App Store Server API documentation

### Tools to help you test

Take advantage of testing tools throughout the development process so your app and server can properly handle common purchase scenarios, like subscription offers, interrupted purchases, and refunds. During early development, you can simulate and test in‑app purchases using Xcode. After you configure your in‑app purchases in App Store Connect, use the sandbox environment or StoreKit Testing in Xcode to test using real product information.

When you’re ready for more people to help you test, TestFlight lets you gain valuable feedback from internal and external testers. Invite up to 10,000 external testers using just their email addresses or by sharing a public link. In‑app purchases in TestFlight use the sandbox environment, so they’re free to testers and don’t carry over into production once your app is released on the App Store.

Once you’re done testing, submit your Apple In-App Purchases for review.

- Testing at all stages of development

## Marketing and engagement features

Once your Apple In-App Purchases are published, you can promote them and encourage engagement in different ways. Learn more about promoting your apps.

### Promotion on the App Store

In iOS and iPadOS, people can browse Apple In-App Purchases directly on the App Store and start a purchase even before downloading your app. Promoted Apple In-App Purchases appear on your product page, can display in search results, and may be featured on the Today, Games, and Apps tabs, helping you showcase your content to a wide audience.

Learn more

### Offer codes

Offer codes let you present people with a limited-time offer for a free or discounted Apple In-App Purchase. Create offer codes to highlight the value of your Apple In-App Purchases as well as encourage engagement and purchases within your apps and game. You can share codes through your marketing channels, including email, in-app messaging, or printed campaigns.

Learn more

### In-App Events on the App Store

People can discover your events on the App Store in iOS and iPadOS, giving you another way to expand their reach. If your event requires an Apple In-App Purchase or subscription to participate, it’s noted on the event details page.

Learn more

### Subscription offers

Attract subscribers and keep them engaged with a discounted price or free access for a specific duration of an auto-renewable subscription. Transactions on the App Store are authenticated, so fraud opportunities — like multiple free trials from a single account — are minimized.

Learn more

### App bundles

You can create app bundles for paid apps or free apps that offer auto-renewable subscriptions. If an app offers a subscription, users can access it across all apps included in the bundle.

Learn more

### Family Sharing

Apps that offer auto-renewable subscriptions or non-consumable Apple In-App Purchases can offer Family Sharing to let people share access with up to five family members. Streamlined and convenient, Family Sharing can help you attract subscribers, encourage paid subscriptions, increase engagement, and improve retention.

Learn more

## Analytics and reporting

Get a wide range of helpful metrics related to each of your Apple In-App Purchases, including sales, number of paying users, average proceeds per paying user, and more. View your final proceeds for each month, earnings by location and currency, rates used to convert your earnings from local currencies (when available), as well as any applied taxes and adjustments. You can also download detailed reports of all transactions for each month, including the number of units sold per app or Apple In-App Purchase.

- Analytics and reporting overview

- View payments and proceeds in Payments and Financial Reports

- Download financial reports

### Data insights only available from Apple

Measure your app’s performance and grow your business on the App Store with unique data insights that only Apple provides. Each month, Apple collects billions of data points to give you valuable information, including:

- Unified sales data across iOS, iPadOS, macOS, tvOS, visionOS, and watchOS.

- Apple In-App Purchase proceeds by source, including App Store browse, App Store search, app referrers, and web referrers.

- Proceeds related to App Store features you use, including in-app events, custom product pages, pre-orders, and more.

- Peer group benchmark data to help you identify how successful your monetization efforts are compared to a relevant peer group.

- Subscription data, including the subscription state (trial, paid, and churned), subscription offer performance metrics, and subscription retention data.

- Subscriber churn data, such as cancellation events and renewals resulting from billing retry.

Learn about viewing analytics

Learn about measuring app performance

### Benchmark your performance

With peer group benchmarks in App Analytics, you can view how your app ranks across key metrics compared to similar apps on the App Store. One of these metrics is average proceeds per paying user, which can help you understand how well your Apple In-App Purchases are performing. Differential privacy techniques are applied to peer groups to preserve privacy, so no sensitive developer information is revealed and your data remains yours.

Learn about peer group benchmarks in App Analytics

Learn about taking action on peer group benchmarks

### Payments and financial reports

View your final proceeds for each month, with earnings broken out by territory and currency. View the rates used to convert your earnings from local currencies (when available) and any taxes and adjustments applied.

## Trust and safety

### Secure transactions and fraud detection

The App Store is a safe and trusted place for customers and developers, and we work to keep it that way. From 2020 through 2023, Apple prevented a combined total of over $7 billion in potentially fraudulent transactions. We continually invest significant resources in building more secure payment technologies, like Apple Pay and StoreKit. For example, with Apple Pay, credit card numbers are never shared with merchants — eliminating a risk factor in the payment transaction process. And purchases are verified through password and biometric security in order to prevent unauthorized use.

These protections are an essential part of keeping customers safe. But customers may not realize that when their credit card information is breached or stolen from another source, fraudsters may turn to online marketplaces like the App Store to attempt to purchase digital goods and services that can be laundered or used for illicit purposes. Apple focuses relentlessly on this kind of fraud as well, with a fusion of sophisticated technology and human review to prevent stolen cards from being used to make fraudulent purchases.

And Apple also takes action against fraudulent customer accounts, disabling those associated with abusive activity and blocking fraudulent new accounts before they can even be created.

### Customer support features

Thoughtful support helps you build trust with your users and can lead to higher retention, improved engagement, and better ratings and reviews. StoreKit and the App Store Server API help you provide more seamless support options and resolve in‑app purchase issues quickly and efficiently.

#### Refund requests

Let people request refunds directly within your app by using the beginRefundRequest API and providing a dedicated place in your app for these requests. You can also provide other options — such as technical support or in-app credits — before the option to request a refund.

If youʼve enabled App Store Server Notifications, youʼll receive a notification when someone receives a refund. You can use this information to take action — for example, updating the account balance based on the refund or restricting access to content unlocked by the Apple In‑App Purchase. If you choose to take action, inform the user of any changes and let them know if there’s anything they need to do. You can also identify if someone previously received refunds for any Apple In‑App Purchases made in your app using the Get Refund History endpoint.

Apple uses a variety of factors to determine whether a refund request is approved or denied. To help inform and improve the refund process, you can send information about a user’s Apple In‑App Purchase (including auto-renewable subscriptions) to Apple via the Send Consumption Information endpoint in the App Store Server API (for example, if they used the Apple In-App Purchase or you were unable to deliver the purchase). Data is incorporated into our refund logic, to help ensure flexible, accurate, and informed decision making.

- Refund request UI best practices

- Enabling App Store Server Notifications

- Handling refund notifications

- Providing subscriber support

#### Purchase management

If someone redownloads your app or switches to a new device, be sure to immediately provide access to the content or functionality from their past Apple In‑App Purchases. Use the currentEntitlements property in StoreKit to understand a user’s entitlements and provide access accordingly. Your app must also include a restore mechanism for any restorable Apple In‑App Purchases, per App Review Guideline 3.1.1.

If someone requests support for an Apple In‑App Purchase, you can use the Look Up Order ID endpoint to make sure you’re taking action on the right purchase. Simply ask the user for the Order ID included on their email receipt from Apple, then use the endpoint to confirm the invoice and any associated information — for example, whether the user has already received a refund for their purchase — or to match the date and time of the purchase with your records.

#### Tools for families

Apple provides tools to help developers and parents deliver safe experiences for children. With Ask to Buy, kids can send a request to the family organizer when they want to buy or download a new app or Apple In-App Purchase. And parents can use Screen Time to prevent unintentional or unauthorized purchases from the App Store, including Apple In-App Purchases across all apps.

#### Help from Apple

Apple provides world-class customer support to help efficiently resolve billing issues. Customers can use Report a Problem at any time to get support for Apple In-App Purchases made within your app or on the App Store. And because our support team is located worldwide, we can respond quickly. Customers receive email receipts from Apple for any purchases they’ve made, and they can view their purchase history in their Apple Account.

You can contact us at any time with questions about your Apple Developer Program membership, App Store Connect, implementing technologies and features, and more.

Learn about distributing on the App Store

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-introductory-offers-for-auto-renewable-subscriptions/
### App Store Connect Help

App Store Connect / Manage subscriptions / Set up introductory offers for auto-renewable subscriptions 
Filter ⌘K  
Filter ⌘K  

Manage subscriptions  

# Set up introductory offers for auto-renewable subscriptions

You can set up introductory offers for your apps on the App Store that contain auto-renewable subscriptions in App Store Connect. An introductory offer is a limited-time discounted price or free trial for the initial period of a subscription.

When you set up an introductory offer, it automatically appears on your app’s product page on the App Store for eligible users. You can also display introductory offers within your app. When displaying offers in your app, use receipt validation to ensure that you’re only showing offers to people who can redeem them. Learn about implementing introductory offers.

There are three types of introductory offers: free trial, pay up front, and pay as you go. You can choose the length of the introductory offer based on the standard subscription duration.

Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

Standard Subscription Duration

Pay As You Go

Pay Up Front

Free Trial

1 Week

1 to 12 Weeks

1, 2, 3, or 6 Months. 1 Year.

3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year.

1 Month

1 to 12 Months

1, 2, 3, or 6 Months. 1 Year.

3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year.

2 Months

2, 4, 6, 8, 10, or 12 Months

1, 2, 3, or 6 Months. 1 Year.

3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year.

3 Months

3, 6, 9, or 12 Months

1, 2, 3, or 6 Months. 1 Year.

3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year.

6 Months

6 or 12 Months

1, 2, 3, or 6 Months. 1 Year.

3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year.

1 Year

1 Year

1, 2, 3, or 6 Months. 1 Year.

3 Days. 1 or 2 Weeks. 1, 2, 3, or 6 Months. 1 Year.

Although you can create an introductory offer for each subscription product in App Store Connect, each person is only eligible to redeem one introductory offer per subscription group.

Learn how to set up introductory offers with the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Create an introductory offer

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions.

-  
Choose the subscription group containing your subscription.

-  
Select a subscription, then go to the Subscription Prices section and click View all Subscription pricing.

-  
Select Set up Introductory Offer.

-  
Select the countries or regions where you want to offer a discounted price, and click Next. You can have one current and one future introductory offer per storefront.

-  
Choose the start and end dates for your introductory offer. If you choose today as the start date, your introductory offer begins immediately. Offers end on the selected end date, with the exact time varying by region.

Click Next. If you create new offers that have overlapping dates, the latest action overwrites existing introductory offers. Learn about available offers and subscriber eligibility using the In-App Purchase API.

-  
Choose Pay as you go, Pay up front, or Free, then choose the appropriate duration, country or region, and price. To search from a larger list of price points, click See Additional Prices.

-  
App Store connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.

-  
Make sure the details of your introductory offer are correct and click Confirm. Once you create an introductory offer, you won’t be able to edit it. To change the details of your introductory offer, delete it and create a new one.

### Delete an introductory offer

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions.

-  
Choose the subscription group containing your subscription.

-  
Click the subscription you want to delete, then go to the Subscription Prices section and click View all Subscription Pricing.

-  
Navigate to the Introductory Offers tab to view, all your offers listed by date and country or region.

-  
Find the introductory offer you wish to delete, and move your pointer over the right side of the price change row until the remove button (—) appears. Click the remove button.

-  
Click Delete in the dialog.

###   FAQs

### What is the difference between introductory offer limits and customer eligibility limits?

App Store Connect allows you to set an introductory offer for each subscription product in App Store Connect. You can have multiple offers in each subscription group. New and returning customers are only eligible to use one introductory offer per subscription group. For example, if a customer uses a free trial and then upgrades to a subscription product in the same group that also has a free trial, they aren't eligible for the second offer.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-subscriptions/create-non-renewing-subscriptions/
### App Store Connect Help

App Store Connect / Manage subscriptions / Create non-renewing subscriptions 
Filter ⌘K  
Filter ⌘K  

Manage subscriptions  

# Create non-renewing subscriptions

A non-renewing subscription gives customers access to a service or content for a specific period of time (for example, access to a magazine for one month). To offer non-renewing subscriptions, enter product details in App Store Connect.

Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

Learn how to create a non-renewing subscription using the App Store Connect API.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Scroll down to Non-Renewing Subscriptions, and click Manage.

-  
Click the add button (+).

-  
Enter a Reference Name and Product ID, then click Create.

-  
Set a price and add localizations.

-  
Click Save.

Note: Your first non-renewing subscription must be submitted with a new app version. After creating your subscription, select Add for Review and include an app version in your submission to have it reviewed together with your app. Once your first non-renewing subscription has been approved, you can submit additional non-renewing subscriptions without a new app version. Learn more about submitting subscriptions for review.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions/
### App Store Connect Help

App Store Connect / Manage subscriptions / Offer auto-renewable subscriptions 
Filter ⌘K  
Filter ⌘K  

Manage subscriptions  

# Offer auto-renewable subscriptions

App Store Connect offers tools to help you run a subscription business on the App Store. How you configure your subscriptions in App Store Connect determine how users subscribe to your service, how often they are billed, and how they upgrade and downgrade between offerings. To begin offering a subscription in your app, you will need to create a Subscription Group, then add one or more Subscription products to that group, then assign levels to those products. Subscription setup is structured as the following:

-  
Subscription group: A set of subscription products with varying levels and durations. You can have up to 100 subscriptions per group. Users can subscribe to one subscription product per group at a time.

-  
Subscription: A product that lets users purchase dynamic content for a set period. Auto-renewable subscriptions renew automatically, unless cancelled by the user. Subscription duration and price is configured in App Store Connect.

-  
Subscription levels: A ranking system of subscriptions within a subscription group that determines the upgrade, downgrade, and crossgrade path available to subscribers. Levels make it possible to offer varying access (basic, premium) of the same service.

-  
Subscription duration: The length of time before the subscription renews and the subscriber is charged. Possible durations are 1 week, 1 month, 2 months, 3 months, 6 months, and 1 year.

## Single subscription product setup

If you offer only one subscription product in your app, the subscription defaults to a single level within the subscription group.

## Multiple subscription and durations product setup 

Arrange your subscriptions in order from the one that offers the most (level 1) to the one that offers the least. You can stack subscriptions with equal content but different durations and other similar variables, at the same level. Each level can have multiple subscription products, offering multiple durations and prices for people to choose from. This lets them upgrade, downgrade, and crossgrade within the subscription group without impacting their days of paid service.

## Subscription proceeds rate

During a subscriber’s first year of service, you receive 70% of the subscription price at each billing cycle, minus applicable taxes. After a subscriber accumulates one year of paid service in the same subscription group, your net revenue increases to 85% of the subscription price, minus applicable taxes. Time spent within a subscription offer is also counted toward the total. Members of the App Store Small Business Program receive 85% starting on the first day.

When an auto-renewable subscription expires, the days of paid service stop accumulating. If someone resubscribes or the subscription is recovered within 60 days, the days of paid service continue from the recovery date. Conversely, if the subscription is recovered after 60 days, the rate reverts to 70% and the day count starts over.

When a subscription expires due to a billing issue, Apple attempts to renew the subscription and collect payment. If you enabled the billing grace period for your apps, there won’t be any interruption to days of paid service or to your revenue, if Apple is able to recover the subscription within the billing grace period (either 6 or 16 days, depending on the subscription duration). Learn more about billing grace periods.

For subscription performance, subscriber activity, and proceeds in your Sales and Trends reports, visit view subscription data.

Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.

### Create a subscription group

To offer subscriptions within your app, you must first create a subscription group in App Store Connect. When you create subscription products, you'll be able to add these products to the subscriptions group. Before creating subscriptions, ensure that you understand the right subscription setup for your business model. Learn about offering subscriptions.

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the add button (+).

-  
Enter a reference name.

-  
Click Create

### Create an additional subscription group

A subscription group contains all the variations of a single subscription product — for example, monthly and annual plans for the same service, or basic and premium tiers. Customers can only hold one active subscription per group at a time. Create additional subscription groups only when your app offers separate subscription products that customers can purchase at the same time.

Note: Since users can only buy one subscription within a group at a time, creating a single group is the best practice for most apps, as it prevents people from accidentally purchasing multiple subscriptions. Users who buy subscriptions in multiple groups are billed separately for each subscription.

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the add button (+).

-  
Read and acknowledge the warning by selecting the checkbox and clicking Next.

Note: You’ll only be prompted with a warning when creating your second subscription group.

-  
Enter the reference name for the new group.

-  
Click Create.

### Delete subscriptions and groups

You can delete a subscription group only if it contains no subscriptions. Delete all subscriptions within the group first, then delete the group itself.

To delete a subscription:

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the subscription group containing the subscription you want to delete.

-  
Click the subscription you want to delete.

-  
Scroll to the bottom of the page, click Delete Subscription and confirm in the dialog that appears.

To delete a subscription group:

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the subscription group you want to delete.

-  
Scroll to the bottom of the page, click Delete Subscription Group and confirm in the dialog that appears.

### Add subscription products

-  
In the Sidebar, under Monetization, click Subscriptions.

-  
Click a subscription group name.

-  
Click Create.

Note: If you're adding a subscription to a group that already has existing subscriptions, you'll click the add button (+).

-  
Enter the subscription’s reference name and Product ID, then click Create. Once you've created your subscription product, you'll be taken to its information page to add more details.

-  
Click Create.

Note: In order to offer a monthly subscription with a 12 month commitment for subscriptions outside the United States and Singapore, select a duration of 1 year. Learn how to offer subscriptions with a 12 month commitment.

-  
Under Subscription Duration, choose a duration and click Save.

-  
Under Subscription Prices, set a price.

-  
Under Availability, select which countries or regions you want to make your subscription available in.

-  
Under Review Information, provide any additional information that may help the App Review team review your In-App Purchase.

-  
Optionally, enable Family Sharing, edit the subscription’s tax category, and add localizations.

-  
Click Save.

Note:

-  
If you'd like your subscription to be accessible from more than one app, create an equivalent subscription product for each app. Learn how to offer subscriptions across multiple apps.

-  
Your first auto-renewable subscription must be submitted with a new app version. Your first subscription group must also be submitted with a new app version and must include an auto-renewable subscription in the same submission. After creating your subscription group and subscription product, select Add for Review on the subscription detail page to submit it for review. Once your first auto-renewable subscription has been approved, you can submit additional auto-renewable subscriptions without a new app version. Learn more about submitting subscriptions for review.

### Assign subscription levels

Once you create a subscription product, you can add subscription group information and set subscription levels. These levels determine the upgrades, downgrades, and crossgrades available within a group.

You don’t have to assign multiple levels. You can choose to offer a single subscription product or offer multiple subscription products and assign them all to the same level within a group. Learn about setting up subscription groups and ensure that you understand the right level setup for your business model.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the subscription group you want to edit.

-  
To set subscription levels, click Edit Order.

-  
In the window that opens, click the reordering control on the left of the subscription name and drag it to a new position to change the subscriptions’ level.

-  
Click Save.

### Add localizations

You can add languages and enter localized metadata for your auto-renewable subscriptions and subscription groups. For a list of supported languages, visit App Store localizations. Subscription group localizations and subscription localizations are reviewed independently from your In-App Purchase submission. For the properties you can localize, visit Required, localizable, and editable properties. For a detailed example visit Localize app information.

Important: You can manage languages only when the app status is editable.

### Add subscription group localizations

In each localization, you can customize subscription group names and app display options. Users will see these names when they manage subscriptions on their devices.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the subscription group name.

-  
In the Display Name and Description section, click Add.

-  
Follow the prompts to select localizations and enter localized subscription group display names and descriptions.

-  
Click Add.

### Add subscription localizations

The localized display name and description for your subscription appear to each customer could be impacted by certain factors, such as the language of the App Store for their location and the language settings on their device.

Learn about App Store localization.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the subscription group name.

-  
Select the subscription.

-  
In the Display Name and Description section, click Add.

-  
Follow the prompts to select localizations and enter localized subscription group display names and descriptions.

-  
Click Add.

Related Manage pricing for auto-renewable subscriptions Create consumable or non-consumable In-App Purchases

=== SOURCE: overview.html
# The page you’re looking for can’t be found.

Search developer.apple.com

=== SOURCE: https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases/
### App Store Connect Help

App Store Connect / Configure In-App Purchase settings / Overview for configuring In-App Purchases 
Filter ⌘K  
Filter ⌘K  

Configure In-App Purchase settings  

# Overview for configuring In-App Purchases

In-App Purchases let you offer extra content and features in your apps distributed on the App Store — including digital goods, subscriptions, and premium content — directly within your app on all Apple platforms. To make an In-App Purchase available in multiple platform versions of your app, create a single In-App Purchase under the Distribution tab in App Store Connect, then use StoreKit to implement the In-App Purchase in the various platform versions of your app.

Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

There are four types of In-App Purchases:

Type

Description

Consumable

A product that is used once, after which it becomes depleted and must be purchased again. Example: fish food in a fishing app.

Non-consumable

A product that is purchased once and does not expire or decrease with use. Example: race track for a game app.

Auto-renewable subscriptions

A product that allows users to purchase dynamic content for a set period. This type of Subscription renews automatically unless canceled by the user. Example: Monthly subscriptions for an app offering streaming services.

Non-renewing subscriptions

A product that allows users to access content for a limited duration of time. This type of Subscription does not renew automatically. Example: One year subscription to view live gaming content.

You can create up to 10,000 In-App Purchase products per app. Every In-App Purchase must be associated with an app and can be shared across multiple platform versions (iOS, macOS, tvOS). In-App Purchases are not shareable between different apps.

Implementing In-App Purchases in your app requires configuration between your apps’ server and Apple’s servers, as well as set up and ongoing management in App Store Connect. The following workflow can be used:

-  
Accept the Paid Apps Agreement

To offer In-App Purchases, the membership Account Holder must accept the Paid Apps Agreement in the Business section of App Store Connect and provide banking and tax information.

Note: The agreement must be Active to test In-App Purchases in the sandbox environment.

-  
Design your In-App Purchase

To ensure your In-App Purchase experience fits well with the rest of your app and effectively showcases your products, review the Human Interface Guidelines and App Review Guidelines.

-  
Configure In-App Purchases in App Store Connect

Create In-App Purchases and add metadata, such as product name, description, price, and availability. You’ll also need to generate In-App Purchase keys and set a tax category, which will allow Apple to calculate the appropriate tax on customer transactions.

-  
Implement StoreKit

Sign your app with a provisioning profile that includes your app's bundle identifier and the In-App Purchase capability. Make sure the bundle identifier and product identifiers in Xcode match those configured for your app and In-App Purchases in App Store Connect.

-  
Test your In-App Purchases

Apple provides a testing environment, called sandbox, which allows you to test In-App Purchases without incurring charges using test accounts. Test each part of your code to verify that you’ve implemented it correctly by using your app to make In-App Purchases.

You can further test your app and In-App Purchases using either TestFlight, or Xcode.

-  
Use App Store Server Notifications

App Store Server Notifications provide near real-time updates about transaction status and key events related to In-App Purchases, such as a refund or a change in subscription status or Family Sharing access. To leverage these notifications, you’ll need to enter URLs for your production and sandbox server environments in App Store Connect.

-  
Submit your In-App Purchases for review

Before you publish your In-App Purchase on the App Store it must be submitted for review. If you’re submitting your first In-App Purchase, you must submit it with a new version of your app. Ensure you aren't missing any required information before submitting. Monitor In-App Purchase statuses to understand if your In-App Purchase is available or if it needs your attention.

Related Developer Videos Marketing In-App Purchases Auto-renewable subscriptions In-App Purchase programming guide

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-promotional-offers-for-auto-renewable-subscriptions/
### App Store Connect Help

App Store Connect / Manage subscriptions / Set up promotional offers for auto-renewable subscriptions 
Filter ⌘K  
Filter ⌘K  

Manage subscriptions  

# Set up promotional offers for auto-renewable subscriptions

Apps on the App Store with auto-renewable subscriptions can provide a discounted price for a specific duration for existing and previously subscribed customers on iOS, macOS, and tvOS. You can use these offers to help win back subscribers who canceled their subscriptions or promote an upgrade to a higher-ranked subscription at a special price. Customers can accept the offer even if they've already accepted an introductory offer.

To get started, generate keys for In-App Purchases, create a promotional offer on your app's In-App Purchase page for each product, and choose a duration and offer type (pay as you go, pay up front, free). You can have up to 10 active offers per subscription. If you have enabled monthly subscriptions with a 12 month commitment you're limited to 10 active offers for that payment configuration.

Once you've created offers in App Store Connect, use Xcode 10.2 or later to implement the StoreKit APIs to allow these offers to be accepted by customers running iOS 12.2, macOS 10.14.4, and tvOS 12.2, or later.

Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

Get business guidance for auto-renewable subscriptions.

Learn how to set up promotional offers with the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Set up a promotional offer

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions.

-  
Choose the subscription group containing your subscription.

-  
Click the subscription, then go to the Subscription Prices section and click the add button (+).

-  
Select Create Promotional Offer.

-  
Enter a Promotional Offer Reference Name and a Promotional Offer Identifier, then click Next.

-  
Choose Pay as you go, Pay up front, or Free, then choose the appropriate duration and a base price. To search from a larger list of price points, click See Additional Prices. Click Next.

-  
Promotional offers apply to all storefronts where your subscription is available — you can't limit an offer to specific countries or regions. App Store Connect provides comparable prices for each storefront, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.

-  
Make sure the details of your promotional offer are correct and click Confirm.

### Edit a promotional offer

Once you create a promotional offer, only the price can be edited. To edit the duration, type, or offer code, you must create a new offer.

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions.

-  
Choose the subscription group containing your subscription.

-  
Click the subscription, then go to the Subscription Prices section and click View all Subscription Pricing.

-  
Navigate to the Promotional Offers tab, where you'll find all your promotional prices listed.

-  
Click the offer you'd like to edit.

-  
Choose a new price from the menu, and click recalculate to view the updated price in each country or region.

-  
Click Save.

### Delete a promotional offer

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions

-  
Choose the subscription group containing your subscription.

-  
Click auto-renewable subscription, then go to the Subscription Prices section and click View all Subscription Pricing.

-  
Click the offer you'd like to delete, then click Delete Offer.

-  
Confirm your changes in the dialogue.

Related Generate keys for In-App Purchases

=== SOURCE: https://developer.apple.comdoc://com.apple.storekit/documentation/StoreKit/handling-refund-notifications
# Handling refund notifications

Respond to notifications about customer refunds for consumable, non-consumable, and non-renewing subscription products.

### Overview

The App Store server sends near real-time notifications when customers receive refunds for Apple In-App Purchases. If you offer content across multiple platforms, for example gems or coins for games, and you update player account balances on your server, receiving refund notifications is important. Respond to refund notifications by interpreting and handling the refund information, and informing customers in the app of any actions you take as a result of the refund.

To enable notifications, see Enabling App Store Server Notifications and App Store Server Notifications.

#### Receive notifications of customer refunds for one-time purchases

Customers request refunds in several ways, such as:

- Contacting Apple Customer Support and asking for a refund

- Logging in and using Apple’s self-service tool, reportaproblem.apple.com, to request a refund

- Asking their payment method issuer for a refund

When the App Store processes a refund, the App Store server sends a REFUND notification to your server, at the URL you configure. Your server must respond to the post with a 200 response code. The REFUND notification applies to consumable, non-consumable, and non-renewing subscriptions only. To detect refunds for auto-renewable subscriptions, see Detect a Refund.

#### Interpret and handle the refund notification

Your server is responsible for parsing and interpreting all notifications from the App Store server. For the REFUND notification, identify the specific transaction, product ID, and relevant dates from the response:

- Find the most recent transaction for the product_id in the unified_receipt.latest_receipt_info by checking the purchase_date to select the most recent transaction.

- The date when App Store issued the refund is in the cancellation_date_ms field for the transaction.

For more information about the response, see App Store Server Notifications.

You’re responsible to store, monitor, and take appropriate action for each refunded transaction when you receive a REFUND notification. For example, you might build your own in-game currency-rebalancing logic that handles refunded transactions by linking a notification to a player account or session.

Inform customers by presenting contextual messaging in the app for any actions you take as a result of the refund.

#### Identify refund abuse

Reduce refund abuse and identify repeated refunded purchases by mapping REFUND notifications to the player accounts on your server. Monitor and analyze your data to identify suspicious refund activity.

If you offer content across multiple platforms, keep the balances for user accounts up to date on your server. Use App Store Server Notifications to get near real-time status updates for the transactions that affect your customers.

## Refunds

- Testing refund requests: Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-in-app-purchases/overview-of-testing-in-sandbox/
### App Store Connect Help

App Store Connect / Test In-App Purchases / Overview of testing in sandbox 
Filter ⌘K  
Filter ⌘K  

Test In-App Purchases  

# Overview of testing in sandbox

Apple provides a sandbox environment that lets you test In-App Purchases and Apple Pay transactions using test accounts without incurring charges. This environment uses the infrastructure of the App Store and returns transactions as if payments were successfully processed instead of processing actual payments.

You can test the following scenarios:

Scenario

Description

Testing App Store country or region

Test on different storefronts using the same Sandbox account, without having to create new testers. Associate your sandbox testers with any of the 175 App Store storefronts.

Testing auto-renewable subscription events

Test auto-renewable subscription events, such as renewals, state changes, interrupted purchases, winback offers, and contingent pricing without having to wait the length of the subscription duration.

Testing App Store Server Notifications

Test that your server receives App Store Server Notifications and notifications for the sandbox environment.

Testing Family Sharing

Create Sandbox Test Families to test Family Sharing in your app and share access to auto-renewable subscriptions and non-consumables with up to five test family members.

Testing Apple Pay transactions 

Test your app's implementation of Apple Pay with test credit and debit cards. Learn more.

To get started, Create Sandbox Apple Accounts in App Store Connect and use them to sign in to devices that are running a development-signed version of your app. You’ll need to enable Developer Mode on each device so you can use it to test your app.

Alternatively, you can test In-App Purchases with StoreKit Testing in Xcode, a local test environment that doesn’t require a connection to App Store servers to test In-App Purchases. Use StoreKit Testing in Xcode to test In-App Purchases before you configure them in App Store Connect or to test your code when a network connection isn’t available. Learn how to test In-App Purchases with Xcode and sandbox.

Related Testing at all stages of development with Xcode and sandbox Testing In-App Purchases with sandbox Watch “Explore testing In-App Purchases”

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-statuses/
### App Store Connect Help

App Store Connect / Reference / In-App Purchases and subscriptions / In-App Purchase statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# In-App Purchase statuses

The In-App Purchase status indicates whether your In-App Purchase is available or if it needs your attention. A red status indicator means that you need to take action before the product can be made available. A yellow status indicator means that a process controlled by you or Apple is ongoing. A green status indicator means that the In-App Purchase is available. 

-  
A red status indicator () means that you need to perform some action before a product can be made available.

-  
A yellow status indicator () means that some process is ongoing, controlled either by you or by Apple.

-  
A green status indicator () means that the In-App Purchase is available.

Status

Description

Prepare for Submission

Your In-App Purchase has been created, but you haven't yet submitted it for review. Use Add for Review to add it to a submission. If your In-App Purchase is missing required metadata, complete it before adding for review.

Ready for Review

Your In-App Purchase has been added to a submission, but you haven't sent the submission to App Review yet. While your product is in this state, you can edit only the reference name, pricing, and availability.

Waiting for Review

You have submitted your In-App Purchase to be reviewed by Apple. While your product is in this state, you can edit only the reference name, pricing, and availability.

In Review

Your In-App Purchase is currently being reviewed by Apple. While your product is in this state, you can edit only the reference name, pricing, and availability.

Accepted 

Your In-App Purchase has been accepted, but one or more other items in the same submission were rejected. Your In-App Purchase won't be approved until all items in the submission are accepted. You can edit the rejected items and resubmit them, or remove them from the submission.

Approved

Apple has approved your In-App Purchase. For this status to appear, you must provide country or region availability for your In-App Purchase. If you select "Remove from Sale," the status appears as "Developer Removed from Sale."

Rejected

Apple has rejected your In-App Purchase during the review process. You can edit the item and use Update Review to resubmit it. If you haven't been contacted by Apple with more information about the rejection, you can inquire through Contact Us.

Developer Rejected

You removed your In-App Purchase from review. When you're ready, use Add for Review to resubmit it.

Developer Removed from Sale

You removed the In-App Purchase from sale. Customers who already purchased it retain access. Those transactions are available with StoreKit and in the App Store Server API. To make the In-App Purchase available for sale again, update its availability settings.

Removed from Sale

Apple removed this In-App Purchase from sale.

Related In-App Purchase information Set availability for In-App Purchases Schedule price changes for In-App Purchases

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription/
### App Store Connect Help

App Store Connect / Manage subscriptions / Set availability for an auto-renewable subscription 
Filter ⌘K  
Filter ⌘K  

Manage subscriptions  

# Set availability for an auto-renewable subscription

You have the option to make your auto-renewable subscription available in any of 175 countries or regions where the App Store is offered. A customer’s Apple Account country or region setting determines which storefront they can purchase auto-renewable subscriptions from. For example, an account set to Japan can only purchase content from the App Store in Japan.

Keep in mind that even if you set availability for a subscription, it may not be available for purchase. Monitor the In-App Purchase statuses to understand if action is needed from you, such as completing missing metadata, or if your In-App Purchase has been approved by App Review.

Learn how to set availability for auto-renewable subscriptions with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Set availability for a subscription

-  
In Apps, select the app you want to view. 

-  
In the sidebar, click Subscriptions.

-  
On the subscriptions detail page, click the subscription group.

-  
Click the subscription you want to set up availability for.

-  
In the Availability section, click Set Up Availability.

-  
Select the countries or regions where you want to make your subscription available.

-  
Click Done.

Keep in mind that even if you set availability for an auto-renewable subscription, it may not be available for purchase. Monitor the In-App Purchase statuses to understand if action is needed from you, such as completing missing metadata, or if your In-App Purchase has been approved by App Review.

### Make changes to your auto-renewable subscription’s availability

-  
In Apps, select the app you want to view. 

-  
In the sidebar, click Subscriptions.

-  
On the subscriptions detail page, click the subscription group.

-  
Click the subscription you want to edit availability for.

-  
Under Availability, click Edit.

-  
In the dialog that appears, change your subscription’s availability by selecting or deselecting your desired countries or regions. 

Note: You must be the Account Holder in order to remove countries or regions, as this will impact existing subscribers.

-  
Click Done.

-  
On the top right, click Save.

If you want to discontinue an auto-renewable subscription, consider the impact on users and any communications you might need to provide. Also consider whether your app still functions without the subscription. If not, remove your app from the App Store.

Keep in mind that you’re required by the Paid Apps Agreement to provide the full amount of content to eligible subscribers through the subscription duration.

Taking the following steps before removing your auto-renewable subscription from sale can help ensure a smooth experience:

-  
Before discontinuing an auto-renewable subscription, remove it from sale, within App Store Connect, to stop additional sign-ups and renewals. We recommend timing the removal of your subscription to be equivalent to its duration. A minimum of 31 days is required from the date subscription is removed from sale and service is stopped to allow monthly and shorter duration subscriptions to expire.

-  
For subscriptions longer than one month, if you're unable to provide the full amount of content to eligible subscribers through the subscription duration before removing the subscription, contact us.

-  
Provide subscribers with advanced notice of the discontinuation of your subscription service through channels such as email, website, and in-app messaging. We recommend notifying them at least 31 days before discontinuing the subscription service.

-  
End any promotions of the subscription to discourage purchases.

To remove your subscription from sale:

-  
In Apps, select the app you want to view. 

-  
In the sidebar, under Monetization, click Subscriptions.

-  
Click the subscription group, then the subscription.

-  
Under Availability, click Removing from Sale and confirm to remove your subscription from sale.

-  
Click Save.

Apps in the Magazines and Newspapers category need at least one active auto-renewable subscription to be listed in that category. If you want to discontinue the only auto-renewable subscription in your app, you must switch to a different category and submit a new binary to App Store Connect. Then you'll be able to remove the subscription.

### Offer monthly subscriptions with 12 month commitment

For subscriptions outside the United States and Singapore, you have the option to configure a billing option where subscribers commit to paying monthly for a set period of time. Unlike a standard monthly subscription, the subscriber is committing to 12 monthly payments. Once all 12 payments are completed, the subscription automatically renews into another 12 month commitment at the standard billing price of that payment option until they choose to cancel. Subscribers can view their completed and remaining payments at any time in their Apple Account, and Apple will send reminders ahead of the next commitment period. This is useful if you want to offer subscribers more affordable options.

Monthly with 12-month commitment subscriptions are only available on devices that use operating system version 26.4 or later (on all storefronts except the United States and Singapore, and excluding watchOS) and apps built with an SDK version of 26.5 or later.

-  
In the Sidebar, under Monetization, click Subscriptions.

-  
Click a subscription group name.

-  
Click Create.

Note: If you're adding a subscription to a group that already has existing subscriptions, you'll click the add button (+).

-  
Enter the subscription’s reference name and Product ID.

-  
Under Subscription Duration, select 1 Year.

-  
Click Create. Once you've created your subscription product, you'll be taken to its information page to add more details.

-  
In the Availability section under 1 Year Upfront, click Set Up Availability.

-  
Select the countries or regions where you'd like the subscription to be available. When this option is enabled, customers will pay for an entire year upfront when they subscribe. When their subscription renews, they'll be billed for another full year if they don't cancel before renewal. Setting up upfront billing availability is required before you can offer the monthly payment option. If you only complete this step, your subscription will be available only as a single upfront annual payment.

-  
Click Confirm.

-  
To give subscribers the option to pay monthly with a 12 month commitment, click Set Up Availability in the Monthly with 12-Month Commitment section.

-  
Select the countries or regions where you'd like to offer the monthly payment option. Customers will commit to paying the monthly price for 12 months before their subscription renews. If a customer cancels before the end of their commitment, they'll continue paying until their commitment is complete (except in certain regions), and their subscription will not renew.

Note: Monthly billing will only be available in countries or regions where you have set up upfront billing availability.

-  
Click Confirm.

-  
In the Subscription Prices section, click Add Subscription Price. 

-  
Choose an upfront and monthly price in the base territory for this subscription, and we'll automatically calculate the prices for all 175 countries or regions based on the most recent foreign exchange rates. The 12-month commitment total must be greater than or equal to the upfront price, and less than or equal to 1.5 times the upfront price. You can edit prices for individual countries or regions (excluding the United States and Singapore) in the next step.

-  
Click Next.

-  
App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.

-  
Review your prices and Click Confirm. 

-  
Optionally, configure subscription offers. Upon completion of the offer period, customers will renew to the 12 month payment commitment.

-  
You can remove this monthly billing option in App Store Connect at any time. In the Availability section under Monthly with 12 Month Commitment, click Remove Monthly Billing. Confirm you want to remove the option and click Confirm. Existing customers won't renew at the end of their 12 month commitment, and new customers won't be able to subscribe to that payment option.

Related Manage availability for your app on the App Store Set availability for In-App Purchases

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-purchase/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit an In-App Purchase 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit an In-App Purchase 

You can submit In-App Purchases and subscriptions for review directly from the In-App Purchases and Subscriptions sections in App Store Connect. Items you add for review are collected in a submission, which you can submit with or without an app version.

Note: The first consumable, non-consumable, auto-renewable subscription, and non-renewing subscription In-App Purchase of each type must be submitted with a new app version. After the first item of a given type is approved, you can submit additional items of that type without a new app version, as long as your app has at least one approved app version at the time of submission. If your app doesn't have an approved version, include one in your next submission.

Learn how to submit In-App Purchases and subscriptions with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Submit an In-App Purchase for the first time

After creating your In-App Purchase or subscription, click Add for Review to add it to a submission. If this is the first time you're submitting that type of In-App Purchase or subscription, include a new app version in the submission. If you're submitting a new subscription it must be submitted together with its subscription group. Each new subscription group must be submitted with at least one of its subscriptions. The app version, subscription group, and every subscription or In-App Purchase you want reviewed together must all be added to the same draft submission before you click Submit for Review.

-  
In Apps, select the app you want to view.

-  
In the sidebar under Monetization, click In-App Purchases or Subscriptions.

-  
Click the In-App Purchase or subscription you want to submit.

-  
Click Add for Review. If you have an existing submission, you can add the item to it or click Create New Submission. 

-  
If your In-App Purchase or subscription requires a new app version, select a platform and the app version to include in your submission. If you're submitting a subscription and the subscription group hasn't been approved yet, add the subscription group to the submission as well. You can add up to 200 items per submission at a time. 

-  
In the submission modal, review the items in your submission and click Submit for Review.

Once your first consumable or non-consumable In-App Purchase has been approved, you can add additional In-App Purchases of that type without including an app version. The same applies for auto-renewable and non-renewing subscriptions.

Note: 

-  
In-App Purchases with content hosting can no longer be submitted for review. You can still make changes to their pricing and availability.

-  
In-App Purchases and subscriptions aren't supported on Apple Watch. To submit an Apple Watch app version, remove all in-app purchases and subscriptions from the submission.

### Add In-App Purchases or subscriptions to an existing submission

You can add multiple In-App Purchases or subscriptions to a submission at the same time from the In-App Purchases or Subscriptions page.

-  
In Apps, select the app you want to view.

-  
In the sidebar under Monetization, click In-App Purchases or Subscriptions.

-  
Click Edit. For subscriptions, first select a group, then click Edit.

-  
Select the items you want to submit.

-  
Click Add for Review. When you click Add for Review, a dropdown appears if there are any existing draft submissions. Select an existing submission to add an item to it, or click Create New Submission to start a new one.

-  
If any items can't be added to the submission, a banner identifies which items weren't added and includes a link to each item. You can add up to 200 items per submission at a time.

### View your submissions and submission history

The App Review section of the sidebar shows all your In-App Purchase and subscription submissions in one place — both active submissions and a history of completed ones.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Review. Draft submissions appear under Drafts, showing the date created, platform, number of items, and status. All other submissions appear under Submissions. App Store Connect shows your last 10 completed submissions from the past 180 days.

-  
Click a submission to view its details. If App Review rejected any items, the reason and relevant guideline citation appear under Messages. You can reply to App Review directly from the submission detail page.

### Resolve and resubmit a rejected In-App Purchase or subscription

If App Review rejects one or more items in a submission, you can edit each rejected item and update the submission before resubmitting for review.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Review and open the submission.

-  
Review the rejection reason in the Messages section and make the necessary changes by clicking Edit next to the rejected item.

-  
Click Save.

-  
Click Update Review to update the item in the submission.

-  
Repeat steps 3–6 for any other rejected items in the submission, or remove them from the submission.

-  
Once all rejected items are resolved or removed, click Resubmit to App Review.

Note: If you haven't been contacted by Apple with more information about the rejection, you can inquire through Contact Us.

=== SOURCE: https://developer.apple.com/app-store/subscriptions/
Win-back offers are now available
Offer codes now available for macOS

# Auto-renewable subscriptions

Offer a seamless experience for digital subscriptions in your apps. StoreKit APIs provide a simple, powerful way to implement auto-renewable subscriptions in apps on all Apple platforms and in all App Store categories.

## What’s New

Offer subscribers more affordable options with a new payment option: monthly subscriptions with a 12-month commitment.

## Overview

Auto-renewable subscriptions provide access to content, services, or premium features in your app on an ongoing basis. They automatically renew at the end of their duration until the user chooses to cancel. Subscriptions are available on iOS, iPadOS, macOS, tvOS, visionOS, and watchOS.

Great subscription apps justify the recurring payment by providing ongoing value and continually innovating the app experience. If you’re considering implementing the subscription model, plan to regularly update your app with feature enhancements or expanded content.

Many types of apps can take advantage of subscriptions, including apps that offer new game levels, episodic content, software as a service, or cloud support. Other appropriate subscriptions include apps that offer consistent, substantive updates, or access to libraries or collections of content. You can offer subscriptions (a type of in-app purchase) alongside other in-app purchase types.

### Getting ready

To offer subscriptions, youʼll need to configure them in App Store Connect and use StoreKit APIs in your app. You’ll also need to assign each subscription to a subscription group (a group of subscriptions with different access levels, prices, and durations that people can choose from), then add details such as a name, price, and description. This information displays in the Apple In-App Purchases section of your app’s product page on the App Store. Ensure that the subscriptions are available across all device types that your app supports. Consider allowing a way for subscribers to see the status of their subscription within your app, along with upgrade, crossgrade, and downgrade options, as well as a way to easily manage or turn off their auto-renewable subscription. Make sure to follow our design and review guidelines.

To get ready:

- Watch the Apple In-App Purchase and Subscriptions videos.

- Refer to the Apple In-App Purchase StoreKit API documentation.

- Learn how to configure your subscriptions in App Store Connect Help.

- Use the App Store Server API and enable App Store Server Notifications to get real-time changes to the status of your subscriptions.

### Understanding subscription guidelines

Before creating your subscriptions, make sure you understand the requirements and best practices that will help you deliver a great experience. The guidelines below provide details on what your subscriptions need to include and how they should be presented in your app, as well as information on making changes to existing subscriptions, offering free trials, and more.

Resources:

- App Review Guidelines

- Human Interface Guidelines

### 85% net revenue after one year

The net revenue structure for auto-renewable subscriptions differs from other business models on the App Store. During a subscriber’s first year of service, you receive 70% of the subscription price at each billing cycle, minus applicable taxes. After a subscriber accumulates one year of paid service, your net revenue increases to 85% of the subscription price, minus applicable taxes.

Here’s how it works:

- Auto-renewable subscriptions on all Apple platforms are eligible.

- Days of paid service include all subscription offer types (introductory, promotional, and offer codes) with paid pricing options (pay as you go, pay up front).

- Free trials and renewal extensions are excluded from days of paid service.

- Days of paid service are specific to each subscription group.

- Upgrades, downgrades, or crossgrades between subscriptions in the same subscription group don’t affect the one year of paid service.

- If you’re currently enrolled in the App Store Small Business Program, you receive 85% of the subscription price at each billing cycle (minus applicable taxes), regardless of whether or not the subscription has accumulated one year of paid service.

If a subscription expires due to a cancellation or billing issue, the days of paid service stop accumulating. If the subscription is renewed within 60 days, the days of paid service resume from the recovery date.

## Creating subscriptions

You’ll configure your auto-renewable subscriptions in App Store Connect. Create each subscription product as part of a subscription group and assign it a level. How you set up your subscription group or groups will determine your proceeds rate, as well as how people can subscribe to your content or services, how they move between subscriptions, and when they are billed. Before creating subscriptions, identify the right subscription setup for your business model.

### Creating a subscription group

Each subscription you offer must be assigned to a subscription group. A subscription group is made up of subscriptions with different access levels, prices, and durations so people can select the option that best fits their needs. Since people can only buy one subscription within a group at a time, creating a single group is the best practice for most apps as it prevents people from accidentally purchasing multiple subscriptions.

If your app needs to offer the ability to buy multiple subscriptions — for example, to subscribe to more than one channel in a streaming app — you can add these subscriptions to different groups. People who buy subscriptions in multiple groups are billed separately for each subscription. Keep in mind that if someone cancels a subscription in one group and then purchases a new subscription in a different group, the renewal date will change and the days of paid service will reset.

Multiple subscription groups aren’t recommended for apps in which people would expect to have a single active subscription. Keep your offerings simple and easy to understand. For each subscription, create a user-friendly, self-explanatory name that differentiates it from others in the group. Use distinct names for the app, the subscription group, and each subscription to avoid confusion.

App Name or Custom App Name  
Subscription Display Name  
Price/Duration   

App Name or Custom App Name  
Subscription Display Name  
Price/Duration    

### Ranking subscriptions within the group

If you offer multiple subscriptions with different prices tiers, you can assign each to a level in App Store Connect. Ranking your subscriptions determines the upgrade, downgrade, and crossgrade paths available. Arrange your subscriptions in order from the one that offers the most (level 1) to the one that offers the least. For subscriptions with lower service or content offerings, you might assign level 2 or 3, depending on your intended subscription experience. You can add more than one subscription to each level if the offerings are equal. For details, see Overview of an Auto-renewable Subscription Group Setup.

People can manage their subscriptions in their account settings on the App Store, where they see all renewal options and subscription groups, and can choose to upgrade, crossgrade, or downgrade between subscriptions as often as they like. You can also use the showManageSubscriptions(in:) method to allow them to do this within your app. When someone makes a change in their subscription level, the timing of the change varies depending on what has happened:

Upgrade. Someone purchases a subscription that offers a higher level of service than their current subscription. They’re immediately upgraded and receive a refund of the prorated amount of their original subscription. If you’d like people to immediately access more content or features, rank the subscription higher to make it an upgrade.

Downgrade. Someone selects a subscription that offers a lower level of service than their current subscription. The subscription continues until the next renewal date, then is renewed at the lower level and price.

Crossgrade. Someone switches to a new subscription of the equivalent level. If both subscriptions are pay-up-front subscriptions and the same duration, the new subscription begins immediately. If the durations are different, the new subscription goes into effect at the next renewal date. When at least one subscription is a monthly subscription with a 12-month commitment, the commitment durations and billing plan types of the subscriptions are also considered. Learn more

### Pricing subscriptions for each territory

Apps with auto-renewable subscriptions can choose from 800 price points across all available currencies and price tiers, with an additional 100 higher price points available upon request. You can set the prices you think are appropriate for subscribers in different locations, and you have the flexibility to price your subscriptions at parity across storefronts.

Pricing tool. The App Store Connect pricing tool can help you manage pricing based on current exchange rates. If there’s a tax change or currency adjustment in a particular region, the price of subscriptions won’t generally be affected unless you decide to pass the change on to your users. If you want to change the price of a subscription in a specific market, it’s important to understand which markets are tax inclusive before you take action. For example, if you decide to lower the subscription price for users in Germany, the revenue you’ll receive will be the purchase price minus the European Union’s value added tax (VAT) and minus Apple’s commission. The default pricing in the App Store Connect pricing tool is inclusive of applicable taxes that Apple collects and remits. For more information, review Schedule 2 of the Apple Developer Program License Agreement, which describes territories that have different tax treatments.

App Store Connect also lets you assign tax categories to your apps and Apple In-App Purchases. These categories are based on your app’s content (for example, videos, books, or news publications) and determine which tax regulations apply in each territory, allowing Apple to administer tax for you at specific rates.

###   Family Sharing 

Family Sharing allows a subscriber to share access to an auto-renewable subscription with up to five family members across their Apple devices. With a streamlined, convenient user experience, Family Sharing can help you attract subscribers, encourage paid subscriptions, increase engagement, and improve retention. You can enable Family Sharing for your subscription in App Store Connect. Please note that this can’t be undone.

Verify subscription access using purchase validation, then provide the proper access to subscribers and their family members. Whether a subscription is shared with a subscriber’s family by default depends on their subscription sharing settings and if the purchase was made before or after you enabled Family Sharing in App Store Connect. Subscribers whose settings don’t share the subscription by default are informed by Apple via push notification that the subscription can be shared with their family.

You can highlight Family Sharing in several ways:

Highlight Family Sharing to potential subscribers. Include Family Sharing in your subscription’s display name so it’s easy to spot when reviewing subscription options. If you offer a Family Sharing-enabled subscription alongside subscriptions that don’t include Family Sharing, you can note the price difference for the Family Sharing option on the sign up screen.

Remind subscribers to enable Family Sharing. Mention Family Sharing within your app — for example, as part of onboarding for new subscribers or via in-app messaging for existing subscribers. Consider explaining how to confirm they’ve turned on Family Sharing for the subscription. If you offer a Family Sharing-enabled subscription they’re not currently subscribed to, you might provide a way for them to upgrade without leaving your app. Make sure you’ve ranked your subscriptions within the same subscription level in App Store Connect to provide a seamless upgrade experience.

Help subscribers share subscriptions. You can use in-app messaging to ask subscribers to confirm their Family Sharing settings, or implement share extensions so they can easily share your app. Within the transaction information, you can look at ownershipType to see if someone is the subscriber or a family member, so you can make sure to display your message to the person who completed the purchase.

Resources:

- Turn on Family Sharing for in-app purchases

- Support Family Sharing in your app

- Family Sharing for in-app purchases

### Offering subscriptions to multiple apps

You can offer auto-renewable subscriptions to access multiple apps. Each app must be approved to use auto-renewable Apple In-App Purchases and published under the same developer account.

Use App Store Connect to set up separate and equivalent auto-renewable subscriptions for each app included in the multiapp subscription so that people can subscribe from any app. To help people avoid paying multiple times for the same offering, make sure to verify that they’re active subscribers before showing any subscription options. View details on determining if a subscription is active.

You can also create an app bundle to group multiple subscription apps into a single download at a reduced price. App bundles can include up to 10 of your iOS apps or up to 10 of your macOS apps.

Resources:

- App bundle essentials

- Offer subscriptions across apps

## Attracting subscribers

By allowing people to try your subscription at the moment they’re most interested in its value, you increase the likelihood that they’ll subscribe. There are several ways you can provide a preview of the subscription experience.

Present subscription benefits during onboarding. By highlighting the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they’ll gain from subscribing. Keep onboarding brief, engaging, and focused on the features your audience cares about, such as the ability to access the subscription across multiple device types. Provide a succinct call to action and clear subscription terms.

Find out what you’ll need to include

Offer a freemium app experience. A freemium app allows customers to use the app at no cost, with the option to subscribe if they want to enhance their experience or engage more deeply. A free experience lowers the barrier to try an app, and people may be more inclined to invest in paid features after having had time to enjoy the app.

Offer a metered paywall. A metered paywall allows access to a finite amount of content for a specified duration before needing to make a purchase — for example, viewing 10 full articles per month for free in a news app. This gives people the opportunity to immediately start sampling your subscription experience, while encouraging them to subscribe.

For freemium and paywall experiences, include contextually relevant prompts to encourage people to subscribe — for example, when they near their monthly limit of free articles or videos. Additionally, consider making it easy to subscribe at any time by including a prompt throughout the app interface. Test and measure the impact of these prompts, and consider trying different versions of your call-to-action messaging to understand what resonates most with your audience.

Optimize subscriptions for success: acquisition

### Clearly describing subscriptions

An effective subscription purchase flow makes it simple for people to get the product or service they’re interested in. Use consistent messaging and include clear terms so people can easily recognize the value of the offer. A lengthy sign-up process will lower your subscription conversion rate, so keep the purchase flow simple and only ask for necessary information. In addition, the following details must be included in your subscription’s sign-up screen:

- Subscription name and duration, and the content or services provided during the subscription period

- Full renewal price, shown clearly and prominently, and localized in available currencies

- A way for current subscribers to sign in or restore purchases

Please note that your app and App Store metadata must include links to your Terms of Use and Privacy Policy.

Billing amount
In the purchase flow, the amount that will be billed must be the most prominent pricing element in the layout. For example, an annual subscription should clearly display the total amount that will be billed upon purchase. While you may also present a breakdown price that the annual amount is equivalent to or a savings when compared to weekly or monthly subscriptions, these additional elements should be displayed in a subordinate position and size to the annual price. This ensures that people are not misled.

Free trials
In the purchase flow for a free trial, clearly indicate how long the free trial lasts and the price billed once the free trial is over.

### Promoting subscriptions on the App Store

You can promote Apple In-App Purchases directly on the App Store, so people can find your subscription or introductory offer and initiate a purchase even before downloading your app. Promoted Apple In-App Purchases appear on your product page, can display in search results, and may be featured on the Today, Games, or Apps tabs. Choose to promote up to 20 Apple In-App Purchases at a time to help you effectively increase discoverability for content within your app. This can be particularly effective for letting new customers know about introductory offers.

Learn about promoting your in-app purchases

Promoted Apple In-App Purchases have unique metadata to communicate their value.   

## Providing subscription offers

Grow, retain, and re-acquire customers by giving them a free or discounted price for a specific duration for an auto-renewable subscription. At the end of the offer period, the subscription auto-renews at the standard price unless a subscriber cancels it.

You can create introductory offers, offer codes, promotional offers, and win-back offers. You can provide some or all of these at once, depending on your business goals. To determine which might be best for a particular use case, consider each offer’s intended use, customer eligibility, redemption limits, and other criteria.

Acquire Retain Re-acquire    
Introductory offers     
Promotional offers     
Win-back offers     
Offer codes       

#### Optimize subscriptions for success: acquisition

#### Improve your subscriber retention with App Store features

### Configuring subscription offers

When setting up offers in App Store Connect, you’ll choose the offer type, eligibility, duration, pricing, and more. To support offers within your app, you’ll use StoreKit APIs. For each offer you create, you’ll choose one of the following offer discount types:

Free trial. A subscriber can access your subscription for free for a specific duration — for example, a one-month free offer for a subscription with a standard renewal price of $4.99 per month. Their subscription begins immediately, but they won’t be billed until the offer duration ends. This discount type may be useful if you want to let people experience your subscription at no immediate cost to them.

Pay as you go. A subscriber pays a discounted price each billing period for a specific duration — for example, $1.99 per month for three months for a subscription with a standard renewal price of $9.99 per month. Once the duration is over, they’re billed at the standard renewal price. This option may be useful if you want to attract price-sensitive people with a recurring discount without having to offer that discount for the lifetime of the subscription.

Pay up front. A subscriber pays a one-time price for a specific duration — for example, $9.99 up front for the first six months of a subscription with a standard renewal price of $39.99 per year. Once the duration is over, they’ll be billed at the standard renewal price. This may be useful if you want to offer an extended experience that gives people time to enjoy the subscription before the next renewal.

### Introductory offers

Introductory offers allow new subscribers to experience your subscription before paying full price. Display offers within your app using StoreKit, and promote the offer’s Apple In-App Purchase to display it on the App Store. When promoted, your offer appears on your product page and may display in search results as well as on the Today, Games, and Apps tabs — helping to further discovery of your offer. You can create an introductory offer for each subscription per territory. Customers can redeem one introductory offer per subscription group.

### Offer codesNow available on macOS

Use offer codes to acquire, retain, and re-acquire subscribers by providing a subscription at a discount or for free for a limited time. You can create two types of offer codes: one-time-use codes (18-digit unique codes), or custom codes (such as SPRINGPROMO). Learn how to create offer codes and how to support offer codes using StoreKit. To get notified of redemptions, ensure you've set up App Store Server Notifications.

#### Distribution

When distributing offer codes, you can use your online and offline marketing channels, such as in-app merchandising, email, or print campaigns. Consider which channels might be most effective at reaching your intended customers.

Offer codes can be used in a variety of ways — for example, you can:

- Send an email sharing the latest features and recently added content with an offer code to current or previous subscribers, so they can experience your service for a limited time.

- Distribute flyers that include custom codes to promote your service to event attendees.

- Partner with another company on a marketing initiative or campaign to help promote your app to new subscribers.

- Create a peer-to-peer member referral program that enables current subscribers to share an offer code and receive a benefit for promoting your app. You are responsible for distributing any benefits or rewards to subscribers.

- Provide a code to a subscriber with a customer service issue to compensate for the issue and encourage retention.

- Distribute one-time-use codes within an app that you’re sunsetting as a way to transition current subscribers to your new app and promote your service.

- Display a save offer in your app to a subscriber who has turned off auto-renew but their subscription hasn’t expired yet.

#### Redemption

Customers can redeem offer codes using a redemption URL or on the App Store (in iOS 14.2, iPadOS 14.2, and macOS 15 or later). They can also redeem offer codes within your app if your app supports the offerCodeRedemption method. For a smooth customer experience, be sure to mention any eligibility or availability limits in your communications.

Apple handles the redemption experience, which includes an offer details screen that includes your app icon, subscription display name, duration, and pricing. If you’ve previously added a promotional image for the subscription, this is shown instead of your app icon. To help people make an informed decision, make sure that these details clearly describe the subscription experience. In order for offer codes to be redeemed, your app must be available on the App Store. If someone doesn’t have your app, they’ll be able to download it during the redemption experience.

Depending on your subscription setup, existing subscribers may be able to redeem more than one offer if the offers are in different subscription groups. If you intend for someone to subscribe to only one subscription group at a time, make sure the offer is within their current subscription group. Existing subscribers can only redeem codes that are an upgrade from or at the same level as their current subscription.

Be sure to provide a relevant experience based on someone’s subscription status. For example, you might provide onboarding that highlights the benefits of your subscription for new subscribers. If your app includes account creation or requires agreement to additional terms, make this process as smooth as possible for customers who redeemed a code and are new to your app.

#### Subscription offer codes essentials

#### Get started with custom offer codes

### Promotional offers

Grow and retain your customer base by giving existing or former subscribers a free or discounted subscription for a specific duration. You decide the business logic for promotional offers, giving you the flexibility to create unique promotions within your app, such as:

- An upgraded subscription at a special price for people who have canceled their subscription

- A free month of service for a tenured subscriber who has renewed multiple times

- A discounted price on a month of service for a subscriber who may not be consistently engaging with your app or game

Use StoreKit or App Store Server APIs to identify the auto-renewal statuses of your subscribers and understand which offers might be most effective. To easily determine eligibility, enable App Store Server Notifications for your app. This allows you to receive notifications when a subscriber's status changes, helping you understand when to display an offer to someone. You can have up to 10 offers for each subscription — be sure to consider the implications of having multiple offers in effect. Learn about configuring promotional offers in App Store Connect.

### Win-back offers

Reach previous subscribers and encourage them to resubscribe with win-back offers. Based on your configuration, Apple displays these offers to eligible customers in various places, such as on the App Store or in your app or game. For example, you can create a pay up front offer for a reduced subscription price of $9.99 for six months, with a standard renewal price of $39.99 per year.

#### Discovery and redemption

Eligible customers can discover and redeem win-back offers in several places, including:

On the App Store: On your product page and in editorial selections and personalized recommendations on the Today, Games, and Apps tabs if you’ve been featured. People can tap your offer to learn more details about your offer and open or redownload your app or game to seamlessly redeem your offer.

In-app: A win-back offer sheet automatically appears to eligible customers within your app or game, with no additional work required. For additional control and display customization, you can use StoreKit views or StoreKit 2 APIs to merchandise win-back offers in your app.

In their Apple account under their Subscription settings. People can tap your app or game to view and redeem any available offers. This appears automatically with no additional work required.

Using a direct link. Similar to offer codes, you can use the URL provided in App Store Connect and share it with people through your own channels, such as email.

For more information on these placement types, see set up win-back offers.

#### Configuration and merchandising

When configuring win-back offers in App Store Connect, you provide offer details and select the offer priority. Your priority selection affects how your offer is ranked within your app, in someone’s Subscription settings, and on the App Store (if you’ve chosen to promote it). Apple uses your subscription display name and description when displaying your win-back offer, so be sure this information is accurate.

If you’d like to display your offer on the App Store, you’ll need an approved subscription image. Aim for a simple graphic that’s different than your app icon or screenshots that conveys the essence of the Apple In-App Purchase included as part of the offer.

By default, streamlined purchasing is turned on for your app or game, which lets people complete a purchase from outside your app. You can turn this off in App Store Connect if you wish.

#### Implement App Store Offers

## Keeping subscribers

For people to stay subscribed to your app, they need to continue getting value out of the subscription. Update your app regularly with new content and feature enhancements to help encourage subscribers to maintain their subscriptions.

### Sending notifications

When written thoughtfully, notifications can help people stay engaged with your service and keep their subscriptions active. To ensure a positive experience, make sure your notifications are timely, serve a clear purpose, and deliver meaningful information. You can also use push notifications to market your content — for example, promoting a subscription offer to people who haven’t yet subscribed. However, people must first explicitly opt in to receiving marketing push notifications via a method within your app that includes consent language and a clear way of opting out. Carefully consider the frequency, timing, and content of your notifications to ensure they always provide value to subscribers. Push notifications must not include sensitive personal or confidential information.

- View design guidance

- Get details on implementing notifications

### Providing support

Thoughtful customer support helps you manage relationships with your subscribers and can lead to improved engagement, higher retention, and better ratings and reviews. Use StoreKit and App Store server APIs to provide more seamless subscriber support, and to resolve issues in a more timely and efficient manner.

#### Letting people manage their subscriptions

A subscriber’s preferences may change during a subscription period. You can use the showManageSubscriptions(in:) method to let them manage their subscription within your app. By providing a dedicated place in your app to manage subscriptions, you can also display other options to complement the system-provided management UI. For example, you might show a promotional offer that provides a higher service level for a discounted price. If they cancel, you might provide an offer to help win them back and encourage them to resubscribe. Or you might present a survey where they can share feedback about their subscription experience and reasons for cancelling, which can inform your marketing strategy. To ensure a positive experience, always make it easy for people to access the system-provided management UI where they can cancel if they wish.

#### Extending a subscription’s renewal date

In cases of service or content delivery issues — such as a server outage or technical glitch — you can extend the renewal date of a subscription using the Renewal Date Extension endpoint. For example, if a sports match is canceled or there’s an interruption to a livestreamed event, you might extend free service for a specified time in order to make up for the issue. You can move the renewal date for a customer’s subscription twice per calendar year, each up to 90 days in the future. Any days included in an extension won’t count toward the one year of paid service needed to receive an 85% proceeds rate.

Alternatively, you can use offer codes to compensate dissatisfied subscribers with a free or discounted subscription for a specific period of time. These codes can be redeemed on the App Store or within your app.

#### Determining subscriber status

The Get All Subscription Statuses endpoint lets you determine in one simple check whether a subscription is active, expired, in billing retry, or in grace period. Use this information to inform your retention strategy and provide subscribers with relevant information within your app, such as their upcoming renewal date. You can also use this endpoint alongside the OfferID and OfferType transaction properties in StoreKit to identify offer redemptions.

- Learn to support customers with StoreKit 2 and the App Store Server API

- Learn to support customers and manage refunds

- Learn to help people manage their subscriptions

### Retaining subscribers

Use the Get All Subscription Statuses endpoint and Get Transaction History endpoint to determine the status of your users’ subscriptions and view transaction history, so you can identify and act on:

Voluntary churn. Determine if a subscriber has turned off auto-renew for a particular subscription using the Get All Subscription Statuses endpoint. You can also use App Store Server Notifications to get real-time updates about changes in a user’s status and key events related to their Apple In-App Purchases, such as a change in renewal status. Use this information to take action in response. For example, you might present a promotional offer or suggest an alternate tier that better fits their needs. When a subscription expires, you can lock access to the subscription’s content or service. Be sure to inform the user of any changes and let them know if there’s anything they need to do in response and how to resubscribe if needed.

Involuntary churn. Sometimes a subscriber might experience a billing issue, such as an expired credit card, that causes their subscription to expire. Starting in iOS 16.4 and iPadOS 16.4, if a subscription doesn’t successfully renew, a system-provided sheet appears in your app upon launch with a prompt that lets customers update the payment method for their Apple Account. If you’d like, you can choose to delay or suppress this sheet in StoreKit using messages and display.

You can learn when a subscription fails to renew using:

- App Store server notifications, which sends a DID_FAIL_TO_RENEW notification type.

- StoreKit renewal state to get information about the renewal state.

- The App Store Server API to get all subscription statuses.

When a subscription renewal fails, Apple attempts to recover it for 60 days. If you’ve chosen to pause access to your service or content during this time, you’ll need to reinstate access once the issue is resolved. If the subscription renews within 60 days, the days of paid service resume from the renewal date.

To prevent service interruptions due to billing issues, enable Billing Grace Period in App Store Connect. Apple attempts to address the billing issue and recover the subscription while the subscriber retains subscription access. You can choose to apply Billing Grace Period to all renewals (existing paid renewals and free offers transitioning to paid renewals) or only to existing paid renewals. You can also set a duration of 3, 16, or 28 days. Be sure to consider what Billing Grace Period configuration best aligns with your business. If the subscription is recovered within the Billing Grace Period, there won’t be any interruption to the days of paid service or to your revenue. If someone resubscribes after 60 days, the days of paid service reset and you’ll receive the standard one-year subscription rate until the next year of paid service passes.

Price increase consent. When you increase the price of a subscription and Apple asks affected subscribers to agree to the new price, you can keep track of their consent status before the change takes effect. Before displaying the price increase sheet to affected users, you might show an in-app message that explains the benefits of the subscription and how the price increase improves the service. If someone doesn’t respond to the increase, their subscription expires at the end of their current billing cycle.

Resources:

- App Store Server API

- App Store Server Notifications

- Reduce involuntary subscriber churn

- Enable Billing Grace Period

### Managing prices

You can price your auto-renewable subscriptions by storefront and choose from 800 price points across all available currencies and price tiers, with an additional 100 higher price points available upon request. After you set a starting price for your auto-renewable subscription, you can schedule one future price change at a time, per territory in App Store Connect.

Price decreases. If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. You don’t have the option to preserve the higher price for existing subscribers. Existing subscribers don’t receive any communications and don’t need to take any action.

Price increases. When you increase the price of an auto-renewable subscription, Apple automatically provides push notifications, email, and in-app messaging to let subscribers know about the upcoming change and how to manage their subscription. Some price increases require subscribers to opt in, while smaller, infrequent price increases can result in notifications without the need to opt in.

If needed, you can temporarily delay the in-app price consent sheet to avoid interrupting someone during a critical moment.

You can keep an unlimited number of active subscribers at their existing price while increasing the price for new subscribers. If you don’t preserve the price for existing subscribers, and they need to consent, they must agree to the new price. If they don’t agree, their subscription expires at the end of their current billing cycle.

If you have several cohorts of subscribers at different prices and want to move all subscribers to the current price, increase the price for those paying closest to the current price first (for example, $2.99 to $3.99), then the next closest, and so on. This ensures that people don’t experience multiple price increases. Before you make any pricing decisions, research your target market’s pricing expectations and weigh the potential impact of raising the price against retaining subscribers.

$3.99 

$2.99 

$1.99 

2022  
2023  
2024    

- New subscribers in 2024 will pay $3.99.

- Subscribers since 2023 continue to pay $2.99.

- Subscribers since 2022 continue to pay $1.99.

Resources:

- Manage pricing for auto-renewable subscriptions

- Manage auto-renewable subscription pricing in App Store Connect

- Delay the price consent sheet

### Measuring performance

View and analyze subscription data to better understand how your subscriptions are performing. Filter data by Plan, Duration, Territory, and more in Analytics in App Store Connect.

Subscriptions dashboard. Get an overview of your subscriptions — including data on active plans, monthly recurring revenue, retention and conversion rates, cancellation reasons, and more. You can use the data on this page to help inform your subscription strategy.

Offers dashboard. Analyze how your subscription offers perform, including introductory offers, promotional offers, and win-back offers, as well as offer codes. For example, if you revise your in-app messaging or change the duration of an offer, you can monitor how these changes impact your performance across the customer lifecycle.

Metrics page. View all of your subscription data in one place, including your total active subscriptions based on their current state: standard price, introductory offers, promotional offers, and billing retry. Use this data to measure your subscriptions’ growth over time. For example, you can group data by Proceeds Rate to understand how many subscriptions earned a higher proceeds rate after one year. Filter or group data by different dimensions, such as Territory, Promotional Offer, Subscription, and more for additional insight.

You can also analyze specific subscription events, including subscription activations, conversions to standard price, reactivations, renewals, and more. Filter data for additional insights. For example, filtering by a specific promotional offer will show you how many times it’s reactivated your lapsed subscriptions. You can use this information to update your promotional offer strategy. View definitions of each subscription event.

Cohorts page. View data related to your subscription retention, as well as data on conversion rates for your introductory and promotional offers. The Subscription Retention view shows the percentage of subscriptions that were renewed for consecutive periods. You can filter this information by a specific subscription, territory, source type, and more to understand which start months have the highest retention and investigate contributing factors to retention — for example, launching new content in a particular month or a seasonal marketing campaign. This can help inform your engagement and retention efforts.

Subscription reports. You can download daily reports containing all of this information plus additional details, such as anonymized start date and days before cancelling.

Resources:

- Sales and Trends essentials

- View subscriptions data

- Download and view reports

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-types/
### App Store Connect Help

App Store Connect / Reference / In-App Purchases and subscriptions / In-App Purchase types 
Filter ⌘K  
Filter ⌘K  

Reference  

# In-App Purchase types

In-App Purchase types refer to the different types of In-App Purchase options available.

Column

Description

Consumable

A product that is used once, after which it becomes depleted and must be purchased again. Example: fish food in a fishing app.

Non-Consumable

A product that is purchased once and does not expire or decrease with use. Example: Race track for a game app.

Auto-Renewable Subscription

A product that allows users to purchase dynamic content for a set period. This type of Subscription renews automatically unless cancelled by the user. Example: Monthly subscriptions for an app offering streaming services. Auto-renewable subscriptions can also support multiseat purchasing, which allows customers to buy multiple seats for a group. Learn how to set purchase options for an auto-renewable subscription.

Non-Renewing Subscription

A product that allows users to purchase a service with a limited duration. The content of this In-App Purchase can be static. This type of Subscription does not renew automatically. Example: One year subscription to a catalog of archived articles.

Related In-App Purchase statuses Create consumable or non-consumable In-App Purchases

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/view-and-edit-in-app-purchase-information/
### App Store Connect Help

App Store Connect / Manage In-App Purchases / View and edit In-App Purchase information 
Filter ⌘K  
Filter ⌘K  

Manage In-App Purchases  

# View and edit In-App Purchase information

You can edit most metadata elements for your In-App Purchases, except for the product ID and purchase type. If your In-App Purchase was never submitted to Apple for review, you can make changes to its metadata. However, if your In-App Purchase was already submitted, some changes require approval by App Review.

Learn how to modify In-App Purchases using the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

Note: 

-  
Developer has read-only access.

-  
It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.

## Add and remove localizations

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, then scroll down to Non-Renewing Subscriptions and click Manage.)

-  
Click the In-App Purchase you want to view or edit.

-  
Under App Store, in the Localization section, click Add Localization or the add button (+).

-  
To delete a localization, hold the pointer over the language listed under App Store Localizations, then click the remove button (—).

-  
Click Delete in the dialog.

### Add or remove an Image

To promote your In-App Purchase on your App Store product page, set up win-back offers or Contingent Pricing, or display your offer codes and payment sheet, you must provide an image. This image represents your In-App Purchase in all countries or regions where your product is available. Your image must meet the following requirements:

-  
JPG or PNG

-  
Dimensions of 1024 x 1024 pixels.

-  
72 dpi, RGB, flattened and no rounded corners.

To add or remove your image:

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, then scroll down to Non-Renewing Subscriptions and click Manage.)

-  
Click the In-App Purchase you want to modify.

-  
Scroll down to the Image section.

-  
To add an image, click Choose File and upload the image. To delete an image, move your pointer over it and click the remove icon (—).

When you're ready, submit your In-App Purchase for review. Your Image must be approved by App Review before it will appear on the App Store.

### Add App Review information

When submitting your In-App Purchase for review, include review notes and a screenshot to help Apple's review process. This information is for Apple’s review only and isn’t displayed on the App Store. You can change it before you submit to App Review, or if your In-App Purchase is rejected.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, then scroll down to Non-Renewing Subscriptions and click Manage.)

-  
Click the In-App Purchase you want to view or edit.

-  
Scroll down to the Review Information section.

-  
Click Choose File to upload your image.

-  
Add information under Review Notes, then click Save.

Related In-App Purchase information

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers/
### App Store Connect Help

App Store Connect / Manage subscriptions / Set up win-back offers 
Filter ⌘K  
Filter ⌘K  

Manage subscriptions  

# Set up win-back offers

If your app offers auto-renewable subscriptions, you have the option to set up win-back offers to encourage lapsed subscribers to re-subscribe on the App Store.

Win-back offers are configured per subscription product, not per subscription group. Customers are only eligible for win-back offers for their most recently lapsed subscription product within each group — so if you want to reach lapsed subscribers across multiple products, create a separate win-back offer for each one.

You can configure offers in App Store Connect to be displayed to eligible customers on your product page and in your app. They may also appear in editorially curated selections and personalized recommendations across the App Store.

App Store Connect allows you to create a maximum of 350 win-back offers per subscription. You can run a maximum of 5 win-back offers per storefront, per subscription at a time. If you have enabled monthly subscriptions with a 12 month commitment you're limited to 5 active offers per storefront for that payment configuration.

Learn more about offers for auto-renewable subscriptions.

Learn about supporting win-back offers in your app.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Set up win-back offers

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions.

-  
Choose the subscription group containing your subscription. Your subscription needs to be approved by App Review before you can create a win-back offer.

-  
Click the subscription, then go to the Subscription Prices section and click the add button (+).

-  
Select Create Win-Back Offer.

-  
Enter a reference name for the offer. Use this reference name to manage the offer in App Store Connect. After you’ve created your offer, the reference name cannot be changed.

-  
Enter an identifier for the offer. This will allow you to identify sales associated with the offer in Sales and Trends reports and in StoreKit transactions. It must not have already been used for another offer in the same subscription group. After you’ve created your offer, you can’t change the offer identifier.

-  
Set the date range for when this offer will be available. The earliest you can schedule your offer to go live is one day after today, and the event must run for a minimum of 3 days. Please note that start dates and times vary by region.

-  
Choose either Normal Priority or High Priority. Indicating an offer is high priority helps the App Store understand which of your offers are your most important business priorities. Along with other offer details, this informs how Apple ranks your offer in placements such as win-back offer sheets, customers' manage subscriptions page, and the App Store if you choose to promote your offer there.

-  
Determine which customers are eligible for the offer, based on how long they were paid subscribers and when their subscriptions ended.

Eligibility Criteria

Definition

Minimum Paid Duration

The minimum time that a customer must have been subscribed to that subscription in order to be eligible for the offer. Choose any value between 1 and 24 months, or 3, 4, and 5 years.

Time Since Last Subscribed

The range of months that must have passed since the customer last had an active subscription. You can choose a minimum value of 1 month and a maximum value of 24 months. For example, selecting a minimum of 5 months and a maximum of 11 months will configure your offer to be shown only to customers who have been lapsed for 5 to 11 months. Both a minimum and maximum value are required.

Wait Between Offers

The required time a customer must wait after a win-back offer ends before redeeming the same offer again. Choose a value between 2 and 24 months. This field is optional.

-  
Choose your country or region availability, then click Next.

App Store Connect informs you if your offer overlaps with any other scheduled offers. Overlap occurs when customers are eligible for more than one offer for the same subscription, based on specified offer dates, eligibility criteria, and country or region availability. If offers overlap, Apple automatically selects and displays one offer to eligible customers based on price, duration, and other factors such as the customer’s paid subscription tenure.

-  
Choose Pay as you go, Pay up front, or Free, then choose the appropriate duration and price. To search from a larger list of price points, click See Additional Prices. Click Next.

-  
App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next. After you’ve created your offer, you can’t change the price.

-  
Make sure the details of your offer are correct, and then click Confirm. After the offer is created, a redemption URL to the offer is generated. The offer will automatically display on the customers' Manage Subscriptions page and within your app once the start date is reached. In order for your offer to appear on the App Store, make sure you have an approved image for your subscription, and have promoted the offer. 

### Promote win-back offers on the App Store

In order for your win-back offer to appear on your app’s product page and in editorially curated selections and personalized recommendations across the App Store, you must promote it. To promote an offer on the App Store, make sure you have an subscription image for your subscription approved by App Review.

The App Store will display your image on a win-back offer sheet alongside your app icon, subscription display name, and description. You may not upload an image that is the same as your app icon, or any of your app screenshots.

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions

-  
Choose the subscription group containing your subscription.

-  
Click the subscription you wish to promote.

-  
Scroll down to the Promote on the App Store section, and click Promote Offer. If you have not yet uploaded an image for your In-App Purchase, you will be prompted to do so before promoting your offer.

-  
Click Promote.

If you choose to promote a win-back offer, it will replace any In-App Purchase promotions in the same storefront.

### Display offers to eligible subscribers

Win-back offers are automatically displayed to eligible customers in their Manage Subscription page on iOS 14.3, iPadOS 14.3, and macOS 14 or later, and within your app on the win-back offer sheet on iOS 18, iPadOS 18, and macOS 15 or later. You can manage how the win-back offer sheet is displayed in your app using StoreKit.

If you choose to promote your win-back offer, it appears on your app’s product page and in editorially curated selections and personalized recommendations across the App Store on macOS 15, iOS 18 and iPadOS 18 and later. (Please note that even if you do not promote your win-back offer, it will still appear in customers’ Manage Subscriptions page and within your app) 

You can also market win-back offers to eligible customers by sharing a redemption URL to your offer with them (such as through an email or website), or merchandise the offer within your app using StoreKit 2 APIs.

To copy your offer's redemption URL to share it with customers:

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions

-  
Choose the subscription group containing your subscription.

-  
Click the subscription, then go to the Redemption URL section and click Copy Link. Make sure you check customers eligibility before you send out the link. Learn more.

### Edit win-back offers

You can edit certain win-back offer details depending on whether the offer is live on the App Store.

Criteria

Before offer is live

After offer is live

Reference Name

Offer Identifier

Country or region availability

Price

Start and end dates

Eligibility criteria

Priority

App Store promotion

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions.

-  
Choose the subscription group containing your subscription.

-  
Click your subscription, then go to the Subscription Prices section and click View all Subscription Pricing.

-  
Click the Win-Back Offers tab.

-  
Click the offer you wish to edit.

-  
Click Edit Offer.

-  
Make your desired changes, and click Save.

### Delete win-back offers

You can delete win-back offers at any time.

-  
From Apps, select your app.

-  
In the sidebar, click Subscriptions.

-  
Choose the subscription group containing your subscription.

-  
Click your subscription, then go to the Subscription Prices section and click View all Subscription Pricing.

-  
Click the Win-Back Offers tab.

-  
Click the offer you wish to edit.

Click Delete Offer. If customers receive a link to a deleted offer, the App Store will display a message stating the offer is no longer available.

Related Implement App Store Offers

