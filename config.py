from dotenv import load_dotenv
from random import choice
from string import ascii_letters, digits
from os import getenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
BASE_WEBHOOK_URL = getenv("BASE_WEBHOOK_URL")
WEBHOOK_PATH = getenv("WEBHOOK_PATH") or "/webhook"
LOCAL_PORT = int(getenv("LOCAL_PORT")) or 8080
WEBHOOK_SECRET = getenv("WEBHOOK_SECRET") or ''.join(
    choice(ascii_letters + digits) for _ in rnage(30))
