# Homepage and Navigation — Requirements

## Overview

Restructure Keigo Coach from a single-entry Decision Simulator into a
five-page app with top-tab navigation. Add a home page that contextualises
the problem and funnels users into practice. Improve the Practice page UX
with card-based option selection, step hints, and a progress indicator.
Add a coming-soon My Progress placeholder. Keep the About page unchanged.

All tab names, labels, hint text, and UI strings belong in config.py.
All home-page text belongs in content/home.md.
No app code changes may introduce hardcoded strings or em dashes.

---

## US-1 — Top navigation

> As a user, I want to see the main sections of the app in a tab bar at
> the top of every page so that I can move between them without hunting
> through a sidebar.

**Acceptance criteria:**
- Five tabs are visible at the top of every page: Home, Practice,
  Phrase Library, My Progress, About.
- The current page's tab is visually distinguished from the others.
- Tab labels come from config.py, never hardcoded.
- Navigation uses `st.navigation` with `position="hidden"` and
  `st.page_link` for the tab bar. If `st.navigation` is unavailable, fall
  back to `st.tabs` in a single app.py file.
- The Streamlit sidebar is hidden for all pages.

---

## US-2 — Home page

> As a first-time visitor, I want to understand what Keigo Coach does and
> get into practice in one click.

**Acceptance criteria:**
- Hero section: Belle (or placeholder), app title, one-sentence description
  read from content/home.md, and a "Start practicing" button that navigates
  to the Practice page.
- "How it works" section: exactly three steps, text read from home.md.
- Five clickable situation cards (one per scenario situation), each opening
  Practice pre-filtered to that situation.
- A short "why keigo is hard" note that explains ウチ/ソト using the
  fictional name 田中. Text read from home.md.
- No invented content: every text string that is not structural (button
  labels, headings) comes from home.md or config.py.

---

## US-3 — Practice page improvements

> As a learner, I want each answer choice to feel intentional and clear,
> and I want to know where I am in the scenario set.

**Acceptance criteria:**
- Each step presents options as large, full-width clickable cards, not
  radio buttons. Clicking a card submits the answer immediately.
- A short hint is shown beneath each step heading, read from config.py.
- A progress line is shown above the scenario card:
  "Scenario X of 5, Step X of 4". Format string in config.py.
- Scenario 1 uses the fictional name 田中 (not any real name). The
  scene_en, scene_jp, correct_sentence, and wrong_options fields in
  data/scenarios.csv are updated accordingly.
- The existing step logic, Belle pose changes, and full explanation are
  preserved.

---

## US-4 — My Progress placeholder

> As a user, I want to see that progress tracking is planned even though
> it is not built yet.

**Acceptance criteria:**
- My Progress page shows a single "coming soon" message.
- No fake statistics, counters, or placeholder charts.
- Message text comes from config.py.

---

## US-5 — About page unchanged

> As a user, I want the About page to continue showing the current content.

**Acceptance criteria:**
- About page content is identical to the current version.
- The page is accessible from the new top navigation.
