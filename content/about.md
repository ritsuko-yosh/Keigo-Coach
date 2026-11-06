# About Keigo Coach

## The problem

Job hunting in Japan as a bilingual candidate involves a specific challenge:
standard Japanese classes teach polite speech (丁寧語), but Japanese workplaces
run on keigo, a structured system of honorific and humble language that marks
social relationships in real time.

The hardest part is not memorising the verb forms. It is knowing when each
form applies. The most common source of confusion is the ウチ/ソト distinction.
In Japanese, your choice of language signals whether someone belongs to your
in-group (ウチ, inside) or out-group (ソト, outside). Even a senior colleague
is treated as ウチ when you speak to a client. This means the humble forms you
use for your own actions also apply to your boss's actions when you are speaking
to an outsider.

## Who this is for

Keigo Coach is built for bilingual job seekers with solid conversational
Japanese who are preparing for interviews, recruiter emails, and early
professional communication. It assumes you already know polite speech
(です/ます) and are ready to move into keigo.

## Why keigo exists

Japanese keigo is not a set of arbitrary grammar rules. It is a language-level
expression of two cultural ideas.

**Respect for social position (尊重):** Japanese society has historically
distinguished between those above and below in a given relationship, and
language reflects that. Using the right form signals that you understand where
you stand.

**Mutual respect (相互尊重):** Modern Japanese workplace culture, and the
2007 government guidance on keigo from the 文化審議会 (Agency for Cultural
Affairs), emphasises that keigo is not about subordination. It is about
creating a shared atmosphere of consideration, what the document calls
丁寧なコミュニケーション (careful, considerate communication).

The ウチ/ソト axis adds a third dimension. Your language must show not only
who you are speaking to, but how the person you are speaking about relates to
both of you at the same time. That is the layer most Japanese textbooks skip.

## How content is sourced

Every phrase and scenario in Keigo Coach is traced to a published source.
The primary reference is the 2007 government advisory document
「敬語の指針」 (Guidelines on Honorific Language), published by the
文化審議会 (Agency for Cultural Affairs).

Reference record at the National Diet Library:
https://ndlsearch.ndl.go.jp/en/books/R100000039-I1164598

An academic paper summarising the document's 謙譲語I / 謙譲語II distinction:
https://petit.lib.yamaguchi-u.ac.jp/23172/files/155453

Rows marked **Unverified** are placeholders. Each one has a source to check
against, but the page number or section has not yet been confirmed. No
invented explanations are included.

## Tech stack

- Python 3.13
- Streamlit 1.67.0
- pandas 3.1.1
- Google Fonts: DM Sans (body), Caveat (accent labels), Klee One (Japanese)
- Data: hand-curated CSV files with source citations

## Planned feature: anonymous answer logging

A future version will log each answer step anonymously. The schema is
described in `.kiro/specs/answer-logging/design.md`. No personal data
will be collected.
