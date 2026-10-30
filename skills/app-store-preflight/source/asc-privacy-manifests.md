=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk
# Adding a privacy manifest to your app or third-party SDK

Report the data you collect and the required reasons API you use in your app or third-party SDK.

### Overview

A privacy manifest is a property list file (PrivacyInfo.xcprivacy) that you add to your target’s resources. The privacy manifest describes the privacy practices of an app or third-party SDK. To add a privacy manifest to your app or third-party SDK using Xcode, see Privacy manifest files. All privacy manifest files in your app must be valid, containing only the expected keys and values. For more information, see “Describe the data your app or third-party SDK collects,” in Describing data use in privacy manifests.

[Important]

Important: App Store Connect rejects app submissions that include invalid privacy manifest files. If you upload an app to App Store Connect that contains privacy manifest files with unexpected keys or values, you receive an email that includes the name and path of the invalid files in your app bundle. If an invalid file comes from a third-party SDK, contact its developer for an updated version of the SDK that includes a valid privacy manifest. To troubleshoot invalid privacy manifests, see TN3181: Debugging an invalid privacy manifest. Starting February 12, 2025, apps you submit for review in App Store Connect must contain a valid privacy manifest file for a certain number of commonly used third-party SDKs. For more information, see Upcoming third-party SDK requirements.

When you add a privacy manifest to the target that builds your app or third-party SDK in Xcode, Xcode automatically places this file in the correct location based on the type of product and its target platform. If you don’t use Xcode to build your product, use the information below to place the privacy manifest in the correct location. Even if you use Xcode, you might find this information useful to verify the privacy manifest location in your product.

#### Add a privacy manifest to your app

If you build an iOS, iPadOS, tvOS, visionOS, or watchOS app, place the privacy manifest at the root of your app’s bundle. The example below shows the bundle structure of an iOS app called Sample, which lists PrivacyInfo.xcprivacy at Sample.app/PrivacyInfo.xcprivacy:

Sample.app/
    Info.plist
    Sample
    PrivacyInfo.xcprivacy 
    ...

For macOS and Mac Catalyst apps, place the privacy manifest file in Contents/Resources/ in your app’s bundle. The following example shows the bundle structure of a macOS app called MacSample, which lists PrivacyInfo.xcprivacy at MacSample.app/Contents/Resources/PrivacyInfo.xcprivacy:

MacSample.app/
    Contents/
        Info.plist
        MacOS/
            MacSample
        Resources/
            PrivacyInfo.xcprivacy
        ...

#### Add a privacy manifest to your framework

The location where you place the privacy manifest in your framework depends on the platform. For iOS, iPadOS, tvOS, visionOS, or watchOS frameworks, place the privacy manifest at the root of your framework’s bundle. The example below shows the layout of an iOS framework called SampleFramework, which lists PrivacyInfo.xcprivacy at SampleFramework.framework/PrivacyInfo.xcprivacy:

SampleFramework.framework/
    Info.plist 
    SampleFramework
    PrivacyInfo.xcprivacy 
    ...

For macOS and Mac Catalyst frameworks, place the privacy manifest file in Versions/A/Resources/ in your framework’s bundle. The following example shows the layout of a macOS framework named MacSampleFramework that supports a single version (A)and includes a privacy manifest file. Its bundle structure lists PrivacyInfo.xcprivacy at MacSampleFramework.framework/Versions/A/Resources/PrivacyInfo.xcprivacy:

MacSampleFramework.framework/
    MacSampleFramework -> Versions/Current/MacSampleFramework
    Resources -> Versions/Current/Resources
    Versions/
        Current -> A
        A/
            MacSampleFramework
            Resources/
                Info.plist 
                PrivacyInfo.xcprivacy
            ...
    ...

#### Add a privacy manifest to your Swift package

A Swift package’s resources can include its privacy manifest file. For more information about adding resource files to Swift packages, see Bundling resources with a Swift package. Source files reside in a subfolder of a package’s Sources directory that has the same name as the target they belong to. This is the default location for resources. If your resource files reside in the default location, add the privacy manifest to it. The following example shows a package manifest that declares the SomeLibrary target. Place your privacy manifest file in Sources/SomeLibrary if you don’t specify an alternative location, as shown below:

SamplePackage/
    README.md
    Package.swift
    Sources/
        SomeLibrary/
            SomeLibrary.swift
            Product.swift
            PrivacyInfo.xcprivacy
            ...
    Tests/
        ...

Alternatively, if your resource files reside in a subfolder separate from your source files, add the privacy manifest to this directory. Place your privacy manifest file in Sources/SomeLibrary/Resources if you put all your resource files into a directory named Resources:

SamplePackage/
    README.md
    Package.swift
    Sources/
        SomeLibrary/
            SomeLibrary.swift
            Product.swift
            ...
            Resources/
                PrivacyInfo.xcprivacy
                ...
    Tests/
        ...

Xcode doesn’t recognize privacy manifest files as resources by default. After adding the manifest file to your package, explicitly declare the file or the directory that includes it as a package resource. In the following example, the package manifest declares PrivacyInfo.xcprivacy as an explicit resource:

targets: [
    .target(
        name: "SomeLibrary",
        resources: [
            .process("PrivacyInfo.xcprivacy")]
    ),
]

In this example, the package manifest lists the Resources directory as an explicit resource:

targets: [
    .target(
        name: "SomeLibrary",
        resources: [
            .process("Resources")]
    ),
]

If you distribute your binary framework as a Swift package, check that your XCFramework bundle includes a privacy manifest for each platform that you support. For more information, see Distributing binary frameworks as Swift packages.

#### Distribute your static library with a privacy manifest

A static library is an archive of object files with a .a file extension. It doesn’t support resources such as the privacy manifest. If you currently distribute your SDK as a static library and want to update it to include a privacy manifest in Xcode, create a new static framework target that includes all your static library’s source files and resources, then add the privacy manifest to the target’s resource. For more information on how to create a static framework, see Creating a static framework.

If you don’t use Xcode to build your static library, create a static framework bundle for your static library manually, then add the privacy manifest to the bundle as a resource. For more information about framework bundle structure, see Placing content in a bundle. To identify the privacy manifest location in the static framework, see Add a privacy manifest to your framework.

#### Verify your XCFramework bundle includes the necessary privacy manifests

An XCFramework bundle is a binary package that can include multiple platform-specific variants of a framework or library. It supports distribution of Swift and C-based code. For more information about creating an XCFramework bundle, see Creating a multiplatform binary framework bundle.

After adding a privacy manifest to your framework, consider distributing it as a signed XCFramework bundle. When you generate an XCFramework bundle with your framework, the generated bundle contains a privacy manifest file for each platform that your framework supports. The framework platform determines the location of the manifest file. When you sign your XCFramework bundle, developers who incorporate the framework can see whether updates to the framework have compatible code signatures. For more information, see Verifying the origin of your XCFrameworks.

After an update, SampleFramework supports iOS, iOS Simulator, Mac Catalyst, and macOS. The MyArchives directory contains archives of each variant of SampleFramework. Running the following command in Terminal creates an XCFramework with variants for iOS, iOS Simulator, Mac Catalyst, and macOS:

xcodebuild -create-xcframework 
-archive MyArchives/SampleFramework-iOS.xcarchive -framework SampleFramework.framework
-archive MyArchives/SampleFramework-macOS.xcarchive -framework SampleFramework.framework
-archive MyArchives/SampleFramework-iOS_Simulator.xcarchive -framework SampleFramework.framework 
-archive MyArchives/SampleFramework-Mac_Catalyst.xcarchive -framework SampleFramework.framework 
-output xcframeworks/SampleFramework.xcframework

Each variant of SampleFramework contains a privacy manifest file at the appropriate location, as shown below:

SampleFramework.xcframework/
    Info.plist
    ios-arm64/
       dSYMs/
           ...
       SampleFramework.framework/
           Info.plist
           SampleFramework
           PrivacyInfo.xcprivacy 
           ...
    macos-arm64_x86_64/
        dSYMs/
            ...
        SampleFramework.framework/
            SampleFramework -> Versions/Current/SampleFramework
            Resources -> Versions/Current/Resources
            Versions/
                Current -> A
                A/
                    SampleFramework
                    Resources/
                        Info.plist
                        PrivacyInfo.xcprivacy
                    ...
            ...
    ios-arm64_x86_64-simulator/
        dSYMs/
            ...
        SampleFramework.framework/
            Info.plist
            SampleFramework
            PrivacyInfo.xcprivacy 
            ...
    ios-arm64_x86_64-maccatalyst/
        dSYMs/
           ...
        SampleFramework.framework/
            SampleFramework -> Versions/Current/SampleFramework
            Resources -> Versions/Current/Resources
            Versions/
                Current -> A
                A/
                    SampleFramework
                    Resources/
                        Info.plist 
                        PrivacyInfo.xcprivacy
                    ...
            ...

To identify the privacy manifest location in frameworks, see Add a privacy manifest to your framework. To ship your static library with a privacy manifest, see Distribute your static library with a privacy manifest.

#### Locate an invalid privacy manifest in your app archive

To find an invalid privacy manifest in your app archive:

1. Gather the location of the file from the email you received from Apple.

2. In Xcode, choose Window > Organizer, then click Archives.

3. Control-click your app archive in the organizer, and choose Show in Finder from the contextual menu. Xcode opens the Finder to the location of your archive.

4. In the Finder, control-click your archive, and choose Show Package Contents to open it.

5. Navigate to the location of the privacy manifest in your archive.

#### Managing an invalid privacy manifest

If you’re unable to obtain a valid privacy manifest from a third-party SDK developer and need to submit your app, locate the invalid privacy manifest in your app archive, delete it, and submit your archive using Xcode. Alternatively, locate the invalid privacy manifest in your app, fix the validation issues in the file, and submit your archive using Xcode. To troubleshoot invalid privacy manifests, see TN3181: Debugging an invalid privacy manifest.

[Important]

Important: Removing or modifying the invalid privacy manifest breaks the archived app’s signature. Xcode will re-sign your app when you distribute your archive from the Archives organizer. For more information, see “Select a method for distribution,” in Distributing your app for beta testing and releases.

## Essentials

- Describing data use in privacy manifests: Declare the data collected by your app or by third-party SDKs.

- Describing use of required reason API: Ensure your use of covered API is consistent with policy.

- Editing property list files: Add, remove, and change keys and values in a structured file.

- App Privacy Configuration: A data structure that represents the root object in a privacy manifest file.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyAccessedAPITypes/NSPrivacyAccessedAPIType
# NSPrivacyAccessedAPIType

A string that describes a category of required reason API your app or third-party SDK uses.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyAccessedAPIType

ideTitle: Privacy Accessed API Type

titleStyle: symbol

string

## Possible Values

### NSPrivacyAccessedAPICategoryFileTimestamp

The following APIs for accessing file timestamps require reasons for use.

- creationDate

- modificationDate

- fileModificationDate

- contentModificationDateKey

- creationDateKey

- getattrlist(_:_:_:_:_:)

- getattrlistbulk(_:_:_:_:_:)

- fgetattrlist(_:_:_:_:_:)

