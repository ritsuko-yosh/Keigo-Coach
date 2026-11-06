---
inclusion: always
---

# Keigo Coach — Tech

## Stack

- Python 3.13
- Streamlit 1.67.0
- pandas 3.1.1
- Google Fonts via @import: DM Sans (body), Caveat (handwritten accent),
  Klee One (Japanese text)

## File layout

```
app.py                     Decision Simulator (Streamlit main page)
pages/
  1_Phrase_Library.py      Phrase reference browser
  2_About.py               About page
config.py                  Single source of truth for all settings
kc_utils.py                Shared utilities (CSS injection, Belle header)
validate.py                Data quality checker for both CSVs
data/
  phrases.csv              Phrase library (14 columns)
  scenarios.csv            Simulator scenarios (14 columns)
assets/
  style.css                All visual styles
  belle_poses.css          Belle's pose and animation rules
  belle_sit.svg            Belle SVG (exact file, do not modify)
content/
  about.md                 About page text (edit here, not in Python)
docs/
  screenshots/             Empty folder, reserved for portfolio screenshots
requirements.txt           Pinned dependencies
```

## Architecture rules

- **Content in data files only.** No phrase text, scenario text, or
  explanations in Python files.
- **Settings in config.py only.** All file paths, enum values, display labels,
  icon strings, UI text, color class names, and pose names must be defined
  in config.py and imported. Never hardcode them in Python logic.
- **CSS in assets/ only.** No style values in Python strings except
  `animation-delay` on individual cards (where it varies per item).
  `belle_poses.css` is loaded alongside `style.css` in every page via
  `kc_utils.inject_css()`.
- **Shared utilities in kc_utils.py.** CSS injection and the Belle header
  block are defined once there and imported by every page.
- **Belle's SVG is read from file and inlined** (not used as an `<img>`)
  so that `belle_poses.css` can reach her internal parts by ID.
- **No secrets or local paths in code.** Ready for Streamlit Community Cloud:
  main file is `app.py`, no environment variables required.

## Validation

Run `python validate.py` before committing. Both `data/phrases.csv` and
`data/scenarios.csv` are checked. Exit code 1 means errors that must be
fixed; warnings (missing source, unverified rows) are acceptable but
should be resolved when a source is confirmed.
