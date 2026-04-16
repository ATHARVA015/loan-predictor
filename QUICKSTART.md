# 🚀 Quick Start Guide

## Step 1: Install Dependencies (First Time Only)

```bash
pip install -r requirements.txt
```

---

## Step 2: Run the Application

### **Option A: Streamlit Web UI (RECOMMENDED)**

```bash
python -m streamlit run streamlit_app.py
```

Browser will open automatically at `http://localhost:8501`

### **Option B: Command Line Interface**

```bash
python app.py
```

---

## Step 3: Choose a Model

### **Tab 1: RFE Model** ⭐ (BEST)
- **Best for:** Balanced accuracy and simplicity
- **Features needed:** 6
- **Accuracy:** 83.33%
- **Selected features:** Gender, Married, Dependents, Education, Self_Employed, Credit_History

### **Tab 2: Baseline Model**
- **Best for:** Comprehensive analysis
- **Features needed:** 11 (all)
- **Accuracy:** 83.33%

### **Tab 3: PCA Model**
- **Best for:** Handling multicollinearity
- **Features needed:** 11 (transforms to 5 components)
- **Accuracy:** 71.53%

---

## Step 4: Enter Your Data

### Feature Encoding Reference:

**Gender:**
- 0 = Male
- 1 = Female

**Married:**
- 0 = No
- 1 = Yes

**Dependents:**
- 0, 1, 2, or 3 (3 = 3 or more)

**Education:**
- 0 = Not Graduate
- 1 = Graduate

**Self_Employed:**
- 0 = No
- 1 = Yes

**Credit_History:**
- 0 = No
- 1 = Yes

**Property_Area:**
- 0 = Rural
- 1 = Semiurban
- 2 = Urban

**Income Values:** Use actual income amounts  
**Loan Amount:** Use in thousands (e.g., 150 = 150,000)  
**Loan Term:** Use in months (e.g., 360 = 30 years)

---

## Step 5: Get Prediction

Click the **"🔮 Predict"** button to see:
- ✅ **ELIGIBLE** or ❌ **NOT ELIGIBLE**
- Model accuracy
- Confidence score

---

## Example Test Cases

### Test 1: Low-Risk Applicant
```
Gender: 1 (Female)
Married: 1 (Yes)
Dependents: 1
Education: 1 (Graduate)
Self_Employed: 0 (No)
Credit_History: 1 (Yes)
```
**Expected:** ELIGIBLE ✅

### Test 2: High-Risk Applicant
```
Gender: 0 (Male)
Married: 0 (No)
Dependents: 0
Education: 0 (Not Graduate)
Self_Employed: 1 (Yes)
Credit_History: 0 (No)
```
**Expected:** NOT ELIGIBLE ❌

---

## Troubleshooting

### **"Module not found" error**
```bash
pip install -r requirements.txt
```

### **Port 8501 already in use**
```bash
python -m streamlit run streamlit_app.py --server.port 8502
```

### **Models not loading**
Ensure all `.pkl` files are in the project directory:
- `reg_clf.pkl` (Baseline)
- `rfe_clf.pkl` (RFE)
- `pca_clf.pkl` (PCA)

---

## File Structure

```
Loan_Eligibility_Prediction/
├── streamlit_app.py          # Web UI (Recommended)
├── app.py                    # CLI version
├── retrain_models.py         # Retrain models if needed
├── test_models.py            # Test models
├── reg_clf.pkl               # Baseline model
├── rfe_clf.pkl               # RFE model
├── pca_clf.pkl               # PCA model
├── Loan_Data.csv             # Original dataset
├── Loan_Data_df.csv          # Processed dataset
├── requirements.txt          # Dependencies
└── README.md                 # Documentation
```

---

## Next Steps

1. ✅ Run the app
2. ✅ Try all 3 models
3. ✅ Test with different inputs
4. ✅ Compare predictions across models
5. ✅ Deploy if needed

---

**Enjoy your Loan Eligibility Predictor! 💰**
