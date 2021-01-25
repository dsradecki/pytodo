from dotenv import load_dotenv

import os

load_dotenv()

# MYSQL Config
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")
HOST = os.getenv("HOST")