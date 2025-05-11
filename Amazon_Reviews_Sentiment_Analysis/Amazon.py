import streamlit as st
from joblib import load
import re
import contractions
from num2words import num2words
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from scipy.sparse import hstack, csr_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import emoji
import os

# Set Streamlit page config
st.set_page_config(page_title="Sentiment Classifier", layout="centered")

# Function to ensure NLTK resources are available
def ensure_nltk_data():
    resources = ["punkt", "stopwords", "wordnet", "omw-1.4", "punkt_tab"]
    for resource in resources:
        try:
            nltk.data.find(f"tokenizers/{resource}" if resource == "punkt" else f"corpora/{resource}")
        except LookupError:
            nltk.download(resource)

# Call the function to ensure NLTK data is available
ensure_nltk_data()

# Load models with caching to avoid reloading on every interaction
@st.cache_resource
def load_models():
    # Check for required files and load them
    required_files = ["neural_network.pkl", "vectorizer.pkl", "label_encoder.pkl"]
    for file in required_files:
        if not os.path.exists(file):
            st.error(f"❌ Required file '{file}' not found.")
            st.stop()
    model = load('neural_network.pkl')
    vectorizer = load('vectorizer.pkl')
    label_encoder = load('label_encoder.pkl')
    scaler = load("scaler.pkl") if os.path.exists("scaler.pkl") else None
    scaling_used = scaler is not None
    return model, vectorizer, label_encoder, scaler, scaling_used

# Load models and resources
model, vectorizer, label_encoder, scaler, scaling_used = load_models()

# Initialize NLP tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Emojis corresponding to sentiment classes
emoji_dict = {
    "Positive": "😃✨💖",
    "Neutral": "😐🌀🤷",
    "Negative": "👿💢👎"
}

# List of keywords indicating neutral sentiment
neutral_keywords = [
    'okay', 'fine', 'average', 'meh', 'just okay', 'not that much', 'not bad',
    'mediocre', 'so-so', 'alright', 'nothing special', 'kind of', 'could be better',
    'couldn’t care less', 'indifferent', 'okay-ish', 'neither good nor bad',
    'passable', 'acceptable', 'not great', 'nothing remarkable', 'alright-ish',
    'just fine', 'could be worse', 'not bad, not good', 'somewhat okay', 'meh, could be better',
    'nothing to complain about', 'barely noticeable', 'average at best', 'mediocre at best', 'tolerable'
]

# Preprocessing functions
def convert_ordinals(text):
    # Convert ordinal numbers to words
    return re.sub(r'\b(\d+)(st|nd|rd|th)\b', lambda m: num2words(int(m.group(1)), to='ordinal'), text)

def preprocess_review(review):
    # Lowercase and normalize text
    review = str(review).lower()
    review = convert_ordinals(review)
    review = contractions.fix(review)  # Expand contractions
    review = re.sub(r"http\S+", "", review)  # Remove URLs
    review = re.sub(r'\S*\d\S*', '', review).strip()  # Remove words with digits
    review = re.sub(r'[^a-zA-Z\s]', ' ', review)  # Remove non-letter characters
    review = re.sub(r'(.)\1{2,}', r'\1\1', review)  # Reduce repeated characters to two
    tokens = word_tokenize(review)  # Tokenize text
    # Lemmatize and remove stopwords
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words and (len(w) > 1 or w in {'no', 'ok', 'go'})]
    return ' '.join(tokens)

def analyze_emojis(text):
    # Count emojis in the input text
    return sum(1 for char in text if char in emoji.EMOJI_DATA)

def handle_neutral_keywords(text, probs, neutral_keywords, confidence_threshold=0.30):
    # Check for neutral keywords in text
    neutral_found = any(re.search(rf'\b{re.escape(kw)}\b', text.lower()) for kw in neutral_keywords)
    if neutral_found:
        return 'Neutral', 100.0  # Force Neutral label with 100% confidence
    elif probs[1] >= confidence_threshold:
        return 'Neutral', probs[1] * 100  # Use model's neutral class probability
    else:
        return None, None

def get_confidence_from_probas(probs, label_classes):
    # Get predicted label and associated confidence percentage
    label_index = np.argmax(probs)
    label = label_classes[label_index]
    confidence = probs[label_index] * 100
    return label, confidence

# Initialize session state keys for user input and prediction results
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""
if "input_key" not in st.session_state:
    st.session_state["input_key"] = 0
if "prediction_result" not in st.session_state:
    st.session_state["prediction_result"] = None

