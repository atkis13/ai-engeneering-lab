import ollama

response = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": "say a cat joke"}]
)

print(response["message"]["content"])

#