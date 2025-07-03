from datetime import timedelta

# Your diarization segments (copy full list here)
diarization = [
    (1.0, 8.2, "SPEAKER_00"),
    (12.0, 15.8, "SPEAKER_01"),
    (16.2, 23.8, "SPEAKER_02"),
    (24.1, 28.9, "SPEAKER_01"),
    (29.2, 31.1, "SPEAKER_02"),
    (31.7, 35.4, "SPEAKER_01"),
    (35.8, 36.0, "SPEAKER_02"),
    (36.5, 37.7, "SPEAKER_01"),
    (38.1, 39.6, "SPEAKER_02"),
    (40.2, 42.2, "SPEAKER_01"),
    (42.4, 46.0, "SPEAKER_02"),
    (46.6, 48.6, "SPEAKER_01"),
    (48.8, 49.5, "SPEAKER_02"),
    (49.5, 54.6, "SPEAKER_01"),
    (55.0, 55.6, "SPEAKER_02"),
    (56.5, 59.5, "SPEAKER_01"),
    (60.0, 61.7, "SPEAKER_02"),
    (62.2, 65.7, "SPEAKER_01"),
    (66.2, 68.0, "SPEAKER_02"),
    (68.3, 72.9, "SPEAKER_01"),
    (73.2, 74.5, "SPEAKER_02"),
    (75.2, 78.7, "SPEAKER_01"),
    (78.9, 81.7, "SPEAKER_02"),
    (82.0, 85.9, "SPEAKER_01"),
    (86.1, 89.3, "SPEAKER_02"),
    (89.8, 90.5, "SPEAKER_01"),
    (91.6, 93.9, "SPEAKER_01"),
    (94.3, 99.0, "SPEAKER_02"),
    (99.6, 100.5, "SPEAKER_01"),
    (100.6, 103.2, "SPEAKER_02"),
    (103.7, 104.9, "SPEAKER_01"),
    (105.1, 109.0, "SPEAKER_02"),
    (109.6, 110.1, "SPEAKER_01"),
    (110.7, 121.1, "SPEAKER_01"),
    (121.4, 123.6, "SPEAKER_02"),
    (125.3, 127.0, "SPEAKER_02"),
    (127.9, 131.3, "SPEAKER_01"),
    (131.6, 133.8, "SPEAKER_02"),
    (134.7, 139.2, "SPEAKER_01"),
    (139.9, 153.0, "SPEAKER_02")
]

# Read the full transcript
with open("transcribed.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

# Naively split the text into as many parts as there are speaker segments
chunks = full_text.split(". ")  # Split into sentences first
num_segments = len(diarization)

# Combine short sentences to fit into segments
group_size = max(1, len(chunks) // num_segments)
merged_chunks = [" ".join(chunks[i:i+group_size]) for i in range(0, len(chunks), group_size)]

# Assign each merged chunk to a speaker
output = []
for i, (start, end, speaker) in enumerate(diarization):
    if i < len(merged_chunks):
        timestamp = f"{timedelta(seconds=start)} --> {timedelta(seconds=end)}"
        output.append(f"{speaker} [{timestamp}]: {merged_chunks[i].strip()}.")

# Save to final output file
with open("final_output.txt", "w", encoding="utf-8") as f:
    for line in output:
        f.write(line + "\n")

print("✅ Final output saved to 'final_output.txt'")
