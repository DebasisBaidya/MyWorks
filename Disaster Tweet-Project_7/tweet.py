import streamlit as st
import joblib
import pickle
import re
import regex
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
from scipy.sparse import hstack
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd

# Download NLTK data
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Load vectorizer and model
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

model = joblib.load("Logistic_Regression.pkl")

# Initialize NLP components
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Helper functions
def decontracted(phrase):
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can't", "can not", phrase)
    phrase = re.sub(r"let's", "let us", phrase)
    phrase = re.sub(r"n't", " not", phrase)
    phrase = re.sub(r"'re", " are", phrase)
    phrase = re.sub(r"'ll", " will", phrase)
    phrase = re.sub(r"'ve", " have", phrase)
    phrase = re.sub(r"'m", " am", phrase)
    phrase = re.sub(r"'d", " would", phrase)
    return phrase

def preprocess_tweet(text):
    text = decontracted(text)
    text = re.sub(r"\S*\d\S*", "", text).strip()
    text = re.sub(r"[^A-Za-z]+", " ", text)
    text = text.replace("#", "").replace("_", " ")
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens if word.lower() not in stop_words]
    return " ".join(tokens)

def count_emojis(text):
    import emoji
    return sum(1 for char in text if char in emoji.EMOJI_DATA)

def extract_features(clean_text, raw):
    tfidf_input = vectorizer.transform([clean_text])
    sentiment = TextBlob(clean_text).sentiment.polarity
    tweet_len = len(clean_text)
    num_hashtags = raw.count("#")
    has_mention = int("@" in raw)
    extra_feat = np.array([[sentiment, tweet_len, num_hashtags, has_mention]])
    return hstack([tfidf_input, extra_feat])

# Initialize Streamlit page
st.set_page_config(page_title="Disaster Tweet Detector", layout="centered")

# Initialize session state
if "tweet_input" not in st.session_state:
    st.session_state.tweet_input = ""

# -------------------- UI Layout --------------------

