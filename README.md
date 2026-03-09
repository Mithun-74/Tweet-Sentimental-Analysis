# 🧠 Twitter Sentiment Analyzer (LSTM + Gradio)

A deep learning based **Sentiment Analysis Web App** that classifies tweets into **Negative, Neutral, or Positive** sentiments using an **LSTM Neural Network**.

The model is trained on a large Twitter sentiment dataset and deployed as an interactive web application using **Gradio** and **Hugging Face Spaces**.

---

## 🚀 Live Demo

🔗 Hugging Face App:  
[https://huggingface.co/spaces/Mithun74/Tweet_Sentiment_Analysis](https://huggingface.co/spaces/Mithun74/Tweet_Sentimental_Analysis)

---

## 📌 Project Overview

Social media platforms contain large amounts of user opinions.  
This project builds an **AI-powered sentiment classifier** capable of analyzing tweets and predicting whether the sentiment is:

- 😡 Negative
- 😐 Neutral
- 😊 Positive

The system uses **Natural Language Processing (NLP)** and **Deep Learning (LSTM)** to understand textual sentiment.

---

## 📊 Dataset

Dataset used:

Sentiment Analysis Dataset from Kaggle

🔗 https://www.kaggle.com/datasets/abdelmalekeladjelet/sentiment-analysis-dataset

Dataset distribution:

| Sentiment | Count |
|----------|------|
| Positive | 103059 |
| Neutral | 82972 |
| Negative | 55114 |

---

## ⚙️ Model Architecture

The model is built using **TensorFlow / Keras**.

Pipeline:

Text Input  
↓  
Text Cleaning  
↓  
Tokenizer  
↓  
Padding Sequences  
↓  
Embedding Layer  
↓  
Bidirectional LSTM  
↓  
Dense Layer  
↓  
Softmax Classification  

### Neural Network
