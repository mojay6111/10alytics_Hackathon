import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="GDP Forecasts · African Fiscal Intelligence",
                   page_icon="📈", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');
:root { --bg:#0a0e1a; --surface:#111827; --border:#1e2d45; --gold:#c9a84c;
        --red:#e05252; --amber:#e08c2e; --green:#3db87a; --text:#e8eaf0; --muted:#8892a4; }
html, body, [data-testid="stAppViewContainer"] { background:var(--bg) !important; color:var(--text) !important; font-family:'DM Sans',sans-serif !important; }
[data-testid="stSidebar"] { background:#111827 !important; border-right:1px solid var(--border) !important; }
[data-testid="stSidebar"] * { color:var(--text) !important; }
h1,h2,h3 { font-family:'Playfair Display',serif !important; color:var(--gold) !important; }
#MainMenu, footer, header { visibility:hidden; }
</style>""", unsafe_allow_html=True)

st.markdown("## 📈 GDP Growth Rate Forecasts")
st.markdown("<p style='color:#8892a4;'>5-year ahead forecasts using Facebook Prophet time-series model. Shaded bands show 95% confidence intervals.</p>", unsafe_allow_html=True)

# ── Forecast Data (from notebook outputs) ────────────────────────────────────
FORECAST_DATA = {
    "Nigeria": {
        "actual": {1990:8.0,1995:0.3,2000:5.0,2003:10.3,2004:33.7,2005:3.4,2006:8.2,2007:6.8,
                   2008:6.3,2009:6.9,2010:7.8,2011:5.3,2012:4.3,2013:6.7,2014:6.3,2015:2.7,
                   2016:-1.6,2017:0.8,2018:1.9,2019:2.2,2020:-1.9,2021:3.6,2022:3.1,2023:2.3,2024:2.9},
        "forecast": {2026:1.92, 2027:1.72, 2028:1.52, 2029:1.33},
        "lower":    {2026:-5.06,2027:-5.52,2028:-5.75,2029:-5.59},
        "upper":    {2026:9.12, 2027:8.93, 2028:8.98, 2029:9.17},
        "color": "#e05252"
    },
    "South Africa": {
        "actual": {1994:3.2,1995:3.1,1996:4.3,1997:2.6,1998:0.5,1999:2.4,2000:4.2,2001:2.7,
                   2002:3.7,2003:2.9,2004:4.5,2005:5.3,2006:5.6,2007:5.4,2008:3.2,2009:-1.5,
                   2010:3.0,2011:3.3,2012:2.2,2013:2.5,2014:1.9,2015:1.3,2016:0.7,2017:1.4,
                   2018:0.8,2019:0.1,2020:-6.3,2021:4.9,2022:1.9,2023:0.7,2024:0.6},
        "forecast": {2026:0.04,  2027:-0.12, 2028:-0.27, 2029:-0.42},
        "lower":    {2026:-2.72, 2027:-3.08, 2028:-3.16, 2029:-3.23},
        "upper":    {2026:2.91,  2027:2.80,  2028:2.72,  2029:2.53},
        "color": "#f5a623"
    },
    "Ghana": {
        "actual": {1990:3.3,1995:4.1,2000:3.7,2005:5.9,2006:6.4,2007:6.5,2008:9.1,2009:4.8,
                   2010:7.9,2011:14.0,2012:9.3,2013:7.3,2014:2.9,2015:3.8,2016:3.4,2017:8.1,
                   2018:6.3,2019:6.5,2020:0.5,2021:5.4,2022:3.1,2023:2.9,2024:4.7},
        "forecast": {2026:4.31, 2027:4.14, 2028:3.97, 2029:3.80},
        "lower":    {2026:-2.50,2027:-2.07,2028:-1.81,2029:-2.08},
        "upper":    {2026:10.39,2027:10.47,2028:10.23,2029:9.90},
        "color": "#3db87a"
    },
    "Egypt": {
        "actual": {1990:5.7,1995:4.6,2000:5.4,2005:4.5,2006:6.8,2007:7.1,2008:7.2,2009:4.7,
                   2010:5.1,2011:1.8,2012:2.2,2013:2.1,2014:2.9,2015:4.4,2016:4.3,2017:4.2,
                   2018:5.3,2019:5.6,2020:3.6,2021:3.3,2022:6.6,2023:3.8,2024:2.4},
        "forecast": {2026:3.58, 2027:3.54, 2028:3.51, 2029:3.47},
        "lower":    {2026:-0.40,2027:-0.36,2028:-0.54,2029:-0.77},
        "upper":    {2026:7.84, 2027:7.55, 2028:7.38, 2029:7.51},
        "color": "#a78bfa"
    },
    "Kenya": {
        "actual": {1990:4.2,1995:4.4,2000:0.6,2005:5.9,2006:6.3,2007:6.8,2008:1.5,2009:2.7,
                   2010:8.4,2011:6.1,2012:4.6,2013:5.9,2014:5.4,2015:5.7,2016:5.9,2017:4.9,
                   2018:6.3,2019:5.4,2020:-0.3,2021:7.6,2022:4.8,2023:5.6,2024:4.6},
        "forecast": {2026:5.74, 2027:5.81, 2028:5.88, 2029:5.95},
        "lower":    {2026:2.31, 2027:2.18, 2028:2.02, 2029:1.89},
        "upper":    {2026:9.07, 2027:9.44, 2028:9.74, 2029:10.01},
        "color": "#38bdf8"
    }
}

COUNTRY_CONTEXT = {
    "Nigeria":      "Africa's largest economy by GDP. Heavily oil-dependent with chronic fiscal deficits and high inflation.",
    "South Africa": "Most industrialised economy in Africa. Faces structural unemployment and slowing growth trajectory.",
    "Ghana":        "West Africa's growth success story, though recent debt restructuring has created headwinds.",
    "Egypt":        "North Africa's largest economy. Benefiting from IMF support and Suez Canal revenues.",
    "Kenya":        "East Africa's economic hub with strong services sector and consistent growth momentum."
}

# ── Country Selector ─────────────────────────────────────────────────────────
col_sel, col_info = st.columns([2, 3])
with col_sel:
    selected = st.multiselect(
        "Select countries to compare",
        options=list(FORECAST_DATA.keys()),
        default=["Nigeria", "Ghana", "Kenya"]
    )
    show_ci = st.toggle("Show confidence intervals", value=True)

with col_info:
    if selected:
        for country in selected:
            color = FORECAST_DATA[country]["color"]
            st.markdown(f"""
            <div style="padding:0.6rem 1rem; margin-bottom:0.5rem; border-radius:6px;
                        border-left:3px solid {color}; background:#111827;">
                <span style="color:{color}; font-weight:600; font-family:'DM Sans',sans-serif;">
                    {country}</span>
                <span style="color:#8892a4; font-size:0.85rem; margin-left:0.8rem;">
                    {COUNTRY_CONTEXT.get(country, '')}</span>
            </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Main Chart ────────────────────────────────────────────────────────────────
if not selected:
    st.info("Select at least one country above to view forecasts.")
else:
    fig = go.Figure()
    CUTOFF = 2025

    for country in selected:
        d = FORECAST_DATA[country]
        color = d["color"]

        actual_years = sorted(d["actual"].keys())
        actual_vals  = [d["actual"][y] for y in actual_years]

        fc_years = sorted(d["forecast"].keys())
        fc_vals  = [d["forecast"][y] for y in fc_years]
        lo_vals  = [d["lower"][y]    for y in fc_years]
        hi_vals  = [d["upper"][y]    for y in fc_years]

        # Actual line
        fig.add_trace(go.Scatter(
            x=actual_years, y=actual_vals, name=f"{country} (Actual)",
            line=dict(color=color, width=2.5),
            mode="lines+markers", marker=dict(size=4)
        ))

        # Bridge from last actual to first forecast
        last_actual_year = actual_years[-1]
        last_actual_val  = actual_vals[-1]
        bridge_x = [last_actual_year, fc_years[0]]
        bridge_y = [last_actual_val,  fc_vals[0]]

        fig.add_trace(go.Scatter(
            x=bridge_x, y=bridge_y, showlegend=False,
            line=dict(color=color, width=2, dash="dot"), mode="lines"
        ))

        # Forecast line
        fig.add_trace(go.Scatter(
            x=fc_years, y=fc_vals, name=f"{country} (Forecast)",
            line=dict(color=color, width=2.5, dash="dash"), mode="lines+markers",
            marker=dict(size=6, symbol="diamond")
        ))

        # Confidence interval
        if show_ci:
            r, g, b = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
            fig.add_trace(go.Scatter(
                x=fc_years + fc_years[::-1],
                y=hi_vals  + lo_vals[::-1],
                fill="toself",
                fillcolor=f"rgba({r},{g},{b},0.12)",
                line=dict(color="rgba(0,0,0,0)"),
                showlegend=False, hoverinfo="skip"
            ))

    # Forecast start line
    fig.add_vline(x=CUTOFF, line_dash="dot", line_color="#c9a84c",
                  annotation_text="Forecast →", annotation_font_color="#c9a84c",
                  annotation_position="top right")

    fig.add_hline(y=0, line_dash="dash", line_color="rgba(255,255,255,0.15)")

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0a0e1a", plot_bgcolor="#0a0e1a",
        font=dict(family="DM Sans", color="#e8eaf0"),
        title=dict(text="GDP Growth Rate — Historical & 5-Year Forecast (%)",
                   font=dict(family="Playfair Display", size=20, color="#c9a84c")),
        xaxis=dict(title="Year", gridcolor="#1e2d45", showgrid=True),
        yaxis=dict(title="GDP Growth Rate (%)", gridcolor="#1e2d45", showgrid=True,
                   zeroline=True, zerolinecolor="#333d50"),
        legend=dict(bgcolor="rgba(17,24,39,0.8)", bordercolor="#1e2d45", borderwidth=1),
        height=520,
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ── Forecast Table ────────────────────────────────────────────────────────
    st.markdown("### Forecast Summary Table")
    rows = []
    for country in selected:
        d = FORECAST_DATA[country]
        for yr in sorted(d["forecast"].keys()):
            rows.append({
                "Country": country,
                "Year": yr,
                "Forecast (%)": round(d["forecast"][yr], 2),
                "Lower CI": round(d["lower"][yr], 2),
                "Upper CI": round(d["upper"][yr], 2),
                "Outlook": "🟢 Positive" if d["forecast"][yr] > 2 else
                           "🟡 Moderate" if d["forecast"][yr] > 0 else "🔴 Negative"
            })

    tbl = pd.DataFrame(rows)
    st.dataframe(
        tbl, use_container_width=True, hide_index=True,
        column_config={
            "Forecast (%)": st.column_config.NumberColumn(format="%.2f%%"),
            "Lower CI":     st.column_config.NumberColumn(format="%.2f%%"),
            "Upper CI":     st.column_config.NumberColumn(format="%.2f%%"),
        }
    )

    # ── Key Insight ───────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-left:4px solid #c9a84c;
                border-radius:8px; padding:1.2rem 1.5rem;">
        <span style="color:#c9a84c; font-weight:600; font-family:'DM Mono',monospace;
                     font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">
            📊 Analyst Note
        </span>
        <p style="color:#e8eaf0; margin:0.5rem 0 0; line-height:1.6;">
            <b>Kenya</b> shows the most optimistic forecast trajectory (~5.7–5.9%), driven by a
            strong services sector. <b>Ghana</b> maintains steady growth (~4.1–4.3%) post-debt restructuring.
            <b>Nigeria</b>'s forecast decline reflects structural oil dependency and persistent inflation.
            <b>South Africa</b> risks entering negative growth by 2027–28 without structural reform.
            All confidence intervals widen over time — reflecting genuine macroeconomic uncertainty.
        </p>
    </div>""", unsafe_allow_html=True)
