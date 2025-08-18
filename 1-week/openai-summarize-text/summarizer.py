from openai import OpenAI

def summarize_text(text: str, model: str = "gpt-4o-mini") -> str:
    """Získa sumarizáciu textu cez OpenAI API."""
    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown. Provide output text into markdown format."},
            {"role": "user", "content": text}
        ],
        temperature=0.5,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()