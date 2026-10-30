=== SOURCE: https://developer.apple.com/app-store/in-app-events/
Watch the latest video: Get started with In-App Events

# In-App Events

In‑App Events are timely events within apps and games — such as game competitions, movie premieres, livestreamed experiences, and more. People can discover your In‑App Events right on the App Store in iOS and iPadOS, so you can showcase your events and reach new, current, and previous users.

## Discovery on the App Store

In-App Events appear across the App Store as event cards that include images or video, the event name, and a short description (on iOS 15 and iPadOS 15, or later). People can tap to open an event details page, which provides a more immersive experience with a longer event description and notes if an Apple In-App Purchase or subscription is required to participate. From this page, they can share your event with others — for example, via Messages or social media. And they can opt in on the event card and event details page to receive a notification from the App Store when your event starts.

If someone doesn’t have your app or game, they can download it directly from your In-App Event card or event details page. Once downloaded, they can tap Open to be seamlessly directed to the appropriate area within your app or game.

Event Card on Product Page

Event Details Page

In-App Events appear:

- On your product page, which displays all of your currently published events.

- In search results. When users search for an app, the event card appears along with your app for users who have downloaded your app, while screenshots show for those who haven’t downloaded your app. Users can also search for In‑App Events directly. When users search for an event, the event card appears along with your app.

- In editorially curated selections and personalized recommendations on the Today, Games, and Apps tabs.

### Marketing your events

You can promote your In‑App Events using email, advertising, social media, and more to create additional awareness and engagement. Be sure to include a link to your event’s details page so people can learn more and download your app or game if they haven’t already.

You can also share your In-App Event with our worldwide team of editors for promotional consideration on the App Store. We highlight new apps and games, as well as those with significant updates, In‑App Events or exclusives, cultural or seasonal moments, and more.

Learn about getting featured on the App Store

Search

Recommendations

Editorial

## Configuring in App Store Connect

In-App Events are easy to set up and manage in App Store Connect. When creating an event, you’ll enter a reference name (visible only in App Store Connect) and event information, including metadata. You’ll also select an event badge and regional availability. You can submit events for review independent of a new app version and have up to 15 approved events in App Store Connect at a time. You can also use the App Store Connect API to automate metadata upload and submission for your events. An app can have up to 10 events published on the App Store at a time.

Good candidates for In‑App Events are challenges, competitions, or special content launches.

The following are not good candidates for In‑App Events:

- Repetitive activities such as daily tasks or rewards.

- Price promotions that don’t introduce any new content, features, or goods.

- General promotions that raise awareness about your app or game. While an In-App Event can highlight added content or features that are permanent or ongoing, the event itself should focus on a related limited-time moment or experience.

### Choosing an event badge

Select the badge that best fits the type of event you’re offering to display above the title on the In-App Event card and event details page.

- Challenge: Activities encouraging the user to achieve a goal before the event ends — for example, a fitness challenge in a workout app or beating a certain number of levels in a game.

- Competition: Activities in which users compete against one another for the highest ranking or to win rewards — for example, a tournament where players battle to win the most matches.

- Live Event: Activities that occur in real-time that all users can experience simultaneously — for example, a sports match or livestreamed concert. These events should provide users with new content, features, or goods.

- Major Update: Introducing significant new features, content, or experiences – for example, the launch of new game modes or levels. These events go beyond minor enhancements like UI adjustments or bug fixes.

- New Season: Introducing new content, storylines, or media libraries to build on established content. For example, a significant sporting event, a battle pass or themed content in a game, or a special episode of a television show. These events should focus on unique content rather than promoting awareness about the entirety of the season.

- Premiere: Introducing new content or media for the first time — for example, a movie debut or newly released audio. These events should focus on the introduction of this unique content, rather than promoting general awareness about your app’s content or service.

- Special Event: Limited-time events that are not captured by another event badge, possibly spanning multiple activities or experiences — for example, an event featuring a collaboration. These events should provide users with new content, features, or goods.

### Creating effective metadata

The metadata you provide is used when displaying your event across the App Store. To ensure a smooth review experience, make sure it accurately portrays your event and is specific to the event experience, rather than sharing general information about your app or promoting its content or services. You’ll enter the following:

Event name: Choose a distinctive, unique name that’s up to 30 characters long and written in title case. This should be the actual name of the event, such as “June Leaderboard Climb,” rather than a call to action or tagline, such as “Watch the livestream.” Avoid generic terms or describing the type of event, since the event badge already displays this information.

Short description: Briefly summarize your In-App Event in up to 50 characters written in sentence case. This information displays on your event card.

Long description: Provide more information about your event — such as potential rewards — in up to 120 characters written in sentence case. This information displays on your event details page.

Event card and event details media: Add an image or video that represents your In-App Event across the App Store. Videos autoplay and repeat, so aim to create a seamless loop. In App Store Connect, you can preview what your provided media will look like in an event card and event details page to confirm that crucial aspects of your image or video will not be obscured.

To ensure your events display properly on the App Store and provide a high-quality user experience, consider these guidelines when creating your metadata:

- Use proper capitalization and punctuation. Avoid using all capitals and don’t use excessive punctuation marks, such as multiple exclamation points.

- Avoid claims that can’t be verified, such as “the best” or “#1,” as well as extra words, such as “game event.”

- Don’t include specific prices in your metadata, as pricing and currencies can vary across regions and can be changed independent of your event. Including specific pricing will lead to rejection by App Review.

- When possible, avoid using text or logos in your media, especially if they include your event name or app name.

- Consider using video in order to provide users with a more dynamic preview of your event.

- Don’t add borders or gradients to your media. Crops and gradients are automatically applied to your media in order to ensure consistency across the App Store.

- Aim to create visual continuity across your event card and event details page by using similar colors or illustration styles.

- Make sure your metadata includes content that you created or have a license to use.

#### Do
Event Card 

Use title case.  
Choose a name that accurately describes the event.  
Use sentence case and describe the event experience.   

Use title case.  
Choose a name that accurately describes the event.  
Use sentence case and describe the event experience.    

#### Don’t
Event Card 

Avoid using text or logos in your media.  

Don’t use a call to action as the name.

Avoid using all capitals.

Don’t use multiple punctuation points.

Don’t use the description to promote your app or services.   

Avoid using text or logos in your media.  

Don’t use a call to action as the name.

Avoid using all capitals.

Don’t use multiple punctuation points.

Don’t use the description to promote your app or services.    

### Adding event details

When configuring your event, you’ll also add additional event details that impact how your In-App Event displays on the App Store.

Determine event availability. When you select start and end dates and times for your In-App Event, you’ll also choose the date and time it appears on the App Store. An In-App Event can last up to 31 days and be promoted up to 14 days before its start date. If you’d like, you can make your event available only in specific regions and customize the dates and times for each location.

Provide an event deep link. This link takes users who tap Open on the In-App Event card or details page to the event content within your app. This can be a universal link (recommended for security) or custom URL. Avoid using URL shorteners and other services that add unnecessary redirects. Test the deep link to make sure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it. Learn about configuring universal links.

Be thoughtful about the most relevant destination to direct users. If your event is live, you can link directly to the event. If your event hasn’t started, you might direct users to a landing page that builds anticipation and reminds them when to return. If a user is new to your app, consider taking them through any necessary onboarding before directing them to the event. Always provide a way for users to return to your main app experience.

Indicate your event purpose. Offering In‑App Events in your app or game can encourage new users to try it, provide existing users with new ways to enjoy your app, and give former users reasons to return. Many In‑App Events are appropriate for all of these purposes, but you may create In‑App Events that are primarily intended for one of these reasons. Choose the option that best fits your event’s purpose:

- Appropriate for all users

- Attract new users: New users are people who have never downloaded your app

- Keep active users informed: Active users are people who downloaded your app and have opened it recently

- Bring back lapsed users: Lapsed users are people who downloaded your app but have not opened it recently

This selection is one of the factors that the App Store uses to offer personalized recommendations and doesn’t display on your event card or event details page. To help your event reach the people it’s intended for, the App Store incorporates app usage information. This data is processed on the device to minimize data collection and enhance user privacy. Regardless of the event purpose you choose, your published events are discoverable on the App Store by all customers.

Designate event priority. Events appear on your product page chronologically based on start time, with the soonest start time displaying first. Any events you select as high priority will appear ahead of normal priority events.

Select cost. Indicate if a specific Apple In-App Purchase is required to participate in the event, as this information is shown on your event details page. For subscription apps, you only need to indicate that an Apple In-App Purchase is required when there’s an additional cost for the event specifically — for example, a pay-per-view event in a subscription app that requires an Apple In-App Purchase in addition to the standard subscription.

### Image and video specifications

Media type Supported extensions Aspect ratio Min size/resolution Max size/resolution    
Event card image .jpg, .jpeg, .png 16:9 1920x1080 px 3840x2160 px  
Event card video .mov, m4v, .mp4 16:9 1920x1080 px 30 fps or 60 fps 3840x2160 px 30 fps or 60 fps  
Event detail page image .jpg, .jpeg, .png 9:16 1080x1920 px 2160x3840 px  
Event detail page video .mov, .m4v, .mp4 9:16 1080x1920 px 30 fps or 60 fps 2160x3840 px 30 fps or 60 fps         

## Measuring event performance

You can use App Analytics in App Store Connect to understand the performance of your published In‑App Events. You’ll be able to:

- Determine which events are best at acquiring app users by viewing downloads and filtering by a specific event.

- Learn where users discover your events by viewing acquisition sources.

- Understand how well your event page engages users by viewing engagement data, such as event impressions, event details page views, and app opens.

- Monitor interest in your event by understanding how many users chose to be notified when your event starts.

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions/
### App Store Connect Help

App Store Connect / Create custom product pages / Configure multiple product page versions 
Filter ⌘K  
Filter ⌘K  

Create custom product pages  

# Configure multiple product page versions

Create up to 70 custom product pages per app on the App Store to highlight features or specific content. Each custom product page can include different screenshots, previews, promotional text, and keywords, and is localizable and shareable through a unique URL.

Custom product pages must be approved before they are visible to users. Learn how to submit a custom product page.

Custom product pages are available on the App Store on iOS 15 and iPadOS 15, or later. Custom product pages are only visible to people if they follow a custom product page link, or if you choose to make your custom product page visible in App Store search results by adding keywords. Otherwise, your app’s default product page displays to all customers on the App Store.

In App Analytics, view App Store metrics such as impressions, downloads, and conversion rate for each page. The metrics are available after a custom product page receives at least five first-time downloads. Learn more about data in App Analytics.

You can optionally add an app deep link to your custom product page. When users running a minimum of iOS 18 or iPadOS 18 click Open on your custom product page, the app deep link directs them to specific content in your app.

-  
An app deep link can be a universal link or custom URL. Use universal links for app deep links to provide users with a secure and integrated mobile experience. Learn about configuring universal links.

-  
Avoid using URL shorteners and other services that add unnecessary redirects.

-  
Test the deep link to ensure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it.

-  
Your app deep link must be approved before it'll function for users. Submit your custom product page for review after you add a deep link in App Store Connect.

Learn how to create and manage a custom product page using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Create a custom product page

You can create a custom product page if your app has the Ready for Distribution status in at least one country or region.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click Create Custom Product Page.

If there’s an existing custom product page, click add button (+).

-  
Enter a reference name to help you identify the page in App Analytics.

-  
Choose whether to start with a blank page or make changes to an existing App Store product page. If you choose to start from an existing page, you can choose a version that’s in the Ready for Distribution state or the Prepare for Submission state and it’ll copy the product page for your primary localization.

-  
Click Create. Your custom product page’s unique URL is automatically generated and displays on this page.

-  
Modify or add additional screenshots, app previews, promotional text, or keywords.

Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.

You can optionally add an app deep link to direct users running a minimum of iOS 18 or iPadOS 18 to specific content in your app.

### Enable keywords for a custom product page

You can assign keywords from your latest approved app version to a custom product page. This directs customers to your custom product page when they search those keywords, rather than your default product page. You can assign keywords in App Store Connect at any time, but the custom product page is searchable only after it’s approved and set to visible.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the custom product page you want to assign keywords to.

-  
In the Keywords section, select the keywords for this custom product page.

Repeat this as necessary for each localization.

-  
Click Publish.

Tip: To ensure the most relevant custom product page appears, select a unique set of keywords for each page.

After assigning keywords to your custom product page, you can disable them individually.

### Edit a custom product page

An approved custom product page can be edited and submitted for review without affecting its unique URL. Changes are published automatically upon approval by App Review.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to edit.

-  
Click Create New Version.

-  
Review the prompt and click Create again to proceed. This creates a new draft of your custom product page in the Ready to Submit state.

-  
Make your edits and click Add for Review.

The submission confirmation screen displays the app version that’ll be associated with the custom product page, and the items that’ll be reviewed. You may choose to add other items to the submission.

-  
Click Submit to App Review.

Once the edited page is approved, it will replace the current page on the App Store.

### Disable a custom product page

You can disable a custom product page at any time. If someone selects a URL for a disabled custom product page, they’re automatically redirected to your default product page.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to disable.

-  
Under the Product Page URL, click Disable Link.

For a disabled link, Enable Link will display instead.

-  
Click Disable.

### Delete a custom product page

You can delete a custom product page at any time. If someone selects a URL for a deleted custom product page, they’re automatically redirected to your default product page. This action is permanent.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to delete.

-  
Scroll to the bottom and click Delete This Product Page.

Related Custom product pages Create search results ad variations Watch "Get started with custom product pages" Watch "Make the most of custom product pages" Watch "Get started with app discovery and marketing"

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/configure-test-treatments/
### App Store Connect Help

App Store Connect / Create product page optimization tests / Configure test treatments 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Configure test treatments

By default, test treatments are copies of your app’s original App Store product page. You can edit the app icon, screenshots, and previews of each treatment. If you choose not to edit one of these items, the metadata from your original product page will display for that item.

Before testing, ensure all metadata in your test treatments is approved. You can submit this metadata without submitting a new version of your app. However, any app icons you wish to use must be part of the app binary for the current App Store version, which should be built with Xcode 13 or later and support alternate icons in asset catalogs through an appropriate SDK.

If you’re simply changing the order of screenshots or previews that are already on the App Store, or only modifying the app icon, your metadata is already approved and you don’t need to resubmit.

Note: Product page optimization tests aren't available for custom product pages or for product pages on the App Store for Apple Watch or iMessage.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Product page optimization.

-  
The default treatment names are Treatment A, Treatment B, and Treatment C. Treatment names are only visible to you in App Store Connect and help you identify treatments in App Analytics. Next to the treatment name you want to edit, click Edit Name.

-  
Enter a treatment name, then click OK.

-  
Click the App Icon tab, which displays if your app binary includes more than one icon. Ensure any icons you want to use are part of the app binary currently on the App Store. This app version must be built with an SDK that supports alternate icons in asset catalogs. Icons must also be sized to 1024x1024 pixels.

-  
Click Change under under the icon of the treatment you want to change.

-  
Choose an icon from the menu that appears. This menu shows all app icons included in your app’s binary. If an app is downloaded from a product page with a test treatment, the test treatment app icon displays throughout the download process and on the user’s device.

-  
Select Header and Search Results or App Previews and Screenshots tab to upload your assets. If you choose not to edit screenshots or previews for a certain device size, the treatment will use the ones on your original product page for that device size. For details on specifications, visit Screenshot specifications and App preview specifications.

Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/create-a-test/
### App Store Connect Help

App Store Connect / Create product page optimization tests / Create a test 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Create a test

Configure product page optimization tests in App Store Connect if your app has a Pre-Order Ready for Distribution or Ready for Distribution status and is live on the App Store. Learn how to design tests.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In the sidebar, click Product Page Optimization.

-  
If you haven’t created a test before, click Create Test. If you've previously created a test, click the add button (+) next to Product Page Optimization.

-  
Enter a reference name to help you identify the test when monitoring results in App Analytics.

-  
Choose the number of treatments you want to create. You can have up to three treatments per test. Please note that the more treatments you add to a test, the longer the test may take to reach a conclusive result.

-  
Choose a traffic proportion. This is the percentage of users that’ll be randomly shown a test treatment instead of your original product page. For example, if a test has three treatments and you choose a 30% traffic proportion, each treatment will be shown to 10% of the total traffic.

-  
Select the localizations you want to include in your test. By default, all localizations that your app supports are selected. If the localization shown to a user is excluded from your test, the user won’t be included in the test.

-  
To view how long it might take to reach your goal, click the arrow next to Estimate Your Test Duration and choose your desired improvement in conversion rate. We use your app’s existing performance data, such as daily impressions and new downloads, to generate this estimate. The estimated duration and impressions needed will appear. This estimate is provided as a guide and won’t impact the test. A test runs for 90 days or until you manually stop it within that time. Keep in mind that it may not be possible to reach your desired improvement in conversion rate within 90 days.

-  
Click Create Test.

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization/
### App Store Connect Help

App Store Connect / Create product page optimization tests / Overview of product page optimization 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Overview of product page optimization

Optimize your iOS or iPadOS app's product page on the App Store by testing up to three different app icons, screenshots, and previews to see which resonate best with customers. Each variant will be randomly shown to a user group you define, and can be localized in any language your app supports. Use App Analytics to evaluate performance and feature the top-performing assets to all users.

The methodology for determining the treatment that’s best at driving app engagement is based on the estimated lift in conversion rate, as well as algorithms that provide confidence in the reliability of the test results. Learn how to view product page optimization results.

Note: Your app must be in the Ready for Distribution state to test its product page. Releasing a new app version while a test is in progress may impact the results if your version contains assets or metadata that are currently being tested. Product page optimization tests aren't available for custom product pages or for product pages on the App Store for Apple Watch or iMessage.

Treatments are shown to users on the App Store on iOS 15 and iPadOS 15, or later.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

Related Creating your product page Get ready to optimize your App Store product page View product page optimization results Product page optimization metrics Make the most of product page optimization Get started with app discovery and marketing

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/run-a-test/
### App Store Connect Help

App Store Connect / Create product page optimization tests / Run a test 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Run a test

Before starting a test, ensure all metadata is approved by App Review for distribution on the App Store. If approval is pending, the metadata will be included in a new submission for review. Learn more about submitting for review.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Start a test

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Product Page Optimization.

-  
Click the name of the test you want to start.

-  
On the top right, click Start Test. The test status automatically updates to Running and shows how long the test has been live.

If your metadata needs to be reviewed, you’ll be prompted to add the test for review. Click Add for Review, then select whether to add the test to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version.

In the submission window, click Submit for Review. The test status will change once the metadata is accepted by App Review.

-  
Your test will run for 90 days or until you manually stop it within that time. Test results appear in App Analytics after there are five first-time downloads associated with the test. Learn how to view product page optimization results.

### Manually stop a test

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Product Page Optimization.

-  
Click the name of the test you want to stop.

-  
On the top right, click Stop Test. Once you stop a test, it can't be restarted. You’ll need to create a new test with the same treatments and run it again.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/audio-descriptions-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Audio Descriptions evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Audio Descriptions evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Audio descriptions are additional dialogue, interspersed between natural pauses in the main audio of a program or interstitial content, that describe to viewers who are blind or low vision what’s happening on-screen during time-based visual content.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Audio Descriptions feature is to support users who are blind or have low vision. Predominantly used in movies and TV shows, audio descriptions (AD) combine the main audio track with additional narration describing inaudible on-screen events. For example, “Mark stares at Gemma through the window. His expression displays inner conflict, as he wonders what to do next.”

When an AD audio track is selected, narration describes for the scene above from Severance as: “In slow motion, Mark and Helly run together down a long white hallway flashing with red light.”

The following sections provide more detail about how to determine whether your app supports Audio Descriptions well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Audio Descriptions on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Audio Descriptions, your app should still enable audio descriptions by default when detecting the systemwide audio descriptions setting. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Review the resources below to learn how to enable audio descriptions for each device your app supports.

-  
For iPhone, visit Hear audio descriptions for video content on iPhone.

-  
For iPad, visit Hear audio descriptions for video content on iPad.

-  
For Mac, visit Change Audio Descriptions settings for accessibility on Mac.

-  
For Apple TV, visit Use audio descriptions on Apple TV.

-  
For Apple Vision Pro, visit Hear audio descriptions for video content on Apple Vision Pro.

## Indicating support for Audio Descriptions

You may say that your app supports Audio Descriptions if it provides narrated descriptions of relevant on-screen content for video played in your app, including game interstitials and audible dialogue. 

-  
Even if your app doesn’t include movies or TV shows, there may be other areas where your app presents on-screen time-based content that may not be available through another form of sensory perception. For example, opening sequences, game interstitials, and cut scenes should be described, even if they’re not delivered in a standard video player. You should also describe tips and hints that are otherwise only available through visual clues.

-  
As one uncommon but creative example, a video streaming service might choose to provide an audio-only watchOS app, and automatically select the audio description track.

Audio Descriptions in third-party content

If your app presents third-party content, such as video posts in a social media app, videos added by the user in a presentation app, or TV or movie streaming in an entertainment app, users should have the ability to include an audio description track for your app to present. To indicate support for Audio Descriptions, you’re not responsible for ensuring every piece of third-party media has audio descriptions. However, you should ensure the following:

-  
Users should be able to determine which pieces of media content are audio described. For example, most video streaming service apps will present an “AD” icon on videos that include audio descriptions. 

-  
If your app includes the functionality to select audio descriptions, but very little or no described content is available on your app, don’t indicate support for Audio Descriptions.

-  
Consider evangelizing audio descriptions to your content providers so more video content has audio descriptions.

## Additional suggestions

-  
Creating great audio description content is a creative process that many movie and TV production teams have started to author and record in-house. Others contract this work to external service firms that specialize in audio description, captioning, and other types of accessible media.

-  
If you or your content partners will be developing the audio descriptions yourself, try watching one of your favorite movies or shows with audio descriptions enabled. Pay attention to the details, like the tone of voice, and terseness that is necessary in some scenes. Pay attention to the detail provided in scenarios like end credits. Apple TV+ provides audio description content in multiple languages, and most other major streaming services provide audio description content as well.

Even after you’re able to indicate support for Audio Descriptions in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Audio Descriptions every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, and Captions.

Related Selecting Subtitles and Alternative Audio Tracks Media Accessibility

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/captions-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Captions evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Captions evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Captions are usually time-synchronized text alternatives for dialogue and relevant sounds in videos or some forms of audio-only content. Captions are an accommodation for the Deaf and hard of hearing communities, but captions are also used widely by those without hearing loss.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Captions feature is to support users whose system settings express a need or desire to have audible dialogue and other sounds visibly rendered on screen, or to an alternate output device like a tactile braille display. Captions are a critical accommodation for the Deaf, DeafBlind, and hard of hearing communities, but captions are also used widely by those without hearing loss.

The following sections provide more detail about how to determine whether your app supports Captions well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Captions on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Captions, your app should still enable captions by default when detecting the systemwide captions setting. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Review the resources below to learn how to turn on systemwide captions for each device your app supports.

-  
For iPhone, visit Display subtitles and captions on iPhone.

-  
For iPad, visit Display subtitles and captions on iPad.

-  
For Mac, visit Use subtitles and closed captions on Mac.

-  
For Apple TV, visit Turn on closed captions and SDH.

-  
For Apple Vision Pro, visit Display subtitles and captions on Apple Vision Pro.

## Indicating support for Captions

You may say that your app supports Captions if it provides captions for video played through your app, including game interstitials and audible dialogue. You may also indicate support for Captions if your app provides text transcripts of audio-only content, such as music lyrics or spoken dialogue in podcasts.

-  
For video content, you may indicate support for Captions if your app has dialogue-only subtitles for primary and alternate languages, but consider improving your pipeline to offer closed captions or SDH, which also includes relevant non-verbal audio such as “[doorbell rings]” or “[dog barks].”

-  
Even if your app doesn’t include movies or TV shows with typical subtitles or closed captions, there may be other areas where your app presents spoken dialogue or other relevant sounds. Game interstitials, for example, often include dialogue that should be captioned, even though it’s not delivered with standard captions in a standard video player.

-  
If your app provides verbal audio content, such as music with lyrics or spoken podcasts, consider providing a text copy of that content as a transcript. Text transcripts don’t need to be time-synchronized, and you may indicate support for Captions based on the inclusion of high quality transcripts. For example, even though watchOS apps don’t support video playback, a watchOS app could include music lyrics or a transcript for spoken audio.

Captions in third-party content

If your app presents third-party video content, such as video posts in a social media app, videos added by the user in a presentation app, or TV or movie streaming in an entertainment app, users should have the ability to include caption data for your app to present. To indicate support for Captions, you’re not responsible for ensuring every piece of third-party media has captions. However, you should ensure the following:

-  
Users should be able to determine which pieces of media content are captioned. For example, most video streaming service apps will present a “CC” or “SDH” icon on videos that include captions, along with other details about available subtitle languages.

-  
If your app includes the functionality to display captions, but very little or no captioned content is available on your app, don’t indicate support for Captions.

-  
Consider evangelizing captions to your content providers so more video content has captions.

Even after you’re able to indicate support for Captions in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Captions every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, and Audio Descriptions.

Related Selecting Subtitles and Alternative Audio Tracks Caption Authoring Improving accessibility support in your visionOS app: Include captions for audio content  Media Accessibility

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Dark Interface evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Dark Interface evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Users with light sensitivity can maintain a dark user interface for the common tasks of the app to reduce eye pain or discomfort.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Dark Interface capability is to support users with light sensitivity for whom large white or bright areas on the screen may cause discomfort or even physical pain. Keep this in mind, because the goal isn't only to make the interface dark, but to keep it that way. Even temporary flashes of bright content may cause discomfort or a difficult user experience.

