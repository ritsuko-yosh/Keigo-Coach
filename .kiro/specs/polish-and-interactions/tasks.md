# Status: Superseded by `.kiro/specs/storybook-book/`

# Polish and Interactions — Tasks

## Status key
- [ ] not started
- [x] done

---

## Task 1 — Create data/belle_tips.csv

**Files:** `data/belle_tips.csv`

- [ ] Header: `id, tip_en, tip_jp, context, source, source_url, source_page, verified`
- [ ] Add at least 5 rows: 3 `context=general`, 1 `context=correct`, 1 `context=wrong`
- [ ] All rows: `source = "needs review"`, `source_url = ""`, `source_page = ""`, `verified = false`
- [ ] No em dashes. No real names.
- [ ] Run `python validate.py` — 0 errors.

---

## Task 2 — Create data/uchi_soto.csv

**Files:** `data/uchi_soto.csv`

- [ ] Header: `id, speaker, listener, speaker_label_en, listener_label_en, uchi_soto_label, expected_keigo, arrow_direction, explanation_en, source, source_url, source_page, verified`
- [ ] Add rows covering: me+outsider (謙譲語II), my_boss+outsider (謙譲語II, ウチ/ソト), client+insider (尊敬語)
- [ ] `arrow_direction` values: `up` (raise listener) or `down` (lower speaker)
- [ ] All rows: `source = "needs review"`, `verified = false`
- [ ] Fictional names only (田中 if any example name is needed)

---

## Task 3 — Create data/keigo_types.csv

**Files:** `data/keigo_types.csv`

- [ ] Header: `id, type_name, definition_en, example_jp, example_en, badge_css_class, source, source_url, source_page, verified`
- [ ] One row per keigo type: 尊敬語, 謙譲語I, 謙譲語II, 丁寧語, 美化語
- [ ] `badge_css_class` values match `config.KEIGO_TYPE_CSS` exactly
- [ ] All rows: `source = "needs review"`, `verified = false`
- [ ] No em dashes in any definition or example

---

## Task 4 — Create content/author.md

**Files:** `content/author.md`

- [ ] Add sections: `name`, `why-built`, `links`
- [ ] Include name, reason for building, LinkedIn, portfolio, and email links
- [ ] No phone number
- [ ] No em dashes
- [ ] This is the only file where the author's real name appears

---

## Task 5 — Update config.py

**Files:** `config.py`

- [ ] Add file path constants: `BELLE_TIPS_CSV_PATH`, `UCHI_SOTO_CSV_PATH`,
      `KEIGO_TYPES_CSV_PATH`, `BELLE_INTERACTIONS_CSS`, `AUTHOR_MD_PATH`
- [ ] Add `BELLE_TAP_LABEL`, `HANKO_CORRECT_TEXT`, `HANKO_CORRECT_CLASS`
- [ ] Add `SITUATION_ICONS` dict (one emoji per situation key)
- [ ] Add `UCHI_SOTO_SPEAKER_OPTIONS`, `UCHI_SOTO_LISTENER_OPTIONS` dicts
- [ ] Add section headings: `HOME_SECTION_UCHI_SOTO`, `HOME_SECTION_KEIGO_TYPES`,
      `ABOUT_AUTHOR_HEADING`
- [ ] Add new pose keys to `BELLE_POSES`: `"tail_wag"`, `"ear_flop"`

---

## Task 6 — Update validate.py to check the three new CSVs

**Files:** `validate.py`

- [ ] Add column definitions for `belle_tips.csv`, `uchi_soto.csv`,
      `keigo_types.csv` to config.py: `BELLE_TIPS_COLUMNS`,
      `UCHI_SOTO_COLUMNS`, `KEIGO_TYPES_COLUMNS`
- [ ] Add enum checks: `context` for belle_tips, `arrow_direction` for
      uchi_soto, `type_name` for keigo_types
- [ ] Add three new `check_csv` calls in `validate.py`
- [ ] Run and confirm 0 errors

---

## Task 7 — Add CSS animations to assets/style.css

**Files:** `assets/style.css`

- [ ] Title pencil-draw underline (`kcPencilDraw` on `.kc-title::after`,
      `.kc-hero-title::after`)
- [ ] Washi tape stick-on (`kcWashiIn` on all card `::before` elements)
- [ ] Practice step page-reveal (`kcPageReveal` on `.kc-step-heading`,
      `.kc-step-hint`, `.kc-option-buttons`)
- [ ] Hanko stamp styles and `kcHanko` keyframes for `.kc-hanko`
- [ ] Gentle shake (`kcShake`) on `.kc-feedback-wrong` and
      `.kc-belle-wrapper.pose-tilt`
- [ ] Tab page fade (`kcPageFade`) on `[data-testid="stMainBlockContainer"]`
- [ ] Tip bubble styles and `kcTipPop` keyframes for `.kc-tip-bubble`
- [ ] All wrapped in `@media (prefers-reduced-motion: no-preference)` blocks
      with graceful fallback for `reduce`

---

## Task 8 — Create assets/belle_interactions.css

**Files:** `assets/belle_interactions.css`, `kc_utils.py`

- [ ] Add `kcBob` animation override for `.pose-sit #belle` if not in
      `belle_poses.css`
- [ ] Blink keyframes: `belleBlink`, `belleBlinkClose` targeting
      `#eyes-open` and `#eyes-closed` via `.kc-belle-wrapper`
- [ ] Sleep after 30s: extend blink animations with a 30s delay fadeout
- [ ] Ears perk on hover: `belleEarPerk` on `.kc-belle-wrapper:hover #ear-left`
      and `#ear-right`
- [ ] Add `belle_interactions.css` loading to `inject_css()` in `kc_utils.py`

---

## Task 9 — Add new pose classes to assets/belle_poses.css

**Files:** `assets/belle_poses.css`

- [ ] Add `.pose-tail-wag #tail` with `belleTailWag` animation
- [ ] Add `.pose-ear-flop #ear-left`, `.pose-ear-flop #ear-right` with
      `belleEarFlop` animation
- [ ] Define `belleTailWag` and `belleEarFlop` keyframes
- [ ] Wrap in `prefers-reduced-motion: no-preference`

---

## Task 10 — Update pages/home.py: larger situation cards

**Files:** `pages/home.py`, `content/home.md`, `config.py`

- [ ] Render situation buttons using icon from `config.SITUATION_ICONS`
      and description from `home.md` sections; no text truncation
- [ ] Use CSS class `kc-situation-buttons` for sticky-note styling
- [ ] Descriptions come from `sections["situation-card-{key}"]`

---

## Task 11 — Update pages/home.py: ウチ/ソト diagram

**Files:** `pages/home.py`, `data/uchi_soto.csv`

- [ ] Load `uchi_soto.csv` with `@st.cache_data`
- [ ] Render section heading from `config.HOME_SECTION_UCHI_SOTO`
- [ ] Two `st.selectbox` calls using `config.UCHI_SOTO_SPEAKER_OPTIONS`
      and `config.UCHI_SOTO_LISTENER_OPTIONS`
- [ ] Look up matching row; render an HTML diagram showing speaker box,
      directional arrow, listener box, expected keigo label, and
      explanation_en
- [ ] Arrow color: `--kc-sonkeigo` for `up`, `--kc-kenjogo2` for `down`
- [ ] All text from CSV or config; no hardcoded strings in Python

---

## Task 12 — Update pages/home.py: keigo type cards

**Files:** `pages/home.py`, `data/keigo_types.csv`

- [ ] Load `keigo_types.csv` with `@st.cache_data`
- [ ] Render section heading from `config.HOME_SECTION_KEIGO_TYPES`
- [ ] Five-column layout; one card per type
- [ ] Each card: badge (colored per `badge_css_class`), type name,
      definition_en, example_jp, example_en, and "Source needed" if
      `verified = false`
- [ ] No hardcoded text in Python

---

## Task 13 — Add Belle tap interaction to all pages

**Files:** `kc_utils.py`, `pages/practice.py`, `pages/home.py`

- [ ] Load `belle_tips.csv` and cache it; expose a `load_tips()` function
      in `kc_utils.py`
- [ ] Render a small tap button (`config.BELLE_TAP_LABEL`) next to Belle
      in `belle_header_html`; on click, pick a random `context=general`
      tip and store in `st.session_state["belle_tip"]`
- [ ] Render the tip bubble below Belle when `belle_tip` is set
- [ ] In `pages/practice.py`, after step submissions: set
      `st.session_state["belle_tip"]` to a `context=correct` or
      `context=wrong` tip
- [ ] In `render_explanation`, if final answer was correct:
      render `<div class="kc-hanko">{config.HANKO_CORRECT_TEXT}</div>`

---

## Task 14 — Update pages/about.py: author section

**Files:** `pages/about.py`, `content/author.md`, `kc_utils.py`

- [ ] `parse_home_md` already handles `## heading` parsing; reuse it
      (rename to `parse_md_sections` in `kc_utils.py` or call it for
      `author.md` too)
- [ ] Append author section below existing content in `about.py`
- [ ] Render heading from `config.ABOUT_AUTHOR_HEADING`
- [ ] Render author name, why-built text, and links from parsed sections

---

## Task 15 — Fix Phrase Library duplicate header

**Files:** `pages/phrase_library.py`

- [ ] Investigate the source of the duplicate header (likely a sidebar
      element or a second `belle_header_html` call)
- [ ] Remove the duplicate so the header appears exactly once
- [ ] Confirm the sidebar filter panel still works (it uses `with st.sidebar:`)
- [ ] Note: with `st.navigation` the sidebar is hidden globally; the Phrase
      Library sidebar filters need to be moved to the main area or a
      `st.expander`

---

## Task 16 — Heading font consistency

**Files:** `assets/style.css`

- [ ] Audit all heading elements (`h1`, `h2`, `h3`, section titles) across
      all tabs
- [ ] Ensure `.kc-section-heading`, `.kc-why-title`, `.kc-step-title`,
      explanation title, and any raw `h2`/`h3` rendered by `st.markdown`
      all use `font-family: var(--kc-font-heading)`
- [ ] Add a CSS rule targeting Streamlit's default heading elements:
      `h1, h2, h3 { font-family: var(--kc-font-heading) !important; }`

---

## Task 17 — Run validate.py and restart

- [ ] Run `python validate.py` — confirm 0 errors across all CSVs
- [ ] Restart app once with `streamlit run app.py`
- [ ] Verify: all five tabs load, animations play (including pencil
      underline, washi tape), Belle blinks, tap button shows a tip,
      Practice shows hanko on correct step 4, ウチ/ソト diagram responds
      to selectbox changes, keigo type cards render, author section
      visible on About
