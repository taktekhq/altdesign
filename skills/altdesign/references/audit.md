# Redesign audit (for an existing page)

Adapted from elaya's `redesign-existing-projects` (MIT, which credits taste-skill, MIT). Diagnose first, report, let the owner veto, then fix in the order at the end. Work inside the existing stack; do not rewrite.

## 1. Run the checker and look

`python3 scripts/check.py path/to/index.html` and screenshots at 390 and 1440 px. List every finding with the element and the fix.

## 2. Scene (most sites fail here first)

- The first screen is type, screenshots or a gradient, not one picture. Fix: a full bleed scene that puns on the headline, in a named style, as a 6 to 10 s loop (`scenes.md`).
- The picture is decorative or stock, has no pun, or has several subjects. Fix: one subject doing one action that is the headline.
- Nothing crosses between art and UI. Fix: art in front of the UI, UI peeking out of the art, or a fixed scene under scrolling content.

## 3. Proof

- Zero or one real image of the product. Fix: get screenshots, real output, a recording.
- The hero visual is decorative (abstract shapes, a stock photo, an icon grid). Fix: show the product doing its one job.
- Claims with nothing beside them. Fix: put the screenshot, number, quote or file next to the claim.
- Mockups with placeholder data ("Lorem", "John Doe", round numbers). Fix: real looking specifics.

## 4. Concept

- Sections that could belong to any product. Fix: one domain metaphor carried through tags, backgrounds, the 404.
- No moment anywhere. Fix: one or two (see system.md, Motion).

## 5. Type

Default fonts (Inter, Roboto, Arial, Helvetica, Open Sans); more than one sans; italic outside the hero flourish; weights 800/900; only 400 and 700 in use; headlines without presence (raise size, tighten tracking to -0.02em); body wider than 75 characters; proportional numbers in data; orphans; Title Case; off scale sizes.

## 6. Colour and surfaces

More than one accent; accent on headings or backgrounds; purple and indigo AI gradient; saturated colour photos fighting the accent; mixed warm and cool greys; background gradients; untinted black shadows; flat empty sections (add a desaturated image, a grid mask or grain, not a gradient); one stray dark band in a light page.

## 7. Layout

Everything centred; three equal cards; 6/6 splits everywhere; `height: 100vh` (use `min-height: 100dvh`); no container; ad hoc spacing; cards forced to equal height; buttons not bottom aligned; no overlap or layering (float UI cards over the hero image); equal top and bottom padding where the bottom needs more.

## 8. Motion and states

Default easing; nothing reveals; raw scroll listeners; nav welded to the top; menu icon swaps without animation; small mobile dropdown; no reduced motion handling; missing hover, active, focus, loading, empty, error states; links to `#`; no current page marker.

## 9. Components

Border plus shadow plus white on every card; always one filled and one outline button (make the second a text link); pill "New" badges everywhere; accordion FAQ as the only pattern (a two column list or a sticky heading beside the answers reads better); three card testimonial carousel; three tower pricing (emphasise the recommended plan with the accent border, not height); four column footer link farm.

## 10. Content

Filler words; vague value proposition; features without outcomes; weak CTA; competing CTAs above the fold; proof at the bottom; no risk reversal (trial, cancel anytime, refund window); passive voice; cute system messages.

## 11. Ship list

See system.md, Ship list.

## Fix order

1. Scene: one moving picture that acts out the headline.
2. Proof: replace drawn or stock visuals below the fold with the real product.
3. Font swap and type scale.
4. Colour: two plus one, flatten surfaces.
5. Hover, active and focus states.
6. Layout and spacing.
7. Motion floor, then one or two moments, then a calm pass.
8. Replace generic components.
9. Loading, empty and error states.
10. Copy pass.
11. Ship list and SEO.
