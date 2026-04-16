# 🚀 Deployment Guide - Streamlit Cloud

## Overview
Deploy your Loan Eligibility Predictor to **Streamlit Cloud** (FREE, easy, no credit card needed).

---

## 🎯 Prerequisites

- ✅ GitHub account (you have this!)
- ✅ Git installed on your computer
- ✅ All project files ready

---

## 📋 Step 1: Prepare Local Repository

### 1.1 Check Git Status
```bash
cd d:\loan-approval-2\Loan_Eligibility_Prediction
git status
```

### 1.2 Add All Files
```bash
git add .
```

### 1.3 Commit Changes
```bash
git commit -m "Loan Eligibility Predictor - Ready for deployment"
```

### 1.4 Check Remote
```bash
git remote -v
```

If no remote, add it:
```bash
git remote add origin https://github.com/YOUR_USERNAME/loan-eligibility-prediction.git
```

---

## 🔧 Step 2: Push to GitHub

### 2.1 Create Repository on GitHub

1. Go to **https://github.com/new**
2. Fill in details:
   - **Repository name:** `loan-eligibility-prediction`
   - **Description:** Loan eligibility prediction using machine learning
   - **Public:** ✓ (required for Streamlit Cloud free tier)
   - Click **Create repository**

### 2.2 Push Code to GitHub

```bash
git branch -M main
git push -u origin main
```

You'll be asked to authenticate - use GitHub credentials or personal access token.

---

## 🌐 Step 3: Deploy to Streamlit Cloud

### 3.1 Go to Streamlit Cloud
1. Visit **https://share.streamlit.io**
2. Click **"New app"** button (top left)

### 3.2 Connect GitHub Repository

1. **GitHub account:** Select your account (authorize if needed)
2. **Repository:** `loan-eligibility-prediction`
3. **Branch:** `main`
4. **Main file path:** `streamlit_app.py`
5. Click **Deploy!**

### 3.3 Wait for Deployment
- Takes 2-5 minutes first time
- You'll see a green checkmark when ready
- URL will be: `https://YOUR_USERNAME-loan-eligibility-prediction.streamlit.app`

---

## ✅ Step 4: Verify Deployment

1. Click the shared link
2. Test all 3 models with sample data
3. Verify predictions work

---

## 📊 Deployment Checklist

- [ ] Git repository created locally
- [ ] All files committed to git
- [ ] GitHub repository created
- [ ] Code pushed to GitHub (main branch)
- [ ] Streamlit Cloud connected
- [ ] App deployed successfully
- [ ] App URL generated
- [ ] All 3 models working in cloud

---

## 🔗 Useful Links

| Link | Purpose |
|------|---------|
| https://github.com/new | Create GitHub repo |
| https://share.streamlit.io | Streamlit Cloud |
| https://docs.streamlit.io/deploy/streamlit-cloud | Deployment docs |

---

## 🐛 Troubleshooting

### **"Module not found" Error**
- Verify `requirements.txt` has all packages
- Check Python version compatibility

### **App Shows Old Code**
- Wait 5 minutes for cache to clear
- Or hard refresh: `Ctrl+Shift+R`

### **App Crashes on Load**
- Check "Manage app" → "Settings" → logs
- Look for error messages

### **Models Not Loading**
- Verify `.pkl` files are in repo
- Check file paths in `streamlit_app.py`

---

## 📝 Files Required for Deployment

```
✓ streamlit_app.py          - Main app
✓ app.py                    - CLI version (optional)
✓ requirements.txt          - Dependencies
✓ reg_clf.pkl              - Baseline model
✓ rfe_clf.pkl              - RFE model
✓ pca_clf.pkl              - PCA model
✓ Loan_Data.csv            - Original data
✓ Loan_Data_df.csv         - Processed data
✓ .gitignore              - Git ignore rules
```

---

## 🎉 After Deployment

### Share Your App
- **Share link:** `https://YOUR_USERNAME-loan-eligibility-prediction.streamlit.app`
- **Embed in portfolio:** Use URL in projects
- **Social media:** Share on LinkedIn, GitHub

### Monitor Performance
- Visit **https://share.streamlit.io** → Your apps
- View analytics, logs, and health metrics

### Update App
- Make changes locally
- Commit and push to GitHub: `git push`
- Streamlit Cloud auto-deploys in 2-5 minutes

---

## 💡 Pro Tips

1. **Custom Domain:** Connect custom domain (paid feature)
2. **Secrets Management:** Store API keys in Streamlit Cloud secrets
3. **Caching:** Add `@st.cache_resource` for faster loads
4. **Performance:** Monitor app health in Streamlit Cloud dashboard

---

## ❓ Need Help?

- Streamlit docs: https://docs.streamlit.io
- GitHub docs: https://docs.github.com
- Streamlit forum: https://discuss.streamlit.io

---

**Happy deploying! 🚀**
