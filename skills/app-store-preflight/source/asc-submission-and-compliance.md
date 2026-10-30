=== SOURCE: https://developer.apple.comdoc://com.apple.security/documentation/Security/complying-with-encryption-export-regulations
# Complying with Encryption Export Regulations

Declare the use of encryption in your app to streamline the app submission process.

### Overview

When you submit your app to TestFlight or the App Store, you upload your app to a server in the United States. If you distribute your app outside the U.S. or Canada, your app is subject to U.S. export laws, regardless of where your legal entity is based. If your app uses, accesses, contains, implements, or incorporates encryption, this is considered an export of encryption software, which means your app is subject to U.S. export compliance requirements, as well as the import compliance requirements of the countries where you distribute your app.

Every time you submit a new version of your app, App Store Connect asks you questions to guide you through a compliance review. You can bypass these questions and streamline the submission process by providing the required information in your app’s Information Property List file.

For more information about export compliance, read Export compliance overview.

#### Declare Your App’s Use of Encryption

Add the ITSAppUsesNonExemptEncryption key to your app’s information property list with a Boolean value that indicates whether your app uses encryption. Set the value to NO if your app—including any third-party libraries it links against—doesn’t use encryption, or if it only uses forms of encryption that are exempt from export compliance documentation requirements. Otherwise, set it to YES.



Typically, the use of encryption that’s built into the operating system—for example, when your app makes HTTPS connections using URLSession—is exempt from export documentation upload requirements, whereas the use of proprietary encryption is not. To determine whether your use of encryption is considered exempt, see Determine and upload app encryption documentation.

[Important]

Important:  If your app uses exempt forms of encryption, you might alternatively be required to submit a year-end self-classification report to the U.S. government. (If you use non-exempt encryption and provide documentation to Apple, the self-classification report isn’t necessary.) To learn more, see How to file an Annual Self Classification Report.

#### Provide Compliance Documentation

If your app requires export compliance documentation, upload the required items to App Store Connect, as described in Determine and upload app encryption documentation. After successfully reviewing the documents, Apple provides you with a code. Add this string as the value for the ITSEncryptionExportComplianceCode key in your app’s information property list.



## Encryption Export Compliance Keys

- ITSAppUsesNonExemptEncryption: A Boolean value indicating whether the app uses encryption.

- ITSEncryptionExportComplianceCode: The export compliance code provided by App Store Connect for apps that require it.

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

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Overview of submitting for review 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Overview of submitting for review

The review process covers every version of your app and its content, like In-App Purchases, subscription offers, and Apple-hosted asset packs, to ensure a safe and trustworthy experience for users and to support developers' success.

Our goal is to make the submission process as convenient and efficient as possible. While you typically submit one submission for review at a time per platform, you also have the flexibility to submit items with one additional submission, even if you already have an app version submitted for review.

For example, if you have an app version currently under review, you can also submit an In-App Event in a separate submission, or if you have a custom product page under review, you can also submit an app version in a separate submission.

Note: Submissions may not be reviewed in the order you submit them.

You can choose to submit items for review together with, or separately from, an app version. If your submission includes an app version, items will be reviewed together with that app version. If your submission doesn’t include an app version, or your submission includes items associated with multiple platforms, items will be reviewed together with the latest version of the platform you specify during the submission process. Use the App Review information section on the latest approved app version for that platform to provide additional information or context that will help App Review during the review process. Learn about App Review guidelines.

App versions for each platform are submitted separately. The status of any app versions on one platform doesn’t influence the status of app versions on other platforms.

Manage your submissions and messages with the App Review team in the App Review section of the sidebar. This section may display four types of content:

-  
App (iOS, macOS, tvOS, visionOS) Submission: App versions and/or items that you submitted to App Review, and any related messages from App Review.

-  
Beta Build: Beta versions of your app that you submitted and App Review didn’t accept, and any related messages from App Review.

-  
Beta Asset Pack: Beta versions of asset packs that you submitted and App Review didn’t accept, and any related messages from App Review.

-  
App Review Message: Other messages from App Review that don’t relate to a submission.

Learn about upcoming submission requirements.

Learn how to submit using the App Store Connect API.

##  FAQs

### How many submissions can I submit for review at a time?

-  
Each platform can have one app version submission under review at a time.

-  
A platform can have a maximum of two submissions under review at a time: one that includes an app version and one that includes items, like In-App Events or custom product pages, without an app version.

### What items can I add to a submission?

Items associated with different platforms can't be added to the same submission. For example, if you’ve selected the macOS platform for a submission with an Apple-hosted asset pack, you’ll need to create a separate submission to submit a custom product page for iOS.

In addition to an app version, you can add the following items to a submission to App Review:

-  
Auto-renewable subscription, non-renewing subscriptions, and subscription groups

-  
In-App Purchases

-  
In-App Events

-  
Custom product pages

-  
Product page optimization tests

-  
Apple-hosted asset packs

-  
Game Center components, including new or modified leaderboards, leaderboard sets, achievements, challenges, and activities 

Related App Review Guidelines Platform version information Run a test Create and submit app bundles

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-an-app/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Submit an app 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Submit an app

Before submitting an app version for review, provide required metadata and choose the build for the version.

Learn how to submit using the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version you want to submit.

-  
On the right, scroll down to the Build section and verify that you added the right build for the version.

-  
On the top right, click “Add for Review,” and select whether to add the app version to an existing draft submission or create a new submission. The app status changes to Ready for Review. Your submission won’t be sent to App Review until you submit it for review in the next step.

You can add items, such as In-App Events or Apple-hosted asset packs, to your submission. All items submitted together must be Accepted to complete the submission.

To review the items you've added, click Draft Submissions on the bottom right of the screen and select the submission. Alternatively, you can go to the App Review section in the sidebar.

-  
Click Submit for Review. When the review process starts, the app status changes to In Review. Learn about the tasks you can do in these statuses.

Related Remove a submission from review

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/reply-to-app-review-messages/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Reply to App Review messages 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Reply to App Review messages

If App Review or TestFlight App Review rejects your app, you can communicate with Apple and resolve issues in the App Review section.

When your app is rejected, you'll get a message containing information about the rejection, including how it violates the App Review Guidelines or Notarization Review Guidelines. You can correspond with Apple, and include attachments, such as screenshots and supporting documents, until you resubmit to App Review. If your app was rejected for a metadata issue, you can resubmit the same build after resolving the issue.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Reply to messages on the App Review page

-  
In Apps, select the app you want to view.

-  
At the top of the page, click the link that indicates that there are unresolved issues.

-  
In the In Progress section, click Resolve next to the submission you want to view.

-  
To reply, click Reply to App Review.

-  
Enter text in the Reply field.

-  
To include a file, click Attach File and, in the dialog that appears, choose a file.

-  
Click Reply.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/remove-a-submission-from-review/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Remove a submission from review 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Remove a submission from review

You can remove an app from the review and release process if the app is in one of the following states:

-  
Waiting for Export Compliance

-  
Waiting for Review

-  
In Review

-  
Pending Developer Release

-  
Pending Apple Release

Learn how to remove a submission from review with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Remove an app from the review and release process

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version that you want to remove a build for.

-  
In the message that appears at the top, click “remove this version from review.”

-  
In the dialog that appears, click Remove.

The app, and any other items in the submission, are removed from the queue and the app status changes to Developer Rejected. If you resubmit the review process will start over.

### Cancel a submission

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Review.

-  
Under Submissions, click the submission you want to remove.

-  
At the bottom of the page, click Cancel Submission.

-  
Click Confirm.

Your submission will be cancelled, and any items marked as Accepted must be resubmitted. If the submission includes an app version, its status will change to Developer Rejected. If you resubmit, the review process will start over.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/manage-a-submission-with-unresolved-issues/
### App Store Connect Help

App Store Connect / Manage submissions to App Review / Manage a submission with unresolved issues 
Filter ⌘K  
Filter ⌘K  

Manage submissions to App Review  

# Manage a submission with unresolved issues

If any of the items in your submission are rejected, the submission status changes to Unresolved Issues. To consider a submission approved, App Review needs to approve all items. To continue with the accepted items, you need to either edit and resubmit, or remove the rejected items from the submission. When a submission has a status of Unresolved Issues, you can’t add more items to it.

## Remove rejected items

-  
In Apps, click View App Review Issues & Messages.

-  
In the In Progress section, click Resolve next to the submission.

-  
Hold the pointer over the item you want to remove, then click the delete button (–).

Once you remove all rejected items, the submission moves to the Completed section of the App Review page and is ready for release.

### Edit and resubmit rejected items

-  
In Apps, click View App Review Issues & Messages.

-  
In the In Progress section, click Resolve next to the submission.

-  
Click Edit next to the item you want to edit.

-  
Make the necessary changes, then click Add for Review.

You can edit items in a submission once before resubmission. If you no longer want to submit the item, you can remove it. Please note that you can’t add back removed items to the same submission.

-  
Once you edit or remove all rejected items, click Resubmit to App Review from the submission details page.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating/
### App Store Connect Help

App Store Connect / Manage app information / Set an app age rating 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Set an app age rating

An age rating is a required app information property that helps users assess the content and any potentially objectionable material within your app or game. This rating supports the functionality of parental controls, allowing parents and guardians to establish a safe online environment for children. As a developer, you can deliver age-appropriate experiences tailored for users across all age groups.

To determine the age rating of your app, respond to the age rating questionnaire in App Store Connect. This questionnaire includes a list of content descriptors, in-app controls, and capabilities that allow you to specify the frequency of each content type in your app. Your selections are then translated into an Apple global age rating, as well as additional region-specific ratings if required. Learn about age rating values and definitions.

This process helps you understand how different types of content can impact your app’s rating across various regions, enabling you to make informed declarations of frequency of the content and features in your app.

Depending on your responses, an age rating is assigned to each country or region based on their specific age suitability standards. This rating will be displayed on the App Store for that country or region and will remain consistent across all platforms. Learn about age rating values with region-specific requirements for Australia, Brazil, and Korea.

Notes: 

-  
Age ratings for an app may vary based on the OS version. View age range value details for Apple devices running a minimum of iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, visionOS 26, and watchOS 26. View details for Apple devices running an earlier OS version.

-  
An Unrated app can’t be published on the App Store. It may be published on alternative app marketplaces or websites.

Learn how to manage app age ratings with the App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

## Set an app age rating

-  
In Apps, select the app you want to view.

-  
In the sidebar, under General, click App Information.

Tip: To learn more about and view examples of the features and content used to determine age ratings, select a category from the panel of examples on the App Information Page. You can also browse Age rating categories.

-  
Below Age Ratings, click the Set Up Age Ratings button.

-  
When the dialog box appears, review the list of in-app controls and capabilities options, and select any that your app includes that can restrict content, then click Next.

-  
Navigate through each section of the progress bar, answering the questions and selecting the appropriate level of frequency for each content description, then click Next.

### Made for Kids category on the App Store

If your calculated rating is 4+ or 9+ and you want your app to also display in the Kids category on the App Store, under Age Categories and Override, choose Made for Kids and from the menu, select the appropriate age range for your app. You can’t change this selection once your app is approved by App Review. The app and all subsequent updates will need to follow the Kids category guidelines.

Note: You can’t select the Made for Kids option for visionOS apps, and apps in the Kids category can’t be made available on visionOS apps. 

### Override to higher age rating

To increase the rating of your app to a rating that exceeds the rating assigned by Apple, choose Override to Higher Age Rating and select the appropriate rating from the menu. App Store will display this specified age rating, and the content descriptions will still reflect your questionnaire answers.

If your app will be distributed through alternative app marketplaces or your website in the European Union and you believe your app is Unrated, select Unrated from the menu options under Override to Higher Age Rating.

Note: 

-  
If your app has a EULA with minimum age requirements that exceed the rating that Apple calculated, you must override to a rating that adheres to the requirements.

-  
The override will apply in all regions where your app is available and may override to a different rating value per region based on region-specific requirements. Learn about age rating values with region-specific requirements for Australia, Brazil, and Korea.

-  
If your app has a dedicated website with details on age suitability, you can provide the URL in the field provided under Age Suitability URL (Optional).

-  
Click Save. The dialog box will close, returning you to the App Information page. Here, you can view your global and region-specific ratings . Click on each panel for details on the age ratings and the specific countries and regions they apply to.

To edit your age rating, click App Information in the sidebar, then click Edit at the top of the page.

Note: You can view the age ratings for Apple devices running an earlier OS version than 26 under the Operating Systems Earlier than Version 26 section. Learn more.

### Override region-specific ratings

### Override age rating for the Republic of Korea

App Review may contact you if the Korean Games Rating and Administration Committee (GRAC) issues a region-specific rating that differs from your app's existing age rating. If you receive this notice, you need to update your app's age rating for the App Store in Korea by providing your Rating Classification Number (RCN) and submitting a new version of your app to App Review.

-  
In Apps, select your app.

-  
In the sidebar, under General, click App Information.

-  
In the Age Ratings section, next to Republic of Korea, click Add RCN.

