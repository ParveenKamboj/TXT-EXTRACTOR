import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22612474"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "6ffcf685477233f28dabb37ae5d03662")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "1282288388"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "1282288388").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://parveen:kamboj123@cluster0.ahvdclp.mongodb.net")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002323905325"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002323905325")  # Optional here you'll get all logs
