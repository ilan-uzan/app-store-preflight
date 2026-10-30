# TestFlight, Builds, Statuses, Updates and Release Options
Source: https://developer.apple.com/help/app-store-connect/  
Retrieved: 2026-10-30

## BUILD.1 TestFlight Overview

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> TestFlight lets you distribute beta builds of your app, manage beta testers, and collect feedback. Learn more.
>
> Make improvements to your app and continue distributing builds until all issues are resolved before you submit your app for review.
>
> To use TestFlight for Mac, build your macOS apps with Xcode 13 or later. If your app includes an App Clip, you can invite testers to test the App Clip experience on its own. Testers who are invited to test your app can test both the app and the App Clip. Either the app or the App Clip can be installed on a device at a time. Testers can choose to switch between them at any time.
>
> Learn how to manage beta testing using the App Store Connect API.

**Applies to:** All apps distributed with TestFlight; "To use TestFlight for Mac" applies to macOS apps

- **[BUILD-01]** Have issues found during TestFlight testing been resolved before the app is submitted for review?
  - quote: "continue distributing builds until all issues are resolved before you submit your app for review"
  - surface: manual
  - verify: App Store Connect > Apps > [app] > TestFlight > Feedback (screenshots and crashes) and build metrics; confirm that no open tester-reported issues remain for the build you plan to submit.
  - fix: Fix the reported issues, upload a new build, and distribute it in TestFlight again before submitting to App Review.
