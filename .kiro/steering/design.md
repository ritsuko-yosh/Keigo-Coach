# Theme: Belle's Seaside Storybook

The app is a rich, living picture book (絵本). Belle, my dog, is the main
character preparing for her first job in Tokyo and learning business keigo.
It is warm, calm, cute, a little deadpan, high quality, and never basic.

The visual mood is a calm, bright picture book resting on clear turquoise
water. Sunlight sparkles in the ripples, white flowers drift, and soft foam
meets white sand. Belle, warm cream with her red collar, is the cozy spot in
a cool, sparkling world. The result is dreamy and calm, never busy and never
like Duolingo.

Never use streaks, XP, points, confetti, cheering, or bright green.

## Book structure

- On load, show a closed book with Belle on the cover. It opens by itself
  after a short pause, several pages riffle past, then Home appears.
  Clicking the cover skips the wait.
- Colored index tabs stick out from the right edge of the book: Home,
  Practice, Phrase library, My progress, About.
- Clicking a tab flips pages to that section. Farther tabs turn more pages.
  Turning the page in Practice flips one sheet.
- Each section is a two-page spread: story or scene on the left, content or
  decisions on the right. On mobile, pages stack vertically and tabs move
  to the top.
- A ribbon bookmark shows progress through chapters without inventing scores.

## Sections

- Home: Belle and a short story intro on the left; how it works in three
  steps and a Start practicing button on the right.
- Practice: chapters by situation, including recorded interview, recruiter
  email, talking about my school, phone call, and career fair. It also has
  a Before you begin chapter with the ウチ/ソト diagram and five keigo type
  cards.
- Phrase library: reference cards for casual, polite, and keigo forms with
  sources.
- My progress: coming soon, never fake numbers.
- About: project information, sources, and the author.

## Colors, only these tokens

### Water and paper

- shallow water: `#BFE6EE`
- turquoise: `#5FB8D4`
- deep water: `#2E7FA8`
- sparkle: `#FFE7A8`
- foam and flowers: `#FFFFFF`
- sand and paper: `#F6F1E9`
- ink: `#2F3B45`
- ink-soft: `#5E6B75`

### Cover and accents

- cover turquoise: `#5FB8D4`
- cover text cream: `#FFF8EC`
- Belle collar accent: `#E86A5F`, used sparingly
- ribbon: `#C9B8E8`

### Tabs

- Home: shallow water `#BFE6EE`
- Practice: sand `#F6F1E9`
- Phrase library: lavender `#C9B8E8`
- My progress: mint `#BFE3D4`
- About: pale coral `#F6C9C0`

### Keigo types

- 尊敬語: `#9CC5E3`
- 謙譲語I: `#A8C3A0`
- 謙譲語II: `#C9B8E8`
- 丁寧語: `#F6C9A8`
- 美化語: `#F2B8C6`

These are the only visual theme tokens. Do not introduce the cancelled
stationery palette or bright green.

## Fonts

- Titles: Fraunces
- English body: Nunito
- Japanese: Zen Maru Gothic
- Handwritten notes and Belle's comments: Caveat

## Background and readability

- When available, use `assets/water.mp4` as a full-page looping background:
  muted, autoplay, inline, no controls, softly brightened and softened.
- Use `assets/water.jpg` on small screens and whenever the user prefers
  reduced motion.
- Until those files exist, use a soft animated CSS water gradient with a
  gentle light shimmer fallback.
- Add a soft foam wave along the bottom edge that slowly washes in and out.
- Add a few low-opacity white flowers drifting slowly and an occasional
  small white butterfly. They must never sit over readable text.
- Book pages are clean sand-white paper with soft shadows, floating above
  the water. Text never sits directly on the water.
- Use visible page-stack depth, warm shadows, subtle paper grain made with
  CSS or SVG noise, and light falloff toward the spine.
- Do not add the mood-reference images to the project or copy them.

## Motion tokens

- quick: `150ms`
- normal: `350ms`
- slow: `700ms`
- page flip: `500ms` to `600ms`
- entering: ease-out
- leaving: ease-in
- Belle: soft spring

Respect `prefers-reduced-motion`. Replace motion with simple fades, disable
parallax and decorative drift, and use `water.jpg` instead of video.

## Signature animations

- Cover opens on load, pages riffle, and light ripples spread as it opens.
- Page turns use a realistic page curl and the configured page-flip timing.
- Clouds, leaves, and small birds in the margins use subtle parallax and move
  slower than page content.
- A correct answer makes a white flower float in and bloom near the page;
  Belle looks at it.
- A wrong answer creates a soft ripple, Belle tilts her head, and a calm
  handwritten note appears with `あれ…？` and a short hint.
- Finishing a scenario adds a flower to the water, building a small floating
  garden. This is not a score or points system.
- Tapping Belle triggers her reaction and a few rising sparkles.
- Belle occasionally walks in from a page edge and sits.

## Belle

- Design Belle only from `assets/belle_sit.svg`. Never redraw her. Only move
  her existing parts with CSS or component transforms.
- Belle is polite, a little nervous, and deadpan.
- She blinks while idle, sleeps with `zzz` after 30 seconds, perks her ears
  on hover, and can be tapped for a random bow, tail wag, or ear flop.
- Tap tips come from `data/belle_tips.csv`, never from invented Python text.
- In Practice, Belle bows on a correct answer and tilts her head on a wrong
  answer.

## Illustrations

- Decorative scene frames on left pages use simple placeholders in
  `assets/scenes/`. They must be clearly marked so they can be replaced by
  the owner's drawings.
- No images from the web are used for illustrations.
- The water video and still image are background assets only. Once the video
  is added, credit its creator and Pexels page in `content/about.md`.

## Architecture

- The whole book runs as one Streamlit HTML component with JavaScript so
  page flips, tabs, background effects, and Belle interactions animate
  smoothly without Streamlit reruns.
- Python loads CSV and markdown content and passes it into the component as
  data. The component does not invent or fetch content.
- All settings, paths, labels, colors, fonts, and motion values are defined
  in `config.py` and passed into the component.
- Content remains in CSV and markdown files.
- No secrets or local machine paths are included in application code.
- The component must work on Streamlit Community Cloud.

## Content rules

- Practice uses `data/scenarios.csv`.
- Phrase library uses `data/phrases.csv`.
- The ウチ/ソト diagram uses `data/uchi_soto.csv`.
- Keigo type cards use `data/keigo_types.csv`.
- Belle tips use `data/belle_tips.csv`.
- Home story text uses `content/story.md`.
- Author content uses `content/author.md`.
- Every unconfirmed row uses `source = "needs review"`, empty
  `source_url` and `source_page`, and `verified = false`.
- Only the approved government guidance and academic papers that summarize
  it may be cited. Never invent sources.
- Fictional names only in scenarios and examples. The author's name appears
  only in the About author content.
- Unverified rows show a small Unverified note.
