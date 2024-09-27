# test_env.py
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("EXCHANGE_RATE_API_KEY")
print(f"API Key: {api_key}")
