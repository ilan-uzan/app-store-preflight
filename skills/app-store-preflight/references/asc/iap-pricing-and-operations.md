# In-App Purchase pricing, availability, offer codes, keys, notifications and sandbox (App Store Connect Help)
Source: https://developer.apple.com/help/app-store-connect/  
Retrieved: 2026-10-30

## IAPX.1 Set a price for an In-App Purchase

**Source page:** https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase

**Source text (verbatim):**
> In order to offer paid content on the App Store, your membership Account Holder will need to accept the Paid Apps Agreement in the Business section of App Store Connect. If the most recent version of this agreement hasn’t been accepted, you can only offer your app for free.
>
> You’ll need to set pricing for your In-App Purchase before you submit it for review. Choose from up to 800 price points by default, and request to access an additional 100 higher price points (up to $10,000).
>
> You can set a price for the country or region you’re familiar with as the basis for automatically generating prices across the other 174 storefronts and 43 currencies. Automatically generated prices account for foreign exchange rates and certain taxes, and follow the most common pricing convention for each country or region.
>
> Periodically, Apple updates prices in certain regions based on changes in taxes and foreign exchange rates. This is done using publicly available exchange rate information from financial data providers. These automatic price adjustments help ensure that your app’s price across all storefronts stays equalized with your base country or region. Automatic price updates help your global earnings stay consistent, customers aren’t incentivized to seek lower prices on certain storefronts, and pricing mistakes are reduced. Apple will never change the price in your base country or region, and will always notify you in advance of changes on other storefronts.
>
> Alternatively, you can choose to manually manage certain storefronts or you can manually manage them all. Keep in mind that you'll be responsible for staying up to date with taxes and exchange rates in the storefronts you manually manage.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> Learn how to set a price for your In-App Purchases using the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> ## Set a price for an In-App Purchase
>
> - In Apps, select the app you want to view.
> - In the sidebar, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - In the Price Schedule section, click Add Pricing.
> - Select a base country or region. Apple uses this base to provide comparable prices on the other 174 storefronts. As taxes and foreign exchange rates change, prices on the other storefronts will be automatically updated by Apple periodically. You can change this base configuration later at any time.
> - Select a price for your base country or region, then click Next. Initially, the list displays 25 price points that follow the most common pricing convention for each country or region. To view more price points, scroll to the end of the menu and then click See Additional Prices. You can choose from up to 800 price points by default. You can also submit a request to access an additional 100 higher price points.
> - A screen appears with comparable prices for all other storefronts. If you’d like Apple to automatically adjust prices for you, don’t make any changes to this pricing. Alternatively, you can choose different prices for individual countries or regions. If you select your own prices, Apple won’t adjust your pricing on those storefronts in the future.
> - Click Next.
> - Review your upcoming price changes, then click Confirm.

**Applies to:** Apps that offer In-App Purchases (including non-renewing subscriptions, which are managed under Subscriptions > Non-Renewing Subscriptions)

- **[IAPX-30]** Has the Account Holder accepted the most recent Paid Apps Agreement in the Business section of App Store Connect (otherwise the app can only be offered for free)?
  - quote: "your membership Account Holder will need to accept the Paid Apps Agreement in the Business section of App Store Connect. If the most recent version of this agreement hasn’t been accepted, you can only offer your app for free."
  - surface: asc
  - verify: App Store Connect > Business: confirm the Paid Apps Agreement shows as active (not pending acceptance of a newer version).
  - fix: manual — requires developer decision/legal/business action (the Account Holder must accept the latest Paid Apps Agreement in Business).
- **[IAPX-01]** Does every In-App Purchase being submitted have pricing set (a base country or region and price in its Price Schedule)?
  - quote: "You’ll need to set pricing for your In-App Purchase before you submit it for review."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > In-App Purchases (non-renewing subscriptions: Subscriptions > Non-Renewing Subscriptions > Manage) > each In-App Purchase > Price Schedule section: a base country or region and price are listed (the section does not only offer Add Pricing).
  - fix: In the Price Schedule section click Add Pricing, select a base country or region and a price, click Next, review the comparable storefront prices, click Next, then Confirm.

## IAPX.2 Edit base country or region for your In-App Purchase

**Source page:** https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase

**Source text (verbatim):**
> You can set the base country or region of each In-App Purchase separately from the app. Once you edit the base country or region or update the pricing of an In-App Purchase, it'll no longer inherit changes you make to the app’s base country or region.
>
> To edit the base country or region of all your In-App Purchases at once, edit your app’s base country or region.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions. Then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - In the Price Schedule section, under Base Country or Region, click Edit.
> - Changing your base country or region deletes any scheduled price changes. Review any scheduled price changes, select the box indicating you understand they’ll be permanently deleted, and then click Edit.
> - Select a base country or region. Apple uses this base to provide comparable prices on the other 174 storefronts. As taxes and foreign exchange rates change, prices on the other storefronts will be automatically updated by Apple periodically. You can change this base configuration later at any time.
> - Select a price for your base country or region, then click Next. Initially, the list displays 25 price points that follow the most common pricing convention for each country or region. To view more price points, scroll to the end of the menu and then click See Additional Prices. You can choose from up to 800 price points by default. You may also submit a request to access an additional 100 higher price points.
> - A screen appears with comparable prices for all other countries or regions based on taxes and foreign exchange rates. If you’d like Apple to automatically adjust prices for you, don’t make any changes to this pricing. Alternatively, you can choose different prices for individual countries or regions. If you select your own prices, Apple won’t adjust your pricing on those storefronts in the future.
> - Click Next.
> - Click Review your upcoming changes, then click Confirm. .
>
> New pricing will go into effect immediately.

**Applies to:** Apps that offer In-App Purchases (including non-renewing subscriptions, which are managed under Subscriptions > Non-Renewing Subscriptions)
**Requires:** iap, subscriptions

## IAPX.3 Schedule price changes for In-App Purchases

**Source page:** https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/schedule-price-changes-for-in-app-purchases

**Source text (verbatim):**
> You can update your In-App Purchase pricing at any time in App Store Connect. Price changes can have definite start and end dates, or they can be permanent changes with no end. For example, you can set a promotional price for a month, then return to the regular price.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> | Property | Description |
> |---|---|
> | Global Price Change | You change the price of your app in your base country or region in App Store Connect. Apple provides comparable prices for all other countries or regions, and may adjust some prices on your behalf in the future to account for changes in taxes and foreign exchange rates. Pricing in your base country or region won't be affected. |
> | Temporary Price Change | You select the start and end dates for a temporary price change in certain countries or regions. During this time, Apple won’t adjust prices on your behalf in these countries or regions. |
> | Custom Price Change | You manually manage prices for some or all countries or regions. Apple won't adjust prices on your behalf in these countries or regions. |
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> ## Schedule a global price change
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions. Then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - Next to Price Schedule, click the add button (+).
> - Select Global Price Change, then click Next.
> - Select an effective date. Effective dates can be scheduled from today up to the end of the next calendar year.
> - Select a price for your base country or region. Apple uses this base to provide comparable prices on the other 174 storefronts. As taxes and foreign exchange rates change, prices on the other storefronts will be automatically updated by Apple periodically. the prices for each country or region, then click Confirm.
> - Review the prices for each country or region, then click Confirm.
>
> ### Schedule a temporary price change
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions. Then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - Next to Price Schedule, click the add button (+).
> - Select Temporary Price Change, then click Next.
> - Select start and end dates, then click Next. Start dates can be scheduled from today up to the end of the next calendar year. The longest length for a temporary price change is one year.
> - Select the App Store countries or regions where you'd like the price change to go into effect, then click Next.
> - Select a country or region and a price, then click Next. Apple will use this to provide comparable prices across the selected countires or regions.
> - Review the pricing that Apple suggested for each country or region. Make any necessary changes, then click Next.
>
> If your temporary price change includes your base country or region, keep in mind that Apple won’t make any automatic adjustments to your In-App Purchase pricing in all 175 countries or regions during the start and end dates you’ve selected. If you’d like to add more countries or regions, click Back or Cancel. Otherwise, click Next.
>
> - Review your temporary price change, then click Confirm.
>
> ### Schedule a custom price change (manually manage prices in specific countries or regions)
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions. Then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - Next to Price Schedule, click the add button (+).
> - Select Custom Price Change, then click Next.
> - Select an effective date. Effective dates can be scheduled from today up to the end of the next calendar year.
> - Choose the first option, “Manually manage prices in specific countries or regions”.
> - Select the App Store countries or regions where you'd like the price change to go into effect, then click Next. Your base country or region can't be selected.
> - Select a country or region and a price, then click Next. Apple will use this to provide comparable prices across the other storefronts you selected.
> - Review the prices for each country or region. Make any necessary changes, then click Next.
> - Review your upcoming changes, then click Confirm.
>
> Once the change goes into effect, Apple will no longer update your In-App Purchase’s pricing to account for changes in taxes or foreign exchange rates in the countries or regions you selected. Ensure that you’ve read and understand the impact of Apple’s pricing capabilities.
>
> ### Schedule a custom price change (manually manage prices in all 175 countries or regions)
>
> If you plan a Custom Price Change that includes your base country or region in App Store Connect, Apple will no longer automatically update prices in any of the 175 App Store countries or regions.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions. Then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - Next to Price Schedule, click the add button (+).
> - Select Custom Price Change, then click Next.
> - Select an effective date. Effective dates can be scheduled from today up to the end of the next calendar year.
> - Choose the second option, “Manually manage prices in all countries or regions,” then click Next. This price must be selected for you to manually manage prices in all 175 countries or regions, and you can keep the price as is or update it.
> - Select a price for your base country or region. This price must be selected for you to manually manage prices in all 175 countries or regions, and you can keep the price as is or update it.
> - Review the current pricing for any countries or regions you didn’t select a price for, then click Next.
> - Review all of your upcoming changes, then click Confirm.
>
> Once the change goes into effect, Apple won’t update pricing to account for changes in taxes or foreign exchange rates. If you do want Apple to automatically adjust prices for you, you need to create a Global Price Change. Ensure you’ve read and understand the impact of Apple’s pricing capabilities.
>
> ### View or edit upcoming price changes
>
> You may view or make changes to your upcoming price changes in App Store Connect at any time.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - Under Price Schedule, view your upcoming changes and their start and end dates.
>
> The price schedule indicates whether Apple may make adjustments to pricing in certain countries or regions due to changes in taxes or foreign exchange rates. Countries where pricing won’t be adjusted display Manually Adjusted. When Apple automatically adjusts prices, you can locate the upcoming scheduled price details in the Price Schedule. Upcoming Apple reprices are marked Foreign Exchange or Tax Rate Adjustment.
>
> - You can delete scheduled price changes by hovering over the red delete button (-). In certain cases, such as upcoming tax or foreign exchange rate adjustments, or when a manually adjusted price is starting or reverting, you may not be able to remove an upcoming price change. Click the date of the price change for details.

**Applies to:** Apps that offer In-App Purchases (including non-renewing subscriptions, which are managed under Subscriptions > Non-Renewing Subscriptions)
**Requires:** iap, subscriptions

## IAPX.4 Set availability for In-App Purchases

**Source page:** https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases

**Source text (verbatim):**
> You have the option to make your In-App Purchase available in any of 175 countries or regions where the App Store is offered. A customer’s Apple Account country or region setting determines which storefront they can purchase content from the App Store. For example, an account set to Japan can only purchase apps from the App Store in Japan.
>
> Learn how to set availability for In-App Purchases with the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> ## Set availability for In-App Purchases
>
> - In Apps, select the app you want to view.
> - In the sidebar, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions. Then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - In the Availability section, click Set Up Availability.
> - Select the countries or regions where you want to make your In-App Purchase available. To submit your In-App Purchase for review without releasing it on the App Store, select “Remove from sale.”
> - Click Done.
>
> Keep in mind that even if you set availability for an In-App Purchase, it may not be available for purchase. Monitor the In-App Purchase statuses to understand if action is needed from you, such as completing missing metadata, or if your In-App Purchase has been approved by App Review.

**Applies to:** Apps that offer In-App Purchases (including non-renewing subscriptions, which are managed under Subscriptions > Non-Renewing Subscriptions)
**Requires:** iap, subscriptions

- **[IAPX-02]** For each In-App Purchase whose availability has been set, does its In-App Purchase status show no action needed from the developer (such as completing missing metadata)?
  - quote: "Monitor the In-App Purchase statuses to understand if action is needed from you, such as completing missing metadata"
  - surface: asc
  - verify: App Store Connect > Apps > [app] > In-App Purchases > each In-App Purchase: the Availability section lists selected countries or regions (not only a Set Up Availability button), and the status shown for the product does not indicate missing metadata or other required action (see the In-App Purchase statuses reference, IAP.STATUS).
  - fix: In the Availability section click Set Up Availability, select the countries or regions, click Done; complete any missing metadata indicated by the status.
- **[IAPX-03]** If an In-App Purchase must go through App Review but should not be released on the App Store yet, is its availability set to “Remove from sale”?
  - quote: "To submit your In-App Purchase for review without releasing it on the App Store, select “Remove from sale.”"
  - surface: asc
  - verify: App Store Connect > Apps > [app] > In-App Purchases > [product] > Availability: confirm “Remove from sale” is selected for products that are intended to be reviewed but not yet sold.
  - fix: In Availability click Set Up Availability (or Edit) and select “Remove from sale,” then click Done.

## IAPX.5 Edit In-App Purchase availability and removing an In-App Purchase from sale

