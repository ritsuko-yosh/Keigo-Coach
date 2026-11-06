# Storybook Book, Seaside Theme, Tasks

## Status

Active task list. Supersedes `.kiro/specs/polish-and-interactions/tasks.md`.
No application implementation has started from this list.

## Status key

- [ ] not started
- [x] complete

---

## Task 1, Confirm supersession and design inputs

- [ ] Keep the prior polish-and-interactions spec for history and mark it
      superseded by storybook-book.
- [ ] Use `.kiro/steering/design.md` as the source of truth for the Seaside
      Storybook palette, fonts, architecture, and motion.
- [ ] Do not add or copy the mood-reference images.

## Task 2, Add config tokens and paths

**Files:** `config.py`

- [ ] Add component path, story path, water video path, water still path,
      and scene directory path.
- [ ] Add only the approved water, paper, ink, cover, ribbon, tab, collar,
      and keigo color tokens.
- [ ] Add Fraunces, Nunito, Zen Maru Gothic, and Caveat font tokens.
- [ ] Add motion tokens: 150ms, 350ms, 700ms, and 550ms page flip, plus
      easing values and reduced-motion settings.
- [ ] Add section labels, tab labels, chapter labels, Unverified text,
      Source needed text, and all other component UI copy.
- [ ] Add Belle state names, tap actions, sleep duration, and tip contexts.
- [ ] Keep the author's name out of config.py.

## Task 3, Validate and load all content

**Files:** `validate.py`, `kc_utils.py`

- [ ] Validate all existing CSVs and source fields.
- [ ] Load `data/scenarios.csv`, `data/phrases.csv`, `data/uchi_soto.csv`,
      `data/keigo_types.csv`, and `data/belle_tips.csv`.
- [ ] Load `content/story.md`, `content/about.md`, and `content/author.md`.
- [ ] Preserve source, source URL, source page, and verified fields.
- [ ] Ensure all unconfirmed rows use `needs review`, empty source URL and
      page, and `verified = false`.
- [ ] Ensure fictional names only appear in scenarios and examples.
- [ ] Report missing fields, invalid values, missing source metadata, and
      unverified rows.

## Task 4, Prepare background and scene assets

**Files:** `assets/water.mp4`, `assets/water.jpg`, `assets/scenes/`

- [ ] Support optional water.mp4 and water.jpg without requiring them for
      the first run.
- [ ] Add no mood-reference images.
- [ ] Add clearly marked scene placeholders under assets/scenes/.
- [ ] Do not use web images for scene illustrations.
- [ ] Once water.mp4 is added, add its creator and Pexels page credit to
      content/about.md.

## Task 5, Create the single component shell

**Files:** `storybook_component.html`, `app.py`

- [ ] Build one self-contained Streamlit HTML component surface.
- [ ] Pass all content and settings through a serialized data payload.
- [ ] Render the closed cover, page stack, spine, tabs, ribbon, and spreads.
- [ ] Use local JavaScript for cover, riffle, tabs, page flips, Practice
      turns, Belle interactions, water fallback, and floating garden state.
- [ ] Do not use an external animation library or backend.

## Task 6, Implement the Seaside background

**Files:** `storybook_component.html`, `assets/style.css`

- [ ] Use muted autoplay looping inline water.mp4 when available.
- [ ] Use water.jpg on small screens and with reduced motion when available.
- [ ] Use a CSS gradient and gentle sparkle shimmer when assets are absent.
- [ ] Add a bottom foam wave, drifting white flowers, and rare low-opacity
      white butterfly in safe margins.
- [ ] Keep all background decoration behind readable book pages.
- [ ] Add reduced-motion fallback and no dark mode.

## Task 7, Implement book opening and depth

**Files:** `storybook_component.html`, `assets/style.css`

- [ ] Show a closed cover initially.
- [ ] Auto-open after a short pause and allow click-to-skip.
- [ ] Riffle several page layers and spread light ripples during opening.
- [ ] Add realistic page curl for tab turns and one-sheet Practice turns.
- [ ] Add page stack edges, paper grain, soft shadows, spine light falloff,
      and responsive mobile stacking.
