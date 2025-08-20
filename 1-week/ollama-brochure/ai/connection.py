import sys
import os
from openai import OpenAI
from dotenv import load_dotenv

MODEL = 'gpt-4o-mini'

# Open AI api key
def check_openai_api_key():
    """Load env"""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key and api_key.startswith('sk-proj-') and len(api_key) > 10:
        print("API key looks good so far")
    else:
        print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
        sys.exit(1)
        
    os.environ["OPENAI_API_KEY"] = api_key

def api_call(messages: list, as_json: bool = False):
    check_openai_api_key()

    params = {
        "model": MODEL,
        "messages": messages
    }

    # ak chcem JSON, pridám response_format
    if as_json:
        params["response_format"] = {"type": "json_object"}
    
    return OpenAI().chat.completions.create(**params)