=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/add-imessage-app-information/
### App Store Connect Help

App Store Connect / Create an app record / Add iMessage app information 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Add iMessage app information

You can create sticker packs or iMessage apps using the Messages framework, making them available on the App Store for iMessage. You can create standalone apps or app extensions that exist within a containing iOS app. Learn more about iMessage apps and Stickers.

Create an app record in App Store Connect if your app is an iMessage app, sticker pack, or an extension of one of these. Add details specific to your iMessage app or sticker pack, and submit an app icon and an iMessage app icon.

Learn how to upload iMessage app screenshots using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Add iMessage screenshots

-  
In Apps, select the app you want to view.

-  
In the sidebar, click on the version under the platform you want to edit. Then, scroll down to the iMessage App section. If necessary, click the disclosure triangle to reveal the well.

-  
Drag the screenshots to the well.

### Change iMessage app type

If you want to change the type of iMessage app you offer, you may need to create and submit it as a new app. Currently, you can offer sticker packs or iMessage apps as either:

-  
Standalone apps: the app is only accessible within iMessage.

-  
Extensions to iOS apps: there's a containing iOS app with additional functionality outside of iMessage.

You can rebuild your standalone iMessage app as a standalone sticker pack and vice versa. Similarly, you can rebuild your iMessage extension as a sticker pack extension and vice versa. Submit these updates as version updates to the same app record in App Store Connect. To rebuild your app from a standalone app to an extension of an iOS app or vice versa, you must create it as a new app.

Related View and edit app information App information Required, localizable, and editable properties Upload builds

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/add-platforms/
### App Store Connect Help

App Store Connect / Create an app record / Add platforms 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Add platforms

You can add platforms to an app to create a universal purchase to let customers access your app and in‑app purchases across multiple platforms with a single purchase. For example, you can include the macOS, tvOS, and visionOS versions of your app within an existing iOS app. This distribution model lets customers obtain the iOS, macOS, tvOS, and visionOS together.

Similar to creating a new version, a macOS, tvOS, visionOS app, or any combination of creating these platforms, uses the same Apple ID (an app identifier), SKU, and bundle ID as the iOS app.

iPhone and iPad. To offer your app on iPhone and iPad, your app needs to support both devices.

Apple Watch. To offer your app on iPhone and Apple Watch, create an iOS app in Xcode that includes a watchOS counterpart. Upload both apps to App Store Connect from the same Xcode project. Watch-only apps can’t be part of a universal purchase. Learn how to add watchOS app information.

Mac Catalyst. Apps built with Mac Catalyst using Xcode 11.4 or later can share a bundle ID with the iOS version of the app, supporting universal purchase. You can’t add additional platform versions to apps built with Mac Catalyst using Xcode 11.3 or earlier on the Mac App Store.

Apple Vision Pro. You can't make apps that have been in the Kids category available on visionOS.

Multiple app records. If your app is currently available on multiple platforms through separate app records, note that you can't merge them. To offer universal purchase, remove all but one version from sale, and add the other versions to the remaining app's record. Once you remove an app from sale, you make its original product page on the App Store unavailable, you're no longer able to provide updates to existing users. Ratings and reviews are not transferred to the new product page.

When adding macOS, tvOS, visionOS, or any combination of these platforms, you must upload the builds for macOS, tvOS, and visionOS from a separate Xcode target. In the Xcode project, set the bundle IDs to match the iOS app's bundle ID. However, the apps for macOS, tvOS, and visionOS may each have different version numbers and build strings than the iOS app.

Note: Once App Store Review approves at least two platform versions, your app becomes available as a universal purchase. Once it’s a universal purchase, your app stays as universal purchase—not being able to remove a single platform version from the app record.

Learn about adding a platform using App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Add Platform.

-  
In the Add Platform dialog that appears, choose the platform you want to add, then click Add.

A version for the platform appears selected in the sidebar with the version number 1.0. You can change the version number in the Version section in the sidebar under App Information.

-  
Review and enter metadata for the new platform version.

When you add a platform, metadata from the existing platform version is transferred to the new one, except for the promotional text, description, and screenshots.

Learn more about the platform version information and its required, localizable, and editable properties.

The Account Holder or an administrator can delete a platform if a build has never been uploaded for the specified platform and at least one existing platform version is in an editable app status. To delete a platform, hold the pointer over the platform you want to delete, and then click the delete button (–), which will appear to the right of the platform.

Related Upload builds Choose a build to submit Create a new version Manage App Store assets Add an app icon Creating your product page

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/add-watchos-app-information/
### App Store Connect Help

App Store Connect / Create an app record / Add watchOS app information 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Add watchOS app information

watchOS  
You can create apps for Apple Watch using the watchOS 6 SDK, either as iOS apps with a watchOS app or as watchOS-only apps.

To prepare watchOS apps for distribution on the App Store, add an iOS app to App Store Connect and then include additional information specific to your app.

Ensure your description includes the app's functionality on Apple Watch. Provide screenshots of Apple Watch and an app icon. App Review reviews your screenshots and icon after you submit your new app version.

Learn how to prepare watchOS metadata for app submission.

Learn about the Human Interface Guidelines on creating your app icon.

Learn more about uploading your app icon.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Add watchOS app information

-  
In Apps, click the add button (+) on the top left.

-  
In the pop-up menu, select New App.

-  
In the New App dialog, select iOS on the top left, then enter your app information.

-  
Click Create, then select the Apple Watch tab under Previews and Screenshots.

-  
Drag Apple Watch screenshots for Apple Watch to the well.

Note: iOS screenshots are also required for apps with an iOS component, but not for watch-only apps.

Related Screenshot specifications Learn how to prepare watchOS app metadata for submission. Learn how to upload your app icon. Learn how to upload watchOS app screenshots with the App Store Connect API.

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/app-sandbox-information/
### App Store Connect Help

App Store Connect / Reference / App uploads / App Sandbox information  
Filter ⌘K  
Filter ⌘K  

Reference  

# App Sandbox information

macOS  
If you use App Sandbox entitlements, Apple needs information on each temporary exception entitlement included in the app. You add a temporary exception entitlement by editing the .entitlements property list file in the Xcode project. For more information, visit App Sandbox Design Guide.

Property

Description

Entitlement Key

The entitlement key that corresponds to a temporary exception entitlement implemented in the app.

Usage Information

Information describing how to assess the entitlement and a description of the values in an array value used by the entitlement. If the entitlement works around a missing App Sandbox feature, file a bug report describing the exception using Feedback Assistant and include the bug ID in the usage information.

The description should include:

-  
How the entitlement can be assessed

-  
Why the entitlement is needed by the app

-  
What functionality this entitlement enables

-  
If the entitlement uses an array value, provide information on each value in the array

-  
If the entitlement works around a missing App Sandbox feature, the ID of the bug you filed describing the exception

Related App Sandbox Design Guide

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/apple-hosted-asset-pack-size-limits/
### App Store Connect Help

App Store Connect / Reference / App uploads / Apple-hosted asset pack size limits 
Filter ⌘K  
Filter ⌘K  

Reference  

# Apple-hosted asset pack size limits

There are limits on the amount of storage used by Apple-hosted asset packs when you upload to App Store Connect. The table below outlines the different size limits for these asset packs. These limits are shared across all platforms offered for your app.

You can make additional space available by archiving asset packs. This removes all versions of an asset pack from App Store Connect, including those being tested in TestFlight and live on the App Store. Learn more.

Your App Store product page shows an “Up to” app size that includes any non-localized essential asset packs and the localized essential asset packs for the single language with the largest total size. Learn more about build file sizes.

Item

Size limit description

Size limit

Asset pack total

The total sum of size usage for all asset packs uploaded to an app record in App Store Connect.

For each asset pack in App Store Connect, Apple calculates the maximum size over all versions that are eligible to be tested in TestFlight or submitted for App Store distribution. This calculation doesn’t include versions that have the Awaiting Upload, Processing, or Failed TestFlight status, nor those that have the Superseded status for both TestFlight and the App Store. Then, the maximum size of each asset pack is added together to reach the asset pack total.

For example, AssetPackID1 has two versions: version 1 is 4 GB, and version 2 is 2 GB. AssetPackID2 has one version: version 1 is 1 GB. The asset pack total for this app is 5 GB, since the maximum size for AssetPackID1 is 4 GB and the maximum size for AssetPackID2 is 1 GB.

If you upload a new asset pack version and reach 80% or more of the asset pack total limit, you'll be notified via email. A banner will also display on the asset pack page in the TestFlight section of App Store Connect.

200 GB

Asset pack count

The total number of asset packs that are allowed to be uploaded to an app record in App Store Connect.

200

Related Overview of Apple-hosted asset packs Upload Apple-hosted asset packs Downloading asset packs hosted by Apple

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/create-and-submit-app-bundles/
### App Store Connect Help

App Store Connect / Create an app record / Create and submit app bundles 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Create and submit app bundles

You can offer apps, including those part of a universal purchase, as an app bundle on the App Store. App bundles simplify the process for you, letting you group up to ten of your apps together in a single download.

Apps in a bundle must follow these guidelines:

-  
All apps must be either all paid or all free.

-  
A paid app bundle can only include paid apps and must be offered at a reduced price.

-  
You must ensure that each app in a free app bundle is free and offers an auto-renewable subscription. The subscription must allow the user to subscribe to and access content or services in all apps included in the bundle.

