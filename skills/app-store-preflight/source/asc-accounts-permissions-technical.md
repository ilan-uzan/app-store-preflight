=== SOURCE: https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion/
### App Review Help

App Review / Guideline reference / 5.1.1(v) - Offering account deletion in your app 
Filter ⌘K  
Filter ⌘K  

Guideline reference  

# 5.1.1(v) - Offering account deletion in your app

Apps submitted to the App Store that support account creation must also let people initiate deletion of their account within the app.

Deleting an account removes the account from the developer's records, along with any data associated with the account that the developer isn't legally required to maintain. Providing this capability gives people more control of the personal data they've shared. If you're updating an app or submitting a new app with account creation, read the guidance below for a smoother submission process.

## Account deletion guidance

Deleting an account is a major decision, so the process to initiate and confirm it must be straightforward and transparent:

-   Make the account deletion option easy to find in your app. Typically, it's included in the app's account settings. 

-   Offer to delete the entire account record, along with associated personal data. You may include additional options, but only offering to temporarily deactivate or disable an account is insufficient. 

-   If people need to visit a website to finish deleting their account, include a link directly to the page on your website where they can complete the process. On tvOS, you can present a static URL or QR code that links directly to the account deletion page. 

-   Keep people informed. If the deletion request will take additional time to complete, let them know. If your app supports in-app purchases, help people understand how billing and cancellations will be handled. If you're legally required to retain some user information, let people know what information will and won't be retained. For additional guidance, read the Human Interface Guidelines. 

Note: Follow applicable legal requirements for storing and retaining user account information and for handling account deletion. This includes complying with local laws where your app is available. If you have questions regarding your legal obligations, check with your legal counsel.

##  FAQs

### Can I direct people to a customer service flow to complete account deletion?

It depends. Apps in highly regulated industries, as described in App Review Guideline 5.1.1(ix), may use additional customer service flows to confirm and facilitate the account deletion process. Apps not operating in highly regulated industries should not require people to make a phone call, send an email, use a chat support flow, or go through other support flows.

### Can I require reauthentication or add confirmation steps to ensure the account isn't deleted by accident or by someone other than the account holder?

Yes. It's appropriate to confirm the user genuinely intends to delete their account. You may add steps to verify the identity of the person making the request, and to confirm that they want to delete the account, such as by entering a code from an email or phone number already associated with the account. However, apps that make it unnecessarily difficult for someone to delete their account will not pass review.

### My app uses Sign in with Apple to provide account creation and authentication. What changes are necessary to support people who delete their accounts?

Apps that support Sign in with Apple should use the Sign in with Apple REST API to revoke user tokens. Use server-to-server notification endpoints to process changes for Sign in with Apple accounts. Note that developers based in the Republic of Korea must provide a server‑to‑server notification endpoint when registering a new Services ID.

### If my app links out to the default web browser for account creation, does it still need to offer account deletion within the app?

Yes. Additionally, linking out to the default web browser to sign in or register an account provides a poor user experience and isn't appropriate, per App Review Guideline 4.

### My app automatically creates an account for the user. Do I need to include an option to initiate account deletion?

Yes. People should have the option to delete automatically generated accounts (sometimes called "guest" accounts) and the data associated with those accounts. Ensure any automatic account creation in your app complies with local laws where your app is available.

### I manually delete accounts and this takes time. Does account deletion need to be immediate and automatic?

No. If your process for account deletion is manual or otherwise takes a reasonable amount of time to complete, this is acceptable. Inform the person how long it will take to delete the account and provide a confirmation when the deletion is complete. Ensure the time it takes to delete accounts complies with local laws where your app is available.

### Does the content provided by a person need to be deleted in apps that display and share user-generated content?

Yes. People expect that all data associated with their account will be deleted when the account is deleted. This includes user-generated content that's shared with others, such as photos, videos, text posts, and reviews. If local laws or regulations require you to maintain some data, let people know.

### I allow account deletion in compliance with CCPA, GDPR, or other local laws in some of the locations where my app is available. Is this sufficient?

No. Everyone should be able to delete their accounts, regardless of where they're located. Existing account deletion flows you've created to comply with local legal requirements can be made available to everyone, as long as they meet the requirements of App Review Guideline 5.1.1(v).

### How do I handle people with auto-renewable subscriptions? I don't want to accidentally charge someone after they've deleted their account.

If a person has an auto-renewable subscription, notify them that billing will continue through Apple and ask them to cancel their subscription before continuing. If you use App Store Server Notifications for auto-renewable subscriptions, you can verify the status of the person's subscription in real time, or use the Subscription Status API to identify subscription status.

Use showManageSubscriptions in iOS 15 and iPadOS 15, or later, or provide this link to let people manage their subscriptions: https://apps.apple.com/account/subscriptions/. For tvOS, provide onscreen instructions to change or cancel a subscription, as described in the Apple TV User Guide.

You can also use beginRefundRequest in iOS 15 and iPadOS 15, or later, or provide this Apple Support link to let customers submit refund requests: https://support.apple.com/118223.

Additionally, you can offer to schedule account deletion for a later date, aligned with the subscription's expiration, as long as there's also an option to delete the account immediately.

Related App Review Guidelines Manage Accounts

=== SOURCE: https://developer.apple.comdoc://com.apple.HIG/design/Human-Interface-Guidelines/app-icons
# App icons

A unique, memorable icon expresses your app’s or game’s purpose and personality and helps people recognize it at a glance.



Your app icon is a crucial aspect of your app’s or game’s branding and user experience. It appears on the Home Screen and in key locations throughout the system, including search results, notifications, system settings, and share sheets. A well-designed app icon conveys your app’s or game’s identity clearly and consistently across all Apple platforms.



### Layer design

Although you can provide a nonlayered image for your icon (see Icon formats), layers give you the most control over how your icon design is represented. A layered app icon comes together to produce a sense of depth and vitality. On each platform, the system applies visual effects that respond to the environment and people’s interactions.

iOS, iPadOS, macOS, and watchOS app icons include a background layer and one or more foreground layers that coalesce to create dimensionality. These icons take on Liquid Glass attributes like specular highlights, refraction, and translucency. These effects automatically adapt with the size of your icon, apply consistently across platforms, and can appear differently between system versions.

tvOS app icons use between two and five layers to create a sense of dynamism as people bring them into focus. When focused, the app icon elevates to the foreground in response to someone’s finger movement on their remote, and gently sways while the surface illuminates. The separation between layers and the use of transparency produce a feeling of depth during the parallax effect.

A visionOS app icon includes a background layer and one or two layers on top, producing a three-dimensional object that subtly expands when people view it. The system enhances the icon’s visual dimensionality by adding shadows that convey a sense of depth between layers and by using the alpha channel of the upper layers to create an embossed appearance.

You use your favorite design tool to craft the individual foreground layers of your app icon. For iOS, iPadOS, macOS, and watchOS icons, you then import your icon layers into Icon Composer, a design tool included with Xcode and available from the Apple Developer website. In Icon Composer, you define the background layer for your icon, adjust your foreground layer placement, apply visual effects like specular highlights and refraction, annotate for default, dark, and mono appearance variants, test and preview your icon across system versions, and export your icon for use in Xcode. For additional guidance, see Creating your app icon using Icon Composer.



For tvOS and visionOS app icons, you add your icon layers directly to an image stack in Xcode to form your complete icon. You can download Parallax Previewer and Parallax Exporter plug-in from Apple Design Resources to preview and test parallax visual effects. For developer guidance, see Configuring your app icon using an asset catalog.

Prefer clearly defined edges in foreground layers. To ensure system-drawn highlights and shadows look best, avoid soft and feathered edges on foreground layer shapes.

Vary opacity in foreground layers to increase the sense of depth and liveliness. For example, the Photos icon separates its centerpiece into multiple layers that contain translucent pieces, bringing greater dynamism to the design. Importing fully opaque layers and adjusting transparency in Icon Composer lets you preview and make adjustments to your design based on how transparency and system effects impact one another.

Design a background that both stands out and emphasizes foreground content. If you choose a gradient for your background layer, ensure that it responds well to system lighting effects. Icon Composer supports solid colors and gradients for background layers, making it unnecessary to import custom background images in most cases. If you do import a background layer, make sure it’s full-bleed and opaque.

Prefer vector graphics when bringing layers into Icon Composer. Unlike raster images, vector graphics (such as SVG or PDF) scale gracefully and appear crisp at any size. Outline artwork and convert text to outline in your design. For mesh gradients and raster artwork, prefer PNG format because it’s a lossless image format.

### Icon formats

In iOS, iPadOS, macOS, and watchOS, you can provide icons in one of two formats: nonlayered bitmap images (such as PNG) or layered Icon Composer files. The Icon Composer format lets you control how Liquid Glass applies to individual elements of your icon, and how color applies across appearance variants.

Provide your icon in the Icon Composer format for more flexibility and control. If you provide a bitmap image instead, the system attempts to segment your icon, isolating the foreground elements from the background to create an icon with two layers. These two layers help make your icon compatible with dark and tinted appearance variants, ensuring the use of a consistent background.

When the system segments your icon, it applies Liquid Glass effects to foreground layers that feature large, simple shapes. It doesn’t automatically apply Liquid Glass effects to smaller, more complex elements in an icon like text and thin lines. To control precisely which elements receive Liquid Glass properties, supply your icon as a layered Icon Composer file.

### Icon shape

An app icon’s shape varies based on a platform’s visual language. In iOS, iPadOS, and macOS, icons are square, and the system applies masking to produce rounded corners that precisely match the curvature of other rounded interface elements throughout the system and the bezel of the physical device itself. In tvOS, icons are rectangular, also with concentric edges. In visionOS and watchOS, icons are square and the system applies circular masking.

Produce appropriately shaped, unmasked layers. The system masks all layer edges to produce an icon’s final shape. For iOS, iPadOS, and macOS icons, provide square layers so the system can apply rounded corners. For visionOS and watchOS, provide square layers so the system can create the circular icon shape. For tvOS, provide rectangular layers so the system can apply rounded corners. Providing layers with pre-defined masking negatively impacts specular highlight effects and makes edges look jagged.

Keep primary content centered to avoid truncation when the system adjusts corners or applies masking. Pay particular attention to centering content in visionOS and watchOS icons. To help with icon placement, use the grids in the app icon production templates, which you can find in Apple Design Resources.

### Design

Embrace simplicity in your icon design. Simple icons tend to be easiest for people to understand and recognize. An icon with fine visual features might look busy when rendered with system-provided shadows and highlights, and details may be hard to discern at smaller sizes. Find a concept or element that captures the essence of your app or game, make it the core idea of your icon, and express it in a simple, unique way with a minimal number of shapes. Prefer a simple background, such as a solid color or gradient, that puts the emphasis on your primary design — you don’t need to fill the entire icon canvas with content.

Provide a visually consistent icon design across all the platforms your app supports. A consistent design helps people quickly find your app wherever it appears and prevents people from mistaking your app for multiple apps.

Consider basing your icon design around filled, overlapping shapes. Overlapping solid shapes in the foreground, particularly when paired with transparency and blurring, can give an icon a sense of depth.

Include text only when it’s essential to your experience or brand. Text in icons doesn’t support accessibility or localization, is often too small to read easily, and can make an icon appear cluttered. In some contexts, your app name already appears nearby, making it redundant to display the name within the icon itself. Although displaying a mnemonic like the first letter of your app’s name can help people recognize your app or game, avoid including nonessential words that tell people what to do with it — like “Watch” or “Play” — or context-specific terms like “New” or “For visionOS.” If you include text in a tvOS app icon, make sure it’s above other layers so it’s not cropped by the parallax effect.

Prefer illustrations to photos and avoid replicating UI components. Photos are full of details that don’t work well when displayed in different appearances, viewed at small sizes, or split into layers. Instead of using photos, create a graphic representation of the content that emphasizes the features you want people to notice. Make sure to avoid extremely thin line weights and sharp corners, because they tend to lose detail and crispness in smaller icon sizes at lower resolutions. If your app has an interface that people recognize, don’t just replicate standard UI components or use app screenshots in your icon.

Don’t use replicas of Apple hardware products. Apple products are copyrighted and can’t be reproduced in your app icons.

### Visual effects

Let the system handle blurring and other visual effects. The system dynamically applies visual effects to your app icon layers, so there’s no need to include specular highlights, drop shadows between layers, beveled edges, blurs, glows, and other effects. In addition to interfering with system-provided effects, custom effects are static, whereas the system supplies dynamic ones. If you do include custom visual effects on your icon layers, use them intentionally and test carefully with Icon Composer, on a simulated device in Device Hub, or on a physical device to make sure they appear as expected and don’t conflict with system effects.

Create layer groupings to apply effects to multiple layers at once. System effects typically occur on individual layers. If it makes sense for your design, however, you can group several layers together in Icon Composer or your design tool so effects occur at the group level. For a group, Icon Composer provides additional customization options for Liquid Glass effects, so you can configure attributes like specular highlights, refraction, and translucency.

### Appearances

In iOS, iPadOS, and macOS, people can choose whether their Home Screen app icons are default, dark, clear, or tinted in appearance. For example, someone may want to personalize their app icon appearance to complement their wallpaper. You can design app icon variants for every appearance variant, and the system automatically generates variants you don’t provide.



Keep your icon’s features consistent across appearances. To create a seamless experience, keep your icon’s core visual features the same in the default, dark, clear, and tinted appearances. Avoid creating custom icon variants that swap elements in and out with each variant, which may make it harder for people to find your app when they switch appearances.

Design dark and tinted icons that feel at home beside system app icons and widgets. You can preserve the color palette of your default icon, but be mindful that dark icons are more subdued, and clear and tinted icons are even more so. A great app icon is visible, legible, and recognizable, regardless of its appearance variant.

Use your light app icon as the basis for your dark icon. Choose complementary colors that reflect the default design, and avoid excessively bright images. Color backgrounds generally offer the greatest contrast in dark icons. For guidance, see Dark Mode.

Consider offering alternate app icons. In iOS, iPadOS, tvOS, and compatible apps running in visionOS, it’s possible to let people visit your app’s settings to choose an alternate version of your app icon. For example, a sports app might offer icons for different teams, letting someone choose their favorite. If you offer this capability, make sure each icon you design remains closely related to your content and experience. Avoid creating one someone might mistake for another app.

[Note]

Note: Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants. As with your default app icon, all alternate and variant icons are subject to app review and must adhere to the App Review Guidelines.

### Platform considerations

No additional considerations for iOS, iPadOS, or macOS.

#### tvOS

Include a safe zone to ensure the system doesn’t crop your content. When someone focuses your app icon, the system may crop content around the edges as the icon scales and moves. To ensure that your icon’s content is always visible, keep a safe zone around it. Be aware that the safe zone can vary, depending on the image size, layer depth, and motion, and the system crops foreground layers more than background layers.



#### visionOS

Avoid adding a shape that’s intended to look like a hole or concave area to the background layer. The system-added shadow and specular highlights can make such a shape stand out instead of recede.

#### watchOS

Avoid using black for your icon’s background. Lighten a black background so the icon doesn’t blend into the display background.

### Specifications

The layout, size, style, and appearances of app icons vary by platform.

| Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |

| iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |

| tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |

| visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |

| watchOS | Square | Circular | 1088x1088 px | Layered | N/A |

The system automatically scales your icon to produce smaller variants that appear in certain locations, such as Settings and notifications.

App icons support the following color spaces:

- sRGB (color)

- Gray Gamma 2.2 (grayscale)

- Display P3 (wide-gamut color in iOS, iPadOS, macOS, tvOS, and watchOS only)

### Resources

##### Related

Apple Design Resources

Icon Composer

Icons

Images

Dark Mode

##### Developer documentation

Creating your app icon using Icon Composer

Configuring your app icon using an asset catalog

##### Videos

- Say hello to the new look of app icons: Get an overview of the new app icon appearances for iOS, iPadOS, and macOS, including light and dark tints, and clear options. Learn how to use frostiness and translucency to make your app icon more vibrant, dynamic, and expressive, and find out how to ensure your icon works well with specular highlights.

- Create icons with Icon Composer: Learn how to use Icon Composer to make updated app icons for iOS, iPadOS, macOS, and watchOS. Find out how to export assets from your design tool of choice, add them to Icon Composer, apply real-time glass properties and other effects, and preview and adjust for different platforms and appearance modes.

### Change log

| Date | Changes |

| October 28, 2026 | Added guidance for app icon format options. |

| June 8, 2026 | Refined guidance for Liquid Glass. |

| June 9, 2025 | Updated guidance to reflect layered icons, consistency across platforms, and best practices for Liquid Glass. |

| June 10, 2024 | Added guidance for creating dark and tinted app icon variants for iOS and iPadOS. |

| January 31, 2024 | Clarified platform availability for alternate app icons. |

| June 21, 2023 | Updated to include guidance for visionOS. |

| September 14, 2022 | Added specifications for Apple Watch Ultra. |

=== SOURCE: https://developer.apple.comdoc://com.apple.HIG/design/Human-Interface-Guidelines/launching
# Launching

A streamlined launch experience helps people start using your app or game immediately.



Launching begins when someone opens your app or game, includes an initial download, and ends when the first screen is ready. After launching completes, you might offer an onboarding experience, which can give people a high-level view of your app or game.

### Best practices

Launch instantly. People want to start interacting with your app or game right away, and sometimes they don’t want to wait more than a couple of seconds.

If the platform requires it, provide a launch screen. In iOS, iPadOS, and tvOS, the system displays your launch screen the moment your app or game starts and quickly replaces it with your first screen, giving people the impression that your experience is fast and responsive. For guidance, see Launch screens. macOS, visionOS, and watchOS don’t require launch screens.

If you need a splash screen, consider displaying it at the beginning of your onboarding flow. A splash screen is a beautiful graphic that succinctly communicates branding and other information you need to provide. If you don’t provide an onboarding experience, you might display your splash screen as soon as launching completes.

Restore the previous state when your app restarts so people can continue where they left off. Avoid making people retrace steps to reach their previous location in your app or game. Restore granular details of the previous state as much as possible. For example, scroll the view to people’s most recent position, and display windows in the same state and location in which people left them.

### Launch screens

Not applicable for macOS, visionOS, or watchOS.

Downplay the launch experience. A launch screen isn’t part of an onboarding experience or a splash screen, and it isn’t an opportunity for artistic expression. A launch screen’s sole function is to enhance the perception of your experience as quick to launch and immediately ready to use.

Design a launch screen that’s nearly identical to the first screen of your app or game. If you include elements that look different when launching completes, people may experience an unpleasant flash between the launch screen and your first screen. If your app or game displays a solid color before transitioning to the first screen, create a launch screen that displays only that solid color. Also make sure that your launch screen matches the device’s current orientation and appearance mode.

Avoid including text on your launch screen, even if your first screen displays text. Because the content in a launch screen doesn’t change, any text you display won’t be localized.

Don’t advertise. The launch screen isn’t a branding opportunity. Avoid creating a screen that looks like a splash screen or an “About” window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen.

### Platform considerations

No additional considerations for macOS or watchOS.

#### iOS, iPadOS

Launch in the appropriate orientation. If your app or game supports both portrait and landscape modes, launch using the device’s current orientation. If your interface only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only interface responds correctly, regardless of whether people enter landscape orientation by rotating the device left or right. For guidance, see Layout.

#### tvOS

[Note]

Note: Unlike the layered images throughout much of a tvOS app, the launch screen is static.

In a live-viewing app, consider automatically starting playback soon after people start the app. People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see Live-viewing apps.

#### visionOS

Consider launching in the Shared Space even if your app is fully immersive. Opening a window in the Shared Space lets you provide more context about your app or game while giving it time to load, and it also lets you present a control that people can use to open your fully immersive experience. In general, people appreciate being able to choose when to transition to a Full Space, especially if they’re currently running other apps in the Shared Space. For guidance, see Immersive experiences.

### Resources

##### Related

Onboarding

Loading

##### Developer documentation

Specifying your app’s launch screen — Xcode

Responding to the launch of your app — UIKit

##### Videos

- Optimizing App Launch: Slow app launches are frustrating. Learn about the new app launch instrument and discover how to make your app launch fast. Gain insights into what happens during app launch and how to minimize, prioritize, and optimize work at this critical time. Hear tips and tricks from the engineers making iOS apps launch fast.

- Love at First Launch: Engage people from the first moment they open your app, and keep them coming back for more. Learn tips on how to make a compelling first impression, methods for teaching new users about your app, and best practices when asking users for more information.

### Change log

| Date | Changes |

| June 10, 2024 | Added guidance on displaying a splash screen. |

| June 21, 2023 | Updated to include guidance for visionOS. |

=== SOURCE: https://developer.apple.comdoc://com.apple.HIG/design/Human-Interface-Guidelines/managing-accounts
# Managing accounts

When it doesn’t create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.



Ask people to create an account only if your core functionality requires it; otherwise, let people enjoy your app or game without one. If you require an account, consider using Sign in with Apple to give people a consistent sign-in experience they can trust and the convenience of not having to remember multiple accounts and authentication methods.

### Best practices

Explain the benefits of creating an account and how to sign up. If your app or game requires an account, write a brief, friendly description of the reasons for the requirement and its benefits. Display this message in your sign-in view.

Delay sign-in for as long as possible. People often abandon apps when they’re forced to sign in before they can do anything useful. To help avoid this situation, give people a chance to get a sense of what your app or game does before asking them to make a commitment to it. For example, a shopping app might let people browse as much as they want, requiring sign-in only when they’re ready to make a purchase.

If you don’t use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey. Passkeys simplify account creation and authentication, eliminating the need for people to create or enter passwords. When an app supports passkeys, people simply provide their user name when creating a new account or signing in to an existing one. For developer guidance, see Supporting passkeys. If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see Securing Logins with iCloud Keychain Verification Codes).

Always identify the authentication method you offer. For example, if you display a button for signing in to your app with Face ID, title it using a phrase like “Sign In with Face ID” instead of a generic phrase like “Sign In.”

Refer only to authentication methods that are available in the current context. For example, don’t reference Face ID on a device that doesn’t offer it. Check the device’s capabilities and use the appropriate terminology. For developer guidance, see LABiometryType.

In general, avoid offering an app-specific setting for opting in to biometric authentication. People turn on biometric authentication at the system level, so presenting an in-app setting is redundant and could be confusing.

Avoid using the term passcode to refer to account authentication. People create a passcode to unlock their device or authenticate for Apple services. If you use the term in your interface, people might think you’re asking them to reuse their passcode in your app or game.

### Deleting accounts

If you help people create an account within your app or game, you must also help them delete it, not just deactivate it. In addition to following the guidelines below, be sure to understand and comply with your region’s legal requirements related to account deletion and the right to be forgotten.

[Important]

Important: If legal requirements compel your app to maintain accounts or information — such as digital health records — or to follow a specific account-deletion process, clearly describe the situation so people can understand the information or accounts you must maintain and the process you must follow.

Provide a clear way to initiate account deletion within your app or game. If people can’t perform account deletion within your app, you must provide a direct link to the webpage on which people can do so. Make the link easy to discover — for example, don’t bury it in your Privacy Policy or Terms of Service pages.

[Developer note]

Developer note: If people used Sign in with Apple to create an account within your app, you revoke the associated tokens when they delete their account. See Token revocation.

Provide a consistent account-deletion experience whether people perform it within your app or game or on the website. For example, avoid making one version of the deletion flow longer or more complicated than the other.

Consider letting people schedule account deletion to occur in the future. People can appreciate the opportunity to use their remaining services or wait until their subscription auto-renews before deleting their account. If you offer a way to schedule account deletion, offer an option for immediate deletion as well.

Tell people when account deletion will complete, and notify them when it’s finished. Because it can sometimes take a while to fully delete an account, it’s essential to keep people informed about the status of the deletion process so they know what to expect.

If you support in-app purchases, help people understand how billing and cancellation work when they delete their account. For example, you might need to help people understand the following scenarios:

- Billing for an auto-renewable subscription continues through Apple until people cancel the subscription, regardless of whether they delete their account.

- After they delete their account, people need to cancel their subscription or request a refund.

In addition to helping people understand these scenarios, provide information that describes how to cancel subscriptions and manage purchases. For guidance, see Helping people manage their subscriptions and Providing help.

[Note]

Note: Even if people didn’t use your app to purchase the subscription, you still need to support account deletion.

### TV provider accounts

Many popular TV providers let people sign in to their accounts at the system level, eliminating the need to authenticate on an app-by-app basis. If your TV provider app requires people to sign in, use TV Provider Authentication to provide the most efficient onboarding experience.

Avoid displaying a sign-out option when people are signed in at the system level. If your app must include a sign-out option, invoking it needs to prompt people to navigate to Settings > TV Provider to sign out of their account.

