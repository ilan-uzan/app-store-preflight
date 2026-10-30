=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses/
### App Store Connect Help

App Store Connect / Reference / App information / App and submission statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# App and submission statuses

## App statuses

The app status indicates where an app is in the review and release process.

-  
A red status indicator () means that you need to perform an action before the app distributes.

-  
A yellow status indicator () means that a process, controlled either by you or Apple, is still happening.

-  
A green status indicator () means that the app is Ready for Distribution.

If an app status indicates as editable below, you can edit app metadata when the app has this status.

Receive automatic notifications to your web server whenever the status of your app changes by using webhooks. Learn how to manage webhooks.

Status

Description

Editable

Prepare for Submission

You’ve created an app record in App Store Connect but are still preparing information for it.

Ready for Review

You’ve entered all of the required metadata for your app and indicated that you intend to submit it for review, but haven’t submitted it yet.

You can submit the app by itself or include other items, such as In-App Events or custom product pages.

Note: Images and videos aren't editable in this state.

Invalid Binary

You’ve submitted your app to App Review, but the build does not meet the current binary requirements. You must upload a new build, or select one that meets all the current build requirements.

Waiting for Review

You’ve submitted a new app or updated version. Apple received your submission, but hasn’t started the review.

While you're waiting for the review, you can:

-  
Edit certain app information.

-  
Remove the build from review.

However, you can't upload or edit screenshots or app previews.

In Review

App Review is reviewing your app. You can remove the build from review.

Accepted

This item has been accepted, but one or more items in your submission were rejected.

The app can only publish when all items in the submission are accepted. You can edit the rejected items and resubmit, or remove them from the submission to move forward with the currently accepted items.

Waiting for Export Compliance

Your CCATS file is in Apple’s export compliance review process.

Pending Developer Release

Your app was accepted, but you still need to release it for distribution on the App Store.

Processing for Distribution

Your app is processing and will be ready for distribution within 24 hours.

Pending Apple Release

Apple is holding your app version until the corresponding Apple operating system version releases to the public.

If you think an app should be released on the existing operating system versions, review the deployment target set in your app build. If you rebuild your app with a different deployment target, reject the build for this version and submit the new version.

Pending App Transfer

The app transferor has initiated the app transfer, but the recipient hasn't yet accepted. The transferor and the recipient can each cancel the transfer. No changes can be made to the app except changes to pricing.

Processing App Transfer

The recipient accepts the app transfer. You can't cancel or make changes to the app until the transfer is complete.

Ready for Distribution

Your app has been accepted and is ready for distribution.

To distribute your app, your agreements must be in effect. The Account Holder can accept the latest agreements in the Business section.

Rejected

Your app wasn't accepted. App Review notifies App Store Connect users with the Admin, App manager, or Developer role with the issues. Learn how to reply to App Review messages.

Metadata Rejected

App Review didn’t accept your metadata. Read the message from App Review, edit the metadata to resolve the issue, and reply to the message from App Review.

Developer Rejected

You removed your app from review. When you’re ready, resubmit your build or submit a new build.

### Submission statuses

These statuses are shown for submissions to App Review. Once all items within the submission are accepted, the submission moves from the In Progress section to the Completed section on the App Review page.

Status

Description

Waiting for Review

Apple received your submission, but hasn’t started review.

While waiting for review, you can:

-  
Edit certain information

-  
Remove items from review

However, you can't:

-  
Upload or edit screenshots or app previews

-  
Edit In-App Event metadata

In Review

App Review is reviewing your submission. You can cancel the submission to remove it from review.

Processing

You removed your submission from review and your action is being processed. When it's done processing the submission moves to Completed in the App Review section.

Unresolved Issues

App Review rejected one or more items in the submission. Learn how to manage a submission with unresolved issues.

Rejected

App Review rejected your app bundle or TestFlight submission. For TestFlight, you must submit a new build for review before you can invite external testers.

### Item statuses

These statuses are shown for items within a submission to App Review. You can locate the status of each item on the item’s page (for example, the app record or In-App Event’s page), or when you click View or Resolve next to the submission. Once all items within the submission are accepted, the submission moves from the In Progress section to the Completed section on the App Review page.

Status

Description

Ready for Review

The item has been added to a submission, but it hasn’t been submitted to App Review yet.

Waiting for Review

Apple received your submission, but hasn’t started review.

While waiting for review, you can:

-  
Edit certain information

-  
Remove items from review

However, you can't:

-  
Upload or edit screenshots or app previews

-  
Edit In-App Event metadata

In Review

App Review is reviewing your submission. You can cancel the submission to remove it from review.

Accepted

This item has been accepted, but there are one or more rejected items in the submission. All items in the submission must be accepted before any can be published.

You can edit the rejected items and resubmit, or you can remove them from the submission.

Learn how to reply to App Review messages.

Rejected

App Review didn’t accept your item. You can edit the item and resubmit, or you can remove the item from the submission.

Learn how to manage a submission with unresolved issues.

### App Store availability statuses

The App Store status tells you whether your app is available in a specific country or region, or if there are any reasons your app isn’t appearing somewhere.

-  
A red status indicator () means your app isn’t available in the country or region.

-  
A yellow status indicator () means your app needs action from you before the app is available in the country or region, or the app is currently processing.

-  
A green status indicator () means your app is available in the country or region.

Status

Description

Available

Your app is live on the App Store for users in this country or region.

Available on App Release

Your app is ready to be released in this country or region after your scheduled release date or after you manually release the app. This status only appears if your app has never released in any regions. Learn how to select an App Store version release option.

Pre-Order Pending Developer Release

You've set up a pre-order that publishes in this country or region after you release a version of your app. Learn more.

Pre-Order (Scheduled Release [date])

The pre-order is live and your app will be releases for download or purchase in this country or region on the date indicated. Customers in this country or region can pre-order your app on the store.

Processing to Available

Your app is processing and should be available in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us.

Processing to Not Available

Your app is processing and should no longer be available in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us.

Processing to Pre-Order

Your app is processing and should publish for pre-order in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us.

Not Available

Your app isn't available in this country or region because you've indicated that you don't intend to distribute in this location. Learn how to select the regions where you want to make your app available.

Missing App Rating

Your app isn't available in this country or region because you haven't set an age rating for your app. Learn how to set an app age rating.

Missing Tax Form

Your app isn't available in Brazil because you haven't submitted Brazilian tax information. Learn more.

Missing Game registration number

Your app isn't available in China mainland because you haven't provided an approval number and supporting documents from China's National Press and Publication Administration. Learn more.

ICP Filing Number Missing

Your app isn't available in China mainland because you haven't provided a valid Internet Content Provider (ICP) Filing Number. Learn more.

ICP Filing Number Invalid

Your app isn't available in China mainland because the Internet Content Provider (ICP) Filing Number or metadata you provided doesn't match the information you have filed with China’s Ministry of Industry and Information Technology (MIIT), or both. Learn more.

Cannot Sell App

Your app isn't available in this country or region. Hold the pointer over the status to locate the reason why. If you have any questions, contact us.

Related Overview of submitting for review App build statuses App information Platform version information App bundle information

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/app-build-statuses/
### App Store Connect Help

App Store Connect / Reference / App uploads / App build statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# App build statuses

The build status tells you immediately whether your build needs attention. The status applies to the build only, not the entire app.

-  
A red status indicator () means that you need to perform some action or the build is expired.

-  
A yellow status indicator () means that some process is ongoing, controlled either by you or by Apple.

-  
A green status indicator () means the build is being tested in TestFlight.

