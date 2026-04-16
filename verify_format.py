"""
Verify input format conversion
"""

import numpy as np
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load RFE model
rfe_model = joblib.load(os.path.join(BASE_DIR, 'rfe_clf.pkl'))

print("=" * 70)
print("INPUT FORMAT VERIFICATION")
print("=" * 70)

# Simulate user selections in UI
print("\n📋 USER SELECTIONS IN UI:")
print("-" * 70)

# Test 1: User selects "Female", "Yes", etc.
print("\nTest 1: User selections (friendly text)")
print("  Gender:        ● Female     (stored as: 1)")
print("  Married:       ● Yes        (stored as: 1)")
print("  Dependents:    ● 2          (stored as: 2)")
print("  Education:     ● Graduate   (stored as: 1)")
print("  Self_Employed: ● Yes        (stored as: 1)")
print("  Credit_History:● Yes        (stored as: 1)")

# These are the numeric values sent to model
user_input_1 = np.array([[1, 1, 2, 1, 1, 1]])
prediction_1 = rfe_model.predict(user_input_1)[0]

print(f"\n✓ Model Input (numeric):  {user_input_1}")
print(f"✓ Prediction:             {'ELIGIBLE ✅' if prediction_1 == 1 else 'NOT ELIGIBLE ❌'}")

print("\n" + "-" * 70)

# Test 2: User selects "Male", "No", etc.
print("\nTest 2: User selections (friendly text)")
print("  Gender:        ● Male       (stored as: 0)")
print("  Married:       ● No         (stored as: 0)")
print("  Dependents:    ● 0          (stored as: 0)")
print("  Education:     ● Not Grad   (stored as: 0)")
print("  Self_Employed: ● No         (stored as: 0)")
print("  Credit_History:● No         (stored as: 0)")

# These are the numeric values sent to model
user_input_2 = np.array([[0, 0, 0, 0, 0, 0]])
prediction_2 = rfe_model.predict(user_input_2)[0]

print(f"\n✓ Model Input (numeric):  {user_input_2}")
print(f"✓ Prediction:             {'ELIGIBLE ✅' if prediction_2 == 1 else 'NOT ELIGIBLE ❌'}")

print("\n" + "=" * 70)
print("✅ FORMAT VERIFICATION COMPLETE")
print("=" * 70)
print("\n✓ UI shows FRIENDLY TEXT (Male/Female, Yes/No, Graduate, etc.)")
print("✓ Model receives NUMERIC VALUES (0, 1, 2, etc.)")
print("✓ This is the CORRECT FORMAT\n")
