from dotenv import load_dotenv

import os

load_dotenv()

# MYSQL Config
USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
DB = os.getenv("MYSQL_DB")
HOST = os.getenv("MYSQL_HOST")