# Homepage and Navigation — Design

## File structure (after this feature)

```
app.py                     Navigation hub only: defines st.navigation, renders
                           top tab bar, calls pg.run(). No page content here.
pages/
  home.py                  Home page (new)
  practice.py              Decision Simulator (content moved from app.py)
  phrase_library.py        Phrase Library (renamed from 1_Phrase_Library.py)
  my_progress.py           My Progress — coming soon (new)
  about.py                 About (renamed from 2_About.py)
kc_utils.py                Add: inject_css(), belle_header_html(),
                           parse_home_md(), render_top_nav()
config.py                  Add: navigation tab names, step hints, progress
                           format, home.md path, coming-soon message,
                           situation card display config
content/
  home.md                  All home-page text, section-marked with ## headings
  about.md                 Unchanged
data/
  scenarios.csv            Fix row 1: replace real name with 田中
```

---

## Navigation architecture

### st.navigation (preferred, available in Streamlit 1.36+)

```python
# app.py
pg = st.navigation([
    st.Page("pages/home.py",           title=config.NAV_HOME),
    st.Page("pages/practice.py",       title=config.NAV_PRACTICE),
    st.Page("pages/phrase_library.py", title=config.NAV_PHRASE_LIBRARY),
    st.Page("pages/my_progress.py",    title=config.NAV_MY_PROGRESS),
    st.Page("pages/about.py",          title=config.NAV_ABOUT),
], position="hidden")

render_top_nav(current_page=pg.title)  # custom tab bar (see below)
pg.run()
```

`position="hidden"` suppresses Streamlit's default sidebar navigation.
`render_top_nav` renders the tab strip.

### Top tab bar (kc_utils.render_top_nav)

Rendered once per page using `st.columns` and `st.page_link`.
`st.page_link` (available since 1.31.0) creates internal navigation links.

```python
def render_top_nav(current_page: str) -> None:
    pages = [
        ("pages/home.py",           config.NAV_HOME),
        ("pages/practice.py",       config.NAV_PRACTICE),
        ("pages/phrase_library.py", config.NAV_PHRASE_LIBRARY),
        ("pages/my_progress.py",    config.NAV_MY_PROGRESS),
        ("pages/about.py",          config.NAV_ABOUT),
    ]
    cols = st.columns(len(pages))
    for col, (path, label) in zip(cols, pages):
        with col:
            st.page_link(path, label=label, use_container_width=True)
```

CSS in style.css styles the `.stPageLink` elements to look like tabs, with
the active page distinguished by a different background or underline.
No new visual theme changes are made.

### Sidebar suppression

```css
/* In assets/style.css */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stSidebarCollapsedControl"] { display: none !important; }
```

---

## content/home.md — structure

The file uses `## section-key` headings as markers. `kc_utils.parse_home_md`
splits the file on these headings and returns a dict `{key: text}`.

```markdown
## tagline
One sentence. Rendered in the hero section.

## start-button
Start practicing

## how-it-works-intro
One sentence introducing the three steps.

## step-1-label
Step 1 label text

## step-1-detail
Step 1 detail text

## step-2-label
...

## step-3-label
...

## step-3-detail
...

## why-keigo-hard
Paragraph using 田中 as the example name for the ウチ/ソト explanation.

## situation-card-recorded-interview
Brief description shown on the situation card.

## situation-card-recruiter-email
...

## situation-card-talking-about-my-school
...

## situation-card-phone-call
...

## situation-card-career-fair
...
```

### parse_home_md (kc_utils.py)

```python
def parse_home_md() -> dict[str, str]:
    raw = Path(config.HOME_MD_PATH).read_text(encoding="utf-8")
    sections = {}
    current_key = None
    buf = []
    for line in raw.splitlines():
        if line.startswith("## "):
            if current_key:
                sections[current_key] = "\n".join(buf).strip()
            current_key = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    if current_key:
        sections[current_key] = "\n".join(buf).strip()
    return sections
```

---

