import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    """Stiahne a vyparsuje text zo zadanej URL."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # extract only texts
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
    text = "\n".join(paragraphs)

    return text