Never instruct people to sign out by adjusting privacy controls. The TV provider controls in Settings > Privacy aren’t a sign-out mechanism. These settings help people manage the apps that can access their TV provider account.

### Platform considerations

No additional considerations for iOS, iPadOS, macOS, or visionOS.

#### tvOS

Most people interact with Apple TV using a remote, not a keyboard, so ask for the minimum amount of information necessary.

Prefer letting people use another device to sign up or authenticate. When you configure your app’s associated domains, Apple TV can work with other devices to safely suggest sign-in credentials, including Sign in with Apple. For developer guidance, see Configuring an associated domain.

When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user. In tvOS 16 and later, your app can share its credentials with all users while storing each individual’s profile and user data separately. When you support this type of sharing, your app can automatically use the current user’s profile without asking each person to sign in separately to a shared account. For developer guidance, see kSecUseUserIndependentKeychain and User Management Entitlement.

Minimize data entry. If you need to gather more than a small amount of information, ask people to visit a website from another device. If you need an email address, show the email keyboard screen, which includes a list of recently entered addresses.

#### watchOS

Use iCloud synchronization to provide access to the Keychain, letting people autofill user names and passwords and preserve app settings.

### Resources

##### Related

Onboarding

Sign in with Apple

##### Developer documentation

Supporting passkeys — Authentication Services

##### Videos

- What’s new in passkeys: Discover how iOS, iPadOS, macOS, and visionOS 26 enhance passkeys. We’ll explore key updates including: the new account creation API for streamlined sign-up, keeping passkeys up-to-date, new ways to drive passkey upgrades through automatic passkey upgrades and passkey management endpoints, and the secure import/export of passkeys. Learn how these improvements enhance user experience and security, and how to implement these updates in your apps to provide a smoother, more secure authentication experience. To get the most out of this video, first watch “Meet passkeys” from WWDC22.

- What’s new in device management: Learn about the latest management capabilities for iOS, iPadOS, macOS, and visionOS, then discover the latest changes to Apple Business Manager and Apple School Manager. We’ll also share updates to Activation Lock, SoftwareUpdate, and Safari management.

=== SOURCE: https://developer.apple.comdoc://com.apple.HIG/design/Human-Interface-Guidelines/privacy
# Privacy

Privacy is paramount: it’s critical to be transparent about the privacy-related data and resources you require and essential to protect the data people allow you to access.



People use their devices in very personal ways and they expect apps to help them preserve their privacy.

When you submit a new or updated app, you must provide details about your privacy practices and the privacy-relevant data you collect so the App Store can display the information on your product page. (You can manage this information at any time in App Store Connect.) People use the privacy details on your product page to make an informed decision before they download your app. To learn more, see App privacy details on the App Store.



### Best practices

Request access only to data that you actually need. Asking for more data than a feature needs — or asking for data before a person shows interest in the feature — can make it hard for people to trust your app. Give people precise control over their data by making your permission requests as specific as possible.

Be transparent about how your app collects and uses people’s data. People are less likely to be comfortable sharing data with your app if they don’t understand exactly how you plan to use it. Always respect people’s choices to use system features like Hide My Email and Mail Privacy Protection, and be sure you understand your obligations with regard to app tracking. To learn more about Apple privacy features, see Privacy; for developer guidance, see User privacy and data use.

Process data on the device where possible. In iOS, for example, you can take advantage of the Apple Neural Engine and custom CreateML models to process the data right on the device, helping you avoid lengthy and potentially risky round trips to a remote server.

Adopt system-defined privacy protections and follow security best practices. For example, in iOS 15 and later, you can rely on CloudKit to provide encryption and key management for additional data types, like strings, numbers, and dates.

### Requesting permission

Here are several examples of the things you must request permission to access:

- Personal data, including location, health, financial, contact, and other personally identifying information

- User-generated content like emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, and audio, video, and photo content

- Protected resources like Bluetooth peripherals, home automation features, Wi-Fi connections, and local networks

- Device capabilities like camera and microphone

- In a visionOS app running in a Full Space, ARKit data, such as hand tracking, plane estimation, image anchoring, and world tracking

- The device’s advertising identifier, which supports app tracking

The system provides a standard alert that lets people view each request you make. You supply copy that describes why your app needs access, and the system displays your description in the alert. People can also view the description — and update their choice — in Settings > Privacy.

Request permission only when your app clearly needs access to the data or resource. It’s natural for people to be suspicious of a request for personal information or access to a device capability, especially if there’s no obvious need for it. Ideally, wait to request permission until people actually use an app feature that requires access. For example, you can use the location button to give people a way to share their location after they indicate interest in a feature that needs that information.

Avoid requesting permission at launch unless the data or resource is required for your app to function. People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it. For example, people understand that a navigation app needs access to their location before they can benefit from it. Similarly, before people can play a visionOS game that lets them bounce virtual objects off walls in their surroundings, they need to permit the game to access information about their surroundings.

Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting. The standard alert displays your copy (called a purpose string or usage description string) after your app name and before the buttons people use to grant or deny their permission. Aim for a brief, complete sentence that’s straightforward, specific, and easy to understand. Use sentence case, avoid passive voice, and include a period at the end. For developer guidance, see Requesting access to protected resources and App Tracking Transparency.

|  | Example purpose string | Notes |

|  | The app records during the night to detect snoring sounds. | An active sentence that clearly describes how and why the app collects the data. |

|  | Microphone access is needed for a better experience. | A passive sentence that provides a vague, undefined justification. |

|  | Turn on microphone access. | An imperative sentence that doesn’t provide any justification. |

Here are several examples of the standard system alert:

#### Pre-alert screens, windows, or views

Ideally, the current context helps people understand why you’re requesting their permission. If it’s essential to provide additional details, you can display a custom screen or window before the system alert appears. The following guidelines apply to custom views that display before system alerts that request permission to access protected data and resources, including camera, microphone, location, contact, calendar, and tracking.

Include only one button and make it clear that it opens the system alert. People can feel manipulated when a custom screen or window also includes a button that doesn’t open the alert because the experience diverts them from making their choice. Another type of manipulation is using a term like “Allow” to title the custom screen’s button. If the custom button seems similar in meaning and visual weight to the allow button in the alert, people can be more likely to choose the alert’s allow button without meaning to. Use a term like “Continue” or “Next” to title the single button in your custom screen or window, clarifying that its action is to open the system alert.

Don’t include additional actions in your custom screen or window, unless needed to obtain a legal consent. For example, don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel.

#### Tracking requests

App tracking is a sensitive issue. In some cases, it might make sense to display a custom screen or window that describes the benefits of tracking. If you want to perform app tracking as soon as people launch your app, you must display the system-provided alert before you collect any tracking data.

Never precede the system-provided alert with a custom screen or window that could confuse or mislead people. People sometimes tap quickly to dismiss alerts without reading them. A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.

There are several prohibited custom-screen designs that will cause rejection. Some examples are offering incentives, displaying a screen or window that looks like a request, displaying an image of the alert, and annotating the screen behind the alert (as shown below). For the avoidance of confusion, a consent screen or window shown before or after an App Tracking Transparency system alert to comply with local privacy laws is allowed. To learn more, see App Review Guidelines: 5.1.1 (iv).

### Location button

In iOS, iPadOS, and watchOS, Core Location provides a button so people can grant your app temporary authorization to access their location at the moment a task needs it. A location button’s appearance can vary to match your app’s UI and it always communicates the action of location sharing in a way that’s instantly recognizable.



The first time people open your app and tap a location button, the system displays a standard alert. The alert helps people understand how using the button limits your app’s access to their location, and reminds them of the location indicator that appears when sharing starts.



After people confirm their understanding of the button’s action, simply tapping the location button gives your app one-time permission to access their location. Although each one-time authorization expires when people stop using your app, they don’t need to reconfirm their understanding of the button’s behavior.

[Note]

Note: If your app has no authorization status, tapping the location button has the same effect as when a person chooses Allow Once in the standard alert. If people previously chose While Using the App, tapping the location button doesn’t change your app’s status. For developer guidance, see LocationButton (SwiftUI) and CLLocationButton (Swift).

Consider using the location button to give people a lightweight way to share their location for specific app features. For example, your app might help people attach their location to a message or post, find a store, or identify a building, plant, or animal they’ve encountered in their location. If you know that people often grant your app Allow Once permission, consider using the location button to help them benefit from sharing their location without having to repeatedly interact with the alert.

Consider customizing the location button to harmonize with your UI. Specifically, you can:

- Choose the system-provided title that works best with your feature, such as “Current Location” or “Share My Current Location.”

- Choose the filled or outlined location glyph.

- Select a background color and a color for the title and glyph.

- Adjust the button’s corner radius.

To help people recognize and trust location buttons, you can’t customize the button’s other visual attributes. The system also ensures a location button remains legible by warning you about problems like low-contrast color combinations or too much translucency. In addition to fixing such problems, you’re responsible for making sure the text fits in the button — for example, button text needs to fit without truncation at all accessibility text sizes and when translated into other languages.

[Important]

Important: If the system identifies consistent problems with your customized location button, it won’t give your app access to the device location when people tap it. Although such a button can perform other app-specific actions, people may lose trust in your app if your location button doesn’t work as they expect.

### Protecting data

Protecting people’s information is paramount. Give people confidence in your app’s security and help preserve their privacy by taking advantage of system-provided security technologies when you need to store information locally, authorize people for specific operations, and transport information across a network.

Here are some high-level guidelines.

Avoid relying solely on passwords for authentication. Where possible, use passkeys to replace passwords. If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see Securing Logins with iCloud Keychain Verification Codes). To further protect access to apps that people keep logged in on their device, use biometric identification like Face ID, Optic ID, or Touch ID. For developer guidance, see Local Authentication.

Store sensitive information in a keychain. A keychain provides a secure, predictable user experience when handling someone’s private information. For developer guidance, see Keychain services.

Never store passwords or other secure content in plain-text files. Even if you restrict access using file permissions, sensitive information is much safer in an encrypted keychain.

Avoid inventing custom authentication schemes. If your app requires authentication, prefer system-provided features like passkeys, Sign in with Apple or Password AutoFill. For related guidance, see Managing accounts.

### Platform considerations

No additional considerations for iOS, iPadOS, tvOS, or watchOS.

#### macOS

Sign your app with a valid Developer ID. If you choose to distribute your app outside the store, signing your app with Developer ID identifies you as an Apple developer and confirms that your app is safe to use. For developer guidance, see Xcode Help.

Protect people’s data with app sandboxing. Sandboxing provides your app with access to system resources and user data while protecting it from malware. All apps submitted to the Mac App Store require sandboxing. For developer guidance, see Configuring the macOS App Sandbox.

Avoid making assumptions about who is signed in. Because of fast user switching, multiple people may be active on the same system.

#### visionOS

By default, visionOS uses ARKit algorithms to handle features like persistence, world mapping, segmentation, matting, and environment lighting. These algorithms are always running, allowing apps and games to automatically benefit from ARKit while in the Shared Space.

ARKit doesn’t send data to apps in the Shared Space; to access ARKit APIs, your app must open a Full Space. Additionally, features like Plane Estimation, Scene Reconstruction, Image Anchoring, and Hand Tracking require people’s permission to access any information. For developer guidance, see Setting up access to ARKit data.

In visionOS, user input is private by design. The system automatically displays hover effects when people look at interactive components you create using SwiftUI or RealityKit, giving people the visual feedback they need without exposing where they’re looking before they tap. For guidance, see Eyes and Gestures > visionOS.

Developer access to device cameras works differently in visionOS than it does in other platforms. Specifically, the back camera provides blank input and is only available as a compatibility convenience; the front camera provides input for spatial Personas, but only after people grant their permission. If the iOS or iPadOS app you’re bringing to visionOS includes a feature that needs camera access, remove it or replace it with an option for people to import content instead. For developer guidance, see Making your existing app compatible with visionOS.

### Resources

##### Related

Entering data

Onboarding

##### Developer documentation

Requesting access to protected resources — UIKit

Security

Requesting authorization to use location services — CoreLocation

App Tracking Transparency

##### Videos

- Meet Trust Insights: Uncover how Trust Insights can help protect people from social scams and coercion. Explore how this new framework uses privacy-preserving machine learning to detect when someone may be coached into risky actions. Find out how to integrate Trust Insights into your app, interpret its signals, and design thoughtful interventions that safeguard people while respecting their privacy.

- Integrate privacy into your development process: Learn how to build privacy into your apps from the planning stages through deployment. We’ll cover practical ways to integrate privacy at each step of the development lifecycle, focusing on data minimization, on-device processing, and transparency and control. You’ll discover how to use Apple’s tools and frameworks to protect user data and create a privacy-respecting app experience. 

- What’s new in passkeys: Discover how iOS, iPadOS, macOS, and visionOS 26 enhance passkeys. We’ll explore key updates including: the new account creation API for streamlined sign-up, keeping passkeys up-to-date, new ways to drive passkey upgrades through automatic passkey upgrades and passkey management endpoints, and the secure import/export of passkeys. Learn how these improvements enhance user experience and security, and how to implement these updates in your apps to provide a smoother, more secure authentication experience. To get the most out of this video, first watch “Meet passkeys” from WWDC22.

### Change log

| Date | Changes |

| June 21, 2023 | Consolidated guidance into new page and updated for visionOS. |

=== SOURCE: https://developer.apple.comdoc://com.apple.HIG/design/Human-Interface-Guidelines/sign-in-with-apple
# Sign in with Apple

Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.



Supporting Sign in with Apple lets people use the Apple Account they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing passwords. In cases where you choose to ask for a name and email address, people have the option to share a unique, random email address that automatically relays messages to their personal email address. For developer guidance, see Authentication Services.

You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.

Sign in with Apple makes it easy for people to authenticate with Face ID, Touch ID, or Optic ID and has two-factor authentication built in for an added layer of security. Apple doesn’t use Sign in with Apple to profile people or their activity in apps.

### Offering Sign in with Apple

Follow these guidelines to offer Sign in with Apple when it’s most convenient for people.

Ask people to sign in only in exchange for value. People need to understand why you’re asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app experience, access additional features, or synchronize data.

Delay sign-in as long as possible. People often abandon apps when they’re forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore available content before signing in to stream something.

If you require an account, ask people to set it up before offering any sign-in options. Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.

Consider letting people link an existing account to Sign in with Apple. When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they’ve already set up. You can offer account linking before or after people sign in to their existing account. For example:

- If people share an email address through Sign in with Apple and it matches the address in an existing account, you can suggest that they link Sign in with Apple to that account.

- If people used an existing user name and password to sign in, you can display an account-linking suggestion in their account’s settings view or another logical place.

In a commerce app, wait until after people make a purchase before asking them to create an account. If you support a guest checkout system, give people a quick way to create an account after the transaction completes. For example, if you support Apple Pay, let people create an account on the order confirmation page. In cases where people have already provided their name and email address during the Apple Pay transaction, you don’t need to ask for this information.



As soon as Sign in with Apple completes, welcome people to their new account. Help people use their new account right away; don’t delay the experience by asking for information that isn’t required.

Indicate when people are currently signed in. You can help people confirm their sign-in method by displaying a phrase like “Using Sign in with Apple” in places like a settings or account interface.

### Collecting data

People appreciate Sign in with Apple for its privacy and convenience. Although some apps or websites may require additional information — such as a date of birth or a region of residence — it’s essential to minimize your requests for data as people set up an account. Build on the trust that people have in Sign in with Apple by describing why you need additional data and clearly displaying the data you receive.

Clarify whether the additional data you request is required or just recommended. If the data is legally or contractually required — such as an agreement to terms of service, country or region of residence, birth date, or information required by a region’s real-identity laws — make sure people understand that they must supply the additional information to complete the setup of their account. If additional data isn’t required but can improve the user experience, make sure people know the request is optional and help them understand the benefits of providing the information.

Don’t ask people to supply a password. A key benefit of Sign in with Apple is that people don’t have to create and memorize additional passwords. Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.

Avoid asking for a personal email address when people supply a private relay address. Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account. It’s essential to respect this choice and avoid overriding it by asking for a personal email address. If you present customer service, retail, or other experiences that request identification via email address, you can:

- Make sure that people can view their private relay address in your app or website

- Direct people to Settings > Apple Account > Password & Security > Apps using Apple Account to retrieve their private relay address

- Use other identifying values, like an order number or phone number collected as part of a purchase

Give people a chance to engage with your app before asking for optional data. As people use your app, you can help them discover places where they can benefit from sharing more information with you. For example, you might suggest that they provide a contact phone number if they want real-time text updates, or social network information if they want to play games with friends. If people choose not to provide optional information, don’t prevent them from accessing their account or using all the features of your app.

Be transparent about the data you collect. People value knowing how you use the data that they share with you. One way you can be transparent is to welcome people by using the name or email address they shared. Doing this helps establish how you use this information and, for a relay address, shows people where to find it in the future. If you don’t display all the data that people provide, they are likely to wonder why you asked for it.

### Displaying buttons

Apple provides several Sign in with Apple buttons you can use to let people set up an account and sign in. If necessary, you can create a custom button to offer Sign in with Apple; for guidelines, see Creating a custom Sign in with Apple button.

Prominently display a Sign in with Apple button. Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button.

#### Using the system-provided buttons

When you use the system-provided APIs to create a Sign in with Apple button, you get the following advantages.

- A button that’s guaranteed to use an Apple-approved appearance

- Assurance that the button’s contents maintain ideal proportions as you change its style

- Automatic translation of the button’s title into the language specified by the device

- Support for configuring the button’s corner radius to match the style of your UI (iOS, macOS, and web)

- A system-provided alternative text label that lets VoiceOver describe the button

For developer guidance, see ASAuthorizationAppleIDButton (iOS, macOS, and tvOS), WKInterfaceAuthorizationAppleIDButton (watchOS), and Displaying Sign in with Apple buttons on the web. You can also visit Sign in with Apple button to view and adjust live previews of web-based buttons and get the code.

The system provides several variants of the button title. Depending on the platform on which your content runs, choose the variant that fits the terminology of your sign-in experience and use it consistently throughout your interfaces.

The following button titles are available for iOS, macOS, tvOS, and the web:

For watchOS, the system provides one title:  Sign in.



Depending on the platform, the system provides up to three options for the appearance of the Sign in with Apple button: white, white with an outline, and black. Choose the appearance that works best with the background on which the button displays.

##### White

The white style is available on all platforms and the web. Use this style on dark backgrounds that provide sufficient contrast.

##### White with outline

The white outlined style is available in iOS, macOS, and the web. Use this style on white or light-color backgrounds that don’t provide sufficient contrast with the white button fill. Avoid using this style on a dark or saturated background, because the black outline can add visual clutter; instead, use the white style to contrast with a dark background.

##### Black

The black style is available on all platforms and the web. Use this style on white or light-color backgrounds that provide sufficient contrast; don’t use it on black or dark backgrounds.

Unlike the black Sign in with Apple button for other platforms, the watchOS button uses a fill color that’s not fully black. To contrast with the pure black background of Apple Watch, the watchOS button uses the system-defined dark gray appearance.



##### Button size and corner radius

Adjust the corner radius to match the appearance of other buttons in your app. By default, the Sign in with Apple button has rounded corners. In iOS, macOS, and the web, you can change the corner radius to produce a button with square corners or a capsule-shape button. For developer guidance, see cornerRadius (iOS and macOS) and Displaying Sign in with Apple buttons on the web.

Maintain the minimum button size and margin around the button in iOS, macOS, and the web. Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.

| Minimum width | Minimum height | Minimum margin |

| 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

#### Creating a custom Sign in with Apple button

If your interface requires it, you can create a custom Sign in with Apple button for iOS, macOS, or the web. For example, you may want to align logos across multiple sign-in buttons, use buttons that display only a logo, or adjust the button’s font, bezel, or background appearance to coordinate with your UI.



Always make sure that people can instantly identify your custom button as a Sign in with Apple button. If your custom button differs too much from the standard one, people may not feel comfortable using it to set up an account or sign in. App Review evaluates all custom Sign in with Apple buttons.

Apple Design Resources provides downloadable Apple logo artwork you can use to create custom Sign in with Apple buttons that display either a logo only or a logo and text. The logo files are available in PNG, SVG, and PDF formats, and the artwork for both types of buttons includes both black and white versions. Here are examples of the black and white logo-only art files, each with a background added for visibility.

All downloadable logo files include padding that simplifies positioning the logo in a button. Logo-only logo files include horizontal and vertical padding that ensures the correct proportion of the logo relative to the button. In addition to padding that keeps the logo and button correctly proportioned, logo files for buttons with text also include horizontal padding that provides a minimum margin between the logo and the button’s leading edge and title.

Use only the logo artwork downloaded from Apple Design Resources; never create a custom Apple logo. As you create a custom Sign in with Apple button, follow these guidelines for using the downloadable logo file:

- Use the logo file to position the Apple logo in a button; never use the Apple logo as a button.

- Match the height of the logo file to the height of the button.

- Don’t crop the logo file.

- Don’t add vertical padding.

To make sure that your custom button is visually consistent with the system-provided Sign in with Apple button, don’t change the following attributes.

- Titles. Use only Sign in with Apple, Sign up with Apple, or Continue with Apple.

- General shape. Buttons that combine the logo with text are always rectangular; logo-only buttons can be circular or rectangular.

- Logo and title colors. Within a button, both items must be either black or white; don’t use custom colors.

To coordinate with your app design, you can change:

- Title font. You can also adjust the font’s weight and size.

- Title case. You can capitalize every letter in the title.

- Background appearance. The overall color needs to remain black or white. If necessary, you can include a subtle texture or gradient to help the button harmonize with your interface.

- Button corner radius. You can use a corner radius value that matches the other buttons in your UI.

- Button bezel and shadow. For example, you can use a stroke to emphasize the button bezel or add a drop shadow.

##### Custom buttons with a logo and text

Choose the format of the logo file based on the height of your button. Because SVG and PDF are vector-based formats, you can use these files in buttons of any height. Use the PNG files only in buttons that are 44 points tall, which is the default (and recommended) button height in iOS. Logos are available in small, medium, and large sizes, so you can match logo sizes in all the sign-up buttons you display.

Prefer the system font for the title — that is, Sign in with Apple, Sign up with Apple, or Continue with Apple. Regardless of the font you choose, the title and button height of your custom button need to use the same proportions that the system uses. Using the system font for example, the title’s font size would be 43% of the button’s height — in other words, the button’s height would be 233% of the title’s font size, rounded to the nearest integer. Here are two examples that show these proportions using different sizes of the system font.





In general, preserve the capitalization style of the title. By default, all variants of the button title capitalize the first word — that is, Sign or Continue — and Apple; all other letters are lowercase. Avoid changing this style unless your interface uses only uppercase.

Keep the title and logo vertically aligned within the button. To do this, vertically align the title to the middle of the button, then add the logo image, making sure its height matches the height of the button. Because the logo image includes top and bottom padding, vertically aligning the title in the button ensures that the title, the logo, and the button stay properly aligned.

Inset the logo if necessary. If you need to horizontally align the Apple logo with other authentication logos, you can adjust the space between the logo and the button’s leading edge.

Maintain a minimum margin between the title and the right edge of the button. Ensure the margin measures at least 8% of the button’s width.

Maintain the minimum button size and margin around the button. Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.

| Minimum width | Minimum height | Minimum margin |

