# Privacy Manifest Files (PrivacyInfo.xcprivacy) — Keys, Required Reason APIs, Collected Data Types, Third-Party SDK Requirements
Source: https://developer.apple.com/documentation/bundleresources/privacy-manifest-files , https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api , https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests , https://developer.apple.com/support/third-party-SDK-requirements/ (and the child pages listed under "## Sources")  
Retrieved: 2026-10-30

Note: Notes for the skill runner
Note: Apple documentation pages were read from their DocC JSON (`https://developer.apple.com/tutorials/data/documentation/<path>.json`). Links inside Apple's text are reproduced as their visible link text only; inline code (`codeVoice`) is shown in backticks.
Note: The "Code search patterns" columns in the required-reason-API tables are NOT Apple text. They are search patterns built only from the symbol names Apple lists on the category page plus the Objective-C names shown on each symbol's own Apple documentation page (retrieved the same day). Every hit must be confirmed by reading the surrounding code; plain-word names such as `creationDate`, `stat` or `systemSize` produce false positives.
Note: Binary SDKs (XCFrameworks, `.a`, `.framework`) cannot be grepped as source. For those, check that the SDK ships its own `PrivacyInfo.xcprivacy` (see PRIV.B / PRIV.O).

---

## PRIV.A Privacy manifest files — overview and top-level keys

**Source text (verbatim):**
> Describe the data your app or third-party SDK collects and the required reasons APIs it uses.
>
> Apps and third-party SDKs — distributed as XCFrameworks, Swift packages, or Xcode projects — can contain a privacy manifest file, named `PrivacyInfo.xcprivacy`. The privacy manifest is a property list that records the following information:
> - The types of data collected by your app or third-party SDK. You need to provide this information for your app or third-party SDK on all platforms.
> - The required reasons APIs your app or third-party SDK uses. You need to provide this information for your app or third-party SDK on iOS, iPadOS, tvOS, visionOS, and watchOS.
>
> For each type of data your app or third-party SDK collects and category of required reasons API it uses, the app or third-party SDK needs to record the reasons in its bundled privacy manifest file.
>
> Important: You need to include a privacy manifest file in your third-party SDK if it’s listed in “SDKs that require a privacy manifest and signature,” in Upcoming third-party SDK requirements. Otherwise, include a privacy manifest file in your third-party SDK if it uses a required reasons API, collects data about the person using apps that include the third-party SDK, enables the app to collect data about people using the app, or contacts tracking domains. Providing a privacy manifest file helps app developers understand the API use and data-collection practices of your third-party SDK.
>
> For information on editing the privacy manifest file, see Editing property list files.
>
> **Create a privacy manifest**
>
> To add the privacy manifest to your app or third-party SDK in Xcode, follow these steps:
> - Choose File > New File.
> - Scroll down to the Resource section, and select App Privacy File type.
> - Click Next.
> - Check your app or third-party SDK’s target in the Targets list.
> - Click Create.
>
> By default, the file is named `PrivacyInfo.xcprivacy`; this is the required file name for bundled privacy manifests.
>
> Note: You need to add the privacy manifest file to your target’s resources for Xcode to use it when you generate a privacy report. If you distribute your third-party SDK as a static library, use the support for static frameworks in Xcode 15 or later to bundle resources, including the privacy manifest file. Create a framework target in Xcode that builds your product, set its Mach-O type build setting to “Static Library,” and add the privacy manifest file to your target’s bundle resources along with any other resources, for example, image files.
>
> At the top level of this property list file, add the following keys to the dictionary:
> - NSPrivacyTracking: A Boolean that indicates whether your app or third-party SDK uses data for tracking as defined under the App Tracking Transparency framework. When set to `true` you need to provide a list of internet domains in `NSPrivacyTrackingDomains`. For more information, see User Privacy and Data Use.
> - NSPrivacyTrackingDomains: An array of strings that lists the internet domains your app or third-party SDK connects to that engage in tracking. If the user has not granted tracking permission through the App Tracking Transparency framework, network requests to these domains fail and your app receives an error. To provide a list of internet domains in `NSPrivacyTrackingDomains`, set `NSPrivacyTracking` to `true`.
> - NSPrivacyCollectedDataTypes: An array of dictionaries that describes the data types your app or third-party SDK collects. For information on the keys and values to use in the dictionaries, see Describing data use in privacy manifests.
> - NSPrivacyAccessedAPITypes: An array of dictionaries that describe the API types your app or third-party SDK accesses that have been designated as APIs that require reasons to access. For information on the keys and values to use in the dictionaries, see Describing use of required reason API.

Top-level keys of the App Privacy Configuration (root dictionary), from https://developer.apple.com/documentation/bundleresources/app-privacy-configuration and each key's page:

| Key | Xcode display name (ideTitle) | Type | Abstract (verbatim) |
|---|---|---|---|
| `NSPrivacyTracking` | Privacy Tracking Enabled | Boolean (default `false`) | A Boolean value that indicates whether your app or third-party SDK uses data for tracking. |
| `NSPrivacyTrackingDomains` | Privacy Tracking Domains | Array of String | A list of the internet domains your app or third-party SDK uses for tracking. |
| `NSPrivacyCollectedDataTypes` | Privacy Nutrition Label Types | Array of Dictionary | A list of dictionaries that report the categories of private data your app or third-party SDK collects. |
| `NSPrivacyAccessedAPITypes` | Privacy Accessed API Types | Array of Dictionary | A list of dictionaries that report the privacy accessed API your app or third-party SDK uses. |

**Applies to:** All apps and third-party SDKs that contain a privacy manifest; the required-reasons portion applies on iOS, iPadOS, tvOS, visionOS, and watchOS.

- **[PRIV-01]** Does every privacy manifest in the project use the exact file name `PrivacyInfo.xcprivacy`?
  - quote: "By default, the file is named `PrivacyInfo.xcprivacy`; this is the required file name for bundled privacy manifests."
  - surface: code
  - verify: `find . -iname '*.xcprivacy' -not -path '*/DerivedData/*'`; flag any file whose name is not exactly `PrivacyInfo.xcprivacy` (case-sensitive).
  - fix: Rename the file to `PrivacyInfo.xcprivacy` (and update the reference in `project.pbxproj` / `Package.swift`).
- **[PRIV-02]** Is the app’s `PrivacyInfo.xcprivacy` a member of the app target’s resources (Copy Bundle Resources)?
  - quote: "You need to add the privacy manifest file to your target’s resources for Xcode to use it when you generate a privacy report."
  - surface: code
  - verify: In `*.xcodeproj/project.pbxproj`, confirm a `PBXBuildFile` for `PrivacyInfo.xcprivacy` appears in the app target’s `PBXResourcesBuildPhase` (or, for synchronized folders, that the file is inside the target’s synchronized root and not excluded). After a build, confirm `PrivacyInfo.xcprivacy` exists inside the built `.app`.
  - fix: Add the file to the app target’s Target Membership / Copy Bundle Resources build phase.
- **[PRIV-03]** For every type of data the app collects and every required-reason API category it uses, is there a matching entry in the app’s bundled privacy manifest?
  - quote: "For each type of data your app or third-party SDK collects and category of required reasons API it uses, the app or third-party SDK needs to record the reasons in its bundled privacy manifest file."
  - surface: code
  - verify: Cross-check the results of PRIV.E (collected data) and PRIV.G–PRIV.K (required reason API scans) against the `NSPrivacyCollectedDataTypes` and `NSPrivacyAccessedAPITypes` arrays of the app’s `PrivacyInfo.xcprivacy`.
  - fix: Add the missing dictionaries (see PRIV.E, PRIV.F, PRIV.M, PRIV.N for the structure).
- **[PRIV-04]** If the app collects data, does a privacy manifest describe the collected data types on every platform the app ships on (including macOS), not only on iOS?
  - quote: "You need to provide this information for your app or third-party SDK on all platforms."
  - surface: code
  - verify: List every app target/platform in the project (`SUPPORTED_PLATFORMS`, `SDKROOT`); for each shipped bundle (iOS, macOS, tvOS, visionOS, watchOS) of an app that collects data, confirm it contains a `PrivacyInfo.xcprivacy` with the `NSPrivacyCollectedDataTypes` that apply to it.
  - fix: Add a `PrivacyInfo.xcprivacy` declaring the collected data types to each such platform target’s resources.
- **[PRIV-05]** If the project contains an SDK the developer distributes to other apps as a third-party SDK (framework target or Swift package), and that SDK uses a required reasons API, collects data about the person using apps that include it, enables the app to collect data, or contacts tracking domains, does that SDK include its own privacy manifest?
  - quote: "include a privacy manifest file in your third-party SDK if it uses a required reasons API, collects data about the person using apps that include the third-party SDK, enables the app to collect data about people using the app, or contacts tracking domains"
  - surface: code
  - verify: Ask the developer which framework targets / local Swift packages they distribute as SDKs to other apps; for each, run the required-reason scans (PRIV.G–PRIV.K) and the data-collection review against that target only; if any hit, confirm a `PrivacyInfo.xcprivacy` is in that target’s resources.
  - fix: Add a `PrivacyInfo.xcprivacy` to that framework target or package (see PRIV.B for location).
- **[PRIV-06]** If the developer distributes a third-party SDK as a static library, is its privacy manifest bundled using a static framework target (Mach-O type “Static Library”), since a bare `.a` doesn’t support resources?
  - quote: "If you distribute your third-party SDK as a static library, use the support for static frameworks in Xcode 15 or later to bundle resources, including the privacy manifest file."
  - surface: code
  - verify: `find . -name '*.a' -not -path '*/DerivedData/*'`; for each static library the developer distributes as an SDK, check whether a static framework target exists with `MACH_O_TYPE = staticlib` and `PrivacyInfo.xcprivacy` in its resources.
  - fix: Create a framework target with Mach-O type “Static Library” and add `PrivacyInfo.xcprivacy` to its bundle resources.

---

## PRIV.B Adding a privacy manifest to your app or third-party SDK — validity and bundle location