- **[BUILD-02]** If you use TestFlight for a macOS app, was the build made with Xcode 13 or later?
  - quote: "To use TestFlight for Mac, build your macOS apps with Xcode 13 or later."
  - surface: code
  - verify: Check the Xcode version used to archive the macOS build (Xcode > About Xcode on the build machine, or the DTXcode / DTXcodeBuild keys in the archived app's Info.plist).
  - fix: Archive and upload the macOS build again with Xcode 13 or later.

## BUILD.2 TestFlight Overview — Step 1: Provide test information

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> Provide test information about your app, such as a beta app description, an explanation of features to test, and an email address where feedback can be submitted. You can also choose to show approved app screenshots and your app category.

**Applies to:** Apps distributed with TestFlight

- **[BUILD-03]** Has test information been entered for the app, including a beta app description, an explanation of features to test, and a feedback email address?
  - quote: "Provide test information about your app, such as a beta app description, an explanation of features to test, and an email address where feedback can be submitted."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > TestFlight > Additional > Test Information: check Beta App Description and Feedback Email; for each build in an external group, check its What to Test text.
  - fix: Fill in Beta App Description, Feedback Email and What to Test, then click Save.

## BUILD.3 TestFlight Overview — Step 2: Upload your build or assets

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> Upload your build to App Store Connect. Read Cryptography and US export compliance to determine if you need to provide app encryption documentation for your app. You can test a build for up to 90 days.
>
> Note: For builds to be eligible for TestFlight, they must include application identifiers within the provisioning profiles.
>
> You also have the option to upload assets that are managed separately from a build by using Apple-Hosted Background Assets.

**Applies to:** Apps distributed with TestFlight

- **[BUILD-04]** Does the provisioning profile used to sign the build include an application identifier?
  - quote: "For builds to be eligible for TestFlight, they must include application identifiers within the provisioning profiles."
  - surface: code
  - verify: In Xcode > target > Signing & Capabilities, check the distribution provisioning profile. Then inspect the embedded.mobileprovision in the archive (`security cms -D -i embedded.mobileprovision`) and confirm that the Entitlements contain `application-identifier`.
  - fix: Sign with a provisioning profile that includes the application identifier, re-archive, and upload a new build.
- **[BUILD-05]** Have you determined whether the app needs app encryption documentation (Cryptography and US export compliance)?
  - quote: "Read Cryptography and US export compliance to determine if you need to provide app encryption documentation for your app."
  - surface: code
  - verify: Review the app's use of encryption, including any third-party SDKs. Check Info.plist for the encryption setting (ITSAppUsesNonExemptEncryption).
  - fix: manual — requires developer decision/legal/business action
- **[BUILD-06]** Is the build being tested less than 90 days old?
  - quote: "You can test a build for up to 90 days."
  - surface: asc
  - verify: App Store Connect > TestFlight > Builds > [platform]: check the build's upload date and any expiry indicator.
  - fix: Increment the build string, then upload a new build.

## BUILD.4 TestFlight Overview — Step 3: Invite internal and external testers

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> Create groups for testers, then assign specific builds to them. After you've added builds to a group, you can add external testers (up to 10,000 people) and internal testers (up to 100 App Store Connect users with access to your content) to test your app. If you invite external testers, your beta build may require review. When you add the first build of your app to a group, the build gets sent to App Review to make sure it follows the App Review Guidelines. A review is required only for the first build. Subsequent builds may not require a full review. Testing can begin once a build is approved.
>
> Note: Managed Apple Accounts created in reserved domains can’t be used to test builds. Learn more about reserved domains in Apple School Manager or Apple Business.

**Applies to:** Apps distributed with TestFlight; review applies when you invite external testers

- **[BUILD-07]** If you plan external testing, does the beta build follow the App Review Guidelines? The first build added to a group is sent to App Review.
  - quote: "When you add the first build of your app to a group, the build gets sent to App Review to make sure it follows the App Review Guidelines."
  - surface: manual
  - verify: Before adding the first build to an external group, run the guideline checks in this skill against that build.
  - fix: Resolve any guideline issues, upload a new build, and add it to the external group.

## BUILD.5 TestFlight Overview — Step 4: Testers download TestFlight and accept your invitations

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> Testers install the free TestFlight app on their devices. Then they use their invitation email or a public link to accept invitations, install your app, send feedback, and get updates. Testers download and install thinned variants of your app.
>
> Note: Setting specific criteria for your public link invitations can limit the number of external testers who can test your app.

**Applies to:** Apps distributed with TestFlight

## BUILD.6 TestFlight Overview — Step 5: View tester and build information

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> Track tester engagement and your app's performance by viewing build status and metrics. These metrics include the number of sessions and crashes. Also, you can resend email invitations to testers who haven't accepted their invitation.

**Applies to:** Apps distributed with TestFlight

## BUILD.7 TestFlight Overview — Step 6: Collect feedback from testers

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> Testers using TestFlight version 2.3 or later on iOS, macOS, and visionOS can submit feedback either through the TestFlight app or by taking a screenshot directly within your beta app. You can view this tester feedback in the TestFlight Feedback section in App Store Connect. Testers running tvOS or earlier versions of iOS can send feedback to the email address you specified in step 1.

**Applies to:** Apps distributed with TestFlight

## BUILD.8 TestFlight Overview — Step 7: Stop testing

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview

**Source text (verbatim):**
> When testing is complete, you have the option to expire a build to stop testing it. If you don’t expire your build and submit it to the App Store, testers who received an invitation to test will still be able to test your build even after it goes live on the App Store. Your build becomes unavailable for testers after 90 days.

**Applies to:** Apps distributed with TestFlight

- **[BUILD-08]** Have you decided whether to expire the TestFlight build before release? If you don't expire it, invited testers can keep testing it after it goes live on the App Store.
  - quote: "If you don’t expire your build and submit it to the App Store, testers who received an invitation to test will still be able to test your build even after it goes live on the App Store."
  - surface: asc
  - verify: App Store Connect > TestFlight > Builds > [platform] > [build]: check whether testing is still active for the build you will submit.
  - fix: manual — requires developer decision/legal/business action

## BUILD.9 Provide test information

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-test-information

**Source text (verbatim):**
> When you distribute your app to external testers, you need to enter additional TestFlight test information about your app for TestFlight App Review. You can enter this information when you add your app to your account or before you invite external testers.
>
> Learn how to provide test information using the App Store Connect API.
>
> Required role: Account Holder, Admin, and App Manager. View role permissions.
>
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, under Additional, click Test Information.
> - On the right, choose a language option and enter the required test information.
>
> The information you enter for your beta app can differ from the information you enter later when submitting your app to the App Store.
>
> - Under Invitation Experience, the App Information checkbox is selected by default. This means that your approved screenshots and app category automatically display in your invite. This information will be pulled from the latest approved version in the Ready for Distribution state.
>
> If you prefer not to display the screenshots or app category in your invite, you can deselect the App Information checkbox.
>
> - In the Beta App Description text field, enter a description of your beta version. This field is required.
> - In the Feedback Email field, enter the email address where testers can contact you through the TestFlight app. This is also the reply-to address in email invitations to testers.
>
> Learn about the TestFlight App Review information properties.
>
> You can update this information at any time, and the updates will display in the TestFlight app.

**Applies to:** When you distribute your app to external testers

- **[BUILD-09]** Has the required test information been entered for TestFlight App Review before you invite external testers?
  - quote: "When you distribute your app to external testers, you need to enter additional TestFlight test information about your app for TestFlight App Review."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > TestFlight > Additional > Test Information: for each language option, check that the required fields are filled in.
  - fix: Enter the required test information for each language option and click Save.
- **[BUILD-10]** Is the Beta App Description field filled in?
  - quote: "In the Beta App Description text field, enter a description of your beta version. This field is required."
  - surface: asc
  - verify: TestFlight > Test Information > Beta App Description is not empty.
  - fix: Write a description of the beta version in Beta App Description and save.
- **[BUILD-11]** Does the Feedback Email field hold an email address where testers can reach you?
  - quote: "In the Feedback Email field, enter the email address where testers can contact you through the TestFlight app."
  - surface: asc
  - verify: TestFlight > Test Information > Feedback Email holds a monitored address. It is also the reply-to address in tester invitation emails.
  - fix: Enter a monitored email address in Feedback Email and save.

## BUILD.10 Invite external testers

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> External testers are people you invite to test your app who aren’t App Store Connect users. After uploading your build, you can invite up to 10,000 external testers per app. To make your build available for external testing, you need to create an external group, add builds, and invite testers using their email addresses or by sharing a public invitation link.
>
> When inviting testers via a public link, you can set tester criteria, such as device and OS requirements, ensuring only qualified testers can accept the invitation. This facilitates the enrollment of relevant testers, who can then provide feedback for your beta app. Learn how to set tester criteria when inviting testers using a public link.
>
> Keep in mind that:
>
> - To create an external group for external testing, you must first create an internal group for internal testing.
> - Builds uploaded as TestFlight Internal Only from Xcode or Xcode Cloud are marked as internal under the build number and can only be added to internal tester groups.
> - Managed Apple Accounts created in reserved domains can’t be used to test builds. Learn more about reserved domains in Apple School Manager or Apple Business.
>
> Learn how to manage tester invitations with the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** Apps tested with external testers

- **[BUILD-12]** If you plan external testing, does an internal testing group exist?
  - quote: "To create an external group for external testing, you must first create an internal group for internal testing."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > TestFlight sidebar: check that at least one group is listed under Internal Testing.
  - fix: Create an internal group for internal testing before you create the external group.
- **[BUILD-13]** If the build is meant for external testers, was it uploaded without the TestFlight Internal Only option?
  - quote: "Builds uploaded as TestFlight Internal Only from Xcode or Xcode Cloud are marked as internal under the build number and can only be added to internal tester groups."
  - surface: asc
  - verify: TestFlight > Builds > [platform]: check whether the build is marked "internal" under its build number. Also check the Xcode Organizer distribution choice or the Xcode Cloud workflow's TestFlight distribution setting.
  - fix: Upload a new build (with an incremented build string) using a distribution method that is not TestFlight Internal Only.
- **[BUILD-59]** For external testing, has an external group been created, builds added to it, and testers invited by email or public link?
  - quote: "To make your build available for external testing, you need to create an external group, add builds, and invite testers using their email addresses or by sharing a public invitation link."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > TestFlight sidebar > External Testing: check that a group exists, that it has a build, and that it has testers or a public link.
  - fix: Create an external group, add the build, and invite testers by email or public link.

## BUILD.11 Invite external testers — Create a group

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, click the add button (+) next to External Testing to add a new group.
> - In the dialog that appears, enter a group name, then click Create.
>
> Later, you can change the name of the group if needed.

**Applies to:** Apps tested with external testers

## BUILD.12 Invite external testers — Add builds to a group

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, under External Testing, select the group to which you want to add builds.
> - On the right, click Add Builds to choose which builds you want to add to this group.
>
> Note: If you plan to invite testers using a public link and set criteria, ensure that the builds you add to the group are compatible with the criteria you’ve set. You can review the insight cards at the top of the group's details page to check for any incompatible builds that have been added.
>
> Note: You can add only one build at a time, but you can add more later. To add additional builds to a group, click the add button (+) next to Builds on the tester group page.
>
> - In the build dialog, select the platform and version from the pop-up menus.
> - In the table, select a build, then click Add.
> - In the What to Test dialog, enter what you want testers to focus on.
> - Optionally, enter localized versions of testing information in the text fields under each language-specific section.
> - Optionally, select "Automatically notify testers."
>
> If you leave this checkbox deselected, you must manually distribute the build to testers after it's approved by TestFlight App Review.
>
> - Depending on the build's status, click either Submit Review or Start Testing.
>
> You can only have one build of each version in review at a time. Once that build is approved, you can submit additional builds.
>
> If your build uses Apple-hosted asset packs, make sure to submit the latest versions of any asset packs needed for testing after submitting the build.
>
> Note: You can submit up to six builds for TestFlight App Review within a 24-hour period.
>
> After you submit your build to TestFlight App Review, Apple reviews the build and its accompanying metadata. The first build you submit requires a full review, but later builds for the same version might not.
>
> If Apple approves your build for TestFlight beta testing, users on the App Store Connect account with the Admin role will receive an email notifying them of the approval.
>
> If Apple rejects your build or metadata, the status of the build will be Rejected. You can click App Review from the sidebar under General to view the rejection details for your beta build.
>
> Note: Enter test information, such as Feedback Email and Contact Information, if these details haven’t been provided in the Test information dialog.

**Applies to:** Builds submitted to TestFlight App Review for external testing

- **[BUILD-60]** If you invite testers by public link with criteria, are the builds in the group compatible with those criteria?
  - quote: "If you plan to invite testers using a public link and set criteria, ensure that the builds you add to the group are compatible with the criteria you’ve set."
  - surface: asc
  - verify: TestFlight > External Testing > [group]: review the insight cards at the top of the group's details page for incompatible builds.
  - fix: Add builds that match the criteria, or change the public link criteria.
- **[BUILD-14]** Has What to Test text been entered for the build, saying what testers should focus on?
  - quote: "In the What to Test dialog, enter what you want testers to focus on."
  - surface: asc
  - verify: TestFlight > Builds > [platform] > [build] > Test Details: check the What to Test field (and its localized versions, if used).
  - fix: Enter What to Test text describing the features or changes testers should focus on.
- **[BUILD-15]** Have test information details such as Feedback Email and Contact Information been provided before the build is submitted for TestFlight App Review?
  - quote: "Enter test information, such as Feedback Email and Contact Information, if these details haven’t been provided in the Test information dialog."
  - surface: asc
  - verify: TestFlight > Additional > Test Information: check that the Feedback Email and the contact information fields are filled in.
  - fix: Fill in the missing test information fields and save, then submit the build for review.
- **[BUILD-16]** Is only one build of this version in TestFlight App Review at a time?
  - quote: "You can only have one build of each version in review at a time."
  - surface: asc
  - verify: TestFlight > Builds > [platform] > [version]: check whether another build of the same version has status Waiting for Review or In Beta Review.
  - fix: Wait until the build in review is approved, then submit the next build.
- **[BUILD-17]** Have you submitted no more than six builds for TestFlight App Review in the last 24 hours?
  - quote: "You can submit up to six builds for TestFlight App Review within a 24-hour period."
  - surface: asc
  - verify: TestFlight > Builds: count the builds submitted for TestFlight App Review in the last 24 hours.
  - fix: Wait until the 24-hour window allows another submission.
- **[BUILD-18]** If the build uses Apple-hosted asset packs, were the latest versions of the asset packs needed for testing submitted after the build?
  - quote: "If your build uses Apple-hosted asset packs, make sure to submit the latest versions of any asset packs needed for testing after submitting the build."
  - surface: asc
  - verify: Check whether the build uses Apple-hosted asset packs. If it does, check in App Store Connect that the latest versions of the asset packs needed for testing were submitted after the build.
  - fix: Submit the latest versions of the required asset packs after submitting the build.
- **[BUILD-19]** If "Automatically notify testers" was left unselected, have testers been notified manually after approval?
  - quote: "If you leave this checkbox deselected, you must manually distribute the build to testers after it's approved by TestFlight App Review."
  - surface: asc
  - verify: TestFlight > Builds > [platform] > [version]: check whether the build row still shows Notify Testers under Status.
  - fix: Click Notify Testers for the approved build row.

## BUILD.13 Invite external testers — Invite external testers using a public link or email

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> Once you have builds available to test, and you've added them to a group, you can invite testers. You can Invite testers using a public link, email, or both. When inviting testers using a public link, you can set tester criteria.

**Applies to:** Apps tested with external testers

## BUILD.14 Invite external testers — Invite testers using a public link

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, under External Testing, select a group.
> - Under the testers tab, click Create Public Link.
> - In the dialog that appears, select either Open to Anyone or Filter by Criteria.
> - Open to Anyone. Anyone can join using the link.
> - Filter by Criteria. Filter who can join by device or platform.
>
> Optionally, under Tester Limit, click Set Limit to limit the number of testers who can join this testing group using the public link. Enter a number between 1 and 10,000.
>
> - If you select Open to Anyone, click Confirm, then copy the link and share it using social media, messages, email, or other channels.
>
> If you select Filter by Criteria, click Next, and then follow the steps below.
>
> - In the dialog that appears, click Add Criteria. You need to add at least one criteria to invite testers.
> - In the drop-down menu, select the device you want to add criteria for, then select the OS details. You can add multiple criteria as needed.
> - From. Only allow testers using the OS version in the specified range to test your app.
> - Newer than or equal to. Only allow testers using the specified OS version or newer to test your app.
> - Older than or equal to. Only allow testers using the specified OS version or older to test your app.
> - All supported (for platform). Allow testers with any OS version for the selected platform to test your app.
> - After adding all your criteria, click Confirm. Then, copy the link and share it on social media, messaging apps, email, or any other channel.
>
> Once you have created your public link, you can add or edit criteria, set or change a tester limit, make the link available to everyone, or disable it. Click Manage next to Public Link to open the dialog, make your changes, and then click Save.
>
> Tip: Check the insight cards at the top of the group details page to identify if there are no compatible builds, if the public link is full, or if a build is about to expire.
>
> View public link metrics to evaluate its performance and review feedback testers may have provided.
>
> Keep in mind that anyone can share this link, so testers could potentially join your testing group even if you do not invite them directly.
>
> If a tester joins your group using a public link, their name and email won’t be displayed in the Testers section in App Store Connect—it will display as anonymous. However, their installation date, sessions, and crashes will be displayed. You can make the public link deactivate at any time.

**Applies to:** Apps tested with external testers invited by public link

- **[BUILD-61]** If you set tester criteria for a public link, has at least one criterion been added?
  - quote: "You need to add at least one criteria to invite testers."
  - surface: asc
  - verify: TestFlight > External Testing > [group] > Manage next to Public Link: check that at least one criterion is listed.
  - fix: Click Add Criteria, add at least one criterion, click Confirm, then share the link.

## BUILD.15 Invite external testers — Invite testers using their email address

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, under External Testing, select a group.
> - Click the add button (+) next to Testers.
> - In the pop-up menu that appears, choose an option. You can add new testers using their email address, existing testers you've previously added, or import testers from a CSV file.
>
> When you invite testers, they will receive an invitation email to begin testing. If a tester accepts an email invitation, their name, email address, installation date, sessions, and crashes, will display in the Testers section in App Store Connect.
>
> Tip: To add users with a specific device type to a group, click Add Filter and select devices to filter by. Select all testers using the checkbox at the top of the table or select testers individually, then click Add to Group. In the dialog that appears, select the eligible groups you want to add these testers to and click Add.

**Applies to:** Apps tested with external testers invited by email

## BUILD.16 Invite external testers — Notify external testers after your build is approved

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> If you didn’t select “Automatically notify testers” when you added your build to your group, you must manually notify testers once your build is approved.
>
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, under Builds, click the platform for your app.
> - Choose a version, then under Status, click Notify Testers for the build row.
>
> The build status changes to Testing. External testers will then receive a notification directing them to accept the invitation using the TestFlight app on their device.

**Applies to:** If you didn’t select “Automatically notify testers” when you added your build to your group

## BUILD.17 Invite external testers — Remove a build from a group

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, under External Testing, select a group.
> - On the right, under Builds, hold the pointer over the build you want to remove.
> - Click the delete button.
> - In the dialog that appears, confirm you want to remove the build from the group and click Remove.
>
> If you want to remove a build from testing for all your testers, go to Stop testing a build.

**Applies to:** Apps tested with external testers

## BUILD.18 Invite external testers — FAQs

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers

**Source text (verbatim):**
> How do I appeal if my beta build was rejected?
>
> To appeal your beta build being rejected, contact TestFlight App Review.

**Applies to:** Beta builds rejected by TestFlight App Review

## BUILD.19 Provide export compliance information for beta builds

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-export-compliance-information-for-beta-builds

**Source text (verbatim):**
> Specify encryption use for your build to avoid the beta being marked as Missing Compliance. Answer the export compliance questions or attach previously approved documentation in the TestFlight section.
>
> Learn how to provide export compliance information for a build using the App Store Connect API.
>
> Required role: Account Holder, Admin, and App Manager. View role permissions.
>
> - In Apps, select the app you want to view.
> - Click the TestFlight tab.
> - In the sidebar, under Builds, click the platform.
> - In the Build column in the table on the right, click the app icon or build string for the build that’s missing compliance information.
>
> To address compliance issues for a build, you can either click Manage beside the relevant build to answer the required questions, or click Choose File to upload previously approved documentation.
>
> - Click Provide Export Compliance Information, and answer the required questions.
> - If app encryption documentation is required, click Go to App Encryption Page to upload your file. Apple will provide you with a key value to enter in Xcode This will remove the need to answer encryption questions with each app submission. Learn more about uploading app encryption documentation.
>
> If documentation isn’t required, click Save. You can indicate that your app doesn’t use encryption or is exempt from documentation by  specifying encryption settings in the app's Info.plist file in Xcode. This eliminates the need to answer encryption questions with each app submission.

**Applies to:** All builds distributed with TestFlight

- **[BUILD-20]** Has encryption use been specified for the build, so that it is not marked Missing Compliance?
  - quote: "Specify encryption use for your build to avoid the beta being marked as Missing Compliance."
  - surface: code
  - verify: Check the app target's Info.plist (or the build settings' generated Info.plist keys) for ITSAppUsesNonExemptEncryption. In App Store Connect > TestFlight > Builds, check that the build's status is not Missing Compliance.
  - fix: Answer the export compliance questions under Manage for the build, or set the encryption settings in Info.plist and upload a new build. If documentation is required, upload it on the App Encryption page and enter the key value that Apple provides in Xcode.
