---
name: design-copy
description: "Use when writing or reviewing the words inside an interface: button labels, errors, empty states, onboarding, permission prompts, loading and confirmation text, release notes. Keeps interface copy short, plain and honest. Defers to apple-design-duo for layout and to anti-slop-writing for style."
---

# Design copy

A good layout with sloppy words still feels cheap. Interface copy is read in a glance, mid-task, so every word earns its place.

Layout, motion and device rules live in `apple-design-duo`. Style bans (banned words, reframes, analogies) live in `anti-slop-writing`. This skill covers what the words on screen must do.

## Rules

- **Buttons use a verb and say what happens.** "Save changes", "Send invoice", "Delete 3 photos". Avoid "OK", "Submit" or "Continue" when something more specific exists.
- **Errors say what happened and what to do next.** "Couldn't save. Check your connection and try again." Never blame the user, never show raw codes alone, never "Oops" or "Something went wrong" with no next step.
- **Empty states say what goes here and how to add it.** "No invoices yet. Create your first one." One line, one action.
- **Loading text names the thing loading** ("Loading your photos"), and appears only if the wait is long enough to notice.
- **Confirmations name the action and its consequence.** "Delete this project? This can't be undone." Buttons: "Delete project" and "Cancel".
- **Permission and purpose strings give the reason in plain words.** "Used to show cafés near you on the map." Say why the app needs access in terms of the user's benefit. A vague string can fail App Store review (see `apple-preflight`).
- **Alerts never use Yes and No.** Repeat the verb: "Delete" and "Cancel". Mark destructive buttons as destructive so the platform styles them.
- **Form errors give the fix, next to the field.** "Enter a postcode, like SW1A 1AA." Avoid "Invalid input" and banners far from the problem.
- **Placeholder text is a hint, never the label.** It disappears as soon as someone types.
- **Icon-only buttons get an accessibility label** using the verb a text button would ("Share", "Delete photo").
- **Onboarding says what the person can do in the next minute.** No feature tours, no welcome speeches.
- **Labels are nouns, instructions are verbs.** Keep one name per thing across the product.

## Style

- Follow the platform's capitalisation. Apple platforms use title case for buttons, menu items and alert titles ("Turn On", "Not Now"). The web and Android use sentence case. Never mix them within one product.
- UK English and UK formats (3 Nov 2026, £12.50). Digits for numbers. Plain words over jargon.
- No exclamation marks, no emojis in system text, no jokes in errors or destructive flows.
- Short beats clever. If a label wraps on the smallest screen, cut words.
- Don't repeat the heading in the body.

## Release notes

Say what changed for the user, in one line each. "Invoices now save automatically." Skip "Improved performance and stability."

## Check before shipping

1. Can someone act on every error without contacting you?
2. Does each button say what it will do?
3. Does every empty state have one next step?
4. Is the same thing called the same name everywhere?
5. Does every icon-only button have a spoken label?
6. Does any line sound like a brochure? Cut it.
