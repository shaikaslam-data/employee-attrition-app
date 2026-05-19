import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Employee Attrition Dashboard",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.metric-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
    text-align: center;
}

h1,h2,h3 {
    color: #1e293b;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================

st.title("Employee Attrition Analysis Dashboard")

st.markdown("""
Comprehensive workforce attrition diagnostics and behavioral analytics
""")

st.markdown("---")

# =====================================================
# KPI SECTION
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Overall Attrition Rate",
        value="47.47%"
    )

with col2:
    st.metric(
        label="Average Employee Income",
        value="$7,299"
    )

with col3:
    st.metric(
        label="Poor Work-Life Balance Attrition",
        value="60.17%"
    )

st.markdown("---")

# =====================================================
# CHART 1
# =====================================================

st.subheader("Attrition Trend Across Job Levels")

job_df = pd.DataFrame({
    "Job Level": ["Entry", "Mid", "Senior"],
    "Attrition Rate": [63.27, 45.42, 20.27]
})

fig1 = px.line(
    job_df,
    x="Job Level",
    y="Attrition Rate",
    markers=True,
    title="Employee Attrition Rate by Job Level"
)

fig1.update_layout(
    template="plotly_white",
    height=450
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("""
### Key Insight
Entry-level employees demonstrate the highest attrition levels, indicating early-career instability and higher workforce replacement exposure.
""")

st.markdown("---")

# =====================================================
# CHART 2
# =====================================================

st.subheader("Composite Attrition Risk Index (CARI) Analysis")

risk_df = pd.DataFrame({
    "Risk Tier": [
        "Critical (61+)",
        "High (41–60)",
        "Medium (21–40)",
        "Low (0–20)"
    ],
    "Headcount": [10041, 26702, 26348, 11407],
    "Attrition Rate": [61.46, 51.98, 42.90, 35.21]
})

fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=risk_df["Risk Tier"],
    y=risk_df["Headcount"],
    name="Headcount"
))

fig2.add_trace(go.Scatter(
    x=risk_df["Risk Tier"],
    y=risk_df["Attrition Rate"],
    mode='lines+markers',
    name="Attrition Rate %"
))

fig2.update_layout(
    title="Employee Risk Tier vs Attrition Behavior",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
### Key Insight
Employees classified in the critical risk segment exhibit substantially higher attrition behavior, making them priority retention targets.
""")

st.markdown("---")

# =====================================================
# CHART 3
# =====================================================

st.subheader("Triple Deprivation Workforce Analysis")

triple_df = pd.DataFrame({
    "Cohort": ["Rest", "Triple Deprivation"],
    "Attrition Rate": [47.06, 63.32]
})

fig3 = px.pie(
    triple_df,
    names="Cohort",
    values="Attrition Rate",
    title="Attrition Distribution Across Triple Deprivation Cohorts",
    hole=0.4
)

fig3.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
### Key Insight
Employees simultaneously experiencing poor satisfaction, weak work-life balance, and poor company reputation exhibit severe attrition vulnerability.
""")

st.markdown("---")

# =====================================================
# CHART 4
# =====================================================

st.subheader("Promotion Impact on High Satisfaction Employees")

promo_df = pd.DataFrame({
    "Promotions": [0,1,2,3,4],
    "Attrition Rate": [11.71,5.77,4.31,0.68,0.14]
})

fig4 = px.scatter(
    promo_df,
    x="Promotions",
    y="Attrition Rate",
    size="Attrition Rate",
    title="Promotion Frequency vs Attrition Rate",
)

fig4.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(fig4, use_container_width=True)

st.markdown("""
### Key Insight
Career growth opportunities significantly reduce employee exit probability, even among highly satisfied employees.
""")

st.markdown("---")

# =====================================================
# CHART 5
# =====================================================

st.subheader("Recognition Deficit Analysis")

talent_df = pd.DataFrame({
    "Talent Segment": [
        "High perf + Low recognition",
        "High perf + High recognition",
        "Low/Below-avg performance"
    ],
    "Attrition Rate": [26.02, 10.88, 10.57]
})

fig5 = px.bar(
    talent_df,
    x="Talent Segment",
    y="Attrition Rate",
    title="Attrition Impact of Recognition Deficiency"
)

fig5.update_layout(
    template="plotly_white",
    height=500
)

st.plotly_chart(fig5, use_container_width=True)

st.markdown("""
### Key Insight
High-performing employees with insufficient recognition show elevated resignation behavior despite strong performance outcomes.
""")

st.markdown("---")

# =====================================================
# CHART 6
# =====================================================

st.subheader("Behavioral Attrition Escalation Curve")

risk2_df = pd.DataFrame({
    "Risk Tier": [
        "Critical (61+)",
        "High (41–60)",
        "Medium (21–40)",
        "Low (0–20)"
    ],
    "Attrited": [2052,10153,15900,7265],
    "Attrition Rate": [63.57,55.52,47.94,36.66]
})

fig6 = go.Figure()

fig6.add_trace(go.Scatter(
    x=risk2_df["Risk Tier"],
    y=risk2_df["Attrited"],
    mode='lines+markers',
    name='Attrited Employees'
))

fig6.add_trace(go.Scatter(
    x=risk2_df["Risk Tier"],
    y=risk2_df["Attrition Rate"],
    mode='lines+markers',
    name='Attrition Rate %'
))

fig6.update_layout(
    title="Attrition Escalation Across Behavioral Risk Tiers",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig6, use_container_width=True)

st.markdown("""
### Key Insight
Combined overtime pressure, dissatisfaction, and weak work-life balance dramatically accelerate workforce attrition patterns.
""")