| 140 pt (140 px @1x, 280 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 of the button’s height |

##### Custom logo-only buttons

Choose the format of the logo file based on the size of your button. The downloadable artwork for logo-only buttons is available in SVG, PDF, and PNG formats. Use the vector-based SVG and PDF formats for buttons of any size; use the PNG format only in buttons that measure 44x44 pt.

Don’t add horizontal padding to a logo-only image. A logo-only Sign in with Apple button always has a 1:1 aspect ratio, and the artwork already includes the correct padding on all sides.

Use a mask to change the default square shape of the logo-only image. For example, you might want to use a circular or rounded rectangular shape to present all logo-only sign-in buttons. Never crop the Apple-provided artwork to decrease its built-in padding or use the logo by itself, and avoid including additional padding.

Maintain a minimum margin around the button. Ensure the margin measures at least 1/10 of the button’s height.

### Platform considerations

No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

### Resources

##### Related

Sign in with Apple button

##### Developer documentation

Authentication Services

Displaying Sign in with Apple buttons on the web — Sign in with Apple

##### Videos

- Move beyond passwords: Despite their prevalence, passwords inherently come with challenges that make them poorly suited to securing someone’s online accounts. Learn more about the challenges passwords pose to modern security and how to move beyond them. Explore the next frontier in account security with secure-by-design, public-key-based credentials that use the Web Authentication standard. Discover in this technology preview how Apple is approaching this standard in iOS 15 and macOS Monterey.

- Simplify sign in for your tvOS apps: Find out how people can use Face ID or Touch ID on their iOS or iPadOS device to authorize purchases and sign into your tvOS app. Discover how you can simplify sign in for people using your app and help them get to the content they want to enjoy, faster. We’ll show you how to set up a simplified sign in process and share some best practices about creating great sign in experiences for Apple TV.

To get the most out of this session, we recommend a basic understanding of associated domains and the Authentication Services framework.

- Introducing Sign In with Apple: Sign In with Apple is the fast, easy way for people to sign in to apps using the Apple IDs they already have. Learn how easy it is to add a Sign In with Apple button to your app or website to acquire new customers and benefit from the built-in security, antifraud, and privacy that Sign In with Apple provides.

### Change log

| Date | Changes |

| September 14, 2022 | Refined guidance on supporting existing accounts, helping people set up a new account, and indicating the current sign-in status. Consolidated guidance into one page. |

=== SOURCE: https://developer.apple.comdoc://com.apple.avfoundation/documentation/AVFoundation/requesting-authorization-to-capture-and-save-media
# Requesting authorization to capture and save media

Prompt the user to authorize access to the camera, microphone, and photo library.

### Overview

In iOS and macOS 10.14 and later, the user must explicitly grant permission for each app to access the camera and microphone. Before your app can use a capture device for the first time, the system presents an alert with an app-specific message that you specify, to ask the user to grant your app access to the capture device. For example, the following screenshots show the camera access alert in iOS and macOS 10.14 and later:





The system remembers the user’s response to each access alert, so subsequent uses of the corresponding capture device don’t cause the alert to appear again. The user can change permission settings for your app in Settings > Privacy in iOS and in System Preferences > Security & Privacy in macOS.

This article outlines the steps you can take to ensure your app has permission before it attempts to capture media.

#### Configure access alerts

The system requires that your app provides static messages to display to the user when the system asks for permission to access the camera or microphone:

- If your app uses device cameras, include the NSCameraUsageDescription key in your app’s Info.plist file.

- If your app uses device microphones, include the NSMicrophoneUsageDescription key in your app’s Info.plist file.

For each key, provide a message that explains to the user why your app needs to capture media so the user can feel confident granting permission to your app.



#### Enable entitlements in macOS

In macOS, you also need to enable the following entitlements in Signing & Capabilities for your app targets:

- If your app uses device cameras, enable the Camera entitlement.

- If your app uses device microphones, enable the Audio Input Entitlement.



[Important]

Important:  Your app needs to contain the appropriate key in its Info.plist file, and the appropriate entitlement enabled in macOS, before it requests authorization or attempts to use a capture device. Otherwise, the system terminates your app.

#### Verify and request authorization for capture

Always test the AVCaptureDevice authorizationStatus(for:) method before setting up a capture session. If the user hasn’t granted or denied capture permission, the authorization status is AVAuthorizationStatus.notDetermined. In this case, use the requestAccess(for:completionHandler:) method to tell the system to prompt the user.

Call requestAccess(for:completionHandler:) before starting capture, but only at a time that’s appropriate for your app. For example, if photo or video capture isn’t the main focus of your app, check for permission only when the user invokes your app’s camera-related features. Here’s an example:

var isAuthorized: Bool {
    get async {
        let status = AVCaptureDevice.authorizationStatus(for: .video)
        
        // Determine if the user previously authorized camera access.
        var isAuthorized = status == .authorized
        
        // If the system hasn't determined the user's authorization status,
        // explicitly prompt them for approval.
        if status == .notDetermined {
            isAuthorized = await AVCaptureDevice.requestAccess(for: .video)
        }
        
        return isAuthorized
    }
}

func setUpCaptureSession() async {
    guard await isAuthorized else { return }
    // Set up the capture session.
}

#### Request authorization to save captured media

Your app must get permission to access the photo library before it attempts to save photos or videos; otherwise the system terminates your app. Which permission you request depends on the types of media you want to save:

- For most photo and video capture workflows, including Live Photos and RAW format capture, use the PHPhotoLibrary and PHAssetCreationRequest classes. These classes require read/write access to the photo library, so you need to use the NSPhotoLibraryUsageDescription key in your Info.plist file to provide the user a message to request access. For additional information, see Delivering an Enhanced Privacy Experience in Your Photos App.

- If your app only needs to save video to the photo library, the UISaveVideoAtPathToSavedPhotosAlbum(_:_:_:_:) function is a simpler alternative to PHPhotoLibrary. This function only requires write access to the library. Use the NSPhotoLibraryAddUsageDescription key in your Info.plist file to provide the user a message to request permission to save to the photo library.

[Note]

Note:  The UIImageWriteToSavedPhotosAlbum(_:_:_:_:) function isn’t recommended for use with photos captured with AVCapturePhotoOutput because UIImage doesn’t support the features and metadata included in photo output.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/choosing-the-location-services-authorization-to-request
# Choosing the  Location Services Authorization to Request

Determine the authorization your app needs to access location data.

### Overview

The authorization status that your app has determines if and when it receives location events. There are two types of authorization your app can request:

When In Use: Your app can use all location services and receive events while the app is in use. In general, iOS apps are considered in use when they’re in the foreground or running in the background with the background location usage indicator enabled.

Always: Your app can use all location services and receive events even if the user is not aware that your app is running. If your app isn’t running, the system launches your app and delivers the event.

#### Prefer When In Use Authorization

Whenever possible, request only When In Use authorization. This mode has powerful features, allowing your app to:

- Access all available location services while the user is using the app. If the user stops using your app, any outstanding requests suspend until the user resumes using your app.

- Continue to get location updates even after your app enters the background, if you’ve enabled background location updates in your Xcode project. See Handling location updates in the background for more information.

- Use location notification triggers to launch. If your app can rely on your user’s interaction, set up a UNLocationNotificationTrigger to notify users when they enter a relevant region. When users click through the notification, the system launches the app, making it eligible to receive the location event. This method lets users decide at a relevant moment whether to share their location with your app.

Location services are available to apps with CLAuthorizationStatus.authorizedWhenInUse only while the app is “in use”. On all platforms that support When In Use authorization, an app is considered in use:

- When the app runs in the foreground.

- In the few seconds after an app leaves the foreground, a short grace period for your app to finish any current location tasks the user initiated.

- When the app shows the background location usage indicator (showsBackgroundLocationIndicator). On iOS, the indicator is a blue bar or pill at the top of the screen; on watchOS it’s a small icon.

For watchOS, the system always considers a complication on the current watch face to be in use. However, while the complication can receive location updates, you request authorization prompts from the main watch app. On watchOS there’s no way to opt out of showing the background location usage indicator.

#### Ask for Always Authorization

Your app might require Always authorization in some situations where users can’t or don’t want to engage with your app every time you need location information. You may need to ask for Always authorization if:

- Your app performs automated tasks during which a prompt might be inconvenient or undesirable. For example, if your app triggers automatic actions when the user enters a location, such as turning on the lights, your app may require Always authorization.

- Your app records numerous locations throughout the day, such as for a diary app. The user may prefer to allow Always authorization so your app can record locations even when it’s not in use, and without prompting the user.

Keep in mind that asking for authorization doesn’t guarantee your app will receive it. If you request Always authorization, the user has the option of granting your app When In Use authorization instead. You must always be prepared to run with When In Use authorization.

[Note]

Note:  If your app requests and receives When In Use authorization, you can make a separate request for Always authorization later. However, apps may make only one request for Always authorization.

While all platforms support When In Use authorization, the availability and functionality of Always authorization varies, as follows:

tvOS: Only supports When In Use authorization

watchOS: Typically, apps only need When In Use authorization. The watch face context is effectively always in use; if you’re developing a complication, your app likely needs only When In Use authorization. Core location API doesn’t provide launching behavior for watchOS.

macOS: Core Location automatically prompts the user for permission when you start any location service; you don’t have to request authorization. Users can either allow or deny authorization. When In Use and Always authorizations are functionally equivalent.

Mac Catalyst: Your UIKit code can and should request the authorization that makes sense on iOS; the same choice will work when the app runs on the Mac. When In Use and Always authorizations are functionally equivalent on the Mac.

iOS: Supports When In Use and Always authorization.

#### Request Authorization for Apps Running in iOS 12 and Earlier

Apps compiled with iOS 13 or later SDKs but running in iOS 12 or earlier will exhibit behavior consistent with iOS 12 for When In Use authorization. Specifically, in iOS 12 or earlier, some location services are only available to apps with Always authorization, as shown in this table:

| Service | When In Use | Always |

| Standard location service | Supported | Supported |

| Significant-change location service | Not available | Supported |

| Visits service | Not available | Supported |

| Region monitoring | Not available | Supported |

| iBeacon ranging | Supported | Supported |

| Heading service | Supported | Supported |

| Geocoding services | Supported | Supported |

## Location

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/BGTaskSchedulerPermittedIdentifiers
# BGTaskSchedulerPermittedIdentifiers

An array of strings containing developer-specified task identifiers in reverse URL notation.

iOS 13.0, iPadOS 13.0, tvOS 13.0, visionOS 1.0

name: BGTaskSchedulerPermittedIdentifiers

ideTitle: Permitted background task scheduler identifiers

titleStyle: symbol

string 

## Related Documentation

- BGTaskScheduler: A class for scheduling tasks that add background support to your app’s most critical work.

## Background execution

- UIBackgroundModes: Services provided by an app that require it to run in the background.

- WKBackgroundModes: The services a watchOS app provides that require it to continue running in the background.

- LSBackgroundOnly: A Boolean value indicating whether the app runs only in the background.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppTransportSecurity/NSAllowsArbitraryLoads
# NSAllowsArbitraryLoads

A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.

iOS 9.0, iPadOS 9.0, macOS 10.11, visionOS 1.0

name: NSAllowsArbitraryLoads

ideTitle: Allow Arbitrary Loads

titleStyle: symbol

boolean

### Discussion

Set this key’s value to YES to disable App Transport Security (ATS) restrictions for all domains not specified in the NSExceptionDomains dictionary. Domains you specify in that dictionary aren’t affected by this key’s value.

[Important]

Important:  You must supply a justification during App Store review if you set the key’s value to YES, as described in Provide Justification for Exceptions. Use this key with caution because it significantly reduces the security of your app. In most cases, it’s better to upgrade your servers to meet the requirements imposed by ATS, or at least to use a narrower exception.

Disabling ATS means that unsecured HTTP connections are allowed. HTTPS connections are also allowed, and are still subject to default server trust evaluation, as described in Ensure the Network Server Meets Minimum Requirements. However, extended security checks—like requiring a minimum Transport Layer Security (TLS) protocol version—are disabled. Without ATS, you’re also free to loosen the default server trust requirements, as described in Performing manual server trust authentication.

In iOS 10 and later and macOS 10.12 and later, the value of the NSAllowsArbitraryLoads key is ignored—and the default value of NO used instead—if any of the following keys are present in your app’s Information Property List file:

- NSAllowsArbitraryLoadsForMedia

- NSAllowsArbitraryLoadsInWebContent

- NSAllowsLocalNetworking

For more information about how the OS version affects ATS behavior, see the NSAppTransportSecurity key’s Versioning section.

## Global Exceptions

- NSAllowsArbitraryLoadsForMedia: A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework.

- NSAllowsArbitraryLoadsInWebContent: A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views.

- NSAllowsLocalNetworking: A Boolean value that indicates whether to allow local resources to load.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppTransportSecurity/NSExceptionDomains
# NSExceptionDomains

Custom App Transport Security (ATS) configurations for named domains.

iOS 9.0, iPadOS 9.0, macOS 10.11, visionOS 1.0

name: NSExceptionDomains

ideTitle: Exception Domains

titleStyle: symbol

dictionary

### Discussion

The value for this key is a dictionary with keys that name specific domains, IP addresses, or IP address ranges for which you want to set exceptions. The value for each domain key is another dictionary that indicates the exceptions for that domain.

NSExceptionDomains : Dictionary {
    <domain-name-or-ip-address-string> : Dictionary {
        NSIncludesSubdomains : Boolean
        NSExceptionAllowsInsecureHTTPLoads : Boolean
        NSExceptionMinimumTLSVersion : String
        NSExceptionRequiresForwardSecrecy : Boolean
    }
}

Follow these rules when setting a domain name string:

- Use lowercase — Use example.com, not EXAMPLE.COM.

- Use a DNS domain name, IP address, or range of IP addresses — In iOS 17, iPadOS 17, and macOS 14, you can use an IPv4 address, for example 192.168.42.63, or an IPv6 address, for example 2001:db8:12::34. You can also use a classless inter-domain routing (CIDR) range, for example 2001:db8:12::/48. For information about how ATS handles IP addresses, see NSAllowsLocalNetworking.

[Note]

Note:  If you exclude a DNS domain name and your app contacts a host by IP address, the ATS exclusion for the domain name doesn’t apply to the connection even if a DNS query for the domain name would resolve to the IP address. If you exclude an IP address and your app contacts a host by DNS name that resolves to that IP address, the ATS exclusion for the IP address doesn’t apply to the connection.

- Don’t include a port number — Use example.com, not example.com:443.

- Don’t include a trailing dot, unless you only want to match a domain string with a trailing dot — For example, example.com. (with a trailing dot) matches “example.com.” but not “example.com”. Similarly, example.com matches “example.com” but not “example.com.”.

- Don’t use wildcard domains — Don’t use *.example.com. Instead, use example.com and set NSIncludesSubdomains to YES.

The values for the keys in each individual domain’s dictionary control how ATS treats connections made to that domain.

[Note]

Note:  If you specify an exception domain dictionary, ATS ignores any global configuration keys, like NSAllowsArbitraryLoads, for that domain. This is true even if you leave the domain-specific dictionary empty and rely entirely on its keys’ default values.

## Subdomains

- NSIncludesSubdomains: A Boolean value that indicates whether to extend the configuration to subdomains of the given domain.

## Exceptions

- NSExceptionAllowsInsecureHTTPLoads: A Boolean value indicating whether to allow insecure HTTP loads.

- NSExceptionMinimumTLSVersion: The minimum Transport Layer Security (TLS) version for network connections.

- NSExceptionRequiresForwardSecrecy: A Boolean value indicating whether to override the perfect forward secrecy requirement.

- NSRequiresCertificateTransparency: An obsolete Boolean value indicating whether to require Certificate Transparency.

- NSExceptionRequiresNIAPTLSPackageVersion: A string that indicates the version to use for the NIAP Functional Package for TLS, applied to an exception domain.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppTransportSecurity
# NSAppTransportSecurity

A description of changes made to the default security for HTTP connections.

iOS 9.0, iPadOS 9.0, macOS 10.11, visionOS 1.0

name: NSAppTransportSecurity

ideTitle: App Transport Security Settings

titleStyle: symbol

dictionary

### Discussion

On Apple platforms, a networking feature called App Transport Security (ATS) improves privacy and data integrity for all apps and app extensions. ATS requires that all HTTP connections made with the URL Loading System—typically using the URLSession class—use HTTPS. It further imposes extended security checks that supplement the default server trust evaluation prescribed by the Transport Layer Security (TLS) protocol. ATS blocks connections that fail to meet minimum security specifications. For additional details, see Preventing Insecure Network Connections.

You can circumvent or augment these protections by adding the NSAppTransportSecurity key to your app’s Information Property List file and providing an ATS configuration dictionary as the value. For example, you can:

- Allow insecure loads for web views while maintaining ATS protections elsewhere in your app using the NSAllowsArbitraryLoadsInWebContent key.

- Enable additional security features like Certificate Transparency using the NSRequiresCertificateTransparency key, or Certificate Pinning using the NSPinnedDomains key.

- Reduce or remove security requirements for communication with particular servers using the NSExceptionDomains key.

[Important]

Important:  Always look for ways to improve server security before adding ATS exceptions. Loosening ATS restrictions reduces the security of your app.

All keys in the ATS configuration dictionary are optional, with default values that are suitable for most apps. Keys that define global exceptions apply to all network connections made by your app, except connections to domains specified in the NSExceptionDomains sub-dictionary. That sub-dictionary allows you to separately manage settings for individual domains.

#### Versioning

ATS operates by default for apps linked against the iOS 9.0 or macOS 10.11 SDKs or later. When you link your app against an older SDK, ATS is disabled no matter which version of operating system your app runs on.

If you specify a value for any of the global exceptions besides NSAllowsArbitraryLoads, then the ATS behavior depends on the version of the OS on which your app runs:

iOS 9.0 or macOS 10.11: ATS uses the NSAllowsArbitraryLoads value that you set, or NO by default, and ignores the other global exceptions.

iOS 10.0 or later or macOS 10.12 or later: ATS ignores the NSAllowsArbitraryLoads value that you set and instead obeys the other key or keys.

This behavior enables you to manage differences between OS versions. You provide a coarse exception (NSAllowsArbitraryLoads) for older versions, and a more targeted exception, like NSAllowsArbitraryLoadsInWebContent, for when it’s available.

## Global Exceptions

- NSAllowsArbitraryLoads: A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.

- NSAllowsArbitraryLoadsForMedia: A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework.

- NSAllowsArbitraryLoadsInWebContent: A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views.

- NSAllowsLocalNetworking: A Boolean value that indicates whether to allow local resources to load.

## Domain-Specific Exceptions

- NSExceptionDomains: Custom App Transport Security (ATS) configurations for named domains.

## Certificate Pinning

- NSPinnedDomains: A collection of certificates that App Transport Security expects when connecting to named domains.

## TLS Functionality Package Compliance

- NSRequiresNIAPTLSPackageVersion: A string that indicates the version to use for the NIAP Functional Package for TLS.

- NSExceptionRequiresNIAPTLSPackageVersion: A string that indicates the version to use for the NIAP Functional Package for TLS, applied to an exception domain.

## Related Documentation

- Preventing Insecure Network Connections: Enforce secure network links in your app by relying on App Transport Security.

## Network

- NSAdvertisingAttributionReportEndpoint: The URL where Private Click Measurement and SKAdNetwork send attribution information.

- NSBonjourServices: Bonjour service types browsed by the app.

- CKSharingSupported: A Boolean value that indicates your app supports CloudKit Sharing.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/UIBackgroundModes
# UIBackgroundModes

Services provided by an app that require it to run in the background.

iOS 4.0, iPadOS 4.0, visionOS 1.0, watchOS 4.0

name: UIBackgroundModes

ideTitle: Required background modes

titleStyle: symbol

string 

## Possible Values

### audio

### bluetooth-central

### bluetooth-peripheral

### external-accessory

### fetch

### location

### nearby-interaction

### network-authentication

### newsstand-content

### processing

### push-to-talk

### remote-notification

### screen-capture

### voip

### Discussion

To add this key to your Information Property List, enable the Background Modes capability in Xcode. For information on configuring background execution modes and the platforms that support them, see Configuring background execution modes.

## Background execution

- WKBackgroundModes: The services a watchOS app provides that require it to continue running in the background.

- BGTaskSchedulerPermittedIdentifiers: An array of strings containing developer-specified task identifiers in reverse URL notation.

- LSBackgroundOnly: A Boolean value indicating whether the app runs only in the background.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/UILaunchScreen
# UILaunchScreen

The user interface to show while an app launches.

iOS 14.0, iPadOS 14.0

name: UILaunchScreen

ideTitle: Launch Screen

titleStyle: symbol

dictionary

### Discussion

You use this key to define the launch screen that the system displays while your app launches. If you need to provide different launch screens in response to being launched by different URL schemes, use UILaunchScreens instead.

[Note]

Note:  Use this key to configure the user interface during app launch in a way that doesn’t rely on storyboards. If you prefer to use storyboards, use UILaunchStoryboardName instead.

## Main Interface

- UIColorName: The name of a color to use as the background color on the launch screen.

- UIImageName: The name of an image to display during app launch.

- UIImageRespectsSafeAreaInsets: A Boolean that specifies whether the launch image should respect the safe area insets.

## Border Elements

- UINavigationBar: Navigation bar visibility and configuration during launch.

- UITabBar: Tab bar visibility and configuration during launch.

- UIToolbar: Toolbar visibility and configuration during launch.

## Launch interface

- UILaunchScreens: The user interfaces to show while an app launches in response to different URL schemes.

- UILaunchStoryboardName: The filename of the storyboard from which to generate the app’s launch image.

- UILaunchStoryboards: The launch storyboard to use to generate a launch image when your app opens from a supported scheme.

- LSUIPresentationMode: The initial user-interface mode for the app.

- UILaunchToFullScreenByDefaultOnMac: A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/UILaunchStoryboardName
# UILaunchStoryboardName

The filename of the storyboard from which to generate the app’s launch image.

iOS 9.0, iPadOS 9.0, tvOS 9.0, watchOS 2.0

name: UILaunchStoryboardName

ideTitle: Launch screen interface file base name

titleStyle: symbol

string

### Discussion

Specify the name of the storyboard file without the filename extension. For example, if the filename of your storyboard is LaunchScreen.storyboard, specify “LaunchScreen” as the value for this key.

If you prefer to configure your app’s launch screen without storyboards, use UILaunchScreen instead.

## Launch interface

- UILaunchScreen: The user interface to show while an app launches.

- UILaunchScreens: The user interfaces to show while an app launches in response to different URL schemes.

- UILaunchStoryboards: The launch storyboard to use to generate a launch image when your app opens from a supported scheme.

- LSUIPresentationMode: The initial user-interface mode for the app.

- UILaunchToFullScreenByDefaultOnMac: A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/protected-resources
# Protected resources

Control an app’s access to protected system services and user data.

### Overview

Before your app can access certain protected resources, like the Bluetooth interface, location information, or the user’s photos, the system asks the user for permission on behalf of your app. The prompt that the system displays includes a UsageDescription string you provide, explaining why your app needs to access the protected resource. Enter the string in the Signing and Capabilities editor for your app’s target, as described in Requesting access to protected resources. Xcode adds the string as the value for the relevant Information Property List key in your app’s build settings. The topics below list the keys you use to provide usage-description strings for protected resources.

## Essentials

- Requesting access to protected resources: Provide a purpose string that explains to a person why you need access to protected resources on their device.

- Inspecting app activity data: Verify that your app accesses only the user data and network resources that you expect it to access.

- Resetting access to protected resources in macOS: Use Terminal to remove your app’s authorization access to protected resources during testing.

## Bluetooth

- NSBluetoothAlwaysUsageDescription: A message that tells people why the app needs access to Bluetooth.

- NSBluetoothPeripheralUsageDescription: A message that tells people why the app is requesting the ability to connect to Bluetooth peripherals.

## Calendar and reminders

- NSCalendarsFullAccessUsageDescription: A message that tells people why the app is requesting access to read and write their calendar data.

- NSCalendarsWriteOnlyAccessUsageDescription: A message that tells people why the app is requesting access to create calendar events.

- NSRemindersFullAccessUsageDescription: A message that tells people why the app is requesting access to read and write their reminders data.

- Accessing the event store: Request access to a person’s calendar data through the event store.

## Camera and sound

- Requesting authorization to capture and save media: Prompt the user to authorize access to the camera, microphone, and photo library.

- Requesting Authorization for Media Capture on macOS: Prompt the user to authorize access to the camera and microphone.

- NSAudioCaptureUsageDescription: A message that tells people why your app is requesting access to capture system audio on macOS.

- NSCameraUsageDescription: A message that tells people why the app is requesting access to the device’s camera.

- NSMainCameraUsageDescription: A message that tells people why the app is requesting access to the device’s main camera.

- NSMicrophoneUsageDescription: A message that tells people why the app is requesting access to the device’s microphone.

## Contacts

- Accessing the contact store: Request permission from the person to read and write their contact data.

- NSContactsUsageDescription: A message that tells people why the app is requesting access to their contacts.

## Face ID

- Logging a User into Your App with Face ID or Touch ID: Supplement your own authentication scheme with biometric authentication, making it easy for users to access sensitive parts of your app.

- NSFaceIDUsageDescription: A message that tells people why the app is requesting the ability to authenticate with Face ID.

## Files and folders

- NSDesktopFolderUsageDescription: A message that tells people why the app needs access to their Desktop folder.

- NSDocumentsFolderUsageDescription: 

- NSDownloadsFolderUsageDescription: A message that tells people why the app needs access to the user’s Downloads folder.

- NSNetworkVolumesUsageDescription: A message that tells people why the app needs access to files on a network volume.

- NSRemovableVolumesUsageDescription: A message that tells people why the app needs access to files on a removable volume.

- NSFileProviderDomainUsageDescription: A message that tells people why the app needs access to files managed by a file provider.

- NSFileProviderPresenceUsageDescription: A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

## Game Center

- NSGKFriendListUsageDescription: A message that tells people why the app needs access to their Game Center friends list.

## Health

- Setting up HealthKit: Set up and configure your HealthKit store.

- NSHealthClinicalHealthRecordsShareUsageDescription: A message to the user that explains why the app requested permission to read clinical records.

- NSHealthShareUsageDescription: A message that explains to people why the app requests permission to read samples from the HealthKit store.

- NSHealthUpdateUsageDescription: A message to the user that explains why the app requested permission to save samples to the HealthKit store.

- NSHealthRequiredReadAuthorizationTypeIdentifiers: The clinical record data types that your app must get permission to read.

## Home

- Enabling HomeKit in your app: Declare your app’s intention to use HomeKit, and get permission from the user to access home automation accessories.

- NSHomeKitUsageDescription: A message that tells people why the app is requesting access to their HomeKit configuration data.

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

## MediaPlayer

- Requesting Access to Apple Music Library: Prompt the customer to authorize access to Apple Music library.

- NSAppleMusicUsageDescription: A message that tells people why the app is requesting access to their media library.

## Messages

- NSCriticalMessagingUsageDescription: A message that tells people why the app needs to send SMS messages.

## Motion

- NSMotionUsageDescription: A message that tells people why the app is requesting access to the device’s motion data.

- NSFallDetectionUsageDescription: A message to the user that explains the app’s request for permission to access fall detection event data.

## Networking

- NSLocalNetworkUsageDescription: A message that tells people why the app is requesting access to the local network.

- NSNearbyInteractionUsageDescription: A request for user permission to begin an interaction session with nearby devices.

- NSNearbyInteractionAllowOnceUsageDescription: A one-time request for user permission to begin an interaction session with nearby devices.

## NFC

- NFCReaderUsageDescription: A message that tells people why the app is requesting access to the device’s NFC hardware.

## Photos

- Delivering an Enhanced Privacy Experience in Your Photos App: Adopt the latest privacy enhancements to deliver advanced user-privacy controls.

- NSPhotoLibraryAddUsageDescription: A message that tells people why the app is requesting add-only access to their photo library.

- NSPhotoLibraryUsageDescription: A message that tells people why the app is requesting access to their photo library.

## Scripting

- NSAppleScriptEnabled: A Boolean value indicating whether AppleScript is enabled.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

## Sensors

- NSSensorKitUsageDescription: A short description of the purpose of your app’s research study.

- NSSensorKitUsageDetail: A dictionary that includes keys for the specific information your app collects.

- NSSensorKitPrivacyPolicyURL: A hyperlink to a webpage that displays the privacy policy for your app’s research study.

## Siri

- Requesting Authorization to Use Siri: Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.

- NSSiriUsageDescription: A message that tells people why the app is requesting to send user data to Siri.

## Speech

- Asking Permission to Use Speech Recognition: Ask the user’s permission to perform speech recognition using Apple’s servers.

- NSSpeechRecognitionUsageDescription: A message that tells people why the app is requesting to send user data to Apple’s speech recognition servers.

## System Extensions

- NSSystemExtensionUsageDescription: A message that tells people why the app is trying to install a system extension bundle.

- OSBundleUsageDescription: A message that tells people why the app is trying to install a driver extension bundle.

## TV

- NSVideoSubscriberAccountUsageDescription: A message that tells people why the app is requesting access to their TV provider account.

## Vision

- NSWorldSensingUsageDescription: A message that tells people why the app is requesting access to image tracking, plane detection, or scene reconstruction.

- NSHandsTrackingUsageDescription: A message that tells people why the app is requesting access to track their hand position and location.

- NSAccessoryTrackingUsageDescription: A message that tells a person why the app is requesting access to track accessory position and location.

## Wallet

- NSFinancialDataUsageDescription: A message that tells people why the app is requesting access to financial data stored in Wallet.

- NSIdentityUsageDescription: A message that tells people why the app is requesting identity information.

- NSIdentityUsageDescriptionDictionary: A dictionary that contains messages that explain why your app is requesting identity information.

## Wi-Fi

- UIRequiresPersistentWiFi: A Boolean value that indicates whether the app requires a Wi-Fi connection.

## Deprecated keys

- NSCalendarsUsageDescription: A message that tells people why the app is requesting access to their calendar data.

- NSEnterpriseMCAMUsageDescription: A message that tells people why the app is requesting access to the device’s main camera.

- NSRemindersUsageDescription: A message that tells people why the app is requesting access to their reminders.

## Services

- Data and storage: Regulate documents, URLs, and other kinds of data movement and storage.

- App services: Configure services provided by the app, like support for giving directions or using game controllers.

- Kernel and drivers: Configure device drivers provided by the app.

=== SOURCE: https://developer.apple.comdoc://com.apple.security/documentation/Security/preventing-insecure-network-connections
# Preventing Insecure Network Connections

Enforce secure network links in your app by relying on App Transport Security.

### Overview

On Apple platforms, a networking security feature called App Transport Security (ATS) improves privacy and data integrity for all apps and app extensions. It does this by requiring that network connections made by your app are secured by the Transport Layer Security (TLS) protocol using reliable certificates and ciphers. ATS blocks connections that don’t meet minimum security requirements.



ATS operates by default for apps linked against the iOS 9.0 or macOS 10.11 SDKs or later. In cases where you need to connect to a server that isn’t fully secure—and that you can’t reconfigure to make more secure—you can add exceptions to loosen some of the ATS requirements.

[Note]

Note:  If you link your app against an SDK older than iOS 9.0 or macOS 10.11, ATS is disabled no matter which version of the operating system your app runs on.

#### Prefer High-Level Frameworks in Your App

The system enforces ATS when you use the standard URL Loading System. Instances of URLSession automatically negotiate the most secure connection available from the server. The only action your app must take is to use secure URLs, like those beginning with https. Otherwise, ATS denies the connection and prints a console message:

App Transport Security has blocked a cleartext HTTP (http://) resource
load since it is insecure. Temporary exceptions can be configured via
your app's Info.plist file.

ATS doesn’t apply to calls your app makes to lower-level networking interfaces like the Network framework or CFNetwork. In these cases, you take responsibility for ensuring the security of the connection. You can construct a secure connection this way, but mistakes are both easy to make and costly. It’s typically safest to rely on the URL Loading System instead.

#### Ensure the Network Server Meets Minimum Requirements

A secure server establishes its identity using an X.509 digital certificate. A connecting client examines this certificate to perform default server trust evaluation, which includes checking that the certificate:

- Has an intact digital signature, showing that the certificate hasn’t been tampered with.

- Isn’t expired.

- Has a name that matches the server’s DNS name.

- Is signed by another valid certificate, which is in turned signed by another, and so on back to a trusted anchor certificate, which must be issued by a Certificate Authority (CA). The anchor certificate must be part of the client operating system, as indicated in Lists of available trusted root certificates in iOS, or be installed on the client by the user or a system administrator.

ATS requires all of these things, and then provides extended security checks:

- The server certificate must be signed with either a Rivest-Shamir-Adleman (RSA) key of at least 2048 bits, or an Elliptic-Curve Cryptography (ECC) key of at least 256 bits.

- The certificate must use the Secure Hash Algorithm 2 (SHA-2) with a digest length, sometimes called a fingerprint, of at least 256 bits (that is, SHA-256 or greater).

- The connection must use Transport Layer Security (TLS) protocol version 1.2 or later.

- Data must be exchanged using either the AES-128 or the AES-256 symmetric cipher.

- The link must support perfect forward secrecy (PFS) through Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange.

[Note]

Note:  URLSession automatically handles server trust evaluation for you, but enables you to customize the process, for example to extend trust to a self-signed certificate embedded in your app, or to bypass certificate expiry. When ATS is enabled, you can no longer loosen trust evaluation requirements that way, but you can still tighten them — for example, to implement certificate pinning. For more information, see Performing manual server trust authentication.

#### Optional NIAP Functional Package for TLS Requirements

ATS provides support to further restrict default TLS client behavior to help meet requirements outlined by the National Information Assurance Partnership (NIAP) in the Functional Package for Transport Layer Security. This compliance mode is opt-in only and provides additional options for regulated environments. To opt-in to this mode, use the NSRequiresNIAPTLSPackageVersion key, which can be set to enforce this mode globally, and the NSExceptionRequiresNIAPTLSPackageVersion key to configure exceptions to the global policy on a per-domain basis.

#### Configure Exceptions Only When Needed and Prefer Server Fixes

ATS disallows a connection if the server fails to meet one of the security checks discussed in the previous section. Your best response is to update the server. If you can’t do that for some reason, you can specify exceptions in your app to disable one or more aspects of ATS.

[Important]

Important:  It’s always better to fix the server when faced with an ATS failure. Exceptions reduce the security of your app. Some also require justification when submitting an app to the App Store, as described in the next section.

You configure ATS exceptions by providing a dictionary as the value for the optional NSAppTransportSecurity key in your app’s Information Property List file. The dictionary has the following structure, where all keys are optional:

NSAppTransportSecurity : Dictionary {
    NSAllowsArbitraryLoads : Boolean
    NSAllowsArbitraryLoadsForMedia : Boolean
    NSAllowsArbitraryLoadsInWebContent : Boolean
    NSAllowsLocalNetworking : Boolean
    NSRequiresNIAPTLSPackageVersion : String
    NSExceptionDomains : Dictionary {
        <domain-name-string> : Dictionary {
            NSIncludesSubdomains : Boolean
            NSExceptionAllowsInsecureHTTPLoads : Boolean
            NSExceptionMinimumTLSVersion : String
            NSExceptionRequiresForwardSecrecy : Boolean
            NSRequiresCertificateTransparency : Boolean
            NSExceptionRequiresNIAPTLSPackageVersion : String
        }
    }
}

Keys at the first level of the NSAppTransportSecurity dictionary apply to connections made to any domain not specifically called out in the NSExceptionDomains subdictionary. For example, by setting NSAllowsArbitraryLoads to YES, you completely disable ATS for all network connections when you add this to your app’s Info.plist:



Depending on your use case, you can provide narrower exceptions. For example, by setting NSAllowsArbitraryLoadsInWebContent to YES, you can disable ATS restrictions on calls made from within web views, like instances of WKWebView:



You might only need to limit your ATS exception to a single domain. For example, if you need to access the insecure server http://example.com, you can still maintain all the benefits of ATS for other domains by setting the NSExceptionAllowsInsecureHTTPLoads to YES in the domain-specific sub-dictionary:



[Note]

Note:  Global exceptions don’t apply to any domains that you add to the NSExceptionDomains dictionary. So you can invert the previous example—allowing insecure traffic on all domains except example.com—by placing NSAllowsArbitraryLoads at the top level, and including an empty example.com dictionary as an exception domain.

You can use the nscurl command line tool to connect to a server using different combinations of ATS exceptions. This helps you quickly narrow down the source of any ATS failures you have and figure out what exceptions you need. See Identifying the Source of Blocked Connections for details.

#### Provide Justification for Exceptions

Adding certain ATS exceptions to your app’s Information Property List file requires you to provide justification, and might trigger additional App Store review for your app. Exceptions that require justification are:

- Arbitrary connection exceptions (NSAllowsArbitraryLoads)

- Media streaming exceptions (NSAllowsArbitraryLoadsForMedia)

- Web content loads (NSAllowsArbitraryLoadsInWebContent)

- Per-domain nonsecure connections (NSExceptionAllowsInsecureHTTPLoads)

- Per-domain minimum TLS version (NSExceptionMinimumTLSVersion)

NSRequiresNIAPTLSPackageVersion and NSExceptionRequiresNIAPTLSPackageVersion don’t require justification because they strengthen rather than weaken security requirements.

Some examples of justifications eligible for consideration are:

- The app must connect to a server managed by another entity that doesn’t support secure connections.

- The app must support connecting to devices that cannot be upgraded to use secure connections, and that must be accessed using public host names.

- The app must display embedded web content from a variety of sources, but can’t use a class supported by the web content exception.

- The app loads media content that is encrypted and that contains no personalized information.

When submitting your app to the App Store, provide sufficient information for the App Store to determine why your app cannot make secure connections by default.

[Important]

Important:  Always look for a way to avoid using exceptions as a first recourse. If you must use an exception, make it as limited in scope as possible.

## Evaluation

- Identifying the Source of Blocked Connections: Figure out why App Transport Security denies a network connection.

## Exceptions

- NSAppTransportSecurity: A description of changes made to the default security for HTTP connections.

=== SOURCE: https://developer.apple.comdoc://com.apple.signinwithapple/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts
# Processing changes for Sign in with Apple accounts

Manage user-initiated modifications to maintain privacy with server-to-server notifications.

### Overview

Sign in with Apple users can modify their accounts, including deleting or disabling their Apple Accounts. If your app or website hosts such an account, Apple can alert you when these changes occur by delivering developer notifications to your server. To learn how your users manage their account preferences for your app, see Manage the apps that you use with Sign in with Apple.

#### Set up your server

To receive server notifications for Sign in with Apple, your server must support the Transport Layer Security (TLS) 1.2 protocol or later. When determining the endpoint URL on your server to receive notifications, you may use the same URL for multiple developer teams and apps. To configure your Sign in with Apple service to receive notifications, see Enabling server-to-server notifications.

#### Decode and validate the notifications

These notifications contain a cryptographically signed payload, in JSON Web Signature (JWS) format, signed by Apple’s private key. After your server receives a notification, examine the JWS payload and use the algorithm specified in the header’s alg parameter to validate the signature. For more information, see Fetch Apple’s public key to verify token signatures.

After validating the token signature, your server performs work according to the type value in the events claim of the token. The notification payload object contains information about user-initiated account modification events. The event types include the following:

email-disabled: The user disables email forwarding to their personal email address using Hide My Email.

email-enabled: The user enables email forwarding to their personal email address using Hide My Email.

consent-revoked: The user revokes consent for your app to use their Apple Account and their credentials become invalid.

account-deleted: The user requests that Apple permanently delete their Apple Account.

Expect an HTTP POST response similar to the following example:

HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
    "payload": "<SERVER_TO_SERVER_NOTIFICATION_JWT>"
}

#### Process a user’s email forwarding change

Users can enable or disable email forwarding to your app or website. When a user enables email forwarding, Apple sends a JWT to your registered endpoint URL with the type value of email-enabled in the events claim. A decoded payload for an email-enabled notification has the following format:

{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "email-enabled",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "email": "ep9ks2tnph@privaterelay.appleid.com",
        "is_private_email": "true"
        "event_time": 1508184845
    }
}

