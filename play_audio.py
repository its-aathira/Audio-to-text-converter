import soundfile as sf
import simpleaudio as sa

# Load the audio file
data, samplerate = sf.read('audio.wav')
print(f"Sample rate: {samplerate}, Data shape: {data.shape}")

# Convert audio to proper format for playback
audio = (data * 32767).astype("int16")  # Convert float to int16
play_obj = sa.play_buffer(audio, 1, 2, samplerate)  # mono=1 channel, 2 bytes/sample
play_obj.wait_done()
