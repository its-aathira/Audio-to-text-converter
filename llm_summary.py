import requests
import json

# Your Groq API key here
GROQ_API_KEY = "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"

# Read transcript from file
with open("final_output.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

# Define your prompt
prompt = f"""You are a smart assistant. Analyze the following conversation transcript:
{transcript}

1. Summarize the conversation clearly.
2. List the key topics discussed.
3. Identify each speaker's tone or emotion if possible.
4. Suggest a title for this conversation.

Be concise and informative."""

# Set up Groq API call
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

# Send the request
response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

# Parse and print response
if response.status_code == 200:
    reply = response.json()["choices"][0]["message"]["content"]
    print("✅ Summary & Analysis:\n")
    print(reply)

    # Optional: Save to file
    with open("llm_output.txt", "w", encoding="utf-8") as out:
        out.write(reply)

else:
    print("❌ Error:", response.status_code, response.text)