-  
Apps that support tvOS only or visionOS only can’t be part of a bundle.

Note: For app bundles created before February 17, 2026, each app in the bundle must support at least one of the same platforms as the first app you add, known as the primary app. For bundles created after the date, apps included in the bundle don’t need to support the same platform as the primary app.

Customers purchase the bundle with a single tap or click, and the individual apps install automatically on their device. Customers who have previously bought one or more apps in an app bundle can use the Complete My Bundle feature. The bundle price adjusts to reflect their existing purchases.

Learn how to set up app bundles and effectively market them on your App Store product page.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Create an app bundle

-  
In Apps, click the add button (+) and select New App Bundle.

-  
In the Name field, enter a unique name for the app bundle.

-  
Under Apps in This Bundle, hold the pointer over the app you want to add to the bundle, and click the add button (+).

You can add an app to a bundle if it’s in the Ready for Distribution state. The first app you choose to include in the bundle becomes the primary app. Certain aspects of the app bundle information is determined based on the primary app.

-  
On the top right, click Create.

Later, the app bundle appears on your Apps page.

-  
Under Bundle Information, enter the required app bundle information, then click Save.

### Submit an app bundle for review

-  
In Apps, select the app bundle you want to view.

-  
On the top right, click Submit for Review.

The app bundle status changes to Waiting for Review. When the review process starts, the app status changes to In Review. After the app bundle is approved, you can no longer add or remove apps from the bundle.

### Remove an app bundle from review

-  
In Apps, select the app bundle you want to remove.

-  
On the top right, click Remove from Review.

This action will remove the app bundle from Apple's review queue, and the app status will change to Developer Rejected.

Related Edit app bundle information App bundle information

=== SOURCE: https://developer.apple.com/help/app-store-connect/
### App Store Connect Help

App Store Connect 
Filter ⌘K  
Filter ⌘K  

# App Store Connect Help

Learn about managing your App Store Connect account.

## Get started

App Store Connect workflow 
Use App Store Connect to submit apps for distribution, manage your apps, distribute beta versions of your apps using TestFlight, accept legal agreements, enter tax and banking information, view trends and financial reports, and more. The App Store Connect API is also available for you to automate your workflow.
Overview of accounts and roles 
Learn how to manage users, add Sandbox testers, manage API keys, and manage access to the source code for Xcode Cloud in App Store Connect.
Upload builds 
After you add an app to your account, you can upload a build with Xcode, Swift Playgrounds, or Transporter for macOS. If you use the App Store Connect API you might want to upload your binary using the Transporter command-line tool and JSON Web Tokens (JWTs) authentication. You can use the same JWTs you use for the API to upload your binary. You can upload more builds as your app changes, distribute a build for testing, or submit your app for review.

## Popular

Screenshot specifications 
Screenshot sizes for Apple Devices in App Store Connect.
Set an app age rating 
Learn how to set an app age rating in App Store Connect to help users understand the type of content in your app.
Overview of Accessibility Nutrition Labels 
Get an overview of Accessibility Nutrition Labels.

## Additional resources

- Documentation

- App Store Connect API

- Developer Account Help

- Videos

- Forums

## Need additional help?

If you have questions about membership, your account, or app management, contact support.

=== SOURCE: https://developer.apple.com/help/app-store-connect/configure-game-center/manage-an-app-version-for-game-center/
### App Store Connect Help

App Store Connect / Configure Game Center / Manage an app version for Game Center 
Filter ⌘K  
Filter ⌘K  

Configure Game Center  

# Manage an app version for Game Center

Apps offering Game Center features need to include the Game Center entitlement in the entitlements plist and have Game Center features configured in App Store Connect before they can be submitted for review.

You can enable or disable Game Center for your app at the version level. Once an app version is approved with Game Center enabled, Game Center can’t be disabled for that version. Instead, you’ll need to disable Game Center when submitting an updated app version.

Note: Games distributed via alternative distribution will need to also be available on at least one App Store storefront to take advantage of Game Center functionality.

Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.

## Enable app version for Game Center

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version you want to enable for Game Center.

-  
Scroll down and select the checkbox next to Game Center.
Learn how to submit Game Center components with the app version for review. 

### Disable app version for Game Center

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version under your desired platform, then navigate to the Game Center section.

-  
Deselect the Game Center checkbox to disable Game Center for the version.

Related Game Center properties Overview of submitting for review Enabling and configuring Game Center

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-a-default-app-clip-experience/
### App Store Connect Help

App Store Connect / Offer App Clip experiences / Offer a default App Clip experience 
Filter ⌘K  
Filter ⌘K  

Offer App Clip experiences  

# Offer a default App Clip experience

A default App Clip experience is required and can be invoked using Safari and Messages, as well as through an NFC tag, QR code, and links in other apps when using an Apple-provided App Clip link. Learn about configuration options.

Note: People can launch your App Clip from other apps on iOS 17 or later.

A default App Clip link is optional, but useful for App Clips that only require a single App Clip experience. This link allows you to invoke the default App Clip experience on devices running iOS 16.4 or later.

When you upload a build that has an App Clip and configure a default App Clip experience, a default App Clip link and App Clip demo URL are automatically generated in App Store Connect.

Default App Clip link

https://appclip.apple.com/id?p=app_clip_bundle_id&key=value

Default App Clip demo URL

https://apps.apple.com/id?p=app-clip-bundle-id-=value

These will become active once your version has been approved.

Once you create a default App Clip experience, you can create advanced App Clip experiences.

Learn how to create a default App Clip experience using the App Store Connect API.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the iOS app version for which you want to add an App Clip experience and scroll down to the App Clip section.

-  
Enter a header image, subtitle, and action. This metadata appears on the App Clip card when the experience is invoked from Safari or Messages.

Learn more about the required, localizable, and editable properties.

Note: You must provide a header image with the following specifications:

-  
Supported extensions: .jpg, .jpeg, .png

-  
Aspect ratio: 3 : 2

-  
Resolutions: 1800 x 1200 pixels

-  
On the top right, click Save.

Related Watch WWDC23 What’s new in App Clips Design > App Clips App Clips framework Maximum build file sizes Choosing the right functionality for your App Clip Creating an App Clip with Xcode

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-an-advanced-app-clip-experience/
### App Store Connect Help

App Store Connect / Offer App Clip experiences / Offer an advanced App Clip experience 
Filter ⌘K  
Filter ⌘K  

Offer App Clip experiences  

# Offer an advanced App Clip experience

Learn how to create an advanced App Clip experience using the App Store Connect API.

## Set up an advanced App Clip experience without place association

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the iOS app version for which you want to add an App Clip experience.

-  
Under Advanced App Clip Experiences, click Edit Advanced Experiences. A new page opens with general information on what to provide.

-  
Click Next.

-  
In the App Clip experience URL field, enter the invocation URL for your App Clip experience.

The App Clip Bundle ID will be prepopulated.

-  
Click Next.

-  
Enter the information for the App Clip card. To add a Default Display Title and Default Subtitle in additional languages, click Add Additional Titles.

-  
Specify that your App Clip experience isn’t associated with a place.

View tooltips next to each field for more details.

-  
Select a call to action, then click Next.

-  
Answer the question about what this App Clip experience promotes. Specify whether it promotes your app’s business, service, or brand or if it’s created on behalf of other businesses, services, or brands that appear within your app.

Learn about creating App Clips for other businesses.

-  
Click Send to Apple.

All the experiences you’ve configured, along with their statuses, will display on the App Clip experiences page.

### Set up an advanced App Clip experience with place association

Connecting your App Clip to a physical location is optional through a place association. This feature is necessary for launching the App Clip experience via Apple Maps. Place association doesn’t guarantee inclusion in Apple Maps and may not be available in all countries and regions.

If your App Clip is part of the location’s official app, it’ll be automatically approved for that location. If it’s not part of the official app, either the business owner must claim the location through Apple Business Connect and approve the App Clip to display, or the creator of the App Clip must be authorized as a partner on the business’ website.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the iOS app version for which you want to add an App Clip experience.

-  
Under Advanced App Clip Experiences, click Edit Advanced Experiences. A new page opens with general information on what to provide.

-  
Click Next.

-  
In the App Clip experience URL field, enter the invocation URL.

The App Clip Bundle ID will be prepopulated.

-  
Click Next.

-  
Enter the information for the App Clip card. To add a Default Display Title and Default Subtitle in additional languages, click Add Additional Titles.

-  
Specify that your App Clip experience is associated with a place.

View tooltips next to each field for more details.

-  
Select a Maps action that best fits the experience and click Next. This determines the action that appears on the place card in Maps.

-  
Choose a place to associate with this App Clip experience.

-  
Answer the question about the relationship between your app and the place associated with this App Clip experience.

-  
Answer the question about what this App Clip experience promotes. Specify whether it promotes your app’s business, service, or brand, or if it’s created on behalf of other businesses, services, or brands that appear within your app.

Learn about creating App Clips for other businesses.

-  
If your App Clip experience promotes another business, service, or brand, select a category.

-  
Click Send to Apple.

All the experiences you’ve configured, along with their statuses, will display on the App Clip experiences page.

Note: To confirm that your App Clip experience appears in Maps, open Maps and search for places associated with the experience.

Related Maximum build file sizes Choosing the right functionality for your App Clip Creating an App Clip with Xcode

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/on-demand-resources-size-limits/
### App Store Connect Help

App Store Connect / Reference / App uploads / On-demand resources size limit 
Filter ⌘K  
Filter ⌘K  