You can view the builds you upload and their file sizes, beta build status, and metrics under the TestFlight tab in App Store Connect.

Status

Description

Internal testing

External testing

Invalid Binary

Apple received your build, but it didn’t meet all the upload requirements. Resolve any issues in the build, and redeliver. Visit Upload builds.

Not visible in TestFlight

Not visible in TestFlight

Missing Compliance

Your build is missing export compliance documentation. Action is needed. Learn how to provide export compliance for beta builds.

Waiting for Export

Compliance Review

Documentation for export compliance has been submitted and is in review. No action is needed on your end.

In Compliance Review

Documentation for export compliance is in review. No action is needed on your end.

Ready to Submit

Your build can be distributed to internal testers, or can be submitted to TestFlight App Review for external testing or to App Review for distribution to customers.

Waiting for Review

Your build has been submitted to TestFlight App Review. It will need to be approved before you can begin external testing.

In Beta Review

Your build is currently being reviewed by TestFlight App Review. It'll need to be approved before you can begin external testing.

Not Available for Testing

Your build can't be used with TestFlight because the provisioning profile is missing an application identifier. To begin testing, upload a new build that includes the application identifier.

Expired

Your build can't be used for testing with TestFlight because it has passed its 90-day availability window.

Rejected

Your build was rejected by TestFlight App Review and can no longer be used in TestFlight. To begin testing, upload a new build.

Not visible in TestFlight

Not visible in TestFlight

Ready to Test

Your build can be tested by external and internal testers, but you haven’t added any testers yet. You may have opted to manually notify testers after your build is approved. You can also submit your app to App Review for distribution to customers.

Testing

Your build is being tested by at least one group or tester. Click on the build to view more details about who is testing your build. You can continue testing or submit your app to App Review for distribution to customers. Testers that have received an invite to test will still be able to test your build even after it's available for customers.

RelatedApp and submission statuses

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

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/build-upload-statuses/
### App Store Connect Help

App Store Connect / Reference / App uploads / Build upload statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# Build upload statuses

The build upload status provides detailed insights into delivery progress, including information, warnings and errors.

State

Description

Processing

Your build upload is still being processed. You'll receive an email notification and the table under Build Uploads will display an updated status when your build has finished processing.

If you upload a build and it remains in the Processing state for more than 24 hours, there may be an issue. To resolve the issue, submit a Feedback Assistant ticket or contact us.

Failed

Your build upload has finished processing, but encountered an issue. Select the build to view potential errors, warnings, and information associated with the failure. Ensure to resolve all errors prior to re-uploading your build. 

Note: If the build upload fails, you can reuse the same build number for your next upload.

Complete 

Your build upload has processed successfully and is now ready for testing. 

Note: If there is a warning badge next to this status, review possible warnings or other information before your next upload.

=== SOURCE: https://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version/
### App Store Connect Help

App Store Connect / Update your app / Create a new version 
Filter ⌘K  
Filter ⌘K  

Update your app  

# Create a new version

When you’re ready to distribute a new version of your app, you create a version using the same app record you created for the original version.

Keep in mind that it's not possible to revert to a previous version on the App Store if you have an issue with your app. You must create and submit a new version. Ensure that the current version status is Ready for Distribution to initiate a new version.

Learn about creating a new version using App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the add button (+) next to the desired platform.

-  
In the New Version dialog, enter an incremental App Store version number, then click Create.

-  
Review and enter metadata about the new version.

When you create a new version, the metadata from the current version is automatically transferred to the new version.

For a description of the version properties, visit Platform version information. For the required and localizable properties, refer to Required, localizable, and editable properties.

-  
On the top right, click Save.

-  
Upload your new build to App Store Connect.

In Xcode, increment the build string before you upload your build to App Store Connect, as described in Set the version number and build string.

-  
When you're ready to submit your build, add it to your latest version, then submit your app to App Review.

Related Upload builds Choose a build to submit Add platforms Get started with app discovery and marketing

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

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers/
### App Store Connect Help

App Store Connect / Test a beta version / Invite external testers 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Invite external testers

External testers are people you invite to test your app who aren’t App Store Connect users. After uploading your build, you can invite up to 10,000 external testers per app. To make your build available for external testing, you need to create an external group, add builds, and invite testers using their email addresses or by sharing a public invitation link.

When inviting testers via a public link, you can set tester criteria, such as device and OS requirements, ensuring only qualified testers can accept the invitation. This facilitates the enrollment of relevant testers, who can then provide feedback for your beta app. Learn how to set tester criteria when inviting testers using a public link.

Keep in mind that:

-  
To create an external group for external testing, you must first create an internal group for internal testing.

-  
Builds uploaded as TestFlight Internal Only from Xcode or Xcode Cloud are marked as internal under the build number and can only be added to internal tester groups.

-  
Managed Apple Accounts created in reserved domains can’t be used to test builds. Learn more about reserved domains in Apple School Manager or Apple Business.

Learn how to manage tester invitations with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Create a group

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, click the add button (+) next to External Testing to add a new group.

-  
In the dialog that appears, enter a group name, then click Create.

Later, you can change the name of the group if needed.

### Add builds to a group

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select the group to which you want to add builds.

-  
On the right, click Add Builds to choose which builds you want to add to this group.

Note: If you plan to invite testers using a public link and set criteria, ensure that the builds you add to the group are compatible with the criteria you’ve set. You can review the insight cards at the top of the group's details page to check for any incompatible builds that have been added.

Note: You can add only one build at a time, but you can add more later. To add additional builds to a group, click the add button (+) next to Builds on the tester group page.

-  
In the build dialog, select the platform and version from the pop-up menus.

-  
In the table, select a build, then click Add.

-  
In the What to Test dialog, enter what you want testers to focus on.

-  
Optionally, enter localized versions of testing information in the text fields under each language-specific section.

-  
Optionally, select "Automatically notify testers."

If you leave this checkbox deselected, you must manually distribute the build to testers after it's approved by TestFlight App Review.

-  
Depending on the build's status, click either Submit Review or Start Testing.

You can only have one build of each version in review at a time. Once that build is approved, you can submit additional builds.

If your build uses Apple-hosted asset packs, make sure to submit the latest versions of any asset packs needed for testing after submitting the build.

Note: You can submit up to six builds for TestFlight App Review within a 24-hour period.

After you submit your build to TestFlight App Review, Apple reviews the build and its accompanying metadata. The first build you submit requires a full review, but later builds for the same version might not.

If Apple approves your build for TestFlight beta testing, users on the App Store Connect account with the Admin role will receive an email notifying them of the approval.

If Apple rejects your build or metadata, the status of the build will be Rejected. You can click App Review from the sidebar under General to view the rejection details for your beta build.

Note: Enter test information, such as Feedback Email and Contact Information, if these details haven’t been provided in the Test information dialog.

## Invite external testers using a public link or email

Once you have builds available to test, and you've added them to a group, you can invite testers. You can Invite testers using a public link, email, or both. When inviting testers using a public link, you can set tester criteria.

### Invite testers using a public link

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select a group.

-  
Under the testers tab, click Create Public Link.

-  
In the dialog that appears, select either Open to Anyone or Filter by Criteria.

-  
Open to Anyone. Anyone can join using the link.

-  
Filter by Criteria. Filter who can join by device or platform.

Optionally, under Tester Limit, click Set Limit to limit the number of testers who can join this testing group using the public link. Enter a number between 1 and 10,000.

-  
If you select Open to Anyone, click Confirm, then copy the link and share it using social media, messages, email, or other channels.