- stat

- fstat(_:_:)

- fstatat(_:_:_:_:)

- lstat(_:_:)

- getattrlistat(_:_:_:_:_:_:)

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from this list.

DDA9.1: Declare this reason to display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device.

C617.1: Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container.

3B52.1: Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller.

0A2A.1: Declare this reason if your third-party SDK is providing a wrapper function around file timestamp API(s) for the app to use, and you only access the file timestamp APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s). Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

### NSPrivacyAccessedAPICategorySystemBootTime

The following APIs for accessing the system boot time require reasons for use.

- systemUptime

- mach_absolute_time()

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

35F9.1: Declare this reason to access the system boot time in order to measure the amount of time that has elapsed between events that occurred within the app or to perform calculations to enable timers. Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception for information about the amount of time that has elapsed between events that occurred within the app, which may be sent off-device.

8FFB.1: Declare this reason to access the system boot time to calculate absolute timestamps for events that occurred within your app, such as events related to the UIKit or AVFAudio frameworks. Absolute timestamps for events that occurred within your app may be sent off-device. System boot time accessed for this reason, or any other information derived from system boot time, may not be sent off-device.

3D61.1: Declare this reason to include system boot time information in an optional bug report that the person using the device chooses to submit. The system boot time information must be prominently displayed to the person as part of the report. Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including system boot time information, and only for the purpose of investigating or responding to the bug report.

### NSPrivacyAccessedAPICategoryDiskSpace

The following APIs for accessing the available disk space require reasons for use.

- volumeAvailableCapacityKey

- volumeAvailableCapacityForImportantUsageKey

- volumeAvailableCapacityForOpportunisticUsageKey

- volumeTotalCapacityKey

- systemFreeSize

- systemSize

- statfs(_:_:)

- statvfs(_:_:)

- fstatfs(_:_:)

- fstatvfs(_:_:)

- getattrlist(_:_:_:_:_:)

- fgetattrlist(_:_:_:_:_:)

- getattrlistat(_:_:_:_:_:_:)

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

85F4.1: Declare this reason to display disk space information to the person using the device. Disk space may be displayed in units of information (such as bytes) or units of time combined with a media type (such as minutes of HD video). Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to send disk space information over the local network to another device operated by the same person only for the purpose of displaying disk space information on that device; this exception only applies if the user has provided explicit permission to send disk space information, and the information may not be sent over the Internet.

E174.1: Declare this reason to check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users. Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to avoid downloading files from a server when disk space is insufficient.

7D9E.1: Declare this reason to include disk space information in an optional bug report that the person using the device chooses to submit. The disk space information must be prominently displayed to the person as part of the report. Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including disk space information, and only for the purpose of investigating or responding to the bug report.

B728.1: Declare this reason if your app is a health research app, and you access this API category to detect and inform research participants about low disk space impacting the research data collection. Your app must comply with App Store Review Guideline §5.1.3. Your app must not offer any functionality other than providing information about and allowing people to participate in health research.

### NSPrivacyAccessedAPICategoryActiveKeyboards

The following API for accessing the list of active keyboards requires reasons for use.

- activeInputModes

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

3EC4.1: Declare this reason if your app is a custom keyboard app, and you access this API category to determine the keyboards that are active on the device. Providing a systemwide custom keyboard to the user must be the primary functionality of the app. Information accessed for this reason, or any derived information, may not be sent off-device.

54BD.1: Declare this reason to access active keyboard information to present the correct customized user interface to the person using the device. The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users. Information accessed for this reason, or any derived information, may not be sent off-device.

### NSPrivacyAccessedAPICategoryUserDefaults

The following API for accessing user defaults requires reasons for use.

- UserDefaults

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

CA92.1: Declare this reason to access user defaults to read and write information that is only accessible to the app itself. This reason does not permit reading information that was written by other apps or the system, or writing information that can be accessed by other apps.

1C8F.1: Declare this reason to access user defaults to read and write information that is only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself. This reason does not permit reading information that was written by apps, app extensions, or App Clips outside the same App Group or by the system. Your app is not responsible if the system provides information from the global domain because a key is not present in your requested domain while your app is attempting to read information that apps, app extensions, or App Clips in your app’s App Group write. This reason also does not permit writing information that can be accessed by apps, app extensions, or App Clips outside the same App Group.

C56D.1: Declare this reason if your third-party SDK is providing a wrapper function around user defaults API(s) for the app to use, and you only access the user defaults APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s). Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

AC6B.1: Declare this reason to access user defaults to read the com.apple.configuration.managed key to retrieve the managed app configuration set by MDM, or to set the com.apple.feedback.managed key to store feedback information to be queried over MDM, as described in the Apple Mobile Device Management Protocol Reference documentation.

### Discussion

For information on required reason API, see Describing use of required reason API.

## Reporting privacy accessed API usage

- NSPrivacyAccessedAPITypeReasons: An array of strings that identifies the reasons your app or third-party SDK uses required reason API.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyAccessedAPITypes/NSPrivacyAccessedAPITypeReasons
# NSPrivacyAccessedAPITypeReasons

An array of strings that identifies the reasons your app or third-party SDK uses required reason API.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyAccessedAPITypeReasons

ideTitle: Privacy Accessed API Reasons

titleStyle: symbol

string 

## Possible Values

### DDA9.1

Declare this reason to display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device.

### C617.1

Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container.

### 3B52.1

Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller.

### 0A2A.1

Declare this reason if your third-party SDK is providing a wrapper function around file timestamp API(s) for the app to use, and you only access the file timestamp APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s).

Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

### 35F9.1

Declare this reason to access the system boot time in order to measure the amount of time that has elapsed between events that occurred within the app or to perform calculations to enable timers.

Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception for information about the amount of time that has elapsed between events that occurred within the app, which may be sent off-device.

### 8FFB.1

Declare this reason to access the system boot time to calculate absolute timestamps for events that occurred within your app, such as events related to the UIKit or AVFAudio frameworks.

Absolute timestamps for events that occurred within your app may be sent off-device. System boot time accessed for this reason, or any other information derived from system boot time, may not be sent off-device.

### 3D61.1

Declare this reason to include system boot time information in an optional bug report that the person using the device chooses to submit. The system boot time information must be prominently displayed to the person as part of the report.

### 85F4.1

Declare this reason to display disk space information to the person using the device. Disk space may be displayed in units of information (such as bytes) or units of time combined with a media type (such as minutes of HD video).

Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to send disk space information over the local network to another device operated by the same person only for the purpose of displaying disk space information on that device; this exception only applies if the user has provided explicit permission to send disk space information, and the information may not be sent over the Internet.

### E174.1

Declare this reason to check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users.

Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to avoid downloading files from a server when disk space is insufficient.

### 7D9E.1

Declare this reason to include disk space information in an optional bug report that the person using the device chooses to submit. The disk space information must be prominently displayed to the person as part of the report.

Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including disk space information, and only for the purpose of investigating or responding to the bug report.

### B728.1

Declare this reason if your app is a health research app, and you access this API category to detect and inform research participants about low disk space impacting the research data collection.

Your app must comply with App Store Review Guideline §5.1.3. Your app must not offer any functionality other than providing information about and allowing people to participate in health research.

### 3EC4.1

Declare this reason if your app is a custom keyboard app, and you access this API category to determine the keyboards that are active on the device. Providing a systemwide custom keyboard to the user must be the primary functionality of the app.

Information accessed for this reason, or any derived information, may not be sent off-device.

### 54BD.1

Declare this reason to access active keyboard information to present the correct customized user interface to the person using the device. The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users.

Information accessed for this reason, or any derived information, may not be sent off-device.

### CA92.1

Declare this reason to access user defaults to read and write information that is only accessible to the app itself.

This reason does not permit reading information that was written by other apps or the system, or writing information that can be accessed by other apps.

### 1C8F.1

Declare this reason to access user defaults to read and write information that is only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself.

This reason does not permit reading information that was written by apps, app extensions, or App Clips outside the same App Group or by the system. Your app is not responsible if the system provides information from the global domain because a key is not present in your requested domain while your app is attempting to read information that apps, app extensions, or App Clips in your app’s App Group write.

This reason also does not permit writing information that can be accessed by apps, app extensions, or App Clips outside the same App Group.

### C56D.1

Declare this reason if your third-party SDK is providing a wrapper function around user defaults API(s) for the app to use, and you only access the user defaults APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s).

Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

### AC6B.1

Declare this reason to access user defaults to read the com.apple.configuration.managed key to retrieve the managed app configuration set by MDM, or to set the com.apple.feedback.managed key to store feedback information to be queried over MDM, as described in the Apple Mobile Device Management Protocol Reference documentation.

### Discussion

For information on which reasons your app or third-party SDK declares for each category of required reasons API it uses, see NSPrivacyAccessedAPIType.

For information on required reason API, see Describing use of required reason API.

## Reporting privacy accessed API usage

- NSPrivacyAccessedAPIType: A string that describes a category of required reason API your app or third-party SDK uses.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyAccessedAPITypes
# NSPrivacyAccessedAPITypes

A list of dictionaries that report the privacy accessed API your app or third-party SDK uses.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyAccessedAPITypes

ideTitle: Privacy Accessed API Types

titleStyle: symbol

dictionary 

### Overview

For more information, see Describing use of required reason API.

## Reporting privacy accessed API usage

- NSPrivacyAccessedAPIType: A string that describes a category of required reason API your app or third-party SDK uses.

- NSPrivacyAccessedAPITypeReasons: An array of strings that identifies the reasons your app or third-party SDK uses required reason API.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyCollectedDataTypes/NSPrivacyCollectedDataType
# NSPrivacyCollectedDataType

A string that identifies the type of data your app or third-party SDK collects.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyCollectedDataType

ideTitle: Collected Data Type

titleStyle: symbol

string

## Possible Values

### NSPrivacyCollectedDataTypeName

Name, such as first or last name.

### NSPrivacyCollectedDataTypeEmailAddress

Email address, including but not limited to a hashed email address.

### NSPrivacyCollectedDataTypePhoneNumber

Phone number, including but not limited to a hashed phone number.

### NSPrivacyCollectedDataTypePhysicalAddress

Physical address, such as home address, physical address, or mailing address.

### NSPrivacyCollectedDataTypeOtherUserContactInfo

Other user contact info; any other information that can be used to contact the user outside the app.

### NSPrivacyCollectedDataTypeHealth

Health and medical data, including but not limited to data from the Clinical Health Records API, HealthKit API, MovementDisorderAPIs, or health-related human subject research or any other user provided health or medical data.

### NSPrivacyCollectedDataTypeFitness

Fitness and exercise data, including but not limited to the Motion and Fitness API.

### NSPrivacyCollectedDataTypePaymentInfo

Payment info; such as form of payment, payment card number, or bank account number. If your app uses a payment service, the payment information is entered outside your app, and you as the developer never have access to the payment information, it is not collected and does not need to be disclosed.

### NSPrivacyCollectedDataTypeCreditInfo

Credit info, such as credit score.

### NSPrivacyCollectedDataTypeOtherFinancialInfo

Other financial info; such as salary, income, assets, debts, or any other financial information.

