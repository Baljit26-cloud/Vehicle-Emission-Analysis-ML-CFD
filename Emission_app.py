import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and feature names
# Ensure these files are in the same directory as app.py
try:
    model = joblib.load('random_forest_model.pkl')
    features = joblib.load('model_features.pkl')
except FileNotFoundError:
    st.error("Model files not found. Please ensure 'random_forest_model.pkl' and 'model_features.pkl' are in the app directory.")

# Page Configuration
st.set_page_config(page_title="Vehicle CO2 Emission Predictor", layout="centered")

st.title("Vehicle CO2 Emission Predictor")
st.markdown("This application predicts CO2 emissions based on vehicle engine and fuel consumption specifications.")

st.sidebar.header("Input Vehicle Specifications")

def get_user_inputs():
    # User inputs based on the top 5 features used in your training script
    engine_size = st.sidebar.number_input("Engine Size (L)", min_value=0.5, max_value=10.0, value=2.0, step=0.1)
    cylinders = st.sidebar.slider("Cylinders", min_value=2, max_value=16, value=4)
    city_fuel = st.sidebar.number_input("Fuel Consumption City (L/100 km)", min_value=1.0, value=9.5)
    hwy_fuel = st.sidebar.number_input("Fuel Consumption Hwy (L/100 km)", min_value=1.0, value=6.8)
    comb_fuel = st.sidebar.number_input("Fuel Consumption Comb (L/100 km)", min_value=1.0, value=8.3)
    
    input_dict = {
        'Engine Size(L)': engine_size,
        'Cylinders': cylinders,
        'Fuel Consumption City (L/100 km)': city_fuel,
        'Fuel Consumption Hwy (L/100 km)': hwy_fuel,
        'Fuel Consumption Comb (L/100 km)': comb_fuel
    }
    
    return pd.DataFrame(input_dict, index=[0])

# Collect input data
df_input = get_user_inputs()

st.subheader("Selected Specifications")
st.write(df_input)

# Prediction Logic
if st.button("Predict Emission"):
    prediction = model.predict(df_input)
    result = round(prediction[0], 2)
    
    st.header(f"Predicted CO2 Emission: {result} g/km")
    
    # Comparison with BMW target threshold
    target_threshold = 210.25
    if result <= target_threshold:
        st.info(f"The predicted value is within the acceptable target range of {target_threshold} g/km.")
    else:
        st.warning(f"The predicted value exceeds the target threshold of {target_threshold} g/km.")

st.markdown("---")
st.caption("Model trained on Canadian Vehicle CO2 Emission dataset.")