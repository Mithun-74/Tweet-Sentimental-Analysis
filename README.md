# Tweet Sentiment Analysis

This repository contains a simple Twitter sentiment analyzer built with TensorFlow and Gradio. The model classifies tweets as **Negative**, **Neutral**, or **Positive** based on an LSTM network.

## Features

- Pretrained Keras LSTM model (`sentiment_model.keras`)
- Tokenizer for tweet preprocessing
- Gradio web interface for interactive prediction

## Screenshot

![Gradio Interface](./img/screenshot.png)

> *Replace `img/screenshot.png` with the path to your actual screenshot file.*

## Description

The `app.py` script loads the trained model and tokenizer, defines a `predict` function for processing text input, and launches a Gradio interface. When launched, open the provided URL in a browser to type or paste a tweet and receive a sentiment prediction.

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Tweet_sentiment_analysis.git
   cd Tweet_sentiment_analysis
   ```

2. Create and activate a virtual environment (Windows PowerShell example):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Start the app:
   ```powershell
   python app.py
   ```

   Gradio will output a local URL (e.g. `http://127.0.0.1:7860`) where you can interact with the model.

## Execution Link

Once running, use the link shown in the terminal to access the Gradio interface. An example is:

```
http://127.0.0.1:7860
```

## License

This project is licensed under the MIT License.