Reference  

# On-Demand Resources size limits

On-Demand Resources are app contents that are hosted on the App Store and are separate from the related app bundle that you download. They enable smaller app bundle, faster downloads, and richer app content.

Note: On-Demand Resources are deprecated on Apple platforms as of iOS 27, iPadOS 27, tvOS 27, and visionOS 27, and support will be removed in future releases. Migrating to Background Assets is recommended.

There are limits on the amount of storage used by On-Demand Resources when you upload your app to App Store Connect or while the app is running.

Note: macOS and watchOS don't support On-Demand Resources.

## On-Demand Resource sizes

The table below outlines the variant size limits for each deployment target after app thinning. For example, the total size limit of each asset pack is 8GB after thinning for apps available on devices running iOS 18 and later.

### On-Demand Resource size limits for iOS and iPadOS apps

Item

Size limit description

Earlier than iOS 18 or earlier than iPadOS 18

iOS 18 or iPadOS 18, or later

App bundle

The size of the thinned app bundle downloaded to the device.

2 GB

4 GB

Asset pack

The size of each thinned asset pack. Asset packs are generated by Xcode when your app is built. One tag may result in multiple asset packs.

512 MB

8 GB

Asset pack count

The total number of asset packs generated by Xcode.

1000

1000

Initial install and prefetched tags

The total size of the thinned asset packs marked with initial install and prefetched tags.

4 GB

No limit

In use On-Demand Resources

The total size of the resources with the tags in use by the app at any one time. A tag is in use as long as at least one NSBundleResourceRequest is accessing it.

2 GB

No limit

Hosted On-Demand Resources

The total size of the thinned asset packs hosted on the App Store.

20 GB

70 GB

### On-Demand Resource size limits for tvOS apps

Item

Size limit description

Earlier than tvOS 18

tvOS 18 or later

App bundle

The size of the thinned app bundle downloaded to the device.

4 GB

4 GB

Asset pack

The size of each thinned asset pack. Asset packs are generated by Xcode when your app is built. One tag may result in multiple asset packs.

512 MB

512 MB

Asset pack count

The total number of asset packs generated by Xcode.

1000

1000

Initial install and prefetched tags

The total size of the thinned asset packs marked with initial install and prefetched tags.

4 GB

4 GB

In use On-Demand Resources

The total size of the resources with the tags in use by the app at any one time. A tag is in use as long as at least one NSBundleResourceRequest is accessing it.

2 GB

No limit

Hosted On-Demand Resources

The total size of the thinned asset packs hosted on the App Store.

20 GB

20 GB

### On-Demand Resource size limits for visionOS apps

Item

Size limit description

Earlier than visionOS 2

visionOS 2 or later

App bundle

The size of the thinned app bundle downloaded to the device.

4 GB

4 GB

Asset pack

The size of each thinned asset pack. Asset packs are generated by Xcode when your app is built. One tag may result in multiple asset packs.

512 MB

8 GB

Asset pack count

The total number of asset packs generated by Xcode.

1000

1000

Initial install and prefetched tags

The total size of the thinned asset packs marked with initial install and prefetched tags.

4 GB

No limit

In use On-Demand Resources

The total size of the resources with the tags in use by the app at any one time. A tag is in use as long as at least one NSBundleResourceRequest is accessing it.

2 GB

No limit

Hosted On-Demand Resources

The total size of the thinned asset packs hosted on the App Store.

20 GB

70 GB

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/overview-of-app-clips/
### App Store Connect Help

App Store Connect / Offer App Clip experiences / Overview of App Clips 
Filter ⌘K  
Filter ⌘K  

Offer App Clip experiences  

# Overview of App Clips

An App Clip is a small part of your app that’s discoverable at the moment it’s needed and lets people quickly start and finish a task from your app. Users running iOS 14 or later can quickly access App Clips without needing to download the full app. Learn about App Clips.

Note: App Clips are subject to the same age restrictions and parental controls as full apps. However, App Clips aren’t available to children under 13 or those with Ask to Buy enabled, regardless of other restrictions and settings. To access all of an app’s features, such as those normally offered through App Clip codes and QR codes, these users must install the full app.

You can configure how your App Clip is discovered and launched by creating App Clip experiences. Each experience includes metadata for the App Clip card, an invocation URL, and various invocation methods. You can create many App Clip experiences to support situations when different tasks from your app might be helpful.

A default App Clip experience is required and can be invoked using Safari and Messages, as well as through an NFC tag, QR code, and links in other apps when using an Apple-provided App Clip link.

You can also create advanced App Clip experiences, which let you configure your App Clip to use multiple domains, associate your App Clip with physical locations, and customize multiple App Clip cards to represent different businesses with a single App Clip. Learn about configuration options.

When you’re ready to submit your app for review to distribute on the App Store, you can optionally provide up to three URLs that are representative of experiences your App Clip provides, allowing App Review to understand the features and functionalities. Add these URLs in the App Clips URLs section in App Review Information toward the bottom of the Version Information page.

To edit the App Clip section in App Store Connect, you must first upload a build that includes an App Clip. Ensure that each subsequent app version you submit includes the App Clip to maintain its availability for users.

Learn how to read App Clip information and manage App Clip experiences using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

Related Maximum build file sizes Choosing the right functionality for your App Clip Creating an App Clip with Xcode

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-asset-packs/overview-of-apple-hosted-asset-packs/
### App Store Connect Help

App Store Connect / Manage asset packs / Overview of Apple-hosted asset packs 
Filter ⌘K  
Filter ⌘K  

Manage asset packs  

# Overview of Apple-hosted asset packs

The Background Assets framework allows you to schedule background downloads of additional content using your server or content delivery network (CDN). Apps targeting iOS 26, iPadOS 26, macOS 26, tvOS 26, and visionOS 26 and later can use Managed Background Assets. With Managed Background Assets, the system automatically manages downloads, updates, and compression for your assets. Additionally, apps distributed through TestFlight and the App Store can use Apple-Hosted Background Assets, and Apple will host the content on your behalf.

Assets for Managed Background Assets are managed through asset packs that you configure using a command-line packaging tool in Xcode, or the Managed Background Assets Developer Tools for Linux. Users’ devices automatically download these asset packs separately from your app build. When you use Apple hosting, you can also upload asset packs to App Store Connect separately from your app build.

Learn how to create, download, and locally test Apple-hosted asset packs.

After you upload an asset pack to App Store Connect, you can test it using TestFlight, and submit it for distribution on the App Store.

## Localized asset packs

Starting with iOS 27, iPadOS 27, macOS 27, tvOS 27, and visionOS 27, you can use Managed Background Assets to distribute localized assets separately from your app build. Include localized assets in separate asset packs for each language, and users automatically receive the appropriate asset pack based on their system settings, or app language preferences when available.

Note: Devices running earlier OS versions won’t receive localized asset packs.

You can associate each asset pack version with one language in the manifest file. The language must be a valid BCP-47 identifier and can contain language, script, and region subtags (for example, “zh-Hans-CN” or “en-US”). You can change the associated language from version to version, and you can associate a language with multiple asset pack versions.

Note: Creating and testing localized asset packs isn’t supported in the Managed Background Assets Developer Tools for Linux. Use the packaging tool in Xcode instead.

If no localized asset packs match a user’s language settings, the system uses the asset pack in the next most relevant language, such as other regional variations of the language or the app’s primary language.

Related Watch “Discover Apple-Hosted Background Assets” Apple-hosted asset pack statuses Apple-hosted asset pack size limits

=== SOURCE: https://developer.apple.com/help/app-store-connect/configure-game-center/overview-of-game-center/
### App Store Connect Help

App Store Connect / Configure Game Center / Overview of Game Center 
Filter ⌘K  
Filter ⌘K  

Configure Game Center  

# Overview of Game Center

Game Center is Apple’s social gaming network that lets players track their progress, invite friends to play, start multiplayer games through auto-match, and more. It also boosts the discovery of your games across players’ devices. Once you’ve implemented Game Center features, you’re ready to enter related metadata in App Store Connect.

Note: To add a game with Game Center features to a new app bundle, the game must be “Ready for Distribution" on at least one App Store storefront. For games distributed through alternative distribution, availability on at least one App Store storefront is required to utilize Game Center functionality.

You can complete the steps below in the order they're listed or move between steps as needed.

Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.

-  
Enable Game Center in Xcode.

In Xcode, create your project, enter an app name and bundle ID, then enable Game Center, which adds the GameKit framework and Game Center Entitlement to your project. Learn more about enabling Game Center in Xcode.

-  
Configure Game Center in App Store Connect.

In App Store Connect, add an app to your account that matches the bundle ID in Xcode, enable your app version for Game Center, and configure Game Center components, such as leaderboards, achievements, challenges, activities, groups, and multiplayer compatibility.

-  
Implement Game Center features.

To integrate Game Center into your app using Xcode, add the necessary code and configure the service's components. Although these components are set up independently from your app bundle, they must be closely integrated with your game's code to fulfill all design and development requirements. Learn more.

Learn the guidance and best practices that can help you design a great experience for Game Center.

-  
Test your game.

Ensure that your Game Center components work individually and together. Apple enables all prerelease development to take place in the same server environment as released games, so you can play with the full player base, not just other testers.

-  
Distribute your game.

Add your Game Center components to your desired platform version before submitting your game for review.

