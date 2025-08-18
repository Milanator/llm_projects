from dotenv import load_dotenv
import os
import sys

def load_api_key():
    """Load env"""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ OPENAI_API_KEY not found in .env")
        sys.exit(1)
    
    return api_key