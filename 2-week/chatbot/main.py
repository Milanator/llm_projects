from openai import OpenAI
import gradio as gr
from api_key import setup_gpt

# python 2-week/chatbot/main.py

OPENAI_MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get."


def get_system_prompt(message: str) -> str:
    prompt = SYSTEM_PROMPT
    prompt += "\nIf the customer asks for shoes, you should respond that shoes are not on sale today, \
but remind the customer to look at hats!"

    # special occasion
    if "belt" in message:
        prompt += " The store does not sell belts; if you are asked for belts, be sure to point out other items on sale."

    return prompt


def send_message(message, history):
    messages = (
        [{"role": "system", "content": get_system_prompt(message)}]
        + history
        + [{"role": "user", "content": message}]
    )

    stream = OpenAI().chat.completions.create(
        model=OPENAI_MODEL, messages=messages, stream=True
    )

    response = ""

    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response


setup_gpt()


gr.ChatInterface(fn=send_message, type="messages").launch()