**Source page:** https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions. Then scroll down to the Non-Renewing Subscriptions section and click Manage.)
> - Click the In-App Purchase you want to edit.
> - Under Availability, click Edit.
> - In the dialog that appears, change your In-App Purchase’s availability by selecting or deselecting your desired countries or regions.
>
> These changes will go into effect immediately.
>
> When deselecting countries or regions where your In-App Purchase is available, consider the impact on users and any communications you might need to provide.
>
> Before removing your In-App Purchase from sale, take the following steps to help ensure a smooth experience:
>
> - Announce your intention to remove the In-App Purchase from sale and stop merchandising it within your app at least 31 days before removal and remove them from sale within App Store Connect. This lets people use up any consumable In-App Purchase products they purchased. You can leverage your own communication channels such as email, websites, and in-app messaging. If you’re unable to provide sufficient notice to users, contact us.
> - End any promotions of the In-App Purchases to discourage purchases.
> - Notify Apple of your intention to remove an In-App Purchase from sale. Apple reserves the right to offer refunds for unfulfilled In-App Purchases.

**Applies to:** Apps deselecting countries or regions for, or removing from sale, an In-App Purchase
**Requires:** iap, subscriptions

- **[IAPX-04]** If an In-App Purchase is being removed from sale, was the removal announced and was in-app merchandising of it stopped at least 31 days before removal?
  - quote: "Announce your intention to remove the In-App Purchase from sale and stop merchandising it within your app at least 31 days before removal"
  - surface: manual
  - verify: Ask for the dated announcement (email, website, in-app messaging) and the planned removal date; in the Xcode project search store/paywall code for the product identifier being retired and confirm the build no longer merchandises it, at least 31 days before the removal date.
  - fix: manual — requires developer decision/legal/business action (announce removal and stop merchandising at least 31 days ahead, or contact Apple if sufficient notice cannot be given).
- **[IAPX-05]** If an In-App Purchase is being removed from sale, have all promotions of it been ended?
  - quote: "End any promotions of the In-App Purchases to discourage purchases."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > In-App Purchases > [product]: confirm it is no longer promoted on the App Store (App Store Image section / Promoted checkbox); ask the developer to confirm any other promotions of it have ended.
  - fix: Unpromote the In-App Purchase, deactivate its offer codes, and end other promotions before removal.
- **[IAPX-06]** If an In-App Purchase is being removed from sale, has Apple been notified of the intention to remove it?
  - quote: "Notify Apple of your intention to remove an In-App Purchase from sale."
  - surface: manual
  - verify: Ask the developer for the record of the notification sent to Apple (Contact Us) for the product being removed.
  - fix: manual — requires developer decision/legal/business action (notify Apple before removing the In-App Purchase from sale).

## IAPX.6 Manage pricing for auto-renewable subscriptions — overview and starting price

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions

**Source text (verbatim):**
> Auto-renewable subscriptions can be priced by App Store country or region (also known as storefronts.) You can choose from 800 price points in each currency, with the option for the Account Holder to submit a request for additional higher price points.
>
> After you set a starting price for your auto-renewable subscription, you can schedule one future price change at a time, per country or region, per billing plan type. If you schedule a second price change when you already have a change scheduled, the first scheduled change will be overwritten. Additionally, if you schedule a price increase before an earlier (previously implemented) price increase has been completed across all of your active subscribers, you may see some subscriptions renew again at their original price when there is not enough time to provide the customers with the required notice or request for consent detailed in the Price Increase section below. You also have the option to preserve prices for existing subscribers.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> Learn how to configure auto-renewable subscription pricing with the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> ## Set a starting price for your auto-renewable subscription
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Subscriptions.
> - Click the subscription group name.
> - Click the subscription reference name.
> - Scroll down to the Subscription Prices section and click Add Subscription Price.
> - Choose a country or region and price, then click Next. To search from a larger list of price points, click See Additional Prices.
> - App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.
> - Make sure your subscription’s starting price is correct and click Confirm.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

## IAPX.7 Decrease the price of an auto-renewable subscription

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions

**Source text (verbatim):**
> If you decrease the price of your auto-renewable subscription, existing subscriptions will automatically renew at the lower price. You don’t have the option to preserve the higher price for existing subscribers.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Subscriptions.
> - Click the subscription group name.
> - Click the subscription reference name.
> - Scroll down to the Subscription Prices section and click the add button (+).
> - Select the storefronts where you want to edit pricing.
> - Choose a start date, country or region, and price, then click Next. To search from a larger list of price points, click See Additional Prices.
> - App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.
> - Make sure the details of your price decrease are correct and click Confirm.
>
> You can schedule one future price change at a time, per storefront, per billing plan type. If you schedule a second price change when you already have a change scheduled, the first scheduled change will be overwritten.
>
> - Once a price decrease goes into effect, it can’t be reversed. However, you can schedule a price increase later.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

## IAPX.8 Increase the price of an auto-renewable subscription (consent and notice rules)

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions

