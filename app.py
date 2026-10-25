import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="LLM Text Toolkit",
    page_icon="🤖"
)

st.title("🤖 LLM Text Toolkit")
st.write("Hugging Face Pipelines using Streamlit")

task = st.selectbox(
    "Choose a task",
    [
        "Summarization",
        "Translation",
        "Sentiment Analysis",
        "Question Answering"
    ]
)

@st.cache_resource
def load_model(task_name):
    models = {
        "Summarization": "sshleifer/distilbart-cnn-12-6",
        "Translation": "Helsinki-NLP/opus-mt-en-fr",
        "Sentiment Analysis": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        "Question Answering": "distilbert/distilbert-base-cased-distilled-squad"
    }

    task_types = {
        "Summarization": "summarization",
        "Translation": "translation_en_to_fr",
        "Sentiment Analysis": "sentiment-analysis",
        "Question Answering": "question-answering"
    }

    return pipeline(
        task_types[task_name],
        model=models[task_name]
    )

if task == "Summarization":

    text = st.text_area("Enter a long paragraph")

    if st.button("Summarize"):
        if text.strip():
            with st.spinner("Summarizing..."):
                model = load_model(task)
                result = model(
                    text,
                    max_length=100,
                    min_length=20,
                    do_sample=False,
                    truncation=True
                )

            st.subheader("Summary")
            st.write(result[0]["summary_text"])
        else:
            st.warning("Please enter some text.")

elif task == "Translation":

    text = st.text_area("Enter English text")

    if st.button("Translate"):
        if text.strip():
            with st.spinner("Translating..."):
                model = load_model(task)
                result = model(text, max_length=200)

            st.subheader("French Translation")
            st.write(result[0]["translation_text"])
        else:
            st.warning("Please enter some text.")

elif task == "Sentiment Analysis":

    text = st.text_area("Enter a sentence")

    if st.button("Analyze Sentiment"):
        if text.strip():
            with st.spinner("Analyzing sentiment..."):
                model = load_model(task)
                result = model(text)

            st.subheader("Result")
            st.write("Sentiment:", result[0]["label"])
            st.write("Confidence:", round(result[0]["score"], 4))
        else:
            st.warning("Please enter some text.")

elif task == "Question Answering":

    context = st.text_area("Enter a paragraph")
    question = st.text_input("Ask a question")

    if st.button("Get Answer"):
        if context.strip() and question.strip():
            with st.spinner("Finding answer..."):
                model = load_model(task)
                result = model(
                    question=question,
                    context=context
                )

            st.subheader("Answer")
            st.write(result["answer"])
        else:
            st.warning("Enter both paragraph and question.")
