import streamlit as st
import requests

st.set_page_config(
    page_title="Hugging Face LLM Toolkit",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Hugging Face LLM Toolkit")
st.write("Summarization, Translation, Sentiment Analysis, and Question Answering")

HF_TOKEN = st.secrets.get("HF_TOKEN", "")

TASKS = {
    "Summarization": "facebook/bart-large-cnn",
    "Translation (English to French)": "Helsinki-NLP/opus-mt-en-fr",
    "Sentiment Analysis": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    "Question Answering": "deepset/roberta-base-squad2"
}

task = st.selectbox("Choose a task", list(TASKS.keys()))

text = st.text_area(
    "Enter your text",
    placeholder="Paste your paragraph here..."
)

question = ""

if task == "Question Answering":
    question = st.text_input("Enter your question")

if st.button("Run Task", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif task == "Question Answering" and not question.strip():
        st.warning("Please enter a question.")
    elif not HF_TOKEN:
        st.error("HF_TOKEN is missing. Add your Hugging Face token in Streamlit Secrets.")
    else:
        model = TASKS[task]

        url = f"https://router.huggingface.co/hf-inference/models/{model}"

        headers = {
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json"
        }

        if task == "Question Answering":
            payload = {
                "inputs": {
                    "question": question,
                    "context": text
                }
            }
        else:
            payload = {"inputs": text}

        try:
            with st.spinner("Processing..."):
                response = requests.post(
                    url,
                    headers=headers,
                    json=payload,
                    timeout=90
                )

            if response.ok:
                result = response.json()
                st.subheader("Result")

                if task == "Summarization":
                    st.write(result[0]["summary_text"])
                elif task == "Translation (English to French)":
                    st.write(result[0]["translation_text"])
                elif task == "Sentiment Analysis":
                    st.write(result)
                else:
                    st.write("Answer:", result.get("answer", "No answer found"))
                    st.write("Confidence:", result.get("score", "N/A"))

            else:
                st.error(f"API Error ({response.status_code})")
                st.write(response.text)

        except requests.exceptions.RequestException as error:
            st.error(f"Connection error: {error}")

st.divider()
st.caption("Built using Python, Streamlit, and Hugging Face Inference API.")
