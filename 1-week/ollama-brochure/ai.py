import os
import sys
import json
from openai import OpenAI
from dotenv import load_dotenv

MODEL = 'gpt-4o-mini'

# Open AI api key
def get_api_key():
    """Load env"""
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key and api_key.startswith('sk-proj-') and len(api_key) > 10:
        print("API key looks good so far")
    else:
        print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
        sys.exit(1)
    
    return api_key

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
def get_user_prompt(website:object):
    user_prompt = f"Here is the list of links on the website of {website['url']} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website['links'])
    return user_prompt

# request call to Open AI
def get_links(website: object) -> str:
    os.environ["OPENAI_API_KEY"] = get_api_key()
    
    openai = OpenAI()
    
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": get_system_prompt()},
            {"role": "user", "content": get_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    
    return json.loads(result)