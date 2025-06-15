# 📱 Project 4: Feature Analysis and Price Prediction for Handsets

[![Python](https://img.shields.io/badge/Python-Used-blue?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Used-purple?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Used-lightgrey?logo=pandas&logoColor=black)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow?logo=scikitlearn&logoColor=black)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Used-orange?logo=python&logoColor=white)](https://xgboost.readthedocs.io/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Used-blue?logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Used-orange?logo=matplotlib&logoColor=white)](https://matplotlib.org/)

---

## 🧾 Overview

This project aims to predict the price of mobile phones based on various features like memory size, RAM, battery capacity, and more.  
By applying machine learning, the goal is to provide a tool that helps manufacturers set competitive prices and assists consumers in understanding price differences.  
The dataset used contains **541 rows** and **12 columns** with no missing values.

---

## 🧠 What This Project Covers

- 🔍 **Data Exploration**: Analyzing the dataset to understand patterns and relationships between features.  
- 🧼 **Data Preprocessing**: Cleaning and preparing data through steps like handling outliers, feature extraction, and encoding.  
- 🏗️ **Model Building**: Training multiple ML models – Linear Regression, Decision Tree, Random Forest, and XGBoost.  
- 🛠️ **Hyperparameter Tuning**: Optimizing XGBoost using GridSearchCV.  
- 📊 **Evaluation**: Comparing models using MAE, RMSE, and R² score.  
- 💡 **Feature Analysis**: Identifying which features most affect price prediction.

---

## 🏆 Key Results

### ✅ Best Model: **Random Forest Regressor**
- **MAE**: 1340.23  
- **RMSE**: 1998.53  
- **R²**: 93.16%

> 🔎 **Why Random Forest?**  
Despite the lower MAE achieved by tuned XGBoost, Random Forest showed consistently strong performance across all metrics and higher explanatory power (R²), making it a reliable choice.

### ⚙️ Tuned XGBoost Results
- **MAE**: 36.78  
> This indicates strong potential for future fine-tuning and exploration.

---

## 🧰 Tools and Libraries Used

- 🐍 **Language**: Python  
- 🧮 **Libraries**:  
  - **Data Analysis**: NumPy, Pandas  
  - **Visualization**: Matplotlib, Seaborn  
  - **ML Models**: Scikit-learn, XGBoost  
  - **Model Saving**: Joblib  

---

## 📁 Files Included

- `Project 4.ipynb`: Full process from EDA to model building.  
- `handset_price_model.pkl`: Saved Random Forest model to predict prices on unseen data.

---

## 🎯 Why This Project Matters

Pricing strategy plays a crucial role in market competition and consumer choice.  
This project helps in:

1. 🏷️ Enabling fair and competitive pricing decisions for manufacturers.  
2. 📈 Revealing the key influencers on handset pricing.  
3. 🔍 Increasing price transparency for buyers.

---

## 🚀 Future Directions

- 🔧 Fine-tune XGBoost further to unleash its full potential.  
- 📦 Expand the dataset to include more brands and features.  
- 🧠 Explore deep learning models for even higher accuracy.

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

> ⭐ If you found this project helpful or insightful, feel free to give it a ⭐ star and connect with me!
