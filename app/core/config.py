import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
mongo_url = os.getenv("MONGO_URL")