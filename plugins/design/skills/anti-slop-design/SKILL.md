---
name: anti-slop-design
description: "Use when designing, generating or reviewing a website or landing page, especially one built with AI, or when a site looks vibe-coded, templated or like every other AI startup. Lists the visual, motion, copy and structure tells of AI-made sites, and the conversion basics they usually miss. The design partner to anti-slop-writing. For app polish use premium-feel."
---

# Anti-slop design

AI design tools drift to the average of everything they've seen, and they're rewarded for showing off: motion, glow, gradients. A visitor is in a hurry and wants three answers: what is this, is it for me, what do I do next. A vibe-coded site looks busy and answers none of them.

Today's AI defaults will date the way an 80s kitchen did. In five years they'll read as "mid-2020s AI site". Resist the default and pick something that belongs to you.

## How to use this

- **Before designing:** get the brand (typeface, colour, tone), the audience and the one action the page exists for. If there's no brand yet, propose a small one first (section 3). Don't start from defaults.
- **Building:** satisfy section 1 before any styling. Then check every design choice against section 2 as you make it.
- **Reviewing:** run the checklist. Report each finding with where it is, which tell it is, and the specific fix. Put anything that blocks the three questions first.

## 1. Answer the three questions above the fold

- **What it is,** in specific words. "Drafts replies to your email in your voice", not "Institutional intelligence and decision infrastructure".
- **Who it's for.** Write to the user with the problem, not to investors. A site that reads like a pitch deck (markets served, guarantees, "who we partner with") is talking to the wrong person.
- **The one action,** visible without scrolling. If the action is typing (an email, a prompt), show the input already open on the page. Every extra click or popup before it costs conversions.
- One primary button colour, used once per view. Two identical primary buttons make people hunt for the right one.
- If the action is free, make "Free" big. There's a reason pricing pages do.
- Never make people choose who they are ("Enterprise / Mid-market / PE") before they've learned what you do.

## 2. The tells

Each one is fine on purpose. Several together read as unedited AI output.

**Visual**
- The default AI fonts: Inter everywhere, Space Grotesk, Instrument Serif headings. They're the em dash of web design.
- The first wave: purple-to-blue gradients, gradient text in the headline, emoji everywhere, glowing buttons with huge coloured shadows.
- The current wave: warm beige or cream backgrounds, a big serif display headline over small sans body text, and cards that float with a soft glow or drop shadow and don't quite belong to the layout. The tells keep moving, so judge the whole look against what every other AI-made site looks like this year.
- Dark mode with neon accents and glass cards by default.
- A grid of identical cards, each with an icon in a tinted circle, a bold title and two lines.
- A pill badge above the headline ("✨ Now with AI"). Sparkle emoji as decoration. Emoji used as feature icons.
- Tiny all-caps grey labels above every section.
- Huge padding around a hero that says little. White space is a luxury only when what sits in it is worth looking at.
- Random words in bold in body copy.
- Blinking dots, faders, fake dashboards and decorative UI that looks interactive. If it looks like an input, people will try to type in it. Either make it real or make it obviously a picture.

**Motion**
- Scroll-jacking. Big companies with millions of visits don't do it, because it frustrates people and doesn't convert. Keep native scrolling.
- Animation that delays the action: a button that has to animate in before you can join.
- Auto-advancing tabs and carousels. Assume nobody sees anything past the first tab. If you must, start the timer only when the section is on screen.
- Screen recordings so dense nobody can follow them. A simplified, purpose-made animation of the one key moment beats a real recording of the whole interface.
- Good motion reinforces the message: a laptop lid closing to show "works while you sleep". Motion for its own sake is the tell.

**Copy**
- Vague category words: platform, infrastructure, intelligence, operating system, "for modern teams".
- "Scroll" or "↓" telling people to do what they'll do anyway. Agents always nudge. Humans don't need it.
- A button labelled with an internal product name ("Ronin") nobody knows yet.
- The story you need to tell sitting halfway down the page. Move it to the top.
- Features listed instead of what changes for the person. "Tracks water intake" becomes "A nudge when it's time for another glass". Use `ogilvy-copy`, and have changes proposed before they're applied.
- Generic system messages: "Your request is being processed" instead of "Saving changes" with a progress bar.
- Invented stats, logos or testimonials. Never. See `anti-slop-writing` for the rest.

**Structure**
- Hero, three feature cards, logo strip, testimonial carousel, pricing, FAQ, giant footer, all in the default order with the default spacing.
- Important text at low contrast or tiny sizes because it "looks clean". If it matters, it should be painfully obvious from any angle.

## 3. What to do instead

- **Decide the brand early.** A short brand book before the first page: one typeface that isn't an AI default, one accent colour, how images look, how the product talks. It's the cheapest way to stop looking generic, and the thing founders most often regret skipping.
- **Give the AI context, not adjectives.** Feed it the brand book, real product screenshots, real copy and components. Ten minutes of context saves hours of undoing defaults. No brand yet? Build one with `mini-design-system`.
- **Reference shipped designs, not concept shots.** Real products that have been through user testing beat design-showcase mock-ups. Say what you like about a reference and ask for your own take with your palette and type. Never copy one to one.
- **Make your own imagery.** Generate or commission images in your house style instead of stock or default AI art.
- **Build the site after the app.** A landing page made from the finished product inherits its real screens, colours and motion. One made first invents a brand the product won't match.
- **Direct improvements precisely.** Not "make it better" but "distil: fewer elements, turn the heavy button into a link", "quieter: less colour and weight", or "bolder: stronger hierarchy". Vague requests produce more slop.
- **Show the product simply.** One clear moment, slowed down, beats every feature at once.
- **Choose social proof that matches the audience.** Quotes only from investors make the product look like it's for investors.
- **Earn trust when you ask for data.** An AI product that reads email, files or messages needs to say plainly what it accesses, where data lives, how long it's kept and whether it leaves the device. Put a Trust or Security link in the main navigation and lead with "on-device" or "open source" when it's true.
- **Length signals substance.** A long, well-spaced page and a full footer suggest an established company. Thin pages suggest a weekend project.
- **Spend the last 20%.** The difference between vibe-coded and designed is the pass after it works. With code this cheap to write, polish no longer costs much time.
- **Test with real users, blind.** Ask "what do you think this site is?" without saying it's yours, or they'll be polite. Then watch whether they find the button.

## Review checklist

1. In five seconds above the fold: can a stranger say what it is, who it's for and what to do?
2. Is there exactly one primary action, visible without scrolling, with any input already open?
3. Count the tells from section 2. Three or more, start fixing from the top of the list.
4. Is the font one an AI would pick by default? Change it.
5. Does anything hijack scrolling, auto-advance or look clickable when it isn't?
6. Is every claim specific and true, and every testimonial real?
7. If the product touches personal data, can a visitor find out what happens to it in one click?
8. Would this page be mistaken for any other AI startup's? What's the one thing only this company has? (See `premium-feel`.)

## Related skills

- App and product polish, type and motion craft: `premium-feel`.
- A compact brand guide an AI can follow: `mini-design-system`.
- Words on the page: `design-copy`, `anti-slop-writing`, and `ogilvy-copy` for selling copy.
- A deeper anti-pattern audit: `impeccable` by Paul Bakaus, installed by `install-others.sh`.
