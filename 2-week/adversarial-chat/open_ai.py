import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

MODEL = 'gpt-4o-mini'
GPT_SYSTEM_PROMPT = "You are a chatbot who is very argumentative; \
you disagree with anything in the conversation and you challenge everything, in a snarky way."

# setup api key
def setup_gpt():
    # Load env
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key and api_key.startswith('sk-proj-') and len(api_key) > 10:
        print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
        sys.exit(1)
        
    os.environ["OPENAI_API_KEY"] = api_key

# request on openai
def call_gpt(gpt_messages: list, ollama_messages: list) -> str:
    messages = [{"role": "system", "content": GPT_SYSTEM_PROMPT}]
   
    for gpt, claude in zip(gpt_messages, ollama_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": claude})
   
    completion = OpenAI().chat.completions.create(
        model = MODEL,
        messages=messages
    )
   
    return completion.choices[0].message.content