If you select Filter by Criteria, click Next, and then follow the steps below.

-  
In the dialog that appears, click Add Criteria. You need to add at least one criteria to invite testers.

-  
In the drop-down menu, select the device you want to add criteria for, then select the OS details. You can add multiple criteria as needed.

-  
From. Only allow testers using the OS version in the specified range to test your app.

-  
Newer than or equal to. Only allow testers using the specified OS version or newer to test your app.

-  
Older than or equal to. Only allow testers using the specified OS version or older to test your app.

-  
All supported (for platform). Allow testers with any OS version for the selected platform to test your app.

-  
After adding all your criteria, click Confirm. Then, copy the link and share it on social media, messaging apps, email, or any other channel.

Once you have created your public link, you can add or edit criteria, set or change a tester limit, make the link available to everyone, or disable it. Click Manage next to Public Link to open the dialog, make your changes, and then click Save.

Tip: Check the insight cards at the top of the group details page to identify if there are no compatible builds, if the public link is full, or if a build is about to expire.

View public link metrics to evaluate its performance and review feedback testers may have provided.

Keep in mind that anyone can share this link, so testers could potentially join your testing group even if you do not invite them directly.

If a tester joins your group using a public link, their name and email won’t be displayed in the Testers section in App Store Connect—it will display as anonymous. However, their installation date, sessions, and crashes will be displayed. You can make the public link deactivate at any time.

### Invite testers using their email address

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select a group.

-  
Click the add button (+) next to Testers.

-  
In the pop-up menu that appears, choose an option. You can add new testers using their email address, existing testers you've previously added, or import testers from a CSV file.

When you invite testers, they will receive an invitation email to begin testing. If a tester accepts an email invitation, their name, email address, installation date, sessions, and crashes, will display in the Testers section in App Store Connect.

Tip: To add users with a specific device type to a group, click Add Filter and select devices to filter by. Select all testers using the checkbox at the top of the table or select testers individually, then click Add to Group. In the dialog that appears, select the eligible groups you want to add these testers to and click Add.

### Notify external testers after your build is approved

If you didn’t select “Automatically notify testers” when you added your build to your group, you must manually notify testers once your build is approved.

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under Builds, click the platform for your app.

-  
Choose a version, then under Status, click Notify Testers for the build row.

The build status changes to Testing. External testers will then receive a notification directing them to accept the invitation using the TestFlight app on their device.

### Remove a build from a group

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select a group.

-  
On the right, under Builds, hold the pointer over the build you want to remove.

-  
Click the delete button.

-  
In the dialog that appears, confirm you want to remove the build from the group and click Remove.

If you want to remove a build from testing for all your testers, go to Stop testing a build.

###   FAQs

### How do I appeal if my beta build was rejected?

To appeal your beta build being rejected, contact TestFlight App Review.

Related TestFlight Overview Add internal testers View and manage tester information

=== SOURCE: https://developer.apple.com/help/app-store-connect/update-your-app/overview-of-maintaining-an-app/
### App Store Connect Help

App Store Connect / Update your app / Overview of maintaining an app 
Filter ⌘K  
Filter ⌘K  

Update your app  

# Overview of maintaining an app

After you publish your app, you perform a number of tasks to respond to customer feedback and to maintain your app throughout its lifetime. You can perform these tasks in any order.

## Create a new version

When you’re ready to distribute a new build of your app, you create a new version using the same app record as your previous version. You can update the metadata for the new app version and add a description of the new features.

## Download catalog reports

If you have several apps in your account, generate catalog reports that detail the information and settings for all your organization’s apps, including In-App Purchase, and metadata for Game Center leaderboards and achievements.

## Monitor App Store customer reviews, sales, and analytics

You can read and respond to reviews. To better understand how your app is doing, you can view sales and trends and view app analytics, such as crashes, sessions, and active users.

## Change App Store pricing and availability

You can change the price, schedule price changes, and change the countries or regions for your app on the App Store at any time. Scheduling price changes is useful for promotions that have start and end dates.

## Remove an app

If you no longer want your app to be available to customers, you can remove it from the App Store, which removes all versions of the app.

Related App and submission statuses Release a version update in phases Ratings and reviews overview Overview of reporting tools

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

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-test-information/
### App Store Connect Help

App Store Connect / Test a beta version / Provide test information 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Provide test information

When you distribute your app to external testers, you need to enter additional TestFlight test information about your app for TestFlight App Review. You can enter this information when you add your app to your account or before you invite external testers.

Learn how to provide test information using the App Store Connect API.

Required role: Account Holder, Admin, and App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under Additional, click Test Information.

-  
On the right, choose a language option and enter the required test information.

The information you enter for your beta app can differ from the information you enter later when submitting your app to the App Store.

-  
Under Invitation Experience, the App Information checkbox is selected by default. This means that your approved screenshots and app category automatically display in your invite. This information will be pulled from the latest approved version in the Ready for Distribution state.

If you prefer not to display the screenshots or app category in your invite, you can deselect the App Information checkbox.

-  
In the Beta App Description text field, enter a description of your beta version. This field is required.

-  
In the Feedback Email field, enter the email address where testers can contact you through the TestFlight app. This is also the reply-to address in email invitations to testers.

Learn about the TestFlight App Review information properties.

You can update this information at any time, and the updates will display in the TestFlight app.

Related TestFlight Overview Testing Apps with TestFlight

=== SOURCE: https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/
### App Store Connect Help

App Store Connect / Update your app / Release a version update in phases 
Filter ⌘K  
Filter ⌘K  

Update your app  

# Release a version update in phases

iOS macOS tvOS  
When you release a version update of your app, you can choose to release the new version to the App Store in stages. This option is available when you submit a version update and your app has one of the following statuses:

-  
Prepare for Submission

-  
Waiting for Review

-  
In Review

-  
Waiting for Export Compliance

-  
Pending Developer Release

-  
Developer Rejected

-  
Rejected

-  
Metadata Rejected

Selecting this option will release your app's update gradually over 7 days. A random sample of users with automatic updates on eligible devices will receive the update, without any notification of their participation in the phased release.

Day of Phased Release

Percentage of Users

1

1%

2

2%

3

5%

4

10%

5

20%

6

50%

7

100%

Keep in mind that apps and app updates in phased release can be manually downloaded from the App Store by anyone at any time.

During phased release, you may pause the release for up to 30 days, with no limit on the number of pauses. If you remove your app from sale — including when your Apple Developer Program membership lapses — phased release will stop and won't be available for that version again. When your app is reinstated, it becomes available to all users immediately, regardless of the percentage reached before removal. To resume a controlled rollout, make the version unavailable for download and submit a new version update with phased release enabled.

Learn how to manage phased releases using the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Release a version update in phases

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version you want to submit.

-  
On the right, scroll down to the Phased Release for Automatic Updates section, select Release update over a 7-day period using phased release.

-  
Click save.

When you submit your app for review and it's approved, the app status will be Ready for Distribution, and will be appended with “Phased Release” next to the status when viewing your app's version page.

When the update is complete, all users with Admin or App Manager roles who have access to this app will receive a notification regarding the completion of the phased release.

### Pause and resume a phased release

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the Ready for Distribution app version.

-  
In the Phased Release for Automatic Updates section, you can either pause the release by selecting Pause Phased Release or resume it by using the Use Phased Release option.

-  
Click Save.

You can pause your release for a total of 30 days. For example, if you pause the release for 10 days and then choose to resume it, you will have 20 days remaining to pause the release again. If you resume a release that was previously paused, your phased release will pick up on the day it was left off when it was paused.

