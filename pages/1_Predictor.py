import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Predictor", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp{background:#0b1220;}
h1,h2,h3{color:#f1f5f9;}
label,p{color:#cbd5e1;}

.section{
    background:#020617;
    border:1px solid #1e293b;
    padding:2rem;
    border-radius:12px;
    margin-bottom:2rem;
}
            .stButton button {
    border-radius: 6px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load():
    with open("house_price_model.pkl","rb") as f:
        model = pickle.load(f)
    with open("feature_columns.pkl","rb") as f:
        columns = pickle.load(f)
    return model, columns

model, feature_columns = load()

# ---------------- HEADER ----------------
st.markdown("""
<div class="section">
<h1>House Price Prediction</h1>
<p>
Enter property characteristics below. The system will estimate the
market value based on the trained machine learning model.
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT FORM ----------------
with st.form("prediction_form"):

    st.markdown("## Structural Details")
    area = st.number_input("Area (sq ft)", 500, 20000, 3000, 100)
    bedrooms = st.selectbox("Bedrooms",[1,2,3,4,5])
    bathrooms = st.selectbox("Bathrooms",[1,2,3,4])
    stories = st.selectbox("Stories",[1,2,3,4])
    parking = st.selectbox("Parking Spaces",[0,1,2,3])

    st.markdown("## Amenities")
    mainroad = st.selectbox("Main Road Access",["yes","no"])
    guestroom = st.selectbox("Guest Room",["yes","no"])
    basement = st.selectbox("Basement",["yes","no"])
    hotwaterheating = st.selectbox("Hot Water Heating",["yes","no"])
    airconditioning = st.selectbox("Air Conditioning",["yes","no"])

    st.markdown("## Location & Preference")
    prefarea = st.selectbox("Preferred Area",["yes","no"])
    furnishingstatus = st.selectbox(
        "Furnishing Status",
        ["furnished","semi-furnished","unfurnished"]
    )

    submit = st.form_submit_button("Predict Price")

# ---------------- PREDICTION ----------------
if submit:
    raw_input = {
        "area":area,
        "bedrooms":bedrooms,
        "bathrooms":bathrooms,
        "stories":stories,
        "parking":parking,
        "mainroad":mainroad,
        "guestroom":guestroom,
        "basement":basement,
        "hotwaterheating":hotwaterheating,
        "airconditioning":airconditioning,
        "prefarea":prefarea,
        "furnishingstatus":furnishingstatus
    }

    df = pd.DataFrame([raw_input])
    df = pd.get_dummies(df)
    df = df.reindex(columns=feature_columns, fill_value=0)

    price = model.predict(df)[0]

    st.success(f"Estimated House Price: ${price:,.0f}")

    st.markdown("""
    **Note:**  
    This estimate is generated using a statistical model trained on historical
    housing data. Actual market prices may vary.
    """)
