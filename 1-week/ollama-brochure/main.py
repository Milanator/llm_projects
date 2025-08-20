import sys
from utils import get_all_details
from ai.links import get_links
import ai.brochure
import traceback
from Website import Website

# source venv/bin/activate
# python 1-week/ollama-brochure/main.py <URL> 

def main():
    try:
        """Missing arguments"""
        if len(sys.argv) < 2:
            sys.exit()
        
        url = sys.argv[1]
        
        homepage = Website(url)
        
        ai_links = get_links(homepage)
        
        print(f"AI links: {ai_links}")
        
        # ai.brochure.create(url, get_all_details(homepage, url))
        
        markdown = ai.brochure.get_stream(url, get_all_details(homepage, url))
        
         # uložíme do súboru
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(markdown)
        
    except Exception as e:
        traceback.print_exc()
    
if __name__ == "__main__":
    main()