@echo off
REM Loan Eligibility Prediction - Quick Setup Script for Windows
REM This script sets up the environment and runs the application

echo.
echo ========================================================
echo Loan Eligibility Prediction - Setup Script
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo Step 1: Checking Python installation...
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Step 2: Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
) else (
    echo Step 2: Virtual environment already exists, skipping creation
)
echo.

REM Activate virtual environment
echo Step 3: Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Install requirements
echo Step 4: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Check if model files exist
echo Step 5: Verifying model files...
if not exist "reg_clf.pkl" (
    echo WARNING: reg_clf.pkl not found
)
if not exist "rfe_clf.pkl" (
    echo WARNING: rfe_clf.pkl not found
)
if not exist "pca_clf.pkl" (
    echo WARNING: pca_clf.pkl not found
)
if not exist "Loan_Data_df.csv" (
    echo WARNING: Loan_Data_df.csv not found (required for PCA model)
)
echo.

REM Run the application
echo Step 6: Starting Loan Eligibility Prediction Application...
echo ========================================================
echo.
python app.py

pause
