import os
import sys
import parser
import ai
import traceback
from IPython.display import Markdown, display, update_display
from openai import OpenAI

# source venv/bin/activate
# python 1-week/ollama-brochure/main.py <URL> 

def main():
    try:
        """Missing arguments"""
        if len(sys.argv) < 2:
            sys.exit()
        
        url = sys.argv[1]
        
        page = parser.parse_page(url)
        
        print("Parsing")
        
        title = parser.get_title(page)
        
        print(f"Title: {title}")
        
        text = parser.get_text(page)
        
        print(f"Text: {text}")
        
        links = parser.get_links(page)
        
        ai_links = ai.get_links({"links": links, "title": title, "url": url})
        
        print(f"AI links: {ai_links}")
        
    except Exception as e:
        traceback.print_exc()
    
if __name__ == "__main__":
    main()