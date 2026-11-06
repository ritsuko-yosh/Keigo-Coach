"""
pages/practice.py - Decision Simulator practice page.
All UI text comes from config.py. All scenario content from data/scenarios.csv.
"""

import random
from html import escape

import pandas as pd
import streamlit as st

import config
from kc_utils import belle_svg_inline, source_html


@st.cache_data
def load_scenarios() -> pd.DataFrame:
    return pd.read_csv(config.SCENARIOS_CSV_PATH, dtype=str)


# ── Session state ─────────────────────────────────────────────────────────────

def init_state() -> None:
    st.session_state.setdefault("sim_idx", 0)
    st.session_state.setdefault("sim_step", 1)
    st.session_state.setdefault("sim_answers", {})


def reset_scenario() -> None:
    st.session_state.sim_step = 1
    st.session_state.sim_answers = {}


# ── Pose logic ────────────────────────────────────────────────────────────────

def step_is_correct(n: int, chosen: str, scenario: pd.Series) -> bool:
    if n == 1:
        correct_raw = str(scenario["actor"]).strip()
        return chosen == config.ACTOR_STEP_MAPPING.get(correct_raw, "other")
    if n == 2:
        return chosen == str(scenario["listener"]).strip()
    if n == 3:
        return chosen == str(scenario["correct_type"]).strip()
    if n == 4:
        return chosen == str(scenario["correct_sentence"]).strip()
    return False


def current_pose_and_comment(scenario: pd.Series) -> tuple:
    answers = st.session_state.sim_answers
    if not answers:
        pose = config.BELLE_POSES["default"]
    else:
        latest_n      = max(answers.keys())
        was_correct   = step_is_correct(latest_n, answers[latest_n], scenario)
        if not was_correct:
            pose = config.BELLE_POSES["wrong"]
        elif latest_n == 4:
            pose = config.BELLE_POSES["correct_keigo"]
        else:
            pose = config.BELLE_POSES["correct_steps"]
    return pose, config.BELLE_COMMENTS.get(pose, "")


# ── HTML helpers ──────────────────────────────────────────────────────────────

def feedback_md(correct: bool, message: str) -> None:
    cls  = "kc-feedback-correct" if correct else "kc-feedback-wrong"
    icon = config.ICON_CORRECT if correct else config.ICON_WRONG
    st.markdown(f'<div class="{cls}">{icon} {message}</div>', unsafe_allow_html=True)


# ── Step renderers ────────────────────────────────────────────────────────────

def render_step(n: int, scenario: pd.Series) -> None:
    if st.session_state.sim_step < n:
        return

    st.markdown(
        f'<div class="kc-step-heading">'
        f'<span class="kc-step-num">Step {n}</span>'
        f'<span class="kc-step-text">{escape(config.STEP_LABELS[n])}</span>'
        f'</div>'
        f'<div class="kc-step-hint">{escape(config.STEP_HINTS[n])}</div>',
        unsafe_allow_html=True,
    )

    answers = st.session_state.sim_answers

    if n == 1:
        correct_raw = str(scenario["actor"]).strip()
        correct     = config.ACTOR_STEP_MAPPING.get(correct_raw, "other")
        options     = list(config.ACTOR_STEP_OPTIONS.keys())

        if n in answers:
            chosen = answers[n]
            is_ok  = chosen == correct
            msg = (config.FEEDBACK_CORRECT[n] if is_ok
                   else config.FEEDBACK_WRONG[n].format(
                       correct_actor=config.ACTOR_STEP_OPTIONS[correct]))
            feedback_md(is_ok, msg)
        else:
            st.markdown('<div class="kc-option-buttons">', unsafe_allow_html=True)
            for i, opt in enumerate(options):
                label = config.ACTOR_STEP_OPTIONS[opt]
                if st.button(label, key=f"s1_opt{i}", use_container_width=True):
                    answers[n] = opt
                    st.session_state.sim_step = 2
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    elif n == 2:
        correct = str(scenario["listener"]).strip()
        options = list(config.LISTENER_OPTIONS.keys())

        if n in answers:
            chosen = answers[n]
            is_ok  = chosen == correct
            msg = (config.FEEDBACK_CORRECT[n] if is_ok else config.FEEDBACK_WRONG[n])
            feedback_md(is_ok, msg)
        else:
            st.markdown('<div class="kc-option-buttons">', unsafe_allow_html=True)
            for i, opt in enumerate(options):
                label = config.LISTENER_OPTIONS[opt]
                if st.button(label, key=f"s2_opt{i}", use_container_width=True):
                    answers[n] = opt
                    st.session_state.sim_step = 3
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    elif n == 3:
        correct = str(scenario["correct_type"]).strip()

        if n in answers:
            chosen = answers[n]
            is_ok  = chosen == correct
            msg = (config.FEEDBACK_CORRECT[n].format(type=correct) if is_ok
                   else config.FEEDBACK_WRONG[n].format(correct_type=correct))
            feedback_md(is_ok, msg)
        else:
            st.markdown('<div class="kc-option-buttons">', unsafe_allow_html=True)
            for i, opt in enumerate(config.KEIGO_TYPES):
                if st.button(opt, key=f"s3_opt{i}", use_container_width=True):
                    answers[n] = opt
                    st.session_state.sim_step = 4
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    elif n == 4:
        correct = str(scenario["correct_sentence"]).strip()
        wrongs  = [w.strip() for w in str(scenario["wrong_options"]).split("|") if w.strip()]
        options = [correct] + wrongs
        rng = random.Random(int(str(scenario["id"]).strip()))
        rng.shuffle(options)

        if n in answers:
            chosen = answers[n]
            is_ok  = chosen == correct
            msg = (config.FEEDBACK_CORRECT[n] if is_ok
                   else config.FEEDBACK_WRONG[n].format(correct_sentence=correct))
            feedback_md(is_ok, msg)
        else:
            st.markdown('<div class="kc-option-buttons">', unsafe_allow_html=True)
            for i, opt in enumerate(options):
                if st.button(opt, key=f"s4_opt{i}", use_container_width=True):
                    answers[n] = opt
                    st.session_state.sim_step = 5
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)


