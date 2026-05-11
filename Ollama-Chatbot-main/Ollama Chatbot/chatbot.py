from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import pyttsx3
import speech_recognition as sr
import threading  

# Set Animated Gradient Background with Normal Font
animated_gradient_bg = """
<style>
@keyframes gradientAnimation {
    0% { background: linear-gradient(45deg, #1e1e1e, #2c3e50); }
    25% { background: linear-gradient(45deg, #2c3e50, #8e44ad); }
    50% { background: linear-gradient(45deg, #8e44ad, #e74c3c); }
    75% { background: linear-gradient(45deg, #e74c3c, #f39c12); }
    100% { background: linear-gradient(45deg, #f39c12, #1e1e1e); }
}

[data-testid="stAppViewContainer"] {
    animation: gradientAnimation 5s infinite alternate;
    background-size: 200% 200%;
    color: #ffffff !important;
    font-family: 'Arial', sans-serif;
}

[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #1e1e1e, #2c3e50);
    color: #ffffff !important;
}

button {
    background-color: #000000 !important;
    color: #ffffff !important;
    border-radius: 10px;
    font-weight: bold;
    padding: 12px;
    border: 2px solid #00FFFF;
    box-shadow: 0px 0px 10px #00FFFF;
    transition: 0.2s;
}

button:hover {
    background-color: #111111 !important;
    box-shadow: 0px 0px 20px #00FFFF;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: #ffffff !important;
}
</style>
"""
st.markdown(animated_gradient_bg, unsafe_allow_html=True)

# Initialize TTS Engine
def init_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    voices = engine.getProperty('voices')
    if voices:
        engine.setProperty('voice', voices[0].id)
    return engine

engine = init_tts()

def speak(text):
    def run_speech():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run_speech, daemon=True).start()

# Function to Recognize Speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
            text = recognizer.recognize_google(audio)
            st.success(f"✅ Recognized: {text}")
            return text
        except sr.WaitTimeoutError:
            st.error("⏳ Timeout! No speech detected.")
            return ""
        except sr.UnknownValueError:
            st.error("❌ Could not understand audio.")
            return ""
        except sr.RequestError:
            st.error("❌ Speech service error. Check internet!")
            return ""

st.title("🤖 AI Chatbot with Animated Background")
st.write("Speak 🎙️ or type ⌨️ your query, and I will respond!")

if st.button("🎙️ Speak"):
    user_speech = recognize_speech()
else:
    user_speech = ""

input_txt = st.text_input("Enter your queries here...", value=user_speech)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant named Echo."),
    ("user", "User query: {query}")
])

llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if "response" not in st.session_state:
    st.session_state.response = None

if st.button("Send"):
    if input_txt.strip():
        st.session_state.response = chain.invoke({"query": input_txt})
        if st.session_state.response:
            st.write(st.session_state.response)
            speak(st.session_state.response)

if st.button("🔊 Speak Response"):
    if st.session_state.response:
        speak(st.session_state.response)
    else:
        st.warning("No response available yet. Please ask a question first!")
