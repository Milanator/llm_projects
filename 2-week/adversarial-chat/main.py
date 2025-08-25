from open_ai import setup_gpt
from open_ai import call_gpt
from ollama import call_ollama

"""
source venv/bin/activate
python 2-week/adversarial-chat/main.py
"""

def main():
    # starting conversions
    gpt_messages = ["Hi there"]
    ollama_messages = ["Hi"]
    
    setup_gpt()
    
    for i in range(5):
        gpt_next = call_gpt(gpt_messages, ollama_messages)
        print(f"GPT:\n{gpt_next}\n")
        gpt_messages.append(gpt_next)
        
        ollama_next = call_ollama(gpt_messages, ollama_messages)
        print(f"Ollama:\n{ollama_next}\n")
        ollama_messages.append(ollama_next)

if __name__ == "__main__":
    main()