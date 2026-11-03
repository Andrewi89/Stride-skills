---
name: apple-design-duo
description: Use when designing, building, or reviewing an iOS app, game, or mockup that must run on iPhone Duo (Apple's dual-display foldable iPhone), or when dealing with its outer/inner displays, hinge or fold, device poses, reserved regions, arrangement views, toolbars and tab bars on the vertical axis (side bars), or making fold and resize transitions feel fluid and polished.
---

# Designing for iPhone Duo

## Overview

Source: Apple Human Interface Guidelines, "Designing for iPhone Duo" (new page, September 9, 2026).
https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo

Core principle: one app that resizes fluidly across two displays and many poses. Don't design a layout per pose; use size classes (compact width = outer display, regular width = inner display) and let standard system components do the adapting. All normal iOS HIG still applies.

Fetch the page above when you need the exact wording or the developer API for a rule.

## The hardware in one paragraph

Outer display (used closed): wider and shorter than other iPhones, camera fixed in a corner and always visible. Inner display (used open): camera hidden behind the display until active. A center hinge allows book-style, flat, and standing-on-edge poses. Toolbars, tab bars, status bar, and Dynamic Island sit **on the side** (vertical axis) everywhere except the inner display in portrait.

## Quick reference checklist

**Layout**
- Build to resize: size classes, layout margins, safe area insets. No fixed widths, nothing tied to one display.
- Same functionality and state on both displays and in every pose. Inner display may add one extra level of hierarchy (Mail: list or message when closed, both side by side when open).
- Respect reserved regions: outer camera (always, grows into Dynamic Island), inner camera (only when active), folding region (only when partially open). Use `ReservedRegion` (SwiftUI) / `UIView.ReservedRegion` (UIKit) for custom components.
- When folding: prefer self-adapting containers (split views even out pane widths), use an even number of grid columns, make small adjustments, never dramatic rearrangement.
- Split views: expand on inner, collapse to one pane on outer, automatically.
- Arrangement views (`ArrangementView` / `UIArrangementViewController`): two views, primary + secondary. *Split* (side by side or stacked, from HStack/VStack-like layouts) or *overlay* (layered, from ZStack-like layouts). Keep navigation containers outside them.

**Vertical controls**
- Keep the system's side placement; in general don't override it.
- Content area is asymmetric: use safe areas so side controls (including another app's in Split View) never cover content. Controls stay on the same side in RTL languages.
- Toolbar order, top down: primary navigation (Back, Close), then prominent actions (Done), then the remaining groups as-is.
- Overflow goes bottom to top by default; set visibility priority (`ToolbarItemVisibilityPriority` / `UIBarButtonItemVisibilityPriority`) so frequent actions (Compose, New Note) and badged items stay visible.
- Group items with `ToolbarItemGroup` / `UIBarButtonItemGroup`; never add manual fixed spacing.
- Every non-text toolbar item gets both a title and a symbol. Minimize text-only buttons (they stay in a horizontal bar).
- Space tight: navigation-focused views compress the toolbar into overflow (default); task-focused views minimize the tab bar instead (`ToolbarVerticalCompressionBehavior` / `UIVerticalBarCompressionBehavior`).
- Use the system overflow menu; ellipsis is for overflow only.
- Controls that belong to a non-trailing pane stay next to that pane (Mail list controls stay above the list).
- Immersive, non-scrolling UIs may span full width if nothing clashes with the Dynamic Island or status bar (Calculator goes 5 columns x 4 rows).

**Games**
- Playable in every pose. Orientation lock is fine, but fill the screen. Keep text and control sizes consistent. Prefer changing aspect ratio over letterbox/pillarbox; if unavoidable, fill padding with artwork.

## From Apple's tech talks

Detail from the three Duo tech talks that the HIG page doesn't spell out (111466 *Design for iPhone Duo*, 111462 *Raise the bar with iPhone Duo*, 111463 *Strike a pose with adaptive layouts*).

**System behaviour to design around**
- Outer display: controls sit on the **right** side for right-thumb reach. Dynamic Island expands vertically as Live Activities arrive, and shares the side strip with app bars. Out of room means app items auto-collapse into overflow.
- Partially folded (book): text, images and interactive elements shift away from the curve. In portrait fold, interactive elements move to the bottom half.
- Split View multitasking: drag an app to the side using the home gesture, giving an even 50/50 split. Each app's controls sit on its outer edge.
- Picture in Picture can pin to the top; the app below resizes vertically, and the video fills half the screen when folded.
- Sheets: on the outer display, sheet toolbars go vertical. On the inner display, sheets are centered with horizontal bars. When folded, sheets slide off the fold. With `preferredPlacement`, a left-placed sheet has no vertical bar and a right-placed one gets one.
- Built-in fold avoidance (sheets, alerts, menus, toolbar buttons and more) nudges interactive elements off the crease. **Scrollable content doesn't need to avoid the fold.**

**Opting in to vertical bars**
1. Rebuild against the latest SDK.
2. Use the bars owned by navigation containers: SwiftUI `.toolbar` on `NavigationStack`, `NavigationSplitView` or `TabView`; UIKit items set on a view controller inside `UINavigationController`/`UITabBarController`. Custom `UIToolbar`/`UINavigationBar`/`UITabBar` content is **not** moved.
- Only containers on the display edge go vertical. In a split view only the detail column does; inspectors don't get their own vertical bar.
- Mapping: top toolbar items go to the top of the strip, bottom items to the bottom, and the tab bar stays bottom-aligned. Flexible spacers are zero height; fixed spacers keep their size.
- Back/Close: automatic with a navigation controller. Custom ones use `.cancellationAction` (SwiftUI) or a leading item with `leftItemSupplementsBackButton = false` (UIKit). Prominent actions use `topBarPinnedTrailing` (SwiftUI) or `pinnedTrailingGroup` (UIKit).

**What goes vertical, what stays horizontal**
- Vertical bars have a fixed width and flexible height, so they suit symbol-only items. Items with an icon go vertical; text-only items (Edit, segmented controls, wide text buttons) stay in the horizontal nav bar.
- Override with the new **AxisBehavior** API: use horizontal-only for an item that morphs between symbol and text (a custom Select; the system Edit button handles this itself), and vertical-preferred for a custom view that has a vertical form (for example a compass).
- Turn text and symbol items into symbol-only with a badge (iOS 26 badge API), for example an inbox count. Keep the text if it carries real information (a cart total).
- Keyboard accessory bars stay attached to the keyboard.
- Custom views: fit the fixed width or provide a vertical layout. Read `toolbarVerticalEdge` (environment value or trait), which is nil when bars can't be vertical.
- Vertical bars have **no scroll-edge effect by default**. They get a background only when Reduce Transparency is on, so custom content must stay legible either way.
- To opt out (a single-page, bottom-heavy app like Calculator, or a sheet with only a Close button), use `toolbarVerticalBehavior` / `preferredVerticalBarBehavior`. A sheet without a vertical bar stops just short of the camera.
- Compression per view: `toolbarCompressionBehavior`. Visibility priority can be high, low or custom; set it by group first, then by item.

**Layout patterns**
- Outer display: most content needs an offset so it isn't hidden behind the controls, which aligning to horizontal safe area insets does for you. Center on the full display only for immersive, non-scrolling UI where nothing interactive sits under the bars. A mixed approach is a full-width background with inset scrolling content, keeping all interactive elements inside the inset area.
- Inner display, so it isn't just a stretched phone app: use a split view, a stacked layout that becomes 2 columns when wide (Music), or, for information-dense apps, the tab bar shown as a sidebar (Health).
- Optional table (laptop) pose layout: media on top, controls on the stable bottom half. It must keep every control and the same hierarchy.
- **Displacement**: move an element out of a reserved region into the region that suits its purpose. Choose the scope: move an element alone if it stands alone, move related elements together, and don't move things far from their source. In book pose, alerts go to the trailing side, near where they'll reappear when closed. In table pose, glanceable content goes top and tappable controls go bottom. Search stays over the view it searches. For a grid, keep the outer margins and widen the gutter at the hinge (Fitness).
- System split views even out to 50/50 when folded (Reminders).

**Reserved region API**
- SwiftUI: `reservedRegion` on `GeometryProxy` (from `GeometryReader` or `onGeometryChange`). UIKit: `reservedRegion` on `UIView`. Use `.frame` for layout.
- There are two kinds. A **division** region (the fold) is active only when folded and is zero width when flat. An **occlusion** region (the inner FaceTime camera) is active only when the camera is on.
- Active regions are returned by default; use `includeInactive` to plan ahead (for example, choose an even column count whenever a division region exists).
- For camera-centric apps, keep key content and controls clear of the inner camera.
- Fold state as an interaction input is covered in the talk *Leverage multiple displays and scenes on iPhone Duo*, which isn't in this skill.

**Arrangement views (iOS 27.1)**
- SwiftUI: `ArrangementView(primary, secondary)` inside a `NavigationStack`, styled with `.arrangementViewStyle(.split)` (the default) or `.overlay`. Use `.split.axes(...)` to limit split direction; if it can't split along the primary axis, it shows only the primary view.
- UIKit: `UIArrangementViewController` as the nav controller's root, `updateArrangement` with `UISplitArrangement`.
- Overlay: stacked when flat, side by side when folded. Read `overlayArrangementZIndex` (SwiftUI), or `state(for:)` then `.zIndex` (UIKit), to switch between collapsed and expanded secondary views.
- Choosing: follow existing patterns (HStack/VStack becomes split, ZStack becomes overlay). Otherwise use **overlay** for a foreground/background relationship where partly obscuring scrollable content is fine (Accessibility Reader), and **split** for main/detail where neither view may be obscured (Podcasts transcript).
- Don't put navigation containers inside an ArrangementView, and don't put an ArrangementView inside `List`/`ScrollView`.

**Readiness audit (from the talks)**
1. Rebuild with the latest SDK.
2. Audit bars: system containers, item order, symbols with titles.
3. Make custom items vertical-ready.
4. Set overflow priorities.
5. Audit centered layouts: should each become 2 columns, be displaced, or use an ArrangementView?
6. Adopt the reserved region API for high-priority, manually laid out controls.

## Duo craft layer (from the apple-design skill)

The HIG says *what* adapts. This section applies Apple's fluid-interface and design-principle guidance (WWDC *Designing Fluid Interfaces*, *Principles of Great Design*) to *how* it should feel on Duo. These are applied principles, not HIG rules. For the full motion toolkit (projection, rubber-banding, velocity handoff), also load Emil Kowalski's `apple-design` skill (from `emilkowalski/skills`) and translate its web examples to SwiftUI/UIKit.

**Folding and resizing motion**
- Folding is a continuous, user-driven gesture. Layout changes that follow it (pane widths evening out, grid reflow, content moving off the folding region) should track the hinge smoothly and be interruptible: a person can stop or reverse mid-fold, so always animate from the current on-screen value, never snap to the end state.
- Use critically damped springs for reflow (SwiftUI `.spring(duration: 0.4, bounce: 0)` or `.smooth`; UIKit `UIView.animate(springDuration:bounce:)` with `bounce: 0`). No bounce: the user didn't flick anything, so overshoot reads as broken.
- Spatial consistency across displays: when someone opens the device, the item they were looking at on the outer display stays the anchor (Mail's open email becomes the trailing pane, not a fresh screen). Keep scroll position and selection; the extra hierarchy level appears *beside* it.
- Small adjustments over rearrangement (HIG) is the same rule as "hint in the direction of the change": elements should visibly slide toward their new spot, not teleport.

**Side controls as a material layer**
- Side toolbars and tab bars float over content with no scroll-edge effect and no background by default (per the tech talk). Don't add a hard divider or your own backing; use safe area insets so content isn't hidden behind the bar.
- Custom views placed in the bar must stay legible over whatever scrolls behind them, and over the solid background that appears with Reduce Transparency.

**Principles mapped to Duo**
- *Familiarity*: don't override the vertical bar placement; it's the platform's new muscle memory.
- *Grouping and mapping*: controls stay next to the pane they affect (Mail list controls above the list).
- *Wayfinding*: in every pose, people should still answer "where am I, how do I get back". Back/Close is always at the top of the vertical axis.
- *Flexibility*: one adaptive layout, Dynamic Type scales with it. Test the largest text size on the narrow-tall outer display with side bars present.
- *Response*: pose changes must never block input. Taps during a fold should still land.

**Accessibility**
- With Reduce Motion on, replace reflow slides/springs with short cross-fades.
- With Reduce Transparency on, side bars become solid.
- Large surfaces moving during a fold: keep motion short and avoid big brightness jumps.

## Common mistakes

| Mistake | Fix |
|---|---|
| Custom layout per pose | Size classes plus resizable layout |
| Hiding features on the outer display | Same controls everywhere; overflow, don't remove |
| Odd grid column count | Even count so the fold splits it cleanly |
| Moving bars back to top/bottom | Keep the vertical axis default (opt out only for Calculator-style single-page apps or one-button sheets) |
| Custom `UIToolbar` or hand-built bars | Use container-owned bars, or they never go vertical |
| Item that morphs between symbol and text placed vertically | `AxisBehavior` horizontal-only |
| Displacing scrolling lists or articles off the fold | Leave scrolling content alone; displace controls |
| NavigationSplitView inside an ArrangementView, or ArrangementView inside a ScrollView | Navigation outside, scroll containers inside the arrangement's views |
| Symbol-only toolbar items | Add a title too (used in overflow menu) |
| Custom "..." menu next to the system one | Merge into the system overflow menu |
| Tab bar inside an arrangement view | Wrap the arrangement view in the navigation container |
| Layout snaps to end state after a fold | Interruptible, critically damped spring from the current value |
| Opening the device resets scroll or selection | Preserve state; add the extra pane beside the current one |
| Hard divider line or custom backing behind side bars | Leave the bar bare; rely on safe area insets |

Test poses with Device Hub in Xcode.
