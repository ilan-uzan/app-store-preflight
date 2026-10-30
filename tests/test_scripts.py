"""Tests for the skill's scripts. Run: python3 -I -m unittest discover -s tests -v"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.join(ROOT, "skills", "app-store-preflight")
SCRIPTS = os.path.join(SKILL, "scripts")
FIXTURE = os.path.join(ROOT, "tests", "fixtures", "MiniApp")


def run(script, *args):
    out = subprocess.run([sys.executable, "-I", os.path.join(SCRIPTS, script), *args],
                         capture_output=True, text=True)
    if out.returncode not in (0, 1):
        raise AssertionError(f"{script} exited {out.returncode}: {out.stderr}")
    return out


class ScanProjectTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.facts_path = os.path.join(cls.tmp, "facts.json")
        run("scan_project.py", FIXTURE, cls.facts_path)
        with open(cls.facts_path) as f:
            cls.facts = json.load(f)

    def test_project_type(self):
        self.assertIn("xcode", self.facts["projectTypes"])

    def test_purpose_strings_from_plist_and_build_settings(self):
        declared = self.facts["purposeStrings"]["declared"]
        self.assertIn("NSCameraUsageDescription", declared)
        self.assertIn("NSPhotoLibraryUsageDescription", declared)  # INFOPLIST_KEY_ build setting
        self.assertIn("NSMicrophoneUsageDescription", self.facts["purposeStrings"]["shortOrEmpty"])

    def test_required_reason_api_detected(self):
        cats = [c["category"] for c in self.facts["requiredReasonApiUsage"]]
        self.assertIn("NSPrivacyAccessedAPICategoryUserDefaults", cats)

    def test_privacy_manifest_parsed(self):
        self.assertEqual(len(self.facts["privacyManifests"]), 1)
        self.assertTrue(self.facts["privacyManifests"][0]["parsed"])

    def test_feature_signals(self):
        self.assertIn("storekit_iap", self.facts["featureSignals"])
        self.assertIn("restore_purchases", self.facts["featureSignals"])

    def test_sdk_requiring_manifest(self):
        self.assertIn("Alamofire", self.facts["sdksRequiringManifest"])

    def test_bundle_id_build_setting(self):
        self.assertIn("com.example.miniapp", self.facts["buildSettings"]["PRODUCT_BUNDLE_IDENTIFIER"])


class ChecksTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.checks_path = os.path.join(cls.tmp, "checks.json")
        out = run("build_checks.py", os.path.join(SKILL, "references"), cls.checks_path, "--strict")
        cls.build_rc = out.returncode
        cls.data = json.load(open(cls.checks_path))

    def test_references_parse_cleanly(self):
        self.assertEqual(self.build_rc, 0)
        self.assertEqual(self.data["errors"], [])
        self.assertGreater(self.data["total"], 1500)

    def test_every_check_complete(self):
        for c in self.data["checks"]:
            self.assertTrue(c["quote"], c["id"])
            self.assertIn(c["surface"], {"code", "asc", "runtime", "manual"}, c["id"])

    def test_requires_tags_parsed(self):
        tagged = [c for c in self.data["checks"] if c["requires"]]
        self.assertTrue(tagged)
        vpn = [c for c in self.data["checks"] if c["unit"] == "5.4"]
        self.assertTrue(vpn and all("vpn" in c["requires"] for c in vpn))

    def test_plan_skips_only_fully_ruled_out(self):
        run_dir = tempfile.mkdtemp()
        profile = os.path.join(run_dir, "profile.json")
        json.dump({"flags": ["iap"], "notFlags": ["vpn"], "evidence": {"vpn": "no NetworkExtension"}}, open(profile, "w"))
        run("plan_checks.py", self.checks_path, profile, run_dir)
        skipped = {v["id"] for v in json.load(open(os.path.join(run_dir, "verdicts", "skipped.json")))}
        by_id = {c["id"]: c for c in self.data["checks"]}
        for cid in skipped:
            self.assertTrue(by_id[cid]["requires"])
            self.assertTrue(all(f == "vpn" for f in by_id[cid]["requires"]), cid)
        self.assertTrue(any(by_id[c]["unit"] == "5.4" for c in skipped))
        plan = json.load(open(os.path.join(run_dir, "plan.json")))
        kept = {i for b in plan["batches"] for i in b["checkIds"]} | {i for v in plan["asc"].values() for i in v}
        self.assertFalse(kept & skipped)
        # Untagged checks and checks needing an undecided flag are always kept.
        untagged = [c["id"] for c in self.data["checks"] if not c["requires"]]
        self.assertFalse(set(untagged) & skipped)


class RenderReportTest(unittest.TestCase):
    def test_grouping_fix_and_defaults(self):
        tmp = tempfile.mkdtemp()
        checks = {"checks": [
            {"id": "A-01", "file": "asc/x.md", "line": 1, "unit": "X.1", "unitTitle": "One", "question": "q1",
             "quote": "q", "surface": "code", "verify": "", "fix": "", "requires": []},
            {"id": "A-02", "file": "asc/x.md", "line": 2, "unit": "X.2", "unitTitle": "Two", "question": "q2",
             "quote": "q", "surface": "code", "verify": "", "fix": "", "requires": []},
            {"id": "A-03", "file": "asc/x.md", "line": 3, "unit": "X.3", "unitTitle": "Three", "question": "q3",
             "quote": "q", "surface": "code", "verify": "", "fix": "", "requires": []},
            {"id": "A-04", "file": "asc/x.md", "line": 4, "unit": "X.4", "unitTitle": "Four", "question": "q4",
             "quote": "q", "surface": "asc", "verify": "", "fix": "", "requires": []},
        ]}
        cpath = os.path.join(tmp, "checks.json")
        json.dump(checks, open(cpath, "w"))
        os.makedirs(os.path.join(tmp, "verdicts"))
        os.makedirs(os.path.join(tmp, "fixes"))
        json.dump([
            {"id": "A-01", "verdict": "FAIL", "location": "App/Paywall.swift:10", "reason": "same place"},
            {"id": "A-02", "verdict": "FAIL", "location": "App/Paywall.swift:10; other.swift:3", "reason": "same place"},
            {"id": "A-03", "verdict": "FAIL", "location": "App/Info.plist:4", "reason": "elsewhere"},
        ], open(os.path.join(tmp, "verdicts", "audit-000.json"), "w"))
        json.dump([{"id": "A-03", "status": "fixed", "files": ["App/Info.plist"], "summary": "s"}],
                  open(os.path.join(tmp, "fixes", "fix-000.json"), "w"))
        json.dump({"id": "A-03", "reverified": True}, open(os.path.join(tmp, "fixes", "reverify-A-03.json"), "w"))
        source = os.path.join(SKILL, "source", "app-review-guidelines.md")
        run("render_report.py", tmp, cpath, source)
        results = {r["id"]: r["verdict"] for r in json.load(open(os.path.join(tmp, "results.json")))["results"]}
        self.assertEqual(results["A-03"], "FIXED")  # fixed and re-verified
        self.assertEqual(results["A-04"], "ASC")    # asc check without a browser verdict
        report = open(os.path.join(tmp, "PREFLIGHT_REPORT.md")).read()
        self.assertIn("1 issue(s) from 2 failed check(s)", report)  # A-01 and A-02 merged


class QuotesTest(unittest.TestCase):
    def test_all_quotes_verbatim(self):
        out = run("verify_quotes.py", SKILL)
        self.assertEqual(out.returncode, 0, out.stdout[-2000:])


if __name__ == "__main__":
    unittest.main()
