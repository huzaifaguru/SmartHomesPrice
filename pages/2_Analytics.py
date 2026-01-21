import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Analytics - SmartHomes AI",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.stApp { background-color: #0b1220; color: #cbd5e1; }
h1, h2, h3 { color: #f1f5f9; }

.metric-card {
    background-color: #020617;
    border: 1px solid #1e293b;
    padding: 1.5rem;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>Analytics Dashboard</h1>
    <p>Model evaluation and performance analysis</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Model Performance Metrics")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Mean Absolute Error", "970,043")
with c2:
    st.metric("Root Mean Square Error", "1,324,507")
with c3:
    st.metric("R² Score", "65.3%")

st.markdown("## Detailed Metrics")

metrics_df = pd.DataFrame({
    "Metric": ["MAE", "RMSE", "R²", "Training Samples", "Test Samples"],
    "Value": ["970,043", "1,324,507", "0.653", "436", "109"]
})

st.dataframe(metrics_df, use_container_width=True, hide_index=True)

st.markdown("## Feature Importance")

st.write("""
Feature importance indicates how strongly each property attribute influences
the predicted house price. Larger values represent greater impact.
""")

feature_importance = pd.DataFrame({
    "Feature": ["Area", "Location", "Bedrooms", "Bathrooms", "Stories"],
    "Importance": [0.45, 0.25, 0.15, 0.10, 0.05]
})

st.bar_chart(feature_importance.set_index("Feature"))

st.markdown("""
**Insights**
- Property size is the dominant factor
- Location has significant influence
- Structural features provide incremental value
""")
