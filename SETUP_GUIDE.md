# Loan Eligibility Prediction - Local Setup Guide

## Project Overview

This is a machine learning application that predicts loan eligibility based on applicant information. It uses three different models trained with different feature selection techniques.

### Three Models Available:

1. **Baseline Model** (`reg_clf.pkl`)
   - Uses all 11 features
   - Accuracy: 79.17%
   - Fastest prediction
   - Best for quick assessment

2. **RFE Model** (`rfe_clf.pkl`)
   - Uses 6 selected features (Gender, Married, Education, Self_Employed, Credit_History, Property_Area)
   - Accuracy: 83.33%
   - Best accuracy for feature-limited predictions
   - Less input required

3. **PCA Model** (`pca_clf.pkl`)
   - Uses 5 principal components (dimensionality reduction)
   - Variable accuracy (~71.5%)
   - Handles multicollinearity well
   - Requires all 11 original features

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Check Python Version:
```bash
python --version
# or
python3 --version
```

---

## Project Files Structure

```
Loan_Eligibility_Prediction/
├── app.py                           # Main local application (NEW)
├── index.py                         # Streamlit web application
├── Loan_Data.csv                    # Original dataset
├── Loan_Data_df.csv                 # Cleaned/preprocessed dataset
├── Loan_Prediction_Feature_Selection.ipynb  # Model training notebook
├── reg_clf.pkl                      # Baseline model
├── rfe_clf.pkl                      # RFE model
├── pca_clf.pkl                      # PCA model
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## Installation Steps

### Step 1: Navigate to Project Directory

```bash
cd path/to/Loan_Eligibility_Prediction
```

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- pandas (1.5.3) - Data manipulation
- numpy (1.26.4) - Numerical operations
- scikit-learn (1.2.2) - Machine learning
- joblib (1.1.1) - Model serialization
- streamlit (1.21.0) - Web interface (optional)

**Verify Installation:**
```bash
pip list
```

---

## Running the Application

### Option 1: Local CLI Application (NEW - Recommended)

```bash
python app.py
```

**Features:**
- Interactive menu-driven interface
- Choose between 3 different models
- Input validation
- Real-time predictions
- Accuracy information displayed

**Example Usage:**
```
Select prediction method:
1. Baseline Model (All 11 features)
2. RFE Model (6 selected features)
3. PCA Model (5 principal components)
4. Exit

Enter choice (1-4): 2
```

### Option 2: Streamlit Web Application

```bash
streamlit run index.py
```

Then open your browser to `http://localhost:8501`

---

## Feature Encoding Reference

### Gender:
- 0 = Male
- 1 = Female

### Married:
- 0 = No
- 1 = Yes

### Dependents:
- 0, 1, 2, or 3 (3 = 3 or more)

### Education:
- 0 = Not Graduate
- 1 = Graduate

### Self_Employed:
- 0 = No
- 1 = Yes

### Credit_History:
- 0 = No
- 1 = Yes

### Property_Area:
- 0 = Rural
- 1 = Semiurban
- 2 = Urban

---

## Model Details

### Data Preprocessing

1. **Categorical to Numeric Conversion:**
   - All categorical variables converted to numeric values (as shown above)
   
2. **Null Value Handling:**
   - Rows with missing values removed

3. **Feature Scaling:**
   - None applied (Ridge Classifier handles raw values)

### Input Features (Baseline/PCA):
1. Gender
2. Married
3. Dependents
4. Education
5. Self_Employed
6. ApplicantIncome
7. CoapplicantIncome
8. LoanAmount (values are in thousands)
9. Loan_Amount_Term (months)
10. Credit_History
11. Property_Area

### RFE Selected Features:
1. Gender
2. Married
3. Education
4. Self_Employed
5. Credit_History
6. Property_Area

### PCA Components:
- 5 principal components derived from all 11 original features

---

## Training Data

- **Source:** Kaggle - Eligibility Prediction for Loan
- **File:** `Loan_Data_df.csv` (preprocessed)
- **Total Records:** ~614 (after null removal)
- **Train-Test Split:** 70-30 (random_state=109)

---

## Troubleshooting

### Error: Module not found (pandas, numpy, etc.)

**Solution:** Make sure virtual environment is activated and dependencies are installed
```bash
pip install -r requirements.txt
```

### Error: "reg_clf.pkl not found"

**Solution:** Ensure all .pkl files are in the same directory as app.py
```bash
ls *.pkl  # On macOS/Linux
dir *.pkl # On Windows
```

### Error: "Loan_Data_df.csv not found" (for PCA)

**Solution:** This file is required for PCA model. Run the notebook first to generate it, or ensure it's in the project directory.

### Error: Permission denied when running app.py

**Solution:** On macOS/Linux, make script executable:
```bash
chmod +x app.py
python app.py
```

---

## Understanding Output

When you make a prediction, the output will show:

```
Model: RFE (6 Features)
Accuracy: 83.33%
Features: Gender, Married, Education, Self_Employed, Credit_History, Property_Area
----
PREDICTION: ELIGIBLE
Confidence: 0.2534
----
```

- **Accuracy:** Model's overall accuracy on test data
- **Prediction:** ELIGIBLE or NOT ELIGIBLE
- **Confidence:** Decision score (higher = more confident)

---

## Python Notebook

For detailed training process and model evaluation, see `Loan_Prediction_Feature_Selection.ipynb`

**Key sections:**
1. Data loading and exploration
2. Data preprocessing
3. Baseline model training
4. Feature selection techniques:
   - Chi-Square
   - RFE (Recursive Feature Elimination)
   - SelectKBest (CFS)
   - PCA (Principal Component Analysis)
   - MIFS (Mutual Information)
   - UFS (Univariate Feature Selection)
5. Model comparison and export

---

## Model Comparison

| Technique | Accuracy | Features | Speed | Best For |
|-----------|----------|----------|-------|----------|
| Baseline | 79.17% | 11 | Very Fast | Quick assessment |
| RFE | 83.33% | 6 | Fast | Balanced accuracy/efficiency |
| PCA | ~71.5% | 5 (components) | Medium | Handling collinearity |

---

## Next Steps

1. Run the application with different inputs
2. Compare predictions across models
3. Review the training notebook for detailed analysis
4. Modify hyperparameters in the notebook for fine-tuning
5. Deploy to cloud if needed (use Streamlit or Flask)

---

## Support

For issues with:
- **Data:** See the notebook for preprocessing details
- **Models:** Check the model files are not corrupted
- **Dependencies:** Reinstall requirements.txt

---

## Citation

Dataset from Kaggle: [Eligibility Prediction for Loan](https://www.kaggle.com/datasets/devzohaib/eligibility-prediction-for-loan)

Feature selection techniques studied in course/research on machine learning best practices.

---

Last Updated: April 2026
