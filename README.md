# Echo – Offline Voice Chatbot using Ollama
A Local LLaMA 2 Based Voice Chatbot built using Python, Streamlit, and Ollama


---

## Overview

Echo is an offline voice-enabled chatbot built using **Python**, **Streamlit**, **LangChain**, and **Ollama**. The chatbot supports both text and voice interaction, allowing users to communicate naturally through a simple conversational interface.

The project uses the **LLaMA 2** model locally through Ollama, enabling chatbot responses without relying on cloud APIs or internet connectivity.

Echo integrates:
- Speech Recognition for voice input
- Text-to-Speech (TTS) for voice responses
- Local LLM execution using Ollama
- Streamlit-based user interface

This project demonstrates the implementation of a locally running conversational chatbot with voice interaction support.

---

# Features

- Offline Chatbot System
- Voice-based Interaction
- Text Input Support
- Local LLaMA 2 Integration
- Text-to-Speech Responses
- Streamlit User Interface
- No Cloud API Dependency
- No Internet Required for Responses
- Beginner-Friendly Project

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| Streamlit | Frontend User Interface |
| LangChain | LLM Workflow Integration |
| Ollama | Local Model Execution |
| LLaMA 2 | Conversational Language Model |
| SpeechRecognition | Voice Input Processing |
| pyttsx3 | Text-to-Speech Conversion |
| Threading | Parallel Task Handling |

---

# Project Structure

```bash
Ollama-Chatbot-main/
│
├── README.md
│
└── Ollama Chatbot/
    ├── chatbot.py
    └── Untitled.ipynb
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/Ollama-Chatbot.git
cd Ollama-Chatbot
```

---

## 2. Install Required Packages

```bash
pip install streamlit
pip install langchain
pip install langchain-community
pip install speechrecognition
pip install pyttsx3
pip install pyaudio
```

---

## 3. Install Ollama

Download and install Ollama from:

https://ollama.com

---

## 4. Pull the LLaMA 2 Model

```bash
ollama run llama2
```

---

# Run the Project

Navigate to the project folder and execute:

```bash
streamlit run chatbot.py
```

---

# How It Works

1. User provides text or voice input
2. SpeechRecognition converts voice into text
3. LangChain sends the query to Ollama
4. LLaMA 2 generates responses locally
5. pyttsx3 converts responses into speech
6. Streamlit displays the chatbot response in real-time

---

# Preview

## Home Interface

<img width="100%" alt="Home Interface" src="YOUR_SCREENSHOT_LINK_HERE"/>

---

## Voice Interaction

<img width="100%" alt="Voice Interaction" src="YOUR_SCREENSHOT_LINK_HERE"/>

---

## Chat Response Interface

<img width="100%" alt="Chat Response Interface" src="YOUR_SCREENSHOT_LINK_HERE"/>

---

## Voice Input Detection

<img width="100%" alt="Voice Input Detection" src="YOUR_SCREENSHOT_LINK_HERE"/>

---

## Streamlit UI

<img width="100%" alt="Streamlit UI" src="YOUR_SCREENSHOT_LINK_HERE"/>

---

# Future Improvements

- Chat History Support
- Multiple Model Integration
- Enhanced UI/UX
- Deployment Support
- Multilingual Voice Interaction
- Database Integration for Conversation Storage

---

# Learning Outcomes

This project helped in understanding:

- Conversational Chatbot Development
- Local LLM Integration
- Streamlit Application Development
- Voice Processing in Python
- Text-to-Speech Systems
- LangChain Workflow Integration

---

# Author

**Akshaya**  
B.E Artificial Intelligence and Machine Learning

---

# License

This project is developed for educational and learning purposes.
