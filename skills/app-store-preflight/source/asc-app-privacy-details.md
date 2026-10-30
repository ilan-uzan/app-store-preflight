=== SOURCE: https://developer.apple.com/app-store/app-privacy-details/
Watch the latest videos about privacy  

# App privacy details on the App Store

The App Store helps people better understand an app’s privacy practices before they download the app on any Apple platform. On each app’s product page, users can learn about some of the data types the app may collect, and whether that data is linked to them or used to track them. You’ll need to provide information about your app’s privacy practices, including the practices of third-party partners whose code you integrate into your app, in App Store Connect. This information is required to submit new apps and app updates to the App Store.

## What’s new

An important part of submitting your app to the App Store is explaining how your app handles user data. Two new updates make it easier to accurately provide Privacy Nutrition Labels and improve the integrity of the software supply chain: signatures for third-party SDKs and privacy manifests. In addition, we’re adding more data type options to use in your Privacy Nutrition Label when describing what types of data your app collects.

- Read more

- Watch the latest videos

## Answering app privacy questions

As you get ready to select your answers from the options presented in App Store Connect, keep in mind:

- You need to identify all of the data you or your third-party partners collect, unless the data meets all of the criteria for optional disclosure listed below.

- Your app’s privacy practices should follow the App Review Guidelines and all applicable laws.

- You’re responsible for keeping your responses accurate and up to date. If your practices change, update your responses in App Store Connect. You may update your answers at any time, and you do not need to submit an app update in order to change your answers.

Account Holders, Admins, and App Managers can learn how to enter their responses in App Store Connect.

## Data collection

The purpose of the label is to help your customers understand what data is collected from your app and how it is used. To complete that, you’ll need to know the types of data that you and/or your third-party partners collect from your app before answering the questions in App Store Connect. Keep in mind that even if you collect the data for reasons other than analytics or advertising, it still needs to be declared. For example, if you collect data solely for the purpose of app functionality, declare the data on your label and indicate that it is only being used for that purpose.

“Collect” refers to transmitting data off the device in a way that allows you and/or your third-party partners to access it for a period longer than what is necessary to service the transmitted request in real time.

“Third-party partners” refers to analytics tools, advertising networks, third-party SDKs, or other external vendors whose code you’ve added to your app.

## Optional disclosure

Data types that meet all of the following criteria are optional to disclose:

- The data is not used for tracking purposes, meaning the data is not linked with Third-Party Data for advertising or advertising measurement purposes, or shared with a data broker. For details, see the Tracking section.

- The data is not used for Third-Party Advertising, your Advertising or Marketing purposes, or for Other Purposes, as those terms are defined in the Tracking section.

- Collection of the data occurs only in infrequent cases that are not part of your app’s primary functionality, and which are optional for the user.

- The data is provided by the user in your app’s interface, it is clear to the user what data is collected, the user’s name or account name is prominently displayed in the submission form alongside the other data elements being submitted, and the user affirmatively chooses to provide the data for collection each time.

Data types must meet all criteria in order to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in App Store Connect.

Examples of data that may not need to be disclosed include data collected in optional feedback forms or customer service requests that are unrelated to the primary purpose of the app and meet the other criteria above.

For the purpose of clarity, data collected on an ongoing basis after an initial request for permission must be disclosed.

#### Product Improvement Programs

Data types that meet all of the following criteria are optional to disclose:

- Data collected is only used for the purpose of improving your app and its services.

- Collection of the data is optional and only occurs if the user explicitly opts in through a choice presented directly within the user interface — where the user is given two clear options: one to share the data and one to not share the data.

- The user’s choice does not impact any features or functionality of the app, or their cost. 

- Users can update their choice at any time through an easily accessible setting. 

- The data is not linked to the user’s identity (via their account, device, or other details).

- The data is not used for tracking purposes, meaning the data is not linked with Third-Party Data for advertising or advertising measurement purposes, or shared with a data broker. For details, see the Tracking section.

- The data is not used for Third-Party Advertising, your Advertising or Marketing purposes, Product Personalization, or Other Purposes.

Data types must meet all the criteria to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

#### Regulated Financial Services Disclosure

Data types that are collected by an app that facilitates regulated financial services and where the data collected meets all of the following criteria are optional to disclose:

- Collection of the regulated data is in accordance with a legally required privacy notice under applicable financial services or data protection laws or regulations (e.g., GDPR or GLBA).

- Collection by the app of that data occurs only in cases that are not part of your app’s primary functionality, and which are optional for the user.

- Such notice provides that data is not shared with unaffiliated third parties to market other products and services.

- Such data is not linked with third-party data for advertising purposes or shared with a data broker except for purposes of fraud detection or prevention or security purposes, or with a consumer reporting agency for credit reporting.

Data types must meet all criteria in order to be considered optional for disclosure. If a data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

#### Health Research Disclosure

Data types that are collected as part of a health research study and where the data collected meets all of the following criteria are optional to disclose:

- The data is collected by an entity whose collection of the data is subject to an informed consent form (ICF) as part of a health research study that has been reviewed and approved by an institutional review board or ethics review board.

- All such data collection must follow the relevant App Review Guidelines and the data may not be used for tracking purposes.

If the data type collected by your app meets some, but not all, of the above criteria, it must be disclosed in your privacy section.

## Types of data

Refer to the list of data types below and compare them to the data collection practices in your app.

