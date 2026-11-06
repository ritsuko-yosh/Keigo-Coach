"""
pages/about.py - About page.
Content lives in content/about.md. Edit that file, not this one.
"""

from pathlib import Path
import streamlit as st
import config
from kc_utils import belle_header_html


def main() -> None:
    st.markdown(
        belle_header_html(subtitle=config.ABOUT_PAGE_TITLE),
        unsafe_allow_html=True,
    )
    st.markdown(Path(config.ABOUT_MD_PATH).read_text(encoding="utf-8"))


main()