## pages/home.py — layout

```
[Belle header with pose-sit, title, tagline]

[Start practicing button]  →  st.switch_page("pages/practice.py")

[How it works — 3 columns]
  Col 1: step-1-label + step-1-detail
  Col 2: step-2-label + step-2-detail
  Col 3: step-3-label + step-3-detail

[Situation cards — 1 row of 5]
  Each: situation name + card description from home.md
  On click: st.session_state["practice_filter"] = situation_key
            st.switch_page("pages/practice.py")

[Why keigo is hard — full width]
  Text from home.md["why-keigo-hard"]
  Rendered with st.markdown
```

Situation card display labels and internal keys:
```python
# In config.py
SITUATION_CARDS = [
    ("recorded_interview", "Recorded Interview"),
    ("recruiter_email",    "Recruiter Email"),
    ("talking_about_my_school", "Talking About My School"),
    ("phone_call",         "Phone Call"),
    ("career_fair",        "Career Fair"),
]
```

---

## pages/practice.py — changes

### practice_filter (cross-page state)

On load:
```python
filter_key = st.session_state.pop("practice_filter", None)
if filter_key:
    # select the matching scenario index
    match = scenarios[scenarios["situation"] == filter_key]
    if not match.empty:
        st.session_state.sim_idx = match.index[0]
        reset_scenario()
```

`.pop` clears the filter after the first use so navigating away and back
does not re-apply it.

### Progress indicator

Displayed above the scenario card.
Format string in config.py: `PROGRESS_FORMAT = "Scenario {scenario} of {total}, Step {step} of {total_steps}"`

```python
st.markdown(
    f'<div class="kc-progress">'
    + config.PROGRESS_FORMAT.format(
        scenario=idx+1, total=n_total,
        step=sim_step, total_steps=4
    )
    + '</div>',
    unsafe_allow_html=True,
)
```

### Step hints

Added below the step heading, above the option cards.
```python
# In config.py
STEP_HINTS = {
    1: "The keigo choice depends on who performs the main action.",
    2: "ウチ (in-group) or ソト (out-group): this determines whether to honor or humble.",
    3: "尊敬語 honors the other person. 謙譲語 lowers yourself or your group.",
    4: "Match the verb transformation to the keigo type you identified in Step 3.",
}
```

Rendered as:
```python
st.markdown(
    f'<div class="kc-step-hint">{config.STEP_HINTS[n]}</div>',
    unsafe_allow_html=True,
)
```

### Option cards (replacing radio buttons)

Each option is rendered as a full-width `st.button`. Clicking selects and
submits in one action. No separate "Check answer" button.

```python
for i, option in enumerate(options):
    if st.button(option, key=f"s{n}_opt{i}", use_container_width=True):
        st.session_state.sim_answers[n] = option
        st.session_state.sim_step = n + 1
        st.rerun()
```

CSS class `.kc-option-card` applied via `st.markdown` wrapper before the
buttons to set the styling context. The "Submit" button (`SUBMIT_LABEL`) is
removed from the Practice page.

---

## data/scenarios.csv — row 1 fix

The current `scene_en`, `scene_jp`, `correct_sentence`, and `wrong_options`
for scenario id=1 contain "吉田里津子", which violates the content rule
prohibiting real names. Replace with the fictional surname 田中:

| Field               | Before                      | After               |
|---------------------|-----------------------------|---------------------|
| scene_en            | ...My name is Yoshida Ritsuko.  | ...My name is Tanaka. |
| scene_jp            | 吉田里津子と___。             | 田中と___。         |
| correct_sentence    | 吉田里津子と申します          | 田中と申します      |
| wrong_options (1)   | 吉田里津子とおっしゃいます    | 田中とおっしゃいます|
| wrong_options (2)   | 吉田里津子と言います          | 田中と言います      |

---

## config.py additions