### NSPrivacyCollectedDataTypePreciseLocation

Precise location; information that describes the location of a user or device with the same or greater resolution as a latitude and longitude with three or more decimal places.

### NSPrivacyCollectedDataTypeCoarseLocation

Coarse location; information that describes the location of a user or device with lower resolution than a latitude and longitude with three or more decimal places, such as Approximate Location Services.

### NSPrivacyCollectedDataTypeSensitiveInfo

Sensitive information; such as racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data.

### NSPrivacyCollectedDataTypeContacts

Contacts; such as a list of contacts in the user’s phone, address book, or social graph.

### NSPrivacyCollectedDataTypeEmailsOrTextMessages

Emails or text messages; including subject line, sender, recipients, and contents of the email or message.

### NSPrivacyCollectedDataTypePhotosorVideos

The user’s photos or videos.

### NSPrivacyCollectedDataTypeAudioData

The user’s voice or sound recordings.

### NSPrivacyCollectedDataTypeGameplayContent

Gameplay content; such as saved games, multiplayer matching or gameplay logic, or user-generated content in-game.

### NSPrivacyCollectedDataTypeCustomerSupport

Data generated by the user during a customer support request.

### NSPrivacyCollectedDataTypeOtherUserContent

Any other user-generated content.

### NSPrivacyCollectedDataTypeBrowsingHistory

Browsing history; information about content the user has viewed that is not part of the app, such as websites.

### NSPrivacyCollectedDataTypeSearchHistory

Information about searches performed in the app.

### NSPrivacyCollectedDataTypeUserID

User ID; such as screen name, handle, account ID, assigned user ID, customer number, or other user- or account-level ID that can be used to identify a particular user or account.

### NSPrivacyCollectedDataTypeDeviceID

Device ID; such as the device’s advertising identifier, or other device-level ID.

### NSPrivacyCollectedDataTypePurchaseHistory

An account’s or individual’s purchases or purchase tendencies.

### NSPrivacyCollectedDataTypeProductInteraction

Product interaction; such as app launches, taps, clicks, scrolling information, music listening data, video views, saved place in a game, video, or song, or other information about how the user interacts with the app.

### NSPrivacyCollectedDataTypeAdvertisingData

Advertising data; such as information about the advertisements the user has seen.

### NSPrivacyCollectedDataTypeOtherUsageData

Any other data about user activity in the app.

### NSPrivacyCollectedDataTypeCrashData

Crash data, such as crash logs.

### NSPrivacyCollectedDataTypePerformanceData

Performance data, such as launch time, freeze rate, or energy use.

### NSPrivacyCollectedDataTypeOtherDiagnosticData

Any other data collected for the purposes of measuring technical diagnostics related to the app.

### NSPrivacyCollectedDataTypeEnvironmentScanning

Environment scanning; such as mesh, planes, scene classification, and/or image detection of the user’s surroundings.

### NSPrivacyCollectedDataTypeHands

The user’s hand structure and hand movements.

### NSPrivacyCollectedDataTypeHead

The user’s head movement.

### NSPrivacyCollectedDataTypeOtherDataTypes

Any other data types not mentioned.

### Discussion

Choose the value that matches the data your app or third-party SDK collects.

## Reporting categories of collected data

- NSPrivacyCollectedDataTypePurposes: An array of strings that identify reasons your app or third-party SDK collects private data.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyCollectedDataTypes/NSPrivacyCollectedDataTypeLinked
# NSPrivacyCollectedDataTypeLinked

A Boolean that indicates whether your app or third-party SDK links this data type to the user’s identity.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyCollectedDataTypeLinked

ideTitle: Linked to User

titleStyle: symbol

boolean

### Discussion

For more information, see Data linked to the user in App privacy details on the App Store.

## Reporting tracking and linking collected data

- NSPrivacyCollectedDataTypeTracking: A Boolean that indicates whether your app or third-party SDK uses this data type to track.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyCollectedDataTypes/NSPrivacyCollectedDataTypePurposes
# NSPrivacyCollectedDataTypePurposes

An array of strings that identify reasons your app or third-party SDK collects private data.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyCollectedDataTypePurposes

ideTitle: Collection Purposes

titleStyle: symbol

string 

## Possible Values

### NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising

Third-party advertising; such as displaying third-party ads in your app, or sharing data with entities who display third-party ads.

### NSPrivacyCollectedDataTypePurposeDeveloperAdvertising

Developer’s advertising or marketing; such as displaying first-party ads in your app, sending marketing communications directly to your users, or sharing data with entities who will display your ads.

### NSPrivacyCollectedDataTypePurposeAnalytics

Analytics — using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics.

### NSPrivacyCollectedDataTypePurposeProductPersonalization

Product personalization — customizing what the user sees, such as a list of recommended products, posts, or suggestions.

### NSPrivacyCollectedDataTypePurposeAppFunctionality

App functionality; such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support.

### NSPrivacyCollectedDataTypePurposeOther

Any other purposes not listed.

## Reporting categories of collected data

- NSPrivacyCollectedDataType: A string that identifies the type of data your app or third-party SDK collects.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyCollectedDataTypes/NSPrivacyCollectedDataTypeTracking
# NSPrivacyCollectedDataTypeTracking

A Boolean that indicates whether your app or third-party SDK uses this data type to track.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyCollectedDataTypeTracking

ideTitle: Used for Tracking

titleStyle: symbol

boolean

## Reporting tracking and linking collected data

- NSPrivacyCollectedDataTypeLinked: A Boolean that indicates whether your app or third-party SDK links this data type to the user’s identity.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyCollectedDataTypes
# NSPrivacyCollectedDataTypes

A list of dictionaries that report the categories of private data your app or third-party SDK collects.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyCollectedDataTypes

ideTitle: Privacy Nutrition Label Types

titleStyle: symbol

dictionary 

### Overview

For more information, see Describing data use in privacy manifests.

## Reporting categories of collected data

- NSPrivacyCollectedDataType: A string that identifies the type of data your app or third-party SDK collects.

- NSPrivacyCollectedDataTypePurposes: An array of strings that identify reasons your app or third-party SDK collects private data.

## Reporting tracking and linking collected data

- NSPrivacyCollectedDataTypeLinked: A Boolean that indicates whether your app or third-party SDK links this data type to the user’s identity.

- NSPrivacyCollectedDataTypeTracking: A Boolean that indicates whether your app or third-party SDK uses this data type to track.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyTracking
# NSPrivacyTracking

A Boolean value that indicates whether your app or third-party SDK uses data for tracking.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyTracking

ideTitle: Privacy Tracking Enabled

titleStyle: symbol

boolean

### Overview

Set the value for this key to true if your app or third-party SDK uses data for tracking as defined under the App Tracking Transparency framework. When set to true you need to provide a list of internet domains in NSPrivacyTrackingDomains. For more information, see User Privacy and Data Use.

## Declaring tracking

- NSPrivacyTrackingDomains: A list of the internet domains your app or third-party SDK uses for tracking.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyTrackingDomains
# NSPrivacyTrackingDomains

A list of the internet domains your app or third-party SDK uses for tracking.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: NSPrivacyTrackingDomains

ideTitle: Privacy Tracking Domains

titleStyle: symbol

string 

### Overview

If the user has not granted tracking permission through the App Tracking Transparency framework, network requests to these domains fail and your app receives an error. To provide a list of internet domains in NSPrivacyTrackingDomains, set NSPrivacyTracking to true. For more information, see User Privacy and Data Use.

## Declaring tracking

- NSPrivacyTracking: A Boolean value that indicates whether your app or third-party SDK uses data for tracking.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/App-Privacy-Configuration
# App Privacy Configuration

A data structure that represents the root object in a privacy manifest file.

iOS 17.0, iPadOS 17.0, Mac Catalyst 14.0, macOS 14.0, tvOS 17.0, visionOS 1.0, watchOS 10.0

name: App Privacy Configuration

titleStyle: symbol

dictionary

### Overview

Use the keys and values in this object in the privacy manifest for your app or third-party SDK. For more information, see Privacy manifest files.

## Describing privacy accessed API use

- NSPrivacyAccessedAPITypes: A list of dictionaries that report the privacy accessed API your app or third-party SDK uses.

## Describing collected data

- NSPrivacyCollectedDataTypes: A list of dictionaries that report the categories of private data your app or third-party SDK collects.

## Declaring tracking

- NSPrivacyTracking: A Boolean value that indicates whether your app or third-party SDK uses data for tracking.

- NSPrivacyTrackingDomains: A list of the internet domains your app or third-party SDK uses for tracking.

## Essentials

- Adding a privacy manifest to your app or third-party SDK: Report the data you collect and the required reasons API you use in your app or third-party SDK.

- Describing data use in privacy manifests: Declare the data collected by your app or by third-party SDKs.

- Describing use of required reason API: Ensure your use of covered API is consistent with policy.

- Editing property list files: Add, remove, and change keys and values in a structured file.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/describing-data-use-in-privacy-manifests
# Describing data use in privacy manifests

Declare the data collected by your app or by third-party SDKs.

### Overview

Record the categories of data that your app or third-party SDK collects about the person using the app, and the reasons it collects the data. App developers can use Xcode to create a privacy report, summarizing the information about collected data in their app and the third-party SDKs the app links to.

[Important]

Important:  Third-party SDKs need to provide their own privacy manifest files that record the types of data they collect. Your app’s privacy manifest file doesn’t need to cover data collected by third-party SDKs that your app links to.

#### Describe the data your app or third-party SDK collects

For each type of data your app or third-party SDK collects, add a dictionary to the NSPrivacyCollectedDataTypes array in your privacy information file. Add the following keys to the dictionary.

NSPrivacyCollectedDataType: A string that identifies the type of data your app or third-party SDK collects. Choose the value from the list of data types below that matches the data your app or third-party SDK collects.

NSPrivacyCollectedDataTypeLinked: A Boolean that indicates whether your app or third-party SDK links this data type to the user’s identity. For more information, see Data linked to the user in App privacy details on the App Store.

NSPrivacyCollectedDataTypeTracking: A Boolean that indicates whether your app or third-party SDK uses this data type to track.

NSPrivacyCollectedDataTypePurposes: An array of strings that lists the reasons your app or third-party SDK collects the data. Choose values from the list of purposes below that match the reasons your app or third-party SDK collects this data type.

Xcode won’t generate a privacy report correctly if you define your own collected data types for the NSPrivacyCollectedDataType key, or provide your own reasons for the NSPrivacyCollectedDataTypePurposes key. Use values listed in the documentation for the keys.

#### Create your app’s privacy report

Xcode can create a privacy report by aggregating the privacy manifests from your app and the third-party SDKs it links to. Use the privacy report to better understand all of the data collected by your app and whether it tracks. Create the privacy report for your app by doing the following:

1. Open your project in Xcode.

2. Choose Product > Archive. Xcode creates the archive and reveals it in the organizer.

3. Control-click the archive in the organizer and choose Generate Privacy Report.

4. Choose a location to save the privacy report.

5. Switch to Finder.

6. Navigate to the location where you saved the privacy report, and double-click to open the report in Preview.

