import sys
import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
from api_key import setup_gpt

# python 2-week/gradio/main.py

MODEL = "gpt-4o-mini"

INPUTS = [gr.Textbox(label="Your message", lines=6)]

OUTPUTS = [gr.Textbox(label="Response", lines=9)]


def call_gpt(prompt: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": prompt},
    ]
    completion = OpenAI().chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return completion.choices[0].message.content


setup_gpt()

app = gr.Interface(fn=call_gpt, inputs=INPUTS, outputs=OUTPUTS, flagging_mode="never")
app.launch()
