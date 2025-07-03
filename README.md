# AURALYZE - Audio Analyzer
# 🎧 Audio-to-Text Converter with Speaker Diarization

This is a GenAI project that transcribes audio into text and identifies **who spoke when** using **WhisperX** and **PyAnnote**. It also integrates **Groq + LLaMA3** to summarize the conversation and detect sentiment and satisfaction level.

---

## 🧠 Features

- 🔊 Transcribe audio files using WhisperX
- 🗣️ Perform speaker diarization with PyAnnote
- 💬 Generate summaries using LLaMA3 (Groq API)
- 🎯 Detect emotion and customer satisfaction

---

## 🛠️ Tech Stack

- `Python`
- `Streamlit` (UI)
- `WhisperX`
- `PyAnnote.audio`
- `Groq API` (LLaMA3 model)
- `dotenv` (for managing API keys)

---

### 1. Clone the Repo

```bash
git clone https://github.com/its-aathira/Audio-to-text-converter.git
cd Audio-to-text-converter

### 2. Create .env File
Create a .env file with your Hugging Face and Groq API tokens.
    HF_TOKEN=your_huggingface_token
    GROQ_API_KEY=your_groq_api_key
    👉 See .env.example for reference.

3. Set Up Virtual Environment
      python -m venv venv
      venv\Scripts\activate        # On Windows
      pip install -r requirements.txt

4. Run the App
      streamlit run app.py
