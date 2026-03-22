import streamlit as st
import pandas as pd

st.set_page_config(page_title="Policy Advisor · African Fiscal Intelligence",
                   page_icon="📋", layout="wide")

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

st.markdown("## 📋 Policy Advisor")
st.markdown("<p style='color:#8892a4;'>SDG-aligned fiscal policy recommendations generated from K-Means cluster assignments. Select a country to view its tailored policy brief.</p>", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
COUNTRY_CLUSTERS = {
    "Nigeria": "🔴 High Stress", "Egypt": "🟡 Moderate Risk", "Ethiopia": "🟡 Moderate Risk",
    "Ghana": "🟡 Moderate Risk", "Ivory Coast": "🟡 Moderate Risk", "Kenya": "🟡 Moderate Risk",
    "Rwanda": "🟡 Moderate Risk", "Togo": "🟡 Moderate Risk", "South Africa": "🟢 Stable",
    "Tanzania": "🟢 Stable", "Algeria": "🟡 Moderate Risk", "Angola": "🟡 Moderate Risk",
    "Botswana": "🟢 Stable", "Senegal": "🟡 Moderate Risk",
}

POLICY_FRAMEWORK = {
    "🔴 High Stress": {
        "color": "#e05252", "bg": "rgba(224,82,82,0.08)",
        "summary": "This economy requires urgent fiscal stabilisation. Chronic deficits, elevated debt, and high inflation are compounding structural weaknesses. Without immediate intervention, fiscal space will continue to erode.",
        "sdgs": [
            ("SDG 1", "No Poverty",           "#e05252", "Fiscal stress directly erodes purchasing power and social spending capacity."),
            ("SDG 8", "Decent Work & Growth",  "#e05252", "Unsustainable deficits crowd out private sector investment and job creation."),
            ("SDG 10","Reduced Inequalities",  "#e05252", "Inflation disproportionately harms low-income households."),
            ("SDG 16","Strong Institutions",   "#e05252", "Fiscal transparency and accountability reforms are foundational."),
        ],
        "fiscal_actions": [
            ("Broaden the tax base",              "Reduce reliance on commodity revenues. Expand VAT compliance and introduce presumptive taxation for informal sector."),
            ("Restructure government debt",       "Engage creditors for debt service relief. Pursue IMF/World Bank concessional financing to extend repayment timelines."),
            ("Rationalise expenditure",           "Audit all recurrent spending. Eliminate ghost workers, reduce fuel subsidies, redirect savings to capital expenditure."),
            ("Tighten monetary policy",           "Central bank must prioritise inflation targeting. Coordinate fiscal-monetary policy to avoid deficit monetisation."),
        ],
        "economic_actions": [
            ("Diversify export base",             "Reduce oil/commodity dependency through targeted industrial policy and export promotion agencies."),
            ("Strengthen social safety nets",     "Protect vulnerable populations from fiscal adjustment through conditional cash transfers and food security programs."),
            ("Attract multilateral support",      "Engage IMF Extended Fund Facility, World Bank DPL, and AfDB budget support operations."),
        ],
        "priority": "URGENT",
        "timeline": "0–18 months"
    },
    "🟡 Moderate Risk": {
        "color": "#e08c2e", "bg": "rgba(224,140,46,0.08)",
        "summary": "Structural vulnerabilities are present but manageable. Proactive fiscal consolidation and institutional strengthening will prevent deterioration. The window for gradual reform is open — delay risks escalation.",
        "sdgs": [
            ("SDG 8", "Decent Work & Growth",     "#e08c2e", "Moderate growth needs structural boost to create sufficient employment."),
            ("SDG 9", "Industry & Innovation",    "#e08c2e", "Infrastructure investment is key to unlocking productivity gains."),
            ("SDG 17","Partnerships for Goals",   "#e08c2e", "Strengthening revenue frameworks through international tax cooperation."),
            ("SDG 11","Sustainable Cities",       "#e08c2e", "Urban fiscal management and local government finance need improvement."),
        ],
        "fiscal_actions": [
            ("Improve tax collection efficiency", "Invest in revenue authority capacity, e-filing systems, and anti-evasion measures. Target 15%+ tax-to-GDP ratio."),
            ("Reduce deficit below 3% GDP",       "Implement medium-term fiscal frameworks with binding deficit ceilings. Publish quarterly fiscal reports."),
            ("Increase capital expenditure",      "Shift spending composition from recurrent to capital. Prioritise infrastructure with high multiplier effects."),
            ("Develop domestic debt markets",     "Issue local currency bonds to reduce forex exposure. Build yield curve to support private sector borrowing."),
        ],
        "economic_actions": [
            ("Invest in infrastructure",          "Roads, power, and digital infrastructure unlock private investment and reduce logistics costs."),
            ("Improve business climate",          "Streamline business registration, reduce permit timelines, and strengthen contract enforcement."),
            ("Regional trade integration",        "Leverage AfCFTA to expand market access and attract FDI through larger consumer market positioning."),
        ],
        "priority": "PROACTIVE",
        "timeline": "12–36 months"
    },
    "🟢 Stable": {
        "color": "#3db87a", "bg": "rgba(61,184,122,0.08)",
        "summary": "Fiscal fundamentals are relatively stable with institutional capacity to manage shocks. The priority is to deepen resilience, invest in human capital, and build fiscal buffers against future volatility.",
        "sdgs": [
            ("SDG 3", "Good Health & Wellbeing",  "#3db87a", "Fiscal space exists to increase health expenditure toward 15% of budget (Abuja Declaration)."),
            ("SDG 4", "Quality Education",        "#3db87a", "Stable budgets enable sustained investment in education outcomes."),
            ("SDG 13","Climate Action",           "#3db87a", "Use fiscal stability to lead green transition and attract climate finance."),
            ("SDG 17","Partnerships for Goals",   "#3db87a", "Position as anchor economy for regional fiscal cooperation."),
        ],
        "fiscal_actions": [
            ("Maintain fiscal discipline",        "Keep debt-to-GDP below 60%. Adopt fiscal rules with independent oversight. Publish long-term fiscal sustainability reports."),
            ("Build fiscal buffers",              "Establish or replenish stabilisation/sovereign wealth funds. Target 3–6 months import cover in reserves."),
            ("Increase social spending",          "Raise health spending to Abuja Declaration target (15% of budget). Expand education quality metrics."),
            ("Strengthen fiscal transparency",    "Adopt IPSAS accounting standards. Publish comprehensive budget documentation and citizens' budgets."),
        ],
        "economic_actions": [
            ("Lead green transition",             "Issue sovereign green bonds. Set net-zero targets. Develop renewable energy capacity to attract climate finance."),
            ("Attract quality FDI",               "Leverage stable macro environment and rule of law to target high-value manufacturing and services FDI."),
            ("Champion regional integration",     "Use institutional strength to anchor AfCFTA implementation and regional infrastructure financing."),
        ],
        "priority": "STRATEGIC",
        "timeline": "36–60 months"
    }
}

# ── Country Selector ──────────────────────────────────────────────────────────
col_sel, col_stat = st.columns([1, 2])

with col_sel:
    country = st.selectbox("Select Country", sorted(COUNTRY_CLUSTERS.keys()))
    cluster = COUNTRY_CLUSTERS[country]
    policy  = POLICY_FRAMEWORK[cluster]

    st.markdown(f"""
    <div style="background:{policy['bg']}; border:1px solid {policy['color']};
                border-radius:10px; padding:1.2rem; margin-top:1rem; text-align:center;">
        <div style="color:{policy['color']}; font-weight:700;
                    font-family:'Playfair Display',serif; font-size:1.1rem;">{cluster}</div>
        <div style="color:#8892a4; font-size:0.8rem; margin-top:0.4rem;
                    font-family:'DM Mono',monospace;">
            Priority: {policy['priority']} · Timeline: {policy['timeline']}
        </div>
    </div>""", unsafe_allow_html=True)

with col_stat:
    st.markdown(f"""
    <div style="background:#111827; border:1px solid #1e2d45; border-left:4px solid {policy['color']};
                border-radius:8px; padding:1.2rem 1.5rem; margin-top:0.5rem;">
        <div style="color:#c9a84c; font-family:'DM Mono',monospace; font-size:0.7rem;
                    text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.6rem;">
            Fiscal Assessment — {country}
        </div>
        <p style="color:#e8eaf0; margin:0; line-height:1.7; font-size:0.95rem;">
            {policy['summary']}
        </p>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr style='border:none;border-top:1px solid #1e2d45;margin:1.5rem 0;'>", unsafe_allow_html=True)

# ── SDG Alignment ─────────────────────────────────────────────────────────────
st.markdown("### Priority SDGs")
sdg_cols = st.columns(4)
for i, (num, name, color, rationale) in enumerate(policy["sdgs"]):
    with sdg_cols[i]:
        st.markdown(f"""
        <div style="background:#111827; border:1px solid {color}; border-radius:10px;
                    padding:1.1rem; height:140px;">
            <div style="color:{color}; font-weight:700; font-family:'DM Mono',monospace;
                        font-size:1rem;">{num}</div>
            <div style="color:#e8eaf0; font-weight:600; margin:0.3rem 0 0.5rem;
                        font-size:0.9rem;">{name}</div>
            <div style="color:#8892a4; font-size:0.78rem; line-height:1.5;">{rationale}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Action Plan ───────────────────────────────────────────────────────────────
col_fiscal, col_econ = st.columns(2, gap="large")

with col_fiscal:
    st.markdown(f"<h3 style='color:{policy['color']};font-size:1.1rem;'>💰 Fiscal Actions</h3>", unsafe_allow_html=True)
    for i, (title, desc) in enumerate(policy["fiscal_actions"], 1):
        st.markdown(f"""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:8px;
                    padding:1rem 1.2rem; margin-bottom:0.7rem;
                    border-left:3px solid {policy['color']};">
            <div style="display:flex; align-items:flex-start; gap:0.7rem;">
                <span style="color:{policy['color']}; font-family:'DM Mono',monospace;
                             font-size:0.8rem; font-weight:600; margin-top:2px;">0{i}</span>
                <div>
                    <div style="color:#e8eaf0; font-weight:600; margin-bottom:0.3rem;
                                font-size:0.92rem;">{title}</div>
                    <div style="color:#8892a4; font-size:0.83rem; line-height:1.5;">{desc}</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

with col_econ:
    st.markdown(f"<h3 style='color:{policy['color']};font-size:1.1rem;'>📈 Economic Actions</h3>", unsafe_allow_html=True)
    for i, (title, desc) in enumerate(policy["economic_actions"], 1):
        st.markdown(f"""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:8px;
                    padding:1rem 1.2rem; margin-bottom:0.7rem;
                    border-left:3px solid #c9a84c;">
            <div style="display:flex; align-items:flex-start; gap:0.7rem;">
                <span style="color:#c9a84c; font-family:'DM Mono',monospace;
                             font-size:0.8rem; font-weight:600; margin-top:2px;">0{i}</span>
                <div>
                    <div style="color:#e8eaf0; font-weight:600; margin-bottom:0.3rem;
                                font-size:0.92rem;">{title}</div>
                    <div style="color:#8892a4; font-size:0.83rem; line-height:1.5;">{desc}</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

# ── All Countries Summary Table ───────────────────────────────────────────────
st.markdown("<hr style='border:none;border-top:1px solid #1e2d45;margin:2rem 0 1rem;'>", unsafe_allow_html=True)
st.markdown("### All Countries — Policy Priority Overview")

rows = []
for c, cl in sorted(COUNTRY_CLUSTERS.items()):
    p = POLICY_FRAMEWORK[cl]
    rows.append({"Country": c, "Cluster": cl, "Priority": p["priority"], "Timeline": p["timeline"]})

df_summary = pd.DataFrame(rows)
st.dataframe(df_summary, use_container_width=True, hide_index=True,
             column_config={"Cluster": st.column_config.TextColumn(width="medium"),
                            "Priority": st.column_config.TextColumn(width="small"),
                            "Timeline": st.column_config.TextColumn(width="small")})
