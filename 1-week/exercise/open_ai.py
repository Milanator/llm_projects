import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

MODEL = 'gpt-4o-mini'

def get_system_prompt() -> str:
    return "You are an assistant and try to me provide the best possible answer, which you can provide."

def get_user_prompt(question: str) -> str:
    user_prompt = f"Please answer me this question\n"
    user_prompt += question
    
    return user_prompt
    
# Open AI api key
def check_openai_api_key():
    """Load env"""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key and api_key.startswith('sk-proj-') and len(api_key) > 10:
        print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
        sys.exit(1)
        
    os.environ["OPENAI_API_KEY"] = api_key
    
    
def answer(question: str) -> str:
    check_openai_api_key()
    
    stream = OpenAI().chat.completions.create(
        model = MODEL,
        messages = [
            {"role": "system", "content": get_system_prompt()},
            {"role": "user", "content": get_user_prompt(question)}
        ], 
        stream = True
    )
    
    response = ""
    
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ''
        response += delta

    return response.replace("```", "").replace("markdown", "")