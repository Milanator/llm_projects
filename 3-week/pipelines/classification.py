from huggingface import get_access_token
from huggingface_hub import login
from transformers import pipeline

# Classification

# source venv/bin/activate
# python 3-week/pipelines/classification.py

login(get_access_token(), add_to_git_credential=True)

classifier = pipeline("zero-shot-classification")
result = classifier(
    "Hugging Face's Transformers library is amazing!",
    candidate_labels=["technology", "sports", "politics"],
)

print(result)
