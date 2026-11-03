---
name: expo-duo
description: Use when building, auditing or fixing an Expo / React Native app for iPhone Duo (Apple's foldable iPhone), including the vertical rail, safe-area insets, NativeTabs, SplitView, ArrangementView, expo-hinge, reserved regions, orientation locks, and testing Duo poses locally or in EAS Workflows CI. Pairs with apple-design-duo (design rules) and expo:eas-workflows (CI YAML).
---

# Expo on iPhone Duo

Source: https://expo.dev/blog/supporting-iphone-duo (Expo SDK 58). Design rules live in `apple-design-duo`; this skill is the Expo and React Native implementation layer. CI pipeline background: https://docs.expo.dev/tutorial/cicd/introduction/ and the `expo:eas-workflows` skill.

## Requirements

- Expo SDK 58 (targets iOS 27) and Xcode 27.1 (iOS 27.1 runtime plus the iPhone Duo simulator).
- EAS Build image: `sdk-58` or `latest`.
- Xcode 27 replaces Simulator.app with Device Hub (Xcode > Open Developer Tool > Device Hub). It has a 3D Duo that folds, rotates and sets the hinge angle.

## Mental model

Folded = compact width, open = regular width. Let layouts widen, never switch designs. Same features and state on both. In book-like poses iOS moves the status bar, tab bar and toolbar into a vertical rail on one edge.

## The four rules

1. **Let iOS draw navigation.** Use Expo Router `Stack` and `NativeTabs`. Custom JS headers and `<TabList>` are not rail-aware (SDK 58 only adds minimal compatibility) and `<TabList>` can't go in the rail.
2. **`SafeAreaView` (`react-native-safe-area-context`) on every screen, horizontal insets included.**
3. **Test every pose.** Fold, unfold, rotate, Split View.
4. **Tweak only where needed**: `ArrangementView`, `preferredPlacement`, reserved regions, hinge APIs, or disabling the rail.

## Safe areas (where most bugs are)

- The rail needs an **84pt inset** on the left or right.
- Wrap scroll content in `SafeAreaView edges={['left','right']}`, not the `ScrollView`, so backgrounds run edge to edge. Set `contentInsetAdjustmentBehavior="automatic"` on the ScrollView (RN patch #59194 should make this alone enough).
- Horizontal carousels: add end padding themselves.
- Floating buttons and toasts: `right: insets.right + 16`. In RTL, read both `left` and `right`.
- Inside `NativeTabs`, `insets.bottom` includes the tab bar only when it runs along the bottom. Never add a fixed tab bar height.
- Pad the content container with insets, not the root view.
- Read `useWindowDimensions` at render time. The left Split View window is 469pt wide.

## Expo Router

- Header buttons in the rail stack in one column, Back or Close first. Text-only items stay horizontal. Custom views are excluded.
- A Live Activity in the Dynamic Island can shrink toolbars into overflow. Don't fight it.
- `<SplitView>` wraps the system split view: one column folded, two open, fold-aware. **Experimental in SDK 58.**
- `NativeTabs` `preferredPlacement`: `'sidebar' | 'tabBar' | 'automatic'`. Applies on the open display in landscape.

## Extra APIs

| Need | API |
|---|---|
| Two-pane content (iOS 27.1 only, older versions render children without a container) | `ArrangementView` from `@expo/ui/swift-ui`, inside a `Host`, with `ArrangementView.Primary` and `.Secondary`. Style with `arrangementViewStyle('split' \| 'overlay')`, `splitArrangementLayoutSize`, `overlayArrangementEdge`. Modifiers from `@expo/ui/swift-ui/modifiers`. |
| Fold and occlusion frames | `npx expo install react-native-reserved-regions`, then `useReservedRegions()` returns `{ kind: 'division' \| 'occlusion', frame }` in points. Good for custom game controls and even-column grids. Do not use it to split content at the fold, use `ArrangementView`. |
| Hinge angle and status | `npx expo install expo-hinge`. `useHinge()`, `getHinge()`, `addHingeListener()`. Status: `closed`, `partiallyOpen`, `fullyOpen`, `unknown`. SwiftUI modifier `onHingeChange` can run on the UI thread via `useWorkletCallback`. Works with Reanimated and Android 11+ foldables. |
| Rail edge | `useVerticalBarEdgeIOS()` returns `'leading'`, `'trailing'` or `null`. **Not a Duo detector** (open portrait returns `null`). |
| Disable the rail | `<StatusBar verticalBarBehaviorIOS="disabled" />` (maps to `preferredVerticalBarBehavior`). Only for video players or calculator-style screens, and keep the choice stable per screen. |

## Orientation

On iOS 27, orientation locks are preferences in resizable contexts. `lockAsync` can be refused and `requireFullScreen` no longer opts out. Locking to portrait or landscape on Duo works only if the app fills the screen through pose changes.

## Known limits

- StandBy is unavailable in the Duo simulator, and most app extensions are unavailable in Xcode 27.1's simulator. Test widgets and extensions on device.
- `expo-app-intents` (alpha, also SDK 58) exposes actions to Siri, Shortcuts and Spotlight. Some schemas need newer iOS than their domain (`.mail.openDraft` needs iOS 27). Unrelated to layout.

## Test checklist

- **Folded:** nothing important under the rail, buttons respond.
- **Open:** layout does not switch designs, nothing under the rail, portrait bars return to top and bottom.
- **Partially open:** nothing essential in the fold, sheets and popovers land on one side.
- **Split View:** content clear of the rail (left edge of the left window).
- **Folding mid-screen:** scroll position, state and actions persist.
- **Standard iPhone:** nothing changes.

## Audit workflow

1. Confirm SDK 58 and rebuild.
2. Grep for custom headers or tab bars (`headerShown: false` plus hand-built bars, `TabList`) and move to `Stack` and `NativeTabs`.
3. Grep for hard-coded `top`, `bottom`, `left`, `right` offsets, fixed tab bar heights, and root-level padding. Replace with insets.
4. Check carousels, FABs and toasts per the safe-area list.
5. Pick two-pane screens: `SplitView` or `ArrangementView`.
6. Decide per screen on reserved regions or hinge only if a custom layout truly needs them.
7. Verify in Device Hub, then in CI (below).

## CI: run it on the Duo simulator

Use the `expo:eas-workflows` skill (fetch the live schema first, do not guess job params). A sensible shape from the CI/CD tutorial: PR-triggered simulator build on the `sdk-58` or `latest` image, optional Maestro E2E, then fingerprint-based choice between a native build and an EAS Update for production. Validate with `npx -y eas-cli@latest workflow:validate .eas/workflows/<file>.yml --non-interactive`. Workflows consume paid EAS minutes.

## Common mistakes

| Mistake | Fix |
|---|---|
| Padding the ScrollView with insets | `SafeAreaView` around it, `contentInsetAdjustmentBehavior="automatic"` |
| Fixed tab bar height in padding | Use `insets.bottom` from safe area |
| Using `useVerticalBarEdgeIOS()` to detect Duo | It is only the rail edge, null in open portrait |
| Splitting content at the fold with reserved regions | `ArrangementView` or `SplitView` |
| Hand-built JS header or tab bar | `Stack` and `NativeTabs` |
| Floating button at `right: 16` | `right: insets.right + 16` |
| Assuming `lockAsync` always succeeds | Treat as a preference and fill the screen |
| Testing only on a standard iPhone | Device Hub, every pose |
