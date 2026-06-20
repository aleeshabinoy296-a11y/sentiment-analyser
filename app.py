import streamlit as st
from textblob import TextBlob
import pandas as pd

# Page setup
st.set_page_config(page_title="Sentiment Analyser", page_icon="🙂", layout="centered")

st.title("🙂 Sentiment Analyser")
st.write("Type any sentence below and the AI will tell you if it sounds positive, negative, or neutral.")

# Keep history of everything analysed in this session
if "history" not in st.session_state:
    st.session_state.history = []

# Text input box
user_text = st.text_area("Enter your text here:", height=120, placeholder="e.g. I absolutely loved this movie!")

col_a, col_b = st.columns([1, 1])
with col_a:
    analyse_clicked = st.button("Analyse sentiment", use_container_width=True)
with col_b:
    clear_clicked = st.button("Clear history", use_container_width=True)

if clear_clicked:
    st.session_state.history = []
    st.rerun()

if analyse_clicked:
    if user_text.strip() == "":
        st.warning("Please type something first.")
    else:
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0.1:
            sentiment, emoji, color = "Positive", "😊", "green"
        elif polarity < -0.1:
            sentiment, emoji, color = "Negative", "😞", "red"
        else:
            sentiment, emoji, color = "Neutral", "😐", "gray"

        # Save to history
        st.session_state.history.append({
            "Text": user_text,
            "Sentiment": sentiment,
            "Polarity": round(polarity, 2),
            "Subjectivity": round(subjectivity, 2),
        })

        # Animated reveal
        st.markdown(f"## {emoji} :{color}[{sentiment}]")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Polarity score", f"{polarity:.2f}")
            st.progress((polarity + 1) / 2)  # maps -1..1 to 0..1 for the bar
        with col2:
            st.metric("Subjectivity score", f"{subjectivity:.2f}")
            st.progress(subjectivity)

        if sentiment == "Positive":
            st.balloons()
        elif sentiment == "Negative":
            st.snow()

        # Word-level breakdown — a nice extra touch
        with st.expander("See word-by-word sentiment breakdown"):
            words_data = []
            for word in blob.words:
                w_blob = TextBlob(word)
                words_data.append({"Word": word, "Polarity": round(w_blob.sentiment.polarity, 2)})
            st.dataframe(pd.DataFrame(words_data), use_container_width=True, hide_index=True)

# Show history as a chart if there's any
if st.session_state.history:
    st.divider()
    st.subheader("Session history")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.line_chart(df["Polarity"])

# Sidebar with info
with st.sidebar:
    st.header("About this app")
    st.write(
        "This app uses **TextBlob**, a Python library for natural "
        "language processing, to analyse the emotional tone of text."
    )
    st.write("Try comparing a few sentences and watch the history chart build up.")
    st.divider()
    st.caption("Built with Python, TextBlob, and Streamlit")