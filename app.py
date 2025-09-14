import streamlit as st
import requests

st.title("🌱 Sustainable Farming Advisor")

# Input farmer details
st.header("Enter Farmer Details")
name = st.text_input("Farmer Name")
location = st.text_input("Location")
soil_type = st.selectbox("Soil Type", ["loamy", "clay", "sandy"])
rainfall = st.number_input("Average Rainfall (mm)", min_value=0)
budget = st.number_input("Budget (USD)", min_value=0)

if st.button("Get Recommendation"):
    try:
        # Call backend API
        response = requests.post(
            "http://127.0.0.1:8000/recommend",
            json={
                "name": name,
                "location": location,
                "soil_type": soil_type,
                "avg_rainfall_mm": rainfall,
                "budget_usd": budget
            }
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"Recommended Crop: {result['crop']}")
        else:
            st.error("Error from backend API")
    except Exception as e:
        st.error(f"Could not connect to backend: {e}")
