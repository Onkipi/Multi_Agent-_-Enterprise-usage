
import os
from dotenv import load_dotenv

load_dotenv()

config_list = [
    {
        "model":"gpt-4o",
        "api_key":os.getenv("OPENAI_API_KEY")
    }
]

llm_config = {
    "config_list":config_list,
    "temperature":0
}