Contact Info   
Name Such as first or last name  
Email Address Including but not limited to a hashed email address  
Phone Number Including but not limited to a hashed phone number  
Physical Address Such as home address, physical address, or mailing address  
Other User Contact Info Any other information that can be used to contact the user outside the app  
Health & Fitness   
Health Health and medical data, including but not limited to data from the Clinical Health Records API, HealthKit API, Movement Disorder API, or health-related human subject research or any other user provided health or medical data  
Fitness Fitness and exercise data, including but not limited to the Motion and Fitness API  
Financial Info   
Payment Info Such as form of payment, payment card number, or bank account number. If your app uses a payment service, the payment information is entered outside your app, and you as the developer never have access to the payment information, it is not collected and does not need to be disclosed.  
Credit Info Such as credit score  
Other Financial Info Such as salary, income, assets, debts, or any other financial information  
Location   
Precise Location Information that describes the location of a user or device with the same or greater resolution as a latitude and longitude with three or more decimal places  
Coarse Location Information that describes the location of a user or device with lower resolution than a latitude and longitude with three or more decimal places, such as Approximate Location Services  
Sensitive Info   
Sensitive Info Such as racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data  
Contacts   
Contacts Such as a list of contacts in the user’s phone, address book, or social graph  
User Content   
Emails or Text Messages Including subject line, sender, recipients, and contents of the email or message  
Photos or Videos The user’s photos or videos  
Audio Data The user’s voice or sound recordings  
Gameplay Content Such as saved games, multiplayer matching or gameplay logic, or user-generated content in-game  
Customer Support Data generated by the user during a customer support request  
Other User Content Any other user-generated content  
Browsing History   
Browsing History Information about content the user has viewed that is not part of the app, such as websites  
Search History   
Search History Information about searches performed in the app  
Identifiers   
User ID Such as screen name, handle, account ID, assigned user ID, customer number, or other user- or account-level ID that can be used to identify a particular user or account  
Device ID Such as the device’s advertising identifier, or other device-level ID  
Purchases   
Purchase History An account’s or individual’s purchases or purchase tendencies  
Usage Data   
Product Interaction Such as app launches, taps, clicks, scrolling information, music listening data, video views, saved place in a game, video, or song, or other information about how the user interacts with the app  
Advertising Data Such as information about the advertisements the user has seen  
Other Usage Data Any other data about user activity in the app  
Diagnostics   
Crash Data Such as crash logs  
Performance Data Such as launch time, hang rate, or energy use  
Other Diagnostic Data Any other data collected for the purposes of measuring technical diagnostics related to the app  
Surroundings   
Environment Scanning Such as mesh, planes, scene classification, and/or image detection of the user’s surroundings  
Body   
Hands The user’s hand structure and hand movements  
Head The user’s head movement  
Other Data   
Other Data Types Any other data types not mentioned    

## Data use

You should have a clear understanding of how each data type is used by you and your third-party partners.

For example, collecting an email address and using it to authenticate the user and personalize the user’s experience within your app would include App Functionality and Product Personalization.

Purpose Definition  
Third-Party Advertising Such as displaying third-party ads in your app, or sharing data with entities who display third-party ads  
Developer’s Advertising or Marketing Such as displaying first-party ads in your app, sending marketing communications directly to your users, or sharing data with entities who will display your ads  
Analytics Using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics  
Product Personalization Customizing what the user sees, such as a list of recommended products, posts, or suggestions  
App Functionality Such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support  
Other Purposes Any other purposes not listed    

## Data linked to the user

You’ll need to identify whether each data type is linked to the user’s identity (via their account, device, or other details) by you and/or your third-party partners. Data collected from an app is often linked to the user’s identity, unless specific privacy protections are put in place before collection to de-identify or anonymize it, such as:

- Stripping data of any direct identifiers, such as user ID or name, before collection.

- Manipulating data to break the linkage and prevent re-linkage to real-world identities.

Additionally, in order for data not to be linked to a particular user’s identity, you must avoid certain activities after collection:

- You must not attempt to link the data back to the user’s identity.

- You must not tie the data to other datasets that enable it to be linked to a particular user’s identity.

Note: “Personal Information” and “Personal Data”, as defined under relevant privacy laws, are considered linked to the user.

## Tracking

You’ll need to understand whether you and/or your third-party partners use data from your app to track users and, if so, which data is used for this purpose.

“Tracking” refers to linking data collected from your app about a particular end-user or device, such as a user ID, device ID, or profile, with Third-Party Data for targeted advertising or advertising measurement purposes, or sharing data collected from your app about a particular end-user or device with a data broker.

“Third-Party Data” refers to any data about a particular end-user or device collected from apps, websites, or offline properties not owned by you.

Examples of tracking include:

- Displaying targeted advertisements in your app based on user data collected from apps and websites owned by other companies.

- Sharing device location data or email lists with a data broker.

- Sharing a list of emails, advertising IDs, or other IDs with a third-party advertising network that uses that information to retarget those users in other developers’ apps or to find similar users.

- Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes. For example, using a login SDK that repurposes the data it collects from your app to enable targeted advertising in other developers’ apps.

The following situations are not considered tracking:

- When the data is linked solely on the end-user’s device and is not sent off the device in a way that can identify the end-user or device.

- When the data broker uses the data shared with them solely for fraud detection or prevention or security purposes.

- When the data broker is a consumer reporting agency and the data is shared with them for purposes of (1) reporting on a consumer’s creditworthiness or (2) obtaining information on a consumer’s creditworthiness for the specific purpose of making a credit determination.

Learn more about tracking.

## Privacy links

By adding the following links on your product page, you can help users easily access your app’s privacy policy and manage their data in your app.

Privacy Policy (Required): The URL to your publicly accessible privacy policy.

Privacy Choices (Optional): A publicly accessible URL where users can learn more about their privacy choices for your app and how to manage them. For example, a webpage where users can access their data, request deletion, or make changes.

## Additional guidance

#### Your app has web views.

Data collected via web traffic must be declared, unless you are enabling the user to navigate the open web.

#### You collect and store IP address from your users.

Declare the relevant data types based on how you use IP address, such as precise location, coarse location, device ID, or diagnostics.

#### You offer in-app private messaging between users that are not SMS text messages.

Declare emails or text messages on your label. Text messages refer to both SMS and non-SMS messages.

#### Your app includes game saves, multiplayer matching, or gameplay logic.

Declare Gameplay Content on your label.

#### You collect different types of data from users depending on whether the user is a child, whether they are a free or paid user, whether they opt in, where they live, or for some other reason. 

Please disclose all data collected from your app, unless it meets all of the criteria outlined in the Optional Disclosure section. You may use the Privacy Choices or Privacy Policy links to provide additional detail about how your data collection practices may vary.

#### You use Apple frameworks or services, such as MapKit, CloudKit, or App Analytics.

If you collect data about your app from Apple frameworks or services, you should indicate what data you collect and how you use it. You are not responsible for disclosing data collected by Apple.