-  
In the dialog that appears, enter your RCN and select the rating you received from GRAC.

-  
Select the checkbox confirming that this is the official rating issued by GRAC for your app, then click Save.

Note: If an error appears after clicking Save, address the error message and click Save again.

You can edit your RCN or override at any time before submitting your app for review by clicking Edit RCN next to Republic of Korea. From there, you can select a new rating, or clear your RCN and rating together by clicking Remove. While your app is in review, you can only view your RCN and rating by clicking View RCN. Once your app is approved, your RCN and rating are locked and can no longer be edited.

Related Age ratings values and definitions Platform version information Required, localizable, and editable properties

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance/
### App Store Connect Help

App Store Connect / Manage app information / Overview of export compliance 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Overview of export compliance

If your app uses, accesses, contains, implements, or incorporates encryption, and you intend to upload, test, and distribute it, you need to determine your export compliance requirements in App Store Connect.

Examples of apps requiring an export compliance determination include, but aren’t limited to, apps that use:

-  
Standard encryption algorithms.

-  
Crypto functionality within Apple’s operating system.

-  
Proprietary or non-standard encryption algorithms. The US Government defines "non-standard cryptography" as any implementation of “cryptography” involving the incorporation or use of proprietary or unpublished cryptographic functionality, including encryption algorithms or protocols that have not been adopted or approved by a duly recognized international standards body (e.g., IEEE, IETF, ISO, ITU, ETSI, 3GPP, TIA, and GSMA) and haven’t otherwise been published.

Please note that it’s your responsibility to review the Export Administration Regulation to determine whether your app's use of encryption requires a formal classification (Commodity Classification Automated Tracking System or CCATS) from BIS. you're responsible for all liabilities associated with misinterpretation of export regulations or claiming exemption inaccurately. To learn about encryption export controls, search for "encryption policy" on the US Department of Commerce Bureau of Industry and Security (BIS) website. The import and export of encryption apps distributed in France are also controlled by the French Government. The main items of control for France are Secure Storage, Secure Communications, and Security Anti-Virus applications. Exemptions include Banking and Medical applications. For more information about these French controls, visit the Agence nationale de la sécurité des systèmes d’information (ANSSI) website.

When you submit a new version of your app, you’ll need to answer questions in App Store Connect about your app's use of encryption. Follow the steps below before submitting your app to App Review to ensure that you’re submitting the right documentation and to bypass these questions if your app doesn’t use encryption.

## Determine your export compliance requirements

App Store Connect provides a simple way for you to determine your export compliance requirements by presenting you with a set of questions about your app and where you plan to make it available. Based on your answers, complete the following steps:

Scenario

Next Steps

No export compliance documentation required

Update your app’s information property list (Info.plist) file in Xcode so that you don’t need to answer encryption questions with each app submission.

Export compliance documentation required

- Use App Store Connect to submit your app encryption documentation.

- Once the documentation is approved, attach it to your beta build or app version build.

- Update your app’s information property list (Info.plist) file in Xcode so that you don’t need to answer encryption questions with each app submission.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-app-information/determine-and-upload-app-encryption-documentation/
### App Store Connect Help

App Store Connect / Manage app information / Determine and upload app encryption documentation 
Filter ⌘K  
Filter ⌘K  

Manage app information  

# Determine and upload app encryption documentation

Learn how to manage app encryption declarations and documentation using the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Determine your export compliance requirements

App Store Connect provides a set of questions to help you determine whether app encryption documentation is required from you, and which forms are specifically needed.

Learn about the app encryption documentation you may need to provide.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Information.

-  
Next to App Encryption Documentation, click the add button (+) and answer the questions that appear in the dialogs.

Alternatively, you can click Manage next to the build that’s missing app encryption information on either the Distribution tab or TestFlight tab to answer the required questions.

### Upload your documentation

If you’re required to upload app encryption documentation, you can do so in the App Encryption Documentation section in the App Store Connect. This should be completed before submitting a build for review on either App Review or TestFlight App Review. To ensure a smooth review process, populate the App Description field and manage availability for your app on the App Store before providing this documentation. Without this information, Apple can’t determine whether the app encryption documents are sufficient.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click App Information.

-  
Next to App Encryption Documentation, click the add button (+) and answer the questions that appear in the dialogs.

-  
When prompted, click Choose File to upload your document.

-  
Click Save.

Apple evaluates export compliance reviews on a case-by-case basis. If you provide complete information, Apple expects to review and clear apps in approximately two business days. Once your documentation is approved, Apple will provide you a key value. You must enter this value in Xcode to avoid answering encryption questions with each app submission. You can find this key value next to your approved documentation in the App Encryption Documentation section of App Store Connect.

If your app doesn’t require documentation, update your app’s information property list (Info.plist) file in Xcode to let us know that your app doesn't use encryption or is exempt from providing documentation.

If you have specific questions about Apple's export process, contact us.

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/export-compliance-documentation-for-encryption/
### App Store Connect Help

App Store Connect / Reference / App information / Export compliance documentation for encryption 
Filter ⌘K  
Filter ⌘K  

Reference  

# Export compliance documentation for encryption

Depending on the kind of encryption algorithm your app uses, you may need to provide documentation in App Store Connect.

Encryption algorithm in use

Required documentation

Your app uses encryption limited to that within the Apple operating system

No documentation required in App Store Connect.

Your app uses an industry standard algorithm, not provided within the Apple operating system

Upload your French encryption declaration in App Store Connect.1

Your app uses proprietary encryption algorithms not accepted by international standard bodies (such as IEEE, IETF, or ITU)

Upload your:

-  
US Commodity Classification Automated Tracking System (CCATS)

-  
French encryption declaration in App Store Connect1

1 French encryption declaration form is only required if you’re distributing your app on the App Store in France.

Related Overview of export compliance

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-export-compliance-information-for-beta-builds/
### App Store Connect Help

App Store Connect / Test a beta version / Provide export compliance information for beta builds 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Provide export compliance information for beta builds

Specify encryption use for your build to avoid the beta being marked as Missing Compliance. Answer the export compliance questions or attach previously approved documentation in the TestFlight section.

Learn how to provide export compliance information for a build using the App Store Connect API.

Required role: Account Holder, Admin, and App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under Builds, click the platform.

-  
In the Build column in the table on the right, click the app icon or build string for the build that’s missing compliance information.

To address compliance issues for a build, you can either click Manage beside the relevant build to answer the required questions, or click Choose File to upload previously approved documentation.

-  
Click Provide Export Compliance Information, and answer the required questions.

-  
If app encryption documentation is required, click Go to App Encryption Page to upload your file. Apple will provide you with a key value to enter in Xcode This will remove the need to answer encryption questions with each app submission. Learn more about uploading app encryption documentation.

If documentation isn’t required, click Save. You can indicate that your app doesn’t use encryption or is exempt from documentation by  specifying encryption settings in the app's Info.plist file in Xcode. This eliminates the need to answer encryption questions with each app submission.

Related TestFlight overview Overview of export compliance Add testers to builds Stop testing a build

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions/
### App Store Connect Help

App Store Connect / Reference / App information / Age ratings values and definitions 
Filter ⌘K  
Filter ⌘K  

Reference  

# Age ratings values and definitions

The age rating is a required app information field used for property used by the parental controls. These controls enable parents and guardians to establish a safe online environment for children. As a developer, you can deliver age-appropriate experiences tailored for users across all age groups.

In App Store Connect, you'll find a list of content descriptors, in-app controls, and capabilities that allow you to specify the frequency or presence of each in your app. Apple generates appropriate ratings based on your answer to the age rating questionnaire. Learn how to set an app age rating.

The tables below provide detailed information about the different age rating categories and age rating values by region.

Notes: 

-  
An Unrated app can't be published on the App Store. It may be published on alternative app marketplaces or websites.

-  
Age ratings for an app may vary based on the OS version. View age range value details for Apple devices running a minimum of iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, visionOS 26, and watchOS 26. View details for Apple devices running an earlier OS version.

## Age rating categories

Category

Examples of included features and content

In-App Controls

-  
Parental Controls: Settings or tools that allow parents/guardians to monitor, manage, or restrict a child's access to in-app content or features that may not be suitable. May include: tools to enable content blocking or filtering; setting usage limits; or restrictions on using certain features, such as making purchases or using communication features.

-  
Age Assurance: Mechanism to confirm an individual's age meets the age requirement for accessing specific content or services. May include: declared age range API; age estimation capabilities; age verification via government-issued passport, drivers license, national ID, or other means of age assurance.

Capabilities 

-  
Unrestricted Web Access: Users can navigate to any webpage within the app or freely browse the web. May include: embedded browser functionality or browser app.

-  
User-Generated Content: Includes the broad distribution of content created by users as a component of the app's intended user experience. May include: broadly distributed videos, photos, text, and/or audio created by users of the app.

-  
Social Media: Redistribution, amplification, or interaction with user-generated content through a social feed or similar discovery method that visibly spreads content to many users. May include: feeds that allow users to engage with and amplify user-generated content through features such as views, likes, comments, and shares.

-  
Social Media Disabled for Users Under 13: Users under 13 don't have access to social media capabilities. At a minimum, the Declared Age Range API is called to check users' age ranges before enabling social media features. Only age-appropriate UGC is delivered.

-  
Messaging and Chat: Users can directly communicate with one another through features within the app. May include: text, voice and/or video chat, direct and/or group messaging, or public posting.

-  
Advertising: Paid promotion of products or services within the app. May include: banner ads, video and playable ads, rich media ads, or native ad formats.

Mature Themes

-  
Profanity or Crude Humor: Offensive or vulgar language that may be considered rude, obscene, or inappropriate. May include: swearing, derogatory slurs, insult-based humor, or jokes about bodily functions.

-  
Horror/Fear Themes: Content or storylines that evoke feelings of anxiety, dread, or terror. May include: supernatural or psychological elements; body horror; or fear of the unknown, isolation, or death.

-  
Alcohol, Tobacco, or Drug Use or References: References to or depictions of the consumption of alcohol, tobacco products, or other licit or illicit substances. May include: drunken behavior, cigarette smoking, or the taking of illegal drugs.

Medical or Wellness

-  
Medical or Treatment Information: Content that provides diagnoses or guidance around the management of medical conditions or health and wellness. May include: medication guidance, emergency medical care, or treatment information.

-  
Health or Wellness Topics: Content that provides self-care or lifestyle recommendations. May include: calorie tracking, dieting advice, or exercise recommendations.

Sexuality or Nudity

-  
Mature or Suggestive Themes: Content that implies or indirectly references sexual or mature topics without being explicit or topics for older audiences due to the complex, intense, or sensitive nature, which may deal with real-world issues or content unsuitable for children. May include: sexual innuendo, sensual or suggestive imagery, censored or implied nudity, real-world crimes, psychological trauma or abuse, moral or ethical dilemmas, or war or political strife.

-  
Sexual Content or Nudity: Non-explicit depictions of sexual behavior, including brief or partial nudity. May include: mild romantic intimacy, implied sexual activity, or erotic or sensual dialog.

-  
Graphic Sexual Content and Nudity: Explicit, detailed depictions of sexual activity or nudity. May include: uncensored or full-frontal nudity; realistic, illustrative, or pornographic portrayals of sex.

Violence

-  
Cartoon or Fantasy Violence: Physical conflict or harm of an exaggerated or fantastical nature that can easily be distinguished from real life. May include: animated magic used to harm animals or animated human wrestling.

-  
Realistic Violence: Aggressive physical conflict or harm involving humans in lifelike situations. May include: a bloody nose from being punched, a shoot-out, or combat between characters.

-  
Prolonged Graphic or Sadistic Realistic Violence: Prolonged detailed or realistic-looking depictions of physical conflict. May include: realistic and/or extreme depictions of gore, human injury, or death.

-  
Guns or Other Weapons: References to or depictions of guns, weapons, or objects that may cause bodily harm. May include: guns, swords, or knives.

Chance-Based Activities

-  
Gambling: Betting or wagering using real money or in-game currency that may be exchanged for real money. May include: casino or card games, sports and non-sports betting, or lotteries and raffles.

-  
Simulated Gambling: Betting or wagering without using real money or in-game currency that can be exchanged for real money.

-  
Contests: Events that allow users to compete with one another for rankings, rewards, or the achievement of personal goals. May include: skill-based competitions, trivia quizzes, or sport or fitness contests

-  
Loot Boxes: Virtual containers that provide players with randomized virtual items for purchase. May include: randomized functional cards or cosmetic items for purchase.

### Age rating values

These ratings apply to all regions that don’t have any additional regional requirements.

Learn about age rating values with region-specific requirements for Australia, Brazil, and Korea.

Rating

Definition

4+

Apps with this rating contain no objectionable material but may contain instances of the following content that may not be suitable for children under the age of 4:

In-App Controls:

-  
Parental controls

-  
Age assurance

Capabilities:

-  
User-generated content

-  
Messaging and chat

-  
Advertising

Chance-Based Activities:

-  
Infrequent contests

9+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 9:

Mature Themes

-  
Infrequent profanity and crude humor

