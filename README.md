# 📊 Customer Churn Prediction

## 📌 Project Overview

Customer Churn Prediction is a Machine Learning project that predicts whether a customer is likely to leave a service.

The project analyzes customer demographic information, service usage, contract details, payment methods, and billing information to identify customers who are at risk of churning.

This project was developed as part of an internship project.

---

## 🎯 Objective

The main objective of this project is to build a classification model that can predict customer churn and identify customers who may be at risk of leaving a service.

The project focuses on:

- Understanding customer churn patterns
- Performing Exploratory Data Analysis
- Cleaning and preprocessing customer data
- Training a Machine Learning classification model
- Evaluating model performance
- Predicting churn probability
- Building an interactive Streamlit application

---

## 📂 Dataset

The project uses a customer churn dataset containing information about customer demographics, services, contracts, payment methods, and charges.

Important features include:

- Gender
- Senior Citizen
- Partner
- Dependents
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
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

The target variable is:

**Churn**

where:

- `1` represents customer churn
- `0` represents customer retention

---

## 🔎 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the dataset and identify important churn patterns.

The analysis included:

- Dataset structure
- Missing value analysis
- Churn distribution
- Numerical feature analysis
- Categorical feature analysis
- Customer tenure analysis
- Monthly charges analysis
- Contract type analysis
- Correlation analysis

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Removed unnecessary columns
2. Handled missing values
3. Converted categorical variables
4. Prepared numerical features
5. Applied feature preprocessing
6. Split the dataset into training and testing sets

---

## 🤖 Machine Learning Model

A classification model was trained to predict customer churn.

The project uses:

**Logistic Regression**

Logistic Regression was selected because it is a suitable classification algorithm for predicting binary outcomes such as churn and non-churn.

---

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy
- Recall
- ROC-AUC
- Confusion Matrix

These evaluation metrics help measure how effectively the model identifies customers who are likely to churn.

---

## 🌐 Streamlit Web Application

An interactive Streamlit application was developed for real-time customer churn prediction.

The application allows users to enter customer information such as:

- Customer demographics
- Tenure
- Internet services
- Contract
- Payment method
- Monthly charges
- Total charges

The application then provides:

- Churn prediction
- Churn probability
- Risk level
- Customer retention recommendation

---

## 📸 Application

Screenshots of the application are stored in the `images` folder.

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
│
├── models/
│   ├── churn_model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   └── Customer_Churn.ipynb
│
├── report/
│
├── .gitignore
├── README.md
└── requirements.txt