#### You use location, device identifiers, and other sensitive data, but only on device, and the data is never sent to a server.

Data that is processed only on device is not “collected” and does not need to be disclosed in your answers. If you derive anything from that data and send it off device, the resulting data should be considered separately.

#### You collect precise location, but immediately de-identify and coarsen it before storing.

Disclose that you collect Coarse Location, since the precise location data is immediately coarsened and precise location is not stored.

#### Your app includes free-form text fields or voice recordings, and users can save any type of information they want through those mediums, including names and health data.

Mark "Other User Content" to represent generic free form text fields and "Audio Data" for voice recordings. You’re not responsible for disclosing all possible data that users may manually enter in the app through free-form fields or voice recordings. However, if you ask a user to input a specific data type into a text field, such as their name or email, or if you have a feature that enables users to upload a particular media type, such as photos or videos, then you’ll need to disclose the specific type of data.

#### You collect data to service a request but do not retain it after servicing the request.

"Collect" refers to transmitting data off the device and storing it in a readable form for longer than the time it takes you and/or your third-party partners to service the request. For example, if an authentication token or IP address is sent on a server call and not retained, or if data is sent to your servers then immediately discarded after servicing the request, you do not need to disclose this in your answers in App Store Connect.

#### You’d like your app to reference consent requests so you can comply with local privacy laws in its App Tracking Transparency prompt.

If you’ve already shown the user a required government data-privacy consent prompt that is also covered by App Tracking Transparency (for example, through a third-party Consent Management Platform), you can reference that in your app’s App Tracking Transparency purpose string. Here’s an example of a purpose string that clearly explains the user’s choice:

“[App] indicates you allowed it to use your data for advertising purposes in its legal prompt. Would you like your Apple device to provide [App] access to the advertising ID or otherwise allow it to use other means for the data processing described above?”

=== SOURCE: https://developer.apple.com/documentation/apptrackingtransparency
App Tracking Transparency | Apple Developer Documentation                              

# This page requires JavaScript.

Please turn on JavaScript in your browser and refresh the page to view its content.

## Automated tools and assistive tools:

A Markdown version of the page content is available: View Markdown

=== SOURCE: https://developer.apple.comdoc://com.apple.adsupport/documentation/AdSupport/ASIdentifierManager/advertisingIdentifier
# advertisingIdentifier

The UUID that is specific to a device.

iOS 6.0, iPadOS 6.0, Mac Catalyst 13.1, macOS 10.14, tvOS 6.0

### Discussion

The advertisingIdentifier is an alphanumeric string that’s unique to each device, and which you only use for advertising. Use this string for frequency capping, attribution, conversion events, estimating the number of unique users, advertising fraud detection, and debugging. On devices running iOS 14.5 and later and iPadOS 14.5 and later, your app must request tracking authorization before it can get the advertising identifier. For more information on getting the advertising identifier, see AdSupport.

The advertising identifier returns either a unique UUID, or all zeros. It returns a unique UUID in the following cases:

- If Settings > Privacy > Tracking > Allow Apps to Request to Track is On, you’ve requested tracking authorization from the user by calling the App Tracking Transparency APIs, and received authorization, indicated by ATTrackingManager.AuthorizationStatus.authorized.

- If the user changes Settings > Privacy > Tracking > Allow Apps to Request to Track to Off after authorizing your app, and leaves the permissions On for your app.

The advertising identifier returns all zeros (00000000-0000-0000-0000-000000000000) in the following cases:

- In Simulator, regardless of any settings.

- When you call this API on a device running macOS.

- When you call this API in a compatible iPad or iPhone app running in visionOS.

- On devices running iOS 14.5 and later and iPadOS 14.5 and later, if you haven’t requested authorization using the App Tracking Transparency framework.

- If you’ve requested authorization using the App Tracking Transparency framework and the user declines, which results in an authorization status of ATTrackingManager.AuthorizationStatus.denied.

- When a profile or configuration restricts access to the advertising identifier. For more information about restrictions, see ATTrackingManager.AuthorizationStatus.restricted.

As a best practice, don’t store the advertising identifier value; access advertisingIdentifier instead. Users can change their authorization for tracking at any time in Settings > Privacy > Tracking. Check your app’s authorization using the App Tracking Transparency API doc://com.apple.documentation/documentation/apptrackingtransparency/attrackingmanager/3547038-trackingauthorizationstatus to determine the user’s intent.

For more information about asking users for permission to track, see User Privacy and Data Use.

## Getting the Advertising Identifier

- shared(): The shared instance of the identifier manager class.

=== SOURCE: https://developer.apple.comdoc://com.apple.apptrackingtransparency/documentation/AppTrackingTransparency/ATTrackingManager/AuthorizationStatus
# ATTrackingManager.AuthorizationStatus

A type that represents the tracking-authorization status of an app.

iOS 14.0, iPadOS 14.0, Mac Catalyst 14.0, macOS 11.0, tvOS 14.0, visionOS 1.0

### Overview

trackingAuthorizationStatus returns this type, and requestTrackingAuthorization(completionHandler:) passes an instance of this type to your completion handler when a person answers the system alert.

## Determining the status

- ATTrackingManager.AuthorizationStatus.authorized: A value that indicates someone grants your app permission to access data your app can use to track a person or device.

- ATTrackingManager.AuthorizationStatus.denied: A value that indicates someone denies your app permission to access data your app can use to track a person or device.

- ATTrackingManager.AuthorizationStatus.notDetermined: A value that indicates the person hasn’t responded to a tracking authorization request.

- ATTrackingManager.AuthorizationStatus.restricted: A value that indicates the system restricts tracking authorization.

## Creating a status

- init(rawValue:): Initializes an authorization status.

## Authorization status and results

- trackingAuthorizationStatus: A value that indicates the status of the app’s tracking authorization.

=== SOURCE: https://developer.apple.comdoc://com.apple.apptrackingtransparency/documentation/AppTrackingTransparency/ATTrackingManager/requestTrackingAuthorization(completionHandler:)
# requestTrackingAuthorization(completionHandler:)

Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

iOS 14.0, iPadOS 14.0, Mac Catalyst 14.0, macOS 11.0, tvOS 14.0, visionOS 1.0

