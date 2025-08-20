from Website import Website
import ai.links

def get_all_details(homepage: Website) -> str:
    result = "Landing page:\n"
    result += homepage.get_contents()
    
    links = ai.links.get(homepage)
    
    print("Found links:", links)
    
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += Website(link["url"]).get_contents()
    
    return result