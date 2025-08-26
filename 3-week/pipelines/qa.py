from huggingface import get_access_token
from huggingface_hub import login
from transformers import pipeline

# Question Answering with Context

# source venv/bin/activate
# python 3-week/pipelines/qa.py

login(get_access_token(), add_to_git_credential=True)

question_answerer = pipeline("question-answering")
result = question_answerer(
    question="Who was the 44th president of the United States?",
    context="Barack Obama was the 44th president of the United States.",
)

print(result)
