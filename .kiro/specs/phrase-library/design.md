# Phrase Library — Design

## Architecture

This is a single-feature, local-first app. No server, no database — just
a CSV file, a Streamlit page, and a standalone validation script.

```
keigo-coach/
├── data/
│   └── phrases.csv          # All phrase data; edited by hand
├── app.py                   # Streamlit browse page (entry point)
├── validate.py              # CLI data-quality checker
├── requirements.txt         # Pinned Python dependencies
└── README.md                # Setup and usage instructions
```

No Python packages beyond `streamlit` and `pandas` are needed at this stage.

---

## data/phrases.csv

Plain UTF-8 CSV with a header row. Columns follow the data model defined
in requirements.md. The file is human-editable in any spreadsheet app or
text editor. All 10 sample rows use `source = "needs review"` and
`verified = false` so the author can review them before marking them live.

Verbs covered in the sample data (at minimum):

| Verb (casual) | Situations targeted |
|---------------|---------------------|
| 言う           | meeting, email      |
| 見る           | meeting             |
| 行く           | interview           |
| 来る           | phone, interview    |
| いる           | email               |
| する           | meeting             |
| 知る           | email, interview    |
| もらう         | phone               |

---

## app.py — Streamlit browse page

### Libraries
- `streamlit` — UI framework
- `pandas` — CSV loading and filtering

### Page structure

```
Title: "Keigo Coach — Phrase Library"

Sidebar:
  - Selectbox: Filter by Situation  [All, interview, email, phone, meeting]
  - Selectbox: Filter by Keigo Type [All, 尊敬語, 謙譲語I, 謙譲語II, 丁寧語, 美化語]

Main area:
  - Row count ("Showing N of M phrases")
  - DataFrame table with columns:
      situation | action_by | keigo_type | casual_jp | polite_jp | keigo_jp
      | english_meaning | explanation_rule | explanation_example
  - Note: id, source, verified are hidden from the table (internal fields)
```

### Filtering logic

```python
# Start with all rows
filtered = df.copy()

# Apply situation filter if not "All"
if situation != "All":
    filtered = filtered[filtered["situation"] == situation]

# Apply keigo_type filter if not "All"
if keigo_type != "All":
    filtered = filtered[filtered["keigo_type"] == keigo_type]
```

### Display considerations
- Use `st.dataframe` with `use_container_width=True` for responsive layout.
- Column widths: narrow for enum columns, wide for explanation columns.
- UTF-8 Japanese characters render correctly in Streamlit out of the box.

---

## validate.py — CSV validation script

### What it checks

| Check                  | Severity | Description                                      |
|------------------------|----------|--------------------------------------------------|
| File exists / readable | ERROR    | Script exits immediately                         |
| Expected columns present | ERROR  | Reports missing column names                     |
| Missing field values   | ERROR    | Any cell that is empty (NaN or blank string)     |
| Invalid `situation`    | ERROR    | Value not in allowed enum                        |
| Invalid `action_by`    | ERROR    | Value not in allowed enum                        |
| Invalid `keigo_type`   | ERROR    | Value not in allowed enum                        |
| `verified = false`     | WARNING  | Row needs human review before going live         |

### Output format

```
Validating data/phrases.csv...

ERRORS (must fix before running the app):
  Row 3: missing value in column 'keigo_jp'
  Row 7: invalid situation 'presentation' — must be one of interview, email, phone, meeting

WARNINGS (should review):
  Row 1: verified = false
  Row 2: verified = false
  ...

Summary: 2 errors, 10 warnings.
```

If there are no errors and no warnings, the script prints:
```
All 10 rows are valid and verified. ✓
```

### Exit codes
- `0` — no errors (warnings are allowed)
- `1` — one or more errors found

---

## requirements.txt

```
streamlit==1.67.0
pandas==3.1.1
```

Both packages are pinned to a specific version so the environment is
reproducible. These versions require Python 3.13 or later. If you need
to update, change the pins here and in requirements.txt together.

---

## README additions

The existing README gets a new **Setup** section:

```markdown
## Setup

**Prerequisites:** Python 3.10 or later.

### 1. Install dependencies
\```
pip install -r requirements.txt
\```

### 2. Run the browse app
\```
streamlit run app.py
\```
The app opens in your browser at http://localhost:8501.

### 3. Validate the phrase data
\```
python validate.py
\```
Fix any ERRORs before using the app. Rows marked `verified = false` are
flagged as WARNINGs — review and set `verified = true` when the content
is confirmed correct.
```

---

## Not implemented in this feature

- User accounts or login
- Persistent quiz results
- Any write-back to the CSV from the UI
