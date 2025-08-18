import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    response = requests.get(url, timeout = 10)
    response.raise_for_status()
    
    parser = BeautifulSoup(response.text, "html.parser")
    
    paragraphs = [p.get_text(strip = True) for p in parser.find_all('p')]
    
    return "\n".join(paragraphs)
    
    