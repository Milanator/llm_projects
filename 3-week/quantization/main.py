from huggingface import get_access_token
from huggingface_hub import login
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TextStreamer,
    BitsAndBytesConfig,
)
import torch
import gc
import os

# source venv/bin/activate
# python 3-week/quantization/main.py

LLAMA_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct"
MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant"},
    {
        "role": "user",
        "content": "Tell a light-hearted joke for a room of Data Scientists",
    },
]

login(get_access_token(), add_to_git_credential=True)

# config - 4 bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
)


def generate(model, messages):
    # getting and setup tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model)
    tokenizer.pad_token = tokenizer.eos_token

    # put into model chat template format
    inputs = tokenizer.apply_chat_template(
        messages, return_tensors="pt", add_generation_prompt=True
    )

    # setup streamer for streaming result
    streamer = TextStreamer(tokenizer)

    # quantization of specified model - decrease weight precision
    model = AutoModelForCausalLM.from_pretrained(
        model, device_map="auto", quantization_config=quantization_config
    )

    outputs = model.generate(inputs, max_new_tokens=80, streamer=streamer)

    del model, inputs, tokenizer, outputs, streamer

    gc.collect()

    torch.cuda.empty_cache()


generate(LLAMA_MODEL, MESSAGES)
