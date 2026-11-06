"""
pages/1_Phrase_Library.py - Phrase reference browser.
"""

import base64
from html import escape
from pathlib import Path

import pandas as pd
import streamlit as st

import config
from kc_utils import inject_css, belle_header_html

st.set_page_config(
    page_title=config.LIBRARY_PAGE_TITLE,
    page_icon="📚",
    layout="wide",
)


@st.cache_data
def load_phrases() -> pd.DataFrame:
    return pd.read_csv(config.CSV_PATH, dtype=str)


def source_html(row: pd.Series) -> str:
    url = str(row.get("source_url", "")).strip()
    src = str(row.get("source", "")).strip()
    url = "" if url in ("nan", "") else url
    src = "" if src in ("nan", "") else src
    if url:
        label = escape(src) if src and src != "needs review" else escape(url)
        return f'<div class="kc-source">📚 <a href="{escape(url)}" target="_blank" rel="noopener">{label}</a></div>'
    return f'<div class="kc-source kc-source-needed">📚 {config.SOURCE_NEEDED_LABEL}</div>'


def card_html(row: pd.Series, idx: int, hide_keigo: bool) -> str:
    delay = idx * 0.06
    situation = escape(config.SITUATION_LABELS.get(str(row["situation"]), str(row["situation"])))
    css_class = config.KEIGO_TYPE_CSS.get(str(row["keigo_type"]), "")
    keigo_type = escape(str(row["keigo_type"]))
    _, actor_label = config.ACTION_BY_LABELS.get(str(row["action_by"]), ("", str(row["action_by"])))

    unverified = (
        f'<span class="kc-unverified">{config.UNVERIFIED_LABEL}</span>'
        if str(row["verified"]).strip().lower() == "false"
        else ""
    )

    keigo_step_cls = "kc-step kc-step-keigo" + (" kc-hidden" if hide_keigo else "")
    keigo_val_cls  = "kc-step-value" + ("" if hide_keigo else " kc-keigo-reveal")

    return (
        f'<div class="kc-card" style="animation-delay:{delay:.2f}s">'
        f'<div class="kc-card-header">'
        f'<span class="kc-situation">{situation}</span>'
        f'<span class="kc-badge {css_class}">{keigo_type}</span>'
        f'{unverified}'
        f'</div>'
        f'<div class="kc-actor"><span>{escape(actor_label)}</span></div>'
        f'<div class="kc-progression">'
        f'<div class="kc-step">'
        f'<div class="kc-step-label">Casual</div>'
        f'<div class="kc-step-value">{escape(str(row["casual_jp"]))}</div>'
        f'</div>'
        f'<div class="kc-arrow">›</div>'
        f'<div class="kc-step">'
        f'<div class="kc-step-label">Polite</div>'
        f'<div class="kc-step-value">{escape(str(row["polite_jp"]))}</div>'
        f'</div>'
        f'<div class="kc-arrow">›</div>'
        f'<div class="{keigo_step_cls}">'
        f'<div class="kc-step-label">Keigo</div>'
        f'<div class="{keigo_val_cls}">{escape(str(row["keigo_jp"]))}</div>'
        f'</div>'
        f'</div>'
        f'<div class="kc-details">'
        f'<div class="kc-meaning">{escape(str(row["english_meaning"]))}</div>'
        f'<div class="kc-rule">{escape(str(row["explanation_rule"]))}</div>'
        f'<div class="kc-example">{escape(str(row["explanation_example"]))}</div>'
        f'{source_html(row)}'
        f'</div>'
        f'</div>'
    )


def main() -> None:
    inject_css()
    df = load_phrases()

    st.markdown(
        belle_header_html(subtitle="Phrase reference library"),
        unsafe_allow_html=True,
    )

    st.sidebar.header(config.FILTER_HEADING)
    sel_situation = st.sidebar.selectbox(
        config.FILTER_SITUATION_LABEL,
        options=["All"] + config.SITUATIONS,
    )
    sel_keigo = st.sidebar.selectbox(
        config.FILTER_KEIGO_LABEL,
        options=["All"] + config.KEIGO_TYPES,
    )
    st.sidebar.divider()
    hide_keigo = st.sidebar.toggle(config.HIDE_KEIGO_LABEL, value=False)

    filtered = df.copy()
    if sel_situation != "All":
        filtered = filtered[filtered["situation"] == sel_situation]
    if sel_keigo != "All":
        filtered = filtered[filtered["keigo_type"] == sel_keigo]

    st.caption(f"Showing {len(filtered)} of {len(df)} phrases")

    if filtered.empty:
        st.info(config.NO_RESULTS_MESSAGE)
        return

    cards = "".join(
        card_html(row, i, hide_keigo)
        for i, (_, row) in enumerate(filtered.iterrows())
    )
    st.markdown(f'<div class="kc-cards">{cards}</div>', unsafe_allow_html=True)


main()
