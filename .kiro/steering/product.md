---
inclusion: always
---

# Keigo Coach — Product

Keigo Coach helps bilingual job seekers learn business keigo through active
decisions, not phrase memorisation. The core experience is a step-by-step
Decision Simulator: the learner identifies who acts, who listens (ウチ/ソト),
which keigo type applies, then picks the correct sentence.

## Goals

1. Teach business keigo as a decision skill, not a grammar list.
2. Serve as a portfolio piece for recruiters at US companies: show problem
   solving, data rigor, and good judgment with AI-generated content.
3. Present keigo as culturally rooted in ウチ/ソト (in-group/out-group) and
   mutual respect (相互尊重), not just as grammar rules.

## Mascot and tone

The mascot is Belle, the owner's dog. Tone is calm, deadpan, and cute.
Belle reacts with short Japanese phrases: for example "あれ…？" when the
learner is wrong, "正解です。" after a correct keigo answer. No celebrations,
streaks, XP, points, hearts, or leaderboards. The experience should never
feel like Duolingo.

## Pages

- **Decision Simulator** (main, app.py): five scenarios, one per situation,
  with step-by-step feedback on actor, listener, keigo type, and sentence.
- **Phrase Library** (pages/1_Phrase_Library.py): filterable reference for
  casual, polite, and keigo forms side by side.
- **About** (pages/2_About.py): explains ウチ/ソト and 相互尊重 in plain
  English for non-Japanese-speaking recruiters; describes sourcing approach.

## Out of scope (current version)

- User accounts and authentication
- Scoring, progress tracking, or streaks
- Anonymous answer logging (design only, in .kiro/specs/answer-logging/)
