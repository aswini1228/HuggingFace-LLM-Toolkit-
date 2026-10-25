import streamlit as st
from google import genai

st.set_page_config(
    page_title="LLM Toolkit",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 LLM Toolkit")
st.write("AI-powered Text Processing using Gemini")

# Get Gemini API Key from Streamlit Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("Gemini API key missing! Check Streamlit Secrets.")
    st.stop()

task = st.selectbox(
    "Choose a Task",
    [
        "Text Summarization",
        "Sentiment Analysis",
        "Question Answering",
        "Text Translation"
    ]
)

if task == "Text Summarization":
    text = st.text_area("Enter text to summarize")

elif task == "Sentiment Analysis":
    text = st.text_area("Enter text for sentiment analysis")

elif task == "Question Answering":
    text = st.text_area("Enter context or passage")
    question = st.text_input("Enter your question")

else:
    text = st.text_area("Enter text to translate")
    language = st.selectbox(
        "Translate into",
        ["English", "Tamil", "Hindi", "French", "Spanish"]
    )

if st.button("Generate"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        if task == "Text Summarization":
            prompt = f"Summarize the following text clearly:\n{text}"

        elif task == "Sentiment Analysis":
            prompt = (
                "Analyze the sentiment of this text. "
                "Classify it as Positive, Negative, or Neutral "
                "and explain briefly:\n" + text
            )

        elif task == "Question Answering":
            if not question.strip():
                st.warning("Please enter a question.")
                st.stop()

            prompt = (
                f"Answer the question using the context below.\n"
                f"Context: {text}\n"
                f"Question: {question}"
            )

        else:
            prompt = (
                f"Translate the following text into {language}. "
                f"Return only the translated text:\n{text}"
            )

        try:
            with st.spinner("Generating response..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.subheader("Output")
            st.write(response.text)

        except Exception as e:
            st.error(f"API Error: {e}")
