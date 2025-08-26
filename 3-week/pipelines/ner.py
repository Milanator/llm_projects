from huggingface import get_access_token
from huggingface_hub import login
from transformers import pipeline

# name entity recognition

# source venv/bin/activate
# python 3-week/pipelines/ner.py

login(get_access_token(), add_to_git_credential=True)

ner = pipeline("ner", grouped_entities=True)
result = ner("Barack Obama was the 44th president of the United States.")

print(result)