Related Game Center Games Use Game Center to boost discovery and engagement

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/provide-app-motion-information/
### App Store Connect Help

App Store Connect / Reference / App information / Provide app motion information 
Filter ⌘K  
Filter ⌘K  

Reference  

# Provide app motion information

App motion is a required app information property for all visionOS apps on the App Store. This information displays on your app’s product page on the App Store to inform users who may be sensitive to apps with high motion.

There are two possible values for this property:

Value

Definition

Yes, this app contains high motion

Has frequent fast or sudden camera movements, quick turns, or unusual orientations.

No, this app doesn't contain high motion

Doesn't have frequent fast or sudden camera movements, quick turns, or unusual orientations.

## About app motion

On Apple Vision Pro, the user’s viewpoint acts as a virtual camera and moves with the motion of their head and body. In some experiences, the virtual camera moves without the user moving their head or body (either controlled by the user through hand gestures or input devices, or scripted by the app without user input).

### When to choose “No, this app doesn’t contain high motion”

If the virtual camera in your app doesn’t move without the user moving their head or body, choose “No, this app doesn’t contain high motion.” You won't need to assess your app further.

#### When to assess your app for high motion

If the virtual camera in your app moves without the user moving their head or body, you might need to choose “Yes, this app contains high motion.” To find out, follow the guidance below to assess your app experience for:

-  
Fast forward or backward motion

-  
Unusual orientations

-  
Fast rotation speeds

-  
Unexpected motion

Keep the following in mind:

-  
Assess only the motion of the user’s viewpoint as a virtual camera, not the motion of a user-controlled character or vehicle. This distinction is especially important when the motion of the virtual camera is different than the motion of a controlled character or vehicle.

-  
If your app has multiple configuration options that affect the motion experience, use the default configuration to assess the experience.

-  
Rate the average motion in your app. If there’s only a brief moment of high motion at a few points in your app and the rest contains no motion, you don’t need to indicate high motion in your app.

-  
If your app consists of several different first-party experiences that are intended by design to be part of the core app experience, consider the average motion across all of them and whether the average contains high motion.

-  
Apps that host a variety of third-party content (like user-uploaded videos or HTML5 games) shouldn’t have a high motion label, unless the app’s intent is to have lots of content with high motion (like user uploads of their first-person thrill-seeking experiences).

#### Elements to assess

### Fast forward or backward motion

Combinations of forward or backward virtual camera motion can lead to very high pixel speeds.

Example 1 demonstrates the pixel speed when the camera moves forward quickly, with objects close by, resulting in high motion. The red arrows indicate the objects’ pixel speed in the scene.

Example 2 shows a much slower pixel speed that doesn’t fall under the category of high motion. This can be produced by moving objects farther away or with slower camera motion.

Choose “Yes, this app contains high motion” if the combination of forward or backward virtual camera speed and object distance in your app produces a pixel speed similar to or higher than that shown in Example 1.

Example 1: High pixel speed

Example 2: Low pixel speed

### Unusual orientations

When the horizon of the virtual world doesn't match the real world, users may experience discomfort. The virtual camera rolls left or right around its longitudinal axis or pitches up or down in situations like these.

Choose “Yes, this app contains high motion” if the virtual camera rolls around its longitudinal axis or pitches up or down more than 10 degrees, with less than 5 minutes between each instance. This includes loops, steep banks or slopes, and upside-down motion.

### Fast rotation speeds

Users can also experience discomfort when they experience fast camera rotation speeds around their vertical axis (yaw).

Choose “Yes, this app contains high motion” if the virtual camera yaws left or right smoothly, while simultaneously moving forward or backward at speeds equal to or slower than running. This includes user-controlled and scripted smooth camera turns in first-person-view experiences.

### Unexpected motion

Choose “Yes, this app contains high motion” if the virtual camera makes unexpected and/or unpredictable motions with less than 5 minutes between each instance. This includes falls, turns, spins, and other orientation changes.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/set-the-app-motion-information-for-apple-vision-pro/
### App Store Connect Help

App Store Connect / Manage app information / Set the app motion information for Apple Vision Pro 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Set the app motion information for Apple Vision Pro

All visionOS apps on the App Store must include the app motion information as a required property within their app information. If your app includes experiences with high motion, users will be informed through a label displayed on your app's product page.

Learn how to assess your app for high motion.

Note: You’ll need to set this information in order to submit your visionOS app for review.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version under the visionOS app platform.

-  
Below App Motion Information, click Set Up.

-  
In the dialog that appears, select either “Yes, this app contains high motion” or “No, this app doesn’t contain high motion”.

-  
Click Save.

Note: To update this information at any time, click Edit next to Contains High Motion. The change reflects on the App Store immediately.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-apple-hosted-asset-packs/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit Apple-hosted asset packs 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit Apple-hosted asset packs

Asset packs must be reviewed before they can be tested externally in TestFlight or made available for users on the App Store. Learn about submitting asset packs for external testing.

Once an asset pack version is approved for the App Store, it’ll automatically be available to all App Store users, and any previous versions of the asset pack will be replaced with the new one.

If your app hasn’t been approved yet and you want to submit an asset pack version, include the asset pack version in the same submission as your first app version. After your app is approved, you can submit an asset pack version with or without an app version. However, if a new app version requires a new asset pack to function, include a version of that asset pack in the same submission as the new app version. You can also add other items to a submission, such as In-App Events.

You can include up to ten different asset packs in a submission, with one version of each asset pack permitted at a time.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under General, click Asset Packs.

If you haven’t uploaded any asset packs yet, the Asset Packs section won’t appear.

-  
On the right, find the asset pack ID with the version you want to submit.

-  
If this is the first version you're submitting for the App Store, click Select Asset Pack Version. If you already have a version available on the App Store, click Replace.

Note: Asset pack versions that are packaged using a beta Managed Background Assets packaging tool can’t be added for review.

-  
Select the asset pack version you want to submit to App Review. 

-  
Click Add for Review, then select whether to add the asset pack version to an existing draft submission or create a new submission. The asset pack version’s status changes to Ready for Review.

If you’re submitting the asset pack for review with an app version, it will be reviewed together with that app version.

If you’re submitting the asset pack for review without an app version, or your submission includes items associated with multiple platforms, select a platform in the draft submission screen. The asset pack version, and any other items in your submission, will be reviewed together with the latest version of the selected platform.

You may choose to add other items to the submission.

-  
Click Submit for Review. The asset pack version’s status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about Apple-hosted asset pack statuses.

Related Overview of Apple-hosted asset packs Upload Apple-hosted asset packs Test Apple-hosted asset packs

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-game-center-components/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit Game Center components 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit Game Center components

New or modified leaderboards, leaderboard sets, achievements, challenges, and activities must be reviewed before they can be made available to players through Game Center.

Include components in the same submission as your app version if this is the first time you're adding them to an app. For subsequent components, you can submit them without an app version.

Game Center components submitted without an app version are reviewed against the latest platform version specified during submission. You can also include other items with these submissions. Get an overview of submitting an app or items for review.

Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.

## Submit Game Center components for review

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Game Center.

-  
Select a Game Center component you want to submit to App Review. For example, a leaderboard.

-  
On the top right, click Add for Review and select whether to add the component to an existing draft submission or create a new submission.

If you’re submitting the component for review with an app version, it’ll be reviewed together with the app version. If you’re submitting it for review without an app version, it’ll be reviewed against the latest version of the selected platform. You can switch the platform in the draft submission screen.

Note: You can include up to 200 different components in a submission. Learn how many leaderboards, leaderboard sets, achievements, challenges, and activities you can create.

-  
Click Submit for Review.

The component’s status changes to Waiting for Review. When the review process starts, the status changes to In Review.

### Remove a Game Center component from draft submission

You can remove the component in Ready for Review status from the draft submission. For submitted Game Center component, you can cancel your submission from review if it’s in Waiting for Review or In Review status. 

-  
In Apps, select the app you want to view.

-  
In the bottom-right corner of the screen, click Draft Submissions, then select the submission you want to remove a component from.

-  
Hover over the component you want to remove, then click the red delete button (-). The component status changes to Developer Rejected.

You can also remove a component from the submission in the Game Center section. In the Game Center section, select the Game Center component you want to remove from review, then click "Remove from Review" in the message that appears at the top. Similarly, you can remove a submission from the App Review section. Learn more.

Related Overview of submitting for review

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/test-an-app-clip-experience/
### App Store Connect Help

App Store Connect / Test a beta version / Test an App Clip experience 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Test an App Clip experience

App Clips allow you to make a small part of your app discoverable and quick to launch at the moment it’s needed. You can add up to three invocation URLs to launch different experiences within your App Clip. Testers running TestFlight for iOS, version 2.7 or later, and iOS 14 beta or later can test and provide feedback on all available App Clip experiences. Currently, testing of other invocation methods is not supported. Learn more about testing your App Clip’s launch experience.

Learn how to view tester feedback.

Learn how to manage App Clip experiences for testers with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Add an App Clip invocation

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, below Builds, click the iOS platform.

-  
In the Builds column, click the app icon or build string for the build that has the App Clip you'd like to test. The page opens with the Test Information tab selected.

-  
Under App Clip Invocations, click Add App Clip Invocation.

-  
In the dialog that appears, enter the title and URL for your App Clip invocation.

Note: You can localize the App Clip title for each URL based on the localizations you have added for your build in TestFlight, but the URL will be the same across localizations.

-  
Click Add.

-  
On the top right of the page, click Save.

