# ============================================================
# Author: Philippe Bolduan
# Module: Risk & Scenario Simulation
# Course: CN6001 Enterprise Application & Cloud Computing
#
# Description:
# This module simulates operational risk and uncertainty in airline
# operations using Monte Carlo–based techniques. Due to the
# confidentiality of real airline operational risk data, a synthetic
# dataset (train.csv) is used for academic demonstration purposes.
#
# Key Concepts:
# - Monte Carlo simulation for delay risk modelling
# - Scenario-based disruption modelling (crisis multiplier)
# - Streamlit UI execution
# ============================================================

import numpy as np
import pandas as pd
import streamlit as st


def _safe_apply_global_styles():
    """Apply shared UI theme if available."""
    try:
        from services.ui_service import apply_global_styles
        apply_global_styles()
    except Exception:
        pass


def _inject_module_css():
    """Inject module-level styling aligned with the global theme."""
    st.markdown(
        """
        <style>
        .back-row {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1rem;
            margin-bottom: 1.2rem;
        }
        .back-row a {
            text-decoration: none;
            font-weight: 600;
            color: #002663;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _kpi_card(title: str, value: str, badge: str):
    """Render a KPI card."""
    st.markdown(
        f"""
        <div style="
            background:#FFFFFF;
            border-radius:16px;
            padding:16px;
            box-shadow:0 2px 10px rgba(0,0,0,0.08);
        ">
            <div style="color:#555;font-size:0.9rem;font-weight:600">{title}</div>
            <div style="color:#002663;font-size:2.2rem;font-weight:800">{value}</div>
            <div style="
                display:inline-block;
                margin-top:8px;
                padding:4px 10px;
                border-radius:999px;
                background:#FFF3B0;
                color:#002663;
                font-size:0.75rem;
                font-weight:700;
            ">{badge}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def simulate_delay_monte_carlo(mean_delay: float, std_delay: float, n: int, crisis_multiplier: float) -> np.ndarray:
    """
    Monte Carlo simulation of departure delays:
    - Normal distribution based on dataset mean/std
    - Clipped to 0 (no negative delays)
    - Scaled by crisis_multiplier for disruption scenarios
    """
    delays = np.random.normal(mean_delay, std_delay, n)
    delays = np.clip(delays, 0, None)
    return delays * crisis_multiplier


def calculate_kpis(delays: np.ndarray, threshold: float) -> dict:
    """Compute risk indicators from simulated delays."""
    return {
        "expected": float(np.mean(delays)),
        "probability": float(np.mean(delays > threshold) * 100),
        "p95": float(np.percentile(delays, 95)),
        "worst": float(np.max(delays)),
    }


def run_streamlit():
    from services.data_service import load_data

    _safe_apply_global_styles()
    _inject_module_css()

    st.markdown(
        """
        <div class="back-row">
            🏠 <a href="/" target="_self">Back to Dashboard</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.title("⚠️ Risk & Scenario Simulation")
    st.caption(
        "This module models operational uncertainty using Monte Carlo simulation and scenario-based risk modelling."
    )

    df = load_data()

    delay_col = "Departure Delay in Minutes"
    if delay_col not in df.columns:
        st.error("Required delay column not found in dataset.")
        return

    delays_data = pd.to_numeric(df[delay_col], errors="coerce").dropna()
    mean_delay = float(delays_data.mean())
    std_delay = float(delays_data.std()) if float(delays_data.std()) > 0 else 10.0

    st.subheader("🎛️ Scenario Controls")
    c1, c2, c3 = st.columns(3)

    with c1:
        simulations = st.slider("Monte Carlo simulations", 2000, 50000, 12000, 2000)
    with c2:
        threshold = st.slider("Delay risk threshold (min)", 15, 180, 60, 5)
    with c3:
        crisis = st.slider("Crisis multiplier", 1.0, 2.5, 1.15, 0.05)

    simulated = simulate_delay_monte_carlo(mean_delay, std_delay, simulations, crisis)
    kpis = calculate_kpis(simulated, threshold)

    st.subheader("⭐ Key Risk Indicators")
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        _kpi_card("Expected Delay (min)", f"{kpis['expected']:.1f}", f"Baseline μ={mean_delay:.1f}")
    with k2:
        _kpi_card(f"P(Delay > {threshold}m)", f"{kpis['probability']:.1f}%", "Operational risk")
    with k3:
        _kpi_card("95th Percentile", f"{kpis['p95']:.1f}", "Resilience KPI")
    with k4:
        _kpi_card("Worst Case", f"{kpis['worst']:.1f}", "Tail risk")

    st.subheader("📊 Simulated Delay Distribution")
    bins = np.arange(0, int(max(180, np.percentile(simulated, 99) + 30)) + 5, 5)
    hist, edges = np.histogram(simulated, bins=bins)
    hist_df = pd.DataFrame({"Delay (min)": edges[:-1], "Count": hist}).set_index("Delay (min)")
    st.bar_chart(hist_df)


def run_cli():
    """CLI entry point for lightweight non-visual demonstration."""
    from services.data_service import load_data

    print("\n--- Risk & Scenario Simulation (CLI) ---")

    df = load_data()

    delay_col = "Departure Delay in Minutes"
    if delay_col not in df.columns:
        print("ERROR: Required delay column not found in dataset.")
        return

    delays_data = pd.to_numeric(df[delay_col], errors="coerce").dropna()
    mean_delay = float(delays_data.mean())
    std_delay = float(delays_data.std()) if float(delays_data.std()) > 0 else 10.0

    simulations = 12000
    threshold = 60
    crisis = 1.15

    simulated = simulate_delay_monte_carlo(mean_delay, std_delay, simulations, crisis)
    kpis = calculate_kpis(simulated, threshold)

    print(f"Baseline mean delay: {mean_delay:.2f} min | std: {std_delay:.2f} min")
    print(f"Simulations: {simulations} | Crisis multiplier: {crisis:.2f}")
    print(f"Expected delay: {kpis['expected']:.2f} min")
    print(f"P(Delay > {threshold} min): {kpis['probability']:.2f}%")
    print(f"95th percentile: {kpis['p95']:.2f} min")
    print(f"Worst case: {kpis['worst']:.2f} min")


def main(mode="streamlit"):
    if mode == "cli":
        run_cli()
    else:
        run_streamlit()


if __name__ == "__main__":
    main()