### Release a version update to all users

If you decide to release your app in phases, you can release it to all users at any time once it has the Ready for Distribution status. When you select this option, all users whose devices have automatic updates turned on gets the latest app version supported on the user’s device.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version that you've submitted.

-  
On the top right of the page, click Release to All Users.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-an-app-store-version-release-option/
### App Store Connect Help

App Store Connect / Manage your app's availability / Select an App Store version release option 
Filter ⌘K  
Filter ⌘K  

Manage your app's availability  

# Select an App Store version release option

You can choose a release option for each platform version of your app in App Store Connect.

Note: If you’re setting up your app for pre-order in a country or region and haven't yet released it on the App Store, you'll need to release the app version manually. The App Store Version Release section will be dimmed and "Release the app yourself" will be automatically selected.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version you want to set a release option for.

-  
In the App Store Version Release section, select a release option:

-  
Release the app yourself: Select “Manually release this version.” (Later, manually release the version.)

-  
Automatically release the app after approval: Select “Automatically release this version.”

-  
Automatically release the app but no earlier than a specified date: Select “Automatically release this version after App Review, no earlier than” and below this option, enter a date and time.

-  
On the top right of the page, click Save.

## Manually release a version to the App Store

When submitting your app for review, you can manually release a version. After approval, release it to the App Store once its status changes to Pending Developer Release.

Releasing an app version is specific to the platform you're working with. If there are app versions for other platforms also in "Pending Developer Release" that you want to release, you must manually release each one for every platform.

Apple will send you an email reminder if an app remains in Pending Developer Release status for more than 30 days.

Learn how to manually release a version with the App Store Connect API.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the app version that has the status of Pending Developer Release.

-  
On the top right, click Release This Version.

-  
In the dialog that appears, click Confirm.

After manually releasing your app version, it may take up to 24 hours for it to appear on the App Store. To cancel the release, select Cancel This Release from the message on the version page.

Note: When you choose Release This Version, the new app will publish for pre-order in countries or regions where pre-order is enabled. It’ll also be available for download or purchase in any country or region where the App Store status is Available or Available on App Release. Learn more.

Related App Store pricing and availability start times by country or region App and submission statuses

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/
### App Store Connect Help

App Store Connect / Test a beta version / TestFlight overview 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# TestFlight Overview

iOS macOS visionOS tvOS watchOS  
TestFlight lets you distribute beta builds of your app, manage beta testers, and collect feedback. Learn more. 

Make improvements to your app and continue distributing builds until all issues are resolved before you submit your app for review.

To use TestFlight for Mac, build your macOS apps with Xcode 13 or later. If your app includes an App Clip, you can invite testers to test the App Clip experience on its own. Testers who are invited to test your app can test both the app and the App Clip. Either the app or the App Clip can be installed on a device at a time. Testers can choose to switch between them at any time.

Learn how to manage beta testing using the App Store Connect API.

## Step 1: Provide test information

Provide test information about your app, such as a beta app description, an explanation of features to test, and an email address where feedback can be submitted. You can also choose to show approved app screenshots and your app category.

### Step 2: Upload your build or assets

Upload your build to App Store Connect. Read Cryptography and US export compliance to determine if you need to provide app encryption documentation for your app. You can test a build for up to 90 days.

Note: For builds to be eligible for TestFlight, they must include application identifiers within the provisioning profiles.

You also have the option to upload assets that are managed separately from a build by using Apple-Hosted Background Assets.

### Step 3: Invite internal and external testers

Create groups for testers, then assign specific builds to them. After you've added builds to a group, you can add external testers (up to 10,000 people) and internal testers (up to 100 App Store Connect users with access to your content) to test your app. If you invite external testers, your beta build may require review. When you add the first build of your app to a group, the build gets sent to App Review to make sure it follows the App Review Guidelines. A review is required only for the first build. Subsequent builds may not require a full review. Testing can begin once a build is approved.

Note: Managed Apple Accounts created in reserved domains can’t be used to test builds. Learn more about reserved domains in Apple School Manager or Apple Business.

### Step 4: Testers download TestFlight and accept your invitations

Testers install the free TestFlight app on their devices. Then they use their invitation email or a public link to accept invitations, install your app, send feedback, and get updates. Testers download and install thinned variants of your app.

Note: Setting specific criteria for your public link invitations can limit the number of external testers who can test your app.

### Step 5: View tester and build information

Track tester engagement and your app's performance by viewing build status and metrics. These metrics include the number of sessions and crashes. Also, you can resend email invitations to testers who haven't accepted their invitation.  

### Step 6: Collect feedback from testers

Testers using TestFlight version 2.3 or later on iOS, macOS, and visionOS can submit feedback either through the TestFlight app or by taking a screenshot directly within your beta app. You can view this tester feedback in the TestFlight Feedback section in App Store Connect. Testers running tvOS or earlier versions of iOS can send feedback to the email address you specified in step 1.

### Step 7: Stop testing

When testing is complete, you have the option to expire a build to stop testing it. If you don’t expire your build and submit it to the App Store, testers who received an invitation to test will still be able to test your build even after it goes live on the App Store. Your build becomes unavailable for testers after 90 days.

Related Upload builds Overview of publishing your app on the App Store Overview of submitting for review Get started with TestFlight

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight/
### App Store Connect Help

App Store Connect / Test a beta version / Testing subscriptions and In-App Purchases in TestFlight 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Testing subscriptions and In-App Purchases in TestFlight

## Subscription renewal rate in TestFlight

When testing your app's subscriptions in TestFlight, the renewal rate is accelerated. Each subscription is renewed daily, up to 6 times within a 1-week period, regardless of the subscription's duration.

Learn more about testing In-App Purchases with sandbox.

Important: To test different renewal rates in TestFlight, you can use your Sandbox Apple Account. Learn more about managing Sandbox Apple Account settings.

Renewal for all durations

1 week

1 month

2 months

3 months

6 months

1 year

Subscription renewal speed

1 Day

1 Day

1 Day

1 Day

1 Day

1 Day

Example scenario: If you start a 1-month subscription on February 1st, it'll renew every 24 hours for a total of 6 renewals before being canceled. Since subscriptions renew at an accelerated rate in TestFlight, you'll see a new transaction for each renewal on February 2nd, 3rd, 4th, 5th, 6th, and 7th. The subscription's auto-renewal will then be disabled on February 8th.

Note: To test subscriptions entering or exiting billing retry, you must test with a Sandbox Apple Account to subscribe and use the sandbox account settings to simulate this scenario. Learn more about testing failing subscription renewals and In-App Purchases.

### Test In-App Purchase scenarios in TestFlight with your Sandbox Apple Account

Apps downloaded from TestFlight will automatically operate in a sandbox environment. However, to test different In-App Purchase scenarios in TestFlight, you can use your Sandbox Apple Account. First, sign out of your production Apple Account under Media & Purchases. Then, go to Developer settings and sign in with your Sandbox Apple Account to access the sandbox controls for testing. For more details, please refer to the  Sign in to your Sandbox Apple Account for TestFlight section.

To learn more about the different In-App Purchase scenarios you can test with your Sandbox Apple Account, visit the Manage Sandbox Apple Account settings page.

Note:  You can only use a Sandbox Apple Account to test apps within your own developer account.

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses
### App Store Connect Help

App Store Connect / Reference / App information / App and submission statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# App and submission statuses

## App statuses

The app status indicates where an app is in the review and release process.

-  
A red status indicator () means that you need to perform an action before the app distributes.

-  
A yellow status indicator () means that a process, controlled either by you or Apple, is still happening.

