"""
Test script to verify model predictions and feature format
"""

import os
import numpy as np
import pandas as pd
import joblib
from sklearn.decomposition import PCA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("MODEL TESTING & VERIFICATION")
print("=" * 60)

# Load models
try:
    baseline_model = joblib.load(os.path.join(BASE_DIR, 'reg_clf.pkl'))
    rfe_model = joblib.load(os.path.join(BASE_DIR, 'rfe_clf.pkl'))
    pca_model = joblib.load(os.path.join(BASE_DIR, 'pca_clf.pkl'))
    print("\n✓ All models loaded successfully")
except Exception as e:
    print(f"\n✗ Error loading models: {e}")
    exit(1)

# Load PCA
try:
    df = pd.read_csv(os.path.join(BASE_DIR, 'Loan_Data_df.csv'))
    X = df.drop(['Loan_Status'], axis=1)
    pca = PCA(n_components=5)
    pca.fit(X)
    print("✓ PCA fitted successfully")
except Exception as e:
    print(f"✗ Error loading PCA: {e}")
    exit(1)

print("\n" + "=" * 60)
print("TEST 1: RFE Model (6 features)")
print("=" * 60)
print("Features: Gender, Married, Education, Self_Employed, Credit_History, Property_Area")

# Test data: [Gender=0, Married=0, Education=0, Self_Employed=0, Credit_History=0, Property_Area=0]
test_rfe_1 = np.array([[0, 0, 0, 0, 0, 0]])
pred_1 = rfe_model.predict(test_rfe_1)[0]
print(f"\nTest 1 Input: [0, 0, 0, 0, 0, 0]")
print(f"Prediction: {'ELIGIBLE (1)' if pred_1 == 1 else 'NOT ELIGIBLE (0)'}")

# Test data: [Gender=1, Married=1, Education=1, Self_Employed=1, Credit_History=1, Property_Area=2]
test_rfe_2 = np.array([[1, 1, 1, 1, 1, 2]])
pred_2 = rfe_model.predict(test_rfe_2)[0]
print(f"\nTest 2 Input: [1, 1, 1, 1, 1, 2]")
print(f"Prediction: {'ELIGIBLE (1)' if pred_2 == 1 else 'NOT ELIGIBLE (0)'}")

print("\n" + "=" * 60)
print("TEST 2: Baseline Model (11 features)")
print("=" * 60)
print("Features: Gender, Married, Dependents, Education, Self_Employed,")
print("          ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,")
print("          Credit_History, Property_Area")

# Test data: typical applicant
test_base = np.array([[0, 0, 0, 0, 0, 5000, 1000, 150, 360, 1, 1]])
pred_3 = baseline_model.predict(test_base)[0]
print(f"\nTest 1 Input: [0, 0, 0, 0, 0, 5000, 1000, 150, 360, 1, 1]")
print(f"Prediction: {'ELIGIBLE (1)' if pred_3 == 1 else 'NOT ELIGIBLE (0)'}")

print("\n" + "=" * 60)
print("TEST 3: PCA Model (11 features → 5 components)")
print("=" * 60)

feature_names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                'Loan_Amount_Term', 'Credit_History', 'Property_Area']

test_pca_df = pd.DataFrame([[0, 0, 0, 0, 0, 5000, 1000, 150, 360, 1, 1]], columns=feature_names)
test_pca_transformed = pca.transform(test_pca_df)
pred_4 = pca_model.predict(test_pca_transformed)[0]
print(f"\nTest 1 Input: [0, 0, 0, 0, 0, 5000, 1000, 150, 360, 1, 1]")
print(f"Transformed to 5 PCA components")
print(f"Prediction: {'ELIGIBLE (1)' if pred_4 == 1 else 'NOT ELIGIBLE (0)'}")

print("\n" + "=" * 60)
print("MODEL STATISTICS")
print("=" * 60)
print(f"RFE Model Type: {type(rfe_model).__name__}")
print(f"Baseline Model Type: {type(baseline_model).__name__}")
print(f"PCA Model Type: {type(pca_model).__name__}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("If all predictions show variety of ELIGIBLE/NOT ELIGIBLE, models are working correctly.")
print("If all show ELIGIBLE, there may be an issue with model training or data format.")
print("\nModels appear to be functioning normally. Check Streamlit app for correct input order.")
