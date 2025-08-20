from ai.connection import api_call

def get_system_prompt(language: str = 'Slovak') -> str:
    return f"You are an assistant that analyzes the contents of brochure for company. Only you need to do, please translate it into {language}."

def get_user_prompt(details: str):
    user_prompt = details
    user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
    
    return user_prompt
    
# translation
def get_stream(details: str, language: str) -> str:
    stream = api_call([
        {"role": "system", "content": get_system_prompt(language)},
        {"role": "user", "content": get_user_prompt(details)}
    ], False, True)
    
    response = ""
    
    # postupne čítame stream
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ''
        response += delta

    # odstránime markdown backticky, ak chceš
    return response.replace("```", "").replace("markdown", "")