# Header section with styling
st.markdown("""
<div style='text-align: center; padding: 15px; border: 1px solid #ddd; border-radius: 10px;'>
    <h3>📦 Amazon Reviews Sentiment Analyzer 🛒💳</h3>
    <p style='font-size:16px;'>Classify product reviews as <b style='color:green;'>Positive</b>, <b style='color:orange;'>Neutral</b>, or <b style='color:red;'>Negative</b></p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Example Buttons section to autofill sample reviews
st.markdown("""
<div style='border: 1px solid #ddd; border-radius: 10px; padding: 15px; text-align:center;'>
    <h4>📋 Try an example</h4>
    <p style='font-size:14px;'>Click any button below to auto-fill the example in the input box.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Layout for example buttons
col_ex1, col_ex2, col_ex3 = st.columns([2, 6, 2])
with col_ex2:
    col1, col2, col3 = st.columns(3)
    if col1.button("😃 Positive"):
        st.session_state["user_input"] = "Absolutely love this product! Works like a charm. 😍"
        st.session_state["prediction_result"] = None  # Clear previous prediction
    if col2.button("😐 Neutral"):
        st.session_state["user_input"] = "It's okay, nothing too great or too bad. 😐😕"
        st.session_state["prediction_result"] = None
    if col3.button("👿 Negative"):
        st.session_state["user_input"] = "Terrible experience. Waste of money. 🤬"
        st.session_state["prediction_result"] = None

# Text input area
st.markdown(
    """
    <div style="text-align:center; font-weight:bold; font-size:18px; margin-bottom:5px;">
        ✍️ Enter your review here:
    </div>
    """,
    unsafe_allow_html=True,
)
user_input = st.text_area(
    "",
    value=st.session_state["user_input"],
    key=f"user_input_{st.session_state['input_key']}",
    height=100,
    label_visibility="collapsed"  # Hide default label
)

# Buttons for prediction and reset
col_left, col_center, col_right = st.columns([1.5, 2, 1.5])
with col_center:
    col1, col2 = st.columns(2)
    predict_clicked = col1.button("🔍 Predict", use_container_width=True)
    reset_clicked = col2.button("🧹 Reset All", use_container_width=True)

# Reset logic: clear input and prediction result on reset
if reset_clicked:
    st.session_state["user_input"] = ""
    st.session_state["input_key"] += 1  # Increment key to reset text area
    st.session_state["prediction_result"] = None  # Clear prediction result

# Prediction logic triggered on button click
if predict_clicked:
    if not user_input.strip():
        st.warning("⚠️ Please enter a review.")  # Warn if input is empty
    else:
        # Preprocess user input
        clean_text = preprocess_review(user_input)
        tfidf_input = vectorizer.transform([clean_text])  # Vectorize text input

        # Extract engineered features
        review_len = len(clean_text)
        word_count = len(clean_text.split())
        exclam_count = user_input.count("!")
        extra_features = [[review_len, word_count, exclam_count]]

        # Scale features if scaler is used
        if scaling_used:
            extra_features = scaler.transform(extra_features)
        extra_sparse = csr_matrix(extra_features)
        final_input = hstack([tfidf_input, extra_sparse])  # Combine vectorized text and features

        # Predict probabilities and label
        probs = model.predict_proba(final_input)[0]
        prediction = model.predict(final_input)[0]

        label_classes = list(label_encoder.classes_)
        label = label_encoder.inverse_transform([prediction])[0]

        # Check for neutral keywords and adjust label/confidence accordingly
        label, confidence = handle_neutral_keywords(user_input, probs, neutral_keywords)

        # If no neutral override, get label and confidence from model probabilities
        if label is None:
            label, confidence = get_confidence_from_probas(probs, label_classes)

        # Calculate sentiment polarity score using TextBlob
        sentiment_score = TextBlob(clean_text).sentiment.polarity
        emoji_count_val = analyze_emojis(user_input)  # Count emojis in original input

        # Determine probabilities to display in pie chart, especially if neutral forced
        if label == "Neutral" and confidence == 100.0:
            display_probs = np.array([0.0, 1.0, 0.0])  # Forced Neutral by neutral keywords
        else:
            display_probs = probs

        # Store all prediction related info in session state for display below
        st.session_state["prediction_result"] = {
            "label": label,
            "confidence": confidence,
            "display_probs": display_probs,
            "review_len": review_len,
            "word_count": word_count,
            "exclam_count": exclam_count,
            "emoji_count_val": emoji_count_val,
            "sentiment_score": sentiment_score,
            "user_input": user_input,
            "probs": probs,
            "label_classes": label_classes,
        }

# If prediction result exists in session state, display results
if st.session_state["prediction_result"] is not None:
    res = st.session_state["prediction_result"]
    label = res["label"]
    confidence = res["confidence"]
    display_probs = res["display_probs"]
    review_len = res["review_len"]
    word_count = res["word_count"]
    exclam_count = res["exclam_count"]
    emoji_count_val = res["emoji_count_val"]
    sentiment_score = res["sentiment_score"]
    user_input = res["user_input"]

    # Display prediction result with styled HTML
    st.markdown(f"""
    <div style='text-align:center; border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px auto; max-width: 600px;'>
        <h2 style='color:#0099ff;'>📢 Prediction Result</h2>
        <div style='font-size:20px; color:{"green" if label == "Positive" else "orange" if label == "Neutral" else "red"};'>
            {"😃 <b>Positive</b>" if label == "Positive" else "😐 <b>Neutral</b>" if label == "Neutral" else "👿 <b>Negative</b>"} <span style='font-size:16px;'>(Confidence Score: {confidence:.2f}%)</span>
        </div>
        <div style='margin-top: 5px;'>{'✅ Appreciative/Praiseful Tone' if label == "Positive" else '🌀 Fair/Balanced/Impartial Tone' if label == "Neutral" else '⚠️ Critical/Disappointed Tone'}</div>
    </div>
    """, unsafe_allow_html=True)

    # Create two columns side by side for confidence breakdown and analysis
    col1, col2 = st.columns(2)

    # Confidence breakdown (Pie chart)
    with col1:
        with st.container():
            st.markdown("""
            <div style='border: 1px solid #ddd; border-radius: 10px; padding: 20px; width: 100%;'>
                <h4 style='text-align:center;'>📈 Confidence Breakdown</h4>
            </div>
            """, unsafe_allow_html=True)

        # Map sentiment to index for probability adjustment
        sentiment_to_idx = {"Positive": 0, "Neutral": 1, "Negative": 2}
        conf_frac = confidence / 100
        probs_adj = display_probs.copy()
        pred_idx = sentiment_to_idx[label]
        other_indices = [i for i in range(3) if i != pred_idx]
        other_sum = display_probs[other_indices].sum()

        # Adjust other probabilities to sum to (1 - confidence)
        if other_sum > 0:
            for i in other_indices:
                probs_adj[i] = display_probs[i] * (1 - conf_frac) / other_sum
        else:
            for i in other_indices:
                probs_adj[i] = 0.0

        # Set predicted class probability to confidence fraction
        probs_adj[pred_idx] = conf_frac

        # Colors for pie chart slices: green, yellow, red
        colors = ['#28a745', '#ffc107', '#dc3545']
        fig, ax = plt.subplots(figsize=(5, 3.5))  # less tall pie chart

        # Plot pie chart with adjusted probabilities
        wedges, texts, autotexts = ax.pie(
            probs_adj,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            wedgeprops={'edgecolor': 'black'},
            pctdistance=0.75,
            labeldistance=1.1
        )

        # Set font size for labels and autopct text
        for text in texts:
            text.set_fontsize(12)
        for autotext in autotexts:
            autotext.set_fontsize(12)
            autotext.set_color('black')

        # Add legend with sentiment names and color patches
        ax.legend(wedges, ["Positive", "Neutral", "Negative"], title="Sentiments", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

        ax.axis('equal')  # Equal aspect ratio ensures pie is circular
        st.pyplot(fig)  # Render pie chart in Streamlit

    # Review analysis section displaying features and sentiment score
    with col2:
        st.markdown("""
        <div style='border: 1px solid #ddd; border-radius: 10px; padding: 20px; width: 100%;'>
            <h4 style='text-align:center;'>📊 Review Analysis</h4>
        </div>
        """, unsafe_allow_html=True)

        # Display analysis details as HTML list
        st.markdown(f"""
            <div style='padding: 12px;'>
                <ul style='font-size:16px;'>
                    <li><b>📝 Review Length:</b> {review_len} characters</li>
                    <li><b>📚 Word Count:</b> {word_count}</li>
                    <li><b>❗❗ Exclamation Marks:</b> {exclam_count}</li>
                    <li><b>😃 Emoji Count:</b> {emoji_count_val}</li>
                    <li><b>❤️ Sentiment Score:</b> {sentiment_score:.3f}</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Prepare dataframe for download with prediction and features
    output_df = pd.DataFrame([{
        "Review": user_input,
        "Prediction": label,
        "Confidence": f"{confidence:.2f}%",
        "Length": review_len,
        "Word Count": word_count,
        "Exclamation Count": exclam_count,
        "Emoji Count": emoji_count_val,
        "Sentiment Score": sentiment_score
    }])

    # Download button centered in layout
    col_dl1, col_dl2, col_dl3 = st.columns([2, 6, 2])
    with col_dl2:
        st.download_button("⬇️ Download Result as CSV", output_df.to_csv(index=False), file_name="review_prediction.csv", use_container_width=True)

    # Footer note about the model
    st.markdown("""
    <div style='text-align:center; padding-top: 10px;'>
        <span style='font-size:13px; color: gray;'>🤖 Powered by Neural Network | TF-IDF + Engineered Features</span>
    </div>
    """, unsafe_allow_html=True)

    # Celebrate prediction with balloons animation
    st.balloons()
