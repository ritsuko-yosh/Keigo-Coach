---
inclusion: always
---

# Keigo Coach — Content Rules

These rules apply to every file in this project, including CSV data,
markdown content, Python code, and comments.

## Sources

Every phrase and scenario must be traceable to a published source.
Allowed sources:

- 文化審議会答申「敬語の指針」(2007).
  NDL record: https://ndlsearch.ndl.go.jp/en/books/R100000039-I1164598
- Academic papers summarising it, for example:
  https://petit.lib.yamaguchi-u.ac.jp/23172/files/155453

If a source cannot be opened and the specific page or section confirmed,
the row must use:

```
source      = "needs review"
source_url  = (empty)
source_page = (empty)
verified    = false
```

Never invent keigo rules, verb forms, explanations, or examples. If a fact
cannot be cited, flag it as needs review rather than stating it as fact.

## Names

Use only fictional names (for example: 田中、吉田、山田 used as surnames
without specific given names). Never use the owner's real name,
collaborators' names, or any name found in local git config. This applies
to CSV data, markdown files, Python comments, and all other text.

## Em dashes

No em dashes (the character —) anywhere in this project. Not in CSV fields,
markdown files, Python strings, CSS comments, or any other file. Use commas,
semicolons, colons, or periods as alternatives.

## Hardcoding

- UI text (button labels, captions, error messages, feedback strings) belongs
  in config.py. Never write it as a string literal in Python logic.
- Phrase and scenario content belongs in CSV files. Never write it in Python.
- File paths belong in config.py. Never write a literal path string in Python
  logic files.
- CSS values belong in assets/style.css. Never write colour hex codes,
  font names, or spacing values in Python strings.

## Validation

Run `python validate.py` before saving data changes. The script checks both
CSVs for missing fields, invalid enum values, missing source fields, and
unverified rows. Fix all errors (exit code 1) before running the app.