-  
A green status indicator () means that the app is Ready for Distribution.

If an app status indicates as editable below, you can edit app metadata when the app has this status.

Receive automatic notifications to your web server whenever the status of your app changes by using webhooks. Learn how to manage webhooks.

Status

Description

Editable

Prepare for Submission

You’ve created an app record in App Store Connect but are still preparing information for it.

Ready for Review

You’ve entered all of the required metadata for your app and indicated that you intend to submit it for review, but haven’t submitted it yet.

You can submit the app by itself or include other items, such as In-App Events or custom product pages.

Note: Images and videos aren't editable in this state.

Invalid Binary

You’ve submitted your app to App Review, but the build does not meet the current binary requirements. You must upload a new build, or select one that meets all the current build requirements.

Waiting for Review

You’ve submitted a new app or updated version. Apple received your submission, but hasn’t started the review.

While you're waiting for the review, you can:

-  
Edit certain app information.

-  
Remove the build from review.

However, you can't upload or edit screenshots or app previews.

In Review

App Review is reviewing your app. You can remove the build from review.

Accepted

This item has been accepted, but one or more items in your submission were rejected.

The app can only publish when all items in the submission are accepted. You can edit the rejected items and resubmit, or remove them from the submission to move forward with the currently accepted items.

Waiting for Export Compliance

Your CCATS file is in Apple’s export compliance review process.

Pending Developer Release

Your app was accepted, but you still need to release it for distribution on the App Store.

Processing for Distribution

Your app is processing and will be ready for distribution within 24 hours.

Pending Apple Release

Apple is holding your app version until the corresponding Apple operating system version releases to the public.

If you think an app should be released on the existing operating system versions, review the deployment target set in your app build. If you rebuild your app with a different deployment target, reject the build for this version and submit the new version.

Pending App Transfer

The app transferor has initiated the app transfer, but the recipient hasn't yet accepted. The transferor and the recipient can each cancel the transfer. No changes can be made to the app except changes to pricing.

Processing App Transfer

The recipient accepts the app transfer. You can't cancel or make changes to the app until the transfer is complete.

Ready for Distribution

Your app has been accepted and is ready for distribution.

To distribute your app, your agreements must be in effect. The Account Holder can accept the latest agreements in the Business section.

Rejected

Your app wasn't accepted. App Review notifies App Store Connect users with the Admin, App manager, or Developer role with the issues. Learn how to reply to App Review messages.

Metadata Rejected

App Review didn’t accept your metadata. Read the message from App Review, edit the metadata to resolve the issue, and reply to the message from App Review.

Developer Rejected

You removed your app from review. When you’re ready, resubmit your build or submit a new build.

### Submission statuses

These statuses are shown for submissions to App Review. Once all items within the submission are accepted, the submission moves from the In Progress section to the Completed section on the App Review page.

Status

Description

Waiting for Review

Apple received your submission, but hasn’t started review.

While waiting for review, you can:

-  
Edit certain information

-  
Remove items from review

However, you can't:

-  
Upload or edit screenshots or app previews

-  
Edit In-App Event metadata

In Review

App Review is reviewing your submission. You can cancel the submission to remove it from review.

Processing

You removed your submission from review and your action is being processed. When it's done processing the submission moves to Completed in the App Review section.

Unresolved Issues

App Review rejected one or more items in the submission. Learn how to manage a submission with unresolved issues.

Rejected

App Review rejected your app bundle or TestFlight submission. For TestFlight, you must submit a new build for review before you can invite external testers.

### Item statuses

These statuses are shown for items within a submission to App Review. You can locate the status of each item on the item’s page (for example, the app record or In-App Event’s page), or when you click View or Resolve next to the submission. Once all items within the submission are accepted, the submission moves from the In Progress section to the Completed section on the App Review page.

Status

Description

Ready for Review

The item has been added to a submission, but it hasn’t been submitted to App Review yet.

Waiting for Review

Apple received your submission, but hasn’t started review.

While waiting for review, you can:

-  
Edit certain information

-  
Remove items from review

However, you can't:

-  
Upload or edit screenshots or app previews

-  
Edit In-App Event metadata

In Review

App Review is reviewing your submission. You can cancel the submission to remove it from review.

Accepted

This item has been accepted, but there are one or more rejected items in the submission. All items in the submission must be accepted before any can be published.

You can edit the rejected items and resubmit, or you can remove them from the submission.

Learn how to reply to App Review messages.

Rejected

App Review didn’t accept your item. You can edit the item and resubmit, or you can remove the item from the submission.

Learn how to manage a submission with unresolved issues.

### App Store availability statuses

The App Store status tells you whether your app is available in a specific country or region, or if there are any reasons your app isn’t appearing somewhere.

-  
A red status indicator () means your app isn’t available in the country or region.

-  
A yellow status indicator () means your app needs action from you before the app is available in the country or region, or the app is currently processing.

-  
A green status indicator () means your app is available in the country or region.

Status

Description

Available

Your app is live on the App Store for users in this country or region.

Available on App Release

Your app is ready to be released in this country or region after your scheduled release date or after you manually release the app. This status only appears if your app has never released in any regions. Learn how to select an App Store version release option.

Pre-Order Pending Developer Release

You've set up a pre-order that publishes in this country or region after you release a version of your app. Learn more.

Pre-Order (Scheduled Release [date])

The pre-order is live and your app will be releases for download or purchase in this country or region on the date indicated. Customers in this country or region can pre-order your app on the store.

Processing to Available

Your app is processing and should be available in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us.

Processing to Not Available

Your app is processing and should no longer be available in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us.

Processing to Pre-Order

Your app is processing and should publish for pre-order in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us.

Not Available

Your app isn't available in this country or region because you've indicated that you don't intend to distribute in this location. Learn how to select the regions where you want to make your app available.

Missing App Rating

Your app isn't available in this country or region because you haven't set an age rating for your app. Learn how to set an app age rating.

Missing Tax Form

Your app isn't available in Brazil because you haven't submitted Brazilian tax information. Learn more.

Missing Game registration number

Your app isn't available in China mainland because you haven't provided an approval number and supporting documents from China's National Press and Publication Administration. Learn more.

ICP Filing Number Missing

Your app isn't available in China mainland because you haven't provided a valid Internet Content Provider (ICP) Filing Number. Learn more.

ICP Filing Number Invalid

Your app isn't available in China mainland because the Internet Content Provider (ICP) Filing Number or metadata you provided doesn't match the information you have filed with China’s Ministry of Industry and Information Technology (MIIT), or both. Learn more.

Cannot Sell App

Your app isn't available in this country or region. Hold the pointer over the status to locate the reason why. If you have any questions, contact us.

Related Overview of submitting for review App build statuses App information Platform version information App bundle information

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/app-build-statuses
### App Store Connect Help

App Store Connect / Reference / App uploads / App build statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# App build statuses

The build status tells you immediately whether your build needs attention. The status applies to the build only, not the entire app.

-  
A red status indicator () means that you need to perform some action or the build is expired.

-  
A yellow status indicator () means that some process is ongoing, controlled either by you or by Apple.

-  
A green status indicator () means the build is being tested in TestFlight.

You can view the builds you upload and their file sizes, beta build status, and metrics under the TestFlight tab in App Store Connect.

Status

Description

Internal testing

External testing

Invalid Binary

Apple received your build, but it didn’t meet all the upload requirements. Resolve any issues in the build, and redeliver. Visit Upload builds.

Not visible in TestFlight

Not visible in TestFlight

Missing Compliance