When a user disables email forwarding, Apple sends a JWT to your registered endpoint URL with the type value of email-disabled in the events claim. A decoded payload for an email-disabled notification has the following format:

{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "email-disabled",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "email": "ep9ks2tnph@privaterelay.appleid.com",
        "is_private_email": "true"
        "event_time": 1508184845
    }
}

To allow or prevent sending emails to the email address, be sure to update your server’s records according to your process. For more information, see Communicating using the private email relay service.

#### Process disabling and deleting a user’s Apple Account

Users can disable their Apple Account for a specific primary app ID, or delete their Apple Account account entirely. When a user disables their Apple Account for an app or app group, Apple sends a JWT to your registered endpoint URL with the type value of consent-revoked in the events claim. A decoded payload for a consent-revoked notification has the following format:

{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "consent-revoked",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "event_time": 1508184845
    }
}

When a user requests for Apple to permanently delete their Apple Account, Apple sends a JWT to your registered endpoint URL with the type value of account-deleted in the events claim. A decoded payload for an account-deleted notification has the following format:

{
    "iss": "https://appleid.apple.com",
    "aud": "com.mytest.app",
    "iat": 1508184845,
    "jti": "abede...67890",
    "events": {
        "type": "account-deleted",
        "sub": "820417.faa325acbc78e1be1668ba852d492d8a.0219",
        "event_time": 1508184845
    }
}

[Important]

Important:  When a user permanently deletes their Apple Account, Sign in with Apple invalidates all user tokens and disables email forwarding for all associated apps. For native apps, the system doesn’t send a credentialRevokedNotification. Use getCredentialState(forUserID:completion:) to respond to account deletion events.

To indicate when the user disables or permanently deletes their Apple Account, be sure to update your server’s records according to your process. For more information about handling Managed Apple Accounts, see Obtaining information about people and classes.

## Web support

- Sign in with Apple JS: Provide users a fast, secure way to sign in to your web service with their Apple Account.

- Sign in with Apple REST API: Communicate between your app servers and Apple’s authentication servers.

- Displaying Sign in with Apple buttons on the web: Configure the appearance of Sign in with Apple buttons with CSS styles.

- Configuring your environment for Sign in with Apple: Authenticate users with your web service by associating an existing app with a Services ID and private key.

=== SOURCE: https://developer.apple.comdoc://com.apple.signinwithapple/documentation/SigninwithApple
# Sign in with Apple

Provide users the ability to sign in to your apps and websites using their Apple Account.

Sign in with Apple JS 1.0, Sign in with Apple REST API 1.0

### Overview

Sign in with Apple gives your users a fast and safe way to sign in to your apps and websites using their Apple Account. Incorporating Sign in with Apple eliminates the need for additional sign-up steps, allowing users to engage and focus on your app or website.

Sign in with Apple at Work & School provides the same ease of use for users with managed Apple Accounts in Apple School Manager (ASM) or Apple Business Manager (ABM).

[Note]

Note:  Administrators can configure Access Management controls for Sign in with Apple at Work & School within Apple Business Manager and Apple School Manager.

To support Sign in with Apple for iOS, macOS, tvOS, and watchOS apps, see Implementing User Authentication with Sign in with Apple. For website support, see Sign in with Apple JS, and use the Sign in with Apple REST API to communicate with Apple servers.

## On-device support

- Implementing User Authentication with Sign in with Apple: Provide a way for users of your app to set up an account and start using your services.

- Displaying Sign in with Apple buttons in your app: Configure the appearance of Sign in with Apple buttons programatically.

## Web support

- Sign in with Apple JS: Provide users a fast, secure way to sign in to your web service with their Apple Account.

- Sign in with Apple REST API: Communicate between your app servers and Apple’s authentication servers.

- Displaying Sign in with Apple buttons on the web: Configure the appearance of Sign in with Apple buttons with CSS styles.

- Configuring your environment for Sign in with Apple: Authenticate users with your web service by associating an existing app with a Services ID and private key.

- Processing changes for Sign in with Apple accounts: Manage user-initiated modifications to maintain privacy with server-to-server notifications.

## Transfers across teams

- Transferring your apps and users to another team: Migrate Sign in with Apple users to another team.

- Bringing new apps and users into your team: Receive Sign in with Apple users and associated apps from another team.

=== SOURCE: https://developer.apple.comdoc://com.apple.signinwithapple/documentation/SigninwithAppleRESTAPI/Revoke-tokens
# Token revocation

Invalidate the tokens and associated user authorizations for a user when they are no longer associated with your app.

Sign in with Apple REST API 1.0

URL: POST https://appleid.apple.com/auth/revoke

200 OK: The request was successful; the provided token has been revoked successfully or was previously invalid.

400 Bad Request: The server was unable to process the request. See the error code description for more information about the underlying error.

### Discussion

In order to revoke authorization for a user, you must obtain a valid refresh token or access token. If you don’t have either token for the user, you can generate tokens when validating an authorization code. For more information about user tokens and creating client secrets, see Token validation.

To invalidate a user’s refresh token, invoke the revoke endpoint with the following HTTP POST method.

curl -v POST "https://appleid.apple.com/auth/revoke" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'token=REFRESH_TOKEN' \
-d 'token_type_hint=refresh_token'

Additionally, to invalidate a user’s access token, use the following HTTP POST method.

curl -v POST "https://appleid.apple.com/auth/revoke" \
-H 'content-type: application/x-www-form-urlencoded' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET' \
-d 'token=ACCESS_TOKEN' \
-d 'token_type_hint=access_token'

For either token revocation request, the revoke endpoint returns a 200 response code without a response body after the server invalidates the token value, or if the token value was previously invalidated. If the response contains an error, please see ErrorResponse for the specific error code provided in the response body.

## Generating and revoking tokens

- Creating a client secret: Generate a signed token to identify your client application.

- Fetch Apple’s public key to verify token signatures: Fetch Apple’s public key to verify ID token and server notification signatures.

- Token validation: Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.

=== SOURCE: https://developer.apple.comdoc://com.apple.uikit/documentation/UIKit/requesting-access-to-protected-resources
# Requesting access to protected resources

Provide a purpose string that explains to a person why you need access to protected resources on their device.

### Overview

Modern devices collect and store a wealth of sensitive information about people who use them. Many apps rely on this kind of data, and the device hardware that generates it, to do useful work. For example, a navigation app needs a person’s GPS coordinates to locate the person on a map. But not all apps need access to all data. The same navigation app doesn’t need access to a person’s health history, camera interface, or Bluetooth peripherals.

Ensure your app accesses only what it needs to do its job. To support this principle, Apple’s operating systems restrict access to protected data and resources by default. Apps can request access on a case-by-case basis, providing an explanation for why they need access. The person who uses the app decides whether to grant or deny the request.

[Tip]

Tip:  In addition to asking people for permission to access a resource, in some cases, you also need to separately declare your intent to do so by adding an entitlement to your app, as described in Entitlements.

#### Provide a purpose string

The first time your app attempts to access a protected resource, the system prompts the person using the app for permission. In the following example, an iOS app called FoodDeliveryApp, which provides a food delivery service, generates a prompt requesting access to the person’s location:



If the person grants permission, the system remembers the person’s choice and doesn’t prompt again. If the person denies permission, the access attempt that initiates the prompt, and any further attempts, fail in a resource-specific way. For the particular case of access to location data, the person can choose to allow access for one session only by tapping Allow Once.

The system automatically generates the prompt’s title, which includes the name of your app. You supply a message called a purpose string or a usage description — in this case, “Your location allows you to view restaurants in delivery range of your address.” — to indicate the reason that your app needs the access. Accurately and concisely explaining to the person why your app needs access to sensitive data, typically in one complete sentence, lets the person make an informed decision and improves the chances that they grant access.

To provide a purpose string, follow these steps in Xcode:

1. Navigate to the Signing and Capabilities editor for your app.

2. Click the Add (+) button to add a capability.

3. Choose the protected resource you want to add; in this case, it’s “Location (When in Use)”.

4. Enter the purpose string in the text field.



Always provide a valid purpose string in the Signing and Capabilities editor if your app uses a protected resource. If you don’t, attempts to access the resource fail, and might cause your app to crash. Xcode detects when your app crashes for this reason and reports an issue, telling you to add the purpose string to your app. Click the Add button to provide the purpose string.



Xcode adds a build setting to your app that configures the purpose string as the value for a Information Property List; in this example, the key is NSLocationWhenInUseUsageDescription, so the build setting is INFOPLIST_KEY_NSLocationWhenInUseUsageDescription. For more information on configuring information property list values using build settings, see Managing your app’s information property list values.

If your app supports multiple locales, in addition to providing a purpose string in the Signing and Capabilities editor, localize the purpose string for each locale you support. Create a string catalog file called InfoPlist.xcstrings, and build your app to populate the string catalog with keys for the usage description strings in your app. Add the translations for your usage description strings to the localizations in the string catalog. For more information, see Localizing and varying text with a string catalog.

#### Adhere to the requirements for purpose strings

To give people useful, concise information about why you’re requesting access to protected resources, make sure each purpose string you provide is valid by checking the following:

- The purpose string isn’t blank and doesn’t consist solely of whitespace characters.

- The purpose string is shorter than 4,000 bytes. Typical purpose strings are one complete sentence, but you can provide additional information to help a person make the right decision about sharing personal information.

- The purpose string has the proper type that the corresponding key requires, typically a string.

- The purpose string provides a description that’s accurate, meaningful, and specific about why the app needs to access the protected resource.

Adhere to these requirements for every purpose string in your app, including localized purpose strings.

App Review checks for the use of protected resources, and rejects apps that contain code accessing those resources without a purpose string. For example, an app accessing location might receive the following information from App Review about the requirement that an NSLocationWhenInUseUsageDescription key be present:

ITMS-90683: Missing purpose string in Info.plist. 
Your app’s code references one or more APIs that access sensitive user 
data, or the app has one or more entitlements that permit such access. 
The Info.plist file for the "{app-bundle-path}" bundle should contain a 
NSLocationWhenInUseUsageDescription key with a user-facing purpose string 
explaining clearly and completely why your app needs the data.
If you’re using external libraries or SDKs, they may reference APIs that 
require a purpose string. While your app might not use these APIs, a 
purpose string is still required. For details, visit: 
https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources.

