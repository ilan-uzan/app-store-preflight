# App Store Connect — Product-Page Extras and Declarations (In-App Events, Custom Product Pages, Product Page Optimization, Asset Library, App Icon, Accessibility Nutrition Labels, Digital Goods and Services, App Tags, EULA, Regulated Medical Devices, Promo Codes, Notarization)
Source: https://developer.apple.com/help/app-store-connect/  
Retrieved: 2026-10-30

## PAGE.1 Overview of In-App Events

**Source page:** https://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events

**Source text (verbatim):**
> In-App Events, such as game competitions, movie premieres, and live-streamed experiences, are timely events within apps and games. Customers can discover these events on the App Store and Apple Games for iOS and iPadOS, providing a new way to showcase and expand their reach.
>
> On iOS 15 and iPadOS 15 and later, In-App Events appear across the App Store as event cards that include images or video, the event name, and a short description. Customers can tap to open an event details page, which provides a more immersive experience with a longer event description. It also includes information about any required In-App Purchases or subscriptions. Customers can opt in on the event card and event details page to receive a notification from the App Store when your event starts.
>
> Customers who don’t have your app or game can download it directly from your In-App Event card or event details page from the App Store. Once downloaded, they can tap Open to be seamlessly directed to the relevant section within your app or game.
>
> In-App Events appear:
>
> - On your App Store and Apple Games product page, which displays all of your currently published events.
> - In App Store and Apple Games search results. When users search for an app, the event card appears along with your app for users who have downloaded your app, while screenshots show for those who haven’t downloaded your app. Users can also search for In-App Events directly. When users search for an event, the event card appears along with your app.
> - In editorially curated selections and personalized recommendations on the Today, Games, and Apps tabs in the App Store and Apple Games.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

**Applies to:** Apps that offer In-App Events

## PAGE.2 Offer In-App Events — limits and creating an event

**Source page:** https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events

**Source text (verbatim):**
> You can publish up to 10 In-App Events on the App Store and Apple Games at a time. Additionally, you can have up to 15 approved In-App Events per app in App Store Connect at a time.
>
> In-app events must be approved before they are visible to users. Learn how to submit an In-App Event.
>
> Learn how to create a high-quality event.
>
> Learn how to create In-App Event using the App Store Connect API.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> Create an In-App Events
>
> - In the left sidebar, click In-App Events.
> - Click Create In-App Event or click the add button (+).
> - Enter a reference name. This name identifies your event in App Store Connect and is not visible on the App Store and Apple Games. Each name must be unique and can be up to 64 characters long.
> - Click Create.

**Applies to:** Apps that offer In-App Events

- **[PAGE-01]** Will no more than 10 In-App Events be published on the App Store and Apple Games at the same time once this event is approved?
  - quote: "You can publish up to 10 In-App Events on the App Store and Apple Games at a time."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > In-App Events (left sidebar): count the events whose status is published/approved and whose publish-to-end window overlaps the new event's window.
  - fix: Reschedule the new event's publish date, or end/remove an existing published event before submitting.
- **[PAGE-02]** Does the app have no more than 15 approved In-App Events in App Store Connect at a time (including the one being submitted)?
  - quote: "you can have up to 15 approved In-App Events per app in App Store Connect at a time."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > In-App Events: count events in an approved state.
  - fix: Remove/archive old approved events before submitting new ones.
- **[PAGE-03]** Is each event's reference name unique and no longer than 64 characters?
  - quote: "Each name must be unique and can be up to 64 characters long."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > In-App Events: compare the reference names in the event list; count the characters of each.
  - fix: Rename the event's reference name to a unique value of 64 characters or fewer.

## PAGE.3 Offer In-App Events — Enter event information

**Source page:** https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events

**Source text (verbatim):**
> Enter event information
>
> - In the left sidebar, click In-App Events.
> - Select your event from the list.
> - Enter an event name to appear on the App Store and Apple Games. It can be up to 30 characters.
> - Enter a short description to appear on your event card in places like the Today tab and Search on the App Store and Apple Games. It can be up to 50 characters.
> - Enter a long description that will appear on your event details page when users tap your event card. It can be up to 120 characters.
> - Upload media for your event card and event details page. Learn about the In-App Event media specifications.
>
> Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.
>
> - Choose a badge that best fits the type of event you’re offering to display above the title on the event card and event details page.
> - Add localizations for your event by choosing the primary language to display the language pop-up menu. Learn about localizing app information.

**Applies to:** Apps that offer In-App Events

- **[PAGE-04]** Is the event name (in every localization) 30 characters or fewer?
  - quote: "Enter an event name to appear on the App Store and Apple Games. It can be up to 30 characters."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > In-App Events > (event): count the characters of Event Name in each language from the language pop-up.
  - fix: Shorten the event name to 30 characters or fewer in each localization.
- **[PAGE-05]** Is the short description (in every localization) 50 characters or fewer?
  - quote: "It can be up to 50 characters."
  - surface: asc
  - verify: In-App Events > (event): count the characters of Short Description in each localization.
  - fix: Shorten the short description to 50 characters or fewer.
- **[PAGE-06]** Is the long description (in every localization) 120 characters or fewer?
  - quote: "It can be up to 120 characters."
  - surface: asc
  - verify: In-App Events > (event): count the characters of Long Description in each localization.
  - fix: Shorten the long description to 120 characters or fewer.
- **[PAGE-07]** Has media been uploaded for both the event card and the event details page?
  - quote: "Upload media for your event card and event details page."
  - surface: asc
  - verify: In-App Events > (event): confirm both the Event Card media slot and the Event Details Page media slot contain an image or video (uploaded or chosen with Browse Assets).
  - fix: Upload media matching the specifications in PAGE.10, or pick approved compatible media with Browse Assets.
- **[PAGE-08]** Has a badge been chosen for the event?
  - quote: "Choose a badge that best fits the type of event you’re offering to display above the title on the event card and event details page."
  - surface: asc
  - verify: In-App Events > (event): confirm the Badge field has a selection.
  - fix: Select the badge whose definition (PAGE.7) matches the event.

## PAGE.4 Offer In-App Events — Country or region availability and custom start dates

**Source page:** https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events

**Source text (verbatim):**
> Select country or region availability
>
> The Country or Region Availability setting controls where your event appears on the App Store and Apple Games. By default, your event is set to appear on all storefronts. However, its visibility is determined by your app’s availability in those regions. You can select the date and time your event first becomes discoverable to users, as well as the date and time the event starts and ends.
>
> - In the left sidebar, click In-App Events.
> - Select your event from the list.
> - Scroll down to the Country or Region Availability section.
> - Select start and end dates and times. You can choose any date in the future for the start date. The end date can be a maximum of 31 days from the start date. Events must be at least 15 minutes long.
>
> Note: You can have up to 10 events with overlapping start dates and times, either approved or in draft status, at the same time.
>
> - Select a publish start date and time. The publish date is when your event will become discoverable on the App Store and Apple Games and can be a maximum of 14 days in advance of the start date.
> - On the top right, click Save.
>
> Customize event start dates and times
>
> The Customize Dates and Times option allows you to select different start times in one or more countries or regions on the App Store and Apple Games. If you choose to start your event on different days in different locations, all of your event start dates must be within 48 hours of each other.
>
> - In the left sidebar, click In-App Events.
> - Select your event from the list.
> - In the Country or Region Availability section, click Customize Dates and Times.
> - Select the locations you want to edit, and click Next.
> - Enter the start date and time. Use the Time Zone toggle on the top right to choose a timezone.
> - Click Done.
> - To customize more regions, click the add button (+) next to Customize Dates and Times.
> - Select the locations you want to edit, and click Next.
> - Enter the start date and time.
> - Click Done.

**Applies to:** Apps that offer In-App Events

- **[PAGE-09]** Is the event's end date no more than 31 days after its start date, and does the event last at least 15 minutes?
  - quote: "The end date can be a maximum of 31 days from the start date. Events must be at least 15 minutes long."
  - surface: asc
  - verify: In-App Events > (event) > Country or Region Availability: compare the start and end dates/times.
  - fix: Adjust the start/end dates so the event lasts between 15 minutes and 31 days.
- **[PAGE-10]** Are there no more than 10 events (approved or draft) with overlapping start dates and times?
  - quote: "You can have up to 10 events with overlapping start dates and times, either approved or in draft status, at the same time."
  - surface: asc
  - verify: In-App Events list: compare start/end dates of all approved and draft events.
  - fix: Reschedule or delete drafts so no more than 10 overlap.
- **[PAGE-11]** Is the publish start date no more than 14 days before the event start date?
  - quote: "The publish date is when your event will become discoverable on the App Store and Apple Games and can be a maximum of 14 days in advance of the start date."
  - surface: asc
  - verify: In-App Events > (event) > Country or Region Availability: compare the publish start date with the event start date.
  - fix: Move the publish date to within 14 days of the start date.
- **[PAGE-12]** If start dates are customized per country or region, are all start dates within 48 hours of each other?
  - quote: "all of your event start dates must be within 48 hours of each other."
  - surface: asc
  - verify: In-App Events > (event) > Country or Region Availability > Customize Dates and Times: list each region's start date/time (normalize time zones) and compute the spread.
  - fix: Change the customized start times so the earliest and latest are no more than 48 hours apart.

## PAGE.5 Offer In-App Events — Add additional information

**Source page:** https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events

**Source text (verbatim):**
> Add additional information
>
> - Provide an event deep link. This link takes users who tap Open on the In-App Event card or details page to the event content within your app. This can be a universal link (recommended for security) or custom URL. Avoid using URL shorteners and other services that add unnecessary redirects. Test the deep link to make sure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it. Learn about configuring universal links.
> - Select the general purpose of your event to help make sure your event reaches the most relevant users on the App Store and Apple Games.
> - Select the priority for your event. Events appear chronologically on the product page based on start time, with the soonest start time displaying first. If you designate an event as High Priority, it will appear ahead of Normal Priority events.
> - Indicate if an In-App Purchase is required to participate in the event, as this information is shown on your event details page. For subscription apps, you only need to indicate that an In-App Purchase is required when there’s an additional cost for the event specifically — for example, a pay-per-view event in a subscription app that requires an In-App Purchase in addition to the standard subscription.
> - Choose your event’s primary language. This will be the default language that displays to users if your event isn’t localized for their device’s language.

**Applies to:** Apps that offer In-App Events

- **[PAGE-13]** Does the event deep link open the event content inside the app (tested on a device)?
  - quote: "Test the deep link to make sure it directs to the proper destination within your app"
  - surface: runtime
  - verify: Copy the Event Deep Link from In-App Events > (event); on a device with the build installed, paste it into Notes and tap it; confirm it opens the event screen. In the Xcode project, confirm the URL scheme (Info.plist CFBundleURLTypes) or Associated Domains entitlement (applinks:) that the link relies on is present and handled in the app's URL/user-activity handler.
  - fix: Correct the deep link URL, or add/repair universal link (apple-app-site-association + Associated Domains) or custom URL scheme handling in the app.
- **[PAGE-14]** Is the deep link free of URL shorteners and redirect services? (advisory)
  - quote: "Avoid using URL shorteners and other services that add unnecessary redirects."
  - surface: asc
  - verify: Inspect the Event Deep Link value; resolve it with curl -sI and check for redirects or a shortener domain.
  - fix: Replace it with the direct universal link or custom URL.
- **[PAGE-15]** Does the "In-App Purchase required" setting reflect reality (for subscription apps, only when the event has an additional cost beyond the standard subscription)?
  - quote: "Indicate if an In-App Purchase is required to participate in the event, as this information is shown on your event details page."
  - surface: asc
  - verify: In-App Events > (event): read the purchase-required setting; compare with how the event is gated in the app (StoreKit product IDs checked on the event screen).
  - fix: Set the purchase-required option to match the event's actual access requirements.

## PAGE.6 In-App Events (App Store marketing page) — Configuring in App Store Connect

**Source page:** https://developer.apple.com/app-store/in-app-events/

**Source text (verbatim):**
> In-App Events are easy to set up and manage in App Store Connect. When creating an event, you’ll enter a reference name (visible only in App Store Connect) and event information, including metadata. You’ll also select an event badge and regional availability. You can submit events for review independent of a new app version and have up to 15 approved events in App Store Connect at a time. You can also use the App Store Connect API to automate metadata upload and submission for your events. An app can have up to 10 events published on the App Store at a time.
>
> Good candidates for In‑App Events are challenges, competitions, or special content launches.
>
> The following are not good candidates for In‑App Events:
>
> - Repetitive activities such as daily tasks or rewards.
>
> - Price promotions that don’t introduce any new content, features, or goods.
>
> - General promotions that raise awareness about your app or game. While an In-App Event can highlight added content or features that are permanent or ongoing, the event itself should focus on a related limited-time moment or experience.

**Applies to:** Apps that offer In-App Events

- **[PAGE-16]** Is the event something other than a repetitive activity such as a daily task or reward? (advisory)
  - quote: "Repetitive activities such as daily tasks or rewards."
  - surface: manual
  - verify: Read the event name, descriptions and badge in In-App Events > (event); compare with the app's recurring features.
  - fix: manual — requires developer decision/legal/business action (choose a different, limited-time event).
- **[PAGE-17]** Does the event introduce new content, features, or goods rather than being only a price promotion? (advisory)
  - quote: "Price promotions that don’t introduce any new content, features, or goods."
  - surface: manual
  - verify: Read the event metadata and compare with what changes in the app during the event window.
  - fix: manual — requires developer decision/legal/business action.
- **[PAGE-18]** Does the event focus on a limited-time moment or experience rather than general promotion of the app? (advisory)
  - quote: "the event itself should focus on a related limited-time moment or experience."
  - surface: manual
  - verify: Read the event name/descriptions: they should describe a specific time-bound happening, not the app in general.
  - fix: Rewrite the event around a specific limited-time moment, or don't submit it as an In-App Event.

## PAGE.7 In-App Events (App Store marketing page) — Choosing an event badge

**Source page:** https://developer.apple.com/app-store/in-app-events/

**Source text (verbatim):**
> Select the badge that best fits the type of event you’re offering to display above the title on the In-App Event card and event details page.
>
> - Challenge: Activities encouraging the user to achieve a goal before the event ends — for example, a fitness challenge in a workout app or beating a certain number of levels in a game.
>
> - Competition: Activities in which users compete against one another for the highest ranking or to win rewards — for example, a tournament where players battle to win the most matches.
>
> - Live Event: Activities that occur in real-time that all users can experience simultaneously — for example, a sports match or livestreamed concert. These events should provide users with new content, features, or goods.
>
> - Major Update: Introducing significant new features, content, or experiences – for example, the launch of new game modes or levels. These events go beyond minor enhancements like UI adjustments or bug fixes.
>
> - New Season: Introducing new content, storylines, or media libraries to build on established content. For example, a significant sporting event, a battle pass or themed content in a game, or a special episode of a television show. These events should focus on unique content rather than promoting awareness about the entirety of the season.
>
> - Premiere: Introducing new content or media for the first time — for example, a movie debut or newly released audio. These events should focus on the introduction of this unique content, rather than promoting general awareness about your app’s content or service.
>
> - Special Event: Limited-time events that are not captured by another event badge, possibly spanning multiple activities or experiences — for example, an event featuring a collaboration. These events should provide users with new content, features, or goods.

**Applies to:** Apps that offer In-App Events

- **[PAGE-19]** Does the selected badge match Apple's definition of that badge for this event?
  - quote: "Select the badge that best fits the type of event you’re offering"
  - surface: manual
  - verify: Compare the badge selected in In-App Events > (event) with the definitions quoted above.
  - fix: Choose the badge whose definition matches the event.
- **[PAGE-20]** If the badge is Major Update, does the event introduce significant new features, content, or experiences (not UI adjustments or bug fixes)?
  - quote: "These events go beyond minor enhancements like UI adjustments or bug fixes."
  - surface: manual
  - verify: Compare the event description with the release notes / changes in the associated build.
  - fix: Choose another badge or don't use an event for minor changes.
- **[PAGE-21]** If the badge is Live Event or Special Event, does the event provide users with new content, features, or goods?
  - quote: "These events should provide users with new content, features, or goods."
  - surface: manual
  - verify: Read the event metadata and check what new content the app delivers during the event.
  - fix: manual — requires developer decision/legal/business action.

## PAGE.8 In-App Events (App Store marketing page) — Creating effective metadata

**Source page:** https://developer.apple.com/app-store/in-app-events/

**Source text (verbatim):**
> The metadata you provide is used when displaying your event across the App Store. To ensure a smooth review experience, make sure it accurately portrays your event and is specific to the event experience, rather than sharing general information about your app or promoting its content or services. You’ll enter the following:
>
> Event name: Choose a distinctive, unique name that’s up to 30 characters long and written in title case. This should be the actual name of the event, such as “June Leaderboard Climb,” rather than a call to action or tagline, such as “Watch the livestream.” Avoid generic terms or describing the type of event, since the event badge already displays this information.
>
> Short description: Briefly summarize your In-App Event in up to 50 characters written in sentence case. This information displays on your event card.
>
> Long description: Provide more information about your event — such as potential rewards — in up to 120 characters written in sentence case. This information displays on your event details page.
>
> Event card and event details media: Add an image or video that represents your In-App Event across the App Store. Videos autoplay and repeat, so aim to create a seamless loop. In App Store Connect, you can preview what your provided media will look like in an event card and event details page to confirm that crucial aspects of your image or video will not be obscured.
>
> To ensure your events display properly on the App Store and provide a high-quality user experience, consider these guidelines when creating your metadata:
>
> - Use proper capitalization and punctuation. Avoid using all capitals and don’t use excessive punctuation marks, such as multiple exclamation points.
>
> - Avoid claims that can’t be verified, such as “the best” or “#1,” as well as extra words, such as “game event.”
>
> - Don’t include specific prices in your metadata, as pricing and currencies can vary across regions and can be changed independent of your event. Including specific pricing will lead to rejection by App Review.
>
> - When possible, avoid using text or logos in your media, especially if they include your event name or app name.
>
> - Consider using video in order to provide users with a more dynamic preview of your event.
>
> - Don’t add borders or gradients to your media. Crops and gradients are automatically applied to your media in order to ensure consistency across the App Store.
>
> - Aim to create visual continuity across your event card and event details page by using similar colors or illustration styles.
>
> - Make sure your metadata includes content that you created or have a license to use.

**Applies to:** Apps that offer In-App Events

- **[PAGE-22]** Is the event metadata specific to the event experience, rather than general information about or promotion of the app?
  - quote: "make sure it accurately portrays your event and is specific to the event experience, rather than sharing general information about your app or promoting its content or services."
  - surface: asc
  - verify: Read Event Name, Short Description and Long Description in every localization.
  - fix: Rewrite the metadata to describe only the event.
- **[PAGE-23]** Is the event name the actual name of the event, written in title case, and not a call to action or tagline?
  - quote: "Choose a distinctive, unique name that’s up to 30 characters long and written in title case." ... "This should be the actual name of the event, such as “June Leaderboard Climb,” rather than a call to action or tagline"
  - surface: asc
  - verify: Read Event Name in each localization; check capitalization and that it is not an imperative phrase such as a call to action.
  - fix: Replace with the event's actual name in title case.
- **[PAGE-24]** Does the event name avoid generic terms and avoid describing the event type? (advisory)
  - quote: "Avoid generic terms or describing the type of event, since the event badge already displays this information."
  - surface: asc
  - verify: Read Event Name; flag words that just restate the badge (e.g., the badge name) or generic terms.
  - fix: Remove the generic/type words from the name.
- **[PAGE-25]** Are the short and long descriptions written in sentence case?
  - quote: "Briefly summarize your In-App Event in up to 50 characters written in sentence case." ... "in up to 120 characters written in sentence case."
  - surface: asc
  - verify: Read Short Description and Long Description in every localization and check capitalization.
  - fix: Rewrite in sentence case.
- **[PAGE-26]** Does the metadata avoid all capitals and excessive punctuation such as multiple exclamation points? (advisory)
  - quote: "Avoid using all capitals and don’t use excessive punctuation marks, such as multiple exclamation points."
  - surface: asc
  - verify: Scan all event text fields for ALL-CAPS words and repeated punctuation (e.g., "!!").
  - fix: Use proper capitalization and single punctuation marks.
- **[PAGE-27]** Does the metadata avoid unverifiable claims and extra words? (advisory)
  - quote: "Avoid claims that can’t be verified, such as “the best” or “#1,” as well as extra words, such as “game event.”"
  - surface: asc
  - verify: Scan event text fields for superlatives/rank claims and filler words.
  - fix: Remove the unverifiable claims and extra words.
- **[PAGE-28]** Does the event metadata contain no specific prices?
  - quote: "Including specific pricing will lead to rejection by App Review."
  - surface: asc
  - verify: Scan Event Name, Short Description, Long Description (all localizations) and the event media for currency symbols, amounts, or prices.
  - fix: Remove all specific prices from text and media.