**Source text (verbatim):**
> Increases in auto-renewable subscription prices result in either a notice to active subscribers or a request for consent, based on certain criteria below. Subscribers on introductory or promotional price subscriptions, including free trials and paid offers, will renew for at least one more renewal period at the price that was displayed when they subscribed, to ensure their notice or request for consent for the new price is sent at least 30 days in advance. If a subscriber doesn't consent before the first renewal at the higher price, their subscription will expire at the end of the last renewal cycle at the former price. If your subscription has multiseat purchasing enabled, additional criteria apply. Visit the FAQs below.
>
> ### Consent needed
>
> If any of the following applies, subscribers must consent to the price increase before their next renewal date in order for the subscription to renew. * Apple will automatically contact subscribers by email or push notification to request consent.
>
> - The subscriber is located in a region that requires consent for any price changes.
> - The price increase is more than 50% of the current price and the difference in price exceeds approximately US$5 per period for non-annual subscriptions, or US$50 per year for annual subscriptions. (International equivalents for prices not in USD are based on current exchange rates with specific thresholds that are subject to change based on changes in taxes or foreign exchange rates.) View a list of thresholds per storefront.
> - The subscriber experienced a price increase for that subscription within the past 12 months.
>
> The timing of price consent requests from Apple depends on the length of the subscription. If a price increase occurs within the minimum required notice period (7 days for weekly subscriptions, 27 days for 1 month subscriptions, and 30 days for subscription durations longer than 1 month), subscribers will renew at their existing price for one more billing period and will receive price consent requests from Apple before the end of their next billing period.
>
> | Subscription duration | First email notification (email, push, in-app messaging) |
> |---|---|
> | 2 month, 3 month, and 6 month, and annual subscriptions | 60 days before renewal date |
> | Monthly subscriptions | 27 days before renewal date |
> | Weekly subscriptions | 7 days before renewal date |
>
> If a subscriber doesn’t agree to the new price or takes no action, Apple will continue to request consent approximately weekly through email, push notifications, and in-app messaging until their subscription expires at the end of their current billing cycle. Learn how StoreKit displays price increase consent messages in your app.
>
> * If you increase the price of an auto-renewable subscription in India, subscribers who have enabled UPI AutoPay must consent to the new price and have a sufficient payment balance associated with their Apple Account, or they’ll go into the billing retry state at the end of their current billing period. Apple will notify these subscribers as part of the price increase notice, but you may also wish to notify subscribers separately. Subscribers who don’t have a sufficient Apple Account balance or who wish to continue paying with UPI AutoPay must repurchase the subscription at the new price. Learn more.
>
> * For users converting from trials or offers in South Korea, Apple will collect consent via email, in-app sheets, or push notifications. The timing and frequency of these communications may differ from those shown for standard subscription price increases. Learn about consent for subscription offer conversions.
>
> ### Consent not needed
>
> If none of the criteria apply, Apple will automatically notify subscribers of the price increase with no additional request for consent. After the new price goes into effect, notifications are sent via email and push notifications — if enabled by the subscriber — 27 or 7 days before the next renewal date. On iOS 13.4 or later, Apple will also notify subscribers via in-app messaging. If a price increase occurs within the minimum required notice period, subscribers will renew at their existing price for one more billing period and will be notified before the end of their next billing period.
>
> Note: A new price increase can overwrite a previous one that a customer was notified about but hasn't yet renewed at. In that case, the customer renews at their existing price for one more billing period.
>
> Price changes apply only to active subscribers. If a subscription recovers during billing retry or the grace period, it renews at the existing price for one more billing period. However, if a subscriber actively renews or purchases the subscription directly, the new price applies immediately. Subscribers receive notice of a price change 27 days before the renewal date, and the subscription renews at the new price on the next renewal date. Subscribers who aren't going to renew don't receive a notification. A subscriber in billing retry who repurchases the current plan, or an offer for it, can consent to the higher price and is charged immediately.
>
> | First email | First in-app messaging | Push notification |
> |---|---|---|
> | 27 days before renewal date.<br>Note: Weekly subscriptions renew at the increased price on the fourth consecutive renewal. | First app launch after entering notice period. | 7 days before renewal date, if in-app messaging wasn't viewed. |
>
> Note: Price changes only apply to active subscribers. If a subscription is recovered in the billing retry or grace period state, it will renew at the existing price for one more billing period. 27 days before the renewal date, the subscriber receives notice of the price change, and the subscription renews at the next renewal date at the new price. Subscribers won't receive a notification if the subscription isn't going to renew. If a user in billing retry attempts to restart service by repurchasing the subscription or an offer for the current plan, they can consent to the higher price and will be charged immediately.
>
> To schedule a price increase:
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Subscriptions.
> - Click an auto-renewable subscription, go to the Subscription Prices section, and click the add button (+).
> - Click Plan Subscription Price Change, then select the countries or regions where you want to edit pricing.
> - Choose a start date, country or region, and price, then click Next. To search from a larger list of 800 price points, click See Additional Prices.
>
> App Store Connect will determine the soonest your price change can be scheduled for based on timezones for your desired date (generally 1 to 2 days in advance.) The time of day your price change goes into effect will vary by region. Ensure you're scheduling your price changes with enough time in advance.
>
> - App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.
> - Choose an option for subscribers paying the current price shown in App Store Connect:
> - A: Keep the current price for existing subscribers. Anyone who subscribed before the start date of this price change won’t be affected. Subscribers whose subscription expires can resubscribe at the preserved price within 60 days of expiration.
> - B: Apply the price change to existing subscribers who are paying the price of your subscription currently displayed on the App Store. App Store Connect will provide an indication if consent is required (or if they'll simply be notified) for each country or region. If you have customer groups that have had their prices preserved and your change is scheduled for the future, keep in mind that circumstances may change and consent will be required based on the conditions of the customer at the time of the increase. you're responsible for ensuring you understand when consent will be required.
> - Click Next.
> - View the list of planned price changes.
> - If all of the information is correct, click Confirm.
>
> Once a price increase goes into effect, it can’t be reversed.

**Applies to:** Apps that increase the price of an auto-renewable subscription
**Requires:** subscriptions

- **[IAPX-07]** If a scheduled price increase applies to existing subscribers, has the developer reviewed, per country or region, whether subscribers will need to consent or will only be notified?
  - quote: "you're responsible for ensuring you understand when consent will be required."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Subscriptions > [subscription] > Subscription Prices > View all Subscription Pricing: review each planned price change and the consent/notify indication App Store Connect shows per country or region; compare with the thresholds in IAPX.12.
  - fix: manual — requires developer decision/legal/business action (decide whether to keep the current price for existing subscribers or apply the increase, knowing where consent is required).

## IAPX.9 Un-preserve prices for subscribers

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click Subscriptions.
> - Click the subscription group name.
> - Click the subscription reference name.
> - Scroll down to the Subscription Pricing section and click View all Subscription Pricing.
> - Click Starting Price.
> - Click Edit Price.
> - App Store Connect displays the countries or regions where subscribers currently pay a lower price
> - Select the countries or regions where you want to increase the price. Click Next.
> - Click Confirm. Any changes you make can’t be reversed.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

## IAPX.10 View or modify your planned price changes

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click Subscriptions.
> - Click the subscription name, go to the Subscription Prices section, then click View all Subscription Pricing.
> - View your planned price changes.
>
> You can download a list of prices customers are currently paying for your auto-renewable subscriptions, as well as a list of upcoming prices. Click Export as CSV.
>
> - To cancel a scheduled price change, move your pointer over the right side of the price change row until the delete button (—) appears. Click the delete button.
>
> Note: In certain cases, such as upcoming tax or foreign exchange rate adjustments, or when a manually adjusted price is starting or reverting, you may not be able to remove an upcoming price change.
>
> - In the dialog that appears, click Delete.
>
> Click the date to view the set or planned price. If you’ve previously preserved pricing for existing subscribers, the current prices paid by these subscribers and the start date of the prices will also appear.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

## IAPX.11 Auto-renewable subscription pricing FAQs (foreign exchange, tax, multiseat)

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions

**Source text (verbatim):**
> ### How will changes to foreign exchange rates and tax adjustments affect auto-renewable subscription pricing?
>
> Apple will not make price adjustments on your auto-renewable subscription products. Retail price changes initiated by Apple due to tax changes and significant foreign exchange rate movements will exclude auto-renewable subscriptions. For any value-added tax (VAT) rate changes, your proceeds and Apple’s commission will be calculated after the deduction of VAT, which means that your proceeds will change. You can choose to pass any changes caused by taxation or foreign exchange onto your subscribers by adjusting the price for your subscription.
>
> ### How do price increases work for multiseat purchases?
>
> For multiseat purchases, Apple evaluates the price of the first seat and the group purchaser's total price, meaning the combined price of all seats, separately. The first seat follows the same criteria described in Consent needed above. Beyond the first seat, consent is required if the group purchaser's total price increases by more than 50%, or if they're located in a country or region that requires consent for any price increase (Visit Auto-renewable subscription price increase thresholds). If none of these criteria apply, Apple notifies the group purchaser of their new total price with no request for consent, on the same timing shown above. If the purchaser doesn't consent before the first renewal at the higher price, the entire subscription expires at the end of the last renewal cycle at the former price, including all seats.
>
> Changes to your pricing tiers only count as a price increase if they increase what the purchaser pays. If you add, remove, merge, or adjust tiers and the group purchaser's total price stays the same or decreases, Apple notifies them of the change but doesn't request consent, including in countries or regions that require consent for any price increase. Group purchasers who add seats while an increase is scheduled buy those seats at the new price and see their new total before purchasing. If the increase requires consent, completing that purchase counts as consent.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

## IAPX.12 Auto-renewable subscription price increase thresholds

**Source page:** https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-price-increase-thresholds

**Source text (verbatim):**
> Increases in auto-renewable subscription prices that exceed the below thresholds in each App Store country or region result in a request for subscribers to consent to the new price.
>
> Whether the threshold is exceeded for a subscriber and consent is required depends on whether the threshold is exceeded when the renewal occurs. These thresholds are subject to change based on changes in tax or foreign exchange rates. Learn more about managing auto-renewable subscription prices.
>
> | ISO code | Country or region | Currency | Non-annual subscriptions | Annual subscriptions |
> |---|---|---|---|---|
> | AFG | Afghanistan | USD | 5 | 50 |
> | ALB | Albania | USD | 6 | 60 |
> | DZA | Algeria | USD | 5 | 50 |
> | AGO | Angola | USD | 5 | 50 |
> | AIA | Anguilla | USD | 5 | 50 |
> | ATG | Antigua and Barbuda | USD | 5 | 50 |
> | ARG | Argentina | USD | 5 | 50 |
> | ARM | Armenia | USD | 6 | 60 |
> | AUS | Australia | AUD | 8 | 80 |
> | AUT | Austria | EUR | Consent required | Consent required |
> | AZE | Azerbaijan | USD | 6 | 60 |
> | BHS | Bahamas | USD | 5 | 50 |
> | BHR | Bahrain | USD | 5 | 50 |
> | BRB | Barbados | USD | 6 | 60 |
> | BLR | Belarus | USD | 6 | 60 |
> | BEL | Belgium | EUR | 5 | 50 |
> | BLZ | Belize | USD | 5 | 50 |
> | BEN | Benin | USD | 6 | 60 |
> | BMU | Bermuda | USD | 5 | 50 |
> | BTN | Bhutan | USD | 5 | 50 |
> | BOL | Bolivia | USD | 5 | 50 |
> | BIH | Bosnia and Herzegovina | EUR | 5 | 50 |
> | BWA | Botswana | USD | 5 | 50 |
> | BRA | Brazil | BRL | 40 | 400 |
> | VGB | British Virgin Islands | USD | 5 | 50 |
> | BRN | Brunei | USD | 5 | 50 |
> | BGR | Bulgaria | EUR | 5 | 50 |
> | BFA | Burkina Faso | USD | 5 | 50 |
> | KHM | Cambodia | USD | 5 | 50 |
> | CMR | Cameroon | USD | 6 | 60 |
> | CAN | Canada | CAD | 7 | 70 |
> | CPV | Cape Verde | USD | 5 | 50 |
> | CYM | Cayman Islands | USD | 5 | 50 |
> | TCD | Chad | USD | 5 | 50 |
> | CHL | Chile | CLP | 7,000 | 70,000 |
> | CHN | China mainland | CNY | 40 | 400 |
> | COL | Colombia | COP | 25,000 | 250,000 |
> | COD | Congo, Democratic Republic of the | USD | 5 | 50 |
> | COG | Congo, Republic of the | USD | 5 | 50 |
> | CRI | Costa Rica | USD | 5 | 50 |
> | CIV | Cote d’Ivoire | USD | 6 | 60 |
> | HRV | Croatia | EUR | 5 | 50 |
> | CYP | Cyprus | EUR | 5 | 50 |
> | CZE | Czechia | CZK | 150 | 1,500 |
> | DNK | Denmark | DKK | 45 | 450 |
> | DMA | Dominica | USD | 5 | 50 |
> | DOM | Dominican Republic | USD | 5 | 50 |
> | ECU | Ecuador | USD | 5 | 50 |
> | EGY | Egypt | EGP | 400 | 4,000 |
> | SLV | El Salvador | USD | 5 | 50 |
> | EST | Estonia | EUR | 5 | 50 |
> | FJI | Fiji | USD | 5 | 50 |
> | FIN | Finland | EUR | 5 | 50 |
> | FRA | France | EUR | 5 | 50 |
> | GAB | Gabon | USD | 5 | 50 |
> | GM | Gambia | USD | 5 | 50 |
> | GEO | Georgia | USD | 6 | 60 |
> | DEU | Germany | EUR | Consent required | Consent required |
> | GHA | Ghana | USD | 6 | 60 |
> | GRC | Greece | EUR | 5 | 50 |
> | GRD | Grenada | USD | 5 | 50 |
> | GTM | Guatemala | USD | 5 | 50 |
> | GNB | Guinea-Bissau | USD | 5 | 50 |
> | GUY | Guyana | USD | 5 | 50 |
> | HND | Honduras | USD | 5 | 50 |
> | HKG | Hong Kong | HKD | 40 | 400 |
> | HUN | Hungary | HUF | 2,500 | 25,000 |
> | ISL | Iceland | EUR | 5 | 50 |
> | IND | India | INR | 500 | 5,000 |
> | IDN | Indonesia | IDR | 100,000 | 1,000,000 |
> | IRQ | Iraq | USD | 5 | 50 |
> | IRL | Ireland | EUR | 5 | 50 |
> | ISR | Israel | ILS | 20 | 200 |
> | ITA | Italy | EUR | 5 | 50 |
> | JAM | Jamaica | USD | 5 | 50 |
> | JPN | Japan | JPY | 800 | 8,000 |
> | JOR | Jordan | USD | 5 | 50 |
> | KAZ | Kazakhstan | KZT | 3,000 | 30,000 |
> | KEN | Kenya | USD | 6 | 60 |
> | XKS | Kosovo | EUR | 5 | 50 |
> | KWT | Kuwait | USD | 5 | 50 |
> | KGZ | Kyrgyzstan | USD | 5 | 50 |
> | LAO | Laos | USD | 5 | 50 |
> | LVA | Latvia | EUR | 5 | 50 |
> | LBN | Lebanon | USD | 5 | 50 |
> | LBR | Liberia | USD | 5 | 50 |
> | LBY | Libya | USD | 5 | 50 |
> | LTU | Lithuania | EUR | 5 | 50 |
> | LUX | Luxembourg | EUR | 5 | 50 |
> | MAC | Macau | USD | 5 | 50 |
> | MDG | Madagascar | USD | 5 | 50 |
> | MWI | Malawi | USD | 5 | 50 |
> | MYS | Malaysia | MYR | 25 | 250 |
> | MDV | Maldives | USD | 5 | 50 |
> | MLI | Mali | USD | 5 | 50 |
> | MLT | Malta | EUR | 5 | 50 |
> | MRT | Mauritania | USD | 5 | 50 |
> | MUS | Mauritius | USD | 5 | 50 |
> | MEX | Mexico | MXN | 150 | 1,500 |
> | FSM | Micronesia | USD | 5 | 50 |
> | MDA | Moldova | USD | 6 | 60 |
> | MNG | Mongolia | USD | 5 | 50 |
> | MNE | Montenegro | EUR | 5 | 50 |
> | MSR | Montserrat | USD | 5 | 50 |
> | MAR | Morocco | USD | 5 | 50 |
> | MOZ | Mozambique | USD | 5 | 50 |
> | MMR | Myanmar | USD | 5 | 50 |
> | NAM | Namibia | USD | 5 | 50 |
> | NRU | Nauru | USD | 5 | 50 |
> | NPL | Nepal | USD | 6 | 60 |
> | NLD | Netherlands | EUR | 5 | 50 |
> | NZL | New Zealand | NZD | 10 | 100 |
> | NIC | Nicaragua | USD | 5 | 50 |
> | NER | Niger | USD | 5 | 50 |
> | NGA | Nigeria | NGN | 12,000 | 120,000 |
> | MKD | North Macedonia | USD | 5 | 50 |
> | NOR | Norway | NOK | 60 | 600 |
> | OMN | Oman | USD | 5 | 50 |
> | PAK | Pakistan | PKR | 1,200 | 12,000 |
> | PLW | Palau | USD | 5 | 50 |
> | PAN | Panama | USD | 5 | 50 |
> | ONG | Papua New Guinea | USD | 5 | 50 |
> | PRY | Paraguay | USD | 5 | 50 |
> | PER | Peru | PEN | 25 | 250 |
> | PHL | Philippines | PHP | 300 | 3,000 |
> | POL | Poland | PLN | Consent required | Consent required |
> | PRT | Portugal | EUR | 5 | 50 |
> | QAT | Qatar | QAR | 20 | 200 |
> | KOR | Republic of Korea | KRW | Consent required | Consent required |
> | ROU | Romania | RON | 30 | 300 |
> | RUS | Russia | RUB | 600 | 6,000 |
> | RWA | Rwanda | USD | 5 | 50 |
> | STP | Sao Tome and Principe | USD | 5 | 50 |
> | SAU | Saudi Arabia | SAR | 20 | 200 |
> | SEN | Senegal | USD | 6 | 60 |
> | SRB | Serbia | EUR | 5 | 50 |
> | SYC | Seychelles | USD | 5 | 50 |
> | SLE | Sierra Leone | USD | 5 | 50 |
> | SGP | Singapore | SGD | 7 | 70 |
> | SVK | Slovakia | EUR | 5 | 50 |
> | SVN | Slovenia | EUR | 5 | 50 |
> | SLB | Solomon Islands | USD | 5 | 50 |
> | ZAF | South Africa | ZAR | 100 | 1,000 |
> | ESP | Spain | EUR | 5 | 50 |
> | LKA | Sri Lanka | USD | 5 | 50 |
> | KNA | St. Kitts and Nevis | USD | 5 | 50 |
> | LCA | St. Lucia | USD | 5 | 50 |
> | VCT | St. Vincent and the Grenadines | USD | 5 | 50 |
> | SUR | Suriname | USD | 5 | 50 |
> | SWZ | Swaziland | USD | 5 | 50 |
> | SWE | Sweden | SEK | 60 | 600 |
> | CHE | Switzerland | CHF | 5 | 50 |
> | TWN | Taiwan | TWD | 200 | 2,000 |
> | TJK | Tajikistan | USD | 6 | 60 |
> | TZA | Tanzania | TZS | 18,000 | 180,000 |
> | THA | Thailand | THB | 200 | 2,000 |
> | TON | Tonga | USD | 5 | 50 |
> | TTO | Trinidad and Tobago | USD | 5 | 50 |
> | TUN | Tunisia | USD | 5 | 50 |
> | TKM | Turkmenistan | USD | 5 | 50 |
> | TCA | Turks and Caicos Islands | USD | 5 | 50 |
> | TUR | Türkiye | TRY | 300 | 3,000 |
> | UGA | Uganda | USD | 6 | 60 |
> | UKR | Ukraine | USD | 6 | 60 |
> | ARE | United Arab Emirates | AED | 20 | 200 |
> | GBR | United Kingdom | GBP | 5 | 50 |
> | USA | United States | USD | 5 | 50 |
> | URY | Uruguay | USD | 5 | 50 |
> | UZB | Uzbekistan | USD | 6 | 60 |
> | VUT | Vanuatu | USD | 5 | 50 |
> | VEN | Venezuela | USD | 5 | 50 |
> | VNM | Vietnam | VND | 130,000 | 1,300,000 |
> | YEM | Yemen | USD | 5 | 50 |
> | ZMB | Zambia | USD | 6 | 60 |
> | ZWE | Zimbabwe | USD | 6 | 60 |

**Applies to:** Apps that increase the price of an auto-renewable subscription
**Requires:** subscriptions

## IAPX.13 Set availability for an auto-renewable subscription

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription

**Source text (verbatim):**
> You have the option to make your auto-renewable subscription available in any of 175 countries or regions where the App Store is offered. A customer’s Apple Account country or region setting determines which storefront they can purchase auto-renewable subscriptions from. For example, an account set to Japan can only purchase content from the App Store in Japan.
>
> Keep in mind that even if you set availability for a subscription, it may not be available for purchase. Monitor the In-App Purchase statuses to understand if action is needed from you, such as completing missing metadata, or if your In-App Purchase has been approved by App Review.
>
> Learn how to set availability for auto-renewable subscriptions with the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> ## Set availability for a subscription
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Subscriptions.
> - On the subscriptions detail page, click the subscription group.
> - Click the subscription you want to set up availability for.
> - In the Availability section, click Set Up Availability.
> - Select the countries or regions where you want to make your subscription available.
> - Click Done.
>
> Keep in mind that even if you set availability for an auto-renewable subscription, it may not be available for purchase. Monitor the In-App Purchase statuses to understand if action is needed from you, such as completing missing metadata, or if your In-App Purchase has been approved by App Review.
>
> ### Make changes to your auto-renewable subscription’s availability
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Subscriptions.
> - On the subscriptions detail page, click the subscription group.
> - Click the subscription you want to edit availability for.
> - Under Availability, click Edit.
> - In the dialog that appears, change your subscription’s availability by selecting or deselecting your desired countries or regions.
>
> Note: You must be the Account Holder in order to remove countries or regions, as this will impact existing subscribers.
>
> - Click Done.
> - On the top right, click Save.

**Applies to:** Apps that offer auto-renewable subscriptions
**Requires:** subscriptions

- **[IAPX-08]** For each auto-renewable subscription whose availability has been set, does its In-App Purchase status show no action needed (such as completing missing metadata)?
  - quote: "Keep in mind that even if you set availability for a subscription, it may not be available for purchase. Monitor the In-App Purchase statuses to understand if action is needed from you, such as completing missing metadata"
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Subscriptions > [group] > [subscription] > Availability: countries or regions are selected; the subscription's status does not indicate missing metadata or other required action.
  - fix: Click Set Up Availability, select countries or regions, click Done, then Save; complete any missing metadata.

## IAPX.14 Discontinuing an auto-renewable subscription

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription

**Source text (verbatim):**
> If you want to discontinue an auto-renewable subscription, consider the impact on users and any communications you might need to provide. Also consider whether your app still functions without the subscription. If not, remove your app from the App Store.
>
> Keep in mind that you’re required by the Paid Apps Agreement to provide the full amount of content to eligible subscribers through the subscription duration.
>
> Taking the following steps before removing your auto-renewable subscription from sale can help ensure a smooth experience:
>
> - Before discontinuing an auto-renewable subscription, remove it from sale, within App Store Connect, to stop additional sign-ups and renewals. We recommend timing the removal of your subscription to be equivalent to its duration. A minimum of 31 days is required from the date subscription is removed from sale and service is stopped to allow monthly and shorter duration subscriptions to expire.
> - For subscriptions longer than one month, if you're unable to provide the full amount of content to eligible subscribers through the subscription duration before removing the subscription, contact us.
> - Provide subscribers with advanced notice of the discontinuation of your subscription service through channels such as email, website, and in-app messaging. We recommend notifying them at least 31 days before discontinuing the subscription service.
> - End any promotions of the subscription to discourage purchases.
>
> To remove your subscription from sale:
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Subscriptions.
> - Click the subscription group, then the subscription.
> - Under Availability, click Removing from Sale and confirm to remove your subscription from sale.
> - Click Save.
>
> Apps in the Magazines and Newspapers category need at least one active auto-renewable subscription to be listed in that category. If you want to discontinue the only auto-renewable subscription in your app, you must switch to a different category and submit a new binary to App Store Connect. Then you'll be able to remove the subscription.

**Applies to:** Apps discontinuing or removing from sale an auto-renewable subscription; Magazines and Newspapers category apps

- **[IAPX-09]** If the app is listed in the Magazines and Newspapers category, does it keep at least one active auto-renewable subscription?
  - quote: "Apps in the Magazines and Newspapers category need at least one active auto-renewable subscription to be listed in that category."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Information > Category: if Magazines and Newspapers is selected, confirm under Subscriptions that at least one auto-renewable subscription remains available (not removed from sale).
  - fix: Keep an active auto-renewable subscription, or switch to a different category and submit a new binary before removing the only subscription.
- **[IAPX-10]** If a subscription is being discontinued, does the app still function without it (otherwise, is the app being removed from the App Store)?
  - quote: "Also consider whether your app still functions without the subscription. If not, remove your app from the App Store."
  - surface: runtime
  - verify: Run the build with no active entitlement to the discontinued product and confirm core features still work and no flow dead-ends on the removed subscription.
  - fix: Rework the app so it functions without the subscription, or remove the app from the App Store.
- **[IAPX-11]** If a subscription is being discontinued, does the app keep providing the full subscribed content to eligible subscribers through their subscription duration?
  - quote: "you’re required by the Paid Apps Agreement to provide the full amount of content to eligible subscribers through the subscription duration."
  - surface: code
  - verify: In the Xcode project, confirm entitlement checks still recognize the discontinued product identifier for current subscribers (the product ID is not deleted from the entitlement mapping) and that server-side content gating does the same.
  - fix: Keep honoring the discontinued product's entitlements until every eligible subscription period has ended; contact Apple if full content cannot be provided.
- **[IAPX-12]** If a subscription is being discontinued, will it be removed from sale at least 31 days before service is stopped?
  - quote: "A minimum of 31 days is required from the date subscription is removed from sale and service is stopped to allow monthly and shorter duration subscriptions to expire."
  - surface: manual
  - verify: Compare the date the subscription was (or will be) set to Remove from Sale in App Store Connect > Subscriptions > [subscription] > Availability with the planned service shutdown date.
  - fix: manual — requires developer decision/legal/business action (schedule removal from sale at least 31 days before stopping service).
- **[IAPX-13]** If a subscription is being discontinued, have subscribers been given advance notice (recommended at least 31 days before discontinuation)?
  - quote: "We recommend notifying them at least 31 days before discontinuing the subscription service."
  - surface: manual
  - verify: Ask for the dated subscriber communications (email, website, in-app messaging) announcing the discontinuation.
  - fix: manual — requires developer decision/legal/business action (notify subscribers in advance).

## IAPX.15 Offer monthly subscriptions with 12 month commitment

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription

**Source text (verbatim):**
> For subscriptions outside the United States and Singapore, you have the option to configure a billing option where subscribers commit to paying monthly for a set period of time. Unlike a standard monthly subscription, the subscriber is committing to 12 monthly payments. Once all 12 payments are completed, the subscription automatically renews into another 12 month commitment at the standard billing price of that payment option until they choose to cancel. Subscribers can view their completed and remaining payments at any time in their Apple Account, and Apple will send reminders ahead of the next commitment period. This is useful if you want to offer subscribers more affordable options.
>
> Monthly with 12-month commitment subscriptions are only available on devices that use operating system version 26.4 or later (on all storefronts except the United States and Singapore, and excluding watchOS) and apps built with an SDK version of 26.5 or later.
>
> - In the Sidebar, under Monetization, click Subscriptions.
> - Click a subscription group name.
> - Click Create.
>
> Note: If you're adding a subscription to a group that already has existing subscriptions, you'll click the add button (+).
>
> - Enter the subscription’s reference name and Product ID.
> - Under Subscription Duration, select 1 Year.
> - Click Create. Once you've created your subscription product, you'll be taken to its information page to add more details.
> - In the Availability section under 1 Year Upfront, click Set Up Availability.
> - Select the countries or regions where you'd like the subscription to be available. When this option is enabled, customers will pay for an entire year upfront when they subscribe. When their subscription renews, they'll be billed for another full year if they don't cancel before renewal. Setting up upfront billing availability is required before you can offer the monthly payment option. If you only complete this step, your subscription will be available only as a single upfront annual payment.
> - Click Confirm.
> - To give subscribers the option to pay monthly with a 12 month commitment, click Set Up Availability in the Monthly with 12-Month Commitment section.
> - Select the countries or regions where you'd like to offer the monthly payment option. Customers will commit to paying the monthly price for 12 months before their subscription renews. If a customer cancels before the end of their commitment, they'll continue paying until their commitment is complete (except in certain regions), and their subscription will not renew.
>
> Note: Monthly billing will only be available in countries or regions where you have set up upfront billing availability.
>
> - Click Confirm.
> - In the Subscription Prices section, click Add Subscription Price.
> - Choose an upfront and monthly price in the base territory for this subscription, and we'll automatically calculate the prices for all 175 countries or regions based on the most recent foreign exchange rates. The 12-month commitment total must be greater than or equal to the upfront price, and less than or equal to 1.5 times the upfront price. You can edit prices for individual countries or regions (excluding the United States and Singapore) in the next step.
> - Click Next.
> - App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.
> - Review your prices and Click Confirm.
> - Optionally, configure subscription offers. Upon completion of the offer period, customers will renew to the 12 month payment commitment.
> - You can remove this monthly billing option in App Store Connect at any time. In the Availability section under Monthly with 12 Month Commitment, click Remove Monthly Billing. Confirm you want to remove the option and click Confirm. Existing customers won't renew at the end of their 12 month commitment, and new customers won't be able to subscribe to that payment option.

**Applies to:** Apps offering the Monthly with 12-Month Commitment billing option (storefronts outside the United States and Singapore)
**Requires:** subscriptions

- **[IAPX-14]** If the app offers monthly subscriptions with a 12-month commitment, is it built with an SDK version of 26.5 or later?
  - quote: "apps built with an SDK version of 26.5 or later"
  - surface: code
  - verify: Check the Xcode version/SDK used to archive the build (Xcode > Settings > Locations, or the DTSDKName/DTPlatformVersion keys in the built app's Info.plist, or the build's SDK shown in App Store Connect).
  - fix: Archive and upload the build with an Xcode release that includes SDK 26.5 or later.
- **[IAPX-15]** If the monthly payment option is offered, is upfront (1 Year Upfront) billing availability set up in those countries or regions?
  - quote: "Setting up upfront billing availability is required before you can offer the monthly payment option."
  - surface: asc
  - verify: App Store Connect > Subscriptions > [group] > [1-year subscription] > Availability: 1 Year Upfront has countries or regions selected, covering every country or region selected under Monthly with 12-Month Commitment.
  - fix: Under 1 Year Upfront click Set Up Availability and select the countries or regions, then Confirm.
- **[IAPX-16]** Is the 12-month commitment total greater than or equal to the upfront price and no more than 1.5 times the upfront price?
  - quote: "The 12-month commitment total must be greater than or equal to the upfront price, and less than or equal to 1.5 times the upfront price."
  - surface: asc
  - verify: App Store Connect > Subscriptions > [subscription] > Subscription Prices: multiply the monthly price by 12 and compare with the upfront price in the base territory and any manually edited storefronts.
  - fix: Adjust the upfront or monthly price so 12 × monthly is between 1× and 1.5× the upfront price.

## IAPX.16 In-App Purchase and subscriptions pricing and availability (reference)

**Source page:** https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability/in-app-purchase-and-subscriptions-pricing-and-availability

**Source text (verbatim):**
> Pricing and availability properties describe when the In-App Purchase is available and at what price.
>
> | Property | Description |
> |---|---|
> | Availability | Allows you to select country or region availability for your In-App Purchases. To remove your In-App Purchases from the App Store, deselect individual countries or regions, or select "Remove from sale." |
> | Price | The price you choose for the In-App Purchase, which determines both the customer price and your proceeds. Click All Prices and Currencies from Pricing to view the price values in each currency. |
> | Start Date | The date when the price becomes available. |
> | End Date | The date that a price is no longer in effect. The price is the last tier scheduled if this value is No end Date. |
>
> These properties describe pricing and availability options for auto-renewable subscriptions.
>
> | Property | Description |
> |---|---|
> | Subscription Prices | Pricing for your auto-renewable subscriptions. Auto-renewable subscriptions can be priced by country or region, with up to 800 price points in each available currency. You have the option to preserve the current price for existing subscribers if you increase the price. Promotional and introductory price points are also available. |
> | Introductory Offers | A discounted introductory price you can set for your auto-renewable subscriptions with a specified duration and type (pay as you go, pay up front, free) for new customers. Introductory offers can be used to acquire new customers. Keep in mind that:<br>- You can have one current and one future introductory offer set up per country or region.<br>- You can manage country or region availability and start and end dates in App Store Connect. Learn more about introductory offers.<br>- Introductory offers display on your App Store product page if you’ve promoted your In-App Purchase.<br>- Customers are eligible for one introductory offer per subscription group.<br>- Introductory offers are available to customers running iOS 10, macOS 10.12.6, and tvOS 10, or later. |
> | Offer Codes | Redeemable codes that provide a free or discounted price for your auto-renewable subscriptions with a specified duration and type (pay as you go, pay up front, free) for new, existing, and previously subscribed customers. Offer codes can be used to acquire, retain, and win back subscribers. Keep in mind that:<br>- You can create codes for a maximum of 1 million redemptions per app, per quarter.<br>- You can select customer eligibility rules, timing, territories, pricing, duration, and number of codes in App Store Connect. Learn more about offer codes.<br>- Customers are eligible to redeem one code per active offer.<br>- Offer codes can be redeemed by customers running iOS 14, iPadOS 14, and macOS 15, or later. |
> | Promotional Offers | A discounted price you can set for your auto-renewable subscriptions for a specific duration and type(Pay as you go, Pay up front, Free) for existing and previously subscribed customers. Offers can be used to help win back subscribers who have canceled their subscriptions or promote an upgrade to a higher-ranked subscription at a special price. Keep in mind that:<br>- You determine when to present the offers through StoreKit APIs.<br>- You must generate a subscription key in Users and Access to validate your offers.<br>- You can have up to 10 active offers per subscription.<br>- Offers don’t display on your App Store product page.<br>- You can select price and duration in App Store Connect. Learn more about promotional offers.<br>- Customers that have completed an introductory offer are still eligible to get a promotional offer.<br>- Customers running iOS 12.2, macOS 10.14.4, and tvOS 12.2, or later can accept these offers. |
> | Retention Offers | A discounted or free offer you can present to subscribers who are in the process of canceling their subscription, as an incentive to stay subscribed. Retention offers are shown within a custom retention message rather than on your App Store product page. You can set customer eligibility based on paid subscription tenure and the time since a previously redeemed offer. You can create up to 10 retention offers for each subscription billing plan type, and associate up to all 10 of those offers with a single retention message. You can select price, duration, storefronts, and eligibility criteria in App Store Connect. Learn how to configure retention messages. |
> | Promotional Offer Reference Name | An internal name for a promotional offer that you can reference. |
> | Promotional Offer Identifier | An identifier that you create. This string is case sensitive and must be unique for each offer you create. You won’t be able to reuse an offer identifier, even if it’s been deleted. |
> | Duration (for promotional and introductory offers) | The length of time between auto-renewals that you select for your promotional or introductory offers. The offer durations available to you depend on the standard duration of your subscription. |
> | Pay As You Go | If you select Pay as you go, customers pay a discounted price for each billing period for a selected duration (for example, $1.99 per month for 3 months for a subscription with a standard price of $9.99).<br>The duration can be:<br>- 1-week subscription, 1 to 12 week<br>- 1-month subscription, 1 to 12 month<br>- 2-month subscription, 2, 4, 6, 8, 10 and 12 month<br>- 3-month subscription, 3, 6, 9 and 12 month<br>- 6-month subscription, 6 and 12 month<br>- 1-year subscription, 1 year |
> | Pay Up Front | If you select Pay up front, customers pay a one-time discounted price for a selected duration (for example, $1.99 for 2 months for a subscription with a standard price of $9.99).<br>The duration can be: 1 Month, 2 Months, 3 Months, 6 Months, 1 Year. |
> | Free | If you select Free, customers access the subscription for free for a selected duration. The duration can be 3 days, 1 week, 2 weeks, 1 month, 2 months, 3 months, 6 months, or 1 year. A one-month trial can vary between 28 days and 31 days. |
> | Available for Purchase From | Where an auto-renewable subscription is available for multiseat purchase. Options are the App Store, Apple Business, and Apple School Manager. Learn how to set purchase options for an auto-renewable subscription. |

**Applies to:** Apps that offer In-App Purchases or auto-renewable subscriptions
**Requires:** iap, subscriptions

- **[IAPX-31]** If the app presents promotional offers for auto-renewable subscriptions, has a subscription (In-App Purchase) key been generated in Users and Access to validate the offers?
  - quote: "You must generate a subscription key in Users and Access to validate your offers."
  - surface: asc
  - verify: App Store Connect > Users and Access > Integrations > In-App Purchase: at least one Active key exists, and its key ID matches the one the server uses to sign promotional offers.
  - fix: Generate an In-App Purchase key in Users and Access, download it once, store it securely on the server and use it to sign the offers.

## IAPX.17 Enable Billing Grace Period for auto-renewable subscriptions

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/enable-billing-grace-period-for-auto-renewable-subscriptions

**Source text (verbatim):**
> Billing Grace Period lets subscribers whose auto-renewal failed due to a payment issue continue accessing your app’s paid content for a period of time while Apple continues to attempt to collect payment. There won’t be any interruption to the subscriber’s days of paid service or to your revenue if Apple recovers the subscription within the grace period. Without enabling Billing Grace Period, the subscriber’s days of paid service pause until Apple is able to collect payment.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment. Billing Grace Period doesn't apply for monthly subscriptions with a 12 month commitment.
>
> You can configure grace periods in App Store Connect using the App Store Connect API.
>
> ## Workflow for enabling Billing Grace Period
>
> Enabling Billing Grace Period requires you turn on and complete configurations in App Store Connect, and use StoreKit to verify subscribers’ renewal states so they retain access to subscription content while in the billing retry state.
>
> The following workflow can be used to properly test and validate your server to app’s logic before fully rolling out the feature to your subscribers.
>
> - Turn on Billing Grace Period in sandbox.
>
> Make sure to do this only before turning it on in production.
>
> - Test Billing Grace Period in sandbox.
>
> Use the sandbox environment to validate your client and server logic to handle subscribers entering and exiting the grace period. View implementation guidance.
>
> - Turn on Billing Grace Period in production.
>
> Once you validate your client and server logic, edit your Billing Grace Period configuration to support the production environment.
>
> Required role: Account Holder, Admin or App Manager. View role permissions.
>
> ### Turn on Billing Grace Period
>
> You can turn on Billing Grace Period for each app in App Store Connect to provide a grace period for all auto-renewable subscriptions in the app. Configurability isn’t available for individual subscription products.
>
> - From Apps, select your app.
> - In the sidebar, click Subscriptions.
> - In the Billing Grace Period section, click Set Up Billing Grace Period.
> - From the menu, select a period of 3, 16, or 28 days to apply across all subscription products in your app.
>
> Note: If your app offers weekly subscriptions, even if you select a 16 or 28 day grace period, the actual grace period will only be 6 days to ensure it isn't longer than the subscription itself.
>
> Your selection will only apply to subscription products in production. Learn about the Billing Grace Period renewal rates in sandbox.
>
> |  | 3 day Billing Grace Period | 16 day Billing Grace Period | 28 day Billing Grace Period |
> |---|---|---|---|
> | Weekly subscriptions | 3 days | 6 days | 6 days |
> | Monthly and yearly subscriptions | 3 days | 16 days | 28 days |
>
> - Select the renewal types for which you want to enable a grace period:
> - All Renewals: Billing Grace Period applies to all renewals, including free introductory offers and free subscription offers transitioning to paid subscriptions.
> - Only Paid to Paid Renewals: Billing Grace Period will only apply to subscriptions in a currently paid period, therefore subscriptions currently in a Free period won’t receive a billing grace period.
> - Select the server environments for which you want to enable Billing Grace Period.
> - Only Sandbox Environment: Billing Grace Period is enabled in the sandbox environment only. Use Sandbox to test that your app provides service to subscriptions during a grace period.
> - Production and Sandbox Environment: Billing Grace Period is enabled in both sandbox and production environments.
> - Click Confirm.
>
> Your app still needs to perform purchase validation and account for the subscriber’s renewal status to identify if a subscription is in a Billing Grace Period.
>
> ### Edit Billing Grace Period configuration
>
> - From Apps, select your app.
> - In the sidebar, click Subscriptions.
> - In the Billing Grace Period section, click Edit. You can edit the duration of the grace period, the eligible renewal types, and the enabled environments. Changes can take up to 24 hours to take effect and will only apply to upcoming renewals. Subscribers currently in Billing Grace Period are still entitled to service during their grace period.
> - Click Done.
>
> ### Turn off Billing Grace Period
>
> You can turn off Billing Grace Period for each app.
>
> - From Apps, select your app.
> - In the sidebar, click Subscriptions.
> - In the Billing Grace Period section, click Edit.
> - Click Turn Off.
>
> Once you turn off Billing Grace Period, subscribers whose renewal fails due to a billing issue won’t accumulate days of paid service until Apple is able to collect payment and renew the subscription. Ensure that your app continues to provide service for subscriptions that are already in Billing Grace Period.

**Applies to:** Apps with auto-renewable subscriptions that turn on (or turn off) Billing Grace Period
**Requires:** subscriptions

- **[IAPX-17]** If Billing Grace Period is turned on, does the app (and server) validate purchases and check the subscriber's renewal status so subscribers in a grace period keep access?
  - quote: "Your app still needs to perform purchase validation and account for the subscriber’s renewal status to identify if a subscription is in a Billing Grace Period."
  - surface: code
  - verify: App Store Connect > Apps > [app] > Subscriptions > Billing Grace Period shows the setting; in the Xcode project, find the entitlement logic and confirm it reads the subscription renewal state (e.g. StoreKit 2 `Product.SubscriptionInfo.RenewalState` / `.inGracePeriod`, or server-side renewal info) and grants access during the grace period rather than treating a failed renewal as expired.
  - fix: Update entitlement logic to treat subscriptions in a Billing Grace Period as active, based on validated renewal status.
- **[IAPX-18]** Before Billing Grace Period is enabled for production, was the client and server logic for entering and exiting the grace period tested in sandbox?
  - quote: "Use the sandbox environment to validate your client and server logic to handle subscribers entering and exiting the grace period."
  - surface: runtime
  - verify: App Store Connect > Subscriptions > Billing Grace Period: check the server environment setting (Only Sandbox Environment vs Production and Sandbox Environment); with a sandbox account, simulate a failed renewal and confirm the app keeps access during the grace period and updates when it ends.
  - fix: Enable Billing Grace Period for Only Sandbox Environment, test, then edit the configuration to Production and Sandbox Environment.
- **[IAPX-19]** If Billing Grace Period is being turned off, does the app continue to provide service for subscriptions already in a Billing Grace Period?
  - quote: "Ensure that your app continues to provide service for subscriptions that are already in Billing Grace Period."
  - surface: code
  - verify: In the entitlement logic, confirm grace-period handling is not removed together with the App Store Connect setting.
  - fix: Keep grace-period entitlement handling in the app/server for subscriptions already in a grace period.

## IAPX.18 Generate keys for In-App Purchases

**Source page:** https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-keys-for-in-app-purchases

**Source text (verbatim):**
> Generating an In-App Purchase key allows Apple to authenticate and validate client-to-server or server-to-server requests related to In-App Purchases, including App Store server APIs and promotional offers for auto-renewable subscriptions.
>
> Required role: Account Holder or Admin. View role permissions.
>
> ## Generate an In-App Purchase key
>
> - Select Users and Access at the top of the page.
> - Click the Integrations tab.
> - In the sidebar, under Keys, click In-App Purchase.
> - Click Generate In-App Purchase Key.
>
> If you already have an Active In-App Purchase key generated, you will click the Add (+) icon to add more.
>
> - Enter a name for the key. The name is used for your reference only and is not part of the key itself.
> - Click Generate.
>
> Once you generate an In-App Purchase key, you won't be able to edit its name. If you need to make changes, revoke the key and generate a new one.
>
> ### Download an In-App Purchase key
>
> In-App Purchase keys are private and can be downloaded only once. After downloading the key, store it in a safe place. Remember to revoke a key immediately if it becomes lost or compromised and ensure that offers using this key are updated.
>
> - Select Users and Access at the top of the page.
> - Click the Integrations tab.
> - In the sidebar, under Keys, click In-App Purchase.
> - Navigate to a key under the Active section, then click Download Key for the key you want to download. Keep in mind that keys can be downloaded only once.
> - In the dialog, click Download.
>
> ### Revoke an In-App Purchase key
>
> If you no longer want to use an In-App Purchase key to validate your offers, you can revoke the key.
>
> - Select Users and Access at the top of the page.
> - Click the Integrations tab.
> - In the sidebar, under Keys, click In-App Purchase.
> - On the top right, click Edit.
> - Select the keys you want to revoke.
> - On the top right, click Revoke Key, then click Revoke in the dialog. You won't be able to reinstate a key after it's been revoked.
>
> Revoke a key to prevent redemption of offers associated with it. Update all offers using that key immediately. Revoked keys from the past 30 days appear in the Revoked section of the In-App Purchase page.

**Applies to:** Apps or servers that use App Store server APIs or promotional offers for auto-renewable subscriptions

- **[IAPX-20]** Is the downloaded In-App Purchase private key (.p8) stored in a safe place (for example, not shipped in the app bundle or committed to the source repository)?
  - quote: "In-App Purchase keys are private and can be downloaded only once. After downloading the key, store it in a safe place."
  - surface: code
  - verify: Search the Xcode project and repository for `*.p8` files and for the string `BEGIN PRIVATE KEY`; confirm no such file is in any target's Copy Bundle Resources or committed to git; signing must happen server-side.
  - fix: Remove the key from the project and git history, move it to secure server-side storage, and revoke it in Users and Access > Integrations > In-App Purchase if it was exposed (then update offers to a new key).
- **[IAPX-21]** Is the In-App Purchase key used by the server listed as Active (not revoked), with all offers updated to a current key?
  - quote: "Revoke a key to prevent redemption of offers associated with it. Update all offers using that key immediately."
  - surface: asc
  - verify: App Store Connect > Users and Access > Integrations > Keys > In-App Purchase: confirm the key ID configured on the server appears under Active, not Revoked.
  - fix: Generate a new In-App Purchase key, deploy it to the server, and update all offers that used the revoked key.

## IAPX.19 Generate a shared secret to verify receipts

**Source page:** https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts

**Source text (verbatim):**
> Include a shared secret in your request to verify App Store subscription or In-App Purchase receipts to increase security between your server and Apple's servers.
>
> A shared secret is a 32-character hexadecimal string generated in App Store Connect. You may generate a primary shared secret, which is a single code for all your apps, or an app-specific shared secret for individual apps. You may also use a primary shared secret for some of your apps, and an app-specific shared secret for others.
>
> The verifyReceipt endpoint is deprecated. To validate In-App Purchases on your server without using receipts, use the App Store Server API instead. For more information, visit Validating Receipts with the App Store.
>
> Required role: Account Holder or Admin. View role permissions.
>
> ## View or generate a shared secret for all your apps (primary shared secret)
>
> - Select Users and Access at the top of the page.
> - Click the Integrations tab.
> - In the sidebar, under Keys, click Shared Secret.
> - Click Generate Primary Shared Secret.
> - Copy the code and use it for your transactions receipt for all of your apps with In-App Purchases.
>
> ### View or generate a shared secret for an individual app (app-specific shared secret)
>
> Access the app-specific shared secret in the Subscriptions page of your app. You may want to use an app-specific shared secret if you want to keep this code private for this app, or if you're planning to transfer this app to another developer account.
>
> Note: App-specific shared secrets can’t be deleted, only regenerated.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under General, click App Information.
> - In the App-Specific Shared Secret section, click Manage.
> - You can generate a shared secret for individual apps, or regenerate a shared secret.
>
> Note: Clicking Regenerate will automatically generate a new shared secret, and any previously generated shared secret for this app will be invalidated.
>
> - Then click Done.
> - To generate a shared secret, click Generate or Regenerate in the dialog.
> - Copy the code and use it for your transactions receipt for this app.
>
> When you regenerate an app-specific shared secret, use the new value to verify your In-App Purchases for this app.
>
> ### Transitioning to a new shared secret
>
> When you regenerate or change a shared secret, expect a transition period of up to 24 hours before the new shared secret takes effect. During this transition period, do the following:
>
> - To change to using an app-specific shared secret from using a primary shared secret, fall back to using the primary shared secret until using the new app-specific shared secret succeeds.
> - To refresh a primary shared secret, fall back to the old primary shared secret until using the new primary shared secret succeeds.

**Applies to:** Apps or servers that verify App Store receipts

- **[IAPX-22]** Does the app or its server avoid the deprecated verifyReceipt endpoint (using the App Store Server API instead)?
  - quote: "The verifyReceipt endpoint is deprecated."
  - surface: code
  - verify: Search the Xcode project and server code for `verifyReceipt`, `buy.itunes.apple.com` and `sandbox.itunes.apple.com`.
  - fix: Migrate server-side validation to the App Store Server API.
- **[IAPX-23]** If the app-specific shared secret was regenerated, does the server use the new value?
  - quote: "When you regenerate an app-specific shared secret, use the new value to verify your In-App Purchases for this app."
  - surface: code
  - verify: Compare the shared secret configured in the server environment with App Store Connect > Apps > [app] > App Information > App-Specific Shared Secret > Manage.
  - fix: Update the server configuration with the new shared secret (falling back to the previous secret during the up-to-24-hour transition).

## IAPX.20 Enter server URLs for App Store Server Notifications

**Source page:** https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/enter-server-urls-for-app-store-server-notifications

**Source text (verbatim):**
> App Store Server Notifications provide information about key events related to your In-App Purchases, such as changes to a subscription's status or the refund of an In-App Purchase. In order to receive these notifications from the App Store, you must provide a URL in App Store Connect that links to your server. You can enter URLs for both production and sandbox endpoints.
>
> To receive App Store Server Notifications, configure your server and visit Enabling App Store Server Notifications. For more details on notifications and their meanings, see the App Store Server Notifications.
>
> Note: It may take up to 1 hour for changes you make to product metadata to appear in the sandbox environment.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> ## Enter a production URL for App Store Server Notifications
>
> - In Apps, select the app you want to view.
> - In the sidebar, under General, click App information.
> - Scroll down to General Information, then go to App Store Server Notifications.
> - Under Production Server URL, click Set Up URL.
> - Enter the URL that you've determined for App Store Server Notifications.
> - Choose either Version 1 (deprecated) or Version 2 notifications. Learn about versions of App Store Server Notifications.
> - Click Save.
>
> ### Enter a URL for testing App Store Server Notifications in a Sandbox environment
>
> If you do not provide a Sandbox URL in App Store Connect, please note that the App Store will automatically send notifications for both environments to the Production URL provided. If you only provide a Sandbox URL, no notifications will be sent in production.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under General, click App information.
> - Scroll down to General Information, then go to App Store Server Notifications.
> - Under Sandbox Server URL, click Set Up URL.
> - Enter the URL that you've determined for App Store Server Notifications.
> - Choose either Version 1 (deprecated) or Version 2 notifications. Learn about versions of App Store Server Notifications.
> - Click Save.
>
> ### Edit your URL for App Store Server Notifications
>
> - In Apps, select the app you want to view.
> - In the sidebar, under General, click App information.
> - Scroll down to General Information, then go to App Store Server Notifications.
> - Next to the URL you want to edit, click Edit.
> - Enter the desired URL and click Save.

**Applies to:** Apps whose server receives App Store Server Notifications
**Requires:** iap, subscriptions

- **[IAPX-32]** If the app's server relies on App Store Server Notifications, is a server URL entered in App Store Connect?
  - quote: "In order to receive these notifications from the App Store, you must provide a URL in App Store Connect that links to your server."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Information > General Information > App Store Server Notifications: a Production Server URL (and, for testing, a Sandbox Server URL) is set and matches the server endpoint that handles notifications.
  - fix: Click Set Up URL next to Production Server URL (and Sandbox Server URL), enter the server URL, choose the version, and click Save.
- **[IAPX-24]** Are the App Store Server Notifications URLs configured for Version 2 notifications rather than the deprecated Version 1?
  - quote: "Choose either Version 1 (deprecated) or Version 2 notifications."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Information > General Information > App Store Server Notifications: check the version shown for the Production Server URL and Sandbox Server URL.
  - fix: Edit each URL and select Version 2 notifications (after the server supports the Version 2 format), then Save.
- **[IAPX-25]** If a Sandbox Server URL is entered, is a Production Server URL also entered?
  - quote: "If you only provide a Sandbox URL, no notifications will be sent in production."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Information > App Store Server Notifications: confirm Production Server URL is set, not only Sandbox Server URL.
  - fix: Under Production Server URL click Set Up URL, enter the server URL, choose the version, and click Save.

## IAPX.21 Promote In-App Purchases

**Source page:** https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases

**Source text (verbatim):**
> iOS
>
> Promoted In-App Purchases appear on your product page, can display in search results, and may be featured on the Today, Games, and Apps tabs.
>
> You can promote up to 20 In-App Purchases on their App Store product page simultaneously, in all countries or regions, for devices running iOS 11 or later. This gives you the flexibility to change the In-App Purchases that appear on your product page at any time based on your business needs — for example, such as launching a limited-time price promotion or offering exclusive content. Promoting In-App Purchases can also encourage downloads of your app. When a user doesn’t have your app installed but wants to buy a promoted In-App Purchases, they’ll receive a prompt to download the app first. Once the app is downloaded, the transaction will continue in the app.
>
> Your app must support the PurchaseIntent API in order for the App Store to display your promoted product pages. All In-App Purchases and metadata must be approved by App Review.
>
> Learn how to manage promoted in-app purchases and subscriptions with the App Store Connect API.
>
> Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.
>
> ## Add an Image
>
> You must add an image in order to promote an In-App Purchase.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, then scroll down to Non-Renewing Subscriptions and click Manage).
> - Click the In-App Purchase you want to promote.
> - Scroll down to the App Store Image section.
> - To add an image, click Choose File and upload the image.
>
> ### Promote an In-App Purchase
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click In-App Purchases. (For non-renewing subscriptions, click Subscriptions, and then scroll down to Non-Renewing Subscriptions and click Manage).
> - Click the In-App Purchase you want to promote.
> - Scroll down to the App Store Image section.
> - Click Promote on the App Store.
> - In the pop-up window, choose which App Store users will see your promotion. Changes to these settings only impact the In-App Purchase you're editing:
> - Show this promotion to all App Store users, even those who don’t have the app installed.  If you select this option, but haven't implemented the PurchaseIntent API, your In-App Purchase won't be visible on the App Store.
> - Only show this promotion to users who meet your conditions in the app.  You can customize the promoted In-App Purchase a customer views on a specific device by using the Product.PromotionInfo API. For example, you can hide an item that a customer has already purchased on that device, or show the most relevant levels in a game based on their gameplay. By default, your promoted In-App Purchases show on all devices, even those without the app installed.
> - Find the In-App Purchase you wish you promote, and then click the checkbox under Promoted. You may also click the reordering control on the left of the In-App Purchase name and drag it to a new position to change its order on your App Store Product page.
> - Click Save.
>
> Keep in mind that if an app isn't ready for sale or the In-App Purchase is pending approval, it may not be available on your App Store product page even when it's available for App Store Promotion. Allow up to 24 hours for changes to reflect on your App Store product page.