### Discussion

This method requests authorization to access app-related data that the app can use to track the person or the device. In France, Germany, Italy, Poland, and Romania, the system presents a full-page sheet; otherwise, the system prompts the person with an alert.

### Handle the person’s response

When the person answers the prompt, the system calls the completion handler with a status object (ATTrackingManager.AuthorizationStatus) set to ATTrackingManager.AuthorizationStatus.authorized or ATTrackingManager.AuthorizationStatus.denied, depending on the person’s response.

The status is ATTrackingManager.AuthorizationStatus.notDetermined if the system dismisses the prompt without a decision from the person; in this scenario, your app needs to call the method again to receive an authorization answer from the person.

In some cases, the system doesn’t display the prompt and instead runs your completion handler immediately. The system doesn’t prompt the person when:

- Tracking is restricted for the device; in this case, the trackingAuthorizationStatus is ATTrackingManager.AuthorizationStatus.restricted regardless of whether the system has shown the person the prompt.

- The person disables “Allow Apps to Request to Track” (called “Allow Apps to Request to Link Your Activity Across Companies” in the European Union) in Settings > Privacy & Security > Tracking.

- An existing permission request is pending.

- Your code invokes this method through an app extension.

- The app’s state is a value other than UIApplicationStateActive.

### Prompt again after a year

In the European Union, if a person answers the prompt, the system notes the date and doesn’t allow the prompt to display again until a year passes. You can make an additional request after a year whether the person approves or denies your app’s previous tracking request, unless the person disables tracking in Settings > Privacy & Security > Tracking.

### Configure the app’s target properties

To use this method, add the NSUserTrackingUsageDescription key to your app’s target properties in Xcode.

In France, Germany, Italy, Poland, and Romania, the full-page sheet displays the NSUserTrackingMarkdownUsageDescription string with support for rich-text elements if you include it in your app’s target configuration in Xcode.

## Authorization requests

- requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:): Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

=== SOURCE: https://developer.apple.comdoc://com.apple.apptrackingtransparency/documentation/AppTrackingTransparency/ATTrackingManager/requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)
# requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)

Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

iOS 27.2, iPadOS 27.2, Mac Catalyst 27.2

### Discussion

This method requests authorization to access app-related data that the app can use to track the person or the device. The method augments the regular authorization request flow (see requestTrackingAuthorization(completionHandler:)) by adding functionality to the modal UI with the option of requesting a full-page sheet, Markdown-formatted text, and an optional Additional Information button.

### Display a full-page sheet

The functionality this method adds to the authorization process is available regionally, and requires the device to be located in a specific European Union country and signed in with an Apple Account with a specific EU country or region:

France, Germany, Italy, Poland, and Romania: The system displays markdown text you supply via NSUserTrackingMarkdownUsageDescription in a full-page sheet regardless of what you set for preferExpandedInterface, and includes an Additional Information button if you supply an action.

The European Union: The system displays markdown text in the NSUserTrackingMarkdownUsageDescription, if you supply it. The system displays the full-page sheet if you set preferExpandedInterface to true, and includes an Additional Information button if you supply an action.

Outside of the European Union, the system doesn’t use either parameter, and presents a system alert displaying the original NSUserTrackingUsageDescription, which is equivalent to calling requestTrackingAuthorization(completionHandler:).

### Handle the person’s response

When the person answers the prompt, the system calls the argument completion handler with a status object (ATTrackingManager.AuthorizationStatus) set to ATTrackingManager.AuthorizationStatus.authorized or ATTrackingManager.AuthorizationStatus.denied, depending on the person’s response.

The status is ATTrackingManager.AuthorizationStatus.notDetermined if the system dismisses the prompt without a decision from the person; in this case, your app needs to call this method again to receive an authorization answer from the person.

In some cases, the system doesn’t display the prompt and instead runs your completion handler immediately. The system doesn’t prompt the person when:

- Tracking is restricted for the device; in this case, the trackingAuthorizationStatus is ATTrackingManager.AuthorizationStatus.restricted regardless of whether the system has shown the person the prompt.

- The person disables “Allow Apps to Request to Track” (called “Allow Apps to Request to Link Your Activity Across Companies” in the European Union) in Settings > Privacy & Security > Tracking.

- An existing permission request is pending.

- Your code invokes this method through an app extension.

- The app’s state is a value other than UIApplicationStateActive.

### Provide additional information

If someone taps Additional Information, the sheet dismisses without recording an answer, and your additionalInformationAction closure runs. In your closure, present your own custom UI that provides more information to assist people in their decision making. Then call this method again to ask for permission once more.

The completion handler still runs after an Additional Information button tap, receiving ATTrackingManager.AuthorizationStatus.notDetermined, since the person hasn’t yet made a decision.

### Prompt again after a year

In the European Union, if a person answers the prompt, the system notes the date and doesn’t allow the prompt to display again until a year passes. You can make an additional request after a year whether the person approves or denies your app’s previous tracking request, unless the person disables tracking in Settings > Privacy & Security > Tracking.

### Configure the app’s target properties

To use this method, add the NSUserTrackingUsageDescription key to your app’s target properties in Xcode.

[Important]

Important: In the European Union, if your app’s target properties in Xcode also include NSUserTrackingMarkdownUsageDescription, the full-page sheet uses that string instead, with support for bold text, italic text, bullet lists, and paragraph breaks.

## Authorization requests

- requestTrackingAuthorization(completionHandler:): Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

=== SOURCE: https://developer.apple.comdoc://com.apple.apptrackingtransparency/documentation/AppTrackingTransparency/ATTrackingManager/trackingAuthorizationStatus
# trackingAuthorizationStatus

A value that indicates the status of the app’s tracking authorization.

iOS 14.0, iPadOS 14.0, Mac Catalyst 14.0, macOS 11.0, tvOS 14.0, visionOS 1.0

### Discussion

Check this property to determine whether your app has permission to access app-related data it can use to track a person or device.

If the status is ATTrackingManager.AuthorizationStatus.notDetermined, call one of the tracking-request methods to present the tracking-authorization prompt and ask the person for permission:

- requestTrackingAuthorization(completionHandler:)

- requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:)

