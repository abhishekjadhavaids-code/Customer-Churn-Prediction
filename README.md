# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a customer is likely to **churn** or **stay** based on their demographic, service, contract, and billing information.

The project includes a trained Machine Learning model and an interactive **Streamlit web application** for making customer churn predictions.

---

## 🚀 Project Overview

Customer churn is an important problem for subscription-based businesses.

This project uses customer information such as:

- Gender
- Senior Citizen status
- Partner and Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming Services
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

The trained model predicts:

- **Customer is likely to STAY**
- **Customer is likely to CHURN**

It also displays the **churn probability** and risk level.

---

## 🎯 Features

- Interactive Streamlit web application
- Customer churn prediction
- Churn probability calculation
- Churn risk interpretation
- Pre-trained Machine Learning model
- Data preprocessing pipeline
- User-friendly customer information form

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

---

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├── app/
│   ├── app.py
│   └── app_backup.py
│
├── dataset/
│   ├── churn.csv
│   └── churn_cleaned.csv
│
├── models/
│   ├── churn_model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   └── Customer_Churn.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt