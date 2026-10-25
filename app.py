import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="LLM Text Toolkit",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 LLM Text Toolkit")
st.write("### Hugging Face Pipelines")
st.write(
    "Perform summarization, translation, "
    "sentiment analysis and question answering."
)

st.divider()

task = st.selectbox(
    "Choose an NLP Task",
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

    st.subheader("📝 Text Summarization")

    text = st.text_area(
        "Enter a paragraph",
        height=200,
        placeholder="Enter a long paragraph here..."
    )

    if st.button("Summarize", use_container_width=True):

        if text.strip():

            try:
                with st.spinner("Generating summary..."):

                    model = load_model(task)

                    result = model(
                        text,
                        max_length=100,
                        min_length=20,
                        do_sample=False,
                        truncation=True
                    )

                st.success("Summary generated!")
                st.write(result[0]["summary_text"])

            except Exception as e:
                st.error("Unable to summarize the text.")
                st.info(
                    "Please check the app logs if the error continues."
                )

        else:
            st.warning("Please enter a paragraph.")


elif task == "Translation":

    st.subheader("🌐 English to French Translation")

    text = st.text_area(
        "Enter English text",
        height=150,
        placeholder="I love learning Artificial Intelligence."
    )

    if st.button("Translate", use_container_width=True):

        if text.strip():

            try:
                with st.spinner("Translating..."):

                    model = load_model(task)
                    result = model(
                        text,
                        max_length=200
                    )

                st.success("Translation completed!")
                st.write(result[0]["translation_text"])

            except Exception:
                st.error(
                    "Translation failed. Please check the app logs."
                )

        else:
            st.warning("Please enter some text.")


elif task == "Sentiment Analysis":

    st.subheader("❤️ Sentiment Analysis")

    text = st.text_area(
        "Enter a sentence",
        height=120,
        placeholder="I love this product!"
    )

    if st.button("Analyze Sentiment", use_container_width=True):

        if text.strip():

            try:
                with st.spinner("Analyzing sentiment..."):

                    model = load_model(task)
                    result = model(text)

                label = result[0]["label"]
                score = result[0]["score"]

                st.success("Analysis completed!")

                if label == "POSITIVE":
                    st.success("Sentiment: Positive 😊")
                else:
                    st.error("Sentiment: Negative 😞")

                st.write("Confidence Score:", round(score, 4))

                st.progress(float(score))

            except Exception:
                st.error(
                    "Sentiment analysis failed. Check the app logs."
                )

        else:
            st.warning("Please enter a sentence.")


elif task == "Question Answering":

    st.subheader("❓ Question Answering")

    context = st.text_area(
        "Enter a paragraph",
        height=200,
        placeholder=(
            "Python is a popular programming language "
            "used to develop Artificial Intelligence applications."
        )
    )

    question = st.text_input(
        "Ask a question",
        placeholder="Which language is used to develop AI applications?"
    )

    if st.button("Get Answer", use_container_width=True):

        if context.strip() and question.strip():

            try:
                with st.spinner("Finding the answer..."):

                    model = load_model(task)

                    result = model(
                        question=question,
                        context=context
                    )

                st.success("Answer found!")
                st.info(result["answer"])

                st.caption(
                    "Confidence Score: "
                    + str(round(result["score"], 4))
                )

            except Exception:
                st.error(
                    "Question answering failed. "
                    "Please check the app logs."
                )

        else:
            st.warning(
                "Please enter both the paragraph and the question."
            )


st.divider()

st.caption(
    "Built using Streamlit and Hugging Face Transformers"
                )
