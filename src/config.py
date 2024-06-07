from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_CONNECTION_URI = os.environ.get("DATABASE_URL")