This property returns ATTrackingManager.AuthorizationStatus.restricted when the system restricts tracking for the device, regardless of whether your app has presented the prompt.

## Authorization status and results

- ATTrackingManager.AuthorizationStatus: A type that represents the tracking-authorization status of an app.

=== SOURCE: https://developer.apple.comdoc://com.apple.apptrackingtransparency/documentation/AppTrackingTransparency/ATTrackingManager
# ATTrackingManager

A class that requests tracking authorization and provides the current authorization status.

iOS 14.0, iPadOS 14.0, Mac Catalyst 14.0, macOS 11.0, tvOS 14.0, visionOS 1.0

### Overview

This class presents an authorization request UI that asks a person for permission to access app-related data that your app can use to track a person or device across apps and websites (see requestTrackingAuthorization(completionHandler:)). You can check the result of prior requests with the trackingAuthorizationStatus property.

[Important]

Important: In the European Union, you can use requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:) to add an optional Additional Information button to the prompt, which provides more details to assist people in their decision-making. The authorization Ul is a full-page sheet that supports rich-text formatting.

## Requesting authorization

- requestTrackingAuthorization(completionHandler:): Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

- requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:): Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

## Determining tracking authorization status

- trackingAuthorizationStatus: A value that indicates the status of the app’s tracking authorization.

- ATTrackingManager.AuthorizationStatus: A type that represents the tracking-authorization status of an app.

## Essentials

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

=== SOURCE: https://developer.apple.comdoc://com.apple.apptrackingtransparency/documentation/AppTrackingTransparency
# App Tracking Transparency

Request authorization to access app-related data that your app can use to track the person or the device.

iOS 14.0, iPadOS 14.0, Mac Catalyst 14.0, macOS 11.0, tvOS 14.0, visionOS 1.0

### Overview

Your app needs to use the App Tracking Transparency framework if it collects data about people and shares it with other companies to track them across apps and websites. The framework presents a tracking-authorization UI and reports the current authorization status.

### Request authorization to access app-related data

To use the App Tracking Transparency framework:

1. Add the NSUserTrackingUsageDescription key to your app’s target properties in Xcode.

2. Call requestTrackingAuthorization(completionHandler:) to present the tracking-authorization request.

3. Check trackingAuthorizationStatus to determine the current authorization status; see ATTrackingManager.AuthorizationStatus for the possible values.

For more information about app tracking and privacy, see User Privacy and Data Use and App Privacy Details.

## Essentials

- ATTrackingManager: A class that requests tracking authorization and provides the current authorization status.

- NSUserTrackingUsageDescription: A message that explains the purpose for accessing data that an app can use to track a person or device.

## Authorization requests

- requestTrackingAuthorization(completionHandler:): Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

- requestTrackingAuthorization(preferExpandedInterface:additionalInformationAction:completionHandler:): Presents a modal UI that asks someone for permission to access data that your app can use to track a person or device.

- NSUserTrackingMarkdownUsageDescription: A message that explains the purpose for accessing data that an application can use to track a person or device.

## Authorization status and results

- trackingAuthorizationStatus: A value that indicates the status of the app’s tracking authorization.

- ATTrackingManager.AuthorizationStatus: A type that represents the tracking-authorization status of an app.

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

=== SOURCE: https://developer.apple.comdoc://com.apple.uikit/documentation/UIKit/UIApplication/openSettingsURLString
# openSettingsURLString

The URL string you use to deep link to your app’s custom settings in the Settings app.

iOS 8.0, iPadOS 8.0, Mac Catalyst 13.1, tvOS, visionOS 1.0

### Discussion

Create a URL from this value and pass it to the open(_:options:completionHandler:) method to launch the Settings app and display your app’s custom settings, if it has any.

For design guidance, see Human Interface Guidelines.

## Deep linking to custom settings

- openNotificationSettingsURLString: The URL string you use to deep link to your app’s notification settings in the Settings app.

- openDefaultApplicationsSettingsURLString: The URL string used to select a default app in the Settings app.

=== SOURCE: https://developer.apple.comdoc://com.apple.uikit/documentation/UIKit/UIDevice/identifierForVendor
# identifierForVendor

An alphanumeric string that uniquely identifies a device to the app’s vendor.

iOS 6.0, iPadOS 6.0, Mac Catalyst 13.1, tvOS, visionOS 1.0

### Discussion

The value of this property is the same for apps that come from the same vendor running on the same device. A different value is returned for apps on the same device that come from different vendors, and for apps on different devices regardless of vendor.

Normally, the vendor is determined by data provided by the App Store. If the app wasn’t installed from the app store (such as enterprise apps and apps still in development), then a vendor identifier is calculated based on the app’s bundle ID. The bundle ID is assumed to be in reverse-DNS format.

- In iOS 6, the first two components of the bundle ID are used to generate the vendor ID. If the bundle ID only has a single component, then the entire bundle ID is used.

- In IOS 7, all components of the bundle except for the last component are used to generate the vendor ID. If the bundle ID only has a single component, then the entire bundle ID is used.

The following table shows a collection of bundle IDs and which portions of the bundle ID the system uses to calculate the vendor ID.

| Bundle ID | iOS 6.x | iOS 7.x |

| Com.example.app1 | Com.example.app1 | Com.example.app1 |

| Com.example.app2 | Com.example.app2 | Com.example.app2 |

| Com.example.app.app1 | Com.example.app.app1 | Com.example.app.app1 |

| Com.example.app.app2 | Com.example.app.app2 | Com.example.app.app2 |

| Example | Example | Example |

For example, com.example.app1 and com.example.app2 would appear to have the same vendor ID.

If the value is nil, wait and get the value again later. This happens, for example, after the device has been restarted but before the user has unlocked the device.

The value in this property remains the same while the app (or another app from the same vendor) is installed on the iOS device. The value changes when the user deletes all of that vendor’s apps from the device and subsequently reinstalls one or more of them. The value can also change when installing test builds using Xcode or when installing an app on a device using ad-hoc distribution. Therefore, if your app stores the value of this property anywhere, you should gracefully handle situations where the identifier changes.

## Identifying the device and operating system

- name: The name of the device.

- systemName: The name of the operating system running on the device.

