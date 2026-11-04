---
name: live-activities
description: "Use when designing or building an iOS Live Activity, Dynamic Island presentation, Lock Screen live widget or home screen widget, especially in an Expo or React Native app. Covers when a Live Activity is the right tool, the presentations to design, Apple's rules, prototyping before native work, and the Expo build path."
---

# Live Activities and widgets

A Live Activity shows something happening right now that the person is waiting on or tracking: a ride arriving, a delivery, a flight, a workout, a timer, a score. It lives on the Lock Screen and in the Dynamic Island while they use other apps. A widget is the calmer sibling: glanceable state on the home or Lock Screen, always there.

## 1. Is it the right tool?

Use a Live Activity only for an event with a clear start and end that the person cares about minute to minute. Not for ads, promotions, news feeds or general app state. Something that's always relevant (today's progress, a balance) is a widget. A one-off message is a notification.

An activity runs for up to 8 hours, then the system ends it. It can stay on the Lock Screen for a few hours after that. End it yourself as soon as the event is over.

## 2. Read Apple's rules first

Before designing, fetch and read Apple's current Human Interface Guidelines for Live Activities and widgets, and the ActivityKit and WidgetKit docs. The sizes, padding, presentation rules and allowed interactions change between iOS versions. Never design from memory.

## 3. Design every presentation

One activity needs a design for each place the system may show it. The system picks which one.

| Presentation | When it shows | Design for |
|---|---|---|
| Compact (leading and trailing) | The only activity running, app in the background | The one number or icon that matters, on each side of the camera. Hug the island; no padding gaps. |
| Minimal | Several activities competing | A single glyph or value. Recognisable at a glance. |
| Expanded | Long press on the island | The key info plus at most one or two actions. Leading, trailing, centre and bottom regions. |
| Lock Screen | Lock Screen and notification banner | The fullest view. Brand colour and imagery allowed, still glanceable. |
| StandBy, Watch Smart Stack | Larger, further away | Check how the Lock Screen design scales. |

Rules that hold everywhere:

- Glanceable in under a second: one primary value, large and high contrast.
- Show progress as progress: a bar, a ring, a filling shape, an arriving icon.
- For countdowns and timers use the system's date-relative timer text, which ticks on its own without updates.
- Tapping opens the app on the exact screen for that activity, never the home screen.
- Buttons (iOS 17 and later) run a small action without opening the app, such as "Log drink" or "Pause". Keep to one or two.
- Animate changes between states with the system's transitions. A rising fill or a count change, nothing flashy.
- Let people switch the activity off in the app's settings, with a preview of what it looks like. They can also disable it in iOS Settings, so the app must work without it.
- Match the app's brand (accent colour, icon, shapes) so it's recognisable at a glance among other activities.

## 4. Prototype before going native

Native widget code is slow to iterate. Prototype first in the browser:

1. Collect a few references of Live Activities you admire.
2. Ask for three distinct variations, each showing compact, minimal, expanded and Lock Screen, on a realistic iPhone frame.
3. Add controls that simulate the real events ("Add drink", "Driver arrives", "Reset") so you can watch every state change and transition.
4. Pick one, refine it, then build it natively to match.

Feedback on motion is easiest as a short screen recording with narration rather than annotated screenshots.

## 5. Build it (Expo)

- **Not in Expo Go.** Widgets and Live Activities need a development build (EAS Build or a local build) and a paid Apple Developer account for signing and device testing.
- **Library:** `expo-widgets` (stable from SDK 56) lets you define widgets and Live Activity slots from the app, with a config plugin that handles the extension target, bundle identifiers and push entitlements. Check the docs for the exact SDK version in `package.json`, because the API moved quickly. Older projects may use `expo-apple-targets` with SwiftUI written by hand.
- **Updates:** start, update and end activities from the app. For updates while the app isn't running (a driver's live position), use ActivityKit push notifications from your server. Widgets refresh on a timeline the system budgets, so they aren't real time.
- **Test on a real device:** the activity appears in the island only when you leave the app. Test long press, Lock Screen, dark mode, several activities at once, and the ended state.
- Before uploading, run `apple-preflight` for entitlements and Info.plist keys.

## Related skills

- iPhone Duo and its outer display, where the island grows: `apple-design-duo`, `expo-duo`.
- Feel and motion polish: `premium-feel`.
- Wording on the activity and its buttons: `design-copy`.
