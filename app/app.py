import streamlit as st
import pandas as pd
import joblib
import os

from pathlib import Path
# import joblib

model_path = Path(__file__).parent / 'model' / 'churn_model.pkl'
model, feature_names = joblib.load(model_path)

st.title("📊 Telco Customer Churn Prediction App")
st.write("Predict whether a customer will churn or not based on their details.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", 0, 72)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0)

input_dict = {
    'gender': [1 if gender == 'Male' else 0],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [1 if Partner == 'Yes' else 0],
    'Dependents': [1 if Dependents == 'Yes' else 0],
    'tenure': [tenure],
    'PhoneService': [1 if PhoneService == 'Yes' else 0],
    'MultipleLines': [1 if MultipleLines == 'Yes' else 0],
    'InternetService': [0 if InternetService == 'DSL' else (1 if InternetService == 'Fiber optic' else 2)],
    'OnlineSecurity': [1 if OnlineSecurity == 'Yes' else 0],
    'OnlineBackup': [1 if OnlineBackup == 'Yes' else 0],
    'DeviceProtection': [1 if DeviceProtection == 'Yes' else 0],
    'TechSupport': [1 if TechSupport == 'Yes' else 0],
    'StreamingTV': [1 if StreamingTV == 'Yes' else 0],
    'StreamingMovies': [1 if StreamingMovies == 'Yes' else 0],
    'Contract': [0 if Contract == 'Month-to-month' else (1 if Contract == 'One year' else 2)],
    'PaperlessBilling': [1 if PaperlessBilling == 'Yes' else 0],
    'PaymentMethod': [0 if PaymentMethod == 'Electronic check' else (
        1 if PaymentMethod == 'Mailed check' else (2 if PaymentMethod == 'Bank transfer (automatic)' else 3)
    )],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]
}

input_data = pd.DataFrame(input_dict)
input_data = input_data[feature_names]

if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    st.subheader("🎯 Prediction Result")
    if prediction == 1:
        st.error("⚠️ The customer is likely to CHURN!")
    else:
        st.success("✅ The customer is likely to STAY!")