- systemVersion: The current version of the operating system.

- model: The model of the device.

- localizedModel: The model of the device as a localized string.

- userInterfaceIdiom: The style of interface to use on the current device.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/
### App Store Connect Help

App Store Connect / Manage app information / Manage app privacy 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Manage app privacy

You’re required to provide a privacy policy URL for your iOS app platform and privacy policy text for your tvOS app platform. Offering a privacy choices URL is optional. Furthermore, if you're distributing your app on the App Store, you're required to explain your data handling practices in App Store Connect. This informs users about the data that may be collected through your app and how it may be used. 

Your responses to the app privacy questions are used to help inform customers about your app’s data practices. Based on the information you submit, your App Store product page will be updated to include details about the app's data collection and usage.

Responses are provided at the app level and should accurately represent your app's data practices across all platforms. You should answer in the most comprehensive and inclusive way if your app collects more data on one platform than another. You must include information about your app's privacy practices and those of third-party partners whose code you integrate into your app.

Note: You’re responsible for keeping your responses accurate and up to date. If your practices change, update your responses in App Store Connect.

Learn about privacy and data.

Learn about responding to app privacy questions.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Answering app privacy questions

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Privacy.

-  
On the right, click Get Started.

-  
In the dialog that appears, indicate whether you or your third-party partners collect data from your app.

-  
If the answer is no, select "No, we do not collect data from this app" and then click Save. You don’t need to answer any further questions.

-  
If the answer is yes, select "Yes, we collect data from this app" and then click Next.

-  
Select all of the data you or your third-party partners collect from this app and click Save.

If your app is currently available on the App Store, make sure your responses reflect the data collected only from that app version.

-  
In the Data Types section, click each data type and answer the questions that follow. If at any point you want to update your data types, click Edit next to Data Types.

-  
Click Save when finished.

-  
Your responses appear in each data type section. Scroll to the Product Page Preview section to view how this information will appear on the App Store. To view product page details, click See Details.

-  
On the top right of the page, click Publish.

-  
A dialog appears confirming that you agree that your responses are accurate, comply with the App Review Guidelines and applicable law, and that you will promptly update your responses if your data practices change. To agree and continue, click Publish. Your responses will be published on your product page on the App Store. If your product page isn’t live yet, your responses will be published once your product page goes live.

### Adding and removing data types

Updates to data types will be published after you click Publish. If you select new data types, you must complete their setup by responding to the questions in each data type section before publishing.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Privacy.

-  
Next to Data Types, click Edit.

-  
Update your selections for all of the data you or your third-party partners collect from this app.

If your app is currently available on the App Store, ensure that your responses reflect the data collected only from that app version.

-  
If you removed an existing data type, click Publish. Your responses to this data type will be removed from your app’s product page.

-  
If you added a new data type, click Continue, then complete the setup for the newly added data type by clicking into it and responding to the questions that follow. Once completing your responses to the questions, click Publish. Your responses to the newly added data type will appear on your app’s product page after publishing.

-  
If you have added a new data type and removed an existing one, click Publish, then click Continue. Your responses to the removed data type will be removed from your app's product page. You need to complete the setup for the newly added data type by clicking into it and responding to the questions that follow. Once you have finished responding to the questions, click Publish. Your responses to the newly added data type will appear on your app's product page after publishing.

### Updating app privacy responses

-  
In Apps, select the app you want to view.

-  
In the sidebar, select App privacy.

-  
To edit existing responses, on the right, click on the data type you'd like to update your responses for.

-  
Update your responses, then click Publish. Your updated responses will be published on your app’s product page after you click Publish.

Below the Product Page Preview section on the App Store Connect, you can preview how this information about your app's data collection and usage will appear. To view the details of the product page preview, click See Details.

### Entering privacy policy information

In App Store Connect, you can enter privacy policy and user privacy choices URLs for your iOS and macOS app platforms, and privacy policy text for your tvOS app platform. A privacy policy URL is required for all apps, while a user privacy choices URL is optional. The URLs for your iOS app and macOS app platform and the text for your tvOS app platform can be updated if your app is in an editable app status. Learn more about required, localizable, and editable properties.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select App privacy.

-  
Next to Privacy Policy, click Edit.

-  
Enter the privacy policy URL and optionally, the user privacy choices URL. If your app includes a tvOS platform, enter the text of your privacy policy in the Apple TV Privacy Policy field.

Note: You can localize the privacy policy URLs and text in all of the languages your app is available in.

-  
Click Save.

Any changes to the URLs releases with your next app version.

=== SOURCE: https://developer.apple.com/app-store/user-privacy-and-data-use/
# User privacy and data use

At Apple, we believe privacy is a fundamental human right. That’s why we’ve built a number of features to help users understand developers’ privacy and data collection and sharing practices, and put users in the driver’s seat when it comes to their data. With Privacy Nutrition Labels on the App Store and in App Privacy Report, users can see what data an app collects and how it’s used. And App Tracking Transparency (ATT) empowers users to choose whether an app has permission to track their activity across other companies’ apps and websites for the purposes of advertising or sharing with data brokers. 

## Describe how your app uses data

##### Privacy Nutrition Labels

The App Store helps users better understand an app’s privacy practices before they download the app. On each app’s product page, users can learn about some of the data types an app may collect, and whether the information is used to track them or is linked to their identity or device. In order to submit new apps and app updates, you must provide information about your privacy practices in App Store Connect.

- App privacy details on the App Store

##### Privacy manifests

If your app uses third-party code, such as advertising or analytics SDKs, you must describe what data it collects, how it is used, and whether it tracks users. Privacy manifest files outline these practices in a single standard format. When you prepare to distribute your app, Xcode combines all these manifests into one comprehensive report, making it easier for you to create accurate Privacy Nutrition Labels.

- Privacy manifest files

- Third-party SDK requirements

## Ask permission to track

In iOS 14.5, iPadOS 14.5, and tvOS 14.5 or later, you need to receive the user’s permission through the App Tracking Transparency (ATT) framework in order to track them or access their device’s advertising identifier. Tracking refers to the act of linking user or device data collected from your app with user or device data collected from other companies’ apps, websites, or offline properties for targeted advertising or advertising measurement purposes. Tracking also refers to sharing user or device data with data brokers.

