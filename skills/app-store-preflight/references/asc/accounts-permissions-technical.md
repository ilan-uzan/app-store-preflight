# Accounts, Permissions & Technical Bundle Requirements
Source: https://developer.apple.com/support/offering-account-deletion-in-your-app/ (redirects to https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion), https://developer.apple.com/design/human-interface-guidelines/managing-accounts, https://developer.apple.com/sign-in-with-apple/ (redirects to https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple), https://developer.apple.com/documentation/signinwithapplerestapi/revoke-tokens, https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts, https://developer.apple.com/documentation/bundleresources/protected-resources (and every child Info.plist key page), https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources, https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings, https://developer.apple.com/design/human-interface-guidelines/privacy, https://developer.apple.com/documentation/bundleresources/choosing-the-location-services-authorization-to-request, https://developer.apple.com/documentation/security/preventing-insecure-network-connections, https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity, https://developer.apple.com/documentation/xcode/configuring-background-execution-modes, https://developer.apple.com/design/human-interface-guidelines/app-icons, https://developer.apple.com/documentation/xcode/configuring-your-app-icon, https://developer.apple.com/design/human-interface-guidelines/launching, https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen (full list in "## Sources")  
Retrieved: 2026-10-30

Notes for the skill: All text below was copied from Apple's pages as fetched on the retrieval date (DocC pages via the `tutorials/data/*.json` endpoint; help pages via HTML). Inline links were flattened to their visible link text and code-voice backticks were kept where they help readability. Images on Apple's pages are not reproduced. Checks quote only the text shown in the unit's source section. Text in square brackets beginning "[Editor:" is not Apple's wording. Apple's sub-headings, definition-list terms and Info.plist key names are rendered as bold labels, "Term: definition" pairs, or "Key — abstract" lines; tables reproduce Apple's tables cell-for-cell, and PERM.A's key table is assembled from each key page's own text.

---

## ACCT.A 5.1.1(v) Offering account deletion in your app

**Source text (verbatim):**
> Apps submitted to the App Store that support account creation must also let people initiate deletion of their account within the app.
>
> Deleting an account removes the account from the developer's records, along with any data associated with the account that the developer isn't legally required to maintain. Providing this capability gives people more control of the personal data they've shared. If you're updating an app or submitting a new app with account creation, read the guidance below for a smoother submission process.
>
> **Account deletion guidance**
>
> Deleting an account is a major decision, so the process to initiate and confirm it must be straightforward and transparent:
> - Make the account deletion option easy to find in your app. Typically, it's included in the app's account settings.
> - Offer to delete the entire account record, along with associated personal data. You may include additional options, but only offering to temporarily deactivate or disable an account is insufficient.
> - If people need to visit a website to finish deleting their account, include a link directly to the page on your website where they can complete the process. On tvOS, you can present a static URL or QR code that links directly to the account deletion page.
> - Keep people informed. If the deletion request will take additional time to complete, let them know. If your app supports in-app purchases, help people understand how billing and cancellations will be handled. If you're legally required to retain some user information, let people know what information will and won't be retained. For additional guidance, read the Human Interface Guidelines.
>
> Note: Follow applicable legal requirements for storing and retaining user account information and for handling account deletion. This includes complying with local laws where your app is available. If you have questions regarding your legal obligations, check with your legal counsel.
>
> **FAQs**
>
> **Can I direct people to a customer service flow to complete account deletion?**
> It depends. Apps in highly regulated industries, as described in App Review Guideline 5.1.1(ix), may use additional customer service flows to confirm and facilitate the account deletion process. Apps not operating in highly regulated industries should not require people to make a phone call, send an email, use a chat support flow, or go through other support flows.
>
> **Can I require reauthentication or add confirmation steps to ensure the account isn't deleted by accident or by someone other than the account holder?**
> Yes. It's appropriate to confirm the user genuinely intends to delete their account. You may add steps to verify the identity of the person making the request, and to confirm that they want to delete the account, such as by entering a code from an email or phone number already associated with the account. However, apps that make it unnecessarily difficult for someone to delete their account will not pass review.
>
> **My app uses Sign in with Apple to provide account creation and authentication. What changes are necessary to support people who delete their accounts?**
> Apps that support Sign in with Apple should use the Sign in with Apple REST API to revoke user tokens. Use server-to-server notification endpoints to process changes for Sign in with Apple accounts. Note that developers based in the Republic of Korea must provide a server‑to‑server notification endpoint when registering a new Services ID.
>
> **If my app links out to the default web browser for account creation, does it still need to offer account deletion within the app?**
> Yes. Additionally, linking out to the default web browser to sign in or register an account provides a poor user experience and isn't appropriate, per App Review Guideline 4.
>
> **My app automatically creates an account for the user. Do I need to include an option to initiate account deletion?**
> Yes. People should have the option to delete automatically generated accounts (sometimes called "guest" accounts) and the data associated with those accounts. Ensure any automatic account creation in your app complies with local laws where your app is available.
>
> **I manually delete accounts and this takes time. Does account deletion need to be immediate and automatic?**
> No. If your process for account deletion is manual or otherwise takes a reasonable amount of time to complete, this is acceptable. Inform the person how long it will take to delete the account and provide a confirmation when the deletion is complete. Ensure the time it takes to delete accounts complies with local laws where your app is available.
>
> **Does the content provided by a person need to be deleted in apps that display and share user-generated content?**
> Yes. People expect that all data associated with their account will be deleted when the account is deleted. This includes user-generated content that's shared with others, such as photos, videos, text posts, and reviews. If local laws or regulations require you to maintain some data, let people know.
>
> **I allow account deletion in compliance with CCPA, GDPR, or other local laws in some of the locations where my app is available. Is this sufficient?**
> No. Everyone should be able to delete their accounts, regardless of where they're located. Existing account deletion flows you've created to comply with local legal requirements can be made available to everyone, as long as they meet the requirements of App Review Guideline 5.1.1(v).
>
> **How do I handle people with auto-renewable subscriptions? I don't want to accidentally charge someone after they've deleted their account.**
> If a person has an auto-renewable subscription, notify them that billing will continue through Apple and ask them to cancel their subscription before continuing. If you use App Store Server Notifications for auto-renewable subscriptions, you can verify the status of the person's subscription in real time, or use the Subscription Status API to identify subscription status.
>
> Use showManageSubscriptions in iOS 15 and iPadOS 15, or later, or provide this link to let people manage their subscriptions: https://apps.apple.com/account/subscriptions/. For tvOS, provide onscreen instructions to change or cancel a subscription, as described in the Apple TV User Guide.
>
> You can also use beginRefundRequest in iOS 15 and iPadOS 15, or later, or provide this Apple Support link to let customers submit refund requests: https://support.apple.com/118223.
>
> Additionally, you can offer to schedule account deletion for a later date, aligned with the subscription's expiration, as long as there's also an option to delete the account immediately.

**Applies to:** Apps that "support account creation" (including apps that automatically create "guest" accounts and apps that link out to a browser for account creation).

- **[TECH-01]** If the app supports account creation, can a person initiate deletion of their account from inside the app?
  - quote: "Apps submitted to the App Store that support account creation must also let people initiate deletion of their account within the app."
  - surface: code
  - verify: Grep the project for account-creation flows (`signUp`, `register`, `createUser`, `createAccount`, Firebase `createUser(withEmail:`, Supabase `auth.signUp`, `ASAuthorizationAppleIDProvider`, Auth0/Cognito sign-up calls). If any exist, grep for a deletion entry point (`deleteAccount`, `deleteUser`, `user.delete(`, "Delete Account" strings in `.strings`/`.xcstrings`/SwiftUI `Text`). FAIL if creation exists and no in-app deletion entry point exists.
  - fix: Add a "Delete Account" action that calls the backend's account-deletion endpoint (or links directly to the web deletion page), plus a confirmation step.
