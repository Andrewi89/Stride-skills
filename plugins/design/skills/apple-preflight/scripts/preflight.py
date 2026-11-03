#!/usr/bin/env python3
"""Check an iOS build against what App Store Connect rejects at processing.

Reads the GENERATED Info.plist and entitlements, not the config that produced them, because
those disagree whenever prebuild has not been rerun and the generated files are what ships.

    python3 preflight.py --app path/to/app

Exits non-zero if anything would bounce, so it can gate a build.
"""

from __future__ import annotations

import argparse
import json
import plistlib
import struct
import subprocess
import sys
from pathlib import Path

failures: list[str] = []
warnings: list[str] = []


def check(ok: bool, label: str, detail: str = "") -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {label}{'  ' + detail if detail else ''}")
    if not ok:
        failures.append(label)


def warn(label: str) -> None:
    print(f"  WARN  {label}")
    warnings.append(label)


def find_native(app: Path) -> tuple[Path, Path] | None:
    """The generated Info.plist and entitlements, whatever the scheme is called."""
    ios = app / "ios"
    if not ios.is_dir():
        return None
    for plist in sorted(ios.glob("*/Info.plist")):
        ents = next(plist.parent.glob("*.entitlements"), None)
        if ents:
            return plist, ents
    return None


def referenced_purpose_strings(app: Path) -> set[str]:
    """Every NS*UsageDescription any linked native module mentions.

    Apple scans the compiled binary, so a key is required when a dependency references the API
    even if this app never calls it. That is the whole of ITMS-90683, and the reason deleting a
    key to reflect what the app "really does" fails on the next upload.
    """
    modules = app / "node_modules"
    if not modules.is_dir():
        return set()
    # Scan the DIRECT dependencies only, and skip Expo's own tooling.
    #
    # Two wrong scopes, both tried. Grepping all of node_modules reports keys belonging to
    # libraries that are not installed: @expo/prebuild-config ships an unversioned plugin for
    # react-native-maps naming NSLocationWhenInUseUsageDescription, which blocks a build with
    # no maps and no location framework. Scanning only compiled .m/.swift misses the opposite
    # case, because most modules declare their required keys in a config plugin rather than in
    # native source, so HealthKit's two keys never appear.
    #
    # Direct dependencies minus the expo umbrella package catches both: a module that needs a
    # key names it somewhere in its own directory, and nothing else gets a vote.
    manifest = app / "package.json"
    if not manifest.exists():
        return set()
    deps = json.loads(manifest.read_text()).get("dependencies", {})
    found: set[str] = set()
    for name in deps:
        if name == "expo" or name.startswith("@expo/"):
            continue
        module = modules / name
        if not module.is_dir():
            continue
        # A list, not a shell string, so paths with spaces still get scanned.
        out = subprocess.run(
            ["grep", "-rhoE", "NS[A-Za-z]+UsageDescription", str(module)],
            capture_output=True, text=True,
        ).stdout
        found.update(out.split())
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--app", default=".", help="directory holding app.json and ios/")
    args = ap.parse_args()
    app = Path(args.app).resolve()

    native = find_native(app)
    if native is None:
        print(f"No generated ios/*/Info.plist under {app}.")
        print("Run `npx expo prebuild --platform ios` first; this checks what ships, not app.json.")
        return 1
    plist_path, ents_path = native
    plist = plistlib.loads(plist_path.read_bytes())
    ents = plistlib.loads(ents_path.read_bytes())
    print(f"  reading {plist_path.relative_to(app)}\n")

    cfg = {}
    if (app / "app.json").exists():
        cfg = json.loads((app / "app.json").read_text()).get("expo", {})

    # ITMS-90771. A 'processing' mode with no identifiers means either missing identifiers or,
    # far more often, background modes nothing in the app ever uses.
    modes = plist.get("UIBackgroundModes", [])
    ids = plist.get("BGTaskSchedulerPermittedIdentifiers", [])
    check("processing" not in modes or bool(ids),
          "ITMS-90771 no 'processing' mode without BGTask identifiers",
          str(modes or "no background modes"))

    # ITMS-90683. Present is the requirement; the app's own usage is not the test.
    need = referenced_purpose_strings(app)
    missing = sorted(k for k in need if not plist.get(k))
    check(not missing, "ITMS-90683 every referenced purpose string present",
          f"{len(need)} referenced" + (f", MISSING {missing}" if missing else ""))

    # Passes upload, invites a reviewer's attention. Not a failure.
    for key, value in sorted(plist.items()):
        if key.endswith("UsageDescription"):
            text = str(value)
            if "$(PRODUCT_NAME)" in text or len(text) < 25:
                warn(f"{key} looks like placeholder text: \"{text[:60]}\"")

    # Absent, Apple holds the build behind a manual question and TestFlight stalls.
    check(plist.get("ITSAppUsesNonExemptEncryption") is not None,
          "export compliance declared", str(plist.get("ITSAppUsesNonExemptEncryption")))

    check(bool(plist.get("UILaunchStoryboardName") or plist.get("UILaunchScreen") is not None),
          "launch screen present")

    # Signing fails, not uploading, so this surfaces as a confusing provisioning error.
    print(f"  INFO  entitlements: {sorted(ents)}")
    print("        these must all be enabled on the App ID or the build fails to sign")

    if cfg.get("ios", {}).get("appleTeamId"):
        print(f"  INFO  team pinned in app.json: {cfg['ios']['appleTeamId']}")
    else:
        warn("no ios.appleTeamId in app.json, so the signing team comes from Xcode's global state")

    icon_rel = cfg.get("icon")
    if icon_rel:
        icon = app / str(icon_rel).removeprefix("./")
        if icon.exists():
            raw = icon.read_bytes()
            width, height = struct.unpack(">II", raw[16:24])
            # PNG colour types 4 and 6 carry alpha, which Apple rejects on an app icon.
            check((width, height) == (1024, 1024) and raw[25] not in (4, 6),
                  "icon 1024x1024 with no alpha", f"{width}x{height}")

    print()
    if failures:
        print(f"  {len(failures)} would bounce: {failures}")
        return 1
    print(f"  ready to submit{f' ({len(warnings)} warning(s))' if warnings else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
