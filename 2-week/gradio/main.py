import gradio as gr
from openai import OpenAI
from api_key import setup_gpt

# python 2-week/gradio/main.py

MODEL = "gpt-4o-mini"

INPUTS = [gr.Textbox(label="Your message", lines=6)]

OUTPUTS = [gr.Markdown(label="Response")]


def call_gpt(prompt: str):
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": prompt},
    ]

    stream = OpenAI().chat.completions.create(
        model=MODEL, messages=messages, stream=True
    )

    result = ""

    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


setup_gpt()

app = gr.Interface(fn=call_gpt, inputs=INPUTS, outputs=OUTPUTS, flagging_mode="never")
app.launch()
