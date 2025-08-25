import requests

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"
OLLAMA_SYSTEM_PROMPT = "You are a very polite, courteous chatbot. You try to agree with \
everything the other person says, or find common ground. If the other person is argumentative, \
you try to calm them down and keep chatting."

def call_ollama(gpt_messages: list, ollama_message: list) -> str:
    messages = [{"role": "system", "content": OLLAMA_SYSTEM_PROMPT}]
    
    for gpt_message, ollama_message in zip(gpt_messages, ollama_message):
        messages.append({"role": "user", "content": gpt_message})
        messages.append({"role": "assistant", "content": ollama_message})
    
    messages.append({"role": "user", "content": gpt_messages[-1]})
    
    payload = {
        "model": MODEL,
        "stream": False,
        "messages": messages,
    }
    
    response = requests.post(OLLAMA_API, json = payload, headers = HEADERS)
    
    return response.json()['message']['content']