---
name: apple-preflight
description: Use before uploading an iOS build to App Store Connect (the checker script targets Expo projects), or after Apple rejects a delivery with an ITMS error code. Checks Info.plist purpose strings, entitlements against the App ID, background modes, icon, encryption declaration and privacy manifests, cross-referenced against Apple's current documentation rather than remembered rules. Also use when asked to diagnose a rejected binary, a failed processing email, or a build that never appears in TestFlight.
user-invocable: true
argument-hint: "[check | diagnose ITMS-XXXXX]"
---

# Apple pre-flight

A rejected upload costs a compile, an upload, and a wait for an email that arrives up to an
hour later. Nearly every cause is visible in the project before the build starts. This finds
them first.

## The rule that matters most

**Never remove a key, capability or entitlement to silence a warning.** Apple requires purpose
strings for APIs a *linked library* references, not only for APIs your code calls. Deleting the
key does not remove the reference, it just moves the rejection from one ITMS code to another.

That mistake is real and it is expensive: an app with no health-writing code had
`NSHealthUpdateUsageDescription` deleted as "untrue", and the next build bounced on ITMS-90683
saying the string was required. Two uploads, two waits, to end up back where it started.

The correct move when a declaration looks wrong is to ask **why the reference exists**:

- Referenced by a dependency, unused by this app → **keep the key**, write a truthful string
- Declared by hand and used by nothing at all → **remove the declaration** (see ITMS-90771)

Those look identical from the config file. Tell them apart by searching the native module
sources, never by reasoning about intent.

## Always read Apple's current documentation first

Requirements change, ITMS codes are added, and privacy rules tightened twice in recent years.
Do not answer from memory.

Fetch before judging:

- Info.plist keys: <https://developer.apple.com/documentation/bundleresources/information-property-list>
- Protected resources: <https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy>
- Privacy manifests and required-reason APIs: <https://developer.apple.com/documentation/bundleresources/privacy-manifest-files>
- Review guidelines: <https://developer.apple.com/app-store/review/guidelines/>

When diagnosing a specific rejection, **search for the exact code** ("ITMS-90683") rather than
inferring from the message text. The wording is often more general than the actual trigger.

For an Expo project, also read the SDK's own docs for the version in `package.json`, and read
the config plugin's source in `node_modules` when a plugin option is involved. Plugin source is
the only authority on what a plugin actually writes; its documentation is frequently stale.

## Running the check

```sh
uv run python <this skill's base directory>/scripts/preflight.py --app <path-to-app-dir>
```

Run it **after** `expo prebuild` (or any native regeneration) and **before** the build, because
it reads the generated `Info.plist` and entitlements, not the config that produced them. Those
disagree whenever prebuild has not been rerun, and the generated files are what ships.

It exits non-zero when something would bounce, so it can gate a build.

## What it cannot see

The script checks what is statically knowable. These still need judgement:

- **Whether a purpose string is good enough.** Present is a processing requirement; *clear* is a
  review requirement. Placeholders containing `$(PRODUCT_NAME)` pass upload and draw reviewer
  attention. The script warns; you decide.
- **Whether the App ID grants the entitlements.** The script only lists them, so check them
  against the App ID in Apple's developer portal. A mismatch fails at signing, not at upload.
- **Guideline 2.5.4**, declaring background modes an app does not use. The script catches the
  missing-identifier case; it cannot tell whether a declared mode is genuinely exercised.

## Diagnosing a rejection that already happened

1. Get the **exact ITMS code** from the email. Do not work from the prose.
2. Read [reference/itms-codes.md](reference/itms-codes.md) for the ones already seen here.
3. Search Apple's documentation for the code, since the cause is often narrower than the text.
4. Find the reference in the project: `grep -rhoE 'NS[A-Za-z]+UsageDescription' node_modules/`
   is what distinguishes "a library needs this" from "someone typed this once".
5. Fix the cause, rerun prebuild, rerun this check, then rebuild.

**A build that never appears in App Store Connect at all has failed processing.** There is no
API that reports this; Apple only emails. Do not keep polling. Ask for the email.
