# Redesign audit (for an existing page)

Adapted from elaya's `redesign-existing-projects` (MIT, which credits taste-skill, MIT). Diagnose first, report, let the owner veto, then fix in the order at the end. Work inside the existing stack; do not rewrite.

## 1. Run the checker and look

`python3 scripts/check.py path/to/index.html` and screenshots at 390 and 1440 px. List every finding with the element and the fix.

## 2. Proof (most sites fail here first)

- Zero or one real image of the product. Fix: get screenshots, real output, a recording.
- The hero visual is decorative (abstract shapes, a stock photo, an icon grid). Fix: show the product doing its one job.
- Claims with nothing beside them. Fix: put the screenshot, number, quote or file next to the claim.
- Mockups with placeholder data ("Lorem", "John Doe", round numbers). Fix: real looking specifics.

## 3. Concept

- Sections that could belong to any product. Fix: one domain metaphor carried through tags, backgrounds, the 404.
- No moment anywhere. Fix: one or two (see system.md, Motion).

## 4. Type

Default fonts (Inter, Roboto, Arial, Helvetica, Open Sans); more than one sans; italic outside the hero flourish; weights 800/900; only 400 and 700 in use; headlines without presence (raise size, tighten tracking to -0.02em); body wider than 75 characters; proportional numbers in data; orphans; Title Case; off scale sizes.

## 5. Colour and surfaces

More than one accent; accent on headings or backgrounds; purple and indigo AI gradient; saturated colour photos fighting the accent; mixed warm and cool greys; background gradients; untinted black shadows; flat empty sections (add a desaturated image, a grid mask or grain, not a gradient); one stray dark band in a light page.

## 6. Layout

Everything centred; three equal cards; 6/6 splits everywhere; `height: 100vh` (use `min-height: 100dvh`); no container; ad hoc spacing; cards forced to equal height; buttons not bottom aligned; no overlap or layering (float UI cards over the hero image); equal top and bottom padding where the bottom needs more.

## 7. Motion and states

Default easing; nothing reveals; raw scroll listeners; nav welded to the top; menu icon swaps without animation; small mobile dropdown; no reduced motion handling; missing hover, active, focus, loading, empty, error states; links to `#`; no current page marker.

## 8. Components

Border plus shadow plus white on every card; always one filled and one outline button (make the second a text link); pill "New" badges everywhere; accordion FAQ as the only pattern (a two column list or a sticky heading beside the answers reads better); three card testimonial carousel; three tower pricing (emphasise the recommended plan with the accent border, not height); four column footer link farm.

## 9. Content

Filler words; vague value proposition; features without outcomes; weak CTA; competing CTAs above the fold; proof at the bottom; no risk reversal (trial, cancel anytime, refund window); passive voice; cute system messages.

## 10. Ship list

See system.md, Ship list.

## Fix order

1. Proof: replace drawn or stock visuals with the real product.
2. Font swap and type scale.
3. Colour: two plus one, flatten surfaces.
4. Hover, active and focus states.
5. Layout and spacing.
6. Motion floor, then one or two moments, then a calm pass.
7. Replace generic components.
8. Loading, empty and error states.
9. Copy pass.
10. Ship list and SEO.
