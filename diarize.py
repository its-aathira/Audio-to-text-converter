import whisperx

# Path to your audio file
audio_path = r"C:\Users\user\OneDrive\Desktop\GenAI Project\audio.wav"  # or use full path if needed

# Step 1: Load model and transcribe
print("⏳ Transcribing...")
model = whisperx.load_model("base", device="cpu", compute_type="int8")  # or "cuda" if you have a GPU
transcription = model.transcribe(audio_path)

# Step 2: Align timestamps (improves timing accuracy)
print("📌 Aligning timestamps...")
align_model, metadata = whisperx.load_align_model(language_code=transcription["language"], device="cpu")
transcription_aligned = whisperx.align(transcription["segments"], align_model, metadata, audio_path, device="cpu")

# Step 3: Diarize speakers
print("🧠 Performing speaker diarization...")
diarize_model = whisperx.load_diarization_model(device="cpu")
diarize_segments = diarize_model(audio_path)

# Step 4: Combine diarization + transcription
result = whisperx.merge_text_diarization(transcription_aligned["segments"], diarize_segments)

# Step 5: Print the output
print("\n🎙️ Final Transcript with Speakers:\n")
for segment in result:
    speaker = segment["speaker"]
    text = segment["text"]
    print(f"{speaker}: {text}")
