#!/usr/bin/env python3
"""Collect App Store review evidence from an app project.

Facts only, no verdicts: the audit agents decide pass/fail against the
guideline references. Standard library only.

Usage: python3 -I scan_project.py <project_root> <out.json>
"""
import json
import os
import plistlib
import re
import struct
import sys
import xml.parsers.expat

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "references", "data")

SKIP_DIRS = {
    ".git", "node_modules", "Pods", "Carthage", "DerivedData", ".build", "build",
    ".swiftpm", "SourcePackages", ".gradle", ".dart_tool", "vendor", ".expo",
    "xcuserdata", ".idea", ".vscode", "fastlane/screenshots",
}
SOURCE_EXT = {".swift", ".m", ".mm", ".h", ".c", ".cpp", ".js", ".jsx", ".ts", ".tsx", ".dart", ".kt"}
MAX_FILE_BYTES = 2_000_000
MAX_HITS_PER_PATTERN = 25


def load_json(name, default):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# Feature signals the profiler uses to decide which guidelines apply.
# Each entry: key -> list of regexes searched in source files.
FEATURE_SIGNALS = {
    "storekit_iap": [r"\bSKPaymentQueue\b", r"\bProduct\.products\(", r"\bTransaction\.(updates|currentEntitlements)\b", r"\bStoreView\b", r"\bSubscriptionStoreView\b", r"\bProductView\b", r"RevenueCat|Purchases\.shared|Adapty|Qonversion|Superwall"],
    "restore_purchases": [r"restoreCompletedTransactions", r"AppStore\.sync\(", r"(?i)restore\s*purchases?", r"restorePurchases"],
    "external_payments": [r"(?i)stripe", r"(?i)paypal", r"(?i)braintree", r"(?i)checkout\.com", r"ExternalPurchase", r"ExternalPurchaseLink"],
    "sign_in_with_apple": [r"ASAuthorizationAppleIDProvider", r"SignInWithAppleButton", r"ASAuthorizationAppleIDButton"],
    "third_party_login": [r"GIDSignIn|GoogleSignIn", r"FBSDKLoginKit|FacebookLogin|LoginManager\(\)", r"(?i)\bauth0\b", r"(?i)firebase.?auth|Auth\.auth\(\)", r"(?i)supabase.*auth|signInWithOAuth|signInWithIdToken", r"(?i)\bclerk\b", r"(?i)login\s*with\s*(google|facebook|twitter|x|github|linkedin|microsoft)"],
    "account_creation": [r"(?i)sign\s*up|create\s*(an\s*)?account|register\b|createUser"],
    "account_deletion": [r"(?i)delete\s*(my\s*)?account|deleteAccount|account\s*deletion|remove\s*account"],
    "app_tracking_transparency": [r"ATTrackingManager", r"requestTrackingAuthorization"],
    "advertising_id": [r"ASIdentifierManager", r"advertisingIdentifier"],
    "ads_sdk": [r"GoogleMobileAds|GADMobileAds|GADBannerView", r"(?i)applovin|ironsource|unityads|UnityAds|chartboost|vungle|inmobi|mintegral|pangle|AppLovinSDK", r"FBAudienceNetwork"],
    "analytics_sdk": [r"(?i)firebase.?analytics|FirebaseAnalytics", r"(?i)\bmixpanel\b", r"(?i)\bamplitude\b", r"(?i)\bsegment\b.*analytics", r"(?i)posthog", r"(?i)appsflyer", r"(?i)adjust\b", r"(?i)branch\.io|import Branch", r"(?i)sentry", r"(?i)crashlytics", r"(?i)datadog", r"(?i)telemetrydeck"],
    "location": [r"CLLocationManager", r"requestWhenInUseAuthorization|requestAlwaysAuthorization", r"CLLocationUpdate"],
    "background_location": [r"allowsBackgroundLocationUpdates", r"requestAlwaysAuthorization"],
    "healthkit": [r"\bHKHealthStore\b", r"import HealthKit"],
    "health_or_medical_terms": [r"(?i)\b(diagnos\w*|dosage|symptom|blood\s*pressure|glucose|heart\s*rate|medical|clinical)\b"],
    "camera": [r"AVCaptureSession|AVCaptureDevice", r"UIImagePickerController", r"\bCameraView\b"],
    "photos": [r"PHPhotoLibrary|PHPickerViewController|PhotosPicker"],
    "microphone": [r"AVAudioRecorder|AVAudioEngine|requestRecordPermission|AVAudioApplication"],
    "speech": [r"SFSpeechRecognizer"],
    "contacts": [r"CNContactStore"],
    "calendar": [r"EKEventStore"],
    "bluetooth": [r"CBCentralManager|CBPeripheralManager"],
    "nfc": [r"NFCNDEFReaderSession|NFCTagReaderSession"],
    "face_id": [r"LAContext", r"evaluatePolicy"],
    "push_notifications": [r"registerForRemoteNotifications", r"UNUserNotificationCenter"],
    "notification_permission": [r"requestAuthorization\(options"],
    "web_view": [r"\bWKWebView\b", r"\bWebView\b", r"react-native-webview"],
    "uiwebview_deprecated": [r"\bUIWebView\b"],
    "safari_view": [r"SFSafariViewController", r"ASWebAuthenticationSession"],
    "user_generated_content": [r"(?i)report\s*(post|user|content|abuse)", r"(?i)block\s*user", r"(?i)\b(comment|post|feed|chat|message)s?\b.*(upload|send|publish)", r"(?i)moderat"],
    "chat_or_social": [r"(?i)\bchat\b", r"(?i)direct\s*message", r"(?i)friend\s*request", r"(?i)\bfollowers?\b"],
    "generative_ai": [r"(?i)api\.openai\.com|OpenAI\(", r"(?i)api\.anthropic\.com|Anthropic\(", r"(?i)generativelanguage\.googleapis|GenerativeModel", r"FoundationModels|LanguageModelSession", r"(?i)replicate\.com|stability\.ai|elevenlabs"],
    "crypto": [r"(?i)\bwallet\b.*(seed|mnemonic|private\s*key)", r"(?i)web3|ethers|walletconnect", r"(?i)\bmining\b|\bminer\b"],
    "vpn": [r"NEVPNManager|NETunnelProviderManager|NEPacketTunnelProvider"],
    "mdm": [r"(?i)mobile\s*device\s*management|\bMDM\b"],
    "callkit": [r"CXProvider|CXCallController"],
    "pushkit_voip": [r"PKPushRegistry"],
    "gambling_or_contests": [r"(?i)\b(sweepstakes|lottery|casino|betting|wager|raffle)\b"],
    "kids_terms": [r"(?i)\b(kids?|children|toddler|preschool)\b"],
    "screen_time_family_controls": [r"FamilyControls|ManagedSettings|DeviceActivity"],
    "matter": [r"MatterSupport|import Matter"],
    "widgets_extensions": [r"WidgetKit|\bWidget\b.*:\s*Widget", r"NSExtensionPointIdentifier"],
    "keyboard_extension": [r"UIInputViewController"],
    "siri_shortcuts": [r"AppIntents|INIntent|AppShortcutsProvider"],
    "apple_pay": [r"PKPaymentRequest|PKPaymentAuthorization|PayWithApplePayButton"],
    "game_center": [r"GKLocalPlayer|GameKit"],
    "arkit": [r"ARKit|ARSession|RealityKit"],
    "remote_desktop_or_streaming": [r"(?i)remote\s*desktop|cloud\s*gaming|game\s*streaming"],
    "dynamic_code_loading": [r"\bdlopen\b", r"NSClassFromString\(", r"JSContext|JavaScriptCore", r"(?i)codepush|expo-updates|hot\s*update", r"(?i)\beval\("],
    "private_api_hints": [r"performSelector\(.*\"_", r"valueForKey:@?\"_", r"value\(forKey:\s*\"_", r"(?i)LSApplicationWorkspace", r"objc_msgSend"],
    "placeholder_text": [r"(?i)lorem\s+ipsum", r"(?i)\bplaceholder\b", r"(?i)coming\s+soon", r"(?i)\bTODO\b", r"(?i)\bFIXME\b", r"(?i)under\s+construction", r"(?i)test\s*user|dummy\s*data"],
    "beta_or_test_wording": [r"(?i)\b(beta|alpha|trial version|demo version|preview build)\b"],
    "other_platform_mentions": [r"(?i)\bandroid\b", r"(?i)google\s*play", r"(?i)\bwindows\s*phone\b"],
    "insecure_http": [r"http://(?!localhost|127\.0\.0\.1|www\.apple\.com/DTDs|schemas\.|www\.w3\.org)"],
    "privacy_policy_link": [r"(?i)privacy\s*policy", r"(?i)/privacy"],
    "terms_link": [r"(?i)terms\s*(of\s*(use|service))?", r"(?i)\bEULA\b", r"(?i)/terms"],
    "support_contact": [r"(?i)mailto:", r"(?i)contact\s*(us|support)", r"(?i)/support"],
    "rate_review_prompt": [r"SKStoreReviewController|requestReview", r"(?i)rate\s*(us|this\s*app)"],
    "custom_review_prompt": [r"(?i)itms-apps://.*action=write-review", r"(?i)leave\s*a\s*review"],
    "alternate_icons": [r"setAlternateIconName"],
    "hidden_features_flags": [r"(?i)remote\s*config|feature\s*flag|RemoteConfig|LaunchDarkly|Statsig|ConfigCat"],
}

