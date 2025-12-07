# ============================================
# Singapore Airlines Data Analytics System
# Main Application Entry
# Backend Output + Frontend UI (Streamlit)
# ============================================

"""
Main entry for Singapore Airlines Analytics System.
Supports BOTH:
1. CLI mode (python3 main.py)
2. Streamlit UI mode (streamlit run main.py)
"""

import os
import logging

# Detect if running in CLI mode
CLI_MODE = __name__ == "__main__" and not os.environ.get("STREAMLIT_SERVER_PORT")

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started.")


# ---------------------------------------------------
# CLI MODE (Interactive Menu with Loop)
# ---------------------------------------------------
if CLI_MODE:

    while True:
        print("===========================================")
        print(" Singapore Airlines Analytics System (CLI) ")
        print("===========================================\n")

        print("Select an analytics module:")
        print("1. Flight Performance Analytics")
        print("2. Customer Experience Analytics")
        print("3. Risk & Scenario Simulation")
        print("4. Cloud Analytics")
        print("5. Exit System\n")

        choice = input("Enter option (1–5): ")

        if choice == "1":
            print("\n[CLI] Running Flight Performance Module...\n")
            logging.info("CLI selected: Flight Performance")
        elif choice == "2":
            print("\n[CLI] Running Customer Experience Module...\n")
            logging.info("CLI selected: Customer Experience")
        elif choice == "3":
            print("\n[CLI] Running Risk Simulation Module...\n")
            logging.info("CLI selected: Risk Simulation")
        elif choice == "4":
            print("\n[CLI] Running Cloud Analytics Module...\n")
            logging.info("CLI selected: Cloud Analytics")
        elif choice == "5":
            print("\nExiting system. Goodbye!")
            logging.info("CLI exited.")
            exit()
        else:
            print("\nInvalid option. Please enter a number from 1–5.\n")
            logging.warning(f"Invalid CLI selection: {choice}")

        # Pause before showing main menu again
        input("Press Enter to return to the main menu...\n")

    # Never runs below this (CLI exits here)
    exit()


# ---------------------------------------------------
# STREAMLIT MODE
# ---------------------------------------------------
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Singapore Airlines Analytics System",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Singapore Airlines Data Analytics System")
st.subheader("Enterprise Cloud-Based Analytics Platform")

# Logo
try:
    logo = Image.open("assets/singapore_airlines_logo.png")
    st.image(logo, width=280)
except Exception:
    st.warning("Logo not found.")

st.write("""
Welcome to the **Singapore Airlines Analytics System**, built using:

- Python  
- Streamlit Web Framework  
- Cloud Execution  
- Data-Driven Analytics  

Use the **left sidebar** to navigate between the analytics modules.
""")

st.markdown("---")

st.subheader("📊 Available Modules")

st.markdown("""
### 1. Flight Performance Analytics  
### 2. Customer Experience Analytics  
### 3. Risk & Scenario Simulation  
### 4. Cloud Analytics  
""")

st.info("Use the sidebar to switch pages.")