To resolve this issue, provide a purpose string that explains why the app needs access to this sensitive information, or remove the code that’s accessing the resource.

[Note]

Note:  If you’re using external libraries or SDKs, they may reference APIs that require a purpose string. Although your app might not use these APIs, a purpose string is still necessary for App Review. You can contact the developer of the library or SDK to request information about which protected resources the developer uses and their purpose, or request that the developer release a version of their code that doesn’t contain the APIs. You’re responsible for all access of protected resources, including external SDK and library access.

#### Check for authorization

Many system frameworks that provide access to protected resources have dedicated APIs for checking and requesting authorization to use those resources. This model allows you to adjust your app’s behavior depending on the current access it has. For example, if a person denies your app permission to do something, you can remove related elements from your user interface.

Because a person can change authorization at any time using Settings, always check the authorization status of a feature before accessing it. In cases without a dedicated API, prepare your app to gracefully handle access failures.

#### Reset authorization access

When your app attempts to access a protected resource after its first attempt, the system remembers the person’s permission choice and doesn’t prompt again. To prompt the person again, you need to reset access to these resources on your device or system.

To reset permission access to a protected resource in iOS apps, tap Settings > General > Transfer or Reset iPhone > Reset > Reset Location & Privacy on your device.

[Important]

Important:  Using Reset Location & Privacy resets location and privacy settings for all services on your device.

To reset permissions for a particular service in macOS apps, run the tccutil reset <service name> command in Terminal. For example, to reset all permissions for AppleEvents, type:

$ tccutil reset AppleEvents

This command resets authorization access for all apps using the protected resource. You can similarly specify Camera, Calendar, Reminders, or other services to reset them individually. For more information, see Resetting access to protected resources in macOS.

## Supporting Privacy

- Encrypting Your App’s Files: Protect the user’s data in iOS by encrypting it on disk.

=== SOURCE: https://developer.apple.comdoc://com.apple.Xcode/documentation/Xcode/configuring-background-execution-modes
# Configuring background execution modes

Indicate the background services your app requires to continue executing in the background in iOS, iPadOS, tvOS, visionOS, and watchOS.

### Overview

Typically, an app is in a suspended state when it’s in the background. However, there are a limited number of background execution modes your app can support that enable it to run when in the background, such as playing audio, receiving location updates, or processing scheduled tasks. For apps that adopt one or more of these modes, the system launches or resumes the app, in the background, and affords it time to process any related events.

Use background execution modes sparingly because overuse can negatively impact device performance and battery life. If an alternative to executing in the background exists, use the alternative instead. For example, apps can use the significant-change location service to receive location events as an alternative to using the Location updates background mode.

Before you can select the background execution modes your app requires, follow the steps in Add a capability to add the Background Modes capability to your app’s target.



The background execution modes that appear after you add the capability depend on the target’s platform. For watchOS apps with separate WatchKit extensions, you need to add the capability to the WatchKit Extension target.

[Note]

Note: The Background Modes capability isn’t available for macOS apps.

#### Specify the background modes your app requires

Before your app can leverage one or more background execution modes, you need to declare the modes it requires by performing the following:

1. Select your project in Xcode’s Project navigator.

2. Select the app’s target in the Targets list.

3. Click the Signing & Capabilities tab in the project editor.

4. Find the Background Modes capability.

5. Select one or more background execution modes using the corresponding checkboxes.

6. For watchOS apps, choose the appropriate session type from the pop-up menu. For more information, see Using extended runtime sessions.



Xcode adds the UIBackgroundModes array to your app’s Info.plist file, if it isn’t already present, and uses the modes you select to populate the array with the necessary values.

Apple’s platforms support these background execution modes:

| Mode | Value | Description | Platforms |

| Audio, AirPlay, and Picture in Picture | audio | The app plays audible content in the background. For more information, see Configuring your app for media playback. | iOS, iPadOS, tvOS, visionOS |

| Audio | audio | The app plays audible content in the background. For more information, see Playing Background Audio. | watchOS |

| Location updates | location | The app provides location-based information and requires the use of the platform’s standard location service. For more information, see Configuring your app to use location services. | iOS, iPadOS, watchOS |

| Voice over IP | voip | The app provides Voice over IP services. For more information, see the CallKit framework. | iOS, iPadOS, visionOS, watchOS |

| External accessory communication | external-accessory | The app communicates with an accessory that delivers data at regular intervals. For more information, see the External Accessory framework. | iOS, iPadOS |

| Uses Bluetooth LE accessories | bluetooth-central | The app communicates with a Bluetooth accessory while in the background. For more information, see the Core Bluetooth framework. | iOS, iPadOS, visionOS |

| Acts as a Bluetooth LE accessory | bluetooth-peripheral | The app uses peripheral mode to communicate with a Bluetooth accessory. For more information, see the Core Bluetooth framework. | iOS, iPadOS |

| Screen Capture | screen-capture | The app captures and streams screen content while in the background. For more information, see the ScreenCaptureKit framework. | iOS, iPadOS, visionOS |

| Background fetch | fetch | The app requires new content from the network at regular intervals. For more information, see Using background tasks to update your app. | iOS, iPadOS, tvOS, visionOS |

| Remote notifications | remote-notification | The app uses push notifications as a signal that new content is available to download. For more information, see Pushing background updates to your App. | iOS, iPadOS, tvOS, visionOS, watchOS |

| Background processing | processing | The app executes scheduled tasks while in the background. For more information, see BGTaskScheduler. | iOS, iPadOS, tvOS, visionOS |

| Workout processing | workout-processing | The app uses a workout session to track a user’s activity on Apple Watch. For more information, see Running workout sessions. | watchOS |

| Uses Nearby Interaction | nearby-interaction | The app locates and interacts with nearby devices. For more information, see the Nearby Interaction framework. | iOS, iPadOS |

| Push to Talk | push-to-talk | The app launches in response to a push notification and plays audible content in the background. For more information, see the Push to Talk framework. | iOS, iPadOS |

## App execution

- Configuring custom fonts: Register your app as a provider or consumer of systemwide custom fonts.

- Configuring game controllers: Enhance gameplay input by enabling the discovery, configuration, and use of physical game controllers.

- Configuring Maps support: Register your iOS routing app to provide point-to-point directions to Maps and other apps.

- Configuring Siri support: Enable your app and its Intents extension to resolve, confirm, and handle user-driven Siri requests for your app’s services.

=== SOURCE: https://developer.apple.comdoc://com.apple.Xcode/documentation/Xcode/configuring-your-app-icon
# Configuring your app icon using an asset catalog

Add app icon variations to an asset catalog that represents your app in places such as the App Store, the Home Screen, Settings, and search results.

### Overview

[Important]

Important: To create your app icon using Icon Composer for all variants, including different platforms and appearances, see Creating your app icon using Icon Composer.

Every app has a distinct app icon that communicates the app’s purpose and makes it easy to recognize throughout the system. Apps require multiple variations of the app icon to look great in different contexts. Xcode can help generate these variations for you using a single high-resolution image, or you can configure your app icon variations by using an app icon’s image set in your project’s asset catalog. visionOS and tvOS app icons are made up of multiple stacked image layers you configure in your project’s asset catalog. iOS and iPadOS app icons support additional dark and tinted styles.

For design guidance on app icons, see Human Interface Guidelines > App icons.

#### Create an app icon

When you create your project from a template, it automatically includes a default asset catalog (Assets.xcassets) that contains the AppIcon. If you don’t have a default asset catalog or existing AppIcon or you want to provide an alternate, you can add an app icon to an asset catalog manually:

1. In the Project navigator, select an asset catalog.

2. Click the Add button (+) at the bottom of the outline view.

3. In the pop-up menu, choose OS variant > OS variant App Icon. Xcode creates a new app icon set or image stack with the name AppIcon.

#### Specify app icon variations

Variations of your app icon appear throughout the system in places like the Home View, Settings, and search results:

- iOS, iPadOS, tvOS, and watchOS apps can auto-generate all icon variations from a single 1024×1024 pixel image. This is the default behavior when you create a new iOS, iPadOS, tvOS, and watchOS app, or a new icon in the asset catalog. If you have an existing project that provides multiple variants, consider providing a single size when that is all your icon requires. However, if you want to customize your app’s icon variants, such as to show more detail at a larger size, you can provide individual assets for the variations.

- For macOS and tvOS, you need to supply an asset for each size.

- For visionOS, you need to supply a single 1024x1024 pixel asset.

For each platform your app supports, choose between using a single size and providing all sizes in the Asset Catalog:



1. In the Project navigator, select an asset catalog.

2. In the Asset Catalog, select the icon.

3. To view and edit attributes, select Inspectors > Attributes from Xcode’s View menu.

4. Select Single Size or All Sizes from the pop-up menu for the platform you want to change.

For each platform your app supports, add a single image that Xcode can use to generate your icon variations, or add an image for each icon variation of an icon set in the Asset Catalog:



1. In the Project navigator, select an asset catalog.

2. In the Asset Catalog, select the icon.

3. From the Finder, drag image variations of the app icon to the image wells in the detail area of the Asset Catalog in Xcode that match their resolutions and use cases. visionOS and tvOS app icons combine a stack of multiple image layers to create a sense of depth. For tvOS apps, the asset catalog contains an App Icon & Top Shelf Image folder with the different app icon and launch image sets.

#### Add dark and tinted icon variants to iOS and iPadOS

iOS and iPadOS support three stylistic variations for app icons: Light, Dark, and Tinted. You can create your own variations to ensure that each one looks exactly the way you way you want.



To add these icon variations to your app:

1. In the Project navigator, select an asset catalog.

2. In the Asset Catalog, select the icon.

3. Select View > Inspectors > Attributes from the Xcode menu.

4. Select Single Size from the iOS pop-up menu.

5. Then select Any, Dark, or Tinted from the Appearance pop-up menu.

After you select the Appearance from the pop-up menu, two image wells appear. Drag your dark and tinted app icons into the appropriate image well. Provide your tinted app icon as a grayscale image. Provide your dark app icon with a transparent background so the system-provided background can show through.

If you prefer, you can take advantage of the system’s automatically generated treatment that is applied to all app icons. It is crafted intelligently to preserve design intent and maintain legibility. This also helps maintain a consistent visual experience across the Home Screen.

For design guidance specific to iOS and iPadOS, see Human Interface Guidelines > App Icons.

#### Configure the layers of an image stack

By default, visionOS and tvOS app icons are constructed with three layers. This is the maximum number of layers visionOS icons support but you can use up to five layers when constructing tvOS icons. To add a layer, Click the Add button, choose OS variant > OS variant App Icon Layer. To remove a layer, select the layer and click the Remove button (-).



Add images to each layer by dragging them from the Finder into the image wells in the detail area of the Asset Catalog in Xcode. For information on the use of layers, see App icons visionOS and tvOS.

[Note]

Note: You can use Parallax Previewer app or Parallax Exporter plug-in to create and preview Layer Source Representation (.lsr and .xlsr) files that you can import into your Asset Catalog in Xcode. Save your file in the LSR file format to import a tvOS icon into Xcode, and save in the XLSR file format to import a visionOS icon. Download these from the Apple Design Resources site.

#### Specify an App Store icon

If you distribute your app through the App Store, you must provide app icon imagery to use in the App Store. In the Project navigator, select an asset catalog and add icon images to the appropriate image wells in an app icon set or image stack. The App Store image well location varies by platform.

| Platform | App Store icon location |

| iOS | Drag an icon image to the iOS 1,024pt image well. |

| iMessage | For the iOS target, drag an icon image to the iOS 1,024pt image well in the AppIcon set. For the iMessage Extension target, drag an icon to the Messages App Store image well in the iMessage App Icon set. |

| Sticker Pack | Drag an icon image to the iOS 1,024pt image well and the Messages App Store image well. |

| macOS | Drag an icon image to the App Store - 2x image well. |

| tvOS | Drag images to the image wells for the layers of your App Icon - App Store stack in the App Icon & Top Shelf Image folder. The App Store generates an icon from the layers of the image stack. |

| visionOS | Drag images to the image wells for the layers of your visionOS App Icon stack. The App Store generates an icon from the layers of the image stack. |

| watchOS | For the iOS target, drag an icon image to the iOS 1,024pt image well. For the WatchKit App target, drag an icon image to the watchOS image well. |

#### Change the default app icon set

If you don’t create your project from a template, or you want to change your default app icon set, specify which one to use in your target’s build settings.

1. In the Project navigator, select the project and in the project editor, select the target.

2. In the App Icons and Launch Screen section of the General pane, choose the app icon set from the App Icons Source pop-up menu.



If you don’t select the Include all app icon assets option, Xcode only includes the app icon set you specify in the App Icons Source pop-up menu when it builds your app. You might leave this option unselected if you want to use a different icon for the Debug and Release builds of your app without including the Debug icon in your Release app bundle. You can specialize the app icon for the Debug and Release configurations by modifying the Primary App Icon Set Name build setting in the Build Settings tab.

Xcode also includes any additional app icon sets you specify under the Alternate App Icon Sets build setting. Include any icon sets your app can select using setAlternateIconName(_:completionHandler:) or use in App Store product pages.

For information on configuring tests that use icons in App Store Connect, see Product Page Optimization.

## App icons and launch screen

- Creating your app icon using Icon Composer: Use Icon Composer to stylize your app icon for different platforms and appearances.

- Configuring your app to use alternate app icons: Add alternate app icons to your app, and let people choose which icon to display.

- Specifying your app’s launch screen: Make your iOS app launch experience faster and more responsive by customizing a launch screen.

=== SOURCE: https://developer.apple.comdoc://com.apple.Xcode/documentation/Xcode/creating-your-app-icon-using-icon-composer
# Creating your app icon using Icon Composer

Use Icon Composer to stylize your app icon for different platforms and appearances.

### Overview

Use Icon Composer to create a single multilayer file that you can add to your Xcode project to represent your Liquid Glass app icon everywhere your app icon appears across iOS, iPadOS, macOS, watchOS, and the App Store. Use your favorite design tool to create the artwork for your app icon, but save some design decisions for Icon Composer, where you can refine the dynamic properties of Liquid Glass and customize variants of your app icon for different platforms and appearances.



Before building your app, add the Icon Composer file to your Xcode project to include it in your app’s bundle. The system automatically renders your app icon for the different platforms, appearances, and sizes from your single Icon Composer file. If your app supports previous releases (in the Minimum Deployments settings in the target’s General pane) that don’t have the same icon and widget style appearances and Liquid Glass material, Xcode automatically generates app icon images at build time for those releases from the Icon Composer file.

[Important]

Important: If you add an Icon Composer file to your Xcode project, it replaces any existing icon asset catalog that you previously used to represent your app icon. Xcode automatically generates a similar-looking version of the Liquid Glass icon for previous releases. If you want your existing icon to appear in previous releases, continue to use asset catalogs to represent your app icon.

To learn more, see the following resources:

- For guidance on designing your app icon, see Human Interface Guidelines > Foundations > App icons.

- For converting older app icons to use the Liquid Glass material, see Adopting Liquid Glass > App icons.

- For more information on Liquid Glass and Icon Composer, watch Say hello to the new look of app icons and Create icons with Icon Composer.

- For tvOS and visionOS targets that still use an AppIcon asset catalog, see Configuring your app icon using an asset catalog.

### Prepare your artwork for export

To design your Liquid Glass app icon, use a third-party vector graphics editor of your choice that exports your layers as graphic files in SVG or PNG format. To give you the most scalability, use vector graphics to draw shapes and export SVG files.

While you design your app icon and before you export layers, follow these guidelines for best results:

- Start with an app icon template that you download from Apple Design Resources that has the latest grid, shape, and canvas size.

- Otherwise, change the canvas size to match the size that you use in Icon Composer, such as 1024 x 1024 pixels for iPhone, iPad, and Mac, and 1088 x 1088 pixels for Apple Watch.

- Design your app icon in layers that the system renders in the z-plane from back to front.

- Separate colors, text, and any other graphics into layers that you want to modify for platforms and appearances in Icon Composer.

- Because SVG format doesn’t preserve fonts, convert text to outlines.

- Give the layers meaningful names that include numbers (increment from back to front) to help you organize them in Icon Composer.

In addition, wait to apply some effects in Icon Composer where you can preview and adjust them for Liquid Glass:

- Remove blurs and shadows, and specular, opacity, and translucency settings.

- Remove background colors and gradients.

When you’re ready to export layers from your third-party tool, choose the SVG format whenever possible. For layers that contain unsupported SVG features, choose PNG or another raster image format that Icon Composer supports. Don’t export the canvas mask because the system applies that automatically to ensure a perfect crop.

### Create your Icon Composer file

To launch Icon Composer in the latest version of Xcode, choose Xcode > Open Developer Tool > Icon Composer. If you don’t install Xcode, go to Icon Composer to download it instead.

Icon Composer shows a default app icon with a solid background color. Give the file a name that you want to use later in the Xcode project, such as AppIcon. Choose File > Save and in the dialog that appears, enter the filename and click Save. Alternatively, click Untitled in the toolbar and change the name and location in the dialog that appears.



You use the sidebar on the left to organize layers into groups, the canvas in the middle to preview variants, and the inspectors on the right to modify appearances. In the canvas area, you use the controls at the bottom to select combinations of platforms and appearances, and the controls at the top to apply a grid or simulate device conditions.

You can continue using Icon Composer to fine-tune your app icon and add it to your Xcode project later. To add your app icon to an Xcode project and associate it with your app target, see Add your Icon Composer file to an Xcode project.

If your Icon Composer file is in your Xcode project, you can select it in the Project navigator and see a preview in the canvas area. To open an Icon Composer file that’s in your Xcode project, click Open with Icon Composer under the preview, or Control-click the file in the Project navigator and choose Open with External Editor.

### Import your graphic files

After you export your artwork from your design tool, import the graphic files, in SVG or PNG format, into your Icon Composer file.

Drag one or more graphic files from the Finder to the sidebar and each becomes a layer in a default group that Icon Composer creates. Alternatively, drag folders containing graphic files to the sidebar. Then the folders become groups and the files in the folders become layers in those groups. Icon Composer organizes the groups and layers alphabetically using the same names as the folders and files.

Alternatively, click the Add button (+) under the sidebar and choose New Image from the pop-up menu. In the dialog that appears, select one or more files (use Command-click to select multiple files) and click Open.

Later, if you want to change the graphic file associated with a layer, select the layer in the sidebar and choose Replace from the Image pop-up menu under Composition in the Style inspector. Then, from the dialog that appears, select the new graphic file.

### Organize layers into groups

After you import the graphic files, organize the layers that appear in the default group into a maximum of four groups to reduce complexity. The groups become the layers in the app icon image the platform renders to give the icon its depth. The system renders the layers in the z-plane from the bottom to the top as they appear in the sidebar. Groups also allow you to apply common settings to multiple layers.



You can use the sidebar to make the following edits:

- To create a group, click the Add button at the bottom of the sidebar and choose New Group from the pop-up menu.

- To change the name of a group or layer, double-click it and enter a name.

- To move layers into groups, drag them to the groups you want them to be in.

- To change the order of a group or layer, drag them up or down. Alternatively, select a layer or group and choose Arrange > Bring [Group | Layer] Forward or Arrange > Send [Group | Layer] Backward (or similar) menu item.

- To add another layer, click the Add button and choose Image.

For more edits, Control-click a layer or group and choose an action from the contextual menu.

To collapse groups in the outline, click the disclosure triangle to the left of the group. To hide or show layers and groups in the canvas, click the eye icon to the right of the group or layer in the sidebar when you hold the pointer over it. Alternatively, hide or show layers and groups using the Visible toggle under Composition in the Style inspector.

To delete groups, layers, or graphics in a layer, select them in the sidebar or canvas, and press Delete. To revert your changes, choose Edit > Undo Delete.

### Customize the Icon Composer interface

Before you begin previewing variants and adding effects to your app icon, consider customizing the Icon Composer interface to show only the platforms that your app supports. Click the Document button in the upper-right corner and choose the platforms from the Document inspector.



For example, if your app runs in iOS only, choose iOS Only from the iOS, macOS pop-up menu and toggle watchOS to off. Icon Composer hides the macOS and watchOS controls so that you can focus on the iOS app icon design.

### Preview variants of your app icon

Icon Composer shows you a preview of your app icon on different platforms (iOS, macOS, and watchOS) and, for iOS and macOS, different appearances (default, dark, and mono). For mono, you can preview clear and tinted variants as well. For watchOS, there are no appearances to preview.

Below the image of your icon in the canvas area, click a platform on the left and appearance on the right to preview or edit that variant. For example, to preview the dark appearance in iOS, select iOS on the left and Dark on the right.

To preview clear and tinted variants, click Mono and then click Options. From the dialog, select Light or Dark, toggle Tinted on or off, and select a tint color using the sliders.



### Simulate device backgrounds, effects, and lighting

To preview your app icon in a different context, use the controls in the toolbar above the canvas area. These controls only change the simulated device where your app icon appears; they don’t edit your app icon.



You can use the toolbar controls to set the following:

- To change the background color, choose a color from the color well on the left.

- To change the background image, choose a background image from the Background Image pop-up menu. To use your own image, click Add Background in the pop-up menu.

- To switch between the background color and image, click the background toggle.

- To add grid lines, choose Light or Dark from the Grid pop-up menu.

- To toggle the grid lines on or off, click the Grid button.

- To view a specific size of the app icon, choose the size from the “Select preview size” pop-up menu.

- To zoom in or out, choose a percentage from the “Change zoom level” pop-up menu.

- To compare the app icon rendering on a previous with the current design generation, click the Effects buttons. For example, to compare macOS 26 with macOS 27 rendering, click 26 and then 27.

- To view the app icon with no Liquid Glass effects, toggle Effects off.

You can use these controls to see the transparency in the clear and tinted modes using your own backgrounds. For example, to preview the clear dark variant over a sample image, select iOS or macOS as the platform and Mono as the appearance. From the Mono options dialog, toggle Tinted off. Then choose Add Background from the Background Image pop-up menu at the top of the canvas and select the screenshot in the dialog that appears.



### Apply effects to the background, groups, and layers

As you preview the variants of your app icon on different platforms and device settings, apply effects and fix any problems you see using the Style inspector. Explore the different settings for groups and layers within a group.

In general, settings under Color are useful for creating variants for dark and mono appearances. For groups and layers, you customize the dynamic material under Liquid Glass. Then use the controls under Composition for varying your design on different platforms.



To quickly duplicate settings, you can Control-click an individual setting or a section, and choose Copy [Setting | Section] or Paste [Setting | Section] from the contextual menu. Alternatively, Control-click a layer or group in the sidebar and choose Copy Style or Paste Style from the contextual menu (Edit > Copy Style and Edit > Paste Style).

For any text fields where you enter numbers, you can enter an equation and Xcode calculates the value for you. For example, enter 35*3, or enter *2 to double an existing value.

To remove any changes you make in the Style inspector, choose Edit > Undo.

### Apply a gradient fill and opacity

Under Color in the Style inspector, you can change a layer’s fill from the default value (Automatic) that Icon Composer gets from the graphic file. Select the layer in the sidebar, and from the Fill pop-up menu in the Style inspector, choose None, Solid, or Gradient.



[Tip]

Tip: To set an RGB value or hexadecimal (hex) color number for a color, use the RGB sliders in the Color Sliders inspector in the Colors window.

For example, apply a gradient to your app icon’s background following these steps:

1. In the sidebar, click the icon filename.

2. In the canvas, select a platform and, optionally, an appearance.

3. To show the settings, click the Style inspector in the upper-right corner of the window.

4. From the Color pop-up menu, choose All to change all variants.

5. From the Fill pop-up menu, choose Gradient.

6. From the two color wells that appear below, select the “From” and “To” colors.

To switch the colors, click the arrows to the left of the Gradient color wells when you hold the pointer over them. For layers, you can use the dots in the canvas that appear on the layer to change the “From” and “To” locations of the gradient.



To set the opacity of the “From” and “To” colors, change the percentage value on the right of the color wells. You can also use the Opacity setting under Color to make a group or layer transparent, revealing details behind it.

### Apply Liquid Glass effects to groups and layers

Icon Composer automatically adds the Liquid Glass material to layers when you import graphics files, and it applies other default Liquid Glass settings to groups when you create them.



For a group, you have all the options to customize the Liquid Glass material. Select a group in the sidebar and choose Individual or Combined from the Mode pop-up menu in the inspector.

- To apply the effects to every layer in the group separately, choose Individual.

- To apply the effects to the layers in the group as one object, choose Combined.