def render_explanation(scenario: pd.Series) -> None:
    if st.session_state.sim_step < 5:
        return
    correct = escape(str(scenario["correct_sentence"]).strip())
    text    = escape(str(scenario["explanation_en"]).strip())
    st.markdown(
        f'<div class="kc-explanation">'
        f'<div class="kc-explanation-sentence">{correct}</div>'
        f'<div class="kc-explanation-text">{text}</div>'
        f'{source_html(scenario)}'
        f'</div>',
        unsafe_allow_html=True,
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    init_state()
    scenarios = load_scenarios()
    n_total   = len(scenarios)

    # Apply situation filter from home page, if set
    filter_key = st.session_state.pop("practice_filter", None)
    if filter_key:
        match = scenarios[scenarios["situation"] == filter_key]
        if not match.empty:
            st.session_state.sim_idx = int(match.index[0])
            reset_scenario()

    idx      = st.session_state.sim_idx % n_total
    scenario = scenarios.iloc[idx]
    pose, comment = current_pose_and_comment(scenario)
    svg = belle_svg_inline()

    # Header with Belle pose
    comment_block = (
        f'<div class="kc-belle-comment">{escape(comment)}</div>'
        if comment else '<div class="kc-belle-comment"></div>'
    )
    st.markdown(
        f'<div class="kc-header">'
        f'<div class="kc-belle-wrapper {escape(pose)}">{svg}</div>'
        f'<div class="kc-header-text">'
        f'<div class="kc-title">{escape(config.APP_TITLE)}</div>'
        f'<div class="kc-subtitle">{escape(config.APP_SUBTITLE)}</div>'
        f'</div>'
        f'{comment_block}'
        f'</div>',
        unsafe_allow_html=True,
    )

    # Progress indicator
    step_display = min(st.session_state.sim_step, 4)
    st.markdown(
        f'<div class="kc-progress">'
        + config.PROGRESS_FORMAT.format(
            scenario=idx + 1, total=n_total,
            step=step_display, total_steps=4,
        )
        + '</div>',
        unsafe_allow_html=True,
    )

    # Scenario card
    situation_display = escape(str(scenario["situation"]).replace("_", " ").title())
    st.markdown(
        f'<div class="kc-scenario-card">'
        f'<div><span class="kc-situation-tag">{situation_display}</span></div>'
        f'<div class="kc-scene-en">{escape(str(scenario["scene_en"]))}</div>'
        f'<div class="kc-scene-jp kc-japanese">{escape(str(scenario["scene_jp"]))}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # Steps
    for step_n in range(1, 5):
        render_step(step_n, scenario)
    render_explanation(scenario)

    # Navigation
    st.markdown('<div class="kc-nav">', unsafe_allow_html=True)
    col_prev, col_ctr, col_next = st.columns([1, 2, 1])
    with col_prev:
        if idx > 0:
            if st.button(config.NAV_PREV_LABEL, key="nav_prev"):
                st.session_state.sim_idx = idx - 1
                reset_scenario()
                st.rerun()
    with col_ctr:
        st.markdown(
            f'<div class="kc-nav-counter">{idx + 1} / {n_total}</div>',
            unsafe_allow_html=True,
        )
    with col_next:
        if idx < n_total - 1:
            if st.button(config.NAV_NEXT_LABEL, key="nav_next"):
                st.session_state.sim_idx = idx + 1
                reset_scenario()
                st.rerun()
        elif st.session_state.sim_step >= 5:
            st.caption(config.ALL_SCENARIOS_COMPLETE)
    st.markdown('</div>', unsafe_allow_html=True)


main()
