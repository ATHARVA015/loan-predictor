"""
Loan Eligibility Prediction - System Verification Script
Tests all components without user interaction
"""

import os
import sys

def check_python_version():
    """Verify Python version"""
    print("\n1. Checking Python Version...")
    version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if sys.version_info >= (3, 8):
        print(f"   ✓ Python {version} (OK - 3.8+)")
        return True
    else:
        print(f"   ✗ Python {version} (ERROR - Need 3.8+)")
        return False

def check_packages():
    """Verify required packages are installed"""
    print("\n2. Checking Required Packages...")
    packages = ['pandas', 'numpy', 'sklearn', 'joblib']
    all_ok = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"   ✓ {package}")
        except ImportError:
            print(f"   ✗ {package} NOT INSTALLED")
            all_ok = False
    
    return all_ok

def check_model_files():
    """Verify model files exist"""
    print("\n3. Checking Model Files (.pkl)...")
    models = ['reg_clf.pkl', 'rfe_clf.pkl', 'pca_clf.pkl']
    all_ok = True
    
    for model in models:
        if os.path.exists(model):
            size = os.path.getsize(model) / 1024  # KB
            print(f"   ✓ {model} ({size:.1f} KB)")
        else:
            print(f"   ✗ {model} NOT FOUND")
            all_ok = False
    
    return all_ok

def check_data_files():
    """Verify data files exist"""
    print("\n4. Checking Data Files...")
    data_files = ['Loan_Data.csv', 'Loan_Data_df.csv']
    all_ok = True
    
    for data_file in data_files:
        if os.path.exists(data_file):
            size = os.path.getsize(data_file) / 1024  # KB
            print(f"   ✓ {data_file} ({size:.1f} KB)")
        else:
            print(f"   ✗ {data_file} NOT FOUND")
            all_ok = False
    
    return all_ok

def check_application_files():
    """Verify application files exist"""
    print("\n5. Checking Application Files...")
    app_files = ['app.py', 'index.py']
    all_ok = True
    
    for app_file in app_files:
        if os.path.exists(app_file):
            size = os.path.getsize(app_file) / 1024  # KB
            print(f"   ✓ {app_file} ({size:.1f} KB)")
        else:
            print(f"   ✗ {app_file} NOT FOUND")
            all_ok = False
    
    return all_ok

def test_model_loading():
    """Test loading models"""
    print("\n6. Testing Model Loading...")
    try:
        import joblib
        
        models_to_test = {
            'reg_clf.pkl': 'Baseline',
            'rfe_clf.pkl': 'RFE',
            'pca_clf.pkl': 'PCA'
        }
        
        all_ok = True
        for model_file, model_name in models_to_test.items():
            try:
                model = joblib.load(model_file)
                print(f"   ✓ {model_name} model loaded")
            except Exception as e:
                print(f"   ✗ {model_name} model failed: {e}")
                all_ok = False
        
        return all_ok
    except Exception as e:
        print(f"   ✗ Error during model loading: {e}")
        return False

def test_predictions():
    """Test making predictions"""
    print("\n7. Testing Predictions...")
    try:
        import joblib
        import numpy as np
        
        # Test Baseline
        try:
            baseline = joblib.load('reg_clf.pkl')
            test_data_baseline = np.array([[1, 1, 0, 1, 1, 5000, 1000, 150, 360, 1, 2]])
            pred = baseline.predict(test_data_baseline)
            print(f"   ✓ Baseline prediction: {'ELIGIBLE' if pred[0] == 1 else 'NOT ELIGIBLE'}")
        except Exception as e:
            print(f"   ✗ Baseline prediction failed: {e}")
            return False
        
        # Test RFE
        try:
            rfe = joblib.load('rfe_clf.pkl')
            test_data_rfe = np.array([[1, 1, 1, 1, 1, 2]])
            pred = rfe.predict(test_data_rfe)
            print(f"   ✓ RFE prediction: {'ELIGIBLE' if pred[0] == 1 else 'NOT ELIGIBLE'}")
        except Exception as e:
            print(f"   ✗ RFE prediction failed: {e}")
            return False
        
        # Test PCA
        try:
            pca_model = joblib.load('pca_clf.pkl')
            # For PCA we need to test with transformed data
            # Just check if model works
            print(f"   ✓ PCA model loads successfully")
        except Exception as e:
            print(f"   ✗ PCA model failed: {e}")
            return False
        
        return True
    except Exception as e:
        print(f"   ✗ Error during prediction testing: {e}")
        return False

def test_data_loading():
    """Test loading data"""
    print("\n8. Testing Data Loading...")
    try:
        import pandas as pd
        
        # Test Loan_Data_df.csv (needed for PCA)
        try:
            df = pd.read_csv('Loan_Data_df.csv')
            rows, cols = df.shape
            print(f"   ✓ Loan_Data_df.csv loaded ({rows} rows, {cols} cols)")
            
            # Check required columns
            required_cols = ['Gender', 'Married', 'Education', 'Self_Employed',
                           'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                           'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status']
            missing = [col for col in required_cols if col not in df.columns]
            if missing:
                print(f"   ✗ Missing columns: {missing}")
                return False
        except Exception as e:
            print(f"   ✗ Data loading failed: {e}")
            return False
        
        return True
    except Exception as e:
        print(f"   ✗ Error during data testing: {e}")
        return False

def print_summary(results):
    """Print final summary"""
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    total = len(results)
    passed = sum(results.values())
    
    for check, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {check}")
    
    print("-"*60)
    print(f"Result: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✓ ALL SYSTEMS READY - Application is ready to run!")
        return True
    else:
        print(f"\n✗ {total - passed} issues found - Please fix and retry")
        return False

def main():
    """Run all verification checks"""
    print("\n" + "="*60)
    print("LOAN ELIGIBILITY PREDICTION - SYSTEM VERIFICATION")
    print("="*60)
    
    results = {}
    
    # Run all checks
    results['Python Version (3.8+)'] = check_python_version()
    results['Required Packages'] = check_packages()
    results['Model Files (.pkl)'] = check_model_files()
    results['Data Files'] = check_data_files()
    results['Application Files'] = check_application_files()
    results['Model Loading'] = test_model_loading()
    results['Predictions'] = test_predictions()
    results['Data Loading'] = test_data_loading()
    
    # Print summary
    all_ok = print_summary(results)
    
    # Exit code
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
