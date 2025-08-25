import base64
from io import BytesIO
from PIL import Image
from openai import OpenAI
from api_key import setup_gpt

# python 2-week/image/main.py


def store_image(image_data: str):
    with open("2-week/image/output.png", "wb") as f:
        f.write(image_data)


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


setup_gpt()

artist("Bratislava")
