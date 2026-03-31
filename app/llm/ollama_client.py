import requests

def call_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    response = requests.post(
        url,
        json={
            "model": "qwen2.5-coder:7b",
            "prompt": prompt,
            "stream": False
        }
    )

    print("DEBUG RESPONSE:", response.text)  # 👈 ADD THIS

    return response.json()["response"]