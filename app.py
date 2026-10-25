import streamlit as st
from google import genai

# Page configuration
st.set_page_config(
    page_title="AI-Powered LLM Toolkit",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI-Powered LLM Toolkit")
st.write("Perform AI tasks using Google's Gemini API.")

# Connect to Gemini
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error(
        "Gemini API key is missing. "
        "Please check Settings → Secrets."
    )
    st.stop()

# Select AI task
task = st.selectbox(
    "Choose a Task",
    [
        "Text Summarization",
        "Sentiment Analysis",
        "Question Answering",
        "Text Translation"
    ]
)

# Input fields
text = st.text_area("Enter your text")

question = ""
language = "English"

if task == "Question Answering":
    question = st.text_input("Enter your question")

elif task == "Text Translation":
    language = st.selectbox(
        "Select Target Language",
        ["English", "Tamil", "Hindi", "French", "Spanish"]
    )

# Generate response
if st.button("Generate"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif task == "Question Answering" and not question.strip():
        st.warning("Please enter your question.")
    else:
        # Create prompt
        if task == "Text Summarization":
            prompt = (
                "Summarize the following text clearly "
                "and concisely:\n\n" + text
            )

        elif task == "Sentiment Analysis":
            prompt = (
                "Analyze the sentiment of the following text. "
                "Classify it as Positive, Negative, or Neutral "
                "and explain briefly:\n\n" + text
            )

        elif task == "Question Answering":
            prompt = (
                "Answer the question using the given text.\n\n"
                "Context: " + text +
                "\n\nQuestion: " + question
            )

        else:
            prompt = (
                f"Translate the following text into {language}. "
                "Return only the translated text:\n\n" + text
            )

        # Call Gemini API
        try:
            with st.spinner("AI is generating your result..."):
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

            st.subheader("✨ Result")
            st.write(response.text)

        except Exception as e:
            st.error(f"API Error: {e}") 
