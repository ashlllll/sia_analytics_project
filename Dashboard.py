# ============================================
# Author: Qian Zhu
# Date: 2023-08-22
# Singapore Airlines Analytics System
# Dashboard (Home Page) + CLI
# ============================================

import sys
import logging

logging.basicConfig(level=logging.INFO)


# =============================================================
# STREAMLIT UI MODE
# =============================================================
def run_streamlit_ui():

    import streamlit as st
    from services.ui_service import apply_global_styles

    st.set_page_config(
        page_title="SIA Dashboard",
        page_icon="🏠",
        layout="wide"
    )

    apply_global_styles()

    # ======================
    # HERO SECTION
    # ======================
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #001A4D 0%, #003A80 100%);
            padding: 3.8rem;
            border-radius: 20px;
            margin-bottom: 2.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        ">
            <h1 style="
                font-size: 3.4rem;
                font-weight: 900;
                letter-spacing: -1px;
                margin-bottom: 0.5rem;
                text-shadow: 0 0 10px rgba(0,0,0,0.5);
            ">
                Singapore Airlines Analytics System
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ======================
    # MODULES
    # ======================
    st.markdown("<h2>📊 Analytics Modules</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    module_card = lambda title, desc, link: st.markdown(
        f"""
        <a href="/{link}" target="_self" style="text-decoration:none;">
            <div class="sia-card">
                <div class="sia-card-title">{title}</div>
                <div class="sia-card-desc">{desc}</div>
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

    with col1:
        module_card("✈️ Flight Performance Analytics",
                    "Fuel efficiency, delays, crew performance, aircraft usage.",
                    "pages/Module1_Flight_Performance.py")

        module_card("⚠️ Risk & Scenario Simulation",
                    "Monte-Carlo models, disruption impacts, scenario forecasting.",
                    "pages/Module3_Risk_Simulation.py")

    with col2:
        module_card("😊 Customer Experience Analytics",
                    "Satisfaction, service, inflight behavior trends.",
                    "pages/Module2_Customer_Experience.py")

        module_card("☁️ Cloud Analytics",
                    "Real-time cloud processing & distributed data pipelines.",
                    "pages/Module4_Cloud_Analytics.py")

    st.info("Use the sidebar or click any module card to navigate.")


# =============================================================
# CLI MODE
# =============================================================
def run_cli():

    from pages.Module2_Customer_Experience import run_customer_experience_cli

    print("===========================================")
    print("   Singapore Airlines Analytics System CLI")
    print("===========================================")

    while True:
        print("\n1. Flight Performance")
        print("2. Customer Experience")
        print("3. Risk Simulation")
        print("4. Cloud Analytics")
        print("5. Exit\n")

        choice = input("Enter option (1–5): ")

        if choice == "2":
            run_customer_experience_cli()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Module not implemented yet.")


# =============================================================
# ENTRY POINT
# =============================================================
if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        run_cli()
    else:
        run_streamlit_ui()