Choose how specular highlights align with each layer, either inside or outside, or let the system decide. From the Specular pop-up menu, choose one of these options:

- To remove the specular highlights, choose Off.

- To apply the specular highlights and let the system determine whether it’s on the inside or outside of the artwork, choose Automatic.

- To apply the specular highlights on the inside of the artwork, choose Inside.

- To apply the specular highlights on the outside of the artwork, choose Outside.

Icon Composer sets the specular highlights to Automatic by default.

Below Specular, you can apply the rest of the Liquid Glass settings (Blur, Refraction, Translucency, and Shadow) to the group.

Refraction lets layers pick up and transmit color and shape from what’s behind them. To turn on refraction, toggle Refraction on. To change the strength of refraction, drag the circle around in the 2D space below or enter percentages in the text fields on the right.

To turn Liquid Glass off for an individual layer, select the layer in the sidebar, and in the inspector, turn off the Effects toggle under Liquid Glass.

[Note]

Note: In iOS, iPadOS, macOS, and watchOS versions earlier than 27, specular highlights appear on when you choose Inside or Outside, and Refraction settings have no visible effect.

### Change the position and scale of graphics

You can reposition and scale graphics in your layers using Icon Composer. Just select and drag the graphics in a layer or group that you want to move within the canvas area.

To move multiple groups, layers, or individual graphics, Command-click them in the sidebar or canvas first, or select them by dragging a bounding box in the canvas. Icon Composer highlights the selection in both the sidebar and canvas. To unselect all graphics, press the Escape key.



Use the guidelines that appear while dragging to align the selection with other graphics. To make more precise edits, you can enter an x, y, and scale in the Layout section of the Style inspector under Composition. To make single point changes, use the Up Arrow and Down Arrow keys.



Optionally, turn the grid on so you can see where to place your graphics. In the toolbar, click the Grid button or choose Light or Dark from the Grid pop-up menu. Icon Composer overlays grid lines on the preview of your app icon in the color that you choose. To remove the grid lines, toggle Grid off.



For other ways to reposition the selection, use the Arrange > Align and Arrange > Distribute menu items.

### Customize variants of your app icon

You can customize specific platform and appearance variants of your app icon using the Style inspector.

To see settings that you customize, select the icon, a group, or a layer in the sidebar and choose All from the Color, Liquid Glass, or Composition pop-up menu in the Style inspector. The custom settings appear below the main setting. For example, if you change the Blend Mode setting for the dark and mono appearances in iOS, then a Dark and Mono setting appears below the Blend Mode setting. The main setting applies to the variants that you don’t customize.



The Style inspector enables the controls for the platform or appearance that you select in the canvas. For example, to enable the Dark setting that appears below Blend Mode, select the dark appearance in the canvas.

To add another custom setting, select the platform or appearance in the canvas that you want to vary and in the Style inspector, click the icon next to the setting. Choose Vary for [appearance | platform] from the Add button pop-up menu. For example, select iOS / macOS and Default in the canvas and choose Vary for iOS / macOS from the Blur pop-up menu under Liquid Glass.



To remove custom settings, click the X next to the platform or appearance. For example, to remove the Dark setting under the Blend Mode setting, click the X next to Dark.

Alternatively, choose the appearance that you select in the canvas from the Color or Liquid Glass pop-up menu. Then the controls in that section only apply to that appearance. Similarly, choose the platform that you select in the canvas from the Composition pop-up menu and the controls in that section apply only to that platform. The controls behave in this way so that the appearance of your app icon remains consistent and only the geometry varies across platforms.



Then you can switch back to seeing all the custom settings you made for platforms and appearances in one place by choosing All from the Color, Liquid Glass, and Composition pop-up menus.

### Add your Icon Composer file to an Xcode project

If you create your Icon Composer file outside of Xcode, you can add it to your Xcode project anytime to view your icon in simulated and physical devices using Device Hub.

Just drag the Icon Composer file from Finder to the Project navigator, and Xcode provides feedback on where to drop it in a target folder. Alternatively, choose Add Files from the Add button at the bottom of the Project navigator and select your Icon Composer file in the dialog that appears.

In the project editor, select the target and the General tab. Under App Icons and Launch Screen, ensure that the name in the App Icon text field matches the name of the Icon Composer file without the extension. You can have multiple Icon Composer files in your project but only one that matches the name in the App Icon text field.

[Note]

Note: The latest version of Xcode uses the Icon Composer file instead of an existing AppIcon asset catalog in your project.

## App icons and launch screen

- Configuring your app to use alternate app icons: Add alternate app icons to your app, and let people choose which icon to display.

- Configuring your app icon using an asset catalog: Add app icon variations to an asset catalog that represents your app in places such as the App Store, the Home Screen, Settings, and search results.

- Specifying your app’s launch screen: Make your iOS app launch experience faster and more responsive by customizing a launch screen.

=== SOURCE: https://developer.apple.comdoc://com.apple.Xcode/documentation/Xcode/specifying-your-apps-launch-screen
# Specifying your app’s launch screen

Make your iOS app launch experience faster and more responsive by customizing a launch screen.

### Overview

Every iOS app must provide a launch screen, a screen that displays while your app launches. The launch screen appears instantly when your app starts up and is quickly replaced with the app’s first screen.

You create a launch screen for your app in your Xcode project in one of two ways:

- Information property list

- User interface file

To make the app launch experience as seamless as possible, create a launch screen with basic views that closely resemble the first screen of your app.
For guidelines about designing a launch screen, see Launching in the Human Interface Guidelines.

#### Configure a launch screen in an information property list

For apps with simple user interfaces, using the information property list in your app provides a quick and straightforward method to configure your launch screen.

1. In the settings for your target, select the Info tab.

2. In the Custom iOS Target Properties section, expand the Launch Screen key.

3. Click the Add button (+), type in UILaunchScreen, and press Return to add the launch screen key to the property list. If the UILaunchScreen key is already present, you can skip this step.

4. Select the UILaunchScreen key, click the Add button, and add additional keys to specify configuration options for your launch screen.



Define the appearance of the launch screen by specifying a combination of launch screen options from the possible keys in UILaunchScreen.

#### Configure a launch screen storyboard

Alternatively, you can configure your launch screen in a user interface file, a file with a .storyboard file extension. A launch screen storyboard contains basic UIKit views, and uses size classes and Auto Layout constraints to support different device sizes and resolutions.

Follow these guidelines when creating a launch screen storyboard:

- Use only UIKit classes.

- Use a single root view that’s a UIView or UIViewController object.

- Don’t make any connections to your code, for example, don’t add actions or outlets.

- Don’t use deprecated views such as UIWebView.

- Don’t use any custom classes.

- Don’t use runtime attributes.

If you create your iOS app from a storyboard template, Xcode adds a default launch screen file, called LaunchScreen.storyboard, to your project. Edit LaunchScreen.storyboard to configure your launch screen.

If your project doesn’t contain a default launch screen file, add a launch screen file and set the launch screen file for the target in the project editor.

1. Choose File > New > File from Template.

2. Under User Interface, select Launch Screen, and click Next.

3. Give the launch screen file a name, choose a location, select the target that you want to add the file to, and click Create.

4. In the settings for your target, select the General tab and find the “App Icons and Launch Screen” section.

5. From the Launch Screen File pop-up menu, choose the new launch screen file.



## App icons and launch screen

- Creating your app icon using Icon Composer: Use Icon Composer to stylize your app icon for different platforms and appearances.

- Configuring your app to use alternate app icons: Add alternate app icons to your app, and let people choose which icon to display.

- Configuring your app icon using an asset catalog: Add app icon variations to an asset catalog that represents your app in places such as the App Store, the Home Screen, Settings, and search results.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/ITSAppUsesNonExemptEncryption
# ITSAppUsesNonExemptEncryption

A Boolean value indicating whether the app uses encryption.

macOS 10.0

name: ITSAppUsesNonExemptEncryption

ideTitle: App Uses Non-Exempt Encryption

titleStyle: symbol

boolean

### Discussion

Set the value for this key to NO in your app’s Information Property List file to indicate that your app—including any third-party libraries you link against—either uses no encryption, or only uses encryption that’s exempt from export compliance requirements, as described in Overview of export compliance. Set the value to YES to indicate that your app uses non-exempt encryption.

If you set the value to YES, you typically also provide a value for the ITSEncryptionExportComplianceCode key. You set that key’s value using a code Apple provides after successfully reviewing your export compliance documentation.

If you don’t have the ITSAppUsesNonExemptEncryption key in your app’s Info.plist file, App Store Connect walks you through an export compliance questionnaire every time you upload a new version of your app. Including the key streamlines the app submission process.

For additional information, see Complying with Encryption Export Regulations.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/ITSEncryptionExportComplianceCode
# ITSEncryptionExportComplianceCode

The export compliance code provided by App Store Connect for apps that require it.

macOS 10.0

name: ITSEncryptionExportComplianceCode

ideTitle: App Encryption Export Compliance Code

titleStyle: symbol

string

### Discussion

Include this key in your app’s Information Property List file if you set the ITSAppUsesNonExemptEncryption key’s value to YES. Set the value for this key to the code that Apple sends you after successfully reviewing export compliance documentation that you provide through App Store Connect.

For additional information, see Complying with Encryption Export Regulations.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NFCReaderUsageDescription
# NFCReaderUsageDescription

A message that tells people why the app is requesting access to the device’s NFC hardware.

iOS 11.0, iPadOS 11.0

name: NFCReaderUsageDescription

ideTitle: Privacy - NFC Scan Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  You’re required to provide this key if your app uses APIs that access the NFC hardware.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAccessoryTrackingUsageDescription
# NSAccessoryTrackingUsageDescription

A message that tells a person why the app is requesting access to track accessory position and location.

visionOS 26.0

name: NSAccessoryTrackingUsageDescription

ideTitle: Privacy - Accessory Tracking Usage Description

titleStyle: symbol

string

### Discussion

Use this key to indicate that your app requires access to accessory-tracking data. The first time your app tries to access accessory-tracking data, the system prompts for permission. Provide a string for the prompt that explains why your app needs access.

## Vision

- NSWorldSensingUsageDescription: A message that tells people why the app is requesting access to image tracking, plane detection, or scene reconstruction.

- NSHandsTrackingUsageDescription: A message that tells people why the app is requesting access to track their hand position and location.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppBundlesUsageDescription
# NSAppBundlesUsageDescription

A message that tells people why the app needs to access the contents of other apps’ bundles.

macOS 13.0

name: NSAppBundlesUsageDescription

ideTitle: Privacy - App Management Usage Description

titleStyle: symbol

string

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppDataUsageDescription
# NSAppDataUsageDescription

A message that tells people why the app needs to access files in other apps’ sandbox containers.

macOS 14.0

name: NSAppDataUsageDescription

ideTitle: Privacy - Other Application Data Usage Description

titleStyle: symbol

string

### Discussion

When your app tries to open a file that’s in another app’s sandbox container, the system requests permission from the person using the app and presents this message. If your app doesn’t have a value for the NSAppDataUsageDescription key in its information property list, the system presents a default message.

The system uses this message any time your app tries to access files in another app’s container, and your app can’t provide different messages for attempts to access containers from different apps.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppleEventsUsageDescription
# NSAppleEventsUsageDescription

A message that tells people why the app is requesting the ability to send Apple events.

macOS 10.14

name: NSAppleEventsUsageDescription

ideTitle: Privacy - AppleEvents Sending Usage Description

titleStyle: symbol

string

### Discussion

An app using Apple events to control another app might be able to gain access to sensitive user data. For example, the Mail app stores a lot of personal information in its local database that other apps can’t access directly. But because Mail can be automated with Apple events, other apps can use Mail to gain access to the data indirectly.

[Important]

Important:  This key is required if your app uses APIs that send Apple events.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription
# NSAppleMusicUsageDescription

A message that tells people why the app is requesting access to their media library.

iOS 2.0, iPadOS 2.0, macOS 15.0, visionOS 1.0

name: NSAppleMusicUsageDescription

ideTitle: Privacy - Media Library Usage Description

titleStyle: symbol

string

### Discussion

Set the value of this key to a user-readable description of how your app intends to use a person’s media library. The first time your app attempts to access their library, the system prompts the user to grant or deny access to your app. The system includes this key’s description in the dialog it displays to the user.

[Important]

Important:  Your app must provide a value for this key to access a person’s media library. This requirement applies to iOS, iPadOS, visionOS, and macOS apps that link against the macOS 15 SDK or later.

## MediaPlayer

- Requesting Access to Apple Music Library: Prompt the customer to authorize access to Apple Music library.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAppleScriptEnabled
# NSAppleScriptEnabled

A Boolean value indicating whether AppleScript is enabled.

macOS 10.0

name: NSAppleScriptEnabled

ideTitle: Scriptable

titleStyle: symbol

boolean

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSAudioCaptureUsageDescription
# NSAudioCaptureUsageDescription

A message that tells people why your app is requesting access to capture system audio on macOS.

macOS 14.2

name: NSAudioCaptureUsageDescription

titleStyle: symbol

string

### Discussion

For more information, see Capturing system audio with Core Audio taps.

## Camera and sound

- Requesting authorization to capture and save media: Prompt the user to authorize access to the camera, microphone, and photo library.

- Requesting Authorization for Media Capture on macOS: Prompt the user to authorize access to the camera and microphone.

- NSCameraUsageDescription: A message that tells people why the app is requesting access to the device’s camera.

- NSMainCameraUsageDescription: A message that tells people why the app is requesting access to the device’s main camera.

- NSMicrophoneUsageDescription: A message that tells people why the app is requesting access to the device’s microphone.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSBluetoothAlwaysUsageDescription
# NSBluetoothAlwaysUsageDescription

A message that tells people why the app needs access to Bluetooth.

iOS 13.0, iPadOS 13.0, macOS 11.0, tvOS 13.0, visionOS 1.0, watchOS 6.0

name: NSBluetoothAlwaysUsageDescription

ideTitle: Privacy - Bluetooth Always Usage Description

titleStyle: symbol

string

### Discussion

This key is required if your app uses the device’s Bluetooth interface.

[Important]

Important:  If your app has a deployment target earlier than iOS 13, add the NSBluetoothPeripheralUsageDescription key to your app’s Information Property List file in addition to this key.

## Bluetooth

- NSBluetoothPeripheralUsageDescription: A message that tells people why the app is requesting the ability to connect to Bluetooth peripherals.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSBluetoothPeripheralUsageDescription
# NSBluetoothPeripheralUsageDescription

A message that tells people why the app is requesting the ability to connect to Bluetooth peripherals.

iOS 6.0, iPadOS 6.0

name: NSBluetoothPeripheralUsageDescription

ideTitle: Privacy - Bluetooth Peripheral Usage Description

titleStyle: symbol

string

### Discussion

For apps with a deployment target of iOS 13 and later, use NSBluetoothAlwaysUsageDescription instead.

For deployment targets earlier than iOS 13, add both NSBluetoothAlwaysUsageDescription and NSBluetoothPeripheralUsageDescription to your app’s Information Property List file. Devices running earlier versions of iOS rely on NSBluetoothPeripheralUsageDescription, while devices running later versions rely on NSBluetoothAlwaysUsageDescription.

[Important]

Important:  This key is required if your app uses APIs that access Bluetooth peripherals and has a deployment target earlier than iOS 13.

## Bluetooth

- NSBluetoothAlwaysUsageDescription: A message that tells people why the app needs access to Bluetooth.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSCalendarsFullAccessUsageDescription
# NSCalendarsFullAccessUsageDescription

A message that tells people why the app is requesting access to read and write their calendar data.

iOS 17.0, iPadOS 17.0, Mac Catalyst 17.0, macOS 14.0, visionOS 1.0, watchOS 10.0

name: NSCalendarsFullAccessUsageDescription

ideTitle: Privacy - Calendars Full Access Usage Description

titleStyle: symbol

string

### Discussion

If your app needs to create calendar events but doesn’t need to read them, use NSCalendarsWriteOnlyAccessUsageDescription. If your app runs on iOS 17 or later and presents an EKEventEditViewController to allow people to create calendar events, you don’t need to request calendar access.

[Important]

Important:  This key is required if your app uses APIs that read and write the person’s calendar data.

## Calendar and reminders

- NSCalendarsWriteOnlyAccessUsageDescription: A message that tells people why the app is requesting access to create calendar events.

- NSRemindersFullAccessUsageDescription: A message that tells people why the app is requesting access to read and write their reminders data.

- Accessing the event store: Request access to a person’s calendar data through the event store.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSCalendarsUsageDescription
# NSCalendarsUsageDescription

A message that tells people why the app is requesting access to their calendar data.

iOS 6.0, iPadOS 6.0, Mac Catalyst 13.0, macOS 10.14, watchOS 6.0

name: NSCalendarsUsageDescription

ideTitle: Privacy - Calendars Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the person’s calendar data.

## Deprecated keys

- NSEnterpriseMCAMUsageDescription: A message that tells people why the app is requesting access to the device’s main camera.

- NSRemindersUsageDescription: A message that tells people why the app is requesting access to their reminders.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSCalendarsWriteOnlyAccessUsageDescription
# NSCalendarsWriteOnlyAccessUsageDescription

A message that tells people why the app is requesting access to create calendar events.

iOS 17.0, iPadOS 17.0, Mac Catalyst 17.0, macOS 14.0, visionOS 1.0, watchOS 10.0

name: NSCalendarsWriteOnlyAccessUsageDescription

ideTitle: Privacy - Calendars Write Only Usage Description

titleStyle: symbol

string

### Discussion

If your app needs to read calendar events in addition to creating them, use NSCalendarsFullAccessUsageDescription. If your app runs on iOS 17 or later and presents an EKEventEditViewController to allow people to create calendar events, you don’t need to request calendar access.

[Important]

Important:  This key is required if your app uses APIs that write to the person’s calendar data.

## Calendar and reminders

- NSCalendarsFullAccessUsageDescription: A message that tells people why the app is requesting access to read and write their calendar data.

- NSRemindersFullAccessUsageDescription: A message that tells people why the app is requesting access to read and write their reminders data.

- Accessing the event store: Request access to a person’s calendar data through the event store.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription
# NSCameraUsageDescription

A message that tells people why the app is requesting access to the device’s camera.

iOS 7.0, iPadOS 7.0, macOS 10.14, tvOS 17.0, visionOS 1.0

name: NSCameraUsageDescription

ideTitle: Privacy - Camera Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the device’s camera.

## Camera and sound

- Requesting authorization to capture and save media: Prompt the user to authorize access to the camera, microphone, and photo library.

- Requesting Authorization for Media Capture on macOS: Prompt the user to authorize access to the camera and microphone.

- NSAudioCaptureUsageDescription: A message that tells people why your app is requesting access to capture system audio on macOS.

- NSMainCameraUsageDescription: A message that tells people why the app is requesting access to the device’s main camera.

- NSMicrophoneUsageDescription: A message that tells people why the app is requesting access to the device’s microphone.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSContactsUsageDescription
# NSContactsUsageDescription

A message that tells people why the app is requesting access to their contacts.

iOS 6.0, iPadOS 6.0, macOS 10.8, visionOS 1.0

name: NSContactsUsageDescription

ideTitle: Privacy - Contacts Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the user’s contacts.

## Contacts

- Accessing the contact store: Request permission from the person to read and write their contact data.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSCriticalMessagingUsageDescription
# NSCriticalMessagingUsageDescription

A message that tells people why the app needs to send SMS messages.

iOS 18.2, iPadOS 18.2, watchOS 11.2

name: NSCriticalMessagingUsageDescription

ideTitle: Privacy - Critical Messaging Usage Description

titleStyle: symbol

string

## Messages

- NSStickerSharingLevel: 

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSDesktopFolderUsageDescription
# NSDesktopFolderUsageDescription

A message that tells people why the app needs access to their Desktop folder.

macOS 10.15

name: NSDesktopFolderUsageDescription

ideTitle: Privacy - Desktop Folder Usage Description

titleStyle: symbol

string

### Discussion

The user implicitly grants your app access to a file in the Desktop folder when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file in the Desktop folder, the app can access that file without user consent.

The first time your app tries to access a file in the user’s Desktop folder without implied user consent, the system prompts the user for permission to access the folder’s contents. Add the NSDesktopFolderUsageDescription key to your app’s Information Property List file to provide a message that explains why your app needs access. The usage description is optional, but highly recommended.

App Sandbox enforces stricter limits on Desktop folder access, so that policy may supersede this one if your app enables sandboxing. See App Sandbox for more information.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the tccutil command line utility with your app’s bundle ID:

$ tccutil reset SystemPolicyDesktopFolder <bundleID>

## Files and folders

- NSDocumentsFolderUsageDescription: 

- NSDownloadsFolderUsageDescription: A message that tells people why the app needs access to the user’s Downloads folder.

- NSNetworkVolumesUsageDescription: A message that tells people why the app needs access to files on a network volume.

- NSRemovableVolumesUsageDescription: A message that tells people why the app needs access to files on a removable volume.

- NSFileProviderDomainUsageDescription: A message that tells people why the app needs access to files managed by a file provider.

- NSFileProviderPresenceUsageDescription: A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSDocumentsFolderUsageDescription
# NSDocumentsFolderUsageDescription



macOS 10.15

name: NSDocumentsFolderUsageDescription

ideTitle: Privacy - Documents Folder Usage Description

titleStyle: symbol

string

### Discussion

The user implicitly grants your app access to a file in the Documents folder when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file in the Documents folder, the app can access that file without user consent.

The first time your app tries to access a file in the user’s Documents folder without implied user consent, the system prompts the user for permission to access the folder’s contents. Add the NSDocumentsFolderUsageDescription key to your app’s Information Property List file to provide a message that explains why your app needs access. The usage description is optional, but highly recommended.

App Sandbox enforces stricter limits on Documents folder access, so that policy may supersede this one if your app enables sandboxing. See App Sandbox for more information.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the tccutil command line utility with your app’s bundle ID:

$ tccutil reset SystemPolicyDocumentsFolder <bundleID>

## Files and folders

- NSDesktopFolderUsageDescription: A message that tells people why the app needs access to their Desktop folder.

- NSDownloadsFolderUsageDescription: A message that tells people why the app needs access to the user’s Downloads folder.

- NSNetworkVolumesUsageDescription: A message that tells people why the app needs access to files on a network volume.

- NSRemovableVolumesUsageDescription: A message that tells people why the app needs access to files on a removable volume.

- NSFileProviderDomainUsageDescription: A message that tells people why the app needs access to files managed by a file provider.

- NSFileProviderPresenceUsageDescription: A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSDownloadsFolderUsageDescription
# NSDownloadsFolderUsageDescription

A message that tells people why the app needs access to the user’s Downloads folder.

macOS 10.15

name: NSDownloadsFolderUsageDescription

ideTitle: Privacy - Downloads Folder Usage Description

titleStyle: symbol

string

### Discussion

The user implicitly grants your app access to a file in the Downloads folder when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file in the Downloads folder, the app can access that file without user consent.

The first time your app tries to access a file in the user’s Downloads folder without implied user consent, the system prompts the user for permission to access the folder’s contents. Add the NSDownloadsFolderUsageDescription key to your app’s Information Property List file to provide a message that explains why your app needs access. The usage description is optional, but highly recommended.

App Sandbox enforces stricter limits on Downloads folder access, so that policy may supersede this one if your app enables sandboxing. See App Sandbox for more information.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the tccutil command line utility with your app’s bundle ID:

$ tccutil reset SystemPolicyDownloadsFolder <bundleID>

## Files and folders

- NSDesktopFolderUsageDescription: A message that tells people why the app needs access to their Desktop folder.

- NSDocumentsFolderUsageDescription: 

- NSNetworkVolumesUsageDescription: A message that tells people why the app needs access to files on a network volume.

- NSRemovableVolumesUsageDescription: A message that tells people why the app needs access to files on a removable volume.

- NSFileProviderDomainUsageDescription: A message that tells people why the app needs access to files managed by a file provider.

- NSFileProviderPresenceUsageDescription: A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSEnterpriseMCAMUsageDescription
# NSEnterpriseMCAMUsageDescription

A message that tells people why the app is requesting access to the device’s main camera.

visionOS 2.0

name: NSEnterpriseMCAMUsageDescription

ideTitle: Main Camera Usage Description

titleStyle: symbol

string

### Discussion

The system uses this string in visionOS 2-2.3 to tell someone why your app requests permission to use the main camera. In newer versions of visionOS, the system uses the value of NSMainCameraUsageDescription instead.

For information about using the main camera in your visionOS app, see Accessing the main camera.

## Deprecated keys

- NSCalendarsUsageDescription: A message that tells people why the app is requesting access to their calendar data.