-  
Infrequent horror or fear themes 

Medical or Wellness

-  
Health and wellness topics 

Sexuality or Nudity

-  
Infrequent mature or suggestive themes

Violence

-  
Infrequent cartoon or fantasy violence

-  
Infrequent guns or other weapons

Chance-Based Activities

-  
Loot boxes

13+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 13:

Capabilities:

-  
Social media

-  
Social media disabled for users under 13

Mature Themes:

-  
Frequent profanity and crude humor

-  
Frequent horror or fear themes

-  
Infrequent alcohol, tobacco, or drug use or references

Medical or Wellness:

-  
Infrequent medical or treatment information

Sexuality or Nudity:

-  
Infrequent sexual content or nudity

Violence:

-  
Frequent cartoon or fantasy violence

-  
Infrequent realistic violence

-  
Frequent guns or other weapons

Chance-Based Activities:

-  
Infrequent simulated gambling

-  
Frequent contests

16+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 16:

Capabilities:

-  
Unrestricted web access

Medical or Wellness:

-  
Frequent medical or treatment information

Sexuality or Nudity:

-  
Frequent mature or suggestive themes

18+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 18:

Mature Themes:

-  
Frequent alcohol, tobacco, or drug use or references

Sexuality or Nudity:

-  
Frequent sexual content or nudity

Violence:

-  
Frequent realistic violence 

Chance-Based Activities:

-  
Gambling

-  
Frequent simulated gambling

Unrated

Apps with this rating may contain instances of the following content that can’t be published on the App Store. It may be published on alternative app marketplaces or websites:

Sexuality or Nudity:

-  
Infrequent or Frequent graphic sexual content and nudity

Violence:

-  
Infrequent or Frequent prolonged graphic or sadistic realistic violence

### Australia age rating values

As required by Australia’s guidelines for the classification of computer games, apps that have at least one of the following content descriptors will display the regional region-specific age rating.

Note: Only the age rating values listed below differ from the age rating values.

Rating

Definition

16+

Apps that contain:

Capabilities:

-  
Social media

-  
Social media disabled for users under 13

Chance-Based Activities:

-  
Loot boxes

R 18+

Apps that contain:

Chance-Based Activities:

-  
Infrequent simulated gambling

If we’re notified by the regulator that your app doesn’t meet their guidelines or requires a region-specific rating, you’ll receive a message from App Review. If you receive this message, follow the instructions and re-submit your app for review.

### Brazil age rating values

As required by the Brazilian Ministry of Justice and Public Security (MJSP), the App Store uses a different set of region-specific rating pictograms and descriptors for self-rated apps, than for ratings officially issued by the MJSP.

Official Brazil region-specific ratings and descriptors apply to apps that were issued an official rating by the MJSP. If a rating or descriptor has been issued to your app by the MJSP, Apple will update your regional rating and/or descriptors on your behalf and it'll display on the App Store in Brazil.

Apps that include fixed-odds betting (gambling) features require a valid Brazilian fixed-odds betting license from the Secretariat of Prizes and Bets (SPA) to be distributed on the App Store in Brazil. When submitting a new app update, provide your license details and any supporting documentation in the App Review Information section in App Store Connect. Enter your license details in the Notes field and attach any supporting documents using the file attachment field.

Review App Review Guideline 5.3.4. to ensure gambling app compliance.

Possible values for official Brazil age pictograms are:

Possible values for self-rated Brazil age pictograms are:

Rating

Definition

AL

Apps that contain no objectionable material but may contain instances of the following content:

In-App Controls:

-  
Parental controls

-  
Age assurance

A6

Apps that contain:

Capabilities:

-  
User-generated content

Violence:

-  
Infrequent cartoon or fantasy violence

Chance-Based Activities:

-  
Infrequent contests

A10

Apps that contain:

Mature Themes:

-  
Infrequent profanity and crude humor

-  
Infrequent horror or fear themes 

Medical or Wellness:

-  
Health and wellness topics 

Violence:

-  
Infrequent guns or other weapons

A12

Apps that contain:

Capabilities:

-  
Advertising

-  
Messaging and chat

Mature Themes:

-  
Frequent profanity and crude humor

Medical or Wellness:

-  
Infrequent medical or treatment information

Sexuality or Nudity:

-  
Infrequent mature or suggestive themes

-  
Infrequent sexual content or nudity

Violence:

-  
Frequent cartoon or fantasy violence

-  
Infrequent realistic violence

-  
Frequent guns or other weapons

Chance-Based Activities:

-  
Infrequent simulated gambling

A14

Apps that contain:

Mature Themes:

-  
Frequent horror or fear themes

-  
Infrequent alcohol, tobacco, or drug use or references

A16

Apps that contain:

Capabilities:

-  
Unrestricted web access

-  
Infrequent guns or other weapons

-  
Social media

-  
Social media disabled for users under 13

Mature Themes:

-  
Frequent alcohol, tobacco, or drug use or references

Medical or Wellness:

-  
Frequent medical or treatment information

A18

Apps that contain:

Sexuality or Nudity:

-  
Frequent mature or suggestive themes

-  
Frequent sexual content or nudity

Violence:

-  
Frequent realistic violence

Chance-Based Activities:

-  
Frequent gambling

-  
Frequent simulated gambling

-  
Loot boxes

### Republic of Korea age rating values

For all apps made available in Korea, the following region-specific rating values will display:

Note: Apps and games with Frequent or Intense simulated gambling content are only available on the App Store in Korea if you provide a Rating Classification Number (RCN).

Rating

Definition

All

Apps that contain:

In-App Controls:

-  
Parental controls

-  
Age assurance

Capabilities:

-  
User-generated content

-  
Messaging and chat

-  
Advertising

Mature Themes:

-  
Infrequent horror or fear themes

Medical or Wellness:

-  
Health or wellness topics

Violence:

-  
Infrequent cartoon or fantasy violence

-  
Infrequent guns or other weapons

Chance-Based Activities:

-  
Infrequent contests

-  
Loot boxes

12+

Apps that contain:

Mature Themes:

-  
Infrequent profanity and crude humor

-  
Frequent profanity and crude humor

-  
Frequent horror or fear themes

-  
Infrequent alcohol, tobacco, or drug use or reference

Medical or Wellness:

-  
Infrequent medical or treatment information

Sexuality or Nudity:

-  
Infrequent mature or suggestive themes

-  
Frequent mature or suggestive themes

-  
Infrequent sexual content or nudity

Violence:

-  
Frequent cartoon or fantasy violence

-  
Infrequent realistic violence

-  
Frequent guns or other weapons

Chance-Based Activities:

-  
Infrequent simulated gambling

15+

Apps that contain:

Capabilities:

-  
Unrestricted web access

-  
Social media

-  
Social media disabled for users under 13

Medical or Wellness:

-  
Frequent medical or treatment information

19+

Apps that contain:

Mature Themes:

-  
Frequent alcohol, tobacco, or drug use or references

Sexuality or Nudity:

-  
Frequent sexual content or nudity

Violence:

-  
Frequent realistic violence 

Chance-Based Activities:

-  
Frequent simulated gambling

Note: You’ll receive a message from App Review if the Korean Games Rating and Administration Committee(GRAC) issues an official rating for your app that is different from your app’s age rating. If you receive this notice, follow the instructions in the override age rating for Korea section and re-submit your app for review.

### Vietnam age rating values

As required by Article 38 of Vietnam Decree 147, apps that have at least one of the following content descriptors will display the region-specific age rating.

Rating

Definition

00+

Apps with this rating contain no objectionable material but may contain instances of the following content:

In-App Controls:

-  
Parental controls

-  
Age assurance

Capabilities:

-  
User-generated content

-  
Messaging and chat

-  
Advertising

Chance-Based Activities:

-  
Infrequent contests

12+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 12:

Mature Themes:

-  
Infrequent profanity and crude humor

-  
Frequent profanity and crude humor

-  
Infrequent horror or fear themes

-  
Frequent horror or fear themes

-  
Infrequent alcohol, tobacco, or drug use or reference

Medical or Wellness:

-  
Infrequent medical or treatment information

-  
Health and wellness topics 

Sexuality or Nudity:

-  
Infrequent mature or suggestive themes

-  
Infrequent sexual content or nudity

Violence:

-  
Infrequent cartoon or fantasy violence

-  
Frequent cartoon or fantasy violence

-  
Infrequent guns or other weapons

Chance-Based Activities:

-  
Frequent contests

-  
Loot boxes

16+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 16:

Capabilities:

-  
Unrestricted web access

-  
Social media

-  
Social media disabled for users under 13

Medical or Wellness:

-  
Frequent medical or treatment information

Sexuality or Nudity:

-  
Frequent mature or suggestive themes

Violence:

-  
Infrequent realistic violence

-  
Frequent guns or other weapons

Chance-Based Activities:

-  
Infrequent simulated gambling

18+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 18:

Mature Themes:

-  
Frequent alcohol, tobacco, or drug use or references

Sexuality or Nudity:

-  
Frequent sexual content or nudity

Violence:

-  
Frequent realistic violence 

Chance-Based Activities:

-  
Frequent simulated gambling

-  
Gambling

## Age ratings on OS versions earlier than 26

The age rating is a required app information field used for parental controls. These controls enable parents and guardians to establish a safe online environment for children. As a developer, you can deliver age-appropriate experiences tailored for users across all age groups. Learn more about how parents approve what kids buy with ask to buy.

View the age ratings that'll be displayed for Apple devices running an earlier OS version than 26 in the Operating Systems Earlier than Version 26 section under Age Ratings in App Store Connect.

View age range value details for Apple devices running a minimum of iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, visionOS 26, and watchOS 26.

## Global age ratings

Rating

Definition

4+

Apps with this rating contain no objectionable material.

9+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 9:

-  
Infrequent or mild cartoon or fantasy violence

-  
Infrequent or mild profanity or crude humor

-  
Infrequent or mild mature, suggestive, or horror or fear themed

12+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 12:

-  
Infrequent or mild medical or treatment-focused content

-  
Infrequent or mild references to alcohol, tobacco, or drug use

-  
Infrequent or mild sexual content or nudity

-  
Frequent or intense contests

-  
Frequent or intense profanity or crude humor

-  
Frequent or intense horror or fear themed content

-  
Frequent or intense cartoon or fantasy violence

-  
Infrequent or mild occurrences of realistic violence

-  
Infrequent or mild simulated gambling

17+

Apps with this rating may contain instances of the following content that may not be suitable for children under the age of 17:

-  
Unrestricted web access, such as with an embedded browser

-  
Gambling

-  
Frequent or intense simulated gambling

-  
Frequent or intense mature or suggestive content

-  
Frequent or intense medical or treatment-focused content

-  
Frequent or intense references to alcohol, tobacco, or drug use

-  
Frequent or intense sexual content or nudity

-  
Frequent or intense realistic violence

Unrated

Apps with this rating may contain instances of the following content that can’t be published on the App Store. It may be published on alternative app marketplaces or websites:

-  
Infrequent or mild graphic sexual content and nudity

-  
Frequent or intense graphic sexual content and nudity

-  
Infrequent or mild prolonged graphic or sadistic realistic violence

-  
Frequent or intense prolonged graphic or sadistic realistic violence

### Australia regional ratings

As required by Australia’s guidelines for the classification of computer games, apps with Games as the primary or secondary category that have at least one of the following content descriptions will display an additional regional rating along with their Apple global age rating. The relevant regional rating will display on the App Store in Australia for iOS 18, macOS 15, tvOS 18, watchOS 11, and visionOS 2 or later.

Content description

Region-specific rating

App that contains purchasable loot boxes

App with any instances of simulated gambling

If we’re notified by the regulator that your app doesn’t meet their guidelines or requires a regional rating, you’ll receive a message from App Review. If you receive this message, follow the instructions and re-submit your app for review.

### Brazil regional ratings

As required by the Brazilian Ministry of Justice and Public Security (MJSP), the App Store uses a different set of regional rating pictograms and descriptors for self-rated apps, than for ratings officially issued by the MJSP.

Official Brazil regional ratings apply to apps that were issued an official rating and/or descriptors by the MJSP. If a rating or descriptor has been issued to your app by the MJSP, Apple will update your regional rating and/or descriptors on your behalf. The updated regional rating will display on the App Store in Brazil for iOS 16.2, iPadOS 16.2, macOS 13.1, and tvOS 16.2, or later.

Possible values for official Brazil age pictograms are:

Possible values for self-rated Brazil age pictograms are:

### France regional rating

As required by the Agence Nationale des Fréquences ("ANFR"), apps with a 17+ Apple global age rating will display an additional regional rating of 18+ on the App Store in France for iOS 18, macOS 15, tvOS 18, watchOS 11, and visionOS 2 or later.

### Republic of Korea regional ratings

As required by the Korean Games Rating and Administration Committee(GRAC), apps in the Games or Entertainment categories (primary or secondary) and/or apps with Frequent/Intense instances of Simulated Gambling will display an additional regional rating along with their Apple global age rating. The relevant regional rating will display on the App Store in Republic of Korea for iOS 18, macOS 15, tvOS 18, watchOS 11, and visionOS 2 or later.

