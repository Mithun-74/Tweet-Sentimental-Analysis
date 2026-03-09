import gradio as gr
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and tokenizer
model = tf.keras.models.load_model("sentiment_model.keras")
tokenizer = pickle.load(open("tokenizer.pkl","rb"))

max_len = 100

label_map = {
    0:"Negative 😡",
    1:"Neutral 😐",
    2:"Positive 😊"
}

def predict_sentiment(text):

    seq = tokenizer.texts_to_sequences([text])
    pad = pad_sequences(seq,maxlen=max_len)

    pred = model.predict(pad)

    label = np.argmax(pred)

    confidence = np.max(pred)

    return label_map[label], f"Confidence: {confidence:.2f}"


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        # 🧠 Twitter Sentiment Analyzer
        ### Analyze whether a tweet is **Positive, Neutral, or Negative**

        This model is trained using **Deep Learning (LSTM)** on a large Twitter dataset.
        """
    )

    with gr.Row():

        with gr.Column():

            text_input = gr.Textbox(
                label="Enter a Tweet",
                placeholder="Type a tweet here...",
                lines=3
            )

            analyze_btn = gr.Button("Analyze Sentiment 🚀")

        with gr.Column():

            sentiment_output = gr.Textbox(label="Sentiment Result")
            confidence_output = gr.Textbox(label="Model Confidence")

    analyze_btn.click(
        fn=predict_sentiment,
        inputs=text_input,
        outputs=[sentiment_output, confidence_output]
    )

    gr.Markdown(
        """
        ---
        **Model:** LSTM Neural Network  
        **Dataset:** Twitter Sentiment Dataset  
        **Classes:** Negative / Neutral / Positive
        """
    )

demo.launch()