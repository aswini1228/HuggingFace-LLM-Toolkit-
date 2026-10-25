import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="LLM Text Toolkit",
    page_icon="🤖"
)

st.title("🤖 LLM Text Toolkit")
st.write("Hugging Face Pipelines")
st.write(
    "Summarization | Translation | "
    "Sentiment Analysis | Question Answering"
)

st.divider()

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

    if task_name == "Summarization":
        return pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

    elif task_name == "Translation":
        return pipeline(
            "translation",
            model="Helsinki-NLP/opus-mt-en-fr"
        )

    elif task_name == "Sentiment Analysis":
        return pipeline(
            "sentiment-analysis",
            model=(
                "distilbert/"
                "distilbert-base-uncased-finetuned-sst-2-english"
            )
        )

    elif task_name == "Question Answering":
        return pipeline(
            "question-answering",
            model=(
                "distilbert/"
                "distilbert-base-cased-distilled-squad"
            )
        )


if task == "Summarization":

    text = st.text_area(
        "Enter a paragraph",
        height=200
    )

    if st.button("Summarize"):

        if text.strip():

            try:
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

            except Exception as e:
                st.error("Summarization failed.")
                st.code(str(e))

        else:
            st.warning("Please enter a paragraph.")


elif task == "Translation":

    text = st.text_area(
        "Enter English text",
        height=150
    )

    if st.button("Translate"):

        if text.strip():

            try:
                with st.spinner("Translating..."):
                    model = load_model(task)
                    result = model(
                        text,
                        max_length=200
                    )

                st.subheader("French Translation")
                st.write(result[0]["translation_text"])

            except Exception as e:
                st.error("Translation failed.")
                st.code(str(e))

        else:
            st.warning("Please enter text.")


elif task == "Sentiment Analysis":

    text = st.text_area(
        "Enter a sentence",
        height=120
    )

    if st.button("Analyze Sentiment"):

        if text.strip():

            try:
                with st.spinner("Analyzing..."):
                    model = load_model(task)
                    result = model(text)

                st.subheader("Sentiment")
                st.write("Label:", result[0]["label"])
                st.write(
                    "Confidence:",
                    round(result[0]["score"], 4)
                )

            except Exception as e:
                st.error("Sentiment analysis failed.")
                st.code(str(e))

        else:
            st.warning("Please enter a sentence.")


elif task == "Question Answering":

    context = st.text_area(
        "Enter a paragraph",
        height=200
    )

    question = st.text_input("Enter your question")

    if st.button("Get Answer"):

        if context.strip() and question.strip():

            try:
                with st.spinner("Finding the answer..."):
                    model = load_model(task)
                    result = model(
                        question=question,
                        context=context
                    )

                st.subheader("Answer")
                st.success(result["answer"])
                st.write(
                    "Confidence:",
                    round(result["score"], 4)
                )

            except Exception as e:
                st.error("Question answering failed.")
                st.code(str(e))

        else:
            st.warning(
                "Please enter both paragraph and question."
            )


st.divider()
st.caption("Built with Streamlit and Hugging Face Transformers")
