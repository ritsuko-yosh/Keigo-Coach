# Storybook Book, Seaside Theme, Design

## Status

Active design. Supersedes `.kiro/specs/polish-and-interactions/`.

## Architecture

The whole book is one Streamlit HTML component. `app.py` loads CSV and
markdown content with Python, serializes a payload, and renders one
`components.html` or `st.components.v1.html` surface. Component-local
JavaScript owns cover opening, page riffle, index tab state, page flips,
Practice sheet turns, Belle tap interaction, flower garden state, and
background effects. This avoids a Streamlit rerun for each tab or page flip.

Python remains responsible for loading files, validating source fields, and
passing data. The component never fetches content and never uses reference
images from the web. No new animation library is required.

### Component files

```text
app.py
storybook_component.html
config.py
kc_utils.py
assets/style.css
assets/belle_poses.css
assets/belle_interactions.css
assets/belle_sit.svg
assets/water.mp4              optional runtime background video
assets/water.jpg              optional still fallback
assets/scenes/                marked replaceable scene placeholders
data/scenarios.csv
data/phrases.csv
data/uchi_soto.csv
data/keigo_types.csv
data/belle_tips.csv
content/story.md
content/about.md
content/author.md
```

The component must work when water.mp4 and water.jpg are not yet present.
It must use the CSS water fallback in that case.

---

## Storybook structure

```text
book
├── closed cover
├── Home spread
├── Practice Before you begin spread
├── Practice scenario spreads
├── Phrase library spread
├── My progress spread
└── About spread
```

Every section is a two-page spread:

```html
<section class="book-spread" data-section="home">
  <div class="book-page book-page-left">story or scene</div>
  <div class="book-spine" aria-hidden="true"></div>
  <div class="book-page book-page-right">content or decisions</div>
</section>
```

On mobile, pages stack vertically and index tabs move from the right edge to
the top. Page content stays on paper surfaces above the water.

---

## Seaside visual tokens

Define these tokens once in config.py and as CSS custom properties. Do not
introduce colors outside this set for theme styling.

```css
--shallow-water: #BFE6EE;
--turquoise:     #5FB8D4;
--deep-water:    #2E7FA8;
--sparkle:       #FFE7A8;
--foam:          #FFFFFF;
--sand-paper:    #F6F1E9;
--ink:           #2F3B45;
--ink-soft:      #5E6B75;
--cover-coral:   #E86A5F;
--cover-cream:   #FFF8EC;
--ribbon:        #C9B8E8;
--tab-home:      #BFE6EE;
--tab-practice:  #F6F1E9;
--tab-library:   #C9B8E8;
--tab-progress:  #BFE3D4;
--tab-about:     #F6C9C0;
--sonkeigo:      #9CC5E3;
--kenjogo1:      #A8C3A0;
--kenjogo2:      #C9B8E8;
--teineigo:      #F6C9A8;
--bikago:        #F2B8C6;
```

Belle's collar accent is `#E86A5F` and is used sparingly. White is reserved
for foam, flowers, and readable paper surfaces. Do not use bright green,
dark mode, or the cancelled stationery palette.

---

## Fonts

Load with CSS and provide system fallbacks:

- Fraunces for titles
- Nunito for English body text
- Zen Maru Gothic for Japanese text
- Caveat for handwritten notes and Belle comments

---

## Water background

The background layer is behind the book and behind all decorative effects:

```html
<video class="water-video" autoplay muted loop playsinline></video>
<div class="water-still" aria-hidden="true"></div>
<div class="water-css-fallback" aria-hidden="true"></div>
```

- Use `assets/water.mp4` when present. It is muted, autoplay, loop, inline,
  and has no controls.
- Use `assets/water.jpg` on small screens and under reduced motion when present.
- If either file is absent, show a CSS gradient using only shallow water,
  turquoise, deep water, and sparkle. Add a gentle shimmer, not a busy effect.
