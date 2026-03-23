import streamlit as st

st.set_page_config(
    page_title="Home · African Fiscal Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400;500&display=swap');

:root {
    --bg:        #0a0e1a;
    --surface:   #111827;
    --border:    #1e2d45;
    --gold:      #c9a84c;
    --gold-soft: #e8c97a;
    --text:      #e8eaf0;
    --muted:     #8892a4;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stSidebar"] {
    background: #111827 !important;
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
    font-weight: 600 !important;
    border: none !important;
    border-radius: 4px !important;
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:3rem 0 2rem 0; text-align:center;">
    <div style="font-family:'DM Mono',monospace; color:#c9a84c; font-size:0.8rem;
                letter-spacing:0.2em; text-transform:uppercase; margin-bottom:1rem;">
        10Alytics Hackathon 2025 · Fiscal Intelligence
    </div>
    <h1 style="font-family:'Playfair Display',serif; font-size:3rem; font-weight:900;
               color:#e8eaf0; line-height:1.15; margin:0;">
        African Fiscal<br>
        <span style="color:#c9a84c;">Intelligence Platform</span>
    </h1>
    <p style="color:#8892a4; font-size:1rem; max-width:600px;
              margin:1.2rem auto 0; line-height:1.7;">
        AI-powered analysis of macroeconomic and fiscal indicators across 14 African economies —
        transforming fragmented data into actionable policy intelligence aligned with the UN SDGs.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:none;border-top:1px solid #1e2d45;margin:0 0 2rem 0;'>", unsafe_allow_html=True)

# ── Summary Cards ─────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, label, value, sub in [
    (c1, "Countries Analysed",  "14",  "Across Sub-Saharan & North Africa"),
    (c2, "Years of Data",       "65",  "1960 – 2025"),
    (c3, "Fiscal Indicators",   "20+", "GDP, Debt, Inflation, Trade & more"),
    (c4, "ML Models Deployed",  "3",   "Prophet · XGBoost · K-Means"),
]:
    with col:
        st.markdown(f"""
        <div style="background:#111827; border:1px solid #1e2d45; border-left:4px solid #c9a84c;
                    border-radius:8px; padding:1.2rem 1.4rem; margin-bottom:1rem;">
            <div style="color:#8892a4; font-size:0.72rem; letter-spacing:0.1em;
                        text-transform:uppercase; font-family:'DM Mono',monospace;
                        margin-bottom:0.3rem;">{label}</div>
            <div style="font-size:1.8rem; font-weight:700; color:#e8eaf0;
                        font-family:'Playfair Display',serif;">{value}</div>
            <div style="font-size:0.8rem; color:#8892a4; margin-top:0.2rem;">{sub}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<hr style='border:none;border-top:1px solid #1e2d45;margin:0.5rem 0 1.5rem 0;'>", unsafe_allow_html=True)

# ── Navigation Cards ──────────────────────────────────────────────────────────
st.markdown("""
<h2 style="font-size:1.6rem; margin-bottom:1.2rem;">Explore the Platform</h2>
""", unsafe_allow_html=True)

n1, n2, n3, n4 = st.columns(4)
for col, icon, title, desc in [
    (n1, "📈", "GDP Forecasts",
     "5-year Prophet forecasts for Nigeria, Ghana, South Africa, Egypt & Kenya with confidence intervals."),
    (n2, "⚠️", "Fiscal Risk Scorer",
     "Enter any country's indicators and get an AI-powered fiscal risk classification instantly."),
    (n3, "🗺️", "Country Clusters",
     "Interactive Africa map showing fiscal health clusters across 14 economies with radar charts."),
    (n4, "📋", "Policy Advisor",
     "SDG-aligned policy recommendations tailored to each country's fiscal cluster assignment."),
]:
    with col:
        st.markdown(f"""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:10px;
                    padding:1.5rem; min-height:200px;">
            <div style="font-size:2rem; margin-bottom:0.8rem;">{icon}</div>
            <div style="font-family:'Playfair Display',serif; font-size:1.05rem;
                        color:#c9a84c; margin-bottom:0.6rem; font-weight:700;">{title}</div>
            <div style="color:#8892a4; font-size:0.85rem; line-height:1.6;">{desc}</div>
        </div>""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding:1rem 0; border-top:1px solid #1e2d45;">
    <p style="color:#8892a4; font-size:0.78rem; font-family:'DM Mono',monospace; margin:0;">
        Use the sidebar to navigate between sections · Built for 10Alytics Hackathon 2025
    </p>
    <p style="margin:0.4rem 0 0;">
        <a href="https://github.com/mojay6111/10alytics_Hackathon"
           style="color:#c9a84c; font-size:0.78rem; text-decoration:none;
                  font-family:'DM Mono',monospace;">
            ⭐ Star on GitHub
        </a>
    </p>
</div>
""", unsafe_allow_html=True)