The privacy report is organized in a similar way to Privacy Nutrition Labels. Refer to this report when you provide your app’s privacy details in App Store Connect. For more information on providing your app’s privacy details, see App privacy details on the App Store.

## Essentials

- Adding a privacy manifest to your app or third-party SDK: Report the data you collect and the required reasons API you use in your app or third-party SDK.

- Describing use of required reason API: Ensure your use of covered API is consistent with policy.

- Editing property list files: Add, remove, and change keys and values in a structured file.

- App Privacy Configuration: A data structure that represents the root object in a privacy manifest file.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/describing-use-of-required-reason-api
# Describing use of required reason API

Ensure your use of covered API is consistent with policy.

### Overview

Some APIs that your app uses to deliver its core functionality — in code you write or included in a third-party SDK — have the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. Describe the reasons your app or third-party SDK on iOS, iPadOS, tvOS, visionOS, or watchOS uses these APIs, and check that your app or third-party SDK only uses the APIs for the expected reasons.

[Important]

Important:  If you upload an app to App Store Connect that uses required reason API without describing the reason in its privacy manifest file, Apple sends you an email reminding you to add the reason to the app’s privacy manifest. Starting May 1, 2024, apps that don’t describe their use of required reason API in their privacy manifest file aren’t accepted by App Store Connect.

For each category of required reason API that your app or third-party SDK uses, add a dictionary to the NSPrivacyAccessedAPITypes array in your app or third-party SDK’s privacy manifest file that reports the reasons your app uses the API category. If you use the API in your app’s code, then you need to report the API in your app’s privacy manifest file. If you use the API in your third-party SDK’s code, then you need to report the API in your third-party SDK’s privacy manifest file. Your third-party SDK can’t rely on the privacy manifest files for apps that link the third-party SDK, or those of other third-party SDKs the app links, to report your third-party SDK’s use of required reasons API.

For each executable or dynamic library in an app that uses a required reason API, the bundle that includes the executable or dynamic library needs to include a privacy manifest file that reports the API. For the expected location of frameworks and dynamic libraries, see Placing content in a bundle.

[Important]

Important:  Your app or third-party SDK must declare one or more approved reasons that accurately reflect your use of each of these APIs and the data derived from their use. You may use these APIs and the data derived from their use for the declared reasons only. These declared reasons must be consistent with your app’s functionality as presented to users, and you may not use the APIs or derived data for tracking.

Each dictionary in the NSPrivacyAccessedAPITypes array needs to contain these keys and values:

NSPrivacyAccessedAPIType: A string that identifies the category of required reason APIs your app uses. The value you provide must be one of the values listed in the sections below.

NSPrivacyAccessedAPITypeReasons: An array of strings that identifies the reasons your app uses the APIs. The values you provide must be the values associated with the accessed API type in the sections below.

The categories of required reason APIs, which APIs are in each category, and the reasons you can include in a privacy manifest are described in the documentation for the dictionary keys.

[Note]

Note:  Apple continually reviews the list of required reason APIs and reasons for usage, and will update this article from time to time. If your app uses required reason API to provide benefits to the people using the app, for a reason that isn’t listed here, submit a request for a new approved reason.

For more information on creating a privacy manifest file, see Create a privacy manifest.

## Essentials

- Adding a privacy manifest to your app or third-party SDK: Report the data you collect and the required reasons API you use in your app or third-party SDK.

- Describing data use in privacy manifests: Declare the data collected by your app or by third-party SDKs.

- Editing property list files: Add, remove, and change keys and values in a structured file.

- App Privacy Configuration: A data structure that represents the root object in a privacy manifest file.

=== SOURCE: https://developer.apple.comdoc://com.apple.bundleresources/documentation/BundleResources/privacy-manifest-files
# Privacy manifest files

Describe the data your app or third-party SDK collects and the required reasons APIs it uses.

### Overview

Apps and third-party SDKs — distributed as XCFrameworks, Swift packages, or Xcode projects — can contain a privacy manifest file, named PrivacyInfo.xcprivacy. The privacy manifest is a property list that records the following information:

- The types of data collected by your app or third-party SDK. You need to provide this information for your app or third-party SDK on all platforms.

- The required reasons APIs your app or third-party SDK uses. You need to provide this information for your app or third-party SDK on iOS, iPadOS, tvOS, visionOS, and watchOS.

For each type of data your app or third-party SDK collects and category of required reasons API it uses, the app or third-party SDK needs to record the reasons in its bundled privacy manifest file.

[Important]

Important:  You need to include a privacy manifest file in your third-party SDK if it’s listed in “SDKs that require a privacy manifest and signature,” in Upcoming third-party SDK requirements. Otherwise, include a privacy manifest file in your third-party SDK if it uses a required reasons API, collects data about the person using apps that include the third-party SDK, enables the app to collect data about people using the app, or contacts tracking domains. Providing a privacy manifest file helps app developers understand the API use and data-collection practices of your third-party SDK.

For information on editing the privacy manifest file, see Editing property list files.

#### Create a privacy manifest

To add the privacy manifest to your app or third-party SDK in Xcode, follow these steps:

- Choose File > New File.

- Scroll down to the Resource section, and select App Privacy File type.

- Click Next.

- Check your app or third-party SDK’s target in the Targets list.

- Click Create.

By default, the file is named PrivacyInfo.xcprivacy; this is the required file name for bundled privacy manifests.

[Note]

Note:  You need to add the privacy manifest file to your target’s resources for Xcode to use it when you generate a privacy report. If you distribute your third-party SDK as a static library, use the support for static frameworks in Xcode 15 or later to bundle resources, including the privacy manifest file. Create a framework target in Xcode that builds your product, set its Mach-O type build setting to “Static Library,” and add the privacy manifest file to your target’s bundle resources along with any other resources, for example, image files.

At the top level of this property list file, add the following keys to the dictionary:

NSPrivacyTracking: A Boolean that indicates whether your app or third-party SDK uses data for tracking as defined under the App Tracking Transparency framework. When set to true you need to provide a list of internet domains in NSPrivacyTrackingDomains. For more information, see User Privacy and Data Use.

NSPrivacyTrackingDomains: An array of strings that lists the internet domains your app or third-party SDK connects to that engage in tracking. If the user has not granted tracking permission through the App Tracking Transparency framework, network requests to these domains fail and your app receives an error. To provide a list of internet domains in NSPrivacyTrackingDomains, set NSPrivacyTracking to true.

NSPrivacyCollectedDataTypes: An array of dictionaries that describes the data types your app or third-party SDK collects. For information on the keys and values to use in the dictionaries, see Describing data use in privacy manifests.

NSPrivacyAccessedAPITypes: An array of dictionaries that describe the API types your app or third-party SDK accesses that have been designated as APIs that require reasons to access. For information on the keys and values to use in the dictionaries, see Describing use of required reason API.

## Essentials

- Adding a privacy manifest to your app or third-party SDK: Report the data you collect and the required reasons API you use in your app or third-party SDK.

- Describing data use in privacy manifests: Declare the data collected by your app or by third-party SDKs.

- Describing use of required reason API: Ensure your use of covered API is consistent with policy.

- Editing property list files: Add, remove, and change keys and values in a structured file.

- App Privacy Configuration: A data structure that represents the root object in a privacy manifest file.

## Property Lists

- Entitlements: Key-value pairs that grant an executable permission to use a service or technology.

- Information Property List: A resource containing key-value pairs that identify and configure a bundle.

=== SOURCE: https://developer.apple.com/support/third-party-SDK-requirements/
# Third-party SDK requirements

Third-party software development kits (SDKs) can provide great functionality for apps; they can also have the potential to impact user privacy in ways that aren’t obvious to developers and users. As a reminder, when you use a third-party SDK with your app, you are responsible for all the code the SDK includes in your app, and need to be aware of its data collection and use practices. At WWDC23, we introduced new privacy manifests and signatures for SDKs to help bring more awareness for how third-party SDKs use data. This functionality is a step forward for all apps, and we encourage all SDKs to adopt it to better support the apps that depend on them.

#### Privacy Manifests

Privacy manifest files outline the privacy practices of the third-party code in an app, in a single standard format. When you prepare to distribute your app, Xcode will combine the privacy manifests across all the third-party SDKs used by your app into a single, easy-to-use report. With one comprehensive report that summarizes all the third-party SDKs found in an app, it will be even easier for you to create more accurate Privacy Nutrition Labels.

#### Signatures for SDKs

When you adopt a new version of a third-party SDK in your app, Xcode will validate that it was signed by the same developer, improving the integrity of your software supply chain.

#### SDKs that require a privacy manifest and signature

The following are commonly used SDKs in apps on the App Store. You must include the privacy manifest for any SDK listed below when you submit new apps in App Store Connect that include those SDKs, or when you submit an app update that adds one of the listed SDKs as part of the update. Signatures are also required in these cases where the listed SDKs are used as binary dependencies. Any version of a listed SDK, as well as any SDKs that repackage those on the list, are included in the requirement.

- Abseil

- AFNetworking

- Alamofire

- AppAuth

- BoringSSL / openssl_grpc

- Capacitor

- Charts

- connectivity_plus

- Cordova

- device_info_plus

- DKImagePickerController

- DKPhotoGallery

- FBAEMKit

- FBLPromises

- FBSDKCoreKit

- FBSDKCoreKit_Basics

- FBSDKLoginKit

- FBSDKShareKit

- file_picker

- FirebaseABTesting

- FirebaseAuth

- FirebaseCore

- FirebaseCoreDiagnostics

- FirebaseCoreExtension

- FirebaseCoreInternal

- FirebaseCrashlytics

- FirebaseDynamicLinks

- FirebaseFirestore

- FirebaseInstallations

- FirebaseMessaging

- FirebaseRemoteConfig

- Flutter

- flutter_inappwebview

- flutter_local_notifications

- fluttertoast

- FMDB

- geolocator_apple

- GoogleDataTransport

- GoogleSignIn

- GoogleToolboxForMac

- GoogleUtilities

- grpcpp

- GTMAppAuth

- GTMSessionFetcher

- hermes

- image_picker_ios

- IQKeyboardManager

- IQKeyboardManagerSwift

- Kingfisher

- leveldb

- Lottie

- MBProgressHUD

- nanopb

- OneSignal

- OneSignalCore

- OneSignalExtension

- OneSignalOutcomes

- OpenSSL

- OrderedSet

- package_info

- package_info_plus

- path_provider

- path_provider_ios

- Promises

- Protobuf

- Reachability

- RealmSwift

- RxCocoa

- RxRelay

- RxSwift

- SDWebImage

- share_plus

- shared_preferences_ios

- SnapKit

- sqflite

- Starscream

- SVProgressHUD

- SwiftyGif

- SwiftyJSON

- Toast

- UnityFramework

- url_launcher

- url_launcher_ios

- video_player_avfoundation

- wakelock

- webview_flutter_wkwebview

=== SOURCE: https://developer.apple.comdoc://com.apple.technotes/documentation/Technotes/tn3181-debugging-invalid-privacy-manifest
# TN3181: Debugging an invalid privacy manifest

Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.

### Overview

