import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_data
def load_model():
    return joblib.load("model.joblib")

model = load_model()

# App title
st.title("Diabetes Prediction App")

# User input form
st.header("Enter Patient Data:")
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
glucose = st.number_input("Glucose", min_value=0, max_value=200, step=1)
bp = st.number_input("Blood Pressure", min_value=0, max_value=150, step=1)
skin = st.number_input("Skin Thickness", min_value=0, max_value=100, step=1)
insulin = st.number_input("Insulin", min_value=0, max_value=900, step=1)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, step=0.1)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, step=0.01)
age = st.number_input("Age", min_value=0, max_value=120, step=1)

# Predict
if st.button("Predict"):
    input_data = pd.DataFrame([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]],
                               columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI",
                                        "DiabetesPedigreeFunction", "Age"])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("The patient is likely to have diabetes.")
    else:
        st.success("The patient is unlikely to have diabetes.")
