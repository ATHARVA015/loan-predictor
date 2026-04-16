#!/bin/bash
# Loan Eligibility Prediction - Quick Setup Script for macOS/Linux
# This script sets up the environment and runs the application

echo ""
echo "========================================================"
echo "Loan Eligibility Prediction - Setup Script"
echo "========================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python 3.8 or higher from https://www.python.org/"
    exit 1
fi

echo "Step 1: Checking Python installation..."
python3 --version
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Step 2: Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created successfully"
else
    echo "Step 2: Virtual environment already exists, skipping creation"
fi
echo ""

# Activate virtual environment
echo "Step 3: Activating virtual environment..."
source venv/bin/activate
echo ""

# Install requirements
echo "Step 4: Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo ""

# Check if model files exist
echo "Step 5: Verifying model files..."
[ ! -f "reg_clf.pkl" ] && echo "WARNING: reg_clf.pkl not found"
[ ! -f "rfe_clf.pkl" ] && echo "WARNING: rfe_clf.pkl not found"
[ ! -f "pca_clf.pkl" ] && echo "WARNING: pca_clf.pkl not found"
[ ! -f "Loan_Data_df.csv" ] && echo "WARNING: Loan_Data_df.csv not found (required for PCA model)"
echo ""

# Run the application
echo "Step 6: Starting Loan Eligibility Prediction Application..."
echo "========================================================"
echo ""
python3 app.py