Starting November 12, 2024, apps you submit for review in App Store Connect must contain a valid privacy manifest file. If you upload an app to App Store Connect that contains invalid privacy manifest files, you’ll receive an email that includes the name and path of the invalid files in your app bundle. For example:

ITMS-91056: Invalid privacy manifest - The PrivacyInfo.xcprivacy file from the following path
is invalid: "PrivacyInfo.xcprivacy". Keys and values in your app's privacy manifests must be
valid. For more details about privacy manifest files, visit: 
https://developer.apple.com/documentation/bundleresources/privacy_manifest_files.

An invalid privacy manifest is:

- A property list file that contains invalid keys or values.

- An improperly formatted property list file.

Review Privacy manifest files to learn about the keys you can include in a privacy manifest. This document lists possible reasons for invalid privacy tracking and accessed API values in your privacy manifest. Validate your privacy manifest to determine why your privacy manifest is malformed.

### Configure a tracking domain

A tracking domain is a string that identifies an internet domain your app or third-party SDK connects to that engages in tracking. You set the value of the NSPrivacyTrackingDomains key to a list of tracking domains in your privacy manifest. The value of the string meets the following requirements:

- Includes the top-level domain or subdomain.

- Contains no path and query components.

- Contains no trailing slash.

### Possible reason for an invalid tracking value

A value for the NSPrivacyTracking key is invalid if the value is any other type than a Boolean. In your privacy manifest, change the type of the key to Boolean.

### Possible reasons for an invalid tracking domains value

A value for the NSPrivacyTrackingDomains key is invalid if the value is any other type than an array of strings. In your privacy manifest, change the type of the key to Array, then add one or more tracking domains to the array. For more information, see Configure a tracking domain.

You can create an invalid privacy manifest when you use both NSPrivacyTrackingDomains and NSPrivacyTracking keys as follows:

| Reason | Solution |

| The value of the NSPrivacyTracking key is true and the value of the NSPrivacyTrackingDomains key is an empty array of strings. | Fill the array with one or more tracking domains your app or third-party SDK connects to. |

| The value of the NSPrivacyTracking key is true and the value of the NSPrivacyTrackingDomains key is an array of strings, but some entries are improperly formatted. | Confirm you configure each tracking domain in the array as described in Configure a tracking domain. |

| The value of the NSPrivacyTracking key is false and the NSPrivacyTrackingDomains key contains some entries. | Remove the NSPrivacyTrackingDomains key from your privacy manifest. |

[Note]

Note: If your app or third-party SDK doesn’t connect, or no longer connects to any tracking domains, remove both NSPrivacyTrackingDomains and NSPrivacyTracking keys from your privacy manifest. Alternatively, set the value of NSPrivacyTracking to false and remove NSPrivacyTrackingDomains from your privacy manifest.

### Possible reasons for an invalid accessed API type value

The following table lists reasons why a value for the NSPrivacyAccessedAPIType key is invalid:

| Reason | Solution |

| The value is any other type than a string. | Change the type of the NSPrivacyAccessedAPIType key to String in your privacy manifest. |

| The value is an empty string, or a string whose value doesn’t match a category of required reason APIs. | Set the value of the NSPrivacyAccessedAPIType key to a string that exactly matches a category of required reason APIs your app uses. For possible values, see Describing use of required reason API. |

### Possible reasons for an invalid accessed API type reasons value

The following table lists reasons why a value for the NSPrivacyAccessedAPITypeReasons key is invalid:

| Reason | Solution |

| The value is any other type than an array of strings. | Change the type of the NSPrivacyAccessedAPITypeReasons key to Array in your privacy manifest. |

| The value is an empty array of strings. | In the dictionary that contains the NSPrivacyAccessedAPITypeReasons key, check the value of the NSPrivacyAccessedAPIType key. Add one or more reason strings to the array whose value exactly matches a value associated with NSPrivacyAccessedAPIType. |

| The value is an array of strings, but some entries don’t match the expected values for the NSPrivacyAccessedAPIType key you provide. | In the dictionary that contains the NSPrivacyAccessedAPITypeReasons key, check the value of the NSPrivacyAccessedAPIType key. Confirm each reason string in the array exactly matches a value associated with NSPrivacyAccessedAPIType. |

[Note]

Note: If your app or third-party SDK doesn’t use, or no longer uses a specific required reason API, remove its related dictionary from the NSPrivacyAccessedAPITypes key. If NSPrivacyAccessedAPITypes is empty, remove it from the privacy manifest.

### Possible reasons for an invalid accessed API types value

The following table lists reasons why a value for the NSPrivacyAccessedAPITypes key is invalid:

| Reason | Solution |

| The value is any other type than an array of dictionaries. | Change the type of the NSPrivacyAccessedAPITypes key to Array in your privacy manifest. |

| The value is an empty array of dictionaries. | Create a dictionary that includes information about a required reason API your app or third-party SDK uses, then add the dictionary to the array. Repeat the process for all required reason APIs your app or third-party SDK uses. |

| The value is an array of dictionaries, but some of the dictionaries are invalid. | Confirm each dictionary in the array contains a NSPrivacyAccessedAPIType key and a NSPrivacyAccessedAPITypeReasons key, and both keys contain valid values. |

### Validate your privacy manifest file

You can use the plutil command to ensure your privacy manifest is a properly formatted plist file. To validate your privacy manifest, run plutil with the -lint option in Terminal:

% plutil -lint /path/to/PrivacyInfo.xcprivacy

If the privacy manifest is a valid plist, the command prints a message similar to the following:

% plutil -lint PrivacyInfo.xcprivacy
~/Documents/SampleApp/PrivacyInfo.xcprivacy: OK

If the privacy manifest is malformed, an error message appears in Terminal:

% plutil -lint PrivacyInfo.xcprivacy
~/Documents/SampleApp/PrivacyInfo.xcprivacy: Encountered unexpected character 
`a` on line 8 while looking for close tag 

To fix the errors, open your privacy manifest in a text editor or Xcode to address them.

[Note]

Note: If your privacy manifest is a valid plist, check its keys and values. Your privacy manifest could still be invalid if its keys and values don’t match the values App Store Connect expects. For more information about the keys and values App Store Connect expects, see Privacy manifest files.

### Revision History

- 2024-11-12 First published.

## Related Documentation

- TN3182: Adding privacy tracking keys to your privacy manifest: Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.

- TN3183: Adding required reason API entries to your privacy manifest: Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.

- TN3184: Adding data collection details to your privacy manifest: Declare the data your app or third-party SDK collects in a privacy manifest.

=== SOURCE: https://developer.apple.comdoc://com.apple.technotes/documentation/Technotes/tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest
# TN3182: Adding privacy tracking keys to your privacy manifest

Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.

### Overview

When you build an app or third-party SDK that contacts domains engaged in tracking, perform these steps in your privacy manifest (PrivacyInfo.xcprivacy):

1. Add the NSPrivacyTracking key and set its value to true.

2. Add the NSPrivacyTrackingDomains key and set its value to a list of tracking domains.

For more information about these keys and the privacy manifest, see Privacy manifest files.

This document describes how to add the NSPrivacyTracking and NSPrivacyTrackingDomains keys to your privacy manifest in Xcode. If you work outside of Xcode, review this document to learn about the expected structure of each key.

[Note]

Note: Before you start adding the keys to your privacy manifest, enable raw keys and values in Xcode to view the raw keys and hide their human-readable names. Click anywhere in the privacy manifest, then choose Xcode > Editor > Raw Keys and Values. Repeat the process to disable this feature.

### Add the privacy tracking key

The NSPrivacyTracking key uses the following format:

<key>NSPrivacyTracking</key>
<!-- Use <true/> if your app or third-party SDK contacts domains engaged in tracking; otherwise use 
    <false/>. -->
<true/>

To add the NSPrivacyTracking key to your privacy manifest:

1. Select PrivacyInfo.xcprivacy in the Project navigator.

2. Click the Add button (+) beside the App Privacy Configuration key in the property list editor.

3. In the pop-up menu that appears, choose NSPrivacyTracking.

4. Confirm the value is Boolean in the Type column.

5. Select YES from the pop-up menu in the Value column.

### Add a tracking domain to the privacy tracking domains key

Set the value of the NSPrivacyTrackingDomains key to a list of tracking domains in your privacy manifest. For more information about tracking domains, see “Configure a tracking domain” in TN3181: Debugging an invalid privacy manifest.

To add a tracking domain to the NSPrivacyTrackingDomains key in your privacy manifest:

1. Select PrivacyInfo.xcprivacy in the Project navigator.

2. Find the NSPrivacyTrackingDomains key in the property list editor.

3. Confirm the value is Array in the Type column.

4. Click the disclosure triangle to the left of NSPrivacyTrackingDomains to reveal it.

5. Click the Add button (+) beside NSPrivacyTrackingDomains to insert a tracking domain such as mywebsite.example.com.

### Add the privacy tracking domains key

The NSPrivacyTrackingDomains key uses the following format:

<key>NSPrivacyTrackingDomains</key>
<array>
    <string>mywebsite.example.com</string>
    ...
</array>

Each string value in the array identifies an internet domain your app or third-party SDK connects to that engages in tracking. For more information, see Add a tracking domain to the privacy tracking domains key.

To add the NSPrivacyTrackingDomains key to your privacy manifest:

1. Select PrivacyInfo.xcprivacy in the Project navigator.

2. Click the Add button (+) beside the App Privacy Configuration key in the property list editor.

3. In the pop-up menu that appears, choose NSPrivacyTrackingDomains.

4. Confirm the value is Array in the Type column.

5. To add a tracking domain to the array, see Add a tracking domain to the privacy tracking domains key.

The following example declares one tracking domain for an app called Sample:

Repeat step 5 for each additional tracking domain your app or third-party SDK contacts. The example below declares an additional tracking domain for Sample:

### Revision History

- 2024-12-17 First published.

## Related Documentation

- TN3181: Debugging an invalid privacy manifest: Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.

- TN3183: Adding required reason API entries to your privacy manifest: Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.

- TN3184: Adding data collection details to your privacy manifest: Declare the data your app or third-party SDK collects in a privacy manifest.

=== SOURCE: https://developer.apple.comdoc://com.apple.technotes/documentation/Technotes/tn3183-adding-required-reason-api-entries-to-your-privacy-manifest
# TN3183: Adding required reason API entries to your privacy manifest

Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.

### Overview

When you build an app or third-party SDK that uses any required reason API, perform these steps in your privacy manifest (PrivacyInfo.xcprivacy):

1. Add the NSPrivacyAccessedAPITypes key and set its value to the dictionary.

2. For each required reason API your app or third-party SDK uses, add a dictionary as a value for the NSPrivacyAccessedAPITypes key. The dictionary includes the category of the reason API and a list of reasons for using this API. For more information, see Add an accessed API type and reasons dictionary.

See Privacy manifest files and Describing use of required reason API for more information about the privacy manifest and these keys.

This document describes how to add the NSPrivacyAccessedAPIType, NSPrivacyAccessedAPITypeReasons, and NSPrivacyAccessedAPITypes keys to your privacy manifest in Xcode. If you work outside of Xcode, review this document to learn about the expected structure of each key.

