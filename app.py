import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Get the absolute path of the folder containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Full path to the model file
model_path = os.path.join(BASE_DIR, "rain_model.pkl")

# Load the model safely
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found! Make sure 'rain_model.pkl' is in the app folder.")
    st.stop()

st.title("Rainfall Prediction App")

# Example input form
st.header("Enter Weather Parameters:")
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
pressure = st.number_input("Pressure (hPa)")

# Prediction button
if st.button("Predict Rainfall"):
    try:
        # Assuming the model expects inputs as a 2D array
        input_data = np.array([[temperature, humidity, pressure]])
        prediction = model.predict(input_data)
        st.success(f"Predicted Rainfall: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
