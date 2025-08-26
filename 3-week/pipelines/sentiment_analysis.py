from huggingface import get_access_token
from huggingface_hub import login
from transformers import pipeline

# Sentiment Analysis

# source venv/bin/activate
# python 3-week/pipelines/sentiment_analysis.py

login(get_access_token(), add_to_git_credential=True)

classifier = pipeline("sentiment-analysis")
result = classifier("I'm super excited to be on the way to LLM mastery!")

print(result)