**Applies to:** Apps that promote In-App Purchases on their App Store product page (iOS)
**Requires:** iap, subscriptions

- **[IAPX-26]** If In-App Purchases are promoted, does the app support the PurchaseIntent API?
  - quote: "Your app must support the PurchaseIntent API in order for the App Store to display your promoted product pages."
  - surface: code
  - verify: Search the Xcode project for `PurchaseIntent` (e.g. iterating `PurchaseIntent.intents`) and confirm the intent is handled by starting the purchase; at runtime, open a promoted In-App Purchase from the App Store product page and confirm the transaction continues in the app.
  - fix: Implement handling of StoreKit `PurchaseIntent` so promoted purchases started on the App Store complete in the app.
- **[IAPX-27]** Does every promoted In-App Purchase have an App Store image added?
  - quote: "You must add an image in order to promote an In-App Purchase."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > In-App Purchases > [product] > App Store Image section: an image is uploaded for each product marked Promoted.
  - fix: In the App Store Image section click Choose File and upload the image.
- **[IAPX-28]** Are all promoted In-App Purchases and their metadata approved by App Review?
  - quote: "All In-App Purchases and metadata must be approved by App Review."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > In-App Purchases: confirm each promoted product's status is approved; submit pending ones with the app version.
  - fix: Submit the In-App Purchases (and metadata) for review and wait for approval.