- **[BUILD-21]** If app encryption documentation is required, has it been uploaded on the App Encryption page?
  - quote: "If app encryption documentation is required, click Go to App Encryption Page to upload your file."
  - surface: asc
  - verify: TestFlight > Builds > [platform] > [build] > Provide Export Compliance Information: if the answers show documentation is required, click Go to App Encryption Page and check that the file has been uploaded.
  - fix: manual — requires developer decision/legal/business action

## BUILD.20 Testing subscriptions and In-App Purchases in TestFlight — Subscription renewal rate in TestFlight

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight

**Source text (verbatim):**
> When testing your app's subscriptions in TestFlight, the renewal rate is accelerated. Each subscription is renewed daily, up to 6 times within a 1-week period, regardless of the subscription's duration.
>
> Learn more about testing In-App Purchases with sandbox.
>
> Important: To test different renewal rates in TestFlight, you can use your Sandbox Apple Account. Learn more about managing Sandbox Apple Account settings.
>
> | Renewal for all durations | 1 week | 1 month | 2 months | 3 months | 6 months | 1 year |
> |---|---|---|---|---|---|---|
> | Subscription renewal speed | 1 Day | 1 Day | 1 Day | 1 Day | 1 Day | 1 Day |
>
> Example scenario: If you start a 1-month subscription on February 1st, it'll renew every 24 hours for a total of 6 renewals before being canceled. Since subscriptions renew at an accelerated rate in TestFlight, you'll see a new transaction for each renewal on February 2nd, 3rd, 4th, 5th, 6th, and 7th. The subscription's auto-renewal will then be disabled on February 8th.
>
> Note: To test subscriptions entering or exiting billing retry, you must test with a Sandbox Apple Account to subscribe and use the sandbox account settings to simulate this scenario. Learn more about testing failing subscription renewals and In-App Purchases.

