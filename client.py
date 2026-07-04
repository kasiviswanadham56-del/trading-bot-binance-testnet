from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def get_client():
    if (
        not API_KEY
        or not API_SECRET
        or API_KEY == "YOUR_BINANCE_TESTNET_API_KEY"
        or API_SECRET == "YOUR_BINANCE_TESTNET_API_SECRET"
    ):
        raise ValueError(
            "Testnet API credentials are missing. Please update the .env file."
        )

    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = "https://testnet.binancefuture.com"

    return client