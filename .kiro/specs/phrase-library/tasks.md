# Phrase Library — Tasks

## Status key
- [ ] not started
- [x] done

---

## Task 1 — Create data/phrases.csv with 10 sample rows

**Files:** `data/phrases.csv`

- [x] Create the `data/` directory.
- [x] Add the CSV header row with all 12 columns:
      `id, situation, action_by, casual_jp, polite_jp, keigo_jp,
      keigo_type, english_meaning, explanation_rule,
      explanation_example, source, verified`
- [x] Add 10 sample rows covering:
  - All four situations (`interview`, `email`, `phone`, `meeting`)
  - Both `action_by` values (`me`, `other_person`)
  - Common business verbs: 言う, 見る, 行く, 来る, いる, する, 知る, もらう
  - A mix of keigo types (尊敬語, 謙譲語I, 謙譲語II, 丁寧語)
- [x] Set `source = "needs review"` on every row.
- [x] Set `verified = false` on every row.

---

## Task 2 — Create validate.py

**Files:** `validate.py`

- [x] Load the CSV with pandas; exit with a clear message if the file
      is not found.
- [x] Check that all 12 expected columns are present.
- [x] For each row, check for empty/NaN values in every column.
- [x] Validate `situation` against `{interview, email, phone, meeting}`.
- [x] Validate `action_by` against `{me, other_person}`.
- [x] Validate `keigo_type` against `{尊敬語, 謙譲語I, 謙譲語II, 丁寧語, 美化語}`.
- [x] Collect `verified = false` rows as warnings.
- [x] Print all errors first, then all warnings, then a summary line.
- [x] Exit with code `1` if there are any errors, `0` otherwise.
- [x] Add comments explaining each section for a reader new to Python.

---

## Task 3 — Create app.py (Streamlit browse page)

**Files:** `app.py`

- [x] Import `streamlit` and `pandas`; add a comment block at the top
      explaining the file's purpose.
- [x] Load `data/phrases.csv` with `pd.read_csv`; cache with
      `@st.cache_data` so it doesn't reload on every interaction.
- [x] Set the page title and layout (`wide`).
- [x] Add a sidebar with:
  - Situation selectbox: `["All", "interview", "email", "phone", "meeting"]`
  - Keigo type selectbox: `["All", "尊敬語", "謙譲語I", "謙譲語II", "丁寧語", "美化語"]`
- [x] Apply the selected filters to the DataFrame (AND logic).
- [x] Show a "Showing N of M phrases" caption above the table.
- [x] Display the filtered table with `st.dataframe`, hiding `id`,
      `source`, and `verified` columns.
- [x] Use `use_container_width=True` for responsive layout.
- [x] Add inline comments explaining each step.

---

## Task 4 — Create requirements.txt

**Files:** `requirements.txt`

- [x] Add `streamlit==1.67.0` (updated from 1.35.0 — requires Python 3.13)
- [x] Add `pandas==3.1.1` (updated from 2.2.2 — requires Python 3.13)

---

## Task 5 — Update README.md

**Files:** `README.md`

- [x] Add a **Setup** section with:
  - Prerequisites (Python 3.10+)
  - venv creation and activation
  - `pip install -r requirements.txt`
  - `streamlit run app.py`
  - `python validate.py`
- [x] Keep the existing project description at the top.