[Note]

Note: Before you start adding the keys to your privacy manifest, enable raw keys and values in Xcode to view the raw keys and hide their human-readable names. Click anywhere in the privacy manifest, then choose Xcode > Editor > Raw Keys and Values. Repeat the process to disable this feature.

### Select an accessed API category

A privacy accessed API category identifies the category of required reason APIs your app or third-party SDK uses. Set the value of the NSPrivacyAccessedAPIType key to a privacy accessed API category. For more information, see Describing use of required reason API.

The possible values of a privacy accessed API category are:

- NSPrivacyAccessedAPICategoryActiveKeyboards

- NSPrivacyAccessedAPICategoryDiskSpace

- NSPrivacyAccessedAPICategoryFileTimestamp

- NSPrivacyAccessedAPICategorySystemBootTime

- NSPrivacyAccessedAPICategoryUserDefaults

### Add an accessed API type key

The NSPrivacyAccessedAPIType key uses the following format:

<key>NSPrivacyAccessedAPIType</key>
<string>NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE</string>

The NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE string represents a privacy accessed API category. For more information, see Select an accessed API category.

To add the NSPrivacyAccessedAPIType key to a privacy accessed API type and reasons dictionary:

1. Select the dictionary in the property list editor.

2. Click the disclosure triangle to the left of the dictionary to reveal it.

3. Click the Add button (+) beside the dictionary to add a new item.

4. In the pop-up menu that appears, choose NSPrivacyAccessedAPIType.

5. Confirm the value is String in the Type column.

6. Select a privacy accessed API category from the pop-up menu in the Value column. For possible values, see Select an accessed API category.

7. Confirm that the value exactly matches the category of required reason API that your app or third-party SDK uses.

### Add an accessed API type reasons key

The NSPrivacyAccessedAPITypeReasons key uses the following format:

<key>NSPrivacyAccessedAPITypeReasons</key>
<array>
    <string>NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE</string>
    ...
</array>

Each NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE string in the array identifies a reason why your app or third-party SDK uses a required reason API. All the values in the array are associated with a NSPrivacyAccessedAPIType key you provide when you create a privacy accessed API type and reasons dictionary.

To add the NSPrivacyAccessedAPITypeReasons key to a privacy accessed API type and reasons dictionary:

1. Select the dictionary in the property list editor.

2. Click the disclosure triangle to the left of the dictionary to reveal it.

3. Confirm the dictionary contains a NSPrivacyAccessedAPIType key with a value as described in Select an accessed API category.

4. Click the Add button (+) beside the dictionary to add a new item.

5. In the pop-up menu that appears, choose NSPrivacyAccessedAPITypeReasons.

6. Confirm the value is Array in the Type column.

7. Click the disclosure triangle to the left of NSPrivacyAccessedAPITypeReasons to reveal it.

8. Click the Add button (+) beside NSPrivacyAccessedAPITypeReasons to add a reason.

9. Choose a reason from the pop-up menu in the Value column. For possible values, see Describing use of required reason API.

10. Confirm that the value exactly matches a reason for the NSPrivacyAccessedAPIType key you use in step 3.

### Add an accessed API type and reasons dictionary

A privacy accessed API type and reasons dictionary includes a category of required reason APIs and a list of related reasons. The dictionary contains exactly two keys: NSPrivacyAccessedAPIType and NSPrivacyAccessedAPITypeReasons. It uses the following format:

<dict>
    <!— Add an accessed API type key. -->
    <key>NSPrivacyAccessedAPIType</key>
    <string>NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE</string>

    <!— Add an accessed API type reasons key. -->
    <key>NSPrivacyAccessedAPITypeReasons</key>
    <array>
        <string>NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE</string>
        ...
    </array>
</dict>

To add a privacy accessed API type and reasons dictionary to the NSPrivacyAccessedAPITypes key in your privacy manifest:

1. Select PrivacyInfo.xcprivacy in the Project navigator.

2. Find the NSPrivacyAccessedAPITypes key in the property list editor.

3. Click the disclosure triangle to the left of NSPrivacyAccessedAPITypes to reveal it.

4. Click the Add button (+) beside NSPrivacyAccessedAPITypes to insert a new item.

5. Confirm the value is Dictionary in the Type column.

6. To add the NSPrivacyAccessedAPIType key to the dictionary, see Add an accessed API type key.

7. To add the NSPrivacyAccessedAPITypeReasons key to the dictionary, see Add an accessed API type reasons key.

### Add the accessed API types key

The NSPrivacyAccessedAPITypes key is an array of privacy accessed API type and reasons dictionaries. For more information, see Add an accessed API type and reasons dictionary. The key uses the following format:

<key>NSPrivacyAccessedAPITypes</key>
<array>
    <dict>
        <key>NSPrivacyAccessedAPIType</key>
        <string>NS_PRIVACY_ACCESSED_API_CATEGORY_VALUE</string>
        <key>NSPrivacyAccessedAPITypeReasons</key>
        <array>
            <string>NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE</string>
            ...
        </array>
    </dict>
    ...
</array>

To add the NSPrivacyAccessedAPITypes key to your privacy manifest:

1. Select PrivacyInfo.xcprivacy in the Project navigator.

2. Click the Add button (+) beside the App Privacy Configuration key in the property list editor.

3. In the pop-up menu that appears, choose NSPrivacyAccessedAPITypes.

4. Confirm the value is Array in the Type column.

5. To add a privacy accessed API type and reasons dictionary to the array, see Add an accessed API type and reasons dictionary.

The following example declares disk space required reason API usage in an app named Sample:

Repeat step 5 for each additional required reason API your app or third-party SDK uses. The example below additionally declares user defaults required reason API usage in Sample:

### Revision History

- 2024-12-17 First published.

## Related Documentation

- TN3181: Debugging an invalid privacy manifest: Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.

- TN3182: Adding privacy tracking keys to your privacy manifest: Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.

- TN3184: Adding data collection details to your privacy manifest: Declare the data your app or third-party SDK collects in a privacy manifest.

=== SOURCE: https://developer.apple.comdoc://com.apple.technotes/documentation/Technotes/tn3184-adding-data-collection-details-to-your-privacy-manifest
# TN3184: Adding data collection details to your privacy manifest

Declare the data your app or third-party SDK collects in a privacy manifest.

### Overview

When you build an app or third-party SDK that collects any data type, perform these steps in your privacy manifest (PrivacyInfo.xcprivacy):

1. Add the NSPrivacyCollectedDataTypes key.

2. For each data type your app or third-party SDK collects, add a dictionary as a value for the NSPrivacyCollectedDataTypes key. The dictionary includes the data type, the data linked to the user and tracking status, and a list of reasons for collecting this data type. For more information, see Add a collected data type and reasons dictionary.

For more information about the privacy manifest and these keys, see Privacy manifest files and Describing data use in privacy manifests.

This document describes how to add the NSPrivacyCollectedDataType, NSPrivacyCollectedDataTypeLinked, NSPrivacyCollectedDataTypeTracking, and NSPrivacyCollectedDataTypePurposes keys to your privacy manifest in Xcode. If you work outside of Xcode, review this document to learn about the expected structure of each key.

[Note]

Note:  Before you start adding the keys to your privacy manifest, enable raw keys and values in Xcode to view the raw keys and hide their human-readable names. Click anywhere in the privacy manifest, then choose Xcode > Editor > Raw Keys and Values. Repeat the process to disable this feature.

### Add a collected data type key

The NSPrivacyCollectedDataType key uses the following format:

<key>NSPrivacyCollectedDataType</key>
<string>NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE</string>

The NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE string specifies the type of data your app or third-party SDK collects. For possible values, see “Report the categories of data your app or third-party SDK collects“ in Describing data use in privacy manifests.

To add the NSPrivacyCollectedDataType key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.

2. Click the disclosure triangle to the left of the dictionary to reveal it.

3. Click the Add button (+) beside the dictionary to add a new item.

4. In the pop-up menu, choose NSPrivacyCollectedDataType.

5. In the Type column, confirm that the value is String.

6. Select a data type from the pop-up menu in the Value column. For possible values, see “Report the categories of data your app or third-party SDK collects“ in Describing data use in privacy manifests.

7. Confirm that the value exactly matches the type of data your app or third-party SDK collects.

### Add a collected data type linked key

The NSPrivacyCollectedDataTypeLinked key uses the following format:

<key>NSPrivacyCollectedDataTypeLinked</key>
<!-- Use <true/> if your app or third-party SDK links this data type to the user’s identity; otherwise,
     use <false/>. -->
<true/>

To add the NSPrivacyCollectedDataTypeLinked key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.

2. Click the disclosure triangle to the left of the dictionary to reveal it.

3. Click the Add button (+) beside the dictionary to add a new item.

4. In the pop-up menu, choose NSPrivacyCollectedDataTypeLinked.

5. In the Type column, confirm that the value is Boolean.

6. Select YES from the pop-up menu in the Value column if your app or third-party SDK links this data type to the user’s identity; otherwise, select NO.

### Add a collected data type tracking key

The NSPrivacyCollectedDataTypeTracking key uses the following format:

<key>NSPrivacyCollectedDataTypeTracking</key>
<!-- Use <true/> if your app or third-party SDK uses this data type to track; otherwise, use <false/>. -->
<true/>

To add the NSPrivacyCollectedDataTypeTracking key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.

2. Click the disclosure triangle to the left of the dictionary to reveal it.

3. Click the Add button (+) beside the dictionary to add a new item.

4. In the pop-up menu, choose NSPrivacyCollectedDataTypeTracking.

5. In the Type column, confirm that the value is Boolean.

6. Select YES from the pop-up menu in the Value column if your app or third-party SDK uses this data type to track; otherwise, select NO.

### Add a collected data type purposes key

The NSPrivacyCollectedDataTypePurposes key uses the following format:

<key>NSPrivacyCollectedDataTypePurposes</key>
<array>
    <string>NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE</string>
    ...
</array>

Each NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE string in the array identifies a reason why your app or third-party SDK collects a data type. For possible values, see “Report the reasons your app or third-party SDK collects data” in Describing data use in privacy manifests.

To add the NSPrivacyCollectedDataTypePurposes key to a privacy collected data type and reasons dictionary in your privacy manifest:

1. Select the dictionary in the property list editor.

2. Click the disclosure triangle to the left of the dictionary to reveal it.

3. Confirm the dictionary contains a NSPrivacyCollectedDataType key with a value as described in Add a collected data type key.

4. Click the Add button (+) beside the dictionary to add a new item.

5. In the pop-up menu, choose NSPrivacyCollectedDataTypePurposes.

6. In the Type column, confirm that the value is Array.

7. Click the disclosure triangle to the left of NSPrivacyCollectedDataTypePurposes to reveal it.

8. Click the Add button (+) beside NSPrivacyCollectedDataTypePurposes to add a reason.

9. Choose a reason from the pop-up menu in the Value column. For possible values, see “Report the reasons your app or third-party SDK collects data” in Describing data use in privacy manifests.

Repeat the last two steps for each reason your app or third-party SDK collects this data type.

### Add a collected data type and reasons dictionary

