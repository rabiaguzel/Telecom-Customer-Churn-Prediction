import streamlit as st
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="Churn Prediction", layout="centered")

st.markdown("<h1 style='text-align: center;'>📞 Telecom Customer Churn Prediction</h1>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("1️⃣ Customer Information")
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", [0, 1], format_func=lambda x: {0: "Female", 1: "Male"}[x])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", [0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])
    dependents = st.selectbox("Dependents", [0, 1], format_func=lambda x: {0: "No", 1: "Yes"}[x])
    tenure = st.slider("Tenure (months)", 0, 100, 24)

with col2:
    phone_service = st.selectbox("Phone Service", [0, 1])
    multiple_lines = st.selectbox("Multiple Lines", [0, 1, 2], format_func=lambda x: {0: "No phone service", 1: "No", 2: "Yes"}[x])
    internet_service = st.selectbox("Internet Service", [0, 1, 2], format_func=lambda x: {0: "DSL", 1: "Fiber optic", 2: "No"}[x])
    online_security = st.selectbox("Online Security", [0, 1, 2], format_func=lambda x: {0: "No", 1: "Yes", 2: "No internet"}[x])
    online_backup = st.selectbox("Online Backup", [0, 1, 2], format_func=lambda x: {0: "No", 1: "Yes", 2: "No internet"}[x])

st.markdown("---")
st.subheader("2️⃣ Additional Services")
col3, col4 = st.columns(2)
with col3:
    device_protection = st.selectbox("Device Protection", [0, 1, 2])
    tech_support = st.selectbox("Tech Support", [0, 1, 2])
    streaming_tv = st.selectbox("Streaming TV", [0, 1, 2])
    streaming_movies = st.selectbox("Streaming Movies", [0, 1, 2])

with col4:
    contract = st.selectbox("Contract", [0, 1, 2])
    paperless_billing = st.selectbox("Paperless Billing", [0, 1])
    payment_method = st.selectbox("Payment Method", [0, 1, 2, 3])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=1000.0)

monthly_to_total_ratio = round(monthly_charges / (total_charges + 1e-5), 4)
multiple_lines_binary = 0 if multiple_lines == 0 else 1
is_paperless_billing = paperless_billing
payment_method_encoded = payment_method

st.markdown("---")

#Predict Button
if st.button("🎯 Predict Churn"):
    input_data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "Monthly_to_TotalRatio": monthly_to_total_ratio,
        "MultipleLines_binary": multiple_lines_binary,
        "IsPaperlessBilling": is_paperless_billing,
        "PaymentMethodEncoded": payment_method_encoded
    }

    try:
        response = requests.post("http://api:5000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]
            probability = result["probability"]

            if prediction == 1:
                st.error("⚠️ Prediction: Customer WILL Churn")
            else:
                st.success("✅ Prediction: Customer will NOT Churn")

            st.metric("Churn Probability", f"{round(probability * 100, 2)}%")

            
            labels = ['No Churn', 'Churn']
            sizes = [1 - probability, probability]
            colors = ['green', 'red']
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
            ax.axis("equal")
            st.pyplot(fig)
        else:
            st.warning("⚠️ API did not respond as expected.")
    except:
        st.error("❌ API Connection Failed. Is your Flask backend running?")
