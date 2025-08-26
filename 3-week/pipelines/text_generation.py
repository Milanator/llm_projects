from huggingface import get_access_token
from huggingface_hub import login
from transformers import pipeline

# Text generation

# source venv/bin/activate
# python 3-week/pipelines/text_generation.py

login(get_access_token(), add_to_git_credential=True)

generator = pipeline("text-generation")
result = generator(
    "If there's one thing I want you to remember about using HuggingFace pipelines, it's"
)

print(result[0]["generated_text"])
