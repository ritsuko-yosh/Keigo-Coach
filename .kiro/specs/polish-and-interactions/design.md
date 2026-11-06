# Status: Superseded by `.kiro/specs/storybook-book/`

# Polish and Interactions — Design

## New files

```
assets/
  belle_interactions.css    Belle-specific idle, blink, sleep, hover,
                            tap, and reaction animations. Loaded via
                            inject_css() alongside style.css and
                            belle_poses.css.
data/
  belle_tips.csv            Tips shown in Belle's tap bubble
  uchi_soto.csv             ウチ/ソト diagram relationship data
  keigo_types.csv           Keigo type definitions and examples
content/
  author.md                 Author bio and contact links
```

---

## CSS animations (all in assets/style.css or belle_interactions.css)

### Title pencil underline

The `.kc-title::after` pseudo-element already exists. Animate `width`
from `0` to `65%` on page load:

```css
@keyframes kcPencilDraw {
  from { width: 0; }
  to   { width: 65%; }
}

@media (prefers-reduced-motion: no-preference) {
  .kc-title::after, .kc-hero-title::after {
    animation: kcPencilDraw 0.6s ease-out 0.1s both;
    width: 0;  /* start collapsed */
  }
}
```

### Washi tape stick-on

Currently cards show the tape instantly via `::before`. Animate it:

```css
@keyframes kcWashiIn {
  from { transform: translateX(-50%) translateY(-14px); opacity: 0; }
  to   { transform: translateX(-50%) translateY(0);    opacity: 0.85; }
}

@media (prefers-reduced-motion: no-preference) {
  .kc-card::before, .kc-scenario-card::before,
  .kc-why-section::before, .kc-step-card::before,
  .kc-explanation::before {
    animation: kcWashiIn 0.35s ease-out both;
  }
  /* Stagger by card index via inline animation-delay on parent */
}
```

### Card hover lift

Already in style.css. Confirm it applies universally:
```css
.kc-card:hover, .kc-scenario-card:hover { box-shadow: 5px 5px 0 rgba(47,42,38,0.18); }
```

### Notebook page step reveal (Practice)

Replace the plain `kcSlideIn` for step content with a page-turn feel:

```css
@keyframes kcPageReveal {
  from { opacity: 0; transform: translateY(-10px) rotateX(-6deg); }
  to   { opacity: 1; transform: translateY(0)     rotateX(0); }
}

.kc-step-heading, .kc-step-hint, .kc-option-buttons {
  animation: kcPageReveal 0.32s ease-out both;
}
```

### Hanko stamp (correct step 4)

A `<div class="kc-hanko">正解</div>` is rendered when `sim_step == 5`
and the final answer was correct. CSS stamps it down:

```css
.kc-hanko {
  display: inline-block;
  font-family: var(--kc-font-jp);
  font-size: 2.2rem;
  font-weight: 700;
  color: #C0392B;
  border: 3px solid #C0392B;
  border-radius: 4px;
  padding: 6px 14px;
  transform: rotate(-15deg);
  margin: 8px 0;
  opacity: 0;
}

@keyframes kcHanko {
  0%   { opacity: 0; transform: rotate(-15deg) scale(2.2); }
  55%  { opacity: 1; transform: rotate(-15deg) scale(0.92); }
  75%  { transform: rotate(-15deg) scale(1.05); }
  100% { opacity: 1; transform: rotate(-15deg) scale(1); }
}

@media (prefers-reduced-motion: no-preference) {
  .kc-hanko { animation: kcHanko 0.55s cubic-bezier(0.22, 1, 0.36, 1) forwards; }
}
@media (prefers-reduced-motion: reduce) {
  .kc-hanko { opacity: 1; }
}
```

`kc-hanko` is rendered in `pages/practice.py` inside `render_explanation`
when the final answer was correct. Whether the final answer was correct
is tracked via `step_is_correct(4, answers[4], scenario)`.

### Gentle shake (wrong answer)

Applied to `.kc-feedback-wrong` and to `.kc-belle-wrapper` when wrong:

```css
@keyframes kcShake {
  0%, 100% { transform: translateX(0); }
  20% { transform: translateX(-5px); }
  40% { transform: translateX(5px); }
  60% { transform: translateX(-3px); }
  80% { transform: translateX(3px); }
}

@media (prefers-reduced-motion: no-preference) {
  .kc-feedback-wrong { animation: kcSlideIn 0.28s ease, kcShake 0.45s ease 0.28s; }
  .kc-belle-wrapper.pose-tilt { animation: kcShake 0.45s ease; }
}
```

### Tab fade-in

Applied to the main page container on every load:

```css
@keyframes kcPageFade {
  from { opacity: 0; transform: translateX(8px); }
  to   { opacity: 1; transform: translateX(0); }
}

@media (prefers-reduced-motion: no-preference) {
  [data-testid="stMainBlockContainer"] { animation: kcPageFade 0.3s ease both; }
}
```

---

## Belle interactions (assets/belle_interactions.css)

Loaded alongside the other CSS files in `inject_css()`. Never modifies
`belle_sit.svg`.

### Blink

```css
@keyframes belleBlink {
  0%, 92%, 100% { opacity: 1; }
  95%           { opacity: 0; }
}
@keyframes belleBlinkClose {
  0%, 92%, 100% { opacity: 0; }
  95%           { opacity: 1; }
}
@media (prefers-reduced-motion: no-preference) {
  .kc-belle-wrapper #eyes-open  { animation: belleBlink      4.5s ease-in-out infinite; }
  .kc-belle-wrapper #eyes-closed { animation: belleBlinkClose 4.5s ease-in-out infinite; }
}
```

### Sleep after 30 seconds (CSS timer reset on every Streamlit rerender)

```css
@keyframes belleSleepIn {
  from { opacity: 1; }
  to   { opacity: 0.5; }
}
@media (prefers-reduced-motion: no-preference) {
  .kc-belle-wrapper #eyes-open {
    animation: belleBlink 4.5s ease-in-out infinite,
               belleSleepIn 1s ease 30s forwards;
  }
}
```

Because Streamlit rerenders on every interaction, the 30s delay resets
automatically each time the user does anything.

### Ears perk on hover

```css
@keyframes belleEarPerk {
  0%, 100% { transform: rotate(0deg) translateY(0); }
  50%       { transform: rotate(-8deg) translateY(-4px); }
}
@media (prefers-reduced-motion: no-preference) {
  .kc-belle-wrapper:hover #ear-left  { animation: belleEarPerk 0.4s ease forwards; }
  .kc-belle-wrapper:hover #ear-right { animation: belleEarPerk 0.4s ease forwards reverse; }
}
```

### Tail wag

```css
@keyframes belleTailWag {
  0%, 100% { transform: rotate(0deg); }
  30% { transform: rotate(-12deg); }
  70% { transform: rotate(12deg); }
}
```

Applied via pose class `.pose-tail-wag` (added to `belle_poses.css`).

### Tip bubble

A `<div class="kc-tip-bubble">` rendered conditionally when
`st.session_state["belle_tip"]` is set. Animates in with a slight
pop:

```css
@keyframes kcTipPop {
  from { opacity: 0; transform: scale(0.85) translateY(4px); }
  to   { opacity: 1; transform: scale(1) translateY(0); }
}
.kc-tip-bubble {
  position: relative;
  background: var(--kc-card);
  border: 1.5px solid var(--kc-border);
  border-radius: 8px 8px 8px 2px;
  padding: 8px 14px;
  font-size: 0.85rem;
  color: var(--kc-text);
  max-width: 200px;
  animation: kcTipPop 0.28s ease both;
}
```

### Tap button for tip

A small `st.button("✦", key="belle_tap")` rendered next to Belle.
On click, picks a random tip from the loaded `belle_tips.csv` based on
`context == "general"`, stores it in `st.session_state["belle_tip"]`.
Tip clears on next step submission.

Tip selection:
```python
import random
general_tips = tips_df[tips_df["context"] == "general"]
tip = general_tips.sample(1).iloc[0]
st.session_state["belle_tip"] = tip["tip_en"]
```

---

## data/belle_tips.csv

Columns: `id, tip_en, tip_jp, context, source, source_url, source_page, verified`

`context` values: `general` (shown on tap), `correct` (shown on correct step 4), `wrong` (shown on wrong answer).

Sample rows — all `source = "needs review"`, `verified = false`:
- "In business Japanese, ウチ/ソト determines your keigo choice more than hierarchy alone." (general)
- "申す is for your own speech. おっしゃる is for someone else's." (general)
- "参る is the 謙譲語II form of both 行く and 来る." (general)
- "正解! That form lowers your own action, which is exactly right here." (correct)
- "Close. Check who is performing the action and try again." (wrong)

---

## data/uchi_soto.csv

Columns: `id, speaker, listener, speaker_label_en, listener_label_en, uchi_soto_label, expected_keigo, arrow_direction, explanation_en, source, source_url, source_page, verified`

`speaker` values: `me`, `my_boss`, `client`
`listener` values: `insider`, `outsider`
`arrow_direction`: `up` (尊敬語, raise listener), `down` (謙譲語, lower speaker)

All rows `source = "needs review"`, `verified = false`.