A privacy collected data type and reasons dictionary includes a data type, a data linked to the user status, a tracking status, and a list of reasons for collecting this data type. The dictionary contains exactly four keys: NSPrivacyCollectedDataType, NSPrivacyCollectedDataTypeLinked, NSPrivacyCollectedDataTypeTracking, and NSPrivacyCollectedDataTypePurposes. It uses the following format:

<dict>
    <!-- Add a privacy collected data type key. -->
    <key>NSPrivacyCollectedDataType</key>
    <string>NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE</string>

    <!-- Add a privacy collected data type linked key. -->
    <key>NSPrivacyCollectedDataTypeLinked</key>
    <false/>

    <!-- Add a privacy collected data type tracking key. -->
    <key>NSPrivacyCollectedDataTypeTracking</key>
    <false/>

    <!-- Add a privacy collected data type purposes key. -->
    <key>NSPrivacyCollectedDataTypePurposes</key>
    <array>
        <string>NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE</string>
        ...
    </array>
</dict>

To add a privacy collected data type and reasons dictionary to the NSPrivacyCollectedDataTypes key in your privacy manifest:

1. Select PrivacyInfo.xcprivacy in the Project navigator in Xcode.

2. Find the NSPrivacyCollectedDataTypes key in the property list editor.

3. Click the disclosure triangle to the left of NSPrivacyCollectedDataTypes to reveal it.

4. Click the Add button (+) beside NSPrivacyCollectedDataTypes to insert a new item.

5. Confirm the value is Dictionary in the Type column.

6. Click the disclosure triangle to the left of the dictionary to reveal it.

7. To add the NSPrivacyCollectedDataType key to the dictionary, see Add a collected data type key.

8. To add the NSPrivacyCollectedDataTypeLinked key to the dictionary, see Add a collected data type linked key.

9. To add the NSPrivacyCollectedDataTypeTracking key to the dictionary, see Add a collected data type tracking key.

10. To add the NSPrivacyCollectedDataTypePurposes key to the dictionary, see Add a collected data type purposes key.

### Add the collected data types key

The NSPrivacyCollectedDataTypes key is an array of privacy collected data type and reasons dictionaries. For more information, see Add a collected data type and reasons dictionary. The key uses the following format:

<key>NSPrivacyCollectedDataTypes</key>
<array>
    <dict>
        <!-- Add a privacy collected data type key. -->
        <key>NSPrivacyCollectedDataType</key>
        <string>NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE</string>

        <!-- Add a privacy collected data type linked key. -->
        <key>NSPrivacyCollectedDataTypeLinked</key>
        <false/>

        <!-- Add a privacy collected data type tracking key. -->
        <key>NSPrivacyCollectedDataTypeTracking</key>
        <false/>

        <!-- Add a privacy collected data type purposes key. -->
        <key>NSPrivacyCollectedDataTypePurposes</key>
        <array>
            <string>NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE</string>
            ...
        </array>
    </dict>
    ...
</array>

To add the NSPrivacyCollectedDataTypes key to your privacy manifest:

1. Select PrivacyInfo.xcprivacy in the Project navigator.

2. Click the Add button (+) beside the App Privacy Configuration key in the property list editor.

3. In the pop-up menu that appears, choose NSPrivacyCollectedDataTypes.

4. Confirm the value is Array in the Type column.

5. To add a privacy collected data type and reasons dictionary, see Add a collected data type and reasons dictionary.

The following example declares the contacts information collected from the user in an app named Sample:

Repeat step 5 for each additional data type your app or third-party SDK collects. In the following example, Sample additionally collects user ID information from the user:

### Revision History

- 2024-12-17 First published.

## Related Documentation

- TN3181: Debugging an invalid privacy manifest: Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.

- TN3182: Adding privacy tracking keys to your privacy manifest: Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.

- TN3183: Adding required reason API entries to your privacy manifest: Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.

=== SOURCE: https://developer.apple.comdoc://com.apple.Xcode/documentation/Xcode/verifying-the-origin-of-your-xcframeworks
# Verifying the origin of your XCFrameworks

Discover who signed a framework, and take action when that changes.

### Overview

When you add third-party binary SDKs to your target as XCFrameworks, the behaviors of those packages become part of the behavior of your product. An attacker who’s able to inject a compromised version of the SDK into your project could change your app’s behavior and cause security and privacy issues for your developers, testers, and people who use your product.

Use Xcode to inspect the information in the code signature embedded in an XCFramework when you add it to your project. The build system fails with an error if the code signature’s subsequently removed, becomes invalid, or a different developer signs an update to the framework. If any of these happens, take action to resolve the issue.

#### Inspect a dependency’s code signing identity

In Xcode, select your dependency’s XCFramework folder in the Project navigator. The File inspector shows you the XCFramework’s code signing status. If the framework is signed with an Apple Developer certificate, the inspector also shows which team signed the framework.



If the XCFramework is signed by a self-issued code signing identity, the inspector shows the SHA-256 fingerprint of the certificate in the framework’s code signature. Verify that the certificate fingerprint matches the value you expect.



#### Diagnose build failures caused by code signature changes

An XCFramework’s code signature can change for legitimate reasons, like:

- the provider of a third-party SDK transfers ownership of the SDK to another organization, who release a version that’s signed with the new organization’s Team ID.

- you switch from a vendor-supplied distribution of an XCFramework to a version that you build and sign yourself.

A changed code signature can also indicate that the XCFramework has been tampered with, or another actor has injected their own code into your system, pretending it’s a version of the XCFramework.

If the code signature for an XCFramework changes, Xcode shows the changed code signature information in the File inspector.



If you attempt to build the software without resolving the changed code signature information, the build system produces an error. Work with the XCFramework’s provider to determine whether the change is expected. If the change is expected, follow these steps:

1. Switch to the Issues navigator.

2. Select the error that says “[XCFramework name] is not signed with the expected identity and may have been compromised”.

3. In the dialog that appears, click Accept Change.



If your team and the SDK provider can’t account for the change to the XCFramework’s code signature, restore a version of the framework with the expected code signature, or remove the framework from your project. To restore the framework to a version with the expected code signature, do the following:

1. In the dialog, click Move to Trash.

2. Switch to or open a new Finder window.

3. Drag a replacement copy of the XCFramework from a trusted source to the Finder folder that contained the copy you deleted.

4. Switch to Xcode, and verify that the XCFramework’s signature is valid in the File inspector.

[Warning]

Warning: If you encounter an unexpected code signature change in an XCFramework, it’s possible that an attacker is exploiting a security vulnerability in your infrastructure. Audit the origins for your XCFrameworks to ensure you obtained them from official sources. You also need to audit your software development and deployment environment carefully, even if you revert the XCFramework to a correctly-signed version.

Xcode also warns you if the XCFramework is signed with an expired or revoked code signing identity, even if the identity hasn’t changed since you added the XCFramework to your project. If this happens, work with the SDK provider to obtain a new version of the framework that’s signed by a valid code signing identity.

#### Diagnose failures caused when a code signature is removed

If someone removes the code signature for an XCFramework, Xcode shows the change in the File inspector.



The build system fails with an error if you attempt to build the software without resolving the removed code signature. Determine why the code signature is missing from the XCFramework. If you no longer expect the XCFramework to be signed, follow these steps:

1. Switch to the Issues navigator.

2. Select the error that says “[XCFramework name] is not signed with the expected identity and may have been compromised”.

3. In the dialog that appears, click Accept Change.



## Security and privacy

- Enabling enhanced security for your app: Detect out-of-bounds memory access, use of freed memory, and other potential vulnerabilities.

- Creating enhanced security helper extensions: Reduce opportunities for an attacker to target your app through its extensions.

- Adopting type-aware memory allocation: Reduce the opportunities to treat pointers as data in your code.

- Conforming to Mach IPC security restrictions: Avoid crashes and potentially insecure situations associated with Mach messages.

=== SOURCE: https://developer.apple.com/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyAccessedAPITypes/NSPrivacyAccessedAPIType (Possible Values)

# NSPrivacyAccessedAPIType — Possible Values

## NSPrivacyAccessedAPICategoryFileTimestamp

The following APIs for accessing file timestamps require reasons for use.

- creationDate

- modificationDate

- fileModificationDate

- contentModificationDateKey

- creationDateKey

- getattrlist(_:_:_:_:_:)

- getattrlistbulk(_:_:_:_:_:)

- fgetattrlist(_:_:_:_:_:)

- stat

- fstat(_:_:)

- fstatat(_:_:_:_:)

- lstat(_:_:)

- getattrlistat(_:_:_:_:_:_:)

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from this list.

DDA9.1: Declare this reason to display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device.

C617.1: Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container.

3B52.1: Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller.

0A2A.1: Declare this reason if your third-party SDK is providing a wrapper function around file timestamp API(s) for the app to use, and you only access the file timestamp APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s). Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

## NSPrivacyAccessedAPICategorySystemBootTime

The following APIs for accessing the system boot time require reasons for use.

- systemUptime

- mach_absolute_time()

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

35F9.1: Declare this reason to access the system boot time in order to measure the amount of time that has elapsed between events that occurred within the app or to perform calculations to enable timers. Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception for information about the amount of time that has elapsed between events that occurred within the app, which may be sent off-device.

8FFB.1: Declare this reason to access the system boot time to calculate absolute timestamps for events that occurred within your app, such as events related to the UIKit or AVFAudio frameworks. Absolute timestamps for events that occurred within your app may be sent off-device. System boot time accessed for this reason, or any other information derived from system boot time, may not be sent off-device.

3D61.1: Declare this reason to include system boot time information in an optional bug report that the person using the device chooses to submit. The system boot time information must be prominently displayed to the person as part of the report. Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including system boot time information, and only for the purpose of investigating or responding to the bug report.

## NSPrivacyAccessedAPICategoryDiskSpace

The following APIs for accessing the available disk space require reasons for use.

- volumeAvailableCapacityKey

- volumeAvailableCapacityForImportantUsageKey

- volumeAvailableCapacityForOpportunisticUsageKey

- volumeTotalCapacityKey

- systemFreeSize

- systemSize

- statfs(_:_:)

- statvfs(_:_:)

- fstatfs(_:_:)

- fstatvfs(_:_:)

- getattrlist(_:_:_:_:_:)

- fgetattrlist(_:_:_:_:_:)

- getattrlistat(_:_:_:_:_:_:)

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

85F4.1: Declare this reason to display disk space information to the person using the device. Disk space may be displayed in units of information (such as bytes) or units of time combined with a media type (such as minutes of HD video). Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to send disk space information over the local network to another device operated by the same person only for the purpose of displaying disk space information on that device; this exception only applies if the user has provided explicit permission to send disk space information, and the information may not be sent over the Internet.

E174.1: Declare this reason to check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users. Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to avoid downloading files from a server when disk space is insufficient.

7D9E.1: Declare this reason to include disk space information in an optional bug report that the person using the device chooses to submit. The disk space information must be prominently displayed to the person as part of the report. Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including disk space information, and only for the purpose of investigating or responding to the bug report.

