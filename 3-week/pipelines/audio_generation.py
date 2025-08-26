from huggingface import get_access_token
from huggingface_hub import login
from transformers import pipeline

# Audio generation

# source venv/bin/activate
# python 3-week/pipelines/audio_generation.py

login(get_access_token(), add_to_git_credential=True)

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts", device="cuda")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

speech = synthesiser(
    "Hi to an artificial intelligence engineer, on the way to mastery!",
    forward_params={"speaker_embeddings": speaker_embedding},
)

sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])
Audio("speech.wav")