Possible values for Korea regional ratings are:

Apple global age ratings

Region-specific rating

4+

9+

12+*

* The GRAC may issue a KR-15 regional rating with an updated pictogram, or text that indicates KR-19 regional age rating for some apps.

Note: You’ll receive a message from App Review if the Korean Games Rating and Administration Committee(GRAC) issues an official rating for your app that is different from your app’s age rating. If you receive this notice, follow the instructions in the override age rating for Korea section and re-submit your app for review.

Related Set an app age rating App information Platform version information

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-builds/choose-a-build-to-submit/
### App Store Connect Help

App Store Connect / Manage builds / Choose a build to submit 
Filter ⌘K  
Filter ⌘K  

Manage builds  

# Choose a build to submit

Before submitting an app to App Review, choose a build from those you’ve uploaded for the version. You can only associate one build with each app version. However, you can change the build as often as you want until you submit the version to App Review.

Learn how to submit builds for review with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Add a build to a version

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version under the platform you wish to select.

-  
On the right, scroll down to the Build section, then click the add button (+) next to Build.

The add button (+) appears once you have uploaded builds but have not yet selected one. If a different build is selected than the one you want to submit for review, remove the build.

-  
In the Add Build dialog, select the build you want to submit.

If an earlier version of your app is Ready for Distribution, the list only includes builds you have uploaded since that version was released on the App Store. Learn how to view available builds.

-  
Click Done.

In the Build section, the app icon, build string, and upload date and time appear.

-  
On the top right, click Save.

Note: If you select a build with the Missing Compliance status, you must answer the export compliance questions before submitting for review. Click Manage or Choose File next to the build and answer the questions, or follow the steps to upload app encryption documentation.

### Remove a build from a version

When you remove a build from an app version, it’s not removed from your account.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version under the platform you wish to remove.

-  
On the right, scroll to the Build section.

-  
Hold the pointer over the build, then click the delete button (–) that appears to the right of the upload date.

-  
On the top right, click Save.

Related Upload builds View builds and metadata Maximum build file sizes Overview of publishing your app on the App Store

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/
### App Store Connect Help

App Store Connect / Manage builds / Upload builds 
Filter ⌘K  
Filter ⌘K  

Manage builds  

# Upload builds

Required role: Account Holder, Admin, App Manager, or Developer. View role permissions.

After adding an app to your account, you can upload a build using Xcode, Swift Playground, altool, or Transporter. If you use the App Store Connect API, you might want to upload your binary using the Transporter command-line tool and JSON Web Tokens (JWTs) for authentication. You can use the same JWTs that you use for the API to upload your binary. As your app changes, you can upload more builds, distribute a build for testing, or submit your app for review.

The first time you upload a build, a beta version of the app is created in your account. However, the build needs to be processed in Apple’s system before it appears in App Store Connect. You’ll receive an email when this process is complete.

Each time you upload a build, the bundle ID and version number, which are located in the app bundle, are used to associate the build with the app and version record in App Store Connect. The build string is used to uniquely identify the build throughout the system.

You can also create and upload your build using Xcode Cloud. Xcode Cloud lets you adopt continuous integration and continuous delivery (CI/CD), a standard practice that helps monitor and improve software quality over time, ensuring your app or framework is always in a releasable state. Learn more about Xcode Cloud.

You also have the option to upload assets that are managed separately from a build by using Apple-Hosted Background Assets. Learn more.

Learn about upcoming upload requirements.

## Upload your app binary files with Xcode

Xcode is Apple’s integrated development environment (IDE). You use Xcode to build apps for Apple products, including iPhone, iPad, Mac, Apple TV, Apple Vision Pro, and Apple Watch. Xcode provides tools to manage your entire development workflow—from creating your app to testing, optimizing, and submitting it for review.

To learn how to upload your app binary using Xcode, visit Distributing your app for beta testing and releases, or in Xcode, choose Help > Xcode Help and search for “Distributing your app for beta testing and releases.”

Download Xcode on the Mac App Store.

### Supported Xcode Versions

App Store Connect supports the following versions of Xcode to upload your app for customer distribution or to testers using TestFlight. You can view delivery progress, including warnings, errors, and delivery logs, as well as a history of past deliveries.

Target type

Built using Xcode

Uploaded using Xcode

iOS app

iOS app extension

watchOS app extension

Xcode 26 or later

Xcode 14 or later

macOS app

Xcode 6 or later

Xcode 14 or later

tvOS app

Xcode 26 or later

Xcode 14 or later

visionOS app

Xcode 26 or later

Xcode 15 or later

Upload for all target types is supported for Transporter and altool.

### Upload your app binary files with the App Store Connect API

The App Store Connect API is a REST API that enables the automation of actions you take in App Store Connect.

Calls to the API require JSON Web Tokens (JWT) for authorization; you obtain keys to create the tokens from your organization’s App Store Connect account. Learn how to create API keys to sign JWT.

You can upload your app binary with the App Store Connect API. Learn more.

### Upload your app binary files with altool

You can use xcrun, included with Xcode, to invoke altool, a command-line tool that lets you validate and upload your app binary files to App Store Connect. Specify one of the following in Terminal at the command-line:

$ xcrun altool --validate-app -f file -t platform -u username [-p password] [--output-format xml] 
$ xcrun altool --upload-app -f file -t platform -u username [-p password] [--output-format xml]  
Learn more about using altool. 

### Upload your app binary files with Transporter

Transporter is a macOS app that provides a simple and easy way to upload an app to App Store Connect for distribution. You can view delivery progress including warnings, errors, delivery logs, and a history of past deliveries.

You can download the latest version of Transporter on the Mac App Store.

Learn more about Transporter Help.

Related View builds and metadata Choose a build to submit Maximum build file sizes App build statuses TN3147: Migrating to the latest notarization tool

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/maximum-build-file-sizes/
### App Store Connect Help

App Store Connect / Reference / App uploads / Maximum build file sizes 
Filter ⌘K  
Filter ⌘K  

Reference  

# Maximum build file sizes

Verify that your app, along with each Mach-O executable file (for example, app_name.app/app_name), doesn’t exceed the maximum file size limits on the supported operating systems.

For iOS, iPadOS, macOS, tvOS, and visionOS apps, you can use Background Assets to host larger assets that are managed separately from your build.

The size shown on your App Store product page varies depending on the device that’s viewing the page. On macOS, the product page shows the the universal installation size. On all other platforms, it shows the installation size for the specific device model. If your app uses Apple-Hosted Background Assets, the product page shows an “Up to” size that also includes any non-localized essential asset packs and the localized essential asset packs for the single language with the largest total size.

Learn how to view the file sizes of an uploaded build.

Platform

Minimum deployment target

Maximum uncompressed app size

Maximum executable file size

iOS and iPadOS

iOS 9.0 and later

iOS 7.X through iOS 8.X

Earlier than iOS 7.0

4 GB

500 MB 1

60 MB 2

80 MB 1

macOS

All macOS versions

200 GB

tvOS

tvOS 9.0 and later

4 GB

500 MB 1

visionOS

visionOS 1.0 and later

4 GB

500 MB 1

watchOS

All watchOS versions

75 MB

1 For the total of all __TEXT sections in the binary.

2 For the __TEXT sections in each architecture slice. An architecture slice is a part of the fat binary layout that targets a specific architecture. For example, a fat binary might include slices for 32-bit and 64-bit architectures.

## App Clips

To ensure a successful launch experience, verify that the uncompressed main bundle of any App Clip variant, after app thinning, doesn’t exceed the maximum size limit for the minimum deployment target used in the App Clip.

Learn how to measure the size of your App Clip.

Minimum deployment target

Maximum variant size

Notes

iOS 17 and later

100 MB

Following requirements must be met:

-  
The App Clip only supports digital invocations — for example, from your website or Spotlight search — and not from physical invocations like App Clip Codes, QR codes, or NFC tags.

-  
People use your App Clip in situations where a reliable internet connection is likely, for example, at home.

-  
Your App Clip doesn’t support iOS versions prior to iOS 17.

iOS 16 and later

15 MB

Earlier than iOS 16

10 MB

Related Add testers to builds Upload builds What is app thinning? (iOS, tvOS, watchOS) Gathering information about memory use Reducing your app’s size

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/app-information/
### App Store Connect Help

App Store Connect / Reference / App information 
Filter ⌘K  
Filter ⌘K  

Reference  

# App information

App information refers to the properties that are shared across the platforms added to an app. Some of these properties are set when you add the app to your account, and later, you can edit app information as needed based on the app's status.

Learn how to make the most of your product page on the App Store.

Property

Description

Name

The localized name of your app as it appears on App Store product pages and when users install your app. The name must be at least two characters and no more than 30 characters. You can edit it until you submit the app to App Review. Later, you can change the name when you create a new version or the status of the app version permits editing this property.

Subtitle

A summary of your app that appears under your app's name on your App Store product page. This can’t be longer than 30 characters.

Privacy Policy URL

A URL that links to your company’s privacy policy. Required for iOS and macOS apps. If your app has a tvOS platform, the text of your privacy policy in the Apple TV Privacy Policy field is required.

Bundle ID

A unique identifier for your app that is used throughout the system. (A build is uniquely identified by the combination of the bundle ID, version number, and build string.) You can’t change this property after you upload a build.

Important: The Bundle ID property must match the bundle ID you set in the Xcode project.

SKU

A unique ID you give to your app for internal tracking that's not visible to customers. The SKU can contain letters, numbers, hyphens, periods, and underscores but not start with a hyphen, period, or underscore. You can’t change the SKU after you add the app to your account.

Apple ID

A unique identifier automatically generated for your app when you add the app to your account. You can view this property in the App information section in App Store Connect. This identifier is also used in the URL for the App Store on desktop computers. You can’t edit this property.

Content Rights

Apps that contain, show, or access third-party content must have all the necessary rights to that content or be otherwise permitted to use it under the laws of each App Store country or region in which they’re available. Learn more about the App Store guidelines.

Age Rating

The age rating of your app for the purpose of parental controls. Note that the rating is set at the app level in the App information section and is applied across all platforms. Learn more about the age rating values. This property is required.

Made for Kids

An indication that the app appears in the Kids category on the App Store. This property includes an age range set for the app. Once an app marked as Made for Kids is approved by App Review, this selection cannot be changed and all subsequent updates will need to follow the Kids category guidelines.

License Agreement

Apple provides a standard EULA (End-User License Agreement) that applies in all regions. You may provide a custom license agreement that supersedes the Apple EULA for one or more regions.

Primary Language

The default language for the metadata that appears on App Store product pages, and is displayed when users install your app, when you don't provide localized metadata for a given country or region. You can change the primary language at any time.

Category (Primary and Secondary)

The categories that best describe your app.

For macOS apps, you also set the app category in Xcode. The primary category you set in App Store Connect should match the category you set in Xcode.

For more information, visit Choosing a Category.

Subcategory

If you select Games or Stickers as the Primary or Secondary Category, you can also select one or two subcategories to help more accurately define your game or stickers app.

Availability in the Republic of Korea - Rating Classification Number

If your app meets one or more of the following characteristics, a Rating Classification Number from the Game Rating and Administration Committee (GRAC) is required in order to offer it on the App Store in the Republic of Korea.

-  
App has been given the KR-19 regional rating by GRAC.

-  
Apps in the Casino subcategory with age rating 17+

-  
Apps in the Games or Entertainment categories with a Frequent/Intense level of frequency in at least one of the following content descriptions:

-  
Simulated Gambling

-  
Sexual Content or Nudity

-  
Alcohol, Tobacco, or Drug Use or Reference

-  
Realistic Violence

Please note that this field will display if your app is in the Games or Entertainment category with a rating of 17+, but is only required if your app meets the above criteria.

Availability in China mainland

Chinese law requires additional documentation for some apps to be available on the App Store in China mainland.

China’s Ministry of Industry and Information Technology (MIIT) requires that some apps possess a valid Internet Content Provider (ICP) Filing Number. The ICP number and metadata on the App Information page should match with the information you have filed with MIIT. This match is required for your Simplified Chinese localization; if not configured, then it should match your primary language. Once the provided ICP Filing Number is verified and saved, it will be displayed on your App Store product page.

In addition, games must secure an approval number and apps with books and magazine content must secure an internet publishing permit from China’s National Press and Publication Administration (NPPA). Apps with religious content must secure an Internet Religious Information Permit from China’s National Religious Affairs Administration (NRAA). Apps with news content must obtain an Internet News Information Permit from the Cyberspace Administration of China (CAC). If you offer or plan to offer any of these on the App Store in China mainland, you must provide the required information along with one or more supporting documents.If applicable, provide the required ICP filing information in the designated section under the “App Information” tab. To help verify your approval number, upload your game’s ISBN Issuing Letter or Approval Reply, and a copy of your latest Business License. Additionally, you can include an authorization agreement from the matching operator. To help verify your publishing permit, upload your internet publishing permit or other relevant permit from the NPPA, a publishing permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation. To help verify your Internet Religious Information Permit, upload your Internet Religious Information Permit, a permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation. To help verify your Internet News Information Permit, upload your Internet News Information Permit, a permit authorization letter from the authorizing party, a business license, an ICP license, or similar supporting documentation.

