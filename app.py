import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("rain_model.pkl", "rb"))

st.title("🌧️ Rainfall Prediction System")
st.write("Enter today's weather data to predict if it will rain tomorrow.")

MinTemp = st.number_input("Minimum Temperature (°C)", value=15.0)
MaxTemp = st.number_input("Maximum Temperature (°C)", value=25.0)
Rainfall = st.number_input("Rainfall Today (mm)", value=0.0)
Humidity3pm = st.number_input("Humidity at 3 PM (%)", value=60.0)
Pressure9am = st.number_input("Pressure at 9 AM (hPa)", value=1010.0)
Temp3pm = st.number_input("Temperature at 3 PM (°C)", value=22.0)

if st.button("Predict"):
    data = np.array([[MinTemp, MaxTemp, Rainfall, Humidity3pm, Pressure9am, Temp3pm]])
    output = model.predict(data)[0]
    
    if output == "Yes":
        st.error("🌧️ Rain is likely tomorrow!")
    else:
        st.success("☀️ No rain expected tomorrow.")
