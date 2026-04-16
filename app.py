"""
Loan Eligibility Prediction - Local Application
This application uses pre-trained machine learning models to predict loan eligibility.
Three models are available: Baseline (all features), RFE (6 features), and PCA (5 components).
"""

import os
import sys
import pandas as pd
import numpy as np
import joblib
from sklearn.decomposition import PCA

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class LoanPredictionApp:
    """Main application class for loan eligibility prediction"""
    
    def __init__(self):
        """Initialize the application with models and data"""
        self.models = {}
        self.pca = None
        self.X_original = None
        self.load_models()
        self.load_training_data()
        
    def load_models(self):
        """Load all three pre-trained models"""
        try:
            model_path = os.path.join(BASE_DIR, 'reg_clf.pkl')
            self.models['baseline'] = joblib.load(model_path)
            print("✓ Baseline model loaded (Accuracy: 0.7917)")
            
            model_path = os.path.join(BASE_DIR, 'rfe_clf.pkl')
            self.models['rfe'] = joblib.load(model_path)
            print("✓ RFE model loaded (Accuracy: 0.8333)")
            
            model_path = os.path.join(BASE_DIR, 'pca_clf.pkl')
            self.models['pca'] = joblib.load(model_path)
            print("✓ PCA model loaded (Accuracy varies)")
            
        except FileNotFoundError as e:
            print(f"ERROR: Model file not found - {e}")
            sys.exit(1)
    
    def load_training_data(self):
        """Load and preprocess training data for PCA"""
        try:
            csv_path = os.path.join(BASE_DIR, 'Loan_Data_df.csv')
            df = pd.read_csv(csv_path)
            self.X_original = df.drop(['Loan_Status'], axis=1)
            
            # Fit PCA with the same parameters as training
            self.pca = PCA(n_components=5)
            self.pca.fit(self.X_original)
            print("✓ Training data and PCA model loaded")
            
        except FileNotFoundError as e:
            print(f"ERROR: Training data file not found - {e}")
    
    def validate_input(self, gender, married, dependents, education, self_employed, 
                      applicant_income, coapplicant_income, loan_amount, 
                      loan_term, credit_history, property_area):
        """Validate and convert input data"""
        
        # Validate numeric ranges
        if not (0 <= gender <= 1) or not (0 <= married <= 1):
            raise ValueError("Gender and Married must be 0 or 1")
        if not (0 <= dependents <= 3):
            raise ValueError("Dependents must be 0, 1, 2, or 3")
        if not (0 <= education <= 1) or not (0 <= self_employed <= 1):
            raise ValueError("Education and Self_Employed must be 0 or 1")
        if applicant_income < 0 or coapplicant_income < 0:
            raise ValueError("Income values must be positive")
        if loan_amount < 0:
            raise ValueError("Loan Amount must be positive")
        if not (0 <= loan_term <= 500):
            raise ValueError("Loan Term must be between 0 and 500")
        if not (0 <= credit_history <= 1):
            raise ValueError("Credit History must be 0 or 1")
        if not (0 <= property_area <= 2):
            raise ValueError("Property Area must be 0, 1, or 2")
        
        return True
    
    def predict_baseline(self, gender, married, dependents, education, self_employed,
                        applicant_income, coapplicant_income, loan_amount,
                        loan_term, credit_history, property_area):
        """Predict using baseline model (all 11 features)"""
        self.validate_input(gender, married, dependents, education, self_employed,
                          applicant_income, coapplicant_income, loan_amount,
                          loan_term, credit_history, property_area)
        
        # Create input array with all 11 features in correct order
        user_data = np.array([[gender, married, dependents, education, self_employed,
                             applicant_income, coapplicant_income, loan_amount,
                             loan_term, credit_history, property_area]])
        
        prediction = self.models['baseline'].predict(user_data)
        confidence = self._get_decision_score(self.models['baseline'], user_data)
        
        return {
            'model': 'Baseline (All Features)',
            'accuracy': 0.7917,
            'features_used': 11,
            'prediction': 'ELIGIBLE' if prediction[0] == 1 else 'NOT ELIGIBLE',
            'confidence': confidence
        }
    
    def predict_rfe(self, gender, married, education, self_employed, 
                   credit_history, property_area):
        """Predict using RFE model (6 selected features)"""
        
        # Validate selected features only
        if not (0 <= gender <= 1) or not (0 <= married <= 1):
            raise ValueError("Gender and Married must be 0 or 1")
        if not (0 <= education <= 1) or not (0 <= self_employed <= 1):
            raise ValueError("Education and Self_Employed must be 0 or 1")
        if not (0 <= credit_history <= 1):
            raise ValueError("Credit History must be 0 or 1")
        if not (0 <= property_area <= 2):
            raise ValueError("Property Area must be 0, 1, or 2")
        
        # Create input array with RFE selected features
        user_data = np.array([[gender, married, education, self_employed,
                             credit_history, property_area]])
        
        prediction = self.models['rfe'].predict(user_data)
        confidence = self._get_decision_score(self.models['rfe'], user_data)
        
        return {
            'model': 'RFE (6 Features)',
            'accuracy': 0.8333,
            'features_used': ['Gender', 'Married', 'Education', 'Self_Employed', 
                            'Credit_History', 'Property_Area'],
            'prediction': 'ELIGIBLE' if prediction[0] == 1 else 'NOT ELIGIBLE',
            'confidence': confidence
        }
    
    def predict_pca(self, gender, married, dependents, education, self_employed,
                   applicant_income, coapplicant_income, loan_amount,
                   loan_term, credit_history, property_area):
        """Predict using PCA model (5 principal components)"""
        self.validate_input(gender, married, dependents, education, self_employed,
                          applicant_income, coapplicant_income, loan_amount,
                          loan_term, credit_history, property_area)
        
        # Create input dataframe with all features in correct order
        feature_names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                        'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                        'Loan_Amount_Term', 'Credit_History', 'Property_Area']
        
        user_data = pd.DataFrame([[gender, married, dependents, education, self_employed,
                                 applicant_income, coapplicant_income, loan_amount,
                                 loan_term, credit_history, property_area]],
                                columns=feature_names)
        
        # Apply PCA transformation
        user_data_pca = self.pca.transform(user_data)
        
        prediction = self.models['pca'].predict(user_data_pca)
        confidence = self._get_decision_score(self.models['pca'], user_data_pca)
        
        return {
            'model': 'PCA (5 Components)',
            'accuracy': 0.7153,
            'features_used': 5,
            'prediction': 'ELIGIBLE' if prediction[0] == 1 else 'NOT ELIGIBLE',
            'confidence': confidence
        }
    
    def _get_decision_score(self, model, data):
        """Get decision score from model (confidence level)"""
        try:
            if hasattr(model, 'decision_function'):
                scores = model.decision_function(data)
                return float(abs(scores[0]))
            else:
                # For models without decision_function, return prediction probability
                return 0.5
        except:
            return 0.5
    
    def interactive_mode(self):
        """Run in interactive mode for user input"""
        print("\n" + "="*60)
        print("LOAN ELIGIBILITY PREDICTION SYSTEM")
        print("="*60)
        
        while True:
            print("\nSelect prediction method:")
            print("1. Baseline Model (All 11 features)")
            print("2. RFE Model (6 selected features)")
            print("3. PCA Model (5 principal components)")
            print("4. Exit")
            
            choice = input("\nEnter choice (1-4): ").strip()
            
            if choice == '4':
                print("\nThank you for using Loan Eligibility Predictor!")
                break
            
            elif choice == '1':
                try:
                    print("\n--- BASELINE MODEL ---")
                    print("Note: Gender (0=Male, 1=Female), Married (0=No, 1=Yes)")
                    print("Education (0=Not Graduate, 1=Graduate)")
                    print("Self_Employed (0=No, 1=Yes), Credit_History (0=No, 1=Yes)")
                    print("Property_Area (0=Rural, 1=Semiurban, 2=Urban)")
                    
                    gender = int(input("Gender (0/1): "))
                    married = int(input("Married (0/1): "))
                    dependents = int(input("Dependents (0/1/2/3): "))
                    education = int(input("Education (0/1): "))
                    self_employed = int(input("Self_Employed (0/1): "))
                    applicant_income = float(input("Applicant Income: "))
                    coapplicant_income = float(input("Coapplicant Income: "))
                    loan_amount = float(input("Loan Amount (x1000): "))
                    loan_term = int(input("Loan Term (months): "))
                    credit_history = int(input("Credit_History (0/1): "))
                    property_area = int(input("Property_Area (0/1/2): "))
                    
                    result = self.predict_baseline(gender, married, dependents, education,
                                                  self_employed, applicant_income,
                                                  coapplicant_income, loan_amount,
                                                  loan_term, credit_history, property_area)
                    
                    self._display_result(result)
                    
                except ValueError as e:
                    print(f"❌ Invalid input: {e}")
            
            elif choice == '2':
                try:
                    print("\n--- RFE MODEL (6 Features) ---")
                    print("Note: Gender (0=Male, 1=Female), Married (0=No, 1=Yes)")
                    print("Education (0=Not Graduate, 1=Graduate)")
                    print("Self_Employed (0=No, 1=Yes), Credit_History (0=No, 1=Yes)")
                    print("Property_Area (0=Rural, 1=Semiurban, 2=Urban)")
                    
                    gender = int(input("Gender (0/1): "))
                    married = int(input("Married (0/1): "))
                    education = int(input("Education (0/1): "))
                    self_employed = int(input("Self_Employed (0/1): "))
                    credit_history = int(input("Credit_History (0/1): "))
                    property_area = int(input("Property_Area (0/1/2): "))
                    
                    result = self.predict_rfe(gender, married, education, self_employed,
                                            credit_history, property_area)
                    
                    self._display_result(result)
                    
                except ValueError as e:
                    print(f"❌ Invalid input: {e}")
            
            elif choice == '3':
                try:
                    print("\n--- PCA MODEL (5 Components) ---")
                    print("Note: Gender (0=Male, 1=Female), Married (0=No, 1=Yes)")
                    print("Education (0=Not Graduate, 1=Graduate)")
                    print("Self_Employed (0=No, 1=Yes), Credit_History (0=No, 1=Yes)")
                    print("Property_Area (0=Rural, 1=Semiurban, 2=Urban)")
                    
                    gender = int(input("Gender (0/1): "))
                    married = int(input("Married (0/1): "))
                    dependents = int(input("Dependents (0/1/2/3): "))
                    education = int(input("Education (0/1): "))
                    self_employed = int(input("Self_Employed (0/1): "))
                    applicant_income = float(input("Applicant Income: "))
                    coapplicant_income = float(input("Coapplicant Income: "))
                    loan_amount = float(input("Loan Amount (x1000): "))
                    loan_term = int(input("Loan Term (months): "))
                    credit_history = int(input("Credit_History (0/1): "))
                    property_area = int(input("Property_Area (0/1/2): "))
                    
                    result = self.predict_pca(gender, married, dependents, education,
                                            self_employed, applicant_income,
                                            coapplicant_income, loan_amount,
                                            loan_term, credit_history, property_area)
                    
                    self._display_result(result)
                    
                except ValueError as e:
                    print(f"❌ Invalid input: {e}")
            
            else:
                print("❌ Invalid choice. Please enter 1-4.")
    
    def _display_result(self, result):
        """Display prediction result"""
        print("\n" + "-"*60)
        print(f"Model: {result['model']}")
        print(f"Accuracy: {result['accuracy']*100:.2f}%")
        if isinstance(result['features_used'], list):
            print(f"Features: {', '.join(result['features_used'])}")
        else:
            print(f"Features Used: {result['features_used']}")
        print("-"*60)
        print(f"PREDICTION: {result['prediction']}")
        print(f"Confidence: {result['confidence']:.4f}")
        print("-"*60 + "\n")


def main():
    """Main entry point"""
    print("\nInitializing Loan Eligibility Prediction System...")
    
    try:
        app = LoanPredictionApp()
        app.interactive_mode()
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
