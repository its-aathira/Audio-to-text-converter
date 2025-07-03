import streamlit as st
import requests
import os 
from dotenv import load_dotenv

load_dotenv()
# === CONFIG ===
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# === PAGE CONFIG ===
st.markdown("""
    <style>
    html, body, .appview-container {
        background: linear-gradient(to right, #e3f2fd, #fce4ec) !important;
        background-attachment: fixed;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton > button {
        margin: 0.3rem;
        width: 100%;
        background-color: #e0f7fa;
        color: #00796b;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
        border: 2px solid #80deea;
        border-radius: 10px;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background-color: #b2ebf2;
    }
    .stTextArea textarea {
        background-color: #f7f7f7;
        border: 1px solid #ccc;
        transition: all 0.3s ease-in-out;
        border-radius: 8px;
    }
    .stTextArea textarea:focus {
        border-color: #64b5f6;
        box-shadow: 0 0 10px #bbdefb;
    }
    </style>
""", unsafe_allow_html=True)


st.title("🔊 AURALYZE - Audio Analyzer")
st.markdown("""
Hi! I am **Auralyze**, your audio analysis assistant. 
Please upload your audio file (in `.wav` format).
""")

# === FILE UPLOAD ===
audio_file = st.file_uploader("🎧 Attach your file", type=["wav", "mp3"])

# === TRANSCRIPT ===
if st.button("📝 Transcribe"):
    try:
        with open("final_output.txt", "r", encoding="utf-8") as f:
            transcript_lines = f.readlines()

        st.subheader("💬 Transcript View")

        for line in transcript_lines:
            if "SPEAKER_00" in line:
                st.markdown(f"<div style='background-color:#eeeeee;padding:10px;border-radius:10px;margin-bottom:5px; transition: all 0.3s ease-in-out;'><b>🎙 Narrator:</b> {line.split(':',1)[1].strip()}</div>", unsafe_allow_html=True)
            elif "SPEAKER_01" in line:
                st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:10px;margin-bottom:5px; transition: all 0.3s ease-in-out;'><b>🧑 Agent:</b> {line.split(':',1)[1].strip()}</div>", unsafe_allow_html=True)
            elif "SPEAKER_02" in line:
                st.markdown(f"<div style='background-color:#d0f0ff;padding:10px;border-radius:10px;margin-bottom:5px; transition: all 0.3s ease-in-out;'><b>👩 Customer:</b> {line.split(':',1)[1].strip()}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='background-color:#ffffff;padding:10px;border-radius:10px;margin-bottom:5px; transition: all 0.3s ease-in-out;'>{line.strip()}</div>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("⚠️ `final_output.txt` not found. Please generate the transcript first.")

# === FUNCTION TO CALL LLM ===
def query_llm(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error from Groq: {response.status_code}"

# === BUTTON LAYOUT ===
col1, col2 = st.columns(2)
with col1:
    if st.button("📄 Summarize"):
        try:
            with open("final_output.txt", "r", encoding="utf-8") as f:
                transcript = f.read()
            prompt = f"Summarize the following conversation in 5–7 lines:\n{transcript}"
            reply = query_llm(prompt)
            st.text_area("🧠 Summary", reply, height=300)
        except:
            st.error("Transcript file missing or API error.")

    if st.button("🏷 Title Suggestion"):
        try:
            with open("final_output.txt", "r", encoding="utf-8") as f:
                transcript = f.read()
            prompt = f"Suggest a one-line meaningful title for the following conversation:\n{transcript}"
            reply = query_llm(prompt)
            st.text_area("🏷 Suggested Title", reply, height=100)
        except:
            st.error("Transcript file missing or API error.")

with col2:
    if st.button("😊 Emotion Detector"):
        try:
            with open("final_output.txt", "r", encoding="utf-8") as f:
                transcript = f.read()
            prompt = f"Analyze the emotional tone of Narrator, Agent, and Customer in this transcript:\n{transcript}"
            reply = query_llm(prompt)
            st.text_area("😊 Emotion Analysis", reply, height=300)
        except:
            st.error("Transcript file missing or API error.")

    if st.button("📊 Customer Satisfaction Rating"):
        try:
            with open("final_output.txt", "r", encoding="utf-8") as f:
                transcript = f.read()
            prompt = f"Rate the customer's satisfaction in this transcript on a scale of 1–5 with explanation:\n{transcript}"
            reply = query_llm(prompt)
            st.text_area("📊 Satisfaction Level", reply, height=300)
        except:
            st.error("Transcript file missing or API error.")
