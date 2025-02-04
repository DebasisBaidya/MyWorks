# Feature Analysis and Price Prediction for Handsets

## Overview

This project aims to predict the price of mobile phones based on various features like memory size, RAM, battery capacity, and more. By applying machine learning, the goal is to provide a tool that helps manufacturers set competitive prices and assists consumers in understanding price differences. The dataset used contains 541 rows and 12 columns with no missing values.

## What This Project Covers

- **Data Exploration**: Analyzing the dataset to understand patterns and relationships between features.
- **Data Preprocessing**: Cleaning and preparing data through steps like handling outliers, feature extraction, and encoding.
- **Model Building**: Training multiple machine learning models, including Linear Regression, Decision Tree, Random Forest, and XGBoost.
- **Hyperparameter Tuning**: Optimizing the XGBoost model using GridSearchCV for better performance.
- **Evaluation**: Comparing models using metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² score.
- **Feature Analysis**: Understanding which features have the most impact on price prediction.

## Key Results

- **Best Model**: The Random Forest Regressor emerged as the top-performing model:
  - **MAE**: 1340.23
  - **RMSE**: 1998.53
  - **R²**: 93.16%
  - **Why Random Forest?**: Despite the lower MAE achieved by the tuned XGBoost model, Random Forest consistently performed well across all metrics and demonstrated strong explanatory power (high R²). Its stability makes it the most reliable choice for this task.

- **XGBoost Performance**: After tuning, the XGBoost model achieved:
  - **MAE**: 36.78
  - This shows its potential for further exploration in future iterations.

## Tools and Libraries Used

- **Languages**: Python
- **Libraries**: 
  - Data Analysis: NumPy, Pandas
  - Visualization: Matplotlib, Seaborn
  - Machine Learning: Scikit-learn, XGBoost
  - Model Saving: Joblib

## Files Included

- **`Project 4.ipynb`**: A step-by-step notebook containing the entire process, from data exploration to final predictions.
- **`handset_price_model.pkl`**: The saved Random Forest model that can be used to predict handset prices on new data.

## Why This Project Matters

Mobile pricing is a critical factor for both manufacturers and consumers. This project demonstrates how data-driven models can:

1. Help manufacturers set competitive and fair prices.
2. Provide insights into the key factors influencing mobile phone prices.
3. Enhance transparency and trust in pricing for consumers.

## Future Directions

- Further optimization of the XGBoost model to leverage its potential.
- Expanding the dataset to include more diverse handset features and brands.
- Exploring other machine learning techniques like neural networks for improved accuracy.

This project combines data analysis, machine learning, and practical applications to make mobile pricing smarter and more efficient.