- NSRemindersUsageDescription: A message that tells people why the app is requesting access to their reminders.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSFaceIDUsageDescription
# NSFaceIDUsageDescription

A message that tells people why the app is requesting the ability to authenticate with Face ID.

iOS 11.0, iPadOS 11.0

name: NSFaceIDUsageDescription

ideTitle: Privacy - Face ID Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access Face ID. Also note that App Clips can’t use Face ID. For more information about functionality that’s unavailable to App Clips, see Choosing the right functionality for your App Clip.

## Face ID

- Logging a User into Your App with Face ID or Touch ID: Supplement your own authentication scheme with biometric authentication, making it easy for users to access sensitive parts of your app.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription
# NSFallDetectionUsageDescription

A message to the user that explains the app’s request for permission to access fall detection event data.

iOS 14.2, iPadOS 14.2, visionOS 1.0, watchOS 7.2

name: NSFallDetectionUsageDescription

ideTitle: Privacy - Fall Detection Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  If your app uses the CMFallDetectionManager, the app requires this key.

## Motion

- NSMotionUsageDescription: A message that tells people why the app is requesting access to the device’s motion data.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSFileProviderDomainUsageDescription
# NSFileProviderDomainUsageDescription

A message that tells people why the app needs access to files managed by a file provider.

macOS 10.15

name: NSFileProviderDomainUsageDescription

ideTitle: Privacy - Access to a File Provide Domain Usage Description

titleStyle: symbol

string

### Discussion

The user implicitly grants your app access to a file managed by a file provider when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file managed by a file provider, the app can access that file without user consent.

The first time your app tries to access a file managed by a file provider without implied user consent, the system prompts the user for permission. Add the NSFileProviderDomainUsageDescription key to your app’s Information Property List file to provide a string for the prompt that explains why your app needs access. The usage description is optional, but highly recommended.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the tccutil command line utility with your app’s bundle ID:

$ tccutil reset FileProviderDomain <bundleID>

## Files and folders

- NSDesktopFolderUsageDescription: A message that tells people why the app needs access to their Desktop folder.

- NSDocumentsFolderUsageDescription: 

- NSDownloadsFolderUsageDescription: A message that tells people why the app needs access to the user’s Downloads folder.

- NSNetworkVolumesUsageDescription: A message that tells people why the app needs access to files on a network volume.

- NSRemovableVolumesUsageDescription: A message that tells people why the app needs access to files on a removable volume.

- NSFileProviderPresenceUsageDescription: A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSFileProviderPresenceUsageDescription
# NSFileProviderPresenceUsageDescription

A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

macOS 10.15

name: NSFileProviderPresenceUsageDescription

ideTitle: Privacy - File Provider Presence Usage Description

titleStyle: symbol

string

## Files and folders

- NSDesktopFolderUsageDescription: A message that tells people why the app needs access to their Desktop folder.

- NSDocumentsFolderUsageDescription: 

- NSDownloadsFolderUsageDescription: A message that tells people why the app needs access to the user’s Downloads folder.

- NSNetworkVolumesUsageDescription: A message that tells people why the app needs access to files on a network volume.

- NSRemovableVolumesUsageDescription: A message that tells people why the app needs access to files on a removable volume.

- NSFileProviderDomainUsageDescription: A message that tells people why the app needs access to files managed by a file provider.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSFinancialDataUsageDescription
# NSFinancialDataUsageDescription

A message that tells people why the app is requesting access to financial data stored in Wallet.

iOS 17.4, iPadOS 17.4

name: NSFinancialDataUsageDescription

ideTitle: Privacy - Financial Data Usage Description

titleStyle: symbol

string

## Wallet

- NSIdentityUsageDescription: A message that tells people why the app is requesting identity information.

- NSIdentityUsageDescriptionDictionary: A dictionary that contains messages that explain why your app is requesting identity information.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSGKFriendListUsageDescription
# NSGKFriendListUsageDescription

A message that tells people why the app needs access to their Game Center friends list.

iOS 14.5, iPadOS 14.5

name: NSGKFriendListUsageDescription

titleStyle: symbol

string

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSHandsTrackingUsageDescription
# NSHandsTrackingUsageDescription

A message that tells people why the app is requesting access to track their hand position and location.

visionOS 1.0

name: NSHandsTrackingUsageDescription

ideTitle: Privacy - Hands Tracking Usage Description

titleStyle: symbol

string

### Discussion

Use this key to indicate that your app requires access to hand-tracking data. This includes hand skeleton, wrist, and forearm position and location. The first time your app tries to access hand-tracking data, the system prompts for permission. Provide a string for the prompt that explains why your app needs access. For more information on setting up ARKit for hand tracking, see Setting up access to ARKit data.

## Vision

- NSWorldSensingUsageDescription: A message that tells people why the app is requesting access to image tracking, plane detection, or scene reconstruction.

- NSAccessoryTrackingUsageDescription: A message that tells a person why the app is requesting access to track accessory position and location.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSHealthClinicalHealthRecordsShareUsageDescription
# NSHealthClinicalHealthRecordsShareUsageDescription

A message to the user that explains why the app requested permission to read clinical records.

iOS 12.0, iPadOS 12.0, visionOS 1.0

name: NSHealthClinicalHealthRecordsShareUsageDescription

ideTitle: Privacy - Health Records Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the user’s clinical records.

## Health

- Setting up HealthKit: Set up and configure your HealthKit store.

- NSHealthShareUsageDescription: A message that explains to people why the app requests permission to read samples from the HealthKit store.

- NSHealthUpdateUsageDescription: A message to the user that explains why the app requested permission to save samples to the HealthKit store.

- NSHealthRequiredReadAuthorizationTypeIdentifiers: The clinical record data types that your app must get permission to read.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSHealthRequiredReadAuthorizationTypeIdentifiers
# NSHealthRequiredReadAuthorizationTypeIdentifiers

The clinical record data types that your app must get permission to read.

iOS 12.0, iPadOS 12.0, visionOS 1.0

name: NSHealthRequiredReadAuthorizationTypeIdentifiers

titleStyle: symbol

string 

### Discussion

Use this key to indicate that your app requires access to specific clinical record data types to function properly. Set the value to an array of strings containing the type identifiers for your required types. For a list of type identifiers, see HKClinicalTypeIdentifier.

To protect the user’s privacy, you must specify three or more required clinical record types. If the user denies authorization to any of the types, authorization fails with an HKError.Code.errorRequiredAuthorizationDenied error. Your app is not told the record types to which the user denied access.

## Health

- Setting up HealthKit: Set up and configure your HealthKit store.

- NSHealthClinicalHealthRecordsShareUsageDescription: A message to the user that explains why the app requested permission to read clinical records.

- NSHealthShareUsageDescription: A message that explains to people why the app requests permission to read samples from the HealthKit store.

- NSHealthUpdateUsageDescription: A message to the user that explains why the app requested permission to save samples to the HealthKit store.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSHealthShareUsageDescription
# NSHealthShareUsageDescription

A message that explains to people why the app requests permission to read samples from the HealthKit store.

iOS 8.0, iPadOS 8.0, visionOS 1.0

name: NSHealthShareUsageDescription

ideTitle: Privacy - Health Share Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the someone’s health data.

## Health

- Setting up HealthKit: Set up and configure your HealthKit store.

- NSHealthClinicalHealthRecordsShareUsageDescription: A message to the user that explains why the app requested permission to read clinical records.

- NSHealthUpdateUsageDescription: A message to the user that explains why the app requested permission to save samples to the HealthKit store.

- NSHealthRequiredReadAuthorizationTypeIdentifiers: The clinical record data types that your app must get permission to read.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSHealthUpdateUsageDescription
# NSHealthUpdateUsageDescription

A message to the user that explains why the app requested permission to save samples to the HealthKit store.

iOS 8.0, iPadOS 8.0, visionOS 1.0

name: NSHealthUpdateUsageDescription

ideTitle: Privacy - Health Update Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that update the user’s health data.

## Health

- Setting up HealthKit: Set up and configure your HealthKit store.

- NSHealthClinicalHealthRecordsShareUsageDescription: A message to the user that explains why the app requested permission to read clinical records.

- NSHealthShareUsageDescription: A message that explains to people why the app requests permission to read samples from the HealthKit store.

- NSHealthRequiredReadAuthorizationTypeIdentifiers: The clinical record data types that your app must get permission to read.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSHomeKitUsageDescription
# NSHomeKitUsageDescription

A message that tells people why the app is requesting access to their HomeKit configuration data.

iOS 8.0, iPadOS 8.0, visionOS 1.0, watchOS 2.0

name: NSHomeKitUsageDescription

ideTitle: Privacy - HomeKit Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the user’s HomeKit configuration data.

For more information about using HomeKit in your app, see Enabling HomeKit in your app.

## Home

- Enabling HomeKit in your app: Declare your app’s intention to use HomeKit, and get permission from the user to access home automation accessories.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSIdentityUsageDescription
# NSIdentityUsageDescription

A message that tells people why the app is requesting identity information.

iOS 16.0, iPadOS 16.0, visionOS 1.0

name: NSIdentityUsageDescription

ideTitle: Privacy - Identity Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access identity information from Wallet.

For more information about requesting identity information, see Requesting identity data from a Wallet pass. For design guidance, see Human Interface Guidelines > Technologies > Wallet.

## Wallet

- NSFinancialDataUsageDescription: A message that tells people why the app is requesting access to financial data stored in Wallet.

- NSIdentityUsageDescriptionDictionary: A dictionary that contains messages that explain why your app is requesting identity information.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSIdentityUsageDescriptionDictionary
# NSIdentityUsageDescriptionDictionary

A dictionary that contains messages that explain why your app is requesting identity information.

iOS 26.2, iPadOS 26.2, visionOS 1.0

name: NSIdentityUsageDescriptionDictionary

ideTitle: Privacy - Identity Usage Description Dictionary

titleStyle: symbol

dictionary

### Discussion

Use this key when you have multiple scenarios for requesting identity information from a person. Provide a description string for each use case, and key each entry with a string that you define. For example, if your app needs age verification for one feature and identity verification for another, use a separate dictionary entry for each purpose. In each description string, describe the reason the feature requires identity information.

The following image shows two description strings that use NSIdentityUsageDescriptionDictionary.



[Note]

Note: The dictionary allows up to 5 entries, and each usage description string allows up to 256 characters.

For more information about requesting identity information, see Requesting identity data from a Wallet pass. For design guidance, see Human Interface Guidelines > Technologies > Wallet.

## Wallet

- NSFinancialDataUsageDescription: A message that tells people why the app is requesting access to financial data stored in Wallet.

- NSIdentityUsageDescription: A message that tells people why the app is requesting identity information.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription
# NSLocalNetworkUsageDescription

A message that tells people why the app is requesting access to the local network.

iOS 14.0, iPadOS 14.0, macOS 11.0, tvOS 14.0, visionOS 1.0

name: NSLocalNetworkUsageDescription

ideTitle: Privacy - Local Network Usage Description

titleStyle: symbol

string

### Discussion

Any app that uses the local network, directly or indirectly, should include this description. This includes apps that use Bonjour and services implemented with Bonjour, as well as direct unicast or multicast connections to local hosts.

## Networking

- NSNearbyInteractionUsageDescription: A request for user permission to begin an interaction session with nearby devices.

- NSNearbyInteractionAllowOnceUsageDescription: A one-time request for user permission to begin an interaction session with nearby devices.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription
# NSLocationAlwaysAndWhenInUseUsageDescription

A message that tells people why the app is requesting access to their location information at all times.

iOS 11.0, iPadOS 11.0, visionOS 1.0

name: NSLocationAlwaysAndWhenInUseUsageDescription

ideTitle: Privacy - Location Always and When In Use Usage Description

titleStyle: symbol

string

### Discussion

Use this key if your iOS app accesses location information while running in the background. If your app only needs location information when in the foreground, use NSLocationWhenInUseUsageDescription instead. For more information, see Choosing the  Location Services Authorization to Request.

If you need location information in a macOS app, use NSLocationUsageDescription instead. If your iOS app deploys to versions earlier than iOS 11, see NSLocationAlwaysUsageDescription.

[Important]

Important:  This key is required if your iOS app uses APIs that access the user’s location information at all times.

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription
# NSLocationAlwaysUsageDescription

A message that tells people why the app is requesting access to their location at all times.

iOS 8.0, iPadOS 8.0

name: NSLocationAlwaysUsageDescription

ideTitle: Privacy - Location Always Usage Description

titleStyle: symbol

string

### Discussion

Use this key if your iOS app accesses location information in the background, and you deploy to a target earlier than iOS 11. In that case, add both this key and NSLocationAlwaysAndWhenInUseUsageDescription to your app’s Info.plist file with the same message. Apps running on older versions of the OS use the message associated with NSLocationAlwaysUsageDescription, while apps running on later versions use the one associated with NSLocationAlwaysAndWhenInUseUsageDescription.

If your app only needs location information when in the foreground, use NSLocationWhenInUseUsageDescription instead. For more information, see Choosing the  Location Services Authorization to Request.

If you need location information in a macOS app, use NSLocationUsageDescription instead.

[Important]

Important:  This key is required if your iOS app uses APIs that access the user’s location at all times and deploys to targets earlier than iOS 11.

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced
# NSLocationDefaultAccuracyReduced

A Boolean value that indicates whether the app requests reduced location accuracy by default.

iOS 14.0, iPadOS 14.0, visionOS 1.0, watchOS 7.0

name: NSLocationDefaultAccuracyReduced

ideTitle: Privacy - Location Default Accuracy Reduced

titleStyle: symbol

boolean

### Discussion

Include this key in your information property list to set your app’s default behavior for location accuracy when it calls the Core Location framework. Set the key value to true to prompt the user for reduced accuracy by default; set it to false to prompt for full location accuracy. If you don’t include that key in your Info.plist, that’s equivalent to setting it to false.

Include the key pair in your Info.plist file as shown:

<!-- Info.plist -->
<key>NSLocationDefaultAccuracyReduced</key>
<true/>

When this key is set to true, all Core Location services (location updates, visit monitoring, significant location change, fence monitoring) receive service at the reduced-accuracy service level.  Users will see that your app is asking for reduced accuracy because the location authorization prompt will show a map with an approximate location, and your app will have the Precise Location toggled off in Settings > Privacy > Location Services . These indicators of an app’s improved privacy are ones that users may value.

If you want to leverage the reduced-accuracy feature to improve privacy in a particular operation without setting this key, use the desiredAccuracy constant kCLLocationAccuracyReduced. This constant causes startUpdatingLocation() to deliver results as if the app were authorized for approximate location until you change the desiredAccuracy constant again.

Setting NSLocationDefaultAccuracyReduced determines the default type of authorization your app gets, but users can override it any time in Settings. Users always control the level of location accuracy they want to share, and can change precision settings in Settings > Privacy > Location Services by selecting Precise Location for your app.

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSLocationTemporaryUsageDescriptionDictionary
# NSLocationTemporaryUsageDescriptionDictionary

A collection of messages that explain why the app is requesting temporary access to their location.

iOS 14.0, iPadOS 14.0, macOS 11.0, visionOS 1.0

name: NSLocationTemporaryUsageDescriptionDictionary

ideTitle: Privacy - Location Temporary Usage Description Dictionary

titleStyle: symbol

dictionary

### Discussion

Use this key if your app needs temporary access to full accuracy location information. Provide a dictionary of messages that address different use cases, keyed by strings that you define. For example, if your app suggests nearby coffee shops in one part of the app, and finds nearby friends in another, you could include two entries:



When you request access, select among the messages at run time by providing the associated key to the requestTemporaryFullAccuracyAuthorization(withPurposeKey:) method:

// Request location access to find coffee shops.
manager.requestTemporaryFullAccuracyAuthorization(withPurposeKey: "coffee")

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSLocationUsageDescription
# NSLocationUsageDescription

A message that tells people why the app is requesting access to their location information.

iOS 6.0, iPadOS 6.0, macOS 10.14

name: NSLocationUsageDescription

ideTitle: Privacy - Location Usage Description

titleStyle: symbol

string

### Discussion

Use this key in a macOS app that accesses the user’s location information. In an iOS app, use NSLocationWhenInUseUsageDescription or NSLocationAlwaysAndWhenInUseUsageDescription instead.

[Important]

Important:  This key is required if your macOS app uses APIs that access the user’s location information.

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription
# NSLocationWhenInUseUsageDescription

A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

iOS 11.0, iPadOS 11.0, visionOS 1.0

name: NSLocationWhenInUseUsageDescription

ideTitle: Privacy - Location When In Use Usage Description

titleStyle: symbol

string

### Discussion

Use this key if your iOS app accesses location information only when running in the foreground. If your app needs location information when in the background, use NSLocationAlwaysAndWhenInUseUsageDescription instead. For more information, see Choosing the  Location Services Authorization to Request.

If you need location information in a macOS app, use NSLocationUsageDescription instead.

[Important]

Important:  This key is required if your iOS app uses APIs that access the user’s location information while the app is in use.

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSWidgetWantsLocation: A Boolean value that indicates a widget uses the user’s location information.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSMainCameraUsageDescription
# NSMainCameraUsageDescription

A message that tells people why the app is requesting access to the device’s main camera.

visionOS 26.0

name: NSMainCameraUsageDescription

ideTitle: Main Camera Usage Description

titleStyle: symbol

string

### Discussion

The system uses this string to tell someone why your app requests permission to use the main camera. In visionOS 2-2.3, the system uses the value of NSEnterpriseMCAMUsageDescription instead.

For information about using the main camera in your visionOS app, see Accessing the main camera.

[Important]

Important:  This key is required if your app uses APIs that access the device’s main camera.

## Camera and sound

- Requesting authorization to capture and save media: Prompt the user to authorize access to the camera, microphone, and photo library.

- Requesting Authorization for Media Capture on macOS: Prompt the user to authorize access to the camera and microphone.

- NSAudioCaptureUsageDescription: A message that tells people why your app is requesting access to capture system audio on macOS.

- NSCameraUsageDescription: A message that tells people why the app is requesting access to the device’s camera.

- NSMicrophoneUsageDescription: A message that tells people why the app is requesting access to the device’s microphone.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription
# NSMicrophoneUsageDescription

A message that tells people why the app is requesting access to the device’s microphone.

iOS 7.0, iPadOS 7.0, macOS 10.14, tvOS 17.0, visionOS 1.0, watchOS 4.0

name: NSMicrophoneUsageDescription

ideTitle: Privacy - Microphone Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the device’s microphone.

## Camera and sound

- Requesting authorization to capture and save media: Prompt the user to authorize access to the camera, microphone, and photo library.

- Requesting Authorization for Media Capture on macOS: Prompt the user to authorize access to the camera and microphone.

- NSAudioCaptureUsageDescription: A message that tells people why your app is requesting access to capture system audio on macOS.

- NSCameraUsageDescription: A message that tells people why the app is requesting access to the device’s camera.

- NSMainCameraUsageDescription: A message that tells people why the app is requesting access to the device’s main camera.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription
# NSMotionUsageDescription

A message that tells people why the app is requesting access to the device’s motion data.

iOS 7.0, iPadOS 7.0, macOS 10.15, visionOS 1.0

name: NSMotionUsageDescription

ideTitle: Privacy - Motion Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the device’s motion data, including CMSensorRecorder, CMPedometer, CMMotionActivityManager, and CMMovementDisorderManager. If you don’t include this key, your app will crash when it attempts to access motion data.

## Motion

- NSFallDetectionUsageDescription: A message to the user that explains the app’s request for permission to access fall detection event data.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSNearbyInteractionAllowOnceUsageDescription
# NSNearbyInteractionAllowOnceUsageDescription

A one-time request for user permission to begin an interaction session with nearby devices.

iOS 14.0, iPadOS 14.0

name: NSNearbyInteractionAllowOnceUsageDescription

ideTitle: Privacy - Nearby Interaction Allow Once Usage Description

titleStyle: symbol

string

### Discussion

[Warning]

Warning:  Define this property in the Info.plist only for apps that deploy to iOS 14. NSNearbyInteractionUsageDescription replaces this property in iOS 15 and later.

Before an app starts an interaction session, the system requests permission to share the user’s relative distance and direction with a nearby peer. The framework presents a prompt that displays the value of this key contained in your project’s Info.plist. Define text that explains your interaction session’s purpose to the user. For more information, see Initiating and maintaining a session.

## Networking

- NSLocalNetworkUsageDescription: A message that tells people why the app is requesting access to the local network.

- NSNearbyInteractionUsageDescription: A request for user permission to begin an interaction session with nearby devices.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSNearbyInteractionUsageDescription
# NSNearbyInteractionUsageDescription

A request for user permission to begin an interaction session with nearby devices.

iOS 15.0, iPadOS 15.0, watchOS 8.0

name: NSNearbyInteractionUsageDescription

ideTitle: Privacy - Nearby Interaction Usage Description

titleStyle: symbol

string

### Discussion

This property defines localizable text that explains your interaction session’s purpose to the user.

Before an app starts an interaction session, the system checks whether the user agrees to share their relative distance and direction with a nearby peer. The first time the app runs, the framework presents a prompt that displays the value of this key contained in your project’s Info.plist. The system persists the user’s choice in Settings. After your app runs for the first time, it consults the user preference in Settings before it begins a new interaction session.

For more information, see Initiating and maintaining a session.

## Networking

- NSLocalNetworkUsageDescription: A message that tells people why the app is requesting access to the local network.

- NSNearbyInteractionAllowOnceUsageDescription: A one-time request for user permission to begin an interaction session with nearby devices.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSNetworkVolumesUsageDescription
# NSNetworkVolumesUsageDescription

A message that tells people why the app needs access to files on a network volume.

macOS 10.15

name: NSNetworkVolumesUsageDescription

ideTitle: Privacy - Network Volumes Usage Description

titleStyle: symbol

string

### Discussion

The user implicitly grants your app access to a file on a network volume when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file on a network volume, the app can access that file without user consent.

The first time your app tries to access a file on a network volume without implied user consent, the system prompts the user for permission to access network volumes. Add the NSNetworkVolumesUsageDescription key to your app’s Information Property List file to provide a string for the prompt that explains why your app needs access. The usage description is optional, but highly recommended.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the tccutil command line utility with your app’s bundle ID:

$ tccutil reset SystemPolicyNetworkVolumes <bundleID>

## Files and folders

- NSDesktopFolderUsageDescription: A message that tells people why the app needs access to their Desktop folder.

- NSDocumentsFolderUsageDescription: 

- NSDownloadsFolderUsageDescription: A message that tells people why the app needs access to the user’s Downloads folder.

- NSRemovableVolumesUsageDescription: A message that tells people why the app needs access to files on a removable volume.

- NSFileProviderDomainUsageDescription: A message that tells people why the app needs access to files managed by a file provider.

- NSFileProviderPresenceUsageDescription: A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSPhotoLibraryAddUsageDescription
# NSPhotoLibraryAddUsageDescription

A message that tells people why the app is requesting add-only access to their photo library.

iOS 11.0, iPadOS 11.0, visionOS 1.0

name: NSPhotoLibraryAddUsageDescription

ideTitle: Privacy - Photo Library Additions Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that have write access to the user’s photo library.

## Photos

- Delivering an Enhanced Privacy Experience in Your Photos App: Adopt the latest privacy enhancements to deliver advanced user-privacy controls.

- NSPhotoLibraryUsageDescription: A message that tells people why the app is requesting access to their photo library.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSPhotoLibraryUsageDescription
# NSPhotoLibraryUsageDescription

A message that tells people why the app is requesting access to their photo library.

iOS 6.0, iPadOS 6.0, macOS 10.14, visionOS 1.0

name: NSPhotoLibraryUsageDescription

ideTitle: Privacy - Photo Library Usage Description

titleStyle: symbol

string

### Discussion

If your app only adds assets to the photo library and does not read assets, use the  NSPhotoLibraryAddUsageDescription key instead.

[Important]

Important:  This key is required if your app uses APIs that have read or write access to the user’s photo library.

## Photos

- Delivering an Enhanced Privacy Experience in Your Photos App: Adopt the latest privacy enhancements to deliver advanced user-privacy controls.

- NSPhotoLibraryAddUsageDescription: A message that tells people why the app is requesting add-only access to their photo library.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSRemindersFullAccessUsageDescription
# NSRemindersFullAccessUsageDescription

A message that tells people why the app is requesting access to read and write their reminders data.

iOS 17.0, iPadOS 17.0, Mac Catalyst 17.0, macOS 14.0, visionOS 1.0, watchOS 10.0

name: NSRemindersFullAccessUsageDescription

ideTitle: Privacy - Reminders Full Access Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the person’s reminder data.

## Calendar and reminders

