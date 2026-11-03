# ITMS codes, and what actually caused them

Each of these cost a real build. The cause is recorded, not just the fix, because the same
message has more than one cause and the wrong fix produces a different rejection.

## ITMS-90771 - missing BGTaskSchedulerPermittedIdentifiers

> The Info.plist key 'BGTaskSchedulerPermittedIdentifiers' must contain a list of identifiers
> used to submit and handle tasks when 'UIBackgroundModes' has a value of 'processing'.

**Two causes, opposite fixes.**

*The app does schedule background tasks.* Add the identifiers it registers. They must match the
strings passed to `BGTaskScheduler.register` exactly.

*The app schedules nothing.* The modes were aspiration. **Remove them.** Confirm first:

```sh
grep -rE "defineTask|registerTaskAsync|BGTaskScheduler" src/
python3 -c "import json;d=json.load(open('package.json'))['dependencies'];print([k for k in d if 'background' in k or 'task' in k])"
```

Both empty means nothing uses the modes and they should go. This also clears a **guideline
2.5.4** risk, since declaring unused background modes is grounds for rejection by itself.

**HealthKit background delivery is not this.** It runs on the
`com.apple.developer.healthkit.background-delivery` entitlement and needs no `UIBackgroundModes`
entry. Read the config plugin source to confirm what it writes; the plugin sets the entitlement
and never touches background modes. Removing `fetch`/`processing` does not affect it.

## ITMS-90683 - missing purpose string

> Your app's code references one or more APIs that access sensitive user data, or the app has
> one or more entitlements that permit such access.

Note **"references"**. Apple scans the compiled binary, so a string is required when any linked
dependency mentions the API, even if the app never calls it. The mail says so explicitly:
*"While your app might not use these APIs, a purpose string is still required."*

Find every key that any linked module references:

```sh
grep -rhoE 'NS[A-Za-z]+UsageDescription' node_modules/@*/  node_modules/expo-* 2>/dev/null | sort | uniq -c
```

Every key in that list must exist in `Info.plist`. **Deleting one because the app does not use
that capability is the wrong fix** and produces exactly this error on the next upload.

Write something truthful instead. An app that only reads health data can say so plainly:
*"This app only reads your activity. It never adds to or changes anything in Health."* That
satisfies the requirement without claiming a capability the app does not have.

## Silence - no build appears at all

Not an ITMS code, but the most confusing failure. `eas submit` reports success, and
`GET /v1/builds` returns an empty array indefinitely.

The upload succeeded and **processing** failed. Apple reports this by email only; nothing is
exposed through the App Store Connect API, so polling reveals nothing no matter how long it
runs. Check the account holder's inbox.

The account holder is the Apple ID on the developer account, which is not necessarily the
address on the Expo account or the one in `eas.json`.

## Things worth checking that have not bounced yet

- **Icon alpha.** A 1024x1024 icon with an alpha channel is rejected. PNG colour types 4 and 6
  carry alpha. Android adaptive icons legitimately have it; the iOS icon must not.
- **ITSAppUsesNonExemptEncryption.** Absent, Apple holds the build behind a manual question
  and TestFlight distribution stalls.
- **Privacy manifests.** Pods carry their own and CocoaPods aggregates them. An app calling a
  required-reason API directly needs its own `PrivacyInfo.xcprivacy`.
- **Entitlements exceeding the App ID.** Fails at signing rather than upload, so it surfaces as
  a build failure with a provisioning message rather than an ITMS code.

## Scoping the purpose-string search

The obvious search is wrong in both directions, and each wrong answer is expensive.

**Too wide.** `grep -r node_modules` reports keys belonging to libraries that are not
installed. `@expo/prebuild-config` bundles an unversioned plugin for react-native-maps that
names `NSLocationWhenInUseUsageDescription`. A project with no maps, no location code and no
CoreLocation linked will look like it is missing a required string.

**Too narrow.** Scanning only compiled `.m`/`.swift` sources misses most real requirements,
because modules usually declare their keys in a config plugin rather than in native code. The
HealthKit library's two keys never appear in its Swift files.

**Right scope:** the directories of packages in `dependencies`, skipping the `expo` umbrella
package and `@expo/*` tooling, whose bundled templates name keys for libraries you do not have.
A module that needs a key names it somewhere inside its own directory, and nothing else votes.