Note: You can test an App Clip experience using TestFlight, provided that the App Clip is included in the build. To create defined experiences, incorporate up to three invocation URLs.

### Delete an App Clip invocation

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under Builds, click the iOS platform.

-  
In the Build column, click the app icon or build string for the build that has the App Clip invocation you'd like to delete. The page opens with Test Information tab selected.

-  
Under App Clip Invocations, hold the pointer over the App Clip invocation and click the delete button (–) that appears to the right of the URL.

-  
In the dialog that appears, click Delete.

-  
On the top right of the page, click Save.

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/add-imessage-app-information
### App Store Connect Help

App Store Connect / Create an app record / Add iMessage app information 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Add iMessage app information

You can create sticker packs or iMessage apps using the Messages framework, making them available on the App Store for iMessage. You can create standalone apps or app extensions that exist within a containing iOS app. Learn more about iMessage apps and Stickers.

Create an app record in App Store Connect if your app is an iMessage app, sticker pack, or an extension of one of these. Add details specific to your iMessage app or sticker pack, and submit an app icon and an iMessage app icon.

Learn how to upload iMessage app screenshots using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Add iMessage screenshots

-  
In Apps, select the app you want to view.

-  
In the sidebar, click on the version under the platform you want to edit. Then, scroll down to the iMessage App section. If necessary, click the disclosure triangle to reveal the well.

-  
Drag the screenshots to the well.

### Change iMessage app type

If you want to change the type of iMessage app you offer, you may need to create and submit it as a new app. Currently, you can offer sticker packs or iMessage apps as either:

-  
Standalone apps: the app is only accessible within iMessage.

-  
Extensions to iOS apps: there's a containing iOS app with additional functionality outside of iMessage.

You can rebuild your standalone iMessage app as a standalone sticker pack and vice versa. Similarly, you can rebuild your iMessage extension as a sticker pack extension and vice versa. Submit these updates as version updates to the same app record in App Store Connect. To rebuild your app from a standalone app to an extension of an iOS app or vice versa, you must create it as a new app.

Related View and edit app information App information Required, localizable, and editable properties Upload builds

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/add-platforms
### App Store Connect Help

App Store Connect / Create an app record / Add platforms 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Add platforms

You can add platforms to an app to create a universal purchase to let customers access your app and in‑app purchases across multiple platforms with a single purchase. For example, you can include the macOS, tvOS, and visionOS versions of your app within an existing iOS app. This distribution model lets customers obtain the iOS, macOS, tvOS, and visionOS together.

Similar to creating a new version, a macOS, tvOS, visionOS app, or any combination of creating these platforms, uses the same Apple ID (an app identifier), SKU, and bundle ID as the iOS app.

iPhone and iPad. To offer your app on iPhone and iPad, your app needs to support both devices.

Apple Watch. To offer your app on iPhone and Apple Watch, create an iOS app in Xcode that includes a watchOS counterpart. Upload both apps to App Store Connect from the same Xcode project. Watch-only apps can’t be part of a universal purchase. Learn how to add watchOS app information.

Mac Catalyst. Apps built with Mac Catalyst using Xcode 11.4 or later can share a bundle ID with the iOS version of the app, supporting universal purchase. You can’t add additional platform versions to apps built with Mac Catalyst using Xcode 11.3 or earlier on the Mac App Store.

Apple Vision Pro. You can't make apps that have been in the Kids category available on visionOS.

Multiple app records. If your app is currently available on multiple platforms through separate app records, note that you can't merge them. To offer universal purchase, remove all but one version from sale, and add the other versions to the remaining app's record. Once you remove an app from sale, you make its original product page on the App Store unavailable, you're no longer able to provide updates to existing users. Ratings and reviews are not transferred to the new product page.

When adding macOS, tvOS, visionOS, or any combination of these platforms, you must upload the builds for macOS, tvOS, and visionOS from a separate Xcode target. In the Xcode project, set the bundle IDs to match the iOS app's bundle ID. However, the apps for macOS, tvOS, and visionOS may each have different version numbers and build strings than the iOS app.

Note: Once App Store Review approves at least two platform versions, your app becomes available as a universal purchase. Once it’s a universal purchase, your app stays as universal purchase—not being able to remove a single platform version from the app record.

Learn about adding a platform using App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Add Platform.

-  
In the Add Platform dialog that appears, choose the platform you want to add, then click Add.

A version for the platform appears selected in the sidebar with the version number 1.0. You can change the version number in the Version section in the sidebar under App Information.

-  
Review and enter metadata for the new platform version.

When you add a platform, metadata from the existing platform version is transferred to the new one, except for the promotional text, description, and screenshots.

Learn more about the platform version information and its required, localizable, and editable properties.

The Account Holder or an administrator can delete a platform if a build has never been uploaded for the specified platform and at least one existing platform version is in an editable app status. To delete a platform, hold the pointer over the platform you want to delete, and then click the delete button (–), which will appear to the right of the platform.

Related Upload builds Choose a build to submit Create a new version Manage App Store assets Add an app icon Creating your product page

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/add-watchos-app-information
### App Store Connect Help

App Store Connect / Create an app record / Add watchOS app information 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Add watchOS app information

watchOS  
You can create apps for Apple Watch using the watchOS 6 SDK, either as iOS apps with a watchOS app or as watchOS-only apps.

To prepare watchOS apps for distribution on the App Store, add an iOS app to App Store Connect and then include additional information specific to your app.

Ensure your description includes the app's functionality on Apple Watch. Provide screenshots of Apple Watch and an app icon. App Review reviews your screenshots and icon after you submit your new app version.

Learn how to prepare watchOS metadata for app submission.

Learn about the Human Interface Guidelines on creating your app icon.

Learn more about uploading your app icon.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Add watchOS app information

-  
In Apps, click the add button (+) on the top left.

-  
In the pop-up menu, select New App.

-  
In the New App dialog, select iOS on the top left, then enter your app information.

-  
Click Create, then select the Apple Watch tab under Previews and Screenshots.

-  
Drag Apple Watch screenshots for Apple Watch to the well.

Note: iOS screenshots are also required for apps with an iOS component, but not for watch-only apps.

Related Screenshot specifications Learn how to prepare watchOS app metadata for submission. Learn how to upload your app icon. Learn how to upload watchOS app screenshots with the App Store Connect API.

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/app-sandbox-information
### App Store Connect Help

App Store Connect / Reference / App uploads / App Sandbox information  
Filter ⌘K  
Filter ⌘K  

Reference  

# App Sandbox information

macOS  
If you use App Sandbox entitlements, Apple needs information on each temporary exception entitlement included in the app. You add a temporary exception entitlement by editing the .entitlements property list file in the Xcode project. For more information, visit App Sandbox Design Guide.

Property

Description

Entitlement Key

The entitlement key that corresponds to a temporary exception entitlement implemented in the app.

Usage Information

Information describing how to assess the entitlement and a description of the values in an array value used by the entitlement. If the entitlement works around a missing App Sandbox feature, file a bug report describing the exception using Feedback Assistant and include the bug ID in the usage information.

The description should include:

-  
How the entitlement can be assessed

-  
Why the entitlement is needed by the app

-  
What functionality this entitlement enables

-  
If the entitlement uses an array value, provide information on each value in the array

-  
If the entitlement works around a missing App Sandbox feature, the ID of the bug you filed describing the exception

Related App Sandbox Design Guide

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/apple-hosted-asset-pack-size-limits
### App Store Connect Help

App Store Connect / Reference / App uploads / Apple-hosted asset pack size limits 
Filter ⌘K  
Filter ⌘K  

Reference  

# Apple-hosted asset pack size limits

There are limits on the amount of storage used by Apple-hosted asset packs when you upload to App Store Connect. The table below outlines the different size limits for these asset packs. These limits are shared across all platforms offered for your app.

You can make additional space available by archiving asset packs. This removes all versions of an asset pack from App Store Connect, including those being tested in TestFlight and live on the App Store. Learn more.

Your App Store product page shows an “Up to” app size that includes any non-localized essential asset packs and the localized essential asset packs for the single language with the largest total size. Learn more about build file sizes.

Item

Size limit description

Size limit

Asset pack total

The total sum of size usage for all asset packs uploaded to an app record in App Store Connect.

For each asset pack in App Store Connect, Apple calculates the maximum size over all versions that are eligible to be tested in TestFlight or submitted for App Store distribution. This calculation doesn’t include versions that have the Awaiting Upload, Processing, or Failed TestFlight status, nor those that have the Superseded status for both TestFlight and the App Store. Then, the maximum size of each asset pack is added together to reach the asset pack total.

For example, AssetPackID1 has two versions: version 1 is 4 GB, and version 2 is 2 GB. AssetPackID2 has one version: version 1 is 1 GB. The asset pack total for this app is 5 GB, since the maximum size for AssetPackID1 is 4 GB and the maximum size for AssetPackID2 is 1 GB.

If you upload a new asset pack version and reach 80% or more of the asset pack total limit, you'll be notified via email. A banner will also display on the asset pack page in the TestFlight section of App Store Connect.

200 GB

Asset pack count

The total number of asset packs that are allowed to be uploaded to an app record in App Store Connect.

200

Related Overview of Apple-hosted asset packs Upload Apple-hosted asset packs Downloading asset packs hosted by Apple

=== SOURCE: https://developer.apple.com/help/app-store-connect/create-an-app-record/create-and-submit-app-bundles
### App Store Connect Help

