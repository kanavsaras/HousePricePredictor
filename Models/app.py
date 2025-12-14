import os
import streamlit as st
import pandas as pd
import pickle
import numpy as np

@st.cache_resource
def load_model():
    base_dir = os.path.dirname(__file__)
    model_path = os.path.join(base_dir, "house_price_model.pkl")

    with open(model_path, "rb") as f:
        return pickle.load(f)
model = load_model()
st.title("🏠 House Price Predictor")
st.write("Enter house details to get an estimated price")
col1, col2 = st.columns(2)

with col1:
    size = st.number_input(
        "Size (sqft)",
        min_value=500,
        max_value=10000,
        value=2000,
        step=100
    )
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3
    )
    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2
    )

with col2:
    age = st.number_input(
        "Age (years)",
        min_value=0,
        max_value=100,
        value=10
    )
    
    location_quality = st.slider(
        "Location Quality (1-10)",
        min_value=1,
        max_value=10,
        value=7
    )


if st.button("Predict Price", type="primary"):
    
    input_data = pd.DataFrame({
        'SquareFeet': [size],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Age': [age],
        'LocationScore': [location_quality]
    })
    
    
    prediction = model.predict(input_data)[0]
    
    
    st.success(f"### Estimated Price: ${prediction:,.2f}")
    
    
    margin = prediction * 0.1
    st.info(f"Typical range: ${prediction - margin:,.2f} - ${prediction + margin:,.2f}")
    
    
    with st.expander("📊 House Details You Entered"):
        st.dataframe(input_data)



st.markdown("-----")
st.caption("Model trained on 500 houses. Predictions are estimates only.")
