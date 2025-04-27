# file: project8_bmi_calculator.py

import streamlit as st

# Page Settings
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        .bmi-title {
            text-align: center;
            font-size: 48px;
            color: #4CAF50;
            font-weight: bold;
        }
        .bmi-result {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #FF5722;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='bmi-title'>⚖️ BMI Calculator</div>", unsafe_allow_html=True)
st.divider()

# Input Fields
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("Enter your height (in cm):", min_value=50, max_value=250, value=170)
with col2:
    weight = st.number_input("Enter your weight (in kg):", min_value=10, max_value=300, value=70)

st.divider()

# Calculate Button
if st.button("Calculate BMI 🧮"):
    height_m = height / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)
    bmi = round(bmi, 2)

    # Display BMI
    st.markdown(f"<div class='bmi-result'>Your BMI is: {bmi}</div>", unsafe_allow_html=True)

    # BMI Category
    if bmi < 18.5:
        st.info("⚠️ You are **Underweight**.")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ You are in **Healthy Weight** range.")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ You are **Overweight**.")
    else:
        st.error("⚠️ You are in **Obesity** range.")

    # Bonus Tip
    st.divider()
    st.caption("💡 Tip: A healthy BMI is between 18.5 and 24.9.")

