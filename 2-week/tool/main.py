import tool
from openai import OpenAI
import gradio as gr
from api_key import setup_gpt

# python 2-week/tool/main.py

OPENAI_MODEL = "gpt-4o-mini"


def get_system_prompt() -> str:
    prompt = "You are a helpful assistant for an Airline called FlightAI. "
    prompt += "Give short, courteous answers, no more than 1 sentence. "
    prompt += "Always be accurate. If you don't know the answer, say so."

    return prompt


def api_call():
    return OpenAI().chat.completions


def chat(message, history):
    messages = (
        [{"role": "system", "content": get_system_prompt()}]
        + history
        + [{"role": "user", "content": message}]
    )
    response = api_call().create(
        model=OPENAI_MODEL, messages=messages, tools=tool.get_tools()
    )

    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response, city = tool.handle_tool_call(message)
        messages.append(message)
        messages.append(response)

        response = api_call().create(model=OPENAI_MODEL, messages=messages)

    print(f"{messages}")

    return response.choices[0].message.content


setup_gpt()

gr.ChatInterface(fn=chat, type="messages").launch()
