import sys
from utils import get_all_details
import ai.brochure
import ai.translation
import traceback
from Website import Website

# source venv/bin/activate
# python 1-week/openai-brochure/main.py <URL> 

def main():
    try:
        """Missing arguments"""
        if len(sys.argv) < 2:
            sys.exit()
        
        url = sys.argv[1]
        
        homepage = Website(url)
        
        ai_links = ai.links.get(homepage)
        
        print(f"AI links: {ai_links}")
        
        details = get_all_details(homepage)
        
        markdown = ai.brochure.get_stream(url, details)
        
        with open("1-week/openai-brochure/output-en.md", "w", encoding="utf-8") as f:
            f.write(markdown)
            
        markdown = ai.translation.get_stream(markdown, 'German')
        
        with open("1-week/openai-brochure/output-de.md", "w", encoding="utf-8") as f:
            f.write(markdown)
        
    except Exception as e:
        traceback.print_exc()
    
if __name__ == "__main__":
    main()