**Applies to:** Apps with auto-renewable subscriptions tested in TestFlight

## BUILD.21 Testing subscriptions and In-App Purchases in TestFlight — Test In-App Purchase scenarios in TestFlight with your Sandbox Apple Account

**Source page:** https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight

**Source text (verbatim):**
> Apps downloaded from TestFlight will automatically operate in a sandbox environment. However, to test different In-App Purchase scenarios in TestFlight, you can use your Sandbox Apple Account. First, sign out of your production Apple Account under Media & Purchases. Then, go to Developer settings and sign in with your Sandbox Apple Account to access the sandbox controls for testing. For more details, please refer to the  Sign in to your Sandbox Apple Account for TestFlight section.
>
> To learn more about the different In-App Purchase scenarios you can test with your Sandbox Apple Account, visit the Manage Sandbox Apple Account settings page.
>
> Note:  You can only use a Sandbox Apple Account to test apps within your own developer account.

**Applies to:** Apps with In-App Purchases tested in TestFlight

## BUILD.22 Build upload statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-uploads/build-upload-statuses

**Source text (verbatim):**
> The build upload status provides detailed insights into delivery progress, including information, warnings and errors.
>
> | State | Description |
> |---|---|
> | Processing | Your build upload is still being processed. You'll receive an email notification and the table under Build Uploads will display an updated status when your build has finished processing.<br>If you upload a build and it remains in the Processing state for more than 24 hours, there may be an issue. To resolve the issue, submit a Feedback Assistant ticket or contact us. |
> | Failed | Your build upload has finished processing, but encountered an issue. Select the build to view potential errors, warnings, and information associated with the failure. Ensure to resolve all errors prior to re-uploading your build.<br>Note: If the build upload fails, you can reuse the same build number for your next upload. |
> | Complete | Your build upload has processed successfully and is now ready for testing.<br>Note: If there is a warning badge next to this status, review possible warnings or other information before your next upload. |

**Applies to:** All apps

- **[BUILD-22]** Is the upload status of the build you intend to test or submit Complete, not Processing or Failed?
  - quote: "Your build upload has processed successfully and is now ready for testing."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > TestFlight > Build Uploads table: check the State column for the build.
  - fix: Wait while the state is Processing. If it is Failed, fix the errors and upload again.
- **[BUILD-23]** If the upload Failed, have all reported errors been resolved before re-uploading?
  - quote: "Ensure to resolve all errors prior to re-uploading your build."
  - surface: asc
  - verify: Build Uploads table > select the Failed build: read the listed errors, warnings and information.
  - fix: Fix each listed error in the Xcode project, archive again, and re-upload. You can reuse the same build number.
- **[BUILD-24]** If the build has been in Processing for more than 24 hours, has the issue been reported?
  - quote: "If you upload a build and it remains in the Processing state for more than 24 hours, there may be an issue. To resolve the issue, submit a Feedback Assistant ticket or contact us."
  - surface: asc
  - verify: Build Uploads table: compare the time the Processing build was uploaded with the current time.
  - fix: Submit a Feedback Assistant ticket or contact Apple.
- **[BUILD-25]** If a Complete build shows a warning badge, have the warnings been reviewed before the next upload?
  - quote: "If there is a warning badge next to this status, review possible warnings or other information before your next upload."
  - surface: asc
  - verify: Build Uploads table: select any Complete build that shows a warning badge and read its warnings.
  - fix: Address the warnings in the Xcode project before the next upload.

## BUILD.23 App build statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-uploads/app-build-statuses

**Source text (verbatim):**
> The build status tells you immediately whether your build needs attention. The status applies to the build only, not the entire app.
>
> - A red status indicator () means that you need to perform some action or the build is expired.
> - A yellow status indicator () means that some process is ongoing, controlled either by you or by Apple.
> - A green status indicator () means the build is being tested in TestFlight.
>
> You can view the builds you upload and their file sizes, beta build status, and metrics under the TestFlight tab in App Store Connect.
>
> | Status | Description | Internal testing | External testing |
> |---|---|---|---|
> | Invalid Binary | Apple received your build, but it didn’t meet all the upload requirements. Resolve any issues in the build, and redeliver. Visit Upload builds. | Not visible in TestFlight | Not visible in TestFlight |
> | Missing Compliance | Your build is missing export compliance documentation. Action is needed. Learn how to provide export compliance for beta builds. | | |
> | Waiting for Export Compliance Review | Documentation for export compliance has been submitted and is in review. No action is needed on your end. | | |
> | In Compliance Review | Documentation for export compliance is in review. No action is needed on your end. | | |
> | Ready to Submit | Your build can be distributed to internal testers, or can be submitted to TestFlight App Review for external testing or to App Review for distribution to customers. | | |
> | Waiting for Review | Your build has been submitted to TestFlight App Review. It will need to be approved before you can begin external testing. | | |
> | In Beta Review | Your build is currently being reviewed by TestFlight App Review. It'll need to be approved before you can begin external testing. | | |
> | Not Available for Testing | Your build can't be used with TestFlight because the provisioning profile is missing an application identifier. To begin testing, upload a new build that includes the application identifier. | | |
> | Expired | Your build can't be used for testing with TestFlight because it has passed its 90-day availability window. | | |
> | Rejected | Your build was rejected by TestFlight App Review and can no longer be used in TestFlight. To begin testing, upload a new build. | Not visible in TestFlight | Not visible in TestFlight |
> | Ready to Test | Your build can be tested by external and internal testers, but you haven’t added any testers yet. You may have opted to manually notify testers after your build is approved. You can also submit your app to App Review for distribution to customers. | | |
> | Testing | Your build is being tested by at least one group or tester. Click on the build to view more details about who is testing your build. You can continue testing or submit your app to App Review for distribution to customers. Testers that have received an invite to test will still be able to test your build even after it's available for customers. | | |

**Applies to:** All builds uploaded to App Store Connect

- **[BUILD-26]** Is the build's status anything other than Invalid Binary?
  - quote: "Apple received your build, but it didn’t meet all the upload requirements. Resolve any issues in the build, and redeliver."
  - surface: asc
  - verify: App Store Connect > TestFlight > Builds > [platform]: check the build's status.
  - fix: Resolve the issues in the build and redeliver it.