## IAPX.22 In-App Purchase localization statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-localization-statuses

**Source text (verbatim):**
> | Status | Description |
> |---|---|
> | Prepare for Submission | You have created your localization but it is not yet submitted to App Review. |
> | Waiting for Review | Your localization is currently being reviewed by App Review. |
> | Approved | Your localization has been approved. |
> | Rejected | Your localization has been rejected. |

**Applies to:** Apps with localized In-App Purchase metadata
**Requires:** iap, subscriptions

## IAPX.23 Create offer codes for In-App Purchases

**Source page:** https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases

**Source text (verbatim):**
> Offer codes provide a way to acquire, retain, and win back customers by offering discounted or free access to In-App Purchases. You create and manage them in App Store Connect, and customers can redeem them through a redemption URL, by entering the code in the App Store, or within your app.
>
> Each app can have up to 10 active offers at a time, with a limit of 1 million codes per app, per quarter. Each customer can redeem one code per offer. You set the eligibility criteria for who can redeem; customers who have never purchased within your app, purchased in the last 30 days, or purchased more than 30 days ago. Selecting all options makes the offer available to everyone. Carefully consider your eligibility requirements before creating and distributing offer codes.
>
> You can create offer codes and sandbox codes regardless of your app's current App Status. To generate one-time-use or custom codes, your app must be Ready for Distribution and the associated In-App Purchase must be Approved.
>
> There are three types of offer codes:
>
> - One-time-use codes are unique, randomly generated codes that each customer can redeem only once. They're best suited to small-scale or targeted distributions. For example, giving codes to event attendees, contest winners, or individuals as a special discount. Customers can redeem them through a unique redemption URL, by entering the code in the App Store, or within your app.
> - Custom codes are codes you name yourself. For example, SUMMER25 or VIPACCESS. Unlike one-time-use codes, a custom code can be redeemed by multiple customers up to a limit you set. They're best suited to large-scale marketing campaigns or promotions targeting specific customer groups. Customers can redeem them through a redemption URL or within your app.
> - Sandbox codes are one-time-use codes for testing. Use them to verify your offer code redemption flow in the sandbox environment without affecting real users or production data. Each app can distribute up to 10,000 sandbox codes per quarter, and sandbox test accounts have no redemption limits. If redemptions are blocked, clear the purchase history for the sandbox Apple account and retest.
>
> You can create offer codes and sandbox codes for your app regardless of its current App Status. However, to generate custom or unique offer codes, your app must be Ready for Distribution, and the associated In-App Purchase must be Approved.
>
> Carefully consider your offer's eligibility requirements before creating and distributing offer codes.
>
> |  | One time-use | Custom | Sandbox |
> |---|---|---|---|
> | How customers redeem | Redemption URL, App Store, or in-apps | Redemption URL or in-app | Sandbox account settings on device |
> | Codes per app per quarter | Up to 1 million<br>Shared across all In-App Purchases | Up to 1 million<br>Shared across all In-App Purchases | Up to 10,000<br>Shared across all In-App Purchases |
> | Expiration | Required — up to 6 months | Optional — up to 6 months if set | Optional |
> | In-app redemption requires | iOS 16.3, macOS 15.0, or visionOS 1.0 or later + StoreKit method | iOS 16.3, macOS 15.0, or visionOS 1.0 or later + StoreKit method | iOS 16.3 or iPadOS 16.3 or later + StoreKit method |
>
> Note: Redemption within your app for one-time-use and custom codes requires customers to use a device running iOS 16.3, macOS 15.0, or visionOS 1.0 or later, and your app must support the appropriate StoreKit method.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> ## Set up offers
>
> - From Apps, select your app.
> - In the sidebar, click In-App Purchases.
> - Click the In-App Purchase you want to create an offer for.
> - Scroll down to the Offer Codes section and click Create Offer (or scroll down to the Non-Renewing Subscriptions section and click Manage, then click Create).
> - Enter a reference name for the offer. Use this reference name to manage the offer in App Store Connect. After you’ve created your offer, the reference name can't be changed.
>
> Note: You can't use a reference name that has already been used for another offer in the same app.
>
> - Select the customer eligibility for your offer, based on their In-App Purchase history within your app. You can select one or more of the following:
> - Never purchased within your app.
> - Purchased within your app in the last 30 days.
> - Purchased within your app more than 30 days ago.
>
> Selecting all of the options will make your offer available to everyone.
>
> - Click Next.
> - Select the countries or regions where you want to make your offer available, then click Next.
> - Choose Paid Offer or Free Offer.
> - Choose the discounted price for a base country or region, then click Next. To search from a larger list of price points, click See Additional Prices.
> - App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.
> - Make sure the details of your offer are correct and click Confirm.
>
> Note: Once you create an offer, you won’t be able to edit it. If changes to customer eligibility are needed, create a new offer.
>
> ### Create one-time use codes
>
> In order for customers to redeem codes, your app must be in the Ready for Distribution state.
>
> - From Apps, select your app.
> - In the sidebar, click In-App Purchases.
> - Choose the In-App Purchase you wish to create codes for.
> - Scroll down to the Offers Codes section and locate your offer in the list.
> - Click the reference name.
> - In the One-Time Use Codes section, click the Create One-Time Use Codes button.
> - Click the “Create One-Time Use Codes” button.
> - In the pop-up window, select the number of codes you want to create.
>
> You must select a minimum of 500 and a maximum of 25,000. If you need more than 25,000 codes, you can create multiple batches of codes for the same offer.
>
> - Choose an expiration date to determine how long the codes are valid. One-time use codes can be valid for a maximum of six months. Codes expire at 12:00 a.m. PT on the expiration date.
> - Click Create.
>
> It may take up to an hour before codes are redeemable by customers.
>
> ### Download one-time use codes
>
> Once your one-time use codes are created, you’ll need to download them from App Store Connect so you can share them.
>
> - From Apps, select your app.
> - In the sidebar, click In-App Purchases (or Non-renewing subscriptions).
> - Choose the In-App Purchase you wish to create codes for.
> - Scroll down to the Offers Codes section and locate your offer in the list.
> - Click the reference name.
> - Locate the codes you want to download and click Download.
> - Open the extracted text (.csv) file in a spreadsheet application.
>
> ### Create custom codes
>
> - From Apps, select your app.
> - In the sidebar, click In-App Purchases.
> - Choose the In-App Purchase you wish to create codes for.
> - Scroll down to the Offers Codes section and locate your offer in the list.
> - Click the reference name.
> - Select the offer from the list.
> - In the Custom Codes section, click the Create Custom Codes button.
> - Enter a custom code up to 64 characters and without any special characters.
> - Choose a redemption limit. This is the total number of people who can redeem this custom code. You can choose a limit of up to 25,000 at a time. If you need more, use the same custom code multiple times for the same offer.
> - Choose an expiration date to determine how long the codes will be valid (with a maximum of 6 months for codes with an expiration date). Codes expire at 12:00 a.m. PT on the expiration date.
>
> To create codes with no expiration date, choose No End Date from the date picker. Expiration dates can't be edited.
>
> Note: To extend a custom code's availability, create a new batch using the same code and a later expiration date. The system always redeems from the earliest non-expired batch first, so codes from both batches remain redeemable until each expires or reaches its redemption limit. To stop the original batch from being redeemed, deactivate it before creating the new one.
>
> - Click Create.
>
> It may take up to an hour before codes are redeemable by customers.
>
> ### Create sandbox codes
>
> Sandbox codes are one-time use codes for testing purposes. You can test offer redemptions through your sandbox account settings on iOS 16.3 and iPadOS 16.3 or later, and if your app supports the required StoreKit APIs. Learn more.
>
> - From Apps, select your app.
> - In the sidebar, click In-App Purchases (or Non-renewing subscriptions).
> - Choose the In-App Purchase you wish to create sandbox codes for.
> - Scroll down to the Offers Codes section and locate your offer in the list.
> - Click the reference name.
> - In the Sandbox Codes section, click the Create Sandbox Codes button.
> - In the pop-up window, choose the number of codes you want to create. You must select a minimum of 10 and a maximum of 10,000 codes.
> - Optionally, choose an expiration date to determine how long the codes are valid. Sandbox codes can be valid for a maximum of six months. Codes expire at 12:00 a.m PT on the expiration date.
>
> ### Deactivate offer codes
>
> - From Apps, select your app.
> - In the sidebar, click In-App Purchases.
> - Choose the In-App Purchase you wish to deactivate codes for.
> - Scroll down to the Offers Codes section and locate your offer in the list.
> - Click the reference name.
> - Locate the offer you want to deactivate and click Deactivate.
> - Click Deactivate again to proceed.
>
> The codes will expire immediately. Subscribers who have already redeemed the codes won’t be affected. Unredeemed codes will also expire and will not be reapplied to the quarterly limit.