- **[TECH-02]** Is the account-deletion option easy to find (for example, in the app's account settings)?
  - quote: "Make the account deletion option easy to find in your app. Typically, it's included in the app's account settings."
  - surface: runtime
  - verify: Launch the app, sign in with a test account, open Settings/Account/Profile. Record how many taps reach the deletion control. FAIL if it is only reachable via help articles, support chat, or is absent from the account/settings area.
  - fix: Place the deletion control in the account/settings screen.
- **[TECH-03]** Does the deletion flow delete the entire account record and associated personal data, rather than only deactivating/disabling the account?
  - quote: "only offering to temporarily deactivate or disable an account is insufficient."
  - surface: code
  - verify: Trace the deletion action to its backend call. FAIL if it only sets a flag such as `isActive=false`, `disabled`, `deactivated`, or signs out, with no deletion of the account record and personal data. If the backend is not in the repo, mark as manual and ask the developer.
  - fix: Implement real deletion of the account record and associated personal data on the server (deactivation may remain as an additional option).
- **[TECH-04]** If deletion must be finished on a website, does the app link directly to the exact deletion page (on tvOS: static URL or QR code to that page)?
  - quote: "If people need to visit a website to finish deleting their account, include a link directly to the page on your website where they can complete the process."
  - surface: code
  - verify: Find the URL opened by the deletion control (`openURL`, `Link(`, `SFSafariViewController`, `UIApplication.shared.open`). FAIL if it points to a home page, generic help center, or privacy policy rather than the deletion page.
  - fix: Link to the URL of the page where deletion is completed.
- **[TECH-05]** If deletion takes additional time, does the app tell the person (and, for manual processes, how long it will take and confirm when complete)?
  - quote: "Inform the person how long it will take to delete the account and provide a confirmation when the deletion is complete."
  - surface: runtime
  - verify: Run the deletion flow with a test account. Check the confirmation UI copy for a timeframe when deletion is not immediate, and check that a completion confirmation (e.g., email/push/in-app) is sent by the backend.
  - fix: Add copy stating the expected completion time and send a completion confirmation.
- **[TECH-06]** If the app supports in-app purchases, does the deletion flow explain how billing and cancellations will be handled?
  - quote: "If your app supports in-app purchases, help people understand how billing and cancellations will be handled."
  - surface: code
  - verify: If StoreKit is used (`import StoreKit`, `Product.purchase`, `SKPaymentQueue`, RevenueCat), inspect the deletion screen strings for billing/cancellation text.
  - fix: Add billing/cancellation explanation to the deletion screen.
- **[TECH-07]** If some user information must legally be retained, does the flow tell people what will and won't be retained?
  - quote: "If you're legally required to retain some user information, let people know what information will and won't be retained."
  - surface: manual
  - verify: Ask the developer whether any data is retained for legal reasons; if yes, check the deletion screen copy lists it.
  - fix: manual — requires developer decision/legal/business action (then add the disclosure copy).
- **[TECH-08]** For apps not in highly regulated industries, does deletion avoid requiring a phone call, email, chat support, or other support flow?
  - quote: "Apps not operating in highly regulated industries should not require people to make a phone call, send an email, use a chat support flow, or go through other support flows."
  - surface: code
  - verify: Inspect the deletion action: FAIL if it opens `mailto:`, `tel:`, an Intercom/Zendesk/Helpshift chat, or a "contact support to delete" message, and the app is not in a highly regulated industry (manual attestation for industry).
  - fix: Replace the support flow with a self-service in-app (or direct web) deletion flow.
- **[TECH-09]** Are confirmation/re-authentication steps limited so deletion is not unnecessarily difficult?
  - quote: "However, apps that make it unnecessarily difficult for someone to delete their account will not pass review."
  - surface: runtime
  - verify: Run the flow; count screens/steps; note retention dark patterns (multiple "are you sure" loops, forced surveys, hidden buttons). Identity verification such as a code sent to the account's email/phone is allowed.
  - fix: Reduce the flow to an identity check (optional) plus one clear confirmation.
- **[TECH-10]** If the app supports Sign in with Apple, does account deletion revoke the user's tokens via the Sign in with Apple REST API?
  - quote: "Apps that support Sign in with Apple should use the Sign in with Apple REST API to revoke user tokens."
  - surface: code
  - verify: If `ASAuthorizationAppleIDProvider`/`SignInWithAppleButton` is used, grep the backend/app for `appleid.apple.com/auth/revoke`. FAIL if absent from the deletion path. (Supabase/Firebase: check their documented revoke hook is configured.)
  - fix: On deletion, POST to `https://appleid.apple.com/auth/revoke` with `client_id`, `client_secret`, `token`, `token_type_hint` (see ACCT.E).
- **[TECH-11]** If the app supports Sign in with Apple, is a server-to-server notification endpoint used to process account changes (mandatory for Republic of Korea developers registering a new Services ID)?
  - quote: "Use server-to-server notification endpoints to process changes for Sign in with Apple accounts."
  - surface: manual
  - verify: Ask the developer (or check the Apple Developer account → Certificates, Identifiers & Profiles → the App ID's Sign in with Apple configuration) whether a server-to-server notification endpoint URL is set; grep backend for handling of `consent-revoked` / `account-deleted` events.
  - fix: Configure the notification endpoint and handle the events (see ACCT.F).
- **[TECH-12]** If account creation happens by linking out to the default web browser, does the app still offer in-app account deletion (and avoid linking out to the browser to sign in/register)?
  - quote: "linking out to the default web browser to sign in or register an account provides a poor user experience and isn't appropriate, per App Review Guideline 4."
  - surface: code
  - verify: Grep for sign-up/sign-in buttons that call `UIApplication.shared.open`/`openURL` with a registration/login URL. FAIL if found; also apply TECH-01.
  - fix: Move sign-in/registration into the app (e.g., `ASWebAuthenticationSession` or native forms) and add in-app deletion.
- **[TECH-13]** If the app automatically creates accounts ("guest" accounts), can people delete those accounts and their data?
  - quote: "People should have the option to delete automatically generated accounts"
  - surface: code
  - verify: Grep for anonymous/guest account creation (`signInAnonymously`, `anonymous`, `guest`, device-ID-based server accounts). If present, confirm a deletion path exists for those accounts.
  - fix: Expose the delete-account action for guest accounts too.
- **[TECH-14]** If the app displays/shares user-generated content, does deletion also delete the person's UGC (photos, videos, text posts, reviews), or disclose what must legally be kept?
  - quote: "This includes user-generated content that's shared with others, such as photos, videos, text posts, and reviews."
  - surface: code
  - verify: Inspect the backend deletion routine (if in repo) for removal of posts/media/comments owned by the user. Otherwise ask the developer.
  - fix: Extend the deletion routine to remove UGC; disclose any legally retained data.
- **[TECH-15]** Is account deletion available to everyone regardless of location (not gated to GDPR/CCPA regions)?
  - quote: "Everyone should be able to delete their accounts, regardless of where they're located."
  - surface: code
  - verify: Grep the deletion UI for conditionals on region/locale/storefront (`Locale.current.region`, `Storefront.current`, `countryCode`, remote-config flags). FAIL if deletion is hidden for some regions.
  - fix: Remove the region gate.
- **[TECH-16]** If a person has an auto-renewable subscription, does the deletion flow notify them that billing continues through Apple and ask them to cancel before continuing?
  - quote: "If a person has an auto-renewable subscription, notify them that billing will continue through Apple and ask them to cancel their subscription before continuing."
  - surface: code
  - verify: If the app sells auto-renewable subscriptions, check the deletion screen for this notice and a manage-subscriptions entry point (`showManageSubscriptions(in:)`, `.manageSubscriptionsSheet`, or the link `https://apps.apple.com/account/subscriptions/`; tvOS: onscreen instructions).
  - fix: Add the notice and a button calling `AppStore.showManageSubscriptions(in:)` (iOS 15+) or opening `https://apps.apple.com/account/subscriptions/`.
- **[TECH-17]** If the app offers to schedule deletion for a later date, does it also offer immediate deletion?
  - quote: "you can offer to schedule account deletion for a later date, aligned with the subscription's expiration, as long as there's also an option to delete the account immediately."
  - surface: runtime
  - verify: If scheduled deletion exists, confirm an "delete now" option exists in the same flow.
  - fix: Add an immediate-deletion option.

## ACCT.B HIG Managing accounts — Introduction and best practices

**Source text (verbatim):**
> When it doesn’t create an unnecessary barrier to your experience, an account can be a convenient way for people to access their content and track personal details.
>
> Ask people to create an account only if your core functionality requires it; otherwise, let people enjoy your app or game without one. If you require an account, consider using Sign in with Apple to give people a consistent sign-in experience they can trust and the convenience of not having to remember multiple accounts and authentication methods.
>
> **Best practices**
>
> Explain the benefits of creating an account and how to sign up. If your app or game requires an account, write a brief, friendly description of the reasons for the requirement and its benefits. Display this message in your sign-in view.
>
> Delay sign-in for as long as possible. People often abandon apps when they’re forced to sign in before they can do anything useful. To help avoid this situation, give people a chance to get a sense of what your app or game does before asking them to make a commitment to it. For example, a shopping app might let people browse as much as they want, requiring sign-in only when they’re ready to make a purchase.
>
> If you don’t use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey. Passkeys simplify account creation and authentication, eliminating the need for people to create or enter passwords. When an app supports passkeys, people simply provide their user name when creating a new account or signing in to an existing one. For developer guidance, see Supporting passkeys. If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see Securing Logins with iCloud Keychain Verification Codes).
>
> Always identify the authentication method you offer. For example, if you display a button for signing in to your app with Face ID, title it using a phrase like “Sign In with Face ID” instead of a generic phrase like “Sign In.”
>
> Refer only to authentication methods that are available in the current context. For example, don’t reference Face ID on a device that doesn’t offer it. Check the device’s capabilities and use the appropriate terminology. For developer guidance, see LABiometryType.
>
> In general, avoid offering an app-specific setting for opting in to biometric authentication. People turn on biometric authentication at the system level, so presenting an in-app setting is redundant and could be confusing.
>
> Avoid using the term passcode to refer to account authentication. People create a passcode to unlock their device or authenticate for Apple services. If you use the term in your interface, people might think you’re asking them to reuse their passcode in your app or game.

**Applies to:** Apps that offer accounts or sign-in (HIG guidance).

- **[TECH-18]** Is an account required only if core functionality requires it, with sign-in delayed until needed?
  - quote: "Ask people to create an account only if your core functionality requires it; otherwise, let people enjoy your app or game without one."
  - surface: runtime
  - verify: Fresh-install launch: note whether a sign-in wall appears before any content. If so, ask the developer to justify why core functionality requires an account. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Allow browsing/using non-account features before sign-in; prompt for sign-in at the feature that needs it.
- **[TECH-19]** If an account is required, does the sign-in view display a brief description of why it is required and its benefits?
  - quote: "If your app or game requires an account, write a brief, friendly description of the reasons for the requirement and its benefits. Display this message in your sign-in view."
  - surface: code
  - verify: Inspect the sign-in view (SwiftUI/UIKit) for explanatory copy. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Add a short benefit/reason message to the sign-in view.
- **[TECH-20]** Do biometric sign-in buttons name the method (e.g., “Sign In with Face ID”) and reference only methods available on the device (checked via `LABiometryType`)?
  - quote: "Refer only to authentication methods that are available in the current context."
  - surface: code
  - verify: Grep for "Face ID"/"Touch ID"/"Optic ID" strings. Confirm the UI chooses the label from `LAContext().biometryType` (`.faceID`, `.touchID`, `.opticID`) rather than hard-coding one. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Derive the label from `LAContext.biometryType` and title the button with the specific method.
- **[TECH-21]** Does the app avoid using the term “passcode” for account authentication?
  - quote: "Avoid using the term passcode to refer to account authentication."
  - surface: code
  - verify: Grep localized strings (`*.strings`, `*.xcstrings`, Swift string literals) for "passcode" (case-insensitive) used for app account credentials. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Rename to "password", "PIN" or "code" as appropriate.
- **[TECH-22]** Does the app avoid an app-specific opt-in setting for biometric authentication?
  - quote: "In general, avoid offering an app-specific setting for opting in to biometric authentication."
  - surface: code
  - verify: Grep settings screens for toggles like "Enable Face ID"/"Use Touch ID". Advisory ("In general") — report as WARN, not FAIL.
  - fix: manual — requires developer decision (remove the toggle or keep with justification).

## ACCT.C HIG Managing accounts — Deleting accounts

**Source text (verbatim):**
> If you help people create an account within your app or game, you must also help them delete it, not just deactivate it. In addition to following the guidelines below, be sure to understand and comply with your region’s legal requirements related to account deletion and the right to be forgotten.
>
> Important: If legal requirements compel your app to maintain accounts or information — such as digital health records — or to follow a specific account-deletion process, clearly describe the situation so people can understand the information or accounts you must maintain and the process you must follow.
>
> Provide a clear way to initiate account deletion within your app or game. If people can’t perform account deletion within your app, you must provide a direct link to the webpage on which people can do so. Make the link easy to discover — for example, don’t bury it in your Privacy Policy or Terms of Service pages.
>
> Developer note: If people used Sign in with Apple to create an account within your app, you revoke the associated tokens when they delete their account. See Token revocation.
>
> Provide a consistent account-deletion experience whether people perform it within your app or game or on the website. For example, avoid making one version of the deletion flow longer or more complicated than the other.
>
> Consider letting people schedule account deletion to occur in the future. People can appreciate the opportunity to use their remaining services or wait until their subscription auto-renews before deleting their account. If you offer a way to schedule account deletion, offer an option for immediate deletion as well.
>
> Tell people when account deletion will complete, and notify them when it’s finished. Because it can sometimes take a while to fully delete an account, it’s essential to keep people informed about the status of the deletion process so they know what to expect.
>
> If you support in-app purchases, help people understand how billing and cancellation work when they delete their account. For example, you might need to help people understand the following scenarios:
> - Billing for an auto-renewable subscription continues through Apple until people cancel the subscription, regardless of whether they delete their account.
> - After they delete their account, people need to cancel their subscription or request a refund.
>
> In addition to helping people understand these scenarios, provide information that describes how to cancel subscriptions and manage purchases. For guidance, see Helping people manage their subscriptions and Providing help.
>
> Note: Even if people didn’t use your app to purchase the subscription, you still need to support account deletion.

**Applies to:** Apps that let people create an account within the app.

- **[TECH-23]** Is the web account-deletion link (when deletion can't happen in-app) easy to discover and not buried in the Privacy Policy or Terms of Service?
  - quote: "Make the link easy to discover — for example, don’t bury it in your Privacy Policy or Terms of Service pages."
  - surface: runtime
  - verify: Locate the deletion link in the running app; FAIL if it only appears inside a privacy-policy/ToS web page.
  - fix: Surface a dedicated "Delete Account" control in account settings.
- **[TECH-24]** Is the in-app deletion flow consistent with the website flow (neither longer nor more complicated than the other)?
  - quote: "avoid making one version of the deletion flow longer or more complicated than the other."
  - surface: manual
  - verify: Compare the step count of the in-app flow with the website flow (if a website flow exists). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Align both flows to the same steps.
- **[TECH-25]** Does the deletion flow provide information describing how to cancel subscriptions and manage purchases (also when the subscription wasn't bought in the app)?
  - quote: "provide information that describes how to cancel subscriptions and manage purchases."
  - surface: code
  - verify: Inspect deletion screen copy/actions for subscription-management info (see TECH-16).
  - fix: Add the info and a manage-subscriptions action.

## ACCT.D HIG Managing accounts — TV provider accounts and platform considerations

**Source text (verbatim):**
> **TV provider accounts**
>
> Many popular TV providers let people sign in to their accounts at the system level, eliminating the need to authenticate on an app-by-app basis. If your TV provider app requires people to sign in, use TV Provider Authentication to provide the most efficient onboarding experience.
>
> Avoid displaying a sign-out option when people are signed in at the system level. If your app must include a sign-out option, invoking it needs to prompt people to navigate to Settings > TV Provider to sign out of their account.
>
> Never instruct people to sign out by adjusting privacy controls. The TV provider controls in Settings > Privacy aren’t a sign-out mechanism. These settings help people manage the apps that can access their TV provider account.
>
> **Platform considerations**
>
> No additional considerations for iOS, iPadOS, macOS, or visionOS.
>
> **tvOS**
>
> Most people interact with Apple TV using a remote, not a keyboard, so ask for the minimum amount of information necessary.
>
> Prefer letting people use another device to sign up or authenticate. When you configure your app’s associated domains, Apple TV can work with other devices to safely suggest sign-in credentials, including Sign in with Apple. For developer guidance, see Configuring an associated domain.
>
> When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user. In tvOS 16 and later, your app can share its credentials with all users while storing each individual’s profile and user data separately. When you support this type of sharing, your app can automatically use the current user’s profile without asking each person to sign in separately to a shared account. For developer guidance, see kSecUseUserIndependentKeychain and User Management Entitlement.
>
> Minimize data entry. If you need to gather more than a small amount of information, ask people to visit a website from another device. If you need an email address, show the email keyboard screen, which includes a list of recently entered addresses.
>
> **watchOS**
>
> Use iCloud synchronization to provide access to the Keychain, letting people autofill user names and passwords and preserve app settings.

**Applies to:** TV provider apps (first part); tvOS and watchOS apps with accounts (platform part).

- **[TECH-26]** In a TV provider app, if a sign-out option exists, does it prompt people to go to Settings > TV Provider, and does the app never instruct sign-out via privacy controls?
  - quote: "Never instruct people to sign out by adjusting privacy controls."
  - surface: code
  - verify: If the app uses `VideoSubscriberAccount` (`VSAccountManager`), grep sign-out copy for "Settings > Privacy" instructions (FAIL) and confirm sign-out directs to Settings > TV Provider.
  - fix: Change sign-out copy to direct people to Settings > TV Provider.
- **[TECH-115]** In a TV provider app that requires sign-in, does the app use TV Provider Authentication, and avoid showing a sign-out option when people are signed in at the system level?
  - quote: "If your TV provider app requires people to sign in, use TV Provider Authentication to provide the most efficient onboarding experience."
  - surface: code
  - verify: If the app is a TV provider app, grep for `VideoSubscriberAccount` / `VSAccountManager`; check whether a sign-out control is shown while the system-level TV provider sign-in is active. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Adopt TV Provider Authentication; hide the in-app sign-out while signed in at the system level (or make it direct people to Settings > TV Provider).
- **[TECH-116]** On tvOS, does account sign-up/sign-in ask for the minimum information, sending people to a website on another device when more than a small amount is needed?
  - quote: "Minimize data entry. If you need to gather more than a small amount of information, ask people to visit a website from another device."
  - surface: runtime
  - verify: Run the tvOS target's sign-up/sign-in flow; count text fields typed with the remote. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Move lengthy forms to a website or another-device flow; keep on-TV entry minimal.

## ACCT.E Sign in with Apple REST API — Token revocation

**Source text (verbatim):**
> Invalidate the tokens and associated user authorizations for a user when they are no longer associated with your app.
>
> [Editor: URL —] POST https://appleid.apple.com/auth/revoke
>
> [Editor: HTTP Body, form-data, application/x-www-form-urlencoded —] The list of input parameters required for the server to invalidate the token.
>
> | Parameter | Required | Description |
> |---|---|---|
> | client_id | Required | The identifier (App ID or Services ID) for your app. The identifier must match the value provided during the authorization request for the user’s information. Additionally, the identifier must not include your Team ID, to help mitigate the possibility of exposing sensitive data to the end user. |
> | client_secret | Required | A secret JSON Web Token (JWT) that uses the Sign in with Apple private key associated with your developer account. For more information about creating client secrets, see Creating a client secret. |
> | token | Required | The user refresh token or access token intended to be revoked. The user session associated with the token provided is revoked if the request is successful. |
> | token_type_hint | Optional | A hint about the type of the token submitted for revocation. Use refresh_token or access_token. |
>
> | Status | Reason | Description |
> |---|---|---|
> | 200 | OK | The request was successful; the provided token has been revoked successfully or was previously invalid. |
> | 400 | Bad Request | The server was unable to process the request. See the error code description for more information about the underlying error. |
>
> In order to revoke authorization for a user, you must obtain a valid refresh token or access token. If you don’t have either token for the user, you can generate tokens when validating an authorization code. For more information about user tokens and creating client secrets, see Token validation.
>
> To invalidate a user’s refresh token, invoke the revoke endpoint with the following HTTP POST method.
> ```
> curl -v POST "https://appleid.apple.com/auth/revoke" \
> -H 'content-type: application/x-www-form-urlencoded' \
> -d 'client_id=CLIENT_ID' \
> -d 'client_secret=CLIENT_SECRET' \
> -d 'token=REFRESH_TOKEN' \
> -d 'token_type_hint=refresh_token'
> ```
> For either token revocation request, the revoke endpoint returns a 200 response code without a response body after the server invalidates the token value, or if the token value was previously invalidated. If the response contains an error, please see ErrorResponse for the specific error code provided in the response body.

**Applies to:** Apps using Sign in with Apple that delete accounts.

- **[TECH-27]** Does the revocation call send `client_id`, `client_secret` (JWT signed with the Sign in with Apple private key) and a valid refresh or access `token`, with `client_id` not including the Team ID?
  - quote: "In order to revoke authorization for a user, you must obtain a valid refresh token or access token."
  - surface: code
  - verify: In the backend code that calls `auth/revoke`, check the form parameters; check that a refresh/access token is stored or obtained (by validating the authorization code) for each Sign in with Apple user.
  - fix: Obtain a refresh or access token for each Sign in with Apple user (the source says you can generate tokens when validating an authorization code; see Token validation), store it server-side, and call `auth/revoke` with it on deletion.

## ACCT.F Processing changes for Sign in with Apple accounts

**Source text (verbatim):**
> Manage user-initiated modifications to maintain privacy with server-to-server notifications.
>
> Sign in with Apple users can modify their accounts, including deleting or disabling their Apple Accounts. If your app or website hosts such an account, Apple can alert you when these changes occur by delivering developer notifications to your server. To learn how your users manage their account preferences for your app, see Manage the apps that you use with Sign in with Apple.
>
> **Set up your server**
>
> To receive server notifications for Sign in with Apple, your server must support the Transport Layer Security (TLS) 1.2 protocol or later. When determining the endpoint URL on your server to receive notifications, you may use the same URL for multiple developer teams and apps. To configure your Sign in with Apple service to receive notifications, see Enabling server-to-server notifications.
>
> **Decode and validate the notifications**
>
> These notifications contain a cryptographically signed payload, in JSON Web Signature (JWS) format, signed by Apple’s private key. After your server receives a notification, examine the JWS payload and use the algorithm specified in the header’s alg parameter to validate the signature. For more information, see Fetch Apple’s public key to verify token signatures.
>
> After validating the token signature, your server performs work according to the type value in the events claim of the token. The notification payload object contains information about user-initiated account modification events. The event types include the following:
>
> | Event type | Meaning |
> |---|---|
> | email-disabled | The user disables email forwarding to their personal email address using Hide My Email. |
> | email-enabled | The user enables email forwarding to their personal email address using Hide My Email. |
> | consent-revoked | The user revokes consent for your app to use their Apple Account and their credentials become invalid. |
> | account-deleted | The user requests that Apple permanently delete their Apple Account. |
>
> **Process disabling and deleting a user’s Apple Account**
>
> Users can disable their Apple Account for a specific primary app ID, or delete their Apple Account account entirely. When a user disables their Apple Account for an app or app group, Apple sends a JWT to your registered endpoint URL with the type value of consent-revoked in the events claim.
>
> When a user requests for Apple to permanently delete their Apple Account, Apple sends a JWT to your registered endpoint URL with the type value of account-deleted in the events claim.
>
> Important: When a user permanently deletes their Apple Account, Sign in with Apple invalidates all user tokens and disables email forwarding for all associated apps. For native apps, the system doesn’t send a credentialRevokedNotification. Use getCredentialState(forUserID:completion:) to respond to account deletion events.
>
> To indicate when the user disables or permanently deletes their Apple Account, be sure to update your server’s records according to your process.

**Applies to:** Apps and websites using Sign in with Apple.

- **[TECH-28]** Does the native app call `getCredentialState(forUserID:completion:)` to respond to account deletion / revocation?
  - quote: "Use getCredentialState(forUserID:completion:) to respond to account deletion events."
  - surface: code
  - verify: Grep Swift/ObjC for `getCredentialState(forUserID:` (or `credentialState(forUserID:)`) on `ASAuthorizationAppleIDProvider`, typically at launch/foreground, and handle `.revoked`/`.notFound` by signing out.
  - fix: Add a credential-state check on launch and when returning to foreground.
- **[TECH-29]** If a server-to-server notification endpoint is configured, does it validate the JWS signature and handle `consent-revoked` and `account-deleted` by updating server records?
  - quote: "To indicate when the user disables or permanently deletes their Apple Account, be sure to update your server’s records according to your process."
  - surface: code
  - verify: Grep backend for the endpoint handling `consent-revoked`, `account-deleted`, `email-disabled`, `email-enabled` and for JWS verification against Apple's public keys.
  - fix: Implement the handler; verify the signature; update/delete user records.
- **[TECH-117]** Does the server endpoint that receives Sign in with Apple notifications support TLS 1.2 or later?
  - quote: "To receive server notifications for Sign in with Apple, your server must support the Transport Layer Security (TLS) 1.2 protocol or later."
  - surface: manual
  - verify: If a notification endpoint is configured, check its host with `nscurl --ats-diagnostics https://<host>` or `openssl s_client -tls1_2 -connect <host>:443`; FAIL if TLS 1.2+ is not supported.
  - fix: Enable TLS 1.2 or later on the endpoint's server.

## SIWA.A Sign in with Apple HIG — Introduction

**Source text (verbatim):**
> Sign in with Apple provides a fast, private way to sign into apps and websites, giving people a consistent experience they can trust and the convenience of not having to remember multiple accounts and passwords.
>
> Supporting Sign in with Apple lets people use the Apple Account they already have to sign in or sign up, and skip filling out forms, verifying email addresses, and choosing passwords. In cases where you choose to ask for a name and email address, people have the option to share a unique, random email address that automatically relays messages to their personal email address. For developer guidance, see Authentication Services.
>
> You can offer Sign in with Apple in every version of your app or website across all platforms — including non-Apple platforms.
>
> Sign in with Apple makes it easy for people to authenticate with Face ID, Touch ID, or Optic ID and has two-factor authentication built in for an added layer of security. Apple doesn’t use Sign in with Apple to profile people or their activity in apps.

**Applies to:** Apps offering Sign in with Apple.

**Status:** Informational — no checks.

## SIWA.B Sign in with Apple HIG — Offering Sign in with Apple

**Source text (verbatim):**
> Follow these guidelines to offer Sign in with Apple when it’s most convenient for people.
>
> Ask people to sign in only in exchange for value. People need to understand why you’re asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app experience, access additional features, or synchronize data.
>
> Delay sign-in as long as possible. People often abandon apps when they’re forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore available content before signing in to stream something.
>
> If you require an account, ask people to set it up before offering any sign-in options. Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.
>
> Consider letting people link an existing account to Sign in with Apple. When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they’ve already set up. You can offer account linking before or after people sign in to their existing account. For example:
> - If people share an email address through Sign in with Apple and it matches the address in an existing account, you can suggest that they link Sign in with Apple to that account.
> - If people used an existing user name and password to sign in, you can display an account-linking suggestion in their account’s settings view or another logical place.
>
> In a commerce app, wait until after people make a purchase before asking them to create an account. If you support a guest checkout system, give people a quick way to create an account after the transaction completes. For example, if you support Apple Pay, let people create an account on the order confirmation page. In cases where people have already provided their name and email address during the Apple Pay transaction, you don’t need to ask for this information.
>
> As soon as Sign in with Apple completes, welcome people to their new account. Help people use their new account right away; don’t delay the experience by asking for information that isn’t required.
>
> Indicate when people are currently signed in. You can help people confirm their sign-in method by displaying a phrase like “Using Sign in with Apple” in places like a settings or account interface.

**Applies to:** Apps offering Sign in with Apple.

- **[TECH-30]** After Sign in with Apple completes, does the app proceed into the account without asking for information that isn't required?
  - quote: "Help people use their new account right away; don’t delay the experience by asking for information that isn’t required."
  - surface: runtime
  - verify: Sign up with Sign in with Apple on a simulator/device; WARN if mandatory forms appear asking for data not required (e.g., re-entering name/email already received). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Make post-sign-up fields optional or remove them.
- **[TECH-31]** Does the settings/account interface indicate the current sign-in method (e.g., “Using Sign in with Apple”)?
  - quote: "Indicate when people are currently signed in."
  - surface: code
  - verify: Inspect the account/settings view for a sign-in method indicator when the session originated from `ASAuthorizationAppleIDCredential`. Advisory — WARN if absent.
  - fix: Show "Using Sign in with Apple" in the account screen.
- **[TECH-118]** In a commerce app, does account creation wait until after the purchase (guest checkout with account creation afterward)?
  - quote: "In a commerce app, wait until after people make a purchase before asking them to create an account."
  - surface: runtime
  - verify: If the app sells goods/services, attempt a purchase on a fresh install; note whether account creation is forced before checkout. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Offer guest checkout and an account-creation option on the order confirmation screen.

## SIWA.C Sign in with Apple HIG — Collecting data

**Source text (verbatim):**
> People appreciate Sign in with Apple for its privacy and convenience. Although some apps or websites may require additional information — such as a date of birth or a region of residence — it’s essential to minimize your requests for data as people set up an account. Build on the trust that people have in Sign in with Apple by describing why you need additional data and clearly displaying the data you receive.
>
> Clarify whether the additional data you request is required or just recommended. If the data is legally or contractually required — such as an agreement to terms of service, country or region of residence, birth date, or information required by a region’s real-identity laws — make sure people understand that they must supply the additional information to complete the setup of their account. If additional data isn’t required but can improve the user experience, make sure people know the request is optional and help them understand the benefits of providing the information.
>
> Don’t ask people to supply a password. A key benefit of Sign in with Apple is that people don’t have to create and memorize additional passwords. Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.
>
> Avoid asking for a personal email address when people supply a private relay address. Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account. It’s essential to respect this choice and avoid overriding it by asking for a personal email address. If you present customer service, retail, or other experiences that request identification via email address, you can:
> - Make sure that people can view their private relay address in your app or website
> - Direct people to Settings > Apple Account > Password & Security > Apps using Apple Account to retrieve their private relay address
> - Use other identifying values, like an order number or phone number collected as part of a purchase
>
> Give people a chance to engage with your app before asking for optional data. As people use your app, you can help them discover places where they can benefit from sharing more information with you. For example, you might suggest that they provide a contact phone number if they want real-time text updates, or social network information if they want to play games with friends. If people choose not to provide optional information, don’t prevent them from accessing their account or using all the features of your app.
>
> Be transparent about the data you collect. People value knowing how you use the data that they share with you. One way you can be transparent is to welcome people by using the name or email address they shared. Doing this helps establish how you use this information and, for a relay address, shows people where to find it in the future. If you don’t display all the data that people provide, they are likely to wonder why you asked for it.

**Applies to:** Apps offering Sign in with Apple.

- **[TECH-32]** Does the Sign in with Apple flow avoid asking people to supply or create a password?
  - quote: "Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password."
  - surface: code
  - verify: After the `ASAuthorizationAppleIDCredential` success handler, inspect the next screens for `SecureField`/`isSecureTextEntry` password fields. WARN if a password is requested for Sign in with Apple users. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Remove the password step for Sign in with Apple users.
- **[TECH-33]** When a private relay address is received, does the app avoid asking for a personal email address?
  - quote: "It’s essential to respect this choice and avoid overriding it by asking for a personal email address."
  - surface: code
  - verify: Grep the post-sign-in flow for email fields shown when the email ends with `privaterelay.appleid.com` or when the credential email is present; WARN if the app asks for another email. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Use the relay address; show it in the account screen.
- **[TECH-34]** Are additional data requests clearly labeled as required or optional, and does declining optional data never block account access or features?
  - quote: "If people choose not to provide optional information, don’t prevent them from accessing their account or using all the features of your app."
  - surface: runtime
  - verify: Sign up and skip every optional field; confirm full access. Check field labels indicate required vs optional. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Mark optional fields, make them skippable, and remove feature gates tied to optional data.

## SIWA.D Sign in with Apple HIG — Displaying buttons

**Source text (verbatim):**
> Apple provides several Sign in with Apple buttons you can use to let people set up an account and sign in. If necessary, you can create a custom button to offer Sign in with Apple; for guidelines, see Creating a custom Sign in with Apple button.
>
> Prominently display a Sign in with Apple button. Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button.
>
> **Using the system-provided buttons**
>
> When you use the system-provided APIs to create a Sign in with Apple button, you get the following advantages.
> - A button that’s guaranteed to use an Apple-approved appearance
> - Assurance that the button’s contents maintain ideal proportions as you change its style
> - Automatic translation of the button’s title into the language specified by the device
> - Support for configuring the button’s corner radius to match the style of your UI (iOS, macOS, and web)
> - A system-provided alternative text label that lets VoiceOver describe the button
>
> For developer guidance, see ASAuthorizationAppleIDButton (iOS, macOS, and tvOS), WKInterfaceAuthorizationAppleIDButton (watchOS), and Displaying Sign in with Apple buttons on the web. You can also visit Sign in with Apple button to view and adjust live previews of web-based buttons and get the code.
>
> The system provides several variants of the button title. Depending on the platform on which your content runs, choose the variant that fits the terminology of your sign-in experience and use it consistently throughout your interfaces.
>
> The following button titles are available for iOS, macOS, tvOS, and the web:

Note: the button titles are shown as images on Apple's page.

>
> For watchOS, the system provides one title:  Sign in.
>
> Depending on the platform, the system provides up to three options for the appearance of the Sign in with Apple button: white, white with an outline, and black. Choose the appearance that works best with the background on which the button displays.
>
> **White** — The white style is available on all platforms and the web. Use this style on dark backgrounds that provide sufficient contrast.
>
> **White with outline** — The white outlined style is available in iOS, macOS, and the web. Use this style on white or light-color backgrounds that don’t provide sufficient contrast with the white button fill. Avoid using this style on a dark or saturated background, because the black outline can add visual clutter; instead, use the white style to contrast with a dark background.
>
> **Black** — The black style is available on all platforms and the web. Use this style on white or light-color backgrounds that provide sufficient contrast; don’t use it on black or dark backgrounds.
>
> Unlike the black Sign in with Apple button for other platforms, the watchOS button uses a fill color that’s not fully black. To contrast with the pure black background of Apple Watch, the watchOS button uses the system-defined dark gray appearance.
>
> **Button size and corner radius**
>
> Adjust the corner radius to match the appearance of other buttons in your app. By default, the Sign in with Apple button has rounded corners. In iOS, macOS, and the web, you can change the corner radius to produce a button with square corners or a capsule-shape button. For developer guidance, see cornerRadius (iOS and macOS) and Displaying Sign in with Apple buttons on the web.
>
> Maintain the minimum button size and margin around the button in iOS, macOS, and the web. Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.
>
> | Minimum width | Minimum height | Minimum margin |
> |---|---|---|
> | 140pt (140px @1x, 280px @2x) | 30pt (30px @1x, 60px @2x) | 1/10 of the button’s height |

**Applies to:** Apps offering Sign in with Apple.

- **[TECH-35]** Is the Sign in with Apple button no smaller than other sign-in buttons and visible without scrolling?
  - quote: "Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button."
  - surface: code
  - verify: In the sign-in view, compare frame/height modifiers of `SignInWithAppleButton`/`ASAuthorizationAppleIDButton` with Google/Facebook/email buttons; run on the smallest supported device (e.g., iPhone SE simulator) and confirm the button is on screen without scrolling. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Give the Apple button the same (or larger) size and place it above the fold.
- **[TECH-36]** Does the app use a system-provided Sign in with Apple button (`ASAuthorizationAppleIDButton`, `WKInterfaceAuthorizationAppleIDButton`, or the SwiftUI equivalent), or a custom button (which must then pass the SIWA.E checks)? (Routing check: the source lists advantages of the system button but does not require it.)
  - quote: "A button that’s guaranteed to use an Apple-approved appearance"
  - surface: code
  - verify: Grep for `ASAuthorizationAppleIDButton`, `SignInWithAppleButton`, `WKInterfaceAuthorizationAppleIDButton`. If Sign in with Apple is triggered by a custom `Button` instead, run TECH-39–TECH-42 and TECH-119. Report as INFO (PASS either way).
  - fix: none required; using the system-provided button avoids the custom-button checks.
- **[TECH-37]** Does the button style suit its background (white on dark; white-outline or black on light; never black on black/dark backgrounds)?
  - quote: "Use this style on white or light-color backgrounds that provide sufficient contrast; don’t use it on black or dark backgrounds."
  - surface: code
  - verify: Check the `.signInWithAppleButtonStyle(...)` / `ASAuthorizationAppleIDButton.Style` against the background color in both light and dark appearance (e.g., style should switch with `colorScheme`). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Use `.white` in dark mode and `.black`/`.whiteOutline` in light mode.
- **[TECH-38]** Does the button meet Apple's guidance minimums of 140pt width, 30pt height and a margin of 1/10 of its height (iOS, macOS, web)? (Apple gives these values "for guidance".)
  - quote: "Maintain the minimum button size and margin around the button in iOS, macOS, and the web."
  - surface: code
  - verify: Inspect `.frame(...)`/Auto Layout constraints on the button; confirm width ≥ 140, height ≥ 30, and surrounding padding ≥ height/10. Advisory (Apple: "Use the following values for guidance") — report as WARN, not FAIL.
  - fix: Adjust constraints/frame to meet the minimums.

## SIWA.E Sign in with Apple HIG — Creating a custom Sign in with Apple button

**Source text (verbatim):**
> If your interface requires it, you can create a custom Sign in with Apple button for iOS, macOS, or the web. For example, you may want to align logos across multiple sign-in buttons, use buttons that display only a logo, or adjust the button’s font, bezel, or background appearance to coordinate with your UI.
>
> Always make sure that people can instantly identify your custom button as a Sign in with Apple button. If your custom button differs too much from the standard one, people may not feel comfortable using it to set up an account or sign in. App Review evaluates all custom Sign in with Apple buttons.
>
> Apple Design Resources provides downloadable Apple logo artwork you can use to create custom Sign in with Apple buttons that display either a logo only or a logo and text. The logo files are available in PNG, SVG, and PDF formats, and the artwork for both types of buttons includes both black and white versions. Here are examples of the black and white logo-only art files, each with a background added for visibility.
>
> All downloadable logo files include padding that simplifies positioning the logo in a button. Logo-only logo files include horizontal and vertical padding that ensures the correct proportion of the logo relative to the button. In addition to padding that keeps the logo and button correctly proportioned, logo files for buttons with text also include horizontal padding that provides a minimum margin between the logo and the button’s leading edge and title.
>
> Use only the logo artwork downloaded from Apple Design Resources; never create a custom Apple logo. As you create a custom Sign in with Apple button, follow these guidelines for using the downloadable logo file:
> - Use the logo file to position the Apple logo in a button; never use the Apple logo as a button.
> - Match the height of the logo file to the height of the button.
> - Don’t crop the logo file.
> - Don’t add vertical padding.
>
> To make sure that your custom button is visually consistent with the system-provided Sign in with Apple button, don’t change the following attributes.
> - Titles. Use only Sign in with Apple, Sign up with Apple, or Continue with Apple.
> - General shape. Buttons that combine the logo with text are always rectangular; logo-only buttons can be circular or rectangular.
> - Logo and title colors. Within a button, both items must be either black or white; don’t use custom colors.
>
> To coordinate with your app design, you can change:
> - Title font. You can also adjust the font’s weight and size.
> - Title case. You can capitalize every letter in the title.
> - Background appearance. The overall color needs to remain black or white. If necessary, you can include a subtle texture or gradient to help the button harmonize with your interface.
> - Button corner radius. You can use a corner radius value that matches the other buttons in your UI.
> - Button bezel and shadow. For example, you can use a stroke to emphasize the button bezel or add a drop shadow.
>
> **Custom buttons with a logo and text**
>
> Choose the format of the logo file based on the height of your button. Because SVG and PDF are vector-based formats, you can use these files in buttons of any height. Use the PNG files only in buttons that are 44 points tall, which is the default (and recommended) button height in iOS. Logos are available in small, medium, and large sizes, so you can match logo sizes in all the sign-up buttons you display.
>
> Prefer the system font for the title — that is, Sign in with Apple, Sign up with Apple, or Continue with Apple. Regardless of the font you choose, the title and button height of your custom button need to use the same proportions that the system uses. Using the system font for example, the title’s font size would be 43% of the button’s height — in other words, the button’s height would be 233% of the title’s font size, rounded to the nearest integer. Here are two examples that show these proportions using different sizes of the system font.
>
> In general, preserve the capitalization style of the title. By default, all variants of the button title capitalize the first word — that is, Sign or Continue — and Apple; all other letters are lowercase. Avoid changing this style unless your interface uses only uppercase.
>
> Keep the title and logo vertically aligned within the button. To do this, vertically align the title to the middle of the button, then add the logo image, making sure its height matches the height of the button. Because the logo image includes top and bottom padding, vertically aligning the title in the button ensures that the title, the logo, and the button stay properly aligned.
>
> Inset the logo if necessary. If you need to horizontally align the Apple logo with other authentication logos, you can adjust the space between the logo and the button’s leading edge.
>
> Maintain a minimum margin between the title and the right edge of the button. Ensure the margin measures at least 8% of the button’s width.
>
> Maintain the minimum button size and margin around the button. Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.
>
> | Minimum width | Minimum height | Minimum margin |
> |---|---|---|
> | 140 pt (140 px @1x, 280 px @2x) | 30 pt (30 px @1x, 60 px @2x) | 1/10 of the button’s height |
>
> **Custom logo-only buttons**
>
> Choose the format of the logo file based on the size of your button. The downloadable artwork for logo-only buttons is available in SVG, PDF, and PNG formats. Use the vector-based SVG and PDF formats for buttons of any size; use the PNG format only in buttons that measure 44x44 pt.
>
> Don’t add horizontal padding to a logo-only image. A logo-only Sign in with Apple button always has a 1:1 aspect ratio, and the artwork already includes the correct padding on all sides.
>
> Use a mask to change the default square shape of the logo-only image. For example, you might want to use a circular or rounded rectangular shape to present all logo-only sign-in buttons. Never crop the Apple-provided artwork to decrease its built-in padding or use the logo by itself, and avoid including additional padding.
>
> Maintain a minimum margin around the button. Ensure the margin measures at least 1/10 of the button’s height.
>
> **Platform considerations**
>
> No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.

**Applies to:** Apps that draw their own Sign in with Apple button instead of the system button.

- **[TECH-39]** Does a custom button use only the titles “Sign in with Apple”, “Sign up with Apple”, or “Continue with Apple”?
  - quote: "Titles. Use only Sign in with Apple, Sign up with Apple, or Continue with Apple."
  - surface: code
  - verify: Grep the custom button's title strings (all localizations) for exact titles; FAIL on "Login with Apple", "Apple Login", "Sign in using Apple", etc.
  - fix: Change the title to one of the three permitted titles.
- **[TECH-40]** Does a custom button use only the logo artwork downloaded from Apple Design Resources (no custom Apple logo, logo file not cropped, no added vertical padding, logo not used by itself as the button)?
  - quote: "Use only the logo artwork downloaded from Apple Design Resources; never create a custom Apple logo."
  - surface: manual
  - verify: Inspect the image asset used in the custom button; ask the developer to confirm it came from Apple Design Resources unmodified.
  - fix: Replace with the Apple Design Resources logo file, or use the system button.
- **[TECH-41]** Within the custom button, are logo and title both black or both white, with the background black or white?
  - quote: "Within a button, both items must be either black or white; don’t use custom colors."
  - surface: code
  - verify: Inspect `foregroundColor`/`tint`/`backgroundColor` on the custom button.
  - fix: Use black or white only.
- **[TECH-42]** Does a logo+text custom button keep at least 8% of its width as margin between title and right edge, and does a logo-only button keep a 1:1 aspect ratio?
  - quote: "Ensure the margin measures at least 8% of the button’s width."
  - surface: code
  - verify: Inspect padding/frame values; for logo-only buttons confirm equal width and height (`aspectRatio(1, contentMode:)`). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Adjust padding and aspect ratio.
- **[TECH-119]** Is a custom button instantly identifiable as Sign in with Apple and does it keep the general shape (logo+text buttons rectangular; logo-only circular or rectangular)?
  - quote: "General shape. Buttons that combine the logo with text are always rectangular; logo-only buttons can be circular or rectangular."
  - surface: manual
  - verify: Screenshot the custom button; FAIL if a logo+text button is not rectangular, or if it differs so much from the standard button that it is not instantly recognizable (Apple: "App Review evaluates all custom Sign in with Apple buttons.").
  - fix: Restore the standard shape and appearance, or switch to the system button.

## PERM.A Protected resources — complete list of Info.plist keys

**Source text (verbatim):**
> Control an app’s access to protected system services and user data.
>
> Before your app can access certain protected resources, like the Bluetooth interface, location information, or the user’s photos, the system asks the user for permission on behalf of your app. The prompt that the system displays includes a UsageDescription string you provide, explaining why your app needs to access the protected resource. Enter the string in the Signing and Capabilities editor for your app’s target, as described in Requesting access to protected resources. Xcode adds the string as the value for the relevant Information Property List key in your app’s build settings. The topics below list the keys you use to provide usage-description strings for protected resources.
>
> [Editor: keys listed on the page, grouped by Apple's topic headings —] Bluetooth (NSBluetoothAlwaysUsageDescription, NSBluetoothPeripheralUsageDescription); Calendar and reminders (NSCalendarsFullAccessUsageDescription, NSCalendarsWriteOnlyAccessUsageDescription, NSRemindersFullAccessUsageDescription); Camera and sound (NSAudioCaptureUsageDescription, NSCameraUsageDescription, NSMainCameraUsageDescription, NSMicrophoneUsageDescription); Contacts (NSContactsUsageDescription); Face ID (NSFaceIDUsageDescription); Files and folders (NSDesktopFolderUsageDescription, NSDocumentsFolderUsageDescription, NSDownloadsFolderUsageDescription, NSNetworkVolumesUsageDescription, NSRemovableVolumesUsageDescription, NSFileProviderDomainUsageDescription, NSFileProviderPresenceUsageDescription); Game Center (NSGKFriendListUsageDescription); Health (NSHealthClinicalHealthRecordsShareUsageDescription, NSHealthShareUsageDescription, NSHealthUpdateUsageDescription, NSHealthRequiredReadAuthorizationTypeIdentifiers); Home (NSHomeKitUsageDescription); Location (NSLocationAlwaysAndWhenInUseUsageDescription, NSLocationUsageDescription, NSLocationWhenInUseUsageDescription, NSLocationTemporaryUsageDescriptionDictionary, NSLocationAlwaysUsageDescription, NSWidgetWantsLocation, NSLocationDefaultAccuracyReduced); MediaPlayer (NSAppleMusicUsageDescription); Messages (NSCriticalMessagingUsageDescription); Motion (NSMotionUsageDescription, NSFallDetectionUsageDescription); Networking (NSLocalNetworkUsageDescription, NSNearbyInteractionUsageDescription, NSNearbyInteractionAllowOnceUsageDescription); NFC (NFCReaderUsageDescription); Photos (NSPhotoLibraryAddUsageDescription, NSPhotoLibraryUsageDescription); Scripting (NSAppleScriptEnabled); Security (NSUpdateSecurityPolicy, NSAppBundlesUsageDescription, NSAppDataUsageDescription, NSUserTrackingUsageDescription, NSUserTrackingMarkdownUsageDescription, NSAppleEventsUsageDescription, NSSystemAdministrationUsageDescription, ITSAppUsesNonExemptEncryption, ITSEncryptionExportComplianceCode); Sensors (NSSensorKitUsageDescription, NSSensorKitUsageDetail, NSSensorKitPrivacyPolicyURL); Siri (NSSiriUsageDescription); Speech (NSSpeechRecognitionUsageDescription); System Extensions (NSSystemExtensionUsageDescription, OSBundleUsageDescription); TV (NSVideoSubscriberAccountUsageDescription); Vision (NSWorldSensingUsageDescription, NSHandsTrackingUsageDescription, NSAccessoryTrackingUsageDescription); Wallet (NSFinancialDataUsageDescription, NSIdentityUsageDescription, NSIdentityUsageDescriptionDictionary); Wi-Fi (UIRequiresPersistentWiFi); Deprecated keys (NSCalendarsUsageDescription, NSEnterpriseMCAMUsageDescription, NSRemindersUsageDescription).
>
> [Editor: full table, one row per key page; Description = Apple's abstract; Platforms/Type/Xcode name from the page metadata; last column = sentences on that key's page stating when it is required or what happens without it.]
>
> | Key | Xcode name | Type | Description | Platforms | Requirement text (verbatim, from key page) |
> |---|---|---|---|---|---|
> | ITSAppUsesNonExemptEncryption | App Uses Non-Exempt Encryption | boolean | A Boolean value indicating whether the app uses encryption. | macOS 10.0 | — |
> | ITSEncryptionExportComplianceCode | App Encryption Export Compliance Code | string | The export compliance code provided by App Store Connect for apps that require it. | macOS 10.0 | — |
> | NFCReaderUsageDescription | Privacy - NFC Scan Usage Description | string | A message that tells people why the app is requesting access to the device’s NFC hardware. | iOS 11.0, iPadOS 11.0 | You’re required to provide this key if your app uses APIs that access the NFC hardware. |
> | NSAccessoryTrackingUsageDescription | Privacy - Accessory Tracking Usage Description | string | A message that tells a person why the app is requesting access to track accessory position and location. | visionOS 26.0 | Use this key to indicate that your app requires access to accessory-tracking data. |
> | NSAppBundlesUsageDescription | Privacy - App Management Usage Description | string | A message that tells people why the app needs to access the contents of other apps’ bundles. | macOS 13.0 | — |
> | NSAppDataUsageDescription | Privacy - Other Application Data Usage Description | string | A message that tells people why the app needs to access files in other apps’ sandbox containers. | macOS 14.0 | — |
> | NSAppleEventsUsageDescription | Privacy - AppleEvents Sending Usage Description | string | A message that tells people why the app is requesting the ability to send Apple events. | macOS 10.14 | This key is required if your app uses APIs that send Apple events. |
> | NSAppleMusicUsageDescription | Privacy - Media Library Usage Description | string | A message that tells people why the app is requesting access to their media library. | iOS 2.0, iPadOS 2.0, macOS 15.0, visionOS 1.0 | Your app must provide a value for this key to access a person’s media library. This requirement applies to iOS, iPadOS, visionOS, and macOS apps that link against the macOS 15 SDK or later. |
> | NSAppleScriptEnabled | Scriptable | boolean | A Boolean value indicating whether AppleScript is enabled. | macOS 10.0 | — |
> | NSAudioCaptureUsageDescription | — | string | A message that tells people why your app is requesting access to capture system audio on macOS. | macOS 14.2 | — |
> | NSBluetoothAlwaysUsageDescription | Privacy - Bluetooth Always Usage Description | string | A message that tells people why the app needs access to Bluetooth. | iOS 13.0, iPadOS 13.0, macOS 11.0, tvOS 13.0, visionOS 1.0, watchOS 6.0 | This key is required if your app uses the device’s Bluetooth interface. |
> | NSBluetoothPeripheralUsageDescription | Privacy - Bluetooth Peripheral Usage Description | string | A message that tells people why the app is requesting the ability to connect to Bluetooth peripherals. | iOS 6.0, iPadOS 6.0 | This key is required if your app uses APIs that access Bluetooth peripherals and has a deployment target earlier than iOS 13. |
> | NSCalendarsFullAccessUsageDescription | Privacy - Calendars Full Access Usage Description | string | A message that tells people why the app is requesting access to read and write their calendar data. | iOS 17.0, iPadOS 17.0, Mac Catalyst 17.0, macOS 14.0, visionOS 1.0, watchOS 10.0 | This key is required if your app uses APIs that read and write the person’s calendar data. |
> | NSCalendarsUsageDescription | Privacy - Calendars Usage Description | string | A message that tells people why the app is requesting access to their calendar data. | iOS 6.0, iPadOS 6.0, Mac Catalyst 13.0, macOS 10.14, watchOS 6.0 | This key is required if your app uses APIs that access the person’s calendar data. |
> | NSCalendarsWriteOnlyAccessUsageDescription | Privacy - Calendars Write Only Usage Description | string | A message that tells people why the app is requesting access to create calendar events. | iOS 17.0, iPadOS 17.0, Mac Catalyst 17.0, macOS 14.0, visionOS 1.0, watchOS 10.0 | This key is required if your app uses APIs that write to the person’s calendar data. |
> | NSCameraUsageDescription | Privacy - Camera Usage Description | string | A message that tells people why the app is requesting access to the device’s camera. | iOS 7.0, iPadOS 7.0, macOS 10.14, tvOS 17.0, visionOS 1.0 | This key is required if your app uses APIs that access the device’s camera. |
> | NSContactsUsageDescription | Privacy - Contacts Usage Description | string | A message that tells people why the app is requesting access to their contacts. | iOS 6.0, iPadOS 6.0, macOS 10.8, visionOS 1.0 | This key is required if your app uses APIs that access the user’s contacts. |
> | NSCriticalMessagingUsageDescription | Privacy - Critical Messaging Usage Description | string | A message that tells people why the app needs to send SMS messages. | iOS 18.2, iPadOS 18.2, watchOS 11.2 | — |
> | NSDesktopFolderUsageDescription | Privacy - Desktop Folder Usage Description | string | A message that tells people why the app needs access to their Desktop folder. | macOS 10.15 | — |
> | NSDocumentsFolderUsageDescription | Privacy - Documents Folder Usage Description | string | — | macOS 10.15 | — |
> | NSDownloadsFolderUsageDescription | Privacy - Downloads Folder Usage Description | string | A message that tells people why the app needs access to the user’s Downloads folder. | macOS 10.15 | — |
> | NSEnterpriseMCAMUsageDescription | Main Camera Usage Description | string | A message that tells people why the app is requesting access to the device’s main camera. | visionOS 2.0 | — |
> | NSFaceIDUsageDescription | Privacy - Face ID Usage Description | string | A message that tells people why the app is requesting the ability to authenticate with Face ID. | iOS 11.0, iPadOS 11.0 | This key is required if your app uses APIs that access Face ID. Also note that App Clips can’t use Face ID. For more information about functionality that’s unavailable to App Clips, see Choosing the right functionality for your App Clip. |
> | NSFallDetectionUsageDescription | Privacy - Fall Detection Usage Description | string | A message to the user that explains the app’s request for permission to access fall detection event data. | iOS 14.2, iPadOS 14.2, visionOS 1.0, watchOS 7.2 | If your app uses the CMFallDetectionManager, the app requires this key. |
> | NSFileProviderDomainUsageDescription | Privacy - Access to a File Provide Domain Usage Description | string | A message that tells people why the app needs access to files managed by a file provider. | macOS 10.15 | — |
> | NSFileProviderPresenceUsageDescription | Privacy - File Provider Presence Usage Description | string | A message that tells people why the app’s file provider needs to determine which files the person is currently accessing. | macOS 10.15 | — |
> | NSFinancialDataUsageDescription | Privacy - Financial Data Usage Description | string | A message that tells people why the app is requesting access to financial data stored in Wallet. | iOS 17.4, iPadOS 17.4 | — |
> | NSGKFriendListUsageDescription | — | string | A message that tells people why the app needs access to their Game Center friends list. | iOS 14.5, iPadOS 14.5 | — |
> | NSHandsTrackingUsageDescription | Privacy - Hands Tracking Usage Description | string | A message that tells people why the app is requesting access to track their hand position and location. | visionOS 1.0 | Use this key to indicate that your app requires access to hand-tracking data. |
> | NSHealthClinicalHealthRecordsShareUsageDescription | Privacy - Health Records Usage Description | string | A message to the user that explains why the app requested permission to read clinical records. | iOS 12.0, iPadOS 12.0, visionOS 1.0 | This key is required if your app uses APIs that access the user’s clinical records. |
> | NSHealthRequiredReadAuthorizationTypeIdentifiers | — | string | The clinical record data types that your app must get permission to read. | iOS 12.0, iPadOS 12.0, visionOS 1.0 | Use this key to indicate that your app requires access to specific clinical record data types to function properly. Set the value to an array of strings containing the type identifiers for your required types. |
> | NSHealthShareUsageDescription | Privacy - Health Share Usage Description | string | A message that explains to people why the app requests permission to read samples from the HealthKit store. | iOS 8.0, iPadOS 8.0, visionOS 1.0 | This key is required if your app uses APIs that access the someone’s health data. |
> | NSHealthUpdateUsageDescription | Privacy - Health Update Usage Description | string | A message to the user that explains why the app requested permission to save samples to the HealthKit store. | iOS 8.0, iPadOS 8.0, visionOS 1.0 | This key is required if your app uses APIs that update the user’s health data. |
> | NSHomeKitUsageDescription | Privacy - HomeKit Usage Description | string | A message that tells people why the app is requesting access to their HomeKit configuration data. | iOS 8.0, iPadOS 8.0, visionOS 1.0, watchOS 2.0 | This key is required if your app uses APIs that access the user’s HomeKit configuration data. |
> | NSIdentityUsageDescription | Privacy - Identity Usage Description | string | A message that tells people why the app is requesting identity information. | iOS 16.0, iPadOS 16.0, visionOS 1.0 | This key is required if your app uses APIs that access identity information from Wallet. |
> | NSIdentityUsageDescriptionDictionary | Privacy - Identity Usage Description Dictionary | dictionary | A dictionary that contains messages that explain why your app is requesting identity information. | iOS 26.2, iPadOS 26.2, visionOS 1.0 | In each description string, describe the reason the feature requires identity information. |
> | NSLocalNetworkUsageDescription | Privacy - Local Network Usage Description | string | A message that tells people why the app is requesting access to the local network. | iOS 14.0, iPadOS 14.0, macOS 11.0, tvOS 14.0, visionOS 1.0 | — |
> | NSLocationAlwaysAndWhenInUseUsageDescription | Privacy - Location Always and When In Use Usage Description | string | A message that tells people why the app is requesting access to their location information at all times. | iOS 11.0, iPadOS 11.0, visionOS 1.0 | This key is required if your iOS app uses APIs that access the user’s location information at all times. |
> | NSLocationAlwaysUsageDescription | Privacy - Location Always Usage Description | string | A message that tells people why the app is requesting access to their location at all times. | iOS 8.0, iPadOS 8.0 | This key is required if your iOS app uses APIs that access the user’s location at all times and deploys to targets earlier than iOS 11. |
> | NSLocationDefaultAccuracyReduced | Privacy - Location Default Accuracy Reduced | boolean | A Boolean value that indicates whether the app requests reduced location accuracy by default. | iOS 14.0, iPadOS 14.0, visionOS 1.0, watchOS 7.0 | — |
> | NSLocationTemporaryUsageDescriptionDictionary | Privacy - Location Temporary Usage Description Dictionary | dictionary | A collection of messages that explain why the app is requesting temporary access to their location. | iOS 14.0, iPadOS 14.0, macOS 11.0, visionOS 1.0 | — |
> | NSLocationUsageDescription | Privacy - Location Usage Description | string | A message that tells people why the app is requesting access to their location information. | iOS 6.0, iPadOS 6.0, macOS 10.14 | This key is required if your macOS app uses APIs that access the user’s location information. |
> | NSLocationWhenInUseUsageDescription | Privacy - Location When In Use Usage Description | string | A message that tells people why the app is requesting access to their location information while the app is running in the foreground. | iOS 11.0, iPadOS 11.0, visionOS 1.0 | This key is required if your iOS app uses APIs that access the user’s location information while the app is in use. |
> | NSMainCameraUsageDescription | Main Camera Usage Description | string | A message that tells people why the app is requesting access to the device’s main camera. | visionOS 26.0 | This key is required if your app uses APIs that access the device’s main camera. |
> | NSMicrophoneUsageDescription | Privacy - Microphone Usage Description | string | A message that tells people why the app is requesting access to the device’s microphone. | iOS 7.0, iPadOS 7.0, macOS 10.14, tvOS 17.0, visionOS 1.0, watchOS 4.0 | This key is required if your app uses APIs that access the device’s microphone. |
> | NSMotionUsageDescription | Privacy - Motion Usage Description | string | A message that tells people why the app is requesting access to the device’s motion data. | iOS 7.0, iPadOS 7.0, macOS 10.15, visionOS 1.0 | This key is required if your app uses APIs that access the device’s motion data, including CMSensorRecorder, CMPedometer, CMMotionActivityManager, and CMMovementDisorderManager. If you don’t include this key, your app will crash when it attempts to access motion data. |
> | NSNearbyInteractionAllowOnceUsageDescription | Privacy - Nearby Interaction Allow Once Usage Description | string | A one-time request for user permission to begin an interaction session with nearby devices. | iOS 14.0, iPadOS 14.0 | Define this property in the Info.plist only for apps that deploy to iOS 14. NSNearbyInteractionUsageDescription replaces this property in iOS 15 and later. |
> | NSNearbyInteractionUsageDescription | Privacy - Nearby Interaction Usage Description | string | A request for user permission to begin an interaction session with nearby devices. | iOS 15.0, iPadOS 15.0, watchOS 8.0 | — |
> | NSNetworkVolumesUsageDescription | Privacy - Network Volumes Usage Description | string | A message that tells people why the app needs access to files on a network volume. | macOS 10.15 | — |
> | NSPhotoLibraryAddUsageDescription | Privacy - Photo Library Additions Usage Description | string | A message that tells people why the app is requesting add-only access to their photo library. | iOS 11.0, iPadOS 11.0, visionOS 1.0 | This key is required if your app uses APIs that have write access to the user’s photo library. |
> | NSPhotoLibraryUsageDescription | Privacy - Photo Library Usage Description | string | A message that tells people why the app is requesting access to their photo library. | iOS 6.0, iPadOS 6.0, macOS 10.14, visionOS 1.0 | This key is required if your app uses APIs that have read or write access to the user’s photo library. |
> | NSRemindersFullAccessUsageDescription | Privacy - Reminders Full Access Usage Description | string | A message that tells people why the app is requesting access to read and write their reminders data. | iOS 17.0, iPadOS 17.0, Mac Catalyst 17.0, macOS 14.0, visionOS 1.0, watchOS 10.0 | This key is required if your app uses APIs that access the person’s reminder data. |
> | NSRemindersUsageDescription | Privacy - Reminders Usage Description | string | A message that tells people why the app is requesting access to their reminders. | iOS 6.0, iPadOS 6.0, Mac Catalyst 13.0, macOS 10.14, watchOS 6.0 | This key is required if your app uses APIs that access the person’s reminders. |
> | NSRemovableVolumesUsageDescription | Privacy - Removable Volumes Usage Description | string | A message that tells people why the app needs access to files on a removable volume. | macOS 10.15 | — |
> | NSSensorKitPrivacyPolicyURL | — | string | A hyperlink to a webpage that displays the privacy policy for your app’s research study. | iOS 14.0, iPadOS 14.0 | — |
> | NSSensorKitUsageDescription | — | string | A short description of the purpose of your app’s research study. | iOS 14.0, iPadOS 14.0 | — |
> | NSSensorKitUsageDetail | — | dictionary | A dictionary that includes keys for the specific information your app collects. | iOS 14.0, iPadOS 14.0 | — |
> | NSSiriUsageDescription | Privacy - Siri Usage Description | string | A message that tells people why the app is requesting to send user data to Siri. | iOS 10.0, iPadOS 10.0, visionOS 1.0 | This key is required if your app uses APIs that send user data to Siri. |
> | NSSpeechRecognitionUsageDescription | Privacy - Speech Recognition Usage Description | string | A message that tells people why the app is requesting to send user data to Apple’s speech recognition servers. | iOS 10.0, iPadOS 10.0, macOS 10.15, visionOS 1.0 | Include this key if your app uses the Speech framework. This applies regardless of whether you set requiresOnDeviceRecognition to true or false. If this key isn’t present, your app crashes when it calls requestAuthorization(_:). |
> | NSSystemAdministrationUsageDescription | Privacy - System Administration Usage Description | string | A message in macOS that tells people why the app is requesting to manipulate the system configuration. | macOS 10.14 | This key is required if your app uses APIs that manipulate the system configuration. |
> | NSSystemExtensionUsageDescription | Privacy - System Extension Usage Description | string | A message that tells people why the app is trying to install a system extension bundle. | iOS 18.4, iPadOS 18.4, Mac Catalyst 18.4, macOS 10.15 | This key is required for all system extensions except DriverKit extensions. |
> | NSUpdateSecurityPolicy | — | dictionary | A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle. | Mac Catalyst 16.0, macOS 13.0 | — |
> | NSUserTrackingMarkdownUsageDescription | Privacy - Tracking Markdown Usage Description | string | A message that explains the purpose for accessing data that an application can use to track a person or device. | iOS 27.2, iPadOS 27.2 | To use this key, the system requires that the device be located in a specific European Union (EU) country and signed in with an Apple Account that has its country or region set to a specific EU country or region: |
> | NSUserTrackingUsageDescription | Privacy - Tracking Usage Description | string | A message that explains the purpose for accessing data that an app can use to track a person or device. | iOS 14.0, iPadOS 14.0, tvOS 14.0, visionOS 1.0 | This key is required. Your app crashes if it attempts to use the App Tracking Transparency framework without including the key in your target’s properties in Xcode. |
> | NSVideoSubscriberAccountUsageDescription | Privacy - Video Subscriber Account Usage Description | string | A message that tells people why the app is requesting access to their TV provider account. | tvOS 9.0 | This key is required if your app uses APIs that access the user’s TV provider account. |
> | NSWidgetWantsLocation | Widget Wants Location | boolean | A Boolean value that indicates a widget uses the user’s location information. | iOS 14.0, iPadOS 14.0, macOS 11.0 | — |
> | NSWorldSensingUsageDescription | Privacy - World Sensing Usage Description | string | A message that tells people why the app is requesting access to image tracking, plane detection, or scene reconstruction. | visionOS 1.0 | Use this key to indicate that your app requires access to world-sensing data. |
> | OSBundleUsageDescription | Privacy - Driver Extension Usage Description | string | A message that tells people why the app is trying to install a driver extension bundle. | iOS 18.4, iPadOS 18.4, Mac Catalyst 18.4, macOS 10.15 | This key is required for all DriverKit extensions. |
> | UIRequiresPersistentWiFi | Application uses Wi-Fi | boolean | A Boolean value that indicates whether the app requires a Wi-Fi connection. | iOS 2.0, iPadOS 2.0, visionOS 1.0 | — |

Note: Platforms column lists the introduced-in versions from each key page. Apple's page metadata marks these keys deprecated: NSBluetoothPeripheralUsageDescription (iOS/iPadOS 13.0), NSCalendarsUsageDescription and NSRemindersUsageDescription (iOS/iPadOS/Mac Catalyst 17.0, macOS 14.0, watchOS 10.0), NSEnterpriseMCAMUsageDescription (visionOS 2.3), NSLocationAlwaysUsageDescription (iOS/iPadOS 10.0), NSLocationUsageDescription (iOS/iPadOS 8.0), NSNearbyInteractionAllowOnceUsageDescription (iOS/iPadOS 15.0). NSHealthRequiredReadAuthorizationTypeIdentifiers takes an array of strings.

**Additional key-page text (verbatim, from the named key's page):**
> NSBluetoothAlwaysUsageDescription — If your app has a deployment target earlier than iOS 13, add the NSBluetoothPeripheralUsageDescription key to your app’s Information Property List file in addition to this key.
>
> NSHealthRequiredReadAuthorizationTypeIdentifiers — To protect the user’s privacy, you must specify three or more required clinical record types.
>
> NSUserTrackingUsageDescription — Alternatively, in the European Union, your app can provide a tracking-usage description that supports rich text elements by using markdown format (see NSUserTrackingMarkdownUsageDescription).
>
> NSLocationAlwaysAndWhenInUseUsageDescription — Use this key if your iOS app accesses location information while running in the background. If your app only needs location information when in the foreground, use NSLocationWhenInUseUsageDescription instead.
>
> NSLocationAlwaysAndWhenInUseUsageDescription — If you need location information in a macOS app, use NSLocationUsageDescription instead. If your iOS app deploys to versions earlier than iOS 11, see NSLocationAlwaysUsageDescription.
>
> NSPhotoLibraryUsageDescription — If your app only adds assets to the photo library and does not read assets, use the  NSPhotoLibraryAddUsageDescription key instead.
>
> NSCalendarsWriteOnlyAccessUsageDescription — If your app needs to read calendar events in addition to creating them, use NSCalendarsFullAccessUsageDescription. If your app runs on iOS 17 or later and presents an EKEventEditViewController to allow people to create calendar events, you don’t need to request calendar access.
>
> NSLocalNetworkUsageDescription — Any app that uses the local network, directly or indirectly, should include this description. This includes apps that use Bonjour and services implemented with Bonjour, as well as direct unicast or multicast connections to local hosts.
>
> NSWidgetWantsLocation — To access the user’s location information from a widget, set the value to true in the widget extension’s Info.plist file.
>
> NSWidgetWantsLocation — Before a widget can access location information, the containing app must request authorization from the user. The containing app’s Info.plist file must also contain relevant purpose strings.
>
> NSIdentityUsageDescriptionDictionary — The dictionary allows up to 5 entries, and each usage description string allows up to 256 characters.

**Applies to:** Any app (or app extension) whose code — including third-party SDK code — references APIs that access a protected resource listed above.

- **[TECH-43]** For every protected-resource API referenced by the app or its SDKs, is the matching usage-description key present in the target's Info.plist (or `INFOPLIST_KEY_*` build setting)?
  - quote: "This key is required if your app uses APIs that access the device’s camera."
  - surface: code
  - verify: Build an API→key map from the table's requirement column and grep sources and linked frameworks: `AVCaptureDevice`/`UIImagePickerController(.camera)` → NSCameraUsageDescription; `AVAudioSession.requestRecordPermission`/`AVAudioApplication.requestRecordPermission`/`AVAudioRecorder` → NSMicrophoneUsageDescription; `PHPhotoLibrary`/`PHAsset` (read) → NSPhotoLibraryUsageDescription; `UIImageWriteToSavedPhotosAlbum`/`PHPhotoLibrary.requestAuthorization(for: .addOnly)` → NSPhotoLibraryAddUsageDescription; `CNContactStore` → NSContactsUsageDescription; `EKEventStore.requestFullAccessToEvents`→NSCalendarsFullAccessUsageDescription, `requestWriteOnlyAccessToEvents`→NSCalendarsWriteOnlyAccessUsageDescription, `requestFullAccessToReminders`→NSRemindersFullAccessUsageDescription; `CLLocationManager.requestWhenInUseAuthorization`→NSLocationWhenInUseUsageDescription, `requestAlwaysAuthorization`→NSLocationAlwaysAndWhenInUseUsageDescription; `CBCentralManager`/`CBPeripheralManager`→NSBluetoothAlwaysUsageDescription; `LAContext` with `.deviceOwnerAuthenticationWithBiometrics` → NSFaceIDUsageDescription; `ATTrackingManager.requestTrackingAuthorization`→NSUserTrackingUsageDescription; `CMPedometer`/`CMMotionActivityManager`/`CMSensorRecorder`/`CMMovementDisorderManager`→NSMotionUsageDescription; `CMFallDetectionManager`→NSFallDetectionUsageDescription; `SFSpeechRecognizer.requestAuthorization`→NSSpeechRecognitionUsageDescription; `HKHealthStore` read/write→NSHealthShareUsageDescription/NSHealthUpdateUsageDescription; `HMHomeManager`→NSHomeKitUsageDescription; `NFCNDEFReaderSession`/`NFCTagReaderSession`→NFCReaderUsageDescription; `INPreferences.requestSiriAuthorization`→NSSiriUsageDescription; `MPMediaLibrary`/`MusicKit` library access→NSAppleMusicUsageDescription; `VSAccountManager`→NSVideoSubscriberAccountUsageDescription; Wallet identity (`PKIdentityAuthorizationController`)→NSIdentityUsageDescription. Also run `nm -u`/`otool -L` on vendored binaries/xcframeworks to catch SDK references. FAIL for each API without its key.
  - fix: Add the missing key with a specific purpose string (or remove the code/SDK that references the API).
- **[TECH-44]** If the app uses App Tracking Transparency, is NSUserTrackingUsageDescription present (the app crashes without it)?
  - quote: "This key is required. Your app crashes if it attempts to use the App Tracking Transparency framework without including the key in your target’s properties in Xcode."
  - surface: code
  - verify: Grep for `import AppTrackingTransparency`/`ATTrackingManager`; check Info.plist/`INFOPLIST_KEY_NSUserTrackingUsageDescription`.
  - fix: Add NSUserTrackingUsageDescription with a specific purpose string.
- **[TECH-45]** If the app uses Core Motion activity/pedometer/sensor-recorder APIs, is NSMotionUsageDescription present (crash otherwise)?
  - quote: "If you don’t include this key, your app will crash when it attempts to access motion data."
  - surface: code
  - verify: Grep for `CMSensorRecorder`, `CMPedometer`, `CMMotionActivityManager`, `CMMovementDisorderManager`; check the key.
  - fix: Add NSMotionUsageDescription.
- **[TECH-46]** If the app uses the Speech framework (even with on-device recognition), is NSSpeechRecognitionUsageDescription present (crash otherwise)?
  - quote: "This applies regardless of whether you set requiresOnDeviceRecognition to true or false."
  - surface: code
  - verify: Grep for `import Speech`, `SFSpeechRecognizer`, `requiresOnDeviceRecognition`; check the key.
  - fix: Add NSSpeechRecognitionUsageDescription.
- **[TECH-47]** For deployment targets earlier than iOS 13, is NSBluetoothPeripheralUsageDescription present in addition to NSBluetoothAlwaysUsageDescription?
  - quote: "If your app has a deployment target earlier than iOS 13, add the NSBluetoothPeripheralUsageDescription key to your app’s Information Property List file in addition to this key."
  - surface: code
  - verify: Read `IPHONEOS_DEPLOYMENT_TARGET` in `project.pbxproj`; if < 13.0 and Core Bluetooth is used, require both keys.
  - fix: Add the missing key.
- **[TECH-48]** Does each location key match the app's actual use (When In Use vs Always; NSLocationAlwaysUsageDescription only for targets earlier than iOS 11; NSLocationUsageDescription for macOS)?
  - quote: "If your app only needs location information when in the foreground, use NSLocationWhenInUseUsageDescription instead."
  - surface: code
  - verify: Grep `requestAlwaysAuthorization` vs `requestWhenInUseAuthorization`; confirm NSLocationAlwaysAndWhenInUseUsageDescription only when Always is requested; check macOS targets use NSLocationUsageDescription.
  - fix: Add/remove keys to match the authorization actually requested.
- **[TECH-49]** If the app only adds photos without reading them, does it use NSPhotoLibraryAddUsageDescription instead of NSPhotoLibraryUsageDescription?
  - quote: "If your app only adds assets to the photo library and does not read assets, use the  NSPhotoLibraryAddUsageDescription key instead."
  - surface: code
  - verify: If the app only writes to the library (e.g., `UISaveVideoAtPathToSavedPhotosAlbum`, `UIImageWriteToSavedPhotosAlbum`) and never reads assets, confirm the add-only key is used. Note: Apple's AVFoundation article states `PHPhotoLibrary`/`PHAssetCreationRequest` "require read/write access" and need NSPhotoLibraryUsageDescription (see TECH-124).
  - fix: Switch to NSPhotoLibraryAddUsageDescription and request `.addOnly` access.
- **[TECH-50]** If the app only creates calendar events, does it use NSCalendarsWriteOnlyAccessUsageDescription (or present `EKEventEditViewController` on iOS 17+ without requesting access)?
  - quote: "If your app runs on iOS 17 or later and presents an EKEventEditViewController to allow people to create calendar events, you don’t need to request calendar access."
  - surface: code
  - verify: Grep EventKit usage (`requestFullAccessToEvents`, `requestWriteOnlyAccessToEvents`, `requestAccess(to: .event`, `EKEventEditViewController`) and compare with the keys present; flag deprecated NSCalendarsUsageDescription/NSRemindersUsageDescription as the only key on iOS 17+ targets.
  - fix: Use the narrowest key/API (write-only or `EKEventEditViewController`).
- **[TECH-51]** If the app uses the local network (Bonjour, unicast/multicast to local hosts), is NSLocalNetworkUsageDescription present?
  - quote: "Any app that uses the local network, directly or indirectly, should include this description."
  - surface: code
  - verify: Grep for `NWBrowser`, `NetService`, `NWListener`, `NSBonjourServices`, multicast (`NWMulticastGroup`), local IPs (`192.168.`, `.local`), Chromecast/DLNA SDKs; check the key.
  - fix: Add NSLocalNetworkUsageDescription (and NSBonjourServices when browsing services).
- **[TECH-52]** If the app accesses the media library (iOS/iPadOS/visionOS, or macOS apps linking the macOS 15 SDK or later), is NSAppleMusicUsageDescription present?
  - quote: "Your app must provide a value for this key to access a person’s media library."
  - surface: code
  - verify: Grep `MPMediaLibrary`, `MPMediaQuery`, `MusicLibrary`, `MusicAuthorization.request`; check the key.
  - fix: Add NSAppleMusicUsageDescription.
- **[TECH-53]** If a widget uses location, is NSWidgetWantsLocation set to true in the widget extension's Info.plist and do the containing app's Info.plist purpose strings exist?
  - quote: "The containing app’s Info.plist file must also contain relevant purpose strings."
  - surface: code
  - verify: For WidgetKit extensions that use `CLLocationManager`, check the extension Info.plist for `NSWidgetWantsLocation` = true and the app Info.plist for location purpose strings.
  - fix: Add the key to the widget extension and purpose strings to the app.
- **[TECH-54]** If the app reads clinical records, does NSHealthRequiredReadAuthorizationTypeIdentifiers (when used) list three or more types, and is NSHealthClinicalHealthRecordsShareUsageDescription present?
  - quote: "To protect the user’s privacy, you must specify three or more required clinical record types."
  - surface: code
  - verify: Inspect Info.plist arrays for `NSHealthRequiredReadAuthorizationTypeIdentifiers` (count ≥ 3) and the clinical-records key when `HKClinicalType` is used.
  - fix: Specify at least three required types or remove the key; add the clinical-records purpose string.
- **[TECH-55]** If NSIdentityUsageDescriptionDictionary is used, does it have at most 5 entries with each string at most 256 characters?
  - quote: "The dictionary allows up to 5 entries, and each usage description string allows up to 256 characters."
  - surface: code
  - verify: Parse the dictionary in Info.plist (`plutil -p`); count entries and string lengths.
  - fix: Reduce entries/shorten strings.
- **[TECH-56]** Is NSNearbyInteractionAllowOnceUsageDescription used only for apps that deploy to iOS 14 (NSNearbyInteractionUsageDescription for iOS 15+)?
  - quote: "Define this property in the Info.plist only for apps that deploy to iOS 14."
  - surface: code
  - verify: If `import NearbyInteraction` is used, check the deployment target and which key(s) are present.
  - fix: Use NSNearbyInteractionUsageDescription for iOS 15+ (keep the allow-once key only when deploying to iOS 14).
- **[TECH-57]** For macOS system extensions / DriverKit extensions, is NSSystemExtensionUsageDescription (non-DriverKit) or OSBundleUsageDescription (DriverKit) present?
  - quote: "This key is required for all system extensions except DriverKit extensions."
  - surface: code
  - verify: If the project contains `.systemextension`/`.dext` targets or uses `OSSystemExtensionRequest`, check the relevant key.
  - fix: Add the appropriate key.
- **[TECH-58]** If the app sends Apple events (macOS), is NSAppleEventsUsageDescription present?
  - quote: "This key is required if your app uses APIs that send Apple events."
  - surface: code
  - verify: Grep for `NSAppleScript`, `NSAppleEventDescriptor`, `AEDeterminePermissionToAutomateTarget`, `SBApplication`, `com.apple.security.automation.apple-events` entitlement.
  - fix: Add NSAppleEventsUsageDescription.
- **[TECH-120]** If the app has an App Clip, does the App Clip avoid Face ID?
  - quote: "Also note that App Clips can’t use Face ID."
  - surface: code
  - verify: For App Clip targets (`com.apple.developer.parent-application-identifiers` / `.appclip` product type), grep their sources for `LAContext` biometric policies and an NSFaceIDUsageDescription key. FAIL if the App Clip uses Face ID.
  - fix: Remove Face ID from the App Clip (offer it in the full app).

## PERM.B Requesting access to protected resources (UIKit article)

**Source text (verbatim):**
> Provide a purpose string that explains to a person why you need access to protected resources on their device.
>
> **Overview**
>
> Modern devices collect and store a wealth of sensitive information about people who use them. Many apps rely on this kind of data, and the device hardware that generates it, to do useful work. For example, a navigation app needs a person’s GPS coordinates to locate the person on a map. But not all apps need access to all data. The same navigation app doesn’t need access to a person’s health history, camera interface, or Bluetooth peripherals.
>
> Ensure your app accesses only what it needs to do its job. To support this principle, Apple’s operating systems restrict access to protected data and resources by default. Apps can request access on a case-by-case basis, providing an explanation for why they need access. The person who uses the app decides whether to grant or deny the request.
>
> Tip: In addition to asking people for permission to access a resource, in some cases, you also need to separately declare your intent to do so by adding an entitlement to your app, as described in Entitlements.
>
> **Provide a purpose string**
>
> The first time your app attempts to access a protected resource, the system prompts the person using the app for permission. In the following example, an iOS app called FoodDeliveryApp, which provides a food delivery service, generates a prompt requesting access to the person’s location:
>
> If the person grants permission, the system remembers the person’s choice and doesn’t prompt again. If the person denies permission, the access attempt that initiates the prompt, and any further attempts, fail in a resource-specific way. For the particular case of access to location data, the person can choose to allow access for one session only by tapping Allow Once.
>
> The system automatically generates the prompt’s title, which includes the name of your app. You supply a message called a purpose string or a usage description — in this case, “Your location allows you to view restaurants in delivery range of your address.” — to indicate the reason that your app needs the access. Accurately and concisely explaining to the person why your app needs access to sensitive data, typically in one complete sentence, lets the person make an informed decision and improves the chances that they grant access.
>
> To provide a purpose string, follow these steps in Xcode:
> - 1. Navigate to the Signing and Capabilities editor for your app.
> - 2. Click the Add (+) button to add a capability.
> - 3. Choose the protected resource you want to add; in this case, it’s “Location (When in Use)”.
> - 4. Enter the purpose string in the text field.
>
> Always provide a valid purpose string in the Signing and Capabilities editor if your app uses a protected resource. If you don’t, attempts to access the resource fail, and might cause your app to crash. Xcode detects when your app crashes for this reason and reports an issue, telling you to add the purpose string to your app. Click the Add button to provide the purpose string.
>
> Xcode adds a build setting to your app that configures the purpose string as the value for a Information Property List; in this example, the key is NSLocationWhenInUseUsageDescription, so the build setting is INFOPLIST_KEY_NSLocationWhenInUseUsageDescription. For more information on configuring information property list values using build settings, see Managing your app’s information property list values.
>
> If your app supports multiple locales, in addition to providing a purpose string in the Signing and Capabilities editor, localize the purpose string for each locale you support. Create a string catalog file called InfoPlist.xcstrings, and build your app to populate the string catalog with keys for the usage description strings in your app. Add the translations for your usage description strings to the localizations in the string catalog. For more information, see Localizing and varying text with a string catalog.
>
> **Adhere to the requirements for purpose strings**
>
> To give people useful, concise information about why you’re requesting access to protected resources, make sure each purpose string you provide is valid by checking the following:
> - The purpose string isn’t blank and doesn’t consist solely of whitespace characters.
> - The purpose string is shorter than 4,000 bytes. Typical purpose strings are one complete sentence, but you can provide additional information to help a person make the right decision about sharing personal information.
> - The purpose string has the proper type that the corresponding key requires, typically a string.
> - The purpose string provides a description that’s accurate, meaningful, and specific about why the app needs to access the protected resource.
>
> Adhere to these requirements for every purpose string in your app, including localized purpose strings.
>
> App Review checks for the use of protected resources, and rejects apps that contain code accessing those resources without a purpose string. For example, an app accessing location might receive the following information from App Review about the requirement that an NSLocationWhenInUseUsageDescription key be present:
> ```
> ITMS-90683: Missing purpose string in Info.plist. 
> Your app’s code references one or more APIs that access sensitive user 
> data, or the app has one or more entitlements that permit such access. 
> The Info.plist file for the "{app-bundle-path}" bundle should contain a 
> NSLocationWhenInUseUsageDescription key with a user-facing purpose string 
> explaining clearly and completely why your app needs the data.
> If you’re using external libraries or SDKs, they may reference APIs that 
> require a purpose string. While your app might not use these APIs, a 
> purpose string is still required. For details, visit: 
> https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy/requesting_access_to_protected_resources.
> ```
> To resolve this issue, provide a purpose string that explains why the app needs access to this sensitive information, or remove the code that’s accessing the resource.
>
> Note: If you’re using external libraries or SDKs, they may reference APIs that require a purpose string. Although your app might not use these APIs, a purpose string is still necessary for App Review. You can contact the developer of the library or SDK to request information about which protected resources the developer uses and their purpose, or request that the developer release a version of their code that doesn’t contain the APIs. You’re responsible for all access of protected resources, including external SDK and library access.
>
> **Check for authorization**
>
> Many system frameworks that provide access to protected resources have dedicated APIs for checking and requesting authorization to use those resources. This model allows you to adjust your app’s behavior depending on the current access it has. For example, if a person denies your app permission to do something, you can remove related elements from your user interface.
>
> Because a person can change authorization at any time using Settings, always check the authorization status of a feature before accessing it. In cases without a dedicated API, prepare your app to gracefully handle access failures.
>
> **Reset authorization access**
>
> When your app attempts to access a protected resource after its first attempt, the system remembers the person’s permission choice and doesn’t prompt again. To prompt the person again, you need to reset access to these resources on your device or system.
>
> To reset permission access to a protected resource in iOS apps, tap Settings > General > Transfer or Reset iPhone > Reset > Reset Location & Privacy on your device.
>
> Important: Using Reset Location & Privacy resets location and privacy settings for all services on your device.
>
> To reset permissions for a particular service in macOS apps, run the tccutil reset <service name> command in Terminal. For example, to reset all permissions for AppleEvents, type: $ tccutil reset AppleEvents
>
> This command resets authorization access for all apps using the protected resource. You can similarly specify Camera, Calendar, Reminders, or other services to reset them individually. For more information, see Resetting access to protected resources in macOS.

**Applies to:** All apps that use a protected resource (directly or via SDKs).

- **[TECH-59]** Is every purpose string non-blank and not only whitespace (in every localization)?
  - quote: "The purpose string isn’t blank and doesn’t consist solely of whitespace characters."
  - surface: code
  - verify: `plutil -p Info.plist` and parse `InfoPlist.xcstrings`/`InfoPlist.strings`; for every key ending in `UsageDescription` check `value.strip() != ""`. Also check `INFOPLIST_KEY_*UsageDescription` build settings in `project.pbxproj`.
  - fix: Write a specific purpose string.
- **[TECH-60]** Is every purpose string shorter than 4,000 bytes and of the type the key requires (typically a string)?
  - quote: "The purpose string is shorter than 4,000 bytes."
  - surface: code
  - verify: For each usage key compute `len(value.encode('utf-8')) < 4000`; check the plist type matches the Type column in PERM.A (string vs dictionary).
  - fix: Shorten/correct type.
- **[TECH-61]** Does every purpose string accurately, meaningfully, and specifically describe why the app needs the resource (including localized versions)?
  - quote: "The purpose string provides a description that’s accurate, meaningful, and specific about why the app needs to access the protected resource."
  - surface: code
  - verify: Read each string; compare with the code path that requests the permission. FAIL on placeholders ("TODO", "Need access", "$(PRODUCT_NAME) needs camera", copy from templates) or descriptions that don't match the feature.
  - fix: Rewrite naming the feature and how data is used (see PERM.C).
- **[TECH-62]** If the app supports multiple locales, is each purpose string localized for each supported locale?
  - quote: "If your app supports multiple locales, in addition to providing a purpose string in the Signing and Capabilities editor, localize the purpose string for each locale you support."
  - surface: code
  - verify: Read `knownRegions` in `project.pbxproj` / `CFBundleLocalizations`; check `InfoPlist.xcstrings` (or `<lang>.lproj/InfoPlist.strings`) contains every usage key for every locale with state `translated`.
  - fix: Add translations to `InfoPlist.xcstrings`.
- **[TECH-63]** Are purpose strings provided for APIs referenced only by third-party SDKs (or the SDK/APIs removed)?
  - quote: "You’re responsible for all access of protected resources, including external SDK and library access."
  - surface: code
  - verify: For each SPM/CocoaPods/Carthage/xcframework dependency, grep sources or `nm`/`strings` the binaries for the protected-resource symbols listed in TECH-43; compare with Info.plist keys. Archive and check for ITMS-90683 warnings in any previous upload emails (manual).
  - fix: Add accurate purpose strings, or ask the SDK vendor for a version without those APIs / remove the SDK.
- **[TECH-64]** Does the app check authorization status before accessing a protected resource and handle denial gracefully?
  - quote: "Because a person can change authorization at any time using Settings, always check the authorization status of a feature before accessing it."
  - surface: code
  - verify: Grep for `authorizationStatus` usage near each protected API (`AVCaptureDevice.authorizationStatus(for:)`, `CLLocationManager.authorizationStatus`, `PHPhotoLibrary.authorizationStatus(for:)`, `CNContactStore.authorizationStatus(for:)`, `EKEventStore.authorizationStatus(for:)`, `ATTrackingManager.trackingAuthorizationStatus`). At runtime, deny each permission and confirm no crash/dead end.
  - fix: Check status before access and adapt the UI when denied.
- **[TECH-65]** Where a resource also needs an entitlement (e.g., HealthKit, HomeKit, Siri), is the entitlement present in the `.entitlements` file?
  - quote: "in some cases, you also need to separately declare your intent to do so by adding an entitlement to your app"
  - surface: code
  - verify: Compare frameworks used (`HealthKit`, `HomeKit`, `Intents`/SiriKit, `CoreNFC`) against `*.entitlements` (`com.apple.developer.healthkit`, `com.apple.developer.homekit`, `com.apple.developer.siri`, `com.apple.developer.nfc.readersession.formats`).
  - fix: Add the capability in Signing & Capabilities.

## PERM.C 5.1.1(ii) Write clear purpose strings

**Source text (verbatim):**
> Apple operating systems restrict access to protected data and resources by default, so before your app can access resources like the camera, location, microphone, or health data, it has to request permission. These requests often include a purpose string, also called a usage description, that explains how your app will use the requested data or resource.
>
> App Review Guideline 5.1.1(ii) specifies requirements for purpose strings:
>
> 5.1.1(ii) Permission
> [...] Ensure your purpose strings clearly and completely describe your use of the data. [...]
>
> This requirement allows users to make an informed decision about whether or not to grant your app access.
>
> **Best practices for purpose strings**
>
> A purpose string that only restates the name of the resource, or promises a general benefit without saying what your app actually does, doesn't meet the requirement.
>
> **Explain specifically how your app will use the data.**
>
> Do
> - Name the specific feature or outcome the data makes possible.
> - Write a separate purpose string for every protected resource your app requests.
>
> Don't
> - Don't obscure who has access to data behind a vague benefit or a passive construction, such as, "Your data will be used to provide a better experience."
> - Don't restate the name of the resource without explaining its use.
>
> **Provide an example of how the data will be used.**
>
> Do
> - Give a concrete example of what your app does with the data.
> - Write one brief, complete sentence in active voice and sentence case, ending with a period.
>
> Don't
> - Don't fill the request with marketing copy or a full feature list.
>
> | Insufficient examples | Clear and specific examples |
> |---|---|
> | "To use location." | "The app uses location data to determine the recommended route to your destination and provide turn-by-turn directions." |
> | "Your data will be used to provide a better experience." | "The app uses tracking data to deliver personalized advertising for products that are most relevant to you." |
>
> **FAQs**
>
> **Do purpose strings need to be localized?**
> Yes. If your app supports localizations for a global audience, you must provide localized purpose strings. Set your app to each localization and test to confirm the correct localized text appears in the permission request. Learn more about app localization.
>
> **A third-party SDK in my app requests permissions. Am I responsible for its purpose strings?**
> Yes. As stated in the App Review Guidelines and the Apple Developer Program License Agreement, you're responsible for everything in your app, including SDKs, libraries, and other code from third parties. SDKs can reference APIs that access protected resources such as location, sometimes without your realizing it. If your app has a valid reason to access a resource, define a purpose string on the Info.plist that describes your app's specific use case. If it doesn't, remove references to those APIs from your app's binary. Familiarize yourself with the resources an SDK may try to access before you submit.

**Applies to:** All apps that include purpose strings.

- **[TECH-66]** Does each purpose string do more than restate the resource name or promise a general benefit (i.e., name the specific feature or outcome)?
  - quote: "A purpose string that only restates the name of the resource, or promises a general benefit without saying what your app actually does, doesn't meet the requirement."
  - surface: code
  - verify: For each `*UsageDescription` value flag patterns like "To use location.", "Camera access", "This app needs access to your photos", "better experience", "improve your experience", "for app functionality".
  - fix: Rewrite as: what the app does + the feature it enables (e.g., "The app uses your camera to scan receipts and attach them to expenses.").
- **[TECH-67]** Is each purpose string one brief, complete sentence in active voice and sentence case, ending with a period, without marketing copy or a feature list?
  - quote: "Write one brief, complete sentence in active voice and sentence case, ending with a period."
  - surface: code
  - verify: Lint each string: ends with "." (or locale equivalent), single sentence, no passive constructions ("will be used", "is needed"), no exclamation/marketing words, no bullet lists. Advisory (listed under "Best practices" Do/Don't) — report as WARN, not FAIL.
  - fix: Rewrite to the pattern.
- **[TECH-68]** Is there a separate purpose string for every protected resource requested (no shared/duplicated generic text across keys)?
  - quote: "Write a separate purpose string for every protected resource your app requests."
  - surface: code
  - verify: Compare values of all usage keys; WARN if identical text is reused across different resources. Advisory (listed under "Best practices" Do/Don't) — report as WARN, not FAIL.
  - fix: Write a distinct string per resource.
- **[TECH-69]** Does the correct localized purpose string appear in each permission request when the app runs in each localization?
  - quote: "Set your app to each localization and test to confirm the correct localized text appears in the permission request."
  - surface: runtime
  - verify: Run the scheme with each App Language (Xcode scheme → Options → App Language) on a simulator after `xcrun simctl privacy <device> reset all <bundle-id>`; trigger each permission and screenshot the alert.
  - fix: Fix missing/incorrect translations in `InfoPlist.xcstrings`.

## PERM.D HIG Privacy — Introduction and best practices

**Source text (verbatim):**
> Privacy is paramount: it’s critical to be transparent about the privacy-related data and resources you require and essential to protect the data people allow you to access.
>
> People use their devices in very personal ways and they expect apps to help them preserve their privacy.
>
> When you submit a new or updated app, you must provide details about your privacy practices and the privacy-relevant data you collect so the App Store can display the information on your product page. (You can manage this information at any time in App Store Connect.) People use the privacy details on your product page to make an informed decision before they download your app. To learn more, see App privacy details on the App Store.
>
> **Best practices**
>
> Request access only to data that you actually need. Asking for more data than a feature needs — or asking for data before a person shows interest in the feature — can make it hard for people to trust your app. Give people precise control over their data by making your permission requests as specific as possible.
>
> Be transparent about how your app collects and uses people’s data. People are less likely to be comfortable sharing data with your app if they don’t understand exactly how you plan to use it. Always respect people’s choices to use system features like Hide My Email and Mail Privacy Protection, and be sure you understand your obligations with regard to app tracking. To learn more about Apple privacy features, see Privacy; for developer guidance, see User privacy and data use.
>
> Process data on the device where possible. In iOS, for example, you can take advantage of the Apple Neural Engine and custom CreateML models to process the data right on the device, helping you avoid lengthy and potentially risky round trips to a remote server.
>
> Adopt system-defined privacy protections and follow security best practices. For example, in iOS 15 and later, you can rely on CloudKit to provide encryption and key management for additional data types, like strings, numbers, and dates.

**Applies to:** All apps.

- **[TECH-70]** Have privacy details (App Privacy) been provided in App Store Connect for this new or updated app?
  - quote: "When you submit a new or updated app, you must provide details about your privacy practices and the privacy-relevant data you collect so the App Store can display the information on your product page."
  - surface: asc
  - verify: App Store Connect → Apps → [app] → App Privacy: confirm the data-collection answers are published (not "Get Started").
  - fix: Complete the App Privacy questionnaire based on the app's and SDKs' data collection.
- **[TECH-71]** Does the app request only permissions that a feature actually needs, with the narrowest variant available?
  - quote: "Give people precise control over their data by making your permission requests as specific as possible."
  - surface: code
  - verify: For each usage key, locate the feature using it; WARN for keys with no corresponding feature code; flag broader-than-needed variants (Always vs When In Use location, full vs add-only photos, full vs write-only calendars). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Remove unused keys/requests and switch to narrower variants.

## PERM.E HIG Privacy — Requesting permission

**Source text (verbatim):**
> Here are several examples of the things you must request permission to access:
> - Personal data, including location, health, financial, contact, and other personally identifying information
> - User-generated content like emails, messages, calendar data, contacts, gameplay information, Apple Music activity, HomeKit data, and audio, video, and photo content
> - Protected resources like Bluetooth peripherals, home automation features, Wi-Fi connections, and local networks
> - Device capabilities like camera and microphone
> - In a visionOS app running in a Full Space, ARKit data, such as hand tracking, plane estimation, image anchoring, and world tracking
> - The device’s advertising identifier, which supports app tracking
>
> The system provides a standard alert that lets people view each request you make. You supply copy that describes why your app needs access, and the system displays your description in the alert. People can also view the description — and update their choice — in Settings > Privacy.
>
> Request permission only when your app clearly needs access to the data or resource. It’s natural for people to be suspicious of a request for personal information or access to a device capability, especially if there’s no obvious need for it. Ideally, wait to request permission until people actually use an app feature that requires access. For example, you can use the location button to give people a way to share their location after they indicate interest in a feature that needs that information.
>
> Avoid requesting permission at launch unless the data or resource is required for your app to function. People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it. For example, people understand that a navigation app needs access to their location before they can benefit from it. Similarly, before people can play a visionOS game that lets them bounce virtual objects off walls in their surroundings, they need to permit the game to access information about their surroundings.
>
> Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting. The standard alert displays your copy (called a purpose string or usage description string) after your app name and before the buttons people use to grant or deny their permission. Aim for a brief, complete sentence that’s straightforward, specific, and easy to understand. Use sentence case, avoid passive voice, and include a period at the end. For developer guidance, see Requesting access to protected resources and App Tracking Transparency.
>
> | Example purpose string | Notes |
> |---|---|
> | The app records during the night to detect snoring sounds. | An active sentence that clearly describes how and why the app collects the data. |
> | Microphone access is needed for a better experience. | A passive sentence that provides a vague, undefined justification. |
> | Turn on microphone access. | An imperative sentence that doesn’t provide any justification. |

**Applies to:** All apps that request permissions.

- **[TECH-72]** Does the app avoid requesting permissions at launch unless the resource is required for the app to function, requesting instead when the feature is used?
  - quote: "Avoid requesting permission at launch unless the data or resource is required for your app to function."
  - surface: code
  - verify: Grep `application(_:didFinishLaunchingWithOptions:)`, `@main App.init`, root view `.onAppear`/`.task`, and onboarding for `requestAuthorization`, `requestWhenInUseAuthorization`, `requestAccess`, `requestTrackingAuthorization`. At runtime: fresh install (`xcrun simctl privacy booted reset all <bundle-id>`), launch, and record alerts shown before any user action. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Move each request to the moment the related feature is first used (or justify launch-time need).

## PERM.F HIG Privacy — Pre-alert screens, windows, or views

**Source text (verbatim):**
> Ideally, the current context helps people understand why you’re requesting their permission. If it’s essential to provide additional details, you can display a custom screen or window before the system alert appears. The following guidelines apply to custom views that display before system alerts that request permission to access protected data and resources, including camera, microphone, location, contact, calendar, and tracking.
>
> Include only one button and make it clear that it opens the system alert. People can feel manipulated when a custom screen or window also includes a button that doesn’t open the alert because the experience diverts them from making their choice. Another type of manipulation is using a term like “Allow” to title the custom screen’s button. If the custom button seems similar in meaning and visual weight to the allow button in the alert, people can be more likely to choose the alert’s allow button without meaning to. Use a term like “Continue” or “Next” to title the single button in your custom screen or window, clarifying that its action is to open the system alert.
>
> Don’t include additional actions in your custom screen or window, unless needed to obtain a legal consent. For example, don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel.

**Applies to:** Apps that show a custom screen before a system permission alert.

- **[TECH-73]** Does each pre-permission screen have exactly one button, titled like “Continue” or “Next” (not “Allow”), that opens the system alert?
  - quote: "Use a term like “Continue” or “Next” to title the single button in your custom screen or window, clarifying that its action is to open the system alert."
  - surface: code
  - verify: Find views shown immediately before permission requests (onboarding/priming screens). Count `Button`s; WARN if more than one or if titled "Allow"/"Enable"/"Turn On"/"Yes". Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Keep a single "Continue" button that triggers the system request.
- **[TECH-74]** Does the pre-permission screen avoid close/cancel/skip/"Not now" actions that leave without viewing the system alert (unless needed for legal consent)?
  - quote: "For example, don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel."
  - surface: code
  - verify: Check the priming view for "Not Now", "Skip", "Maybe later", "X" close buttons or swipe-to-dismiss (`interactiveDismissDisabled` absent on a sheet). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Remove secondary actions (or remove the custom screen entirely).

## PERM.G HIG Privacy — Tracking requests

**Source text (verbatim):**
> App tracking is a sensitive issue. In some cases, it might make sense to display a custom screen or window that describes the benefits of tracking. If you want to perform app tracking as soon as people launch your app, you must display the system-provided alert before you collect any tracking data.
>
> Never precede the system-provided alert with a custom screen or window that could confuse or mislead people. People sometimes tap quickly to dismiss alerts without reading them. A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.
>
> There are several prohibited custom-screen designs that will cause rejection. Some examples are offering incentives, displaying a screen or window that looks like a request, displaying an image of the alert, and annotating the screen behind the alert (as shown below). For the avoidance of confusion, a consent screen or window shown before or after an App Tracking Transparency system alert to comply with local privacy laws is allowed. To learn more, see App Review Guidelines: 5.1.1 (iv).
>
> [Editor: the page shows image tabs titled Incentive, Imitation request, Alert image, Alert annotation.]

**Applies to:** Apps that perform app tracking / use App Tracking Transparency.

- **[TECH-75]** If the app tracks from launch, is the ATT system alert shown before any tracking data is collected (ad/attribution SDKs not initialized with IDFA collection before authorization)?
  - quote: "If you want to perform app tracking as soon as people launch your app, you must display the system-provided alert before you collect any tracking data."
  - surface: code
  - verify: Find where ad/attribution/analytics SDKs (AppsFlyer, Adjust, Branch, Facebook SDK, Google Mobile Ads, Singular) are started and where `ATTrackingManager.requestTrackingAuthorization` is called; FAIL if IDFA (`ASIdentifierManager.advertisingIdentifier`) or tracking collection starts before authorization is `.authorized`. Runtime: proxy traffic (e.g., Charles/mitmproxy) on first launch before answering the alert.
  - fix: Delay SDK start / enable "wait for ATT" options until the authorization callback.
- **[TECH-76]** Does any screen before the ATT alert avoid incentives, imitation request UI, images of the alert, or annotations pointing at the alert?
  - quote: "Some examples are offering incentives, displaying a screen or window that looks like a request, displaying an image of the alert, and annotating the screen behind the alert (as shown below)."
  - surface: runtime
  - verify: Fresh install; screenshot each screen up to and including the ATT alert. FAIL for rewards ("get coins if you allow"), fake alert UI, alert screenshots, arrows/highlights toward "Allow".
  - fix: Remove the custom pre-prompt or reduce it to neutral explanatory content with one "Continue" button.

## PERM.H HIG Privacy — Location button

**Source text (verbatim):**
> In iOS, iPadOS, and watchOS, Core Location provides a button so people can grant your app temporary authorization to access their location at the moment a task needs it. A location button’s appearance can vary to match your app’s UI and it always communicates the action of location sharing in a way that’s instantly recognizable.
>
> The first time people open your app and tap a location button, the system displays a standard alert. The alert helps people understand how using the button limits your app’s access to their location, and reminds them of the location indicator that appears when sharing starts.
>
> After people confirm their understanding of the button’s action, simply tapping the location button gives your app one-time permission to access their location. Although each one-time authorization expires when people stop using your app, they don’t need to reconfirm their understanding of the button’s behavior.
>
> Note: If your app has no authorization status, tapping the location button has the same effect as when a person chooses Allow Once in the standard alert. If people previously chose While Using the App, tapping the location button doesn’t change your app’s status. For developer guidance, see LocationButton (SwiftUI) and CLLocationButton (Swift).
>
> Consider using the location button to give people a lightweight way to share their location for specific app features. For example, your app might help people attach their location to a message or post, find a store, or identify a building, plant, or animal they’ve encountered in their location. If you know that people often grant your app Allow Once permission, consider using the location button to help them benefit from sharing their location without having to repeatedly interact with the alert.
>
> Consider customizing the location button to harmonize with your UI. Specifically, you can:
> - Choose the system-provided title that works best with your feature, such as “Current Location” or “Share My Current Location.”
> - Choose the filled or outlined location glyph.
> - Select a background color and a color for the title and glyph.
> - Adjust the button’s corner radius.
>
> To help people recognize and trust location buttons, you can’t customize the button’s other visual attributes. The system also ensures a location button remains legible by warning you about problems like low-contrast color combinations or too much translucency. In addition to fixing such problems, you’re responsible for making sure the text fits in the button — for example, button text needs to fit without truncation at all accessibility text sizes and when translated into other languages.
>
> Important: If the system identifies consistent problems with your customized location button, it won’t give your app access to the device location when people tap it. Although such a button can perform other app-specific actions, people may lose trust in your app if your location button doesn’t work as they expect.

**Applies to:** Apps using `LocationButton` / `CLLocationButton`.

- **[TECH-77]** If the app uses a location button, does its text fit without truncation at all accessibility text sizes and in every localization, with no low-contrast/translucency warnings?
  - quote: "button text needs to fit without truncation at all accessibility text sizes and when translated into other languages."
  - surface: runtime
  - verify: Grep for `LocationButton`/`CLLocationButton`. Run with Dynamic Type set to the largest accessibility size (`xcrun simctl ui booted content_size accessibility-extra-extra-extra-large`) and each localization; check for truncation and console warnings about the button.
  - fix: Allow the button to grow, pick a shorter system title, adjust colors.

## PERM.I HIG Privacy — Protecting data

**Source text (verbatim):**
> Protecting people’s information is paramount. Give people confidence in your app’s security and help preserve their privacy by taking advantage of system-provided security technologies when you need to store information locally, authorize people for specific operations, and transport information across a network.
>
> Here are some high-level guidelines.
>
> Avoid relying solely on passwords for authentication. Where possible, use passkeys to replace passwords. If you need to continue using passwords for authentication, augment security by requiring two-factor authentication (for developer guidance, see Securing Logins with iCloud Keychain Verification Codes). To further protect access to apps that people keep logged in on their device, use biometric identification like Face ID, Optic ID, or Touch ID. For developer guidance, see Local Authentication.
>
> Store sensitive information in a keychain. A keychain provides a secure, predictable user experience when handling someone’s private information. For developer guidance, see Keychain services.
>
> Never store passwords or other secure content in plain-text files. Even if you restrict access using file permissions, sensitive information is much safer in an encrypted keychain.
>
> Avoid inventing custom authentication schemes. If your app requires authentication, prefer system-provided features like passkeys, Sign in with Apple or Password AutoFill. For related guidance, see Managing accounts.

**Applies to:** Apps that store credentials or sensitive information.

- **[TECH-78]** Is sensitive information (passwords, tokens and other secure content) stored in a keychain, and never in plain-text files?
  - quote: "Never store passwords or other secure content in plain-text files."
  - surface: code
  - verify: Grep for file writes and unencrypted stores (`UserDefaults`/`@AppStorage` plists, JSON/text files) holding keys like `password`, `token`, `accessToken`, `refreshToken`, `secret`; confirm `SecItemAdd`/a Keychain wrapper is used instead. (Apple: "Store sensitive information in a keychain.")
  - fix: Move secrets to the keychain (`SecItemAdd` with an appropriate `kSecAttrAccessible`).
- **[TECH-114]** Does the app avoid relying solely on passwords (passkeys where possible, or two-factor authentication if passwords remain)?
  - quote: "If you need to continue using passwords for authentication, augment security by requiring two-factor authentication"
  - surface: code
  - verify: Inspect the sign-in implementation for passkey support (`ASAuthorizationPlatformPublicKeyCredentialProvider`) or a second factor after password entry. Advisory (HIG guidance: "Avoid relying solely on passwords for authentication.") — report as WARN, not FAIL.
  - fix: Add passkeys or a second factor (developer decision).

## PERM.J HIG Privacy — Platform considerations

**Source text (verbatim):**
> No additional considerations for iOS, iPadOS, tvOS, or watchOS.
>
> **macOS**
>
> Sign your app with a valid Developer ID. If you choose to distribute your app outside the store, signing your app with Developer ID identifies you as an Apple developer and confirms that your app is safe to use. For developer guidance, see Xcode Help.
>
> Protect people’s data with app sandboxing. Sandboxing provides your app with access to system resources and user data while protecting it from malware. All apps submitted to the Mac App Store require sandboxing. For developer guidance, see Configuring the macOS App Sandbox.
>
> Avoid making assumptions about who is signed in. Because of fast user switching, multiple people may be active on the same system.
>
> **visionOS**
>
> By default, visionOS uses ARKit algorithms to handle features like persistence, world mapping, segmentation, matting, and environment lighting. These algorithms are always running, allowing apps and games to automatically benefit from ARKit while in the Shared Space.
>
> ARKit doesn’t send data to apps in the Shared Space; to access ARKit APIs, your app must open a Full Space. Additionally, features like Plane Estimation, Scene Reconstruction, Image Anchoring, and Hand Tracking require people’s permission to access any information. For developer guidance, see Setting up access to ARKit data.
>
> In visionOS, user input is private by design. The system automatically displays hover effects when people look at interactive components you create using SwiftUI or RealityKit, giving people the visual feedback they need without exposing where they’re looking before they tap. For guidance, see Eyes and Gestures > visionOS.
>
> Developer access to device cameras works differently in visionOS than it does in other platforms. Specifically, the back camera provides blank input and is only available as a compatibility convenience; the front camera provides input for spatial Personas, but only after people grant their permission. If the iOS or iPadOS app you’re bringing to visionOS includes a feature that needs camera access, remove it or replace it with an option for people to import content instead. For developer guidance, see Making your existing app compatible with visionOS.

**Applies to:** macOS apps (sandboxing); visionOS apps.

- **[TECH-79]** For a Mac App Store submission, is App Sandbox enabled?
  - quote: "All apps submitted to the Mac App Store require sandboxing."
  - surface: code
  - verify: For macOS targets (and Mac Catalyst), check the `.entitlements` file contains `com.apple.security.app-sandbox` = `true` (`codesign -d --entitlements - <App>.app` on an archive).
  - fix: Add the App Sandbox capability and the specific sandbox entitlements needed.
- **[TECH-80]** For a visionOS app brought from iOS/iPadOS, is any camera-dependent feature removed or replaced with an import option?
  - quote: "If the iOS or iPadOS app you’re bringing to visionOS includes a feature that needs camera access, remove it or replace it with an option for people to import content instead."
  - surface: code
  - verify: If the app supports visionOS (`SUPPORTED_PLATFORMS` includes `xros`/Designed for iPad on visionOS), check camera features are conditionally removed (`#if os(visionOS)`) or replaced.
  - fix: Hide camera features on visionOS and offer import.

## PERM.K Choosing the Location Services Authorization to Request

**Source text (verbatim):**
> Determine the authorization your app needs to access location data.
>
> The authorization status that your app has determines if and when it receives location events. There are two types of authorization your app can request:
> - When In Use: Your app can use all location services and receive events while the app is in use. In general, iOS apps are considered in use when they’re in the foreground or running in the background with the background location usage indicator enabled.
> - Always: Your app can use all location services and receive events even if the user is not aware that your app is running. If your app isn’t running, the system launches your app and delivers the event.
>
> **Prefer When In Use Authorization**
>
> Whenever possible, request only When In Use authorization. This mode has powerful features, allowing your app to:
> - Access all available location services while the user is using the app. If the user stops using your app, any outstanding requests suspend until the user resumes using your app.
> - Continue to get location updates even after your app enters the background, if you’ve enabled background location updates in your Xcode project. See Handling location updates in the background for more information.
> - Use location notification triggers to launch. If your app can rely on your user’s interaction, set up a UNLocationNotificationTrigger to notify users when they enter a relevant region. When users click through the notification, the system launches the app, making it eligible to receive the location event. This method lets users decide at a relevant moment whether to share their location with your app.
>
> **Ask for Always Authorization**
>
> Your app might require Always authorization in some situations where users can’t or don’t want to engage with your app every time you need location information. You may need to ask for Always authorization if:
> - Your app performs automated tasks during which a prompt might be inconvenient or undesirable. For example, if your app triggers automatic actions when the user enters a location, such as turning on the lights, your app may require Always authorization.
> - Your app records numerous locations throughout the day, such as for a diary app. The user may prefer to allow Always authorization so your app can record locations even when it’s not in use, and without prompting the user.
>
> Keep in mind that asking for authorization doesn’t guarantee your app will receive it. If you request Always authorization, the user has the option of granting your app When In Use authorization instead. You must always be prepared to run with When In Use authorization.
>
> Note: If your app requests and receives When In Use authorization, you can make a separate request for Always authorization later. However, apps may make only one request for Always authorization.

**Applies to:** Apps using Core Location on iOS.

- **[TECH-81]** If the app requests Always authorization, does it still work when only When In Use is granted?
  - quote: "You must always be prepared to run with When In Use authorization."
  - surface: runtime
  - verify: Grant "While Using the App" on the simulator (`xcrun simctl privacy booted grant location <bundle-id>`), exercise location features; confirm no dead ends or repeated prompts. In code, check handling of `.authorizedWhenInUse` in `locationManagerDidChangeAuthorization`.
  - fix: Handle `.authorizedWhenInUse` gracefully; degrade features that need Always.
- **[TECH-82]** Does the app request Always authorization only when needed (prefer When In Use)?
  - quote: "Whenever possible, request only When In Use authorization."
  - surface: code
  - verify: Grep `requestAlwaysAuthorization`; ask the developer which feature requires Always (automated tasks or recording locations when not in use, per the source). Advisory ("Whenever possible") — report as WARN, not FAIL.
  - fix: Use `requestWhenInUseAuthorization` (plus background location updates or `UNLocationNotificationTrigger`) where possible.
- **[TECH-121]** Does the app make at most one request for Always authorization (no repeated `requestAlwaysAuthorization` prompts expected)?
  - quote: "However, apps may make only one request for Always authorization."
  - surface: code
  - verify: Grep `requestAlwaysAuthorization` call sites; flag flows that call it repeatedly (e.g., on every launch or after a denial) and expect a new prompt instead of directing people to Settings.
  - fix: Request Always once, after When In Use is granted, at the moment the feature needs it; afterwards link to Settings.

## PERM.M Requesting authorization to capture and save media (AVFoundation)

**Source text (verbatim):**
> Prompt the user to authorize access to the camera, microphone, and photo library.
>
> In iOS and macOS 10.14 and later, the user must explicitly grant permission for each app to access the camera and microphone. Before your app can use a capture device for the first time, the system presents an alert with an app-specific message that you specify, to ask the user to grant your app access to the capture device.
>
> **Configure access alerts**
>
> The system requires that your app provides static messages to display to the user when the system asks for permission to access the camera or microphone:
> - If your app uses device cameras, include the NSCameraUsageDescription key in your app’s Info.plist file.
> - If your app uses device microphones, include the NSMicrophoneUsageDescription key in your app’s Info.plist file.
>
> For each key, provide a message that explains to the user why your app needs to capture media so the user can feel confident granting permission to your app.
>
> **Enable entitlements in macOS**
>
> In macOS, you also need to enable the following entitlements in Signing & Capabilities for your app targets:
> - If your app uses device cameras, enable the Camera entitlement.
> - If your app uses device microphones, enable the Audio Input Entitlement.
>
> Important: Your app needs to contain the appropriate key in its Info.plist file, and the appropriate entitlement enabled in macOS, before it requests authorization or attempts to use a capture device. Otherwise, the system terminates your app.
>
> **Verify and request authorization for capture**
>
> Always test the AVCaptureDevice authorizationStatus(for:) method before setting up a capture session. If the user hasn’t granted or denied capture permission, the authorization status is AVAuthorizationStatus.notDetermined. In this case, use the requestAccess(for:completionHandler:) method to tell the system to prompt the user.
>
> Call requestAccess(for:completionHandler:) before starting capture, but only at a time that’s appropriate for your app. For example, if photo or video capture isn’t the main focus of your app, check for permission only when the user invokes your app’s camera-related features.
>
> **Request authorization to save captured media**
>
> Your app must get permission to access the photo library before it attempts to save photos or videos; otherwise the system terminates your app. Which permission you request depends on the types of media you want to save:
> - For most photo and video capture workflows, including Live Photos and RAW format capture, use the PHPhotoLibrary and PHAssetCreationRequest classes. These classes require read/write access to the photo library, so you need to use the NSPhotoLibraryUsageDescription key in your Info.plist file to provide the user a message to request access. For additional information, see Delivering an Enhanced Privacy Experience in Your Photos App.
> - If your app only needs to save video to the photo library, the UISaveVideoAtPathToSavedPhotosAlbum(_:_:_:_:) function is a simpler alternative to PHPhotoLibrary. This function only requires write access to the library. Use the NSPhotoLibraryAddUsageDescription key in your Info.plist file to provide the user a message to request permission to save to the photo library.

**Applies to:** Apps that capture from the camera or microphone, or save captured media to the photo library.

- **[TECH-122]** For macOS targets that use the camera or microphone, are the Camera and Audio Input entitlements enabled (in addition to the Info.plist keys)?
  - quote: "Your app needs to contain the appropriate key in its Info.plist file, and the appropriate entitlement enabled in macOS, before it requests authorization or attempts to use a capture device. Otherwise, the system terminates your app."
  - surface: code
  - verify: For macOS (and Mac Catalyst) targets using `AVCaptureDevice`, check the `.entitlements` file for `com.apple.security.device.camera` / `com.apple.security.device.audio-input` and the Info.plist for NSCameraUsageDescription / NSMicrophoneUsageDescription. FAIL if either is missing for a used device.
  - fix: Enable Camera / Audio Input in Signing & Capabilities and add the usage keys.
- **[TECH-123]** Does capture code check `AVCaptureDevice.authorizationStatus(for:)` before setting up a capture session, and request access only when the user invokes camera-related features (when capture isn't the app's main focus)?
  - quote: "Always test the AVCaptureDevice authorizationStatus(for:) method before setting up a capture session."
  - surface: code
  - verify: Grep for `AVCaptureSession` setup and confirm a preceding `authorizationStatus(for:)` check and `requestAccess(for:)` only on `.notDetermined`; check the request is triggered from the camera feature, not at launch, unless capture is the app's main focus.
  - fix: Gate session setup on the authorization status; move the request to the camera feature's entry point.
- **[TECH-124]** Before saving captured photos/videos, does the app have the matching photo-library permission key (NSPhotoLibraryUsageDescription for `PHPhotoLibrary`/`PHAssetCreationRequest`; NSPhotoLibraryAddUsageDescription for `UISaveVideoAtPathToSavedPhotosAlbum`)?
  - quote: "Your app must get permission to access the photo library before it attempts to save photos or videos; otherwise the system terminates your app."
  - surface: code
  - verify: Grep for `PHAssetCreationRequest`, `PHPhotoLibrary.shared().performChanges`, `UISaveVideoAtPathToSavedPhotosAlbum`; confirm the matching key per the source's two bullets and an authorization request before the save.
  - fix: Add the matching key and request photo-library authorization before saving.

## ATS.A Preventing Insecure Network Connections

**Source text (verbatim):**
> Enforce secure network links in your app by relying on App Transport Security.
>
> On Apple platforms, a networking security feature called App Transport Security (ATS) improves privacy and data integrity for all apps and app extensions. It does this by requiring that network connections made by your app are secured by the Transport Layer Security (TLS) protocol using reliable certificates and ciphers. ATS blocks connections that don’t meet minimum security requirements.
>
> ATS operates by default for apps linked against the iOS 9.0 or macOS 10.11 SDKs or later. In cases where you need to connect to a server that isn’t fully secure—and that you can’t reconfigure to make more secure—you can add exceptions to loosen some of the ATS requirements.
>
> Note: If you link your app against an SDK older than iOS 9.0 or macOS 10.11, ATS is disabled no matter which version of the operating system your app runs on.
>
> **Prefer High-Level Frameworks in Your App**
>
> The system enforces ATS when you use the standard URL Loading System. Instances of URLSession automatically negotiate the most secure connection available from the server. The only action your app must take is to use secure URLs, like those beginning with https. Otherwise, ATS denies the connection and prints a console message:
> ```
> App Transport Security has blocked a cleartext HTTP (http://) resource
> load since it is insecure. Temporary exceptions can be configured via
> your app's Info.plist file.
> ```
> ATS doesn’t apply to calls your app makes to lower-level networking interfaces like the Network framework or CFNetwork. In these cases, you take responsibility for ensuring the security of the connection. You can construct a secure connection this way, but mistakes are both easy to make and costly. It’s typically safest to rely on the URL Loading System instead.
>
> **Ensure the Network Server Meets Minimum Requirements**
>
> A secure server establishes its identity using an X.509 digital certificate. A connecting client examines this certificate to perform default server trust evaluation, which includes checking that the certificate:
> - Has an intact digital signature, showing that the certificate hasn’t been tampered with.
> - Isn’t expired.
> - Has a name that matches the server’s DNS name.
> - Is signed by another valid certificate, which is in turned signed by another, and so on back to a trusted anchor certificate, which must be issued by a Certificate Authority (CA). The anchor certificate must be part of the client operating system, as indicated in Lists of available trusted root certificates in iOS, or be installed on the client by the user or a system administrator.
>
> ATS requires all of these things, and then provides extended security checks:
> - The server certificate must be signed with either a Rivest-Shamir-Adleman (RSA) key of at least 2048 bits, or an Elliptic-Curve Cryptography (ECC) key of at least 256 bits.
> - The certificate must use the Secure Hash Algorithm 2 (SHA-2) with a digest length, sometimes called a fingerprint, of at least 256 bits (that is, SHA-256 or greater).
> - The connection must use Transport Layer Security (TLS) protocol version 1.2 or later.
> - Data must be exchanged using either the AES-128 or the AES-256 symmetric cipher.
> - The link must support perfect forward secrecy (PFS) through Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange.
>
> Note: URLSession automatically handles server trust evaluation for you, but enables you to customize the process, for example to extend trust to a self-signed certificate embedded in your app, or to bypass certificate expiry. When ATS is enabled, you can no longer loosen trust evaluation requirements that way, but you can still tighten them — for example, to implement certificate pinning. For more information, see Performing manual server trust authentication.
>
> **Optional NIAP Functional Package for TLS Requirements**
>
> ATS provides support to further restrict default TLS client behavior to help meet requirements outlined by the National Information Assurance Partnership (NIAP) in the Functional Package for Transport Layer Security. This compliance mode is opt-in only and provides additional options for regulated environments. To opt-in to this mode, use the NSRequiresNIAPTLSPackageVersion key, which can be set to enforce this mode globally, and the NSExceptionRequiresNIAPTLSPackageVersion key to configure exceptions to the global policy on a per-domain basis.
>
> **Configure Exceptions Only When Needed and Prefer Server Fixes**
>
> ATS disallows a connection if the server fails to meet one of the security checks discussed in the previous section. Your best response is to update the server. If you can’t do that for some reason, you can specify exceptions in your app to disable one or more aspects of ATS.
>
> Important: It’s always better to fix the server when faced with an ATS failure. Exceptions reduce the security of your app. Some also require justification when submitting an app to the App Store, as described in the next section.
>
> You configure ATS exceptions by providing a dictionary as the value for the optional NSAppTransportSecurity key in your app’s Information Property List file. The dictionary has the following structure, where all keys are optional:
> ```
> NSAppTransportSecurity : Dictionary {
>     NSAllowsArbitraryLoads : Boolean
>     NSAllowsArbitraryLoadsForMedia : Boolean
>     NSAllowsArbitraryLoadsInWebContent : Boolean
>     NSAllowsLocalNetworking : Boolean
>     NSRequiresNIAPTLSPackageVersion : String
>     NSExceptionDomains : Dictionary {
>         <domain-name-string> : Dictionary {
>             NSIncludesSubdomains : Boolean
>             NSExceptionAllowsInsecureHTTPLoads : Boolean
>             NSExceptionMinimumTLSVersion : String
>             NSExceptionRequiresForwardSecrecy : Boolean
>             NSRequiresCertificateTransparency : Boolean
>             NSExceptionRequiresNIAPTLSPackageVersion : String
>         }
>     }
> }
> ```
> Keys at the first level of the NSAppTransportSecurity dictionary apply to connections made to any domain not specifically called out in the NSExceptionDomains subdictionary. For example, by setting NSAllowsArbitraryLoads to YES, you completely disable ATS for all network connections when you add this to your app’s Info.plist:
>
> Depending on your use case, you can provide narrower exceptions. For example, by setting NSAllowsArbitraryLoadsInWebContent to YES, you can disable ATS restrictions on calls made from within web views, like instances of WKWebView:
>
> You might only need to limit your ATS exception to a single domain. For example, if you need to access the insecure server http://example.com, you can still maintain all the benefits of ATS for other domains by setting the NSExceptionAllowsInsecureHTTPLoads to YES in the domain-specific sub-dictionary:
>
> Note: Global exceptions don’t apply to any domains that you add to the NSExceptionDomains dictionary. So you can invert the previous example—allowing insecure traffic on all domains except example.com—by placing NSAllowsArbitraryLoads at the top level, and including an empty example.com dictionary as an exception domain.
>
> You can use the nscurl command line tool to connect to a server using different combinations of ATS exceptions. This helps you quickly narrow down the source of any ATS failures you have and figure out what exceptions you need. See Identifying the Source of Blocked Connections for details.
>
> **Provide Justification for Exceptions**
>
> Adding certain ATS exceptions to your app’s Information Property List file requires you to provide justification, and might trigger additional App Store review for your app. Exceptions that require justification are:
> - Arbitrary connection exceptions (NSAllowsArbitraryLoads)
> - Media streaming exceptions (NSAllowsArbitraryLoadsForMedia)
> - Web content loads (NSAllowsArbitraryLoadsInWebContent)
> - Per-domain nonsecure connections (NSExceptionAllowsInsecureHTTPLoads)
> - Per-domain minimum TLS version (NSExceptionMinimumTLSVersion)
>
> NSRequiresNIAPTLSPackageVersion and NSExceptionRequiresNIAPTLSPackageVersion don’t require justification because they strengthen rather than weaken security requirements.
>
> Some examples of justifications eligible for consideration are:
> - The app must connect to a server managed by another entity that doesn’t support secure connections.
> - The app must support connecting to devices that cannot be upgraded to use secure connections, and that must be accessed using public host names.
> - The app must display embedded web content from a variety of sources, but can’t use a class supported by the web content exception.
> - The app loads media content that is encrypted and that contains no personalized information.
>
> When submitting your app to the App Store, provide sufficient information for the App Store to determine why your app cannot make secure connections by default.
>
> Important: Always look for a way to avoid using exceptions as a first recourse. If you must use an exception, make it as limited in scope as possible.

**Applies to:** All apps and app extensions that make network connections.

- **[TECH-83]** Does the app use secure (`https`) URLs for URL Loading System requests?
  - quote: "The only action your app must take is to use secure URLs, like those beginning with https."
  - surface: code
  - verify: Grep sources, plists and config files for `"http://` (excluding `http://localhost`, XML namespaces, and comments); run the app and check the console for "App Transport Security has blocked a cleartext HTTP".
  - fix: Switch endpoints to `https://` (fix servers if needed).
- **[TECH-84]** Does the Info.plist avoid ATS exceptions that require justification (NSAllowsArbitraryLoads, NSAllowsArbitraryLoadsForMedia, NSAllowsArbitraryLoadsInWebContent, NSExceptionAllowsInsecureHTTPLoads, NSExceptionMinimumTLSVersion), or, if present, is a justification ready for submission?
  - quote: "Adding certain ATS exceptions to your app’s Information Property List file requires you to provide justification, and might trigger additional App Store review for your app."
  - surface: code
  - verify: `plutil -extract NSAppTransportSecurity xml1 -o - Info.plist` for each target (app + extensions) and check `INFOPLIST_KEY_` settings; list each justification-requiring key. If any exist, confirm with the developer that the reason (matching one of the listed example justifications) will be supplied to App Review with the submission.
  - fix: Remove the exception (fix the server), narrow it to a single domain in NSExceptionDomains, or prepare the justification text for App Review.
- **[TECH-85]** Is each ATS exception as limited in scope as possible (per-domain instead of global; no `NSIncludesSubdomains` unless needed)?
  - quote: "If you must use an exception, make it as limited in scope as possible."
  - surface: code
  - verify: WARN if `NSAllowsArbitraryLoads` = YES is used where only specific domains/web content/media need it; flag wildcard-like broad subdomain inclusions. Advisory ("as limited in scope as possible") — report as WARN, not FAIL.
  - fix: Replace global exceptions with NSExceptionDomains entries or NSAllowsArbitraryLoadsInWebContent/ForMedia.
- **[TECH-86]** Do the app's servers meet ATS minimums (TLS 1.2+, RSA ≥2048/ECC ≥256-bit key, SHA-256+ signature, AES-128/256, ECDHE forward secrecy, valid trusted unexpired cert matching the DNS name)?
  - quote: "The connection must use Transport Layer Security (TLS) protocol version 1.2 or later."
  - surface: runtime
  - verify: On macOS run `nscurl --ats-diagnostics --verbose https://<host>` for every host the app contacts (collect from code and a proxy capture); FAIL if the default ATS configuration fails.
  - fix: Update server TLS configuration/certificates.
- **[TECH-87]** Does code using lower-level networking (Network framework, CFNetwork, raw sockets) ensure secure connections itself?
  - quote: "ATS doesn’t apply to calls your app makes to lower-level networking interfaces like the Network framework or CFNetwork. In these cases, you take responsibility for ensuring the security of the connection."
  - surface: code
  - verify: Grep for `NWConnection`, `NWParameters.tcp` (without `.tls`), `CFStreamCreatePairWithSocketToHost`, BSD sockets, third-party socket libs; confirm TLS is used for remote hosts.
  - fix: Use `NWParameters.tls` / URLSession, or document why plaintext is safe (e.g., local network only).
- **[TECH-88]** Are ATS keys spelled and typed as documented (Boolean/String/Dictionary per the structure)?
  - quote: "The dictionary has the following structure, where all keys are optional:"
  - surface: code
  - verify: Parse NSAppTransportSecurity with `plutil -p`; compare every key and type against the structure in ATS.A and the key table above; flag keys not in the documented structure as likely misspellings; FAIL on misspellings (e.g., `NSAllowArbitraryLoads`) or wrong types (string "YES" instead of Boolean).
  - fix: Correct key names/types.

## ATS.B NSAppTransportSecurity (Info.plist key)

**Source text (verbatim):**
> A description of changes made to the default security for HTTP connections.
>
> On Apple platforms, a networking feature called App Transport Security (ATS) improves privacy and data integrity for all apps and app extensions. ATS requires that all HTTP connections made with the URL Loading System—typically using the URLSession class—use HTTPS. It further imposes extended security checks that supplement the default server trust evaluation prescribed by the Transport Layer Security (TLS) protocol. ATS blocks connections that fail to meet minimum security specifications. For additional details, see Preventing Insecure Network Connections.
>
> You can circumvent or augment these protections by adding the NSAppTransportSecurity key to your app’s Information Property List file and providing an ATS configuration dictionary as the value. For example, you can:
> - Allow insecure loads for web views while maintaining ATS protections elsewhere in your app using the NSAllowsArbitraryLoadsInWebContent key.
> - Enable additional security features like Certificate Transparency using the NSRequiresCertificateTransparency key, or Certificate Pinning using the NSPinnedDomains key.
> - Reduce or remove security requirements for communication with particular servers using the NSExceptionDomains key.
>
> Important: Always look for ways to improve server security before adding ATS exceptions. Loosening ATS restrictions reduces the security of your app.
>
> All keys in the ATS configuration dictionary are optional, with default values that are suitable for most apps. Keys that define global exceptions apply to all network connections made by your app, except connections to domains specified in the NSExceptionDomains sub-dictionary. That sub-dictionary allows you to separately manage settings for individual domains.
>
> **Versioning**
>
> ATS operates by default for apps linked against the iOS 9.0 or macOS 10.11 SDKs or later. When you link your app against an older SDK, ATS is disabled no matter which version of operating system your app runs on.
>
> If you specify a value for any of the global exceptions besides NSAllowsArbitraryLoads, then the ATS behavior depends on the version of the OS on which your app runs:
> - iOS 9.0 or macOS 10.11: ATS uses the NSAllowsArbitraryLoads value that you set, or NO by default, and ignores the other global exceptions.
> - iOS 10.0 or later or macOS 10.12 or later: ATS ignores the NSAllowsArbitraryLoads value that you set and instead obeys the other key or keys.
>
> This behavior enables you to manage differences between OS versions. You provide a coarse exception (NSAllowsArbitraryLoads) for older versions, and a more targeted exception, like NSAllowsArbitraryLoadsInWebContent, for when it’s available.
>
> | Topic | Key | Description |
> |---|---|---|
> | Global Exceptions | NSAllowsArbitraryLoads | A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections. |
> | Global Exceptions | NSAllowsArbitraryLoadsForMedia | A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made using the AV Foundation framework. |
> | Global Exceptions | NSAllowsArbitraryLoadsInWebContent | A Boolean value indicating whether all App Transport Security restrictions are disabled for requests made from web views. |
> | Global Exceptions | NSAllowsLocalNetworking | A Boolean value that indicates whether to allow local resources to load. |
> | Domain-Specific Exceptions | NSExceptionDomains | Custom App Transport Security (ATS) configurations for named domains. |
> | Certificate Pinning | NSPinnedDomains | A collection of certificates that App Transport Security expects when connecting to named domains. |
> | TLS Functionality Package Compliance | NSRequiresNIAPTLSPackageVersion | A string that indicates the version to use for the NIAP Functional Package for TLS. |
> | TLS Functionality Package Compliance | NSExceptionRequiresNIAPTLSPackageVersion | A string that indicates the version to use for the NIAP Functional Package for TLS, applied to an exception domain. |

**Applies to:** Apps that include an NSAppTransportSecurity dictionary.

**Status:** Informational — key-name/type checks for this dictionary are TECH-88 (ATS.A); exception checks are TECH-84, TECH-85, TECH-89, TECH-125.

## ATS.C NSAllowsArbitraryLoads

**Source text (verbatim):**
> A Boolean value indicating whether App Transport Security restrictions are disabled for all network connections.
>
> [Editor: Attributes —] Default: NO
>
> Set this key’s value to YES to disable App Transport Security (ATS) restrictions for all domains not specified in the NSExceptionDomains dictionary. Domains you specify in that dictionary aren’t affected by this key’s value.
>
> Important: You must supply a justification during App Store review if you set the key’s value to YES, as described in Provide Justification for Exceptions. Use this key with caution because it significantly reduces the security of your app. In most cases, it’s better to upgrade your servers to meet the requirements imposed by ATS, or at least to use a narrower exception.
>
> Disabling ATS means that unsecured HTTP connections are allowed. HTTPS connections are also allowed, and are still subject to default server trust evaluation, as described in Ensure the Network Server Meets Minimum Requirements. However, extended security checks—like requiring a minimum Transport Layer Security (TLS) protocol version—are disabled. Without ATS, you’re also free to loosen the default server trust requirements, as described in Performing manual server trust authentication.
>
> In iOS 10 and later and macOS 10.12 and later, the value of the NSAllowsArbitraryLoads key is ignored—and the default value of NO used instead—if any of the following keys are present in your app’s Information Property List file:
> - NSAllowsArbitraryLoadsForMedia
> - NSAllowsArbitraryLoadsInWebContent
> - NSAllowsLocalNetworking
>
> For more information about how the OS version affects ATS behavior, see the NSAppTransportSecurity key’s Versioning section.

**Applies to:** Apps that set NSAllowsArbitraryLoads.

- **[TECH-89]** If NSAllowsArbitraryLoads is YES alongside NSAllowsArbitraryLoadsForMedia, NSAllowsArbitraryLoadsInWebContent or NSAllowsLocalNetworking, has the developer accounted for it being ignored on iOS 10+/macOS 10.12+?
  - quote: "In iOS 10 and later and macOS 10.12 and later, the value of the NSAllowsArbitraryLoads key is ignored—and the default value of NO used instead—if any of the following keys are present in your app’s Information Property List file:"
  - surface: code
  - verify: Parse NSAppTransportSecurity; if NSAllowsArbitraryLoads=YES and any of the three keys is present, report that the global exception is ignored on iOS 10+ (and that it still needs justification per TECH-84).
  - fix: Remove NSAllowsArbitraryLoads if the deployment target is iOS 10+/macOS 10.12+, keeping only the narrower keys.

## ATS.D NSExceptionDomains

**Source text (verbatim):**
> Custom App Transport Security (ATS) configurations for named domains.
>
> The value for this key is a dictionary with keys that name specific domains, IP addresses, or IP address ranges for which you want to set exceptions. The value for each domain key is another dictionary that indicates the exceptions for that domain.
>
> Follow these rules when setting a domain name string:
> - Use lowercase — Use example.com, not EXAMPLE.COM.
> - Use a DNS domain name, IP address, or range of IP addresses — In iOS 17, iPadOS 17, and macOS 14, you can use an IPv4 address, for example 192.168.42.63, or an IPv6 address, for example 2001:db8:12::34. You can also use a classless inter-domain routing (CIDR) range, for example 2001:db8:12::/48. For information about how ATS handles IP addresses, see NSAllowsLocalNetworking.
> - Don’t include a port number — Use example.com, not example.com:443.
> - Don’t include a trailing dot, unless you only want to match a domain string with a trailing dot — For example, example.com. (with a trailing dot) matches “example.com.” but not “example.com”. Similarly, example.com matches “example.com” but not “example.com.”.
> - Don’t use wildcard domains — Don’t use *.example.com. Instead, use example.com and set NSIncludesSubdomains to YES.
>
> Note: If you exclude a DNS domain name and your app contacts a host by IP address, the ATS exclusion for the domain name doesn’t apply to the connection even if a DNS query for the domain name would resolve to the IP address. If you exclude an IP address and your app contacts a host by DNS name that resolves to that IP address, the ATS exclusion for the IP address doesn’t apply to the connection.
>
> The values for the keys in each individual domain’s dictionary control how ATS treats connections made to that domain.
>
> Note: If you specify an exception domain dictionary, ATS ignores any global configuration keys, like NSAllowsArbitraryLoads, for that domain. This is true even if you leave the domain-specific dictionary empty and rely entirely on its keys’ default values.

**Applies to:** Apps whose NSAppTransportSecurity dictionary contains NSExceptionDomains.

- **[TECH-125]** Is every NSExceptionDomains key a lowercase DNS name, IP address or CIDR range, with no port number, no unintended trailing dot, and no wildcard (`*.`)?
  - quote: "Follow these rules when setting a domain name string:"
  - surface: code
  - verify: `plutil -extract NSAppTransportSecurity.NSExceptionDomains xml1 -o - Info.plist`; FAIL on keys containing uppercase letters, `:<port>`, a leading `*.`, or a trailing `.`; IP/CIDR keys apply only on iOS 17, iPadOS 17, macOS 14 and later.
  - fix: Rewrite the domain key (e.g., `example.com` with `NSIncludesSubdomains` = YES instead of `*.example.com`).
- **[TECH-126]** Does each exception domain match how the app actually contacts the host (DNS name vs IP address), given that one does not cover the other?
  - quote: "If you exclude a DNS domain name and your app contacts a host by IP address, the ATS exclusion for the domain name doesn’t apply to the connection even if a DNS query for the domain name would resolve to the IP address."
  - surface: code
  - verify: Compare exception-domain keys with the hosts used in code/config; flag a DNS-name exception for a host the app reaches by IP literal (or the reverse).
  - fix: Add the exception for the form (name or IP) the app actually uses, or connect by the excepted form.

## BG.A Configuring background execution modes / UIBackgroundModes

**Source text (verbatim):**
> UIBackgroundModes — Services provided by an app that require it to run in the background.

Note: Xcode name: Required background modes; type: array of strings. Possible values listed on the key page: audio, bluetooth-central, bluetooth-peripheral, external-accessory, fetch, location, nearby-interaction, network-authentication, newsstand-content, processing, push-to-talk, remote-notification, screen-capture, voip.

>
> To add this key to your Information Property List, enable the Background Modes capability in Xcode. For information on configuring background execution modes and the platforms that support them, see Configuring background execution modes.
>
> **Configuring background execution modes**
>
> Indicate the background services your app requires to continue executing in the background in iOS, iPadOS, tvOS, visionOS, and watchOS.
>
> Typically, an app is in a suspended state when it’s in the background. However, there are a limited number of background execution modes your app can support that enable it to run when in the background, such as playing audio, receiving location updates, or processing scheduled tasks. For apps that adopt one or more of these modes, the system launches or resumes the app, in the background, and affords it time to process any related events.
>
> Use background execution modes sparingly because overuse can negatively impact device performance and battery life. If an alternative to executing in the background exists, use the alternative instead. For example, apps can use the significant-change location service to receive location events as an alternative to using the Location updates background mode.
>
> Before you can select the background execution modes your app requires, follow the steps in Add a capability to add the Background Modes capability to your app’s target.
>
> The background execution modes that appear after you add the capability depend on the target’s platform. For watchOS apps with separate WatchKit extensions, you need to add the capability to the WatchKit Extension target.
>
> Note: The Background Modes capability isn’t available for macOS apps.
>
> **Specify the background modes your app requires**
>
> Before your app can leverage one or more background execution modes, you need to declare the modes it requires by performing the following:
> - 1. Select your project in Xcode’s Project navigator.
> - 2. Select the app’s target in the Targets list.
> - 3. Click the Signing & Capabilities tab in the project editor.
> - 4. Find the Background Modes capability.
> - 5. Select one or more background execution modes using the corresponding checkboxes.
> - 6. For watchOS apps, choose the appropriate session type from the pop-up menu. For more information, see Using extended runtime sessions.
>
> Xcode adds the UIBackgroundModes array to your app’s Info.plist file, if it isn’t already present, and uses the modes you select to populate the array with the necessary values.
>
> Apple’s platforms support these background execution modes:
>
> | Mode | Value | Description | Platforms |
> |---|---|---|---|
> | Audio, AirPlay, and Picture in Picture | audio | The app plays audible content in the background. For more information, see Configuring your app for media playback. | iOS, iPadOS, tvOS, visionOS |
> | Audio | audio | The app plays audible content in the background. For more information, see Playing Background Audio. | watchOS |
> | Location updates | location | The app provides location-based information and requires the use of the platform’s standard location service. For more information, see Configuring your app to use location services. | iOS, iPadOS, watchOS |
> | Voice over IP | voip | The app provides Voice over IP services. For more information, see the CallKit framework. | iOS, iPadOS, visionOS, watchOS |
> | External accessory communication | external-accessory | The app communicates with an accessory that delivers data at regular intervals. For more information, see the External Accessory framework. | iOS, iPadOS |
> | Uses Bluetooth LE accessories | bluetooth-central | The app communicates with a Bluetooth accessory while in the background. For more information, see the Core Bluetooth framework. | iOS, iPadOS, visionOS |
> | Acts as a Bluetooth LE accessory | bluetooth-peripheral | The app uses peripheral mode to communicate with a Bluetooth accessory. For more information, see the Core Bluetooth framework. | iOS, iPadOS |
> | Screen Capture | screen-capture | The app captures and streams screen content while in the background. For more information, see the ScreenCaptureKit framework. | iOS, iPadOS, visionOS |
> | Background fetch | fetch | The app requires new content from the network at regular intervals. For more information, see Using background tasks to update your app. | iOS, iPadOS, tvOS, visionOS |
> | Remote notifications | remote-notification | The app uses push notifications as a signal that new content is available to download. For more information, see Pushing background updates to your App. | iOS, iPadOS, tvOS, visionOS, watchOS |
> | Background processing | processing | The app executes scheduled tasks while in the background. For more information, see BGTaskScheduler. | iOS, iPadOS, tvOS, visionOS |
> | Workout processing | workout-processing | The app uses a workout session to track a user’s activity on Apple Watch. For more information, see Running workout sessions. | watchOS |
> | Uses Nearby Interaction | nearby-interaction | The app locates and interacts with nearby devices. For more information, see the Nearby Interaction framework. | iOS, iPadOS |
> | Push to Talk | push-to-talk | The app launches in response to a push notification and plays audible content in the background. For more information, see the Push to Talk framework. | iOS, iPadOS |

**Applies to:** Apps whose Info.plist contains UIBackgroundModes.

- **[TECH-90]** Is every declared UIBackgroundModes value backed by code that uses that service (per the table's description)?
  - quote: "Use background execution modes sparingly because overuse can negatively impact device performance and battery life."
  - surface: code
  - verify: For each value: `audio` → `AVAudioSession` category `.playback`/`.playAndRecord` with background playback; `location` → `allowsBackgroundLocationUpdates = true` / `CLBackgroundActivitySession`; `voip` → CallKit/PushKit `PKPushRegistry` with `.voIP`; `external-accessory` → `EAAccessoryManager`; `bluetooth-central`/`bluetooth-peripheral` → `CBCentralManager`/`CBPeripheralManager`; `fetch` → `BGAppRefreshTask`/`setMinimumBackgroundFetchInterval`; `remote-notification` → `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` with `content-available`; `processing` → `BGProcessingTaskRequest`; `nearby-interaction` → `NISession`; `push-to-talk` → `PTChannelManager`; `screen-capture` → ScreenCaptureKit. WARN for modes with no matching code. Advisory ("Use background execution modes sparingly" — the source does not say unused modes cause rejection) — report as WARN, not FAIL.
  - fix: Remove unused modes from Signing & Capabilities → Background Modes.
- **[TECH-91]** Where an alternative to background execution exists (e.g., significant-change location instead of the `location` mode), is the alternative used?
  - quote: "If an alternative to executing in the background exists, use the alternative instead."
  - surface: code
  - verify: If `location` mode is declared, check whether the feature only needs coarse/periodic updates (`startMonitoringSignificantLocationChanges` would suffice). Ask the developer to justify continuous background location. Advisory ("If an alternative ... exists") — report as WARN, not FAIL.
  - fix: Switch to the alternative API and drop the mode.
- **[TECH-92]** Is each declared background mode valid for the target's platform (and UIBackgroundModes not relied on for macOS apps)?
  - quote: "The Background Modes capability isn’t available for macOS apps."
  - surface: code
  - verify: Compare each value with the Platforms column (e.g., `workout-processing` watchOS only; `push-to-talk`/`nearby-interaction` iOS/iPadOS only); check macOS targets.
  - fix: Remove modes not supported on the target platform.

## ICON.A HIG App icons — Layer design, icon formats, icon shape

**Source text (verbatim):**
> A unique, memorable icon expresses your app’s or game’s purpose and personality and helps people recognize it at a glance.
>
> Your app icon is a crucial aspect of your app’s or game’s branding and user experience. It appears on the Home Screen and in key locations throughout the system, including search results, notifications, system settings, and share sheets. A well-designed app icon conveys your app’s or game’s identity clearly and consistently across all Apple platforms.
>
> **Layer design**
>
> Although you can provide a nonlayered image for your icon (see Icon formats), layers give you the most control over how your icon design is represented. A layered app icon comes together to produce a sense of depth and vitality. On each platform, the system applies visual effects that respond to the environment and people’s interactions.
>
> iOS, iPadOS, macOS, and watchOS app icons include a background layer and one or more foreground layers that coalesce to create dimensionality. These icons take on Liquid Glass attributes like specular highlights, refraction, and translucency. These effects automatically adapt with the size of your icon, apply consistently across platforms, and can appear differently between system versions.
>
> tvOS app icons use between two and five layers to create a sense of dynamism as people bring them into focus. When focused, the app icon elevates to the foreground in response to someone’s finger movement on their remote, and gently sways while the surface illuminates. The separation between layers and the use of transparency produce a feeling of depth during the parallax effect.
>
> A visionOS app icon includes a background layer and one or two layers on top, producing a three-dimensional object that subtly expands when people view it. The system enhances the icon’s visual dimensionality by adding shadows that convey a sense of depth between layers and by using the alpha channel of the upper layers to create an embossed appearance.
>
> You use your favorite design tool to craft the individual foreground layers of your app icon. For iOS, iPadOS, macOS, and watchOS icons, you then import your icon layers into Icon Composer, a design tool included with Xcode and available from the Apple Developer website. In Icon Composer, you define the background layer for your icon, adjust your foreground layer placement, apply visual effects like specular highlights and refraction, annotate for default, dark, and mono appearance variants, test and preview your icon across system versions, and export your icon for use in Xcode. For additional guidance, see Creating your app icon using Icon Composer.
>
> For tvOS and visionOS app icons, you add your icon layers directly to an image stack in Xcode to form your complete icon. You can download Parallax Previewer and Parallax Exporter plug-in from Apple Design Resources to preview and test parallax visual effects. For developer guidance, see Configuring your app icon using an asset catalog.
>
> Prefer clearly defined edges in foreground layers. To ensure system-drawn highlights and shadows look best, avoid soft and feathered edges on foreground layer shapes.
>
> Vary opacity in foreground layers to increase the sense of depth and liveliness. For example, the Photos icon separates its centerpiece into multiple layers that contain translucent pieces, bringing greater dynamism to the design. Importing fully opaque layers and adjusting transparency in Icon Composer lets you preview and make adjustments to your design based on how transparency and system effects impact one another.
>
> Design a background that both stands out and emphasizes foreground content. If you choose a gradient for your background layer, ensure that it responds well to system lighting effects. Icon Composer supports solid colors and gradients for background layers, making it unnecessary to import custom background images in most cases. If you do import a background layer, make sure it’s full-bleed and opaque.
>
> Prefer vector graphics when bringing layers into Icon Composer. Unlike raster images, vector graphics (such as SVG or PDF) scale gracefully and appear crisp at any size. Outline artwork and convert text to outline in your design. For mesh gradients and raster artwork, prefer PNG format because it’s a lossless image format.
>
> **Icon formats**
>
> In iOS, iPadOS, macOS, and watchOS, you can provide icons in one of two formats: nonlayered bitmap images (such as PNG) or layered Icon Composer files. The Icon Composer format lets you control how Liquid Glass applies to individual elements of your icon, and how color applies across appearance variants.
>
> Provide your icon in the Icon Composer format for more flexibility and control. If you provide a bitmap image instead, the system attempts to segment your icon, isolating the foreground elements from the background to create an icon with two layers. These two layers help make your icon compatible with dark and tinted appearance variants, ensuring the use of a consistent background.
>
> When the system segments your icon, it applies Liquid Glass effects to foreground layers that feature large, simple shapes. It doesn’t automatically apply Liquid Glass effects to smaller, more complex elements in an icon like text and thin lines. To control precisely which elements receive Liquid Glass properties, supply your icon as a layered Icon Composer file.
>
> **Icon shape**
>
> An app icon’s shape varies based on a platform’s visual language. In iOS, iPadOS, and macOS, icons are square, and the system applies masking to produce rounded corners that precisely match the curvature of other rounded interface elements throughout the system and the bezel of the physical device itself. In tvOS, icons are rectangular, also with concentric edges. In visionOS and watchOS, icons are square and the system applies circular masking.
>
> Produce appropriately shaped, unmasked layers. The system masks all layer edges to produce an icon’s final shape. For iOS, iPadOS, and macOS icons, provide square layers so the system can apply rounded corners. For visionOS and watchOS, provide square layers so the system can create the circular icon shape. For tvOS, provide rectangular layers so the system can apply rounded corners. Providing layers with pre-defined masking negatively impacts specular highlight effects and makes edges look jagged.
>
> Keep primary content centered to avoid truncation when the system adjusts corners or applies masking. Pay particular attention to centering content in visionOS and watchOS icons. To help with icon placement, use the grids in the app icon production templates, which you can find in Apple Design Resources.

**Applies to:** All apps (app icon).

- **[TECH-93]** Are icon images/layers square (rectangular for tvOS) and unmasked — no pre-rounded corners or circular masks baked in?
  - quote: "Providing layers with pre-defined masking negatively impacts specular highlight effects and makes edges look jagged."
  - surface: code
  - verify: Open `AppIcon.appiconset/*.png` (or `.icon` layer files); with Python/PIL check width == height (tvOS: per spec) and that corner pixels are not transparent (alpha at (0,0),(w-1,0),(0,h-1),(w-1,h-1) should be 255 for the opaque full-bleed background). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Re-export unmasked square artwork; let the system apply masking.
- **[TECH-94]** If a background layer image is imported, is it full-bleed and opaque?
  - quote: "If you do import a background layer, make sure it’s full-bleed and opaque."
  - surface: code
  - verify: For the background layer image (Icon Composer bundle or tvOS/visionOS image stack "Back" layer), check every pixel's alpha is 255. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Flatten the background onto an opaque fill.

## ICON.B HIG App icons — Design, visual effects, appearances

**Source text (verbatim):**
> **Design**
>
> Embrace simplicity in your icon design. Simple icons tend to be easiest for people to understand and recognize. An icon with fine visual features might look busy when rendered with system-provided shadows and highlights, and details may be hard to discern at smaller sizes. Find a concept or element that captures the essence of your app or game, make it the core idea of your icon, and express it in a simple, unique way with a minimal number of shapes. Prefer a simple background, such as a solid color or gradient, that puts the emphasis on your primary design — you don’t need to fill the entire icon canvas with content.
>
> Provide a visually consistent icon design across all the platforms your app supports. A consistent design helps people quickly find your app wherever it appears and prevents people from mistaking your app for multiple apps.
>
> Consider basing your icon design around filled, overlapping shapes. Overlapping solid shapes in the foreground, particularly when paired with transparency and blurring, can give an icon a sense of depth.
>
> Include text only when it’s essential to your experience or brand. Text in icons doesn’t support accessibility or localization, is often too small to read easily, and can make an icon appear cluttered. In some contexts, your app name already appears nearby, making it redundant to display the name within the icon itself. Although displaying a mnemonic like the first letter of your app’s name can help people recognize your app or game, avoid including nonessential words that tell people what to do with it — like “Watch” or “Play” — or context-specific terms like “New” or “For visionOS.” If you include text in a tvOS app icon, make sure it’s above other layers so it’s not cropped by the parallax effect.
>
> Prefer illustrations to photos and avoid replicating UI components. Photos are full of details that don’t work well when displayed in different appearances, viewed at small sizes, or split into layers. Instead of using photos, create a graphic representation of the content that emphasizes the features you want people to notice. Make sure to avoid extremely thin line weights and sharp corners, because they tend to lose detail and crispness in smaller icon sizes at lower resolutions. If your app has an interface that people recognize, don’t just replicate standard UI components or use app screenshots in your icon.
>
> Don’t use replicas of Apple hardware products. Apple products are copyrighted and can’t be reproduced in your app icons.
>
> **Visual effects**
>
> Let the system handle blurring and other visual effects. The system dynamically applies visual effects to your app icon layers, so there’s no need to include specular highlights, drop shadows between layers, beveled edges, blurs, glows, and other effects. In addition to interfering with system-provided effects, custom effects are static, whereas the system supplies dynamic ones. If you do include custom visual effects on your icon layers, use them intentionally and test carefully with Icon Composer, on a simulated device in Device Hub, or on a physical device to make sure they appear as expected and don’t conflict with system effects.
>
> Create layer groupings to apply effects to multiple layers at once. System effects typically occur on individual layers. If it makes sense for your design, however, you can group several layers together in Icon Composer or your design tool so effects occur at the group level. For a group, Icon Composer provides additional customization options for Liquid Glass effects, so you can configure attributes like specular highlights, refraction, and translucency.
>
> **Appearances**
>
> In iOS, iPadOS, and macOS, people can choose whether their Home Screen app icons are default, dark, clear, or tinted in appearance. For example, someone may want to personalize their app icon appearance to complement their wallpaper. You can design app icon variants for every appearance variant, and the system automatically generates variants you don’t provide.
>
> Keep your icon’s features consistent across appearances. To create a seamless experience, keep your icon’s core visual features the same in the default, dark, clear, and tinted appearances. Avoid creating custom icon variants that swap elements in and out with each variant, which may make it harder for people to find your app when they switch appearances.
>
> Design dark and tinted icons that feel at home beside system app icons and widgets. You can preserve the color palette of your default icon, but be mindful that dark icons are more subdued, and clear and tinted icons are even more so. A great app icon is visible, legible, and recognizable, regardless of its appearance variant.
>
> Use your light app icon as the basis for your dark icon. Choose complementary colors that reflect the default design, and avoid excessively bright images. Color backgrounds generally offer the greatest contrast in dark icons. For guidance, see Dark Mode.
>
> Consider offering alternate app icons. In iOS, iPadOS, tvOS, and compatible apps running in visionOS, it’s possible to let people visit your app’s settings to choose an alternate version of your app icon. For example, a sports app might offer icons for different teams, letting someone choose their favorite. If you offer this capability, make sure each icon you design remains closely related to your content and experience. Avoid creating one someone might mistake for another app.
>
> Note: Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants. As with your default app icon, all alternate and variant icons are subject to app review and must adhere to the App Review Guidelines.

**Applies to:** All apps (app icon); alternate icons where offered.

- **[TECH-95]** Does the icon avoid replicas of Apple hardware products?
  - quote: "Don’t use replicas of Apple hardware products."
  - surface: manual
  - verify: View the icon at 1024px (and all variants/alternate icons); FAIL if it depicts an iPhone, iPad, Mac, Apple Watch, AirPods, etc.
  - fix: Redesign the icon without Apple hardware imagery.
- **[TECH-96]** Does the icon avoid app screenshots/replicated standard UI components, and include text only when essential (no words like “Watch”, “Play”, “New”, “For visionOS”)?
  - quote: "If your app has an interface that people recognize, don’t just replicate standard UI components or use app screenshots in your icon."
  - surface: manual
  - verify: Inspect the icon art visually (and OCR for text); flag screenshots, UI chrome, and nonessential words. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Replace with a simple graphic representation.
- **[TECH-97]** If the app offers alternate icons on iOS/iPadOS, does each alternate have its own dark, clear, and tinted variants, and is each closely related to the app's content?
  - quote: "Alternate app icons in iOS and iPadOS require their own dark, clear, and tinted variants."
  - surface: code
  - verify: Grep `setAlternateIconName`; read `CFBundleAlternateIcons`/`ASSETCATALOG_COMPILER_ALTERNATE_APPICON_NAMES`; for each alternate icon set (or `.icon` file) confirm dark/tinted (and clear) appearances are provided.
  - fix: Add the missing appearance variants (Icon Composer or asset catalog appearances).
- **[TECH-98]** Is the core design consistent across default, dark, clear and tinted appearances (no swapped elements)?
  - quote: "Avoid creating custom icon variants that swap elements in and out with each variant, which may make it harder for people to find your app when they switch appearances."
  - surface: manual
  - verify: Compare the provided appearance images side by side (or preview in Icon Composer). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Keep the same core elements in every variant.

## ICON.C HIG App icons — Platform considerations and specifications

**Source text (verbatim):**
> **Platform considerations**
>
> No additional considerations for iOS, iPadOS, or macOS.
>
> **tvOS**
>
> Include a safe zone to ensure the system doesn’t crop your content. When someone focuses your app icon, the system may crop content around the edges as the icon scales and moves. To ensure that your icon’s content is always visible, keep a safe zone around it. Be aware that the safe zone can vary, depending on the image size, layer depth, and motion, and the system crops foreground layers more than background layers.
>
> **visionOS**
>
> Avoid adding a shape that’s intended to look like a hole or concave area to the background layer. The system-added shadow and specular highlights can make such a shape stand out instead of recede.
>
> **watchOS**
>
> Avoid using black for your icon’s background. Lighten a black background so the icon doesn’t blend into the display background.
>
> **Specifications**
>
> The layout, size, style, and appearances of app icons vary by platform.
>
> | Platform | Layout shape | Icon shape after system masking | Layout size | Style | Appearances |
> |---|---|---|---|---|---|
> | iOS, iPadOS, macOS | Square | Rounded rectangle (square) | 1024x1024 px | Layered | Default, dark, clear light, clear dark, tinted light, tinted dark |
> | tvOS | Rectangle (landscape) | Rounded rectangle (rectangular) | 800x480 px | Layered (Parallax) | N/A |
> | visionOS | Square | Circular | 1024x1024 px | Layered (3D) | N/A |
> | watchOS | Square | Circular | 1088x1088 px | Layered | N/A |
>
> The system automatically scales your icon to produce smaller variants that appear in certain locations, such as Settings and notifications.
>
> App icons support the following color spaces:
> - sRGB (color)
> - Gray Gamma 2.2 (grayscale)
> - Display P3 (wide-gamut color in iOS, iPadOS, macOS, tvOS, and watchOS only)

**Applies to:** All apps (per platform).

- **[TECH-99]** Does the icon source match the platform layout size (iOS/iPadOS/macOS 1024x1024 px, tvOS 800x480 px, visionOS 1024x1024 px, watchOS 1088x1088 px) and use a supported color space (sRGB, Gray Gamma 2.2, or Display P3 except visionOS)?
  - quote: "The layout, size, style, and appearances of app icons vary by platform."
  - surface: code
  - verify: `sips -g pixelWidth -g pixelHeight -g space <file>` on each icon PNG (or Icon Composer canvas size); compare with the table; FAIL on other color profiles (e.g., CMYK, Adobe RGB) or Display P3 on visionOS.
  - fix: Re-export at the specified size in a supported color space.
- **[TECH-100]** For watchOS, does the icon avoid a black background?
  - quote: "Avoid using black for your icon’s background."
  - surface: code
  - verify: Sample the watchOS icon background pixels; WARN if near #000000.
  - fix: Lighten the background.

## ICON.D Configuring your app icon using an asset catalog

**Source text (verbatim):**
> Add app icon variations to an asset catalog that represents your app in places such as the App Store, the Home Screen, Settings, and search results.
>
> Important: To create your app icon using Icon Composer for all variants, including different platforms and appearances, see Creating your app icon using Icon Composer.
>
> Every app has a distinct app icon that communicates the app’s purpose and makes it easy to recognize throughout the system. Apps require multiple variations of the app icon to look great in different contexts. Xcode can help generate these variations for you using a single high-resolution image, or you can configure your app icon variations by using an app icon’s image set in your project’s asset catalog. visionOS and tvOS app icons are made up of multiple stacked image layers you configure in your project’s asset catalog. iOS and iPadOS app icons support additional dark and tinted styles.
>
> **Create an app icon**
>
> When you create your project from a template, it automatically includes a default asset catalog (Assets.xcassets) that contains the AppIcon. If you don’t have a default asset catalog or existing AppIcon or you want to provide an alternate, you can add an app icon to an asset catalog manually:
> - 1. In the Project navigator, select an asset catalog.
> - 2. Click the Add button (+) at the bottom of the outline view.
> - 3. In the pop-up menu, choose OS variant > OS variant App Icon. Xcode creates a new app icon set or image stack with the name AppIcon.
>
> **Specify app icon variations**
>
> Variations of your app icon appear throughout the system in places like the Home View, Settings, and search results:
> - iOS, iPadOS, tvOS, and watchOS apps can auto-generate all icon variations from a single 1024×1024 pixel image. This is the default behavior when you create a new iOS, iPadOS, tvOS, and watchOS app, or a new icon in the asset catalog. If you have an existing project that provides multiple variants, consider providing a single size when that is all your icon requires. However, if you want to customize your app’s icon variants, such as to show more detail at a larger size, you can provide individual assets for the variations.
> - For macOS and tvOS, you need to supply an asset for each size.
> - For visionOS, you need to supply a single 1024x1024 pixel asset.
>
> **Add dark and tinted icon variants to iOS and iPadOS**
>
> iOS and iPadOS support three stylistic variations for app icons: Light, Dark, and Tinted. You can create your own variations to ensure that each one looks exactly the way you way you want.
>
> After you select the Appearance from the pop-up menu, two image wells appear. Drag your dark and tinted app icons into the appropriate image well. Provide your tinted app icon as a grayscale image. Provide your dark app icon with a transparent background so the system-provided background can show through.
>
> If you prefer, you can take advantage of the system’s automatically generated treatment that is applied to all app icons. It is crafted intelligently to preserve design intent and maintain legibility. This also helps maintain a consistent visual experience across the Home Screen.
>
> **Configure the layers of an image stack**
>
> By default, visionOS and tvOS app icons are constructed with three layers. This is the maximum number of layers visionOS icons support but you can use up to five layers when constructing tvOS icons. To add a layer, Click the Add button, choose OS variant > OS variant App Icon Layer. To remove a layer, select the layer and click the Remove button (-).
>
> **Specify an App Store icon**
>
> If you distribute your app through the App Store, you must provide app icon imagery to use in the App Store. In the Project navigator, select an asset catalog and add icon images to the appropriate image wells in an app icon set or image stack. The App Store image well location varies by platform.
>
> | Platform | App Store icon location |
> |---|---|
> | iOS | Drag an icon image to the iOS 1,024pt image well. |
> | iMessage | For the iOS target, drag an icon image to the iOS 1,024pt image well in the AppIcon set. For the iMessage Extension target, drag an icon to the Messages App Store image well in the iMessage App Icon set. |
> | Sticker Pack | Drag an icon image to the iOS 1,024pt image well and the Messages App Store image well. |
> | macOS | Drag an icon image to the App Store - 2x image well. |
> | tvOS | Drag images to the image wells for the layers of your App Icon - App Store stack in the App Icon & Top Shelf Image folder. The App Store generates an icon from the layers of the image stack. |
> | visionOS | Drag images to the image wells for the layers of your visionOS App Icon stack. The App Store generates an icon from the layers of the image stack. |
> | watchOS | For the iOS target, drag an icon image to the iOS 1,024pt image well. For the WatchKit App target, drag an icon image to the watchOS image well. |

**Applies to:** Apps distributed through the App Store using an asset-catalog icon.

- **[TECH-101]** Is App Store icon imagery provided in the platform's App Store image well (e.g., iOS 1,024pt well; macOS App Store - 2x; tvOS App Store stack layers)?
  - quote: "If you distribute your app through the App Store, you must provide app icon imagery to use in the App Store."
  - surface: code
  - verify: Read `Assets.xcassets/AppIcon.appiconset/Contents.json` (or `.solidimagestack`/`.brandassets` for tvOS/visionOS); confirm the 1024 / `ios-marketing` / macOS `512x512@2x` entry has a `filename` and the file exists; confirm `ASSETCATALOG_COMPILER_APPICON_NAME` points to it (or an `.icon` Icon Composer file is in the target).
  - fix: Add the missing App Store image(s).
- **[TECH-102]** For macOS and tvOS asset-catalog icons, is an asset supplied for each size (visionOS: a single 1024x1024 asset)?
  - quote: "For macOS and tvOS, you need to supply an asset for each size."
  - surface: code
  - verify: Parse `Contents.json` for macOS/tvOS icon sets; FAIL if any `images` entry lacks `filename`.
  - fix: Supply all sizes.
- **[TECH-103]** If custom iOS/iPadOS dark and tinted variants are provided, is the tinted icon grayscale and the dark icon on a transparent background?
  - quote: "Provide your tinted app icon as a grayscale image. Provide your dark app icon with a transparent background so the system-provided background can show through."
  - surface: code
  - verify: In `Contents.json` find entries with `appearances` `luminosity: dark` / `luminosity: tinted`; check the tinted PNG is grayscale (R=G=B) and the dark PNG has transparent background pixels.
  - fix: Re-export variants accordingly (or remove them to use the system treatment).
- **[TECH-104]** Does a visionOS icon stack use at most three layers and a tvOS stack at most five?
  - quote: "This is the maximum number of layers visionOS icons support but you can use up to five layers when constructing tvOS icons."
  - surface: code
  - verify: Count layer folders in the `.solidimagestack`/`.imagestack` directories.
  - fix: Merge layers to fit the limit.

## ICON.E Creating your app icon using Icon Composer — Overview

**Source text (verbatim):**
> Use Icon Composer to create a single multilayer file that you can add to your Xcode project to represent your Liquid Glass app icon everywhere your app icon appears across iOS, iPadOS, macOS, watchOS, and the App Store. Use your favorite design tool to create the artwork for your app icon, but save some design decisions for Icon Composer, where you can refine the dynamic properties of Liquid Glass and customize variants of your app icon for different platforms and appearances.
>
> Before building your app, add the Icon Composer file to your Xcode project to include it in your app’s bundle. The system automatically renders your app icon for the different platforms, appearances, and sizes from your single Icon Composer file. If your app supports previous releases (in the Minimum Deployments settings in the target’s General pane) that don’t have the same icon and widget style appearances and Liquid Glass material, Xcode automatically generates app icon images at build time for those releases from the Icon Composer file.
>
> Important: If you add an Icon Composer file to your Xcode project, it replaces any existing icon asset catalog that you previously used to represent your app icon. Xcode automatically generates a similar-looking version of the Liquid Glass icon for previous releases. If you want your existing icon to appear in previous releases, continue to use asset catalogs to represent your app icon.

**Applies to:** iOS, iPadOS, macOS, watchOS apps using an Icon Composer (`.icon`) file.

- **[TECH-105]** If an Icon Composer `.icon` file is used, is it included in the app target (so it ships in the bundle), and is the developer aware it replaces the asset-catalog icon?
  - quote: "Before building your app, add the Icon Composer file to your Xcode project to include it in your app’s bundle."
  - surface: code
  - verify: Find `*.icon` in the project; check `project.pbxproj` lists it in the app target's resources and `ASSETCATALOG_COMPILER_APPICON_NAME` matches its name. If both `.icon` and `AppIcon.appiconset` exist, report which one is used.
  - fix: Add the `.icon` file to the target membership and set the App Icon name.

## LAUNCH.A HIG Launching

**Source text (verbatim):**
> A streamlined launch experience helps people start using your app or game immediately.
>
> Launching begins when someone opens your app or game, includes an initial download, and ends when the first screen is ready. After launching completes, you might offer an onboarding experience, which can give people a high-level view of your app or game.
>
> **Best practices**
>
> Launch instantly. People want to start interacting with your app or game right away, and sometimes they don’t want to wait more than a couple of seconds.
>
> If the platform requires it, provide a launch screen. In iOS, iPadOS, and tvOS, the system displays your launch screen the moment your app or game starts and quickly replaces it with your first screen, giving people the impression that your experience is fast and responsive. For guidance, see Launch screens. macOS, visionOS, and watchOS don’t require launch screens.
>
> If you need a splash screen, consider displaying it at the beginning of your onboarding flow. A splash screen is a beautiful graphic that succinctly communicates branding and other information you need to provide. If you don’t provide an onboarding experience, you might display your splash screen as soon as launching completes.
>
> Restore the previous state when your app restarts so people can continue where they left off. Avoid making people retrace steps to reach their previous location in your app or game. Restore granular details of the previous state as much as possible. For example, scroll the view to people’s most recent position, and display windows in the same state and location in which people left them.
>
> **Launch screens**
>
> Not applicable for macOS, visionOS, or watchOS.
>
> Downplay the launch experience. A launch screen isn’t part of an onboarding experience or a splash screen, and it isn’t an opportunity for artistic expression. A launch screen’s sole function is to enhance the perception of your experience as quick to launch and immediately ready to use.
>
> Design a launch screen that’s nearly identical to the first screen of your app or game. If you include elements that look different when launching completes, people may experience an unpleasant flash between the launch screen and your first screen. If your app or game displays a solid color before transitioning to the first screen, create a launch screen that displays only that solid color. Also make sure that your launch screen matches the device’s current orientation and appearance mode.
>
> Avoid including text on your launch screen, even if your first screen displays text. Because the content in a launch screen doesn’t change, any text you display won’t be localized.
>
> Don’t advertise. The launch screen isn’t a branding opportunity. Avoid creating a screen that looks like a splash screen or an “About” window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen.
>
> **Platform considerations**
>
> No additional considerations for macOS or watchOS.
>
> **iOS, iPadOS**
>
> Launch in the appropriate orientation. If your app or game supports both portrait and landscape modes, launch using the device’s current orientation. If your interface only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only interface responds correctly, regardless of whether people enter landscape orientation by rotating the device left or right. For guidance, see Layout.
>
> **tvOS**
>
> Note: Unlike the layered images throughout much of a tvOS app, the launch screen is static.
>
> In a live-viewing app, consider automatically starting playback soon after people start the app. People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see Live-viewing apps.
>
> **visionOS**
>
> Consider launching in the Shared Space even if your app is fully immersive. Opening a window in the Shared Space lets you provide more context about your app or game while giving it time to load, and it also lets you present a control that people can use to open your fully immersive experience. In general, people appreciate being able to choose when to transition to a Full Space, especially if they’re currently running other apps in the Shared Space. For guidance, see Immersive experiences.

**Applies to:** iOS, iPadOS, tvOS apps (launch screens); all apps (launch speed, state restoration).

- **[TECH-106]** Does the launch screen avoid text?
  - quote: "Avoid including text on your launch screen, even if your first screen displays text."
  - surface: code
  - verify: Open the launch storyboard XML and grep for `<label`, `<textView`, `text=`; for `UILaunchScreen`, check `UIImageName` artwork for text (manual). Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Remove text from the launch screen.
- **[TECH-107]** Does the launch screen avoid advertising/branding (logos only if they are a fixed part of the first screen) and look nearly identical to the first screen?
  - quote: "don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen."
  - surface: runtime
  - verify: Launch the app on a simulator with slow animations or record video (`xcrun simctl io booted recordVideo`); compare the launch frame with the first screen; check light and dark appearance. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Replace the launch screen with a background color/simplified first-screen layout.
- **[TECH-108]** Does the app launch in the device's current orientation (or its single supported orientation), and does a landscape-only UI handle both landscape-left and landscape-right?
  - quote: "Ensure a landscape-only interface responds correctly, regardless of whether people enter landscape orientation by rotating the device left or right."
  - surface: code
  - verify: Read `UISupportedInterfaceOrientations` / `UISupportedInterfaceOrientations~ipad`; if landscape-only, confirm both `UIInterfaceOrientationLandscapeLeft` and `UIInterfaceOrientationLandscapeRight` are listed. Runtime: launch rotated each way. Advisory (HIG guidance) — report as WARN, not FAIL.
  - fix: Add both landscape orientations.

## LAUNCH.B Specifying your app’s launch screen

**Source text (verbatim):**
> Make your iOS app launch experience faster and more responsive by customizing a launch screen.
>
> Every iOS app must provide a launch screen, a screen that displays while your app launches. The launch screen appears instantly when your app starts up and is quickly replaced with the app’s first screen.
>
> You create a launch screen for your app in your Xcode project in one of two ways:
> - Information property list
> - User interface file
>
> To make the app launch experience as seamless as possible, create a launch screen with basic views that closely resemble the first screen of your app.
>
> **Configure a launch screen in an information property list**
>
> For apps with simple user interfaces, using the information property list in your app provides a quick and straightforward method to configure your launch screen.
> - 1. In the settings for your target, select the Info tab.
> - 2. In the Custom iOS Target Properties section, expand the Launch Screen key.
> - 3. Click the Add button (+), type in UILaunchScreen, and press Return to add the launch screen key to the property list. If the UILaunchScreen key is already present, you can skip this step.
> - 4. Select the UILaunchScreen key, click the Add button, and add additional keys to specify configuration options for your launch screen.
>
> Define the appearance of the launch screen by specifying a combination of launch screen options from the possible keys in UILaunchScreen.
>
> **Configure a launch screen storyboard**
>
> Alternatively, you can configure your launch screen in a user interface file, a file with a .storyboard file extension. A launch screen storyboard contains basic UIKit views, and uses size classes and Auto Layout constraints to support different device sizes and resolutions.
>
> Follow these guidelines when creating a launch screen storyboard:
> - Use only UIKit classes.
> - Use a single root view that’s a UIView or UIViewController object.
> - Don’t make any connections to your code, for example, don’t add actions or outlets.
> - Don’t use deprecated views such as UIWebView.
> - Don’t use any custom classes.
> - Don’t use runtime attributes.
>
> If you create your iOS app from a storyboard template, Xcode adds a default launch screen file, called LaunchScreen.storyboard, to your project. Edit LaunchScreen.storyboard to configure your launch screen.
>
> If your project doesn’t contain a default launch screen file, add a launch screen file and set the launch screen file for the target in the project editor.
> - 1. Choose File > New > File from Template.
> - 2. Under User Interface, select Launch Screen, and click Next.
> - 3. Give the launch screen file a name, choose a location, select the target that you want to add the file to, and click Create.
> - 4. In the settings for your target, select the General tab and find the “App Icons and Launch Screen” section.
> - 5. From the Launch Screen File pop-up menu, choose the new launch screen file.

**Applies to:** All iOS apps.

- **[TECH-109]** Does the iOS app provide a launch screen via `UILaunchScreen` (or `UILaunchScreens`) or a launch screen storyboard (`UILaunchStoryboardName`)?
  - quote: "Every iOS app must provide a launch screen, a screen that displays while your app launches."
  - surface: code
  - verify: Check the target's Info.plist and build settings (`INFOPLIST_KEY_UILaunchScreen_Generation`, `INFOPLIST_KEY_UILaunchStoryboardName`) for one of the keys; if `UILaunchStoryboardName` is set, confirm `<name>.storyboard` exists in the target.
  - fix: Add `UILaunchScreen` (e.g., with `UIColorName`) or a LaunchScreen.storyboard and set it as the Launch Screen File.
- **[TECH-110]** Does the launch storyboard use only UIKit classes, a single root view, no outlets/actions, no custom classes, no runtime attributes, and no deprecated views such as UIWebView?
  - quote: "Don’t use deprecated views such as UIWebView."
  - surface: code
  - verify: Parse the launch `.storyboard` XML: FAIL on `customClass=`, `<connections>` with `outlet`/`action`, `<userDefinedRuntimeAttributes>`, `<webView`, or more than one root scene/view.
  - fix: Simplify the storyboard to plain UIKit views without connections.

## LAUNCH.C UILaunchScreen and UILaunchStoryboardName (Info.plist keys)

**Source text (verbatim):**
> UILaunchScreen — The user interface to show while an app launches.

Note: Xcode name: Launch Screen; type: dictionary.

>
> You use this key to define the launch screen that the system displays while your app launches. If you need to provide different launch screens in response to being launched by different URL schemes, use UILaunchScreens instead.
>
> Note: Use this key to configure the user interface during app launch in a way that doesn’t rely on storyboards. If you prefer to use storyboards, use UILaunchStoryboardName instead.
>
> | Topic | Key | Description |
> |---|---|---|
> | Main Interface | UIColorName | The name of a color to use as the background color on the launch screen. |
> | Main Interface | UIImageName | The name of an image to display during app launch. |
> | Main Interface | UIImageRespectsSafeAreaInsets | A Boolean that specifies whether the launch image should respect the safe area insets. |
> | Border Elements | UINavigationBar | Navigation bar visibility and configuration during launch. |
> | Border Elements | UITabBar | Tab bar visibility and configuration during launch. |
> | Border Elements | UIToolbar | Toolbar visibility and configuration during launch. |
>
> UILaunchStoryboardName — The filename of the storyboard from which to generate the app’s launch image.

Note: Xcode name: Launch screen interface file base name; type: string.

>
> Specify the name of the storyboard file without the filename extension. For example, if the filename of your storyboard is LaunchScreen.storyboard, specify “LaunchScreen” as the value for this key.
>
> If you prefer to configure your app’s launch screen without storyboards, use UILaunchScreen instead.

**Applies to:** iOS apps configuring their launch screen with these keys.

- **[TECH-111]** Is `UILaunchStoryboardName` set to the storyboard name without the file extension, and do `UILaunchScreen` `UIColorName`/`UIImageName` values refer to assets that exist?
  - quote: "Specify the name of the storyboard file without the filename extension."
  - surface: code
  - verify: FAIL if the value ends in `.storyboard`; for `UILaunchScreen`, confirm a color set named `UIColorName` and an image set named `UIImageName` exist in an asset catalog in the target.
  - fix: Correct the value / add the missing asset.

## PERM.L Export compliance keys (ITSAppUsesNonExemptEncryption, ITSEncryptionExportComplianceCode)

**Source text (verbatim):**
> ITSAppUsesNonExemptEncryption — A Boolean value indicating whether the app uses encryption.
>
> Set the value for this key to NO in your app’s Information Property List file to indicate that your app—including any third-party libraries you link against—either uses no encryption, or only uses encryption that’s exempt from export compliance requirements, as described in Overview of export compliance. Set the value to YES to indicate that your app uses non-exempt encryption.
>
> If you set the value to YES, you typically also provide a value for the ITSEncryptionExportComplianceCode key. You set that key’s value using a code Apple provides after successfully reviewing your export compliance documentation.
>
> If you don’t have the ITSAppUsesNonExemptEncryption key in your app’s Info.plist file, App Store Connect walks you through an export compliance questionnaire every time you upload a new version of your app. Including the key streamlines the app submission process.
>
> ITSEncryptionExportComplianceCode — The export compliance code provided by App Store Connect for apps that require it.
>
> Include this key in your app’s Information Property List file if you set the ITSAppUsesNonExemptEncryption key’s value to YES. Set the value for this key to the code that Apple sends you after successfully reviewing export compliance documentation that you provide through App Store Connect.

**Applies to:** All apps uploaded to App Store Connect.

- **[TECH-112]** Is ITSAppUsesNonExemptEncryption present in Info.plist with a value that reflects the app's (and its libraries') encryption use?
  - quote: "If you don’t have the ITSAppUsesNonExemptEncryption key in your app’s Info.plist file, App Store Connect walks you through an export compliance questionnaire every time you upload a new version of your app."
  - surface: code
  - verify: `plutil -extract ITSAppUsesNonExemptEncryption raw Info.plist` (or `INFOPLIST_KEY_ITSAppUsesNonExemptEncryption`). If missing, WARN. If NO, ask the developer to confirm no non-exempt encryption (including third-party libraries) is used.
  - fix: Add the key with the correct Boolean (developer decision on exemption status).
- **[TECH-113]** If ITSAppUsesNonExemptEncryption is YES, is ITSEncryptionExportComplianceCode set to the code Apple provided?
  - quote: "Include this key in your app’s Information Property List file if you set the ITSAppUsesNonExemptEncryption key’s value to YES."
  - surface: code
  - verify: If the first key is YES, check for a non-empty ITSEncryptionExportComplianceCode; cross-check in App Store Connect → App Information / build's export compliance status.
  - fix: Add the code from App Store Connect (manual — requires export compliance documentation approval).

## Sources

| URL | Page title |
|---|---|
| https://developer.apple.com/support/offering-account-deletion-in-your-app/ → https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion | 5.1.1(v) - Offering account deletion in your app - Guideline reference - App Review - Help - Apple Developer |
| https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings | 5.1.1(ii) - Write clear purpose strings |
| https://developer.apple.com/design/human-interface-guidelines/managing-accounts | Managing accounts |
| https://developer.apple.com/sign-in-with-apple/ → https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple | Sign in with Apple (HIG) |
| https://developer.apple.com/documentation/signinwithapple | Sign in with Apple |
| https://developer.apple.com/documentation/signinwithapplerestapi/revoke-tokens | Token revocation |
| https://developer.apple.com/documentation/signinwithapple/processing-changes-for-sign-in-with-apple-accounts | Processing changes for Sign in with Apple accounts |
| https://developer.apple.com/documentation/bundleresources/protected-resources | Protected resources |
| https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources | Requesting access to protected resources |
| https://developer.apple.com/documentation/bundleresources/choosing-the-location-services-authorization-to-request | Choosing the  Location Services Authorization to Request |
| https://developer.apple.com/documentation/avfoundation/requesting-authorization-to-capture-and-save-media | Requesting authorization to capture and save media |
| https://developer.apple.com/design/human-interface-guidelines/privacy | Privacy |
| https://developer.apple.com/documentation/security/preventing-insecure-network-connections | Preventing Insecure Network Connections |
| https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity | NSAppTransportSecurity |
| https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsallowsarbitraryloads | NSAllowsArbitraryLoads |
| https://developer.apple.com/documentation/bundleresources/information-property-list/nsapptransportsecurity/nsexceptiondomains | NSExceptionDomains |
| https://developer.apple.com/documentation/bundleresources/information-property-list/uibackgroundmodes | UIBackgroundModes |
| https://developer.apple.com/documentation/xcode/configuring-background-execution-modes | Configuring background execution modes |
| https://developer.apple.com/documentation/bundleresources/information-property-list/bgtaskschedulerpermittedidentifiers | BGTaskSchedulerPermittedIdentifiers (fetched; abstract only, no checks derived) |
| https://developer.apple.com/design/human-interface-guidelines/app-icons | App icons |
| https://developer.apple.com/documentation/xcode/configuring-your-app-icon | Configuring your app icon using an asset catalog |
| https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer | Creating your app icon using Icon Composer |
| https://developer.apple.com/design/human-interface-guidelines/launching | Launching |
| https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen | Specifying your app’s launch screen |
| https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreen | UILaunchScreen |
| https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchstoryboardname | UILaunchStoryboardName |
| https://developer.apple.com/documentation/bundleresources/information-property-list/<key> for each of the 69 keys in PERM.A | Each key's page (title = key name): ITSAppUsesNonExemptEncryption, ITSEncryptionExportComplianceCode, NFCReaderUsageDescription, NSAccessoryTrackingUsageDescription, NSAppBundlesUsageDescription, NSAppDataUsageDescription, NSAppleEventsUsageDescription, NSAppleMusicUsageDescription, NSAppleScriptEnabled, NSAudioCaptureUsageDescription, NSBluetoothAlwaysUsageDescription, NSBluetoothPeripheralUsageDescription, NSCalendarsFullAccessUsageDescription, NSCalendarsUsageDescription, NSCalendarsWriteOnlyAccessUsageDescription, NSCameraUsageDescription, NSContactsUsageDescription, NSCriticalMessagingUsageDescription, NSDesktopFolderUsageDescription, NSDocumentsFolderUsageDescription, NSDownloadsFolderUsageDescription, NSEnterpriseMCAMUsageDescription, NSFaceIDUsageDescription, NSFallDetectionUsageDescription, NSFileProviderDomainUsageDescription, NSFileProviderPresenceUsageDescription, NSFinancialDataUsageDescription, NSGKFriendListUsageDescription, NSHandsTrackingUsageDescription, NSHealthClinicalHealthRecordsShareUsageDescription, NSHealthRequiredReadAuthorizationTypeIdentifiers, NSHealthShareUsageDescription, NSHealthUpdateUsageDescription, NSHomeKitUsageDescription, NSIdentityUsageDescription, NSIdentityUsageDescriptionDictionary, NSLocalNetworkUsageDescription, NSLocationAlwaysAndWhenInUseUsageDescription, NSLocationAlwaysUsageDescription, NSLocationDefaultAccuracyReduced, NSLocationTemporaryUsageDescriptionDictionary, NSLocationUsageDescription, NSLocationWhenInUseUsageDescription, NSMainCameraUsageDescription, NSMicrophoneUsageDescription, NSMotionUsageDescription, NSNearbyInteractionAllowOnceUsageDescription, NSNearbyInteractionUsageDescription, NSNetworkVolumesUsageDescription, NSPhotoLibraryAddUsageDescription, NSPhotoLibraryUsageDescription, NSRemindersFullAccessUsageDescription, NSRemindersUsageDescription, NSRemovableVolumesUsageDescription, NSSensorKitPrivacyPolicyURL, NSSensorKitUsageDescription, NSSensorKitUsageDetail, NSSiriUsageDescription, NSSpeechRecognitionUsageDescription, NSSystemAdministrationUsageDescription, NSSystemExtensionUsageDescription, NSUpdateSecurityPolicy, NSUserTrackingMarkdownUsageDescription, NSUserTrackingUsageDescription, NSVideoSubscriberAccountUsageDescription, NSWidgetWantsLocation, NSWorldSensingUsageDescription, OSBundleUsageDescription, UIRequiresPersistentWiFi |
