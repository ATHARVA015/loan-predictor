# QUICK REFERENCE - Loan Eligibility Prediction

## 🚀 Quick Start (Choose One)

### Windows Users:
```bash
cd path\to\project
run.bat
```

### macOS/Linux Users:
```bash
cd path/to/project
chmod +x run.sh
./run.sh
```

### Manual:
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
pip install -r requirements.txt
python app.py
```

---

## 📊 Three Models Available

### 1️⃣ RFE Model ⭐ **BEST**
- **Accuracy:** 83.33%
- **Features:** 6 (Gender, Married, Education, Self_Employed, Credit_History, Property_Area)
- **Speed:** Fast
- **Data Needed:** Only categorical data

### 2️⃣ Baseline Model
- **Accuracy:** 79.17%
- **Features:** All 11
- **Speed:** Very fast
- **Data Needed:** All fields

### 3️⃣ PCA Model
- **Accuracy:** 71.53%
- **Features:** 5 components (from all 11)
- **Speed:** Medium
- **Data Needed:** All fields

---

## 🔢 Input Encoding Guide

```
Gender:           0=Male,  1=Female
Married:          0=No,    1=Yes
Dependents:       0, 1, 2, or 3
Education:        0=Not Graduate,  1=Graduate
Self_Employed:    0=No,    1=Yes
Credit_History:   0=No,    1=Yes
Property_Area:    0=Rural, 1=Semiurban, 2=Urban
```

---

## 📁 Project Files

```
✓ app.py                                  (Main application)
✓ index.py                                (Streamlit web app)
✓ run.bat / run.sh                        (Auto setup scripts)
✓ requirements.txt                        (Dependencies)

✓ reg_clf.pkl                            (Baseline model)
✓ rfe_clf.pkl                            (RFE model - BEST)
✓ pca_clf.pkl                            (PCA model)

✓ Loan_Data.csv                          (Original data)
✓ Loan_Data_df.csv                       (Cleaned data)
✓ Loan_Prediction_Feature_Selection.ipynb (Training notebook)

✓ SETUP_GUIDE.md                         (Installation guide)
✓ PROJECT_ANALYSIS.md                    (Detailed analysis)
✓ QUICK_REFERENCE.md                     (This file)
```

---

## ⚡ Features Used by Each Model

### RFE Model (6 features)
1. Gender
2. Married
3. Education
4. Self_Employed
5. Credit_History
6. Property_Area

### Baseline Model (all 11 features)
1. Gender
2. Married
3. Dependents
4. Education
5. Self_Employed
6. ApplicantIncome
7. CoapplicantIncome
8. LoanAmount
9. Loan_Amount_Term
10. Credit_History
11. Property_Area

### PCA Model (5 components from all 11)
- PC1, PC2, PC3, PC4, PC5

---

## 🔍 What Are .pkl Files?

- **Format:** Python pickle (serialized objects)
- **Purpose:** Store trained models
- **Size:** ~2-5 KB each
- **Tool:** joblib library loads them
- **Content:** Trained Ridge Classifier + weights

### The Three Models:
- `reg_clf.pkl` → Baseline classifier (11 features)
- `rfe_clf.pkl` → RFE classifier (6 features)
- `pca_clf.pkl` → PCA classifier (5 components)

---

## 💡 Example Predictions

### Using RFE Model:
Input: Female graduate, married, self-employed, good credit, urban
```
Gender: 1 (Female)
Married: 1 (Yes)
Education: 1 (Graduate)
Self_Employed: 1 (Yes)
Credit_History: 1 (Yes)
Property_Area: 2 (Urban)
↓
Result: ELIGIBLE (83.33% model)
```

### Using Baseline Model:
Same person, all fields:
```
Gender: 1, Married: 1, Dependents: 0,
Education: 1, Self_Employed: 1,
ApplicantIncome: 5000, CoapplicantIncome: 1000,
LoanAmount: 150, Loan_Amount_Term: 360,
Credit_History: 1, Property_Area: 2
↓
Result: ELIGIBLE (79.17% model)
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Module not found" | `pip install -r requirements.txt` |
| ".pkl file not found" | Check files are in project directory |
| "Permission denied" | `chmod +x run.sh` (macOS/Linux) |
| Python not found | Install Python 3.8+ from python.org |
| Virtual env fails | Use `python3` instead of `python` |

---

## 📈 Model Comparison Table

| Feature | Baseline | RFE | PCA |
|---------|----------|-----|-----|
| Accuracy | 79.17% | **83.33%** ⭐ | 71.53% |
| Speed | ⚡⚡⚡ | ⚡⚡ | ⚡ |
| Simplicity | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Data Required | All 11 | 6 only | All 11 |
| Best For | Quick check | Production | Analysis |

---

## 🎯 Recommended Workflow

1. **Start with RFE model** (best accuracy + simplicity)
2. **Compare with Baseline** (check consistency)
3. **Use Baseline for speed** (if needed)
4. **Avoid PCA** (lower accuracy)

---

## 📚 Files Documentation

### app.py
- **What:** Local CLI application
- **Run:** `python app.py`
- **Interface:** Menu-driven
- **Advantage:** No web dependency

### index.py
- **What:** Streamlit web app
- **Run:** `streamlit run index.py`
- **Interface:** Web browser (localhost:8501)
- **Advantage:** Rich UI, sliders

### Notebook
- **What:** Training & analysis
- **Run:** Open in Jupyter/VS Code
- **Contains:** Model training code
- **Purpose:** Retrain with new data

---

## 🔧 Dependencies Explained

| Package | Version | Why |
|---------|---------|-----|
| pandas | 1.5.3 | CSV file handling |
| numpy | 1.26.4 | Math operations |
| scikit-learn | 1.2.2 | ML algorithms |
| joblib | 1.1.1 | Load .pkl models |
| streamlit | 1.21.0 | Web UI (optional) |

---

## 📊 Data Preprocessing Done

✓ Categorical → Numeric conversion
✓ Null values removed
✓ Feature ordering consistent
✓ 70-30 train-test split
✓ Models saved as .pkl

---

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] project directory accessible
- [ ] All .pkl files present
- [ ] Loan_Data_df.csv available
- [ ] requirements.txt not modified
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] app.py runs without errors

---

## 🎓 Learning Resources in Project

1. **SETUP_GUIDE.md** - How to install and run
2. **PROJECT_ANALYSIS.md** - Deep technical analysis
3. **Loan_Prediction_Feature_Selection.ipynb** - Model training
4. **README.md** - Original project info

---

## 🚀 Next Steps

1. Run: `python app.py`
2. Select model (RFE recommended)
3. Input applicant data
4. Get prediction
5. Compare across models
6. Deploy if satisfied

---

## 📞 Support

**Common Issues:**
- Python not found → Install from python.org
- Module errors → `pip install -r requirements.txt`
- .pkl not found → Check project directory
- Permission denied → `chmod +x run.sh`

**For more details:**
- See SETUP_GUIDE.md for installation
- See PROJECT_ANALYSIS.md for technical details
- See README.md for project overview

---

**Status: ✅ READY TO RUN LOCALLY**

All models are trained and ready. No additional training or setup needed!