- Add a bottom foam wave in white that washes in and out slowly.
- Add a few white flowers and an occasional small white butterfly with low
  opacity. Place them in safe margins, never over text or controls.
- Add subtle light falloff around the book spine.
- Do not add the provided mood-reference images.

When water.mp4 is added, credit its creator and its Pexels page in
`content/about.md`. The component should not invent a credit before that.

---

## Book depth and spreads

The book has a sand-paper surface, visible stacked page edges, soft shadows,
and a central spine shadow. Use CSS or inline SVG noise only for paper grain.
No image texture files.

The cover uses turquoise with cream title text. Pages use sand paper. The
cover and pages float above the water with a soft warm shadow. Content is
centered inside the book and has sufficient contrast against paper.

Tabs are index tabs on the right edge. Their colors are:

```text
Home:            #BFE6EE
Practice:        #F6F1E9
Phrase library:  #C9B8E8
My progress:     #BFE3D4
About:           #F6C9C0
```

The ribbon bookmark is `#C9B8E8`. It shows chapter position only, never
points or scores.

---

## Motion

Define these tokens in config.py and CSS:

```text
quick: 150ms
normal: 350ms
slow: 700ms
page flip: 550ms
enter: ease-out
leave: ease-in
Belle: soft spring
```

Required animations:

- Cover opening after a short pause, with click-to-skip
- Several page layers riffling during the opening
- Light ripples spreading as the book opens
- Realistic page curl on tab turns
- One-sheet page turn inside Practice
- Slower parallax for clouds, leaves, and small birds in the margins
- Correct answer: white flower floats and blooms; Belle looks at it and bows
- Wrong answer: soft ripple, Belle tilt, handwritten note with `あれ…？`
- Finished scenario: one new flower joins the floating garden
- Belle tap: reaction plus a few rising sparkle particles
- Occasional Belle walk-in and sit

`prefers-reduced-motion: reduce` disables transforms, parallax, drifting,
video motion, and spring effects. Use simple fades and the still image when
available.

---

## Belle

Use only `assets/belle_sit.svg`. Do not redraw, recolor, or alter its shapes.
CSS and component transforms may move its existing SVG IDs.

Required states:

```text
pose-sit
pose-bow-small
pose-bow-deep
pose-tilt
pose-tail-wag
pose-ear-flop
```

Belle blinks while idle, sleeps with a `zzz` text layer after 30 seconds,
perks ears on hover, and supports a tap that chooses bow, tail wag, or ear
flop. Tap tips are selected from `data/belle_tips.csv` with
`context = general`. Practice reactions use scenario correctness.

---

## Data payload

Python passes these fields into the single component:

```text
story
scenarios
phrases
uchi_soto
keigo_types
belle_tips
author
source_metadata
settings
```

Records retain source, source URL, source page, and verified values. The
component shows a small Unverified note for false values and Source needed
when no source URL is available.

Content locations are fixed:

- Practice: `data/scenarios.csv`
- Phrase library: `data/phrases.csv`
- ウチ/ソト: `data/uchi_soto.csv`
- Keigo type cards: `data/keigo_types.csv`
- Belle tips: `data/belle_tips.csv`
- Home story: `content/story.md`
- About author: `content/author.md`

The author's name appears only in author content. Fictional names only are
allowed in scenarios and examples.

---

## Content and source rules

Unconfirmed rows must use `source = "needs review"`, empty source URL and
page fields, and `verified = false`. Never invent sources. Only the approved
government guidance and academic papers that summarize it may be cited.

All settings, paths, labels, colors, and motion values belong in config.py.
All content belongs in CSV or markdown. No content or UI copy is hardcoded
inside Python or JavaScript templates.

---

## Component state and future logging

The component keeps active section, cover state, selected tab, Practice step,
Belle pose, tip, ripple, and floating garden state locally. It may emit the
future answer event below, but this feature does not persist logging:

```json
{
  "event": "answer",
  "scenario_id": "string",
  "step": 1,
  "correct": true,
  "timestamp": "ISO-8601"
}
```
