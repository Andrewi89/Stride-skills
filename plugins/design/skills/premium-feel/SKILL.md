---
name: premium-feel
description: "Use when designing, building or reviewing an app or site that should feel premium, polished or luxurious, or when someone says it feels cheap, unfinished or off without knowing why. Two layers: the state and trust details whose absence makes a product feel cheap, then the restraint, type, colour, motion and distinctiveness that make it feel expensive. Pairs with design-copy for the words and anti-slop-design for websites."
---

# Premium feel

Cheap products leave doubt. Premium ones remove it, then show restraint. Fix layer 1 before touching layer 2: beautiful type never rescues an app that loses someone's form data.

## How to use this

- **Building:** apply layer 1 to every screen as you build it, then layer 2. Design the failure and empty states before the happy path.
- **Reviewing:** walk the checklist at the end. Report each finding with where it is, why it reads as cheap, and the specific fix. Order findings by how much doubt they cause the user, not by how easy they are.
- **Not sure what the product should feel like?** Ask for the brand, the audience and one or two products the owner admires before choosing type, colour or motion. No brand guide yet: `mini-design-system` first.
- **Exploring:** offer three distinct directions, not one. For anything that moves, prototype it with controls that trigger each state (add, succeed, fail, reset) so the motion can be judged before it's built for real.

## Layer 1: don't feel cheap

Each item is small. Missing several makes a product feel thrown together, even when nobody can say why.

### Every state is designed

Failure states reveal more about a product than success does.

- **Every action confirms.** A tick, a toast, a state change. Nobody should wonder whether it worked.
- **Every wait explains itself.** Respond to a tap within 100 ms, even if only with a pressed state. Under a second, show nothing extra. Longer, use a skeleton in the shape of the real content, or step text that says what is happening ("Checking availability"). Never a bare spinner with no end. Uncertain waits feel longer than explained ones.
- **Treat latency as a design material.** Update optimistically when the action is safe to undo. Prefetch the obvious next screen. Reserve space so nothing jumps as it loads.
- **Every dead end has an exit.** Empty states, errors and finished flows each offer one clear next step.
- **Errors name the problem and the fix.** "Password needs 8 or more characters", never "Something went wrong". Wording rules live in `design-copy`.
- **Helper text wherever the outcome is unclear.** Who sees this note? When is the card charged? One line under the field removes the pause.
- **No accidental choices.** Decisions that matter (an answer, a purchase, a delete) need a deliberate confirm, not a tap someone can make while rushing through.

### Trust before asking

- **A legal line where people hand over details.** "By continuing you agree to the Terms and Privacy Policy" above sign-up and payment buttons. It signals a real business.
- **Permissions in context, after value.** Location when they open the map, notifications after the first thing worth being told about. Never a stack of system prompts at launch.
- **Never ask twice.** Prefill what the app knows, remember what they entered, carry it between steps.
- **Say what happens to their data** when the product reads personal things (messages, files, health, location): what it reads, where it lives, how long it's kept.

### Respect their time and control

- **Filters show what's active and offer "Clear all".**
- **Never truncate what a decision depends on:** prices, dates, fees, names, terms. Truncate decoration, not facts.
- **Labels say exactly what happens.** "Confirm purchase", not "Let's go".
- **Keep context visible.** In long conversations, chat and multi-step flows, let people scroll back to what was said or chosen earlier.
- **Put text next to what it refers to.** A label by its control, a caption by its image, a message by the person who sent it.

### Consistency the eye notices

- **One icon family:** one stroke weight, one corner style, filled or outlined by rule, no tinted blobs behind them.
- **One spacing scale and one radius scale,** used everywhere.
- **Design with real content:** the longest name, the 3-line title, the missing photo, the largest text size.
- **Every interactive element has pressed, hover and focus states.** Disabled states say why when they can.

## Layer 2: feel expensive

Luxury is mostly subtraction. Each item is a decision to do less, better.

### Restraint

One primary action per screen. Fewer elements, more space around them. Space is the cheapest luxury material, and crowding is the fastest way to look cheap. Before adding anything, remove something.

### Type

- One family, two at most. A clear scale with real contrast between sizes, never five sizes that nearly match.
- Hierarchy from size, weight and space before colour, boxes or lines. Big and bold says "important"; small and light says "footnote".
- Tighten tracking and line height on large display text. Loosen both on small text so each letter stands apart.
- Tabular figures for numbers that line up or change. Real quotes and apostrophes.

### Readable, not just beautiful

Designers drift towards small, light, high-contrast type because it looks refined. It's tiring to read.

- Go a size bigger than feels classy. Allow for viewing distance: a tablet on a lap is two or three times further away than a phone. Support system text scaling.
- Lines of roughly 45 to 75 characters. Don't stretch text to fill empty width.
- Left-align anything longer than one line.
- High stroke contrast (hairline thins, fat stems) only at display sizes. Body text wants an even face at regular weight, a touch heavier on dark backgrounds. Never light weights for body.
- All caps, italics and monospace for emphasis only, never running text.
- Text over imagery needs a backing: a solid panel, a scrim, or a bolder weight. Keep recurring text (captions, subtitles, dialogue) in one fixed place.
- Before committing to a font, check: it covers every language needed, including accents; kerning is on (set "AVATAR" and look at the gaps); confusable letters are distinct ("Illinois"); and which OpenType features it has (tabular figures, alternates).
- For dyslexic readers, a larger x-height and looser spacing in your own font works about as well as a dyslexia font, and keeps the look intact.
- A striking look buys a little patience from readers. Not much.

