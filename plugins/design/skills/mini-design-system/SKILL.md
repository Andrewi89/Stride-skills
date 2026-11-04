---
name: mini-design-system
description: "Use when a product has no brand guide or design system yet, when AI-generated screens keep drifting off-brand or into the generic AI look, or when someone asks for a brand guide, style guide or design rules an AI can follow. Builds a compact, AI-readable style guide from the product's goals and real competitor references, then turns it into a project skill that loads whenever that product's UI is created or changed."
---

# Mini design system

AI drifts back to its defaults on every new screen unless something stops it. A full design system (80 colours, 50 components) is too much for an agent to hold in context, so it gets ignored. A mini design system is small enough to load every time and specific enough to keep every screen on brand.

## 1. Gather the inputs

Ask for, or infer and confirm:

- **What the product is and who uses it.** "A finance app for freelancers", not "a SaaS platform".
- **Mode and mood in plain words.** Light or dark, quiet or loud, warm or clinical, dense or airy.
- **2 to 4 products it should sit alongside,** usually respected competitors or adjacent tools.
- **Anything already decided:** logo, typeface, colour, app screenshots.

Then study real shipped interfaces from those products: live sites, the App Store, or a library of production screens. Prefer shipped, user-tested designs over concept shots from design showcases, which look good and often don't work. Note what they do, never copy them.

## 2. Write the guide

Hard limits keep it loadable. If a section grows past its limit, cut.

| Section | Contents | Limit |
|---|---|---|
| Principles | 3 to 5 lines on how the product should feel and what it must never look like | 5 lines |
| Colour | Neutrals, one accent, semantic colours (success, warning, error), each with a hex value and its job | about 20 tokens |
| Type | One family (two at most), a size scale with its uses, weights, line heights | 6 to 8 sizes |
| Space and shape | Spacing scale, radius scale, border and shadow rules | 1 line each |
| Components | Only the core set, each with its states and one rule: button, input, badge or tag, segmented control, list or table row, card or metric tile, empty state | 6 to 10 |
| Imagery and icons | Icon family and weight, photo or illustration style | 2 to 3 lines |
| Voice | How it talks in 3 lines, plus 3 example labels or messages | 6 lines |
| Never | The specific AI tells this product must avoid (see `anti-slop-design`) | 8 to 10 lines |

Make the choices distinctive. A guide that lands on Inter, a purple accent and soft shadows has only written the AI defaults down. Give the reasoning in a few words beside each choice so later changes stay in the spirit.

Show it before turning it into a skill: render the tokens and core components on one page (local HTML is fine) so the owner can see and approve it.

## 3. Turn it into a project skill

Save it as a skill in the product's repo, for example `.claude/skills/<product>-design/SKILL.md`, with:

- A description that triggers on any UI work for this product: "Use whenever creating or changing any <product> screen, component, page or email."
- The guide itself, in the table and list form above. No prose essays.
- An instruction to check every new screen against the Never list before finishing.
- A pointer to the component code if it exists, so the agent reuses components instead of redrawing them.

Keep it under 200 lines. If it can't fit, the product needs a real design system in code, not a longer skill.

## 4. Use it

- **New screens:** "Build <screen> for <product>, inspired by how <respected product> handles it." The agent studies the reference, then applies the product skill. Take the structure, never the look. Change the palette and type so it's clearly your own.
- **Imagery:** generate or commission images in the guide's style rather than using stock. Extend a hand-made or house style; don't let a model invent one each time.
- **Improving a screen:** say what's wrong, not "fix it". "Distil this: fewer elements, lighter actions." "Quieter: less colour, less weight." "Bolder: stronger hierarchy." Specific direction gets senior-looking results; vague requests get more slop.
- **Drift:** when a screen looks off-brand, fix the guide if the rule was missing, then fix the screen.

## Related skills

- Spotting the AI look: `anti-slop-design`.
- Polish once the system is in place: `premium-feel`.
- Interface wording: `design-copy`.