App Store Connect / Create an app record / Create and submit app bundles 
Filter ⌘K  
Filter ⌘K  

Create an app record  

# Create and submit app bundles

You can offer apps, including those part of a universal purchase, as an app bundle on the App Store. App bundles simplify the process for you, letting you group up to ten of your apps together in a single download.

Apps in a bundle must follow these guidelines:

-  
All apps must be either all paid or all free.

-  
A paid app bundle can only include paid apps and must be offered at a reduced price.

-  
You must ensure that each app in a free app bundle is free and offers an auto-renewable subscription. The subscription must allow the user to subscribe to and access content or services in all apps included in the bundle.

-  
Apps that support tvOS only or visionOS only can’t be part of a bundle.

Note: For app bundles created before February 17, 2026, each app in the bundle must support at least one of the same platforms as the first app you add, known as the primary app. For bundles created after the date, apps included in the bundle don’t need to support the same platform as the primary app.

Customers purchase the bundle with a single tap or click, and the individual apps install automatically on their device. Customers who have previously bought one or more apps in an app bundle can use the Complete My Bundle feature. The bundle price adjusts to reflect their existing purchases.

Learn how to set up app bundles and effectively market them on your App Store product page.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Create an app bundle

-  
In Apps, click the add button (+) and select New App Bundle.

-  
In the Name field, enter a unique name for the app bundle.

-  
Under Apps in This Bundle, hold the pointer over the app you want to add to the bundle, and click the add button (+).

You can add an app to a bundle if it’s in the Ready for Distribution state. The first app you choose to include in the bundle becomes the primary app. Certain aspects of the app bundle information is determined based on the primary app.

-  
On the top right, click Create.

Later, the app bundle appears on your Apps page.

-  
Under Bundle Information, enter the required app bundle information, then click Save.

### Submit an app bundle for review

-  
In Apps, select the app bundle you want to view.

-  
On the top right, click Submit for Review.

The app bundle status changes to Waiting for Review. When the review process starts, the app status changes to In Review. After the app bundle is approved, you can no longer add or remove apps from the bundle.

### Remove an app bundle from review

-  
In Apps, select the app bundle you want to remove.

-  
On the top right, click Remove from Review.

This action will remove the app bundle from Apple's review queue, and the app status will change to Developer Rejected.

Related Edit app bundle information App bundle information

=== SOURCE: https://developer.apple.com/help/app-store-connect/configure-game-center/manage-an-app-version-for-game-center
### App Store Connect Help

App Store Connect / Configure Game Center / Manage an app version for Game Center 
Filter ⌘K  
Filter ⌘K  

Configure Game Center  

# Manage an app version for Game Center

Apps offering Game Center features need to include the Game Center entitlement in the entitlements plist and have Game Center features configured in App Store Connect before they can be submitted for review.

You can enable or disable Game Center for your app at the version level. Once an app version is approved with Game Center enabled, Game Center can’t be disabled for that version. Instead, you’ll need to disable Game Center when submitting an updated app version.

Note: Games distributed via alternative distribution will need to also be available on at least one App Store storefront to take advantage of Game Center functionality.

Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.

## Enable app version for Game Center

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version you want to enable for Game Center.

-  
Scroll down and select the checkbox next to Game Center.
Learn how to submit Game Center components with the app version for review. 

### Disable app version for Game Center

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version under your desired platform, then navigate to the Game Center section.

-  
Deselect the Game Center checkbox to disable Game Center for the version.

Related Game Center properties Overview of submitting for review Enabling and configuring Game Center

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-a-default-app-clip-experience
### App Store Connect Help

App Store Connect / Offer App Clip experiences / Offer a default App Clip experience 
Filter ⌘K  
Filter ⌘K  

Offer App Clip experiences  

# Offer a default App Clip experience

A default App Clip experience is required and can be invoked using Safari and Messages, as well as through an NFC tag, QR code, and links in other apps when using an Apple-provided App Clip link. Learn about configuration options.

Note: People can launch your App Clip from other apps on iOS 17 or later.

A default App Clip link is optional, but useful for App Clips that only require a single App Clip experience. This link allows you to invoke the default App Clip experience on devices running iOS 16.4 or later.

When you upload a build that has an App Clip and configure a default App Clip experience, a default App Clip link and App Clip demo URL are automatically generated in App Store Connect.

Default App Clip link

https://appclip.apple.com/id?p=app_clip_bundle_id&key=value

Default App Clip demo URL

https://apps.apple.com/id?p=app-clip-bundle-id-=value

These will become active once your version has been approved.

Once you create a default App Clip experience, you can create advanced App Clip experiences.

Learn how to create a default App Clip experience using the App Store Connect API.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the iOS app version for which you want to add an App Clip experience and scroll down to the App Clip section.

-  
Enter a header image, subtitle, and action. This metadata appears on the App Clip card when the experience is invoked from Safari or Messages.

Learn more about the required, localizable, and editable properties.

Note: You must provide a header image with the following specifications:

-  
Supported extensions: .jpg, .jpeg, .png

-  
Aspect ratio: 3 : 2

-  
Resolutions: 1800 x 1200 pixels

-  
On the top right, click Save.

Related Watch WWDC23 What’s new in App Clips Design > App Clips App Clips framework Maximum build file sizes Choosing the right functionality for your App Clip Creating an App Clip with Xcode

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/offer-an-advanced-app-clip-experience
### App Store Connect Help

App Store Connect / Offer App Clip experiences / Offer an advanced App Clip experience 
Filter ⌘K  
Filter ⌘K  

Offer App Clip experiences  

# Offer an advanced App Clip experience

Learn how to create an advanced App Clip experience using the App Store Connect API.

## Set up an advanced App Clip experience without place association

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the iOS app version for which you want to add an App Clip experience.

-  
Under Advanced App Clip Experiences, click Edit Advanced Experiences. A new page opens with general information on what to provide.

-  
Click Next.

-  
In the App Clip experience URL field, enter the invocation URL for your App Clip experience.

The App Clip Bundle ID will be prepopulated.

-  
Click Next.

-  
Enter the information for the App Clip card. To add a Default Display Title and Default Subtitle in additional languages, click Add Additional Titles.

-  
Specify that your App Clip experience isn’t associated with a place.

View tooltips next to each field for more details.

-  
Select a call to action, then click Next.

-  
Answer the question about what this App Clip experience promotes. Specify whether it promotes your app’s business, service, or brand or if it’s created on behalf of other businesses, services, or brands that appear within your app.

Learn about creating App Clips for other businesses.

-  
Click Send to Apple.

All the experiences you’ve configured, along with their statuses, will display on the App Clip experiences page.

### Set up an advanced App Clip experience with place association

Connecting your App Clip to a physical location is optional through a place association. This feature is necessary for launching the App Clip experience via Apple Maps. Place association doesn’t guarantee inclusion in Apple Maps and may not be available in all countries and regions.

If your App Clip is part of the location’s official app, it’ll be automatically approved for that location. If it’s not part of the official app, either the business owner must claim the location through Apple Business Connect and approve the App Clip to display, or the creator of the App Clip must be authorized as a partner on the business’ website.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the iOS app version for which you want to add an App Clip experience.

-  
Under Advanced App Clip Experiences, click Edit Advanced Experiences. A new page opens with general information on what to provide.

-  
Click Next.

-  
In the App Clip experience URL field, enter the invocation URL.

The App Clip Bundle ID will be prepopulated.

-  
Click Next.

-  
Enter the information for the App Clip card. To add a Default Display Title and Default Subtitle in additional languages, click Add Additional Titles.

-  
Specify that your App Clip experience is associated with a place.

View tooltips next to each field for more details.

-  
Select a Maps action that best fits the experience and click Next. This determines the action that appears on the place card in Maps.

-  
Choose a place to associate with this App Clip experience.

-  
Answer the question about the relationship between your app and the place associated with this App Clip experience.

-  
Answer the question about what this App Clip experience promotes. Specify whether it promotes your app’s business, service, or brand, or if it’s created on behalf of other businesses, services, or brands that appear within your app.

Learn about creating App Clips for other businesses.

-  
If your App Clip experience promotes another business, service, or brand, select a category.

-  
Click Send to Apple.

All the experiences you’ve configured, along with their statuses, will display on the App Clip experiences page.

Note: To confirm that your App Clip experience appears in Maps, open Maps and search for places associated with the experience.

Related Maximum build file sizes Choosing the right functionality for your App Clip Creating an App Clip with Xcode

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/on-demand-resources-size-limits
### App Store Connect Help

App Store Connect / Reference / App uploads / On-demand resources size limit 
Filter ⌘K  
Filter ⌘K  

Reference  

# On-Demand Resources size limits

On-Demand Resources are app contents that are hosted on the App Store and are separate from the related app bundle that you download. They enable smaller app bundle, faster downloads, and richer app content.

Note: On-Demand Resources are deprecated on Apple platforms as of iOS 27, iPadOS 27, tvOS 27, and visionOS 27, and support will be removed in future releases. Migrating to Background Assets is recommended.

There are limits on the amount of storage used by On-Demand Resources when you upload your app to App Store Connect or while the app is running.

Note: macOS and watchOS don't support On-Demand Resources.

## On-Demand Resource sizes

The table below outlines the variant size limits for each deployment target after app thinning. For example, the total size limit of each asset pack is 8GB after thinning for apps available on devices running iOS 18 and later.

