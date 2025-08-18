import requests

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

def summarize_text(text:str) -> str:
    payload = {
        "model": MODEL,
        "stream": False,
        "messages": [
            {"role": "system", "content": "You are an assistant that analyzes the contents of a website \
            and provides a short summary, ignoring text that might be navigation related. \
            Respond in markdown. Provide output text into markdown format."},
            {"role": "user", "content": text}
        ],
    }
    
    response = requests.post(OLLAMA_API, json = payload, headers = HEADERS)
        
    return response.json()['message']['content']