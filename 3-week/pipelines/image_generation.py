import torch
from huggingface_hub import login
from diffusers import DiffusionPipeline
from huggingface import get_access_token
from huggingface_hub import login

# Image generation

# source venv/bin/activate
# python 3-week/pipelines/image_generation.py

login(get_access_token(), add_to_git_credential=True)

image_gen = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
).to("cuda")

text = "A class of Data Scientists learning about AI, in the surreal style of Salvador Dali"
image = image_gen(prompt=text).images[0]
image
