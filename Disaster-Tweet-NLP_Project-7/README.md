# 🌍 Disaster Tweet Classification (NLP Project)

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-brightgreen?logo=streamlit)](https://disaster-tweet-nlp-debasis-baidya.streamlit.app)
[![re](https://img.shields.io/badge/re-Regex-blue)](https://docs.python.org/3/library/re.html)
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

This project is about classifying tweets to check whether they are related to a real disaster or not using NLP techniques. It covers everything from text cleaning, feature extraction, model building, and finally deployment.

- 🚀 **Live App**: [Streamlit Link](https://disaster-tweet-nlp-debasis-baidya.streamlit.app)
- 📺 **All About My App**: [Demo Video Link](https://youtu.be/VebH__P0o5s)

---

## 📌 Problem Statement

Sometimes people tweet about disasters, and sometimes they just use words like “fire” or “storm” in a casual way. The goal here is to build a model that can tell whether a tweet is actually referring to a real disaster or not.

---

## 🧠 What’s Inside

- Cleaned the tweets by removing links, mentions, hashtags, special characters, etc.
- Used **TF-IDF** for feature extraction
- Combined it with features like sentiment score, tweet length, hashtag/mention count
- Tried out models like **Logistic Regression**, **Random Forest**, etc.
- Built a simple but interactive **Streamlit app** to make predictions easily

---

## 🖥️ Streamlit App Features

- 🔍 Type or paste any tweet and get a real-time prediction
- 📋 Try out predefined examples with one click
- 📈 View confidence score in a pie chart
- 📊 Analyze the tweet: sentiment, length, emoji count, etc.
- ⬇️ Download prediction as a CSV file
- 🧠 All backed by Logistic Regression with TF-IDF + extra features

---

## 🧪 Example

If you enter a tweet like: "BREAKING: Uncontrolled forest fires ravaging California, claiming lives 🔥💔"


The model will predict:  
**🚨 Disaster** (with a confidence score)

---

## 🔍 How the App Works (Behind the Scenes)

1. **Text Preprocessing**:
   - Removes noise like URLs, numbers, mentions, etc.
   - Tokenizes and lemmatizes the tweet
   - Filters stopwords

2. **Feature Extraction**:
   - TF-IDF vector
   - Sentiment polarity using TextBlob
   - Tweet length, hashtag count, mention presence

3. **Model Prediction**:
   - Logistic Regression model trained on the cleaned dataset
   - Probability scores returned and interpreted live

4. **Interactive UI**:
   - Everything handled using Streamlit with instant feedback
   - Pie chart for confidence
   - Tweet-level breakdown and downloadable result

---

## 📸 App Preview

![App Screenshot](app_screenshot.png)

> Screenshot of Hosted Streamlit Dashboard.

---

## 📁 Project Files

- `Disaster Tweet Classifier.ipynb`: The main notebook with code and models
- `tweet.py`: Streamlit app logic
- `requirements.txt`: List of packages used for Streamlit
- `vectorizer.pkl` & `Logistic_Regression.pkl`: Model + vectorizer files

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

