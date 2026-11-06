# Answer Logging — Design (not yet built)

## Purpose

Anonymously record each answer step so the author can see which scenarios
and steps learners find hardest, without collecting any personal data.

## Schema

One row per submitted step.

| Column        | Type     | Description                                  |
|---------------|----------|----------------------------------------------|
| `ts`          | ISO 8601 | Timestamp of submission (UTC)                |
| `scenario_id` | integer  | The `id` field from data/scenarios.csv       |
| `step`        | integer  | 1, 2, 3, or 4                                |
| `correct`     | boolean  | Whether the submitted answer was correct     |

No user identifiers, IP addresses, or answer content are stored.

## Storage options (choose one when building)

- **Streamlit Community Cloud:** Streamlit's built-in `st.connection` with
  a free-tier Supabase or PlanetScale database.
- **Local / self-hosted:** append rows to a `logs/answers.jsonl` file.

## When to build

After the first round of real user testing, so the schema can be adjusted
based on what questions actually come up.