The following sections provide more detail about how to determine whether your app supports a Dark Interface well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Dark Interface on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Dark Interface, we recommend reviewing how Apple’s system apps respond to the systemwide setting to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

To ensure proficiency in testing with a dark interface, review the resources below to learn how to turn on Dark Mode for each device your app supports.

-  
For iPhone, visit Adjust the screen brightness and color on iPhone.

-  
For iPad, visit Adjust the screen brightness and color on iPad.

-  
For Mac, visit Use a light or dark appearance on your Mac.

-  
For Apple Vision Pro, visit Change the appearance of text, app windows, and more on Apple Vision Pro.

A common mistake is supporting sufficient contrast in your light mode interface, but forgetting to support sufficient contrast in a dark interface. Many developers use gray-on-black for dark mode reading, which can reduce eye strain for standard vision in low-light scenarios, but this reduced contrast variant may be more difficult to read for those with low vision or light sensitivity. Consider testing your app while combining the dark mode color scheme alongside the Increase Contrast accessibility setting.

## Indicating support for Dark Interface

You may indicate support if your app is dark by default for all common tasks, excluding any third-party or user-generated content. For example, most apps on tvOS and watchOS are dark by default.

If your app isn’t dark by default for all common tasks, you may still indicate support if it allows the user to enable a mode or setting that keeps the interface dark. This can include supporting the systemwide Dark Mode appearance or using a custom dark color scheme, or as a last resort, supporting the systemwide Smart Invert accessibility setting.

-  
Be careful of unintended color changes that may cause user confusion. For example, if relying on the Smart Invert setting, a red “Delete” button may invert to green if you don’t account for the color inversion. Additionally, when Smart Invert is enabled, make sure the colors in the media don’t appear inverted.

-  
For translucent views, including Apple Vision Pro apps using passthrough, you may indicate support for Dark Interface if your app renders only dark UI. You’re not responsible for background light filtering through your app. However, consider whether your app should reduce the translucency if the system Increase Contrast or Reduce Transparency settings are enabled.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Even after you’re able to indicate support for Dark Interface in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Dark Interface every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related 
Human Interface Guidelines > Dark Mode
Supporting Dark Mode in your Interface Watch “Make your app visually accessible”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/differentiate-without-color-alone-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Differentiate Without Color Alone evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Differentiate Without Color Alone evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Users shouldn't have to rely on color to distinguish different selection states or values in an app. Instead, apps should use additional methods beyond color, such as text labels or icons, to convey information to users with common forms of color blindness.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal is to ensure that your app doesn’t exclude users who may not be able to perceive all colors. Color blindness is one of the most common forms of disability, affecting up to 10% of some populations.

Color is extremely useful in communicating information quickly. Don’t remove color from your app to support this capability; just make sure color isn’t the only way you’re conveying information.

The following sections provide more detail about how to determine whether your app supports Differentiate Without Color Alone well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Differentiate Without Color Alone on the App Store.

### Getting started with testing

A great way to evaluate your app is to try testing using the Grayscale color filter in Accessibility Display settings. While this's not a representation of what color-blind users see, it's a good way to discover unanticipated problems with the use of color in your app. If you can’t use your own app in grayscale, rethink your app’s design and differentiate without color alone.

Ideally, your app should be designed by default to convey information using more than color alone. Using a setting to invoke this experience should be a last resort or stop-gap solution until your app's reliance on color can be improved.

## Indicating support for Differentiate Without Color Alone

You may indicate your app supports Differentiate Without Color Alone if the common tasks of your app don't rely on color as the only way to convey information. For example, a game may distinguish teams using symbols, in addition to representing them with colors. If your app does use color as the only differentiator (e.g. color-coded charts), make sure that users can customize the design for their needs with a setting or by choosing multiple color schemes.

-  
Consider where your elements, controls, or content rely solely on color to differentiate or communicate key information. Examples include status buttons or icons whose only distinguishing difference is red 🔴 vs green 🟢 to indicate positive or negative, online or offline. This visual difference may not be easy for people with red-green color-blindness to perceive.

-  
Instead of relying on color alone, consider using placement, order, shape, iconography, or other stylistic differences in addition to color. Differences like a red square 🟥 or green circle 🟢 are perceivable by all sighted users, regardless of color perception ability.

-  
Consider allowing multiple color schemes so users can avoid the problematic color combinations they have difficulty distinguishing. One example is in apps and games where color is used to indicate different teams or characters.

-  
In complex charts or data visualization apps, consider arranging the chart colors in the same order as the legend keys. Alternatively, you can provide options for in-chart iconography or labels on each element directly to help communicate the data.

Note: These differences reduce cognitive load and help users of all abilities remember what each color means.

For Someone with red-green color blindness, these indicators might appear the same.  
Both visual indicators and color help differentiate between indicators.   

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Even after you’re able to indicate support for Differentiate Without Color Alone in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Differentiate Without Color Alone every time you update the app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related 
Human Interface Guidelines > Vision > Convey information with more than color alone
Watch “Make your app visually accessible”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/larger-text-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Larger Text evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Larger Text evaluation criteria

iOS tvOS visionOS watchOS  

## Description

Users can adjust the size of text and icons to make them more legible, visible, and comfortable to read.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. Ensuring that extra large fonts work well in your app makes the interface more convenient and accessible to more people. While some low-vision or legally blind users may be able to manage default font sizes by using screen zoom or holding their device extremely close to see the text and small icons in your app, this isn't a good user experience.

The following sections provide more detail about how to determine whether your app supports Larger Text well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Larger Text on the App Store.

### Getting started with testing

Allow primary content such as body text to scale as large as possible, while retaining usability and informational hierarchy in your app. Many accessibility guidelines recommend allowing users to enlarge text to 200% or larger than the default size. Dynamic Type on iOS, for example, reaches sizes larger than 200% at the AX3 size, and allows body text sizes over 300% at the AX5 size. Testing your app at the largest sizes helps you catch issues such as truncated or overlapping text.

Be sure to design for and test small, medium, large, and extra large accessibility sizes.

While you’re not required to use Apple frameworks to indicate support for Larger Text, we recommend reviewing how Apple’s platform and apps respond to the systemwide settings to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Design and test your app at all text sizes, including extra large accessibility sizes.

-  
For iPhone, watch “How to adjust text size on iPhone or iPad” and visit Make text easier to read on iPhone.

-  
For iPad, watch “How to adjust text size on iPhone or iPad” and visit Make text easier to read on iPad.

-  
For Apple Vision Pro, visit Text display settings on Apple Vision Pro.

-  
For Apple Watch, visit Adjust text size and other visual settings on Apple Watch.

## Indicating support for Larger Text

You can indicate that your app supports Larger Text if users can enlarge text to at least 200% or the maximum font size for the system. Allow users to resize text and meaningful icons as large as possible. Body text in the primary iPhone, iPad, and Mac views should increase in size without affecting readability through overlapping layouts or severe truncation. If you have controls that can't reasonably increase in size, review the details below for other ways to make those perceivable, usable, and understandable.

Don’t rely on system-provided assistive technology like Zoom or Hover Text to claim support for Larger Text. These features are available to users regardless of your app’s implementation, so users will already be aware that they can enlarge most or all on-screen text to a sufficient size using Zoom or Hover Text.

The Larger Text label is useful to users of your app as a way to determine whether the user interface of your app supports font size enlargement separate from these built-in features like Zoom. You may indicate support for Larger Text, either by using an Apple-provided feature like Dynamic Type, or by using your own in-app font size control to achieve equivalent font sizes.

You’re not required to adopt Apple frameworks to indicate support for Larger Text, but we recommend detecting when a user has Apple system settings enabled so they don’t have to manually update another setting for the app to function as expected. If you offer your own in-app setting that has additional customization or granular controls, you may not need to use the Apple system setting.

If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Use the system font size, or manage your own.

Most iOS apps typically use Dynamic Type, but some developers of games or apps that rely heavily on the use of text may choose to manage their own font sizes with an in-app setting. For most apps, using system frameworks is easier and more reliable than implementing your own.

Apple Books is a good example of an app that supports larger text well, but doesn’t rely on Dynamic Type. While the Books app doesn’t leverage the system font size setting, it offers more granular controls. For example, users can change text to their preferred size, and the app’s layout changes from two columns to a single column at larger text sizes in landscape orientation, so that low-vision users can perceive more words in an uninterrupted line of text.

Safari on iOS is another great example of an app with a custom font size controller. Since not all web pages scale to larger text sizes well, Safari allows users to adjust the font size for each site they visit. If your app uses a web view as part of its common tasks, provide a font size controller or let Safari handle this task for your users.

Use responsive design principles to adjust layout and information hierarchy based on needed text size.

Consider which text to enlarge to reinforce a clear information hierarchy to low-vision users of your app, and prioritize scaling the main content areas before repeated, predictable navigational elements.

Consider the value of screen real estate when determining which elements to scale. For example, the Back and Edit buttons on iOS remain small in the example below because they are repeated, predictable, and secondary elements of the interface. Primary content and action buttons are enlarged, extending to full screen width and lengthening the page to use the available space.

Smaller side-by-side elements may overlap when enlarged, so consider wrapping them onto a new line or laying them out vertically rather than horizontally. In the example below, the layout of the message sender, receiver, and date changes from horizontal to vertical to support larger text sizes.

Keep in mind that some features, like Tab Bars, don’t grow with dynamic text to avoid overlapping valuable screen estate. Consider other ways to make those elements accessible, such as the Large Content Viewer.

Avoid overlapping text and excessive or unusable truncation.

Scaling text to much larger sizes may produce unpredictable results, especially on devices with smaller screens. As text is enlarged, consider how that changes the experience:

-  
Content may overlap making it difficult to read.

-  
Content designed for a single line might become truncated, showing only the first few characters. 

Follow these principles for a great experience: 

-  
Avoid overlapping text.

-  
Avoid truncating text to the point that it becomes unreadable or ambiguous for the user. Consider allowing the text to wrap to two or more lines instead of truncation.

-  
If text is truncated, ensure that users are still able to access the same information as if the text were smaller. For example, in a list view, you can truncate text to a single line or two as long as the full text is available in a different view so users can dive into the details. 

-  
Test your app's larger text layout with different languages. In addition to languages with a longer average word length, test right-to-left languages and those with larger ascenders, descenders, and diacritics that may by clipped by layout constraints.

## Larger Text on tvOS apps

Scale most text in your tvOS app to retain a relative information hierarchy. Section headings and media titles must remain larger than less important description text, even if the scaling isn't exactly proportional.

Rather than focusing on a particular percentage increase, scale the smallest text element as large as possible while retaining the overall usability, information hierarchy, and feel of your app. Watch Prepare your tvOS apps for Dynamic Type for tips on adopting Dynamic Type and design considerations for larger text sizes in tvOS.

You can indicate support for Larger Text in your tvOS app by supporting the largest Dynamic Type size or an equivalent font size using your own implementation.

## Larger Text on watchOS apps

Because Apple Watch has a smaller screen, the largest Dynamic Type size on watchOS is larger than 140% of the default size. You can indicate support for Larger Text on your watchOS app by implementing Dynamic Type or by supporting an equivalent or larger size for body text or other primary content.

You might also consider some of the techniques employed by the X-Large watch faces, where each complication can be set up as its own watch face, taking advantage of the full screen size. Low-vision users can still view multiple complications (including your app’s watch face complications) by swiping through each of their saved watch faces.

Even after you’re able to indicate support for Larger Text in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Larger Text every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Watch “Get started with Dynamic Type” Watch “Large Content Viewer - Ensuring Readability for Everyone” 
Human Interface Guidelines > Vision

Human Interface Guidelines > Typography
Scaling Fonts Automatically Applying custom fonts to text

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/manage-accessibility-nutrition-labels/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Manage Accessibility Nutrition Labels 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Manage Accessibility Nutrition Labels

Review the evaluation criteria for each label before you begin indicating support for the accessibility features.
Learn how to manage Accessibility Nutrition Labels with the App Store Connect API. 
Required role: Account Holder, Admin, Finance, App Manager, or Marketing. View role permissions.

## Indicate your app’s accessibility support

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Accessibility.

-  
On the right, click Get Started.

-  
We automatically detect the devices your app supports if your latest app version is live on the App Store, or if your app record only support one device, like Mac. If the latest version of your app is in an editable state, like Prepare for Submission, select the devices you want to add accessibility support for, then click Save.

-  
Click Add [Device] Support for the relevant device.

-  
Select Yes if your app supports any of the accessibility features on the selected device, or No if it doesn’t support any of the features, then click Next.

-  
Select the accessibility features that your app supports, then click Next. 

-  
Your responses will be saved as a draft. Click Publish to publish your responses to the App Store. 

You can only publish support for devices that have a live version on the App Store.

If you’ve indicated support for multiple devices, you’ll need to confirm the devices you want to publish support for. Select each applicable device, then click Publish again.

The responses will be published immediately but may require up to 24 hours to be visible to all users.

### Update your app’s accessibility support

You can update your app accessibility responses at any time. 

-  
In Apps, select the app you want to view.

-  
In the sidebar, select App Accessibility.

-  
On the right, click Edit next to the device you want to update your responses for.

-  
Make your desired changes, then click Save.

-  
Click Publish to publish your updated responses to the App Store.

The changes will take effect immediately but may require up to 24 hours to be visible to all users.

### Manage the accessibility URL

If you have other accessibility information you'd like to provide, you can optionally include a URL. This link will show on your app's product page across all devices, except Apple TV.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select App Accessibility.

-  
Below Accessibility URL, click Add URL.

To update the accessibility URL, click Edit next to the existing URL.

-  
Enter your URL, then click Publish.

If your app is already live on the App Store, the URL will be published immediately but may require up to 24 hours to be visible to all users. If you haven’t published any versions of your app yet, the accessibility URL will automatically go live with the first release.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Overview of Accessibility Nutrition Labels 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Overview of Accessibility Nutrition Labels

The Accessibility Nutrition Labels help users learn if an app will be accessible to them before they download, and give developers the opportunity to better inform and educate their users on features that their app supports. The labels appear on the app product page and will help users understand if they can use a feature like VoiceOver or Larger Text to complete common tasks in the app.

In order to give you time to prepare and evaluate your apps, providing these labels will be voluntary to start. However, you’re encouraged to report your accessibility support to help everyone, including people with disabilities, better discover apps that fit their needs. You’ll be given ample time and evaluation resources before this is mandatory, but over time, you’ll be required to share accessibility support details to submit new apps and app updates to the App Store.

## Types of Accessibility Features

Below are the accessibility features you can provide Accessibility Nutrition Labels for. We recommend that you evaluate your features in this order. Most of the work that goes into making your app accessible to VoiceOver users, for example, can also make it more accessible for users of other assistive technologies, like Voice Control and more.

Some accessibility labels aren’t available on some devices, as indicated in the table below, so you’ll be prompted to indicate support only for the accessibility features that are applicable to each device in App Store Connect.

Accessibility feature

Description

VoiceOver

Users can navigate and explore the app using gestures, keyboard, braille, and speech output.

Voice Control

Users can navigate and interact with the app using their voice to tap, swipe, click, type, and more. This isn't supported on Apple TV and Apple Watch.

Larger Text

Increases the text size in the app to 200% or more. This label isn't supported on Mac.

Dark Interface

Applies a dark color scheme to the screens, menus, and controls to reduce eye strain.

Differentiate Without Color Alone

Uses shapes or text, in addition to or instead of color, to distinguish key information.

Sufficient Contrast

Increases or adjusts the contrast between text or iconography and background.

Reduced Motion

Modifies or reduces certain types of animation that may cause motion sickness or discomfort.

Captions

Users can follow the dialog and relevant sounds of video or audio-only content with time-synchronized text.

Audio Descriptions

Users can hear audio descriptions of video content in a clip, show, or movie with time-synchronized narration.

## Discovery on the App Store

The Accessibility Nutrition Labels will appear on your app’s product page in all countries or regions where your app is available. The App Store displays the labels specific to the device type (iPhone, Mac, etc.) used to view your product page.

Note: The Accessibility Nutrition Labels will appear on Apple devices running iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26 or later.

You have the option to provide information for each device your app supports in App Store Connect. If you don’t provide this information for a device, the section will still appear on your product page and show that you haven’t indicated support yet. This section will also indicate if your app supports none of these accessibility features.

You also have the option to provide an accessibility URL that links to your website so that users can learn more about the app’s accessibility features. This link will show on your app's product page across all devices, except Apple TV. This accessibility URL should correspond uniquely to your app and can include information such as other accessibility features, how to turn on and manage any in-app accessibility settings, what languages are supported in captions, or areas of your app that don’t support an accessibility feature.

Users can include Accessibility Nutrition Label features as part of their search query to make their results more relevant. For example, in searches like “VoiceOver note taking apps” or “running apps with Larger Text,” apps that have indicated support for those features in their labels will be considered more relevant in search results.

## Planning for your responses

To encourage developers to respond consistently across all apps, the App Store has set evaluation criteria a developer should meet before indicating support in the Accessibility Nutrition Labels.

Before providing your responses in App Store Connect, you’ll need to audit your app to understand the level of support it provides and how it aligns to the App Store’s standards for each accessibility feature. Since your app’s support of an accessibility feature can differ per device and you can provide responses for each device in App Store Connect, you should assess your app on each of the devices your app supports.

To indicate support for an accessibility feature in the Accessibility Nutrition Labels, users must be able to complete all of the common tasks of your app using that feature.

In addition to following the evaluation criteria, make sure to follow App Review Guideline 2.3 for accurate metadata. If an app potentially has intentionally misleading or harmful accessibility labels, App Review has the ability to contact the developer and ask them to update their Accessibility Nutrition Labels.

You’re responsible for keeping your responses accurate and up-to-date. If your practices change, please update your responses.

### Identifying the common tasks in your app

To indicate support of an accessibility feature in the Accessibility Nutrition Labels, users should be able to complete all of the common tasks of your app using that feature. Before you begin evaluating features, compile a list of the common tasks that a person can perform in your app.

Common tasks checklist

Common tasks consist of the primary functionality that you expect users to perform in your app, plus functionality that's fundamental to using an app in general: first launch experience, login, purchase, and settings.

-  
Primary functionality specific to your app

-  
To indicate support for an accessibility feature, a user should be able to perceive, operate, and understand all of the primary functionality specific to your app while using the feature.

-  
To come up with your list of primary functionality, start by defining the key goals, functionality, and features users download and use your app for. It may be helpful to consider what you market in your app’s description, screenshots, and app previews.

As an example, a to-do list app’s common tasks will include these tasks below.

-  
View task list

-  
The user may need to mark a task as complete, undo marking a task as complete, change the due date, or create a new task.

-  
Task detail view

-  
For a new or existing task, the user may need to enter information about the task, save the task to a list, or exit the screen without making modifications.

-  
First launch experience

-  
To indicate support for an accessibility feature, a user should be able to complete the app’s first launch experience while using the accessibility feature. For example, your first launch experience may have a video with sound that you may want to express in captions, or an onboarding flow that a user should be able to complete or skip.

-  
Login

-  
To indicate support for an accessibility feature, a user should be able to complete the login experience while using the accessibility feature. For example, the user should be able to choose a login service, enter a username and password, interact with a login button, request a password reset, or enter information to create a new account.

-  
Purchase

-  
If your app offers purchases, to indicate support for an accessibility feature, a user should be able to complete the purchase experience while using the accessibility feature. For example, the user should be able to select a payment provider, enter a credit card number, review the terms of an offer, or review before completing the purchase.

-  
Settings

-  
To indicate support for an accessibility feature, a user should be able to adjust app settings while using the accessibility feature. For example, the user should be able to turn on accessibility or privacy features, manage purchases, or exit the settings screen without modifying settings.

Ensuring a comprehensive list

As you make your list, consider the following to ensure you have a comprehensive list of common tasks:

-  
Make sure your list includes common tasks that users both with and without disabilities can perform.

-  
Consider differences by device, such as if a certain experience is only available on Apple Watch but not Mac.

-  
Include tasks that you make mandatory to use your app, such as account sign-up or purchasing a subscription.

-  
Especially for new users, consider default and loading screens, such as the screen to view the task list when the user hasn’t added tasks yet.

-  
Consider actions a user can take outside your app that are common tasks, such as marking a task complete in a notification or widget from your to-do list app.

-  
When evaluating, you're not required to consider tasks that are uncommon in your app. If you're unsure if a task is common, ask yourself whether you'd ship an urgent fix if users were blocked from completing this task. For example, if your app provides links to your app’s marketing channels on social media and web but that isn’t a key goal of using the app, you're not required to include it in your evaluation. If you want to provide more information about the accessibility of uncommon tasks, use the accessibility URL to do so.

Recommended: Create an accessibility testing matrix

After you identify your app’s common tasks, to guide your evaluation, it may be helpful to create an accessibility testing matrix for each device you plan to provide Accessibility Nutrition Labels for in App Store Connect. Following this matrix isn’t required, but it can help make sure you’re validating that all common tasks can be completed for an accessibility feature on that device. This is especially helpful since some of your app’s common tasks may not be available on some devices, and some accessibility features aren’t available on certain devices.

To start, create a matrix for each device you’ll be evaluating for Accessibility Nutrition Labels.

For each matrix, take the common tasks that are available on that device, and add them as rows. For example, if a common task is only available on Mac but not Apple Watch, include the common task in your matrix for Mac but not your matrix for Apple Watch.

Next, consider the accessibility features you want to evaluate. Since some accessibility features aren’t available on certain devices, you won’t be able to provide Accessibility Nutrition Labels for them. Take the accessibility features that are available on that device, and add them as columns.

Now you're ready to evaluate your app.

## Tips

Implementation

-  
Whenever possible, use the Apple-provided native API to reduce implementation complexity and so customers who have turned on the system setting will automatically get this experience without an additional setting. We highly recommend Apple-provided native APIs for complex app behaviors, such as drag and drop or multi-touch gestures.

-  
Provide native support for core assistive technologies, including VoiceOver and Voice Control. These assistive technologies allow connection to hardware interfaces, such as braille displays, and interaction with operating system features, like app switching, that your app otherwise wouldn’t be able to support. Don’t attempt to make a custom implementation of the functionality provided by core assistive technologies like VoiceOver or Voice Control.

-  
With the exception of core assistive technologies like VoiceOver and Voice Control, you may use a custom implementation to indicate support for your labels, such as a custom dark color scheme, instead of using the system’s standard dark appearance.

-  
Even if you use a custom implementation for an accessibility feature, consider leveraging the user’s system setting to ensure your app responds to their needs. For example, if you render custom captions in a game, check the user’s system setting that indicates a need or preference for displaying captions when available. If you offer your own in-app setting, it should offer more granular user interface customization than the system setting provides.

-  
Pay extra attention to custom elements, since they are less likely than standard elements to have accommodations for accessible experiences. Additionally, some custom elements may require additional work to support features like VoiceOver and Voice Control.

Third-party content

-  
You don’t have to consider third-party or user-generated content when evaluating accessibility labels if those views aren’t part of your common tasks.

-  
When third-party or user-generated content views are part of your common tasks, you don’t need to ensure all third-party content is accessible, but your app should provide the third-party content creators a reasonable, discoverable way to make their content accessible. For example:

-  
In most video streaming apps, developers support a way to display closed captions, even though not all third-party movie and television studios provide captions with their video content.

-  
In apps that allow users to upload images, developers should provide a way for the users to label the image, so the image content is perceivable to VoiceOver users.

-  
In apps that use a web view to load third-party websites, WebKit provides default support for most accessibility labels for web content by using web standards like HTML, CSS, and ARIA.

-  
In addition, web browsers like Safari provide additional accessibility features, like site-specific font size settings, which allow users to enlarge the font sizes of web sites to 200% the default size, or sometimes larger.

Best practices

-  
The common guiding principles of accessibility are that content, controls, and interfaces should be perceivable, operable, understandable, and robust. Keep these principles in mind as you’re evaluating your app. For example, a blind VoiceOver user should be able to perceive the content of a visual photograph or icon, often by experiencing its text alternative label as speech or braille. Likewise, if most users can operate an item by tapping, clicking, or dragging it, the item should also be operable to assistive technologies like VoiceOver and Voice Control, so that users with disabilities can use all the same functions of an app.

-  
You may consider exceptions to the recommendations here if users with disabilities would find them reasonable. For example, you might hide a button from VoiceOver in one view if it duplicates functionality that’s already available and discoverable elsewhere.

## Additional guidance

Your app has bugs that affect its accessibility.

If bugs are significant enough to change your answer according to the Accessibility Nutrition Labels evaluation criteria, then don’t indicate support for the accessibility feature. To avoid misleading users, you shouldn’t enter answers that aren’t aligned with the evaluation criteria.

An accessibility feature doesn't apply to your app.

Review the evaluation criteria for the accessibility feature to determine if it's applicable and whether to indicate support.

You have additional accessibility information to share with users.

Add an accessibility URL to your product page to provide users additional accessibility information, such as other accessibility features, how to turn on and manage any in-app accessibility settings, what languages are supported in captions, or areas of your app that don’t support an accessibility feature feature.

Your app includes app extensions.

Your app may include app extensions such as stickers, custom keyboards, Safari extensions, or photo editing extensions. To determine whether to include app extensions in your evaluation, determine whether they are part of your app’s common tasks. If using the app extension isn't part of your app’s primary functionality, then it's unlikely to be one of your app’s common tasks.

Your app has advertising.