- **[PAGE-29]** Does the event media avoid text and logos, especially the event name or app name? (advisory)
  - quote: "When possible, avoid using text or logos in your media, especially if they include your event name or app name."
  - surface: manual
  - verify: View the event card and event details media in In-App Events > (event) preview.
  - fix: Replace with media without overlaid text/logos.
- **[PAGE-30]** Is the event media free of added borders and gradients?
  - quote: "Don’t add borders or gradients to your media."
  - surface: manual
  - verify: View the event card and details media files.
  - fix: Re-export the media without borders or gradients.
- **[PAGE-31]** Is all event metadata and media content that the developer created or has a license to use?
  - quote: "Make sure your metadata includes content that you created or have a license to use."
  - surface: manual
  - verify: Ask the developer for the source/licence of every image, video, music track and trademark in the event media and text.
  - fix: manual — requires developer decision/legal/business action.

## PAGE.9 In-App Events (App Store marketing page) — Adding event details

**Source page:** https://developer.apple.com/app-store/in-app-events/

**Source text (verbatim):**
> When configuring your event, you’ll also add additional event details that impact how your In-App Event displays on the App Store.
>
> Determine event availability. When you select start and end dates and times for your In-App Event, you’ll also choose the date and time it appears on the App Store. An In-App Event can last up to 31 days and be promoted up to 14 days before its start date. If you’d like, you can make your event available only in specific regions and customize the dates and times for each location.
>
> Provide an event deep link. This link takes users who tap Open on the In-App Event card or details page to the event content within your app. This can be a universal link (recommended for security) or custom URL. Avoid using URL shorteners and other services that add unnecessary redirects. Test the deep link to make sure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it. Learn about configuring universal links.
>
> Be thoughtful about the most relevant destination to direct users. If your event is live, you can link directly to the event. If your event hasn’t started, you might direct users to a landing page that builds anticipation and reminds them when to return. If a user is new to your app, consider taking them through any necessary onboarding before directing them to the event. Always provide a way for users to return to your main app experience.
>
> Indicate your event purpose. Offering In‑App Events in your app or game can encourage new users to try it, provide existing users with new ways to enjoy your app, and give former users reasons to return. Many In‑App Events are appropriate for all of these purposes, but you may create In‑App Events that are primarily intended for one of these reasons. Choose the option that best fits your event’s purpose:
>
> - Appropriate for all users
>
> - Attract new users: New users are people who have never downloaded your app
>
> - Keep active users informed: Active users are people who downloaded your app and have opened it recently
>
> - Bring back lapsed users: Lapsed users are people who downloaded your app but have not opened it recently
>
> This selection is one of the factors that the App Store uses to offer personalized recommendations and doesn’t display on your event card or event details page. To help your event reach the people it’s intended for, the App Store incorporates app usage information. This data is processed on the device to minimize data collection and enhance user privacy. Regardless of the event purpose you choose, your published events are discoverable on the App Store by all customers.
>
> Designate event priority. Events appear on your product page chronologically based on start time, with the soonest start time displaying first. Any events you select as high priority will appear ahead of normal priority events.
>
> Select cost. Indicate if a specific Apple In-App Purchase is required to participate in the event, as this information is shown on your event details page. For subscription apps, you only need to indicate that an Apple In-App Purchase is required when there’s an additional cost for the event specifically — for example, a pay-per-view event in a subscription app that requires an Apple In-App Purchase in addition to the standard subscription.

**Applies to:** Apps that offer In-App Events

- **[PAGE-32]** From the screen the event deep link opens, can the user get back to the main app experience?
  - quote: "Always provide a way for users to return to your main app experience."
  - surface: runtime
  - verify: Open the event deep link on a device (fresh install and existing install) and confirm a back/close/tab navigation path to the app's main UI exists.
  - fix: Add navigation from the event destination to the main app UI.

## PAGE.10 In-App Event media and audio specifications

**Source page:** https://developer.apple.com/help/app-store-connect/reference/in-app-events/in-app-event-media-and-audio-specifications

**Source text (verbatim):**
> Note: Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation.
>
> | Media Type | Supported Extensions | Aspect Ratio | Min Resolution/Frame Rate | Max Resolution/Frame Rate | Max File Size |
> |---|---|---|---|---|---|
> | Event Card Image | .jpg, .jpeg, .png | 16 : 9 | 1920x1080 px | 3840x2160 px | 500MB |
> | Event Card Video | .mov, .m4v, .mp4 | 16 : 9 | 1920x1080 px<br>30 fps or 60 fps | 3840x2160 px<br>30 fps or 60 fps | 500MB |
> | Event Details Page Image | .jpg, .jpeg, .png | 9 : 16 | 1080x1920 px | 2160x3840 px | 500MB |
> | Event Details Page Video | .mov, .m4v, .mp4 | 9 : 16 | 1080x1920 px<br>30 fps or 60 fps | 2160x3840 px<br>30 fps or 60 fps | 500MB |
>
> Audio specifications
>
> Audio specifications
>
> Event Card Video:
>
> - Stereo
> - Codec: 256kbps AAC
> - Sample Rate: 44.1kHz or 48kHz
> - Tracks without audio are supported
>
> Event Details Page Video:
>
> - Stereo
> - Codec: PCM or 256kbps AAC
> - Bit Depth (for PCM): 16-, 24-, or 32-bit
> - Sample Rate: 44.1 or 48kHz
> - Tracks without audio are supported
>
> Stereo configuration:
>
> - 1 track with 2-channel stereo (1st channel L and 2nd channel R)
> - 2 tracks with 1-channel stereo (1st track L and 2nd track R)
>
> Stereo configuration:
>
> - 1 track with 2-channel stereo (1st channel L and 2nd channel R)
> - 2 tracks with 1-channel stereo (1st track L and 2nd track R)

**Applies to:** Apps that offer In-App Events

- **[PAGE-33]** Is the event card media landscape (16:9) and the event details media portrait (9:16)?
  - quote: "Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation."
  - surface: manual
  - verify: Check the pixel dimensions of each media file (e.g., sips -g pixelWidth -g pixelHeight <file> for images; ffprobe/mdls for video).
  - fix: Re-export the card media at 16:9 landscape and the details media at 9:16 portrait.
- **[PAGE-34]** Is the event card image/video between 1920x1080 px and 3840x2160 px, in .jpg/.jpeg/.png (image) or .mov/.m4v/.mp4 (video)?
  - quote: "Event Card Image | .jpg, .jpeg, .png | 16 : 9 | 1920x1080 px | 3840x2160 px"
  - surface: manual
  - verify: Inspect the card media file's extension and pixel dimensions.
  - fix: Re-export within the stated minimum/maximum resolution and a supported extension.
- **[PAGE-35]** Is the event details page image/video between 1080x1920 px and 2160x3840 px, in a supported extension?
  - quote: "Event Details Page Image | .jpg, .jpeg, .png | 9 : 16 | 1080x1920 px | 2160x3840 px"
  - surface: manual
  - verify: Inspect the details media file's extension and pixel dimensions.
  - fix: Re-export within the stated resolution range.
- **[PAGE-36]** Are event videos 30 fps or 60 fps and every media file 500MB or smaller?
  - quote: "30 fps or 60 fps" ... "500MB"
  - surface: manual
  - verify: Check frame rate (ffprobe or QuickTime Inspector) and file size (ls -l) of each event media file.
  - fix: Re-encode at 30 or 60 fps and reduce file size to 500MB or less.
- **[PAGE-37]** Does event card video audio (if present) use stereo, 256kbps AAC, 44.1kHz or 48kHz?
  - quote: "Codec: 256kbps AAC" ... "Sample Rate: 44.1kHz or 48kHz"
  - surface: manual
  - verify: Inspect the card video's audio track (ffprobe: codec, bitrate, sample rate, channels).
  - fix: Re-encode audio to stereo 256kbps AAC at 44.1 or 48kHz, or remove the audio track.
- **[PAGE-38]** Does event details page video audio (if present) use stereo, PCM (16/24/32-bit) or 256kbps AAC, 44.1 or 48kHz?
  - quote: "Codec: PCM or 256kbps AAC" ... "Bit Depth (for PCM): 16-, 24-, or 32-bit" ... "Sample Rate: 44.1 or 48kHz"
  - surface: manual
  - verify: Inspect the details video's audio track with ffprobe.
  - fix: Re-encode audio to a supported codec/sample rate, or remove the audio track.

## PAGE.11 Submit an In-App Event

**Source page:** https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-event

**Source text (verbatim):**
> Before publishing your In-App Event on the App Store, submit your event details and media for review, ensuring all required information is complete. If you want to submit an In-App Event and your app hasn’t been approved yet, include the In-App Event in the same submission as your first iOS app version. If your app is already approved, you can choose to submit an In-App Event with or without an iOS app version. You can also add other items to a submission.
>
> You can publish up to 10 In-App Events on the App Store and Apple Games at a time. Additionally, you can have up to 15 approved In-App Events per app in App Store Connect at a time.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click In-App Events.
> - Select your event from the list.
> - On the top right, click Add for Review and select whether to add the In-App Event to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version. The In-App Event status changes to Ready for Review.
>
> If you’re submitting the In-App Event for review with an app version, it will be reviewed together with that app version.
>
> If you’re submitting the In-App Event for review without an app version, select a platform in the draft submission screen. The In-App Event will be reviewed together with the latest version of the selected platform.
>
> You may choose to add other items to the submission.
>
> Note: Users with the marketing role can’t add app versions to a submission.
>
> - Click Submit for Review. The In-App Event status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about item statuses.

**Applies to:** Apps that offer In-App Events

- **[PAGE-39]** Is all required information for the event complete before it is submitted?
  - quote: "submit your event details and media for review, ensuring all required information is complete."
  - surface: asc
  - verify: In-App Events > (event): confirm reference name, event name, short and long descriptions, card and details media, badge, availability dates, deep link, purpose, priority, In-App Purchase setting, and primary language are all filled in.
  - fix: Complete the missing fields (see PAGE.3–PAGE.5).
- **[PAGE-40]** If the app has not been approved yet, is the In-App Event included in the same submission as the first iOS app version?
  - quote: "include the In-App Event in the same submission as your first iOS app version."
  - surface: asc
  - verify: App Review section / draft submission: confirm the event and the first iOS version are items of the same submission.
  - fix: Add the event to the draft submission that contains the first iOS version.
- **[PAGE-41]** If the submission must include an app version, is it being submitted by a user whose role is not Marketing?
  - quote: "Users with the marketing role can’t add app versions to a submission."
  - surface: asc
  - verify: Users and Access: check the submitting user's role.
  - fix: Have an Account Holder, Admin, or App Manager add the version to the submission.

## PAGE.12 Configure multiple product page versions (custom product pages)

**Source page:** https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions

**Source text (verbatim):**
> Create up to 70 custom product pages per app on the App Store to highlight features or specific content. Each custom product page can include different screenshots, previews, promotional text, and keywords, and is localizable and shareable through a unique URL.
>
> Custom product pages must be approved before they are visible to users. Learn how to submit a custom product page.
>
> Custom product pages are available on the App Store on iOS 15 and iPadOS 15, or later. Custom product pages are only visible to people if they follow a custom product page link, or if you choose to make your custom product page visible in App Store search results by adding keywords. Otherwise, your app’s default product page displays to all customers on the App Store.
>
> In App Analytics, view App Store metrics such as impressions, downloads, and conversion rate for each page. The metrics are available after a custom product page receives at least five first-time downloads. Learn more about data in App Analytics.
>
> You can optionally add an app deep link to your custom product page. When users running a minimum of iOS 18 or iPadOS 18 click Open on your custom product page, the app deep link directs them to specific content in your app.
>
> - An app deep link can be a universal link or custom URL. Use universal links for app deep links to provide users with a secure and integrated mobile experience. Learn about configuring universal links.
> - Avoid using URL shorteners and other services that add unnecessary redirects.
> - Test the deep link to ensure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it.
> - Your app deep link must be approved before it'll function for users. Submit your custom product page for review after you add a deep link in App Store Connect.
>
> Learn how to create and manage a custom product page using the App Store Connect API.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

**Applies to:** Apps that use custom product pages

- **[PAGE-42]** Does the app have no more than 70 custom product pages?
  - quote: "Create up to 70 custom product pages per app on the App Store"
  - surface: asc
  - verify: App Store Connect > Apps > (app) > Custom Product Pages: count the pages.
  - fix: Delete unused custom product pages.
- **[PAGE-43]** If a custom product page has an app deep link, does it open the intended content in the app (tested on a device)?
  - quote: "Test the deep link to ensure it directs to the proper destination within your app"
  - surface: runtime
  - verify: Copy the deep link from Custom Product Pages > (page); paste into Notes on a device with the build installed and tap it. In Xcode, confirm the Associated Domains entitlement (applinks:) or CFBundleURLTypes entry needed by the link, and the handler code.
  - fix: Correct the deep link or implement its handling in the app.
- **[PAGE-44]** If a deep link was added or changed, has the custom product page been submitted for review afterwards?
  - quote: "Your app deep link must be approved before it'll function for users."
  - surface: asc
  - verify: Custom Product Pages > (page): check the page status after the deep link edit (Ready for Review / Waiting for Review / approved).
  - fix: Submit the custom product page for review (PAGE.16).

## PAGE.13 Create a custom product page

**Source page:** https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions

**Source text (verbatim):**
> You can create a custom product page if your app has the Ready for Distribution status in at least one country or region.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Custom Product Pages.
> - Click Create Custom Product Page.
>
> If there’s an existing custom product page, click add button (+).
>
> - Enter a reference name to help you identify the page in App Analytics.
> - Choose whether to start with a blank page or make changes to an existing App Store product page. If you choose to start from an existing page, you can choose a version that’s in the Ready for Distribution state or the Prepare for Submission state and it’ll copy the product page for your primary localization.
> - Click Create. Your custom product page’s unique URL is automatically generated and displays on this page.
> - Modify or add additional screenshots, app previews, promotional text, or keywords.
>
> Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.
>
> You can optionally add an app deep link to direct users running a minimum of iOS 18 or iPadOS 18 to specific content in your app.

**Applies to:** Apps that use custom product pages

- **[PAGE-45]** Does the app have the Ready for Distribution status in at least one country or region before custom product pages are created?
  - quote: "You can create a custom product page if your app has the Ready for Distribution status in at least one country or region."
  - surface: asc
  - verify: App Store Connect > Apps > (app): check the app's current version status.
  - fix: manual — requires developer decision/legal/business action (release a version first).

## PAGE.14 Enable keywords for a custom product page

**Source page:** https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions

**Source text (verbatim):**
> You can assign keywords from your latest approved app version to a custom product page. This directs customers to your custom product page when they search those keywords, rather than your default product page. You can assign keywords in App Store Connect at any time, but the custom product page is searchable only after it’s approved and set to visible.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Custom Product Pages.
> - Click the custom product page you want to assign keywords to.
> - In the Keywords section, select the keywords for this custom product page.
>
> Repeat this as necessary for each localization.
>
> - Click Publish.
>
> Tip: To ensure the most relevant custom product page appears, select a unique set of keywords for each page.
>
> After assigning keywords to your custom product page, you can disable them individually.

**Applies to:** Custom product pages that use keywords

- **[PAGE-46]** Are the keywords assigned to the custom product page taken from the latest approved app version, and selected in each localization?
  - quote: "You can assign keywords from your latest approved app version to a custom product page."
  - surface: asc
  - verify: Custom Product Pages > (page) > Keywords section: check selections per localization against the approved version's Keywords field.
  - fix: Select the keywords per localization, then click Publish.
- **[PAGE-47]** Does each custom product page use a set of keywords distinct from other pages? (advisory)
  - quote: "To ensure the most relevant custom product page appears, select a unique set of keywords for each page."
  - surface: asc
  - verify: Compare Keywords selections across all custom product pages.
  - fix: Reassign overlapping keywords so each page has a unique set.
- **[PAGE-153]** If the custom product page should appear in App Store search for its keywords, has it been approved and set to visible?
  - quote: "the custom product page is searchable only after it’s approved and set to visible."
  - surface: asc
  - verify: Custom Product Pages > (page): check the page is approved and its keywords were published (Publish clicked) and the page is visible.
  - fix: Submit the page for review (PAGE.16), then set it to visible and click Publish in the Keywords section.

## PAGE.15 Edit, disable, or delete a custom product page

**Source page:** https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions

**Source text (verbatim):**
> An approved custom product page can be edited and submitted for review without affecting its unique URL. Changes are published automatically upon approval by App Review.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Custom Product Pages.
> - Click the page you want to edit.
> - Click Create New Version.
> - Review the prompt and click Create again to proceed. This creates a new draft of your custom product page in the Ready to Submit state.
> - Make your edits and click Add for Review.
>
> The submission confirmation screen displays the app version that’ll be associated with the custom product page, and the items that’ll be reviewed. You may choose to add other items to the submission.
>
> - Click Submit to App Review.
>
> Once the edited page is approved, it will replace the current page on the App Store.
>
> Disable a custom product page
>
> You can disable a custom product page at any time. If someone selects a URL for a disabled custom product page, they’re automatically redirected to your default product page.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Custom Product Pages.
> - Click the page you want to disable.
> - Under the Product Page URL, click Disable Link.
>
> For a disabled link, Enable Link will display instead.
>
> - Click Disable.
>
> Delete a custom product page
>
> You can delete a custom product page at any time. If someone selects a URL for a deleted custom product page, they’re automatically redirected to your default product page. This action is permanent.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Custom Product Pages.
> - Click the page you want to delete.
> - Scroll to the bottom and click Delete This Product Page.

**Applies to:** Apps that use custom product pages

## PAGE.16 Submit a custom product page

**Source page:** https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-a-custom-product-page

**Source text (verbatim):**
> Custom product pages, and their associated metadata like deep links, must be reviewed before they’re visible to users on the App Store.
>
> If you want to submit a custom product page and your app hasn’t been approved yet, include the custom product page in the same submission as your first iOS app version. If your app is already approved, you can choose to submit a custom product page with or without an iOS app version. You can also add other items to a submission.
>
> Learn how to submit using the App Store Connect API.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Custom Product Pages.
> - Click the page you want to submit for review.
> - On the top right, click Add for Review and select whether to add the custom product page to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version. The custom product page status changes to Ready for Review.
>
> You may choose to add other items to the submission.
>
> Note: Users with the marketing role can’t add app versions to a submission.
>
> - Click Submit for Review. The custom product page status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about item statuses.
>
> You can’t modify a custom product page's screenshots, previews, promotional text, or keywords, while it's under review. Withdrawing the submission makes the page editable, so you can make changes and resubmit.
>
> After an app submission is approved, users can access the custom product page URL.

**Applies to:** Apps that use custom product pages

- **[PAGE-48]** Has every custom product page that should be visible (including its deep link) been submitted to App Review?
  - quote: "Custom product pages, and their associated metadata like deep links, must be reviewed before they’re visible to users on the App Store."
  - surface: asc
  - verify: Custom Product Pages list: check each page's status (not left in Prepare for Submission / Ready to Submit when it is meant to go live).
  - fix: Add the page for review and click Submit for Review.
- **[PAGE-49]** If the app hasn't been approved yet, is the custom product page in the same submission as the first iOS app version?
  - quote: "include the custom product page in the same submission as your first iOS app version."
  - surface: asc
  - verify: App Review section / draft submission: confirm both items are in one submission.
  - fix: Add the custom product page to the draft submission containing the first iOS version.
- **[PAGE-50]** Are all intended screenshot, preview, promotional text, and keyword changes made before submitting the custom product page?
  - quote: "You can’t modify a custom product page's screenshots, previews, promotional text, or keywords, while it's under review."
  - surface: asc
  - verify: Review the page's screenshots, previews, promotional text and keywords before clicking Submit for Review.
  - fix: Finish edits first; if already submitted, withdraw the submission, edit, and resubmit.

## PAGE.17 Overview of product page optimization

**Source page:** https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization

**Source text (verbatim):**
> Optimize your iOS or iPadOS app's product page on the App Store by testing up to three different app icons, screenshots, and previews to see which resonate best with customers. Each variant will be randomly shown to a user group you define, and can be localized in any language your app supports. Use App Analytics to evaluate performance and feature the top-performing assets to all users.
>
> The methodology for determining the treatment that’s best at driving app engagement is based on the estimated lift in conversion rate, as well as algorithms that provide confidence in the reliability of the test results. Learn how to view product page optimization results.
>
> Note: Your app must be in the Ready for Distribution state to test its product page. Releasing a new app version while a test is in progress may impact the results if your version contains assets or metadata that are currently being tested. Product page optimization tests aren't available for custom product pages or for product pages on the App Store for Apple Watch or iMessage.
>
> Treatments are shown to users on the App Store on iOS 15 and iPadOS 15, or later.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