Learn more about approval numbers from the NPPA.

Learn more about internet publishing permits.

Learn more about Internet Religious Information Permits.

Learn more about Internet News Information Permits.

Learn more about ICP Filing Number.

Availability in Vietnam

Vietnamese regulators require games distributed in Vietnam to be licensed to remain available on the App Store in Vietnam.

To learn more about the game license, review the regulations on licensing game publishing in Vietnam.

URL for App Store Server Notifications

If your app offers In-App Purchases, you can receive server notifications from the App Store about key events by setting up an optional URL that links to your server. Learn how to enable App Store Server Notifications.

Digital Services Act (DSA)

You’ll be asked to disclose whether or not you’re a trader under the European Union’s Digital Services Act (DSA) in order to distribute apps in the EU. If you’re a trader, the DSA requires that you provide certain identification information, including your address and contact details, to be displayed on your App Store product pages to consumers in the EU. You also have the option to provide a labels and markings URL. Learn more.

Regulated Medical Devices

Apps that are available in the EU/EEA, UK, or U.S., and have a primary or secondary category of Health & Fitness or Medical, or that have "frequent" Medical or Treatment information listed in the age rating, are required to complete this declaration.

Learn more about regulated medical devices in the EU/EEA.

Learn more about regulated medical devices in the UK.

Learn more about regulated medical devices in the US.

Related Add a new app View and edit app information Platform version information Required, localizable, and editable properties

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/
### App Store Connect Help

App Store Connect / Reference / App information / Platform version information 
Filter ⌘K  
Filter ⌘K  

Reference  

# Platform version information

## Platform version information

Platform version information refers to the set of properties of an app version specific to each platform the app supports.

View product page marketing guidelines.

Property

Description

Language

The language you choose to localize your metadata. This property is editable depending on the app status.

Screenshots

Screenshots that show what your app looks like on a device. Learn about the screenshot specifications.

This property is required and can be localized.

App Preview

An app preview is an optional short video demonstrating your app. You may add up to three app previews for each localization, per device size. Learn about the app preview specifications.

Promotional Text

Promotional text lets you inform your App Store visitors of any current app features without requiring an updated submission. This text will appear above your description on the App Store for customers with devices running iOS 11 or later. This property can’t be longer than 170 characters.

Description

A description of the app, detailing the features and functionality. Limited to 4000 characters. The description should be in plain text, with line breaks as needed. HTML format isn't supported.

This appears on your app’s product page, when users install your app, and will be used for web engine search results once you release your app.

This property is required and can be localized.

Keywords

One or more keywords (each greater than two characters) describing your app. You can provide up to 100 bytes of content. Your app is searchable by app name and company name, so you shouldn't duplicate these values in the keyword list. Names of other apps or companies aren't allowed.

This property is required and can be localized.

Support URL

