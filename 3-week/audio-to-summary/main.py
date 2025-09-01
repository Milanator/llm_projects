# source venv/bin/activate
# python 3-week/audio-to-summary/main.py

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

CHAT_MODEL = "gpt-4o-mini"
AUDIO_MODEL = "whisper-1"
AUDIO = "3-week/audio-to-summary/na_lasku_nam_staci_mono.mp3"

openaiClient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_messages(transcript: str) -> list:
    return [
        {
            "role": "system",
            "content": "You are a helpful assistant. Summarize main thought of songs in slovak slovak language.",
        },
        {"role": "user", "content": f"{transcript}"},
    ]


def get_summary(messages: str):
    response = OpenAI().chat.completions.create(
        model=CHAT_MODEL, messages=messages, temperature=0.5, max_tokens=100
    )

    return response.choices[0].message.content.strip()


def get_transcript() -> str:
    with open(AUDIO, "rb") as file:
        transcript = openaiClient.audio.transcriptions.create(
            model=AUDIO_MODEL, file=file
        )

    return transcript.text


transcript = get_transcript()
messages = get_messages(transcript)
summary = get_summary(messages)

print(summary)