Your build is missing export compliance documentation. Action is needed. Learn how to provide export compliance for beta builds.

Waiting for Export

Compliance Review

Documentation for export compliance has been submitted and is in review. No action is needed on your end.

In Compliance Review

Documentation for export compliance is in review. No action is needed on your end.

Ready to Submit

Your build can be distributed to internal testers, or can be submitted to TestFlight App Review for external testing or to App Review for distribution to customers.

Waiting for Review

Your build has been submitted to TestFlight App Review. It will need to be approved before you can begin external testing.

In Beta Review

Your build is currently being reviewed by TestFlight App Review. It'll need to be approved before you can begin external testing.

Not Available for Testing

Your build can't be used with TestFlight because the provisioning profile is missing an application identifier. To begin testing, upload a new build that includes the application identifier.

Expired

Your build can't be used for testing with TestFlight because it has passed its 90-day availability window.

Rejected

Your build was rejected by TestFlight App Review and can no longer be used in TestFlight. To begin testing, upload a new build.

Not visible in TestFlight

Not visible in TestFlight

Ready to Test

Your build can be tested by external and internal testers, but you haven’t added any testers yet. You may have opted to manually notify testers after your build is approved. You can also submit your app to App Review for distribution to customers.

Testing

Your build is being tested by at least one group or tester. Click on the build to view more details about who is testing your build. You can continue testing or submit your app to App Review for distribution to customers. Testers that have received an invite to test will still be able to test your build even after it's available for customers.

RelatedApp and submission statuses

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-uploads/build-upload-statuses
### App Store Connect Help

App Store Connect / Reference / App uploads / Build upload statuses 
Filter ⌘K  
Filter ⌘K  

Reference  

# Build upload statuses

The build upload status provides detailed insights into delivery progress, including information, warnings and errors.

State

Description

Processing

Your build upload is still being processed. You'll receive an email notification and the table under Build Uploads will display an updated status when your build has finished processing.

If you upload a build and it remains in the Processing state for more than 24 hours, there may be an issue. To resolve the issue, submit a Feedback Assistant ticket or contact us.

Failed

Your build upload has finished processing, but encountered an issue. Select the build to view potential errors, warnings, and information associated with the failure. Ensure to resolve all errors prior to re-uploading your build. 

Note: If the build upload fails, you can reuse the same build number for your next upload.

Complete 

Your build upload has processed successfully and is now ready for testing. 

Note: If there is a warning badge next to this status, review possible warnings or other information before your next upload.

=== SOURCE: https://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version
### App Store Connect Help

App Store Connect / Update your app / Create a new version 
Filter ⌘K  
Filter ⌘K  

Update your app  

# Create a new version

When you’re ready to distribute a new version of your app, you create a version using the same app record you created for the original version.

Keep in mind that it's not possible to revert to a previous version on the App Store if you have an issue with your app. You must create and submit a new version. Ensure that the current version status is Ready for Distribution to initiate a new version.

Learn about creating a new version using App Store Connect API.

Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the add button (+) next to the desired platform.

-  
In the New Version dialog, enter an incremental App Store version number, then click Create.

-  
Review and enter metadata about the new version.

When you create a new version, the metadata from the current version is automatically transferred to the new version.

For a description of the version properties, visit Platform version information. For the required and localizable properties, refer to Required, localizable, and editable properties.

-  
On the top right, click Save.

-  
Upload your new build to App Store Connect.

In Xcode, increment the build string before you upload your build to App Store Connect, as described in Set the version number and build string.

-  
When you're ready to submit your build, add it to your latest version, then submit your app to App Review.

Related Upload builds Choose a build to submit Add platforms Get started with app discovery and marketing

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers
### App Store Connect Help

App Store Connect / Test a beta version / Invite external testers 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Invite external testers

External testers are people you invite to test your app who aren’t App Store Connect users. After uploading your build, you can invite up to 10,000 external testers per app. To make your build available for external testing, you need to create an external group, add builds, and invite testers using their email addresses or by sharing a public invitation link.

When inviting testers via a public link, you can set tester criteria, such as device and OS requirements, ensuring only qualified testers can accept the invitation. This facilitates the enrollment of relevant testers, who can then provide feedback for your beta app. Learn how to set tester criteria when inviting testers using a public link.

Keep in mind that:

-  
To create an external group for external testing, you must first create an internal group for internal testing.

-  
Builds uploaded as TestFlight Internal Only from Xcode or Xcode Cloud are marked as internal under the build number and can only be added to internal tester groups.

-  
Managed Apple Accounts created in reserved domains can’t be used to test builds. Learn more about reserved domains in Apple School Manager or Apple Business.

Learn how to manage tester invitations with the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Create a group

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, click the add button (+) next to External Testing to add a new group.

-  
In the dialog that appears, enter a group name, then click Create.

Later, you can change the name of the group if needed.

### Add builds to a group

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select the group to which you want to add builds.

-  
On the right, click Add Builds to choose which builds you want to add to this group.

Note: If you plan to invite testers using a public link and set criteria, ensure that the builds you add to the group are compatible with the criteria you’ve set. You can review the insight cards at the top of the group's details page to check for any incompatible builds that have been added.

Note: You can add only one build at a time, but you can add more later. To add additional builds to a group, click the add button (+) next to Builds on the tester group page.

-  
In the build dialog, select the platform and version from the pop-up menus.

-  
In the table, select a build, then click Add.

-  
In the What to Test dialog, enter what you want testers to focus on.

-  
Optionally, enter localized versions of testing information in the text fields under each language-specific section.

-  
Optionally, select "Automatically notify testers."

If you leave this checkbox deselected, you must manually distribute the build to testers after it's approved by TestFlight App Review.

-  
Depending on the build's status, click either Submit Review or Start Testing.

You can only have one build of each version in review at a time. Once that build is approved, you can submit additional builds.

If your build uses Apple-hosted asset packs, make sure to submit the latest versions of any asset packs needed for testing after submitting the build.

Note: You can submit up to six builds for TestFlight App Review within a 24-hour period.

After you submit your build to TestFlight App Review, Apple reviews the build and its accompanying metadata. The first build you submit requires a full review, but later builds for the same version might not.

If Apple approves your build for TestFlight beta testing, users on the App Store Connect account with the Admin role will receive an email notifying them of the approval.

If Apple rejects your build or metadata, the status of the build will be Rejected. You can click App Review from the sidebar under General to view the rejection details for your beta build.

Note: Enter test information, such as Feedback Email and Contact Information, if these details haven’t been provided in the Test information dialog.

## Invite external testers using a public link or email

Once you have builds available to test, and you've added them to a group, you can invite testers. You can Invite testers using a public link, email, or both. When inviting testers using a public link, you can set tester criteria.

### Invite testers using a public link

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select a group.

-  
Under the testers tab, click Create Public Link.

-  
In the dialog that appears, select either Open to Anyone or Filter by Criteria.

-  
Open to Anyone. Anyone can join using the link.

-  
Filter by Criteria. Filter who can join by device or platform.

Optionally, under Tester Limit, click Set Limit to limit the number of testers who can join this testing group using the public link. Enter a number between 1 and 10,000.

-  
If you select Open to Anyone, click Confirm, then copy the link and share it using social media, messages, email, or other channels.

If you select Filter by Criteria, click Next, and then follow the steps below.

-  
In the dialog that appears, click Add Criteria. You need to add at least one criteria to invite testers.

-  
In the drop-down menu, select the device you want to add criteria for, then select the OS details. You can add multiple criteria as needed.