Examples of tracking include, but are not limited to:

- Displaying targeted advertisements in your app based on user data collected from apps and websites owned by other companies.

- Sharing device location data or email lists with a data broker.

- Sharing a list of emails, advertising IDs, or other IDs with a third-party advertising network that uses that information to retarget those users in other developers’ apps or to find similar users.

- Placing a third-party SDK in your app that combines user data from your app with user data from other developers’ apps to target advertising or measure advertising efficiency, even if you don’t use the SDK for these purposes. For example, using an analytics SDK that repurposes the data it collects from your app to enable targeted advertising in other developers’ apps.

The following use cases are not considered tracking, and do not require user permission through the App Tracking Transparency framework:

- When user or device data from your app is linked to third-party data solely on the user's device and is not sent off the device in a way that can identify the user or device.

- When the data broker with whom you share data uses the data solely for fraud detection, fraud prevention, or security purposes. For example, using a data broker solely to prevent credit card fraud.

- When the data broker is a consumer reporting agency and the data is shared with them for purposes of (1) reporting on a consumer's creditworthiness, or (2) obtaining information on a consumer's creditworthiness for the specific purpose of making a credit determination.

### Using the App Tracking Transparency framework

To request permission to track the user and access the device’s advertising identifier, use the App Tracking Transparency framework. You must also include a purpose string in the system prompt that explains why you’d like to track the user. Unless you receive permission from the user to enable tracking, the device’s advertising identifier value will be all zeros and you may not track them as described above.

While you can display the App Tracking Transparency prompt whenever you choose, the device’s advertising identifier value will only be returned once you present the prompt and the user grants permission. Use the purpose string to explain what this data will be used for to help the user understand what they’re opting in to share. If the user allows apps to request to track, but has turned tracking off for your app, you can ask the user to change their preference for your app by providing a shortcut to Settings where they can change the tracking permission.

The identifier for vendor (IDFV) may be used for analytics across apps from the same content provider. In this case, the use of the App Tracking Transparency framework is not required. The IDFV may not be combined with other data to track a user across apps and websites owned by other companies. You remain fully responsible for ensuring that your collection and use of the IDFV comply with applicable law.

For more information, see:

- App Tracking Transparency

- Human Interface Guidelines: Privacy

- AdSupport Framework

## ATT in the European Union

As part of agreements with select European competition authorities, Apple is introducing changes to its App Tracking Transparency framework in the European Union. Beginning with iOS 27.2 and iPadOS 27.2, developers will have the option to use an alternative version of the App Tracking Transparency system prompt in the EU. The requirements for when you must seek permission to track users will remain the same. Due to legal requirements, only the alternative version of the system prompt is available for apps distributed in Germany, France, Italy, Poland, and Romania.

The alternative version of the App Tracking Transparency system prompt has modified formatting and language and provides you the option to use a text button labeled “Additional Information.” This allows you to surface additional information about your request to link user or device data collected from your app with user or device data collected from other companies’ apps, websites, or offline properties for targeted advertising or advertising measurement purposes, or to share user or device data with a data broker.

In addition, for users in the European Union, you can reprompt a user via the App Tracking Transparency system prompt one year after the user’s previous choice in your app’s App Tracking Transparency system prompt, regardless of whether that choice was to accept or reject. A user cannot be re-prompted if they have disabled “Allow Apps to Request to Track” (renamed to “Allow Apps to Request to Link Your Activity Across Companies” in the EU) in their device’s Settings.

For technical details on using the alternative App Tracking Transparency system prompt and optional text button in the European Union, see:

- Requesting Authorization with Expanded Interface (new)

- Requesting Authorization

- Tracking Markdown Usage Description (new)

- Tracking Usage Description

## Frequently asked questions

### Can I gate functionality on agreeing to allow tracking, or incentivize users to agree to allow tracking in the App Tracking Transparency prompt?

No, per the App Review Guidelines: 5.1.2(i).

### Can I explain to users why I would like permission to track them before I show the tracking permission prompt?

Yes, so long as you are transparent to users about your use of the data in your explanation. Per the App Review Guidelines: 5.1.1 (iv), apps must respect the user's permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access.

### If I have not received permission from a user via the tracking permission prompt, can I use an identifier other than the IDFA (for example, a hashed email address or hashed phone number) to track that user?

No. You will need to receive the user's permission through the App Tracking Transparency framework to track that user.

### If a user provides permission for tracking via a separate process on our website, but declines permission in the App Tracking Transparency prompt, can I track that user across apps and websites owned by other companies?

Developers must get permission via the App Tracking Transparency prompt for data that's collected in the app and used for tracking. Data collected separately, outside of the app and not related to the app, is not in scope.

### Can I fingerprint or use signals from the device to try to identify the device or a user?

No. Per the Apple Developer Program License Agreement, you may not derive data from a device for the purpose of uniquely identifying it. Examples of user or device data include, but are not limited to: properties of a user's web browser and its configuration, the user's device and its configuration, the user's location, or the user's network connection. Apps that are found to be engaging in this practice, or that reference SDKs (including but not limited to Ad Networks, Attribution services, and Analytics) that are, may be rejected from the App Store.

### If I share data with a consumer reporting agency to conduct fraud checks, and separately share data with them as part of a credit check or for credit reporting purposes, do I need permission to track?

No. You do not need permission from the user when a data broker uses the data shared with them solely for fraud detection or prevention or security purposes. You also do not need permission from the user when sharing data with a consumer reporting agency and the data is shared with them for purposes of (1) reporting on a consumer's creditworthiness, or (2) obtaining information on a consumer's creditworthiness for the specific purpose of making a credit determination.

### Do I need to use the App Tracking Transparency framework to get user permission to use third-party deep-linking or deferred deep-linking tools?

Yes. If your application uses any third-party services that pass unique identifiers or create a shared identity of the user between applications from different companies for ad targeting, ad measurement, or sharing with a data broker, your app will need to request permission from the user using the App Tracking Transparency framework.

### I have integrated an SDK from another company. Am I responsible for the data collection and tracking of users of my app by that company?

