# AI-Powered LLM Toolkit
# demonstrations link:https://pasj2z4a9q3xcbmvrn2iau.streamlit.app/

## Project Overview

The AI-Powered LLM Toolkit is a web-based application developed using Python, Streamlit, and Google's Gemini API. It uses Large Language Model (LLM) capabilities to perform various natural language processing tasks through a simple and user-friendly interface.

The application supports text summarization, sentiment analysis, question answering, and text translation. Users can enter text, select a task, and generate AI-powered results.

## Objectives

- To develop an AI-powered text-processing application.
- To integrate Google's Gemini API with Streamlit.
- To summarize lengthy text into concise information.
- To analyze sentiment in user-provided text.
- To answer questions based on the provided context.
- To translate text into different languages.
- # Screenshots
- 

## Features

### 1. Text Summarization

Summarizes lengthy text into short, meaningful content while preserving the main ideas.

### 2. Sentiment Analysis

Analyzes the given text and classifies its sentiment into three categories:

- Positive
- Negative
- Neutral

### 3. Question Answering

Generates answers to user questions based on the context provided by the user.

### 4. Text Translation

Translates text into a selected target language, including English, Tamil, Hindi, French, and Spanish.

### 5. User-Friendly Interface

Provides an interactive interface developed using Streamlit, allowing users to select tasks and view results easily.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- GitHub
- Streamlit Community Cloud

## System Requirements

- Python 3.10 or a compatible version
- Internet connection
- Google Gemini API key
- Required Python packages
- Web browser

## Project Structure


AI-Powered-LLM-Toolkit/
|
|-- app.py
|-- requirements.txt
|-- README.m
File Description
app.py: Contains the Streamlit user interface and Gemini API integration.
requirements.txt: Lists the Python packages required to run the application.
README.md: Provides project documentation, features, and setup instructions.
How It Works
The user opens the web application.
The user selects an AI task from the available options.
The user enters text or a question.
The application generates an appropriate prompt based on the selected task.
The prompt is sent to the Gemini API.
The Gemini model processes the input and generates a response.
The generated result is displayed on the Streamlit interface.''' text
Installation and Setup
Step 1: Clone the Repository
Clone the project repository to your local system.
git clone YOUR_GITHUB_REPOSITORY_URL
Step 2: Navigate to the Project Directory
cd AI-Powered-LLM-Toolkit
Step 3: Install Dependencies
Install the required Python packages using the following command.
pip install -r requirements.txt
Step 4: Configure the Gemini API Key
Create a .streamlit directory in the project folder and create a secrets.toml file inside it.
Add the following configuration:
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
Replace YOUR_GEMINI_API_KEY with your actual Gemini API key.
Never publish your API key in a public repository or share it publicly.
Step 5: Run the Application
Start the Streamlit application using the following command.
streamlit run app.py
The application will open in your default web browser.
### Deployment
The application can be deployed using Streamlit Community Cloud.
Deployment Steps
Upload the project files to GitHub.
Open Streamlit Community Cloud.
Sign in and connect your GitHub account.
Select the project repository.
Choose app.py as the main application file.
Open the application settings.
Add the GEMINI_API_KEY under the Secrets section.
Deploy the application.
After successful deployment, the application can be accessed through its Streamlit URL.
Expected Output
The application provides four main text-processing tasks.
Task
### Description
Expected Result
Text Summarization
Summarizes lengthy text
A concise summary
Sentiment Analysis
Identifies the sentiment of text
Positive, Negative, or Neutral classification
### Question Answering
Answers questions using the supplied context
A relevant answer
### Text Translation
Translates text into the selected language
Translated text
### Applications
The AI-Powered LLM Toolkit can be used in several areas:
Educational content summarization
Customer feedback analysis
Document understanding
Question-answering systems
Multilingual communication
Text analysis and processing
Language learning support
### Advantages
Simple and user-friendly interface.
Supports multiple AI-powered text-processing tasks.
Reduces the time required to summarize lengthy content.
Helps users understand the sentiment of text.
Supports question answering based on provided context.
Provides translation into multiple languages.
Can be accessed through a web browser after deployment.
### Limitations
Requires an internet connection to access the Gemini API.
API usage may be subject to rate limits and account-specific quotas.
Response quality depends on the input and the underlying AI model.
Generated answers may occasionally contain inaccurate information.
Translation quality may vary depending on the language and context.
Future Enhancements
The project can be improved with the following features:
PDF and document summarization.
Support for additional languages.
Conversation history and session management.
Downloadable output reports.
Improved input validation and error handling.
Speech-to-text and text-to-speech capabilities.
File upload support for text analysis.
Additional AI models and configurable generation settings.
### Conclusion
The AI-Powered LLM Toolkit demonstrates the integration of Large Language Models into a web-based application using Python, Streamlit, and Google's Gemini API.
The application provides text summarization, sentiment analysis, question answering, and text translation through a simple interface. It demonstrates the practical application of prompt engineering, API integration, natural language processing, and cloud deployment.
This project provides a foundation for developing more advanced AI-powered applications that simplify text-processing tasks and improve user productivity.
### Author
Developed as an AI and Large Language Model application project.
