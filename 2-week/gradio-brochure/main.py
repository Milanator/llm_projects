import gradio as gr
from ollama import chat
from openai import OpenAI
from api_key import setup_gpt
from website import Website

# python 2-week/gradio-brochure/main.py

OLLAMA_MODEL = "llama3.2"
OPENAI_MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = "You are an assistant that analyzes the contents of a company website landing page \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in markdown."

INPUTS = [
    gr.Textbox(label="Company name"),
    gr.Textbox(label="Landing page url"),
    gr.Dropdown(["GPT", "Ollama"], label="Select model"),
]

OUTPUTS = [gr.Markdown(label="Response")]


def stream_gpt(prompt):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    stream = OpenAI().chat.completions.create(
        model=OPENAI_MODEL, messages=messages, stream=True
    )

    result = ""

    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


def stream_ollama(prompt):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    stream = chat(
        model=OLLAMA_MODEL,
        messages=messages,
        stream=True,
    )

    result = ""

    for chunk in stream:
        result += chunk["message"]["content"] or ""
        yield result


def get_user_prompt(company_name: str, url: str) -> str:
    prompt = f"Please generate a company brochure for {company_name}. Here is their landing page:\n"
    prompt += Website(url).get_contents()

    return prompt


def call_model(company_name: str, url: str, model: str):
    prompt = get_user_prompt(company_name, url)

    if model == "GPT":
        stream = stream_gpt(prompt)
    elif model == "Ollama":
        stream = stream_ollama(prompt)
    else:
        raise ValueError("Unknown model")

    yield from stream


setup_gpt()

app = gr.Interface(fn=call_model, inputs=INPUTS, outputs=OUTPUTS, flagging_mode="never")
app.launch()
