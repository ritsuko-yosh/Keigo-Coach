"""
pages/2_About.py - About page.
Content lives in content/about.md — edit that file, not this one.
"""

from pathlib import Path
import streamlit as st
import config
from kc_utils import inject_css, belle_header_html

st.set_page_config(
    page_title=config.ABOUT_PAGE_TITLE,
    page_icon="ℹ️",
    layout="wide",
)


def main() -> None:
    inject_css()
    st.markdown(belle_header_html(subtitle="About this project"), unsafe_allow_html=True)
    st.markdown(Path(config.ABOUT_MD_PATH).read_text(encoding="utf-8"))


main()