- [ ] Use only approved color and font tokens.

## Task 8, Implement tabs and spreads

**Files:** `storybook_component.html`, `assets/style.css`

- [ ] Render colored right-edge tabs for Home, Practice, Phrase library,
      My progress, and About.
- [ ] Move tabs to the top on mobile.
- [ ] Make farther tabs turn more pages.
- [ ] Add the ribbon bookmark without scores or fake progress.
- [ ] Render all five sections as two-page spreads.

## Task 9, Implement Home and Before you begin

**Files:** `storybook_component.html`, `content/story.md`

- [ ] Render story.md and Belle on the left Home page.
- [ ] Render three-step explanation and Start practicing on the right.
- [ ] Add the Practice Before you begin entry point.
- [ ] Render the ウチ/ソト diagram from data/uchi_soto.csv.
- [ ] Render five keigo type cards from data/keigo_types.csv.
- [ ] Show Unverified or Source needed indicators from row metadata.

## Task 10, Implement Practice chapters

**Files:** `storybook_component.html`

- [ ] Render five scenario chapters from data/scenarios.csv.
- [ ] Implement ordered actor, listener, keigo type, and sentence decisions.
- [ ] Reveal only the next step after an answer.
- [ ] Correct answer: flower bloom, Belle bow, and paper pop-up.
- [ ] Wrong answer: ripple, Belle tilt, and handwritten note with a hint.
- [ ] Finished scenario adds a flower to the floating garden without score.
- [ ] Show each row's verification and source state.

## Task 11, Implement Phrase library

**Files:** `storybook_component.html`

- [ ] Render phrase cards from data/phrases.csv.
- [ ] Show casual, polite, keigo, English explanations, and sources.
- [ ] Keep the chapter inside the same two-page book spread.
- [ ] Ensure no duplicate header is rendered.

## Task 12, Implement My progress and About

**Files:** `storybook_component.html`, `content/about.md`, `content/author.md`

- [ ] My progress shows only coming soon and story context.
- [ ] Do not show fake numbers, scores, charts, streaks, or points.
- [ ] About shows project content, allowed source information, and author
      content from author.md.
- [ ] Include no phone number.
- [ ] Add background video credit to about.md only after water.mp4 is added.
- [ ] Keep the author's name out of all other content and code.

## Task 13, Implement Belle interaction

**Files:** `storybook_component.html`, `assets/belle_poses.css`,
`assets/belle_interactions.css`

- [ ] Inline assets/belle_sit.svg without redrawing or changing it.
- [ ] Add blink, 30-second sleep with zzz, ear hover, tap reaction,
      tail wag, ear flop, tip bubble, walk-in, and sit.
- [ ] Load tips only from data/belle_tips.csv.
- [ ] Add sparkle particles on tap.
- [ ] Add reduced-motion fallbacks for every Belle animation.

## Task 14, Add source indicators and integrity checks

**Files:** `storybook_component.html`, `validate.py`

- [ ] Show a small Unverified note for every false verified field.
- [ ] Show Source needed when source URL is empty.
- [ ] Link only to non-empty approved source URLs.
- [ ] Run the validator across all data files.
- [ ] Confirm no errors before launch.

## Task 15, Verify the Storybook

- [ ] Run `python validate.py`.
- [ ] Start the app locally.
- [ ] Verify cover auto-open and click-to-skip.
- [ ] Verify page riffle, ripples, page curls, tab distance, and Practice turns.
- [ ] Verify all sections render as two-page spreads.
- [ ] Verify water video, still-image, and CSS fallback paths.
- [ ] Verify mobile tabs and stacked pages.
- [ ] Verify flowers, foam, butterfly, parallax, and reduced-motion behavior.
- [ ] Verify Practice reactions and floating garden without scores.
- [ ] Verify Belle tips use CSV sources.
- [ ] Verify no mood-reference image was added.
- [ ] Verify the author's name appears only in About author content.