- **[BUILD-27]** Is the build's status anything other than Missing Compliance?
  - quote: "Your build is missing export compliance documentation. Action is needed."
  - surface: asc
  - verify: TestFlight > Builds > [platform]: check the build's status.
  - fix: Click Manage beside the build to answer the export compliance questions, or click Choose File to upload previously approved documentation. To avoid this for future builds, specify the encryption settings in Info.plist.
- **[BUILD-28]** Is the build's status anything other than Not Available for Testing? That status means the provisioning profile is missing an application identifier.
  - quote: "Your build can't be used with TestFlight because the provisioning profile is missing an application identifier. To begin testing, upload a new build that includes the application identifier."
  - surface: code
  - verify: TestFlight > Builds: check the status. In the archive's embedded.mobileprovision, check for the `application-identifier` entitlement.
  - fix: Regenerate the distribution provisioning profile, re-archive, and upload a new build.
- **[BUILD-29]** Is the build you plan to test still inside its 90-day availability window (status not Expired)?
  - quote: "Your build can't be used for testing with TestFlight because it has passed its 90-day availability window."
  - surface: asc
  - verify: TestFlight > Builds > [platform]: check whether the build's status is Expired.
  - fix: Upload a new build with an incremented build string.
- **[BUILD-30]** If the build was Rejected by TestFlight App Review, has a new build been uploaded for testing?
  - quote: "Your build was rejected by TestFlight App Review and can no longer be used in TestFlight. To begin testing, upload a new build."
  - surface: asc
  - verify: TestFlight > Builds: check the status. Under General > App Review in the sidebar, read the rejection details.
  - fix: Address the rejection reasons, then upload and submit a new build.

## BUILD.24 App and submission statuses — App statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses

**Source text (verbatim):**
> The app status indicates where an app is in the review and release process.
>
> - A red status indicator () means that you need to perform an action before the app distributes.
> - A yellow status indicator () means that a process, controlled either by you or Apple, is still happening.
> - A green status indicator () means that the app is Ready for Distribution.
>
> If an app status indicates as editable below, you can edit app metadata when the app has this status.
>
> Receive automatic notifications to your web server whenever the status of your app changes by using webhooks. Learn how to manage webhooks.
>
> | Status | Description | Editable |
> |---|---|---|
> | Prepare for Submission | You’ve created an app record in App Store Connect but are still preparing information for it. | |
> | Ready for Review | You’ve entered all of the required metadata for your app and indicated that you intend to submit it for review, but haven’t submitted it yet.<br>You can submit the app by itself or include other items, such as In-App Events or custom product pages.<br>Note: Images and videos aren't editable in this state. | |
> | Invalid Binary | You’ve submitted your app to App Review, but the build does not meet the current binary requirements. You must upload a new build, or select one that meets all the current build requirements. | |
> | Waiting for Review | You’ve submitted a new app or updated version. Apple received your submission, but hasn’t started the review.<br>While you're waiting for the review, you can:<br>- Edit certain app information.<br>- Remove the build from review.<br>However, you can't upload or edit screenshots or app previews. | |
> | In Review | App Review is reviewing your app. You can remove the build from review. | |
> | Accepted | This item has been accepted, but one or more items in your submission were rejected.<br>The app can only publish when all items in the submission are accepted. You can edit the rejected items and resubmit, or remove them from the submission to move forward with the currently accepted items. | |
> | Waiting for Export Compliance | Your CCATS file is in Apple’s export compliance review process. | |
> | Pending Developer Release | Your app was accepted, but you still need to release it for distribution on the App Store. | |
> | Processing for Distribution | Your app is processing and will be ready for distribution within 24 hours. | |
> | Pending Apple Release | Apple is holding your app version until the corresponding Apple operating system version releases to the public.<br>If you think an app should be released on the existing operating system versions, review the deployment target set in your app build. If you rebuild your app with a different deployment target, reject the build for this version and submit the new version. | |
> | Pending App Transfer | The app transferor has initiated the app transfer, but the recipient hasn't yet accepted. The transferor and the recipient can each cancel the transfer. No changes can be made to the app except changes to pricing. | |
> | Processing App Transfer | The recipient accepts the app transfer. You can't cancel or make changes to the app until the transfer is complete. | |
> | Ready for Distribution | Your app has been accepted and is ready for distribution.<br>To distribute your app, your agreements must be in effect. The Account Holder can accept the latest agreements in the Business section. | |
> | Rejected | Your app wasn't accepted. App Review notifies App Store Connect users with the Admin, App manager, or Developer role with the issues. Learn how to reply to App Review messages. | |
> | Metadata Rejected | App Review didn’t accept your metadata. Read the message from App Review, edit the metadata to resolve the issue, and reply to the message from App Review. | |
> | Developer Rejected | You removed your app from review. When you’re ready, resubmit your build or submit a new build. | |

**Applies to:** All apps

- **[BUILD-31]** Does the build selected for the version meet all current binary requirements (app status not Invalid Binary)?
  - quote: "You must upload a new build, or select one that meets all the current build requirements."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > [platform version]: check the app status and the Build section.
  - fix: Upload a new build, or select a different build that meets the current build requirements.
- **[BUILD-32]** Are the agreements needed to distribute the app in effect?
  - quote: "To distribute your app, your agreements must be in effect. The Account Holder can accept the latest agreements in the Business section."
  - surface: asc
  - verify: App Store Connect > Business: check that every required agreement shows as active and that no new terms are waiting to be accepted.
  - fix: manual — requires developer decision/legal/business action
- **[BUILD-33]** Is the build's deployment target right for release on the operating system versions already available to the public? A version that targets an unreleased OS is held as Pending Apple Release.
  - quote: "If you think an app should be released on the existing operating system versions, review the deployment target set in your app build."
  - surface: code
  - verify: Xcode > target > General > Minimum Deployments (IPHONEOS_DEPLOYMENT_TARGET / MACOSX_DEPLOYMENT_TARGET etc.): compare with the OS versions currently released to the public, and check the SDK used to build.
  - fix: Rebuild with the intended deployment target, reject the build for this version, and submit the new version.
- **[BUILD-34]** If the status is Metadata Rejected, has the metadata been edited to resolve the issue and a reply sent to App Review?
  - quote: "Read the message from App Review, edit the metadata to resolve the issue, and reply to the message from App Review."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Review: read the message, then check the edited metadata fields.
  - fix: Edit the metadata named in the message and reply to App Review.
- **[BUILD-35]** If any item in the submission was rejected, has it been fixed and resubmitted, or removed? The app can only publish when every item in the submission is accepted.
  - quote: "The app can only publish when all items in the submission are accepted."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Review: check each item's status in the submission.
  - fix: Edit and resubmit the rejected items, or remove them from the submission.

## BUILD.25 App and submission statuses — Submission statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses

**Source text (verbatim):**
> These statuses are shown for submissions to App Review. Once all items within the submission are accepted, the submission moves from the In Progress section to the Completed section on the App Review page.
>
> | Status | Description |
> |---|---|
> | Waiting for Review | Apple received your submission, but hasn’t started review.<br>While waiting for review, you can:<br>- Edit certain information<br>- Remove items from review<br>However, you can't:<br>- Upload or edit screenshots or app previews<br>- Edit In-App Event metadata |
> | In Review | App Review is reviewing your submission. You can cancel the submission to remove it from review. |
> | Processing | You removed your submission from review and your action is being processed. When it's done processing the submission moves to Completed in the App Review section. |
> | Unresolved Issues | App Review rejected one or more items in the submission. Learn how to manage a submission with unresolved issues. |
> | Rejected | App Review rejected your app bundle or TestFlight submission. For TestFlight, you must submit a new build for review before you can invite external testers. |

**Applies to:** Submissions to App Review