```python
HOME_MD_PATH  = "content/home.md"
MY_PROGRESS_MD_PATH = "content/my_progress.md"   # or inline string via config

# Navigation tab labels
NAV_HOME          = "Home"
NAV_PRACTICE      = "Practice"
NAV_PHRASE_LIBRARY = "Phrase Library"
NAV_MY_PROGRESS   = "My Progress"
NAV_ABOUT         = "About"

NAV_PAGES = [                               # ordered list for render_top_nav
    ("pages/home.py",           NAV_HOME),
    ("pages/practice.py",       NAV_PRACTICE),
    ("pages/phrase_library.py", NAV_PHRASE_LIBRARY),
    ("pages/my_progress.py",    NAV_MY_PROGRESS),
    ("pages/about.py",          NAV_ABOUT),
]

# Situation cards on home page
SITUATION_CARDS = [
    ("recorded_interview",      "Recorded Interview"),
    ("recruiter_email",         "Recruiter Email"),
    ("talking_about_my_school", "Talking About My School"),
    ("phone_call",              "Phone Call"),
    ("career_fair",             "Career Fair"),
]

# Practice step hints (displayed below each step heading)
STEP_HINTS = {
    1: "The keigo choice depends on who performs the main action.",
    2: "ウチ (in-group) or ソト (out-group): this determines whether to honor or humble.",
    3: "尊敬語 honors the other person. 謙譲語 lowers yourself or your group.",
    4: "Match the verb transformation to the keigo type you identified in Step 3.",
}

# Progress indicator format
PROGRESS_FORMAT = "Scenario {scenario} of {total}, Step {step} of {total_steps}"

# My Progress page
MY_PROGRESS_COMING_SOON = "Progress tracking is coming soon."

# Home page button
START_BUTTON_LABEL = "Start practicing"
```

---

## kc_utils.py additions

- `parse_home_md() -> dict[str, str]`: splits home.md into sections
- `render_top_nav(nav_pages: list) -> None`: renders tab bar using st.page_link

---

## Theme: Belle's first day at the office

### Colors (defined in config.py AND as CSS variables in assets/style.css)

| Token | Hex | Use |
|---|---|---|
| Background | `#FAF6EE` | Page background (warm paper) |
| Text | `#2F2A26` | Main body text (soft ink) |
| Text muted | `#6E6660` | Secondary text, hints, captions |
| Card | `#FFFFFF` | Card backgrounds |
| Accent | `#E86A5F` | Buttons, highlights (Belle's collar coral) |
| Washi yellow | `#F3D27A` | Situation tags, sticky-note labels |
| 尊敬語 | `#9CC5E3` | Sky blue |
| 謙譲語I | `#A8C3A0` | Sage green |
| 謙譲語II | `#C9B8E8` | Lavender |
| 丁寧語 | `#F6C9A8` | Peach |
| 美化語 | `#F2B8C6` | Pink |

Card border: 1.5px solid `#2F2A26` at 25% opacity. Box shadow: 3px 3px 0 at 10% opacity. Slightly irregular border-radius for hand-drawn feel.

### Fonts (Google Fonts — loaded via @import in style.css)

- Headings and tab labels: **Caveat** (handwritten)
- English body text: **Nunito**
- Japanese text: **Zen Maru Gothic**

### Decorations (CSS only, no extra dependencies)

- Washi tape strip on the top-center of every card (`::before` pseudo-element, 36px wide, 10px tall, `--kc-washi` background)
- Situation tags styled as sticky notes (washi yellow, slight drop shadow)
- Scenario card styled like a notebook page (subtle horizontal rule lines in background via repeating-linear-gradient)
- Title has a hand-drawn underline (`::after` pseudo-element, coral, 3px, slight rotation)
- Paper texture on body: very subtle repeating dot pattern via CSS `background-image`

### Layout

- Content centered, `max-width: 960px`
- Generous padding: `2rem` horizontal, `1.5rem` vertical between sections
- Streamlit top bar hidden via CSS; extra top padding added so the header is never cut off
- Responsive: on screens below 640px, columns stack vertically
