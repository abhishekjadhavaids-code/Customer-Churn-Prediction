# 📊 Customer Churn Prediction

🌐 **Live Demo:** https://customer-churn-predictor-project.streamlit.app/

A Machine Learning project that predicts whether a customer is likely to **churn** or **stay** based on their demographic, service, contract, and billing information.

The project includes a trained Machine Learning model, data preprocessing pipeline, Jupyter Notebook, and an interactive **Streamlit web application** for making customer churn predictions.

---

## 🚀 Project Overview

Customer churn is an important problem for subscription-based businesses. Identifying customers who are likely to leave can help businesses take appropriate retention actions.

This project uses customer information such as:

- Gender
- Senior Citizen status
- Partner and Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

The trained Machine Learning model predicts:

- **Customer is likely to STAY**
- **Customer is likely to CHURN**

The application also displays the **churn probability** and **risk level**.

---

## 🎯 Features

- Interactive Streamlit web application
- Customer churn prediction
- Churn probability calculation
- Churn risk interpretation
- Pre-trained Machine Learning model
- Saved preprocessing pipeline
- User-friendly customer information form
- Jupyter Notebook containing the Machine Learning workflow
- Local deployment using Streamlit

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git
- GitHub

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
├── images/
│   └── churn_prediction.png
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