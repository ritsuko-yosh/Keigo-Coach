# Homepage and Navigation — Tasks

## Status key
- [ ] not started
- [x] done

---

## Task 1 — Fix scenario 1 data

**Files:** `data/scenarios.csv`

- [ ] Replace "吉田里津子" with "田中" in `scene_en`, `scene_jp`,
      `correct_sentence`, and both entries in `wrong_options` for row id=1.
- [ ] Confirm no other real names appear in either CSV.
- [ ] Run `python validate.py` and confirm 0 errors.

---

## Task 2 — Add new config.py keys

**Files:** `config.py`

- [ ] Add `HOME_MD_PATH = "content/home.md"`.
- [ ] Add navigation tab labels: `NAV_HOME`, `NAV_PRACTICE`,
      `NAV_PHRASE_LIBRARY`, `NAV_MY_PROGRESS`, `NAV_ABOUT`.
- [ ] Add `NAV_PAGES`: ordered list of `(page_path, label)` tuples.
- [ ] Add `SITUATION_CARDS`: ordered list of `(situation_key, display_label)`.
- [ ] Add `STEP_HINTS` dict (steps 1-4).
- [ ] Add `PROGRESS_FORMAT` string.
- [ ] Add `MY_PROGRESS_COMING_SOON` string.
- [ ] Add `START_BUTTON_LABEL`.
- [ ] Remove `SUBMIT_LABEL` (no longer used in Practice after this feature).
      Check no other page still uses it before removing.

---

## Task 3 — Create content/home.md

**Files:** `content/home.md`

- [ ] Add sections in order: `tagline`, `start-button`, `how-it-works-intro`,
      `step-1-label`, `step-1-detail`, `step-2-label`, `step-2-detail`,
      `step-3-label`, `step-3-detail`, one `situation-card-*` section per
      situation, `why-keigo-hard`.
- [ ] Write the `why-keigo-hard` section using the fictional name 田中 for
      the ウチ/ソト example.
- [ ] No em dashes, no real names, no invented keigo facts.
- [ ] Source for any keigo claims is cited or the passage is clearly
      labelled as a usage illustration (not a factual claim).

---

## Task 4 — Add helpers to kc_utils.py

**Files:** `kc_utils.py`

- [ ] Add `parse_home_md() -> dict[str, str]`: reads `config.HOME_MD_PATH`,
      splits on `## ` headings, returns dict of `{key: text}`.
- [ ] Add `render_top_nav(nav_pages: list) -> None`: renders a row of
      `st.page_link` calls in `st.columns`, one column per page.
- [ ] Both functions are documented with a one-line docstring.

---

## Task 5 — Restructure page files

**Files:** rename/move existing pages; create new ones

- [ ] Move Decision Simulator logic from `app.py` to a new `pages/practice.py`.
      Keep all step rendering, pose logic, and explanation rendering intact.
- [ ] Rename `pages/1_Phrase_Library.py` to `pages/phrase_library.py`.
      No logic changes.
- [ ] Rename `pages/2_About.py` to `pages/about.py`. No logic changes.
- [ ] Create empty stubs for `pages/home.py` and `pages/my_progress.py`
      (to be filled in Tasks 6 and 7).
- [ ] Confirm all `import` and `from` statements still resolve after rename.

---

## Task 6 — Rewrite app.py as navigation hub

**Files:** `app.py`

- [ ] Import `st.navigation` and `st.Page`.
- [ ] Define the five pages using `config.NAV_PAGES`, with `position="hidden"`.
- [ ] Call `inject_css()` once at the top (CSS applies to every page).
- [ ] Call `render_top_nav(config.NAV_PAGES)` to show the tab bar.
- [ ] Call `pg.run()` to execute the current page.
- [ ] Add CSS to `assets/style.css` to hide the Streamlit sidebar
      (`[data-testid="stSidebar"] { display: none !important; }`) if not
      already present.
- [ ] Add CSS to distinguish the active page link in the tab bar.

---

## Task 7 — Build pages/home.py

**Files:** `pages/home.py`, `content/home.md`

- [ ] Set page config: title from `config.NAV_HOME`, icon "🏠".
- [ ] Call `inject_css()` and render the Belle header with `belle_header_html`.
- [ ] Read sections from `parse_home_md()`.
- [ ] Hero: render `sections["tagline"]` and a button using
      `config.START_BUTTON_LABEL`. On click, call
      `st.switch_page("pages/practice.py")`.
- [ ] How it works: three-column layout using steps from home.md sections.
- [ ] Situation cards: one `st.button` per `config.SITUATION_CARDS` entry
      in a five-column row. On click: set
      `st.session_state["practice_filter"] = situation_key` then call
      `st.switch_page("pages/practice.py")`.
- [ ] Why keigo is hard: render `sections["why-keigo-hard"]` with
      `st.markdown`.

---

## Task 8 — Update pages/practice.py (option cards, hints, progress)

**Files:** `pages/practice.py`

- [ ] Add practice_filter handling at the top of `main()`: pop
      `"practice_filter"` from session state, find matching scenario index,
      call `reset_scenario()`.
- [ ] Add progress indicator above the scenario card using
      `config.PROGRESS_FORMAT`.
- [ ] Replace each `st.radio + st.button("Check answer")` with a loop of
      `st.button(option, use_container_width=True)`. Clicking selects and
      submits immediately. Remove the separate submit button.
- [ ] Render step hint using `config.STEP_HINTS[n]` below the step heading.
- [ ] Preserve all existing step logic, feedback messages, Belle poses,
      and the full explanation block.

---

## Task 9 — Create pages/my_progress.py

**Files:** `pages/my_progress.py`

- [ ] Set page config: title from `config.NAV_MY_PROGRESS`.
- [ ] Call `inject_css()` and render the Belle header.
- [ ] Display `config.MY_PROGRESS_COMING_SOON` with `st.info` or
      `st.markdown`.
- [ ] No charts, counters, or fake data.

---

## Task 10 — Verify and run

- [ ] Run `python validate.py` — confirm 0 errors.
- [ ] Run `streamlit run app.py` — confirm all five tabs render, Home loads
      with Belle, situation cards navigate to Practice with the correct
      scenario pre-selected, Practice shows progress + hints + option cards,
      My Progress shows coming-soon message, About shows existing content.
- [ ] Check that no page shows the Streamlit sidebar.
- [ ] Check that the tab bar shows the correct current page as active.
