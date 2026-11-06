"""
app.py - Keigo Coach navigation hub.

Defines the five-page navigation, injects global CSS, and renders the
top tab bar. All page content lives in pages/.
"""

import streamlit as st
import config
from kc_utils import inject_css, render_top_nav

st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="🎌",
    layout="wide",
)

pg = st.navigation(
    [
        st.Page("pages/home.py",           title=config.NAV_HOME,           default=True),
        st.Page("pages/practice.py",       title=config.NAV_PRACTICE),
        st.Page("pages/phrase_library.py", title=config.NAV_PHRASE_LIBRARY),
        st.Page("pages/my_progress.py",    title=config.NAV_MY_PROGRESS),
        st.Page("pages/about.py",          title=config.NAV_ABOUT),
    ],
    position="hidden",
)

inject_css()
render_top_nav(active_title=pg.title)
pg.run()
