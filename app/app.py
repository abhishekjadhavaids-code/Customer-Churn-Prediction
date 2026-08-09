import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Load Model and Preprocessor
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(
    os.path.join(BASE_DIR, "models", "churn_model.pkl")
)

preprocessor = joblib.load(
    os.path.join(BASE_DIR, "models", "preprocessor.pkl")
)

# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------

st.markdown(
    '<div class="main-title">📊 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict whether a customer is likely to churn using Machine Learning</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Customer Input
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )


with col2:

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        max_value=200.0,
        value=50.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        max_value=10000.0,
        value=500.0
    )

# -----------------------------
# Prediction Button
# -----------------------------

st.markdown("---")

button_col1, button_col2, button_col3 = st.columns([1, 2, 1])

with button_col2:

    predict_button = st.button(
        "🔍 Predict Churn",
        use_container_width=True
    )

# -----------------------------
# Prediction
# -----------------------------

if predict_button:

    customer_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [senior_citizen],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone_service],
        "MultipleLines": [multiple_lines],
        "InternetService": [internet_service],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless_billing],
        "PaymentMethod": [payment_method],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges]
    })

    customer_processed = preprocessor.transform(customer_data)

    prediction = model.predict(customer_processed)

    probability = model.predict_proba(customer_processed)[0][1]

    # -----------------------------
    # Prediction Result
    # -----------------------------

    st.markdown("---")

    st.subheader("📌 Prediction Result")

    if prediction[0] == 1:

        st.error(
            "⚠️ Customer is likely to CHURN."
        )

    else:

        st.success(
            "✅ Customer is likely to STAY."
        )

    # -----------------------------
    # Churn Probability
    # -----------------------------

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )

    st.progress(probability)

    # -----------------------------
    # Risk Level
    # -----------------------------

    if probability < 0.30:

        risk_level = "LOW"

        st.success(
            "🟢 Risk Level: LOW"
        )

        st.info(
            "Customer has a low risk of churn."
        )

        st.write(
            "Recommendation: Continue providing good service and maintain customer engagement."
        )

    elif probability < 0.60:

        risk_level = "MEDIUM"

        st.warning(
            "🟠 Risk Level: MEDIUM"
        )

        st.warning(
            "Customer has a moderate risk of churn."
        )

        st.write(
            "Recommendation: Consider offering personalized support, discounts, or service improvements."
        )

    else:

        risk_level = "HIGH"

        st.error(
            "🔴 Risk Level: HIGH"
        )

        st.error(
            "Customer has a high risk of churn."
        )

        st.write(
            "Recommendation: Immediate customer retention action is recommended."
        )

    # -----------------------------
    # Customer Summary
    # -----------------------------

    st.markdown("---")

    st.subheader("📋 Customer Summary")

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:

        st.write("**Contract:**", contract)

        st.write("**Tenure:**", f"{tenure} months")

    with summary_col2:

        st.write(
            "**Monthly Charges:**",
            f"${monthly_charges:.2f}"
        )

        st.write(
            "**Total Charges:**",
            f"${total_charges:.2f}"
        )

    with summary_col3:

        st.write(
            "**Internet Service:**",
            internet_service
        )

        st.write(
            "**Payment Method:**",
            payment_method
        )

# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption(
    "Customer Churn Prediction | Machine Learning Project"
)