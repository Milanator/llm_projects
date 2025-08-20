import json
from Website import Website
from ai.connection import api_call

# system prompt
def get_system_prompt() -> str:
    system_prompt = "You are provided with a list of links found on a webpage. \
    You are able to decide which of the links would be most relevant to include in a brochure about the company, \
    such as links to an About page, or a Company page, or Careers/Jobs pages.\n"
    system_prompt += "You should respond in JSON as in this example:"
    system_prompt += """
    {
        "links": [
            {"type": "about page", "url": "https://full.url/goes/here/about"},
            {"type": "careers page", "url": "https://another.full.url/careers"}
        ]
    }
    """
    
    return system_prompt

# user prompt
def get_user_prompt(page: Website):
    user_prompt = f"Here is the list of links on the website of {page.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(page.links)
  
    return user_prompt

# request call to Open AI
def get_links(page: Website) -> str:
    response = api_call([
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": get_user_prompt(page)}
    ], True)
    
    result = response.choices[0].message.content
    
    return json.loads(result)