**Applies to:** Apps that create offer codes for In-App Purchases
**Requires:** iap, subscriptions

- **[IAPX-29]** If customers are told they can redeem In-App Purchase offer codes within the app, does the app support the appropriate StoreKit method, available on iOS 16.3, macOS 15.0, or visionOS 1.0 or later?
  - quote: "Redemption within your app for one-time-use and custom codes requires customers to use a device running iOS 16.3, macOS 15.0, or visionOS 1.0 or later, and your app must support the appropriate StoreKit method."
  - surface: code
  - verify: Search the Xcode project for the StoreKit offer-code redemption API (e.g. the SwiftUI `offerCodeRedemption` modifier or `presentOfferCodeRedeemSheet`), confirm the redeem entry point is shown only on OS versions that support it (`#available` checks), and at runtime redeem a sandbox code through Sandbox Account settings.
  - fix: Implement the StoreKit offer-code redemption method behind the appropriate availability check, or remove in-app redemption claims.

## IAPX.24 Set up subscription offer codes

**Source page:** https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-subscription-offer-codes

**Source text (verbatim):**
> If you offer auto-renewable subscriptions on the App Store, you can set up offer codes to provide people with a free or discounted price for a specific duration and help you acquire, retain, and win back subscribers. You can create codes for a maximum of 1 million redemptions per app, per quarter.
>
> There are two types of offer codes:
>
> ## One-time-use codes
>
> - Unique, one-time-use codes that customers redeem through a redemption URL, by entering the code in the App Store code redemption flow, or within your app.
> - Customers are limited to redeeming one code per offer.
> - Redeemable by customers within your app if they’re using a device running iOS 14, iPadOS 14, or macOS 15, or later and your app supports the appropriate StoreKit method. Learn how to support offer codes in your app.
> - Useful for small-scale distribution or when code access needs to be restricted.
> - Each app can have up to 1 million codes per quarter, shared across all subscriptions.
> - Expire after a maximum of six months from the date they’re created.
>
> ### Custom codes
>
> - Uniquely named custom codes — for example, SPRINGPROMO — that customers redeem through a redemption URL or within your app.
> - Customers are limited to redeeming one code per offer.
> - Redeemable by customers within your app if they’re using a device running iOS 14, iPadOS 14, or macOS 15, or later and your app supports the appropriate StoreKit method. Learn how to support offer codes in your app.
> - Ideal for large campaigns that require mass distribution.
> - An expiration date isn't required for custom codes. You can optionally set a maximum redemption limit and/or expiration date.
> - Each app can have up to 1 million codes per quarter, shared across all subscriptions.
>
> Customer eligibility is determined by you in App Store Connect and can include customers with new, active, and expired subscriptions. Consider your offer’s eligibility requirements before creating and distributing offer codes.
>
> Learn about offer types and which one to choose.
>
> Get business guidance for auto-renewable subscriptions.
>
> Learn how to provide offer codes using the App Store Connect API.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> ### Set up subscription offer codes
>
> - From Apps, select your app.
> - In the sidebar, click Subscriptions.
> - Choose the subscription group containing your subscription.
> - Select the subscription from the list.
> - In the Subscription Prices section, click the add button (+).
> - From the menu, click Create Offer Codes.
> - Enter a reference name for the offer. You’ll use this reference name to manage the offer in App Store Connect and to identify sales associated with offers in Sales and Trends reports and StoreKit transactions.
> - Choose whether you'd like the subscription to automatically renew to the standard price upon conclusion of the offer period. (Checking the box will prevent auto-renewal, ensuring customers receive a commitment-free trial subscription. If you choose this option, you’ll only be able to choose Free offers).
> - Select the customer eligibility for your offer. You can select one or more of the following:
> - New subscribers: Customers who have never subscribed to any subscription product within the group.
> - Existing subscribers: Customers who are currently subscribed to a product within the group. This includes subscribers in billing retry or a grace period, as long as auto-renew remains enabled.
> - Expired subscribers: Customers who were previously subscribed to a product within the group, but whose auto-renew is turned off and subscription period has ended.
> - If your subscription has an introductory offer, determine whether people redeeming your codes should be eligible to redeem both a code and the introductory offer by choosing from the following options:
> - Yes. Eligible customers will redeem your app’s introductory offer first, then automatically renew to the offer they redeemed with the code. (If you've disabled auto-renewal, you won’t be able to choose this option).
> - No. Eligible customers will redeem the offer code first, then automatically renew to the standard subscription price without using the introductory offer. If they cancel and resubscribe at any point, they’re still eligible to redeem an introductory offer.
> - Click Next.
> - Select the countries or regions where you want to make your offer available, then click Next.
> - Choose Pay as you go, Pay up front, or Free. (If you've opted to disable auto-renewal, you'll only have the option to make your offer free.)
> - Choose the appropriate duration, and if applicable, the discounted price for a base country or region, then click Next. To search from a larger list of price points,click See Additional Prices.
>
> App Store Connect provides comparable prices for all 175 App Store countries and regions, taking into account taxes and foreign exchange rates. If you want to set different prices for specific storefronts, make the changes and click Next.
>
> - Make sure the details of your offer are correct and click Confirm.
>
> Note: Once you create an offer, you won’t be able to edit it. If changes to customer eligibility are needed, create a new offer.
>
> ### Create sandbox codes
>
> Sandbox codes are one-time use codes for testing purposes. You can test offer redemptions through your Sandbox Account settings on iOS 16.3, macOS 15.0, and visionOS 1.0 or later, and if your app supports the required StoreKit APIs. Learn how to support offer codes in your app.
>
> - From Apps, select your app.
> - In the sidebar, click subscriptions.
> - Choose the subscription group containing your subscription.
> - Select the subscription from the list.
> - Scroll down to the Offers section and locate your offer in the list.
> - Click the reference name.
> - In the Sandbox Codes section, click the Create Sandbox Codes button.
> - In the pop-up window, choose the number of codes you want to create. You must select a minimum of 10 and a maximum of 10,000 codes.
> - Choose an expiration date to determine how long the codes are valid. Sandbox codes can be valid for a maximum of six months. Codes expire at 12:00 a.m PT on the expiration date.
>
> ### Create one-time use codes
>
> In order for customers to redeem codes, your app must be in the Ready for Sale state.
>
> - From Apps, select your app.
> - In the sidebar, click subscriptions.
> - Choose the subscription group containing your subscription.
> - Click the subscription, then go to the Subscription Prices section and click View all Subscription Pricing.
> - In the menu bar, click Offer Codes.
> - Select your offer from the list.
> - Click the “Create One-Time Use Codes” button.
> - In the pop-up window, select the number of codes you want to create.
>
> You must select a minimum of 500 and a maximum of 25,000. If you need more than 25,000 codes, you can create multiple batches of codes for the same offer.
>
> - Choose an expiration date to determine how long the codes are valid. One-time use codes can be valid for a maximum of six months. Codes expire at 12:00 a.m. PT on the expiration date.
> - Click Create. It may take up to an hour before codes are redeemable by customers.
>
> ### Download one-time use codes
>
> Once your one-time use codes are created, you’ll need to download them from App Store Connect so you can share them.
>
> - From Apps, select your app.
> - In the sidebar, click subscriptions.
> - Choose the subscription group containing your subscription.
> - Click the subscription, then go to the Subscription Prices section and click View all Subscription Pricing.
> - In the menu bar, click Offer Codes.
> - Locate your offer in the list and click the reference name.
> - Locate the codes you want to download and click Download.
> - Open the extracted text (.csv) file in a spreadsheet application.
>
> ### Create custom codes
>
> Once you’ve created custom codes, you won’t be able to edit them. Custom codes can’t be used for other offer campaigns or subscriptions for the app. To create a custom code that's already being used by a different offer for the same app, you must first deactivate the code.
>
> - From Apps, select your app.
> - In the sidebar, click subscriptions.
> - Choose the subscription group containing your subscription.
> - Click the subscription, then go to the Subscription Prices section and click View all Subscription Pricing.
> - In the menu bar, click Offer Codes.
> - Select the offer from the list.
> - Click the “Create Custom Codes” button.
> - Enter a custom code up to 64 characters and without any special characters.
> - Choose a redemption limit. This is the total number of people who can redeem this custom code. You can choose a limit of up to 25,000 at a time. If you need more, use the same custom code multiple times for the same offer.
>
> Note: To extend a custom code's availability, create a new batch using the same code and a later expiration date. The system always redeems from the earliest non-expired batch first, so codes from both batches remain redeemable until each expires or reaches its redemption limit. To stop the original batch from being redeemed, deactivate it before creating the new one.
>
> - Choose an expiration date to determine how long the codes will be valid (with a maximum of 6 months for codes with an expiration date). Codes expire at 12:00 a.m. PT on the expiration date.
>
> To create codes with no expiration date, choose No End Date from the date picker. Expiration dates can't be edited.
>
> - Click Create. It may take up to an hour before codes are redeemable by customers.
>
> ### Distribute offer codes
>
> You're responsible for distributing offer codes to your customers. You can utilize your own channels, such as email or offline marketing campaigns.
>
> - Give codes to customers directly: Codes can be shared through online or offline channels. For example, you might print the codes on cards that you give out at an event. People can redeem one-time use codes by entering them in the “Redeem Gift Card or Code” page in their App Store account settings, or redeem custom codes within your app if you’ve implemented the appropriate StoreKit method. Learn more about offer codes distribution.
> - Create a unique redemption URL: Codes can be used to create redemption URLs that you can share directly. When someone visits the URL, they'll land on a page where they can redeem your code. People who haven't installed your app will first be prompted to download the app before redeeming the code.
>
> To create these URLs for one-time use codes, copy the example link from your offer details page, then add each code to the end of the URL. One-time use code URLs are also included in the downloadable text file.
>
> ### Deactivate offer codes
>
> - From Apps, select your app.
> - In the sidebar, click subscriptions.
> - Choose the subscription group containing your subscription.
> - Click a subscription, then go to the Subscription Prices section and click View all Subscription Pricing.
> - In the menu bar, click Offer Codes.
> - Click the reference name of the offer.
> - Locate the codes you want to deactivate and click Deactivate.
> - Click Deactivate again to proceed
>
> The codes will expire immediately. Subscribers who have already redeemed the codes won’t be affected. Unredeemed codes will also expire and will not be reapplied to the 1,000,000 quarterly limit.
>
> ### Deactivate offers
>
> You can have up to 10 active offers per subscription SKU at a time in App Store Connect. If you wish to deactivate an offer, please note that the offer can't be reactivated later. All codes associated with the offer will be invalidated. Subscribers who have already redeemed codes for the offer won't be affected.
>
> - From Apps, select your app.
> - In the sidebar, click subscriptions.
> - Choose the subscription group containing your subscription.
> - Click a subscription, then go to the Subscription Prices section and click View all Subscription Pricing.
> - In the menu bar, click Offer Codes.
> - Click the reference name of the offer.
> - In the upper corner, click Deactivate.
>
> You can view your deactivated offers anytime, as well as download expired codes associated with deactivated offers.

**Applies to:** Apps that set up offer codes for auto-renewable subscriptions
**Requires:** subscriptions

## IAPX.25 Overview of testing in sandbox

**Source page:** https://developer.apple.com/help/app-store-connect/test-in-app-purchases/overview-of-testing-in-sandbox

**Source text (verbatim):**
> Apple provides a sandbox environment that lets you test In-App Purchases and Apple Pay transactions using test accounts without incurring charges. This environment uses the infrastructure of the App Store and returns transactions as if payments were successfully processed instead of processing actual payments.
>
> You can test the following scenarios:
>
> | Scenario | Description |
> |---|---|
> | Testing App Store country or region | Test on different storefronts using the same Sandbox account, without having to create new testers. Associate your sandbox testers with any of the 175 App Store storefronts. |
> | Testing auto-renewable subscription events | Test auto-renewable subscription events, such as renewals, state changes, interrupted purchases, winback offers, and contingent pricing without having to wait the length of the subscription duration. |
> | Testing App Store Server Notifications | Test that your server receives App Store Server Notifications and notifications for the sandbox environment. |
> | Testing Family Sharing | Create Sandbox Test Families to test Family Sharing in your app and share access to auto-renewable subscriptions and non-consumables with up to five test family members. |
> | Testing Apple Pay transactions | Test your app's implementation of Apple Pay with test credit and debit cards. Learn more. |
>
> To get started, Create Sandbox Apple Accounts in App Store Connect and use them to sign in to devices that are running a development-signed version of your app. You’ll need to enable Developer Mode on each device so you can use it to test your app.
>
> Alternatively, you can test In-App Purchases with StoreKit Testing in Xcode, a local test environment that doesn’t require a connection to App Store servers to test In-App Purchases. Use StoreKit Testing in Xcode to test In-App Purchases before you configure them in App Store Connect or to test your code when a network connection isn’t available. Learn how to test In-App Purchases with Xcode and sandbox.

**Applies to:** Apps that offer In-App Purchases or Apple Pay
**Requires:** iap, subscriptions, apple-pay

## IAPX.26 Create a Sandbox Apple Account

**Source page:** https://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-a-sandbox-apple-account

**Source text (verbatim):**
> If your app offers In-App Purchases or Apple Pay, you can test this functionality by creating Sandbox accounts in App Store Connect and using them to sign in to devices that are running a development-signed version of your app. You’ll need to enable Developer Mode on each device so you can use it to test your app.
>
> Testing In-App Purchases and testing Apple Pay require signing into a Sandbox account in different ways:
>
> - In-App Purchases: Sign in with a Sandbox account in the App Store on your test device. You don't need to sign out of your personal Apple Account at the device level.
> - Apple Pay: Sign out of your personal Apple Account on the test device, then sign in with your Sandbox account as the device's Apple ID. For more information, visit Apple Pay Sandbox Testing.
>
> With a Sandbox account, you can test different payment scenarios (such as successful subscription renewals, payment failures, and refunds), as well as Family Sharing functionality. This is important for ensuring that In-App Purchases work as expected and that there are no issues with the payment process.
>
> You can create up to 10,000 Sandbox accounts in App Store Connect. These accounts are only valid for testing purposes and can’t be used to sign in to or make purchases on the App Store.
>
> Note: The email address you use for a Sandbox account must not already be registered as an Apple Account. Using an existing Apple Account will cause errors during testing — use an email address that isn't associated with any Apple Account. When signing in on a test device, use the Sandbox sign-in option in Settings, not your main Apple Account settings.
>
> Required role: Account Holder, Admin, App Manager, or Developer. View role permissions.
>
> ## Create a Sandbox account
>
> - Select Users and Access at the top of the page.
> - In the top navigation, click Sandbox, then click the add button (+). If it’s your first time adding sandbox testers, click Create Test Accounts.
> - Enter a first and last name for your tester.
>
> Note: Once you create a tester, you can’t edit the name, email, or password.
>
> - Enter an email address. Use an email address that hasn’t been used as Apple Account or to purchase iTunes or App Store content. Consider creating a dedicated email address for each sandbox tester.
>
> If your email service provider supports email subaddressing with a plus sign (+), you can use subaddresses of a sandbox-specific address for a sandbox tester. For example, if your base sandbox email is billjames2@icloud.com, you can use billjames2+UK@icloud.com, billjames2+US@icloud.com, and billjames2+JP@icloud.com as email addresses for additional testers. All communications sent to the subaddresses are also sent to the base address.
>
> - Enter a password. Like standard accounts, Sandbox accounts require strong passwords. When you enter a password, recommendations display if your password doesn't meet the requirements.
> - Choose an App Store country or region. Each test account is associated with one of the 175 App Store storefronts. You can edit a tester’s App Store country or region after the account is created to test on different storefronts using the same Sandbox account, without having to create new testers.
> - Click Create.
>
> ### Delete a Sandbox account
>
> You can delete a tester by clicking their Sandbox account in the list of test accounts, then clicking Delete Account. Alternatively, you can take the following steps to delete multiple testers at once.
>
> Note: Testers that are part of a Sandbox Test Family must be removed from the family before they can be deleted.
>
> - Select Users and Access at the top of the page.
> - In the top navigation, click Sandbox.
> - Select the checkbox for each tester you want to delete, then click Delete Account.
> - In the dialog that appears, click Delete Account.
>
> If you delete a sandbox tester, the associated Sandbox account and email can no longer be used as an App Store Connect user, to test in the sandbox environment, or to make purchases on the iTunes Store or App Store.

**Applies to:** Apps that offer In-App Purchases or Apple Pay
**Requires:** iap, subscriptions, apple-pay

## IAPX.27 Manage Sandbox Apple Account settings

**Source page:** https://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings

**Source text (verbatim):**
> When managing Sandbox accounts, you can choose from different In-App Purchase scenarios to ensure they work as expected.
>
> App Store Connect displays the last purchase date for active testers, or Sandbox accounts that have completed a purchase within the last 180 days. You can use filters to identify inactive testers and testers associated with a particular country or region.
>
> Required role: Account Holder, Admin, App Manager, or Developer. View role permissions.
>
> ## Edit country or region on the App Store
>
> Each test account is associated with one of the 175 App Store storefronts. You can edit a tester's App Store country or region at any time in App Store Connect to test on different App Store storefronts using the same Sandbox account, without having to create new testers.
>
> Note: All members of a Sandbox Test Family must be associated with the same App Store country or region as the family organizer. If the tester is a member of a Sandbox Test Family and you want to change their country or region, you’ll need to first remove the account from the Sandbox Test Family.
>
> - Select Users and Access at the top of the page.
> - Click Sandbox to view Sandbox accounts.
> - Click the Sandbox account you want to modify.
> - Under Country or Region, make your desired change.
> - Click Save. Once you change the country or region, the tester will need to sign in again with their Sandbox account on their iOS device to complete this change.
>
> ### Edit subscription renewal rate
>
> The subscription renewal rate is the speed at which subscriptions renew for each tester in sandbox. The subscription renewal rate also determines the length of Billing Retry and Billing Grace Period for those testers.
>
> You can change a tester’s subscription renewal rate at any time in their iOS Sandbox Account Settings or by following these steps in App Store Connect:
>
> - Select Users and Access at the top of the page.
> - Click Sandbox to view Sandbox accounts.
> - Click the Sandbox account you want to modify.
> - In the dialog that appears under Subscription Renewal Rate, select a renewal speed and click Save.
>
> By default, accounts are set to a speed equalization of 1 month = 5 minutes. You can slow down or speed up the renewal period using the options below. Subscriptions automatically renew up to 12 times before auto-renewal turns off on the thirteenth renewal attempt. Note that the speed of renewal in sandbox depends on the length of the subscription.
>
> ### Renewal every 3 minutes
>
> | Subscription duration | 1 week | 1 month | 2 months | 3 months | 6 months | 1 year |
> |---|---|---|---|---|---|---|
> | Subscription renewal speed | 3 minutes | 3 minutes | 6 minutes | 9 minutes | 18 minutes | 36 minutes |
> | Length of Billing Retry | 6 minutes | 6 minutes | 6 minutes | 6 minutes | 6 minutes | 6 minutes |
> | Length of Biling Grace Period | 3 minutes | 3 minutes | 3 minutes | 3 minutes | 3 minutes | 3 minutes |
>
> ### Renewal every 5 minutes (default)
>
> | Subscription duration | 1 week | 1 month | 2 months | 3 months | 6 months | 1 year |
> |---|---|---|---|---|---|---|
> | Subscription renewal speed | 3 minutes | 5 minutes | 10 minutes | 15 minutes | 30 minutes | 1 hour |
> | Length of Billing Retry | 10 minutes | 10 minutes | 10 minutes | 10 minutes | 10 minutes | 10 minutes |
> | Length of Biling Grace Period | 3 minutes | 5 minutes | 5 minutes | 5 minutes | 5 minutes | 5 minutes |
>
> ### Renewal every 30 minutes
>
> | Subscription duration | 1 week | 1 month | 2 months | 3 months | 6 months | 1 year |
> |---|---|---|---|---|---|---|
> | Subscription renewal speed | 10 minutes | 30 minutes | 1 hour | 1 hour 30 minutes | 3 hours | 6 hours |
> | Length of Billing Retry | 1 hour | 1 hour | 1 hour | 1 hour | 1 hour | 1 hour |
> | Length of Biling Grace Period | 10 minutes | 30 minutes | 30 minutes | 30 minutes | 30 minutes | 30 minutes |
>
> ### Renewal every hour
>
> | Subscription duration | 1 week | 1 month | 2 months | 3 months | 6 months | 1 year |
> |---|---|---|---|---|---|---|
> | Subscription renewal speed | 15 minutes | 1 hour | 2 hours | 3 hours | 6 hours | 12 hours |
> | Length of Billing Retry | 15 minutes | 1 hour | 1 hour | 1 hour | 1 hour | 1 hour |
> | Length of Biling Grace Period | 1 hour | 2 hours | 2 hours | 2 hours | 2 hours | 2 hours |
>
> ### Enable interrupted purchases for a Sandbox account
>
> You can test interrupted purchase scenarios on a device running iOS 14 or later by enabling interrupted purchases for a specific Sandbox account. An interrupted purchase is experienced anytime a customer tries to complete an App Store transaction but needs to perform an action outside of your app first. For example, they may need to agree to updated terms and conditions or update an expired payment method.
>
> You can enable or disable interrupted purchases for a tester at any time in their iOS Sandbox Account Settings or by following these steps in App Store Connect:
>
> - Select Users and Access at the top of the page.
> - Click Sandbox to view Sandbox accounts.
> - Click the Sandbox account you want to modify.
> - In the dialog that appears, select the checkbox next to “Interrupt Purchases for This Tester” to enable interrupted purchases. Deselect the checkbox to disable interrupted purchases.
> - Click Save.
>
> Once interrupted purchases are enabled, on-device purchase attempts by that Sandbox account will be interrupted in the sandbox environment and continue to be interrupted until the option is deselected or the tester agrees to terms and conditions on their iOS device.
>
> ### Clear Sandbox account purchase history
>
> You can clear the purchase history for a tester to continue testing with the same Sandbox account. Clearing purchase history deletes all past purchases made by the selected testers in the sandbox environment. This action can’t be reversed. Customer accounts aren’t affected.
>
> You can clear a tester’s purchase history at any time in their iOS Sandbox Account Settings or by following these steps in App Store Connect:
>
> - Select Users and Access at the top of the page.
> - Click Sandbox to view Sandbox accounts.
> - Select the testers you want to modify and click Clear Purchase History.
> - Click Clear Purchase History in the dialog that appears.
>
> Sandbox accounts with a high number of purchases may take longer to clear.
>
> ### Create a Sandbox Test Family
>
> Family Sharing lets people share and access auto-renewable subscriptions or non-consumables that have Family Sharing enabled with with up to five family members. You can use Sandbox Test Families to make sure Family Sharing works in your app as expected.
>
> After you’ve created at least two Sandbox accounts, you can create a Sandbox Test Family in App Store Connect.
>
> - Select Users and Access at the top of the page.
> - In the top navigation, click Sandbox, then click Family Sharing.
> - Click the add button (+) or, if it’s your first time creating a test family, click Create Test Family.
> - Select a test account to serve as the family organizer, then click Next.
> - Choose up to five test accounts to serve as family members. All members must be from the same country or region as the family organizer, and members can only belong to one Sandbox Test Family.
> - Select whether each member in the family is allowed to share and receive purchases with each other in the Share Purchases menu, then click Create.
>
> ### Manage a Sandbox Test Family
>
> You can manage a Sandbox Test Family at any time in App Store Connect. Use the following steps to add or remove test accounts serving as family members and modify whether they can share purchases.
>
> Note: Testers can also modify whether each family member shares purchases with other members of the Sandbox Test Family in their iOS Sandbox Account Settings. Learn more.
>
> - Select Users and Access at the top of the page.
> - In the top navigation, click Sandbox, then click Family Sharing.
> - Click Manage next to the Sandbox Test Family the tester is a member of.
> - Make your changes, then click Save.
>
> Note: Changes to purchase sharing may take time to appear in the sandbox environment.
>
> If a family member is removed from a Sandbox Test Family, they can no longer share their purchases or access purchases made by members of that family.
>
> ### Delete a Sandbox Test Family
>
> You can delete a Sandbox Test Family at any time in App Store Connect.
>
> Note: Members of a deleted test family will no longer be able to share their purchases or access purchases made by members of that family. Members will retain access to purchases made from their own account.
>
> - Select Users and Access at the top of the page.
> - In the top navigation, click Sandbox, then click Family Sharing.
> - Click Manage next to the Sandbox Test Family you want to delete.
> - Click Delete Test Family.
> - Click Delete in the dialog that appears.

**Applies to:** Apps that offer In-App Purchases or Apple Pay
**Requires:** iap, subscriptions, apple-pay

## Sources

- https://developer.apple.com/help/app-store-connect/
- https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase
- https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/schedule-price-changes-for-in-app-purchases
- https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-availability-for-in-app-purchases
- https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions
- https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-price-increase (404 — "The page you’re looking for can’t be found."; current page found via the help index: reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-price-increase-thresholds)
- https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-price-increase-thresholds
- https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription
- https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability/in-app-purchase-and-subscriptions-pricing-and-availability
- https://developer.apple.com/help/app-store-connect/manage-subscriptions/enable-billing-grace-period-for-auto-renewable-subscriptions
- https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-keys-for-in-app-purchases
- https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts
- https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/enter-server-urls-for-app-store-server-notifications
- https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases
- https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-localization-statuses
- https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-offer-codes-for-in-app-purchases
- https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-subscription-offer-codes
- https://developer.apple.com/help/app-store-connect/test-in-app-purchases/overview-of-testing-in-sandbox
- https://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-a-sandbox-apple-account
- https://developer.apple.com/help/app-store-connect/test-in-app-purchases/manage-sandbox-apple-account-settings