**Applies to:** iOS or iPadOS apps that run product page optimization tests

- **[PAGE-51]** Is the app in the Ready for Distribution state before a product page optimization test is set up?
  - quote: "Your app must be in the Ready for Distribution state to test its product page."
  - surface: asc
  - verify: App Store Connect > Apps > (app): check the live version's status.
  - fix: manual — requires developer decision/legal/business action (release a version first).
- **[PAGE-52]** Does the planned app version release avoid changing assets or metadata that are being tested in a running test? (advisory)
  - quote: "Releasing a new app version while a test is in progress may impact the results if your version contains assets or metadata that are currently being tested."
  - surface: asc
  - verify: Product Page Optimization: check for a Running test; compare its tested items (icon, screenshots, previews) with the changes in the version being submitted.
  - fix: Stop the test or keep the tested assets unchanged in the new version.

## PAGE.18 Create a product page optimization test

**Source page:** https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/create-a-test

**Source text (verbatim):**
> Configure product page optimization tests in App Store Connect if your app has a Pre-Order Ready for Distribution or Ready for Distribution status and is live on the App Store. Learn how to design tests.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> - In the sidebar, click Product Page Optimization.
> - If you haven’t created a test before, click Create Test. If you've previously created a test, click the add button (+) next to Product Page Optimization.
> - Enter a reference name to help you identify the test when monitoring results in App Analytics.
> - Choose the number of treatments you want to create. You can have up to three treatments per test. Please note that the more treatments you add to a test, the longer the test may take to reach a conclusive result.
> - Choose a traffic proportion. This is the percentage of users that’ll be randomly shown a test treatment instead of your original product page. For example, if a test has three treatments and you choose a 30% traffic proportion, each treatment will be shown to 10% of the total traffic.
> - Select the localizations you want to include in your test. By default, all localizations that your app supports are selected. If the localization shown to a user is excluded from your test, the user won’t be included in the test.
> - To view how long it might take to reach your goal, click the arrow next to Estimate Your Test Duration and choose your desired improvement in conversion rate. We use your app’s existing performance data, such as daily impressions and new downloads, to generate this estimate. The estimated duration and impressions needed will appear. This estimate is provided as a guide and won’t impact the test. A test runs for 90 days or until you manually stop it within that time. Keep in mind that it may not be possible to reach your desired improvement in conversion rate within 90 days.
> - Click Create Test.

**Applies to:** iOS or iPadOS apps that run product page optimization tests

- **[PAGE-53]** Does the test have no more than three treatments?
  - quote: "You can have up to three treatments per test."
  - surface: asc
  - verify: Product Page Optimization > (test): count the treatments.
  - fix: Reduce the number of treatments to three or fewer.

## PAGE.19 Configure test treatments

**Source page:** https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/configure-test-treatments

**Source text (verbatim):**
> By default, test treatments are copies of your app’s original App Store product page. You can edit the app icon, screenshots, and previews of each treatment. If you choose not to edit one of these items, the metadata from your original product page will display for that item.
>
> Before testing, ensure all metadata in your test treatments is approved. You can submit this metadata without submitting a new version of your app. However, any app icons you wish to use must be part of the app binary for the current App Store version, which should be built with Xcode 13 or later and support alternate icons in asset catalogs through an appropriate SDK.
>
> If you’re simply changing the order of screenshots or previews that are already on the App Store, or only modifying the app icon, your metadata is already approved and you don’t need to resubmit.
>
> Note: Product page optimization tests aren't available for custom product pages or for product pages on the App Store for Apple Watch or iMessage.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Product page optimization.
> - The default treatment names are Treatment A, Treatment B, and Treatment C. Treatment names are only visible to you in App Store Connect and help you identify treatments in App Analytics. Next to the treatment name you want to edit, click Edit Name.
> - Enter a treatment name, then click OK.
> - Click the App Icon tab, which displays if your app binary includes more than one icon. Ensure any icons you want to use are part of the app binary currently on the App Store. This app version must be built with an SDK that supports alternate icons in asset catalogs. Icons must also be sized to 1024x1024 pixels.
> - Click Change under under the icon of the treatment you want to change.
> - Choose an icon from the menu that appears. This menu shows all app icons included in your app’s binary. If an app is downloaded from a product page with a test treatment, the test treatment app icon displays throughout the download process and on the user’s device.
> - Select Header and Search Results or App Previews and Screenshots tab to upload your assets. If you choose not to edit screenshots or previews for a certain device size, the treatment will use the ones on your original product page for that device size. For details on specifications, visit Screenshot specifications and App preview specifications.
>
> Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.

**Applies to:** iOS or iPadOS apps that run product page optimization tests

- **[PAGE-54]** Is all metadata in the test treatments approved (or submitted for approval) before the test is started?
  - quote: "Before testing, ensure all metadata in your test treatments is approved."
  - surface: asc
  - verify: Product Page Optimization > (test): check each treatment's screenshots/previews status, or whether Start Test prompts to Add for Review.
  - fix: Add the test to a submission and submit it for review.
- **[PAGE-55]** Is every alternate app icon used in a treatment included in the binary of the current App Store version?
  - quote: "any app icons you wish to use must be part of the app binary for the current App Store version"
  - surface: code
  - verify: In the Xcode project of the live version, inspect the asset catalog (Assets.xcassets) for the additional app icon sets and the target's App Icons build settings (alternate app icon names / include all app icon assets); in App Store Connect, confirm the App Icon tab of the treatment lists the icon.
  - fix: Add the alternate icon set to the asset catalog, ship it in an App Store version, then use it in the treatment.
