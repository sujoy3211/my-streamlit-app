import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# -----------------------------
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
except Exception as e:
    st.error(f"Failed to load the model: {e}")
    st.stop()

# -----------------------------
# Streamlit UI
st.title("Rainfall Prediction App")
st.write("Predict rainfall based on weather parameters.")

# Input form
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
pressure = st.number_input("Pressure (hPa)")

# Predict button
if st.button("Predict Rainfall"):
    try:
        input_data = np.array([[temperature, humidity, pressure]])
        prediction = model.predict(input_data)
        st.success(f"Predicted Rainfall: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