### On-Demand Resource size limits for iOS and iPadOS apps

Item

Size limit description

Earlier than iOS 18 or earlier than iPadOS 18

iOS 18 or iPadOS 18, or later

App bundle

The size of the thinned app bundle downloaded to the device.

2 GB

4 GB

Asset pack

The size of each thinned asset pack. Asset packs are generated by Xcode when your app is built. One tag may result in multiple asset packs.

512 MB

8 GB

Asset pack count

The total number of asset packs generated by Xcode.

1000

1000

Initial install and prefetched tags

The total size of the thinned asset packs marked with initial install and prefetched tags.

4 GB

No limit

In use On-Demand Resources

The total size of the resources with the tags in use by the app at any one time. A tag is in use as long as at least one NSBundleResourceRequest is accessing it.

2 GB

No limit

Hosted On-Demand Resources

The total size of the thinned asset packs hosted on the App Store.

20 GB

70 GB

### On-Demand Resource size limits for tvOS apps

Item

Size limit description

Earlier than tvOS 18

tvOS 18 or later

App bundle

The size of the thinned app bundle downloaded to the device.

4 GB

4 GB

Asset pack

The size of each thinned asset pack. Asset packs are generated by Xcode when your app is built. One tag may result in multiple asset packs.

512 MB

512 MB

Asset pack count

The total number of asset packs generated by Xcode.

1000

1000

Initial install and prefetched tags

The total size of the thinned asset packs marked with initial install and prefetched tags.

4 GB

4 GB

In use On-Demand Resources

The total size of the resources with the tags in use by the app at any one time. A tag is in use as long as at least one NSBundleResourceRequest is accessing it.

2 GB

No limit

Hosted On-Demand Resources

The total size of the thinned asset packs hosted on the App Store.

20 GB

20 GB

### On-Demand Resource size limits for visionOS apps

Item

Size limit description

Earlier than visionOS 2

visionOS 2 or later

App bundle

The size of the thinned app bundle downloaded to the device.

4 GB

4 GB

Asset pack

The size of each thinned asset pack. Asset packs are generated by Xcode when your app is built. One tag may result in multiple asset packs.

512 MB

8 GB

Asset pack count

The total number of asset packs generated by Xcode.

1000

1000

Initial install and prefetched tags

The total size of the thinned asset packs marked with initial install and prefetched tags.

4 GB

No limit

In use On-Demand Resources

The total size of the resources with the tags in use by the app at any one time. A tag is in use as long as at least one NSBundleResourceRequest is accessing it.

2 GB

No limit

Hosted On-Demand Resources

The total size of the thinned asset packs hosted on the App Store.

20 GB

70 GB

=== SOURCE: https://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/overview-of-app-clips
### App Store Connect Help

App Store Connect / Offer App Clip experiences / Overview of App Clips 
Filter ⌘K  
Filter ⌘K  

Offer App Clip experiences  

# Overview of App Clips

An App Clip is a small part of your app that’s discoverable at the moment it’s needed and lets people quickly start and finish a task from your app. Users running iOS 14 or later can quickly access App Clips without needing to download the full app. Learn about App Clips.

Note: App Clips are subject to the same age restrictions and parental controls as full apps. However, App Clips aren’t available to children under 13 or those with Ask to Buy enabled, regardless of other restrictions and settings. To access all of an app’s features, such as those normally offered through App Clip codes and QR codes, these users must install the full app.

You can configure how your App Clip is discovered and launched by creating App Clip experiences. Each experience includes metadata for the App Clip card, an invocation URL, and various invocation methods. You can create many App Clip experiences to support situations when different tasks from your app might be helpful.

A default App Clip experience is required and can be invoked using Safari and Messages, as well as through an NFC tag, QR code, and links in other apps when using an Apple-provided App Clip link.

You can also create advanced App Clip experiences, which let you configure your App Clip to use multiple domains, associate your App Clip with physical locations, and customize multiple App Clip cards to represent different businesses with a single App Clip. Learn about configuration options.

When you’re ready to submit your app for review to distribute on the App Store, you can optionally provide up to three URLs that are representative of experiences your App Clip provides, allowing App Review to understand the features and functionalities. Add these URLs in the App Clips URLs section in App Review Information toward the bottom of the Version Information page.

To edit the App Clip section in App Store Connect, you must first upload a build that includes an App Clip. Ensure that each subsequent app version you submit includes the App Clip to maintain its availability for users.

Learn how to read App Clip information and manage App Clip experiences using the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

Related Maximum build file sizes Choosing the right functionality for your App Clip Creating an App Clip with Xcode

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-asset-packs/overview-of-apple-hosted-asset-packs
### App Store Connect Help

App Store Connect / Manage asset packs / Overview of Apple-hosted asset packs 
Filter ⌘K  
Filter ⌘K  

Manage asset packs  

# Overview of Apple-hosted asset packs

The Background Assets framework allows you to schedule background downloads of additional content using your server or content delivery network (CDN). Apps targeting iOS 26, iPadOS 26, macOS 26, tvOS 26, and visionOS 26 and later can use Managed Background Assets. With Managed Background Assets, the system automatically manages downloads, updates, and compression for your assets. Additionally, apps distributed through TestFlight and the App Store can use Apple-Hosted Background Assets, and Apple will host the content on your behalf.

Assets for Managed Background Assets are managed through asset packs that you configure using a command-line packaging tool in Xcode, or the Managed Background Assets Developer Tools for Linux. Users’ devices automatically download these asset packs separately from your app build. When you use Apple hosting, you can also upload asset packs to App Store Connect separately from your app build.

Learn how to create, download, and locally test Apple-hosted asset packs.

After you upload an asset pack to App Store Connect, you can test it using TestFlight, and submit it for distribution on the App Store.

## Localized asset packs

Starting with iOS 27, iPadOS 27, macOS 27, tvOS 27, and visionOS 27, you can use Managed Background Assets to distribute localized assets separately from your app build. Include localized assets in separate asset packs for each language, and users automatically receive the appropriate asset pack based on their system settings, or app language preferences when available.

Note: Devices running earlier OS versions won’t receive localized asset packs.

You can associate each asset pack version with one language in the manifest file. The language must be a valid BCP-47 identifier and can contain language, script, and region subtags (for example, “zh-Hans-CN” or “en-US”). You can change the associated language from version to version, and you can associate a language with multiple asset pack versions.

Note: Creating and testing localized asset packs isn’t supported in the Managed Background Assets Developer Tools for Linux. Use the packaging tool in Xcode instead.

If no localized asset packs match a user’s language settings, the system uses the asset pack in the next most relevant language, such as other regional variations of the language or the app’s primary language.

Related Watch “Discover Apple-Hosted Background Assets” Apple-hosted asset pack statuses Apple-hosted asset pack size limits

=== SOURCE: https://developer.apple.com/help/app-store-connect/configure-game-center/overview-of-game-center
### App Store Connect Help

App Store Connect / Configure Game Center / Overview of Game Center 
Filter ⌘K  
Filter ⌘K  

Configure Game Center  

# Overview of Game Center

Game Center is Apple’s social gaming network that lets players track their progress, invite friends to play, start multiplayer games through auto-match, and more. It also boosts the discovery of your games across players’ devices. Once you’ve implemented Game Center features, you’re ready to enter related metadata in App Store Connect.

Note: To add a game with Game Center features to a new app bundle, the game must be “Ready for Distribution" on at least one App Store storefront. For games distributed through alternative distribution, availability on at least one App Store storefront is required to utilize Game Center functionality.

You can complete the steps below in the order they're listed or move between steps as needed.

Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.

-  
Enable Game Center in Xcode.

In Xcode, create your project, enter an app name and bundle ID, then enable Game Center, which adds the GameKit framework and Game Center Entitlement to your project. Learn more about enabling Game Center in Xcode.

-  
Configure Game Center in App Store Connect.

In App Store Connect, add an app to your account that matches the bundle ID in Xcode, enable your app version for Game Center, and configure Game Center components, such as leaderboards, achievements, challenges, activities, groups, and multiplayer compatibility.

-  
Implement Game Center features.

To integrate Game Center into your app using Xcode, add the necessary code and configure the service's components. Although these components are set up independently from your app bundle, they must be closely integrated with your game's code to fulfill all design and development requirements. Learn more.

Learn the guidance and best practices that can help you design a great experience for Game Center.

-  
Test your game.

Ensure that your Game Center components work individually and together. Apple enables all prerelease development to take place in the same server environment as released games, so you can play with the full player base, not just other testers.

-  
Distribute your game.

Add your Game Center components to your desired platform version before submitting your game for review.

Related Game Center Games Use Game Center to boost discovery and engagement

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/provide-app-motion-information
### App Store Connect Help

App Store Connect / Reference / App information / Provide app motion information 
Filter ⌘K  
Filter ⌘K  

Reference  

# Provide app motion information

App motion is a required app information property for all visionOS apps on the App Store. This information displays on your app’s product page on the App Store to inform users who may be sensitive to apps with high motion.

There are two possible values for this property:

Value

Definition

Yes, this app contains high motion

Has frequent fast or sudden camera movements, quick turns, or unusual orientations.

No, this app doesn't contain high motion

Doesn't have frequent fast or sudden camera movements, quick turns, or unusual orientations.

## About app motion

On Apple Vision Pro, the user’s viewpoint acts as a virtual camera and moves with the motion of their head and body. In some experiences, the virtual camera moves without the user moving their head or body (either controlled by the user through hand gestures or input devices, or scripted by the app without user input).