-  
From. Only allow testers using the OS version in the specified range to test your app.

-  
Newer than or equal to. Only allow testers using the specified OS version or newer to test your app.

-  
Older than or equal to. Only allow testers using the specified OS version or older to test your app.

-  
All supported (for platform). Allow testers with any OS version for the selected platform to test your app.

-  
After adding all your criteria, click Confirm. Then, copy the link and share it on social media, messaging apps, email, or any other channel.

Once you have created your public link, you can add or edit criteria, set or change a tester limit, make the link available to everyone, or disable it. Click Manage next to Public Link to open the dialog, make your changes, and then click Save.

Tip: Check the insight cards at the top of the group details page to identify if there are no compatible builds, if the public link is full, or if a build is about to expire.

View public link metrics to evaluate its performance and review feedback testers may have provided.

Keep in mind that anyone can share this link, so testers could potentially join your testing group even if you do not invite them directly.

If a tester joins your group using a public link, their name and email won’t be displayed in the Testers section in App Store Connect—it will display as anonymous. However, their installation date, sessions, and crashes will be displayed. You can make the public link deactivate at any time.

### Invite testers using their email address

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select a group.

-  
Click the add button (+) next to Testers.

-  
In the pop-up menu that appears, choose an option. You can add new testers using their email address, existing testers you've previously added, or import testers from a CSV file.

When you invite testers, they will receive an invitation email to begin testing. If a tester accepts an email invitation, their name, email address, installation date, sessions, and crashes, will display in the Testers section in App Store Connect.

Tip: To add users with a specific device type to a group, click Add Filter and select devices to filter by. Select all testers using the checkbox at the top of the table or select testers individually, then click Add to Group. In the dialog that appears, select the eligible groups you want to add these testers to and click Add.

### Notify external testers after your build is approved

If you didn’t select “Automatically notify testers” when you added your build to your group, you must manually notify testers once your build is approved.

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under Builds, click the platform for your app.

-  
Choose a version, then under Status, click Notify Testers for the build row.

The build status changes to Testing. External testers will then receive a notification directing them to accept the invitation using the TestFlight app on their device.

### Remove a build from a group

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under External Testing, select a group.

-  
On the right, under Builds, hold the pointer over the build you want to remove.

-  
Click the delete button.

-  
In the dialog that appears, confirm you want to remove the build from the group and click Remove.

If you want to remove a build from testing for all your testers, go to Stop testing a build.

###   FAQs

### How do I appeal if my beta build was rejected?

To appeal your beta build being rejected, contact TestFlight App Review.

Related TestFlight Overview Add internal testers View and manage tester information

=== SOURCE: https://developer.apple.com/help/app-store-connect/update-your-app/overview-of-maintaining-an-app
### App Store Connect Help

App Store Connect / Update your app / Overview of maintaining an app 
Filter ⌘K  
Filter ⌘K  

Update your app  

# Overview of maintaining an app

After you publish your app, you perform a number of tasks to respond to customer feedback and to maintain your app throughout its lifetime. You can perform these tasks in any order.

## Create a new version

When you’re ready to distribute a new build of your app, you create a new version using the same app record as your previous version. You can update the metadata for the new app version and add a description of the new features.

## Download catalog reports

If you have several apps in your account, generate catalog reports that detail the information and settings for all your organization’s apps, including In-App Purchase, and metadata for Game Center leaderboards and achievements.

## Monitor App Store customer reviews, sales, and analytics

You can read and respond to reviews. To better understand how your app is doing, you can view sales and trends and view app analytics, such as crashes, sessions, and active users.

## Change App Store pricing and availability

You can change the price, schedule price changes, and change the countries or regions for your app on the App Store at any time. Scheduling price changes is useful for promotions that have start and end dates.

## Remove an app

If you no longer want your app to be available to customers, you can remove it from the App Store, which removes all versions of the app.

Related App and submission statuses Release a version update in phases Ratings and reviews overview Overview of reporting tools

=== SOURCE: https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information
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

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-export-compliance-information-for-beta-builds
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

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-test-information
### App Store Connect Help

App Store Connect / Test a beta version / Provide test information 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Provide test information

When you distribute your app to external testers, you need to enter additional TestFlight test information about your app for TestFlight App Review. You can enter this information when you add your app to your account or before you invite external testers.

Learn how to provide test information using the App Store Connect API.

Required role: Account Holder, Admin, and App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
Click the TestFlight tab.

-  
In the sidebar, under Additional, click Test Information.

-  
On the right, choose a language option and enter the required test information.

The information you enter for your beta app can differ from the information you enter later when submitting your app to the App Store.

-  
Under Invitation Experience, the App Information checkbox is selected by default. This means that your approved screenshots and app category automatically display in your invite. This information will be pulled from the latest approved version in the Ready for Distribution state.

If you prefer not to display the screenshots or app category in your invite, you can deselect the App Information checkbox.

-  
In the Beta App Description text field, enter a description of your beta version. This field is required.

-  
In the Feedback Email field, enter the email address where testers can contact you through the TestFlight app. This is also the reply-to address in email invitations to testers.

Learn about the TestFlight App Review information properties.

You can update this information at any time, and the updates will display in the TestFlight app.

Related TestFlight Overview Testing Apps with TestFlight

=== SOURCE: https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases
### App Store Connect Help

App Store Connect / Update your app / Release a version update in phases 
Filter ⌘K  
Filter ⌘K  

Update your app  

# Release a version update in phases

iOS macOS tvOS  
When you release a version update of your app, you can choose to release the new version to the App Store in stages. This option is available when you submit a version update and your app has one of the following statuses:

-  
Prepare for Submission

-  
Waiting for Review

-  
In Review

-  
Waiting for Export Compliance

-  
Pending Developer Release

-  
Developer Rejected

-  
Rejected

-  
Metadata Rejected

Selecting this option will release your app's update gradually over 7 days. A random sample of users with automatic updates on eligible devices will receive the update, without any notification of their participation in the phased release.

Day of Phased Release

Percentage of Users

1

1%

2

2%

3

5%

4

10%

5

20%

6

50%

7

100%

Keep in mind that apps and app updates in phased release can be manually downloaded from the App Store by anyone at any time.

During phased release, you may pause the release for up to 30 days, with no limit on the number of pauses. If you remove your app from sale — including when your Apple Developer Program membership lapses — phased release will stop and won't be available for that version again. When your app is reinstated, it becomes available to all users immediately, regardless of the percentage reached before removal. To resume a controlled rollout, make the version unavailable for download and submit a new version update with phased release enabled.

Learn how to manage phased releases using the App Store Connect API.

Required role: Account Holder, Admin, or App Manager. View role permissions.

## Release a version update in phases

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version you want to submit.

-  
On the right, scroll down to the Phased Release for Automatic Updates section, select Release update over a 7-day period using phased release.

-  
Click save.

When you submit your app for review and it's approved, the app status will be Ready for Distribution, and will be appended with “Phased Release” next to the status when viewing your app's version page.

When the update is complete, all users with Admin or App Manager roles who have access to this app will receive a notification regarding the completion of the phased release.

### Pause and resume a phased release

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the Ready for Distribution app version.

-  
In the Phased Release for Automatic Updates section, you can either pause the release by selecting Pause Phased Release or resume it by using the Use Phased Release option.

-  
Click Save.

You can pause your release for a total of 30 days. For example, if you pause the release for 10 days and then choose to resume it, you will have 20 days remaining to pause the release again. If you resume a release that was previously paused, your phased release will pick up on the day it was left off when it was paused.

### Release a version update to all users

