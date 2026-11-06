"""
kc_utils.py - Shared utilities for all Keigo Coach pages.
CSS injection, Belle header rendering, top nav, and home.md parsing.
"""

from html import escape
from pathlib import Path

import streamlit as st

import config


def inject_css() -> None:
    """Inject style.css and belle_poses.css into the page."""
    css = Path(config.CSS_PATH).read_text(encoding="utf-8")
    belle_css = Path(config.BELLE_POSES_CSS_PATH).read_text(encoding="utf-8")
    st.markdown(f"<style>{css}\n{belle_css}</style>", unsafe_allow_html=True)


def belle_svg_inline() -> str:
    """Return belle_sit.svg normalised to a single line.
    Single-line prevents Streamlit's markdown parser from treating
    SVG lines that begin with 4+ spaces as code blocks."""
    raw = Path(config.BELLE_SVG_PATH).read_text(encoding="utf-8")
    return " ".join(raw.split())


def belle_header_html(
    pose: str = "pose-sit",
    comment: str = "",
    subtitle: str = "",
) -> str:
    """Build the compact page header: Belle + title + subtitle + comment."""
    svg = belle_svg_inline()
    sub = subtitle or config.APP_SUBTITLE
    comment_block = (
        f'<div class="kc-belle-comment">{escape(comment)}</div>'
        if comment
        else '<div class="kc-belle-comment"></div>'
    )
    return (
        f'<div class="kc-header">'
        f'<div class="kc-belle-wrapper {escape(pose)}">{svg}</div>'
        f'<div class="kc-header-text">'
        f'<div class="kc-title">{escape(config.APP_TITLE)}</div>'
        f'<div class="kc-subtitle">{escape(sub)}</div>'
        f'</div>'
        f'{comment_block}'
        f'</div>'
    )


def render_top_nav(active_title: str = "") -> None:
    """Render the horizontal tab bar across the top of every page.
    Uses st.page_link for inactive tabs (clickable navigation links) and
    a plain styled span for the active tab (current page)."""
    st.markdown('<div class="kc-topnav">', unsafe_allow_html=True)
    cols = st.columns(len(config.NAV_PAGES))
    for col, (path, label) in zip(cols, config.NAV_PAGES):
        with col:
            if label == active_title:
                # Active tab: render as styled text, not a link
                st.markdown(
                    f'<div class="kc-nav-tab-active">{escape(label)}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.page_link(path, label=label, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


def parse_home_md() -> dict:
    """Read content/home.md and split it into sections by ## heading.
    Returns a dict where keys are the heading text and values are
    the content below each heading (stripped of whitespace)."""
    raw = Path(config.HOME_MD_PATH).read_text(encoding="utf-8")
    sections: dict = {}
    current_key = None
    buf: list = []
    for line in raw.splitlines():
        if line.startswith("## "):
            if current_key is not None:
                sections[current_key] = "\n".join(buf).strip()
            current_key = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    if current_key is not None:
        sections[current_key] = "\n".join(buf).strip()
    return sections


def source_html(row) -> str:
    """Return a source citation link or a 'Source needed' notice."""
    url = str(row.get("source_url", "")).strip()
    src = str(row.get("source", "")).strip()
    url = "" if url in ("nan", "") else url
    src = "" if src in ("nan", "") else src
    if url:
        label = escape(src) if src and src != "needs review" else escape(url)
        return (
            f'<div class="kc-source">'
            f'📚 <a href="{escape(url)}" target="_blank" rel="noopener">{label}</a>'
            f'</div>'
        )
    return f'<div class="kc-source kc-source-needed">📚 {config.SOURCE_NEEDED_LABEL}</div>'
