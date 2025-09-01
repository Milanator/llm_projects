import sys
import os
from dotenv import load_dotenv


def get_access_token() -> str:
    """Load env"""
    load_dotenv()

    access_token = os.getenv("HUGGING_FACE_KEY")

    if not access_token:
        print(
            "There might be a problem with your API key? Please visit the troubleshooting notebook!"
        )
        sys.exit(1)

    return access_token
