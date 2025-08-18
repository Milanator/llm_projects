import sys
from scraper import scrape_website
from summarizer import summarize_text
from utils import store_file

# source venv/bin/activate
# python 1-week/ollama-summarize-text/main.py <URL> 

FILE_PATH = "1-week/ollama-summarize-text/summary.txt"

def main():
    """Missing arguments"""
    if len(sys.argv) < 2:
        sys.exit()
    
    url = sys.argv[1]
    
    print(f"Web scraping: {url} ...")
    text = scrape_website(url)
    
    print("Summarizing content")
    summary = summarize_text(text)
    
    print(f"Storing file {FILE_PATH}")
    store_file(FILE_PATH, summary)
    
if __name__ == "__main__":
    main()