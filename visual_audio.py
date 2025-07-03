import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np
plt.use('TkAgg')
# Load audio file
data, samplerate = sf.read(r'C:\Users\user\OneDrive\Desktop\GenAI Project\audio.wav')

# Create time axis
time = np.linspace(0, len(data) / samplerate, num=len(data))

# Plot the waveform
plt.figure(figsize=(12, 4))
plt.plot(time, data)
plt.title("Waveform of Audio File")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()
plt.show()
