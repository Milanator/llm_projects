import tool
import base64
from io import BytesIO
from PIL import Image
from openai import OpenAI
import gradio as gr
from openai import OpenAI
from api_key import setup_gpt

# python 2-week/agent/main.py

OPENAI_MODEL = "gpt-4o-mini"


def store_image(image_data: str):
    with open("2-week/agent/output.png", "wb") as f:
        f.write(image_data)


def get_system_prompt() -> str:
    prompt = "You are a helpful assistant for an Airline called FlightAI. "
    prompt += "Give short, courteous answers, no more than 1 sentence. "
    prompt += "Always be accurate. If you don't know the answer, say so."

    return prompt


def chat(history):
    messages = [{"role": "system", "content": get_system_prompt()}] + history
    response = OpenAI().chat.completions.create(
        model=OPENAI_MODEL, messages=messages, tools=tool.get_tools()
    )
    image = None

    if response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        response, city = tool.handle_tool_call(message)

        messages.append(message)
        messages.append(response)

        image = artist(city)

        response = OpenAI().chat.completions.create(
            model=OPENAI_MODEL, messages=messages
        )

    reply = response.choices[0].message.content
    history += [{"role": "assistant", "content": reply}]

    return history, image


def artist(city):
    image_response = OpenAI().images.generate(
        model="dall-e-3",
        prompt=f"An image representing a vacation in {city}, showing tourist spots and everything unique about {city}, in a vibrant pop-art style",
        size="1024x1024",
        n=1,
        response_format="b64_json",
    )

    image_base64 = image_response.data[0].b64_json

    image_data = base64.b64decode(image_base64)

    store_image(image_data)

    return Image.open(BytesIO(image_data))


with gr.Blocks() as ui:
    with gr.Row():
        chatbot = gr.Chatbot(height=500, type="messages")
        image_output = gr.Image(height=500)
    with gr.Row():
        entry = gr.Textbox(label="Chat with our AI Assistant:")
    with gr.Row():
        clear = gr.Button("Clear")

    def do_entry(message, history):
        history += [{"role": "user", "content": message}]
        return "", history

    entry.submit(do_entry, inputs=[entry, chatbot], outputs=[entry, chatbot]).then(
        chat, inputs=chatbot, outputs=[chatbot, image_output]
    )
    clear.click(lambda: None, inputs=None, outputs=chatbot, queue=False)

setup_gpt()

ui.launch(inbrowser=True)