Key rows:
- speaker=me, listener=outsider: 謙譲語II, lower yourself to the client
- speaker=my_boss, listener=outsider: 謙譲語II, boss is ウチ to the outsider
- speaker=client, listener=me (insider): 尊敬語, honor the client's actions

---

## data/keigo_types.csv

Columns: `id, type_name, definition_en, example_jp, example_en, badge_css_class, source, source_url, source_page, verified`

`badge_css_class` maps directly to `config.KEIGO_TYPE_CSS` values.
All rows `source = "needs review"`, `verified = false` until confirmed.

---

## ウチ/ソト diagram (pages/home.py)

Uses two `st.selectbox` calls for speaker and listener. On selection,
look up the matching row in `uchi_soto_df`. Render an HTML diagram:

```
[Speaker box]  ──arrow──  [Listener box]
    label          keigo type label
    explanation_en
```

Arrow direction and color come from `arrow_direction` column.
If `arrow_direction == "up"`: arrow points from speaker to listener,
color = `--kc-sonkeigo` (blue). If `"down"`: arrow points down from
listener onto speaker, color = `--kc-kenjogo2` (lavender).

All labels come from the CSV. Diagram rendered via `st.markdown` with
`unsafe_allow_html=True`.

---

## content/author.md

```markdown
## name
Ritsuko Yoshida

## why-built
I built Keigo Coach while preparing for job interviews in Japan as
a bilingual job seeker. Business keigo, especially the ウチ/ソト
distinction, was the one gap that grammar classes did not cover.

## links
- [LinkedIn](https://www.linkedin.com/in/ritsuko-yoshida77)
- [Portfolio](https://ritsuko-yosh.github.io/)
- [Email](mailto:ritsukoyoshida77@gmail.com)
```

Parsed by the same `parse_home_md` pattern (split on `## heading`).
Rendered at the bottom of `pages/about.py`.

---

## Phrase Library duplicate header fix

Currently `pages/phrase_library.py` calls `belle_header_html()` inside
`main()` and renders it via `st.markdown`. The duplication happens
because `app.py` also calls `inject_css()` and renders the top nav,
but the Belle header is rendered again inside the page. The fix: each
page file renders its own Belle header once. Confirm there is no second
call in `phrase_library.py` or that `app.py` does not render a header.

Looking at the current code, the header is only in `phrase_library.py`
so the duplication likely comes from a leftover sidebar. Investigate
and remove the duplicate.

---

## config.py additions

```python
# New file paths
BELLE_TIPS_CSV_PATH    = "data/belle_tips.csv"
UCHI_SOTO_CSV_PATH     = "data/uchi_soto.csv"
KEIGO_TYPES_CSV_PATH   = "data/keigo_types.csv"
BELLE_INTERACTIONS_CSS = "assets/belle_interactions.css"
AUTHOR_MD_PATH         = "content/author.md"

# Belle tap button label
BELLE_TAP_LABEL = "✦"

# Hanko stamp text
HANKO_CORRECT_TEXT  = "正解"
HANKO_CORRECT_CLASS = "kc-hanko"

# Situation card icons (one per situation, keyed by situation ID)
SITUATION_ICONS = {
    "recorded_interview":      "🎥",
    "recruiter_email":         "📧",
    "talking_about_my_school": "🏫",
    "phone_call":              "📞",
    "career_fair":             "🤝",
}

# ウチ/ソト diagram speaker and listener display labels
UCHI_SOTO_SPEAKER_OPTIONS = {
    "me":       "I am speaking",
    "my_boss":  "My boss or colleague (ウチ) is speaking",
    "client":   "The client (ソト) is speaking",
}
UCHI_SOTO_LISTENER_OPTIONS = {
    "insider":  "Someone inside my group (ウチ)",
    "outsider": "Someone outside my group (ソト)",
}

# ウチ/ソト diagram section heading
HOME_SECTION_UCHI_SOTO   = "The ウチ/ソト rule"
HOME_SECTION_KEIGO_TYPES = "Five keigo types"

# About page author section heading
ABOUT_AUTHOR_HEADING = "About the author"
```

---

## New pose classes for belle_poses.css

```css
.pose-tail-wag #tail {
  animation: belleTailWag 0.6s ease-in-out 3;
}

.pose-ear-flop #ear-left,
.pose-ear-flop #ear-right {
  transform-box: fill-box;
  transform-origin: 50% 0%;
  animation: belleEarFlop 0.5s ease-in-out;
}
@keyframes belleEarFlop {
  0%, 100% { transform: rotate(0deg); }
  50%      { transform: rotate(15deg); }
}
```

Add `pose-tail-wag` and `pose-ear-flop` to `BELLE_POSES` in config.py.
