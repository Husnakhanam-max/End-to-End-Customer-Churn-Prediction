import streamlit as st
import joblib
import pandas as pd
import os

# Load model safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "customer_churn_model.joblib")

model = joblib.load(MODEL_PATH)

# App Title
st.title("📊 Telecom Customer Churn Predictor")
st.write("Enter customer details to predict churn risk.")

# User Inputs
tenure = st.number_input("Tenure (Months)", min_value=0, value=12)

monthly_charges = st.number_input(
    "Monthly Charges ($)",
    min_value=0.0,
    value=50.0
)

total_charges = st.number_input(
    "Total Charges ($)",
    min_value=0.0,
    value=600.0
)

support_calls = st.number_input(
    "Number of Support Calls",
    min_value=0,
    value=0
)

internet_service = st.selectbox(
    "Internet Service",
    ["Fiber", "DSL"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.selectbox(
    "Payment Method",
    ["Debit", "Credit", "Upi"]
)

# Prediction
if st.button("Analyze Customer Risk"):

    customer_data = pd.DataFrame([{
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges,
        "support_calls": support_calls,
        "internet_service": internet_service,
        "online_security": online_security,
        "tech_support": tech_support,
        "contract": contract,
        "payment_method": payment_method
    }])

    prediction = model.predict(customer_data)[0]

    probability = model.predict_proba(customer_data)[0][1]

    if prediction == 1:
        st.error(
            f"⚠️ High Churn Risk ({probability:.1%})"
        )
    else:
        st.success(
            f"✅ Customer Likely to Stay ({1-probability:.1%})"
        )

    st.write("### Customer Details")
    st.dataframe(customer_data)