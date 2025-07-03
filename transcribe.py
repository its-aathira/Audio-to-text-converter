import whisper

print("⏳ Loading model...")
model = whisper.load_model("base")

print("🎙️ Starting transcription...")
result = model.transcribe(r"C:\Users\user\OneDrive\Desktop\GenAI Project\audio.wav")

print("✅ Transcription completed.\n")
print("Transcribed Text:\n")
print(result["text"])
