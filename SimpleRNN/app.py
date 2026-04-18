import streamlit as st
from utils import predict_sentiment

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

st.title("🎬 IMDB Sentiment Analysis (Simple RNN)")
st.write("Enter a movie review and get sentiment prediction.")

# Input
review = st.text_area("Enter your review:")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        sentiment, score = predict_sentiment(review)
        
        st.subheader(f"Sentiment: {sentiment}")
        st.write(f"Confidence Score: {score:.2f}")
        
        # Progress bar
        st.progress(float(score))
        
        if sentiment == "Positive":
            st.success("This is a positive review 😊")
        else:
            st.error("This is a negative review 😐")