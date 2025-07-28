# Loan Eligibility Predictor

This project predicts loan approval chances based on applicant information such as income, credit history, and property area. It is part of the CST2216 course at Algonquin College.

## 🎯 Project Overview

- 🔍 Uses historical loan application data to train a machine learning model
- 📊 Processes and cleans user input for real-time prediction
- 🧠 Trained with `RandomForestClassifier`
- 🌐 Deployed using Streamlit for interactive input and output

## 📁 Project Structure

Loan_Eligibility_Predictor/
│
├── data/
│ └── credit.csv
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ ├── model.py
│ └── utils.py
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
└── config.toml


## ⚙️ How to Run

1. Clone this repo  
2. Install dependencies:

```bash
pip install -r requirements.txt
streamlit run app.py
📘 Dataset
File: credit.csv

Source: Historical loan applications dataset

Target variable: Loan_Status (Y or N)

📦 Features Used
Gender, Married, Education, Self_Employed

Applicant & Coapplicant Income

LoanAmount, Loan_Amount_Term, Credit_History

Property_Area

📌 Output
Approves or denies a hypothetical loan application based on inputs

Displays prediction with success message