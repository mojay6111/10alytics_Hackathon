import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Country Clusters · African Fiscal Intelligence",
                   page_icon="🗺️", layout="wide")

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

st.markdown("## 🗺️ Fiscal Health Country Clusters")
st.markdown("<p style='color:#8892a4;'>K-Means clustering with Z-score normalization across 6 fiscal indicators. Currency-corrected to prevent scale distortion.</p>", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
CLUSTERS = {
    "Nigeria":      {"cluster": "🔴 High Stress",  "color": "#e05252", "lat":  9.08, "lon":  8.68},
    "Egypt":        {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat": 26.82, "lon": 30.80},
    "Ethiopia":     {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat":  9.14, "lon": 40.49},
    "Ghana":        {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat":  7.94, "lon": -1.02},
    "Ivory Coast":  {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat":  7.54, "lon": -5.55},
    "Kenya":        {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat": -0.02, "lon": 37.91},
    "Rwanda":       {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat": -1.94, "lon": 29.87},
    "Togo":         {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat":  8.62, "lon":  0.82},
    "South Africa": {"cluster": "🟢 Stable",        "color": "#3db87a", "lat":-30.56, "lon": 22.94},
    "Tanzania":     {"cluster": "🟢 Stable",        "color": "#3db87a", "lat": -6.37, "lon": 34.89},
    "Algeria":      {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat": 28.03, "lon":  1.66},
    "Angola":       {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat":-11.20, "lon": 17.87},
    "Botswana":     {"cluster": "🟢 Stable",        "color": "#3db87a", "lat":-22.33, "lon": 24.68},
    "Senegal":      {"cluster": "🟡 Moderate Risk", "color": "#e08c2e", "lat": 14.50, "lon":-14.45},
}

PROFILES = {
    "Nigeria":      {"Budget Deficit/GDP (%)": -6.2,  "Govt Debt/GDP (%)": 38.7, "GDP Growth (%)": 2.3,  "Inflation (%)": 24.5, "Unemployment (%)":  5.0, "Tax Revenue/GDP (%)":  6.2},
    "Egypt":        {"Budget Deficit/GDP (%)": -6.1,  "Govt Debt/GDP (%)": 87.2, "GDP Growth (%)": 3.8,  "Inflation (%)": 33.9, "Unemployment (%)":  7.4, "Tax Revenue/GDP (%)": 14.8},
    "Ethiopia":     {"Budget Deficit/GDP (%)": -2.8,  "Govt Debt/GDP (%)": 54.4, "GDP Growth (%)": 8.4,  "Inflation (%)": 28.0, "Unemployment (%)":  3.4, "Tax Revenue/GDP (%)":  8.7},
    "Ghana":        {"Budget Deficit/GDP (%)": -5.8,  "Govt Debt/GDP (%)": 88.1, "GDP Growth (%)": 2.9,  "Inflation (%)": 23.2, "Unemployment (%)": 13.4, "Tax Revenue/GDP (%)": 13.6},
    "Ivory Coast":  {"Budget Deficit/GDP (%)": -4.2,  "Govt Debt/GDP (%)": 56.8, "GDP Growth (%)": 6.1,  "Inflation (%)":  4.2, "Unemployment (%)":  3.4, "Tax Revenue/GDP (%)": 12.1},
    "Kenya":        {"Budget Deficit/GDP (%)": -5.4,  "Govt Debt/GDP (%)": 70.2, "GDP Growth (%)": 5.6,  "Inflation (%)":  6.8, "Unemployment (%)":  5.5, "Tax Revenue/GDP (%)": 15.2},
    "Rwanda":       {"Budget Deficit/GDP (%)": -5.1,  "Govt Debt/GDP (%)": 68.4, "GDP Growth (%)": 8.2,  "Inflation (%)":  7.2, "Unemployment (%)": 14.2, "Tax Revenue/GDP (%)": 16.1},
    "Togo":         {"Budget Deficit/GDP (%)": -2.4,  "Govt Debt/GDP (%)": 64.2, "GDP Growth (%)": 5.8,  "Inflation (%)":  7.6, "Unemployment (%)":  3.4, "Tax Revenue/GDP (%)": 15.4},
    "South Africa": {"Budget Deficit/GDP (%)": -5.3,  "Govt Debt/GDP (%)": 73.4, "GDP Growth (%)": 0.7,  "Inflation (%)":  6.1, "Unemployment (%)": 32.9, "Tax Revenue/GDP (%)": 25.3},
    "Tanzania":     {"Budget Deficit/GDP (%)": -3.2,  "Govt Debt/GDP (%)": 42.1, "GDP Growth (%)": 5.1,  "Inflation (%)":  4.4, "Unemployment (%)":  2.3, "Tax Revenue/GDP (%)": 12.8},
    "Algeria":      {"Budget Deficit/GDP (%)": -3.8,  "Govt Debt/GDP (%)": 60.2, "GDP Growth (%)": 3.6,  "Inflation (%)":  9.3, "Unemployment (%)": 12.5, "Tax Revenue/GDP (%)": 32.4},
    "Angola":       {"Budget Deficit/GDP (%)": -2.1,  "Govt Debt/GDP (%)": 84.1, "GDP Growth (%)": 1.2,  "Inflation (%)": 13.6, "Unemployment (%)":  7.1, "Tax Revenue/GDP (%)": 20.6},
    "Botswana":     {"Budget Deficit/GDP (%)": -4.2,  "Govt Debt/GDP (%)": 18.6, "GDP Growth (%)": 3.8,  "Inflation (%)":  4.2, "Unemployment (%)": 24.5, "Tax Revenue/GDP (%)": 28.1},
    "Senegal":      {"Budget Deficit/GDP (%)": -4.6,  "Govt Debt/GDP (%)": 73.1, "GDP Growth (%)": 4.4,  "Inflation (%)":  5.8, "Unemployment (%)":  3.4, "Tax Revenue/GDP (%)": 14.2},
}

def hex_to_rgba(hex_color, alpha=0.15):
    """Safely convert #rrggbb to rgba(r,g,b,alpha) string."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return "rgba({},{},{},{})".format(r, g, b, alpha)

df_clusters = pd.DataFrame([
    {"Country": k, "Cluster": v["cluster"], "Color": v["color"],
     "Lat": v["lat"], "Lon": v["lon"]}
    for k, v in CLUSTERS.items()
])

# ── Map ───────────────────────────────────────────────────────────────────────
fig_map = go.Figure()

for cluster, color, label in [
    ("🔴 High Stress",  "#e05252", "High Stress"),
    ("🟡 Moderate Risk","#e08c2e", "Moderate Risk"),
    ("🟢 Stable",       "#3db87a", "Stable"),
]:
    sub = df_clusters[df_clusters["Cluster"] == cluster]
    fig_map.add_trace(go.Scattergeo(
        lat=sub["Lat"], lon=sub["Lon"],
        text=sub["Country"],
        name=cluster,
        mode="markers+text",
        textposition="top center",
        textfont=dict(size=11, color=color, family="DM Sans"),
        marker=dict(size=16, color=color, opacity=0.85,
                    line=dict(width=2, color="white")),
        hovertemplate="<b>%{text}</b><br>" + cluster + "<extra></extra>"
    ))

fig_map.update_layout(
    geo=dict(
        scope="africa",
        bgcolor="#0a0e1a",
        landcolor="#111827",
        oceancolor="#0a0e1a",
        lakecolor="#0a0e1a",
        countrycolor="#1e2d45",
        showland=True, showocean=True, showlakes=True,
        showcountries=True,
        projection_type="natural earth",
        framecolor="#1e2d45",
    ),
    paper_bgcolor="#0a0e1a",
    font=dict(family="DM Sans", color="#e8eaf0"),
    legend=dict(bgcolor="rgba(17,24,39,0.9)", bordercolor="#1e2d45",
                borderwidth=1, font=dict(size=13)),
    title=dict(text="African Fiscal Health Clusters (Z-Score Normalized)",
               font=dict(family="Playfair Display", size=18, color="#c9a84c")),
    height=560,
    margin=dict(t=50, b=0, l=0, r=0)
)

st.plotly_chart(fig_map, use_container_width=True)

# ── Cluster Summary Pills ─────────────────────────────────────────────────────
c1, c2, c3 = st.columns(3)
for col, cluster, color, bg, countries_filter in [
    (c1, "🔴 High Stress",   "#e05252", "rgba(224,82,82,0.1)",   "🔴 High Stress"),
    (c2, "🟡 Moderate Risk", "#e08c2e", "rgba(224,140,46,0.1)",  "🟡 Moderate Risk"),
    (c3, "🟢 Stable",        "#3db87a", "rgba(61,184,122,0.1)",  "🟢 Stable"),
]:
    countries = df_clusters[df_clusters["Cluster"] == countries_filter]["Country"].tolist()
    with col:
        st.markdown(f"""
        <div style="background:{bg}; border:1px solid {color}; border-radius:10px; padding:1.2rem;">
            <div style="color:{color}; font-weight:700; font-size:1rem;
                        font-family:'Playfair Display',serif; margin-bottom:0.8rem;">
                {cluster} · {len(countries)} countries
            </div>
            {"".join(f'<span style="background:rgba(255,255,255,0.06); color:#e8eaf0; border-radius:4px; padding:0.2rem 0.6rem; margin:0.2rem; display:inline-block; font-size:0.82rem;">{c}</span>' for c in countries)}
        </div>""", unsafe_allow_html=True)

# ── Country Deep Dive ─────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### Country Deep Dive")

selected_country = st.selectbox("Select a country", sorted(PROFILES.keys()))

if selected_country:
    profile = PROFILES[selected_country]
    cluster = CLUSTERS[selected_country]["cluster"]
    color   = CLUSTERS[selected_country]["color"]
    fill_color = hex_to_rgba(color, 0.15)

    categories = list(profile.keys())
    values     = list(profile.values())

    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values, theta=categories, fill="toself",
        line=dict(color=color, width=2),
        fillcolor=fill_color,
        name=selected_country
    ))

    # Regional median reference line
    median_vals = [-4.5, 62.0, 4.2, 10.8, 8.6, 16.2]
    fig_radar.add_trace(go.Scatterpolar(
        r=median_vals, theta=categories, fill="toself",
        line=dict(color="#8892a4", width=1.5, dash="dot"),
        fillcolor="rgba(136,146,164,0.05)",
        name="Regional Median"
    ))

    fig_radar.update_layout(
        polar=dict(
            bgcolor="#111827",
            radialaxis=dict(visible=True, color="#8892a4", gridcolor="#1e2d45"),
            angularaxis=dict(color="#e8eaf0", gridcolor="#1e2d45")
        ),
        paper_bgcolor="#0a0e1a",
        font=dict(family="DM Sans", color="#e8eaf0"),
        title=dict(text="{} — Fiscal Radar vs Regional Median".format(selected_country),
                   font=dict(family="Playfair Display", size=16, color="#c9a84c")),
        legend=dict(bgcolor="rgba(17,24,39,0.8)", bordercolor="#1e2d45"),
        height=420,
    )

    col_radar, col_stats = st.columns([1, 1])
    with col_radar:
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_stats:
        st.markdown("""
        <div style="background:#111827; border:1px solid {color}; border-radius:10px;
                    padding:1.5rem; margin-top:1rem;">
            <div style="color:{color}; font-family:'Playfair Display',serif;
                        font-size:1.1rem; font-weight:700; margin-bottom:1rem;">
                {country} · {cluster}
            </div>
        """.format(color=color, country=selected_country, cluster=cluster),
        unsafe_allow_html=True)

        for metric, value in profile.items():
            is_bad = (metric == "Inflation (%)" and value > 10) or \
                     (metric == "Budget Deficit/GDP (%)" and value < -5) or \
                     (metric == "Govt Debt/GDP (%)" and value > 70)
            val_color = "#e05252" if is_bad else "#3db87a"
            st.markdown("""
            <div style="display:flex; justify-content:space-between; align-items:center;
                        padding:0.5rem 0; border-bottom:1px solid #1e2d45;">
                <span style="color:#8892a4; font-size:0.85rem;">{metric}</span>
                <span style="color:{val_color}; font-family:'DM Mono',monospace;
                             font-weight:600;">{value:+.1f}</span>
            </div>""".format(metric=metric, val_color=val_color, value=value),
            unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)