- **[PAGE-56]** Was the current App Store version built with Xcode 13 or later and an SDK that supports alternate icons in asset catalogs?
  - quote: "which should be built with Xcode 13 or later and support alternate icons in asset catalogs through an appropriate SDK."
  - surface: code
  - verify: Check the Xcode version/SDK used for the live build (App Store Connect build details, or the project's build environment).
  - fix: Rebuild with Xcode 13 or later and submit a new version containing the icons.
- **[PAGE-57]** Are treatment app icons sized 1024x1024 pixels?
  - quote: "Icons must also be sized to 1024x1024 pixels."
  - surface: code
  - verify: Open each alternate app icon set in the asset catalog and confirm the 1024x1024 image (e.g., sips -g pixelWidth -g pixelHeight).
  - fix: Provide a 1024x1024 image for each alternate icon.

## PAGE.20 Run a product page optimization test

**Source page:** https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/run-a-test

**Source text (verbatim):**
> Before starting a test, ensure all metadata is approved by App Review for distribution on the App Store. If approval is pending, the metadata will be included in a new submission for review. Learn more about submitting for review.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> Start a test
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Product Page Optimization.
> - Click the name of the test you want to start.
> - On the top right, click Start Test. The test status automatically updates to Running and shows how long the test has been live.
>
> If your metadata needs to be reviewed, you’ll be prompted to add the test for review. Click Add for Review, then select whether to add the test to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version.
>
> In the submission window, click Submit for Review. The test status will change once the metadata is accepted by App Review.
>
> - Your test will run for 90 days or until you manually stop it within that time. Test results appear in App Analytics after there are five first-time downloads associated with the test. Learn how to view product page optimization results.
>
> Manually stop a test
>
> - In Apps, select the app you want to view.
> - In the left sidebar, click Product Page Optimization.
> - Click the name of the test you want to stop.
> - On the top right, click Stop Test. Once you stop a test, it can't be restarted. You’ll need to create a new test with the same treatments and run it again.

**Applies to:** iOS or iPadOS apps that run product page optimization tests

## PAGE.21 Submit assets from Asset Library

**Source page:** https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-assets-from-asset-library

**Source text (verbatim):**
> If you want to submit an asset and your app doesn't have an approved version, include the asset in the same submission as your first app version. If your app is already approved, you can choose to submit an asset with or without an app version. You can also add other items to a submission.
>
> - First app version: If your app doesn’t yet have an approved version, include your assets in the same submission as your first app version.
> - Subsequent updates: After your app has an approved version, you can submit standalone assets directly from the Asset Library without creating a new app version.
> - Assets assigned to other items: When you submit an app version, Custom Product Page, Product Page Optimization test, or In-App Event, any assets assigned to it are automatically included in that submission and reviewed together.
> - Submission restrictions: An asset can’t be submitted on its own through the Asset Library if the item it is assigned to is already part of an active submission.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> - In Apps, select the app you want to view.
> - In the sidebar, select the Asset Library.
> - Click Edit at the top right.
> - Select the assets you want to submit for review.
>
> You can also select the Add for Review link in the Status column.
>
> - On the top right, click Add for Review, then select whether to add the asset to an existing draft submission or create a new submission.
>
> If you submit an app version, Custom Product Page, Product Page Optimization test, or In-App Event, any assets assigned to it are reviewed as part of that submission. You can’t submit those assets separately in the Asset Library.
>
> If you're submitting the asset for review without an app version, or your submission includes items associated with multiple platforms, select a platform in the draft submission screen. The asset, and any other items in your submission, are reviewed together with the latest version of the selected platform.
>
> You can also add other items to the submission.
>
> - In the Draft Submission pane, click Submit for Review.
>
> Learn how to remove a submission from review.

**Applies to:** Apps that submit assets from the Asset Library

- **[PAGE-58]** If the app has no approved version yet, are the Asset Library assets included in the same submission as the first app version?
  - quote: "If your app doesn’t yet have an approved version, include your assets in the same submission as your first app version."
  - surface: asc
  - verify: App Review section / draft submission: confirm the assets and the first app version are in the same submission.
  - fix: Add the assets to the draft submission containing the first version.
- **[PAGE-59]** Is no asset being submitted on its own while the item it is assigned to is already in an active submission?
  - quote: "An asset can’t be submitted on its own through the Asset Library if the item it is assigned to is already part of an active submission."
  - surface: asc
  - verify: Asset Library: for each asset to submit, check which item it is assigned to and whether that item's submission is active.
  - fix: Let the asset be reviewed with its item's submission instead of submitting it separately.
- **[PAGE-60]** Is the user submitting Asset Library assets an Account Holder, Admin, or App Manager?
  - quote: "Required role: Account Holder, Admin, or App Manager."
  - surface: asc
  - verify: Users and Access: check the submitting user's role.
  - fix: Have a user with one of those roles submit the assets.

## PAGE.22 Creative assets specifications

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications

**Source text (verbatim):**
> Creative assets include product page header, search results, and in-app event cards.
>
> Learn more about App Store asset best practices and resources.
>
> Learn how to manage creative assets in App Store Connect.
>
> Image specifications for product page header and search results
>
> Note: Images can’t include alpha channels or transparencies.
>
> | Placement | Aspect ratio | Resolution | Supported extensions |
> |---|---|---|---|
> | Product page header | 21:9 | 3840 x 1646 pixels | .jpeg, .jpg, or .png |
> |  | 16:9 | 5244 x 2950 pixels | .png |
> | Search results | 3:2 | Min: 1920 x 1280 pixels<br>Max: 3840 x 2560 pixels | .jpeg, .jpg, or .png |
> |  | 16:9 | 5244 x 2950 pixels | .png |
>
> Video specifications for product page header and search results
>
> Note: Videos are muted by default in search results and can't currently be unmuted. On your product page, videos are also muted by default, but people can unmute them. Videos loop continuously in both placements.
>
> | Placement | Aspect ratio | Resolution | Frames per second | Minimum length | Maximum length | Supported extensions |
> |---|---|---|---|---|---|---|
> | Product page header | 21:9 | 3840 x 1646 pixels | 30 fps or 60 fps | 5 seconds | 30 seconds | .mov, .m4v, or .mp4 |
> | Search results | 3:2 | Min: 1920 x 1280 pixels<br>Max: 3840 x 2560 pixels | 30 fps or 60 fps | 5 seconds | 30 seconds | .mov, .m4v, or .mp4 |
>
> Image specifications for In-App Event cards
>
> Note: Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation. Learn more about In-App Event media and audio specifications.
>
> | Placement | Aspect ratio | Resolution | Maximum file size | Supported extensions |
> |---|---|---|---|---|
> | In-App Event card | 16:9 | Min: 1920 x 1080 pixels<br>Max: 3840 x 2160 pixels | 500 MB | .jpeg, .jpg, or .png |
> | In-App Event details page | 9:16 | Min: 1080 x 1920 pixels<br>Max: 2160 x 3840 pixels | 500 MB | .jpeg, .jpg, or .png |
>
> Video specifications for In-App Event media
>
> Notes:
>
> - Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation. Learn more about In-App Event media and audio specifications.
> - Videos are muted by default in search results and can't currently be unmuted. On your product page, videos are also muted by default, but people can unmute them. Videos loop continuously in both placements.
>
> | Placement | Aspect ratio | Resolution | Frames per second | Minimum length | Maximum length | Supported extensions |
> |---|---|---|---|---|---|---|
> | In-App Event card | 16:9 | Min: 1920 x 1080 pixels<br>Max: 3840 x 2160 pixels | 30 fps or 60 fps | 15 seconds | 30 seconds | .mov, .m4v, or .mp4 |
> | In-App Event details page | 9:16 | Min: 1080 x 1920 pixels<br>Max: 2160 x 3840 pixels | 30 fps or 60 fps | 15 seconds | 30 seconds | .mov, .m4v, or .mp4 |

In the first table, an empty Placement cell continues the placement of the row above (Apple's table spans that cell across two rows).

**Applies to:** Apps that upload creative assets (product page header, search results, In-App Event media)

- **[PAGE-61]** Are creative asset images free of alpha channels and transparency?
  - quote: "Images can’t include alpha channels or transparencies."
  - surface: manual
  - verify: For each image, run sips -g hasAlpha <file> (expect "no").
  - fix: Flatten/re-export the image without an alpha channel (e.g., JPEG, or PNG without alpha).
- **[PAGE-62]** Is each product page header image 21:9 at 3840 x 1646 pixels (.jpeg/.jpg/.png) or 16:9 at 5244 x 2950 pixels (.png)?
  - quote: "3840 x 1646 pixels"
  - surface: manual
  - verify: Check extension and pixel dimensions of each product page header image.
  - fix: Re-export at one of the listed sizes and formats.
- **[PAGE-63]** Is each search results image 3:2 between 1920 x 1280 and 3840 x 2560 pixels (.jpeg/.jpg/.png) or 16:9 at 5244 x 2950 pixels (.png)?
  - quote: "Min: 1920 x 1280 pixels" ... "Max: 3840 x 2560 pixels"
  - surface: manual
  - verify: Check extension and pixel dimensions of each search results image.
  - fix: Re-export at a listed size and format.
- **[PAGE-64]** Are product page header and search results videos 5–30 seconds long, 30 fps or 60 fps, in .mov/.m4v/.mp4, at the listed resolution?
  - quote: "30 fps or 60 fps | 5 seconds | 30 seconds | .mov, .m4v, or .mp4"
  - surface: manual
  - verify: Inspect duration, frame rate, resolution and extension of each video (ffprobe or QuickTime Inspector).
  - fix: Re-edit/re-encode to the listed length, frame rate and resolution.
- **[PAGE-65]** Are In-App Event videos 15–30 seconds long?
  - quote: "30 fps or 60 fps | 15 seconds | 30 seconds"
  - surface: manual
  - verify: Inspect the duration of each In-App Event card and details video.
  - fix: Re-edit to between 15 and 30 seconds.

## PAGE.23 App Store asset statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-asset-statuses

**Source text (verbatim):**
> When an asset — such as an app preview, screenshot, or creative asset — is added to the Asset Library, it moves through the following statuses:
>
> | Status | What it means |
> |---|---|
> | Uploading | The asset is being added to the Asset Library. |
> | Processing | Your uploaded asset is being processed and validated. You can’t take action on the asset until processing completes. |
> | Prepare for Submission | You’ve uploaded an asset to App Store Connect, but haven’t submitted it to App Review. While in this state, the asset is available to browse and select when configuring app versions, Custom Product Pages, Product Page Optimization tests, or In-App Events. You can also delete the asset. |
> | Ready for Review | The asset has been added to a submission, but it hasn't been submitted to App Review yet. |
> | Waiting for Review | Apple received your submission, but hasn't started review. |
> | In Review | App Review is reviewing your submission. You can cancel the submission to remove it from review. |
> | Accepted | This asset has been accepted, but there are one or more rejected items in the submission. All items in the submission must be accepted before any can be published. You can edit the rejected items and resubmit, or you can remove the item from the submission. |
> | Approved | Apple has approved your asset. |
> | Rejected | App Review didn't accept your asset. You can edit the item and resubmit, or you can remove the item from the submission. |
> | Archived | The asset belonged to a previous app version and has been replaced by a newer one. Archived assets don't appear in the Asset Library by default; use filters to view them. |

**Applies to:** Apps that use the Asset Library

- **[PAGE-66]** Are there no Rejected items left in a submission that also holds Accepted assets the developer expects to publish?
  - quote: "All items in the submission must be accepted before any can be published."
  - surface: asc
  - verify: Asset Library and App Review section: look for assets in Accepted status and Rejected items in the same submission.
  - fix: Edit and resubmit the rejected items, or remove them from the submission.
- **[PAGE-67]** Has every asset that should go live finished Processing and left Prepare for Submission (added to a submission)?
  - quote: "You’ve uploaded an asset to App Store Connect, but haven’t submitted it to App Review."
  - surface: asc
  - verify: Asset Library > Status column: list assets still in Processing or Prepare for Submission.
  - fix: Wait for processing, then add the assets for review (PAGE.21) or assign them to an item being submitted.

## PAGE.24 Add an app icon

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-information/add-an-app-icon

**Source text (verbatim):**
> An app icon serves as the representation of your app, and it appears on the Home Screen and in key locations throughout the system, including search results, notifications, system settings, share sheets, and TestFlight. For design guidance on app icons, visit Human Interface Guidelines > App icons.
>
> You can create your app icon using Icon Composer or add your app icon to an asset catalog within your Xcode project. After adding icons in Xcode, upload the build to App Store Connect.
>
> If you want to change your app icon after publishing, you must create and upload a new version of your app. Then, submit it for review.
>
> Required role: Account Holder, Admin, App Manager, or Developer. View role permissions.

**Applies to:** All apps

- **[PAGE-68]** Is the app icon provided in the Xcode project (an Icon Composer icon or an app icon in an asset catalog) and included in the uploaded build?
  - quote: "You can create your app icon using Icon Composer or add your app icon to an asset catalog within your Xcode project."
  - surface: code
  - verify: In the Xcode project, find the .icon file (Icon Composer) or the AppIcon set in Assets.xcassets and confirm the target's App Icon build setting (ASSETCATALOG_COMPILER_APPICON_NAME) points to it; in App Store Connect, confirm the build shows an icon.
  - fix: Add the icon in Icon Composer or the asset catalog, set it as the target's app icon, then upload a new build.
- **[PAGE-69]** If the icon is being changed after publishing, is it delivered in a new app version that is submitted for review?
  - quote: "If you want to change your app icon after publishing, you must create and upload a new version of your app. Then, submit it for review."
  - surface: asc
  - verify: Confirm the new icon is in the build attached to a new version in App Store Connect.
  - fix: Create a new version, upload a build with the new icon, and submit it.

## PAGE.25 Overview of Accessibility Nutrition Labels — Introduction and types of features

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels

**Source text (verbatim):**
> The Accessibility Nutrition Labels help users learn if an app will be accessible to them before they download, and give developers the opportunity to better inform and educate their users on features that their app supports. The labels appear on the app product page and will help users understand if they can use a feature like VoiceOver or Larger Text to complete common tasks in the app.
>
> In order to give you time to prepare and evaluate your apps, providing these labels will be voluntary to start. However, you’re encouraged to report your accessibility support to help everyone, including people with disabilities, better discover apps that fit their needs. You’ll be given ample time and evaluation resources before this is mandatory, but over time, you’ll be required to share accessibility support details to submit new apps and app updates to the App Store.
>
> Types of Accessibility Features
>
> Below are the accessibility features you can provide Accessibility Nutrition Labels for. We recommend that you evaluate your features in this order. Most of the work that goes into making your app accessible to VoiceOver users, for example, can also make it more accessible for users of other assistive technologies, like Voice Control and more.
>
> Some accessibility labels aren’t available on some devices, as indicated in the table below, so you’ll be prompted to indicate support only for the accessibility features that are applicable to each device in App Store Connect.
>
> | Accessibility feature | Description |
> |---|---|
> | VoiceOver | Users can navigate and explore the app using gestures, keyboard, braille, and speech output. |
> | Voice Control | Users can navigate and interact with the app using their voice to tap, swipe, click, type, and more. This isn't supported on Apple TV and Apple Watch. |
> | Larger Text | Increases the text size in the app to 200% or more. This label isn't supported on Mac. |
> | Dark Interface | Applies a dark color scheme to the screens, menus, and controls to reduce eye strain. |
> | Differentiate Without Color Alone | Uses shapes or text, in addition to or instead of color, to distinguish key information. |
> | Sufficient Contrast | Increases or adjusts the contrast between text or iconography and background. |
> | Reduced Motion | Modifies or reduces certain types of animation that may cause motion sickness or discomfort. |
> | Captions | Users can follow the dialog and relevant sounds of video or audio-only content with time-synchronized text. |
> | Audio Descriptions | Users can hear audio descriptions of video content in a clip, show, or movie with time-synchronized narration. |

**Applies to:** All apps (voluntary to start)

## PAGE.26 Overview of Accessibility Nutrition Labels — Discovery on the App Store

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels

**Source text (verbatim):**
> The Accessibility Nutrition Labels will appear on your app’s product page in all countries or regions where your app is available. The App Store displays the labels specific to the device type (iPhone, Mac, etc.) used to view your product page.
>
> Note: The Accessibility Nutrition Labels will appear on Apple devices running iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26 or later.
>
> You have the option to provide information for each device your app supports in App Store Connect. If you don’t provide this information for a device, the section will still appear on your product page and show that you haven’t indicated support yet. This section will also indicate if your app supports none of these accessibility features.
>
> You also have the option to provide an accessibility URL that links to your website so that users can learn more about the app’s accessibility features. This link will show on your app's product page across all devices, except Apple TV. This accessibility URL should correspond uniquely to your app and can include information such as other accessibility features, how to turn on and manage any in-app accessibility settings, what languages are supported in captions, or areas of your app that don’t support an accessibility feature.
>
> Users can include Accessibility Nutrition Label features as part of their search query to make their results more relevant. For example, in searches like “VoiceOver note taking apps” or “running apps with Larger Text,” apps that have indicated support for those features in their labels will be considered more relevant in search results.

**Applies to:** Apps that provide Accessibility Nutrition Labels or an accessibility URL

- **[PAGE-70]** If an accessibility URL is provided, does it point to a page that corresponds uniquely to this app?
  - quote: "This accessibility URL should correspond uniquely to your app"
  - surface: asc
  - verify: App Store Connect > Apps > (app) > App Accessibility > Accessibility URL: open the URL and confirm it describes this app's accessibility (not a generic company page).
  - fix: Publish an app-specific accessibility page and update the URL.

## PAGE.27 Overview of Accessibility Nutrition Labels — Planning for your responses

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels

**Source text (verbatim):**
> To encourage developers to respond consistently across all apps, the App Store has set evaluation criteria a developer should meet before indicating support in the Accessibility Nutrition Labels.
>
> Before providing your responses in App Store Connect, you’ll need to audit your app to understand the level of support it provides and how it aligns to the App Store’s standards for each accessibility feature. Since your app’s support of an accessibility feature can differ per device and you can provide responses for each device in App Store Connect, you should assess your app on each of the devices your app supports.
>
> To indicate support for an accessibility feature in the Accessibility Nutrition Labels, users must be able to complete all of the common tasks of your app using that feature.
>
> In addition to following the evaluation criteria, make sure to follow App Review Guideline 2.3 for accurate metadata. If an app potentially has intentionally misleading or harmful accessibility labels, App Review has the ability to contact the developer and ask them to update their Accessibility Nutrition Labels.
>
> You’re responsible for keeping your responses accurate and up-to-date. If your practices change, please update your responses.

**Applies to:** Apps that provide Accessibility Nutrition Labels

- **[PAGE-71]** For every accessibility feature marked as supported, can users complete all of the app's common tasks using that feature?
  - quote: "To indicate support for an accessibility feature in the Accessibility Nutrition Labels, users must be able to complete all of the common tasks of your app using that feature."
  - surface: runtime
  - verify: App Accessibility page: list the features claimed per device; for each, run every common task (PAGE.28) on that device with the feature on (see PAGE.32–PAGE.40 criteria).
  - fix: Fix the blocking issues, or edit the device's responses to remove the unsupported feature and Publish.
- **[PAGE-72]** Were the responses assessed separately on each device the app supports?
  - quote: "you should assess your app on each of the devices your app supports."
  - surface: manual
  - verify: Compare the devices listed on the App Accessibility page with the devices the app supports (Xcode target supported destinations); ask for per-device test evidence.
  - fix: Test on each device and set each device's responses separately.
- **[PAGE-73]** Are the accessibility labels accurate and not misleading (App Review Guideline 2.3)?
  - quote: "make sure to follow App Review Guideline 2.3 for accurate metadata."
  - surface: asc
  - verify: Compare the published App Accessibility responses with the results of PAGE-71.
  - fix: Update the responses to match actual support.
- **[PAGE-74]** Are the responses up to date with the current build's accessibility support?
  - quote: "You’re responsible for keeping your responses accurate and up-to-date."
  - surface: asc
  - verify: Compare the App Accessibility responses with changes in the build being submitted (new screens, removed features, new custom controls).
  - fix: Edit the responses and click Publish.

## PAGE.28 Overview of Accessibility Nutrition Labels — Identifying the common tasks in your app

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels

**Source text (verbatim):**
> To indicate support of an accessibility feature in the Accessibility Nutrition Labels, users should be able to complete all of the common tasks of your app using that feature. Before you begin evaluating features, compile a list of the common tasks that a person can perform in your app.
>
> Common tasks checklist
>
> Common tasks consist of the primary functionality that you expect users to perform in your app, plus functionality that's fundamental to using an app in general: first launch experience, login, purchase, and settings.
>
> - Primary functionality specific to your app
> - To indicate support for an accessibility feature, a user should be able to perceive, operate, and understand all of the primary functionality specific to your app while using the feature.
> - To come up with your list of primary functionality, start by defining the key goals, functionality, and features users download and use your app for. It may be helpful to consider what you market in your app’s description, screenshots, and app previews.
>
> As an example, a to-do list app’s common tasks will include these tasks below.
>
> - View task list
> - The user may need to mark a task as complete, undo marking a task as complete, change the due date, or create a new task.
> - Task detail view
> - For a new or existing task, the user may need to enter information about the task, save the task to a list, or exit the screen without making modifications.
> - First launch experience
> - To indicate support for an accessibility feature, a user should be able to complete the app’s first launch experience while using the accessibility feature. For example, your first launch experience may have a video with sound that you may want to express in captions, or an onboarding flow that a user should be able to complete or skip.
> - Login
> - To indicate support for an accessibility feature, a user should be able to complete the login experience while using the accessibility feature. For example, the user should be able to choose a login service, enter a username and password, interact with a login button, request a password reset, or enter information to create a new account.
> - Purchase
> - If your app offers purchases, to indicate support for an accessibility feature, a user should be able to complete the purchase experience while using the accessibility feature. For example, the user should be able to select a payment provider, enter a credit card number, review the terms of an offer, or review before completing the purchase.
> - Settings
> - To indicate support for an accessibility feature, a user should be able to adjust app settings while using the accessibility feature. For example, the user should be able to turn on accessibility or privacy features, manage purchases, or exit the settings screen without modifying settings.
>
> Ensuring a comprehensive list
>
> As you make your list, consider the following to ensure you have a comprehensive list of common tasks:
>
> - Make sure your list includes common tasks that users both with and without disabilities can perform.
> - Consider differences by device, such as if a certain experience is only available on Apple Watch but not Mac.
> - Include tasks that you make mandatory to use your app, such as account sign-up or purchasing a subscription.
> - Especially for new users, consider default and loading screens, such as the screen to view the task list when the user hasn’t added tasks yet.
> - Consider actions a user can take outside your app that are common tasks, such as marking a task complete in a notification or widget from your to-do list app.
> - When evaluating, you're not required to consider tasks that are uncommon in your app. If you're unsure if a task is common, ask yourself whether you'd ship an urgent fix if users were blocked from completing this task. For example, if your app provides links to your app’s marketing channels on social media and web but that isn’t a key goal of using the app, you're not required to include it in your evaluation. If you want to provide more information about the accessibility of uncommon tasks, use the accessibility URL to do so.
>
> Recommended: Create an accessibility testing matrix
>
> After you identify your app’s common tasks, to guide your evaluation, it may be helpful to create an accessibility testing matrix for each device you plan to provide Accessibility Nutrition Labels for in App Store Connect. Following this matrix isn’t required, but it can help make sure you’re validating that all common tasks can be completed for an accessibility feature on that device. This is especially helpful since some of your app’s common tasks may not be available on some devices, and some accessibility features aren’t available on certain devices.
>
> To start, create a matrix for each device you’ll be evaluating for Accessibility Nutrition Labels.
>
> For each matrix, take the common tasks that are available on that device, and add them as rows. For example, if a common task is only available on Mac but not Apple Watch, include the common task in your matrix for Mac but not your matrix for Apple Watch.
>
> Next, consider the accessibility features you want to evaluate. Since some accessibility features aren’t available on certain devices, you won’t be able to provide Accessibility Nutrition Labels for them. Take the accessibility features that are available on that device, and add them as columns.
>
> Now you're ready to evaluate your app.

**Applies to:** Apps that provide Accessibility Nutrition Labels

- **[PAGE-75]** Does the evaluated common-task list include the app's primary functionality plus first launch experience, login, purchase (if offered), and settings?
  - quote: "Common tasks consist of the primary functionality that you expect users to perform in your app, plus functionality that's fundamental to using an app in general: first launch experience, login, purchase, and settings."
  - surface: manual
  - verify: Derive the common tasks from the app's screens (onboarding, sign-in, paywall/StoreKit flows, settings) and its App Store description/screenshots; confirm each was evaluated.
  - fix: Add the missing tasks to the evaluation and re-test.
- **[PAGE-76]** Does the list include tasks the app makes mandatory, such as account sign-up or purchasing a subscription?
  - quote: "Include tasks that you make mandatory to use your app, such as account sign-up or purchasing a subscription."
  - surface: manual
  - verify: Walk the first-run flow for any forced sign-up or paywall and confirm it was included.
  - fix: Add those tasks to the evaluation.
- **[PAGE-77]** Were common tasks performed outside the app (for example in notifications or widgets) considered? (advisory)
  - quote: "Consider actions a user can take outside your app that are common tasks"
  - surface: code
  - verify: Check the project for widget extensions, notification actions (UNNotificationCategory), Live Activities, or similar, and whether they are part of common tasks.
  - fix: Include them in the evaluation.

## PAGE.29 Overview of Accessibility Nutrition Labels — Tips

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels

**Source text (verbatim):**
> Implementation
>
> - Whenever possible, use the Apple-provided native API to reduce implementation complexity and so customers who have turned on the system setting will automatically get this experience without an additional setting. We highly recommend Apple-provided native APIs for complex app behaviors, such as drag and drop or multi-touch gestures.
> - Provide native support for core assistive technologies, including VoiceOver and Voice Control. These assistive technologies allow connection to hardware interfaces, such as braille displays, and interaction with operating system features, like app switching, that your app otherwise wouldn’t be able to support. Don’t attempt to make a custom implementation of the functionality provided by core assistive technologies like VoiceOver or Voice Control.
> - With the exception of core assistive technologies like VoiceOver and Voice Control, you may use a custom implementation to indicate support for your labels, such as a custom dark color scheme, instead of using the system’s standard dark appearance.
> - Even if you use a custom implementation for an accessibility feature, consider leveraging the user’s system setting to ensure your app responds to their needs. For example, if you render custom captions in a game, check the user’s system setting that indicates a need or preference for displaying captions when available. If you offer your own in-app setting, it should offer more granular user interface customization than the system setting provides.
> - Pay extra attention to custom elements, since they are less likely than standard elements to have accommodations for accessible experiences. Additionally, some custom elements may require additional work to support features like VoiceOver and Voice Control.
>
> Third-party content
>
> - You don’t have to consider third-party or user-generated content when evaluating accessibility labels if those views aren’t part of your common tasks.
> - When third-party or user-generated content views are part of your common tasks, you don’t need to ensure all third-party content is accessible, but your app should provide the third-party content creators a reasonable, discoverable way to make their content accessible. For example:
> - In most video streaming apps, developers support a way to display closed captions, even though not all third-party movie and television studios provide captions with their video content.
> - In apps that allow users to upload images, developers should provide a way for the users to label the image, so the image content is perceivable to VoiceOver users.
> - In apps that use a web view to load third-party websites, WebKit provides default support for most accessibility labels for web content by using web standards like HTML, CSS, and ARIA.
> - In addition, web browsers like Safari provide additional accessibility features, like site-specific font size settings, which allow users to enlarge the font sizes of web sites to 200% the default size, or sometimes larger.
>
> Best practices
>
> - The common guiding principles of accessibility are that content, controls, and interfaces should be perceivable, operable, understandable, and robust. Keep these principles in mind as you’re evaluating your app. For example, a blind VoiceOver user should be able to perceive the content of a visual photograph or icon, often by experiencing its text alternative label as speech or braille. Likewise, if most users can operate an item by tapping, clicking, or dragging it, the item should also be operable to assistive technologies like VoiceOver and Voice Control, so that users with disabilities can use all the same functions of an app.
> - You may consider exceptions to the recommendations here if users with disabilities would find them reasonable. For example, you might hide a button from VoiceOver in one view if it duplicates functionality that’s already available and discoverable elsewhere.

**Applies to:** Apps that provide Accessibility Nutrition Labels

- **[PAGE-78]** Does the app avoid custom re-implementations of VoiceOver or Voice Control functionality?
  - quote: "Don’t attempt to make a custom implementation of the functionality provided by core assistive technologies like VoiceOver or Voice Control."
  - surface: code
  - verify: Search the code for in-app screen-reader/speech-navigation substitutes (e.g., custom AVSpeechSynthesizer-driven navigation of UI elements, custom voice command recognizers driving UI) used instead of native accessibility APIs.
  - fix: Use the native accessibility APIs so VoiceOver/Voice Control work directly.
- **[PAGE-79]** Where third-party or user-generated content views are part of common tasks, does the app give content creators a reasonable, discoverable way to make that content accessible?
  - quote: "your app should provide the third-party content creators a reasonable, discoverable way to make their content accessible."
  - surface: runtime
  - verify: In upload/compose flows, check for options such as image descriptions (alt text) or caption tracks.
  - fix: Add a field/option for creators to supply accessible alternatives.

## PAGE.30 Overview of Accessibility Nutrition Labels — Additional guidance

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels

**Source text (verbatim):**
> Your app has bugs that affect its accessibility.
>
> If bugs are significant enough to change your answer according to the Accessibility Nutrition Labels evaluation criteria, then don’t indicate support for the accessibility feature. To avoid misleading users, you shouldn’t enter answers that aren’t aligned with the evaluation criteria.
>
> An accessibility feature doesn't apply to your app.
>
> Review the evaluation criteria for the accessibility feature to determine if it's applicable and whether to indicate support.
>
> You have additional accessibility information to share with users.
>
> Add an accessibility URL to your product page to provide users additional accessibility information, such as other accessibility features, how to turn on and manage any in-app accessibility settings, what languages are supported in captions, or areas of your app that don’t support an accessibility feature feature.
>
> Your app includes app extensions.
>
> Your app may include app extensions such as stickers, custom keyboards, Safari extensions, or photo editing extensions. To determine whether to include app extensions in your evaluation, determine whether they are part of your app’s common tasks. If using the app extension isn't part of your app’s primary functionality, then it's unlikely to be one of your app’s common tasks.
>
> Your app has advertising.
>
> Include advertising in your evaluation if it’s present in the UI when users are completing your app’s common tasks. If the advertising experience prevents users from completing a common task using an accessibility feature (for example, the advertisement contains problematic motion that can't be addressed by a system or in-app setting to reduce motion), then don’t indicate support for the feature.
>
> Your app is a compatible iPhone and iPad app on Apple Vision Pro.
>
> If your iPhone and iPad app is compatible with and can run on Apple Vision Pro, no responses are needed for Apple Vision Pro. The labels for iPhone or iPad will be shown to users on the Apple Vision Pro App Store.
>
> Your app is a compatible iPhone and iPad app on Macs with Apple silicon.
>
> If your iPhone and iPad app is compatible with and can run on Macs with Apple silicon, no responses are needed for Mac. The labels for iPhone or iPad will be shown to users on the Mac App Store.
>
> At Apple, we believe that the best technology works for everyone to help them connect, create, play, and do what they love in the ways that work best for them. Even after you’re able to claim support for an accessibility feature in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Can all users use all features of the app, not just the common tasks? While it’s not required, we encourage you to go beyond this criteria to provide the most accessible experience you can for all users.
>
> Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

**Applies to:** Apps that provide Accessibility Nutrition Labels

- **[PAGE-80]** Are no features claimed as supported despite accessibility bugs significant enough to change the answer under the evaluation criteria?
  - quote: "If bugs are significant enough to change your answer according to the Accessibility Nutrition Labels evaluation criteria, then don’t indicate support for the accessibility feature."
  - surface: runtime
  - verify: Review open accessibility bugs and test results for each claimed feature.
  - fix: Fix the bugs or remove the claim and Publish the updated responses.
- **[PAGE-81]** If ads appear during common tasks, were they included in the evaluation and do they not prevent completing a common task with each claimed feature?
  - quote: "Include advertising in your evaluation if it’s present in the UI when users are completing your app’s common tasks."
  - surface: runtime
  - verify: Check the project for ad SDKs; run common tasks with each claimed feature while ads display.
  - fix: Fix the ad experience or don't indicate support for the affected feature.

## PAGE.31 Manage Accessibility Nutrition Labels

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/manage-accessibility-nutrition-labels

**Source text (verbatim):**
> Review the evaluation criteria for each label before you begin indicating support for the accessibility features.
>
> Learn how to manage Accessibility Nutrition Labels with the App Store Connect API.
>
> Required role: Account Holder, Admin, Finance, App Manager, or Marketing. View role permissions.
>
> Indicate your app’s accessibility support
>
> - In Apps, select the app you want to view.
> - In the sidebar, click App Accessibility.
> - On the right, click Get Started.
> - We automatically detect the devices your app supports if your latest app version is live on the App Store, or if your app record only support one device, like Mac. If the latest version of your app is in an editable state, like Prepare for Submission, select the devices you want to add accessibility support for, then click Save.
> - Click Add [Device] Support for the relevant device.
> - Select Yes if your app supports any of the accessibility features on the selected device, or No if it doesn’t support any of the features, then click Next.
> - Select the accessibility features that your app supports, then click Next.
> - Your responses will be saved as a draft. Click Publish to publish your responses to the App Store.
>
> You can only publish support for devices that have a live version on the App Store.
>
> If you’ve indicated support for multiple devices, you’ll need to confirm the devices you want to publish support for. Select each applicable device, then click Publish again.
>
> The responses will be published immediately but may require up to 24 hours to be visible to all users.
>
> Update your app’s accessibility support
>
> You can update your app accessibility responses at any time.
>
> - In Apps, select the app you want to view.
> - In the sidebar, select App Accessibility.
> - On the right, click Edit next to the device you want to update your responses for.
> - Make your desired changes, then click Save.
> - Click Publish to publish your updated responses to the App Store.
>
> The changes will take effect immediately but may require up to 24 hours to be visible to all users.
>
> Manage the accessibility URL
>
> If you have other accessibility information you'd like to provide, you can optionally include a URL. This link will show on your app's product page across all devices, except Apple TV.
>
> - In Apps, select the app you want to view.
> - In the sidebar, select App Accessibility.
> - Below Accessibility URL, click Add URL.
>
> To update the accessibility URL, click Edit next to the existing URL.
>
> - Enter your URL, then click Publish.
>
> If your app is already live on the App Store, the URL will be published immediately but may require up to 24 hours to be visible to all users. If you haven’t published any versions of your app yet, the accessibility URL will automatically go live with the first release.

**Applies to:** Apps that provide Accessibility Nutrition Labels

- **[PAGE-82]** Were the evaluation criteria for each label reviewed before indicating support?
  - quote: "Review the evaluation criteria for each label before you begin indicating support for the accessibility features."
  - surface: manual
  - verify: Confirm each claimed feature was evaluated against PAGE.32–PAGE.40.
  - fix: Evaluate against the criteria and correct the responses.
- **[PAGE-83]** Have saved responses been published rather than left as drafts?
  - quote: "Your responses will be saved as a draft. Click Publish to publish your responses to the App Store."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > App Accessibility: check each device for unpublished draft responses.
  - fix: Click Publish and confirm the devices.

## PAGE.32 VoiceOver evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voiceover-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Using Apple’s VoiceOver screen reader, users can navigate an app’s interface without needing to see the screen. Many people who are blind or low vision use VoiceOver to understand and control apps.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. If you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should strive to make it work with VoiceOver, too. If you can see an important item on the screen, your app should use a label or description that a VoiceOver user would perceive in audible speech or braille.
>
> Note: Most of the work that goes into making your app accessible to VoiceOver users will also make it more accessible for users of other assistive technologies like Voice Control, Switch Control, and Hover Text. For this reason, we recommend you start your accessibility evaluation with VoiceOver before moving on to test Voice Control.
>
> The following sections provide more detail about how to determine whether your app supports VoiceOver well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports VoiceOver on the App Store.
>
> Getting started with testing
>
> In order to accurately evaluate this label, proficient testing of your app using VoiceOver is necessary on all devices your app supports. To ensure your proficiency in testing with VoiceOver, take some time to review the resources below.
>
> - For iPhone, watch "How to Navigate your iPhone or iPad with VoiceOver,” then visit Turn on and practice VoiceOver on iPhone, Use VoiceOver Gestures on iPhone, and Operate iPhone when VoiceOver is on.
> - For iPad, watch  "How to Navigate your iPhone or iPad with VoiceOver,” then visit Turn on and practice VoiceOver on iPad, Use VoiceOver gestures on iPad, and Operate iPad when VoiceOver is on.
> - For Mac, visit Learn and practice VoiceOver on Mac, then review other topics in the VoiceOver User Guide for macOS.
> - For Apple TV, visit Use VoiceOver on Apple TV.
> - For Apple Vision Pro, visit Turn on and practice VoiceOver on Apple Vision Pro, and Learn VoiceOver gestures on Apple Vision Pro.
> - For Apple Watch, visit Use VoiceOver on Apple Watch.
>
> Once you’ve learned the basics of VoiceOver, you’re ready to begin testing. However, to ensure the best VoiceOver experience for users, we recommend diving deeper into the user guides to learn about advanced functionality that experienced VoiceOver users may rely on.
>
> Indicating support for VoiceOver
>
> You may indicate your app supports VoiceOver if users are able to navigate and interact with visual elements, including text, media, buttons, and controls, using only VoiceOver. Using gestures or keyboard commands, users should be able to focus on each part of the UI, hear what it is, and activate it. Make sure users can complete all of the common tasks of your app using only VoiceOver, without sighted assistance.
>
> All controls should have concise, accurate labels.
>
> Labels, also known as “alternative text,” help VoiceOver users to quickly understand the purpose of each control or interface element.
>
> - Buttons, icons, form controls, and all other elements should contain a concise label providing a text equivalent for VoiceOver users. Interactive text fields and similar form controls should have a label (for example, “phone number”) in addition to the text value (“555-555-1212”) of the selection or contents.
> - Labels should be concise, so that the interface isn’t tedious for a user to navigate and understand quickly. For example, a button for composing a new message should be labeled “New Message” rather than something more verbose like “Press to compose a new message.”
> - Ensure the labels make sense out of context. Because VoiceOver users may land on an element in different ways, avoid ambiguous labels that are unclear when the user encounters the item in a non-linear order, such as “Click here” or “Learn more.” If multiple action elements have the same label, like “Delete” in a Shopping Cart, the label text should make it clear what the action will do, especially in the case of destructive actions. For example, which cart item will be deleted?
> - Ensure that labels don’t include control types like "checkbox" or states like "checked." Otherwise, VoiceOver may speak redundant information to the user, such as “Unsubscribe checkbox, checkbox.” Instead, implement these in your app as traits or through similar APIs appropriate to the device.
> - Most images should include a relevant description or alternative text. If an image is purely decorative, make sure it’s ignored completely by VoiceOver.
> - If your app provides a way for users to upload media, such as images, ensure users have a way to include labels or descriptions for the user-generated content, so that VoiceOver users can hear this description when encountering the media.
> - Charts and other data visualizations should include accessibility information through a more specific chart API, or at minimum, include a reasonably complete text alternative.
> - If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.
> - For more ideas, watch “Writing Great Accessibility Labels“ and "Bring accessibility to charts in your app."
>
> VoiceOver users should be aware of element type and control status or value.
>
> People who rely on VoiceOver often need to hear more information than just labels and text content, since the status or value may be conveyed only through visual means such as a checked box. Implement this information in your app as traits or through similar APIs appropriate to the device.
>
> - When a VoiceOver user lands on an item, VoiceOver should speak the type of element in addition to the label or text content. For example, “Unsubscribe from all emails, checkbox."
> - Users should be able to understand control state and values. Keep in mind that default states, like the “unchecked” state of a checkbox, are implied so they may not be spoken by VoiceOver. For example, “Unsubscribe from all emails, checkbox.” Additionally, take care to update the API for control state and values. For example, once the user has checked the checkbox, VoiceOver will describe the control, including its new state, as, “Unsubscribe from all emails, checked checkbox."
>
> VoiceOver should be able to speak all visible text in your app, and all text entry methods should be operable by VoiceOver users.
>
> The accessibility of most visible text will be automatically supported when using Apple frameworks. However, if your app uses another framework, or custom text entry methods, extra work may be required. For example, Apple has an open-source accessibility plug-in for Unity-based apps.
>
> - All visible text in the app should be accessible to assistive technologies, including VoiceOver. Plain text elements, such as paragraphs, don’t need a separate label, though you should ensure that VoiceOver can speak the text content.
> - Custom keyboards and text entry methods (for example, custom keyboards or PIN code entry widgets) should be operable with VoiceOver, and produce correct speech/braille output for the user, in addition to providing accurate text entry and selection.
> - Temporary status banners and important in-app alerts should be conveyed to VoiceOver users in a timely but non-disruptive manner, often done so with an AccessibilityNotification.
>
> VoiceOver navigation and grouping should be consistent, complete, and use a logical order.
>
> VoiceOver users should be able to navigate in page order, or move directly to a part of the screen using features like the VoiceOver rotors.
>
> - VoiceOver users should be able to navigate to any visible element, either in order (swipe right, VO+Right, and so on) or by using a rotor and touch navigation on most platforms.
> - VoiceOver users should be able to navigate away from the element they are on, whether by continuing forward, going backward (Swipe Left, VO+Left, etc), or by using a rotor or touch navigation on most platforms.
> - If multiple elements or actions are presented as a group, VoiceOver users should be able to either move to each item in the group, or be able to interact with the grouped behaviors (for example, reply, forward, delete) through features like custom actions.
> - VoiceOver users should be able to progress to each element without skipping items or looping back to the same item repeatedly. Try navigating forward through all contents, then backwards through all contents. Try looping through all rotor items forward and backwards, too.
> - When content reloads or refreshes in the background, a VoiceOver user’s reading position shouldn’t reset unexpectedly. For example, if a VoiceOver user is near the bottom of a content feed when the app loads more content, the VoiceOver cursor shouldn’t accidentally reset to the top of the list.
> - When the screen changes or a modal dialog appears, the VoiceOver cursor should move logically into the new content area. VoiceOver users shouldn’t be able to move into invisible, offscreen, or background content.
>
> All interactive elements and controls should be discoverable, operable, and work consistently with VoiceOver.
>
> As a reminder, if you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should make it work with VoiceOver, too.
>
> - VoiceOver’s activation gesture (select then double-tap) and keyboard command (VO+space) should trigger the same behavior as a standard tap or click.
> - Standard keyboard operations (for example, arrow keys) and keyboard modifier shortcuts should continue to work, even when VoiceOver is active, and the VoiceOver cursor should follow changes triggered by standard keyboard navigation like the Tab key, arrow keys, and more.
> - If your app’s controls provide a context menu, overload a long press, or provide other non-default behaviors, consider providing the same behaviors as a custom action using VoiceOver’s actions rotor or its equivalent “show context menu” keyboard command (VO+Shift+M).
> - VoiceOver should work with modal views, like dialogs. Apps should ensure that inactive content behind the modal view isn’t accessible to VoiceOver while the content is inactive. Apps should also support VoiceOver users being able to dismiss modal views, like closing the dialog, using the Escape key or an accessibilityPerformEscape action.
> - Complex app behaviors, such as drag and drop or multi-touch gestures, should be provided in an accessible, discoverable way, such as through a custom rotor or action. Whenever possible, use the Apple-provided native API to reduce implementation complexity.
> - Custom elements, if used by the app or any included frameworks, should provide equivalent accessibility of native elements provided by the Apple UIKit, AppKit, and SwiftUI frameworks. For example, custom buttons, tab bars, and sliders should be operable with VoiceOver and convey the same information as controls using standard API equivalents.
>
> Even after you’re able to indicate support for VoiceOver in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app's support for VoiceOver every time you update your app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for VoiceOver (iOS, macOS, tvOS, visionOS, watchOS)

- **[PAGE-84]** Can users complete all of the app's common tasks using only VoiceOver, without sighted assistance?
  - quote: "Make sure users can complete all of the common tasks of your app using only VoiceOver, without sighted assistance."
  - surface: runtime
  - verify: With VoiceOver on, perform every common task (PAGE.28) on each claimed device.
  - fix: Fix blockers, or don't indicate VoiceOver support.
- **[PAGE-85]** Do buttons, icons, form controls, and other elements have concise labels, and do text fields have a label in addition to their value?
  - quote: "Buttons, icons, form controls, and all other elements should contain a concise label providing a text equivalent for VoiceOver users."
  - surface: code
  - verify: Search for image-only buttons/icons without accessibilityLabel / .accessibilityLabel(_:); run Xcode Accessibility Inspector audit on each common-task screen.
  - fix: Add concise accessibility labels.
- **[PAGE-86]** Are control types and states conveyed through traits/APIs rather than written into labels?
  - quote: "Instead, implement these in your app as traits or through similar APIs appropriate to the device."
  - surface: code
  - verify: Search accessibility labels for words like button/checkbox/checked/selected; check custom controls set accessibilityTraits / .accessibilityAddTraits and accessibilityValue.
  - fix: Remove type/state words from labels and set traits/values.
- **[PAGE-87]** Are purely decorative images ignored by VoiceOver?
  - quote: "If an image is purely decorative, make sure it’s ignored completely by VoiceOver."
  - surface: code
  - verify: Check decorative images for isAccessibilityElement = false / .accessibilityHidden(true) / Image(decorative:).
  - fix: Hide decorative images from accessibility.
- **[PAGE-88]** If users can upload media, can they add labels or descriptions for it?
  - quote: "ensure users have a way to include labels or descriptions for the user-generated content"
  - surface: runtime
  - verify: Check upload flows for a description/alt-text field and that VoiceOver reads it on the media.
  - fix: Add a description field and expose it as the media's accessibility label.
- **[PAGE-89]** Do charts and data visualizations provide accessibility information via a chart API or a reasonably complete text alternative?
  - quote: "Charts and other data visualizations should include accessibility information through a more specific chart API, or at minimum, include a reasonably complete text alternative."
  - surface: code
  - verify: Check charts (Swift Charts, custom drawing) for accessibilityChartDescriptor / AXChartDescriptor or text alternatives.
  - fix: Add an audio graph/chart descriptor or a text alternative.
- **[PAGE-90]** Can users understand control state and values with VoiceOver, including after state changes?
  - quote: "Users should be able to understand control state and values."
  - surface: runtime
  - verify: With VoiceOver, toggle checkboxes/switches/sliders and confirm the new state/value is spoken.
  - fix: Update accessibilityValue/traits when state changes.
- **[PAGE-91]** Is all visible text accessible to VoiceOver?
  - quote: "All visible text in the app should be accessible to assistive technologies, including VoiceOver."
  - surface: runtime
  - verify: Swipe through each common-task screen with VoiceOver and confirm all visible text is spoken (pay attention to text drawn in canvases, game engines, or images).
  - fix: Expose the text as accessibility elements (or use Apple's Unity accessibility plug-in for Unity apps).
- **[PAGE-92]** Are custom keyboards and text entry methods (e.g., PIN entry) operable with VoiceOver?
  - quote: "Custom keyboards and text entry methods (for example, custom keyboards or PIN code entry widgets) should be operable with VoiceOver"
  - surface: runtime
  - verify: Enter text/PINs in each custom entry widget using VoiceOver.
  - fix: Make keys accessibility elements with labels and traits, and announce entered values correctly.
- **[PAGE-93]** Are temporary status banners and important in-app alerts announced to VoiceOver users?
  - quote: "Temporary status banners and important in-app alerts should be conveyed to VoiceOver users in a timely but non-disruptive manner"
  - surface: code
  - verify: Search for toast/banner components and check they post an announcement (AccessibilityNotification.Announcement / UIAccessibility.post(notification: .announcement)).
  - fix: Post an accessibility announcement when banners appear.
- **[PAGE-94]** Can VoiceOver users progress through every element forward and backward without skipping items or looping?
  - quote: "VoiceOver users should be able to progress to each element without skipping items or looping back to the same item repeatedly."
  - surface: runtime
  - verify: Swipe forward through all content, then backward, and loop through rotor items, on each common-task screen.
  - fix: Fix element ordering/grouping (accessibilityElements, .accessibilitySortPriority, containers).
- **[PAGE-95]** Does the VoiceOver reading position stay put when content reloads in the background?
  - quote: "When content reloads or refreshes in the background, a VoiceOver user’s reading position shouldn’t reset unexpectedly."
  - surface: runtime
  - verify: With VoiceOver focus near the bottom of a feed, trigger a load-more/refresh and confirm focus doesn't jump.
  - fix: Preserve focus during reloads (avoid full reloadData / view identity changes).
- **[PAGE-96]** When screens change or modals appear, does VoiceOver focus move into the new content and stay out of background content?
  - quote: "VoiceOver users shouldn’t be able to move into invisible, offscreen, or background content."
  - surface: runtime
  - verify: Open each modal/sheet/dialog with VoiceOver and try swiping to content behind it.
  - fix: Use accessibilityViewIsModal / modal presentation and post screenChanged notifications.
- **[PAGE-97]** Can VoiceOver users dismiss modal views (Escape key or accessibilityPerformEscape)?
  - quote: "Apps should also support VoiceOver users being able to dismiss modal views, like closing the dialog, using the Escape key or an accessibilityPerformEscape action."
  - surface: code
  - verify: Check custom modals implement accessibilityPerformEscape() (UIKit) or are dismissible via standard presentation; test the two-finger scrub gesture.
  - fix: Implement accessibilityPerformEscape or use standard presentation.
- **[PAGE-98]** Are complex interactions (drag and drop, multi-touch gestures, context menus, long presses) also available through custom actions or rotors?
  - quote: "Complex app behaviors, such as drag and drop or multi-touch gestures, should be provided in an accessible, discoverable way, such as through a custom rotor or action."
  - surface: code
  - verify: Search for gesture recognizers / onDrag / onLongPressGesture and check matching accessibilityCustomActions / .accessibilityAction exist.
  - fix: Add custom actions or rotors for those behaviors.
- **[PAGE-99]** Do custom elements (including those from included frameworks) provide accessibility equivalent to native UIKit/AppKit/SwiftUI elements?
  - quote: "Custom elements, if used by the app or any included frameworks, should provide equivalent accessibility of native elements provided by the Apple UIKit, AppKit, and SwiftUI frameworks."
  - surface: code
  - verify: List custom buttons, tab bars, sliders etc.; check their accessibility label, traits, value and adjustable actions.
  - fix: Implement the missing accessibility properties or replace with native controls.

## PAGE.33 Voice Control evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voice-control-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Using Apple’s Voice Control feature, users with reduced mobility or dexterity can navigate an app’s interface using only their voice. When looking at the screen, they can use commands like “tap," "click," or "swipe" to interact with on-screen elements.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. If you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should strive to make it work with Voice Control, too.
>
> Note: Most of the work that goes into making your app accessible to VoiceOver users will also make it more accessible for Voice Control users. For this reason, we recommend you start with the  VoiceOver evaluation criteria before evaluating Voice Control.
>
> The following sections provide more detail about how to determine whether your app supports Voice Control well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Voice Control on the App Store.
>
> Getting started with testing
>
> In order to accurately indicate support, proficient testing of your app using Voice Control is necessary on all platforms for your app. Even if you already have a basic proficiency in testing with Voice Control, take some time to go beyond the basics.
>
> Review the resources below to learn more about using Voice Control for each device your app supports.
>
> - For iPhone, watch “How to use Voice Control on iPhone, iPad, and iPod touch,” then visit Use Voice Control commands to interact with iPhone and  Use Voice Control on your iPhone, iPad, or iPod touch.
> - For iPad, watch “How to use Voice Control on iPhone, iPad, and iPod touch,” then visit  Use Voice Control commands to interact with iPad and Use Voice Control on your iPhone, iPad, or iPod touch.
> - For Mac, visit Get started with Voice Control on Mac.
> - For Apple Vision Pro, visit the Use Voice Control to interact with Apple Vision Pro.
>
> Indicating support for Voice Control
>
> You may say your app supports Voice Control if users are able to navigate and interact with your app using only voice commands. Users should be able to complete all of the common tasks, actions, and functions of your app using only Voice Control, without touching the display.
>
> Using only their voice, users should be able to activate all tappable or clickable elements on the screen.
>
> - Speak “Show numbers” to make sure all buttons, links, and other interactive elements display a number.
> - Speak “Show names” to make sure all buttons, links, and other interactive elements display a label, also known as “alternative text.” Refer to the VoiceOver evaluation criteria for more tips on writing good default labels, and review how to  use accessibilityInputLabels(_:) for Voice Control.
> - If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.
> - Use commands like “tap” or “click” plus the name or number of a control to drive your app’s common workflows. For example, “Tap Compose,” “Click Back,” or “Tap 4.”
> - Match Voice Control labels to the visible text. If the Voice Control label is different from the visible text in your app (for example, “Leave call” instead of “End call”), users may be confused. Your users may be forced to speak “Show names” in order to understand why Voice Control isn’t working as they expected with your app.
>
> Using only their voice, users should be able to operate all interactions in your app, including those that are more complex.
>
> - If your app uses swipes, long presses, secondary clicks, or other ways to show additional interactive controls, make sure those are accessible to Voice Control users. For example, use a custom action. Elements with custom actions will be indicated with a double chevron; try speaking “Show actions for <number>.”
> - If your app reveals a hidden user interface (for example, on hover or swipe), make sure that the user has a speech-only way to show the hidden elements or trigger the same behavior through an action or context menu.
> - Ensure scrolling works in your app. For example, “Scroll down.” For panning views like maps or layout canvases, try out speech commands such as “Pan left” and “Zoom out.”
> - If other multi-touch gestures are required, try speaking the gesture, such as “Swipe up with two fingers.”
> - If your app has a recording option, or if you have a custom dictation function, ensure users can start and stop the recording using only their voice.
>
> Using only their voice, users should be able to dictate and edit text in any text field.
>
> - Make sure that users can dictate text in any text field in your app. Speak “type” and the text you’d like to type.
> - Try speaking commands like “Select” and the text you want selected. Ensure the text is selected, then speak “Delete that” and verify the text is deleted.
> - If you use standard text fields from Apple frameworks, Voice Control will be automatically supported. However, if you use your own custom text entry or a third-party framework, extra work may be required. For example, Apple has an open-source accessibility plug-in for Unity-based apps.
> - If your app uses any custom text fields, text entry behavior, or input validation, review and test the rest of Voice Control’s text commands very carefully.
>
> Additional suggestions
>
> - Some users with physical or cognitive impairments may need more time, or wish to avoid distracting auto-play defaults. If aspects of your app auto-play or auto-hide on a time delay, consider allowing users to cancel or extend that delay.
> - Consider implementing SiriKit and App Intents to make your app better for all users, including Voice Control users. Review  “Bring your app to Siri” for more details.
>
> Even after you’re able to indicate support for Voice Control in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app's support for Voice Control every time you update your app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Voice Control (iOS, macOS, visionOS)

- **[PAGE-100]** Can users complete all common tasks using only Voice Control, without touching the display?
  - quote: "Users should be able to complete all of the common tasks, actions, and functions of your app using only Voice Control, without touching the display."
  - surface: runtime
  - verify: With Voice Control on, perform each common task by voice only, on each claimed device.
  - fix: Fix blockers, or don't indicate Voice Control support.
- **[PAGE-101]** Do all buttons, links, and interactive elements show a number ("Show numbers") and a label ("Show names")?
  - quote: "Speak “Show numbers” to make sure all buttons, links, and other interactive elements display a number."
  - surface: runtime
  - verify: On each common-task screen, speak "Show numbers" and "Show names" and check every interactive element.
  - fix: Make elements accessibility elements with labels.
- **[PAGE-102]** Do Voice Control labels match the visible text?
  - quote: "Match Voice Control labels to the visible text."
  - surface: code
  - verify: Compare accessibility labels / accessibilityInputLabels with the visible button text.
  - fix: Align labels or add accessibilityInputLabels that include the visible text.
- **[PAGE-103]** Are swipe, long-press, secondary-click, and hover-revealed controls accessible to Voice Control users?
  - quote: "If your app uses swipes, long presses, secondary clicks, or other ways to show additional interactive controls, make sure those are accessible to Voice Control users."
  - surface: runtime
  - verify: Speak "Show actions for <number>" on elements with hidden actions; check hidden UI can be revealed by speech.
  - fix: Add custom actions or context menus.
- **[PAGE-104]** Does scrolling (and panning/zooming where used) work by voice?
  - quote: "Ensure scrolling works in your app."
  - surface: runtime
  - verify: Speak "Scroll down", and for maps/canvases "Pan left", "Zoom out".
  - fix: Use standard scroll views or support accessibility scroll actions.
- **[PAGE-105]** If the app records or has custom dictation, can recording be started and stopped by voice alone?
  - quote: "ensure users can start and stop the recording using only their voice."
  - surface: runtime
  - verify: Start and stop recording with Voice Control commands.
  - fix: Make record/stop controls labelled accessibility elements.
- **[PAGE-106]** Can users dictate and edit text in every text field by voice?
  - quote: "Make sure that users can dictate text in any text field in your app."
  - surface: runtime
  - verify: Speak "type ...", "Select ...", "Delete that" in each text field (especially custom fields).
  - fix: Use standard text fields or implement text input protocols fully.

## PAGE.34 Larger Text evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/larger-text-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Users can adjust the size of text and icons to make them more legible, visible, and comfortable to read.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. Ensuring that extra large fonts work well in your app makes the interface more convenient and accessible to more people. While some low-vision or legally blind users may be able to manage default font sizes by using screen zoom or holding their device extremely close to see the text and small icons in your app, this isn't a good user experience.
>
> The following sections provide more detail about how to determine whether your app supports Larger Text well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Larger Text on the App Store.
>
> Getting started with testing
>
> Allow primary content such as body text to scale as large as possible, while retaining usability and informational hierarchy in your app. Many accessibility guidelines recommend allowing users to enlarge text to 200% or larger than the default size. Dynamic Type on iOS, for example, reaches sizes larger than 200% at the AX3 size, and allows body text sizes over 300% at the AX5 size. Testing your app at the largest sizes helps you catch issues such as truncated or overlapping text.
>
> Be sure to design for and test small, medium, large, and extra large accessibility sizes.
>
> While you’re not required to use Apple frameworks to indicate support for Larger Text, we recommend reviewing how Apple’s platform and apps respond to the systemwide settings to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.
>
> Design and test your app at all text sizes, including extra large accessibility sizes.
>
> - For iPhone, watch “How to adjust text size on iPhone or iPad” and visit Make text easier to read on iPhone.
> - For iPad, watch “How to adjust text size on iPhone or iPad” and visit Make text easier to read on iPad.
> - For Apple Vision Pro, visit Text display settings on Apple Vision Pro.
> - For Apple Watch, visit Adjust text size and other visual settings on Apple Watch.
>
> Indicating support for Larger Text
>
> You can indicate that your app supports Larger Text if users can enlarge text to at least 200% or the maximum font size for the system. Allow users to resize text and meaningful icons as large as possible. Body text in the primary iPhone, iPad, and Mac views should increase in size without affecting readability through overlapping layouts or severe truncation. If you have controls that can't reasonably increase in size, review the details below for other ways to make those perceivable, usable, and understandable.
>
> Don’t rely on system-provided assistive technology like Zoom or Hover Text to claim support for Larger Text. These features are available to users regardless of your app’s implementation, so users will already be aware that they can enlarge most or all on-screen text to a sufficient size using Zoom or Hover Text.
>
> The Larger Text label is useful to users of your app as a way to determine whether the user interface of your app supports font size enlargement separate from these built-in features like Zoom. You may indicate support for Larger Text, either by using an Apple-provided feature like Dynamic Type, or by using your own in-app font size control to achieve equivalent font sizes.
>
> You’re not required to adopt Apple frameworks to indicate support for Larger Text, but we recommend detecting when a user has Apple system settings enabled so they don’t have to manually update another setting for the app to function as expected. If you offer your own in-app setting that has additional customization or granular controls, you may not need to use the Apple system setting.
>
> If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.
>
> Use the system font size, or manage your own.
>
> Most iOS apps typically use Dynamic Type, but some developers of games or apps that rely heavily on the use of text may choose to manage their own font sizes with an in-app setting. For most apps, using system frameworks is easier and more reliable than implementing your own.
>
> Apple Books is a good example of an app that supports larger text well, but doesn’t rely on Dynamic Type. While the Books app doesn’t leverage the system font size setting, it offers more granular controls. For example, users can change text to their preferred size, and the app’s layout changes from two columns to a single column at larger text sizes in landscape orientation, so that low-vision users can perceive more words in an uninterrupted line of text.
>
> Safari on iOS is another great example of an app with a custom font size controller. Since not all web pages scale to larger text sizes well, Safari allows users to adjust the font size for each site they visit. If your app uses a web view as part of its common tasks, provide a font size controller or let Safari handle this task for your users.
>
> Use responsive design principles to adjust layout and information hierarchy based on needed text size.
>
> Consider which text to enlarge to reinforce a clear information hierarchy to low-vision users of your app, and prioritize scaling the main content areas before repeated, predictable navigational elements.
>
> Consider the value of screen real estate when determining which elements to scale. For example, the Back and Edit buttons on iOS remain small in the example below because they are repeated, predictable, and secondary elements of the interface. Primary content and action buttons are enlarged, extending to full screen width and lengthening the page to use the available space.
>
> Smaller side-by-side elements may overlap when enlarged, so consider wrapping them onto a new line or laying them out vertically rather than horizontally. In the example below, the layout of the message sender, receiver, and date changes from horizontal to vertical to support larger text sizes.
>
> Keep in mind that some features, like Tab Bars, don’t grow with dynamic text to avoid overlapping valuable screen estate. Consider other ways to make those elements accessible, such as the Large Content Viewer.
>
> Avoid overlapping text and excessive or unusable truncation.
>
> Scaling text to much larger sizes may produce unpredictable results, especially on devices with smaller screens. As text is enlarged, consider how that changes the experience:
>
> - Content may overlap making it difficult to read.
> - Content designed for a single line might become truncated, showing only the first few characters.
>
> Follow these principles for a great experience:
>
> - Avoid overlapping text.
> - Avoid truncating text to the point that it becomes unreadable or ambiguous for the user. Consider allowing the text to wrap to two or more lines instead of truncation.
> - If text is truncated, ensure that users are still able to access the same information as if the text were smaller. For example, in a list view, you can truncate text to a single line or two as long as the full text is available in a different view so users can dive into the details.
> - Test your app's larger text layout with different languages. In addition to languages with a longer average word length, test right-to-left languages and those with larger ascenders, descenders, and diacritics that may by clipped by layout constraints.
>
> Larger Text on tvOS apps
>
> Scale most text in your tvOS app to retain a relative information hierarchy. Section headings and media titles must remain larger than less important description text, even if the scaling isn't exactly proportional.
>
> Rather than focusing on a particular percentage increase, scale the smallest text element as large as possible while retaining the overall usability, information hierarchy, and feel of your app. Watch Prepare your tvOS apps for Dynamic Type for tips on adopting Dynamic Type and design considerations for larger text sizes in tvOS.
>
> You can indicate support for Larger Text in your tvOS app by supporting the largest Dynamic Type size or an equivalent font size using your own implementation.
>
> Larger Text on watchOS apps
>
> Because Apple Watch has a smaller screen, the largest Dynamic Type size on watchOS is larger than 140% of the default size. You can indicate support for Larger Text on your watchOS app by implementing Dynamic Type or by supporting an equivalent or larger size for body text or other primary content.
>
> You might also consider some of the techniques employed by the X-Large watch faces, where each complication can be set up as its own watch face, taking advantage of the full screen size. Low-vision users can still view multiple complications (including your app’s watch face complications) by swiping through each of their saved watch faces.
>
> Even after you’re able to indicate support for Larger Text in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Larger Text every time you update your app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Larger Text (iOS, tvOS, visionOS, watchOS)

- **[PAGE-107]** Can users enlarge text to at least 200% or the system maximum font size?
  - quote: "You can indicate that your app supports Larger Text if users can enlarge text to at least 200% or the maximum font size for the system."
  - surface: code
  - verify: Check text uses Dynamic Type (text styles, UIFontMetrics, .font(.body), adjustsFontForContentSizeCategory) or an in-app size control; run at AX5 in Simulator Environment Overrides.
  - fix: Adopt Dynamic Type or an equivalent in-app control.
- **[PAGE-108]** Does body text in primary views grow without overlapping layouts or severe truncation?
  - quote: "Body text in the primary iPhone, iPad, and Mac views should increase in size without affecting readability through overlapping layouts or severe truncation."
  - surface: runtime
  - verify: Run each common-task screen at the largest accessibility sizes; look for overlap and truncation.
  - fix: Allow wrapping, switch to vertical layouts at large sizes.
- **[PAGE-109]** Is the claim based on the app's own text scaling rather than on Zoom or Hover Text?
  - quote: "Don’t rely on system-provided assistive technology like Zoom or Hover Text to claim support for Larger Text."
  - surface: manual
  - verify: Confirm the evaluation was done with text size settings, not Zoom/Hover Text.
  - fix: Re-evaluate with text size settings.
- **[PAGE-110]** Where text is truncated, is the same information still accessible elsewhere?
  - quote: "If text is truncated, ensure that users are still able to access the same information as if the text were smaller."
  - surface: runtime
  - verify: At large sizes, check truncated cells/labels have a detail view showing full text.
  - fix: Provide full text in a detail view or allow wrapping.
- **[PAGE-111]** If a web view is part of common tasks, is a font size control provided (or Safari used)?
  - quote: "If your app uses a web view as part of its common tasks, provide a font size controller or let Safari handle this task for your users."
  - surface: code
  - verify: Search for WKWebView usage in common tasks; check for a text-size control or SFSafariViewController.
  - fix: Add a font size control or use Safari.
- **[PAGE-112]** On tvOS, do section headings and media titles remain larger than description text at large sizes?
  - quote: "Section headings and media titles must remain larger than less important description text"
  - surface: runtime
  - verify: On Apple TV at the largest text size, compare heading/title sizes with descriptions.
  - fix: Adjust font scaling to keep hierarchy.
- **[PAGE-154]** On tvOS, does the app support the largest Dynamic Type size or an equivalent font size?
  - quote: "You can indicate support for Larger Text in your tvOS app by supporting the largest Dynamic Type size or an equivalent font size using your own implementation."
  - surface: code
  - verify: Check tvOS text uses Dynamic Type text styles (or an in-app size control); test at the largest text size on Apple TV.
  - fix: Adopt Dynamic Type in the tvOS app, or don't indicate Larger Text support for Apple TV.
- **[PAGE-113]** On watchOS, is Dynamic Type (or an equivalent or larger size for body text) supported?
  - quote: "You can indicate support for Larger Text on your watchOS app by implementing Dynamic Type or by supporting an equivalent or larger size for body text or other primary content."
  - surface: code
  - verify: Check watchOS text uses Dynamic Type text styles; test at the largest size.
  - fix: Adopt Dynamic Type in the watchOS app.

## PAGE.35 Dark Interface evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Users with light sensitivity can maintain a dark user interface for the common tasks of the app to reduce eye pain or discomfort.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Dark Interface capability is to support users with light sensitivity for whom large white or bright areas on the screen may cause discomfort or even physical pain. Keep this in mind, because the goal isn't only to make the interface dark, but to keep it that way. Even temporary flashes of bright content may cause discomfort or a difficult user experience.
>
> The following sections provide more detail about how to determine whether your app supports a Dark Interface well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Dark Interface on the App Store.
>
> Getting started with testing
>
> While you’re not required to use Apple frameworks to indicate support for Dark Interface, we recommend reviewing how Apple’s system apps respond to the systemwide setting to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.
>
> To ensure proficiency in testing with a dark interface, review the resources below to learn how to turn on Dark Mode for each device your app supports.
>
> - For iPhone, visit Adjust the screen brightness and color on iPhone.
> - For iPad, visit Adjust the screen brightness and color on iPad.
> - For Mac, visit Use a light or dark appearance on your Mac.
> - For Apple Vision Pro, visit Change the appearance of text, app windows, and more on Apple Vision Pro.
>
> A common mistake is supporting sufficient contrast in your light mode interface, but forgetting to support sufficient contrast in a dark interface. Many developers use gray-on-black for dark mode reading, which can reduce eye strain for standard vision in low-light scenarios, but this reduced contrast variant may be more difficult to read for those with low vision or light sensitivity. Consider testing your app while combining the dark mode color scheme alongside the Increase Contrast accessibility setting.
>
> Indicating support for Dark Interface
>
> You may indicate support if your app is dark by default for all common tasks, excluding any third-party or user-generated content. For example, most apps on tvOS and watchOS are dark by default.
>
> If your app isn’t dark by default for all common tasks, you may still indicate support if it allows the user to enable a mode or setting that keeps the interface dark. This can include supporting the systemwide Dark Mode appearance or using a custom dark color scheme, or as a last resort, supporting the systemwide Smart Invert accessibility setting.
>
> - Be careful of unintended color changes that may cause user confusion. For example, if relying on the Smart Invert setting, a red “Delete” button may invert to green if you don’t account for the color inversion. Additionally, when Smart Invert is enabled, make sure the colors in the media don’t appear inverted.
> - For translucent views, including Apple Vision Pro apps using passthrough, you may indicate support for Dark Interface if your app renders only dark UI. You’re not responsible for background light filtering through your app. However, consider whether your app should reduce the translucency if the system Increase Contrast or Reduce Transparency settings are enabled.
> - If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.
>
> Even after you’re able to indicate support for Dark Interface in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Dark Interface every time you update your app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Dark Interface (iOS, macOS, tvOS, visionOS, watchOS)

- **[PAGE-114]** Is every common task dark by default, or kept dark through a mode or setting (Dark Mode, custom dark scheme, or as a last resort Smart Invert)?
  - quote: "you may still indicate support if it allows the user to enable a mode or setting that keeps the interface dark."
  - surface: code
  - verify: Check for UIUserInterfaceStyle=Light in Info.plist or overrideUserInterfaceStyle/.preferredColorScheme(.light) forcing light mode; check asset catalog colors have dark variants; run common tasks in Dark Mode.
  - fix: Add dark appearances for all common-task screens, or don't indicate support.
- **[PAGE-115]** Are there no temporary flashes of bright content in dark mode (e.g., white launch screens, web views, loading states)?
  - quote: "Even temporary flashes of bright content may cause discomfort or a difficult user experience."
  - surface: runtime
  - verify: In Dark Mode, navigate common tasks watching transitions, launch screen, and web/loading views.
  - fix: Give launch screens, web views and placeholders dark backgrounds.
- **[PAGE-116]** If relying on Smart Invert, do colors stay meaningful and media not appear inverted?
  - quote: "when Smart Invert is enabled, make sure the colors in the media don’t appear inverted."
  - surface: code
  - verify: Check images/video views set accessibilityIgnoresInvertColors / .accessibilityIgnoresInvertColors(); test with Smart Invert.
  - fix: Mark media views to ignore invert colors.

## PAGE.36 Differentiate Without Color Alone evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/differentiate-without-color-alone-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Users shouldn't have to rely on color to distinguish different selection states or values in an app. Instead, apps should use additional methods beyond color, such as text labels or icons, to convey information to users with common forms of color blindness.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. The goal is to ensure that your app doesn’t exclude users who may not be able to perceive all colors. Color blindness is one of the most common forms of disability, affecting up to 10% of some populations.
>
> Color is extremely useful in communicating information quickly. Don’t remove color from your app to support this capability; just make sure color isn’t the only way you’re conveying information.
>
> The following sections provide more detail about how to determine whether your app supports Differentiate Without Color Alone well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Differentiate Without Color Alone on the App Store.
>
> Getting started with testing
>
> A great way to evaluate your app is to try testing using the Grayscale color filter in Accessibility Display settings. While this's not a representation of what color-blind users see, it's a good way to discover unanticipated problems with the use of color in your app. If you can’t use your own app in grayscale, rethink your app’s design and differentiate without color alone.
>
> Ideally, your app should be designed by default to convey information using more than color alone. Using a setting to invoke this experience should be a last resort or stop-gap solution until your app's reliance on color can be improved.
>
> Indicating support for Differentiate Without Color Alone
>
> You may indicate your app supports Differentiate Without Color Alone if the common tasks of your app don't rely on color as the only way to convey information. For example, a game may distinguish teams using symbols, in addition to representing them with colors. If your app does use color as the only differentiator (e.g. color-coded charts), make sure that users can customize the design for their needs with a setting or by choosing multiple color schemes.
>
> - Consider where your elements, controls, or content rely solely on color to differentiate or communicate key information. Examples include status buttons or icons whose only distinguishing difference is red 🔴 vs green 🟢 to indicate positive or negative, online or offline. This visual difference may not be easy for people with red-green color-blindness to perceive.
> - Instead of relying on color alone, consider using placement, order, shape, iconography, or other stylistic differences in addition to color. Differences like a red square 🟥 or green circle 🟢 are perceivable by all sighted users, regardless of color perception ability.
> - Consider allowing multiple color schemes so users can avoid the problematic color combinations they have difficulty distinguishing. One example is in apps and games where color is used to indicate different teams or characters.
> - In complex charts or data visualization apps, consider arranging the chart colors in the same order as the legend keys. Alternatively, you can provide options for in-chart iconography or labels on each element directly to help communicate the data.
>
> Note: These differences reduce cognitive load and help users of all abilities remember what each color means.
>
> For Someone with red-green color blindness, these indicators might appear the same.
>
> Both visual indicators and color help differentiate between indicators.
>
> - If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.
>
> Even after you’re able to indicate support for Differentiate Without Color Alone in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Differentiate Without Color Alone every time you update the app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Differentiate Without Color Alone (iOS, macOS, tvOS, visionOS, watchOS)

- **[PAGE-117]** Do common tasks avoid relying on color as the only way to convey information?
  - quote: "the common tasks of your app don't rely on color as the only way to convey information."
  - surface: runtime
  - verify: Turn on the Grayscale color filter and perform the common tasks; check status indicators, charts, validation errors.
  - fix: Add shapes, icons, text labels or placement differences.
- **[PAGE-118]** Where color is the only differentiator (e.g., color-coded charts), can users customize the design with a setting or alternative color schemes?
  - quote: "make sure that users can customize the design for their needs with a setting or by choosing multiple color schemes."
  - surface: runtime
  - verify: Look for an in-app color scheme setting or response to the Differentiate Without Color setting (accessibilityDifferentiateWithoutColor).
  - fix: Add an alternate scheme or non-color indicators.

## PAGE.37 Sufficient Contrast evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Sufficient Contrast helps users whose vision is reduced due to a disability or situational impairment such as bright sunlight. Users can increase or adjust the contrast between text or iconography and the background, improving readability.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Sufficient Contrast feature is to support low-vision users who may have reduced visual acuity, clarity, and/or contrast perception.
>
> The following sections provide more detail about how to determine whether your app supports Sufficient Contrast well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Sufficient Contrast on the App Store.
>
> Getting started with testing
>
> The accessibility settings for each device include a number of features that can help users customize contrast to fit their needs. Most users that have a need for higher contrast will enable the settings for Bold Text, Increase Contrast, and Reduce Transparency. You’re not required to use the built-in system settings, but testing with them on may give you an understanding of the contrast minimums your users expect. If you offer your own in-app setting, it should either support similar functionality to the systemwide settings, or offer more granular user interface customization.
>
> Enable all three settings before testing your app for sufficient contrast. Review the resources below for details about turning on these settings for each device your app supports.
>
> - For iPhone, visit Change display colors on iPhone to make it easier to see what’s onscreen.
> - For iPad, visit Make text easier to read on iPad.
> - For Mac, visit Make text and icons bigger on Mac and Change Display settings for accessibility on Mac.
> - For Apple TV, visit Display bold text on Apple TV and Increase Apple TV screen contrast.
> - For Apple Vision Pro, visit Text display settings on Apple Vision Pro and Adjust colors and contrast on Apple Vision Pro.
> - For Apple Watch, visit Adjust text size and other visual settings on Apple Watch.
>
> You can check the contrast of elements in your app by using Xcode’s Accessibility Inspector or other color contrast checkers to determine contrast ratios for elements in your app. Most modern accessibility guidelines recommend a minimum contrast ratio of “4.5 to 1 between foreground text and its background” based on a formula provided by the World Wide Web Consortium’s (W3C’s) Web Content Accessibility Guidelines.
>
> If your app supports Dark Mode, be sure to check the minimum contrast in both light and dark modes. A common mistake is supporting sufficient contrast in your light mode interface, but forgetting to support sufficient contrast in a dark interface. Many developers use gray-on-black for dark mode reading, which can reduce eye strain for standard vision in low-light scenarios, but this reduced contrast variant may be more difficult to read for those with low vision or light sensitivity. Consider testing your app while combining the dark mode color scheme alongside the Increase Contras setting.
>
> Consider not only contrast, but also translucency (opacity/blurring) of your background materials, controls, and content. Include legibility of text, icons, and other content, elements, and controls in your evaluation. Remember to test with Increase Contrast on and Reduce Transparency off, and with both settings on.
>
> Make sure to provide sufficient contrast on interactive controls and non-text representations of a state, such as a selection. For example, if you design a custom checkbox, make sure there is sufficient contrast between the checked and unchecked states. Meeting a 3:1 minimum contrast ratio is commonly recommended for non-text contrast.
>
> If you don’t have an existing proficiency in testing sufficient contrast, take some time to go beyond the basics. Review Strive to meet color contrast minimum standards in the Human Interface Guidelines to understand if the contrast of adjacent colors in your UI meets minimum acceptable levels.
>
> A button with insufficient color contrast.
>
> A button with sufficient color contrast.
>
> The systemRed default color in iOS.
>
> The systemRed accessible color in iOS.
>
> Indicating support for Sufficient Contrast
>
> You may indicate your app supports Sufficient Contrast if the user interface for your common tasks, including text, buttons, and other controls, meets general contrast guidelines by default — usually 4.5 to 1 for most text elements.
>
> If your app doesn't provide this minimum contrast by default:
>
> - If your app uses Apple-provided UI frameworks, verify that the Increase Contrast setting applies sufficient contrast.
> - If your app supports custom frameworks, provide users with a choice of multiple color schemes that meet contrast minimums.
> - If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.
>
> Even after you’re able to indicate support for Sufficient Contrast in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Sufficient Contrast every time you update the app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Sufficient Contrast (iOS, macOS, tvOS, visionOS, watchOS)

- **[PAGE-119]** Does common-task UI (text, buttons, controls) meet contrast guidelines by default, usually 4.5 to 1 for most text?
  - quote: "meets general contrast guidelines by default — usually 4.5 to 1 for most text elements."
  - surface: runtime
  - verify: Run Xcode Accessibility Inspector's contrast audit on each common-task screen.
  - fix: Adjust colors to meet the ratio.
- **[PAGE-120]** If not by default, does Increase Contrast (Apple frameworks) or an in-app color scheme (custom frameworks) provide sufficient contrast?
  - quote: "verify that the Increase Contrast setting applies sufficient contrast."
  - surface: code
  - verify: Check asset catalog colors for High Contrast variants or code honoring accessibilityContrast / colorSchemeContrast; test with Increase Contrast on.
  - fix: Add high-contrast color variants or a compliant color scheme.
- **[PAGE-121]** Was contrast checked in both light and dark modes (if Dark Mode is supported)?
  - quote: "be sure to check the minimum contrast in both light and dark modes."
  - surface: runtime
  - verify: Repeat the contrast audit in Dark Mode.
  - fix: Fix dark-mode colors (avoid low-contrast gray-on-black).

## PAGE.38 Reduced Motion evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Motion can enrich app experience, but certain types of motion, such as scaling, spinning, or peripheral motion, cause dizziness or nausea for people with motion sensitivity. Although motion sickness is commonly discussed in the context of augmented and virtual reality, motion can cause reactions in 2D screens as well for users with severe motion-sensitivity conditions. If your app includes these motion triggers, make them optional or provide alternative animations.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability.
>
> The goal of Reduced Motion is to support users with extreme motion sensitivity, who may experience negative side effects, such as nausea, dizziness, headaches, or distraction when encountering certain types of motion triggers. Often, the problematic types of motion are spinning or scaling, and other techniques used to simulate three-dimensional effects or depth.
>
> Well designed animations can convey information intuitively, increasing the usability and understandability of your app. Removing such animations unnecessarily might make your app experience more confusing, so don’t remove or modify all animations prematurely. Review the support criteria below to determine which animations to leave as they are, which animations to modify, and which animations to consider removing entirely.
>
> The following sections provide more detail about how to determine whether your app supports Reduced Motion well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app supports Reduced Motion on the App Store.
>
> Getting started with testing
>
> While you’re not required to use Apple frameworks to indicate support for Reduced Motion, we recommend reviewing how Apple’s system apps respond to the systemwide setting to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.
>
> Review the resources below for details about enabling the Reduce Motion system setting on each device your app supports.
>
> - For iPhone, watch “How to reduce screen motion on iPhone, iPad, and iPod touch” and visit Customize onscreen motion on iPhone.
> - For iPad, watch “How to reduce screen motion on iPhone, iPad, and iPod touch” and visit Customize onscreen motion on iPad.
> - For Mac, visit Customize onscreen motion on Mac.
> - For Apple TV, visit the Reduce screen motion on Apple TV 4K.
> - For Apple Vision Pro, visit Stop or reduce visual motion effects or screen movements on Apple Vision Pro.
> - For Apple Watch, visit the Adjust text size and other visual settings on Apple Watch.
>
> If you don’t have an existing proficiency in testing reduced motion, take some time to go beyond the basics and review the additional resources below.
>
> - Human Interface Guideline > Motion
> - Human Interface Guideline > Accessibility
>
> Indicating support for Reduce Motion
>
> You’re not required to adopt Apple frameworks to indicate support for Reduced Motion, but we recommend detecting when a user has the Apple system setting enabled so they don’t have to manually update another setting for the app to function as expected. If you offer your own in-app setting that has additional customization or granular controls, you may not need to use the Apple system setting.
>
> When testing your app, determine if any views or transitional animations include potential motion triggers that can cause discomfort or distraction for some users. If your app doesn’t contain any problematic motion triggers, you may indicate that it supports Reduced Motion.
>
> - If your app uses depth simulation (including parallax effects, animated blur, and depth-of-field effects), you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion.
> - If your app includes multi-axis motion, multi-speed motion, spinning, or vortex effects, you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion.
> - If your app includes auto-advancing carousel screens or any other ongoing motion, consider stopping the motion based on the user’s setting, or providing a control to allow the user to stop the motion.
> - If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.
> - Review the related links below for more examples of motion triggers.
>
> If your app does contain these types of motion, consider each animation individually.
>
> - Is the animation included purely for stylistic or decorative effect? If so, consider stopping it entirely when the user’s system setting indicates a need or preference for reduced motion.
> - Removing animations entirely can have a negative effect on usability and understandability. If the motion itself conveys some meaning, such as a status change (for example, item moved to cart) or a hierarchical context transition (for example, this view is a subview of the prior view), don’t remove the animation entirely. Instead, consider providing a new animation that avoids motion, or at least reduces full screen motion, such as a dissolve, highlight fade, or color shift. Also consider whether you want to replace your default animation, or only use the new one when the user’s setting indicates a need or preference for reduced motion.
>
> Once your app no longer displays problematic motion triggers to users whose setting indicates a need or preference for reduced motion, you may indicate that it supports Reduced Motion.
>
> Even after you’re able to indicate support for Reduced Motion in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Reduced Motion every time you update your app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Reduced Motion (iOS, macOS, tvOS, visionOS, watchOS)

- **[PAGE-122]** Are depth-simulation animations (parallax, animated blur, depth of field) disabled or changed when the user prefers reduced motion?
  - quote: "If your app uses depth simulation (including parallax effects, animated blur, and depth-of-field effects), you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion."
  - surface: code
  - verify: Search for parallax/motion effects (UIInterpolatingMotionEffect, scroll-driven 3D transforms) and check they branch on UIAccessibility.isReduceMotionEnabled / @Environment(\.accessibilityReduceMotion) or an in-app setting.
  - fix: Disable or replace the animation when Reduce Motion is on.
- **[PAGE-123]** Are multi-axis, multi-speed, spinning, or vortex effects disabled or changed when the user prefers reduced motion?
  - quote: "If your app includes multi-axis motion, multi-speed motion, spinning, or vortex effects, you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion."
  - surface: code
  - verify: Search for rotation/scale animations and check for a Reduce Motion branch; test with Reduce Motion on.
  - fix: Replace with dissolves/fades when Reduce Motion is on.
- **[PAGE-124]** Can auto-advancing carousels or other ongoing motion be stopped (by setting or control)? (advisory)
  - quote: "If your app includes auto-advancing carousel screens or any other ongoing motion, consider stopping the motion based on the user’s setting, or providing a control to allow the user to stop the motion."
  - surface: runtime
  - verify: With Reduce Motion on, check carousels and looping animations.
  - fix: Stop auto-advance under Reduce Motion or add a pause control.

## PAGE.39 Captions evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/captions-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Captions are usually time-synchronized text alternatives for dialogue and relevant sounds in videos or some forms of audio-only content. Captions are an accommodation for the Deaf and hard of hearing communities, but captions are also used widely by those without hearing loss.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Captions feature is to support users whose system settings express a need or desire to have audible dialogue and other sounds visibly rendered on screen, or to an alternate output device like a tactile braille display. Captions are a critical accommodation for the Deaf, DeafBlind, and hard of hearing communities, but captions are also used widely by those without hearing loss.
>
> The following sections provide more detail about how to determine whether your app supports Captions well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Captions on the App Store.
>
> Getting started with testing
>
> While you’re not required to use Apple frameworks to indicate support for Captions, your app should still enable captions by default when detecting the systemwide captions setting. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.
>
> Review the resources below to learn how to turn on systemwide captions for each device your app supports.
>
> - For iPhone, visit Display subtitles and captions on iPhone.
> - For iPad, visit Display subtitles and captions on iPad.
> - For Mac, visit Use subtitles and closed captions on Mac.
> - For Apple TV, visit Turn on closed captions and SDH.
> - For Apple Vision Pro, visit Display subtitles and captions on Apple Vision Pro.
>
> Indicating support for Captions
>
> You may say that your app supports Captions if it provides captions for video played through your app, including game interstitials and audible dialogue. You may also indicate support for Captions if your app provides text transcripts of audio-only content, such as music lyrics or spoken dialogue in podcasts.
>
> - For video content, you may indicate support for Captions if your app has dialogue-only subtitles for primary and alternate languages, but consider improving your pipeline to offer closed captions or SDH, which also includes relevant non-verbal audio such as “[doorbell rings]” or “[dog barks].”
> - Even if your app doesn’t include movies or TV shows with typical subtitles or closed captions, there may be other areas where your app presents spoken dialogue or other relevant sounds. Game interstitials, for example, often include dialogue that should be captioned, even though it’s not delivered with standard captions in a standard video player.
> - If your app provides verbal audio content, such as music with lyrics or spoken podcasts, consider providing a text copy of that content as a transcript. Text transcripts don’t need to be time-synchronized, and you may indicate support for Captions based on the inclusion of high quality transcripts. For example, even though watchOS apps don’t support video playback, a watchOS app could include music lyrics or a transcript for spoken audio.
>
> Captions in third-party content
>
> If your app presents third-party video content, such as video posts in a social media app, videos added by the user in a presentation app, or TV or movie streaming in an entertainment app, users should have the ability to include caption data for your app to present. To indicate support for Captions, you’re not responsible for ensuring every piece of third-party media has captions. However, you should ensure the following:
>
> - Users should be able to determine which pieces of media content are captioned. For example, most video streaming service apps will present a “CC” or “SDH” icon on videos that include captions, along with other details about available subtitle languages.
> - If your app includes the functionality to display captions, but very little or no captioned content is available on your app, don’t indicate support for Captions.
> - Consider evangelizing captions to your content providers so more video content has captions.
>
> Even after you’re able to indicate support for Captions in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Captions every time you update your app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Captions (iOS, macOS, tvOS, visionOS, watchOS)

- **[PAGE-125]** Does the app provide captions for video it plays (including game interstitials and audible dialogue), or transcripts of audio-only content?
  - quote: "You may say that your app supports Captions if it provides captions for video played through your app, including game interstitials and audible dialogue."
  - surface: runtime
  - verify: Play each video/interstitial in common tasks and confirm captions; for audio-only content, confirm transcripts.
  - fix: Add caption tracks or transcripts, or don't indicate support.
- **[PAGE-126]** Are captions enabled by default when the systemwide captions setting is on?
  - quote: "your app should still enable captions by default when detecting the systemwide captions setting."
  - surface: code
  - verify: Check custom players honor MACaptionAppearance / AVPlayer media selection criteria (appliesMediaSelectionCriteriaAutomatically) or use AVPlayerViewController; test with Subtitles & Captioning > Closed Captions + SDH on.
  - fix: Honor the system captions preference.
- **[PAGE-127]** For third-party media, can users tell which content is captioned?
  - quote: "Users should be able to determine which pieces of media content are captioned."
  - surface: runtime
  - verify: Browse media listings for a CC/SDH indicator.
  - fix: Show a caption indicator on captioned media.
- **[PAGE-128]** Is there a meaningful amount of captioned content (not just captioning functionality)?
  - quote: "If your app includes the functionality to display captions, but very little or no captioned content is available on your app, don’t indicate support for Captions."
  - surface: manual
  - verify: Sample the catalog for captioned content.
  - fix: Don't indicate support until captioned content is available.

## PAGE.40 Audio Descriptions evaluation criteria

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-accessibility/audio-descriptions-evaluation-criteria

**Source text (verbatim):**
> Description
>
> Audio descriptions are additional dialogue, interspersed between natural pauses in the main audio of a program or interstitial content, that describe to viewers who are blind or low vision what’s happening on-screen during time-based visual content.
>
> Goals
>
> Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Audio Descriptions feature is to support users who are blind or have low vision. Predominantly used in movies and TV shows, audio descriptions (AD) combine the main audio track with additional narration describing inaudible on-screen events. For example, “Mark stares at Gemma through the window. His expression displays inner conflict, as he wonders what to do next.”
>
> When an AD audio track is selected, narration describes for the scene above from Severance as: “In slow motion, Mark and Helly run together down a long white hallway flashing with red light.”
>
> The following sections provide more detail about how to determine whether your app supports Audio Descriptions well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Audio Descriptions on the App Store.
>
> Getting started with testing
>
> While you’re not required to use Apple frameworks to indicate support for Audio Descriptions, your app should still enable audio descriptions by default when detecting the systemwide audio descriptions setting. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.
>
> Review the resources below to learn how to enable audio descriptions for each device your app supports.
>
> - For iPhone, visit Hear audio descriptions for video content on iPhone.
> - For iPad, visit Hear audio descriptions for video content on iPad.
> - For Mac, visit Change Audio Descriptions settings for accessibility on Mac.
> - For Apple TV, visit Use audio descriptions on Apple TV.
> - For Apple Vision Pro, visit Hear audio descriptions for video content on Apple Vision Pro.
>
> Indicating support for Audio Descriptions
>
> You may say that your app supports Audio Descriptions if it provides narrated descriptions of relevant on-screen content for video played in your app, including game interstitials and audible dialogue.
>
> - Even if your app doesn’t include movies or TV shows, there may be other areas where your app presents on-screen time-based content that may not be available through another form of sensory perception. For example, opening sequences, game interstitials, and cut scenes should be described, even if they’re not delivered in a standard video player. You should also describe tips and hints that are otherwise only available through visual clues.
> - As one uncommon but creative example, a video streaming service might choose to provide an audio-only watchOS app, and automatically select the audio description track.
>
> Audio Descriptions in third-party content
>
> If your app presents third-party content, such as video posts in a social media app, videos added by the user in a presentation app, or TV or movie streaming in an entertainment app, users should have the ability to include an audio description track for your app to present. To indicate support for Audio Descriptions, you’re not responsible for ensuring every piece of third-party media has audio descriptions. However, you should ensure the following:
>
> - Users should be able to determine which pieces of media content are audio described. For example, most video streaming service apps will present an “AD” icon on videos that include audio descriptions.
> - If your app includes the functionality to select audio descriptions, but very little or no described content is available on your app, don’t indicate support for Audio Descriptions.
> - Consider evangelizing audio descriptions to your content providers so more video content has audio descriptions.
>
> Additional suggestions
>
> - Creating great audio description content is a creative process that many movie and TV production teams have started to author and record in-house. Others contract this work to external service firms that specialize in audio description, captioning, and other types of accessible media.
> - If you or your content partners will be developing the audio descriptions yourself, try watching one of your favorite movies or shows with audio descriptions enabled. Pay attention to the details, like the tone of voice, and terseness that is necessary in some scenes. Pay attention to the detail provided in scenarios like end credits. Apple TV+ provides audio description content in multiple languages, and most other major streaming services provide audio description content as well.
>
> Even after you’re able to indicate support for Audio Descriptions in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Audio Descriptions every time you update your app. Set a goal to make your app more accessible to more people in every release.

**Applies to:** Apps that indicate support for Audio Descriptions (iOS, macOS, tvOS, visionOS, watchOS)

- **[PAGE-129]** Does the app provide narrated descriptions of relevant on-screen content for video it plays, including game interstitials and cut scenes?
  - quote: "You may say that your app supports Audio Descriptions if it provides narrated descriptions of relevant on-screen content for video played in your app, including game interstitials and audible dialogue."
  - surface: runtime
  - verify: Play videos, opening sequences, interstitials and cut scenes with audio descriptions enabled.
  - fix: Add audio description tracks, or don't indicate support.
- **[PAGE-130]** Are audio descriptions enabled by default when the systemwide audio descriptions setting is on?
  - quote: "your app should still enable audio descriptions by default when detecting the systemwide audio descriptions setting."
  - surface: code
  - verify: Check the player selects the AD audio track automatically (AVPlayer media selection criteria / MAAudibleMedia preferences); test with Audio Descriptions on.
  - fix: Honor the system audio descriptions preference.
- **[PAGE-131]** For third-party media, can users tell which content is audio described?
  - quote: "Users should be able to determine which pieces of media content are audio described."
  - surface: runtime
  - verify: Browse media listings for an AD indicator.
  - fix: Show an AD indicator on described media.
- **[PAGE-132]** Is there a meaningful amount of described content (not just the ability to select audio descriptions)?
  - quote: "If your app includes the functionality to select audio descriptions, but very little or no described content is available on your app, don’t indicate support for Audio Descriptions."
  - surface: manual
  - verify: Sample the catalog for audio-described content.
  - fix: Don't indicate support until described content is available.

## PAGE.41 Complete the Digital Goods and Services questionnaire

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-information/complete-the-digital-goods-and-services-questionnaire

**Source text (verbatim):**
> The App Store empowers you to scale your app distribution worldwide using a variety of business models, including the sale of digital goods and services in your apps. Digital goods and services are content, features, subscriptions, and other digital experiences offered or consumed within an app. Complete the Digital Goods and Services questionnaire in App Store Connect to indicate how customers pay for or access digital goods and services in your app.
>
> Completing this questionnaire helps ensure your app complies with the App Review Guidelines, Developer Program License Agreement, and helps you identify supported payment options for your customers.
>
> Note: If this questionnaire doesn’t appear in App Store Connect for your app, no action is required.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> Indicate payment options
>
> Indicate how customers consume and access digital goods and services in your app across regions. Digital goods and services are content, features, subscriptions, and other digital experiences offered or consumed within an app.
>
> - From Apps, select your app.
> - In the sidebar under General, click App Information.
> - Scroll to the Digital Goods and Services in Your Apps section, then click Get Started.
> - Answer the questions:
> - If you select No to “Can customers consume digital goods and services in this app?”, click Next.
> - If you select Yes, confirm whether your app uses Apple In-App Purchase exclusively, or select the available payment options (such as alternative payment processing or out-of-app offers) for each country or region where you offer digital goods and services. Then click Next.
> - Confirm and save:
> - On the Confirmation page, take a moment to look over your answers and make any changes before submitting.
> - Click Save.
>
> To edit your answers later, click Edit under Digital Goods and Services in Your App.
>
> Note: After you submit this form, your choices for the European Union remain locked for 12 months and can’t be changed. If you have questions, contact us.

**Applies to:** Apps for which the questionnaire appears in App Store Connect ("If this questionnaire doesn’t appear in App Store Connect for your app, no action is required.")

- **[PAGE-133]** If the Digital Goods and Services questionnaire appears for the app, has it been completed and saved?
  - quote: "Complete the Digital Goods and Services questionnaire in App Store Connect to indicate how customers pay for or access digital goods and services in your app."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > App Information (under General) > Digital Goods and Services in Your Apps section: check whether it still shows Get Started.
  - fix: Click Get Started, answer the questions, review the Confirmation page and click Save.
- **[PAGE-134]** Do the questionnaire answers match how the app actually sells or grants access to digital goods (Apple In-App Purchase only vs. alternative payment processing or out-of-app offers, per country or region)?
  - quote: "confirm whether your app uses Apple In-App Purchase exclusively, or select the available payment options (such as alternative payment processing or out-of-app offers) for each country or region where you offer digital goods and services."
  - surface: code
  - verify: Inspect the project for StoreKit purchase code, external purchase / link-out entitlements and APIs, and third-party payment SDKs; compare with the questionnaire answers per region.
  - fix: Edit the answers to match the app (note the EU lock in PAGE-135), or change the app's payment flows.
- **[PAGE-135]** Has the developer confirmed the EU answers before saving, given they lock for 12 months?
  - quote: "After you submit this form, your choices for the European Union remain locked for 12 months and can’t be changed."
  - surface: manual
  - verify: Ask the developer to confirm the EU payment option selections on the Confirmation page before saving.
  - fix: manual — requires developer decision/legal/business action.

## PAGE.42 Manage app tags

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags

**Source text (verbatim):**
> App tags are glanceable terms that help people understand more about your app or game’s essential qualities. In addition to appearing in App Store search results, app tags can now appear on your product page, further improving the discoverability of your apps and games on the App Store. From these placements, people can tap a specific tag - for example, Sleep - to view more apps and games related to that specific tag. Tags are based on the App Store metadata you provide in App Store Connect, artificial intelligence, and human curation. You can also manage which of your selected tags appear across the App Store in the app information section of App Store Connect.
>
> App Tags allow you to:
>
> - Increase discoverability: Tags appear as glanceable terms in search results and as clickable entities on Search Landing Page and Product Page.
> - Connect with the right audience: Tags align your app with user intent, leading to improved relevance.
>
> You can manage tags in App Store Connect to ensure they are relevant to your app’s functionality. Currently, tags are only supported and displayed to users across the App Store in the United States.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> Edit App Tags
>
> Tags are applied to your app by default, based on the metadata you provide in App Store Connect (en_US only). You can deselect the tags you don't want associated with your app. Deselecting all tags may affect your discoverability on the App Store.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click App Information, under General.
> - Below App Store Tags, click Edit.
>
> - In the pop up window, review your selections. Make any desired changes, and click Save.

**Applies to:** Apps on the United States App Store ("Currently, tags are only supported and displayed to users across the App Store in the United States.")

- **[PAGE-136]** Have the app's tags been reviewed so the selected ones are relevant to the app's functionality? (advisory)
  - quote: "You can manage tags in App Store Connect to ensure they are relevant to your app’s functionality."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > App Information (under General) > App Store Tags > Edit: review the selected tags against the app's features.
  - fix: Deselect irrelevant tags and click Save.
- **[PAGE-137]** Is at least one tag left selected? (advisory)
  - quote: "Deselecting all tags may affect your discoverability on the App Store."
  - surface: asc
  - verify: App Store Tags section: confirm not all tags are deselected.
  - fix: Re-select relevant tags.

## PAGE.43 Provide a custom license agreement

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement

**Source text (verbatim):**
> Apple provides a standard end-user license agreement (EULA) that applies in all countries and regions. If you don’t provide a custom EULA, the standard EULA is applied to your app and the license agreement link isn’t shown on your App Store product page.
>
> Learn how to manage your EULA with the App Store Connect API.
>
> Edit the license agreement
>
> - In Apps, select the app you want to view.
> - In the sidebar, under General, click App Information.
> - On the left, in the General Information section, click Edit next to License Agreement.
> - In the dialog that appears, select “Apply a custom EULA to all chosen countries or regions”.
> - In the Custom License Agreement field, enter your custom EULA as a plain text document.
>
> All HTML tags are stripped and escaped, and only line break characters are accepted.
>
> Tip: To add localized text for your custom EULA, you’ll need to add the localized text for each language within the same text field.
>
> - In the Countries or Regions section, select each country or region where you want to apply your custom EULA.
> - Click Done.
> - On the top right, click Save.

**Applies to:** Apps that provide a custom EULA (otherwise "the standard EULA is applied to your app")

- **[PAGE-138]** Is the custom EULA entered as plain text (no HTML relied on for formatting)?
  - quote: "In the Custom License Agreement field, enter your custom EULA as a plain text document."
  - surface: asc
  - verify: App Information > General Information > License Agreement > Edit: read the Custom License Agreement field for HTML tags or markup.
  - fix: Replace with plain text using only line breaks.
- **[PAGE-139]** Are all countries or regions where the custom EULA should apply selected?
  - quote: "In the Countries or Regions section, select each country or region where you want to apply your custom EULA."
  - surface: asc
  - verify: License Agreement dialog > Countries or Regions: compare selections with the app's availability.
  - fix: Select the missing countries or regions, click Done, then Save.
- **[PAGE-140]** If the custom EULA is localized, is all localized text in the same text field?
  - quote: "To add localized text for your custom EULA, you’ll need to add the localized text for each language within the same text field."
  - surface: asc
  - verify: Read the Custom License Agreement field for each language's text.
  - fix: Add each language's text to the same field.

## PAGE.44 Declare regulated medical device status — Who must declare and required information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-information/declare-regulated-medical-device-status

**Source text (verbatim):**
> To provide additional transparency on the App Store, apps that are available in the European Union (EU)/European Economic Area (EEA), United Kingdom (UK), or United States (US), and that also meet either of the criteria listed below must indicate whether they’re regulated medical device with respect to each region’s regulatory authority or body responsible for the governance and compliance of medical devices.
>
> - Have a primary or secondary category of Health & Fitness or Medical
> - Have indicated your app contains “frequent” in the Medical or Treatment Information field in the age rating questionnaire in App Store Connect
>
> Regulated medical device apps are used for a range of medical purposes, including diagnosis, prevention, monitoring, and treatment of diseases and physiological conditions. They may function on their own or by interfacing with medical device hardware. These apps may require registration or authorization from regulatory bodies such as the U.S. Food and Drug Administration (FDA). Learn more about regulated medical devices in the EU/EEA, in the UK, and in the US.
>
> If your app doesn’t provide any health or medical features, or access health data to support non-health features, you should select No, to declare that your app is not a regulated medical device.
>
> If your app is a regulated medical device, you'll need to provide the following information. In some instances this'll require obtaining authorization or completing registration from the region’s regulatory authority. This information will display to customers on your App Store product page.
>
> - EU Manufacturer SRN or FDA Owner/Operator Number: This should align with your EUDAMED listing and/or FDA establishment registrations. This isn't required for the UK.
> - Instructions for use URL: The URL containing the user guide or instructions for use for your app, hosted on your website.
> - Use statement: For the US, this is your indications for use statement. For the EU/EEA and UK, this is your intended purpose or intended use statement.
> - Safety information: Provide relevant warnings, precautions, and contraindications as they appear in your labeling. For the US, this is also where you can include a statement about how users can report a problem to the FDA such as "To report a problem or adverse event to the FDA, visit www.fda.gov/safety/report-problem-fda".
>
> How to know if your app is a regulated medical device
>
> - Your app was cleared or approved by the US FDA
> - Your app is registered on the US FDA medical device database
> - Your app was issued a CE mark by an EU-based notified body for compliance with the EU Medical Device Regulation (MDR) or Medical Device Directive (MDD)
> - Your app was issued a UKCA mark by a UK-based approved body for compliance with the UK Medical Device Regulations
> - You’ve self-certified your app under the EU Medical Device Regulation (MDR) or Medical Device Directive (MDD)
> - You’ve self-certified your app under the UK Medical Device Regulations

**Applies to:** Apps available in the EU/EEA, UK, or US that have a primary or secondary category of Health & Fitness or Medical, or that indicated “frequent” in the Medical or Treatment Information field in the age rating questionnaire

- **[PAGE-141]** If the app is available in the EU/EEA, UK, or US and is in Health & Fitness or Medical (primary or secondary) or rates "frequent" Medical or Treatment Information, has it declared whether it is a regulated medical device?
  - quote: "must indicate whether they’re regulated medical device with respect to each region’s regulatory authority or body responsible for the governance and compliance of medical devices."
  - surface: asc
  - verify: App Information: check Primary/Secondary Category and the age rating's Medical or Treatment Information answer, plus availability; then check App Store Regulations & Permits > Regulated Medical Devices for a declaration.
  - fix: Click Declare Regulated Medical Device and answer Yes or No.
- **[PAGE-142]** If the app has no health or medical features and doesn't access health data for non-health features, is the declaration No?
  - quote: "you should select No, to declare that your app is not a regulated medical device."
  - surface: code
  - verify: Check the project for HealthKit entitlements/usage, medical device hardware integrations, and health features; compare with the declaration.
  - fix: Set the declaration to No (or Yes with details if it is a device).
- **[PAGE-143]** If the app is a regulated medical device, are the EU Manufacturer SRN or FDA Owner/Operator Number (not required for UK), instructions for use URL, use statement, and safety information provided?
  - quote: "If your app is a regulated medical device, you'll need to provide the following information."
  - surface: asc
  - verify: App Information > Regulated Medical Devices: for each declared country or region, check all fields are filled.
  - fix: manual — requires developer decision/legal/business action (obtain registrations/authorization and enter the details).
- **[PAGE-144]** Does the instructions for use URL point to a user guide hosted on the developer's website?
  - quote: "The URL containing the user guide or instructions for use for your app, hosted on your website."
  - surface: asc
  - verify: Open the URL and confirm it loads the app's instructions for use.
  - fix: Host the instructions for use on the website and update the URL.

## PAGE.45 Declare regulated medical device status — Declaring, updating, and statuses

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-information/declare-regulated-medical-device-status

**Source text (verbatim):**
> Required role: Account Holder or Admin. View role permissions.
>
> Declare regulated medical device
>
> - In Apps, select the app you want to view.
> - In the sidebar, under General, click App Information.
> - Under App Store Regulations & Permits, click Declare Regulated Medical Device.
> - Indicate if your app is a regulated medical device in any country or region.
> - If you select No, click Save and you are done.
> - If you select Yes, continue with step 5.
> - Select which countries your app is a regulated medical device in and click Save.
> - Complete the required information for each country or region where your app is considered a regulated medical device.
> - Verify your contact information that will appear on the App Store. If this information is inaccurate, you’ll need to update it in the Business section of App Store Connect.
> - Enter your EU Manufacturer SRN or FDA Owner/Operator Number for the US as applicable
> - Provide the instructions for use URL, use statement, and safety information. If you wish to localize this information, you can add the required details in each localization from the dropdown menu.
> - Once all the information has been completed and verified, click Save, and the information will go live on the App Store within 24 hours. If the app is not yet approved to be live, the information will go live once the app is approved and released to the store.
>
> Update your regulated medical device declaration
>
> You can click Edit next to the Regulated Medical Devices section to change your declaration for your app or to add or remove countries and regions.
>
> If you have declared that your app is a regulated medical device and need to update the information provided, you can click Edit next to the country or region that needs to be updated in order to make the necessary changes.
>
> You can also manage your contact information by going directly to the Business section and selecting Regulated Medical Devices under the Compliance section.
>
> Updated information will be reflected on the App Store within 24 hours of saving the changes.
>
> Regulated medical device statuses
>
> | Status | Definition |
> |---|---|
> | Yes | You've declared your app is a regulated medical device in this country or region and entered the required information. |
> | No | You've indicated that your app is not a regulated medical device in this country or region. |
> | Missing Info | You've indicated that your app is a regulated medical device in this country or region, but have not completed the required information. |

**Applies to:** Apps that must declare regulated medical device status (see PAGE.44)

- **[PAGE-145]** Is the declaration being made by an Account Holder or Admin?
  - quote: "Required role: Account Holder or Admin."
  - surface: asc
  - verify: Users and Access: check the role of the user making the declaration.
  - fix: Have the Account Holder or an Admin make the declaration.
- **[PAGE-146]** Is the contact information that will appear on the App Store accurate?
  - quote: "Verify your contact information that will appear on the App Store."
  - surface: asc
  - verify: Regulated Medical Devices declaration and Business > Compliance > Regulated Medical Devices: read the contact information.
  - fix: Update it in the Business section of App Store Connect.
- **[PAGE-147]** Does no country or region show the Missing Info status?
  - quote: "You've indicated that your app is a regulated medical device in this country or region, but have not completed the required information."
  - surface: asc
  - verify: App Information > Regulated Medical Devices: check each country or region's status.
  - fix: Click Edit next to the country or region and complete the required information.

## PAGE.46 Request and manage promo codes

**Source page:** https://developer.apple.com/help/app-store-connect/offer-promo-codes/request-and-manage-promo-codes

**Source text (verbatim):**
> Promo codes offer potential App Store customers or reviewers a free copy of apps on iOS, macOS, or tvOS. These codes can be redeemed on any App Store storefront where your app is available. Each code remains valid for four weeks from its generation date and can be used only once.
>
> You can distribute promo codes by any means. Purchases made using promo codes are indicated in your Sales and Trends reports.
>
> Note: Promo codes can't be generated for apps available only on Apple Business or Apple School Manager. If your app has been removed from sale on all App Store storefronts, promo codes can't be generated or redeemed — even if a version has a Ready for Distribution or Pending Developer Release status.
>
> When a customer downloads an app using a promo code, the app functions as if it were purchased. For example, the customer has the opportunity to update to new versions of the app. However, customers can’t rate or review the app. Promo codes can be used to redeem unreleased versions of apps available on the App Store. Promo codes for tvOS or multi-platform apps must be redeemed on an iOS device. After the code is redeemed, the tvOS app appears in the customer’s purchase history on the App Store for Apple TV. You can request up to 100 promo codes per version of each platform your app supports.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> Request promo codes
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Promo Codes. The Promo Code page opens with Generate selected.
> - Under App Promo Codes, enter the number of version promo codes you want to generate.
> - On the top right, click Generate Code.
> - Read and agree to the contract terms for Apple to distribute free versions of your app, and click Generate Code.
> - Click OK. You can view or download the generated promo codes on the History tab.
>
> View history of promo codes
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Promo Codes. The Promo Code page opens with Generate selected.
> - Click History tab.
>
> The history table shows the date each set of codes was generated in App Store Connect. Use this date to determine the expiration date of your codes.
>
> - Click View Codes to view or download generated promo codes.
>
> You can copy the codes in the dialog, or click “text file“ to download a .txt file containing the codes.

**Applies to:** Apps on iOS, macOS, or tvOS that use promo codes

## PAGE.47 Submit for Notarization

**Source page:** https://developer.apple.com/help/app-store-connect/managing-alternative-distribution/submit-for-notarization

**Source text (verbatim):**
> If you’ve set up alternative distribution, you can choose to make your app version eligible only for alternative distribution by selecting to have it evaluated based on the Notarization Review Guidelines (a subset of the App Review Guidelines). Otherwise, App Review uses the App Review Guidelines to evaluate your app version to make it eligible for distribution on the App Store, alternative app marketplaces, and your website (in the EU) if approved. After you've added your app as eligible for distribution on a marketplace in App Store Connect or an alternative distribution domain using the App Store Connect API, follow these steps.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> - In Apps, select your app.
> - In the sidebar, click the app version you want to submit.
> - Scroll down to the App Review Information section, click Edit under Review Type.
> - Select “Notarization” and click Save.
>
> Note: The Review Type selection applies to each version individually. If you want to publish a later version through the App Store instead, select App Store in this same step when you submit that version.
>
> - On the top right, click “Add for Review”. The app status changes to “Ready for Review”. If you changed any app information, you need to click Continue in the dialog that appears.
> - Click “Submit to App Review”. The app status changes to “Waiting for Review”. When the review process starts, the app status changes to “In Review”. Learn about the tasks you can do in these statuses.
>
> The app version is accepted, an alternative distribution package automatically generates.

**Applies to:** Apps that have set up alternative distribution (EU)

- **[PAGE-148]** Before submitting for Notarization, has the app been added as eligible for distribution on a marketplace (or an alternative distribution domain via the App Store Connect API)?
  - quote: "After you've added your app as eligible for distribution on a marketplace in App Store Connect or an alternative distribution domain using the App Store Connect API, follow these steps."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > distribution settings: check marketplace eligibility (or the API's alternative distribution domain configuration).
  - fix: Add the app as eligible for a marketplace or set up the domain, then submit.
- **[PAGE-149]** Is the version's Review Type set correctly — Notarization for alternative-distribution-only versions, App Store for versions meant for the App Store?
  - quote: "The Review Type selection applies to each version individually."
  - surface: asc
  - verify: Version page > App Review Information > Review Type: read the selection for the version being submitted.
  - fix: Click Edit under Review Type, choose Notarization or App Store, and Save.
- **[PAGE-155]** Is the user submitting the version for Notarization an Account Holder, Admin, or App Manager?
  - quote: "Required role: Account Holder, Admin, or App Manager."
  - surface: asc
  - verify: Users and Access: check the submitting user's role.
  - fix: Have a user with one of those roles set the Review Type and submit the version.

## PAGE.48 Required, localizable, and editable properties for Notarization

**Source page:** https://developer.apple.com/help/app-store-connect/managing-alternative-distribution/submit-for-notarization

**Source text (verbatim):**
> The tables below show the app and version properties required to submit your app for Notarization. The tables also indicate the properties that you can localize and edit at any time without submitting a new version of your app.
>
> Learn about the required, localizable, and editable properties for App Store distribution.
>
> App information
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Name | ✓ | ✓ |  |
> | Subtitle |  | ✓ |  |
> | Rating | ✓ |  |  |
> | Bundle ID | ✓ |  |  |
> | SKU | ✓ |  |  |
> | Content Rights |  |  |  |
> | License Agreement |  | ✓ 1 | ✓ |
> | Primary Language | ✓ |  | ✓ |
> | Primary Category | ✓ |  |  |
> | Secondary Category |  |  |  |
> | Availability in the Republic of Korea2 |  |  | ✓ |
> | Availability in China mainland3 |  |  | ✓ 4 |
>
> 1 Custom License Agreement text box can include localized text.
>
> 2 Required for developers who enroll as an organization and distribute apps on the App Store in South Korea.
>
> 3 Required for apps that meet certain criteria to be available on the App Store in China mainland. Learn about availability requirements.
>
> 4 Enter at any time, but submits for review with the next version submission.
>
> Platform version information
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Screenshots | ✓ | ✓ |  |
> | App Preview |  | ✓ |  |
> | Promotional Text |  | ✓ | ✓ |
> | Description | ✓ | ✓ |  |
> | Keywords |  | ✓ |  |
> | Support URL | ✓ | ✓ |  |
> | Marketing URL |  | ✓ |  |
> | Version Number | ✓ |  |  |
> | Copyright |  |  | ✓ |
> | Routing App Coverage File |  |  | ✓ |
> | App Review Information | ✓ |  | ✓ |
> | Version Release settings |  |  |  |
> | What’s New in this Version |  | ✓ |  |
> | Phased Release for Automatic Updates |  |  |  |
> | Reset overview rating |  |  |  |
>
> App privacy
>
> | Property | Required | Localized | Editable |
> |---|---|---|---|
> | Privacy Policy URL | ✓ | ✓ |  |
> | Privacy Choices URL |  | ✓ |  |
> | Data Types |  |  | ✓ |

In these tables "✓" stands for Apple's check-circle icon (its alt text is the column name: "Required", "Localized", or "Editable"); digits are Apple's footnote markers.

**Applies to:** Apps submitted for Notarization (alternative distribution, EU)

- **[PAGE-150]** Are the required app information properties for Notarization completed: Name, Rating, Bundle ID, SKU, Primary Language, and Primary Category?
  - quote: "The tables below show the app and version properties required to submit your app for Notarization."
  - surface: asc
  - verify: App Store Connect > Apps > (app) > App Information: confirm each of these properties has a value.
  - fix: Fill in the missing properties and click Save.
- **[PAGE-151]** Are the required platform version properties completed: Screenshots, Description, Support URL, Version Number, and App Review Information?
  - quote: "The tables below show the app and version properties required to submit your app for Notarization."
  - surface: asc
  - verify: Version page: confirm screenshots, description and support URL (in each localization), version number and App Review Information are set.
  - fix: Fill in the missing properties and click Save.
- **[PAGE-152]** Is a Privacy Policy URL provided?
  - quote: "The tables below show the app and version properties required to submit your app for Notarization."
  - surface: asc
  - verify: App Privacy (or App Information) page: confirm the Privacy Policy URL is set and loads.
  - fix: Add a Privacy Policy URL.

## Sources

- https://developer.apple.com/app-store/in-app-events/
- https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions
- https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/configure-test-treatments
- https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/create-a-test
- https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization
- https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/run-a-test
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/audio-descriptions-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/captions-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/differentiate-without-color-alone-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/larger-text-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/manage-accessibility-nutrition-labels
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voice-control-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voiceover-evaluation-criteria
- https://developer.apple.com/help/app-store-connect/manage-app-information/add-an-app-icon
- https://developer.apple.com/help/app-store-connect/manage-app-information/complete-the-digital-goods-and-services-questionnaire
- https://developer.apple.com/help/app-store-connect/manage-app-information/declare-regulated-medical-device-status
- https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags
- https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-a-custom-product-page
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-event
- https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-assets-from-asset-library
- https://developer.apple.com/help/app-store-connect/managing-alternative-distribution/submit-for-notarization
- https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events
- https://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events
- https://developer.apple.com/help/app-store-connect/offer-promo-codes/request-and-manage-promo-codes
- https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-asset-statuses
- https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications
- https://developer.apple.com/help/app-store-connect/reference/in-app-events/in-app-event-media-and-audio-specifications