B728.1: Declare this reason if your app is a health research app, and you access this API category to detect and inform research participants about low disk space impacting the research data collection. Your app must comply with App Store Review Guideline §5.1.3. Your app must not offer any functionality other than providing information about and allowing people to participate in health research.

## NSPrivacyAccessedAPICategoryActiveKeyboards

The following API for accessing the list of active keyboards requires reasons for use.

- activeInputModes

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

3EC4.1: Declare this reason if your app is a custom keyboard app, and you access this API category to determine the keyboards that are active on the device. Providing a systemwide custom keyboard to the user must be the primary functionality of the app. Information accessed for this reason, or any derived information, may not be sent off-device.

54BD.1: Declare this reason to access active keyboard information to present the correct customized user interface to the person using the device. The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users. Information accessed for this reason, or any derived information, may not be sent off-device.

## NSPrivacyAccessedAPICategoryUserDefaults

The following API for accessing user defaults requires reasons for use.

- UserDefaults

In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

CA92.1: Declare this reason to access user defaults to read and write information that is only accessible to the app itself. This reason does not permit reading information that was written by other apps or the system, or writing information that can be accessed by other apps.

1C8F.1: Declare this reason to access user defaults to read and write information that is only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself. This reason does not permit reading information that was written by apps, app extensions, or App Clips outside the same App Group or by the system. Your app is not responsible if the system provides information from the global domain because a key is not present in your requested domain while your app is attempting to read information that apps, app extensions, or App Clips in your app’s App Group write. This reason also does not permit writing information that can be accessed by apps, app extensions, or App Clips outside the same App Group.

C56D.1: Declare this reason if your third-party SDK is providing a wrapper function around user defaults API(s) for the app to use, and you only access the user defaults APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s). Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

AC6B.1: Declare this reason to access user defaults to read the com.apple.configuration.managed key to retrieve the managed app configuration set by MDM, or to set the com.apple.feedback.managed key to store feedback information to be queried over MDM, as described in the Apple Mobile Device Management Protocol Reference documentation.

=== SOURCE: https://developer.apple.com/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyAccessedAPITypes/NSPrivacyAccessedAPITypeReasons (Possible Values)

# NSPrivacyAccessedAPITypeReasons — Possible Values

## DDA9.1

Declare this reason to display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device.

## C617.1

Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container.

## 3B52.1

Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller.

## 0A2A.1

Declare this reason if your third-party SDK is providing a wrapper function around file timestamp API(s) for the app to use, and you only access the file timestamp APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s).

Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

## 35F9.1

Declare this reason to access the system boot time in order to measure the amount of time that has elapsed between events that occurred within the app or to perform calculations to enable timers.

Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception for information about the amount of time that has elapsed between events that occurred within the app, which may be sent off-device.

## 8FFB.1

Declare this reason to access the system boot time to calculate absolute timestamps for events that occurred within your app, such as events related to the UIKit or AVFAudio frameworks.

Absolute timestamps for events that occurred within your app may be sent off-device. System boot time accessed for this reason, or any other information derived from system boot time, may not be sent off-device.

## 3D61.1

Declare this reason to include system boot time information in an optional bug report that the person using the device chooses to submit. The system boot time information must be prominently displayed to the person as part of the report.

## 85F4.1

Declare this reason to display disk space information to the person using the device. Disk space may be displayed in units of information (such as bytes) or units of time combined with a media type (such as minutes of HD video).

Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to send disk space information over the local network to another device operated by the same person only for the purpose of displaying disk space information on that device; this exception only applies if the user has provided explicit permission to send disk space information, and the information may not be sent over the Internet.

## E174.1

Declare this reason to check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users.

Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to avoid downloading files from a server when disk space is insufficient.

## 7D9E.1

Declare this reason to include disk space information in an optional bug report that the person using the device chooses to submit. The disk space information must be prominently displayed to the person as part of the report.

Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including disk space information, and only for the purpose of investigating or responding to the bug report.

## B728.1

Declare this reason if your app is a health research app, and you access this API category to detect and inform research participants about low disk space impacting the research data collection.

Your app must comply with App Store Review Guideline §5.1.3. Your app must not offer any functionality other than providing information about and allowing people to participate in health research.

## 3EC4.1

Declare this reason if your app is a custom keyboard app, and you access this API category to determine the keyboards that are active on the device. Providing a systemwide custom keyboard to the user must be the primary functionality of the app.

Information accessed for this reason, or any derived information, may not be sent off-device.

## 54BD.1

Declare this reason to access active keyboard information to present the correct customized user interface to the person using the device. The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users.

Information accessed for this reason, or any derived information, may not be sent off-device.

## CA92.1

Declare this reason to access user defaults to read and write information that is only accessible to the app itself.

This reason does not permit reading information that was written by other apps or the system, or writing information that can be accessed by other apps.

## 1C8F.1

Declare this reason to access user defaults to read and write information that is only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself.

This reason does not permit reading information that was written by apps, app extensions, or App Clips outside the same App Group or by the system. Your app is not responsible if the system provides information from the global domain because a key is not present in your requested domain while your app is attempting to read information that apps, app extensions, or App Clips in your app’s App Group write.

This reason also does not permit writing information that can be accessed by apps, app extensions, or App Clips outside the same App Group.

## C56D.1

Declare this reason if your third-party SDK is providing a wrapper function around user defaults API(s) for the app to use, and you only access the user defaults APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s).

Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK.

## AC6B.1

Declare this reason to access user defaults to read the com.apple.configuration.managed key to retrieve the managed app configuration set by MDM, or to set the com.apple.feedback.managed key to store feedback information to be queried over MDM, as described in the Apple Mobile Device Management Protocol Reference documentation.

=== SOURCE: https://developer.apple.com/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyCollectedDataTypes/NSPrivacyCollectedDataType (Possible Values)

# NSPrivacyCollectedDataType — Possible Values

## NSPrivacyCollectedDataTypeName

Name, such as first or last name.

## NSPrivacyCollectedDataTypeEmailAddress

Email address, including but not limited to a hashed email address.

## NSPrivacyCollectedDataTypePhoneNumber

Phone number, including but not limited to a hashed phone number.

## NSPrivacyCollectedDataTypePhysicalAddress

Physical address, such as home address, physical address, or mailing address.

## NSPrivacyCollectedDataTypeOtherUserContactInfo

Other user contact info; any other information that can be used to contact the user outside the app.

## NSPrivacyCollectedDataTypeHealth

Health and medical data, including but not limited to data from the Clinical Health Records API, HealthKit API, MovementDisorderAPIs, or health-related human subject research or any other user provided health or medical data.

## NSPrivacyCollectedDataTypeFitness

Fitness and exercise data, including but not limited to the Motion and Fitness API.

## NSPrivacyCollectedDataTypePaymentInfo

Payment info; such as form of payment, payment card number, or bank account number. If your app uses a payment service, the payment information is entered outside your app, and you as the developer never have access to the payment information, it is not collected and does not need to be disclosed.

## NSPrivacyCollectedDataTypeCreditInfo

Credit info, such as credit score.

## NSPrivacyCollectedDataTypeOtherFinancialInfo

Other financial info; such as salary, income, assets, debts, or any other financial information.

## NSPrivacyCollectedDataTypePreciseLocation

Precise location; information that describes the location of a user or device with the same or greater resolution as a latitude and longitude with three or more decimal places.

## NSPrivacyCollectedDataTypeCoarseLocation

Coarse location; information that describes the location of a user or device with lower resolution than a latitude and longitude with three or more decimal places, such as Approximate Location Services.

## NSPrivacyCollectedDataTypeSensitiveInfo

Sensitive information; such as racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data.

## NSPrivacyCollectedDataTypeContacts

Contacts; such as a list of contacts in the user’s phone, address book, or social graph.

## NSPrivacyCollectedDataTypeEmailsOrTextMessages

Emails or text messages; including subject line, sender, recipients, and contents of the email or message.

## NSPrivacyCollectedDataTypePhotosorVideos

The user’s photos or videos.

## NSPrivacyCollectedDataTypeAudioData

The user’s voice or sound recordings.

## NSPrivacyCollectedDataTypeGameplayContent

Gameplay content; such as saved games, multiplayer matching or gameplay logic, or user-generated content in-game.

## NSPrivacyCollectedDataTypeCustomerSupport

Data generated by the user during a customer support request.

## NSPrivacyCollectedDataTypeOtherUserContent

Any other user-generated content.

## NSPrivacyCollectedDataTypeBrowsingHistory

Browsing history; information about content the user has viewed that is not part of the app, such as websites.

## NSPrivacyCollectedDataTypeSearchHistory

Information about searches performed in the app.

## NSPrivacyCollectedDataTypeUserID

User ID; such as screen name, handle, account ID, assigned user ID, customer number, or other user- or account-level ID that can be used to identify a particular user or account.

## NSPrivacyCollectedDataTypeDeviceID

Device ID; such as the device’s advertising identifier, or other device-level ID.

## NSPrivacyCollectedDataTypePurchaseHistory

An account’s or individual’s purchases or purchase tendencies.

## NSPrivacyCollectedDataTypeProductInteraction

Product interaction; such as app launches, taps, clicks, scrolling information, music listening data, video views, saved place in a game, video, or song, or other information about how the user interacts with the app.

## NSPrivacyCollectedDataTypeAdvertisingData

Advertising data; such as information about the advertisements the user has seen.

## NSPrivacyCollectedDataTypeOtherUsageData

Any other data about user activity in the app.

## NSPrivacyCollectedDataTypeCrashData

Crash data, such as crash logs.

## NSPrivacyCollectedDataTypePerformanceData

Performance data, such as launch time, freeze rate, or energy use.

## NSPrivacyCollectedDataTypeOtherDiagnosticData

Any other data collected for the purposes of measuring technical diagnostics related to the app.

## NSPrivacyCollectedDataTypeEnvironmentScanning

Environment scanning; such as mesh, planes, scene classification, and/or image detection of the user’s surroundings.

## NSPrivacyCollectedDataTypeHands

The user’s hand structure and hand movements.

## NSPrivacyCollectedDataTypeHead

The user’s head movement.

## NSPrivacyCollectedDataTypeOtherDataTypes

Any other data types not mentioned.

=== SOURCE: https://developer.apple.com/documentation/BundleResources/App-Privacy-Configuration/NSPrivacyCollectedDataTypes/NSPrivacyCollectedDataTypePurposes (Possible Values)

# NSPrivacyCollectedDataTypePurposes — Possible Values

## NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising

Third-party advertising; such as displaying third-party ads in your app, or sharing data with entities who display third-party ads.

## NSPrivacyCollectedDataTypePurposeDeveloperAdvertising

Developer’s advertising or marketing; such as displaying first-party ads in your app, sending marketing communications directly to your users, or sharing data with entities who will display your ads.

## NSPrivacyCollectedDataTypePurposeAnalytics

Analytics — using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics.

## NSPrivacyCollectedDataTypePurposeProductPersonalization

Product personalization — customizing what the user sees, such as a list of recommended products, posts, or suggestions.

## NSPrivacyCollectedDataTypePurposeAppFunctionality

App functionality; such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support.

## NSPrivacyCollectedDataTypePurposeOther

Any other purposes not listed.

