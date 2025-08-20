import sys
import traceback
import open_ai
import ollama

# source venv/bin/activate
# python 1-week/exercise/main.py <QUESTION> 
# python 1-week/exercise/main.py "Please explain what this code does and why: yield from { book.get('author') for book in books book.get('author') }"

def main():
    try:
        """Missing arguments"""
        if len(sys.argv) < 2:
            sys.exit()
        
        question = sys.argv[1]
        
        openAiAnswer = open_ai.answer(question)
        
        with open("1-week/exercise/open_ai.md", "w", encoding="utf-8") as f:
            f.write(openAiAnswer)
            
        ollamaAnswer = ollama.answer(question)
        
        with open("1-week/exercise/ollama.md", "w", encoding="utf-8") as f:
            f.write(ollamaAnswer)
        
    except Exception as e:
        traceback.print_exc()
    
if __name__ == "__main__":
    main()