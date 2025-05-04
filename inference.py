import streamlit as st
import numpy as np
import joblib
# import pickle

# Load model, scaler, and feature column names
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
features = joblib.load('features.pkl')

# model = pickle.load(open('model.pkl','rb'))
# scaler = pickle.load(open('scaler.pkl','rb'))
# features = pickle.load(open('features.pkl','rb'))

st.title("🌍 WHO Life Expectancy Predictor")

st.markdown("### Enter the required features:")

# Dynamically create input fields for each feature
user_input = []
for feature in features:
    value = st.text_input(f"{feature}", placeholder="Enter a numeric value")
    user_input.append(value)

# Predict button
if st.button("Predict"):
    try:
        # Convert input to float and check for missing fields
        input_data = np.array([float(x) for x in user_input]).reshape(1, -1)

        # Apply the saved scaler
        scaled_input = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(scaled_input)

        st.success(f"🧬 Predicted Life Expectancy: **{prediction[0]:.2f}** years")

    except ValueError:
        st.error("❌ Please enter valid numeric values for all fields.")
