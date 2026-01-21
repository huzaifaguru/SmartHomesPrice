import streamlit as st

st.set_page_config(
    page_title="About - SmartHomes AI",
    page_icon="ℹ️",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: #cbd5e1;
}

h1, h2, h3 {
    color: #f1f5f9;
}

p, li {
    color: #cbd5e1;
    line-height: 1.7;
}

.main-header {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 2.5rem;
    border-radius: 14px;
    border: 1px solid #1e293b;
    text-align: center;
    margin-bottom: 3rem;
}

.info-card {
    background-color: #020617;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 1.8rem;
    margin-bottom: 1.5rem;
}

.tech-badge {
    display: inline-block;
    background-color: #1e293b;
    color: #e5e7eb;
    padding: 0.4rem 0.9rem;
    border-radius: 20px;
    margin: 0.3rem;
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ----------------
st.markdown("""
<div class="main-header">
    <h1>About SmartHomes AI</h1>
    <p>System overview, methodology, and technical background</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Mission ----------------
st.markdown("## Project Objective")

st.write("""
SmartHomes AI is a machine learning–based system developed to estimate residential house prices
using structured property data. The goal of the project is to provide a transparent, fast, and
data-driven alternative to subjective property valuation methods.

The platform is designed primarily for educational, analytical, and experimental use, allowing
users to understand how different property attributes influence housing prices.
""")

# ---------------- How It Works ----------------
st.markdown("## System Workflow")

cols = st.columns(4)
steps = [
    ("Data Input", "Users provide property attributes such as area, rooms, and amenities."),
    ("Preprocessing", "Inputs are encoded and aligned with the training feature space."),
    ("Model Prediction", "A trained Linear Regression model estimates the house price."),
    ("Result Output", "The predicted price is displayed in a clear and interpretable format.")
]

for col, (title, desc) in zip(cols, steps):
    with col:
        st.markdown(f"### {title}")
        st.write(desc)

# ---------------- Tech Stack ----------------
st.markdown("## Technology Stack")

st.markdown("### Machine Learning & Data Processing")
st.markdown("""
<span class="tech-badge">Python</span>
<span class="tech-badge">Scikit-learn</span>
<span class="tech-badge">Pandas</span>
<span class="tech-badge">NumPy</span>
<span class="tech-badge">Linear Regression</span>
""", unsafe_allow_html=True)

st.markdown("### Web Application")
st.markdown("""
<span class="tech-badge">Streamlit</span>
<span class="tech-badge">HTML/CSS</span>
""", unsafe_allow_html=True)

# ---------------- Model Details ----------------
st.markdown("## Model Details")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h3>Algorithm</h3>
        <p>Linear Regression is used due to its interpretability and strong performance
        on structured tabular data.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <h3>Training Data</h3>
        <ul>
            <li>Total samples: 545</li>
            <li>Training set: 80%</li>
            <li>Test set: 20%</li>
            <li>Input features: 13</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3>Model Performance</h3>
        <ul>
            <li>R² Score: 65.3%</li>
            <li>MAE: ~970,000</li>
            <li>RMSE: ~1,324,000</li>
            <li>Prediction latency: < 0.1 seconds</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------- Limitations ----------------
st.markdown("## Limitations")

st.warning("""
This system provides **estimates only** and should not be treated as a replacement
for professional real estate appraisal. Model accuracy depends on similarity between
input data and the training dataset.
""")

# ---------------- Footer ----------------
st.markdown("""
<div style="text-align:center; color:#94a3b8; padding:2rem;">
    <p>SmartHomes AI © 2024</p>
    <p>Educational and experimental machine learning project</p>
</div>
""", unsafe_allow_html=True)