- **[BUILD-36]** Are screenshots and app previews final before the submission enters Waiting for Review? After that, they can't be uploaded or edited.
  - quote: "Upload or edit screenshots or app previews"
  - surface: asc
  - verify: App Store Connect > Apps > [app] > [platform version] > Previews and Screenshots: check every localization before you submit.
  - fix: Finish the screenshots and previews before submitting. If they need to change after submission, remove the items from review first.
- **[BUILD-37]** If a TestFlight submission was Rejected, has a new build been submitted for review before you invite external testers?
  - quote: "For TestFlight, you must submit a new build for review before you can invite external testers."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Review: check the status of the TestFlight submission. In TestFlight > Builds, check whether a newer build has been submitted.
  - fix: Address the rejection, upload a new build, and submit it for TestFlight App Review.

## BUILD.26 App and submission statuses — Item statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses

**Source text (verbatim):**
> These statuses are shown for items within a submission to App Review. You can locate the status of each item on the item’s page (for example, the app record or In-App Event’s page), or when you click View or Resolve next to the submission. Once all items within the submission are accepted, the submission moves from the In Progress section to the Completed section on the App Review page.
>
> | Status | Description |
> |---|---|
> | Ready for Review | The item has been added to a submission, but it hasn’t been submitted to App Review yet. |
> | Waiting for Review | Apple received your submission, but hasn’t started review.<br>While waiting for review, you can:<br>- Edit certain information<br>- Remove items from review<br>However, you can't:<br>- Upload or edit screenshots or app previews<br>- Edit In-App Event metadata |
> | In Review | App Review is reviewing your submission. You can cancel the submission to remove it from review. |
> | Accepted | This item has been accepted, but there are one or more rejected items in the submission. All items in the submission must be accepted before any can be published.<br>You can edit the rejected items and resubmit, or you can remove them from the submission.<br>Learn how to reply to App Review messages. |
> | Rejected | App Review didn’t accept your item. You can edit the item and resubmit, or you can remove the item from the submission.<br>Learn how to manage a submission with unresolved issues. |

**Applies to:** Items within a submission to App Review

- **[BUILD-38]** If the submission includes In-App Events, is their metadata final before the submission enters Waiting for Review?
  - quote: "Edit In-App Event metadata"
  - surface: asc
  - verify: App Store Connect > Apps > [app] > In-App Events: check each event in the submission before you submit.
  - fix: Finish the In-App Event metadata before submitting. If it needs to change, remove the item from review first.

## BUILD.27 App and submission statuses — App Store availability statuses

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses

**Source text (verbatim):**
> The App Store status tells you whether your app is available in a specific country or region, or if there are any reasons your app isn’t appearing somewhere.
>
> - A red status indicator () means your app isn’t available in the country or region.
> - A yellow status indicator () means your app needs action from you before the app is available in the country or region, or the app is currently processing.
> - A green status indicator () means your app is available in the country or region.
>
> | Status | Description |
> |---|---|
> | Available | Your app is live on the App Store for users in this country or region. |
> | Available on App Release | Your app is ready to be released in this country or region after your scheduled release date or after you manually release the app. This status only appears if your app has never released in any regions. Learn how to select an App Store version release option. |
> | Pre-Order Pending Developer Release | You've set up a pre-order that publishes in this country or region after you release a version of your app. Learn more. |
> | Pre-Order (Scheduled Release [date]) | The pre-order is live and your app will be releases for download or purchase in this country or region on the date indicated. Customers in this country or region can pre-order your app on the store. |
> | Processing to Available | Your app is processing and should be available in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us. |
> | Processing to Not Available | Your app is processing and should no longer be available in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us. |
> | Processing to Pre-Order | Your app is processing and should publish for pre-order in this country or region within 24 hours. If your app is in this status for more than 24 hours, contact us. |
> | Not Available | Your app isn't available in this country or region because you've indicated that you don't intend to distribute in this location. Learn how to select the regions where you want to make your app available. |
> | Missing App Rating | Your app isn't available in this country or region because you haven't set an age rating for your app. Learn how to set an app age rating. |
> | Missing Tax Form | Your app isn't available in Brazil because you haven't submitted Brazilian tax information. Learn more. |
> | Missing Game registration number | Your app isn't available in China mainland because you haven't provided an approval number and supporting documents from China's National Press and Publication Administration. Learn more. |
> | ICP Filing Number Missing | Your app isn't available in China mainland because you haven't provided a valid Internet Content Provider (ICP) Filing Number. Learn more. |
> | ICP Filing Number Invalid | Your app isn't available in China mainland because the Internet Content Provider (ICP) Filing Number or metadata you provided doesn't match the information you have filed with China’s Ministry of Industry and Information Technology (MIIT), or both. Learn more. |
> | Cannot Sell App | Your app isn't available in this country or region. Hold the pointer over the status to locate the reason why. If you have any questions, contact us. |

**Applies to:** All apps; the Brazil and China mainland statuses apply where the app is distributed in those locations

- **[BUILD-39]** Has an age rating been set for the app?
  - quote: "Your app isn't available in this country or region because you haven't set an age rating for your app."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Information > Age Rating: check that the questionnaire is complete. Under Pricing and Availability, check that no region shows Missing App Rating.
  - fix: Complete the age rating questionnaire in App Information.
- **[BUILD-40]** If the app is distributed in Brazil, has Brazilian tax information been submitted?
  - quote: "Your app isn't available in Brazil because you haven't submitted Brazilian tax information."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability: check the Brazil row for the Missing Tax Form status.
  - fix: manual — requires developer decision/legal/business action
- **[BUILD-41]** If the app is a game distributed in China mainland, have the approval number and supporting documents from China's National Press and Publication Administration been provided?
  - quote: "Your app isn't available in China mainland because you haven't provided an approval number and supporting documents from China's National Press and Publication Administration."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability: check the China mainland row for the Missing Game registration number status.
  - fix: manual — requires developer decision/legal/business action
- **[BUILD-42]** If the app is distributed in China mainland, has a valid ICP Filing Number been provided that matches the information filed with MIIT?
  - quote: "Your app isn't available in China mainland because you haven't provided a valid Internet Content Provider (ICP) Filing Number."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability: check the China mainland row for ICP Filing Number Missing or ICP Filing Number Invalid.
  - fix: manual — requires developer decision/legal/business action
- **[BUILD-43]** Is the app's status free of Cannot Sell App in every region where you intend to distribute it?
  - quote: "Your app isn't available in this country or region. Hold the pointer over the status to locate the reason why."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability: check the status of each region you distribute in, and hold the pointer over any Cannot Sell App status to see the reason.
  - fix: manual — requires developer decision/legal/business action

## BUILD.28 Overview of maintaining an app

**Source page:** https://developer.apple.com/help/app-store-connect/update-your-app/overview-of-maintaining-an-app

**Source text (verbatim):**
> After you publish your app, you perform a number of tasks to respond to customer feedback and to maintain your app throughout its lifetime. You can perform these tasks in any order.
>
> Create a new version
>
> When you’re ready to distribute a new build of your app, you create a new version using the same app record as your previous version. You can update the metadata for the new app version and add a description of the new features.
>
> Download catalog reports
>
> If you have several apps in your account, generate catalog reports that detail the information and settings for all your organization’s apps, including In-App Purchase, and metadata for Game Center leaderboards and achievements.
>
> Monitor App Store customer reviews, sales, and analytics
>
> You can read and respond to reviews. To better understand how your app is doing, you can view sales and trends and view app analytics, such as crashes, sessions, and active users.
>
> Change App Store pricing and availability
>
> You can change the price, schedule price changes, and change the countries or regions for your app on the App Store at any time. Scheduling price changes is useful for promotions that have start and end dates.
>
> Remove an app
>
> If you no longer want your app to be available to customers, you can remove it from the App Store, which removes all versions of the app.

**Applies to:** Apps already published on the App Store

## BUILD.29 Create a new version

**Source page:** https://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version

