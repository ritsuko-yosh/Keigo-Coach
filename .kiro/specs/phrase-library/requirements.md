# Phrase Library — Requirements

## Overview

The phrase library is the data and browsing foundation of Keigo Coach.
It stores a curated set of Japanese business phrases in a CSV file and
surfaces them through a simple Streamlit web page. An English-speaking
learner can filter by situation and keigo type, then compare the casual,
polite, and keigo forms of each phrase alongside an English meaning and
a grammar explanation.

A companion validation script helps the content author catch data-quality
problems (missing fields, invalid enum values, unverified rows) before
the app is run.

---

## User Stories

### US-1 — Browse phrases by situation

> As a bilingual job seeker studying business Japanese,
> I want to filter the phrase list by situation (interview, email, phone,
> meeting) so that I can focus on language that is relevant right now.

**Acceptance criteria:**
- The browse page shows a situation filter (default: all situations).
- Selecting a situation hides rows that do not match.
- The filter resets to "all" when the user removes the selection.

---

### US-2 — Filter by keigo type

> As a learner, I want to filter by keigo type (尊敬語, 謙譲語I,
> 謙譲語II, 丁寧語, 美化語) so that I can study one grammatical
> category at a time.

**Acceptance criteria:**
- The browse page shows a keigo-type filter (default: all types).
- Situation and keigo-type filters combine (AND logic).
- The active filter state is visible at all times.

---

### US-3 — Compare phrase forms side by side

> As a learner, I want to see the casual, polite, and keigo versions of
> a phrase in the same row so that I can understand the transformation
> at a glance.

**Acceptance criteria:**
- Each table row shows: situation, keigo type, casual (Japanese),
  polite (Japanese), keigo (Japanese), English meaning, and explanation.
- Long explanation text is readable without horizontal scrolling.

---

### US-4 — Understand who performs the action

> As a learner, I want to know whether a phrase is used when I am the
> actor ("me") or when the other person is the actor ("other_person") so
> that I do not accidentally use humble language when I should use
> honorific language (or vice versa).

**Acceptance criteria:**
- The `action_by` column is visible in the table or clearly labeled.

---

### US-5 — Validate CSV content

> As a content author, I want to run a script that reports any rows with
> missing fields, invalid enum values, or unverified status so that I
> can fix data quality issues before they reach learners.

**Acceptance criteria:**
- The script exits 0 and prints a summary when the CSV is clean.
- The script prints a clear, actionable error message for every
  problematic row, identifying the row number and the specific issue.
- Invalid situation, action_by, or keigo_type values are flagged.
- Rows where `verified = false` are listed as a warning (not an error).

---

### US-6 — Install and run the app locally

> As a developer or learner setting up the project, I want a
> requirements.txt and README instructions so that I can get the app
> running with a few commands.

**Acceptance criteria:**
- `requirements.txt` lists all necessary packages with pinned versions.
- README includes: prerequisites, install steps, how to run the
  Streamlit app, and how to run the validation script.

---

## Data Model

File: `data/phrases.csv`

| Column               | Type    | Allowed values                                          |
|----------------------|---------|---------------------------------------------------------|
| `id`                 | integer | unique, sequential                                      |
| `situation`          | enum    | `interview`, `email`, `phone`, `meeting`                |
| `action_by`          | enum    | `me`, `other_person`                                    |
| `casual_jp`          | string  | Japanese text (may be empty if no casual equivalent)    |
| `polite_jp`          | string  | Japanese text (です/ます form)                           |
| `keigo_jp`           | string  | Japanese text (full keigo)                              |
| `keigo_type`         | enum    | `尊敬語`, `謙譲語I`, `謙譲語II`, `丁寧語`, `美化語`      |
| `english_meaning`    | string  | English gloss of the keigo phrase                       |
| `explanation_rule`   | string  | Grammar rule in English                                 |
| `explanation_example`| string  | Usage example or note in English                        |
| `source`             | string  | Free text — citation or `"needs review"`                |
| `verified`           | boolean | `true` or `false`                                       |

---

## Out of Scope (this feature)

- Quiz / practice mode
- User session logging
- Progress dashboard
- Authentication
