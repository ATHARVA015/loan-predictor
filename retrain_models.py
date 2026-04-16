"""
Retrain all models with current scikit-learn version
This ensures compatibility with the current environment
"""

import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import RidgeClassifier
from sklearn.feature_selection import RFE
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif

print("=" * 60)
print("RETRAINING MODELS")
print("=" * 60)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load and preprocess data
print("\n1. Loading and preprocessing data...")
df = pd.read_csv(os.path.join(BASE_DIR, 'Loan_Data.csv'))

# Drop Loan_ID
df = df.drop(['Loan_ID'], axis=1)

# Convert categorical to numeric
df['Gender'] = df['Gender'].replace({'Male': 0, 'Female': 1})
df['Married'] = df['Married'].replace({'No': 0, 'Yes': 1})
df['Dependents'] = df['Dependents'].replace({'0': 0, '1': 1, '2': 2, '3+': 3})
df['Education'] = df['Education'].replace({'Not Graduate': 0, 'Graduate': 1})
df['Self_Employed'] = df['Self_Employed'].replace({'No': 0, 'Yes': 1})
df['Property_Area'] = df['Property_Area'].replace({'Rural': 0, "Semiurban": 1, "Urban": 2})
df['Loan_Status'] = df['Loan_Status'].replace({"N": 0, "Y": 1})

# Drop null values
df = df.dropna()
print(f"   Data shape: {df.shape}")

# Prepare features and target
y = df['Loan_Status'].astype(int)
X = df.drop(['Loan_Status'], axis=1)

print("\n2. Training Baseline Model (all 11 features)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=109)

baseline_clf = RidgeClassifier()
baseline_clf.fit(X_train, y_train)

y_pred = baseline_clf.predict(X_test)
baseline_acc = metrics.accuracy_score(y_test, y_pred)
print(f"   Baseline Accuracy: {baseline_acc:.4f}")

# Save baseline model
joblib.dump(baseline_clf, os.path.join(BASE_DIR, 'reg_clf.pkl'))
print("   ✓ Saved: reg_clf.pkl")

print("\n3. Training RFE Model (6 selected features)...")
rfe = RFE(estimator=RidgeClassifier(), n_features_to_select=6, step=1)
X_rfe = rfe.fit_transform(X_train, y_train)

rfe_clf = RidgeClassifier()
rfe_clf.fit(X_rfe, y_train)

X_test_rfe = rfe.transform(X_test)
y_pred_rfe = rfe_clf.predict(X_test_rfe)
rfe_acc = metrics.accuracy_score(y_test, y_pred_rfe)
print(f"   RFE Accuracy: {rfe_acc:.4f}")

# Get selected features
rfe_selected = X.columns[rfe.support_]
print(f"   Selected features: {list(rfe_selected)}")

# Save RFE model
joblib.dump(rfe_clf, os.path.join(BASE_DIR, 'rfe_clf.pkl'))
print("   ✓ Saved: rfe_clf.pkl")

print("\n4. Training PCA Model (5 components)...")
pca = PCA(n_components=5)
X_pca = pca.fit_transform(X_train)

pca_clf = RidgeClassifier()
pca_clf.fit(X_pca, y_train)

X_test_pca = pca.transform(X_test)
y_pred_pca = pca_clf.predict(X_test_pca)
pca_acc = metrics.accuracy_score(y_test, y_pred_pca)
print(f"   PCA Accuracy: {pca_acc:.4f}")

# Save PCA model
joblib.dump(pca_clf, os.path.join(BASE_DIR, 'pca_clf.pkl'))
print("   ✓ Saved: pca_clf.pkl")

# Save processed data for PCA transformation
df.to_csv(os.path.join(BASE_DIR, 'Loan_Data_df.csv'), index=False)
print("   ✓ Saved: Loan_Data_df.csv")

print("\n" + "=" * 60)
print("MODEL SUMMARY")
print("=" * 60)
print(f"Baseline Model:  {baseline_acc:.4f} (79.17% expected)")
print(f"RFE Model:       {rfe_acc:.4f} (83.33% expected)")
print(f"PCA Model:       {pca_acc:.4f} (71.53% expected)")
print("\n✓ All models retrained and saved successfully!")
print("=" * 60)