INFO_PLIST_KEYS_OF_INTEREST = {
    "CFBundleDisplayName", "CFBundleName", "CFBundleIdentifier", "CFBundleShortVersionString",
    "CFBundleVersion", "UIBackgroundModes", "NSAppTransportSecurity", "ITSAppUsesNonExemptEncryption",
    "ITSEncryptionExportComplianceCode", "LSApplicationQueriesSchemes", "UIRequiredDeviceCapabilities",
    "CFBundleURLTypes", "UISupportedInterfaceOrientations", "UISupportedInterfaceOrientations~ipad",
    "UIRequiresFullScreen", "UILaunchStoryboardName", "UILaunchScreen", "UIApplicationSceneManifest",
    "NSUserActivityTypes", "LSSupportsOpeningDocumentsInPlace", "UIFileSharingEnabled",
    "GADApplicationIdentifier", "SKAdNetworkItems", "NSUserTrackingUsageDescription",
    "UIApplicationExitsOnSuspend", "MinimumOSVersion", "LSMinimumSystemVersion", "NSPrincipalClass",
    "NSExtension", "WKApplication", "WKCompanionAppBundleIdentifier", "WKRunsIndependentlyOfCompanionApp",
}


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        rel = os.path.relpath(dirpath, root)
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.endswith(".xcarchive")
                       and os.path.join(rel, d).lstrip("./") not in SKIP_DIRS]
        for name in filenames:
            yield os.path.join(dirpath, name)


