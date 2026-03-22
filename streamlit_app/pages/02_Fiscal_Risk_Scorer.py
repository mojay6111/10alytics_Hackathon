import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib, os

st.set_page_config(page_title="Fiscal Risk Scorer · African Fiscal Intelligence",
                   page_icon="⚠️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');
:root { --bg:#0a0e1a; --surface:#111827; --border:#1e2d45; --gold:#c9a84c;
        --red:#e05252; --amber:#e08c2e; --green:#3db87a; --text:#e8eaf0; --muted:#8892a4; }
html, body, [data-testid="stAppViewContainer"] { background:var(--bg) !important; color:var(--text) !important; font-family:'DM Sans',sans-serif !important; }
[data-testid="stSidebar"] { background:#111827 !important; border-right:1px solid var(--border) !important; }
[data-testid="stSidebar"] * { color:var(--text) !important; }
h1,h2,h3 { font-family:'Playfair Display',serif !important; color:var(--gold) !important; }
.stSlider > div > div { color:var(--text) !important; }
#MainMenu, footer, header { visibility:hidden; }
</style>""", unsafe_allow_html=True)

st.markdown("## ⚠️ Fiscal Risk Scorer")
st.markdown("<p style='color:#8892a4;'>Enter a country's macroeconomic indicators to receive an AI-powered fiscal risk assessment.</p>", unsafe_allow_html=True)

# ── Preset country profiles (based on actual data) ───────────────────────────
PRESETS = {
    "— Custom —":       dict(revenue=0,   expenditure=0,   gdp_growth=0,   inflation=0,  unemployment=0,  tax_revenue=0,   capex=0,   health_exp=0),
    "Nigeria (2023)":   dict(revenue=1.2e7,expenditure=2.1e7,gdp_growth=2.3,inflation=24.5,unemployment=5.0,tax_revenue=3.5e6, capex=1.2e6,health_exp=8.2e5),
    "South Africa":     dict(revenue=2.1e6,expenditure=2.4e6,gdp_growth=0.7,inflation=6.1, unemployment=32.9,tax_revenue=1.9e6,capex=1.4e5,health_exp=2.4e5),
    "Ghana":            dict(revenue=8.5e4,expenditure=1.2e5,gdp_growth=2.9,inflation=23.2,unemployment=13.4,tax_revenue=5.8e4,capex=1.2e4,health_exp=4.2e3),
    "Kenya":            dict(revenue=2.8e5,expenditure=3.5e5,gdp_growth=5.6,inflation=6.8, unemployment=5.5, tax_revenue=2.2e5,capex=3.5e4,health_exp=2.1e4),
    "Egypt":            dict(revenue=8.5e5,expenditure=1.2e6,gdp_growth=3.8,inflation=33.9,unemployment=7.4, tax_revenue=6.4e5,capex=1.8e5,health_exp=9.5e4),
}

# ── Layout ────────────────────────────────────────────────────────────────────
left, right = st.columns([1, 1], gap="large")

with left:
    st.markdown("### Input Indicators")

    preset = st.selectbox("Load a preset country profile", list(PRESETS.keys()))
    p = PRESETS[preset]

    revenue      = st.number_input("Revenue (local currency units)", value=float(p["revenue"]),      format="%.0f")
    expenditure  = st.number_input("Expenditure (local currency units)", value=float(p["expenditure"]), format="%.0f")
    gdp_growth   = st.slider("GDP Growth Rate (%)", -15.0, 20.0, float(p["gdp_growth"]), 0.1)
    inflation    = st.slider("Inflation Rate (%)", 0.0, 100.0, float(p["inflation"]), 0.5)
    unemployment = st.slider("Unemployment Rate (%)", 0.0, 60.0, float(p["unemployment"]), 0.5)
    tax_revenue  = st.number_input("Tax Revenue", value=float(p["tax_revenue"]), format="%.0f")
    capex        = st.number_input("Capital Expenditure", value=float(p["capex"]), format="%.0f")
    health_exp   = st.number_input("Health Expenditure", value=float(p["health_exp"]), format="%.0f")

with right:
    st.markdown("### Risk Assessment")

    features = np.array([[revenue, expenditure, gdp_growth, inflation,
                          unemployment, tax_revenue, capex, health_exp]])

    # ── Rule-based scoring (when model not available) ─────────────────────────
    score = 0
    reasons = []

    if expenditure > 0 and revenue > 0:
        deficit_ratio = (expenditure - revenue) / max(revenue, 1)
        if deficit_ratio > 0.3:
            score += 35
            reasons.append(("🔴", f"Expenditure exceeds revenue by {deficit_ratio:.0%}"))
        elif deficit_ratio > 0.1:
            score += 20
            reasons.append(("🟡", f"Moderate deficit — expenditure {deficit_ratio:.0%} above revenue"))
        else:
            reasons.append(("🟢", "Revenue-expenditure balance is healthy"))

    if inflation > 20:
        score += 30
        reasons.append(("🔴", f"Hyperinflationary pressure at {inflation:.1f}%"))
    elif inflation > 10:
        score += 18
        reasons.append(("🟡", f"Elevated inflation at {inflation:.1f}% — above 10% threshold"))
    else:
        reasons.append(("🟢", f"Inflation contained at {inflation:.1f}%"))

    if gdp_growth < 0:
        score += 25
        reasons.append(("🔴", f"GDP contraction at {gdp_growth:.1f}% — recession territory"))
    elif gdp_growth < 2:
        score += 12
        reasons.append(("🟡", f"Sluggish growth at {gdp_growth:.1f}% — below 2% threshold"))
    else:
        reasons.append(("🟢", f"Solid GDP growth at {gdp_growth:.1f}%"))

    if unemployment > 25:
        score += 10
        reasons.append(("🔴", f"Critical unemployment at {unemployment:.1f}%"))
    elif unemployment > 15:
        score += 6
        reasons.append(("🟡", f"High unemployment at {unemployment:.1f}%"))
    else:
        reasons.append(("🟢", f"Unemployment at {unemployment:.1f}%"))

    score = min(score, 100)

    # Risk label
    if score >= 60:
        risk_label = "🔴 HIGH RISK"
        risk_color = "#e05252"
        risk_bg    = "rgba(224,82,82,0.1)"
        risk_desc  = "This economy shows critical fiscal stress indicators. Immediate policy intervention is recommended."
    elif score >= 30:
        risk_label = "🟡 MODERATE RISK"
        risk_color = "#e08c2e"
        risk_bg    = "rgba(224,140,46,0.1)"
        risk_desc  = "Structural vulnerabilities present. Proactive fiscal consolidation advised."
    else:
        risk_label = "🟢 LOW RISK"
        risk_color = "#3db87a"
        risk_bg    = "rgba(61,184,122,0.1)"
        risk_desc  = "Fiscal fundamentals are relatively stable. Focus on maintaining discipline."

    # ── Risk Score Gauge ──────────────────────────────────────────────────────
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Fiscal Stress Score", "font": {"size": 16, "color": "#c9a84c",
                                                        "family": "Playfair Display"}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "#8892a4"},
            "bar":  {"color": risk_color},
            "bgcolor": "#111827",
            "bordercolor": "#1e2d45",
            "steps": [
                {"range": [0,  30], "color": "rgba(61,184,122,0.15)"},
                {"range": [30, 60], "color": "rgba(224,140,46,0.15)"},
                {"range": [60,100], "color": "rgba(224,82,82,0.15)"},
            ],
            "threshold": {"line": {"color": "#c9a84c", "width": 2}, "value": score}
        },
        number={"font": {"color": risk_color, "size": 40, "family": "Playfair Display"},
                "suffix": "/100"}
    ))
    fig_gauge.update_layout(
        paper_bgcolor="#0a0e1a", font_color="#e8eaf0",
        height=280, margin=dict(t=40, b=20, l=30, r=30)
    )
    st.plotly_chart(fig_gauge, use_container_width=True)

    # Risk label banner
    st.markdown(f"""
    <div style="background:{risk_bg}; border:1px solid {risk_color}; border-radius:8px;
                padding:1rem 1.5rem; text-align:center; margin-bottom:1rem;">
        <div style="font-size:1.4rem; font-weight:700; color:{risk_color};
                    font-family:'Playfair Display',serif;">{risk_label}</div>
        <div style="color:#8892a4; font-size:0.88rem; margin-top:0.4rem;">{risk_desc}</div>
    </div>""", unsafe_allow_html=True)

    # ── Signal Breakdown ──────────────────────────────────────────────────────
    st.markdown("**Signal Breakdown**")
    for icon, msg in reasons:
        color = "#e05252" if icon == "🔴" else "#e08c2e" if icon == "🟡" else "#3db87a"
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:0.6rem; padding:0.5rem 0;
                    border-bottom:1px solid #1e2d45;">
            <span style="font-size:1rem;">{icon}</span>
            <span style="color:#e8eaf0; font-size:0.88rem;">{msg}</span>
        </div>""", unsafe_allow_html=True)

# ── SDG Mapping ───────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### SDG Alignment")

sdg_map = {
    "🔴 HIGH RISK":      [("SDG 1","No Poverty","#e05252"),      ("SDG 8","Decent Work","#e05252"),   ("SDG 10","Reduced Inequalities","#e05252")],
    "🟡 MODERATE RISK":  [("SDG 8","Decent Work","#e08c2e"),     ("SDG 9","Industry & Innovation","#e08c2e"), ("SDG 17","Partnerships","#e08c2e")],
    "🟢 LOW RISK":       [("SDG 3","Good Health","#3db87a"),      ("SDG 4","Quality Education","#3db87a"),     ("SDG 13","Climate Action","#3db87a")],
}

sdgs = sdg_map.get(risk_label, [])
cols = st.columns(len(sdgs))
for col, (num, name, color) in zip(cols, sdgs):
    with col:
        st.markdown(f"""
        <div style="background:#111827; border:1px solid {color}; border-radius:8px;
                    padding:1rem; text-align:center;">
            <div style="color:{color}; font-weight:700; font-family:'DM Mono',monospace;
                        font-size:0.9rem;">{num}</div>
            <div style="color:#e8eaf0; font-size:0.85rem; margin-top:0.3rem;">{name}</div>
        </div>""", unsafe_allow_html=True)
