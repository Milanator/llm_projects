from huggingface import get_access_token
from huggingface_hub import login
from transformers import AutoTokenizer

# source venv/bin/activate
# python 3-week/tokenizers/main.py

PHI3_MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
QWEN2_MODEL_NAME = "Qwen/Qwen2-7B-Instruct"
STARCODER2_MODEL_NAME = "bigcode/starcoder2-3b"

MODEL = "meta-llama/Meta-Llama-3.1-8B"

login(get_access_token(), add_to_git_credential=True)

tokenizer = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)

text = "I am excited to show Tokenizers in action to my LLM engineers"

# encode text to tokens
tokens = tokenizer.encode(text)

print(tokens)

# decode text from tokens
print(tokenizer.decode(tokens))

# decode text from tokens to array
tokenizer.batch_decode(tokens)

# token and expression mapping
tokenizer.vocab

# special vocabs
tokenizer.get_added_vocab()