# Header
st.markdown("""
<div style='text-align: center; padding: 15px; border: 1px solid #ddd; border-radius: 10px;'>
    <h1>🌪️ Disaster Tweet Detector</h1>
    <p style='font-size:16px;'>Classify tweets as <b style='color:red;'>Disaster</b> 🚨 or <b style='color:green;'>Non-Disaster</b> ✅</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Try an Example (with buttons inside)
st.markdown("""
<div style='border: 1px solid #ddd; border-radius: 10px; padding: 15px; text-align:center;'>
    <h4>📋 Try an example</h4>
    <p style='font-size:14px;'>Click any button below to auto-feed the example in the input box.</p>
</div>
""", unsafe_allow_html=True)

col_ex1, col_ex2, col_ex3 = st.columns([3, 8, 3])
with col_ex2:
     # Add a gap above the buttons
    st.markdown("<br>", unsafe_allow_html=True)

    col_b1, col_b2 = st.columns(2)
    if col_b1.button("✅ Puppy Tweet 🐶"):
        st.session_state.tweet_input = "Just got a new puppy, he's so cute! 🐾"
    if col_b2.button("🔥 Fire Alert Tweet 🚨"):
        st.session_state.tweet_input = "BREAKING: Uncontrolled forest fires ravaging California, claiming countless animal lives 🔥💔 Urgent action needed! @US_President, we need your help NOW to combat this disaster #SaveCalifornia #StopTheBurn"


# Input field
st.markdown("<div style='text-align:center;'><label style='font-size:16px;font-weight:bold;'>✍️ Enter a tweet to classify:</label></div>", unsafe_allow_html=True)
tweet_input = st.text_area("", value=st.session_state.tweet_input, height=100, label_visibility="collapsed")

# Buttons
col_left, col_center, col_right = st.columns([1.5, 2, 1.5])
with col_center:
    col1, col2 = st.columns(2)
    predict_clicked = col1.button("🔍 Predict", use_container_width=True)
    clear_clicked = col2.button("🧹 Reset All", use_container_width=True)

if clear_clicked:
    st.session_state.tweet_input = ""  # Clears session state input
    tweet_input = ""  # Clears the text area input box immediately
  


if predict_clicked:
    if not tweet_input.strip():
        st.warning("⚠️ Please enter a tweet to analyze.")
    else:
        st.session_state.tweet_input = tweet_input
        clean_text = preprocess_tweet(tweet_input)
        features = extract_features(clean_text, tweet_input)
        prediction_proba = model.predict_proba(features)[0]
        prediction = int(np.argmax(prediction_proba))
        confidence = prediction_proba[prediction]
        sentiment_score = TextBlob(clean_text).sentiment.polarity
        emoji_count = count_emojis(tweet_input)

        mood = "😊 Casual / Friendly Tone" if sentiment_score >= 0.3 else (
               "🔥 Urgent / Alarming Tone" if sentiment_score <= -0.2 else "💬 Matter-of-Fact Tone")

        with st.spinner("Analyzing tweet..."):
            time.sleep(1.5)

        # Prediction Result
        st.markdown(f"""
        <div style='text-align:center; border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px auto; max-width: 600px;'>
            <h2 style='color:#0099ff;'>📢 Prediction Result</h2>
            <div style='font-size:20px; color:{"red" if prediction == 1 else "green"};'>
                {"🚨 <b>Disaster</b>" if prediction == 1 else "✅ <b>Non-Disaster</b>"} <span style='font-size:16px;'>(Confidence: {confidence:.2%})</span>
            </div>
            <div style='margin-top: 5px;'>{'🛑 Emergency or disaster related content.' if prediction == 1 else '☑️ Likely personal or casual tweet.'}</div>
            <div style='margin-top: 10px; font-style: italic; color: gray;'>{mood}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Side-by-side output boxes
        col1, col2 = st.columns(2)

        # Confidence Breakdown
        with col1:
            with st.container():
                st.markdown("""
                <div style='border: 1px solid #ddd; border-radius: 10px; padding: 20px; width: 100%;'>
                    <h4 style='text-align:center;'>📈 Confidence Breakdown</h4>
                """, unsafe_allow_html=True)

                # Resize the pie chart to fit properly
                fig, ax = plt.subplots(figsize=(2.5, 2))  # Adjusted figure size for better fit
                ax.pie(prediction_proba, labels=["Non-Disaster", "Disaster"], autopct="%1.1f%%", colors=["#8BC34A", "#FF5252"])
                ax.axis("equal")
                st.pyplot(fig)

                st.markdown("</div>", unsafe_allow_html=True)

        # Tweet Analysis
        with col2:
            st.markdown("""
            <div style='border: 1px solid #ddd; border-radius: 10px; padding: 20px; width: 100%;'>
                <h4 style='text-align:center;'>📊 Tweet Analysis</h4>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <div style='padding: 12px;'>
                    <ul style='font-size:16px;'>
                        <li><b>🧠 Sentiment Score:</b> {sentiment_score:.3f}</li>
                        <li><b>📝 Tweet Length:</b> {len(clean_text)} characters</li>
                        <li><b>#️⃣ Hashtags Count:</b> {tweet_input.count("#")}</li>
                        <li><b>👥 Mentions Present:</b> {int('@' in tweet_input)}</li>
                        <li><b>😊 Emoji Count:</b> {emoji_count}</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

        # Save prediction CSV with additional details
        output_df = pd.DataFrame([{
            "Tweet": tweet_input,
            "Prediction": "Disaster" if prediction == 1 else "Non-Disaster",
            "Confidence": f"{confidence:.2%}",
            "Sentiment Score": sentiment_score,
            "Tweet Length": len(clean_text),
            "Hashtags Count": tweet_input.count("#"),
            "Mentions Present": int('@' in tweet_input),
            "Emoji Count": emoji_count
        }])


        # Download Button Alignment
        col_dl1, col_dl2, col_dl3 = st.columns([2, 6, 2])  # Adjust columns to center the button
        with col_dl2:
            st.download_button("⬇️ Download Prediction as CSV", output_df.to_csv(index=False), file_name="tweet_prediction.csv", use_container_width=True)


        st.markdown("""
        <div style='text-align:center; padding-top: 10px;'>
            <span style='font-size:13px; color: gray;'>🤖 Powered by Logistic Regression | TF-IDF + Sentiment + Length + Hashtags + Mentions</span>
        </div>
        """, unsafe_allow_html=True)
