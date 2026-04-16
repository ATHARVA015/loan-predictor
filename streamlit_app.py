"""
Loan Eligibility Prediction - Streamlit Web Application
A professional web UI for loan eligibility prediction using machine learning models.
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.decomposition import PCA

# Page configuration
st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        font-weight: 600;
    }
    .prediction-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f0f2f6;
        margin: 1rem 0;
    }
    .eligible {
        background-color: #d1e7dd;
        border-left: 5px solid #198754;
    }
    .not-eligible {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
    }
    </style>
    """, unsafe_allow_html=True)

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_models():
    """Load all models"""
    try:
        models = {}
        
        model_path = os.path.join(BASE_DIR, 'reg_clf.pkl')
        models['baseline'] = joblib.load(model_path)
        
        model_path = os.path.join(BASE_DIR, 'rfe_clf.pkl')
        models['rfe'] = joblib.load(model_path)
        
        model_path = os.path.join(BASE_DIR, 'pca_clf.pkl')
        models['pca'] = joblib.load(model_path)
        
        return models
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None

@st.cache_resource
def load_pca_model():
    """Load and fit PCA model"""
    try:
        csv_path = os.path.join(BASE_DIR, 'Loan_Data_df.csv')
        df = pd.read_csv(csv_path)
        X = df.drop(['Loan_Status'], axis=1)
        
        pca = PCA(n_components=5)
        pca.fit(X)
        return pca
    except Exception as e:
        st.error(f"Error loading PCA: {e}")
        return None

def validate_input(data):
    """Validate input data"""
    errors = []
    
    if 'gender' in data and not (0 <= data['gender'] <= 1):
        errors.append("Gender must be 0 (Male) or 1 (Female)")
    if 'married' in data and not (0 <= data['married'] <= 1):
        errors.append("Married must be 0 (No) or 1 (Yes)")
    if 'dependents' in data and not (0 <= data['dependents'] <= 3):
        errors.append("Dependents must be 0, 1, 2, or 3")
    if 'education' in data and not (0 <= data['education'] <= 1):
        errors.append("Education must be 0 (Not Graduate) or 1 (Graduate)")
    if 'self_employed' in data and not (0 <= data['self_employed'] <= 1):
        errors.append("Self Employed must be 0 (No) or 1 (Yes)")
    if 'applicant_income' in data and data['applicant_income'] < 0:
        errors.append("Applicant Income must be positive")
    if 'coapplicant_income' in data and data['coapplicant_income'] < 0:
        errors.append("Coapplicant Income must be positive")
    if 'loan_amount' in data and data['loan_amount'] < 0:
        errors.append("Loan Amount must be positive")
    if 'loan_term' in data and not (0 <= data['loan_term'] <= 500):
        errors.append("Loan Term must be between 0 and 500 months")
    if 'credit_history' in data and not (0 <= data['credit_history'] <= 1):
        errors.append("Credit History must be 0 (No) or 1 (Yes)")
    if 'property_area' in data and not (0 <= data['property_area'] <= 2):
        errors.append("Property Area must be 0 (Rural), 1 (Semiurban), or 2 (Urban)")
    
    return errors

# Header
st.title("💰 Loan Eligibility Predictor")
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    ### Predict your loan eligibility using Machine Learning
    Choose from 3 different models with varying accuracy and feature requirements
    """)

st.markdown("---")

# Load models
models = load_models()
pca_model = load_pca_model()

if models is None or pca_model is None:
    st.error("Failed to load models. Please check that all files are in the correct directory.")
    st.stop()

# Tabs for different models
tab1, tab2, tab3, tab4 = st.tabs(["🎯 RFE Model", "📊 Baseline Model", "🔍 PCA Model", "ℹ️ Info"])

# ==================== TAB 1: RFE MODEL ====================
with tab1:
    st.header("RFE Model (6 Features)")
    st.write("**Accuracy:** 83.33% | **Features:** 6 selected features")
    st.info("This model uses Recursive Feature Elimination to select the 6 most important features. Selected: Gender, Married, Dependents, Education, Self_Employed, Credit_History")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Features")
        
        gender_rfe = st.radio(
            "Gender",
            options=[0, 1],
            format_func=lambda x: "Male" if x == 0 else "Female",
            key="gender_rfe"
        )
        
        married_rfe = st.radio(
            "Married",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="married_rfe"
        )
        
        dependents_rfe = st.radio(
            "Dependents",
            options=[0, 1, 2, 3],
            format_func=lambda x: "3+" if x == 3 else str(x),
            key="dependents_rfe"
        )
        
        education_rfe = st.radio(
            "Education",
            options=[0, 1],
            format_func=lambda x: "Not Graduate" if x == 0 else "Graduate",
            key="education_rfe"
        )
        
        self_employed_rfe = st.radio(
            "Self Employed",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="self_employed_rfe"
        )
        
        credit_history_rfe = st.radio(
            "Credit History",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="credit_history_rfe"
        )
    
    with col2:
        st.subheader("Summary")
        summary_data = {
            "Gender": "Male" if gender_rfe == 0 else "Female",
            "Married": "No" if married_rfe == 0 else "Yes",
            "Dependents": "3+" if dependents_rfe == 3 else str(dependents_rfe),
            "Education": "Not Graduate" if education_rfe == 0 else "Graduate",
            "Self Employed": "No" if self_employed_rfe == 0 else "Yes",
            "Credit History": "No" if credit_history_rfe == 0 else "Yes"
        }
        
        st.dataframe(
            pd.DataFrame(summary_data.items(), columns=["Feature", "Value"]),
            use_container_width=True,
            hide_index=True
        )
        
        # Predict button
        if st.button("🔮 Predict (RFE)", use_container_width=True, key="predict_rfe"):
            rfe_input = np.array([[gender_rfe, married_rfe, dependents_rfe, 
                                  education_rfe, self_employed_rfe, credit_history_rfe]])
            
            prediction = models['rfe'].predict(rfe_input)[0]
            
            prediction_text = "✅ ELIGIBLE" if prediction == 1 else "❌ NOT ELIGIBLE"
            prediction_class = "eligible" if prediction == 1 else "not-eligible"
            
            st.markdown(f"""
            <div class="prediction-box {prediction_class}">
                <h2 style="margin: 0;">{prediction_text}</h2>
                <p style="margin: 0.5rem 0 0 0;"><strong>Model Accuracy:</strong> 83.33%</p>
                <p style="margin: 0.5rem 0 0 0;"><strong>Features Used:</strong> 6</p>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 2: BASELINE MODEL ====================
