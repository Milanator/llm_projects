from IPython.display import Markdown, display, update_display
from ai.connection import api_call

def get_system_prompt() -> str:
    return "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown.\
Include details of company culture, customers and careers/jobs if you have the information."

def get_brochure_user_prompt(company_name, details):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    user_prompt += details
    user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
    
    return user_prompt

def create_brochure(company_name, details):
    response = api_call([
        {"role": "system", "content": get_system_prompt()},
        {"role": "user", "content": get_brochure_user_prompt(company_name, details)}
    ])
    
    result = response.choices[0].message.content
    
    display(Markdown(result))