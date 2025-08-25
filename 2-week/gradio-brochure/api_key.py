import sys
import os
from dotenv import load_dotenv


# setup api key
def setup_gpt():
    # Load env
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key and api_key.startswith("sk-proj-") and len(api_key) > 10:
        print(
            "There might be a problem with your API key? Please visit the troubleshooting notebook!"
        )
        sys.exit(1)

    os.environ["OPENAI_API_KEY"] = api_key