**Source text (verbatim):**
> Report the data you collect and the required reasons API you use in your app or third-party SDK.
>
> A privacy manifest is a property list file (`PrivacyInfo.xcprivacy`) that you add to your target’s resources. The privacy manifest describes the privacy practices of an app or third-party SDK. To add a privacy manifest to your app or third-party SDK using Xcode, see Privacy manifest files. All privacy manifest files in your app must be valid, containing only the expected keys and values. For more information, see “Describe the data your app or third-party SDK collects,” in Describing data use in privacy manifests.
>
> Important: App Store Connect rejects app submissions that include invalid privacy manifest files. If you upload an app to App Store Connect that contains privacy manifest files with unexpected keys or values, you receive an email that includes the name and path of the invalid files in your app bundle. If an invalid file comes from a third-party SDK, contact its developer for an updated version of the SDK that includes a valid privacy manifest. To troubleshoot invalid privacy manifests, see TN3181: Debugging an invalid privacy manifest. Starting February 12, 2025, apps you submit for review in App Store Connect must contain a valid privacy manifest file for a certain number of commonly used third-party SDKs. For more information, see Upcoming third-party SDK requirements.
>
> When you add a privacy manifest to the target that builds your app or third-party SDK in Xcode, Xcode automatically places this file in the correct location based on the type of product and its target platform. If you don’t use Xcode to build your product, use the information below to place the privacy manifest in the correct location. Even if you use Xcode, you might find this information useful to verify the privacy manifest location in your product.
>
> **Add a privacy manifest to your app**
>
> If you build an iOS, iPadOS, tvOS, visionOS, or watchOS app, place the privacy manifest at the root of your app’s bundle. The example below shows the bundle structure of an iOS app called `Sample`, which lists `PrivacyInfo.xcprivacy` at `Sample.app/PrivacyInfo.xcprivacy`:
> ```
> Sample.app/
>     Info.plist
>     Sample
>     PrivacyInfo.xcprivacy
>     ...
> ```
> For macOS and Mac Catalyst apps, place the privacy manifest file in `Contents/Resources/` in your app’s bundle. The following example shows the bundle structure of a macOS app called `MacSample`, which lists `PrivacyInfo.xcprivacy` at `MacSample.app/Contents/Resources/PrivacyInfo.xcprivacy`:
> ```
> MacSample.app/
>     Contents/
>         Info.plist
>         MacOS/
>             MacSample
>         Resources/
>             PrivacyInfo.xcprivacy
>         ...
> ```
>
> **Add a privacy manifest to your framework**
>
> The location where you place the privacy manifest in your framework depends on the platform. For iOS, iPadOS, tvOS, visionOS, or watchOS frameworks, place the privacy manifest at the root of your framework’s bundle. The example below shows the layout of an iOS framework called `SampleFramework`, which lists `PrivacyInfo.xcprivacy` at `SampleFramework.framework/PrivacyInfo.xcprivacy`:
> ```
> SampleFramework.framework/
>     Info.plist
>     SampleFramework
>     PrivacyInfo.xcprivacy
>     ...
> ```
> For macOS and Mac Catalyst frameworks, place the privacy manifest file in `Versions/A/Resources/` in your framework’s bundle. The following example shows the layout of a macOS framework named `MacSampleFramework` that supports a single version (`A)`and includes a privacy manifest file. Its bundle structure lists `PrivacyInfo.xcprivacy` at `MacSampleFramework.framework/Versions/A/Resources/PrivacyInfo.xcprivacy`:
> ```
> MacSampleFramework.framework/
>     MacSampleFramework -> Versions/Current/MacSampleFramework
>     Resources -> Versions/Current/Resources
>     Versions/
>         Current -> A
>         A/
>             MacSampleFramework
>             Resources/
>                 Info.plist
>                 PrivacyInfo.xcprivacy
>             ...
>     ...
> ```
>
> **Add a privacy manifest to your Swift package**
>
> A Swift package’s resources can include its privacy manifest file. For more information about adding resource files to Swift packages, see Bundling resources with a Swift package. Source files reside in a subfolder of a package’s `Sources` directory that has the same name as the target they belong to. This is the default location for resources. If your resource files reside in the default location, add the privacy manifest to it. The following example shows a package manifest that declares the `SomeLibrary` target. Place your privacy manifest file in Sources/SomeLibrary if you don’t specify an alternative location, as shown below:
> ```
> SamplePackage/
>     README.md
>     Package.swift
>     Sources/
>         SomeLibrary/
>             SomeLibrary.swift
>             Product.swift
>             PrivacyInfo.xcprivacy
>             ...
>     Tests/
>         ...
> ```
> Alternatively, if your resource files reside in a subfolder separate from your source files, add the privacy manifest to this directory. Place your privacy manifest file in `Sources/SomeLibrary/Resources` if you put all your resource files into a directory named `Resources`:
> ```
> SamplePackage/
>     README.md
>     Package.swift
>     Sources/
>         SomeLibrary/
>             SomeLibrary.swift
>             Product.swift
>             ...
>             Resources/
>                 PrivacyInfo.xcprivacy
>                 ...
>     Tests/
>         ...
> ```
> Xcode doesn’t recognize privacy manifest files as resources by default. After adding the manifest file to your package, explicitly declare the file or the directory that includes it as a package resource. In the following example, the package manifest declares `PrivacyInfo.xcprivacy` as an explicit resource:
> ```
> targets: [
>     .target(
>         name: "SomeLibrary",
>         resources: [
>             .process("PrivacyInfo.xcprivacy")]
>     ),
> ]
> ```
> In this example, the package manifest lists the `Resources` directory as an explicit resource:
> ```
> targets: [
>     .target(
>         name: "SomeLibrary",
>         resources: [
>             .process("Resources")]
>     ),
> ]
> ```
> If you distribute your binary framework as a Swift package, check that your XCFramework bundle includes a privacy manifest for each platform that you support. For more information, see Distributing binary frameworks as Swift packages.
>
> **Distribute your static library with a privacy manifest**
>
> A static library is an archive of object files with a `.a` file extension. It doesn’t support resources such as the privacy manifest. If you currently distribute your SDK as a static library and want to update it to include a privacy manifest in Xcode, create a new static framework target that includes all your static library’s source files and resources, then add the privacy manifest to the target’s resource. For more information on how to create a static framework, see Creating a static framework.
>
> If you don’t use Xcode to build your static library, create a static framework bundle for your static library manually, then add the privacy manifest to the bundle as a resource. For more information about framework bundle structure, see Placing content in a bundle. To identify the privacy manifest location in the static framework, see Add a privacy manifest to your framework.
>
> **Verify your XCFramework bundle includes the necessary privacy manifests**
>
> An XCFramework bundle is a binary package that can include multiple platform-specific variants of a framework or library. It supports distribution of Swift and C-based code. For more information about creating an XCFramework bundle, see Creating a multiplatform binary framework bundle.
>
> After adding a privacy manifest to your framework, consider distributing it as a signed XCFramework bundle. When you generate an XCFramework bundle with your framework, the generated bundle contains a privacy manifest file for each platform that your framework supports. The framework platform determines the location of the manifest file. When you sign your XCFramework bundle, developers who incorporate the framework can see whether updates to the framework have compatible code signatures. For more information, see Verifying the origin of your XCFrameworks.
>
> After an update, `SampleFramework` supports iOS, iOS Simulator, Mac Catalyst, and macOS. The `MyArchives` directory contains archives of each variant of `SampleFramework`. Running the following command in Terminal creates an XCFramework with variants for iOS, iOS Simulator, Mac Catalyst, and macOS:
> ```
> xcodebuild -create-xcframework
> -archive MyArchives/SampleFramework-iOS.xcarchive -framework SampleFramework.framework
> -archive MyArchives/SampleFramework-macOS.xcarchive -framework SampleFramework.framework
> -archive MyArchives/SampleFramework-iOS_Simulator.xcarchive -framework SampleFramework.framework
> -archive MyArchives/SampleFramework-Mac_Catalyst.xcarchive -framework SampleFramework.framework
> -output xcframeworks/SampleFramework.xcframework
> ```
> Each variant of `SampleFramework` contains a privacy manifest file at the appropriate location, as shown below:
> ```
> SampleFramework.xcframework/
>     Info.plist
>     ios-arm64/
>        dSYMs/
>            ...
>        SampleFramework.framework/
>            Info.plist
>            SampleFramework
>            PrivacyInfo.xcprivacy
>            ...
>     macos-arm64_x86_64/
>         dSYMs/
>             ...
>         SampleFramework.framework/
>             SampleFramework -> Versions/Current/SampleFramework
>             Resources -> Versions/Current/Resources
>             Versions/
>                 Current -> A
>                 A/
>                     SampleFramework
>                     Resources/
>                         Info.plist
>                         PrivacyInfo.xcprivacy
>                     ...
>             ...
>     ios-arm64_x86_64-simulator/
>         dSYMs/
>             ...
>         SampleFramework.framework/
>             Info.plist
>             SampleFramework
>             PrivacyInfo.xcprivacy
>             ...
>     ios-arm64_x86_64-maccatalyst/
>         dSYMs/
>            ...
>         SampleFramework.framework/
>             SampleFramework -> Versions/Current/SampleFramework
>             Resources -> Versions/Current/Resources
>             Versions/
>                 Current -> A
>                 A/
>                     SampleFramework
>                     Resources/
>                         Info.plist
>                         PrivacyInfo.xcprivacy
>                     ...
>             ...
> ```
> To identify the privacy manifest location in frameworks, see Add a privacy manifest to your framework. To ship your static library with a privacy manifest, see Distribute your static library with a privacy manifest.

Required bundle locations (verbatim paths from the source):

| Product | Platform | Location of `PrivacyInfo.xcprivacy` |
|---|---|---|
| App | iOS, iPadOS, tvOS, visionOS, watchOS | `Sample.app/PrivacyInfo.xcprivacy` (root of the app bundle) |
| App | macOS, Mac Catalyst | `MacSample.app/Contents/Resources/PrivacyInfo.xcprivacy` |
| Framework | iOS, iPadOS, tvOS, visionOS, watchOS | `SampleFramework.framework/PrivacyInfo.xcprivacy` (root of the framework bundle) |
| Framework | macOS, Mac Catalyst | `MacSampleFramework.framework/Versions/A/Resources/PrivacyInfo.xcprivacy` |
| Swift package | — | `Sources/SomeLibrary/PrivacyInfo.xcprivacy` or `Sources/SomeLibrary/Resources/PrivacyInfo.xcprivacy`, declared with `.process(...)` in `resources:` |
| XCFramework | each platform variant | one `PrivacyInfo.xcprivacy` per variant, at that platform’s framework location |

**Applies to:** All apps (validity); apps and frameworks/packages that contain a privacy manifest (location).

- **[PRIV-07]** Does every privacy manifest in the app (including those from third-party SDKs) contain only the expected keys and values?
  - quote: "All privacy manifest files in your app must be valid, containing only the expected keys and values."
  - surface: code
  - verify: Build/archive the app, then `find <Archive>.xcarchive/Products/Applications -name PrivacyInfo.xcprivacy`; for each file run `plutil -convert json -o - <file>` and confirm the root keys are only `NSPrivacyTracking`, `NSPrivacyTrackingDomains`, `NSPrivacyCollectedDataTypes`, `NSPrivacyAccessedAPITypes`, and that every nested key/value is one of the values listed in PRIV.E, PRIV.G–PRIV.K, PRIV.L.
  - fix: Remove unexpected keys / correct values in first-party manifests; for third-party manifests see PRIV-08 and PRIV.C.
- **[PRIV-08]** If an invalid privacy manifest comes from a third-party SDK, has the SDK been updated to a version that includes a valid privacy manifest?
  - quote: "If an invalid file comes from a third-party SDK, contact its developer for an updated version of the SDK that includes a valid privacy manifest."
  - surface: code
  - verify: For each invalid file found by PRIV-07, map its path (e.g. `Frameworks/X.framework/PrivacyInfo.xcprivacy` or `X_Bundle.bundle/PrivacyInfo.xcprivacy`) to the dependency in `Package.resolved` / `Podfile.lock` / `Cartfile.resolved`; check whether a newer version of that SDK is available.
  - fix: Update the SDK to a version with a valid manifest; if none exists, contact the SDK developer (manual) or follow PRIV.C.
- **[PRIV-09]** Has the developer checked for an App Store Connect email naming invalid privacy manifest files from a previous upload?
  - quote: "If you upload an app to App Store Connect that contains privacy manifest files with unexpected keys or values, you receive an email that includes the name and path of the invalid files in your app bundle."
  - surface: manual
  - verify: Ask the developer whether they received such an email for any build of this app; if so, record the file names/paths it lists and confirm each is fixed (PRIV-07).
  - fix: manual — requires developer decision/legal/business action
- **[PRIV-10]** For iOS, iPadOS, tvOS, visionOS, or watchOS apps, is the app’s `PrivacyInfo.xcprivacy` at the root of the `.app` bundle?
  - quote: "If you build an iOS, iPadOS, tvOS, visionOS, or watchOS app, place the privacy manifest at the root of your app’s bundle."
  - surface: code
  - verify: Build the app; `ls <Build>/Products/*/<App>.app/PrivacyInfo.xcprivacy` must exist (not only inside a nested folder or resource bundle).
  - fix: Add the file to the app target’s resources (Xcode places it at the bundle root); remove any folder reference that nests it.
- **[PRIV-11]** For macOS and Mac Catalyst apps, is the privacy manifest at `Contents/Resources/PrivacyInfo.xcprivacy` in the app bundle?
  - quote: "For macOS and Mac Catalyst apps, place the privacy manifest file in `Contents/Resources/` in your app’s bundle."
  - surface: code
  - verify: Build the macOS / Mac Catalyst variant; check `<App>.app/Contents/Resources/PrivacyInfo.xcprivacy` exists.
  - fix: Add the file to the macOS target’s Copy Bundle Resources phase.
- **[PRIV-12]** For first-party frameworks, is the privacy manifest at the framework bundle root (iOS/iPadOS/tvOS/visionOS/watchOS) or at `Versions/A/Resources/` (macOS/Mac Catalyst)?
  - quote: "For iOS, iPadOS, tvOS, visionOS, or watchOS frameworks, place the privacy manifest at the root of your framework’s bundle."
  - surface: code
  - verify: For each built first-party `.framework` under `<App>.app/Frameworks/` (or `Contents/Frameworks/`), check `X.framework/PrivacyInfo.xcprivacy` (iOS-family) or `X.framework/Versions/A/Resources/PrivacyInfo.xcprivacy` (macOS/Mac Catalyst).
  - fix: Add `PrivacyInfo.xcprivacy` to the framework target’s resources.
- **[PRIV-13]** For local/first-party Swift packages that contain a privacy manifest, is `PrivacyInfo.xcprivacy` (or its enclosing directory) explicitly declared as a resource in `Package.swift`?
  - quote: "Xcode doesn’t recognize privacy manifest files as resources by default. After adding the manifest file to your package, explicitly declare the file or the directory that includes it as a package resource."
  - surface: code
  - verify: `find . -path '*/Sources/*' -name PrivacyInfo.xcprivacy -not -path '*/.build/*'`; for each, open the package’s `Package.swift` and confirm the target has `resources: [.process("PrivacyInfo.xcprivacy")]` or `.process("<dir containing it>")` (or `.copy(...)` covering it).
  - fix: Add `.process("PrivacyInfo.xcprivacy")` (or the `Resources` directory) to that target’s `resources:` array.
- **[PRIV-14]** For binary frameworks distributed as Swift packages / XCFrameworks that the developer owns, does each platform variant include a privacy manifest?
  - quote: "If you distribute your binary framework as a Swift package, check that your XCFramework bundle includes a privacy manifest for each platform that you support."
  - surface: code
  - verify: For each first-party `.xcframework`, list its variant directories (from its `Info.plist` `AvailableLibraries`) and confirm `PrivacyInfo.xcprivacy` exists in each variant at the platform-specific location from the table above.
  - fix: Rebuild the XCFramework with `xcodebuild -create-xcframework` from archives whose framework targets include the manifest.

---

## PRIV.C Locating and managing an invalid privacy manifest

**Source text (verbatim):**
> **Locate an invalid privacy manifest in your app archive**
>
> To find an invalid privacy manifest in your app archive:
> - 1. Gather the location of the file from the email you received from Apple.
> - 2. In Xcode, choose Window > Organizer, then click Archives.
> - 3. Control-click your app archive in the organizer, and choose Show in Finder from the contextual menu. Xcode opens the Finder to the location of your archive.
> - 4. In the Finder, control-click your archive, and choose Show Package Contents to open it.
> - 5. Navigate to the location of the privacy manifest in your archive.
>
> **Managing an invalid privacy manifest**
>
> If you’re unable to obtain a valid privacy manifest from a third-party SDK developer and need to submit your app, locate the invalid privacy manifest in your app archive, delete it, and submit your archive using Xcode. Alternatively, locate the invalid privacy manifest in your app, fix the validation issues in the file, and submit your archive using Xcode. To troubleshoot invalid privacy manifests, see TN3181: Debugging an invalid privacy manifest.
>
> Important: Removing or modifying the invalid privacy manifest breaks the archived app’s signature. Xcode will re-sign your app when you distribute your archive from the Archives organizer. For more information, see “Select a method for distribution,” in Distributing your app for beta testing and releases.

**Applies to:** Apps whose archive contains an invalid privacy manifest from a third-party SDK that cannot be updated.

- **[PRIV-15]** If an invalid third-party privacy manifest was deleted or edited inside the archive, was the archive then distributed from Xcode’s Archives organizer (so Xcode re-signs it) rather than uploaded by another route?
  - quote: "Removing or modifying the invalid privacy manifest breaks the archived app’s signature. Xcode will re-sign your app when you distribute your archive from the Archives organizer."
  - surface: manual
  - verify: Ask the developer whether any `PrivacyInfo.xcprivacy` was removed/edited inside an `.xcarchive`; if yes, confirm the upload was done via Window > Organizer > Archives > Distribute App.
  - fix: Distribute the modified archive from the Xcode Archives organizer.

---

## PRIV.D NSPrivacyTracking and NSPrivacyTrackingDomains

**Source text (verbatim):**
> **NSPrivacyTracking**
>
> A Boolean value that indicates whether your app or third-party SDK uses data for tracking.
>
> Set the value for this key to `true` if your app or third-party SDK uses data for tracking as defined under the App Tracking Transparency framework. When set to `true` you need to provide a list of internet domains in NSPrivacyTrackingDomains. For more information, see User Privacy and Data Use.
>
> **NSPrivacyTrackingDomains**
>
> A list of the internet domains your app or third-party SDK uses for tracking.
>
> If the user has not granted tracking permission through the App Tracking Transparency framework, network requests to these domains fail and your app receives an error. To provide a list of internet domains in `NSPrivacyTrackingDomains`, set NSPrivacyTracking to `true`. For more information, see User Privacy and Data Use.
>
> (TN3181) **Configure a tracking domain**
>
> A tracking domain is a string that identifies an internet domain your app or third-party SDK connects to that engages in tracking. You set the value of the `NSPrivacyTrackingDomains` key to a list of tracking domains in your privacy manifest. The value of the string meets the following requirements:
> - Includes the top-level domain or subdomain.
> - Contains no path and query components.
> - Contains no trailing slash.
>
> **Possible reason for an invalid tracking value**
>
> A value for the `NSPrivacyTracking` key is invalid if the value is any other type than a `Boolean`. In your privacy manifest, change the type of the key to `Boolean`.
>
> **Possible reasons for an invalid tracking domains value**
>
> A value for the `NSPrivacyTrackingDomains` key is invalid if the value is any other type than an array of strings. In your privacy manifest, change the type of the key to `Array`, then add one or more tracking domains to the array. For more information, see Configure a tracking domain.
>
> You can create an invalid privacy manifest when you use both `NSPrivacyTrackingDomains` and `NSPrivacyTracking` keys as follows:
>
> Note: If your app or third-party SDK doesn’t connect, or no longer connects to any tracking domains, remove both `NSPrivacyTrackingDomains` and `NSPrivacyTracking` keys from your privacy manifest. Alternatively, set the value of `NSPrivacyTracking` to `false` and remove `NSPrivacyTrackingDomains` from your privacy manifest.
>
> (TN3182) When you build an app or third-party SDK that contacts domains engaged in tracking, perform these steps in your privacy manifest (`PrivacyInfo.xcprivacy`):
> - 1. Add the `NSPrivacyTracking` key and set its value to `true`.
> - 2. Add the `NSPrivacyTrackingDomains` key and set its value to a list of tracking domains.
>
> Each string value in the array identifies an internet domain your app or third-party SDK connects to that engages in tracking.

TN3181 table (verbatim):

| Reason | Solution |
|---|---|
| The value of the `NSPrivacyTracking` key is `true` and the value of the `NSPrivacyTrackingDomains` key is an empty array of strings. | Fill the array with one or more tracking domains your app or third-party SDK connects to. |
| The value of the `NSPrivacyTracking` key is `true` and the value of the `NSPrivacyTrackingDomains` key is an array of strings, but some entries are improperly formatted. | Confirm you configure each tracking domain in the array as described in Configure a tracking domain. |
| The value of the `NSPrivacyTracking` key is `false` and the `NSPrivacyTrackingDomains` key contains some entries. | Remove the `NSPrivacyTrackingDomains` key from your privacy manifest. |

TN3182 format examples (verbatim):
```
<key>NSPrivacyTracking</key>
<!-- Use <true/> if your app or third-party SDK contacts domains engaged in tracking; otherwise use 
    <false/>. -->
<true/>
```
```
<plist>
<dict>
    <key>NSPrivacyTracking</key>
    <true/>
    <key>NSPrivacyTrackingDomains</key>
    <array>
        <string>mywebsite.example.com</string>
        <string>tracking.subdomain.example.com</string>
    </array>
</dict>
</plist>
```

**Applies to:** Apps and third-party SDKs whose privacy manifest contains `NSPrivacyTracking` or `NSPrivacyTrackingDomains`, or that use data for tracking / contact domains engaged in tracking.

- **[PRIV-16]** If the app uses data for tracking as defined under App Tracking Transparency, is `NSPrivacyTracking` set to `true`?
  - quote: "Set the value for this key to `true` if your app or third-party SDK uses data for tracking as defined under the App Tracking Transparency framework."
  - surface: code
  - verify: Grep the app for ATT use (`ATTrackingManager`, `requestTrackingAuthorization`, `NSUserTrackingUsageDescription` in Info.plist) and for any `NSPrivacyCollectedDataTypeTracking` = `true` entry; if present, read `NSPrivacyTracking` in the app’s `PrivacyInfo.xcprivacy` (`plutil -extract NSPrivacyTracking raw PrivacyInfo.xcprivacy`). Whether data is used for tracking is ultimately a developer attestation.
  - fix: Set `<key>NSPrivacyTracking</key><true/>` and add `NSPrivacyTrackingDomains` (PRIV-17).
- **[PRIV-17]** When `NSPrivacyTracking` is `true`, does `NSPrivacyTrackingDomains` exist and contain one or more domains?
  - quote: "The value of the `NSPrivacyTracking` key is `true` and the value of the `NSPrivacyTrackingDomains` key is an empty array of strings."
  - surface: code
  - verify: `plutil -convert json -o - PrivacyInfo.xcprivacy`; if `NSPrivacyTracking == true`, `NSPrivacyTrackingDomains` must be a non-empty array.
  - fix: Fill the array with one or more tracking domains your app connects to.
- **[PRIV-18]** When `NSPrivacyTracking` is `false`, is `NSPrivacyTrackingDomains` free of entries?
  - quote: "The value of the `NSPrivacyTracking` key is `false` and the `NSPrivacyTrackingDomains` key contains some entries."
  - surface: code
  - verify: Same JSON dump; if `NSPrivacyTracking` is `false` and `NSPrivacyTrackingDomains` has entries, fail.
  - fix: Remove the `NSPrivacyTrackingDomains` key from your privacy manifest.
- **[PRIV-19]** Is `NSPrivacyTracking` a Boolean (not a string or number)?
  - quote: "A value for the `NSPrivacyTracking` key is invalid if the value is any other type than a `Boolean`."
  - surface: code
  - verify: In the XML, the value following `<key>NSPrivacyTracking</key>` must be `<true/>` or `<false/>`.
  - fix: Change the type of the key to `Boolean`.
- **[PRIV-20]** Is `NSPrivacyTrackingDomains` an array of strings?
  - quote: "A value for the `NSPrivacyTrackingDomains` key is invalid if the value is any other type than an array of strings."
  - surface: code
  - verify: The value following `<key>NSPrivacyTrackingDomains</key>` must be `<array>` containing only `<string>` elements.
  - fix: Change the type of the key to `Array`, then add one or more tracking domains to the array.
- **[PRIV-21]** Does every tracking domain include the top-level domain or subdomain, contain no path and query components, and contain no trailing slash?
  - quote: "Contains no path and query components."
  - surface: code
  - verify: For each `NSPrivacyTrackingDomains` string, fail if it contains `/` (a path component or trailing slash) or `?` (a query component); confirm it includes the top-level domain (Apple’s examples: `mywebsite.example.com`, `tracking.subdomain.example.com`).
  - fix: Rewrite each entry in the form of Apple’s examples, e.g. `mywebsite.example.com`.
- **[PRIV-22]** If the app contacts domains engaged in tracking, are those domains listed in `NSPrivacyTrackingDomains`? (Apple notes that requests to listed domains fail when the user has not granted tracking permission.)
  - quote: "Add the `NSPrivacyTrackingDomains` key and set its value to a list of tracking domains."
  - surface: runtime
  - verify: Grep source for hard-coded hosts (`https?://[A-Za-z0-9.-]+`) and SDK endpoints; ask the developer which engage in tracking; then run the app with tracking permission denied (Settings > Privacy & Security > Tracking off) and observe network errors to listed domains in the Xcode console / Instruments Network to confirm core app flows still work.
  - fix: Add missing tracking domains to `NSPrivacyTrackingDomains`. Because “If the user has not granted tracking permission through the App Tracking Transparency framework, network requests to these domains fail and your app receives an error,” review the observed errors with the developer.
- **[PRIV-23]** If the app does not connect (or no longer connects) to any tracking domains, have `NSPrivacyTrackingDomains` and `NSPrivacyTracking` been removed (or `NSPrivacyTracking` set to `false` with domains removed)?
  - quote: "If your app or third-party SDK doesn’t connect, or no longer connects to any tracking domains, remove both `NSPrivacyTrackingDomains` and `NSPrivacyTracking` keys from your privacy manifest."
  - surface: code
  - verify: If the developer attests no tracking domains, confirm the manifest has neither key, or has `NSPrivacyTracking` = `false` and no `NSPrivacyTrackingDomains`.
  - fix: Remove both keys, or set `NSPrivacyTracking` to `false` and remove `NSPrivacyTrackingDomains`.

---

## PRIV.E Describing data use in privacy manifests — NSPrivacyCollectedDataTypes

**Source text (verbatim):**
> Declare the data collected by your app or by third-party SDKs.
>
> Record the categories of data that your app or third-party SDK collects about the person using the app, and the reasons it collects the data. App developers can use Xcode to create a privacy report, summarizing the information about collected data in their app and the third-party SDKs the app links to.
>
> Important: Third-party SDKs need to provide their own privacy manifest files that record the types of data they collect. Your app’s privacy manifest file doesn’t need to cover data collected by third-party SDKs that your app links to.
>
> **Describe the data your app or third-party SDK collects**
>
> For each type of data your app or third-party SDK collects, add a dictionary to the NSPrivacyCollectedDataTypes array in your privacy information file. Add the following keys to the dictionary.
> - NSPrivacyCollectedDataType: A string that identifies the type of data your app or third-party SDK collects. Choose the value from the list of data types below that matches the data your app or third-party SDK collects.
> - NSPrivacyCollectedDataTypeLinked: A Boolean that indicates whether your app or third-party SDK links this data type to the user’s identity. For more information, see Data linked to the user in App privacy details on the App Store.
> - NSPrivacyCollectedDataTypeTracking: A Boolean that indicates whether your app or third-party SDK uses this data type to track.
> - NSPrivacyCollectedDataTypePurposes: An array of strings that lists the reasons your app or third-party SDK collects the data. Choose values from the list of purposes below that match the reasons your app or third-party SDK collects this data type.
>
> Xcode won’t generate a privacy report correctly if you define your own collected data types for the `NSPrivacyCollectedDataType` key, or provide your own reasons for the `NSPrivacyCollectedDataTypePurposes` key. Use values listed in the documentation for the keys.
>
> **Create your app’s privacy report**
>
> Xcode can create a privacy report by aggregating the privacy manifests from your app and the third-party SDKs it links to. Use the privacy report to better understand all of the data collected by your app and whether it tracks. Create the privacy report for your app by doing the following:
> - 1. Open your project in Xcode.
> - 2. Choose Product > Archive. Xcode creates the archive and reveals it in the organizer.
> - 3. Control-click the archive in the organizer and choose Generate Privacy Report.
> - 4. Choose a location to save the privacy report.
> - 5. Switch to Finder.
> - 6. Navigate to the location where you saved the privacy report, and double-click to open the report in Preview.
>
> The privacy report is organized in a similar way to Privacy Nutrition Labels. Refer to this report when you provide your app’s privacy details in App Store Connect. For more information on providing your app’s privacy details, see App privacy details on the App Store.

Sub-keys of each `NSPrivacyCollectedDataTypes` dictionary (key pages):

| Key | Xcode display name (ideTitle) | Type | Abstract (verbatim) |
|---|---|---|---|
| `NSPrivacyCollectedDataType` | Collected Data Type | String | A string that identifies the type of data your app or third-party SDK collects. |
| `NSPrivacyCollectedDataTypeLinked` | Linked to User | Boolean | A Boolean that indicates whether your app or third-party SDK links this data type to the user’s identity. |
| `NSPrivacyCollectedDataTypeTracking` | Used for Tracking | Boolean | A Boolean that indicates whether your app or third-party SDK uses this data type to track. |
| `NSPrivacyCollectedDataTypePurposes` | Collection Purposes | Array of String | An array of strings that identify reasons your app or third-party SDK collects private data. |

Allowed `NSPrivacyCollectedDataType` values (complete, verbatim, from https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes/nsprivacycollecteddatatype):

| Value | Description (verbatim) |
|---|---|
| `NSPrivacyCollectedDataTypeName` | Name, such as first or last name. |
| `NSPrivacyCollectedDataTypeEmailAddress` | Email address, including but not limited to a hashed email address. |
| `NSPrivacyCollectedDataTypePhoneNumber` | Phone number, including but not limited to a hashed phone number. |
| `NSPrivacyCollectedDataTypePhysicalAddress` | Physical address, such as home address, physical address, or mailing address. |
| `NSPrivacyCollectedDataTypeOtherUserContactInfo` | Other user contact info; any other information that can be used to contact the user outside the app. |
| `NSPrivacyCollectedDataTypeHealth` | Health and medical data, including but not limited to data from the Clinical Health Records API, HealthKit API, MovementDisorderAPIs, or health-related human subject research or any other user provided health or medical data. |
| `NSPrivacyCollectedDataTypeFitness` | Fitness and exercise data, including but not limited to the Motion and Fitness API. |
| `NSPrivacyCollectedDataTypePaymentInfo` | Payment info; such as form of payment, payment card number, or bank account number. If your app uses a payment service, the payment information is entered outside your app, and you as the developer never have access to the payment information, it is not collected and does not need to be disclosed. |
| `NSPrivacyCollectedDataTypeCreditInfo` | Credit info, such as credit score. |
| `NSPrivacyCollectedDataTypeOtherFinancialInfo` | Other financial info; such as salary, income, assets, debts, or any other financial information. |
| `NSPrivacyCollectedDataTypePreciseLocation` | Precise location; information that describes the location of a user or device with the same or greater resolution as a latitude and longitude with three or more decimal places. |
| `NSPrivacyCollectedDataTypeCoarseLocation` | Coarse location; information that describes the location of a user or device with lower resolution than a latitude and longitude with three or more decimal places, such as Approximate Location Services. |
| `NSPrivacyCollectedDataTypeSensitiveInfo` | Sensitive information; such as racial or ethnic data, sexual orientation, pregnancy or childbirth information, disability, religious or philosophical beliefs, trade union membership, political opinion, genetic information, or biometric data. |
| `NSPrivacyCollectedDataTypeContacts` | Contacts; such as a list of contacts in the user’s phone, address book, or social graph. |
| `NSPrivacyCollectedDataTypeEmailsOrTextMessages` | Emails or text messages; including subject line, sender, recipients, and contents of the email or message. |
| `NSPrivacyCollectedDataTypePhotosorVideos` | The user’s photos or videos. |
| `NSPrivacyCollectedDataTypeAudioData` | The user’s voice or sound recordings. |
| `NSPrivacyCollectedDataTypeGameplayContent` | Gameplay content; such as saved games, multiplayer matching or gameplay logic, or user-generated content in-game. |
| `NSPrivacyCollectedDataTypeCustomerSupport` | Data generated by the user during a customer support request. |
| `NSPrivacyCollectedDataTypeOtherUserContent` | Any other user-generated content. |
| `NSPrivacyCollectedDataTypeBrowsingHistory` | Browsing history; information about content the user has viewed that is not part of the app, such as websites. |
| `NSPrivacyCollectedDataTypeSearchHistory` | Information about searches performed in the app. |
| `NSPrivacyCollectedDataTypeUserID` | User ID; such as screen name, handle, account ID, assigned user ID, customer number, or other user- or account-level ID that can be used to identify a particular user or account. |
| `NSPrivacyCollectedDataTypeDeviceID` | Device ID; such as the device’s advertising identifier, or other device-level ID. |
| `NSPrivacyCollectedDataTypePurchaseHistory` | An account’s or individual’s purchases or purchase tendencies. |
| `NSPrivacyCollectedDataTypeProductInteraction` | Product interaction; such as app launches, taps, clicks, scrolling information, music listening data, video views, saved place in a game, video, or song, or other information about how the user interacts with the app. |
| `NSPrivacyCollectedDataTypeAdvertisingData` | Advertising data; such as information about the advertisements the user has seen. |
| `NSPrivacyCollectedDataTypeOtherUsageData` | Any other data about user activity in the app. |
| `NSPrivacyCollectedDataTypeCrashData` | Crash data, such as crash logs. |
| `NSPrivacyCollectedDataTypePerformanceData` | Performance data, such as launch time, freeze rate, or energy use. |
| `NSPrivacyCollectedDataTypeOtherDiagnosticData` | Any other data collected for the purposes of measuring technical diagnostics related to the app. |
| `NSPrivacyCollectedDataTypeEnvironmentScanning` | Environment scanning; such as mesh, planes, scene classification, and/or image detection of the user’s surroundings. |
| `NSPrivacyCollectedDataTypeHands` | The user’s hand structure and hand movements. |
| `NSPrivacyCollectedDataTypeHead` | The user’s head movement. |
| `NSPrivacyCollectedDataTypeOtherDataTypes` | Any other data types not mentioned. |

(35 values. Note Apple’s exact casing `NSPrivacyCollectedDataTypePhotosorVideos` — lowercase “or”.)

Allowed `NSPrivacyCollectedDataTypePurposes` values (complete, verbatim, from https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes/nsprivacycollecteddatatypepurposes):

| Value | Description (verbatim) |
|---|---|
| `NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising` | Third-party advertising; such as displaying third-party ads in your app, or sharing data with entities who display third-party ads. |
| `NSPrivacyCollectedDataTypePurposeDeveloperAdvertising` | Developer’s advertising or marketing; such as displaying first-party ads in your app, sending marketing communications directly to your users, or sharing data with entities who will display your ads. |
| `NSPrivacyCollectedDataTypePurposeAnalytics` | Analytics — using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics. |
| `NSPrivacyCollectedDataTypePurposeProductPersonalization` | Product personalization — customizing what the user sees, such as a list of recommended products, posts, or suggestions. |
| `NSPrivacyCollectedDataTypePurposeAppFunctionality` | App functionality; such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support. |
| `NSPrivacyCollectedDataTypePurposeOther` | Any other purposes not listed. |

**Applies to:** Apps and third-party SDKs that collect data about the person using the app.

- **[PRIV-24]** For each type of data the app collects, is there a dictionary in `NSPrivacyCollectedDataTypes`?
  - quote: "For each type of data your app or third-party SDK collects, add a dictionary to the NSPrivacyCollectedDataTypes array in your privacy information file."
  - surface: code
  - verify: Inventory what the app’s own code sends off-device: grep for networking (`URLSession`, `URLRequest`, `Alamofire`, `WebSocket`, analytics/crash SDK calls), sign-in fields (email, name, phone), `CLLocationManager`, `HKHealthStore`, `CNContactStore`, `PHPicker`/`PHPhotoLibrary`, `AVAudioRecorder`, `ASIdentifierManager`/`advertisingIdentifier`, `identifierForVendor`, purchase/receipt uploads, crash/diagnostic upload; map each to a value in the data-type table and confirm a dictionary exists. Confirm with the developer what their server stores.
  - fix: Add one dictionary per collected data type with the four keys (PRIV.N).
- **[PRIV-25]** Is every `NSPrivacyCollectedDataType` value exactly one of the 35 values in Apple’s list (no custom values, exact casing)?
  - quote: "Xcode won’t generate a privacy report correctly if you define your own collected data types for the `NSPrivacyCollectedDataType` key"
  - surface: code
  - verify: Extract all `NSPrivacyCollectedDataType` strings (`plutil -convert json -o - PrivacyInfo.xcprivacy`) and compare case-sensitively against the table above.
  - fix: Replace custom/misspelled values with the matching value from the table (e.g. `NSPrivacyCollectedDataTypePhotosorVideos`).
- **[PRIV-26]** Is every `NSPrivacyCollectedDataTypePurposes` value exactly one of the 6 values in Apple’s list?
  - quote: "or provide your own reasons for the `NSPrivacyCollectedDataTypePurposes` key. Use values listed in the documentation for the keys."
  - surface: code
  - verify: Extract every string in every `NSPrivacyCollectedDataTypePurposes` array; compare case-sensitively against the purposes table.
  - fix: Replace with the matching purpose value.
- **[PRIV-27]** Does each collected-data dictionary have `NSPrivacyCollectedDataTypeLinked` set correctly (true if the data is linked to the user’s identity)?
  - quote: "A Boolean that indicates whether your app or third-party SDK links this data type to the user’s identity."
  - surface: manual
  - verify: For each entry, confirm the key exists and is `<true/>`/`<false/>`; ask the developer whether this data is associated with an account, user ID, or other identity on their servers.
  - fix: Set `NSPrivacyCollectedDataTypeLinked` to the value the developer attests.
- **[PRIV-28]** Does each collected-data dictionary have `NSPrivacyCollectedDataTypeTracking` set correctly (true if the data type is used to track)?
  - quote: "A Boolean that indicates whether your app or third-party SDK uses this data type to track."
  - surface: manual
  - verify: Confirm the key exists and is Boolean; ask the developer whether the data type is used for tracking; if any entry is `true`, PRIV-16 must also pass.
  - fix: Set `NSPrivacyCollectedDataTypeTracking` accordingly.
- **[PRIV-29]** Apple says to refer to the Xcode privacy report when providing App Privacy details: has a privacy report been generated from the release archive and compared with the App Privacy details in App Store Connect?
  - quote: "Refer to this report when you provide your app’s privacy details in App Store Connect."
  - surface: asc
  - verify: Archive the app (Product > Archive), Control-click the archive > Generate Privacy Report; then in App Store Connect > Apps > [App] > App Privacy, compare each data type, “Linked to you”, “Used to track you” and purpose against the report (which aggregates the app’s and SDKs’ manifests).
  - fix: Update App Store Connect > App Privacy answers (or the manifests) so they agree with the privacy report and actual data practices.
- **[PRIV-30]** Is the app relying on its own manifest only for its own data collection, with each linked third-party SDK supplying its own manifest for the data it collects?
  - quote: "Third-party SDKs need to provide their own privacy manifest files that record the types of data they collect."
  - surface: code
  - verify: For every third-party SDK that collects data (analytics, ads, crash reporting, auth), confirm the resolved SDK ships `PrivacyInfo.xcprivacy` (check `SourcePackages/checkouts/<pkg>/**/PrivacyInfo.xcprivacy`, `Pods/<pod>/**/PrivacyInfo.xcprivacy`, or inside the `.xcframework` variants).
  - fix: Update SDKs to versions that include a privacy manifest; if a vendor provides none, contact the vendor (manual).

---

## PRIV.F Describing use of required reason API — general rules

**Source text (verbatim):**
> Ensure your use of covered API is consistent with policy.
>
> Some APIs that your app uses to deliver its core functionality — in code you write or included in a third-party SDK — have the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. Describe the reasons your app or third-party SDK on iOS, iPadOS, tvOS, visionOS, or watchOS uses these APIs, and check that your app or third-party SDK only uses the APIs for the expected reasons.
>
> Important: If you upload an app to App Store Connect that uses required reason API without describing the reason in its privacy manifest file, Apple sends you an email reminding you to add the reason to the app’s privacy manifest. Starting May 1, 2024, apps that don’t describe their use of required reason API in their privacy manifest file aren’t accepted by App Store Connect.
>
> For each category of required reason API that your app or third-party SDK uses, add a dictionary to the NSPrivacyAccessedAPITypes array in your app or third-party SDK’s privacy manifest file that reports the reasons your app uses the API category. If you use the API in your app’s code, then you need to report the API in your app’s privacy manifest file. If you use the API in your third-party SDK’s code, then you need to report the API in your third-party SDK’s privacy manifest file. Your third-party SDK can’t rely on the privacy manifest files for apps that link the third-party SDK, or those of other third-party SDKs the app links, to report your third-party SDK’s use of required reasons API.
>
> For each executable or dynamic library in an app that uses a required reason API, the bundle that includes the executable or dynamic library needs to include a privacy manifest file that reports the API. For the expected location of frameworks and dynamic libraries, see Placing content in a bundle.
>
> Important: Your app or third-party SDK must declare one or more approved reasons that accurately reflect your use of each of these APIs and the data derived from their use. You may use these APIs and the data derived from their use for the declared reasons only. These declared reasons must be consistent with your app’s functionality as presented to users, and you may not use the APIs or derived data for tracking.
>
> Each dictionary in the `NSPrivacyAccessedAPITypes` array needs to contain these keys and values:
> - NSPrivacyAccessedAPIType: A string that identifies the category of required reason APIs your app uses. The value you provide must be one of the values listed in the sections below.
> - NSPrivacyAccessedAPITypeReasons: An array of strings that identifies the reasons your app uses the APIs. The values you provide must be the values associated with the accessed API type in the sections below.
>
> The categories of required reason APIs, which APIs are in each category, and the reasons you can include in a privacy manifest are described in the documentation for the dictionary keys.
>
> Note: Apple continually reviews the list of required reason APIs and reasons for usage, and will update this article from time to time. If your app uses required reason API to provide benefits to the people using the app, for a reason that isn’t listed here, submit a request for a new approved reason.

Sub-keys of each `NSPrivacyAccessedAPITypes` dictionary:

| Key | Xcode display name (ideTitle) | Type | Abstract (verbatim) |
|---|---|---|---|
| `NSPrivacyAccessedAPIType` | Privacy Accessed API Type | String | A string that describes a category of required reason API your app or third-party SDK uses. |
| `NSPrivacyAccessedAPITypeReasons` | Privacy Accessed API Reasons | Array of String | An array of strings that identifies the reasons your app or third-party SDK uses required reason API. |

Complete list of `NSPrivacyAccessedAPIType` category values (from the NSPrivacyAccessedAPIType page and TN3183 “Select an accessed API category”):

| Category value | Unit |
|---|---|
| `NSPrivacyAccessedAPICategoryFileTimestamp` | PRIV.G |
| `NSPrivacyAccessedAPICategorySystemBootTime` | PRIV.H |
| `NSPrivacyAccessedAPICategoryDiskSpace` | PRIV.I |
| `NSPrivacyAccessedAPICategoryActiveKeyboards` | PRIV.J |
| `NSPrivacyAccessedAPICategoryUserDefaults` | PRIV.K |

**Applies to:** Apps and third-party SDKs on iOS, iPadOS, tvOS, visionOS, or watchOS that use required reason API.

- **[PRIV-31]** For each required-reason API category used in the app’s own code, does the app’s privacy manifest contain a dictionary in `NSPrivacyAccessedAPITypes` for that category?
  - quote: "If you use the API in your app’s code, then you need to report the API in your app’s privacy manifest file."
  - surface: code
  - verify: Run the PRIV.G–PRIV.K code searches over the app target’s source (exclude `Pods/`, `Carthage/`, `.build/`, `SourcePackages/`); for each category with confirmed hits, confirm an `NSPrivacyAccessedAPIType` dictionary with that category value exists in the app’s `PrivacyInfo.xcprivacy`.
  - fix: Add a dictionary `{NSPrivacyAccessedAPIType: <category>, NSPrivacyAccessedAPITypeReasons: [<reason>]}` (PRIV.M).
- **[PRIV-32]** For each executable or dynamic library in the app bundle (app extensions, widgets, watch app, embedded dynamic frameworks) that uses a required reason API, does the bundle containing it include its own privacy manifest reporting the API?
  - quote: "For each executable or dynamic library in an app that uses a required reason API, the bundle that includes the executable or dynamic library needs to include a privacy manifest file that reports the API."
  - surface: code
  - verify: List all targets that produce executables/dylibs (app extensions `.appex`, watch apps, dynamic `.framework`s). Run the PRIV.G–PRIV.K searches per target’s sources; for each target with hits, confirm `PrivacyInfo.xcprivacy` is in that target’s resources and declares the category. After build, check `<App>.app/PlugIns/*.appex/PrivacyInfo.xcprivacy`, `<App>.app/Frameworks/*.framework/PrivacyInfo.xcprivacy`, `<App>.app/Watch/*.app/PrivacyInfo.xcprivacy`.
  - fix: Add a `PrivacyInfo.xcprivacy` to that extension/framework target with the required categories and reasons.
- **[PRIV-33]** Does each third-party SDK that uses required reason API report it in the SDK’s own manifest (the app’s manifest cannot cover it)?
  - quote: "Your third-party SDK can’t rely on the privacy manifest files for apps that link the third-party SDK, or those of other third-party SDKs the app links, to report your third-party SDK’s use of required reasons API."
  - surface: code
  - verify: For source SDKs (SPM checkouts, Pods), run the PRIV.G–PRIV.K searches inside each SDK directory; for each SDK with hits, confirm it ships a `PrivacyInfo.xcprivacy` declaring that category. For binary SDKs, check `nm -u`/`strings` on the binary for the C symbols (e.g. `_stat`, `_mach_absolute_time`, `_statfs`) and confirm the shipped manifest.
  - fix: Update the SDK to a version whose manifest declares its API use; do not try to cover SDK use in the app manifest.
- **[PRIV-34]** Does every `NSPrivacyAccessedAPITypes` dictionary declare at least one approved reason that accurately reflects how the API and derived data are used?
  - quote: "Your app or third-party SDK must declare one or more approved reasons that accurately reflect your use of each of these APIs and the data derived from their use."
  - surface: manual
  - verify: For each declared category, read the code at each search hit and compare the actual use to the exact wording of the declared reason(s) in PRIV.G–PRIV.K; confirm with the developer.
  - fix: Change the declared reason(s) to the one(s) matching actual use, or change the code so its use matches an approved reason.
- **[PRIV-35]** Are the required reason APIs and derived data never used for tracking or fingerprinting?
  - quote: "you may not use the APIs or derived data for tracking"
  - surface: manual
  - verify: Trace data from each search hit: confirm values (boot time, disk space, keyboards, file timestamps, user defaults contents) are not sent to analytics/ads/attribution endpoints or combined into device identifiers.
  - fix: Remove any code that sends these values off-device for tracking/fingerprinting.
- **[PRIV-36]** If the app uses a required reason API for a reason not in Apple’s approved list, has the developer submitted a request for a new approved reason instead of declaring an unrelated reason?
  - quote: "If your app uses required reason API to provide benefits to the people using the app, for a reason that isn’t listed here, submit a request for a new approved reason."
  - surface: manual
  - verify: Ask the developer whether any required-reason API use does not match any reason code in PRIV.G–PRIV.K.
  - fix: manual — requires developer decision/legal/business action (submit at https://developer.apple.com/contact/request/privacy-manifest-reason/ or remove the API use).
- **[PRIV-79]** Are the required reason APIs and their derived data used only for the declared reasons, and are those reasons consistent with the app’s functionality as presented to users?
  - quote: "You may use these APIs and the data derived from their use for the declared reasons only. These declared reasons must be consistent with your app’s functionality as presented to users"
  - surface: manual
  - verify: For each declared category, compare each confirmed code hit (PRIV.G–PRIV.K) with the declared reason codes, and compare those reasons with the app’s user-facing features (e.g. `85F4.1` requires a screen that displays disk space; `54BD.1` requires text fields and keyboard-dependent UI); list mismatches for the developer.
  - fix: Change the code so its use matches a declared reason, or declare the reason that matches the actual, user-facing use.
- **[PRIV-80]** Does the app (including its third-party SDKs) avoid fingerprinting, whether or not the user has granted tracking permission?
  - quote: "Regardless of whether a user gives your app permission to track, fingerprinting is not allowed."
  - surface: manual
  - verify: Grep for code that combines device signals into an identifier (e.g. hashing values from the PRIV.G–PRIV.K APIs, `identifierForVendor`, locale/keyboard/disk/boot-time values) and sends it off-device; review every hit with the developer, including SDK-side collection documented by each SDK.
  - fix: Remove fingerprinting code; replace or update SDKs that fingerprint.

---

## PRIV.G Required reason APIs — File timestamp (NSPrivacyAccessedAPICategoryFileTimestamp)

**Source text (verbatim):**
> NSPrivacyAccessedAPICategoryFileTimestamp
>
> The following APIs for accessing file timestamps require reasons for use.
> - creationDate
> - modificationDate
> - fileModificationDate
> - contentModificationDateKey
> - creationDateKey
> - `getattrlist(_:_:_:_:_:)`
> - `getattrlistbulk(_:_:_:_:_:)`
> - `fgetattrlist(_:_:_:_:_:)`
> - stat
> - `fstat(_:_:)`
> - `fstatat(_:_:_:_:)`
> - `lstat(_:_:)`
> - `getattrlistat(_:_:_:_:_:_:)`
>
> In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from this list.

| API (as Apple lists it) | Apple doc page / owner | Objective-C name (from the symbol’s Apple page) | Code search pattern (not Apple text) |
|---|---|---|---|
| creationDate | `FileAttributeKey.creationDate` (Foundation) | `NSFileCreationDate` | `\.creationDate\b\|FileAttributeKey\.creationDate\|NSFileCreationDate` |
| modificationDate | `FileAttributeKey.modificationDate` (Foundation) | `NSFileModificationDate` | `\.modificationDate\b\|FileAttributeKey\.modificationDate\|NSFileModificationDate` |
| fileModificationDate | `UIDocument.fileModificationDate` (UIKit) | `fileModificationDate` | `\bfileModificationDate\b` |
| contentModificationDateKey | `URLResourceKey.contentModificationDateKey` (Foundation) | `NSURLContentModificationDateKey` | `contentModificationDateKey\|contentModificationDate\b\|NSURLContentModificationDateKey` |
| creationDateKey | `URLResourceKey.creationDateKey` (Foundation) | `NSURLCreationDateKey` | `creationDateKey\|NSURLCreationDateKey` |
| `getattrlist(_:_:_:_:_:)` | C (Darwin) | `getattrlist` | `\bgetattrlist\s*\(` |
| `getattrlistbulk(_:_:_:_:_:)` | C (Darwin) | `getattrlistbulk` | `\bgetattrlistbulk\s*\(` |
| `fgetattrlist(_:_:_:_:_:)` | C (Darwin) | `fgetattrlist` | `\bfgetattrlist\s*\(` |
| stat | `stat` (kernel, `struct stat`) | `stat` | `\bstat\s*\(\|struct\s+stat\b` |
| `fstat(_:_:)` | C (Darwin) | `fstat` | `\bfstat\s*\(` |
| `fstatat(_:_:_:_:)` | C (Darwin) | `fstatat` | `\bfstatat\s*\(` |
| `lstat(_:_:)` | C (Darwin) | `lstat` | `\blstat\s*\(` |
| `getattrlistat(_:_:_:_:_:_:)` | C (Darwin) | `getattrlistat` | `\bgetattrlistat\s*\(` |

Approved reasons (complete, verbatim):

| Reason code | Exact wording |
|---|---|
| `DDA9.1` | Declare this reason to display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device. |
| `C617.1` | Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container. |
| `3B52.1` | Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller. |
| `0A2A.1` | Declare this reason if your third-party SDK is providing a wrapper function around file timestamp API(s) for the app to use, and you only access the file timestamp APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s). Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK. |

**Applies to:** Apps and third-party SDKs on iOS, iPadOS, tvOS, visionOS, or watchOS that call any API in the table above.

- **[PRIV-37]** If the code uses any file timestamp API, does the bundle’s privacy manifest declare `NSPrivacyAccessedAPICategoryFileTimestamp`?
  - quote: "The following APIs for accessing file timestamps require reasons for use."
  - surface: code
  - verify: `grep -rnE --include=*.swift --include=*.m --include=*.mm --include=*.h --include=*.c --include=*.cpp --include=*.cc '(FileAttributeKey\.)?\.(creationDate|modificationDate)\b|NSFileCreationDate|NSFileModificationDate|\bfileModificationDate\b|contentModificationDateKey|NSURLContentModificationDateKey|creationDateKey|NSURLCreationDateKey|\b(getattrlist|getattrlistbulk|fgetattrlist|getattrlistat|stat|fstat|fstatat|lstat)\s*\(|struct\s+stat\b' <target sources>`; discard hits that are not these Apple APIs (e.g. your own model property named `creationDate`); for confirmed hits, check the manifest for the category.
  - fix: Add `{NSPrivacyAccessedAPIType: NSPrivacyAccessedAPICategoryFileTimestamp, NSPrivacyAccessedAPITypeReasons: [<code>]}`.
- **[PRIV-38]** Are the declared File timestamp reasons only from `DDA9.1`, `C617.1`, `3B52.1`, `0A2A.1`?
  - quote: "In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from this list."
  - surface: code
  - verify: In the FileTimestamp dictionary, every reason string must be one of the four codes (exact match, including `.1`).
  - fix: Replace invalid codes with the code matching actual use.
- **[PRIV-39]** Is `0A2A.1` absent from the app target’s own manifest (it may only be declared by third-party SDKs)?
  - quote: "This reason may only be declared by third-party SDKs."
  - surface: code
  - verify: In the app (and app extension) target manifests, fail if `0A2A.1` appears.
  - fix: Replace with the reason that matches the app’s use (`DDA9.1`, `C617.1`, or `3B52.1`).
- **[PRIV-40]** If `DDA9.1` is declared, are the file timestamps (and derived information) only displayed to the user and never sent off-device?
  - quote: "Declare this reason to display file timestamps to the person using the device. Information accessed for this reason, or any derived information, may not be sent off-device."
  - surface: manual
  - verify: Trace each timestamp hit to its use; confirm it feeds UI only and is not included in network payloads, analytics events, or sync uploads.
  - fix: Stop sending the data off-device, or declare the reason that matches (`C617.1` / `3B52.1`) if applicable.
- **[PRIV-41]** If `C617.1` is declared, are the timestamp/metadata accesses limited to files inside the app container, app group container, or the app’s CloudKit container?
  - quote: "Declare this reason to access the timestamps, size, or other metadata of files inside the app container, app group container, or the app’s CloudKit container."
  - surface: code
  - verify: For each hit, confirm the URL/path passed comes from `FileManager.default.urls(for:in:)`, `NSHomeDirectory()`, `containerURL(forSecurityApplicationGroupIdentifier:)`, temporary directory, or CloudKit assets — not arbitrary system paths.
  - fix: Restrict the access to app/app-group/CloudKit container files, or declare `3B52.1` for user-granted files.
- **[PRIV-42]** If `3B52.1` is declared, are the accessed files/directories only those the user specifically granted access to (e.g. via a document picker)?
  - quote: "Declare this reason to access the timestamps, size, or other metadata of files or directories that the user specifically granted access to, such as using a document picker view controller."
  - surface: code
  - verify: Confirm the URLs come from `UIDocumentPickerViewController`, `.fileImporter`, `NSOpenPanel`, drag-and-drop, or security-scoped bookmarks the user created.
  - fix: Restrict to user-granted files or declare the matching reason.

---

## PRIV.H Required reason APIs — System boot time (NSPrivacyAccessedAPICategorySystemBootTime)

**Source text (verbatim):**
> NSPrivacyAccessedAPICategorySystemBootTime
>
> The following APIs for accessing the system boot time require reasons for use.
> - systemUptime
> - `mach_absolute_time()`
>
> In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

| API (as Apple lists it) | Apple doc page / owner | Objective-C name (from the symbol’s Apple page) | Code search pattern (not Apple text) |
|---|---|---|---|
| systemUptime | `ProcessInfo.systemUptime` (Foundation) | `systemUptime` (on `NSProcessInfo`) | `\bsystemUptime\b` |
| `mach_absolute_time()` | C (Darwin) | `mach_absolute_time` | `\bmach_absolute_time\s*\(` |

Approved reasons (complete, verbatim — wording from the NSPrivacyAccessedAPIType page):

| Reason code | Exact wording |
|---|---|
| `35F9.1` | Declare this reason to access the system boot time in order to measure the amount of time that has elapsed between events that occurred within the app or to perform calculations to enable timers. Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception for information about the amount of time that has elapsed between events that occurred within the app, which may be sent off-device. |
| `8FFB.1` | Declare this reason to access the system boot time to calculate absolute timestamps for events that occurred within your app, such as events related to the UIKit or AVFAudio frameworks. Absolute timestamps for events that occurred within your app may be sent off-device. System boot time accessed for this reason, or any other information derived from system boot time, may not be sent off-device. |
| `3D61.1` | Declare this reason to include system boot time information in an optional bug report that the person using the device chooses to submit. The system boot time information must be prominently displayed to the person as part of the report. Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including system boot time information, and only for the purpose of investigating or responding to the bug report. |

(The NSPrivacyAccessedAPITypeReasons page shows a shorter `3D61.1` text that ends after “…must be prominently displayed to the person as part of the report.” The longer text above is from the NSPrivacyAccessedAPIType page.)

**Applies to:** Apps and third-party SDKs on iOS, iPadOS, tvOS, visionOS, or watchOS that call `systemUptime` or `mach_absolute_time()`.

- **[PRIV-43]** If the code uses `systemUptime` or `mach_absolute_time()`, does the bundle’s manifest declare `NSPrivacyAccessedAPICategorySystemBootTime`?
  - quote: "The following APIs for accessing the system boot time require reasons for use."
  - surface: code
  - verify: `grep -rnE --include=*.swift --include=*.m --include=*.mm --include=*.h --include=*.c --include=*.cpp '\bsystemUptime\b|\bmach_absolute_time\s*\(' <target sources>`; for confirmed hits, check the manifest.
  - fix: Add `{NSPrivacyAccessedAPIType: NSPrivacyAccessedAPICategorySystemBootTime, NSPrivacyAccessedAPITypeReasons: [<code>]}`.
- **[PRIV-44]** Are the declared System boot time reasons only from `35F9.1`, `8FFB.1`, `3D61.1`?
  - quote: "In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below."
  - surface: code
  - verify: Every reason string in the SystemBootTime dictionary must be one of the three codes.
  - fix: Replace invalid codes.
- **[PRIV-45]** If `35F9.1` is declared, is boot time used only to measure elapsed time between in-app events or for timers, with nothing but elapsed in-app durations sent off-device?
  - quote: "Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception for information about the amount of time that has elapsed between events that occurred within the app, which may be sent off-device."
  - surface: manual
  - verify: Trace each hit: values must be used as differences (durations/timers); confirm the raw uptime value is not in any network payload.
  - fix: Send only elapsed durations, never raw uptime/boot time.
- **[PRIV-46]** If `8FFB.1` is declared, is boot time used only to compute absolute timestamps for in-app events, with boot time itself never sent off-device?
  - quote: "System boot time accessed for this reason, or any other information derived from system boot time, may not be sent off-device."
  - surface: manual
  - verify: Trace each hit; confirm only the computed absolute event timestamps (not uptime) leave the device.
  - fix: Remove raw boot time from payloads.
- **[PRIV-47]** If `3D61.1` is declared, is boot time only included in an optional, user-initiated bug report where it is prominently displayed to the user before sending?
  - quote: "The system boot time information must be prominently displayed to the person as part of the report."
  - surface: runtime
  - verify: Exercise the bug-report flow in the simulator: confirm it is optional, the boot-time info is visibly shown in the report, and nothing is sent until the user affirmatively submits.
  - fix: Display the info in the report UI and send only after explicit user submission.

---

## PRIV.I Required reason APIs — Disk space (NSPrivacyAccessedAPICategoryDiskSpace)

**Source text (verbatim):**
> NSPrivacyAccessedAPICategoryDiskSpace
>
> The following APIs for accessing the available disk space require reasons for use.
> - volumeAvailableCapacityKey
> - volumeAvailableCapacityForImportantUsageKey
> - volumeAvailableCapacityForOpportunisticUsageKey
> - volumeTotalCapacityKey
> - systemFreeSize
> - systemSize
> - `statfs(_:_:)`
> - `statvfs(_:_:)`
> - `fstatfs(_:_:)`
> - `fstatvfs(_:_:)`
> - `getattrlist(_:_:_:_:_:)`
> - `fgetattrlist(_:_:_:_:_:)`
> - `getattrlistat(_:_:_:_:_:_:)`
>
> In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

| API (as Apple lists it) | Apple doc page / owner | Objective-C name (from the symbol’s Apple page) | Code search pattern (not Apple text) |
|---|---|---|---|
| volumeAvailableCapacityKey | `URLResourceKey.volumeAvailableCapacityKey` (Foundation) | `NSURLVolumeAvailableCapacityKey` | `volumeAvailableCapacityKey\|volumeAvailableCapacity\b\|NSURLVolumeAvailableCapacityKey` |
| volumeAvailableCapacityForImportantUsageKey | `URLResourceKey.volumeAvailableCapacityForImportantUsageKey` (Foundation) | `NSURLVolumeAvailableCapacityForImportantUsageKey` | `volumeAvailableCapacityForImportantUsage(Key)?\|NSURLVolumeAvailableCapacityForImportantUsageKey` |
| volumeAvailableCapacityForOpportunisticUsageKey | `URLResourceKey.volumeAvailableCapacityForOpportunisticUsageKey` (Foundation) | `NSURLVolumeAvailableCapacityForOpportunisticUsageKey` | `volumeAvailableCapacityForOpportunisticUsage(Key)?\|NSURLVolumeAvailableCapacityForOpportunisticUsageKey` |
| volumeTotalCapacityKey | `URLResourceKey.volumeTotalCapacityKey` (Foundation) | `NSURLVolumeTotalCapacityKey` | `volumeTotalCapacity(Key)?\|NSURLVolumeTotalCapacityKey` |
| systemFreeSize | `FileAttributeKey.systemFreeSize` (Foundation) | `NSFileSystemFreeSize` | `\.systemFreeSize\b\|NSFileSystemFreeSize` |
| systemSize | `FileAttributeKey.systemSize` (Foundation) | `NSFileSystemSize` | `\.systemSize\b\|NSFileSystemSize\b` |
| `statfs(_:_:)` | C (Darwin) | `statfs` | `\bstatfs\s*\(\|struct\s+statfs\b` |
| `statvfs(_:_:)` | C (Darwin) | `statvfs` | `\bstatvfs\s*\(\|struct\s+statvfs\b` |
| `fstatfs(_:_:)` | C (Darwin) | `fstatfs` | `\bfstatfs\s*\(` |
| `fstatvfs(_:_:)` | C (Darwin) | `fstatvfs` | `\bfstatvfs\s*\(` |
| `getattrlist(_:_:_:_:_:)` | C (Darwin) | `getattrlist` | `\bgetattrlist\s*\(` |
| `fgetattrlist(_:_:_:_:_:)` | C (Darwin) | `fgetattrlist` | `\bfgetattrlist\s*\(` |
| `getattrlistat(_:_:_:_:_:_:)` | C (Darwin) | `getattrlistat` | `\bgetattrlistat\s*\(` |

(`getattrlist`, `fgetattrlist` and `getattrlistat` appear in both the File timestamp and Disk space categories.)

Approved reasons (complete, verbatim):

| Reason code | Exact wording |
|---|---|
| `85F4.1` | Declare this reason to display disk space information to the person using the device. Disk space may be displayed in units of information (such as bytes) or units of time combined with a media type (such as minutes of HD video). Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to send disk space information over the local network to another device operated by the same person only for the purpose of displaying disk space information on that device; this exception only applies if the user has provided explicit permission to send disk space information, and the information may not be sent over the Internet. |
| `E174.1` | Declare this reason to check whether there is sufficient disk space to write files, or to check whether the disk space is low so that the app can delete files when the disk space is low. The app must behave differently based on disk space in a way that is observable to users. Information accessed for this reason, or any derived information, may not be sent off-device. There is an exception that allows the app to avoid downloading files from a server when disk space is insufficient. |
| `7D9E.1` | Declare this reason to include disk space information in an optional bug report that the person using the device chooses to submit. The disk space information must be prominently displayed to the person as part of the report. Information accessed for this reason, or any derived information, may be sent off-device only after the user affirmatively chooses to submit the specific bug report including disk space information, and only for the purpose of investigating or responding to the bug report. |
| `B728.1` | Declare this reason if your app is a health research app, and you access this API category to detect and inform research participants about low disk space impacting the research data collection. Your app must comply with App Store Review Guideline §5.1.3. Your app must not offer any functionality other than providing information about and allowing people to participate in health research. |

**Applies to:** Apps and third-party SDKs on iOS, iPadOS, tvOS, visionOS, or watchOS that call any API in the table above.

- **[PRIV-48]** If the code uses any disk space API, does the bundle’s manifest declare `NSPrivacyAccessedAPICategoryDiskSpace`?
  - quote: "The following APIs for accessing the available disk space require reasons for use."
  - surface: code
  - verify: `grep -rnE --include=*.swift --include=*.m --include=*.mm --include=*.h --include=*.c --include=*.cpp 'volumeAvailableCapacity(ForImportantUsage|ForOpportunisticUsage)?(Key)?\b|NSURLVolumeAvailableCapacity(ForImportantUsage|ForOpportunisticUsage)?Key|volumeTotalCapacity(Key)?\b|NSURLVolumeTotalCapacityKey|\.systemFreeSize\b|NSFileSystemFreeSize|\.systemSize\b|NSFileSystemSize\b|\b(statfs|statvfs|fstatfs|fstatvfs|getattrlist|fgetattrlist|getattrlistat)\s*\(' <target sources>`; confirm hits, then check the manifest.
  - fix: Add `{NSPrivacyAccessedAPIType: NSPrivacyAccessedAPICategoryDiskSpace, NSPrivacyAccessedAPITypeReasons: [<code>]}`.
- **[PRIV-49]** Are the declared Disk space reasons only from `85F4.1`, `E174.1`, `7D9E.1`, `B728.1`?
  - quote: "In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below."
  - surface: code
  - verify: Every reason string in the DiskSpace dictionary must be one of the four codes.
  - fix: Replace invalid codes.
- **[PRIV-50]** If `85F4.1` is declared, is disk space only displayed to the user and not sent off-device (except local-network display to the same person’s device with explicit permission)?
  - quote: "Declare this reason to display disk space information to the person using the device."
  - surface: manual
  - verify: Trace hits to UI; confirm no network payload contains disk space values except a permitted local-network display flow with explicit user permission and no Internet transfer.
  - fix: Remove off-device transmission or add explicit permission and restrict to local network display.
- **[PRIV-51]** If `E174.1` is declared, does the app visibly behave differently based on disk space (e.g. warns, skips writing, deletes cached files), without sending disk space off-device?
  - quote: "The app must behave differently based on disk space in a way that is observable to users."
  - surface: runtime
  - verify: Read the code branch after each disk-space check; in the simulator, exercise the low-space path (e.g. mock the value) and confirm a user-observable effect; confirm the value is not sent to a server.
  - fix: Add user-observable behavior for the low-space condition, or declare the reason matching actual use.
- **[PRIV-52]** If `7D9E.1` is declared, is disk space only included in an optional, user-submitted bug report where it is prominently displayed?
  - quote: "The disk space information must be prominently displayed to the person as part of the report."
  - surface: runtime
  - verify: Exercise the bug-report flow; confirm the disk space info is visible in the report and sent only after the user affirmatively submits.
  - fix: Display the info in the report UI; send only on explicit submission.
- **[PRIV-53]** If `B728.1` is declared, is the app a health research app that complies with Guideline 5.1.3 and offers no other functionality?
  - quote: "Your app must not offer any functionality other than providing information about and allowing people to participate in health research."
  - surface: manual
  - verify: Confirm with the developer the app is solely a health research app; review the app’s feature set.
  - fix: Remove `B728.1` and declare the reason matching actual use (e.g. `E174.1`), or manual — requires developer decision/legal/business action.

---

## PRIV.J Required reason APIs — Active keyboards (NSPrivacyAccessedAPICategoryActiveKeyboards)

**Source text (verbatim):**
> NSPrivacyAccessedAPICategoryActiveKeyboards
>
> The following API for accessing the list of active keyboards requires reasons for use.
> - activeInputModes
>
> In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below.

| API (as Apple lists it) | Apple doc page / owner | Objective-C name (from the symbol’s Apple page) | Code search pattern (not Apple text) |
|---|---|---|---|
| activeInputModes | `UITextInputMode.activeInputModes` (UIKit) | `activeInputModes` (on `UITextInputMode`) | `\bactiveInputModes\b` |

Approved reasons (complete, verbatim):

| Reason code | Exact wording |
|---|---|
| `3EC4.1` | Declare this reason if your app is a custom keyboard app, and you access this API category to determine the keyboards that are active on the device. Providing a systemwide custom keyboard to the user must be the primary functionality of the app. Information accessed for this reason, or any derived information, may not be sent off-device. |
| `54BD.1` | Declare this reason to access active keyboard information to present the correct customized user interface to the person using the device. The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users. Information accessed for this reason, or any derived information, may not be sent off-device. |

**Applies to:** Apps and third-party SDKs on iOS, iPadOS, tvOS, visionOS, or watchOS that access `activeInputModes`.

- **[PRIV-54]** If the code uses `activeInputModes`, does the bundle’s manifest declare `NSPrivacyAccessedAPICategoryActiveKeyboards`?
  - quote: "The following API for accessing the list of active keyboards requires reasons for use."
  - surface: code
  - verify: `grep -rnE --include=*.swift --include=*.m --include=*.mm --include=*.h '\bactiveInputModes\b' <target sources>`; for hits, check the manifest.
  - fix: Add `{NSPrivacyAccessedAPIType: NSPrivacyAccessedAPICategoryActiveKeyboards, NSPrivacyAccessedAPITypeReasons: [<code>]}`.
- **[PRIV-55]** Are the declared Active keyboards reasons only from `3EC4.1`, `54BD.1`?
  - quote: "In your NSPrivacyAccessedAPITypeReasons array, supply the relevant values from the list below."
  - surface: code
  - verify: Every reason string in the ActiveKeyboards dictionary must be `3EC4.1` or `54BD.1`.
  - fix: Replace invalid codes.
- **[PRIV-56]** If `3EC4.1` is declared, is providing a systemwide custom keyboard the primary functionality of the app (a keyboard extension exists)?
  - quote: "Providing a systemwide custom keyboard to the user must be the primary functionality of the app."
  - surface: code
  - verify: Confirm a target with `NSExtensionPointIdentifier` = `com.apple.keyboard-service` exists in an extension Info.plist; confirm with the developer it is the app’s primary function.
  - fix: Declare `54BD.1` if that matches, or remove the API use.
- **[PRIV-57]** If `54BD.1` is declared, does the app have text fields and visibly change its UI based on the active keyboards, without sending keyboard info off-device?
  - quote: "The app must have text fields for entering or editing text and must behave differently based on active keyboards in a way that is observable to users."
  - surface: runtime
  - verify: Read the code after each `activeInputModes` hit for a UI change; run the app with different keyboards enabled and observe the difference; confirm no network payload includes keyboard info.
  - fix: Make the behavior user-observable or remove the API use; stop any off-device transmission.

---

## PRIV.K Required reason APIs — User defaults (NSPrivacyAccessedAPICategoryUserDefaults)

**Source text (verbatim):**
> NSPrivacyAccessedAPICategoryUserDefaults
>
> The following API for accessing user defaults requires reasons for use.
> - UserDefaults
>
> In your `NSPrivacyAccessedAPITypeReasons` array, supply the relevant values from the list below.

| API (as Apple lists it) | Apple doc page / owner | Objective-C name (from the symbol’s Apple page) | Code search pattern (not Apple text) |
|---|---|---|---|
| UserDefaults | `UserDefaults` (Foundation) | `NSUserDefaults` | `\bUserDefaults\b\|\bNSUserDefaults\b\|@AppStorage\b` |

(`@AppStorage` is included in the search pattern because Apple’s SwiftUI documentation describes `AppStorage` as “A property wrapper type that reflects a value from `UserDefaults` and invalidates a view on a change in value in that user default.” — https://developer.apple.com/documentation/swiftui/appstorage)

Approved reasons (complete, verbatim):

| Reason code | Exact wording |
|---|---|
| `CA92.1` | Declare this reason to access user defaults to read and write information that is only accessible to the app itself. This reason does not permit reading information that was written by other apps or the system, or writing information that can be accessed by other apps. |
| `1C8F.1` | Declare this reason to access user defaults to read and write information that is only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself. This reason does not permit reading information that was written by apps, app extensions, or App Clips outside the same App Group or by the system. Your app is not responsible if the system provides information from the global domain because a key is not present in your requested domain while your app is attempting to read information that apps, app extensions, or App Clips in your app’s App Group write. This reason also does not permit writing information that can be accessed by apps, app extensions, or App Clips outside the same App Group. |
| `C56D.1` | Declare this reason if your third-party SDK is providing a wrapper function around user defaults API(s) for the app to use, and you only access the user defaults APIs when the app calls your wrapper function. This reason may only be declared by third-party SDKs. This reason may not be declared if your third-party SDK was created primarily to wrap required reason API(s). Information accessed for this reason, or any derived information, may not be used for your third-party SDK’s own purposes or sent off-device by your third-party SDK. |
| `AC6B.1` | Declare this reason to access user defaults to read the `com.apple.configuration.managed` key to retrieve the managed app configuration set by MDM, or to set the `com.apple.feedback.managed` key to store feedback information to be queried over MDM, as described in the Apple Mobile Device Management Protocol Reference documentation. |

**Applies to:** Apps and third-party SDKs on iOS, iPadOS, tvOS, visionOS, or watchOS that access `UserDefaults`.

- **[PRIV-58]** If the code uses `UserDefaults`, does the bundle’s manifest declare `NSPrivacyAccessedAPICategoryUserDefaults`? (The search also flags `@AppStorage`, which Apple documents as reflecting a value from `UserDefaults`; confirm each hit.)
  - quote: "The following API for accessing user defaults requires reasons for use."
  - surface: code
  - verify: `grep -rnE --include=*.swift --include=*.m --include=*.mm --include=*.h '\bUserDefaults\b|\bNSUserDefaults\b|@AppStorage\b' <target sources>` (run per target, including widgets/extensions); for hits, check that target bundle’s manifest.
  - fix: Add `{NSPrivacyAccessedAPIType: NSPrivacyAccessedAPICategoryUserDefaults, NSPrivacyAccessedAPITypeReasons: [<code>]}`.
- **[PRIV-59]** Are the declared User defaults reasons only from `CA92.1`, `1C8F.1`, `C56D.1`, `AC6B.1`?
  - quote: "In your `NSPrivacyAccessedAPITypeReasons` array, supply the relevant values from the list below."
  - surface: code
  - verify: Every reason string in the UserDefaults dictionary must be one of the four codes.
  - fix: Replace invalid codes.
- **[PRIV-60]** If the app uses `UserDefaults(suiteName:)` with an App Group identifier (or `@AppStorage(..., store: UserDefaults(suiteName:))`), does the declared reason accurately reflect that App Group access (Apple’s `1C8F.1` reason covers it)?
  - quote: "Declare this reason to access user defaults to read and write information that is only accessible to the apps, app extensions, and App Clips that are members of the same App Group as the app itself."
  - surface: code
  - verify: `grep -rnE 'UserDefaults\s*\(\s*suiteName:|initWithSuiteName:' <sources>`; compare the suite name to `com.apple.security.application-groups` in the `.entitlements` files; if it is an app group, the declared reasons must accurately reflect that use (PRIV-34); `1C8F.1` is the reason whose wording covers App Group access.
  - fix: Add `1C8F.1` to the UserDefaults reasons.
- **[PRIV-61]** If `CA92.1` is declared, does the code avoid reading defaults written by other apps or the system (e.g. reading `AppleLanguages`, `AppleLocale`, or other global-domain keys) and avoid writing data readable by other apps?
  - quote: "This reason does not permit reading information that was written by other apps or the system, or writing information that can be accessed by other apps."
  - surface: code
  - verify: Grep for `UserDefaults.standard.(object|string|array|value)\(forKey:` / `objectForKey:` with keys not written by the app itself (e.g. `"AppleLanguages"`, `"AppleLocale"`, `"AppleKeyboards"`); list them for developer review.
  - fix: Remove reads of system/other-app keys, or declare the reason that matches the actual use.
- **[PRIV-62]** Is `C56D.1` absent from the app target’s own manifest (it may only be declared by third-party SDKs)?
  - quote: "This reason may only be declared by third-party SDKs."
  - surface: code
  - verify: In app/app-extension target manifests, fail if `C56D.1` appears.
  - fix: Replace with `CA92.1` and/or `1C8F.1` as appropriate.
- **[PRIV-63]** If `AC6B.1` is declared, does the code actually read `com.apple.configuration.managed` or set `com.apple.feedback.managed`?
  - quote: "Declare this reason to access user defaults to read the `com.apple.configuration.managed` key to retrieve the managed app configuration set by MDM, or to set the `com.apple.feedback.managed` key"
  - surface: code
  - verify: `grep -rn 'com.apple.configuration.managed\|com.apple.feedback.managed' <sources>`; if `AC6B.1` is declared and there are no hits, fail.
  - fix: Remove `AC6B.1` if the app does not use MDM managed configuration.

---

## PRIV.L TN3181 — Debugging an invalid privacy manifest (accessed API values and plist validation)

**Source text (verbatim):**
> Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
>
> Starting November 12, 2024, apps you submit for review in App Store Connect must contain a valid privacy manifest file. If you upload an app to App Store Connect that contains invalid privacy manifest files, you’ll receive an email that includes the name and path of the invalid files in your app bundle. For example:
> ```
> ITMS-91056: Invalid privacy manifest - The PrivacyInfo.xcprivacy file from the following path
> is invalid: "PrivacyInfo.xcprivacy". Keys and values in your app's privacy manifests must be
> valid. For more details about privacy manifest files, visit:
> https://developer.apple.com/documentation/bundleresources/privacy_manifest_files.
> ```
> An invalid privacy manifest is:
> - A property list file that contains invalid keys or values.
> - An improperly formatted property list file.
>
> Review Privacy manifest files to learn about the keys you can include in a privacy manifest. This document lists possible reasons for invalid privacy tracking and accessed API values in your privacy manifest. Validate your privacy manifest to determine why your privacy manifest is malformed.
>
> **Possible reasons for an invalid accessed API type value**
>
> The following table lists reasons why a value for the `NSPrivacyAccessedAPIType` key is invalid:
>
> **Possible reasons for an invalid accessed API type reasons value**
>
> The following table lists reasons why a value for the `NSPrivacyAccessedAPITypeReasons` key is invalid:
>
> Note: If your app or third-party SDK doesn’t use, or no longer uses a specific required reason API, remove its related dictionary from the `NSPrivacyAccessedAPITypes` key. If `NSPrivacyAccessedAPITypes` is empty, remove it from the privacy manifest.
>
> **Possible reasons for an invalid accessed API types value**
>
> The following table lists reasons why a value for the `NSPrivacyAccessedAPITypes` key is invalid:
>
> **Validate your privacy manifest file**
>
> You can use the `plutil` command to ensure your privacy manifest is a properly formatted plist file. To validate your privacy manifest, run `plutil` with the `-lint` option in Terminal:
> ```
> % plutil -lint /path/to/PrivacyInfo.xcprivacy
> ```
> If the privacy manifest is a valid plist, the command prints a message similar to the following:
> ```
> % plutil -lint PrivacyInfo.xcprivacy
> ~/Documents/SampleApp/PrivacyInfo.xcprivacy: OK
> ```
> If the privacy manifest is malformed, an error message appears in Terminal:
> ```
> % plutil -lint PrivacyInfo.xcprivacy
> ~/Documents/SampleApp/PrivacyInfo.xcprivacy: Encountered unexpected character
> `a` on line 8 while looking for close tag
> ```
> To fix the errors, open your privacy manifest in a text editor or Xcode to address them.
>
> Note: If your privacy manifest is a valid plist, check its keys and values. Your privacy manifest could still be invalid if its keys and values don’t match the values App Store Connect expects. For more information about the keys and values App Store Connect expects, see Privacy manifest files.

`NSPrivacyAccessedAPIType` invalid values (verbatim):

| Reason | Solution |
|---|---|
| The value is any other type than a string. | Change the type of the `NSPrivacyAccessedAPIType` key to `String` in your privacy manifest. |
| The value is an empty string, or a string whose value doesn’t match a category of required reason APIs. | Set the value of the `NSPrivacyAccessedAPIType` key to a string that exactly matches a category of required reason APIs your app uses. For possible values, see Describing use of required reason API. |

`NSPrivacyAccessedAPITypeReasons` invalid values (verbatim):

| Reason | Solution |
|---|---|
| The value is any other type than an array of strings. | Change the type of the `NSPrivacyAccessedAPITypeReasons` key to `Array` in your privacy manifest. |
| The value is an empty array of strings. | In the dictionary that contains the `NSPrivacyAccessedAPITypeReasons` key, check the value of the `NSPrivacyAccessedAPIType` key. Add one or more reason strings to the array whose value exactly matches a value associated with `NSPrivacyAccessedAPIType`. |
| The value is an array of strings, but some entries don’t match the expected values for the `NSPrivacyAccessedAPIType` key you provide. | In the dictionary that contains the `NSPrivacyAccessedAPITypeReasons` key, check the value of the `NSPrivacyAccessedAPIType` key. Confirm each reason string in the array exactly matches a value associated with `NSPrivacyAccessedAPIType`. |

`NSPrivacyAccessedAPITypes` invalid values (verbatim):

| Reason | Solution |
|---|---|
| The value is any other type than an array of dictionaries. | Change the type of the `NSPrivacyAccessedAPITypes` key to `Array` in your privacy manifest. |
| The value is an empty array of dictionaries. | Create a dictionary that includes information about a required reason API your app or third-party SDK uses, then add the dictionary to the array. Repeat the process for all required reason APIs your app or third-party SDK uses. |
| The value is an array of dictionaries, but some of the dictionaries are invalid. | Confirm each dictionary in the array contains a `NSPrivacyAccessedAPIType` key and a `NSPrivacyAccessedAPITypeReasons` key, and both keys contain valid values. |

**Applies to:** All apps submitted for review in App Store Connect that contain privacy manifest files.

- **[PRIV-64]** Does `plutil -lint` report `OK` for every `PrivacyInfo.xcprivacy` in the project and in the built app?
  - quote: "You can use the `plutil` command to ensure your privacy manifest is a properly formatted plist file."
  - surface: code
  - verify: `find . <built .app> -name PrivacyInfo.xcprivacy -not -path '*/DerivedData/*' -print0 | xargs -0 -n1 plutil -lint`; every line must end with `: OK`.
  - fix: Open the file in Xcode or a text editor and correct the malformed XML reported by `plutil`.
- **[PRIV-65]** Is every `NSPrivacyAccessedAPIType` value a non-empty string exactly matching one of the five category values?
  - quote: "The value is an empty string, or a string whose value doesn’t match a category of required reason APIs."
  - surface: code
  - verify: Dump with `plutil -convert json -o - PrivacyInfo.xcprivacy`; each `NSPrivacyAccessedAPIType` must be a JSON string equal to one of: `NSPrivacyAccessedAPICategoryFileTimestamp`, `NSPrivacyAccessedAPICategorySystemBootTime`, `NSPrivacyAccessedAPICategoryDiskSpace`, `NSPrivacyAccessedAPICategoryActiveKeyboards`, `NSPrivacyAccessedAPICategoryUserDefaults`.
  - fix: Set the value to the exact category string your app uses.
- **[PRIV-66]** Is every `NSPrivacyAccessedAPITypeReasons` a non-empty array of strings whose entries all belong to the paired category’s reason list?
  - quote: "The value is an array of strings, but some entries don’t match the expected values for the `NSPrivacyAccessedAPIType` key you provide."
  - surface: code
  - verify: For each dictionary, look up the category’s allowed codes (FileTimestamp: DDA9.1, C617.1, 3B52.1, 0A2A.1; SystemBootTime: 35F9.1, 8FFB.1, 3D61.1; DiskSpace: 85F4.1, E174.1, 7D9E.1, B728.1; ActiveKeyboards: 3EC4.1, 54BD.1; UserDefaults: CA92.1, 1C8F.1, C56D.1, AC6B.1); fail on empty arrays, non-string entries, or codes from another category.
  - fix: Add one or more reason strings that exactly match a value associated with the category; remove mismatched codes.
- **[PRIV-67]** If present, is `NSPrivacyAccessedAPITypes` a non-empty array of dictionaries, each with both `NSPrivacyAccessedAPIType` and `NSPrivacyAccessedAPITypeReasons`?
  - quote: "Confirm each dictionary in the array contains a `NSPrivacyAccessedAPIType` key and a `NSPrivacyAccessedAPITypeReasons` key, and both keys contain valid values."
  - surface: code
  - verify: JSON dump; `NSPrivacyAccessedAPITypes` must be an array; if empty, fail (remove it); each element must be a dict containing both keys.
  - fix: Add the missing key to each dictionary, or if no required reason API is used, remove the empty `NSPrivacyAccessedAPITypes` key.
- **[PRIV-68]** Are dictionaries for required reason APIs the app no longer uses removed from `NSPrivacyAccessedAPITypes`?
  - quote: "If your app or third-party SDK doesn’t use, or no longer uses a specific required reason API, remove its related dictionary from the `NSPrivacyAccessedAPITypes` key."
  - surface: code
  - verify: For each declared category in a first-party manifest, confirm the PRIV.G–PRIV.K search for that category has at least one confirmed hit in that target.
  - fix: Remove the dictionary for unused categories; if the array becomes empty, remove the key.

---

## PRIV.M TN3183 — Required reason API entry structure

**Source text (verbatim):**
> Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
>
> When you build an app or third-party SDK that uses any required reason API, perform these steps in your privacy manifest (`PrivacyInfo.xcprivacy`):
> - 1. Add the `NSPrivacyAccessedAPITypes` key and set its value to the dictionary.
> - 2. For each required reason API your app or third-party SDK uses, add a dictionary as a value for the `NSPrivacyAccessedAPITypes` key. The dictionary includes the category of the reason API and a list of reasons for using this API. For more information, see Add an accessed API type and reasons dictionary.
>
> Note: Before you start adding the keys to your privacy manifest, enable raw keys and values in Xcode to view the raw keys and hide their human-readable names. Click anywhere in the privacy manifest, then choose Xcode > Editor > Raw Keys and Values. Repeat the process to disable this feature.
>
> **Select an accessed API category**
>
> A privacy accessed API category identifies the category of required reason APIs your app or third-party SDK uses. Set the value of the `NSPrivacyAccessedAPIType` key to a privacy accessed API category. For more information, see Describing use of required reason API.
>
> The possible values of a privacy accessed API category are:
> - `NSPrivacyAccessedAPICategoryActiveKeyboards`
> - `NSPrivacyAccessedAPICategoryDiskSpace`
> - `NSPrivacyAccessedAPICategoryFileTimestamp`
> - `NSPrivacyAccessedAPICategorySystemBootTime`
> - `NSPrivacyAccessedAPICategoryUserDefaults`
>
> Each `NS_PRIVACY_ACCESSED_API_TYPE_REASON_VALUE` string in the array identifies a reason why your app or third-party SDK uses a required reason API. All the values in the array are associated with a `NSPrivacyAccessedAPIType` key you provide when you create a privacy accessed API type and reasons dictionary.
>
> **Add an accessed API type and reasons dictionary**
>
> A privacy accessed API type and reasons dictionary includes a category of required reason APIs and a list of related reasons. The dictionary contains exactly two keys: `NSPrivacyAccessedAPIType` and `NSPrivacyAccessedAPITypeReasons`.
>
> The `NSPrivacyAccessedAPITypes` key is an array of privacy accessed API type and reasons dictionaries.

TN3183 example (verbatim):
```
<plist>
<dict>
    <key>NSPrivacyAccessedAPITypes</key>
    <array>
        <!-- Declares disk space required reason API in the `Sample` app. -->
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategoryDiskSpace</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>B728.1</string>
                <string>E174.1</string>
            </array>
        </dict>
        <!-- Declares user defaults required reason APIs in the `Sample` app. -->
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>CA92.1</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
```

**Applies to:** Apps and third-party SDKs that use any required reason API.

- **[PRIV-69]** Does each `NSPrivacyAccessedAPITypes` dictionary contain exactly two keys, `NSPrivacyAccessedAPIType` and `NSPrivacyAccessedAPITypeReasons`, and nothing else?
  - quote: "The dictionary contains exactly two keys: `NSPrivacyAccessedAPIType` and `NSPrivacyAccessedAPITypeReasons`."
  - surface: code
  - verify: JSON dump; for each element of `NSPrivacyAccessedAPITypes`, the set of keys must equal `{NSPrivacyAccessedAPIType, NSPrivacyAccessedAPITypeReasons}`.
  - fix: Remove extra keys (e.g. comments stored as keys, `NSPrivacyAccessedAPITypeReason` typos) and add any missing one.
- **[PRIV-70]** Are all reasons in each dictionary associated with that dictionary’s own `NSPrivacyAccessedAPIType` (no cross-category codes)?
  - quote: "All the values in the array are associated with a `NSPrivacyAccessedAPIType` key you provide when you create a privacy accessed API type and reasons dictionary."
  - surface: code
  - verify: Same as PRIV-66 per dictionary (e.g. `CA92.1` inside a DiskSpace dictionary fails).
  - fix: Move each code into the dictionary for its category.

---

## PRIV.N TN3184 — Collected data entry structure

**Source text (verbatim):**
> Declare the data your app or third-party SDK collects in a privacy manifest.
>
> When you build an app or third-party SDK that collects any data type, perform these steps in your privacy manifest (`PrivacyInfo.xcprivacy`):
> - 1. Add the `NSPrivacyCollectedDataTypes` key.
> - 2. For each data type your app or third-party SDK collects, add a dictionary as a value for the `NSPrivacyCollectedDataTypes` key. The dictionary includes the data type, the data linked to the user and tracking status, and a list of reasons for collecting this data type. For more information, see Add a collected data type and reasons dictionary.
>
> **Add a collected data type and reasons dictionary**
>
> A privacy collected data type and reasons dictionary includes a data type, a data linked to the user status, a tracking status, and a list of reasons for collecting this data type. The dictionary contains exactly four keys: `NSPrivacyCollectedDataType`, `NSPrivacyCollectedDataTypeLinked`, `NSPrivacyCollectedDataTypeTracking`, and `NSPrivacyCollectedDataTypePurposes`. It uses the following format:
> ```
> <dict>
>     <!-- Add a privacy collected data type key. -->
>     <key>NSPrivacyCollectedDataType</key>
>     <string>NS_PRIVACY_COLLECTED_DATA_TYPE_VALUE</string>
>
>     <!-- Add a privacy collected data type linked key. -->
>     <key>NSPrivacyCollectedDataTypeLinked</key>
>     <false/>
>
>     <!-- Add a privacy collected data type tracking key. -->
>     <key>NSPrivacyCollectedDataTypeTracking</key>
>     <false/>
>
>     <!-- Add a privacy collected data type purposes key. -->
>     <key>NSPrivacyCollectedDataTypePurposes</key>
>     <array>
>         <string>NS_PRIVACY_COLLECTED_DATA_TYPE_PURPOSE_VALUE</string>
>         ...
>     </array>
> </dict>
> ```
> The `NSPrivacyCollectedDataTypes` key is an array of privacy collected data type and reasons dictionaries.

**Applies to:** Apps and third-party SDKs that collect any data type.

- **[PRIV-71]** Does each `NSPrivacyCollectedDataTypes` dictionary contain exactly the four keys `NSPrivacyCollectedDataType`, `NSPrivacyCollectedDataTypeLinked`, `NSPrivacyCollectedDataTypeTracking`, `NSPrivacyCollectedDataTypePurposes`?
  - quote: "The dictionary contains exactly four keys: `NSPrivacyCollectedDataType`, `NSPrivacyCollectedDataTypeLinked`, `NSPrivacyCollectedDataTypeTracking`, and `NSPrivacyCollectedDataTypePurposes`."
  - surface: code
  - verify: JSON dump; each element’s key set must equal the four keys; `Linked`/`Tracking` must be Booleans; `NSPrivacyCollectedDataType` a string; `NSPrivacyCollectedDataTypePurposes` an array of strings.
  - fix: Add missing keys / remove extra keys / correct value types.
- **[PRIV-72]** Is `NSPrivacyCollectedDataTypes` an array (of dictionaries)?
  - quote: "The `NSPrivacyCollectedDataTypes` key is an array of privacy collected data type and reasons dictionaries."
  - surface: code
  - verify: The value after `<key>NSPrivacyCollectedDataTypes</key>` must be `<array>` whose children are `<dict>`.
  - fix: Change the type to Array and wrap each entry in a dictionary.

---

## PRIV.O Third-party SDK requirements — SDKs that require a privacy manifest and signature

**Source text (verbatim):**
> Third-party software development kits (SDKs) can provide great functionality for apps; they can also have the potential to impact user privacy in ways that aren’t obvious to developers and users. As a reminder, when you use a third-party SDK with your app, you are responsible for all the code the SDK includes in your app, and need to be aware of its data collection and use practices. At WWDC23, we introduced new privacy manifests and signatures for SDKs to help bring more awareness for how third-party SDKs use data. This functionality is a step forward for all apps, and we encourage all SDKs to adopt it to better support the apps that depend on them.
>
> **Privacy Manifests**
>
> Privacy manifest files outline the privacy practices of the third-party code in an app, in a single standard format. When you prepare to distribute your app, Xcode will combine the privacy manifests across all the third-party SDKs used by your app into a single, easy-to-use report. With one comprehensive report that summarizes all the third-party SDKs found in an app, it will be even easier for you to create more accurate Privacy Nutrition Labels.
>
> **Signatures for SDKs**
>
> When you adopt a new version of a third-party SDK in your app, Xcode will validate that it was signed by the same developer, improving the integrity of your software supply chain.
>
> **SDKs that require a privacy manifest and signature**
>
> The following are commonly used SDKs in apps on the App Store. You must include the privacy manifest for any SDK listed below when you submit new apps in App Store Connect that include those SDKs, or when you submit an app update that adds one of the listed SDKs as part of the update. Signatures are also required in these cases where the listed SDKs are used as binary dependencies. Any version of a listed SDK, as well as any SDKs that repackage those on the list, are included in the requirement.

Complete list (86 entries, verbatim, in Apple’s order):

| # | SDK |
|---|---|
| 1 | Abseil |
| 2 | AFNetworking |
| 3 | Alamofire |
| 4 | AppAuth |
| 5 | BoringSSL / openssl_grpc |
| 6 | Capacitor |
| 7 | Charts |
| 8 | connectivity_plus |
| 9 | Cordova |
| 10 | device_info_plus |
| 11 | DKImagePickerController |
| 12 | DKPhotoGallery |
| 13 | FBAEMKit |
| 14 | FBLPromises |
| 15 | FBSDKCoreKit |
| 16 | FBSDKCoreKit_Basics |
| 17 | FBSDKLoginKit |
| 18 | FBSDKShareKit |
| 19 | file_picker |
| 20 | FirebaseABTesting |
| 21 | FirebaseAuth |
| 22 | FirebaseCore |
| 23 | FirebaseCoreDiagnostics |
| 24 | FirebaseCoreExtension |
| 25 | FirebaseCoreInternal |
| 26 | FirebaseCrashlytics |
| 27 | FirebaseDynamicLinks |
| 28 | FirebaseFirestore |
| 29 | FirebaseInstallations |
| 30 | FirebaseMessaging |
| 31 | FirebaseRemoteConfig |
| 32 | Flutter |
| 33 | flutter_inappwebview |
| 34 | flutter_local_notifications |
| 35 | fluttertoast |
| 36 | FMDB |
| 37 | geolocator_apple |
| 38 | GoogleDataTransport |
| 39 | GoogleSignIn |
| 40 | GoogleToolboxForMac |
| 41 | GoogleUtilities |
| 42 | grpcpp |
| 43 | GTMAppAuth |
| 44 | GTMSessionFetcher |
| 45 | hermes |
| 46 | image_picker_ios |
| 47 | IQKeyboardManager |
| 48 | IQKeyboardManagerSwift |
| 49 | Kingfisher |
| 50 | leveldb |
| 51 | Lottie |
| 52 | MBProgressHUD |
| 53 | nanopb |
| 54 | OneSignal |
| 55 | OneSignalCore |
| 56 | OneSignalExtension |
| 57 | OneSignalOutcomes |
| 58 | OpenSSL |
| 59 | OrderedSet |
| 60 | package_info |
| 61 | package_info_plus |
| 62 | path_provider |
| 63 | path_provider_ios |
| 64 | Promises |
| 65 | Protobuf |
| 66 | Reachability |
| 67 | RealmSwift |
| 68 | RxCocoa |
| 69 | RxRelay |
| 70 | RxSwift |
| 71 | SDWebImage |
| 72 | share_plus |
| 73 | shared_preferences_ios |
| 74 | SnapKit |
| 75 | sqflite |
| 76 | Starscream |
| 77 | SVProgressHUD |
| 78 | SwiftyGif |
| 79 | SwiftyJSON |
| 80 | Toast |
| 81 | UnityFramework |
| 82 | url_launcher |
| 83 | url_launcher_ios |
| 84 | video_player_avfoundation |
| 85 | wakelock |
| 86 | webview_flutter_wkwebview |

Related date (from “Adding a privacy manifest to your app or third-party SDK”, verbatim): “Starting February 12, 2025, apps you submit for review in App Store Connect must contain a valid privacy manifest file for a certain number of commonly used third-party SDKs.”

**Applies to:** New apps submitted in App Store Connect that include a listed SDK, and app updates that add a listed SDK (signatures: where the listed SDK is used as a binary dependency).

- **[PRIV-73]** If this is a new app, or an update that adds a listed SDK, does every listed SDK (any version, or any SDK that repackages one) the app includes ship a privacy manifest in the built app?
  - quote: "You must include the privacy manifest for any SDK listed below when you submit new apps in App Store Connect that include those SDKs, or when you submit an app update that adds one of the listed SDKs as part of the update."
  - surface: code
  - verify: Collect dependency names from `Package.resolved` (`identity`/`location`), `Podfile.lock` (`PODS:`), `Cartfile.resolved`, `pubspec.lock` (Flutter), `package.json` (Capacitor/Cordova/React Native `hermes`), embedded `*.xcframework` / `*.framework` names, and Unity `UnityFramework`; case-insensitively match against the 86-entry table. For each match, build/archive and confirm a `PrivacyInfo.xcprivacy` from that SDK exists in the bundle (`<App>.app/Frameworks/<SDK>.framework/PrivacyInfo.xcprivacy` or `<App>.app/<SDK>_Privacy.bundle/PrivacyInfo.xcprivacy` / `<App>.app/<Package>_<Target>.bundle/PrivacyInfo.xcprivacy` for SwiftPM/CocoaPods resource bundles) and passes PRIV-64–PRIV-72.
  - fix: Update the SDK to a version that ships a valid privacy manifest; if no such version exists, contact its developer or remove the SDK (manual decision).
- **[PRIV-74]** In those same cases (new app, or update adding a listed SDK), where a listed SDK is used as a binary dependency (XCFramework), is it signed?
  - quote: "Signatures are also required in these cases where the listed SDKs are used as binary dependencies."
  - surface: code
  - verify: For each listed SDK included as `.xcframework`, run `codesign -dv --verbose=2 <SDK>.xcframework` (expect `Authority=` lines / `TeamIdentifier=`, not “code object is not signed at all”); also select the XCFramework in Xcode’s Project navigator and read the File inspector’s signature section.
  - fix: Obtain a signed XCFramework release from the SDK vendor (or use the source distribution via SwiftPM/CocoaPods); see PRIV.P.
- **[PRIV-75]** Has the developer reviewed the data collection and use practices of every third-party SDK included in the app?
  - quote: "when you use a third-party SDK with your app, you are responsible for all the code the SDK includes in your app, and need to be aware of its data collection and use practices"
  - surface: manual
  - verify: List every third-party dependency; for each, confirm the developer has read its privacy manifest / documentation and reflected its collection in App Store Connect App Privacy (via the PRIV-29 privacy report).
  - fix: manual — requires developer decision/legal/business action

---

## PRIV.P Verifying the origin of your XCFrameworks (SDK signatures)

**Source text (verbatim):**
> Discover who signed a framework, and take action when that changes.
>
> When you add third-party binary SDKs to your target as XCFrameworks, the behaviors of those packages become part of the behavior of your product. An attacker who’s able to inject a compromised version of the SDK into your project could change your app’s behavior and cause security and privacy issues for your developers, testers, and people who use your product.
>
> Use Xcode to inspect the information in the code signature embedded in an XCFramework when you add it to your project. The build system fails with an error if the code signature’s subsequently removed, becomes invalid, or a different developer signs an update to the framework. If any of these happens, take action to resolve the issue.
>
> **Inspect a dependency’s code signing identity**
>
> In Xcode, select your dependency’s XCFramework folder in the Project navigator. The File inspector shows you the XCFramework’s code signing status. If the framework is signed with an Apple Developer certificate, the inspector also shows which team signed the framework.
>
> If the XCFramework is signed by a self-issued code signing identity, the inspector shows the SHA-256 fingerprint of the certificate in the framework’s code signature. Verify that the certificate fingerprint matches the value you expect.
>
> **Diagnose build failures caused by code signature changes**
>
> An XCFramework’s code signature can change for legitimate reasons, like:
> - the provider of a third-party SDK transfers ownership of the SDK to another organization, who release a version that’s signed with the new organization’s Team ID.
> - you switch from a vendor-supplied distribution of an XCFramework to a version that you build and sign yourself.
>
> A changed code signature can also indicate that the XCFramework has been tampered with, or another actor has injected their own code into your system, pretending it’s a version of the XCFramework.
>
> If the code signature for an XCFramework changes, Xcode shows the changed code signature information in the File inspector.
>
> If you attempt to build the software without resolving the changed code signature information, the build system produces an error. Work with the XCFramework’s provider to determine whether the change is expected. If the change is expected, follow these steps:
> - 1. Switch to the Issues navigator.
> - 2. Select the error that says “[XCFramework name] is not signed with the expected identity and may have been compromised”.
> - 3. In the dialog that appears, click Accept Change.
>
> If your team and the SDK provider can’t account for the change to the XCFramework’s code signature, restore a version of the framework with the expected code signature, or remove the framework from your project. To restore the framework to a version with the expected code signature, do the following:
> - 1. In the dialog, click Move to Trash.
> - 2. Switch to or open a new Finder window.
> - 3. Drag a replacement copy of the XCFramework from a trusted source to the Finder folder that contained the copy you deleted.
> - 4. Switch to Xcode, and verify that the XCFramework’s signature is valid in the File inspector.
>
> Warning: If you encounter an unexpected code signature change in an XCFramework, it’s possible that an attacker is exploiting a security vulnerability in your infrastructure. Audit the origins for your XCFrameworks to ensure you obtained them from official sources. You also need to audit your software development and deployment environment carefully, even if you revert the XCFramework to a correctly-signed version.
>
> Xcode also warns you if the XCFramework is signed with an expired or revoked code signing identity, even if the identity hasn’t changed since you added the XCFramework to your project. If this happens, work with the SDK provider to obtain a new version of the framework that’s signed by a valid code signing identity.
>
> **Diagnose failures caused when a code signature is removed**
>
> If someone removes the code signature for an XCFramework, Xcode shows the change in the File inspector.
>
> The build system fails with an error if you attempt to build the software without resolving the removed code signature. Determine why the code signature is missing from the XCFramework. If you no longer expect the XCFramework to be signed, follow these steps:
> - 1. Switch to the Issues navigator.
> - 2. Select the error that says “[XCFramework name] is not signed with the expected identity and may have been compromised”.
> - 3. In the dialog that appears, click Accept Change.

**Applies to:** Apps that add third-party binary SDKs as XCFrameworks.

- **[PRIV-76]** Does the project build without any “[XCFramework name] is not signed with the expected identity and may have been compromised” error?
  - quote: "Select the error that says “[XCFramework name] is not signed with the expected identity and may have been compromised”."
  - surface: code
  - verify: `xcodebuild -scheme <Scheme> -destination 'generic/platform=iOS' build 2>&1 | grep -i 'not signed with the expected identity'` must return nothing.
  - fix: Work with the SDK provider to confirm the change; if expected, Accept Change in the Issues navigator; if not, restore a correctly signed copy from a trusted source or remove the framework (manual decision).
- **[PRIV-77]** Are XCFrameworks free of expired or revoked code signing identity warnings?
  - quote: "Xcode also warns you if the XCFramework is signed with an expired or revoked code signing identity"
  - surface: code
  - verify: Inspect build log warnings for the XCFramework signature; run `codesign -dv --verbose=4 <X>.xcframework` and check the certificate chain.
  - fix: Obtain a new version of the framework signed by a valid code signing identity from the SDK provider.
- **[PRIV-78]** For XCFrameworks signed with a self-issued identity, does the SHA-256 certificate fingerprint shown in Xcode’s File inspector match the value the vendor publishes?
  - quote: "Verify that the certificate fingerprint matches the value you expect."
  - surface: manual
  - verify: Select the XCFramework in the Project navigator, read the SHA-256 fingerprint in the File inspector, compare against the vendor’s published fingerprint.
  - fix: If it does not match, replace the framework with a copy from the official source and audit the build environment (manual).

---

## Sources

| URL | Page title |
|---|---|
| https://developer.apple.com/documentation/bundleresources/privacy-manifest-files (JSON: https://developer.apple.com/tutorials/data/documentation/bundleresources/privacy-manifest-files.json) | Privacy manifest files |
| https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api (JSON: …/bundleresources/describing-use-of-required-reason-api.json) | Describing use of required reason API |
| https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests (JSON: …/bundleresources/describing-data-use-in-privacy-manifests.json) | Describing data use in privacy manifests |
| https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk (JSON) | Adding a privacy manifest to your app or third-party SDK |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration (JSON) | App Privacy Configuration |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacytracking (JSON) | NSPrivacyTracking |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacytrackingdomains (JSON) | NSPrivacyTrackingDomains |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes (JSON) | NSPrivacyCollectedDataTypes |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes/nsprivacycollecteddatatype (JSON) | NSPrivacyCollectedDataType |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes/nsprivacycollecteddatatypelinked (JSON) | NSPrivacyCollectedDataTypeLinked |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes/nsprivacycollecteddatatypetracking (JSON) | NSPrivacyCollectedDataTypeTracking |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes/nsprivacycollecteddatatypepurposes (JSON) | NSPrivacyCollectedDataTypePurposes |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacyaccessedapitypes (JSON) | NSPrivacyAccessedAPITypes |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitype (JSON) | NSPrivacyAccessedAPIType |
| https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitypereasons (JSON) | NSPrivacyAccessedAPITypeReasons |
| https://developer.apple.com/documentation/technotes/tn3181-debugging-invalid-privacy-manifest (JSON) | TN3181: Debugging an invalid privacy manifest |
| https://developer.apple.com/documentation/technotes/tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest (JSON) | TN3182: Adding privacy tracking keys to your privacy manifest |
| https://developer.apple.com/documentation/technotes/tn3183-adding-required-reason-api-entries-to-your-privacy-manifest (JSON) | TN3183: Adding required reason API entries to your privacy manifest |
| https://developer.apple.com/documentation/technotes/tn3184-adding-data-collection-details-to-your-privacy-manifest (JSON) | TN3184: Adding data collection details to your privacy manifest |
| https://developer.apple.com/documentation/xcode/verifying-the-origin-of-your-xcframeworks (JSON) | Verifying the origin of your XCFrameworks |
| https://developer.apple.com/support/third-party-SDK-requirements/ | Third-party SDK requirements |
| https://developer.apple.com/documentation/foundation/fileattributekey/creationdate (JSON) | creationDate |
| https://developer.apple.com/documentation/foundation/fileattributekey/modificationdate (JSON) | modificationDate |
| https://developer.apple.com/documentation/uikit/uidocument/filemodificationdate (JSON) | fileModificationDate |
| https://developer.apple.com/documentation/foundation/urlresourcekey/contentmodificationdatekey (JSON) | contentModificationDateKey |
| https://developer.apple.com/documentation/foundation/urlresourcekey/creationdatekey (JSON) | creationDateKey |
| https://developer.apple.com/documentation/kernel/stat (JSON) | stat |
| https://developer.apple.com/documentation/foundation/processinfo/systemuptime (JSON) | systemUptime |
| https://developer.apple.com/documentation/foundation/urlresourcekey/volumeavailablecapacitykey (JSON) | volumeAvailableCapacityKey |
| https://developer.apple.com/documentation/foundation/urlresourcekey/volumeavailablecapacityforimportantusagekey (JSON) | volumeAvailableCapacityForImportantUsageKey |
| https://developer.apple.com/documentation/foundation/urlresourcekey/volumeavailablecapacityforopportunisticusagekey (JSON) | volumeAvailableCapacityForOpportunisticUsageKey |
| https://developer.apple.com/documentation/foundation/urlresourcekey/volumetotalcapacitykey (JSON) | volumeTotalCapacityKey |
| https://developer.apple.com/documentation/foundation/fileattributekey/systemfreesize (JSON) | systemFreeSize |
| https://developer.apple.com/documentation/foundation/fileattributekey/systemsize (JSON) | systemSize |
| https://developer.apple.com/documentation/uikit/uitextinputmode/activeinputmodes (JSON) | activeInputModes |
| https://developer.apple.com/documentation/foundation/userdefaults (JSON) | UserDefaults |
| https://developer.apple.com/documentation/swiftui/appstorage (JSON) | AppStorage |
