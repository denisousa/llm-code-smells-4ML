from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_client_openai():
    return OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

def get_client_lm_studio():
    return OpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
    )


def get_azure_client():
    GPT4_KEY = os.getenv("GPT4_KEY")
    AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
    return AzureOpenAI(api_key=GPT4_KEY,
                azure_endpoint=AZURE_ENDPOINT,
                api_version="2024-02-15-preview")