**Source text (verbatim):**
> When you’re ready to distribute a new version of your app, you create a version using the same app record you created for the original version.
>
> Keep in mind that it's not possible to revert to a previous version on the App Store if you have an issue with your app. You must create and submit a new version. Ensure that the current version status is Ready for Distribution to initiate a new version.
>
> Learn about creating a new version using App Store Connect API.
>
> Required role: Account Holder, Admin, App Manager, or Marketing. View role permissions.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click the add button (+) next to the desired platform.
> - In the New Version dialog, enter an incremental App Store version number, then click Create.
> - Review and enter metadata about the new version.
>
> When you create a new version, the metadata from the current version is automatically transferred to the new version.
>
> For a description of the version properties, visit Platform version information. For the required and localizable properties, refer to Required, localizable, and editable properties.
>
> - On the top right, click Save.
> - Upload your new build to App Store Connect.
>
> In Xcode, increment the build string before you upload your build to App Store Connect, as described in Set the version number and build string.
>
> - When you're ready to submit your build, add it to your latest version, then submit your app to App Review.

**Applies to:** Updates to an app that already has a version on the App Store

- **[BUILD-44]** Is the current version's status Ready for Distribution before the new version is created?
  - quote: "Ensure that the current version status is Ready for Distribution to initiate a new version."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > sidebar: check the status of the current platform version.
  - fix: Wait until the current version reaches Ready for Distribution, or release it, before creating the new version.
- **[BUILD-45]** Is the new App Store version number an increment over the current version?
  - quote: "In the New Version dialog, enter an incremental App Store version number, then click Create."
  - surface: code
  - verify: Compare the new version in App Store Connect with the live version. In Xcode > target > General, check that Version (CFBundleShortVersionString / MARKETING_VERSION) matches the new version and is higher than the live one.
  - fix: Set MARKETING_VERSION in Xcode to a higher version number and use the same number for the App Store Connect version.
- **[BUILD-46]** Was the build string incremented in Xcode before the new build was uploaded?
  - quote: "In Xcode, increment the build string before you upload your build to App Store Connect"
  - surface: code
  - verify: Xcode > target > General > Build (CFBundleVersion / CURRENT_PROJECT_VERSION): check that it is higher than the build strings already uploaded for this version in TestFlight > Builds.
  - fix: Increment CURRENT_PROJECT_VERSION, archive, and upload again.
- **[BUILD-47]** Has the metadata carried over from the current version been reviewed and updated for the new version?
  - quote: "When you create a new version, the metadata from the current version is automatically transferred to the new version."
  - surface: asc
  - verify: App Store Connect > [new platform version]: review the description, screenshots, promotional text, keywords, and What's New for every localization.
  - fix: Update any carried-over metadata that no longer matches the new version, then click Save.
- **[BUILD-48]** Has the new build been added to the latest version before you submit to App Review?
  - quote: "When you're ready to submit your build, add it to your latest version, then submit your app to App Review."
  - surface: asc
  - verify: App Store Connect > [new platform version] > Build section: check that the intended build is selected.
  - fix: Click Add Build, select the new build, and save.

## BUILD.30 Platform version information — What’s New, Version Release Settings and Phased Release properties

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information

**Source text (verbatim):**
> | Property | Description |
> |---|---|
> | Version Release Settings | Determines how the app version will be released. The following settings are allowed:<br>- Manual. When the app status changes to Pending Developer Release after approval and you must manually release the version.<br>- Automatic. The app goes live automatically after it is approved by App Review.<br>- Automatic, no earlier than. If the date hasn't passed when the app is approved, the app status changes to Pending Developer Release, but is automatically released at the date specified. |
> | What’s New in this Version | A description of the changes in this version of the app, such as new features, UI improvements, or bug fixes. Limited to 4000 characters.<br>We recommend that you provide detailed information to let users know the specifics of the changes, improvements, or fixes in the version.<br>This property isn't available for the first version of the app but required for all subsequent versions. This property can be localized. |
> | Phased Release for Automatic Updates | When you release a version update of your app, you can choose to release your iOS app in stages. If you choose this option, your version update will be released over a 7-day period to a percentage of your users on iOS with automatic updates turned on. Learn how to release a version update in phases. |

**Applies to:** App versions after the first version (What’s New); all app versions (Version Release Settings)

- **[BUILD-49]** For an update (not the first version), is What’s New in this Version filled in for every localization, within 4000 characters?
  - quote: "This property isn't available for the first version of the app but required for all subsequent versions."
  - surface: asc
  - verify: App Store Connect > [new platform version] > What’s New in This Version: check every localization for non-empty text of 4000 characters or fewer.
  - fix: Write What’s New text describing the changes in this version for each localization.

## BUILD.31 Platform version information — App Review information

**Source page:** https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information

**Source text (verbatim):**
> You must provide the following information to App Review. It isn’t visible to customers and can be edited at any time.
>
> Submissions that include an app version will be reviewed together with the App Review information for that version.
>
> Submissions that don’t include an app version, or those that include items associated with multiple platforms, will be reviewed together with the App Review information for the latest approved version of the platform you specify during the submission process. To edit the App Review information on an approved app version, click Edit in the top right corner of the App Review Information section.
>
> | Property | Description | Required |
> |---|---|---|
> | Contact:<br>Name, email, phone number | Information for the contact person in your organization if the App Review team needs additional information.<br>Enter the phone number in international format, including a plus sign (+) followed by the country code (for example, +852 for Hong Kong) — the field doesn't accept numbers-only entry. | |
> | Notes | Additional information about your app that can help during the review process. Include information that may be needed to test your app, such as app-specific settings and test registration or account details. If your app delivers streaming video over the cellular network, enter a test stream URL. The Notes field can contain up to 4000 bytes. You can write notes in any language. | |
> | Sign-in required:<br>Username and password | Sign-in information for a demo account. If your app uses a single sign-on service, such as Facebook or Twitter, include the demo account login information for it. The demo account is used during the App Review process and must not expire. Details for additional accounts should be included in the Notes field. | If your app requires a login to use it. |

**Applies to:** All submissions to App Review (this page is the target of the "TestFlight App Review information properties" link on Provide test information); sign-in applies "If your app requires a login to use it."

- **[BUILD-50]** Is App Review contact information (name, email, phone number) entered, with the phone number in international format starting with + and the country code?
  - quote: "Enter the phone number in international format, including a plus sign (+) followed by the country code"
  - surface: asc
  - verify: App Store Connect > [platform version] > App Review Information > Contact Information (and TestFlight > Test Information for beta review): check the name, email and phone fields.
  - fix: Enter the contact name and email, and the phone number as +<country code><number>.
- **[BUILD-51]** If the app requires a login, are a demo account username and password provided, and will the account not expire?
  - quote: "The demo account is used during the App Review process and must not expire."
  - surface: asc
  - verify: App Store Connect > [platform version] > App Review Information > Sign-in required: check that the username and password are filled in. Then sign in with the credentials in a fresh install of the build.
  - fix: Create a non-expiring demo account, enter its username and password, and put details for any additional accounts in Notes.
- **[BUILD-52]** If the app uses a single sign-on service, is demo account login information for that service included?
  - quote: "If your app uses a single sign-on service, such as Facebook or Twitter, include the demo account login information for it."
  - surface: asc
  - verify: App Review Information > Sign-In Information and Notes: check for credentials for each single sign-on provider the app requires.
  - fix: Add demo login information for the single sign-on service in Sign-In Information or Notes.
- **[BUILD-53]** If the app delivers streaming video over the cellular network, is a test stream URL entered in Notes, and are the Notes within 4000 bytes?
  - quote: "If your app delivers streaming video over the cellular network, enter a test stream URL."
  - surface: asc
  - verify: App Review Information > Notes: check for a test stream URL, and check that the field is no larger than 4000 bytes.
  - fix: Add a working test stream URL to Notes, shortening other text if needed.

## BUILD.32 Select an App Store version release option

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-an-app-store-version-release-option