Yes. Developers are responsible for all code included in their apps. If you are unsure about the data collection and tracking practices of code used in your app that you didn't write, we suggest contacting the developer of the SDK.

### I have integrated single sign-on functionality provided by another company. Am I responsible for the data collection and tracking practices of that company?

Yes. Developers are responsible for all code included in their app, including single sign-on (SSO) functionality provided by third parties. If the user will be subject to tracking as a result of SSO functionality included in your app, you must use the App Tracking Transparency prompt to obtain permission from that user first.

### What kind of company constitutes a data broker?

Data brokers are defined by law in some jurisdictions. In general, a data broker is a company that regularly collects and sells, licenses, or otherwise discloses to third parties the personal information of particular end-users with whom the business does not have a direct relationship.

### What identifiers or data are governed by the "tracking" policy?

Any user or device level identifier that is used to join data from your app with data from third parties (including SDKs used in your app) for purposes of advertising or ad measurement or sharing with a data broker. This includes, but is not limited to, the device's advertising identifier, session ID, fingerprint IDs, and device graph identifiers. If your app receives or shares any of these identifiers for the above listed purposes, you must use the App Tracking Transparency framework to obtain user consent.

### If tracking occurs within a webview inside an app, do I need to use the App Tracking Transparency prompt?

Yes. If you are using a webview for app functionality, it should be treated the same way as native functionality in your app, unless you are enabling the user to navigate the open web.

### What OS versions require App Tracking Transparency permission to access the value of the IDFA?

To access the value of the IDFA for users on iOS/iPadOS version 14.5 or later, you will first need to receive permission from the user through the App Tracking Transparency prompt. For additional guidance on tracking, please refer to App Review Guidelines: 5.1.1 (iv).

### Can I offer a control in my app, separate from ATT, to comply with local privacy laws?

Yes. You can offer separate privacy controls in your app. You can also provide a shortcut to Settings to enable the user to change their preference for your app with regard to the App Tracking Transparency permissions. When offering a separate control to comply with local privacy laws, please consider the following:

- Don't confuse the user. Be clear that the control doesn't override their previous ATT choice.

- Provide context. If possible, show the user's ATT status as part of a separate control so they can understand the choices they've already made.

- Be clear about what the choice is. If the user has not granted ATT permission, and there is no additional data use beyond the scope of ATT, be clear that no further action is required. If the user has granted ATT permission, it should be clear what impact the separate control will have on their ATT choice.

### Can I add other permission requests in order to comply with legal obligations or regulations?

Yes, you can choose to include screens in order to comply with applicable law or government regulations. However, your app must always respect the user’s response to the App Tracking Transparency prompt, even if their response to other prompts conflicts. Guideline 5.1.1 (iv) states: "Apps must respect the user's permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access." This includes altering a user’s App Tracking Transparency response by only respecting their response to other permission requests. You can use third-party Consent Management Platforms to add these permission requests, as long as your collection and use of device or user data collected from your app does not contradict a user’s App Tracking Transparency response. You remain fully responsible to ensure that your collection and use of information linked to users’ identity or to their device, including information used to track users, complies with applicable law or government regulations.

### Can I reference consent requests to comply with local privacy laws in my app’s App Tracking Transparency system prompt?

Yes. If you have already prompted the user with a prompt to comply with government regulations for data practices covered by App Tracking Transparency, e.g. using a third-party Consent Management Platform, and the user consented, you have the option to reference that previous legal consent in your app's App Tracking Transparency system prompt purpose string. When doing so, please consider the following:

- Don’t confuse the user. Be clear about how the impact of the user’s respective choices.

- Be consistent. You should not display the ATT prompt to users who have opted out of all relevant legal consent choices made in the previous, separate control.

- You remain fully responsible to ensure that your implementation of consent requests in combination with the ATT prompt complies with applicable privacy laws.

### Can I provide additional information and consent controls with my app’s ATT prompt implementation, to comply with local privacy laws in the European Union, such as ePrivacy or GDPR?

Yes. In the European Union, you have the option to use the “Additional Information” text button in the ATT prompt to surface additional information and more granular consent controls to comply with local privacy laws or other applicable legal requirements for the collection and use of device or user data collected from your app that are described in your app’s App Tracking Transparency system prompt. Any additional information related to your request or more granular consent controls provided via the text button are entirely your responsibility. However, you cannot access the device’s advertising identifier, or otherwise collect and use device or user data from your app as described in the App Tracking Transparency system prompt, until the user has granted your app permission in that prompt. When implementing this “layered” approach to comply with local privacy laws, please consider the following:

- Provide context. The purpose string in the App Tracking Transparency system prompt should contain the most important information about your intended collection and use of the advertising identifier or other relevant device or user data collected from your app, in line with local privacy laws and regulatory guidelines. You can also include information in the purpose string in the App Tracking Transparency system prompt to explain to your user what additional information and granular consent controls they can obtain by tapping on the “Additional Information” text button.

- Be consistent. After a user taps on “Additional Information” and accesses the relevant screen in your app or page in your website, you can redirect the user back to the App Tracking Transparency system prompt for your app to ensure their choice is recorded in the App Tracking Transparency framework. However you should not redirect users to your ATT prompt if they have opted out of all relevant legal consent choices in the screen or page surfaced.

- Assess the clearest and most suitable option for your app. The ability to link to additional information and more granular consent controls within the App Tracking Transparency prompt for your app is entirely optional. In addition, you remain free to add other permission requests and separate controls for your app independently from App Tracking Transparency (see Questions above).

- You remain fully responsible to ensure that your implementation of the App Tracking Transparency system prompt and any corresponding information surfaced via the “Additional Information” text button complies with applicable privacy laws.

## App Privacy Report

With iOS and iPadOS, users can turn on App Privacy Report to see details about how often apps access their data — like location, camera, microphone, and more. They can see information about each app’s network activity and website network activity, as well as the web domains that all apps contact most frequently. 

- About App Privacy Report

## Attributing app installations

Advertisers can use AdAttributionKit — Apple’s privacy-preserving, industry-leading technology — to attribute in-app ad campaigns and web ads on mobile, while maintaining user privacy. 

- Measuring ad performance with AdAttributionKit

