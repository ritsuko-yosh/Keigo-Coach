# Status: Superseded by `.kiro/specs/storybook-book/`

# Polish and Interactions — Requirements

## Overview

Apply the full theme from the homepage-and-navigation spec consistently
across every tab, add signature CSS animations, give Belle interactive
life, enrich the Home tab with a ウチ/ソト diagram and keigo type cards,
add an author section to the About tab, and fix the Phrase Library
duplicate header.

All content comes from CSV and markdown files. All settings, labels,
and UI text live in config.py. No new fonts, libraries, or dependencies
beyond those already in requirements.txt, except for CSS animations
(CSS only) and optional self-contained JavaScript embedded in
components.v1.html for Belle's tap interaction.

---

## US-1 — Theme applied everywhere

> As a user, I want every tab to feel like the same cozy stationery app,
> not a patchwork of different styles.

**Acceptance criteria:**
- Background, card borders, fonts (Caveat headings, Nunito body,
  Zen Maru Gothic Japanese), and washi yellow tags match design.md on
  every tab.
- Washi tape strip decorates the top of every card on every tab.
- Situation tags are sticky-note style (washi yellow, slight shadow).
- Scenario cards in Practice are styled as notebook pages (ruled-line
  background).
- All headings use the Caveat font.
- Phrase Library header is not duplicated (currently shows twice).

---

## US-2 — Signature animations

> As a user, I want the interface to feel handmade and alive through
> small, purposeful animations.

**Acceptance criteria:**
- Title underline draws in from left like a pencil stroke on page load.
- Washi tape strips animate downward onto cards instead of appearing
  instantly (CSS `@keyframes`, staggered by card index).
- Cards lift slightly on hover with a soft shadow increase.
- Practice steps slide in like a notebook page turning (CSS transform,
  respects `prefers-reduced-motion`).
- A "hanko stamp" (正解 in red, rotated ~-15°) slams onto the screen
  when step 4 (sentence) is answered correctly.
- Wrong answers trigger a gentle horizontal shake on the feedback box
  and on Belle.
- Navigating between tabs uses a fade-in transition.
- All animations defined in `assets/style.css` only. No new JS libraries.
- All animations respect `prefers-reduced-motion: reduce`.

---

## US-3 — Interactive Belle

> As a user, I want Belle to feel alive and to react to what I do.

**Acceptance criteria:**
- Belle blinks periodically (CSS animation on SVG elements, no SVG edits).
- After 30 seconds without interaction, Belle shows a "sleep" pose
  (CSS animation with 30s delay; resets on every Streamlit rerender,
  which happens on any interaction).
- Hovering over Belle makes her ears perk up slightly (CSS :hover).
- A small tap button beside Belle triggers a random animation (bow,
  tail wag, or ear flop) and shows a tip bubble with text from
  `data/belle_tips.csv`.
- In Practice: Belle bows on a correct answer, tilts her head on wrong.
- Belle's tips are never invented. Rows in `data/belle_tips.csv` use
  `source = "needs review"` and `verified = false` until confirmed.

---

## US-4 — Home tab: larger situation cards

> As a user, I want the situation cards to show their full description
> without truncation, with a clear icon.

**Acceptance criteria:**
- Each of the five situation cards is a sticky note (washi yellow) with
  a situation icon (emoji) and the full description from `content/home.md`.
- No text is truncated or ellipsised.
- Clicking the card navigates to Practice pre-filtered to that situation.

---

## US-5 — Home tab: ウチ/ソト interactive diagram

> As a user, I want to explore the ウチ/ソト concept by picking who is
> speaking and who is listening, and seeing animated arrows that show
> which keigo is appropriate.

**Acceptance criteria:**
- The diagram has two selectboxes: "Who is speaking?" and "Who is
  listening?"
- Selecting a combination shows an animated HTML/CSS diagram with arrows
  and labels explaining whether 尊敬語 or 謙譲語 is used, and why.
- All actor labels, relationship descriptions, and explanations come from
  `data/uchi_soto.csv`.
- Fictional names only (for example 田中) in any example text.
- Rows in `data/uchi_soto.csv` use `source = "needs review"` until
  confirmed.

---

## US-6 — Home tab: keigo type cards

> As a user, I want to see all five keigo types on the home page with
> a short definition and one example each, before I start practicing.

**Acceptance criteria:**
- Five cards (one per keigo type) are shown below the diagram.
- Each card shows the type name, a one-sentence definition in English,
  and one Japanese example phrase with English gloss.
- All content comes from `data/keigo_types.csv`.
- Cards use the same pastel badge colors defined in config.py and
  style.css.
- Unconfirmed rows are tagged "Source needed".

---

## US-7 — About tab: author section

> As a visitor (including recruiters), I want to know who built this
> and how to get in touch.

**Acceptance criteria:**
- The About page ends with an author section containing:
  Ritsuko Yoshida, one or two sentences on why the app was built,
  links to LinkedIn, portfolio, and email.
- No phone number.
- All text comes from `content/author.md`.
- The author's real name appears only in this section, nowhere else in
  the codebase (not in scenarios, examples, or Python strings).
