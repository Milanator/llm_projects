from huggingface import get_access_token
from huggingface_hub import login
from transformers import pipeline

# Text Summarization

# source venv/bin/activate
# python 3-week/pipelines/text_summarization.py

login(get_access_token(), add_to_git_credential=True)

# summarizer = pipeline("summarization", device="cuda")
summarizer = pipeline("summarization")
text = """The Hugging Face transformers library is an incredibly versatile and powerful tool for natural language processing (NLP).
It allows users to perform a wide range of tasks such as text classification, named entity recognition, and question answering, among others.
It's an extremely popular library that's widely used by the open-source data science community.
It lowers the barrier to entry into the field by providing Data Scientists with a productive, convenient way to work with transformer models.
"""
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)

print(summary[0]["summary_text"])