Include advertising in your evaluation if it’s present in the UI when users are completing your app’s common tasks. If the advertising experience prevents users from completing a common task using an accessibility feature (for example, the advertisement contains problematic motion that can't be addressed by a system or in-app setting to reduce motion), then don’t indicate support for the feature.

Your app is a compatible iPhone and iPad app on Apple Vision Pro.

If your iPhone and iPad app is compatible with and can run on Apple Vision Pro, no responses are needed for Apple Vision Pro. The labels for iPhone or iPad will be shown to users on the Apple Vision Pro App Store.

Your app is a compatible iPhone and iPad app on Macs with Apple silicon.

If your iPhone and iPad app is compatible with and can run on Macs with Apple silicon, no responses are needed for Mac. The labels for iPhone or iPad will be shown to users on the Mac App Store.

At Apple, we believe that the best technology works for everyone to help them connect, create, play, and do what they love in the ways that work best for them. Even after you’re able to claim support for an accessibility feature in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Can all users use all features of the app, not just the common tasks? While it’s not required, we encourage you to go beyond this criteria to provide the most accessible experience you can for all users.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Watch “Prepare your app for Accessibility Nutrition Labels” Watch “Evaluate your app for Accessibility Nutrition Labels”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Reduced Motion evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Reduced Motion evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Motion can enrich app experience, but certain types of motion, such as scaling, spinning, or peripheral motion, cause dizziness or nausea for people with motion sensitivity. Although motion sickness is commonly discussed in the context of augmented and virtual reality, motion can cause reactions in 2D screens as well for users with severe motion-sensitivity conditions. If your app includes these motion triggers, make them optional or provide alternative animations.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability.

The goal of Reduced Motion is to support users with extreme motion sensitivity, who may experience negative side effects, such as nausea, dizziness, headaches, or distraction when encountering certain types of motion triggers. Often, the problematic types of motion are spinning or scaling, and other techniques used to simulate three-dimensional effects or depth.

Well designed animations can convey information intuitively, increasing the usability and understandability of your app. Removing such animations unnecessarily might make your app experience more confusing, so don’t remove or modify all animations prematurely. Review the support criteria below to determine which animations to leave as they are, which animations to modify, and which animations to consider removing entirely.

The following sections provide more detail about how to determine whether your app supports Reduced Motion well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app supports Reduced Motion on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Reduced Motion, we recommend reviewing how Apple’s system apps respond to the systemwide setting to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Review the resources below for details about enabling the Reduce Motion system setting on each device your app supports.

-  
For iPhone, watch “How to reduce screen motion on iPhone, iPad, and iPod touch” and visit Customize onscreen motion on iPhone.

-  
For iPad, watch “How to reduce screen motion on iPhone, iPad, and iPod touch” and visit Customize onscreen motion on iPad.

-  
For Mac, visit Customize onscreen motion on Mac.

-  
For Apple TV, visit the Reduce screen motion on Apple TV 4K.

-  
For Apple Vision Pro, visit Stop or reduce visual motion effects or screen movements on Apple Vision Pro.

-  
For Apple Watch, visit the Adjust text size and other visual settings on Apple Watch.

If you don’t have an existing proficiency in testing reduced motion, take some time to go beyond the basics and review the additional resources below.

-  
Human Interface Guideline > Motion

-  
Human Interface Guideline > Accessibility

## Indicating support for Reduce Motion

You’re not required to adopt Apple frameworks to indicate support for Reduced Motion, but we recommend detecting when a user has the Apple system setting enabled so they don’t have to manually update another setting for the app to function as expected. If you offer your own in-app setting that has additional customization or granular controls, you may not need to use the Apple system setting.

When testing your app, determine if any views or transitional animations include potential motion triggers that can cause discomfort or distraction for some users. If your app doesn’t contain any problematic motion triggers, you may indicate that it supports Reduced Motion.

-  
If your app uses depth simulation (including parallax effects, animated blur, and depth-of-field effects), you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion.

-  
If your app includes multi-axis motion, multi-speed motion, spinning, or vortex effects, you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion.

-  
If your app includes auto-advancing carousel screens or any other ongoing motion, consider stopping the motion based on the user’s setting, or providing a control to allow the user to stop the motion.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

-  
Review the related links below for more examples of motion triggers.

If your app does contain these types of motion, consider each animation individually.

-  
Is the animation included purely for stylistic or decorative effect? If so, consider stopping it entirely when the user’s system setting indicates a need or preference for reduced motion.

-  
Removing animations entirely can have a negative effect on usability and understandability. If the motion itself conveys some meaning, such as a status change (for example, item moved to cart) or a hierarchical context transition (for example, this view is a subview of the prior view), don’t remove the animation entirely. Instead, consider providing a new animation that avoids motion, or at least reduces full screen motion, such as a dissolve, highlight fade, or color shift. Also consider whether you want to replace your default animation, or only use the new one when the user’s setting indicates a need or preference for reduced motion.

Once your app no longer displays problematic motion triggers to users whose setting indicates a need or preference for reduced motion, you may indicate that it supports Reduced Motion.

Even after you’re able to indicate support for Reduced Motion in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Reduced Motion every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Captions, and Audio Descriptions.

Related Improving accessibility support in your visionOS app 
Human Interface Guideline > Designing for visionOS
Watch “Make your app visually accessible” Watch “Design considerations for vision and motion“ Responsive Design for Motion

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Sufficient Contrast evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Sufficient Contrast evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Sufficient Contrast helps users whose vision is reduced due to a disability or situational impairment such as bright sunlight. Users can increase or adjust the contrast between text or iconography and the background, improving readability.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Sufficient Contrast feature is to support low-vision users who may have reduced visual acuity, clarity, and/or contrast perception.

The following sections provide more detail about how to determine whether your app supports Sufficient Contrast well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Sufficient Contrast on the App Store.

### Getting started with testing

The accessibility settings for each device include a number of features that can help users customize contrast to fit their needs. Most users that have a need for higher contrast will enable the settings for Bold Text, Increase Contrast, and Reduce Transparency. You’re not required to use the built-in system settings, but testing with them on may give you an understanding of the contrast minimums your users expect. If you offer your own in-app setting, it should either support similar functionality to the systemwide settings, or offer more granular user interface customization.

Enable all three settings before testing your app for sufficient contrast. Review the resources below for details about turning on these settings for each device your app supports.

-  
For iPhone, visit Change display colors on iPhone to make it easier to see what’s onscreen.

-  
For iPad, visit Make text easier to read on iPad.

-  
For Mac, visit Make text and icons bigger on Mac and Change Display settings for accessibility on Mac.

-  
For Apple TV, visit Display bold text on Apple TV and Increase Apple TV screen contrast.

-  
For Apple Vision Pro, visit Text display settings on Apple Vision Pro and Adjust colors and contrast on Apple Vision Pro.

-  
For Apple Watch, visit Adjust text size and other visual settings on Apple Watch.

You can check the contrast of elements in your app by using Xcode’s Accessibility Inspector or other color contrast checkers to determine contrast ratios for elements in your app. Most modern accessibility guidelines recommend a minimum contrast ratio of “4.5 to 1 between foreground text and its background” based on a formula provided by the World Wide Web Consortium’s (W3C’s) Web Content Accessibility Guidelines.

If your app supports Dark Mode, be sure to check the minimum contrast in both light and dark modes. A common mistake is supporting sufficient contrast in your light mode interface, but forgetting to support sufficient contrast in a dark interface. Many developers use gray-on-black for dark mode reading, which can reduce eye strain for standard vision in low-light scenarios, but this reduced contrast variant may be more difficult to read for those with low vision or light sensitivity. Consider testing your app while combining the dark mode color scheme alongside the Increase Contras setting.

Consider not only contrast, but also translucency (opacity/blurring) of your background materials, controls, and content. Include legibility of text, icons, and other content, elements, and controls in your evaluation. Remember to test with Increase Contrast on and Reduce Transparency off, and with both settings on.

Make sure to provide sufficient contrast on interactive controls and non-text representations of a state, such as a selection. For example, if you design a custom checkbox, make sure there is sufficient contrast between the checked and unchecked states. Meeting a 3:1 minimum contrast ratio is commonly recommended for non-text contrast.

If you don’t have an existing proficiency in testing sufficient contrast, take some time to go beyond the basics. Review Strive to meet color contrast minimum standards in the Human Interface Guidelines to understand if the contrast of adjacent colors in your UI meets minimum acceptable levels.

A button with insufficient color contrast.  
A button with sufficient color contrast.   

The systemRed default color in iOS.  
The systemRed accessible color in iOS.    

## Indicating support for Sufficient Contrast

You may indicate your app supports Sufficient Contrast if the user interface for your common tasks, including text, buttons, and other controls, meets general contrast guidelines by default — usually 4.5 to 1 for most text elements.

If your app doesn't provide this minimum contrast by default: 

-  
If your app uses Apple-provided UI frameworks, verify that the Increase Contrast setting applies sufficient contrast.

-  
If your app supports custom frameworks, provide users with a choice of multiple color schemes that meet contrast minimums.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Even after you’re able to indicate support for Sufficient Contrast in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Sufficient Contrast every time you update the app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Reduced Motion, Captions, and Audio Descriptions.

Related Watch “Make your app visually accessible”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voice-control-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / Voice Control evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Voice Control evaluation criteria

iOS macOS visionOS  

## Description

Using Apple’s Voice Control feature, users with reduced mobility or dexterity can navigate an app’s interface using only their voice. When looking at the screen, they can use commands like “tap," "click," or "swipe" to interact with on-screen elements.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. If you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should strive to make it work with Voice Control, too. 

Note: Most of the work that goes into making your app accessible to VoiceOver users will also make it more accessible for Voice Control users. For this reason, we recommend you start with the  VoiceOver evaluation criteria before evaluating Voice Control.

The following sections provide more detail about how to determine whether your app supports Voice Control well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Voice Control on the App Store. 

### Getting started with testing

In order to accurately indicate support, proficient testing of your app using Voice Control is necessary on all platforms for your app. Even if you already have a basic proficiency in testing with Voice Control, take some time to go beyond the basics. 

Review the resources below to learn more about using Voice Control for each device your app supports. 

-  
For iPhone, watch “How to use Voice Control on iPhone, iPad, and iPod touch,” then visit Use Voice Control commands to interact with iPhone and  Use Voice Control on your iPhone, iPad, or iPod touch.

-  
For iPad, watch “How to use Voice Control on iPhone, iPad, and iPod touch,” then visit  Use Voice Control commands to interact with iPad and Use Voice Control on your iPhone, iPad, or iPod touch.

-  
For Mac, visit Get started with Voice Control on Mac.

-  
For Apple Vision Pro, visit the Use Voice Control to interact with Apple Vision Pro.

## Indicating support for Voice Control 

You may say your app supports Voice Control if users are able to navigate and interact with your app using only voice commands. Users should be able to complete all of the common tasks, actions, and functions of your app using only Voice Control, without touching the display.

Using only their voice, users should be able to activate all tappable or clickable elements on the screen.

-  
Speak “Show numbers” to make sure all buttons, links, and other interactive elements display a number. 

-  
Speak “Show names” to make sure all buttons, links, and other interactive elements display a label, also known as “alternative text.” Refer to the VoiceOver evaluation criteria for more tips on writing good default labels, and review how to  use accessibilityInputLabels(_:) for Voice Control.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

-  
Use commands like “tap” or “click” plus the name or number of a control to drive your app’s common workflows. For example, “Tap Compose,” “Click Back,” or “Tap 4.” 

-  
Match Voice Control labels to the visible text. If the Voice Control label is different from the visible text in your app (for example, “Leave call” instead of “End call”), users may be confused. Your users may be forced to speak “Show names” in order to understand why Voice Control isn’t working as they expected with your app.

Using only their voice, users should be able to operate all interactions in your app, including those that are more complex.

-  
If your app uses swipes, long presses, secondary clicks, or other ways to show additional interactive controls, make sure those are accessible to Voice Control users. For example, use a custom action. Elements with custom actions will be indicated with a double chevron; try speaking “Show actions for <number>.”

-  
If your app reveals a hidden user interface (for example, on hover or swipe), make sure that the user has a speech-only way to show the hidden elements or trigger the same behavior through an action or context menu.

-  
Ensure scrolling works in your app. For example, “Scroll down.” For panning views like maps or layout canvases, try out speech commands such as “Pan left” and “Zoom out.”

-  
If other multi-touch gestures are required, try speaking the gesture, such as “Swipe up with two fingers.”

-  
If your app has a recording option, or if you have a custom dictation function, ensure users can start and stop the recording using only their voice.

Using only their voice, users should be able to dictate and edit text in any text field.

-  
Make sure that users can dictate text in any text field in your app. Speak “type” and the text you’d like to type.

-  
Try speaking commands like “Select” and the text you want selected. Ensure the text is selected, then speak “Delete that” and verify the text is deleted. 

-  
If you use standard text fields from Apple frameworks, Voice Control will be automatically supported. However, if you use your own custom text entry or a third-party framework, extra work may be required. For example, Apple has an open-source accessibility plug-in for Unity-based apps.

-  
If your app uses any custom text fields, text entry behavior, or input validation, review and test the rest of Voice Control’s text commands very carefully.

### Additional suggestions

-  
Some users with physical or cognitive impairments may need more time, or wish to avoid distracting auto-play defaults. If aspects of your app auto-play or auto-hide on a time delay, consider allowing users to cancel or extend that delay. 

-  
Consider implementing SiriKit and App Intents to make your app better for all users, including Voice Control users. Review  “Bring your app to Siri” for more details.

Even after you’re able to indicate support for Voice Control in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app's support for Voice Control every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Learn How to Develop for Voice Control Watch “Writing Great Accessibility Labels“ Review how to use accessibilityInputLabels(_:) for Voice Control
Watch “Accessibility design for Mac Catalyst” Watch “Catch up on accessibility in SwiftUI” Watch Apple Support “Mobility Features“ playlist for iPhone & iPad

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voiceover-evaluation-criteria/
### App Store Connect Help

App Store Connect / Manage App Accessibility / VoiceOver evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# VoiceOver evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Using Apple’s VoiceOver screen reader, users can navigate an app’s interface without needing to see the screen. Many people who are blind or low vision use VoiceOver to understand and control apps.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. If you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should strive to make it work with VoiceOver, too. If you can see an important item on the screen, your app should use a label or description that a VoiceOver user would perceive in audible speech or braille.

Note: Most of the work that goes into making your app accessible to VoiceOver users will also make it more accessible for users of other assistive technologies like Voice Control, Switch Control, and Hover Text. For this reason, we recommend you start your accessibility evaluation with VoiceOver before moving on to test Voice Control.

The following sections provide more detail about how to determine whether your app supports VoiceOver well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports VoiceOver on the App Store.

### Getting started with testing

In order to accurately evaluate this label, proficient testing of your app using VoiceOver is necessary on all devices your app supports. To ensure your proficiency in testing with VoiceOver, take some time to review the resources below.

-  
For iPhone, watch "How to Navigate your iPhone or iPad with VoiceOver,” then visit Turn on and practice VoiceOver on iPhone, Use VoiceOver Gestures on iPhone, and Operate iPhone when VoiceOver is on.

-  
For iPad, watch  "How to Navigate your iPhone or iPad with VoiceOver,” then visit Turn on and practice VoiceOver on iPad, Use VoiceOver gestures on iPad, and Operate iPad when VoiceOver is on.

-  
For Mac, visit Learn and practice VoiceOver on Mac, then review other topics in the VoiceOver User Guide for macOS.

-  
For Apple TV, visit Use VoiceOver on Apple TV.

-  
For Apple Vision Pro, visit Turn on and practice VoiceOver on Apple Vision Pro, and Learn VoiceOver gestures on Apple Vision Pro.

-  
For Apple Watch, visit Use VoiceOver on Apple Watch.

Once you’ve learned the basics of VoiceOver, you’re ready to begin testing. However, to ensure the best VoiceOver experience for users, we recommend diving deeper into the user guides to learn about advanced functionality that experienced VoiceOver users may rely on.

## Indicating support for VoiceOver

You may indicate your app supports VoiceOver if users are able to navigate and interact with visual elements, including text, media, buttons, and controls, using only VoiceOver. Using gestures or keyboard commands, users should be able to focus on each part of the UI, hear what it is, and activate it. Make sure users can complete all of the common tasks of your app using only VoiceOver, without sighted assistance.

All controls should have concise, accurate labels.

Labels, also known as “alternative text,” help VoiceOver users to quickly understand the purpose of each control or interface element.

-  
Buttons, icons, form controls, and all other elements should contain a concise label providing a text equivalent for VoiceOver users. Interactive text fields and similar form controls should have a label (for example, “phone number”) in addition to the text value (“555-555-1212”) of the selection or contents.

-  
Labels should be concise, so that the interface isn’t tedious for a user to navigate and understand quickly. For example, a button for composing a new message should be labeled “New Message” rather than something more verbose like “Press to compose a new message.” 

-  
Ensure the labels make sense out of context. Because VoiceOver users may land on an element in different ways, avoid ambiguous labels that are unclear when the user encounters the item in a non-linear order, such as “Click here” or “Learn more.” If multiple action elements have the same label, like “Delete” in a Shopping Cart, the label text should make it clear what the action will do, especially in the case of destructive actions. For example, which cart item will be deleted?

-  
Ensure that labels don’t include control types like "checkbox" or states like "checked." Otherwise, VoiceOver may speak redundant information to the user, such as “Unsubscribe checkbox, checkbox.” Instead, implement these in your app as traits or through similar APIs appropriate to the device.

-  
Most images should include a relevant description or alternative text. If an image is purely decorative, make sure it’s ignored completely by VoiceOver.

-  
If your app provides a way for users to upload media, such as images, ensure users have a way to include labels or descriptions for the user-generated content, so that VoiceOver users can hear this description when encountering the media.

-  
Charts and other data visualizations should include accessibility information through a more specific chart API, or at minimum, include a reasonably complete text alternative.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

-  
For more ideas, watch “Writing Great Accessibility Labels“ and "Bring accessibility to charts in your app."

VoiceOver users should be aware of element type and control status or value.

People who rely on VoiceOver often need to hear more information than just labels and text content, since the status or value may be conveyed only through visual means such as a checked box. Implement this information in your app as traits or through similar APIs appropriate to the device.

-  
When a VoiceOver user lands on an item, VoiceOver should speak the type of element in addition to the label or text content. For example, “Unsubscribe from all emails, checkbox."

-  
Users should be able to understand control state and values. Keep in mind that default states, like the “unchecked” state of a checkbox, are implied so they may not be spoken by VoiceOver. For example, “Unsubscribe from all emails, checkbox.” Additionally, take care to update the API for control state and values. For example, once the user has checked the checkbox, VoiceOver will describe the control, including its new state, as, “Unsubscribe from all emails, checked checkbox."

VoiceOver should be able to speak all visible text in your app, and all text entry methods should be operable by VoiceOver users.

The accessibility of most visible text will be automatically supported when using Apple frameworks. However, if your app uses another framework, or custom text entry methods, extra work may be required. For example, Apple has an open-source accessibility plug-in for Unity-based apps.

-  
All visible text in the app should be accessible to assistive technologies, including VoiceOver. Plain text elements, such as paragraphs, don’t need a separate label, though you should ensure that VoiceOver can speak the text content.

-  
Custom keyboards and text entry methods (for example, custom keyboards or PIN code entry widgets) should be operable with VoiceOver, and produce correct speech/braille output for the user, in addition to providing accurate text entry and selection.

-  
Temporary status banners and important in-app alerts should be conveyed to VoiceOver users in a timely but non-disruptive manner, often done so with an AccessibilityNotification.

VoiceOver navigation and grouping should be consistent, complete, and use a logical order.

VoiceOver users should be able to navigate in page order, or move directly to a part of the screen using features like the VoiceOver rotors.

-  
VoiceOver users should be able to navigate to any visible element, either in order (swipe right, VO+Right, and so on) or by using a rotor and touch navigation on most platforms.

-  
VoiceOver users should be able to navigate away from the element they are on, whether by continuing forward, going backward (Swipe Left, VO+Left, etc), or by using a rotor or touch navigation on most platforms.

-  
If multiple elements or actions are presented as a group, VoiceOver users should be able to either move to each item in the group, or be able to interact with the grouped behaviors (for example, reply, forward, delete) through features like custom actions.

-  
VoiceOver users should be able to progress to each element without skipping items or looping back to the same item repeatedly. Try navigating forward through all contents, then backwards through all contents. Try looping through all rotor items forward and backwards, too.

-  
When content reloads or refreshes in the background, a VoiceOver user’s reading position shouldn’t reset unexpectedly. For example, if a VoiceOver user is near the bottom of a content feed when the app loads more content, the VoiceOver cursor shouldn’t accidentally reset to the top of the list.

-  
When the screen changes or a modal dialog appears, the VoiceOver cursor should move logically into the new content area. VoiceOver users shouldn’t be able to move into invisible, offscreen, or background content.

All interactive elements and controls should be discoverable, operable, and work consistently with VoiceOver.

As a reminder, if you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should make it work with VoiceOver, too.

-  
VoiceOver’s activation gesture (select then double-tap) and keyboard command (VO+space) should trigger the same behavior as a standard tap or click.

-  
Standard keyboard operations (for example, arrow keys) and keyboard modifier shortcuts should continue to work, even when VoiceOver is active, and the VoiceOver cursor should follow changes triggered by standard keyboard navigation like the Tab key, arrow keys, and more.

-  
If your app’s controls provide a context menu, overload a long press, or provide other non-default behaviors, consider providing the same behaviors as a custom action using VoiceOver’s actions rotor or its equivalent “show context menu” keyboard command (VO+Shift+M).

-  
VoiceOver should work with modal views, like dialogs. Apps should ensure that inactive content behind the modal view isn’t accessible to VoiceOver while the content is inactive. Apps should also support VoiceOver users being able to dismiss modal views, like closing the dialog, using the Escape key or an accessibilityPerformEscape action.

-  
Complex app behaviors, such as drag and drop or multi-touch gestures, should be provided in an accessible, discoverable way, such as through a custom rotor or action. Whenever possible, use the Apple-provided native API to reduce implementation complexity.

-  
Custom elements, if used by the app or any included frameworks, should provide equivalent accessibility of native elements provided by the Apple UIKit, AppKit, and SwiftUI frameworks. For example, custom buttons, tab bars, and sliders should be operable with VoiceOver and convey the same information as controls using standard API equivalents.

Even after you’re able to indicate support for VoiceOver in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app's support for VoiceOver every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Learn more about VoiceOver Support VoiceOver in your app 
Human Interface Guidelines > Accessibility
Watch "Tailor the VoiceOver experience in data-rich apps Watch "VoiceOver efficiency with custom rotors

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/add-an-app-icon/
### App Store Connect Help

App Store Connect / Manage app information / Add an app icon 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Add an app icon

An app icon serves as the representation of your app, and it appears on the Home Screen and in key locations throughout the system, including search results, notifications, system settings, share sheets, and TestFlight. For design guidance on app icons, visit Human Interface Guidelines > App icons.

You can create your app icon using Icon Composer or add your app icon to an asset catalog within your Xcode project. After adding icons in Xcode, upload the build to App Store Connect.

If you want to change your app icon after publishing, you must create and upload a new version of your app. Then, submit it for review.

Required role: Account Holder, Admin, App Manager, or Developer. View role permissions.

Related View and edit app information Get started with app discovery and marketing

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/complete-the-digital-goods-and-services-questionnaire/
### App Store Connect Help

App Store Connect / Manage app information / Complete the Digital Goods and Services questionnaire 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Complete the Digital Goods and Services questionnaire

The App Store empowers you to scale your app distribution worldwide using a variety of business models, including the sale of digital goods and services in your apps. Digital goods and services are content, features, subscriptions, and other digital experiences offered or consumed within an app. Complete the Digital Goods and Services questionnaire in App Store Connect to indicate how customers pay for or access digital goods and services in your app.

Completing this questionnaire helps ensure your app complies with the App Review Guidelines, Developer Program License Agreement, and helps you identify supported payment options for your customers.

Note: If this questionnaire doesn’t appear in App Store Connect for your app, no action is required.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Indicate payment options

Indicate how customers consume and access digital goods and services in your app across regions. Digital goods and services are content, features, subscriptions, and other digital experiences offered or consumed within an app.

-  
From Apps, select your app.

-  
In the sidebar under General, click App Information.

-  
Scroll to the Digital Goods and Services in Your Apps section, then click Get Started.

-  
Answer the questions:

-  
If you select No to “Can customers consume digital goods and services in this app?”, click Next.

-  
If you select Yes, confirm whether your app uses Apple In-App Purchase exclusively, or select the available payment options (such as alternative payment processing or out-of-app offers) for each country or region where you offer digital goods and services. Then click Next.

-  
Confirm and save:

-  
On the Confirmation page, take a moment to look over your answers and make any changes before submitting.

-  
Click Save.

To edit your answers later, click Edit under Digital Goods and Services in Your App.

Note: After you submit this form, your choices for the European Union remain locked for 12 months and can’t be changed. If you have questions, contact us.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/declare-regulated-medical-device-status/
### App Store Connect Help

App Store Connect / Manage app information / Declare regulated medical device status 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Declare regulated medical device status

To provide additional transparency on the App Store, apps that are available in the European Union (EU)/European Economic Area (EEA), United Kingdom (UK), or United States (US), and that also meet either of the criteria listed below must indicate whether they’re regulated medical device with respect to each region’s regulatory authority or body responsible for the governance and compliance of medical devices.

-  
Have a primary or secondary category of Health & Fitness or Medical

-  
Have indicated your app contains “frequent” in the Medical or Treatment Information field in the age rating questionnaire in App Store Connect

Regulated medical device apps are used for a range of medical purposes, including diagnosis, prevention, monitoring, and treatment of diseases and physiological conditions. They may function on their own or by interfacing with medical device hardware. These apps may require registration or authorization from regulatory bodies such as the U.S. Food and Drug Administration (FDA). Learn more about regulated medical devices in the EU/EEA, in the UK, and in the US.

If your app doesn’t provide any health or medical features, or access health data to support non-health features, you should select No, to declare that your app is not a regulated medical device.

If your app is a regulated medical device, you'll need to provide the following information. In some instances this'll require obtaining authorization or completing registration from the region’s regulatory authority. This information will display to customers on your App Store product page.

-  
EU Manufacturer SRN or FDA Owner/Operator Number: This should align with your EUDAMED listing and/or FDA establishment registrations. This isn't required for the UK.

-  
Instructions for use URL: The URL containing the user guide or instructions for use for your app, hosted on your website.

-  
Use statement: For the US, this is your indications for use statement. For the EU/EEA and UK, this is your intended purpose or intended use statement.

-  
Safety information: Provide relevant warnings, precautions, and contraindications as they appear in your labeling. For the US, this is also where you can include a statement about how users can report a problem to the FDA such as "To report a problem or adverse event to the FDA, visit www.fda.gov/safety/report-problem-fda". 

## How to know if your app is a regulated medical device

-  
Your app was cleared or approved by the US FDA

-  
Your app is registered on the US FDA medical device database

-  
Your app was issued a CE mark by an EU-based notified body for compliance with the EU Medical Device Regulation (MDR) or Medical Device Directive (MDD)

-  
Your app was issued a UKCA mark by a UK-based approved body for compliance with the UK Medical Device Regulations

-  
You’ve self-certified your app under the EU Medical Device Regulation (MDR) or Medical Device Directive (MDD)

-  
You’ve self-certified your app under the UK Medical Device Regulations 

Required role: Account Holder or Admin. View role permissions.

### Declare regulated medical device

-  
In Apps, select the app you want to view.

-  
In the sidebar, under General, click App Information.

-  
Under App Store Regulations & Permits, click Declare Regulated Medical Device.

-  
Indicate if your app is a regulated medical device in any country or region.

-  
If you select No, click Save and you are done.

-  
If you select Yes, continue with step 5.

-  
Select which countries your app is a regulated medical device in and click Save.

-  
Complete the required information for each country or region where your app is considered a regulated medical device.

-  
Verify your contact information that will appear on the App Store. If this information is inaccurate, you’ll need to update it in the Business section of App Store Connect.

-  
Enter your EU Manufacturer SRN or FDA Owner/Operator Number for the US as applicable

-  
Provide the instructions for use URL, use statement, and safety information. If you wish to localize this information, you can add the required details in each localization from the dropdown menu.

-  
Once all the information has been completed and verified, click Save, and the information will go live on the App Store within 24 hours. If the app is not yet approved to be live, the information will go live once the app is approved and released to the store.

### Update your regulated medical device declaration

You can click Edit next to the Regulated Medical Devices section to change your declaration for your app or to add or remove countries and regions.

If you have declared that your app is a regulated medical device and need to update the information provided, you can click Edit next to the country or region that needs to be updated in order to make the necessary changes.

You can also manage your contact information by going directly to the Business section and selecting Regulated Medical Devices under the Compliance section.

Updated information will be reflected on the App Store within 24 hours of saving the changes.

### Regulated medical device statuses

Status

Definition

Yes

You've declared your app is a regulated medical device in this country or region and entered the required information.

No

You've indicated that your app is not a regulated medical device in this country or region.

Missing Info

You've indicated that your app is a regulated medical device in this country or region, but have not completed the required information.

Related App information Required, localizable, and editable properties

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags/
### App Store Connect Help

App Store Connect / Manage app information / Manage app tags 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Manage app tags

App tags are glanceable terms that help people understand more about your app or game’s essential qualities. In addition to appearing in App Store search results, app tags can now appear on your product page, further improving the discoverability of your apps and games on the App Store. From these placements, people can tap a specific tag - for example, Sleep - to view more apps and games related to that specific tag. Tags are based on the App Store metadata you provide in App Store Connect, artificial intelligence, and human curation. You can also manage which of your selected tags appear across the App Store in the app information section of App Store Connect.

App Tags allow you to:

-  
Increase discoverability: Tags appear as glanceable terms in search results and as clickable entities on Search Landing Page and Product Page.

-  
Connect with the right audience: Tags align your app with user intent, leading to improved relevance.

You can manage tags in App Store Connect to ensure they are relevant to your app’s functionality. Currently, tags are only supported and displayed to users across the App Store in the United States. 

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Edit App Tags

Tags are applied to your app by default, based on the metadata you provide in App Store Connect (en_US only). You can deselect the tags you don't want associated with your app. Deselecting all tags may affect your discoverability on the App Store.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Information, under General.

-  
Below App Store Tags, click Edit. 

- In the pop up window, review your selections. Make any desired changes, and click Save.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement/
### App Store Connect Help

App Store Connect / Manage app information / Provide a custom license agreement 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Provide a custom license agreement

Apple provides a standard end-user license agreement (EULA) that applies in all countries and regions. If you don’t provide a custom EULA, the standard EULA is applied to your app and the license agreement link isn’t shown on your App Store product page.

Learn how to manage your EULA with the App Store Connect API.

## Edit the license agreement

-  
In Apps, select the app you want to view.

-  
In the sidebar, under General, click App Information.

-  
On the left, in the General Information section, click Edit next to License Agreement.

-  
In the dialog that appears, select “Apply a custom EULA to all chosen countries or regions”.

-  
In the Custom License Agreement field, enter your custom EULA as a plain text document.

All HTML tags are stripped and escaped, and only line break characters are accepted.

Tip: To add localized text for your custom EULA, you’ll need to add the localized text for each language within the same text field.

-  
In the Countries or Regions section, select each country or region where you want to apply your custom EULA.

-  
Click Done.

-  
On the top right, click Save.

Related Instructions for Minimum Terms of Developer’s End-User License Agreement Licensed Application End User License Agreement View and edit app information Localize app information App information

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-a-custom-product-page/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit a custom product page 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit a custom product page

Custom product pages, and their associated metadata like deep links, must be reviewed before they’re visible to users on the App Store.

If you want to submit a custom product page and your app hasn’t been approved yet, include the custom product page in the same submission as your first iOS app version. If your app is already approved, you can choose to submit a custom product page with or without an iOS app version. You can also add other items to a submission.

Learn how to submit using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to submit for review.

-  
On the top right, click Add for Review and select whether to add the custom product page to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version. The custom product page status changes to Ready for Review.

You may choose to add other items to the submission.

Note: Users with the marketing role can’t add app versions to a submission.

-  
Click Submit for Review. The custom product page status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about item statuses.

You can’t modify a custom product page's screenshots, previews, promotional text, or keywords, while it's under review. Withdrawing the submission makes the page editable, so you can make changes and resubmit.

After an app submission is approved, users can access the custom product page URL.

Related Configure multiple product page versions

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-event/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit an In-App Event 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit an In-App Event

iOS  
Before publishing your In-App Event on the App Store, submit your event details and media for review, ensuring all required information is complete. If you want to submit an In-App Event and your app hasn’t been approved yet, include the In-App Event in the same submission as your first iOS app version. If your app is already approved, you can choose to submit an In-App Event with or without an iOS app version. You can also add other items to a submission.

You can publish up to 10 In-App Events on the App Store and Apple Games at a time. Additionally, you can have up to 15 approved In-App Events per app in App Store Connect at a time.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
On the top right, click Add for Review and select whether to add the In-App Event to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version. The In-App Event status changes to Ready for Review.

If you’re submitting the In-App Event for review with an app version, it will be reviewed together with that app version.

If you’re submitting the In-App Event for review without an app version, select a platform in the draft submission screen. The In-App Event will be reviewed together with the latest version of the selected platform.

You may choose to add other items to the submission.

Note: Users with the marketing role can’t add app versions to a submission.

-  
Click Submit for Review. The In-App Event status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about item statuses.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-assets-from-asset-library/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit assets from Asset Library 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit assets from Asset Library

If you want to submit an asset and your app doesn't have an approved version, include the asset in the same submission as your first app version. If your app is already approved, you can choose to submit an asset with or without an app version. You can also add other items to a submission.

-  
First app version: If your app doesn’t yet have an approved version, include your assets in the same submission as your first app version.

-  
Subsequent updates: After your app has an approved version, you can submit standalone assets directly from the Asset Library without creating a new app version.

-  
Assets assigned to other items: When you submit an app version, Custom Product Page, Product Page Optimization test, or In-App Event, any assets assigned to it are automatically included in that submission and reviewed together.

-  
Submission restrictions: An asset can’t be submitted on its own through the Asset Library if the item it is assigned to is already part of an active submission.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the Asset Library.

-  
Click Edit at the top right.

-  
Select the assets you want to submit for review.

You can also select the Add for Review link in the Status column.

-  
On the top right, click Add for Review, then select whether to add the asset to an existing draft submission or create a new submission.

If you submit an app version, Custom Product Page, Product Page Optimization test, or In-App Event, any assets assigned to it are reviewed as part of that submission. You can’t submit those assets separately in the Asset Library.

If you're submitting the asset for review without an app version, or your submission includes items associated with multiple platforms, select a platform in the draft submission screen. The asset, and any other items in your submission, are reviewed together with the latest version of the selected platform.

You can also add other items to the submission.

-  
In the Draft Submission pane, click Submit for Review.

Learn how to remove a submission from review.

=== SOURCE: https://developer.apple.com/help/app-store-connect/managing-alternative-distribution/submit-for-notarization/
### App Store Connect Help

App Store Connect / Managing alternative distribution / Submit for Notarization 
Filter ⌘K  
Filter ⌘K  

Managing alternative distribution  

# Submit for Notarization

If you’ve set up alternative distribution, you can choose to make your app version eligible only for alternative distribution by selecting to have it evaluated based on the Notarization Review Guidelines (a subset of the App Review Guidelines). Otherwise, App Review uses the App Review Guidelines to evaluate your app version to make it eligible for distribution on the App Store, alternative app marketplaces, and your website (in the EU) if approved. After you've added your app as eligible for distribution on a marketplace in App Store Connect or an alternative distribution domain using the App Store Connect API, follow these steps.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select your app.

-  
In the sidebar, click the app version you want to submit.

-  
Scroll down to the App Review Information section, click Edit under Review Type.

-  
Select “Notarization” and click Save.

Note: The Review Type selection applies to each version individually. If you want to publish a later version through the App Store instead, select App Store in this same step when you submit that version.

-  
On the top right, click “Add for Review”. The app status changes to “Ready for Review”. If you changed any app information, you need to click Continue in the dialog that appears.

-  
Click “Submit to App Review”. The app status changes to “Waiting for Review”. When the review process starts, the app status changes to “In Review”. Learn about the tasks you can do in these statuses.

The app version is accepted, an alternative distribution package automatically generates.

## Required, localizable, and editable properties for Notarization

The tables below show the app and version properties required to submit your app for Notarization. The tables also indicate the properties that you can localize and edit at any time without submitting a new version of your app.

Learn about the required, localizable, and editable properties for App Store distribution.

### App information

Property

Required

Localized

Editable

Name

Subtitle

Rating

Bundle ID

SKU

Content Rights

License Agreement

1       

Primary Language

Primary Category

Secondary Category

Availability in the Republic of Korea2

Availability in China mainland3

4       
1 Custom License Agreement text box can include localized text.

2 Required for developers who enroll as an organization and distribute apps on the App Store in South Korea.

3 Required for apps that meet certain criteria to be available on the App Store in China mainland. Learn about availability requirements.

4 Enter at any time, but submits for review with the next version submission.

#### Platform version information

Property

Required

Localized

Editable

Screenshots

App Preview

Promotional Text

Description

Keywords

Support URL

Marketing URL

Version Number

Copyright

Routing App Coverage File

App Review Information

Version Release settings

What’s New in this Version

Phased Release for Automatic Updates

Reset overview rating

##### App privacy

Property

Required

Localized

Editable

Privacy Policy URL

Privacy Choices URL

Data Types

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events/
### App Store Connect Help

App Store Connect / Offer In-App Events 
Filter ⌘K  
Filter ⌘K  

Offer In-App Events  

# Offer In-App Events

iOS  
You can publish up to 10 In-App Events on the App Store and Apple Games at a time. Additionally, you can have up to 15 approved In-App Events per app in App Store Connect at a time.

In-app events must be approved before they are visible to users. Learn how to submit an In-App Event.

Learn how to create a high-quality event.

Learn how to create In-App Event using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Create an In-App Events

-  
In the left sidebar, click In-App Events.

-  
Click Create In-App Event or click the add button (+).

-  
Enter a reference name. This name identifies your event in App Store Connect and is not visible on the App Store and Apple Games. Each name must be unique and can be up to 64 characters long.

-  
Click Create.

### Enter event information

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
Enter an event name to appear on the App Store and Apple Games. It can be up to 30 characters.

-  
Enter a short description to appear on your event card in places like the Today tab and Search on the App Store and Apple Games. It can be up to 50 characters.

-  
Enter a long description that will appear on your event details page when users tap your event card. It can be up to 120 characters.

-  
Upload media for your event card and event details page. Learn about the In-App Event media specifications.

Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.

-  
Choose a badge that best fits the type of event you’re offering to display above the title on the event card and event details page.

-  
Add localizations for your event by choosing the primary language to display the language pop-up menu. Learn about localizing app information.

### Select country or region availability

The Country or Region Availability setting controls where your event appears on the App Store and Apple Games. By default, your event is set to appear on all storefronts. However, its visibility is determined by your app’s availability in those regions. You can select the date and time your event first becomes discoverable to users, as well as the date and time the event starts and ends.

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
Scroll down to the Country or Region Availability section.

-  
Select start and end dates and times. You can choose any date in the future for the start date. The end date can be a maximum of 31 days from the start date. Events must be at least 15 minutes long.

Note: You can have up to 10 events with overlapping start dates and times, either approved or in draft status, at the same time.

-  
Select a publish start date and time. The publish date is when your event will become discoverable on the App Store and Apple Games and can be a maximum of 14 days in advance of the start date.

-  
On the top right, click Save.

### Customize event start dates and times

The Customize Dates and Times option allows you to select different start times in one or more countries or regions on the App Store and Apple Games. If you choose to start your event on different days in different locations, all of your event start dates must be within 48 hours of each other.

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
In the Country or Region Availability section, click Customize Dates and Times.

-  
Select the locations you want to edit, and click Next.

-  
Enter the start date and time. Use the Time Zone toggle on the top right to choose a timezone.

-  
Click Done.

-  
To customize more regions, click the add button (+) next to Customize Dates and Times.

-  
Select the locations you want to edit, and click Next.

-  
Enter the start date and time.

-  
Click Done.

### Add additional information

-  
Provide an event deep link. This link takes users who tap Open on the In-App Event card or details page to the event content within your app. This can be a universal link (recommended for security) or custom URL. Avoid using URL shorteners and other services that add unnecessary redirects. Test the deep link to make sure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it. Learn about configuring universal links.

-  
Select the general purpose of your event to help make sure your event reaches the most relevant users on the App Store and Apple Games.

-  
Select the priority for your event. Events appear chronologically on the product page based on start time, with the soonest start time displaying first. If you designate an event as High Priority, it will appear ahead of Normal Priority events.

-  
Indicate if an In-App Purchase is required to participate in the event, as this information is shown on your event details page. For subscription apps, you only need to indicate that an In-App Purchase is required when there’s an additional cost for the event specifically — for example, a pay-per-view event in a subscription app that requires an In-App Purchase in addition to the standard subscription.

-  
Choose your event’s primary language. This will be the default language that displays to users if your event isn’t localized for their device’s language.

Related In-App Event badges In-App Event media and audio specifications Submit an In-App Event

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events/
### App Store Connect Help

App Store Connect / Offer In-App Events / Overview of In-App Events 
Filter ⌘K  
Filter ⌘K  

Offer In-App Events  

# Overview of In-App Events

iOS  
In-App Events, such as game competitions, movie premieres, and live-streamed experiences, are timely events within apps and games. Customers can discover these events on the App Store and Apple Games for iOS and iPadOS, providing a new way to showcase and expand their reach.

On iOS 15 and iPadOS 15 and later, In-App Events appear across the App Store as event cards that include images or video, the event name, and a short description. Customers can tap to open an event details page, which provides a more immersive experience with a longer event description. It also includes information about any required In-App Purchases or subscriptions. Customers can opt in on the event card and event details page to receive a notification from the App Store when your event starts.

Customers who don’t have your app or game can download it directly from your In-App Event card or event details page from the App Store. Once downloaded, they can tap Open to be seamlessly directed to the relevant section within your app or game.

In-App Events appear:

-  
On your App Store and Apple Games product page, which displays all of your currently published events.

-  
In App Store and Apple Games search results. When users search for an app, the event card appears along with your app for users who have downloaded your app, while screenshots show for those who haven’t downloaded your app. Users can also search for In-App Events directly. When users search for an event, the event card appears along with your app.

-  
In editorially curated selections and personalized recommendations on the Today, Games, and Apps tabs in the App Store and Apple Games.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

Related In-App Events Get started with app discovery and marketing Submit an In-App Event

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-promo-codes/request-and-manage-promo-codes/
### App Store Connect Help

App Store Connect / Offer promo codes / Request and manage promo codes 
Filter ⌘K  
Filter ⌘K  

Offer promo codes  

# Request and manage promo codes

Promo codes offer potential App Store customers or reviewers a free copy of apps on iOS, macOS, or tvOS. These codes can be redeemed on any App Store storefront where your app is available. Each code remains valid for four weeks from its generation date and can be used only once.

You can distribute promo codes by any means. Purchases made using promo codes are indicated in your Sales and Trends reports.

Note: Promo codes can't be generated for apps available only on Apple Business or Apple School Manager. If your app has been removed from sale on all App Store storefronts, promo codes can't be generated or redeemed — even if a version has a Ready for Distribution or Pending Developer Release status.

When a customer downloads an app using a promo code, the app functions as if it were purchased. For example, the customer has the opportunity to update to new versions of the app. However, customers can’t rate or review the app. Promo codes can be used to redeem unreleased versions of apps available on the App Store. Promo codes for tvOS or multi-platform apps must be redeemed on an iOS device. After the code is redeemed, the tvOS app appears in the customer’s purchase history on the App Store for Apple TV. You can request up to 100 promo codes per version of each platform your app supports.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Request promo codes

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Promo Codes. The Promo Code page opens with Generate selected.

-  
Under App Promo Codes, enter the number of version promo codes you want to generate.

-  
On the top right, click Generate Code.

-  
Read and agree to the contract terms for Apple to distribute free versions of your app, and click Generate Code.

-  
Click OK. You can view or download the generated promo codes on the History tab.

### View history of promo codes

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Promo Codes. The Promo Code page opens with Generate selected.

-  
Click History tab.

The history table shows the date each set of codes was generated in App Store Connect. Use this date to determine the expiration date of your codes.

-  
Click View Codes to view or download generated promo codes.

You can copy the codes in the dialog, or click “text file“ to download a .txt file containing the codes.

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-asset-statuses/
### App Store Connect Help

App Store Connect / Reference / App information / App Store asset statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# App Store asset statuses

When an asset — such as an app preview, screenshot, or creative asset — is added to the Asset Library, it moves through the following statuses:

Status

What it means

Uploading

The asset is being added to the Asset Library.

Processing

Your uploaded asset is being processed and validated. You can’t take action on the asset until processing completes.

Prepare for Submission

You’ve uploaded an asset to App Store Connect, but haven’t submitted it to App Review. While in this state, the asset is available to browse and select when configuring app versions, Custom Product Pages, Product Page Optimization tests, or In-App Events. You can also delete the asset.

Ready for Review

The asset has been added to a submission, but it hasn't been submitted to App Review yet.

Waiting for Review

Apple received your submission, but hasn't started review.

In Review

App Review is reviewing your submission. You can cancel the submission to remove it from review.

Accepted

This asset has been accepted, but there are one or more rejected items in the submission. All items in the submission must be accepted before any can be published. You can edit the rejected items and resubmit, or you can remove the item from the submission.

Approved

Apple has approved your asset. 

Rejected

App Review didn't accept your asset. You can edit the item and resubmit, or you can remove the item from the submission.

Archived

The asset belonged to a previous app version and has been replaced by a newer one. Archived assets don't appear in the Asset Library by default; use filters to view them.

Related Manage your App Store assets

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications/
### App Store Connect Help

App Store Connect / Reference / App information / Creative assets specifications 
Filter ⌘K  
Filter ⌘K  

Reference  

# Creative assets specifications

Creative assets include product page header, search results, and in-app event cards.

Learn more about App Store asset best practices and resources.
Learn how to manage creative assets in App Store Connect.

## Image specifications for product page header and search results

Note: Images can’t include alpha channels or transparencies.

Placement

Aspect ratio

Resolution

Supported extensions

Product page header

21:9

3840 x 1646 pixels

.jpeg, .jpg, or .png

16:9

5244 x 2950 pixels

.png

Search results

3:2

Min: 1920 x 1280 pixels

Max: 3840 x 2560 pixels

.jpeg, .jpg, or .png

16:9

5244 x 2950 pixels

.png

## Video specifications for product page header and search results

Note: Videos are muted by default in search results and can't currently be unmuted. On your product page, videos are also muted by default, but people can unmute them. Videos loop continuously in both placements.

Placement

Aspect ratio

Resolution

Frames per second

Minimum length

Maximum length

Supported extensions

Product page header

21:9

3840 x 1646 pixels

30 fps or 60 fps

5 seconds

30 seconds

.mov, .m4v, or .mp4

Search results

3:2

Min: 1920 x 1280 pixels

Max: 3840 x 2560 pixels

30 fps or 60 fps

5 seconds

30 seconds

.mov, .m4v, or .mp4

## Image specifications for In-App Event cards

Note: Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation. Learn more about In-App Event media and audio specifications.

Placement

Aspect ratio

Resolution

Maximum file size

Supported extensions

In-App Event card

16:9

Min: 1920 x 1080 pixels

Max: 3840 x 2160 pixels

500 MB

.jpeg, .jpg, or .png

In-App Event details page

9:16

Min: 1080 x 1920 pixels

Max: 2160 x 3840 pixels

500 MB

.jpeg, .jpg, or .png

## Video specifications for In-App Event media

Notes: 

-  
Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation. Learn more about In-App Event media and audio specifications.

-  
Videos are muted by default in search results and can't currently be unmuted. On your product page, videos are also muted by default, but people can unmute them. Videos loop continuously in both placements.

Placement

Aspect ratio

Resolution

Frames per second

Minimum length

Maximum length

Supported extensions

In-App Event card

16:9

Min: 1920 x 1080 pixels

Max: 3840 x 2160 pixels

30 fps or 60 fps

15 seconds

30 seconds

.mov, .m4v, or .mp4

In-App Event details page

9:16

Min: 1080 x 1920 pixels

Max: 2160 x 3840 pixels

30 fps or 60 fps

15 seconds

30 seconds

.mov, .m4v, or .mp4

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/in-app-events/in-app-event-media-and-audio-specifications/
### App Store Connect Help

App Store Connect / Reference / In-App Events / In-App Event media and audio specifications 
Filter ⌘K  
Filter ⌘K  

Reference  

# In-App Event media and audio specifications

## In-App Event media specifications

Note: Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation.

Media Type

Supported Extensions

Aspect Ratio

Min Resolution/Frame Rate

Max Resolution/Frame Rate

Max File Size

Event Card Image

.jpg, .jpeg, .png

16 : 9

1920x1080 px

3840x2160 px

500MB

Event Card Video

.mov, .m4v, .mp4

16 : 9

1920x1080 px 

30 fps or 60 fps

3840x2160 px 

30 fps or 60 fps

500MB

Event Details Page Image

.jpg, .jpeg, .png

9 : 16

1080x1920 px

2160x3840 px

500MB

Event Details Page Video

.mov, .m4v, .mp4

9 : 16

1080x1920 px 

30 fps or 60 fps

2160x3840 px 

30 fps or 60 fps

500MB

### Audio specifications

Audio specifications

Event Card Video:

-  
Stereo

-  
Codec: 256kbps AAC

-  
Sample Rate: 44.1kHz or 48kHz

-  
Tracks without audio are supported

Event Details Page Video:

-  
Stereo

-  
Codec: PCM or 256kbps AAC

-  
Bit Depth (for PCM): 16-, 24-, or 32-bit

-  
Sample Rate: 44.1 or 48kHz

-  
Tracks without audio are supported

Stereo configuration:

-  
1 track with 2-channel stereo (1st channel L and 2nd channel R)

-  
2 tracks with 1-channel stereo (1st track L and 2nd track R)

Stereo configuration:

-  
1 track with 2-channel stereo (1st channel L and 2nd channel R)

-  
2 tracks with 1-channel stereo (1st track L and 2nd track R)

Related Overview of In-App Events In-App Events

=== SOURCE: https://developer.apple.com/app-store/in-app-events/
Watch the latest video: Get started with In-App Events

# In-App Events

In‑App Events are timely events within apps and games — such as game competitions, movie premieres, livestreamed experiences, and more. People can discover your In‑App Events right on the App Store in iOS and iPadOS, so you can showcase your events and reach new, current, and previous users.

## Discovery on the App Store

In-App Events appear across the App Store as event cards that include images or video, the event name, and a short description (on iOS 15 and iPadOS 15, or later). People can tap to open an event details page, which provides a more immersive experience with a longer event description and notes if an Apple In-App Purchase or subscription is required to participate. From this page, they can share your event with others — for example, via Messages or social media. And they can opt in on the event card and event details page to receive a notification from the App Store when your event starts.

If someone doesn’t have your app or game, they can download it directly from your In-App Event card or event details page. Once downloaded, they can tap Open to be seamlessly directed to the appropriate area within your app or game.

Event Card on Product Page

Event Details Page

In-App Events appear:

- On your product page, which displays all of your currently published events.

- In search results. When users search for an app, the event card appears along with your app for users who have downloaded your app, while screenshots show for those who haven’t downloaded your app. Users can also search for In‑App Events directly. When users search for an event, the event card appears along with your app.

- In editorially curated selections and personalized recommendations on the Today, Games, and Apps tabs.

### Marketing your events

You can promote your In‑App Events using email, advertising, social media, and more to create additional awareness and engagement. Be sure to include a link to your event’s details page so people can learn more and download your app or game if they haven’t already.

You can also share your In-App Event with our worldwide team of editors for promotional consideration on the App Store. We highlight new apps and games, as well as those with significant updates, In‑App Events or exclusives, cultural or seasonal moments, and more.

Learn about getting featured on the App Store

Search

Recommendations

Editorial

## Configuring in App Store Connect

In-App Events are easy to set up and manage in App Store Connect. When creating an event, you’ll enter a reference name (visible only in App Store Connect) and event information, including metadata. You’ll also select an event badge and regional availability. You can submit events for review independent of a new app version and have up to 15 approved events in App Store Connect at a time. You can also use the App Store Connect API to automate metadata upload and submission for your events. An app can have up to 10 events published on the App Store at a time.

Good candidates for In‑App Events are challenges, competitions, or special content launches.

The following are not good candidates for In‑App Events:

- Repetitive activities such as daily tasks or rewards.

- Price promotions that don’t introduce any new content, features, or goods.

- General promotions that raise awareness about your app or game. While an In-App Event can highlight added content or features that are permanent or ongoing, the event itself should focus on a related limited-time moment or experience.

### Choosing an event badge

Select the badge that best fits the type of event you’re offering to display above the title on the In-App Event card and event details page.

- Challenge: Activities encouraging the user to achieve a goal before the event ends — for example, a fitness challenge in a workout app or beating a certain number of levels in a game.

- Competition: Activities in which users compete against one another for the highest ranking or to win rewards — for example, a tournament where players battle to win the most matches.

- Live Event: Activities that occur in real-time that all users can experience simultaneously — for example, a sports match or livestreamed concert. These events should provide users with new content, features, or goods.

- Major Update: Introducing significant new features, content, or experiences – for example, the launch of new game modes or levels. These events go beyond minor enhancements like UI adjustments or bug fixes.

- New Season: Introducing new content, storylines, or media libraries to build on established content. For example, a significant sporting event, a battle pass or themed content in a game, or a special episode of a television show. These events should focus on unique content rather than promoting awareness about the entirety of the season.

- Premiere: Introducing new content or media for the first time — for example, a movie debut or newly released audio. These events should focus on the introduction of this unique content, rather than promoting general awareness about your app’s content or service.

- Special Event: Limited-time events that are not captured by another event badge, possibly spanning multiple activities or experiences — for example, an event featuring a collaboration. These events should provide users with new content, features, or goods.

### Creating effective metadata

The metadata you provide is used when displaying your event across the App Store. To ensure a smooth review experience, make sure it accurately portrays your event and is specific to the event experience, rather than sharing general information about your app or promoting its content or services. You’ll enter the following:

Event name: Choose a distinctive, unique name that’s up to 30 characters long and written in title case. This should be the actual name of the event, such as “June Leaderboard Climb,” rather than a call to action or tagline, such as “Watch the livestream.” Avoid generic terms or describing the type of event, since the event badge already displays this information.

Short description: Briefly summarize your In-App Event in up to 50 characters written in sentence case. This information displays on your event card.

Long description: Provide more information about your event — such as potential rewards — in up to 120 characters written in sentence case. This information displays on your event details page.

Event card and event details media: Add an image or video that represents your In-App Event across the App Store. Videos autoplay and repeat, so aim to create a seamless loop. In App Store Connect, you can preview what your provided media will look like in an event card and event details page to confirm that crucial aspects of your image or video will not be obscured.

To ensure your events display properly on the App Store and provide a high-quality user experience, consider these guidelines when creating your metadata:

- Use proper capitalization and punctuation. Avoid using all capitals and don’t use excessive punctuation marks, such as multiple exclamation points.

- Avoid claims that can’t be verified, such as “the best” or “#1,” as well as extra words, such as “game event.”

- Don’t include specific prices in your metadata, as pricing and currencies can vary across regions and can be changed independent of your event. Including specific pricing will lead to rejection by App Review.

- When possible, avoid using text or logos in your media, especially if they include your event name or app name.

- Consider using video in order to provide users with a more dynamic preview of your event.

- Don’t add borders or gradients to your media. Crops and gradients are automatically applied to your media in order to ensure consistency across the App Store.

- Aim to create visual continuity across your event card and event details page by using similar colors or illustration styles.

- Make sure your metadata includes content that you created or have a license to use.

#### Do
Event Card 

Use title case.  
Choose a name that accurately describes the event.  
Use sentence case and describe the event experience.   

Use title case.  
Choose a name that accurately describes the event.  
Use sentence case and describe the event experience.    

#### Don’t
Event Card 

Avoid using text or logos in your media.  

Don’t use a call to action as the name.

Avoid using all capitals.

Don’t use multiple punctuation points.

Don’t use the description to promote your app or services.   

Avoid using text or logos in your media.  

Don’t use a call to action as the name.

Avoid using all capitals.

Don’t use multiple punctuation points.

Don’t use the description to promote your app or services.    

### Adding event details

When configuring your event, you’ll also add additional event details that impact how your In-App Event displays on the App Store.

Determine event availability. When you select start and end dates and times for your In-App Event, you’ll also choose the date and time it appears on the App Store. An In-App Event can last up to 31 days and be promoted up to 14 days before its start date. If you’d like, you can make your event available only in specific regions and customize the dates and times for each location.

Provide an event deep link. This link takes users who tap Open on the In-App Event card or details page to the event content within your app. This can be a universal link (recommended for security) or custom URL. Avoid using URL shorteners and other services that add unnecessary redirects. Test the deep link to make sure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it. Learn about configuring universal links.

Be thoughtful about the most relevant destination to direct users. If your event is live, you can link directly to the event. If your event hasn’t started, you might direct users to a landing page that builds anticipation and reminds them when to return. If a user is new to your app, consider taking them through any necessary onboarding before directing them to the event. Always provide a way for users to return to your main app experience.

Indicate your event purpose. Offering In‑App Events in your app or game can encourage new users to try it, provide existing users with new ways to enjoy your app, and give former users reasons to return. Many In‑App Events are appropriate for all of these purposes, but you may create In‑App Events that are primarily intended for one of these reasons. Choose the option that best fits your event’s purpose:

- Appropriate for all users

- Attract new users: New users are people who have never downloaded your app

- Keep active users informed: Active users are people who downloaded your app and have opened it recently

- Bring back lapsed users: Lapsed users are people who downloaded your app but have not opened it recently

This selection is one of the factors that the App Store uses to offer personalized recommendations and doesn’t display on your event card or event details page. To help your event reach the people it’s intended for, the App Store incorporates app usage information. This data is processed on the device to minimize data collection and enhance user privacy. Regardless of the event purpose you choose, your published events are discoverable on the App Store by all customers.

Designate event priority. Events appear on your product page chronologically based on start time, with the soonest start time displaying first. Any events you select as high priority will appear ahead of normal priority events.

Select cost. Indicate if a specific Apple In-App Purchase is required to participate in the event, as this information is shown on your event details page. For subscription apps, you only need to indicate that an Apple In-App Purchase is required when there’s an additional cost for the event specifically — for example, a pay-per-view event in a subscription app that requires an Apple In-App Purchase in addition to the standard subscription.

### Image and video specifications

Media type Supported extensions Aspect ratio Min size/resolution Max size/resolution    
Event card image .jpg, .jpeg, .png 16:9 1920x1080 px 3840x2160 px  
Event card video .mov, m4v, .mp4 16:9 1920x1080 px 30 fps or 60 fps 3840x2160 px 30 fps or 60 fps  
Event detail page image .jpg, .jpeg, .png 9:16 1080x1920 px 2160x3840 px  
Event detail page video .mov, .m4v, .mp4 9:16 1080x1920 px 30 fps or 60 fps 2160x3840 px 30 fps or 60 fps         

## Measuring event performance

You can use App Analytics in App Store Connect to understand the performance of your published In‑App Events. You’ll be able to:

- Determine which events are best at acquiring app users by viewing downloads and filtering by a specific event.

- Learn where users discover your events by viewing acquisition sources.

- Understand how well your event page engages users by viewing engagement data, such as event impressions, event details page views, and app opens.

- Monitor interest in your event by understanding how many users chose to be notified when your event starts.

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions
### App Store Connect Help

App Store Connect / Create custom product pages / Configure multiple product page versions 
Filter ⌘K  
Filter ⌘K  

Create custom product pages  

# Configure multiple product page versions

Create up to 70 custom product pages per app on the App Store to highlight features or specific content. Each custom product page can include different screenshots, previews, promotional text, and keywords, and is localizable and shareable through a unique URL.

Custom product pages must be approved before they are visible to users. Learn how to submit a custom product page.

Custom product pages are available on the App Store on iOS 15 and iPadOS 15, or later. Custom product pages are only visible to people if they follow a custom product page link, or if you choose to make your custom product page visible in App Store search results by adding keywords. Otherwise, your app’s default product page displays to all customers on the App Store.

In App Analytics, view App Store metrics such as impressions, downloads, and conversion rate for each page. The metrics are available after a custom product page receives at least five first-time downloads. Learn more about data in App Analytics.

You can optionally add an app deep link to your custom product page. When users running a minimum of iOS 18 or iPadOS 18 click Open on your custom product page, the app deep link directs them to specific content in your app.

-  
An app deep link can be a universal link or custom URL. Use universal links for app deep links to provide users with a secure and integrated mobile experience. Learn about configuring universal links.

-  
Avoid using URL shorteners and other services that add unnecessary redirects.

-  
Test the deep link to ensure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it.

-  
Your app deep link must be approved before it'll function for users. Submit your custom product page for review after you add a deep link in App Store Connect.

Learn how to create and manage a custom product page using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Create a custom product page

You can create a custom product page if your app has the Ready for Distribution status in at least one country or region.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click Create Custom Product Page.

If there’s an existing custom product page, click add button (+).

-  
Enter a reference name to help you identify the page in App Analytics.

-  
Choose whether to start with a blank page or make changes to an existing App Store product page. If you choose to start from an existing page, you can choose a version that’s in the Ready for Distribution state or the Prepare for Submission state and it’ll copy the product page for your primary localization.

-  
Click Create. Your custom product page’s unique URL is automatically generated and displays on this page.

-  
Modify or add additional screenshots, app previews, promotional text, or keywords.

Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.

You can optionally add an app deep link to direct users running a minimum of iOS 18 or iPadOS 18 to specific content in your app.

### Enable keywords for a custom product page

You can assign keywords from your latest approved app version to a custom product page. This directs customers to your custom product page when they search those keywords, rather than your default product page. You can assign keywords in App Store Connect at any time, but the custom product page is searchable only after it’s approved and set to visible.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the custom product page you want to assign keywords to.

-  
In the Keywords section, select the keywords for this custom product page.

Repeat this as necessary for each localization.

-  
Click Publish.

Tip: To ensure the most relevant custom product page appears, select a unique set of keywords for each page.

After assigning keywords to your custom product page, you can disable them individually.

### Edit a custom product page

An approved custom product page can be edited and submitted for review without affecting its unique URL. Changes are published automatically upon approval by App Review.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to edit.

-  
Click Create New Version.

-  
Review the prompt and click Create again to proceed. This creates a new draft of your custom product page in the Ready to Submit state.

-  
Make your edits and click Add for Review.

The submission confirmation screen displays the app version that’ll be associated with the custom product page, and the items that’ll be reviewed. You may choose to add other items to the submission.

-  
Click Submit to App Review.

Once the edited page is approved, it will replace the current page on the App Store.

### Disable a custom product page

You can disable a custom product page at any time. If someone selects a URL for a disabled custom product page, they’re automatically redirected to your default product page.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to disable.

-  
Under the Product Page URL, click Disable Link.

For a disabled link, Enable Link will display instead.

-  
Click Disable.

### Delete a custom product page

You can delete a custom product page at any time. If someone selects a URL for a deleted custom product page, they’re automatically redirected to your default product page. This action is permanent.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to delete.

-  
Scroll to the bottom and click Delete This Product Page.

Related Custom product pages Create search results ad variations Watch "Get started with custom product pages" Watch "Make the most of custom product pages" Watch "Get started with app discovery and marketing"

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/configure-test-treatments
### App Store Connect Help

App Store Connect / Create product page optimization tests / Configure test treatments 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Configure test treatments

By default, test treatments are copies of your app’s original App Store product page. You can edit the app icon, screenshots, and previews of each treatment. If you choose not to edit one of these items, the metadata from your original product page will display for that item.

Before testing, ensure all metadata in your test treatments is approved. You can submit this metadata without submitting a new version of your app. However, any app icons you wish to use must be part of the app binary for the current App Store version, which should be built with Xcode 13 or later and support alternate icons in asset catalogs through an appropriate SDK.

If you’re simply changing the order of screenshots or previews that are already on the App Store, or only modifying the app icon, your metadata is already approved and you don’t need to resubmit.

Note: Product page optimization tests aren't available for custom product pages or for product pages on the App Store for Apple Watch or iMessage.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Product page optimization.

-  
The default treatment names are Treatment A, Treatment B, and Treatment C. Treatment names are only visible to you in App Store Connect and help you identify treatments in App Analytics. Next to the treatment name you want to edit, click Edit Name.

-  
Enter a treatment name, then click OK.

-  
Click the App Icon tab, which displays if your app binary includes more than one icon. Ensure any icons you want to use are part of the app binary currently on the App Store. This app version must be built with an SDK that supports alternate icons in asset catalogs. Icons must also be sized to 1024x1024 pixels.

-  
Click Change under under the icon of the treatment you want to change.

-  
Choose an icon from the menu that appears. This menu shows all app icons included in your app’s binary. If an app is downloaded from a product page with a test treatment, the test treatment app icon displays throughout the download process and on the user’s device.

-  
Select Header and Search Results or App Previews and Screenshots tab to upload your assets. If you choose not to edit screenshots or previews for a certain device size, the treatment will use the ones on your original product page for that device size. For details on specifications, visit Screenshot specifications and App preview specifications.

Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/create-a-test
### App Store Connect Help

App Store Connect / Create product page optimization tests / Create a test 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Create a test

Configure product page optimization tests in App Store Connect if your app has a Pre-Order Ready for Distribution or Ready for Distribution status and is live on the App Store. Learn how to design tests.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In the sidebar, click Product Page Optimization.

-  
If you haven’t created a test before, click Create Test. If you've previously created a test, click the add button (+) next to Product Page Optimization.

-  
Enter a reference name to help you identify the test when monitoring results in App Analytics.

-  
Choose the number of treatments you want to create. You can have up to three treatments per test. Please note that the more treatments you add to a test, the longer the test may take to reach a conclusive result.

-  
Choose a traffic proportion. This is the percentage of users that’ll be randomly shown a test treatment instead of your original product page. For example, if a test has three treatments and you choose a 30% traffic proportion, each treatment will be shown to 10% of the total traffic.

-  
Select the localizations you want to include in your test. By default, all localizations that your app supports are selected. If the localization shown to a user is excluded from your test, the user won’t be included in the test.

-  
To view how long it might take to reach your goal, click the arrow next to Estimate Your Test Duration and choose your desired improvement in conversion rate. We use your app’s existing performance data, such as daily impressions and new downloads, to generate this estimate. The estimated duration and impressions needed will appear. This estimate is provided as a guide and won’t impact the test. A test runs for 90 days or until you manually stop it within that time. Keep in mind that it may not be possible to reach your desired improvement in conversion rate within 90 days.

-  
Click Create Test.

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/overview-of-product-page-optimization
### App Store Connect Help

App Store Connect / Create product page optimization tests / Overview of product page optimization 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Overview of product page optimization

Optimize your iOS or iPadOS app's product page on the App Store by testing up to three different app icons, screenshots, and previews to see which resonate best with customers. Each variant will be randomly shown to a user group you define, and can be localized in any language your app supports. Use App Analytics to evaluate performance and feature the top-performing assets to all users.

The methodology for determining the treatment that’s best at driving app engagement is based on the estimated lift in conversion rate, as well as algorithms that provide confidence in the reliability of the test results. Learn how to view product page optimization results.

Note: Your app must be in the Ready for Distribution state to test its product page. Releasing a new app version while a test is in progress may impact the results if your version contains assets or metadata that are currently being tested. Product page optimization tests aren't available for custom product pages or for product pages on the App Store for Apple Watch or iMessage.

Treatments are shown to users on the App Store on iOS 15 and iPadOS 15, or later.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

Related Creating your product page Get ready to optimize your App Store product page View product page optimization results Product page optimization metrics Make the most of product page optimization Get started with app discovery and marketing

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/run-a-test
### App Store Connect Help

App Store Connect / Create product page optimization tests / Run a test 
Filter ⌘K  
Filter ⌘K  

Create product page optimization tests  

# Run a test

Before starting a test, ensure all metadata is approved by App Review for distribution on the App Store. If approval is pending, the metadata will be included in a new submission for review. Learn more about submitting for review.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Start a test

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Product Page Optimization.

-  
Click the name of the test you want to start.

-  
On the top right, click Start Test. The test status automatically updates to Running and shows how long the test has been live.

If your metadata needs to be reviewed, you’ll be prompted to add the test for review. Click Add for Review, then select whether to add the test to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version.

In the submission window, click Submit for Review. The test status will change once the metadata is accepted by App Review.

-  
Your test will run for 90 days or until you manually stop it within that time. Test results appear in App Analytics after there are five first-time downloads associated with the test. Learn how to view product page optimization results.

### Manually stop a test

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Product Page Optimization.

-  
Click the name of the test you want to stop.

-  
On the top right, click Stop Test. Once you stop a test, it can't be restarted. You’ll need to create a new test with the same treatments and run it again.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/audio-descriptions-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Audio Descriptions evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Audio Descriptions evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Audio descriptions are additional dialogue, interspersed between natural pauses in the main audio of a program or interstitial content, that describe to viewers who are blind or low vision what’s happening on-screen during time-based visual content.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Audio Descriptions feature is to support users who are blind or have low vision. Predominantly used in movies and TV shows, audio descriptions (AD) combine the main audio track with additional narration describing inaudible on-screen events. For example, “Mark stares at Gemma through the window. His expression displays inner conflict, as he wonders what to do next.”

When an AD audio track is selected, narration describes for the scene above from Severance as: “In slow motion, Mark and Helly run together down a long white hallway flashing with red light.”

The following sections provide more detail about how to determine whether your app supports Audio Descriptions well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Audio Descriptions on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Audio Descriptions, your app should still enable audio descriptions by default when detecting the systemwide audio descriptions setting. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Review the resources below to learn how to enable audio descriptions for each device your app supports.

-  
For iPhone, visit Hear audio descriptions for video content on iPhone.

-  
For iPad, visit Hear audio descriptions for video content on iPad.

-  
For Mac, visit Change Audio Descriptions settings for accessibility on Mac.

-  
For Apple TV, visit Use audio descriptions on Apple TV.

-  
For Apple Vision Pro, visit Hear audio descriptions for video content on Apple Vision Pro.

## Indicating support for Audio Descriptions

You may say that your app supports Audio Descriptions if it provides narrated descriptions of relevant on-screen content for video played in your app, including game interstitials and audible dialogue. 

-  
Even if your app doesn’t include movies or TV shows, there may be other areas where your app presents on-screen time-based content that may not be available through another form of sensory perception. For example, opening sequences, game interstitials, and cut scenes should be described, even if they’re not delivered in a standard video player. You should also describe tips and hints that are otherwise only available through visual clues.

-  
As one uncommon but creative example, a video streaming service might choose to provide an audio-only watchOS app, and automatically select the audio description track.

Audio Descriptions in third-party content

If your app presents third-party content, such as video posts in a social media app, videos added by the user in a presentation app, or TV or movie streaming in an entertainment app, users should have the ability to include an audio description track for your app to present. To indicate support for Audio Descriptions, you’re not responsible for ensuring every piece of third-party media has audio descriptions. However, you should ensure the following:

-  
Users should be able to determine which pieces of media content are audio described. For example, most video streaming service apps will present an “AD” icon on videos that include audio descriptions. 

-  
If your app includes the functionality to select audio descriptions, but very little or no described content is available on your app, don’t indicate support for Audio Descriptions.

-  
Consider evangelizing audio descriptions to your content providers so more video content has audio descriptions.

## Additional suggestions

-  
Creating great audio description content is a creative process that many movie and TV production teams have started to author and record in-house. Others contract this work to external service firms that specialize in audio description, captioning, and other types of accessible media.

-  
If you or your content partners will be developing the audio descriptions yourself, try watching one of your favorite movies or shows with audio descriptions enabled. Pay attention to the details, like the tone of voice, and terseness that is necessary in some scenes. Pay attention to the detail provided in scenarios like end credits. Apple TV+ provides audio description content in multiple languages, and most other major streaming services provide audio description content as well.

Even after you’re able to indicate support for Audio Descriptions in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Audio Descriptions every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, and Captions.

Related Selecting Subtitles and Alternative Audio Tracks Media Accessibility

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/captions-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Captions evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Captions evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Captions are usually time-synchronized text alternatives for dialogue and relevant sounds in videos or some forms of audio-only content. Captions are an accommodation for the Deaf and hard of hearing communities, but captions are also used widely by those without hearing loss.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Captions feature is to support users whose system settings express a need or desire to have audible dialogue and other sounds visibly rendered on screen, or to an alternate output device like a tactile braille display. Captions are a critical accommodation for the Deaf, DeafBlind, and hard of hearing communities, but captions are also used widely by those without hearing loss.

The following sections provide more detail about how to determine whether your app supports Captions well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Captions on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Captions, your app should still enable captions by default when detecting the systemwide captions setting. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Review the resources below to learn how to turn on systemwide captions for each device your app supports.

-  
For iPhone, visit Display subtitles and captions on iPhone.

-  
For iPad, visit Display subtitles and captions on iPad.

-  
For Mac, visit Use subtitles and closed captions on Mac.

-  
For Apple TV, visit Turn on closed captions and SDH.

-  
For Apple Vision Pro, visit Display subtitles and captions on Apple Vision Pro.

## Indicating support for Captions

You may say that your app supports Captions if it provides captions for video played through your app, including game interstitials and audible dialogue. You may also indicate support for Captions if your app provides text transcripts of audio-only content, such as music lyrics or spoken dialogue in podcasts.

-  
For video content, you may indicate support for Captions if your app has dialogue-only subtitles for primary and alternate languages, but consider improving your pipeline to offer closed captions or SDH, which also includes relevant non-verbal audio such as “[doorbell rings]” or “[dog barks].”

-  
Even if your app doesn’t include movies or TV shows with typical subtitles or closed captions, there may be other areas where your app presents spoken dialogue or other relevant sounds. Game interstitials, for example, often include dialogue that should be captioned, even though it’s not delivered with standard captions in a standard video player.

-  
If your app provides verbal audio content, such as music with lyrics or spoken podcasts, consider providing a text copy of that content as a transcript. Text transcripts don’t need to be time-synchronized, and you may indicate support for Captions based on the inclusion of high quality transcripts. For example, even though watchOS apps don’t support video playback, a watchOS app could include music lyrics or a transcript for spoken audio.

Captions in third-party content

If your app presents third-party video content, such as video posts in a social media app, videos added by the user in a presentation app, or TV or movie streaming in an entertainment app, users should have the ability to include caption data for your app to present. To indicate support for Captions, you’re not responsible for ensuring every piece of third-party media has captions. However, you should ensure the following:

-  
Users should be able to determine which pieces of media content are captioned. For example, most video streaming service apps will present a “CC” or “SDH” icon on videos that include captions, along with other details about available subtitle languages.

-  
If your app includes the functionality to display captions, but very little or no captioned content is available on your app, don’t indicate support for Captions.

-  
Consider evangelizing captions to your content providers so more video content has captions.

Even after you’re able to indicate support for Captions in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Captions every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, and Audio Descriptions.

Related Selecting Subtitles and Alternative Audio Tracks Caption Authoring Improving accessibility support in your visionOS app: Include captions for audio content  Media Accessibility

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/dark-interface-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Dark Interface evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Dark Interface evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Users with light sensitivity can maintain a dark user interface for the common tasks of the app to reduce eye pain or discomfort.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Dark Interface capability is to support users with light sensitivity for whom large white or bright areas on the screen may cause discomfort or even physical pain. Keep this in mind, because the goal isn't only to make the interface dark, but to keep it that way. Even temporary flashes of bright content may cause discomfort or a difficult user experience.

The following sections provide more detail about how to determine whether your app supports a Dark Interface well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Dark Interface on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Dark Interface, we recommend reviewing how Apple’s system apps respond to the systemwide setting to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

To ensure proficiency in testing with a dark interface, review the resources below to learn how to turn on Dark Mode for each device your app supports.

-  
For iPhone, visit Adjust the screen brightness and color on iPhone.

-  
For iPad, visit Adjust the screen brightness and color on iPad.

-  
For Mac, visit Use a light or dark appearance on your Mac.

-  
For Apple Vision Pro, visit Change the appearance of text, app windows, and more on Apple Vision Pro.

A common mistake is supporting sufficient contrast in your light mode interface, but forgetting to support sufficient contrast in a dark interface. Many developers use gray-on-black for dark mode reading, which can reduce eye strain for standard vision in low-light scenarios, but this reduced contrast variant may be more difficult to read for those with low vision or light sensitivity. Consider testing your app while combining the dark mode color scheme alongside the Increase Contrast accessibility setting.

## Indicating support for Dark Interface

You may indicate support if your app is dark by default for all common tasks, excluding any third-party or user-generated content. For example, most apps on tvOS and watchOS are dark by default.

If your app isn’t dark by default for all common tasks, you may still indicate support if it allows the user to enable a mode or setting that keeps the interface dark. This can include supporting the systemwide Dark Mode appearance or using a custom dark color scheme, or as a last resort, supporting the systemwide Smart Invert accessibility setting.

-  
Be careful of unintended color changes that may cause user confusion. For example, if relying on the Smart Invert setting, a red “Delete” button may invert to green if you don’t account for the color inversion. Additionally, when Smart Invert is enabled, make sure the colors in the media don’t appear inverted.

-  
For translucent views, including Apple Vision Pro apps using passthrough, you may indicate support for Dark Interface if your app renders only dark UI. You’re not responsible for background light filtering through your app. However, consider whether your app should reduce the translucency if the system Increase Contrast or Reduce Transparency settings are enabled.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Even after you’re able to indicate support for Dark Interface in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Dark Interface every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related 
Human Interface Guidelines > Dark Mode
Supporting Dark Mode in your Interface Watch “Make your app visually accessible”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/differentiate-without-color-alone-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Differentiate Without Color Alone evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Differentiate Without Color Alone evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Users shouldn't have to rely on color to distinguish different selection states or values in an app. Instead, apps should use additional methods beyond color, such as text labels or icons, to convey information to users with common forms of color blindness.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal is to ensure that your app doesn’t exclude users who may not be able to perceive all colors. Color blindness is one of the most common forms of disability, affecting up to 10% of some populations.

Color is extremely useful in communicating information quickly. Don’t remove color from your app to support this capability; just make sure color isn’t the only way you’re conveying information.

The following sections provide more detail about how to determine whether your app supports Differentiate Without Color Alone well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Differentiate Without Color Alone on the App Store.

### Getting started with testing

A great way to evaluate your app is to try testing using the Grayscale color filter in Accessibility Display settings. While this's not a representation of what color-blind users see, it's a good way to discover unanticipated problems with the use of color in your app. If you can’t use your own app in grayscale, rethink your app’s design and differentiate without color alone.

Ideally, your app should be designed by default to convey information using more than color alone. Using a setting to invoke this experience should be a last resort or stop-gap solution until your app's reliance on color can be improved.

## Indicating support for Differentiate Without Color Alone

You may indicate your app supports Differentiate Without Color Alone if the common tasks of your app don't rely on color as the only way to convey information. For example, a game may distinguish teams using symbols, in addition to representing them with colors. If your app does use color as the only differentiator (e.g. color-coded charts), make sure that users can customize the design for their needs with a setting or by choosing multiple color schemes.

-  
Consider where your elements, controls, or content rely solely on color to differentiate or communicate key information. Examples include status buttons or icons whose only distinguishing difference is red 🔴 vs green 🟢 to indicate positive or negative, online or offline. This visual difference may not be easy for people with red-green color-blindness to perceive.

-  
Instead of relying on color alone, consider using placement, order, shape, iconography, or other stylistic differences in addition to color. Differences like a red square 🟥 or green circle 🟢 are perceivable by all sighted users, regardless of color perception ability.

-  
Consider allowing multiple color schemes so users can avoid the problematic color combinations they have difficulty distinguishing. One example is in apps and games where color is used to indicate different teams or characters.

-  
In complex charts or data visualization apps, consider arranging the chart colors in the same order as the legend keys. Alternatively, you can provide options for in-chart iconography or labels on each element directly to help communicate the data.

Note: These differences reduce cognitive load and help users of all abilities remember what each color means.

For Someone with red-green color blindness, these indicators might appear the same.  
Both visual indicators and color help differentiate between indicators.   

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Even after you’re able to indicate support for Differentiate Without Color Alone in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Differentiate Without Color Alone every time you update the app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related 
Human Interface Guidelines > Vision > Convey information with more than color alone
Watch “Make your app visually accessible”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/larger-text-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Larger Text evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Larger Text evaluation criteria

iOS tvOS visionOS watchOS  

## Description

Users can adjust the size of text and icons to make them more legible, visible, and comfortable to read.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. Ensuring that extra large fonts work well in your app makes the interface more convenient and accessible to more people. While some low-vision or legally blind users may be able to manage default font sizes by using screen zoom or holding their device extremely close to see the text and small icons in your app, this isn't a good user experience.

The following sections provide more detail about how to determine whether your app supports Larger Text well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Larger Text on the App Store.

### Getting started with testing

Allow primary content such as body text to scale as large as possible, while retaining usability and informational hierarchy in your app. Many accessibility guidelines recommend allowing users to enlarge text to 200% or larger than the default size. Dynamic Type on iOS, for example, reaches sizes larger than 200% at the AX3 size, and allows body text sizes over 300% at the AX5 size. Testing your app at the largest sizes helps you catch issues such as truncated or overlapping text.

Be sure to design for and test small, medium, large, and extra large accessibility sizes.

While you’re not required to use Apple frameworks to indicate support for Larger Text, we recommend reviewing how Apple’s platform and apps respond to the systemwide settings to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Design and test your app at all text sizes, including extra large accessibility sizes.

-  
For iPhone, watch “How to adjust text size on iPhone or iPad” and visit Make text easier to read on iPhone.

-  
For iPad, watch “How to adjust text size on iPhone or iPad” and visit Make text easier to read on iPad.

-  
For Apple Vision Pro, visit Text display settings on Apple Vision Pro.

-  
For Apple Watch, visit Adjust text size and other visual settings on Apple Watch.

## Indicating support for Larger Text

You can indicate that your app supports Larger Text if users can enlarge text to at least 200% or the maximum font size for the system. Allow users to resize text and meaningful icons as large as possible. Body text in the primary iPhone, iPad, and Mac views should increase in size without affecting readability through overlapping layouts or severe truncation. If you have controls that can't reasonably increase in size, review the details below for other ways to make those perceivable, usable, and understandable.

Don’t rely on system-provided assistive technology like Zoom or Hover Text to claim support for Larger Text. These features are available to users regardless of your app’s implementation, so users will already be aware that they can enlarge most or all on-screen text to a sufficient size using Zoom or Hover Text.

The Larger Text label is useful to users of your app as a way to determine whether the user interface of your app supports font size enlargement separate from these built-in features like Zoom. You may indicate support for Larger Text, either by using an Apple-provided feature like Dynamic Type, or by using your own in-app font size control to achieve equivalent font sizes.

You’re not required to adopt Apple frameworks to indicate support for Larger Text, but we recommend detecting when a user has Apple system settings enabled so they don’t have to manually update another setting for the app to function as expected. If you offer your own in-app setting that has additional customization or granular controls, you may not need to use the Apple system setting.

If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Use the system font size, or manage your own.

Most iOS apps typically use Dynamic Type, but some developers of games or apps that rely heavily on the use of text may choose to manage their own font sizes with an in-app setting. For most apps, using system frameworks is easier and more reliable than implementing your own.

Apple Books is a good example of an app that supports larger text well, but doesn’t rely on Dynamic Type. While the Books app doesn’t leverage the system font size setting, it offers more granular controls. For example, users can change text to their preferred size, and the app’s layout changes from two columns to a single column at larger text sizes in landscape orientation, so that low-vision users can perceive more words in an uninterrupted line of text.

Safari on iOS is another great example of an app with a custom font size controller. Since not all web pages scale to larger text sizes well, Safari allows users to adjust the font size for each site they visit. If your app uses a web view as part of its common tasks, provide a font size controller or let Safari handle this task for your users.

Use responsive design principles to adjust layout and information hierarchy based on needed text size.

Consider which text to enlarge to reinforce a clear information hierarchy to low-vision users of your app, and prioritize scaling the main content areas before repeated, predictable navigational elements.

Consider the value of screen real estate when determining which elements to scale. For example, the Back and Edit buttons on iOS remain small in the example below because they are repeated, predictable, and secondary elements of the interface. Primary content and action buttons are enlarged, extending to full screen width and lengthening the page to use the available space.

Smaller side-by-side elements may overlap when enlarged, so consider wrapping them onto a new line or laying them out vertically rather than horizontally. In the example below, the layout of the message sender, receiver, and date changes from horizontal to vertical to support larger text sizes.

Keep in mind that some features, like Tab Bars, don’t grow with dynamic text to avoid overlapping valuable screen estate. Consider other ways to make those elements accessible, such as the Large Content Viewer.

Avoid overlapping text and excessive or unusable truncation.

Scaling text to much larger sizes may produce unpredictable results, especially on devices with smaller screens. As text is enlarged, consider how that changes the experience:

-  
Content may overlap making it difficult to read.

-  
Content designed for a single line might become truncated, showing only the first few characters. 

Follow these principles for a great experience: 

-  
Avoid overlapping text.

-  
Avoid truncating text to the point that it becomes unreadable or ambiguous for the user. Consider allowing the text to wrap to two or more lines instead of truncation.

-  
If text is truncated, ensure that users are still able to access the same information as if the text were smaller. For example, in a list view, you can truncate text to a single line or two as long as the full text is available in a different view so users can dive into the details. 

-  
Test your app's larger text layout with different languages. In addition to languages with a longer average word length, test right-to-left languages and those with larger ascenders, descenders, and diacritics that may by clipped by layout constraints.

## Larger Text on tvOS apps

Scale most text in your tvOS app to retain a relative information hierarchy. Section headings and media titles must remain larger than less important description text, even if the scaling isn't exactly proportional.

Rather than focusing on a particular percentage increase, scale the smallest text element as large as possible while retaining the overall usability, information hierarchy, and feel of your app. Watch Prepare your tvOS apps for Dynamic Type for tips on adopting Dynamic Type and design considerations for larger text sizes in tvOS.

You can indicate support for Larger Text in your tvOS app by supporting the largest Dynamic Type size or an equivalent font size using your own implementation.

## Larger Text on watchOS apps

Because Apple Watch has a smaller screen, the largest Dynamic Type size on watchOS is larger than 140% of the default size. You can indicate support for Larger Text on your watchOS app by implementing Dynamic Type or by supporting an equivalent or larger size for body text or other primary content.

You might also consider some of the techniques employed by the X-Large watch faces, where each complication can be set up as its own watch face, taking advantage of the full screen size. Low-vision users can still view multiple complications (including your app’s watch face complications) by swiping through each of their saved watch faces.

Even after you’re able to indicate support for Larger Text in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Larger Text every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Watch “Get started with Dynamic Type” Watch “Large Content Viewer - Ensuring Readability for Everyone” 
Human Interface Guidelines > Vision

Human Interface Guidelines > Typography
Scaling Fonts Automatically Applying custom fonts to text

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/manage-accessibility-nutrition-labels
### App Store Connect Help

App Store Connect / Manage App Accessibility / Manage Accessibility Nutrition Labels 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Manage Accessibility Nutrition Labels

Review the evaluation criteria for each label before you begin indicating support for the accessibility features.
Learn how to manage Accessibility Nutrition Labels with the App Store Connect API. 
Required role: Account Holder, Admin, Finance, App Manager, or Marketing. View role permissions.

## Indicate your app’s accessibility support

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Accessibility.

-  
On the right, click Get Started.

-  
We automatically detect the devices your app supports if your latest app version is live on the App Store, or if your app record only support one device, like Mac. If the latest version of your app is in an editable state, like Prepare for Submission, select the devices you want to add accessibility support for, then click Save.

-  
Click Add [Device] Support for the relevant device.

-  
Select Yes if your app supports any of the accessibility features on the selected device, or No if it doesn’t support any of the features, then click Next.

-  
Select the accessibility features that your app supports, then click Next. 

-  
Your responses will be saved as a draft. Click Publish to publish your responses to the App Store. 

You can only publish support for devices that have a live version on the App Store.

If you’ve indicated support for multiple devices, you’ll need to confirm the devices you want to publish support for. Select each applicable device, then click Publish again.

The responses will be published immediately but may require up to 24 hours to be visible to all users.

### Update your app’s accessibility support

You can update your app accessibility responses at any time. 

-  
In Apps, select the app you want to view.

-  
In the sidebar, select App Accessibility.

-  
On the right, click Edit next to the device you want to update your responses for.

-  
Make your desired changes, then click Save.

-  
Click Publish to publish your updated responses to the App Store.

The changes will take effect immediately but may require up to 24 hours to be visible to all users.

### Manage the accessibility URL

If you have other accessibility information you'd like to provide, you can optionally include a URL. This link will show on your app's product page across all devices, except Apple TV.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select App Accessibility.

-  
Below Accessibility URL, click Add URL.

To update the accessibility URL, click Edit next to the existing URL.

-  
Enter your URL, then click Publish.

If your app is already live on the App Store, the URL will be published immediately but may require up to 24 hours to be visible to all users. If you haven’t published any versions of your app yet, the accessibility URL will automatically go live with the first release.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels
### App Store Connect Help

App Store Connect / Manage App Accessibility / Overview of Accessibility Nutrition Labels 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Overview of Accessibility Nutrition Labels

The Accessibility Nutrition Labels help users learn if an app will be accessible to them before they download, and give developers the opportunity to better inform and educate their users on features that their app supports. The labels appear on the app product page and will help users understand if they can use a feature like VoiceOver or Larger Text to complete common tasks in the app.

In order to give you time to prepare and evaluate your apps, providing these labels will be voluntary to start. However, you’re encouraged to report your accessibility support to help everyone, including people with disabilities, better discover apps that fit their needs. You’ll be given ample time and evaluation resources before this is mandatory, but over time, you’ll be required to share accessibility support details to submit new apps and app updates to the App Store.

## Types of Accessibility Features

Below are the accessibility features you can provide Accessibility Nutrition Labels for. We recommend that you evaluate your features in this order. Most of the work that goes into making your app accessible to VoiceOver users, for example, can also make it more accessible for users of other assistive technologies, like Voice Control and more.

Some accessibility labels aren’t available on some devices, as indicated in the table below, so you’ll be prompted to indicate support only for the accessibility features that are applicable to each device in App Store Connect.

Accessibility feature

Description

VoiceOver

Users can navigate and explore the app using gestures, keyboard, braille, and speech output.

Voice Control

Users can navigate and interact with the app using their voice to tap, swipe, click, type, and more. This isn't supported on Apple TV and Apple Watch.

Larger Text

Increases the text size in the app to 200% or more. This label isn't supported on Mac.

Dark Interface

Applies a dark color scheme to the screens, menus, and controls to reduce eye strain.

Differentiate Without Color Alone

Uses shapes or text, in addition to or instead of color, to distinguish key information.

Sufficient Contrast

Increases or adjusts the contrast between text or iconography and background.

Reduced Motion

Modifies or reduces certain types of animation that may cause motion sickness or discomfort.

Captions

Users can follow the dialog and relevant sounds of video or audio-only content with time-synchronized text.

Audio Descriptions

Users can hear audio descriptions of video content in a clip, show, or movie with time-synchronized narration.

## Discovery on the App Store

The Accessibility Nutrition Labels will appear on your app’s product page in all countries or regions where your app is available. The App Store displays the labels specific to the device type (iPhone, Mac, etc.) used to view your product page.

Note: The Accessibility Nutrition Labels will appear on Apple devices running iOS 26, iPadOS 26, macOS 26, tvOS 26, visionOS 26, and watchOS 26 or later.

You have the option to provide information for each device your app supports in App Store Connect. If you don’t provide this information for a device, the section will still appear on your product page and show that you haven’t indicated support yet. This section will also indicate if your app supports none of these accessibility features.

You also have the option to provide an accessibility URL that links to your website so that users can learn more about the app’s accessibility features. This link will show on your app's product page across all devices, except Apple TV. This accessibility URL should correspond uniquely to your app and can include information such as other accessibility features, how to turn on and manage any in-app accessibility settings, what languages are supported in captions, or areas of your app that don’t support an accessibility feature.

Users can include Accessibility Nutrition Label features as part of their search query to make their results more relevant. For example, in searches like “VoiceOver note taking apps” or “running apps with Larger Text,” apps that have indicated support for those features in their labels will be considered more relevant in search results.

## Planning for your responses

To encourage developers to respond consistently across all apps, the App Store has set evaluation criteria a developer should meet before indicating support in the Accessibility Nutrition Labels.

Before providing your responses in App Store Connect, you’ll need to audit your app to understand the level of support it provides and how it aligns to the App Store’s standards for each accessibility feature. Since your app’s support of an accessibility feature can differ per device and you can provide responses for each device in App Store Connect, you should assess your app on each of the devices your app supports.

To indicate support for an accessibility feature in the Accessibility Nutrition Labels, users must be able to complete all of the common tasks of your app using that feature.

In addition to following the evaluation criteria, make sure to follow App Review Guideline 2.3 for accurate metadata. If an app potentially has intentionally misleading or harmful accessibility labels, App Review has the ability to contact the developer and ask them to update their Accessibility Nutrition Labels.

You’re responsible for keeping your responses accurate and up-to-date. If your practices change, please update your responses.

### Identifying the common tasks in your app

To indicate support of an accessibility feature in the Accessibility Nutrition Labels, users should be able to complete all of the common tasks of your app using that feature. Before you begin evaluating features, compile a list of the common tasks that a person can perform in your app.

Common tasks checklist

Common tasks consist of the primary functionality that you expect users to perform in your app, plus functionality that's fundamental to using an app in general: first launch experience, login, purchase, and settings.

-  
Primary functionality specific to your app

-  
To indicate support for an accessibility feature, a user should be able to perceive, operate, and understand all of the primary functionality specific to your app while using the feature.

-  
To come up with your list of primary functionality, start by defining the key goals, functionality, and features users download and use your app for. It may be helpful to consider what you market in your app’s description, screenshots, and app previews.

As an example, a to-do list app’s common tasks will include these tasks below.

-  
View task list

-  
The user may need to mark a task as complete, undo marking a task as complete, change the due date, or create a new task.

-  
Task detail view

-  
For a new or existing task, the user may need to enter information about the task, save the task to a list, or exit the screen without making modifications.

-  
First launch experience

-  
To indicate support for an accessibility feature, a user should be able to complete the app’s first launch experience while using the accessibility feature. For example, your first launch experience may have a video with sound that you may want to express in captions, or an onboarding flow that a user should be able to complete or skip.

-  
Login

-  
To indicate support for an accessibility feature, a user should be able to complete the login experience while using the accessibility feature. For example, the user should be able to choose a login service, enter a username and password, interact with a login button, request a password reset, or enter information to create a new account.

-  
Purchase

-  
If your app offers purchases, to indicate support for an accessibility feature, a user should be able to complete the purchase experience while using the accessibility feature. For example, the user should be able to select a payment provider, enter a credit card number, review the terms of an offer, or review before completing the purchase.

-  
Settings

-  
To indicate support for an accessibility feature, a user should be able to adjust app settings while using the accessibility feature. For example, the user should be able to turn on accessibility or privacy features, manage purchases, or exit the settings screen without modifying settings.

Ensuring a comprehensive list

As you make your list, consider the following to ensure you have a comprehensive list of common tasks:

-  
Make sure your list includes common tasks that users both with and without disabilities can perform.

-  
Consider differences by device, such as if a certain experience is only available on Apple Watch but not Mac.

-  
Include tasks that you make mandatory to use your app, such as account sign-up or purchasing a subscription.

-  
Especially for new users, consider default and loading screens, such as the screen to view the task list when the user hasn’t added tasks yet.

-  
Consider actions a user can take outside your app that are common tasks, such as marking a task complete in a notification or widget from your to-do list app.

-  
When evaluating, you're not required to consider tasks that are uncommon in your app. If you're unsure if a task is common, ask yourself whether you'd ship an urgent fix if users were blocked from completing this task. For example, if your app provides links to your app’s marketing channels on social media and web but that isn’t a key goal of using the app, you're not required to include it in your evaluation. If you want to provide more information about the accessibility of uncommon tasks, use the accessibility URL to do so.

Recommended: Create an accessibility testing matrix

After you identify your app’s common tasks, to guide your evaluation, it may be helpful to create an accessibility testing matrix for each device you plan to provide Accessibility Nutrition Labels for in App Store Connect. Following this matrix isn’t required, but it can help make sure you’re validating that all common tasks can be completed for an accessibility feature on that device. This is especially helpful since some of your app’s common tasks may not be available on some devices, and some accessibility features aren’t available on certain devices.

To start, create a matrix for each device you’ll be evaluating for Accessibility Nutrition Labels.

For each matrix, take the common tasks that are available on that device, and add them as rows. For example, if a common task is only available on Mac but not Apple Watch, include the common task in your matrix for Mac but not your matrix for Apple Watch.

Next, consider the accessibility features you want to evaluate. Since some accessibility features aren’t available on certain devices, you won’t be able to provide Accessibility Nutrition Labels for them. Take the accessibility features that are available on that device, and add them as columns.

Now you're ready to evaluate your app.

## Tips

Implementation

-  
Whenever possible, use the Apple-provided native API to reduce implementation complexity and so customers who have turned on the system setting will automatically get this experience without an additional setting. We highly recommend Apple-provided native APIs for complex app behaviors, such as drag and drop or multi-touch gestures.

-  
Provide native support for core assistive technologies, including VoiceOver and Voice Control. These assistive technologies allow connection to hardware interfaces, such as braille displays, and interaction with operating system features, like app switching, that your app otherwise wouldn’t be able to support. Don’t attempt to make a custom implementation of the functionality provided by core assistive technologies like VoiceOver or Voice Control.

-  
With the exception of core assistive technologies like VoiceOver and Voice Control, you may use a custom implementation to indicate support for your labels, such as a custom dark color scheme, instead of using the system’s standard dark appearance.

-  
Even if you use a custom implementation for an accessibility feature, consider leveraging the user’s system setting to ensure your app responds to their needs. For example, if you render custom captions in a game, check the user’s system setting that indicates a need or preference for displaying captions when available. If you offer your own in-app setting, it should offer more granular user interface customization than the system setting provides.

-  
Pay extra attention to custom elements, since they are less likely than standard elements to have accommodations for accessible experiences. Additionally, some custom elements may require additional work to support features like VoiceOver and Voice Control.

Third-party content

-  
You don’t have to consider third-party or user-generated content when evaluating accessibility labels if those views aren’t part of your common tasks.

-  
When third-party or user-generated content views are part of your common tasks, you don’t need to ensure all third-party content is accessible, but your app should provide the third-party content creators a reasonable, discoverable way to make their content accessible. For example:

-  
In most video streaming apps, developers support a way to display closed captions, even though not all third-party movie and television studios provide captions with their video content.

-  
In apps that allow users to upload images, developers should provide a way for the users to label the image, so the image content is perceivable to VoiceOver users.

-  
In apps that use a web view to load third-party websites, WebKit provides default support for most accessibility labels for web content by using web standards like HTML, CSS, and ARIA.

-  
In addition, web browsers like Safari provide additional accessibility features, like site-specific font size settings, which allow users to enlarge the font sizes of web sites to 200% the default size, or sometimes larger.

Best practices

-  
The common guiding principles of accessibility are that content, controls, and interfaces should be perceivable, operable, understandable, and robust. Keep these principles in mind as you’re evaluating your app. For example, a blind VoiceOver user should be able to perceive the content of a visual photograph or icon, often by experiencing its text alternative label as speech or braille. Likewise, if most users can operate an item by tapping, clicking, or dragging it, the item should also be operable to assistive technologies like VoiceOver and Voice Control, so that users with disabilities can use all the same functions of an app.

-  
You may consider exceptions to the recommendations here if users with disabilities would find them reasonable. For example, you might hide a button from VoiceOver in one view if it duplicates functionality that’s already available and discoverable elsewhere.

## Additional guidance

Your app has bugs that affect its accessibility.

If bugs are significant enough to change your answer according to the Accessibility Nutrition Labels evaluation criteria, then don’t indicate support for the accessibility feature. To avoid misleading users, you shouldn’t enter answers that aren’t aligned with the evaluation criteria.

An accessibility feature doesn't apply to your app.

Review the evaluation criteria for the accessibility feature to determine if it's applicable and whether to indicate support.

You have additional accessibility information to share with users.

Add an accessibility URL to your product page to provide users additional accessibility information, such as other accessibility features, how to turn on and manage any in-app accessibility settings, what languages are supported in captions, or areas of your app that don’t support an accessibility feature feature.

Your app includes app extensions.

Your app may include app extensions such as stickers, custom keyboards, Safari extensions, or photo editing extensions. To determine whether to include app extensions in your evaluation, determine whether they are part of your app’s common tasks. If using the app extension isn't part of your app’s primary functionality, then it's unlikely to be one of your app’s common tasks.

Your app has advertising.

Include advertising in your evaluation if it’s present in the UI when users are completing your app’s common tasks. If the advertising experience prevents users from completing a common task using an accessibility feature (for example, the advertisement contains problematic motion that can't be addressed by a system or in-app setting to reduce motion), then don’t indicate support for the feature.

Your app is a compatible iPhone and iPad app on Apple Vision Pro.

If your iPhone and iPad app is compatible with and can run on Apple Vision Pro, no responses are needed for Apple Vision Pro. The labels for iPhone or iPad will be shown to users on the Apple Vision Pro App Store.

Your app is a compatible iPhone and iPad app on Macs with Apple silicon.

If your iPhone and iPad app is compatible with and can run on Macs with Apple silicon, no responses are needed for Mac. The labels for iPhone or iPad will be shown to users on the Mac App Store.

At Apple, we believe that the best technology works for everyone to help them connect, create, play, and do what they love in the ways that work best for them. Even after you’re able to claim support for an accessibility feature in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Can all users use all features of the app, not just the common tasks? While it’s not required, we encourage you to go beyond this criteria to provide the most accessible experience you can for all users.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Watch “Prepare your app for Accessibility Nutrition Labels” Watch “Evaluate your app for Accessibility Nutrition Labels”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Reduced Motion evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Reduced Motion evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Motion can enrich app experience, but certain types of motion, such as scaling, spinning, or peripheral motion, cause dizziness or nausea for people with motion sensitivity. Although motion sickness is commonly discussed in the context of augmented and virtual reality, motion can cause reactions in 2D screens as well for users with severe motion-sensitivity conditions. If your app includes these motion triggers, make them optional or provide alternative animations.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability.

The goal of Reduced Motion is to support users with extreme motion sensitivity, who may experience negative side effects, such as nausea, dizziness, headaches, or distraction when encountering certain types of motion triggers. Often, the problematic types of motion are spinning or scaling, and other techniques used to simulate three-dimensional effects or depth.

Well designed animations can convey information intuitively, increasing the usability and understandability of your app. Removing such animations unnecessarily might make your app experience more confusing, so don’t remove or modify all animations prematurely. Review the support criteria below to determine which animations to leave as they are, which animations to modify, and which animations to consider removing entirely.

The following sections provide more detail about how to determine whether your app supports Reduced Motion well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app supports Reduced Motion on the App Store.

### Getting started with testing

While you’re not required to use Apple frameworks to indicate support for Reduced Motion, we recommend reviewing how Apple’s system apps respond to the systemwide setting to understand what a good experience is like for users. If you offer your own in-app setting, it should either support similar functionality to the systemwide setting, or offer more granular user interface customization.

Review the resources below for details about enabling the Reduce Motion system setting on each device your app supports.

-  
For iPhone, watch “How to reduce screen motion on iPhone, iPad, and iPod touch” and visit Customize onscreen motion on iPhone.

-  
For iPad, watch “How to reduce screen motion on iPhone, iPad, and iPod touch” and visit Customize onscreen motion on iPad.

-  
For Mac, visit Customize onscreen motion on Mac.

-  
For Apple TV, visit the Reduce screen motion on Apple TV 4K.

-  
For Apple Vision Pro, visit Stop or reduce visual motion effects or screen movements on Apple Vision Pro.

-  
For Apple Watch, visit the Adjust text size and other visual settings on Apple Watch.

If you don’t have an existing proficiency in testing reduced motion, take some time to go beyond the basics and review the additional resources below.

-  
Human Interface Guideline > Motion

-  
Human Interface Guideline > Accessibility

## Indicating support for Reduce Motion

You’re not required to adopt Apple frameworks to indicate support for Reduced Motion, but we recommend detecting when a user has the Apple system setting enabled so they don’t have to manually update another setting for the app to function as expected. If you offer your own in-app setting that has additional customization or granular controls, you may not need to use the Apple system setting.

When testing your app, determine if any views or transitional animations include potential motion triggers that can cause discomfort or distraction for some users. If your app doesn’t contain any problematic motion triggers, you may indicate that it supports Reduced Motion.

-  
If your app uses depth simulation (including parallax effects, animated blur, and depth-of-field effects), you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion.

-  
If your app includes multi-axis motion, multi-speed motion, spinning, or vortex effects, you should disable or change the animation when the user’s setting indicates a need or preference for reduced motion.

-  
If your app includes auto-advancing carousel screens or any other ongoing motion, consider stopping the motion based on the user’s setting, or providing a control to allow the user to stop the motion.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

-  
Review the related links below for more examples of motion triggers.

If your app does contain these types of motion, consider each animation individually.

-  
Is the animation included purely for stylistic or decorative effect? If so, consider stopping it entirely when the user’s system setting indicates a need or preference for reduced motion.

-  
Removing animations entirely can have a negative effect on usability and understandability. If the motion itself conveys some meaning, such as a status change (for example, item moved to cart) or a hierarchical context transition (for example, this view is a subview of the prior view), don’t remove the animation entirely. Instead, consider providing a new animation that avoids motion, or at least reduces full screen motion, such as a dissolve, highlight fade, or color shift. Also consider whether you want to replace your default animation, or only use the new one when the user’s setting indicates a need or preference for reduced motion.

Once your app no longer displays problematic motion triggers to users whose setting indicates a need or preference for reduced motion, you may indicate that it supports Reduced Motion.

Even after you’re able to indicate support for Reduced Motion in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Reduced Motion every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Captions, and Audio Descriptions.

Related Improving accessibility support in your visionOS app 
Human Interface Guideline > Designing for visionOS
Watch “Make your app visually accessible” Watch “Design considerations for vision and motion“ Responsive Design for Motion

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Sufficient Contrast evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Sufficient Contrast evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Sufficient Contrast helps users whose vision is reduced due to a disability or situational impairment such as bright sunlight. Users can increase or adjust the contrast between text or iconography and the background, improving readability.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. The goal of the Sufficient Contrast feature is to support low-vision users who may have reduced visual acuity, clarity, and/or contrast perception.

The following sections provide more detail about how to determine whether your app supports Sufficient Contrast well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Sufficient Contrast on the App Store.

### Getting started with testing

The accessibility settings for each device include a number of features that can help users customize contrast to fit their needs. Most users that have a need for higher contrast will enable the settings for Bold Text, Increase Contrast, and Reduce Transparency. You’re not required to use the built-in system settings, but testing with them on may give you an understanding of the contrast minimums your users expect. If you offer your own in-app setting, it should either support similar functionality to the systemwide settings, or offer more granular user interface customization.

Enable all three settings before testing your app for sufficient contrast. Review the resources below for details about turning on these settings for each device your app supports.

-  
For iPhone, visit Change display colors on iPhone to make it easier to see what’s onscreen.

-  
For iPad, visit Make text easier to read on iPad.

-  
For Mac, visit Make text and icons bigger on Mac and Change Display settings for accessibility on Mac.

-  
For Apple TV, visit Display bold text on Apple TV and Increase Apple TV screen contrast.

-  
For Apple Vision Pro, visit Text display settings on Apple Vision Pro and Adjust colors and contrast on Apple Vision Pro.

-  
For Apple Watch, visit Adjust text size and other visual settings on Apple Watch.

You can check the contrast of elements in your app by using Xcode’s Accessibility Inspector or other color contrast checkers to determine contrast ratios for elements in your app. Most modern accessibility guidelines recommend a minimum contrast ratio of “4.5 to 1 between foreground text and its background” based on a formula provided by the World Wide Web Consortium’s (W3C’s) Web Content Accessibility Guidelines.

If your app supports Dark Mode, be sure to check the minimum contrast in both light and dark modes. A common mistake is supporting sufficient contrast in your light mode interface, but forgetting to support sufficient contrast in a dark interface. Many developers use gray-on-black for dark mode reading, which can reduce eye strain for standard vision in low-light scenarios, but this reduced contrast variant may be more difficult to read for those with low vision or light sensitivity. Consider testing your app while combining the dark mode color scheme alongside the Increase Contras setting.

Consider not only contrast, but also translucency (opacity/blurring) of your background materials, controls, and content. Include legibility of text, icons, and other content, elements, and controls in your evaluation. Remember to test with Increase Contrast on and Reduce Transparency off, and with both settings on.

Make sure to provide sufficient contrast on interactive controls and non-text representations of a state, such as a selection. For example, if you design a custom checkbox, make sure there is sufficient contrast between the checked and unchecked states. Meeting a 3:1 minimum contrast ratio is commonly recommended for non-text contrast.

If you don’t have an existing proficiency in testing sufficient contrast, take some time to go beyond the basics. Review Strive to meet color contrast minimum standards in the Human Interface Guidelines to understand if the contrast of adjacent colors in your UI meets minimum acceptable levels.

A button with insufficient color contrast.  
A button with sufficient color contrast.   

The systemRed default color in iOS.  
The systemRed accessible color in iOS.    

## Indicating support for Sufficient Contrast

You may indicate your app supports Sufficient Contrast if the user interface for your common tasks, including text, buttons, and other controls, meets general contrast guidelines by default — usually 4.5 to 1 for most text elements.

If your app doesn't provide this minimum contrast by default: 

-  
If your app uses Apple-provided UI frameworks, verify that the Increase Contrast setting applies sufficient contrast.

-  
If your app supports custom frameworks, provide users with a choice of multiple color schemes that meet contrast minimums.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

Even after you’re able to indicate support for Sufficient Contrast in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app’s support for Sufficient Contrast every time you update the app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Reduced Motion, Captions, and Audio Descriptions.

Related Watch “Make your app visually accessible”

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voice-control-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / Voice Control evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# Voice Control evaluation criteria

iOS macOS visionOS  

## Description

Using Apple’s Voice Control feature, users with reduced mobility or dexterity can navigate an app’s interface using only their voice. When looking at the screen, they can use commands like “tap," "click," or "swipe" to interact with on-screen elements.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. If you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should strive to make it work with Voice Control, too. 

Note: Most of the work that goes into making your app accessible to VoiceOver users will also make it more accessible for Voice Control users. For this reason, we recommend you start with the  VoiceOver evaluation criteria before evaluating Voice Control.

The following sections provide more detail about how to determine whether your app supports Voice Control well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports Voice Control on the App Store. 

### Getting started with testing

In order to accurately indicate support, proficient testing of your app using Voice Control is necessary on all platforms for your app. Even if you already have a basic proficiency in testing with Voice Control, take some time to go beyond the basics. 

Review the resources below to learn more about using Voice Control for each device your app supports. 

-  
For iPhone, watch “How to use Voice Control on iPhone, iPad, and iPod touch,” then visit Use Voice Control commands to interact with iPhone and  Use Voice Control on your iPhone, iPad, or iPod touch.

-  
For iPad, watch “How to use Voice Control on iPhone, iPad, and iPod touch,” then visit  Use Voice Control commands to interact with iPad and Use Voice Control on your iPhone, iPad, or iPod touch.

-  
For Mac, visit Get started with Voice Control on Mac.

-  
For Apple Vision Pro, visit the Use Voice Control to interact with Apple Vision Pro.

## Indicating support for Voice Control 

You may say your app supports Voice Control if users are able to navigate and interact with your app using only voice commands. Users should be able to complete all of the common tasks, actions, and functions of your app using only Voice Control, without touching the display.

Using only their voice, users should be able to activate all tappable or clickable elements on the screen.

-  
Speak “Show numbers” to make sure all buttons, links, and other interactive elements display a number. 

-  
Speak “Show names” to make sure all buttons, links, and other interactive elements display a label, also known as “alternative text.” Refer to the VoiceOver evaluation criteria for more tips on writing good default labels, and review how to  use accessibilityInputLabels(_:) for Voice Control.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

-  
Use commands like “tap” or “click” plus the name or number of a control to drive your app’s common workflows. For example, “Tap Compose,” “Click Back,” or “Tap 4.” 

-  
Match Voice Control labels to the visible text. If the Voice Control label is different from the visible text in your app (for example, “Leave call” instead of “End call”), users may be confused. Your users may be forced to speak “Show names” in order to understand why Voice Control isn’t working as they expected with your app.

Using only their voice, users should be able to operate all interactions in your app, including those that are more complex.

-  
If your app uses swipes, long presses, secondary clicks, or other ways to show additional interactive controls, make sure those are accessible to Voice Control users. For example, use a custom action. Elements with custom actions will be indicated with a double chevron; try speaking “Show actions for <number>.”

-  
If your app reveals a hidden user interface (for example, on hover or swipe), make sure that the user has a speech-only way to show the hidden elements or trigger the same behavior through an action or context menu.

-  
Ensure scrolling works in your app. For example, “Scroll down.” For panning views like maps or layout canvases, try out speech commands such as “Pan left” and “Zoom out.”

-  
If other multi-touch gestures are required, try speaking the gesture, such as “Swipe up with two fingers.”

-  
If your app has a recording option, or if you have a custom dictation function, ensure users can start and stop the recording using only their voice.

Using only their voice, users should be able to dictate and edit text in any text field.

-  
Make sure that users can dictate text in any text field in your app. Speak “type” and the text you’d like to type.

-  
Try speaking commands like “Select” and the text you want selected. Ensure the text is selected, then speak “Delete that” and verify the text is deleted. 

-  
If you use standard text fields from Apple frameworks, Voice Control will be automatically supported. However, if you use your own custom text entry or a third-party framework, extra work may be required. For example, Apple has an open-source accessibility plug-in for Unity-based apps.

-  
If your app uses any custom text fields, text entry behavior, or input validation, review and test the rest of Voice Control’s text commands very carefully.

### Additional suggestions

-  
Some users with physical or cognitive impairments may need more time, or wish to avoid distracting auto-play defaults. If aspects of your app auto-play or auto-hide on a time delay, consider allowing users to cancel or extend that delay. 

-  
Consider implementing SiriKit and App Intents to make your app better for all users, including Voice Control users. Review  “Bring your app to Siri” for more details.

Even after you’re able to indicate support for Voice Control in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app's support for Voice Control every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for VoiceOver, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Learn How to Develop for Voice Control Watch “Writing Great Accessibility Labels“ Review how to use accessibilityInputLabels(_:) for Voice Control
Watch “Accessibility design for Mac Catalyst” Watch “Catch up on accessibility in SwiftUI” Watch Apple Support “Mobility Features“ playlist for iPhone & iPad

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voiceover-evaluation-criteria
### App Store Connect Help

App Store Connect / Manage App Accessibility / VoiceOver evaluation criteria 
Filter ⌘K  
Filter ⌘K  

Manage app accessibility  

# VoiceOver evaluation criteria

iOS macOS tvOS visionOS watchOS  

## Description

Using Apple’s VoiceOver screen reader, users can navigate an app’s interface without needing to see the screen. Many people who are blind or low vision use VoiceOver to understand and control apps.

### Goals

Everyone should be able to use your app, regardless of whether they have a disability. If you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should strive to make it work with VoiceOver, too. If you can see an important item on the screen, your app should use a label or description that a VoiceOver user would perceive in audible speech or braille.

Note: Most of the work that goes into making your app accessible to VoiceOver users will also make it more accessible for users of other assistive technologies like Voice Control, Switch Control, and Hover Text. For this reason, we recommend you start your accessibility evaluation with VoiceOver before moving on to test Voice Control.

The following sections provide more detail about how to determine whether your app supports VoiceOver well. The goal is to help ensure users with disabilities can leverage all common tasks of the app, therefore performing this evaluation will help you determine whether to indicate your app Supports VoiceOver on the App Store.

### Getting started with testing

In order to accurately evaluate this label, proficient testing of your app using VoiceOver is necessary on all devices your app supports. To ensure your proficiency in testing with VoiceOver, take some time to review the resources below.

-  
For iPhone, watch "How to Navigate your iPhone or iPad with VoiceOver,” then visit Turn on and practice VoiceOver on iPhone, Use VoiceOver Gestures on iPhone, and Operate iPhone when VoiceOver is on.

-  
For iPad, watch  "How to Navigate your iPhone or iPad with VoiceOver,” then visit Turn on and practice VoiceOver on iPad, Use VoiceOver gestures on iPad, and Operate iPad when VoiceOver is on.

-  
For Mac, visit Learn and practice VoiceOver on Mac, then review other topics in the VoiceOver User Guide for macOS.

-  
For Apple TV, visit Use VoiceOver on Apple TV.

-  
For Apple Vision Pro, visit Turn on and practice VoiceOver on Apple Vision Pro, and Learn VoiceOver gestures on Apple Vision Pro.

-  
For Apple Watch, visit Use VoiceOver on Apple Watch.

Once you’ve learned the basics of VoiceOver, you’re ready to begin testing. However, to ensure the best VoiceOver experience for users, we recommend diving deeper into the user guides to learn about advanced functionality that experienced VoiceOver users may rely on.

## Indicating support for VoiceOver

You may indicate your app supports VoiceOver if users are able to navigate and interact with visual elements, including text, media, buttons, and controls, using only VoiceOver. Using gestures or keyboard commands, users should be able to focus on each part of the UI, hear what it is, and activate it. Make sure users can complete all of the common tasks of your app using only VoiceOver, without sighted assistance.

All controls should have concise, accurate labels.

Labels, also known as “alternative text,” help VoiceOver users to quickly understand the purpose of each control or interface element.

-  
Buttons, icons, form controls, and all other elements should contain a concise label providing a text equivalent for VoiceOver users. Interactive text fields and similar form controls should have a label (for example, “phone number”) in addition to the text value (“555-555-1212”) of the selection or contents.

-  
Labels should be concise, so that the interface isn’t tedious for a user to navigate and understand quickly. For example, a button for composing a new message should be labeled “New Message” rather than something more verbose like “Press to compose a new message.” 

-  
Ensure the labels make sense out of context. Because VoiceOver users may land on an element in different ways, avoid ambiguous labels that are unclear when the user encounters the item in a non-linear order, such as “Click here” or “Learn more.” If multiple action elements have the same label, like “Delete” in a Shopping Cart, the label text should make it clear what the action will do, especially in the case of destructive actions. For example, which cart item will be deleted?

-  
Ensure that labels don’t include control types like "checkbox" or states like "checked." Otherwise, VoiceOver may speak redundant information to the user, such as “Unsubscribe checkbox, checkbox.” Instead, implement these in your app as traits or through similar APIs appropriate to the device.

-  
Most images should include a relevant description or alternative text. If an image is purely decorative, make sure it’s ignored completely by VoiceOver.

-  
If your app provides a way for users to upload media, such as images, ensure users have a way to include labels or descriptions for the user-generated content, so that VoiceOver users can hear this description when encountering the media.

-  
Charts and other data visualizations should include accessibility information through a more specific chart API, or at minimum, include a reasonably complete text alternative.

-  
If third-party or user-generated content is required in your common tasks, refer to the detailed guidance for third-party content on the Overview of Accessibility Nutrition Labels.

-  
For more ideas, watch “Writing Great Accessibility Labels“ and "Bring accessibility to charts in your app."

VoiceOver users should be aware of element type and control status or value.

People who rely on VoiceOver often need to hear more information than just labels and text content, since the status or value may be conveyed only through visual means such as a checked box. Implement this information in your app as traits or through similar APIs appropriate to the device.

-  
When a VoiceOver user lands on an item, VoiceOver should speak the type of element in addition to the label or text content. For example, “Unsubscribe from all emails, checkbox."

-  
Users should be able to understand control state and values. Keep in mind that default states, like the “unchecked” state of a checkbox, are implied so they may not be spoken by VoiceOver. For example, “Unsubscribe from all emails, checkbox.” Additionally, take care to update the API for control state and values. For example, once the user has checked the checkbox, VoiceOver will describe the control, including its new state, as, “Unsubscribe from all emails, checked checkbox."

VoiceOver should be able to speak all visible text in your app, and all text entry methods should be operable by VoiceOver users.

The accessibility of most visible text will be automatically supported when using Apple frameworks. However, if your app uses another framework, or custom text entry methods, extra work may be required. For example, Apple has an open-source accessibility plug-in for Unity-based apps.

-  
All visible text in the app should be accessible to assistive technologies, including VoiceOver. Plain text elements, such as paragraphs, don’t need a separate label, though you should ensure that VoiceOver can speak the text content.

-  
Custom keyboards and text entry methods (for example, custom keyboards or PIN code entry widgets) should be operable with VoiceOver, and produce correct speech/braille output for the user, in addition to providing accurate text entry and selection.

-  
Temporary status banners and important in-app alerts should be conveyed to VoiceOver users in a timely but non-disruptive manner, often done so with an AccessibilityNotification.

VoiceOver navigation and grouping should be consistent, complete, and use a logical order.

VoiceOver users should be able to navigate in page order, or move directly to a part of the screen using features like the VoiceOver rotors.

-  
VoiceOver users should be able to navigate to any visible element, either in order (swipe right, VO+Right, and so on) or by using a rotor and touch navigation on most platforms.

-  
VoiceOver users should be able to navigate away from the element they are on, whether by continuing forward, going backward (Swipe Left, VO+Left, etc), or by using a rotor or touch navigation on most platforms.

-  
If multiple elements or actions are presented as a group, VoiceOver users should be able to either move to each item in the group, or be able to interact with the grouped behaviors (for example, reply, forward, delete) through features like custom actions.

-  
VoiceOver users should be able to progress to each element without skipping items or looping back to the same item repeatedly. Try navigating forward through all contents, then backwards through all contents. Try looping through all rotor items forward and backwards, too.

-  
When content reloads or refreshes in the background, a VoiceOver user’s reading position shouldn’t reset unexpectedly. For example, if a VoiceOver user is near the bottom of a content feed when the app loads more content, the VoiceOver cursor shouldn’t accidentally reset to the top of the list.

-  
When the screen changes or a modal dialog appears, the VoiceOver cursor should move logically into the new content area. VoiceOver users shouldn’t be able to move into invisible, offscreen, or background content.

All interactive elements and controls should be discoverable, operable, and work consistently with VoiceOver.

As a reminder, if you can tap, click, or drag something in your app using a mouse or touchscreen gestures, you should make it work with VoiceOver, too.

-  
VoiceOver’s activation gesture (select then double-tap) and keyboard command (VO+space) should trigger the same behavior as a standard tap or click.

-  
Standard keyboard operations (for example, arrow keys) and keyboard modifier shortcuts should continue to work, even when VoiceOver is active, and the VoiceOver cursor should follow changes triggered by standard keyboard navigation like the Tab key, arrow keys, and more.

-  
If your app’s controls provide a context menu, overload a long press, or provide other non-default behaviors, consider providing the same behaviors as a custom action using VoiceOver’s actions rotor or its equivalent “show context menu” keyboard command (VO+Shift+M).

-  
VoiceOver should work with modal views, like dialogs. Apps should ensure that inactive content behind the modal view isn’t accessible to VoiceOver while the content is inactive. Apps should also support VoiceOver users being able to dismiss modal views, like closing the dialog, using the Escape key or an accessibilityPerformEscape action.

-  
Complex app behaviors, such as drag and drop or multi-touch gestures, should be provided in an accessible, discoverable way, such as through a custom rotor or action. Whenever possible, use the Apple-provided native API to reduce implementation complexity.

-  
Custom elements, if used by the app or any included frameworks, should provide equivalent accessibility of native elements provided by the Apple UIKit, AppKit, and SwiftUI frameworks. For example, custom buttons, tab bars, and sliders should be operable with VoiceOver and convey the same information as controls using standard API equivalents.

Even after you’re able to indicate support for VoiceOver in the common tasks of your app, there are likely further improvements you’ll be able to make to the accessibility of your app. Re-evaluate your app's support for VoiceOver every time you update your app. Set a goal to make your app more accessible to more people in every release.

Learn more about the evaluation criteria for Voice Control, Larger Text, Dark Interface, Differentiate Without Color Alone, Sufficient Contrast, Reduced Motion, Captions, and Audio Descriptions.

Related Learn more about VoiceOver Support VoiceOver in your app 
Human Interface Guidelines > Accessibility
Watch "Tailor the VoiceOver experience in data-rich apps Watch "VoiceOver efficiency with custom rotors

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/add-an-app-icon
### App Store Connect Help

App Store Connect / Manage app information / Add an app icon 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Add an app icon

An app icon serves as the representation of your app, and it appears on the Home Screen and in key locations throughout the system, including search results, notifications, system settings, share sheets, and TestFlight. For design guidance on app icons, visit Human Interface Guidelines > App icons.

You can create your app icon using Icon Composer or add your app icon to an asset catalog within your Xcode project. After adding icons in Xcode, upload the build to App Store Connect.

If you want to change your app icon after publishing, you must create and upload a new version of your app. Then, submit it for review.

Required role: Account Holder, Admin, App Manager, or Developer. View role permissions.

Related View and edit app information Get started with app discovery and marketing

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/complete-the-digital-goods-and-services-questionnaire
### App Store Connect Help

App Store Connect / Manage app information / Complete the Digital Goods and Services questionnaire 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Complete the Digital Goods and Services questionnaire

The App Store empowers you to scale your app distribution worldwide using a variety of business models, including the sale of digital goods and services in your apps. Digital goods and services are content, features, subscriptions, and other digital experiences offered or consumed within an app. Complete the Digital Goods and Services questionnaire in App Store Connect to indicate how customers pay for or access digital goods and services in your app.

Completing this questionnaire helps ensure your app complies with the App Review Guidelines, Developer Program License Agreement, and helps you identify supported payment options for your customers.

Note: If this questionnaire doesn’t appear in App Store Connect for your app, no action is required.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Indicate payment options

Indicate how customers consume and access digital goods and services in your app across regions. Digital goods and services are content, features, subscriptions, and other digital experiences offered or consumed within an app.

-  
From Apps, select your app.

-  
In the sidebar under General, click App Information.

-  
Scroll to the Digital Goods and Services in Your Apps section, then click Get Started.

-  
Answer the questions:

-  
If you select No to “Can customers consume digital goods and services in this app?”, click Next.

-  
If you select Yes, confirm whether your app uses Apple In-App Purchase exclusively, or select the available payment options (such as alternative payment processing or out-of-app offers) for each country or region where you offer digital goods and services. Then click Next.

-  
Confirm and save:

-  
On the Confirmation page, take a moment to look over your answers and make any changes before submitting.

-  
Click Save.

To edit your answers later, click Edit under Digital Goods and Services in Your App.

Note: After you submit this form, your choices for the European Union remain locked for 12 months and can’t be changed. If you have questions, contact us.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/declare-regulated-medical-device-status
### App Store Connect Help

App Store Connect / Manage app information / Declare regulated medical device status 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Declare regulated medical device status

To provide additional transparency on the App Store, apps that are available in the European Union (EU)/European Economic Area (EEA), United Kingdom (UK), or United States (US), and that also meet either of the criteria listed below must indicate whether they’re regulated medical device with respect to each region’s regulatory authority or body responsible for the governance and compliance of medical devices.

-  
Have a primary or secondary category of Health & Fitness or Medical

-  
Have indicated your app contains “frequent” in the Medical or Treatment Information field in the age rating questionnaire in App Store Connect

Regulated medical device apps are used for a range of medical purposes, including diagnosis, prevention, monitoring, and treatment of diseases and physiological conditions. They may function on their own or by interfacing with medical device hardware. These apps may require registration or authorization from regulatory bodies such as the U.S. Food and Drug Administration (FDA). Learn more about regulated medical devices in the EU/EEA, in the UK, and in the US.

If your app doesn’t provide any health or medical features, or access health data to support non-health features, you should select No, to declare that your app is not a regulated medical device.

If your app is a regulated medical device, you'll need to provide the following information. In some instances this'll require obtaining authorization or completing registration from the region’s regulatory authority. This information will display to customers on your App Store product page.

-  
EU Manufacturer SRN or FDA Owner/Operator Number: This should align with your EUDAMED listing and/or FDA establishment registrations. This isn't required for the UK.

-  
Instructions for use URL: The URL containing the user guide or instructions for use for your app, hosted on your website.

-  
Use statement: For the US, this is your indications for use statement. For the EU/EEA and UK, this is your intended purpose or intended use statement.

-  
Safety information: Provide relevant warnings, precautions, and contraindications as they appear in your labeling. For the US, this is also where you can include a statement about how users can report a problem to the FDA such as "To report a problem or adverse event to the FDA, visit www.fda.gov/safety/report-problem-fda". 

## How to know if your app is a regulated medical device

-  
Your app was cleared or approved by the US FDA

-  
Your app is registered on the US FDA medical device database

-  
Your app was issued a CE mark by an EU-based notified body for compliance with the EU Medical Device Regulation (MDR) or Medical Device Directive (MDD)

-  
Your app was issued a UKCA mark by a UK-based approved body for compliance with the UK Medical Device Regulations

-  
You’ve self-certified your app under the EU Medical Device Regulation (MDR) or Medical Device Directive (MDD)

-  
You’ve self-certified your app under the UK Medical Device Regulations 

Required role: Account Holder or Admin. View role permissions.

### Declare regulated medical device

-  
In Apps, select the app you want to view.

-  
In the sidebar, under General, click App Information.

-  
Under App Store Regulations & Permits, click Declare Regulated Medical Device.

-  
Indicate if your app is a regulated medical device in any country or region.

-  
If you select No, click Save and you are done.

-  
If you select Yes, continue with step 5.

-  
Select which countries your app is a regulated medical device in and click Save.

-  
Complete the required information for each country or region where your app is considered a regulated medical device.

-  
Verify your contact information that will appear on the App Store. If this information is inaccurate, you’ll need to update it in the Business section of App Store Connect.

-  
Enter your EU Manufacturer SRN or FDA Owner/Operator Number for the US as applicable

-  
Provide the instructions for use URL, use statement, and safety information. If you wish to localize this information, you can add the required details in each localization from the dropdown menu.

-  
Once all the information has been completed and verified, click Save, and the information will go live on the App Store within 24 hours. If the app is not yet approved to be live, the information will go live once the app is approved and released to the store.

### Update your regulated medical device declaration

You can click Edit next to the Regulated Medical Devices section to change your declaration for your app or to add or remove countries and regions.

If you have declared that your app is a regulated medical device and need to update the information provided, you can click Edit next to the country or region that needs to be updated in order to make the necessary changes.

You can also manage your contact information by going directly to the Business section and selecting Regulated Medical Devices under the Compliance section.

Updated information will be reflected on the App Store within 24 hours of saving the changes.

### Regulated medical device statuses

Status

Definition

Yes

You've declared your app is a regulated medical device in this country or region and entered the required information.

No

You've indicated that your app is not a regulated medical device in this country or region.

Missing Info

You've indicated that your app is a regulated medical device in this country or region, but have not completed the required information.

Related App information Required, localizable, and editable properties

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags
### App Store Connect Help

App Store Connect / Manage app information / Manage app tags 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Manage app tags

App tags are glanceable terms that help people understand more about your app or game’s essential qualities. In addition to appearing in App Store search results, app tags can now appear on your product page, further improving the discoverability of your apps and games on the App Store. From these placements, people can tap a specific tag - for example, Sleep - to view more apps and games related to that specific tag. Tags are based on the App Store metadata you provide in App Store Connect, artificial intelligence, and human curation. You can also manage which of your selected tags appear across the App Store in the app information section of App Store Connect.

App Tags allow you to:

-  
Increase discoverability: Tags appear as glanceable terms in search results and as clickable entities on Search Landing Page and Product Page.

-  
Connect with the right audience: Tags align your app with user intent, leading to improved relevance.

You can manage tags in App Store Connect to ensure they are relevant to your app’s functionality. Currently, tags are only supported and displayed to users across the App Store in the United States. 

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Edit App Tags

Tags are applied to your app by default, based on the metadata you provide in App Store Connect (en_US only). You can deselect the tags you don't want associated with your app. Deselecting all tags may affect your discoverability on the App Store.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Information, under General.

-  
Below App Store Tags, click Edit. 

- In the pop up window, review your selections. Make any desired changes, and click Save.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement
### App Store Connect Help

App Store Connect / Manage app information / Provide a custom license agreement 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Provide a custom license agreement

Apple provides a standard end-user license agreement (EULA) that applies in all countries and regions. If you don’t provide a custom EULA, the standard EULA is applied to your app and the license agreement link isn’t shown on your App Store product page.

Learn how to manage your EULA with the App Store Connect API.

## Edit the license agreement

-  
In Apps, select the app you want to view.

-  
In the sidebar, under General, click App Information.

-  
On the left, in the General Information section, click Edit next to License Agreement.

-  
In the dialog that appears, select “Apply a custom EULA to all chosen countries or regions”.

-  
In the Custom License Agreement field, enter your custom EULA as a plain text document.

All HTML tags are stripped and escaped, and only line break characters are accepted.

Tip: To add localized text for your custom EULA, you’ll need to add the localized text for each language within the same text field.

-  
In the Countries or Regions section, select each country or region where you want to apply your custom EULA.

-  
Click Done.

-  
On the top right, click Save.

Related Instructions for Minimum Terms of Developer’s End-User License Agreement Licensed Application End User License Agreement View and edit app information Localize app information App information

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-a-custom-product-page
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit a custom product page 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit a custom product page

Custom product pages, and their associated metadata like deep links, must be reviewed before they’re visible to users on the App Store.

If you want to submit a custom product page and your app hasn’t been approved yet, include the custom product page in the same submission as your first iOS app version. If your app is already approved, you can choose to submit a custom product page with or without an iOS app version. You can also add other items to a submission.

Learn how to submit using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click Custom Product Pages.

-  
Click the page you want to submit for review.

-  
On the top right, click Add for Review and select whether to add the custom product page to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version. The custom product page status changes to Ready for Review.

You may choose to add other items to the submission.

Note: Users with the marketing role can’t add app versions to a submission.

-  
Click Submit for Review. The custom product page status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about item statuses.

You can’t modify a custom product page's screenshots, previews, promotional text, or keywords, while it's under review. Withdrawing the submission makes the page editable, so you can make changes and resubmit.

After an app submission is approved, users can access the custom product page URL.

Related Configure multiple product page versions

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-in-app-event
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit an In-App Event 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit an In-App Event

iOS  
Before publishing your In-App Event on the App Store, submit your event details and media for review, ensuring all required information is complete. If you want to submit an In-App Event and your app hasn’t been approved yet, include the In-App Event in the same submission as your first iOS app version. If your app is already approved, you can choose to submit an In-App Event with or without an iOS app version. You can also add other items to a submission.

You can publish up to 10 In-App Events on the App Store and Apple Games at a time. Additionally, you can have up to 15 approved In-App Events per app in App Store Connect at a time.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
On the top right, click Add for Review and select whether to add the In-App Event to an existing draft submission or create a new submission. Items in the submission will be reviewed together with your latest iOS version. The In-App Event status changes to Ready for Review.

If you’re submitting the In-App Event for review with an app version, it will be reviewed together with that app version.

If you’re submitting the In-App Event for review without an app version, select a platform in the draft submission screen. The In-App Event will be reviewed together with the latest version of the selected platform.

You may choose to add other items to the submission.

Note: Users with the marketing role can’t add app versions to a submission.

-  
Click Submit for Review. The In-App Event status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about item statuses.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-assets-from-asset-library
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit assets from Asset Library 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit assets from Asset Library

If you want to submit an asset and your app doesn't have an approved version, include the asset in the same submission as your first app version. If your app is already approved, you can choose to submit an asset with or without an app version. You can also add other items to a submission.

-  
First app version: If your app doesn’t yet have an approved version, include your assets in the same submission as your first app version.

-  
Subsequent updates: After your app has an approved version, you can submit standalone assets directly from the Asset Library without creating a new app version.

-  
Assets assigned to other items: When you submit an app version, Custom Product Page, Product Page Optimization test, or In-App Event, any assets assigned to it are automatically included in that submission and reviewed together.

-  
Submission restrictions: An asset can’t be submitted on its own through the Asset Library if the item it is assigned to is already part of an active submission.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the Asset Library.

-  
Click Edit at the top right.

-  
Select the assets you want to submit for review.

You can also select the Add for Review link in the Status column.

-  
On the top right, click Add for Review, then select whether to add the asset to an existing draft submission or create a new submission.

If you submit an app version, Custom Product Page, Product Page Optimization test, or In-App Event, any assets assigned to it are reviewed as part of that submission. You can’t submit those assets separately in the Asset Library.

If you're submitting the asset for review without an app version, or your submission includes items associated with multiple platforms, select a platform in the draft submission screen. The asset, and any other items in your submission, are reviewed together with the latest version of the selected platform.

You can also add other items to the submission.

-  
In the Draft Submission pane, click Submit for Review.

Learn how to remove a submission from review.

=== SOURCE: https://developer.apple.com/help/app-store-connect/managing-alternative-distribution/submit-for-notarization
### App Store Connect Help

App Store Connect / Managing alternative distribution / Submit for Notarization 
Filter ⌘K  
Filter ⌘K  

Managing alternative distribution  

# Submit for Notarization

If you’ve set up alternative distribution, you can choose to make your app version eligible only for alternative distribution by selecting to have it evaluated based on the Notarization Review Guidelines (a subset of the App Review Guidelines). Otherwise, App Review uses the App Review Guidelines to evaluate your app version to make it eligible for distribution on the App Store, alternative app marketplaces, and your website (in the EU) if approved. After you've added your app as eligible for distribution on a marketplace in App Store Connect or an alternative distribution domain using the App Store Connect API, follow these steps.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select your app.

-  
In the sidebar, click the app version you want to submit.

-  
Scroll down to the App Review Information section, click Edit under Review Type.

-  
Select “Notarization” and click Save.

Note: The Review Type selection applies to each version individually. If you want to publish a later version through the App Store instead, select App Store in this same step when you submit that version.

-  
On the top right, click “Add for Review”. The app status changes to “Ready for Review”. If you changed any app information, you need to click Continue in the dialog that appears.

-  
Click “Submit to App Review”. The app status changes to “Waiting for Review”. When the review process starts, the app status changes to “In Review”. Learn about the tasks you can do in these statuses.

The app version is accepted, an alternative distribution package automatically generates.

## Required, localizable, and editable properties for Notarization

The tables below show the app and version properties required to submit your app for Notarization. The tables also indicate the properties that you can localize and edit at any time without submitting a new version of your app.

Learn about the required, localizable, and editable properties for App Store distribution.

### App information

Property

Required

Localized

Editable

Name

Subtitle

Rating

Bundle ID

SKU

Content Rights

License Agreement

1       

Primary Language

Primary Category

Secondary Category

Availability in the Republic of Korea2

Availability in China mainland3

4       
1 Custom License Agreement text box can include localized text.

2 Required for developers who enroll as an organization and distribute apps on the App Store in South Korea.

3 Required for apps that meet certain criteria to be available on the App Store in China mainland. Learn about availability requirements.

4 Enter at any time, but submits for review with the next version submission.

#### Platform version information

Property

Required

Localized

Editable

Screenshots

App Preview

Promotional Text

Description

Keywords

Support URL

Marketing URL

Version Number

Copyright

Routing App Coverage File

App Review Information

Version Release settings

What’s New in this Version

Phased Release for Automatic Updates

Reset overview rating

##### App privacy

Property

Required

Localized

Editable

Privacy Policy URL

Privacy Choices URL

Data Types

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events
### App Store Connect Help

App Store Connect / Offer In-App Events 
Filter ⌘K  
Filter ⌘K  

Offer In-App Events  

# Offer In-App Events

iOS  
You can publish up to 10 In-App Events on the App Store and Apple Games at a time. Additionally, you can have up to 15 approved In-App Events per app in App Store Connect at a time.

In-app events must be approved before they are visible to users. Learn how to submit an In-App Event.

Learn how to create a high-quality event.

Learn how to create In-App Event using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Create an In-App Events

-  
In the left sidebar, click In-App Events.

-  
Click Create In-App Event or click the add button (+).

-  
Enter a reference name. This name identifies your event in App Store Connect and is not visible on the App Store and Apple Games. Each name must be unique and can be up to 64 characters long.

-  
Click Create.

### Enter event information

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
Enter an event name to appear on the App Store and Apple Games. It can be up to 30 characters.

-  
Enter a short description to appear on your event card in places like the Today tab and Search on the App Store and Apple Games. It can be up to 50 characters.

-  
Enter a long description that will appear on your event details page when users tap your event card. It can be up to 120 characters.

-  
Upload media for your event card and event details page. Learn about the In-App Event media specifications.

Note: You can also click Browse Assets to use approved, compatible images and videos from Asset Library.

-  
Choose a badge that best fits the type of event you’re offering to display above the title on the event card and event details page.

-  
Add localizations for your event by choosing the primary language to display the language pop-up menu. Learn about localizing app information.

### Select country or region availability

The Country or Region Availability setting controls where your event appears on the App Store and Apple Games. By default, your event is set to appear on all storefronts. However, its visibility is determined by your app’s availability in those regions. You can select the date and time your event first becomes discoverable to users, as well as the date and time the event starts and ends.

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
Scroll down to the Country or Region Availability section.

-  
Select start and end dates and times. You can choose any date in the future for the start date. The end date can be a maximum of 31 days from the start date. Events must be at least 15 minutes long.

Note: You can have up to 10 events with overlapping start dates and times, either approved or in draft status, at the same time.

-  
Select a publish start date and time. The publish date is when your event will become discoverable on the App Store and Apple Games and can be a maximum of 14 days in advance of the start date.

-  
On the top right, click Save.

### Customize event start dates and times

The Customize Dates and Times option allows you to select different start times in one or more countries or regions on the App Store and Apple Games. If you choose to start your event on different days in different locations, all of your event start dates must be within 48 hours of each other.

-  
In the left sidebar, click In-App Events.

-  
Select your event from the list.

-  
In the Country or Region Availability section, click Customize Dates and Times.

-  
Select the locations you want to edit, and click Next.

-  
Enter the start date and time. Use the Time Zone toggle on the top right to choose a timezone.

-  
Click Done.

-  
To customize more regions, click the add button (+) next to Customize Dates and Times.

-  
Select the locations you want to edit, and click Next.

-  
Enter the start date and time.

-  
Click Done.

### Add additional information

-  
Provide an event deep link. This link takes users who tap Open on the In-App Event card or details page to the event content within your app. This can be a universal link (recommended for security) or custom URL. Avoid using URL shorteners and other services that add unnecessary redirects. Test the deep link to make sure it directs to the proper destination within your app — for example, you can paste your URL into the Notes app and tap it. Learn about configuring universal links.

-  
Select the general purpose of your event to help make sure your event reaches the most relevant users on the App Store and Apple Games.

-  
Select the priority for your event. Events appear chronologically on the product page based on start time, with the soonest start time displaying first. If you designate an event as High Priority, it will appear ahead of Normal Priority events.

-  
Indicate if an In-App Purchase is required to participate in the event, as this information is shown on your event details page. For subscription apps, you only need to indicate that an In-App Purchase is required when there’s an additional cost for the event specifically — for example, a pay-per-view event in a subscription app that requires an In-App Purchase in addition to the standard subscription.

-  
Choose your event’s primary language. This will be the default language that displays to users if your event isn’t localized for their device’s language.

Related In-App Event badges In-App Event media and audio specifications Submit an In-App Event

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events
### App Store Connect Help

App Store Connect / Offer In-App Events / Overview of In-App Events 
Filter ⌘K  
Filter ⌘K  

Offer In-App Events  

# Overview of In-App Events

iOS  
In-App Events, such as game competitions, movie premieres, and live-streamed experiences, are timely events within apps and games. Customers can discover these events on the App Store and Apple Games for iOS and iPadOS, providing a new way to showcase and expand their reach.

On iOS 15 and iPadOS 15 and later, In-App Events appear across the App Store as event cards that include images or video, the event name, and a short description. Customers can tap to open an event details page, which provides a more immersive experience with a longer event description. It also includes information about any required In-App Purchases or subscriptions. Customers can opt in on the event card and event details page to receive a notification from the App Store when your event starts.

Customers who don’t have your app or game can download it directly from your In-App Event card or event details page from the App Store. Once downloaded, they can tap Open to be seamlessly directed to the relevant section within your app or game.

In-App Events appear:

-  
On your App Store and Apple Games product page, which displays all of your currently published events.

-  
In App Store and Apple Games search results. When users search for an app, the event card appears along with your app for users who have downloaded your app, while screenshots show for those who haven’t downloaded your app. Users can also search for In-App Events directly. When users search for an event, the event card appears along with your app.

-  
In editorially curated selections and personalized recommendations on the Today, Games, and Apps tabs in the App Store and Apple Games.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

Related In-App Events Get started with app discovery and marketing Submit an In-App Event

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-promo-codes/request-and-manage-promo-codes
### App Store Connect Help

App Store Connect / Offer promo codes / Request and manage promo codes 
Filter ⌘K  
Filter ⌘K  

Offer promo codes  

# Request and manage promo codes

Promo codes offer potential App Store customers or reviewers a free copy of apps on iOS, macOS, or tvOS. These codes can be redeemed on any App Store storefront where your app is available. Each code remains valid for four weeks from its generation date and can be used only once.

You can distribute promo codes by any means. Purchases made using promo codes are indicated in your Sales and Trends reports.

Note: Promo codes can't be generated for apps available only on Apple Business or Apple School Manager. If your app has been removed from sale on all App Store storefronts, promo codes can't be generated or redeemed — even if a version has a Ready for Distribution or Pending Developer Release status.

When a customer downloads an app using a promo code, the app functions as if it were purchased. For example, the customer has the opportunity to update to new versions of the app. However, customers can’t rate or review the app. Promo codes can be used to redeem unreleased versions of apps available on the App Store. Promo codes for tvOS or multi-platform apps must be redeemed on an iOS device. After the code is redeemed, the tvOS app appears in the customer’s purchase history on the App Store for Apple TV. You can request up to 100 promo codes per version of each platform your app supports.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Request promo codes

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Promo Codes. The Promo Code page opens with Generate selected.

-  
Under App Promo Codes, enter the number of version promo codes you want to generate.

-  
On the top right, click Generate Code.

-  
Read and agree to the contract terms for Apple to distribute free versions of your app, and click Generate Code.

-  
Click OK. You can view or download the generated promo codes on the History tab.

### View history of promo codes

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Promo Codes. The Promo Code page opens with Generate selected.

-  
Click History tab.

The history table shows the date each set of codes was generated in App Store Connect. Use this date to determine the expiration date of your codes.

-  
Click View Codes to view or download generated promo codes.

You can copy the codes in the dialog, or click “text file“ to download a .txt file containing the codes.

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-asset-statuses
### App Store Connect Help

App Store Connect / Reference / App information / App Store asset statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# App Store asset statuses

When an asset — such as an app preview, screenshot, or creative asset — is added to the Asset Library, it moves through the following statuses:

Status

What it means

Uploading

The asset is being added to the Asset Library.

Processing

Your uploaded asset is being processed and validated. You can’t take action on the asset until processing completes.

Prepare for Submission

You’ve uploaded an asset to App Store Connect, but haven’t submitted it to App Review. While in this state, the asset is available to browse and select when configuring app versions, Custom Product Pages, Product Page Optimization tests, or In-App Events. You can also delete the asset.

Ready for Review

The asset has been added to a submission, but it hasn't been submitted to App Review yet.

Waiting for Review

Apple received your submission, but hasn't started review.

In Review

App Review is reviewing your submission. You can cancel the submission to remove it from review.

Accepted

This asset has been accepted, but there are one or more rejected items in the submission. All items in the submission must be accepted before any can be published. You can edit the rejected items and resubmit, or you can remove the item from the submission.

Approved

Apple has approved your asset. 

Rejected

App Review didn't accept your asset. You can edit the item and resubmit, or you can remove the item from the submission.

Archived

The asset belonged to a previous app version and has been replaced by a newer one. Archived assets don't appear in the Asset Library by default; use filters to view them.

Related Manage your App Store assets

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications
### App Store Connect Help

App Store Connect / Reference / App information / Creative assets specifications 
Filter ⌘K  
Filter ⌘K  

Reference  

# Creative assets specifications

Creative assets include product page header, search results, and in-app event cards.

Learn more about App Store asset best practices and resources.
Learn how to manage creative assets in App Store Connect.

## Image specifications for product page header and search results

Note: Images can’t include alpha channels or transparencies.

Placement

Aspect ratio

Resolution

Supported extensions

Product page header

21:9

3840 x 1646 pixels

.jpeg, .jpg, or .png

16:9

5244 x 2950 pixels

.png

Search results

3:2

Min: 1920 x 1280 pixels

Max: 3840 x 2560 pixels

.jpeg, .jpg, or .png

16:9

5244 x 2950 pixels

.png

## Video specifications for product page header and search results

Note: Videos are muted by default in search results and can't currently be unmuted. On your product page, videos are also muted by default, but people can unmute them. Videos loop continuously in both placements.

Placement

Aspect ratio

Resolution

Frames per second

Minimum length

Maximum length

Supported extensions

Product page header

21:9

3840 x 1646 pixels

30 fps or 60 fps

5 seconds

30 seconds

.mov, .m4v, or .mp4

Search results

3:2

Min: 1920 x 1280 pixels

Max: 3840 x 2560 pixels

30 fps or 60 fps

5 seconds

30 seconds

.mov, .m4v, or .mp4

## Image specifications for In-App Event cards

Note: Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation. Learn more about In-App Event media and audio specifications.

Placement

Aspect ratio

Resolution

Maximum file size

Supported extensions

In-App Event card

16:9

Min: 1920 x 1080 pixels

Max: 3840 x 2160 pixels

500 MB

.jpeg, .jpg, or .png

In-App Event details page

9:16

Min: 1080 x 1920 pixels

Max: 2160 x 3840 pixels

500 MB

.jpeg, .jpg, or .png

## Video specifications for In-App Event media

Notes: 

-  
Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation. Learn more about In-App Event media and audio specifications.

-  
Videos are muted by default in search results and can't currently be unmuted. On your product page, videos are also muted by default, but people can unmute them. Videos loop continuously in both placements.

Placement

Aspect ratio

Resolution

Frames per second

Minimum length

Maximum length

Supported extensions

In-App Event card

16:9

Min: 1920 x 1080 pixels

Max: 3840 x 2160 pixels

30 fps or 60 fps

15 seconds

30 seconds

.mov, .m4v, or .mp4

In-App Event details page

9:16

Min: 1080 x 1920 pixels

Max: 2160 x 3840 pixels

30 fps or 60 fps

15 seconds

30 seconds

.mov, .m4v, or .mp4

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/in-app-events/in-app-event-media-and-audio-specifications
### App Store Connect Help

App Store Connect / Reference / In-App Events / In-App Event media and audio specifications 
Filter ⌘K  
Filter ⌘K  

Reference  

# In-App Event media and audio specifications

## In-App Event media specifications

Note: Event Card media should appear in landscape orientation and Event Detail media should appear in portrait orientation.

Media Type

Supported Extensions

Aspect Ratio

Min Resolution/Frame Rate

Max Resolution/Frame Rate

Max File Size

Event Card Image

.jpg, .jpeg, .png

16 : 9

1920x1080 px

3840x2160 px

500MB

Event Card Video

.mov, .m4v, .mp4

16 : 9

1920x1080 px 

30 fps or 60 fps

3840x2160 px 

30 fps or 60 fps

500MB

Event Details Page Image

.jpg, .jpeg, .png

9 : 16

1080x1920 px

2160x3840 px

500MB

Event Details Page Video

.mov, .m4v, .mp4

9 : 16

1080x1920 px 

30 fps or 60 fps

2160x3840 px 

30 fps or 60 fps

500MB

### Audio specifications

Audio specifications

Event Card Video:

-  
Stereo

-  
Codec: 256kbps AAC

-  
Sample Rate: 44.1kHz or 48kHz

-  
Tracks without audio are supported

Event Details Page Video:

-  
Stereo

-  
Codec: PCM or 256kbps AAC

-  
Bit Depth (for PCM): 16-, 24-, or 32-bit

-  
Sample Rate: 44.1 or 48kHz

-  
Tracks without audio are supported

Stereo configuration:

-  
1 track with 2-channel stereo (1st channel L and 2nd channel R)

-  
2 tracks with 1-channel stereo (1st track L and 2nd track R)

Stereo configuration:

-  
1 track with 2-channel stereo (1st channel L and 2nd channel R)

-  
2 tracks with 1-channel stereo (1st track L and 2nd track R)

Related Overview of In-App Events In-App Events

