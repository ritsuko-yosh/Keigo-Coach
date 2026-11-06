# Storybook Book, Seaside Theme, Requirements

## Status

Active specification. It supersedes `.kiro/specs/polish-and-interactions/`.
The visual direction is Belle's Seaside Storybook and replaces the cancelled
stationery theme.

## Overview

Keigo Coach is a rich, living picture book (絵本) resting on clear turquoise
water. Belle is preparing for her first job in Tokyo and learning business
keigo. The experience is calm, bright, dreamy, and lightly deadpan. It is
never busy and never uses Duolingo-style mechanics.

The whole book is one Streamlit HTML component. Python loads trusted CSV and
markdown files and passes them into the component. Component-local JavaScript
handles cover opening, page riffle, tab turns, Practice sheet turns, Belle
interactions, and background effects without a Streamlit rerun for each
interaction.

The implementation must follow `.kiro/steering/design.md` for all visual
tokens, fonts, book behavior, motion, Belle rules, background assets, and
content rules.

---

## US-1, Open the seaside storybook

**Acceptance criteria:**

- Initial state is a closed book with Belle on the cover.
- The cover opens automatically after a short pause.
- Several page layers riffle while light ripples spread.
- Clicking the cover skips the wait.
- Reduced motion uses a simple fade and disables riffle and ripple movement.
- If `assets/water.mp4` is absent, a CSS water-gradient shimmer is used.
- If `assets/water.mp4` exists, it is muted, autoplaying, looping, inline,
  and has no controls.
- `assets/water.jpg` is used on small screens and with reduced motion when
  available.

---

## US-2, Navigate by colored index tabs

**Acceptance criteria:**

- Right-edge tabs are Home, Practice, Phrase library, My progress, and About.
- Tab colors use only the five approved soft sea pastels.
- Clicking a tab turns the pages. Farther tabs turn more pages.
- Practice scenario navigation turns one sheet.
- Tabs move to the top on mobile.
- The active tab is visually clear.
- A lavender ribbon bookmark shows chapter position without scores or fake
  progress numbers.

---

## US-3, Render every section as a two-page spread

**Acceptance criteria:**

- Home, Practice, Phrase library, My progress, and About each have a spread.
- The left page contains story, scene, or explanation.
- The right page contains content, reference material, or decisions.
- Pages are clean sand-white paper floating above water.
- Text never sits directly on the water background.
- The book has page-stack depth, soft shadows, subtle paper grain, and spine
  light falloff.
- Decorative left-page scene frames use clearly marked placeholders in
  `assets/scenes/`.
- Reference mood images are not copied or added.

---

## US-4, Home chapter

**Acceptance criteria:**

- The left page loads story text from `content/story.md` and shows Belle.
- The right page explains the experience in three steps and provides a
  Start practicing action.
- The Home spread includes a path to the Practice Before you begin chapter.
- Water, foam, flowers, and occasional butterflies remain behind the book
  and never reduce text readability.

---

## US-5, Practice Before you begin chapter

**Acceptance criteria:**

- Practice starts with a Before you begin chapter.
- It includes an interactive ウチ/ソト diagram loaded from
  `data/uchi_soto.csv`.
- It includes five keigo type cards loaded from `data/keigo_types.csv`.
- Each unverified card shows a small Unverified note.
- Fictional names only appear in examples.

---

## US-6, Practice scenario chapters

**Acceptance criteria:**

- Practice has chapters for all five situations in `data/scenarios.csv`:
  recorded interview, recruiter email, talking about my school, phone call,
  and career fair.
- Each scenario asks in order: who acts, who listens, which keigo type,
  and which sentence is correct.
- Only the next step is interactive after the prior step is answered.
- Correct answer: a paper pop-up rises, a white flower floats in and blooms,
  Belle looks toward it and bows.
- Wrong answer: a soft ripple spreads, Belle tilts her head, and a calm
  handwritten note appears with `あれ…？` and a short hint.
- Finishing a scenario adds one flower to the floating garden, without score,
  points, or ranking.
- Page turns inside Practice use one-sheet turns.
- Practice content comes only from `data/scenarios.csv`.

---

## US-7, Phrase library chapter

**Acceptance criteria:**

- Reference cards show casual, polite, and keigo forms, English meaning,
  explanations, and source information from `data/phrases.csv`.
- The chapter uses the same seaside book, page, tab, and keigo color system.
- Unverified rows show a small Unverified note.
- No duplicate header appears inside the component.

---

## US-8, My progress chapter

**Acceptance criteria:**

- The section says coming soon and contains no fake numbers.
- It does not use streaks, XP, points, rankings, or charts.
- The floating garden is a visual completion record only, not a score.

---

## US-9, About chapter

**Acceptance criteria:**

- About includes project content, sources, and author content.
- Author content is loaded from `content/author.md`.
- It includes the specified author name, reason for building, LinkedIn,
  portfolio, and email links, with no phone number.
- The background video creator and Pexels page are credited in
  `content/about.md` once the video asset is added.
- The author's name appears only in the About author content.

---

## US-10, Interactive Belle

**Acceptance criteria:**

- Belle is rendered inline only from `assets/belle_sit.svg`.
- Existing Belle parts are moved, not redrawn.
- Belle blinks, sleeps with `zzz` after 30 seconds, perks ears on hover,
  and supports tap reactions: bow, tail wag, or ear flop.
- Tap reactions show rising sparkles and a tip from `data/belle_tips.csv`.
- Practice correct and wrong reactions follow the seaside motion rules.
- All Belle animation has reduced-motion fallbacks.

---

## US-11, Content integrity and sources

**Acceptance criteria:**

- Practice reads `data/scenarios.csv`.
- Phrase library reads `data/phrases.csv`.
- The diagram reads `data/uchi_soto.csv`.
- Keigo cards read `data/keigo_types.csv`.
- Belle tips read `data/belle_tips.csv`.
- Home story reads `content/story.md`.
- Author text reads `content/author.md`.
- Unconfirmed rows use `needs review`, empty source URL and page fields,
  and `verified = false`.
- Only approved sources are used, and no sources are invented.
- Every unverified row displays an Unverified note.
- All settings and UI values are in config.py, not hardcoded in Python or
  JavaScript content templates.
