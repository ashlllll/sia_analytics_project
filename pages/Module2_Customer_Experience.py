# ============================================================
# Author: Ruitao He
# Last Updated: 2025-12-10
# Module 2: Customer Experience Analytics
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import streamlit as st

# ============================================================
# Global Visual Settings (Singapore Airlines Theme)
# ============================================================

mpl.rcParams["figure.figsize"] = (8, 4)
mpl.rcParams["figure.dpi"] = 150
sns.set(style="whitegrid")

SIA_BLUE = "#003A80"
SIA_GOLD = "#D4A037"


def apply_sia_chart_style(ax):
    """Remove gridlines and apply the clean SIA premium look."""

    # Remove all gridlines
    ax.grid(False)

    # Clean modern axes
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#BBBBBB")
    ax.spines["bottom"].set_color("#BBBBBB")

    # Remove tick marks for a cleaner look
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", colors="#333333")

    # Title formatting
    ax.title.set_fontsize(16)
    ax.title.set_fontweight("bold")


# ============================================================
# Load Dataset
# ============================================================

def load_data():
    try:
        df = pd.read_csv("assets/train.csv")
        df = df.loc[:, ~df.columns.str.contains("unnamed", case=False)]
        return df
    except Exception:
        return None


# ============================================================
# STREAMLIT UI
# ============================================================

def run_customer_experience_ui():

    from services.ui_service import apply_global_styles

    st.set_page_config(
        page_title="Customer Experience Analytics",
        page_icon="😊",
        layout="wide"
    )

    apply_global_styles()

    # ------------------------------------------------------------
    # Page Header
    # ------------------------------------------------------------
    st.title("😊 Customer Experience Analytics")
    st.markdown(
        """
        This module explores passenger satisfaction, inflight service ratings,
        and behavioural patterns across the customer journey.
        """
    )
    st.divider()

    # ------------------------------------------------------------
    # Load Data
    # ------------------------------------------------------------
    df = load_data()
    if df is None:
        st.error("❌ Unable to load dataset from assets/train.csv.")
        st.stop()

    # Standardize satisfaction to numeric score
    df["satisfaction"] = df["satisfaction"].astype(str).str.lower()
    satisfaction_map = {
        "very dissatisfied": 1,
        "dissatisfied": 2,
        "neutral": 3,
        "neutral or dissatisfied": 3,
        "neutral or satisfied": 4,
        "satisfied": 4,
        "very satisfied": 5,
    }

    df["satisfaction_score"] = df["satisfaction"].map(satisfaction_map).fillna(3)

    # ------------------------------------------------------------
    # KPI Summary
    # ------------------------------------------------------------
    c1, c2 = st.columns(2)
    c1.metric("⭐ Average Satisfaction Score", f"{df['satisfaction_score'].mean():.2f}")
    c2.metric("👥 Total Passengers", f"{len(df)}")

    st.divider()

    # ============================================================
    # Chart 1 — Satisfaction Distribution (Bar Chart)
    # ============================================================

    st.subheader("📊 Satisfaction Score Distribution")

    score_counts = df["satisfaction_score"].value_counts().sort_index()

    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.barplot(
        x=score_counts.index,
        y=score_counts.values,
        color=SIA_BLUE,
        ax=ax1
    )

    ax1.set_xlabel("Satisfaction Score (1–5)")
    ax1.set_ylabel("Passenger Count")
    ax1.set_title("Distribution of Satisfaction Scores")

    apply_sia_chart_style(ax1)
    st.pyplot(fig1)
    st.divider()

    # ============================================================
    # Chart 2 — Satisfaction by Flight Distance (Bar Chart)
    # ============================================================

    st.subheader("🧭 Impact of Flight Distance on Satisfaction")

    min_d = int(df["Flight Distance"].min())
    max_d = int(df["Flight Distance"].max())

    threshold = st.slider(
        "Minimum Flight Distance (km)",
        min_d,
        max_d,
        value=min_d + (max_d - min_d) // 3,
        step=100,
    )

    filtered = df[df["Flight Distance"] >= threshold]
    st.write(f"Passengers included: **{len(filtered)}**")

    filtered_counts = filtered["satisfaction_score"].value_counts().sort_index()

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.barplot(
        x=filtered_counts.index,
        y=filtered_counts.values,
        color=SIA_GOLD,
        ax=ax2
    )

    ax2.set_xlabel("Satisfaction Score")
    ax2.set_ylabel("Passenger Count")
    ax2.set_title("Satisfaction Levels for Long-Distance Flights")

    apply_sia_chart_style(ax2)
    st.pyplot(fig2)
    st.divider()

    # ============================================================
    # Chart 3 — Average Inflight Service Ratings
    # ============================================================

    st.subheader("🔥 Average Inflight Service Ratings")

    service_cols = [
        "Inflight wifi service",
        "Departure/Arrival time convenient",
        "Ease of Online booking",
        "Gate location",
        "Food and drink",
        "Online boarding",
        "Seat comfort",
        "Inflight entertainment",
        "On-board service",
        "Leg room service",
        "Baggage handling",
        "Checkin service",
        "Inflight service",
        "Cleanliness",
    ]

    service_scores = df[service_cols].mean().sort_values(ascending=True)

    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.barplot(
        x=service_scores.values,
        y=service_scores.index,
        palette=[SIA_BLUE if i < len(service_scores) / 2 else SIA_GOLD
                 for i in range(len(service_scores))],
        ax=ax3,
    )

    ax3.set_xlabel("Average Rating (1–5)")
    ax3.set_ylabel("Service Category")
    ax3.set_title("Passenger Evaluation of Inflight Service Attributes")

    apply_sia_chart_style(ax3)
    st.pyplot(fig3)
    st.divider()

    # Back Navigation
    st.page_link("Dashboard.py", label="⬅️ Back to Dashboard", icon="🏠")


# ============================================================
# CLI Version
# ============================================================

def run_customer_experience_cli():

    print("\n=======================================")
    print("  CUSTOMER EXPERIENCE ANALYTICS (CLI)  ")
    print("=======================================\n")

    df = load_data()
    if df is None:
        print("❌ ERROR: Dataset not found.")
        input("Press ENTER to return...")
        return

    df["satisfaction"] = df["satisfaction"].astype(str).str.lower()

    mapping = {
        "neutral or dissatisfied": 0,
        "satisfied": 1
    }

    df["satisfaction_score"] = df["satisfaction"].map(mapping).fillna(-1)

    print(f"⭐ Average Satisfaction Score: {df['satisfaction_score'].mean():.2f}\n")
    print("📊 Satisfaction Distribution:")
    print(df["satisfaction"].value_counts())

    print("\n✔ Analysis Completed.")
    input("Press ENTER to return...")


# ============================================================
# Auto-run Streamlit if page is opened directly
# ============================================================

try:
    if st.runtime.exists():
        run_customer_experience_ui()
except Exception:
    pass
