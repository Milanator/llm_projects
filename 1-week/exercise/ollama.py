import requests

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

def get_system_prompt() -> str:
    return "You are an assistant and try to me provide the best possible answer, which you can provide."

def get_user_prompt(question: str) -> str:
    user_prompt = f"Please answer me this question\n"
    user_prompt += question
    
    return user_prompt

def answer(question: str) -> str:
    response = requests.post(
        OLLAMA_API, 
        json = {
            "model": MODEL,
            "stream": False,
            "messages": [
                {
                    "role": "system", 
                    "content": get_system_prompt()
                },
                {
                    "role": "user", 
                    "content": get_user_prompt(question)
                }
            ],
        }, 
        headers = HEADERS
    )
        
    return response.json()['message']['content']