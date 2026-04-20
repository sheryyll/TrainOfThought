import pickle
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

@st.cache_resource
def load_assets():
    model     = tf.keras.models.load_model("next_word_lstm.keras")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    with open("model_config.pkl", "rb") as f:
        cfg = pickle.load(f)
    return model, tokenizer, cfg["max_sequence_len"]

model, tokenizer, max_sequence_len = load_assets()


def predict_next_word(text, top_k=5):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1):]
    padded = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
    probs  = model.predict(padded, verbose=0)[0]
    top_indices  = np.argsort(probs)[-top_k:][::-1]
    index_to_word = {v: k for k, v in tokenizer.word_index.items()}
    return [(index_to_word.get(i, "<UNK>"), float(probs[i])) for i in top_indices]


def generate_text(seed, num_words):
    result = seed
    for _ in range(num_words):
        preds = predict_next_word(result, top_k=1)
        if not preds:
            break
        result += " " + preds[0][0]
    return result

# streamlit app
st.set_page_config(page_title="Next Word Prediction", page_icon="📝")
st.title(" Next Word Prediction")
st.caption("Trained on Shakespeare — Hamlet")

tab1, tab2 = st.tabs(["🔮 Predict next word", "✍️ Generate text"])

# Tab 1 — single next-word prediction
with tab1:
    user_input = st.text_input(
        "Enter a phrase:",
        value="to be or not to be",
        placeholder="Type some Shakespeare..."
    )
    top_k = st.slider("Show top N predictions", 1, 10, 5)

    if st.button("Predict", use_container_width=True):
        if user_input.strip():
            with st.spinner("Predicting..."):
                predictions = predict_next_word(user_input.strip(), top_k=top_k)

            st.subheader("Predictions")
            for rank, (word, prob) in enumerate(predictions, 1):
                col1, col2 = st.columns([3, 7])
                col1.markdown(f"**{rank}. {word}**")
                col2.progress(prob, text=f"{prob*100:.1f}%")
        else:
            st.warning("Please enter some text first.")

# Tab 2 — text generation
with tab2:
    seed_text  = st.text_input(
        "Seed phrase:",
        value="the quality of mercy",
        placeholder="Starting phrase..."
    )
    num_words  = st.slider("Words to generate", 1, 30, 10)

    if st.button("Generate", use_container_width=True):
        if seed_text.strip():
            with st.spinner("Generating..."):
                output = generate_text(seed_text.strip(), num_words)
            st.subheader("Generated text")
            st.info(output)
        else:
            st.warning("Please enter a seed phrase first.")

st.divider()
st.caption("Model: LSTM  |  Corpus: All Shakespeare (NLTK Gutenberg)")
