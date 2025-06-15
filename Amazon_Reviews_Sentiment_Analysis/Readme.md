# 📦 Amazon Reviews Sentiment Analysis (NLP Project)

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen?logo=streamlit)](https://debasis-baidya-amazonreviewssentiment-nlp.streamlit.app/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-blueviolet?logo=python&logoColor=white)](https://www.nltk.org/)
[![TextBlob](https://img.shields.io/badge/TextBlob-Sentiment-yellowgreen)](https://textblob.readthedocs.io/en/dev/)
[![WordCloud](https://img.shields.io/badge/WordCloud-Used-lightblue)](https://amueller.github.io/word_cloud/)
[![scipy.sparse](https://img.shields.io/badge/SciPy.sparse-SparseMatrix-orange)](https://docs.scipy.org/doc/scipy/reference/sparse.html)
[![joblib](https://img.shields.io/badge/Joblib-ModelSaving-darkgreen)](https://joblib.readthedocs.io/)
[![pickle](https://img.shields.io/badge/Pickle-Serialization-green)](https://docs.python.org/3/library/pickle.html)
[![tqdm](https://img.shields.io/badge/tqdm-ProgressBar-teal)](https://tqdm.github.io/)
[![collections](https://img.shields.io/badge/collections-DataStructures-lightgrey)](https://docs.python.org/3/library/collections.html)
[![transformers](https://img.shields.io/badge/Transformers-HuggingFace-red?logo=huggingface&logoColor=white)](https://huggingface.co/transformers/)
[![os](https://img.shields.io/badge/OS_Module-Used-lightgrey)](https://docs.python.org/3/library/os.html)
[![IPython.display](https://img.shields.io/badge/IPython.display-Jupyter-magenta)](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


This project focuses on classifying Amazon product reviews into **Positive**, **Neutral**, or **Negative** sentiments using NLP and Machine/Deep Learning. The app is built using **Streamlit** and allows for real-time sentiment prediction with visual feedback.

- 🚀 **Live App**: [Click to Open App](https://debasis-baidya-amazonreviewssentiment-nlp.streamlit.app)
- 📺 **All About My App**: [App Usage Demo](https://youtu.be/8qG7-s3eflk)
---

## 📌 Problem Statement

In today’s e-commerce world, customer reviews hold massive value. But manually reading each one to gauge sentiment is time-consuming. This project aims to automate that by using machine learning to predict the sentiment behind each review.

---

## 🧠 What’s Inside

- Cleaned the review texts (lowercased, removed URLs/digits/punctuation, lemmatized)
- Converted text into **TF-IDF vectors**
- Engineered features like:
  - Review length
  - Word count
  - Exclamation count
  - Emoji count
  - TextBlob sentiment score
- Trained a **Neural Network** classifier with SMOTE for balance
- Built an interactive **Streamlit** app for live predictions

---

## 🖥️ Streamlit App Features

- ✍️ Type or paste any product review and get real-time predictions
- 📋 One-click examples for Positive, Neutral, and Negative cases
- 📈 Pie chart showing sentiment confidence scores
- 📊 Review-level analysis (length, emojis, polarity, etc.)
- ⬇️ Download results as a CSV
- 🤖 Powered by TF-IDF + engineered features + Neural Network

---

## 🔍 How the App Works (Behind the Scenes)

1. **Preprocessing**:
   - Expands contractions, removes noise, normalizes text
   - Lemmatizes and tokenizes using NLTK

2. **Feature Extraction**:
   - TF-IDF vector
   - Extra numerical features
   - Emoji count and polarity score

3. **Prediction**:
   - Neural Network outputs probabilities
   - Includes keyword-based override for detecting neutral sentiments

4. **Visualization**:
   - Interactive pie chart
   - Detailed feature breakdown
   - Exportable results

---

## 📸 App Preview

<p align="center">
  <img src="app_screenshot_1.png" alt="App Screenshot 1" width="45%" style="margin-right:10px;">
  <img src="app_screenshot_2.png" alt="App Screenshot 2" width="45%">
</p>

> Screenshot of Hosted Streamlit App in action.

---

## 📁 Project Files

- `Amazon_Sentiment_Analysis.ipynb` – Main Jupyter notebook: preprocessing, modeling, evaluation
- `Amazon.py` – Streamlit app to deploy the classifier with an interactive UI
- `neural_network.pkl` – Trained MLPClassifier (Neural Network) model
- `vectorizer.pkl` – Saved TF-IDF vectorizer for consistent inputs
- `label_encoder.pkl` – Encodes/decodes sentiment labels
- `scaler.pkl` – Scaler used for numerical feature normalization
- `requirements.txt` – All required libraries for Streamlit

---

## 🙋‍♂️ About Me

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