**Source text (verbatim):**
> You can choose a release option for each platform version of your app in App Store Connect.
>
> Note: If you’re setting up your app for pre-order in a country or region and haven't yet released it on the App Store, you'll need to release the app version manually. The App Store Version Release section will be dimmed and "Release the app yourself" will be automatically selected.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click the app version you want to set a release option for.
> - In the App Store Version Release section, select a release option:
> - Release the app yourself: Select “Manually release this version.” (Later, manually release the version.)
> - Automatically release the app after approval: Select “Automatically release this version.”
> - Automatically release the app but no earlier than a specified date: Select “Automatically release this version after App Review, no earlier than” and below this option, enter a date and time.
> - On the top right of the page, click Save.

**Applies to:** All app versions; manual release is required when setting up pre-order for an app not yet released on the App Store

- **[BUILD-54]** Has the App Store Version Release option for each platform version been set to the release behavior you intend?
  - quote: "You can choose a release option for each platform version of your app in App Store Connect."
  - surface: asc
  - verify: App Store Connect > [platform version] > App Store Version Release: check which option is selected (manual, automatic, or automatic no earlier than a date and time) and any date entered.
  - fix: manual — requires developer decision/legal/business action
- **[BUILD-55]** If the app is set up for pre-order and has never been released, is the plan to release the version manually?
  - quote: "If you’re setting up your app for pre-order in a country or region and haven't yet released it on the App Store, you'll need to release the app version manually."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability (pre-order) and [platform version] > App Store Version Release: check that "Release the app yourself" is selected (the section is dimmed).
  - fix: Plan to click Release This Version after approval. The pre-order then publishes where it is enabled.

## BUILD.33 Select an App Store version release option — Manually release a version to the App Store

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-an-app-store-version-release-option

**Source text (verbatim):**
> When submitting your app for review, you can manually release a version. After approval, release it to the App Store once its status changes to Pending Developer Release.
>
> Releasing an app version is specific to the platform you're working with. If there are app versions for other platforms also in "Pending Developer Release" that you want to release, you must manually release each one for every platform.
>
> Apple will send you an email reminder if an app remains in Pending Developer Release status for more than 30 days.
>
> Learn how to manually release a version with the App Store Connect API.
>
> - In Apps, select the app you want to view.
> - In the sidebar, select the app version that has the status of Pending Developer Release.
> - On the top right, click Release This Version.
> - In the dialog that appears, click Confirm.
>
> After manually releasing your app version, it may take up to 24 hours for it to appear on the App Store. To cancel the release, select Cancel This Release from the message on the version page.
>
> Note: When you choose Release This Version, the new app will publish for pre-order in countries or regions where pre-order is enabled. It’ll also be available for download or purchase in any country or region where the App Store status is Available or Available on App Release. Learn more.

**Applies to:** App versions set to manual release

- **[BUILD-56]** If several platform versions are in Pending Developer Release, has each platform been released manually?
  - quote: "you must manually release each one for every platform."
  - surface: asc
  - verify: App Store Connect > Apps > [app] sidebar: check every platform version for the Pending Developer Release status.
  - fix: For each platform version you want to release, select it and click Release This Version > Confirm.

## BUILD.34 Release a version update in phases

**Source page:** https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases

**Source text (verbatim):**
> When you release a version update of your app, you can choose to release the new version to the App Store in stages. This option is available when you submit a version update and your app has one of the following statuses:
>
> - Prepare for Submission
> - Waiting for Review
> - In Review
> - Waiting for Export Compliance
> - Pending Developer Release
> - Developer Rejected
> - Rejected
> - Metadata Rejected
>
> Selecting this option will release your app's update gradually over 7 days. A random sample of users with automatic updates on eligible devices will receive the update, without any notification of their participation in the phased release.
>
> | Day of Phased Release | Percentage of Users |
> |---|---|
> | 1 | 1% |
> | 2 | 2% |
> | 3 | 5% |
> | 4 | 10% |
> | 5 | 20% |
> | 6 | 50% |
> | 7 | 100% |
>
> Keep in mind that apps and app updates in phased release can be manually downloaded from the App Store by anyone at any time.
>
> During phased release, you may pause the release for up to 30 days, with no limit on the number of pauses. If you remove your app from sale — including when your Apple Developer Program membership lapses — phased release will stop and won't be available for that version again. When your app is reinstated, it becomes available to all users immediately, regardless of the percentage reached before removal. To resume a controlled rollout, make the version unavailable for download and submit a new version update with phased release enabled.
>
> Learn how to manage phased releases using the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** Version updates of iOS, macOS and tvOS apps

- **[BUILD-57]** If you want a staged rollout, has phased release been chosen while the version update is still in one of the eligible statuses (Prepare for Submission through Metadata Rejected)?
  - quote: "This option is available when you submit a version update and your app has one of the following statuses:"
  - surface: asc
  - verify: App Store Connect > [platform version] > Phased Release for Automatic Updates: check whether "Release update over a 7-day period using phased release" is selected, and check the current status of the version.
  - fix: manual — requires developer decision/legal/business action
- **[BUILD-58]** If you use phased release, are you prepared for anyone to download the update manually during the rollout?
  - quote: "Keep in mind that apps and app updates in phased release can be manually downloaded from the App Store by anyone at any time."
  - surface: manual
  - verify: Confirm that the release plan (for example, a server-side migration or feature flags) does not assume only the phased percentage of users has the update.
  - fix: manual — requires developer decision/legal/business action

## BUILD.35 Release a version update in phases — Release a version update in phases (steps)

**Source page:** https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click the app version you want to submit.
> - On the right, scroll down to the Phased Release for Automatic Updates section, select Release update over a 7-day period using phased release.
> - Click save.
>
> When you submit your app for review and it's approved, the app status will be Ready for Distribution, and will be appended with “Phased Release” next to the status when viewing your app's version page.
>
> When the update is complete, all users with Admin or App Manager roles who have access to this app will receive a notification regarding the completion of the phased release.

**Applies to:** Version updates of iOS, macOS and tvOS apps using phased release

## BUILD.36 Release a version update in phases — Pause and resume a phased release

**Source page:** https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click the Ready for Distribution app version.
> - In the Phased Release for Automatic Updates section, you can either pause the release by selecting Pause Phased Release or resume it by using the Use Phased Release option.
> - Click Save.
>
> You can pause your release for a total of 30 days. For example, if you pause the release for 10 days and then choose to resume it, you will have 20 days remaining to pause the release again. If you resume a release that was previously paused, your phased release will pick up on the day it was left off when it was paused.

**Applies to:** Version updates in phased release

## BUILD.37 Release a version update in phases — Release a version update to all users

**Source page:** https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases

**Source text (verbatim):**
> If you decide to release your app in phases, you can release it to all users at any time once it has the Ready for Distribution status. When you select this option, all users whose devices have automatic updates turned on gets the latest app version supported on the user’s device.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click the app version that you've submitted.
> - On the top right of the page, click Release to All Users.

**Applies to:** Version updates in phased release with Ready for Distribution status

## Sources

- https://developer.apple.com/help/app-store-connect/
- https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview
- https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-test-information
- https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers
- https://developer.apple.com/help/app-store-connect/test-a-beta-version/provide-export-compliance-information-for-beta-builds
- https://developer.apple.com/help/app-store-connect/test-a-beta-version/testing-subscriptions-and-in-app-purchases-in-testflight
- https://developer.apple.com/help/app-store-connect/reference/app-uploads/build-upload-statuses
- https://developer.apple.com/help/app-store-connect/reference/app-uploads/app-build-statuses
- https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses
- https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information (reached via https://developer.apple.com/help/app-store-connect/reference/app-review-information)
- https://developer.apple.com/help/app-store-connect/update-your-app/overview-of-maintaining-an-app
- https://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version
- https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/select-an-app-store-version-release-option
- https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases
