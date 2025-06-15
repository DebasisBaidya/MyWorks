# 🏬 Sales Forecasting Across Multiple Retail Stores for Rossmann Pharmaceuticals

[![Python](https://img.shields.io/badge/Python-Used-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit&logoColor=white)](https://salesforecastingproject-6-baycznp8znqyhupggduqbm.streamlit.app/)
[![Logging](https://img.shields.io/badge/Python-Logging-informational?logo=python&logoColor=white)](https://docs.python.org/3/library/logging.html)
[![SciPy](https://img.shields.io/badge/SciPy-Used-blue?logo=scipy&logoColor=white)](https://scipy.org/)
[![Statsmodels](https://img.shields.io/badge/statsmodels-Used-lightgrey)](https://www.statsmodels.org/)
[![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange?logo=mlflow&logoColor=white)](https://mlflow.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Model-orange?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep_Learning-red?logo=keras&logoColor=white)](https://keras.io/)
[![Pickle](https://img.shields.io/badge/Pickle-Serialization-green)](https://docs.python.org/3/library/pickle.html)
[![OS](https://img.shields.io/badge/OS_Module-Used-lightgrey)](https://docs.python.org/3/library/os.html)


---

## 📊 Streamlit Deployed Dashboard

🔗 **Live Tool/App**: [Streamlit Link](https://salesforecastingproject-6-baycznp8znqyhupggduqbm.streamlit.app/)  

---

## 🧾 Project Overview

This project forecasts sales across multiple retail outlets using Machine Learning and Deep Learning. It helps businesses plan better using future sales predictions and key trend insights.

🎯 **Goal**:  
To build a predictive model and interactive dashboard for future retail sales planning.

🛠️ **Workflow**:  
Data Preprocessing ➜ Machine Learning ➜ Deep Learning (LSTM) ➜ Streamlit App

---

## 🔹 Step 1:  
### 🧹 Data Preprocessing & EDA (`Task 1.ipynb`)

- 🧽 Cleaned missing values, checked consistency  
- 📈 Performed EDA to identify patterns, trends, insights crucial in sales for model training.
- 📊 Explored features like `DayOfWeek`, `Promo`, and `StateHoliday` to assess their impact on sales.

---

## 🔹 Step 2:  
### 🤖 Machine Learning Model (`Task 2-2.5 ML.ipynb`)

- 🧠 Trained multiple regression models  
- 📉 The best-performing model was selected based on evaluation metrics such as RMSE and MAE.  
- 🔍 Identified most important features driving sales  

---

## 🔹 Step 3:  
### 🧠 Deep Learning with LSTM (`Task 2.6 DL.ipynb`)

- ⏳ Used LSTM (Long Short-Term Memory) neural network to capture time-based patterns & to enhance prediction accuracy by capturing temporal dependencies in the sales data. 
- ⚡ Achieved enhanced performance over ML models  

---

## 🔹 Step 4:  
### 📲 Streamlit App Deployment (`Task 2.7-3.py`)

- 🖥️ Built interactive dashboard with input file support for seamless user interaction.
- ⛲ Users can upload CSV or Excel files with necessary data fields, receive instant predictions, and visualize results.
- 📆 Predicts future sales and shows trend graphs  
- 💾 Exports predictions as downloadable CSV  

---

## 📸 App Preview

![App Screenshot](Hosted%20Streamlit%20Dashboard.png)

> Screenshot of Hosted Streamlit Dashboard.

---

## ✨ Features

- 📁 Upload CSV/Excel with test data  
- 📌 See uploaded file name & last available date  
- 📊 Predicts next 6 weeks’ sales  
- 📉 Shows result table + prediction graph  
- ⬇️ Download predicted results as CSV  
- 📋 Feature importance visualization (simulated)

---

## 🚀 How to Use

1. 🔗 Click on the dashboard link above.  
2. 📤 Upload a file with required columns:  
   - `Id`, `Store`, `DayOfWeek`, `Open`, `Promo`, `StateHoliday`, `SchoolHoliday`, `Date`  
3. 📈 See forecast results and download them as needed.

---

## 📌 Why This Project Matters

- 📈 Helps retail chains plan ahead and manage inventory  
- 🧠 Combines both traditional ML and LSTM time-series modeling  
- 🧪 Makes advanced forecasting accessible with an easy UI  
- 🌐 Useful for analysts, decision-makers, and non-tech users alike

---

## 👤 About Me

**Debasis Baidya**  
Senior MIS | Data Science Intern  
✅ Automated 80%+ of manual processes at my workplace  
📊 Skilled in Python, Power BI, SQL, Google Apps Script, ML, DL, NLP  
<p align="left">
  📫 <strong>Connect with me:</strong>&nbsp;

  <a href="https://www.linkedin.com/in/debasisbaidya">
    <img src="https://img.shields.io/badge/LinkedIn-View_Profile-blue?logo=linkedin&logoColor=white" />
  </a>

  <a href="mailto:speak2debasis@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-Mail_Me-red?logo=gmail&logoColor=white" />
  </a>

  <a href="https://api.whatsapp.com/send?phone=918013316086&text=Hi%20Debasis!">
    <img src="https://img.shields.io/badge/WhatsApp-Message-green?logo=whatsapp&logoColor=white" />
  </a>
</p>

---

⭐ If you found this project helpful, don’t forget to **star this repo** and stay connected!
