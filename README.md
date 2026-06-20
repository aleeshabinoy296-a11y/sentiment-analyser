# Sentiment Analyser

An AI-powered web app that detects whether a piece of text is **positive**, **negative**, or **neutral** — built with Python, TextBlob, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red) ![TextBlob](https://img.shields.io/badge/TextBlob-NLP-green)

---

## What it does

- Takes any text input from the user
- Uses NLP (Natural Language Processing) to analyse the sentiment
- Shows a Positive / Negative / Neutral result
- Displays a Polarity score (-1 to +1) and a Subjectivity score (0 to 1)

---

## Tech stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Programming language |
| TextBlob | NLP library for sentiment analysis |
| Streamlit | Web app framework |

---

## How to run it locally

### Step 1 — Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/sentiment-analyser.git
cd sentiment-analyser
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## File structure

```
sentiment-analyser/
├── app.py             # Main application code
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

---

## What I learned

- How NLP sentiment analysis works (polarity and subjectivity)
- How to build and deploy a web app using Streamlit
- How to use the TextBlob library for text processing
- Git workflow: committing and pushing code to GitHub

---

## Future improvements

- [ ] Add support for multiple languages
- [ ] Show word-level sentiment highlighting
- [ ] Add a history of analysed texts
- [ ] Deploy to Streamlit Cloud (free hosting)

---
Live app: [https://sentiment-analyser-u9cslhencrfoebehmzfovp.streamlit.app/]

*Made by Aleesha Binoy — BCA Data Science & AI*
