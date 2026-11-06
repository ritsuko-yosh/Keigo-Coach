# Keigo Coach

**Step-by-step keigo practice for bilingual job seekers.**

---

## The problem

Standard Japanese classes teach polite speech (です/ます). Japanese workplaces
run on keigo. The gap is real, and the hardest part is not the verb forms:
it is knowing when to use each one, especially the ウチ/ソト distinction
(in-group vs out-group) that decides whether to humble yourself or honor
the other person.

---

## Features

- **Decision Simulator:** walk through real scenarios step by step.
  Identify who is acting, who is listening, which keigo type applies,
  then pick the correct sentence. Instant feedback on each step.
- **Phrase Library:** browse and filter 10+ keigo forms by situation and type.
  Compare casual, polite, and keigo forms side by side with English explanations.
- **About:** explains ウチ/ソト and 相互尊重 in plain English for anyone
  new to the concept.
- **Source citations:** every row links to a published reference or is flagged
  "Source needed" for review.
- **Hide keigo toggle:** blur the keigo form and test recall before revealing.

---

## Screenshots

_(Add screenshots here after deploying)_

---

## Tech stack

| Layer       | Tool                              |
|-------------|-----------------------------------|
| Language    | Python 3.13                       |
| Framework   | Streamlit 1.67.0                  |
| Data layer  | pandas 3.1.1                      |
| Fonts       | DM Sans, Caveat, Klee One (Google Fonts) |
| Data format | Hand-curated CSV with source citations |

---

## How content is verified

Each phrase and scenario has `source`, `source_url`, and `source_page` columns.

The primary reference is the 2007 government advisory document
「敬語の指針」 published by the 文化審議会 (Agency for Cultural Affairs):
https://ndlsearch.ndl.go.jp/en/books/R100000039-I1164598

Rows marked `verified = false` are pending review. Run `python validate.py`
at any time to see the current verification status of all data.

---

## How to run locally

**Prerequisites:** Python 3.10 or later.

```bash
# 1. Clone and enter the project
git clone <repo-url>
cd keigo-coach

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Validate data (optional but recommended)
python validate.py

# 5. Run the app
streamlit run app.py
```

The app opens at http://localhost:8501.

---

## Deploying to Streamlit Community Cloud

1. Push to a public GitHub repository.
2. Go to https://share.streamlit.io and connect the repo.
3. Set the main file to `app.py`.
4. No secrets required.

---

## Results

_(Fill in after user testing)_

---

## Planned features

- Anonymous answer logging (schema: scenario id, step, correct/incorrect,
  timestamp). Design notes in `.kiro/specs/answer-logging/design.md`.