If you decide to release your app in phases, you can release it to all users at any time once it has the Ready for Distribution status. When you select this option, all users whose devices have automatic updates turned on gets the latest app version supported on the user’s device.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version that you've submitted.

-  
On the top right of the page, click Release to All Users.

=== SOURCE: https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-an-app-store-version-release-option
### App Store Connect Help

App Store Connect / Manage your app's availability / Select an App Store version release option 
Filter ⌘K  
Filter ⌘K  

Manage your app's availability  

# Select an App Store version release option

You can choose a release option for each platform version of your app in App Store Connect.

Note: If you’re setting up your app for pre-order in a country or region and haven't yet released it on the App Store, you'll need to release the app version manually. The App Store Version Release section will be dimmed and "Release the app yourself" will be automatically selected.

Required role: Account Holder, Admin, or App Manager. View role permissions.

-  
In Apps, select the app you want to view.

-  
In the sidebar, click the app version you want to set a release option for.

-  
In the App Store Version Release section, select a release option:

-  
Release the app yourself: Select “Manually release this version.” (Later, manually release the version.)

-  
Automatically release the app after approval: Select “Automatically release this version.”

-  
Automatically release the app but no earlier than a specified date: Select “Automatically release this version after App Review, no earlier than” and below this option, enter a date and time.

-  
On the top right of the page, click Save.

## Manually release a version to the App Store

When submitting your app for review, you can manually release a version. After approval, release it to the App Store once its status changes to Pending Developer Release.

Releasing an app version is specific to the platform you're working with. If there are app versions for other platforms also in "Pending Developer Release" that you want to release, you must manually release each one for every platform.

Apple will send you an email reminder if an app remains in Pending Developer Release status for more than 30 days.

Learn how to manually release a version with the App Store Connect API.

-  
In Apps, select the app you want to view.

-  
In the sidebar, select the app version that has the status of Pending Developer Release.

-  
On the top right, click Release This Version.

-  
In the dialog that appears, click Confirm.

After manually releasing your app version, it may take up to 24 hours for it to appear on the App Store. To cancel the release, select Cancel This Release from the message on the version page.

Note: When you choose Release This Version, the new app will publish for pre-order in countries or regions where pre-order is enabled. It’ll also be available for download or purchase in any country or region where the App Store status is Available or Available on App Release. Learn more.

Related App Store pricing and availability start times by country or region App and submission statuses

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview
### App Store Connect Help

App Store Connect / Test a beta version / TestFlight overview 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# TestFlight Overview

iOS macOS visionOS tvOS watchOS  
TestFlight lets you distribute beta builds of your app, manage beta testers, and collect feedback. Learn more. 

Make improvements to your app and continue distributing builds until all issues are resolved before you submit your app for review.

To use TestFlight for Mac, build your macOS apps with Xcode 13 or later. If your app includes an App Clip, you can invite testers to test the App Clip experience on its own. Testers who are invited to test your app can test both the app and the App Clip. Either the app or the App Clip can be installed on a device at a time. Testers can choose to switch between them at any time.

Learn how to manage beta testing using the App Store Connect API.

## Step 1: Provide test information

Provide test information about your app, such as a beta app description, an explanation of features to test, and an email address where feedback can be submitted. You can also choose to show approved app screenshots and your app category.

### Step 2: Upload your build or assets

Upload your build to App Store Connect. Read Cryptography and US export compliance to determine if you need to provide app encryption documentation for your app. You can test a build for up to 90 days.

Note: For builds to be eligible for TestFlight, they must include application identifiers within the provisioning profiles.

You also have the option to upload assets that are managed separately from a build by using Apple-Hosted Background Assets.

### Step 3: Invite internal and external testers

Create groups for testers, then assign specific builds to them. After you've added builds to a group, you can add external testers (up to 10,000 people) and internal testers (up to 100 App Store Connect users with access to your content) to test your app. If you invite external testers, your beta build may require review. When you add the first build of your app to a group, the build gets sent to App Review to make sure it follows the App Review Guidelines. A review is required only for the first build. Subsequent builds may not require a full review. Testing can begin once a build is approved.

Note: Managed Apple Accounts created in reserved domains can’t be used to test builds. Learn more about reserved domains in Apple School Manager or Apple Business.

### Step 4: Testers download TestFlight and accept your invitations

Testers install the free TestFlight app on their devices. Then they use their invitation email or a public link to accept invitations, install your app, send feedback, and get updates. Testers download and install thinned variants of your app.

Note: Setting specific criteria for your public link invitations can limit the number of external testers who can test your app.

### Step 5: View tester and build information

Track tester engagement and your app's performance by viewing build status and metrics. These metrics include the number of sessions and crashes. Also, you can resend email invitations to testers who haven't accepted their invitation.  

### Step 6: Collect feedback from testers

Testers using TestFlight version 2.3 or later on iOS, macOS, and visionOS can submit feedback either through the TestFlight app or by taking a screenshot directly within your beta app. You can view this tester feedback in the TestFlight Feedback section in App Store Connect. Testers running tvOS or earlier versions of iOS can send feedback to the email address you specified in step 1.

### Step 7: Stop testing

When testing is complete, you have the option to expire a build to stop testing it. If you don’t expire your build and submit it to the App Store, testers who received an invitation to test will still be able to test your build even after it goes live on the App Store. Your build becomes unavailable for testers after 90 days.

Related Upload builds Overview of publishing your app on the App Store Overview of submitting for review Get started with TestFlight

=== SOURCE: https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight
### App Store Connect Help

App Store Connect / Test a beta version / Testing subscriptions and In-App Purchases in TestFlight 
Filter ⌘K  
Filter ⌘K  

Test a beta version  

# Testing subscriptions and In-App Purchases in TestFlight

## Subscription renewal rate in TestFlight

When testing your app's subscriptions in TestFlight, the renewal rate is accelerated. Each subscription is renewed daily, up to 6 times within a 1-week period, regardless of the subscription's duration.

Learn more about testing In-App Purchases with sandbox.

Important: To test different renewal rates in TestFlight, you can use your Sandbox Apple Account. Learn more about managing Sandbox Apple Account settings.

Renewal for all durations

1 week

1 month

2 months

3 months

6 months

1 year

Subscription renewal speed

1 Day

1 Day

1 Day

1 Day

1 Day

1 Day

Example scenario: If you start a 1-month subscription on February 1st, it'll renew every 24 hours for a total of 6 renewals before being canceled. Since subscriptions renew at an accelerated rate in TestFlight, you'll see a new transaction for each renewal on February 2nd, 3rd, 4th, 5th, 6th, and 7th. The subscription's auto-renewal will then be disabled on February 8th.

Note: To test subscriptions entering or exiting billing retry, you must test with a Sandbox Apple Account to subscribe and use the sandbox account settings to simulate this scenario. Learn more about testing failing subscription renewals and In-App Purchases.

### Test In-App Purchase scenarios in TestFlight with your Sandbox Apple Account

Apps downloaded from TestFlight will automatically operate in a sandbox environment. However, to test different In-App Purchase scenarios in TestFlight, you can use your Sandbox Apple Account. First, sign out of your production Apple Account under Media & Purchases. Then, go to Developer settings and sign in with your Sandbox Apple Account to access the sandbox controls for testing. For more details, please refer to the  Sign in to your Sandbox Apple Account for TestFlight section.

To learn more about the different In-App Purchase scenarios you can test with your Sandbox Apple Account, visit the Manage Sandbox Apple Account settings page.

Note:  You can only use a Sandbox Apple Account to test apps within your own developer account.

