import streamlit as st
import pandas as pd
import numpy as np
import pickle
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# Setting up the Streamlit page with title and wide layout
st.set_page_config(page_title='📂 LSTM Sales Prediction - File Upload', layout='wide')

# Loading the trained LSTM model and pre-fitted scalers
# These are required to preprocess the input data and make predictions
model = keras.models.load_model('lstm.keras')
with open('scaler_X.pkl', 'rb') as f:
    scaler_X = pickle.load(f)
with open('scaler_y.pkl', 'rb') as f:
    scaler_y = pickle.load(f)

# Function to preprocess input data
# This function scales the necessary numeric features before passing them to the model
def preprocess_data(df):
    num_cols = ['Id', 'Store', 'DayOfWeek', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday']
    df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce')  # Convert necessary columns to numeric
    df.fillna(0, inplace=True)  # Replace any missing values with 0
    df_scaled = df.copy()
    df_scaled[num_cols] = scaler_X.transform(df[num_cols])  # Apply the scaler to standardize input features
    X_scaled = np.array(df_scaled[num_cols]).reshape((df_scaled.shape[0], 1, len(num_cols)))  # Reshape data for LSTM input format
    return X_scaled

# Function to make predictions using the trained model
def make_predictions(X_scaled):
    y_pred_scaled = model.predict(X_scaled)  # Get predictions in scaled format
    y_pred = scaler_y.inverse_transform(y_pred_scaled)  # Convert predictions back to original scale
    return y_pred.flatten()

# Function to generate future dates for visualization
# This creates a list of weekly intervals based on the most recent date in the dataset
def generate_future_dates(last_date, weeks=6):
    return [(last_date + timedelta(weeks=i)).strftime('%d/%m/%Y') for i in range(1, weeks + 1)]

# Function to visualize predictions using a line plot
def prediction_graph(pred_dates, y_pred):
    df_graph = pd.DataFrame({'Date': pred_dates, 'Predicted Sales': y_pred})
    st.markdown('<div style="text-align: center; padding: 10px; border: 1px solid #ddd; margin-top: 20px; margin-bottom: 10px;"><h3>📉 Prediction Graph</h3></div>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    plt.plot(df_graph['Date'], df_graph['Predicted Sales'], marker='o', linestyle='-', color='blue')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Predicted Sales')
    plt.title('Predicted Sales Over Time')
    st.pyplot(plt)

# Function to display a placeholder feature importance dashboard
def feature_importance():
    importance = np.random.rand(7)  # Generate random feature importance values (placeholder)
    features = ['Id', 'Store', 'DayOfWeek', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday']
    st.markdown('<div style="text-align: center; padding: 10px; border: 1px solid #ddd; margin-top: 20px; margin-bottom: 10px;"><h3>📊 Feature Importance Dashboard</h3></div>', unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importance, y=features)
    plt.title('Feature Importance')
    plt.xlabel('Importance')
    plt.ylabel('Features')
    st.pyplot(plt)

# Displaying the dashboard title
st.markdown('<h1 style="text-align:center;">📂 LSTM Rossmann Pharmaceuticals Sales Forecasting Dashboard - Upload File to Predict</h1>', unsafe_allow_html=True)

# Displaying instructions for required columns in the uploaded file
st.markdown('<div style="text-align: center; border: 1px solid #ddd; padding: 10px; margin-bottom: 20px;">Required Columns: Id, Store, DayOfWeek, Open, Promo, StateHoliday, SchoolHoliday, Date as in Test Data</div>', unsafe_allow_html=True)

# File uploader to accept CSV or Excel files
uploaded_file = st.file_uploader('', type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Reading the uploaded file into a pandas DataFrame
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    last_date = pd.to_datetime(df['Date'].max())  # Get the latest date in the dataset
    X_scaled = preprocess_data(df)  # Preprocess the data
    y_pred = make_predictions(X_scaled)  # Generate predictions
    pred_dates = generate_future_dates(last_date)  # Create future prediction dates
    predictions = pd.DataFrame({'Date': pred_dates, 'Predicted Sales': [f'{val:.2f}' for val in y_pred[:6]]})  # Format predictions to 2 decimal places

    # Displaying the last available date in the uploaded file
    st.markdown('---')
    st.markdown(f'<div style="text-align: center; margin-top: 10px; border: 1px solid #ddd; padding: 10px;"><strong>Last Available Date in Uploaded Filename ({uploaded_file.name}):</strong> {last_date.strftime("%d/%m/%Y")}</div>', unsafe_allow_html=True)

    # Displaying data preview and predictions
    col3, col4 = st.columns([1, 1], gap="medium")
    with col3:
        st.markdown('<div style="text-align: center; margin-top: 20px; border: 1px solid #ddd; padding: 10px;"><strong>Preview of Uploaded Data:</strong></div>', unsafe_allow_html=True)
        st.write(df.head(), use_container_width=True)
    with col4:
        st.markdown('<div style="text-align: center; margin-top: 20px; border: 1px solid #ddd; padding: 10px;"><strong>Future Prediction Dates & Predicted Sales (6 weeks):</strong></div>', unsafe_allow_html=True)
        st.write(predictions, use_container_width=True)
        if st.button('Download Predictions as CSV'):
            predictions.to_csv('predictions.csv', index=False)
            st.write('✅ Predictions saved successfully!')

    st.markdown('---')

    # Displaying prediction graph and feature importance section
    col1, col2 = st.columns([1, 1], gap="medium")
    with col1:
        prediction_graph(pred_dates, y_pred[:6])
    with col2:
        feature_importance()
