import sys
from scraper import scrape_website
from summarizer import summarize_text
from utils import load_api_key
import os

"""
source venv/bin/activate
python 1-week/openai-summarize-text/main.py <URL> 
"""

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    url = sys.argv[1]

    api_key = load_api_key()

    os.environ["OPENAI_API_KEY"] = api_key

    print(f"Web scraping: {url} ...")
    text = scrape_website(url)

    print("Summarizing content")
    summary = summarize_text(text)

    with open("1-week/openai-summarize-text/summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("Done! Output is stored in summary.txt")

if __name__ == "__main__":
    main()