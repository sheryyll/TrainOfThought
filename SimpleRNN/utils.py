import re
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Load word index
word_index = imdb.get_word_index()

# Load model
model = load_model('simple_rnn_imdb.keras')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    words = text.split()
    encoded = [word_index.get(word, 2) + 3 for word in words]
    
    padded = sequence.pad_sequences([encoded], maxlen=500)
    return padded

def predict_sentiment(review):
    processed = preprocess_text(review)
    prediction = model.predict(processed)
    
    score = float(prediction[0][0])
    sentiment = "Positive" if score > 0.5 else "Negative"
    
    return sentiment, score