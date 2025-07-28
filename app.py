import streamlit as st
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model
from src.utils import configure_logging

configure_logging()

st.title("Loan Eligibility Predictor")

# Load data
df = load_data("data/credit.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Preprocess and train
X_train, X_test, y_train, y_test = preprocess_data(df)
model = train_model(X_train, y_train)
st.success("Model trained successfully!")

# Simple prediction input
st.subheader("Check Eligibility")
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income = st.number_input("Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)

if st.button("Predict"):
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0
    education = 1 if education == "Graduate" else 0
    self_employed = 1 if self_employed == "Yes" else 0

    input_data = [[gender, married, education, income, loan_amount]]
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Denied ❌")
