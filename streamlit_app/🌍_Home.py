import streamlit as st

st.set_page_config(
    page_title="🌍 Home · African Fiscal Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

:root {
    --bg:        #0a0e1a;
    --surface:   #111827;
    --border:    #1e2d45;
    --gold:      #c9a84c;
    --gold-soft: #e8c97a;
    --red:       #e05252;
    --amber:     #e08c2e;
    --green:     #3db87a;
    --text:      #e8eaf0;
    --muted:     #8892a4;
    --accent:    #2563eb;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * { color: var(--text) !important; }

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: var(--gold) !important;
}

.stButton > button {
    background: var(--gold) !important;
    color: #0a0e1a !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 0.5rem 1.5rem !important;
}

.stButton > button:hover {
    background: var(--gold-soft) !important;
}

.stSelectbox > div, .stMultiSelect > div {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
}

.metric-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 4px solid var(--gold);
    border-radius: 8px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 0.8rem;
}

.metric-card h4 { color: var(--muted); font-size: 0.75rem; letter-spacing: 0.1em;
                  text-transform: uppercase; margin: 0 0 0.3rem 0; font-family: 'DM Mono', monospace; }
.metric-card .value { font-size: 1.8rem; font-weight: 700; color: var(--text);
                      font-family: 'Playfair Display', serif; }
.metric-card .delta { font-size: 0.8rem; color: var(--muted); margin-top: 0.2rem; }

.cluster-pill {
    display: inline-block;
    padding: 0.25rem 0.9rem;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 600;
    font-family: 'DM Mono', monospace;
}
.pill-red    { background: rgba(224,82,82,0.15);  color: #e05252; border: 1px solid rgba(224,82,82,0.3); }
.pill-amber  { background: rgba(224,140,46,0.15); color: #e08c2e; border: 1px solid rgba(224,140,46,0.3); }
.pill-green  { background: rgba(61,184,122,0.15); color: #3db87a; border: 1px solid rgba(61,184,122,0.3); }

.divider { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 3rem 0 2rem 0; text-align: center;">
    <div style="font-family:'DM Mono',monospace; color:#c9a84c; font-size:0.8rem;
                letter-spacing:0.2em; text-transform:uppercase; margin-bottom:1rem;">
        10Alytics Hackathon 2025 · Fiscal Intelligence
    </div>
    <h1 style="font-family:'Playfair Display',serif; font-size:3.2rem; font-weight:900;
               color:#e8eaf0; line-height:1.15; margin:0;">
        African Fiscal<br>
        <span style="color:#c9a84c;">Intelligence Platform</span>
    </h1>
    <p style="color:#8892a4; font-size:1.05rem; max-width:620px;
              margin:1.2rem auto 0; line-height:1.7;">
        AI-powered analysis of macroeconomic and fiscal indicators across 14 African economies —
        transforming fragmented data into actionable policy intelligence aligned with the UN SDGs.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── Summary Cards ─────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <h4>Countries Analysed</h4>
        <div class="value">14</div>
        <div class="delta">Across Sub-Saharan & North Africa</div>
    </div>""", unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <h4>Years of Data</h4>
        <div class="value">65</div>
        <div class="delta">1960 – 2025</div>
    </div>""", unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <h4>Fiscal Indicators</h4>
        <div class="value">20+</div>
        <div class="delta">GDP, Debt, Inflation, Trade & more</div>
    </div>""", unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <h4>ML Models Deployed</h4>
        <div class="value">3</div>
        <div class="delta">Prophet · XGBoost · K-Means</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ── Navigation Cards ──────────────────────────────────────────────────────────
st.markdown("""
<h2 style="font-size:1.6rem; margin-bottom:1.5rem;">Explore the Platform</h2>
""", unsafe_allow_html=True)

n1, n2, n3, n4 = st.columns(4)

nav_style = """
<div style="background:#111827; border:1px solid #1e2d45; border-radius:10px;
            padding:1.5rem; height:180px; transition:border-color 0.2s;">
    <div style="font-size:2rem; margin-bottom:0.8rem;">{icon}</div>
    <div style="font-family:'Playfair Display',serif; font-size:1.1rem;
                color:#c9a84c; margin-bottom:0.5rem;">{title}</div>
    <div style="color:#8892a4; font-size:0.85rem; line-height:1.5;">{desc}</div>
</div>
"""

with n1:
    st.markdown(nav_style.format(
        icon="📈", title="GDP Forecasts",
        desc="5-year Prophet forecasts for Nigeria, Ghana, South Africa, Egypt & Kenya"
    ), unsafe_allow_html=True)

with n2:
    st.markdown(nav_style.format(
        icon="⚠️", title="Fiscal Risk Scorer",
        desc="Enter any country's indicators and get an AI-powered risk classification"
    ), unsafe_allow_html=True)

with n3:
    st.markdown(nav_style.format(
        icon="🗺️", title="Country Clusters",
        desc="Interactive map of fiscal health clusters across 14 African economies"
    ), unsafe_allow_html=True)

with n4:
    st.markdown(nav_style.format(
        icon="📋", title="Policy Advisor",
        desc="SDG-aligned recommendations tailored to each country's fiscal cluster"
    ), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<p style="text-align:center; color:#8892a4; font-size:0.8rem; font-family:'DM Mono',monospace;">
    Use the sidebar to navigate between sections · Built for 10Alytics Hackathon 2025
</p>
""", unsafe_allow_html=True)
