import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
que = {}
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5520909793").split()))
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
LOG_GROUP = getenv("LOG_GROUP", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_USERNAME = getenv("SPOTIFY_USERNAME", "")
MONGO_DB = getenv("MONGO_DB", "")
ALIVE_IMG = getenv("ALIVE_IMG", "")
DB_URL = getenv("DATABASE_URL", "")
STRING_SESSION = getenv("STRING_SESSION", "")
