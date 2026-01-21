# app.py - Home Page
import streamlit as st

st.set_page_config(
    page_title="SmartHomes AI",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="SmartHomes AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# Dark Theme CSS (Streamlit-Safe)
# ---------------------------------
st.markdown("""
<style>

/* Global Typography */
html, body, [class*="css"] {
    font-family: "Segoe UI", Arial, sans-serif;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* App Background */
.stApp {
    background-color: #0b1220;
}

/* ---------------- Hero Section ---------------- */
.main-header {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 3rem 2rem;
    border-radius: 14px;
    color: #f9fafb;
    text-align: center;
    margin-bottom: 3rem;
    border: 1px solid #1f2937;
}

.main-header h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: #f9fafb;
}

.main-header p {
    font-size: 1.1rem;
    color: #cbd5e1;
}

/* ---------------- Headings ---------------- */
h2 {
    color: #f1f5f9;
    font-weight: 700;
    margin-bottom: 1rem;
}

h3 {
    color: #e5e7eb;
    font-weight: 600;
}

/* ---------------- Text ---------------- */
p, li {
    color: #cbd5e1;
    line-height: 1.7;
    font-size: 1rem;
}

/* ---------------- Cards ---------------- */
.feature-card {
    background-color: #020617;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid #1e293b;
    min-height: 240px;
}

.feature-card p {
    color: #94a3b8;
    font-size: 0.95rem;
}

/* ---------------- Metrics ---------------- */
[data-testid="stMetric"] {
    background-color: #020617;
    padding: 1.3rem;
    border-radius: 12px;
    border: 1px solid #1e293b;
}

[data-testid="stMetricValue"] {
    font-size: 2rem;
    font-weight: 700;
    color: #38bdf8;
}

/* ---------------- Sidebar ---------------- */
section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #f8fafc;
}

section[data-testid="stSidebar"] p {
    color: #cbd5e1;
}

/* ---------------- Info Box ---------------- */
.stAlert {
    background-color: #020617;
    border: 1px solid #1e293b;
    color: #e5e7eb;
}

/* ---------------- Footer ---------------- */
.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 0.85rem;
    padding: 2.5rem 1rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    st.title("SmartHomes AI")
    st.divider()

    st.markdown("### Model Overview")
    st.write("Prediction Task: Residential House Prices")
    st.write("Machine Learning Model: Linear Regression")
    st.write("Total Input Features: 13")

    st.divider()
    st.markdown("### Model Performance")
    st.write("R² Score: 0.65")
    st.write("Prediction Latency: < 1 second")

# ---------------------------------
# Hero Section
# ---------------------------------
st.markdown("""
<div class="main-header">
    <h1>SmartHomes AI</h1>
    <p>
        A machine learning–based platform for accurate residential house price prediction
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------
# About Section
# ---------------------------------
st.markdown("## About the System")

st.write("""
SmartHomes AI is a data-driven web application developed to estimate residential house prices
based on multiple property characteristics. The system uses historical housing data and machine
learning techniques to model the relationship between property features and market value.

By applying a Linear Regression model, the platform delivers transparent and interpretable
predictions, making it suitable for academic use, experimentation, and practical decision support.
""")

# ---------------------------------
# Problem Motivation
# ---------------------------------
st.markdown("## Why House Price Prediction Matters")

st.write("""
Estimating house prices accurately is a challenging task due to the number of variables involved,
such as location, size, number of rooms, and overall quality. Traditional estimation methods often
rely on subjective judgment and limited comparisons.

Machine learning enables the system to learn patterns from historical data and produce consistent,
objective predictions based on measurable attributes. This approach improves reliability and
reduces human bias in valuation.
""")

# ---------------------------------
# Features Section
# ---------------------------------
st.markdown("## Key Platform Capabilities")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>Data-Driven Predictions</h3>
        <p>
            The model is trained on structured housing datasets and captures relationships
            between input features and property prices.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>Efficient Model Execution</h3>
        <p>
            Linear Regression allows fast computation, enabling near-instant price predictions
            after user input.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>Simple and Transparent Design</h3>
        <p>
            The system prioritizes clarity and usability, allowing users to understand and trust
            the prediction results.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------
# Model Statistics
# ---------------------------------
st.markdown("## Model Statistics")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Input Features", "13")
with m2:
    st.metric("Model Type", "Linear Regression")
with m3:
    st.metric("Model Accuracy", "65% (R²)")
with m4:
    st.metric("Prediction Time", "< 1 second")

# ---------------------------------
# How It Works
# ---------------------------------
st.markdown("## Prediction Workflow")

st.write("""
1. **User Input**  
   The user enters property details such as floor area, number of rooms, and location-related attributes.

2. **Feature Processing**  
   Inputs are validated and transformed into the format required by the trained model.

3. **Price Estimation**  
   The Linear Regression model processes the inputs and computes the predicted house price.

4. **Result Display**  
   The predicted value is presented clearly to support informed decision-making.
""")

# ---------------------------------
# Call to Action
# ---------------------------------
st.markdown("## Start Predicting")

st.info(
    "Navigate to the predictor page using the sidebar to enter property details "
    "and generate a house price estimate."
)

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("""
<div class="footer">
    <p>Built using Streamlit and Scikit-learn</p>
    <p>SmartHomes AI © 2024</p>
</div>
""", unsafe_allow_html=True)
