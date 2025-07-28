from sklearn.model_selection import train_test_split

def preprocess_data(df):
    # Drop missing values
    df = df.dropna()

    # Encode categorical variables (basic example)
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
    df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
    df['Self_Employed'] = df['Self_Employed'].map({'Yes': 1, 'No': 0})
    df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

    # Select features and target
    X = df[['Gender', 'Married', 'Education', 'ApplicantIncome', 'LoanAmount']]
    y = df['Loan_Status']

    return train_test_split(X, y, test_size=0.2, random_state=42)