- NSCalendarsFullAccessUsageDescription: A message that tells people why the app is requesting access to read and write their calendar data.

- NSCalendarsWriteOnlyAccessUsageDescription: A message that tells people why the app is requesting access to create calendar events.

- Accessing the event store: Request access to a person’s calendar data through the event store.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSRemindersUsageDescription
# NSRemindersUsageDescription

A message that tells people why the app is requesting access to their reminders.

iOS 6.0, iPadOS 6.0, Mac Catalyst 13.0, macOS 10.14, watchOS 6.0

name: NSRemindersUsageDescription

ideTitle: Privacy - Reminders Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the person’s reminders.

## Deprecated keys

- NSCalendarsUsageDescription: A message that tells people why the app is requesting access to their calendar data.

- NSEnterpriseMCAMUsageDescription: A message that tells people why the app is requesting access to the device’s main camera.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSRemovableVolumesUsageDescription
# NSRemovableVolumesUsageDescription

A message that tells people why the app needs access to files on a removable volume.

macOS 10.15

name: NSRemovableVolumesUsageDescription

ideTitle: Privacy - Removable Volumes Usage Description

titleStyle: symbol

string

### Discussion

The user implicitly grants your app access to a file on a removable volume—like a USB thumb drive—when selecting the file in an Open or Save panel, dragging it onto your app, or opening it in Finder. Your app can access that file right away and any time in the future. In addition, if your app creates a new file on a removable volume, the app can access that file without user consent.

The first time your app tries to access a file on a removable volume without implied user consent, the system prompts the user for permission to access removable volumes. Add the NSRemovableVolumesUsageDescription key to your app’s Information Property List file to provide a string for the prompt that explains why your app needs access. The usage description is optional, but highly recommended.

After the user chooses whether to grant access, the system remembers the user’s choice. To reset permissions, use the tccutil command line utility with your app’s bundle ID:

$ tccutil reset SystemPolicyRemovableVolumes <bundleID>

## Files and folders

- NSDesktopFolderUsageDescription: A message that tells people why the app needs access to their Desktop folder.

- NSDocumentsFolderUsageDescription: 

- NSDownloadsFolderUsageDescription: A message that tells people why the app needs access to the user’s Downloads folder.

- NSNetworkVolumesUsageDescription: A message that tells people why the app needs access to files on a network volume.

- NSFileProviderDomainUsageDescription: A message that tells people why the app needs access to files managed by a file provider.

- NSFileProviderPresenceUsageDescription: A message that tells people why the app’s file provider needs to determine which files the person is currently accessing.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSSensorKitPrivacyPolicyURL
# NSSensorKitPrivacyPolicyURL

A hyperlink to a webpage that displays the privacy policy for your app’s research study.

iOS 14.0, iPadOS 14.0

name: NSSensorKitPrivacyPolicyURL

titleStyle: symbol

string

### Discussion

When your app attempts to read sensor information for the first time on a user’s device, the system presents a sheet that displays a link to your app’s privacy policy. Users approve or deny your app’s ability to read private sensor information based on their assessment of your app’s privacy policy.

For more information, see Configuring your project for sensor reading.

## Sensors

- NSSensorKitUsageDescription: A short description of the purpose of your app’s research study.

- NSSensorKitUsageDetail: A dictionary that includes keys for the specific information your app collects.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDescription
# NSSensorKitUsageDescription

A short description of the purpose of your app’s research study.

iOS 14.0, iPadOS 14.0

name: NSSensorKitUsageDescription

titleStyle: symbol

string

### Discussion

When your app attempts to read sensor information for the first time on a user’s device, the system presents this string to explain your app’s study. Users approve or deny your app’s ability to read private sensor information based on the description you provide for this property.

For more information, see Configuring your project for sensor reading.

## Sensors

- NSSensorKitUsageDetail: A dictionary that includes keys for the specific information your app collects.

- NSSensorKitPrivacyPolicyURL: A hyperlink to a webpage that displays the privacy policy for your app’s research study.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail
# NSSensorKitUsageDetail

A dictionary that includes keys for the specific information your app collects.

iOS 14.0, iPadOS 14.0

name: NSSensorKitUsageDetail

titleStyle: symbol

dictionary

### Discussion

When your app attempts to read sensor information for the first time on a user’s device, the system presents a sheet that describes the information your app collects. You specify which information by defining an Info.plist key in this dictionary for each sensor your app uses, such as SRSensorUsageAmbientLightSensor. Users approve or deny your app’s ability to read private sensor information based on the description you provide for these properties.

For more information, see Configuring your project for sensor reading.

## Device Activity

- SRSensorUsageDeviceUsage: A collection of properties that explain your app’s need to observe how frequently a user’s device activates.

- SRSensorUsageKeyboardMetrics: A collection of properties that explain your app’s need to observe the user’s keyboard activity.

- SRSensorUsageWristDetection: A collection of properties that explain your app’s need to observe how the user wears their watch.

## App Activity

- SRSensorUsageMessageUsage: A collection of properties that explain your app’s need to observe the user’s activity in Messages.

- SRSensorUsagePhoneUsage: A collection of properties that explain your app’s need to observe the user’s phone activity.

## User Activity

- SRSensorUsageECG: A collection of properties that explains your app’s need to observe the person’s electrocardiogram sensor data.

- SRSensorUsageElevation: A collection of properties that explains your app’s need to observe the device’s elevation data.

- SRSensorUsageFacialMetrics: A collection of properties that explains your app’s need to observe the user’s facial expressions.

- SRSensorUsageHeartRate: A collection of properties that explains your app’s need to observe the user’s heart rate.

- SRSensorUsageMediaEvents: A collection of properties that explains your app’s need to observe the user’s interactions with media, such as images and videos, in messaging apps.

- SRSensorUsageMotion: A collection of properties that explain your app’s need to observe motion data.

- SRSensorUsageOdometer: A collection of properties that explains your app’s need to observe the user’s odometer data.

- SRSensorUsagePedometer: A collection of properties that explain your app’s need to observe steps information.

- SRSensorUsagePPG: A collection of properties that explains your app’s need to observe the person’s photoplethysmogram sensor data.

- SRSensorUsageSpeechMetrics: A collection of properties that explain your app’s need to analyze the user’s speech.

- SRSensorUsageVisits: A collection of properties that explain your app’s need to observe the locations that the user frequents.

- SRSensorUsageWristTemperature: A collection of properties that explains your app’s need to observe the user’s wrist temperature while the user sleeps.

## Environment

- SRSensorUsageAmbientLightSensor: A collection of properties that explain your app’s need to observe light levels in the user’s environment.

## Sensors

- NSSensorKitUsageDescription: A short description of the purpose of your app’s research study.

- NSSensorKitPrivacyPolicyURL: A hyperlink to a webpage that displays the privacy policy for your app’s research study.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSSiriUsageDescription
# NSSiriUsageDescription

A message that tells people why the app is requesting to send user data to Siri.

iOS 10.0, iPadOS 10.0, visionOS 1.0

name: NSSiriUsageDescription

ideTitle: Privacy - Siri Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that send user data to Siri.

## Siri

- Requesting Authorization to Use Siri: Request permission from the user for Siri and Maps to communicate with your app or Intents app extension.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSSpeechRecognitionUsageDescription
# NSSpeechRecognitionUsageDescription

A message that tells people why the app is requesting to send user data to Apple’s speech recognition servers.

iOS 10.0, iPadOS 10.0, macOS 10.15, visionOS 1.0

name: NSSpeechRecognitionUsageDescription

ideTitle: Privacy - Speech Recognition Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  Include this key if your app uses the Speech framework. This applies regardless of whether you set requiresOnDeviceRecognition to true or false. If this key isn’t present, your app crashes when it calls requestAuthorization(_:).

## Speech

- Asking Permission to Use Speech Recognition: Ask the user’s permission to perform speech recognition using Apple’s servers.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSSystemAdministrationUsageDescription
# NSSystemAdministrationUsageDescription

A message in macOS that tells people why the app is requesting to manipulate the system configuration.

macOS 10.14

name: NSSystemAdministrationUsageDescription

ideTitle: Privacy - System Administration Usage Description

titleStyle: symbol

string

### Discussion

Use this key if your app uses certain APIs that manipulate system configuration, like ODRecordSetValue(_:_:_:_:).

[Important]

Important:  This key is required if your app uses APIs that manipulate the system configuration.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSSystemExtensionUsageDescription
# NSSystemExtensionUsageDescription

A message that tells people why the app is trying to install a system extension bundle.

iOS 18.4, iPadOS 18.4, Mac Catalyst 18.4, macOS 10.15

name: NSSystemExtensionUsageDescription

ideTitle: Privacy - System Extension Usage Description

titleStyle: symbol

string

### Discussion

This key is required for all system extensions except DriverKit extensions. Failure to include this key results in an error at activation time. For DriverKit extensions, use OSBundleUsageDescription instead.

## System Extensions

- OSBundleUsageDescription: A message that tells people why the app is trying to install a driver extension bundle.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSUpdateSecurityPolicy
# NSUpdateSecurityPolicy

A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

Mac Catalyst 16.0, macOS 13.0

name: NSUpdateSecurityPolicy

titleStyle: symbol

dictionary

### Discussion

The NSUpdateSecurityPolicy property list key describes a security policy dictionary that defines the processes and packages that the system allows to modify an app’s bundle. You specify these by Team ID (any package signed by that team), or Team IDs and signing identifiers (to identify a specific executable) signed by a team.

For signed apps, macOS allows apps from the same developer — those sharing the same Team ID — to modify the app’s bundle. Use this security policy to change the default behavior and customize which specific apps or installers can write to your app’s bundle.

If this protection mechanism isn’t relevant to your app, you can opt out of this capability and disable the hardened runtime by adding the com.apple.security.cs.disable-executable-page-protection entitlement to your app’s info.plist file. For information about this entitlement — and important information about the security ramifications of disabling this protection — see Disable Executable Memory Protection Entitlement.

The NSUpdateSecurityPolicy key is a dictionary you add to your app’s info.plist file in the source editor pane of your app’s Xcode target. Add the key following the instructions below, and add one or both of the dictionary’s subkeys, depending on the types of apps or installers you want to allow to perform updates to your app’s resources. The subkeys are:

- AllowPackages: An array of Team IDs. The operating system allows any installer package signed by any Team ID in this list to write content into this app’s bundle.

- AllowProcesses: A dictionary that maps Team IDs to an array of signing (bundle) IDs. The operating system allows an app (process) with the matching bundle ID that’s signed by the specified Team ID to write content into this app’s bundle.

#### Add the policy dictionary to your app’s information property list

To add the NSUpdateSecurityPolicy key to your app’s info.plist file, follow these steps:

1. In Xcode, select your app’s target from the Target navigator, and then select the source editor pane in the detail section.

2. Control-click the last item in the list, and choose Add Row from the drop-down menu.

3. Edit the text for the new row, replacing the existing text with NSUpdateSecurityPolicy, and press Return.

4. Control-click  the Type field for the new row and choose Dictionary from the drop-down menu.

5. Click the disclosure triangle next to the new NSUpdateSecurityPolicy dictionary to open it (the arrow needs to point down). This ensures that in the next steps, the editor adds elements inside the dictionary, and not as separate items parallel to it in the property list.

The newly created, empty NSUpdateSecurityPolicy dictionary in your app’s property list resembles the image below:



Next, add one or both subcomponents to the security policy dictionary depending on your app’s update policy requirements. To allow any installer package signed by a specific Team ID, add an AllowPackages array to the NSUpdateSecurityPolicy dictionary. Using this key, the operating system allows any installer package signed by the specified Team IDs in this array to write content into the app’s bundle.

1. Control-click the NSUpdateSecurityPolicy row in the property list and choose Add Row.

2. Edit the row name, replacing the default text with AllowPackages and press Return.

3. Control-click the new AllowPackages row’s Type drop-down menu and choose Array.

4. Control-click the new AllowPackages row and choose Add Row. This adds a new element to the AllowPackages array.

5. Set the value of the new array element to the Team ID of the team whose installers you’re authorizing to update this app.

6. Repeat steps 4 and 5 for each additional team whose installers you want to authorize.

To allow specific apps from specific teams to write to this app’s bundle, add an AllowProcesses dictionary to the NSUpdateSecurityPolicy dictionary. Using this key, and it’s subdictionaries, the operating system allows specific apps defined by both a Team ID and signing ID (also called a bundle ID) to write content into this app’s bundle.

1. Control-click the NSUpdateSecurityPolicy row in the property list and choose Add Row.

2. Edit the row name, replacing the default text with AllowProcesses and press Return.

3. Control-click the new AllowProcesses row’s Type drop-down menu and choose Dictionary.

4. Control-click the new AllowProcesses row and choose Add Row. This adds a new element to the AllowProcesses dictionary.

5. Control-click the new row’s Type drop-down menu, and choose Dictionary. Set the new row’s name to be the Team ID of the app or apps you want to allow to update this app’s bundle.

6. Control-click the new Team ID row, and add a row to the newly created team dictionary.

7. Control-click the new row’s Type drop-down menu and choose Array.

8. Control-click the array row, and add a new row to the array.

9. Set the value of the new array element to the signing ID (bundle ID) of the app you’re authorizing to write to the app’s bundle.

10. To add additional authorized apps for this Team ID, repeat steps 8 and 9.

11. To add additional teams and apps, repeat steps 5 through 9.

The final new NSUpdateSecurityPolicy dictionary resembles the configuration in the image below:



The following sample code describes a complete update policy, in JSON format, that allows any installer package signed by Team ID Z9P22VQP42 to write to the app bundle. The policy also allows a single app associated with the bundle ID com.example.myapp.updater (also signed with the Team ID Z9P22VQP42) that can modify the app bundle.

{
  "NSUpdateSecurityPolicy": {
    "AllowPackages": [
      0: "Z9P22VQP42"
    ]
    "AllowProcesses": {
      "Z9P22VQP42": [
        0: "com.example.myapp.updater"
      ]
    }
  }
}

## Security policies

- AllowPackages: An array of Team IDs that the system uses to determine whether an installer package, signed by one of the specified Team IDs, can update an app’s bundle.

- AllowProcesses: A dictionary that maps Team IDs to an array of signing (bundle) IDs that the system uses to determine whether a process can update an app’s bundle.

## Security

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSUserTrackingMarkdownUsageDescription
# NSUserTrackingMarkdownUsageDescription

A message that explains the purpose for accessing data that an application can use to track a person or device.

iOS 27.2, iPadOS 27.2

name: NSUserTrackingMarkdownUsageDescription

ideTitle: Privacy - Tracking Markdown Usage Description

titleStyle: symbol

string

### Discussion

If your application uses the App Tracking Transparency framework, use this key to provide a usage-description string to explain your app’s purpose for accessing data that the app can use to track the person or the device. The system displays the string value in a full-page authorization sheet from which the person can grant or deny permission to access the tracking data.

The format of the string is Markdown text; you can apply bold or italic style, but it doesn’t support underline. You can include bullet lists and paragraph breaks.

This key is optional. The system uses the NSUserTrackingUsageDescription if your app’s target properties omit this key.

This key has regional availability. To use this key, the system requires that the device be located in a specific European Union (EU) country and signed in with an Apple Account that has its country or region set to a specific EU country or region:

France, Germany, Italy, Poland, and Romania: The system uses this key, if available.

The European Union: The system uses this key if available when your app calls requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:), passing preferExpandedInterface a value of true.

Outside of the EU, the system uses the NSUserTrackingUsageDescription key instead of this key.

[Tip]

Tip: Keep the text of your description short and specific. The system displays your app name in the prompt so you don’t need to include it in the string. For example usage descriptions, see Apple’s Human Interface Guidelines.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription
# NSUserTrackingUsageDescription

A message that explains the purpose for accessing data that an app can use to track a person or device.

iOS 14.0, iPadOS 14.0, tvOS 14.0, visionOS 1.0

name: NSUserTrackingUsageDescription

ideTitle: Privacy - Tracking Usage Description

titleStyle: symbol

string

### Discussion

If your application uses the App Tracking Transparency framework, you need to provide a usage-description string to explain the purpose for accessing app-related data that the app can use to track a person or device. The system displays the string in a modal UI from which the person can grant or deny permission to access the tracking data.

This key is required. Your app crashes if it attempts to use the App Tracking Transparency framework without including the key in your target’s properties in Xcode.

The system displays this key’s string in a modal UI when your app requests authorization to access app-related data that the app can use to track the person or the device by calling either method:

- requestTrackingAuthorization(completionHandler:)

- requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)

[Important]

Important: Alternatively, in the European Union, your app can provide a tracking-usage description that supports rich text elements by using markdown format (see NSUserTrackingMarkdownUsageDescription).

Keep the text of your description short and specific. The system displays your app name in the prompt, so you don’t need to include it in the string. For example usage descriptions, see Apple’s Human Interface Guidelines.

## Security

- NSUpdateSecurityPolicy: A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.

- NSAppBundlesUsageDescription: A message that tells people why the app needs to access the contents of other apps’ bundles.

- NSAppDataUsageDescription: A message that tells people why the app needs to access files in other apps’ sandbox containers.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

- NSAppleEventsUsageDescription: A message that tells people why the app is requesting the ability to send Apple events.

- NSSystemAdministrationUsageDescription: A message in macOS that tells people why the app is requesting to manipulate the system configuration.

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSVideoSubscriberAccountUsageDescription
# NSVideoSubscriberAccountUsageDescription

A message that tells people why the app is requesting access to their TV provider account.

tvOS 9.0

name: NSVideoSubscriberAccountUsageDescription

ideTitle: Privacy - Video Subscriber Account Usage Description

titleStyle: symbol

string

### Discussion

[Important]

Important:  This key is required if your app uses APIs that access the user’s TV provider account.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSWidgetWantsLocation
# NSWidgetWantsLocation

A Boolean value that indicates a widget uses the user’s location information.

iOS 14.0, iPadOS 14.0, macOS 11.0

name: NSWidgetWantsLocation

ideTitle: Widget Wants Location

titleStyle: symbol

boolean

### Discussion

To access the user’s location information from a widget, set the value to true in the widget extension’s Info.plist file.

Before a widget can access location information, the containing app must request authorization from the user. The containing app’s Info.plist file must also contain relevant purpose strings. For more information, see Requesting authorization to use location services.

## Location

- Choosing the  Location Services Authorization to Request: Determine the authorization your app needs to access location data.

- NSLocationAlwaysAndWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information at all times.

- NSLocationUsageDescription: A message that tells people why the app is requesting access to their location information.

- NSLocationWhenInUseUsageDescription: A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

- NSLocationTemporaryUsageDescriptionDictionary: A collection of messages that explain why the app is requesting temporary access to their location.

- NSLocationAlwaysUsageDescription: A message that tells people why the app is requesting access to their location at all times.

- NSLocationDefaultAccuracyReduced: A Boolean value that indicates whether the app requests reduced location accuracy by default.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/NSWorldSensingUsageDescription
# NSWorldSensingUsageDescription

A message that tells people why the app is requesting access to image tracking, plane detection, or scene reconstruction.

visionOS 1.0

name: NSWorldSensingUsageDescription

ideTitle: Privacy - World Sensing Usage Description

titleStyle: symbol

string

### Discussion

Use this key to indicate that your app requires access to world-sensing data. This includes plane detection, image tracking, and scene-reconstruction anchors. The first time your app tries to access world-sensing data, the system prompts for permission. Provide a string for the prompt that explains why your app needs access. For more information on setting up ARKit for world sensing, see Setting up access to ARKit data.

[Note]

Note:  World tracking — unlike world sensing — doesn’t require authorization. For more information, see Tracking specific points in world space.

## Vision

- NSHandsTrackingUsageDescription: A message that tells people why the app is requesting access to track their hand position and location.

- NSAccessoryTrackingUsageDescription: A message that tells a person why the app is requesting access to track accessory position and location.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/OSBundleUsageDescription
# OSBundleUsageDescription

A message that tells people why the app is trying to install a driver extension bundle.

iOS 18.4, iPadOS 18.4, Mac Catalyst 18.4, macOS 10.15

name: OSBundleUsageDescription

ideTitle: Privacy - Driver Extension Usage Description

titleStyle: symbol

string

### Discussion

This key is required for all DriverKit extensions. Failure to include this key results in an error at activation time. For system extensions that are not DriverKit extensions, use NSSystemExtensionUsageDescription instead.

## System Extensions

- NSSystemExtensionUsageDescription: A message that tells people why the app is trying to install a system extension bundle.

=== SOURCE: https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings/
### App Review Help

App Review / Guideline reference / 5.1.1(ii) - Write clear purpose strings 
Filter ⌘K  
Filter ⌘K  

Guideline reference  

# 5.1.1(ii) - Write clear purpose strings

Apple operating systems restrict access to protected data and resources by default, so before your app can access resources like the camera, location, microphone, or health data, it has to request permission. These requests often include a purpose string, also called a usage description, that explains how your app will use the requested data or resource.

App Review Guideline 5.1.1(ii) specifies requirements for purpose strings:

5.1.1(ii) Permission

[...] Ensure your purpose strings clearly and completely describe your use of the data. [...]

This requirement allows users to make an informed decision about whether or not to grant your app access.

## Best practices for purpose strings

A purpose string that only restates the name of the resource, or promises a general benefit without saying what your app actually does, doesn't meet the requirement.

###  Explain specifically how your app will use the data.

#### Do

-  
Name the specific feature or outcome the data makes possible.

-  
Write a separate purpose string for every protected resource your app requests.

#### Don't

-  
Don't obscure who has access to data behind a vague benefit or a passive construction, such as, "Your data will be used to provide a better experience."

-  
Don't restate the name of the resource without explaining its use.

###  Provide an example of how the data will be used.

#### Do

-  
Give a concrete example of what your app does with the data.

-  
Write one brief, complete sentence in active voice and sentence case, ending with a period.

#### Don't

-  
Don't fill the request with marketing copy or a full feature list.

Insufficient examples

Clear and specific examples

"To use location."

"The app uses location data to determine the recommended route to your destination and provide turn-by-turn directions."

"Your data will be used to provide a better experience."

"The app uses tracking data to deliver personalized advertising for products that are most relevant to you."

## FAQs

### Do purpose strings need to be localized?

Yes. If your app supports localizations for a global audience, you must provide localized purpose strings. Set your app to each localization and test to confirm the correct localized text appears in the permission request. Learn more about app localization.

### A third-party SDK in my app requests permissions. Am I responsible for its purpose strings?

Yes. As stated in the App Review Guidelines and the Apple Developer Program License Agreement, you're responsible for everything in your app, including SDKs, libraries, and other code from third parties. SDKs can reference APIs that access protected resources such as location, sometimes without your realizing it. If your app has a valid reason to access a resource, define a purpose string on the Info.plist that describes your app's specific use case. If it doesn't, remove references to those APIs from your app's binary. Familiarize yourself with the resources an SDK may try to access before you submit.

Related App Review Guideline 5.1.1 Requesting access to protected resources Human Interface Guidelines: Privacy Provide information for a complete review

=== SOURCE: https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple
Sign in with Apple | Apple Developer Documentation                         

# This page requires JavaScript.

Please turn on JavaScript in your browser and refresh the page to view its content.

## Automated tools and assistive tools:

A Markdown version of the page content is available: View Markdown

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/Information-Property-List/UIRequiresPersistentWiFi
# UIRequiresPersistentWiFi

A Boolean value that indicates whether the app requires a Wi-Fi connection.

iOS 2.0, iPadOS 2.0, visionOS 1.0

name: UIRequiresPersistentWiFi

ideTitle: Application uses Wi-Fi

titleStyle: symbol

boolean

### Discussion

If YES, iOS opens a Wi-Fi connection when the app launches and keeps it open while the app is running. If NO, iOS closes the active Wi-Fi connection after 30 minutes. If the app tries to connect to the network when there’s no open Wi-Fi connection, the system may use the cellular network instead.

=== SOURCE: https://developer.apple.comdoc://com.apple.signinwithapple/documentation/SigninwithAppleRESTAPI/Revoke-tokens (HTTP Body parameters)
- client_id (Required): The identifier (App ID or Services ID) for your app. The identifier must match the value provided during the authorization request for the user’s information. Additionally, the identifier must not include your Team ID, to help mitigate the possibility of exposing sensitive data to the end user.
- client_secret (Required): A secret JSON Web Token (JWT) that uses the Sign in with Apple private key associated with your developer account. For more information about creating client secrets, see  Creating a client secret.
- token (Required): The user refresh token or access token intended to be revoked. The user session associated with the token provided is revoked if the request is successful.
- token_type_hint (Optional): A hint about the type of the token submitted for revocation. Use refresh_token or access_token.

