# ============================================================
# ui_service.py – Singapore Airlines Inspired Global UI Theme
# ============================================================
import streamlit as st

PRIMARY_NAVY = "#002663"
ACCENT_GOLD = "#FFED4D"
BACKGROUND_CREAM = "#F5F3EE"
TEXT_GREY = "#555555"

CARD_BG = "#FFFFFF"
CARD_BORDER = "#E5E7EB"

def apply_global_styles():
    st.markdown(
        f"""
<style>

.stApp {{
    background-color: {BACKGROUND_CREAM} !important;
}}

.block-container {{
    padding-top: 2rem;
    padding-bottom: 3rem;
    padding-left: 3rem;
    padding-right: 3rem;
}}

h1, h2, h3 {{
    color: {PRIMARY_NAVY} !important;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
}}

h4, h5 {{
    color: {PRIMARY_NAVY} !important;
    font-weight: 700 !important;
}}

p, li {{
    color: {TEXT_GREY} !important;
    font-size: 1.05rem;
}}

.sia-card {{
    background: {CARD_BG};
    padding: 1.3rem 1.6rem;
    border-radius: 14px;
    border: 1px solid {CARD_BORDER};
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    transition: 0.2s ease-in-out;
}}

.sia-card:hover {{
    transform: scale(1.02);
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    cursor: pointer;
}}

.sia-card-title {{
    color: {PRIMARY_NAVY};
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
}}

.sia-card-desc {{
    color: {TEXT_GREY};
    font-size: 0.93rem;
    line-height: 1.35;
}}

[data-testid="stMetricValue"] {{
    color: {PRIMARY_NAVY} !important;
    font-weight: 800 !important;
}}

.stButton > button {{
    background-color: {PRIMARY_NAVY};
    color: white;
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    border: none;
}}

.stButton > button:hover {{
    background-color: {ACCENT_GOLD};
    color: black !important;
}}

section[data-testid="stSidebar"] {{
    background-color: {PRIMARY_NAVY} !important;
    border-right: 1px solid {CARD_BORDER};
}}

</style>
        """,
        unsafe_allow_html=True,
    )

def render_section_title(title: str, icon: str = "📌"):
    st.markdown(f"<h2>{icon} {title}</h2>", unsafe_allow_html=True)
    st.markdown("---")

def render_kpi_cards(metrics: dict):
    cols = st.columns(len(metrics))
    for idx, (label, value) in enumerate(metrics.items()):
        with cols[idx]:
            st.markdown(
                f"""
<div class="sia-card">
    <div class="sia-card-title" style="font-size:2rem;">{value}</div>
    <div class="sia-card-desc">{label}</div>
</div>
                """,
                unsafe_allow_html=True,
            )

def render_chart(fig, use_full_width=False):
    fig.tight_layout()
    st.pyplot(fig, clear_figure=True, use_container_width=use_full_width)