with tab2:
    st.header("Baseline Model (All Features)")
    st.write("**Accuracy:** 79.17% | **Features:** 11 original features")
    st.info("This model uses all available features without any feature selection. Most comprehensive approach.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Features")
        
        gender_base = st.radio(
            "Gender",
            options=[0, 1],
            format_func=lambda x: "Male" if x == 0 else "Female",
            key="gender_base"
        )
        
        married_base = st.radio(
            "Married",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="married_base"
        )
        
        dependents_base = st.radio(
            "Dependents",
            options=[0, 1, 2, 3],
            format_func=lambda x: "3+" if x == 3 else str(x),
            key="dependents_base"
        )
        
        education_base = st.radio(
            "Education",
            options=[0, 1],
            format_func=lambda x: "Not Graduate" if x == 0 else "Graduate",
            key="education_base"
        )
        
        self_employed_base = st.radio(
            "Self Employed",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="self_employed_base"
        )
    
    with col2:
        st.subheader("Financial Information")
        
        applicant_income_base = st.number_input(
            "Applicant Income",
            min_value=0.0,
            value=5000.0,
            step=100.0,
            key="applicant_income_base"
        )
        
        coapplicant_income_base = st.number_input(
            "Coapplicant Income",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            key="coapplicant_income_base"
        )
        
        loan_amount_base = st.number_input(
            "Loan Amount (x1000)",
            min_value=0.0,
            value=150.0,
            step=10.0,
            key="loan_amount_base"
        )
        
        loan_term_base = st.number_input(
            "Loan Term (months)",
            min_value=0,
            max_value=500,
            value=360,
            step=12,
            key="loan_term_base"
        )
        
        credit_history_base = st.radio(
            "Credit History",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="credit_history_base"
        )
        
        property_area_base = st.radio(
            "Property Area",
            options=[0, 1, 2],
            format_func=lambda x: ["Rural", "Semiurban", "Urban"][x],
            key="property_area_base"
        )
    
    # Predict button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔮 Predict (Baseline)", use_container_width=True, key="predict_base"):
            base_input = np.array([[gender_base, married_base, dependents_base, education_base,
                                   self_employed_base, applicant_income_base, coapplicant_income_base,
                                   loan_amount_base, loan_term_base, credit_history_base, property_area_base]])
            
            prediction = models['baseline'].predict(base_input)[0]
            
            prediction_text = "✅ ELIGIBLE" if prediction == 1 else "❌ NOT ELIGIBLE"
            prediction_class = "eligible" if prediction == 1 else "not-eligible"
            
            st.markdown(f"""
            <div class="prediction-box {prediction_class}">
                <h2 style="margin: 0;">{prediction_text}</h2>
                <p style="margin: 0.5rem 0 0 0;"><strong>Model Accuracy:</strong> 79.17%</p>
                <p style="margin: 0.5rem 0 0 0;"><strong>Features Used:</strong> 11</p>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 3: PCA MODEL ====================
with tab3:
    st.header("PCA Model (5 Components)")
    st.write("**Accuracy:** ~71.53% | **Features:** 5 principal components")
    st.info("This model uses Principal Component Analysis to reduce dimensionality. Handles multicollinearity well.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Personal Information")
        
        gender_pca = st.radio(
            "Gender",
            options=[0, 1],
            format_func=lambda x: "Male" if x == 0 else "Female",
            key="gender_pca"
        )
        
        married_pca = st.radio(
            "Married",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="married_pca"
        )
        
        dependents_pca = st.radio(
            "Dependents",
            options=[0, 1, 2, 3],
            format_func=lambda x: "3+" if x == 3 else str(x),
            key="dependents_pca"
        )
        
        education_pca = st.radio(
            "Education",
            options=[0, 1],
            format_func=lambda x: "Not Graduate" if x == 0 else "Graduate",
            key="education_pca"
        )
        
        self_employed_pca = st.radio(
            "Self Employed",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="self_employed_pca"
        )
    
    with col2:
        st.subheader("Financial Information")
        
        applicant_income_pca = st.number_input(
            "Applicant Income",
            min_value=0.0,
            value=5000.0,
            step=100.0,
            key="applicant_income_pca"
        )
        
        coapplicant_income_pca = st.number_input(
            "Coapplicant Income",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            key="coapplicant_income_pca"
        )
        
        loan_amount_pca = st.number_input(
            "Loan Amount (x1000)",
            min_value=0.0,
            value=150.0,
            step=10.0,
            key="loan_amount_pca"
        )
        
        loan_term_pca = st.number_input(
            "Loan Term (months)",
            min_value=0,
            max_value=500,
            value=360,
            step=12,
            key="loan_term_pca"
        )
        
        credit_history_pca = st.radio(
            "Credit History",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
            key="credit_history_pca"
        )
        
        property_area_pca = st.radio(
            "Property Area",
            options=[0, 1, 2],
            format_func=lambda x: ["Rural", "Semiurban", "Urban"][x],
            key="property_area_pca"
        )
    
    # Predict button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔮 Predict (PCA)", use_container_width=True, key="predict_pca"):
            feature_names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                            'Loan_Amount_Term', 'Credit_History', 'Property_Area']
            
            pca_input_df = pd.DataFrame([[gender_pca, married_pca, dependents_pca, education_pca,
                                         self_employed_pca, applicant_income_pca, coapplicant_income_pca,
                                         loan_amount_pca, loan_term_pca, credit_history_pca, property_area_pca]],
                                       columns=feature_names)
            
            pca_transformed = pca_model.transform(pca_input_df)
            prediction = models['pca'].predict(pca_transformed)[0]
            
            prediction_text = "✅ ELIGIBLE" if prediction == 1 else "❌ NOT ELIGIBLE"
            prediction_class = "eligible" if prediction == 1 else "not-eligible"
            
            st.markdown(f"""
            <div class="prediction-box {prediction_class}">
                <h2 style="margin: 0;">{prediction_text}</h2>
                <p style="margin: 0.5rem 0 0 0;"><strong>Model Accuracy:</strong> ~71.53%</p>
                <p style="margin: 0.5rem 0 0 0;"><strong>Features Used:</strong> 5 (Principal Components)</p>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 4: INFO ====================
with tab4:
    st.header("ℹ️ Application Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Models Overview")
        
        models_info = pd.DataFrame({
            "Model": ["RFE", "Baseline", "PCA"],
            "Accuracy": ["83.33%", "79.17%", "~71.53%"],
            "Features": [6, 11, 5],
            "Speed": ["Fast", "Very Fast", "Medium"],
            "Best For": ["Balanced", "Quick", "Collinearity"]
        })
        
        st.dataframe(models_info, use_container_width=True, hide_index=True)
        
        st.subheader("🎯 Feature Encoding")
        
        encoding_info = {
            "Gender": {"0": "Male", "1": "Female"},
            "Married": {"0": "No", "1": "Yes"},
            "Dependents": {"0": "0", "1": "1", "2": "2", "3": "3+"},
            "Education": {"0": "Not Graduate", "1": "Graduate"},
            "Self Employed": {"0": "No", "1": "Yes"},
            "Credit History": {"0": "No", "1": "Yes"},
            "Property Area": {"0": "Rural", "1": "Semiurban", "2": "Urban"}
        }
        
        for feature, values in encoding_info.items():
            st.write(f"**{feature}:** {', '.join([f'{k}={v}' for k, v in values.items()])}")
    
    with col2:
        st.subheader("📊 About the Models")
        
        st.write("""
        **RFE Model (Recommended)**
        - Uses Recursive Feature Elimination
        - Selected 6 most important features
        - Features: Gender, Married, Dependents, Education, Self_Employed, Credit_History
        - Highest accuracy among all models
        - Requires only 6 inputs
        
        **Baseline Model**
        - Uses all 11 original features
        - No feature selection applied
        - Good for comprehensive analysis
        - Slightly lower accuracy
        
        **PCA Model**
        - Uses Principal Component Analysis
        - Reduces to 5 components
        - Handles multicollinearity
        - Lower accuracy but robust
        """)
        
        st.subheader("📈 Dataset Info")
        st.write("""
        - **Source:** Kaggle - Eligibility Prediction for Loan
        - **Total Records:** ~614 (after preprocessing)
        - **Train-Test Split:** 70-30
        - **Target:** Loan Eligibility (Yes/No)
        - **Algorithm:** Ridge Classifier (except PCA uses RidgeClassifier)
        """)
    
    st.markdown("---")
    st.info("💡 **Tip:** Start with the RFE Model for best accuracy with minimal input requirements!")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🔧 Built with Streamlit & Scikit-learn")
with col2:
    st.caption("📊 Dataset from Kaggle")
with col3:
    st.caption("✨ ML Models using Feature Selection")