def rel(root, path):
    return os.path.relpath(path, root)


def read_text(path):
    try:
        if os.path.getsize(path) > MAX_FILE_BYTES:
            return None
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return None


def load_plist(path):
    try:
        with open(path, "rb") as f:
            return plistlib.load(f)
    except (OSError, plistlib.InvalidFileException, xml.parsers.expat.ExpatError, ValueError):
        return None


def grep(text, pattern):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if re.search(pattern, line):
            hits.append((i, line.strip()[:200]))
    return hits


def png_info(path):
    """Return (width, height, has_alpha) for a PNG without third-party libs."""
    try:
        with open(path, "rb") as f:
            head = f.read(33)
        if head[:8] != b"\x89PNG\r\n\x1a\n":
            return None
        width, height, _depth, color_type = struct.unpack(">IIBB", head[16:26])
        return {"width": width, "height": height, "has_alpha_channel": color_type in (4, 6)}
    except (OSError, struct.error):
        return None


def pbxproj_settings(text):
    keys = (
        "PRODUCT_BUNDLE_IDENTIFIER", "MARKETING_VERSION", "CURRENT_PROJECT_VERSION",
        "IPHONEOS_DEPLOYMENT_TARGET", "MACOSX_DEPLOYMENT_TARGET", "WATCHOS_DEPLOYMENT_TARGET",
        "TVOS_DEPLOYMENT_TARGET", "XROS_DEPLOYMENT_TARGET", "TARGETED_DEVICE_FAMILY", "SDKROOT",
        "SUPPORTED_PLATFORMS", "CODE_SIGN_ENTITLEMENTS", "INFOPLIST_FILE", "GENERATE_INFOPLIST_FILE",
        "SWIFT_VERSION", "ASSETCATALOG_COMPILER_APPICON_NAME", "ENABLE_APP_SANDBOX", "ENABLE_HARDENED_RUNTIME",
        "SUPPORTS_MACCATALYST", "SUPPORTS_MAC_DESIGNED_FOR_IPHONE_IPAD", "PRODUCT_NAME",
    )
    out = {}
    for line in text.splitlines():
        m = re.match(r"\s*\"?([A-Z_]+(?:\[[^\]]*\])?)\"?\s*=\s*(.+?);\s*$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip().strip('"')
        base = key.split("[")[0]
        if base in keys or base.startswith("INFOPLIST_KEY_"):
            out.setdefault(key, set()).add(value)
    return {k: sorted(v) for k, v in out.items()}


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    root = os.path.abspath(sys.argv[1])
    out_path = sys.argv[2]

    required_reason = load_json("required_reason_apis.json", {"categories": []})
    sdk_list = load_json("sdks_requiring_manifest.json", {"sdks": []})
    purpose_keys = load_json("purpose_string_keys.json", {"keys": []})

    facts = {
        "projectRoot": root,
        "projectTypes": [],
        "xcodeProjects": [],
        "infoPlists": [],
        "generatedInfoPlistKeys": {},
        "buildSettings": {},
        "entitlements": [],
        "privacyManifests": [],
        "requiredReasonApiUsage": [],
        "dependencies": {"spm": [], "cocoapods": [], "carthage": [], "npm": [], "pub": []},
        "sdksRequiringManifest": [],
        "featureSignals": {},
        "appIcons": [],
        "localizations": [],
        "storeKitConfigs": [],
        "fastlaneMetadata": [],
        "counts": {"sourceFiles": 0},
        "notes": [],
    }

    sources = []
    for path in walk(root):
        name = os.path.basename(path)
        ext = os.path.splitext(name)[1]
        r = rel(root, path)

        if name == "project.pbxproj":
            text = read_text(path) or ""
            facts["xcodeProjects"].append(r)
            settings = pbxproj_settings(text)
            for k, v in settings.items():
                if k.startswith("INFOPLIST_KEY_"):
                    facts["generatedInfoPlistKeys"].setdefault(k[len("INFOPLIST_KEY_"):], []).extend(v)
                else:
                    facts["buildSettings"].setdefault(k, []).extend(v)
        elif name == "Info.plist" or (ext == ".plist" and name.endswith("-Info.plist")):
            pl = load_plist(path)
            if isinstance(pl, dict):
                usage = {k: v for k, v in pl.items() if k.endswith("UsageDescription")}
                interesting = {k: pl[k] for k in pl if k in INFO_PLIST_KEYS_OF_INTEREST}
                facts["infoPlists"].append({"path": r, "usageDescriptions": usage, "keys": interesting})
        elif ext == ".entitlements":
            pl = load_plist(path)
            if isinstance(pl, dict):
                facts["entitlements"].append({"path": r, "values": pl})
        elif name == "PrivacyInfo.xcprivacy":
            pl = load_plist(path)
            facts["privacyManifests"].append({"path": r, "parsed": pl is not None, "values": pl if isinstance(pl, dict) else None})
        elif name == "Package.resolved":
            try:
                data = json.loads(read_text(path) or "{}")
                pins = data.get("pins") or data.get("object", {}).get("pins", [])
                for p in pins:
                    facts["dependencies"]["spm"].append({
                        "identity": p.get("identity") or p.get("package"),
                        "location": p.get("location") or p.get("repositoryURL"),
                        "version": (p.get("state") or {}).get("version"),
                    })
            except json.JSONDecodeError:
                facts["notes"].append(f"Could not parse {r}")
        elif name == "Podfile.lock":
            text = read_text(path) or ""
            for m in re.finditer(r"^  - ([A-Za-z0-9_\-+/.]+) \(([^)]+)\)", text, re.M):
                facts["dependencies"]["cocoapods"].append({"name": m.group(1), "version": m.group(2)})
        elif name == "Cartfile.resolved":
            for line in (read_text(path) or "").splitlines():
                parts = line.split()
                if len(parts) >= 3:
                    facts["dependencies"]["carthage"].append({"name": parts[1].strip('"'), "version": parts[2].strip('"')})
        elif name == "package.json" and "node_modules" not in r:
            try:
                data = json.loads(read_text(path) or "{}")
                deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                facts["dependencies"]["npm"].extend({"name": k, "version": v} for k, v in deps.items())
                if "react-native" in deps:
                    facts["projectTypes"].append("react-native")
                if "expo" in deps:
                    facts["projectTypes"].append("expo")
                if "@capacitor/core" in deps or "cordova" in deps:
                    facts["projectTypes"].append("hybrid-webview")
            except json.JSONDecodeError:
                pass
        elif name == "pubspec.lock":
            facts["projectTypes"].append("flutter")
            for m in re.finditer(r"^  ([a-z0-9_]+):\n(?:    .*\n)*?    version: \"([^\"]+)\"", read_text(path) or "", re.M):
                facts["dependencies"]["pub"].append({"name": m.group(1), "version": m.group(2)})
        elif ext == ".storekit":
            facts["storeKitConfigs"].append(r)
        elif name == "Contents.json" and ".appiconset" in r:
            folder = os.path.dirname(path)
            try:
                data = json.loads(read_text(path) or "{}")
            except json.JSONDecodeError:
                data = {}
            images = []
            for img in data.get("images", []):
                fn = img.get("filename")
                info = png_info(os.path.join(folder, fn)) if fn else None
                images.append({"filename": fn, "size": img.get("size"), "idiom": img.get("idiom"),
                               "platform": img.get("platform"), "appearances": img.get("appearances"), "png": info})
            facts["appIcons"].append({"path": rel(root, folder), "images": images})
        elif ext == ".lproj" or name.endswith(".xcstrings"):
            facts["localizations"].append(r)
        elif "/fastlane/metadata/" in "/" + r:
            facts["fastlaneMetadata"].append(r)

        if ext in SOURCE_EXT:
            sources.append(path)
        if ext == ".lproj":
            pass

    for dirpath, dirnames, _ in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for d in dirnames:
            if d.endswith(".lproj"):
                facts["localizations"].append(rel(root, os.path.join(dirpath, d)))
    facts["localizations"] = sorted(set(facts["localizations"]))

    if facts["xcodeProjects"]:
        facts["projectTypes"].append("xcode")
    if any(os.path.basename(p) == "Package.swift" for p in sources) or os.path.exists(os.path.join(root, "Package.swift")):
        facts["projectTypes"].append("swiftpm")
    facts["projectTypes"] = sorted(set(facts["projectTypes"]))
    facts["counts"]["sourceFiles"] = len(sources)

    texts = {}
    for path in sources:
        t = read_text(path)
        if t is not None:
            texts[rel(root, path)] = t

    for key, patterns in FEATURE_SIGNALS.items():
        hits = []
        for r, t in texts.items():
            for pat in patterns:
                for line_no, line in grep(t, pat):
                    hits.append({"file": r, "line": line_no, "text": line, "pattern": pat})
                    if len(hits) >= MAX_HITS_PER_PATTERN * len(patterns):
                        break
        if hits:
            facts["featureSignals"][key] = {"count": len(hits), "hits": hits[:MAX_HITS_PER_PATTERN]}

    for cat in required_reason.get("categories", []):
        hits = []
        for r, t in texts.items():
            for sym in cat.get("symbols", []):
                for line_no, line in grep(t, r"\b" + re.escape(sym) + r"\b"):
                    hits.append({"file": r, "line": line_no, "symbol": sym, "text": line})
        if hits:
            facts["requiredReasonApiUsage"].append({
                "category": cat.get("category"), "count": len(hits), "hits": hits[:MAX_HITS_PER_PATTERN]})

    dep_names = set()
    for group in facts["dependencies"].values():
        for d in group:
            for field in ("identity", "name", "location"):
                v = d.get(field)
                if v:
                    dep_names.add(v.lower().rstrip("/").split("/")[-1].removesuffix(".git"))
                    dep_names.add(v.lower())
    for sdk in sdk_list.get("sdks", []):
        aliases = [a.lower() for a in sdk.get("aliases", [sdk.get("name", "")])]
        if any(a in dep_names or any(a == n.split("/")[0] for n in dep_names) for a in aliases):
            facts["sdksRequiringManifest"].append(sdk.get("name"))

    declared = set()
    for p in facts["infoPlists"]:
        declared.update(p["usageDescriptions"].keys())
    declared.update(k for k in facts["generatedInfoPlistKeys"] if k.endswith("UsageDescription"))
    values = {}
    for p in facts["infoPlists"]:
        for k, v in p["usageDescriptions"].items():
            values.setdefault(k, []).append({"source": p["path"], "value": v})
    for k, vs in facts["generatedInfoPlistKeys"].items():
        if k.endswith("UsageDescription"):
            values.setdefault(k, []).extend({"source": "build setting INFOPLIST_KEY_" + k, "value": v} for v in vs)
    known = {k.get("key") for k in purpose_keys.get("keys", [])}
    facts["purposeStrings"] = {
        "declared": sorted(declared),
        "values": values,
        # Heuristic hint for auditors, not a verdict: very short or empty strings rarely explain the use.
        "shortOrEmpty": sorted(k for k, vs in values.items() if any(len(str(v["value"]).strip()) < 20 for v in vs)),
        "unknownKeys": sorted(k for k in declared if known and k not in known),
        "knownKeys": sorted(known),
    }

    if not facts["xcodeProjects"] and not facts["projectTypes"]:
        facts["notes"].append("No Xcode project, Swift package, React Native, Expo or Flutter project was found under the root.")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(facts, f, indent=2, default=str)
    summary = {
        "projectTypes": facts["projectTypes"],
        "infoPlists": len(facts["infoPlists"]),
        "privacyManifests": len(facts["privacyManifests"]),
        "entitlements": len(facts["entitlements"]),
        "sourceFiles": facts["counts"]["sourceFiles"],
        "featureSignals": sorted(facts["featureSignals"]),
        "requiredReasonCategoriesUsed": [c["category"] for c in facts["requiredReasonApiUsage"]],
        "sdksRequiringManifest": facts["sdksRequiringManifest"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
