"""
pages/home.py - Home page.
All text comes from content/home.md and config.py.
"""

from html import escape
import streamlit as st
import config
from kc_utils import inject_css, belle_svg_inline, parse_home_md


def main() -> None:
    sections = parse_home_md()
    svg = belle_svg_inline()

    # ── Hero ──────────────────────────────────────────────────────────────
    col_belle, col_text = st.columns([1, 3], gap="medium")

    with col_belle:
        st.markdown(
            f'<div class="kc-hero-belle pose-sit">{svg}</div>',
            unsafe_allow_html=True,
        )

    with col_text:
        st.markdown(
            f'<h1 class="kc-hero-title">{escape(config.APP_TITLE)}</h1>'
            f'<div class="kc-hero-tagline">{escape(sections.get("tagline", ""))}</div>',
            unsafe_allow_html=True,
        )
        if st.button(
            sections.get("start-button", config.START_BUTTON_LABEL),
            key="home_start",
            type="primary",
        ):
            st.switch_page("pages/practice.py")

    # ── How it works ──────────────────────────────────────────────────────
    st.markdown(
        f'<h2 class="kc-section-heading">{escape(config.HOME_SECTION_HOW)}</h2>',
        unsafe_allow_html=True,
    )

    step_cols = st.columns(3, gap="small")
    steps = [
        ("step-1-label", "step-1-detail", "1"),
        ("step-2-label", "step-2-detail", "2"),
        ("step-3-label", "step-3-detail", "3"),
    ]
    for col, (label_key, detail_key, num) in zip(step_cols, steps):
        with col:
            st.markdown(
                f'<div class="kc-step-card">'
                f'<div class="kc-step-number">{num}</div>'
                f'<div class="kc-step-title">{escape(sections.get(label_key, ""))}</div>'
                f'<div class="kc-step-desc">{escape(sections.get(detail_key, ""))}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    # ── Choose a situation ────────────────────────────────────────────────
    st.markdown(
        f'<h2 class="kc-section-heading">{escape(config.HOME_SECTION_SITUATIONS)}</h2>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="kc-situation-buttons">', unsafe_allow_html=True)
    sit_cols = st.columns(len(config.SITUATION_CARDS), gap="small")
    for col, (sit_key, sit_label) in zip(sit_cols, config.SITUATION_CARDS):
        desc = sections.get(f"situation-card-{sit_key}", "")
        with col:
            btn_label = sit_label + ("\n" + desc if desc else "")
            if st.button(btn_label, key=f"sit_{sit_key}", use_container_width=True):
                st.session_state["practice_filter"] = sit_key
                st.switch_page("pages/practice.py")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Why keigo is hard ─────────────────────────────────────────────────
    why_title = sections.get("why-keigo-hard-title", "")
    why_text  = sections.get("why-keigo-hard", "")

    if why_title or why_text:
        st.markdown(
            f'<div class="kc-why-section">'
            f'<div class="kc-why-title">{escape(why_title)}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        if why_text:
            st.markdown(why_text)


main()
