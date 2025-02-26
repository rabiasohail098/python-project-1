import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from gtts import gTTS
import base64

# Load API Key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini AI Initialize Karo
genai.configure(api_key=api_key)

# Function: AI Response Generate Karna
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Function: Text Ko Speech Me Convert Karna
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")  # English me voice generate karega
    audio_file = "response.mp3"
    tts.save(audio_file)
    return audio_file

# Streamlit UI
st.title("🤖 AI Chatbot with Voice")
user_input = st.text_input("Ask me anything:")

if st.button("Generate Response"):
    if user_input:
        # Gemini AI ka Response Lo
        response = get_gemini_response(user_input)
        st.write(response)

        # Voice Generate Karo
        audio_file = text_to_speech(response)

        # Audio Ko Play Karne Ke Liye Encode Karo
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3")

    else:
        st.warning("Please enter a question.")
