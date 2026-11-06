"""
pages/phrase_library.py - Phrase reference browser.
All UI text from config.py. All phrase content from data/phrases.csv.
"""

from html import escape
from pathlib import Path

import pandas as pd
import streamlit as st

import config
from kc_utils import inject_css, belle_header_html, source_html


@st.cache_data
def load_phrases() -> pd.DataFrame:
    return pd.read_csv(config.CSV_PATH, dtype=str)


def card_html(row: pd.Series, idx: int, hide_keigo: bool) -> str:
    delay        = idx * 0.06
    situation    = escape(config.SITUATION_LABELS.get(str(row["situation"]), str(row["situation"])))
    css_class    = config.KEIGO_TYPE_CSS.get(str(row["keigo_type"]), "")
    keigo_type   = escape(str(row["keigo_type"]))
    _, actor_lbl = config.ACTION_BY_LABELS.get(str(row["action_by"]), ("", str(row["action_by"])))

    unverified = (
        f'<span class="kc-unverified">{escape(config.UNVERIFIED_LABEL)}</span>'
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
        f'<div class="kc-actor"><span>{escape(actor_lbl)}</span></div>'
        f'<div class="kc-progression">'
        f'<div class="kc-step"><div class="kc-step-label">Casual</div>'
        f'<div class="kc-step-value">{escape(str(row["casual_jp"]))}</div></div>'
        f'<div class="kc-arrow">›</div>'
        f'<div class="kc-step"><div class="kc-step-label">Polite</div>'
        f'<div class="kc-step-value">{escape(str(row["polite_jp"]))}</div></div>'
        f'<div class="kc-arrow">›</div>'
        f'<div class="{keigo_step_cls}"><div class="kc-step-label">Keigo</div>'
        f'<div class="{keigo_val_cls}">{escape(str(row["keigo_jp"]))}</div></div>'
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
    df = load_phrases()

    st.markdown(
        belle_header_html(subtitle=config.LIBRARY_PAGE_TITLE),
        unsafe_allow_html=True,
    )

    with st.sidebar:
        st.header(config.FILTER_HEADING)
        sel_situation = st.selectbox(
            config.FILTER_SITUATION_LABEL,
            options=["All"] + config.SITUATIONS,
        )
        sel_keigo = st.selectbox(
            config.FILTER_KEIGO_LABEL,
            options=["All"] + config.KEIGO_TYPES,
        )
        st.divider()
        hide_keigo = st.toggle(config.HIDE_KEIGO_LABEL, value=False)

    filtered = df.copy()
    if sel_situation != "All":
        filtered = filtered[filtered["situation"] == sel_situation]
    if sel_keigo != "All":
        filtered = filtered[filtered["keigo_type"] == sel_keigo]

    st.caption(config.SHOWING_FORMAT.format(shown=len(filtered), total=len(df)))

    if filtered.empty:
        st.info(config.NO_RESULTS_MESSAGE)
        return

    cards = "".join(
        card_html(row, i, hide_keigo)
        for i, (_, row) in enumerate(filtered.iterrows())
    )
    st.markdown(f'<div class="kc-cards">{cards}</div>', unsafe_allow_html=True)


main()
