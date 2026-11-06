"""
pages/my_progress.py - My Progress placeholder.
Shows a coming-soon message. No fake data.
"""

import streamlit as st
import config
from kc_utils import belle_header_html


def main() -> None:
    st.markdown(
        belle_header_html(subtitle=config.PROGRESS_PAGE_TITLE),
        unsafe_allow_html=True,
    )
    st.info(config.MY_PROGRESS_COMING_SOON)


main()