### When to choose “No, this app doesn’t contain high motion”

If the virtual camera in your app doesn’t move without the user moving their head or body, choose “No, this app doesn’t contain high motion.” You won't need to assess your app further.

#### When to assess your app for high motion

If the virtual camera in your app moves without the user moving their head or body, you might need to choose “Yes, this app contains high motion.” To find out, follow the guidance below to assess your app experience for:

-  
Fast forward or backward motion

-  
Unusual orientations

-  
Fast rotation speeds

-  
Unexpected motion

Keep the following in mind:

-  
Assess only the motion of the user’s viewpoint as a virtual camera, not the motion of a user-controlled character or vehicle. This distinction is especially important when the motion of the virtual camera is different than the motion of a controlled character or vehicle.

-  
If your app has multiple configuration options that affect the motion experience, use the default configuration to assess the experience.

-  
Rate the average motion in your app. If there’s only a brief moment of high motion at a few points in your app and the rest contains no motion, you don’t need to indicate high motion in your app.

-  
If your app consists of several different first-party experiences that are intended by design to be part of the core app experience, consider the average motion across all of them and whether the average contains high motion.

-  
Apps that host a variety of third-party content (like user-uploaded videos or HTML5 games) shouldn’t have a high motion label, unless the app’s intent is to have lots of content with high motion (like user uploads of their first-person thrill-seeking experiences).

#### Elements to assess

### Fast forward or backward motion

Combinations of forward or backward virtual camera motion can lead to very high pixel speeds.

Example 1 demonstrates the pixel speed when the camera moves forward quickly, with objects close by, resulting in high motion. The red arrows indicate the objects’ pixel speed in the scene.

Example 2 shows a much slower pixel speed that doesn’t fall under the category of high motion. This can be produced by moving objects farther away or with slower camera motion.

Choose “Yes, this app contains high motion” if the combination of forward or backward virtual camera speed and object distance in your app produces a pixel speed similar to or higher than that shown in Example 1.

Example 1: High pixel speed

Example 2: Low pixel speed

### Unusual orientations

When the horizon of the virtual world doesn't match the real world, users may experience discomfort. The virtual camera rolls left or right around its longitudinal axis or pitches up or down in situations like these.

Choose “Yes, this app contains high motion” if the virtual camera rolls around its longitudinal axis or pitches up or down more than 10 degrees, with less than 5 minutes between each instance. This includes loops, steep banks or slopes, and upside-down motion.

### Fast rotation speeds

Users can also experience discomfort when they experience fast camera rotation speeds around their vertical axis (yaw).

Choose “Yes, this app contains high motion” if the virtual camera yaws left or right smoothly, while simultaneously moving forward or backward at speeds equal to or slower than running. This includes user-controlled and scripted smooth camera turns in first-person-view experiences.

### Unexpected motion

Choose “Yes, this app contains high motion” if the virtual camera makes unexpected and/or unpredictable motions with less than 5 minutes between each instance. This includes falls, turns, spins, and other orientation changes.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/set-the-app-motion-information-for-apple-vision-pro
### App Store Connect Help

App Store Connect / Manage app information / Set the app motion information for Apple Vision Pro 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Set the app motion information for Apple Vision Pro

All visionOS apps on the App Store must include the app motion information as a required property within their app information. If your app includes experiences with high motion, users will be informed through a label displayed on your app's product page.

Learn how to assess your app for high motion.

Note: You’ll need to set this information in order to submit your visionOS app for review.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version under the visionOS app platform.

-  
Below App Motion Information, click Set Up.

-  
In the dialog that appears, select either “Yes, this app contains high motion” or “No, this app doesn’t contain high motion”.

-  
Click Save.

Note: To update this information at any time, click Edit next to Contains High Motion. The change reflects on the App Store immediately.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-apple-hosted-asset-packs
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit Apple-hosted asset packs 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit Apple-hosted asset packs

Asset packs must be reviewed before they can be tested externally in TestFlight or made available for users on the App Store. Learn about submitting asset packs for external testing.

Once an asset pack version is approved for the App Store, it’ll automatically be available to all App Store users, and any previous versions of the asset pack will be replaced with the new one.

If your app hasn’t been approved yet and you want to submit an asset pack version, include the asset pack version in the same submission as your first app version. After your app is approved, you can submit an asset pack version with or without an app version. However, if a new app version requires a new asset pack to function, include a version of that asset pack in the same submission as the new app version. You can also add other items to a submission, such as In-App Events.

You can include up to ten different asset packs in a submission, with one version of each asset pack permitted at a time.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, under General, click Asset Packs.

If you haven’t uploaded any asset packs yet, the Asset Packs section won’t appear.

-  
On the right, find the asset pack ID with the version you want to submit.

-  
If this is the first version you're submitting for the App Store, click Select Asset Pack Version. If you already have a version available on the App Store, click Replace.

Note: Asset pack versions that are packaged using a beta Managed Background Assets packaging tool can’t be added for review.

-  
Select the asset pack version you want to submit to App Review. 

-  
Click Add for Review, then select whether to add the asset pack version to an existing draft submission or create a new submission. The asset pack version’s status changes to Ready for Review.

If you’re submitting the asset pack for review with an app version, it will be reviewed together with that app version.

If you’re submitting the asset pack for review without an app version, or your submission includes items associated with multiple platforms, select a platform in the draft submission screen. The asset pack version, and any other items in your submission, will be reviewed together with the latest version of the selected platform.

You may choose to add other items to the submission.

-  
Click Submit for Review. The asset pack version’s status changes to Waiting for Review. When the review process starts, the status changes to In Review. Learn more about Apple-hosted asset pack statuses.

Related Overview of Apple-hosted asset packs Upload Apple-hosted asset packs Test Apple-hosted asset packs

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-game-center-components
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit Game Center components 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit Game Center components

New or modified leaderboards, leaderboard sets, achievements, challenges, and activities must be reviewed before they can be made available to players through Game Center.

Include components in the same submission as your app version if this is the first time you're adding them to an app. For subsequent components, you can submit them without an app version.

Game Center components submitted without an app version are reviewed against the latest platform version specified during submission. You can also include other items with these submissions. Get an overview of submitting an app or items for review.

Required role: Account Holder, Admin, App Manager, Developer, or Marketing. View role permissions.

## Submit Game Center components for review

-  
In Apps, select the app you want to view.

-  
In the sidebar, click Game Center.

-  
Select a Game Center component you want to submit to App Review. For example, a leaderboard.

-  
On the top right, click Add for Review and select whether to add the component to an existing draft submission or create a new submission.

If you’re submitting the component for review with an app version, it’ll be reviewed together with the app version. If you’re submitting it for review without an app version, it’ll be reviewed against the latest version of the selected platform. You can switch the platform in the draft submission screen.

Note: You can include up to 200 different components in a submission. Learn how many leaderboards, leaderboard sets, achievements, challenges, and activities you can create.

-  
Click Submit for Review.

The component’s status changes to Waiting for Review. When the review process starts, the status changes to In Review.

### Remove a Game Center component from draft submission

You can remove the component in Ready for Review status from the draft submission. For submitted Game Center component, you can cancel your submission from review if it’s in Waiting for Review or In Review status. 

-  
In Apps, select the app you want to view.

-  
In the bottom-right corner of the screen, click Draft Submissions, then select the submission you want to remove a component from.

-  
Hover over the component you want to remove, then click the red delete button (-). The component status changes to Developer Rejected.

You can also remove a component from the submission in the Game Center section. In the Game Center section, select the Game Center component you want to remove from review, then click "Remove from Review" in the message that appears at the top. Similarly, you can remove a submission from the App Review section. Learn more.

Related Overview of submitting for review

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/test-an-app-clip-experience
### App Store Connect Help

App Store Connect / Test a beta version / Test an App Clip experience 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Test an App Clip experience

App Clips allow you to make a small part of your app discoverable and quick to launch at the moment it’s needed. You can add up to three invocation URLs to launch different experiences within your App Clip. Testers running TestFlight for iOS, version 2.7 or later, and iOS 14 beta or later can test and provide feedback on all available App Clip experiences. Currently, testing of other invocation methods is not supported. Learn more about testing your App Clip’s launch experience.

Learn how to view tester feedback.

Learn how to manage App Clip experiences for testers with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Add an App Clip invocation

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, below Builds, click the iOS platform.

-  
In the Builds column, click the app icon or build string for the build that has the App Clip you'd like to test. The page opens with the Test Information tab selected.

-  
Under App Clip Invocations, click Add App Clip Invocation.

-  
In the dialog that appears, enter the title and URL for your App Clip invocation.

Note: You can localize the App Clip title for each URL based on the localizations you have added for your build in TestFlight, but the URL will be the same across localizations.

-  
Click Add.

-  
On the top right of the page, click Save.

Note: You can test an App Clip experience using TestFlight, provided that the App Clip is included in the build. To create defined experiences, incorporate up to three invocation URLs.

### Delete an App Clip invocation

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under Builds, click the iOS platform.

-  
In the Build column, click the app icon or build string for the build that has the App Clip invocation you'd like to delete. The page opens with Test Information tab selected.

-  
Under App Clip Invocations, hold the pointer over the App Clip invocation and click the delete button (–) that appears to the right of the URL.

-  
In the dialog that appears, click Delete.

-  
On the top right of the page, click Save.