### Colour

- A quiet neutral base and one accent, rare enough to mean something.
- Tint neutrals and shadows slightly towards the brand rather than flat grey and pure black.
- No gradient, glow or glass by default. Each one has to earn its place.

### Imagery

Fewer, better images with one consistent treatment. Real photography over stock. Correct aspect ratios, no awkwardly cropped faces. Images fade in rather than pop.

### Motion

- **Quick:** most interface transitions take 150 to 300 ms. Ease out on entry.
- **Physical:** things move from where they came from and can be interrupted mid-gesture.
- **Purposeful:** motion explains a change of state or place. No bounce for its own sake.
- **Depth from layering:** foreground and background moving at slightly different rates gives a sense of space. Use it sparingly.
- **Two moments get the best motion:** the first screen someone sees, which can take its time, and the moment they succeed, which can land with a small settle or a burst of particles.
- Respect reduced-motion settings.

Name the technique when asking for motion. "Add animations" gets bland results.

| Technique | Use it for |
|---|---|
| Layout transition | Items reordering, a list becoming a grid, a card opening into a page. The easiest premium win, natively supported on most platforms. |
| Spring | Buttons, toggles, anything that should feel physical. Choose gentle, snappy or bouncy deliberately. |
| Gesture with momentum | Dragging, swiping, flinging. Tracks the finger exactly, carries speed on release, overshoots slightly, settles. |
| Keyframes | A choreographed sequence from state A to B: position, size, colour, opacity. |
| Path and shape morph | Movement along a curve, or one vector shape becoming another. Jagged edges mean the path needs more points. |
| Particles | Confetti or sparkle on a real achievement. Rarely. |
| Shader | Pixel effects such as refraction, blur or glow on custom surfaces. |
| Physics | Things that should fall, collide or respond to tilt. |
| Rive or Lottie | Characters and illustrated animation, built as a state machine where every animation returns to a resting state. |

Review motion by eye, slowed down, frame by frame. Nothing automated can judge whether it feels good or spot a clipped edge. When something feels off, it's usually the easing: start faster, or settle more slowly.

### Pace and manners

- Calm. No countdown timers, stacked modals, nag screens or upsells at the moment someone finishes a task. Luxury never begs.
- Haptics on confirmations and meaningful moments only. Sound rarely, never by surprise.
- Copy is short and confident. No exclamation marks, no "Oops!", no jokes in errors.

### Distinctive, not generic

Anything that looks like it already exists reads as cheap, however clean it is.

- Own at least one thing nobody else has: a custom or rarely used typeface, a house illustration style, a signature shape.
- Start from something made by hand (sketches, painted marks, real photographs). Use AI to extend that style, never to invent it. Clean default AI imagery looks like everything else.
- Judge the design in its real context: on the actual device, the real page, the shopfront, next to the competition. Never only on a blank artboard.
- One unusual, well-made detail beats ten clever ones. Premium feels inevitable rather than inventive.

### Systems people can't get wrong

When others will use the design (a client's team, another developer, future you), give them a few fixed choices rather than open rules: two layouts, two type widths, a short colour list, templates filled with real content, and a short demo of the system in use. Fewer options, fewer mistakes, and the brand stays intact after handover.

### Edit content to fit the design

Long titles, dense paragraphs and documents that link away mid-thought are design problems. Set a template with fixed lengths, then cut the copy until it fits. Short paragraphs people can skim beat complete ones nobody reads.

### Budget the last mile

Getting it working is most of the build. Making it feel right is a separate pass after that. Plan time for it rather than squeezing it in.

## Review checklist

1. Walk every flow down its failure path: no network, bad input, empty account, slow response. Does each state have a design and an exit?
2. Does every action confirm, and does every wait over a second explain itself?
3. Does anything jump as it loads?
4. Is anything asked for twice, or before the user has a reason to trust the app?
5. Any truncated price, date, fee or term? Any important choice made with a single careless tap?
6. Icons: one family, one weight?
7. Count primary actions per screen. More than one? Remove one.
8. Count type sizes and colours. Can either list shrink?
9. Squint: is the one important thing still obvious? Read a paragraph at arm's length: still comfortable?
10. Put a screenshot next to the best product in its category. What's the first difference you notice? Fix that.
11. Could this have come from any other company? Name the one thing only this product has.

## Related skills

- Interface wording (errors, empty states, permission strings): `design-copy`.
- Websites and landing pages that look AI-made: `anti-slop-design`.
- Apple platform specifics: `apple-design-duo`, and Apple's [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/).
- Motion craft in depth: Emil Kowalski's skills ([emilkowalski/skills](https://github.com/emilkowalski/skills)), installed by `install-others.sh`.