The URL of the support website you plan to provide for users, which displays on the App Store for users who have downloaded your app. This URL must lead to actual contact information (legal address, email address, telephone number), as may be required by local law, so that users can reach you regarding app issues, general feedback, and feature enhancement requests. Specify the entire URL, including the protocol (for example, http://support.example.com).

If you need to provide a Software Bill of Materials (SBOM), you can include it on your support site.

This property is required and can be localized.

Marketing URL

The website where users get more information about the app. Specify the entire URL, including the protocol.

This property can be localized.

Version Number

The version number that's provided for your app that appears on App Store product pages and is displayed when users install your app.

Copyright

The name of the person or entity that owns the exclusive rights to the app, preceded by the year the rights were obtained (for example, 2014 Example, Inc.). The copyright symbol is added automatically.

This property is required.

Routing App Coverage File

A routing app’s geographic coverage file (a file with a .geojson file extension) that specify the geographic regions supported by your app.

The file can have only one MultiPolygon element. MultiPolygon elements consist of at least one Polygon. Polygons contain at least four coordinate points. The start and end coordinate points for a polygon must be the same. For file specifications, read “Specifying the Geographic Coverage File Contents” in Location and Maps Programming Guide.

Version Release Settings

Determines how the app version will be released. The following settings are allowed:

-  
Manual. When the app status changes to Pending Developer Release after approval and you must manually release the version.

-  
Automatic. The app goes live automatically after it is approved by App Review.

-  
Automatic, no earlier than. If the date hasn't passed when the app is approved, the app status changes to Pending Developer Release, but is automatically released at the date specified.

What’s New in this Version

A description of the changes in this version of the app, such as new features, UI improvements, or bug fixes. Limited to 4000 characters.

We recommend that you provide detailed information to let users know the specifics of the changes, improvements, or fixes in the version.

This property isn't available for the first version of the app but required for all subsequent versions. This property can be localized.

Phased Release for Automatic Updates

When you release a version update of your app, you can choose to release your iOS app in stages. If you choose this option, your version update will be released over a 7-day period to a percentage of your users on iOS with automatic updates turned on. Learn how to release a version update in phases.

Reset Overview Rating

You can reset your app’s overview rating when you release a new version. Learn how to reset overview rating.

### App Review information

You must provide the following information to App Review. It isn’t visible to customers and can be edited at any time.

Submissions that include an app version will be reviewed together with the App Review information for that version.

Submissions that don’t include an app version, or those that include items associated with multiple platforms, will be reviewed together with the App Review information for the latest approved version of the platform you specify during the submission process. To edit the App Review information on an approved app version, click Edit in the top right corner of the App Review Information section.

Property

Description

Required

Contact:

Name, email, phone number

Information for the contact person in your organization if the App Review team needs additional information.

Enter the phone number in international format, including a plus sign (+) followed by the country code (for example, +852 for Hong Kong) — the field doesn't accept numbers-only entry.

Notes

Additional information about your app that can help during the review process. Include information that may be needed to test your app, such as app-specific settings and test registration or account details. If your app delivers streaming video over the cellular network, enter a test stream URL. The Notes field can contain up to 4000 bytes. You can write notes in any language.

Sign-in required:

Username and password

Sign-in information for a demo account. If your app uses a single sign-on service, such as Facebook or Twitter, include the demo account login information for it. The demo account is used during the App Review process and must not expire. Details for additional accounts should be included in the Notes field.

If your app requires a login to use it.

Related App information Required, localizable, and editable properties

=== SOURCE: https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations
Complying with Encryption Export Regulations | Apple Developer Documentation                              

# This page requires JavaScript.

Please turn on JavaScript in your browser and refresh the page to view its content.

## Automated tools and assistive tools:

A Markdown version of the page content is available: View Markdown

=== SOURCE: https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/
### App Review Help

App Review / Before submitting for review / Provide information for a complete review 
Filter ⌘K  
Filter ⌘K  

Before submitting for review  

# Provide information for a complete review

Add everything App Review needs to complete its review in the App Review information section of App Store Connect, including:

-   General information about the app's concept, features, and intended audience 

-   Demo account credentials for account-based features 

-   Required documentation for regulated fields 

Submitting all required information and documentation up front can ensure a faster and more predictable review. Incomplete submissions will be rejected.

## Provide information about the app

Tell App Review about your app in general, covering who it's for and how it works:

-  
New apps: Describe your app's concept and business model.

-  
Updates: Describe what's changed, and where reviewers can find significant new content or features.

-  
Purpose and audience: Describe the app's purpose and target audience.

-  
Devices and OS versions tested: List the device models and operating systems you tested the app on before submitting.

-  
External services and platforms: List the external services, tools, or platforms the app uses to deliver its core functionality (for example, data providers, authentication services, payment processors, or AI services).

-  
Required hardware: Apps with required hardware must provide a video (not a screen recording) that shows your app running on a physical Apple device as it pairs and interacts with the hardware.

-  
Regional differences: Describe any regional differences in the app's features or content, or confirm that the app functions consistently across all regions.

## Provide demo accounts

Add up-to-date demo account login credentials:

-  
Enter a username and password that work at the time of submission. Credentials that expire or change before your review starts may result in the submission being rejected.

-  
If your app has multiple account types, such as administrative and general user accounts, use the Notes field to add additional credentials for each type.

-  
If your app offers auto-renewable subscriptions, provide a demo account with an expired subscription to enable review of the entire purchase flow.

-  
If your app requires an authentication code in addition to or instead of login credentials, include it in the Notes field in advance. Without it, a call may be required to continue the review. Calls are typically completed within three to five business days.

## Provide required documentation

Developers with apps operating in regulated fields must provide documentation demonstrating they are qualified and authorized to provide those services. If the app is available in multiple countries and regions, developers may need to provide additional documentation for each location where the app is distributed. Similarly, developers with apps containing protected content must show they have permission to include it in the app.

Provide required documentation, which can vary by app type:

-  
Medical apps that make diagnostic or treatment claims: Regulatory clearance for each country or region where the app is available, such as FDA, CE, or CFDA documentation, or a supporting test report or peer-reviewed study.

-  
Cryptocurrency exchange apps: A cryptocurrency exchange license for each country or region where the app is available, plus partnership documentation if you're working with a third-party exchange.

-  
Financial apps, including apps that offer loans: Documentation showing your partnership with the licensed financial institution or lender providing the underlying service.

-  
Apps offering gambling, lotteries, or real-money gaming: The applicable gambling or lottery license for each storefront where your app is available.

-  
Apps that use another party's intellectual property: Trademark or rights documentation, such as a signed contract, or email correspondence showing you have permission.

If your app falls into one of these categories, attach everything App Review will need to complete its review in the App Review Information section before you submit.

If you're unsure what information your app's review needs, consider requesting a one-on-one appointment to discuss your app's concept before you submit.

### Documentation examples by guideline

App Review Guideline

Documentation typically requested

1.4.1: Diagnosing or Treating Patients

Regulatory clearance (FDA, CE, or CFDA documentation); a supporting test report or peer-reviewed study.

1.4.3: Cannabis, Alcohol, and Illegal Substances

Cannabis dispensary license.

1.7: Reporting Criminal Activity

Documentation confirming the developer's partnership with law enforcement or a government entity, printed on that entity's official letterhead.

2.1: Registration Verification

International Standard Book Number (ISBN) or GRN documentation (China).

3.1.5: Cryptocurrencies

Cryptocurrency exchange license; partnership documentation if you're leveraging a third-party exchange partner; legal opinion.

3.2.1: Financial Apps

Documentation showing your partnership with the financial institution or bank providing the underlying service.

3.2.1 / 3.2.2: Apps Offering Loans

Loan license; business license; partnership documentation demonstrating the formal agreement between you and a licensed lender.

4.1 / 5.2.1 / 5.2.3: Third-party trademarks, copycat concepts, fan apps, sports and sporting events, specific marks, audio/video/music, and apps that download or stream third-party content

Trademark or rights documentation, such as a signed contract, electronic communication (emails, messaging-service screenshots), video recordings, or licensing documents.

5.0: Published Works for Sale in China

Publication permit; Internet Publishing License; Internet Culture Operations Permit; Operating License of Publication; Radio and Television Program Production license, where applicable.

5.1.1: Verifying Seller and Company

Partnership evidence, for example with an insurance company, brokerage, or applicable government body.

5.1.3: Health and Human Research

Ethics Review Board or Institutional Review Board (IRB) approval; human research consent form.

5.3.3: Lotteries and Raffles

Gambling license; SUSEP and SECAP documents (Brazil); lottery app license (China).

5.3.4: Gambling

Gambling license.

### Use a demonstration mode when appropriate

If your app handles sensitive user information, or operates in a highly regulated industry, you can implement a demonstration mode instead of providing a demo account. A demonstration mode should show your app's full features and functionality using demonstration data.

Related Request a one-on-one App Review appointment Manage App Review information with the App Store Connect API Test your app on compatible devices

=== SOURCE: https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review/
### App Review Help

App Review / After submitting for review / Request an expedited review 
Filter ⌘K  
Filter ⌘K  

After submitting for review  

# Request an expedited review

App Review works around the clock with the goal of reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours. However, if you're facing extenuating circumstances, such as fixing a critical bug or timing your release to coincide with an event, you can request an expedited review.

-  
Submit the app for review in App Store Connect. Only submissions that have already been sent to App Review can be expedited. Make sure the app is ready for review by adding all required information in the Notes field and providing a demo account or demo mode for account-based features.

-  
Go to Request an Expedited App Review, select the app and platform which you would like to receive an expedited review, and submit.

-  
App Review will evaluate your request and expedite the app's review as allowed by availability and demand.

Note: Expedite requests should be reserved for matters of genuine urgency.

### Critical bug fixes

If you're requesting an expedited review to fix a critical bug, include this information in the Notes field in App Store Connect when you submit the app for review.

### Event-related apps

If you're requesting an expedited review to align the app's release with an upcoming event, include the event, its date, and how your app is associated with it in the Notes field in App Store Connect when you submit the app for review. Schedule its release in App Store Connect ahead of time if you can.

Related Track a submission's review status Contact App Review for help with a submission

=== SOURCE: https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board/
### App Review Help

App Review / After submitting for review / Appeal to the App Review Board 
Filter ⌘K  
Filter ⌘K  

After submitting for review  

# Appeal to the App Review Board

If you disagree with the outcome of a review, you can file an appeal with the App Review Board. It's appropriate to file an appeal when:

-  
Your app was rejected or removed, but you believe it follows the App Review Guidelines and the Apple Developer Program License Agreement.

-  
Your account is facing termination, but you believe it complies with the App Review Guidelines and the Apple Developer Program License Agreement.

-  
You believe you experienced unfair or biased treatment during review.

Note: Don't file an appeal to reinstate an already-terminated account, get a status update on your app, or request an expedited review. For these requests, use the appropriate Contact Us form instead.

-  
Before filing an appeal, reply to the rejection, removal, or termination message you received in App Store Connect and provide clarification about the issue. If this clarification is not sufficient to resolve the issue, proceed with filing an appeal.

-  
Go to Submit an appeal to App Review and describe why you believe your app or account follows the App Review Guidelines and the Apple Developer Program License Agreement.

For app rejections or removals, point to the specific requirements involved and explain how your app satisfies them.

For account terminations, reference the specific terms your account was found to be violating, and explain how your account meets those requirements. If the termination references other guideline violations you believe were in error, provide an additional explanation of those instances as well.

-  
The App Review Board will send you a message in App Store Connect once its investigation is complete. They may also message you in App Store Connect to request additional information or schedule a call to discuss the outcome of the investigation.

Note: Only submit one appeal per rejected or removed app. If an app's rejection or removal message cites multiple guideline violations, address all of them in one appeal.

## What to include in your appeal

#### Do

-  
Cite the specific guideline or terms your app was rejected or removed under, and explain point by point how your app meets it.

-  
Include additional information about your app that is relevant to the rejection, removal, or pending termination decision you're disputing.

-  
Use the form to submit appeals for up to five rejected or removed apps.

#### Don't

-  
Don't file an appeal for requests from App Review for additional information or documentation about your app. This information is necessary for App Review to complete the review.

-  
Don't include information that is not relevant to the rejection, removal, or pending termination decision you are appealing.

-  
Don't file an appeal if you've addressed the issues App Review identified and resubmitted the app for review.

#### Example (Complete)

"My app was rejected under Guideline 2.1 for incomplete information. The demo account and setup steps needed to test the flagged feature are included in the App Review Information section of this submission, along with screenshots showing the feature working as described."

#### Example (Incomplete)

"This app is important to my business and shouldn't have been rejected. Please take another look."

Note: Appeals that include all required information help the App Review Board process your request quickly. Submitting a complete appeal does not guarantee that the App Review Board will overturn the rejection, removal, or termination.

Related App Review Guidelines Apple Developer Program License Agreement Contact App Review for help with a submission Track a submission's review status Request an expedited review

=== SOURCE: https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review/
### App Review Help

App Review / After submitting for review / Contact App Review for help with a submission 
Filter ⌘K  
Filter ⌘K  

After submitting for review  

# Contact App Review for help with a submission

If a submission doesn't pass review, you'll receive a message from App Review in App Store Connect detailing the issues requiring your attention.

If you have questions, contact App Review directly by clicking Reply to App Review in App Store Connect. Using App Store Connect to contact App Review is the best way to receive assistance with an ongoing submission. A specialist familiar with your app will reply to your message.

## What to include in your reply to App Review

#### Do

-  
Be specific about what you're asking, such as the exact feature, guideline, or step you need clarified.

-  
Provide additional information that can help App Review understand the app's concept and intended functionality if you believe your app was misunderstood.

#### Don't

-  
Don't use the Reply to App Review field to appeal a rejection or removal or to request an expedited review. For these requests, use the appropriate Contact Us form instead.

-  
Don't ask about the status of apps from other developers. Just as App Review wouldn't discuss your app with someone else, App Review can't discuss other developers' apps with you.

### Request a call with an Apple representative

If you need additional assistance after App Review replies to your message, you can use the Reply to App Review message window to request a call with an Apple representative.

Before requesting a call, confirm your contact details in the App Review Information section of App Store Connect are up to date.

When requesting a call, include your time zone so App Review can attempt to call during your local business hours. You can also specify a preferred language for the call. App Review will try to accommodate your request, though availability can vary. Calls are typically completed within three to five business days.

Related Accept Bug Fix Submission offers Appeal to the App Review Board Request an expedited review

=== SOURCE: https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions/
### App Review Help

App Review / After submitting for review / Accept Bug Fix Submission offers 
Filter ⌘K  
Filter ⌘K  

After submitting for review  

# Accept Bug Fix Submission offers

If a bug-fix update is rejected but introduces no legal or safety concerns, you can choose to resolve the issues in your next submission. This process allows you to deliver bug fixes quickly, giving you time to resolve any outstanding issues in your next submission.

Note: Bug Fix Submission offers are only available for updates to apps that have been previously approved for the App Store or alternative distribution.

-  
In App Store Connect, open the rejection message. If your submission is eligible, this language will appear at the top of the message:

"Bug Fix Submissions: The issues we've identified below are eligible to be resolved on your next update."

-  
If you see the note, reply to the message and let App Review know you'd like the current submission approved and will address the issues in your next update. Do not resubmit the app at this time, as it will trigger a new review.

If you don't see the note, the submission doesn't qualify, and you'll need to resolve the issues before the submission can be approved.

-  
App Review will reply to confirm and approve the submission.

-  
In your next update, resolve all deferred issues from the prior submission. App Review will verify that each issue has been addressed before approving the update.

Note: Issues that were deferred on a previous submission aren't eligible to be deferred again on the next submission.

Related Contact App Review for help with a submission

=== SOURCE: https://developer.apple.com/help/app-review/after-submitting-for-review/review-status/
### App Review Help

App Review / After submitting for review / Track a submission's review status 
Filter ⌘K  
Filter ⌘K  

After submitting for review  

# Track a submission’s review status

App Review works around the clock with the goal of reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours. While updates with minor changes and bug fixes typically move through review quickly, other submissions may take longer to verify.

## Check your submission status

You can check the status of a submission at any time by visiting the App Review section of App Store Connect. Track the status of all your submitted items in one place, including your app versions, In-App Purchases, custom product pages, and more.

Your submission will display one of several statuses during the review process, including:

-  
Waiting for Review: Apple received your submission, but review hasn’t started. You can still edit certain information or remove items from the submission, though you can’t upload or edit screenshots and app previews.

-  
In Review: App Review is reviewing your submission. You can cancel the submission to remove it from review.

-  
Unresolved Issues: App Review identified issues with one or more items in the submission.

For the full list of app, submission, and item statuses, see App and submission statuses.

You can also set up webhooks to receive automatic server notifications whenever a submission’s status changes.

## When to resubmit for review

In general, reserve resubmissions for changes that require a new review.

It’s not necessary to resubmit when:

-  
App Review requested more information and there are no other issues to resolve. Instead, you can reply directly to the message in App Store Connect. Resubmitting starts a new review, after which App Review can no longer reply to your previous message.

-  
Issues can be resolved by revising metadata or making server-side adjustments, such as providing or activating demo credentials. Reply to App Review in App Store Connect once the required changes have been made.

-  
You’ve been offered and want to accept approval for a Bug Fix Submission. Reply to the message to accept the offer without resubmitting. Learn more about accepting Bug Fix Submission offers.

-  
You’re appealing a rejection or removal to the App Review Board. Resubmitting will initiate a new review and the appeal will be closed. Learn more about appealing to the App Review Board.

It’s appropriate to resubmit when:

-  
The submission is rejected for an issue in the build and you’ve fixed it. Upload the new build and submit that version. This starts a full review of the new build.

-  
Some items in the submission were rejected, others were accepted, and you want to move ahead with approval on the accepted items. Remove the rejected items and resubmit.

Note: Don’t resubmit until you’ve resolved every issue identified by App Review. Resubmitting with unresolved issues delays review and results in the same outcome. If you have questions about how to resolve an issue, contact App Review for help with a submission.

### Why some reviews take longer

Most submissions are reviewed within 48 hours. Some need additional time for verification, particularly those involving the following:

-  
Limited review history: Apps with little or no prior App Review history.

-  
Required documentation: Authorizations, licenses, partnership agreements, or other materials App Review must confirm before approval.

-  
Complex or novel issues: Regulated content, new platform capabilities, enabled entitlements, or other sensitive features that require greater scrutiny.

To help reduce review time, provide information about your app and attach all required documentation in the App Review Information section before submitting. Learn more about providing information for a complete review.

### When fraud or malicious activity is detected

To protect the App Store’s high standards for privacy, security, and quality, App Review has a zero-tolerance policy for fraudulent or malicious activity. App Review investigates all reported or identified conduct that falls outside the Developer Code of Conduct, which requires accurate representation and integrity across the app ecosystem. An investigation can extend a submission’s review. Examples include:

-  
Misrepresented developer identity or impersonation, such as providing inauthentic documentation. (Guidelines 4.1 and 5.6.2)

-  
Manipulation of the App Store experience, including gaming charts, search results, reviews, or referrals, or attempting to hide features in review. (Guidelines 2.3.1(a) and 5.6.3)

-  
Submitting low-quality apps, as indicated by excessive customer reports such as negative customer reviews and high-volume refund requests. (Guidelines 4.3 and 5.6.4)

When these signals appear, App Review investigates thoroughly. Repeated or serious violations can lead to additional rejections, app removals, and removal of your account from the Apple Developer Program.

Related Provide information for a complete review Contact App Review for help with a submission Request an expedited review App and submission statuses

=== SOURCE: https://developer.apple.com/help/app-review/before-submitting-for-review/app-review-appointment/
### App Review Help

App Review / Before submitting for review / Request a one-on-one App Review appointment 
Filter ⌘K  
Filter ⌘K  

Before submitting for review  

# Request a one-on-one App Review appointment

If you have questions about the review process, you can request to meet with App Review over Webex. In each 30-minute video appointment, you can ask for advice on what to expect during review, how your app can best align with guidelines, reasons for common rejections, and topics related to the process of reviewing your app for distribution.

## How to request an App Review appointment

-  
Request an appointment on the Meet with Apple schedule page. Appointments are subject to availability during your local business hours on Tuesdays and Thursdays.

-  
In your request, include your app's Apple ID from App Store Connect (if you have one) and the specific questions you'd like to discuss.

-  
Discuss your app with an App Review expert during the appointment. Appointments are conducted on video over Webex; having your camera on is optional.

Note: A Meet with Apple appointment is informational. It doesn't replace, expedite, or guarantee the outcome of your app's review.

## Tips about appointment requests

#### Do

-  
Request an appointment if you're unsure how a specific guideline applies to your app, or want general guidance on how to prepare an app for review.

-  
Come with specific questions so App Review can provide useful feedback in the time available.

-  
Keep in mind every submission is evaluated against the App Review Guidelines at the time of review, so App Review cannot preapprove apps or specific features during your appointment.

#### Don't

-  
Don't consider an App Review appointment a replacement for reading the App Review Guidelines yourself.

Related Provide information for a complete review Contact App Review for help with a submission

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/
### App Store Connect Help

App Store Connect / Manage compliance information / Manage European Union Digital Services Act trader requirements 
Filter ⌘K  
Filter ⌘K  

Manage compliance information  

# Manage European Union Digital Services Act trader requirements

Articles 30 and 31 of the Digital Services Act (DSA) require Apple to verify and display trader contact information for all traders distributing apps on the App Store in the European Union (EU). This includes an address, phone number, and email address that you provide to Apple for the purpose of posting on your App Store product page in accordance with the DSA. Once verified, Apple will publish this information on your App Store product page when your app is distributed in any of the 27 territories of the EU. Even if you don’t distribute apps in the EU, you’ll still need to declare a trader status.

If you haven't already confirmed your trader status, next time you submit a new app in App Store Connect you’ll be asked to disclose whether or not you’re a trader in connection with the DSA in order to stay compliant across territories when distributing on the App Store. You'll need to confirm your trader status if you have at least one app on the App Store in the EU that qualifies you as a trader. You’ll then have the option to turn off or specify your trader status for each specific app that you distribute. If you’re not a trader, consumers in the EU will be informed that consumer rights stemming from applicable consumer protection laws won’t apply to contracts between you and them.

## Trader self-assessment

You must assess whether you're a trader for EU law purposes. If you don't distribute apps on the App Store in the EU (for example you only distribute apps through alternative distribution, or TestFlight, or on the App Store only outside the EU), you're not acting as a trader on the App Store. Apple can't determine whether you're a trader.

## How to know if you’re a trader

The DSA defines a trader as “any natural person, or any legal person irrespective of whether privately or publicly owned, who is acting, including through any person acting in his or her name or on his or her behalf, for purposes relating to his or her trade, business, craft or profession.”

The European Commission (EC) has issued a Notice on what constitutes a trader (See Section 2.2. “Concept of Trader"), though it is not specific to digital commerce. The EC has also published Guidance in the digital commerce context, from the perspective of when an ”influencer“ may be considered a trader.

To determine if you're a trader, you should consider a range of non-exhaustive and non-exclusive factors (see those listed on page 2 in the EC’s Guidance), which may include:

-  
Whether you make revenue as a result of your app, for example if your app includes In-App Purchases, or if it's a paid or ad-sponsored app — especially if you're transacting in large volumes;

-  
Whether you engage in commercial practices towards consumers, including advertising, or promoting products or services;

-  
Whether you're registered for VAT purposes; and

-  
Whether you develop your app in connection with your trade, business, craft, or profession—meaning that you’re acting in a professional/business capacity. You're unlikely to be a trader for EU law purposes if you're acting “for purposes which are outside your trade, business, craft, or profession.” For example, if you're a hobbyist and you developed your app with no intention of commercializing it, you may not be considered a trader.

Regardless of whether you’re an individual developer or organization, if you have a legal status associated with a business activity, that would suggest you may be a trader.

The material contained herein is informational, general in nature, and does not constitute legal advice. If you're uncertain about your status as a trader, consult with your legal advisor.

## Information you need to provide if you're a trader

The information you need to provide depends on whether you’re enrolled in the Apple Developer Program as an individual or organization.

Organizations: The address associated with your D-U-N-S Number will automatically display. You’ll need to enter the following for display on your App Store product pages:

-  
Phone number

-  
Email address

This information is for display purposes only and won’t impact the information associated with your Apple Developer Program membership. If you need to update your physical address, contact us.

Individuals: You’ll need to enter the following for display on your App Store product pages:

-  
Address or P.O. Box

-  
Phone number

-  
Email address

This information is for display purposes only and won’t impact the information associated with your Apple Developer Program membership.

All traders: You’ll need to provide payment account details, if you haven’t already entered them in App Store Connect. You'll also be asked to certify that you only offer products or services that comply with the applicable rules of EU law.

### Enter EU Digital Services Act compliance information

Required role: Account Holder or Admin. View role permissions.

-  
Select Business at the top of the page.

-  
On the Agreements tab, scroll down to the Compliance section.

-  
Next to Digital Services Act, click Complete Compliance Requirements.

-  
Select from the following options:

-  
“This is a trader account.” You’ll need to enter contact information for display on your App Store product pages. Continue to step 5.

Note: You’ll still have the option to turn off your trader status for specific apps later.

-  
“This is not a trader account.” You won’t need to provide any contact information. Click Done.

-  
Enter or confirm the required contact information and click Next.

-  
Validate the email address you provided using two-factor authentication. Once you’re done, you’ll automatically be directed to the next step.

-  
Validate the phone number you provided on the previous screen using two-factor authentication. Once you’re done, you’ll automatically be directed to the next step. If you're using a phone number that can't receive two-factor authentication codes, you can request manual verification.

-  
Follow the instructions to upload your documentation. You’ll need to provide a current document that verifies your business name and address. Acceptable documents include business or legal records. If you’re displaying an alternate address, such as a P.O. Box, you’ll also need to provide documentation that reflects your association with this alternate address (for example, a receipt or bill). When you’re done, click Next.

-  
Review your information to make sure it’s correct, then click Confirm.

### Enter app-specific EU Digital Services Act compliance information

Required role: Account Holder and Admin. View role permissions.

If you need to change your trader status for one or more of your individual apps, you can do so.

-  
In Apps, select your app from the list.

-  
In the left sidebar, click App Information.

-  
Scroll to the App Store Regulations and Permits section.

-  
Under Digital Services Act, click Edit.

-  
In the pop-up window, change your trader status for that app. If you’re declaring yourself a trader for the first time, you’ll need to enter and verify your contact information that displays on your app’s App Store product page.

### Enter labels and markings URLs

Required role: Account Holder and Admin. View role permissions.

Under the Digital Services Act, you have the option to provide a Labels and Markings URL to display labels or markings required by European Union law. This URL will be visible on your App Store product pages for apps where you have identified as a trader.

-  
In Apps, select your app from the list.

-  
In the left sidebar, click App Information.

-  
Scroll to the App Store Regulations and Permits section.

-  
Click Add Labels and Markings.

-  
In the pop-up window, enter the URL and click Done. You can edit this URL at any time.

=== SOURCE: https://developer.apple.com/news/upcoming-requirements/
## iOS and iPadOS minimum system requirements

Since September 9, 2026

iOS and iPadOS apps uploaded to App Store Connect must target iOS 13 or later.

Learn about submitting apps

## SDK minimum requirements

Since April 28, 2026

Apps uploaded to App Store Connect must be built with Xcode 26 or later using an SDK for iOS 26, iPadOS 26, tvOS 26, visionOS 26, or watchOS 26.

Learn about submitting apps

## Age Rating Updates

Since January 31, 2026

Ratings for all apps and games on the App Store have been automatically updated to align with our new age rating system and will be reflected on Apple devices running a minimum of iOS 26, iPadOS 26, macOS Tahoe 26, tvOS 26, visionOS 26, and watchOS 26.

Provide responses to the updated age rating questions for each of your apps by January 31, 2026, to avoid an interruption when submitting your app updates in App Store Connect. You can view the age rating for each of your apps under the updated system and respond to the new questions in the App Information section of your app in App Store Connect.

- Learn more about age ratings values and definitions

- Learn how to set your app rating

## APNs Certificate Update

Since February 24, 2025

The Apple Push Notification service (APNs) will be updated with a new server certificate in production on February 24, 2025. Update your application’s Trust Store to include the new server certificate: SHA-2 Root : USERTrust RSA Certification Authority certificate.

## Quarantine attribute in macOS apps uploaded to App Store Connect

Since February 18, 2025

macOS apps distributed on TestFlight and the App Store shouldn’t include the quarantine extended file attribute com.apple.quarantine. Starting February 18, you must remove this attribute from all files within macOS apps in order to upload to App Store Connect.

## DSA trader status required for apps in the EU

Since February 17, 2025

Apps without trader status will be removed from the App Store in the European Union (EU) until trader status is provided and verified in order to comply with the Digital Services Act.

## App Store Receipt Signing Intermediate Certificate

Since January 24, 2025

The SHA-1 intermediate certificate used for signing App Store receipts expires on January 24, 2025. If your app performs on-device receipt validation, make sure it supports the SHA-256 algorithm; alternatively, use the AppTransaction and Transaction APIs to verify App Store transactions.

For more details, view TN3138: Handling App Store receipt signing certificate change.

## APNs Certificate Update

Since January 20, 2025

The Apple Push Notification service (APNs) will be updated with a new server certificate in sandbox on January 20, 2025. Update your application’s Trust Store to include the new server certificate: SHA-2 Root : USERTrust RSA Certification Authority certificate.

## DSA trader status required for app updates in the EU

Since October 16, 2024

Your trader status is required to submit app updates for apps distributed on the App Store in the European Union (EU), in order to comply with the Digital Services Act.

## Transition from XML to the App Store Connect API

Since July 15, 2024

Game Center management will no longer be supported by the XML feed as of July 15, 2024.

Support for in-app purchases, subscriptions, metadata, and app pricing ended on November 9, 2022.

You can manage this content via the App Store Connect REST API, which makes it easy to customize and automate your workflows.

## Approved reasons for APIs

Since May 1, 2024

You’ll need to include approved reasons for the listed APIs used by your app’s code (including from third-party SDKs) to upload a new or updated app to App Store Connect.

## Xcode 15

Since April 29, 2024

Apps uploaded to App Store Connect must be built with Xcode 15 for iOS 17, iPadOS 17, tvOS 17, or watchOS 10 starting April 29, 2024.

Learn about submitting your apps

## Apple notary service update

Since November 1, 2023

If you notarize Mac software with the Apple notary service using the altool command-line utility or Xcode 13 or earlier, you’ll need to transition to the notarytool command-utility or upgrade to Xcode 14 or later. Starting November 1, 2023, the Apple notary service will no longer accept uploads from altool or Xcode 13 or earlier. Existing notarized software will continue to function properly.

Learn about notarizing software

## Game Center entitlement and configuration requirement

Since August 16, 2023

New apps and app updates for iOS, iPadOS, or tvOS offering Game Center features need to include the Game Center entitlement in the entitlements plist and have Game Center features configured in App Store Connect before you can submit them to the App Store.

Learn about configuring Game Center in Xcode

Learn about configuring Game Center in App Store Connect

View capability and entitlement updates

## Intermediate certificate update

Since August 16, 2023

Receipts in new apps and app updates submitted to the App Store, as well as all apps in sandbox, will be signed with the SHA‑256 intermediate certificate. If your app verifies App Store transactions using the AppTransaction and Transaction APIs, or the verifyReceipt web service endpoint, no action is required.

If your app validates App Store receipts on device, make sure your app will support the SHA-256 version of this certificate. New apps and app updates that don’t support the SHA-256 version of this certificate will no longer be accepted by the App Store starting August 16, 2023.

## tvOS 16.1 SDK

Since July 31, 2023

All tvOS apps submitted to the App Store must be built with Xcode 14.1 and tvOS 16.1 SDK or later.

Learn about submitting apps

## App Store global pricing update in May

Since May 9, 2023

Pricing for existing apps and one-time in-app purchases will be updated with enhanced global prices across App Store storefronts using your current price in the United States as the basis—unless you’ve made relevant updates after March 8, 2023. This update has been deferred to later this year for the App Store in Türkye.

Learn more

## Xcode 14.1

Since April 25, 2023

iOS and iPadOS apps submitted to the App Store must be built with Xcode 14.1 and the iOS 16.1 SDK or later. And watchOS apps submitted to the App Store must be built with Xcode 14.1 and the watchOS 9.1 SDK or later.

Learn about submitting apps

## Transition from subscription reports version 1.2 to 1.3

Since March 1, 2023

Subscription reports version 1.2 will no longer be available as of March 1, 2023. If you automatically download subscription reports using the App Store Connect API or Reporter, please update your query parameter to version 1.3 if you haven’t already.

## Transition from XML to App Store Connect API

Since November 9, 2022

The XML feed will no longer support in-app purchases, subscriptions, metadata, or app pricing as of November 9, 2022. You can manage this content via the App Store Connect REST API, which makes it easy to customize and automate your workflows. 

The XML feed will continue to support existing Game Center management functionality.

Learn more about the API

=== SOURCE: p6.html


=== SOURCE: https://developer.apple.com/distribute/app-review/
# App Review

We review all apps, app updates, app bundles, in-app purchases, and in-app events submitted to App Store Connect to help provide a safe and trusted experience for users and the opportunity for developers to succeed. As you plan and build, use these guidelines and resources to help the review process go as smoothly as possible.

## Preparing for review

Learn about the guidelines your submission needs to follow and information you’ll provide for review.

### Guidelines

Get in-depth details on the technical, content, and design criteria that we use for review, and learn about other key guidelines.

- App Review Guidelines

- Human Interface Design Guidelines

- Guidelines for Using Apple Trademarks and Copyrights

### Apple Developer Program License Agreement

The Apple Developer Program License Agreement details your obligations and responsibilities for the use of Apple software and services. The latest agreement can be found on the Agreements and Guidelines page.

Read the latest license agreement

### App review information

If your app requires specific settings, user account information, or special instructions, include these details in the App Review Information section of App Store Connect. If you don’t include this information, the app review process may be delayed and your app may not pass review.

Learn more about providing information for a complete review on App Review Help.

## Submitting for review

When you submit for review in App Store Connect, you can:

- Manage your submissions and communicate with App Review on the App Review page within Apps. You can visit the App Review page at any time, even if you don’t have active submissions or conversations.

- Submit items such as in-app events, custom product pages, and product page optimization tests without needing a new app version.

- Include multiple items in one submission.

- Remove items with issues from your submission and continue with items that were accepted by App Review.

- View a history of submissions created using the updated experience, including messages from App Review.

- Decide whether your app is reviewed for the App Store or Notarization only.

Learn more about submitting for review on App Store Connect Help.

### Review status

App Review works around the clock, typically reviewing at least 50% of submissions in less than 24 hours and 90% in less than 48 hours. You’ll be notified by email of status changes. You can also check the review status of your submission in the Apps section of App Store Connect or on the App Store Connect app for iPhone and iPad. If your submission is incomplete, review times may be delayed or your submission may not pass.

Learn more about how to track a submission’s review status on App Review Help.

## Avoiding common issues

We’ve highlighted some of the most common issues to help you better prepare before submitting for review. On average, over 40% of unresolved issues are related to guideline 2.1: App Completeness, which covers crashes, placeholder content, incomplete information, and more.

Watch “Tips for preventing common review issues”

### Crashes and bugs

Submit items for review only when they’re complete and ready to be published. Make sure to thoroughly test on devices running the latest software and fix all bugs before submitting. View guideline 2.1.

### Broken links

All links in your app must be functional. A link to user support with up-to-date contact information and a link to your privacy policy is required for all apps. View guideline 2.1 and guideline 5.1.

### Placeholder content

Finalize all images and text before submitting for review. Items that are still in progress and contain placeholder content are not ready to be distributed and cannot be approved. View guideline 2.1.

### Incomplete information

Enter all of the details needed for review in the App Review Information section of App Store Connect. If some features require signing in, provide a valid demo account username and password. If there are special configurations to set, include the specifics. If features require an environment that is hard to replicate or require specific hardware, be prepared to provide a demo video or the hardware. Also, please make sure your contact information is complete and up to date. View guideline 2.1.

Specific documentation is required for certain scenarios and types of apps. Here are a few examples:

- If the app is for kids and contains third-party ads, provide a link to the ad services’ publicly documented practices and policies for Kids category apps, including human review of ad creatives for age appropriateness. View guideline 1.3.

- If the app works with medical hardware, provide a copy of regulatory clearance for the locations where the app is available. View guideline 1.4.

- If the app features third-party trademarks or copyrighted content or lets users stream or download third-party content, provide the authorization to do so. Examples include video streaming and marketing that uses imagery of celebrities, sports, movies, or music. View guideline 4.1 and guideline 5.2.

- If the app facilitates services requiring licensing, such as real money gaming and gambling, lotteries, raffles, and VPN licensing, provide the authorization to do so. Note that licensing requirements may vary depending on region. View guideline 5.

### Privacy policy issues

Make sure your privacy policy adheres to guideline 5.1 and:

- Identifies the data the app collects, how it collects that data, and all uses of that data.

- Confirms that any third party with whom the app shares user data provides the same or equal protection of user data as stated in the app’s privacy policy.

- Explains your data retention and deletion policies and describes how a user can revoke consent and/or request deletion of their data.

Watch “Do more with less data”

### Unclear data access requests

When requesting permission to access user or usage data, you should clearly and completely describe how your app will use the data. Including an example can help users understand why your app is requesting access to their personal information.

If your app’s code references one or more APIs that access sensitive user data, the app’s Info.plist file should contain a $!{infoPlistKey} key with a user-facing purpose string explaining clearly and completely why your app needs the data. All apps submitted to App Store Connect that access user data are required to include a purpose string.

To learn more, visit 5.1.1(ii) - Write clear purpose strings on App Review Help and view guideline 5.1.

### Inaccurate screenshots

Screenshots should accurately communicate value and functionality. Use text and overlay images to highlight the user experience, not obscure it. To learn more, visit 2.3.3 - Show your app in use with screenshots on App Review Help and view guideline 2.3.

### Substandard user interface

Apple places a high value on clean, refined, and user-friendly interfaces. Make sure your UI meets these requirements by planning your design carefully and following our design guides.

### Web clippings, content aggregators, or a collection of links

Your app should be engaging and useful, and make the most of the features unique to iOS. Websites served in an iOS app, web content that is not formatted for iOS, and limited web interactions do not make a quality app. View guideline 4.2.

### Repeated submission of similar apps

Submitting several apps that are essentially the same ties up the App Review process and risks your apps not passing review. Improve your review experience — and the experience of your future users — by thoughtfully combining your apps into one. View guideline 4.3.

### Copycats

When working on your app, focus on creating interesting, unique experiences that aren’t already available. Apps that actively try to copy other apps won’t pass review. To learn more, visit 4.1 - Preventing copycat and impersonation rejections on App Review Help and view guideline 4.1.

### Misleading users

Your app must perform as advertised and should not give users the impression the app is something it is not. If your app appears to promise certain features and functionalities, it needs to deliver. View guideline 2.3.

### Not enough lasting value

If your app doesn’t offer much functionality or content, or only applies to a small niche market, it may not be approved. Before creating your app, take a look at the apps in your category on the App Store and consider how you can provide an even better user experience. View guideline 4.2.

### Submitted by incorrect entity

Certain types of apps must be submitted by the legal entity that provides the services rather than an individual developer. These apps include, but are not limited to, those that require sensitive user information or provide services in highly regulated fields, such as banking and financial services, cryptocurrency, healthcare, gambling, and air travel. If you need to provide partnership documentation or authorization, attach the files in the Attachment section in App Store Connect and provide any descriptions or links in the Review Notes field. View guideline 3 and guideline 5.1.1.

### Technical Support

If your app didn’t pass review for technical reasons, such as crashes or bugs, view the following documentation:

- Acquiring Crash Reports and Diagnostic Logs

- Analyzing a Crash Report

- Identifying the Cause of Common Crashes

You can also visit the Apple Developer Forums or request code-level support.

## Contacting us

### App Review submissions

You can view your past and current submissions to App Review in App Store Connect. If your submission didn’t pass review, details are provided, including any specific App Review Guidelines that your submission didn’t follow. You can correspond with App Review to resolve the issues before resubmitting the build. Access the App Review section on the app’s page in App Store Connect.

Learn more about contacting App Review for help with a submission.

### Appointment

Meet with App Review over Webex to discuss the App Review Guidelines and explore best practices for a smooth review process. In each 30-minute video appointment, you can ask for advice on what to expect during review, how your app can best align with guidelines, reasons for common rejections, and topics related to the process of reviewing your app. 

Learn more about appointment requests.

### Appeals

If your app didn’t pass review and you feel we misunderstood your app’s concept and functionality, or that you were treated unfairly by Apple in the course of our review, you may choose to submit an appeal to the App Review Board. If you file an appeal, make sure to:

- Provide specific reasons why you believe your app complies with the App Review Guidelines.

- Submit only one appeal per submission that didn’t pass review.

- Respond to any requests for additional information before submitting an appeal.

Learn more about submitting complete appeals.

### Expedited reviews

You can request the review of your app to be expedited if you face extenuating circumstances, such as fixing a critical bug in your app or releasing your app to coincide with an event you’re directly associated with.

Critical bug fix. When submitting an expedited review to fix a critical bug, include the steps to reproduce the bug on the current version of your app.

Event-related app. For apps associated with an event, we recommend you plan and schedule the release of your app in App Store Connect. However, if your app is still in review and the launch of your event is quickly approaching, you can request to have your app review expedited. Make sure your request includes the event, date of the event, and your app’s association with the event.

Learn more about expedite requests.

### Bug fix submissions

If you’re submitting a bug fix update for your app and we find additional issues during review, you have the option to resolve the additional issues with your next submission, as long as there are no legal or safety concerns. To accept, simply reply to the offer message in App Store Connect and indicate you would like the current submission to be approved.

Learn more about bug fix submissions.

### Suggestions

Help improve the App Review Guidelines or identify a need for clarity in our policies by suggesting guideline changes. Your suggestions will be taken into consideration by App Review.

Learn more about suggesting changes to the guidelines.

### Report a concern

If you believe that an app presents a trust or safety concern, or is in violation of the App Review Guidelines, you can share details with us to investigate.

Learn more about reporting apps.

### Other questions

You can contact us to ask for support with an unresolved app rejection or removal.

Contact us

=== SOURCE: https://developer.apple.com/app-store/submitting/
# Submit your apps and games today

Take advantage of the latest capabilities in Apple platforms and the App Store to deliver your most innovative apps yet.

## Update for the latest OS releases

Build and test with Xcode 27, which supports the latest SDKs for iOS, iPadOS, macOS, tvOS, visionOS, and watchOS to take advantage of the latest advancements in Apple platforms. Make sure your apps and games work as expected on Apple devices running the latest OS releases. Starting April 2027, apps and games uploaded to App Store Connect need to meet the following minimum requirements.

- iOS and iPadOS apps must be built with the iOS & iPadOS 27 SDK or later, and target iOS 15 or later

- tvOS apps must be built with the tvOS 27 SDK or later

- visionOS apps must be built with the visionOS 27 SDK or later

- watchOS apps must be built with the watchOS 27 SDK or later

Download Xcode 27

iPhone Duo is now in the hands of customers. Make sure your app looks great by building with the latest SDKs, optimizing your assets, and submitting them to App Store Connect.

Learn how to make your app shine on iPhone Duo

##      Set up in App Store Connect 

When you distribute on the App Store, people around the world can discover and download your apps and games in 175 storefronts and 50 languages.

### App Review

The guiding principle of the App Store is simple — we want to provide a trusted experience for people to get apps and games, and a great opportunity for developers to succeed. To do this, Apple reviews submissions to confirm they're safe, secure, and reliable. This includes apps and app updates, as well as bundles, Apple In-App Purchases, In-App Events, App Store metadata, and other content you submit for review. As you plan and build, get acquainted with the App Review Guidelines early on in your app or game’s development in order to make appropriate design decisions and help your review process goes as smooth as possible.

Learn about App Review

### TestFlight

You can get feedback on your apps, games, and App Clips throughout your development using TestFlight, Apple’s beta app testing service. Simply add testers from your internal team, or invite external testers via email or public link. Testers download, test, and provide feedback on your beta app, using the TestFlight app. You can then use their provided feedback — including screenshots with contextual feedback, or crash details — to improve your app or game.

Learn about TestFlight

### Product page

Make sure your app’s name, icon, description, screenshots, app previews, and keywords are ready for your App Store product page. You can also take this opportunity to update your subtitle and promotional text, and choose to promote any new Apple In-App Purchases. Before submitting, make sure to:

Complete the age rating questionnaire. Respond to the age rating questionnaire in App Store Connect. This questionnaire includes a list of content descriptors, in-app controls, and capabilities that allow you to specify the frequency of each content type in your app. An Apple global age rating is provided based on your responses, as well as additional region-specific ratings if required. Learn how to set an app rating.

Provide your app’s privacy details. Enter all necessary information about your app’s privacy practices, including the practices of third‑party partners whose code you integrate into your app, in App Store Connect. These details inform the Privacy Nutrition Label that appears on your product page and are required in order to submit new apps and app updates to the App Store.

Indicate your accessibility support. You can share information in App Store Connect about your app or game’s support — such as whether it includes VoiceOver, Voice Control, Larger Text, Captions, and more. Based on this information, an Accessibility Nutrition Label will appear on your App Store product page, specific to each platform you support. If you’d like, you can also add a URL on your App Store product page that links people to a website with even more details.

Learn about creating product pages

### Availability options

Verify required device capabilities. The App Store is designed to provide users with apps that work seamlessly with their devices’ capabilities. Verify that your information property list (info.plist) is compatible with any device requirements when submitting a new app that takes advantage of the latest technologies.

Explore universal purchase. With universal purchase, people can discover and enjoy your app or game across their Apple devices with a single purchase. Apple In-App Purchases and subscriptions can also easily be set up and shared across platforms. Your product page shows the other platforms your app supports along with screenshots, and you’ll be able to promote your app using a single URL across your marketing channels.

Offer iPadOS and iOS apps on Mac computers and Apple Vision Pro. Most iPadOS and iOS apps can run unmodified on Apple Vision Pro and on Mac computers with Apple silicon, so your app can easily extend to these platforms — with no additional work required. By default, your compatible apps are published automatically on the App Store for Apple Vision Pro or Mac using the metadata you’ve already provided in App Store Connect.

Learn about managing your app’s availability

##      Increase discoverability 

Boost discoverability for your app or game with built-in marketing features on the App Store.

### Grow with App Store features

Create assets for your product page headers and search results. Make a strong impression to drive people to download your app or game using compelling assets across the App Store. Take advantage of product page headers and search result assets to further showcase your app or game’s value in addition to your app previews and screenshots. You can also use the product page preview tool to visualize your product page before it’s published on the App Store. Get guidance and ready-made templates to create captivating assets that people will love.

Create custom product pages. In addition to your default product page, you can use custom product pages to showcase a particular feature, content, character, or aspect of gameplay. Highlight this content on each page with unique screenshots, app previews, and promotional text that differ from your default product page. Share a particular page with people by using its unique URL in your marketing efforts or an Apple Ads campaign.

Optimize your product page. Test different elements of your App Store product page to understand if different app icons, screenshots, or app preview videos result in more engagement.

Offer In-App Events. Promote timely content within your app or game — such as game competitions, movie premieres, livestreamed experiences, and more — using In-App Events. People can find In-App Events across the App Store, including on your product page, in search results, and on the Today, Games, and Apps tabs. Learn about In-App Events.

### Promote your apps and games

Share your story with us. Use Featuring Nominations in App Store Connect to share your story with our team. The App Store showcases incredible apps and games that people love across Apple platforms, and shines a spotlight on developers from communities around the world. Each Apple platform has a dedicated App Store to help people discover the best apps, games, in-app content, and more. Learn about getting featured.

Get custom marketing assets. Use the App Store marketing tools and the App Store Connect app to get premade assets to celebrate moments such as a launch, new version, and more. Simply download your selected assets, then share them using your social media or marketing channels to amplify your app or game. Learn about marketing assets.

### Apple Games app

Games that are available on the App Store will automatically appear on the Games app, including in search results, the Library tab, and the Continue Playing section. Additionally, games that include Game Center features and In-App Events are prominently displayed across the Games app in order to help players discover and engage deeper with them.

Learn about the Games app

