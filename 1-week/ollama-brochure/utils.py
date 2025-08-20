from Website import Website
from ai.links import get_links

def get_all_details(homepage: Website, url: str) -> str:
    result = "Landing page:\n"
    result += homepage.get_contents()
    
    links = get_links(homepage)
    
    print("Found links:", links)
    
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += Website(link["url"]).get_contents()
    
    return result