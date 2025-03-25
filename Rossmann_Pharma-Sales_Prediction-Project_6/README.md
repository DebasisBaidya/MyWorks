**Sales Forecasting Across Multiple Retail Stores for Rossmann Pharmaceuticals**

## Streamlit Deployed Dashboard Link
🔗 [Deployed Dashboard Link](https://salesforecastingproject-6-baycznp8znqyhupggduqbm.streamlit.app/)  
🔗 [Embed Code](https://salesforecastingproject-6-baycznp8znqyhupggduqbm.streamlit.app/?embed_options=show_toolbar,show_padding,show_footer,light_theme,show_colored_line)  

This project predicts sales trends using Machine Learning and Deep Learning models, designed to assist businesses in planning and decision-making. The final solution is deployed as an interactive Streamlit dashboard for easy accessibility.

## Project Overview
The project follows a structured workflow involving data preprocessing, machine learning modeling, deep learning implementation, and dashboard deployment. Each phase is outlined below:

## Step 1: Data Preprocessing & EDA (`Task 1.ipynb`)
In this step:
- The dataset was cleaned by handling missing values and ensuring data consistency.
- Exploratory Data Analysis (EDA) was performed to uncover patterns, trends, and insights crucial for model training.
- Key features such as `DayOfWeek`, `Promo`, and `StateHoliday` were analyzed to assess their impact on sales.

## Step 2: Machine Learning Model (`Task 2-2.5 ML.ipynb`)
- Various regression models were explored to predict sales based on features like store details, promotions, and holidays.
- The best-performing model was selected based on evaluation metrics such as RMSE and MAE.
- Feature importance analysis provided insights into the most influential variables.

## Step 3: Deep Learning Model (`Task 2.6 DL.ipynb`)
- An LSTM (Long Short-Term Memory) neural network was developed to enhance prediction accuracy by capturing temporal dependencies in the sales data.

## Step 4: Streamlit Deployment (`task 2.7-3.py`)
- The trained LSTM model was integrated into a Streamlit dashboard for seamless user interaction.
- Users can upload CSV or Excel files with necessary data fields, receive instant predictions, and visualize results.
- The dashboard includes interactive graphs for predicted sales trends and a feature importance visualization (generated using random values as a placeholder).

## Features
- ✅ Simple interface for easy use, Excel or CSV File upload i.e. Test Data
- ✅ Uploaded Data Preview
- ✅ Displays the last available date with Uploaded File Name from uploaded data for better context
- ✅ Predicts sales for the next 6 weeks
- ✅ CSV download option for predicted results
- ✅ Interactive visualizations for better insights i.e. Prediction Graph & Feature Importance Dashboard

## How to Use
1. Upload a CSV/Excel file with the required columns: `Id`, `Store`, `DayOfWeek`, `Open`, `Promo`, `StateHoliday`, `SchoolHoliday`, `Date`.
2. View predicted sales trends in both tabular and graphical formats.
3. Download the results as a CSV file if needed.

Effortlessly predict future sales trends with interactive visualizations and detailed insights. 🚀
