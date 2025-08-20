import requests
from bs4 import BeautifulSoup

HEADERS = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

def parse_page(url: str) -> BeautifulSoup:
    response = requests.get(url, headers = HEADERS)
    body = response.content
    
    return BeautifulSoup(body, 'html.parser')


# getting links
def get_links(page: BeautifulSoup) -> list:    
    links = [link.get('href') for link in page.find_all('a')]
    
    return [link for link in links if link]


# getting texts
def get_text(page: BeautifulSoup) -> list:    
    if page.body:
        for irrelevant in page.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = page.body.get_text(separator="\n", strip=True)
    else:
        text = ""
        
    return text


# getting title
def get_title(page: BeautifulSoup) -> list:    
    return page.title.string if page.title else "No title found"